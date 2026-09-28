"""Durable component → 21 Judge → score → AtomicStageCourtV2 pipeline."""

from __future__ import annotations

from dataclasses import dataclass, replace
import json
import os
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.researcher_mode.schemas import (
    CANONICAL_COMPONENT_ORDER,
    ComponentAnchor,
    ComponentJudgeDecision,
    ComponentResearchMemo,
    EvidenceFact,
)
from e2r.research_brain.scoring import (
    CreditValidatedImpact,
    EventOverlayInput,
    FullScoreValidityEvidenceV2,
)

from ..atomic_io import fsync_directory
from ..ids import canonical_hash, canonical_json, stable_id
from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob, ResearchMode
from ..gaps.supplemental_service import (
    load_effective_verified_evidence,
    resolved_supplemental_gap_keys,
)
from ..reuse import DeltaScoringReuseContext
from ..multi_pass import load_effective_research_dossier
from ..state_machine import TransitionContext
from .component_bridge import (
    ComponentBridgeResult,
    ProComponentMemoCompiler,
    evidence_fact_from_mapping,
)
from .judge_bridge import (
    EvidenceOnlyJudgeProvider,
    JudgeBridgeResult,
    JudgeCallReceipt,
    ProEvidenceOnlyJudgeBridge,
)
from .publication_gate import (
    FullThesisEligibilityReceipt,
    FullThesisPublicationGate,
    ResearchEligibilityDecision,
    research_incomplete_result,
    validate_full_thesis_eligibility_receipt,
)
from .scorer_bridge import CalibratedScoreBridgeResult, ProCalibratedScorerBridge
from .stagecourt_bridge import ProAtomicStageCourtBridge, StageCourtBridgeResult


@dataclass(frozen=True)
class ProScoringPipelineRun:
    job: ProResearchJob
    component_result: ComponentBridgeResult | None
    judge_result: JudgeBridgeResult | None
    score_result: CalibratedScoreBridgeResult | None
    stagecourt_result: StageCourtBridgeResult | None
    score_receipt: Mapping[str, Any] | None
    stagecourt_receipt: Mapping[str, Any] | None
    reuse_receipt: Mapping[str, Any]
    scoring_root: Path
    research_eligibility: ResearchEligibilityDecision | None = None
    full_thesis_eligibility: FullThesisEligibilityReceipt | None = None
    research_incomplete_result: Mapping[str, Any] | None = None


@dataclass(frozen=True)
class _DeltaResolvedInputs:
    facts: tuple[EvidenceFact, ...]
    source_verifications: tuple[Mapping[str, Any], ...]
    claim_fact_links: tuple[Mapping[str, Any], ...]
    validated_impacts: tuple[CreditValidatedImpact, ...]
    terminal_evidence: Mapping[str, Mapping[str, Any]]
    prior_memos: tuple[ComponentResearchMemo, ...]
    prior_judges: JudgeBridgeResult
    prior_facts: tuple[EvidenceFact, ...]
    prior_gap_decisions: tuple[Mapping[str, Any], ...]
    prior_impacts: tuple[CreditValidatedImpact, ...]
    prior_terminal_evidence: Mapping[str, Mapping[str, Any]]


class ProScoringPipelineService:
    def __init__(self, store: ProFirstJobStore) -> None:
        self.store = store

    def run_job(
        self,
        job_id: str,
        *,
        job_root: str | Path,
        selected_archetype_id: str,
        judge_provider: EvidenceOnlyJudgeProvider | None,
        historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
        validated_impacts: Sequence[CreditValidatedImpact],
        terminal_evidence: Mapping[str, Mapping[str, Any]],
        validity_evidence: FullScoreValidityEvidenceV2,
        event_overlay_input: EventOverlayInput | None = None,
        hard_break_claim_ids: Sequence[str] = (),
        research_saturation_receipt: Mapping[str, Any] | None = None,
        delta_reuse_context: DeltaScoringReuseContext | None = None,
    ) -> ProScoringPipelineRun:
        root = Path(job_root).resolve()
        scoring_root = root / "scoring"
        score_receipt_path = scoring_root / "score_receipt.json"
        stage_receipt_path = scoring_root / "stagecourt_receipt.json"
        reuse_receipt_path = scoring_root / "reuse_receipt.json"
        research_gate_path = scoring_root / "research_eligibility_receipt.json"
        full_gate_path = scoring_root / "full_thesis_eligibility_receipt.json"
        incomplete_result_path = scoring_root / "research_incomplete_result.json"
        job = self.store.get_job(job_id)
        if job.status == JobStatus.FINAL.value:
            durable_score = self.store.get_score_receipt(job_id)
            durable_stage = self.store.get_stagecourt_receipt(job_id)
            reuse_receipt = (
                _read_json(reuse_receipt_path)
                if reuse_receipt_path.is_file()
                else None
            )
            if (
                durable_score is None
                or durable_stage is None
                or not score_receipt_path.is_file()
                or not stage_receipt_path.is_file()
                or not reuse_receipt_path.is_file()
                or not full_gate_path.is_file()
                or canonical_json(_read_json(score_receipt_path))
                != canonical_json(durable_score)
                or canonical_json(_read_json(stage_receipt_path))
                != canonical_json(durable_stage)
                or reuse_receipt is None
                or not _reuse_receipt_is_valid(
                    reuse_receipt,
                    expected_job_id=job_id,
                    require_complete=True,
                )
                or canonical_json(reuse_receipt)
                != canonical_json(durable_score.get("reuse_receipt") or {})
            ):
                raise ValueError("FINAL scoring artifacts differ from the durable ledger")
            full_gate = _read_json(full_gate_path)
            validate_full_thesis_eligibility_receipt(
                full_gate,
                expected_job_id=job_id,
            )
            if (
                durable_score.get("full_thesis_eligibility_hash")
                != full_gate.get("eligibility_hash")
                or canonical_json(
                    durable_score.get("full_thesis_eligibility") or {}
                )
                != canonical_json(full_gate)
            ):
                raise ValueError("FINAL score is detached from full-thesis eligibility")
            return ProScoringPipelineRun(
                job=job,
                component_result=None,
                judge_result=None,
                score_result=None,
                stagecourt_result=None,
                score_receipt=durable_score,
                stagecourt_receipt=durable_stage,
                reuse_receipt=reuse_receipt,
                scoring_root=scoring_root,
                full_thesis_eligibility=_full_eligibility_from_mapping(full_gate),
            )
        if job.status not in {
            JobStatus.COMPONENT_RESEARCH.value,
            JobStatus.JUDGING.value,
            JobStatus.SCORING.value,
            JobStatus.STAGECOURT.value,
        }:
            raise ValueError("job is outside the component/Judge scoring boundary")
        if (
            job.mode == ResearchMode.DELTA_RESEARCH.value
            and delta_reuse_context is None
        ):
            raise ValueError("DELTA_RESEARCH scoring requires an explicit prior-job context")
        if (
            job.mode != ResearchMode.DELTA_RESEARCH.value
            and delta_reuse_context is not None
        ):
            raise ValueError("delta reuse context is only valid for DELTA_RESEARCH")
        dossier = load_effective_research_dossier(root)
        fact_rows, claim_fact_links, source_verifications = (
            load_effective_verified_evidence(root)
        )
        facts = tuple(evidence_fact_from_mapping(row) for row in fact_rows)
        resolved_gap_keys = resolved_supplemental_gap_keys(root)
        gap_decisions = tuple(
            row
            for row in self.store.get_gap_decisions(job_id)
            if str(row.get("evidence_gap_key") or "") not in resolved_gap_keys
        )
        delta_inputs = None
        effective_impacts = tuple(validated_impacts)
        effective_terminal_evidence = dict(terminal_evidence)
        if delta_reuse_context is not None:
            delta_inputs = self._resolve_delta_inputs(
                job=job,
                context=delta_reuse_context,
                current_facts=facts,
                current_source_verifications=source_verifications,
                current_claim_fact_links=claim_fact_links,
                current_impacts=effective_impacts,
                current_terminal_evidence=effective_terminal_evidence,
            )
            facts = delta_inputs.facts
            source_verifications = delta_inputs.source_verifications
            claim_fact_links = delta_inputs.claim_fact_links
            effective_impacts = delta_inputs.validated_impacts
            effective_terminal_evidence = dict(delta_inputs.terminal_evidence)
        saturation_path = root / "saturation/research_saturation_receipt.json"
        effective_saturation_receipt = research_saturation_receipt
        if effective_saturation_receipt is None and saturation_path.is_file():
            effective_saturation_receipt = _read_json(saturation_path)
        research_eligibility = FullThesisPublicationGate().evaluate_research(
            job=job,
            dossier=dossier,
            selected_archetype_id=selected_archetype_id,
            saturation_receipt=effective_saturation_receipt,
            evidence_facts=facts,
            claim_fact_links=claim_fact_links,
        )
        self._write_json_atomic(
            research_gate_path,
            research_eligibility.to_dict(),
        )
        if not research_eligibility.component_entry_allowed:
            if job.status != JobStatus.COMPONENT_RESEARCH.value:
                raise ValueError(
                    "research saturation became invalid after component entry"
                )
            incomplete = research_incomplete_result(
                research_eligibility,
                current_verified_fact_ids=tuple(row.fact_id for row in facts),
            )
            self._write_json_atomic(incomplete_result_path, incomplete)
            reuse_receipt = {
                "schema_version": "e2r_pro_scoring_reuse_receipt_v1",
                "status": "RESEARCH_INCOMPLETE",
                "job_id": job_id,
                "scoring_query_count": 0,
                "scoring_fetch_count": 0,
                "research_eligibility_hash": research_eligibility.decision_hash,
            }
            return ProScoringPipelineRun(
                job=job,
                component_result=None,
                judge_result=None,
                score_result=None,
                stagecourt_result=None,
                score_receipt=None,
                stagecourt_receipt=None,
                reuse_receipt=reuse_receipt,
                scoring_root=scoring_root,
                research_eligibility=research_eligibility,
                research_incomplete_result=incomplete,
            )
        component = ProComponentMemoCompiler().compile(
            dossier=dossier,
            job=job,
            selected_archetype_id=selected_archetype_id,
            verified_facts=facts,
            source_verifications=source_verifications,
            claim_fact_links=claim_fact_links,
            gap_decisions=gap_decisions,
            historical_anchors=historical_anchors,
        )
        if delta_inputs is not None and delta_reuse_context is not None:
            component, changed_components, reused_components = (
                self._resolve_delta_components(
                    job=job,
                    current_component=component,
                    facts=facts,
                    current_gap_decisions=gap_decisions,
                    current_impacts=effective_impacts,
                    terminal_evidence=effective_terminal_evidence,
                    delta_inputs=delta_inputs,
                    context=delta_reuse_context,
                )
            )
        else:
            changed_components = tuple(CANONICAL_COMPONENT_ORDER)
            reused_components = ()
        component_rows = [row.to_dict() for row in component.memos]
        component_receipt = {
            **component.receipt_payload,
            "job_id": job_id,
            "component_memos_hash": canonical_hash(component_rows),
        }
        self._write_or_verify_jsonl(
            scoring_root / "component_memos.jsonl",
            component_rows,
        )
        self._write_or_verify_json(
            scoring_root / "component_bridge_receipt.json",
            component_receipt,
        )
        if job.status == JobStatus.COMPONENT_RESEARCH.value:
            job = self.store.transition(
                job_id,
                expected_version=job.state_version,
                to_status=JobStatus.JUDGING,
                actor="pro-component-bridge",
                idempotency_key=f"component-bridge:{canonical_hash(component.receipt_payload)}",
                context=TransitionContext(
                    component_coverage_complete=True,
                    research_saturation_valid=True,
                ),
                payload={"component_count": len(component.memos)},
            )
        judges = self._load_complete_judges(
            scoring_root=scoring_root,
            job_id=job_id,
        )
        if judges is None:
            pre_score_judge_recovery = (
                job.status == JobStatus.SCORING.value
                and self.store.get_score_receipt(job_id) is None
                and self.store.get_stagecourt_receipt(job_id) is None
            )
            if (
                job.status != JobStatus.JUDGING.value
                and not pre_score_judge_recovery
            ):
                raise ValueError(
                    "durable 21-Judge artifacts are required after JUDGING"
                )
            if delta_inputs is None:
                judges = ProEvidenceOnlyJudgeBridge(judge_provider).run(
                    memos=component.memos,
                    evidence_facts=facts,
                    historical_anchors=historical_anchors,
                    gap_decisions=gap_decisions,
                    response_cache_root=scoring_root / "judge_response_cache",
                )
            else:
                changed_judges = ProEvidenceOnlyJudgeBridge(judge_provider).run(
                    memos=component.memos,
                    evidence_facts=facts,
                    historical_anchors=historical_anchors,
                    gap_decisions=gap_decisions,
                    component_ids=changed_components,
                    response_cache_root=scoring_root / "judge_response_cache",
                )
                judges = _combine_delta_judges(
                    prior=delta_inputs.prior_judges,
                    changed=changed_judges,
                    changed_component_ids=changed_components,
                )
            judge_decision_rows = [row.to_dict() for row in judges.decisions]
            judge_call_rows = [row.to_dict() for row in judges.call_receipts]
            judge_receipt = _judge_bridge_receipt(
                job_id=job_id,
                judges=judges,
                decision_rows=judge_decision_rows,
                call_rows=judge_call_rows,
            )
            self._write_jsonl_atomic(
                scoring_root / "judge_decisions.jsonl",
                judge_decision_rows,
            )
            self._write_jsonl_atomic(
                scoring_root / "judge_calls.jsonl",
                judge_call_rows,
            )
            self._write_json_atomic(
                scoring_root / "judge_bridge_receipt.json",
                judge_receipt,
            )
        else:
            judge_receipt = _read_json(
                scoring_root / "judge_bridge_receipt.json"
            )
        reuse_receipt = _build_reuse_receipt(
            job=job,
            context=delta_reuse_context,
            changed_component_ids=changed_components,
            reused_component_ids=reused_components,
            judges=judges,
        )
        self._write_or_progress_reuse_receipt(reuse_receipt_path, reuse_receipt)
        if not judges.score_valid:
            return ProScoringPipelineRun(
                job=job,
                component_result=component,
                judge_result=judges,
                score_result=None,
                stagecourt_result=None,
                score_receipt=None,
                stagecourt_receipt=None,
                reuse_receipt=reuse_receipt,
                scoring_root=scoring_root,
                research_eligibility=research_eligibility,
            )
        full_thesis_eligibility = FullThesisPublicationGate().evaluate_full_thesis(
            research=research_eligibility,
            memos=component.memos,
            judges=judges,
            evidence_facts=facts,
            claim_fact_links=claim_fact_links,
            validated_impacts=effective_impacts,
        )
        full_thesis_eligibility_payload = full_thesis_eligibility.to_dict()
        self._write_or_verify_json(full_gate_path, full_thesis_eligibility_payload)
        if job.status == JobStatus.JUDGING.value:
            job = self.store.transition(
                job_id,
                expected_version=job.state_version,
                to_status=JobStatus.SCORING,
                actor="pro-judge-bridge",
                idempotency_key=(
                    f"judge-complete:{canonical_hash(judges.receipt_payload)}"
                ),
                context=TransitionContext(judge_coverage_complete=True),
                payload={"judge_decision_count": len(judges.decisions)},
            )
        accepted_claim_ids = tuple(
            dict.fromkeys(
                str(row.get("claim_id") or "")
                for row in claim_fact_links
                if str(row.get("claim_id") or "")
            )
        )
        accepted_claim_fact_ids: dict[str, list[str]] = {}
        for row in claim_fact_links:
            claim_id = str(row.get("claim_id") or "")
            fact_id = str(row.get("fact_id") or "")
            if claim_id and fact_id:
                accepted_claim_fact_ids.setdefault(claim_id, []).append(fact_id)
        score_result = ProCalibratedScorerBridge().score(
            selected_archetype_id=selected_archetype_id,
            memos=component.memos,
            judge_result=judges,
            validated_impacts=effective_impacts,
            terminal_evidence=effective_terminal_evidence,
            validity_evidence=validity_evidence,
            accepted_claim_ids=accepted_claim_ids,
            accepted_claim_fact_ids=accepted_claim_fact_ids,
            proposed_score_ranges_hash=canonical_hash(
                dossier.get("proposed_score_ranges") or {}
            ),
            proposed_stage=(
                str(dossier["proposed_stage"])
                if dossier.get("proposed_stage") is not None
                else None
            ),
        )
        if score_result.score is None:
            raise ValueError("complete Judge coverage did not produce a deterministic score")
        if not score_result.score_valid:
            pending_decision = replace(
                research_eligibility,
                status="RESEARCH_INCOMPLETE",
                research_status="RESEARCH_INCOMPLETE",
                stage_status="RESEARCH_INCOMPLETE",
                publication_status="WITHHELD_PENDING_RESEARCH_SATURATION",
                withhold_reasons=tuple(
                    dict.fromkeys(
                        (
                            *score_result.pending_reasons,
                            "DETERMINISTIC_SCORE_VALIDITY_PENDING",
                        )
                    )
                ),
            )
            incomplete = research_incomplete_result(
                pending_decision,
                diagnostic_partial_score=_diagnostic_score_value(score_result),
                diagnostic_partial_stage=None,
                diagnostic_component_vector=(
                    score_result.score.component_score_vector
                ),
                diagnostic_score_interval={
                    "lower": score_result.score.provisional_score_lower,
                    "upper": score_result.score.provisional_score_upper,
                },
                component_coverage="7/7",
                judge_coverage="21/21",
                current_verified_fact_ids=tuple(row.fact_id for row in facts),
            )
            self._write_json_atomic(incomplete_result_path, incomplete)
            return ProScoringPipelineRun(
                job=job,
                component_result=component,
                judge_result=judges,
                score_result=score_result,
                stagecourt_result=None,
                score_receipt=None,
                stagecourt_receipt=None,
                reuse_receipt=reuse_receipt,
                scoring_root=scoring_root,
                research_eligibility=pending_decision,
                full_thesis_eligibility=full_thesis_eligibility,
                research_incomplete_result=incomplete,
            )
        score_base = {
            **score_result.receipt_payload,
            "job_id": job_id,
            "selected_archetype_id": selected_archetype_id,
            "judge_decision_count": len(judges.decisions),
            "accepted_claim_count": len(accepted_claim_ids),
            "reuse_receipt": reuse_receipt,
            "component_bridge_hash": canonical_hash(component_receipt),
            "judge_bridge_hash": canonical_hash(judge_receipt),
            "full_thesis_eligibility_hash": (
                full_thesis_eligibility.eligibility_hash
            ),
            "full_thesis_eligibility": full_thesis_eligibility_payload,
        }
        score_hash = canonical_hash(score_base)
        score_receipt_id = stable_id(
            "PROSCORE", {"job_id": job_id, "score_hash": score_hash}
        )
        score_receipt = _canonical_mapping(
            {
                **score_base,
                "score_receipt_id": score_receipt_id,
                "score_hash": score_hash,
            }
        )
        self._write_or_verify_json(score_receipt_path, score_receipt)
        if job.status == JobStatus.SCORING.value:
            job = self.store.record_score_result(
                job_id,
                expected_version=job.state_version,
                score_receipt_id=score_receipt_id,
                score_hash=score_hash,
                receipt=score_receipt,
                actor="pro-calibrated-scorer",
                idempotency_key=f"calibrated-score:{score_hash}",
            )
        else:
            durable_score = self.store.get_score_receipt(job_id)
            if canonical_json(durable_score) != canonical_json(score_receipt):
                raise ValueError("durable score differs from deterministic replay")
        stage_result = ProAtomicStageCourtBridge().decide(
            target_id=job.symbol,
            as_of_date=job.as_of_date,
            selected_archetype_id=selected_archetype_id,
            score_result=score_result,
            accepted_claim_ids=accepted_claim_ids,
            evidence_facts=facts,
            event_overlay_input=event_overlay_input,
            hard_break_claim_ids=hard_break_claim_ids,
            ignored_proposed_stage=(
                str(dossier["proposed_stage"])
                if dossier.get("proposed_stage") is not None
                else None
            ),
        )
        stage_base = {
            **stage_result.receipt_payload,
            "job_id": job_id,
            "score_receipt_id": score_receipt_id,
            "full_thesis_eligibility_hash": (
                full_thesis_eligibility.eligibility_hash
            ),
        }
        stagecourt_hash = canonical_hash(stage_base)
        stagecourt_receipt_id = stable_id(
            "PROSTAGECOURT",
            {"job_id": job_id, "stagecourt_hash": stagecourt_hash},
        )
        stage_receipt = _canonical_mapping(
            {
                **stage_base,
                "stagecourt_receipt_id": stagecourt_receipt_id,
                "stagecourt_hash": stagecourt_hash,
            }
        )
        self._write_or_verify_json(stage_receipt_path, stage_receipt)
        job = self.store.record_stagecourt_result(
            job_id,
            expected_version=job.state_version,
            stagecourt_receipt_id=stagecourt_receipt_id,
            stagecourt_hash=stagecourt_hash,
            receipt=stage_receipt,
            actor="pro-atomic-stagecourt",
            idempotency_key=f"atomic-stagecourt:{stagecourt_hash}",
        )
        return ProScoringPipelineRun(
            job=job,
            component_result=component,
            judge_result=judges,
            score_result=score_result,
            stagecourt_result=stage_result,
            score_receipt=score_receipt,
            stagecourt_receipt=stage_receipt,
            reuse_receipt=reuse_receipt,
            scoring_root=scoring_root,
            research_eligibility=research_eligibility,
            full_thesis_eligibility=full_thesis_eligibility,
        )

    def _resolve_delta_inputs(
        self,
        *,
        job: ProResearchJob,
        context: DeltaScoringReuseContext,
        current_facts: Sequence[EvidenceFact],
        current_source_verifications: Sequence[Mapping[str, Any]],
        current_claim_fact_links: Sequence[Mapping[str, Any]],
        current_impacts: Sequence[CreditValidatedImpact],
        current_terminal_evidence: Mapping[str, Mapping[str, Any]],
    ) -> _DeltaResolvedInputs:
        prior = self.store.get_job(context.prior_job_id)
        if (
            prior.status != JobStatus.FINAL.value
            or prior.symbol != job.symbol
            or prior.as_of_date > job.as_of_date
            or not self.store.get_score_receipt(prior.job_id)
            or not self.store.get_stagecourt_receipt(prior.job_id)
        ):
            raise ValueError("delta reuse prior job is not a compatible FINAL result")
        prior_root = context.prior_job_root
        prior_verification = prior_root / "verification"
        prior_scoring = prior_root / "scoring"
        prior_facts = tuple(
            evidence_fact_from_mapping(row)
            for row in _read_jsonl(prior_verification / "evidence_facts.jsonl")
        )
        prior_links = _read_jsonl(prior_verification / "claim_fact_links.jsonl")
        prior_sources = _read_jsonl(
            prior_verification / "source_verifications.jsonl"
        )
        prior_memo_rows = _read_jsonl(prior_scoring / "component_memos.jsonl")
        prior_memos = tuple(
            _component_memo_from_mapping(row)
            for row in prior_memo_rows
        )
        if len(prior_memos) != 7:
            raise ValueError("delta prior component roster is incomplete")
        prior_judges = self._load_complete_judges(
            scoring_root=prior_scoring,
            job_id=prior.job_id,
        )
        if prior_judges is None:
            raise ValueError("delta prior 21-Judge roster is incomplete")
        score_receipt = self.store.get_score_receipt(prior.job_id) or {}
        stage_receipt = self.store.get_stagecourt_receipt(prior.job_id) or {}
        component_receipt = _read_json(
            prior_scoring / "component_bridge_receipt.json"
        )
        judge_receipt = _read_json(prior_scoring / "judge_bridge_receipt.json")
        if (
            component_receipt.get("component_memos_hash")
            != canonical_hash(prior_memo_rows)
            or score_receipt.get("component_bridge_hash")
            != canonical_hash(component_receipt)
            or score_receipt.get("judge_bridge_hash")
            != canonical_hash(judge_receipt)
            or canonical_json(_read_json(prior_scoring / "score_receipt.json"))
            != canonical_json(score_receipt)
            or canonical_json(_read_json(prior_scoring / "stagecourt_receipt.json"))
            != canonical_json(stage_receipt)
        ):
            raise ValueError("delta prior scoring artifacts lack durable hash lineage")
        prior_impacts = tuple(
            _impact_from_mapping(row)
            for row in score_receipt.get("validated_impacts") or ()
        )
        terminalized_fact_ids = {
            str(fact_id)
            for row in current_claim_fact_links
            for fact_id in (
                *(row.get("supersedes_fact_ids") or ()),
                *(row.get("resolves_fact_ids") or ()),
            )
        }
        current_fact_by_id = {row.fact_id: row for row in current_facts}
        prior_fact_by_id = {row.fact_id: row for row in prior_facts}
        for fact_id in set(current_fact_by_id) & set(prior_fact_by_id):
            if canonical_hash(current_fact_by_id[fact_id].to_dict()) != canonical_hash(
                prior_fact_by_id[fact_id].to_dict()
            ):
                raise ValueError("delta fact id changed its immutable content")
        merged_facts = {
            fact_id: fact
            for fact_id, fact in prior_fact_by_id.items()
            if fact_id not in terminalized_fact_ids
        }
        merged_facts.update(current_fact_by_id)
        prior_terminalized_claim_ids = {
            str(row.get("claim_id") or "")
            for row in prior_links
            if str(row.get("fact_id") or "") in terminalized_fact_ids
        }
        merged_links = {
            (
                str(row.get("claim_id") or ""),
                str(row.get("fact_id") or ""),
            ): dict(row)
            for row in prior_links
            if str(row.get("claim_id") or "")
            and str(row.get("fact_id") or "")
            and str(row.get("fact_id") or "") not in terminalized_fact_ids
        }
        merged_links.update(
            {
                (
                    str(row.get("claim_id") or ""),
                    str(row.get("fact_id") or ""),
                ): dict(row)
                for row in current_claim_fact_links
                if str(row.get("claim_id") or "")
                and str(row.get("fact_id") or "")
            }
        )
        merged_sources = {
            str(row.get("dossier_fact_id") or canonical_hash(row)): dict(row)
            for row in prior_sources
        }
        merged_sources.update(
            {
                str(row.get("dossier_fact_id") or canonical_hash(row)): dict(row)
                for row in current_source_verifications
            }
        )
        merged_impacts = {
            row.impact_id: row
            for row in prior_impacts
            if row.claim_id not in prior_terminalized_claim_ids
        }
        merged_impacts.update({row.impact_id: row for row in current_impacts})
        prior_terminal = {
            str(row.get("component_id") or ""): {
                "status": row.get("status"),
                "search_exhaustion_proof": list(
                    row.get("search_exhaustion_proof") or ()
                ),
            }
            for row in score_receipt.get("component_assessments") or ()
            if str(row.get("component_id") or "")
        }
        merged_terminal = dict(prior_terminal)
        merged_terminal.update(
            {
                str(component_id): dict(value)
                for component_id, value in current_terminal_evidence.items()
            }
        )
        return _DeltaResolvedInputs(
            facts=tuple(merged_facts[key] for key in sorted(merged_facts)),
            source_verifications=tuple(
                merged_sources[key] for key in sorted(merged_sources)
            ),
            claim_fact_links=tuple(
                merged_links[key] for key in sorted(merged_links)
            ),
            validated_impacts=tuple(
                merged_impacts[key] for key in sorted(merged_impacts)
            ),
            terminal_evidence=merged_terminal,
            prior_memos=prior_memos,
            prior_judges=prior_judges,
            prior_facts=prior_facts,
            prior_gap_decisions=self.store.get_gap_decisions(prior.job_id),
            prior_impacts=prior_impacts,
            prior_terminal_evidence=prior_terminal,
        )

    @staticmethod
    def _resolve_delta_components(
        *,
        job: ProResearchJob,
        current_component: ComponentBridgeResult,
        facts: Sequence[EvidenceFact],
        current_gap_decisions: Sequence[Mapping[str, Any]],
        current_impacts: Sequence[CreditValidatedImpact],
        terminal_evidence: Mapping[str, Mapping[str, Any]],
        delta_inputs: _DeltaResolvedInputs,
        context: DeltaScoringReuseContext,
    ) -> tuple[ComponentBridgeResult, tuple[str, ...], tuple[str, ...]]:
        fact_by_id = {row.fact_id: row for row in facts}
        prior_by_component = {
            row.component_id: row for row in delta_inputs.prior_memos
        }
        current_by_component = {
            row.component_id: _augment_delta_memo(
                current=row,
                prior=prior_by_component[row.component_id],
                fact_by_id=fact_by_id,
                job_id=job.job_id,
            )
            for row in current_component.memos
        }
        changed = []
        for component_id in CANONICAL_COMPONENT_ORDER:
            current_hash = _delta_component_input_hash(
                component_id=component_id,
                memo=current_by_component[component_id],
                facts=facts,
                gaps=current_gap_decisions,
                impacts=current_impacts,
                terminal_evidence=terminal_evidence,
            )
            prior_hash = _delta_component_input_hash(
                component_id=component_id,
                memo=prior_by_component[component_id],
                facts=tuple(
                    row for row in delta_inputs.prior_facts if row.fact_id in fact_by_id
                ),
                gaps=delta_inputs.prior_gap_decisions,
                impacts=delta_inputs.prior_impacts,
                terminal_evidence=delta_inputs.prior_terminal_evidence,
            )
            if current_hash != prior_hash:
                changed.append(component_id)
        undeclared = set(changed) - set(context.components_to_revisit)
        if undeclared:
            raise ValueError(
                "delta changed components outside the declared revisit roster: "
                + ",".join(sorted(undeclared))
            )
        if not changed:
            raise ValueError(
                "NO_MATERIAL_DELTA: stop before browser submission and reuse prior result"
            )
        changed_set = set(changed)
        resolved = tuple(
            current_by_component[component_id]
            if component_id in changed_set
            else prior_by_component[component_id]
            for component_id in CANONICAL_COMPONENT_ORDER
        )
        reused = tuple(
            component_id
            for component_id in CANONICAL_COMPONENT_ORDER
            if component_id not in changed_set
        )
        return (
            ComponentBridgeResult(
                memos=resolved,
                removed_unverified_dossier_fact_ids=(
                    current_component.removed_unverified_dossier_fact_ids
                ),
                verified_dossier_to_evidence_fact=(
                    current_component.verified_dossier_to_evidence_fact
                ),
            ),
            tuple(changed),
            reused,
        )

    @classmethod
    def _write_or_progress_reuse_receipt(
        cls,
        path: Path,
        payload: Mapping[str, Any],
    ) -> None:
        if not _reuse_receipt_is_valid(
            payload,
            expected_job_id=str(payload.get("job_id") or ""),
            require_complete=False,
        ):
            raise ValueError("scoring reuse receipt is invalid")
        if path.is_file():
            existing = _read_json(path)
            if existing.get("status") == "REUSE_COMPLETE":
                if canonical_json(existing) != canonical_json(payload):
                    raise ValueError("complete reuse receipt changed")
                return
        cls._write_json_atomic(path, payload)

    @staticmethod
    def _write_json_atomic(path: Path, payload: Mapping[str, Any]) -> None:
        _write_atomic(path, canonical_json(payload) + "\n")

    @staticmethod
    def _write_jsonl_atomic(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
        _write_atomic(path, "".join(canonical_json(row) + "\n" for row in rows))

    @classmethod
    def _write_or_verify_json(cls, path: Path, payload: Mapping[str, Any]) -> None:
        if path.is_file():
            if canonical_json(_read_json(path)) != canonical_json(payload):
                raise ValueError(f"durable JSON artifact changed: {path}")
            return
        cls._write_json_atomic(path, payload)

    @classmethod
    def _write_or_verify_jsonl(
        cls,
        path: Path,
        rows: Sequence[Mapping[str, Any]],
    ) -> None:
        expected = tuple(dict(row) for row in rows)
        if path.is_file():
            if canonical_json(_read_jsonl(path)) != canonical_json(expected):
                raise ValueError(f"durable JSONL artifact changed: {path}")
            return
        cls._write_jsonl_atomic(path, expected)

    @staticmethod
    def _load_complete_judges(
        *,
        scoring_root: Path,
        job_id: str,
    ) -> JudgeBridgeResult | None:
        decisions_path = scoring_root / "judge_decisions.jsonl"
        calls_path = scoring_root / "judge_calls.jsonl"
        receipt_path = scoring_root / "judge_bridge_receipt.json"
        if not all(path.is_file() for path in (decisions_path, calls_path, receipt_path)):
            return None
        receipt = _read_json(receipt_path)
        if receipt.get("status") != "JUDGING_COMPLETE":
            return None
        decision_rows = _read_jsonl(decisions_path)
        call_rows = _read_jsonl(calls_path)
        decisions = tuple(
            _judge_decision_from_mapping(row) for row in decision_rows
        )
        calls = tuple(_judge_call_receipt_from_mapping(row) for row in call_rows)
        result = JudgeBridgeResult(
            status="JUDGING_COMPLETE",
            decisions=decisions,
            call_receipts=calls,
            pending_reasons=(),
        )
        calls_by_id = {row.judge_call_id: row for row in calls}
        if (
            len(decisions) != 21
            or len(calls) != 21
            or len(calls_by_id) != 21
            or any(row.status != "COMPLETE" for row in calls)
            or any(
                decision.judge_call_id not in calls_by_id
                or calls_by_id[decision.judge_call_id].component_id
                != decision.component_id
                or calls_by_id[decision.judge_call_id].role != decision.role
                or calls_by_id[decision.judge_call_id].prompt_hash
                != decision.prompt_hash
                or calls_by_id[decision.judge_call_id].response_hash
                != decision.response_hash
                for decision in decisions
            )
        ):
            raise ValueError("durable Judge calls do not bind to all decisions")
        expected = _judge_bridge_receipt(
            job_id=job_id,
            judges=result,
            decision_rows=decision_rows,
            call_rows=call_rows,
        )
        if receipt != expected or not result.score_valid:
            raise ValueError("durable Judge roster or receipt is invalid")
        return result


def _component_memo_from_mapping(row: Mapping[str, Any]) -> ComponentResearchMemo:
    return ComponentResearchMemo(
        memo_id=str(row.get("memo_id") or ""),
        target_id=str(row.get("target_id") or ""),
        archetype_id=str(row.get("archetype_id") or ""),
        component_id=str(row.get("component_id") or ""),
        component_max_points=float(row.get("component_max_points") or 0.0),
        positive_fact_ids=tuple(row.get("positive_fact_ids") or ()),
        counter_fact_ids=tuple(row.get("counter_fact_ids") or ()),
        resolution_fact_ids=tuple(row.get("resolution_fact_ids") or ()),
        context_fact_ids=tuple(row.get("context_fact_ids") or ()),
        structured_metrics=dict(row.get("structured_metrics") or {}),
        historical_anchor_ids=tuple(row.get("historical_anchor_ids") or ()),
        researcher_summary=str(row.get("researcher_summary") or ""),
        positive_case=str(row.get("positive_case") or ""),
        counter_case=str(row.get("counter_case") or ""),
        uncertainties=tuple(row.get("uncertainties") or ()),
        source_coverage=tuple(row.get("source_coverage") or ()),
        proposed_score_lower=float(row.get("proposed_score_lower") or 0.0),
        proposed_score_mid=float(row.get("proposed_score_mid") or 0.0),
        proposed_score_upper=float(row.get("proposed_score_upper") or 0.0),
        confidence=float(row.get("confidence") or 0.0),
        research_complete=row.get("research_complete") is True,
        nearest_positive_anchor_ids=tuple(
            row.get("nearest_positive_anchor_ids") or ()
        ),
        nearest_counter_anchor_ids=tuple(
            row.get("nearest_counter_anchor_ids") or ()
        ),
        why_not_higher=str(row.get("why_not_higher") or ""),
        why_not_lower=str(row.get("why_not_lower") or ""),
        researcher_role=str(row.get("researcher_role") or ""),
        schema_version=str(
            row.get("schema_version") or "e2r_component_research_memo_v2"
        ),
    )


def _impact_from_mapping(row: Mapping[str, Any]) -> CreditValidatedImpact:
    payload = dict(row)
    payload["counter_claim_ids"] = tuple(payload.get("counter_claim_ids") or ())
    payload["lineage_mapping_ids"] = tuple(
        payload.get("lineage_mapping_ids") or ()
    )
    return CreditValidatedImpact(**payload)


def _augment_delta_memo(
    *,
    current: ComponentResearchMemo,
    prior: ComponentResearchMemo,
    fact_by_id: Mapping[str, EvidenceFact],
    job_id: str,
) -> ComponentResearchMemo:
    if (
        current.component_id != prior.component_id
        or current.target_id != prior.target_id
        or current.archetype_id != prior.archetype_id
    ):
        raise ValueError("delta component memo identity differs from prior")

    def active_union(*groups: Sequence[str]) -> tuple[str, ...]:
        return tuple(
            value
            for value in dict.fromkeys(
                str(item) for group in groups for item in group
            )
            if value in fact_by_id
        )

    positive = active_union(prior.positive_fact_ids, current.positive_fact_ids)
    counter = active_union(prior.counter_fact_ids, current.counter_fact_ids)
    resolution = active_union(
        prior.resolution_fact_ids,
        current.resolution_fact_ids,
    )
    context = active_union(prior.context_fact_ids, current.context_fact_ids)
    fact_ids = (*positive, *counter, *resolution, *context)
    sources = tuple(
        sorted(
            {
                source_id
                for fact_id in fact_ids
                for source_id in fact_by_id[fact_id].source_ids
            }
        )
    )
    structured_metrics = {
        **dict(prior.structured_metrics),
        **dict(current.structured_metrics),
    }
    anchor_ids = tuple(
        dict.fromkeys((*prior.historical_anchor_ids, *current.historical_anchor_ids))
    )
    nearest_positive = tuple(
        value
        for value in dict.fromkeys(
            (
                *prior.nearest_positive_anchor_ids,
                *current.nearest_positive_anchor_ids,
            )
        )
        if value in anchor_ids
    )
    nearest_counter = tuple(
        value
        for value in dict.fromkeys(
            (
                *prior.nearest_counter_anchor_ids,
                *current.nearest_counter_anchor_ids,
            )
        )
        if value in anchor_ids
    )
    memo_id = stable_id(
        "PROMEMO",
        {
            "job_id": job_id,
            "archetype_id": current.archetype_id,
            "component_id": current.component_id,
            "fact_ids": sorted(fact_ids),
            "structured_metrics_hash": canonical_hash(structured_metrics),
        },
    )
    return replace(
        current,
        memo_id=memo_id,
        positive_fact_ids=positive,
        counter_fact_ids=counter,
        resolution_fact_ids=resolution,
        context_fact_ids=context,
        structured_metrics=structured_metrics,
        historical_anchor_ids=anchor_ids,
        uncertainties=tuple(
            dict.fromkeys((*prior.uncertainties, *current.uncertainties))
        ),
        source_coverage=sources,
        research_complete=prior.research_complete and current.research_complete,
        nearest_positive_anchor_ids=nearest_positive,
        nearest_counter_anchor_ids=nearest_counter,
    )


def _delta_component_input_hash(
    *,
    component_id: str,
    memo: ComponentResearchMemo,
    facts: Sequence[EvidenceFact],
    gaps: Sequence[Mapping[str, Any]],
    impacts: Sequence[CreditValidatedImpact],
    terminal_evidence: Mapping[str, Mapping[str, Any]],
) -> str:
    memo_payload = dict(memo.to_dict())
    memo_payload.pop("memo_id", None)
    component_facts = tuple(
        row.to_dict()
        for row in sorted(facts, key=lambda value: value.fact_id)
        if component_id in set(row.allowed_component_ids)
    )
    component_gaps = tuple(
        _semantic_gap_payload(row)
        for row in gaps
        if component_id
        in set(((row.get("assessment") or {}).get("affected_component_ids")) or ())
    )
    component_impacts = tuple(
        row.to_dict()
        for row in sorted(impacts, key=lambda value: value.impact_id)
        if row.component_id == component_id
    )
    return canonical_hash(
        {
            "component_id": component_id,
            "memo": memo_payload,
            "facts": component_facts,
            "gaps": sorted(component_gaps, key=canonical_json),
            "impacts": component_impacts,
            "terminal_evidence": dict(terminal_evidence.get(component_id) or {}),
        }
    )


def _semantic_gap_payload(row: Mapping[str, Any]) -> Mapping[str, Any]:
    assessment = dict(row.get("assessment") or {})
    materiality = dict(row.get("materiality") or {})
    return {
        "planner_label": row.get("planner_label"),
        "deterministic_evidence_class": row.get("deterministic_evidence_class"),
        "assessment": {
            key: assessment.get(key)
            for key in (
                "affected_component_ids",
                "missing_source_role",
                "component_range_bounded",
                "could_change_score",
                "could_change_stage",
                "could_change_hard_break",
            )
        },
        "materiality": {
            key: materiality.get(key)
            for key in (
                "max_score_delta",
                "stage_boundary_distance",
                "stage_cap_reason",
                "supplemental_allowed",
                "full_restart_allowed",
            )
        },
    }


def _combine_delta_judges(
    *,
    prior: JudgeBridgeResult,
    changed: JudgeBridgeResult,
    changed_component_ids: Sequence[str],
) -> JudgeBridgeResult:
    if not prior.score_valid:
        raise ValueError("delta reuse requires a complete prior Judge roster")
    changed_set = {str(value) for value in changed_component_ids}
    if not changed_set or not changed_set.issubset(CANONICAL_COMPONENT_ORDER):
        raise ValueError("delta changed Judge roster is invalid")
    if any(row.component_id not in changed_set for row in changed.decisions) or any(
        row.component_id not in changed_set for row in changed.call_receipts
    ):
        raise ValueError("delta Judge output escaped the changed component roster")
    prior_decisions = tuple(
        row for row in prior.decisions if row.component_id not in changed_set
    )
    prior_calls = tuple(
        row for row in prior.call_receipts if row.component_id not in changed_set
    )
    role_order = {"ANALYST": 0, "SKEPTIC": 1, "CALIBRATION_JUDGE": 2}
    component_order = {
        component_id: index
        for index, component_id in enumerate(CANONICAL_COMPONENT_ORDER)
    }
    decisions = tuple(
        sorted(
            (*prior_decisions, *changed.decisions),
            key=lambda row: (component_order[row.component_id], role_order[row.role]),
        )
    )
    calls = tuple(
        sorted(
            (*prior_calls, *changed.call_receipts),
            key=lambda row: (component_order[row.component_id], role_order[row.role]),
        )
    )
    complete_changed = (
        changed.status in {"JUDGING_COMPLETE", "JUDGING_PARTIAL_COMPLETE"}
        and len(changed.decisions) == 3 * len(changed_set)
        and len(changed.call_receipts) == 3 * len(changed_set)
        and all(row.status == "COMPLETE" for row in changed.call_receipts)
    )
    if complete_changed and len(decisions) == 21 and len(calls) == 21:
        return JudgeBridgeResult(
            status="JUDGING_COMPLETE",
            decisions=decisions,
            call_receipts=calls,
            pending_reasons=(),
        )
    return JudgeBridgeResult(
        status="JUDGING_PROVIDER_PENDING",
        decisions=decisions,
        call_receipts=calls,
        pending_reasons=changed.pending_reasons
        or ("DELTA_JUDGE_COVERAGE_INCOMPLETE",),
    )


def _build_reuse_receipt(
    *,
    job: ProResearchJob,
    context: DeltaScoringReuseContext | None,
    changed_component_ids: Sequence[str],
    reused_component_ids: Sequence[str],
    judges: JudgeBridgeResult,
) -> Mapping[str, Any]:
    changed_set = set(changed_component_ids)
    changed_judges = sum(
        row.component_id in changed_set for row in judges.decisions
    )
    reused_judges = len(judges.decisions) - changed_judges
    base = {
        "schema_version": "e2r_pro_scoring_reuse_receipt_v1",
        "status": "REUSE_COMPLETE" if judges.score_valid else "REUSE_PENDING",
        "job_id": job.job_id,
        "research_mode": job.mode,
        "prior_job_id": context.prior_job_id if context else None,
        "declared_revisit_components": (
            list(context.components_to_revisit) if context else []
        ),
        "recomputed_components": list(changed_component_ids),
        "reused_components": list(reused_component_ids),
        "recomputed_component_count": len(changed_component_ids),
        "reused_component_count": len(reused_component_ids),
        "planned_recomputed_judge_count": 3 * len(changed_component_ids),
        "recomputed_judge_count": changed_judges,
        "reused_judge_count": reused_judges,
        "browser_submit_count_before_scoring": job.submit_count,
        "scoring_query_count": 0,
        "scoring_fetch_count": 0,
        "supplemental_query_count": 0,
        "supplemental_fetch_count": 0,
        "full_restart_count": 0,
    }
    return _canonical_mapping({**base, "reuse_hash": canonical_hash(base)})


def _reuse_receipt_is_valid(
    receipt: Mapping[str, Any],
    *,
    expected_job_id: str,
    require_complete: bool,
) -> bool:
    payload = dict(receipt)
    reuse_hash = str(payload.pop("reuse_hash", ""))
    return bool(
        receipt.get("schema_version") == "e2r_pro_scoring_reuse_receipt_v1"
        and receipt.get("job_id") == expected_job_id
        and (not require_complete or receipt.get("status") == "REUSE_COMPLETE")
        and reuse_hash
        and reuse_hash == canonical_hash(payload)
    )


def _judge_bridge_receipt(
    *,
    job_id: str,
    judges: JudgeBridgeResult,
    decision_rows: Sequence[Mapping[str, Any]],
    call_rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    return {
        **judges.receipt_payload,
        "job_id": job_id,
        "judge_decisions_hash": canonical_hash(decision_rows),
        "judge_calls_hash": canonical_hash(call_rows),
    }


def _full_eligibility_from_mapping(
    row: Mapping[str, Any],
) -> FullThesisEligibilityReceipt:
    validate_full_thesis_eligibility_receipt(
        row,
        expected_job_id=str(row.get("job_id") or ""),
    )
    return FullThesisEligibilityReceipt(
        job_id=str(row.get("job_id") or ""),
        selected_archetype_id=str(row.get("selected_archetype_id") or ""),
        research_eligibility_hash=str(row.get("research_eligibility_hash") or ""),
        saturation_receipt_hash=str(row.get("saturation_receipt_hash") or ""),
        verified_fact_roster_hash=str(row.get("verified_fact_roster_hash") or ""),
        claim_lineage_roster_hash=str(row.get("claim_lineage_roster_hash") or ""),
        component_memo_hash=str(row.get("component_memo_hash") or ""),
        judge_decision_hash=str(row.get("judge_decision_hash") or ""),
        component_count=int(row.get("component_count") or 0),
        component_terminal_count=int(row.get("component_terminal_count") or 0),
        judge_count=int(row.get("judge_count") or 0),
        claim_lineage_count=int(row.get("claim_lineage_count") or 0),
        impact_count=int(row.get("impact_count") or 0),
        query_count=int(row.get("query_count") or 0),
        fetch_count=int(row.get("fetch_count") or 0),
        score_authority=row.get("score_authority") is True,
        stage_authority=row.get("stage_authority") is True,
    )


def _diagnostic_score_value(
    result: CalibratedScoreBridgeResult,
) -> float | None:
    if result.score is None:
        return None
    payload = result.score.to_dict()
    for key in (
        "full_e2r_score",
        "verified_supported_score",
        "provisional_score_lower",
    ):
        value = payload.get(key)
        if isinstance(value, (int, float)):
            return float(value)
    return None


def _read_json(path: Path) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"expected JSON object: {path}")
    return payload


def _canonical_mapping(payload: Mapping[str, Any]) -> Mapping[str, Any]:
    normalized = json.loads(canonical_json(payload))
    if not isinstance(normalized, Mapping):
        raise ValueError("canonical payload must remain a JSON object")
    return normalized


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    rows = tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )
    if not all(isinstance(row, Mapping) for row in rows):
        raise ValueError(f"expected JSONL objects: {path}")
    return rows


def _judge_decision_from_mapping(row: Mapping[str, Any]) -> ComponentJudgeDecision:
    return ComponentJudgeDecision(
        judge_id=str(row.get("judge_id") or ""),
        judge_call_id=str(row.get("judge_call_id") or ""),
        memo_id=str(row.get("memo_id") or ""),
        component_id=str(row.get("component_id") or ""),
        component_max_points=float(row.get("component_max_points") or 0.0),
        role=str(row.get("role") or ""),
        pass_name=str(row.get("pass_name") or ""),
        prompt_hash=str(row.get("prompt_hash") or ""),
        response_hash=str(row.get("response_hash") or ""),
        provider_name=str(row.get("provider_name") or ""),
        anchor_comparisons=tuple(row.get("anchor_comparisons") or ()),
        proposed_points=float(row.get("proposed_points") or 0.0),
        allowed_range=tuple(row.get("allowed_range") or ()),  # type: ignore[arg-type]
        rationale=str(row.get("rationale") or ""),
        disagreements=tuple(row.get("disagreements") or ()),
        support_fact_ids=tuple(row.get("support_fact_ids") or ()),
        counter_fact_ids=tuple(row.get("counter_fact_ids") or ()),
        nearest_anchor_ids=tuple(row.get("nearest_anchor_ids") or ()),
        why_not_higher=str(row.get("why_not_higher") or ""),
        why_not_lower=str(row.get("why_not_lower") or ""),
        production_total_score_authority=(
            row.get("production_total_score_authority") is True
        ),
        production_stage_authority=row.get("production_stage_authority") is True,
        schema_version=str(
            row.get("schema_version") or "e2r_component_judge_decision_v2"
        ),
    )


def _judge_call_receipt_from_mapping(row: Mapping[str, Any]) -> JudgeCallReceipt:
    if (
        row.get("mode") != "EVIDENCE_ONLY_NO_SEARCH"
        or row.get("query_count") != 0
        or row.get("fetch_count") != 0
        or row.get("web_search_allowed") is not False
        or row.get("source_fetch_allowed") is not False
        or row.get("production_total_score_authority") is not False
        or row.get("production_stage_authority") is not False
    ):
        raise ValueError("durable Judge call violated no-search authority")
    return JudgeCallReceipt(
        judge_call_id=str(row.get("judge_call_id") or ""),
        component_id=str(row.get("component_id") or ""),
        role=str(row.get("role") or ""),
        prompt_hash=str(row.get("prompt_hash") or ""),
        response_hash=(
            str(row["response_hash"])
            if row.get("response_hash") is not None
            else None
        ),
        provider_name=str(row.get("provider_name") or ""),
        status=str(row.get("status") or ""),
        error=str(row["error"]) if row.get("error") is not None else None,
    )


def _write_atomic(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    part = path.with_suffix(path.suffix + ".part")
    with part.open("w", encoding="utf-8") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(part, path)
    fsync_directory(path.parent)


__all__ = ["ProScoringPipelineRun", "ProScoringPipelineService"]

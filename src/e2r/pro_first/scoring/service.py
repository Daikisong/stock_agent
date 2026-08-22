"""Durable component → 21 Judge → score → AtomicStageCourtV2 pipeline."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.researcher_mode.schemas import (
    ComponentAnchor,
    ComponentJudgeDecision,
)
from e2r.research_brain.scoring import (
    CreditValidatedImpact,
    EventOverlayInput,
    FullScoreValidityEvidenceV2,
)

from ..ids import canonical_hash, canonical_json, stable_id
from ..job_store import ProFirstJobStore
from ..models import JobStatus, ProResearchJob
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
    scoring_root: Path


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
    ) -> ProScoringPipelineRun:
        root = Path(job_root).resolve()
        scoring_root = root / "scoring"
        score_receipt_path = scoring_root / "score_receipt.json"
        stage_receipt_path = scoring_root / "stagecourt_receipt.json"
        job = self.store.get_job(job_id)
        if job.status == JobStatus.FINAL.value:
            durable_score = self.store.get_score_receipt(job_id)
            durable_stage = self.store.get_stagecourt_receipt(job_id)
            if (
                durable_score is None
                or durable_stage is None
                or not score_receipt_path.is_file()
                or not stage_receipt_path.is_file()
                or canonical_json(_read_json(score_receipt_path))
                != canonical_json(durable_score)
                or canonical_json(_read_json(stage_receipt_path))
                != canonical_json(durable_stage)
            ):
                raise ValueError("FINAL scoring artifacts differ from the durable ledger")
            return ProScoringPipelineRun(
                job=job,
                component_result=None,
                judge_result=None,
                score_result=None,
                stagecourt_result=None,
                score_receipt=durable_score,
                stagecourt_receipt=durable_stage,
                scoring_root=scoring_root,
            )
        if job.status not in {
            JobStatus.COMPONENT_RESEARCH.value,
            JobStatus.JUDGING.value,
            JobStatus.SCORING.value,
            JobStatus.STAGECOURT.value,
        }:
            raise ValueError("job is outside the component/Judge scoring boundary")
        dossier = _read_json(root / "import/research_dossier.normalized.json")
        verification_root = root / "verification"
        facts = tuple(
            evidence_fact_from_mapping(row)
            for row in _read_jsonl(verification_root / "evidence_facts.jsonl")
        )
        source_verifications = _read_jsonl(
            verification_root / "source_verifications.jsonl"
        )
        claim_fact_links = _read_jsonl(
            verification_root / "claim_fact_links.jsonl"
        )
        gap_decisions = self.store.get_gap_decisions(job_id)
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
        component_rows = [row.to_dict() for row in component.memos]
        component_receipt = {**component.receipt_payload, "job_id": job_id}
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
                context=TransitionContext(component_coverage_complete=True),
                payload={"component_count": len(component.memos)},
            )
        judges = self._load_complete_judges(
            scoring_root=scoring_root,
            job_id=job_id,
        )
        if judges is None:
            if job.status != JobStatus.JUDGING.value:
                raise ValueError(
                    "durable 21-Judge artifacts are required after JUDGING"
                )
            judges = ProEvidenceOnlyJudgeBridge(judge_provider).run(
                memos=component.memos,
                evidence_facts=facts,
                historical_anchors=historical_anchors,
                gap_decisions=gap_decisions,
            )
            self._write_jsonl_atomic(
                scoring_root / "judge_decisions.jsonl",
                [row.to_dict() for row in judges.decisions],
            )
            self._write_jsonl_atomic(
                scoring_root / "judge_calls.jsonl",
                [row.to_dict() for row in judges.call_receipts],
            )
            self._write_json_atomic(
                scoring_root / "judge_bridge_receipt.json",
                {**judges.receipt_payload, "job_id": job_id},
            )
        if not judges.score_valid:
            return ProScoringPipelineRun(
                job=job,
                component_result=component,
                judge_result=judges,
                score_result=None,
                stagecourt_result=None,
                score_receipt=None,
                stagecourt_receipt=None,
                scoring_root=scoring_root,
            )
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
            validated_impacts=validated_impacts,
            terminal_evidence=terminal_evidence,
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
        score_base = {
            **score_result.receipt_payload,
            "job_id": job_id,
            "selected_archetype_id": selected_archetype_id,
            "judge_decision_count": len(judges.decisions),
            "accepted_claim_count": len(accepted_claim_ids),
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
            scoring_root=scoring_root,
        )

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
        decisions = tuple(
            _judge_decision_from_mapping(row)
            for row in _read_jsonl(decisions_path)
        )
        calls = tuple(
            _judge_call_receipt_from_mapping(row)
            for row in _read_jsonl(calls_path)
        )
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
        expected = {**result.receipt_payload, "job_id": job_id}
        if receipt != expected or not result.score_valid:
            raise ValueError("durable Judge roster or receipt is invalid")
        return result


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
    descriptor = os.open(path.parent, os.O_RDONLY)
    try:
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


__all__ = ["ProScoringPipelineRun", "ProScoringPipelineService"]

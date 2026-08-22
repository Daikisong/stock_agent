"""Compile verified Pro facts through the existing impact validation stack."""

from __future__ import annotations

from dataclasses import dataclass, replace
import json
import os
from pathlib import Path
from typing import Any, Mapping, Sequence
from urllib.parse import urlparse

from e2r.research_brain.compiler.evidence_impact_rubric_compiler import (
    compile_evidence_impact_rubrics,
)
from e2r.research_brain.runtime.scoring_contracts import (
    audit_scoring_schema_totality,
)
from e2r.research_brain.scoring import (
    CreditValidatedImpact,
    FullScoreValidityEvidenceV2,
    ImpactValidator,
)
from e2r.research_brain.scoring.business_mechanism_scope import (
    infer_business_mechanism_scope,
)
from e2r.research_brain.scoring.claim_impact_ledger import (
    ClaimImpactLedgerBuilder,
)
from e2r.research_brain.scoring.evidence_impact_adjudicator import (
    EvidenceImpactAdjudicator,
    EvidenceImpactProvider,
    compile_question_component_subcriteria,
)
from e2r.research_brain.scoring.question_impact_contract import (
    load_question_impact_contracts,
)
from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER

from ..atomic_io import fsync_directory
from ..ids import canonical_hash, canonical_json, stable_id
from ..models import ProResearchJob
from ..gaps.supplemental_service import (
    load_effective_dossier_facts,
    load_effective_verified_evidence,
)
from .component_bridge import evidence_fact_from_mapping


_DIRECTION_BY_FACT = {
    "POSITIVE": "SUPPORT",
    "COUNTER": "COUNTER",
    "NEGATIVE": "COUNTER",
    "RESOLUTION": "RESOLUTION",
    "NEUTRAL": "NEUTRAL",
}


@dataclass(frozen=True)
class ProImpactCompilationResult:
    status: str
    impacts: tuple[CreditValidatedImpact, ...]
    terminal_evidence: Mapping[str, Mapping[str, Any]]
    validity_evidence: FullScoreValidityEvidenceV2
    pending_reasons: tuple[str, ...]
    receipt: Mapping[str, Any]
    provider_call_count: int
    reused: bool = False

    @property
    def ready_for_judging(self) -> bool:
        return self.status == "PRO_VALIDATED_IMPACT_COMPILATION_COMPLETE"


class ProValidatedImpactCompiler:
    """Use Codex for semantic proposals and deterministic E2R validators for credit.

    The provider may select bounded rubric edges, but it cannot create a source,
    fact, mapping capability, component edge, credit cap, score, or Stage.  Every
    accepted impact is revalidated by ``ClaimImpactLedgerBuilder`` and
    ``ImpactValidator`` before it reaches the existing scorer.
    """

    def __init__(
        self,
        provider: EvidenceImpactProvider,
        *,
        repo_root: str | Path = ".",
    ) -> None:
        self.provider = provider
        self.repo_root = Path(repo_root).expanduser().resolve()

    def compile(
        self,
        *,
        job: ProResearchJob,
        dossier: Mapping[str, Any],
        job_root: str | Path,
        selected_archetype_id: str,
    ) -> ProImpactCompilationResult:
        root = Path(job_root).resolve()
        verification_root = root / "verification"
        scoring_root = root / "scoring"
        fact_rows, links, verifications = load_effective_verified_evidence(root)
        facts = tuple(
            evidence_fact_from_mapping(row) for row in fact_rows
        )
        gap_decisions = _read_jsonl(root / "gaps/gap_decisions.jsonl")
        if selected_archetype_id not in set(job.archetype_ids):
            raise ValueError("impact compiler archetype is outside the durable job")
        input_hash = canonical_hash(
            {
                "job_id": job.job_id,
                "dossier_hash": canonical_hash(dossier),
                "selected_archetype_id": selected_archetype_id,
                "facts": [row.to_dict() for row in facts],
                "links": links,
                "verifications": verifications,
                "gap_decisions": gap_decisions,
            }
        )
        reused = self._reuse_complete(
            scoring_root=scoring_root,
            expected_input_hash=input_hash,
            expected_job_id=job.job_id,
            expected_archetype_id=selected_archetype_id,
        )
        if reused is not None:
            return reused

        fact_by_id = {row.fact_id: row for row in facts}
        verification_by_claim = {
            str(row.get("compiled_claim_id") or ""): row
            for row in verifications
            if str(row.get("compiled_claim_id") or "")
        }
        dossier_fact_by_id = {
            str(row.get("dossier_fact_id") or ""): row
            for row in load_effective_dossier_facts(dossier, root)
        }
        primary_links = tuple(
            row
            for row in links
            if str(row.get("link_role") or "PRIMARY_FACT_CLAIM")
            == "PRIMARY_FACT_CLAIM"
        )
        claim_rows: list[Mapping[str, Any]] = []
        provenance_rows: list[Mapping[str, Any]] = []
        eligibility_rows: list[Mapping[str, Any]] = []
        compilation_rows: list[Mapping[str, Any]] = []
        prepared_by_claim: dict[str, Mapping[str, Any]] = {}
        question_catalog = {
            key: value
            for key, value in load_question_impact_contracts().items()
            if value.archetype_id == selected_archetype_id
        }
        rubrics = compile_evidence_impact_rubrics(selected_archetype_id)
        rubric_by_primitive = rubrics.by_primitive()
        all_known_claim_ids = {
            str(row.get("claim_id") or "") for row in primary_links
        }

        for link in primary_links:
            claim_id = str(link.get("claim_id") or "")
            fact = fact_by_id.get(str(link.get("fact_id") or ""))
            verification = verification_by_claim.get(claim_id)
            if fact is None or verification is None:
                raise ValueError("impact compiler found detached verified claim lineage")
            dossier_fact = dossier_fact_by_id.get(
                str(verification.get("dossier_fact_id") or "")
            )
            if dossier_fact is None:
                raise ValueError("impact compiler cannot resolve the dossier fact")
            allowed_components = tuple(fact.allowed_component_ids)
            primitive_ids = tuple(
                sorted(
                    {
                        primitive_id
                        for contract in question_catalog.values()
                        if set(contract.allowed_component_ids).intersection(
                            allowed_components
                        )
                        for primitive_id in contract.allowed_primitive_ids
                        if primitive_id in rubric_by_primitive
                        and set(
                            rubric_by_primitive[primitive_id].allowed_component_ids
                        ).intersection(allowed_components)
                    }
                )
            )
            mapping_by_primitive = {
                primitive_id: stable_id(
                    "PROMAPCAND",
                    {
                        "job_id": job.job_id,
                        "claim_id": claim_id,
                        "archetype_id": selected_archetype_id,
                        "primitive_id": primitive_id,
                    },
                )
                for primitive_id in primitive_ids
            }
            direction = _DIRECTION_BY_FACT.get(fact.direction)
            if direction is None:
                raise ValueError("verified fact direction cannot enter impact compilation")
            source_family = _source_family(dossier_fact, job=job)
            evidence_family_id = stable_id(
                "PROEVIDENCEFAMILY",
                {
                    "economic_fact_key": link.get("economic_fact_key"),
                    "source_independence_group": fact.source_independence_group,
                },
            )
            claim = {
                "claim_id": claim_id,
                "accepted": True,
                "accepted_by_evidence_os": True,
                "evidence_origin": "ORGANIC_LIVE",
                "target_id": job.symbol,
                "subject": fact.subject,
                "business_segment": fact.business_segment,
                "product_family": fact.product_family,
                "economic_mechanism": fact.economic_mechanism,
                "predicate": fact.predicate,
                "exact_quote": str(dossier_fact.get("supporting_excerpt") or ""),
                "event_date": dossier_fact.get("event_date"),
                "effective_start": fact.period,
                "effective_end": fact.period,
                "reporting_period": fact.period,
                "polarity": direction,
                "mapping_ids": list(mapping_by_primitive.values()),
                "mapping_candidates": [
                    {"mapping_id": mapping_id, "primitive_id": primitive_id}
                    for primitive_id, mapping_id in mapping_by_primitive.items()
                ],
                "raw_assertion": {
                    "subject": fact.subject,
                    "predicate": fact.predicate,
                    "object_text": str(dossier_fact.get("statement") or ""),
                    "exact_quote": str(
                        dossier_fact.get("supporting_excerpt") or ""
                    ),
                },
                "economic_fact_key": str(link.get("economic_fact_key") or ""),
            }
            source_path = root / str(verification.get("document_path") or "")
            provenance = {
                "claim_id": claim_id,
                "mapping_ids": list(mapping_by_primitive.values()),
                "source_proxy_only": False,
                "test_only": False,
                "fetched": True,
                "anchor_verified": True,
                "directness": "DIRECT",
                "temporal_status": "CURRENT",
                "mapping_status": "ACCEPTED",
                "source_url": str(verification.get("source_url") or ""),
                "document_id": str(verification.get("source_id") or ""),
                "content_hash": verification.get("content_hash"),
                "exact_quote": str(dossier_fact.get("supporting_excerpt") or ""),
                "effective_period": fact.period,
                "source_independence_group": fact.source_independence_group,
            }
            eligibility_id = stable_id(
                "PROELIGIBILITY",
                {
                    "job_id": job.job_id,
                    "claim_id": claim_id,
                    "archetype_id": selected_archetype_id,
                    "verification_hash": verification.get("content_hash"),
                },
            )
            eligibility = {
                "eligibility_decision_id": eligibility_id,
                "claim_id": claim_id,
                "archetype_id": selected_archetype_id,
                "ledger_acceptance": True,
                "source_task_satisfaction": "PRO_DOSSIER_SOURCE_VERIFIED",
                "component_scoring_eligibility": bool(allowed_components),
                "risk_scoring_eligibility": direction == "COUNTER",
                "stage_event_eligibility": False,
                "full_thesis_eligibility": bool(allowed_components),
                "eligibility_status": (
                    "ELIGIBLE" if allowed_components else "INELIGIBLE_WRONG_MECHANISM"
                ),
                "eligibility_reasons": (
                    [] if allowed_components else ["NO_ALLOWED_COMPONENT_EDGE"]
                ),
            }
            claim_rows.append(claim)
            provenance_rows.append(provenance)
            eligibility_rows.append(eligibility)
            prepared_by_claim[claim_id] = {
                "claim": claim,
                "provenance": provenance,
                "eligibility": eligibility,
                "fact": fact,
                "dossier_fact": dossier_fact,
                "mapping_by_primitive": mapping_by_primitive,
                "direction": direction,
                "source_family": source_family,
                "evidence_family_id": evidence_family_id,
                "document_context_excerpt": _document_context(source_path),
            }

        proposals = []
        pending: list[str] = []
        provider_call_count = 0
        for claim_id, prepared in prepared_by_claim.items():
            mapping_by_primitive = prepared["mapping_by_primitive"]
            fact = prepared["fact"]
            allowed_components = tuple(fact.allowed_component_ids)
            contracts = tuple(
                contract
                for contract in question_catalog.values()
                if set(contract.allowed_primitive_ids).intersection(
                    mapping_by_primitive
                )
                and set(contract.allowed_component_ids).intersection(
                    allowed_components
                )
            )
            if not contracts or not mapping_by_primitive:
                compilation_rows.append(
                    {
                        "claim_id": claim_id,
                        "status": "NO_APPLICABLE_SCORING_CONTRACT",
                        "provider_call_count": 0,
                    }
                )
                continue
            scope_primitive = next(iter(mapping_by_primitive))
            try:
                result = EvidenceImpactAdjudicator(self.provider).adjudicate(
                    target_identity={
                        "target_id": job.symbol,
                        "company_name": job.company_name,
                    },
                    as_of_date=job.as_of_date,
                    archetype_id=selected_archetype_id,
                    accepted_claim=prepared["claim"],
                    exact_quote=str(prepared["claim"]["exact_quote"]),
                    document_metadata={
                        "document_id": prepared["provenance"]["document_id"],
                        "source_url": prepared["provenance"]["source_url"],
                        "published_date": prepared["dossier_fact"].get(
                            "published_at"
                        ),
                        "source_family": prepared["source_family"],
                        "evidence_origin": "ORGANIC_LIVE",
                        "document_context_excerpt": prepared[
                            "document_context_excerpt"
                        ],
                    },
                    current_claim_ledger=tuple(claim_rows),
                    counter_claims=tuple(
                        row
                        for row in claim_rows
                        if row.get("polarity") == "COUNTER"
                        and row.get("claim_id") != claim_id
                    ),
                    rubrics=rubrics.rubrics,
                    allowed_component_ids=allowed_components,
                    business_mechanism_scope=infer_business_mechanism_scope(
                        prepared["claim"],
                        primitive_id=scope_primitive,
                        archetype_id=selected_archetype_id,
                    ),
                    question_impact_contracts=contracts,
                    claim_eligibility_decision=prepared["eligibility"],
                    component_subcriteria=compile_question_component_subcriteria(
                        contracts,
                        allowed_component_ids=allowed_components,
                    ),
                )
            except Exception as error:
                pending.append(
                    f"IMPACT_PROVIDER_ERROR:{claim_id}:{type(error).__name__}"
                )
                compilation_rows.append(
                    {
                        "claim_id": claim_id,
                        "status": "PROVIDER_ERROR",
                        "error_class": type(error).__name__,
                        "provider_call_count": 0,
                    }
                )
                break
            provider_call_count += len(result.response_hashes)
            valid = []
            invalid_count = 0
            for proposal in result.proposals:
                expected_mapping = mapping_by_primitive.get(proposal.primitive_id)
                expected_direction = prepared["direction"]
                if (
                    expected_mapping is None
                    or proposal.mapping_id != expected_mapping
                    or proposal.direction != expected_direction
                    or proposal.source_family != prepared["source_family"]
                    or proposal.temporal_scope != "CURRENT"
                    or not set(proposal.counter_claim_ids).issubset(
                        all_known_claim_ids
                    )
                ):
                    invalid_count += 1
                    continue
                valid.append(
                    replace(
                        proposal,
                        evidence_family_id=prepared["evidence_family_id"],
                        confidence=min(proposal.confidence, fact.confidence),
                        lineage_mapping_ids=(),
                    )
                )
            if result.status != "IMPACT_ADJUDICATION_PASS" or invalid_count:
                pending.append(f"IMPACT_ADJUDICATION_PENDING:{claim_id}")
            proposals.extend(valid)
            compilation_rows.append(
                {
                    "claim_id": claim_id,
                    "status": result.status,
                    "valid_proposal_count": len(valid),
                    "invalid_proposal_count": invalid_count,
                    "prompt_hashes": list(result.prompt_hashes),
                    "response_hashes": list(result.response_hashes),
                    "provider_call_count": len(result.response_hashes),
                    "critical_count_sum": int(
                        result.audit.get("critical_count_sum") or 0
                    ),
                }
            )

        if pending:
            return self._pending_result(
                scoring_root=scoring_root,
                input_hash=input_hash,
                pending_reasons=tuple(dict.fromkeys(pending)),
                compilation_rows=compilation_rows,
                provider_call_count=provider_call_count,
                job_id=job.job_id,
                target_id=job.symbol,
                selected_archetype_id=selected_archetype_id,
            )
        ledger = ClaimImpactLedgerBuilder().build(
            proposals=proposals,
            accepted_current_claims=claim_rows,
            claim_provenance=provenance_rows,
            source_task_satisfaction=(),
            claim_eligibility_decisions=eligibility_rows,
        )
        validation = ImpactValidator().validate(
            impacts=ledger.validated_impacts,
            claim_provenance=provenance_rows,
            claim_eligibility_decisions=eligibility_rows,
            accepted_current_claims=claim_rows,
        )
        validation_pending = []
        if ledger.status != "MANY_TO_MANY_CLAIM_IMPACT_PASS":
            validation_pending.append("CLAIM_IMPACT_LEDGER_PENDING")
        if int(validation.audit.get("critical_count_sum") or 0) > 0:
            validation_pending.append("IMPACT_VALIDATION_CRITICAL")
        if validation.rejected:
            validation_pending.append("IMPACT_VALIDATION_REJECTED")
        covered_components = {
            row.component_id
            for row in validation.impacts
            if max(
                row.support_credit_fraction,
                row.counter_effect_fraction,
                row.resolution_effect,
            )
            > 0
        }
        contract_components = set(CANONICAL_COMPONENT_ORDER)
        missing_components = tuple(
            sorted(contract_components - covered_components)
        )
        terminal_evidence = {
            component_id: {
                "status": "PROVIDER_PENDING",
                "reason": "no credit-validated impact closed this component",
                "missing_questions": ["CREDIT_VALIDATED_IMPACT_REQUIRED"],
            }
            for component_id in missing_components
        }
        if missing_components:
            validation_pending.append(
                "COMPONENT_IMPACT_COVERAGE_PENDING:" + ",".join(missing_components)
            )
        schema_audit = audit_scoring_schema_totality(repo_root=self.repo_root)
        impact_counts = validation.audit.get("critical_counts") or {}
        validity = FullScoreValidityEvidenceV2(
            schema_totality_status=str(schema_audit.get("status") or ""),
            scoring_schema_critical_count=int(
                schema_audit.get("critical_count_sum") or 0
            ),
            silent_zero_default_count=int(
                (schema_audit.get("critical_counts") or {}).get(
                    "silent_zero_default_count"
                )
                or 0
            ),
            positive_impact_zeroed_by_missing_cap_count=int(
                impact_counts.get("positive_impact_zeroed_by_missing_cap_count")
                or 0
            ),
            counter_impact_zeroed_by_missing_cap_count=int(
                impact_counts.get("counter_impact_zeroed_by_missing_cap_count")
                or 0
            ),
            mechanism_scope_failure_count=int(
                impact_counts.get("cross_mechanism_impact_count") or 0
            ),
            question_component_reconciliation_critical_count=0,
            unresolved_contradiction_count=0,
            pending_state_count=len(missing_components),
            absence_without_adequacy_count=0,
            gold_critical_fact_miss_count=0,
            cross_business_question_closure_count=0,
            same_fact_duplicate_credit_count=int(
                impact_counts.get("same_fact_duplicate_credit_count") or 0
            ),
            same_document_duplicate_credit_count=int(
                impact_counts.get("same_document_duplicate_credit_count") or 0
            ),
            source_audit_ids=(
                input_hash,
                str(schema_audit.get("policy_config_hash") or ""),
            ),
        )
        status = (
            "PRO_VALIDATED_IMPACT_COMPILATION_COMPLETE"
            if not validation_pending
            else "PRO_VALIDATED_IMPACT_COMPILATION_PENDING"
        )
        receipt = {
            "schema_version": "e2r_pro_validated_impact_compilation_v1",
            "status": status,
            "job_id": job.job_id,
            "target_id": job.symbol,
            "input_hash": input_hash,
            "selected_archetype_id": selected_archetype_id,
            "verified_fact_count": len(facts),
            "primary_claim_count": len(primary_links),
            "impact_proposal_count": len(proposals),
            "validated_impact_count": len(validation.impacts),
            "covered_component_ids": sorted(covered_components),
            "missing_component_ids": list(missing_components),
            "pending_reasons": validation_pending,
            "provider_name": str(
                getattr(self.provider, "provider_name", "UNKNOWN")
            ),
            "provider_call_count": provider_call_count,
            "validated_impacts_hash": canonical_hash(
                [row.to_dict() for row in validation.impacts]
            ),
            "terminal_evidence_hash": canonical_hash(terminal_evidence),
            "validity_evidence_hash": canonical_hash(validity.to_dict()),
            "compilation_rows_hash": canonical_hash(compilation_rows),
            "ledger_audit_hash": canonical_hash(ledger.audit),
            "impact_validation_audit_hash": canonical_hash(validation.audit),
            "scoring_schema_audit_hash": canonical_hash(schema_audit),
            "pro_score_authority": False,
            "pro_stage_authority": False,
            "production_score_authority": False,
            "production_stage_authority": False,
        }
        self._write_artifacts(
            scoring_root=scoring_root,
            impacts=validation.impacts,
            terminal_evidence=terminal_evidence,
            validity_evidence=validity,
            compilation_rows=compilation_rows,
            receipt=receipt,
        )
        return ProImpactCompilationResult(
            status=status,
            impacts=tuple(validation.impacts),
            terminal_evidence=terminal_evidence,
            validity_evidence=validity,
            pending_reasons=tuple(validation_pending),
            receipt=receipt,
            provider_call_count=provider_call_count,
        )

    def _pending_result(
        self,
        *,
        scoring_root: Path,
        input_hash: str,
        pending_reasons: tuple[str, ...],
        compilation_rows: Sequence[Mapping[str, Any]],
        provider_call_count: int,
        job_id: str,
        target_id: str,
        selected_archetype_id: str,
    ) -> ProImpactCompilationResult:
        validity = _pending_validity(len(pending_reasons), input_hash)
        receipt = {
            "schema_version": "e2r_pro_validated_impact_compilation_v1",
            "status": "PRO_VALIDATED_IMPACT_COMPILATION_PENDING",
            "job_id": job_id,
            "target_id": target_id,
            "selected_archetype_id": selected_archetype_id,
            "input_hash": input_hash,
            "validated_impact_count": 0,
            "pending_reasons": list(pending_reasons),
            "provider_name": str(
                getattr(self.provider, "provider_name", "UNKNOWN")
            ),
            "provider_call_count": provider_call_count,
            "validated_impacts_hash": canonical_hash([]),
            "terminal_evidence_hash": canonical_hash({}),
            "validity_evidence_hash": canonical_hash(validity.to_dict()),
            "compilation_rows_hash": canonical_hash(compilation_rows),
            "pro_score_authority": False,
            "pro_stage_authority": False,
            "production_score_authority": False,
            "production_stage_authority": False,
        }
        self._write_artifacts(
            scoring_root=scoring_root,
            impacts=(),
            terminal_evidence={},
            validity_evidence=validity,
            compilation_rows=compilation_rows,
            receipt=receipt,
        )
        return ProImpactCompilationResult(
            status="PRO_VALIDATED_IMPACT_COMPILATION_PENDING",
            impacts=(),
            terminal_evidence={},
            validity_evidence=validity,
            pending_reasons=pending_reasons,
            receipt=receipt,
            provider_call_count=provider_call_count,
        )

    def _reuse_complete(
        self,
        *,
        scoring_root: Path,
        expected_input_hash: str,
        expected_job_id: str,
        expected_archetype_id: str,
    ) -> ProImpactCompilationResult | None:
        receipt_path = scoring_root / "impact_compilation_receipt.json"
        impacts_path = scoring_root / "validated_impacts.jsonl"
        terminal_path = scoring_root / "impact_terminal_evidence.json"
        validity_path = scoring_root / "impact_validity_evidence.json"
        compilation_path = scoring_root / "impact_adjudications.jsonl"
        if not all(
            path.is_file()
            for path in (
                receipt_path,
                impacts_path,
                terminal_path,
                validity_path,
                compilation_path,
            )
        ):
            return None
        receipt = _read_json(receipt_path)
        if (
            receipt.get("status")
            != "PRO_VALIDATED_IMPACT_COMPILATION_COMPLETE"
            or receipt.get("input_hash") != expected_input_hash
        ):
            return None
        impacts = tuple(_impact_from_mapping(row) for row in _read_jsonl(impacts_path))
        terminal = _read_json(terminal_path)
        validity = FullScoreValidityEvidenceV2(**_read_json(validity_path))
        compilation_rows = _read_jsonl(compilation_path)
        covered_components = {
            row.component_id
            for row in impacts
            if max(
                row.support_credit_fraction,
                row.counter_effect_fraction,
                row.resolution_effect,
            )
            > 0
        }
        validity_critical = sum(
            int(getattr(validity, field_name))
            for field_name in (
                "scoring_schema_critical_count",
                "silent_zero_default_count",
                "positive_impact_zeroed_by_missing_cap_count",
                "counter_impact_zeroed_by_missing_cap_count",
                "mechanism_scope_failure_count",
                "question_component_reconciliation_critical_count",
                "unresolved_contradiction_count",
                "pending_state_count",
                "absence_without_adequacy_count",
                "gold_critical_fact_miss_count",
                "cross_business_question_closure_count",
                "same_fact_duplicate_credit_count",
                "same_document_duplicate_credit_count",
            )
        )
        if (
            receipt.get("job_id") != expected_job_id
            or receipt.get("selected_archetype_id") != expected_archetype_id
            or any(row.target_id != self._expected_target_id(receipt) for row in impacts)
            or any(row.archetype_id != expected_archetype_id for row in impacts)
            or int(receipt.get("validated_impact_count") or 0) != len(impacts)
            or set(receipt.get("covered_component_ids") or ())
            != set(CANONICAL_COMPONENT_ORDER)
            or tuple(receipt.get("missing_component_ids") or ())
            or tuple(receipt.get("pending_reasons") or ())
            or covered_components != set(CANONICAL_COMPONENT_ORDER)
            or terminal
            or validity.schema_totality_status != "SCORING_SCHEMA_TOTALITY_PASS"
            or validity_critical
            or receipt.get("validated_impacts_hash")
            != canonical_hash([row.to_dict() for row in impacts])
            or receipt.get("terminal_evidence_hash") != canonical_hash(terminal)
            or receipt.get("validity_evidence_hash")
            != canonical_hash(validity.to_dict())
            or receipt.get("compilation_rows_hash")
            != canonical_hash(compilation_rows)
        ):
            raise ValueError("reused impact artifacts are not a complete validated roster")
        return ProImpactCompilationResult(
            status=str(receipt["status"]),
            impacts=impacts,
            terminal_evidence=terminal,
            validity_evidence=validity,
            pending_reasons=(),
            receipt=receipt,
            provider_call_count=0,
            reused=True,
        )

    @staticmethod
    def _expected_target_id(receipt: Mapping[str, Any]) -> str:
        return str(receipt.get("target_id") or "")

    def _write_artifacts(
        self,
        *,
        scoring_root: Path,
        impacts: Sequence[CreditValidatedImpact],
        terminal_evidence: Mapping[str, Mapping[str, Any]],
        validity_evidence: FullScoreValidityEvidenceV2,
        compilation_rows: Sequence[Mapping[str, Any]],
        receipt: Mapping[str, Any],
    ) -> None:
        _write_atomic(
            scoring_root / "impact_adjudications.jsonl",
            "".join(canonical_json(row) + "\n" for row in compilation_rows),
        )
        _write_atomic(
            scoring_root / "validated_impacts.jsonl",
            "".join(canonical_json(row.to_dict()) + "\n" for row in impacts),
        )
        _write_atomic(
            scoring_root / "impact_terminal_evidence.json",
            canonical_json(terminal_evidence) + "\n",
        )
        _write_atomic(
            scoring_root / "impact_validity_evidence.json",
            canonical_json(validity_evidence.to_dict()) + "\n",
        )
        _write_atomic(
            scoring_root / "impact_compilation_receipt.json",
            canonical_json(receipt) + "\n",
        )


def _pending_validity(count: int, source_id: str) -> FullScoreValidityEvidenceV2:
    return FullScoreValidityEvidenceV2(
        schema_totality_status="SCORING_SCHEMA_TOTALITY_PENDING",
        scoring_schema_critical_count=1,
        silent_zero_default_count=0,
        positive_impact_zeroed_by_missing_cap_count=0,
        counter_impact_zeroed_by_missing_cap_count=0,
        mechanism_scope_failure_count=0,
        question_component_reconciliation_critical_count=0,
        unresolved_contradiction_count=0,
        pending_state_count=max(count, 1),
        absence_without_adequacy_count=0,
        gold_critical_fact_miss_count=0,
        cross_business_question_closure_count=0,
        same_fact_duplicate_credit_count=0,
        same_document_duplicate_credit_count=0,
        source_audit_ids=(source_id,),
    )


def _source_family(fact: Mapping[str, Any], *, job: ProResearchJob) -> str:
    host = (urlparse(str(fact.get("source_url") or "")).hostname or "").casefold()
    publisher = str(fact.get("source_publisher") or "").casefold()
    issuer = job.company_name.casefold()
    if host.endswith("dart.fss.or.kr") or host.endswith("kind.krx.co.kr"):
        return "OFFICIAL_FILING"
    if issuer and issuer in publisher:
        return "ISSUER_OFFICIAL"
    return "TRUSTED_INDEPENDENT"


def _document_context(path: Path, *, maximum_chars: int = 6000) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return ""
    return text[:maximum_chars]


def _impact_from_mapping(row: Mapping[str, Any]) -> CreditValidatedImpact:
    payload = dict(row)
    for key in ("counter_claim_ids", "lineage_mapping_ids"):
        payload[key] = tuple(payload.get(key) or ())
    return CreditValidatedImpact(**payload)


def _read_json(path: Path) -> Mapping[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError(f"expected JSON object: {path}")
    return value


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
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


__all__ = ["ProImpactCompilationResult", "ProValidatedImpactCompiler"]

"""Deterministic full-thesis eligibility gates for scoring and publication.

The Pro dossier may contain proposed score or Stage fields, but neither those
fields nor component/Judge completeness can establish research adequacy.  This
module binds the downstream deterministic pipeline to the V2/V3
question-closure receipt and keeps incomplete research in a non-publishable
diagnostic shape.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping, Sequence

from e2r.research_brain.researcher_mode.schemas import (
    CANONICAL_COMPONENT_ORDER,
    ComponentResearchMemo,
    EvidenceFact,
)
from e2r.research_brain.scoring import CreditValidatedImpact

from ..ids import canonical_hash
from ..models import ProResearchJob
from ..research_contracts import select_contract_bundle
from .judge_bridge import JudgeBridgeResult


WITHHELD = "WITHHELD_PENDING_RESEARCH_SATURATION"


@dataclass(frozen=True)
class ResearchEligibilityDecision:
    job_id: str
    selected_archetype_id: str
    status: str
    research_status: str
    research_saturation_valid: bool
    component_entry_allowed: bool
    score_valid: bool
    canonical_stage: None
    stage_status: str
    publication_status: str
    saturation_receipt_hash: str | None
    verified_fact_roster_hash: str
    claim_lineage_roster_hash: str
    pending_question_ids: tuple[str, ...]
    missing_source_roles: tuple[str, ...]
    monitoring_conditions: tuple[str, ...]
    withhold_reasons: tuple[str, ...]

    @property
    def decision_hash(self) -> str:
        return canonical_hash(self.to_dict(include_hash=False))

    def to_dict(self, *, include_hash: bool = True) -> Mapping[str, Any]:
        payload = {
            "schema_version": "e2r_pro_research_eligibility_decision_v1",
            **asdict(self),
        }
        for name in (
            "pending_question_ids",
            "missing_source_roles",
            "monitoring_conditions",
            "withhold_reasons",
        ):
            payload[name] = list(payload[name])
        if include_hash:
            payload["decision_hash"] = canonical_hash(payload)
        return payload


@dataclass(frozen=True)
class FullThesisEligibilityReceipt:
    job_id: str
    selected_archetype_id: str
    research_eligibility_hash: str
    saturation_receipt_hash: str
    verified_fact_roster_hash: str
    claim_lineage_roster_hash: str
    component_memo_hash: str
    judge_decision_hash: str
    component_count: int
    component_terminal_count: int
    judge_count: int
    claim_lineage_count: int
    impact_count: int
    query_count: int = 0
    fetch_count: int = 0
    score_authority: bool = False
    stage_authority: bool = False

    def __post_init__(self) -> None:
        if self.component_count != 7 or self.component_terminal_count != 7:
            raise ValueError("full thesis requires seven terminal component memos")
        if self.judge_count != 21:
            raise ValueError("full thesis requires twenty-one terminal Judge decisions")
        if self.score_authority or self.stage_authority:
            raise ValueError("eligibility gate cannot own score or Stage authority")
        if self.query_count or self.fetch_count:
            raise ValueError("scoring eligibility gate must not search or fetch")

    @property
    def eligibility_hash(self) -> str:
        return canonical_hash(self.to_dict(include_hash=False))

    def to_dict(self, *, include_hash: bool = True) -> Mapping[str, Any]:
        payload = {
            "schema_version": "e2r_pro_full_thesis_eligibility_receipt_v1",
            "status": "FULL_THESIS_SCORE_ELIGIBLE",
            **asdict(self),
            "research_saturation_valid": True,
            "component_coverage": "7/7",
            "judge_coverage": "21/21",
            "score_valid": False,
            "canonical_stage": None,
            "stage_status": "FULL_THESIS_SCORE_PENDING",
            "publication_status": "WITHHELD_UNTIL_DETERMINISTIC_STAGECOURT",
            "pro_score_ignored": True,
            "pro_stage_ignored": True,
        }
        if include_hash:
            payload["eligibility_hash"] = canonical_hash(payload)
        return payload


class FullThesisPublicationGate:
    """Validate saturation before component work and lineage before scoring."""

    def evaluate_research(
        self,
        *,
        job: ProResearchJob,
        dossier: Mapping[str, Any],
        selected_archetype_id: str,
        saturation_receipt: Mapping[str, Any] | None,
        evidence_facts: Sequence[EvidenceFact],
        claim_fact_links: Sequence[Mapping[str, Any]],
    ) -> ResearchEligibilityDecision:
        fact_hash = canonical_hash(
            [row.to_dict() for row in sorted(evidence_facts, key=lambda row: row.fact_id)]
        )
        lineage_hash = _claim_lineage_hash(claim_fact_links)
        if not saturation_receipt:
            return _withheld_decision(
                job=job,
                selected_archetype_id=selected_archetype_id,
                fact_hash=fact_hash,
                lineage_hash=lineage_hash,
                reasons=("RESEARCH_SATURATION_RECEIPT_MISSING",),
            )

        receipt = dict(saturation_receipt)
        _validate_receipt_hash(receipt)
        pending_ids = _pending_question_ids(receipt)
        missing_roles = tuple(
            sorted(
                {
                    str(role)
                    for row in receipt.get("question_decisions") or ()
                    for role in (
                        *(row.get("missing_core_source_roles") or ()),
                        *(row.get("missing_corroboration_source_roles") or ()),
                    )
                    if str(role)
                }
            )
        )
        monitoring = tuple(
            sorted(
                {
                    str(row.get("question_family_id") or "")
                    for row in receipt.get("question_decisions") or ()
                    if (row.get("availability") or {}).get("monitoring_only") is True
                    or row.get("gap_class") in {"CORROBORATION_CAP", "MONITORING_GAP"}
                }
                - {""}
            )
        )
        reasons = _saturation_failure_reasons(
            job=job,
            dossier=dossier,
            selected_archetype_id=selected_archetype_id,
            receipt=receipt,
        )
        if reasons:
            return _withheld_decision(
                job=job,
                selected_archetype_id=selected_archetype_id,
                fact_hash=fact_hash,
                lineage_hash=lineage_hash,
                reasons=reasons,
                pending_ids=pending_ids,
                missing_roles=missing_roles,
                monitoring=monitoring,
                saturation_receipt_hash=str(receipt.get("receipt_hash") or "") or None,
                research_status=str(
                    receipt.get("deterministic_research_status")
                    or "RESEARCH_INCOMPLETE"
                ),
            )
        return ResearchEligibilityDecision(
            job_id=job.job_id,
            selected_archetype_id=selected_archetype_id,
            status="RESEARCH_SATURATION_VALID",
            research_status="FULL_THESIS_READY",
            research_saturation_valid=True,
            component_entry_allowed=True,
            score_valid=False,
            canonical_stage=None,
            stage_status="FULL_THESIS_COMPONENT_PENDING",
            publication_status="WITHHELD_UNTIL_DETERMINISTIC_STAGECOURT",
            saturation_receipt_hash=str(receipt["receipt_hash"]),
            verified_fact_roster_hash=fact_hash,
            claim_lineage_roster_hash=lineage_hash,
            pending_question_ids=(),
            missing_source_roles=missing_roles,
            monitoring_conditions=monitoring,
            withhold_reasons=(),
        )

    def evaluate_full_thesis(
        self,
        *,
        research: ResearchEligibilityDecision,
        memos: Sequence[ComponentResearchMemo],
        judges: JudgeBridgeResult,
        evidence_facts: Sequence[EvidenceFact],
        claim_fact_links: Sequence[Mapping[str, Any]],
        validated_impacts: Sequence[CreditValidatedImpact],
    ) -> FullThesisEligibilityReceipt:
        if not research.research_saturation_valid or not research.component_entry_allowed:
            raise ValueError("full thesis scoring requires valid research saturation")
        memo_rows = tuple(memos)
        memo_ids = {row.component_id for row in memo_rows}
        if (
            len(memo_rows) != 7
            or memo_ids != set(CANONICAL_COMPONENT_ORDER)
            or not all(row.research_complete for row in memo_rows)
        ):
            raise ValueError("full thesis scoring requires seven terminal component memos")
        if not judges.score_valid or len(judges.decisions) != 21:
            raise ValueError("full thesis scoring requires twenty-one terminal Judges")
        fact_ids = {row.fact_id for row in evidence_facts}
        lineage = {
            (str(row.get("claim_id") or ""), str(row.get("fact_id") or ""))
            for row in claim_fact_links
            if str(row.get("claim_id") or "") and str(row.get("fact_id") or "")
        }
        if any(fact_id not in fact_ids for _claim_id, fact_id in lineage):
            raise ValueError("claim lineage references an unknown verified EvidenceFact")
        for impact in validated_impacts:
            if not any(
                claim_id == impact.claim_id and fact_id in fact_ids
                for claim_id, fact_id in lineage
            ):
                raise ValueError("nonzero score candidate lacks accepted claim/fact lineage")
        return FullThesisEligibilityReceipt(
            job_id=research.job_id,
            selected_archetype_id=research.selected_archetype_id,
            research_eligibility_hash=research.decision_hash,
            saturation_receipt_hash=str(research.saturation_receipt_hash),
            verified_fact_roster_hash=research.verified_fact_roster_hash,
            claim_lineage_roster_hash=research.claim_lineage_roster_hash,
            component_memo_hash=canonical_hash([row.to_dict() for row in memo_rows]),
            judge_decision_hash=canonical_hash(
                [row.to_dict() for row in judges.decisions]
            ),
            component_count=len(memo_rows),
            component_terminal_count=sum(row.research_complete for row in memo_rows),
            judge_count=len(judges.decisions),
            claim_lineage_count=len(lineage),
            impact_count=len(tuple(validated_impacts)),
        )


def research_incomplete_result(
    decision: ResearchEligibilityDecision,
    *,
    diagnostic_partial_score: float | None = None,
    diagnostic_partial_stage: str | None = None,
    diagnostic_component_vector: Mapping[str, float] | None = None,
    diagnostic_score_interval: Mapping[str, float | None] | None = None,
    component_coverage: str = "0/7",
    judge_coverage: str = "0/21",
    current_verified_fact_ids: Sequence[str] = (),
) -> Mapping[str, Any]:
    """Build a dashboard-safe, explicitly non-final diagnostic record."""

    payload = {
        "schema_version": "e2r_pro_research_incomplete_result_v1",
        "job_id": decision.job_id,
        "selected_archetype_id": decision.selected_archetype_id,
        "research_status": "RESEARCH_INCOMPLETE",
        "research_saturation_valid": decision.research_saturation_valid,
        "pending_question_ids": list(decision.pending_question_ids),
        "missing_source_roles": list(decision.missing_source_roles),
        "monitoring_conditions": list(decision.monitoring_conditions),
        "current_verified_fact_ids": sorted(
            dict.fromkeys(str(value) for value in current_verified_fact_ids)
        ),
        "diagnostic_partial_score": diagnostic_partial_score,
        "diagnostic_partial_stage": diagnostic_partial_stage,
        "diagnostic_component_vector": dict(diagnostic_component_vector or {}),
        "diagnostic_score_interval": dict(diagnostic_score_interval or {}),
        "component_coverage": component_coverage,
        "judge_coverage": judge_coverage,
        "full_thesis_score": None,
        "score_valid": False,
        "canonical_stage": None,
        "stage_status": "RESEARCH_INCOMPLETE",
        "publication_status": WITHHELD,
        "withhold_reasons": list(decision.withhold_reasons),
        "research_eligibility_hash": decision.decision_hash,
        "score_authority": "ResearchCalibratedComponentScorer",
        "stage_authority": "AtomicStageCourtV2",
        "pro_score_ignored": True,
        "pro_stage_ignored": True,
    }
    return {**payload, "result_hash": canonical_hash(payload)}


def validate_full_thesis_eligibility_receipt(
    receipt: Mapping[str, Any],
    *,
    expected_job_id: str,
) -> None:
    payload = dict(receipt)
    identity = payload.pop("eligibility_hash", None)
    if (
        payload.get("schema_version")
        != "e2r_pro_full_thesis_eligibility_receipt_v1"
        or payload.get("status") != "FULL_THESIS_SCORE_ELIGIBLE"
        or payload.get("job_id") != expected_job_id
        or payload.get("research_saturation_valid") is not True
        or payload.get("component_coverage") != "7/7"
        or payload.get("judge_coverage") != "21/21"
        or payload.get("component_count") != 7
        or payload.get("component_terminal_count") != 7
        or payload.get("judge_count") != 21
        or payload.get("score_authority") is not False
        or payload.get("stage_authority") is not False
        or payload.get("query_count") != 0
        or payload.get("fetch_count") != 0
        or identity != canonical_hash(payload)
    ):
        raise ValueError("invalid full-thesis eligibility receipt")


def _saturation_failure_reasons(
    *,
    job: ProResearchJob,
    dossier: Mapping[str, Any],
    selected_archetype_id: str,
    receipt: Mapping[str, Any],
) -> tuple[str, ...]:
    reasons: list[str] = []
    if dossier.get("schema_version") not in {
        "e2r_pro_research_dossier_v2",
        "e2r_pro_research_dossier_v3",
    }:
        reasons.append("RESEARCH_DOSSIER_V2_OR_V3_REQUIRED")
    if receipt.get("schema_version") != "e2r_pro_research_saturation_receipt_v2":
        reasons.append("SATURATION_SCHEMA_INVALID")
    if receipt.get("job_id") != job.job_id:
        reasons.append("SATURATION_JOB_ID_MISMATCH")
    if receipt.get("target_id") not in {job.symbol, str((dossier.get("target") or {}).get("target_id") or "")}:
        reasons.append("SATURATION_TARGET_MISMATCH")
    if receipt.get("as_of_date") != job.as_of_date:
        reasons.append("SATURATION_AS_OF_DATE_MISMATCH")
    selected = tuple(str(value) for value in receipt.get("selected_archetype_ids") or ())
    dossier_selected = tuple(str(value) for value in dossier.get("selected_archetypes") or ())
    if selected_archetype_id not in selected or selected != dossier_selected:
        reasons.append("SATURATION_ARCHETYPE_SCOPE_MISMATCH")
    try:
        bundle = select_contract_bundle(selected)
    except (TypeError, ValueError) as exc:
        reasons.append(f"SATURATION_CONTRACT_BUNDLE_INVALID:{type(exc).__name__}")
    else:
        expected = tuple(
            str(question["question_family_id"])
            for contract in bundle.contracts
            for question in contract["question_families"]
            if question.get("mandatory_for_full_thesis") is True
        )
        if tuple(receipt.get("selected_contract_ids") or ()) != bundle.contract_ids:
            reasons.append("SATURATION_CONTRACT_ROSTER_MISMATCH")
        if tuple(receipt.get("expected_mandatory_question_ids") or ()) != expected:
            reasons.append("SATURATION_MANDATORY_ROSTER_MISMATCH")
        decisions = tuple(receipt.get("question_decisions") or ())
        decision_ids = tuple(str(row.get("question_family_id") or "") for row in decisions)
        if decision_ids != expected:
            reasons.append("SATURATION_QUESTION_DECISION_ROSTER_MISMATCH")
        if any(
            row.get("ready") is not True
            or row.get("terminal") is not True
            or row.get("question_to_source_linkage_complete") is not True
            or tuple(row.get("failure_codes") or ())
            for row in decisions
        ):
            reasons.append("SATURATION_QUESTION_NOT_READY")
    blockers = {
        "missing_mandatory_question_ids": "MANDATORY_QUESTION_MISSING",
        "nonterminal_mandatory_question_ids": "MANDATORY_QUESTION_NONTERMINAL",
        "public_material_gap_question_ids": "PUBLIC_MATERIAL_GAP_OPEN",
        "verifier_repair_pending_ids": "VERIFIER_REPAIR_PENDING",
        "provider_parser_core_pending_question_ids": "CORE_PROVIDER_PARSER_PENDING",
        "lifecycle_hard_break_pending_ids": "HARD_BREAK_LIFECYCLE_PENDING",
        "source_linkage_incomplete_question_ids": "QUESTION_SOURCE_LINEAGE_INCOMPLETE",
    }
    for field, code in blockers.items():
        if tuple(receipt.get(field) or ()):
            reasons.append(code)
    if (
        receipt.get("status") != "FULL_THESIS_READY"
        or receipt.get("research_saturation_valid") is not True
        or receipt.get("component_entry_allowed") is not True
    ):
        reasons.append("RESEARCH_SATURATION_NOT_VALID")
    if receipt.get("score_authority") is not False or receipt.get("stage_authority") is not False:
        reasons.append("SATURATION_AUTHORITY_ESCALATION")
    return tuple(dict.fromkeys(reasons))


def _validate_receipt_hash(receipt: Mapping[str, Any]) -> None:
    payload = dict(receipt)
    identity = payload.pop("receipt_hash", None)
    if not isinstance(identity, str) or len(identity) != 64 or canonical_hash(payload) != identity:
        raise ValueError("research saturation receipt hash mismatch")


def _pending_question_ids(receipt: Mapping[str, Any]) -> tuple[str, ...]:
    fields = (
        "missing_mandatory_question_ids",
        "nonterminal_mandatory_question_ids",
        "public_material_gap_question_ids",
        "verifier_repair_pending_ids",
        "provider_parser_core_pending_question_ids",
        "lifecycle_hard_break_pending_ids",
        "source_linkage_incomplete_question_ids",
    )
    return tuple(
        dict.fromkeys(
            str(value)
            for field in fields
            for value in receipt.get(field) or ()
            if str(value)
        )
    )


def _claim_lineage_hash(rows: Sequence[Mapping[str, Any]]) -> str:
    normalized = sorted(
        (
            {
                "claim_id": str(row.get("claim_id") or ""),
                "fact_id": str(row.get("fact_id") or ""),
                "link_role": str(row.get("link_role") or ""),
            }
            for row in rows
            if str(row.get("claim_id") or "") and str(row.get("fact_id") or "")
        ),
        key=lambda row: (row["claim_id"], row["fact_id"], row["link_role"]),
    )
    return canonical_hash(normalized)


def _withheld_decision(
    *,
    job: ProResearchJob,
    selected_archetype_id: str,
    fact_hash: str,
    lineage_hash: str,
    reasons: Sequence[str],
    pending_ids: Sequence[str] = (),
    missing_roles: Sequence[str] = (),
    monitoring: Sequence[str] = (),
    saturation_receipt_hash: str | None = None,
    research_status: str = "RESEARCH_INCOMPLETE",
) -> ResearchEligibilityDecision:
    return ResearchEligibilityDecision(
        job_id=job.job_id,
        selected_archetype_id=selected_archetype_id,
        status="RESEARCH_INCOMPLETE",
        research_status=research_status,
        research_saturation_valid=False,
        component_entry_allowed=False,
        score_valid=False,
        canonical_stage=None,
        stage_status="RESEARCH_INCOMPLETE",
        publication_status=WITHHELD,
        saturation_receipt_hash=saturation_receipt_hash,
        verified_fact_roster_hash=fact_hash,
        claim_lineage_roster_hash=lineage_hash,
        pending_question_ids=tuple(dict.fromkeys(str(value) for value in pending_ids)),
        missing_source_roles=tuple(dict.fromkeys(str(value) for value in missing_roles)),
        monitoring_conditions=tuple(dict.fromkeys(str(value) for value in monitoring)),
        withhold_reasons=tuple(dict.fromkeys(str(value) for value in reasons)),
    )


__all__ = [
    "FullThesisEligibilityReceipt",
    "FullThesisPublicationGate",
    "ResearchEligibilityDecision",
    "WITHHELD",
    "research_incomplete_result",
    "validate_full_thesis_eligibility_receipt",
]

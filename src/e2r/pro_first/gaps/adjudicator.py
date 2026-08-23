"""Materiality-first gap adjudication over verified Pro dossier evidence."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping, Sequence

from e2r.research_brain.researcher_mode.evidence_gap import (
    EvidenceGapAssessment,
    EvidenceGapClass,
    EvidenceGapDisposition,
    EvidenceGapKey,
    GapScoreMaterialityAssessment,
    MissingSourceRole,
    accepted_lineage_profile,
    derive_objective_identity,
    guard_source_query_generation,
)

from ..ids import canonical_hash
from ..models import ProResearchJob


SUPPLEMENTAL_ALLOWED_LABELS = frozenset(
    {"CORE_SCORE_BLOCKER", "STAGE_BOUNDARY_GAP", "HARD_BREAK_GAP"}
)
SUPPLEMENTAL_PROHIBITED_LABELS = frozenset(
    {"CORROBORATION_CAP", "MONITORING_GAP"}
)


@dataclass(frozen=True)
class DeterministicGapContext:
    """Existing deterministic scorer/Stage/Red-Team bounds for one Pro gap.

    These values are supplied by E2R rules, never copied from the Pro proposal.
    The context deliberately carries deltas and bounded Stage outputs rather
    than a writable final score or final Stage.
    """

    dossier_gap_id: str
    component_lower_delta: Mapping[str, float]
    component_upper_delta: Mapping[str, float]
    deterministic_lower_stage: str | None = None
    deterministic_upper_stage: str | None = None
    executable_new_source_route_signatures: tuple[str, ...] = ()
    provider_or_parser_failure: bool = False
    provider_or_parser_recovered: bool = False
    direct_contradiction_or_hard_break_unresolved: bool = False
    required_red_team_evidence_missing: bool = False
    could_change_score: bool = False
    monitoring_only: bool = False
    new_current_event: bool = False
    official_first_attempted: bool = True
    official_gap_reasons: tuple[str, ...] = ()
    question_family_id: str | None = None
    mandatory_primary_source_roles: tuple[str, ...] = ()
    verified_primary_source_roles: tuple[str, ...] = ()
    missing_route_is_independent_corroboration: bool = False
    missing_predicate_is_new_core: bool = True
    public_route_fixpoint_reached: bool = False
    hard_break_polarity_resolved: bool = False
    score_stage_range_bounded: bool = False
    rationale: str = "deterministic gap materiality bounds"

    def __post_init__(self) -> None:
        if not self.dossier_gap_id.strip():
            raise ValueError("deterministic gap context requires dossier_gap_id")
        if not self.rationale.strip():
            raise ValueError("deterministic gap context requires a rationale")
        if (self.deterministic_lower_stage is None) != (
            self.deterministic_upper_stage is None
        ):
            raise ValueError("lower and upper deterministic Stage must be paired")
        routes = tuple(
            dict.fromkeys(
                str(value).strip()
                for value in self.executable_new_source_route_signatures
                if str(value).strip()
            )
        )
        object.__setattr__(self, "executable_new_source_route_signatures", routes)
        reasons = tuple(
            dict.fromkeys(
                str(value).strip()
                for value in self.official_gap_reasons
                if str(value).strip()
            )
        )
        object.__setattr__(self, "official_gap_reasons", reasons)
        question_family_id = str(self.question_family_id or "").strip() or None
        object.__setattr__(self, "question_family_id", question_family_id)
        mandatory_roles = tuple(
            dict.fromkeys(
                str(value).strip()
                for value in self.mandatory_primary_source_roles
                if str(value).strip()
            )
        )
        verified_roles = tuple(
            dict.fromkeys(
                str(value).strip()
                for value in self.verified_primary_source_roles
                if str(value).strip()
            )
        )
        object.__setattr__(self, "mandatory_primary_source_roles", mandatory_roles)
        object.__setattr__(self, "verified_primary_source_roles", verified_roles)
        if set(verified_roles) - set(mandatory_roles):
            raise ValueError(
                "verified primary roles must belong to the mandatory primary roster"
            )
        if self.missing_route_is_independent_corroboration and not question_family_id:
            raise ValueError(
                "independent corroboration requires an exact question-family id"
            )
        if reasons and not self.official_first_attempted and not all(
            reason.startswith("NO_DIRECT_CONNECTOR_FOR_REQUESTED_OFFICIAL_FAMILY:")
            for reason in reasons
        ):
            raise ValueError(
                "an unattempted official lane may only record deterministic connector absence"
            )
        if self.monitoring_only and any(
            (
                self.provider_or_parser_failure,
                self.direct_contradiction_or_hard_break_unresolved,
                self.required_red_team_evidence_missing,
                self.could_change_score,
            )
        ):
            raise ValueError("monitoring-only context cannot carry material blockers")

    @property
    def primary_question_supported(self) -> bool:
        mandatory = set(self.mandatory_primary_source_roles)
        verified = set(self.verified_primary_source_roles)
        return bool(self.question_family_id and mandatory and mandatory.issubset(verified))

    @property
    def corroboration_cap_eligible(self) -> bool:
        """Whether question-level evidence proves a true corroboration remainder.

        Component fact counts are deliberately absent.  A cap is allowed only
        after the exact mandatory question's primary roles and deterministic
        score/Stage/hard-break bounds have been established.
        """

        no_public_route_remaining = bool(
            not self.executable_new_source_route_signatures
            or self.public_route_fixpoint_reached
        )
        return bool(
            self.primary_question_supported
            and self.missing_route_is_independent_corroboration
            and not self.missing_predicate_is_new_core
            and no_public_route_remaining
            and self.hard_break_polarity_resolved
            and self.score_stage_range_bounded
            and not self.provider_or_parser_failure
            and not self.direct_contradiction_or_hard_break_unresolved
            and not self.required_red_team_evidence_missing
        )


@dataclass(frozen=True)
class ProGapDecision:
    dossier_gap_id: str
    key: EvidenceGapKey
    assessment: EvidenceGapAssessment
    materiality: GapScoreMaterialityAssessment
    planner_label: str
    supplemental_allowed: bool
    pro_proposed_gap_class: str
    pro_proposed_missing_source_role: str
    pro_proposed_materiality: Mapping[str, bool]
    deterministic_context: DeterministicGapContext
    reopen_reason: str | None = None

    def __post_init__(self) -> None:
        known = SUPPLEMENTAL_ALLOWED_LABELS | SUPPLEMENTAL_PROHIBITED_LABELS
        if self.planner_label not in known:
            raise ValueError("unknown Pro-first gap planner label")
        expected = self.planner_label in SUPPLEMENTAL_ALLOWED_LABELS
        if self.supplemental_allowed != expected:
            raise ValueError("supplemental permission disagrees with planner label")
        if self.supplemental_allowed != self.materiality.search_required:
            raise ValueError("supplemental permission disagrees with materiality")

    @property
    def decision_hash(self) -> str:
        return canonical_hash(self.to_dict(include_hash=False))

    def to_dict(self, *, include_hash: bool = True) -> Mapping[str, Any]:
        payload = {
            "schema_version": "e2r_pro_gap_decision_v1",
            "dossier_gap_id": self.dossier_gap_id,
            "evidence_gap_key": self.key.gap_key,
            "semantic_gap_id": self.key.semantic_gap_id,
            "key": self.key.to_dict(),
            "assessment": self.assessment.to_dict(),
            "materiality": self.materiality.to_dict(),
            "deterministic_evidence_class": self.assessment.gap_class.value,
            "planner_label": self.planner_label,
            "supplemental_allowed": self.supplemental_allowed,
            "pro_proposed_gap_class": self.pro_proposed_gap_class,
            "pro_proposed_missing_source_role": (
                self.pro_proposed_missing_source_role
            ),
            "pro_proposed_materiality": dict(self.pro_proposed_materiality),
            "pro_proposal_authoritative": False,
            "pro_proposal_matches_planner_label": (
                self.pro_proposed_gap_class == self.planner_label
            ),
            "deterministic_context": {
                **asdict(self.deterministic_context),
                "component_lower_delta": dict(
                    self.deterministic_context.component_lower_delta
                ),
                "component_upper_delta": dict(
                    self.deterministic_context.component_upper_delta
                ),
                "executable_new_source_route_signatures": list(
                    self.deterministic_context.executable_new_source_route_signatures
                ),
                "official_gap_reasons": list(
                    self.deterministic_context.official_gap_reasons
                ),
            },
            "reopen_reason": self.reopen_reason,
            "full_research_restart_allowed": False,
            "production_score_authority": False,
            "production_stage_authority": False,
        }
        if include_hash:
            payload["decision_hash"] = canonical_hash(payload)
        return payload


@dataclass(frozen=True)
class GapAdjudicationResult:
    decisions: tuple[ProGapDecision, ...]
    fact_snapshot_hash: str
    accepted_lineage_roster_hash: str

    @property
    def supplemental_decisions(self) -> tuple[ProGapDecision, ...]:
        return tuple(row for row in self.decisions if row.supplemental_allowed)

    @property
    def receipt_payload(self) -> Mapping[str, Any]:
        return {
            "schema_version": "e2r_pro_gap_adjudication_receipt_v1",
            "status": "GAP_ADJUDICATION_COMPLETE",
            "gap_count": len(self.decisions),
            "decision_count": len(self.decisions),
            "supplemental_gap_count": len(self.supplemental_decisions),
            "planner_label_counts": {
                label: sum(row.planner_label == label for row in self.decisions)
                for label in sorted(
                    SUPPLEMENTAL_ALLOWED_LABELS | SUPPLEMENTAL_PROHIBITED_LABELS
                )
            },
            "fact_snapshot_hash": self.fact_snapshot_hash,
            "accepted_lineage_roster_hash": self.accepted_lineage_roster_hash,
            "full_research_restart_count": 0,
            "pro_gap_class_authority": False,
            "pro_score_authority": False,
            "pro_stage_authority": False,
        }


class ProGapAdjudicator:
    def adjudicate(
        self,
        *,
        dossier: Mapping[str, Any],
        job: ProResearchJob,
        verified_facts: Sequence[Mapping[str, Any] | Any],
        claim_fact_links: Sequence[Mapping[str, Any] | Any],
        deterministic_contexts: Mapping[str, DeterministicGapContext],
        prior_dispositions: Sequence[EvidenceGapDisposition] = (),
    ) -> GapAdjudicationResult:
        facts = tuple(_mapping(row) for row in verified_facts)
        links = tuple(_mapping(row) for row in claim_fact_links)
        fact_snapshot_hash = canonical_hash(
            sorted(
                (dict(row) for row in facts),
                key=lambda row: str(row.get("fact_id") or ""),
            )
        )
        lineage = accepted_lineage_profile(
            links,
            active_fact_ids=tuple(str(row.get("fact_id") or "") for row in facts),
        )
        lineage_hash = str(lineage["accepted_lineage_roster_hash"])
        gap_rows = tuple(dossier.get("unresolved_gaps") or ())
        gap_ids = tuple(str(row.get("dossier_gap_id") or "") for row in gap_rows)
        if not all(gap_ids) or len(gap_ids) != len(set(gap_ids)):
            raise ValueError("dossier unresolved gaps require unique stable ids")
        if set(deterministic_contexts) != set(gap_ids):
            raise ValueError("every Pro gap requires one exact deterministic context")
        previous_by_semantic_id = {
            row.key.semantic_gap_id: row for row in prior_dispositions
        }
        if len(previous_by_semantic_id) != len(tuple(prior_dispositions)):
            raise ValueError("multiple prior dispositions exist for one semantic gap")
        decisions: list[ProGapDecision] = []
        for gap in gap_rows:
            gap_id = str(gap["dossier_gap_id"])
            context = deterministic_contexts[gap_id]
            if context.dossier_gap_id != gap_id:
                raise ValueError("deterministic context belongs to another Pro gap")
            required_families = tuple(
                str(value) for value in gap.get("required_source_families") or ()
            )
            affected = tuple(
                str(value) for value in gap.get("affected_component_ids") or ()
            )
            archetype_id = str(gap.get("archetype_id") or "")
            if archetype_id not in set(job.archetype_ids):
                raise ValueError("Pro gap archetype is outside the selected job")
            key = EvidenceGapKey(
                target_id=job.symbol,
                as_of_date=job.as_of_date,
                archetype_id=archetype_id,
                objective_identity=derive_objective_identity(
                    stable_objective_id=(
                        str(gap["stable_objective_id"])
                        if gap.get("stable_objective_id") is not None
                        else None
                    ),
                    affected_component_ids=affected,
                    required_source_family=required_families,
                    economic_mechanism_id=str(gap.get("economic_mechanism_id") or ""),
                    predicate_or_fact_need_id=str(
                        gap.get("predicate_or_fact_need_id") or ""
                    ),
                ),
                affected_component_ids=affected,
                required_source_family=required_families,
                economic_mechanism_id=str(gap.get("economic_mechanism_id") or ""),
                predicate_or_fact_need_id=str(
                    gap.get("predicate_or_fact_need_id") or ""
                ),
                fact_snapshot_hash=fact_snapshot_hash,
                accepted_lineage_roster_hash=lineage_hash,
            )
            explicitly_nonblocking = bool(
                context.monitoring_only or context.corroboration_cap_eligible
            )
            source_backed = (
                key.affected_component_ids if explicitly_nonblocking else ()
            )
            range_bounded = explicitly_nonblocking
            missing_role = (
                MissingSourceRole.MONITORING_ONLY
                if context.monitoring_only
                else MissingSourceRole.INDEPENDENT_CORROBORATION
                if context.corroboration_cap_eligible
                else MissingSourceRole.CORE_SCORE_SOURCE
            )
            assessment = EvidenceGapAssessment.classify(
                key=key,
                missing_source_role=missing_role,
                source_backed_component_ids=source_backed,
                component_range_bounded=range_bounded,
                provider_or_parser_failure=context.provider_or_parser_failure,
                direct_contradiction_or_hard_break_unresolved=(
                    context.direct_contradiction_or_hard_break_unresolved
                ),
                required_red_team_evidence_missing=(
                    context.required_red_team_evidence_missing
                ),
                could_change_score=context.could_change_score,
                could_change_stage=(
                    context.deterministic_lower_stage
                    != context.deterministic_upper_stage
                ),
                could_change_hard_break=(
                    context.direct_contradiction_or_hard_break_unresolved
                ),
                economic_reason=context.rationale,
                llm_proposed_gap_class=str(gap.get("proposed_gap_class") or ""),
            )
            crossing_without_route = bool(
                context.deterministic_lower_stage is not None
                and context.deterministic_lower_stage
                != context.deterministic_upper_stage
                and not context.executable_new_source_route_signatures
                and assessment.gap_class
                in {
                    EvidenceGapClass.CORROBORATION_CAP,
                    EvidenceGapClass.MONITORING_GAP,
                }
            )
            materiality = GapScoreMaterialityAssessment.assess(
                assessment=assessment,
                component_lower_delta=context.component_lower_delta,
                component_upper_delta=context.component_upper_delta,
                deterministic_lower_stage=context.deterministic_lower_stage,
                deterministic_upper_stage=context.deterministic_upper_stage,
                executable_new_source_route_exists=bool(
                    context.executable_new_source_route_signatures
                ),
                rationale=context.rationale,
                stage_cap_reason=(
                    "unconfirmed non-core gap keeps the deterministic lower Stage"
                    if crossing_without_route
                    else None
                ),
            )
            planner_label = _planner_label(assessment, materiality)
            supplemental_allowed = materiality.search_required
            if supplemental_allowed != (planner_label in SUPPLEMENTAL_ALLOWED_LABELS):
                raise ValueError("gap planner label cannot bypass materiality policy")
            previous = previous_by_semantic_id.get(key.semantic_gap_id)
            reopen_reason = None
            if previous is not None:
                reopen_reason = guard_source_query_generation(
                    disposition=previous,
                    candidate_key=key,
                    candidate_route_signatures=(
                        context.executable_new_source_route_signatures
                    ),
                    provider_or_parser_recovered=(
                        context.provider_or_parser_recovered
                    ),
                    new_current_event=context.new_current_event,
                )
            decisions.append(
                ProGapDecision(
                    dossier_gap_id=gap_id,
                    key=key,
                    assessment=assessment,
                    materiality=materiality,
                    planner_label=planner_label,
                    supplemental_allowed=supplemental_allowed,
                    pro_proposed_gap_class=str(gap.get("proposed_gap_class") or ""),
                    pro_proposed_missing_source_role=str(
                        gap.get("proposed_missing_source_role") or ""
                    ),
                    pro_proposed_materiality={
                        "could_change_score": gap.get("proposed_could_change_score")
                        is True,
                        "could_change_stage": gap.get("proposed_could_change_stage")
                        is True,
                        "could_change_hard_break": gap.get(
                            "proposed_could_change_hard_break"
                        )
                        is True,
                    },
                    deterministic_context=context,
                    reopen_reason=reopen_reason,
                )
            )
        return GapAdjudicationResult(
            decisions=tuple(decisions),
            fact_snapshot_hash=fact_snapshot_hash,
            accepted_lineage_roster_hash=lineage_hash,
        )


def _mapping(row: Mapping[str, Any] | Any) -> Mapping[str, Any]:
    if isinstance(row, Mapping):
        return row
    method = getattr(row, "to_dict", None)
    if callable(method):
        value = method()
        if isinstance(value, Mapping):
            return value
    raise TypeError("verified fact lineage rows must be mappings or expose to_dict")


def _planner_label(
    assessment: EvidenceGapAssessment,
    materiality: GapScoreMaterialityAssessment,
) -> str:
    if materiality.could_change_hard_break:
        return "HARD_BREAK_GAP"
    if materiality.could_cross_stage_boundary and materiality.search_required:
        return "STAGE_BOUNDARY_GAP"
    if assessment.gap_class is EvidenceGapClass.CORE_SCORE_BLOCKER:
        return "CORE_SCORE_BLOCKER"
    if assessment.gap_class is EvidenceGapClass.CORROBORATION_CAP:
        return "CORROBORATION_CAP"
    return "MONITORING_GAP"


__all__ = [
    "DeterministicGapContext",
    "GapAdjudicationResult",
    "ProGapAdjudicator",
    "ProGapDecision",
    "SUPPLEMENTAL_ALLOWED_LABELS",
    "SUPPLEMENTAL_PROHIBITED_LABELS",
]

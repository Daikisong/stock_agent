"""Compile Pro component analysis into existing ComponentResearchMemo rows."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from e2r.research_brain.researcher_mode.schemas import (
    CANONICAL_COMPONENT_ORDER,
    ComponentAnchor,
    ComponentResearchMemo,
    EvidenceFact,
)
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)

from ..ids import stable_id
from ..models import ProResearchJob


@dataclass(frozen=True)
class ComponentBridgeResult:
    memos: tuple[ComponentResearchMemo, ...]
    removed_unverified_dossier_fact_ids: tuple[str, ...]
    verified_dossier_to_evidence_fact: Mapping[str, str]

    @property
    def receipt_payload(self) -> Mapping[str, Any]:
        return {
            "schema_version": "e2r_pro_component_bridge_receipt_v1",
            "status": "COMPONENT_BRIDGE_COMPLETE",
            "component_count": len(self.memos),
            "research_complete_count": sum(row.research_complete for row in self.memos),
            "removed_unverified_dossier_fact_ids": list(
                self.removed_unverified_dossier_fact_ids
            ),
            "verified_dossier_fact_count": len(
                self.verified_dossier_to_evidence_fact
            ),
            "pro_score_authority": False,
            "pro_stage_authority": False,
        }


class ProComponentMemoCompiler:
    def compile(
        self,
        *,
        dossier: Mapping[str, Any],
        job: ProResearchJob,
        selected_archetype_id: str,
        verified_facts: Sequence[EvidenceFact | Mapping[str, Any]],
        source_verifications: Sequence[Mapping[str, Any]],
        claim_fact_links: Sequence[Mapping[str, Any]],
        gap_decisions: Sequence[Mapping[str, Any]],
        historical_anchors: Sequence[ComponentAnchor | Mapping[str, Any]],
    ) -> ComponentBridgeResult:
        if selected_archetype_id not in set(job.archetype_ids):
            raise ValueError("component bridge archetype is outside the selected job")
        contract = load_archetype_scoring_contract(selected_archetype_id)
        if set(contract.component_weights) != set(CANONICAL_COMPONENT_ORDER):
            raise ValueError("selected archetype contract lacks canonical seven components")
        facts = tuple(evidence_fact_from_mapping(row) for row in verified_facts)
        fact_by_id = {row.fact_id: row for row in facts}
        if len(fact_by_id) != len(facts):
            raise ValueError("verified EvidenceFact ids must be unique")
        claim_to_fact = {
            str(row.get("claim_id") or ""): str(row.get("fact_id") or "")
            for row in claim_fact_links
            if str(row.get("claim_id") or "") and str(row.get("fact_id") or "")
        }
        supplemental_fact_ids = {
            claim_to_fact[str(row.get("compiled_claim_id") or "")]
            for row in source_verifications
            if row.get("origin") == "PRO_SUPPLEMENTAL_MATERIAL_GAP"
            and str(row.get("compiled_claim_id") or "") in claim_to_fact
            and claim_to_fact[str(row.get("compiled_claim_id") or "")] in fact_by_id
        }
        dossier_to_fact = {
            str(row.get("dossier_fact_id") or ""): claim_to_fact[
                str(row.get("compiled_claim_id") or "")
            ]
            for row in source_verifications
            if row.get("status")
            in {"ACCEPTED_CURRENT", "ACCEPTED_COUNTER", "ACCEPTED_RESOLUTION"}
            and str(row.get("compiled_claim_id") or "") in claim_to_fact
            and claim_to_fact[str(row.get("compiled_claim_id") or "")] in fact_by_id
        }
        component_rows = dossier.get("component_research") or {}
        if set(component_rows) != set(CANONICAL_COMPONENT_ORDER):
            raise ValueError("Pro component analysis must cover exactly seven components")
        anchor_by_id = {
            _anchor_id(row): row for row in historical_anchors if _anchor_id(row)
        }
        removed: set[str] = set()
        memos: list[ComponentResearchMemo] = []
        for component_id in CANONICAL_COMPONENT_ORDER:
            row = component_rows[component_id]
            if not isinstance(row, Mapping):
                raise ValueError("Pro component analysis rows must be objects")
            eligible = {
                fact.fact_id
                for fact in facts
                if component_id in set(fact.allowed_component_ids)
            }
            explicit_keys = {
                "positive_fact_ids",
                "counter_fact_ids",
                "counterfact_ids",
                "resolution_fact_ids",
            }
            explicit = bool(explicit_keys & set(row))
            if explicit:
                positive, removed_positive = _project_dossier_ids(
                    row.get("positive_fact_ids") or (),
                    dossier_to_fact=dossier_to_fact,
                    eligible={
                        fact_id
                        for fact_id in eligible
                        if fact_by_id[fact_id].direction == "POSITIVE"
                    },
                )
                counter, removed_counter = _project_dossier_ids(
                    row.get("counter_fact_ids")
                    or row.get("counterfact_ids")
                    or (),
                    dossier_to_fact=dossier_to_fact,
                    eligible={
                        fact_id
                        for fact_id in eligible
                        if fact_by_id[fact_id].direction == "COUNTER"
                    },
                )
                resolution, removed_resolution = _project_dossier_ids(
                    row.get("resolution_fact_ids") or (),
                    dossier_to_fact=dossier_to_fact,
                    eligible={
                        fact_id
                        for fact_id in eligible
                        if fact_by_id[fact_id].direction == "RESOLUTION"
                    },
                )
                removed.update((*removed_positive, *removed_counter, *removed_resolution))
                positive = tuple(
                    dict.fromkeys(
                        (
                            *positive,
                            *(
                                fact_id
                                for fact_id in supplemental_fact_ids
                                if fact_id in eligible
                                and fact_by_id[fact_id].direction == "POSITIVE"
                            ),
                        )
                    )
                )
                counter = tuple(
                    dict.fromkeys(
                        (
                            *counter,
                            *(
                                fact_id
                                for fact_id in supplemental_fact_ids
                                if fact_id in eligible
                                and fact_by_id[fact_id].direction == "COUNTER"
                            ),
                        )
                    )
                )
                resolution = tuple(
                    dict.fromkeys(
                        (
                            *resolution,
                            *(
                                fact_id
                                for fact_id in supplemental_fact_ids
                                if fact_id in eligible
                                and fact_by_id[fact_id].direction == "RESOLUTION"
                            ),
                        )
                    )
                )
            else:
                positive = tuple(
                    fact.fact_id
                    for fact in facts
                    if fact.fact_id in eligible and fact.direction == "POSITIVE"
                )
                counter = tuple(
                    fact.fact_id
                    for fact in facts
                    if fact.fact_id in eligible and fact.direction == "COUNTER"
                )
                resolution = tuple(
                    fact.fact_id
                    for fact in facts
                    if fact.fact_id in eligible and fact.direction == "RESOLUTION"
                )
            context_fact_ids = tuple(
                fact.fact_id
                for fact in facts
                if fact.fact_id in eligible and fact.direction == "NEUTRAL"
            )
            fact_ids = {*positive, *counter, *resolution, *context_fact_ids}
            source_coverage = tuple(
                sorted(
                    {
                        source_id
                        for fact_id in fact_ids
                        for source_id in fact_by_id[fact_id].source_ids
                    }
                )
            )
            known_anchor_ids = tuple(
                anchor_id
                for anchor_id in row.get("historical_anchor_ids") or ()
                if str(anchor_id) in anchor_by_id
            )
            if not known_anchor_ids:
                known_anchor_ids = tuple(
                    anchor_id
                    for anchor_id, anchor in anchor_by_id.items()
                    if _anchor_component(anchor) == component_id
                    and _anchor_archetype(anchor) == selected_archetype_id
                )
            structured_metrics = _verified_metrics(
                row.get("structured_metrics") or {},
                eligible_fact_ids=fact_ids,
            )
            score_range = _proposed_range(
                row,
                maximum=float(contract.component_max_points[component_id]),
            )
            component_gaps = tuple(
                gap
                for gap in gap_decisions
                if component_id
                in set(
                    ((gap.get("assessment") or {}).get("affected_component_ids"))
                    or ()
                )
            )
            core_blocked = any(
                str(gap.get("deterministic_evidence_class") or "")
                == "CORE_SCORE_BLOCKER"
                for gap in component_gaps
            )
            uncertainties = tuple(
                dict.fromkeys(
                    (
                        *(
                            str(value)
                            for value in row.get("uncertainties") or ()
                            if str(value).strip()
                        ),
                        *(
                            "gap:" + str(gap.get("planner_label") or "")
                            for gap in component_gaps
                        ),
                    )
                )
            )
            memo_id = stable_id(
                "PROMEMO",
                {
                    "job_id": job.job_id,
                    "archetype_id": selected_archetype_id,
                    "component_id": component_id,
                    "fact_ids": sorted(fact_ids),
                },
            )
            memos.append(
                ComponentResearchMemo(
                    memo_id=memo_id,
                    target_id=job.symbol,
                    archetype_id=selected_archetype_id,
                    component_id=component_id,
                    component_max_points=float(
                        contract.component_max_points[component_id]
                    ),
                    positive_fact_ids=positive,
                    counter_fact_ids=counter,
                    resolution_fact_ids=resolution,
                    context_fact_ids=context_fact_ids,
                    structured_metrics=structured_metrics,
                    historical_anchor_ids=known_anchor_ids,
                    researcher_summary=_text(
                        row.get("researcher_summary") or row.get("summary"),
                        "Pro component analysis contains no narrative summary.",
                    ),
                    positive_case=_text(
                        row.get("positive_case"),
                        "No verified positive case was stated.",
                    ),
                    counter_case=_text(
                        row.get("counter_case"),
                        "No verified counter case was stated.",
                    ),
                    uncertainties=uncertainties,
                    source_coverage=source_coverage,
                    proposed_score_lower=score_range[0],
                    proposed_score_mid=score_range[1],
                    proposed_score_upper=score_range[2],
                    confidence=_probability(row.get("confidence"), default=0.5),
                    research_complete=not core_blocked,
                    nearest_positive_anchor_ids=tuple(
                        anchor_id
                        for anchor_id in row.get("nearest_positive_anchor_ids") or ()
                        if str(anchor_id) in set(known_anchor_ids)
                    ),
                    nearest_counter_anchor_ids=tuple(
                        anchor_id
                        for anchor_id in row.get("nearest_counter_anchor_ids") or ()
                        if str(anchor_id) in set(known_anchor_ids)
                    ),
                    why_not_higher=_text(
                        row.get("why_not_higher"),
                        "Only verified fact lineage may support a higher range.",
                    ),
                    why_not_lower=_text(
                        row.get("why_not_lower"),
                        "Verified counter and resolution lineage bound the lower range.",
                    ),
                    researcher_role="PRO_DOSSIER_COMPONENT_BRIDGE",
                )
            )
        return ComponentBridgeResult(
            memos=tuple(memos),
            removed_unverified_dossier_fact_ids=tuple(sorted(removed)),
            verified_dossier_to_evidence_fact=dict(sorted(dossier_to_fact.items())),
        )


def evidence_fact_from_mapping(
    row: EvidenceFact | Mapping[str, Any],
) -> EvidenceFact:
    if isinstance(row, EvidenceFact):
        return row
    return EvidenceFact(
        fact_id=str(row["fact_id"]),
        target_id=str(row["target_id"]),
        as_of_date=str(row["as_of_date"]),
        subject=str(row.get("subject") or ""),
        business_segment=str(row.get("business_segment") or ""),
        product_family=str(row.get("product_family") or ""),
        economic_mechanism=str(row.get("economic_mechanism") or ""),
        predicate=str(row.get("predicate") or ""),
        value=row.get("value"),
        unit=(str(row["unit"]) if row.get("unit") is not None else None),
        period=str(row.get("period") or ""),
        direction=str(row.get("direction") or ""),
        source_ids=tuple(row.get("source_ids") or ()),
        claim_ids=tuple(row.get("claim_ids") or ()),
        quote_ids=tuple(row.get("quote_ids") or ()),
        current_lifecycle=str(row.get("current_lifecycle") or ""),
        source_independence_group=str(row.get("source_independence_group") or ""),
        confidence=float(row.get("confidence") or 0.0),
        corroborating_independence_groups=tuple(
            row.get("corroborating_independence_groups") or ()
        ),
        question_family_tags=tuple(row.get("question_family_tags") or ()),
        primitive_tags=tuple(row.get("primitive_tags") or ()),
        allowed_component_ids=tuple(row.get("allowed_component_ids") or ()),
        structured_evidence_roles=tuple(row.get("structured_evidence_roles") or ()),
    )


def _project_dossier_ids(
    values: Sequence[Any],
    *,
    dossier_to_fact: Mapping[str, str],
    eligible: set[str],
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    projected: list[str] = []
    removed: list[str] = []
    for value in values:
        dossier_id = str(value)
        fact_id = dossier_to_fact.get(dossier_id)
        if fact_id is None or fact_id not in eligible:
            removed.append(dossier_id)
        else:
            projected.append(fact_id)
    return tuple(dict.fromkeys(projected)), tuple(dict.fromkeys(removed))


def _verified_metrics(
    values: Any,
    *,
    eligible_fact_ids: set[str],
) -> Mapping[str, Any]:
    if not isinstance(values, Mapping):
        return {}
    result = {}
    for key, value in values.items():
        if not isinstance(value, Mapping):
            continue
        fact_ids = {str(item) for item in value.get("fact_ids") or ()}
        if fact_ids and fact_ids.issubset(eligible_fact_ids):
            result[str(key)] = dict(value)
    return result


def _proposed_range(row: Mapping[str, Any], *, maximum: float) -> tuple[float, float, float]:
    nested = row.get("proposed_score_range") or {}
    if not isinstance(nested, Mapping):
        raise ValueError("Pro component proposed_score_range must be an object")
    raw = (
        row.get("proposed_score_lower", nested.get("lower", 0.0)),
        row.get("proposed_score_mid", nested.get("mid", 0.0)),
        row.get("proposed_score_upper", nested.get("upper", 0.0)),
    )
    try:
        values = tuple(float(value) for value in raw)
    except (TypeError, ValueError) as error:
        raise ValueError("Pro component range must be numeric") from error
    if not 0 <= values[0] <= values[1] <= values[2] <= maximum:
        raise ValueError("Pro component range exceeds the selected archetype contract")
    return values  # type: ignore[return-value]


def _anchor_id(row: ComponentAnchor | Mapping[str, Any]) -> str:
    return str(row.anchor_id if isinstance(row, ComponentAnchor) else row.get("anchor_id") or "")


def _anchor_component(row: ComponentAnchor | Mapping[str, Any]) -> str:
    return str(
        row.component_id if isinstance(row, ComponentAnchor) else row.get("component_id") or ""
    )


def _anchor_archetype(row: ComponentAnchor | Mapping[str, Any]) -> str:
    return str(
        row.archetype_id if isinstance(row, ComponentAnchor) else row.get("archetype_id") or ""
    )


def _text(value: Any, default: str) -> str:
    text = str(value or "").strip()
    return text or default


def _probability(value: Any, *, default: float) -> float:
    if value is None:
        return default
    try:
        number = float(value)
    except (TypeError, ValueError):
        normalized = (
            str(value)
            .strip()
            .upper()
            .replace("-", "_")
            .replace("/", "_")
            .replace(" ", "_")
        )
        tokens = set(normalized.split("_"))
        qualitative: list[float] = []
        if "LOW" in tokens:
            qualitative.append(0.35)
        if tokens.intersection({"MEDIUM", "MODERATE"}):
            qualitative.append(0.60)
        if "HIGH" in tokens:
            qualitative.append(0.80)
        if not qualitative:
            raise ValueError(
                "Pro component confidence must be numeric or use HIGH/MEDIUM/LOW labels"
            )
        # Compound labels describe confidence in several parts of one memo.
        # Use the weakest stated band so a prose label cannot inflate credit.
        number = min(qualitative)
    if not 0 <= number <= 1:
        raise ValueError("Pro component confidence must be between 0 and 1")
    return number


__all__ = [
    "ComponentBridgeResult",
    "ProComponentMemoCompiler",
    "evidence_fact_from_mapping",
]

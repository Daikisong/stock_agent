"""Research-derived component subcriterion model and deterministic aggregation."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import stable_hash
from e2r.research_brain.runtime.scoring_contracts import (
    load_archetype_scoring_contract,
)
from e2r.research_brain.runtime.scoring_contracts.scoring_policy_v2 import (
    load_scoring_policy_v2,
)

from .impact_validator import CreditValidatedImpact


DEFAULT_COMPONENT_MODEL_PATH = Path(
    "configs/e2r_component_scoring_models_v1.json"
)


@dataclass(frozen=True)
class ComponentSubcriterion:
    subcriterion_id: str
    max_points: float
    role: str
    aggregation_dimension: str
    allowed_primitive_ids: tuple[str, ...]
    allowed_question_family_ids: tuple[str, ...]
    allowed_directions: tuple[str, ...]
    counter_mode: str
    historical_case_refs: tuple[str, ...]


@dataclass(frozen=True)
class ComponentScoringModel:
    component_id: str
    max_points: float
    aggregation_mode: str
    missing_required_cap_fraction: float
    support_counter_rules: tuple[str, ...]
    correlation_groups: tuple[str, ...]
    subcriteria: tuple[ComponentSubcriterion, ...]


@dataclass(frozen=True)
class ArchetypeComponentScoringModel:
    archetype_id: str
    research_lineage: Mapping[str, str]
    components: tuple[ComponentScoringModel, ...]
    config_hash: str

    def by_component(self) -> Mapping[str, ComponentScoringModel]:
        return {row.component_id: row for row in self.components}


@dataclass(frozen=True)
class ComponentSubcriterionScore:
    score_id: str
    component_id: str
    subcriterion_id: str
    max_points: float
    role: str
    support_impact_ids: tuple[str, ...]
    counter_impact_ids: tuple[str, ...]
    resolution_impact_ids: tuple[str, ...]
    support_fraction: float
    counter_effect_fraction: float
    resolution_effect: float
    net_fraction: float
    points: float
    status: str
    historical_case_refs: tuple[str, ...]

    def to_dict(self) -> Mapping[str, Any]:
        return json.loads(json.dumps(asdict(self), ensure_ascii=False))


@dataclass(frozen=True)
class ComponentSubcriteriaScoringResult:
    status: str
    scores: tuple[ComponentSubcriterionScore, ...]
    component_points: Mapping[str, float]
    component_support_fractions: Mapping[str, float]
    unmapped_impact_ids: tuple[str, ...]
    audit: Mapping[str, Any]


def load_component_scoring_model(
    archetype_id: str,
    path: str | Path = DEFAULT_COMPONENT_MODEL_PATH,
) -> ArchetypeComponentScoringModel | None:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if payload.get("schema_version") != "e2r_component_scoring_models_v1":
        raise ValueError("component scoring model schema mismatch")
    raw = (payload.get("models") or {}).get(archetype_id)
    if raw is None:
        return None
    components = []
    for component in raw.get("components") or ():
        subcriteria = tuple(
            ComponentSubcriterion(
                subcriterion_id=str(row["subcriterion_id"]),
                max_points=float(row["max_points"]),
                role=str(row["role"]),
                aggregation_dimension=str(
                    row.get("aggregation_dimension") or "IMPACT_CREDIT"
                ),
                allowed_primitive_ids=tuple(row["allowed_primitive_ids"]),
                allowed_question_family_ids=tuple(
                    row["allowed_question_family_ids"]
                ),
                allowed_directions=tuple(row["allowed_directions"]),
                counter_mode=str(row["counter_mode"]),
                historical_case_refs=tuple(row["historical_case_refs"]),
            )
            for row in component.get("subcriteria") or ()
        )
        components.append(
            ComponentScoringModel(
                component_id=str(component["component_id"]),
                max_points=float(component["max_points"]),
                aggregation_mode=str(component["aggregation_mode"]),
                missing_required_cap_fraction=float(
                    component["missing_required_cap_fraction"]
                ),
                support_counter_rules=tuple(
                    component["support_counter_rules"]
                ),
                correlation_groups=tuple(component["correlation_groups"]),
                subcriteria=subcriteria,
            )
        )
    model_payload = {
        "archetype_id": archetype_id,
        "research_lineage": raw["research_lineage"],
        "components": raw["components"],
    }
    model = ArchetypeComponentScoringModel(
        archetype_id=archetype_id,
        research_lineage={
            str(key): str(value)
            for key, value in raw["research_lineage"].items()
        },
        components=tuple(components),
        config_hash=stable_hash(model_payload),
    )
    _validate_model(model)
    return model


def component_subcriteria_context(
    *,
    archetype_id: str,
    question_contracts: Sequence[Any],
    allowed_component_ids: Sequence[str],
) -> Mapping[str, tuple[Mapping[str, Any], ...]]:
    model = load_component_scoring_model(archetype_id)
    if model is None:
        return {}
    by_component = model.by_component()
    result: dict[str, list[Mapping[str, Any]]] = {
        component_id: [] for component_id in allowed_component_ids
    }
    for question in question_contracts:
        for component_id in question.allowed_component_ids:
            component = by_component.get(component_id)
            if component is None or component_id not in result:
                continue
            for subcriterion in component.subcriteria:
                primitive_match = (
                    "*" in subcriterion.allowed_primitive_ids
                    or bool(
                        set(question.allowed_primitive_ids).intersection(
                            subcriterion.allowed_primitive_ids
                        )
                    )
                )
                question_match = (
                    "*" in subcriterion.allowed_question_family_ids
                    or question.question_family_id
                    in subcriterion.allowed_question_family_ids
                )
                if not primitive_match or not question_match:
                    continue
                primitive_ids = (
                    tuple(question.allowed_primitive_ids)
                    if "*" in subcriterion.allowed_primitive_ids
                    else tuple(
                        primitive_id
                        for primitive_id in question.allowed_primitive_ids
                        if primitive_id in subcriterion.allowed_primitive_ids
                    )
                )
                result[component_id].append(
                    {
                        "subcriterion_id": subcriterion.subcriterion_id,
                        "question_family_id": question.question_family_id,
                        "role": subcriterion.role,
                        "aggregation_dimension": (
                            subcriterion.aggregation_dimension
                        ),
                        "subcriterion_max_points": subcriterion.max_points,
                        "aggregation_mode": component.aggregation_mode,
                        "allowed_primitive_ids": primitive_ids,
                        "allowed_directions": (
                            subcriterion.allowed_directions
                        ),
                        "counter_mode": subcriterion.counter_mode,
                    }
                )
    return {
        component_id: tuple(
            {
                (row["subcriterion_id"], row["question_family_id"]): row
                for row in rows
            }.values()
        )
        for component_id, rows in result.items()
    }


def score_component_subcriteria(
    *,
    model: ArchetypeComponentScoringModel,
    impacts: Sequence[CreditValidatedImpact],
) -> ComponentSubcriteriaScoringResult:
    by_component = model.by_component()
    assignments: dict[str, list[CreditValidatedImpact]] = {
        subcriterion.subcriterion_id: []
        for component in model.components
        for subcriterion in component.subcriteria
    }
    unmapped = []
    for impact in impacts:
        if impact.validated_credit_fraction <= 0:
            continue
        component = by_component.get(impact.component_id)
        subcriterion = (
            _resolve_subcriterion(component, impact)
            if component is not None
            else None
        )
        if subcriterion is None:
            unmapped.append(impact.impact_id)
            continue
        assignments[subcriterion.subcriterion_id].append(impact)

    scores = []
    component_points = {}
    component_support_fractions = {}
    for component in model.components:
        if component.aggregation_mode == "MAX_SOURCE_QUALITY":
            component_scores = list(
                _score_max_source_quality(
                    model=model,
                    component=component,
                    impacts=tuple(
                        row
                        for row in impacts
                        if row.component_id == component.component_id
                        and row.validated_credit_fraction > 0
                    ),
                )
            )
        else:
            component_scores = [
                _score_assigned_subcriterion(
                    model=model,
                    component=component,
                    subcriterion=subcriterion,
                    rows=assignments[subcriterion.subcriterion_id],
                )
                for subcriterion in component.subcriteria
            ]
        scores.extend(component_scores)
        raw_points = _aggregate_component_points(
            component=component,
            scores=component_scores,
        )
        missing_required = any(
            row.role == "REQUIRED" and row.support_fraction <= 0
            for row in component_scores
        )
        if component.aggregation_mode == "CAP_BY_MISSING_BRIDGE" and missing_required:
            raw_points = min(
                raw_points,
                component.max_points
                * component.missing_required_cap_fraction,
            )
        points = round(min(component.max_points, raw_points), 6)
        component_points[component.component_id] = points
        component_support_fractions[component.component_id] = round(
            points / component.max_points if component.max_points else 0.0,
            6,
        )
    critical = {
        "unmapped_nonzero_impact_count": len(unmapped),
        "subcriterion_points_over_budget_count": sum(
            row.points > row.max_points + 1e-9 for row in scores
        ),
        "component_points_over_budget_count": sum(
            component_points[row.component_id] > row.max_points + 1e-9
            for row in model.components
        ),
        "component_subcriterion_budget_mismatch_count": sum(
            abs(
                sum(item.max_points for item in row.subcriteria)
                - row.max_points
            )
            > 1e-9
            for row in model.components
        ),
        "same_impact_multi_subcriterion_count": 0,
    }
    critical_sum = sum(critical.values())
    return ComponentSubcriteriaScoringResult(
        status=(
            "COMPONENT_SUBCRITERIA_SCORING_PASS"
            if critical_sum == 0
            else "COMPONENT_SUBCRITERIA_SCORING_FAIL"
        ),
        scores=tuple(scores),
        component_points=component_points,
        component_support_fractions=component_support_fractions,
        unmapped_impact_ids=tuple(unmapped),
        audit={
            "schema_version": "e2r_component_subcriteria_scoring_audit_v1",
            "status": (
                "COMPONENT_SUBCRITERIA_SCORING_PASS"
                if critical_sum == 0
                else "COMPONENT_SUBCRITERIA_SCORING_FAIL"
            ),
            "model_hash": model.config_hash,
            "subcriterion_count": len(scores),
            "critical_counts": critical,
            "critical_count_sum": critical_sum,
        },
    )


def _score_assigned_subcriterion(
    *,
    model: ArchetypeComponentScoringModel,
    component: ComponentScoringModel,
    subcriterion: ComponentSubcriterion,
    rows: Sequence[CreditValidatedImpact],
) -> ComponentSubcriterionScore:
    support = tuple(row for row in rows if row.support_credit_fraction > 0)
    counter = tuple(row for row in rows if row.counter_effect_fraction > 0)
    resolution = tuple(row for row in rows if row.resolution_effect > 0)
    support_fraction = min(
        1.0, sum(row.support_credit_fraction for row in support)
    )
    counter_fraction = min(
        1.0, sum(row.counter_effect_fraction for row in counter)
    )
    resolution_effect = max(
        (row.resolution_effect for row in resolution), default=0.0
    )
    return _make_subcriterion_score(
        model=model,
        component=component,
        subcriterion=subcriterion,
        support=support,
        counter=counter,
        resolution=resolution,
        support_fraction=support_fraction,
        counter_fraction=counter_fraction,
        resolution_effect=resolution_effect,
    )


def _score_max_source_quality(
    *,
    model: ArchetypeComponentScoringModel,
    component: ComponentScoringModel,
    impacts: Sequence[CreditValidatedImpact],
) -> tuple[ComponentSubcriterionScore, ...]:
    support = tuple(row for row in impacts if row.support_credit_fraction > 0)
    counter = tuple(row for row in impacts if row.counter_effect_fraction > 0)
    resolution = tuple(row for row in impacts if row.resolution_effect > 0)
    primary = max(
        support,
        key=lambda row: (
            row.source_cap,
            row.support_credit_fraction,
            row.evidence_confidence,
            row.impact_id,
        ),
        default=None,
    )
    corroborating = ()
    if primary is not None:
        independent = tuple(
            row
            for row in support
            if row.impact_id != primary.impact_id
            and row.source_independence_key != primary.source_independence_key
            and row.document_cluster_id != primary.document_cluster_id
        )
        if independent:
            corroborating = (
                max(
                    independent,
                    key=lambda row: (
                        row.support_credit_fraction,
                        row.source_cap,
                        row.evidence_confidence,
                        row.impact_id,
                    ),
                ),
            )
    result = []
    for subcriterion in component.subcriteria:
        dimension = subcriterion.aggregation_dimension
        dimension_support: tuple[CreditValidatedImpact, ...] = ()
        support_fraction = 0.0
        if primary is not None and dimension == "BEST_SOURCE_QUALITY":
            dimension_support = (primary,)
            support_fraction = min(
                primary.raw_credit_fraction,
                primary.source_cap,
            )
        elif primary is not None and dimension == "TARGET_DIRECTNESS":
            dimension_support = (primary,)
            support_fraction = min(
                primary.raw_credit_fraction,
                primary.causal_cap,
            )
        elif primary is not None and dimension == "CURRENT_ANCHOR":
            dimension_support = (primary,)
            support_fraction = min(
                primary.raw_credit_fraction,
                primary.temporal_cap,
            )
        elif dimension == "INDEPENDENT_CORROBORATION" and corroborating:
            dimension_support = corroborating
            support_fraction = corroborating[0].support_credit_fraction
        result.append(
            _make_subcriterion_score(
                model=model,
                component=component,
                subcriterion=subcriterion,
                support=dimension_support,
                counter=counter if dimension == "BEST_SOURCE_QUALITY" else (),
                resolution=(
                    resolution if dimension == "BEST_SOURCE_QUALITY" else ()
                ),
                support_fraction=support_fraction,
                counter_fraction=min(
                    1.0,
                    sum(row.counter_effect_fraction for row in counter),
                )
                if dimension == "BEST_SOURCE_QUALITY"
                else 0.0,
                resolution_effect=max(
                    (row.resolution_effect for row in resolution), default=0.0
                )
                if dimension == "BEST_SOURCE_QUALITY"
                else 0.0,
            )
        )
    return tuple(result)


def _make_subcriterion_score(
    *,
    model: ArchetypeComponentScoringModel,
    component: ComponentScoringModel,
    subcriterion: ComponentSubcriterion,
    support: Sequence[CreditValidatedImpact],
    counter: Sequence[CreditValidatedImpact],
    resolution: Sequence[CreditValidatedImpact],
    support_fraction: float,
    counter_fraction: float,
    resolution_effect: float,
) -> ComponentSubcriterionScore:
    effective_counter = counter_fraction * (1.0 - resolution_effect)
    net_fraction = max(0.0, support_fraction - effective_counter)
    points = round(subcriterion.max_points * net_fraction, 6)
    if support_fraction and effective_counter:
        status = "SUPPORT_WITH_COUNTER"
    elif support_fraction:
        status = "SUPPORTED"
    elif effective_counter:
        status = "COUNTER_ONLY"
    elif resolution_effect:
        status = "RESOLVED_COUNTER"
    else:
        status = "UNSUPPORTED"
    impact_ids = tuple(
        dict.fromkeys(
            row.impact_id for row in (*support, *counter, *resolution)
        )
    )
    return ComponentSubcriterionScore(
        score_id="SUBSCORE-"
        + stable_hash(
            {
                "model": model.config_hash,
                "subcriterion": subcriterion.subcriterion_id,
                "impacts": impact_ids,
            }
        )[:24],
        component_id=component.component_id,
        subcriterion_id=subcriterion.subcriterion_id,
        max_points=subcriterion.max_points,
        role=subcriterion.role,
        support_impact_ids=tuple(row.impact_id for row in support),
        counter_impact_ids=tuple(row.impact_id for row in counter),
        resolution_impact_ids=tuple(row.impact_id for row in resolution),
        support_fraction=round(support_fraction, 6),
        counter_effect_fraction=round(effective_counter, 6),
        resolution_effect=round(resolution_effect, 6),
        net_fraction=round(net_fraction, 6),
        points=points,
        status=status,
        historical_case_refs=subcriterion.historical_case_refs,
    )


def _aggregate_component_points(
    *,
    component: ComponentScoringModel,
    scores: Sequence[ComponentSubcriterionScore],
) -> float:
    if component.aggregation_mode == "COVERAGE_WEIGHTED":
        coverage = sum(
            (row.max_points / component.max_points) * row.net_fraction
            for row in scores
        )
        return component.max_points * coverage
    if component.aggregation_mode in {
        "SUM_DISTINCT_SUBCRITERIA",
        "MAX_SOURCE_QUALITY",
        "NET_SUPPORT_COUNTER",
        "CAP_BY_MISSING_BRIDGE",
    }:
        return sum(row.points for row in scores)
    raise ValueError("unknown component aggregation mode")


def audit_component_scoring_model(
    *, archetype_id: str = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
) -> Mapping[str, Any]:
    from .question_impact_contract import load_question_impact_contracts

    model = load_component_scoring_model(archetype_id)
    if model is None:
        raise ValueError("component scoring model is missing")
    contract = load_archetype_scoring_contract(archetype_id)
    policy = load_scoring_policy_v2()
    by_component = model.by_component()
    question_contracts = tuple(
        row
        for row in load_question_impact_contracts().values()
        if row.archetype_id == archetype_id
    )
    question_ids = {row.question_family_id for row in question_contracts}
    uncovered_edges = []
    for primitive_id, component_ids in (
        contract.primitive_to_component_allowed_edges.items()
    ):
        for component_id in component_ids:
            component = by_component.get(component_id)
            if component is None or not any(
                "*" in row.allowed_primitive_ids
                or primitive_id in row.allowed_primitive_ids
                for row in component.subcriteria
            ):
                uncovered_edges.append(
                    {"primitive_id": primitive_id, "component_id": component_id}
                )
    unknown_question_refs = [
        {
            "component_id": component.component_id,
            "subcriterion_id": subcriterion.subcriterion_id,
            "question_family_id": question_id,
        }
        for component in model.components
        for subcriterion in component.subcriteria
        for question_id in subcriterion.allowed_question_family_ids
        if question_id != "*" and question_id not in question_ids
    ]
    unreachable_subcriteria = [
        {
            "component_id": component.component_id,
            "subcriterion_id": subcriterion.subcriterion_id,
        }
        for component in model.components
        for subcriterion in component.subcriteria
        if not any(
            component.component_id in question.allowed_component_ids
            and (
                "*" in subcriterion.allowed_question_family_ids
                or question.question_family_id
                in subcriterion.allowed_question_family_ids
            )
            and (
                "*" in subcriterion.allowed_primitive_ids
                or bool(
                    set(subcriterion.allowed_primitive_ids).intersection(
                        question.allowed_primitive_ids
                    )
                )
            )
            for question in question_contracts
        )
    ]
    required_max_source_dimensions = {
        "BEST_SOURCE_QUALITY",
        "TARGET_DIRECTNESS",
        "CURRENT_ANCHOR",
        "INDEPENDENT_CORROBORATION",
    }
    critical = {
        "component_coverage_mismatch_count": len(
            set(contract.component_max_points) ^ set(by_component)
        ),
        "component_max_mismatch_count": sum(
            abs(
                by_component[component_id].max_points
                - contract.component_max_points[component_id]
            )
            > 1e-9
            for component_id in set(contract.component_max_points).intersection(
                by_component
            )
        ),
        "subcriterion_budget_sum_mismatch_count": sum(
            abs(sum(item.max_points for item in row.subcriteria) - row.max_points)
            > 1e-9
            for row in model.components
        ),
        "unknown_aggregation_mode_count": sum(
            row.aggregation_mode
            not in policy.enum_registry["component_aggregation_modes"]
            for row in model.components
        ),
        "unknown_counter_mode_count": sum(
            item.counter_mode
            not in policy.enum_registry["counter_effect_modes"]
            for row in model.components
            for item in row.subcriteria
        ),
        "unknown_question_family_count": len(unknown_question_refs),
        "unreachable_subcriterion_count": len(unreachable_subcriteria),
        "max_source_quality_dimension_mismatch_count": sum(
            {
                item.aggregation_dimension for item in row.subcriteria
            }
            != required_max_source_dimensions
            for row in model.components
            if row.aggregation_mode == "MAX_SOURCE_QUALITY"
        ),
        "missing_research_lineage_count": int(
            not all(model.research_lineage.values())
        ),
        "subcriterion_without_research_ref_count": sum(
            not item.historical_case_refs
            for row in model.components
            for item in row.subcriteria
        ),
        "uncovered_primitive_component_edge_count": len(uncovered_edges),
        "target_specific_exception_count": int(
            any(
                token in json.dumps(
                    {
                        "research_lineage": model.research_lineage,
                        "components": [asdict(row) for row in model.components],
                    },
                    ensure_ascii=False,
                ).casefold()
                for token in ("005930", "000660", "삼성전자", "sk하이닉스")
            )
        ),
    }
    critical_sum = sum(critical.values())
    audit = {
        "schema_version": "e2r_component_scoring_model_audit_v1",
        "status": (
            "COMPONENT_SCORING_MODEL_PASS"
            if critical_sum == 0
            else "COMPONENT_SCORING_MODEL_FAIL"
        ),
        "archetype_id": archetype_id,
        "model_hash": model.config_hash,
        "component_count": len(model.components),
        "subcriterion_count": sum(
            len(row.subcriteria) for row in model.components
        ),
        "component_models": [
            {
                **asdict(row),
                "subcriteria": [asdict(item) for item in row.subcriteria],
            }
            for row in model.components
        ],
        "uncovered_edges": uncovered_edges,
        "unknown_question_refs": unknown_question_refs,
        "unreachable_subcriteria": unreachable_subcriteria,
        "critical_counts": critical,
        "critical_count_sum": critical_sum,
    }
    return json.loads(json.dumps(audit, ensure_ascii=False))


def _resolve_subcriterion(
    component: ComponentScoringModel,
    impact: CreditValidatedImpact,
) -> ComponentSubcriterion | None:
    exact = next(
        (
            row
            for row in component.subcriteria
            if row.subcriterion_id == impact.component_subcriterion_id
        ),
        None,
    )
    if exact is not None:
        if not _subcriterion_allows(exact, impact):
            return None
        return exact
    candidates = [
        row
        for row in component.subcriteria
        if _subcriterion_allows(row, impact)
    ]
    if not candidates:
        return None
    candidates.sort(
        key=lambda row: (
            int(impact.question_family_id in row.allowed_question_family_ids),
            int(impact.primitive_id in row.allowed_primitive_ids),
            -component.subcriteria.index(row),
        ),
        reverse=True,
    )
    return candidates[0]


def _subcriterion_allows(
    row: ComponentSubcriterion, impact: CreditValidatedImpact
) -> bool:
    return (
        ("*" in row.allowed_primitive_ids or impact.primitive_id in row.allowed_primitive_ids)
        and (
            "*" in row.allowed_question_family_ids
            or not impact.question_family_id
            or impact.question_family_id in row.allowed_question_family_ids
        )
        and impact.direction in row.allowed_directions
    )


def _validate_model(model: ArchetypeComponentScoringModel) -> None:
    if not model.components or not all(model.research_lineage.values()):
        raise ValueError("component scoring model is incomplete")
    component_ids = [row.component_id for row in model.components]
    if len(component_ids) != len(set(component_ids)):
        raise ValueError("component scoring model has duplicate components")
    subcriterion_ids = [
        item.subcriterion_id
        for row in model.components
        for item in row.subcriteria
    ]
    if len(subcriterion_ids) != len(set(subcriterion_ids)):
        raise ValueError("component scoring model has duplicate subcriteria")
    for component in model.components:
        if not component.subcriteria:
            raise ValueError("component scoring model has no subcriteria")
        if abs(
            sum(row.max_points for row in component.subcriteria)
            - component.max_points
        ) > 1e-9:
            raise ValueError("subcriterion budgets do not sum to component max")
        if not 0 <= component.missing_required_cap_fraction <= 1:
            raise ValueError("component missing bridge cap is invalid")
        for row in component.subcriteria:
            if (
                row.role not in {"REQUIRED", "OPTIONAL"}
                or not row.allowed_primitive_ids
                or not row.allowed_question_family_ids
                or not row.allowed_directions
                or not row.historical_case_refs
            ):
                raise ValueError("component subcriterion contract is incomplete")


__all__ = [
    "ArchetypeComponentScoringModel",
    "ComponentScoringModel",
    "ComponentSubcriteriaScoringResult",
    "ComponentSubcriterion",
    "ComponentSubcriterionScore",
    "audit_component_scoring_model",
    "component_subcriteria_context",
    "load_component_scoring_model",
    "score_component_subcriteria",
]

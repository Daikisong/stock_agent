from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.runtime.scoring_contracts import load_archetype_scoring_contract
from e2r.research_brain.scoring.evidence_impact_rubric import (
    EvidenceImpactRubric,
    EvidenceImpactRubricCatalog,
)


DEFAULT_RECIPE_PATH = Path("configs/e2r_evidence_recipe_semantics_v1.json")
DEFAULT_SUPPLEMENT_PATH = Path("configs/e2r_evidence_impact_rubric_semantics_v1.json")
DEFAULT_HISTORICAL_PATH = Path("configs/e2r_historical_source_backed_replay_v1.json")


def _read(path: Path) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"rubric input must be an object: {path}")
    return payload


def _hash(payload: Any) -> str:
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def compile_evidence_impact_rubrics(
    archetype_id: str,
    *,
    recipe_path: str | Path = DEFAULT_RECIPE_PATH,
    supplemental_path: str | Path = DEFAULT_SUPPLEMENT_PATH,
    historical_path: str | Path = DEFAULT_HISTORICAL_PATH,
) -> EvidenceImpactRubricCatalog:
    recipe = _read(Path(recipe_path))
    supplemental = _read(Path(supplemental_path))
    historical = _read(Path(historical_path))
    contract = load_archetype_scoring_contract(archetype_id)
    rows: list[Mapping[str, Any]] = []
    for row in recipe.get("primitive_definitions") or ():
        if row.get("archetype_id") != archetype_id:
            continue
        primitive_id = str(row.get("primitive_id") or "")
        rows.append({
            "primitive_id": primitive_id,
            "allowed_component_ids": contract.primitive_to_component_allowed_edges.get(primitive_id, ()),
            "economic_mechanism": str(row.get("question_to_answer") or ""),
            "positive_predicates": tuple(row.get("positive_examples") or ()),
            "partial_predicates": tuple(row.get("semantic_tests") or ()),
            "counter_predicates": tuple(row.get("counterexamples") or ()),
            "unsupported_predicates": tuple(row.get("rejection_conditions") or ()),
        })
    archetype_supplement = (
        (supplemental.get("archetypes") or {}).get(archetype_id) or {}
    )
    rows.extend(archetype_supplement.get("supplemental_primitives") or ())
    cases = tuple(
        row for row in historical.get("cases") or ()
        if row.get("archetype_id") == archetype_id
    )
    rubrics: list[EvidenceImpactRubric] = []
    for row in rows:
        primitive_id = str(row.get("primitive_id") or "")
        declared_case_ids = set(str(value) for value in row.get("historical_case_ids") or ())
        matching = tuple(
            case for case in cases
            if case.get("primitive_id") == primitive_id
            or str(case.get("case_id") or "") in declared_case_ids
        )
        source_examples = tuple({
            "case_id": str(case.get("case_id") or ""),
            "source_role": str(case.get("source_role") or ""),
            "url": str(case.get("url") or ""),
            "as_of_date": str(case.get("as_of_date") or ""),
            "quote_contains": str(case.get("quote_contains") or ""),
            "predicate": str(case.get("predicate") or ""),
        } for case in matching)
        payload = {
            "archetype_id": archetype_id,
            "primitive_id": primitive_id,
            "allowed_component_ids": tuple(row.get("allowed_component_ids") or ()),
            "economic_mechanism": str(row.get("economic_mechanism") or ""),
            "positive_predicates": tuple(row.get("positive_predicates") or ()),
            "partial_predicates": tuple(row.get("partial_predicates") or ()),
            "counter_predicates": tuple(row.get("counter_predicates") or ()),
            "unsupported_predicates": tuple(row.get("unsupported_predicates") or ()),
            "strength_bands": {"NONE": 0.0, "WEAK": 0.25, "MODERATE": 0.5, "STRONG": 0.75, "VERY_STRONG": 1.0},
            "completeness_bands": {"MENTION": 0.2, "PARTIAL": 0.5, "SUBSTANTIAL": 0.8, "COMPLETE_FOR_PRIMITIVE": 1.0},
            "causal_distance_caps": {"DIRECT": 1.0, "ONE_HOP": 0.75, "TWO_HOP": 0.4, "INDUSTRY_ONLY": 0.0},
            "source_family_caps": dict(contract.source_tier_caps),
            "actual_vs_forward_rules": {"DIRECT_ACTUAL": 1.0, "DIRECT_FORWARD": 0.8, "PROFILE_ONLY": 0.2, "DISCOVERY_ONLY": 0.0},
            "evidence_family_diversity_rules": {"independent_family_bonus_allowed": True, "same_family_duplicate_bonus": 0.0},
            "double_count_correlation_rules": {"claim_total_fraction_cap": 1.0, "same_economic_effect_deduped": True},
            "positive_historical_case_refs": tuple(str(case.get("case_id")) for case in matching if case.get("source_role") == "POSITIVE"),
            "counterexample_refs": tuple(str(case.get("case_id")) for case in matching if case.get("source_role") != "POSITIVE"),
            "source_backed_examples": source_examples,
            "source_proxy_planning_only": True,
        }
        rubrics.append(EvidenceImpactRubric(rubric_id="EIR-" + _hash(payload)[:24], **payload))
    catalog_payload = [item.to_dict() for item in rubrics]
    return EvidenceImpactRubricCatalog(
        schema_version="e2r_evidence_impact_rubric_catalog_v1",
        archetype_id=archetype_id,
        rubrics=tuple(rubrics),
        policies={str(k): bool(v) for k, v in (supplemental.get("policies") or {}).items()},
        config_hash=_hash(catalog_payload),
    )


def audit_evidence_impact_rubrics(catalog: EvidenceImpactRubricCatalog) -> Mapping[str, Any]:
    serialized = json.dumps([item.to_dict() for item in catalog.rubrics], ensure_ascii=False).lower()
    critical = {
        "positive_predicate_missing_count": sum(not item.positive_predicates for item in catalog.rubrics),
        "partial_predicate_missing_count": sum(not item.partial_predicates for item in catalog.rubrics),
        "counter_predicate_missing_count": sum(not item.counter_predicates for item in catalog.rubrics),
        "unsupported_predicate_missing_count": sum(not item.unsupported_predicates for item in catalog.rubrics),
        "future_outcome_leakage_count": int(any(token in serialized for token in ('"mfe', '"mae', 'stage_after', 'future_price_outcome'))),
        "source_proxy_current_score_allowed_count": int(catalog.policies.get("source_proxy_current_score_allowed") is not False),
        "generic_verify_primitive_rubric_count": sum(item.economic_mechanism.strip().lower() == "verify primitive" for item in catalog.rubrics),
    }
    return {
        "schema_version": "e2r_evidence_impact_rubric_audit_v1",
        "status": "RESEARCH_CALIBRATED_IMPACT_RUBRIC_PASS" if sum(critical.values()) == 0 else "RESEARCH_CALIBRATED_IMPACT_RUBRIC_FAIL",
        "archetype_id": catalog.archetype_id,
        "rubric_count": len(catalog.rubrics),
        "source_backed_example_count": sum(len(item.source_backed_examples) for item in catalog.rubrics),
        "semantic_distinctions": [item.primitive_id for item in catalog.rubrics],
        "config_hash": catalog.config_hash,
        "critical_counts": critical,
        "critical_count_sum": sum(critical.values()),
    }


__all__ = ["audit_evidence_impact_rubrics", "compile_evidence_impact_rubrics"]

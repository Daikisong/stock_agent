"""Selection-bound compact score-lineage receipts for one Phase-106 canary.

The Phase-106 summary receipt deliberately stays small.  It is therefore not
enough to reproduce a score.  This module seals the complete compact lineage
for one selected canary: seven component decisions, twenty-one judge
decisions, every score-bearing fact and source, the accepted tracked anchors,
provider-call lineage, and the deterministic StageCourt input.

The compiler is benchmark-independent.  Its only upstream authority is the
validated Phase-105 selection manifest plus the eight exact receipt artifacts.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Mapping, Sequence
from datetime import date
import hashlib
import json
import math
import os
from pathlib import Path
import re
import secrets
from typing import Any

from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_selection import (
    _open_existing_directory_no_symlinks,
    _open_or_create_directory_no_symlinks,
    _read_regular_from_directory,
    validate_cross_archetype_canary_selection_manifest,
)
from e2r.production.v6_canary_results import (
    CANARY_RESULT_PASS,
    CANARY_RESULT_SCHEMA,
    build_full_researcher_mode_canary_receipt,
    validate_full_researcher_mode_canary_receipt,
    validate_full_researcher_mode_canary_result,
)
from e2r.research_brain.researcher_mode.canary_leaf_contract import (
    canary_output_tree_hash,
)
from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    CollaborationCodexSubagentTransport,
)
from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER
from e2r.research_brain.researcher_mode.tracked_receipts import (
    _anchor_receipts,
    _component_receipts,
    _decode_journal_envelope,
    _decision_rows,
    _fact_receipts,
    _judge_receipts,
    _provider_call_receipts,
    _recompute_stage,
    _source_receipts,
    _stage_receipt,
    _tracked_component_maxima,
    _tracked_historical_anchors,
    _verify_component_formula,
)


COMPACT_RECEIPT_SCHEMA = "e2r_v6_selection_bound_compact_receipt_v1"
COMPACT_RECEIPT_PASS = "E2R_V6_SELECTION_BOUND_COMPACT_RECEIPT_PASS"
COMPACT_REVIEW_SCHEMA = "e2r_v6_selection_bound_compact_review_v1"
COMPACT_REVIEW_PASS = "E2R_V6_SELECTION_BOUND_COMPACT_REVIEW_PASS"

RECEIPT_MANIFEST_NAME = "receipt_manifest.json"
REVIEW_DIRECTORY_NAME = "independent_reviews"
REVIEW_NAMES = ("review_a.json", "review_b.json")
REQUIRED_ARTIFACT_NAMES = (
    "score_receipt.json",
    "component_decisions.jsonl",
    "scoring_facts.jsonl",
    "judge_decisions.jsonl",
    "source_manifest.jsonl",
    "anchor_manifest.jsonl",
    "provider_calls.jsonl",
    "stagecourt_receipt.json",
)

_HEX64 = re.compile(r"[0-9a-f]{64}\Z")
_TARGET = re.compile(r"[0-9A-Z]{6}\Z")
_CANONICAL_STAGES = frozenset(
    {"0", "1", "2", "3-Green", "3-Yellow", "3-Red", "4A", "4B", "4C", "5"}
)
_JUDGE_ROLES = ("ANALYST", "SKEPTIC", "CALIBRATION_JUDGE")
_AUTHORIZED_PROVIDERS = frozenset({"CODEX", "COLLABORATION_CODEX"})

_MANIFEST_KEYS = frozenset(
    {
        "schema_version",
        "status",
        "receipt_id",
        "receipt_payload_hash",
        "selection_id",
        "selection_roster_hash",
        "target_id",
        "archetype_id",
        "as_of_date",
        "run_id",
        "result_id",
        "result_payload_hash",
        "production_receipt_id",
        "production_receipt_hash",
        "output_tree_hash",
        "artifact_names",
        "artifact_hashes",
        "artifact_roster_hash",
        "component_count",
        "judge_decision_count",
        "fact_count",
        "source_count",
        "anchor_count",
        "provider_call_count",
        "production_query_count",
        "production_document_count",
        "production_fact_count",
        "production_counterfact_count",
        "material_gap_count",
        "production_provider_call_count",
        "provider_error_count",
        "unauthorized_provider_call_count",
        "local_provider_call_count",
        "independent_review_count",
        "score_valid",
        "canonical_stage",
        "score_or_stage_authority",
    }
)
_SCORE_KEYS = frozenset(
    {
        "schema_version",
        "target_id",
        "as_of_date",
        "selection_id",
        "selection_roster_hash",
        "score_valid",
        "research_complete",
        "component_score_vector",
        "component_max_vector",
        "total_score",
        "canonical_stage",
        "canary_result",
        "production_receipt",
        "blind_review_inventory",
        "score_or_stage_authority",
    }
)
_COMPONENT_KEYS = frozenset(
    {
        "schema_version",
        "component_id",
        "max_points",
        "support_points",
        "counter_effect",
        "final_points",
        "confidence",
        "proposal_median",
        "consensus_band",
        "judge_proposals",
        "aggregation_method",
        "aggregator_config_hash",
        "support_fact_ids",
        "counter_fact_ids",
        "resolution_fact_ids",
        "anchor_ids",
        "judge_decision_ids",
    }
)
_BLIND_INVENTORY_KEYS = frozenset(
    {
        "fact_id",
        "target_id",
        "as_of_date",
        "subject_id",
        "business_segment",
        "product_family",
        "economic_mechanism",
        "fact_roles",
        "source_document_id",
        "source_family",
        "source_tier",
        "published_at",
        "available_at",
        "exact_quote_hash",
        "current_score_eligible",
    }
)
_FACT_KEYS = frozenset(
    {
        "schema_version",
        "fact_id",
        "target_id",
        "as_of_date",
        "component_ids",
        "fact_roles",
        "subject_id",
        "business_segment",
        "product_family",
        "economic_mechanism",
        "source_document_id",
        "document_content_hash",
        "exact_quote",
        "exact_quote_hash",
        "published_at",
        "available_at",
        "current_score_eligible",
        "extraction_provider_name",
        "provider_call_id",
        "provider_prompt_hash",
        "provider_response_hash",
        "accepted_fact_record_hash",
    }
)
_JUDGE_KEYS = frozenset(
    {
        "schema_version",
        "judge_decision_id",
        "component_id",
        "role",
        "proposed_points",
        "allowed_range",
        "support_fact_ids",
        "counter_fact_ids",
        "anchor_ids",
        "provider_call_id",
        "prompt_hash",
        "response_hash",
        "score_or_stage_authority",
    }
)
_SOURCE_KEYS = frozenset(
    {
        "schema_version",
        "source_document_id",
        "target_id",
        "as_of_date",
        "source_url",
        "source_title",
        "source_publisher",
        "source_tier",
        "source_family",
        "published_at",
        "available_at",
        "document_content_hash",
        "fact_ids",
        "fact_exact_quote_hashes",
        "accepted_source_record_hash",
    }
)
_ANCHOR_KEYS = frozenset(
    {
        "schema_version",
        "anchor_id",
        "component_id",
        "archetype_id",
        "max_points",
        "normalized_anchor_payload",
        "anchor_payload_hash",
    }
)
_PROVIDER_KEYS = frozenset(
    {
        "schema_version",
        "provider_call_id",
        "provider_name",
        "call_scope",
        "status",
        "prompt_hash",
        "response_hash",
        "judge_decision_ids",
        "fact_ids",
        "score_or_stage_authority",
    }
)
_STAGE_KEYS = frozenset(
    {
        "schema_version",
        "target_id",
        "as_of_date",
        "score_receipt_hash",
        "component_score_vector_hash",
        "total_score",
        "canonical_stage",
        "decision_status",
        "score_valid",
        "stage_final",
        "classification_input",
        "decision_trace_hash",
        "score_or_stage_authority",
    }
)
_REVIEW_KEYS = frozenset(
    {
        "schema_version",
        "status",
        "review_id",
        "reviewer_id",
        "provider_name",
        "provider_call_id",
        "prompt_hash",
        "response_hash",
        "selection_id",
        "selection_roster_hash",
        "receipt_id",
        "receipt_payload_hash",
        "target_id",
        "archetype_id",
        "as_of_date",
        "recomputed_component_score_vector",
        "recomputed_total_score",
        "recomputed_canonical_stage",
        "all_eight_artifacts_verified",
        "full_score_lineage_verified",
        "independent_review",
        "review_complete",
        "critical_findings",
        "critical_count_sum",
        "material_fact_omission_count",
        "counterfact_omission_count",
        "subject_or_segment_mismatch_count",
        "currentness_failure_count",
        "source_quality_failure_count",
        "component_calibration_failure_count",
        "historical_anchor_analogy_failure_count",
        "score_or_stage_authority",
    }
)

_SCHEMA_BY_ARTIFACT = {
    "score_receipt.json": "e2r_v6_canary_compact_score_v1",
    "component_decisions.jsonl": "e2r_v6_canary_compact_component_v1",
    "scoring_facts.jsonl": "e2r_v6_canary_compact_fact_v1",
    "judge_decisions.jsonl": "e2r_v6_canary_compact_judge_v1",
    "source_manifest.jsonl": "e2r_v6_canary_compact_source_v1",
    "anchor_manifest.jsonl": "e2r_v6_canary_compact_anchor_v1",
    "provider_calls.jsonl": "e2r_v6_canary_compact_provider_call_v1",
    "stagecourt_receipt.json": "e2r_v6_canary_compact_stagecourt_v1",
}
_ROW_KEYS_BY_ARTIFACT = {
    "component_decisions.jsonl": _COMPONENT_KEYS,
    "scoring_facts.jsonl": _FACT_KEYS,
    "judge_decisions.jsonl": _JUDGE_KEYS,
    "source_manifest.jsonl": _SOURCE_KEYS,
    "anchor_manifest.jsonl": _ANCHOR_KEYS,
    "provider_calls.jsonl": _PROVIDER_KEYS,
}


def _mapping(value: object, *, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{context} must be an object")
    return value


def _rows(value: object, *, context: str) -> tuple[Mapping[str, Any], ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise ValueError(f"{context} must be an array")
    return tuple(_mapping(row, context=f"{context} row") for row in value)


def _finite(value: object) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def _unique_strings(value: object, *, context: str) -> tuple[str, ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        raise ValueError(f"{context} must be an array")
    result = tuple(str(item) for item in value)
    if any(not item or item != item.strip() for item in result) or len(result) != len(set(result)):
        raise ValueError(f"{context} must contain unique nonempty strings")
    return result


def _index(rows: Sequence[Mapping[str, Any]], key: str, *, context: str) -> dict[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        identity = str(row.get(key) or "")
        if not identity or identity in result:
            raise ValueError(f"{context} identities must be unique")
        result[identity] = row
    return result


def _without_hash(payload: Mapping[str, Any], field: str) -> Mapping[str, Any]:
    return {key: value for key, value in payload.items() if key != field}


def _date_not_future(value: object, *, cutoff: date, context: str) -> None:
    try:
        parsed = date.fromisoformat(str(value)[:10])
    except ValueError as exc:
        raise ValueError(f"{context} must be an ISO date") from exc
    if parsed > cutoff:
        raise ValueError(f"{context} is after the canary as-of date")


def _selection_row(
    selection: Mapping[str, Any],
    *,
    selection_id: str,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    validate_cross_archetype_canary_selection_manifest(
        selection,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    matches = tuple(
        _mapping(row, context="selection row")
        for row in selection.get("selections") or ()
        if isinstance(row, Mapping) and row.get("selection_id") == selection_id
    )
    if len(matches) != 1:
        raise ValueError("receipt must bind exactly one current Phase-105 selection")
    return matches[0]


def _validate_artifact_shape(artifacts: Mapping[str, Any]) -> None:
    if set(artifacts) != set(REQUIRED_ARTIFACT_NAMES):
        raise ValueError("exact eight-artifact compact receipt roster is required")
    score = _mapping(artifacts["score_receipt.json"], context="score receipt")
    stage = _mapping(artifacts["stagecourt_receipt.json"], context="StageCourt receipt")
    if set(score) != _SCORE_KEYS or score.get("schema_version") != _SCHEMA_BY_ARTIFACT["score_receipt.json"]:
        raise ValueError("score receipt schema is not exact")
    if set(stage) != _STAGE_KEYS or stage.get("schema_version") != _SCHEMA_BY_ARTIFACT["stagecourt_receipt.json"]:
        raise ValueError("StageCourt receipt schema is not exact")
    for name, keys in _ROW_KEYS_BY_ARTIFACT.items():
        rows = _rows(artifacts[name], context=name)
        if any(set(row) != keys or row.get("schema_version") != _SCHEMA_BY_ARTIFACT[name] for row in rows):
            raise ValueError(f"{name} row schema is not exact")


def validate_selection_bound_canary_artifacts(
    *,
    selection: Mapping[str, Any],
    selection_id: str,
    artifacts: Mapping[str, Any],
    repo_root: str | Path,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Validate and return recomputed score facts for one compact receipt."""

    row = _selection_row(
        selection,
        selection_id=selection_id,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    _validate_artifact_shape(artifacts)
    target_id = str(row["target_id"])
    archetype_id = str(row["archetype_id"])
    as_of_date = str(row["selection_as_of_date"])
    if _TARGET.fullmatch(target_id) is None:
        raise ValueError("selection target is invalid")
    cutoff = date.fromisoformat(as_of_date)

    score = _mapping(artifacts["score_receipt.json"], context="score receipt")
    stage = _mapping(artifacts["stagecourt_receipt.json"], context="StageCourt receipt")
    components = _rows(artifacts["component_decisions.jsonl"], context="components")
    facts = _rows(artifacts["scoring_facts.jsonl"], context="facts")
    judges = _rows(artifacts["judge_decisions.jsonl"], context="judges")
    sources = _rows(artifacts["source_manifest.jsonl"], context="sources")
    anchors = _rows(artifacts["anchor_manifest.jsonl"], context="anchors")
    provider_calls = _rows(artifacts["provider_calls.jsonl"], context="provider calls")

    identity_fields = {
        "target_id": target_id,
        "as_of_date": as_of_date,
        "selection_id": selection_id,
        "selection_roster_hash": selection["selection_roster_hash"],
    }
    if any(score.get(key) != value for key, value in identity_fields.items()):
        raise ValueError("score receipt is not bound to the selected canary")
    canary_result = _mapping(score.get("canary_result"), context="full canary result")
    production_receipt = _mapping(
        score.get("production_receipt"), context="full canary production receipt"
    )
    validate_full_researcher_mode_canary_result(
        canary_result,
        selection=selection,
        selection_row=row,
    )
    validate_full_researcher_mode_canary_receipt(
        production_receipt,
        result=canary_result,
        selection=selection,
        selection_row=row,
    )
    if (
        score.get("score_valid") is not True
        or score.get("research_complete") is not True
        or score.get("score_or_stage_authority") is not False
        or score.get("canonical_stage") not in _CANONICAL_STAGES
    ):
        raise ValueError("score receipt is not a complete deterministic result")

    maxima = _mapping(score.get("component_max_vector"), context="component maxima")
    vector = _mapping(score.get("component_score_vector"), context="component vector")
    tracked_maxima = _tracked_component_maxima(repo_root=repo_root, archetype_id=archetype_id)
    if set(maxima) != set(CANONICAL_COMPONENT_ORDER) or set(vector) != set(CANONICAL_COMPONENT_ORDER):
        raise ValueError("score vectors must contain exactly seven components")
    if any(not _finite(maxima[key]) or float(maxima[key]) != float(tracked_maxima[key]) for key in CANONICAL_COMPONENT_ORDER):
        raise ValueError("component maxima are not bound to the tracked archetype profile")
    if any(not _finite(vector[key]) or not 0.0 <= float(vector[key]) <= float(maxima[key]) for key in CANONICAL_COMPONENT_ORDER):
        raise ValueError("component score vector is invalid")
    total = round(sum(float(vector[key]) for key in CANONICAL_COMPONENT_ORDER), 6)
    if not _finite(score.get("total_score")) or abs(float(score["total_score"]) - total) > 1e-9:
        raise ValueError("component sum does not reproduce total score")
    if (
        stable_hash(canary_result.get("component_score_vector")) != stable_hash(vector)
        or float(canary_result.get("total_score")) != total
        or canary_result.get("canonical_stage") != score.get("canonical_stage")
        or canary_result.get("score_valid") is not True
        or canary_result.get("stage_final") is not True
        or canary_result.get("full_researcher_mode_complete") is not True
    ):
        raise ValueError("compact score does not match the full canary result")

    if len(components) != 7 or tuple(str(item.get("component_id")) for item in components) != tuple(CANONICAL_COMPONENT_ORDER):
        raise ValueError("component decision roster must be the canonical ordered seven")
    component_by_id = _index(components, "component_id", context="component")
    judge_by_id = _index(judges, "judge_decision_id", context="judge")
    fact_by_id = _index(facts, "fact_id", context="fact")
    source_by_id = _index(sources, "source_document_id", context="source")
    anchor_by_id = _index(anchors, "anchor_id", context="anchor")
    provider_by_id = _index(provider_calls, "provider_call_id", context="provider call")
    inventory = _rows(score.get("blind_review_inventory"), context="blind review inventory")
    inventory_by_id = _index(inventory, "fact_id", context="blind review inventory")
    if not inventory or any(set(item) != _BLIND_INVENTORY_KEYS for item in inventory):
        raise ValueError("blind review inventory must contain exact accepted-fact rows")
    if not set(fact_by_id).issubset(inventory_by_id):
        raise ValueError("blind review inventory omits a score-bearing accepted fact")
    for inventory_fact_id, item in inventory_by_id.items():
        if (
            item.get("target_id") != target_id
            or item.get("as_of_date") != as_of_date
            or _HEX64.fullmatch(str(item.get("exact_quote_hash") or "")) is None
        ):
            raise ValueError(f"blind review inventory scope is invalid: {inventory_fact_id}")
        _date_not_future(item.get("published_at"), cutoff=cutoff, context="inventory published_at")
        _date_not_future(item.get("available_at"), cutoff=cutoff, context="inventory available_at")

    if len(judges) != 21:
        raise ValueError("exactly twenty-one judge decisions are required")
    if (
        canary_result.get("component_count") != len(components)
        or canary_result.get("judge_decision_count") != len(judges)
        or int(canary_result.get("fact_count") or 0) < len(facts)
        or int(canary_result.get("source_count") or 0) < len(sources)
    ):
        raise ValueError("full canary result does not cover the compact score artifacts")
    expected_fact_components: dict[str, set[str]] = defaultdict(set)
    expected_fact_roles: dict[str, set[str]] = defaultdict(set)
    expected_anchor_components: dict[str, set[str]] = defaultdict(set)
    for component_id in CANONICAL_COMPONENT_ORDER:
        component = component_by_id[component_id]
        if (
            not _finite(component.get("max_points"))
            or float(component["max_points"]) != float(maxima[component_id])
            or not _finite(component.get("final_points"))
            or float(component["final_points"]) != float(vector[component_id])
        ):
            raise ValueError(f"component score mismatch: {component_id}")
        component_judges = tuple(judge for judge in judges if judge.get("component_id") == component_id)
        if tuple(str(judge.get("role")) for judge in component_judges) != _JUDGE_ROLES:
            raise ValueError(f"component must have Analyst/Skeptic/Calibration once: {component_id}")
        declared_judges = _unique_strings(component.get("judge_decision_ids"), context="component judge IDs")
        if declared_judges != tuple(str(judge["judge_decision_id"]) for judge in component_judges):
            raise ValueError(f"component/judge roster is not bidirectional: {component_id}")
        union_support: set[str] = set()
        union_counter: set[str] = set()
        union_anchors: set[str] = set()
        for judge in component_judges:
            if judge.get("score_or_stage_authority") is not False:
                raise ValueError("judge cannot have score or Stage authority")
            if not _finite(judge.get("proposed_points")):
                raise ValueError("judge proposal must be finite")
            allowed = judge.get("allowed_range")
            if isinstance(allowed, (str, bytes)) or not isinstance(allowed, Sequence) or len(allowed) != 2 or any(not _finite(value) for value in allowed):
                raise ValueError("judge allowed range must be two finite numbers")
            lower, upper = (float(allowed[0]), float(allowed[1]))
            proposal = float(judge["proposed_points"])
            if not 0.0 <= lower <= proposal <= upper <= float(maxima[component_id]):
                raise ValueError("judge proposal is outside its valid range")
            union_support.update(_unique_strings(judge.get("support_fact_ids"), context="judge support facts"))
            union_counter.update(_unique_strings(judge.get("counter_fact_ids"), context="judge counter facts"))
            union_anchors.update(_unique_strings(judge.get("anchor_ids"), context="judge anchors"))
            if _HEX64.fullmatch(str(judge.get("prompt_hash") or "")) is None or _HEX64.fullmatch(str(judge.get("response_hash") or "")) is None:
                raise ValueError("judge prompt/response hashes are invalid")
        formula_failures: list[Mapping[str, Any]] = []
        _verify_component_formula(component, component_judges, formula_failures)
        if formula_failures:
            raise ValueError(
                f"component deterministic aggregation mismatch: {component_id}:"
                f"{formula_failures[0]['code']}"
            )
        judge_proposals = _mapping(
            component.get("judge_proposals"), context="component judge proposals"
        )
        if (
            component.get("aggregation_method")
            != "MEDIAN_WITH_ALLOWED_RANGE_INTERSECTION"
            or _HEX64.fullmatch(str(component.get("aggregator_config_hash") or ""))
            is None
            or set(judge_proposals) != set(_JUDGE_ROLES)
            or any(
                not _finite(judge_proposals.get(role))
                or float(judge_proposals[role])
                != float(next(judge["proposed_points"] for judge in component_judges if judge["role"] == role))
                for role in _JUDGE_ROLES
            )
        ):
            raise ValueError(f"component aggregation trace is incomplete: {component_id}")
        support = set(_unique_strings(component.get("support_fact_ids"), context="component support facts"))
        counter = set(_unique_strings(component.get("counter_fact_ids"), context="component counter facts"))
        resolution = set(_unique_strings(component.get("resolution_fact_ids"), context="component resolution facts"))
        anchor_ids = set(_unique_strings(component.get("anchor_ids"), context="component anchors"))
        if support != union_support or counter != union_counter or anchor_ids != union_anchors:
            raise ValueError(f"component evidence is not the exact judge union: {component_id}")
        for role, ids in (("SUPPORT", support), ("COUNTER", counter), ("RESOLUTION", resolution)):
            for fact_id in ids:
                expected_fact_components[fact_id].add(component_id)
                expected_fact_roles[fact_id].add(role)
        for anchor_id in anchor_ids:
            expected_anchor_components[anchor_id].add(component_id)

    if set(fact_by_id) != set(expected_fact_components):
        raise ValueError("accepted scoring fact roster is not exact and bidirectional")
    expected_source_facts: dict[str, set[str]] = defaultdict(set)
    expected_fact_provider_calls: dict[str, set[str]] = defaultdict(set)
    for fact_id, fact in fact_by_id.items():
        if set(fact.get("component_ids") or ()) != expected_fact_components[fact_id] or set(fact.get("fact_roles") or ()) != expected_fact_roles[fact_id]:
            raise ValueError(f"fact role/component linkage mismatch: {fact_id}")
        if (
            fact.get("target_id") != target_id
            or fact.get("as_of_date") != as_of_date
            or fact.get("current_score_eligible") is not True
            or _HEX64.fullmatch(str(fact.get("document_content_hash") or "")) is None
        ):
            raise ValueError(f"fact target/date/eligibility is invalid: {fact_id}")
        fact_provider_call_id = str(fact.get("provider_call_id") or "")
        if (
            not fact_provider_call_id
            or fact.get("extraction_provider_name") not in _AUTHORIZED_PROVIDERS
            or _HEX64.fullmatch(str(fact.get("provider_prompt_hash") or "")) is None
            or _HEX64.fullmatch(str(fact.get("provider_response_hash") or "")) is None
        ):
            raise ValueError(f"fact extraction provider lineage is invalid: {fact_id}")
        expected_fact_provider_calls[fact_provider_call_id].add(fact_id)
        quote = str(fact.get("exact_quote") or "")
        quote_hash = hashlib.sha256(quote.encode("utf-8")).hexdigest()
        if not quote or fact.get("exact_quote_hash") != quote_hash:
            raise ValueError(f"fact exact quote hash mismatch: {fact_id}")
        if fact.get("accepted_fact_record_hash") != stable_hash(_without_hash(fact, "accepted_fact_record_hash")):
            raise ValueError(f"accepted fact record hash mismatch: {fact_id}")
        inventory_item = inventory_by_id[fact_id]
        for field in (
            "target_id",
            "as_of_date",
            "subject_id",
            "business_segment",
            "product_family",
            "economic_mechanism",
            "source_document_id",
            "published_at",
            "available_at",
            "exact_quote_hash",
            "current_score_eligible",
        ):
            if inventory_item.get(field) != fact.get(field):
                raise ValueError(f"blind inventory/scoring fact mismatch: {fact_id}:{field}")
        _date_not_future(fact.get("published_at"), cutoff=cutoff, context="fact published_at")
        _date_not_future(fact.get("available_at"), cutoff=cutoff, context="fact available_at")
        source_id = str(fact.get("source_document_id") or "")
        if source_id not in source_by_id:
            raise ValueError(f"fact source is missing: {fact_id}")
        expected_source_facts[source_id].add(fact_id)

    if set(source_by_id) != set(expected_source_facts):
        raise ValueError("source roster must equal sources used by accepted facts")
    for source_id, source in source_by_id.items():
        fact_ids = set(_unique_strings(source.get("fact_ids"), context="source fact IDs"))
        if fact_ids != expected_source_facts[source_id]:
            raise ValueError(f"source/fact roster mismatch: {source_id}")
        if source.get("target_id") != target_id or source.get("as_of_date") != as_of_date:
            raise ValueError(f"source target/date mismatch: {source_id}")
        if _HEX64.fullmatch(str(source.get("document_content_hash") or "")) is None:
            raise ValueError(f"source document hash is invalid: {source_id}")
        _date_not_future(source.get("published_at"), cutoff=cutoff, context="source published_at")
        _date_not_future(source.get("available_at"), cutoff=cutoff, context="source available_at")
        quote_hashes = _mapping(source.get("fact_exact_quote_hashes"), context="source quote hashes")
        if set(quote_hashes) != fact_ids:
            raise ValueError(f"source quote roster mismatch: {source_id}")
        for fact_id in fact_ids:
            fact = fact_by_id[fact_id]
            inventory_item = inventory_by_id[fact_id]
            if (
                fact.get("document_content_hash") != source.get("document_content_hash")
                or quote_hashes[fact_id] != fact.get("exact_quote_hash")
                or inventory_item.get("source_family") != source.get("source_family")
                or inventory_item.get("source_tier") != source.get("source_tier")
            ):
                raise ValueError(f"fact/source content linkage mismatch: {fact_id}")
        if source.get("accepted_source_record_hash") != stable_hash(_without_hash(source, "accepted_source_record_hash")):
            raise ValueError(f"accepted source record hash mismatch: {source_id}")

    if set(anchor_by_id) != set(expected_anchor_components):
        raise ValueError("accepted anchor roster is not exact and bidirectional")
    tracked_anchors = {
        str(anchor["anchor_id"]): anchor
        for anchor in _tracked_historical_anchors(repo_root=repo_root, archetype_id=archetype_id)
    }
    for anchor_id, anchor in anchor_by_id.items():
        normalized = _mapping(anchor.get("normalized_anchor_payload"), context="anchor payload")
        if (
            anchor.get("archetype_id") != archetype_id
            or anchor.get("component_id") not in expected_anchor_components[anchor_id]
            or len(expected_anchor_components[anchor_id]) != 1
            or anchor.get("anchor_payload_hash") != stable_hash(normalized)
            or tracked_anchors.get(anchor_id) != normalized
            or not _finite(anchor.get("max_points"))
            or float(anchor["max_points"]) != float(maxima[str(anchor["component_id"])])
        ):
            raise ValueError(f"anchor is not bound to tracked current config: {anchor_id}")

    expected_provider_judges: dict[str, set[str]] = defaultdict(set)
    for judge_id, judge in judge_by_id.items():
        call_id = str(judge.get("provider_call_id") or "")
        if call_id not in provider_by_id:
            raise ValueError(f"judge provider call is missing: {judge_id}")
        expected_provider_judges[call_id].add(judge_id)
    expected_provider_ids = set(expected_provider_judges) | set(expected_fact_provider_calls)
    if set(provider_by_id) != expected_provider_ids:
        raise ValueError("provider-call roster must equal judge and fact call lineage")
    for call_id, call in provider_by_id.items():
        judge_ids = set(_unique_strings(call.get("judge_decision_ids"), context="provider judge IDs"))
        fact_ids = set(_unique_strings(call.get("fact_ids"), context="provider fact IDs"))
        call_scope = call.get("call_scope")
        if (
            judge_ids != expected_provider_judges.get(call_id, set())
            or fact_ids != expected_fact_provider_calls.get(call_id, set())
            or call.get("provider_name") not in _AUTHORIZED_PROVIDERS
            or call_scope not in {"COMPONENT_JUDGE", "FACT_EXTRACTION"}
            or (call_scope == "COMPONENT_JUDGE" and (not judge_ids or fact_ids))
            or (call_scope == "FACT_EXTRACTION" and (not fact_ids or judge_ids))
            or call.get("status") != "COMPLETED"
            or call.get("score_or_stage_authority") is not False
            or _HEX64.fullmatch(str(call.get("prompt_hash") or "")) is None
            or _HEX64.fullmatch(str(call.get("response_hash") or "")) is None
        ):
            raise ValueError(f"provider call is invalid: {call_id}")
        for judge_id in judge_ids:
            judge = judge_by_id[judge_id]
            if call.get("prompt_hash") != judge.get("prompt_hash") or call.get("response_hash") != judge.get("response_hash"):
                raise ValueError(f"provider/judge hash linkage mismatch: {judge_id}")
        for fact_id in fact_ids:
            fact = fact_by_id[fact_id]
            if (
                call.get("provider_name") != fact.get("extraction_provider_name")
                or call.get("prompt_hash") != fact.get("provider_prompt_hash")
                or call.get("response_hash") != fact.get("provider_response_hash")
            ):
                raise ValueError(f"provider/fact hash linkage mismatch: {fact_id}")

    if (
        stage.get("target_id") != target_id
        or stage.get("as_of_date") != as_of_date
        or stage.get("score_receipt_hash") != stable_hash(score)
        or stage.get("component_score_vector_hash") != stable_hash(vector)
        or not _finite(stage.get("total_score"))
        or abs(float(stage["total_score"]) - total) > 1e-9
        or stage.get("canonical_stage") != score.get("canonical_stage")
        or stage.get("decision_status") != "FINAL"
        or stage.get("score_valid") is not True
        or stage.get("stage_final") is not True
        or stage.get("score_or_stage_authority") is not False
    ):
        raise ValueError("StageCourt receipt is not bound to the score receipt")
    trace = {
        "score_receipt_hash": stage["score_receipt_hash"],
        "component_score_vector_hash": stage["component_score_vector_hash"],
        "total_score": stage["total_score"],
        "classification_input": stage["classification_input"],
        "canonical_stage": stage["canonical_stage"],
    }
    if stage.get("decision_trace_hash") != stable_hash(trace):
        raise ValueError("StageCourt decision trace hash mismatch")
    try:
        recomputed_stage = _recompute_stage(score, stage)
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError("StageCourt classification input is invalid") from exc
    if recomputed_stage != score.get("canonical_stage"):
        raise ValueError("canonical Stage does not recompute from deterministic rules")

    return {
        "selection_row": row,
        "component_score_vector": dict(vector),
        "component_max_vector": dict(maxima),
        "total_score": total,
        "canonical_stage": recomputed_stage,
        "component_count": len(components),
        "judge_decision_count": len(judges),
        "fact_count": len(facts),
        "source_count": len(sources),
        "anchor_count": len(anchors),
        "provider_call_count": len(provider_calls),
        "production_query_count": canary_result["query_count"],
        "production_document_count": canary_result["document_count"],
        "production_fact_count": canary_result["fact_count"],
        "production_counterfact_count": canary_result["counterfact_count"],
        "material_gap_count": canary_result["material_gap_count"],
        "production_provider_call_count": sum(
            int(value)
            for value in _mapping(
                canary_result["provider_call_counts"],
                context="provider call counts",
            ).values()
        ),
        "provider_error_count": canary_result["provider_error_count"],
        "unauthorized_provider_call_count": canary_result[
            "unauthorized_provider_call_count"
        ],
        "local_provider_call_count": canary_result[
            "local_provider_call_count"
        ],
        "run_id": canary_result["run_id"],
        "result_id": canary_result["result_id"],
        "result_payload_hash": stable_hash(canary_result),
        "production_receipt_id": production_receipt["receipt_id"],
        "production_receipt_hash": stable_hash(production_receipt),
        "output_tree_hash": canary_result["output_tree_hash"],
    }


def build_selection_bound_canary_manifest(
    *,
    selection: Mapping[str, Any],
    selection_id: str,
    artifacts: Mapping[str, Any],
    repo_root: str | Path,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Build a manifest only after all eight score-lineage artifacts validate."""

    verified = validate_selection_bound_canary_artifacts(
        selection=selection,
        selection_id=selection_id,
        artifacts=artifacts,
        repo_root=repo_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    row = verified["selection_row"]
    artifact_hashes = {name: stable_hash(artifacts[name]) for name in REQUIRED_ARTIFACT_NAMES}
    payload_scope = {
        "selection_id": selection_id,
        "selection_roster_hash": selection["selection_roster_hash"],
        "target_id": row["target_id"],
        "archetype_id": row["archetype_id"],
        "as_of_date": row["selection_as_of_date"],
        "artifact_hashes": artifact_hashes,
    }
    payload_hash = stable_hash(payload_scope)
    return {
        "schema_version": COMPACT_RECEIPT_SCHEMA,
        "status": COMPACT_RECEIPT_PASS,
        "receipt_id": "CANCOMPACT-" + payload_hash[:24],
        "receipt_payload_hash": payload_hash,
        "selection_id": selection_id,
        "selection_roster_hash": selection["selection_roster_hash"],
        "target_id": row["target_id"],
        "archetype_id": row["archetype_id"],
        "as_of_date": row["selection_as_of_date"],
        "run_id": verified["run_id"],
        "result_id": verified["result_id"],
        "result_payload_hash": verified["result_payload_hash"],
        "production_receipt_id": verified["production_receipt_id"],
        "production_receipt_hash": verified["production_receipt_hash"],
        "output_tree_hash": verified["output_tree_hash"],
        "artifact_names": list(REQUIRED_ARTIFACT_NAMES),
        "artifact_hashes": artifact_hashes,
        "artifact_roster_hash": stable_hash(
            [{"name": name, "payload_hash": artifact_hashes[name]} for name in REQUIRED_ARTIFACT_NAMES]
        ),
        "component_count": verified["component_count"],
        "judge_decision_count": verified["judge_decision_count"],
        "fact_count": verified["fact_count"],
        "source_count": verified["source_count"],
        "anchor_count": verified["anchor_count"],
        "provider_call_count": verified["provider_call_count"],
        "production_query_count": verified["production_query_count"],
        "production_document_count": verified["production_document_count"],
        "production_fact_count": verified["production_fact_count"],
        "production_counterfact_count": verified[
            "production_counterfact_count"
        ],
        "material_gap_count": verified["material_gap_count"],
        "production_provider_call_count": verified[
            "production_provider_call_count"
        ],
        "provider_error_count": verified["provider_error_count"],
        "unauthorized_provider_call_count": verified[
            "unauthorized_provider_call_count"
        ],
        "local_provider_call_count": verified["local_provider_call_count"],
        "independent_review_count": 2,
        "score_valid": True,
        "canonical_stage": verified["canonical_stage"],
        "score_or_stage_authority": False,
    }


def _read_current_json(path: Path) -> Mapping[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"required current output leaf is unavailable: {path.name}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"required current output leaf is invalid: {path.name}") from exc
    return _mapping(payload, context=path.name)


def _read_current_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"required current output leaf is unavailable: {path.name}")
    try:
        return tuple(
            _mapping(json.loads(line), context=path.name)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"required current output leaf is invalid: {path.name}") from exc


def _normalized_provider_name(value: object) -> str:
    normalized = str(value or "").strip().upper()
    if normalized in _AUTHORIZED_PROVIDERS:
        return normalized
    if normalized == "COLLABORATION_CODEX_SUBAGENT_STRUCTURED_RESEARCHER_MODE":
        return "COLLABORATION_CODEX"
    if normalized == "CODEX_STRUCTURED_RESEARCHER_MODE":
        return "CODEX"
    raise ValueError("current output names an unauthorized research provider")


def _sequence_gap_count(value: object) -> int:
    if value is None:
        return 0
    if isinstance(value, Mapping):
        return len(value)
    if isinstance(value, Sequence) and not isinstance(
        value, (str, bytes, bytearray)
    ):
        return len(value)
    return int(bool(value))


def _material_gap_count(
    *,
    saturation: Mapping[str, Any],
    supervisor: Mapping[str, Any],
) -> int:
    """Recount unresolved semantic material directly from terminal leaves."""

    return sum(
        _sequence_gap_count(value)
        for value in (
            saturation.get("pending_reasons"),
            supervisor.get("unresolved_material_questions"),
            supervisor.get("missing_material_facts"),
            supervisor.get("parser_or_extractor_failures"),
            supervisor.get("reasonable_positive_routes_remaining"),
            supervisor.get("next_actions"),
        )
    )


def _production_provider_accounting(
    provider_audit: Mapping[str, Any],
    *,
    terminal_output_complete: bool,
) -> Mapping[str, int | str]:
    """Fail closed on current calls without criminalizing immutable history.

    Collaboration requests are append-only.  A semantic correction can leave
    an old request unanswered or its rejected response quarantined even though
    every provider call used by the terminal score has completed.  Requiring
    ``responses == all historical requests`` makes the only apparent escape
    filling obsolete requests with fabricated answers.

    Historical unanswered/quarantined rows are therefore allowed only behind
    an already terminal score/Stage/saturation boundary, with exact accounting
    and a fully valid quarantine audit.  Invalid requests, invalid responses,
    orphan responses, current provider errors, and count drift still fail.
    """

    def count(payload: Mapping[str, Any], field: str) -> int:
        value = payload.get(field, 0)
        if value is None:
            return 0
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"Collaboration provider count is invalid: {field}")
        return value

    provider_name = _normalized_provider_name(provider_audit.get("provider_name"))
    if provider_name != "COLLABORATION_CODEX":
        raise ValueError("Phase106 current canaries require Collaboration Codex")
    logical = count(provider_audit, "logical_call_count")
    successful = count(provider_audit, "successful_call_count")
    top_failure_fields = (
        "provider_error_count",
        "provider_output_rejected_count",
        "prompt_transport_rejected_count",
        "provider_usage_limit_transport_error_count",
        "provider_usage_limit_short_circuit_count",
        "cache_invalid_or_unreadable_count",
        "downstream_semantic_cache_delete_failure_count",
    )
    top_failures = sum(count(provider_audit, field) for field in top_failure_fields)
    journal = _mapping(
        provider_audit.get("collaboration_journal"),
        context="Collaboration provider journal audit",
    )
    journal_integrity_failure_fields = (
        "invalid_request_count",
        "invalid_response_count",
        "orphan_response_count",
        "invalid_quarantined_response_count",
    )
    journal_failures = sum(
        count(journal, field) for field in journal_integrity_failure_fields
    )
    request_count = count(journal, "request_count")
    validated_request_count = count(journal, "validated_request_count")
    response_count = count(journal, "response_file_count")
    validated_response_count = count(journal, "validated_response_count")
    pending_response_count = count(journal, "pending_response_count")
    quarantined_response_count = count(
        journal, "quarantined_response_count"
    )
    validated_quarantined_response_count = count(
        journal, "validated_quarantined_response_count"
    )
    unresolved_pending_response_count = count(
        journal, "unresolved_pending_response_count"
    )
    historical_nonactive_count = (
        unresolved_pending_response_count
        + validated_quarantined_response_count
    )
    if (
        provider_audit.get("status") != "COLLABORATION_PROVIDER_JOURNAL_ACTIVE"
        or journal.get("status") != "COLLABORATION_JOURNAL_ACTIVE"
        or logical <= 0
        or successful != logical
        or top_failures != 0
        or journal_failures != 0
        or request_count <= 0
        or request_count != validated_request_count
        or response_count != validated_response_count
        or pending_response_count != request_count - response_count
        or quarantined_response_count
        != validated_quarantined_response_count
        or historical_nonactive_count != pending_response_count
        or (
            historical_nonactive_count > 0
            and not terminal_output_complete
        )
    ):
        raise ValueError(
            "current Collaboration provider lineage is not clean and complete"
        )
    return {
        "provider_name": provider_name,
        "successful_call_count": successful,
        "provider_error_count": top_failures + journal_failures,
    }


def _provider_audit_with_revalidated_journal(
    provider_audit: Mapping[str, Any],
    *,
    target_root: Path,
) -> Mapping[str, Any]:
    """Upgrade a persisted audit only by rereading its immutable journal.

    Terminal outputs created before quarantine accounting was strengthened do
    not contain the new split counts.  Guessing those counts from
    ``request_count - response_count`` would silently trust a damaged
    quarantine.  When a journal exists, recompute it with the current strict
    validator and require every legacy count to match before adding the new
    fields.  Normal synthetic/legacy fixtures with no pending history need no
    filesystem upgrade.
    """

    saved_journal = _mapping(
        provider_audit.get("collaboration_journal"),
        context="persisted Collaboration provider journal audit",
    )
    journal_root = target_root / "collaboration_codex_subagent_provider"
    has_nonactive_history = (
        int(saved_journal.get("pending_response_count") or 0) > 0
        or int(saved_journal.get("quarantined_response_count") or 0) > 0
    )
    if not journal_root.is_dir():
        if has_nonactive_history:
            raise ValueError(
                "persisted Collaboration history lacks its immutable journal"
            )
        return dict(provider_audit)
    if journal_root.is_symlink() or any(
        path.is_symlink() for path in journal_root.rglob("*")
    ):
        raise ValueError("Collaboration provider journal contains a symlink")
    saved_root = str(saved_journal.get("journal_root") or "")
    if saved_root and Path(saved_root).resolve() != journal_root.resolve():
        raise ValueError("persisted Collaboration journal root has drifted")

    # Assigning the already-existing root keeps this receipt projection
    # read-only; configure_journal_root() is intentionally not called because
    # it is allowed to create missing directories.
    transport = CollaborationCodexSubagentTransport()
    transport.journal_root = journal_root
    current_journal = dict(transport.journal_audit())
    legacy_exact_fields = (
        "status",
        "request_count",
        "validated_request_count",
        "invalid_request_count",
        "response_file_count",
        "validated_response_count",
        "invalid_response_count",
        "orphan_response_count",
        "pending_response_count",
        "quarantined_response_count",
    )
    if any(
        saved_journal.get(field) != current_journal.get(field)
        for field in legacy_exact_fields
    ):
        raise ValueError(
            "persisted Collaboration audit disagrees with its immutable journal"
        )
    upgraded = dict(provider_audit)
    upgraded["collaboration_journal"] = current_journal
    return upgraded


def _fact_extraction_transport_hashes(
    target_root: Path,
) -> Mapping[tuple[str, str], tuple[str, str]]:
    """Bind stable fact compiler IDs to full Collaboration transport hashes.

    Evidence OS intentionally stores compact ``FACTPROMPT``/``FACTRESP``
    identities on accepted claims.  The post-run compact receipt requires the
    full SHA-256 prompt and response-payload hashes instead.  The bridge is the
    validated join: tracked provider-call receipts already prove that each
    stable pair belongs to one exact request/response envelope.
    """

    by_stable_identity: dict[tuple[str, str], tuple[str, str]] = {}
    for call in _provider_call_receipts(target_root):
        if call.get("call_scope") != "FACT_EXTRACTION":
            continue
        request = _decode_journal_envelope(
            call.get("request_envelope_zlib_b64")
        )
        response = _decode_journal_envelope(
            call.get("response_envelope_zlib_b64")
        )
        stable_identity = (
            str(call.get("prompt_hash") or ""),
            str(call.get("response_hash") or ""),
        )
        transport_identity = (
            str(request.get("prompt_hash") or ""),
            str(response.get("payload_hash") or ""),
        )
        if (
            re.fullmatch(r"FACTPROMPT-[0-9a-f]{24}", stable_identity[0])
            is None
            or re.fullmatch(
                r"FACTRESP-[0-9a-f]{24}", stable_identity[1]
            )
            is None
            or _HEX64.fullmatch(transport_identity[0]) is None
            or _HEX64.fullmatch(transport_identity[1]) is None
        ):
            raise ValueError(
                "fact extraction provider receipt lacks exact transport hashes"
            )
        prior = by_stable_identity.setdefault(
            stable_identity,
            transport_identity,
        )
        if prior != transport_identity:
            raise ValueError(
                "fact extraction stable identity maps to multiple transports"
            )
    return by_stable_identity


def _accepted_fact_inventory(
    evidence_rows: Sequence[Mapping[str, Any]],
    counter_rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Mapping[str, Any]]:
    """Merge the full fact ledger and its counter-only materialized view.

    ``evidence_facts.jsonl`` is the canonical all-direction ledger, while
    ``counterfacts.jsonl`` intentionally repeats its COUNTER rows for a
    convenient downstream view.  Identical repetitions are one fact; only a
    same-ID content disagreement is a collision.
    """

    by_id: dict[str, Mapping[str, Any]] = {}
    for row in (*evidence_rows, *counter_rows):
        fact_id = str(row.get("fact_id") or "")
        if not fact_id:
            raise ValueError("current accepted fact lacks an identity")
        prior = by_id.setdefault(fact_id, row)
        if dict(prior) != dict(row):
            raise ValueError(
                "current accepted fact inventory contains a conflicting identity"
            )
    return by_id


def build_selection_bound_canary_artifacts_from_output(
    *,
    repo_root: str | Path,
    target_root: str | Path,
    selection: Mapping[str, Any],
    selection_row: Mapping[str, Any],
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Project the eight compact artifacts from one terminal current output.

    Only production research leaves are read.  The post-run evaluation lane is
    neither an input nor a completion authority for this projection.
    """

    repo = Path(repo_root).resolve()
    target = Path(target_root).absolute()
    selected = _selection_row(
        selection,
        selection_id=str(selection_row.get("selection_id") or ""),
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    if dict(selected) != dict(selection_row):
        raise ValueError("selection row is not the exact row in the sealed manifest")
    target_id = str(selected["target_id"])
    archetype_id = str(selected["archetype_id"])
    as_of_date = str(selected["selection_as_of_date"])
    if target.name != target_id:
        raise ValueError("target output directory is not bound to the selection target")
    if target.is_symlink() or not target.is_dir():
        raise ValueError("target output directory must be a real current directory")
    if any(path.is_symlink() for path in target.rglob("*")):
        raise ValueError("target output tree cannot contain symlinks")

    required_inputs = (
        "target_run_manifest.json",
        "score_vector.json",
        "atomic_stage_decision.json",
        "semantic_saturation_certificate.json",
        "fact_extraction_audit.json",
        "current_structured_materialization.json",
        "business_model_memo.json",
        "red_team_research.json",
        "research_supervisor_review.json",
        "research_provider_response_cache_audit.json",
        "final_component_decisions.jsonl",
        "component_research_memos.jsonl",
        "component_judge_decisions.jsonl",
        "evidence_facts.jsonl",
        "counterfacts.jsonl",
        "material_fact_claims.jsonl",
        "documents.jsonl",
        "query_ledger.jsonl",
        "stagecourt_trace.json",
    )
    for name in required_inputs:
        path = target / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"terminal output is missing required leaf: {name}")

    target_manifest = _read_current_json(target / "target_run_manifest.json")
    score_vector = _read_current_json(target / "score_vector.json")
    atomic_stage = _read_current_json(target / "atomic_stage_decision.json")
    saturation = _read_current_json(target / "semantic_saturation_certificate.json")
    fact_audit = _read_current_json(target / "fact_extraction_audit.json")
    structured = _read_current_json(target / "current_structured_materialization.json")
    business = _read_current_json(target / "business_model_memo.json")
    red_team = _read_current_json(target / "red_team_research.json")
    supervisor = _read_current_json(target / "research_supervisor_review.json")
    provider_audit = _read_current_json(
        target / "research_provider_response_cache_audit.json"
    )
    query_rows = _read_current_jsonl(target / "query_ledger.jsonl")
    all_document_rows = _read_current_jsonl(target / "documents.jsonl")
    raw_evidence_rows = _read_current_jsonl(target / "evidence_facts.jsonl")
    raw_counter_rows = _read_current_jsonl(target / "counterfacts.jsonl")
    material_gap_count = _material_gap_count(
        saturation=saturation,
        supervisor=supervisor,
    )
    terminal_provider_boundary = bool(
        target_manifest.get("status")
        == "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
        and target_manifest.get("production_research_complete") is True
        and score_vector.get("status") == "COMPLETE"
        and score_vector.get("score_valid") is True
        and atomic_stage.get("status") == "FINAL"
        and atomic_stage.get("score_valid") is True
        and saturation.get("status") == "CERTIFIED"
        and saturation.get("semantic_saturation_certified") is True
        and supervisor.get("status")
        == "READY_FOR_INDEPENDENT_SATURATION_REVIEW"
        and material_gap_count == 0
    )
    provider_accounting = _production_provider_accounting(
        _provider_audit_with_revalidated_journal(
            provider_audit,
            target_root=target,
        ),
        terminal_output_complete=terminal_provider_boundary,
    )
    query_ids = tuple(str(row.get("query_id") or "") for row in query_rows)
    document_ids = tuple(
        str(row.get("document_id") or "") for row in all_document_rows
    )
    if (
        not query_rows
        or not all_document_rows
        or not raw_evidence_rows
        or not raw_counter_rows
        or material_gap_count != 0
        or any(not value for value in query_ids)
        or len(set(query_ids)) != len(query_ids)
        or any(not value for value in document_ids)
        or len(set(document_ids)) != len(document_ids)
    ):
        raise ValueError(
            "terminal output lacks a positive unique query/document/fact/counterfact "
            "roster or still has a material gap"
        )
    actual_output_hash = canary_output_tree_hash(
        target, include_post_run_gold=False
    )
    if (
        target_manifest.get("status")
        != "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
        or target_manifest.get("target_id") != target_id
        or target_manifest.get("as_of_date") != as_of_date
        or target_manifest.get("archetype_id") != archetype_id
        or target_manifest.get("production_research_complete") is not True
        or target_manifest.get("gold_visibility") is not False
        or target_manifest.get("gold_comparison_timing") != "POST_RUN_ONLY"
        or target_manifest.get("completion_based_on_fixed_rounds") is not False
        or target_manifest.get("zero_search_result_treated_as_completion") is not False
        or target_manifest.get("transport_budget_treated_as_completion") is not False
        or target_manifest.get("output_tree_hash") != actual_output_hash
        or score_vector.get("target_id") != target_id
        or score_vector.get("as_of_date") != as_of_date
        or score_vector.get("status") != "COMPLETE"
        or score_vector.get("score_valid") is not True
        or atomic_stage.get("target_id") != target_id
        or atomic_stage.get("as_of_date") != as_of_date
        or atomic_stage.get("status") != "FINAL"
        or atomic_stage.get("score_valid") is not True
        or saturation.get("status") != "CERTIFIED"
        or saturation.get("semantic_saturation_certified") is not True
        or fact_audit.get("status") != "FACT_EXTRACTION_AUDIT_PASS"
        or int(fact_audit.get("critical_count_sum") or 0) != 0
        or structured.get("status") != "COMPLETE"
        or structured.get("target_id") != target_id
        or structured.get("as_of_date") != as_of_date
        or business.get("research_complete") is not True
        or business.get("target_id") != target_id
        or business.get("as_of_date") != as_of_date
        or red_team.get("status") != "COMPLETE"
        or supervisor.get("status") != "READY_FOR_INDEPENDENT_SATURATION_REVIEW"
        or supervisor.get("structured_data_complete") is not True
        or provider_accounting["provider_error_count"] != 0
    ):
        raise ValueError("target output is not terminal, current, and provider-clean")

    decision_rows = _decision_rows(target)
    rich_components = _component_receipts(target, decision_rows)
    rich_judges = _judge_receipts(target)
    rich_facts = _fact_receipts(
        target,
        rich_components,
        as_of_date=as_of_date,
        target_id=target_id,
    )
    rich_sources = _source_receipts(rich_facts)
    rich_anchors = _anchor_receipts(
        repo,
        archetype_id=archetype_id,
        components=rich_components,
    )

    judges: list[Mapping[str, Any]] = []
    provider_calls: list[Mapping[str, Any]] = []
    rich_judge_by_component_role = {
        (str(row["component_id"]), str(row["role"])): row for row in rich_judges
    }
    for component_id in CANONICAL_COMPONENT_ORDER:
        for role in _JUDGE_ROLES:
            row = rich_judge_by_component_role.get((component_id, role))
            if row is None:
                raise ValueError("current output lacks the exact twenty-one judge roster")
            judge_provider_name = _normalized_provider_name(row["provider_name"])
            if judge_provider_name != "COLLABORATION_CODEX":
                raise ValueError("Phase106 judge lineage is not Collaboration Codex")
            judge = {
                "schema_version": _SCHEMA_BY_ARTIFACT["judge_decisions.jsonl"],
                "judge_decision_id": row["judge_decision_id"],
                "component_id": component_id,
                "role": role,
                "proposed_points": row["proposed_points"],
                "allowed_range": list(row["allowed_range"]),
                "support_fact_ids": list(row.get("support_fact_ids") or ()),
                "counter_fact_ids": list(row.get("counter_fact_ids") or ()),
                "anchor_ids": list(row.get("anchor_ids") or ()),
                "provider_call_id": row["provider_call_id"],
                "prompt_hash": row["prompt_hash"],
                "response_hash": row["response_hash"],
                "score_or_stage_authority": False,
            }
            judges.append(judge)
            provider_calls.append(
                {
                    "schema_version": _SCHEMA_BY_ARTIFACT["provider_calls.jsonl"],
                    "provider_call_id": row["provider_call_id"],
                    "provider_name": judge_provider_name,
                    "call_scope": "COMPONENT_JUDGE",
                    "status": "COMPLETED",
                    "prompt_hash": row["prompt_hash"],
                    "response_hash": row["response_hash"],
                    "judge_decision_ids": [row["judge_decision_id"]],
                    "fact_ids": [],
                    "score_or_stage_authority": False,
                }
            )

    components = [
        {
            "schema_version": _SCHEMA_BY_ARTIFACT["component_decisions.jsonl"],
            "component_id": row["component_id"],
            "max_points": row["max_points"],
            "support_points": row["support_points"],
            "counter_effect": row["counter_effect"],
            "final_points": row["final_points"],
            "confidence": row["confidence"],
            "proposal_median": row["proposal_median"],
            "consensus_band": list(row["consensus_band"]),
            "judge_proposals": dict(row["judge_proposals"]),
            "aggregation_method": row["aggregation_method"],
            "aggregator_config_hash": row["aggregator_config_hash"],
            "support_fact_ids": list(row.get("support_fact_ids") or ()),
            "counter_fact_ids": list(row.get("counter_fact_ids") or ()),
            "resolution_fact_ids": list(row.get("resolution_fact_ids") or ()),
            "anchor_ids": list(row.get("historical_anchor_ids") or ()),
            "judge_decision_ids": [
                rich_judge_by_component_role[(str(row["component_id"]), role)][
                    "judge_decision_id"
                ]
                for role in _JUDGE_ROLES
            ],
        }
        for row in rich_components
    ]

    facts: list[Mapping[str, Any]] = []
    fact_call_groups: dict[
        tuple[str, str, str], list[str]
    ] = defaultdict(list)
    needs_transport_resolution = any(
        str(row.get("provider_prompt_hash") or "").startswith(
            "FACTPROMPT-"
        )
        or str(row.get("provider_response_hash") or "").startswith(
            "FACTRESP-"
        )
        for row in rich_facts
    )
    fact_transport_hashes = (
        _fact_extraction_transport_hashes(target)
        if needs_transport_resolution
        else {}
    )
    for row in rich_facts:
        extraction_provider_name = _normalized_provider_name(
            row.get("extraction_provider_name")
        )
        if extraction_provider_name != "COLLABORATION_CODEX":
            raise ValueError(
                "Phase106 fact extraction lineage is not Collaboration Codex"
            )
        provider_prompt_identity = str(
            row.get("provider_prompt_hash") or ""
        )
        provider_response_identity = str(
            row.get("provider_response_hash") or ""
        )
        if (
            _HEX64.fullmatch(provider_prompt_identity) is not None
            and _HEX64.fullmatch(provider_response_identity) is not None
        ):
            provider_prompt_hash = provider_prompt_identity
            provider_response_hash = provider_response_identity
        else:
            resolved_transport = fact_transport_hashes.get(
                (
                    provider_prompt_identity,
                    provider_response_identity,
                )
            )
            if resolved_transport is None:
                raise ValueError(
                    "accepted fact lacks exact extraction provider lineage"
                )
            provider_prompt_hash, provider_response_hash = (
                resolved_transport
            )
        if (
            _HEX64.fullmatch(provider_prompt_hash) is None
            or _HEX64.fullmatch(provider_response_hash) is None
        ):
            raise ValueError("accepted fact lacks exact extraction provider hashes")
        fact_call_key = (
            extraction_provider_name,
            provider_prompt_hash,
            provider_response_hash,
        )
        provider_call_id = "FACTCALL-" + stable_hash(fact_call_key)[:24]
        fact = {
            "schema_version": _SCHEMA_BY_ARTIFACT["scoring_facts.jsonl"],
            "fact_id": row["fact_id"],
            "target_id": target_id,
            "as_of_date": as_of_date,
            "component_ids": list(row.get("component_ids") or ()),
            "fact_roles": list(row.get("fact_roles") or ()),
            "subject_id": row.get("subject_id"),
            "business_segment": row.get("business_segment"),
            "product_family": row.get("product_family"),
            "economic_mechanism": row.get("economic_mechanism"),
            "source_document_id": row["source_document_id"],
            "document_content_hash": row["document_content_hash"],
            "exact_quote": row["exact_quote"],
            "exact_quote_hash": row["exact_quote_hash"],
            "published_at": row["published_at"],
            "available_at": row["available_at"],
            "current_score_eligible": row["current_score_eligible"],
            "extraction_provider_name": extraction_provider_name,
            "provider_call_id": provider_call_id,
            "provider_prompt_hash": provider_prompt_hash,
            "provider_response_hash": provider_response_hash,
            "accepted_fact_record_hash": "",
        }
        fact["accepted_fact_record_hash"] = stable_hash(
            _without_hash(fact, "accepted_fact_record_hash")
        )
        facts.append(fact)
        fact_call_groups[fact_call_key].append(str(row["fact_id"]))

    for (provider_name, prompt_hash, response_hash), fact_ids in sorted(
        fact_call_groups.items()
    ):
        provider_calls.append(
            {
                "schema_version": _SCHEMA_BY_ARTIFACT["provider_calls.jsonl"],
                "provider_call_id": "FACTCALL-"
                + stable_hash((provider_name, prompt_hash, response_hash))[:24],
                "provider_name": provider_name,
                "call_scope": "FACT_EXTRACTION",
                "status": "COMPLETED",
                "prompt_hash": prompt_hash,
                "response_hash": response_hash,
                "judge_decision_ids": [],
                "fact_ids": sorted(fact_ids),
                "score_or_stage_authority": False,
            }
        )

    sources: list[Mapping[str, Any]] = []
    for row in rich_sources:
        source = {
            "schema_version": _SCHEMA_BY_ARTIFACT["source_manifest.jsonl"],
            "source_document_id": row["source_document_id"],
            "target_id": target_id,
            "as_of_date": as_of_date,
            "source_url": row["source_url"],
            "source_title": row["source_title"],
            "source_publisher": row["source_publisher"],
            "source_tier": row["source_tier"],
            "source_family": row["source_family"],
            "published_at": row["published_at"],
            "available_at": row["available_at"],
            "document_content_hash": row["document_content_hash"],
            "fact_ids": list(row["fact_document_hashes"]),
            "fact_exact_quote_hashes": dict(row["fact_exact_quote_hashes"]),
            "accepted_source_record_hash": "",
        }
        source["accepted_source_record_hash"] = stable_hash(
            _without_hash(source, "accepted_source_record_hash")
        )
        sources.append(source)

    anchors = [
        {
            "schema_version": _SCHEMA_BY_ARTIFACT["anchor_manifest.jsonl"],
            "anchor_id": row["anchor_id"],
            "component_id": row["component_id"],
            "archetype_id": row["archetype_id"],
            "max_points": row["normalized_anchor_payload"]["max_points"],
            "normalized_anchor_payload": row["normalized_anchor_payload"],
            "anchor_payload_hash": row["anchor_payload_hash"],
        }
        for row in rich_anchors
    ]

    vector = {
        component_id: float(score_vector["component_score_vector"][component_id])
        for component_id in CANONICAL_COMPONENT_ORDER
    }
    maxima = {
        str(row["component_id"]): float(row["max_points"]) for row in components
    }
    total = round(sum(vector.values()), 6)
    raw_fact_by_id = _accepted_fact_inventory(
        raw_evidence_rows,
        raw_counter_rows,
    )
    raw_claim_by_id = {
        str(row["claim_id"]): row
        for row in _read_current_jsonl(target / "material_fact_claims.jsonl")
        if str(row.get("claim_id") or "")
    }
    raw_document_by_id = {
        str(row["document_id"]): row
        for row in all_document_rows
        if str(row.get("document_id") or "")
    }
    compact_fact_by_id = {str(row["fact_id"]): row for row in facts}
    counter_ids = {str(row["fact_id"]) for row in raw_counter_rows}
    blind_review_inventory: list[Mapping[str, Any]] = []
    for fact_id in sorted(raw_fact_by_id):
        raw_fact = raw_fact_by_id[fact_id]
        claim = next(
            (
                raw_claim_by_id[str(claim_id)]
                for claim_id in raw_fact.get("claim_ids") or ()
                if str(claim_id) in raw_claim_by_id
            ),
            None,
        )
        if claim is None:
            raise ValueError(f"accepted fact lacks a material claim: {fact_id}")
        document_id = str(claim.get("document_id") or "")
        document = raw_document_by_id.get(document_id)
        exact_quote = str(claim.get("exact_quote") or "")
        if document is None or not exact_quote:
            raise ValueError(f"accepted fact lacks source inventory: {fact_id}")
        selected_fact = compact_fact_by_id.get(fact_id)
        blind_review_inventory.append(
            {
                "fact_id": fact_id,
                "target_id": target_id,
                "as_of_date": as_of_date,
                "subject_id": (
                    selected_fact.get("subject_id")
                    if selected_fact is not None
                    else claim.get("subject_id") or raw_fact.get("subject")
                ),
                "business_segment": (
                    selected_fact.get("business_segment")
                    if selected_fact is not None
                    else raw_fact.get("business_segment") or claim.get("business_segment") or ""
                ),
                "product_family": (
                    selected_fact.get("product_family")
                    if selected_fact is not None
                    else raw_fact.get("product_family") or claim.get("product_family") or ""
                ),
                "economic_mechanism": (
                    selected_fact.get("economic_mechanism")
                    if selected_fact is not None
                    else raw_fact.get("economic_mechanism") or claim.get("economic_mechanism") or ""
                ),
                "fact_roles": (
                    list(selected_fact["fact_roles"])
                    if selected_fact is not None
                    else ["COUNTER_CONTEXT" if fact_id in counter_ids else "MATERIAL_CONTEXT"]
                ),
                "source_document_id": document_id,
                "source_family": claim.get("source_family") or document.get("source_family") or "",
                "source_tier": claim.get("source_tier") or document.get("source_family") or "",
                "published_at": claim.get("published_at") or document.get("published_at"),
                "available_at": claim.get("available_at") or document.get("available_at"),
                "exact_quote_hash": hashlib.sha256(exact_quote.encode("utf-8")).hexdigest(),
                "current_score_eligible": selected_fact is not None,
            }
        )
    provider_name = str(provider_accounting["provider_name"])
    result_body = {
        "schema_version": CANARY_RESULT_SCHEMA,
        "status": CANARY_RESULT_PASS,
        "run_id": "RESEARCHRUN-"
        + stable_hash(
            {
                "selection_id": selected["selection_id"],
                "output_tree_hash": actual_output_hash,
            }
        )[:24],
        "selection_id": selected["selection_id"],
        "selection_roster_hash": selection["selection_roster_hash"],
        "archetype_id": archetype_id,
        "target_id": target_id,
        "as_of_date": as_of_date,
        "production_research_status": "COMPLETE",
        "fact_extraction_status": "COMPLETE",
        "structured_materialization_status": "COMPLETE",
        "business_model_status": "COMPLETE",
        "component_research_status": "COMPLETE",
        "judge_status": "COMPLETE",
        "red_team_status": "COMPLETE",
        "synthesis_status": "COMPLETE",
        "supervisor_status": "COMPLETE",
        "semantic_saturation_status": "COMPLETE",
        "score_status": "COMPLETE",
        "stagecourt_status": "FINAL",
        "full_researcher_mode_complete": True,
        "component_score_vector": vector,
        "total_score": total,
        "canonical_stage": atomic_stage["canonical_stage"],
        "score_valid": True,
        "stage_final": True,
        "component_count": len(components),
        "judge_decision_count": len(judges),
        "query_count": len(query_rows),
        "document_count": len(all_document_rows),
        "fact_count": len(raw_fact_by_id),
        "counterfact_count": len(raw_counter_rows),
        "material_gap_count": material_gap_count,
        "source_count": len(all_document_rows),
        "output_tree_hash": actual_output_hash,
        "provider_call_counts": {
            provider_name: int(provider_accounting["successful_call_count"])
        },
        "provider_error_count": int(provider_accounting["provider_error_count"]),
        "unauthorized_provider_call_count": 0,
        "local_provider_call_count": 0,
        "score_or_stage_authority": False,
        "production_readiness_authority": False,
    }
    canary_result = {
        **result_body,
        "result_id": "CANARYRUN-" + stable_hash(result_body)[:24],
    }
    production_receipt = build_full_researcher_mode_canary_receipt(
        canary_result,
        selection=selection,
        selection_row=selected,
    )
    score = {
        "schema_version": _SCHEMA_BY_ARTIFACT["score_receipt.json"],
        "target_id": target_id,
        "as_of_date": as_of_date,
        "selection_id": selected["selection_id"],
        "selection_roster_hash": selection["selection_roster_hash"],
        "score_valid": True,
        "research_complete": True,
        "component_score_vector": vector,
        "component_max_vector": maxima,
        "total_score": total,
        "canonical_stage": atomic_stage["canonical_stage"],
        "canary_result": canary_result,
        "production_receipt": production_receipt,
        "blind_review_inventory": blind_review_inventory,
        "score_or_stage_authority": False,
    }
    rich_stage = _stage_receipt(repo, target, score, receipt_id="COMPACT-PROJECTION")
    stage = {
        "schema_version": _SCHEMA_BY_ARTIFACT["stagecourt_receipt.json"],
        "target_id": target_id,
        "as_of_date": as_of_date,
        "score_receipt_hash": stable_hash(score),
        "component_score_vector_hash": stable_hash(vector),
        "total_score": total,
        "canonical_stage": atomic_stage["canonical_stage"],
        "decision_status": "FINAL",
        "score_valid": True,
        "stage_final": True,
        "classification_input": rich_stage["classification_input"],
        "decision_trace_hash": "",
        "score_or_stage_authority": False,
    }
    stage["decision_trace_hash"] = stable_hash(
        {
            "score_receipt_hash": stage["score_receipt_hash"],
            "component_score_vector_hash": stage["component_score_vector_hash"],
            "total_score": stage["total_score"],
            "classification_input": stage["classification_input"],
            "canonical_stage": stage["canonical_stage"],
        }
    )
    artifacts = {
        "score_receipt.json": score,
        "component_decisions.jsonl": components,
        "scoring_facts.jsonl": facts,
        "judge_decisions.jsonl": judges,
        "source_manifest.jsonl": sources,
        "anchor_manifest.jsonl": anchors,
        "provider_calls.jsonl": provider_calls,
        "stagecourt_receipt.json": stage,
    }
    validate_selection_bound_canary_artifacts(
        selection=selection,
        selection_id=str(selected["selection_id"]),
        artifacts=artifacts,
        repo_root=repo,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    return artifacts


def _validate_manifest(
    manifest: Mapping[str, Any],
    *,
    expected: Mapping[str, Any],
) -> None:
    if set(manifest) != _MANIFEST_KEYS or dict(manifest) != dict(expected):
        raise ValueError("compact receipt manifest does not recompute exactly")


def _validate_reviews(
    reviews: Sequence[Mapping[str, Any]],
    *,
    manifest: Mapping[str, Any],
    verified: Mapping[str, Any],
) -> None:
    if len(reviews) != 2:
        raise ValueError("exactly two independent reviews are required")
    portable_reviewer_ids = {
        "CODEX_POST_RUN_REVIEWER_A",
        "CODEX_POST_RUN_REVIEWER_B",
    }
    reviewer_ids: set[str] = set()
    provider_call_ids: set[str] = set()
    prompt_hashes: set[str] = set()
    response_hashes: set[str] = set()
    for review in reviews:
        if set(review) != _REVIEW_KEYS or review.get("schema_version") != COMPACT_REVIEW_SCHEMA:
            raise ValueError("independent review schema is not exact")
        reviewer_id = str(review.get("reviewer_id") or "")
        call_id = str(review.get("provider_call_id") or "")
        prompt_hash = str(review.get("prompt_hash") or "")
        response_hash = str(review.get("response_hash") or "")
        if (
            reviewer_id not in portable_reviewer_ids
            or not call_id
            or _HEX64.fullmatch(prompt_hash) is None
            or _HEX64.fullmatch(response_hash) is None
            or reviewer_id in reviewer_ids
            or call_id in provider_call_ids
            or prompt_hash in prompt_hashes
            or response_hash in response_hashes
        ):
            raise ValueError("the two reviews are not independent")
        reviewer_ids.add(reviewer_id)
        provider_call_ids.add(call_id)
        prompt_hashes.add(prompt_hash)
        response_hashes.add(response_hash)
        identity = {
            "reviewer_id": reviewer_id,
            "provider_call_id": call_id,
            "prompt_hash": prompt_hash,
            "response_hash": response_hash,
            "receipt_payload_hash": manifest["receipt_payload_hash"],
        }
        if (
            review.get("review_id") != "CANREVIEW-" + stable_hash(identity)[:24]
            or review.get("status") != COMPACT_REVIEW_PASS
            or review.get("provider_name") not in _AUTHORIZED_PROVIDERS
            or review.get("selection_id") != manifest["selection_id"]
            or review.get("selection_roster_hash") != manifest["selection_roster_hash"]
            or review.get("receipt_id") != manifest["receipt_id"]
            or review.get("receipt_payload_hash") != manifest["receipt_payload_hash"]
            or review.get("target_id") != manifest["target_id"]
            or review.get("archetype_id") != manifest["archetype_id"]
            or review.get("as_of_date") != manifest["as_of_date"]
            or stable_hash(review.get("recomputed_component_score_vector"))
            != stable_hash(verified["component_score_vector"])
            or not _finite(review.get("recomputed_total_score"))
            or abs(float(review["recomputed_total_score"]) - float(verified["total_score"])) > 1e-9
            or review.get("recomputed_canonical_stage") != verified["canonical_stage"]
            or review.get("all_eight_artifacts_verified") is not True
            or review.get("full_score_lineage_verified") is not True
            or review.get("independent_review") is not True
            or review.get("review_complete") is not True
            or review.get("critical_findings") != []
            or any(
                isinstance(review.get(field), bool)
                or not isinstance(review.get(field), int)
                or review.get(field) != 0
                for field in (
                    "material_fact_omission_count",
                    "counterfact_omission_count",
                    "subject_or_segment_mismatch_count",
                    "currentness_failure_count",
                    "source_quality_failure_count",
                    "component_calibration_failure_count",
                    "historical_anchor_analogy_failure_count",
                )
            )
            or isinstance(review.get("critical_count_sum"), bool)
            or not isinstance(review.get("critical_count_sum"), int)
            or review.get("critical_count_sum") != 0
            or review.get("score_or_stage_authority") is not False
        ):
            raise ValueError("independent review did not reproduce the full compact receipt")
    if reviewer_ids != portable_reviewer_ids:
        raise ValueError("portable reviewer role roster is incomplete")


def validate_selection_bound_canary_bundle(
    *,
    selection: Mapping[str, Any],
    manifest: Mapping[str, Any],
    artifacts: Mapping[str, Any],
    reviews: Sequence[Mapping[str, Any]],
    repo_root: str | Path,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Validate one manifest, its exact eight artifacts, and two reviews."""

    verified = validate_selection_bound_canary_artifacts(
        selection=selection,
        selection_id=str(manifest.get("selection_id") or ""),
        artifacts=artifacts,
        repo_root=repo_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    expected = build_selection_bound_canary_manifest(
        selection=selection,
        selection_id=str(manifest.get("selection_id") or ""),
        artifacts=artifacts,
        repo_root=repo_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    _validate_manifest(manifest, expected=expected)
    _validate_reviews(tuple(reviews), manifest=manifest, verified=verified)
    return verified


def _encode_artifact(name: str, payload: Any) -> bytes:
    if name.endswith(".jsonl"):
        rows = _rows(payload, context=name)
        return b"".join(
            (json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")
            for row in rows
        )
    return (json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")


def _write_private(parent_fd: int, name: str, payload: bytes) -> None:
    descriptor = os.open(
        name,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
        0o600,
        dir_fd=parent_fd,
    )
    try:
        view = memoryview(payload)
        while view:
            written = os.write(descriptor, view)
            view = view[written:]
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def export_selection_bound_canary_bundle(
    *,
    output_directory: str | Path,
    selection: Mapping[str, Any],
    manifest: Mapping[str, Any],
    artifacts: Mapping[str, Any],
    reviews: Sequence[Mapping[str, Any]],
    repo_root: str | Path,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> Path:
    """Atomically publish a fully validated compact canary receipt directory."""

    validate_selection_bound_canary_bundle(
        selection=selection,
        manifest=manifest,
        artifacts=artifacts,
        reviews=reviews,
        repo_root=repo_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    destination = Path(output_directory).absolute()
    parent_fd = _open_or_create_directory_no_symlinks(destination.parent)
    temporary_name = f".{destination.name}.{secrets.token_hex(16)}.tmp"
    temporary_fd = -1
    try:
        try:
            os.stat(destination.name, dir_fd=parent_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise ValueError("compact receipt destination already exists")
        os.mkdir(temporary_name, mode=0o700, dir_fd=parent_fd)
        temporary_fd = os.open(
            temporary_name,
            os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0),
            dir_fd=parent_fd,
        )
        _write_private(temporary_fd, RECEIPT_MANIFEST_NAME, _encode_artifact(RECEIPT_MANIFEST_NAME, manifest))
        for name in REQUIRED_ARTIFACT_NAMES:
            _write_private(temporary_fd, name, _encode_artifact(name, artifacts[name]))
        os.mkdir(REVIEW_DIRECTORY_NAME, mode=0o700, dir_fd=temporary_fd)
        review_fd = os.open(
            REVIEW_DIRECTORY_NAME,
            os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0),
            dir_fd=temporary_fd,
        )
        try:
            for name, review in zip(REVIEW_NAMES, reviews):
                _write_private(review_fd, name, _encode_artifact(name, review))
            os.fsync(review_fd)
        finally:
            os.close(review_fd)
        os.fsync(temporary_fd)
        os.rename(temporary_name, destination.name, src_dir_fd=parent_fd, dst_dir_fd=parent_fd)
        os.fsync(parent_fd)
    finally:
        if temporary_fd >= 0:
            os.close(temporary_fd)
        os.close(parent_fd)
    return destination


def _decode_json(encoded: bytes, *, context: str) -> Mapping[str, Any]:
    try:
        return _mapping(json.loads(encoded.decode("utf-8")), context=context)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{context} is not valid JSON") from exc


def _decode_jsonl(encoded: bytes, *, context: str) -> tuple[Mapping[str, Any], ...]:
    try:
        lines = encoded.decode("utf-8").splitlines()
        return tuple(_mapping(json.loads(line), context=context) for line in lines if line.strip())
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{context} is not valid JSONL") from exc


def load_selection_bound_canary_directory(
    *,
    receipt_directory: str | Path,
    selection: Mapping[str, Any],
    repo_root: str | Path,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Load and offline-verify an exact compact receipt tree."""

    root_fd = _open_existing_directory_no_symlinks(Path(receipt_directory))
    try:
        names = set(os.listdir(root_fd))
        expected = {RECEIPT_MANIFEST_NAME, REVIEW_DIRECTORY_NAME, *REQUIRED_ARTIFACT_NAMES}
        if names != expected:
            raise ValueError("compact receipt directory has an unexpected or missing entry")
        manifest = _decode_json(
            _read_regular_from_directory(root_fd, RECEIPT_MANIFEST_NAME)[0],
            context="compact receipt manifest",
        )
        artifacts: dict[str, Any] = {}
        for name in REQUIRED_ARTIFACT_NAMES:
            encoded, _ = _read_regular_from_directory(root_fd, name)
            artifacts[name] = _decode_jsonl(encoded, context=name) if name.endswith(".jsonl") else _decode_json(encoded, context=name)
        review_fd = os.open(
            REVIEW_DIRECTORY_NAME,
            os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0),
            dir_fd=root_fd,
        )
        try:
            if set(os.listdir(review_fd)) != set(REVIEW_NAMES):
                raise ValueError("compact receipt must contain exactly two review files")
            reviews = tuple(
                _decode_json(_read_regular_from_directory(review_fd, name)[0], context=name)
                for name in REVIEW_NAMES
            )
        finally:
            os.close(review_fd)
    finally:
        os.close(root_fd)
    verified = validate_selection_bound_canary_bundle(
        selection=selection,
        manifest=manifest,
        artifacts=artifacts,
        reviews=reviews,
        repo_root=repo_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    return {
        "manifest": dict(manifest),
        "artifacts": dict(artifacts),
        "reviews": tuple(dict(row) for row in reviews),
        "verified": dict(verified),
    }


def verify_selection_bound_canary_directory(
    *,
    receipt_directory: str | Path,
    selection: Mapping[str, Any],
    repo_root: str | Path,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Offline-verify an exact compact receipt tree without production output."""

    loaded = load_selection_bound_canary_directory(
        receipt_directory=receipt_directory,
        selection=selection,
        repo_root=repo_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    return _mapping(loaded["verified"], context="verified compact receipt")


__all__ = [
    "COMPACT_RECEIPT_PASS",
    "COMPACT_RECEIPT_SCHEMA",
    "COMPACT_REVIEW_PASS",
    "COMPACT_REVIEW_SCHEMA",
    "REQUIRED_ARTIFACT_NAMES",
    "build_selection_bound_canary_artifacts_from_output",
    "build_selection_bound_canary_manifest",
    "export_selection_bound_canary_bundle",
    "load_selection_bound_canary_directory",
    "validate_selection_bound_canary_artifacts",
    "validate_selection_bound_canary_bundle",
    "verify_selection_bound_canary_directory",
]

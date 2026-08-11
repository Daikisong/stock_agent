"""Fail-closed Phase-106 compilation for five full Researcher Mode canaries.

Phase 105 chooses five targets without seeing a score or Stage.  This module
consumes that sealed selection only after every target has a complete
Researcher Mode result, one result receipt, and two independent Codex
Collaboration review receipts.  It never reads a Gold artifact and it never
computes or mutates a score or Stage.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from datetime import date
import hashlib
import json
import math
import os
from pathlib import Path
import re
import secrets
import stat
from typing import Any

from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_selection import (
    REQUIRED_ARCHETYPES,
    _open_existing_directory_no_symlinks,
    _open_or_create_directory_no_symlinks,
    _read_regular_from_directory,
    validate_cross_archetype_canary_selection_manifest,
)
from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER


CANARY_RESULT_SCHEMA = "e2r_v6_full_researcher_mode_canary_result_v1"
CANARY_RESULT_PASS = "E2R_V6_FULL_RESEARCHER_MODE_CANARY_PASS"
CANARY_RECEIPT_SCHEMA = "e2r_v6_full_researcher_mode_canary_receipt_v1"
CANARY_REVIEW_SCHEMA = "e2r_v6_cross_archetype_canary_review_v1"
CANARY_REVIEW_PASS = "E2R_V6_CROSS_ARCHETYPE_CANARY_REVIEW_PASS"
CANARY_SUMMARY_SCHEMA = "e2r_v6_cross_archetype_canary_summary_v1"
CANARY_SUMMARY_PASS = "E2R_V6_CROSS_ARCHETYPE_CANARY_SUMMARY_PASS"
CANARY_COMPILATION_SCHEMA = "e2r_v6_cross_archetype_canary_compilation_v1"
CANARY_COMPILATION_PASS = "E2R_V6_CROSS_ARCHETYPE_CANARY_COMPILATION_PASS"
CANARY_COMPILATION_PENDING = "E2R_V6_CROSS_ARCHETYPE_CANARY_COMPILATION_PENDING"
CANARY_COMPILATION_FAIL = "E2R_V6_CROSS_ARCHETYPE_CANARY_COMPILATION_FAIL"

CANARY_RESULT_NAME = "researcher_mode_result.json"
CANARY_RECEIPT_NAME = "production_receipt.json"
CANARY_REVIEWS_DIRECTORY = "independent_reviews"
CANARY_REVIEW_NAMES = ("review_a.json", "review_b.json")

_HEX64 = re.compile(r"[0-9a-f]{64}\Z")
_TARGET = re.compile(r"[0-9A-Z]{6}\Z")
_RUN_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.:-]{7,127}\Z")
_REVIEWER_ID = re.compile(r"[A-Za-z0-9/_.:-]{3,128}\Z")
_CANONICAL_STAGES = frozenset(
    {"0", "1", "2", "3-Green", "3-Yellow", "3-Red", "4A", "4B", "4C", "5"}
)
_AUTHORIZED_PROVIDER_NAMES = frozenset({"CODEX", "COLLABORATION_CODEX"})
_FORBIDDEN_TEXT_MARKERS = (
    "gold",
    "localhost",
    "127.0.0.1",
    "::1",
)
_SAFE_ZERO_AUDIT_KEYS = frozenset(
    {
        "local_provider_call_count",
    }
)

_RESULT_KEYS = frozenset(
    {
        "schema_version",
        "result_id",
        "status",
        "run_id",
        "selection_id",
        "selection_roster_hash",
        "archetype_id",
        "target_id",
        "as_of_date",
        "production_research_status",
        "fact_extraction_status",
        "structured_materialization_status",
        "business_model_status",
        "component_research_status",
        "judge_status",
        "red_team_status",
        "synthesis_status",
        "supervisor_status",
        "semantic_saturation_status",
        "score_status",
        "stagecourt_status",
        "full_researcher_mode_complete",
        "component_score_vector",
        "total_score",
        "canonical_stage",
        "score_valid",
        "stage_final",
        "component_count",
        "judge_decision_count",
        "query_count",
        "document_count",
        "fact_count",
        "counterfact_count",
        "material_gap_count",
        "source_count",
        "output_tree_hash",
        "provider_call_counts",
        "provider_error_count",
        "unauthorized_provider_call_count",
        "local_provider_call_count",
        "score_or_stage_authority",
        "production_readiness_authority",
    }
)
_RECEIPT_KEYS = frozenset(
    {
        "schema_version",
        "receipt_id",
        "result_id",
        "result_payload_hash",
        "run_id",
        "selection_id",
        "selection_roster_hash",
        "archetype_id",
        "target_id",
        "as_of_date",
        "output_tree_hash",
        "component_score_vector_hash",
        "total_score",
        "canonical_stage",
        "score_valid",
        "stage_final",
        "component_count",
        "query_count",
        "document_count",
        "fact_count",
        "counterfact_count",
        "material_gap_count",
        "source_count",
        "judge_decision_count",
        "provider_call_counts",
        "provider_error_count",
        "unauthorized_provider_call_count",
        "local_provider_call_count",
        "full_researcher_mode_complete",
        "receipt_complete",
        "score_or_stage_authority",
        "production_readiness_authority",
    }
)
_REVIEW_KEYS = frozenset(
    {
        "schema_version",
        "review_id",
        "status",
        "reviewer_id",
        "provider_name",
        "provider_call_id",
        "prompt_hash",
        "response_hash",
        "selection_id",
        "selection_roster_hash",
        "archetype_id",
        "target_id",
        "as_of_date",
        "result_id",
        "result_payload_hash",
        "production_receipt_id",
        "production_receipt_hash",
        "recomputed_component_score_vector",
        "recomputed_total_score",
        "recomputed_canonical_stage",
        "production_research_complete",
        "score_reproduction_matches",
        "stage_reproduction_matches",
        "evidence_lineage_complete",
        "independent_review",
        "review_complete",
        "verdict",
        "critical_findings",
        "critical_count_sum",
        "score_or_stage_authority",
        "production_readiness_authority",
    }
)
_SUMMARY_KEYS = frozenset(
    {
        "schema_version",
        "summary_id",
        "status",
        "as_of_date",
        "selection_roster_hash",
        "required_archetypes",
        "canary_count",
        "independent_review_count",
        "canaries",
        "critical_count_sum",
        "score_or_stage_authority",
        "production_readiness_authority",
    }
)
_SUMMARY_ROW_KEYS = frozenset(
    {
        "archetype_id",
        "target_id",
        "selection_id",
        "result_id",
        "result_payload_hash",
        "production_receipt_id",
        "production_receipt_hash",
        "reviewer_ids",
        "review_ids",
        "review_receipt_hashes",
        "component_score_vector",
        "total_score",
        "canonical_stage",
        "score_valid",
        "stage_final",
    }
)


def _mapping(value: object, *, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{context} must be an object")
    return value


def _false_authority(payload: Mapping[str, Any]) -> bool:
    return (
        payload.get("score_or_stage_authority") is False
        and payload.get("production_readiness_authority") is False
    )


def _is_count(value: object, *, positive: bool = False) -> bool:
    return bool(
        isinstance(value, int)
        and not isinstance(value, bool)
        and value >= (1 if positive else 0)
    )


def _is_score(value: object) -> bool:
    return bool(
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
        and 0.0 <= float(value) <= 100.0
    )


def _is_iso_date(value: object) -> bool:
    try:
        parsed = date.fromisoformat(str(value))
    except (TypeError, ValueError):
        return False
    return parsed.isoformat() == value


def _contains_forbidden_text(value: object) -> bool:
    def visit(item: object) -> bool:
        if isinstance(item, Mapping):
            return any(
                (
                    False
                    if str(key).casefold() in _SAFE_ZERO_AUDIT_KEYS and child == 0
                    else visit(str(key))
                )
                or visit(child)
                for key, child in item.items()
            )
        if isinstance(item, Sequence) and not isinstance(
            item, (str, bytes, bytearray)
        ):
            return any(visit(child) for child in item)
        if isinstance(item, str):
            lowered = item.casefold()
            return any(marker in lowered for marker in _FORBIDDEN_TEXT_MARKERS)
        return False

    return visit(value)


def _vector(value: object) -> Mapping[str, float]:
    vector = _mapping(value, context="component score vector")
    if set(vector) != set(CANONICAL_COMPONENT_ORDER):
        raise ValueError("component score vector must contain the exact seven components")
    normalized: dict[str, float] = {}
    for component_id in CANONICAL_COMPONENT_ORDER:
        points = vector.get(component_id)
        if not _is_score(points):
            raise ValueError("component score vector contains an invalid value")
        normalized[component_id] = float(points)
    return normalized


def _selection_rows(
    selection: Mapping[str, Any],
    *,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Mapping[str, Any]]:
    validate_cross_archetype_canary_selection_manifest(
        selection,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    rows = tuple(selection.get("selections") or ())
    return {
        str(row.get("archetype_id") or ""): _mapping(row, context="selection row")
        for row in rows
    }


def _identity_matches_selection(
    payload: Mapping[str, Any],
    *,
    selection: Mapping[str, Any],
    row: Mapping[str, Any],
) -> bool:
    return bool(
        payload.get("selection_id") == row.get("selection_id")
        and payload.get("selection_roster_hash") == selection.get("selection_roster_hash")
        and payload.get("archetype_id") == row.get("archetype_id")
        and payload.get("target_id") == row.get("target_id")
        and payload.get("as_of_date") == selection.get("selection_as_of_date")
    )


def validate_full_researcher_mode_canary_result(
    payload: Mapping[str, Any],
    *,
    selection: Mapping[str, Any],
    selection_row: Mapping[str, Any],
) -> None:
    """Validate one full result projection without trusting its score authority."""

    vector = _vector(payload.get("component_score_vector"))
    provider_counts = payload.get("provider_call_counts")
    result_without_id = {key: value for key, value in payload.items() if key != "result_id"}
    terminal_complete_fields = (
        "production_research_status",
        "fact_extraction_status",
        "structured_materialization_status",
        "business_model_status",
        "component_research_status",
        "judge_status",
        "red_team_status",
        "synthesis_status",
        "supervisor_status",
        "semantic_saturation_status",
        "score_status",
    )
    if (
        set(payload) != _RESULT_KEYS
        or payload.get("schema_version") != CANARY_RESULT_SCHEMA
        or payload.get("status") != CANARY_RESULT_PASS
        or not _identity_matches_selection(payload, selection=selection, row=selection_row)
        or not _is_iso_date(payload.get("as_of_date"))
        or _RUN_ID.fullmatch(str(payload.get("run_id") or "")) is None
        or payload.get("result_id")
        != "CANARYRUN-" + stable_hash(result_without_id)[:24]
        or any(payload.get(field) != "COMPLETE" for field in terminal_complete_fields)
        or payload.get("stagecourt_status") != "FINAL"
        or payload.get("full_researcher_mode_complete") is not True
        or payload.get("score_valid") is not True
        or payload.get("stage_final") is not True
        or not _is_score(payload.get("total_score"))
        or not math.isclose(
            sum(vector.values()),
            float(payload.get("total_score")),
            rel_tol=0.0,
            abs_tol=1e-9,
        )
        or payload.get("canonical_stage") not in _CANONICAL_STAGES
        or payload.get("component_count") != len(CANONICAL_COMPONENT_ORDER)
        or payload.get("judge_decision_count") != 3 * len(CANONICAL_COMPONENT_ORDER)
        or not _is_count(payload.get("query_count"), positive=True)
        or not _is_count(payload.get("document_count"), positive=True)
        or not _is_count(payload.get("fact_count"), positive=True)
        or not _is_count(payload.get("counterfact_count"), positive=True)
        or int(payload.get("counterfact_count") or 0)
        > int(payload.get("fact_count") or 0)
        or not _is_count(payload.get("material_gap_count"))
        or payload.get("material_gap_count") != 0
        or not _is_count(payload.get("source_count"), positive=True)
        or _HEX64.fullmatch(str(payload.get("output_tree_hash") or "")) is None
        or not isinstance(provider_counts, Mapping)
        or not provider_counts
        or set(provider_counts) - _AUTHORIZED_PROVIDER_NAMES
        or any(not _is_count(value) for value in provider_counts.values())
        or sum(int(value) for value in provider_counts.values()) <= 0
        or any(
            not _is_count(payload.get(field)) or payload.get(field) != 0
            for field in (
                "provider_error_count",
                "unauthorized_provider_call_count",
                "local_provider_call_count",
            )
        )
        or not _false_authority(payload)
        or _contains_forbidden_text(payload)
    ):
        raise ValueError("full Researcher Mode canary result contract is invalid")


def build_full_researcher_mode_canary_receipt(
    result: Mapping[str, Any],
    *,
    selection: Mapping[str, Any],
    selection_row: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Build the deterministic receipt projection for one validated result."""

    validate_full_researcher_mode_canary_result(
        result, selection=selection, selection_row=selection_row
    )
    body = {
        "schema_version": CANARY_RECEIPT_SCHEMA,
        "result_id": result["result_id"],
        "result_payload_hash": stable_hash(result),
        "run_id": result["run_id"],
        "selection_id": result["selection_id"],
        "selection_roster_hash": result["selection_roster_hash"],
        "archetype_id": result["archetype_id"],
        "target_id": result["target_id"],
        "as_of_date": result["as_of_date"],
        "output_tree_hash": result["output_tree_hash"],
        "component_score_vector_hash": stable_hash(result["component_score_vector"]),
        "total_score": result["total_score"],
        "canonical_stage": result["canonical_stage"],
        "score_valid": True,
        "stage_final": True,
        "component_count": result["component_count"],
        "query_count": result["query_count"],
        "document_count": result["document_count"],
        "fact_count": result["fact_count"],
        "counterfact_count": result["counterfact_count"],
        "material_gap_count": result["material_gap_count"],
        "source_count": result["source_count"],
        "judge_decision_count": result["judge_decision_count"],
        "provider_call_counts": dict(result["provider_call_counts"]),
        "provider_error_count": result["provider_error_count"],
        "unauthorized_provider_call_count": result[
            "unauthorized_provider_call_count"
        ],
        "local_provider_call_count": result["local_provider_call_count"],
        "full_researcher_mode_complete": True,
        "receipt_complete": True,
        "score_or_stage_authority": False,
        "production_readiness_authority": False,
    }
    return {**body, "receipt_id": "CANARYREC-" + stable_hash(body)[:24]}


def validate_full_researcher_mode_canary_receipt(
    payload: Mapping[str, Any],
    *,
    result: Mapping[str, Any],
    selection: Mapping[str, Any],
    selection_row: Mapping[str, Any],
) -> None:
    expected = build_full_researcher_mode_canary_receipt(
        result, selection=selection, selection_row=selection_row
    )
    if (
        set(payload) != _RECEIPT_KEYS
        or dict(payload) != dict(expected)
        or _contains_forbidden_text(payload)
    ):
        raise ValueError("full Researcher Mode production receipt is invalid")


def build_independent_canary_review(
    *,
    reviewer_id: str,
    provider_call_id: str,
    prompt_hash: str,
    response_hash: str,
    result: Mapping[str, Any],
    receipt: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Build one affirmative independent review receipt for validated tests/fixtures."""

    body = {
        "schema_version": CANARY_REVIEW_SCHEMA,
        "status": CANARY_REVIEW_PASS,
        "reviewer_id": reviewer_id,
        "provider_name": "COLLABORATION_CODEX",
        "provider_call_id": provider_call_id,
        "prompt_hash": prompt_hash,
        "response_hash": response_hash,
        "selection_id": result["selection_id"],
        "selection_roster_hash": result["selection_roster_hash"],
        "archetype_id": result["archetype_id"],
        "target_id": result["target_id"],
        "as_of_date": result["as_of_date"],
        "result_id": result["result_id"],
        "result_payload_hash": stable_hash(result),
        "production_receipt_id": receipt["receipt_id"],
        "production_receipt_hash": stable_hash(receipt),
        "recomputed_component_score_vector": dict(result["component_score_vector"]),
        "recomputed_total_score": result["total_score"],
        "recomputed_canonical_stage": result["canonical_stage"],
        "production_research_complete": True,
        "score_reproduction_matches": True,
        "stage_reproduction_matches": True,
        "evidence_lineage_complete": True,
        "independent_review": True,
        "review_complete": True,
        "verdict": "APPROVE",
        "critical_findings": [],
        "critical_count_sum": 0,
        "score_or_stage_authority": False,
        "production_readiness_authority": False,
    }
    return {**body, "review_id": "CANARYREV-" + stable_hash(body)[:24]}


def validate_independent_canary_review(
    payload: Mapping[str, Any],
    *,
    result: Mapping[str, Any],
    receipt: Mapping[str, Any],
    selection: Mapping[str, Any],
    selection_row: Mapping[str, Any],
) -> None:
    vector = _vector(payload.get("recomputed_component_score_vector"))
    body = {key: value for key, value in payload.items() if key != "review_id"}
    if (
        set(payload) != _REVIEW_KEYS
        or payload.get("schema_version") != CANARY_REVIEW_SCHEMA
        or payload.get("status") != CANARY_REVIEW_PASS
        or not _identity_matches_selection(payload, selection=selection, row=selection_row)
        or _REVIEWER_ID.fullmatch(str(payload.get("reviewer_id") or "")) is None
        or payload.get("provider_name") != "COLLABORATION_CODEX"
        or _RUN_ID.fullmatch(str(payload.get("provider_call_id") or "")) is None
        or any(
            _HEX64.fullmatch(str(payload.get(field) or "")) is None
            for field in ("prompt_hash", "response_hash")
        )
        or payload.get("result_id") != result.get("result_id")
        or payload.get("result_payload_hash") != stable_hash(result)
        or payload.get("production_receipt_id") != receipt.get("receipt_id")
        or payload.get("production_receipt_hash") != stable_hash(receipt)
        or vector != _vector(result.get("component_score_vector"))
        or not _is_score(payload.get("recomputed_total_score"))
        or not math.isclose(
            float(payload.get("recomputed_total_score")),
            float(result.get("total_score")),
            rel_tol=0.0,
            abs_tol=1e-9,
        )
        or payload.get("recomputed_canonical_stage") != result.get("canonical_stage")
        or any(
            payload.get(field) is not True
            for field in (
                "production_research_complete",
                "score_reproduction_matches",
                "stage_reproduction_matches",
                "evidence_lineage_complete",
                "independent_review",
                "review_complete",
            )
        )
        or payload.get("verdict") != "APPROVE"
        or payload.get("critical_findings") != []
        or not _is_count(payload.get("critical_count_sum"))
        or payload.get("critical_count_sum") != 0
        or not _false_authority(payload)
        or payload.get("review_id") != "CANARYREV-" + stable_hash(body)[:24]
        or _contains_forbidden_text(payload)
    ):
        raise ValueError("independent canary review contract is invalid")


def _summary_row(
    *,
    result: Mapping[str, Any],
    receipt: Mapping[str, Any],
    reviews: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    ordered = tuple(sorted(reviews, key=lambda item: str(item["reviewer_id"])))
    return {
        "archetype_id": result["archetype_id"],
        "target_id": result["target_id"],
        "selection_id": result["selection_id"],
        "result_id": result["result_id"],
        "result_payload_hash": stable_hash(result),
        "production_receipt_id": receipt["receipt_id"],
        "production_receipt_hash": stable_hash(receipt),
        "reviewer_ids": [item["reviewer_id"] for item in ordered],
        "review_ids": [item["review_id"] for item in ordered],
        "review_receipt_hashes": [stable_hash(item) for item in ordered],
        "component_score_vector": dict(result["component_score_vector"]),
        "total_score": result["total_score"],
        "canonical_stage": result["canonical_stage"],
        "score_valid": True,
        "stage_final": True,
    }


def _diagnostic(
    *,
    status: str,
    selection: Mapping[str, Any],
    complete_count: int,
    review_count: int,
    pending_reasons: Sequence[Mapping[str, Any]],
    failures: Sequence[Mapping[str, Any]],
    summary: Mapping[str, Any] | None,
) -> Mapping[str, Any]:
    return {
        "schema_version": CANARY_COMPILATION_SCHEMA,
        "status": status,
        "selection_roster_hash": str(selection.get("selection_roster_hash") or ""),
        "required_archetypes": list(REQUIRED_ARCHETYPES),
        "complete_canary_count": complete_count,
        "independent_review_count": review_count,
        "pending_reasons": [dict(item) for item in pending_reasons],
        "failures": [dict(item) for item in failures],
        "summary": dict(summary) if summary is not None else None,
        "score_or_stage_authority": False,
        "production_readiness_authority": False,
    }


def compile_cross_archetype_canary_results(
    *,
    selection: Mapping[str, Any],
    bundles_by_archetype: Mapping[str, Mapping[str, Any]],
    pending_reasons: Sequence[Mapping[str, Any]] = (),
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> Mapping[str, Any]:
    """Compile all five result/receipt/review bundles or fail closed."""

    rows = _selection_rows(
        selection,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    failures: list[Mapping[str, Any]] = []
    pending = [dict(item) for item in pending_reasons]
    summary_rows: list[Mapping[str, Any]] = []
    review_count = 0
    seen_result_ids: set[str] = set()
    seen_receipt_ids: set[str] = set()
    seen_review_ids: set[str] = set()
    seen_provider_call_ids: set[str] = set()
    seen_prompt_hashes: set[str] = set()
    seen_response_hashes: set[str] = set()
    if set(bundles_by_archetype) - set(REQUIRED_ARCHETYPES):
        failures.append({"code": "FOREIGN_CANARY_BUNDLE"})
    for archetype_id in REQUIRED_ARCHETYPES:
        bundle = bundles_by_archetype.get(archetype_id)
        if bundle is None:
            pending.append({"code": "CANARY_BUNDLE_MISSING", "archetype_id": archetype_id})
            continue
        if set(bundle) != {"result", "receipt", "reviews"}:
            failures.append({"code": "CANARY_BUNDLE_SHAPE_INVALID", "archetype_id": archetype_id})
            continue
        try:
            result = _mapping(bundle.get("result"), context="canary result")
            receipt = _mapping(bundle.get("receipt"), context="canary receipt")
            reviews_raw = bundle.get("reviews")
            if not isinstance(reviews_raw, Sequence) or isinstance(
                reviews_raw, (str, bytes, bytearray)
            ):
                raise ValueError("independent reviews must be a list")
            reviews = tuple(_mapping(item, context="independent review") for item in reviews_raw)
            if len(reviews) != 2:
                raise ValueError("exactly two independent reviews are required")
            row = rows[archetype_id]
            validate_full_researcher_mode_canary_result(
                result, selection=selection, selection_row=row
            )
            validate_full_researcher_mode_canary_receipt(
                receipt, result=result, selection=selection, selection_row=row
            )
            for review in reviews:
                validate_independent_canary_review(
                    review,
                    result=result,
                    receipt=receipt,
                    selection=selection,
                    selection_row=row,
                )
            uniqueness_fields = ("reviewer_id", "review_id", "provider_call_id", "response_hash")
            if any(len({str(item[field]) for item in reviews}) != 2 for field in uniqueness_fields):
                raise ValueError("the two review receipts are not independent")
            result_id = str(result["result_id"])
            receipt_id = str(receipt["receipt_id"])
            if result_id in seen_result_ids or receipt_id in seen_receipt_ids:
                raise ValueError("result or production receipt identity was reused")
            seen_result_ids.add(result_id)
            seen_receipt_ids.add(receipt_id)
            for review in reviews:
                review_id = str(review["review_id"])
                call_id = str(review["provider_call_id"])
                prompt_hash = str(review["prompt_hash"])
                response_hash = str(review["response_hash"])
                if (
                    review_id in seen_review_ids
                    or call_id in seen_provider_call_ids
                    or prompt_hash in seen_prompt_hashes
                    or response_hash in seen_response_hashes
                ):
                    raise ValueError("an independent review lineage was reused across canaries")
                seen_review_ids.add(review_id)
                seen_provider_call_ids.add(call_id)
                seen_prompt_hashes.add(prompt_hash)
                seen_response_hashes.add(response_hash)
            summary_rows.append(_summary_row(result=result, receipt=receipt, reviews=reviews))
            review_count += 2
        except (KeyError, TypeError, ValueError) as exc:
            failures.append(
                {
                    "code": "CANARY_BUNDLE_INVALID",
                    "archetype_id": archetype_id,
                    "detail": str(exc),
                }
            )

    if failures:
        return _diagnostic(
            status=CANARY_COMPILATION_FAIL,
            selection=selection,
            complete_count=len(summary_rows),
            review_count=review_count,
            pending_reasons=pending,
            failures=failures,
            summary=None,
        )
    if pending or len(summary_rows) != len(REQUIRED_ARCHETYPES):
        return _diagnostic(
            status=CANARY_COMPILATION_PENDING,
            selection=selection,
            complete_count=len(summary_rows),
            review_count=review_count,
            pending_reasons=pending,
            failures=(),
            summary=None,
        )
    summary_body = {
        "schema_version": CANARY_SUMMARY_SCHEMA,
        "status": CANARY_SUMMARY_PASS,
        "as_of_date": selection["selection_as_of_date"],
        "selection_roster_hash": selection["selection_roster_hash"],
        "required_archetypes": list(REQUIRED_ARCHETYPES),
        "canary_count": len(REQUIRED_ARCHETYPES),
        "independent_review_count": 2 * len(REQUIRED_ARCHETYPES),
        "canaries": summary_rows,
        "critical_count_sum": 0,
        "score_or_stage_authority": False,
        "production_readiness_authority": False,
    }
    summary = {
        **summary_body,
        "summary_id": "CANARYSUM-" + stable_hash(summary_body)[:24],
    }
    validate_cross_archetype_canary_summary(
        summary,
        selection=selection,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    return _diagnostic(
        status=CANARY_COMPILATION_PASS,
        selection=selection,
        complete_count=len(summary_rows),
        review_count=review_count,
        pending_reasons=(),
        failures=(),
        summary=summary,
    )


def validate_cross_archetype_canary_summary(
    payload: Mapping[str, Any],
    *,
    selection: Mapping[str, Any],
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
) -> None:
    """Validate the final summary shape and exact Phase-105 identity binding."""

    rows = _selection_rows(
        selection,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    canaries = tuple(payload.get("canaries") or ())
    body = {key: value for key, value in payload.items() if key != "summary_id"}
    if (
        set(payload) != _SUMMARY_KEYS
        or payload.get("schema_version") != CANARY_SUMMARY_SCHEMA
        or payload.get("status") != CANARY_SUMMARY_PASS
        or payload.get("as_of_date") != selection.get("selection_as_of_date")
        or not _is_iso_date(payload.get("as_of_date"))
        or payload.get("selection_roster_hash") != selection.get("selection_roster_hash")
        or tuple(payload.get("required_archetypes") or ()) != REQUIRED_ARCHETYPES
        or payload.get("canary_count") != len(REQUIRED_ARCHETYPES)
        or payload.get("independent_review_count") != 2 * len(REQUIRED_ARCHETYPES)
        or len(canaries) != len(REQUIRED_ARCHETYPES)
        or not _is_count(payload.get("critical_count_sum"))
        or payload.get("critical_count_sum") != 0
        or not _false_authority(payload)
        or payload.get("summary_id") != "CANARYSUM-" + stable_hash(body)[:24]
        or _contains_forbidden_text(payload)
    ):
        raise ValueError("cross-archetype canary summary contract is invalid")
    result_ids: list[str] = []
    receipt_ids: list[str] = []
    review_ids: list[str] = []
    review_hashes: list[str] = []
    for expected_archetype, raw in zip(REQUIRED_ARCHETYPES, canaries):
        row = _mapping(raw, context="canary summary row")
        selection_row = rows[expected_archetype]
        vector = _vector(row.get("component_score_vector"))
        if (
            set(row) != _SUMMARY_ROW_KEYS
            or row.get("archetype_id") != expected_archetype
            or row.get("target_id") != selection_row.get("target_id")
            or row.get("selection_id") != selection_row.get("selection_id")
            or _RUN_ID.fullmatch(str(row.get("result_id") or "")) is None
            or _HEX64.fullmatch(str(row.get("result_payload_hash") or "")) is None
            or _RUN_ID.fullmatch(str(row.get("production_receipt_id") or "")) is None
            or _HEX64.fullmatch(str(row.get("production_receipt_hash") or "")) is None
            or not isinstance(row.get("reviewer_ids"), list)
            or len(row.get("reviewer_ids") or ()) != 2
            or len(set(row.get("reviewer_ids") or ())) != 2
            or not isinstance(row.get("review_ids"), list)
            or len(row.get("review_ids") or ()) != 2
            or len(set(row.get("review_ids") or ())) != 2
            or not isinstance(row.get("review_receipt_hashes"), list)
            or len(row.get("review_receipt_hashes") or ()) != 2
            or len(set(row.get("review_receipt_hashes") or ())) != 2
            or any(
                _HEX64.fullmatch(str(value or "")) is None
                for value in row.get("review_receipt_hashes") or ()
            )
            or not _is_score(row.get("total_score"))
            or not math.isclose(
                sum(vector.values()),
                float(row.get("total_score")),
                rel_tol=0.0,
                abs_tol=1e-9,
            )
            or row.get("canonical_stage") not in _CANONICAL_STAGES
            or row.get("score_valid") is not True
            or row.get("stage_final") is not True
        ):
            raise ValueError("cross-archetype canary summary row is invalid")
        result_ids.append(str(row["result_id"]))
        receipt_ids.append(str(row["production_receipt_id"]))
        review_ids.extend(str(value) for value in row["review_ids"])
        review_hashes.extend(str(value) for value in row["review_receipt_hashes"])
    if (
        len(set(result_ids)) != len(REQUIRED_ARCHETYPES)
        or len(set(receipt_ids)) != len(REQUIRED_ARCHETYPES)
        or len(set(review_ids)) != 2 * len(REQUIRED_ARCHETYPES)
        or len(set(review_hashes)) != 2 * len(REQUIRED_ARCHETYPES)
    ):
        raise ValueError("cross-archetype canary summary reuses a receipt identity")


def _directory_name(row: Mapping[str, Any]) -> str:
    archetype_id = str(row.get("archetype_id") or "")
    target_id = str(row.get("target_id") or "")
    if archetype_id not in REQUIRED_ARCHETYPES or _TARGET.fullmatch(target_id) is None:
        raise ValueError("unsafe canary directory identity")
    return f"{archetype_id}_{target_id}"


def _read_json_at(parent_fd: int, name: str) -> Mapping[str, Any]:
    encoded, _metadata = _read_regular_from_directory(parent_fd, name)
    try:
        payload = json.loads(encoded.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{name} is not valid JSON") from exc
    return _mapping(payload, context=name)


def _open_directory_at(parent_fd: int, name: str) -> int:
    if not name or name in {".", ".."} or "/" in name:
        raise ValueError("unsafe canary directory name")
    descriptor = os.open(
        name,
        os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0),
        dir_fd=parent_fd,
    )
    metadata = os.fstat(descriptor)
    if not stat.S_ISDIR(metadata.st_mode) or metadata.st_mode & 0o022:
        os.close(descriptor)
        raise ValueError("canary input directory is unsafe")
    return descriptor


def compile_cross_archetype_canary_directory(
    *,
    selection: Mapping[str, Any],
    live_root: str | Path,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
    repo_root: str | Path = ".",
) -> Mapping[str, Any]:
    """Load the exact five immutable input directories and compile them."""

    rows = _selection_rows(
        selection,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    expected = {_directory_name(rows[item]): item for item in REQUIRED_ARCHETYPES}
    root_path = Path(live_root).absolute()
    try:
        root_fd = _open_existing_directory_no_symlinks(root_path)
    except FileNotFoundError:
        return compile_cross_archetype_canary_results(
            selection=selection,
            bundles_by_archetype={},
            pending_reasons=({"code": "CURRENT_LIVE_CANARY_ROOT_MISSING"},),
            issuer_business_profile_manifest=issuer_business_profile_manifest,
        )
    except (OSError, ValueError) as exc:
        return _diagnostic(
            status=CANARY_COMPILATION_FAIL,
            selection=selection,
            complete_count=0,
            review_count=0,
            pending_reasons=(),
            failures=({"code": "CURRENT_LIVE_CANARY_ROOT_UNSAFE", "detail": str(exc)},),
            summary=None,
        )
    bundles: dict[str, Mapping[str, Any]] = {}
    pending: list[Mapping[str, Any]] = []
    failures: list[Mapping[str, Any]] = []
    try:
        root_metadata = os.fstat(root_fd)
        if not stat.S_ISDIR(root_metadata.st_mode) or root_metadata.st_mode & 0o022:
            raise ValueError("current live canary root is unsafe")
        actual = set(os.listdir(root_fd))
        extras = sorted(actual - set(expected))
        if extras:
            failures.append({"code": "FOREIGN_CURRENT_LIVE_CANARY_ENTRY", "detail": extras})
        for directory_name, archetype_id in expected.items():
            if directory_name not in actual:
                pending.append({"code": "CANARY_DIRECTORY_MISSING", "archetype_id": archetype_id})
                continue
            directory_fd = -1
            reviews_fd = -1
            try:
                directory_fd = _open_directory_at(root_fd, directory_name)
                entries = set(os.listdir(directory_fd))
                thin_entries = {
                    CANARY_RESULT_NAME,
                    CANARY_RECEIPT_NAME,
                    CANARY_REVIEWS_DIRECTORY,
                }
                # Import locally: the compact module imports this module's
                # result validators while constructing its nested receipt.
                from e2r.production.v6_canary_compact_receipt import (
                    RECEIPT_MANIFEST_NAME,
                    REQUIRED_ARTIFACT_NAMES,
                    REVIEW_DIRECTORY_NAME,
                    load_selection_bound_canary_directory,
                )

                strong_entries = {
                    RECEIPT_MANIFEST_NAME,
                    REVIEW_DIRECTORY_NAME,
                    *REQUIRED_ARTIFACT_NAMES,
                }
                if entries == strong_entries:
                    loaded = load_selection_bound_canary_directory(
                        receipt_directory=root_path / directory_name,
                        selection=selection,
                        repo_root=repo_root,
                        issuer_business_profile_manifest=(
                            issuer_business_profile_manifest
                        ),
                    )
                    artifacts = _mapping(
                        loaded.get("artifacts"), context="compact artifacts"
                    )
                    score = _mapping(
                        artifacts.get("score_receipt.json"),
                        context="compact score receipt",
                    )
                    result = _mapping(
                        score.get("canary_result"), context="full canary result"
                    )
                    receipt = _mapping(
                        score.get("production_receipt"),
                        context="full canary production receipt",
                    )
                    compact_reviews = tuple(
                        _mapping(item, context="compact independent review")
                        for item in loaded.get("reviews") or ()
                    )
                    if len(compact_reviews) != 2:
                        raise ValueError(
                            "strong compact canary requires exactly two reviews"
                        )
                    reviews = tuple(
                        build_independent_canary_review(
                            reviewer_id=str(review["reviewer_id"]),
                            provider_call_id=str(review["provider_call_id"]),
                            prompt_hash=str(review["prompt_hash"]),
                            response_hash=str(review["response_hash"]),
                            result=result,
                            receipt=receipt,
                        )
                        for review in compact_reviews
                    )
                    bundles[archetype_id] = {
                        "result": result,
                        "receipt": receipt,
                        "reviews": reviews,
                    }
                    continue
                if entries - thin_entries:
                    raise ValueError("canary directory contains an unaccounted entry")
                missing_entries = thin_entries - entries
                if missing_entries:
                    pending.append(
                        {
                            "code": "CANARY_INPUT_FILE_MISSING",
                            "archetype_id": archetype_id,
                            "detail": sorted(missing_entries),
                        }
                    )
                    continue
                result = _read_json_at(directory_fd, CANARY_RESULT_NAME)
                receipt = _read_json_at(directory_fd, CANARY_RECEIPT_NAME)
                reviews_fd = _open_directory_at(directory_fd, CANARY_REVIEWS_DIRECTORY)
                review_entries = set(os.listdir(reviews_fd))
                missing_reviews = set(CANARY_REVIEW_NAMES) - review_entries
                extra_reviews = review_entries - set(CANARY_REVIEW_NAMES)
                if extra_reviews:
                    raise ValueError("independent review directory contains an unaccounted entry")
                if missing_reviews:
                    pending.append(
                        {
                            "code": "INDEPENDENT_REVIEW_FILE_MISSING",
                            "archetype_id": archetype_id,
                            "detail": sorted(missing_reviews),
                        }
                    )
                    continue
                reviews = tuple(_read_json_at(reviews_fd, name) for name in CANARY_REVIEW_NAMES)
                if set(os.listdir(reviews_fd)) != set(CANARY_REVIEW_NAMES):
                    raise ValueError("independent review directory changed while read")
                if set(os.listdir(directory_fd)) != thin_entries:
                    raise ValueError("canary directory changed while read")
                bundles[archetype_id] = {
                    "result": result,
                    "receipt": receipt,
                    "reviews": reviews,
                }
            except (OSError, TypeError, ValueError) as exc:
                failures.append(
                    {"code": "CANARY_INPUT_TREE_INVALID", "archetype_id": archetype_id, "detail": str(exc)}
                )
            finally:
                if reviews_fd >= 0:
                    os.close(reviews_fd)
                if directory_fd >= 0:
                    os.close(directory_fd)
        if set(os.listdir(root_fd)) != actual:
            failures.append({"code": "CURRENT_LIVE_CANARY_ROOT_CHANGED_DURING_READ"})
    except (OSError, ValueError) as exc:
        failures.append({"code": "CURRENT_LIVE_CANARY_ROOT_UNSAFE", "detail": str(exc)})
    finally:
        os.close(root_fd)
    if failures:
        return _diagnostic(
            status=CANARY_COMPILATION_FAIL,
            selection=selection,
            complete_count=0,
            review_count=0,
            pending_reasons=pending,
            failures=failures,
            summary=None,
        )
    return compile_cross_archetype_canary_results(
        selection=selection,
        bundles_by_archetype=bundles,
        pending_reasons=pending,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )


def seal_cross_archetype_canary_summary(
    path: str | Path,
    payload: Mapping[str, Any],
    *,
    selection: Mapping[str, Any],
    live_root: str | Path,
    issuer_business_profile_manifest: Mapping[str, Any] | None = None,
    repo_root: str | Path = ".",
) -> Path:
    """Atomically create the immutable Phase-106 summary seal."""

    validate_cross_archetype_canary_summary(
        payload,
        selection=selection,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
    )
    recomputed = compile_cross_archetype_canary_directory(
        selection=selection,
        live_root=live_root,
        issuer_business_profile_manifest=issuer_business_profile_manifest,
        repo_root=repo_root,
    )
    if (
        recomputed.get("status") != CANARY_COMPILATION_PASS
        or not isinstance(recomputed.get("summary"), Mapping)
        or dict(recomputed["summary"]) != dict(payload)
    ):
        raise ValueError("canary summary does not match the five immutable input bundles")
    destination = Path(path).absolute()
    encoded = (
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        + "\n"
    ).encode("utf-8")
    try:
        parent_fd = _open_or_create_directory_no_symlinks(destination.parent)
    except OSError as exc:
        raise ValueError("canary summary parent is unsafe") from exc
    temporary_name = f".{destination.name}.{secrets.token_hex(16)}.tmp"
    temporary_fd = -1
    guard_fd = -1
    linked = False
    created = False
    completed = False
    try:
        try:
            existing, _ = _read_regular_from_directory(parent_fd, destination.name)
        except FileNotFoundError:
            existing = None
        if existing is not None:
            if existing != encoded:
                raise ValueError("canary summary seal already has different content")
            return destination
        temporary_fd = os.open(
            temporary_name,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
            0o600,
            dir_fd=parent_fd,
        )
        with os.fdopen(temporary_fd, "wb") as handle:
            temporary_fd = -1
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
            guard_fd = os.dup(handle.fileno())
        temporary_stat = os.fstat(guard_fd)
        try:
            os.link(
                temporary_name,
                destination.name,
                src_dir_fd=parent_fd,
                dst_dir_fd=parent_fd,
                follow_symlinks=False,
            )
            linked = True
            created = True
        except FileExistsError:
            existing, _ = _read_regular_from_directory(parent_fd, destination.name)
            if existing != encoded:
                raise ValueError("canary summary was concurrently replaced")
            return destination
        destination_stat = os.stat(destination.name, dir_fd=parent_fd, follow_symlinks=False)
        if (destination_stat.st_dev, destination_stat.st_ino) != (
            temporary_stat.st_dev,
            temporary_stat.st_ino,
        ):
            raise ValueError("canary summary inode changed during creation")
        linked_bytes, _ = _read_regular_from_directory(
            parent_fd, destination.name, expected_link_count=2
        )
        if linked_bytes != encoded:
            raise ValueError("canary summary bytes changed during creation")
        os.unlink(temporary_name, dir_fd=parent_fd)
        linked = False
        final_bytes, final_stat = _read_regular_from_directory(parent_fd, destination.name)
        guarded = os.fstat(guard_fd)
        expected_identity = (
            temporary_stat.st_dev,
            temporary_stat.st_ino,
            temporary_stat.st_uid,
            temporary_stat.st_gid,
            stat.S_IMODE(temporary_stat.st_mode),
        )
        if (
            final_bytes != encoded
            or expected_identity
            != (
                final_stat.st_dev,
                final_stat.st_ino,
                final_stat.st_uid,
                final_stat.st_gid,
                stat.S_IMODE(final_stat.st_mode),
            )
            or expected_identity
            != (
                guarded.st_dev,
                guarded.st_ino,
                guarded.st_uid,
                guarded.st_gid,
                stat.S_IMODE(guarded.st_mode),
            )
        ):
            raise ValueError("canary summary changed after atomic creation")
        os.fsync(parent_fd)
        reopened_fd = _open_existing_directory_no_symlinks(destination.parent)
        try:
            pinned = os.fstat(parent_fd)
            reopened = os.fstat(reopened_fd)
            if (pinned.st_dev, pinned.st_ino) != (reopened.st_dev, reopened.st_ino):
                raise ValueError("canary summary parent changed during creation")
        finally:
            os.close(reopened_fd)
        completed = True
    finally:
        if temporary_fd >= 0:
            os.close(temporary_fd)
        if guard_fd >= 0:
            os.close(guard_fd)
        try:
            os.unlink(temporary_name, dir_fd=parent_fd)
        except FileNotFoundError:
            pass
        if linked or (created and not completed):
            try:
                os.unlink(destination.name, dir_fd=parent_fd)
            except FileNotFoundError:
                pass
        os.close(parent_fd)
    return destination


__all__ = [
    "CANARY_COMPILATION_FAIL",
    "CANARY_COMPILATION_PASS",
    "CANARY_COMPILATION_PENDING",
    "CANARY_RECEIPT_NAME",
    "CANARY_RECEIPT_SCHEMA",
    "CANARY_RESULT_NAME",
    "CANARY_RESULT_PASS",
    "CANARY_RESULT_SCHEMA",
    "CANARY_REVIEW_NAMES",
    "CANARY_REVIEW_PASS",
    "CANARY_REVIEW_SCHEMA",
    "CANARY_REVIEWS_DIRECTORY",
    "CANARY_SUMMARY_PASS",
    "CANARY_SUMMARY_SCHEMA",
    "build_full_researcher_mode_canary_receipt",
    "build_independent_canary_review",
    "compile_cross_archetype_canary_directory",
    "compile_cross_archetype_canary_results",
    "seal_cross_archetype_canary_summary",
    "validate_cross_archetype_canary_summary",
    "validate_full_researcher_mode_canary_receipt",
    "validate_full_researcher_mode_canary_result",
    "validate_independent_canary_review",
]

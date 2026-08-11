"""Natural Phase-107 L5 runner and Gold-free tracked-style receipts.

The Phase-105 exact-five canaries are a validation roster, not evidence that a
current Census candidate reached L5 naturally.  This module therefore starts
only from a COMPLETE current planner row loaded without an issuer-profile
override, resumes one canonical Researcher Mode checkpoint, and publishes a
separate compact receipt whose manifest binds the KRX/trigger/depth/planner
lineage.

The eight score-lineage leaves intentionally reuse the tracked-receipt row
formats.  The score and manifest schemas are Phase-107 specific because a
natural production completion must not invent a post-run Gold result.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable, Mapping, Sequence
from datetime import date
import hashlib
import json
import math
import os
from pathlib import Path
import re
import secrets
import shutil
from typing import Any

from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_compact_receipt import (
    _material_gap_count,
    _production_provider_accounting,
)
from e2r.production.v6_canary_selection import (
    _candidate_projection,
    _open_existing_directory_no_symlinks,
    _open_or_create_directory_no_symlinks,
    _read_regular_from_directory,
    load_current_live_selection_inputs,
)
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode.canary_leaf_contract import (
    canary_output_tree_hash,
)
from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    CollaborationCodexResearcherProvider,
)
from e2r.research_brain.researcher_mode.collaboration_envelope_contract import (
    validate_collaboration_request,
)
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    CurrentResearchTarget,
    CurrentResearcherModeConfig,
    CurrentResearcherModeTargetRunner,
    FactExtractionCheckpointPending,
)
from e2r.research_brain.researcher_mode.schemas import (
    CANONICAL_COMPONENT_ORDER,
)
from e2r.research_brain.researcher_mode.tracked_readiness import (
    canonical_repository_root,
)
from e2r.research_brain.researcher_mode.tracked_receipts import (
    ANCHOR_RECEIPT_KEYS,
    COMPONENT_RECEIPT_KEYS,
    JUDGE_RECEIPT_KEYS,
    PROVIDER_CALL_COMMON_KEYS,
    PROVIDER_CALL_FACT_KEYS,
    PROVIDER_CALL_FULL_RUN_KEYS,
    PROVIDER_ROUTE,
    REQUIRED_TARGET_FILES,
    SCORING_FACT_RECEIPT_KEYS,
    SOURCE_RECEIPT_KEYS,
    STAGECOURT_RECEIPT_KEYS,
    STAGECOURT_RECEIPT_SCHEMA,
    VERIFICATION_FAIL,
    VERIFICATION_PASS,
    VERIFICATION_SCHEMA,
    _anchor_receipts,
    _component_receipts,
    _contains_local_provider_marker,
    _decision_rows,
    _embedded_fact_journal_call_is_exact,
    _fact_scope_attestation_hash,
    _fact_receipts,
    _judge_receipts,
    _provider_call_receipts,
    _provider_kind,
    _recompute_stage,
    _source_receipts,
    _stage_receipt,
    _tracked_component_maxima,
    _tracked_historical_anchors,
    _verify_component_formula,
    receipt_content_index,
    receipt_content_tree_hash,
    stagecourt_rule_hash,
)


PHASE107_DEEP_RUN_SCHEMA = "e2r_v6_current_krx_deep_receipt_runner_v1"
PHASE107_DEEP_RUN_PASS = "E2R_V6_CURRENT_KRX_DEEP_RECEIPT_RUN_PASS"
PHASE107_DEEP_RUN_PENDING = "E2R_V6_CURRENT_KRX_DEEP_RECEIPT_RUN_PENDING"
PHASE107_DEEP_RECEIPT_SCHEMA = "e2r_v6_current_krx_deep_receipt_manifest_v1"
PHASE107_DEEP_RECEIPT_PASS = "E2R_V6_CURRENT_KRX_DEEP_RECEIPT_PASS"
PHASE107_DEEP_SCORE_SCHEMA = "e2r_v6_current_krx_deep_score_receipt_v1"
PHASE107_TERMINAL_RESEARCH_STATUS = (
    "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
)

_TARGET_RE = re.compile(r"[0-9A-Z]{6}\Z")
_HEX64_RE = re.compile(r"[0-9a-f]{64}\Z")
_CANONICAL_STAGES = frozenset(
    {"0", "1", "2", "3-Green", "3-Yellow", "3-Red", "4A", "4B", "4C", "5"}
)
_JUDGE_ROLES = frozenset({"ANALYST", "SKEPTIC", "CALIBRATION_JUDGE"})
_ALLOWED_PROVIDER_KINDS = frozenset({"CODEX", "COLLABORATION_CODEX"})

_SCORE_KEYS = frozenset(
    {
        "schema_version",
        "receipt_id",
        "target_id",
        "company_name",
        "as_of_date",
        "latest_trading_snapshot_date",
        "archetype_id",
        "score_scale",
        "score_valid",
        "research_complete",
        "semantic_saturation_certified",
        "material_gap_count",
        "provider_error_count",
        "unauthorized_provider_call_count",
        "local_provider_call_count",
        "query_count",
        "document_count",
        "fact_count",
        "counterfact_count",
        "component_score_vector",
        "component_max_vector",
        "total_score",
        "total_score_recomputed",
        "component_sum_matches_total",
        "canonical_stage",
        "score_status",
        "stagecourt_status",
        "production_research_status",
        "gold_visibility",
        "score_or_stage_authority",
    }
)

_LINEAGE_KEYS = frozenset(
    {
        "planner_terminal_status",
        "planner_run_id",
        "blind_input_id",
        "plan_hash",
        "depth_decision_id",
        "depth_decision_hash",
        "candidate_event_id",
        "candidate_event_hash",
        "trigger_signal_ids",
        "trigger_types",
        "trigger_lineage_hash",
        "source_refs",
        "event_source_refs",
        "event_latest_effective_date",
        "event_summary_hash",
        "leading_archetype_id",
        "direct_current_supporting_fact_ids",
        "recipe_ids",
        "available_source_families",
        "priority_score",
        "krx_effective_date",
        "krx_source_url",
        "krx_source_hash",
        "krx_request_id",
        "natural_selection",
        "official_profile_binding",
        "phase105_canary_receipt_reused",
    }
)

_MANIFEST_KEYS = frozenset(
    {
        "schema_version",
        "status",
        "receipt_id",
        "receipt_payload_hash",
        "target_id",
        "company_name",
        "as_of_date",
        "latest_trading_snapshot_date",
        "archetype_id",
        "natural_lineage",
        "natural_lineage_hash",
        "output_tree_hash",
        "artifact_names",
        "tracked_receipt_content_index",
        "tracked_receipt_tree_hash",
        "component_count",
        "judge_decision_count",
        "scoring_fact_count",
        "source_count",
        "anchor_count",
        "provider_call_count",
        "query_count",
        "document_count",
        "fact_count",
        "counterfact_count",
        "material_gap_count",
        "provider_error_count",
        "unauthorized_provider_call_count",
        "local_provider_call_count",
        "score_valid",
        "canonical_stage",
        "gold_visibility",
        "score_or_stage_authority",
        "production_readiness_authority",
    }
)


CheckpointRunnerFactory = Callable[[Mapping[str, Any]], Any]


def _mapping(value: object, *, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{context} must be an object")
    return value


def _rows(value: object, *, context: str) -> tuple[Mapping[str, Any], ...]:
    if isinstance(value, (str, bytes, bytearray)) or not isinstance(value, Sequence):
        raise ValueError(f"{context} must be an array")
    return tuple(_mapping(row, context=f"{context} row") for row in value)


def _finite(value: object) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def _read_json(path: Path) -> Mapping[str, Any]:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"required JSON leaf is unsafe or missing: {path.name}")
    try:
        return _mapping(json.loads(path.read_text(encoding="utf-8")), context=path.name)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"required JSON leaf is invalid: {path.name}") from exc


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"required JSONL leaf is unsafe or missing: {path.name}")
    try:
        return tuple(
            _mapping(json.loads(line), context=f"{path.name} row")
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"required JSONL leaf is invalid: {path.name}") from exc


def _sha256_text(value: object) -> str:
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()


def _excerpt(value: object, limit: int = 240) -> str:
    compact = " ".join(str(value).split())
    return compact if len(compact) <= limit else compact[: limit - 1] + "…"


def _index(
    rows: Sequence[Mapping[str, Any]], key: str, *, context: str
) -> dict[str, Mapping[str, Any]]:
    result: dict[str, Mapping[str, Any]] = {}
    for row in rows:
        identity = str(row.get(key) or "")
        if not identity or identity in result:
            raise ValueError(f"{context} identities must be unique and nonempty")
        result[identity] = row
    return result


def project_natural_current_candidate(
    raw_candidate: Mapping[str, Any],
    *,
    trigger_rows: Sequence[Mapping[str, Any]],
    as_of_date: str,
) -> Mapping[str, Any]:
    """Validate and project one real COMPLETE KRX planner lineage.

    No issuer profile is accepted here.  An ABSTAINED/forced row consequently
    cannot be made natural by changing a label in a later receipt.
    """

    date.fromisoformat(as_of_date)
    projected = _candidate_projection(raw_candidate, selection_date=as_of_date)
    depth = _mapping(raw_candidate.get("depth_decision"), context="depth decision")
    if (
        projected.get("planner_terminal_status") != "COMPLETE"
        or projected.get("official_profile_binding") is not None
        or depth.get("selected_for_deep") is not True
        or depth.get("selected_for_brain") is not True
        or depth.get("acquisition_eligible") is not True
        or depth.get("maximum_depth") != "L3_RESEARCH_BRAIN"
    ):
        raise ValueError("natural Phase107 candidate is not a COMPLETE selected L3 plan")
    priority = depth.get("priority_score")
    if not _finite(priority):
        raise ValueError("natural Phase107 priority score is invalid")
    target_id = str(projected["target_id"])
    referenced_ids = tuple(str(value) for value in projected["event_trigger_signal_ids"])
    signal_by_id = _index(trigger_rows, "trigger_signal_id", context="trigger signal")
    ordered_target_signals = tuple(
        sorted(
            (
                row
                for row in trigger_rows
                if str(row.get("target_id") or "") == target_id
            ),
            key=lambda row: (
                str(row.get("effective_date") or ""),
                str(row.get("trigger_signal_id") or ""),
            ),
        )
    )
    expected_ids = tuple(
        str(row.get("trigger_signal_id") or "") for row in ordered_target_signals
    )
    expected_types = tuple(
        sorted({str(row.get("trigger_type") or "") for row in ordered_target_signals})
    )
    expected_sources = tuple(
        dict.fromkeys(
            str(source)
            for row in ordered_target_signals
            for source in row.get("source_refs") or ()
        )
    )
    expected_latest = max(
        (str(row.get("effective_date") or "") for row in ordered_target_signals),
        default="",
    )
    expected_summary = (
        f"{projected['company_name']}: {', '.join(expected_types)} current trigger "
        f"{len(ordered_target_signals)}건 검증 필요"
    )
    if (
        not ordered_target_signals
        or referenced_ids != expected_ids
        or tuple(projected.get("event_trigger_types") or ()) != expected_types
        or tuple(projected.get("event_source_refs") or ()) != expected_sources
        or str(projected.get("event_latest_effective_date") or "") != expected_latest
        or str(projected.get("event_summary") or "") != expected_summary
        or any(
            str(row.get("target_name") or "") != projected["company_name"]
            for row in ordered_target_signals
        )
    ):
        raise ValueError("natural candidate event does not equal its complete trigger roster")
    referenced: list[Mapping[str, Any]] = []
    for signal_id in referenced_ids:
        signal = signal_by_id.get(signal_id)
        if (
            signal is None
            or str(signal.get("target_id") or "") != target_id
            or signal.get("investigation_required") is not True
            or str(signal.get("effective_date") or "") > as_of_date
        ):
            raise ValueError("natural candidate trigger lineage is incomplete or future-dated")
        referenced.append(signal)
    if not referenced:
        raise ValueError("natural candidate requires at least one current trigger")
    lineage = {
        "planner_terminal_status": "COMPLETE",
        "planner_run_id": projected["planner_run_id"],
        "blind_input_id": projected["blind_input_id"],
        "plan_hash": projected["plan_hash"],
        "depth_decision_id": projected["depth_decision_id"],
        "depth_decision_hash": projected["depth_decision_hash"],
        "candidate_event_id": projected["candidate_event_id"],
        "candidate_event_hash": projected["candidate_event_hash"],
        "trigger_signal_ids": list(referenced_ids),
        "trigger_types": list(expected_types),
        "trigger_lineage_hash": stable_hash([dict(row) for row in referenced]),
        "source_refs": list(projected["source_refs"]),
        "event_source_refs": list(projected["event_source_refs"]),
        "event_latest_effective_date": projected["event_latest_effective_date"],
        "event_summary_hash": stable_hash(projected["event_summary"]),
        "leading_archetype_id": projected["leading_archetype_id"],
        "direct_current_supporting_fact_ids": list(
            projected["direct_current_supporting_fact_ids"]
        ),
        "recipe_ids": list(projected["recipe_ids"]),
        "available_source_families": list(projected["available_source_families"]),
        "priority_score": float(priority),
        "krx_effective_date": projected["krx_effective_date"],
        "krx_source_url": projected["krx_source_url"],
        "krx_source_hash": projected["krx_source_hash"],
        "krx_request_id": projected["krx_request_id"],
        "natural_selection": True,
        "official_profile_binding": None,
        "phase105_canary_receipt_reused": False,
    }
    if set(lineage) != _LINEAGE_KEYS:
        raise AssertionError("natural lineage projection schema drift")
    return {
        "target_id": target_id,
        "company_name": projected["company_name"],
        "as_of_date": as_of_date,
        "archetype_id": projected["leading_archetype_id"],
        "latest_trading_snapshot_date": projected["krx_effective_date"],
        "natural_lineage": lineage,
        "natural_lineage_hash": stable_hash(lineage),
    }


def natural_current_candidates(
    *, live_root: str | Path, as_of_date: str
) -> tuple[Mapping[str, Any], ...]:
    raw_candidates, trigger_rows = load_current_live_selection_inputs(
        live_root,
        selection_as_of_date=as_of_date,
        issuer_business_profile_manifest=None,
    )
    projected = tuple(
        project_natural_current_candidate(
            row,
            trigger_rows=trigger_rows,
            as_of_date=as_of_date,
        )
        for row in raw_candidates
    )
    if len({str(row["target_id"]) for row in projected}) != len(projected):
        raise ValueError("natural Phase107 candidate target roster is not unique")
    return tuple(
        sorted(
            projected,
            key=lambda row: (
                -float(_mapping(row["natural_lineage"], context="lineage")["priority_score"]),
                str(row["target_id"]),
                str(_mapping(row["natural_lineage"], context="lineage")["planner_run_id"]),
            ),
        )
    )


def _terminal_artifacts(
    *, repo_root: Path, target_root: Path, candidate: Mapping[str, Any]
) -> Mapping[str, Any]:
    target_id = str(candidate["target_id"])
    company_name = str(candidate["company_name"])
    as_of_date = str(candidate["as_of_date"])
    archetype_id = str(candidate["archetype_id"])
    latest_trading_snapshot_date = str(candidate["latest_trading_snapshot_date"])
    if target_root.name != target_id or target_root.is_symlink() or not target_root.is_dir():
        raise ValueError("terminal target output path is not the natural candidate")
    if any(path.is_symlink() for path in target_root.rglob("*")):
        raise ValueError("terminal target output contains a symlink")
    required = (
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
    if any((target_root / name).is_symlink() or not (target_root / name).is_file() for name in required):
        raise ValueError("terminal target output lacks a required Researcher Mode leaf")

    target_manifest = _read_json(target_root / "target_run_manifest.json")
    score_vector = _read_json(target_root / "score_vector.json")
    atomic_stage = _read_json(target_root / "atomic_stage_decision.json")
    saturation = _read_json(target_root / "semantic_saturation_certificate.json")
    fact_audit = _read_json(target_root / "fact_extraction_audit.json")
    structured = _read_json(target_root / "current_structured_materialization.json")
    business = _read_json(target_root / "business_model_memo.json")
    red_team = _read_json(target_root / "red_team_research.json")
    supervisor = _read_json(target_root / "research_supervisor_review.json")
    provider_audit = _read_json(target_root / "research_provider_response_cache_audit.json")
    query_rows = _read_jsonl(target_root / "query_ledger.jsonl")
    document_rows = _read_jsonl(target_root / "documents.jsonl")
    evidence_rows = _read_jsonl(target_root / "evidence_facts.jsonl")
    counter_rows = _read_jsonl(target_root / "counterfacts.jsonl")
    material_gap_count = _material_gap_count(saturation=saturation, supervisor=supervisor)
    provider_accounting = _production_provider_accounting(provider_audit)
    output_tree_hash = canary_output_tree_hash(target_root, include_post_run_gold=False)
    query_ids = tuple(str(row.get("query_id") or "") for row in query_rows)
    document_ids = tuple(str(row.get("document_id") or "") for row in document_rows)
    accepted_fact_ids = tuple(
        str(row.get("fact_id") or "") for row in (*evidence_rows, *counter_rows)
    )
    if (
        not query_rows
        or not document_rows
        or not evidence_rows
        or not counter_rows
        or any(not value for value in query_ids)
        or len(set(query_ids)) != len(query_ids)
        or any(not value for value in document_ids)
        or len(set(document_ids)) != len(document_ids)
        or any(not value for value in accepted_fact_ids)
        or len(set(accepted_fact_ids)) != len(accepted_fact_ids)
        or material_gap_count != 0
    ):
        raise ValueError("terminal target lacks positive query/document/fact/counterfact lineage")
    if (
        target_manifest.get("status") != PHASE107_TERMINAL_RESEARCH_STATUS
        or target_manifest.get("target_id") != target_id
        or target_manifest.get("company_name") != company_name
        or target_manifest.get("as_of_date") != as_of_date
        or target_manifest.get("archetype_id") != archetype_id
        or target_manifest.get("latest_trading_snapshot_date") != latest_trading_snapshot_date
        or target_manifest.get("production_research_complete") is not True
        or target_manifest.get("gold_visibility") is not False
        or target_manifest.get("gold_comparison_timing") != "POST_RUN_ONLY"
        or target_manifest.get("completion_based_on_fixed_rounds") is not False
        or target_manifest.get("zero_search_result_treated_as_completion") is not False
        or target_manifest.get("transport_budget_treated_as_completion") is not False
        or target_manifest.get("output_tree_hash") != output_tree_hash
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
        or int(provider_accounting["provider_error_count"]) != 0
    ):
        raise ValueError("target output is not terminal, current, and provider-clean")

    decision_rows = _decision_rows(target_root)
    components = _component_receipts(target_root, decision_rows)
    judges = _judge_receipts(target_root)
    facts = _fact_receipts(
        target_root,
        components,
        as_of_date=as_of_date,
        target_id=target_id,
    )
    sources = _source_receipts(facts)
    anchors = _anchor_receipts(
        repo_root,
        archetype_id=archetype_id,
        components=components,
    )
    provider_calls = _provider_call_receipts(target_root)
    if len(components) != 7 or len(judges) != 21 or not facts or not sources or not provider_calls:
        raise ValueError("terminal target lacks the exact score-bearing receipt roster")
    provider_kinds = tuple(_provider_kind(row.get("provider_name")) for row in provider_calls)
    if (
        any(kind not in _ALLOWED_PROVIDER_KINDS for kind in provider_kinds)
        or _contains_local_provider_marker(provider_calls)
    ):
        raise ValueError("terminal receipt provider roster is not Codex-only")

    vector = {
        component_id: float(score_vector["component_score_vector"][component_id])
        for component_id in CANONICAL_COMPONENT_ORDER
    }
    maxima = {
        str(row["component_id"]): float(row["max_points"]) for row in components
    }
    total = round(sum(vector.values()), 6)
    declared_total = score_vector.get("total_points", score_vector.get("total_score"))
    if not _finite(declared_total) or abs(float(declared_total) - total) > 1e-9:
        raise ValueError("terminal component vector does not reproduce total score")
    receipt_id = "KDXDEEP-" + stable_hash(
        {
            "natural_lineage_hash": candidate["natural_lineage_hash"],
            "output_tree_hash": output_tree_hash,
            "target_id": target_id,
            "as_of_date": as_of_date,
        }
    )[:24]
    score = {
        "schema_version": PHASE107_DEEP_SCORE_SCHEMA,
        "receipt_id": receipt_id,
        "target_id": target_id,
        "company_name": company_name,
        "as_of_date": as_of_date,
        "latest_trading_snapshot_date": latest_trading_snapshot_date,
        "archetype_id": archetype_id,
        "score_scale": "FULL_E2R_100",
        "score_valid": True,
        "research_complete": True,
        "semantic_saturation_certified": True,
        "material_gap_count": 0,
        "provider_error_count": 0,
        "unauthorized_provider_call_count": 0,
        "local_provider_call_count": 0,
        "query_count": len(query_rows),
        "document_count": len(document_rows),
        "fact_count": len(evidence_rows) + len(counter_rows),
        "counterfact_count": len(counter_rows),
        "component_score_vector": vector,
        "component_max_vector": maxima,
        "total_score": total,
        "total_score_recomputed": total,
        "component_sum_matches_total": True,
        "canonical_stage": atomic_stage["canonical_stage"],
        "score_status": "COMPLETE",
        "stagecourt_status": "FINAL",
        "production_research_status": "COMPLETE",
        "gold_visibility": False,
        "score_or_stage_authority": False,
    }
    stage = dict(_stage_receipt(repo_root, target_root, score, receipt_id=receipt_id))
    if stage.get("canonical_stage") != atomic_stage.get("canonical_stage"):
        raise ValueError("StageCourt trace and atomic Stage disagree")
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
    return {
        "receipt_id": receipt_id,
        "output_tree_hash": output_tree_hash,
        "artifacts": artifacts,
        "provider_successful_call_count": int(provider_accounting["successful_call_count"]),
    }


def _encode(name: str, payload: Any) -> bytes:
    if name.endswith(".jsonl"):
        rows = _rows(payload, context=name)
        return b"".join(
            (
                json.dumps(
                    row,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                    allow_nan=False,
                )
                + "\n"
            ).encode("utf-8")
            for row in rows
        )
    return (
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
        + "\n"
    ).encode("utf-8")


def _write_private(parent_fd: int, name: str, encoded: bytes) -> None:
    descriptor = os.open(
        name,
        os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0),
        0o600,
        dir_fd=parent_fd,
    )
    try:
        view = memoryview(encoded)
        while view:
            view = view[os.write(descriptor, view) :]
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def _assert_pinned_directory(path: Path, descriptor: int) -> None:
    reopened = _open_existing_directory_no_symlinks(path)
    try:
        pinned = os.fstat(descriptor)
        current = os.fstat(reopened)
        if (pinned.st_dev, pinned.st_ino) != (current.st_dev, current.st_ino):
            raise ValueError("natural deep receipt parent changed during publication")
    finally:
        os.close(reopened)


def _manifest_for_staging(
    *,
    staging: Path,
    candidate: Mapping[str, Any],
    built: Mapping[str, Any],
) -> Mapping[str, Any]:
    artifacts = _mapping(built["artifacts"], context="deep receipt artifacts")
    score = _mapping(artifacts["score_receipt.json"], context="score receipt")
    content_index = receipt_content_index(staging)
    body = {
        "schema_version": PHASE107_DEEP_RECEIPT_SCHEMA,
        "status": PHASE107_DEEP_RECEIPT_PASS,
        "receipt_id": built["receipt_id"],
        "target_id": candidate["target_id"],
        "company_name": candidate["company_name"],
        "as_of_date": candidate["as_of_date"],
        "latest_trading_snapshot_date": candidate["latest_trading_snapshot_date"],
        "archetype_id": candidate["archetype_id"],
        "natural_lineage": dict(_mapping(candidate["natural_lineage"], context="natural lineage")),
        "natural_lineage_hash": candidate["natural_lineage_hash"],
        "output_tree_hash": built["output_tree_hash"],
        "artifact_names": list(REQUIRED_TARGET_FILES),
        "tracked_receipt_content_index": list(content_index),
        "tracked_receipt_tree_hash": receipt_content_tree_hash(staging),
        "component_count": len(_rows(artifacts["component_decisions.jsonl"], context="components")),
        "judge_decision_count": len(_rows(artifacts["judge_decisions.jsonl"], context="judges")),
        "scoring_fact_count": len(_rows(artifacts["scoring_facts.jsonl"], context="facts")),
        "source_count": len(_rows(artifacts["source_manifest.jsonl"], context="sources")),
        "anchor_count": len(_rows(artifacts["anchor_manifest.jsonl"], context="anchors")),
        "provider_call_count": len(_rows(artifacts["provider_calls.jsonl"], context="provider calls")),
        "query_count": score["query_count"],
        "document_count": score["document_count"],
        "fact_count": score["fact_count"],
        "counterfact_count": score["counterfact_count"],
        "material_gap_count": 0,
        "provider_error_count": 0,
        "unauthorized_provider_call_count": 0,
        "local_provider_call_count": 0,
        "score_valid": True,
        "canonical_stage": score["canonical_stage"],
        "gold_visibility": False,
        "score_or_stage_authority": False,
        "production_readiness_authority": False,
    }
    return {**body, "receipt_payload_hash": stable_hash(body)}


def export_current_krx_deep_receipt(
    *,
    repo_root: str | Path,
    target_root: str | Path,
    destination_root: str | Path,
    candidate: Mapping[str, Any],
) -> Path:
    """Build, offline-verify, and atomically publish one natural deep receipt."""

    repo = Path(repo_root).resolve()
    built = _terminal_artifacts(
        repo_root=repo,
        target_root=Path(target_root).absolute(),
        candidate=candidate,
    )
    root = Path(destination_root).absolute()
    root_fd = _open_or_create_directory_no_symlinks(root)
    name = str(candidate["target_id"])
    temporary_name = f".{name}.{secrets.token_hex(16)}.tmp"
    temporary_fd = -1
    renamed = False
    published_report: Mapping[str, Any] | None = None
    try:
        _assert_pinned_directory(root, root_fd)
        try:
            os.stat(name, dir_fd=root_fd, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise ValueError("natural deep receipt destination already exists")
        os.mkdir(temporary_name, mode=0o700, dir_fd=root_fd)
        temporary_fd = os.open(
            temporary_name,
            os.O_RDONLY | os.O_DIRECTORY | getattr(os, "O_NOFOLLOW", 0),
            dir_fd=root_fd,
        )
        staging = root / temporary_name
        artifacts = _mapping(built["artifacts"], context="deep receipt artifacts")
        for artifact_name in REQUIRED_TARGET_FILES:
            _write_private(temporary_fd, artifact_name, _encode(artifact_name, artifacts[artifact_name]))
        manifest = _manifest_for_staging(staging=staging, candidate=candidate, built=built)
        _write_private(temporary_fd, "receipt_manifest.json", _encode("receipt_manifest.json", manifest))
        os.fsync(temporary_fd)
        _assert_pinned_directory(root, root_fd)
        report = verify_current_krx_deep_receipt(
            staging,
            repo_root=repo,
            expected_candidate=candidate,
            _allow_staging_name=True,
        )
        if report.get("status") != VERIFICATION_PASS or int(report.get("critical_count") or 0) != 0:
            raise ValueError(f"staged natural deep receipt did not verify: {report}")
        _assert_pinned_directory(root, root_fd)
        os.rename(temporary_name, name, src_dir_fd=root_fd, dst_dir_fd=root_fd)
        renamed = True
        os.fsync(root_fd)
        _assert_pinned_directory(root, root_fd)
        published_report = verify_current_krx_deep_receipt(
            root / name,
            repo_root=repo,
            expected_candidate=candidate,
        )
        if published_report.get("status") != VERIFICATION_PASS:
            raise ValueError("published natural deep receipt did not reverify")
        _assert_pinned_directory(root, root_fd)
    finally:
        if temporary_fd >= 0:
            os.close(temporary_fd)
        if not renamed:
            staging = root / temporary_name
            try:
                _assert_pinned_directory(root, root_fd)
            except (OSError, ValueError):
                pass
            else:
                if staging.exists() and not staging.is_symlink():
                    shutil.rmtree(staging)
        os.close(root_fd)
    destination = root / name
    if published_report is None:
        raise ValueError("natural deep receipt publication did not commit")
    return destination


def _decode_json(encoded: bytes, *, context: str) -> Mapping[str, Any]:
    try:
        return _mapping(json.loads(encoded.decode("utf-8")), context=context)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{context} is not valid JSON") from exc


def _decode_jsonl(encoded: bytes, *, context: str) -> tuple[Mapping[str, Any], ...]:
    try:
        return tuple(
            _mapping(json.loads(line), context=f"{context} row")
            for line in encoded.decode("utf-8").splitlines()
            if line.strip()
        )
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{context} is not valid JSONL") from exc


def _load_receipt_tree(path: Path) -> tuple[Mapping[str, Any], Mapping[str, Any]]:
    root_fd = _open_existing_directory_no_symlinks(path)
    try:
        expected = {"receipt_manifest.json", *REQUIRED_TARGET_FILES}
        if set(os.listdir(root_fd)) != expected:
            raise ValueError("natural deep receipt has an unexpected or missing leaf")
        manifest = _decode_json(
            _read_regular_from_directory(root_fd, "receipt_manifest.json")[0],
            context="receipt manifest",
        )
        artifacts: dict[str, Any] = {}
        for name in REQUIRED_TARGET_FILES:
            encoded, _ = _read_regular_from_directory(root_fd, name)
            artifacts[name] = (
                _decode_jsonl(encoded, context=name)
                if name.endswith(".jsonl")
                else _decode_json(encoded, context=name)
            )
    finally:
        os.close(root_fd)
    return manifest, artifacts


def _validate_lineage(
    manifest: Mapping[str, Any], expected_candidate: Mapping[str, Any] | None
) -> None:
    lineage = _mapping(manifest.get("natural_lineage"), context="natural lineage")
    if (
        set(lineage) != _LINEAGE_KEYS
        or lineage.get("planner_terminal_status") != "COMPLETE"
        or lineage.get("natural_selection") is not True
        or lineage.get("official_profile_binding") is not None
        or lineage.get("phase105_canary_receipt_reused") is not False
        or not lineage.get("trigger_signal_ids")
        or not lineage.get("trigger_types")
        or not lineage.get("source_refs")
        or not lineage.get("event_source_refs")
        or not lineage.get("direct_current_supporting_fact_ids")
        or not lineage.get("recipe_ids")
        or not lineage.get("available_source_families")
        or len(tuple(lineage.get("trigger_signal_ids") or ()))
        != len(set(lineage.get("trigger_signal_ids") or ()))
        or len(tuple(lineage.get("source_refs") or ()))
        != len(set(lineage.get("source_refs") or ()))
        or any(
            len(tuple(lineage.get(field) or ()))
            != len(set(lineage.get(field) or ()))
            for field in (
                "trigger_types",
                "event_source_refs",
                "direct_current_supporting_fact_ids",
                "recipe_ids",
                "available_source_families",
            )
        )
        or any(
            not str(lineage.get(field) or "").strip()
            for field in (
                "planner_run_id",
                "blind_input_id",
                "depth_decision_id",
                "candidate_event_id",
                "leading_archetype_id",
                "krx_source_url",
                "krx_request_id",
            )
        )
        or lineage.get("leading_archetype_id") != manifest.get("archetype_id")
        or not _finite(lineage.get("priority_score"))
        or any(
            _HEX64_RE.fullmatch(str(lineage.get(field) or "")) is None
            for field in (
                "plan_hash",
                "depth_decision_hash",
                "candidate_event_hash",
                "trigger_lineage_hash",
                "krx_source_hash",
                "event_summary_hash",
            )
        )
        or manifest.get("natural_lineage_hash") != stable_hash(lineage)
    ):
        raise ValueError("natural trigger/depth/planner lineage is not exact")
    if expected_candidate is not None:
        expected = _mapping(expected_candidate, context="expected natural candidate")
        for field in (
            "target_id",
            "company_name",
            "as_of_date",
            "latest_trading_snapshot_date",
            "archetype_id",
            "natural_lineage_hash",
        ):
            if manifest.get(field) != expected.get(field):
                raise ValueError(f"deep receipt differs from current natural candidate: {field}")
        if dict(lineage) != dict(_mapping(expected.get("natural_lineage"), context="expected lineage")):
            raise ValueError("deep receipt natural lineage differs from current live leaves")


def _validate_artifacts(
    *,
    repo_root: Path,
    manifest: Mapping[str, Any],
    artifacts: Mapping[str, Any],
) -> Mapping[str, Any]:
    score = _mapping(artifacts["score_receipt.json"], context="score receipt")
    stage = _mapping(artifacts["stagecourt_receipt.json"], context="StageCourt receipt")
    components = _rows(artifacts["component_decisions.jsonl"], context="components")
    facts = _rows(artifacts["scoring_facts.jsonl"], context="facts")
    judges = _rows(artifacts["judge_decisions.jsonl"], context="judges")
    sources = _rows(artifacts["source_manifest.jsonl"], context="sources")
    anchors = _rows(artifacts["anchor_manifest.jsonl"], context="anchors")
    provider_calls = _rows(artifacts["provider_calls.jsonl"], context="provider calls")
    if set(score) != _SCORE_KEYS or score.get("schema_version") != PHASE107_DEEP_SCORE_SCHEMA:
        raise ValueError("natural deep score receipt schema is not exact")
    if set(stage) != STAGECOURT_RECEIPT_KEYS or stage.get("schema_version") != STAGECOURT_RECEIPT_SCHEMA:
        raise ValueError("natural deep StageCourt receipt schema is not exact")
    schema_contracts = (
        (components, COMPONENT_RECEIPT_KEYS, "e2r_v6_component_decision_receipt_v1"),
        (facts, SCORING_FACT_RECEIPT_KEYS, "e2r_v6_scoring_fact_receipt_v1"),
        (judges, JUDGE_RECEIPT_KEYS, "e2r_v6_judge_decision_receipt_v1"),
        (sources, SOURCE_RECEIPT_KEYS, "e2r_v6_source_manifest_row_v1"),
        (anchors, ANCHOR_RECEIPT_KEYS, "e2r_v6_anchor_manifest_row_v1"),
    )
    for rows, keys, schema in schema_contracts:
        if any(set(row) != keys or row.get("schema_version") != schema for row in rows):
            raise ValueError(f"tracked-style receipt row schema mismatch: {schema}")
    for call in provider_calls:
        expected_keys = (
            PROVIDER_CALL_FACT_KEYS
            if call.get("call_scope") == "FACT_EXTRACTION"
            else PROVIDER_CALL_FULL_RUN_KEYS
            if call.get("call_scope") == "FULL_RESEARCH_INVOCATION_AUDIT"
            else PROVIDER_CALL_COMMON_KEYS
        )
        if set(call) != expected_keys or call.get("schema_version") != "e2r_v6_provider_call_receipt_v1":
            raise ValueError("provider call receipt schema is not exact")

    target_id = str(manifest["target_id"])
    as_of_date = str(manifest["as_of_date"])
    archetype_id = str(manifest["archetype_id"])
    cutoff = date.fromisoformat(as_of_date)
    if (
        set(score.get("component_score_vector") or ()) != set(CANONICAL_COMPONENT_ORDER)
        or set(score.get("component_max_vector") or ()) != set(CANONICAL_COMPONENT_ORDER)
        or len(components) != 7
        or tuple(str(row.get("component_id") or "") for row in components) != tuple(CANONICAL_COMPONENT_ORDER)
        or len(judges) != 21
        or not facts
        or not sources
        or not anchors
        or not provider_calls
    ):
        raise ValueError("natural deep receipt lacks 7 components/21 judges/source-backed facts")
    identity = {
        "receipt_id": manifest["receipt_id"],
        "target_id": target_id,
        "company_name": manifest["company_name"],
        "as_of_date": as_of_date,
        "latest_trading_snapshot_date": manifest["latest_trading_snapshot_date"],
        "archetype_id": archetype_id,
    }
    if any(score.get(key) != value for key, value in identity.items()):
        raise ValueError("score receipt identity differs from its natural manifest")
    vector = _mapping(score["component_score_vector"], context="component vector")
    maxima = _mapping(score["component_max_vector"], context="component maxima")
    tracked_maxima = _tracked_component_maxima(repo_root=repo_root, archetype_id=archetype_id)
    if any(
        not _finite(vector.get(component_id))
        or not _finite(maxima.get(component_id))
        or float(maxima[component_id]) != float(tracked_maxima[component_id])
        or not 0.0 <= float(vector[component_id]) <= float(maxima[component_id])
        for component_id in CANONICAL_COMPONENT_ORDER
    ):
        raise ValueError("component vectors are not bound to tracked current maxima")
    total = round(sum(float(vector[key]) for key in CANONICAL_COMPONENT_ORDER), 6)
    if (
        not _finite(score.get("total_score"))
        or not _finite(score.get("total_score_recomputed"))
        or abs(float(score["total_score"]) - total) > 1e-9
        or abs(float(score["total_score_recomputed"]) - total) > 1e-9
        or score.get("component_sum_matches_total") is not True
        or score.get("score_valid") is not True
        or score.get("research_complete") is not True
        or score.get("semantic_saturation_certified") is not True
        or score.get("material_gap_count") != 0
        or score.get("provider_error_count") != 0
        or score.get("unauthorized_provider_call_count") != 0
        or score.get("local_provider_call_count") != 0
        or any(
            isinstance(score.get(field), bool)
            or not isinstance(score.get(field), int)
            or int(score[field]) <= 0
            for field in (
                "query_count",
                "document_count",
                "fact_count",
                "counterfact_count",
            )
        )
        or int(score["fact_count"]) < len(facts)
        or int(score["counterfact_count"]) > int(score["fact_count"])
        or score.get("score_status") != "COMPLETE"
        or score.get("stagecourt_status") != "FINAL"
        or score.get("production_research_status") != "COMPLETE"
        or score.get("gold_visibility") is not False
        or score.get("score_or_stage_authority") is not False
        or score.get("canonical_stage") not in _CANONICAL_STAGES
    ):
        raise ValueError("natural deep score is not a complete Gold-free result")

    component_by_id = _index(components, "component_id", context="component")
    judge_by_id = _index(judges, "judge_decision_id", context="judge")
    expected_fact_components: dict[str, set[str]] = defaultdict(set)
    expected_fact_roles: dict[str, set[str]] = defaultdict(set)
    expected_anchor_components: dict[str, set[str]] = defaultdict(set)
    for component_id in CANONICAL_COMPONENT_ORDER:
        component = component_by_id[component_id]
        component_judges = tuple(row for row in judges if row.get("component_id") == component_id)
        if (
            {str(row.get("role") or "") for row in component_judges} != _JUDGE_ROLES
            or len(component_judges) != 3
            or set(str(value) for value in component.get("judge_decision_ids") or ())
            != {str(row["judge_decision_id"]) for row in component_judges}
            or float(component.get("max_points")) != float(maxima[component_id])
            or float(component.get("final_points")) != float(vector[component_id])
        ):
            raise ValueError(f"component/judge score lineage mismatch: {component_id}")
        formula_failures: list[Mapping[str, Any]] = []
        _verify_component_formula(component, component_judges, formula_failures)
        if formula_failures:
            raise ValueError(f"component deterministic formula mismatch: {component_id}")
        judge_support = {
            str(value)
            for row in component_judges
            for value in row.get("support_fact_ids") or ()
        }
        judge_counter = {
            str(value)
            for row in component_judges
            for value in row.get("counter_fact_ids") or ()
        }
        judge_anchors = {
            str(value)
            for row in component_judges
            for value in row.get("anchor_ids") or ()
        }
        if (
            judge_support
            != {str(value) for value in component.get("support_fact_ids") or ()}
            or judge_counter
            != {str(value) for value in component.get("counter_fact_ids") or ()}
            or judge_anchors
            != {str(value) for value in component.get("historical_anchor_ids") or ()}
        ):
            raise ValueError(f"component evidence is not the exact judge union: {component_id}")
        for field, role in (
            ("support_fact_ids", "SUPPORT"),
            ("counter_fact_ids", "COUNTER"),
            ("resolution_fact_ids", "RESOLUTION"),
        ):
            for fact_id in component.get(field) or ():
                expected_fact_components[str(fact_id)].add(component_id)
                expected_fact_roles[str(fact_id)].add(role)
        for anchor_id in component.get("historical_anchor_ids") or ():
            expected_anchor_components[str(anchor_id)].add(component_id)

    fact_by_id = _index(facts, "fact_id", context="fact")
    source_by_id = _index(sources, "source_document_id", context="source")
    if set(fact_by_id) != set(expected_fact_components):
        raise ValueError("score-bearing fact roster is not exact and bidirectional")
    expected_source_facts: dict[str, set[str]] = defaultdict(set)
    for fact_id, fact in fact_by_id.items():
        source_id = str(fact.get("source_document_id") or "")
        exact_quote = str(fact.get("exact_quote") or "")
        if (
            fact.get("target_id") != target_id
            or fact.get("as_of_date") != as_of_date
            or set(fact.get("component_ids") or ()) != expected_fact_components[fact_id]
            or set(fact.get("fact_roles") or ()) != expected_fact_roles[fact_id]
            or fact.get("fact_role")
            != next(
                (
                    role
                    for role in ("SUPPORT", "COUNTER", "RESOLUTION", "HARD_BREAK")
                    if role in expected_fact_roles[fact_id]
                ),
                None,
            )
            or fact.get("direct_point_input")
            is not (fact.get("fact_role") in {"SUPPORT", "COUNTER"})
            or not set(
                str(value) for value in fact.get("allowed_component_ids") or ()
            )
            or not expected_fact_components[fact_id]
            <= set(
                str(value) for value in fact.get("allowed_component_ids") or ()
            )
            or fact.get("claim_scope_hash")
            != stable_hash(
                {
                    "primary_claim_id": fact.get("primary_claim_id"),
                    "allowed_component_ids": list(
                        fact.get("allowed_component_ids") or ()
                    ),
                    "scope_business_segment": fact.get(
                        "scope_business_segment"
                    ),
                    "scope_product_family": fact.get("scope_product_family"),
                    "scope_technology_family": fact.get(
                        "scope_technology_family"
                    ),
                    "scope_transaction_type": fact.get(
                        "scope_transaction_type"
                    ),
                    "scope_economic_mechanism": fact.get(
                        "scope_economic_mechanism"
                    ),
                    "scope_confidence": fact.get("scope_confidence"),
                }
            )
            or str(fact.get("primary_claim_id") or "")
            not in {str(value) for value in fact.get("claim_ids") or ()}
            or fact.get("current_score_eligible") is not True
            or fact.get("current_score_eligibility_basis")
            != "FINAL_DECISION_REFERENCE_AND_AS_OF_VALIDATED"
            or fact.get("gold_fact") is not False
            or fact.get("issuer_scoped") is not True
            or not exact_quote
            or fact.get("exact_quote_hash") != _sha256_text(exact_quote)
            or fact.get("quote_excerpt") != _excerpt(exact_quote)
            or fact.get("quote_excerpt_hash")
            != _sha256_text(fact.get("quote_excerpt"))
            or _HEX64_RE.fullmatch(str(fact.get("document_content_hash") or "")) is None
            or source_id not in source_by_id
            or _provider_kind(fact.get("extraction_provider_name")) not in _ALLOWED_PROVIDER_KINDS
        ):
            raise ValueError(f"score-bearing fact/source lineage mismatch: {fact_id}")
        for field in ("published_at", "available_at"):
            if date.fromisoformat(str(fact.get(field) or "")[:10]) > cutoff:
                raise ValueError(f"future fact date in receipt: {fact_id}")
        expected_source_facts[source_id].add(fact_id)
    if set(source_by_id) != set(expected_source_facts):
        raise ValueError("source manifest roster is not exact")
    for source_id, source in source_by_id.items():
        fact_ids = expected_source_facts[source_id]
        if (
            set((source.get("fact_document_hashes") or {}).keys()) != fact_ids
            or set((source.get("fact_exact_quote_hashes") or {}).keys()) != fact_ids
        ):
            raise ValueError(f"source/fact hashes are not bidirectional: {source_id}")
        for fact_id in fact_ids:
            fact = fact_by_id[fact_id]
            if (
                (source.get("fact_document_hashes") or {}).get(fact_id) != fact.get("document_content_hash")
                or (source.get("fact_exact_quote_hashes") or {}).get(fact_id) != fact.get("exact_quote_hash")
                or any(
                    source.get(field) != fact.get(field)
                    for field in (
                        "source_url",
                        "source_title",
                        "source_publisher",
                        "source_tier",
                        "source_family",
                        "published_at",
                        "available_at",
                        "document_content_hash",
                        "source_independence_group",
                    )
                )
            ):
                raise ValueError(f"source/fact content hash mismatch: {fact_id}")

    anchor_by_id = _index(anchors, "anchor_id", context="anchor")
    tracked_anchors = _index(
        _tracked_historical_anchors(repo_root=repo_root, archetype_id=archetype_id),
        "anchor_id",
        context="tracked anchor",
    )
    if set(anchor_by_id) != set(expected_anchor_components):
        raise ValueError("anchor roster is not exact and bidirectional")
    for anchor_id, anchor in anchor_by_id.items():
        payload = _mapping(anchor.get("normalized_anchor_payload"), context="anchor payload")
        if (
            anchor.get("anchor_payload_hash") != stable_hash(payload)
            or tracked_anchors.get(anchor_id) != payload
            or expected_anchor_components[anchor_id] != {str(anchor.get("component_id") or "")}
            or anchor.get("archetype_id") != archetype_id
        ):
            raise ValueError(f"anchor is not bound to tracked config: {anchor_id}")

    if _contains_local_provider_marker(provider_calls):
        raise ValueError("local provider marker appears in deep receipt")
    full_runs = tuple(row for row in provider_calls if row.get("call_scope") == "FULL_RESEARCH_INVOCATION_AUDIT")
    if len(full_runs) != 1:
        raise ValueError("deep receipt requires one full-run provider audit")
    full = full_runs[0]
    if (
        _provider_kind(full.get("provider_name")) != "COLLABORATION_CODEX"
        or full.get("provider_kind") != "COLLABORATION_CODEX"
        or full.get("status") != "COLLABORATION_PROVIDER_JOURNAL_ACTIVE"
        or int(full.get("provider_attempt_count") or 0) <= 0
        or full.get("successful_call_count") != full.get("provider_attempt_count")
        or full.get("transport_call_count") != full.get("provider_attempt_count")
        or full.get("provider_error_count") != 0
    ):
        raise ValueError("full-run Collaboration provider audit is not clean")
    call_by_id = _index(provider_calls, "provider_call_id", context="provider call")
    for call in provider_calls:
        if (
            _provider_kind(call.get("provider_name")) not in _ALLOWED_PROVIDER_KINDS
            or call.get("provider_kind") != _provider_kind(call.get("provider_name"))
            or call.get("score_or_stage_authority") is not False
        ):
            raise ValueError("provider call is unauthorized or claims score authority")
        if call.get("call_scope") == "FACT_EXTRACTION" and (
            call.get("status") not in {"COMPLETE", "SUCCESS"}
            or not _embedded_fact_journal_call_is_exact(call)
        ):
            raise ValueError("fact extraction provider journal receipt is not exact")
    judge_call_ids = {
        str(row.get("provider_call_id") or "") for row in judges
    }
    component_call_ids = {
        str(row.get("provider_call_id") or "")
        for row in provider_calls
        if row.get("call_scope") == "COMPONENT_JUDGE"
    }
    if component_call_ids != judge_call_ids:
        raise ValueError("component judge provider-call roster is not exact")
    for judge_id, judge in judge_by_id.items():
        call = call_by_id.get(str(judge.get("provider_call_id") or ""))
        if (
            call is None
            or call.get("call_scope") != "COMPONENT_JUDGE"
            or call.get("status") != "SUCCESS"
            or call.get("provider_name") != judge.get("provider_name")
            or call.get("prompt_hash") != judge.get("prompt_hash")
            or call.get("response_hash") != judge.get("response_hash")
            or judge.get("provider_route") != PROVIDER_ROUTE
            or judge.get("score_or_stage_authority") is not False
        ):
            raise ValueError(f"judge provider call linkage mismatch: {judge_id}")
    fact_lineages: dict[tuple[str, str, str], set[str]] = defaultdict(set)
    for call in provider_calls:
        if call.get("call_scope") != "FACT_EXTRACTION":
            continue
        lineage = (
            str(call.get("provider_name") or ""),
            str(call.get("prompt_hash") or ""),
            str(call.get("response_hash") or ""),
        )
        fact_lineages[lineage].update(
            str(value) for value in call.get("fact_scope_attestation_hashes") or ()
        )
    for fact_id, fact in fact_by_id.items():
        lineage = (
            str(fact.get("extraction_provider_name") or ""),
            str(fact.get("provider_prompt_hash") or ""),
            str(fact.get("provider_response_hash") or ""),
        )
        if (
            lineage not in fact_lineages
            or _fact_scope_attestation_hash(fact) not in fact_lineages[lineage]
        ):
            raise ValueError(f"fact provider call linkage mismatch: {fact_id}")

    if (
        stage.get("target_id") != target_id
        or stage.get("score_receipt_id") != manifest.get("receipt_id")
        or stage.get("component_score_vector_hash") != stable_hash(vector)
        or not _finite(stage.get("total_score"))
        or abs(float(stage["total_score"]) - total) > 1e-9
        or stage.get("canonical_stage") != score.get("canonical_stage")
        or stage.get("decision_status") != "FINAL"
        or stage.get("score_valid") is not True
        or stage.get("stagecourt_rule_hash") != stagecourt_rule_hash(repo_root)
    ):
        raise ValueError("StageCourt receipt is not bound to the deterministic score")
    if _recompute_stage(score, {**stage, "as_of_date": as_of_date}) != score.get("canonical_stage"):
        raise ValueError("canonical Stage does not recompute from tracked rules")
    return {
        "component_count": len(components),
        "judge_decision_count": len(judges),
        "scoring_fact_count": len(facts),
        "source_count": len(sources),
        "anchor_count": len(anchors),
        "provider_call_count": len(provider_calls),
        "total_score_recomputed": total,
        "canonical_stage_recomputed": score["canonical_stage"],
    }


def verify_current_krx_deep_receipt(
    target_root: str | Path,
    *,
    repo_root: str | Path | None = None,
    expected_candidate: Mapping[str, Any] | None = None,
    _allow_staging_name: bool = False,
) -> Mapping[str, Any]:
    """Offline-verify one natural deep receipt without the production output."""

    path = Path(target_root).absolute()
    target_id = path.name
    failures: list[Mapping[str, Any]] = []
    metrics: Mapping[str, Any] = {}
    try:
        repo = Path(repo_root).resolve() if repo_root is not None else canonical_repository_root()
        manifest, artifacts = _load_receipt_tree(path)
        target_id = str(manifest.get("target_id") or target_id)
        path_identity_matches = path.name == target_id or bool(
            _allow_staging_name
            and path.name.startswith(f".{target_id}.")
            and path.name.endswith(".tmp")
        )
        if (
            set(manifest) != _MANIFEST_KEYS
            or manifest.get("schema_version") != PHASE107_DEEP_RECEIPT_SCHEMA
            or manifest.get("status") != PHASE107_DEEP_RECEIPT_PASS
            or not path_identity_matches
            or _TARGET_RE.fullmatch(target_id) is None
            or manifest.get("artifact_names") != list(REQUIRED_TARGET_FILES)
            or _HEX64_RE.fullmatch(str(manifest.get("output_tree_hash") or "")) is None
            or manifest.get("receipt_id")
            != "KDXDEEP-"
            + stable_hash(
                {
                    "natural_lineage_hash": manifest.get("natural_lineage_hash"),
                    "output_tree_hash": manifest.get("output_tree_hash"),
                    "target_id": manifest.get("target_id"),
                    "as_of_date": manifest.get("as_of_date"),
                }
            )[:24]
            or date.fromisoformat(str(manifest.get("latest_trading_snapshot_date") or ""))
            > date.fromisoformat(str(manifest.get("as_of_date") or ""))
            or manifest.get("gold_visibility") is not False
            or manifest.get("score_or_stage_authority") is not False
            or manifest.get("production_readiness_authority") is not False
        ):
            raise ValueError("natural deep receipt manifest schema or authority is invalid")
        body = {key: value for key, value in manifest.items() if key != "receipt_payload_hash"}
        if manifest.get("receipt_payload_hash") != stable_hash(body):
            raise ValueError("natural deep receipt manifest payload hash mismatch")
        _validate_lineage(manifest, expected_candidate)
        actual_index = receipt_content_index(path)
        if (
            tuple(manifest.get("tracked_receipt_content_index") or ()) != actual_index
            or manifest.get("tracked_receipt_tree_hash") != receipt_content_tree_hash(path)
        ):
            raise ValueError("natural deep receipt raw content hash mismatch")
        metrics = _validate_artifacts(repo_root=repo, manifest=manifest, artifacts=artifacts)
        count_fields = {
            "component_count": "component_count",
            "judge_decision_count": "judge_decision_count",
            "scoring_fact_count": "scoring_fact_count",
            "source_count": "source_count",
            "anchor_count": "anchor_count",
            "provider_call_count": "provider_call_count",
        }
        if any(manifest.get(field) != metrics.get(metric) for field, metric in count_fields.items()):
            raise ValueError("natural deep receipt manifest counts do not recompute")
        score = _mapping(artifacts["score_receipt.json"], context="score receipt")
        if any(
            manifest.get(field) != score.get(field)
            for field in (
                "query_count",
                "document_count",
                "fact_count",
                "counterfact_count",
                "material_gap_count",
                "provider_error_count",
                "unauthorized_provider_call_count",
                "local_provider_call_count",
                "score_valid",
                "canonical_stage",
            )
        ):
            raise ValueError("natural deep receipt manifest and score disagree")
    except (OSError, TypeError, ValueError, KeyError, json.JSONDecodeError) as exc:
        failures.append(
            {
                "code": "CURRENT_KRX_DEEP_RECEIPT_VERIFICATION_FAILED",
                "detail": f"{type(exc).__name__}:{' '.join(str(exc).split())}",
            }
        )
    return {
        "schema_version": VERIFICATION_SCHEMA,
        "status": VERIFICATION_PASS if not failures else VERIFICATION_FAIL,
        "target_id": target_id,
        "critical_count": len(failures),
        "critical_count_sum": len(failures),
        "failures": failures,
        "metrics": dict(metrics),
        "offline": True,
        "gold_visibility": False,
        "score_or_stage_authority": False,
    }


def validate_current_krx_deep_receipt_root(
    *,
    live_root: str | Path,
    deep_receipt_root: str | Path,
    as_of_date: str,
    repo_root: str | Path | None = None,
) -> Mapping[str, Any]:
    """Revalidate the deterministic natural target and its canonical receipt."""

    failures: list[Mapping[str, Any]] = []
    reports: list[Mapping[str, Any]] = []
    selected_target_id: str | None = None
    try:
        candidates = natural_current_candidates(live_root=live_root, as_of_date=as_of_date)
        if not candidates:
            raise ValueError("no natural COMPLETE current planner candidate is available")
        candidate = candidates[0]
        selected_target_id = str(candidate["target_id"])
        candidate_by_target = {
            str(row["target_id"]): row for row in candidates
        }
        root = Path(deep_receipt_root).absolute()
        if root.is_symlink() or not root.is_dir():
            raise ValueError("natural deep receipt root is unavailable or unsafe")
        children = tuple(sorted(root.iterdir(), key=lambda path: path.name))
        if any(not path.is_dir() or path.is_symlink() for path in children):
            raise ValueError("natural deep receipt root contains an unsafe entry")
        if not children:
            raise ValueError("natural deep receipt root is empty")
        for target in children:
            expected = candidate_by_target.get(target.name)
            if expected is None:
                raise ValueError("deep receipt target is absent from current natural planner roster")
            report = verify_current_krx_deep_receipt(
                target,
                repo_root=repo_root,
                expected_candidate=expected,
            )
            reports.append(report)
            if report.get("status") != VERIFICATION_PASS or int(report.get("critical_count") or 0) != 0:
                raise ValueError("a current natural deep receipt did not verify")
        if selected_target_id not in {path.name for path in children}:
            raise ValueError("highest-priority natural deep receipt is missing")
        if not any(
            str((report.get("metrics") or {}).get("canonical_stage_recomputed") or "")
            not in {"", "0"}
            and _finite((report.get("metrics") or {}).get("total_score_recomputed"))
            and abs(float((report.get("metrics") or {})["total_score_recomputed"]))
            > 1e-12
            for report in reports
        ):
            raise ValueError(
                "natural deep receipts are complete but still all Stage 0 or zero-score"
            )
    except (OSError, TypeError, ValueError, KeyError, json.JSONDecodeError) as exc:
        failures.append(
            {
                "code": "CURRENT_KRX_DEEP_RECEIPT_ROOT_INVALID",
                "detail": f"{type(exc).__name__}:{' '.join(str(exc).split())}",
            }
        )
    return {
        "schema_version": VERIFICATION_SCHEMA,
        "status": VERIFICATION_PASS if not failures else VERIFICATION_FAIL,
        "selected_target_id": selected_target_id,
        "critical_count": len(failures),
        "critical_count_sum": len(failures),
        "reports": reports,
        "failures": failures,
        "offline": True,
        "gold_visibility": False,
        "score_or_stage_authority": False,
    }


def _default_checkpoint_runner(_candidate: Mapping[str, Any]) -> Any:
    return CurrentResearcherModeTargetRunner(
        provider=CollaborationCodexResearcherProvider.default()
    )


def _pending_request_ids(target_root: Path) -> tuple[str, ...]:
    request_root = target_root / "collaboration_codex_subagent_provider" / "requests"
    response_root = target_root / "collaboration_codex_subagent_provider" / "responses"
    if not request_root.is_dir() or request_root.is_symlink():
        return ()
    result: list[str] = []
    for path in sorted(request_root.glob("*.json")):
        if path.is_symlink() or not path.is_file():
            raise ValueError("Collaboration request journal contains an unsafe leaf")
        try:
            request = validate_collaboration_request(
                _mapping(
                    json.loads(path.read_text(encoding="utf-8")),
                    context="Collaboration request",
                )
            )
        except (OSError, UnicodeError, json.JSONDecodeError, TypeError, ValueError) as exc:
            raise ValueError("Collaboration request journal is invalid") from exc
        request_id = str(request["request_id"])
        if path.name != f"{request_id}.json":
            raise ValueError("Collaboration request path identity is invalid")
        response = response_root / f"{request_id}.json"
        if response.is_symlink():
            raise ValueError("Collaboration response journal contains a symlink")
        if not response.is_file():
            result.append(request_id)
    return tuple(result)


def _pending_result(
    *, candidate: Mapping[str, Any] | None, detail: str, target_root: Path | None = None
) -> Mapping[str, Any]:
    request_ids = _pending_request_ids(target_root) if target_root is not None else ()
    marker = "COLLABORATION_RESPONSE_PENDING" if request_ids else "SOURCE_PENDING"
    return {
        "schema_version": PHASE107_DEEP_RUN_SCHEMA,
        "status": PHASE107_DEEP_RUN_PENDING,
        "active_target_id": candidate.get("target_id") if candidate else None,
        "active_archetype_id": candidate.get("archetype_id") if candidate else None,
        "natural_lineage_hash": candidate.get("natural_lineage_hash") if candidate else None,
        "pending_kind": detail,
        "pending_requests": list(request_ids),
        "external_wait_marker": marker,
        "blockers": [marker],
        "completion_based_on_fixed_retries": False,
        "gold_visibility": False,
        "gold_call_count": 0,
        "local_provider_call_count": 0,
        "score_or_stage_authority": False,
        "production_readiness_authority": False,
    }


class V6CurrentKrxDeepReceiptRunner:
    """Advance the highest-priority natural COMPLETE candidate by one checkpoint."""

    def __init__(
        self, *, checkpoint_runner_factory: CheckpointRunnerFactory | None = None
    ) -> None:
        self._checkpoint_runner_factory = checkpoint_runner_factory or _default_checkpoint_runner

    def run_checkpoint(
        self,
        *,
        repo_root: str | Path,
        as_of_date: str,
        live_root: str | Path,
        work_root: str | Path,
        deep_receipt_root: str | Path,
        live_materialization_authorized: bool,
        checkpoint_resume: bool,
        fact_documents_per_call: int = 1,
    ) -> Mapping[str, Any]:
        if not live_materialization_authorized or not checkpoint_resume:
            raise ValueError("Phase107 requires live authorization and checkpoint resume")
        if (
            isinstance(fact_documents_per_call, bool)
            or not isinstance(fact_documents_per_call, int)
            or fact_documents_per_call <= 0
        ):
            raise ValueError("fact_documents_per_call must be positive")
        repo = Path(repo_root).resolve()
        live = Path(live_root).absolute()
        work = Path(work_root).absolute()
        receipts = Path(deep_receipt_root).absolute()
        candidates = natural_current_candidates(live_root=live, as_of_date=as_of_date)
        if not candidates:
            return _pending_result(candidate=None, detail="NATURAL_CURRENT_CANDIDATE_PENDING")
        completed: list[tuple[Mapping[str, Any], Path, Mapping[str, Any]]] = []
        candidate: Mapping[str, Any] | None = None
        for row in candidates:
            existing = receipts / str(row["target_id"])
            if not existing.exists():
                candidate = row
                break
            report = verify_current_krx_deep_receipt(
                existing,
                repo_root=repo,
                expected_candidate=row,
            )
            if report.get("status") != VERIFICATION_PASS:
                raise ValueError("existing natural deep receipt is invalid or stale")
            completed.append((row, existing, report))
        if candidate is None:
            if not completed:
                raise ValueError("natural Phase107 candidate roster did not advance")
            row, existing, report = completed[0]
            return self._pass_result(
                candidate=row,
                receipt_path=existing,
                report=report,
            )
        target_id = str(candidate["target_id"])

        work_fd = _open_or_create_directory_no_symlinks(work)
        os.close(work_fd)
        lineage = _mapping(candidate["natural_lineage"], context="natural lineage")
        planner_run_id = str(lineage["planner_run_id"])
        if re.fullmatch(r"[A-Za-z0-9_.-]+", planner_run_id) is None:
            raise ValueError("planner run ID is unsafe for a checkpoint path")
        research_parent = work / "research" / planner_run_id
        target_root = research_parent / target_id
        terminal = False
        manifest_path = target_root / "target_run_manifest.json"
        if manifest_path.is_file() and not manifest_path.is_symlink():
            manifest = _read_json(manifest_path)
            terminal = bool(
                manifest.get("status") == PHASE107_TERMINAL_RESEARCH_STATUS
                and manifest.get("production_research_complete") is True
            )
        if not terminal:
            target = CurrentResearchTarget(
                symbol=target_id,
                company_name=str(candidate["company_name"]),
            )
            config = CurrentResearcherModeConfig(
                as_of_date=as_of_date,
                archetype_id=str(candidate["archetype_id"]),
                output_root=research_parent,
                live_materialization_authorized=True,
                checkpoint_resume=True,
                gold_lane_isolated=True,
                require_researcher_parity=True,
                latest_trading_snapshot_date=str(candidate["latest_trading_snapshot_date"]),
                fact_documents_per_call=fact_documents_per_call,
            )
            checkpoint_runner = self._checkpoint_runner_factory(candidate)
            try:
                run = checkpoint_runner.run_checkpoint(
                    config=config,
                    target=target,
                    repo_root=repo,
                    source_resume_mode="REUSE_READY_CHECKPOINT",
                )
            except FactExtractionCheckpointPending:
                return _pending_result(
                    candidate=candidate,
                    detail="FACT_EXTRACTION_CHECKPOINT_PENDING",
                    target_root=target_root,
                )
            except StructuredProviderUnavailable as exc:
                if not str(exc).startswith("COLLABORATION_RESPONSE_PENDING:"):
                    raise
                return _pending_result(
                    candidate=candidate,
                    detail="RESEARCH_COLLABORATION_RESPONSE",
                    target_root=target_root,
                )
            if getattr(run, "status", None) != PHASE107_TERMINAL_RESEARCH_STATUS:
                return _pending_result(
                    candidate=candidate,
                    detail="SEMANTIC_CHECKPOINT_PENDING",
                    target_root=target_root,
                )
        receipt_path = export_current_krx_deep_receipt(
            repo_root=repo,
            target_root=target_root,
            destination_root=receipts,
            candidate=candidate,
        )
        report = verify_current_krx_deep_receipt(
            receipt_path,
            repo_root=repo,
            expected_candidate=candidate,
        )
        if report.get("status") != VERIFICATION_PASS:
            raise ValueError("canonical natural deep receipt verification failed")
        return self._pass_result(candidate=candidate, receipt_path=receipt_path, report=report)

    @staticmethod
    def _pass_result(
        *,
        candidate: Mapping[str, Any],
        receipt_path: Path,
        report: Mapping[str, Any],
    ) -> Mapping[str, Any]:
        return {
            "schema_version": PHASE107_DEEP_RUN_SCHEMA,
            "status": PHASE107_DEEP_RUN_PASS,
            "selected_target_id": candidate["target_id"],
            "selected_archetype_id": candidate["archetype_id"],
            "natural_lineage_hash": candidate["natural_lineage_hash"],
            "receipt_path": str(receipt_path),
            "verification_status": report["status"],
            "completion_based_on_fixed_retries": False,
            "gold_visibility": False,
            "gold_call_count": 0,
            "local_provider_call_count": 0,
            "score_or_stage_authority": False,
            "production_readiness_authority": False,
        }


__all__ = [
    "PHASE107_DEEP_RECEIPT_PASS",
    "PHASE107_DEEP_RECEIPT_SCHEMA",
    "PHASE107_DEEP_RUN_PASS",
    "PHASE107_DEEP_RUN_PENDING",
    "PHASE107_DEEP_RUN_SCHEMA",
    "PHASE107_DEEP_SCORE_SCHEMA",
    "V6CurrentKrxDeepReceiptRunner",
    "export_current_krx_deep_receipt",
    "natural_current_candidates",
    "project_natural_current_candidate",
    "validate_current_krx_deep_receipt_root",
    "verify_current_krx_deep_receipt",
]

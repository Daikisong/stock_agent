"""Strict Phase-107 current KRX Census cutover projection.

The legacy Census packager is intentionally useful for baseline and pending
maps.  A baseline map, however, is not evidence that the Phase-107 selective
deep contract completed.  This module adds the stronger cutover boundary:

* every row comes from the current official KRX universe;
* trigger/depth/planner lineage is reloaded from the live leaves;
* a current score or Stage is exposed only from an independently verified
  compact Researcher Mode receipt; and
* at least one naturally selected candidate reaches L5 with a valid score and
  FINAL StageCourt decision.

No summary field is accepted as a substitute for those leaves.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from datetime import date, datetime
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence
from zoneinfo import ZoneInfo

from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_selection import load_current_live_selection_inputs
from e2r.production.v6_current_krx_deep_receipt_runner import (
    project_natural_current_candidate,
    verify_current_krx_deep_receipt,
)
from e2r.research_brain.runtime.live_materialization import (
    LiveDepth,
    LiveUniverseRow,
    load_depth_decisions,
    load_trigger_signals,
    load_universe_rows,
)
from e2r.research_brain.researcher_mode.tracked_receipts import (
    VERIFICATION_PASS,
)


CURRENT_KRX_CENSUS_SCHEMA = "e2r_v6_current_krx_census_summary_v1"
CURRENT_KRX_STAGE_ROW_SCHEMA = "e2r_v6_current_krx_stage_map_row_v1"
CURRENT_KRX_CENSUS_PASS = "CURRENT_KRX_CENSUS_SELECTIVE_DEEP_OPERATIONAL_PASS"
CURRENT_KRX_CENSUS_FAIL = "CURRENT_KRX_CENSUS_SELECTIVE_DEEP_OPERATIONAL_FAIL"
CURRENT_KRX_CENSUS_TEST_PASS = "CURRENT_KRX_CENSUS_SELECTIVE_DEEP_CONTRACT_TEST_PASS"

CANONICAL_TRIGGER_LANES = (
    "OFFICIAL_DISCLOSURE",
    "ISSUER_IR_EARNINGS",
    "TRUSTED_NEWS",
    "REPORT_CONSENSUS_REVISION",
    "PRICE_VOLUME_ANOMALY",
    "RESEARCH_MEMORY_HINT",
    "RISK_EVENT",
)

_TRIGGER_LANE_BY_TYPE = {
    "OFFICIAL": "OFFICIAL_DISCLOSURE",
    "EARNINGS": "ISSUER_IR_EARNINGS",
    "IR": "ISSUER_IR_EARNINGS",
    "NEWS": "TRUSTED_NEWS",
    "REPORT": "REPORT_CONSENSUS_REVISION",
    "MARKET": "PRICE_VOLUME_ANOMALY",
    "EXISTING_LEDGER": "RESEARCH_MEMORY_HINT",
    "RISK": "RISK_EVENT",
}

_DEPTH_LABEL = {
    LiveDepth.L0_UNIVERSE.value: "L0",
    LiveDepth.L1_BASELINE.value: "L1",
    LiveDepth.L2_OFFICIAL_LIGHT.value: "L2",
    LiveDepth.L3_RESEARCH_BRAIN.value: "L3",
    LiveDepth.L4_ACQUISITION.value: "L4",
    LiveDepth.L5_FULL_THESIS.value: "L5",
}

_REQUIRED_LIVE_FILES = (
    "universe_provenance.json",
    "universe_raw.jsonl",
    "universe_eligible.jsonl",
    "universe_excluded.jsonl",
    "universe_audit.json",
    "baseline_lanes.jsonl",
    "baseline_lane_audit.json",
    "trigger_signals.jsonl",
    "candidate_events.jsonl",
    "trigger_fusion_audit.json",
    "depth_decisions.jsonl",
    "candidate_selection_audit.json",
    "planner_runs.jsonl",
    "llm_prompts.jsonl",
    "llm_responses.jsonl",
    "planner_validation.json",
    "source_tasks.jsonl",
    "question_source_tasks.jsonl",
    "source_task_audit.json",
    "provider_requests.jsonl",
    "provider_fetch_results.jsonl",
    "evidence_documents.jsonl",
    "provider_call_report.json",
    "source_task_satisfaction.jsonl",
    "adjudicated_claims.jsonl",
    "claim_compiler_audit.json",
    "current_claim_ledger.jsonl",
    "gap_closure_status.jsonl",
    "adaptive_gap_audit.json",
    "primitive_states.jsonl",
    "atomic_stage_decisions.jsonl",
    "atomic_score_audit.json",
)

_AUDIT_CONTRACTS = {
    "universe_audit.json": ("e2r_live_universe_audit_v1", None),
    "baseline_lane_audit.json": (
        "e2r_live_baseline_lane_audit_v1",
        "CURRENT_BASELINE_LANES_PASS",
    ),
    "trigger_fusion_audit.json": (
        "e2r_live_trigger_fusion_audit_v1",
        "CURRENT_TRIGGER_FUSION_PASS",
    ),
    "candidate_selection_audit.json": (
        "e2r_live_depth_selection_audit_v1",
        "CURRENT_DEPTH_SELECTION_PASS",
    ),
    "planner_validation.json": (
        "e2r_live_brain_planner_audit_v1",
        "CURRENT_BRAIN_PLANNER_PASS",
    ),
    "source_task_audit.json": (
        "e2r_live_source_task_audit_v1",
        "CURRENT_SOURCE_TASK_PASS",
    ),
    "provider_call_report.json": (
        "e2r_live_source_acquisition_audit_v1",
        "CURRENT_SOURCE_ACQUISITION_PASS",
    ),
    "claim_compiler_audit.json": (
        "e2r_live_current_claim_audit_v1",
        "CURRENT_CLAIM_COMPILER_PASS",
    ),
    "adaptive_gap_audit.json": (
        "e2r_live_adaptive_gap_audit_v1",
        "ADAPTIVE_GAP_CLOSURE_PASS",
    ),
    "atomic_score_audit.json": (
        "e2r_live_current_atomic_score_audit_v1",
        "CURRENT_ATOMIC_DECISION_PASS",
    ),
}

ReceiptVerifier = Callable[[str | Path], Mapping[str, Any]]


def compile_current_krx_census_cutover(
    *,
    assessment_as_of_date: str,
    live_root: str | Path,
    deep_receipt_root: str | Path,
    receipt_verifier: ReceiptVerifier = verify_current_krx_deep_receipt,
    test_mode: bool = False,
    execution_date_kst: str | None = None,
) -> tuple[Mapping[str, Any], tuple[Mapping[str, Any], ...]]:
    """Compile the strict full-universe map and Phase-107 verdict.

    ``receipt_verifier`` is injectable only for bounded unit fixtures.  The
    production path is permanently tied to the Gold-free natural deep receipt
    verifier.  A Phase-101 Gold receipt or Phase-105 forced canary therefore
    cannot be substituted for a current natural L5 completion.
    A fixture pass is labelled separately and can never claim operational
    readiness.
    """

    date.fromisoformat(assessment_as_of_date)
    execution_date_kst = execution_date_kst or datetime.now(
        ZoneInfo("Asia/Seoul")
    ).date().isoformat()
    date.fromisoformat(execution_date_kst)
    if not isinstance(test_mode, bool):
        raise TypeError("test_mode must be boolean")
    if receipt_verifier is not verify_current_krx_deep_receipt and not test_mode:
        raise ValueError("production Census cannot replace the receipt verifier")

    live = Path(live_root)
    receipt_root = Path(deep_receipt_root)
    failures: list[Mapping[str, Any]] = []
    missing_live_files = tuple(
        name for name in _REQUIRED_LIVE_FILES if not _regular_file(live / name)
    )
    if missing_live_files:
        failures.append(
            {
                "code": "LIVE_STAGE_LEAF_MISSING",
                "detail": list(missing_live_files),
            }
        )

    audit_failure_count = 0
    audit_payloads: dict[str, Mapping[str, Any]] = {}
    if not missing_live_files:
        for name, (expected_schema, expected_status) in _AUDIT_CONTRACTS.items():
            try:
                audit = _read_json(live / name)
            except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
                failures.append(
                    {
                        "code": "LIVE_STAGE_AUDIT_INVALID",
                        "detail": {"path": name, "reason": str(exc)},
                    }
                )
                audit_failure_count += 1
                continue
            audit_payloads[name] = audit
            critical_sum = audit.get("critical_count_sum")
            if (
                audit.get("schema_version") != expected_schema
                or str(audit.get("as_of_date") or "") != assessment_as_of_date
                or (
                    expected_status is not None
                    and audit.get("status") != expected_status
                )
                or isinstance(critical_sum, bool)
                or not isinstance(critical_sum, int)
                or critical_sum != 0
                or audit.get("hard_acceptance_pass") is not True
            ):
                failures.append(
                    {
                        "code": "LIVE_STAGE_AUDIT_NOT_PASS",
                        "detail": name,
                    }
                )
                audit_failure_count += 1

    universe: tuple[LiveUniverseRow, ...] = ()
    triggers = ()
    depth = ()
    selection_candidates: Sequence[Mapping[str, Any]] = ()
    selection_trigger_rows: Sequence[Mapping[str, Any]] = ()
    source_available_at: str | None = None
    if not missing_live_files:
        try:
            raw_universe = load_universe_rows(live / "universe_raw.jsonl")
            universe = load_universe_rows(live / "universe_eligible.jsonl")
            excluded_universe = load_universe_rows(
                live / "universe_excluded.jsonl"
            )
            provenance = _read_json(live / "universe_provenance.json")
            universe_audit = audit_payloads["universe_audit.json"]
            source_available_at = _validate_universe_partition(
                assessment_as_of_date=assessment_as_of_date,
                raw_universe=raw_universe,
                eligible_universe=universe,
                excluded_universe=excluded_universe,
                provenance=provenance,
                universe_audit=universe_audit,
            )
            triggers = load_trigger_signals(live / "trigger_signals.jsonl")
            depth = load_depth_decisions(live / "depth_decisions.jsonl")
            selection_candidates, selection_trigger_rows = load_current_live_selection_inputs(
                live,
                selection_as_of_date=assessment_as_of_date,
            )
        except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
            failures.append(
                {
                    "code": "LIVE_LINEAGE_VALIDATION_FAILED",
                    "detail": f"{type(exc).__name__}:{exc}",
                }
            )

    universe_by_symbol = {
        str(row.symbol): row for row in universe if row.eligible and row.symbol
    }
    if len(universe_by_symbol) != len(universe):
        failures.append({"code": "ELIGIBLE_UNIVERSE_IDENTITY_MISMATCH", "detail": None})
    decision_by_target = {row.target_id: row for row in depth}
    if len(decision_by_target) != len(depth):
        failures.append({"code": "DEPTH_DECISION_TARGET_DUPLICATE", "detail": None})
    triggers_by_target: dict[str, list[Any]] = {}
    for row in triggers:
        triggers_by_target.setdefault(row.target_id, []).append(row)

    expected_natural_candidates: Mapping[str, Mapping[str, Any]] | None = None
    if receipt_verifier is verify_current_krx_deep_receipt:
        try:
            projected_candidates = tuple(
                project_natural_current_candidate(
                    row,
                    trigger_rows=selection_trigger_rows,
                    as_of_date=assessment_as_of_date,
                )
                for row in selection_candidates
            )
            expected_natural_candidates = {
                str(row["target_id"]): row for row in projected_candidates
            }
            if len(expected_natural_candidates) != len(projected_candidates):
                raise ValueError("natural planner target roster is duplicated")
        except (KeyError, TypeError, ValueError) as exc:
            failures.append(
                {
                    "code": "NATURAL_DEEP_CANDIDATE_LINEAGE_INVALID",
                    "detail": f"{type(exc).__name__}:{exc}",
                }
            )
            expected_natural_candidates = {}
    receipt_rows, receipt_failures = _verified_deep_receipts(
        receipt_root=receipt_root,
        universe_by_symbol=universe_by_symbol,
        assessment_as_of_date=assessment_as_of_date,
        receipt_verifier=receipt_verifier,
        expected_natural_candidates=expected_natural_candidates,
    )
    failures.extend(receipt_failures)
    receipt_by_target = {str(row["target_id"]): row for row in receipt_rows}

    planner_targets = {
        str(row.get("target_id") or "") for row in selection_candidates
    }
    source_task_targets = {
        str(row.get("target_id") or "")
        for row in _safe_jsonl(live / "source_tasks.jsonl")
    }
    document_targets = {
        str(row.get("target_id") or "")
        for row in _safe_jsonl(live / "evidence_documents.jsonl")
    }
    accepted_claims = tuple(
        row
        for row in _safe_jsonl(live / "adjudicated_claims.jsonl")
        if str(row.get("investigation_status") or row.get("status") or "")
        in {"ACCEPTED", "CURRENT_ACCEPTED", "ADJUDICATED_ACCEPTED"}
        or row.get("accepted") is True
    )

    stage_rows: list[Mapping[str, Any]] = []
    for target_id, member in sorted(universe_by_symbol.items()):
        decision = decision_by_target.get(target_id)
        target_triggers = tuple(
            sorted(
                triggers_by_target.get(target_id, ()),
                key=lambda row: (row.effective_date, row.trigger_signal_id),
            )
        )
        receipt = receipt_by_target.get(target_id)
        maximum_depth = _effective_depth(
            target_id=target_id,
            decision=decision,
            planner_targets=planner_targets,
            source_task_targets=source_task_targets,
            document_targets=document_targets,
            has_verified_receipt=receipt is not None,
        )
        if receipt is not None:
            current_score = receipt["total_score"]
            current_score_status = "COMPLETE"
            canonical_stage = receipt["canonical_stage"]
            stage_status = "FINAL"
            research_status = "FULL_RESEARCH_COMPLETE"
            pending_reason = None
            dossier_receipt_id = receipt["receipt_id"]
        else:
            current_score = None
            current_score_status = (
                "RESEARCH_IN_PROGRESS"
                if decision is not None and decision.selected_for_deep
                else "NO_CURRENT_COMPLETE_SCORE"
            )
            canonical_stage = None
            stage_status = (
                "RESEARCH_IN_PROGRESS"
                if decision is not None and decision.selected_for_deep
                else "NOT_OPEN"
            )
            research_status = _research_status(
                maximum_depth=maximum_depth,
                selected_for_deep=bool(decision and decision.selected_for_deep),
            )
            pending_reason = (
                "VERIFIED_FULL_RESEARCH_RECEIPT_PENDING"
                if decision is not None and decision.selected_for_deep
                else None
            )
            dossier_receipt_id = None
        row = {
            "schema_version": CURRENT_KRX_STAGE_ROW_SCHEMA,
            "symbol": target_id,
            "company_name": str(member.company_name),
            "market": member.market,
            "assessment_as_of_date": assessment_as_of_date,
            "latest_trading_snapshot_date": member.source_effective_date,
            "trigger_lane_ids": sorted(
                {
                    _TRIGGER_LANE_BY_TYPE[row.trigger_type]
                    for row in target_triggers
                    if row.trigger_type in _TRIGGER_LANE_BY_TYPE
                }
            ),
            "maximum_depth": maximum_depth,
            "research_status": research_status,
            "current_score": current_score,
            "current_score_status": current_score_status,
            "last_effective_score": None,
            "canonical_stage": canonical_stage,
            "last_effective_stage": None,
            "stage_status": stage_status,
            "dossier_receipt_id": dossier_receipt_id,
            "pending_reason": pending_reason,
        }
        stage_rows.append(row)

    stage_tuple = tuple(stage_rows)
    trigger_lane_counts = {
        lane: sum(lane in row["trigger_lane_ids"] for row in stage_tuple)
        for lane in CANONICAL_TRIGGER_LANES
    }
    depth_counts = {
        level: sum(row["maximum_depth"] == level for row in stage_tuple)
        for level in ("L0", "L1", "L2", "L3", "L4", "L5")
    }
    # A selected depth row is only an upstream intention.  Natural L5
    # authority begins at the loader-validated COMPLETE planner roster; an
    # ABSTAINED/PENDING target must not inflate this count merely because its
    # depth and trigger leaves exist.
    natural_candidate_ids = planner_targets & set(triggers_by_target)
    l5_target_ids = {
        str(row["symbol"]) for row in stage_tuple if row["maximum_depth"] == "L5"
    }
    scoring_fact_count = sum(int(row["scoring_fact_count"]) for row in receipt_rows)
    nonzero_score_contribution_count = sum(
        int(row["nonzero_score_contribution_count"]) for row in receipt_rows
    )
    provider_failed_final_score_count = sum(
        bool(row.get("provider_failure_count")) for row in receipt_rows
    )
    snippet_score_count = sum(int(row["snippet_score_count"]) for row in receipt_rows)
    source_proxy_current_score_count = sum(
        row["current_score"] is not None and row["dossier_receipt_id"] is None
        for row in stage_tuple
    )
    score_valid_count = len(receipt_rows)
    final_stage_count = sum(row["stage_status"] == "FINAL" for row in stage_tuple)
    natural_l5_count = len(natural_candidate_ids & l5_target_ids)

    critical_counts = {
        "live_stage_leaf_missing_count": len(missing_live_files),
        "live_stage_audit_failure_count": audit_failure_count,
        "synthetic_target_count": sum(
            not row.source_url.startswith("https://data-dbg.krx.co.kr/")
            or row.source_mode != "LIVE"
            for row in universe
        ),
        "eligible_coverage_mismatch_count": abs(len(stage_tuple) - len(universe)),
        "missing_depth_decision_count": len(set(universe_by_symbol) - set(decision_by_target)),
        "duplicate_stage_symbol_count": len(stage_tuple)
        - len({row["symbol"] for row in stage_tuple}),
        "natural_trigger_lane_shortfall_count": max(
            0, 3 - sum(value > 0 for value in trigger_lane_counts.values())
        ),
        "natural_candidate_missing_count": int(not natural_candidate_ids),
        "l3_missing_count": int(not planner_targets),
        "l4_missing_count": int(not (source_task_targets & document_targets)),
        "l5_completed_missing_count": int(not l5_target_ids),
        "natural_l5_completed_missing_count": int(natural_l5_count == 0),
        "accepted_scoring_fact_missing_count": int(scoring_fact_count == 0),
        "score_contribution_missing_count": int(
            nonzero_score_contribution_count == 0
        ),
        "score_valid_deep_row_missing_count": int(score_valid_count == 0),
        "final_stage_deep_row_missing_count": int(final_stage_count == 0),
        "provider_failed_final_score_count": provider_failed_final_score_count,
        "snippet_score_count": snippet_score_count,
        "source_proxy_current_score_count": source_proxy_current_score_count,
        "all_zero_or_all_pending_false_pass_count": int(
            bool(stage_tuple)
            and (
                score_valid_count == 0
                or final_stage_count == 0
                or all(row["canonical_stage"] in {None, "0"} for row in stage_tuple)
            )
        ),
        "receipt_validation_failure_count": len(receipt_failures),
    }
    critical_count_sum = len(failures) + sum(
        int(value) for value in critical_counts.values()
    )
    production_pass = critical_count_sum == 0 and not test_mode
    contract_test_pass = critical_count_sum == 0 and test_mode
    summary_core = {
        "schema_version": CURRENT_KRX_CENSUS_SCHEMA,
        "status": (
            CURRENT_KRX_CENSUS_PASS
            if production_pass
            else CURRENT_KRX_CENSUS_TEST_PASS
            if contract_test_pass
            else CURRENT_KRX_CENSUS_FAIL
        ),
        "assessment_as_of_date": assessment_as_of_date,
        "execution_date_kst": execution_date_kst,
        "latest_available_trading_snapshot_date": max(
            (row.source_effective_date for row in universe),
            default=None,
        ),
        "source_available_at": source_available_at,
        "real_krx_universe_source": bool(universe)
        and all(
            row.source_url.startswith("https://data-dbg.krx.co.kr/")
            and row.source_mode == "LIVE"
            for row in universe
        ),
        "eligible_universe_count": len(universe),
        "stage_map_row_count": len(stage_tuple),
        "trigger_lane_counts": trigger_lane_counts,
        "natural_trigger_lane_count": sum(
            value > 0 for value in trigger_lane_counts.values()
        ),
        "depth_counts": depth_counts,
        "natural_candidate_count": len(natural_candidate_ids),
        "natural_l5_completed_count": natural_l5_count,
        "accepted_scoring_fact_count": scoring_fact_count,
        "nonzero_score_contribution_count": nonzero_score_contribution_count,
        "score_valid_deep_row_count": score_valid_count,
        "final_stage_deep_row_count": final_stage_count,
        "deep_receipt_ids": sorted(str(row["receipt_id"]) for row in receipt_rows),
        "stage_map_hash": stable_hash(stage_tuple),
        "live_input_tree_hash": _tree_hash(live, _REQUIRED_LIVE_FILES),
        "critical_counts": critical_counts,
        "critical_count_sum": critical_count_sum,
        "failures": failures,
        "production_runtime_ready": production_pass,
        "test_mode": test_mode,
        "investment_recommendation_emitted": False,
    }
    return {
        **summary_core,
        "summary_hash": stable_hash(summary_core),
    }, stage_tuple


def _verified_deep_receipts(
    *,
    receipt_root: Path,
    universe_by_symbol: Mapping[str, LiveUniverseRow],
    assessment_as_of_date: str,
    receipt_verifier: ReceiptVerifier,
    expected_natural_candidates: Mapping[str, Mapping[str, Any]] | None,
) -> tuple[tuple[Mapping[str, Any], ...], list[Mapping[str, Any]]]:
    rows: list[Mapping[str, Any]] = []
    failures: list[Mapping[str, Any]] = []
    if not receipt_root.is_dir() or receipt_root.is_symlink():
        return (), [
            {
                "code": "DEEP_RECEIPT_ROOT_MISSING_OR_UNSAFE",
                "detail": str(receipt_root),
            }
        ]
    children = tuple(sorted(receipt_root.iterdir(), key=lambda path: path.name))
    invalid = tuple(
        path.name for path in children if not path.is_dir() or path.is_symlink()
    )
    if invalid:
        failures.append(
            {"code": "DEEP_RECEIPT_ROOT_ENTRY_INVALID", "detail": list(invalid)}
        )
    for target_root in children:
        if not target_root.is_dir() or target_root.is_symlink():
            continue
        report = receipt_verifier(target_root)
        target_id = str(report.get("target_id") or target_root.name)
        if (
            report.get("status") != VERIFICATION_PASS
            or int(report.get("critical_count") or 0) != 0
        ):
            failures.append(
                {
                    "code": "DEEP_RECEIPT_VERIFICATION_FAILED",
                    "detail": {"target_id": target_id, "report": dict(report)},
                }
            )
            continue
        try:
            manifest = _read_json(target_root / "receipt_manifest.json")
            score = _read_json(target_root / "score_receipt.json")
            stage = _read_json(target_root / "stagecourt_receipt.json")
            facts = _read_jsonl(target_root / "scoring_facts.jsonl")
            provider_calls = _read_jsonl(target_root / "provider_calls.jsonl")
        except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
            failures.append(
                {
                    "code": "DEEP_RECEIPT_LEAF_READ_FAILED",
                    "detail": {"target_id": target_id, "reason": str(exc)},
                }
            )
            continue
        if expected_natural_candidates is not None:
            expected = expected_natural_candidates.get(target_id)
            expected_lineage = (
                expected.get("natural_lineage")
                if isinstance(expected, Mapping)
                else None
            )
            if (
                expected is None
                or manifest.get("company_name") != expected.get("company_name")
                or manifest.get("archetype_id") != expected.get("archetype_id")
                or manifest.get("latest_trading_snapshot_date")
                != expected.get("latest_trading_snapshot_date")
                or manifest.get("natural_lineage_hash")
                != expected.get("natural_lineage_hash")
                or manifest.get("natural_lineage") != expected_lineage
            ):
                failures.append(
                    {
                        "code": "DEEP_RECEIPT_NATURAL_LINEAGE_MISMATCH",
                        "detail": target_id,
                    }
                )
                continue
        if (
            target_id not in universe_by_symbol
            or manifest.get("target_id") != target_id
            or manifest.get("as_of_date") != assessment_as_of_date
            or score.get("target_id") != target_id
            or score.get("score_valid") is not True
            or score.get("research_complete") is not True
            or score.get("semantic_saturation_certified") is not True
            or int(score.get("material_gap_count") or 0) != 0
            or int(score.get("provider_error_count") or 0) != 0
            or stage.get("target_id") != target_id
            or stage.get("decision_status") != "FINAL"
            or stage.get("score_valid") is not True
            or stage.get("canonical_stage") != score.get("canonical_stage")
        ):
            failures.append(
                {
                    "code": "DEEP_RECEIPT_CURRENT_COMPLETION_MISMATCH",
                    "detail": target_id,
                }
            )
            continue
        total_score = score.get("total_score")
        if (
            isinstance(total_score, bool)
            or not isinstance(total_score, (int, float))
            or not math.isfinite(float(total_score))
        ):
            failures.append(
                {"code": "DEEP_RECEIPT_SCORE_INVALID", "detail": target_id}
            )
            continue
        snippet_count = sum(
            fact.get("headline_or_snippet_only") is True
            or str(fact.get("source_tier") or "").upper() in {"SNIPPET", "SEARCH_SNIPPET"}
            or not str(fact.get("quote_excerpt") or "").strip()
            for fact in facts
        )
        provider_failure_count = sum(
            any(
                token in str(
                    row.get("provider_status") or row.get("status") or ""
                ).upper()
                for token in ("ERROR", "FAILED", "PENDING", "QUARANTIN")
            )
            for row in provider_calls
        )
        component_vector = score.get("component_score_vector")
        if isinstance(component_vector, Mapping):
            nonzero_score_contribution_count = sum(
                isinstance(value, (int, float))
                and not isinstance(value, bool)
                and math.isfinite(float(value))
                and abs(float(value)) > 1e-12
                for value in component_vector.values()
            )
        else:
            # Production receipts are schema-verified and always carry the
            # component vector.  This fallback keeps bounded contract fixtures
            # useful without letting a zero total masquerade as contribution.
            nonzero_score_contribution_count = int(abs(float(total_score)) > 1e-12)
        rows.append(
            {
                "target_id": target_id,
                "receipt_id": str(manifest.get("receipt_id") or ""),
                "total_score": float(total_score),
                "canonical_stage": str(stage.get("canonical_stage") or ""),
                "scoring_fact_count": len(facts),
                "snippet_score_count": snippet_count,
                "provider_failure_count": provider_failure_count,
                "nonzero_score_contribution_count": (
                    nonzero_score_contribution_count
                ),
            }
        )
    if len({row["target_id"] for row in rows}) != len(rows):
        failures.append({"code": "DEEP_RECEIPT_TARGET_DUPLICATE", "detail": None})
    return tuple(rows), failures


def _validate_universe_partition(
    *,
    assessment_as_of_date: str,
    raw_universe: Sequence[LiveUniverseRow],
    eligible_universe: Sequence[LiveUniverseRow],
    excluded_universe: Sequence[LiveUniverseRow],
    provenance: Mapping[str, Any],
    universe_audit: Mapping[str, Any],
) -> str:
    """Validate the complete official KRX partition and return availability.

    Reading only ``universe_eligible.jsonl`` would allow a hand-authored
    shortlist to look like a Census.  The provenance hashes, raw/excluded
    partition and audit counts therefore have to agree exactly.
    """

    as_of = date.fromisoformat(assessment_as_of_date)
    raw_payload = [row.to_dict() for row in raw_universe]
    eligible_payload = [row.to_dict() for row in eligible_universe]
    if (
        provenance.get("schema_version")
        != "e2r_live_krx_universe_provenance_v1"
        or provenance.get("status") != "CURRENT_UNIVERSE_MATERIALIZATION_PASS"
        or provenance.get("as_of_date") != assessment_as_of_date
        or provenance.get("raw_universe_hash") != stable_hash(raw_payload)
        or provenance.get("eligible_universe_hash")
        != stable_hash(eligible_payload)
        or not raw_universe
        or not eligible_universe
        or any(not row.eligible for row in eligible_universe)
        or any(row.eligible for row in excluded_universe)
    ):
        raise ValueError("current KRX universe provenance or eligibility mismatch")
    raw_roster = Counter(stable_hash(row.to_dict()) for row in raw_universe)
    partition_roster = Counter(
        stable_hash(row.to_dict())
        for row in (*eligible_universe, *excluded_universe)
    )
    if raw_roster != partition_roster:
        raise ValueError("current KRX raw/eligible/excluded partition mismatch")
    effective_dates = {row.source_effective_date for row in raw_universe}
    source_effective_date = str(provenance.get("source_effective_date") or "")
    if (
        effective_dates != {source_effective_date}
        or date.fromisoformat(source_effective_date) > as_of
        or int(universe_audit.get("raw_universe_count", -1))
        != len(raw_universe)
        or int(universe_audit.get("eligible_universe_count", -1))
        != len(eligible_universe)
        or int(universe_audit.get("excluded_universe_count", -1))
        != len(excluded_universe)
        or int(universe_audit.get("duplicate_eligible_symbol_count", -1)) != 0
        or int(universe_audit.get("missing_symbol_count", -1)) != 0
        or universe_audit.get("source_effective_date") != source_effective_date
    ):
        raise ValueError("current KRX universe audit count/date mismatch")
    attempts = tuple(provenance.get("request_attempts") or ())
    selected_attempts: list[Mapping[str, Any]] = []
    for raw_attempt in attempts:
        if not isinstance(raw_attempt, Mapping):
            raise ValueError("current KRX provenance request attempt is invalid")
        attempt = dict(raw_attempt)
        if (
            attempt.get("status") == "FETCHED"
            and attempt.get("effective_date") == source_effective_date
            and int(attempt.get("row_count") or 0) > 0
        ):
            selected_attempts.append(attempt)
    if (
        len(selected_attempts) != len({row.market for row in raw_universe})
        or int(universe_audit.get("provider_request_count", -1)) != len(attempts)
    ):
        raise ValueError("current KRX selected request provenance mismatch")
    fetched_at_values: list[str] = []
    for attempt in selected_attempts:
        fetched_at = str(attempt.get("fetched_at") or "")
        parsed = datetime.fromisoformat(fetched_at.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            raise ValueError("current KRX source availability must be timezone-aware")
        fetched_at_values.append(parsed.isoformat())
    if not fetched_at_values:
        raise ValueError("current KRX source availability is missing")
    return max(fetched_at_values)


def _effective_depth(
    *,
    target_id: str,
    decision: Any | None,
    planner_targets: set[str],
    source_task_targets: set[str],
    document_targets: set[str],
    has_verified_receipt: bool,
) -> str:
    if has_verified_receipt:
        return "L5"
    if target_id in source_task_targets and target_id in document_targets:
        return "L4"
    if target_id in planner_targets:
        return "L3"
    if decision is None:
        return "L0"
    return _DEPTH_LABEL.get(decision.maximum_depth, "L0")


def _research_status(*, maximum_depth: str, selected_for_deep: bool) -> str:
    if selected_for_deep:
        return "RESEARCH_IN_PROGRESS"
    if maximum_depth == "L2":
        return "OFFICIAL_LIGHT_COMPLETE"
    if maximum_depth == "L1":
        return "BASELINE_COMPLETE"
    return "UNIVERSE_ONLY"


def _regular_file(path: Path) -> bool:
    return path.is_file() and not path.is_symlink()


def _read_json(path: Path) -> Mapping[str, Any]:
    if not _regular_file(path):
        raise ValueError(f"unsafe or missing JSON file: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, Mapping):
        raise ValueError(f"JSON root must be object: {path}")
    return value


def _read_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    if not _regular_file(path):
        raise ValueError(f"unsafe or missing JSONL file: {path}")
    rows = tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )
    if any(not isinstance(row, Mapping) for row in rows):
        raise ValueError(f"JSONL row must be object: {path}")
    return rows


def _safe_jsonl(path: Path) -> tuple[Mapping[str, Any], ...]:
    try:
        return _read_jsonl(path)
    except (OSError, TypeError, ValueError, json.JSONDecodeError):
        return ()


def _tree_hash(root: Path, names: Sequence[str]) -> str | None:
    if any(not _regular_file(root / name) for name in names):
        return None
    rows = tuple(
        {
            "path": name,
            "sha256": hashlib.sha256((root / name).read_bytes()).hexdigest(),
        }
        for name in sorted(names)
    )
    return stable_hash(rows)


__all__ = [
    "CANONICAL_TRIGGER_LANES",
    "CURRENT_KRX_CENSUS_FAIL",
    "CURRENT_KRX_CENSUS_PASS",
    "CURRENT_KRX_CENSUS_SCHEMA",
    "CURRENT_KRX_CENSUS_TEST_PASS",
    "CURRENT_KRX_STAGE_ROW_SCHEMA",
    "compile_current_krx_census_cutover",
]

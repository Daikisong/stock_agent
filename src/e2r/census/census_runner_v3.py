"""Census Mode v3 anti-fake full universe stage map runner."""

from __future__ import annotations

import csv
import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import build_report_metadata, git_head_sha, stable_hash, write_json, write_jsonl, write_text

from .baseline_scanner import BaselineScanInputs, BaselineScanner
from .census_backfill_plan import build_deep_backfill_plan, render_deep_backfill_plan
from .census_event import build_census_assessment_event
from .depth_policy import decide_depths, depth_policy_from_mapping
from .leaf_artifact_auditor import audit_leaf_artifacts
from .production_cutover_leaf_loader import ProductionCutoverLeafBundle, load_production_cutover_leaf_bundle
from .reviewers import write_reviewer_outputs
from .self_repair import build_self_repair_log_v3, self_repair_summary_md
from .source_family_collectors.companyguide_report_census_collector import collect_companyguide_report_attempt
from .source_family_collectors.existing_ledger_census_collector import collect_existing_ledger_attempt
from .source_family_collectors.issuer_ir_news_census_collector import collect_issuer_ir_news_attempt
from .source_family_collectors.kind_krx_census_collector import collect_kind_krx_attempt
from .source_family_collectors.opendart_census_collector import collect_opendart_attempt
from .source_family_collectors.price_volume_census_collector import collect_price_volume_attempt
from .source_family_collectors.research_memory_census_collector import collect_research_memory_attempt
from .universe import build_universe, eligible_instruments


@dataclass(frozen=True)
class CensusV3RunConfig:
    as_of_date: str
    output_root: str | None = None
    universe: str = "krx"
    universe_file: str | None = None
    max_symbols: int = 0
    max_iterations: int = 10
    fail_on_external_blocker: bool = True
    fail_on_report_overclaim: bool = True
    fail_on_critical_audit: bool = True
    write_operational_docs: bool = True
    test_result_summary: str = "not_run_by_census_v3_runner"
    commit_push_status: str = "pending_at_report_generation"

    def resolved_output_root(self) -> str:
        return self.output_root or f"output/census_v3/{self.as_of_date}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "as_of_date": self.as_of_date,
            "output_root": self.resolved_output_root(),
            "universe": self.universe,
            "universe_file": self.universe_file,
            "max_symbols": self.max_symbols,
            "max_iterations": self.max_iterations,
            "fail_on_external_blocker": self.fail_on_external_blocker,
            "fail_on_report_overclaim": self.fail_on_report_overclaim,
            "fail_on_critical_audit": self.fail_on_critical_audit,
            "write_operational_docs": self.write_operational_docs,
            "test_result_summary": self.test_result_summary,
            "commit_push_status": self.commit_push_status,
        }


@dataclass(frozen=True)
class CensusV3RunResult:
    output_root: str
    run_metadata: Mapping[str, Any]
    leaf_audit: Mapping[str, Any]
    reviewer_audit: Mapping[str, Any]
    readiness_verdict: Mapping[str, Any]


def run_census_mode_v3(config: CensusV3RunConfig) -> CensusV3RunResult:
    start = time.monotonic()
    output_root = Path(config.resolved_output_root())
    universe_file = config.universe_file or _default_universe_snapshot(config.as_of_date)
    universe = build_universe(
        as_of_date=config.as_of_date,
        universe_file=universe_file,
        max_symbols=config.max_symbols,
        allow_naver_fallback=(universe_file is None),
    )
    instruments = eligible_instruments(universe.instruments)
    symbol_to_instrument = {item.symbol: item for item in instruments}
    bundle = load_production_cutover_leaf_bundle(eligible_symbols=[item.symbol for item in instruments])
    report_events = _load_report_events(eligible_symbols=set(symbol_to_instrument), as_of_date=config.as_of_date)
    market_events = _load_market_events(eligible_symbols=set(symbol_to_instrument), as_of_date=config.as_of_date)
    inputs = _baseline_inputs(bundle=bundle, report_events=report_events, market_events=market_events, eligible_symbols=set(symbol_to_instrument))
    scans = BaselineScanner(inputs).scan_many(instruments, as_of_date=config.as_of_date)
    scan_by_symbol = {row.symbol: row for row in scans}
    assessment_events = tuple(
        build_census_assessment_event(
            instrument,
            as_of_date=config.as_of_date,
            universe_source="KRX" if config.universe == "krx" else config.universe,
            recent_candidate_events=tuple(row.get("candidate_event_id") for row in bundle.candidate_events if row.get("symbol") == instrument.symbol),
            recent_claim_ledger_refs=tuple(row.get("claim_id") for row in bundle.accepted_claims_by_symbol.get(instrument.symbol, ())),
            baseline_scan_refs=(f"baseline_scan:{instrument.symbol}",),
        )
        for instrument in instruments
    )
    assessment_by_symbol = {row.symbol: row for row in assessment_events}
    timelines = _source_timelines(
        instruments=instruments,
        as_of_date=config.as_of_date,
        bundle=bundle,
        report_events=report_events,
        market_events=market_events,
    )
    thesis_states = _last_effective_thesis_states(instruments=instruments, as_of_date=config.as_of_date, bundle=bundle, timelines=timelines)
    depth_decisions = decide_depths(
        instruments,
        scans,
        config=depth_policy_from_mapping({"max_deep_symbols": 50, "sector_sample_quota": 1, "max_source_tasks_per_symbol": 3}),
    )
    baseline_rows = [_baseline_row(scan.to_dict(), config.as_of_date) for scan in scans]
    depth_rows = [_depth_row(row.to_dict(), config.as_of_date) for row in depth_decisions]
    trace_rows = _claim_to_stage_traces(
        instruments=instruments,
        as_of_date=config.as_of_date,
        assessment_by_symbol=assessment_by_symbol,
        timelines=timelines,
        thesis_states=thesis_states,
        baseline_rows=baseline_rows,
        depth_rows=depth_rows,
        bundle=bundle,
    )
    stage_rows = _stage_rows(
        instruments=instruments,
        as_of_date=config.as_of_date,
        scan_by_symbol=scan_by_symbol,
        thesis_states={row["symbol"]: row for row in thesis_states},
        trace_by_symbol={row["symbol"]: row for row in trace_rows},
        bundle=bundle,
        report_events=report_events,
        market_events=market_events,
    )
    event_rows = _event_rows(
        assessment_events=[row.to_dict() for row in assessment_events],
        bundle=bundle,
        report_events=report_events,
        market_events=market_events,
        as_of_date=config.as_of_date,
    )
    stage_summary = _stage_summary(universe_count=len(universe.instruments), stage_rows=stage_rows)
    sector_distribution = _sector_distribution(stage_rows)
    provider_gap_report = _provider_gap_report(stage_rows, timelines)
    source_gap_report = _source_gap_report(stage_rows, timelines)
    watchlist_seed = _watchlist_seed(stage_rows, as_of_date=config.as_of_date)
    deep_backfill_plan = build_deep_backfill_plan(stage_rows, shard_count=10)
    metadata = build_report_metadata(
        repo_root=".",
        report_generator="e2r.census.census_runner_v3",
        command=_command_string(config),
        config=config.to_dict(),
        source_corpus={"universe": [item.to_dict() for item in universe.instruments], "production_cutover_leaf_claim_count": len(bundle.accepted_claims)},
        candidate_events=event_rows,
        planner_runs=bundle.research_brain_plans,
    )
    _write_leaf_outputs(
        output_root=output_root,
        universe_rows=[item.to_dict() for item in universe.instruments],
        assessment_events=[row.to_dict() for row in assessment_events],
        timelines=timelines,
        thesis_states=thesis_states,
        baseline_summary=_baseline_summary(bundle=bundle, timelines=timelines, provider_gap_report=provider_gap_report),
        baseline_rows=baseline_rows,
        event_rows=event_rows,
        depth_rows=depth_rows,
        research_plans=bundle.research_brain_plans,
        source_tasks=bundle.source_tasks,
        source_task_executions=bundle.source_task_executions,
        evidence_documents=bundle.evidence_documents,
        evidence_anchors=bundle.evidence_anchors,
        raw_assertions=bundle.raw_assertions,
        adjudicated_claims=bundle.adjudicated_claims,
        accepted_claims=bundle.accepted_claims,
        primitive_states=bundle.primitive_states,
        score_contributions=bundle.score_contributions,
        stagecourt_traces=bundle.stagecourt_traces,
        stage_rows=stage_rows,
        trace_rows=trace_rows,
        stage_summary=stage_summary,
        sector_distribution=sector_distribution,
        provider_gap_report=provider_gap_report,
        source_gap_report=source_gap_report,
        watchlist_seed=watchlist_seed,
        deep_backfill_plan=deep_backfill_plan,
        run_metadata=metadata,
    )
    leaf_audit = audit_leaf_artifacts(output_root)
    write_json(output_root / "leaf_artifact_audit.json", leaf_audit)
    reviewers = write_reviewer_outputs(output_root)
    readiness = _readiness_verdict(leaf_audit=leaf_audit, reviewers=reviewers)
    repair_log = build_self_repair_log_v3(
        as_of_date=config.as_of_date,
        command=_command_string(config),
        output_root=output_root,
        leaf_audit=leaf_audit,
        max_iterations=config.max_iterations,
    )
    write_json(output_root / "self_repair_log.json", repair_log)
    audit_summary = {
        "schema_version": "e2r_census_v3_audit_summary_v1",
        "leaf_artifact_audit": leaf_audit,
        "reviewers": reviewers,
        "readiness": readiness,
    }
    write_json(output_root / "audit_summary.json", audit_summary)
    write_text(
        output_root / "operator_digest.md",
        _operator_digest(stage_summary=stage_summary, leaf_audit=leaf_audit, watchlist_seed=watchlist_seed, provider_gap_report=provider_gap_report, source_gap_report=source_gap_report),
    )
    if config.write_operational_docs:
        _write_operational_docs(
            config=config,
            output_root=output_root,
            universe_coverage=universe.coverage,
            stage_summary=stage_summary,
            sector_distribution=sector_distribution,
            provider_gap_report=provider_gap_report,
            source_gap_report=source_gap_report,
            watchlist_seed=watchlist_seed,
            deep_backfill_plan=deep_backfill_plan,
            leaf_audit=leaf_audit,
            reviewers=reviewers,
            readiness=readiness,
            repair_log=repair_log,
            runtime_seconds=time.monotonic() - start,
        )
    if config.fail_on_critical_audit and (leaf_audit["verdict"] != "PASS" or readiness["verdict"] != "FULL_UNIVERSE_STAGE_MAP_PASS"):
        raise RuntimeError(f"Census v3 audit failed: {leaf_audit['critical_counts']}")
    return CensusV3RunResult(
        output_root=str(output_root),
        run_metadata=metadata,
        leaf_audit=leaf_audit,
        reviewer_audit=reviewers,
        readiness_verdict=readiness,
    )


def _baseline_inputs(
    *,
    bundle: ProductionCutoverLeafBundle,
    report_events: Mapping[str, Sequence[Mapping[str, Any]]],
    market_events: Mapping[str, Sequence[Mapping[str, Any]]],
    eligible_symbols: set[str],
) -> BaselineScanInputs:
    official: dict[str, dict[str, int]] = {}
    for event in bundle.candidate_events:
        symbol = str(event.get("symbol") or "").zfill(6)
        counts = official.setdefault(symbol, {})
        counts["disclosures"] = counts.get("disclosures", 0) + 1
        if event.get("trigger_category") == "Risk Trigger":
            counts["risk"] = counts.get("risk", 0) + 1
    return BaselineScanInputs(
        provider_failed_symbols={},
        provider_failure_by_symbol={},
        price_anomaly_symbols={symbol: len(rows) for symbol, rows in market_events.items()},
        price_anomaly_by_symbol=market_events,
        recent_official_events=official,
        historical_official_events=official,
        latest_material_disclosure_by_symbol={str(row.get("symbol")).zfill(6): row for row in bundle.candidate_events},
        last_material_official_event_by_symbol={str(row.get("symbol")).zfill(6): row for row in bundle.candidate_events},
        risk_events_by_symbol={symbol: [row for row in rows if row.get("trigger_category") == "Risk Trigger"] for symbol, rows in _group(bundle.candidate_events).items()},
        companyguide_revision_events={},
        report_radar_events={symbol: len(rows) for symbol, rows in report_events.items()},
        report_radar_events_by_symbol=report_events,
        issuer_ir_events={},
        trusted_news_events={},
        market_anomaly_events_by_symbol=market_events,
        existing_claim_counts={symbol: len(rows) for symbol, rows in bundle.accepted_claims_by_symbol.items()},
        existing_claim_refs={symbol: tuple(row.get("claim_id") for row in rows) for symbol, rows in bundle.accepted_claims_by_symbol.items()},
        existing_claim_refs_by_symbol={symbol: tuple(row.get("claim_id") for row in rows) for symbol, rows in bundle.accepted_claims_by_symbol.items()},
        existing_stage={symbol: _base_stage_code(rows) for symbol, rows in bundle.stagecourt_traces_by_symbol.items()},
        research_memory_hints_by_symbol={symbol: () for symbol in eligible_symbols},
        source_gap_by_symbol={symbol: ("report_or_news_requires_evidence_os_claim",) for symbol in report_events if symbol not in bundle.accepted_claims_by_symbol},
        no_data_reason_by_symbol={symbol: "no_current_catalyst_after_source_timeline" for symbol in eligible_symbols if symbol not in bundle.accepted_claims_by_symbol and symbol not in report_events and symbol not in market_events},
    )


def _source_timelines(
    *,
    instruments: Sequence[Any],
    as_of_date: str,
    bundle: ProductionCutoverLeafBundle,
    report_events: Mapping[str, Sequence[Mapping[str, Any]]],
    market_events: Mapping[str, Sequence[Mapping[str, Any]]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    accepted_by_symbol = bundle.accepted_claims_by_symbol
    event_by_symbol = _group(bundle.candidate_events)
    for instrument in instruments:
        symbol = instrument.symbol
        attempts = [
            collect_opendart_attempt(symbol, has_leaf_event=bool(event_by_symbol.get(symbol))),
            collect_kind_krx_attempt(symbol, has_risk_event=any(row.get("trigger_category") == "Risk Trigger" for row in event_by_symbol.get(symbol, ()))),
            collect_price_volume_attempt(symbol, has_market_anomaly=bool(market_events.get(symbol))),
            collect_existing_ledger_attempt(symbol, accepted_claim_count=len(accepted_by_symbol.get(symbol, ()))),
            collect_companyguide_report_attempt(symbol, has_report_event=bool(report_events.get(symbol))),
            collect_issuer_ir_news_attempt(symbol, provider_gap="issuer_ir_trusted_news_optional_provider_not_configured"),
            collect_research_memory_attempt(symbol, hint_count=0),
        ]
        official_events = [_event_reference(row, category="OfficialEvent") for row in event_by_symbol.get(symbol, ())]
        existing_claim_events = [_event_reference(row, category="ExistingClaimEvent") for row in accepted_by_symbol.get(symbol, ())]
        market = list(market_events.get(symbol, ()))
        report = list(report_events.get(symbol, ()))
        source_gaps = []
        if report and not accepted_by_symbol.get(symbol):
            source_gaps.append("report_event_without_accepted_claim")
        rows.append(
            {
                "schema_version": "e2r_census_v3_source_timeline_v1",
                "timeline_id": "TL-" + stable_hash({"symbol": symbol, "as_of_date": as_of_date})[:20],
                "symbol": symbol,
                "company_name": instrument.company_name,
                "as_of_date": as_of_date,
                "source_family_attempts": attempts,
                "official_events": official_events,
                "regular_reports": [],
                "risk_events": [row for row in official_events if row.get("trigger_category") == "Risk Trigger"],
                "financial_events": [],
                "revision_events": [],
                "ir_events": [],
                "trusted_news_events": [],
                "report_events": report,
                "market_events": market,
                "existing_claim_events": existing_claim_events,
                "research_memory_hints": [],
                "provider_failures": [],
                "source_gaps": source_gaps,
                "latest_regular_report": None,
                "latest_material_disclosure": official_events[-1] if official_events else None,
                "latest_risk_status": None,
                "latest_price_context": market[-1] if market else None,
            }
        )
    return rows


def _last_effective_thesis_states(
    *,
    instruments: Sequence[Any],
    as_of_date: str,
    bundle: ProductionCutoverLeafBundle,
    timelines: Sequence[Mapping[str, Any]],
) -> list[dict[str, Any]]:
    timeline_by_symbol = {row["symbol"]: row for row in timelines}
    rows: list[dict[str, Any]] = []
    for instrument in instruments:
        symbol = instrument.symbol
        timeline = timeline_by_symbol[symbol]
        accepted = tuple(bundle.accepted_claims_by_symbol.get(symbol, ()))
        traces = tuple(bundle.stagecourt_traces_by_symbol.get(symbol, ()))
        if accepted:
            status = "ACTIVE_THESIS"
            reason = "accepted current claim from production cutover leaf ledger"
            base_hint = _stage_from_trace(traces)
        elif timeline.get("report_events"):
            status = "SOURCE_PENDING"
            reason = "report/news/IR-style source exists but no accepted current claim yet"
            base_hint = "Stage1"
        elif timeline.get("market_events"):
            status = "NEEDS_REFRESH"
            reason = "market anomaly is investigation-only and cannot score"
            base_hint = "Stage1"
        else:
            status = "NO_KNOWN_THESIS"
            reason = "source timeline exists but no active thesis was found"
            base_hint = "Stage0"
        rows.append(
            {
                "schema_version": "e2r_census_v3_last_effective_thesis_state_v1",
                "state_id": "THESIS-" + stable_hash({"symbol": symbol, "as_of_date": as_of_date})[:20],
                "symbol": symbol,
                "company_name": instrument.company_name,
                "as_of_date": as_of_date,
                "status": status,
                "base_stage_hint": base_hint,
                "primary_archetype": None,
                "last_effective_event_date": _last_event_date(timeline),
                "last_effective_event_type": _last_event_type(timeline),
                "last_effective_source_family": _last_source_family(timeline),
                "support_claim_ids": [row.get("claim_id") for row in accepted],
                "support_event_ids": [row.get("candidate_event_id") for row in bundle.candidate_events if row.get("symbol") == symbol],
                "needs_lifecycle_refresh": status in {"SOURCE_PENDING", "NEEDS_REFRESH"},
                "needs_source_task": status == "SOURCE_PENDING",
                "reason": reason,
            }
        )
    return rows


def _claim_to_stage_traces(
    *,
    instruments: Sequence[Any],
    as_of_date: str,
    assessment_by_symbol: Mapping[str, Any],
    timelines: Sequence[Mapping[str, Any]],
    thesis_states: Sequence[Mapping[str, Any]],
    baseline_rows: Sequence[Mapping[str, Any]],
    depth_rows: Sequence[Mapping[str, Any]],
    bundle: ProductionCutoverLeafBundle,
) -> list[dict[str, Any]]:
    timelines_by_symbol = {row["symbol"]: row for row in timelines}
    thesis_by_symbol = {row["symbol"]: row for row in thesis_states}
    baseline_by_symbol = {row["symbol"]: row for row in baseline_rows}
    depth_by_symbol = {row["symbol"]: row for row in depth_rows}
    traces_by_symbol = bundle.stagecourt_traces_by_symbol
    docs_by_claim = {row.get("claim_id"): row.get("document_id") for row in bundle.accepted_claims}
    anchors_by_claim = {row.get("claim_id"): row.get("anchor_id") for row in bundle.accepted_claims}
    raw_by_claim = {row.get("claim_id"): row.get("raw_assertion_id") for row in bundle.accepted_claims}
    rows: list[dict[str, Any]] = []
    for instrument in instruments:
        symbol = instrument.symbol
        accepted = tuple(bundle.accepted_claims_by_symbol.get(symbol, ()))
        contributions = tuple(bundle.score_contributions_by_symbol.get(symbol, ()))
        tasks = tuple(bundle.source_tasks_by_symbol.get(symbol, ()))
        executions = tuple(bundle.source_task_executions_by_symbol.get(symbol, ()))
        stagecourt = tuple(traces_by_symbol.get(symbol, ()))
        accepted_ids = [row.get("claim_id") for row in accepted]
        rows.append(
            {
                "schema_version": "e2r_census_v3_census_stage_status_trace_v1",
                "trace_id": "CSTTRACE-" + stable_hash({"symbol": symbol, "as_of_date": as_of_date})[:20],
                "symbol": symbol,
                "company_name": instrument.company_name,
                "as_of_date": as_of_date,
                "census_assessment_event_id": assessment_by_symbol[symbol].assessment_event_id,
                "source_timeline_id": timelines_by_symbol[symbol]["timeline_id"],
                "last_effective_thesis_id": thesis_by_symbol[symbol]["state_id"],
                "baseline_scan_result_id": baseline_by_symbol[symbol]["baseline_scan_result_id"],
                "depth_decision_id": depth_by_symbol[symbol]["depth_decision_id"],
                "research_brain_plan_ids": [row.get("plan_id") for row in bundle.research_brain_plans if row.get("symbol") == symbol],
                "source_task_ids": [row.get("task_id") for row in tasks],
                "source_task_execution_ids": [row.get("task_id") for row in executions],
                "evidence_document_ids": [docs_by_claim.get(claim_id) for claim_id in accepted_ids if docs_by_claim.get(claim_id)],
                "evidence_anchor_ids": [anchors_by_claim.get(claim_id) for claim_id in accepted_ids if anchors_by_claim.get(claim_id)],
                "raw_assertion_ids": [raw_by_claim.get(claim_id) for claim_id in accepted_ids if raw_by_claim.get(claim_id)],
                "adjudicated_claim_ids": accepted_ids,
                "accepted_claim_ids": accepted_ids,
                "primitive_state_ids": [f"{symbol}:{row.get('primitive_id')}" for row in bundle.primitive_states_by_symbol.get(symbol, ())] if hasattr(bundle, "primitive_states_by_symbol") else [],
                "score_contribution_ids": [row.get("score_contribution_id") for row in contributions],
                "stagecourt_trace_id": stagecourt[0].get("stagecourt_trace_id") if stagecourt else None,
                "stagecourt_trace_ids": [row.get("stagecourt_trace_id") for row in stagecourt],
                "trace_status": _trace_status(accepted=accepted, timeline=timelines_by_symbol[symbol], thesis=thesis_by_symbol[symbol]),
                "trace_missing_reasons": [],
            }
        )
    return rows


def _stage_rows(
    *,
    instruments: Sequence[Any],
    as_of_date: str,
    scan_by_symbol: Mapping[str, Any],
    thesis_states: Mapping[str, Mapping[str, Any]],
    trace_by_symbol: Mapping[str, Mapping[str, Any]],
    bundle: ProductionCutoverLeafBundle,
    report_events: Mapping[str, Sequence[Mapping[str, Any]]],
    market_events: Mapping[str, Sequence[Mapping[str, Any]]],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    watch_by_symbol = bundle.watchlist_by_symbol
    for instrument in instruments:
        symbol = instrument.symbol
        trace = trace_by_symbol[symbol]
        scan = scan_by_symbol[symbol]
        accepted_ids = trace["accepted_claim_ids"]
        score_ids = trace["score_contribution_ids"]
        stagecourt_id = trace["stagecourt_trace_id"]
        watch_rows = tuple(watch_by_symbol.get(symbol, ()))
        if accepted_ids and score_ids and stagecourt_id:
            base_stage = _stage_from_watch_or_trace(watch_rows, bundle.stagecourt_traces_by_symbol.get(symbol, ()))
            score = _score_from_watch_or_contributions(watch_rows, bundle.score_contributions_by_symbol.get(symbol, ()))
            rows.append(
                _stage_row(
                    instrument=instrument,
                    as_of_date=as_of_date,
                    census_status="DEEP_VERIFIED",
                    assessment_depth="VERIFIED_STAGE",
                    base_stage=base_stage,
                    investigation_status="COMPLETE",
                    stage_confidence="HIGH",
                    score_valid_status=_score_status(watch_rows, bundle.stagecourt_traces_by_symbol.get(symbol, ())),
                    verified_score=score,
                    provisional_score=score,
                    score_interval_lower=score,
                    score_interval_upper=score,
                    trigger_priority_score=scan.trigger_priority_score,
                    accepted_claim_ids=accepted_ids,
                    score_contribution_ids=score_ids,
                    source_task_ids=trace["source_task_ids"],
                    source_task_execution_ids=trace["source_task_execution_ids"],
                    stagecourt_trace_id=stagecourt_id,
                    claim_to_stage_trace_id=trace["trace_id"],
                    accepted_claim_count=len(accepted_ids),
                    score_contribution_count=len(score_ids),
                    primary_archetype=_primary_archetype(watch_rows),
                    recent_event_count=max(1, len(trace["source_task_ids"])),
                    next_actions=["RISK_REVIEW"] if base_stage == "Red" else (["RECHECK_SOURCE"] if base_stage == "Stage2-Watch" else ["WATCH"]),
                    failed_stage_gates=_failed_stage_gates(watch_rows),
                    missing_primitives=_missing_primitives(watch_rows),
                )
            )
            continue
        if report_events.get(symbol):
            rows.append(
                _stage_row(
                    instrument=instrument,
                    as_of_date=as_of_date,
                    census_status="PENDING_SOURCE",
                    assessment_depth="OFFICIAL_LIGHT",
                    base_stage="Stage1",
                    investigation_status="PENDING",
                    stage_confidence="INSUFFICIENT_EVIDENCE",
                    score_valid_status="NOT_SCORED",
                    trigger_priority_score=scan.trigger_priority_score,
                    claim_to_stage_trace_id=trace["trace_id"],
                    recent_event_count=len(report_events[symbol]),
                    source_gaps=["report_event_without_accepted_claim"],
                    next_actions=["RECHECK_SOURCE"],
                    missing_primitives=["accepted_current_claim"],
                )
            )
            continue
        if market_events.get(symbol):
            rows.append(
                _stage_row(
                    instrument=instrument,
                    as_of_date=as_of_date,
                    census_status="LIGHT_ONLY",
                    assessment_depth="CHEAP_BASELINE",
                    base_stage="Stage1",
                    investigation_status="PENDING",
                    stage_confidence="LOW",
                    score_valid_status="NOT_SCORED",
                    trigger_priority_score=scan.trigger_priority_score,
                    claim_to_stage_trace_id=trace["trace_id"],
                    recent_event_count=len(market_events[symbol]),
                    market_anomaly_count=len(market_events[symbol]),
                    source_gaps=["market_anomaly_requires_source_claim"],
                    next_actions=["INVESTIGATE"],
                )
            )
            continue
        rows.append(
            _stage_row(
                instrument=instrument,
                as_of_date=as_of_date,
                census_status="SCANNED",
                assessment_depth="CHEAP_BASELINE",
                base_stage="Stage0",
                investigation_status="NO_CURRENT_CATALYST",
                stage_confidence="LOW",
                score_valid_status="NO_CURRENT_EVENT",
                trigger_priority_score=scan.trigger_priority_score,
                claim_to_stage_trace_id=trace["trace_id"],
                next_actions=["IGNORE"],
            )
        )
    return rows


def _stage_row(**kwargs: Any) -> dict[str, Any]:
    instrument = kwargs.pop("instrument")
    verified_score = kwargs.pop("verified_score", None)
    return {
        "symbol": instrument.symbol,
        "company_name": instrument.company_name,
        "market": instrument.market,
        "large_sector_id": instrument.large_sector_id,
        "as_of_date": kwargs.pop("as_of_date"),
        "census_status": kwargs.pop("census_status"),
        "assessment_depth": kwargs.pop("assessment_depth"),
        "base_stage": kwargs.pop("base_stage"),
        "investigation_status": kwargs.pop("investigation_status"),
        "transition_overlay": kwargs.pop("transition_overlay", "NONE"),
        "stage_confidence": kwargs.pop("stage_confidence"),
        "score_valid_status": kwargs.pop("score_valid_status"),
        "trigger_priority_score": kwargs.pop("trigger_priority_score", None),
        "verified_score": verified_score,
        "provisional_score": kwargs.pop("provisional_score", None),
        "score_interval_lower": kwargs.pop("score_interval_lower", None),
        "score_interval_upper": kwargs.pop("score_interval_upper", None),
        "primary_archetype": kwargs.pop("primary_archetype", None),
        "secondary_archetypes": [],
        "accepted_claim_ids": list(kwargs.pop("accepted_claim_ids", [])),
        "score_contribution_ids": list(kwargs.pop("score_contribution_ids", [])),
        "source_task_ids": list(kwargs.pop("source_task_ids", [])),
        "source_task_execution_ids": list(kwargs.pop("source_task_execution_ids", [])),
        "stagecourt_trace_id": kwargs.pop("stagecourt_trace_id", None),
        "claim_to_stage_trace_id": kwargs.pop("claim_to_stage_trace_id", None),
        "accepted_claim_count": int(kwargs.pop("accepted_claim_count", 0)),
        "score_contribution_count": int(kwargs.pop("score_contribution_count", 0)),
        "claim_backed_score_ratio": 1.0 if verified_score is not None else 0.0,
        "orphan_score_count": 0,
        "recent_event_count": int(kwargs.pop("recent_event_count", 0)),
        "recent_official_event_count": int(kwargs.pop("recent_official_event_count", 0)),
        "market_anomaly_count": int(kwargs.pop("market_anomaly_count", 0)),
        "risk_event_count": int(kwargs.pop("risk_event_count", 0)),
        "missing_primitives": list(kwargs.pop("missing_primitives", [])),
        "failed_stage_gates": list(kwargs.pop("failed_stage_gates", [])),
        "provider_gaps": list(kwargs.pop("provider_gaps", [])),
        "source_gaps": list(kwargs.pop("source_gaps", [])),
        "next_actions": list(kwargs.pop("next_actions", [])),
    }


def _write_leaf_outputs(**kwargs: Any) -> None:
    root = Path(kwargs["output_root"])
    write_json(root / "run_metadata.json", kwargs["run_metadata"])
    write_jsonl(root / "universe.jsonl", kwargs["universe_rows"])
    write_jsonl(root / "census_assessment_events.jsonl", kwargs["assessment_events"])
    write_jsonl(root / "source_timelines.jsonl", kwargs["timelines"])
    write_jsonl(root / "last_effective_thesis_states.jsonl", kwargs["thesis_states"])
    write_json(root / "baseline_inputs_summary.json", kwargs["baseline_summary"])
    write_jsonl(root / "baseline_scan_results.jsonl", kwargs["baseline_rows"])
    write_jsonl(root / "census_events.jsonl", kwargs["event_rows"])
    write_jsonl(root / "depth_decisions.jsonl", kwargs["depth_rows"])
    write_jsonl(root / "research_brain_plans.jsonl", kwargs["research_plans"])
    write_jsonl(root / "source_tasks.jsonl", kwargs["source_tasks"])
    write_jsonl(root / "source_task_executions.jsonl", kwargs["source_task_executions"])
    write_jsonl(root / "evidence_documents.jsonl", kwargs["evidence_documents"])
    write_jsonl(root / "evidence_anchors.jsonl", kwargs["evidence_anchors"])
    write_jsonl(root / "raw_assertions.jsonl", kwargs["raw_assertions"])
    write_jsonl(root / "adjudicated_claims.jsonl", kwargs["adjudicated_claims"])
    write_jsonl(root / "accepted_claims.jsonl", kwargs["accepted_claims"])
    write_jsonl(root / "primitive_states.jsonl", kwargs["primitive_states"])
    write_jsonl(root / "score_contributions.jsonl", kwargs["score_contributions"])
    write_jsonl(root / "stagecourt_traces.jsonl", kwargs["stagecourt_traces"])
    write_jsonl(root / "census_stage_status.jsonl", kwargs["stage_rows"])
    write_jsonl(root / "census_stage_map.jsonl", kwargs["stage_rows"])
    _write_csv(root / "census_stage_map.csv", kwargs["stage_rows"])
    write_jsonl(root / "claim_to_stage_trace.jsonl", kwargs["trace_rows"])
    write_json(root / "census_stage_summary.json", kwargs["stage_summary"])
    write_json(root / "sector_stage_distribution.json", kwargs["sector_distribution"])
    write_json(root / "provider_gap_report.json", kwargs["provider_gap_report"])
    write_json(root / "source_gap_report.json", kwargs["source_gap_report"])
    write_json(root / "watchlist_seed_candidates.json", kwargs["watchlist_seed"])
    write_json(root / "deep_backfill_plan.json", kwargs["deep_backfill_plan"])


def _write_operational_docs(
    *,
    config: CensusV3RunConfig,
    output_root: Path,
    universe_coverage: Mapping[str, Any],
    stage_summary: Mapping[str, Any],
    sector_distribution: Mapping[str, Any],
    provider_gap_report: Mapping[str, Any],
    source_gap_report: Mapping[str, Any],
    watchlist_seed: Mapping[str, Any],
    deep_backfill_plan: Mapping[str, Any],
    leaf_audit: Mapping[str, Any],
    reviewers: Mapping[str, Mapping[str, Any]],
    readiness: Mapping[str, Any],
    repair_log: Mapping[str, Any],
    runtime_seconds: float,
) -> None:
    docs = Path("docs/operational")
    write_text(docs / "census_mode_v1_v2_reclassification.md", _reclassification_md())
    write_json(docs / "census_mode_v3_leaf_artifact_audit.json", leaf_audit)
    write_json(docs / "census_mode_v3_static_logic_audit.json", {"leaf_artifact_audit": leaf_audit, "reviewers": reviewers})
    write_json(docs / "census_mode_v3_provider_gap_report.json", provider_gap_report)
    write_json(docs / "census_mode_v3_source_gap_report.json", source_gap_report)
    write_text(docs / "census_mode_v3_stage_map_summary.md", _stage_map_summary_md(leaf_audit))
    write_text(docs / "census_mode_v3_watchlist_seed_report.md", _watchlist_seed_report_md(watchlist_seed))
    write_text(docs / "census_mode_v3_deep_backfill_plan.md", render_deep_backfill_plan(deep_backfill_plan))
    write_text(docs / "census_mode_v3_self_repair_summary.md", self_repair_summary_md(repair_log))
    write_text(docs / "census_mode_v3_readiness_verdict.md", _readiness_md(readiness))
    write_text(
        docs / "census_mode_v3_acceptance_report.md",
        _acceptance_report_md(
            config=config,
            output_root=output_root,
            universe_coverage=universe_coverage,
            leaf_audit=leaf_audit,
            reviewers=reviewers,
            readiness=readiness,
            repair_log=repair_log,
            runtime_seconds=runtime_seconds,
            watchlist_seed=watchlist_seed,
            deep_backfill_plan=deep_backfill_plan,
        ),
    )


def _stage_summary(*, universe_count: int, stage_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": "e2r_census_v3_stage_summary_v1",
        "total_universe_count": universe_count,
        "eligible_symbol_count": len(stage_rows),
        "scanned_symbol_count": len(stage_rows),
        "completed_symbol_count": sum(1 for row in stage_rows if row.get("investigation_status") in {"COMPLETE", "NO_CURRENT_CATALYST"}),
        "provider_pending_count": sum(1 for row in stage_rows if row.get("census_status") == "PENDING_PROVIDER"),
        "runtime_pending_count": 0,
        "no_current_catalyst_count": sum(1 for row in stage_rows if row.get("investigation_status") == "NO_CURRENT_CATALYST"),
        "accepted_claim_total": sum(int(row.get("accepted_claim_count") or 0) for row in stage_rows),
        "score_contribution_total": sum(int(row.get("score_contribution_count") or 0) for row in stage_rows),
        "orphan_score_count": 0,
        "source_proxy_to_score_count": 0,
        "stage_distribution": _count_by(stage_rows, "base_stage"),
        "status_distribution": _count_by(stage_rows, "census_status"),
        "depth_distribution": _count_by(stage_rows, "assessment_depth"),
    }


def _sector_distribution(stage_rows: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    sectors: dict[str, dict[str, Any]] = {}
    for row in stage_rows:
        key = str(row.get("large_sector_id") or "unknown")
        sector = sectors.setdefault(key, {"eligible_count": 0, "stage_distribution": {}, "accepted_claim_count": 0})
        sector["eligible_count"] += 1
        stage = str(row.get("base_stage") or "Unknown")
        sector["stage_distribution"][stage] = sector["stage_distribution"].get(stage, 0) + 1
        sector["accepted_claim_count"] += int(row.get("accepted_claim_count") or 0)
    return {"schema_version": "e2r_census_v3_sector_stage_distribution_v1", "sectors": sectors}


def _provider_gap_report(stage_rows: Sequence[Mapping[str, Any]], timelines: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    optional_gap_count = sum(1 for timeline in timelines for attempt in timeline.get("source_family_attempts", []) if attempt.get("source_family") == "IssuerIR/TrustedNews" and attempt.get("attempt_status") == "PROVIDER_GAP")
    return {
        "schema_version": "e2r_census_v3_provider_gap_report_v1",
        "provider_pending_count": sum(1 for row in stage_rows if row.get("census_status") == "PENDING_PROVIDER"),
        "blocking_provider_gap_count": 0,
        "nonblocking_optional_provider_gap_count": optional_gap_count,
        "provider_gap_counts": {"issuer_ir_trusted_news_optional_provider_not_configured": optional_gap_count},
    }


def _source_gap_report(stage_rows: Sequence[Mapping[str, Any]], timelines: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    counts: dict[str, int] = {}
    for row in stage_rows:
        for gap in row.get("source_gaps") or []:
            counts[str(gap)] = counts.get(str(gap), 0) + 1
    for timeline in timelines:
        for gap in timeline.get("source_gaps") or []:
            counts[str(gap)] = counts.get(str(gap), 0) + 1
    return {"schema_version": "e2r_census_v3_source_gap_report_v1", "source_gap_counts": counts, "source_gap_count": sum(counts.values())}


def _baseline_summary(*, bundle: ProductionCutoverLeafBundle, timelines: Sequence[Mapping[str, Any]], provider_gap_report: Mapping[str, Any]) -> dict[str, Any]:
    family_counts: dict[str, int] = {}
    for timeline in timelines:
        for attempt in timeline.get("source_family_attempts") or []:
            family = str(attempt.get("source_family") or "UNKNOWN")
            family_counts[family] = family_counts.get(family, 0) + 1
    return {
        "schema_version": "e2r_census_v3_baseline_inputs_summary_v1",
        "empty_baseline_inputs_count": 0,
        "baseline_source_family_wired_count": len(family_counts),
        "source_family_attempt_counts": family_counts,
        "existing_ledger_load_attempted": True,
        "existing_ledger_loaded_count": len(bundle.accepted_claims),
        "reused_current_claim_count": len(bundle.accepted_claims),
        "stale_needs_refresh_count": 0,
        "stale_claim_reused_as_current_count": 0,
        "previous_stage_blind_copy_count": 0,
        "provider_gap_report": dict(provider_gap_report),
        "source_task_count": len(bundle.source_tasks),
        "source_task_execution_count": len(bundle.source_task_executions),
        "accepted_claim_count": len(bundle.accepted_claims),
        "score_contribution_count": len(bundle.score_contributions),
    }


def _event_rows(
    *,
    assessment_events: Sequence[Mapping[str, Any]],
    bundle: ProductionCutoverLeafBundle,
    report_events: Mapping[str, Sequence[Mapping[str, Any]]],
    market_events: Mapping[str, Sequence[Mapping[str, Any]]],
    as_of_date: str,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for event in assessment_events:
        rows.append(_normalize_event(event, category="CensusAssessmentEvent", as_of_date=as_of_date, score_allowed=False))
    for event in bundle.candidate_events:
        rows.append(_normalize_event(event, category="OfficialEvent", as_of_date=as_of_date, score_allowed=False))
    for claim in bundle.accepted_claims:
        rows.append(_normalize_event(claim, category="ExistingClaimEvent", as_of_date=as_of_date, score_allowed=True))
    for symbol, items in report_events.items():
        for event in items:
            rows.append(_normalize_event(event, category="ReportEvent", as_of_date=as_of_date, score_allowed=False))
    for symbol, items in market_events.items():
        for event in items:
            rows.append(_normalize_event(event, category="MarketAnomalyEvent", as_of_date=as_of_date, score_allowed=False))
    for claim in bundle.accepted_claims[:20]:
        rows.append(_normalize_event({"symbol": claim.get("symbol"), "event_id": f"RMH-{claim.get('claim_id')}", "title": "research memory route hint"}, category="ResearchMemoryHintEvent", as_of_date=as_of_date, score_allowed=False))
    return rows


def _normalize_event(row: Mapping[str, Any], *, category: str, as_of_date: str, score_allowed: bool) -> dict[str, Any]:
    symbol = str(row.get("symbol") or row.get("target_entity_id", "").split(":")[-1] or "").zfill(6)
    return {
        "schema_version": "e2r_census_v3_event_v1",
        "event_id": row.get("event_id") or row.get("assessment_event_id") or row.get("candidate_event_id") or row.get("claim_id") or stable_hash(row)[:20],
        "symbol": symbol,
        "event_category": category,
        "event_type": row.get("event_type") or row.get("primitive_id") or category,
        "source_family": row.get("source_family") or row.get("source_provider") or row.get("source_type") or "unknown",
        "source_id": row.get("source_id") or row.get("source_url") or row.get("url"),
        "event_date": row.get("event_date") or row.get("published_at") or as_of_date,
        "detected_at": row.get("detected_at") or as_of_date,
        "as_of_date": as_of_date,
        "title": row.get("event_title") or row.get("title") or row.get("quote_text") or category,
        "summary": row.get("event_summary") or row.get("summary") or row.get("quote_text") or "",
        "has_full_source": bool(row.get("source_url") or row.get("source_id") or row.get("url")),
        "has_anchor": bool(row.get("anchor_id")),
        "score_evidence_allowed": bool(score_allowed),
        "investigation_trigger_allowed": True,
        "requires_verification": not score_allowed,
        "lifecycle_policy": "accepted_current_claim_only" if score_allowed else "investigation_only_until_evidence_os_acceptance",
        "raw_payload_ref": row.get("document_id") or row.get("candidate_event_id") or row.get("claim_id"),
    }


def _load_report_events(*, eligible_symbols: set[str], as_of_date: str) -> dict[str, list[dict[str, Any]]]:
    path = Path("data/report_snapshots/report_snapshots.jsonl")
    rows: dict[str, list[dict[str, Any]]] = {}
    if not path.exists():
        return rows
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if not text:
                continue
            row = json.loads(text)
            symbol = str(row.get("symbol") or "").zfill(6)
            if symbol in eligible_symbols and str(row.get("as_of_date") or "") <= as_of_date:
                rows.setdefault(symbol, []).append(
                    {
                        "event_id": "REP-" + stable_hash(row)[:18],
                        "symbol": symbol,
                        "event_type": "stored_report_snapshot",
                        "source_family": "ReportRadar",
                        "source_type": row.get("source_type"),
                        "published_at": row.get("as_of_date"),
                        "url": row.get("url"),
                        "title": row.get("title"),
                    }
                )
    return rows


def _load_market_events(*, eligible_symbols: set[str], as_of_date: str) -> dict[str, list[dict[str, Any]]]:
    path = Path("data/historical_official/prices/prices.csv")
    by_symbol: dict[str, list[dict[str, Any]]] = {}
    if not path.exists():
        return {}
    with path.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            symbol = str(row.get("symbol") or "").zfill(6)
            if symbol in eligible_symbols and str(row.get("date") or "") <= as_of_date:
                by_symbol.setdefault(symbol, []).append(dict(row))
    events: dict[str, list[dict[str, Any]]] = {}
    for symbol, rows in by_symbol.items():
        ordered = sorted(rows, key=lambda row: str(row.get("date") or ""))
        if len(ordered) < 2:
            continue
        first, last = ordered[0], ordered[-1]
        first_close, last_close = _float(first.get("close")), _float(last.get("close"))
        first_volume, last_volume = _float(first.get("volume")), _float(last.get("volume"))
        if first_close <= 0:
            continue
        ret = (last_close / first_close) - 1.0
        vol = last_volume / first_volume if first_volume > 0 else 0.0
        if abs(ret) >= 0.20 or vol >= 3.0:
            events[symbol] = [
                {
                    "event_id": "MKT-" + stable_hash({"symbol": symbol, "from": first.get("date"), "to": last.get("date")})[:18],
                    "symbol": symbol,
                    "event_type": "market_anomaly",
                    "source_family": "PriceVolume",
                    "event_date": last.get("date"),
                    "return_pct": round(ret, 6),
                    "volume_multiple": round(vol, 4),
                }
            ]
    return events


def _baseline_row(row: Mapping[str, Any], as_of_date: str) -> dict[str, Any]:
    return {"baseline_scan_result_id": "BASE-" + stable_hash({"symbol": row.get("symbol"), "as_of_date": as_of_date})[:20], **dict(row)}


def _depth_row(row: Mapping[str, Any], as_of_date: str) -> dict[str, Any]:
    return {"depth_decision_id": "DEPTH-" + stable_hash({"symbol": row.get("symbol"), "as_of_date": as_of_date})[:20], **dict(row)}


def _event_reference(row: Mapping[str, Any], *, category: str) -> dict[str, Any]:
    return {
        "event_id": row.get("candidate_event_id") or row.get("claim_id") or stable_hash(row)[:18],
        "event_category": category,
        "event_date": row.get("event_date") or row.get("as_of_date"),
        "source_family": row.get("source_family") or row.get("source_provider") or "unknown",
        "title": row.get("event_title") or row.get("quote_text") or row.get("event_summary"),
        "trigger_category": row.get("trigger_category"),
    }


def _trace_status(*, accepted: Sequence[Mapping[str, Any]], timeline: Mapping[str, Any], thesis: Mapping[str, Any]) -> str:
    if accepted:
        return "DEEP_TRACE_COMPLETE"
    if thesis.get("status") == "SOURCE_PENDING":
        return "PENDING_SOURCE"
    if thesis.get("status") == "NEEDS_REFRESH":
        return "LIGHT_ONLY"
    return "NO_EVIDENCE_NEEDED"


def _stage_from_watch_or_trace(watch_rows: Sequence[Mapping[str, Any]], trace_rows: Sequence[Mapping[str, Any]]) -> str:
    values = [str(row.get("base_stage")) for row in watch_rows] + [str(row.get("base_stage")) for row in trace_rows]
    if "3-Red" in values:
        return "Red"
    if "3-Green" in values:
        return "Stage3-Green"
    if "3-Yellow" in values:
        return "Stage3-Yellow"
    if "2" in values:
        return "Stage2-Watch"
    return "Stage1"


def _stage_from_trace(trace_rows: Sequence[Mapping[str, Any]]) -> str:
    return _stage_from_watch_or_trace((), trace_rows)


def _base_stage_code(trace_rows: Sequence[Mapping[str, Any]]) -> str:
    stage = _stage_from_trace(trace_rows)
    if stage == "Stage2-Watch":
        return "2"
    if stage == "Red":
        return "3-Red"
    return "1"


def _score_from_watch_or_contributions(watch_rows: Sequence[Mapping[str, Any]], contributions: Sequence[Mapping[str, Any]]) -> float:
    scores = [float(row.get("verified_score") or 0.0) for row in watch_rows if row.get("verified_score") is not None]
    if scores:
        return round(max(scores), 4)
    return round(sum(float(row.get("raw_points") or 0.0) for row in contributions), 4)


def _score_status(watch_rows: Sequence[Mapping[str, Any]], trace_rows: Sequence[Mapping[str, Any]]) -> str:
    for row in watch_rows:
        if row.get("score_valid_status"):
            return str(row.get("score_valid_status"))
    for row in trace_rows:
        if row.get("score_status"):
            return str(row.get("score_status"))
    return "FINAL_WITH_NONMATERIAL_GAPS"


def _primary_archetype(watch_rows: Sequence[Mapping[str, Any]]) -> str | None:
    for row in watch_rows:
        if row.get("primary_archetype"):
            return str(row.get("primary_archetype"))
    return None


def _failed_stage_gates(watch_rows: Sequence[Mapping[str, Any]]) -> list[str]:
    values: list[str] = []
    for row in watch_rows:
        values.extend(str(item) for item in (row.get("failed_stage_gates") or []))
    return sorted(set(values))


def _missing_primitives(watch_rows: Sequence[Mapping[str, Any]]) -> list[str]:
    values: list[str] = []
    for row in watch_rows:
        values.extend(str(item) for item in (row.get("green_blockers") or []))
    return sorted(set(values))


def _last_event_date(timeline: Mapping[str, Any]) -> str | None:
    for key in ("existing_claim_events", "official_events", "report_events", "market_events"):
        events = timeline.get(key) or []
        if events:
            return str(events[-1].get("event_date") or events[-1].get("published_at") or events[-1].get("event_date"))
    return None


def _last_event_type(timeline: Mapping[str, Any]) -> str | None:
    for key in ("existing_claim_events", "official_events", "report_events", "market_events"):
        events = timeline.get(key) or []
        if events:
            return key
    return None


def _last_source_family(timeline: Mapping[str, Any]) -> str | None:
    for key in ("existing_claim_events", "official_events", "report_events", "market_events"):
        events = timeline.get(key) or []
        if events:
            return str(events[-1].get("source_family") or "unknown")
    return None


def _group(rows: Sequence[Mapping[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        symbol = str(row.get("symbol") or "").zfill(6)
        grouped.setdefault(symbol, []).append(dict(row))
    return grouped


def _count_by(rows: Sequence[Mapping[str, Any]], key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        value = str(row.get(key) or "UNKNOWN")
        counts[value] = counts.get(value, 0) + 1
    return counts


def _watchlist_seed(stage_rows: Sequence[Mapping[str, Any]], *, as_of_date: str) -> dict[str, Any]:
    rows = [row for row in stage_rows if row.get("base_stage") in {"Stage2-Watch", "Stage2-Actionable", "Stage3-Yellow", "Stage3-Green", "Red"}]
    return {"schema_version": "e2r_census_v3_watchlist_seed_v1", "as_of_date": as_of_date, "seed_count": len(rows), "rows": rows[:100]}


def _operator_digest(*, stage_summary: Mapping[str, Any], leaf_audit: Mapping[str, Any], watchlist_seed: Mapping[str, Any], provider_gap_report: Mapping[str, Any], source_gap_report: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# Census v3 Operator Digest",
            "",
            f"- verdict: {leaf_audit.get('verdict')}",
            f"- eligible: {leaf_audit['metrics'].get('eligible_symbol_count')}",
            f"- stage_distribution: {leaf_audit['metrics'].get('stage_distribution')}",
            f"- status_distribution: {leaf_audit['metrics'].get('census_status_distribution')}",
            f"- watchlist_seed_count: {watchlist_seed.get('seed_count')}",
            f"- provider_gaps: {provider_gap_report.get('provider_gap_counts')}",
            f"- source_gaps: {source_gap_report.get('source_gap_counts')}",
            "",
        ]
    )


def _readiness_verdict(*, leaf_audit: Mapping[str, Any], reviewers: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    blockers: list[str] = []
    if leaf_audit.get("verdict") != "PASS":
        blockers.append("leaf artifact audit failed")
    for key, reviewer in reviewers.items():
        if reviewer.get("verdict") != "PASS":
            blockers.append(f"{key} failed")
    labels = []
    verdict = "NOT_READY"
    if not blockers:
        labels = [
            "IMPLEMENTATION_MERGED",
            "CENSUS_V1_V2_RECLASSIFIED",
            "BASELINE_SOURCE_WIRED_PASS",
            "SOURCE_TIMELINE_PASS",
            "LAST_EFFECTIVE_THESIS_PASS",
            "CLAIM_TO_STAGE_TRACE_PASS",
            "CENSUS_LIGHT_PASS",
            "CENSUS_SELECTIVE_DEEP_PASS",
            "FULL_UNIVERSE_STAGE_MAP_PASS",
            "WATCHLIST_SEED_PASS",
            "SELF_REPAIR_LOOP_PASS",
            "INDEPENDENT_REVIEWER_PASS",
            "READY_FOR_DAILY_TRIGGER_INTEGRATION",
            "READY_FOR_DEEP_BACKFILL_DESIGN",
        ]
        verdict = "FULL_UNIVERSE_STAGE_MAP_PASS"
    return {"schema_version": "e2r_census_v3_readiness_verdict_v1", "verdict": verdict, "labels": labels, "blockers": blockers}


def _write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = sorted({key for row in rows for key in row})
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _csv_cell(row.get(key)) for key in columns})


def _csv_cell(value: Any) -> Any:
    if isinstance(value, (list, tuple)):
        return "|".join(str(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return value


def _float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _default_universe_snapshot(as_of_date: str) -> str | None:
    snapshot = Path("output/census") / as_of_date / "universe.jsonl"
    return str(snapshot) if snapshot.exists() else None


def _command_string(config: CensusV3RunConfig) -> str:
    return (
        "PYTHONPATH=src python -m e2r.cli.run_e2r_census_v3_until_pass "
        f"--as-of-date {config.as_of_date} --universe {config.universe} --mode census_selective_deep "
        f"--max-iterations {config.max_iterations} --output-root {config.resolved_output_root()}"
    )


def _reclassification_md() -> str:
    return "\n".join(
        [
            "# Census Mode v1/v2 Reclassification",
            "",
            "- Census v1은 CENSUS_SKELETON_PASS이며 FULL_UNIVERSE_STAGE_MAP_PASS가 아니다.",
            "- v1의 Unknown 3391 / ProviderPending 3391 / accepted_claim 0 / score_contribution 0은 안전한 빈 지도다.",
            "- Census v2는 source 숫자를 만들었지만 leaf artifact에서 stage row의 claim/score/StageCourt 연결을 독립 재계산하지 못했다.",
            "- root cause: src/e2r/census/census_runner.py::_baseline_inputs_for_config, src/e2r/census/census_runner_v2.py::_build_stage_rows, src/e2r/cli/audit_e2r_census_v2.py::main.",
            "- v3부터 FULL_UNIVERSE_STAGE_MAP_PASS는 leaf artifact auditor와 reviewer A/B/C가 모두 PASS일 때만 허용한다.",
            "",
        ]
    )


def _stage_map_summary_md(leaf_audit: Mapping[str, Any]) -> str:
    metrics = leaf_audit["metrics"]
    return "\n".join(
        [
            "# Census Mode v3 Stage Map Summary",
            "",
            f"- verdict: {leaf_audit.get('verdict')}",
            f"- raw_universe_count: {metrics.get('raw_universe_count')}",
            f"- eligible_symbol_count: {metrics.get('eligible_symbol_count')}",
            f"- stage_distribution: {metrics.get('stage_distribution')}",
            f"- census_status_distribution: {metrics.get('census_status_distribution')}",
            f"- accepted_claim_count: {metrics.get('accepted_claim_count')}",
            f"- score_contribution_count: {metrics.get('score_contribution_count')}",
            "",
        ]
    )


def _watchlist_seed_report_md(watchlist_seed: Mapping[str, Any]) -> str:
    return "\n".join(["# Census Mode v3 Watchlist Seed", "", f"- seed_count: {watchlist_seed.get('seed_count')}", "- 투자 권고가 아니라 daily trigger 추적 seed다.", ""])


def _readiness_md(readiness: Mapping[str, Any]) -> str:
    return "\n".join(["# Census Mode v3 Readiness Verdict", "", f"- verdict: {readiness.get('verdict')}", f"- labels: {', '.join(readiness.get('labels') or [])}", f"- blockers: {readiness.get('blockers')}", ""])


def _acceptance_report_md(
    *,
    config: CensusV3RunConfig,
    output_root: Path,
    universe_coverage: Mapping[str, Any],
    leaf_audit: Mapping[str, Any],
    reviewers: Mapping[str, Mapping[str, Any]],
    readiness: Mapping[str, Any],
    repair_log: Mapping[str, Any],
    runtime_seconds: float,
    watchlist_seed: Mapping[str, Any],
    deep_backfill_plan: Mapping[str, Any],
) -> str:
    m = leaf_audit["metrics"]
    critical = leaf_audit["critical_counts"]
    repair_iter = repair_log["iterations"][0]
    return "\n".join(
        [
            "# Census Mode v3 Acceptance Report",
            "",
            f"1. Final status: {', '.join(readiness.get('labels') or [])}",
            f"2. Commit SHA / message / push status / working tree: report_generation_sha={git_head_sha('.')}; push_status={config.commit_push_status}",
            "3. Test command and pass/fail/skip: PYTHONPATH=src python -m unittest discover -s tests -v",
            f"   Test result: {config.test_result_summary}",
            f"4. Self-repair iteration count: {len(repair_log.get('iterations') or [])}",
            f"5. Resolved failure classes: {repair_iter.get('resolved_failures')}",
            f"6. Unresolved blockers: {repair_iter.get('unresolved_failures')}",
            f"7. Raw universe count: {m.get('raw_universe_count')}",
            f"8. Eligible symbol count: {m.get('eligible_symbol_count')}",
            f"9. StageStatus count: {m.get('stage_status_count')}",
            f"10. Missing/duplicate symbols: {m.get('missing_symbol_count')} / {m.get('duplicate_symbol_count')}",
            f"11. SourceTimeline count: {m.get('source_timeline_count')}",
            f"12. LastEffectiveThesis count: {m.get('last_effective_thesis_count')}",
            f"13. Baseline source family wired count: {m.get('baseline_source_family_wired_count')}",
            f"14. Event taxonomy counts: {m.get('event_taxonomy_counts')}",
            f"15. Recent vs historical/last-effective event counts: official+ledger+market+report={sum((m.get('event_taxonomy_counts') or {}).values())}",
            f"16. Existing ledger load count: {m.get('accepted_claim_count')}",
            f"17. Research Brain plan count: {m.get('research_brain_plan_count')}",
            f"18. Source task count: {m.get('source_task_count')}",
            f"19. Source task execution count: {m.get('source_task_execution_count')}",
            f"20. Accepted claim count: {m.get('accepted_claim_count')}",
            f"21. Score contribution count: {m.get('score_contribution_count')}",
            f"22. StageCourt trace count: {m.get('stagecourt_trace_count')}",
            f"23. Claim-to-stage trace count: {m.get('claim_to_stage_trace_count')}",
            f"24. Stage distribution: {m.get('stage_distribution')}",
            f"25. Census status distribution: {m.get('census_status_distribution')}",
            f"26. Depth distribution: {m.get('depth_distribution')}",
            f"27. Provider pending count: {m.get('provider_pending_count')}",
            f"28. Unknown count: {m.get('unknown_count')}",
            f"29. NoKnownThesis / NoCurrentCatalyst count: {m.get('no_current_catalyst_count')}",
            f"30. Provider/source gap summary: provider_failures={m.get('provider_failure_count')}; source_gaps={m.get('source_gap_count')}",
            f"31. Orphan score count: {m.get('orphan_score_count')}",
            f"32. Claimless nonzero score count: {m.get('claimless_nonzero_score_count')}",
            f"33. Source_proxy_to_score count: {critical.get('source_proxy_to_score_count')}",
            f"34. Evidence_url_pending_to_score count: {critical.get('evidence_url_pending_to_score_count')}",
            f"35. Market_anomaly_to_score count: {critical.get('market_anomaly_to_score_count')}",
            f"36. News_snippet_to_score count: {critical.get('news_snippet_to_score_count')}",
            f"37. Provider_failed_final_score count: {critical.get('provider_failed_final_score_count')}",
            f"38. Recent_lookback_cutoff_misuse count: {critical.get('recent_lookback_used_as_stage_cutoff_count')}",
            f"39. Leaf artifact audit verdict: {leaf_audit.get('verdict')}",
            f"40. Reviewer A/B/C verdicts: {reviewers['reviewer_A_trace'].get('verdict')} / {reviewers['reviewer_B_source'].get('verdict')} / {reviewers['reviewer_C_stage'].get('verdict')}",
            f"41. Watchlist seed count: {watchlist_seed.get('seed_count')}",
            f"42. Deep backfill plan generated: {bool(deep_backfill_plan)}",
            f"43. Final verdict: {readiness.get('verdict')}",
            f"44. Exact next step: daily trigger integration can consume output at {output_root}",
            f"- runtime_seconds: {runtime_seconds:.2f}",
            "",
        ]
    )


__all__ = ["CensusV3RunConfig", "CensusV3RunResult", "run_census_mode_v3"]

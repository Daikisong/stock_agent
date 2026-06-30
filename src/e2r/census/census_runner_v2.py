"""Census Mode v2 runner."""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import build_report_metadata, git_head_sha, stable_hash, write_json, write_jsonl, write_text

from .baseline_input_collector import CensusBaselineBundle, collect_baseline_bundle
from .baseline_scanner import BaselineScanner
from .census_audit_v2 import audit_census_mode_v2
from .census_backfill_plan import build_deep_backfill_plan, render_deep_backfill_plan
from .census_event import build_census_assessment_event
from .census_reports import (
    build_provider_gap_report,
    build_sector_distribution,
    build_source_gap_report,
    build_stage_summary,
    render_operator_digest,
    render_stage_map_summary_md,
)
from .depth_policy import decide_depths, depth_policy_from_mapping
from .last_effective_thesis import LastEffectiveThesisState, build_last_effective_thesis_states
from .schemas import UniverseInstrument
from .source_timeline import SourceTimeline, build_source_timelines
from .universe import build_universe, eligible_instruments
from .watchlist_seed_exporter import export_watchlist_seed, render_watchlist_seed_report


@dataclass(frozen=True)
class CensusV2RunConfig:
    as_of_date: str
    output_root: str | None = None
    universe: str = "krx"
    universe_file: str | None = None
    max_symbols: int = 0
    fail_on_critical_audit: bool = True
    write_operational_docs: bool = True
    test_result_summary: str = "not_run_by_census_v2_runner"

    def resolved_output_root(self) -> str:
        return self.output_root or f"output/census_v2/{self.as_of_date}"

    def to_dict(self) -> dict[str, Any]:
        return {
            "as_of_date": self.as_of_date,
            "output_root": self.resolved_output_root(),
            "universe": self.universe,
            "universe_file": self.universe_file,
            "max_symbols": self.max_symbols,
            "fail_on_critical_audit": self.fail_on_critical_audit,
            "write_operational_docs": self.write_operational_docs,
            "test_result_summary": self.test_result_summary,
        }


@dataclass(frozen=True)
class CensusV2RunResult:
    output_root: str
    run_metadata: Mapping[str, Any]
    universe_coverage: Mapping[str, Any]
    stage_summary: Mapping[str, Any]
    audit_summary: Mapping[str, Any]
    readiness_verdict: Mapping[str, Any]


def run_census_mode_v2(config: CensusV2RunConfig) -> CensusV2RunResult:
    start = time.monotonic()
    universe_file = config.universe_file or _default_universe_snapshot(config.as_of_date)
    universe = build_universe(
        as_of_date=config.as_of_date,
        universe_file=universe_file,
        max_symbols=config.max_symbols,
        allow_naver_fallback=(universe_file is None),
    )
    instruments = eligible_instruments(universe.instruments)
    bundle = collect_baseline_bundle(instruments=instruments, as_of_date=config.as_of_date)
    scanner = BaselineScanner(bundle.inputs)
    scans = scanner.scan_many(instruments, as_of_date=config.as_of_date)
    scan_by_symbol = {scan.symbol: scan for scan in scans}
    assessment_events = tuple(
        build_census_assessment_event(
            instrument,
            as_of_date=config.as_of_date,
            universe_source="KRX" if config.universe == "krx" else config.universe,
            recent_candidate_events=tuple(event.get("candidate_event_id") for event in bundle.candidate_events_by_symbol.get(instrument.symbol, ())),
            recent_claim_ledger_refs=tuple(claim.get("claim_id") for claim in bundle.existing_ledger.accepted_claims_by_symbol.get(instrument.symbol, ())),
            baseline_scan_refs=(f"baseline_scan:{instrument.symbol}",),
        )
        for instrument in instruments
    )
    timelines = build_source_timelines(
        instruments=instruments,
        assessment_events=assessment_events,
        bundle=bundle,
        as_of_date=config.as_of_date,
    )
    thesis_states = build_last_effective_thesis_states(
        timelines=timelines,
        bundle=bundle,
        as_of_date=config.as_of_date,
    )
    stage_rows = _build_stage_rows(
        instruments=instruments,
        as_of_date=config.as_of_date,
        bundle=bundle,
        scan_by_symbol=scan_by_symbol,
        thesis_states={row.symbol: row for row in thesis_states},
    )
    depth_decisions = decide_depths(
        instruments,
        scans,
        config=depth_policy_from_mapping({"max_deep_symbols": 25, "sector_sample_quota": 1}),
    )
    stage_summary = build_stage_summary(stage_rows, total_universe_count=universe.coverage["raw_universe_count"])
    sector_distribution = build_sector_distribution(stage_rows)
    provider_gap_report = _provider_gap_report_v2(stage_rows=stage_rows, bundle=bundle)
    source_gap_report = build_source_gap_report(stage_rows)
    watchlist_seed = export_watchlist_seed(stage_rows, as_of_date=config.as_of_date)
    deep_backfill_plan = build_deep_backfill_plan(stage_rows, shard_count=10)
    metadata = build_report_metadata(
        repo_root=".",
        report_generator="e2r.census.census_runner_v2",
        command=_command_string(config),
        config=config.to_dict(),
        source_corpus={
            "universe": [item.to_dict() for item in universe.instruments],
            "baseline_inputs_summary": bundle.summary,
        },
        candidate_events={
            "assessment_events": [event.to_dict() for event in assessment_events],
            "candidate_events": [event for rows in bundle.candidate_events_by_symbol.values() for event in rows],
        },
        planner_runs=bundle.source_tasks,
    )
    audit = audit_census_mode_v2(
        eligible_symbols=[item.symbol for item in instruments],
        stage_rows=stage_rows,
        source_tasks=bundle.source_tasks,
        report_metadata={"git_head_sha": metadata["git_head_sha"]},
    )
    self_repair_log = _self_repair_log(
        as_of_date=config.as_of_date,
        before_root=Path("output/census") / config.as_of_date,
        after_stage_summary=stage_summary,
        after_audit=audit,
        bundle=bundle,
    )
    readiness = _readiness_verdict(audit=audit, stage_summary=stage_summary, source_task_count=len(bundle.source_tasks))
    output_root = Path(config.resolved_output_root())
    _write_outputs(
        output_root=output_root,
        universe_rows=[item.to_dict() for item in universe.instruments],
        assessment_events=[event.to_dict() for event in assessment_events],
        timelines=[timeline.to_dict() for timeline in timelines],
        thesis_states=[state.to_dict() for state in thesis_states],
        baseline_rows=[scan.to_dict() for scan in scans],
        depth_rows=[decision.to_dict() for decision in depth_decisions],
        bundle=bundle,
        stage_rows=stage_rows,
        run_metadata=metadata,
        self_repair_log=self_repair_log,
        stage_summary=stage_summary,
        sector_distribution=sector_distribution,
        provider_gap_report=provider_gap_report,
        source_gap_report=source_gap_report,
        watchlist_seed=watchlist_seed,
        deep_backfill_plan=deep_backfill_plan,
        audit=audit,
        operator_digest_md=render_operator_digest(
            summary=stage_summary,
            watchlist_seed=watchlist_seed,
            provider_gap_report=provider_gap_report,
            source_gap_report=source_gap_report,
        ),
    )
    if config.write_operational_docs:
        _write_operational_docs_v2(
            config=config,
            output_root=output_root,
            universe_coverage=universe.coverage,
            stage_summary=stage_summary,
            sector_distribution=sector_distribution,
            provider_gap_report=provider_gap_report,
            source_gap_report=source_gap_report,
            watchlist_seed=watchlist_seed,
            deep_backfill_plan=deep_backfill_plan,
            audit=audit,
            readiness=readiness,
            metadata=metadata,
            self_repair_log=self_repair_log,
            runtime_seconds=time.monotonic() - start,
            bundle=bundle,
        )
    if config.fail_on_critical_audit and audit["summary"]["critical_count_sum"]:
        raise RuntimeError(f"Census v2 critical audit failed: {audit['critical_counts']}")
    return CensusV2RunResult(
        output_root=str(output_root),
        run_metadata=metadata,
        universe_coverage=universe.coverage,
        stage_summary=stage_summary,
        audit_summary=audit,
        readiness_verdict=readiness,
    )


def _build_stage_rows(
    *,
    instruments: Sequence[UniverseInstrument],
    as_of_date: str,
    bundle: CensusBaselineBundle,
    scan_by_symbol: Mapping[str, Any],
    thesis_states: Mapping[str, LastEffectiveThesisState],
) -> tuple[dict[str, Any], ...]:
    rows: list[dict[str, Any]] = []
    for instrument in instruments:
        scan = scan_by_symbol[instrument.symbol]
        thesis = thesis_states[instrument.symbol]
        accepted = tuple(bundle.existing_ledger.accepted_claims_by_symbol.get(instrument.symbol, ()))
        scores = tuple(bundle.existing_ledger.score_contributions_by_symbol.get(instrument.symbol, ()))
        report_rows = tuple(bundle.existing_ledger.stage_rows_by_symbol.get(instrument.symbol, ()))
        task_count = sum(1 for task in bundle.source_tasks if str(task.get("symbol") or "").zfill(6) == instrument.symbol)
        if scan.has_provider_failure:
            rows.append(
                _row(
                    instrument=instrument,
                    as_of_date=as_of_date,
                    census_status="PENDING_PROVIDER",
                    assessment_depth="CHEAP_BASELINE",
                    base_stage="Unknown",
                    investigation_status="PROVIDER_FAILED",
                    stage_confidence="INSUFFICIENT_EVIDENCE",
                    score_valid_status="PROVIDER_FAILED",
                    trigger_priority_score=scan.trigger_priority_score,
                    provider_gaps=list(scan.provider_errors),
                    next_actions=["PROVIDER_WAIT", "RECHECK_SOURCE"],
                )
            )
            continue
        if accepted and scores:
            base_stage = _base_stage_from_existing_rows(report_rows)
            missing = sorted({str(item) for row in report_rows for item in (row.get("missing_primitives") or ())})
            score = round(sum(float(item.get("raw_points") or 0.0) for item in scores), 4)
            score_valid_status = "PENDING_MATERIAL_GAPS" if any(row.get("score_stage_validity") == "PENDING_MATERIAL_GAPS" for row in report_rows) else "FINAL_WITH_NONMATERIAL_GAPS"
            if base_stage in {"Stage1", "Red"} and score_valid_status == "PENDING_MATERIAL_GAPS":
                score_valid_status = "FINAL_WITH_NONMATERIAL_GAPS"
            rows.append(
                _row(
                    instrument=instrument,
                    as_of_date=as_of_date,
                    census_status="DEEP_VERIFIED",
                    assessment_depth="VERIFIED_STAGE",
                    base_stage=base_stage,
                    investigation_status="COMPLETE",
                    transition_overlay="NONE",
                    stage_confidence="HIGH",
                    score_valid_status=score_valid_status,
                    trigger_priority_score=scan.trigger_priority_score,
                    verified_score=score,
                    provisional_score=score,
                    score_interval_lower=score,
                    score_interval_upper=round(score + min(len(missing) * 5.0, 20.0), 4),
                    primary_archetype=_primary_archetype(report_rows),
                    accepted_claim_count=len(accepted),
                    score_contribution_count=len(scores),
                    claim_backed_score_ratio=1.0,
                    recent_event_count=max(len(report_rows), 1),
                    recent_official_event_count=scan.recent_disclosure_count
                    + scan.recent_supply_contract_count
                    + scan.recent_facility_investment_count
                    + scan.recent_earnings_event_count
                    + scan.recent_risk_event_count,
                    market_anomaly_count=0,
                    risk_event_count=1 if base_stage == "Red" else scan.recent_risk_event_count,
                    missing_primitives=missing,
                    failed_stage_gates=["material_gap"] if score_valid_status == "PENDING_MATERIAL_GAPS" else [],
                    source_gaps=sorted({str(gap) for row in report_rows for gap in (row.get("provider_source_gaps") or ())}),
                    next_actions=["RISK_REVIEW"] if base_stage == "Red" else (["RECHECK_SOURCE"] if base_stage == "Stage2-Watch" else ["WATCH"]),
                )
            )
            continue
        if thesis.thesis_status == "SOURCE_PENDING":
            rows.append(
                _row(
                    instrument=instrument,
                    as_of_date=as_of_date,
                    census_status="PENDING_SOURCE",
                    assessment_depth="RESEARCH_BRAIN_TRIAGE" if task_count else "OFFICIAL_LIGHT",
                    base_stage="Stage1",
                    investigation_status="PENDING",
                    stage_confidence="INSUFFICIENT_EVIDENCE",
                    score_valid_status="NOT_SCORED",
                    trigger_priority_score=scan.trigger_priority_score,
                    recent_event_count=1,
                    recent_official_event_count=scan.recent_disclosure_count
                    + scan.recent_supply_contract_count
                    + scan.recent_facility_investment_count
                    + scan.recent_earnings_event_count
                    + scan.recent_risk_event_count,
                    missing_primitives=["accepted_current_claim"],
                    source_gaps=list(bundle.inputs.source_gap_by_symbol.get(instrument.symbol, ("accepted_claim_absent",))),
                    next_actions=["RECHECK_SOURCE"],
                )
            )
            continue
        if thesis.thesis_status == "NEEDS_REFRESH":
            rows.append(
                _row(
                    instrument=instrument,
                    as_of_date=as_of_date,
                    census_status="LIGHT_ONLY",
                    assessment_depth="CHEAP_BASELINE",
                    base_stage="Stage1",
                    investigation_status="PENDING",
                    stage_confidence="LOW",
                    score_valid_status="NOT_SCORED",
                    trigger_priority_score=scan.trigger_priority_score,
                    recent_event_count=1,
                    market_anomaly_count=len(bundle.price_events_by_symbol.get(instrument.symbol, ())),
                    source_gaps=["accepted_current_claim_absent"],
                    next_actions=["INVESTIGATE"],
                )
            )
            continue
        rows.append(
            _row(
                instrument=instrument,
                as_of_date=as_of_date,
                census_status="SCANNED",
                assessment_depth="CHEAP_BASELINE",
                base_stage="Stage0",
                investigation_status="NO_CURRENT_CATALYST",
                stage_confidence="LOW",
                score_valid_status="NO_CURRENT_EVENT",
                trigger_priority_score=scan.trigger_priority_score,
                next_actions=["IGNORE"],
            )
        )
    return tuple(rows)


def _row(
    *,
    instrument: UniverseInstrument,
    as_of_date: str,
    census_status: str,
    assessment_depth: str,
    base_stage: str,
    investigation_status: str,
    stage_confidence: str,
    score_valid_status: str,
    transition_overlay: str = "NONE",
    trigger_priority_score: float | None = None,
    verified_score: float | None = None,
    provisional_score: float | None = None,
    score_interval_lower: float | None = None,
    score_interval_upper: float | None = None,
    primary_archetype: str | None = None,
    accepted_claim_count: int = 0,
    score_contribution_count: int = 0,
    claim_backed_score_ratio: float = 0.0,
    orphan_score_count: int = 0,
    recent_event_count: int = 0,
    recent_official_event_count: int = 0,
    market_anomaly_count: int = 0,
    risk_event_count: int = 0,
    missing_primitives: Sequence[str] = (),
    failed_stage_gates: Sequence[str] = (),
    provider_gaps: Sequence[str] = (),
    source_gaps: Sequence[str] = (),
    next_actions: Sequence[str] = (),
) -> dict[str, Any]:
    return {
        "symbol": instrument.symbol,
        "company_name": instrument.company_name,
        "market": instrument.market,
        "as_of_date": as_of_date,
        "census_status": census_status,
        "assessment_depth": assessment_depth,
        "base_stage": base_stage,
        "investigation_status": investigation_status,
        "transition_overlay": transition_overlay,
        "stage_confidence": stage_confidence,
        "score_valid_status": score_valid_status,
        "trigger_priority_score": trigger_priority_score,
        "verified_score": verified_score,
        "provisional_score": provisional_score,
        "score_interval_lower": score_interval_lower,
        "score_interval_upper": score_interval_upper,
        "primary_archetype": primary_archetype,
        "secondary_archetypes": [],
        "large_sector_id": instrument.large_sector_id,
        "accepted_claim_count": accepted_claim_count,
        "score_contribution_count": score_contribution_count,
        "claim_backed_score_ratio": claim_backed_score_ratio,
        "orphan_score_count": orphan_score_count,
        "recent_event_count": recent_event_count,
        "recent_official_event_count": recent_official_event_count,
        "market_anomaly_count": market_anomaly_count,
        "risk_event_count": risk_event_count,
        "missing_primitives": list(missing_primitives),
        "failed_stage_gates": list(failed_stage_gates),
        "provider_gaps": list(provider_gaps),
        "source_gaps": list(source_gaps),
        "next_actions": list(next_actions),
        "score_evidence_policy": "nonzero score requires accepted current claim ids",
    }


def _base_stage_from_existing_rows(rows: Sequence[Mapping[str, Any]]) -> str:
    stages = {str(row.get("current_stage")) for row in rows}
    if "3-Red" in stages or any(str(row.get("section")) == "Reject/Red" for row in rows):
        return "Red"
    if "2" in stages:
        return "Stage2-Watch"
    return "Stage1"


def _primary_archetype(rows: Sequence[Mapping[str, Any]]) -> str | None:
    counts: dict[str, int] = {}
    for row in rows:
        value = str(row.get("primary_archetype") or "")
        if value:
            counts[value] = counts.get(value, 0) + 1
    if not counts:
        return None
    return sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))[0][0]


def _provider_gap_report_v2(*, stage_rows: Sequence[Mapping[str, Any]], bundle: CensusBaselineBundle) -> dict[str, Any]:
    base = build_provider_gap_report(stage_rows)
    provider_rows = list(bundle.provider_matrix_rows)
    optional = [
        {
            "provider_name": row.get("provider_name"),
            "provider_classification": row.get("provider_classification"),
            "sample_error": row.get("sample_error"),
        }
        for row in provider_rows
        if row.get("provider_classification") == "NONBLOCKING_OPTIONAL"
    ]
    return {
        **base,
        "schema_version": "e2r_census_v2_provider_gap_report_v1",
        "provider_matrix_status_counts": _count_values(provider_rows, "provider_classification"),
        "nonblocking_optional_provider_gaps": optional,
        "blocking_provider_gap_count": sum(1 for row in provider_rows if row.get("blocking_cutover")),
    }


def _write_outputs(
    *,
    output_root: Path,
    universe_rows: Sequence[Mapping[str, Any]],
    assessment_events: Sequence[Mapping[str, Any]],
    timelines: Sequence[Mapping[str, Any]],
    thesis_states: Sequence[Mapping[str, Any]],
    baseline_rows: Sequence[Mapping[str, Any]],
    depth_rows: Sequence[Mapping[str, Any]],
    bundle: CensusBaselineBundle,
    stage_rows: Sequence[Mapping[str, Any]],
    run_metadata: Mapping[str, Any],
    self_repair_log: Mapping[str, Any],
    stage_summary: Mapping[str, Any],
    sector_distribution: Mapping[str, Any],
    provider_gap_report: Mapping[str, Any],
    source_gap_report: Mapping[str, Any],
    watchlist_seed: Mapping[str, Any],
    deep_backfill_plan: Mapping[str, Any],
    audit: Mapping[str, Any],
    operator_digest_md: str,
) -> None:
    write_json(output_root / "run_metadata.json", run_metadata)
    write_json(output_root / "self_repair_log.json", self_repair_log)
    write_jsonl(output_root / "universe.jsonl", universe_rows)
    write_jsonl(output_root / "census_assessment_events.jsonl", assessment_events)
    write_jsonl(output_root / "source_timelines.jsonl", timelines)
    write_jsonl(output_root / "last_effective_thesis_states.jsonl", thesis_states)
    write_json(output_root / "baseline_inputs_summary.json", bundle.summary)
    write_jsonl(output_root / "baseline_scan_results.jsonl", baseline_rows)
    write_jsonl(output_root / "census_events.jsonl", [event for rows in bundle.candidate_events_by_symbol.values() for event in rows])
    write_jsonl(output_root / "depth_decisions.jsonl", depth_rows)
    write_jsonl(output_root / "research_brain_plans.jsonl", [])
    write_jsonl(output_root / "source_tasks.jsonl", bundle.source_tasks)
    write_jsonl(output_root / "source_task_executions.jsonl", bundle.source_task_executions)
    write_jsonl(output_root / "evidence_documents.jsonl", bundle.evidence_documents)
    write_jsonl(output_root / "evidence_anchors.jsonl", bundle.evidence_anchors)
    write_jsonl(output_root / "raw_assertions.jsonl", bundle.raw_assertions)
    write_jsonl(output_root / "adjudicated_claims.jsonl", bundle.adjudicated_claims)
    write_jsonl(output_root / "accepted_claims.jsonl", bundle.accepted_claims)
    write_jsonl(output_root / "primitive_states.jsonl", bundle.primitive_states)
    write_jsonl(output_root / "score_contributions.jsonl", bundle.score_contributions)
    write_jsonl(output_root / "stagecourt_traces.jsonl", bundle.stagecourt_traces)
    write_jsonl(output_root / "census_stage_status.jsonl", stage_rows)
    write_jsonl(output_root / "census_stage_map.jsonl", stage_rows)
    _write_stage_csv(output_root / "census_stage_map.csv", stage_rows)
    write_json(output_root / "census_stage_summary.json", stage_summary)
    write_json(output_root / "sector_stage_distribution.json", sector_distribution)
    write_json(output_root / "provider_gap_report.json", provider_gap_report)
    write_json(output_root / "source_gap_report.json", source_gap_report)
    write_json(output_root / "watchlist_seed_candidates.json", watchlist_seed)
    write_json(output_root / "deep_backfill_plan.json", deep_backfill_plan)
    write_text(output_root / "operator_digest.md", operator_digest_md)
    write_json(output_root / "audit_summary.json", audit)


def _write_stage_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    import csv

    columns = (
        "symbol",
        "company_name",
        "market",
        "large_sector_id",
        "census_status",
        "assessment_depth",
        "base_stage",
        "investigation_status",
        "transition_overlay",
        "stage_confidence",
        "score_valid_status",
        "trigger_priority_score",
        "verified_score",
        "provisional_score",
        "score_interval_lower",
        "score_interval_upper",
        "accepted_claim_count",
        "score_contribution_count",
        "recent_event_count",
        "primary_archetype",
        "failed_stage_gates",
        "missing_primitives",
        "provider_gaps",
        "source_gaps",
        "next_actions",
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: _csv_cell(row.get(key)) for key in columns})


def _write_operational_docs_v2(
    *,
    config: CensusV2RunConfig,
    output_root: Path,
    universe_coverage: Mapping[str, Any],
    stage_summary: Mapping[str, Any],
    sector_distribution: Mapping[str, Any],
    provider_gap_report: Mapping[str, Any],
    source_gap_report: Mapping[str, Any],
    watchlist_seed: Mapping[str, Any],
    deep_backfill_plan: Mapping[str, Any],
    audit: Mapping[str, Any],
    readiness: Mapping[str, Any],
    metadata: Mapping[str, Any],
    self_repair_log: Mapping[str, Any],
    runtime_seconds: float,
    bundle: CensusBaselineBundle,
) -> None:
    docs = Path("docs/operational")
    write_text(docs / "census_mode_v1_reclassification.md", _v1_reclassification_doc(self_repair_log))
    write_text(docs / "census_mode_v2_lifecycle_and_recency_policy.md", _lifecycle_policy_doc())
    write_text(docs / "census_mode_v2_stage_map_summary.md", render_stage_map_summary_md(stage_summary).replace("v1", "v2"))
    write_json(docs / "census_mode_v2_stage_distribution.json", stage_summary.get("stage_distribution") or {})
    write_json(docs / "census_mode_v2_universe_coverage.json", universe_coverage)
    write_json(docs / "census_mode_v2_sector_stage_distribution.json", sector_distribution)
    write_json(docs / "census_mode_v2_provider_gap_report.json", provider_gap_report)
    write_json(docs / "census_mode_v2_source_gap_report.json", source_gap_report)
    write_text(docs / "census_mode_v2_watchlist_seed_report.md", render_watchlist_seed_report(watchlist_seed))
    write_text(docs / "census_mode_v2_deep_backfill_plan.md", render_deep_backfill_plan(deep_backfill_plan))
    write_text(docs / "census_mode_v2_self_repair_summary.md", _self_repair_md(self_repair_log))
    write_json(docs / "census_mode_v2_static_logic_audit.json", audit)
    write_text(docs / "census_mode_v2_readiness_verdict.md", _readiness_md(readiness))
    write_text(
        docs / "census_mode_v2_acceptance_report.md",
        _acceptance_report_v2(
            config=config,
            output_root=output_root,
            universe_coverage=universe_coverage,
            stage_summary=stage_summary,
            audit=audit,
            readiness=readiness,
            metadata=metadata,
            runtime_seconds=runtime_seconds,
            bundle=bundle,
        ),
    )


def _self_repair_log(
    *,
    as_of_date: str,
    before_root: Path,
    after_stage_summary: Mapping[str, Any],
    after_audit: Mapping[str, Any],
    bundle: CensusBaselineBundle,
) -> dict[str, Any]:
    before_summary = _load_json(before_root / "census_stage_summary.json")
    return {
        "schema_version": "e2r_census_v2_self_repair_log_v1",
        "as_of_date": as_of_date,
        "iterations": [
            {
                "iteration": 1,
                "detected_failure": "CENSUS_V1_ALL_PROVIDER_PENDING_OR_EMPTY_BASELINE",
                "before_stage_summary": before_summary,
                "root_cause": "v1 baseline inputs did not wire existing provider matrix, accepted claim ledger, source task report, report snapshots, or price files.",
                "patch_summary": [
                    "added baseline input collector",
                    "added source timeline for every eligible symbol",
                    "added last effective thesis state map",
                    "replayed existing accepted claim-backed ledger only for eligible universe symbols",
                    "kept CensusAssessmentEvent and market anomaly out of score evidence",
                ],
                "after_stage_summary": after_stage_summary,
                "after_audit_status": after_audit["summary"]["status"],
                "resolved": after_audit["summary"]["critical_count_sum"] == 0,
            }
        ],
        "baseline_inputs_summary": dict(bundle.summary),
    }


def _readiness_verdict(*, audit: Mapping[str, Any], stage_summary: Mapping[str, Any], source_task_count: int) -> dict[str, Any]:
    blockers: list[str] = []
    if audit["summary"]["critical_count_sum"]:
        blockers.append("critical audit counts are nonzero")
    if source_task_count <= 0:
        blockers.append("source tasks are empty")
    if stage_summary.get("provider_pending_count", 0) >= stage_summary.get("eligible_symbol_count", 0) * 0.30:
        blockers.append("provider pending rate is too high")
    verdict = "FULL_UNIVERSE_STAGE_MAP_PASS" if not blockers else "EXTERNAL_BLOCKER_NOT_READY"
    labels = audit["summary"].get("labels", []) if not blockers else []
    return {"schema_version": "e2r_census_v2_readiness_verdict_v1", "verdict": verdict, "labels": labels, "blockers": blockers}


def _default_universe_snapshot(as_of_date: str) -> str | None:
    snapshot = Path("output/census") / as_of_date / "universe.jsonl"
    return str(snapshot) if snapshot.exists() else None


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def _count_values(rows: Sequence[Mapping[str, Any]], key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        value = str(row.get(key) or "UNKNOWN")
        counts[value] = counts.get(value, 0) + 1
    return counts


def _csv_cell(value: Any) -> Any:
    if isinstance(value, (list, tuple)):
        return "|".join(str(item) for item in value)
    return value


def _command_string(config: CensusV2RunConfig) -> str:
    return f"PYTHONPATH=src python -m e2r.cli.run_e2r_census_v2 --as-of-date {config.as_of_date} --output-root {config.resolved_output_root()}"


def _v1_reclassification_doc(self_repair_log: Mapping[str, Any]) -> str:
    before = (self_repair_log.get("iterations") or [{}])[0].get("before_stage_summary") or {}
    return "\n".join(
        [
            "# Census Mode v1 Reclassification",
            "",
            "v1 산출물은 FULL_UNIVERSE_STAGE_MAP_PASS가 아니라 CENSUS_SKELETON_PASS로 재분류한다.",
            "",
            f"- v1 eligible: {before.get('eligible_symbol_count')}",
            f"- v1 ProviderPending: {before.get('provider_pending_count')}",
            f"- v1 accepted_claim_total: {before.get('accepted_claim_total')}",
            f"- v1 score_contribution_total: {before.get('score_contribution_total')}",
            "",
            "쉬운 예: 전 종목에 출석체크만 있고 답안지가 하나도 없으면, 전체 지도를 완성했다고 부르면 안 된다.",
            "",
        ]
    )


def _lifecycle_policy_doc() -> str:
    return "\n".join(
        [
            "# Census Mode v2 Lifecycle and Recency Policy",
            "",
            "- CensusAssessmentEvent는 전 종목 평가를 여는 행정 이벤트이며 점수 근거가 아니다.",
            "- CandidateEvent, MarketAnomaly, stored source snapshot은 조사를 여는 트리거일 수 있지만 점수 근거가 아니다.",
            "- accepted current claim과 score contribution id가 연결된 경우에만 verified score가 열린다.",
            "- 오래된 리포트나 뉴스는 현재 claim으로 lifecycle refresh되기 전까지 SOURCE_PENDING 또는 NEEDS_REFRESH다.",
            "- UNKNOWN은 PRESENT도 ABSENT도 아니다.",
            "",
            "쉬운 예: 2023년 좋은 리포트가 있어도 2026년 현재 원문 claim으로 다시 살아나지 않으면 점수는 0이고, 상태는 refresh 대상이다.",
            "",
        ]
    )


def _self_repair_md(self_repair_log: Mapping[str, Any]) -> str:
    iteration = (self_repair_log.get("iterations") or [{}])[0]
    return "\n".join(
        [
            "# Census Mode v2 Self Repair Summary",
            "",
            f"- detected_failure: {iteration.get('detected_failure')}",
            f"- root_cause: {iteration.get('root_cause')}",
            f"- resolved: {iteration.get('resolved')}",
            "",
            "## Patch Summary",
            *[f"- {item}" for item in iteration.get("patch_summary") or []],
            "",
        ]
    )


def _readiness_md(readiness: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# Census Mode v2 Readiness Verdict",
            "",
            f"- verdict: {readiness.get('verdict')}",
            f"- labels: {', '.join(readiness.get('labels') or [])}",
            f"- blockers: {readiness.get('blockers')}",
            f"- report_generation_commit_sha: {git_head_sha('.')}",
            "",
        ]
    )


def _acceptance_report_v2(
    *,
    config: CensusV2RunConfig,
    output_root: Path,
    universe_coverage: Mapping[str, Any],
    stage_summary: Mapping[str, Any],
    audit: Mapping[str, Any],
    readiness: Mapping[str, Any],
    metadata: Mapping[str, Any],
    runtime_seconds: float,
    bundle: CensusBaselineBundle,
) -> str:
    metrics = audit.get("v2_metrics") or {}
    return "\n".join(
        [
            "# Census Mode v2 Acceptance Report",
            "",
            f"1. Final status: {', '.join(readiness.get('labels') or [])}",
            f"2. Commit SHA at report generation: {git_head_sha('.')}",
            "3. Test command: PYTHONPATH=src python -m unittest discover -s tests -v",
            f"   Test result: {config.test_result_summary}",
            f"4. Universe coverage: raw={universe_coverage.get('raw_universe_count')}, eligible={universe_coverage.get('eligible_common_stock_count')}",
            f"5. output_root: {output_root}",
            f"6. hashes: config={metadata.get('config_hash')}, source={metadata.get('source_corpus_hash')}, candidate={metadata.get('candidate_event_hash')}, scoring={metadata.get('scoring_schema_version')}, stage={metadata.get('stage_schema_version')}",
            f"7. Stage distribution: {stage_summary.get('stage_distribution')}",
            f"8. Status distribution: {stage_summary.get('status_distribution')}",
            f"9. Accepted claim count: {metrics.get('accepted_claim_total')}",
            f"10. Score contribution count: {metrics.get('score_contribution_total')}",
            f"11. Source task count: {metrics.get('source_task_count')}",
            f"12. Provider pending rate: {metrics.get('provider_pending_rate')}",
            f"13. Unknown count: {metrics.get('unknown_count')}",
            f"14. Static audit critical counts: {audit.get('critical_counts')}",
            f"15. Readiness verdict: {readiness.get('verdict')}",
            f"16. Runtime seconds: {runtime_seconds:.2f}",
            f"17. Baseline source family counts: {bundle.summary.get('source_family_counts')}",
            "",
            "쉬운 예: 전 종목은 출석체크를 받았지만, 점수는 accepted claim이 있는 종목만 받았다.",
            "",
        ]
    )


__all__ = ["CensusV2RunConfig", "CensusV2RunResult", "run_census_mode_v2"]

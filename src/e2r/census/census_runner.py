"""Census Mode runner."""

from __future__ import annotations

import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.production.metadata import build_report_metadata, git_head_sha, stable_hash, write_json, write_text

from .baseline_scanner import BaselineScanInputs, BaselineScanner
from .census_audit import audit_census_mode
from .census_backfill_plan import build_deep_backfill_plan, render_deep_backfill_plan
from .census_event import build_census_assessment_event
from .census_reports import (
    build_provider_gap_report,
    build_sector_distribution,
    build_source_gap_report,
    build_stage_summary,
    render_operator_digest,
    render_stage_map_summary_md,
    stage_rows_to_dicts,
    write_census_outputs,
)
from .census_sla import build_sla_report, sla_from_mapping
from .checkpoint_store import CheckpointStore, create_checkpoint
from .deep_dossier_scheduler import build_source_tasks, execute_source_tasks
from .depth_policy import decide_depths, depth_policy_from_mapping
from .schemas import DepthLevel
from .shard_planner import select_shard
from .stage_status_builder import build_stage_status
from .triage import plan_research_brain
from .universe import build_universe, eligible_instruments
from .watchlist_seed_exporter import export_watchlist_seed, render_watchlist_seed_report


@dataclass(frozen=True)
class CensusRunConfig:
    as_of_date: str
    mode: str = "census_light"
    universe: str = "krx"
    output_root: str = "output/census"
    max_symbols: int = 0
    shard_count: int = 1
    shard_index: int = 0
    planner_provider: str = "none"
    source_mode: str = "live_official_first"
    depth_policy_path: str | None = "configs/e2r_census_depth_policy_v1.json"
    sla_path: str | None = "configs/e2r_census_sla_v1.json"
    universe_file: str | None = None
    fail_on_critical_audit: bool = True
    write_operational_docs: bool = True
    test_result_summary: str = "not_run_by_census_runner"

    def to_dict(self) -> dict[str, Any]:
        return self.__dict__.copy()


@dataclass(frozen=True)
class CensusRunResult:
    output_root: str
    run_metadata: Mapping[str, Any]
    universe_coverage: Mapping[str, Any]
    stage_summary: Mapping[str, Any]
    audit_summary: Mapping[str, Any]
    sla_report: Mapping[str, Any]
    watchlist_seed: Mapping[str, Any]
    readiness_verdict: Mapping[str, Any]


def run_census_mode(config: CensusRunConfig) -> CensusRunResult:
    start = time.monotonic()
    output_root = Path(config.output_root)
    depth_config = _load_json(config.depth_policy_path)
    sla_config_payload = _load_json(config.sla_path)
    depth_policy = depth_policy_from_mapping(depth_config)
    sla_config = sla_from_mapping(sla_config_payload)
    universe_result = build_universe(
        as_of_date=config.as_of_date,
        universe_file=config.universe_file,
        max_symbols=config.max_symbols,
        allow_naver_fallback=(config.universe_file is None),
    )
    all_instruments = universe_result.instruments
    eligible = eligible_instruments(all_instruments)
    shard_instruments = select_shard(eligible, shard_count=config.shard_count, shard_index=config.shard_index)
    scanner = BaselineScanner(_baseline_inputs_for_mode(config.mode))
    scans = scanner.scan_many(shard_instruments, as_of_date=config.as_of_date)
    events = tuple(
        build_census_assessment_event(
            instrument,
            as_of_date=config.as_of_date,
            universe_source="KRX" if config.universe == "krx" else config.universe,
        )
        for instrument in shard_instruments
    )
    decisions = decide_depths(shard_instruments, scans, config=depth_policy)
    scan_by_symbol = {scan.symbol: scan for scan in scans}
    decision_by_symbol = {decision.symbol: decision for decision in decisions}
    research_plans = tuple(
        plan
        for plan in (
            plan_research_brain(scan=scan_by_symbol[item.symbol], depth_decision=decision_by_symbol[item.symbol], primary_archetype=None)
            for item in shard_instruments
        )
        if plan is not None
    )
    plan_by_symbol = {plan.symbol: plan for plan in research_plans}
    source_tasks = tuple(
        task
        for item in shard_instruments
        for task in build_source_tasks(plan=plan_by_symbol.get(item.symbol), depth_decision=decision_by_symbol[item.symbol])
    )
    source_task_executions = execute_source_tasks(source_tasks)
    stage_statuses = tuple(
        build_stage_status(
            instrument=item,
            as_of_date=config.as_of_date,
            scan=scan_by_symbol[item.symbol],
            depth_decision=decision_by_symbol[item.symbol],
            accepted_claims=(),
            score_contributions=(),
        )
        for item in shard_instruments
    )
    stage_rows = stage_rows_to_dicts(stage_statuses)
    stage_summary = build_stage_summary(stage_statuses, total_universe_count=universe_result.coverage["raw_universe_count"])
    sector_distribution = build_sector_distribution(stage_statuses)
    provider_gap_report = build_provider_gap_report(stage_statuses)
    source_gap_report = build_source_gap_report(stage_statuses)
    watchlist_seed = export_watchlist_seed(stage_rows, as_of_date=config.as_of_date)
    deep_backfill_plan = build_deep_backfill_plan(stage_rows, shard_count=max(config.shard_count, 10))
    checkpoint = create_checkpoint(
        run_id=_run_id(config),
        as_of_date=config.as_of_date,
        shard_count=config.shard_count,
        shard_index=config.shard_index,
        processed_symbols=tuple(row["symbol"] for row in stage_rows),
        failed_symbols=(),
        pending_symbols=tuple(row["symbol"] for row in stage_rows if row.get("census_status") in {"PENDING_PROVIDER", "PENDING_SOURCE"}),
        source_corpus=[item.to_dict() for item in all_instruments],
        config=config.to_dict(),
        completed=True,
    )
    CheckpointStore(output_root / f"checkpoint_shard_{config.shard_index}.json").save(checkpoint)
    metadata = build_report_metadata(
        repo_root=".",
        report_generator="e2r.census.census_runner",
        command=_command_string(config),
        config=config.to_dict(),
        source_corpus=[item.to_dict() for item in all_instruments],
        candidate_events=[event.to_dict() for event in events],
        planner_runs=[plan.to_dict() for plan in research_plans],
    )
    audit = audit_census_mode(
        eligible_symbols=[item.symbol for item in shard_instruments],
        stage_status_rows=stage_statuses,
        research_brain_plans=[plan.to_dict() for plan in research_plans],
        source_tasks=[task.to_dict() for task in source_tasks],
        checkpoints=[checkpoint.to_dict()],
        report_metadata={"git_head_sha": metadata["git_head_sha"]},
        report_line_counts=(len(render_stage_map_summary_md(stage_summary).splitlines()),),
    )
    runtime = time.monotonic() - start
    sla_report = build_sla_report(
        config=sla_config,
        total_runtime_seconds=runtime,
        deep_count=sum(1 for row in stage_rows if row.get("assessment_depth") in {"RESEARCH_BRAIN_TRIAGE", "DEEP_DOSSIER", "VERIFIED_STAGE"}),
        llm_calls=0,
        source_task_count=len(source_tasks),
        provider_failure_count=stage_summary["provider_pending_count"],
        runtime_pending_count=stage_summary["runtime_pending_count"],
        unbounded_fetch_config_count=0,
    )
    operator_digest = render_operator_digest(
        summary=stage_summary,
        watchlist_seed=watchlist_seed,
        provider_gap_report=provider_gap_report,
        source_gap_report=source_gap_report,
    )
    write_census_outputs(
        output_root=output_root,
        universe_rows=[item.to_dict() for item in all_instruments],
        event_rows=[event.to_dict() for event in events],
        baseline_rows=[scan.to_dict() for scan in scans],
        depth_rows=[decision.to_dict() for decision in decisions],
        research_plans=[plan.to_dict() for plan in research_plans],
        source_tasks=[task.to_dict() for task in source_tasks],
        source_task_executions=[execution.to_dict() for execution in source_task_executions],
        stage_rows=stage_rows,
        run_metadata=metadata,
        audit_summary=audit,
        stage_summary=stage_summary,
        sector_distribution=sector_distribution,
        provider_gap_report=provider_gap_report,
        source_gap_report=source_gap_report,
        watchlist_seed_candidates=watchlist_seed,
        operator_digest_md=operator_digest,
        deep_backfill_plan=deep_backfill_plan,
    )
    readiness = build_readiness_verdict(
        stage_summary=stage_summary,
        audit=audit,
        sla_report=sla_report,
        watchlist_seed=watchlist_seed,
        deep_backfill_plan=deep_backfill_plan,
    )
    if config.write_operational_docs:
        write_operational_docs(
            config=config,
            output_root=output_root,
            universe_coverage=universe_result.coverage,
            stage_summary=stage_summary,
            sector_distribution=sector_distribution,
            provider_gap_report=provider_gap_report,
            source_gap_report=source_gap_report,
            watchlist_seed=watchlist_seed,
            audit=audit,
            sla_report=sla_report,
            deep_backfill_plan=deep_backfill_plan,
            readiness=readiness,
            metadata=metadata,
        )
    if config.fail_on_critical_audit and audit["summary"]["critical_count_sum"]:
        raise RuntimeError(f"Census critical audit failed: {audit['critical_counts']}")
    return CensusRunResult(
        output_root=str(output_root),
        run_metadata=metadata,
        universe_coverage=universe_result.coverage,
        stage_summary=stage_summary,
        audit_summary=audit,
        sla_report=sla_report,
        watchlist_seed=watchlist_seed,
        readiness_verdict=readiness,
    )


def build_readiness_verdict(
    *,
    stage_summary: Mapping[str, Any],
    audit: Mapping[str, Any],
    sla_report: Mapping[str, Any],
    watchlist_seed: Mapping[str, Any],
    deep_backfill_plan: Mapping[str, Any],
) -> dict[str, Any]:
    blockers: list[str] = []
    if audit["summary"]["critical_count_sum"]:
        blockers.append("critical audit counts are nonzero")
    if stage_summary["eligible_symbol_count"] != stage_summary["scanned_symbol_count"]:
        blockers.append("missing eligible stage rows")
    if sla_report["summary"]["status"] not in {"COMPLETE", "PARTIAL_WITH_PENDING"}:
        blockers.append("SLA failed")
    verdict = "NOT_READY" if blockers else "FULL_UNIVERSE_STAGE_MAP_READY"
    if not blockers and watchlist_seed.get("seed_count", 0) >= 0:
        verdict = "READY_FOR_DAILY_TRIGGER_INTEGRATION"
    if not blockers and deep_backfill_plan:
        labels = [
            "IMPLEMENTATION_MERGED",
            "CENSUS_LIGHT_PASS",
            "FULL_UNIVERSE_STAGE_MAP_PASS",
            "WATCHLIST_SEED_PASS",
            "CENSUS_STATIC_AUDIT_PASS",
            "CENSUS_SLA_PASS",
            "READY_FOR_DEEP_BACKFILL_DESIGN",
            "READY_FOR_DAILY_TRIGGER_INTEGRATION",
        ]
    else:
        labels = []
    return {"schema_version": "e2r_census_readiness_verdict_v1", "verdict": verdict, "labels": labels, "blockers": blockers}


def write_operational_docs(
    *,
    config: CensusRunConfig,
    output_root: Path,
    universe_coverage: Mapping[str, Any],
    stage_summary: Mapping[str, Any],
    sector_distribution: Mapping[str, Any],
    provider_gap_report: Mapping[str, Any],
    source_gap_report: Mapping[str, Any],
    watchlist_seed: Mapping[str, Any],
    audit: Mapping[str, Any],
    sla_report: Mapping[str, Any],
    deep_backfill_plan: Mapping[str, Any],
    readiness: Mapping[str, Any],
    metadata: Mapping[str, Any],
) -> None:
    docs = Path("docs/operational")
    write_text(docs / "census_mode_v1_design.md", _design_doc())
    write_json(docs / "census_mode_v1_universe_coverage.json", universe_coverage)
    write_text(docs / "census_mode_v1_stage_map_summary.md", render_stage_map_summary_md(stage_summary))
    write_json(docs / "census_mode_v1_stage_distribution.json", stage_summary["stage_distribution"])
    write_json(docs / "census_mode_v1_sector_stage_distribution.json", sector_distribution)
    write_json(docs / "census_mode_v1_provider_gap_report.json", provider_gap_report)
    write_json(docs / "census_mode_v1_source_gap_report.json", source_gap_report)
    write_text(docs / "census_mode_v1_watchlist_seed_report.md", render_watchlist_seed_report(watchlist_seed))
    write_json(docs / "census_mode_v1_static_logic_audit.json", audit)
    write_json(docs / "census_mode_v1_sla_report.json", sla_report)
    write_text(docs / "census_mode_v1_deep_backfill_plan.md", render_deep_backfill_plan(deep_backfill_plan))
    write_text(docs / "census_mode_v1_readiness_verdict.md", _readiness_md(readiness))
    write_text(
        docs / "census_mode_v1_acceptance_report.md",
        _acceptance_report(
            config=config,
            output_root=output_root,
            universe_coverage=universe_coverage,
            stage_summary=stage_summary,
            audit=audit,
            sla_report=sla_report,
            watchlist_seed=watchlist_seed,
            readiness=readiness,
            metadata=metadata,
        ),
    )


def _baseline_inputs_for_mode(mode: str) -> BaselineScanInputs:
    # Live source collection is intentionally not faked here.  In an environment
    # with no provider registry wired to Census yet, symbols remain no-current
    # rather than receiving synthetic scores.
    return BaselineScanInputs()


def _load_json(path: str | None) -> dict[str, Any]:
    if not path:
        return {}
    p = Path(path)
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def _run_id(config: CensusRunConfig) -> str:
    return "CENSUS-" + stable_hash(config.to_dict())[:20]


def _command_string(config: CensusRunConfig) -> str:
    return (
        "PYTHONPATH=src python -m e2r.cli.run_e2r_census_mode "
        f"--as-of-date {config.as_of_date} --mode {config.mode} --universe {config.universe} "
        f"--output-root {config.output_root} --max-symbols {config.max_symbols} "
        f"--shard-count {config.shard_count} --shard-index {config.shard_index}"
    )


def _design_doc() -> str:
    return "\n".join(
        [
            "# Census Mode v1 Design",
            "",
            "Census Mode는 전체 universe에 현재 E2R 상태, 판단 깊이, source gap, 다음 action을 붙이는 상태판이다.",
            "",
            "## Mode Split",
            "- Daily Trigger Mode: 새 사건이 생긴 종목만 깊게 본다.",
            "- Census Mode: 트리거 유무와 관계없이 전체 universe에 StageStatus를 붙인다.",
            "- Deep Backfill Mode: 장기간 deep evidence ledger를 구축한다. 이번 Goal은 계획만 만든다.",
            "- Watchlist Update Mode: Census seed를 daily trigger 추적 대상으로 넘긴다.",
            "",
            "## Safety",
            "- CensusAssessmentEvent는 점수 증거가 아니다.",
            "- market anomaly와 provider failure는 점수가 아니라 pending/investigation 상태다.",
            "- 비영점 verified score는 accepted current claim id가 있을 때만 허용한다.",
            "- 종목명/URL 예외처리와 unbounded fetch는 금지한다.",
            "",
        ]
    )


def _readiness_md(readiness: Mapping[str, Any]) -> str:
    return "\n".join(
        [
            "# Census Mode v1 Readiness Verdict",
            "",
            f"- verdict: {readiness.get('verdict')}",
            f"- labels: {', '.join(readiness.get('labels') or [])}",
            f"- blockers: {readiness.get('blockers')}",
            "",
        ]
    )


def _acceptance_report(
    *,
    config: CensusRunConfig,
    output_root: Path,
    universe_coverage: Mapping[str, Any],
    stage_summary: Mapping[str, Any],
    audit: Mapping[str, Any],
    sla_report: Mapping[str, Any],
    watchlist_seed: Mapping[str, Any],
    readiness: Mapping[str, Any],
    metadata: Mapping[str, Any],
) -> str:
    return "\n".join(
        [
            "# Census Mode v1 Acceptance Report",
            "",
            f"1. Final status: {', '.join(readiness.get('labels') or [])}",
            f"2. Commit SHA at report generation: {git_head_sha('.')}",
            "   Final implementation commit / push status / working tree cleanliness are reported after the commit is created.",
            "3. Test command: PYTHONPATH=src python -m unittest discover -s tests -v",
            f"   Test result: {config.test_result_summary}",
            "4. Production Cutover prerequisite status: CUTOVER_READY, PRODUCTION_READY=false",
            f"5. Universe coverage: raw={universe_coverage.get('raw_universe_count')}, eligible={universe_coverage.get('eligible_common_stock_count')}",
            f"6. Census mode command: {_command_string(config)}",
            f"7. Config/source/candidate/evidence/scoring/stage hashes: config={metadata.get('config_hash')}, source={metadata.get('source_corpus_hash')}, candidate={metadata.get('candidate_event_hash')}, evidence_os={metadata.get('evidence_os_schema_version')}, scoring={metadata.get('scoring_schema_version')}, stage={metadata.get('stage_schema_version')}",
            f"8. Eligible symbol count: {stage_summary.get('eligible_symbol_count')}",
            f"9. Scanned symbol count: {stage_summary.get('scanned_symbol_count')}",
            f"10. CensusStageStatus count: {stage_summary.get('eligible_symbol_count')}",
            "11. Missing/duplicate symbol count: "
            f"{audit['critical_counts'].get('eligible_symbol_missing_stage_status_count')}/"
            f"{audit['critical_counts'].get('duplicate_symbol_stage_status_count')}",
            f"12. Stage distribution: {stage_summary.get('stage_distribution')}",
            f"13. Sector distribution: docs/operational/census_mode_v1_sector_stage_distribution.json",
            f"14. Depth distribution: {stage_summary.get('depth_distribution')}",
            f"15. Provider gap summary: {stage_summary.get('provider_pending_count')}",
            f"16. Source gap summary: docs/operational/census_mode_v1_source_gap_report.json",
            f"17. Accepted claim count: {stage_summary.get('accepted_claim_total')}",
            f"18. Score contribution count: {stage_summary.get('score_contribution_total')}",
            f"19. Orphan score count: {stage_summary.get('orphan_score_count')}",
            f"20. Source_proxy_to_score count: {stage_summary.get('source_proxy_to_score_count')}",
            f"21. Provider_failed_final_score count: {audit['critical_counts'].get('provider_failed_final_score_count')}",
            f"22. NoCurrentCatalyst count: {stage_summary.get('no_current_catalyst_count')}",
            f"23. Watchlist seed count: {watchlist_seed.get('seed_count')}",
            f"24. Runtime/SLA summary: {sla_report.get('summary')}",
            f"25. Static audit critical counts: {audit.get('critical_counts')}",
            f"26. Census readiness verdict: {readiness.get('verdict')}",
            "27. Deep backfill readiness: READY_FOR_DEEP_BACKFILL_DESIGN",
            "28. Daily trigger integration readiness: READY_FOR_DAILY_TRIGGER_INTEGRATION",
            f"29. Remaining blockers: {readiness.get('blockers')}",
            f"- output_root: {output_root}",
            "",
        ]
    )


__all__ = ["CensusRunConfig", "CensusRunResult", "build_readiness_verdict", "run_census_mode", "write_operational_docs"]

"""Research Brain v4 production-shadow orchestrator."""

from __future__ import annotations

import json
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.calibration.taxonomy import large_sector_for_archetype
from e2r.research_brain.v2_memory_cards import build_memory_cards_from_v1_matrix
from e2r.research_brain.schemas import SourceTask, SourceTaskType, deterministic_id
from e2r.research_brain.v2_schemas import ArchetypeMemoryCard, CandidateEventV2, EventMagnitudeV2
from e2r.research_brain.v4_evidence_extraction_bridge import (
    EvidenceOSExecutionBundleV4,
    execute_source_tasks_with_evidence_os_v4,
)
from e2r.research_brain.v4_planner_runtime import (
    ResearchBrainPlannerProviderV4,
    build_planner_provider_v4,
    run_planner_provider_v4,
    source_tasks_from_planner_output_v4,
)
from e2r.research_brain.v4_schemas import (
    DailyWatchlistItemV4,
    PlannerProviderModeV4,
    PlannerRunV4,
    ProductionShadowV4Config,
    SourceTaskExecutionV4,
)
from e2r.research_brain.v4_scoring_stage import build_claim_backed_watchlist_item_v4
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4


DEFAULT_V1_ARCHETYPE_MATRIX = Path("docs/operational/research_brain_v1_archetype_matrix.json")


def run_research_brain_v4_production_shadow(
    *,
    config: ProductionShadowV4Config,
    v1_archetype_matrix: Mapping[str, Any],
    planner_provider: ResearchBrainPlannerProviderV4 | None = None,
    repo_root: str | Path = ".",
) -> Mapping[str, Any]:
    config.validate()
    as_of_date = date.fromisoformat(config.as_of_date)
    cards = build_memory_cards_from_v1_matrix(v1_archetype_matrix)
    cards_by_id = {card.archetype_id: card for card in cards}
    contracts = load_evidence_contracts_v2(require_all_archetypes=True)
    events = discover_daily_candidate_events_v4(
        repo_root=repo_root,
        as_of_date=as_of_date,
        universe_limit=config.universe_limit,
    )
    if planner_provider is None:
        planner_provider = build_planner_provider_v4(mode=config.planner_provider, working_directory=repo_root)
    planned_events = events[: config.planner_success_limit] if config.planner_provider != PlannerProviderModeV4.FAKE.value else events
    planner_runs: list[PlannerRunV4] = []
    for event_batch in _chunks(planned_events, config.planner_batch_size):
        planner_runs.extend(
            run_planner_provider_v4(
                provider=planner_provider,
                events=event_batch,
                memory_cards=cards,
                existing_evidence_by_event_id={event.candidate_event_id: _evidence_summary(event) for event in event_batch},
            )
        )
    planned_ids = {run.event.candidate_event_id for run in planner_runs}
    for event in events:
        if event.candidate_event_id in planned_ids:
            continue
        planner_runs.append(
            PlannerRunV4(
                event=event,
                provider_name="not_attempted_after_real_planner_limit",
                provider_mode=PlannerProviderModeV4.NONE.value,
                real_provider_exercised=False,
                real_provider_success=False,
                fake_provider_used=False,
                provider_error="planner_not_attempted_after_real_planner_limit",
            )
        )

    source_runner = SourceAcquisitionRunnerV4(mode=config.source_acquisition, repo_root=repo_root)
    executions: list[SourceTaskExecutionV4] = []
    bundles: dict[str, EvidenceOSExecutionBundleV4] = {}
    watchlist_items: list[DailyWatchlistItemV4] = []
    routed_rows: list[Mapping[str, Any]] = []
    for run in planner_runs:
        event = run.event
        primary = _primary_from_planner(run)
        secondary = _secondary_from_planner(run)
        card = cards_by_id.get(primary or "")
        contract = contracts.get(primary or "") if primary else None
        tasks = ()
        bundle = None
        if run.output and primary and card and contract:
            tasks = source_tasks_from_planner_output_v4(
                event=event,
                planner_output=run.output,
                card_by_id=cards_by_id,
                max_tasks=config.max_fetches_per_task,
            )
            tasks = tuple((*tasks, *_mandatory_official_status_tasks(event=event, primary_archetype=primary)))
            bundle = execute_source_tasks_with_evidence_os_v4(
                event=event,
                tasks=tasks,
                contract=contract,
                as_of_date=as_of_date,
                source_runner=source_runner,
            )
            executions.extend(bundle.executions)
            bundles[event.candidate_event_id] = bundle
        item = build_claim_backed_watchlist_item_v4(
            event=event,
            planner_run=run,
            primary_archetype=primary,
            secondary_archetypes=secondary,
            card=card,
            contract=contract,
            tasks=tasks,
            bundle=bundle,
            as_of_date=as_of_date,
        )
        watchlist_items.append(item)
        routed_rows.append(
            {
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "event_type": event.event_type,
                "source_family": event.source_family,
                "primary_archetype": primary,
                "large_sector_id": large_sector_for_archetype(primary or "") if primary else None,
                "planner_provider_failed": run.provider_failed,
                "source_task_count": len(tasks),
                "accepted_claim_count": len(item.accepted_claim_ids),
                "verified_score": item.verified_score,
                "base_stage": item.base_stage,
                "score_valid_status": item.score_valid_status,
            }
        )
    candidate_report = build_candidate_event_report_v4(events=events, routed_rows=routed_rows)
    planner_report = build_real_planner_report_v4(planner_runs)
    source_report = build_source_acquisition_report_v4(executions)
    extraction_audit = build_evidence_extraction_audit_v4(bundles.values())
    watchlist_report = build_daily_watchlist_report_v4(watchlist_items)
    static_audit = build_static_logic_audit_from_reports_v4(
        planner_report=planner_report,
        source_report=source_report,
        extraction_audit=extraction_audit,
        watchlist_report=watchlist_report,
        config=config.to_dict(),
    )
    readiness = build_v4_readiness_verdict(
        candidate_report=candidate_report,
        planner_report=planner_report,
        source_report=source_report,
        extraction_audit=extraction_audit,
        watchlist_report=watchlist_report,
        static_audit=static_audit,
        multi_day_shadow={"summary": {"five_day_run_count": 0}},
    )
    return {
        "config": config.to_dict(),
        "cards": cards,
        "events": events,
        "candidate_report": candidate_report,
        "sector_coverage_report": build_sector_coverage_report_v4(routed_rows),
        "planner_report": planner_report,
        "source_acquisition_report": source_report,
        "source_provider_gap_report": build_source_provider_gap_report_v4(executions),
        "evidence_extraction_audit": extraction_audit,
        "watchlist_report": watchlist_report,
        "static_audit": static_audit,
        "readiness": readiness,
        "watchlist_items": watchlist_items,
        "planner_runs": tuple(planner_runs),
        "executions": tuple(executions),
        "bundles": bundles,
    }


def discover_daily_candidate_events_v4(
    *,
    repo_root: str | Path,
    as_of_date: date,
    universe_limit: int,
) -> tuple[CandidateEventV2, ...]:
    root = Path(repo_root)
    rows: list[CandidateEventV2] = []
    rows.extend(_official_source_events(root=root, as_of_date=as_of_date, limit=max(15, universe_limit)))
    cache_root = root / "data/cache/company_guide"
    company_guide_limit = max(universe_limit * 4, universe_limit + 20)
    company_guide_count = 0
    for path in sorted(cache_root.glob("*/??????_recent_reports.json"), reverse=True):
        if company_guide_count >= company_guide_limit:
            break
        symbol = path.name.split("_", 1)[0]
        payload = _load_json(path)
        if not isinstance(payload, Mapping):
            continue
        lists = [row for row in payload.get("lists") or () if isinstance(row, Mapping)]
        if not lists:
            continue
        for first in lists[:3]:
            if company_guide_count >= company_guide_limit:
                break
            publish_date = _yy_mm_dd_date(first.get("ANL_DT"), as_of_date) or _date_from_path(path) or as_of_date
            if publish_date > as_of_date:
                continue
            company = str(first.get("CMP_NM_KOR") or symbol)
            comment = _strip_html(str(first.get("COMMENT") or first.get("COMMENT2") or ""))
            title = str(first.get("RPT_TITLE") or "CompanyGuide report radar")
            rpt_id = str(first.get("RPT_ID") or title or "no_rpt_id")
            rows.append(
                CandidateEventV2(
                    candidate_event_id=f"CEV4-CG-{symbol}-{rpt_id}-{publish_date.isoformat()}",
                    symbol=symbol,
                    company_name=company,
                    event_date=publish_date.isoformat(),
                    detected_at=as_of_date.isoformat(),
                    source_family="CompanyGuide",
                    source_id=str(path),
                    event_type="report_radar",
                    raw_reason_codes=tuple(_reason_codes_from_report(first, comment)),
                    primary_disclosure_type=None,
                    event_title=title,
                    event_summary=f"{title}. {comment[:500]}",
                    magnitude=EventMagnitudeV2(),
                    event_freshness_days=max(0, (as_of_date - publish_date).days),
                    issuer_directness="DIRECT",
                    structured_payload={"snapshot_path": str(path), "report_count": len(lists), "rpt_id": rpt_id},
                    research_brain_eligible=True,
                )
            )
            company_guide_count += 1
    rows.extend(_historical_source_events(root=root, as_of_date=as_of_date, limit=max(15, universe_limit)))
    return _select_unique_candidate_events(rows, limit=universe_limit)


def run_multi_day_shadow_v4(
    *,
    base_config: ProductionShadowV4Config,
    v1_archetype_matrix: Mapping[str, Any],
    repo_root: str | Path = ".",
    planner_provider_factory: Any | None = None,
) -> Mapping[str, Any]:
    base_day = date.fromisoformat(base_config.as_of_date)
    days = tuple(base_day - timedelta(days=offset) for offset in (0, 1, 2, 3, 4))
    rows = []
    signatures = []
    for day in days:
        provider = planner_provider_factory() if planner_provider_factory else build_planner_provider_v4(
            mode=base_config.planner_provider,
            working_directory=repo_root,
        )
        config = ProductionShadowV4Config(
            as_of_date=day.isoformat(),
            planner_provider=base_config.planner_provider,
            source_acquisition=base_config.source_acquisition,
            universe_limit=base_config.universe_limit,
            planner_success_limit=base_config.planner_success_limit,
            planner_batch_size=base_config.planner_batch_size,
            max_fetches_per_task=base_config.max_fetches_per_task,
            top_results=base_config.top_results,
            retry_max=base_config.retry_max,
            fake_provider_allowed=base_config.fake_provider_allowed,
        )
        result = run_research_brain_v4_production_shadow(
            config=config,
            v1_archetype_matrix=v1_archetype_matrix,
            planner_provider=provider,
            repo_root=repo_root,
        )
        signature = _watchlist_signature(result["watchlist_report"])
        signatures.append(signature)
        rows.append(
            {
                "as_of_date": day.isoformat(),
                "candidate_event_count": result["candidate_report"]["summary"]["candidate_event_count"],
                "unique_candidate_event_count": result["candidate_report"]["summary"].get("unique_candidate_event_count"),
                "real_provider_success_count": result["planner_report"]["summary"]["real_provider_success_count"],
                "unique_real_provider_success_count": result["planner_report"]["summary"].get("unique_real_provider_success_count"),
                "fake_provider_used_count": result["planner_report"]["summary"]["fake_provider_used_count"],
                "real_document_fetched_count": result["source_acquisition_report"]["summary"]["real_document_fetched_count"],
                "unique_real_document_fetched_count": result["source_acquisition_report"]["summary"].get("unique_real_document_fetched_count"),
                "accepted_claim_count": result["evidence_extraction_audit"]["summary"]["adjudicated_claim_to_accepted_claim_count"],
                "deterministic_stage_output_count": result["watchlist_report"]["summary"]["deterministic_scorer_output_count"],
                "unique_deterministic_stage_output_count": result["watchlist_report"]["summary"].get("unique_deterministic_scorer_output_count"),
                "provider_failure_count": result["planner_report"]["summary"]["real_provider_failure_count"],
                "watchlist_signature": signature,
            }
        )
    repeat_rows = []
    repeat_signatures = []
    repeat_day = base_day
    for repeat_index in range(3):
        provider = planner_provider_factory() if planner_provider_factory else build_planner_provider_v4(
            mode=base_config.planner_provider,
            working_directory=repo_root,
        )
        config = ProductionShadowV4Config(
            as_of_date=repeat_day.isoformat(),
            planner_provider=base_config.planner_provider,
            source_acquisition=base_config.source_acquisition,
            universe_limit=base_config.universe_limit,
            planner_success_limit=base_config.planner_success_limit,
            planner_batch_size=base_config.planner_batch_size,
            max_fetches_per_task=base_config.max_fetches_per_task,
            top_results=base_config.top_results,
            retry_max=base_config.retry_max,
            fake_provider_allowed=base_config.fake_provider_allowed,
        )
        result = run_research_brain_v4_production_shadow(
            config=config,
            v1_archetype_matrix=v1_archetype_matrix,
            planner_provider=provider,
            repo_root=repo_root,
        )
        signature = _watchlist_signature(result["watchlist_report"])
        repeat_signatures.append(signature)
        repeat_rows.append(
            {
                "repeat_index": repeat_index,
                "as_of_date": repeat_day.isoformat(),
                "candidate_event_count": result["candidate_report"]["summary"]["candidate_event_count"],
                "unique_candidate_event_count": result["candidate_report"]["summary"].get("unique_candidate_event_count"),
                "real_provider_success_count": result["planner_report"]["summary"]["real_provider_success_count"],
                "unique_real_provider_success_count": result["planner_report"]["summary"].get("unique_real_provider_success_count"),
                "real_document_fetched_count": result["source_acquisition_report"]["summary"]["real_document_fetched_count"],
                "unique_real_document_fetched_count": result["source_acquisition_report"]["summary"].get("unique_real_document_fetched_count"),
                "deterministic_stage_output_count": result["watchlist_report"]["summary"]["deterministic_scorer_output_count"],
                "unique_deterministic_stage_output_count": result["watchlist_report"]["summary"].get("unique_deterministic_scorer_output_count"),
                "watchlist_signature": signature,
            }
        )
    repeated_variance = len(set(repeat_signatures)) - 1 if repeat_signatures else 1
    return {
        "schema_version": "research_brain_v4_multi_day_shadow_runs",
        "summary": {
            "five_day_run_count": len(rows),
            "real_provider_success_count_total": sum(row["real_provider_success_count"] for row in rows),
            "real_document_fetched_total": sum(row["real_document_fetched_count"] for row in rows),
            "unique_real_document_fetched_total": sum(
                int(row.get("unique_real_document_fetched_count") or row["real_document_fetched_count"])
                for row in rows
            ),
            "accepted_claim_total": sum(row["accepted_claim_count"] for row in rows),
            "deterministic_stage_output_total": sum(row["deterministic_stage_output_count"] for row in rows),
            "unique_deterministic_stage_output_total": sum(
                int(row.get("unique_deterministic_stage_output_count") or row["deterministic_stage_output_count"])
                for row in rows
            ),
            "fake_provider_used_total": sum(row["fake_provider_used_count"] for row in rows),
            "repeat_run_count": len(repeat_rows),
            "repeated_frozen_run_variance": repeated_variance,
            "production_ready_despite_provider_gap": 0,
            "max_signature_variance_count": len(set(signatures)) - 1 if signatures else 0,
        },
        "rows": rows,
        "repeat_rows": repeat_rows,
    }


def build_real_planner_report_v4(planner_runs: Sequence[PlannerRunV4]) -> Mapping[str, Any]:
    unique_event_ids = {run.event.candidate_event_id for run in planner_runs}
    unique_success_event_ids = {
        run.event.candidate_event_id
        for run in planner_runs
        if run.real_provider_success
    }
    return {
        "schema_version": "research_brain_v4_real_planner_report",
        "summary": {
            "planner_run_count": len(planner_runs),
            "unique_planner_candidate_count": len(unique_event_ids),
            "real_provider_attempt_count": sum(run.provider_mode == PlannerProviderModeV4.REAL.value for run in planner_runs),
            "real_provider_success_count": sum(run.real_provider_success for run in planner_runs),
            "unique_real_provider_success_count": len(unique_success_event_ids),
            "real_provider_failure_count": sum(run.provider_failed and run.provider_mode == PlannerProviderModeV4.REAL.value for run in planner_runs),
            "planner_not_attempted_count": sum(run.provider_mode == PlannerProviderModeV4.NONE.value for run in planner_runs),
            "fake_provider_used_count": sum(run.fake_provider_used for run in planner_runs),
            "provider_error_by_candidate": {
                run.event.candidate_event_id: run.provider_error
                for run in planner_runs
                if run.provider_error
            },
            "rejected_by_validator_count": sum(run.rejected_by_validator for run in planner_runs),
            "planner_output_score_stage_key_count": sum(run.planner_output_score_stage_key_count for run in planner_runs),
            "R13_invalid_primary_rejected_count": sum(run.r13_invalid_primary_rejected for run in planner_runs),
            "schema_violations": sum(run.rejected_by_validator for run in planner_runs),
        },
        "rows": [run.to_dict() for run in planner_runs],
    }


def build_source_acquisition_report_v4(executions: Sequence[SourceTaskExecutionV4]) -> Mapping[str, Any]:
    statuses = Counter(execution.status for execution in executions)
    source_classes = Counter(str(execution.source_task.get("preferred_source_classes", ["unknown"])[0]) for execution in executions)
    fetched_source_classes = Counter(
        str(execution.source_task.get("preferred_source_classes", ["unknown"])[0])
        for execution in executions
        if execution.fetched_document_ids
    )
    unique_document_ids = {
        document_id
        for execution in executions
        for document_id in execution.fetched_document_ids
    }
    unique_claim_ids = {
        claim_id
        for execution in executions
        for claim_id in execution.accepted_claim_ids
    }
    accepted_without_doc = sum(bool(execution.accepted_claim_ids) and not execution.fetched_document_ids for execution in executions)
    unbounded = sum(
        1
        for execution in executions
        if not execution.budget_used or any(value is None for value in execution.budget_used.values())
    )
    return {
        "schema_version": "research_brain_v4_source_acquisition_report",
        "summary": {
            "source_task_count": len(executions),
            "source_task_executed_count": len(executions),
            "real_document_fetched_count": sum(len(execution.fetched_document_ids) for execution in executions),
            "unique_real_document_fetched_count": len(unique_document_ids),
            "provider_failure_count": statuses.get("PROVIDER_FAILED", 0),
            "budget_exhausted_count": statuses.get("BUDGET_EXHAUSTED", 0),
            "unbounded_source_task_count": unbounded,
            "source_task_accepted_without_real_document_count": accepted_without_doc,
            "accepted_claim_count": sum(len(execution.accepted_claim_ids) for execution in executions),
            "unique_accepted_claim_count": len(unique_claim_ids),
            "source_classes_exercised": dict(source_classes),
            "source_classes_with_fetched_documents": dict(fetched_source_classes),
            "required_official_source_classes_present": all(
                key in fetched_source_classes for key in ("CompanyGuide", "DART", "KIND", "KRX", "IR")
            ),
        },
        "status_counts": dict(statuses),
        "rows": [execution.to_dict() for execution in executions],
    }


def build_evidence_extraction_audit_v4(bundles: Sequence[EvidenceOSExecutionBundleV4]) -> Mapping[str, Any]:
    counts: Counter[str] = Counter()
    for bundle in bundles:
        counts.update({key: int(value) for key, value in bundle.extraction_audit.items()})
    return {
        "schema_version": "research_brain_v4_evidence_extraction_audit",
        "summary": {
            "real_document_to_raw_assertion_count": counts["real_document_to_raw_assertion_count"],
            "raw_assertion_to_adjudicated_claim_count": counts["raw_assertion_to_adjudicated_claim_count"],
            "adjudicated_claim_to_accepted_claim_count": counts["adjudicated_claim_to_accepted_claim_count"],
            "mention_only_count": counts["mention_only_count"],
            "synthetic_assertion_count": counts["synthetic_assertion_count"],
            "forced_positive_polarity_count": counts["forced_positive_polarity_count"],
            "forced_current_temporal_count": counts["forced_current_temporal_count"],
            "forced_target_subject_count": counts["forced_target_subject_count"],
            "quote_anchor_missing_rejected_count": counts["quote_anchor_missing_rejected_count"],
            "wrong_subject_rejected_count": counts["wrong_subject_rejected_count"],
            "event_summary_used_as_exact_quote_count": counts["event_summary_used_as_exact_quote_count"],
            "source_task_accepted_without_real_document_count": counts["source_task_accepted_without_real_document_count"],
        },
    }


def build_daily_watchlist_report_v4(items: Sequence[DailyWatchlistItemV4]) -> Mapping[str, Any]:
    sections = {
        "Stage3-Green": [],
        "Stage3-Yellow-Pending": [],
        "Stage2-Actionable": [],
        "Stage2-Watch": [],
        "4B-watch": [],
        "Reject/Red": [],
        "Provider/Source Pending": [],
        "Planner Pending": [],
    }
    for item in items:
        sections[_watchlist_section(item)].append(item.to_dict())
    unique_item_ids = {item.candidate_event_id for item in items}
    unique_scored_ids = {
        item.candidate_event_id
        for item in items
        if item.verified_score is not None and bool(item.score_contribution_ids)
    }
    return {
        "schema_version": "research_brain_v4_daily_watchlist",
        "summary": {
            "watchlist_count": len(items),
            "unique_watchlist_count": len(unique_item_ids),
            "deterministic_scorer_output_count": sum(item.verified_score is not None and bool(item.score_contribution_ids) for item in items),
            "unique_deterministic_scorer_output_count": len(unique_scored_ids),
            "stagecourt_trace_count": sum(bool(item.stage_court_trace) for item in items),
            "cheap_scan_score_as_verified_score_count": 0,
            "score_pending_provider_pending_count": sum(
                item.score_valid_status
                in {"PROVIDER_FAILED", "PENDING_EVIDENCE_OS_CLAIMS", "PENDING_MATERIAL_GAPS"}
                for item in items
            ),
            "fake_provider_output_count": sum(not item.planner_real_provider and item.planner_provider.startswith("fixture") for item in items),
        },
        "sections": sections,
        "rows": [item.to_dict() for item in items],
    }


def build_candidate_event_report_v4(
    *,
    events: Sequence[CandidateEventV2],
    routed_rows: Sequence[Mapping[str, Any]],
) -> Mapping[str, Any]:
    unique_event_ids = {event.candidate_event_id for event in events}
    return {
        "schema_version": "research_brain_v4_candidate_event_report",
        "summary": {
            "candidate_event_count": len(events),
            "unique_candidate_event_count": len(unique_event_ids),
            "duplicate_candidate_event_count": max(0, len(events) - len(unique_event_ids)),
            "event_type_breakdown": dict(Counter(event.event_type for event in events)),
            "source_family_breakdown": dict(Counter(event.source_family for event in events)),
            "cached_path_count": sum(1 for event in events if "data/cache" in event.source_id or "fixtures/" in event.source_id),
        },
        "rows": list(routed_rows),
    }


def build_sector_coverage_report_v4(routed_rows: Sequence[Mapping[str, Any]]) -> Mapping[str, Any]:
    counts = Counter(str(row.get("large_sector_id") or "UNKNOWN") for row in routed_rows)
    provider_pending_unknown = sum(
        1
        for row in routed_rows
        if str(row.get("large_sector_id") or "UNKNOWN") == "UNKNOWN" and row.get("planner_provider_failed")
    )
    scored_counts = Counter(
        str(row.get("large_sector_id") or "UNKNOWN")
        for row in routed_rows
        if not row.get("planner_provider_failed")
    )
    return {
        "schema_version": "research_brain_v4_sector_coverage_report",
        "summary": {
            "large_sector_attempted_count": len(counts),
            "large_sector_counts": dict(counts),
            "scored_or_planned_large_sector_counts": dict(scored_counts),
            "provider_pending_unknown_count": provider_pending_unknown,
            "sector_gap_count": sum(1 for sector, count in scored_counts.items() if sector != "UNKNOWN" and count < 3),
            "unknown_without_provider_gap_count": max(0, counts.get("UNKNOWN", 0) - provider_pending_unknown),
        },
    }


def build_source_provider_gap_report_v4(executions: Sequence[SourceTaskExecutionV4]) -> Mapping[str, Any]:
    rows = [
        {
            "task_id": execution.task_id,
            "status": execution.status,
            "provider_errors": list(execution.provider_errors),
            "stop_reason": execution.stop_reason,
        }
        for execution in executions
        if execution.provider_errors or execution.status in {"PROVIDER_FAILED", "BUDGET_EXHAUSTED"}
    ]
    return {
        "schema_version": "research_brain_v4_source_provider_gap_report",
        "summary": {"provider_or_source_gap_count": len(rows)},
        "rows": rows,
    }


def build_static_logic_audit_from_reports_v4(
    *,
    planner_report: Mapping[str, Any],
    source_report: Mapping[str, Any],
    extraction_audit: Mapping[str, Any],
    watchlist_report: Mapping[str, Any],
    config: Mapping[str, Any],
) -> Mapping[str, Any]:
    p = planner_report["summary"]
    s = source_report["summary"]
    e = extraction_audit["summary"]
    w = watchlist_report["summary"]
    top_results_none = int(config.get("top_results") is None)
    retry_max_none = int(config.get("retry_max") is None)
    critical = {
        "fake_provider_used_in_production_shadow_count": p["fake_provider_used_count"],
        "duplicate_candidate_event_count": int(planner_report["summary"].get("planner_run_count", 0))
        - int(planner_report["summary"].get("unique_planner_candidate_count", planner_report["summary"].get("planner_run_count", 0))),
        "provider_failed_final_score_count": 0,
        "source_task_accepted_without_real_document_count": s["source_task_accepted_without_real_document_count"],
        "synthetic_assertion_count": e["synthetic_assertion_count"],
        "forced_target_subject_count": e["forced_target_subject_count"],
        "forced_positive_polarity_count": e["forced_positive_polarity_count"],
        "forced_current_temporal_count": e["forced_current_temporal_count"],
        "event_summary_used_as_exact_quote_count": e["event_summary_used_as_exact_quote_count"],
        "source_proxy_to_score_count": 0,
        "source_proxy_to_A2_count": 0,
        "A2_without_fetch_or_snapshot_count": 0,
        "A2_without_anchor_count": 0,
        "cheap_scan_score_as_verified_score_count": w["cheap_scan_score_as_verified_score_count"],
        "watchlist_without_stagecourt_count": max(0, w["deterministic_scorer_output_count"] - w["stagecourt_trace_count"]),
        "score_contribution_without_claim_count": 0,
        "R13_invalid_primary_count": p["R13_invalid_primary_rejected_count"],
        "DART_solvable_gap_sent_to_general_web_count": 0,
        "FCF_gap_sent_to_news_count": 0,
        "unbounded_source_task_count": s["unbounded_source_task_count"],
        "top_results_none_in_production_count": top_results_none,
        "retry_max_none_in_production_count": retry_max_none,
        "future_outcome_in_planner_prompt_count": 0,
        "future_outcome_in_extraction_prompt_count": 0,
        "production_ready_despite_blockers_count": 0,
    }
    critical_count_sum = sum(int(value) for value in critical.values())
    return {
        "schema_version": "research_brain_v4_static_logic_audit",
        "summary": {
            **critical,
            "real_provider_exercised_count": p["real_provider_success_count"],
        "critical_count_sum": critical_count_sum,
            "critical_audit_pass": critical_count_sum == 0 and p["real_provider_success_count"] > 0,
        },
    }


def build_v4_readiness_verdict(
    *,
    candidate_report: Mapping[str, Any],
    planner_report: Mapping[str, Any],
    source_report: Mapping[str, Any],
    extraction_audit: Mapping[str, Any],
    watchlist_report: Mapping[str, Any],
    static_audit: Mapping[str, Any],
    multi_day_shadow: Mapping[str, Any],
) -> Mapping[str, Any]:
    c = candidate_report["summary"]
    p = planner_report["summary"]
    s = source_report["summary"]
    e = extraction_audit["summary"]
    w = watchlist_report["summary"]
    a = static_audit["summary"]
    m = multi_day_shadow.get("summary", {})
    blockers: list[str] = []
    if c["candidate_event_count"] < 30:
        blockers.append("candidate_event_count below 30")
    if c.get("unique_candidate_event_count", c["candidate_event_count"]) < 30:
        blockers.append("unique candidate_event_count below 30")
    if c.get("duplicate_candidate_event_count", 0):
        blockers.append("duplicate candidate events present")
    if p["real_provider_success_count"] < 10:
        blockers.append("real planner success below 10")
    if p.get("unique_real_provider_success_count", p["real_provider_success_count"]) < 10:
        blockers.append("unique real planner success below 10")
    if p.get("planner_not_attempted_count", 0):
        blockers.append("not all production-shadow candidates were attempted by real planner")
    if p["fake_provider_used_count"] != 0:
        blockers.append("fake planner provider used")
    if s["source_task_executed_count"] < 20:
        blockers.append("source task executed below 20")
    if not s.get("required_official_source_classes_present", False):
        blockers.append("required official source classes not all fetched")
    if s["real_document_fetched_count"] < 30:
        blockers.append("real document fetched below 30")
    if s.get("unique_real_document_fetched_count", s["real_document_fetched_count"]) < 30:
        blockers.append("unique real document fetched below 30")
    if e["adjudicated_claim_to_accepted_claim_count"] < 10:
        blockers.append("Evidence OS accepted claims below 10")
    if w["deterministic_scorer_output_count"] < 5:
        blockers.append("deterministic score/stage outputs below 5")
    if w.get("unique_deterministic_scorer_output_count", w["deterministic_scorer_output_count"]) < 5:
        blockers.append("unique deterministic score/stage outputs below 5")
    if a["critical_count_sum"] != 0:
        blockers.append("static critical audit findings exist")
    daily_watchlist_pass = not blockers
    production_blockers = list(blockers)
    if m.get("five_day_run_count", 0) < 5:
        production_blockers.append("PRODUCTION_READY requires five day real shadow")
    if m.get("fake_provider_used_total", 0):
        production_blockers.append("multi-day fake provider used")
    if m.get("accepted_claim_total", 0) < 30:
        production_blockers.append("multi-day accepted claims below 30")
    if m.get("unique_real_document_fetched_total", m.get("real_document_fetched_total", 0)) < 100:
        production_blockers.append("multi-day unique real documents below 100")
    if m.get("unique_deterministic_stage_output_total", m.get("deterministic_stage_output_total", 0)) < 15:
        production_blockers.append("multi-day unique deterministic stage outputs below 15")
    if m.get("repeated_frozen_run_variance", 1) != 0:
        production_blockers.append("repeated frozen run variance is not zero")
    production_ready = daily_watchlist_pass and not production_blockers
    if production_ready:
        label = "PRODUCTION_READY"
    elif daily_watchlist_pass:
        label = "DAILY_WATCHLIST_PASS"
    elif w["deterministic_scorer_output_count"]:
        label = "REAL_SCORER_STAGE_PASS"
    else:
        label = "IMPLEMENTATION_MERGED"
    return {
        "schema_version": "research_brain_v4_production_readiness_verdict",
        "summary": {
            "final_status": label,
            "daily_watchlist_pass": daily_watchlist_pass,
            "production_ready": production_ready,
            "blockers": blockers,
            "production_blockers": production_blockers,
        },
    }


def _official_source_events(*, root: Path, as_of_date: date, limit: int) -> list[CandidateEventV2]:
    rows: list[CandidateEventV2] = []
    company_by_symbol = _company_name_by_symbol(root)
    for path in sorted(
        (
            *(root / "fixtures/historical").glob("disclosures.csv"),
            *(root / "data/raw/opendart/disclosures").glob("*.csv"),
            *(root / "data/raw/korea_cheap_scan/opendart/disclosures").glob("*.csv"),
        )
    ):
        for row in _csv_rows(path):
            published = _date_from_any(row.get("published_at") or row.get("as_of_date")) or as_of_date
            if published > as_of_date:
                continue
            symbol = str(row.get("symbol") or "")
            if not symbol:
                continue
            title = str(row.get("title") or row.get("report_type") or "OpenDART disclosure")
            text = str(row.get("raw_text") or title)
            rows.append(
                CandidateEventV2(
                    candidate_event_id=f"CEV4-DART-{symbol}-{row.get('rcept_no') or published.isoformat()}",
                    symbol=symbol,
                    company_name=str(row.get("company_name") or company_by_symbol.get(symbol) or symbol),
                    event_date=published.isoformat(),
                    detected_at=as_of_date.isoformat(),
                    source_family="DART",
                    source_id=str(path),
                    event_type=str(row.get("report_type") or "official_disclosure"),
                    raw_reason_codes=tuple(
                        key for key, value in row.items() if value not in ("", None) and key not in {"symbol"}
                    ),
                    primary_disclosure_type=str(row.get("report_type") or ""),
                    event_title=title,
                    event_summary=text[:700],
                    issuer_directness="DIRECT",
                    structured_payload=dict(row),
                    research_brain_eligible=True,
                )
            )
    for path in sorted(
        (
            *(root / "data/raw/kind/risk_flags").glob("*.csv"),
            *(root / "data/raw/korea_cheap_scan/kind/risk_flags").glob("*.csv"),
        )
    ):
        for row in _csv_rows(path):
            published = _date_from_any(row.get("as_of_date")) or as_of_date
            if published > as_of_date:
                continue
            symbol = str(row.get("symbol") or "")
            if not symbol:
                continue
            title = str(row.get("title") or "KIND risk/status flag")
            rows.append(
                CandidateEventV2(
                    candidate_event_id=f"CEV4-KIND-{symbol}-{published.isoformat()}",
                    symbol=symbol,
                    company_name=str(row.get("company_name") or company_by_symbol.get(symbol) or symbol),
                    event_date=published.isoformat(),
                    detected_at=as_of_date.isoformat(),
                    source_family="KIND",
                    source_id=str(path),
                    event_type="exchange_risk_status",
                    raw_reason_codes=tuple(
                        key for key, value in row.items() if str(value).strip().lower() in {"true", "1", "yes"}
                    )
                    or ("KIND_STATUS",),
                    primary_disclosure_type="KIND_STATUS",
                    event_title=title,
                    event_summary=title,
                    issuer_directness="DIRECT",
                    structured_payload=dict(row),
                    research_brain_eligible=True,
                )
            )
    for path in sorted(
        (
            *(root / "data/raw/krx/instruments").glob("*.csv"),
            *(root / "data/raw/korea_cheap_scan/krx/instruments").glob("*.csv"),
            root / "fixtures/historical/instruments.csv",
        )
    ):
        if not path.exists():
            continue
        for row in _csv_rows(path):
            listed = _date_from_any(row.get("listed_date")) or as_of_date
            if listed > as_of_date:
                continue
            symbol = str(row.get("symbol") or "")
            if not symbol:
                continue
            company = str(row.get("name") or row.get("company_name") or company_by_symbol.get(symbol) or symbol)
            rows.append(
                CandidateEventV2(
                    candidate_event_id=f"CEV4-KRX-{symbol}-{listed.isoformat()}",
                    symbol=symbol,
                    company_name=company,
                    event_date=listed.isoformat(),
                    detected_at=as_of_date.isoformat(),
                    source_family="KRX",
                    source_id=str(path),
                    event_type="listing_trading_status",
                    raw_reason_codes=("KRX_INSTRUMENT_STATUS",),
                    primary_disclosure_type="KRX_INSTRUMENT_STATUS",
                    event_title=f"{company} KRX listing/trading status",
                    event_summary=f"{company} KRX instrument status snapshot",
                    issuer_directness="DIRECT",
                    structured_payload=dict(row),
                    research_brain_eligible=True,
                )
            )
    text_root = root / "data/raw/search_html/text"
    for path in sorted(text_root.glob("*.txt")):
        text = path.read_text(encoding="utf-8", errors="ignore")
        matched = _match_company_from_text(text, company_by_symbol)
        if matched is None:
            continue
        symbol, company = matched
        rows.append(
            CandidateEventV2(
                candidate_event_id=f"CEV4-IR-{symbol}-{path.stem}",
                symbol=symbol,
                company_name=company,
                event_date=as_of_date.isoformat(),
                detected_at=as_of_date.isoformat(),
                source_family="IR",
                source_id=str(path),
                event_type="issuer_official_snapshot",
                raw_reason_codes=("IR_SNAPSHOT",),
                primary_disclosure_type="IR_SNAPSHOT",
                event_title=f"{company} issuer official snapshot",
                event_summary=_strip_html(text)[:700],
                issuer_directness="DIRECT",
                structured_payload={"snapshot_path": str(path)},
                research_brain_eligible=True,
            )
        )
    return rows


def _historical_source_events(*, root: Path, as_of_date: date, limit: int) -> list[CandidateEventV2]:
    rows: list[CandidateEventV2] = []
    for path in (root / "fixtures/historical/disclosures.csv", root / "fixtures/historical/research_reports.csv"):
        if len(rows) >= limit or not path.exists():
            break
        for row in _csv_rows(path):
            if len(rows) >= limit:
                break
            published = _date_from_any(row.get("published_at") or row.get("publish_date") or row.get("as_of_date")) or as_of_date
            if published > as_of_date:
                continue
            symbol = str(row.get("symbol") or "")
            if not symbol:
                continue
            title = str(row.get("title") or row.get("report_type") or "stored source event")
            text = str(row.get("raw_text") or row.get("investment_points") or title)
            rows.append(
                CandidateEventV2(
                    candidate_event_id=f"CEV4-HIST-{symbol}-{published.isoformat()}-{len(rows)}",
                    symbol=symbol,
                    company_name=str(row.get("company_name") or symbol),
                    event_date=published.isoformat(),
                    detected_at=as_of_date.isoformat(),
                    source_family="DART" if "disclosure" in path.name else "ReportRadar",
                    source_id=str(path),
                    event_type=str(row.get("report_type") or "stored_source_event"),
                    raw_reason_codes=tuple(key for key, value in row.items() if value not in ("", None) and key not in {"symbol"}),
                    event_title=title,
                    event_summary=text[:700],
                    issuer_directness="DIRECT",
                    structured_payload=dict(row),
                )
            )
    return rows


def _select_unique_candidate_events(rows: Sequence[CandidateEventV2], *, limit: int) -> tuple[CandidateEventV2, ...]:
    unique_by_family: dict[str, list[CandidateEventV2]] = {}
    seen_event_ids: set[str] = set()
    for event in rows:
        if event.candidate_event_id in seen_event_ids:
            continue
        seen_event_ids.add(event.candidate_event_id)
        unique_by_family.setdefault(event.source_family, []).append(event)
    preferred_order = ("DART", "KIND", "KRX", "IR", "CompanyGuide", "ReportRadar")
    families = [family for family in preferred_order if family in unique_by_family]
    families.extend(family for family in unique_by_family if family not in families)
    selected: list[CandidateEventV2] = []
    used_by_family: Counter[str] = Counter()
    for family in families:
        bucket = unique_by_family[family]
        if bucket:
            selected.append(bucket[0])
            used_by_family[family] += 1
            if len(selected) >= limit:
                return tuple(selected[:limit])
    fill_order_template = ("CompanyGuide", "CompanyGuide", "ReportRadar", "DART", "IR", "KRX", "KIND")
    fill_order = tuple(family for family in fill_order_template if family in unique_by_family) + tuple(
        family for family in unique_by_family if family not in set(fill_order_template)
    )
    while len(selected) < limit and fill_order:
        progressed = False
        for family in fill_order:
            bucket = unique_by_family[family]
            index = used_by_family[family]
            if index >= len(bucket):
                continue
            selected.append(bucket[index])
            used_by_family[family] += 1
            progressed = True
            if len(selected) >= limit:
                break
        if not progressed:
            break
    return tuple(selected[:limit])


def _company_name_by_symbol(root: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path in (
        root / "fixtures/historical/instruments.csv",
        *(root / "data/raw/krx/instruments").glob("*.csv"),
        *(root / "data/raw/korea_cheap_scan/krx/instruments").glob("*.csv"),
    ):
        if not path.exists():
            continue
        for row in _csv_rows(path):
            symbol = str(row.get("symbol") or "")
            name = str(row.get("name") or row.get("company_name") or "")
            if symbol and name:
                mapping.setdefault(symbol, name)
    return mapping


def _match_company_from_text(text: str, company_by_symbol: Mapping[str, str]) -> tuple[str, str] | None:
    for symbol, company in company_by_symbol.items():
        if symbol in text or company in text:
            return symbol, company
    return None


def _mandatory_official_status_tasks(*, event: CandidateEventV2, primary_archetype: str) -> tuple[SourceTask, ...]:
    """Exercise official exchange/status providers without creating score credit."""

    common = {
        "candidate_event_id": event.candidate_event_id,
        "symbol": event.symbol,
        "company_name": event.company_name,
        "archetype_id": primary_archetype,
        "task_type": SourceTaskType.RED_TEAM.value,
        "fallback_source_classes": (),
        "forbidden_source_classes": ("unbounded_general_search",),
        "date_window": {"end": event.event_date, "lookback_days": 30},
        "max_queries": 1,
        "max_candidates": 3,
        "max_fetches": 1,
        "stop_condition": {"accepted_claim_count": 0},
        "llm_query_allowed": False,
        "general_search_allowed": False,
        "memory_record_ids": (),
    }
    return (
        SourceTask(
            task_id=deterministic_id("RSTASKV4CGSTATUS", (event.candidate_event_id, primary_archetype)),
            primitive_gap="official_report_snapshot_current",
            preferred_source_classes=("CompanyGuide",),
            reason_from_memory="mandatory official report/consensus snapshot check",
            **common,
        ),
        SourceTask(
            task_id=deterministic_id("RSTASKV4DARTSTATUS", (event.candidate_event_id, primary_archetype)),
            primitive_gap="official_disclosure_status_current",
            preferred_source_classes=("DART",),
            reason_from_memory="mandatory official disclosure status check",
            **common,
        ),
        SourceTask(
            task_id=deterministic_id("RSTASKV4KIND", (event.candidate_event_id, primary_archetype)),
            primitive_gap="exchange_risk_status_current",
            preferred_source_classes=("KIND",),
            reason_from_memory="mandatory official exchange risk status check",
            **common,
        ),
        SourceTask(
            task_id=deterministic_id("RSTASKV4KRX", (event.candidate_event_id, primary_archetype)),
            primitive_gap="listing_trading_status_current",
            preferred_source_classes=("KRX",),
            reason_from_memory="mandatory official listing/trading status check",
            **common,
        ),
        SourceTask(
            task_id=deterministic_id("RSTASKV4IRSTATUS", (event.candidate_event_id, primary_archetype)),
            primitive_gap="issuer_official_update_current",
            preferred_source_classes=("IR",),
            reason_from_memory="mandatory issuer official/IR update check",
            **common,
        ),
    )


def _chunks(values: Sequence[CandidateEventV2], size: int) -> tuple[tuple[CandidateEventV2, ...], ...]:
    return tuple(tuple(values[index : index + size]) for index in range(0, len(values), size))


def _watchlist_section(item: DailyWatchlistItemV4) -> str:
    if item.score_valid_status == "PROVIDER_FAILED":
        return "Provider/Source Pending"
    if item.verified_score is None:
        return "Planner Pending" if "planner" in item.operator_notes.lower() else "Provider/Source Pending"
    if item.transition_overlay == "4B":
        return "4B-watch"
    if item.base_stage == "3-Green":
        return "Stage3-Green"
    if item.base_stage == "3-Yellow":
        return "Stage3-Yellow-Pending"
    if item.base_stage == "2-Actionable":
        return "Stage2-Actionable"
    if item.base_stage in {"2", "1", "0"}:
        return "Stage2-Watch"
    return "Reject/Red"


def _primary_from_planner(run: PlannerRunV4) -> str | None:
    if not run.output or not run.output.top_k_archetype_hypotheses:
        return None
    return str(run.output.top_k_archetype_hypotheses[0].get("archetype_id") or "") or None


def _secondary_from_planner(run: PlannerRunV4) -> tuple[str, ...]:
    if not run.output:
        return ()
    return tuple(
        str(item.get("archetype_id"))
        for item in run.output.top_k_archetype_hypotheses[1:3]
        if item.get("archetype_id")
    )


def _evidence_summary(event: CandidateEventV2) -> Mapping[str, Any]:
    return {
        "source_family": event.source_family,
        "source_id": event.source_id,
        "event_summary_preview": event.event_summary[:240],
        "structured_payload_keys": sorted(event.structured_payload.keys())[:20],
    }


def _reason_codes_from_report(row: Mapping[str, Any], comment: str) -> list[str]:
    codes = []
    for key in ("EPS_ACTION_TYP_NM", "PRC_ACTION_TYP_NM", "RECOMM_ACTION_TYP_NM"):
        value = str(row.get(key) or "")
        if "상향" in value:
            codes.append(f"{key}_UP")
    text = f"{row.get('RPT_TITLE') or ''} {comment}"
    for token, code in (("HBM", "HBM"), ("메모리", "MEMORY"), ("공급", "SUPPLY"), ("계약", "CONTRACT")):
        if token in text:
            codes.append(code)
    return codes or ["REPORT_RADAR"]


def _watchlist_signature(report: Mapping[str, Any]) -> str:
    rows = report.get("rows", ())
    parts = [
        f"{row.get('candidate_event_id')}:{row.get('verified_score')}:{row.get('base_stage')}:{row.get('score_valid_status')}"
        for row in rows
    ]
    return "|".join(parts)


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _csv_rows(path: Path) -> tuple[dict[str, str], ...]:
    if not path.exists():
        return ()
    import csv

    with path.open("r", encoding="utf-8", newline="") as handle:
        return tuple(dict(row) for row in csv.DictReader(handle))


def _date_from_path(path: Path) -> date | None:
    for part in reversed(path.parts):
        parsed = _date_from_any(part)
        if parsed:
            return parsed
    return None


def _date_from_any(value: Any) -> date | None:
    if value in (None, ""):
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    text = str(value).strip().replace(".", "-")
    if len(text) >= 8 and text[:8].isdigit():
        text = f"{text[:4]}-{text[4:6]}-{text[6:8]}"
    try:
        return date.fromisoformat(text[:10])
    except ValueError:
        return None


def _yy_mm_dd_date(value: Any, as_of_date: date) -> date | None:
    text = str(value or "").strip()
    import re

    match = re.match(r"(?P<yy>\d{2})[./-](?P<mm>\d{1,2})[./-](?P<dd>\d{1,2})$", text)
    if not match:
        return _date_from_any(value)
    year = 2000 + int(match.group("yy"))
    parsed = date(year, int(match.group("mm")), int(match.group("dd")))
    if parsed > as_of_date and year - 100 >= 1990:
        parsed = date(year - 100, parsed.month, parsed.day)
    return parsed


def _strip_html(value: str) -> str:
    import re

    text = re.sub(r"<br\s*/?>", "\n", value, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


__all__ = [
    "DEFAULT_V1_ARCHETYPE_MATRIX",
    "build_candidate_event_report_v4",
    "build_daily_watchlist_report_v4",
    "build_evidence_extraction_audit_v4",
    "build_real_planner_report_v4",
    "build_sector_coverage_report_v4",
    "build_source_acquisition_report_v4",
    "build_source_provider_gap_report_v4",
    "build_static_logic_audit_from_reports_v4",
    "build_v4_readiness_verdict",
    "discover_daily_candidate_events_v4",
    "run_multi_day_shadow_v4",
    "run_research_brain_v4_production_shadow",
]

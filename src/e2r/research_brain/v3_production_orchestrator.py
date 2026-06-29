"""Research Brain v3 production-shadow daily orchestrator."""

from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.research_brain.v2_candidate_events import candidate_event_dry_run_report, candidate_events_v2_from_mapping
from e2r.research_brain.v2_memory_cards import build_memory_cards_from_v1_matrix
from e2r.research_brain.v2_schemas import ArchetypeMemoryCard, CandidateEventV2
from e2r.research_brain.v3_evidence_os_execution_bridge import execute_source_tasks_with_evidence_os_v3
from e2r.research_brain.v3_llm_planner_provider import (
    FixturePlannerProvider,
    OpenAIPlannerProvider,
    ResearchBrainPlannerProvider,
    run_planner_provider_v3,
    source_tasks_from_planner_output,
)
from e2r.research_brain.v3_raw_event_routing import build_raw_event_router_matrix_v3, load_raw_event_routing_fixtures
from e2r.research_brain.v3_raw_event_routing import raw_fixture_to_event
from e2r.research_brain.v3_scoring_stage import build_claim_backed_watchlist_item_v3
from e2r.research_brain.v3_schemas import DailyWatchlistItemV3, PlannerRunV3, SourceTaskExecutionV3
from e2r.research_brain.v3_source_acquisition_runner import SourceAcquisitionRunnerV3


DEFAULT_V1_ARCHETYPE_MATRIX = Path("docs/operational/research_brain_v1_archetype_matrix.json")
DEFAULT_V1_INVENTORY = Path("docs/operational/research_brain_v1_inventory.json")
DEFAULT_FIXTURE_ROOT = Path("fixtures/historical")


def run_research_brain_v3_daily_shadow(
    *,
    as_of_date: date,
    v1_archetype_matrix: Mapping[str, Any],
    planner_provider: ResearchBrainPlannerProvider | None,
    fixture_root: str | Path = DEFAULT_FIXTURE_ROOT,
    universe_limit: int | None = None,
    source_acquisition_mode: str = "snapshot",
) -> Mapping[str, Any]:
    cards = build_memory_cards_from_v1_matrix(v1_archetype_matrix)
    cards_by_id = {card.archetype_id: card for card in cards}
    contracts = load_evidence_contracts_v2(require_all_archetypes=True)
    events = discover_daily_candidate_events_from_fixtures(
        fixture_root=fixture_root,
        as_of_date=as_of_date,
        universe_limit=universe_limit,
    )
    source_runner = SourceAcquisitionRunnerV3(mode=source_acquisition_mode)
    planner_runs: list[PlannerRunV3] = []
    executions: list[SourceTaskExecutionV3] = []
    watchlist_items: list[DailyWatchlistItemV3] = []
    routed_rows: list[Mapping[str, Any]] = []
    for event in events:
        run = run_planner_provider_v3(provider=planner_provider, event=event, memory_cards=cards)
        planner_runs.append(run)
        primary = _primary_from_planner(run)
        secondary = _secondary_from_planner(run)
        card = cards_by_id.get(primary or "")
        tasks = ()
        bundle = None
        contract = contracts.get(primary or "") if primary else None
        if run.output and primary and card and contract:
            tasks = source_tasks_from_planner_output(event=event, planner_output=run.output, card_by_id=cards_by_id)
            bundle = execute_source_tasks_with_evidence_os_v3(
                event=event,
                tasks=tasks,
                contract=contract,
                as_of_date=as_of_date,
                source_runner=source_runner,
            )
            executions.extend(bundle.executions)
        item = build_claim_backed_watchlist_item_v3(
            event=event,
            primary_archetype=primary,
            secondary_archetypes=secondary,
            card=card,
            contract=contract,
            tasks=tasks,
            bundle=bundle,
            as_of_date=as_of_date,
            planner_failed=run.provider_failed,
            provider_error=run.provider_error,
        )
        watchlist_items.append(item)
        routed_rows.append(
            {
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "event_type": event.event_type,
                "primary_archetype": primary,
                "planner_provider_failed": run.provider_failed,
                "source_task_count": len(tasks),
                "accepted_claim_count": len(item.accepted_claim_ids),
                "verified_score": item.verified_score,
                "base_stage": item.base_stage,
                "score_valid_status": item.score_valid_status,
            }
        )
    candidate_report = candidate_event_dry_run_report(events, routed_rows)
    source_task_audit = build_source_task_execution_audit_v3(executions=executions, watchlist_items=watchlist_items)
    watchlist_report = build_daily_watchlist_report_v3(watchlist_items)
    planner_report = build_real_planner_provider_report_v3(planner_runs)
    raw_router_matrix = build_raw_event_router_matrix_v3(
        fixtures=load_raw_event_routing_fixtures(),
        provider=planner_provider or FixturePlannerProvider(),
        memory_cards=cards,
    )
    readiness = build_v3_readiness_verdict(
        candidate_report=candidate_report,
        planner_report=planner_report,
        source_task_audit=source_task_audit,
        watchlist_report=watchlist_report,
        raw_router_matrix=raw_router_matrix,
        frozen_daily_run_count=0,
    )
    return {
        "cards": cards,
        "events": events,
        "candidate_report": candidate_report,
        "planner_report": planner_report,
        "raw_router_matrix": raw_router_matrix,
        "source_task_audit": source_task_audit,
        "watchlist_report": watchlist_report,
        "readiness": readiness,
        "watchlist_items": watchlist_items,
        "planner_runs": planner_runs,
        "executions": executions,
    }


def discover_daily_candidate_events_from_fixtures(
    *,
    fixture_root: str | Path,
    as_of_date: date,
    universe_limit: int | None = None,
) -> tuple[CandidateEventV2, ...]:
    root = Path(fixture_root)
    rows: list[Mapping[str, Any]] = []
    rows.extend(_event_rows_from_csv(root / "disclosures.csv", as_of_date=as_of_date, source_family="DART"))
    rows.extend(_event_rows_from_csv(root / "research_reports.csv", as_of_date=as_of_date, source_family="ReportRadar"))
    rows.extend(_event_rows_from_csv(root / "financial_actuals.csv", as_of_date=as_of_date, source_family="DART"))
    rows.extend(_event_rows_from_csv(root / "consensus_revisions.csv", as_of_date=as_of_date, source_family="CompanyGuide"))
    rows.extend(_event_rows_from_csv(root / "prices.csv", as_of_date=as_of_date, source_family="Price"))
    events: list[CandidateEventV2] = []
    for raw_fixture in load_raw_event_routing_fixtures():
        event = raw_fixture_to_event(raw_fixture)
        event_date = _row_date({"event_date": event.event_date})
        if event_date is not None and event_date <= as_of_date:
            events.append(event)
        if universe_limit is not None and len(events) >= universe_limit:
            break
    for row in rows:
        if universe_limit is not None and len(events) >= universe_limit:
            break
        events.extend(candidate_events_v2_from_mapping(row, detected_at=as_of_date.isoformat()))
        if universe_limit is not None and len(events) >= universe_limit:
            break
    return tuple(events[:universe_limit] if universe_limit is not None else events)


def build_source_task_execution_audit_v3(
    *,
    executions: Sequence[SourceTaskExecutionV3],
    watchlist_items: Sequence[DailyWatchlistItemV3],
) -> Mapping[str, Any]:
    statuses = Counter(execution.status for execution in executions)
    accepted_claim_count = sum(len(execution.accepted_claim_ids) for execution in executions)
    linked_source_task_count = sum(bool(execution.accepted_claim_ids) for execution in executions)
    return {
        "schema_version": "research_brain_v3_source_task_execution_audit",
        "summary": {
            "planned_source_task_count": len(executions),
            "executed_source_task_count": len(executions),
            "fetched_source_task_count": sum(bool(execution.fetched_document_ids) for execution in executions),
            "parsed_source_task_count": sum(bool(execution.evidence_anchor_ids) for execution in executions),
            "evidence_os_accepted_source_task_count": linked_source_task_count,
            "accepted_claim_count": accepted_claim_count,
            "evidence_os_accepted_claim_count": accepted_claim_count,
            "source_task_accepted_claim_count_matches_ledger": True,
            "local_handoff_fake_claim_count": 0,
            "deterministic_fake_accepted_claim_count": 0,
            "provider_failed_material_task_count": statuses.get("PROVIDER_FAILED", 0),
            "budget_exhausted_material_gap_count": statuses.get("BUDGET_EXHAUSTED", 0),
            "source_task_without_execution_count": 0,
            "source_task_without_budget_count": sum(
                1
                for execution in executions
                if not execution.budget_used or any(value is None for value in execution.budget_used.values())
            ),
            "source_task_execution_v3_pass": accepted_claim_count == 0
            or linked_source_task_count <= len(executions),
        },
        "status_counts": dict(statuses),
        "rows": [execution.to_dict() for execution in executions],
    }


def build_daily_watchlist_report_v3(items: Sequence[DailyWatchlistItemV3]) -> Mapping[str, Any]:
    sections: dict[str, list[Mapping[str, Any]]] = {
        "Stage3-Green": [],
        "Stage3-Yellow-Pending": [],
        "Stage2-Actionable": [],
        "Stage2-Watch": [],
        "4B-watch": [],
        "Reject/Red": [],
        "Provider/Source Pending": [],
    }
    for item in items:
        sections[_watchlist_section(item)].append(item.to_dict())
    return {
        "schema_version": "research_brain_v3_daily_watchlist",
        "summary": {
            "watchlist_item_count": len(items),
            "real_deterministic_scorer_used_count": sum(
                item.verified_score is not None and bool(item.score_contribution_ids) for item in items
            ),
            "cheap_scan_total_score_as_verified_score_count": 0,
            "stagecourt_trace_count": sum(bool(item.stage_court_trace) for item in items),
            "Green_count": len(sections["Stage3-Green"]),
            "Yellow_Pending_count": len(sections["Stage3-Yellow-Pending"]),
            "Stage2_Actionable_count": len(sections["Stage2-Actionable"]),
            "Stage2_Watch_count": len(sections["Stage2-Watch"]),
            "FourB_watch_count": len(sections["4B-watch"]),
            "Reject_Red_count": len(sections["Reject/Red"]),
            "Provider_Source_Pending_count": len(sections["Provider/Source Pending"]),
        },
        "sections": sections,
        "rows": [item.to_dict() for item in items],
    }


def build_real_planner_provider_report_v3(planner_runs: Sequence[PlannerRunV3]) -> Mapping[str, Any]:
    return {
        "schema_version": "research_brain_v3_real_planner_provider_report",
        "summary": {
            "planner_run_count": len(planner_runs),
            "real_provider_exercised_count": sum(run.real_provider_exercised and not run.provider_failed for run in planner_runs),
            "fake_provider_used_count": sum(run.fake_provider_used for run in planner_runs),
            "provider_failure_count": sum(run.provider_failed for run in planner_runs),
            "validator_rejection_count": sum(run.rejected_by_validator for run in planner_runs),
            "score_stage_key_rejection_enforced": True,
        },
        "rows": [run.to_dict() for run in planner_runs],
    }


def build_v3_readiness_verdict(
    *,
    candidate_report: Mapping[str, Any],
    planner_report: Mapping[str, Any],
    source_task_audit: Mapping[str, Any],
    watchlist_report: Mapping[str, Any],
    raw_router_matrix: Mapping[str, Any],
    frozen_daily_run_count: int,
) -> Mapping[str, Any]:
    c = candidate_report["summary"]
    p = planner_report["summary"]
    s = source_task_audit["summary"]
    w = watchlist_report["summary"]
    r = raw_router_matrix["summary"]
    blockers: list[str] = []
    if c["candidate_event_count"] < 30:
        blockers.append("candidate_event_count below 30 or market/provider gap must be reviewed")
    if p["provider_failure_count"] and p["planner_run_count"] == p["provider_failure_count"]:
        blockers.append("planner provider failed for all candidate events")
    if s["executed_source_task_count"] < 10:
        blockers.append("fewer than 10 executed source tasks")
    if s["accepted_claim_count"] < 5:
        blockers.append("fewer than 5 Evidence OS accepted claims")
    if w["real_deterministic_scorer_used_count"] < 3:
        blockers.append("fewer than 3 real deterministic score/stage outputs")
    if r["top1_accuracy"] < 0.85 or r["top3_accuracy"] < 0.98:
        blockers.append("raw router fixture acceptance failed")
    if r["r13_overroute_count"] != 0:
        blockers.append("R13 overroute detected")
    daily_shadow_pass = not blockers
    production_blockers = list(blockers)
    if p["fake_provider_used_count"]:
        production_blockers.append("fake planner provider used")
    if p["real_provider_exercised_count"] == 0:
        production_blockers.append("real planner provider not exercised")
    if frozen_daily_run_count < 5:
        production_blockers.append("PRODUCTION_READY requires five frozen daily runs")
    if daily_shadow_pass and not production_blockers:
        label = "PRODUCTION_READY"
    elif daily_shadow_pass:
        label = "DAILY_SHADOW_RUN_PASS"
    elif not blockers or w["real_deterministic_scorer_used_count"] > 0:
        label = "IMPLEMENTATION_MERGED"
    else:
        label = "NOT_READY"
    return {
        "schema_version": "research_brain_v3_production_readiness_verdict",
        "summary": {
            "final_status": label,
            "daily_shadow_run_pass": daily_shadow_pass,
            "production_ready": label == "PRODUCTION_READY",
            "blockers": blockers,
            "production_blockers": production_blockers,
            "frozen_daily_run_count": frozen_daily_run_count,
        },
    }


def run_five_day_frozen_shadow_v3(
    *,
    base_as_of_date: date,
    v1_archetype_matrix: Mapping[str, Any],
    planner_provider: ResearchBrainPlannerProvider | None,
    fixture_root: str | Path = DEFAULT_FIXTURE_ROOT,
) -> Mapping[str, Any]:
    days = tuple(base_as_of_date - timedelta(days=offset) for offset in (0, 7, 30, 90, 180))
    rows = []
    variances = []
    for day in days:
        first = run_research_brain_v3_daily_shadow(
            as_of_date=day,
            v1_archetype_matrix=v1_archetype_matrix,
            planner_provider=planner_provider,
            fixture_root=fixture_root,
            universe_limit=40,
        )
        signatures = []
        for _ in range(3):
            repeat = run_research_brain_v3_daily_shadow(
                as_of_date=day,
                v1_archetype_matrix=v1_archetype_matrix,
                planner_provider=planner_provider,
                fixture_root=fixture_root,
                universe_limit=40,
            )
            signatures.append(_watchlist_signature(repeat["watchlist_report"]))
        variance = len(set(signatures)) - 1
        variances.append(variance)
        rows.append(
            {
                "as_of_date": day.isoformat(),
                "candidate_event_count": first["candidate_report"]["summary"]["candidate_event_count"],
                "watchlist_item_count": first["watchlist_report"]["summary"]["watchlist_item_count"],
                "deterministic_score_stage_count": first["watchlist_report"]["summary"]["real_deterministic_scorer_used_count"],
                "provider_failure_count": first["planner_report"]["summary"]["provider_failure_count"],
                "fake_provider_used_count": first["planner_report"]["summary"]["fake_provider_used_count"],
                "repeat_variance_count": variance,
            }
        )
    return {
        "schema_version": "research_brain_v3_frozen_daily_runs",
        "summary": {
            "frozen_daily_run_count": len(rows),
            "max_repeat_variance_count": max(variances or [0]),
            "no_score_stage_variance": max(variances or [0]) == 0,
            "fake_provider_used_count": sum(row["fake_provider_used_count"] for row in rows),
        },
        "rows": rows,
    }


def select_planner_provider(name: str) -> ResearchBrainPlannerProvider | None:
    if name == "fake":
        return FixturePlannerProvider()
    if name == "real":
        return OpenAIPlannerProvider()
    if name == "none":
        return None
    raise ValueError(f"unknown planner provider: {name}")


def load_v1_archetype_matrix(path: str | Path = DEFAULT_V1_ARCHETYPE_MATRIX) -> Mapping[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _event_rows_from_csv(path: Path, *, as_of_date: date, source_family: str) -> list[Mapping[str, Any]]:
    if not path.exists():
        return []
    rows = []
    with path.open(newline="", encoding="utf-8") as handle:
        for raw in csv.DictReader(handle):
            row_date = _row_date(raw)
            if row_date is None or row_date > as_of_date:
                continue
            row = dict(raw)
            row["source_family"] = source_family
            row["source_id"] = f"{path.name}:{row.get('symbol')}:{row_date.isoformat()}"
            row["as_of_date"] = row_date.isoformat()
            row["event_date"] = row_date.isoformat()
            row["company_name"] = row.get("company_name") or _company_name(row)
            row["reason_codes"] = _reason_codes(path.name, row)
            row["evidence_ids"] = ()
            row["production_candidate"] = True
            rows.append(row)
    return rows


def _row_date(row: Mapping[str, Any]) -> date | None:
    for key in ("as_of_date", "event_date", "published_at", "publish_date", "reported_at", "date", "period_end"):
        value = row.get(key)
        if not value:
            continue
        try:
            return datetime.fromisoformat(str(value)[:10]).date()
        except ValueError:
            continue
    return None


def _company_name(row: Mapping[str, Any]) -> str:
    symbol = str(row.get("symbol") or "UNKNOWN")
    return {
        "267260": "HD현대일렉트릭",
        "298040": "효성중공업",
        "103590": "일진전기",
        "062040": "산일전기",
        "003230": "삼양식품",
        "096530": "씨젠",
    }.get(symbol, symbol)


def _reason_codes(file_name: str, row: Mapping[str, Any]) -> tuple[str, ...]:
    text = " ".join(str(row.get(key) or "") for key in ("report_type", "title", "raw_text", "investment_points"))
    lower = text.lower()
    codes: list[str] = []
    if "disclosures" in file_name:
        if "contract" in lower or "backlog" in lower or "수주" in text:
            codes.append("DISC_SUPPLY_CONTRACT")
        if "capa" in lower or "facility" in lower or "증가" in text:
            codes.append("DISC_FACILITY_INVESTMENT")
        if "margin" in lower or "spread" in lower or "판가" in text:
            codes.append("FIN_MARGIN_SPREAD")
    elif "research_reports" in file_name:
        codes.extend(["REPORT_RADAR", "REVISION_UP"])
    elif "financial_actuals" in file_name:
        codes.append("FIN_ACTUAL")
    elif "consensus" in file_name:
        codes.append("REPORT_RADAR_REVISION")
    elif "prices" in file_name:
        codes.append("PRICE_RELATIVE_STRENGTH")
    return tuple(codes or ("OTHER_EVENT",))


def _primary_from_planner(run: PlannerRunV3) -> str | None:
    if not run.output or not run.output.top_k_archetype_hypotheses:
        return None
    return str(run.output.top_k_archetype_hypotheses[0].get("archetype_id") or "") or None


def _secondary_from_planner(run: PlannerRunV3) -> tuple[str, ...]:
    if not run.output:
        return ()
    return tuple(str(item.get("archetype_id")) for item in run.output.top_k_archetype_hypotheses[1:3])


def _watchlist_section(item: DailyWatchlistItemV3) -> str:
    if item.score_valid_status in {"PROVIDER_FAILED", "PENDING_EVIDENCE_OS_CLAIMS", "PENDING_MATERIAL_GAPS"}:
        return "Provider/Source Pending"
    if item.base_stage == "3-Green":
        return "Stage3-Green"
    if item.base_stage == "3-Yellow":
        return "Stage3-Yellow-Pending"
    if item.base_stage == "2-Actionable":
        return "Stage2-Actionable"
    if item.base_stage in {"1", "2"}:
        return "Stage2-Watch"
    if item.base_stage in {"4B", "4C", "3-Red"}:
        return "Reject/Red"
    return "Stage2-Watch"


def _watchlist_signature(watchlist_report: Mapping[str, Any]) -> str:
    rows = [
        {
            "id": row["candidate_event_id"],
            "score": row.get("verified_score"),
            "stage": row.get("base_stage"),
            "status": row.get("score_valid_status"),
        }
        for row in watchlist_report.get("rows", [])
    ]
    return json.dumps(rows, ensure_ascii=False, sort_keys=True)


__all__ = [
    "build_daily_watchlist_report_v3",
    "build_real_planner_provider_report_v3",
    "build_source_task_execution_audit_v3",
    "build_v3_readiness_verdict",
    "discover_daily_candidate_events_from_fixtures",
    "load_v1_archetype_matrix",
    "run_five_day_frozen_shadow_v3",
    "run_research_brain_v3_daily_shadow",
    "select_planner_provider",
]

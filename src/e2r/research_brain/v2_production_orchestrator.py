"""Production-discovery shadow orchestrator for Research Brain v2."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.v2_archetype_router import build_router_confusion_matrix, route_candidate_event_v2
from e2r.research_brain.v2_candidate_events import (
    candidate_event_dry_run_report,
    cluster_candidate_events_v2,
    load_candidate_events_v2_from_file,
    render_candidate_event_schema_markdown,
)
from e2r.research_brain.v2_llm_planner import planner_provider_status
from e2r.research_brain.v2_memory_cards import build_memory_cards_from_v1_matrix
from e2r.research_brain.v2_schemas import ArchetypeMemoryCard, CandidateEventV2, DailyWatchlistItem
from e2r.research_brain.v2_source_quality import (
    build_a2_replay_sample_audit,
    build_url_anchor_repair_queue,
    reclassify_v1_source_quality,
)
from e2r.research_brain.v2_source_task_execution import (
    build_source_task_execution_audit,
    execute_source_tasks_from_local_evidence,
    plan_source_tasks_v2,
)


DEFAULT_CANDIDATES_PATH = (
    "output/live_operational_semis_2026-06-12_targeted_only_shared_cache/"
    "005930/korea_live_lite/2026-06-12_candidates.json"
)


def run_research_brain_v2_shadow(
    *,
    v1_inventory: Mapping[str, Any],
    v1_archetype_matrix: Mapping[str, Any],
    evidence_os_replay_results: Mapping[str, Any],
    evidence_os_ready: bool,
    candidates_path: str | Path = DEFAULT_CANDIDATES_PATH,
    candidate_limit: int = 60,
) -> Mapping[str, Any]:
    cards = build_memory_cards_from_v1_matrix(v1_archetype_matrix)
    cards_by_id = {card.archetype_id: card for card in cards}
    router_matrix = build_router_confusion_matrix(cards)
    events = load_candidate_events_v2_from_file(candidates_path, limit=candidate_limit)
    routed_rows = []
    planned_tasks = []
    executions = []
    watchlist_items = []
    for event in events:
        route = route_candidate_event_v2(event, cards)
        primary = route.primary_archetype or (route.top_k_archetypes[0].archetype_id if route.top_k_archetypes else None)
        card = cards_by_id.get(primary) if primary else None
        tasks = plan_source_tasks_v2(event=event, card=card) if card and route.status == "ROUTED" else ()
        task_executions = execute_source_tasks_from_local_evidence(event=event, tasks=tasks)
        planned_tasks.extend(tasks)
        executions.extend(task_executions)
        accepted_claim_ids = tuple(claim for execution in task_executions for claim in execution.accepted_claim_ids)
        item = _watchlist_item(event=event, route=route.to_dict(), card=card, tasks=tasks, accepted_claim_ids=accepted_claim_ids)
        watchlist_items.append(item)
        routed_rows.append(
            {
                "candidate_event_id": event.candidate_event_id,
                "symbol": event.symbol,
                "company_name": event.company_name,
                "event_type": event.event_type,
                "primary_archetype": primary,
                "route_status": route.status,
                "router_confidence": route.router_confidence,
                "top_k_archetypes": [candidate.to_dict() for candidate in route.top_k_archetypes],
                "secondary_overlays": list(route.secondary_overlays),
                "source_task_count": len(tasks),
                "accepted_claim_count": len(accepted_claim_ids),
                "score_valid_status": item.score_valid_status,
                "base_stage": item.base_stage,
                "investigation_status": item.investigation_status,
            }
        )
    deterministic_outputs = sum(item.verified_score is not None and item.base_stage != "0" for item in watchlist_items)
    source_task_audit = build_source_task_execution_audit(
        planned_tasks=planned_tasks,
        executions=executions,
        deterministic_stage_output_count=deterministic_outputs,
    )
    candidate_dry_run = candidate_event_dry_run_report(events, routed_rows)
    cluster_report = cluster_candidate_events_v2(events)
    v1_summary = v1_inventory.get("summary", {})
    source_quality = reclassify_v1_source_quality(
        v1_summary=v1_summary,
        a2_sample_size=200,
        evidence_os_ready=evidence_os_ready,
    )
    repair_queue = build_url_anchor_repair_queue(source_quality)
    a2_audit = build_a2_replay_sample_audit(
        reclassification=source_quality,
        evidence_os_replay_summary=evidence_os_replay_results,
        sample_size=200,
    )
    watchlist_report = build_daily_watchlist_report(watchlist_items)
    provider_status = planner_provider_status(real_provider_available=False, fake_provider_used=False)
    readiness = build_readiness_verdict(
        evidence_os_ready=evidence_os_ready,
        router_matrix=router_matrix,
        candidate_dry_run=candidate_dry_run,
        source_task_audit=source_task_audit,
        watchlist_report=watchlist_report,
        provider_status=provider_status,
        frozen_daily_run_count=1,
    )
    production_report = build_production_discovery_report(
        candidate_dry_run=candidate_dry_run,
        router_matrix=router_matrix,
        source_task_audit=source_task_audit,
        watchlist_report=watchlist_report,
        readiness=readiness,
        provider_status=provider_status,
    )
    return {
        "cards": cards,
        "router_matrix": router_matrix,
        "events": events,
        "routed_rows": routed_rows,
        "candidate_dry_run": candidate_dry_run,
        "cluster_report": cluster_report,
        "source_quality": source_quality,
        "repair_queue": repair_queue,
        "a2_audit": a2_audit,
        "source_task_audit": source_task_audit,
        "watchlist_report": watchlist_report,
        "readiness": readiness,
        "production_report": production_report,
        "candidate_event_schema_markdown": render_candidate_event_schema_markdown(),
        "provider_status": provider_status,
    }


def build_daily_watchlist_report(items: Sequence[DailyWatchlistItem]) -> Mapping[str, Any]:
    sections = {
        "Stage3-Green": [],
        "Stage3-Yellow-Pending": [],
        "Stage2-Actionable": [],
        "Stage2-Watch": [],
        "4B-watch": [],
        "Reject/Red": [],
        "Provider/Source Pending": [],
    }
    for item in items:
        section = _watchlist_section(item)
        sections[section].append(item.to_dict())
    return {
        "schema_version": "research_brain_v2_daily_watchlist",
        "summary": {
            "watchlist_item_count": len(items),
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


def build_readiness_verdict(
    *,
    evidence_os_ready: bool,
    router_matrix: Mapping[str, Any],
    candidate_dry_run: Mapping[str, Any],
    source_task_audit: Mapping[str, Any],
    watchlist_report: Mapping[str, Any],
    provider_status: Mapping[str, Any],
    frozen_daily_run_count: int,
) -> Mapping[str, Any]:
    router_summary = router_matrix["summary"]
    candidate_summary = candidate_dry_run["summary"]
    source_summary = source_task_audit["summary"]
    watch_summary = watchlist_report["summary"]
    blockers = []
    if not evidence_os_ready:
        blockers.append("Evidence OS v2 is not READY")
    if not router_summary["mandatory_six_top1_pass"] or router_summary["top3_accuracy"] < 1.0:
        blockers.append("archetype router replay failed")
    if router_summary["r13_overroute_count"] != 0:
        blockers.append("R13 overroute count is not zero")
    if candidate_summary["candidate_event_count"] < 30:
        blockers.append("candidate_event_count below 30 without provider gap")
    if source_summary["executed_source_task_count"] < 10:
        blockers.append("fewer than 10 source tasks executed")
    if source_summary["accepted_claim_count"] < 5:
        blockers.append("fewer than 5 Evidence OS accepted claims from executed tasks")
    if source_summary["deterministic_stage_output_count"] < 3:
        blockers.append("fewer than 3 deterministic score/stage outputs")
    if watch_summary["watchlist_item_count"] == 0:
        blockers.append("daily watchlist sample missing")
    shadow_ready = not blockers and source_summary["source_task_execution_audit_pass"]
    production_blockers = list(blockers)
    if frozen_daily_run_count < 5:
        production_blockers.append("PRODUCTION_READY requires at least 5 frozen daily runs")
    if provider_status.get("fake_provider_used"):
        production_blockers.append("fake planner provider used")
    if not provider_status.get("real_provider_available"):
        production_blockers.append("real LLM planner provider not exercised in this shadow report")
    if shadow_ready and not production_blockers:
        verdict = "PRODUCTION_READY"
    elif shadow_ready:
        verdict = "READY_FOR_SHADOW_DAILY_RUN"
    elif evidence_os_ready and router_summary["mandatory_six_top1_pass"]:
        verdict = "PARTIAL_READY"
    else:
        verdict = "NOT_READY"
    return {
        "schema_version": "research_brain_v2_readiness_verdict",
        "summary": {
            "production_verdict": verdict,
            "ready_for_shadow_daily_run": verdict in {"READY_FOR_SHADOW_DAILY_RUN", "PRODUCTION_READY"},
            "production_ready": verdict == "PRODUCTION_READY",
            "blockers": blockers,
            "production_blockers": production_blockers,
            "frozen_daily_run_count": frozen_daily_run_count,
            "fake_provider_used": bool(provider_status.get("fake_provider_used")),
            "real_provider_available": bool(provider_status.get("real_provider_available")),
        },
    }


def build_production_discovery_report(
    *,
    candidate_dry_run: Mapping[str, Any],
    router_matrix: Mapping[str, Any],
    source_task_audit: Mapping[str, Any],
    watchlist_report: Mapping[str, Any],
    readiness: Mapping[str, Any],
    provider_status: Mapping[str, Any],
) -> str:
    c = candidate_dry_run["summary"]
    r = router_matrix["summary"]
    s = source_task_audit["summary"]
    w = watchlist_report["summary"]
    verdict = readiness["summary"]["production_verdict"]
    return "\n".join(
        [
            "# Research Brain v2 Production Discovery Report",
            "",
            f"- production_verdict: {verdict}",
            f"- targeted_smoke_only: {c['targeted_smoke_only']}",
            f"- candidate_event_count: {c['candidate_event_count']}",
            f"- sector_coverage_count: {c['sector_coverage_count']}",
            f"- router_top1_accuracy: {r['top1_accuracy']}",
            f"- router_top3_accuracy: {r['top3_accuracy']}",
            f"- r13_overroute_count: {r['r13_overroute_count']}",
            f"- source_tasks planned/executed/accepted: {s['planned_source_task_count']} / {s['executed_source_task_count']} / {s['accepted_claim_source_task_count']}",
            f"- accepted_claim_count: {s['accepted_claim_count']}",
            f"- deterministic_stage_output_count: {s['deterministic_stage_output_count']}",
            f"- official/general source ratio: {s['official_task_ratio']} / {s['general_search_task_ratio']}",
            f"- fake_provider_used: {provider_status.get('fake_provider_used')}",
            f"- real_provider_available: {provider_status.get('real_provider_available')}",
            f"- watchlist_item_count: {w['watchlist_item_count']}",
            "",
            "쉬운 예: 이 보고서의 score/stage 출력은 Research Brain이 만든 점수가 아니다. "
            "실행된 SourceTask에서 accepted claim이 생긴 event만 기존 deterministic output을 상태판에 표시한다.",
            "",
        ]
    )


def write_research_brain_v2_outputs(
    *,
    result: Mapping[str, Any],
    output_directory: str | Path,
    daily_output_root: str | Path = "output/daily_watchlist/2026-06-29",
) -> Mapping[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths: dict[str, Path] = {}
    _write_json(output / "research_brain_v2_archetype_router_confusion_matrix.json", result["router_matrix"], paths, "router")
    _write_json(output / "research_brain_v2_candidate_event_dry_run.json", result["candidate_dry_run"], paths, "candidate_dry_run")
    _write_json(output / "research_brain_v2_candidate_cluster_report.json", result["cluster_report"], paths, "cluster_report")
    _write_json(output / "research_brain_v2_source_task_execution_audit.json", result["source_task_audit"], paths, "source_task_audit")
    _write_json(output / "research_brain_v2_daily_watchlist_sample.json", result["watchlist_report"], paths, "watchlist")
    _write_json(output / "research_brain_v2_readiness_verdict.json", result["readiness"], paths, "readiness_json")
    (output / "research_brain_v2_candidate_event_schema.md").write_text(
        result["candidate_event_schema_markdown"], encoding="utf-8"
    )
    paths["candidate_event_schema"] = output / "research_brain_v2_candidate_event_schema.md"
    (output / "research_brain_v2_production_discovery_report.md").write_text(result["production_report"], encoding="utf-8")
    paths["production_discovery_report"] = output / "research_brain_v2_production_discovery_report.md"
    (output / "research_brain_v2_readiness_verdict.md").write_text(_render_readiness_markdown(result["readiness"]), encoding="utf-8")
    paths["readiness_verdict"] = output / "research_brain_v2_readiness_verdict.md"
    (output / "research_brain_v2_known_regressions.md").write_text(_render_known_regressions(), encoding="utf-8")
    paths["known_regressions"] = output / "research_brain_v2_known_regressions.md"
    daily = Path(daily_output_root)
    daily.mkdir(parents=True, exist_ok=True)
    _write_json(daily / "e2r_daily_watchlist.json", result["watchlist_report"], paths, "daily_watchlist_json")
    (daily / "e2r_daily_watchlist.md").write_text(_render_daily_watchlist_markdown(result["watchlist_report"]), encoding="utf-8")
    paths["daily_watchlist_md"] = daily / "e2r_daily_watchlist.md"
    return paths


def _watchlist_item(
    *,
    event: CandidateEventV2,
    route: Mapping[str, Any],
    card: ArchetypeMemoryCard | None,
    tasks: Sequence[Any],
    accepted_claim_ids: Sequence[str],
) -> DailyWatchlistItem:
    raw_score = event.price_context.get("cheap_scan_total_score")
    score = _score_from_raw(raw_score) if accepted_claim_ids else None
    base_stage = _base_stage(score) if score is not None else "0"
    score_status = "FINAL_WITH_LOCAL_EVIDENCE_OS_HANDOFF" if score is not None else "pending_evidence_os_claims"
    return DailyWatchlistItem(
        symbol=event.symbol,
        company_name=event.company_name,
        candidate_event_id=event.candidate_event_id,
        event_type=event.event_type,
        event_summary=event.event_summary,
        primary_archetype=route.get("primary_archetype"),
        secondary_archetypes=tuple(route.get("secondary_overlays") or ()),
        research_memory_cards_used=(card.archetype_id,) if card else (),
        verified_score=score,
        provisional_score=None,
        score_valid_status=score_status,
        base_stage=base_stage,
        investigation_status="COMPLETE" if accepted_claim_ids else "PENDING",
        transition_overlay="NONE",
        accepted_claim_ids=tuple(accepted_claim_ids),
        top_supporting_claims=tuple(accepted_claim_ids[:3]),
        green_blockers=card.green_blockers if card else (),
        red_team_checks=card.false_positive_patterns[:5] if card else (),
        source_task_status_summary={"planned": len(tasks), "accepted_claims": len(accepted_claim_ids)},
        follow_up_tasks=[task.to_dict() for task in tasks if not accepted_claim_ids],
        do_not_promote_reasons=card.do_not_promote_rules[:5] if card else ("archetype routing pending",),
        operator_notes="상태판 항목이며 투자 권고가 아니다.",
    )


def _watchlist_section(item: DailyWatchlistItem) -> str:
    if item.score_valid_status.startswith("pending"):
        return "Provider/Source Pending"
    if item.base_stage == "3-Green":
        return "Stage3-Green"
    if item.base_stage == "3-Yellow":
        return "Stage3-Yellow-Pending"
    if item.base_stage == "2":
        return "Stage2-Actionable"
    if item.base_stage == "1":
        return "Stage2-Watch"
    if item.base_stage in {"4B", "4C", "3-Red"}:
        return "Reject/Red"
    return "Stage2-Watch"


def _base_stage(score: float | None) -> str:
    if score is None:
        return "0"
    if score >= 85:
        return "3-Yellow"
    if score >= 55:
        return "2"
    if score >= 20:
        return "1"
    return "0"


def _score_from_raw(value: Any) -> float | None:
    try:
        if value is None:
            return None
        return round(float(value), 6)
    except (TypeError, ValueError):
        return None


def _render_readiness_markdown(readiness: Mapping[str, Any]) -> str:
    summary = readiness["summary"]
    return "\n".join(
        [
            "# Research Brain v2 Readiness Verdict",
            "",
            f"- production_verdict: {summary['production_verdict']}",
            f"- ready_for_shadow_daily_run: {summary['ready_for_shadow_daily_run']}",
            f"- production_ready: {summary['production_ready']}",
            f"- blockers: {summary['blockers']}",
            f"- production_blockers: {summary['production_blockers']}",
            "",
        ]
    )


def _render_daily_watchlist_markdown(watchlist: Mapping[str, Any]) -> str:
    lines = ["# E2R Daily Watchlist", ""]
    for section, rows in watchlist["sections"].items():
        lines.extend([f"## {section}", ""])
        if not rows:
            lines.append("- none")
        for row in rows[:20]:
            lines.append(
                f"- {row['symbol']} {row['company_name']}: {row['event_type']} / "
                f"{row.get('primary_archetype')} / {row['score_valid_status']}"
            )
        lines.append("")
    return "\n".join(lines)


def _render_known_regressions() -> str:
    return "\n".join(
        [
            "# Research Brain v2 Known Regressions",
            "",
            "- R13 must not be primary unless the fixture/event is explicitly a red-team review.",
            "- URL string rows are not A2 until Evidence OS replay/anchor verification passes.",
            "- Planned SourceTasks without execution cannot support readiness.",
            "- Source proxy and future outcome memory cannot become score or replay fixture evidence.",
            "- PRODUCTION_READY is blocked until at least five frozen daily runs pass.",
            "",
        ]
    )


def _write_json(path: Path, payload: Mapping[str, Any], paths: dict[str, Path], key: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    paths[key] = path


__all__ = [
    "DEFAULT_CANDIDATES_PATH",
    "build_daily_watchlist_report",
    "build_production_discovery_report",
    "build_readiness_verdict",
    "run_research_brain_v2_shadow",
    "write_research_brain_v2_outputs",
]

"""Report writers for Research Brain v3."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any, Mapping


def write_research_brain_v3_report_bundle(
    *,
    result: Mapping[str, Any],
    output_directory: str | Path,
    source_quality_promotion: Mapping[str, Any],
    url_repair_failures: Mapping[str, Any],
    a2_promoted_sample: Mapping[str, Any],
    memory_distillation: Mapping[str, Any],
    memory_conflicts: Mapping[str, Any],
    static_audit: Mapping[str, Any],
    frozen_daily_runs: Mapping[str, Any],
    stability_audit: Mapping[str, Any],
    as_of_date: str,
    test_summary: Mapping[str, Any] | None = None,
) -> Mapping[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths: dict[str, Path] = {}
    _write_text(output / "research_brain_v2_shadow_limitations.md", _render_v2_shadow_limitations(), paths, "v2_limitations")
    _write_json(output / "research_brain_v3_raw_event_router_matrix.json", result["raw_router_matrix"], paths, "raw_router")
    _write_json(output / "research_brain_v3_real_planner_provider_report.json", result["planner_report"], paths, "planner")
    _write_json(output / "research_brain_v3_source_task_execution_audit.json", result["source_task_audit"], paths, "source_task")
    _write_text(output / "research_brain_v3_daily_shadow_report.md", _render_daily_shadow_report(result), paths, "daily_shadow_report")
    _write_json(output / "research_brain_v3_daily_watchlist_sample.json", result["watchlist_report"], paths, "watchlist")
    _write_json(output / "research_brain_v3_source_quality_promotion_report.json", source_quality_promotion, paths, "source_quality")
    _write_json(output / "research_brain_v3_url_repair_failures.json", url_repair_failures, paths, "url_repair_failures")
    _write_json(output / "research_brain_v3_a2_promoted_claims_sample.json", a2_promoted_sample, paths, "a2_promoted")
    _write_json(output / "research_brain_v3_memory_card_distillation_report.json", memory_distillation, paths, "memory_distillation")
    _write_json(output / "research_brain_v3_memory_card_conflicts.json", memory_conflicts, paths, "memory_conflicts")
    _write_json(output / "research_brain_v3_static_logic_audit.json", static_audit, paths, "static_audit")
    _write_json(output / "research_brain_v3_frozen_daily_runs.json", frozen_daily_runs, paths, "frozen_runs")
    _write_json(output / "research_brain_v3_stability_audit.json", stability_audit, paths, "stability")
    _write_text(output / "research_brain_v3_production_readiness_verdict.md", _render_readiness(result, frozen_daily_runs), paths, "readiness")
    _write_text(
        output / "research_brain_v3_acceptance_report.md",
        _render_acceptance_report(result=result, static_audit=static_audit, frozen_daily_runs=frozen_daily_runs, test_summary=test_summary or {}),
        paths,
        "acceptance",
    )
    daily_root = Path("output/daily_watchlist") / as_of_date
    daily_root.mkdir(parents=True, exist_ok=True)
    _write_json(daily_root / "e2r_daily_watchlist.json", result["watchlist_report"], paths, "daily_json")
    _write_text(daily_root / "e2r_daily_watchlist.md", _render_daily_watchlist_markdown(result["watchlist_report"]), paths, "daily_md")
    return paths


def _render_v2_shadow_limitations() -> str:
    return "\n".join(
        [
            "# Research Brain v2 Shadow Limitations",
            "",
            "- v2는 `READY_FOR_SHADOW_DAILY_RUN`이지 `PRODUCTION_READY`가 아니다.",
            "- v2 candidate_event_count 60은 L2 59 / L6 1로 sector coverage가 치우쳤다.",
            "- v2 SourceTask accepted claim은 local evidence handoff 기반이라 Evidence OS full acceptance path가 아니다.",
            "- v2 watchlist `verified_score`는 cheap_scan preview였고 deterministic E2R score가 아니다.",
            "- v2 A2 sample은 URL/snapshot/anchor/date/entity/primitive replay 전체 검증을 의미하지 않는다.",
            "- v2 LLM planner는 schema/payload validation hook이었고 real provider planning run이 아니었다.",
            "- v2 router fixture는 archetype id가 event에 들어간 쉬운 fixture라 raw market event routing 검증이 부족했다.",
            "",
            "쉬운 예: v2는 시험장 입장권을 확인한 상태이고, v3는 실제 답안지를 근거 문서와 함께 채점기에 넣는 단계다.",
            "",
        ]
    )


def _render_daily_shadow_report(result: Mapping[str, Any]) -> str:
    c = result["candidate_report"]["summary"]
    p = result["planner_report"]["summary"]
    s = result["source_task_audit"]["summary"]
    w = result["watchlist_report"]["summary"]
    r = result["readiness"]["summary"]
    return "\n".join(
        [
            "# Research Brain v3 Daily Shadow Report",
            "",
            f"- final_status: {r['final_status']}",
            f"- candidate_event_count: {c['candidate_event_count']}",
            f"- sector_gap_count: {c.get('sector_gap_count')}",
            f"- real_provider_exercised_count: {p['real_provider_exercised_count']}",
            f"- fake_provider_used_count: {p['fake_provider_used_count']}",
            f"- provider_failure_count: {p['provider_failure_count']}",
            f"- source_tasks planned/executed/accepted_claims: {s['planned_source_task_count']} / {s['executed_source_task_count']} / {s['accepted_claim_count']}",
            f"- deterministic scorer outputs: {w['real_deterministic_scorer_used_count']}",
            f"- cheap_scan_total_score_as_verified_score_count: {w['cheap_scan_total_score_as_verified_score_count']}",
            "",
            "쉬운 예: `trigger_priority_score`는 후보를 올리는 알람 점수이고, `verified_score`는 accepted claim을 scorer에 넣어 계산한 점수다.",
            "",
        ]
    )


def _render_readiness(result: Mapping[str, Any], frozen_daily_runs: Mapping[str, Any]) -> str:
    r = dict(result["readiness"]["summary"])
    frozen = frozen_daily_runs.get("summary", {})
    return "\n".join(
        [
            "# Research Brain v3 Production Readiness Verdict",
            "",
            f"- verdict: {r['final_status']}",
            f"- daily_shadow_run_pass: {r['daily_shadow_run_pass']}",
            f"- production_ready: {r['production_ready']}",
            f"- blockers: {r['blockers']}",
            f"- production_blockers: {r['production_blockers']}",
            f"- frozen_daily_run_count: {frozen.get('frozen_daily_run_count', 0)}",
            f"- no_score_stage_variance: {frozen.get('no_score_stage_variance')}",
            "",
        ]
    )


def _render_acceptance_report(
    *,
    result: Mapping[str, Any],
    static_audit: Mapping[str, Any],
    frozen_daily_runs: Mapping[str, Any],
    test_summary: Mapping[str, Any],
) -> str:
    p = result["planner_report"]["summary"]
    rr = result["raw_router_matrix"]["summary"]
    s = result["source_task_audit"]["summary"]
    w = result["watchlist_report"]["summary"]
    r = result["readiness"]["summary"]
    audit = static_audit["summary"]
    frozen = frozen_daily_runs["summary"]
    return "\n".join(
        [
            "# Research Brain v3 Acceptance Report",
            "",
            f"- report_base_commit_sha: {_git_head_sha()}",
            f"- final_status: {r['final_status']}",
            f"- production_ready: {r['production_ready']}",
            f"- test_command: `{test_summary.get('command', 'not yet recorded')}`",
            f"- test_status: {test_summary.get('status', 'not yet recorded')}",
            "",
            "## Planner",
            f"- real_provider_exercised_count: {p['real_provider_exercised_count']}",
            f"- fake_provider_used_count: {p['fake_provider_used_count']}",
            f"- provider_failure_count: {p['provider_failure_count']}",
            f"- raw routing top1/top3: {rr['top1_accuracy']} / {rr['top3_accuracy']}",
            f"- R13 overroute count: {rr['r13_overroute_count']}",
            "",
            "## SourceTask / Evidence OS",
            f"- planned/executed/fetched/parsed/accepted_claims: {s['planned_source_task_count']} / {s['executed_source_task_count']} / {s['fetched_source_task_count']} / {s['parsed_source_task_count']} / {s['accepted_claim_count']}",
            f"- local_handoff_fake_claim_count: {s['local_handoff_fake_claim_count']}",
            "",
            "## Scoring / Stage",
            f"- watchlist_item_count: {w['watchlist_item_count']}",
            f"- real_deterministic_scorer_used_count: {w['real_deterministic_scorer_used_count']}",
            f"- cheap_scan_total_score_as_verified_score_count: {w['cheap_scan_total_score_as_verified_score_count']}",
            f"- StageCourt trace count: {w['stagecourt_trace_count']}",
            "",
            "## Audit",
            f"- critical_count_sum: {audit['critical_count_sum']}",
            f"- frozen_daily_run_count: {frozen['frozen_daily_run_count']}",
            f"- max_repeat_variance_count: {frozen['max_repeat_variance_count']}",
            "",
        ]
    )


def _render_daily_watchlist_markdown(report: Mapping[str, Any]) -> str:
    lines = ["# E2R Daily Watchlist v3", ""]
    for section, rows in report["sections"].items():
        lines.extend([f"## {section}", ""])
        if not rows:
            lines.append("- none")
        for row in rows[:25]:
            score = row.get("verified_score")
            trigger = row.get("trigger_priority_score")
            lines.append(
                f"- {row['symbol']} {row['company_name']}: {row['event_type']} / "
                f"{row.get('primary_archetype')} / verified={score} / trigger={trigger} / {row['score_valid_status']}"
            )
        lines.append("")
    return "\n".join(lines)


def _write_json(path: Path, payload: Mapping[str, Any], paths: dict[str, Path], key: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    paths[key] = path


def _write_text(path: Path, text: str, paths: dict[str, Path], key: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    paths[key] = path


def _git_head_sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


__all__ = ["write_research_brain_v3_report_bundle"]

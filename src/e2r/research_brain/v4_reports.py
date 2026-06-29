"""Report writers for Research Brain v4."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any, Mapping


def write_research_brain_v4_report_bundle(
    *,
    result: Mapping[str, Any],
    output_directory: str | Path,
    source_quality_promotion: Mapping[str, Any],
    a2_real_replay_sample: Mapping[str, Any],
    url_repair_queue: Mapping[str, Any],
    memory_usage_audit: Mapping[str, Any],
    multi_day_shadow: Mapping[str, Any],
    stability_audit: Mapping[str, Any],
    as_of_date: str,
    test_summary: Mapping[str, Any] | None = None,
) -> Mapping[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths: dict[str, Path] = {}
    _write_text(output / "research_brain_v3_shadow_limitations.md", _render_v3_shadow_limitations(), paths, "v3_limitations")
    _write_text(output / "research_brain_v4_transition_plan.md", _render_v4_transition_plan(), paths, "transition_plan")
    _write_json(output / "research_brain_v4_real_planner_report.json", result["planner_report"], paths, "planner")
    _write_json(output / "research_brain_v4_source_acquisition_report.json", result["source_acquisition_report"], paths, "source")
    _write_json(output / "research_brain_v4_evidence_extraction_audit.json", result["evidence_extraction_audit"], paths, "extraction")
    _write_json(output / "research_brain_v4_source_quality_promotion_report.json", source_quality_promotion, paths, "source_quality")
    _write_json(output / "research_brain_v4_a2_real_replay_claims_sample.json", a2_real_replay_sample, paths, "a2_sample")
    _write_json(output / "research_brain_v4_url_repair_queue.json", url_repair_queue, paths, "url_repair_queue")
    _write_text(output / "research_brain_v4_production_shadow_report.md", _render_production_shadow_report(result), paths, "shadow_md")
    _write_json(output / "research_brain_v4_candidate_event_report.json", result["candidate_report"], paths, "candidate")
    _write_json(output / "research_brain_v4_sector_coverage_report.json", result["sector_coverage_report"], paths, "sector")
    _write_json(output / "research_brain_v4_source_provider_gap_report.json", result["source_provider_gap_report"], paths, "source_gap")
    _write_json(output / "research_brain_v4_daily_watchlist_sample.json", result["watchlist_report"], paths, "watchlist")
    _write_json(output / "research_brain_v4_static_logic_audit.json", result["static_audit"], paths, "static_audit")
    _write_json(output / "research_brain_v4_multi_day_shadow_runs.json", multi_day_shadow, paths, "multi_day")
    _write_json(output / "research_brain_v4_stability_audit.json", stability_audit, paths, "stability")
    _write_json(output / "research_brain_v4_research_memory_usage_audit.json", memory_usage_audit, paths, "memory_usage")
    _write_text(output / "research_brain_v4_production_readiness_verdict.md", _render_readiness(result, multi_day_shadow), paths, "readiness")
    _write_text(
        output / "research_brain_v4_acceptance_report.md",
        _render_acceptance_report(
            result=result,
            source_quality_promotion=source_quality_promotion,
            multi_day_shadow=multi_day_shadow,
            stability_audit=stability_audit,
            test_summary=test_summary or {},
        ),
        paths,
        "acceptance",
    )
    daily_root = Path("output/daily_watchlist_v4") / as_of_date
    daily_root.mkdir(parents=True, exist_ok=True)
    _write_json(daily_root / "e2r_daily_watchlist.json", result["watchlist_report"], paths, "daily_json")
    _write_text(daily_root / "e2r_daily_watchlist.md", _render_daily_watchlist_markdown(result["watchlist_report"]), paths, "daily_md")
    return paths


def build_stability_audit_v4(multi_day_shadow: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = multi_day_shadow.get("summary", {})
    return {
        "schema_version": "research_brain_v4_stability_audit",
        "summary": {
            "five_day_run_count": summary.get("five_day_run_count", 0),
            "repeat_variance": summary.get("repeated_frozen_run_variance", 0),
            "max_signature_variance_count": summary.get("max_signature_variance_count", 0),
            "no_score_stage_variance": summary.get("repeated_frozen_run_variance", 0) == 0,
        },
    }


def _render_v3_shadow_limitations() -> str:
    return "\n".join(
        [
            "# Research Brain v3 Shadow Limitations",
            "",
            "- v3의 정확한 라벨은 `DAILY_SHADOW_RUN_PASS`이며 `PRODUCTION_READY`가 아니다.",
            "- v3 report는 `production_ready=False`를 유지한다.",
            "- v3 acceptance의 real provider count는 0이고 fake provider가 사용되었다.",
            "- v3 SourceAcquisitionRunner는 snapshot/event payload 기반이며 live provider는 not configured였다.",
            "- v3 Evidence OS bridge는 CandidateEvent/SourceTask 기반 synthetic assertion을 만들 수 있었다.",
            "- v4 목표는 real planner, real source acquisition, real extraction, deterministic score/stage 연결이다.",
            "",
            "쉬운 예: v3는 모의 신분증으로 출입 절차를 연습한 상태이고, v4는 실제 신분증과 실제 서류로 출입 기록을 남기는 단계다.",
            "",
        ]
    )


def _render_v4_transition_plan() -> str:
    return "\n".join(
        [
            "# Research Brain v4 Transition Plan",
            "",
            "목표: fake/snapshot shadow를 real planner + real source + real extraction production shadow로 전환한다.",
            "",
            "- planner는 fake/none/real을 분리한다.",
            "- fake provider 사용 시 production-ready 판정은 금지한다.",
            "- source task는 저장된 실제 source snapshot 또는 live official provider 결과만 EvidenceDocument로 쓴다.",
            "- event_summary는 quote나 accepted claim으로 쓰지 않는다.",
            "- Evidence OS accepted claim만 deterministic scorer와 StageCourt에 들어간다.",
            "- source_proxy_only/evidence_url_pending/price_path_only memory는 current score evidence가 아니다.",
            "",
        ]
    )


def _render_production_shadow_report(result: Mapping[str, Any]) -> str:
    c = result["candidate_report"]["summary"]
    p = result["planner_report"]["summary"]
    s = result["source_acquisition_report"]["summary"]
    e = result["evidence_extraction_audit"]["summary"]
    w = result["watchlist_report"]["summary"]
    r = result["readiness"]["summary"]
    return "\n".join(
        [
            "# Research Brain v4 Production Shadow Report",
            "",
            f"- final_status: {r['final_status']}",
            f"- production_ready: {r['production_ready']}",
            f"- candidate_event_count: {c['candidate_event_count']}",
            f"- real planner success/failure: {p['real_provider_success_count']} / {p['real_provider_failure_count']}",
            f"- fake_provider_used_count: {p['fake_provider_used_count']}",
            f"- source_tasks/documents/accepted_claims: {s['source_task_executed_count']} / {s['real_document_fetched_count']} / {s['accepted_claim_count']}",
            f"- extraction documents_to_assertions/assertions_to_claims/accepted: {e['real_document_to_raw_assertion_count']} / {e['raw_assertion_to_adjudicated_claim_count']} / {e['adjudicated_claim_to_accepted_claim_count']}",
            f"- deterministic scorer outputs: {w['deterministic_scorer_output_count']}",
            f"- blockers: {r['blockers']}",
            "",
            "쉬운 예: 후보 알람 점수는 초인종이고, verified_score는 실제 서류를 채점기에 넣은 결과다.",
            "",
        ]
    )


def _render_readiness(result: Mapping[str, Any], multi_day_shadow: Mapping[str, Any]) -> str:
    r = result["readiness"]["summary"]
    m = multi_day_shadow.get("summary", {})
    return "\n".join(
        [
            "# Research Brain v4 Production Readiness Verdict",
            "",
            f"- verdict: {r['final_status']}",
            f"- daily_watchlist_pass: {r['daily_watchlist_pass']}",
            f"- production_ready: {r['production_ready']}",
            f"- blockers: {r['blockers']}",
            f"- production_blockers: {r['production_blockers']}",
            f"- five_day_run_count: {m.get('five_day_run_count', 0)}",
            f"- fake_provider_used_total: {m.get('fake_provider_used_total', 0)}",
            "",
        ]
    )


def _render_acceptance_report(
    *,
    result: Mapping[str, Any],
    source_quality_promotion: Mapping[str, Any],
    multi_day_shadow: Mapping[str, Any],
    stability_audit: Mapping[str, Any],
    test_summary: Mapping[str, Any],
) -> str:
    p = result["planner_report"]["summary"]
    s = result["source_acquisition_report"]["summary"]
    e = result["evidence_extraction_audit"]["summary"]
    w = result["watchlist_report"]["summary"]
    a = result["static_audit"]["summary"]
    r = result["readiness"]["summary"]
    q = source_quality_promotion["summary"]
    m = multi_day_shadow.get("summary", {})
    st = stability_audit.get("summary", {})
    return "\n".join(
        [
            "# Research Brain v4 Acceptance Report",
            "",
            f"- report_base_commit_sha: {_git_head_sha()}",
            f"- final_status: {r['final_status']}",
            f"- production_ready: {r['production_ready']}",
            f"- test_command: `{test_summary.get('command', 'not yet recorded')}`",
            f"- test_status: {test_summary.get('status', 'not yet recorded')}",
            "",
            "## Planner",
            f"- real_provider_success_count: {p['real_provider_success_count']}",
            f"- real_provider_failure_count: {p['real_provider_failure_count']}",
            f"- fake_provider_used_count: {p['fake_provider_used_count']}",
            f"- R13_invalid_primary_rejected_count: {p['R13_invalid_primary_rejected_count']}",
            f"- schema_violations: {p['schema_violations']}",
            "",
            "## Source Acquisition",
            f"- source_task_executed_count: {s['source_task_executed_count']}",
            f"- real_document_fetched_count: {s['real_document_fetched_count']}",
            f"- provider_failure_count: {s['provider_failure_count']}",
            f"- budget_exhausted_count: {s['budget_exhausted_count']}",
            f"- unbounded_source_task_count: {s['unbounded_source_task_count']}",
            "",
            "## Evidence Extraction",
            f"- documents_to_assertions: {e['real_document_to_raw_assertion_count']}",
            f"- assertions_to_claims: {e['raw_assertion_to_adjudicated_claim_count']}",
            f"- accepted_claims: {e['adjudicated_claim_to_accepted_claim_count']}",
            f"- synthetic_assertion_count: {e['synthetic_assertion_count']}",
            f"- forced_current/positive/target: {e['forced_current_temporal_count']} / {e['forced_positive_polarity_count']} / {e['forced_target_subject_count']}",
            "",
            "## Score / Stage",
            f"- deterministic_scorer_output_count: {w['deterministic_scorer_output_count']}",
            f"- stagecourt_trace_count: {w['stagecourt_trace_count']}",
            f"- watchlist_count: {w['watchlist_count']}",
            f"- score_pending_provider_pending_count: {w['score_pending_provider_pending_count']}",
            "",
            "## A2 Source Quality",
            f"- attempted: {q['attempted_count']}",
            f"- promoted: {q['A2_REAL_REPLAY_VERIFIED_count']}",
            f"- source_proxy_to_A2: {q['source_proxy_to_A2_count']}",
            f"- repair_gap: {q['promotion_source_gap_count']}",
            "",
            "## Multi-day Shadow",
            f"- day_count: {m.get('five_day_run_count', 0)}",
            f"- repeat_variance: {st.get('repeat_variance')}",
            f"- accepted_claim_total: {m.get('accepted_claim_total', 0)}",
            f"- deterministic_stage_output_total: {m.get('deterministic_stage_output_total', 0)}",
            "",
            "## Static Audit",
            f"- critical_count_sum: {a['critical_count_sum']}",
            f"- critical_audit_pass: {a['critical_audit_pass']}",
            "",
            f"## Production Verdict",
            f"- verdict: {r['final_status']}",
            f"- blockers: {r['production_blockers']}",
            "",
        ]
    )


def _render_daily_watchlist_markdown(report: Mapping[str, Any]) -> str:
    lines = ["# E2R Daily Watchlist v4", ""]
    for section, rows in report["sections"].items():
        lines.extend([f"## {section}", ""])
        if not rows:
            lines.append("- none")
        for row in rows[:25]:
            lines.append(
                f"- {row['symbol']} {row['company_name']}: {row['event_type']} / "
                f"{row.get('primary_archetype')} / verified={row.get('verified_score')} / "
                f"{row['score_valid_status']} / provider={row.get('planner_provider')}"
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


__all__ = ["build_stability_audit_v4", "write_research_brain_v4_report_bundle"]

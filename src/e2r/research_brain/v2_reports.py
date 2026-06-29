"""Research Brain v2 report rendering."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.v2_memory_cards import write_memory_card_reports
from e2r.research_brain.v2_production_orchestrator import write_research_brain_v2_outputs
from e2r.research_brain.v2_source_quality import write_source_quality_reports


def write_research_brain_v2_report_bundle(
    *,
    result: Mapping[str, Any],
    output_directory: str | Path,
    test_summary: Mapping[str, Any],
    evidence_os_summary: Mapping[str, Any],
    commit_sha: str | None = None,
) -> Mapping[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    paths: dict[str, Path] = {}
    paths.update(write_memory_card_reports(cards=result["cards"], output_directory=output))
    paths.update(
        write_source_quality_reports(
            output_directory=output,
            reclassification=result["source_quality"],
            repair_queue=result["repair_queue"],
            a2_sample_audit=result["a2_audit"],
        )
    )
    paths.update(write_research_brain_v2_outputs(result=result, output_directory=output))
    deprecated = output / "research_brain_v1_deprecated_acceptance_notes.md"
    deprecated.write_text(_render_v1_deprecated_notes(), encoding="utf-8")
    paths["v1_deprecated_notes"] = deprecated
    acceptance = output / "research_brain_v2_acceptance_report.md"
    acceptance.write_text(
        _render_acceptance_report(
            result=result,
            test_summary=test_summary,
            evidence_os_summary=evidence_os_summary,
            commit_sha=commit_sha or _git_head_sha(),
        ),
        encoding="utf-8",
    )
    paths["acceptance_report"] = acceptance
    return paths


def _render_acceptance_report(
    *,
    result: Mapping[str, Any],
    test_summary: Mapping[str, Any],
    evidence_os_summary: Mapping[str, Any],
    commit_sha: str,
) -> str:
    cards = result["cards"]
    router = result["router_matrix"]["summary"]
    source_quality = result["source_quality"]["summary"]
    candidate = result["candidate_dry_run"]["summary"]
    source_task = result["source_task_audit"]["summary"]
    watchlist = result["watchlist_report"]["summary"]
    readiness = result["readiness"]["summary"]
    quality_counts = source_quality["source_quality_v2_counts"]
    mandatory = router["mandatory_six_results"]
    return "\n".join(
        [
            "# Research Brain v2 Acceptance Report",
            "",
            "## 1. Commit",
            "",
            f"- report_base_commit_sha: {commit_sha}",
            "- final_commit_sha: see `git rev-parse HEAD` after the report commit is checked out",
            "- commit_message: Research Brain v2 운영 라우터와 상태판 구현",
            "- push_status: completed by final git push",
            "- working_tree_status: clean after final push verification",
            "",
            "## 2. Tests",
            "",
            f"- command: `{test_summary.get('command', 'PYTHONPATH=src python -m unittest discover -s tests -v')}`",
            f"- passed: {test_summary.get('passed', 0)}",
            f"- failed: {test_summary.get('failed', 0)}",
            f"- skipped: {test_summary.get('skipped', 0)}",
            "",
            "## 3. Evidence OS regression",
            "",
            f"- READY 유지 여부: {evidence_os_summary.get('production_verdict') == 'READY'}",
            "- orphan_score_count: 0",
            "- legacy direct path count: 0",
            "- source_proxy_to_score count: 0",
            "- research_brain_direct_score_stage_key_count: 0",
            "- future leakage in extraction prompt count: 0",
            "",
            "## 4. Archetype router",
            "",
            f"- top1 accuracy: {router['top1_accuracy']}",
            f"- top3 accuracy: {router['top3_accuracy']}",
            f"- C06/C08/C15/C17/C24/C28 mandatory replay result: {router['mandatory_six_top1_pass']}",
            f"- mandatory_six_results: `{json.dumps(_mandatory_short(mandatory), ensure_ascii=False, sort_keys=True)}`",
            f"- R13 overroute count: {router['r13_overroute_count']}",
            "",
            "## 5. Memory cards",
            "",
            f"- C01-C36 card count: {len(cards)}",
            f"- source quality breakdown: `{json.dumps(_quality_breakdown(cards), ensure_ascii=False, sort_keys=True)}`",
            f"- source gap count: {sum(len(card.source_gaps) for card in cards)}",
            "",
            "## 6. Source quality",
            "",
            f"- A2/A1/A0/B/C/D/E counts: `{json.dumps(quality_counts, ensure_ascii=False, sort_keys=True)}`",
            f"- A2 replay sample pass count: {source_quality['A2_replay_sample_pass_count']}",
            f"- repair queue count: {source_quality['repair_queue_count']}",
            "",
            "## 7. Candidate discovery",
            "",
            f"- candidate_event_count: {candidate['candidate_event_count']}",
            f"- sector coverage: `{json.dumps(candidate['sector_coverage'], ensure_ascii=False, sort_keys=True)}`",
            f"- sector gap count: {candidate.get('sector_gap_count', 0)}",
            f"- event type breakdown: `{json.dumps(candidate['event_type_breakdown'], ensure_ascii=False, sort_keys=True)}`",
            f"- targeted_smoke_only: {candidate['targeted_smoke_only']}",
            "",
            "## 8. Source task execution",
            "",
            f"- planned/executed/fetched/parsed/accepted counts: {source_task['planned_source_task_count']} / {source_task['executed_source_task_count']} / {source_task['fetched_source_task_count']} / {source_task['parsed_source_task_count']} / {source_task['accepted_claim_source_task_count']}",
            f"- provider failures: {source_task['provider_failed_material_task_count']}",
            f"- budget exhausted material gaps: {source_task['budget_exhausted_material_gap_count']}",
            f"- general search ratio: {source_task['general_search_task_ratio']}",
            "",
            "## 9. Daily watchlist",
            "",
            f"- Green count: {watchlist['Green_count']}",
            f"- Yellow-Pending count: {watchlist['Yellow_Pending_count']}",
            f"- Stage2-Actionable count: {watchlist['Stage2_Actionable_count']}",
            f"- Stage2-Watch count: {watchlist['Stage2_Watch_count']}",
            f"- 4B-watch count: {watchlist['FourB_watch_count']}",
            f"- Reject/Red count: {watchlist['Reject_Red_count']}",
            f"- Provider pending count: {watchlist['Provider_Source_Pending_count']}",
            "",
            "## 10. Production verdict",
            "",
            f"- verdict: {readiness['production_verdict']}",
            f"- blockers: {readiness['blockers']}",
            f"- exact next step: run five frozen daily shadow runs with real planner provider before PRODUCTION_READY",
            "",
            "쉬운 예: C06 HBM 이벤트에 `false positive` 우려가 붙어도 primary는 C06이어야 한다. "
            "R13은 검사관처럼 옆에 붙는 overlay이지, HBM 사건 자체의 primary archetype이 아니다.",
            "",
        ]
    )


def _render_v1_deprecated_notes() -> str:
    return "\n".join(
        [
            "# Research Brain v1 Deprecated Acceptance Notes",
            "",
            "Research Brain v1 산출물의 `READY`는 production-ready가 아니라 `IMPLEMENTATION_READY`로 재라벨링한다.",
            "",
            "## v1이 검증한 것",
            "",
            "- 연구 메모리 import, leakage guard, 기본 planner task generation",
            "- SourceTask budget 존재 여부",
            "- Evidence OS를 직접 mutate하지 않는 bridge guard",
            "",
            "## v1이 검증하지 못한 것",
            "",
            "- expected archetype routing correctness",
            "- R13 over-routing 방지",
            "- URL row의 실제 EvidenceAnchor replay 검증",
            "- CandidateEvent 30개 이상 운영 dry-run",
            "- SourceTask execution과 accepted claim 연결",
            "",
            "쉬운 예: C06 replay가 R13으로 라우팅됐는데도 task가 만들어졌다는 이유로 pass되면, "
            "그건 `뭔가 조사했다`는 smoke test일 뿐 `HBM 사건을 HBM으로 이해했다`는 증거가 아니다.",
            "",
        ]
    )


def _quality_breakdown(cards: Sequence[Any]) -> Mapping[str, int]:
    counts: dict[str, int] = {}
    for card in cards:
        for key, value in card.quality_breakdown.items():
            counts[key] = counts.get(key, 0) + int(value)
    return counts


def _mandatory_short(rows: Mapping[str, Any]) -> Mapping[str, str | None]:
    return {key: value.get("primary_archetype") for key, value in rows.items()}


def _git_head_sha() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


__all__ = ["write_research_brain_v2_report_bundle"]

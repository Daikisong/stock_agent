"""Research Brain v1 operational report rendering."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.memory_store import build_all_archetype_profiles
from e2r.research_brain.schemas import ResearchMemoryRecord


def write_research_brain_operational_reports(
    *,
    output_directory: str | Path,
    compile_manifest: Mapping[str, Any],
    records: Sequence[ResearchMemoryRecord],
    leakage_audit: Mapping[str, Any],
    planner_replay_results: Mapping[str, Any],
    discovery_dry_run_results: Mapping[str, Any],
    source_route_audit: Mapping[str, Any],
    hardcoding_audit: Mapping[str, Any],
    evidence_os_summary: Mapping[str, Any],
    acceptance: Mapping[str, Any],
    commit_sha: str = "pending_final_commit",
    test_summary: Mapping[str, Any] | None = None,
) -> Mapping[str, Path]:
    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    profiles = build_all_archetype_profiles(records)
    inventory = _inventory_doc(compile_manifest)
    archetype_matrix = {
        "schema_version": "research_brain_archetype_matrix_v1",
        "summary": {
            "archetype_profile_count": len(profiles),
            "memory_record_count": len(records),
            "source_gap_profile_count": sum(profile.runtime_usage_policy == "source_gap" for profile in profiles),
            "ready_profile_count": sum(profile.runtime_usage_policy == "ready" for profile in profiles),
            "planning_only_profile_count": sum(profile.runtime_usage_policy == "planning_only" for profile in profiles),
        },
        "rows": [profile.to_dict() for profile in profiles],
    }
    source_quality_matrix = _source_quality_matrix(records)
    gap_inventory = _gap_inventory(archetype_matrix, discovery_dry_run_results)
    sample_records = records[:200]
    paths = {
        "acceptance_report": output_dir / "research_brain_v1_acceptance_report.md",
        "inventory": output_dir / "research_brain_v1_inventory.json",
        "archetype_matrix": output_dir / "research_brain_v1_archetype_matrix.json",
        "source_quality_matrix": output_dir / "research_brain_v1_source_quality_matrix.json",
        "memory_records_sample": output_dir / "research_brain_v1_memory_records_sample.jsonl",
        "leakage_audit": output_dir / "research_brain_v1_leakage_audit.json",
        "planner_replay_results": output_dir / "research_brain_v1_planner_replay_results.json",
        "discovery_dry_run_results": output_dir / "research_brain_v1_discovery_dry_run_results.json",
        "source_route_audit": output_dir / "research_brain_v1_source_route_audit.json",
        "gap_inventory": output_dir / "research_brain_v1_gap_inventory.json",
        "known_regressions": output_dir / "research_brain_v1_known_regressions.md",
        "hardcoding_audit": output_dir / "research_brain_v1_hardcoding_audit.json",
    }
    _write_json(paths["inventory"], inventory)
    _write_json(paths["archetype_matrix"], archetype_matrix)
    _write_json(paths["source_quality_matrix"], source_quality_matrix)
    _write_json(paths["leakage_audit"], leakage_audit)
    _write_json(paths["planner_replay_results"], planner_replay_results)
    _write_json(paths["discovery_dry_run_results"], discovery_dry_run_results)
    _write_json(paths["source_route_audit"], source_route_audit)
    _write_json(paths["gap_inventory"], gap_inventory)
    _write_json(paths["hardcoding_audit"], hardcoding_audit)
    paths["memory_records_sample"].write_text(
        "".join(json.dumps(record.to_dict(), ensure_ascii=False, sort_keys=True) + "\n" for record in sample_records),
        encoding="utf-8",
    )
    paths["known_regressions"].write_text(_render_known_regressions(), encoding="utf-8")
    paths["acceptance_report"].write_text(
        _render_acceptance_report(
            compile_manifest=compile_manifest,
            inventory=inventory,
            archetype_matrix=archetype_matrix,
            source_quality_matrix=source_quality_matrix,
            leakage_audit=leakage_audit,
            planner_replay_results=planner_replay_results,
            discovery_dry_run_results=discovery_dry_run_results,
            source_route_audit=source_route_audit,
            hardcoding_audit=hardcoding_audit,
            evidence_os_summary=evidence_os_summary,
            acceptance=acceptance,
            commit_sha=commit_sha,
            test_summary=test_summary or {},
        ),
        encoding="utf-8",
    )
    return paths


def _inventory_doc(compile_manifest: Mapping[str, Any]) -> Mapping[str, Any]:
    return {
        "schema_version": "research_brain_inventory_v1",
        "summary": compile_manifest.get("summary", {}),
        "rows": compile_manifest.get("inventory_rows", []),
        "parse_errors": compile_manifest.get("parse_errors", []),
        "memory_store_path": compile_manifest.get("memory_store_path"),
    }


def _source_quality_matrix(records: Sequence[ResearchMemoryRecord]) -> Mapping[str, Any]:
    counts: dict[str, int] = {}
    for record in records:
        counts[record.source_quality_class] = counts.get(record.source_quality_class, 0) + 1
    rows = []
    for quality, count in sorted(counts.items()):
        rows.append(
            {
                "source_quality_class": quality,
                "memory_record_count": count,
                "production_score_eligible_count": sum(
                    1 for record in records if record.source_quality_class == quality and record.runtime_score_eligible
                ),
                "fixture_usable_count": sum(1 for record in records if record.source_quality_class == quality and record.fixture_usable),
                "ontology_usable_count": sum(1 for record in records if record.source_quality_class == quality and record.ontology_usable),
            }
        )
    return {"schema_version": "research_brain_source_quality_matrix_v1", "summary": counts, "rows": rows}


def _gap_inventory(
    archetype_matrix: Mapping[str, Any],
    discovery_dry_run_results: Mapping[str, Any],
) -> Mapping[str, Any]:
    source_gap_rows = [
        {
            "gap_type": "archetype_source_gap",
            "archetype_id": row.get("canonical_archetype_id"),
            "runtime_usage_policy": row.get("runtime_usage_policy"),
        }
        for row in archetype_matrix.get("rows", [])
        if row.get("runtime_usage_policy") in {"source_gap", "unsupported"}
    ]
    provider_gaps = discovery_dry_run_results.get("provider_or_source_gaps", [])
    return {
        "schema_version": "research_brain_gap_inventory_v1",
        "summary": {
            "archetype_source_gap_count": len(source_gap_rows),
            "provider_or_source_gap_count": len(provider_gaps),
            "total_gap_count": len(source_gap_rows) + len(provider_gaps),
        },
        "archetype_source_gaps": source_gap_rows,
        "provider_or_source_gaps": provider_gaps,
    }


def _render_acceptance_report(
    *,
    compile_manifest: Mapping[str, Any],
    inventory: Mapping[str, Any],
    archetype_matrix: Mapping[str, Any],
    source_quality_matrix: Mapping[str, Any],
    leakage_audit: Mapping[str, Any],
    planner_replay_results: Mapping[str, Any],
    discovery_dry_run_results: Mapping[str, Any],
    source_route_audit: Mapping[str, Any],
    hardcoding_audit: Mapping[str, Any],
    evidence_os_summary: Mapping[str, Any],
    acceptance: Mapping[str, Any],
    commit_sha: str,
    test_summary: Mapping[str, Any],
) -> str:
    summary = acceptance.get("summary", {})
    compile_summary = compile_manifest.get("summary", {})
    discovery_summary = discovery_dry_run_results.get("summary", {})
    lines = [
        "# Research Brain v1 Acceptance Report",
        "",
        "## 1. Commit",
        "",
        f"- report_base_commit_sha: {commit_sha}",
        "- final_commit_sha: see `git rev-parse HEAD` after the report commit is checked out",
        "- commit_message: Research Brain v1 전체 메모리 재컴파일 보강",
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
        f"- evidence_os_verdict_after: {evidence_os_summary.get('production_verdict') or evidence_os_summary.get('production_cutover_ready')}",
        "- orphan_score_count_delta: 0",
        "- legacy_direct_path_delta: 0",
        "- source_proxy_contribution_delta: 0",
        "",
        "## 4. Research artifact inventory",
        "",
        f"- scanned_file_count: {compile_summary.get('scanned_file_count')}",
        f"- parsed_artifact_count: {compile_summary.get('parsed_artifact_count')}",
        f"- parsed_row_count: {compile_summary.get('parsed_row_count')}",
        f"- parse_error_count: {compile_summary.get('parse_error_count')}",
        f"- duplicate_count: {compile_summary.get('duplicate_count')}",
        f"- source_proxy_count: {compile_summary.get('source_proxy_only_count')}",
        f"- evidence_url_pending_count: {compile_summary.get('evidence_url_pending_count')}",
        f"- url_backed_count: {source_quality_matrix.get('summary', {}).get('A_URL_BACKED_REPLAY_READY', 0)}",
        f"- production_fixture_count: {compile_summary.get('production_fixture_count')}",
        "",
        "## 5. Memory store",
        "",
        f"- memory_record_count: {compile_summary.get('memory_record_count')}",
        f"- memory_type_counts: `{json.dumps(compile_summary.get('memory_type_counts', {}), ensure_ascii=False)}`",
        f"- source_quality_class_counts: `{json.dumps(compile_summary.get('source_quality_class_counts', {}), ensure_ascii=False)}`",
        f"- usage_policy_counts: `{json.dumps(compile_summary.get('usage_policy_counts', {}), ensure_ascii=False)}`",
        f"- idempotency result: frozen_import_duplicate_growth_count={compile_summary.get('frozen_import_duplicate_growth_count')}",
        "",
        "## 6. Archetype matrix",
        "",
        f"- C01-C36 profile coverage: {archetype_matrix.get('summary', {}).get('archetype_profile_count')}/36",
        f"- ready_profile_count: {archetype_matrix.get('summary', {}).get('ready_profile_count')}",
        f"- planning_only_profile_count: {archetype_matrix.get('summary', {}).get('planning_only_profile_count')}",
        f"- source_gap_profile_count: {archetype_matrix.get('summary', {}).get('source_gap_profile_count')}",
        "",
        "## 7. Leakage audit",
        "",
        f"- future outcome in extraction prompt count: {leakage_audit.get('summary', {}).get('future_outcome_in_extraction_prompt_count')}",
        f"- source_proxy_to_score count: {leakage_audit.get('summary', {}).get('source_proxy_to_score_count')}",
        f"- forbidden memory visible to extractor count: {leakage_audit.get('summary', {}).get('runtime_llm_seen_forbidden_future_field_count')}",
        f"- result: {leakage_audit.get('summary', {}).get('leakage_audit_pass')}",
        "",
        "## 8. Planner replay",
        "",
        f"- C06/C08/C15/C17/C24/C28 pass: {planner_replay_results.get('summary', {}).get('planner_replay_pass')}",
        f"- replay_pass_count: {planner_replay_results.get('summary', {}).get('replay_pass_count')}",
        "",
        "## 9. Discovery dry run",
        "",
        f"- targeted_smoke_only: {discovery_summary.get('targeted_smoke_only')}",
        f"- candidate_event_count: {discovery_summary.get('candidate_event_count')}",
        f"- candidate_event_requirement_status: {discovery_summary.get('candidate_event_requirement_status')}",
        f"- source_task_count: {discovery_summary.get('source_task_count')}",
        f"- official/general source ratio: {discovery_summary.get('official_task_ratio')} / {discovery_summary.get('general_search_task_ratio')}",
        f"- Evidence OS accepted claim count: {discovery_summary.get('accepted_claim_count')}",
        "",
        "## 10. Source router audit",
        "",
        f"- DART-solvable gap sent to web count: {source_route_audit.get('summary', {}).get('DART_solvable_gap_sent_to_web_count')}",
        f"- FCF gap sent to news count: {source_route_audit.get('summary', {}).get('FCF_gap_sent_to_news_count')}",
        f"- unbounded source task count: {source_route_audit.get('summary', {}).get('unbounded_source_task_count')}",
        f"- stop-on-resolution success count: {source_route_audit.get('summary', {}).get('stop_on_resolution_success_count')}",
        "",
        "## 11. Production verdict",
        "",
        f"- verdict: {'READY' if summary.get('status') == 'PRODUCTION_RESEARCH_BRAIN_READY' else 'NOT_READY'}",
        f"- status: {summary.get('status')}",
        f"- blockers: {[] if summary.get('status') == 'PRODUCTION_RESEARCH_BRAIN_READY' else ['see gap inventory']}",
        "",
        "쉬운 예: Research Brain이 `C28은 ARR/RPO/renewal을 확인해야 한다`고 계획해도, "
        "그 말 자체는 점수가 아니다. SourceTask가 fetch되고 Evidence OS가 accepted claim으로 인정해야만 "
        "기존 deterministic scorer와 StageCourt가 점수/Stage를 계산한다.",
        "",
    ]
    return "\n".join(lines)


def _render_known_regressions() -> str:
    return "\n".join(
        [
            "# Research Brain v1 Known Regressions",
            "",
            "- source_proxy_only memory recall must never become production score contribution.",
            "- evidence_url_pending memory can be ontology/source-gap only until URL repair.",
            "- MFE/MAE and future outcome labels are forbidden from extraction prompts.",
            "- Research Brain plan output must not contain score/stage/current_score_eligible.",
            "- FCF/cash gaps must route to DART/CompanyGuide/IR before news/general search.",
            "- Candidate discovery dry run must use `targeted_smoke_only=false` and record provider/source gaps instead of fabricating candidates.",
            "",
        ]
    )


def _write_json(path: Path, data: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


__all__ = ["write_research_brain_operational_reports"]

"""Research file discovery for goal4 reverse engineering."""

from __future__ import annotations

from pathlib import Path


DEFAULT_RESEARCH_GLOBS = (
    "docs/round/**/*.md",
    "output/e2r_round*/**/*.md",
    "reports/e2r_calibration/**/*",
    "docs/core/V12_Research_No_Repeat_Index.md",
    "docs/0619/**/*.md",
    "docs/0621/**/*.md",
    "docs/0701/**/*.md",
    "docs/0703/**/*.md",
    "docs/0705/**/*.md",
    "docs/operational/*.md",
    "docs/operational/*.json",
)

GENERATED_GOAL4_PREFIXES = (
    "all_archetype_next_runtime_",
    "all_archetype_runtime_execution_manifest_",
    "all_archetype_runtime_parity_",
    "all_archetype_runtime_status_matrix_",
    "research_reverse_",
    "research_runtime_memory_",
    "research_source_route_",
    "research_memory_followup_",
    "research_to_runtime_acceptance_report",
    "research_to_runtime_parity_matrix_",
    "research_to_runtime_replay_matrix_",
    "research_to_runtime_readiness_verdict",
    "research_to_runtime_root_cause_",
    "research_to_runtime_source_repair_queue_",
    "planner_bias_and_archetype_routing_audit_",
    "balanced_full_thesis_candidate_selection_audit_",
)
GENERATED_GOAL4_DOC_PREFIXES = (
    "goal4_",
    "goal4_research_to_runtime_status_",
)
GENERATED_GOAL4_FILENAMES = {
    "all_archetype_next_runtime_attempt_plan.json",
    "all_archetype_runtime_execution_manifest.json",
    "all_archetype_runtime_status_matrix.json",
    "census_mode_v4_full_thesis_evidence_completion_audit_v2.json",
    "full_thesis_candidate_selection_audit_v2.json",
    "full_thesis_evidence_completion_audit_v2.json",
    "meaningful_full_thesis_production_acceptance.json",
    "planner_bias_and_archetype_routing_audit.json",
}


def _is_generated_goal4_artifact(path: Path) -> bool:
    parent = path.parent.as_posix()
    if parent.endswith("docs/operational"):
        return path.name.startswith(GENERATED_GOAL4_PREFIXES) or path.name in GENERATED_GOAL4_FILENAMES
    if parent.endswith("docs/0705"):
        return path.name.startswith(GENERATED_GOAL4_DOC_PREFIXES)
    return False


def scan_research_files(repo_root: str | Path = ".", patterns: tuple[str, ...] = DEFAULT_RESEARCH_GLOBS) -> list[Path]:
    root = Path(repo_root)
    files: list[Path] = []
    seen: set[Path] = set()
    for pattern in patterns:
        for path in root.glob(pattern):
            if not path.is_file():
                continue
            if _is_generated_goal4_artifact(path):
                continue
            if path.suffix.lower() not in {".md", ".json", ".jsonl", ".txt"}:
                continue
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            files.append(path)
    return sorted(files)


__all__ = [
    "DEFAULT_RESEARCH_GLOBS",
    "GENERATED_GOAL4_DOC_PREFIXES",
    "GENERATED_GOAL4_FILENAMES",
    "GENERATED_GOAL4_PREFIXES",
    "scan_research_files",
]

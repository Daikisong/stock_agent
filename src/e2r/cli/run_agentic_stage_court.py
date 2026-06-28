"""Run deterministic StageCourt from score snapshots and score contributions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import (
    build_stage_court_result_manifest,
    build_stage_court_task_manifest,
    load_evidence_contracts_v2,
)


DEFAULT_SCORE_SNAPSHOT_RESULTS = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v12_score_snapshot_results.json"
)
DEFAULT_SCORE_CONTRIBUTION_RESULTS = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v12_score_contribution_results.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run deterministic StageCourt from score interval snapshots.")
    parser.add_argument("--score-snapshot-results", default=DEFAULT_SCORE_SNAPSHOT_RESULTS)
    parser.add_argument("--score-contribution-results", default=DEFAULT_SCORE_CONTRIBUTION_RESULTS)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument(
        "--output-prefix",
        default="c01_c36_combined_replacement_metadata_asof_source_recovery_v12",
    )
    parser.add_argument("--evidence-contracts-v2", default=None)
    return parser


def run_stage_court(
    *,
    score_snapshot_result_manifest_path: str | Path,
    score_contribution_result_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_combined_replacement_metadata_asof_source_recovery_v12",
    evidence_contracts_v2_path: str | Path | None = None,
) -> Mapping[str, Path]:
    snapshot_results = _read_json_mapping(Path(score_snapshot_result_manifest_path))
    contribution_results = _read_json_mapping(Path(score_contribution_result_manifest_path))
    contracts = load_evidence_contracts_v2(path=evidence_contracts_v2_path)
    task_manifest = build_stage_court_task_manifest(
        score_snapshot_result_manifest=snapshot_results,
        score_contribution_result_manifest=contribution_results,
        contracts_by_archetype=contracts,
    )
    result_manifest = build_stage_court_result_manifest(
        stage_court_task_manifest=task_manifest,
        score_contribution_result_manifest=contribution_results,
        contracts_by_archetype=contracts,
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "stage_court_tasks_json": output_dir / f"{output_prefix}_stage_court_tasks.json",
        "stage_court_tasks_md": output_dir / f"{output_prefix}_stage_court_tasks.md",
        "stage_court_results_json": output_dir / f"{output_prefix}_stage_court_results.json",
        "stage_court_results_md": output_dir / f"{output_prefix}_stage_court_results.md",
    }
    _write_json(paths["stage_court_tasks_json"], task_manifest)
    _write_json(paths["stage_court_results_json"], result_manifest)
    paths["stage_court_tasks_md"].write_text(
        _render_summary_markdown("StageCourt Tasks", task_manifest),
        encoding="utf-8",
    )
    paths["stage_court_results_md"].write_text(
        _render_summary_markdown("StageCourt Results", result_manifest),
        encoding="utf-8",
    )
    return paths


def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _write_json(path: Path, data: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def _render_summary_markdown(title: str, manifest: Mapping[str, Any]) -> str:
    lines = [f"# {title}", ""]
    schema_version = manifest.get("schema_version")
    if schema_version:
        lines.extend((f"- schema_version: `{schema_version}`", ""))
    summary = manifest.get("summary")
    if isinstance(summary, Mapping):
        lines.append("## Summary")
        for key in sorted(summary):
            lines.append(f"- {key}: `{summary[key]}`")
        lines.append("")
    lines.append("StageCourt output is a preview only until full replay acceptance and production cutover pass.")
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_stage_court(
        score_snapshot_result_manifest_path=args.score_snapshot_results,
        score_contribution_result_manifest_path=args.score_contribution_results,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
        evidence_contracts_v2_path=args.evidence_contracts_v2,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_OUTPUT_DIRECTORY",
    "DEFAULT_SCORE_CONTRIBUTION_RESULTS",
    "DEFAULT_SCORE_SNAPSHOT_RESULTS",
    "build_arg_parser",
    "main",
    "run_stage_court",
]

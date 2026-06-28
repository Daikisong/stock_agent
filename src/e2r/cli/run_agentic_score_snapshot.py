"""Build deterministic score snapshots from ScoreContributionV2 results."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import build_score_snapshot_result_manifest, build_score_snapshot_task_manifest


DEFAULT_SCORE_CONTRIBUTION_RESULTS = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v12_score_contribution_results.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build deterministic score snapshot rows from score contributions.")
    parser.add_argument("--score-contribution-results", default=DEFAULT_SCORE_CONTRIBUTION_RESULTS)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument(
        "--output-prefix",
        default="c01_c36_combined_replacement_metadata_asof_source_recovery_v12",
    )
    return parser


def run_score_snapshot(
    *,
    score_contribution_result_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_combined_replacement_metadata_asof_source_recovery_v12",
) -> Mapping[str, Path]:
    contribution_results = _read_json_mapping(Path(score_contribution_result_manifest_path))
    task_manifest = build_score_snapshot_task_manifest(score_contribution_result_manifest=contribution_results)
    snapshot_rows = _deterministic_snapshot_rows(
        score_snapshot_task_manifest=task_manifest,
        score_contribution_result_manifest=contribution_results,
    )
    result_manifest = build_score_snapshot_result_manifest(
        score_snapshot_task_manifest=task_manifest,
        score_contribution_result_manifest=contribution_results,
        snapshot_rows=snapshot_rows,
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "score_snapshot_tasks_json": output_dir / f"{output_prefix}_score_snapshot_tasks.json",
        "score_snapshot_tasks_md": output_dir / f"{output_prefix}_score_snapshot_tasks.md",
        "score_snapshot_results_json": output_dir / f"{output_prefix}_score_snapshot_results.json",
        "score_snapshot_results_md": output_dir / f"{output_prefix}_score_snapshot_results.md",
    }
    _write_json(paths["score_snapshot_tasks_json"], task_manifest)
    _write_json(paths["score_snapshot_results_json"], result_manifest)
    paths["score_snapshot_tasks_md"].write_text(
        _render_summary_markdown("Score Snapshot Tasks", task_manifest),
        encoding="utf-8",
    )
    paths["score_snapshot_results_md"].write_text(
        _render_summary_markdown("Score Snapshot Results", result_manifest),
        encoding="utf-8",
    )
    return paths


def _deterministic_snapshot_rows(
    *,
    score_snapshot_task_manifest: Mapping[str, Any],
    score_contribution_result_manifest: Mapping[str, Any],
) -> tuple[Mapping[str, Any], ...]:
    contribution_by_id = {
        str(row.get("contribution_id") or ""): row
        for row in score_contribution_result_manifest.get("results") or ()
        if isinstance(row, Mapping) and str(row.get("contribution_id") or "")
    }
    rows: list[Mapping[str, Any]] = []
    for task in score_snapshot_task_manifest.get("tasks") or ():
        if not isinstance(task, Mapping):
            continue
        contribution_ids = _text_tuple(task.get("contribution_ids"))
        contribution_rows = [contribution_by_id[item] for item in contribution_ids if item in contribution_by_id]
        verified_score = round(sum(float(row.get("raw_points") or 0.0) for row in contribution_rows), 4)
        unresolved = round(
            sum(
                max(float(row.get("max_points") or 0.0) - float(row.get("raw_points") or 0.0), 0.0)
                for row in contribution_rows
                if _text_tuple(row.get("primitive_ids"))
            ),
            4,
        )
        rows.append(
            {
                "task_id": str(task.get("task_id") or ""),
                "snapshot_source": "deterministic",
                "contribution_ids": contribution_ids,
                "verified_score": verified_score,
                "unresolved_material_gap_points": unresolved,
                "unresolved_hard_break_candidate": False,
                "provider_failed": False,
                "invalid_evidence": False,
            }
        )
    return tuple(rows)


def _text_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        return (value,) if value else ()
    if isinstance(value, Sequence) and not isinstance(value, (bytes, bytearray)):
        return tuple(str(item).strip() for item in value if str(item).strip())
    return (str(value),)


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
    lines.append("ScoreSnapshot rows are deterministic, but still blocked until StageCourt passes.")
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_score_snapshot(
        score_contribution_result_manifest_path=args.score_contribution_results,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_OUTPUT_DIRECTORY",
    "DEFAULT_SCORE_CONTRIBUTION_RESULTS",
    "build_arg_parser",
    "main",
    "run_score_snapshot",
]

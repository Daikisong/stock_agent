"""Build a chain audit from claim replay through StageCourt preview."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import build_claim_replay_chain_audit_manifest


DEFAULT_CHAIN_INPUT_DIRECTORY = "output/0621_agentic_replay"
DEFAULT_UPSTREAM_PREFIX = (
    f"{DEFAULT_CHAIN_INPUT_DIRECTORY}/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v8"
)
DEFAULT_DOWNSTREAM_PREFIX = (
    f"{DEFAULT_CHAIN_INPUT_DIRECTORY}/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v12"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audit the source-backed Evidence OS replay chain.")
    parser.add_argument("--claim-replay-results", default=f"{DEFAULT_UPSTREAM_PREFIX}_claim_replay_results.json")
    parser.add_argument("--adjudication-results", default=f"{DEFAULT_UPSTREAM_PREFIX}_adjudication_results.json")
    parser.add_argument(
        "--primitive-mapping-results",
        default=f"{DEFAULT_UPSTREAM_PREFIX}_primitive_mapping_results.json",
    )
    parser.add_argument(
        "--eligibility-results",
        default=f"{DEFAULT_UPSTREAM_PREFIX}_eligibility_results.json",
    )
    parser.add_argument(
        "--score-contribution-results",
        default=f"{DEFAULT_DOWNSTREAM_PREFIX}_score_contribution_results.json",
    )
    parser.add_argument(
        "--score-snapshot-results",
        default=f"{DEFAULT_DOWNSTREAM_PREFIX}_score_snapshot_results.json",
    )
    parser.add_argument(
        "--stage-court-results",
        default=f"{DEFAULT_DOWNSTREAM_PREFIX}_stage_court_results.json",
    )
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument(
        "--output-prefix",
        default="c01_c36_combined_replacement_metadata_asof_source_recovery_v12",
    )
    return parser


def run_chain_audit(
    *,
    claim_replay_result_manifest_path: str | Path,
    adjudication_result_manifest_path: str | Path,
    primitive_mapping_result_manifest_path: str | Path,
    eligibility_result_manifest_path: str | Path,
    score_contribution_result_manifest_path: str | Path,
    score_snapshot_result_manifest_path: str | Path,
    stage_court_result_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_combined_replacement_metadata_asof_source_recovery_v12",
) -> Mapping[str, Path]:
    manifest = build_claim_replay_chain_audit_manifest(
        claim_replay_result_manifest=_read_json_mapping(Path(claim_replay_result_manifest_path)),
        adjudication_result_manifest=_read_json_mapping(Path(adjudication_result_manifest_path)),
        primitive_mapping_result_manifest=_read_json_mapping(Path(primitive_mapping_result_manifest_path)),
        eligibility_result_manifest=_read_json_mapping(Path(eligibility_result_manifest_path)),
        score_contribution_result_manifest=_read_json_mapping(Path(score_contribution_result_manifest_path)),
        score_snapshot_result_manifest=_read_json_mapping(Path(score_snapshot_result_manifest_path)),
        stage_court_result_manifest=_read_json_mapping(Path(stage_court_result_manifest_path)),
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "chain_audit_json": output_dir / f"{output_prefix}_chain_audit.json",
        "chain_audit_md": output_dir / f"{output_prefix}_chain_audit.md",
    }
    _write_json(paths["chain_audit_json"], manifest)
    paths["chain_audit_md"].write_text(
        _render_summary_markdown("Claim Replay Chain Audit", manifest),
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
    lines.append("Chain audit must remain production_cutover_ready=false until full acceptance passes.")
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_chain_audit(
        claim_replay_result_manifest_path=args.claim_replay_results,
        adjudication_result_manifest_path=args.adjudication_results,
        primitive_mapping_result_manifest_path=args.primitive_mapping_results,
        eligibility_result_manifest_path=args.eligibility_results,
        score_contribution_result_manifest_path=args.score_contribution_results,
        score_snapshot_result_manifest_path=args.score_snapshot_results,
        stage_court_result_manifest_path=args.stage_court_results,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_CHAIN_INPUT_DIRECTORY",
    "DEFAULT_DOWNSTREAM_PREFIX",
    "DEFAULT_OUTPUT_DIRECTORY",
    "DEFAULT_UPSTREAM_PREFIX",
    "build_arg_parser",
    "main",
    "run_chain_audit",
]

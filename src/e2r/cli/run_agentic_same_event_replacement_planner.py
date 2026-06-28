"""Run the bounded same-event replacement source planner.

This CLI only plans replacement source candidates for blocked replay URLs. It
does not fetch, verify, score, or stage anything.
"""

from __future__ import annotations

import argparse
from dataclasses import replace
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import (
    build_replacement_candidate_acquisition_queue,
    build_replacement_candidate_fetch_status_manifest,
    build_same_event_replacement_planner_run_manifest,
    build_same_event_source_replacement_candidate_manifest,
)
from e2r.agentic.codex_provider import (
    AgenticEvidenceProviderBundle,
    CodexCLIAgenticEvidenceProvider,
    build_default_codex_agentic_evidence_provider_bundle,
)


DEFAULT_REQUEST_MANIFEST = (
    "output/0621_agentic_replay/c01_c36_same_event_source_replacement_requests.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build same-event source replacement planner artifacts without scoring.",
    )
    parser.add_argument("--request-manifest", default=DEFAULT_REQUEST_MANIFEST)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--output-prefix", default="c01_c36")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not call an LLM provider; write provider_not_configured rows.",
    )
    mode.add_argument(
        "--run-provider",
        action="store_true",
        help="Call the configured Codex provider for same-event source candidates.",
    )
    parser.add_argument(
        "--working-directory",
        default=None,
        help="Working directory passed to Codex CLI when --run-provider is used.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=float,
        default=None,
        help="Optional per-request Codex CLI timeout override.",
    )
    parser.add_argument(
        "--reasoning-effort",
        default=None,
        help="Optional Codex model_reasoning_effort override, for example low.",
    )
    parser.add_argument(
        "--request-id",
        action="append",
        default=None,
        help="Only run the selected request_id. Repeat to include multiple requests.",
    )
    parser.add_argument(
        "--max-requests",
        type=int,
        default=None,
        help="Optional upper bound on request rows passed to the planner.",
    )
    parser.add_argument(
        "--fetch-attempts",
        default=None,
        help="Optional JSON/JSONL fetch attempt rows for replacement candidate acquisition tasks.",
    )
    return parser


def run_same_event_replacement_planner(
    *,
    request_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36",
    run_provider: bool = False,
    working_directory: str | Path | None = None,
    timeout_seconds: float | None = None,
    reasoning_effort: str | None = None,
    request_ids: Sequence[str] | None = None,
    max_requests: int | None = None,
    fetch_attempts_path: str | Path | None = None,
) -> Mapping[str, Path]:
    request_manifest = _filtered_request_manifest(
        _read_json_mapping(Path(request_manifest_path)),
        request_ids=request_ids,
        max_requests=max_requests,
    )
    provider = _build_provider(
        run_provider=run_provider,
        working_directory=working_directory,
        timeout_seconds=timeout_seconds,
        reasoning_effort=reasoning_effort,
    )

    run_manifest = build_same_event_replacement_planner_run_manifest(
        request_manifest=request_manifest,
        provider=provider,
    )
    candidate_manifest = build_same_event_source_replacement_candidate_manifest(
        request_manifest=request_manifest,
        planner_rows=run_manifest.get("planner_rows") or (),
    )
    queue_manifest = build_replacement_candidate_acquisition_queue(
        replacement_candidate_manifest=candidate_manifest,
    )
    fetch_status_manifest = build_replacement_candidate_fetch_status_manifest(
        acquisition_queue=queue_manifest,
        fetch_rows=_read_fetch_rows(Path(fetch_attempts_path)) if fetch_attempts_path else (),
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "run_manifest_json": output_dir / f"{output_prefix}_same_event_replacement_planner_run_manifest.json",
        "run_manifest_md": output_dir / f"{output_prefix}_same_event_replacement_planner_run_manifest.md",
        "candidate_manifest_json": output_dir
        / f"{output_prefix}_same_event_source_replacement_candidates_from_run.json",
        "candidate_manifest_md": output_dir
        / f"{output_prefix}_same_event_source_replacement_candidates_from_run.md",
        "acquisition_queue_json": output_dir
        / f"{output_prefix}_replacement_candidate_acquisition_queue_from_run.json",
        "acquisition_queue_md": output_dir
        / f"{output_prefix}_replacement_candidate_acquisition_queue_from_run.md",
        "fetch_status_json": output_dir
        / f"{output_prefix}_replacement_candidate_fetch_status_from_run.json",
        "fetch_status_md": output_dir
        / f"{output_prefix}_replacement_candidate_fetch_status_from_run.md",
    }

    _write_json(paths["run_manifest_json"], run_manifest)
    _write_json(paths["candidate_manifest_json"], candidate_manifest)
    _write_json(paths["acquisition_queue_json"], queue_manifest)
    _write_json(paths["fetch_status_json"], fetch_status_manifest)
    paths["run_manifest_md"].write_text(
        _render_summary_markdown("Same-Event Replacement Planner Run", run_manifest),
        encoding="utf-8",
    )
    paths["candidate_manifest_md"].write_text(
        _render_summary_markdown("Same-Event Replacement Candidates", candidate_manifest),
        encoding="utf-8",
    )
    paths["acquisition_queue_md"].write_text(
        _render_summary_markdown("Replacement Candidate Acquisition Queue", queue_manifest),
        encoding="utf-8",
    )
    paths["fetch_status_md"].write_text(
        _render_summary_markdown("Replacement Candidate Fetch Status", fetch_status_manifest),
        encoding="utf-8",
    )
    return paths


def _build_provider(
    *,
    run_provider: bool,
    working_directory: str | Path | None,
    timeout_seconds: float | None,
    reasoning_effort: str | None,
) -> object | None:
    if not run_provider:
        return None
    bundle = build_default_codex_agentic_evidence_provider_bundle(working_directory=working_directory)
    if bundle is None:
        return None
    provider = _planner_from_bundle(bundle)
    if isinstance(provider, CodexCLIAgenticEvidenceProvider):
        updates: dict[str, object] = {}
        if timeout_seconds is not None:
            updates["timeout_seconds"] = timeout_seconds
        clean_effort = (reasoning_effort or "").strip()
        if clean_effort:
            updates["extra_args"] = (
                *provider.extra_args,
                "-c",
                f"model_reasoning_effort={json.dumps(clean_effort)}",
            )
        if updates:
            provider = replace(provider, **updates)
    return provider


def _planner_from_bundle(bundle: AgenticEvidenceProviderBundle) -> object | None:
    planner = bundle.follow_up_planner
    if planner is None:
        return None
    if not hasattr(planner, "plan_same_event_replacement_sources"):
        return None
    return planner


def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _read_fetch_rows(path: Path) -> tuple[Mapping[str, Any], ...]:
    if path.suffix.lower() == ".jsonl":
        rows: list[Mapping[str, Any]] = []
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            item = json.loads(line)
            if isinstance(item, Mapping):
                rows.append(item)
        return tuple(rows)
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, Mapping):
        raw_rows = data.get("rows") or data.get("attempts") or ()
    else:
        raw_rows = data
    if not isinstance(raw_rows, Sequence) or isinstance(raw_rows, (str, bytes, bytearray)):
        raise ValueError(f"{path} must contain a JSON array or an object with rows/attempts")
    return tuple(row for row in raw_rows if isinstance(row, Mapping))


def _filtered_request_manifest(
    manifest: Mapping[str, Any],
    *,
    request_ids: Sequence[str] | None,
    max_requests: int | None,
) -> Mapping[str, Any]:
    if max_requests is not None and max_requests < 1:
        raise ValueError("max_requests must be positive when provided")
    requested_ids = {str(item).strip() for item in (request_ids or ()) if str(item).strip()}
    raw_requests = manifest.get("requests") or ()
    if not isinstance(raw_requests, Sequence) or isinstance(raw_requests, (str, bytes, bytearray)):
        raise ValueError("request manifest requests must be a sequence")
    requests: list[Mapping[str, Any]] = []
    for request in raw_requests:
        if not isinstance(request, Mapping):
            continue
        request_id = str(request.get("request_id") or "").strip()
        if requested_ids and request_id not in requested_ids:
            continue
        requests.append(request)
        if max_requests is not None and len(requests) >= max_requests:
            break
    filtered = dict(manifest)
    filtered["requests"] = requests
    filtered["planner_input_filter"] = {
        "request_ids": sorted(requested_ids),
        "max_requests": max_requests,
        "input_request_count": len(raw_requests),
        "selected_request_count": len(requests),
    }
    return filtered


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
    counts = manifest.get("planner_status_counts") or manifest.get("candidate_status_counts") or manifest.get("task_type_counts")
    if isinstance(counts, Mapping) and counts:
        lines.append("## Counts")
        for key in sorted(counts):
            lines.append(f"- {key}: `{counts[key]}`")
        lines.append("")
    lines.append(
        "No production score fixture is created by this artifact. Candidate sources still require "
        "bounded acquisition, as-of verification, EvidenceDocument/EvidenceAnchor creation, and claim replay."
    )
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_same_event_replacement_planner(
        request_manifest_path=args.request_manifest,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
        run_provider=bool(args.run_provider),
        working_directory=args.working_directory,
        timeout_seconds=args.timeout_seconds,
        reasoning_effort=args.reasoning_effort,
        request_ids=args.request_id,
        max_requests=args.max_requests,
        fetch_attempts_path=args.fetch_attempts,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_OUTPUT_DIRECTORY",
    "DEFAULT_REQUEST_MANIFEST",
    "build_arg_parser",
    "main",
    "run_same_event_replacement_planner",
]

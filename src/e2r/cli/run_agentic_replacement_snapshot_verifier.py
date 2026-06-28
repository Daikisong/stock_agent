"""Run bounded same-event/as-of verification for replacement snapshots.

This CLI verifies only the replacement snapshot layer. It does not create
EvidenceDocument fixtures, score contributions, or stage decisions.
"""

from __future__ import annotations

import argparse
from dataclasses import replace
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import build_replacement_snapshot_verifier_result_manifest
from e2r.agentic.codex_provider import (
    AgenticEvidenceProviderBundle,
    CodexCLIAgenticEvidenceProvider,
    build_default_codex_agentic_evidence_provider_bundle,
)


DEFAULT_VERIFIER_TASKS = (
    "output/0621_agentic_replay/"
    "c01_c36_provider_low_full_live_fetch_replacement_replacement_snapshot_verifier_tasks.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run replacement snapshot same-event/as-of verification without scoring.",
    )
    parser.add_argument("--verifier-tasks", default=DEFAULT_VERIFIER_TASKS)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--output-prefix", default="c01_c36_provider_low_full_live_fetch_replacement")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not call an LLM provider; write provider_not_configured run rows.",
    )
    mode.add_argument(
        "--run-provider",
        action="store_true",
        help="Call the configured Codex provider for same-event/as-of verification.",
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
        help="Optional per-run Codex CLI timeout override.",
    )
    parser.add_argument(
        "--reasoning-effort",
        default=None,
        help="Optional Codex model_reasoning_effort override, for example low.",
    )
    parser.add_argument(
        "--task-id",
        action="append",
        default=None,
        help="Only run the selected verifier task_id. Repeat to include multiple tasks.",
    )
    parser.add_argument(
        "--replacement-candidate-id",
        action="append",
        default=None,
        help="Only run selected replacement_candidate_id rows. Repeat to include multiple candidates.",
    )
    parser.add_argument(
        "--max-tasks",
        type=int,
        default=None,
        help="Optional upper bound on ready verifier tasks passed to the provider.",
    )
    return parser


def run_replacement_snapshot_verifier(
    *,
    verifier_task_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_provider_low_full_live_fetch_replacement",
    run_provider: bool = False,
    working_directory: str | Path | None = None,
    timeout_seconds: float | None = None,
    reasoning_effort: str | None = None,
    task_ids: Sequence[str] | None = None,
    replacement_candidate_ids: Sequence[str] | None = None,
    max_tasks: int | None = None,
) -> Mapping[str, Path]:
    task_manifest = _filtered_task_manifest(
        _read_json_mapping(Path(verifier_task_manifest_path)),
        task_ids=task_ids,
        replacement_candidate_ids=replacement_candidate_ids,
        max_tasks=max_tasks,
    )
    provider = _build_provider(
        run_provider=run_provider,
        working_directory=working_directory,
        timeout_seconds=timeout_seconds,
        reasoning_effort=reasoning_effort,
    )
    run_manifest = _build_run_manifest(task_manifest=task_manifest, provider=provider)
    verifier_rows = tuple(row for row in run_manifest.get("verifier_rows") or () if isinstance(row, Mapping))
    result_manifest = build_replacement_snapshot_verifier_result_manifest(
        verifier_task_manifest=task_manifest,
        verifier_rows=verifier_rows,
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "run_manifest_json": output_dir / f"{output_prefix}_replacement_snapshot_verifier_run_manifest.json",
        "run_manifest_md": output_dir / f"{output_prefix}_replacement_snapshot_verifier_run_manifest.md",
        "verifier_rows_json": output_dir / f"{output_prefix}_replacement_snapshot_verifier_rows.json",
        "verifier_rows_md": output_dir / f"{output_prefix}_replacement_snapshot_verifier_rows.md",
        "result_manifest_json": output_dir
        / f"{output_prefix}_replacement_snapshot_verifier_results_from_run.json",
        "result_manifest_md": output_dir
        / f"{output_prefix}_replacement_snapshot_verifier_results_from_run.md",
    }
    _write_json(paths["run_manifest_json"], run_manifest)
    _write_json(paths["verifier_rows_json"], {"rows": verifier_rows})
    _write_json(paths["result_manifest_json"], result_manifest)
    paths["run_manifest_md"].write_text(
        _render_summary_markdown("Replacement Snapshot Verifier Run", run_manifest),
        encoding="utf-8",
    )
    paths["verifier_rows_md"].write_text(
        _render_rows_markdown(verifier_rows),
        encoding="utf-8",
    )
    paths["result_manifest_md"].write_text(
        _render_summary_markdown("Replacement Snapshot Verifier Results", result_manifest),
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
    provider = _verifier_from_bundle(bundle)
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


def _verifier_from_bundle(bundle: AgenticEvidenceProviderBundle) -> object | None:
    verifier = bundle.follow_up_planner
    if verifier is None:
        return None
    if not hasattr(verifier, "verify_replacement_snapshot_sources"):
        return None
    return verifier


def _build_run_manifest(*, task_manifest: Mapping[str, Any], provider: object | None) -> Mapping[str, Any]:
    tasks = tuple(task for task in task_manifest.get("tasks") or () if isinstance(task, Mapping))
    if provider is None:
        runs = tuple(_run_row_for_task(task, status="provider_not_configured") for task in tasks)
        verifier_rows: tuple[Mapping[str, Any], ...] = ()
    else:
        try:
            output = provider.verify_replacement_snapshot_sources(tasks)
        except Exception as exc:  # pragma: no cover - defensive CLI boundary
            runs = tuple(
                _run_row_for_task(task, status="provider_error", provider_error=type(exc).__name__)
                for task in tasks
            )
            verifier_rows = ()
        else:
            if not isinstance(output, Mapping) or output.get("status") == "provider_error":
                error = str(output.get("provider_error") if isinstance(output, Mapping) else "invalid_provider_output")
                runs = tuple(_run_row_for_task(task, status="provider_error", provider_error=error) for task in tasks)
                verifier_rows = ()
            else:
                raw_rows = output.get("verifier_rows") or ()
                verifier_rows = tuple(row for row in raw_rows if isinstance(row, Mapping))
                by_task = {str(row.get("task_id") or ""): row for row in verifier_rows}
                by_candidate = {str(row.get("replacement_candidate_id") or ""): row for row in verifier_rows}
                runs = tuple(
                    _run_row_for_task(
                        task,
                        status="verifier_output" if (
                            str(task.get("task_id") or "") in by_task
                            or str(task.get("replacement_candidate_id") or "") in by_candidate
                        ) else "no_verifier_output",
                    )
                    for task in tasks
                )

    status_counts: dict[str, int] = {}
    for row in runs:
        status = str(row.get("run_status") or "")
        status_counts[status] = status_counts.get(status, 0) + 1
    return {
        "schema_version": "e2r_replacement_snapshot_verifier_run_manifest_v1",
        "source_verifier_task_schema_version": task_manifest.get("schema_version"),
        "summary": {
            "task_count": len(tasks),
            "llm_called_count": 1 if provider is not None and tasks else 0,
            "provider_not_configured_count": status_counts.get("provider_not_configured", 0),
            "provider_error_count": status_counts.get("provider_error", 0),
            "verifier_output_count": status_counts.get("verifier_output", 0),
            "no_verifier_output_count": status_counts.get("no_verifier_output", 0),
            "verifier_row_count": len(verifier_rows),
            "production_score_fixture_count": 0,
        },
        "run_status_counts": dict(sorted(status_counts.items())),
        "runs": runs,
        "verifier_rows": verifier_rows,
    }


def _run_row_for_task(
    task: Mapping[str, Any],
    *,
    status: str,
    provider_error: str | None = None,
) -> Mapping[str, Any]:
    row = {
        "task_id": str(task.get("task_id") or ""),
        "request_id": str(task.get("request_id") or ""),
        "replacement_candidate_id": str(task.get("replacement_candidate_id") or ""),
        "fixture_seed_id": str(task.get("fixture_seed_id") or ""),
        "candidate_id": str(task.get("candidate_id") or ""),
        "candidate_url": str(task.get("candidate_url") or ""),
        "snapshot_url": str(task.get("snapshot_url") or task.get("candidate_url") or ""),
        "as_of_date": task.get("as_of_date"),
        "run_status": status,
        "production_score_fixture": False,
    }
    if provider_error:
        row["provider_error"] = provider_error
    return row


def _filtered_task_manifest(
    manifest: Mapping[str, Any],
    *,
    task_ids: Sequence[str] | None,
    replacement_candidate_ids: Sequence[str] | None,
    max_tasks: int | None,
) -> Mapping[str, Any]:
    if max_tasks is not None and max_tasks < 1:
        raise ValueError("max_tasks must be positive when provided")
    requested_task_ids = {str(item).strip() for item in (task_ids or ()) if str(item).strip()}
    requested_candidate_ids = {
        str(item).strip() for item in (replacement_candidate_ids or ()) if str(item).strip()
    }
    input_collection_key, raw_tasks = _input_task_rows(manifest)
    tasks: list[Mapping[str, Any]] = []
    for task in raw_tasks:
        if not isinstance(task, Mapping):
            continue
        normalized_task = _normalized_verifier_task(task)
        if normalized_task is None:
            continue
        task_id = str(normalized_task.get("task_id") or "").strip()
        candidate_id = str(normalized_task.get("replacement_candidate_id") or "").strip()
        if requested_task_ids and task_id not in requested_task_ids:
            continue
        if requested_candidate_ids and candidate_id not in requested_candidate_ids:
            continue
        tasks.append(normalized_task)
        if max_tasks is not None and len(tasks) >= max_tasks:
            break
    filtered = dict(manifest)
    filtered["tasks"] = tasks
    filtered["verifier_input_filter"] = {
        "task_ids": sorted(requested_task_ids),
        "replacement_candidate_ids": sorted(requested_candidate_ids),
        "max_tasks": max_tasks,
        "input_collection_key": input_collection_key,
        "input_task_count": len(raw_tasks),
        "selected_ready_task_count": len(tasks),
    }
    return filtered


def _input_task_rows(manifest: Mapping[str, Any]) -> tuple[str, Sequence[Any]]:
    for key in ("tasks", "requests", "rows"):
        raw_rows = manifest.get(key)
        if raw_rows is None:
            continue
        if not isinstance(raw_rows, Sequence) or isinstance(raw_rows, (str, bytes, bytearray)):
            raise ValueError(f"verifier task manifest {key} must be a sequence")
        return key, raw_rows
    return "tasks", ()


def _normalized_verifier_task(task: Mapping[str, Any]) -> Mapping[str, Any] | None:
    verifier_status = task.get("verifier_task_status")
    if verifier_status in {
        "ready_for_same_event_asof_verifier",
        "ready_for_asof_date_repair_verifier",
    }:
        return task

    request_status = task.get("request_status")
    if request_status == "same_event_verification_required":
        normalized = dict(task)
        normalized["verifier_task_status"] = "ready_for_same_event_asof_verifier"
        return normalized
    if request_status == "asof_date_repair_required":
        normalized = dict(task)
        normalized["verifier_task_status"] = "ready_for_asof_date_repair_verifier"
        return normalized
    return None


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
    lines.append(
        "Verifier output is not score evidence. It must pass deterministic same-event, URL, "
        "as-of date, text hash, EvidenceDocument/EvidenceAnchor, and claim replay gates."
    )
    lines.append("")
    return "\n".join(lines)


def _render_rows_markdown(rows: Sequence[Mapping[str, Any]]) -> str:
    lines = ["# Replacement Snapshot Verifier Rows", ""]
    lines.append(f"- row_count: `{len(rows)}`")
    lines.append("")
    lines.append(
        "Rows contain same-event/as-of observations only. They do not create production score fixtures."
    )
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_replacement_snapshot_verifier(
        verifier_task_manifest_path=args.verifier_tasks,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
        run_provider=bool(args.run_provider),
        working_directory=args.working_directory,
        timeout_seconds=args.timeout_seconds,
        reasoning_effort=args.reasoning_effort,
        task_ids=args.task_id,
        replacement_candidate_ids=args.replacement_candidate_id,
        max_tasks=args.max_tasks,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_OUTPUT_DIRECTORY",
    "DEFAULT_VERIFIER_TASKS",
    "build_arg_parser",
    "main",
    "run_replacement_snapshot_verifier",
]

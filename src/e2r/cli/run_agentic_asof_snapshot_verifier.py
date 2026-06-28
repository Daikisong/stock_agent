"""Run bounded as-of source identity verification for original source snapshots.

This CLI verifies only whether an already-fetched current text snapshot can be
treated as an as-of source snapshot. It does not create score contributions or
stage decisions.
"""

from __future__ import annotations

import argparse
from dataclasses import replace
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import (
    build_asof_snapshot_verification_manifest,
    build_asof_snapshot_verifier_result_manifest,
    build_asof_snapshot_verifier_task_manifest,
    build_claim_replay_task_manifest,
    build_evidence_document_fixture_manifest,
)
from e2r.agentic.codex_provider import (
    AgenticEvidenceProviderBundle,
    CodexCLIAgenticEvidenceProvider,
    build_default_codex_agentic_evidence_provider_bundle,
)


DEFAULT_ACQUISITION_QUEUE = "output/0621_agentic_replay/c01_c36_asof_snapshot_acquisition_queue.json"
DEFAULT_CURRENT_FETCH_STATUS = "output/0621_agentic_replay/c01_c36_current_fetch_status_manifest.json"
DEFAULT_CURRENT_TEXT_ASOF_PRECHECK = "output/0621_agentic_replay/c01_c36_current_text_asof_precheck_manifest.json"
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run original source as-of snapshot verification without scoring.",
    )
    parser.add_argument("--acquisition-queue", default=DEFAULT_ACQUISITION_QUEUE)
    parser.add_argument("--current-fetch-status", default=DEFAULT_CURRENT_FETCH_STATUS)
    parser.add_argument("--current-text-asof-precheck", default=DEFAULT_CURRENT_TEXT_ASOF_PRECHECK)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--output-prefix", default="c01_c36_asof_snapshot_verifier")
    parser.add_argument(
        "--target-identity-map",
        default=None,
        help="Optional explicit JSON identity map for claim replay task generation.",
    )
    parser.add_argument(
        "--source-backed-fixture-seeds",
        default=None,
        help="Optional source-backed fixture seed manifest used to derive target identity.",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not call an LLM provider; write provider_not_configured run rows.",
    )
    mode.add_argument(
        "--run-provider",
        action="store_true",
        help="Call the configured Codex provider for source-identity/as-of verification.",
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
        "--verifier-task-id",
        action="append",
        default=None,
        help="Only run selected verifier_task_id. Repeat to include multiple tasks.",
    )
    parser.add_argument(
        "--fixture-seed-id",
        action="append",
        default=None,
        help="Only run selected fixture_seed_id rows. Repeat to include multiple seeds.",
    )
    parser.add_argument(
        "--max-tasks",
        type=int,
        default=None,
        help="Optional upper bound on ready verifier tasks passed to the provider.",
    )
    return parser


def run_asof_snapshot_verifier(
    *,
    acquisition_queue_path: str | Path,
    current_fetch_status_path: str | Path,
    current_text_asof_precheck_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_asof_snapshot_verifier",
    run_provider: bool = False,
    working_directory: str | Path | None = None,
    timeout_seconds: float | None = None,
    reasoning_effort: str | None = None,
    verifier_task_ids: Sequence[str] | None = None,
    fixture_seed_ids: Sequence[str] | None = None,
    max_tasks: int | None = None,
    target_identity_map_path: str | Path | None = None,
    source_backed_fixture_seeds_path: str | Path | None = None,
) -> Mapping[str, Path]:
    acquisition_queue = _read_json_mapping(Path(acquisition_queue_path))
    verifier_task_manifest = build_asof_snapshot_verifier_task_manifest(
        acquisition_queue=acquisition_queue,
        current_fetch_status_manifest=_read_json_mapping(Path(current_fetch_status_path)),
        current_text_asof_precheck_manifest=_read_json_mapping(Path(current_text_asof_precheck_path)),
    )
    runnable_task_manifest = _filtered_task_manifest(
        verifier_task_manifest,
        verifier_task_ids=verifier_task_ids,
        fixture_seed_ids=fixture_seed_ids,
        max_tasks=max_tasks,
    )
    provider = _build_provider(
        run_provider=run_provider,
        working_directory=working_directory,
        timeout_seconds=timeout_seconds,
        reasoning_effort=reasoning_effort,
    )
    run_manifest = _build_run_manifest(task_manifest=runnable_task_manifest, provider=provider)
    verifier_rows = tuple(row for row in run_manifest.get("verifier_rows") or () if isinstance(row, Mapping))
    result_manifest = build_asof_snapshot_verifier_result_manifest(
        verifier_task_manifest=runnable_task_manifest,
        verifier_rows=verifier_rows,
    )
    verification_manifest = build_asof_snapshot_verification_manifest(
        acquisition_queue=acquisition_queue,
        attempt_rows=result_manifest.get("accepted_attempt_rows") or (),
    )
    evidence_document_fixtures = build_evidence_document_fixture_manifest(
        snapshot_availability_manifest=verification_manifest,
    )
    identity_by_candidate_id, identity_by_fixture_seed_id = _combined_target_identity_maps(
        target_identity_map_path=Path(target_identity_map_path) if target_identity_map_path else None,
        source_backed_fixture_seeds_path=(
            Path(source_backed_fixture_seeds_path) if source_backed_fixture_seeds_path else None
        ),
    )
    claim_replay_tasks = build_claim_replay_task_manifest(
        evidence_document_fixture_manifest=evidence_document_fixtures,
        target_identity_by_candidate_id=identity_by_candidate_id,
        target_identity_by_fixture_seed_id=identity_by_fixture_seed_id,
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "verifier_tasks_json": output_dir / f"{output_prefix}_asof_snapshot_verifier_tasks.json",
        "verifier_tasks_md": output_dir / f"{output_prefix}_asof_snapshot_verifier_tasks.md",
        "run_manifest_json": output_dir / f"{output_prefix}_asof_snapshot_verifier_run_manifest.json",
        "run_manifest_md": output_dir / f"{output_prefix}_asof_snapshot_verifier_run_manifest.md",
        "verifier_rows_json": output_dir / f"{output_prefix}_asof_snapshot_verifier_rows.json",
        "verifier_rows_md": output_dir / f"{output_prefix}_asof_snapshot_verifier_rows.md",
        "result_manifest_json": output_dir / f"{output_prefix}_asof_snapshot_verifier_results_from_run.json",
        "result_manifest_md": output_dir / f"{output_prefix}_asof_snapshot_verifier_results_from_run.md",
        "snapshot_verification_json": output_dir / f"{output_prefix}_asof_snapshot_verification_from_run.json",
        "snapshot_verification_md": output_dir / f"{output_prefix}_asof_snapshot_verification_from_run.md",
        "evidence_document_fixtures_json": output_dir / f"{output_prefix}_asof_evidence_document_fixtures.json",
        "evidence_document_fixtures_md": output_dir / f"{output_prefix}_asof_evidence_document_fixtures.md",
        "claim_replay_tasks_json": output_dir / f"{output_prefix}_asof_claim_replay_tasks.json",
        "claim_replay_tasks_md": output_dir / f"{output_prefix}_asof_claim_replay_tasks.md",
    }
    _write_json(paths["verifier_tasks_json"], verifier_task_manifest)
    _write_json(paths["run_manifest_json"], run_manifest)
    _write_json(paths["verifier_rows_json"], {"rows": verifier_rows})
    _write_json(paths["result_manifest_json"], result_manifest)
    _write_json(paths["snapshot_verification_json"], verification_manifest)
    _write_json(paths["evidence_document_fixtures_json"], evidence_document_fixtures)
    _write_json(paths["claim_replay_tasks_json"], claim_replay_tasks)
    paths["verifier_tasks_md"].write_text(
        _render_summary_markdown("Asof Snapshot Verifier Tasks", verifier_task_manifest),
        encoding="utf-8",
    )
    paths["run_manifest_md"].write_text(
        _render_summary_markdown("Asof Snapshot Verifier Run", run_manifest),
        encoding="utf-8",
    )
    paths["verifier_rows_md"].write_text(_render_rows_markdown(verifier_rows), encoding="utf-8")
    paths["result_manifest_md"].write_text(
        _render_summary_markdown("Asof Snapshot Verifier Results", result_manifest),
        encoding="utf-8",
    )
    paths["snapshot_verification_md"].write_text(
        _render_summary_markdown("Asof Snapshot Verification", verification_manifest),
        encoding="utf-8",
    )
    paths["evidence_document_fixtures_md"].write_text(
        _render_summary_markdown("Asof Evidence Document Fixtures", evidence_document_fixtures),
        encoding="utf-8",
    )
    paths["claim_replay_tasks_md"].write_text(
        _render_summary_markdown("Asof Claim Replay Tasks", claim_replay_tasks),
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
    if not hasattr(verifier, "verify_asof_snapshot_sources"):
        return None
    return verifier


def _build_run_manifest(*, task_manifest: Mapping[str, Any], provider: object | None) -> Mapping[str, Any]:
    tasks = tuple(task for task in task_manifest.get("tasks") or () if isinstance(task, Mapping))
    if provider is None:
        runs = tuple(_run_row_for_task(task, status="provider_not_configured") for task in tasks)
        verifier_rows: tuple[Mapping[str, Any], ...] = ()
    else:
        try:
            output = provider.verify_asof_snapshot_sources(tasks)
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
                by_task = {str(row.get("verifier_task_id") or row.get("task_id") or ""): row for row in verifier_rows}
                runs = tuple(
                    _run_row_for_task(
                        task,
                        status="verifier_output"
                        if str(task.get("verifier_task_id") or "") in by_task
                        else "no_verifier_output",
                    )
                    for task in tasks
                )

    status_counts: dict[str, int] = {}
    for row in runs:
        status = str(row.get("run_status") or "")
        status_counts[status] = status_counts.get(status, 0) + 1
    return {
        "schema_version": "e2r_asof_snapshot_verifier_run_manifest_v1",
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
        "verifier_task_id": str(task.get("verifier_task_id") or ""),
        "acquisition_task_id": str(task.get("acquisition_task_id") or ""),
        "fixture_seed_id": str(task.get("fixture_seed_id") or ""),
        "candidate_id": str(task.get("candidate_id") or ""),
        "source_anchor": str(task.get("source_anchor") or ""),
        "snapshot_url": str(task.get("snapshot_url") or task.get("source_anchor") or ""),
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
    verifier_task_ids: Sequence[str] | None,
    fixture_seed_ids: Sequence[str] | None,
    max_tasks: int | None,
) -> Mapping[str, Any]:
    if max_tasks is not None and max_tasks < 1:
        raise ValueError("max_tasks must be positive when provided")
    requested_task_ids = {str(item).strip() for item in (verifier_task_ids or ()) if str(item).strip()}
    requested_seed_ids = {str(item).strip() for item in (fixture_seed_ids or ()) if str(item).strip()}
    raw_tasks = manifest.get("tasks") or ()
    if not isinstance(raw_tasks, Sequence) or isinstance(raw_tasks, (str, bytes, bytearray)):
        raise ValueError("verifier task manifest tasks must be a sequence")
    tasks: list[Mapping[str, Any]] = []
    for task in raw_tasks:
        if not isinstance(task, Mapping):
            continue
        if task.get("verifier_task_status") not in {
            "ready_for_source_identity_asof_verifier",
            "ready_for_source_metadata_asof_verifier",
        }:
            continue
        task_id = str(task.get("verifier_task_id") or "").strip()
        fixture_seed_id = str(task.get("fixture_seed_id") or "").strip()
        if requested_task_ids and task_id not in requested_task_ids:
            continue
        if requested_seed_ids and fixture_seed_id not in requested_seed_ids:
            continue
        tasks.append(task)
        if max_tasks is not None and len(tasks) >= max_tasks:
            break
    filtered = dict(manifest)
    filtered["tasks"] = tasks
    filtered["verifier_input_filter"] = {
        "verifier_task_ids": sorted(requested_task_ids),
        "fixture_seed_ids": sorted(requested_seed_ids),
        "max_tasks": max_tasks,
        "input_task_count": len(raw_tasks),
        "selected_ready_task_count": len(tasks),
    }
    return filtered


def _combined_target_identity_maps(
    *,
    target_identity_map_path: Path | None,
    source_backed_fixture_seeds_path: Path | None,
) -> tuple[Mapping[str, Mapping[str, Any]], Mapping[str, Mapping[str, Any]]]:
    by_candidate: dict[str, Mapping[str, Any]] = {}
    by_seed: dict[str, Mapping[str, Any]] = {}
    if source_backed_fixture_seeds_path is not None:
        seed_by_candidate, seed_by_seed = _target_identity_maps_from_source_backed_fixture_seeds(
            source_backed_fixture_seeds_path
        )
        by_candidate.update(seed_by_candidate)
        by_seed.update(seed_by_seed)
    if target_identity_map_path is not None:
        explicit_by_candidate, explicit_by_seed = _read_target_identity_maps(target_identity_map_path)
        by_candidate.update(explicit_by_candidate)
        by_seed.update(explicit_by_seed)
    return by_candidate, by_seed


def _read_target_identity_maps(path: Path) -> tuple[Mapping[str, Mapping[str, Any]], Mapping[str, Mapping[str, Any]]]:
    if not path.exists():
        return {}, {}
    data = _read_json_mapping(path)
    by_candidate = data.get("by_candidate_id") or {}
    by_seed = data.get("by_fixture_seed_id") or {}
    if not isinstance(by_candidate, Mapping):
        by_candidate = {}
    if not isinstance(by_seed, Mapping):
        by_seed = {}
    return by_candidate, by_seed


def _target_identity_maps_from_source_backed_fixture_seeds(
    path: Path,
) -> tuple[Mapping[str, Mapping[str, Any]], Mapping[str, Mapping[str, Any]]]:
    if not path.exists():
        return {}, {}
    data = _read_json_mapping(path)
    raw_rows = data.get("seeds") or data.get("rows") or data.get("candidates") or ()
    if not isinstance(raw_rows, Sequence) or isinstance(raw_rows, (str, bytes, bytearray)):
        raise ValueError(f"{path} must contain seeds/rows/candidates")
    by_candidate: dict[str, Mapping[str, Any]] = {}
    by_seed: dict[str, Mapping[str, Any]] = {}
    for row in raw_rows:
        if not isinstance(row, Mapping):
            continue
        identity = _target_identity_from_source_backed_seed(row)
        if identity is None:
            continue
        candidate_id = str(row.get("candidate_id") or "").strip()
        fixture_seed_id = str(row.get("fixture_seed_id") or "").strip()
        if candidate_id:
            by_candidate[candidate_id] = identity
        if fixture_seed_id:
            by_seed[fixture_seed_id] = identity
    return by_candidate, by_seed


def _target_identity_from_source_backed_seed(row: Mapping[str, Any]) -> Mapping[str, Any] | None:
    symbol = str(row.get("symbol") or "").strip()
    company_name = str(row.get("company_name") or "").strip()
    if not symbol and not company_name:
        return None
    target_names = tuple(dict.fromkeys(item for item in (company_name, symbol) if item))
    target_entity_id = f"KRX:{symbol}" if symbol else company_name
    return {
        "target_entity_id": target_entity_id,
        "target_names": target_names,
        "symbol": symbol or None,
        "company_name": company_name or None,
        "identity_source": "source_backed_fixture_seed_manifest",
    }


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
        "Verifier output is not score evidence. It must pass deterministic URL, as-of date, "
        "text hash, EvidenceDocument/EvidenceAnchor, and claim replay gates."
    )
    lines.append("")
    return "\n".join(lines)


def _render_rows_markdown(rows: Sequence[Mapping[str, Any]]) -> str:
    lines = ["# Asof Snapshot Verifier Rows", ""]
    lines.append(f"- row_count: `{len(rows)}`")
    lines.append("")
    lines.append(
        "Rows contain source-identity/as-of observations only. They do not create production score fixtures."
    )
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_asof_snapshot_verifier(
        acquisition_queue_path=args.acquisition_queue,
        current_fetch_status_path=args.current_fetch_status,
        current_text_asof_precheck_path=args.current_text_asof_precheck,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
        run_provider=bool(args.run_provider),
        working_directory=args.working_directory,
        timeout_seconds=args.timeout_seconds,
        reasoning_effort=args.reasoning_effort,
        verifier_task_ids=args.verifier_task_id,
        fixture_seed_ids=args.fixture_seed_id,
        max_tasks=args.max_tasks,
        target_identity_map_path=args.target_identity_map,
        source_backed_fixture_seeds_path=args.source_backed_fixture_seeds,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_ACQUISITION_QUEUE",
    "DEFAULT_CURRENT_FETCH_STATUS",
    "DEFAULT_CURRENT_TEXT_ASOF_PRECHECK",
    "DEFAULT_OUTPUT_DIRECTORY",
    "build_arg_parser",
    "main",
    "run_asof_snapshot_verifier",
]

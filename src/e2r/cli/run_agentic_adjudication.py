"""Run target/temporal adjudication for extracted RawAssertions.

This CLI executes only the adjudication layer. It does not map primitives,
score, or stage anything.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, replace
from datetime import date
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import (
    AdjudicationInput,
    AdjudicationProposal,
    AnchorType,
    CodexCLIAgenticEvidenceProvider,
    EntityRecord,
    EntityRegistry,
    EvidenceAnchor,
    EvidenceDocument,
    SourceType,
    build_adjudication_result_manifest,
    build_default_codex_agentic_evidence_provider_bundle,
    build_primitive_mapping_task_manifest,
    decode_adjudication_proposal,
    decode_claim_extraction_output,
)


DEFAULT_ADJUDICATION_TASKS = (
    "output/0621_agentic_replay/"
    "c01_c36_provider_low_full_live_fetch_replacement_provider_seeded_provider_claim_extraction_adjudication_tasks.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run target/temporal adjudication without primitive mapping or scoring.",
    )
    parser.add_argument("--adjudication-tasks", default=DEFAULT_ADJUDICATION_TASKS)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--output-prefix", default="c01_c36_provider_low_full_live_fetch_replacement_provider_seeded")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--run-provider", action="store_true")
    parser.add_argument("--working-directory", default=None)
    parser.add_argument("--timeout-seconds", type=float, default=None)
    parser.add_argument("--reasoning-effort", default=None)
    parser.add_argument("--task-id", action="append", default=None)
    parser.add_argument("--claim-replay-task-id", action="append", default=None)
    parser.add_argument("--max-tasks", type=int, default=None)
    parser.add_argument(
        "--batch-size",
        type=int,
        default=8,
        help="Maximum adjudication tasks per provider batch call.",
    )
    return parser


def run_adjudication(
    *,
    adjudication_task_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_provider_low_full_live_fetch_replacement_provider_seeded",
    run_provider: bool = False,
    working_directory: str | Path | None = None,
    timeout_seconds: float | None = None,
    reasoning_effort: str | None = None,
    task_ids: Sequence[str] | None = None,
    claim_replay_task_ids: Sequence[str] | None = None,
    max_tasks: int | None = None,
    batch_size: int = 8,
) -> Mapping[str, Path]:
    task_manifest = _filtered_task_manifest(
        _read_json_mapping(Path(adjudication_task_manifest_path)),
        task_ids=task_ids,
        claim_replay_task_ids=claim_replay_task_ids,
        max_tasks=max_tasks,
    )
    provider = _build_provider(
        run_provider=run_provider,
        working_directory=working_directory,
        timeout_seconds=timeout_seconds,
        reasoning_effort=reasoning_effort,
    )
    run_manifest = _build_run_manifest(task_manifest=task_manifest, provider=provider, batch_size=batch_size)
    adjudication_rows = tuple(row for row in run_manifest.get("adjudication_rows") or () if isinstance(row, Mapping))
    adjudication_results = build_adjudication_result_manifest(
        adjudication_task_manifest=task_manifest,
        adjudication_rows=adjudication_rows,
    )
    primitive_mapping_tasks = build_primitive_mapping_task_manifest(
        adjudication_result_manifest=adjudication_results,
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "run_manifest_json": output_dir / f"{output_prefix}_adjudication_run_manifest.json",
        "run_manifest_md": output_dir / f"{output_prefix}_adjudication_run_manifest.md",
        "adjudication_rows_json": output_dir / f"{output_prefix}_adjudication_rows.json",
        "adjudication_rows_md": output_dir / f"{output_prefix}_adjudication_rows.md",
        "adjudication_results_json": output_dir / f"{output_prefix}_adjudication_results_from_run.json",
        "adjudication_results_md": output_dir / f"{output_prefix}_adjudication_results_from_run.md",
        "primitive_mapping_tasks_json": output_dir / f"{output_prefix}_primitive_mapping_tasks_from_adjudication.json",
        "primitive_mapping_tasks_md": output_dir / f"{output_prefix}_primitive_mapping_tasks_from_adjudication.md",
    }
    _write_json(paths["run_manifest_json"], run_manifest)
    _write_json(paths["adjudication_rows_json"], {"rows": adjudication_rows})
    _write_json(paths["adjudication_results_json"], adjudication_results)
    _write_json(paths["primitive_mapping_tasks_json"], primitive_mapping_tasks)
    paths["run_manifest_md"].write_text(_render_summary_markdown("Adjudication Run", run_manifest), encoding="utf-8")
    paths["adjudication_rows_md"].write_text(_render_rows_markdown(adjudication_rows), encoding="utf-8")
    paths["adjudication_results_md"].write_text(
        _render_summary_markdown("Adjudication Results From Run", adjudication_results),
        encoding="utf-8",
    )
    paths["primitive_mapping_tasks_md"].write_text(
        _render_summary_markdown("Primitive Mapping Tasks From Adjudication", primitive_mapping_tasks),
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
    provider = bundle.adjudicator
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
    if not (hasattr(provider, "adjudicate_many") or hasattr(provider, "adjudicate")):
        return None
    return provider


def _build_run_manifest(
    *,
    task_manifest: Mapping[str, Any],
    provider: object | None,
    batch_size: int,
) -> Mapping[str, Any]:
    if batch_size < 1:
        raise ValueError("batch_size must be positive")
    tasks = tuple(task for task in task_manifest.get("tasks") or () if isinstance(task, Mapping))
    runs: list[Mapping[str, Any]] = []
    rows: list[Mapping[str, Any]] = []
    if provider is None:
        runs.extend(_run_row_for_task(task, status="provider_not_configured") for task in tasks)
    else:
        for batch in _batched(tasks, batch_size):
            inputs: list[tuple[Mapping[str, Any], AdjudicationInput]] = []
            for task in batch:
                adjudication_input, error_row = _adjudication_input_for_task(task)
                if error_row is not None:
                    rows.append(error_row)
                    runs.append(_run_row_for_task(task, status="input_error", provider_error=error_row["reason"]))
                    continue
                inputs.append((task, adjudication_input))
            if not inputs:
                continue
            try:
                proposals = _provider_adjudicate(provider, tuple(item[1] for item in inputs))
            except Exception as exc:  # pragma: no cover - defensive CLI boundary
                reason = type(exc).__name__
                for task, _ in inputs:
                    rows.append(_adjudication_error_row(task, reason=reason))
                    runs.append(_run_row_for_task(task, status="provider_error", provider_error=reason))
                continue
            for (task, _), proposal in zip(inputs, proposals):
                row = _adjudication_row_from_output(task, proposal)
                rows.append(row)
                if row.get("ok") is False:
                    runs.append(
                        _run_row_for_task(
                            task,
                            status="provider_error",
                            provider_error=str(row.get("reason") or ""),
                        )
                    )
                else:
                    runs.append(_run_row_for_task(task, status="adjudication_output"))

    status_counts: dict[str, int] = {}
    for row in runs:
        status = str(row.get("run_status") or "")
        status_counts[status] = status_counts.get(status, 0) + 1
    return {
        "schema_version": "e2r_adjudication_run_manifest_v1",
        "source_adjudication_task_schema_version": task_manifest.get("schema_version"),
        "summary": {
            "task_count": len(tasks),
            "llm_called_count": status_counts.get("adjudication_output", 0),
            "provider_not_configured_count": status_counts.get("provider_not_configured", 0),
            "provider_error_count": status_counts.get("provider_error", 0),
            "input_error_count": status_counts.get("input_error", 0),
            "adjudication_output_count": status_counts.get("adjudication_output", 0),
            "adjudication_row_count": len(rows),
            "production_score_fixture_count": 0,
        },
        "run_status_counts": dict(sorted(status_counts.items())),
        "runs": tuple(runs),
        "adjudication_rows": tuple(rows),
    }


def _provider_adjudicate(provider: object, inputs: Sequence[AdjudicationInput]) -> tuple[Any, ...]:
    if hasattr(provider, "adjudicate_many"):
        return tuple(provider.adjudicate_many(inputs))
    return tuple(provider.adjudicate(item) for item in inputs)


def _adjudication_input_for_task(
    task: Mapping[str, Any],
) -> tuple[AdjudicationInput | None, Mapping[str, Any] | None]:
    raw_payload = task.get("raw_assertion")
    if not isinstance(raw_payload, Mapping):
        return None, _adjudication_error_row(task, reason="raw_assertion_missing")
    try:
        raw_assertion = decode_claim_extraction_output(
            {"status": "ok", "blocked_reason": None, "raw_assertions": [raw_payload]}
        ).raw_assertions[0]
    except Exception:
        return None, _adjudication_error_row(task, reason="raw_assertion_decode_failed")
    as_of = _parse_date(task.get("as_of_date"))
    if as_of is None:
        return None, _adjudication_error_row(task, reason="invalid_as_of_date")
    text_path = Path(str(task.get("extracted_text_path") or ""))
    text = text_path.read_text(encoding="utf-8", errors="ignore") if text_path.exists() else raw_assertion.exact_quote
    if not text.strip():
        text = raw_assertion.exact_quote or raw_assertion.object_text
    published_at = _parse_date(task.get("document_published_at")) or as_of
    source_type = _source_type(task.get("source_type"))
    document = EvidenceDocument.from_text(
        text=text,
        canonical_url=str(task.get("canonical_url") or "") or None,
        source_type=source_type,
        source_name=str(task.get("source_name") or source_type.value),
        published_at=published_at,
        available_at=published_at,
        parser_version="adjudication_input_v1",
        source_proxy_only=False,
        score_block_reasons=("adjudication_pending",),
    )
    anchor = EvidenceAnchor(
        anchor_id=str(task.get("anchor_id") or ""),
        document_id=document.document_id,
        anchor_type=AnchorType.TEXT_SPAN,
        locator=str(task.get("anchor_locator") or "char:0:800"),
        exact_text=raw_assertion.exact_quote,
        content_hash=hashlib.sha256(raw_assertion.exact_quote.encode("utf-8")).hexdigest(),
        anchor_verified=raw_assertion.exact_quote in text,
    )
    names = tuple(str(item).strip() for item in (task.get("target_names") or ()) if str(item).strip())
    target_entity_id = str(task.get("target_entity_id") or "").strip()
    legal_name = names[0] if names else target_entity_id
    entity_registry = EntityRegistry(
        entities={
            target_entity_id: EntityRecord(
                entity_id=target_entity_id,
                legal_name=legal_name,
                aliases=tuple(name for name in names[1:] if name != legal_name),
            )
        }
    )
    return (
        AdjudicationInput(
            raw_assertion=raw_assertion,
            document=document,
            anchor=anchor,
            target_entity_id=target_entity_id,
            entity_registry=entity_registry,
            as_of_date=as_of,
        ),
        None,
    )


def _adjudication_row_from_output(task: Mapping[str, Any], output: Any) -> Mapping[str, Any]:
    if isinstance(output, Mapping):
        try:
            output = decode_adjudication_proposal(output)
        except Exception as exc:
            return _adjudication_error_row(
                task,
                reason=f"provider_output_schema_violation:{type(exc).__name__}",
            )
    if isinstance(output, AdjudicationProposal):
        return {
            "task_id": str(task.get("task_id") or ""),
            "ok": True,
            "output": _adjudication_proposal_payload(output),
        }
    return _adjudication_error_row(task, reason="invalid_provider_output")


def _adjudication_proposal_payload(proposal: AdjudicationProposal) -> Mapping[str, Any]:
    payload = asdict(proposal)
    for key in (
        "relation_to_target",
        "directness",
        "target_scope_status",
        "polarity",
        "temporal_status",
        "semantic_status",
        "investigation_status",
    ):
        value = payload.get(key)
        if hasattr(value, "value"):
            payload[key] = value.value
    for key in ("event_date", "effective_start", "effective_end"):
        value = payload.get(key)
        if hasattr(value, "isoformat"):
            payload[key] = value.isoformat()
    return payload


def _adjudication_error_row(task: Mapping[str, Any], *, reason: str) -> Mapping[str, Any]:
    return {
        "task_id": str(task.get("task_id") or ""),
        "ok": False,
        "reason": reason,
    }


def _run_row_for_task(
    task: Mapping[str, Any],
    *,
    status: str,
    provider_error: str | None = None,
) -> Mapping[str, Any]:
    row = {
        "task_id": str(task.get("task_id") or ""),
        "claim_replay_task_id": str(task.get("claim_replay_task_id") or ""),
        "raw_assertion_id": str(task.get("raw_assertion_id") or ""),
        "archetype_id": str(task.get("archetype_id") or ""),
        "target_entity_id": str(task.get("target_entity_id") or ""),
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
    claim_replay_task_ids: Sequence[str] | None,
    max_tasks: int | None,
) -> Mapping[str, Any]:
    if max_tasks is not None and max_tasks < 1:
        raise ValueError("max_tasks must be positive when provided")
    requested_task_ids = {str(item).strip() for item in (task_ids or ()) if str(item).strip()}
    requested_claim_task_ids = {
        str(item).strip() for item in (claim_replay_task_ids or ()) if str(item).strip()
    }
    raw_tasks = manifest.get("tasks") or ()
    if not isinstance(raw_tasks, Sequence) or isinstance(raw_tasks, (str, bytes, bytearray)):
        raise ValueError("adjudication task manifest tasks must be a sequence")
    tasks: list[Mapping[str, Any]] = []
    for task in raw_tasks:
        if not isinstance(task, Mapping):
            continue
        task_id = str(task.get("task_id") or "").strip()
        claim_task_id = str(task.get("claim_replay_task_id") or "").strip()
        if requested_task_ids and task_id not in requested_task_ids:
            continue
        if requested_claim_task_ids and claim_task_id not in requested_claim_task_ids:
            continue
        tasks.append(task)
        if max_tasks is not None and len(tasks) >= max_tasks:
            break
    filtered = dict(manifest)
    filtered["tasks"] = tasks
    filtered["adjudication_input_filter"] = {
        "task_ids": sorted(requested_task_ids),
        "claim_replay_task_ids": sorted(requested_claim_task_ids),
        "max_tasks": max_tasks,
        "input_task_count": len(raw_tasks),
        "selected_task_count": len(tasks),
    }
    return filtered


def _batched(items: Sequence[Mapping[str, Any]], batch_size: int) -> tuple[tuple[Mapping[str, Any], ...], ...]:
    return tuple(tuple(items[index : index + batch_size]) for index in range(0, len(items), batch_size))


def _source_type(value: Any) -> SourceType:
    text = str(value or "").strip()
    try:
        return SourceType(text)
    except ValueError:
        return SourceType.NEWS


def _parse_date(value: Any) -> date | None:
    try:
        return date.fromisoformat(str(value or "").strip()[:10])
    except ValueError:
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
        "Adjudication output is not score evidence until primitive mapping, eligibility checks, "
        "and ScoreContribution construction pass."
    )
    lines.append("")
    return "\n".join(lines)


def _render_rows_markdown(rows: Sequence[Mapping[str, Any]]) -> str:
    lines = ["# Adjudication Rows", ""]
    lines.append(f"- row_count: `{len(rows)}`")
    lines.append("")
    lines.append("Rows contain target/temporal adjudication output only. They do not create production score fixtures.")
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_adjudication(
        adjudication_task_manifest_path=args.adjudication_tasks,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
        run_provider=bool(args.run_provider),
        working_directory=args.working_directory,
        timeout_seconds=args.timeout_seconds,
        reasoning_effort=args.reasoning_effort,
        task_ids=args.task_id,
        claim_replay_task_ids=args.claim_replay_task_id,
        max_tasks=args.max_tasks,
        batch_size=args.batch_size,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_ADJUDICATION_TASKS",
    "DEFAULT_OUTPUT_DIRECTORY",
    "build_arg_parser",
    "main",
    "run_adjudication",
]

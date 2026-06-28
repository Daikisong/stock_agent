"""Run primitive mapping for adjudicated source-backed claims.

This CLI executes only the primitive mapping layer. It does not decide score
eligibility, score contributions, or Stage.
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
    AdjudicatedClaim,
    AnchorType,
    CodexCLIAgenticEvidenceProvider,
    Directness,
    EvidenceAnchor,
    EvidenceDocument,
    GateOperator,
    InvestigationStatus,
    MappingStatus,
    Polarity,
    PrimitiveMappingInput,
    PrimitiveMappingOutput,
    PrimitiveMappingProposal,
    RelationToTarget,
    SemanticStatus,
    SourceType,
    TargetScopeStatus,
    TemporalStatus,
    VerificationStatus,
    build_default_codex_agentic_evidence_provider_bundle,
    build_eligibility_task_manifest,
    build_primitive_mapping_result_manifest,
    decode_claim_extraction_output,
    decode_primitive_mapping_output,
    load_evidence_contracts_v2,
    validate_primitive_mappings,
)


DEFAULT_PRIMITIVE_MAPPING_TASKS = (
    "output/0621_agentic_replay/"
    "c01_c36_provider_low_full_live_fetch_replacement_provider_seeded_extracted_provider_gated_primitive_mapping_tasks.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run primitive mapping without score eligibility, scoring, or staging.",
    )
    parser.add_argument("--primitive-mapping-tasks", default=DEFAULT_PRIMITIVE_MAPPING_TASKS)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--output-prefix", default="c01_c36_provider_low_full_live_fetch_replacement_provider_seeded")
    parser.add_argument("--evidence-contracts-v2", default=None)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--run-provider", action="store_true")
    parser.add_argument("--working-directory", default=None)
    parser.add_argument("--timeout-seconds", type=float, default=None)
    parser.add_argument("--reasoning-effort", default=None)
    parser.add_argument("--task-id", action="append", default=None)
    parser.add_argument("--candidate-id", action="append", default=None)
    parser.add_argument("--archetype-id", action="append", default=None)
    parser.add_argument("--max-tasks", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=8)
    return parser


def run_primitive_mapping(
    *,
    primitive_mapping_task_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_provider_low_full_live_fetch_replacement_provider_seeded",
    evidence_contracts_v2_path: str | Path | None = None,
    run_provider: bool = False,
    working_directory: str | Path | None = None,
    timeout_seconds: float | None = None,
    reasoning_effort: str | None = None,
    task_ids: Sequence[str] | None = None,
    candidate_ids: Sequence[str] | None = None,
    archetype_ids: Sequence[str] | None = None,
    max_tasks: int | None = None,
    batch_size: int = 8,
) -> Mapping[str, Path]:
    task_manifest = _filtered_task_manifest(
        _read_json_mapping(Path(primitive_mapping_task_manifest_path)),
        task_ids=task_ids,
        candidate_ids=candidate_ids,
        archetype_ids=archetype_ids,
        max_tasks=max_tasks,
    )
    contracts = load_evidence_contracts_v2(path=evidence_contracts_v2_path)
    canonical_registry = _canonical_primitive_registry(contracts)
    provider = _build_provider(
        run_provider=run_provider,
        working_directory=working_directory,
        timeout_seconds=timeout_seconds,
        reasoning_effort=reasoning_effort,
    )
    run_manifest = _build_run_manifest(
        task_manifest=task_manifest,
        contracts=contracts,
        canonical_registry=canonical_registry,
        provider=provider,
        batch_size=batch_size,
    )
    mapping_rows = tuple(row for row in run_manifest.get("primitive_mapping_rows") or () if isinstance(row, Mapping))
    mapping_results = build_primitive_mapping_result_manifest(
        primitive_mapping_task_manifest=task_manifest,
        mapping_rows=mapping_rows,
        canonical_primitive_ids_by_archetype=canonical_registry,
    )
    eligibility_tasks = build_eligibility_task_manifest(
        primitive_mapping_result_manifest=mapping_results,
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "run_manifest_json": output_dir / f"{output_prefix}_primitive_mapping_run_manifest.json",
        "run_manifest_md": output_dir / f"{output_prefix}_primitive_mapping_run_manifest.md",
        "primitive_mapping_rows_json": output_dir / f"{output_prefix}_primitive_mapping_rows.json",
        "primitive_mapping_rows_md": output_dir / f"{output_prefix}_primitive_mapping_rows.md",
        "primitive_mapping_results_json": output_dir / f"{output_prefix}_primitive_mapping_results_from_run.json",
        "primitive_mapping_results_md": output_dir / f"{output_prefix}_primitive_mapping_results_from_run.md",
        "eligibility_tasks_json": output_dir / f"{output_prefix}_eligibility_tasks_from_mapping.json",
        "eligibility_tasks_md": output_dir / f"{output_prefix}_eligibility_tasks_from_mapping.md",
    }
    _write_json(paths["run_manifest_json"], run_manifest)
    _write_json(paths["primitive_mapping_rows_json"], {"rows": mapping_rows})
    _write_json(paths["primitive_mapping_results_json"], mapping_results)
    _write_json(paths["eligibility_tasks_json"], eligibility_tasks)
    paths["run_manifest_md"].write_text(_render_summary_markdown("Primitive Mapping Run", run_manifest), encoding="utf-8")
    paths["primitive_mapping_rows_md"].write_text(_render_rows_markdown(mapping_rows), encoding="utf-8")
    paths["primitive_mapping_results_md"].write_text(
        _render_summary_markdown("Primitive Mapping Results From Run", mapping_results),
        encoding="utf-8",
    )
    paths["eligibility_tasks_md"].write_text(
        _render_summary_markdown("Eligibility Tasks From Mapping", eligibility_tasks),
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
    provider = bundle.mapper
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
    if not (hasattr(provider, "map_many") or hasattr(provider, "map")):
        return None
    return provider


def _build_run_manifest(
    *,
    task_manifest: Mapping[str, Any],
    contracts: Mapping[str, Any],
    canonical_registry: Mapping[str, Sequence[str]],
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
        for batch in _batched_by_archetype(tasks, batch_size):
            inputs: list[tuple[Mapping[str, Any], PrimitiveMappingInput]] = []
            for task in batch:
                mapping_input, error_row = _primitive_mapping_input_for_task(
                    task,
                    contracts=contracts,
                    canonical_registry=canonical_registry,
                )
                if error_row is not None:
                    rows.append(error_row)
                    runs.append(_run_row_for_task(task, status="input_error", provider_error=error_row["reason"]))
                    continue
                inputs.append((task, mapping_input))
            if not inputs:
                continue
            try:
                output = _provider_map(provider, tuple(item[1] for item in inputs))
            except Exception as exc:  # pragma: no cover - defensive CLI boundary
                reason = type(exc).__name__
                for task, _ in inputs:
                    rows.append(_mapping_error_row(task, reason=reason))
                    runs.append(_run_row_for_task(task, status="provider_error", provider_error=reason))
                continue
            task_rows = _mapping_rows_from_batch(inputs, output)
            rows.extend(task_rows)
            row_by_task = {str(row.get("task_id") or ""): row for row in task_rows}
            for task, _ in inputs:
                row = row_by_task.get(str(task.get("task_id") or ""))
                if row is None:
                    runs.append(_run_row_for_task(task, status="provider_error", provider_error="missing_mapping_row"))
                elif row.get("ok") is False:
                    runs.append(_run_row_for_task(task, status="provider_error", provider_error=str(row.get("reason") or "")))
                else:
                    runs.append(_run_row_for_task(task, status="primitive_mapping_output"))

    status_counts: dict[str, int] = {}
    for row in runs:
        status = str(row.get("run_status") or "")
        status_counts[status] = status_counts.get(status, 0) + 1
    return {
        "schema_version": "e2r_primitive_mapping_run_manifest_v1",
        "source_primitive_mapping_task_schema_version": task_manifest.get("schema_version"),
        "summary": {
            "task_count": len(tasks),
            "llm_called_count": status_counts.get("primitive_mapping_output", 0),
            "provider_not_configured_count": status_counts.get("provider_not_configured", 0),
            "provider_error_count": status_counts.get("provider_error", 0),
            "input_error_count": status_counts.get("input_error", 0),
            "primitive_mapping_output_count": status_counts.get("primitive_mapping_output", 0),
            "primitive_mapping_row_count": len(rows),
            "archetype_batch_count": len(_batched_by_archetype(tasks, batch_size)),
            "production_score_fixture_count": 0,
        },
        "run_status_counts": dict(sorted(status_counts.items())),
        "runs": tuple(runs),
        "primitive_mapping_rows": tuple(rows),
    }


def _primitive_mapping_input_for_task(
    task: Mapping[str, Any],
    *,
    contracts: Mapping[str, Any],
    canonical_registry: Mapping[str, Sequence[str]],
) -> tuple[PrimitiveMappingInput | None, Mapping[str, Any] | None]:
    archetype_id = str(task.get("archetype_id") or "").strip()
    contract = contracts.get(archetype_id)
    if contract is None:
        return None, _mapping_error_row(task, reason="evidence_contract_missing_for_archetype")
    raw_payload = task.get("raw_assertion")
    if not isinstance(raw_payload, Mapping):
        return None, _mapping_error_row(task, reason="raw_assertion_missing")
    try:
        raw_assertion = decode_claim_extraction_output(
            {"status": "ok", "blocked_reason": None, "raw_assertions": [raw_payload]}
        ).raw_assertions[0]
    except Exception:
        return None, _mapping_error_row(task, reason="raw_assertion_decode_failed")
    document_id = str(task.get("document_id") or "").strip()
    if not document_id:
        return None, _mapping_error_row(task, reason="document_id_missing")
    content_hash = str(task.get("content_hash") or "").strip() or hashlib.sha256(document_id.encode("utf-8")).hexdigest()
    published_at = _parse_date(task.get("document_published_at")) or _parse_date(task.get("as_of_date"))
    source_type = _source_type(task.get("source_type"))
    document = EvidenceDocument(
        document_id=document_id,
        canonical_url=str(task.get("canonical_url") or "") or None,
        source_type=source_type,
        source_name=str(task.get("source_name") or source_type.value),
        content_hash=content_hash,
        published_at=published_at,
        available_at=published_at,
        parser_version="primitive_mapping_input_v1",
        source_proxy_only=False,
        score_block_reasons=("primitive_mapping_pending",),
    )
    exact_text = raw_assertion.exact_quote or raw_assertion.object_text
    anchor = EvidenceAnchor(
        anchor_id=str(task.get("anchor_id") or raw_assertion.anchor_id),
        document_id=document.document_id,
        anchor_type=AnchorType.TEXT_SPAN,
        locator=str(task.get("anchor_locator") or raw_assertion.anchor_id),
        exact_text=exact_text,
        content_hash=hashlib.sha256(exact_text.encode("utf-8")).hexdigest() if exact_text else None,
        anchor_verified=bool(exact_text),
    )
    claim = AdjudicatedClaim.from_raw(
        raw=raw_assertion,
        document=document,
        anchor=anchor,
        subject_entity_id=str(task.get("subject_entity_id") or "").strip(),
        target_entity_id=str(task.get("target_entity_id") or "").strip(),
        relation_to_target=_enum_value(RelationToTarget, task.get("relation_to_target"), RelationToTarget.UNKNOWN),
        directness=_enum_value(Directness, task.get("directness"), Directness.UNKNOWN),
        verification_status=VerificationStatus.SEMANTIC_VERIFIED,
        target_scope_status=_enum_value(TargetScopeStatus, task.get("target_scope_status"), TargetScopeStatus.UNKNOWN),
        polarity=_enum_value(Polarity, task.get("polarity"), Polarity.CONDITIONAL),
        temporal_status=_enum_value(TemporalStatus, task.get("temporal_status"), TemporalStatus.UNKNOWN),
        semantic_status=_enum_value(SemanticStatus, task.get("semantic_status"), SemanticStatus.UNVERIFIED),
        investigation_status=_enum_value(
            InvestigationStatus,
            task.get("investigation_status"),
            InvestigationStatus.FOLLOWUP_REQUIRED,
        ),
        event_date=_parse_date(task.get("event_date")),
        effective_start=_parse_date(task.get("effective_start")),
        effective_end=_parse_date(task.get("effective_end")),
    )
    expected_claim_id = str(task.get("claim_id") or "").strip()
    if expected_claim_id and expected_claim_id != claim.claim_id:
        return None, _mapping_error_row(task, reason="claim_id_reconstruction_mismatch")
    primitive_ids = tuple(str(item).strip() for item in canonical_registry.get(archetype_id, ()) if str(item).strip())
    if not primitive_ids:
        return None, _mapping_error_row(task, reason="canonical_primitive_registry_missing_for_archetype")
    return (
        PrimitiveMappingInput(
            claim=claim,
            contract=contract,
            canonical_primitive_ids=primitive_ids,
            raw_assertion=raw_assertion,
            anchor=anchor,
        ),
        None,
    )


def _provider_map(provider: object, inputs: Sequence[PrimitiveMappingInput]) -> PrimitiveMappingOutput:
    if hasattr(provider, "map_many"):
        output = provider.map_many(inputs)
    else:
        mappings: list[PrimitiveMappingProposal] = []
        for item in inputs:
            single = provider.map(item)
            single_output = decode_primitive_mapping_output(single) if isinstance(single, Mapping) else single
            if isinstance(single_output, PrimitiveMappingOutput):
                mappings.extend(single_output.mappings)
        return PrimitiveMappingOutput(tuple(mappings))
    if isinstance(output, Mapping):
        return decode_primitive_mapping_output(output)
    if isinstance(output, PrimitiveMappingOutput):
        return output
    raise ValueError("invalid primitive mapper output")


def _mapping_rows_from_batch(
    inputs: Sequence[tuple[Mapping[str, Any], PrimitiveMappingInput]],
    output: PrimitiveMappingOutput,
) -> tuple[Mapping[str, Any], ...]:
    by_claim: dict[str, list[PrimitiveMappingProposal]] = {}
    task_claims = {item.claim.claim_id for _, item in inputs}
    unmatched: list[PrimitiveMappingProposal] = []
    for mapping in output.mappings:
        if mapping.claim_id in task_claims:
            by_claim.setdefault(mapping.claim_id, []).append(mapping)
        else:
            unmatched.append(mapping)
    rows: list[Mapping[str, Any]] = []
    for index, (task, mapping_input) in enumerate(inputs):
        mappings = tuple(by_claim.get(mapping_input.claim.claim_id, ()))
        if index == 0 and unmatched:
            mappings = (*mappings, *unmatched)
        if not mappings:
            rows.append(_mapping_error_row(task, reason="primitive_mapping_missing_for_claim"))
            continue
        rows.append(
            {
                "task_id": str(task.get("task_id") or ""),
                "ok": True,
                "mappings": tuple(
                    _primitive_mapping_payload(mapping)
                    for mapping in _deterministically_validated_mappings(mapping_input, mappings)
                ),
            }
        )
    return tuple(rows)


def _deterministically_validated_mappings(
    mapping_input: PrimitiveMappingInput,
    mappings: Sequence[PrimitiveMappingProposal],
) -> tuple[PrimitiveMappingProposal, ...]:
    accepted: list[PrimitiveMappingProposal] = []
    for mapping in mappings:
        if mapping.mapping_status != MappingStatus.ACCEPTED:
            accepted.append(mapping)
            continue
        try:
            validated = validate_primitive_mappings(mapping_input, PrimitiveMappingOutput((mapping,)))
        except ValueError:
            accepted.append(mapping)
            continue
        if validated.mappings:
            accepted.extend(validated.mappings)
        else:
            accepted.append(
                PrimitiveMappingProposal.build(
                    claim_id=mapping.claim_id,
                    archetype_id=mapping.archetype_id,
                    primitive_id=mapping.primitive_id,
                    support_direction=mapping.support_direction,
                    mapping_status=MappingStatus.REJECTED,
                    rationale="deterministic_mapping_validation_rejected",
                    contract_rule_id=mapping.contract_rule_id,
                    counter_primitive_ids=mapping.counter_primitive_ids,
                )
            )
    return tuple(accepted)


def _canonical_primitive_registry(contracts: Mapping[str, Any]) -> Mapping[str, Sequence[str]]:
    return {
        archetype_id: _canonical_primitive_ids(contract)
        for archetype_id, contract in contracts.items()
    }


def _canonical_primitive_ids(contract: Any) -> tuple[str, ...]:
    ids: list[str] = []
    ids.extend(getattr(contract, "required_primitives", ()) or ())
    for key, values in (getattr(contract, "alternative_primitives", {}) or {}).items():
        ids.append(str(key))
        ids.extend(str(item) for item in values)
    for key in (getattr(contract, "primitive_aliases", {}) or {}):
        ids.append(str(key))
    ids.extend((getattr(contract, "freshness", {}) or {}).keys())
    ids.extend((getattr(contract, "guard_modes", {}) or {}).keys())
    ids.extend(_gate_primitive_ids(getattr(contract, "green_gate", None)))
    return tuple(dict.fromkeys(str(item).strip() for item in ids if str(item).strip()))


def _gate_primitive_ids(gate: Any) -> tuple[str, ...]:
    if gate is None:
        return ()
    if getattr(gate, "operator", None) == GateOperator.PRIMITIVE:
        primitive_id = str(getattr(gate, "primitive_id", "") or "").strip()
        return (primitive_id,) if primitive_id else ()
    result: list[str] = []
    for child in getattr(gate, "children", ()) or ():
        result.extend(_gate_primitive_ids(child))
    return tuple(result)


def _primitive_mapping_payload(mapping: PrimitiveMappingProposal) -> Mapping[str, Any]:
    payload = asdict(mapping)
    for key in ("support_direction", "mapping_status"):
        value = payload.get(key)
        if hasattr(value, "value"):
            payload[key] = value.value
    return payload


def _mapping_error_row(task: Mapping[str, Any], *, reason: str) -> Mapping[str, Any]:
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
        "claim_id": str(task.get("claim_id") or ""),
        "adjudication_task_id": str(task.get("adjudication_task_id") or ""),
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
    candidate_ids: Sequence[str] | None,
    archetype_ids: Sequence[str] | None,
    max_tasks: int | None,
) -> Mapping[str, Any]:
    if max_tasks is not None and max_tasks < 1:
        raise ValueError("max_tasks must be positive when provided")
    requested_task_ids = {str(item).strip() for item in (task_ids or ()) if str(item).strip()}
    requested_candidate_ids = {str(item).strip() for item in (candidate_ids or ()) if str(item).strip()}
    requested_archetype_ids = {str(item).strip() for item in (archetype_ids or ()) if str(item).strip()}
    raw_tasks = manifest.get("tasks") or ()
    if not isinstance(raw_tasks, Sequence) or isinstance(raw_tasks, (str, bytes, bytearray)):
        raise ValueError("primitive mapping task manifest tasks must be a sequence")
    tasks: list[Mapping[str, Any]] = []
    for task in raw_tasks:
        if not isinstance(task, Mapping):
            continue
        task_id = str(task.get("task_id") or "").strip()
        candidate_id = str(task.get("candidate_id") or "").strip()
        archetype_id = str(task.get("archetype_id") or "").strip()
        if requested_task_ids and task_id not in requested_task_ids:
            continue
        if requested_candidate_ids and candidate_id not in requested_candidate_ids:
            continue
        if requested_archetype_ids and archetype_id not in requested_archetype_ids:
            continue
        tasks.append(task)
        if max_tasks is not None and len(tasks) >= max_tasks:
            break
    filtered = dict(manifest)
    filtered["tasks"] = tasks
    filtered["primitive_mapping_input_filter"] = {
        "task_ids": sorted(requested_task_ids),
        "candidate_ids": sorted(requested_candidate_ids),
        "archetype_ids": sorted(requested_archetype_ids),
        "max_tasks": max_tasks,
        "input_task_count": len(raw_tasks),
        "selected_task_count": len(tasks),
    }
    return filtered


def _batched_by_archetype(
    tasks: Sequence[Mapping[str, Any]],
    batch_size: int,
) -> tuple[tuple[Mapping[str, Any], ...], ...]:
    grouped: dict[str, list[Mapping[str, Any]]] = {}
    for task in tasks:
        grouped.setdefault(str(task.get("archetype_id") or ""), []).append(task)
    batches: list[tuple[Mapping[str, Any], ...]] = []
    for group in grouped.values():
        for index in range(0, len(group), batch_size):
            batches.append(tuple(group[index : index + batch_size]))
    return tuple(batches)


def _source_type(value: Any) -> SourceType:
    text = str(value or "").strip()
    try:
        return SourceType(text)
    except ValueError:
        return SourceType.NEWS


def _enum_value(enum_cls: Any, value: Any, default: Any) -> Any:
    try:
        return enum_cls(str(value or "").strip())
    except ValueError:
        return default


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
    lines.append("Primitive mapping output is not score evidence until eligibility and ScoreContribution checks pass.")
    lines.append("")
    return "\n".join(lines)


def _render_rows_markdown(rows: Sequence[Mapping[str, Any]]) -> str:
    lines = ["# Primitive Mapping Rows", ""]
    lines.append(f"- row_count: `{len(rows)}`")
    lines.append("")
    lines.append("Rows contain primitive mapping output only. They do not create production score fixtures.")
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_primitive_mapping(
        primitive_mapping_task_manifest_path=args.primitive_mapping_tasks,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
        evidence_contracts_v2_path=args.evidence_contracts_v2,
        run_provider=bool(args.run_provider),
        working_directory=args.working_directory,
        timeout_seconds=args.timeout_seconds,
        reasoning_effort=args.reasoning_effort,
        task_ids=args.task_id,
        candidate_ids=args.candidate_id,
        archetype_ids=args.archetype_id,
        max_tasks=args.max_tasks,
        batch_size=args.batch_size,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_OUTPUT_DIRECTORY",
    "DEFAULT_PRIMITIVE_MAPPING_TASKS",
    "build_arg_parser",
    "main",
    "run_primitive_mapping",
]

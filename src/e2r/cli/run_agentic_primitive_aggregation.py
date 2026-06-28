"""Aggregate score-eligible mappings into PrimitiveStateV2 rows.

This CLI is deterministic. It does not create scores or stages.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import (
    MappingStatus,
    PrimitiveMappingProposal,
    PrimitiveStateV2,
    PrimitiveStatus,
    SupportDirection,
    load_evidence_contracts_v2,
)


DEFAULT_ELIGIBILITY_TASKS = (
    "output/0621_agentic_replay/"
    "c01_c36_provider_low_full_live_fetch_replacement_provider_seeded_v2_extracted_provider_gated_pmap_provider_v2_"
    "eligibility_tasks_from_mapping.json"
)
DEFAULT_ELIGIBILITY_RESULTS = (
    "output/0621_agentic_replay/"
    "c01_c36_provider_low_full_live_fetch_replacement_provider_seeded_v2_extracted_provider_gated_pmap_provider_v2_"
    "eligibility_eligibility_results_from_run.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Aggregate eligible primitive mappings before score contribution construction.",
    )
    parser.add_argument("--eligibility-tasks", default=DEFAULT_ELIGIBILITY_TASKS)
    parser.add_argument("--eligibility-results", default=DEFAULT_ELIGIBILITY_RESULTS)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument("--output-prefix", default="c01_c36_provider_low_full_live_fetch_replacement_provider_seeded")
    parser.add_argument("--evidence-contracts-v2", default=None)
    parser.add_argument("--candidate-id", action="append", default=None)
    parser.add_argument("--archetype-id", action="append", default=None)
    parser.add_argument("--max-groups", type=int, default=None)
    return parser


def run_primitive_aggregation(
    *,
    eligibility_task_manifest_path: str | Path,
    eligibility_result_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_provider_low_full_live_fetch_replacement_provider_seeded",
    evidence_contracts_v2_path: str | Path | None = None,
    candidate_ids: Sequence[str] | None = None,
    archetype_ids: Sequence[str] | None = None,
    max_groups: int | None = None,
) -> Mapping[str, Path]:
    task_manifest = _read_json_mapping(Path(eligibility_task_manifest_path))
    result_manifest = _read_json_mapping(Path(eligibility_result_manifest_path))
    contracts = load_evidence_contracts_v2(path=evidence_contracts_v2_path)
    primitive_state_manifest = build_primitive_state_manifest(
        eligibility_task_manifest=task_manifest,
        eligibility_result_manifest=result_manifest,
        contracts=contracts,
        candidate_ids=candidate_ids,
        archetype_ids=archetype_ids,
        max_groups=max_groups,
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "primitive_state_manifest_json": output_dir / f"{output_prefix}_primitive_state_manifest.json",
        "primitive_state_manifest_md": output_dir / f"{output_prefix}_primitive_state_manifest.md",
    }
    _write_json(paths["primitive_state_manifest_json"], primitive_state_manifest)
    paths["primitive_state_manifest_md"].write_text(
        _render_summary_markdown("Primitive State Manifest", primitive_state_manifest),
        encoding="utf-8",
    )
    return paths


def build_primitive_state_manifest(
    *,
    eligibility_task_manifest: Mapping[str, Any],
    eligibility_result_manifest: Mapping[str, Any],
    contracts: Mapping[str, Any],
    candidate_ids: Sequence[str] | None = None,
    archetype_ids: Sequence[str] | None = None,
    max_groups: int | None = None,
) -> Mapping[str, Any]:
    requested_candidate_ids = {str(item).strip() for item in (candidate_ids or ()) if str(item).strip()}
    requested_archetype_ids = {str(item).strip() for item in (archetype_ids or ()) if str(item).strip()}
    if max_groups is not None and max_groups < 1:
        raise ValueError("max_groups must be positive when provided")

    tasks_by_id = {
        str(task.get("task_id") or ""): task
        for task in eligibility_task_manifest.get("tasks") or ()
        if isinstance(task, Mapping)
    }
    ready_rows: list[tuple[Mapping[str, Any], Mapping[str, Any]]] = []
    skipped_results: list[Mapping[str, Any]] = []
    for result in eligibility_result_manifest.get("results") or ():
        if not isinstance(result, Mapping):
            continue
        if result.get("result_status") != "score_contribution_ready" or not _optional_bool(result.get("eligibility_ready")):
            skipped_results.append(_skip_row(result, "eligibility_not_ready"))
            continue
        task_id = str(result.get("eligibility_task_id") or "").strip()
        task = tasks_by_id.get(task_id)
        if task is None:
            skipped_results.append(_skip_row(result, "eligibility_task_missing"))
            continue
        candidate_id = str(task.get("candidate_id") or "").strip()
        archetype_id = str(task.get("archetype_id") or "").strip()
        if requested_candidate_ids and candidate_id not in requested_candidate_ids:
            continue
        if requested_archetype_ids and archetype_id not in requested_archetype_ids:
            continue
        ready_rows.append((task, result))

    grouped: dict[tuple[str, str, str, str, str], list[tuple[Mapping[str, Any], Mapping[str, Any]]]] = {}
    for task, result in ready_rows:
        key = (
            str(task.get("fixture_seed_id") or ""),
            str(task.get("candidate_id") or ""),
            str(task.get("archetype_id") or ""),
            str(task.get("target_entity_id") or ""),
            str(task.get("as_of_date") or ""),
        )
        grouped.setdefault(key, []).append((task, result))

    groups: list[Mapping[str, Any]] = []
    for key, rows in sorted(grouped.items()):
        if max_groups is not None and len(groups) >= max_groups:
            break
        groups.append(_primitive_state_group(key, rows, contracts=contracts))

    all_states = [state for group in groups for state in group.get("primitive_states", ())]
    source_input_count = sum(int(group.get("source_family_input_count") or 0) for group in groups)
    source_unique_count = sum(int(group.get("source_family_unique_count") or 0) for group in groups)
    return {
        "schema_version": "e2r_primitive_state_manifest_v1",
        "source_eligibility_task_schema_version": eligibility_task_manifest.get("schema_version"),
        "source_eligibility_result_schema_version": eligibility_result_manifest.get("schema_version"),
        "summary": {
            "group_count": len(groups),
            "primitive_state_count": len(all_states),
            "present_current_count": sum(1 for state in all_states if state.get("status") == PrimitiveStatus.PRESENT_CURRENT.value),
            "contradicted_count": sum(1 for state in all_states if state.get("status") == PrimitiveStatus.CONTRADICTED.value),
            "unknown_count": sum(1 for state in all_states if state.get("status") == PrimitiveStatus.UNKNOWN.value),
            "absent_explicitly_confirmed_count": sum(
                1 for state in all_states if state.get("status") == PrimitiveStatus.ABSENT_EXPLICITLY_CONFIRMED.value
            ),
            "eligibility_ready_input_count": len(ready_rows),
            "skipped_result_count": len(skipped_results),
            "source_family_input_count": source_input_count,
            "source_family_unique_count": source_unique_count,
            "duplicate_source_family_collapsed_count": max(source_input_count - source_unique_count, 0),
            "score_blocked_until_score_contribution": True,
            "production_score_fixture_count": 0,
        },
        "input_filter": {
            "candidate_ids": sorted(requested_candidate_ids),
            "archetype_ids": sorted(requested_archetype_ids),
            "max_groups": max_groups,
        },
        "groups": groups,
        "skipped_results": skipped_results,
    }


def _primitive_state_group(
    key: tuple[str, str, str, str, str],
    rows: Sequence[tuple[Mapping[str, Any], Mapping[str, Any]]],
    *,
    contracts: Mapping[str, Any],
) -> Mapping[str, Any]:
    fixture_seed_id, candidate_id, archetype_id, target_entity_id, as_of_date = key
    contract = contracts.get(archetype_id)
    primitive_ids = set(_contract_primitive_ids(contract)) if contract is not None else set()
    for task, _result in rows:
        primitive_id = str(task.get("primitive_id") or "").strip()
        if primitive_id:
            primitive_ids.add(primitive_id)

    evidence_by_primitive: dict[str, list[Mapping[str, Any]]] = {}
    for task, result in rows:
        primitive_id = str(task.get("primitive_id") or "").strip()
        if not primitive_id:
            continue
        evidence_by_primitive.setdefault(primitive_id, []).append(_evidence_row(task, result))

    states: list[Mapping[str, Any]] = []
    source_inputs = 0
    source_uniques: set[str] = set()
    for primitive_id in sorted(primitive_ids):
        evidence_rows = evidence_by_primitive.get(primitive_id, [])
        state = _primitive_state_row(primitive_id, evidence_rows)
        states.append(state)
        source_inputs += len(evidence_rows)
        source_uniques.update(state.get("support_source_family_ids") or ())
        source_uniques.update(state.get("counter_source_family_ids") or ())

    return {
        "group_id": _group_id(key),
        "fixture_seed_id": fixture_seed_id,
        "candidate_id": candidate_id,
        "archetype_id": archetype_id,
        "target_entity_id": target_entity_id,
        "as_of_date": as_of_date,
        "primitive_state_count": len(states),
        "present_current_count": sum(1 for state in states if state.get("status") == PrimitiveStatus.PRESENT_CURRENT.value),
        "source_family_input_count": source_inputs,
        "source_family_unique_count": len(source_uniques),
        "duplicate_source_family_collapsed_count": max(source_inputs - len(source_uniques), 0),
        "score_blocked_until_score_contribution": True,
        "production_score_fixture": False,
        "primitive_states": states,
    }


def _primitive_state_row(primitive_id: str, evidence_rows: Sequence[Mapping[str, Any]]) -> Mapping[str, Any]:
    support = [row for row in evidence_rows if row.get("support_direction") == SupportDirection.SUPPORT.value]
    counter = [row for row in evidence_rows if row.get("support_direction") == SupportDirection.COUNTER.value]
    support_claim_ids = tuple(sorted({str(row.get("claim_id") or "") for row in support if row.get("claim_id")}))
    counter_claim_ids = tuple(sorted({str(row.get("claim_id") or "") for row in counter if row.get("claim_id")}))
    support_mapping_ids = tuple(sorted({str(row.get("mapping_id") or "") for row in support if row.get("mapping_id")}))
    counter_mapping_ids = tuple(sorted({str(row.get("mapping_id") or "") for row in counter if row.get("mapping_id")}))
    support_sources = tuple(sorted({str(row.get("source_family_id") or "") for row in support if row.get("source_family_id")}))
    counter_sources = tuple(sorted({str(row.get("source_family_id") or "") for row in counter if row.get("source_family_id")}))
    freshness_values = [
        int(row["freshness_days"])
        for row in evidence_rows
        if isinstance(row.get("freshness_days"), int)
    ]
    if support_claim_ids and counter_claim_ids:
        status = PrimitiveStatus.CONTRADICTED
    elif support_claim_ids:
        status = PrimitiveStatus.PRESENT_CURRENT
    elif counter_claim_ids:
        status = PrimitiveStatus.ABSENT_EXPLICITLY_CONFIRMED
    else:
        status = PrimitiveStatus.UNKNOWN
    state = PrimitiveStateV2(
        primitive_id=primitive_id,
        status=status,
        support_claim_ids=support_claim_ids,
        counter_claim_ids=counter_claim_ids,
        support_source_family_ids=support_sources,
        counter_source_family_ids=counter_sources,
        freshness_days=min(freshness_values) if freshness_values else None,
        support_mapping_ids=support_mapping_ids,
        counter_mapping_ids=counter_mapping_ids,
    )
    return {
        "primitive_id": state.primitive_id,
        "status": state.status.value,
        "support_claim_ids": state.support_claim_ids,
        "counter_claim_ids": state.counter_claim_ids,
        "support_mapping_ids": state.support_mapping_ids,
        "counter_mapping_ids": state.counter_mapping_ids,
        "support_source_family_ids": state.support_source_family_ids,
        "counter_source_family_ids": state.counter_source_family_ids,
        "freshness_days": state.freshness_days,
        "source_family_input_count": len(evidence_rows),
        "source_family_unique_count": len(set(support_sources) | set(counter_sources)),
        "duplicate_source_family_collapsed_count": max(len(evidence_rows) - len(set(support_sources) | set(counter_sources)), 0),
    }


def _evidence_row(task: Mapping[str, Any], result: Mapping[str, Any]) -> Mapping[str, Any]:
    claim_id = str(task.get("claim_id") or result.get("claim_id") or "").strip()
    archetype_id = str(task.get("archetype_id") or "").strip()
    primitive_id = str(task.get("primitive_id") or "").strip()
    support_direction = str(task.get("support_direction") or "").strip()
    event_date = _date_text(task.get("event_date") or task.get("document_published_at"))
    as_of_date = _date_text(task.get("as_of_date"))
    return {
        "claim_id": claim_id,
        "mapping_id": _mapping_id(
            claim_id=claim_id,
            archetype_id=archetype_id,
            primitive_id=primitive_id,
            support_direction=support_direction,
        ),
        "source_family_id": _source_family_id(task),
        "support_direction": support_direction,
        "freshness_days": _freshness_days(event_date=event_date, as_of_date=as_of_date),
    }


def _contract_primitive_ids(contract: Any) -> tuple[str, ...]:
    if contract is None:
        return ()
    ids: list[str] = []
    ids.extend(getattr(contract, "required_primitives", ()) or ())
    ids.extend(getattr(getattr(contract, "green_gate", None), "primitive_ids", lambda: ())())
    for key, values in (getattr(contract, "alternative_primitives", {}) or {}).items():
        ids.append(str(key))
        ids.extend(str(item) for item in values)
    for values in (getattr(contract, "score_rubric", {}) or {}).values():
        ids.extend(str(item) for item in values)
    ids.extend((getattr(contract, "guard_modes", {}) or {}).keys())
    return tuple(dict.fromkeys(str(item).strip() for item in ids if str(item).strip()))


def _source_family_id(task: Mapping[str, Any]) -> str:
    source_lineage = str(task.get("source_lineage_id") or "").strip()
    if source_lineage:
        return source_lineage
    original_anchor = str(task.get("original_source_anchor") or "").strip()
    if original_anchor:
        return "ORIG-" + hashlib.sha1(original_anchor.encode("utf-8")).hexdigest()[:20]
    document_id = str(task.get("document_id") or "").strip()
    if document_id:
        return document_id
    canonical_url = str(task.get("canonical_url") or "").strip()
    if canonical_url:
        return "URL-" + hashlib.sha1(canonical_url.encode("utf-8")).hexdigest()[:20]
    return "SOURCE-UNKNOWN"


def _mapping_id(*, claim_id: str, archetype_id: str, primitive_id: str, support_direction: str) -> str:
    try:
        direction = SupportDirection(support_direction)
    except ValueError:
        direction = SupportDirection.NEUTRAL
    return PrimitiveMappingProposal.build(
        claim_id=claim_id,
        archetype_id=archetype_id,
        primitive_id=primitive_id,
        support_direction=direction,
        mapping_status=MappingStatus.ACCEPTED,
        rationale="primitive aggregation id reconstruction",
    ).mapping_id


def _freshness_days(*, event_date: str | None, as_of_date: str | None) -> int | None:
    if not event_date or not as_of_date:
        return None
    try:
        from datetime import date

        event = date.fromisoformat(event_date[:10])
        as_of = date.fromisoformat(as_of_date[:10])
    except ValueError:
        return None
    return max((as_of - event).days, 0)


def _date_text(value: Any) -> str | None:
    text = str(value or "").strip()
    return text[:10] if text else None


def _skip_row(result: Mapping[str, Any], reason: str) -> Mapping[str, Any]:
    return {
        "eligibility_result_id": str(result.get("task_id") or ""),
        "eligibility_task_id": str(result.get("eligibility_task_id") or ""),
        "primitive_id": str(result.get("primitive_id") or ""),
        "result_status": str(result.get("result_status") or ""),
        "skip_reason": reason,
        "production_score_fixture": False,
    }


def _group_id(key: Sequence[str]) -> str:
    return "PSTATE-" + hashlib.sha1("|".join(key).encode("utf-8")).hexdigest()[:20]


def _optional_bool(value: Any) -> bool | None:
    if isinstance(value, bool):
        return value
    if value is None:
        return None
    text = str(value).strip().lower()
    if text in {"true", "1", "yes", "y"}:
        return True
    if text in {"false", "0", "no", "n"}:
        return False
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
    lines.append("Primitive states are not scores. ScoreContribution construction remains blocked after this step.")
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_primitive_aggregation(
        eligibility_task_manifest_path=args.eligibility_tasks,
        eligibility_result_manifest_path=args.eligibility_results,
        output_directory=args.output_directory,
        output_prefix=args.output_prefix,
        evidence_contracts_v2_path=args.evidence_contracts_v2,
        candidate_ids=args.candidate_id,
        archetype_ids=args.archetype_id,
        max_groups=args.max_groups,
    )
    for name, path in paths.items():
        print(f"{name}={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = [
    "DEFAULT_ELIGIBILITY_RESULTS",
    "DEFAULT_ELIGIBILITY_TASKS",
    "DEFAULT_OUTPUT_DIRECTORY",
    "build_arg_parser",
    "build_primitive_state_manifest",
    "main",
    "run_primitive_aggregation",
]

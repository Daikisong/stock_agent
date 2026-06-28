"""Build deterministic ScoreContributionV2 rows from PrimitiveStateV2 manifests."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import PrimitiveStateV2, PrimitiveStatus, load_evidence_contracts_v2
from e2r.agentic.score_contribution_ledger import (
    DEFAULT_SCORE_COMPONENT_MAX_POINTS,
    build_component_score_contributions_from_rubric,
)


DEFAULT_PRIMITIVE_STATE_MANIFEST = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v12_primitive_state_manifest.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build claim/mapping/source-backed ScoreContributionV2 rows from aggregated primitive states.",
    )
    parser.add_argument("--primitive-state-manifest", default=DEFAULT_PRIMITIVE_STATE_MANIFEST)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument(
        "--output-prefix",
        default="c01_c36_combined_replacement_metadata_asof_source_recovery_v12",
    )
    parser.add_argument("--evidence-contracts-v2", default=None)
    parser.add_argument("--candidate-id", action="append", default=None)
    parser.add_argument("--archetype-id", action="append", default=None)
    parser.add_argument("--max-groups", type=int, default=None)
    return parser


def run_score_contribution(
    *,
    primitive_state_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_combined_replacement_metadata_asof_source_recovery_v12",
    evidence_contracts_v2_path: str | Path | None = None,
    candidate_ids: Sequence[str] | None = None,
    archetype_ids: Sequence[str] | None = None,
    max_groups: int | None = None,
) -> Mapping[str, Path]:
    primitive_state_manifest = _read_json_mapping(Path(primitive_state_manifest_path))
    contracts = load_evidence_contracts_v2(path=evidence_contracts_v2_path)
    result_manifest = build_score_contribution_manifest(
        primitive_state_manifest=primitive_state_manifest,
        contracts=contracts,
        candidate_ids=candidate_ids,
        archetype_ids=archetype_ids,
        max_groups=max_groups,
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "score_contribution_results_json": output_dir / f"{output_prefix}_score_contribution_results.json",
        "score_contribution_results_md": output_dir / f"{output_prefix}_score_contribution_results.md",
    }
    _write_json(paths["score_contribution_results_json"], result_manifest)
    paths["score_contribution_results_md"].write_text(
        _render_summary_markdown("Score Contribution Results", result_manifest),
        encoding="utf-8",
    )
    return paths


def build_score_contribution_manifest(
    *,
    primitive_state_manifest: Mapping[str, Any],
    contracts: Mapping[str, Any],
    candidate_ids: Sequence[str] | None = None,
    archetype_ids: Sequence[str] | None = None,
    max_groups: int | None = None,
) -> Mapping[str, Any]:
    requested_candidate_ids = {str(item).strip() for item in (candidate_ids or ()) if str(item).strip()}
    requested_archetype_ids = {str(item).strip() for item in (archetype_ids or ()) if str(item).strip()}
    if max_groups is not None and max_groups < 1:
        raise ValueError("max_groups must be positive when provided")

    results: list[Mapping[str, Any]] = []
    skipped_groups: list[Mapping[str, Any]] = []
    processed_group_count = 0
    for group in primitive_state_manifest.get("groups") or ():
        if not isinstance(group, Mapping):
            continue
        candidate_id = str(group.get("candidate_id") or "").strip()
        archetype_id = str(group.get("archetype_id") or "").strip()
        if requested_candidate_ids and candidate_id not in requested_candidate_ids:
            continue
        if requested_archetype_ids and archetype_id not in requested_archetype_ids:
            continue
        if max_groups is not None and processed_group_count >= max_groups:
            break
        processed_group_count += 1
        contract = contracts.get(archetype_id)
        if contract is None:
            skipped_groups.append(_skip_group(group, "evidence_contract_missing"))
            continue
        if not getattr(contract, "score_rubric", None):
            skipped_groups.append(_skip_group(group, "score_rubric_empty"))
            continue
        primitive_states = _primitive_states_from_group(group)
        contributions = build_component_score_contributions_from_rubric(
            components=_components_for_rubric(contract.score_rubric),
            primitive_states=primitive_states,
            score_rubric=contract.score_rubric,
            component_max_points=DEFAULT_SCORE_COMPONENT_MAX_POINTS,
        )
        for contribution in contributions:
            primitive_ids = tuple(
                dict.fromkeys(
                    str(item).strip()
                    for item in contract.score_rubric.get(contribution.component_key, ())
                    if str(item).strip()
                )
            )
            results.append(
                _result_row(
                    group=group,
                    contribution=contribution,
                    primitive_ids=primitive_ids,
                    primitive_state_rows=tuple(group.get("primitive_states") or ()),
                )
            )

    by_status: dict[str, int] = {}
    for result in results:
        status = str(result.get("result_status") or "")
        by_status[status] = by_status.get(status, 0) + 1
    nonzero_results = [row for row in results if float(row.get("raw_points") or 0.0) > 0.0]
    return {
        "schema_version": "e2r_score_contribution_result_manifest_v1",
        "source_primitive_state_schema_version": primitive_state_manifest.get("schema_version"),
        "summary": {
            "group_count": processed_group_count,
            "skipped_group_count": len(skipped_groups),
            "task_count": len(results),
            "score_contribution_ready_count": sum(1 for result in results if result.get("score_contribution_ready")),
            "nonzero_score_contribution_count": len(nonzero_results),
            "zero_score_contribution_count": len(results) - len(nonzero_results),
            "orphan_score_blocked_count": sum(
                1
                for row in nonzero_results
                if not row.get("support_claim_ids") or not row.get("mapping_ids") or not row.get("source_family_ids")
            ),
            "score_blocked_task_count": sum(1 for result in results if result.get("score_blocked_until_score_snapshot")),
            "production_score_fixture_count": sum(1 for result in results if result.get("production_score_fixture")),
        },
        "result_status_counts": dict(sorted(by_status.items())),
        "input_filter": {
            "candidate_ids": sorted(requested_candidate_ids),
            "archetype_ids": sorted(requested_archetype_ids),
            "max_groups": max_groups,
        },
        "results": results,
        "skipped_groups": skipped_groups,
    }


def _primitive_states_from_group(group: Mapping[str, Any]) -> Mapping[str, PrimitiveStateV2]:
    states: dict[str, PrimitiveStateV2] = {}
    for row in group.get("primitive_states") or ():
        if not isinstance(row, Mapping):
            continue
        primitive_id = str(row.get("primitive_id") or "").strip()
        if not primitive_id:
            continue
        try:
            status = PrimitiveStatus(str(row.get("status") or "UNKNOWN"))
        except ValueError:
            status = PrimitiveStatus.UNKNOWN
        states[primitive_id] = PrimitiveStateV2(
            primitive_id=primitive_id,
            status=status,
            support_claim_ids=_text_tuple(row.get("support_claim_ids")),
            counter_claim_ids=_text_tuple(row.get("counter_claim_ids")),
            support_source_family_ids=_text_tuple(row.get("support_source_family_ids")),
            counter_source_family_ids=_text_tuple(row.get("counter_source_family_ids")),
            freshness_days=_optional_int(row.get("freshness_days")),
            support_mapping_ids=_text_tuple(row.get("support_mapping_ids")),
            counter_mapping_ids=_text_tuple(row.get("counter_mapping_ids")),
        )
    return states


def _components_for_rubric(score_rubric: Mapping[str, Sequence[str]]) -> Mapping[str, float]:
    return {
        str(component_key): float(DEFAULT_SCORE_COMPONENT_MAX_POINTS.get(str(component_key), 0.0))
        for component_key in score_rubric
    }


def _result_row(
    *,
    group: Mapping[str, Any],
    contribution: Any,
    primitive_ids: Sequence[str],
    primitive_state_rows: Sequence[Any],
) -> Mapping[str, Any]:
    task_id = _score_contribution_result_id(
        group_id=str(group.get("group_id") or ""),
        component_key=contribution.component_key,
        criterion_id=contribution.criterion_id,
        contribution_id=contribution.contribution_id,
    )
    return {
        "task_id": task_id,
        "score_contribution_task_id": task_id.replace("SCRES-", "SCTASK-", 1),
        "fixture_seed_id": str(group.get("fixture_seed_id") or ""),
        "candidate_id": str(group.get("candidate_id") or ""),
        "archetype_id": str(group.get("archetype_id") or ""),
        "target_entity_id": str(group.get("target_entity_id") or ""),
        "as_of_date": str(group.get("as_of_date") or ""),
        "result_status": "score_contribution_ready",
        "contribution_source": "deterministic_primitive_state_rubric",
        "component_key": contribution.component_key,
        "criterion_id": contribution.criterion_id,
        "raw_points": contribution.raw_points,
        "max_points": contribution.max_points,
        "contribution_id": contribution.contribution_id,
        "support_claim_ids": contribution.support_claim_ids,
        "counter_claim_ids": contribution.counter_claim_ids,
        "mapping_ids": contribution.mapping_ids,
        "source_family_ids": contribution.source_family_ids,
        "cap_reason": contribution.cap_reason,
        "rationale": contribution.rationale,
        "primitive_id": primitive_ids[0] if len(primitive_ids) == 1 else None,
        "primitive_ids": tuple(primitive_ids),
        "present_primitive_ids": _present_primitive_ids(primitive_state_rows, primitive_ids=primitive_ids),
        "primitive_states": tuple(
            row
            for row in primitive_state_rows
            if isinstance(row, Mapping) and str(row.get("primitive_id") or "") in set(primitive_ids)
        ),
        "score_contribution_ready": True,
        "score_blocked_until_score_snapshot": True,
        "production_score_fixture": False,
        "reasons": ("score_contribution_v2_built_from_primitive_state_manifest",),
    }


def _present_primitive_ids(primitive_state_rows: Sequence[Any], *, primitive_ids: Sequence[str]) -> tuple[str, ...]:
    allowed = set(primitive_ids)
    present: list[str] = []
    for row in primitive_state_rows:
        if not isinstance(row, Mapping):
            continue
        primitive_id = str(row.get("primitive_id") or "").strip()
        if primitive_id not in allowed:
            continue
        if row.get("status") == PrimitiveStatus.PRESENT_CURRENT.value and _text_tuple(row.get("support_claim_ids")):
            present.append(primitive_id)
    return tuple(dict.fromkeys(present))


def _score_contribution_result_id(
    *,
    group_id: str,
    component_key: str,
    criterion_id: str,
    contribution_id: str,
) -> str:
    return "SCRES-" + hashlib.sha1(
        "|".join((group_id, component_key, criterion_id, contribution_id)).encode("utf-8")
    ).hexdigest()[:20]


def _skip_group(group: Mapping[str, Any], reason: str) -> Mapping[str, Any]:
    return {
        "group_id": str(group.get("group_id") or ""),
        "fixture_seed_id": str(group.get("fixture_seed_id") or ""),
        "candidate_id": str(group.get("candidate_id") or ""),
        "archetype_id": str(group.get("archetype_id") or ""),
        "target_entity_id": str(group.get("target_entity_id") or ""),
        "skip_reason": reason,
        "production_score_fixture": False,
    }


def _text_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        return (value,) if value else ()
    if isinstance(value, Sequence) and not isinstance(value, (bytes, bytearray)):
        return tuple(str(item).strip() for item in value if str(item).strip())
    return (str(value),)


def _optional_int(value: Any) -> int | None:
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
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
    lines.append("ScoreContribution rows are deterministic, but still blocked until ScoreSnapshot and StageCourt pass.")
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_score_contribution(
        primitive_state_manifest_path=args.primitive_state_manifest,
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
    "DEFAULT_OUTPUT_DIRECTORY",
    "DEFAULT_PRIMITIVE_STATE_MANIFEST",
    "build_arg_parser",
    "build_score_contribution_manifest",
    "main",
    "run_score_contribution",
]

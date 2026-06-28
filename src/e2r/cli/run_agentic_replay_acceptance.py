"""Summarise C01-C36 replay coverage for the Evidence OS preview chain."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.agentic import load_evidence_contracts_v2
from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS


DEFAULT_PRIMITIVE_STATE_MANIFEST = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v12_primitive_state_manifest.json"
)
DEFAULT_STAGE_COURT_RESULTS = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v12_stage_court_results.json"
)
DEFAULT_CHAIN_AUDIT = (
    "output/0621_agentic_replay/"
    "c01_c36_combined_replacement_metadata_asof_source_recovery_v12_chain_audit.json"
)
DEFAULT_OUTPUT_DIRECTORY = "output/0621_agentic_replay"


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build C01-C36 Evidence OS replay coverage acceptance manifest.")
    parser.add_argument("--primitive-state-manifest", default=DEFAULT_PRIMITIVE_STATE_MANIFEST)
    parser.add_argument("--stage-court-results", default=DEFAULT_STAGE_COURT_RESULTS)
    parser.add_argument("--chain-audit", default=DEFAULT_CHAIN_AUDIT)
    parser.add_argument("--evidence-contracts-v2", default=None)
    parser.add_argument("--output-directory", default=DEFAULT_OUTPUT_DIRECTORY)
    parser.add_argument(
        "--output-prefix",
        default="c01_c36_combined_replacement_metadata_asof_source_recovery_v13_replay_acceptance",
    )
    return parser


def run_replay_acceptance(
    *,
    primitive_state_manifest_path: str | Path,
    stage_court_result_manifest_path: str | Path,
    chain_audit_manifest_path: str | Path,
    output_directory: str | Path,
    output_prefix: str = "c01_c36_combined_replacement_metadata_asof_source_recovery_v13_replay_acceptance",
    evidence_contracts_v2_path: str | Path | None = None,
) -> Mapping[str, Path]:
    primitive_state_manifest = _read_json_mapping(Path(primitive_state_manifest_path))
    stage_court_results = _read_json_mapping(Path(stage_court_result_manifest_path))
    chain_audit = _read_json_mapping(Path(chain_audit_manifest_path))
    contracts = load_evidence_contracts_v2(path=evidence_contracts_v2_path)
    manifest = build_replay_acceptance_manifest(
        primitive_state_manifest=primitive_state_manifest,
        stage_court_result_manifest=stage_court_results,
        chain_audit_manifest=chain_audit,
        contracts=contracts,
    )

    output_dir = Path(output_directory)
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "acceptance_json": output_dir / f"{output_prefix}_acceptance.json",
        "acceptance_md": output_dir / f"{output_prefix}_acceptance.md",
    }
    _write_json(paths["acceptance_json"], manifest)
    paths["acceptance_md"].write_text(_render_acceptance_markdown(manifest), encoding="utf-8")
    return paths


def build_replay_acceptance_manifest(
    *,
    primitive_state_manifest: Mapping[str, Any],
    stage_court_result_manifest: Mapping[str, Any],
    chain_audit_manifest: Mapping[str, Any],
    contracts: Mapping[str, Any],
) -> Mapping[str, Any]:
    groups_by_archetype: dict[str, list[Mapping[str, Any]]] = {}
    for group in primitive_state_manifest.get("groups") or ():
        if isinstance(group, Mapping):
            archetype_id = str(group.get("archetype_id") or "")
            groups_by_archetype.setdefault(archetype_id, []).append(group)
    stage_by_archetype: dict[str, list[Mapping[str, Any]]] = {}
    for row in stage_court_result_manifest.get("results") or ():
        if isinstance(row, Mapping):
            archetype_id = str(row.get("archetype_id") or "")
            stage_by_archetype.setdefault(archetype_id, []).append(row)

    rows: list[Mapping[str, Any]] = []
    for archetype_id in CANONICAL_ARCHETYPE_IDS:
        contract_present = archetype_id in contracts
        groups = groups_by_archetype.get(archetype_id, [])
        stage_rows = stage_by_archetype.get(archetype_id, [])
        ready_stage_rows = [
            row for row in stage_rows if row.get("result_status") == "stage_court_ready" and row.get("stage_court_ready")
        ]
        if not contract_present:
            status = "evidence_contract_missing"
        elif ready_stage_rows:
            status = "stage_preview_ready"
        elif groups:
            status = "primitive_state_present_stage_not_ready"
        else:
            status = "unsupported_source_gap"
        rows.append(
            {
                "archetype_id": archetype_id,
                "coverage_status": status,
                "contract_present": contract_present,
                "primitive_group_count": len(groups),
                "stage_court_ready_count": len(ready_stage_rows),
                "production_score_fixture": False,
                "production_stage_fixture": False,
            }
        )

    status_counts: dict[str, int] = {}
    for row in rows:
        status = str(row.get("coverage_status") or "")
        status_counts[status] = status_counts.get(status, 0) + 1
    chain_summary = chain_audit_manifest.get("summary") if isinstance(chain_audit_manifest.get("summary"), Mapping) else {}
    stage_ready_count = status_counts.get("stage_preview_ready", 0)
    unsupported_count = status_counts.get("unsupported_source_gap", 0)
    present_not_ready_count = status_counts.get("primitive_state_present_stage_not_ready", 0)
    missing_contract_count = status_counts.get("evidence_contract_missing", 0)
    canonical_archetype_ids = tuple(CANONICAL_ARCHETYPE_IDS)
    contract_ids = tuple(str(archetype_id) for archetype_id in contracts)
    missing_contract_ids = tuple(archetype_id for archetype_id in canonical_archetype_ids if archetype_id not in contracts)
    extra_contract_ids = tuple(sorted(set(contract_ids) - set(canonical_archetype_ids)))
    contract_schema_all_archetypes_ready = not missing_contract_ids and not extra_contract_ids
    chain_ready = _chain_ready(chain_summary)
    replay_acceptance_ready = (
        bool(rows)
        and chain_ready
        and stage_ready_count == len(rows)
        and unsupported_count == 0
        and present_not_ready_count == 0
        and missing_contract_count == 0
    )
    return {
        "schema_version": "e2r_replay_acceptance_manifest_v1",
        "source_primitive_state_schema_version": primitive_state_manifest.get("schema_version"),
        "source_stage_court_schema_version": stage_court_result_manifest.get("schema_version"),
        "source_chain_audit_schema_version": chain_audit_manifest.get("schema_version"),
        "summary": {
            "archetype_count": len(rows),
            "canonical_archetype_count": len(canonical_archetype_ids),
            "contract_count": len(contracts),
            "contract_schema_all_archetypes_ready": contract_schema_all_archetypes_ready,
            "contract_missing_archetype_count": len(missing_contract_ids),
            "contract_extra_archetype_count": len(extra_contract_ids),
            "contract_missing_archetype_ids": list(missing_contract_ids),
            "contract_extra_archetype_ids": list(extra_contract_ids),
            "stage_preview_ready_count": stage_ready_count,
            "unsupported_source_gap_count": unsupported_count,
            "primitive_state_present_stage_not_ready_count": present_not_ready_count,
            "evidence_contract_missing_count": missing_contract_count,
            "replay_acceptance_ready": replay_acceptance_ready,
            "production_cutover_ready": replay_acceptance_ready,
            "chain_status": chain_summary.get("chain_status"),
            "chain_evidence_os_ready": chain_ready,
            "chain_production_cutover_ready": chain_summary.get("production_cutover_ready"),
            "production_score_fixture_total": chain_summary.get("production_score_fixture_total", 0),
            "production_stage_fixture_total": chain_summary.get("production_stage_fixture_total", 0),
        },
        "coverage_status_counts": dict(sorted(status_counts.items())),
        "rows": rows,
    }


def _read_json_mapping(path: Path) -> Mapping[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, Mapping):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def _chain_ready(chain_summary: Mapping[str, Any]) -> bool:
    if chain_summary.get("evidence_os_chain_ready") is True:
        return True
    return (
        chain_summary.get("chain_status") == "stage_preview_ready_not_production_cutover"
        and _int_or_zero(chain_summary.get("stage_court_ready_count")) > 0
        and _int_or_zero(chain_summary.get("production_score_fixture_total")) == 0
        and _int_or_zero(chain_summary.get("production_stage_fixture_total")) == 0
    )


def _int_or_zero(value: Any) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def _write_json(path: Path, data: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def _render_acceptance_markdown(manifest: Mapping[str, Any]) -> str:
    lines = ["# Evidence OS Replay Acceptance", ""]
    summary = manifest.get("summary")
    if isinstance(summary, Mapping):
        lines.append("## Summary")
        for key in sorted(summary):
            lines.append(f"- {key}: `{summary[key]}`")
        lines.append("")
    lines.append("## Coverage")
    for row in manifest.get("rows") or ():
        if not isinstance(row, Mapping):
            continue
        lines.append(f"- `{row.get('archetype_id')}`: `{row.get('coverage_status')}`")
    lines.append("")
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    paths = run_replay_acceptance(
        primitive_state_manifest_path=args.primitive_state_manifest,
        stage_court_result_manifest_path=args.stage_court_results,
        chain_audit_manifest_path=args.chain_audit,
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
    "DEFAULT_CHAIN_AUDIT",
    "DEFAULT_OUTPUT_DIRECTORY",
    "DEFAULT_PRIMITIVE_STATE_MANIFEST",
    "DEFAULT_STAGE_COURT_RESULTS",
    "build_arg_parser",
    "build_replay_acceptance_manifest",
    "main",
    "run_replay_acceptance",
]

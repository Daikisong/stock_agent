from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Any

from e2r.agentic.evidence_contract_v2 import load_evidence_contracts_v2
from e2r.census.census_runner_v4 import CensusV4RunConfig, run_census_mode_v4
from tests.census_v3_test_helpers import census_v3_artifacts


_CACHE: dict[str, Any] | None = None
_SUPPORT_TEMP_DIR: tempfile.TemporaryDirectory[str] | None = None
_SUPPORT_PATHS: dict[str, str] | None = None


def census_v4_artifacts() -> dict[str, Any]:
    global _CACHE
    if _CACHE is None:
        support = census_v4_test_support_kwargs()
        output_root = Path(_support_root()) / "census_v4"
        result = run_census_mode_v4(
            CensusV4RunConfig(
                as_of_date="2026-07-01",
                output_root=str(output_root),
                fail_on_critical_audit=True,
                write_operational_docs=False,
                test_result_summary="unit_test_cached_run",
                full_thesis_smoke_mode="controlled_replay",
                **support,
            )
        )
        _CACHE = {
            "result": result,
            "output_root": output_root,
            "leaf_audit": read_json(output_root / "leaf_artifact_audit.json"),
            "artifact_manifest": read_json(output_root / "artifact_manifest.json"),
            "stage_summary": read_json(output_root / "census_stage_summary.json"),
            "stage_rows": read_jsonl(output_root / "census_stage_status.jsonl"),
            "sample_rows": read_jsonl(output_root / "sample_leaf_bundle.jsonl"),
            "atomic_rows": read_jsonl(output_root / "atomic_stage_decisions.jsonl"),
            "readiness": read_json(output_root / "readiness_verdict.json"),
        }
    return _CACHE


def census_v3_output_root() -> Path:
    return Path(census_v3_artifacts()["output_root"])


def census_v4_test_support_kwargs() -> dict[str, Any]:
    global _SUPPORT_PATHS
    if _SUPPORT_PATHS is None:
        root = Path(_support_root())
        manifest_path = root / "all_archetype_source_backed_replay_manifest.json"
        replay_path = root / "all_archetype_replay_acceptance.json"
        adversarial_path = root / "all_archetype_adversarial_acceptance.json"
        _write_all_archetype_test_acceptance(
            manifest_path=manifest_path,
            replay_path=replay_path,
            adversarial_path=adversarial_path,
        )
        _SUPPORT_PATHS = {
            "v3_output_root": str(census_v3_output_root()),
            "test_mode": True,
            "test_all_archetype_source_backed_replay_manifest_path": str(manifest_path),
            "test_all_archetype_replay_acceptance_path": str(replay_path),
            "test_all_archetype_adversarial_acceptance_path": str(adversarial_path),
        }
    return dict(_SUPPORT_PATHS)


def _support_root() -> str:
    global _SUPPORT_TEMP_DIR
    if _SUPPORT_TEMP_DIR is None:
        _SUPPORT_TEMP_DIR = tempfile.TemporaryDirectory()
    return _SUPPORT_TEMP_DIR.name


def _write_all_archetype_test_acceptance(
    *,
    manifest_path: Path,
    replay_path: Path,
    adversarial_path: Path,
) -> None:
    archetype_ids = tuple(load_evidence_contracts_v2(require_all_archetypes=True))
    candidates: list[dict[str, Any]] = []
    archetype_rows: list[dict[str, Any]] = []
    for archetype_id in archetype_ids:
        candidate_ids = [f"RPLAY-TEST-{archetype_id[:3]}-{index}" for index in range(3)]
        archetype_rows.append(
            {
                "archetype_id": archetype_id,
                "selected_candidate_count": 3,
                "selected_candidate_ids": candidate_ids,
                "fixture_ready_candidate_count": 3,
                "unique_fixture_ready_candidate_count": 3,
            }
        )
        candidates.extend(
            {
                "candidate_id": candidate_id,
                "archetype_id": archetype_id,
                "source_anchors": [f"https://example.test/replay/{archetype_id}/{index}"],
                "selection_reasons": ["concrete_source_anchor"],
                "production_score_fixture": False,
                "production_stage_fixture": False,
            }
            for index, candidate_id in enumerate(candidate_ids)
        )
    write_json(
        manifest_path,
        {
            "schema_version": "e2r_source_backed_replay_manifest_v1",
            "contract_count": len(archetype_ids),
            "archetype_rows": archetype_rows,
            "candidates": candidates,
            "summary": {
                "selected_candidate_count": len(candidates),
                "unique_fixture_ready_candidate_count": len(candidates),
                "production_score_fixture_count": 0,
            },
        },
    )
    replay_rows = [
        {
            "archetype_id": archetype_id,
            "contract_present": True,
            "coverage_status": "stage_preview_ready",
            "primitive_group_count": 1,
            "stage_court_ready_count": 1,
            "production_score_fixture": False,
            "production_stage_fixture": False,
        }
        for archetype_id in archetype_ids
    ]
    write_json(
        replay_path,
        {
            "schema_version": "e2r_replay_acceptance_manifest_v1",
            "rows": replay_rows,
            "summary": {
                "archetype_count": len(archetype_ids),
                "stage_preview_ready_count": len(archetype_ids),
                "unsupported_source_gap_count": 0,
                "replay_acceptance_ready": True,
            },
        },
    )
    adversarial_rows = [
        {
            "case_id": f"ADVERSARIAL-TEST-{index:02d}",
            "adversarial_case_ready": True,
            "production_score_fixture": False,
            "production_stage_fixture": False,
        }
        for index in range(24)
    ]
    write_json(
        adversarial_path,
        {
            "schema_version": "e2r_adversarial_acceptance_manifest_v1",
            "rows": adversarial_rows,
            "summary": {
                "case_count": len(adversarial_rows),
                "named_regression_covered_count": len(adversarial_rows),
                "missing_representative_test_count": 0,
                "adversarial_acceptance_ready": True,
                "production_cutover_ready": True,
            },
        },
    )


def by_symbol(rows: list[dict[str, Any]], symbol: str) -> dict[str, Any]:
    for row in rows:
        if row.get("symbol") == symbol:
            return row
    raise AssertionError(f"symbol not found: {symbol}")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if text:
                rows.append(json.loads(text))
    return rows

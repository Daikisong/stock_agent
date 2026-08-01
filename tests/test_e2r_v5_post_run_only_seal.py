from __future__ import annotations

import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from typing import Mapping
from unittest.mock import Mock, patch

from e2r.cli.run_e2r_researcher_mode_until_pass import main
from e2r.production.metadata import stable_hash
from e2r.research_brain.researcher_mode.current_researcher_mode import (
    CurrentResearcherModeConfig,
    load_current_research_target_registry,
    load_current_research_targets,
)
from e2r.research_brain.researcher_mode.canary_leaf_contract import (
    canary_output_tree_hash,
)
from e2r.research_brain.researcher_mode.full_thesis_gold_benchmark import (
    PHASE93_POST_RUN_PASS,
)
from e2r.research_brain.researcher_mode.sealed_production import (
    assert_frozen_production_unchanged,
    build_current_production_semantics,
    make_production_semantics_seal,
    verify_sealed_production,
)


AS_OF_DATE = "2026-06-29"
ARCHETYPE = "CURRENT-ARCHETYPE"
TARGET_IDS = ("CURRENT-A", "CURRENT-B")


class E2RV5PostRunOnlySealTests(unittest.TestCase):
    def test_production_fingerprint_does_not_read_post_run_gold_code(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = _write_registry(root)
            rows = load_current_research_target_registry(registry)
            targets = load_current_research_targets(
                symbols=TARGET_IDS,
                registry_path=registry,
                registry_rows=rows,
                as_of_date=AS_OF_DATE,
            )
            config = CurrentResearcherModeConfig(
                as_of_date=AS_OF_DATE,
                archetype_id=ARCHETYPE,
                output_root=root,
                live_materialization_authorized=True,
                checkpoint_resume=True,
                gold_lane_isolated=True,
                require_researcher_parity=True,
                latest_trading_snapshot_date=AS_OF_DATE,
            )
            original = Path.read_bytes

            def guarded(path: Path) -> bytes:
                if path.name in {
                    "full_thesis_gold_benchmark.py",
                    "blind_benchmark.py",
                }:
                    raise AssertionError("production fingerprint read Gold code")
                return original(path)

            with patch.object(Path, "read_bytes", guarded):
                semantics = build_current_production_semantics(
                    config=config,
                    targets=targets,
                    registry_rows=rows,
                    target_registry_path=registry,
                    provider_manifest={"provider_name": "TEST"},
                    repo_root=Path.cwd(),
                )
            self.assertTrue(semantics["code_fingerprint"])

    def test_valid_seal_hashes_all_production_files_and_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            expected = _example_semantics()
            _write_valid_sealed_lane(root, expected=expected)

            verification = verify_sealed_production(
                output_root=root,
                target_ids=TARGET_IDS,
                as_of_date=AS_OF_DATE,
                archetype_id=ARCHETYPE,
                expected_semantics=expected,
            )

            self.assertTrue(verification.eligible, verification.reasons)
            self.assertEqual(len(verification.frozen_file_sha256), 12)
            _write_json(root / "post_run_gold_recall_audit.json", {"status": "PASS"})
            for target_id in TARGET_IDS:
                _write_jsonl(
                    root / target_id / "gold_fact_comparison.jsonl",
                    ({"target_id": target_id},),
                )
            assert_frozen_production_unchanged(
                output_root=root,
                verification=verification,
            )

    def test_post_run_mutation_of_frozen_stagecourt_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            expected = _example_semantics()
            _write_valid_sealed_lane(root, expected=expected)
            verification = verify_sealed_production(
                output_root=root,
                target_ids=TARGET_IDS,
                as_of_date=AS_OF_DATE,
                archetype_id=ARCHETYPE,
                expected_semantics=expected,
            )
            trace_path = root / TARGET_IDS[0] / "stagecourt_trace.json"
            trace = json.loads(trace_path.read_text(encoding="utf-8"))
            trace["decision"]["canonical_stage"] = "3-Green"
            _write_json(trace_path, trace)

            with self.assertRaisesRegex(RuntimeError, "stagecourt_trace.json"):
                assert_frozen_production_unchanged(
                    output_root=root,
                    verification=verification,
                )

    def test_current_manifest_tree_binding_rejects_nonfrozen_input_tamper(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            expected = _example_semantics()
            _write_valid_sealed_lane(root, expected=expected)
            _write_json(
                root / TARGET_IDS[0] / "deterministic_total_score.json",
                {"status": "TAMPERED"},
            )

            verification = verify_sealed_production(
                output_root=root,
                target_ids=TARGET_IDS,
                as_of_date=AS_OF_DATE,
                archetype_id=ARCHETYPE,
                expected_semantics=expected,
            )

            self.assertFalse(verification.eligible)
            self.assertIn(
                f"{TARGET_IDS[0]}:manifest_output_tree_hash_mismatch",
                verification.reasons,
            )
            self.assertIn(
                f"{TARGET_IDS[0]}:score_vector_source_binding_invalid",
                verification.reasons,
            )

    def test_code_or_input_semantics_mismatch_forbids_skip(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sealed = _example_semantics()
            _write_valid_sealed_lane(root, expected=sealed)

            for key in ("code_fingerprint", "input_semantics_fingerprint"):
                with self.subTest(key=key):
                    current = {**sealed, key: "changed-" + str(sealed[key])}
                    fingerprints = {
                        name: current[name]
                        for name in (
                            "code_fingerprint",
                            "config_fingerprint",
                            "provider_fingerprint",
                            "input_semantics_fingerprint",
                        )
                    }
                    current["semantics_fingerprint"] = stable_hash(fingerprints)
                    verification = verify_sealed_production(
                        output_root=root,
                        target_ids=TARGET_IDS,
                        as_of_date=AS_OF_DATE,
                        archetype_id=ARCHETYPE,
                        expected_semantics=current,
                    )
                    self.assertFalse(verification.eligible)
                    self.assertIn(
                        f"production_semantics_{key}_mismatch",
                        verification.reasons,
                    )

    def test_cli_uses_post_run_only_and_preserves_all_frozen_hashes(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = _write_registry(root)
            provider_manifest = {
                "provider_name": "TEST",
                "score_or_stage_authority": False,
            }
            expected = _current_semantics(
                root=root,
                registry=registry,
                provider_manifest=provider_manifest,
            )
            _write_valid_sealed_lane(root, expected=expected)
            _write_review_file_names(root)
            before = _frozen_hashes(root)
            run_mock = Mock(side_effect=AssertionError("production rerun is forbidden"))
            compare = Mock(
                return_value=SimpleNamespace(
                    status=PHASE93_POST_RUN_PASS,
                    comparisons=tuple(
                        {"target_id": target_id} for target_id in TARGET_IDS
                    ),
                    audit={
                        "critical_counts": {
                            "critical_material_fact_recall_below_threshold_count": 0
                        }
                    },
                )
            )

            with (
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_build_research_provider",
                    return_value=object(),
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "CurrentResearcherModeTargetRunner",
                    return_value=SimpleNamespace(provider=object()),
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_research_provider_manifest",
                    return_value=provider_manifest,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_run_target_until_semantic_terminal",
                    run_mock,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "write_production_lane"
                ) as write_lane,
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_load_post_run_gold_tools",
                    return_value=(PHASE93_POST_RUN_PASS, compare, Mock()),
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "write_canary_post_run_gold_comparison"
                ),
                patch("builtins.print"),
            ):
                exit_code = main(_cli_args(root=root, registry=registry))
                second_exit_code = main(
                    _cli_args(root=root, registry=registry)
                )

            self.assertEqual(exit_code, 0)
            self.assertEqual(second_exit_code, 0)
            run_mock.assert_not_called()
            write_lane.assert_not_called()
            self.assertEqual(compare.call_count, 2)
            self.assertEqual(before, _frozen_hashes(root))
            summary = json.loads(
                (root / "phase94_run_summary.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                summary["production_execution_mode"],
                "SEALED_PRODUCTION_POST_RUN_ONLY",
            )
            self.assertTrue(summary["sealed_production_verified"])
            self.assertEqual(summary["frozen_production_file_count"], 12)

    def test_cli_input_fingerprint_mismatch_runs_production_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            registry = _write_registry(root)
            provider_manifest = {
                "provider_name": "TEST",
                "score_or_stage_authority": False,
            }
            expected = _current_semantics(
                root=root,
                registry=registry,
                provider_manifest=provider_manifest,
            )
            _write_valid_sealed_lane(root, expected=expected)
            _write_review_file_names(root)
            registry_payload = json.loads(registry.read_text(encoding="utf-8"))
            registry_payload["mandatory_targets"][0]["aliases"] = ["changed-input"]
            _write_json(registry, registry_payload)
            runs = tuple(
                SimpleNamespace(
                    status="PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD",
                    target=SimpleNamespace(target_id=target_id),
                    completion_gates={"all_complete": True},
                )
                for target_id in TARGET_IDS
            )
            run_mock = Mock(side_effect=runs)

            with (
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_build_research_provider",
                    return_value=object(),
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "CurrentResearcherModeTargetRunner",
                    return_value=SimpleNamespace(provider=object()),
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_research_provider_manifest",
                    return_value=provider_manifest,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_run_target_until_semantic_terminal",
                    run_mock,
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "write_production_lane",
                    return_value={"lane": root / "production_lane_manifest.json"},
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "_load_post_run_gold_tools",
                    return_value=(
                        PHASE93_POST_RUN_PASS,
                        Mock(
                            return_value=SimpleNamespace(
                                status=PHASE93_POST_RUN_PASS,
                                comparisons=(),
                                audit={
                                    "critical_counts": {
                                        "critical_material_fact_recall_"
                                        "below_threshold_count": 0
                                    }
                                },
                            )
                        ),
                        Mock(),
                    ),
                ),
                patch(
                    "e2r.cli.run_e2r_researcher_mode_until_pass."
                    "write_canary_post_run_gold_comparison"
                ),
                patch("builtins.print"),
            ):
                main(_cli_args(root=root, registry=registry))

            self.assertEqual(run_mock.call_count, 2)


def _example_semantics() -> dict[str, object]:
    fingerprints: dict[str, object] = {
        "code_fingerprint": "code-a",
        "config_fingerprint": "config-a",
        "provider_fingerprint": "provider-a",
        "input_semantics_fingerprint": "input-a",
    }
    return {
        "schema_version": "e2r_v5_phase94_production_semantics_seal_v1",
        **fingerprints,
        "semantics_fingerprint": stable_hash(fingerprints),
        "code_file_count": 1,
        "reference_file_count": 1,
    }


def _current_semantics(
    *, root: Path, registry: Path, provider_manifest: dict[str, object]
) -> Mapping[str, object]:
    rows = load_current_research_target_registry(registry)
    targets = load_current_research_targets(
        symbols=TARGET_IDS,
        registry_path=registry,
        registry_rows=rows,
        as_of_date=AS_OF_DATE,
    )
    config = CurrentResearcherModeConfig(
        as_of_date=AS_OF_DATE,
        archetype_id=ARCHETYPE,
        output_root=root,
        live_materialization_authorized=True,
        checkpoint_resume=True,
        gold_lane_isolated=True,
        require_researcher_parity=True,
        latest_trading_snapshot_date=AS_OF_DATE,
    )
    return build_current_production_semantics(
        config=config,
        targets=targets,
        registry_rows=rows,
        target_registry_path=registry,
        provider_manifest=provider_manifest,
        repo_root=Path.cwd(),
    )


def _write_valid_sealed_lane(
    root: Path, *, expected: Mapping[str, object]
) -> None:
    gates = {"all_complete": True}
    seal = make_production_semantics_seal(
        before_run=expected,
        after_run=expected,
    )
    _write_json(
        root / "production_lane_manifest.json",
        {
            "schema_version": "e2r_v5_phase94_production_lane_v1",
            "lane_role": "PRODUCTION",
            "as_of_date": AS_OF_DATE,
            "archetype_id": ARCHETYPE,
            "target_ids": list(TARGET_IDS),
            "target_statuses": {
                target_id: "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD"
                for target_id in TARGET_IDS
            },
            "gold_visibility": False,
            "gold_query_visibility": False,
            "gold_url_visibility": False,
            "gold_fact_visibility": False,
            "comparison_timing": "POST_RUN_ONLY",
            "production_research_complete": True,
            "production_semantics_seal": seal,
        },
    )
    _write_jsonl(
        root / "production_material_facts.jsonl",
        tuple(
            {
                "target_id": target_id,
                "fact_id": f"FACT-{target_id}",
                "gold_visibility": False,
            }
            for target_id in TARGET_IDS
        ),
    )
    _write_jsonl(
        root / "production_component_memos.jsonl",
        tuple(
            {
                "target_id": target_id,
                "memo_id": f"MEMO-{target_id}",
                "gold_visibility": False,
            }
            for target_id in TARGET_IDS
        ),
    )
    _write_jsonl(
        root / "production_input_manifest.jsonl",
        tuple(
            {"target_id": target_id, "input_id": f"INPUT-{target_id}"}
            for target_id in TARGET_IDS
        ),
    )
    for target_id in TARGET_IDS:
        target_root = root / target_id
        target_root.mkdir(parents=True, exist_ok=True)
        _write_jsonl(
            target_root / "evidence_facts.jsonl",
            ({"target_id": target_id, "fact_id": f"FACT-{target_id}"},),
        )
        _write_jsonl(
            target_root / "component_research_memos.jsonl",
            ({"target_id": target_id, "memo_id": f"MEMO-{target_id}"},),
        )
        score_source = target_root / "deterministic_total_score.json"
        _write_json(score_source, {"status": "COMPLETE"})
        _write_json(
            target_root / "score_vector.json",
            {
                "schema_version": "e2r_v5_canary_score_vector_v1",
                "target_id": target_id,
                "as_of_date": AS_OF_DATE,
                "status": "COMPLETE",
                "score_valid": True,
                "production_stage_authority": False,
                "pending_reasons": [],
                "source_artifact": "deterministic_total_score.json",
                "source_sha256": _file_hash(score_source),
            },
        )
        _write_json(
            target_root / "stagecourt_trace.json",
            {
                "schema_version": "e2r_v5_researcher_stagecourt_run_v1",
                "decision": {
                    "target_id": target_id,
                    "as_of_date": AS_OF_DATE,
                    "status": "FINAL",
                    "score_valid": True,
                    "research_complete": True,
                    "counter_thesis_complete": True,
                    "stage_gates_complete": True,
                    "canonical_stage": "2",
                },
                "audit": {
                    "status": "STAGECOURT_AUDIT_PASS",
                    "critical_count_sum": 0,
                    "canonical_stage": "2",
                },
            },
        )
        audit = {
            "schema_version": "e2r_v5_current_researcher_mode_v1",
            "target_id": target_id,
            "as_of_date": AS_OF_DATE,
            "status": "PRODUCTION_RESEARCH_COMPLETE_PENDING_POST_RUN_GOLD",
            "production_research_complete": True,
            "gold_visibility": False,
            "completion_gates": gates,
            "canary_leaf_contract": {
                "status": "CANARY_LEAF_CONTRACT_PASS",
                "critical_count_sum": 0,
            },
        }
        _write_json(target_root / "current_researcher_mode_audit.json", audit)
        _write_json(
            target_root / "canary_leaf_contract_audit.json",
            {
                "status": "CANARY_LEAF_CONTRACT_PASS",
                "target_id": target_id,
                "as_of_date": AS_OF_DATE,
                "critical_count_sum": 0,
            },
        )
        _write_json(
            target_root / "target_run_manifest.json",
            {
                **audit,
                "archetype_id": ARCHETYPE,
                "output_tree_hash": canary_output_tree_hash(
                    target_root,
                    include_post_run_gold=False,
                ),
            },
        )


def _write_registry(root: Path) -> Path:
    path = root / "targets.json"
    _write_json(
        path,
        {
            "mandatory_targets": [
                {"symbol": target_id, "company_name": target_id}
                for target_id in TARGET_IDS
            ]
        },
    )
    return path


def _write_review_file_names(root: Path) -> None:
    _write_json(root / "post_run_gold_semantic_primary.json", {"ready": True})
    review_root = root / "post_run_gold_semantic_reviews"
    _write_json(review_root / "review-a.json", {"ready": True})
    _write_json(review_root / "review-b.json", {"ready": True})


def _cli_args(*, root: Path, registry: Path) -> list[str]:
    return [
        "--as-of-date",
        AS_OF_DATE,
        "--symbols",
        ",".join(TARGET_IDS),
        "--archetype",
        ARCHETYPE,
        "--live-materialization-authorized",
        "true",
        "--checkpoint-resume",
        "true",
        "--gold-lane-isolated",
        "true",
        "--require-researcher-parity",
        "true",
        "--output-root",
        str(root),
        "--target-registry",
        str(registry),
    ]


def _frozen_hashes(root: Path) -> dict[str, str]:
    paths = [
        root / "production_lane_manifest.json",
        root / "production_material_facts.jsonl",
        root / "production_component_memos.jsonl",
        root / "production_input_manifest.jsonl",
    ]
    paths.extend(
        root / target_id / filename
        for target_id in TARGET_IDS
        for filename in (
            "evidence_facts.jsonl",
            "component_research_memos.jsonl",
            "score_vector.json",
            "stagecourt_trace.json",
        )
    )
    return {str(path.relative_to(root)): _file_hash(path) for path in paths}


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _write_jsonl(path: Path, rows: tuple[dict[str, object], ...]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(
            json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
            for row in rows
        ),
        encoding="utf-8",
    )


def _file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


if __name__ == "__main__":
    unittest.main()

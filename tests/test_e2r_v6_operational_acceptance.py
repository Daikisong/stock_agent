from __future__ import annotations

import json
import io
import hashlib
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from e2r.cli.run_e2r_v6_operational_acceptance_until_pass import (
    main as operational_cli_main,
)
from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_selection import (
    ISSUER_PROFILE_MANIFEST_NAME,
    REQUIRED_ARCHETYPES,
    compile_cross_archetype_canary_selection,
    seal_cross_archetype_canary_selection,
    seal_current_issuer_business_profile_manifest,
)
from e2r.production.v6_canary_results import (
    build_independent_canary_review,
    compile_cross_archetype_canary_directory,
)
from e2r.production.v6_current_krx_census import (
    CURRENT_KRX_CENSUS_PASS,
    CURRENT_KRX_CENSUS_SCHEMA,
    CURRENT_KRX_STAGE_ROW_SCHEMA,
)
from e2r.production.v6_production_static_audit import (
    PRODUCTION_STATIC_AUDIT_LEAF,
    compile_production_static_audit,
)
from e2r.production.v6_operational_self_repair import (
    FAILURE_CLASSES,
    SELF_REPAIR_AUDIT_LEAF,
    SELF_REPAIR_JOURNAL_LEAF,
    SELF_REPAIR_PASS,
    SELF_REPAIR_SCHEMA,
)
from e2r.production.v6_operational_acceptance import (
    OPERATIONAL_ACCEPTANCE_FAIL,
    OPERATIONAL_ACCEPTANCE_PENDING,
    OPERATIONAL_ACCEPTANCE_TEST_PASS,
    REVIEWER_GATE_PASS,
    REVIEWER_IDS,
    _load_selection_and_profile,
    _run_phase_subprocess,
    compile_operational_acceptance,
    run_operational_acceptance_phases,
)
from e2r.research_brain.researcher_mode.artifact_lifecycle import (
    ARTIFACT_LIFECYCLE_AUDIT_SCHEMA,
    ARTIFACT_LIFECYCLE_PASS,
    CANARY_RECEIPT_DATE,
    CLEAN_CLONE_REPRODUCTION_PASS,
    CLEAN_CLONE_REPRODUCTION_SCHEMA,
    CLEAN_CLONE_TEST_PASS,
    CLEAN_CLONE_TEST_SCHEMA,
    CROSS_ARCHETYPE_CANARY_SUMMARY_PASS,
    CROSS_ARCHETYPE_CANARY_SUMMARY_SCHEMA,
    FINAL_ROOT_RELATIVE,
    PROVIDER_RUNTIME_AUDIT_PASS,
    PROVIDER_RUNTIME_AUDIT_SCHEMA,
)
from e2r.research_brain.researcher_mode.independent_acceptance import (
    REVIEWER_GATE_PASS as LEGACY_GATE_PASS,
    SCHEMA_VERSION as LEGACY_GATE_SCHEMA,
)
from e2r.research_brain.researcher_mode.tracked_receipts import (
    PHASE101_TARGET_IDS,
    VERIFICATION_PASS,
    VERIFICATION_SCHEMA,
)
from e2r.research_brain.researcher_mode.tracked_readiness import (
    TRACKED_READINESS_PASS,
    TRACKED_READINESS_SCHEMA,
)
from tests.test_e2r_v6_canary_results import (
    _bundles as _phase106_bundles,
    _selection as _phase106_selection,
    _write_live_tree as _write_phase106_live_tree,
)
from tests import test_e2r_v6_canary_selection as selection_fixtures


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def _write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


_STATIC_AUDIT_FIXTURE: dict[str, object] | None = None


def _static_audit_fixture() -> dict[str, object]:
    global _STATIC_AUDIT_FIXTURE
    if _STATIC_AUDIT_FIXTURE is None:
        _STATIC_AUDIT_FIXTURE = dict(
            compile_production_static_audit(repo_root=Path.cwd())
        )
    return json.loads(json.dumps(_STATIC_AUDIT_FIXTURE))


def _self_repair_fixture() -> dict[str, object]:
    critical_counts = {
        "journal_missing_count": 0,
        "journal_empty_count": 0,
        "journal_parse_error_count": 0,
        "duplicate_iteration_id_count": 0,
        "unknown_failure_class_count": 0,
        "invalid_iteration_count": 0,
        "unverifiable_patch_commit_count": 0,
        "before_hash_mismatch_count": 0,
        "after_hash_mismatch_count": 0,
        "focused_test_failure_count": 0,
        "clean_rerun_failure_count": 0,
        "remaining_blocker_count": 0,
        "unresolved_failure_class_count": 0,
    }
    iteration = {
        "iteration_id": "E2RREPAIR-0123456789abcdef01234567",
        "failure_class": "RECEIPT_LINEAGE_BROKEN",
        "patch_commit": "a" * 40,
        "first_parent": "b" * 40,
        "file_path": "src/e2r/example.py",
        "shape_valid": True,
        "patch_commit_verified": True,
        "before_hash_verified": True,
        "after_hash_verified": True,
        "before_hash_recomputed": "c" * 64,
        "after_hash_recomputed": "d" * 64,
        "focused_tests_verified": True,
        "clean_rerun_verified": True,
        "remaining_blocker_count": 0,
        "resolved": True,
    }
    class_counts = {name: 0 for name in FAILURE_CLASSES}
    class_counts["RECEIPT_LINEAGE_BROKEN"] = 1
    core = {
        "schema_version": SELF_REPAIR_SCHEMA,
        "status": SELF_REPAIR_PASS,
        "journal_path": SELF_REPAIR_JOURNAL_LEAF,
        "journal_sha256": "e" * 64,
        "iteration_count": 1,
        "iteration_roster_hash": "f" * 64,
        "failure_class_counts": class_counts,
        "unresolved_failure_class_counts": {name: 0 for name in FAILURE_CLASSES},
        "iteration_audits": [iteration],
        "critical_counts": critical_counts,
        "critical_count_sum": 0,
        "all_failure_classes_resolved": True,
        "fixed_iteration_count_is_completion_authority": False,
        "caller_attestation_trusted": False,
        "production_readiness_authority": False,
        "score_or_stage_authority": False,
        "test_mode": True,
    }
    return {**core, "audit_hash": stable_hash(core)}


def _target_report(target_id: str) -> dict[str, object]:
    return {
        "target_id": target_id,
        "status": VERIFICATION_PASS,
        "critical_count": 0,
        "failures": [],
        "forbidden_runtime_inputs_read": [],
        "metrics": {
            "total_score_recomputed": 61.0,
            "canonical_stage_recomputed": "3-Yellow",
            "component_count": 7,
            "judge_count": 7,
            "scoring_fact_count": 3,
            "source_count": 2,
            "anchor_count": 7,
            "provider_call_receipt_count": 1,
        },
    }


class _Fixture:
    def __init__(self, root: Path) -> None:
        self.repo = root
        self.final = root / FINAL_ROOT_RELATIVE
        self.final.mkdir(parents=True)
        self.canary_targets: dict[str, str] = {}
        self._build()

    def _build(self) -> None:
        _write_json(
            self.final / "starting_state.json",
            {"v5_full_test_count": 6637},
        )
        receipt_root = self.final / "canary_receipts" / CANARY_RECEIPT_DATE
        for target_id in PHASE101_TARGET_IDS:
            target = receipt_root / target_id
            target.mkdir(parents=True)
            _write_json(target / "receipt_manifest.json", {"target_id": target_id})
            _write_jsonl(
                target / "provider_calls.jsonl",
                [{"provider_name": "COLLABORATION_CODEX", "status": "SUCCESS", "score_or_stage_authority": False}],
            )

        selection = _phase106_selection()
        selection_rows = selection["selections"]
        assert isinstance(selection_rows, list)
        live = self.final / "current_live_canaries"
        for row in selection_rows:
            assert isinstance(row, dict)
            self.canary_targets[str(row["archetype_id"])] = str(row["target_id"])
        _write_json(
            self.final / "cross_archetype_canary_selection.json",
            selection,
        )
        bundles = _phase106_bundles(selection)
        for archetype, bundle in bundles.items():
            result = bundle["result"]
            receipt = bundle["receipt"]
            bundle["reviews"] = [
                build_independent_canary_review(
                    reviewer_id=f"reviewer_{reviewer.casefold()}",
                    provider_call_id=f"COLLABCALL-{archetype}-{reviewer}",
                    prompt_hash=hashlib.sha256(f"prompt:{archetype}:{reviewer}".encode()).hexdigest(),
                    response_hash=hashlib.sha256(f"response:{archetype}:{reviewer}".encode()).hexdigest(),
                    result=result,
                    receipt=receipt,
                )
                for reviewer in ("A", "B")
            ]
        _write_phase106_live_tree(live, selection, bundles)
        compilation = compile_cross_archetype_canary_directory(
            selection=selection,
            live_root=live,
        )
        self.canary_compilation = compilation
        _write_json(
            self.final / "cross_archetype_canary_summary.json",
            compilation["summary"],
        )

        rows: list[dict[str, object]] = []
        for index in range(1001):
            maximum = "L3" if index == 0 else "L4" if index == 1 else "L5" if index == 2 else "L1"
            rows.append(
                {
                    "schema_version": CURRENT_KRX_STAGE_ROW_SCHEMA,
                    "symbol": f"{300000 + index:06d}",
                    "company_name": f"기업{index}",
                    "market": "KOSPI",
                    "assessment_as_of_date": "2026-08-09",
                    "latest_trading_snapshot_date": "2026-08-07",
                    "trigger_lane_ids": [
                        "OFFICIAL_DISCLOSURE",
                        "PRICE_VOLUME_ANOMALY",
                        "TRUSTED_NEWS",
                    ] if index == 0 else [],
                    "maximum_depth": maximum,
                    "current_score": 61.0 if maximum == "L5" else None,
                    "canonical_stage": "3-Yellow" if maximum == "L5" else None,
                    "stage_status": "FINAL" if maximum == "L5" else "NOT_OPEN",
                    "dossier_receipt_id": "DEEP-RECEIPT-1" if maximum == "L5" else None,
                }
            )
        _write_jsonl(self.final / "current_krx_stage_map_compact.jsonl", rows)
        census_core = {
            "schema_version": CURRENT_KRX_CENSUS_SCHEMA,
            "status": CURRENT_KRX_CENSUS_PASS,
            "assessment_as_of_date": "2026-08-09",
            "real_krx_universe_source": True,
            "eligible_universe_count": len(rows),
            "stage_map_hash": stable_hash(tuple(rows)),
            "natural_trigger_lane_count": 3,
            "natural_candidate_count": 1,
            "accepted_scoring_fact_count": 1,
            "deep_receipt_ids": ["DEEP-RECEIPT-1"],
            "live_input_tree_hash": "a" * 64,
            "critical_count_sum": 0,
            "production_runtime_ready": True,
            "test_mode": False,
        }
        _write_json(
            self.final / "current_krx_census_summary.json",
            {
                **census_core,
                "summary_hash": stable_hash(census_core),
            },
        )

        manifest = {
            "schema_version": "fixture_lifecycle",
            "artifacts": [{"artifact_id": "current"}],
            "status_projection": {"score_valid": True, "stage_final": True},
        }
        _write_json(self.final / "artifact_lifecycle_manifest.json", manifest)
        _write_json(
            self.final / "artifact_lifecycle_audit.json",
            {
                "schema_version": ARTIFACT_LIFECYCLE_AUDIT_SCHEMA,
                "status": ARTIFACT_LIFECYCLE_PASS,
                "ready": True,
                "critical_count_sum": 0,
                "manifest_hash": stable_hash(manifest),
            },
        )
        receipt_recompute = {
            "schema_version": VERIFICATION_SCHEMA,
            "status": VERIFICATION_PASS,
            "critical_count_sum": 0,
            "target_ids": list(PHASE101_TARGET_IDS),
        }
        readiness = {
            "schema_version": TRACKED_READINESS_SCHEMA,
            "status": TRACKED_READINESS_PASS,
            "ready": True,
            "offline": True,
            "critical_count": 0,
            "same_receipt_replay_variance": 0,
        }
        tests = {
            "schema_version": CLEAN_CLONE_TEST_SCHEMA,
            "status": CLEAN_CLONE_TEST_PASS,
            "executed_test_count": 100,
            "failed_test_count": 0,
            "error_test_count": 0,
        }
        _write_json(self.final / "clean_clone/receipt_recompute_result.json", receipt_recompute)
        _write_json(self.final / "clean_clone/tracked_readiness_result.json", readiness)
        _write_json(self.final / "clean_clone/test_result.json", tests)
        clean_clone_root = self.final / "clean_clone"
        _write_json(
            self.final / "clean_clone_reproduction.json",
            {
                "schema_version": CLEAN_CLONE_REPRODUCTION_SCHEMA,
                "status": CLEAN_CLONE_REPRODUCTION_PASS,
                "critical_count_sum": 0,
                "receipt_recompute_result_hash": hashlib.sha256(
                    (clean_clone_root / "receipt_recompute_result.json").read_bytes()
                ).hexdigest(),
                "tracked_readiness_result_hash": hashlib.sha256(
                    (clean_clone_root / "tracked_readiness_result.json").read_bytes()
                ).hexdigest(),
                "test_result_hash": hashlib.sha256(
                    (clean_clone_root / "test_result.json").read_bytes()
                ).hexdigest(),
            },
        )
        _write_json(
            self.final / "provider_runtime_audit.json",
            {
                "schema_version": PROVIDER_RUNTIME_AUDIT_SCHEMA,
                "status": PROVIDER_RUNTIME_AUDIT_PASS,
                "critical_count_sum": 0,
                "qwen_call_count": 0,
                "ollama_call_count": 0,
                "provider_call_counts": {"COLLABORATION_CODEX": 22},
            },
        )
        _write_json(
            self.final / PRODUCTION_STATIC_AUDIT_LEAF,
            _static_audit_fixture(),
        )
        _write_jsonl(
            self.final / SELF_REPAIR_JOURNAL_LEAF,
            [{"fixture": "journal presence is independently represented by audit"}],
        )
        _write_json(
            self.final / SELF_REPAIR_AUDIT_LEAF,
            _self_repair_fixture(),
        )
        legacy_rows = [
            {
                "reviewer_id": reviewer,
                "status": "PASS",
                "critical_count_sum": 0,
                "detector_run_count": 1,
                "detector_pass_count": 1,
            }
            for reviewer in "ABCDEFGHIJ"
        ]
        _write_json(
            self.repo / "docs/operational/e2r_v5_reviewer_gate.json",
            {
                "schema_version": LEGACY_GATE_SCHEMA,
                "status": LEGACY_GATE_PASS,
                "reviewer_roster": list("ABCDEFGHIJ"),
                "reviewers": legacy_rows,
            },
        )

    @staticmethod
    def receipt_report(_path: str | Path) -> dict[str, object]:
        targets = [_target_report(target) for target in PHASE101_TARGET_IDS]
        return {
            "status": VERIFICATION_PASS,
            "critical_count_sum": 0,
            "target_ids": list(PHASE101_TARGET_IDS),
            "targets": targets,
        }

    @staticmethod
    def target_report(path: str | Path) -> dict[str, object]:
        return _target_report(Path(path).name)

    @staticmethod
    def repository_probe(_repo: Path, _paths: object) -> dict[str, bool]:
        return {
            "canonical_repository": True,
            "origin_main_matches_head": True,
            "worktree_clean": True,
            "all_acceptance_artifacts_tracked_at_head": True,
        }

    @staticmethod
    def tests(_repo: Path) -> dict[str, object]:
        return {
            "status": "PASS",
            "executed_test_count": 6637,
            "failed_test_count": 0,
            "error_test_count": 0,
        }

    @staticmethod
    def static_audit(*, repo_root: Path) -> dict[str, object]:
        del repo_root
        return _static_audit_fixture()

    def compile(self) -> dict[str, object]:
        return dict(
            compile_operational_acceptance(
                repo_root=self.repo,
                final_root=FINAL_ROOT_RELATIVE,
                receipt_verifier=self.receipt_report,
                repository_probe=self.repository_probe,
                test_runner=self.tests,
                static_audit_compiler=self.static_audit,
                test_mode=True,
            )
        )


class E2RV6OperationalAcceptanceTests(unittest.TestCase):
    def test_full_phase_fixture_recomputes_exact_k_to_v_roster_without_production_authority(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture = _Fixture(Path(tmp))
            result = fixture.compile()

        self.assertEqual(result["status"], OPERATIONAL_ACCEPTANCE_TEST_PASS)
        self.assertFalse(result["ready"])
        self.assertFalse(result["production_readiness_authority"])
        self.assertEqual(
            tuple(row["reviewer_id"] for row in result["reviewer_gate"]["reviewers"]),
            REVIEWER_IDS,
        )
        self.assertTrue(all(row["leaf_recomputed"] for row in result["reviewer_gate"]["reviewers"]))

    def test_reviewer_v_rejects_full_test_count_below_starting_baseline(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture = _Fixture(Path(tmp))
            result = compile_operational_acceptance(
                repo_root=fixture.repo,
                final_root=FINAL_ROOT_RELATIVE,
                receipt_verifier=fixture.receipt_report,
                repository_probe=fixture.repository_probe,
                static_audit_compiler=fixture.static_audit,
                test_runner=lambda _repo: {
                    "status": "PASS",
                    "executed_test_count": 6636,
                    "failed_test_count": 0,
                    "error_test_count": 0,
                },
                test_mode=True,
            )

        reviewer_v = next(
            row
            for row in result["reviewer_gate"]["reviewers"]
            if row["reviewer_id"] == "V"
        )
        self.assertEqual(reviewer_v["status"], "FAIL")
        self.assertEqual(
            reviewer_v["critical_counts"]["full_test_failure_count"],
            1,
        )
        self.assertEqual(reviewer_v["metrics"]["full_test_count_baseline"], 6637)
        self.assertEqual(reviewer_v["metrics"]["full_test_count_delta"], -1)

    def test_terminal_publications_do_not_self_hash_into_their_reviewer_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture = _Fixture(Path(tmp))
            before = fixture.compile()["reviewer_gate"]
            _write_json(
                fixture.final / "operational_acceptance_reviewer_gate.json",
                before,
            )
            (fixture.final / "operational_cutover_final.md").write_text(
                "# final publication\n",
                encoding="utf-8",
            )
            after = fixture.compile()["reviewer_gate"]

        self.assertEqual(after, before)

    def test_absent_phase101_108_artifacts_cannot_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            result = compile_operational_acceptance(
                repo_root=repo,
                final_root=FINAL_ROOT_RELATIVE,
                receipt_verifier=lambda _path: {},
                repository_probe=_Fixture.repository_probe,
                test_runner=_Fixture.tests,
                test_mode=True,
            )

        self.assertEqual(result["status"], OPERATIONAL_ACCEPTANCE_FAIL)
        self.assertEqual(
            set(result["phase_artifact_presence"]),
            set("101 102 103 104 105 106 107 108".split()),
        )
        self.assertGreater(
            result["critical_counts"]["phase101_108_missing_count"],
            0,
        )

    def test_caller_cannot_replace_production_verifiers_with_placeholders(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "cannot replace verifiers"):
                compile_operational_acceptance(
                    repo_root=tmp,
                    receipt_verifier=lambda _path: {"status": VERIFICATION_PASS},
                )

    def test_tampered_stage_map_hash_fails_reviewer_q_and_final_v(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture = _Fixture(Path(tmp))
            census_path = fixture.final / "current_krx_census_summary.json"
            census = json.loads(census_path.read_text())
            census["stage_map_hash"] = "0" * 64
            _write_json(census_path, census)
            result = fixture.compile()

        by_id = {row["reviewer_id"]: row for row in result["reviewer_gate"]["reviewers"]}
        self.assertEqual(by_id["Q"]["status"], "FAIL")
        self.assertEqual(by_id["Q"]["critical_counts"]["stage_map_hash_mismatch_count"], 1)
        self.assertEqual(by_id["V"]["status"], "FAIL")

    def test_reviewer_u_recomputes_static_findings_instead_of_trusting_zero_leaf(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture = _Fixture(Path(tmp))
            recomputed = fixture.static_audit(repo_root=fixture.repo)
            counts = dict(recomputed["critical_counts"])
            counts["target_conditioned_branch_count"] = 1
            recomputed["critical_counts"] = counts
            recomputed["critical_count_sum"] = 1
            recomputed["all_required_counts_zero"] = False
            recomputed["status"] = "E2R_V6_PRODUCTION_STATIC_AUDIT_FAIL"
            recomputed["findings"] = [
                {
                    "finding_class": "target_conditioned_branch_count",
                    "path": "src/e2r/production/known_bad.py",
                    "line": 1,
                    "column": 0,
                    "rule": "TARGET_LITERAL_CONTROLS_BRANCH",
                }
            ]
            core = {
                key: value
                for key, value in recomputed.items()
                if key != "audit_hash"
            }
            recomputed["audit_hash"] = stable_hash(core)
            result = compile_operational_acceptance(
                repo_root=fixture.repo,
                final_root=FINAL_ROOT_RELATIVE,
                receipt_verifier=fixture.receipt_report,
                repository_probe=fixture.repository_probe,
                test_runner=fixture.tests,
                static_audit_compiler=lambda **_kwargs: recomputed,
                test_mode=True,
            )

        by_id = {
            row["reviewer_id"]: row
            for row in result["reviewer_gate"]["reviewers"]
        }
        self.assertEqual(by_id["U"]["status"], "FAIL")
        self.assertEqual(
            by_id["U"]["critical_counts"][
                "recomputed_target_conditioned_branch_count"
            ],
            1,
        )
        self.assertEqual(
            by_id["U"]["critical_counts"][
                "production_static_audit_contract_failure_count"
            ],
            1,
        )
        self.assertEqual(by_id["V"]["status"], "FAIL")

    def test_local_provider_lineage_and_absolute_path_are_independent_failures(self):
        with tempfile.TemporaryDirectory() as tmp:
            fixture = _Fixture(Path(tmp))
            provider = next(
                (fixture.final / "canary_receipts" / CANARY_RECEIPT_DATE).rglob("provider_calls.jsonl")
            )
            _write_jsonl(provider, [{"provider_name": "Qwen-local", "status": "SUCCESS", "score_or_stage_authority": False}])
            (fixture.final / "portable_note.md").write_text("identity=/root/cache/run.json\n", encoding="utf-8")
            result = fixture.compile()

        by_id = {row["reviewer_id"]: row for row in result["reviewer_gate"]["reviewers"]}
        self.assertEqual(by_id["N"]["status"], "FAIL")
        self.assertGreater(by_id["N"]["critical_counts"]["local_provider_call_count"], 0)
        self.assertEqual(by_id["U"]["status"], "FAIL")
        self.assertGreater(by_id["U"]["critical_counts"]["absolute_path_identity_count"], 0)

    def test_one_command_cli_requires_every_resume_and_verification_phase(self):
        with tempfile.TemporaryDirectory() as tmp, self.assertRaisesRegex(
            SystemExit, "requires every phase flag"
        ):
            operational_cli_main(
                [
                    "--repo-root",
                    tmp,
                    "--live-materialization-authorized",
                    "true",
                    "--research-provider",
                    "codex-collaboration",
                    "--run-current-krx-census",
                    "false",
                ]
            )

    def test_one_command_cli_writes_checkpoint_and_k_v_gate_without_false_success(self):
        fake = {
            "schema_version": "e2r_v6_operational_acceptance_v1",
            "status": OPERATIONAL_ACCEPTANCE_FAIL,
            "blockers": ["phase101_107_missing"],
            "reviewer_gate": {"status": "FAIL", "reviewers": []},
        }
        with tempfile.TemporaryDirectory() as tmp, patch(
            "e2r.cli.run_e2r_v6_operational_acceptance_until_pass.run_operational_acceptance_phases",
            return_value=fake,
        ), redirect_stdout(io.StringIO()):
            output = Path(tmp) / "checkpoint"
            code = operational_cli_main(
                [
                    "--repo-root",
                    tmp,
                    "--live-materialization-authorized",
                    "true",
                    "--research-provider",
                    "codex-collaboration",
                    "--output-root",
                    str(output),
                ]
            )

            self.assertEqual(code, 3)
            self.assertEqual(
                json.loads((output / "operational_acceptance_checkpoint.json").read_text())["status"],
                OPERATIONAL_ACCEPTANCE_FAIL,
            )
            self.assertTrue((output / "operational_reviewer_gate_k_v.json").is_file())

    def test_one_command_cli_rejects_output_symlink_alias_before_driver(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            repo = Path(tmp).resolve()
            alias = repo / "output-alias"
            alias.symlink_to(Path(outside), target_is_directory=True)
            with patch(
                "e2r.cli.run_e2r_v6_operational_acceptance_until_pass.run_operational_acceptance_phases"
            ) as run, self.assertRaisesRegex(ValueError, "cannot traverse a symlink"):
                operational_cli_main(
                    [
                        "--repo-root",
                        str(repo),
                        "--live-materialization-authorized",
                        "true",
                        "--research-provider",
                        "codex-collaboration",
                        "--output-root",
                        str(alias / "phase108"),
                    ]
                )

            run.assert_not_called()
            self.assertEqual(tuple(Path(outside).iterdir()), ())

    def test_phase_driver_missing_selection_stops_at_missing_forced_profile(self):
        calls: list[list[str]] = []
        checkpoints: list[dict[str, object]] = []
        stdout = json.dumps({"status": "SELECTION_INPUT_PENDING"})

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            return subprocess.CompletedProcess(command, 2, stdout=stdout, stderr="")

        with tempfile.TemporaryDirectory() as tmp, patch(
            "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
            return_value=True,
        ), patch(
            "e2r.production.v6_operational_acceptance._phase105_live_inputs_ready",
            return_value=True,
        ):
            result = run_operational_acceptance_phases(
                repo_root=tmp,
                output_root=Path(tmp) / "driver",
                as_of_date="2026-08-09",
                research_provider="codex-collaboration",
                command_runner=runner,
                checkpoint_writer=lambda payload: checkpoints.append(dict(payload)),
                test_mode=True,
            )

        self.assertEqual(result["status"], OPERATIONAL_ACCEPTANCE_PENDING)
        self.assertEqual(result["blockers"], ["PHASE105_ISSUER_PROFILE_PENDING"])
        self.assertEqual(len(calls), 2)
        self.assertEqual(calls[0][1:3], ["-m", "e2r.cli.select_e2r_v6_cross_archetype_canaries"])
        self.assertEqual(
            calls[1][1:3],
            ["-m", "e2r.cli.materialize_e2r_v6_issuer_business_profiles"],
        )
        attempt = result["phase_driver"]["command_attempts"][0]
        self.assertEqual(attempt["exit_code"], 2)
        self.assertEqual(attempt["semantic_status"], "SELECTION_INPUT_PENDING")
        self.assertEqual(attempt["stdout_sha256"], hashlib.sha256(stdout.encode()).hexdigest())
        self.assertFalse(attempt["shell"])
        self.assertFalse(attempt["score_or_stage_authority"])
        self.assertTrue(checkpoints)
        self.assertNotIn("reviewer_gate", result)
        self.assertNotIn("full_test_result", result)

    def test_phase105_materializes_current_krx_inputs_before_selection(self):
        calls: list[list[str]] = []

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            status = (
                "SOURCE_PENDING"
                if command[2] == "e2r.cli.run_e2r_census_mode"
                else "SELECTION_INPUT_PENDING"
            )
            return subprocess.CompletedProcess(
                command,
                2,
                stdout=json.dumps({"status": status}),
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp, patch(
            "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
            return_value=True,
        ), patch(
            "e2r.production.v6_operational_acceptance._phase105_live_inputs_ready",
            side_effect=(False, True),
        ), patch(
            "e2r.production.v6_operational_acceptance._phase105_selection_ready",
            return_value=False,
        ), patch(
            "e2r.production.v6_operational_acceptance._phase105_profile_ready",
            return_value=False,
        ):
            result = run_operational_acceptance_phases(
                repo_root=tmp,
                output_root=Path(tmp) / "driver",
                as_of_date="2026-08-21",
                research_provider="codex-collaboration",
                command_runner=runner,
                test_mode=True,
            )

        modules = [command[2] for command in calls]
        self.assertEqual(
            modules,
            [
                "e2r.cli.run_e2r_census_mode",
                "e2r.cli.select_e2r_v6_cross_archetype_canaries",
                "e2r.cli.materialize_e2r_v6_issuer_business_profiles",
            ],
        )
        census = calls[0]
        self.assertEqual(
            census[census.index("--as-of-date") + 1],
            "2026-08-21",
        )
        self.assertEqual(
            census[census.index("--materialize-live-input") + 1],
            "true",
        )
        self.assertIn("--resume", census)
        self.assertEqual(
            result["blockers"],
            ["PHASE105_ISSUER_PROFILE_PENDING"],
        )
        self.assertEqual(
            result["phase_driver"]["command_attempts"][0]["step_id"],
            "current_krx_input_materialization",
        )

    def test_phase105_profile_is_materialized_then_exactly_passed_to_selector(self):
        calls: list[list[str]] = []

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            module = command[2]
            if module == "e2r.cli.materialize_e2r_v6_issuer_business_profiles":
                return subprocess.CompletedProcess(
                    command,
                    0,
                    stdout=json.dumps({"status": "E2R_V6_ISSUER_BUSINESS_PROFILE_PASS"}),
                    stderr="",
                )
            return subprocess.CompletedProcess(
                command,
                2,
                stdout=json.dumps({"status": "E2R_V6_CROSS_ARCHETYPE_CANARY_SELECTION_FAIL"}),
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp, patch(
            "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
            return_value=True,
        ), patch(
            "e2r.production.v6_operational_acceptance._phase105_live_inputs_ready",
            return_value=True,
        ), patch(
            "e2r.production.v6_operational_acceptance._phase105_selection_ready",
            return_value=False,
        ), patch(
            "e2r.production.v6_operational_acceptance._phase105_profile_ready",
            side_effect=(False, True),
        ):
            result = run_operational_acceptance_phases(
                repo_root=tmp,
                output_root=Path(tmp) / "driver",
                as_of_date="2026-08-09",
                research_provider="codex-collaboration",
                command_runner=runner,
                test_mode=True,
            )

        self.assertEqual(result["blockers"], ["PHASE105_SELECTION_PENDING"])
        self.assertEqual(
            [command[2] for command in calls],
            [
                "e2r.cli.select_e2r_v6_cross_archetype_canaries",
                "e2r.cli.materialize_e2r_v6_issuer_business_profiles",
                "e2r.cli.select_e2r_v6_cross_archetype_canaries",
            ],
        )
        profile_path = str(
            Path(tmp)
            / "docs/operational/e2r_v6_operational_cutover"
            / "issuer_business_profile_manifest.json"
        )
        self.assertIn("--issuer-profile-manifest", calls[2])
        self.assertEqual(
            calls[2][calls[2].index("--issuer-profile-manifest") + 1],
            profile_path,
        )

    def test_phase105_profile_collaboration_wait_stops_before_profiled_selection(self):
        calls: list[list[str]] = []

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            if command[2] == "e2r.cli.materialize_e2r_v6_issuer_business_profiles":
                return subprocess.CompletedProcess(
                    command,
                    3,
                    stdout=json.dumps(
                        {
                            "status": "E2R_V6_ISSUER_BUSINESS_PROFILE_PENDING",
                            "blockers": ["COLLABORATION_RESPONSE_PENDING"],
                        }
                    ),
                    stderr="",
                )
            return subprocess.CompletedProcess(
                command,
                2,
                stdout=json.dumps({"status": "SELECTION_PENDING"}),
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp, patch(
            "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
            return_value=True,
        ), patch(
            "e2r.production.v6_operational_acceptance._phase105_live_inputs_ready",
            return_value=True,
        ), patch(
            "e2r.production.v6_operational_acceptance._phase105_selection_ready",
            return_value=False,
        ), patch(
            "e2r.production.v6_operational_acceptance._phase105_profile_ready",
            return_value=False,
        ):
            result = run_operational_acceptance_phases(
                repo_root=tmp,
                output_root=Path(tmp) / "driver",
                as_of_date="2026-08-09",
                research_provider="codex-collaboration",
                command_runner=runner,
                test_mode=True,
            )

        self.assertEqual(
            result["blockers"],
            ["PHASE105_ISSUER_PROFILE_COLLABORATION_PENDING"],
        )
        self.assertEqual(len(calls), 2)
        self.assertEqual(
            calls[-1][2],
            "e2r.cli.materialize_e2r_v6_issuer_business_profiles",
        )

    def test_forced_selection_reopens_only_with_its_sealed_official_profile(self):
        selection_fixture = selection_fixtures.E2RV6CanarySelectionTests(
            methodName=(
                "test_forced_exact_five_require_complete_official_profile_and_abstention"
            )
        )
        candidates = selection_fixture._abstained_candidates()
        profile = selection_fixture._forced_profile_manifest(candidates)
        selection = compile_cross_archetype_canary_selection(
            selection_as_of_date=selection_fixture.AS_OF_DATE,
            candidates=candidates,
            trigger_events=selection_fixture._signals(candidates),
            issuer_business_profile_manifest=profile,
        )
        self.assertEqual(
            {row["archetype_id"] for row in selection["selections"]},
            set(REQUIRED_ARCHETYPES),
        )

        with tempfile.TemporaryDirectory() as tmp:
            final = Path(tmp) / FINAL_ROOT_RELATIVE
            profile_path = final / ISSUER_PROFILE_MANIFEST_NAME
            selection_path = final / "cross_archetype_canary_selection.json"
            seal_current_issuer_business_profile_manifest(profile_path, profile)
            seal_cross_archetype_canary_selection(
                selection_path,
                selection,
                issuer_business_profile_manifest=profile,
            )

            reopened_selection, reopened_profile = _load_selection_and_profile(
                selection_path,
                issuer_profile_path=profile_path,
            )
            self.assertEqual(stable_hash(reopened_selection), stable_hash(selection))
            self.assertIsNotNone(reopened_profile)
            self.assertEqual(stable_hash(reopened_profile), stable_hash(profile))

            profile_path.unlink()
            with self.assertRaisesRegex(
                (OSError, ValueError),
                "profile|missing|exist",
            ):
                _load_selection_and_profile(
                    selection_path,
                    issuer_profile_path=profile_path,
                )

    def test_phase101_nonzero_canonical_runner_fails_closed_before_selection(self):
        calls: list[list[str]] = []

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            return subprocess.CompletedProcess(
                command,
                2,
                stdout=json.dumps({"status": "PRODUCTION_RESEARCH_FAIL"}),
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp, patch(
            "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
            return_value=False,
        ):
            result = run_operational_acceptance_phases(
                repo_root=tmp,
                output_root=Path(tmp) / "driver",
                as_of_date="2026-08-09",
                research_provider="codex-collaboration",
                command_runner=runner,
                test_mode=True,
            )

        self.assertEqual(result["blockers"], ["PHASE101_C06_CANONICAL_RUN_PENDING"])
        self.assertEqual(len(calls), 1)
        self.assertEqual(
            calls[0][1:3],
            ["-m", "e2r.cli.run_e2r_researcher_mode_until_pass"],
        )
        self.assertEqual(
            calls[0][calls[0].index("--fact-documents-per-call") + 1],
            "8",
        )
        self.assertNotIn(
            "e2r.cli.select_e2r_v6_cross_archetype_canaries",
            calls[0],
        )

    def test_phase101_collaboration_wait_returns_before_receipt_export(self):
        calls: list[list[str]] = []

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            return subprocess.CompletedProcess(
                command,
                3,
                stdout=json.dumps(
                    {
                        "status": "PRODUCTION_RESEARCH_PENDING",
                        "blockers": ["COLLABORATION_RESPONSE_PENDING"],
                    }
                ),
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp, patch(
            "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
            return_value=False,
        ):
            result = run_operational_acceptance_phases(
                repo_root=tmp,
                output_root=Path(tmp) / "driver",
                as_of_date="2026-08-09",
                research_provider="codex-collaboration",
                command_runner=runner,
                test_mode=True,
            )

        self.assertEqual(result["blockers"], ["PHASE101_C06_COLLABORATION_PENDING"])
        self.assertEqual(len(calls), 1)
        self.assertEqual(
            calls[0][1:3],
            ["-m", "e2r.cli.run_e2r_researcher_mode_until_pass"],
        )

    def test_phase101_compact_stdout_recomputes_current_leaf_collaboration_wait(self):
        calls: list[list[str]] = []
        request_id = "COLLABREQ-" + "a" * 64

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            return subprocess.CompletedProcess(
                command,
                2,
                stdout=json.dumps(
                    {"status": "PHASE94_CURRENT_RESEARCHER_MODE_PENDING"}
                ),
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            target = (
                repo
                / "output/researcher_mode/c06"
                / CANARY_RECEIPT_DATE
                / "005930"
            )
            provider = target / "collaboration_codex_subagent_provider"
            (provider / "requests").mkdir(parents=True)
            (provider / "responses").mkdir()
            _write_json(
                target / "target_run_manifest.json",
                {"status": "RESEARCH_CHECKPOINT_PENDING"},
            )
            _write_json(
                target / "source_graph_checkpoint.json",
                {
                    "status": "CANDIDATE_RANKING_PENDING",
                    "pending_reasons": [
                        "PARTITION_0:RANKING_PROVIDER_ERROR:"
                        f"COLLABORATION_RESPONSE_PENDING:{request_id}"
                    ],
                },
            )
            _write_json(
                provider / "requests" / f"{request_id}.json",
                {"request_id": request_id},
            )
            with patch(
                "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
                return_value=False,
            ):
                result = run_operational_acceptance_phases(
                    repo_root=repo,
                    output_root=repo / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )

        self.assertEqual(
            result["blockers"], ["PHASE101_C06_COLLABORATION_PENDING"]
        )
        self.assertEqual(len(calls), 1)
        attempt = result["phase_driver"]["command_attempts"][0]
        self.assertEqual(
            attempt["pending_markers"], ["COLLABORATION_RESPONSE_PENDING"]
        )
        self.assertEqual(attempt["current_collaboration_request_ids"], [request_id])

    def test_phase101_compact_stdout_finds_current_epoch_supervisor_wait(self):
        calls: list[list[str]] = []
        request_id = "COLLABREQ-" + "e" * 64

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            return subprocess.CompletedProcess(
                command,
                2,
                stdout=json.dumps(
                    {"status": "PHASE94_CURRENT_RESEARCHER_MODE_PENDING"}
                ),
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            target = (
                repo
                / "output/researcher_mode/c06"
                / CANARY_RECEIPT_DATE
                / "005930"
            )
            provider = target / "collaboration_codex_subagent_provider"
            (provider / "requests").mkdir(parents=True)
            (provider / "responses").mkdir()
            _write_json(
                target / "target_run_manifest.json",
                {"status": "RESEARCH_CHECKPOINT_PENDING"},
            )
            _write_json(
                target / "research_epoch_checkpoint.json",
                {
                    "status": "NEXT_RESEARCH_REQUIRED",
                    "supervisor_review": {
                        "status": "NEXT_RESEARCH_REQUIRED",
                        "rationale": (
                            "SUPERVISOR_PROVIDER_OR_OUTPUT_ERROR:"
                            "StructuredProviderUnavailable:"
                            f"COLLABORATION_RESPONSE_PENDING:{request_id}"
                        ),
                    },
                },
            )
            _write_json(
                provider / "requests" / f"{request_id}.json",
                {"request_id": request_id},
            )
            with patch(
                "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
                return_value=False,
            ):
                result = run_operational_acceptance_phases(
                    repo_root=repo,
                    output_root=repo / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )

        self.assertEqual(
            result["blockers"], ["PHASE101_C06_COLLABORATION_PENDING"]
        )
        self.assertEqual(len(calls), 1)
        attempt = result["phase_driver"]["command_attempts"][0]
        self.assertEqual(
            attempt["pending_markers"], ["COLLABORATION_RESPONSE_PENDING"]
        )
        self.assertEqual(attempt["current_collaboration_request_ids"], [request_id])

    def test_phase101_compact_stdout_finds_current_scoring_judge_wait(self):
        request_id = "COLLABREQ-" + "f" * 64

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            return subprocess.CompletedProcess(
                command,
                2,
                stdout=json.dumps(
                    {"status": "PHASE94_CURRENT_RESEARCHER_MODE_PENDING"}
                ),
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            target = (
                repo
                / "output/researcher_mode/c06"
                / CANARY_RECEIPT_DATE
                / "000660"
            )
            provider = target / "collaboration_codex_subagent_provider"
            (provider / "requests").mkdir(parents=True)
            (provider / "responses").mkdir()
            _write_json(
                target / "target_run_manifest.json",
                {"status": "RESEARCH_CHECKPOINT_PENDING"},
            )
            _write_json(
                target / "component_scoring_memo_run.json",
                {
                    "status": "SCORING_MEMO_PENDING",
                    "pending_reasons": [
                        "ANALYST:PROVIDER_ERROR:"
                        f"COLLABORATION_RESPONSE_PENDING:{request_id}"
                    ],
                },
            )
            _write_json(
                provider / "requests" / f"{request_id}.json",
                {"request_id": request_id},
            )
            with patch(
                "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
                return_value=False,
            ):
                result = run_operational_acceptance_phases(
                    repo_root=repo,
                    output_root=repo / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )

        self.assertEqual(
            result["blockers"], ["PHASE101_C06_COLLABORATION_PENDING"]
        )
        attempt = result["phase_driver"]["command_attempts"][0]
        self.assertEqual(
            attempt["pending_markers"], ["COLLABORATION_RESPONSE_PENDING"]
        )
        self.assertEqual(attempt["current_collaboration_request_ids"], [request_id])

    def test_phase101_compact_stdout_finds_current_stagecourt_wait(self):
        request_id = "COLLABREQ-" + "1" * 64

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            return subprocess.CompletedProcess(
                command,
                2,
                stdout=json.dumps(
                    {"status": "PHASE94_CURRENT_RESEARCHER_MODE_PENDING"}
                ),
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            target = (
                repo
                / "output/researcher_mode/c06"
                / CANARY_RECEIPT_DATE
                / "000660"
            )
            provider = target / "collaboration_codex_subagent_provider"
            (provider / "requests").mkdir(parents=True)
            (provider / "responses").mkdir()
            _write_json(
                target / "target_run_manifest.json",
                {"status": "RESEARCH_CHECKPOINT_PENDING"},
            )
            _write_json(
                target / "stagecourt.json",
                {
                    "status": "PENDING_RESEARCH",
                    "reason_codes": [
                        "STAGE_GATE_MAPPING_PROVIDER_OR_OUTPUT_ERROR:"
                        "StructuredProviderUnavailable:"
                        f"COLLABORATION_RESPONSE_PENDING:{request_id}"
                    ],
                },
            )
            _write_json(
                provider / "requests" / f"{request_id}.json",
                {"request_id": request_id},
            )
            with patch(
                "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
                return_value=False,
            ):
                result = run_operational_acceptance_phases(
                    repo_root=repo,
                    output_root=repo / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )

        self.assertEqual(
            result["blockers"], ["PHASE101_C06_COLLABORATION_PENDING"]
        )
        attempt = result["phase_driver"]["command_attempts"][0]
        self.assertEqual(
            attempt["pending_markers"], ["COLLABORATION_RESPONSE_PENDING"]
        )
        self.assertEqual(attempt["current_collaboration_request_ids"], [request_id])

    def test_phase101_current_leaf_with_existing_response_is_not_external_wait(self):
        request_id = "COLLABREQ-" + "b" * 64

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            return subprocess.CompletedProcess(
                command,
                2,
                stdout=json.dumps(
                    {"status": "PHASE94_CURRENT_RESEARCHER_MODE_PENDING"}
                ),
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            target = (
                repo
                / "output/researcher_mode/c06"
                / CANARY_RECEIPT_DATE
                / "005930"
            )
            provider = target / "collaboration_codex_subagent_provider"
            (provider / "requests").mkdir(parents=True)
            (provider / "responses").mkdir()
            _write_json(
                target / "target_run_manifest.json",
                {"status": "RESEARCH_CHECKPOINT_PENDING"},
            )
            _write_json(
                target / "fact_extraction_result.json",
                {
                    "status": "FACT_EXTRACTION_PENDING",
                    "pending_reasons": [
                        "FACT_EXTRACTION_PROVIDER_OR_OUTPUT_ERROR:"
                        f"COLLABORATION_RESPONSE_PENDING:{request_id}"
                    ],
                },
            )
            _write_json(
                provider / "requests" / f"{request_id}.json",
                {"request_id": request_id},
            )
            _write_json(
                provider / "responses" / f"{request_id}.json",
                {"request_id": request_id, "response_id": "COLLABRESP-" + "c" * 64},
            )
            with patch(
                "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
                return_value=False,
            ):
                result = run_operational_acceptance_phases(
                    repo_root=repo,
                    output_root=repo / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )

        self.assertEqual(result["blockers"], ["PHASE101_C06_CANONICAL_RUN_PENDING"])
        attempt = result["phase_driver"]["command_attempts"][0]
        self.assertEqual(attempt["pending_markers"], [])
        self.assertNotIn("current_collaboration_request_ids", attempt)

    def test_phase101_hard_runner_error_is_not_masked_by_an_older_open_request(self):
        request_id = "COLLABREQ-" + "d" * 64

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            return subprocess.CompletedProcess(
                command,
                1,
                stdout="",
                stderr="ValueError: authoritative fact ledger source checkpoint binding drift",
            )

        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            target = (
                repo
                / "output/researcher_mode/c06"
                / CANARY_RECEIPT_DATE
                / "005930"
            )
            provider = target / "collaboration_codex_subagent_provider"
            (provider / "requests").mkdir(parents=True)
            (provider / "responses").mkdir()
            _write_json(
                target / "target_run_manifest.json",
                {"status": "RESEARCH_CHECKPOINT_PENDING"},
            )
            _write_json(
                target / "source_graph_checkpoint.json",
                {
                    "status": "CANDIDATE_RANKING_PENDING",
                    "pending_reasons": [
                        "PARTITION_0:RANKING_PROVIDER_ERROR:"
                        f"COLLABORATION_RESPONSE_PENDING:{request_id}"
                    ],
                },
            )
            _write_json(
                provider / "requests" / f"{request_id}.json",
                {"request_id": request_id},
            )
            with patch(
                "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
                return_value=False,
            ):
                result = run_operational_acceptance_phases(
                    repo_root=repo,
                    output_root=repo / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )

        self.assertEqual(result["blockers"], ["PHASE101_C06_CANONICAL_RUN_PENDING"])
        attempt = result["phase_driver"]["command_attempts"][0]
        self.assertEqual(attempt["exit_code"], 1)
        self.assertEqual(attempt["pending_markers"], [])
        self.assertNotIn("current_collaboration_request_ids", attempt)

    def test_phase101_missing_receipts_runs_research_export_verify_in_order(self):
        modules: list[str] = []

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            module = command[2]
            modules.append(module)
            code = 2 if module == "e2r.cli.select_e2r_v6_cross_archetype_canaries" else 0
            return subprocess.CompletedProcess(
                command,
                code,
                stdout=json.dumps({"status": "PASS" if code == 0 else "SELECTION_PENDING"}),
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp, patch(
            "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
            side_effect=(False, True),
        ), patch(
            "e2r.production.v6_operational_acceptance._phase105_live_inputs_ready",
            return_value=True,
        ):
            result = run_operational_acceptance_phases(
                repo_root=tmp,
                output_root=Path(tmp) / "driver",
                as_of_date="2026-08-09",
                research_provider="codex-collaboration",
                command_runner=runner,
                test_mode=True,
            )

        self.assertEqual(result["blockers"], ["PHASE105_ISSUER_PROFILE_PENDING"])
        self.assertEqual(
            modules[:3],
            [
                "e2r.cli.run_e2r_researcher_mode_until_pass",
                "e2r.cli.export_e2r_v6_tracked_receipts",
                "e2r.cli.verify_e2r_v6_tracked_receipts",
            ],
        )
        self.assertEqual(
            modules[3:5],
            [
                "e2r.cli.select_e2r_v6_cross_archetype_canaries",
                "e2r.cli.materialize_e2r_v6_issuer_business_profiles",
            ],
        )

    def test_phase_driver_runs_reviewer_and_full_tests_only_after_all_leaves_validate(self):
        compiler_calls: list[dict[str, object]] = []

        def compiler(**kwargs: object) -> dict[str, object]:
            compiler_calls.append(dict(kwargs))
            return {
                "schema_version": "e2r_v6_operational_acceptance_v1",
                "status": OPERATIONAL_ACCEPTANCE_TEST_PASS,
                "blockers": [],
                "reviewer_gate": {"status": REVIEWER_GATE_PASS},
                "full_test_result": {"status": "PASS", "executed_test_count": 1},
            }

        def no_command(_argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            raise AssertionError("validated leaves must not rerun canonical CLIs")

        ready_patches = (
            patch("e2r.production.v6_operational_acceptance._phase101_receipts_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase105_selection_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase106_canaries_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase107_census_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase108_static_audit_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase108_self_repair_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase102_reproduction_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase103_clean_clone_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase104_lifecycle_ready", return_value=True),
        )
        with tempfile.TemporaryDirectory() as tmp:
            for active in ready_patches:
                active.start()
            try:
                result = run_operational_acceptance_phases(
                    repo_root=tmp,
                    output_root=Path(tmp) / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=no_command,
                    acceptance_compiler=compiler,
                    test_mode=True,
                )
            finally:
                for active in reversed(ready_patches):
                    active.stop()

        self.assertEqual(len(compiler_calls), 1)
        step_by_id = {
            row["step_id"]: row for row in result["phase_driver"]["steps"]
        }
        self.assertEqual(step_by_id["reviewer_gate"]["status"], "VALIDATED_CHECKPOINT")
        self.assertEqual(step_by_id["full_tests"]["status"], "VALIDATED_CHECKPOINT")
        self.assertEqual(
            step_by_id["full_tests"]["action"],
            "EXECUTED_AFTER_ALL_LEAVES_READY",
        )

    def test_phase102_103_clean_clone_attempt_is_exact_and_fail_closed(self):
        for exit_code in (0, 2):
            with self.subTest(exit_code=exit_code), tempfile.TemporaryDirectory() as tmp:
                repo = Path(tmp).resolve()
                (repo / FINAL_ROOT_RELATIVE).mkdir(parents=True)
                calls: list[list[str]] = []

                def runner(
                    argv: object,
                    _cwd: Path,
                ) -> subprocess.CompletedProcess[str]:
                    command = list(argv)  # type: ignore[arg-type]
                    calls.append(command)
                    return subprocess.CompletedProcess(
                        command,
                        exit_code,
                        stdout=json.dumps(
                            {
                                "status": (
                                    CLEAN_CLONE_REPRODUCTION_PASS
                                    if exit_code == 0
                                    else "E2R_V6_CLEAN_CLONE_REPRODUCTION_FAIL"
                                )
                            }
                        ),
                        stderr="",
                    )

                patches = (
                    patch(
                        "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
                        return_value=True,
                    ),
                    patch(
                        "e2r.production.v6_operational_acceptance._phase105_selection_ready",
                        return_value=True,
                    ),
                    patch(
                        "e2r.production.v6_operational_acceptance._phase106_canaries_ready",
                        return_value=True,
                    ),
                    patch(
                        "e2r.production.v6_operational_acceptance._phase107_census_ready",
                        return_value=True,
                    ),
                    patch(
                        "e2r.production.v6_operational_acceptance._phase108_static_audit_ready",
                        return_value=True,
                    ),
                )
                for active in patches:
                    active.start()
                try:
                    result = run_operational_acceptance_phases(
                        repo_root=repo,
                        output_root=repo / "driver",
                        as_of_date="2026-08-09",
                        research_provider="codex-collaboration",
                        command_runner=runner,
                        test_mode=True,
                    )
                finally:
                    for active in reversed(patches):
                        active.stop()

                expected_argv = [
                    "/usr/bin/python3",
                    "-I",
                    "-S",
                    "-B",
                    str(repo / "scripts/run_e2r_v6_clean_clone_reproduction.py"),
                    "--repo-root",
                    str(repo),
                ]
                self.assertEqual(calls, [expected_argv])
                self.assertEqual(
                    result["blockers"],
                    ["PHASE102_103_CLEAN_CLONE_REPRODUCTION_PENDING"],
                )
                attempt = result["phase_driver"]["command_attempts"][0]
                self.assertEqual(attempt["step_id"], "clean_clone_reproduction")
                self.assertEqual(attempt["argv"], expected_argv)
                self.assertFalse(attempt["shell"])
                self.assertNotIn("-m", attempt["argv"])
                self.assertNotIn("reviewer_gate", result)

    def test_phase108_static_audit_runs_canonical_cli_before_clean_clone(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp).resolve()
            (repo / FINAL_ROOT_RELATIVE).mkdir(parents=True)
            calls: list[list[str]] = []

            def runner(
                argv: object,
                _cwd: Path,
            ) -> subprocess.CompletedProcess[str]:
                command = list(argv)  # type: ignore[arg-type]
                calls.append(command)
                return subprocess.CompletedProcess(command, 2, stdout="{}", stderr="")

            patches = (
                patch("e2r.production.v6_operational_acceptance._phase101_receipts_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase105_selection_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase106_canaries_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase107_census_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase108_static_audit_ready", return_value=False),
            )
            for active in patches:
                active.start()
            try:
                result = run_operational_acceptance_phases(
                    repo_root=repo,
                    output_root=repo / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )
            finally:
                for active in reversed(patches):
                    active.stop()

        self.assertEqual(
            calls,
            [
                [
                    sys.executable,
                    "-m",
                    "e2r.cli.compile_e2r_v6_production_static_audit",
                    "--repo-root",
                    str(repo),
                    "--final-root",
                    str(FINAL_ROOT_RELATIVE),
                ]
            ],
        )
        self.assertEqual(
            result["blockers"],
            ["PHASE108_PRODUCTION_STATIC_AUDIT_PENDING"],
        )

    def test_phase108_self_repair_runs_after_clean_clone_and_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp).resolve()
            (repo / FINAL_ROOT_RELATIVE).mkdir(parents=True)
            calls: list[list[str]] = []

            def runner(
                argv: object,
                _cwd: Path,
            ) -> subprocess.CompletedProcess[str]:
                command = list(argv)  # type: ignore[arg-type]
                calls.append(command)
                return subprocess.CompletedProcess(command, 2, stdout="{}", stderr="")

            patches = (
                patch("e2r.production.v6_operational_acceptance._phase101_receipts_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase105_selection_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase106_canaries_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase107_census_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase108_static_audit_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase102_reproduction_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase103_clean_clone_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase108_self_repair_ready", return_value=False),
            )
            for active in patches:
                active.start()
            try:
                result = run_operational_acceptance_phases(
                    repo_root=repo,
                    output_root=repo / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )
            finally:
                for active in reversed(patches):
                    active.stop()

        self.assertEqual(
            calls,
            [[
                sys.executable,
                "-m",
                "e2r.cli.compile_e2r_v6_operational_self_repair",
                "--repo-root",
                str(repo),
                "--final-root",
                str(FINAL_ROOT_RELATIVE),
            ]],
        )
        self.assertEqual(
            result["blockers"],
            ["PHASE108_OPERATIONAL_SELF_REPAIR_PENDING"],
        )

    def test_phase_subprocess_runs_exact_argv_with_shell_disabled(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp).resolve()
            argv = [
                "/usr/bin/python3",
                "-I",
                "-S",
                "-B",
                str(repo / "scripts/run_e2r_v6_clean_clone_reproduction.py"),
                "--repo-root",
                str(repo),
            ]
            completed = subprocess.CompletedProcess(
                argv,
                0,
                stdout="{}",
                stderr="",
            )
            with patch(
                "e2r.production.v6_operational_acceptance.subprocess.run",
                return_value=completed,
            ) as run:
                self.assertIs(_run_phase_subprocess(argv, repo), completed)

        positional, keyword = run.call_args
        self.assertEqual(positional, (argv,))
        self.assertIs(keyword["shell"], False)
        self.assertEqual(keyword["cwd"], repo)

    def test_phase102_103_clean_clone_pass_is_revalidated_then_continues(self):
        compiler_calls: list[dict[str, object]] = []

        def compiler(**kwargs: object) -> dict[str, object]:
            compiler_calls.append(dict(kwargs))
            return {
                "schema_version": "e2r_v6_operational_acceptance_v1",
                "status": OPERATIONAL_ACCEPTANCE_TEST_PASS,
                "blockers": [],
                "reviewer_gate": {"status": REVIEWER_GATE_PASS},
                "full_test_result": {"status": "PASS", "executed_test_count": 1},
            }

        with tempfile.TemporaryDirectory() as tmp:
            fixture = _Fixture(Path(tmp))
            repo = fixture.repo.resolve()
            relative_leaves = (
                Path("clean_clone/receipt_recompute_result.json"),
                Path("clean_clone/tracked_readiness_result.json"),
                Path("clean_clone/test_result.json"),
                Path("clean_clone_reproduction.json"),
            )
            sealed_bytes = {
                relative: (fixture.final / relative).read_bytes()
                for relative in relative_leaves
            }
            for relative in reversed(relative_leaves):
                (fixture.final / relative).unlink()
            (fixture.final / "clean_clone").rmdir()
            calls: list[list[str]] = []

            def runner(
                argv: object,
                _cwd: Path,
            ) -> subprocess.CompletedProcess[str]:
                command = list(argv)  # type: ignore[arg-type]
                calls.append(command)
                for relative, encoded in sealed_bytes.items():
                    destination = fixture.final / relative
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_bytes(encoded)
                return subprocess.CompletedProcess(
                    command,
                    0,
                    stdout=json.dumps(
                        {"status": CLEAN_CLONE_REPRODUCTION_PASS}
                    ),
                    stderr="",
                )

            patches = (
                patch(
                    "e2r.production.v6_operational_acceptance._phase101_receipts_ready",
                    return_value=True,
                ),
                patch(
                    "e2r.production.v6_operational_acceptance._phase105_selection_ready",
                    return_value=True,
                ),
                patch(
                    "e2r.production.v6_operational_acceptance._phase106_canaries_ready",
                    return_value=True,
                ),
                patch(
                    "e2r.production.v6_operational_acceptance._phase107_census_ready",
                    return_value=True,
                ),
                patch(
                    "e2r.production.v6_operational_acceptance._phase108_static_audit_ready",
                    return_value=True,
                ),
                patch(
                    "e2r.production.v6_operational_acceptance._phase108_self_repair_ready",
                    return_value=True,
                ),
                patch(
                    "e2r.production.v6_operational_acceptance._phase104_lifecycle_ready",
                    return_value=True,
                ),
            )
            for active in patches:
                active.start()
            try:
                result = run_operational_acceptance_phases(
                    repo_root=repo,
                    output_root=repo / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    acceptance_compiler=compiler,
                    test_mode=True,
                )
            finally:
                for active in reversed(patches):
                    active.stop()

        expected_argv = [
            "/usr/bin/python3",
            "-I",
            "-S",
            "-B",
            str(repo / "scripts/run_e2r_v6_clean_clone_reproduction.py"),
            "--repo-root",
            str(repo),
        ]
        self.assertEqual(calls, [expected_argv])
        self.assertEqual(len(compiler_calls), 1)
        self.assertEqual(result["status"], OPERATIONAL_ACCEPTANCE_TEST_PASS)
        step_ids = [row["step_id"] for row in result["phase_driver"]["steps"]]
        self.assertLess(
            step_ids.index("clean_clone_reproduction"),
            step_ids.index("clean_clone_verification"),
        )
        self.assertLess(
            step_ids.index("clean_clone_verification"),
            step_ids.index("artifact_lifecycle"),
        )

    def test_phase104_compiles_provider_audit_before_lifecycle_manifest(self):
        calls: list[list[str]] = []

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            return subprocess.CompletedProcess(
                command,
                2,
                stdout=json.dumps(
                    {"status": "E2R_V6_PROVIDER_RUNTIME_AUDIT_FAIL"}
                ),
                stderr="",
            )

        ready_patches = (
            patch("e2r.production.v6_operational_acceptance._phase101_receipts_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase105_selection_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase106_canaries_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase107_census_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase108_static_audit_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase108_self_repair_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase102_reproduction_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase103_clean_clone_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase104_lifecycle_ready", return_value=False),
            patch("e2r.production.v6_operational_acceptance._phase104_provider_audit_ready", return_value=False),
        )
        with tempfile.TemporaryDirectory() as tmp:
            for active in ready_patches:
                active.start()
            try:
                result = run_operational_acceptance_phases(
                    repo_root=tmp,
                    output_root=Path(tmp) / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )
            finally:
                for active in reversed(ready_patches):
                    active.stop()

        self.assertEqual(
            result["blockers"],
            ["PHASE104_PROVIDER_RUNTIME_AUDIT_PENDING"],
        )
        self.assertEqual(len(calls), 1)
        self.assertEqual(
            calls[0][1:3],
            ["-m", "e2r.cli.compile_e2r_v6_provider_runtime_audit"],
        )

    def test_phase_driver_returns_immediately_on_census_collaboration_wait(self):
        calls: list[list[str]] = []
        stdout = json.dumps(
            {
                "status": "SOURCE_PENDING",
                "blockers": ["COLLABORATION_RESPONSE_PENDING"],
                "score_or_stage_authority": False,
            }
        )

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            return subprocess.CompletedProcess(command, 3, stdout=stdout, stderr="")

        patches = (
            patch("e2r.production.v6_operational_acceptance._phase101_receipts_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase105_selection_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase106_canaries_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase107_census_ready", return_value=False),
        )
        with tempfile.TemporaryDirectory() as tmp:
            for active in patches:
                active.start()
            try:
                result = run_operational_acceptance_phases(
                    repo_root=tmp,
                    output_root=Path(tmp) / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )
            finally:
                for active in reversed(patches):
                    active.stop()

        self.assertEqual(result["blockers"], ["PHASE107_SOURCE_OR_PROVIDER_PENDING"])
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0][1:3], ["-m", "e2r.cli.run_e2r_census_mode"])
        self.assertIn("--resume", calls[0])
        self.assertNotIn("reviewer_gate", result)
        attempt = result["phase_driver"]["command_attempts"][0]
        self.assertEqual(
            attempt["pending_markers"],
            ["COLLABORATION_RESPONSE_PENDING", "SOURCE_PENDING"],
        )

    def test_phase107_deep_collaboration_wait_uses_exact_cli_once(self):
        calls: list[list[str]] = []

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            if "e2r.cli.run_e2r_census_mode" in command:
                # The initial Census can fail solely because its natural L5
                # receipt is still absent.  A fully materialized live root is
                # enough to enter the dedicated repair runner once.
                return subprocess.CompletedProcess(command, 2, stdout="{}", stderr="")
            return subprocess.CompletedProcess(
                command,
                3,
                stdout=json.dumps(
                    {
                        "status": "E2R_V6_CURRENT_KRX_DEEP_RECEIPT_RUN_PENDING",
                        "external_wait_marker": "COLLABORATION_RESPONSE_PENDING",
                        "blockers": ["COLLABORATION_RESPONSE_PENDING"],
                        "score_or_stage_authority": False,
                    }
                ),
                stderr="",
            )

        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp).resolve()
            (repo / FINAL_ROOT_RELATIVE).mkdir(parents=True)
            live = repo / "output/live_materialization/2026-08-09"
            live.mkdir(parents=True)
            patches = (
                patch("e2r.production.v6_operational_acceptance._phase101_receipts_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase105_selection_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase106_canaries_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase107_census_ready", return_value=False),
                patch("e2r.production.v6_operational_acceptance._phase107_deep_receipts_ready", return_value=False),
            )
            for active in patches:
                active.start()
            try:
                result = run_operational_acceptance_phases(
                    repo_root=repo,
                    output_root=repo / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )
            finally:
                for active in reversed(patches):
                    active.stop()

        self.assertEqual(
            result["blockers"],
            ["PHASE107_DEEP_RECEIPT_COLLABORATION_PENDING"],
        )
        self.assertEqual(len(calls), 2)
        expected_deep = [
            sys.executable,
            "-m",
            "e2r.cli.run_e2r_v6_current_krx_deep_receipts_until_pass",
            "--as-of-date",
            "2026-08-09",
            "--repo-root",
            str(repo),
            "--live-root",
            str(live),
            "--work-root",
            str(repo / "driver/phase107"),
            "--deep-receipt-root",
            str(repo / "driver/current_krx_census_run/deep_receipts"),
            "--live-materialization-authorized",
            "true",
            "--checkpoint-resume",
            "true",
            "--research-provider",
            "codex-collaboration",
            "--fact-documents-per-call",
            "3",
        ]
        self.assertEqual(calls[1], expected_deep)
        self.assertEqual(calls[1].count("--research-provider"), 1)
        self.assertEqual(
            [row["step_id"] for row in result["phase_driver"]["command_attempts"]],
            ["current_krx_census", "current_krx_natural_deep_receipt"],
        )
        self.assertEqual(
            len(result["phase_driver"]["command_attempts"]),
            len(calls),
        )
        self.assertFalse(result["score_or_stage_authority"])

    def test_phase107_deep_zero_exit_without_valid_receipt_fails_closed(self):
        calls: list[list[str]] = []

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            return subprocess.CompletedProcess(command, 0, stdout="{}", stderr="")

        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp).resolve()
            (repo / FINAL_ROOT_RELATIVE).mkdir(parents=True)
            (repo / "output/live_materialization/2026-08-09").mkdir(parents=True)
            patches = (
                patch("e2r.production.v6_operational_acceptance._phase101_receipts_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase105_selection_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase106_canaries_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase107_census_ready", return_value=False),
                patch("e2r.production.v6_operational_acceptance._phase107_deep_receipts_ready", side_effect=(False, False)),
            )
            for active in patches:
                active.start()
            try:
                result = run_operational_acceptance_phases(
                    repo_root=repo,
                    output_root=repo / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )
            finally:
                for active in reversed(patches):
                    active.stop()

        self.assertEqual(result["blockers"], ["PHASE107_DEEP_RECEIPT_PENDING"])
        self.assertEqual(len(calls), 2)
        self.assertNotIn("e2r.cli.compile_e2r_v6_current_krx_census", calls[-1])

    def test_phase107_valid_deep_receipt_is_rechecked_before_census_publish(self):
        calls: list[list[str]] = []

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            return subprocess.CompletedProcess(command, 0, stdout="{}", stderr="")

        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp).resolve()
            (repo / FINAL_ROOT_RELATIVE).mkdir(parents=True)
            (repo / "output/live_materialization/2026-08-09").mkdir(parents=True)
            patches = (
                patch("e2r.production.v6_operational_acceptance._phase101_receipts_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase105_selection_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase106_canaries_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase107_census_ready", side_effect=(False, False, True)),
                patch("e2r.production.v6_operational_acceptance._phase107_deep_receipts_ready", side_effect=(False, True)),
                patch("e2r.production.v6_operational_acceptance._phase108_static_audit_ready", return_value=True),
                patch("e2r.production.v6_operational_acceptance._phase102_reproduction_ready", return_value=False),
                patch("e2r.production.v6_operational_acceptance._phase103_clean_clone_ready", return_value=False),
            )
            for active in patches:
                active.start()
            try:
                result = run_operational_acceptance_phases(
                    repo_root=repo,
                    output_root=repo / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )
            finally:
                for active in reversed(patches):
                    active.stop()

        modules = [
            command[command.index("-m") + 1]
            for command in calls
            if "-m" in command
        ]
        self.assertEqual(
            modules[:3],
            [
                "e2r.cli.run_e2r_census_mode",
                "e2r.cli.run_e2r_v6_current_krx_deep_receipts_until_pass",
                "e2r.cli.compile_e2r_v6_current_krx_census",
            ],
        )
        self.assertEqual(
            result["blockers"],
            ["PHASE102_103_CLEAN_CLONE_REPRODUCTION_PENDING"],
        )

    def test_phase106_collaboration_wait_returns_before_census(self):
        calls: list[list[str]] = []
        stdout = json.dumps(
            {
                "status": "E2R_V6_CURRENT_LIVE_CANARY_RUN_PENDING",
                "blockers": ["COLLABORATION_RESPONSE_PENDING"],
                "external_wait_marker": "COLLABORATION_RESPONSE_PENDING",
                "pending_requests": [{"request_id": "COLLABREQ-test"}],
            }
        )

        def runner(argv: object, _cwd: Path) -> subprocess.CompletedProcess[str]:
            command = list(argv)  # type: ignore[arg-type]
            calls.append(command)
            return subprocess.CompletedProcess(command, 3, stdout=stdout, stderr="")

        patches = (
            patch("e2r.production.v6_operational_acceptance._phase101_receipts_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase105_selection_ready", return_value=True),
            patch("e2r.production.v6_operational_acceptance._phase106_canaries_ready", return_value=False),
        )
        with tempfile.TemporaryDirectory() as tmp:
            for active in patches:
                active.start()
            try:
                result = run_operational_acceptance_phases(
                    repo_root=tmp,
                    output_root=Path(tmp) / "driver",
                    as_of_date="2026-08-09",
                    research_provider="codex-collaboration",
                    command_runner=runner,
                    test_mode=True,
                )
            finally:
                for active in reversed(patches):
                    active.stop()

        self.assertEqual(
            result["blockers"],
            ["PHASE106_LIVE_CANARY_COLLABORATION_PENDING"],
        )
        self.assertEqual(len(calls), 1)
        self.assertEqual(
            calls[0][1:3],
            ["-m", "e2r.cli.run_e2r_v6_current_live_canaries_until_pass"],
        )
        self.assertNotIn("e2r.cli.run_e2r_census_mode", calls[0])
        self.assertEqual(
            calls[0][calls[0].index("--fact-documents-per-call") + 1],
            "3",
        )
        self.assertEqual(
            result["phase_driver"]["command_attempts"][0]["pending_markers"],
            ["COLLABORATION_RESPONSE_PENDING"],
        )


if __name__ == "__main__":
    unittest.main()

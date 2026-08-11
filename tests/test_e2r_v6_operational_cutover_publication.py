from __future__ import annotations

import copy
from contextlib import redirect_stdout
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from e2r.cli.publish_e2r_v6_operational_cutover import main as publish_main
from e2r.cli.verify_e2r_v6_operational_cutover_publication import (
    main as verify_main,
)
from e2r.production.metadata import stable_hash
from e2r.production.v6_canary_selection import REQUIRED_ARCHETYPES
from e2r.production.v6_current_krx_census import CANONICAL_TRIGGER_LANES
from e2r.production.v6_operational_acceptance import (
    OPERATIONAL_ACCEPTANCE_PASS,
    OPERATIONAL_ACCEPTANCE_SCHEMA,
    OPERATIONAL_REVIEWER_GATE_SCHEMA,
    REVIEWER_GATE_PASS,
    REVIEWER_IDS,
    _run_full_tests,
    _terminal_publication_repository_probe,
)
from e2r.production.v6_operational_cutover_publication import (
    FINAL_CUTOVER_VERDICT,
    GATE_NAME,
    PHASE109_PUBLICATION_PASS,
    PHASE109_PUBLICATION_TEST_PASS,
    PHASE109_REVIEWER_GATE_PASS,
    PHASE109_REVIEWER_GATE_SCHEMA,
    PHASE109_VERIFICATION_FAIL,
    PHASE109_VERIFICATION_PASS,
    REPORT_FIELD_ORDER,
    REPORT_NAME,
    _build_publication,
    _compile_publication_evidence,
    _terminal_git_relationship,
    publish_operational_cutover,
    verify_operational_cutover_publication,
)
from e2r.research_brain.researcher_mode.artifact_lifecycle import (
    CLEAN_CLONE_REPRODUCTION_PASS,
    CLEAN_CLONE_REPRODUCTION_SCHEMA,
    FINAL_ROOT_RELATIVE,
)
from e2r.research_brain.researcher_mode.independent_acceptance import (
    FINAL_READY_LABEL,
    REVIEWER_GATE_PASS as LEGACY_REVIEWER_GATE_PASS,
    SCHEMA_VERSION as LEGACY_REVIEWER_GATE_SCHEMA,
)
from e2r.research_brain.researcher_mode.schemas import CANONICAL_COMPONENT_ORDER
from e2r.research_brain.researcher_mode.tracked_readiness import (
    TRACKED_READINESS_PASS,
    TRACKED_READINESS_SCHEMA,
)
from e2r.research_brain.researcher_mode.tracked_receipts import (
    PHASE101_TARGET_IDS,
    PROVIDER_ROUTE,
    VERIFICATION_PASS,
    VERIFICATION_SCHEMA,
)


HEAD = "a" * 40
PUBLICATION_HEAD = "b" * 40


def _acceptance() -> dict[str, object]:
    current_reviewers = [
        {
            "reviewer_id": reviewer_id,
            "status": "PASS",
            "critical_count_sum": 0,
            "leaf_recomputed": True,
            **(
                {
                    "metrics": {
                        "current_test_count": 6637,
                        "full_test_count_baseline": 6637,
                        "full_test_count_delta": 0,
                    }
                }
                if reviewer_id == "V"
                else {}
            ),
        }
        for reviewer_id in REVIEWER_IDS
    ]
    gate = {
        "schema_version": OPERATIONAL_REVIEWER_GATE_SCHEMA,
        "status": REVIEWER_GATE_PASS,
        "reviewer_roster": list(REVIEWER_IDS),
        "reviewers": current_reviewers,
        "failed_reviewers": [],
        "critical_count_sum": 0,
        "all_reviewers_leaf_recomputed": True,
        "one_critical_forces_failure": True,
        "production_readiness_authority": True,
    }
    test_result_core = {
        "status": "PASS",
        "executed_test_count": 6637,
        "failed_test_count": 0,
        "error_test_count": 0,
        "exit_code": 0,
        "output_hash_scope": "DETERMINISTIC_TEST_RESULT_FIELDS",
    }
    core: dict[str, object] = {
        "schema_version": OPERATIONAL_ACCEPTANCE_SCHEMA,
        "status": OPERATIONAL_ACCEPTANCE_PASS,
        "ready": True,
        "contract_test_pass": False,
        "production_readiness_authority": True,
        "phase_artifact_presence": {
            str(phase): {"complete": True, "artifacts": []}
            for phase in range(101, 109)
        },
        "reviewer_gate": gate,
        "orchestration_steps": [],
        "full_test_result": {
            **test_result_core,
            "output_hash": stable_hash(test_result_core),
        },
        "repository_provenance": {
            "canonical_repository": True,
            "origin_main_matches_head": True,
            "worktree_clean": True,
            "all_acceptance_artifacts_tracked_at_head": True,
        },
        "critical_counts": {},
        "critical_count_sum": 0,
        "blockers": [],
        "fixed_retry_count_is_completion_authority": False,
        "score_or_stage_authority": False,
        "investment_recommendation_emitted": False,
        "test_mode": False,
    }
    return {**core, "acceptance_hash": stable_hash(core)}


def _legacy_gate() -> dict[str, object]:
    reviewers = [
        {
            "reviewer_id": reviewer_id,
            "status": "PASS",
            "critical_count_sum": 0,
            "detector_run_count": 1,
            "detector_pass_count": 1,
        }
        for reviewer_id in "ABCDEFGHIJ"
    ]
    return {
        "schema_version": LEGACY_REVIEWER_GATE_SCHEMA,
        "status": LEGACY_REVIEWER_GATE_PASS,
        "reviewer_count": 10,
        "reviewer_roster": list("ABCDEFGHIJ"),
        "reviewers": reviewers,
        "failed_reviewers": [],
        "critical_count_sum": 0,
        "blockers": [],
        "all_reviewers_independently_recomputed": True,
        "one_critical_forces_failure": True,
        "production_readiness_authority": True,
        "exact_verdict": FINAL_READY_LABEL,
    }


def _target_result(target_id: str, company_name: str) -> dict[str, object]:
    vector = {
        component: float(index)
        for index, component in enumerate(CANONICAL_COMPONENT_ORDER, start=1)
    }
    return {
        "target_id": target_id,
        "company_name": company_name,
        "component_score_vector": vector,
        "total_score": sum(vector.values()),
        "canonical_stage": "2",
    }


def _evidence() -> dict[str, object]:
    canaries = {
        archetype: {
            "target_id": f"T{index:02d}",
            "company_name": f"회사 {index}",
            "total_score": 50.0 + index,
            "canonical_stage": "3-Yellow",
        }
        for index, archetype in enumerate(REQUIRED_ARCHETYPES, start=1)
    }
    return {
        "test_mode": False,
        "verified_cutover_head": HEAD,
        "acceptance": _acceptance(),
        "reviewer_gate": _acceptance()["reviewer_gate"],
        "legacy_gate": _legacy_gate(),
        "phase101_verification": {
            "schema_version": VERIFICATION_SCHEMA,
            "status": VERIFICATION_PASS,
            "critical_count_sum": 0,
            "target_ids": list(PHASE101_TARGET_IDS),
            "offline": True,
        },
        "samsung_result": _target_result("005930", "삼성전자"),
        "hynix_result": _target_result("000660", "SK하이닉스"),
        "canary_results": canaries,
        "census": {
            "universe_counts": {
                "eligible_universe_count": 6,
                "stage_map_row_count": 6,
                "real_krx_universe_source": True,
            },
            "trigger_lane_counts": {
                lane: 1 for lane in CANONICAL_TRIGGER_LANES
            },
            "depth_counts": {f"L{level}": 1 for level in range(6)},
            "natural_candidate_count": 1,
            "score_stage_counts": {
                "score_valid_deep_row_count": 1,
                "final_stage_deep_row_count": 1,
                "natural_l5_completed_count": 1,
            },
        },
        "provider": {
            "route_count_scope": "PHASE101_AND_PHASE106_TRACKED_RECEIPTS",
            "expected_judge_receipt_count": 147,
            "provider_route_counts": {PROVIDER_ROUTE: 147},
            "provider_call_counts": {"COLLABORATION_CODEX": 21},
            "scored_fact_provider_lineage_counts": {"CODEX": 7},
            "provider_error_count": 0,
            "unauthorized_provider_call_count": 0,
            "local_provider_call_count": 0,
            "qwen_call_count": 0,
            "ollama_call_count": 0,
            "inherited_qwen_scored_fact_count": 0,
            "inherited_ollama_scored_fact_count": 0,
        },
        "tracked_readiness": {
            "schema_version": TRACKED_READINESS_SCHEMA,
            "status": TRACKED_READINESS_PASS,
            "ready": True,
            "offline": True,
            "production_readiness_authority": False,
            "critical_count": 0,
            "same_receipt_replay_variance": 0,
            "target_ids": sorted(PHASE101_TARGET_IDS),
        },
        "clean_clone": {
            "schema_version": CLEAN_CLONE_REPRODUCTION_SCHEMA,
            "status": CLEAN_CLONE_REPRODUCTION_PASS,
            "critical_count_sum": 0,
            "production_readiness_authority": False,
            "receipt_recompute_result_hash": "1" * 64,
            "tracked_readiness_result_hash": "2" * 64,
            "test_result_hash": "3" * 64,
        },
        "phase_evidence_index": [
            {
                "relative_path": (
                    FINAL_ROOT_RELATIVE / "README.md"
                ).as_posix(),
                "sha256": "4" * 64,
                "size_bytes": 10,
            }
        ],
    }


class _Compiler:
    def __init__(self, evidence: dict[str, object]) -> None:
        self.evidence = evidence
        self.calls: list[str | None] = []
        self.on_verify = None

    def __call__(self, _repo: Path, head: str | None) -> dict[str, object]:
        self.calls.append(head)
        value = copy.deepcopy(self.evidence)
        if head is not None and self.on_verify is not None:
            self.on_verify(value)
        return value


class OperationalCutoverPublicationTests(unittest.TestCase):
    def _repo(self, tmp: str) -> tuple[Path, Path]:
        repo = Path(tmp).resolve()
        final = repo / FINAL_ROOT_RELATIVE
        final.mkdir(parents=True)
        return repo, final

    def test_publish_and_reverify_exact_21_fields_and_a_v_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            compiler = _Compiler(_evidence())
            result = publish_operational_cutover(
                repo_root=repo,
                evidence_compiler=compiler,
                test_mode=True,
            )
            payload = json.loads((final / GATE_NAME).read_text(encoding="utf-8"))
            markdown = (final / REPORT_NAME).read_text(encoding="utf-8")
            verification = verify_operational_cutover_publication(
                repo_root=repo,
                evidence_compiler=compiler,
                test_mode=True,
            )

        self.assertEqual(result["status"], PHASE109_PUBLICATION_TEST_PASS)
        self.assertEqual(verification["status"], PHASE109_VERIFICATION_PASS)
        self.assertEqual(tuple(payload["report_field_order"]), REPORT_FIELD_ORDER)
        self.assertEqual(set(payload["report_fields"]), set(REPORT_FIELD_ORDER))
        self.assertEqual(
            payload["report_fields"]["exact_final_verdict"],
            "MEANINGFUL_E2R_OPERATIONAL_MARKET_CUTOVER_READY",
        )
        self.assertEqual(FINAL_CUTOVER_VERDICT, OPERATIONAL_ACCEPTANCE_PASS)
        self.assertEqual(
            payload["reviewer_gate"]["schema_version"],
            PHASE109_REVIEWER_GATE_SCHEMA,
        )
        self.assertEqual(payload["reviewer_gate"]["status"], PHASE109_REVIEWER_GATE_PASS)
        self.assertEqual(payload["reviewer_gate"]["reviewer_roster"], list("ABCDEFGHIJKLMNOPQRSTUV"))
        self.assertEqual(payload["reviewer_gate"]["reviewer_count"], 22)
        self.assertFalse(payload["production_readiness_authority"])
        self.assertEqual(markdown.count("\n## "), 21)
        self.assertIn("C08 current canary 결과", markdown)
        self.assertNotIn("자연 canary 결과", markdown)
        self.assertIn("first-parent", markdown)
        self.assertEqual(
            verification["publication_head_relationship"],
            "CONTRACT_TEST_INJECTED",
        )
        self.assertEqual(compiler.calls, [None, HEAD, HEAD])

    def test_component_vector_json_key_order_is_not_semantic(self):
        evidence = _evidence()
        for name in ("samsung_result", "hynix_result"):
            result = evidence[name]
            self.assertIsInstance(result, dict)
            vector = result["component_score_vector"]  # type: ignore[index]
            result["component_score_vector"] = dict(reversed(tuple(vector.items())))  # type: ignore[index,union-attr]
        evidence["test_mode"] = True
        payload, _markdown = _build_publication(evidence)
        rendered = payload["report_fields"]["samsung_result"]["component_score_vector"]
        self.assertEqual(tuple(rendered), CANONICAL_COMPONENT_ORDER)

    def test_acceptance_label_tamper_publishes_nothing(self):
        evidence = _evidence()
        acceptance = evidence["acceptance"]
        self.assertIsInstance(acceptance, dict)
        acceptance["status"] = "NOT_READY"
        core = {key: value for key, value in acceptance.items() if key != "acceptance_hash"}
        acceptance["acceptance_hash"] = stable_hash(core)
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            with self.assertRaises(ValueError):
                publish_operational_cutover(
                    repo_root=repo,
                    evidence_compiler=_Compiler(evidence),
                    test_mode=True,
                )
            self.assertFalse((final / GATE_NAME).exists())
            self.assertFalse((final / REPORT_NAME).exists())

    def test_wrong_final_verdict_constant_publishes_nothing(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            with (
                patch(
                    "e2r.production.v6_operational_cutover_publication.FINAL_CUTOVER_VERDICT",
                    "WRONG_READY_LABEL",
                ),
                self.assertRaises(RuntimeError),
            ):
                publish_operational_cutover(
                    repo_root=repo,
                    evidence_compiler=_Compiler(_evidence()),
                    test_mode=True,
                )
            self.assertFalse((final / GATE_NAME).exists())
            self.assertFalse((final / REPORT_NAME).exists())

    def test_reviewer_v_baseline_cannot_be_lowered_or_ignored(self):
        evidence = _evidence()
        acceptance = evidence["acceptance"]
        self.assertIsInstance(acceptance, dict)
        reviewer_v = acceptance["reviewer_gate"]["reviewers"][-1]  # type: ignore[index]
        reviewer_v["metrics"]["full_test_count_baseline"] = 6638
        reviewer_v["metrics"]["full_test_count_delta"] = -1
        evidence["reviewer_gate"] = copy.deepcopy(acceptance["reviewer_gate"])
        core = {key: value for key, value in acceptance.items() if key != "acceptance_hash"}
        acceptance["acceptance_hash"] = stable_hash(core)
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            with self.assertRaises(ValueError):
                publish_operational_cutover(
                    repo_root=repo,
                    evidence_compiler=_Compiler(evidence),
                    test_mode=True,
                )
            self.assertFalse((final / GATE_NAME).exists())
            self.assertFalse((final / REPORT_NAME).exists())

    def test_one_failed_reviewer_publishes_nothing(self):
        evidence = _evidence()
        legacy = evidence["legacy_gate"]
        self.assertIsInstance(legacy, dict)
        legacy["reviewers"][0]["status"] = "FAIL"  # type: ignore[index]
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            with self.assertRaises(ValueError):
                publish_operational_cutover(
                    repo_root=repo,
                    evidence_compiler=_Compiler(evidence),
                    test_mode=True,
                )
            self.assertFalse((final / GATE_NAME).exists())
            self.assertFalse((final / REPORT_NAME).exists())

    def test_current_reviewer_gate_cannot_diverge_from_acceptance(self):
        evidence = _evidence()
        current = evidence["reviewer_gate"]
        self.assertIsInstance(current, dict)
        current["reviewers"][0]["status"] = "FAIL"  # type: ignore[index]
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            with self.assertRaises(ValueError):
                publish_operational_cutover(
                    repo_root=repo,
                    evidence_compiler=_Compiler(evidence),
                    test_mode=True,
                )
            self.assertFalse((final / GATE_NAME).exists())
            self.assertFalse((final / REPORT_NAME).exists())

    def test_terminal_self_hash_row_publishes_nothing(self):
        evidence = _evidence()
        evidence["phase_evidence_index"][0]["relative_path"] = (  # type: ignore[index]
            FINAL_ROOT_RELATIVE / GATE_NAME
        ).as_posix()
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            with self.assertRaises(ValueError):
                publish_operational_cutover(
                    repo_root=repo,
                    evidence_compiler=_Compiler(evidence),
                    test_mode=True,
                )
            self.assertFalse((final / GATE_NAME).exists())
            self.assertFalse((final / REPORT_NAME).exists())

    def test_bad_raw_file_sha_or_clean_clone_status_publishes_nothing(self):
        mutations = (
            lambda evidence: evidence["phase_evidence_index"][0].__setitem__(  # type: ignore[index,union-attr]
                "sha256", "not-a-sha"
            ),
            lambda evidence: evidence["clean_clone"].__setitem__(  # type: ignore[union-attr]
                "status", "FAIL"
            ),
        )
        for mutate in mutations:
            with self.subTest(mutation=mutate), tempfile.TemporaryDirectory() as tmp:
                evidence = _evidence()
                mutate(evidence)
                repo, final = self._repo(tmp)
                with self.assertRaises(ValueError):
                    publish_operational_cutover(
                        repo_root=repo,
                        evidence_compiler=_Compiler(evidence),
                        test_mode=True,
                    )
                self.assertFalse((final / GATE_NAME).exists())
                self.assertFalse((final / REPORT_NAME).exists())

    def test_untrusted_repository_fails_before_leaf_compilation(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            with (
                patch(
                    "e2r.production.v6_operational_cutover_publication.canonical_repository_root",
                    return_value=repo,
                ),
                patch(
                    "e2r.production.v6_operational_cutover_publication._repository_identity_is_trusted",
                    return_value=False,
                ),
            ):
                with self.assertRaises(ValueError):
                    _compile_publication_evidence(repo, None)
            self.assertFalse((final / GATE_NAME).exists())
            self.assertFalse((final / REPORT_NAME).exists())

    def test_existing_terminal_symlink_is_never_replaced(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            outside = repo / "outside.json"
            outside.write_text("sentinel", encoding="utf-8")
            (final / GATE_NAME).symlink_to(outside)
            with self.assertRaises(ValueError):
                publish_operational_cutover(
                    repo_root=repo,
                    evidence_compiler=_Compiler(_evidence()),
                    test_mode=True,
                )
            self.assertEqual(outside.read_text(encoding="utf-8"), "sentinel")
            self.assertTrue((final / GATE_NAME).is_symlink())
            self.assertFalse((final / REPORT_NAME).exists())

    def test_json_and_markdown_tamper_fail_reverification(self):
        for leaf in (GATE_NAME, REPORT_NAME):
            with self.subTest(leaf=leaf), tempfile.TemporaryDirectory() as tmp:
                repo, final = self._repo(tmp)
                compiler = _Compiler(_evidence())
                publish_operational_cutover(
                    repo_root=repo,
                    evidence_compiler=compiler,
                    test_mode=True,
                )
                path = final / leaf
                path.write_bytes(
                    path.read_bytes() + (b"\n" if leaf == GATE_NAME else b"tamper\n")
                )
                result = verify_operational_cutover_publication(
                    repo_root=repo,
                    evidence_compiler=compiler,
                    test_mode=True,
                )
                self.assertEqual(result["status"], PHASE109_VERIFICATION_FAIL)
                self.assertEqual(result["critical_count_sum"], 1)

    def test_head_drift_fails_reverification(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, _final = self._repo(tmp)
            compiler = _Compiler(_evidence())
            publish_operational_cutover(
                repo_root=repo,
                evidence_compiler=compiler,
                test_mode=True,
            )

            def drift(value: dict[str, object]) -> None:
                value["verified_cutover_head"] = PUBLICATION_HEAD

            compiler.on_verify = drift
            result = verify_operational_cutover_publication(
                repo_root=repo,
                evidence_compiler=compiler,
                test_mode=True,
            )
        self.assertEqual(result["status"], PHASE109_VERIFICATION_FAIL)

    def test_terminal_swap_during_leaf_recomputation_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            compiler = _Compiler(_evidence())
            publish_operational_cutover(
                repo_root=repo,
                evidence_compiler=compiler,
                test_mode=True,
            )

            def swap(_value: dict[str, object]) -> None:
                (final / REPORT_NAME).write_text("swapped\n", encoding="utf-8")

            compiler.on_verify = swap
            result = verify_operational_cutover_publication(
                repo_root=repo,
                evidence_compiler=compiler,
                test_mode=True,
            )
        self.assertEqual(result["status"], PHASE109_VERIFICATION_FAIL)

    def test_directory_swap_during_compilation_fails_before_publish(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            moved = repo / "moved-cutover"

            def swap_compiler(_repo: Path, _head: str | None) -> dict[str, object]:
                final.rename(moved)
                final.mkdir(parents=True)
                return _evidence()

            with self.assertRaises(ValueError):
                publish_operational_cutover(
                    repo_root=repo,
                    evidence_compiler=swap_compiler,
                    test_mode=True,
                )
            self.assertFalse((final / GATE_NAME).exists())
            self.assertFalse((final / REPORT_NAME).exists())
            self.assertFalse((moved / GATE_NAME).exists())
            self.assertFalse((moved / REPORT_NAME).exists())

    def test_gate_rename_precedes_result_last_markdown_rename(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, _final = self._repo(tmp)
            destinations: list[str] = []
            real_replace = os.replace

            def recording_replace(src: object, dst: object, **kwargs: object) -> None:
                destinations.append(os.fspath(dst))
                real_replace(src, dst, **kwargs)

            with patch(
                "e2r.production.v6_operational_cutover_publication.os.replace",
                side_effect=recording_replace,
            ):
                publish_operational_cutover(
                    repo_root=repo,
                    evidence_compiler=_Compiler(_evidence()),
                    test_mode=True,
                )
        self.assertEqual(destinations, [GATE_NAME, REPORT_NAME])

    def test_final_commit_relationship_requires_exact_two_file_diff(self):
        allowed_diff = (
            (FINAL_ROOT_RELATIVE / GATE_NAME).as_posix().encode()
            + b"\0"
            + (FINAL_ROOT_RELATIVE / REPORT_NAME).as_posix().encode()
            + b"\0"
        )
        with (
            patch(
                "e2r.production.v6_operational_cutover_publication._git_text",
                side_effect=(PUBLICATION_HEAD, PUBLICATION_HEAD, HEAD),
            ),
            patch(
                "e2r.production.v6_operational_cutover_publication.subprocess.check_output",
                side_effect=(b"", allowed_diff),
            ),
        ):
            result = _terminal_git_relationship(
                Path("/repo"), verified_cutover_head=HEAD
            )
        self.assertEqual(result["current_repository_head"], PUBLICATION_HEAD)
        self.assertTrue(result["terminal_commit_verified"])
        self.assertEqual(result["relationship"], "EXACT_TERMINAL_FIRST_PARENT_COMMIT")

        with (
            patch(
                "e2r.production.v6_operational_cutover_publication._git_text",
                side_effect=(PUBLICATION_HEAD, PUBLICATION_HEAD, HEAD),
            ),
            patch(
                "e2r.production.v6_operational_cutover_publication.subprocess.check_output",
                side_effect=(b"", allowed_diff + b"src/extra.py\0"),
            ),
        ):
            with self.assertRaises(ValueError):
                _terminal_git_relationship(
                    Path("/repo"), verified_cutover_head=HEAD
                )

    def test_actual_git_first_parent_terminal_commit_relationship(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            commands = (
                ("git", "init", "-q"),
                ("git", "config", "user.name", "Phase109 Test"),
                ("git", "config", "user.email", "phase109@example.invalid"),
            )
            for command in commands:
                subprocess.run(command, cwd=repo, check=True)
            (repo / "base.txt").write_text("base\n", encoding="utf-8")
            subprocess.run(("git", "add", "base.txt"), cwd=repo, check=True)
            subprocess.run(
                ("git", "commit", "-q", "-m", "base"), cwd=repo, check=True
            )
            verified = subprocess.check_output(
                ("git", "rev-parse", "HEAD"), cwd=repo, text=True
            ).strip()
            subprocess.run(
                ("git", "update-ref", "refs/remotes/origin/main", verified),
                cwd=repo,
                check=True,
            )
            (final / GATE_NAME).write_text("{}\n", encoding="utf-8")
            (final / REPORT_NAME).write_text("report\n", encoding="utf-8")
            subprocess.run(
                ("git", "add", str(FINAL_ROOT_RELATIVE)), cwd=repo, check=True
            )
            subprocess.run(
                ("git", "commit", "-q", "-m", "terminal publication"),
                cwd=repo,
                check=True,
            )
            current = subprocess.check_output(
                ("git", "rev-parse", "HEAD"), cwd=repo, text=True
            ).strip()
            subprocess.run(
                ("git", "update-ref", "refs/remotes/origin/main", current),
                cwd=repo,
                check=True,
            )
            result = _terminal_git_relationship(
                repo, verified_cutover_head=verified
            )
        self.assertEqual(result["current_repository_head"], current)
        self.assertTrue(result["terminal_commit_verified"])

    def test_full_test_hash_ignores_wall_clock_but_binds_result_fields(self):
        outputs = (
            "Ran 1 test in 0.001s\n\nOK\nRan 6637 tests in 1.234s\n\nOK\n",
            "Ran 6637 tests in 98.765s\n\nOK\n",
        )
        completed = tuple(
            subprocess.CompletedProcess(
                ["python", "-m", "unittest"], 0, stdout=output, stderr=None
            )
            for output in outputs
        )
        with patch(
            "e2r.production.v6_operational_acceptance.subprocess.run",
            side_effect=completed,
        ):
            first = _run_full_tests(Path("/repo"))
            second = _run_full_tests(Path("/repo"))
        self.assertEqual(first, second)
        self.assertEqual(
            first["output_hash_scope"], "DETERMINISTIC_TEST_RESULT_FIELDS"
        )

        changed = subprocess.CompletedProcess(
            ["python", "-m", "unittest"],
            0,
            stdout="Ran 6638 tests in 1.234s\n\nOK\n",
            stderr=None,
        )
        with patch(
            "e2r.production.v6_operational_acceptance.subprocess.run",
            return_value=changed,
        ):
            different = _run_full_tests(Path("/repo"))
        self.assertNotEqual(first["output_hash"], different["output_hash"])

    def test_operational_probe_accepts_only_exact_terminal_first_parent_commit(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            (final / GATE_NAME).write_text("{}", encoding="utf-8")
            (final / REPORT_NAME).write_text("report", encoding="utf-8")
            allowed_diff = (
                (FINAL_ROOT_RELATIVE / GATE_NAME).as_posix().encode()
                + b"\0"
                + (FINAL_ROOT_RELATIVE / REPORT_NAME).as_posix().encode()
                + b"\0"
            )

            def git_output(command: list[str], **_kwargs: object) -> object:
                joined = " ".join(command)
                if "diff-tree" in command:
                    return allowed_diff
                if "--show-toplevel" in command:
                    return str(repo)
                if command[-1] == "HEAD":
                    return PUBLICATION_HEAD
                if "refs/remotes/origin/main" in command:
                    return PUBLICATION_HEAD
                if "--porcelain=v1" in command:
                    return b""
                if command[-1] == "HEAD^":
                    return HEAD
                raise AssertionError(joined)

            with (
                patch(
                    "e2r.production.v6_operational_acceptance.canonical_repository_root",
                    return_value=repo,
                ),
                patch(
                    "e2r.production.v6_operational_acceptance._tracked_at_head",
                    return_value=True,
                ),
                patch(
                    "e2r.production.v6_operational_acceptance.subprocess.check_output",
                    side_effect=git_output,
                ),
            ):
                passed = _terminal_publication_repository_probe(
                    repo, (repo / "artifact.json",), verified_head=HEAD
                )
            self.assertTrue(all(passed.values()))

            def extra_output(command: list[str], **kwargs: object) -> object:
                value = git_output(command, **kwargs)
                if "diff-tree" in command:
                    return value + b"src/extra.py\0"  # type: ignore[operator]
                return value

            with (
                patch(
                    "e2r.production.v6_operational_acceptance.canonical_repository_root",
                    return_value=repo,
                ),
                patch(
                    "e2r.production.v6_operational_acceptance._tracked_at_head",
                    return_value=True,
                ),
                patch(
                    "e2r.production.v6_operational_acceptance.subprocess.check_output",
                    side_effect=extra_output,
                ),
            ):
                failed = _terminal_publication_repository_probe(
                    repo, (repo / "artifact.json",), verified_head=HEAD
                )
            self.assertFalse(any(failed.values()))

    def test_production_verifier_reports_actual_committed_head_separately(self):
        evidence = _evidence()
        payload, markdown = _build_publication(evidence)
        encoded = json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
            allow_nan=False,
        ) + "\n"
        with tempfile.TemporaryDirectory() as tmp:
            repo, final = self._repo(tmp)
            (final / GATE_NAME).write_text(encoded, encoding="utf-8")
            (final / REPORT_NAME).write_bytes(markdown)
            with (
                patch(
                    "e2r.production.v6_operational_cutover_publication._compile_publication_evidence",
                    return_value=copy.deepcopy(evidence),
                ),
                patch(
                    "e2r.production.v6_operational_cutover_publication._terminal_git_relationship",
                    return_value={
                        "current_repository_head": PUBLICATION_HEAD,
                        "relationship": "EXACT_TERMINAL_FIRST_PARENT_COMMIT",
                        "current_head_matches_verified_cutover_head": False,
                        "terminal_commit_verified": True,
                    },
                ),
            ):
                result = verify_operational_cutover_publication(repo_root=repo)
        self.assertEqual(result["status"], PHASE109_VERIFICATION_PASS)
        self.assertEqual(result["verified_cutover_head"], HEAD)
        self.assertEqual(result["current_repository_head"], PUBLICATION_HEAD)
        self.assertTrue(result["terminal_commit_verified"])

    def test_publish_and_verify_cli_exit_contracts(self):
        with (
            patch(
                "e2r.cli.publish_e2r_v6_operational_cutover.publish_operational_cutover",
                return_value={"status": PHASE109_PUBLICATION_PASS},
            ),
            redirect_stdout(io.StringIO()) as output,
        ):
            self.assertEqual(publish_main(["--repo-root", "/repo"]), 0)
            self.assertEqual(
                json.loads(output.getvalue())["status"], PHASE109_PUBLICATION_PASS
            )
        with (
            patch(
                "e2r.cli.verify_e2r_v6_operational_cutover_publication.verify_operational_cutover_publication",
                return_value={"status": PHASE109_VERIFICATION_PASS},
            ),
            redirect_stdout(io.StringIO()) as output,
        ):
            self.assertEqual(verify_main(["--repo-root", "/repo"]), 0)
            self.assertEqual(
                json.loads(output.getvalue())["status"], PHASE109_VERIFICATION_PASS
            )

    def test_cli_failure_never_claims_a_verified_publication(self):
        with (
            patch(
                "e2r.cli.publish_e2r_v6_operational_cutover.publish_operational_cutover",
                side_effect=ValueError("not ready"),
            ),
            redirect_stdout(io.StringIO()) as output,
        ):
            self.assertEqual(publish_main(["--repo-root", "/repo"]), 2)
            payload = json.loads(output.getvalue())
        self.assertFalse(payload["terminal_publication_verified"])
        self.assertIsNone(payload["terminal_publication_written"])

        with (
            patch(
                "e2r.cli.verify_e2r_v6_operational_cutover_publication.verify_operational_cutover_publication",
                return_value={"status": PHASE109_VERIFICATION_FAIL},
            ),
            redirect_stdout(io.StringIO()),
        ):
            self.assertEqual(verify_main(["--repo-root", "/repo"]), 2)


if __name__ == "__main__":
    unittest.main()

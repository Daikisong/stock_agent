from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from e2r.cli.compile_e2r_v6_artifact_lifecycle import (
    _write_json_atomic,
    main as lifecycle_cli_main,
)
from e2r.production.metadata import stable_hash
from e2r.research_brain.researcher_mode.artifact_lifecycle import (
    ARTIFACT_LIFECYCLE_FAIL,
    ARTIFACT_LIFECYCLE_MANIFEST_SCHEMA,
    ARTIFACT_LIFECYCLE_PASS,
    CANARY_RECEIPT_DATE,
    CANARY_TARGET_IDS,
    CURRENT_AUTHORITY,
    CURRENT_LIVE_CANARY_PREFIXES,
    FINAL_ROOT_RELATIVE,
    FINAL_STATUS_PROJECTION,
    HISTORICAL_SNAPSHOT,
    PRE_GOLD_PENDING_STATUS,
    SUPERSEDED,
    compile_artifact_lifecycle,
)


def _run_git(repo: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=repo, text=True, stderr=subprocess.DEVNULL
    ).strip()


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )


class _TrackedDossierFixture:
    def __init__(self) -> None:
        self._temporary = tempfile.TemporaryDirectory()
        self.base = Path(self._temporary.name)
        self.repo = self.base / "repo"
        self.repo.mkdir()
        _run_git(self.repo, "init", "-q")
        _run_git(self.repo, "config", "user.email", "phase104@example.invalid")
        _run_git(self.repo, "config", "user.name", "Phase 104 Test")
        self.final = self.repo / FINAL_ROOT_RELATIVE
        self._create_final_tree()
        self.commit("initial tracked dossier")

    def close(self) -> None:
        self._temporary.cleanup()

    def __enter__(self) -> "_TrackedDossierFixture":
        return self

    def __exit__(self, *_args: object) -> None:
        self.close()

    def _create_final_tree(self) -> None:
        self.final.mkdir(parents=True)
        (self.final / "README.md").write_text("# E2R v6 dossier\n", encoding="utf-8")
        _write_json(self.final / "starting_state.json", {"snapshot": "START"})
        for name in (
            "clean_clone_reproduction.json",
            "provider_runtime_audit.json",
            "cross_archetype_canary_selection.json",
            "cross_archetype_canary_summary.json",
            "current_krx_census_summary.json",
            "operational_acceptance_reviewer_gate.json",
        ):
            _write_json(self.final / name, {"artifact": name, "complete": True})
        (self.final / "current_krx_stage_map_compact.jsonl").write_text(
            '{"target_id":"TEST","canonical_stage":"2"}\n',
            encoding="utf-8",
        )
        (self.final / "operational_cutover_final.md").write_text(
            "\n".join(
                (
                    "# Final",
                    "production_research_status=COMPLETE",
                    "gold_evaluation_status=PASS",
                    "score_status=COMPLETE",
                    "stagecourt_status=FINAL",
                    "score_valid=true",
                    "stage_final=true",
                    "",
                )
            ),
            encoding="utf-8",
        )
        for target_id in CANARY_TARGET_IDS:
            target_root = (
                self.final
                / "canary_receipts"
                / CANARY_RECEIPT_DATE
                / target_id
            )
            target_root.mkdir(parents=True)
            vector = {"eps_fcf_explosion": 10.0, "earnings_visibility": 8.0}
            score = {
                "schema_version": "e2r_v6_score_receipt_v1",
                "receipt_id": f"SCORE-{target_id}",
                "target_id": target_id,
                "component_score_vector": vector,
                "total_score": 18.0,
                "canonical_stage": "2",
                "score_valid": True,
                **dict(FINAL_STATUS_PROJECTION),
            }
            stage = {
                "schema_version": "e2r_v6_stagecourt_receipt_v1",
                "target_id": target_id,
                "score_receipt_id": score["receipt_id"],
                "component_score_vector_hash": stable_hash(vector),
                "total_score": 18.0,
                "canonical_stage": "2",
                "decision_status": "FINAL",
                "score_valid": True,
            }
            _write_json(target_root / "score_receipt.json", score)
            _write_json(target_root / "stagecourt_receipt.json", stage)
            _write_json(target_root / "receipt_manifest.json", {"target_id": target_id})
            for name in (
                "component_decisions.jsonl",
                "scoring_facts.jsonl",
                "judge_decisions.jsonl",
                "source_manifest.jsonl",
            ):
                (target_root / name).write_text(
                    json.dumps({"target_id": target_id, "kind": name}) + "\n",
                    encoding="utf-8",
                )
        live_root = self.final / "current_live_canaries"
        for prefix in CURRENT_LIVE_CANARY_PREFIXES:
            (live_root / f"{prefix}fixture").mkdir(parents=True)
        clone_root = self.final / "clean_clone"
        for name in (
            "receipt_recompute_result.json",
            "tracked_readiness_result.json",
            "test_result.json",
        ):
            _write_json(clone_root / name, {"status": "PASS"})

    def commit(self, message: str) -> str:
        _run_git(self.repo, "add", "-A")
        _run_git(self.repo, "commit", "-qm", message)
        return _run_git(self.repo, "rev-parse", "HEAD")

    def manifest(self) -> dict[str, object]:
        head = _run_git(self.repo, "rev-parse", "HEAD")
        audit_path = self.final / "artifact_lifecycle_audit.json"
        artifacts: list[dict[str, object]] = []
        for path in sorted(item for item in self.final.rglob("*") if item.is_file()):
            if path == audit_path:
                continue
            relative = path.relative_to(self.repo).as_posix()
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            artifact_id = "ART-" + hashlib.sha256(relative.encode()).hexdigest()[:20]
            historical = path == self.final / "starting_state.json"
            artifacts.append(
                {
                    "artifact_id": artifact_id,
                    "artifact_path": relative,
                    "artifact_role": (
                        HISTORICAL_SNAPSHOT if historical else CURRENT_AUTHORITY
                    ),
                    "authority_scope": relative,
                    "as_of_date": "2026-07-12",
                    "generated_at": "2026-08-09T01:02:03+09:00",
                    "commit_sha": head,
                    "content_hash": digest,
                    "supersedes": [],
                    "superseded_by": None,
                    "production_readiness_authority": not historical,
                }
            )
        return {
            "schema_version": ARTIFACT_LIFECYCLE_MANIFEST_SCHEMA,
            "artifacts": artifacts,
            "status_projection": dict(FINAL_STATUS_PROJECTION),
        }

    def compile(self, manifest: dict[str, object] | None = None) -> dict[str, object]:
        return dict(
            compile_artifact_lifecycle(
                manifest or self.manifest(),
                repo_root=self.repo,
                prospective_audit_path=self.final / "artifact_lifecycle_audit.json",
            )
        )

    @staticmethod
    def row_for(manifest: dict[str, object], suffix: str) -> dict[str, object]:
        rows = manifest["artifacts"]
        assert isinstance(rows, list)
        return next(
            row
            for row in rows
            if isinstance(row, dict) and str(row["artifact_path"]).endswith(suffix)
        )


class E2RV6ArtifactLifecycleTests(unittest.TestCase):
    def setUp(self) -> None:
        trust = patch(
            "e2r.research_brain.researcher_mode.artifact_lifecycle."
            "_repository_identity_is_trusted",
            return_value=True,
        )
        trust.start()
        self.addCleanup(trust.stop)

    def test_untrusted_repository_cannot_publish_current_authority(self) -> None:
        with _TrackedDossierFixture() as fixture, patch(
            "e2r.research_brain.researcher_mode.artifact_lifecycle."
            "_repository_identity_is_trusted",
            return_value=False,
        ):
            result = fixture.compile()
        self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
        self.assertEqual(
            result["critical_counts"]["repository_identity_untrusted_count"], 1
        )
        self.assertFalse(result["criteria"]["repository_identity_trusted"])

    def test_complete_tracked_dossier_passes_without_synthesizing_authority(self) -> None:
        with _TrackedDossierFixture() as fixture:
            result = fixture.compile()

            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_PASS)
            self.assertTrue(result["ready"])
            self.assertEqual(result["critical_count_sum"], 0)
            self.assertEqual(
                result["hard_acceptance_counts"],
                {
                    "current_authority_contradiction_count": 0,
                    "stale_snapshot_masquerading_current_count": 0,
                    "pending_status_after_gold_pass_count": 0,
                    "score_stage_receipt_mismatch_count": 0,
                },
            )
            self.assertTrue(result["authority_not_synthesized"])
            self.assertFalse(result["score_or_stage_authority"])
            self.assertFalse(
                (fixture.final / "artifact_lifecycle_audit.json").exists()
            )

    def test_git_content_binding_and_path_escape_fail_closed(self) -> None:
        with _TrackedDossierFixture() as fixture:
            manifest = fixture.manifest()
            (fixture.final / "README.md").write_text(
                "# changed after manifest\n", encoding="utf-8"
            )
            result = fixture.compile(manifest)
            readme = next(
                row
                for row in result["artifact_validations"]
                if str(row["artifact_path"]).endswith("README.md")
            )
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertIn(
                "GIT_BINDING:head_index_worktree_match", readme["errors"]
            )
            self.assertIn("GIT_BINDING:content_hash_matches", readme["errors"])

        with _TrackedDossierFixture() as fixture:
            manifest = fixture.manifest()
            row = _TrackedDossierFixture.row_for(manifest, "README.md")
            row["artifact_path"] = "../outside.json"
            result = fixture.compile(manifest)
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertIn(
                "ARTIFACT_PATH_INVALID_OR_OUTSIDE_FINAL_ROOT",
                result["invalid_artifact_rows"][0]["errors"],
            )

        with _TrackedDossierFixture() as fixture:
            manifest = fixture.manifest()
            row = _TrackedDossierFixture.row_for(manifest, "README.md")
            row["artifact_path"] = (
                f"{FINAL_ROOT_RELATIVE.as_posix()}/bad\nname.json"
            )
            result = fixture.compile(manifest)
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertIn(
                "ARTIFACT_PATH_INVALID_OR_OUTSIDE_FINAL_ROOT",
                result["invalid_artifact_rows"][0]["errors"],
            )

    def test_final_root_cannot_be_redirected_away_from_contract_path(self) -> None:
        with _TrackedDossierFixture() as fixture:
            result = compile_artifact_lifecycle(
                fixture.manifest(),
                repo_root=fixture.repo,
                final_root="docs/a-different-final-root",
                prospective_audit_path=(
                    fixture.repo
                    / "docs/a-different-final-root/artifact_lifecycle_audit.json"
                ),
            )
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertEqual(
                result["critical_counts"]["final_root_argument_invalid_count"], 1
            )

    def test_symlink_in_final_tree_is_rejected(self) -> None:
        with _TrackedDossierFixture() as fixture:
            link = fixture.final / "linked-outside.json"
            link.symlink_to(fixture.base / "outside.json")
            result = fixture.compile()
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertEqual(result["critical_counts"]["final_tree_symlink_count"], 1)
            self.assertIn(
                link.relative_to(fixture.repo).as_posix(), result["final_tree_symlinks"]
            )

    def test_current_authority_scope_is_unique(self) -> None:
        with _TrackedDossierFixture() as fixture:
            manifest = fixture.manifest()
            first = _TrackedDossierFixture.row_for(manifest, "README.md")
            second = _TrackedDossierFixture.row_for(
                manifest, "provider_runtime_audit.json"
            )
            second["authority_scope"] = first["authority_scope"]
            result = fixture.compile(manifest)
            self.assertEqual(
                result["hard_acceptance_counts"][
                    "current_authority_contradiction_count"
                ],
                1,
            )
            self.assertFalse(result["criteria"]["current_authority_scope_unique"])

    def test_supersession_must_be_bidirectional_and_acyclic(self) -> None:
        with _TrackedDossierFixture() as fixture:
            manifest = fixture.manifest()
            older = _TrackedDossierFixture.row_for(manifest, "starting_state.json")
            newer = _TrackedDossierFixture.row_for(
                manifest, "operational_cutover_final.md"
            )
            older["artifact_role"] = SUPERSEDED
            older["superseded_by"] = newer["artifact_id"]
            newer["supersedes"] = [older["artifact_id"]]
            self.assertEqual(fixture.compile(manifest)["status"], ARTIFACT_LIFECYCLE_PASS)

            newer["supersedes"] = []
            broken = fixture.compile(manifest)
            self.assertEqual(broken["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertEqual(
                broken["critical_counts"][
                    "supersession_bidirectional_mismatch_count"
                ],
                1,
            )

        with _TrackedDossierFixture() as fixture:
            manifest = fixture.manifest()
            left = _TrackedDossierFixture.row_for(manifest, "starting_state.json")
            right = _TrackedDossierFixture.row_for(
                manifest, "clean_clone_reproduction.json"
            )
            for row, successor, older in (
                (left, right, right),
                (right, left, left),
            ):
                row["artifact_role"] = SUPERSEDED
                row["production_readiness_authority"] = False
                row["superseded_by"] = successor["artifact_id"]
                row["supersedes"] = [older["artifact_id"]]
            cyclic = fixture.compile(manifest)
            self.assertEqual(cyclic["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertEqual(cyclic["critical_counts"]["supersession_cycle_count"], 1)

    def test_four_hard_counts_reject_nested_or_receipt_contradictions(self) -> None:
        cases = (
            (
                "current_authority_contradiction_count",
                "provider_runtime_audit.json",
                {"nested": {"score_valid": False}},
            ),
            (
                "stale_snapshot_masquerading_current_count",
                "provider_runtime_audit.json",
                {"snapshot_status": "SUPERSEDED_PRE_FINAL"},
            ),
            (
                "pending_status_after_gold_pass_count",
                "clean_clone_reproduction.json",
                {
                    "nested": {
                        "production_research_status": PRE_GOLD_PENDING_STATUS
                    }
                },
            ),
        )
        for hard_count, suffix, payload in cases:
            with self.subTest(hard_count=hard_count):
                with _TrackedDossierFixture() as fixture:
                    path = next(
                        item
                        for item in fixture.final.rglob("*")
                        if item.is_file() and item.name == suffix
                    )
                    _write_json(path, payload)
                    fixture.commit(f"mutate {hard_count}")
                    result = fixture.compile()
                    self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
                    self.assertGreater(
                        result["hard_acceptance_counts"][hard_count], 0
                    )

        with _TrackedDossierFixture() as fixture:
            stage_path = (
                fixture.final
                / "canary_receipts"
                / CANARY_RECEIPT_DATE
                / CANARY_TARGET_IDS[0]
                / "stagecourt_receipt.json"
            )
            stage = json.loads(stage_path.read_text(encoding="utf-8"))
            stage["total_score"] = 17.0
            _write_json(stage_path, stage)
            fixture.commit("make score and StageCourt disagree")
            result = fixture.compile()
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertEqual(
                result["hard_acceptance_counts"][
                    "score_stage_receipt_mismatch_count"
                ],
                1,
            )
            self.assertIn(
                "TOTAL_SCORE_MISMATCH",
                result["score_stage_receipt_mismatches"][0]["reasons"],
            )

    def test_missing_required_file_and_directory_never_create_authority(self) -> None:
        with _TrackedDossierFixture() as fixture:
            missing_file = fixture.final / "provider_runtime_audit.json"
            missing_file.unlink()
            missing_dir = fixture.final / "current_live_canaries" / "C08_fixture"
            missing_dir.rmdir()
            result = fixture.compile()
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertGreater(
                result["critical_counts"]["missing_required_final_file_count"], 0
            )
            self.assertIn("C08_", result["missing_current_live_canary_prefixes"])
            self.assertTrue(result["authority_not_synthesized"])
            self.assertFalse(missing_file.exists())
            self.assertFalse(
                (fixture.final / "artifact_lifecycle_audit.json").exists()
            )

    def test_cli_writes_result_last_and_preserves_old_output_on_replace_failure(self) -> None:
        with _TrackedDossierFixture() as fixture:
            manifest_path = fixture.base / "lifecycle_manifest.json"
            manifest = fixture.manifest()
            _write_json(manifest_path, manifest)
            output = fixture.final / "artifact_lifecycle_audit.json"
            argv = [
                "compile_e2r_v6_artifact_lifecycle",
                "--manifest",
                str(manifest_path),
                "--repo-root",
                str(fixture.repo),
                "--output",
                str(output),
            ]
            with patch.object(sys, "argv", argv), redirect_stdout(io.StringIO()):
                exit_code = lifecycle_cli_main()
            self.assertEqual(exit_code, 0)
            result = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(result["status"], ARTIFACT_LIFECYCLE_PASS)
            self.assertFalse(list(output.parent.glob(f".{output.name}.*.tmp")))

            untracked_recheck = compile_artifact_lifecycle(
                manifest, repo_root=fixture.repo
            )
            self.assertEqual(untracked_recheck["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertFalse(
                untracked_recheck["criteria"][
                    "lifecycle_audit_output_contract_satisfied"
                ]
            )
            fixture.commit("track compiled lifecycle audit")
            tracked_recheck = compile_artifact_lifecycle(
                manifest, repo_root=fixture.repo
            )
            self.assertEqual(tracked_recheck["status"], ARTIFACT_LIFECYCLE_PASS)

            original = output.read_bytes()
            with patch("os.replace", side_effect=OSError("simulated crash")):
                with self.assertRaisesRegex(OSError, "simulated crash"):
                    _write_json_atomic(output, {"status": "replacement"})
            self.assertEqual(output.read_bytes(), original)
            self.assertFalse(list(output.parent.glob(f".{output.name}.*.tmp")))

            _write_json(output, {"not": "a lifecycle audit"})
            fixture.commit("track malformed lifecycle audit")
            invalid_existing = compile_artifact_lifecycle(
                manifest, repo_root=fixture.repo
            )
            self.assertEqual(invalid_existing["status"], ARTIFACT_LIFECYCLE_FAIL)
            self.assertFalse(
                invalid_existing["criteria"][
                    "lifecycle_audit_output_contract_satisfied"
                ]
            )

    def test_atomic_writer_pins_parent_directory_inode(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            parent = root / "output"
            parent.mkdir()
            displaced = root / "output-original"
            victim = root / "victim"
            victim.mkdir()
            output = parent / "audit.json"
            original_replace = __import__("os").replace
            attacked = False

            def replace_after_parent_swap(*args, **kwargs):
                nonlocal attacked
                if not attacked:
                    attacked = True
                    parent.rename(displaced)
                    parent.symlink_to(victim, target_is_directory=True)
                return original_replace(*args, **kwargs)

            with patch(
                "e2r.cli.compile_e2r_v6_artifact_lifecycle.os.replace",
                side_effect=replace_after_parent_swap,
            ):
                _write_json_atomic(output, {"status": "safe"})

            self.assertFalse((victim / output.name).exists())
            self.assertEqual(
                json.loads((displaced / output.name).read_text(encoding="utf-8")),
                {"status": "safe"},
            )

    def test_atomic_writer_never_creates_through_a_swapped_symlink_parent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            victim = root / "final-receipts"
            victim.mkdir()
            swapped_parent = root / "outside"
            swapped_parent.symlink_to(victim, target_is_directory=True)
            output = swapped_parent / "new-parent" / "audit.json"
            with self.assertRaises((OSError, ValueError)):
                _write_json_atomic(output, {"status": "forbidden"})
            self.assertFalse((victim / "new-parent").exists())


if __name__ == "__main__":
    unittest.main()

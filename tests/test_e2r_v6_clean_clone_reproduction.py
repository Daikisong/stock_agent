from __future__ import annotations

import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/run_e2r_v6_clean_clone_reproduction.py"
SPEC = importlib.util.spec_from_file_location(
    "e2r_v6_clean_clone_reproduction_bootstrap", SCRIPT
)
assert SPEC is not None and SPEC.loader is not None
clean_clone = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(clean_clone)


class E2RV6CleanCloneReproductionTests(unittest.TestCase):
    maxDiff = None

    @staticmethod
    def receipt_result() -> dict[str, object]:
        return {
            "schema_version": clean_clone.VERIFICATION_SCHEMA,
            "status": clean_clone.VERIFICATION_PASS,
            "offline": True,
            "critical_count_sum": 0,
            "target_count": 2,
            "target_ids": list(clean_clone.EXPECTED_TARGET_IDS),
        }

    @classmethod
    def readiness_result(cls) -> dict[str, object]:
        receipt = cls.receipt_result()
        return {
            "schema_version": clean_clone.TRACKED_READINESS_SCHEMA,
            "status": clean_clone.TRACKED_READINESS_PASS,
            "ready": True,
            "offline": True,
            "production_readiness_authority": False,
            "critical_count": 0,
            "same_receipt_replay_variance": 0,
            "verification_status": clean_clone.VERIFICATION_PASS,
            "verification_critical_count_sum": 0,
            "receipt_verification_hash": clean_clone._stable_hash(receipt),
            "target_ids": list(clean_clone.EXPECTED_TARGET_IDS),
        }

    @staticmethod
    def full_test_result(executed: int = 17) -> dict[str, object]:
        return {
            "schema_version": clean_clone.CLEAN_CLONE_TEST_SCHEMA,
            "status": clean_clone.CLEAN_CLONE_TEST_PASS,
            "executed_test_count": executed,
            "failed_test_count": 0,
            "error_test_count": 0,
            "critical_count_sum": 0,
            "production_readiness_authority": False,
        }

    @staticmethod
    def make_publish_repo(root: Path) -> Path:
        repo = root / "repo"
        (repo / clean_clone.FINAL_ROOT_RELATIVE).mkdir(parents=True)
        return repo

    def test_bootstrap_has_no_mutable_worktree_e2r_import(self) -> None:
        tree = ast.parse(SCRIPT.read_text(encoding="utf-8"))
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.add(node.module)
        self.assertFalse(any(name == "e2r" or name.startswith("e2r.") for name in imported))
        self.assertIn("python -I -S", SCRIPT.read_text(encoding="utf-8"))

    def test_clone_and_worker_commands_are_exactly_isolated(self) -> None:
        destination = Path("/tmp/example-clean-clone")
        command = clean_clone._clone_command("/usr/bin/git", destination)
        self.assertEqual(command[0:2], ["/usr/bin/git", "clone"])
        self.assertIn("--no-local", command)
        self.assertIn("--single-branch", command)
        self.assertEqual(command[-2], clean_clone.TRUSTED_CLONE_URL)
        self.assertEqual(command[-1], str(destination))

        worker = clean_clone._isolated_python_command(
            worker_source="pass", arguments=("one",)
        )
        self.assertEqual(worker[1:4], ["-I", "-S", "-B"])
        self.assertIn("-c", worker)

        pip_command = clean_clone._pip_install_command(
            pip_wheel=Path("/scratch/pip.whl"),
            dependency_root=Path("/scratch/deps"),
            lock=Path("/clone/requirements/locked.txt"),
        )
        self.assertEqual(pip_command[0:4], ["/usr/bin/python3", "-I", "-S", "-B"])
        self.assertIn("--require-hashes", pip_command)
        self.assertIn("--no-deps", pip_command)
        self.assertIn("--no-cache-dir", pip_command)
        self.assertIn("--only-binary=:all:", pip_command)
        self.assertEqual(pip_command[-2:], ["-r", "/clone/requirements/locked.txt"])
        self.assertEqual(
            clean_clone.PIP_BOOTSTRAP_SHA256,
            "99cb1c2899893b075ff56e4ed0af55669a955b49ad7fb8d8603ecdaf4ed653fb",
        )

    def test_sanitized_environment_drops_credentials_and_python_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            env = clean_clone._sanitized_environment(Path(directory))
        self.assertNotIn("PYTHONPATH", env)
        self.assertNotIn("VIRTUAL_ENV", env)
        self.assertNotIn("SSH_AUTH_SOCK", env)
        self.assertNotIn("AWS_ACCESS_KEY_ID", env)
        self.assertEqual(env["GIT_CONFIG_NOSYSTEM"], "1")
        self.assertEqual(env["GIT_CONFIG_GLOBAL"], "/dev/null")

    def test_dirty_source_fails_before_baseline_or_e2r_execution(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory) / "repo"
            repo.mkdir()
            subprocess.run(["git", "init", "-q", "-b", "main"], cwd=repo, check=True)
            (repo / "tracked").write_text("tracked\n", encoding="utf-8")
            subprocess.run(["git", "add", "tracked"], cwd=repo, check=True)
            subprocess.run(
                [
                    "git",
                    "-c",
                    "user.name=test",
                    "-c",
                    "user.email=test@example.com",
                    "commit",
                    "-qm",
                    "initial",
                ],
                cwd=repo,
                check=True,
            )
            subprocess.run(
                [
                    "git",
                    "remote",
                    "add",
                    "origin",
                    clean_clone.TRUSTED_CLONE_URL,
                ],
                cwd=repo,
                check=True,
            )
            subprocess.run(
                ["git", "update-ref", "refs/remotes/origin/main", "HEAD"],
                cwd=repo,
                check=True,
            )
            (repo / "untracked").write_text("dirty\n", encoding="utf-8")
            env = clean_clone._sanitized_environment(Path(directory) / "runtime")
            with self.assertRaisesRegex(
                clean_clone.CleanCloneReproductionError, "worktree is dirty"
            ):
                clean_clone._trusted_source_head(repo, env)

    def test_local_clone_hardlinked_objects_are_rejected_even_with_forged_origin(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            subprocess.run(["git", "init", "-q", "-b", "main"], cwd=source, check=True)
            (source / "tracked").write_text("tracked\n", encoding="utf-8")
            subprocess.run(["git", "add", "tracked"], cwd=source, check=True)
            subprocess.run(
                [
                    "git",
                    "-c",
                    "user.name=test",
                    "-c",
                    "user.email=test@example.com",
                    "commit",
                    "-qm",
                    "initial",
                ],
                cwd=source,
                check=True,
            )
            head = subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=source, text=True
            ).strip()
            clone = root / "local-clone"
            subprocess.run(
                ["git", "clone", "--local", "-q", str(source), str(clone)],
                check=True,
            )
            subprocess.run(
                ["git", "remote", "set-url", "origin", clean_clone.TRUSTED_CLONE_URL],
                cwd=clone,
                check=True,
            )
            env = clean_clone._sanitized_environment(root / "runtime")
            with self.assertRaisesRegex(
                clean_clone.CleanCloneReproductionError,
                "objects are not private no-local copies",
            ):
                clean_clone._validate_clean_clone(
                    clone, expected_sha=head, env=env
                )

    def test_output_env_cache_and_journal_are_each_forbidden(self) -> None:
        for relative in clean_clone._FORBIDDEN_CLONE_PATHS:
            with self.subTest(relative=relative), tempfile.TemporaryDirectory() as directory:
                clone = Path(directory) / "clone"
                clone.mkdir()
                path = clone / relative
                if path.suffix or path.name == ".env":
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text("forbidden\n", encoding="utf-8")
                else:
                    path.mkdir(parents=True)
                with self.assertRaisesRegex(
                    clean_clone.CleanCloneReproductionError,
                    "forbidden runtime inputs",
                ):
                    clean_clone._assert_forbidden_clone_inputs_absent(clone)

    def test_full_unittest_result_requires_real_zero_exit_summary(self) -> None:
        success = subprocess.CompletedProcess(
            [], 0, stdout="", stderr="Ran 42 tests in 1.000s\n\nOK\n"
        )
        with patch.object(clean_clone.subprocess, "run", return_value=success):
            result = clean_clone._run_full_test_suite(
                Path("/clone"),
                dependency_root=Path("/scratch/deps"),
                python_wrapper=Path("/scratch/python"),
                env={"PATH": "/usr/bin"},
            )
        self.assertEqual(result["executed_test_count"], 42)
        self.assertEqual(result["status"], clean_clone.CLEAN_CLONE_TEST_PASS)

        failure = subprocess.CompletedProcess(
            [], 1, stdout="", stderr="Ran 42 tests in 1.000s\n\nFAILED (failures=1)\n"
        )
        with patch.object(clean_clone.subprocess, "run", return_value=failure):
            with self.assertRaises(clean_clone.CleanCloneReproductionError):
                clean_clone._run_full_test_suite(
                    Path("/clone"),
                    dependency_root=Path("/scratch/deps"),
                    python_wrapper=Path("/scratch/python"),
                    env={"PATH": "/usr/bin"},
                )

    def test_nested_python_wrapper_keeps_subprocesses_on_the_exact_target(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            runtime = Path(directory)
            clone = runtime / "clone"
            dependency_root = runtime / "deps"
            (clone / "src").mkdir(parents=True)
            (clone / "tests").mkdir()
            package = dependency_root / "fake_dependency"
            package.mkdir(parents=True)
            (package / "__init__.py").write_text("VALUE = 7\n", encoding="utf-8")
            wrapper = clean_clone._create_isolated_python_wrapper(
                runtime,
                clone=clone,
                dependency_root=dependency_root,
            )
            source = (
                "import fake_dependency,json,sys;"
                "print(json.dumps({'value':fake_dependency.VALUE,"
                "'origin':fake_dependency.__file__,'executable':sys.executable,"
                "'paths':sys.path}))"
            )
            completed = subprocess.run(
                [str(wrapper), "-c", source],
                cwd=clone,
                env={"PATH": "/usr/bin:/bin", "PYTHONPATH": "/untrusted"},
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            row = json.loads(completed.stdout)
            self.assertEqual(row["value"], 7)
            self.assertEqual(row["executable"], str(wrapper))
            self.assertTrue(Path(row["origin"]).is_relative_to(dependency_root))
            self.assertNotIn("/untrusted", row["paths"])
            self.assertFalse(
                any("site-packages" in path for path in row["paths"])
            )

    def test_bad_lock_and_bad_pip_bootstrap_hash_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            clone = root / "clone"
            lock = clone / clean_clone.DEPENDENCY_LOCK_RELATIVE_PATH
            lock.parent.mkdir(parents=True)
            lock.write_text("pypdf>=4\n", encoding="utf-8")
            with self.assertRaisesRegex(
                clean_clone.CleanCloneReproductionError,
                "exact version and SHA256",
            ):
                clean_clone._validate_dependency_lock(clone)

        class FakeResponse:
            status = 200

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def geturl(self):
                return clean_clone.PIP_BOOTSTRAP_URL

            def read(self, size):
                del size
                if hasattr(self, "used"):
                    return b""
                self.used = True
                return b"not-the-pinned-wheel"

        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(
                clean_clone.CleanCloneReproductionError, "SHA256 mismatch"
            ):
                clean_clone._download_pip_bootstrap(
                    Path(directory), opener=lambda *_args, **_kwargs: FakeResponse()
                )

    def test_success_replays_twice_and_publishes_exact_raw_hashes(self) -> None:
        receipt = self.receipt_result()
        readiness = self.readiness_result()
        tests = self.full_test_result(123)
        with tempfile.TemporaryDirectory() as directory:
            repo = self.make_publish_repo(Path(directory))

            def fake_clone(*, scratch_root, expected_sha, env):
                del expected_sha, env
                path = scratch_root / "origin-main"
                path.mkdir()
                return path

            replay_rows = [receipt, readiness, readiness]
            with patch.object(
                clean_clone, "_trusted_source_head", return_value="a" * 40
            ) as trust, patch.object(
                clean_clone, "_clone_origin_main", side_effect=fake_clone
            ), patch.object(
                clean_clone, "_validate_clean_clone"
            ) as validate, patch.object(
                clean_clone, "_run_replay_worker", side_effect=replay_rows
            ) as replay, patch.object(
                clean_clone,
                "_install_test_dependencies",
                return_value=(Path("/scratch/deps"), {"pypdf": "6.13.3"}),
            ), patch.object(
                clean_clone, "_run_dependency_import_smoke", return_value={"rows": []}
            ), patch.object(
                clean_clone,
                "_create_isolated_python_wrapper",
                return_value=Path("/scratch/python"),
            ), patch.object(
                clean_clone, "_run_full_test_suite", return_value=tests
            ):
                result = clean_clone.produce_clean_clone_reproduction(repo)

            self.assertEqual(trust.call_count, 2)
            self.assertEqual(validate.call_count, 6)
            self.assertEqual(
                [call.kwargs["mode"] for call in replay.call_args_list],
                ["receipt", "readiness", "readiness"],
            )
            final = repo / clean_clone.FINAL_ROOT_RELATIVE
            child = final / "clean_clone"
            self.assertTrue(clean_clone._published_bundle_matches(repo))
            self.assertEqual(
                result["receipt_recompute_result_hash"],
                hashlib.sha256(
                    (child / "receipt_recompute_result.json").read_bytes()
                ).hexdigest(),
            )
            self.assertEqual(
                result["tracked_readiness_result_hash"],
                hashlib.sha256(
                    (child / "tracked_readiness_result.json").read_bytes()
                ).hexdigest(),
            )
            self.assertEqual(
                result["test_result_hash"],
                hashlib.sha256((child / "test_result.json").read_bytes()).hexdigest(),
            )

    def test_untrusted_clone_or_test_failure_never_creates_a_pass_artifact(self) -> None:
        cases = ("trust", "clone", "install", "test")
        for failure_point in cases:
            with self.subTest(failure_point=failure_point), tempfile.TemporaryDirectory() as directory:
                repo = self.make_publish_repo(Path(directory))

                def fake_clone(*, scratch_root, expected_sha, env):
                    del expected_sha, env
                    if failure_point == "clone":
                        raise clean_clone.CleanCloneReproductionError("clone failed")
                    path = scratch_root / "origin-main"
                    path.mkdir()
                    return path

                def fake_trust(*args, **kwargs):
                    del args, kwargs
                    if failure_point == "trust":
                        raise clean_clone.CleanCloneReproductionError(
                            "repository origin is untrusted"
                        )
                    return "a" * 40

                with patch.object(
                    clean_clone, "_trusted_source_head", side_effect=fake_trust
                ), patch.object(
                    clean_clone, "_clone_origin_main", side_effect=fake_clone
                ), patch.object(
                    clean_clone, "_validate_clean_clone"
                ), patch.object(
                    clean_clone,
                    "_run_replay_worker",
                    side_effect=[
                        self.receipt_result(),
                        self.readiness_result(),
                        self.readiness_result(),
                    ],
                ), patch.object(
                    clean_clone,
                    "_install_test_dependencies",
                    side_effect=(
                        clean_clone.CleanCloneReproductionError("install failed")
                        if failure_point == "install"
                        else None
                    ),
                    return_value=(Path("/scratch/deps"), {"pypdf": "6.13.3"}),
                ), patch.object(
                    clean_clone, "_run_dependency_import_smoke", return_value={"rows": []}
                ), patch.object(
                    clean_clone,
                    "_create_isolated_python_wrapper",
                    return_value=Path("/scratch/python"),
                ), patch.object(
                    clean_clone,
                    "_run_full_test_suite",
                    side_effect=clean_clone.CleanCloneReproductionError("tests failed"),
                ):
                    with self.assertRaises(clean_clone.CleanCloneReproductionError):
                        clean_clone.produce_clean_clone_reproduction(repo)
                final = repo / clean_clone.FINAL_ROOT_RELATIVE
                self.assertFalse((final / "clean_clone").exists())
                self.assertFalse((final / "clean_clone_reproduction.json").exists())

    def test_divergent_second_readiness_replay_publishes_nothing(self) -> None:
        first = self.readiness_result()
        second = dict(first)
        second["receipt_replay_verification_hash"] = "b" * 64
        with tempfile.TemporaryDirectory() as directory:
            repo = self.make_publish_repo(Path(directory))

            def fake_clone(*, scratch_root, expected_sha, env):
                del expected_sha, env
                path = scratch_root / "origin-main"
                path.mkdir()
                return path

            with patch.object(
                clean_clone, "_trusted_source_head", return_value="a" * 40
            ), patch.object(
                clean_clone, "_clone_origin_main", side_effect=fake_clone
            ), patch.object(
                clean_clone, "_validate_clean_clone"
            ), patch.object(
                clean_clone,
                "_run_replay_worker",
                side_effect=[self.receipt_result(), first, second],
            ), patch.object(
                clean_clone, "_run_full_test_suite", return_value=self.full_test_result()
            ):
                with self.assertRaisesRegex(
                    clean_clone.CleanCloneReproductionError, "replays diverged"
                ):
                    clean_clone.produce_clean_clone_reproduction(repo)
            final = repo / clean_clone.FINAL_ROOT_RELATIVE
            self.assertFalse((final / "clean_clone").exists())
            self.assertFalse((final / "clean_clone_reproduction.json").exists())

    def test_result_is_committed_last_after_complete_child_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = self.make_publish_repo(Path(directory))
            final = repo / clean_clone.FINAL_ROOT_RELATIVE
            observed = []

            def before_result() -> None:
                observed.append(
                    (
                        all(
                            (final / "clean_clone" / name).is_file()
                            for name in clean_clone.CLEAN_CLONE_CHILD_NAMES
                        ),
                        (final / clean_clone.REPRODUCTION_RESULT_NAME).exists(),
                    )
                )

            clean_clone._publish_artifacts(
                repo,
                receipt_result=self.receipt_result(),
                readiness_result=self.readiness_result(),
                test_result=self.full_test_result(),
                before_result_commit=before_result,
            )
            self.assertEqual(observed, [(True, False)])
            self.assertTrue(clean_clone._published_bundle_matches(repo))

    def test_symlink_parent_and_parent_swap_cannot_publish_into_victim(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / "repo"
            victim = root / "victim"
            victim.mkdir()
            final = repo / clean_clone.FINAL_ROOT_RELATIVE
            final.parent.mkdir(parents=True)
            final.symlink_to(victim, target_is_directory=True)
            with self.assertRaises(OSError):
                clean_clone._publish_artifacts(
                    repo,
                    receipt_result=self.receipt_result(),
                    readiness_result=self.readiness_result(),
                    test_result=self.full_test_result(),
                )
            self.assertEqual(tuple(victim.iterdir()), ())

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = self.make_publish_repo(root)
            final = repo / clean_clone.FINAL_ROOT_RELATIVE
            moved = root / "moved-cutover"
            victim = root / "victim"
            victim.mkdir()

            def swap_parent() -> None:
                final.rename(moved)
                final.symlink_to(victim, target_is_directory=True)

            with self.assertRaises((OSError, clean_clone.CleanCloneReproductionError)):
                clean_clone._publish_artifacts(
                    repo,
                    receipt_result=self.receipt_result(),
                    readiness_result=self.readiness_result(),
                    test_result=self.full_test_result(),
                    before_result_commit=swap_parent,
                )
            self.assertEqual(tuple(victim.iterdir()), ())
            self.assertFalse((victim / clean_clone.REPRODUCTION_RESULT_NAME).exists())
            self.assertFalse((moved / clean_clone.REPRODUCTION_RESULT_NAME).exists())
            self.assertFalse((moved / "clean_clone").exists())

    def test_raw_hash_tamper_is_rejected_and_different_existing_bundle_is_not_replaced(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = self.make_publish_repo(Path(directory))
            clean_clone._publish_artifacts(
                repo,
                receipt_result=self.receipt_result(),
                readiness_result=self.readiness_result(),
                test_result=self.full_test_result(),
            )
            child = (
                repo
                / clean_clone.FINAL_ROOT_RELATIVE
                / "clean_clone/receipt_recompute_result.json"
            )
            child.write_bytes(child.read_bytes() + b" \n")
            self.assertFalse(clean_clone._published_bundle_matches(repo))
            with self.assertRaisesRegex(
                clean_clone.CleanCloneReproductionError, "already exist"
            ):
                clean_clone._publish_artifacts(
                    repo,
                    receipt_result=self.receipt_result(),
                    readiness_result=self.readiness_result(),
                    test_result=self.full_test_result(),
                )

    def test_identical_existing_bundle_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            repo = self.make_publish_repo(Path(directory))
            first = clean_clone._publish_artifacts(
                repo,
                receipt_result=self.receipt_result(),
                readiness_result=self.readiness_result(),
                test_result=self.full_test_result(),
            )
            second = clean_clone._publish_artifacts(
                repo,
                receipt_result=self.receipt_result(),
                readiness_result=self.readiness_result(),
                test_result=self.full_test_result(),
            )
            self.assertEqual(first, second)
            self.assertTrue(clean_clone._published_bundle_matches(repo))


if __name__ == "__main__":
    unittest.main()

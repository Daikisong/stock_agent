from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from e2r.cli.compile_e2r_v6_operational_self_repair import main as self_repair_cli
from e2r.production.v6_operational_self_repair import (
    FAILURE_CLASSES,
    SELF_REPAIR_AUDIT_LEAF,
    SELF_REPAIR_FAIL,
    SELF_REPAIR_JOURNAL_LEAF,
    SELF_REPAIR_PASS,
    compile_operational_self_repair_audit,
    validate_operational_self_repair_audit,
)
from e2r.research_brain.researcher_mode.artifact_lifecycle import FINAL_ROOT_RELATIVE


class E2RV6OperationalSelfRepairTests(unittest.TestCase):
    def test_git_recomputed_iteration_passes_without_fixed_iteration_authority(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, final, row = _fixture(Path(tmp))
            _write_journal(final, [row])
            result = compile_operational_self_repair_audit(
                repo_root=repo,
                final_root=final,
                test_mode=True,
            )

        self.assertEqual(result["status"], SELF_REPAIR_PASS)
        self.assertEqual(result["critical_count_sum"], 0)
        self.assertEqual(result["iteration_count"], 1)
        self.assertFalse(result["fixed_iteration_count_is_completion_authority"])
        self.assertEqual(set(result["failure_class_counts"]), set(FAILURE_CLASSES))
        self.assertTrue(
            validate_operational_self_repair_audit(result, allow_test_mode=True)
        )

    def test_hash_and_commit_are_recomputed_not_trusted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, final, row = _fixture(Path(tmp))
            row["after_artifact_hash"] = "0" * 64
            _write_journal(final, [row])
            result = compile_operational_self_repair_audit(
                repo_root=repo,
                final_root=final,
                test_mode=True,
            )

        self.assertEqual(result["status"], SELF_REPAIR_FAIL)
        self.assertEqual(result["critical_counts"]["after_hash_mismatch_count"], 1)
        self.assertFalse(validate_operational_self_repair_audit(result, allow_test_mode=True))

    def test_stale_self_repair_snapshot_cannot_replace_current_recompute(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, final, row = _fixture(Path(tmp))
            _write_journal(final, [row])
            current = compile_operational_self_repair_audit(
                repo_root=repo,
                final_root=final,
                test_mode=True,
            )
            stale = json.loads(json.dumps(current))
            stale["journal_sha256"] = "0" * 64
            core = {key: value for key, value in stale.items() if key != "audit_hash"}
            from e2r.production.metadata import stable_hash

            stale["audit_hash"] = stable_hash(core)

        self.assertFalse(
            validate_operational_self_repair_audit(
                stale,
                recomputed=current,
                allow_test_mode=True,
            )
        )

    def test_remaining_blocker_or_fixed_rerun_failure_cannot_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, final, row = _fixture(Path(tmp))
            row["remaining_blockers"] = ["provider still pending"]
            row["clean_rerun_status"] = "PENDING"
            _write_journal(final, [row])
            result = compile_operational_self_repair_audit(
                repo_root=repo,
                final_root=final,
                test_mode=True,
            )

        self.assertEqual(result["critical_counts"]["remaining_blocker_count"], 1)
        self.assertEqual(result["critical_counts"]["clean_rerun_failure_count"], 1)
        self.assertGreater(result["critical_counts"]["unresolved_failure_class_count"], 0)

    def test_duplicate_iteration_and_unknown_failure_class_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, final, row = _fixture(Path(tmp))
            bad = dict(row)
            bad["failure_class"] = "MADE_UP_FAILURE"
            _write_journal(final, [row, bad])
            result = compile_operational_self_repair_audit(
                repo_root=repo,
                final_root=final,
                test_mode=True,
            )

        self.assertEqual(result["critical_counts"]["duplicate_iteration_id_count"], 1)
        self.assertEqual(result["critical_counts"]["unknown_failure_class_count"], 1)

    def test_empty_or_duplicate_key_journal_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            _git(repo, "init")
            final = repo / FINAL_ROOT_RELATIVE
            final.mkdir(parents=True)
            empty = compile_operational_self_repair_audit(
                repo_root=repo,
                final_root=final,
                test_mode=True,
            )
            (final / SELF_REPAIR_JOURNAL_LEAF).write_text(
                '{"iteration_id":"a","iteration_id":"b"}\n', encoding="utf-8"
            )
            duplicate = compile_operational_self_repair_audit(
                repo_root=repo,
                final_root=final,
                test_mode=True,
            )

        self.assertGreater(empty["critical_counts"]["journal_missing_count"], 0)
        self.assertGreater(duplicate["critical_counts"]["journal_parse_error_count"], 0)

    def test_cli_writes_then_verify_only_recomputes_exact_leaf(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, final, row = _fixture(Path(tmp))
            _write_journal(final, [row])
            self.assertEqual(
                self_repair_cli(
                    [
                        "--repo-root",
                        str(repo),
                        "--final-root",
                        str(FINAL_ROOT_RELATIVE),
                    ]
                ),
                0,
            )
            self.assertEqual(
                self_repair_cli(
                    [
                        "--repo-root",
                        str(repo),
                        "--final-root",
                        str(FINAL_ROOT_RELATIVE),
                        "--verify-only",
                    ]
                ),
                0,
            )
            stored = json.loads((final / SELF_REPAIR_AUDIT_LEAF).read_text(encoding="utf-8"))

        self.assertEqual(stored["status"], SELF_REPAIR_PASS)


def _fixture(root: Path) -> tuple[Path, Path, dict[str, object]]:
    repo = root.resolve()
    _git(repo, "init")
    _git(repo, "config", "user.email", "test@example.com")
    _git(repo, "config", "user.name", "E2R Test")
    path = repo / "src/e2r/example.py"
    path.parent.mkdir(parents=True)
    before = b"READY = False\n"
    path.write_bytes(before)
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "base")
    path.write_bytes(b"READY = verify_receipt()\n")
    after = path.read_bytes()
    _git(repo, "add", ".")
    _git(repo, "commit", "-m", "receipt 계보를 재계산해 준비 상태를 봉인")
    commit = _git(repo, "rev-parse", "HEAD").stdout.strip()
    final = repo / FINAL_ROOT_RELATIVE
    final.mkdir(parents=True)
    row: dict[str, object] = {
        "iteration_id": "E2RREPAIR-0123456789abcdef01234567",
        "phase": "PHASE108",
        "target_or_scope": "operational receipt verifier",
        "failure_class": "RECEIPT_LINEAGE_BROKEN",
        "root_cause": "READY 문구가 leaf 재계산보다 먼저 사용됨",
        "file_function_config": "src/e2r/example.py#READY",
        "before_artifact_hash": hashlib.sha256(before).hexdigest(),
        "patch_commit": commit,
        "focused_tests": [
            "PYTHONPATH=src python -m unittest tests.test_e2r_v6_operational_self_repair"
        ],
        "focused_test_status": "PASS",
        "clean_rerun_status": "PASS",
        "after_artifact_hash": hashlib.sha256(after).hexdigest(),
        "remaining_blockers": [],
    }
    return repo, final, row


def _write_journal(final: Path, rows: list[dict[str, object]]) -> None:
    (final / SELF_REPAIR_JOURNAL_LEAF).write_text(
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def _git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["/usr/bin/git", *args],
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(result.stderr)
    return result


if __name__ == "__main__":
    unittest.main()

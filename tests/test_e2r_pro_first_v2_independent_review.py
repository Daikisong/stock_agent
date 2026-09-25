from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from e2r.pro_first.ids import canonical_hash
from e2r.pro_first.independent_review_v2 import (
    REVIEWER_SPECS,
    _run_reviewer,
)


class ProFirstV2IndependentReviewTest(unittest.TestCase):
    def test_reviewer_roster_is_exact_a_to_h_with_distinct_leaf_commands(self) -> None:
        self.assertEqual(tuple(row.reviewer_id for row in REVIEWER_SPECS), tuple("ABCDEFGH"))
        commands = tuple(row.test_modules for row in REVIEWER_SPECS)
        self.assertEqual(len(commands), len(set(commands)))
        self.assertTrue(all(row.input_paths for row in REVIEWER_SPECS))
        root = Path(__file__).resolve().parents[1]
        self.assertTrue(
            all((root / relative).is_file() for row in REVIEWER_SPECS for relative in row.input_paths)
        )

    def test_reviewer_hashes_exact_inputs_and_command_output(self) -> None:
        spec = REVIEWER_SPECS[0]
        root = Path(__file__).resolve().parents[1]
        output = b"test_leaf ... ok\n\nRan 1 test in 0.001s\n\nOK\n"
        with patch(
            "e2r.pro_first.independent_review_v2.subprocess.run",
            return_value=SimpleNamespace(returncode=0, stdout=output),
        ):
            row = _run_reviewer(root, spec, timeout_seconds=10)

        expected_manifest = []
        for relative in spec.input_paths:
            data = (root / relative).read_bytes()
            expected_manifest.append(
                {
                    "path": relative,
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "bytes": len(data),
                }
            )
        self.assertEqual(row["verdict"], "PASS")
        self.assertEqual(row["test_count"], 1)
        self.assertEqual(row["input_hash"], canonical_hash(expected_manifest))
        self.assertEqual(row["output_hash"], hashlib.sha256(output).hexdigest())

    def test_reviewer_fails_closed_when_command_has_no_tests(self) -> None:
        root = Path(__file__).resolve().parents[1]
        with patch(
            "e2r.pro_first.independent_review_v2.subprocess.run",
            return_value=SimpleNamespace(returncode=0, stdout=b"OK\n"),
        ):
            row = _run_reviewer(root, REVIEWER_SPECS[0], timeout_seconds=10)
        self.assertEqual(row["verdict"], "FAIL")

    def test_reviewer_timeout_is_a_hashed_fail_receipt(self) -> None:
        root = Path(__file__).resolve().parents[1]
        output = b"test_leaf ... "
        with patch(
            "e2r.pro_first.independent_review_v2.subprocess.run",
            side_effect=subprocess.TimeoutExpired(
                cmd="python -m unittest",
                timeout=10,
                output=output,
            ),
        ):
            row = _run_reviewer(root, REVIEWER_SPECS[0], timeout_seconds=10)
        self.assertEqual(row["verdict"], "FAIL")
        self.assertTrue(row["timed_out"])
        self.assertEqual(row["exit_code"], 124)
        self.assertEqual(row["output_hash"], hashlib.sha256(output).hexdigest())


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import unittest

from e2r.pro_first.generalization import (
    MANDATORY_MECHANISM_FAMILIES,
    REQUIRED_V2_KNOWN_BAD_CASE_IDS,
    audit_v2_known_bad_corpus,
    compile_generalization_acceptance,
)


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests/fixtures/pro_first_v2"
TRACKED_RECEIPT = (
    ROOT / "docs/operational/e2r_pro_first_v2/generalization_acceptance.json"
)


class ProFirstV2GeneralizationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.golden = json.loads(
            (FIXTURES / "mechanism_golden_cases.json").read_text(encoding="utf-8")
        )
        cls.known_bad = json.loads(
            (FIXTURES / "known_bad_corpus.json").read_text(encoding="utf-8")
        )
        cls.runtime = compile_generalization_acceptance(ROOT)

    def test_mandatory_mechanism_roster_is_exact_13(self) -> None:
        observed = tuple(
            row["mechanism_family"] for row in self.golden["cases"]
        )
        self.assertEqual(observed, MANDATORY_MECHANISM_FAMILIES)
        self.assertEqual(len(observed), 13)

    def test_all_13_mechanism_golden_replays_pass(self) -> None:
        self.assertEqual(self.runtime["status"], "PASS")
        self.assertEqual(self.runtime["critical_count_sum"], 0)
        self.assertEqual(self.runtime["golden_replay_pass_count"], 13)
        self.assertEqual(len(self.runtime["golden_replays"]), 13)
        for replay in self.runtime["golden_replays"]:
            with self.subTest(case_id=replay["case_id"]):
                self.assertEqual(replay["status"], "PASS")
                self.assertEqual(replay["failure_codes"], [])

    def test_golden_acceptance_metrics_are_complete(self) -> None:
        for replay in self.runtime["golden_replays"]:
            with self.subTest(case_id=replay["case_id"]):
                self.assertEqual(
                    replay["critical_question_recall_count"],
                    replay["critical_question_count"],
                )
                self.assertTrue(replay["material_positive_recall"])
                self.assertTrue(replay["material_counter_recall"])
                self.assertTrue(replay["source_role_coverage_complete"])
                self.assertTrue(replay["question_terminality_complete"])
                self.assertTrue(replay["public_gap_open_before_closure"])
                self.assertEqual(replay["public_gap_count_after_closure"], 0)
                self.assertEqual(replay["verifier_repair_pending_count"], 0)
                self.assertEqual(replay["future_leakage_count"], 0)
                self.assertEqual(replay["gold_injection_count"], 0)
                self.assertEqual(replay["query_count"], 0)
                self.assertEqual(replay["fetch_count"], 0)
                self.assertIs(replay["score_authority"], False)
                self.assertIs(replay["stage_authority"], False)

    def test_all_36_prompt_snapshots_remain_green(self) -> None:
        self.assertEqual(self.runtime["prompt_snapshot_count"], 36)
        self.assertEqual(
            self.runtime["critical_counts"]["prompt_snapshot_critical_count"],
            0,
        )
        self.assertEqual(
            self.runtime["critical_counts"][
                "prompt_snapshot_count_mismatch_count"
            ],
            0,
        )

    def test_known_bad_roster_is_exact_30(self) -> None:
        observed = tuple(row["case_id"] for row in self.known_bad["cases"])
        self.assertEqual(observed, REQUIRED_V2_KNOWN_BAD_CASE_IDS)
        self.assertEqual(len(observed), 30)
        audit = audit_v2_known_bad_corpus(self.known_bad)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["critical_count_sum"], 0)

    def test_every_known_bad_detector_test_is_loadable(self) -> None:
        unique_detector_ids = {
            detector_id
            for row in self.known_bad["cases"]
            for detector_id in row["detector_test_ids"]
        }
        self.assertEqual(len(unique_detector_ids), 29)
        loader = unittest.defaultTestLoader
        for detector_id in sorted(unique_detector_ids):
            with self.subTest(detector_id=detector_id):
                suite = loader.loadTestsFromName(detector_id)
                self.assertEqual(suite.countTestCases(), 1)
                loaded = tuple(_flatten_suite(suite))
                self.assertEqual(len(loaded), 1)
                self.assertNotEqual(loaded[0].__class__.__name__, "_FailedTest")

    def test_known_bad_tamper_fails_audit(self) -> None:
        tampered = deepcopy(self.known_bad)
        tampered["cases"][0]["score_authority"] = True
        audit = audit_v2_known_bad_corpus(tampered)
        self.assertEqual(audit["status"], "FAIL")
        self.assertGreater(audit["critical_count_sum"], 0)

    def test_tracked_generalization_acceptance_matches_runtime(self) -> None:
        tracked = json.loads(TRACKED_RECEIPT.read_text(encoding="utf-8"))
        self.assertEqual(tracked, self.runtime)


def _flatten_suite(suite: unittest.TestSuite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from _flatten_suite(item)
        else:
            yield item


if __name__ == "__main__":
    unittest.main()

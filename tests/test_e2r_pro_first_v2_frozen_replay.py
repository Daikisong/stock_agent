from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import unittest

from e2r.pro_first.canary import compile_frozen_partial_corpus_replay
from e2r.pro_first.ids import canonical_hash


ROOT = Path(__file__).resolve().parents[1]
PROJECTION = (
    ROOT / "tests/fixtures/pro_first_v2/000660_frozen_v1_projection.json"
)
TRACKED_RECEIPT = (
    ROOT / "docs/operational/e2r_pro_first_v2/000660_frozen_v1_replay.json"
)


class ProFirstV2FrozenReplayTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.projection = json.loads(PROJECTION.read_text(encoding="utf-8"))
        cls.replay = compile_frozen_partial_corpus_replay(cls.projection)

    def test_frozen_projection_matches_hash_bound_legacy_counts(self) -> None:
        self.assertEqual(
            self.projection["source_report_sha256"],
            "92394591d8d56dc52321f5a2df60a72a658c7347353f99ae96f3584fda211f9b",
        )
        self.assertEqual(self.projection["source_report_byte_count"], 127517)
        self.assertEqual(
            (
                self.projection["material_fact_count"],
                self.projection["counterfact_count"],
                self.projection["lineage_group_count"],
                self.projection["unresolved_gap_count"],
            ),
            (20, 15, 15, 13),
        )
        self.assertEqual(self.projection["verified_fact_count"], 26)
        self.assertIs(self.projection["raw_report_tracked"], False)
        self.assertIs(
            self.projection["projection_contains_article_or_quote_text"],
            False,
        )

    def test_existing_hynix_md_replays_as_partial_corpus_guard(self) -> None:
        self.assertEqual(
            self.replay["status"],
            "PRO_FIRST_V2_PARTIAL_CORPUS_GUARD_PASS",
        )
        self.assertEqual(self.replay["critical_count_sum"], 0)
        self.assertFalse(self.replay["research_saturation_valid"])
        self.assertFalse(self.replay["component_entry_allowed"])
        self.assertTrue(self.replay["legacy_complete_diverged"])
        self.assertEqual(
            self.replay["v2_deterministic_research_status"],
            "NEEDS_PUBLIC_GAP_CLOSURE",
        )

    def test_frozen_gaps_are_not_silently_downgraded_to_one_cap_class(self) -> None:
        self.assertEqual(
            self.replay["gap_candidate_class_counts"],
            {
                "LIKELY_NONPUBLIC_CANDIDATE": 7,
                "PUBLIC_SEARCHABLE": 4,
                "FUTURE_EVENT_ONLY_CANDIDATE": 2,
            },
        )
        self.assertEqual(
            sum(self.replay["gap_candidate_class_counts"].values()),
            13,
        )
        self.assertEqual(self.replay["expected_mandatory_question_count"], 28)
        self.assertEqual(self.replay["nonterminal_mandatory_question_count"], 28)
        self.assertGreaterEqual(
            self.replay["public_searchable_material_gap_count"],
            1,
        )

    def test_partial_diagnostic_is_preserved_but_not_published(self) -> None:
        self.assertEqual(self.replay["first_pass_diagnostic_score"], 23.202275)
        self.assertEqual(self.replay["first_pass_diagnostic_stage"], "0")
        self.assertIsNone(self.replay["full_thesis_score"])
        self.assertIsNone(self.replay["full_thesis_stage"])
        self.assertFalse(self.replay["full_thesis_score_valid"])
        self.assertEqual(
            self.replay["publication_status"],
            "WITHHELD_PENDING_RESEARCH_SATURATION",
        )
        self.assertEqual(self.replay["new_query_count"], 0)
        self.assertEqual(self.replay["new_fetch_count"], 0)

    def test_projection_tamper_is_rejected(self) -> None:
        tampered = deepcopy(self.projection)
        tampered["unresolved_gaps"].pop()
        with self.assertRaisesRegex(ValueError, "projection hash mismatch"):
            compile_frozen_partial_corpus_replay(tampered)

    def test_replay_does_not_branch_on_target_symbol(self) -> None:
        renamed = deepcopy(self.projection)
        renamed["job_id"] = "PROJOB-BLIND-REPLAY"
        renamed["run_id"] = "PRORUN-BLIND-REPLAY"
        renamed["target"] = {
            "target_id": "BLIND",
            "symbol": "BLIND",
            "company_name": "블라인드 대상",
        }
        renamed["projection_hash"] = canonical_hash(
            {key: value for key, value in renamed.items() if key != "projection_hash"}
        )
        result = compile_frozen_partial_corpus_replay(renamed)
        self.assertEqual(result["status"], self.replay["status"])
        self.assertEqual(
            result["gap_candidate_class_counts"],
            self.replay["gap_candidate_class_counts"],
        )
        self.assertEqual(
            result["public_searchable_material_gap_count"],
            self.replay["public_searchable_material_gap_count"],
        )

    def test_tracked_frozen_replay_matches_runtime(self) -> None:
        tracked = json.loads(TRACKED_RECEIPT.read_text(encoding="utf-8"))
        self.assertEqual(tracked, self.replay)


if __name__ == "__main__":
    unittest.main()

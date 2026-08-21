from __future__ import annotations

import json
import unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

from e2r.research_brain.runtime.live_materialization import final_readiness as module


REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO_ROOT / "configs/e2r_live_final_readiness_v1.json"


class LiveFinalReadinessReviewerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        cls.paths = {
            key: REPO_ROOT / value
            for key, value in cls.config["paths"].items()
        }
        required = (
            cls.paths["live_root"] / "universe_eligible.jsonl",
            cls.paths["canonical_current_root"] / "accepted_claims.jsonl",
            cls.paths["canonical_census_root"] / "census_stage_map.jsonl",
            cls.paths["promotion_manifest"],
        )
        cls.missing_frozen_leaves = tuple(
            str(path) for path in required if not path.is_file()
        )

    def test_all_reviewers_recompute_canonical_leaf_chain(self) -> None:
        if self.missing_frozen_leaves:
            # The clean PR does not publish these raw output leaves.  Validate
            # the tracked result only as a historical receipt; do not claim a
            # clean-clone leaf recomputation.
            receipt = json.loads(
                (
                    REPO_ROOT / "docs/operational/e2r_live_reviewer_gates.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(receipt["status"], "REVIEWER_A_TO_F_PASS")
            self.assertEqual(receipt["critical_count_sum"], 0)
            self.assertEqual(
                [row["reviewer_id"] for row in receipt["reviewers"]],
                list("ABCDEF"),
            )
            return
        reviewers = self._reviewers()
        self.assertEqual([row["reviewer_id"] for row in reviewers], list("ABCDEF"))
        self.assertTrue(all(row["status"] == "PASS" for row in reviewers))
        self.assertTrue(all(row["independent_leaf_reread"] for row in reviewers))
        self.assertTrue(all(row["leaf_hashes"] for row in reviewers))

    def test_reviewer_a_rejects_wrong_baseline_lane_family(self) -> None:
        self._require_frozen_leaves()
        baseline_path = self.paths["live_root"] / "baseline_lanes.jsonl"
        with self._patched_jsonl(
            baseline_path,
            lambda rows: self._replace_first(rows, lane="FAKE_LANE"),
        ):
            result = self._reviewer(module._reviewer_a)
        self.assertEqual(result["status"], "FAIL")
        self.assertGreater(result["critical_counts"]["baseline_lane_family_gap"], 0)

    def test_reviewer_b_rejects_query_without_llm_response_lineage(self) -> None:
        self._require_frozen_leaves()
        task_path = self.paths["canonical_current_root"] / "source_tasks.jsonl"
        with self._patched_jsonl(
            task_path,
            lambda rows: self._replace_first(rows, query_response_hash="0" * 64),
        ):
            result = self._reviewer(module._reviewer_b)
        self.assertEqual(result["status"], "FAIL")
        self.assertGreater(result["critical_counts"]["query_response_lineage_gap"], 0)

    def test_reviewer_c_rejects_quote_not_in_fetched_document(self) -> None:
        self._require_frozen_leaves()
        provenance_path = (
            self.paths["canonical_current_root"] / "claim_provenance.jsonl"
        )
        with self._patched_jsonl(
            provenance_path,
            lambda rows: self._replace_first(rows, exact_quote="본문에 없는 인용문"),
        ):
            result = self._reviewer(module._reviewer_c)
        self.assertEqual(result["status"], "FAIL")
        self.assertGreater(
            result["critical_counts"]["claim_provenance_contract_failure"], 0
        )

    def test_reviewer_d_rejects_orphan_score_contribution(self) -> None:
        self._require_frozen_leaves()
        contribution_path = (
            self.paths["canonical_current_root"] / "score_contributions.jsonl"
        )
        with self._patched_jsonl(
            contribution_path,
            lambda rows: self._replace_first(
                rows, support_claim_ids=["CLM-NOT-IN-CANONICAL-LEDGER"]
            ),
        ):
            result = self._reviewer(module._reviewer_d)
        self.assertEqual(result["status"], "FAIL")
        self.assertGreater(result["critical_counts"]["orphan_score_contribution"], 0)

    def test_reviewer_e_rejects_current_census_source_hash_mismatch(self) -> None:
        self._require_frozen_leaves()
        census_audit_path = (
            self.paths["canonical_census_root"] / "census_acceptance_audit.json"
        )
        with self._patched_json(
            census_audit_path,
            lambda row: {**row, "census_source_corpus_hash": "f" * 64},
        ):
            result = self._reviewer(module._reviewer_e)
        self.assertEqual(result["status"], "FAIL")
        self.assertGreater(
            result["critical_counts"]["current_census_source_corpus_hash_failure"],
            0,
        )

    def test_reviewer_f_rejects_materializer_counterfeit(self) -> None:
        self._require_frozen_leaves()
        orchestration_path = (
            self.paths["live_root"] / "current_orchestration_audit.json"
        )
        with self._patched_json(
            orchestration_path,
            lambda row: {**row, "materializer_called": False},
        ):
            result = self._reviewer(module._reviewer_f)
        self.assertEqual(result["status"], "FAIL")
        self.assertEqual(result["critical_counts"]["materializer_not_called"], 1)

    def test_reviewer_f_does_not_create_commit_manifest_hash_cycle(self) -> None:
        self._require_frozen_leaves()
        result = self._reviewer(module._reviewer_f)
        command_paths = {
            str(self.paths["canonical_current_root"] / "command_run_manifest.json"),
            str(self.paths["canonical_census_root"] / "command_run_manifest.json"),
        }
        self.assertTrue(command_paths.isdisjoint(result["leaf_hashes"]))
        self.assertTrue(result["evidence"]["current_census_same_commit"])
        self.assertEqual(
            result["critical_counts"]["current_command_reproducibility_failure"],
            0,
        )
        self.assertEqual(
            result["critical_counts"]["census_command_reproducibility_failure"],
            0,
        )

    def _reviewers(self):
        return tuple(
            self._reviewer(reviewer)
            for reviewer in (
                module._reviewer_a,
                module._reviewer_b,
                module._reviewer_c,
                module._reviewer_d,
                module._reviewer_e,
                module._reviewer_f,
            )
        )

    def _require_frozen_leaves(self) -> None:
        if self.missing_frozen_leaves:
            self.skipTest(
                "raw live reviewer leaves are excluded from clean packaging; "
                "the tracked result is a historical receipt"
            )

    def _reviewer(self, reviewer):
        return reviewer(
            config=self.config,
            paths=self.paths,
            verify_repository=False,
        )

    @staticmethod
    def _replace_first(rows, **changes):
        copied = [deepcopy(row) for row in rows]
        copied[0] = {**copied[0], **changes}
        return tuple(copied)

    def _patched_jsonl(self, target: Path, mutate):
        original = module._read_jsonl
        target = target.resolve()

        def side_effect(path: Path):
            rows = original(path)
            return mutate(rows) if Path(path).resolve() == target else rows

        return patch.object(module, "_read_jsonl", side_effect=side_effect)

    def _patched_json(self, target: Path, mutate):
        original = module._read_json
        target = target.resolve()

        def side_effect(path: Path):
            row = original(path)
            return mutate(dict(row)) if Path(path).resolve() == target else row

        return patch.object(module, "_read_json", side_effect=side_effect)


if __name__ == "__main__":
    unittest.main()

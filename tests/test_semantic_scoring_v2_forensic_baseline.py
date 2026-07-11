from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring.semantic_v2_forensic import (
    compile_semantic_scoring_v2_forensic_baseline,
)


class SemanticScoringV2ForensicBaselineTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    @classmethod
    def setUpClass(cls) -> None:
        cls.audit = compile_semantic_scoring_v2_forensic_baseline(
            repo_root=cls.ROOT
        )

    def test_support_type_and_silent_zero_defects_are_reproduced(self) -> None:
        metrics = self.audit["metrics"]
        self.assertEqual(metrics["declared_support_type_count"], 7)
        self.assertEqual(metrics["cap_table_support_type_count"], 4)
        self.assertEqual(metrics["missing_support_type_count"], 3)
        self.assertEqual(
            self.audit["missing_support_types"],
            ["PARTIAL_BRIDGE", "RISK_OPEN", "RISK_RESOLVED"],
        )
        self.assertEqual(
            metrics["positive_proposal_zeroed_by_missing_cap_count"], 9
        )
        self.assertEqual(
            metrics["counter_proposal_zeroed_by_missing_cap_count"], 1
        )

    def test_question_scope_counter_stage_and_eligibility_defects_exist(self) -> None:
        metrics = self.audit["metrics"]
        self.assertGreater(
            metrics["supported_question_absent_component_count"], 0
        )
        self.assertGreater(
            metrics["partially_supported_question_absent_component_count"],
            0,
        )
        self.assertGreater(metrics["cross_business_question_closure_count"], 0)
        self.assertGreater(
            metrics["same_document_duplicate_credit_count"], 0
        )
        self.assertEqual(
            metrics["support_counter_component_counter_effect_zero_count"], 1
        )
        self.assertEqual(metrics["accepted_claim_event_score_injection_count"], 2)
        self.assertEqual(metrics["eligibility_field_contradiction_count"], 39)

    def test_tesla_foundry_exact_row_is_recorded(self) -> None:
        rows = [
            row
            for row in self.audit["mechanism_failure_rows"]
            if row["claim_id"] == "CLM-464ca5cde1b30c363997"
        ]
        self.assertTrue(rows)
        self.assertTrue(
            all(row["failure_reason"] == "WRONG_BUSINESS_SEGMENT_FOUNDRY" for row in rows)
        )
        self.assertTrue(
            any(
                row["question_family_id"]
                == "current_customer_allocation_commitment"
                for row in rows
            )
        )

    def test_all_phase58_artifacts_exist_and_match_key_counts(self) -> None:
        docs = self.ROOT / "docs/operational"
        required = (
            "e2r_semantic_scoring_v2_forensic_baseline.md",
            "e2r_support_type_cap_matrix_before.json",
            "e2r_question_component_consistency_before.json",
            "e2r_business_mechanism_scope_failures_before.json",
            "e2r_counter_credit_failures_before.json",
            "e2r_fact_duplication_before.json",
            "e2r_stage_event_injection_before.json",
        )
        self.assertEqual([name for name in required if not (docs / name).is_file()], [])
        cap = json.loads(
            (docs / "e2r_support_type_cap_matrix_before.json").read_text()
        )
        self.assertEqual(cap["missing_support_types"], self.audit["missing_support_types"])
        stage = json.loads(
            (docs / "e2r_stage_event_injection_before.json").read_text()
        )
        self.assertEqual(stage["eligibility_field_contradiction_count"], 39)


if __name__ == "__main__":
    unittest.main()

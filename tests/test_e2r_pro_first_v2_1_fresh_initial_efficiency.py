from __future__ import annotations

import unittest

from e2r.pro_first.fresh_session import evaluate_initial_efficiency


class FreshInitialEfficiencyGateTest(unittest.TestCase):
    def test_eight_of_ten_material_candidates_passes_initial_gate(self) -> None:
        gate = self._evaluate(accepted_count=8)

        self.assertTrue(gate.passed)
        self.assertEqual(gate.receipt["post_preflight_acceptance_ratio"], 0.8)
        self.assertEqual(gate.receipt["initial_material_candidate_count"], 10)
        self.assertEqual(gate.receipt["post_preflight_accepted_material_count"], 8)
        self.assertEqual(gate.receipt["failure_reasons"], [])
        self.assertFalse(gate.receipt["score_authority"])
        self.assertFalse(gate.receipt["stage_authority"])

    def test_seven_of_ten_is_sealed_before_repair_can_mask_ratio(self) -> None:
        gate = self._evaluate(accepted_count=7)

        self.assertFalse(gate.passed)
        self.assertIn(
            "INITIAL_ACCEPTANCE_RATIO_BELOW_80_PERCENT",
            gate.receipt["failure_reasons"],
        )
        self.assertEqual(gate.receipt["repair_pass_count"], 0)
        self.assertTrue(gate.receipt["publication_withheld"])

    def test_structural_defect_fails_even_when_verifier_ratio_is_high(self) -> None:
        dossier = self._dossier()
        dossier["material_facts"][0]["question_family_ids"] = []
        gate = self._evaluate(accepted_count=10, dossier=dossier)

        self.assertFalse(gate.passed)
        self.assertIn(
            "MATERIAL_QUESTION_UNBOUND",
            gate.receipt["failure_reasons"],
        )

    def test_local_and_representation_defects_cannot_be_sent_to_pro(self) -> None:
        gate = self._evaluate(
            accepted_count=10,
            verification_receipt={
                "local_normalizable_sent_to_pro_count": 1,
                "source_representation_sent_to_pro_count": 1,
                "unclassified_rejection_count": 0,
            },
        )

        self.assertFalse(gate.passed)
        self.assertIn("LOCAL_NORMALIZABLE_SENT_TO_PRO", gate.receipt["failure_reasons"])
        self.assertIn(
            "SOURCE_REPRESENTATION_SENT_TO_PRO",
            gate.receipt["failure_reasons"],
        )

    def test_six_genuine_repairs_fail_ten_candidate_efficiency_limit(self) -> None:
        rejection_rows = [
            {
                "candidate_id": f"FACT-{index:02d}",
                "cause_class": "GENUINE_SEMANTIC_OR_SOURCE_DEFECT",
                "material": True,
                "send_to_pro_allowed": True,
            }
            for index in range(6)
        ]
        gate = self._evaluate(
            accepted_count=8,
            rejection_rows=rejection_rows,
        )

        self.assertFalse(gate.passed)
        self.assertEqual(gate.receipt["genuine_semantic_repair_candidate_limit"], 5)
        self.assertIn(
            "GENUINE_SEMANTIC_REPAIR_ROSTER_TOO_LARGE",
            gate.receipt["failure_reasons"],
        )

    def _evaluate(
        self,
        *,
        accepted_count: int,
        dossier: dict | None = None,
        verification_receipt: dict | None = None,
        rejection_rows: list[dict] | None = None,
    ):
        payload = dossier or self._dossier()
        rows = [
            {
                "dossier_fact_id": f"FACT-{index:02d}",
                "status": (
                    "ACCEPTED_CURRENT"
                    if index < accepted_count
                    else "REJECTED_QUOTE_MISMATCH"
                ),
            }
            for index in range(10)
        ]
        return evaluate_initial_efficiency(
            dossier=payload,
            mandatory_question_ids=("Q01", "Q02"),
            verification_rows=rows,
            rejection_rows=rejection_rows or [],
            verification_receipt=verification_receipt
            or {
                "local_normalizable_sent_to_pro_count": 0,
                "source_representation_sent_to_pro_count": 0,
                "unclassified_rejection_count": 0,
            },
            prompt_char_count=50_000,
            response_char_count=25_000,
            initial_research_seconds=30.0,
            total_elapsed_seconds=40.0,
            job_id="PROJOB-FRESH",
            run_id="PRORUN-FRESH",
            conversation_id="fresh-conversation",
        )

    @staticmethod
    def _dossier() -> dict:
        return {
            "source_documents": [
                {
                    "source_document_id": f"SRC-{index:02d}",
                    "canonical_url": f"https://example.com/source/{index}",
                }
                for index in range(10)
            ],
            "material_facts": [
                {
                    "dossier_fact_id": f"FACT-{index:02d}",
                    "source_document_id": f"SRC-{index:02d}",
                    "question_family_ids": ["Q01" if index % 2 == 0 else "Q02"],
                    "verifier_preflight": {
                        "derived_calculation_mixed_into_fact": False,
                    },
                }
                for index in range(10)
            ],
            "counterfacts": [],
            "resolution_facts": [],
            "question_family_results": [
                {"question_family_id": "Q01"},
                {"question_family_id": "Q02"},
            ],
        }


if __name__ == "__main__":
    unittest.main()

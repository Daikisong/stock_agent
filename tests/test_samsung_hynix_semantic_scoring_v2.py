from __future__ import annotations

import json
import unittest
from pathlib import Path


class SamsungHynixSemanticScoringV2Tests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]
    LIVE_ROOT = ROOT / "output/evidence_to_score_v2/live_2026-07-11"
    FORBIDDEN_TERMINAL_STATUSES = {
        "UNKNOWN_UNINVESTIGATED",
        "SOURCE_PENDING",
        "PROVIDER_PENDING",
        "BUDGET_PENDING",
        "CONTRADICTED_OPEN",
        "SCORING_PIPELINE_ERROR",
    }

    @classmethod
    def setUpClass(cls) -> None:
        cls.raw_dossiers_available = all(
            (
                cls.LIVE_ROOT
                / target_id
                / "atomic_stage_decision.json"
            ).is_file()
            for target_id in ("005930", "000660")
        )
        cls.tracked_receipts = {
            "005930": (
                cls.ROOT
                / "docs/operational/e2r_samsung_semantic_scoring_v2.md"
            ).read_text(encoding="utf-8"),
            "000660": (
                cls.ROOT
                / "docs/operational/e2r_sk_hynix_semantic_scoring_v2.md"
            ).read_text(encoding="utf-8"),
        }

    def test_both_live_dossiers_are_full_deterministic_terminal_scores(self) -> None:
        expected = {
            "005930": {"claims": 18, "validated": 37, "score": 18.159977},
            "000660": {"claims": 33, "validated": 115, "score": 19.120509},
        }
        if not self.raw_dossiers_available:
            # This is tracked-receipt consistency only.  It does not claim the
            # omitted output/** dossiers were rebuilt in a clean checkout.
            for target_id, metrics in expected.items():
                text = self.tracked_receipts[target_id]
                self.assertIn("`FULL_E2R_100`", text)
                self.assertIn(f"`{metrics['score']}점`", text)
                self.assertIn("`full_score_valid=true`", text)
                self.assertIn(
                    f"organic accepted claim {metrics['claims']}건",
                    text,
                )
                self.assertIn(
                    f"{metrics['validated']}건",
                    text,
                )
                self.assertIn("impact", text)
            return
        for target_id, metrics in expected.items():
            with self.subTest(target_id=target_id):
                root = self.LIVE_ROOT / target_id
                decision = self._json(root / "atomic_stage_decision.json")
                stage_trace = self._json(root / "stagecourt_trace.json")
                components = self._jsonl(root / "component_assessments.jsonl")
                closures = self._jsonl(root / "semantic_closure_trace.jsonl")
                comparisons = self._jsonl(root / "material_fact_comparison.jsonl")

                self.assertTrue(decision["full_score_valid"])
                self.assertEqual(decision["score_type"], "FULL_E2R_100")
                self.assertEqual(decision["decision_status"], "FINAL")
                self.assertEqual(decision["canonical_stage"], "0")
                self.assertAlmostEqual(
                    decision["full_e2r_score"], metrics["score"], places=6
                )
                self.assertEqual(
                    stage_trace["canonical_stage"], decision["canonical_stage"]
                )
                self.assertEqual(
                    stage_trace["decision_id"],
                    decision["decision_id"],
                )
                self.assertEqual(stage_trace["full_thesis_stage"], "0")
                self.assertEqual(stage_trace["stage_event_claim_ids"], [])
                self.assertEqual(
                    len(self._jsonl(root / "accepted_current_claims.jsonl")),
                    metrics["claims"],
                )
                self.assertEqual(
                    len(self._jsonl(root / "claim_impacts_validated.jsonl")),
                    metrics["validated"],
                )
                self.assertEqual(len(components), 7)
                self.assertEqual(len(closures), 13)
                self.assertFalse(
                    self.FORBIDDEN_TERMINAL_STATUSES
                    & {row["status"] for row in components}
                )
                self.assertFalse(
                    self.FORBIDDEN_TERMINAL_STATUSES
                    & {row["reconciled_closure_status"] for row in closures}
                )
                self.assertTrue(comparisons)
                self.assertTrue(
                    all(
                        row["semantic_match"]
                        and row["source_quality_match"]
                        and row["currentness_match"]
                        and row["mechanism_scope_match"]
                        for row in comparisons
                    )
                )

    def test_samsung_hbm4_shipment_scores_without_foundry_cross_wire(self) -> None:
        if not self.raw_dossiers_available:
            text = self.tracked_receipts["005930"]
            self.assertIn("HBM4 양산 출하", text)
            self.assertIn("Tesla/Foundry 관련 claim", text)
            self.assertIn("0이다", text)
            return
        root = self.LIVE_ROOT / "005930"
        production_facts = self._jsonl(root / "production_material_facts.jsonl")
        validated = self._jsonl(root / "claim_impacts_validated.jsonl")
        accepted = self._jsonl(root / "accepted_current_claims.jsonl")

        self.assertTrue(
            any(
                row["question_family_id"] == "shipment_mass_production_generation"
                and row["fact_role"] == "SUPPORT"
                and "hbm4" in row["normalized_object"]
                for row in production_facts
            )
        )
        self.assertTrue(
            any(
                row["primitive_id"] == "shipment_or_revenue_mix"
                and float(row["validated_credit_fraction"]) > 0
                for row in validated
            )
        )
        accepted_text = json.dumps(accepted, ensure_ascii=False).casefold()
        self.assertNotIn("tesla", accepted_text)
        self.assertNotIn("foundry", accepted_text)
        self.assertNotIn("테슬라", accepted_text)
        self.assertNotIn("파운드리", accepted_text)

    def test_hynix_shortage_is_nonzero_and_substrate_remains_zero_credit(self) -> None:
        if not self.raw_dossiers_available:
            text = self.tracked_receipts["000660"]
            self.assertIn("capacity constraint", text)
            self.assertIn("nonzero support", text)
            self.assertIn("substrate 9개사 공급", text)
            self.assertIn("profile/non-scoring guard", text)
            return
        validated = self._jsonl(
            self.LIVE_ROOT / "000660/claim_impacts_validated.jsonl"
        )
        shortage = [
            row
            for row in validated
            if row["primitive_id"] == "hbm_capacity_constraint"
        ]
        substrate = [
            row
            for row in validated
            if row["primitive_id"] == "package_substrate_sympathy"
        ]
        self.assertTrue(shortage)
        self.assertTrue(
            any(float(row["validated_credit_fraction"]) > 0 for row in shortage)
        )
        self.assertTrue(substrate)
        self.assertTrue(
            all(float(row["support_credit_fraction"]) == 0 for row in substrate)
        )
        self.assertEqual(
            {row["component_id"] for row in substrate},
            {"information_confidence"},
        )

    @staticmethod
    def _json(path: Path):
        return json.loads(path.read_text(encoding="utf-8"))

    @staticmethod
    def _jsonl(path: Path):
        return [
            json.loads(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]


if __name__ == "__main__":
    unittest.main()

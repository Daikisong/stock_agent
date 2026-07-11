from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPLAY_PATH = ROOT / "docs/operational/e2r_c06_historical_component_replay.json"


def _case(case_id: str) -> dict:
    audit = json.loads(REPLAY_PATH.read_text(encoding="utf-8"))
    return next(row for row in audit["cases"] if row["case_id"] == case_id)


class SamsungQ1ClaimComponentImpactTests(unittest.TestCase):
    def test_asp_and_record_revenue_do_not_become_customer_allocation(self) -> None:
        row = _case("C06-SAMSUNG-20250131-REOPEN-CAP")
        self.assertEqual(row["primitive_id"], "actual_earnings_conversion")
        self.assertNotIn("earnings_visibility", row["predicted_component_ids"])
        self.assertNotIn("bottleneck_pricing", row["predicted_component_ids"])
        unsupported = {
            aspect.lower()
            for proposal in row["proposal_rows"]
            for aspect in proposal["unsupported_aspects"]
        }
        self.assertTrue(any("customer" in aspect for aspect in unsupported))
        self.assertTrue(any("capacity" in aspect for aspect in unsupported))

    def test_asp_and_record_revenue_keep_bounded_economic_impacts(self) -> None:
        row = _case("C06-SAMSUNG-20250131-REOPEN-CAP")
        self.assertEqual(row["adjudication_status"], "IMPACT_ADJUDICATION_PASS")
        self.assertEqual(row["forbidden_component_count"], 0)
        self.assertEqual(
            set(row["predicted_component_ids"]),
            {"eps_fcf_explosion", "information_confidence"},
        )
        self.assertGreater(len(row["proposal_rows"]), 0)

    def test_hbm_product_keyword_does_not_become_sold_out_capacity(self) -> None:
        row = _case("C06-SKHYNIX-PRODUCT-SPEC-GUARD")
        self.assertEqual(row["primitive_id"], "hbm_product_profile")
        self.assertEqual(row["predicted_component_ids"], ["information_confidence"])
        self.assertNotIn("earnings_visibility", row["predicted_component_ids"])
        self.assertNotIn("bottleneck_pricing", row["predicted_component_ids"])

    def test_package_profile_does_not_become_target_hbm_allocation(self) -> None:
        row = _case("C06-SAMSUNG-PACKAGE-PROFILE-GUARD")
        self.assertEqual(row["primitive_id"], "package_substrate_sympathy")
        self.assertEqual(row["predicted_component_ids"], ["information_confidence"])
        self.assertNotIn("earnings_visibility", row["predicted_component_ids"])
        self.assertNotIn("bottleneck_pricing", row["predicted_component_ids"])


if __name__ == "__main__":
    unittest.main()

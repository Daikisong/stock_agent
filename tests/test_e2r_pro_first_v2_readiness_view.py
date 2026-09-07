from __future__ import annotations

import json
from pathlib import Path
import unittest

from e2r.pro_first.readiness_view import project_full_thesis_readiness


ROOT = Path(__file__).resolve().parents[1]
LEGACY = (
    ROOT
    / "docs/operational/e2r_pro_first_v1/live_canary_acceptance_2026-08-22.json"
)


class ProFirstV2ReadinessViewTest(unittest.TestCase):
    def test_legacy_live_canary_is_diagnostic_until_v2_saturation_exists(self) -> None:
        before = LEGACY.read_bytes()
        legacy = json.loads(before)

        view = project_full_thesis_readiness(legacy)

        self.assertEqual(
            view["transport_canary_status"],
            "PRO_FIRST_END_TO_END_TRANSPORT_CANARY_PASS",
        )
        self.assertEqual(
            view["first_pass_status"],
            "FIRST_PASS_PARTIAL_CORPUS_DIAGNOSTIC_ONLY",
        )
        self.assertEqual(view["first_pass_diagnostic_score"], 23.202275)
        self.assertEqual(view["first_pass_diagnostic_stage"], "0")
        self.assertIsNone(view["full_thesis_score"])
        self.assertIsNone(view["full_thesis_stage"])
        self.assertFalse(view["full_thesis_score_valid"])
        self.assertEqual(
            view["publication_status"],
            "WITHHELD_PENDING_RESEARCH_SATURATION",
        )
        self.assertEqual(LEGACY.read_bytes(), before)

    def test_full_thesis_requires_every_material_pending_roster_to_be_empty(self) -> None:
        legacy = json.loads(LEGACY.read_text(encoding="utf-8"))
        incomplete = {
            "status": "FULL_THESIS_READY",
            "full_thesis_score_valid": True,
            "mandatory_nonterminal_count": 0,
            "public_searchable_material_gap_count": 1,
            "verifier_repair_pending_count": 0,
            "core_provider_parser_pending_count": 0,
            "full_thesis_score": 70.0,
            "full_thesis_stage": "2",
        }

        view = project_full_thesis_readiness(
            legacy,
            saturation_receipt=incomplete,
        )

        self.assertFalse(view["full_thesis_score_valid"])
        self.assertIsNone(view["full_thesis_score"])
        self.assertEqual(view["research_status"], "RESEARCH_INCOMPLETE")


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring import audit_stagecourt_event_separation


class StageCourtEventSeparationTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_operational_audit_matches_recompiled_decisions(self) -> None:
        actual = audit_stagecourt_event_separation()
        expected = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_full_thesis_event_separation_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, expected)
        self.assertEqual(actual["status"], "STAGECOURT_EVENT_SEPARATION_PASS")
        self.assertEqual(actual["critical_count_sum"], 0)

    def test_claim_count_and_event_overlay_never_change_full_thesis_stage(self) -> None:
        audit = audit_stagecourt_event_separation()
        stages = {
            audit["no_event_decision"]["canonical_stage"],
            audit["more_generic_claims_decision"]["canonical_stage"],
            audit["explicit_event_decision"]["canonical_stage"],
        }
        self.assertEqual(len(stages), 1)
        self.assertNotEqual(
            audit["more_generic_claims_decision"]["canonical_stage"], "1"
        )

    def test_explicit_quality_contract_creates_overlay_only(self) -> None:
        audit = audit_stagecourt_event_separation()
        explicit = audit["explicit_event_decision"]
        generic = audit["generic_boolean_decision"]
        self.assertEqual(explicit["event_overlay"]["status"], "EVENT_OVERLAY_ACTIVE")
        self.assertEqual(explicit["event_overlay"]["stage_signal"], "EVENT_WATCH")
        self.assertEqual(explicit["event_overlay"]["canonical_stage_effect"], "NONE")
        self.assertEqual(generic["event_overlay"]["status"], "NO_EVENT_OVERLAY")

    def test_required_hard_acceptance_counts_are_zero(self) -> None:
        critical = audit_stagecourt_event_separation()["critical_counts"]
        for name in (
            "claim_count_event_boost_count",
            "generic_claim_high_quality_event_count",
            "full_thesis_event_score_injection_count",
        ):
            self.assertEqual(critical[name], 0)


if __name__ == "__main__":
    unittest.main()

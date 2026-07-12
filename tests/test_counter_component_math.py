from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring import audit_counter_component_math


class CounterComponentMathTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def setUp(self) -> None:
        self.audit = audit_counter_component_math()

    def test_audit_matches_committed_source_backed_canaries(self) -> None:
        expected = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_counter_component_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(self.audit, expected)
        self.assertEqual(self.audit["status"], "COUNTER_COMPONENT_MATH_PASS")
        self.assertEqual(self.audit["critical_count_sum"], 0)

    def test_open_counter_blocks_finalization_and_preserves_both_planes(self) -> None:
        scenario = self.audit["scenarios"]["open_qualification_counter"]
        component = scenario["active_component_assessments"][0]
        self.assertEqual(component["status"], "CONTRADICTED_OPEN")
        self.assertEqual(component["support_points"], 1.8)
        self.assertEqual(component["counter_effect"], 1.8)
        self.assertEqual(component["net_points"], 0.0)
        self.assertFalse(scenario["full_score_valid"])

    def test_bounded_counter_keeps_research_cap_and_net_points(self) -> None:
        scenario = self.audit["scenarios"]["bounded_asp_counter"]
        component = scenario["active_component_assessments"][0]
        self.assertEqual(component["status"], "SUPPORT_WITH_COUNTER_CAP")
        self.assertEqual(component["support_points"], 3.0)
        self.assertEqual(component["counter_effect"], 2.0)
        self.assertEqual(component["net_points"], 1.0)
        self.assertTrue(scenario["full_score_valid"])

    def test_linked_resolution_releases_penalty_without_erasing_history(self) -> None:
        scenario = self.audit["scenarios"][
            "resolved_qualification_counter"
        ]
        component = scenario["active_component_assessments"][0]
        subcriterion = scenario["active_subcriterion_scores"][0]
        self.assertEqual(component["status"], "RESOLVED_COUNTER")
        self.assertEqual(component["counter_effect"], 0.0)
        self.assertEqual(component["net_points"], 1.8)
        self.assertEqual(
            subcriterion["resolved_counter_impact_ids"],
            ["IMPACT-RESOLVED-COUNTER"],
        )

    def test_unlinked_resolution_cannot_clear_another_counter(self) -> None:
        scenario = self.audit["scenarios"][
            "unlinked_resolution_keeps_counter_open"
        ]
        component = scenario["active_component_assessments"][0]
        subcriterion = scenario["active_subcriterion_scores"][0]
        self.assertEqual(component["status"], "CONTRADICTED_OPEN")
        self.assertEqual(component["counter_effect"], 1.8)
        self.assertEqual(subcriterion["resolution_effect"], 0.0)
        self.assertFalse(scenario["full_score_valid"])

    def test_capacity_expansion_support_and_scarcity_counter_both_survive(self) -> None:
        scenario = self.audit["scenarios"][
            "capacity_support_and_scarcity_counter"
        ]
        by_component = {
            row["component_id"]: row
            for row in scenario["active_component_assessments"]
        }
        self.assertGreater(
            by_component["capital_allocation"]["support_points"], 0
        )
        self.assertGreater(
            by_component["bottleneck_pricing"]["counter_effect"], 0
        )

    def test_capacity_counter_in_another_subcriterion_caps_same_component(self) -> None:
        scenario = self.audit["scenarios"][
            "same_component_distinct_subcriterion_counter"
        ]
        component = scenario["active_component_assessments"][0]
        self.assertEqual(component["status"], "SUPPORT_WITH_COUNTER_CAP")
        self.assertGreater(component["support_points"], 0)
        self.assertGreater(component["counter_effect"], 0)
        self.assertTrue(scenario["full_score_valid"])


if __name__ == "__main__":
    unittest.main()

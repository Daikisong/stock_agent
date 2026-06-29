import unittest

from e2r.research_brain.v2_archetype_router import build_router_confusion_matrix, route_candidate_event_v2
from e2r.research_brain.v2_schemas import CandidateEventV2
from research_brain_v2_test_helpers import load_v2_cards


class ResearchBrainV2ArchetypeRouterTests(unittest.TestCase):
    def test_mandatory_replays_route_to_expected_top1(self):
        matrix = build_router_confusion_matrix(load_v2_cards())
        summary = matrix["summary"]
        self.assertTrue(summary["mandatory_six_top1_pass"])
        for archetype_id, row in summary["mandatory_six_results"].items():
            self.assertEqual(row["primary_archetype"], archetype_id)

    def test_c01_c36_top3_accuracy_is_complete(self):
        matrix = build_router_confusion_matrix(load_v2_cards())
        self.assertEqual(matrix["summary"]["top3_accuracy"], 1.0)
        self.assertGreaterEqual(matrix["summary"]["top1_accuracy"], 0.9)

    def test_low_confidence_routes_to_pending_disambiguation(self):
        event = CandidateEventV2(
            candidate_event_id="ambiguous",
            symbol="000000",
            company_name="모호",
            event_date="2026-06-29",
            detected_at="2026-06-29",
            source_family="Manual",
            source_id="none",
            event_type="other",
            event_summary="unclear event with no operating mechanism",
        )
        route = route_candidate_event_v2(event, load_v2_cards())
        self.assertEqual(route.status, "ARCTYPE_PENDING_DISAMBIGUATION")
        self.assertIsNone(route.primary_archetype)


if __name__ == "__main__":
    unittest.main()

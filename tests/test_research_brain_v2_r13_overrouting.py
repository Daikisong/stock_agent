import unittest

from e2r.research_brain.v2_archetype_router import build_router_confusion_matrix, route_candidate_event_v2
from e2r.research_brain.v2_schemas import CandidateEventV2
from research_brain_v2_test_helpers import load_v2_cards


class ResearchBrainV2R13OverroutingTests(unittest.TestCase):
    def test_r13_overroute_count_is_zero_for_non_r13_fixtures(self):
        matrix = build_router_confusion_matrix(load_v2_cards())
        self.assertEqual(matrix["summary"]["r13_overroute_count"], 0)

    def test_c06_event_with_red_team_concern_keeps_c06_primary_and_r13_overlay(self):
        cards = load_v2_cards()
        event = CandidateEventV2(
            candidate_event_id="case-c06-risk",
            symbol="000660",
            company_name="SK하이닉스",
            event_date="2026-06-29",
            detected_at="2026-06-29",
            source_family="DART",
            source_id="fixture",
            event_type="operating_event",
            raw_reason_codes=("HBM_CUSTOMER_CAPACITY",),
            event_title="HBM capacity allocation with false positive red team concern",
            event_summary="HBM memory customer allocation capacity sold-out qualification revenue mix false positive risk guard",
            issuer_directness="DIRECT",
        )
        route = route_candidate_event_v2(event, cards)
        self.assertEqual(route.primary_archetype, "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertTrue(any(item.startswith("R13_") for item in route.secondary_overlays))

    def test_explicit_r13_review_can_route_to_r13(self):
        cards = load_v2_cards()
        event = CandidateEventV2(
            candidate_event_id="case-r13",
            symbol="R13",
            company_name="R13 fixture",
            event_date="2026-06-29",
            detected_at="2026-06-29",
            source_family="ReplayFixture",
            source_id="r13",
            event_type="red_team_review",
            raw_reason_codes=("EXPLICIT_R13_REVIEW",),
            event_title="cross archetype red team false positive review",
            event_summary="cross archetype red team false positive review guardrail accounting trust validation",
        )
        route = route_candidate_event_v2(event, cards)
        self.assertTrue(route.primary_archetype and route.primary_archetype.startswith("R13_"))
        self.assertTrue(route.r13_primary_allowed)

    def test_c15_raw_commodity_headline_keeps_c15_primary_not_r13(self):
        cards = load_v2_cards()
        event = CandidateEventV2(
            candidate_event_id="case-c15-raw",
            symbol="C15",
            company_name="소재",
            event_date="2026-06-29",
            detected_at="2026-06-29",
            source_family="TrustedNews",
            source_id="fixture",
            event_type="operating_event",
            raw_reason_codes=("MATERIAL_SPREAD",),
            event_title="material spread raw commodity headline",
            event_summary="material spread supercycle raw commodity headline pass-through realized margin false positive guard",
        )
        route = route_candidate_event_v2(event, cards)
        self.assertEqual(route.primary_archetype, "C15_MATERIAL_SPREAD_SUPERCYCLE")
        self.assertNotEqual(route.primary_archetype, "R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW")


if __name__ == "__main__":
    unittest.main()

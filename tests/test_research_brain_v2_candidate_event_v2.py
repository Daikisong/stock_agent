import unittest

from e2r.research_brain.v2_candidate_events import candidate_events_v2_from_mapping, cluster_candidate_events_v2


class ResearchBrainV2CandidateEventTests(unittest.TestCase):
    def test_multiple_reason_families_split_into_multiple_events(self):
        row = {
            "symbol": "123456",
            "company_name": "테스트",
            "as_of_date": "2026-06-29",
            "candidate_source_path": "official_cheap_scan",
            "reason_codes": ["DISC_SUPPLY_CONTRACT", "DISC_FACILITY_INVESTMENT", "PRICE_VOLUME_SPIKE"],
            "evidence_ids": ["dart:1"],
        }
        events = candidate_events_v2_from_mapping(row)
        self.assertEqual({event.event_type for event in events}, {"supply_contract", "facility_investment", "price_relative_strength"})
        self.assertEqual(len({event.candidate_event_id for event in events}), 3)

    def test_event_id_is_deterministic(self):
        row = {
            "symbol": "123456",
            "company_name": "테스트",
            "as_of_date": "2026-06-29",
            "reason_codes": ["DISC_SUPPLY_CONTRACT"],
        }
        first = candidate_events_v2_from_mapping(row)[0]
        second = candidate_events_v2_from_mapping(row)[0]
        self.assertEqual(first.candidate_event_id, second.candidate_event_id)

    def test_cluster_groups_same_symbol_date_source_family(self):
        row = {
            "symbol": "123456",
            "company_name": "테스트",
            "as_of_date": "2026-06-29",
            "candidate_source_path": "official_cheap_scan",
            "reason_codes": ["DISC_SUPPLY_CONTRACT", "PRICE_VOLUME_SPIKE"],
        }
        report = cluster_candidate_events_v2(candidate_events_v2_from_mapping(row))
        self.assertEqual(report["summary"]["cluster_count"], 1)
        self.assertEqual(report["summary"]["multi_event_cluster_count"], 1)


if __name__ == "__main__":
    unittest.main()

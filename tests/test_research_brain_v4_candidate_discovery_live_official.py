import unittest
from datetime import date

from e2r.research_brain.v4_production_orchestrator import discover_daily_candidate_events_v4
from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
from research_brain_v4_test_helpers import c06_source_task, sample_v4_event


class ResearchBrainV4CandidateDiscoveryLiveOfficialTests(unittest.TestCase):
    def test_daily_discovery_finds_current_real_snapshot_candidates(self):
        events = discover_daily_candidate_events_v4(repo_root=".", as_of_date=date(2026, 6, 29), universe_limit=30)
        self.assertGreaterEqual(len(events), 30)
        self.assertEqual(len({event.candidate_event_id for event in events}), len(events))
        source_families = {event.source_family for event in events}
        self.assertTrue({"DART", "KIND", "KRX", "CompanyGuide"}.issubset(source_families))
        self.assertTrue(all(event.event_date <= "2026-06-29" for event in events))

    def test_live_official_mode_fetches_snapshot_or_reports_provider_failed(self):
        result = SourceAcquisitionRunnerV4(mode="live_official_only").acquire(
            event=sample_v4_event(),
            task=c06_source_task(),
            as_of_date=date(2026, 6, 29),
        )
        self.assertIn(result.status, {"PARSED", "PROVIDER_FAILED"})
        if result.status == "PARSED":
            self.assertTrue(result.fetched_document_ids)
        else:
            self.assertTrue(result.provider_errors)


if __name__ == "__main__":
    unittest.main()

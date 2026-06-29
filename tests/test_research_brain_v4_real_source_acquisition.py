import unittest
from datetime import date

from e2r.research_brain.v4_source_acquisition_runner import SourceAcquisitionRunnerV4
from research_brain_v4_test_helpers import c06_source_task, sample_v4_event


class ResearchBrainV4RealSourceAcquisitionTests(unittest.TestCase):
    def test_companyguide_snapshot_fetches_real_document_and_anchor(self):
        result = SourceAcquisitionRunnerV4(mode="frozen_real_source_snapshot").acquire(
            event=sample_v4_event(),
            task=c06_source_task(),
            as_of_date=date(2026, 6, 29),
        )
        self.assertEqual(result.status, "PARSED")
        self.assertGreaterEqual(len(result.fetched_document_ids), 1)
        self.assertEqual(len(result.fetched_document_ids), len(result.anchor_ids))
        self.assertTrue(all(url.startswith("snapshot://company_guide/") for url in result.document_urls))
        self.assertNotIn(sample_v4_event().event_summary, result.document_text_by_id.values())


if __name__ == "__main__":
    unittest.main()

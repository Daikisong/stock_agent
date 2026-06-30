import unittest

from census_v3_test_helpers import census_v3_artifacts


class CensusV3NewsIrReportNotIgnoredTests(unittest.TestCase):
    def test_report_events_are_ingested_as_investigation_events(self):
        self.assertGreater(census_v3_artifacts()["leaf_audit"]["metrics"]["event_taxonomy_counts"].get("ReportEvent", 0), 0)


if __name__ == "__main__":
    unittest.main()

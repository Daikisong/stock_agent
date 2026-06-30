import unittest

from census_v2_test_helpers import census_v2_artifacts


class CensusV2BaselineInputCollectorTests(unittest.TestCase):
    def test_collector_wires_existing_sources_instead_of_global_provider_pending(self):
        artifacts = census_v2_artifacts()
        summary = artifacts["baseline_summary"]
        self.assertGreater(summary["existing_ledger_accepted_claim_count"], 0)
        self.assertGreater(summary["source_task_count"], 0)
        self.assertGreater(summary["evidence_document_count"], 0)
        self.assertEqual(summary["provider_failed_symbol_count"], 0)
        self.assertIn("CompanyGuide", summary["source_family_counts"])
        self.assertIn("ReportRadar", summary["source_family_counts"])


if __name__ == "__main__":
    unittest.main()

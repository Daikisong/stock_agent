import unittest

from tests.census_v4_test_helpers import census_v4_artifacts, read_json


class CensusV4ResearchBrainBridgeHonestyTests(unittest.TestCase):
    def test_imported_research_brain_v4_report_does_not_create_brain_web_pass(self):
        artifacts = census_v4_artifacts()
        readiness = artifacts["readiness"]
        bridge = readiness["research_brain_bridge"]

        self.assertIn("RESEARCH_BRAIN_V4_REPORT_BRIDGE_IMPORTED", readiness["labels"])
        self.assertFalse(readiness["brain_web_evidence_pass"])
        self.assertFalse(bridge["usable_for_census_cutover"])
        self.assertGreater(bridge["accepted_claim_count"], 0)
        self.assertGreater(bridge["snapshot_url_count"], 0)
        self.assertIn("shadow/import-only", " ".join(readiness["remaining_operational_gaps"]))

    def test_bridge_audit_records_shadow_blockers_without_failing_anti_fake_pass(self):
        artifacts = census_v4_artifacts()
        bridge = read_json(artifacts["output_root"] / "research_brain_v4_bridge_audit.json")
        leaf_audit = artifacts["leaf_audit"]

        self.assertEqual(bridge["verdict"], "SHADOW_OR_IMPORT_ONLY")
        self.assertFalse(bridge["usable_for_census_cutover"])
        self.assertGreater(bridge["snapshot_url_count"], 0)
        self.assertIn("Research Brain v4 report is not production_cutover_ready", bridge["blockers"])
        self.assertEqual(leaf_audit["critical_counts"]["research_brain_bridge_cutover_overclaim_count"], 0)
        self.assertEqual(leaf_audit["metrics"]["research_brain_bridge_verdict"], "SHADOW_OR_IMPORT_ONLY")


if __name__ == "__main__":
    unittest.main()

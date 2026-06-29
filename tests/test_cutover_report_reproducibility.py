import unittest

from e2r.cli.audit_operational_report_reproducibility import audit_report_reproducibility
from e2r.production.cutover_shadow import ProductionCutoverConfig, build_production_cutover_bundle


class CutoverReportReproducibilityTests(unittest.TestCase):
    def test_metadata_contains_required_hashes(self):
        bundle = build_production_cutover_bundle(
            config=ProductionCutoverConfig(as_of_date="2026-06-30"),
            repo_root=".",
            command="unit-test",
        )
        audit = audit_report_reproducibility(bundle["shadow_latest"], repo_root=".")
        summary = audit["summary"]
        self.assertEqual(summary["missing_command_count"], 0)
        self.assertEqual(summary["missing_config_hash_count"], 0)
        self.assertEqual(summary["missing_planner_hash_count"], 0)


if __name__ == "__main__":
    unittest.main()

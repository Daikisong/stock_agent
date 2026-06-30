import unittest

from e2r.production.cutover_v3 import ProductionCutoverV3Config, _multiday_validation_v3
from tests.cutover_v3_test_helpers import fake_provider_matrix, fake_v3_base, fake_v3_frozen_base


class CutoverV3ProviderFailurePendingInMultidayTests(unittest.TestCase):
    def test_provider_failures_are_recorded_as_nonfinal_pending_context(self):
        base = dict(fake_v3_base())
        base["source_connector_report"] = {"summary": {"provider_failure_count": 2}, "rows": []}
        report = _multiday_validation_v3(
            base_bundles=[base for _ in range(5)],
            frozen_bundles=[fake_v3_frozen_base(f"2026-06-{day:02d}") for day in range(15, 25)]
            + [fake_v3_frozen_base(f"2026-06-{day:02d}", run_index=run_index) for day in range(15, 18) for run_index in (2, 3)],
            provider_matrix=fake_provider_matrix(),
            config=ProductionCutoverV3Config(as_of_date="2026-06-30"),
        )
        self.assertGreater(report["summary"]["source_provider_failure_total"], 0)
        self.assertTrue(all(row["provider_pending_or_nonfinal"] for row in report["rows"]))


if __name__ == "__main__":
    unittest.main()

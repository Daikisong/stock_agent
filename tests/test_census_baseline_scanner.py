import unittest

from e2r.census.baseline_scanner import BaselineScanInputs, BaselineScanner
from tests.census_test_helpers import instrument


class CensusBaselineScannerTests(unittest.TestCase):
    def test_baseline_scan_is_traceable_not_score(self):
        inst = instrument()
        scanner = BaselineScanner(
            BaselineScanInputs(
                price_anomaly_symbols={inst.symbol: 1},
                recent_official_events={inst.symbol: {"disclosures": 1, "supply_contracts": 1}},
            )
        )
        scan = scanner.scan(inst, as_of_date="2026-07-01")
        self.assertEqual(scan.scan_status, "SCANNED")
        self.assertIn("market_anomaly_investigation_only", scan.reason_codes)
        self.assertGreater(scan.trigger_priority_score, 0)


if __name__ == "__main__":
    unittest.main()

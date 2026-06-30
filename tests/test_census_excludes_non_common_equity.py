import csv
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from e2r.census.universe import build_universe


class CensusExcludesNonCommonEquityTests(unittest.TestCase):
    def test_excludes_preferred_spac_reit_etf_etn(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "u.csv"
            rows = [
                ("000001", "보통주", "COMMON"),
                ("000002", "테스트스팩", "SPAC"),
                ("000003", "테스트리츠", "REIT"),
                ("000004", "테스트ETF", "ETF"),
                ("000005", "테스트ETN", "ETN"),
                ("000006", "테스트우", "COMMON"),
            ]
            with path.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=["symbol", "company_name", "market", "instrument_type"])
                writer.writeheader()
                for symbol, name, typ in rows:
                    writer.writerow({"symbol": symbol, "company_name": name, "market": "KOSPI", "instrument_type": typ})
            result = build_universe(as_of_date="2026-07-01", universe_file=path)
            self.assertEqual(result.coverage["eligible_common_stock_count"], 1)
            self.assertEqual(result.coverage["excluded_spac_count"], 1)
            self.assertEqual(result.coverage["excluded_reit_count"], 1)
            self.assertEqual(result.coverage["excluded_etf_count"], 1)
            self.assertEqual(result.coverage["excluded_etn_count"], 1)
            self.assertEqual(result.coverage["excluded_preferred_count"], 1)


if __name__ == "__main__":
    unittest.main()

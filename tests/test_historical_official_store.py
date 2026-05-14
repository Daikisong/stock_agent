from datetime import date
from pathlib import Path
import tempfile
import unittest

from e2r.backtest.historical_official_store import HistoricalOfficialStore
from e2r.models import Market


class HistoricalOfficialStoreTests(unittest.TestCase):
    def test_universe_comes_from_official_history(self):
        with tempfile.TemporaryDirectory() as root:
            _write_minimal_official(root, include_disclosure=False)
            store = HistoricalOfficialStore(root)

            universe = store.load_universe(date(2023, 8, 1), Market.KR)

        self.assertEqual([item.symbol for item in universe], ["111111"])
        self.assertEqual(universe[0].name, "공식테스트")

    def test_as_of_filters_price_and_disclosure(self):
        with tempfile.TemporaryDirectory() as root:
            _write_minimal_official(root, include_disclosure=True)
            store = HistoricalOfficialStore(root)

            early_bars = store.load_price_bars("111111", date(2023, 1, 1), date(2023, 7, 1), date(2023, 7, 1))
            late_bars = store.load_price_bars("111111", date(2023, 1, 1), date(2023, 8, 1), date(2023, 8, 1))
            disclosures = store.load_disclosures("111111", date(2023, 7, 1), date(2023, 8, 1), date(2023, 8, 1))

        self.assertEqual(len(early_bars), 1)
        self.assertEqual(len(late_bars), 2)
        self.assertEqual(len(disclosures), 1)


def _write_minimal_official(root: str, *, include_disclosure: bool) -> None:
    root_path = Path(root)
    for name in ("universe", "prices", "disclosures", "financials", "risks"):
        (root_path / name).mkdir(parents=True, exist_ok=True)
    (root_path / "universe" / "universe.csv").write_text(
        "symbol,name,market,exchange,listed_date\n111111,공식테스트,KR,KRX,2020-01-01\n",
        encoding="utf-8",
    )
    (root_path / "prices" / "prices.csv").write_text(
        "symbol,date,open,high,low,close,adj_close,volume,trading_value,market_cap,source,as_of_date\n"
        "111111,2023-06-01,1000,1000,1000,1000,1000,100,100000,100000000,historical,2023-06-01\n"
        "111111,2023-07-27,1300,1400,1200,1350,1350,1000,1350000,135000000,historical,2023-07-27\n",
        encoding="utf-8",
    )
    disclosure_rows = (
        "symbol,source,report_type,title,published_at,observed_at,available_at,as_of_date,rcept_no,raw_text\n"
    )
    if include_disclosure:
        disclosure_rows += (
            '111111,OpenDART,단일판매·공급계약체결,단일판매·공급계약체결,2023-07-27T08:00:00,'
            '2023-07-27T08:00:00,2023-07-27T08:00:00,2023-07-27,r1,'
            '"계약금액 100억원 매출액 대비 20% 계약기간 2023-07-27 ~ 2026-07-26"\n'
        )
    (root_path / "disclosures" / "disclosures.csv").write_text(disclosure_rows, encoding="utf-8")
    (root_path / "financials" / "financials.csv").write_text(
        "symbol,fiscal_year,fiscal_quarter,period_end,reported_at,as_of_date,source\n",
        encoding="utf-8",
    )
    (root_path / "risks" / "risks.csv").write_text(
        "symbol,as_of_date,source,managed_issue,trading_halt,investment_warning,investor_caution,unfaithful_disclosure,delisting_risk,raw_text\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    unittest.main()

from datetime import date, datetime
import unittest

from e2r.connectors import EmptyDataConnector, FallbackDataConnector, MockDataConnector
from e2r.fixtures import FIXTURE_CASES
from e2r.models import (
    DisclosureEvent,
    FinancialActual,
    Instrument,
    Market,
    PriceBar,
    ResearchReport,
)


def make_bar(symbol, bar_date, close, as_of_date=None):
    return PriceBar(
        symbol=symbol,
        date=bar_date,
        open=close,
        high=close + 1,
        low=close - 1,
        close=close,
        adj_close=close,
        volume=1000,
        trading_value=close * 1000,
        market_cap=1000000000.0,
        source="test",
        as_of_date=as_of_date or bar_date,
    )


class MockDataConnectorTests(unittest.TestCase):
    def test_fixture_connector_exposes_required_domains(self):
        connector = MockDataConnector.from_fixture_cases()
        sample = FIXTURE_CASES[0]
        symbol = sample.scoring_payload.symbol

        instruments = connector.list_instruments(sample.market, sample.stage3_date)
        prices = connector.get_price_bars(symbol, date(2024, 1, 1), date(2024, 1, 20), sample.stage3_date)
        consensus = connector.get_consensus(symbol, sample.stage3_date)
        reports = connector.get_research_reports(symbol, date(2024, 1, 1), date(2024, 1, 20), sample.stage3_date)
        news = connector.get_news(symbol, date(2024, 1, 1), date(2024, 1, 20), sample.stage3_date)

        self.assertTrue(any(instrument.symbol == symbol for instrument in instruments))
        self.assertTrue(prices)
        self.assertTrue(consensus)
        self.assertTrue(reports)
        self.assertTrue(news)

    def test_price_bars_are_filtered_by_as_of_date(self):
        connector = MockDataConnector(
            price_bars=(
                make_bar("CASE", date(2024, 1, 2), 100, as_of_date=date(2024, 1, 2)),
                make_bar("CASE", date(2024, 1, 3), 101, as_of_date=date(2024, 1, 5)),
            )
        )

        bars = connector.get_price_bars("CASE", date(2024, 1, 1), date(2024, 1, 5), date(2024, 1, 4))

        self.assertEqual([bar.date for bar in bars], [date(2024, 1, 2)])

    def test_documents_are_filtered_by_range_and_availability(self):
        connector = MockDataConnector(
            disclosures=(
                DisclosureEvent(
                    symbol="CASE",
                    source="mock",
                    report_type="contract",
                    title="available",
                    published_at=datetime(2024, 1, 2, 8, 0),
                    observed_at=datetime(2024, 1, 2, 8, 1),
                    available_at=datetime(2024, 1, 2, 8, 2),
                    as_of_date=date(2024, 1, 2),
                ),
                DisclosureEvent(
                    symbol="CASE",
                    source="mock",
                    report_type="contract",
                    title="future",
                    published_at=datetime(2024, 1, 4, 8, 0),
                    observed_at=datetime(2024, 1, 4, 8, 1),
                    available_at=datetime(2024, 1, 4, 8, 2),
                    as_of_date=date(2024, 1, 4),
                ),
            ),
            research_reports=(
                ResearchReport(
                    symbol="CASE",
                    publish_date=date(2024, 1, 3),
                    broker="mock",
                    title="report",
                    as_of_date=date(2024, 1, 3),
                ),
            ),
        )

        disclosures = connector.get_disclosures("CASE", date(2024, 1, 1), date(2024, 1, 5), date(2024, 1, 3))
        reports = connector.get_research_reports("CASE", date(2024, 1, 1), date(2024, 1, 5), date(2024, 1, 3))

        self.assertEqual([item.title for item in disclosures], ["available"])
        self.assertEqual([item.title for item in reports], ["report"])

    def test_financials_are_filtered_by_reported_date(self):
        connector = MockDataConnector(
            financial_actuals=(
                FinancialActual(
                    symbol="CASE",
                    fiscal_year=2024,
                    fiscal_quarter=1,
                    period_end=date(2024, 3, 31),
                    reported_at=datetime(2024, 4, 30, 8, 0),
                    as_of_date=date(2024, 4, 30),
                    source="mock",
                    sales=100,
                ),
                FinancialActual(
                    symbol="CASE",
                    fiscal_year=2024,
                    fiscal_quarter=2,
                    period_end=date(2024, 6, 30),
                    reported_at=datetime(2024, 8, 14, 8, 0),
                    as_of_date=date(2024, 8, 14),
                    source="mock",
                    sales=150,
                ),
            )
        )

        actuals = connector.get_financial_actuals("CASE", date(2024, 5, 1))

        self.assertEqual(len(actuals), 1)
        self.assertEqual(actuals[0].sales, 100)

    def test_date_range_validation(self):
        connector = MockDataConnector()

        with self.assertRaisesRegex(ValueError, "start cannot be after end"):
            connector.get_price_bars("CASE", date(2024, 1, 5), date(2024, 1, 1), date(2024, 1, 5))


class FallbackDataConnectorTests(unittest.TestCase):
    def test_fallback_is_used_when_primary_has_no_data(self):
        fallback = MockDataConnector(
            instruments=(
                Instrument(
                    symbol="CASE",
                    name="Fallback Case",
                    market=Market.KR,
                    exchange="KRX",
                    listed_date=date(2024, 1, 1),
                ),
            )
        )
        connector = FallbackDataConnector(primary=EmptyDataConnector(), fallback=fallback)

        instruments = connector.list_instruments(Market.KR, date(2024, 1, 2))

        self.assertEqual([instrument.symbol for instrument in instruments], ["CASE"])

    def test_primary_result_is_preferred_over_fallback(self):
        primary = MockDataConnector(price_bars=(make_bar("CASE", date(2024, 1, 2), 100),))
        fallback = MockDataConnector(price_bars=(make_bar("CASE", date(2024, 1, 2), 200),))
        connector = FallbackDataConnector(primary=primary, fallback=fallback)

        bars = connector.get_price_bars("CASE", date(2024, 1, 1), date(2024, 1, 3), date(2024, 1, 3))

        self.assertEqual([bar.close for bar in bars], [100])


if __name__ == "__main__":
    unittest.main()


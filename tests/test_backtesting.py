from datetime import date
import unittest

from e2r.backtesting import BacktestEngine, Stage3BacktestInput, evaluate_stage3_backtest
from e2r.models import PriceBar, Stage, StageSnapshot


def make_bar(day, low, high, close, as_of_date=None):
    bar_date = date(2024, 1, day)
    return PriceBar(
        symbol="CASE",
        date=bar_date,
        open=close,
        high=high,
        low=low,
        close=close,
        adj_close=close,
        volume=1000,
        trading_value=close * 1000,
        market_cap=1000000000.0,
        source="mock",
        as_of_date=as_of_date or bar_date,
    )


def sample_bars():
    return (
        make_bar(1, 70, 75, 72),
        make_bar(2, 60, 70, 66),
        make_bar(3, 50, 65, 60),
        make_bar(4, 55, 68, 64),
        make_bar(5, 80, 95, 90),
        make_bar(6, 95, 110, 100),
        make_bar(7, 90, 120, 95),
        make_bar(8, 105, 151, 150),
        make_bar(9, 130, 160, 160),
        make_bar(10, 140, 180, 170),
        make_bar(11, 110, 130, 120),
        make_bar(12, 115, 125, 118),
    )


class BacktestEngineTests(unittest.TestCase):
    def test_stage3_path_metrics_are_computed(self):
        stages = (
            StageSnapshot(symbol="CASE", as_of_date=date(2024, 1, 9), stage=Stage.STAGE_4B),
            StageSnapshot(symbol="CASE", as_of_date=date(2024, 1, 11), stage=Stage.STAGE_4C),
        )

        result = BacktestEngine().evaluate_stage3(
            Stage3BacktestInput(
                symbol="CASE",
                stage3_date=date(2024, 1, 6),
                price_bars=sample_bars(),
                stage_snapshots=stages,
                stage3_price=100.0,
            )
        )

        self.assertEqual(result.stage3_price, 100.0)
        self.assertEqual(result.pre_runup_252d, 1.0)
        self.assertEqual(result.pre_runup_3y, 1.0)
        self.assertEqual(result.mfe_30d, 0.8)
        self.assertEqual(result.mae_30d, -0.1)
        self.assertTrue(result.below_entry_flag)
        self.assertEqual(result.time_to_50pct, 2)
        self.assertIsNone(result.time_to_100pct)
        self.assertIsNone(result.time_to_200pct)
        self.assertEqual(result.time_to_4b, 3)
        self.assertEqual(result.time_to_4c, 5)
        self.assertEqual(result.stage4b_price, 160)
        self.assertEqual(result.stage4b_return_from_stage3, 0.6)
        self.assertEqual(result.stage4c_price, 120)
        self.assertEqual(result.peak_date, date(2024, 1, 10))
        self.assertEqual(result.peak_price, 180)
        self.assertEqual(result.peak_return_from_stage3, 0.8)
        self.assertEqual(result.drawdown_after_peak, -0.388889)

    def test_stage3_price_defaults_to_stage_date_close(self):
        result = evaluate_stage3_backtest(
            symbol="CASE",
            stage3_date=date(2024, 1, 6),
            price_bars=sample_bars(),
        )

        self.assertEqual(result.stage3_price, 100)

    def test_pre_event_price_bars_must_be_available_as_of_stage3_date(self):
        bars = list(sample_bars())
        bars[4] = make_bar(5, 80, 95, 90, as_of_date=date(2024, 1, 7))

        with self.assertRaisesRegex(ValueError, "pre-event price bars must be available"):
            BacktestEngine().evaluate_stage3(
                Stage3BacktestInput(
                    symbol="CASE",
                    stage3_date=date(2024, 1, 6),
                    price_bars=tuple(bars),
                    stage3_price=100.0,
                )
            )

    def test_stage3_date_must_exist_in_price_bars(self):
        with self.assertRaisesRegex(ValueError, "stage3_date must exist"):
            BacktestEngine().evaluate_stage3(
                Stage3BacktestInput(
                    symbol="CASE",
                    stage3_date=date(2024, 1, 13),
                    price_bars=sample_bars(),
                    stage3_price=100.0,
                )
            )

    def test_duplicate_price_dates_are_rejected(self):
        bars = sample_bars() + (make_bar(6, 95, 110, 100),)

        with self.assertRaisesRegex(ValueError, "duplicate price bar date"):
            BacktestEngine().evaluate_stage3(
                Stage3BacktestInput(
                    symbol="CASE",
                    stage3_date=date(2024, 1, 6),
                    price_bars=bars,
                    stage3_price=100.0,
                )
            )


if __name__ == "__main__":
    unittest.main()


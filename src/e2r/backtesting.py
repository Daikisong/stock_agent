"""Point-in-time backtesting metrics for Stage 3 events."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Sequence

from .models import BacktestResult, PriceBar, Stage, StageSnapshot


TRADING_DAYS_1Y = 252
TRADING_DAYS_2Y = 504
TRADING_DAYS_3Y = 756


def _require_date(value: date, field_name: str) -> None:
    if type(value) is not date:
        raise ValueError(f"{field_name} must be a date")


def _require_text(value: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")


def _require_positive(value: float, field_name: str) -> None:
    if value <= 0:
        raise ValueError(f"{field_name} must be positive")


def _return(numerator: float, denominator: float) -> float:
    return round((numerator / denominator) - 1.0, 6)


@dataclass(frozen=True)
class Stage3BacktestInput:
    """Inputs for one Stage 3 backtest event.

    `stage3_price` should be the point-in-time recognition price. If omitted,
    the engine uses the Stage 3 date close, but only when that bar was available
    as of the Stage 3 date.
    """

    symbol: str
    stage3_date: date
    price_bars: Sequence[PriceBar]
    stage_snapshots: Sequence[StageSnapshot] = field(default_factory=tuple)
    stage3_price: float | None = None

    def __post_init__(self) -> None:
        _require_text(self.symbol, "symbol")
        _require_date(self.stage3_date, "stage3_date")
        if self.stage3_price is not None:
            _require_positive(self.stage3_price, "stage3_price")
        object.__setattr__(self, "price_bars", tuple(self.price_bars))
        object.__setattr__(self, "stage_snapshots", tuple(self.stage_snapshots))


class BacktestEngine:
    """Computes required E2R 2.0 Stage 3 path metrics."""

    def evaluate_stage3(self, inputs: Stage3BacktestInput) -> BacktestResult:
        bars = self._prepare_bars(inputs.symbol, inputs.price_bars)
        stage_index = self._stage_index(bars, inputs.stage3_date)
        self._validate_pre_event_point_in_time(bars[: stage_index + 1], inputs.stage3_date)

        stage3_price = inputs.stage3_price
        if stage3_price is None:
            stage3_price = bars[stage_index].close
        _require_positive(stage3_price, "stage3_price")

        pre_runup_252d = self._pre_runup(bars, stage_index, stage3_price, TRADING_DAYS_1Y)
        pre_runup_3y = self._pre_runup(bars, stage_index, stage3_price, TRADING_DAYS_3Y)

        stage4b_snapshot = self._first_stage_snapshot(inputs, Stage.STAGE_4B)
        stage4c_snapshot = self._first_stage_snapshot(inputs, Stage.STAGE_4C)
        stage4b_bar = self._bar_on_or_after(bars, stage4b_snapshot.as_of_date) if stage4b_snapshot else None
        stage4c_bar = self._bar_on_or_after(bars, stage4c_snapshot.as_of_date) if stage4c_snapshot else None

        peak_bar_index = self._peak_bar_index(bars, stage_index)
        peak_bar = bars[peak_bar_index]
        post_peak_low = min(bar.low for bar in bars[peak_bar_index:])

        return BacktestResult(
            symbol=inputs.symbol,
            stage3_date=inputs.stage3_date,
            stage3_price=stage3_price,
            pre_runup_252d=pre_runup_252d,
            pre_runup_3y=pre_runup_3y,
            mfe_30d=self._mfe(bars, stage_index, stage3_price, 30),
            mfe_90d=self._mfe(bars, stage_index, stage3_price, 90),
            mfe_180d=self._mfe(bars, stage_index, stage3_price, 180),
            mfe_1y=self._mfe(bars, stage_index, stage3_price, TRADING_DAYS_1Y),
            mfe_2y=self._mfe(bars, stage_index, stage3_price, TRADING_DAYS_2Y),
            mae_30d=self._mae(bars, stage_index, stage3_price, 30),
            mae_90d=self._mae(bars, stage_index, stage3_price, 90),
            mae_180d=self._mae(bars, stage_index, stage3_price, 180),
            mae_1y=self._mae(bars, stage_index, stage3_price, TRADING_DAYS_1Y),
            below_entry_flag=self._below_entry(bars, stage_index, stage3_price),
            time_to_50pct=self._time_to_return(bars, stage_index, stage3_price, 0.50),
            time_to_100pct=self._time_to_return(bars, stage_index, stage3_price, 1.00),
            time_to_200pct=self._time_to_return(bars, stage_index, stage3_price, 2.00),
            time_to_4b=self._time_to_bar(bars, stage_index, stage4b_bar),
            time_to_4c=self._time_to_bar(bars, stage_index, stage4c_bar),
            stage4b_date=stage4b_snapshot.as_of_date if stage4b_snapshot else None,
            stage4b_price=stage4b_bar.close if stage4b_bar else None,
            stage4b_return_from_stage3=_return(stage4b_bar.close, stage3_price) if stage4b_bar else None,
            stage4c_date=stage4c_snapshot.as_of_date if stage4c_snapshot else None,
            stage4c_price=stage4c_bar.close if stage4c_bar else None,
            peak_date=peak_bar.date,
            peak_price=peak_bar.high,
            peak_return_from_stage3=_return(peak_bar.high, stage3_price),
            drawdown_after_peak=_return(post_peak_low, peak_bar.high),
        )

    @staticmethod
    def _prepare_bars(symbol: str, price_bars: Sequence[PriceBar]) -> tuple[PriceBar, ...]:
        if not price_bars:
            raise ValueError("price_bars must not be empty")
        for bar in price_bars:
            if bar.symbol != symbol:
                raise ValueError("all price bars must match the input symbol")
        sorted_bars = tuple(sorted(price_bars, key=lambda bar: bar.date))
        seen_dates: set[date] = set()
        for bar in sorted_bars:
            if bar.date in seen_dates:
                raise ValueError(f"duplicate price bar date: {bar.date.isoformat()}")
            seen_dates.add(bar.date)
        return sorted_bars

    @staticmethod
    def _stage_index(bars: Sequence[PriceBar], stage3_date: date) -> int:
        for index, bar in enumerate(bars):
            if bar.date == stage3_date:
                return index
        raise ValueError("stage3_date must exist in price_bars")

    @staticmethod
    def _validate_pre_event_point_in_time(bars: Sequence[PriceBar], stage3_date: date) -> None:
        for bar in bars:
            if bar.as_of_date > stage3_date:
                raise ValueError("pre-event price bars must be available as of stage3_date")

    @staticmethod
    def _window(bars: Sequence[PriceBar], start_index: int, horizon: int) -> Sequence[PriceBar]:
        return bars[start_index : min(len(bars), start_index + horizon + 1)]

    @staticmethod
    def _pre_runup(
        bars: Sequence[PriceBar],
        stage_index: int,
        stage3_price: float,
        lookback: int,
    ) -> float | None:
        prior_bars = bars[max(0, stage_index - lookback) : stage_index]
        if not prior_bars:
            return None
        prior_low = min(bar.low for bar in prior_bars)
        return _return(stage3_price, prior_low)

    def _mfe(
        self,
        bars: Sequence[PriceBar],
        stage_index: int,
        stage3_price: float,
        horizon: int,
    ) -> float:
        window = self._window(bars, stage_index, horizon)
        return _return(max(bar.high for bar in window), stage3_price)

    def _mae(
        self,
        bars: Sequence[PriceBar],
        stage_index: int,
        stage3_price: float,
        horizon: int,
    ) -> float:
        window = self._window(bars, stage_index, horizon)
        return _return(min(bar.low for bar in window), stage3_price)

    @staticmethod
    def _below_entry(bars: Sequence[PriceBar], stage_index: int, stage3_price: float) -> bool:
        return any(bar.low < stage3_price or bar.close < stage3_price for bar in bars[stage_index + 1 :])

    @staticmethod
    def _time_to_return(
        bars: Sequence[PriceBar],
        stage_index: int,
        stage3_price: float,
        target_return: float,
    ) -> int | None:
        target_price = stage3_price * (1.0 + target_return)
        for index, bar in enumerate(bars[stage_index:], start=stage_index):
            if bar.high >= target_price:
                return index - stage_index
        return None

    @staticmethod
    def _peak_bar_index(bars: Sequence[PriceBar], stage_index: int) -> int:
        peak_index = stage_index
        peak_high = bars[stage_index].high
        for index, bar in enumerate(bars[stage_index:], start=stage_index):
            if bar.high > peak_high:
                peak_high = bar.high
                peak_index = index
        return peak_index

    @staticmethod
    def _first_stage_snapshot(inputs: Stage3BacktestInput, target_stage: Stage) -> StageSnapshot | None:
        candidates = [
            snapshot
            for snapshot in inputs.stage_snapshots
            if snapshot.symbol == inputs.symbol
            and snapshot.stage == target_stage
            and snapshot.as_of_date >= inputs.stage3_date
        ]
        if not candidates:
            return None
        return sorted(candidates, key=lambda snapshot: snapshot.as_of_date)[0]

    @staticmethod
    def _bar_on_or_after(bars: Sequence[PriceBar], target_date: date) -> PriceBar | None:
        for bar in bars:
            if bar.date >= target_date:
                return bar
        return None

    @staticmethod
    def _time_to_bar(bars: Sequence[PriceBar], stage_index: int, target_bar: PriceBar | None) -> int | None:
        if target_bar is None:
            return None
        for index, bar in enumerate(bars):
            if bar.date == target_bar.date:
                return index - stage_index
        return None


def evaluate_stage3_backtest(
    *,
    symbol: str,
    stage3_date: date,
    price_bars: Iterable[PriceBar],
    stage_snapshots: Iterable[StageSnapshot] = (),
    stage3_price: float | None = None,
) -> BacktestResult:
    """Convenience wrapper for one Stage 3 event."""

    return BacktestEngine().evaluate_stage3(
        Stage3BacktestInput(
            symbol=symbol,
            stage3_date=stage3_date,
            price_bars=tuple(price_bars),
            stage_snapshots=tuple(stage_snapshots),
            stage3_price=stage3_price,
        )
    )


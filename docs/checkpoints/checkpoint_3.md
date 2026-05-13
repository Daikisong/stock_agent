# Checkpoint 3 Report

## Files Changed

- `src/e2r/backtesting.py`
- `src/e2r/__init__.py`
- `tests/test_backtesting.py`
- `docs/checkpoints/checkpoint_3.md`

## What Was Implemented

- Added the point-in-time Stage 3 backtesting engine:
  - `Stage3BacktestInput`
  - `BacktestEngine`
  - `evaluate_stage3_backtest`
- Implemented required Stage 3 event metrics:
  - `stage3_date`
  - `stage3_price`
  - `pre_runup_252d`
  - `pre_runup_3y`
  - `mfe_30d`
  - `mfe_90d`
  - `mfe_180d`
  - `mfe_1y`
  - `mfe_2y`
  - `mae_30d`
  - `mae_90d`
  - `mae_180d`
  - `mae_1y`
  - `below_entry_flag`
  - `time_to_50pct`
  - `time_to_100pct`
  - `time_to_200pct`
  - `time_to_4b`
  - `time_to_4c`
  - `stage4b_date`
  - `stage4b_price`
  - `stage4b_return_from_stage3`
  - `stage4c_date`
  - `stage4c_price`
  - `peak_date`
  - `peak_price`
  - `peak_return_from_stage3`
  - `drawdown_after_peak`
- Added point-in-time safeguards:
  - Stage 3 date must exist in the price bars.
  - Pre-event price bars must be available as of the Stage 3 date.
  - Duplicate price dates are rejected.
  - Price bars must match the requested symbol.
- Added stage timeline support:
  - First Stage 4B snapshot after Stage 3 is used for `time_to_4b`.
  - First Stage 4C snapshot after Stage 3 is used for `time_to_4c`.
- Added a fallback rule for Stage 3 price:
  - If `stage3_price` is supplied, it is used as the recognition price.
  - If omitted, the Stage 3 date close is used only after pre-event availability validation.

## How It Was Verified

Commands run:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
python -m compileall -q src tests
```

Test result:

```text
Ran 27 tests in 0.003s
OK
```

New test coverage includes:

- pre-runup calculation from prior lows
- MFE and MAE calculation
- below-entry flag calculation
- time-to-50/100/200% calculation
- time-to-4B and time-to-4C calculation from stage snapshots
- Stage 4B and 4C price/return extraction
- peak and post-peak drawdown calculation
- default Stage 3 price from Stage 3 date close
- rejection of future-unavailable pre-event price bars
- rejection of missing Stage 3 price date
- rejection of duplicate price dates

## What Remains

- Checkpoint 4: add fixture cases for success, warning, failure, peak-out, and US boom/bust behavior.
- Checkpoint 5: add mock/fallback data connectors.
- Checkpoint 6: add Korean morning briefing generator.
- Checkpoint 7: add integration tests and final review.

## Assumptions Or Missing Data

- Stage 3 recognition itself is an input to the backtest engine. The engine does not decide whether Stage 3 should have happened; that remains the classifier's job.
- Future price bars are used only as outcome data after the Stage 3 event, not as historical classification input.
- `MFE_N` and `MAE_N` use the Stage 3 date through `N` trading sessions after Stage 3, bounded by available price bars.
- `time_to_4B` and `time_to_4C` are measured in trading-bar offsets from the Stage 3 bar.
- If a Stage 4B/4C snapshot date is not itself a trading day, the next available price bar is used for price and trading-day offset.
- No historical winner names are used in backtesting logic.
- No investment recommendation wording is produced.


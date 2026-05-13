# Checkpoint 1 Report

## Files Changed

- `pyproject.toml`
- `src/e2r/__init__.py`
- `src/e2r/models.py`
- `src/e2r/scoring.py`
- `tests/test_models.py`
- `tests/test_scoring.py`
- `docs/checkpoints/checkpoint_1.md`

## What Was Implemented

- Created the initial dependency-free Python package structure under `src/e2r`.
- Added core data models with validation:
  - `Instrument`
  - `PriceBar`
  - `FinancialActual`
  - `ConsensusSnapshot`
  - `ConsensusRevision`
  - `DisclosureEvent`
  - `ResearchReport`
  - `NewsItem`
  - `SectorRegime`
  - `Evidence`
  - `ScoreSnapshot`
  - `StageSnapshot`
  - `RedTeamFinding`
  - `BacktestResult`
- Added canonical enums:
  - `Market`
  - `SourceTier`
  - `Stage`
- Added point-in-time evidence validation:
  - `published_at`
  - `observed_at`
  - `available_at`
  - `as_of_date`
- Added the deterministic scoring interface:
  - `ScoreComponentSpec`
  - `ScoringPayload`
  - `Scorer` protocol
  - `DeterministicScorer`
- Implemented the canonical 100-point component shape from the spec:
  - `eps_fcf_explosion`, max 20
  - `earnings_visibility`, max 20
  - `bottleneck_pricing`, max 20
  - `market_mispricing`, max 15
  - `valuation_rerating`, max 15
  - `capital_allocation`, max 5
  - `information_confidence`, max 5
  - `risk_penalty`, subtractive
- Added `unittest` coverage for:
  - evidence point-in-time validation
  - rejection of evidence not yet available as of the decision date
  - price bar OHLC validation
  - canonical Stage 3 color enum support
  - missing score component rejection
  - component max score validation
  - deterministic total score output
  - score floor at zero

## How It Was Verified

Commands run:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
python -m compileall -q src tests
```

Test result:

```text
Ran 8 tests in 0.001s
OK
```

`compileall` completed without syntax errors.

## What Remains

- Checkpoint 2: implement the actual stage classifier and Red Team thesis-break rules.
- Checkpoint 3: implement the backtesting engine and required MFE/MAE, pre-runup, below-entry, and time-to metrics.
- Checkpoint 4: add fixture cases for success, warning, failure, peak-out, and US boom/bust behavior.
- Checkpoint 5: add mock/fallback connectors.
- Checkpoint 6: add the Korean morning briefing generator.
- Checkpoint 7: add integration tests and final review.

## Assumptions Or Missing Data

- `pytest` is not installed in the environment, so tests use the Python standard library `unittest`.
- No live market, filing, consensus, or news data source is assumed at this checkpoint.
- `StageSnapshot` stores canonical stages, but transition rules are intentionally left for Checkpoint 2.
- `BacktestResult` stores the required metric fields, but metric calculation is intentionally left for Checkpoint 3.
- Historical winners are not referenced by the scoring code. They remain future fixture candidates only.
- The scoring interface outputs monitoring scores only and does not produce buy/sell recommendations.


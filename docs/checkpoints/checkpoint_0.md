# Checkpoint 0 Report

## Files Changed

- `docs/e2r_2_0_spec.md`
- `docs/checkpoints/checkpoint_0.md`

## What Was Implemented

- Read and distilled `docs/레퍼런스1.md` through `docs/레퍼런스13.md`.
- Checked for a repo-local `AGENTS.md`; none exists under `/home/eorb915/projects/stock_agent`.
- Wrote the canonical E2R 2.0 specification.
- Fixed the official stage machine:
  - Stage 0
  - Stage 1
  - Stage 2
  - Stage 3-Green
  - Stage 3-Yellow
  - Stage 3-Red
  - Stage 4A
  - Stage 4B
  - Stage 4C
  - Stage 5
- Defined the deterministic 100-point scoring model:
  - EPS/FCF Explosion, 20
  - Earnings Visibility and Quality, 20
  - Bottleneck and Pricing Power, 20
  - Market Mispricing, 15
  - Valuation Rerating Runway, 15
  - Capital Allocation, 5
  - Information Confidence, 5
  - Risk Penalty
- Defined evidence tracking with `published_at`, `observed_at`, `available_at`, and `as_of_date`.
- Defined conceptual data models for instruments, prices, financials, consensus, disclosures, reports, news, scores, stages, Red Team findings, and backtest results.
- Defined Red Team thesis-break monitoring rules.
- Defined required backtest metrics:
  - MFE/MAE
  - pre-runup
  - time-to-50/100/200%
  - time-to-4B/4C
  - below-entry flag
  - 4B/4C price and drawdown fields
- Defined mock/fallback connector interface for future checkpoints.
- Defined Korean daily morning briefing requirements.
- Added explicit guardrails against:
  - hardcoding historical winners
  - future-data leakage
  - buy/sell recommendation wording

## How It Was Verified

- Confirmed reference files exist:

```text
docs/레퍼런스1.md
...
docs/레퍼런스13.md
```

- Confirmed total reference corpus size with `wc -l`:

```text
7782 total lines
```

- Extracted and reviewed headings and key sections covering:
  - scoring formulas
  - stage rules
  - Red Team rules
  - data source and database structure
  - morning briefing format
  - backtest metrics
  - 4B/4C rules
- No automated tests were added in Checkpoint 0 because this checkpoint only creates the canonical spec. Tests begin in Checkpoint 1 with data models and scoring interfaces.

## What Remains

- Checkpoint 1: create package structure, data models, scoring interfaces, and model tests.
- Checkpoint 2: implement stage classifier and Red Team rules.
- Checkpoint 3: implement point-in-time backtesting engine.
- Checkpoint 4: add fixture cases.
- Checkpoint 5: add mock/fallback connectors.
- Checkpoint 6: add Korean morning briefing generator.
- Checkpoint 7: add integration tests and final review.

## Assumptions Or Missing Data

- No repo-local `AGENTS.md` file exists in `/home/eorb915/projects/stock_agent`; only the session-provided instruction was available.
- The repository currently contains reference documents only, so Checkpoint 1 will need to create the initial Python project structure.
- Live vendor data access is not assumed. The implementation will use mock/fallback connectors first.
- Historical examples from the references are allowed as fixtures and expected-output cases, but not as scoring shortcuts.
- The system outputs monitoring classifications, not investment recommendations.


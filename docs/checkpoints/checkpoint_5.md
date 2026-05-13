# Checkpoint 5 Report

## Files Changed

- `src/e2r/connectors.py`
- `src/e2r/__init__.py`
- `tests/test_connectors.py`
- `docs/checkpoints/checkpoint_5.md`

## What Was Implemented

- Added the stable data connector protocol:
  - `list_instruments(market, as_of_date)`
  - `get_price_bars(symbol, start, end, as_of_date)`
  - `get_financial_actuals(symbol, as_of_date)`
  - `get_consensus(symbol, as_of_date)`
  - `get_consensus_revisions(symbol, as_of_date)`
  - `get_disclosures(symbol, start, end, as_of_date)`
  - `get_research_reports(symbol, start, end, as_of_date)`
  - `get_news(symbol, start, end, as_of_date)`
- Added `MockDataConnector`, an in-memory connector for pre-live operation.
- Added `MockDataConnector.from_fixture_cases()` so existing synthetic fixture cases can feed connector-backed tests and future briefings.
- Added `EmptyDataConnector` for explicit empty source behavior.
- Added `FallbackDataConnector`:
  - returns primary connector data when present
  - falls back only when primary returns no result
- Added point-in-time filtering:
  - price bars require `bar.as_of_date <= query as_of_date`
  - financials require `reported_at <= query as_of_date`
  - consensus requires `date <= as_of_date` and snapshot `as_of_date <= query as_of_date`
  - disclosures require `available_at <= query as_of_date`
  - research reports require report `as_of_date <= query as_of_date`
  - news requires `published_at <= query as_of_date`
- Added date range validation for range-based connector calls.

## How It Was Verified

Commands run:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
python -m compileall -q src tests
```

Test result:

```text
Ran 40 tests in 0.004s
OK
```

New test coverage includes:

- fixture connector exposes instruments, prices, consensus, reports, and news
- price bars are filtered by `as_of_date`
- disclosures and research reports are filtered by date range and availability
- financial actuals are filtered by reported date
- invalid date range is rejected
- fallback connector uses fallback when primary is empty
- fallback connector prefers primary when primary has data

## What Remains

- Checkpoint 6: add Korean morning briefing generator.
- Checkpoint 7: add integration tests and final review.

## Assumptions Or Missing Data

- No live KRX, OpenDART, SEC, FnGuide, QuantiWise, WiseReport, or news API integration is implemented yet.
- The connector protocol is intentionally shaped so live connectors can replace mock connectors later without changing downstream pipeline code.
- Mock connector data is deterministic and local.
- The fallback connector is domain-level fallback, not row-level merge. 예를 들어 primary가 가격 데이터를 하나라도 반환하면 그 호출에서는 fallback 가격 데이터를 섞지 않는다.
- No investment recommendation wording is produced.


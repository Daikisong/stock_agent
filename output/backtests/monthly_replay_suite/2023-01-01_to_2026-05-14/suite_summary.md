# Monthly Historical Replay Suite

- replay_period: 2023-01-01 to 2026-05-14
- modes_run: case_fixture, official_only, hybrid
- replay_dates: 126
- total_scanned_instruments_cases: 1008
- total_candidates: 702
- event_search_or_higher: 702
- deep_research: 418
- Stage 2 count: 32
- Stage 3-Green count: 202
- Stage 3-Yellow count: 46
- Stage 3-Red count: 84
- Stage 4B count: 0
- Stage 4C count: 0
- still_active count: 10
- missed known winners: 6
- false_positive_or_boom_bust cases: 6

## Evidence Coverage

- consensus: 418
- consensus_revision: 418
- disclosure: 627
- financial_actual: 702
- news: 70
- price: 762
- research_report: 418
- missing_report_news_snapshot_count: 632
- stage4b_unknown_count: 0

## Major Limitations

- Layer 1 recall is not Stage 3 conviction.
- case_fixture success is curated fixture replay, not proof of live discovery.
- official_only misses report-driven winners when old report/news snapshots are unavailable.
- 4B is not fabricated; unknown_insufficient_evidence is a valid result.
- Missing report/news snapshots limit historical discovery claims.

## Readiness

Monthly replay is structurally sane for a larger fixture backtest, but conclusions remain limited by missing historical report/news snapshots and sparse 4B evidence.

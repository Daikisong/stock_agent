# Historical Replay Runbook

## What This Is

Historical replay is the offline quality loop for E2R 2.0.

It is different from a live scan:

```text
live scan
-> today's APIs/searches
-> today's candidates

historical replay
-> old fixture evidence
-> point-in-time filtering
-> asks what the agent would have seen then
```

It does not create trading recommendations.

## Three Replay Types

### Layer-1 Recall

Layer-1 recall asks only:

```text
Would this historical case reach event_search or deep_research?
```

Example:

```text
일진전기 long-term contract fixture exists
-> Layer 1 should at least route it to event_search
```

It does not require immediate Stage 3-Green.

### Case Replay

Case replay runs one known fixture through:

```text
FeatureEngineering
-> StageClassifier
-> RedTeam
-> BacktestEngine
```

This is useful for known cases like HD현대일렉트릭, Zoom, 씨젠, and SMCI.

### Universe Replay

Universe replay runs by date:

```text
replay date
-> fixture universe visible as of that date
-> Layer-1 candidate routing
-> Stage snapshots
-> lifecycle metrics for Stage 2 / Stage 3 candidates
```

This is closer to the question:

```text
What would the agent have discovered on each historical date?
```

## Modes

### official_only

Uses official-style local evidence:

```text
price bars
OpenDART-like disclosures
financial actuals
```

It excludes:

```text
broker reports
news
consensus/revision fixtures
```

If a report is needed but not allowed in this mode, the output says so.

Example:

```text
evidence_missing:research_report_excluded_in_official_only
```

This means the replay is being honest, not that the company had no evidence in real life.

### case_fixture

Uses the full curated historical fixture:

```text
reports
news
disclosures
financial actuals
consensus-like rows
price path
```

This is best for deterministic pipeline regression testing.

### hybrid

Uses official evidence plus any available report/news fixtures.

Use this when some cases have report snapshots and others do not.

## Point-In-Time Rule

The replay filters every evidence item by `as_of_date` or `available_at`.

Example:

```text
Replay date: 2023-07-27
Report date: 2023-07-31
Result: report is not visible
```

Missing evidence is recorded instead of filled in.

## How To Run

Monthly replay first:

```bash
PYTHONPATH=src python -m e2r.cli.run_historical_replay \
  --start-date 2023-07-01 \
  --end-date 2024-12-31 \
  --frequency monthly \
  --mode case_fixture \
  --output-directory output/backtests/historical_replay
```

Official-only replay:

```bash
PYTHONPATH=src python -m e2r.cli.run_historical_replay \
  --start-date 2023-07-01 \
  --end-date 2024-12-31 \
  --frequency monthly \
  --mode official_only
```

Weekly replay after monthly looks reasonable:

```bash
PYTHONPATH=src python -m e2r.cli.run_historical_replay \
  --start-date 2023-07-01 \
  --end-date 2024-12-31 \
  --frequency weekly \
  --mode hybrid
```

Daily replay should be used after the reports look sane.

## Output Files

The runner writes:

```text
output/backtests/historical_replay/YYYY-MM-DD_summary.json
output/backtests/historical_replay/YYYY-MM-DD_summary.md
output/backtests/historical_replay/stage_lifecycle_results.csv
output/backtests/historical_replay/stage_lifecycle_results.json
output/backtests/historical_replay/top_stage3_candidates.md
output/backtests/historical_replay/false_positive_cases.md
output/backtests/historical_replay/missed_winner_cases.md
```

## How To Read Stage Results

Stage 2 means:

```text
candidate evidence exists, but rerating confirmation is not complete
```

Stage 3-Green means:

```text
strong deterministic score
meaningful revision evidence
contract/visibility quality
low Red Team risk
```

Stage 3-Yellow means:

```text
score is high, but Green confirmation is incomplete
```

Stage 3-Red means:

```text
there is a rerating-like event, but one-off risk, weak quality, valuation risk, or Red Team risk is high
```

## How To Read 4B/4C

4B is not guessed.

If evidence is missing, the lifecycle result says:

```text
stage4b_status = unknown_insufficient_evidence
```

Example:

```text
price doubled, but no revision slowdown or backlog slowdown fixture exists
-> do not fabricate 4B
-> mark unknown_insufficient_evidence
```

4C is only recorded when a fixture StageSnapshot or Red Team hard break exists.

## Why Missing Report Snapshots Matter

Manual research often depends on broker reports and news pages.

If the historical fixture lacks the old report text or search snapshot, the replay cannot prove the agent would have found it.

That is why the output distinguishes:

```text
detected
missed
detected_late
detected_but_yellow_red
skipped_missing_historical_report_news_data
```

## Scaling Order

Use this order:

```text
1. case_fixture monthly
2. official_only monthly
3. hybrid monthly
4. hybrid weekly
5. hybrid daily
```

Do not jump straight to daily replay if monthly output has obvious missing evidence or parser problems.

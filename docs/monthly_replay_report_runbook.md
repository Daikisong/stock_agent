# Monthly Replay Report Runbook

## Purpose

The monthly replay suite turns historical fixture replay into a report an operator can read without opening raw JSON.

It answers:

```text
Which cases reached event_search or deep_research?
Which cases reached Stage 2 or Stage 3?
What happened to price after Stage 3?
Which winners were missed?
Which warning cases were contained?
Where is evidence missing?
```

It does not generate buy/sell recommendations.

Important:

```text
The production flow is E2R_STANDARD.
official_only / case_fixture / hybrid are diagnostic replay modes.
case_fixture success is regression success, not proof of live discovery.
```

For serious blind discovery after Checkpoint 24, use:

```text
PYTHONPATH=src python -m e2r.cli.run_blind_discovery_replay ... --flow E2R_STANDARD --no-fixture-source-proxy
```

The monthly suite remains useful for mode comparison and fixture regression.
It should not be presented as proof that the agent found old winners without help.

## How To Run

Default suite:

```bash
PYTHONPATH=src python -m e2r.cli.run_monthly_replay_suite \
  --start-date 2023-01-01 \
  --end-date 2026-05-14 \
  --output-directory output/backtests/monthly_replay_suite
```

Run selected modes:

```bash
PYTHONPATH=src python -m e2r.cli.run_monthly_replay_suite \
  --start-date 2023-01-01 \
  --end-date 2026-05-14 \
  --modes case_fixture,hybrid \
  --skip-official-only
```

Small debugging run:

```bash
PYTHONPATH=src python -m e2r.cli.run_monthly_replay_suite \
  --start-date 2023-07-01 \
  --end-date 2023-12-31 \
  --universe-limit 5
```

## Output Folder

The output root is:

```text
output/backtests/monthly_replay_suite/YYYY-MM-DD_to_YYYY-MM-DD/
```

Main reports:

```text
suite_summary.md
mode_comparison.md
stage3_lifecycle_summary.md
known_case_validation.md
missed_winners.md
false_positives.md
stage4b_4c_review.md
evidence_coverage.md
next_backtest_readiness.md
top_stage3_candidate_cards.md
```

Machine-readable files:

```text
suite_summary.json
mode_comparison.json
stage3_lifecycle_results.csv
stage3_lifecycle_results.json
```

Each mode's original Checkpoint 21 output is preserved under:

```text
case_fixture/
official_only/
hybrid/
```

## How To Read The Modes

### case_fixture

Uses curated historical case fixtures:

```text
reports
news
disclosures
financial actuals
consensus-like rows
price paths
```

This is good for regression testing.
It is not proof that a live agent would have found the same report on the same date.

### official_only

Uses only official-style evidence:

```text
disclosures
financial actuals
price bars
```

If a winner was report-driven, official_only may miss it.

Example:

```text
official_only_excluded_report_news
```

This means:

```text
The report existed in the fixture,
but this mode was not allowed to use it.
```

### hybrid

Uses official evidence plus available report/news fixtures.

This is currently the best practical approximation for larger fixture replay when report snapshots exist.

## Reading suite_summary.md

Use this first.

Important lines:

```text
total_candidates
event_search_or_higher
deep_research
Stage 2 count
Stage 3-Green count
Stage 3-Yellow count
Stage 3-Red count
missed known winners
false-positive / boom-bust cases
```

Example interpretation:

```text
Stage 3-Green count is high
-> check whether this is repeated monthly detection of the same fixture
-> do not treat it as unique live discoveries
```

## Reading mode_comparison.md

This report compares:

```text
official_only vs case_fixture vs hybrid
```

If official_only is weak but hybrid is strong, the likely issue is:

```text
historical report/news snapshots matter
```

That is not automatically a scoring bug.

## Reading stage3_lifecycle_summary.md

This report answers what happened after Stage 3:

```text
MFE = maximum favorable excursion
MAE = maximum adverse excursion
below_entry_rate = how often price went below Stage 3 entry
time_to_50pct / 100pct / 200pct = days to reach those returns
```

Example:

```text
Stage 3-Green MFE high, MAE shallow
-> historical fixture outcomes are directionally consistent

Stage 3-Red MFE high but 4C later
-> boom-bust warning behavior needs review, not Green promotion
```

## Reading known_case_validation.md

This is the most important sanity table.

It shows:

```text
case_id
company_name
expected_group
expected_stage
actual_stage_by_mode
layer1_result_by_mode
status_by_mode
evidence_types_seen
missing_evidence_warnings
future_data_used
interpretation
```

Expected group examples:

```text
structural
one_off
boom_bust
valuation_overheat
```

One-off or boom-bust cases should not become Stage 3-Green.

## Reading missed_winners.md

This report gives the miss reason:

```text
source_missing
threshold_too_high
parser_failure
no_report_radar_path
no_price_signal
no_disclosure_signal
evidence_available_but_not_scored
not_in_universe
official_only_excluded_report_news
unknown
```

Example:

```text
official_only_excluded_report_news
-> acceptable limitation for official_only
-> add report/news snapshots or use hybrid
```

Do not lower thresholds just because this file has misses.
First check whether the evidence was available.

## Reading false_positives.md

This report checks whether warning cases were contained.

Examples:

```text
씨젠 -> one_off
SMCI -> boom_bust
대한전선-like -> valuation_overheat
```

Correct behavior:

```text
Stage 3-Yellow or Stage 3-Red is allowed.
Unsafe Stage 3-Green is not allowed.
```

## Reading stage4b_4c_review.md

This report asks whether 4B appeared before or near the peak.

Statuses:

```text
detected_before_peak
detected_near_peak
detected_after_peak
unknown_insufficient_evidence
```

If evidence is missing, the system records:

```text
unknown_insufficient_evidence
```

It does not invent a 4B date.

## Reading evidence_coverage.md

This report shows whether the replay has enough source coverage.

Important fields:

```text
research_report count
news count
disclosure count
financial_actual count
consensus_revision count
missing_report_news_snapshot_count
stage4b_unknown_count
```

If report/news coverage is weak, larger replay conclusions are limited.

## Reading next_backtest_readiness.md

This is the final operator decision file.

It answers:

```text
Is monthly replay sane enough for larger backtest?
Which mode should be used next?
Which evidence sources are weak?
What must be fixed before weekly/daily replay?
```

Recommended order:

```text
1. hybrid monthly
2. hybrid weekly
3. official_only monthly with more official historical rows
4. hybrid daily
```

## Interpretation Rules

Keep these rules:

```text
Layer 1 recall is not Stage 3 conviction.
Stage 3-Green requires strict evidence quality.
A candidate can be detected but still be Yellow/Red.
official_only missing report-driven winners is not automatically a failure.
case_fixture success is not proof of live discovery.
hybrid is the best practical approximation when report/news fixtures exist.
4B must not be fabricated.
unknown_insufficient_evidence is valid.
one-off demand must not become structural E2R.
missing evidence should be reported, not filled.
```

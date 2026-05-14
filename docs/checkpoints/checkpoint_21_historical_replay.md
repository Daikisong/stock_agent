# Checkpoint 21 Historical Universe Replay

## Purpose

This checkpoint adds the first broader historical replay layer.

It asks:

```text
historical fixture universe
-> point-in-time evidence filtering
-> Layer-1 candidate routing
-> deterministic score
-> Stage classification
-> Stage lifecycle price-path metrics
```

Simple example:

```text
2023-07-27 replay date
-> HD현대일렉트릭 report/disclosure available
-> candidate reaches deep_research
-> Stage 3-Green if deterministic evidence is strong
-> later price path is measured for MFE/MAE
```

If a 2023-07-31 report exists, it is not visible to a 2023-07-27 replay date.

## Added Modules

```text
src/e2r/backtest/historical_universe_replay.py
src/e2r/backtest/stage_lifecycle_backtest.py
src/e2r/cli/run_historical_replay.py
tests/test_historical_universe_replay.py
tests/test_stage_lifecycle_backtest.py
docs/historical_replay_runbook.md
```

The existing `historical_case_replay.py` remains the focused known-case replay runner.
The new universe replay is date-based and writes candidate, stage, missing-evidence, and lifecycle reports.

## Replay Modes

```text
official_only
case_fixture
hybrid
```

`official_only` uses only fixture official-style evidence such as disclosures and financial actuals.
It excludes reports, news, and consensus fixtures and records missing evidence explicitly.

Example:

```text
HD현대일렉트릭 has a broker report fixture
official_only excludes it
-> evidence_missing:research_report_excluded_in_official_only
```

`case_fixture` uses the full historical case fixture set.

`hybrid` allows official evidence plus available report/news fixtures.

## Stage Lifecycle Metrics

The stage lifecycle backtest computes:

```text
pre_runup_252d
pre_runup_3y
MFE/MAE over 30d, 90d, 180d, 1y, 2y
below_entry_flag
time_to_50pct / 100pct / 200pct
peak date/price/return
4B date/price/return when evidence exists
4C date/price when evidence exists
drawdown after peak
still active flag
```

If 4B evidence is unavailable, the result says:

```text
stage4b_status = unknown_insufficient_evidence
```

It does not invent a 4B date.

## Outputs

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

These output paths are intentionally under `output/`, which is gitignored.

## Known Case Validation

The report checks structural and warning fixtures separately.

Structural examples:

```text
HD현대일렉트릭
효성중공업
일진전기
산일전기
삼양식품
한화에어로스페이스
NVIDIA, when using US fixtures
```

Warning examples:

```text
Zoom
씨젠
SMCI
대한전선-like
```

One-off and boom-bust cases may reach event search or deep research, but they should not become Stage 3-Green.

## Tests

Added tests prove:

```text
case_fixture mode detects known structural winners
official_only mode marks missing report evidence
replay does not use report evidence after as_of_date
one-off cases do not become Stage 3-Green
stage lifecycle computes MFE/MAE
4B remains unknown when evidence is missing
SMCI-like 4B appears before 4C when fixture evidence exists
all output reports are written
```

## Limitations

This is still fixture replay, not proof that every historical winner would have been found live.

The important limitation is:

```text
No historical search snapshot
-> no claim that the agent could have found that exact report on that exact day
```

The report therefore separates `official_only`, `case_fixture`, and `hybrid`.

# Checkpoint 21 Historical Case Replay

## Purpose

Layer-1 recall asks whether a case reaches event search or deep research.

Historical full replay asks more:

```text
fixture case
-> FeatureEngineering
-> deterministic score
-> Red Team
-> StageClassifier
-> BacktestEngine
-> Layer-1 result + final Stage + MFE/MAE + 4B/4C timing
```

This is not live proof. It is a fixture replay that checks whether the deterministic pipeline still behaves correctly on known examples.

## Runner

Programmatic use:

```python
from datetime import date
from e2r.backtest.historical_case_replay import HistoricalCaseReplayRunner

summary = HistoricalCaseReplayRunner().run(as_of_date=date.today())
print(summary.output_json_path)
print(summary.output_md_path)
```

Outputs:

```text
output/backtests/historical_case_replay/YYYY-MM-DD_results.json
output/backtests/historical_case_replay/YYYY-MM-DD_summary.md
```

## Cases

Success / structural-like:

```text
HD현대일렉트릭
효성중공업
일진전기
산일전기
삼양식품
한화에어로스페이스
NVIDIA
```

Warning / failure-like:

```text
Zoom
씨젠
SMCI
대한전선-like
```

## Current Fixture Replay Result

Current fixture replay summary:

```text
total_cases: 11
passed_cases: 10
failed_cases: 1
stage_distribution:
  Stage 1: 3
  Stage 2: 2
  Stage 3-Green: 3
  Stage 3-Yellow: 1
  Stage 3-Red: 2
SMCI 4B before 4C: true
one_off_green_violations: none
```

The one known structural miss is:

```text
samyang_foods_2024 -> structural_case_below_stage2
```

Interpretation:

```text
The runner did not hide the miss.
The fixture likely needs stronger revision/visibility evidence if this case is expected to replay as Stage 2 or higher.
```

## Expected Behavior Checked

The replay verifies:

```text
structural winners reach Stage 2 or Stage 3 Green/Yellow when evidence supports it
one-off cases do not become Stage 3-Green
SMCI-like case has 4B before 4C
대한전선-like case does not become Green
MFE/MAE are computed when price path exists
Layer-1 result is recorded for every case
```

## How To Read Failures

A failure is not automatically a code bug.

Examples:

```text
structural_case_below_stage2
-> fixture evidence may be too weak
-> parser may not map a field
-> deterministic threshold may need review

one_off_case_became_green
-> precision bug
-> one-off shortage risk or Red Team rule likely failed
```

Full replay is useful before standard shadow because it checks that historical cases still produce reasonable stages without forcing Green.

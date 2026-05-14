# Checkpoint 20 Layer-1 Recall Results

## Purpose

Layer-1 recall asks a narrow question:

```text
Would the system route a known historical case to event_search or deep_research?
```

It does not ask:

```text
Should every structural winner immediately become Stage 3-Green?
```

Stage 3-Green remains a later precision gate.

## Fixture Cases

Structural or success-like cases:

```text
HD현대일렉트릭 2023
효성중공업 2023
일진전기 2023~2024
산일전기 2025
삼양식품 2024
한화에어로스페이스 2024
NVIDIA 2023
```

Warning or false-positive-like cases:

```text
Zoom 2020
씨젠 2020
SMCI 2024
대한전선-like 2026 red fixture
```

## Current Fixture Result

The fixture recall test produced:

```text
cases: 11
recall_top_50: 1.0
reached_event_search: 11
reached_deep_research: 11
failed_cases: 0
```

All fixture cases contain historical report evidence, so the current fixture route is usually `deep_research`.

Example:

```text
HD현대일렉트릭 report + disclosure + news + consensus revision
-> deep_research
-> deterministic scoring later classifies Stage 3-Green
```

Counter-example:

```text
Zoom 2020 report + news + financial actual
-> deep_research
-> one_off_shortage_risk remains high
-> Stage 3-Red, not Stage 3-Green
```

## Failure Reasons

If a structural fixture fails Layer 1, the result records a reason instead of silently passing:

```text
source_missing
threshold_too_high
parser_failure
no_report_radar_path
no_price_signal
no_disclosure_signal
evidence_available_but_not_scored
not_in_universe
unknown
```

Current test coverage includes a forced missing-evidence case and verifies the failure reason is `source_missing`.

## Interpretation

This backtest is not proof of future live recall. It proves the routing code can express the manual workflow on fixture data:

```text
evidence exists by as_of_date
-> Layer 1 catches it
-> web/report route is available
-> final Stage still depends on deterministic E2R evidence quality
```

Live recall should be checked again after a standard shadow run with Report Radar enabled and OpenDART detail fetches capped.

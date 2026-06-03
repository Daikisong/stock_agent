# E2R Extension Matrix Round 3

`docs/round/round_03.md` expands the case-library design beyond the first 25
core archetypes.

The important distinction is:

```text
core archetype
-> broad scoring bucket

extension archetype
-> more precise case-library bucket
```

Example:

```text
SEMI_EQUIPMENT_CAPEX
-> broad bucket

AI_DATA_CENTER_INFRASTRUCTURE
-> extension bucket for power/cooling/server/network bottlenecks
```

## What Changed

Round 3 adds a report-only matrix for:

- `GREEN_ELIGIBLE`
- `YELLOW_WATCH`
- `RED_4B_GUARDRAIL`

This does not change production scoring.

## Stage Posture Examples

`AI_DATA_CENTER_INFRASTRUCTURE` is `GREEN_ELIGIBLE` because confirmed orders,
customer CAPEX visibility, and capacity bottlenecks can create multi-year
EPS/FCF change.

`ROBOTICS_FACTORY_AUTOMATION` is `YELLOW_WATCH` because a robot theme or MOU is
not enough. It needs actual customer adoption, revenue conversion, and repeat
service or software revenue.

`CONSTRUCTION_REAL_ESTATE_CREDIT` is `RED_4B_GUARDRAIL` because PF, liquidity,
unsold inventory, and credit risk can dominate headline orders.

## Required Case Record Fields

Round 3 also makes future case records more concrete:

```text
stage1_evidence
stage2_evidence
stage3_evidence
stage4b_evidence
stage4c_evidence
price_pattern
must_have_fields
red_flag_fields
score_weight_hint
```

This matters because narrative notes are not enough for later backtests.

Example:

```text
Robot company
-> Stage 1: Samsung investment headline
-> Stage 2: real customer adoption and revenue conversion
-> Green: still restricted until repeat revenue and OPM are visible
```

## Guardrails

- Do not apply these as StageClassifier thresholds.
- Do not use case records as candidate-generation input.
- Do not create stock-name rules.
- Do not loosen Stage 3-Green for recall.
- Keep construction/PF, one-off, theme overheat, and pre-revenue biotech
  Green-restricted.

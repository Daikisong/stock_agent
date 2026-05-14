# E2R Case Record Schema v0.2

The v0.2 case record pack is calibration/evaluation material. It must not be
used as production candidate-generation input.

## Purpose

The schema records two separate questions:

```text
1. Evidence quality: was there real E2R evidence?
2. Price alignment: did price behave like a rerating after that evidence?
```

Example:

```text
삼양식품
-> evidence: export channel, recurring demand, OPM, EPS
-> price_validation: stage price and MFE/MAE if historical price exists

진단키트 one-off
-> evidence: pandemic demand, OPM spike
-> red flags: one-off demand, demand cliff
-> rerating_result: no_rerating, not true structural rerating
```

## Required Identity Fields

- `case_id`
- `symbol`
- `company_name`
- `market`
- `large_sector`
- `sector_raw`
- `primary_archetype`
- `secondary_archetypes`

## Classification Fields

- `case_type`
- `expected_group`
- `score_price_alignment`
- `rerating_result`
- `stage_failure_type`
- `price_pattern`

Allowed `case_type` values:

- `structural_success`
- `success_candidate`
- `cyclical_success`
- `one_off`
- `overheat`
- `failed_rerating`
- `event_premium`
- `4b_watch`
- `4c_thesis_break`

Allowed `score_price_alignment` values:

- `unknown`
- `aligned`
- `false_positive_score`
- `missed_due_to_score`
- `price_moved_without_evidence`
- `evidence_good_but_price_failed`

Allowed `rerating_result` values:

- `unknown`
- `true_rerating`
- `cyclical_rerating`
- `event_premium`
- `theme_overheat`
- `no_rerating`
- `thesis_break`
- `credit_relief_rally`
- `policy_event_rerating`

Allowed `stage_failure_type` values:

- `unknown`
- `green_success`
- `yellow_success`
- `stage2_watch_success`
- `false_green`
- `false_yellow`
- `should_have_been_red`
- `missed_structural`

Example:

```text
robotics theme case
-> strategic investment headline appears
-> no revenue conversion
-> price spikes and then fades
-> stage_failure_type = should_have_been_red
```

## Lifecycle Fields

- `stage1_date`
- `stage2_date`
- `stage3_date`
- `stage4a_date`
- `stage4b_date`
- `stage4c_date`
- `peak_date`

Unknown dates stay null. They are not inferred from the case label.

## Evidence Fields

- `stage1_evidence`
- `stage2_evidence`
- `stage3_evidence`
- `stage4b_evidence`
- `stage4c_evidence`
- `must_have_fields`
- `red_flag_fields`
- `key_evidence_fields`
- `green_guardrails`

These are field names and evidence themes, not proof by themselves. Production
scoring still requires real Evidence objects from the E2R flow.

## Price Validation

`price_validation` contains:

- `stage1_price`
- `stage2_price`
- `stage3_price`
- `stage4b_price`
- `stage4c_price`
- `peak_price`
- `peak_return_from_stage3`
- `mfe_30d`
- `mfe_90d`
- `mfe_180d`
- `mfe_1y`
- `mfe_2y`
- `mae_30d`
- `mae_90d`
- `mae_180d`
- `mae_1y`
- `mae_2y`
- `drawdown_after_peak`
- `below_stage3_price_flag`
- `time_to_50pct`
- `time_to_100pct`
- `time_to_200pct`
- `price_validation_status`

If local price data is missing:

```text
price_validation_status = missing_price_data
prices = null
```

No price is invented.

## Guardrails

- Do not import case-library modules from production scoring.
- Do not use case labels as input evidence.
- Do not apply `score_weight_hint` to live scoring yet.
- Do not lower Stage 3-Green thresholds based on this pack alone.
- Treat `event_premium`, `one_off`, `overheat`, and `4c_thesis_break` as guardrail cases.

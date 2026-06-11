# E2R v12 Stock-Web Residual Research — R7 / C23 Bio Regulatory Approval Commercialization

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R7
selected_loop: 102
round_schedule_status: coverage_index_selected
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_VS_BINARY_CRL_FALSE_POSITIVE
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_accessed: false
```

## 1. Objective

This run fills the remaining Priority 0 gap for `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`.

C23 is not a simple "FDA headline is bullish" bucket. It is a bridge archetype:

```text
confirmed regulatory decision
→ partner / channel / reimbursement / launch timing
→ commercialization visibility
→ revenue, royalty, or margin conversion
```

The residual question is where the current calibrated profile still confuses:

```text
approval expectation or trial-data hype
```

with:

```text
confirmed approval + commercialization route
```

## 2. Coverage and no-repeat logic

The No-Repeat Index marks C23 as a Priority 0 bucket with 29 rows and 1 row needed to reach the 30-row minimum stability threshold. This run adds three independent symbol paths.

Hard duplicate avoidance key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected symbols:

| symbol | name | role |
|---|---|---|
| 000100 | 유한양행 | positive confirmed approval + global partner commercialization bridge |
| 145020 | 휴젤 | moderate positive FDA approval + US commercial entry bridge with high MAE |
| 028300 | HLB | counterexample: approval-expectation rally → CRL / hard 4C |

## 3. Price source validation

`Songdaiki/stock-web` manifest:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
research_pack_default_price_basis = tradable_raw
max_date = 2026-02-20
```

Symbol profile checks:

```text
000100: 유한양행 / KOSPI / active-like / 2024 shard available
145020: 휴젤 / KOSDAQ GLOBAL / active-like / 2024 shard available
028300: HLB / KOSDAQ / active-like / 2024 shard available
```

## 4. Case table

| case_id | symbol | entry | peak | trough | MFE | MAE | classification |
|---|---:|---:|---:|---:|---:|---:|---|
| C23_000100_2024_08_20_LAZERTINIB_US_APPROVAL_COMMERCIALIZATION_BRIDGE | 000100 | 94,000 | 166,900 | 91,500 | +77.55% | -2.66% | positive_regulatory_approval_to_commercialization_bridge |
| C23_145020_2024_03_04_LETYBO_US_APPROVAL_MODERATE_COMMERCIALIZATION_BRIDGE | 145020 | 202,500 | 231,000 | 172,300 | +14.07% | -14.91% | positive_control_moderate_mfe_high_mae |
| C23_028300_2024_05_16_FDA_EXPECTATION_TO_CRL_HARD_4C | 028300 | 95,800 | 98,100 | 45,150 | +2.40% | -52.87% | counterexample_regulatory_binary_failure_hard_4c |

## 5. Interpretation

### 5.1 000100 — confirmed approval + partner channel unlock

유한양행 is the cleanest C23 positive example. The FDA approval of lazertinib with amivantamab created a binary regulatory event, but the important C23 bridge is not the approval headline alone. The bridge is that the approval sits inside a partner commercialization route rather than a local single-company launch fantasy.

Observed path:

```text
entry close: 2024-08-20 / 94,000
peak high:   2024-10-15 / 166,900
trough low:  2024-08-22 / 91,500
MFE: +77.55%
MAE: -2.66%
```

This is the kind of C23 path where Stage2-Actionable should be allowed and Stage3-Yellow can be considered after the market confirms the commercialization bridge.

### 5.2 145020 — approval positive, but commercialization velocity still matters

휴젤 is an approval-positive case, but it is not a clean "raise everything to Green" case. The Letybo approval gave the market a regulatory anchor, yet the price path still had a deep local drawdown.

Observed path:

```text
entry close: 2024-03-04 / 202,500
peak high:   2024-04-30 / 231,000
trough low:  2024-03-21 / 172,300
MFE: +14.07%
MAE: -14.91%
```

This supports a narrower C23 rule: FDA approval plus commercial launch path can justify Stage2-Actionable, but Green should still require sell-through, launch timing, partner economics, and revision confirmation.

### 5.3 028300 — pending approval expectation should not be treated as approval

HLB is the clean counterexample. The pre-decision regulatory expectation behaved like an approval-commercialization story before the binary decision was known. The subsequent path shows why C23 needs a hard split between "pending approval" and "confirmed approval".

Observed path:

```text
entry close: 2024-05-16 / 95,800
post-entry peak high: 2024-07-08 / 98,100
trough low: 2024-05-21 / 45,150
MFE: +2.40%
MAE: -52.87%
```

This is not a Stage2-Actionable positive. It is a pending-approval / CRL hard 4C audit row.

## 6. Residual rule candidate

```text
new_axis_proposed =
c23_binary_approval_partner_commercialization_bridge_required_for_stage2_actionable_shadow_only
```

Candidate behavior:

```text
IF canonical_archetype_id == C23
AND trigger_type is approval expectation / pending FDA / pending regulator decision
AND there is no confirmed binary approval
THEN block positive Stage2-Actionable and route to 4B-watch or binary-event watch.

IF confirmed approval exists
AND partner/channel/reimbursement/launch timing exists
THEN allow Stage2-Actionable and consider Stage3-Yellow after price path confirms.

IF CRL / approval failure / inspection block / label failure occurs
THEN route to hard 4C, regardless of prior price strength.
```

This does not loosen Stage3-Green. It narrows the gate between approval-expectation beta and approval-to-commercialization bridge.

## 7. Machine-readable rows

### case_rows_jsonl
```jsonl
{"row_type": "case", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "102", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_VS_BINARY_CRL_FALSE_POSITIVE", "case_id": "C23_000100_2024_08_20_LAZERTINIB_US_APPROVAL_COMMERCIALIZATION_BRIDGE", "symbol": "000100", "name": "유한양행", "market": "KOSPI", "trigger_date": "2024-08-19", "entry_date": "2024-08-20", "entry_price": 94000, "peak_date": "2024-10-15", "peak_price": 166900, "trough_date": "2024-08-22", "trough_price": 91500, "exit_date": "2024-11-18", "exit_price": 119700, "mfe_pct": 77.55, "mae_pct": -2.66, "exit_return_pct": 27.34, "classification": "positive_regulatory_approval_to_commercialization_bridge", "trigger_type": "FDA_APPROVAL_COMMERCIALIZATION_BRIDGE", "evidence_family": "regulatory_approval_partner_commercialization", "path_label": "positive_high_mfe_low_mae", "calibration_usable": true, "representative_for_aggregate": true}
{"row_type": "case", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "102", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_VS_BINARY_CRL_FALSE_POSITIVE", "case_id": "C23_145020_2024_03_04_LETYBO_US_APPROVAL_MODERATE_COMMERCIALIZATION_BRIDGE", "symbol": "145020", "name": "휴젤", "market": "KOSDAQ GLOBAL", "trigger_date": "2024-02-29", "entry_date": "2024-03-04", "entry_price": 202500, "peak_date": "2024-04-30", "peak_price": 231000, "trough_date": "2024-03-21", "trough_price": 172300, "exit_date": "2024-05-31", "exit_price": 208500, "mfe_pct": 14.07, "mae_pct": -14.91, "exit_return_pct": 2.96, "classification": "positive_control_moderate_mfe_high_mae", "trigger_type": "FDA_APPROVAL_COMMERCIALIZATION_BRIDGE", "evidence_family": "regulatory_approval_us_commercial_entry", "path_label": "approval_positive_but_high_mae", "calibration_usable": true, "representative_for_aggregate": true}
{"row_type": "case", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "102", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_VS_BINARY_CRL_FALSE_POSITIVE", "case_id": "C23_028300_2024_05_16_FDA_EXPECTATION_TO_CRL_HARD_4C", "symbol": "028300", "name": "HLB", "market": "KOSDAQ", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 95800, "peak_date": "2024-07-08", "peak_price": 98100, "trough_date": "2024-05-21", "trough_price": 45150, "exit_date": "2024-08-16", "exit_price": 82500, "mfe_pct": 2.4, "mae_pct": -52.87, "exit_return_pct": -13.88, "classification": "counterexample_regulatory_binary_failure_hard_4c", "trigger_type": "FDA_APPROVAL_EXPECTATION_WITHOUT_CONFIRMATION", "evidence_family": "regulatory_binary_risk_crl", "path_label": "hard_4c_high_mae", "calibration_usable": true, "representative_for_aggregate": true}
```

### trigger_rows_jsonl
```jsonl
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "102", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_VS_BINARY_CRL_FALSE_POSITIVE", "case_id": "C23_000100_2024_08_20_LAZERTINIB_US_APPROVAL_COMMERCIALIZATION_BRIDGE", "symbol": "000100", "name": "유한양행", "trigger_date": "2024-08-19", "trigger_type": "FDA_APPROVAL_COMMERCIALIZATION_BRIDGE", "entry_date": "2024-08-20", "entry_price": 94000, "mfe_90d_pct": 77.55, "mae_90d_pct": -2.66, "classification": "positive_regulatory_approval_to_commercialization_bridge", "evidence_family": "regulatory_approval_partner_commercialization", "path_label": "positive_high_mfe_low_mae", "dedupe_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|000100|FDA_APPROVAL_COMMERCIALIZATION_BRIDGE|2024-08-20", "price_source": "Songdaiki/stock-web:atlas/ohlcv_tradable_by_symbol_year"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "102", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_VS_BINARY_CRL_FALSE_POSITIVE", "case_id": "C23_145020_2024_03_04_LETYBO_US_APPROVAL_MODERATE_COMMERCIALIZATION_BRIDGE", "symbol": "145020", "name": "휴젤", "trigger_date": "2024-02-29", "trigger_type": "FDA_APPROVAL_COMMERCIALIZATION_BRIDGE", "entry_date": "2024-03-04", "entry_price": 202500, "mfe_90d_pct": 14.07, "mae_90d_pct": -14.91, "classification": "positive_control_moderate_mfe_high_mae", "evidence_family": "regulatory_approval_us_commercial_entry", "path_label": "approval_positive_but_high_mae", "dedupe_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|145020|FDA_APPROVAL_COMMERCIALIZATION_BRIDGE|2024-03-04", "price_source": "Songdaiki/stock-web:atlas/ohlcv_tradable_by_symbol_year"}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "102", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "REGULATORY_APPROVAL_TO_COMMERCIALIZATION_BRIDGE_VS_BINARY_CRL_FALSE_POSITIVE", "case_id": "C23_028300_2024_05_16_FDA_EXPECTATION_TO_CRL_HARD_4C", "symbol": "028300", "name": "HLB", "trigger_date": "2024-05-16", "trigger_type": "FDA_APPROVAL_EXPECTATION_WITHOUT_CONFIRMATION", "entry_date": "2024-05-16", "entry_price": 95800, "mfe_90d_pct": 2.4, "mae_90d_pct": -52.87, "classification": "counterexample_regulatory_binary_failure_hard_4c", "evidence_family": "regulatory_binary_risk_crl", "path_label": "hard_4c_high_mae", "dedupe_key": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|028300|FDA_APPROVAL_EXPECTATION_WITHOUT_CONFIRMATION|2024-05-16", "price_source": "Songdaiki/stock-web:atlas/ohlcv_tradable_by_symbol_year"}
```

### score_simulation_rows_jsonl
```jsonl
{"row_type": "score_simulation", "case_id": "C23_000100_2024_08_20_LAZERTINIB_US_APPROVAL_COMMERCIALIZATION_BRIDGE", "symbol": "000100", "round": "R7", "loop": "102", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_total": 82.5, "current_profile_proxy": "Stage3-Yellow_to_Stage2-Actionable", "score_return_alignment": "aligned", "residual_error": "current profile may underweight binary regulatory approval when paired with partner commercialization channel"}
{"row_type": "score_simulation", "case_id": "C23_145020_2024_03_04_LETYBO_US_APPROVAL_MODERATE_COMMERCIALIZATION_BRIDGE", "symbol": "145020", "round": "R7", "loop": "102", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_total": 77.0, "current_profile_proxy": "Stage2-Actionable_watch", "score_return_alignment": "aligned", "residual_error": "approval alone is insufficient for Green unless commercialization velocity is visible"}
{"row_type": "score_simulation", "case_id": "C23_028300_2024_05_16_FDA_EXPECTATION_TO_CRL_HARD_4C", "symbol": "028300", "round": "R7", "loop": "102", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_total": 74.0, "current_profile_proxy": "Stage2_false_positive_to_4C", "score_return_alignment": "misaligned", "residual_error": "current profile can still over-credit pending approval expectation without binary decision and commercialization channel"}
```

### stage_transition_summary_jsonl
```jsonl
{"row_type": "stage_transition_summary", "case_id": "C23_000100_2024_08_20_LAZERTINIB_US_APPROVAL_COMMERCIALIZATION_BRIDGE", "symbol": "000100", "entry_date": "2024-08-20", "stage_current_proxy": "Stage3-Yellow_to_Stage2-Actionable", "observed_path_label": "positive_high_mfe_low_mae", "mfe_90d_pct": 77.55, "mae_90d_pct": -2.66}
{"row_type": "stage_transition_summary", "case_id": "C23_145020_2024_03_04_LETYBO_US_APPROVAL_MODERATE_COMMERCIALIZATION_BRIDGE", "symbol": "145020", "entry_date": "2024-03-04", "stage_current_proxy": "Stage2-Actionable_watch", "observed_path_label": "approval_positive_but_high_mae", "mfe_90d_pct": 14.07, "mae_90d_pct": -14.91}
{"row_type": "stage_transition_summary", "case_id": "C23_028300_2024_05_16_FDA_EXPECTATION_TO_CRL_HARD_4C", "symbol": "028300", "entry_date": "2024-05-16", "stage_current_proxy": "Stage2_false_positive_to_4C", "observed_path_label": "hard_4c_high_mae", "mfe_90d_pct": 2.4, "mae_90d_pct": -52.87}
```

### aggregate_metric_jsonl
```jsonl
{"row_type": "aggregate_metric", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "102", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "case_count": 3, "positive_case_count": 2, "counterexample_count": 1, "avg_mfe_pct": 31.34, "avg_mae_pct": -23.48, "median_mfe_pct": 14.07, "median_mae_pct": -14.91, "new_axis_proposed": "c23_binary_approval_partner_commercialization_bridge_required_for_stage2_actionable_shadow_only"}
```

### shadow_weight_jsonl
```jsonl
{"row_type": "shadow_weight", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "102", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "shadow_only": true, "axis": "c23_binary_approval_partner_commercialization_bridge_required_for_stage2_actionable_shadow_only", "proposed_rule": "C23 Stage2-Actionable requires confirmed regulatory decision plus commercialization bridge: partner/channel/reimbursement/launch timing. Pending approval expectation without binary decision routes to 4B watch or 4C on CRL.", "expected_effect": "Reduce C23 false positives from approval-expectation rallies while preserving positive approval-to-launch paths."}
```

### residual_contribution_jsonl
```jsonl
{"row_type": "residual_contribution", "schema_family": "v12_sector_archetype_residual", "round": "R7", "loop": "102", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_axis_proposed": "c23_binary_approval_partner_commercialization_bridge_required_for_stage2_actionable_shadow_only", "existing_axis_strengthened": "full_4b_requires_non_price_evidence scoped to C23 approval-expectation rallies", "existing_axis_weakened": null}
```

## 8. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent. Do not execute this prompt during the research run.

Task:
Batch-ingest this MD with other v12 residual research files. Evaluate whether the following shadow-only C23 axis is supported across the broader corpus:

c23_binary_approval_partner_commercialization_bridge_required_for_stage2_actionable_shadow_only

Implementation constraints:
- Do not loosen Stage3-Green.
- Do not treat pending approval expectation as confirmed approval.
- Confirmed approval alone is not enough for Green.
- Stage2-Actionable for C23 should require binary approval plus at least one commercialization bridge:
  partner/channel/reimbursement/launch timing/royalty economics.
- CRL or approval failure should override prior positive price strength and route to 4C/hard thesis break.

Primary rows in this MD:
- 000100 / 2024-08-20 / FDA_APPROVAL_COMMERCIALIZATION_BRIDGE / positive
- 145020 / 2024-03-04 / FDA_APPROVAL_COMMERCIALIZATION_BRIDGE / moderate positive with high MAE
- 028300 / 2024-05-16 / FDA_APPROVAL_EXPECTATION_WITHOUT_CONFIRMATION / hard 4C counterexample

Output:
Only propose a production patch if the same rule repeats across multiple C23 and C24/C25 adjacent cases. Otherwise keep this as shadow-only evidence.
```

# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 6
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: BIO_DEVICE_APPROVAL_EXPORT_HIGH_MAE_ROUTE_SPLIT_COMMERCIAL_BRIDGE_VS_LABEL_FAILURE
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

R13 is a cross-archetype guardrail checkpoint. This file does not add a new R7 bio sector-positive thesis. It tests the recent C23/C25 bio-device rows through the high-MAE routing lens.

The previous local `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` run reached loop 5, so this continuation is `loop 6`.

---

## 1. Research thesis

High MAE in bio/device names has to be routed by bridge quality, not by the headline.

```text
approval / export / device label
→ commercial revenue, launch cadence, reimbursement, royalty, installed base, consumable reorder, margin
→ price path decides whether Stage2 survives, stays local 4B, or becomes false positive
```

The route split:

```text
A. commercialized drug + visible revenue/profit + low MAE
   → keep Stage2, block hard 4C

B. approval-to-launch + high MFE + moderate MAE
   → keep Stage2, local 4B until launch revenue cadence

C. device installed-base/export bridge + high MFE + 180D MAE
   → keep Stage2, local 4B until consumable/margin refresh

D. approval/device label + low MFE + deep MAE
   → hard false-positive block

E. severe dental/digital device drawdown
   → hard block; do not keep Stage2 without recurring cash bridge
```

A headline is a doorway. The high-MAE guardrail asks whether there is a floor behind it.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_cases: 6
  source_archetypes:
    - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
    - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - cross-archetype high-MAE routing
    - local 4B vs hard block split
    - Stage3-Green block conditions
    - no production scoring changes
```

---

## 3. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - e2r_stock_web_v12_residual_round_R7_loop_137_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
  - e2r_stock_web_v12_residual_round_R7_loop_99_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
  - e2r_stock_web_v12_residual_round_R13_loop_9_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md
  - e2r_stock_web_v12_residual_round_R13_loop_8_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md
reason:
  - rows already computed from Songdaiki/stock-web tradable 1D OHLC
  - this run changes canonical scope to R13 high-MAE guardrail
  - no production scoring changed
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"APPROVED_DRUG_COMMERCIAL_REVENUE_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"326030","name":"SK바이오팜","trigger_type":"Stage2-Actionable","entry_date":"2024-08-12","entry_close":98800,"price_basis":"tradable_raw","mfe_30d_pct":20.95,"mae_30d_pct":-5.87,"mfe_90d_pct":31.58,"mae_90d_pct":-5.87,"mfe_180d_pct":31.58,"mae_180d_pct":-5.87,"forward_high_30d":119500,"forward_low_30d":93000,"forward_high_90d":130000,"forward_low_90d":93000,"forward_high_180d":130000,"forward_low_180d":93000,"calibration_usable":true,"case_role":"positive_control_block_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|326030|Stage2-Actionable|2024-08-12","route":"KeepStage2_BlockHard4C","guardrail_lesson":"commercialized drug revenue/profit bridge with low MAE should not be hard-blocked"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"FDA_APPROVAL_LAUNCH_BRIDGE_MODERATE_MAE_LOCAL_4B","source_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"006280","name":"녹십자","trigger_type":"Stage2-Actionable","entry_date":"2024-07-09","entry_close":124900,"price_basis":"tradable_raw","mfe_30d_pct":33.71,"mae_30d_pct":-4.56,"mfe_90d_pct":45.56,"mae_90d_pct":-4.56,"mfe_180d_pct":45.56,"mae_180d_pct":-10.49,"forward_high_30d":167000,"forward_low_30d":119200,"forward_high_90d":181800,"forward_low_90d":119200,"forward_high_180d":181800,"forward_low_180d":111800,"calibration_usable":true,"case_role":"local_4B_watch","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|006280|Stage2-Actionable|2024-07-09","route":"Local4B_UntilLaunchRevenueCadence","guardrail_lesson":"FDA approval-to-launch bridge keeps Stage2 alive, but Green waits for launch revenue cadence"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"APPROVAL_LABEL_LOW_MFE_DEEP_MAE_HARD_BLOCK","source_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"170900","name":"동아에스티","trigger_type":"Stage2-FalsePositive","entry_date":"2024-10-11","entry_close":76400,"price_basis":"tradable_raw","mfe_30d_pct":5.63,"mae_30d_pct":-20.16,"mfe_90d_pct":5.63,"mae_90d_pct":-36.32,"mfe_180d_pct":5.63,"mae_180d_pct":-46.47,"forward_high_30d":80700,"forward_low_30d":61000,"forward_high_90d":80700,"forward_low_90d":48650,"forward_high_180d":80700,"forward_low_180d":40900,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|170900|Stage2-FalsePositive|2024-10-11","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"approval label with low MFE and deep MAE should be hard-blocked without listed-company economics"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"DEVICE_EXPORT_INSTALLED_BASE_HIGH_MFE_180D_MAE_LOCAL_4B","source_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"335890","name":"비올","trigger_type":"Stage2-Actionable","entry_date":"2024-03-13","entry_close":8480,"price_basis":"tradable_raw","mfe_30d_pct":41.86,"mae_30d_pct":-13.92,"mfe_90d_pct":41.86,"mae_90d_pct":-13.92,"mfe_180d_pct":41.86,"mae_180d_pct":-21.82,"forward_high_30d":12030,"forward_low_30d":7300,"forward_high_90d":12030,"forward_low_90d":7300,"forward_high_180d":12030,"forward_low_180d":6630,"calibration_usable":true,"case_role":"device_bridge_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|335890|Stage2-Actionable|2024-03-13","route":"Local4B_RequireConsumableMarginRefresh","guardrail_lesson":"device installed-base/export bridge can survive Stage2, but 180D MAE blocks Green without reorder and margin refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"DENTAL_IMAGING_LABEL_LOW_MFE_HIGH_MAE_BLOCK","source_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"043150","name":"바텍","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-17","entry_close":30150,"price_basis":"tradable_raw","mfe_30d_pct":1.49,"mae_30d_pct":-13.10,"mfe_90d_pct":1.49,"mae_90d_pct":-24.71,"mfe_180d_pct":1.49,"mae_180d_pct":-38.64,"forward_high_30d":30600,"forward_low_30d":26200,"forward_high_90d":30600,"forward_low_90d":22700,"forward_high_180d":30600,"forward_low_180d":18500,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|043150|Stage2-FalsePositive|2024-05-17","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"dental imaging export label with low MFE and high MAE should be blocked without reimbursement/consumable bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"DIGITAL_DENTAL_LABEL_SEVERE_180D_MAE_HARD_BLOCK","source_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"228670","name":"레이","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-13","entry_close":17020,"price_basis":"tradable_raw","mfe_30d_pct":3.88,"mae_30d_pct":-23.21,"mfe_90d_pct":3.88,"mae_90d_pct":-39.07,"mfe_180d_pct":3.88,"mae_180d_pct":-70.15,"forward_high_30d":17680,"forward_low_30d":13070,"forward_high_90d":17680,"forward_low_90d":10370,"forward_high_180d":17680,"forward_low_180d":5080,"calibration_usable":true,"case_role":"severe_hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|228670|Stage2-FalsePositive|2024-03-13","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"severe MAE with digital dental label and no recurring cash bridge should be hard-blocked"}
```

---

## 5. Case analysis

### 5.1 SK Biopharm / 326030 — low-MAE positive control

The commercialized drug bridge produced MFE while drawdown stayed shallow.

```text
route = KeepStage2_BlockHard4C
```

### 5.2 Green Cross / 006280 — approval-to-launch local 4B

The FDA approval bridge is real. High MFE validates Stage2, but launch revenue cadence is needed before Green.

```text
route = Local4B_UntilLaunchRevenueCadence
```

### 5.3 Dong-A ST / 170900 — approval-label hard block

The label was real but listed-company economics were missing. Low MFE and deep MAE make it a hard block.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 5.4 VIOL / 335890 — device bridge local 4B

Installed-base/export economics can keep Stage2 open, but 180D MAE requires consumable/reorder/margin refresh.

```text
route = Local4B_RequireConsumableMarginRefresh
```

### 5.5 Vatech / 043150 — dental imaging hard block

Low MFE and high MAE show that export vocabulary did not become recurring cash economics.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 5.6 Ray / 228670 — severe hard block

This is the strongest false-positive guardrail row. Stage2 should not survive without recurring cash bridge.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_control_count: 1
local_4B_watch_count: 2
hard_4C_or_stage2_block_count: 3
current_profile_error_count: 4
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 326030 | C23 | keep Stage2 / block 4C | +31.58 / -5.87 | +31.58 / -5.87 | commercialized drug bridge validates |
| 006280 | C23 | local 4B | +45.56 / -4.56 | +45.56 / -10.49 | approval-to-launch needs revenue cadence |
| 170900 | C23 | hard block | +5.63 / -36.32 | +5.63 / -46.47 | approval label without economics fails |
| 335890 | C25 | local 4B | +41.86 / -13.92 | +41.86 / -21.82 | device bridge needs consumable refresh |
| 043150 | C25 | hard block | +1.49 / -24.71 | +1.49 / -38.64 | dental export label lacks bridge |
| 228670 | C25 | hard block | +3.88 / -39.07 | +3.88 / -70.15 | digital dental severe false positive |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"326030","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":0,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"006280","raw_bridge_quality":4,"raw_accounting_trust":3,"raw_mfe_validation":4,"raw_mae_penalty":1,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_UntilLaunchRevenue"}
{"row_type":"score_simulation","symbol":"170900","raw_bridge_quality":1,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":5,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"335890","raw_bridge_quality":4,"raw_accounting_trust":3,"raw_mfe_validation":4,"raw_mae_penalty":3,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_ConsumableRefresh"}
{"row_type":"score_simulation","symbol":"043150","raw_bridge_quality":1,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":4,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"228670","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

The profile can still make both mistakes:

```text
bad block:
all bio/device high-MAE cases -> hard 4C
```

This would kill Green Cross and VIOL too early.

```text
bad reward:
approval/device label + any MFE -> Stage2 or Green
```

This would keep Dong-A ST, Vatech, and Ray alive too long.

Correct routing:

```text
commercial bridge + low MAE -> keep Stage2
commercial bridge + drawdown -> local 4B
label-only + low MFE/high MAE -> hard block
```

### Rule candidate

```text
R13_HIGH_MAE_BIO_DEVICE_ROUTE_SPLIT_V6

if approved_drug_commercial_revenue_profit_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_hard_4C = true
```

```text
if approval_to_launch_or_device_installed_base_bridge == true
and MFE_30D_pct >= +30
and MAE_180D_pct <= -10:
    route = local_4B_watch
    block_stage3_green = true
    require_revenue_or_consumable_margin_refresh = true
```

```text
if approval_or_device_label == true
and listed_company_commercial_cash_bridge == false
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = hard_4C_or_Stage2_FalsePositive_Block
    stage2_actionable_bonus = 0
```

```text
if dental_or_digital_device_label == true
and MAE_180D_pct <= -50:
    route = hard_4C
    require_new_evidence_family_before_reopen = true
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_high_MAE_guardrail_candidate
new_axis_proposed: R13_HIGH_MAE_BIO_DEVICE_ROUTE_SPLIT_V6
existing_axis_strengthened:
  - commercialized_drug_low_MAE_keep_stage2
  - approval_launch_bridge_local_4B
  - device_installed_base_consumable_bridge_local_4B
  - approval_label_without_economics_hard_4C
  - severe_dental_device_drawdown_hard_4C
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this R13 loop with R13 accounting-trust bio/device loop 9, R13 Stage2 false-positive bio/device loop 8, C23 loop 137, C25 loop 99, and C24 trial-data guardrail files. Extract `R13_HIGH_MAE_BIO_DEVICE_ROUTE_SPLIT_V6` as a cross-archetype shadow rule. Preserve commercialized-drug and device installed-base escape hatches, but hard-block approval/device labels with low MFE and deep MAE when listed-company cash bridge is absent.
```

---

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 6
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT_retest_with_battery_and_grid_policy_controls
```

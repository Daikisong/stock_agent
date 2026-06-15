# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 8
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: BIO_DEVICE_APPROVAL_EXPORT_LABEL_STAGE2_FALSE_POSITIVE_GATE_VS_COMMERCIAL_REVENUE_AND_INSTALLED_BASE_ESCAPE
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

R13 is a cross-archetype guardrail checkpoint. This loop is not a new R7 bio sector-positive run. It reuses the current-session C23 and C25 stock-web-derived rows to test where Stage2 should be preserved and where it should be blocked.

The previous local `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW` run reached loop 7. This continuation is therefore `loop 8`.

---

## 1. Research thesis

Stage2 false positives in bio/device names usually come from confusing a label with a cash bridge.

```text
approval label / device export vocabulary / installed base story
→ must become commercial revenue, reimbursement, launch cadence, royalty, consumable reorder, margin, or profit
→ otherwise Stage2 should be capped or blocked
```

This loop tests six routes.

1. **Approved drug with commercial revenue/profit bridge**  
   Stage2 should survive.

2. **FDA approval with near-term launch bridge**  
   Stage2 may survive, but Green must wait for launch revenue cadence.

3. **Approval label without listed-company economics**  
   Stage2 false-positive block.

4. **Device export / installed base / consumable bridge**  
   Stage2 may survive with local 4B if drawdown appears.

5. **Dental imaging export label without reimbursement/consumable bridge**  
   Stage2 false-positive block.

6. **Digital dental vocabulary with severe MAE and no recurring cash bridge**  
   hard false-positive block.

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
    - cross-archetype Stage2 false-positive gate
    - approved-drug escape hatch
    - device installed-base local 4B
    - approval/device label hard-block logic
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
reason:
  - rows already computed from Songdaiki/stock-web tradable 1D OHLC
  - this run changes canonical scope to R13 Stage2 false-positive review
  - no production scoring changed
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"APPROVED_DRUG_COMMERCIAL_REVENUE_STAGE2_ESCAPE_HATCH","source_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"326030","name":"SK바이오팜","trigger_type":"Stage2-Actionable","entry_date":"2024-08-12","entry_close":98800,"price_basis":"tradable_raw","mfe_30d_pct":20.95,"mae_30d_pct":-5.87,"mfe_90d_pct":31.58,"mae_90d_pct":-5.87,"mfe_180d_pct":31.58,"mae_180d_pct":-5.87,"forward_high_30d":119500,"forward_low_30d":93000,"forward_high_90d":130000,"forward_low_90d":93000,"forward_high_180d":130000,"forward_low_180d":93000,"calibration_usable":true,"case_role":"positive_escape_hatch","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|326030|Stage2-Actionable|2024-08-12","stage2_error":"none; approved drug has visible commercialization, revenue and profit bridge","route":"KeepStage2_CommercialRevenueBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"FDA_APPROVAL_STAGE2_KEEP_BUT_GREEN_BLOCK_UNTIL_LAUNCH_REVENUE","source_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"006280","name":"녹십자","trigger_type":"Stage2-Actionable","entry_date":"2024-07-09","entry_close":124900,"price_basis":"tradable_raw","mfe_30d_pct":33.71,"mae_30d_pct":-4.56,"mfe_90d_pct":45.56,"mae_90d_pct":-4.56,"mfe_180d_pct":45.56,"mae_180d_pct":-10.49,"forward_high_30d":167000,"forward_low_30d":119200,"forward_high_90d":181800,"forward_low_90d":119200,"forward_high_180d":181800,"forward_low_180d":111800,"calibration_usable":true,"case_role":"stage2_keep_with_4B","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|006280|Stage2-Actionable|2024-07-09","stage2_error":"approval is valid but Green before launch revenue cadence would be premature","route":"KeepStage2_Local4BUntilLaunchRevenue"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"BIOSIMILAR_APPROVAL_LABEL_WITHOUT_LISTED_COMPANY_ECONOMICS_BLOCK","source_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"170900","name":"동아에스티","trigger_type":"Stage2-FalsePositive","entry_date":"2024-10-11","entry_close":76400,"price_basis":"tradable_raw","mfe_30d_pct":5.63,"mae_30d_pct":-20.16,"mfe_90d_pct":5.63,"mae_90d_pct":-36.32,"mfe_180d_pct":5.63,"mae_180d_pct":-46.47,"forward_high_30d":80700,"forward_low_30d":61000,"forward_high_90d":80700,"forward_low_90d":48650,"forward_high_180d":80700,"forward_low_180d":40900,"calibration_usable":true,"case_role":"hard_false_positive","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|170900|Stage2-FalsePositive|2024-10-11","stage2_error":"approval label lacked listed-company royalty, launch, reimbursement or margin bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_INSTALLED_BASE_STAGE2_KEEP_WITH_4B","source_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"335890","name":"비올","trigger_type":"Stage2-Actionable","entry_date":"2024-03-13","entry_close":8480,"price_basis":"tradable_raw","mfe_30d_pct":41.86,"mae_30d_pct":-13.92,"mfe_90d_pct":41.86,"mae_90d_pct":-13.92,"mfe_180d_pct":41.86,"mae_180d_pct":-21.82,"forward_high_30d":12030,"forward_low_30d":7300,"forward_high_90d":12030,"forward_low_90d":7300,"forward_high_180d":12030,"forward_low_180d":6630,"calibration_usable":true,"case_role":"device_positive_with_4B","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|335890|Stage2-Actionable|2024-03-13","stage2_error":"none for Stage2, but 180D drawdown means installed-base/consumable margin refresh required before Green","route":"KeepStage2_Local4BConsumableRefresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"DENTAL_IMAGING_EXPORT_LABEL_WITHOUT_REIMBURSEMENT_STAGE2_BLOCK","source_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"043150","name":"바텍","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-17","entry_close":30150,"price_basis":"tradable_raw","mfe_30d_pct":1.49,"mae_30d_pct":-13.10,"mfe_90d_pct":1.49,"mae_90d_pct":-24.71,"mfe_180d_pct":1.49,"mae_180d_pct":-38.64,"forward_high_30d":30600,"forward_low_30d":26200,"forward_high_90d":30600,"forward_low_90d":22700,"forward_high_180d":30600,"forward_low_180d":18500,"calibration_usable":true,"case_role":"device_label_false_positive","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|043150|Stage2-FalsePositive|2024-05-17","stage2_error":"dental imaging/export label lacked reimbursement, consumable, revision or cash bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":8,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"DIGITAL_DENTAL_LABEL_SEVERE_MAE_STAGE2_HARD_BLOCK","source_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"228670","name":"레이","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-13","entry_close":17020,"price_basis":"tradable_raw","mfe_30d_pct":3.88,"mae_30d_pct":-23.21,"mfe_90d_pct":3.88,"mae_90d_pct":-39.07,"mfe_180d_pct":3.88,"mae_180d_pct":-70.15,"forward_high_30d":17680,"forward_low_30d":13070,"forward_high_90d":17680,"forward_low_90d":10370,"forward_high_180d":17680,"forward_low_180d":5080,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|228670|Stage2-FalsePositive|2024-03-13","stage2_error":"digital dental label had no recurring revenue, reimbursement, installed-base, consumable or margin bridge","route":"Stage2FalsePositiveBlock"}
```

---

## 5. Case analysis

### 5.1 SK Biopharm / 326030 — Stage2 escape hatch

SK Biopharm prevents the guardrail from blocking all approval stories. The commercial bridge was visible and price validated with contained MAE.

```text
route = KeepStage2_CommercialRevenueBridge
```

### 5.2 Green Cross / 006280 — approval-to-launch bridge, not immediate Green

Green Cross had a valid FDA approval-to-launch setup. Stage2 stays open, but launch revenue cadence is needed before Green.

```text
route = KeepStage2_Local4BUntilLaunchRevenue
```

### 5.3 Dong-A ST / 170900 — approval label block

Dong-A ST is the approval-label false positive. Approval alone did not become listed-company economics in the validation window.

```text
route = Stage2FalsePositiveBlock
```

### 5.4 VIOL / 335890 — device installed-base bridge with 4B watch

VIOL is a device positive with local 4B. Installed-base and consumable economics can support Stage2, but the 180D drawdown requires refresh.

```text
route = KeepStage2_Local4BConsumableRefresh
```

### 5.5 Vatech / 043150 — dental imaging label block

Vatech shows that export/dental vocabulary is not enough.

```text
route = Stage2FalsePositiveBlock
```

### 5.6 Ray / 228670 — severe digital-dental false positive

Ray is the hard counterexample. The label was present, but the cash bridge was absent and MAE became extreme.

```text
route = Stage2FalsePositiveBlock
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_escape_or_control_count: 1
stage2_keep_with_4B_count: 2
stage2_false_positive_count: 3
current_profile_error_count: 4
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 326030 | C23 | KeepStage2 | +31.58 / -5.87 | +31.58 / -5.87 | commercialization bridge validates |
| 006280 | C23 | Stage2 + 4B | +45.56 / -4.56 | +45.56 / -10.49 | launch revenue cadence needed for Green |
| 170900 | C23 | hard block | +5.63 / -36.32 | +5.63 / -46.47 | approval label lacks economics |
| 335890 | C25 | Stage2 + 4B | +41.86 / -13.92 | +41.86 / -21.82 | installed-base/consumable bridge needs refresh |
| 043150 | C25 | hard block | +1.49 / -24.71 | +1.49 / -38.64 | dental export label lacks bridge |
| 228670 | C25 | hard block | +3.88 / -39.07 | +3.88 / -70.15 | digital dental label hard false positive |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"326030","raw_approval_label":3,"raw_commercial_revenue_bridge":5,"raw_reimbursement_or_market_access":3,"raw_consumable_or_recurring_bridge":0,"raw_margin_profit_bridge":4,"raw_validation":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_CommercialRevenueBridge"}
{"row_type":"score_simulation","symbol":"006280","raw_approval_label":5,"raw_commercial_revenue_bridge":3,"raw_reimbursement_or_market_access":3,"raw_consumable_or_recurring_bridge":0,"raw_margin_profit_bridge":2,"raw_validation":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_Local4BUntilLaunchRevenue"}
{"row_type":"score_simulation","symbol":"170900","raw_approval_label":4,"raw_commercial_revenue_bridge":1,"raw_reimbursement_or_market_access":1,"raw_consumable_or_recurring_bridge":0,"raw_margin_profit_bridge":1,"raw_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"335890","raw_approval_label":0,"raw_commercial_revenue_bridge":4,"raw_reimbursement_or_market_access":2,"raw_consumable_or_recurring_bridge":4,"raw_margin_profit_bridge":3,"raw_validation":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_Local4BConsumableRefresh"}
{"row_type":"score_simulation","symbol":"043150","raw_approval_label":0,"raw_commercial_revenue_bridge":1,"raw_reimbursement_or_market_access":0,"raw_consumable_or_recurring_bridge":1,"raw_margin_profit_bridge":1,"raw_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"228670","raw_approval_label":0,"raw_commercial_revenue_bridge":0,"raw_reimbursement_or_market_access":0,"raw_consumable_or_recurring_bridge":0,"raw_margin_profit_bridge":0,"raw_validation":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

The current profile can still open Stage2 too easily for:

```text
approval headline
device export label
dental/digital device vocabulary
```

The right test:

```text
Does the product cross into accounts?
```

A drug approval is a passport, not a paycheck. A device shipment is hardware, not always recurring margin. The score should look for prescriptions, reimbursement, launch revenue, royalties, installed base, consumables, reorder, service and profit.

### Rule candidate

```text
R13_STAGE2_FALSE_POSITIVE_BIO_DEVICE_GATE_V8

if approval_or_device_label == true
and listed_company_revenue_reimbursement_royalty_consumable_margin_or_profit_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if approved_drug_commercial_revenue_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

```text
if FDA_approval_to_launch_bridge == true
and quarterly_launch_revenue_cadence == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if device_installed_base_or_consumable_bridge == true
and MFE_30D_pct >= +30
and MAE_180D_pct <= -20:
    local_4B_watch = true
    require_reorder_margin_refresh = true
```

```text
if dental_or_digital_device_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2FalsePositiveBlock
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_stage2_false_positive_guardrail_candidate
new_axis_proposed: R13_STAGE2_FALSE_POSITIVE_BIO_DEVICE_GATE_V8
existing_axis_strengthened:
  - approved_drug_commercialization_escape_hatch
  - FDA_approval_launch_bridge_4B_until_revenue_cadence
  - approval_label_without_economics_stage2_block
  - device_installed_base_consumable_bridge_4B
  - dental_device_label_false_positive_block
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this R13 loop with R13 accounting-trust bio/device loop 9, C23 loop 137, C25 loop 99, and adjacent Stage2 false-positive files. Extract `R13_STAGE2_FALSE_POSITIVE_BIO_DEVICE_GATE_V8` as a shadow-rule candidate. Preserve approved-drug commercialization and device installed-base/consumable escape hatches while blocking approval/device labels without listed-company revenue, reimbursement, royalty, consumable, margin or profit bridge.
```

---

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 8
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```

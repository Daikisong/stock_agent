# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 5
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: FINANCIAL_INSURANCE_PF_LABEL_STAGE2_FALSE_POSITIVE_VS_DIRECT_ROE_RESERVE_BRIDGE_ESCAPE
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

R13 is a cross-archetype red-team checkpoint. This loop tests Stage2 false positives from recent C21/C22/C30 outputs rather than adding a new sector-specific positive.

The prior local `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW` run reached loop 4. This continuation is therefore `loop 5`.

---

## 1. Research thesis

Stage2 should open only when a label has a transmission shaft into listed-company economics.

```text
low PBR / Value-up / insurance / PF-support label
→ must become ROE, capital return, reserve quality, commission cash conversion, refinancing relief, or issuer-specific cash bridge
→ price path must validate
```

If the bridge is absent, the signal is only a signboard. A signboard can attract a crowd, but it cannot move the machinery.

This loop separates five routes:

1. **Direct ROE/capital-return or reserve bridge escape hatch**  
   Keep Stage2 when the accounting bridge and price path both validate.

2. **Weak low-PBR / Value-up label**  
   Cap or block Stage2 when MFE stays below +10 and bridge proof is absent.

3. **Insurance distribution / GA label**  
   Reclassify away from C22 reserve-cycle logic unless reserve/solvency bridge is present.

4. **PF support / large-builder label**  
   Block Stage2 if issuer-specific refinancing or cash bridge is absent and price path fails.

5. **Direct workout stress-control**  
   Use as a stress row, not clean aggregate, because survival bridge and equity bridge are not the same.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_cases: 7
  source_archetypes:
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C22_INSURANCE_RATE_CYCLE_RESERVE
    - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - cross-archetype Stage2 false-positive guardrail
    - direct-bridge escape-hatch preservation
    - no production scoring changes
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"SECURITIES_ROE_CAPITAL_RETURN_DIRECT_BRIDGE_ESCAPE_HATCH","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"005940","name":"NH투자증권","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":11420,"price_basis":"tradable_raw","mfe_30d_pct":14.71,"mae_30d_pct":-2.36,"mfe_90d_pct":14.71,"mae_90d_pct":-2.36,"mfe_180d_pct":26.09,"mae_180d_pct":-2.36,"forward_high_30d":13100,"forward_low_30d":11150,"forward_high_90d":13100,"forward_low_90d":11150,"forward_high_180d":14400,"forward_low_180d":11150,"calibration_usable":true,"case_role":"positive_escape_hatch","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|005940|Stage2-Actionable|2024-02-26","stage2_error":"none; direct securities ROE/capital-return bridge validated","route":"KeepStage2_DirectBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOW_PBR_SECURITIES_LABEL_LOW_MFE_HIGH_MAE_STAGE2_BLOCK","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage2-FalsePositive","entry_date":"2024-02-26","entry_close":8680,"price_basis":"tradable_raw","mfe_30d_pct":5.53,"mae_30d_pct":-10.71,"mfe_90d_pct":5.53,"mae_90d_pct":-20.16,"mfe_180d_pct":5.53,"mae_180d_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|006800|Stage2-FalsePositive|2024-02-26","stage2_error":"low-PBR brokerage label without post-trigger ROE/capital-return validation","route":"Stage2_FalsePositive_Block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"GA_INSURANCE_DISTRIBUTION_LABEL_STAGE2_CAP_RECLASSIFY","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"244920","name":"에이플러스에셋","trigger_type":"Stage2-Watch","entry_date":"2024-05-10","entry_close":4100,"price_basis":"tradable_raw","mfe_30d_pct":9.76,"mae_30d_pct":-2.32,"mfe_90d_pct":9.76,"mae_90d_pct":-13.78,"mfe_180d_pct":14.63,"mae_180d_pct":-13.78,"forward_high_30d":4500,"forward_low_30d":4005,"forward_high_90d":4500,"forward_low_90d":3535,"forward_high_180d":4700,"forward_low_180d":3535,"calibration_usable":true,"case_role":"stage2_cap_reclassification","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|244920|Stage2-Watch|2024-05-10","stage2_error":"insurance-adjacent GA label without reserve/solvency/rate-cycle bridge","route":"Stage2Cap_ReclassifyToDistributionCommission"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"GA_DISTRIBUTION_HIGH_MFE_4B_NOT_C22_GREEN","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"211050","name":"인카금융서비스","trigger_type":"Stage2-Watch","entry_date":"2024-05-02","entry_close":4925,"price_basis":"tradable_raw","mfe_30d_pct":31.57,"mae_30d_pct":-4.57,"mfe_90d_pct":31.57,"mae_90d_pct":-16.35,"mfe_180d_pct":31.57,"mae_180d_pct":-16.35,"forward_high_30d":6480,"forward_low_30d":4700,"forward_high_90d":6480,"forward_low_90d":4120,"forward_high_180d":6480,"forward_low_180d":4120,"calibration_usable":true,"case_role":"vertical_MFE_reclassification_watch","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|211050|Stage2-Watch|2024-05-02","stage2_error":"high MFE came from GA distribution/commission economics, not C22 reserve-cycle validation","route":"Local4B_Reclassify_NotStage3Green"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"REINSURANCE_RESERVE_RATE_CYCLE_LOW_VOL_CONTROL","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"003690","name":"코리안리","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_close":7930,"price_basis":"tradable_raw","mfe_30d_pct":6.81,"mae_30d_pct":-1.01,"mfe_90d_pct":6.81,"mae_90d_pct":-5.42,"mfe_180d_pct":13.49,"mae_180d_pct":-5.42,"forward_high_30d":8470,"forward_low_30d":7850,"forward_high_90d":8470,"forward_low_90d":7500,"forward_high_180d":9000,"forward_low_180d":7500,"calibration_usable":true,"case_role":"reused_positive_control","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|003690|Stage2-Watch|2024-02-26","stage2_error":"none; visible-covered reinsurance control, low-vol reserve-cycle bridge","route":"KeepStage2Watch_Control"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LARGEBUILDER_PF_SUPPORT_LABEL_LOW_MFE_HIGH_MAE_STAGE2_BLOCK","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"000720","name":"현대건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-27","entry_close":33250,"price_basis":"tradable_raw","mfe_30d_pct":4.81,"mae_30d_pct":-6.17,"mfe_90d_pct":8.27,"mae_90d_pct":-6.17,"mfe_180d_pct":8.27,"mae_180d_pct":-27.52,"forward_high_30d":34850,"forward_low_30d":31200,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":24100,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|000720|Stage2-FalsePositive|2024-03-27","stage2_error":"PF support / large-builder label without issuer-specific refinancing or cash bridge","route":"Stage2_FalsePositive_Block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"DIRECT_WORKOUT_STRESS_CONTROL_NOT_STAGE2_RECOVERY","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"009410","name":"태영건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-11","entry_close":3765,"price_basis":"tradable_raw","mfe_30d_pct":9.16,"mae_30d_pct":-42.10,"mfe_90d_pct":9.16,"mae_90d_pct":-42.10,"mfe_180d_pct":62.28,"mae_180d_pct":-42.10,"forward_high_30d":4110,"forward_low_30d":2180,"forward_high_90d":4110,"forward_low_90d":2180,"forward_high_180d":6110,"forward_low_180d":2180,"calibration_usable":false,"case_role":"stress_control_excluded_from_clean_aggregate","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|009410|Stage2-Watch|2024-01-11","stage2_error":"direct workout survival bridge does not equal clean equity recovery and has corporate-action/trading-gap contamination","route":"StressControl_ExcludeCleanAggregate"}
```

---

## 4. Case analysis

### 4.1 NH Investment & Securities / 005940 — direct bridge escape hatch

`NH투자증권` prevents the Stage2 false-positive guardrail from becoming a blanket anti-financial rule. The trigger had a credible securities ROE/capital-return bridge, and price validated with MFE +26.09% by 180D and MAE only -2.36%.

```text
route = KeepStage2_DirectBridge
```

This is the axle that should remain connected. When ROE, brokerage/IB/WM flow, and shareholder-return expectations are visible, R13 should not zero the Stage2 bonus.

---

### 4.2 Mirae Asset Securities / 006800 — low-PBR brokerage label false positive

`미래에셋증권` is the brokerage false-positive. It had the same broad Value-up/low-PBR context, but MFE stayed below +6% while MAE went below -20% by 90D.

```text
route = Stage2_FalsePositive_Block
```

This is the key C21 guardrail: cheapness is not a cash-flow bridge.

---

### 4.3 A Plus Asset / 244920 — GA label cap

`에이플러스에셋` is insurance-adjacent but not an insurance balance-sheet case. Its economics are commission/distribution driven. That can be useful in another axis, but it does not validate C22 reserve/rate-cycle scoring.

```text
route = Stage2Cap_ReclassifyToDistributionCommission
```

---

### 4.4 INCA Financial Service / 211050 — high MFE, but not C22 Green

`인카금융서비스` is more dangerous because the MFE was high. Price-only learning could wrongly label it as a C22 hit. But the bridge is GA commission/distribution, not reserve adequacy or solvency capital.

```text
route = Local4B_Reclassify_NotStage3Green
```

---

### 4.5 Korean Re / 003690 — low-vol reinsurance control

`코리안리` is already visible in the no-repeat index, so it is a reused control, not new coverage. It anchors what a more economically native C22 case looks like: reinsurance pricing/reserve/underwriting-cycle logic, modest MFE, shallow MAE.

```text
route = KeepStage2Watch_Control
```

---

### 4.6 Hyundai E&C / 000720 — PF support label false positive

`현대건설` is the clean C30 hard counterexample. It had a large-builder/support label but no issuer-specific refinancing/cash bridge. Price MFE stayed below +10 and 180D MAE reached -27.52%.

```text
route = Stage2_FalsePositive_Block
```

---

### 4.7 Taeyoung E&C / 009410 — direct workout stress-control

`태영건설` is not a clean aggregate row. Workout is a survival bridge first, not an equity bridge. The full window also has corporate-action/trading-gap contamination.

```text
route = StressControl_ExcludeCleanAggregate
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 5
reused_control_case_count: 2
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_escape_or_control_count: 2
stage2_cap_or_reclassification_count: 2
hard_false_positive_count: 2
stress_control_excluded_count: 1
current_profile_error_count: 5
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 005940 | C21 | KeepStage2 | +14.71 / -2.36 | +26.09 / -2.36 | direct ROE/capital-return bridge validates |
| 006800 | C21 | hard block | +5.53 / -20.16 | +5.53 / -23.96 | low-PBR brokerage label fails |
| 244920 | C22 | Stage2 cap | +9.76 / -13.78 | +14.63 / -13.78 | GA distribution is not reserve cycle |
| 211050 | C22 | 4B/reclassify | +31.57 / -16.35 | +31.57 / -16.35 | high MFE but wrong C22 bridge |
| 003690 | C22 | reused control | +6.81 / -5.42 | +13.49 / -5.42 | low-vol reinsurance control |
| 000720 | C30 | hard block | +8.27 / -6.17 | +8.27 / -27.52 | PF support label fails without issuer bridge |
| 009410 | C30 | stress-only | +9.16 / -42.10 | +62.28 / -42.10 | workout is not clean equity recovery |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"005940","raw_direct_bridge":4,"raw_revenue_or_ROE_bridge":4,"raw_capital_or_reserve_bridge":3,"raw_validation":4,"raw_label_only_risk":0,"raw_contamination_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_DirectBridge"}
{"row_type":"score_simulation","symbol":"006800","raw_direct_bridge":1,"raw_revenue_or_ROE_bridge":1,"raw_capital_or_reserve_bridge":1,"raw_validation":0,"raw_label_only_risk":4,"raw_contamination_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2_FalsePositive_Block"}
{"row_type":"score_simulation","symbol":"244920","raw_direct_bridge":1,"raw_revenue_or_ROE_bridge":2,"raw_capital_or_reserve_bridge":0,"raw_validation":1,"raw_label_only_risk":3,"raw_contamination_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_Reclassify"}
{"row_type":"score_simulation","symbol":"211050","raw_direct_bridge":2,"raw_revenue_or_ROE_bridge":3,"raw_capital_or_reserve_bridge":0,"raw_validation":2,"raw_label_only_risk":3,"raw_contamination_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_Reclassify"}
{"row_type":"score_simulation","symbol":"003690","raw_direct_bridge":2,"raw_revenue_or_ROE_bridge":2,"raw_capital_or_reserve_bridge":3,"raw_validation":2,"raw_label_only_risk":0,"raw_contamination_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Reinsurance_Control"}
{"row_type":"score_simulation","symbol":"000720","raw_direct_bridge":0,"raw_revenue_or_ROE_bridge":0,"raw_capital_or_reserve_bridge":0,"raw_validation":0,"raw_label_only_risk":4,"raw_contamination_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2_FalsePositive_Block"}
{"row_type":"score_simulation","symbol":"009410","raw_direct_bridge":2,"raw_revenue_or_ROE_bridge":0,"raw_capital_or_reserve_bridge":0,"raw_validation":0,"raw_label_only_risk":2,"raw_contamination_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"StressControl_ExcludeCleanAggregate"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The current profile can still over-score:

```text
financial / insurance / PF label
+ macro policy headline
+ short-lived MFE
```

This can fail in three ways:

1. `low PBR` is not shareholder-return execution.
2. `insurance-adjacent` is not reserve quality.
3. `workout/support` is not necessarily equity recovery.

### Rule candidate

```text
R13_STAGE2_FALSE_POSITIVE_LABEL_BRIDGE_GATE_V5

if label_trigger == true
and company_specific_revenue_ROE_reserve_capital_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if MFE_90D_pct < +10
and MAE_90D_pct <= -15
and company_specific_bridge == false:
    route = Stage2_FalsePositive_Block
```

```text
if insurance_distribution_or_GA_label == true
and reserve_solvency_rate_cycle_bridge == false:
    route = Stage2Cap_ReclassifyToDistributionCommission
    block_C22_stage3_green = true
```

```text
if MFE_30D_pct >= +25
and bridge_belongs_to_other_axis == true:
    route = Local4B_Reclassify
    block_stage3_green_for_selected_archetype = true
```

```text
if direct_workout_or_support_headline == true
and shareholder_equity_bridge == false:
    route = StressControl_or_Stage2FalsePositiveBlock
    stage2_actionable_bonus = 0
```

```text
if direct_ROE_capital_return_or_reserve_bridge == true
and MFE_90D_pct >= +10
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_stage2_false_positive_guardrail_candidate
new_axis_proposed: R13_STAGE2_FALSE_POSITIVE_LABEL_BRIDGE_GATE_V5
existing_axis_strengthened:
  - low_PBR_label_without_ROE_capital_return_execution_block
  - GA_distribution_not_C22_reserve_cycle_reclassification
  - PF_support_label_without_issuer_bridge_block
  - direct_workout_survival_not_equity_recovery_stress_control
  - direct_bridge_escape_hatch_keep_stage2
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_retest_with_digital_financial_and_brokerage_counterexamples
C22_INSURANCE_RATE_CYCLE_RESERVE_retest_with_healthcare_underwriting_controls
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
```

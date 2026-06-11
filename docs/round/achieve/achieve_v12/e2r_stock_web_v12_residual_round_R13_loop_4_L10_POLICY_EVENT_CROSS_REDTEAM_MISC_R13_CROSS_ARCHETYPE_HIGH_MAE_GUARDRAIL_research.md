# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 4
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: FINANCIAL_INSURANCE_AND_PF_HIGH_MAE_ROUTE_SPLIT_REAL_BRIDGE_VS_LABEL_OR_WORKOUT_STRESS
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

R13 is a cross-archetype red-team checkpoint. This run does not add a new sector-positive archetype. It retests recent `C21`, `C22`, and `C30` outputs through the high-MAE routing lens.

The prior local `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` run reached loop 3, so this continuation is loop 4.

---

## 1. Research thesis

High MAE is not one disease. It is a fever that can come from several different organs.

```text
A. Real accounting / capital-return / reserve-quality bridge + manageable MAE
   → keep Stage2; block hard 4C

B. Real bridge + high-ish MAE
   → local 4B watch; require bridge refresh before Green

C. Weak label + low MFE + meaningful MAE
   → Stage2 cap or false-positive block

D. Direct workout / restructuring + high MFE and high MAE
   → stress-control only; do not learn as clean equity recovery

E. PF support label / large-builder label + low MFE and deep MAE
   → hard block unless issuer-specific refinancing/cash bridge appears
```

The goal is to stop the current profile from making two opposite mistakes:

1. Killing a real bridge merely because the path had a drawdown.
2. Rewarding a violent spike or sector label merely because it had temporary MFE.

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
    - cross-archetype high-MAE routing
    - local 4B vs hard block split
    - no production scoring changes
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"NONLIFE_RESERVE_QUALITY_LOW_MAE_POSITIVE_CONTROL_BLOCK_HARD_4C","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":95000,"price_basis":"tradable_raw","mfe_30d_pct":15.79,"mae_30d_pct":-4.11,"mfe_90d_pct":27.05,"mae_90d_pct":-9.26,"mfe_180d_pct":30.53,"mae_180d_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"calibration_usable":true,"case_role":"positive_control","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|005830|Stage2-Actionable|2024-02-26","route":"KeepStage2_BlockHard4C","guardrail_lesson":"reserve/loss-ratio quality bridge plus strong MFE and low MAE should not be penalized"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"BANK_CAPITAL_RETURN_REAL_BRIDGE_HIGH_MAE_LOCAL_4B","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"105560","name":"KB금융","trigger_type":"Stage2-Actionable","entry_date":"2024-07-26","entry_close":87900,"price_basis":"tradable_raw","mfe_30d_pct":5.12,"mae_30d_pct":-15.81,"mfe_90d_pct":18.20,"mae_90d_pct":-15.81,"mfe_180d_pct":18.20,"mae_180d_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"calibration_usable":true,"case_role":"real_bridge_local_4B_watch","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|105560|Stage2-Actionable|2024-07-26","route":"Local4B_NotHard4C","guardrail_lesson":"bank capital-return bridge can survive high MAE, but Stage3-Green requires CET1/credit-cost/shareholder-return refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LOW_PBR_BANK_LABEL_LOW_MFE_MID_MAE_STAGE2_CAP","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"316140","name":"우리금융지주","trigger_type":"Stage2-Watch","entry_date":"2024-07-26","entry_close":16180,"price_basis":"tradable_raw","mfe_30d_pct":4.08,"mae_30d_pct":-15.08,"mfe_90d_pct":5.69,"mae_90d_pct":-15.08,"mfe_180d_pct":5.69,"mae_180d_pct":-15.08,"forward_high_30d":16840,"forward_low_30d":13740,"forward_high_90d":17100,"forward_low_90d":13740,"forward_high_180d":17100,"forward_low_180d":13740,"calibration_usable":true,"case_role":"weak_bridge_cap","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|316140|Stage2-Watch|2024-07-26","route":"Stage2Cap","guardrail_lesson":"low-PBR bank label with MFE below 10 should not stay actionable without incremental capital-return execution"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_LABEL_LOW_MFE_MID_MAE_STAGE2_CAP","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"088350","name":"한화생명","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_close":3060,"price_basis":"tradable_raw","mfe_30d_pct":9.31,"mae_30d_pct":-8.17,"mfe_90d_pct":9.31,"mae_90d_pct":-15.69,"mfe_180d_pct":9.31,"mae_180d_pct":-15.69,"forward_high_30d":3345,"forward_low_30d":2810,"forward_high_90d":3345,"forward_low_90d":2580,"forward_high_180d":3345,"forward_low_180d":2580,"calibration_usable":true,"case_role":"weak_life_label_cap","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|088350|Stage2-Watch|2024-02-26","route":"Stage2Cap","guardrail_lesson":"life-insurance value-up label should be capped when reserve/solvency/capital-policy bridge is not refreshed and MFE stays under 10"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"DIRECT_WORKOUT_HIGH_MFE_HIGH_MAE_STRESS_CONTROL_NOT_CLEAN_AGGREGATE","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"009410","name":"태영건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-11","entry_close":3765,"price_basis":"tradable_raw","mfe_30d_pct":9.16,"mae_30d_pct":-42.10,"mfe_90d_pct":9.16,"mae_90d_pct":-42.10,"mfe_180d_pct":62.28,"mae_180d_pct":-42.10,"forward_high_30d":4110,"forward_low_30d":2180,"forward_high_90d":4110,"forward_low_90d":2180,"forward_high_180d":6110,"forward_low_180d":2180,"calibration_usable":false,"case_role":"workout_stress_control","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|009410|Stage2-Watch|2024-01-11","route":"StressControl_ExcludeCleanAggregate","guardrail_lesson":"direct workout may save survival value but does not automatically create clean shareholder recovery; corporate-action/trading-gap contamination must be blocked"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"LARGE_BUILDER_LABEL_LOW_MFE_HIGH_MAE_HARD_BLOCK","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"000720","name":"현대건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-27","entry_close":33250,"price_basis":"tradable_raw","mfe_30d_pct":4.81,"mae_30d_pct":-6.17,"mfe_90d_pct":8.27,"mae_90d_pct":-6.17,"mfe_180d_pct":8.27,"mae_180d_pct":-27.52,"forward_high_30d":34850,"forward_low_30d":31200,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":24100,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|000720|Stage2-FalsePositive|2024-03-27","route":"Stage2FalsePositiveBlock","guardrail_lesson":"large-builder or PF-support label with MFE below 10 and full-window MAE below -25 should be hard-blocked without issuer-specific bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":4,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"MID_BUILDER_DELAYED_POSITIVE_LOW_MAE_4B_WATCH","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"014790","name":"HL D&I","trigger_type":"Stage2-Watch","entry_date":"2024-03-27","entry_close":2010,"price_basis":"tradable_raw","mfe_30d_pct":1.74,"mae_30d_pct":-3.73,"mfe_90d_pct":32.34,"mae_90d_pct":-3.73,"mfe_180d_pct":32.34,"mae_180d_pct":-3.73,"forward_high_30d":2045,"forward_low_30d":1935,"forward_high_90d":2660,"forward_low_90d":1935,"forward_high_180d":2660,"forward_low_180d":1935,"calibration_usable":true,"case_role":"delayed_positive_control","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|014790|Stage2-Watch|2024-03-27","route":"DelayedLocal4B_NotImmediateStage2","guardrail_lesson":"low 30D MFE but strong 90D MFE should not be backfilled as immediate success; route as delayed 4B if refinancing/liquidity bridge refreshes"}
```

---

## 4. Case analysis

### 4.1 DB Insurance / 005830 — low-MAE positive-control

DB Insurance is the clean positive-control. It produced meaningful MFE with low MAE. That makes it a guardrail against over-punishing financial/insurance signals.

```yaml
entry_close: 95000
90d_high: 120700
90d_low: 86200
180d_high: 124000
180d_low: 86200
route: KeepStage2_BlockHard4C
```

The nonlife reserve/loss-ratio/capital-return bridge should survive R13 red-team.

---

### 4.2 KB Financial / 105560 — real bridge, high-ish MAE, local 4B

KB is not a low-PBR label only. It had a real C21 bank-holding capital-return bridge, but the August drawdown was meaningful.

```yaml
entry_close: 87900
90d_high: 103900
90d_low: 74000
route: Local4B_NotHard4C
```

This is the archetypal local 4B case: the bridge exists, the price later validates, but drawdown prevents Green until CET1, credit-cost and shareholder-return execution are refreshed.

---

### 4.3 Woori Financial / 316140 — weak bridge cap

Woori participated in the value-up bank trade, but the forward MFE from this entry stayed below 10%.

```yaml
entry_close: 16180
90d_high: 17100
90d_low: 13740
route: Stage2Cap
```

The model should not give every low-PBR bank equal C21 credit.

---

### 4.4 Hanwha Life / 088350 — life-insurance value-up label cap

Hanwha Life is the insurance version of weak-label risk. It had label exposure but insufficient post-trigger MFE.

```yaml
entry_close: 3060
90d_high: 3345
90d_low: 2580
route: Stage2Cap
```

The life-insurer path requires solvency, reserve, CSM and capital-policy evidence, not just value-up beta.

---

### 4.5 Taeyoung E&C / 009410 — direct workout stress-control

Taeyoung is not a clean positive or negative aggregate row. It is a stress-control. The direct workout event is real, but the price path has deep MAE and corporate-action/trading-gap caveats.

```yaml
entry_close: 3765
30d_low: 2180
180d_high: 6110
corporate_action_candidate_in_window: true
route: StressControl_ExcludeCleanAggregate
```

Direct workout is like putting a patient on life support. Survival improves; equity recovery is a different question.

---

### 4.6 Hyundai E&C / 000720 — hard block

Hyundai E&C is the clean C30 hard block. It did not produce enough MFE and later drew down deeply.

```yaml
entry_close: 33250
90d_high: 36000
180d_low: 24100
route: Stage2FalsePositiveBlock
```

Large-builder quality and PF support labels are not enough without issuer-specific refinancing, debt-service or cash-flow bridge.

---

### 4.7 HL D&I / 014790 — delayed 4B positive

HL D&I prevents over-blocking the C30 group. The 30D move was weak, but the later 90D move was strong and drawdown stayed shallow.

```yaml
entry_close: 2010
30d_high: 2045
90d_high: 2660
90d_low: 1935
route: DelayedLocal4B_NotImmediateStage2
```

This case should not be scored as immediate Stage2-Actionable. It is a delayed local 4B candidate after refinancing/liquidity/housing bridge refresh.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 6
stress_control_case_count: 1
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_control_count: 1
local_4B_or_delayed_4B_count: 2
stage2_cap_count: 2
hard_block_count: 1
current_profile_error_count: 4
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 005830 | C22 | keep Stage2 / block hard 4C | +27.05 / -9.26 | +30.53 / -9.26 | real reserve bridge with low MAE |
| 105560 | C21 | local 4B | +18.20 / -15.81 | +18.20 / -15.81 | real capital-return bridge, high-ish MAE |
| 316140 | C21 | Stage2 cap | +5.69 / -15.08 | +5.69 / -15.08 | low-PBR label without enough execution |
| 088350 | C22 | Stage2 cap | +9.31 / -15.69 | +9.31 / -15.69 | life-insurance value-up label weak |
| 009410 | C30 | stress-control only | +9.16 / -42.10 | +62.28 / -42.10 | workout is not clean equity recovery |
| 000720 | C30 | hard block | +8.27 / -6.17 | +8.27 / -27.52 | support/large-builder label failed |
| 014790 | C30 | delayed 4B | +32.34 / -3.73 | +32.34 / -3.73 | delayed positive, not immediate Stage2 |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"005830","raw_bridge_quality":4,"raw_accounting_trust":4,"raw_mfe_validation":4,"raw_mae_penalty":0,"raw_contamination_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"105560","raw_bridge_quality":4,"raw_accounting_trust":3,"raw_mfe_validation":2,"raw_mae_penalty":2,"raw_contamination_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_NotHard4C"}
{"row_type":"score_simulation","symbol":"316140","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_mfe_validation":0,"raw_mae_penalty":2,"raw_contamination_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap"}
{"row_type":"score_simulation","symbol":"088350","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_mfe_validation":0,"raw_mae_penalty":2,"raw_contamination_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap"}
{"row_type":"score_simulation","symbol":"009410","raw_bridge_quality":3,"raw_accounting_trust":0,"raw_mfe_validation":1,"raw_mae_penalty":5,"raw_contamination_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"StressControl_ExcludeCleanAggregate"}
{"row_type":"score_simulation","symbol":"000720","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":4,"raw_contamination_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"014790","raw_bridge_quality":2,"raw_accounting_trust":1,"raw_mfe_validation":3,"raw_mae_penalty":0,"raw_contamination_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The current profile can still confuse the timing and route of high-MAE cases.

```text
bad compression:
high MAE -> hard block everything
```

This would kill KB-like real bridge cases.

```text
bad reward:
high MFE -> successful trigger
```

This would overlearn Taeyoung-like workout stress or Hwashin-style blowoff paths.

### Rule candidate

```text
R13_HIGH_MAE_ROUTE_SPLIT_V4

if company_specific_accounting_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -12:
    keep_stage2_actionable_bonus = true
    block_hard_4C = true
```

```text
if company_specific_accounting_bridge == true
and MFE_90D_pct >= +10
and MAE_90D_pct <= -12:
    route = local_4B_watch
    block_stage3_green = true
    require_bridge_refresh = true
```

```text
if MFE_90D_pct < +10
and MAE_90D_pct <= -15
and company_specific_revenue_margin_cash_or_capital_bridge == false:
    route = Stage2Cap_or_FalsePositiveBlock
    stage2_actionable_bonus = 0
```

```text
if direct_workout_or_debt_restructuring == true
and equity_value_bridge == false:
    route = StressControl_ExcludeCleanAggregate
    stage2_actionable_bonus = 0
```

```text
if MFE_30D_pct < +5
and MFE_90D_pct >= +25
and MAE_90D_pct > -10:
    route = DelayedLocal4B
    do_not_backfill_as_immediate_Stage2_Actionable = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_high_MAE_guardrail_candidate
new_axis_proposed: R13_HIGH_MAE_ROUTE_SPLIT_V4
existing_axis_strengthened:
  - real_accounting_bridge_low_MAE_keep_stage2
  - real_bridge_high_MAE_local_4B_watch
  - weak_label_low_MFE_mid_MAE_stage2_cap
  - direct_workout_high_MAE_stress_control_exclude_clean_aggregate
  - delayed_4B_do_not_backfill_immediate_stage2
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_retest_with_securities_and_regional_bank_controls
C22_INSURANCE_RATE_CYCLE_RESERVE_retest_with_healthcare_GA_and_reinsurer_controls
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

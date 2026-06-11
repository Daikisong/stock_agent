# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 5
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: CONTRACT_POLICY_EQUIPMENT_NUCLEAR_HIGH_MAE_ROUTE_SPLIT_DIRECT_BRIDGE_VS_LABEL_FAILURE
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

R13 is a cross-archetype checkpoint. This run does not add a new sector-specific positive. It re-tests recent C03/C31/C04/C22 evidence through the high-MAE routing gate.

The previous local `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` run reached loop 4. This continuation is therefore `loop 5`.

---

## 1. Research thesis

High MAE is not automatically a thesis break. But it is never ignorable.

```text
headline noticed by market
→ MFE appears
→ then drawdown tests whether bridge was real, stale, missing, or misclassified
```

The route split:

```text
A. direct contract / system export chain + high MFE + low MAE
   → keep Stage2, block hard 4C

B. company-specific demand bridge + high MAE
   → local 4B, block Green until bridge refresh

C. broad policy label + weak execution bridge + deep MAE
   → hard 4C / Stage2 false-positive block

D. equipment/capex bridge + high MFE + high MAE
   → local 4B, require order/backlog/margin refresh

E. project-policy event + legal/final-contract delay + high MAE
   → Stage2 cap / local 4B until final contract cash bridge

F. adjacent business model label
   → reclassify and cap selected archetype
```

The guardrail behaves like a circuit breaker. It should not shut down a working motor because of one voltage dip, but it must cut off a wire that was never connected to the machine.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_cases: 7
  source_archetypes:
    - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
    - C22_INSURANCE_RATE_CYCLE_RESERVE
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - high-MAE routing
    - local 4B vs hard 4C split
    - Stage3-Green block conditions
    - no production scoring changes
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"DIRECT_DEFENSE_EXPORT_CONTRACT_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"012450","name":"한화에어로스페이스","trigger_type":"Stage2-Actionable","entry_date":"2024-07-10","entry_close":256500,"price_basis":"tradable_raw","mfe_30d_pct":28.65,"mae_30d_pct":-3.70,"mfe_90d_pct":42.11,"mae_90d_pct":-3.70,"mfe_180d_pct":65.69,"mae_180d_pct":-3.70,"forward_high_30d":330000,"forward_low_30d":247000,"forward_high_90d":364500,"forward_low_90d":247000,"forward_high_180d":425000,"forward_low_180d":247000,"calibration_usable":true,"case_role":"positive_control_block_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|012450|Stage2-Actionable|2024-07-10","route":"KeepStage2_BlockHard4C","guardrail_lesson":"signed export contract with delivery/backlog bridge and low MAE should not be hard-blocked"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"DEFENSE_EXPORT_SYSTEM_ADOPTION_NEAR_ZERO_MAE_POSITIVE_CONTROL","source_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"079550","name":"LIG넥스원","trigger_type":"Stage2-Actionable","entry_date":"2024-02-07","entry_close":113400,"price_basis":"tradable_raw","mfe_30d_pct":64.46,"mae_30d_pct":-0.53,"mfe_90d_pct":64.46,"mae_90d_pct":-0.53,"mfe_180d_pct":119.58,"mae_180d_pct":-0.53,"forward_high_30d":186500,"forward_low_30d":112800,"forward_high_90d":186500,"forward_low_90d":112800,"forward_high_180d":249000,"forward_low_180d":112800,"calibration_usable":true,"case_role":"positive_control","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|079550|Stage2-Actionable|2024-02-07","route":"KeepStage2_PositiveControl","guardrail_lesson":"export-system adoption chain with high MFE and near-zero MAE is a real positive control"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"HBM_REVENUE_BRIDGE_HIGH_MAE_LOCAL_4B_NOT_HARD_4C","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"000660","name":"SK하이닉스","trigger_type":"Stage2-Actionable","entry_date":"2024-05-23","entry_close":200000,"price_basis":"tradable_raw","mfe_30d_pct":21.50,"mae_30d_pct":-5.90,"mfe_90d_pct":24.25,"mae_90d_pct":-24.20,"mfe_180d_pct":24.25,"mae_180d_pct":-27.65,"forward_high_30d":243000,"forward_low_30d":188200,"forward_high_90d":248500,"forward_low_90d":151600,"forward_high_180d":248500,"forward_low_180d":144700,"calibration_usable":true,"case_role":"real_bridge_high_MAE_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|000660|Stage2-Actionable|2024-05-23","route":"Local4B_NotHard4C_CapPolicyContribution","guardrail_lesson":"HBM revenue bridge keeps Stage2 alive, but high MAE blocks Green and caps broad policy contribution"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"POLICY_LABEL_DEEP_180D_MAE_HARD_4C_BLOCK","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"005930","name":"삼성전자","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-23","entry_close":78300,"price_basis":"tradable_raw","mfe_30d_pct":5.36,"mae_30d_pct":-6.13,"mfe_90d_pct":13.41,"mae_90d_pct":-10.34,"mfe_180d_pct":13.41,"mae_180d_pct":-36.27,"forward_high_30d":82500,"forward_low_30d":73500,"forward_high_90d":88800,"forward_low_90d":70200,"forward_high_180d":88800,"forward_low_180d":49900,"calibration_usable":true,"case_role":"hard_4C_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|005930|Stage2-FalsePositive|2024-05-23","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"broad policy label without execution bridge should be hard-blocked after deep 180D MAE"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"EQUIPMENT_CAPEX_HIGH_MFE_HIGH_MAE_LOCAL_4B","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"042700","name":"한미반도체","trigger_type":"Stage2-Actionable","entry_date":"2024-05-23","entry_close":146400,"price_basis":"tradable_raw","mfe_30d_pct":34.02,"mae_30d_pct":-5.67,"mfe_90d_pct":34.02,"mae_90d_pct":-32.99,"mfe_180d_pct":34.02,"mae_180d_pct":-45.97,"forward_high_30d":196200,"forward_low_30d":138100,"forward_high_90d":196200,"forward_low_90d":98100,"forward_high_180d":196200,"forward_low_180d":79100,"calibration_usable":true,"case_role":"vertical_MFE_local_4B_watch","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|042700|Stage2-Actionable|2024-05-23","route":"Local4B_RequireOrderMarginRefresh","guardrail_lesson":"equipment/capex bridge had real MFE but high MAE blocks Green without order and margin refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"NUCLEAR_POLICY_LEGAL_DELAY_HIGH_MAE_LOCAL_4B","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage2-Watch","entry_date":"2024-07-17","entry_close":21250,"price_basis":"tradable_raw","mfe_30d_pct":17.65,"mae_30d_pct":-28.71,"mfe_90d_pct":17.65,"mae_90d_pct":-28.71,"mfe_180d_pct":17.65,"mae_180d_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"case_role":"policy_legal_delay_local_4B_watch","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|034020|Stage2-Watch|2024-07-17","route":"Local4B_BlockGreenUntilFinalContractCashBridge","guardrail_lesson":"nuclear preferred-bidder spike should not become Green while legal/final-contract and company-specific cash bridge remain unresolved"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"ADJACENT_GA_LABEL_RECLASSIFICATION_CAP","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"244920","name":"에이플러스에셋","trigger_type":"Stage2-Watch","entry_date":"2024-05-10","entry_close":4100,"price_basis":"tradable_raw","mfe_30d_pct":9.76,"mae_30d_pct":-2.32,"mfe_90d_pct":9.76,"mae_90d_pct":-13.78,"mfe_180d_pct":14.63,"mae_180d_pct":-13.78,"forward_high_30d":4500,"forward_low_30d":4005,"forward_high_90d":4500,"forward_low_90d":3535,"forward_high_180d":4700,"forward_low_180d":3535,"calibration_usable":true,"case_role":"reclassification_cap","novelty_key":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|244920|Stage2-Watch|2024-05-10","route":"Stage2Cap_Reclassify","guardrail_lesson":"GA commission economics belong to distribution commission axis, not C22 reserve-cycle Green"}
```

---

## 4. Case analysis

### 4.1 Hanwha Aerospace / 012450 — positive control against over-blocking

This row prevents the high-MAE guardrail from becoming a blunt weapon. There is high MFE, low MAE, and a signed export contract.

```text
route = KeepStage2_BlockHard4C
```

### 4.2 LIG Nex1 / 079550 — clean positive control

This is the cleanest export-system adoption control. It has extreme MFE with almost no MAE.

```text
route = KeepStage2_PositiveControl
```

### 4.3 SK Hynix / 000660 — high-MAE local 4B, not hard 4C

The HBM bridge is real. But high MAE means the model must block Green and demand HBM revenue/order refresh.

```text
route = Local4B_NotHard4C_CapPolicyContribution
```

### 4.4 Samsung Electronics / 005930 — hard 4C policy-label failure

The same policy umbrella did not protect Samsung. Execution bridge failed and the full-window drawdown was deep.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 4.5 Hanmi Semiconductor / 042700 — high-MFE equipment path, local 4B

The first rally was valid enough not to call the trigger meaningless. But the high MAE forbids Green.

```text
route = Local4B_RequireOrderMarginRefresh
```

### 4.6 Doosan Enerbility / 034020 — legal-delay high-MAE local 4B

The nuclear policy event produced a spike, but legal/final-contract delay kept the bridge incomplete.

```text
route = Local4B_BlockGreenUntilFinalContractCashBridge
```

### 4.7 A Plus Asset / 244920 — reclassification cap

This row is not mainly a high-MAE failure. It is a taxonomy failure. GA commission economics should not be treated as C22 reserve-cycle evidence.

```text
route = Stage2Cap_Reclassify
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 7
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_control_count: 2
local_4B_watch_count: 3
hard_4C_or_stage2_block_count: 1
reclassification_cap_count: 1
current_profile_error_count: 5
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 012450 | C03 | keep Stage2 / block 4C | +42.11 / -3.70 | +65.69 / -3.70 | direct signed export bridge |
| 079550 | C03 | positive control | +64.46 / -0.53 | +119.58 / -0.53 | export-system adoption chain |
| 000660 | C31 | local 4B | +24.25 / -24.20 | +24.25 / -27.65 | real HBM bridge, policy contribution capped |
| 005930 | C31 | hard 4C | +13.41 / -10.34 | +13.41 / -36.27 | policy label without execution failed |
| 042700 | C31 | local 4B | +34.02 / -32.99 | +34.02 / -45.97 | equipment bridge needs refresh |
| 034020 | C04 | local 4B | +17.65 / -28.71 | +17.65 / -28.71 | nuclear policy legal-delay spike |
| 244920 | C22 | reclassify cap | +9.76 / -13.78 | +14.63 / -13.78 | adjacent business model belongs elsewhere |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"012450","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":0,"raw_reclassification_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"079550","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":5,"raw_mae_penalty":0,"raw_reclassification_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_PositiveControl"}
{"row_type":"score_simulation","symbol":"000660","raw_bridge_quality":4,"raw_accounting_trust":3,"raw_mfe_validation":3,"raw_mae_penalty":3,"raw_reclassification_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_NotHard4C"}
{"row_type":"score_simulation","symbol":"005930","raw_bridge_quality":1,"raw_accounting_trust":0,"raw_mfe_validation":1,"raw_mae_penalty":4,"raw_reclassification_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"042700","raw_bridge_quality":3,"raw_accounting_trust":2,"raw_mfe_validation":3,"raw_mae_penalty":5,"raw_reclassification_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_RequireOrderMarginRefresh"}
{"row_type":"score_simulation","symbol":"034020","raw_bridge_quality":2,"raw_accounting_trust":1,"raw_mfe_validation":2,"raw_mae_penalty":4,"raw_reclassification_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_BlockGreenUntilFinalContractCashBridge"}
{"row_type":"score_simulation","symbol":"244920","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_mfe_validation":1,"raw_mae_penalty":2,"raw_reclassification_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_Reclassify"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The current profile can still confuse three situations:

```text
direct bridge + low MAE
real bridge + high MAE
label-only + deep MAE
```

Bad rule:

```text
if MAE high: hard block
```

This kills SK Hynix and Hanmi too early.

Bad rule:

```text
if MFE high: Green
```

This overlearns Hanmi and Doosan.

### Rule candidate

```text
R13_HIGH_MAE_ROUTE_SPLIT_V5

if direct_contract_or_direct_revenue_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_hard_4C = true
```

```text
if company_specific_bridge == true
and MFE_30D_pct >= +20
and MAE_90D_pct <= -20:
    route = local_4B_watch
    block_stage3_green = true
    require_order_margin_cash_refresh = true
```

```text
if broad_policy_or_sector_label == true
and company_specific_execution_bridge == false
and MAE_180D_pct <= -25:
    route = hard_4C_or_Stage2_FalsePositive_Block
    stage2_actionable_bonus = 0
```

```text
if policy_project_event == true
and legal_or_final_contract_delay == true
and MAE_90D_pct <= -20:
    route = local_4B_watch
    block_stage3_green_until_final_contract_cash_bridge = true
```

```text
if selected_archetype_bridge_missing == true
and bridge_belongs_to_other_axis == true:
    route = Stage2Cap_Reclassify
    block_stage3_green_for_selected_archetype = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_high_MAE_guardrail_candidate
new_axis_proposed: R13_HIGH_MAE_ROUTE_SPLIT_V5
existing_axis_strengthened:
  - direct_contract_low_MAE_keep_stage2_block_4C
  - real_bridge_high_MAE_local_4B
  - policy_label_execution_missing_hard_4C
  - nuclear_policy_legal_delay_local_4B_until_contract_cash_bridge
  - adjacent_business_model_reclassification_cap
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this file with adjacent R13 4B/4C, accounting-trust and Stage2 false-positive review files. Extract the proposed shadow rule `R13_HIGH_MAE_ROUTE_SPLIT_V5` and compare it against existing 4B/4C route logic. Preserve direct-contract positive-control escape hatches while blocking broad policy-label failures and reclassifying adjacent business-model cases.
```

---

## 10. Next research state

```yaml
completed_round: R13
completed_loop: 5
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT_retest_with_battery_and_grid_policy_controls
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_retest_with_digital_financial_and_brokerage_counterexamples
  - C22_INSURANCE_RATE_CYCLE_RESERVE_retest_with_healthcare_underwriting_controls
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
```

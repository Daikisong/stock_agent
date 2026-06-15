# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 6
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: CONTRACT_POLICY_NUCLEAR_AND_EQUIPMENT_STAGE2_ESCAPE_HATCH_VS_POLICY_LABEL_BLOCK
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

R13 is a cross-archetype checkpoint, not a new sector discovery round. This loop tests whether Stage2 should remain open or be blocked after recent C03/C31/C04 evidence.

The previous local `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW` run reached loop 5, so this continuation is `loop 6`.

---

## 1. Research thesis

A Stage2 trigger is allowed only when the event has a working shaft into listed-company economics.

```text
headline / policy / sector label
→ signed contract, delivery, order, tax credit, margin, revenue, cash, or shareholder economics
→ price path validates or rejects
```

This loop splits six routes:

1. **Signed export contract escape hatch**  
   Direct contract plus delivery/backlog bridge should survive Stage2 review.

2. **System export adoption positive-control**  
   Repeated country adoption of a defense system is not merely a label; it is a backlog chain.

3. **Policy headline with company-specific demand bridge**  
   Stage2 may remain open, but the policy contribution must be capped.

4. **Policy/subsidy label without execution bridge**  
   Stage2 should be blocked when MFE is weak and 180D MAE is deep.

5. **Equipment/capex high-MFE path**  
   Stage2 may remain local 4B, but not Green, until order/margin/cash bridge refreshes.

6. **Nuclear policy/legal-delay path**  
   A preferred-bidder policy spike cannot become Stage2-Green while final-contract and legal-delay risk remain unresolved.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_cases: 6
  source_archetypes:
    - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - Stage2 false-positive review
    - direct-bridge escape hatch preservation
    - policy-label block
    - local 4B vs Stage2 block split
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"SIGNED_DEFENSE_EXPORT_CONTRACT_STAGE2_ESCAPE_HATCH","source_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"012450","name":"한화에어로스페이스","trigger_type":"Stage2-Actionable","entry_date":"2024-07-10","entry_close":256500,"price_basis":"tradable_raw","mfe_30d_pct":28.65,"mae_30d_pct":-3.70,"mfe_90d_pct":42.11,"mae_90d_pct":-3.70,"mfe_180d_pct":65.69,"mae_180d_pct":-3.70,"forward_high_30d":330000,"forward_low_30d":247000,"forward_high_90d":364500,"forward_low_90d":247000,"forward_high_180d":425000,"forward_low_180d":247000,"calibration_usable":true,"case_role":"positive_escape_hatch","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|012450|Stage2-Actionable|2024-07-10","stage2_error":"none; signed export contract and delivery/backlog bridge validated","route":"KeepStage2_DirectContract"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"DEFENSE_EXPORT_SYSTEM_ADOPTION_STAGE2_POSITIVE_CONTROL","source_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"079550","name":"LIG넥스원","trigger_type":"Stage2-Actionable","entry_date":"2024-02-07","entry_close":113400,"price_basis":"tradable_raw","mfe_30d_pct":64.46,"mae_30d_pct":-0.53,"mfe_90d_pct":64.46,"mae_90d_pct":-0.53,"mfe_180d_pct":119.58,"mae_180d_pct":-0.53,"forward_high_30d":186500,"forward_low_30d":112800,"forward_high_90d":186500,"forward_low_90d":112800,"forward_high_180d":249000,"forward_low_180d":112800,"calibration_usable":true,"case_role":"positive_control","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|079550|Stage2-Actionable|2024-02-07","stage2_error":"none; export-system adoption chain is price-validated","route":"KeepStage2_PositiveControl"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"POLICY_HBM_DEMAND_BRIDGE_STAGE2_KEEP_WITH_CONTRIBUTION_CAP","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"000660","name":"SK하이닉스","trigger_type":"Stage2-Actionable","entry_date":"2024-05-23","entry_close":200000,"price_basis":"tradable_raw","mfe_30d_pct":21.50,"mae_30d_pct":-5.90,"mfe_90d_pct":24.25,"mae_90d_pct":-24.20,"mfe_180d_pct":24.25,"mae_180d_pct":-27.65,"forward_high_30d":243000,"forward_low_30d":188200,"forward_high_90d":248500,"forward_low_90d":151600,"forward_high_180d":248500,"forward_low_180d":144700,"calibration_usable":true,"case_role":"stage2_keep_with_contribution_cap","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|000660|Stage2-Actionable|2024-05-23","stage2_error":"policy headline alone would be over-credit; HBM revenue bridge keeps Stage2 alive but caps selected-policy contribution","route":"KeepStage2_CapPolicyContribution_Local4B"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"BROAD_POLICY_SUBSIDY_LABEL_WITHOUT_EXECUTION_STAGE2_BLOCK","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"005930","name":"삼성전자","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-23","entry_close":78300,"price_basis":"tradable_raw","mfe_30d_pct":5.36,"mae_30d_pct":-6.13,"mfe_90d_pct":13.41,"mae_90d_pct":-10.34,"mfe_180d_pct":13.41,"mae_180d_pct":-36.27,"forward_high_30d":82500,"forward_low_30d":73500,"forward_high_90d":88800,"forward_low_90d":70200,"forward_high_180d":88800,"forward_low_180d":49900,"calibration_usable":true,"case_role":"hard_false_positive","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|005930|Stage2-FalsePositive|2024-05-23","stage2_error":"broad policy/subsidy label without company-specific execution bridge failed price validation","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"EQUIPMENT_CAPEX_HIGH_MFE_NOT_STAGE3_GREEN","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"042700","name":"한미반도체","trigger_type":"Stage2-Actionable","entry_date":"2024-05-23","entry_close":146400,"price_basis":"tradable_raw","mfe_30d_pct":34.02,"mae_30d_pct":-5.67,"mfe_90d_pct":34.02,"mae_90d_pct":-32.99,"mfe_180d_pct":34.02,"mae_180d_pct":-45.97,"forward_high_30d":196200,"forward_low_30d":138100,"forward_high_90d":196200,"forward_low_90d":98100,"forward_high_180d":196200,"forward_low_180d":79100,"calibration_usable":true,"case_role":"local_4B_not_Green","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|042700|Stage2-Actionable|2024-05-23","stage2_error":"high MFE is real, but deep MAE means Stage2 must stay local 4B until order/margin bridge refreshes","route":"Local4B_NotStage3Green"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":6,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"NUCLEAR_PREFERRED_BIDDER_LEGAL_DELAY_STAGE2_CAP","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage2-Watch","entry_date":"2024-07-17","entry_close":21250,"price_basis":"tradable_raw","mfe_30d_pct":17.65,"mae_30d_pct":-28.71,"mfe_90d_pct":17.65,"mae_90d_pct":-28.71,"mfe_180d_pct":17.65,"mae_180d_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"case_role":"stage2_cap_legal_delay","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|034020|Stage2-Watch|2024-07-17","stage2_error":"preferred-bidder nuclear policy event lacks final-contract/order/margin cash bridge during validation window","route":"Stage2Cap_Local4BUntilFinalContractBridge"}
```

---

## 4. Case analysis

### 4.1 Hanwha Aerospace / 012450 — direct contract escape hatch

This is the key positive escape hatch. R13 must not block direct export contracts that have platform scope and delivery/backlog bridge.

```text
route = KeepStage2_DirectContract
```

### 4.2 LIG Nex1 / 079550 — export-system positive-control

LIG Nex1 is the cleanest Stage2-positive control in this set. The M-SAM / Cheongung-II export chain produced high MFE and nearly no MAE.

```text
route = KeepStage2_PositiveControl
```

### 4.3 SK Hynix / 000660 — policy contribution cap, not full Stage2 policy credit

The policy label alone should not get full credit. Stage2 survives because HBM demand and revenue bridge are visible, not because the policy headline alone worked.

```text
route = KeepStage2_CapPolicyContribution_Local4B
```

### 4.4 Samsung Electronics / 005930 — Stage2 false positive

Samsung is the clean hard block. The broad semiconductor policy label did not translate into validated execution or price durability.

```text
route = Stage2FalsePositiveBlock
```

### 4.5 Hanmi Semiconductor / 042700 — high MFE but not Green

The equipment/capex bridge was tradable, but the deep drawdown says Stage2 must remain local 4B.

```text
route = Local4B_NotStage3Green
```

### 4.6 Doosan Enerbility / 034020 — legal-delay cap

The Czech preferred-bidder event created MFE, but final-contract, legal appeal and company-specific economics were unresolved. This is Stage2-Watch / local 4B, not Green.

```text
route = Stage2Cap_Local4BUntilFinalContractBridge
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_escape_or_control_count: 2
stage2_keep_with_contribution_cap_count: 1
local_4B_not_green_count: 1
stage2_false_positive_count: 1
stage2_cap_legal_delay_count: 1
current_profile_error_count: 4
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 012450 | C03 | KeepStage2 | +42.11 / -3.70 | +65.69 / -3.70 | direct contract bridge survives |
| 079550 | C03 | Positive control | +64.46 / -0.53 | +119.58 / -0.53 | system export adoption validates |
| 000660 | C31 | Stage2 + cap | +24.25 / -24.20 | +24.25 / -27.65 | policy contribution capped; HBM bridge drives |
| 005930 | C31 | hard block | +13.41 / -10.34 | +13.41 / -36.27 | policy label without execution fails |
| 042700 | C31 | local 4B | +34.02 / -32.99 | +34.02 / -45.97 | high MFE not enough for Green |
| 034020 | C04 | Stage2 cap | +17.65 / -28.71 | +17.65 / -28.71 | nuclear policy event needs final-contract cash bridge |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"012450","raw_direct_bridge":5,"raw_revenue_or_margin_bridge":4,"raw_validation":4,"raw_label_only_risk":0,"raw_legal_delay_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_DirectContract"}
{"row_type":"score_simulation","symbol":"079550","raw_direct_bridge":5,"raw_revenue_or_margin_bridge":5,"raw_validation":5,"raw_label_only_risk":0,"raw_legal_delay_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_PositiveControl"}
{"row_type":"score_simulation","symbol":"000660","raw_direct_bridge":2,"raw_revenue_or_margin_bridge":5,"raw_validation":3,"raw_label_only_risk":2,"raw_legal_delay_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"KeepStage2_CapPolicyContribution_Local4B"}
{"row_type":"score_simulation","symbol":"005930","raw_direct_bridge":0,"raw_revenue_or_margin_bridge":1,"raw_validation":0,"raw_label_only_risk":5,"raw_legal_delay_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"042700","raw_direct_bridge":2,"raw_revenue_or_margin_bridge":3,"raw_validation":2,"raw_label_only_risk":2,"raw_legal_delay_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_NotStage3Green"}
{"row_type":"score_simulation","symbol":"034020","raw_direct_bridge":1,"raw_revenue_or_margin_bridge":1,"raw_validation":1,"raw_label_only_risk":3,"raw_legal_delay_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_LegalDelay"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The current profile can still open Stage2 too easily for broad policy labels:

```text
policy headline
+ famous beneficiary
+ early MFE
```

That is not enough. Stage2 is a drawbridge, not a banner. It should lower only when the event has a company-specific mechanism crossing the moat.

### Rule candidate

```text
R13_STAGE2_FALSE_POSITIVE_BRIDGE_GATE_V6

if direct_contract_or_export_system_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

```text
if broad_policy_or_subsidy_label == true
and company_specific_execution_bridge == false
and MAE_180D_pct <= -25:
    stage2_actionable_bonus = 0
    route = Stage2FalsePositiveBlock
```

```text
if broad_policy_headline == true
and company_specific_cycle_or_demand_bridge == true:
    keep_stage2_actionable_bonus = true
    cap_policy_contribution = true
    local_4B_watch = true if MAE_90D_pct <= -20
```

```text
if high_MFE_equipment_or_capex_path == true
and MAE_90D_pct <= -25
and refreshed_order_margin_cash_bridge == false:
    route = Local4B_NotStage3Green
```

```text
if project_policy_event == true
and legal_or_final_contract_delay == true:
    stage2_actionable_bonus = 0
    route = Stage2Cap_Local4BUntilFinalContractBridge
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_stage2_false_positive_guardrail_candidate
new_axis_proposed: R13_STAGE2_FALSE_POSITIVE_BRIDGE_GATE_V6
existing_axis_strengthened:
  - direct_contract_stage2_escape_hatch
  - broad_policy_label_without_execution_stage2_block
  - company_specific_demand_bridge_policy_contribution_cap
  - high_MFE_equipment_path_local_4B_not_Green
  - legal_delay_project_policy_stage2_cap
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_retest_with_digital_financial_and_brokerage_counterexamples
C22_INSURANCE_RATE_CYCLE_RESERVE_retest_with_healthcare_underwriting_controls
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
C31_POLICY_SUBSIDY_LEGISLATION_EVENT_retest_with_battery_and_grid_policy_controls
```

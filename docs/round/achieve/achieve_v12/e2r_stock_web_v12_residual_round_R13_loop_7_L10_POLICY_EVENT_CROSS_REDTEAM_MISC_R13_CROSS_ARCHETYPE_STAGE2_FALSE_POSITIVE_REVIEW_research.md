# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 7
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: POLICY_TO_CASHFLOW_STAGE2_FALSE_POSITIVE_GATE_EXPORT_CONTRACT_VS_EXPLORATION_VALUEUP_AND_SUBSIDY_LABELS
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

R13 is a cross-archetype checkpoint. This loop tests the newest C31 policy-to-cashflow cases against older C31/C03/C04 controls to decide when Stage2 should survive and when it should be blocked as a false positive.

The previous local `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW` run reached loop 6, so this continuation is `loop 7`.

---

## 1. Research thesis

A policy event can reach the stock in three different ways:

```text
A. signed contract or legally binding order
   → direct revenue bridge
   → Stage2 can survive

B. shareholder-return plan
   → real cash intention
   → Stage2 only if the operating cycle does not overwhelm it

C. exploration / subsidy / policy label
   → attention first, economics later
   → Stage2 should be capped or blocked until reserves, order scope, tax credit, margin or cashflow is confirmed
```

Stage2 is not a news-alert gate. It is a bridge gate. The gate opens only when the bridge reaches the company’s accounts.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_cases: 7
  source_archetypes:
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
    - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - Stage2 false-positive review
    - policy-to-cashflow guardrail
    - direct contract escape hatch
    - local 4B vs hard block split
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"STATE_LINKED_EXPORT_CONTRACT_DIRECT_REVENUE_STAGE2_ESCAPE_HATCH","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"064350","name":"현대로템","trigger_type":"Stage2-Actionable","entry_date":"2025-02-26","entry_close":85600,"price_basis":"tradable_raw","mfe_30d_pct":36.45,"mae_30d_pct":-8.64,"mfe_90d_pct":157.59,"mae_90d_pct":-8.64,"mfe_180d_pct":157.59,"mae_180d_pct":-8.64,"forward_high_30d":116800,"forward_low_30d":78200,"forward_high_90d":220500,"forward_low_90d":78200,"forward_high_180d":220500,"forward_low_180d":78200,"calibration_usable":true,"case_role":"positive_escape_hatch","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|064350|Stage2-Actionable|2025-02-26","stage2_error":"none; state-linked signed export contract has direct revenue bridge","route":"KeepStage2_DirectContract"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"VALUEUP_SHAREHOLDER_RETURN_REAL_CASH_BUT_CORE_CYCLE_OVERRIDES_STAGE2_CAP","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"005380","name":"현대차","trigger_type":"Stage2-Watch","entry_date":"2024-08-28","entry_close":259000,"price_basis":"tradable_raw","mfe_30d_pct":3.09,"mae_30d_pct":-14.48,"mfe_90d_pct":3.09,"mae_90d_pct":-22.78,"mfe_180d_pct":3.09,"mae_180d_pct":-32.12,"forward_high_30d":267000,"forward_low_30d":221500,"forward_high_90d":267000,"forward_low_90d":200000,"forward_high_180d":267000,"forward_low_180d":175800,"calibration_usable":true,"case_role":"policy_cash_return_cap","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|005380|Stage2-Watch|2024-08-28","stage2_error":"cash-return plan is real but core auto volume/mix/margin cycle overwhelmed price path","route":"Stage2Cap_CycleOverridesPolicy"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"EXPLORATION_POLICY_HEADLINE_HIGH_MFE_LOCAL_4B_NOT_GREEN","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"036460","name":"한국가스공사","trigger_type":"Stage2-Watch","entry_date":"2024-06-03","entry_close":38700,"price_basis":"tradable_raw","mfe_30d_pct":66.67,"mae_30d_pct":-3.49,"mfe_90d_pct":66.67,"mae_90d_pct":-5.68,"mfe_180d_pct":66.67,"mae_180d_pct":-23.51,"forward_high_30d":64500,"forward_low_30d":37350,"forward_high_90d":64500,"forward_low_90d":36500,"forward_high_180d":64500,"forward_low_180d":29600,"calibration_usable":true,"case_role":"vertical_MFE_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|036460|Stage2-Watch|2024-06-03","stage2_error":"exploration headline made real MFE but confirmed commercial reserve/cashflow bridge was absent","route":"Local4B_BlockGreenUntilCommerciality"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"BROAD_POLICY_SUBSIDY_LABEL_WITHOUT_EXECUTION_STAGE2_BLOCK","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"005930","name":"삼성전자","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-23","entry_close":78300,"price_basis":"tradable_raw","mfe_30d_pct":5.36,"mae_30d_pct":-6.13,"mfe_90d_pct":13.41,"mae_90d_pct":-10.34,"mfe_180d_pct":13.41,"mae_180d_pct":-36.27,"forward_high_30d":82500,"forward_low_30d":73500,"forward_high_90d":88800,"forward_low_90d":70200,"forward_high_180d":88800,"forward_low_180d":49900,"calibration_usable":true,"case_role":"hard_false_positive","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|005930|Stage2-FalsePositive|2024-05-23","stage2_error":"broad semiconductor policy label lacked company-specific execution bridge in the validation window","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"HBM_REVENUE_BRIDGE_POLICY_CONTRIBUTION_CAP_LOCAL_4B","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"000660","name":"SK하이닉스","trigger_type":"Stage2-Actionable","entry_date":"2024-05-23","entry_close":200000,"price_basis":"tradable_raw","mfe_30d_pct":21.50,"mae_30d_pct":-5.90,"mfe_90d_pct":24.25,"mae_90d_pct":-24.20,"mfe_180d_pct":24.25,"mae_180d_pct":-27.65,"forward_high_30d":243000,"forward_low_30d":188200,"forward_high_90d":248500,"forward_low_90d":151600,"forward_high_180d":248500,"forward_low_180d":144700,"calibration_usable":true,"case_role":"stage2_keep_with_contribution_cap","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|000660|Stage2-Actionable|2024-05-23","stage2_error":"policy label alone would over-credit; HBM revenue bridge keeps Stage2 alive but high MAE blocks Green","route":"KeepStage2_CapPolicyContribution_Local4B"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"DIRECT_DEFENSE_EXPORT_CONTRACT_STAGE2_ESCAPE_HATCH","source_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","symbol":"012450","name":"한화에어로스페이스","trigger_type":"Stage2-Actionable","entry_date":"2024-07-10","entry_close":256500,"price_basis":"tradable_raw","mfe_30d_pct":28.65,"mae_30d_pct":-3.70,"mfe_90d_pct":42.11,"mae_90d_pct":-3.70,"mfe_180d_pct":65.69,"mae_180d_pct":-3.70,"forward_high_30d":330000,"forward_low_30d":247000,"forward_high_90d":364500,"forward_low_90d":247000,"forward_high_180d":425000,"forward_low_180d":247000,"calibration_usable":true,"case_role":"direct_contract_control","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|012450|Stage2-Actionable|2024-07-10","stage2_error":"none; signed export contract and delivery/backlog bridge validated","route":"KeepStage2_DirectContract"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":7,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"NUCLEAR_PREFERRED_BIDDER_LEGAL_DELAY_STAGE2_CAP","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage2-Watch","entry_date":"2024-07-17","entry_close":21250,"price_basis":"tradable_raw","mfe_30d_pct":17.65,"mae_30d_pct":-28.71,"mfe_90d_pct":17.65,"mae_90d_pct":-28.71,"mfe_180d_pct":17.65,"mae_180d_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"case_role":"stage2_cap_legal_delay","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|034020|Stage2-Watch|2024-07-17","stage2_error":"preferred-bidder nuclear policy event lacks final-contract/order/margin cash bridge during validation window","route":"Stage2Cap_Local4BUntilFinalContractBridge"}
```

---

## 4. Case analysis

### 4.1 Hyundai Rotem / 064350 — direct state-linked contract escape hatch

This is the positive C31 control. A state-linked export event becomes Stage2-quality only when it is a signed order with direct revenue path.

```yaml
route: KeepStage2_DirectContract
mfe_90d_pct: 157.59
mae_90d_pct: -8.64
```

### 4.2 Hyundai Motor / 005380 — real shareholder return, failed trigger

Hyundai Motor is not a fake-policy case. The shareholder-return plan can be real. The problem is that price path says the operating cycle dominated the event.

```yaml
route: Stage2Cap_CycleOverridesPolicy
mfe_90d_pct: 3.09
mae_90d_pct: -22.78
```

### 4.3 Korea Gas Corporation / 036460 — exploration flare, not cashflow

Korea Gas Corporation had a huge MFE, but exploration economics were not confirmed. This should stay local 4B, not Green.

```yaml
route: Local4B_BlockGreenUntilCommerciality
mfe_90d_pct: 66.67
mae_90d_pct: -5.68
```

### 4.4 Samsung Electronics / 005930 — broad policy label block

Samsung is the policy-label hard block. A large sector beneficiary still fails if execution bridge does not validate.

```yaml
route: Stage2FalsePositiveBlock
mfe_180d_pct: 13.41
mae_180d_pct: -36.27
```

### 4.5 SK Hynix / 000660 — keep Stage2, cap policy contribution

SK Hynix survives because of HBM revenue economics, not because broad policy alone was sufficient.

```yaml
route: KeepStage2_CapPolicyContribution_Local4B
mfe_90d_pct: 24.25
mae_90d_pct: -24.20
```

### 4.6 Hanwha Aerospace / 012450 — direct contract control

Hanwha Aerospace is the non-policy control: signed contract plus delivery/backlog bridge.

```yaml
route: KeepStage2_DirectContract
mfe_90d_pct: 42.11
mae_90d_pct: -3.70
```

### 4.7 Doosan Enerbility / 034020 — preferred bidder legal-delay cap

Doosan Enerbility is the project-policy cap. Preferred bidder is not final contract economics.

```yaml
route: Stage2Cap_Local4BUntilFinalContractBridge
mfe_90d_pct: 17.65
mae_90d_pct: -28.71
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 7
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_escape_or_control_count: 2
stage2_keep_with_contribution_cap_count: 1
stage2_cap_count: 2
local_4B_not_green_count: 1
stage2_false_positive_count: 1
current_profile_error_count: 5
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 064350 | C31 | KeepStage2 | +157.59 / -8.64 | +157.59 / -8.64 | signed export order validates policy event |
| 005380 | C31 | Stage2 cap | +3.09 / -22.78 | +3.09 / -32.12 | cash return real but auto cycle dominates |
| 036460 | C31 | local 4B | +66.67 / -5.68 | +66.67 / -23.51 | exploration headline needs commerciality |
| 005930 | C31 | hard block | +13.41 / -10.34 | +13.41 / -36.27 | broad policy label failed |
| 000660 | C31 | Stage2 + cap | +24.25 / -24.20 | +24.25 / -27.65 | HBM bridge, not pure policy |
| 012450 | C03 | KeepStage2 | +42.11 / -3.70 | +65.69 / -3.70 | signed export contract bridge |
| 034020 | C04 | Stage2 cap | +17.65 / -28.71 | +17.65 / -28.71 | preferred bidder needs final contract |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"064350","raw_direct_bridge":5,"raw_company_specific_cashflow":5,"raw_validation":5,"raw_policy_label_risk":0,"raw_cycle_or_legal_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_DirectContract"}
{"row_type":"score_simulation","symbol":"005380","raw_direct_bridge":2,"raw_company_specific_cashflow":3,"raw_validation":0,"raw_policy_label_risk":2,"raw_cycle_or_legal_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_CycleOverridesPolicy"}
{"row_type":"score_simulation","symbol":"036460","raw_direct_bridge":1,"raw_company_specific_cashflow":0,"raw_validation":1,"raw_policy_label_risk":4,"raw_cycle_or_legal_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_BlockGreenUntilCommerciality"}
{"row_type":"score_simulation","symbol":"005930","raw_direct_bridge":0,"raw_company_specific_cashflow":1,"raw_validation":0,"raw_policy_label_risk":5,"raw_cycle_or_legal_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"000660","raw_direct_bridge":2,"raw_company_specific_cashflow":5,"raw_validation":3,"raw_policy_label_risk":2,"raw_cycle_or_legal_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"KeepStage2_CapPolicyContribution_Local4B"}
{"row_type":"score_simulation","symbol":"012450","raw_direct_bridge":5,"raw_company_specific_cashflow":4,"raw_validation":4,"raw_policy_label_risk":0,"raw_cycle_or_legal_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_DirectContract"}
{"row_type":"score_simulation","symbol":"034020","raw_direct_bridge":1,"raw_company_specific_cashflow":1,"raw_validation":1,"raw_policy_label_risk":3,"raw_cycle_or_legal_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_LegalDelay"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The current profile can still treat policy headlines as if they are already cashflow.

Bad pattern:

```text
policy headline + sector beneficiary = Stage2-Actionable
```

Correct pattern:

```text
policy headline + signed order / cash transfer / ROE return / confirmed economics = Stage2 candidate
policy headline + exploration potential / unresolved legal gate / cycle override = Watch or Block
```

A policy event is a key. It only matters if it fits the company’s lock.

### Rule candidate

```text
R13_STAGE2_FALSE_POSITIVE_POLICY_TO_CASHFLOW_GATE_V7

if signed_contract_or_legally_binding_cash_transfer == true
and direct_revenue_or_shareholder_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
```

```text
if policy_event_or_legislation_headline == true
and company_specific_cashflow_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if policy_event == true
and MFE_30D_pct >= +30
and confirmed_project_economics_or_cash_bridge == false:
    route = Local4B_NotStage3Green
    block_stage3_green = true
```

```text
if shareholder_return_plan == true
and cyclical_volume_margin_risk_overrides == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    policy_bonus_cap = true
    route = Stage2Cap_CycleOverridesPolicy
```

```text
if preferred_bidder_or_project_policy_event == true
and final_contract_or_order_scope_bridge == false:
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
new_axis_proposed: R13_STAGE2_FALSE_POSITIVE_POLICY_TO_CASHFLOW_GATE_V7
existing_axis_strengthened:
  - signed_contract_policy_event_stage2_escape_hatch
  - exploration_policy_headline_local_4B_until_commerciality
  - shareholder_return_policy_cap_when_margin_cycle_overrides
  - broad_policy_label_without_execution_stage2_block
  - preferred_bidder_project_policy_legal_delay_stage2_cap
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this R13 loop with C31 loop 100~101 and adjacent R13 accounting-trust/high-MAE files. Extract `R13_STAGE2_FALSE_POSITIVE_POLICY_TO_CASHFLOW_GATE_V7` as a cross-archetype shadow rule. Preserve direct signed contract / binding cash-transfer escape hatches while blocking exploration-only, broad subsidy-label, and preferred-bidder-without-final-contract paths.
```

---

## 10. Next research state

```yaml
completed_round: R13
completed_loop: 7
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

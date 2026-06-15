# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R1
selected_loop: 113
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: CZECH_NUCLEAR_PREFERRED_BIDDER_TO_FINAL_CONTRACT_CASH_BRIDGE_VS_SUPPLIER_THEME_DECAY
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

`C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` remains a thin and failure-prone archetype in the no-repeat index. The previous local C04 runs reached `loop 112`, so this continuation is `R1/C04 loop 113`.

This run deliberately does not re-prove that “nuclear policy can move stocks.” The narrower question is whether the preferred-bidder headline has a company-specific bridge into final contract, order scope, margin, and cash conversion.

---

## 1. Research thesis

C04 is the archetype for the space between policy/project headline and economically bankable project execution.

```text
nuclear policy / preferred bidder / project headline
→ final contract, legal clearance, appeals, financing, order scope
→ named listed-company equipment/service/revenue/margin bridge
→ price path validation
```

The core failure mode is that the market treats `preferred bidder` like `signed final economics`. They are not the same. A preferred-bidder headline is the door opening; a final contract is the freight entering the warehouse.

This loop splits four routes:

1. **Direct nuclear engineering / project scope but legal delay high MAE**  
   A relatively direct project beneficiary can still fail Stage2-Green if final contract and legal clearance remain unresolved.

2. **O&M/service visibility low-MAE escape hatch**  
   Names with recurring O&M/service visibility can retain Stage2 or Stage2-Watch credit even while the project has legal overhang.

3. **Supplier theme / small-cap spike decay**  
   Supplier vocabulary without named order scope should be capped or blocked.

4. **Reheated nuclear theme after legal news**  
   A second spike needs fresh contract economics; otherwise it is local 4B at most.

---

## 2. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action contaminated windows blocked by default.
```

Symbol caveats:

```yaml
034020:
  name: 두산에너빌리티
  role: nuclear policy / preferred-bidder supply-chain case
  relevant_window_after_name_change_to_doosan_enerbility: true

052690:
  name: 한전기술
  role: direct nuclear engineering-scope case
  relevant_window_after_old corporate-action candidates: true

051600:
  name: 한전KPS
  role: service/O&M visibility positive-control
  relevant_window_after old corporate-action candidates: true

457550:
  name: 우진엔텍
  role: supplier theme spike / high-MAE stress-control
  relevant_window: post-IPO 2024 tradable rows
```

External policy/legal anchor:

```text
2024-07-17: Czech government selected KHNP as preferred bidder for two Dukovany nuclear reactors.
2024-08-27: EDF and Westinghouse appealed against the Czech tender decision.
2024-10-31: Czech competition watchdog rejected EDF and Westinghouse complaints, but final contract economics remained the key bridge.
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":113,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"CZECH_PREFERRED_BIDDER_SUPPLY_CHAIN_POLICY_SPIKE_LOCAL_4B","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage2-Watch","entry_date":"2024-07-17","entry_close":21250,"price_basis":"tradable_raw","mfe_30d_pct":17.65,"mae_30d_pct":-28.71,"mfe_90d_pct":17.65,"mae_90d_pct":-28.71,"mfe_180d_pct":17.65,"mae_180d_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"case_role":"local_4B_policy_supply_chain_watch","novelty_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|034020|Stage2-Watch|2024-07-17","non_price_bridge":"Czech nuclear preferred-bidder event with supply-chain exposure but unresolved final contract/order/margin bridge","score_alignment":"Stage2-Watch only; block Green until final contract, order scope, and cash bridge refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":113,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"DIRECT_ENGINEERING_SCOPE_LEGAL_DELAY_HIGH_MAE_STAGE2_CAP","symbol":"052690","name":"한전기술","trigger_type":"Stage2-Actionable","entry_date":"2024-07-18","entry_close":82000,"price_basis":"tradable_raw","mfe_30d_pct":19.63,"mae_30d_pct":-24.88,"mfe_90d_pct":19.63,"mae_90d_pct":-24.88,"mfe_180d_pct":19.63,"mae_180d_pct":-39.94,"forward_high_30d":98100,"forward_low_30d":61600,"forward_high_90d":98100,"forward_low_90d":61600,"forward_high_180d":98100,"forward_low_180d":49250,"calibration_usable":true,"case_role":"direct_scope_counterexample","novelty_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|052690|Stage2-Actionable|2024-07-18","non_price_bridge":"Direct engineering-scope beneficiary, but preferred-bidder headline did not yet equal final contract cash bridge","score_alignment":"cap Stage2-Actionable; high MAE blocks Green until legal/final-contract bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":113,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_SERVICE_OM_SCOPE_LOW_MAE_ESCAPE_HATCH","symbol":"051600","name":"한전KPS","trigger_type":"Stage2-Actionable","entry_date":"2024-09-12","entry_close":42150,"price_basis":"tradable_raw","mfe_30d_pct":14.47,"mae_30d_pct":-4.39,"mfe_90d_pct":16.49,"mae_90d_pct":-4.39,"mfe_180d_pct":16.49,"mae_180d_pct":-9.85,"forward_high_30d":48250,"forward_low_30d":40300,"forward_high_90d":49100,"forward_low_90d":40300,"forward_high_180d":49100,"forward_low_180d":38000,"calibration_usable":true,"case_role":"positive_low_MAE_escape_hatch","novelty_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|051600|Stage2-Actionable|2024-09-12","non_price_bridge":"Nuclear service/O&M visibility; less dependent on single preferred-bidder spike","score_alignment":"keep Stage2 with Green blocked until service/order economics refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":113,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"SMALL_SUPPLIER_THEME_SPIKE_HIGH_MFE_HIGH_MAE_BLOCK","symbol":"457550","name":"우진엔텍","trigger_type":"Stage2-Watch","entry_date":"2024-07-18","entry_close":31500,"price_basis":"tradable_raw","mfe_30d_pct":32.06,"mae_30d_pct":-50.83,"mfe_90d_pct":32.06,"mae_90d_pct":-58.25,"mfe_180d_pct":32.06,"mae_180d_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":13150,"forward_high_180d":41600,"forward_low_180d":13150,"calibration_usable":true,"case_role":"supplier_theme_counterexample","novelty_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|457550|Stage2-Watch|2024-07-18","non_price_bridge":"Small supplier nuclear vocabulary and theme spike without listed-company final-contract cash bridge","score_alignment":"route to Stage2-Watch or false-positive block; do not learn price-only spike as Green"}
```

---

## 4. Case analysis

### 4.1 Doosan Enerbility / 034020 — policy spike, incomplete cash bridge

The Czech preferred-bidder decision created an immediate tradable move, but the full validation path was weak. The forward low arrived quickly and MAE stayed deep across all windows.

```yaml
entry_close: 21250
30d_high: 25000
30d_low: 15150
90d_high: 25000
90d_low: 15150
180d_high: 25000
180d_low: 15150
```

Interpretation:

```text
classification = Stage2-Watch / local 4B
```

The stock had a policy/project spark. C04 should not call it Green without final contract, scope allocation, turbine/equipment margin, and cash collection bridge.

---

### 4.2 KEPCO Engineering / 052690 — direct scope still fails without legal clearance

KEPCO Engineering is more directly tied to nuclear engineering economics than generic supplier names, but even direct scope did not prevent a high-MAE path.

```yaml
entry_close: 82000
30d_high: 98100
30d_low: 61600
90d_high: 98100
90d_low: 61600
180d_high: 98100
180d_low: 49250
```

Interpretation:

```text
classification = Stage2 cap / direct-scope counterexample
```

This is an important nuance: direct beneficiary status is not enough. C04 must wait for legal clearance and final economics.

---

### 4.3 KEPCO KPS / 051600 — service/O&M low-MAE escape hatch

KEPCO KPS acts as the positive counterweight. It did not explode, but it retained a much healthier path than small supplier spikes.

```yaml
entry_close: 42150
30d_high: 48250
30d_low: 40300
90d_high: 49100
90d_low: 40300
180d_high: 49100
180d_low: 38000
```

Interpretation:

```text
classification = Stage2-Actionable with Green blocked
```

O&M/service visibility can be a better bridge than one-day supplier vocabulary. But Green still requires clearer order/revenue/cash evidence.

---

### 4.4 Woojin Entech / 457550 — price-only supplier spike decay

Woojin Entech is the harshest counterexample. High MFE appears first, but MAE overwhelms the thesis.

```yaml
entry_close: 31500
30d_high: 41600
30d_low: 15490
90d_high: 41600
90d_low: 13150
180d_high: 41600
180d_low: 13150
```

Interpretation:

```text
classification = Stage2-Watch / false-positive block candidate
```

A supplier theme spike is a flare; without contract economics it burns out.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 1
reused_control_case_count: 3
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_or_escape_hatch_count: 1
local_4B_watch_count: 1
counterexample_or_cap_count: 3
current_profile_error_count: 3
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 034020 | policy supply-chain 4B | +17.65 / -28.71 | +17.65 / -28.71 | +17.65 / -28.71 | preferred bidder spike needs final contract cash bridge |
| 052690 | direct scope cap | +19.63 / -24.88 | +19.63 / -24.88 | +19.63 / -39.94 | direct beneficiary still fails without legal/economic closure |
| 051600 | low-MAE escape hatch | +14.47 / -4.39 | +16.49 / -4.39 | +16.49 / -9.85 | service/O&M visibility survives better |
| 457550 | supplier spike counterexample | +32.06 / -50.83 | +32.06 / -58.25 | +32.06 / -58.25 | price-only supplier theme should not become Green |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"034020","raw_project_policy_bridge":4,"raw_final_contract_bridge":1,"raw_legal_clearance":1,"raw_company_specific_cash_bridge":1,"raw_validation":1,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2-Watch-local-4B"}
{"row_type":"score_simulation","symbol":"052690","raw_project_policy_bridge":4,"raw_final_contract_bridge":1,"raw_legal_clearance":1,"raw_company_specific_cash_bridge":2,"raw_validation":1,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-cap-direct-scope-counterexample"}
{"row_type":"score_simulation","symbol":"051600","raw_project_policy_bridge":3,"raw_final_contract_bridge":2,"raw_legal_clearance":1,"raw_company_specific_cash_bridge":3,"raw_validation":3,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-low-MAE-service-escape"}
{"row_type":"score_simulation","symbol":"457550","raw_project_policy_bridge":2,"raw_final_contract_bridge":0,"raw_legal_clearance":0,"raw_company_specific_cash_bridge":0,"raw_validation":0,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-or-FalsePositiveBlock-supplier-spike"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C04 can over-reward:

```text
preferred bidder
+ nuclear supplier label
+ same-day MFE
```

That is too broad. A nuclear project has multiple gates: political selection, legal clearance, final contract, financing, scope assignment, equipment order, delivery, margin, and cash. The model should treat each gate as a lock, not assume the first key opens every door.

### Rule candidate

```text
C04_FINAL_CONTRACT_LEGAL_CLEARANCE_CASH_BRIDGE_REQUIREMENT

if C04
and preferred_bidder_or_policy_project_headline == true
and final_contract_legal_clearance_company_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C04
and direct_engineering_or_equipment_scope == true
and MAE_90D_pct <= -20
and final_contract_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C04
and service_OM_visibility == true
and MFE_90D_pct >= +10
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_order_revenue_refresh = true
```

```text
if C04
and small_supplier_theme_spike == true
and MFE_30D_pct >= +20
and MAE_90D_pct <= -30
and listed_company_contract_scope == false:
    route = Stage2_FalsePositive_Block
    do_not_learn_price_only_spike = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C04_FINAL_CONTRACT_LEGAL_CLEARANCE_CASH_BRIDGE_REQUIREMENT
existing_axis_strengthened:
  - C04_preferred_bidder_not_final_contract
  - C04_direct_scope_high_MAE_stage2_cap
  - C04_service_OM_visibility_low_MAE_escape_hatch
  - C04_small_supplier_theme_spike_false_positive_block
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C04 file with adjacent C04 loop 110~112 and R13 high-MAE/accounting-trust guardrail files. Extract `C04_FINAL_CONTRACT_LEGAL_CLEARANCE_CASH_BRIDGE_REQUIREMENT`. Implement only as a shadow-rule candidate after checking duplicate rows, corporate-action windows, and whether service/O&M visibility should remain a separate escape hatch.
```

---

## 10. Next research state

```yaml
completed_round: R1
completed_loop: 113
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT_retest_with_battery_and_grid_policy_controls
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_retest_with_digital_financial_and_brokerage_counterexamples
  - C22_INSURANCE_RATE_CYCLE_RESERVE_retest_with_healthcare_underwriting_controls
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_retest_with_final_contract_signature_or_delay_update
```

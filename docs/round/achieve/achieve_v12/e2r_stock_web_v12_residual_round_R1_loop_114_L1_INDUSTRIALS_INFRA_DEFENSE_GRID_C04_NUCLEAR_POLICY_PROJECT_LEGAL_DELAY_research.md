# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R1
selected_loop: 114
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: DUKOVANY_FINAL_CONTRACT_LEGAL_CLEARANCE_VS_PREFERRED_BIDDER_PRICE_SPIKE_BACKFILL_GUARD
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards: cache_miss_observed
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

`C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` remains Priority 0 in the current no-repeat index: 6 representative rows, still 24 rows short of the 30-row minimum. The selected archetype maps to `R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID` under the v12 scheduler.

This run is not a live nuclear-stock scan. It is a historical calibration and residual rule formalization file. Direct uncached symbol-shard fetch returned cache misses in this turn, so the file reuses stock-web-derived C04 rows already generated in the current v12 session and updates the non-price event interpretation using the Czech tender appeal / final-contract chronology. No production scoring is changed.

---

## 1. Research thesis

C04 is the gap between a nuclear policy headline and an investable company-level project bridge.

```text
preferred bidder / nuclear policy / legal clearance / final contract
→ final contract economics, legal clearance, financing, project scope, order allocation, margin and cash collection
→ price path validation
```

The hard lesson from the Czech Dukovany case is that `preferred bidder` and `final contract` are not the same evidence family.

The timeline matters:

```text
2024-07-17: preferred-bidder headline
2024-08-27: EDF / Westinghouse appeals
2024-10-31: Czech watchdog rejected or stopped appeal proceedings, but the decisions were not final and could still be appealed
2025-06-04: Czech Republic and KHNP signed the contract after a court cleared the way
```

Therefore, C04 should not backfill the 2025 contract signing into the 2024 preferred-bidder trigger. The 2024 trigger must still be scored as a policy/project event with legal-delay and final-contract risk. The later final signing can be a new evidence family only if stock-web price windows are calculated from the 2025 event date.

This loop formalizes four routes:

1. **Preferred-bidder supply-chain spike**
   - Tradable MFE can exist.
   - But Stage3-Green is blocked until final contract, order scope and cash bridge are confirmed.

2. **Direct engineering scope**
   - Even a direct nuclear engineering beneficiary can fail if legal clearance and final contract economics are not settled inside the validation window.

3. **Service / O&M visibility escape hatch**
   - Recurring service/O&M names can survive better because their bridge is less dependent on a single contract signing.

4. **Small supplier theme spike**
   - High MFE followed by deep MAE without named project economics is a false-positive or hard local-4B-to-block route.

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

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - e2r_stock_web_v12_residual_round_R1_loop_113_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
  - e2r_stock_web_v12_residual_round_R13_loop_6_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md
  - e2r_stock_web_v12_residual_round_R13_loop_5_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file formalizes the C04 legal-clearance / final-contract bridge after later non-price updates
  - exact duplicate trigger keys should not be counted again as new aggregate rows
  - no production scoring changed
```

External non-price anchor:

```yaml
2024-08-27:
  source: Reuters
  event: EDF and Westinghouse appealed against the Czech nuclear tender decision.
  interpretation: preferred-bidder headline had live legal / licensing / procurement risk.

2024-10-31:
  source: Reuters
  event: Czech watchdog rejected or stopped appeals, but decisions were not final and could still be appealed.
  interpretation: legal overhang eased but final contract was not yet cash bridge.

2025-06-04:
  source: AP
  event: Czech Republic signed the Dukovany reactor contract with KHNP after court clearance.
  interpretation: final-contract evidence family appeared after the 2024 trigger window; do not backfill into 2024 preferred-bidder rows without a separate 2025 stock-web price calculation.
```

Symbol caveats:

```yaml
034020:
  name: 두산에너빌리티
  role: nuclear policy / preferred-bidder supply-chain spike with legal-delay 4B watch
  calibration_usable: true

052690:
  name: 한전기술
  role: direct engineering-scope case, but legal/final-contract bridge incomplete at 2024 trigger
  calibration_usable: true

051600:
  name: 한전KPS
  role: service/O&M low-MAE escape hatch
  calibration_usable: true

457550:
  name: 우진엔텍
  role: small supplier theme spike and high-MAE false-positive stress row
  calibration_usable: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":114,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"PREFERRED_BIDDER_SUPPLY_CHAIN_SPIKE_LEGAL_DELAY_LOCAL_4B","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage2-Watch","entry_date":"2024-07-17","entry_close":21250,"price_basis":"tradable_raw","mfe_30d_pct":17.65,"mae_30d_pct":-28.71,"mfe_90d_pct":17.65,"mae_90d_pct":-28.71,"mfe_180d_pct":17.65,"mae_180d_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"case_role":"policy_supply_chain_local_4B_watch","novelty_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|034020|Stage2-Watch|2024-07-17","non_price_bridge":"Czech preferred-bidder supply-chain exposure, but legal/final-contract/order-scope cash bridge incomplete in 2024 trigger window","score_alignment":"Stage2-Watch only; block Green until final contract, order scope, margin and cash bridge refresh","dedupe_for_aggregate":true,"aggregate_group_role":"control","do_not_count_as_new_case":true,"reuse_reason":"C04 loop 113 row reused for final-contract backfill guard"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":114,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"DIRECT_ENGINEERING_SCOPE_WITH_LEGAL_FINAL_CONTRACT_GAP_STAGE2_CAP","symbol":"052690","name":"한전기술","trigger_type":"Stage2-Actionable","entry_date":"2024-07-18","entry_close":82000,"price_basis":"tradable_raw","mfe_30d_pct":19.63,"mae_30d_pct":-24.88,"mfe_90d_pct":19.63,"mae_90d_pct":-24.88,"mfe_180d_pct":19.63,"mae_180d_pct":-39.94,"forward_high_30d":98100,"forward_low_30d":61600,"forward_high_90d":98100,"forward_low_90d":61600,"forward_high_180d":98100,"forward_low_180d":49250,"calibration_usable":true,"case_role":"direct_scope_counterexample","novelty_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|052690|Stage2-Actionable|2024-07-18","non_price_bridge":"direct nuclear engineering exposure, but preferred-bidder headline did not yet equal final contract cash bridge","score_alignment":"cap Stage2-Actionable; high MAE blocks Green until legal clearance and final-contract economics are confirmed","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"C04 loop 113 row reused for direct-scope legal-delay guard"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":114,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_SERVICE_OM_VISIBILITY_LOW_MAE_ESCAPE_HATCH","symbol":"051600","name":"한전KPS","trigger_type":"Stage2-Actionable","entry_date":"2024-09-12","entry_close":42150,"price_basis":"tradable_raw","mfe_30d_pct":14.47,"mae_30d_pct":-4.39,"mfe_90d_pct":16.49,"mae_90d_pct":-4.39,"mfe_180d_pct":16.49,"mae_180d_pct":-9.85,"forward_high_30d":48250,"forward_low_30d":40300,"forward_high_90d":49100,"forward_low_90d":40300,"forward_high_180d":49100,"forward_low_180d":38000,"calibration_usable":true,"case_role":"positive_low_MAE_escape_hatch","novelty_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|051600|Stage2-Actionable|2024-09-12","non_price_bridge":"nuclear service/O&M visibility; less dependent on single preferred-bidder contract spike","score_alignment":"keep Stage2 with Green blocked until service/order economics refresh","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"C04 loop 113 low-MAE service control row"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R1","loop":114,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"SMALL_SUPPLIER_THEME_SPIKE_NO_CONTRACT_SCOPE_HARD_BLOCK","symbol":"457550","name":"우진엔텍","trigger_type":"Stage2-Watch","entry_date":"2024-07-18","entry_close":31500,"price_basis":"tradable_raw","mfe_30d_pct":32.06,"mae_30d_pct":-50.83,"mfe_90d_pct":32.06,"mae_90d_pct":-58.25,"mfe_180d_pct":32.06,"mae_180d_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":13150,"forward_high_180d":41600,"forward_low_180d":13150,"calibration_usable":true,"case_role":"supplier_theme_counterexample","novelty_key":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|457550|Stage2-Watch|2024-07-18","non_price_bridge":"small supplier nuclear theme spike without listed-company final-contract, order scope or cash bridge","score_alignment":"route to Stage2-Watch or false-positive block; do not learn price-only supplier spike as Green","dedupe_for_aggregate":true,"aggregate_group_role":"representative","do_not_count_as_new_case":true,"reuse_reason":"C04 loop 113 supplier stress row"}
```

---

## 4. Case analysis

### 4.1 Doosan Enerbility / 034020 — preferred-bidder spike remains local 4B

The 2025 final contract improves the long-run project story, but it does not rewrite the 2024 trigger path. In July 2024, the stock reacted to a preferred-bidder / supply-chain headline while legal and final-contract gates were still unresolved.

```yaml
entry_close: 21250
30D_MFE_MAE: +17.65 / -28.71
90D_MFE_MAE: +17.65 / -28.71
180D_MFE_MAE: +17.65 / -28.71
route: Stage2-Watch / local 4B
```

Interpretation:

```text
do_not_backfill_final_contract_to_2024_trigger = true
```

The correct C04 treatment is: tradable spike accepted, Green blocked until final contract, order allocation, margin and cash path are separately validated.

---

### 4.2 KEPCO Engineering / 052690 — direct scope is not enough without final economics

KEPCO Engineering is a stronger direct beneficiary than a generic supplier, yet the price path failed badly. This is the key C04 caution.

```yaml
entry_close: 82000
30D_MFE_MAE: +19.63 / -24.88
90D_MFE_MAE: +19.63 / -24.88
180D_MFE_MAE: +19.63 / -39.94
route: Stage2 cap / direct-scope counterexample
```

Direct scope is a bridge start, not a bridge finish. C04 should require legal clearance, final contract scope, design/engineering revenue allocation and margin.

---

### 4.3 KEPCO KPS / 051600 — O&M/service low-MAE escape hatch

KEPCO KPS is the low-MAE escape hatch. Its bridge is less dependent on one single new-build contract signing because O&M/service visibility can carry a steadier accounting path.

```yaml
entry_close: 42150
30D_MFE_MAE: +14.47 / -4.39
90D_MFE_MAE: +16.49 / -4.39
180D_MFE_MAE: +16.49 / -9.85
route: Stage2-Actionable with Green blocked
```

This row prevents the guardrail from over-blocking all nuclear-linked names.

---

### 4.4 Woojin Entech / 457550 — supplier theme spike hard warning

Woojin Entech is the price-only spike trap.

```yaml
entry_close: 31500
30D_MFE_MAE: +32.06 / -50.83
90D_MFE_MAE: +32.06 / -58.25
180D_MFE_MAE: +32.06 / -58.25
route: Stage2-Watch / false-positive block candidate
```

High MFE proves attention. It does not prove project economics.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 0
reused_control_case_count: 4
calibration_usable_case_count: 4
calibration_usable_trigger_count: 4
positive_or_escape_hatch_count: 1
local_4B_watch_count: 1
counterexample_or_cap_count: 3
current_profile_error_count: 3
duplicate_note: exact C04 novelty keys likely already represented in loop 113; use this file as rule-refinement evidence unless batch ingest finds a new key
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 034020 | policy supply-chain 4B | +17.65 / -28.71 | +17.65 / -28.71 | +17.65 / -28.71 | final contract later must not backfill preferred-bidder spike |
| 052690 | direct scope cap | +19.63 / -24.88 | +19.63 / -24.88 | +19.63 / -39.94 | direct beneficiary still needs legal/final economics |
| 051600 | O&M escape hatch | +14.47 / -4.39 | +16.49 / -4.39 | +16.49 / -9.85 | service visibility survives better |
| 457550 | supplier spike counterexample | +32.06 / -50.83 | +32.06 / -58.25 | +32.06 / -58.25 | price-only supplier spike should not become Green |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"034020","raw_project_policy_bridge":4,"raw_final_contract_bridge_at_trigger":0,"raw_legal_clearance_at_trigger":1,"raw_company_specific_cash_bridge":1,"raw_validation":1,"raw_label_only_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2Watch_Local4B_PreferredBidderNoBackfill"}
{"row_type":"score_simulation","symbol":"052690","raw_project_policy_bridge":4,"raw_final_contract_bridge_at_trigger":0,"raw_legal_clearance_at_trigger":1,"raw_company_specific_cash_bridge":2,"raw_validation":1,"raw_label_only_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_DirectScopeLegalDelay"}
{"row_type":"score_simulation","symbol":"051600","raw_project_policy_bridge":3,"raw_final_contract_bridge_at_trigger":1,"raw_legal_clearance_at_trigger":1,"raw_company_specific_cash_bridge":3,"raw_validation":3,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2Actionable_ServiceOMEscape"}
{"row_type":"score_simulation","symbol":"457550","raw_project_policy_bridge":2,"raw_final_contract_bridge_at_trigger":0,"raw_legal_clearance_at_trigger":0,"raw_company_specific_cash_bridge":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositive_SupplierSpike"}
```

---

## 7. Profile comparison

```jsonl
{"row_type":"profile_comparison","profile_id":"P0","profile_scope":"baseline_current_proxy","profile_hypothesis":"e2r_2_2_current_proxy","eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":21.20,"avg_MAE_90D_pct":-29.56,"avg_MFE_180D_pct":21.20,"avg_MAE_180D_pct":-34.18,"false_positive_rate":0.50,"local_4B_count":1,"score_return_alignment_verdict":"too_much_preferred_bidder_credit_if_final_contract_backfilled"}
{"row_type":"profile_comparison","profile_id":"P1","profile_scope":"sector_specific_candidate_profile","profile_hypothesis":"separate_preferred_bidder_from_final_contract","eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":21.20,"avg_MAE_90D_pct":-29.56,"avg_MFE_180D_pct":21.20,"avg_MAE_180D_pct":-34.18,"false_positive_rate":0.25,"local_4B_count":2,"score_return_alignment_verdict":"better_prevents_2025_final_contract_backfill_into_2024_rows"}
{"row_type":"profile_comparison","profile_id":"P2","profile_scope":"canonical_archetype_candidate_profile","profile_hypothesis":"C04_FINAL_CONTRACT_NO_BACKFILL_REQUIREMENT_V114","eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":21.20,"avg_MAE_90D_pct":-29.56,"avg_MFE_180D_pct":21.20,"avg_MAE_180D_pct":-34.18,"false_positive_rate":0.25,"local_4B_count":2,"score_return_alignment_verdict":"preferred_shadow_rule"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

C04 can still over-credit two things:

```text
preferred bidder headline
later final contract
```

The subtle error is temporal. Later evidence can validate the broad project story, but it should not retroactively erase the risk that existed at the original trigger.

A preferred-bidder event is an invitation letter. A final contract is a signed invoice path. The model should not book invoice revenue on the invitation date.

### Rule candidate

```text
C04_FINAL_CONTRACT_NO_BACKFILL_REQUIREMENT_V114

if C04
and preferred_bidder_or_policy_project_headline == true
and final_contract_legal_clearance_company_cash_bridge_at_trigger_date == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
    block_stage3_green = true
```

```text
if C04
and later_final_contract_signed == true
and later_contract_date > original_trigger_date:
    do_not_backfill_later_contract_to_original_trigger = true
    require_new_trigger_row_from_later_contract_date_with_stock_web_price_window = true
```

```text
if C04
and direct_engineering_or_equipment_scope == true
and MAE_90D_pct <= -20
and final_contract_bridge_at_trigger_date == false:
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

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_refinement_from_existing_controls
new_axis_proposed: C04_FINAL_CONTRACT_NO_BACKFILL_REQUIREMENT_V114
existing_axis_strengthened:
  - C04_preferred_bidder_not_final_contract
  - C04_later_final_contract_no_backfill_to_original_trigger
  - C04_direct_scope_high_MAE_stage2_cap
  - C04_service_OM_visibility_low_MAE_escape_hatch
  - C04_small_supplier_theme_spike_false_positive_block
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C04 loop with C04 loop 113 and adjacent R13 high-MAE/accounting-trust/Stage2-false-positive files. Extract `C04_FINAL_CONTRACT_NO_BACKFILL_REQUIREMENT_V114` as a shadow-rule candidate. Preserve O&M/service low-MAE escape hatches, cap preferred-bidder and direct-scope rows until final-contract/legal/cash bridge exists at the trigger date, and never backfill later contract signing into earlier preferred-bidder triggers. If 2025 final-contract rows are needed, compute separate stock-web windows from the 2025 contract date.
```

---

## 11. Next research state

```yaml
completed_round: R1
completed_loop: 114
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  - C22_INSURANCE_RATE_CYCLE_RESERVE
  - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

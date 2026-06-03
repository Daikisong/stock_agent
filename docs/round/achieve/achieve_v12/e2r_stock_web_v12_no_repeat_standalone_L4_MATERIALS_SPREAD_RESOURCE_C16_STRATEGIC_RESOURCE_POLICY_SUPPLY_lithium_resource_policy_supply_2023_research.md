# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C16 — Strategic resource policy supply / lithium guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_REVISION_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_lithium_resource_policy_supply_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY current coverage:
rows=7, symbols=4, date range=2019-05-20~2023-10-23, good/bad S2=2/0, 4B/4C=0/0
top covered symbols: 005290(2), 027580(2), 047400(2), 093370(1)
```

This run avoids those top-covered C16 symbols and adds 005490, 003670, and 005070.  
Each row uses a new `C16 + symbol + trigger_type + entry_date` hard key.

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
005490 POSCO홀딩스: corporate_action_candidate_count=0.
003670 포스코퓨처엠: 2023 forward window clean; corporate-action candidates are 2015-05-04 and 2021-02-03, outside the selected test window.
005070 코스모신소재: 2023 forward window clean; corporate-action candidates are old, with latest candidate 2019-11-13 outside the selected test window.
```

## 3. Research thesis

C16 should not treat strategic-resource policy as immediate earnings. It should test whether policy and resource optionality become mined, processed, contracted supply:

```text
strategic resource / lithium / critical-mineral policy attention
→ resource-development milestone
→ offtake or customer conversion
→ cost curve and capex timing
→ margin and revision bridge
→ rerating
```

The resource story is a map, not the mine. Stage2 can follow the map early, but Green should wait until the mine, contract and margin bridge begin to exist outside the investor deck.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C16_005490_POSCOHOLDINGS_20230307_LITHIUM_RESOURCE_POLICY_STAGE2 | 005490 | positive_lithium_resource_policy_stage2_success_with_later_4b | 2023-03-07 | 335000 | 764000 on 2023-07-26 | 314500 on 2023-03-20 | 30.15% | 54.33% | 128.06% | -6.12% | -47.71% |
| C16_003670_POSCOFUTUREM_20230726_LITHIUM_CATHODE_RESOURCE_PREMIUM_4B | 003670 | late_lithium_cathode_resource_premium_counterexample | 2023-07-26 | 560000 | 694000 on 2023-07-26 | 231500 on 2023-11-01 | 23.93% | 23.93% | 23.93% | -58.66% | -66.64% |
| C16_005070_COSMOAM_20230726_LITHIUM_CATHODE_SUPPLY_PRICE_PREMIUM_4B | 005070 | cathode_resource_supply_price_premium_counterexample | 2023-07-26 | 190400 | 226000 on 2023-07-26 | 133400 on 2023-11-01 | 18.7% | 18.7% | 18.7% | -29.94% | -40.97% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Strategic resource, lithium, and critical-mineral policy attention can be valid Stage2 routes when they attach to credible integrated supply-chain optionality.
- 005490 is the positive anchor: the early 2023 lithium/resource route produced a large forward MFE before the late-July price premium required risk discipline.

### Stage3 / Green
- C16 Green should require resource-development milestones, offtake/customer conversion, cost curve, capex timing, margin and revision confirmation.
- 003670 and 005070 show why downstream/cathode exposure should not be promoted to Green merely because the upstream resource narrative is hot.

### 4B
- 003670 and 005070 fill the missing C16 4B pocket. Both rows captured the July 2023 resource/cathode price premium, but the following drawdown shows that non-price resource evidence had already stopped adding enough marginal support.
- A strategic-resource story becomes dangerous when the market pays for the whole mine before the contract and cost curve arrive.

### 4C
- No hard accounting or project-cancellation break is asserted.
- The C16 break mode is resource-conversion failure: the policy and supply-chain narrative remain plausible, but resource milestones, customer offtake, input-cost pass-through, margin and revision evidence do not carry the valuation.

## 6. Raw component score breakdown

```json
{
  "C16_003670_POSCOFUTUREM_20230726_LITHIUM_CATHODE_RESOURCE_PREMIUM_4B": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 31,
    "valuation_rerating_runway": 2,
    "visibility_quality": 6
  },
  "C16_005070_COSMOAM_20230726_LITHIUM_CATHODE_SUPPLY_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 29,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C16_005490_POSCOHOLDINGS_20230307_LITHIUM_RESOURCE_POLICY_STAGE2": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 3,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 58,
    "valuation_rerating_runway": 9,
    "visibility_quality": 11
  }
}
```

## 7. Current calibrated profile stress test

Suggested C16 guard:
```text
if strategic_resource_policy_attention and credible_integrated_supply_chain_route:
    allow_stage2_actionable = true

if resource_price_premium and no incremental_resource_milestone_offtake_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and resource_or_customer_conversion_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 003670 / 2023-07-26: lithium/cathode vertical-integration premium can be over-promoted if the model does not require incremental resource milestone and revision evidence after the price run.
- 005070 / 2023-07-26: cathode/resource supply-chain price premium can become price-only when customer offtake, input-cost and margin bridge are not refreshed.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -6.12, "MAE_30D_pct": -6.12, "MAE_90D_pct": -6.12, "MFE_180D_pct": 128.06, "MFE_30D_pct": 30.15, "MFE_90D_pct": 54.33, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_005490_POSCOHOLDINGS_20230307_LITHIUM_RESOURCE_POLICY_STAGE2", "case_role": "positive_lithium_resource_policy_stage2_success_with_later_4b", "company_name": "POSCO홀딩스", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when lithium/resource policy and integrated supply-chain optionality created a credible rerating route, but Green still requires resource development milestones, offtake/customer conversion, cost curve, capex timing and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -47.71, "entry_date": "2023-03-07", "entry_price": 335000, "evidence_family": "lithium_resource_policy_supply_chain_integration_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-03-20", "low_price_180d": 314500, "peak_date": "2023-07-26", "peak_price": 764000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005490.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 3, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 11, "total": 58, "valuation_rerating_runway": 9, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C16_005490_POSCOHOLDINGS_20230307_LITHIUM_RESOURCE_POLICY_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_attention", "lithium_or_critical_mineral_supply_chain_visibility", "integrated_resource_to_customer_route"], "stage3_evidence_fields": ["resource_development_milestone_required", "offtake_or_customer_contract_conversion_required", "cost_curve_capex_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_milestone_delay", "offtake_or_customer_conversion_gap", "input_cost_margin_revision_bridge_failure"], "symbol": "005490", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv", "trigger_date": "2023-03-07", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -58.66, "MAE_30D_pct": -28.57, "MAE_90D_pct": -58.66, "MFE_180D_pct": 23.93, "MFE_30D_pct": 23.93, "MFE_90D_pct": 23.93, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_003670_POSCOFUTUREM_20230726_LITHIUM_CATHODE_RESOURCE_PREMIUM_4B", "case_role": "late_lithium_cathode_resource_premium_counterexample", "company_name": "포스코퓨처엠", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "Late lithium/cathode resource premium should route to local 4B unless incremental mine/resource milestone, contract conversion, margin and revision evidence keep expanding after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -66.64, "entry_date": "2023-07-26", "entry_price": 560000, "evidence_family": "lithium_cathode_vertical_integration_price_premium_without_incremental_resource_milestone_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-11-01", "low_price_180d": 231500, "peak_date": "2023-07-26", "peak_price": 694000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003670.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 4, "total": 31, "valuation_rerating_runway": 2, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C16_003670_POSCOFUTUREM_20230726_LITHIUM_CATHODE_RESOURCE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_attention", "lithium_or_critical_mineral_supply_chain_visibility", "integrated_resource_to_customer_route"], "stage3_evidence_fields": ["resource_development_milestone_required", "offtake_or_customer_contract_conversion_required", "cost_curve_capex_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_milestone_delay", "offtake_or_customer_conversion_gap", "input_cost_margin_revision_bridge_failure"], "symbol": "003670", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -29.94, "MAE_30D_pct": -24.84, "MAE_90D_pct": -29.94, "MFE_180D_pct": 18.7, "MFE_30D_pct": 18.7, "MFE_90D_pct": 18.7, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_005070_COSMOAM_20230726_LITHIUM_CATHODE_SUPPLY_PRICE_PREMIUM_4B", "case_role": "cathode_resource_supply_price_premium_counterexample", "company_name": "코스모신소재", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "Cathode/resource-supply premium should route to local 4B or counterexample unless resource procurement, input-cost pass-through, customer offtake, margin and revision evidence remain visible.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -40.97, "entry_date": "2023-07-26", "entry_price": 190400, "evidence_family": "cathode_lithium_supply_chain_price_premium_without_resource_cost_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-11-01", "low_price_180d": 133400, "peak_date": "2023-07-26", "peak_price": 226000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005070.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 4, "total": 29, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C16_005070_COSMOAM_20230726_LITHIUM_CATHODE_SUPPLY_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_attention", "lithium_or_critical_mineral_supply_chain_visibility", "integrated_resource_to_customer_route"], "stage3_evidence_fields": ["resource_development_milestone_required", "offtake_or_customer_contract_conversion_required", "cost_curve_capex_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["resource_milestone_delay", "offtake_or_customer_conversion_gap", "input_cost_margin_revision_bridge_failure"], "symbol": "005070", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005070/2023.csv", "trigger_date": "2023-07-26", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "LITHIUM_RESOURCE_POLICY_SUPPLY_CHAIN_REVISION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "strategic_lithium_resource_policy_supply_new_symbols_and_4b_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C16 strategic-resource policy/supply rows should allow Stage2 when policy, integrated resource optionality and credible customer/offtake routes emerge early, but Stage3 Green requires resource-development milestones, offtake/customer conversion, cost curve, capex timing, margin and revision bridge; late resource price premium without incremental resource proof should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C16 + symbol + trigger_type + entry_date.
3. Add C16-specific strategic-resource / lithium / offtake / cost-curve / capex-margin guard only as a shadow candidate until more rows exist.

Candidate rule:
- C16_STAGE2_ALLOWED_ON_EARLY_RESOURCE_POLICY_INTEGRATED_SUPPLY_ROUTE
- C16_GREEN_REQUIRES_RESOURCE_MILESTONE_OFFTAKE_COST_CURVE_CAPEX_MARGIN_REVISION
- C16_LITHIUM_RESOURCE_PRICE_PREMIUM_LOCAL_4B
- C16_CATHODE_RESOURCE_STORY_WITHOUT_OFFTAKE_MARGIN_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.


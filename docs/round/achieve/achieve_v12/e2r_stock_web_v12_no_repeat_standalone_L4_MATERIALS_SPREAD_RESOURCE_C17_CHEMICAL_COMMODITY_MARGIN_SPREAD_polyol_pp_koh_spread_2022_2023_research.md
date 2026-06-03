# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C17 — Chemical commodity margin-spread guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: POLYOL_PP_KOH_SPREAD_INPUT_COST_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_polyol_pp_koh_spread_2022_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD current coverage:
rows=29, symbols=8, date range=2020-08-03~2024-07-15, good/bad S2=10/5, 4B/4C=0/0
top covered symbols: 298020(7), 011780(5), 010060(3), 011170(3), 004000(2)
```

This run avoids those top-covered C17 symbols and adds 298000, 014830, and 025000.  
Each row uses a new `C17 + symbol + trigger_type + entry_date` hard key.

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
298000 효성화학: corporate_action_candidate_count=0.
014830 유니드: selected 2023 forward window clean; corporate-action candidates are 2015-08-18 and 2022-11-28, outside selected test window.
025000 KPX케미칼: selected 2022 forward window clean; corporate-action candidate is 2006-09-29, outside selected test window.
```

## 3. Research thesis

C17 should not treat every chemical product-price move as durable margin spread. It should test whether the spread survives input costs, inventory and demand volume:

```text
chemical commodity spread attention
→ product price duration and demand volume
→ feedstock / energy input-cost pass-through
→ inventory and working-capital quality
→ gross margin and revision bridge
→ rerating or local 4B cap
```

A chemical spread is like a flame under a boiler. Price can flare quickly, but Green should ask whether the boiler pressure becomes usable steam after feedstock, energy, inventory and working capital absorb the heat.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C17_298000_HYOSUNGCHEM_20220211_PP_PROPANE_SPREAD_PREMIUM_4B | 298000 | protective_pp_propane_spread_price_premium_4b_success | 2022-02-11 | 289500 | 306000 on 2022-02-17 | 112500 on 2022-09-30 | 5.7% | 5.7% | 5.7% | -61.14% | -63.24% |
| C17_014830_UNID_20230116_KOH_CAUSTIC_SPREAD_FALSE_GREEN | 014830 | koh_caustic_potash_spread_false_green_counterexample | 2023-01-16 | 89000 | 92000 on 2023-01-17 | 51000 on 2023-08-17 | 3.37% | 3.37% | 3.37% | -42.7% | -44.57% |
| C17_025000_KPXCHEM_20220329_POLYOL_SPREAD_PRICE_PREMIUM_4B | 025000 | polyol_chemical_spread_price_premium_counterexample | 2022-03-29 | 54600 | 54900 on 2022-04-06 | 47000 on 2022-09-27 | 0.55% | 0.55% | 0.55% | -13.92% | -14.39% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as clean Stage2/Green positive. The loop is focused on a C17 4B gap.
- C17 Green should require product-price duration, demand volume, input-cost pass-through, inventory/working-capital quality, gross margin and revision confirmation.
- 014830 shows why KOH/caustic spread recovery should remain Yellow when early price confirmation is not followed by demand and margin evidence.

### 4B
- 298000 is the protective 4B anchor. The PP/propane spread narrative had very little forward upside from the trigger and then became a deep drawdown.
- 025000 is a lower-beta but still useful polyol/PU spread 4B row. The price premium did not have enough spread duration or revision follow-through.
- 014830 adds the false-Green version: a brief high after the trigger was not enough to carry 180D margin-spread risk.

### 4C
- No hard plant shutdown, covenant failure or accounting break is asserted.
- The C17 break mode is spread exhaustion: the product spread remains plausible, but feedstock/energy costs, inventory, volume and margin revisions stop supporting the price already paid.

## 6. Raw component score breakdown

```json
{
  "C17_014830_UNID_20230116_KOH_CAUSTIC_SPREAD_FALSE_GREEN": {
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "input_cost_pass_through": 4,
    "market_mispricing": 5,
    "spread_duration_quality": 5,
    "total": 31,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C17_025000_KPXCHEM_20220329_POLYOL_SPREAD_PRICE_PREMIUM_4B": {
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "input_cost_pass_through": 4,
    "market_mispricing": 4,
    "spread_duration_quality": 4,
    "total": 27,
    "valuation_rerating_runway": 1,
    "visibility_quality": 5
  },
  "C17_298000_HYOSUNGCHEM_20220211_PP_PROPANE_SPREAD_PREMIUM_4B": {
    "capital_allocation": 1,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "input_cost_pass_through": 3,
    "market_mispricing": 4,
    "spread_duration_quality": 4,
    "total": 26,
    "valuation_rerating_runway": 1,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C17 guard:
```text
if chemical_spread_price_premium and no spread_duration_input_cost_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if price_confirmation and demand_volume_or_input_cost_pass_through_fails:
    keep_stage3_yellow_or_counterexample = true

if post_peak_drawdown confirms:
    require_non_price_margin_revision_evidence_before_reentry = true
```

Residual errors:
```text
current_profile_error_count = 2
- 014830 / 2023-01-16: KOH/caustic-potash spread recovery can be over-promoted if price confirmation substitutes for demand, input-cost and margin proof.
- 025000 / 2022-03-29: polyol spread premium can look stable, but should remain local 4B without volume, raw-material pass-through and revision evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -61.14, "MAE_30D_pct": -13.3, "MAE_90D_pct": -33.33, "MFE_180D_pct": 5.7, "MFE_30D_pct": 5.7, "MFE_90D_pct": 5.7, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_298000_HYOSUNGCHEM_20220211_PP_PROPANE_SPREAD_PREMIUM_4B", "case_role": "protective_pp_propane_spread_price_premium_4b_success", "company_name": "효성화학", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2022_forward_window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful when PP/propane chemical-spread enthusiasm had already been capitalized but feedstock-cost pass-through, utilization, export volume, inventory and margin/revision evidence did not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -63.24, "entry_date": "2022-02-11", "entry_price": 289500, "evidence_family": "pp_propane_chemical_spread_price_premium_without_feedstock_volume_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "POLYOL_PP_KOH_SPREAD_INPUT_COST_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-09-30", "low_price_180d": 112500, "peak_date": "2022-02-17", "peak_price": 306000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/298/298000.json", "raw_component_score_breakdown": {"capital_allocation": 1, "eps_fcf_explosion": 5, "information_confidence": 3, "input_cost_pass_through": 3, "market_mispricing": 4, "spread_duration_quality": 4, "total": 26, "valuation_rerating_runway": 1, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C17_298000_HYOSUNGCHEM_20220211_PP_PROPANE_SPREAD_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_spread_attention", "product_price_duration_or_volume_signal", "input_cost_pass_through_margin_revision_route"], "stage3_evidence_fields": ["spread_duration_and_demand_volume_required", "feedstock_energy_input_cost_pass_through_required", "inventory_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["chemical_spread_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "feedstock_energy_cost_or_inventory_pressure", "margin_revision_bridge_failure"], "symbol": "298000", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298000/2022.csv", "trigger_date": "2022-02-11", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -42.7, "MAE_30D_pct": -11.35, "MAE_90D_pct": -20.34, "MFE_180D_pct": 3.37, "MFE_30D_pct": 3.37, "MFE_90D_pct": 3.37, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_014830_UNID_20230116_KOH_CAUSTIC_SPREAD_FALSE_GREEN", "case_role": "koh_caustic_potash_spread_false_green_counterexample", "company_name": "유니드", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidates are 2015-08-18 and 2022-11-28, outside selected test window", "current_profile_error": true, "current_profile_verdict": "KOH/caustic-potash spread recovery should stay Yellow if demand, energy/feedstock cost, export volume, inventory and margin/revision evidence do not keep improving after price confirmation.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.57, "entry_date": "2023-01-16", "entry_price": 89000, "evidence_family": "koh_caustic_potash_spread_price_confirmation_without_demand_feedstock_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "POLYOL_PP_KOH_SPREAD_INPUT_COST_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-08-17", "low_price_180d": 51000, "peak_date": "2023-01-17", "peak_price": 92000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/014/014830.json", "raw_component_score_breakdown": {"capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "input_cost_pass_through": 4, "market_mispricing": 5, "spread_duration_quality": 5, "total": 31, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C17_014830_UNID_20230116_KOH_CAUSTIC_SPREAD_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_spread_attention", "product_price_duration_or_volume_signal", "input_cost_pass_through_margin_revision_route"], "stage3_evidence_fields": ["spread_duration_and_demand_volume_required", "feedstock_energy_input_cost_pass_through_required", "inventory_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["chemical_spread_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "feedstock_energy_cost_or_inventory_pressure", "margin_revision_bridge_failure"], "symbol": "014830", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014830/2023.csv", "trigger_date": "2023-01-16", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -13.92, "MAE_30D_pct": -2.56, "MAE_90D_pct": -13.1, "MFE_180D_pct": 0.55, "MFE_30D_pct": 0.55, "MFE_90D_pct": 0.55, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_025000_KPXCHEM_20220329_POLYOL_SPREAD_PRICE_PREMIUM_4B", "case_role": "polyol_chemical_spread_price_premium_counterexample", "company_name": "KPX케미칼", "corporate_action_window_status": "clean_2022_forward_window; corporate-action candidate is 2006-09-29 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Polyol/PU chemical-spread price premium should route to local 4B or counterexample unless product-price duration, raw-material pass-through, volume, inventory and margin/revision evidence continue improving after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -14.39, "entry_date": "2022-03-29", "entry_price": 54600, "evidence_family": "polyol_pu_chemical_spread_price_premium_without_volume_inputcost_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "POLYOL_PP_KOH_SPREAD_INPUT_COST_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-09-27", "low_price_180d": 47000, "peak_date": "2022-04-06", "peak_price": 54900, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/025/025000.json", "raw_component_score_breakdown": {"capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "input_cost_pass_through": 4, "market_mispricing": 4, "spread_duration_quality": 4, "total": 27, "valuation_rerating_runway": 1, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C17_025000_KPXCHEM_20220329_POLYOL_SPREAD_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_spread_attention", "product_price_duration_or_volume_signal", "input_cost_pass_through_margin_revision_route"], "stage3_evidence_fields": ["spread_duration_and_demand_volume_required", "feedstock_energy_input_cost_pass_through_required", "inventory_working_capital_margin_revision_bridge_required"], "stage4b_evidence_fields": ["chemical_spread_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "feedstock_energy_cost_or_inventory_pressure", "margin_revision_bridge_failure"], "symbol": "025000", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025000/2022.csv", "trigger_date": "2022-03-29", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "POLYOL_PP_KOH_SPREAD_INPUT_COST_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "chemical_commodity_margin_spread_pp_polyol_koh_4b_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C17 chemical commodity margin-spread rows should block Green when product-price spread lacks demand volume, input-cost pass-through, inventory/working-capital quality and margin/revision confirmation; chemical-spread price premium without duration proof should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C17 + symbol + trigger_type + entry_date.
3. Add C17-specific chemical-spread / input-cost / inventory / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C17_BLOCK_GREEN_WITHOUT_SPREAD_DURATION_INPUT_COST_MARGIN_REVISION
- C17_CHEMICAL_SPREAD_PRICE_PREMIUM_LOCAL_4B
- C17_REQUIRE_DEMAND_VOLUME_INVENTORY_WORKING_CAPITAL_BRIDGE
- C17_PRICE_CONFIRMATION_WITHOUT_MARGIN_REVISION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.


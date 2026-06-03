# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C15 — Material spread supercycle guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: RESOURCE_TRADING_STEELPIPE_FERTILIZER_SPREAD_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_resource_trading_steelpipe_fertilizer_spread_2022_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C15_MATERIAL_SPREAD_SUPERCYCLE current coverage:
rows=10, symbols=7, date range=2020-08-10~2024-05-21, good/bad S2=4/0, 4B/4C=0/0
top covered symbols: 006260(2), 011170(2), 103140(2), 006650(1), 011780(1)
```

This run avoids those top-covered C15 symbols and adds 001120, 003030, and 025860.  
Each row uses a new `C15 + symbol + trigger_type + entry_date` hard key.

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
001120 LX인터내셔널: 2022 forward window clean; corporate-action candidates are 1996/1999/2006 and outside selected test window.
003030 세아제강지주: 2022 forward window clean; corporate-action candidates are 2001/2018/2019 and outside selected test window.
025860 남해화학: 2022 forward window clean; corporate-action candidates are 1999/2000/2002 and outside selected test window.
```

## 3. Research thesis

C15 should not treat every raw-material price rise as a durable supercycle EPS event. It should test whether spread expansion survives through volume, costs, inventory and working capital:

```text
material/resource spread attention
→ product price versus input-cost spread
→ export volume, order backlog or trading margin
→ freight, FX, inventory and working-capital quality
→ margin and revision bridge
→ rerating
```

A spread is a tide. Stage2 can follow the first rising waterline, but Green should require the ship to actually float after input costs, inventory and working capital are loaded.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C15_001120_LXINTL_20220211_COAL_TRADING_SPREAD_STAGE2 | 001120 | positive_resource_trading_coal_spread_stage2_success_with_later_4b | 2022-02-11 | 27750 | 49650 on 2022-09-15 | 26500 on 2022-02-18 | 28.65% | 53.15% | 78.92% | -4.5% | -24.77% |
| C15_003030_SEAHHOLDINGS_20220225_STEELPIPE_OCTG_SPREAD_STAGE2 | 003030 | positive_steelpipe_octg_spread_stage2_success_with_later_4b | 2022-02-25 | 127000 | 203000 on 2022-08-26 | 113000 on 2022-03-17 | 16.54% | 31.89% | 59.84% | -11.02% | -36.45% |
| C15_025860_NAMHAE_20220419_FERTILIZER_SPREAD_PRICE_PREMIUM_4B | 025860 | fertilizer_input_spread_price_premium_counterexample | 2022-04-19 | 16450 | 17000 on 2022-04-19 | 9000 on 2022-07-04 | 3.34% | 3.34% | 3.34% | -45.29% | -47.06% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Material spread supercycle signals can be valid Stage2 routes when product/resource spread expansion is tied to export volume, trading margin, or order backlog before valuation fully prices the cycle.
- 001120 is the resource-trading anchor: coal/resource spread and trading-margin visibility produced a large forward MFE before the September 2022 premium required risk control.
- 003030 is the steel-pipe/OCTG anchor: export spread and energy-infrastructure demand produced a strong rerating before the August 2022 blowoff.

### Stage3 / Green
- C15 Green should require spread duration, volume, product mix, input-cost pass-through, inventory/working-capital quality, margin and revision confirmation.
- A commodity price headline alone is not enough. The model should ask whether the company captures the spread after raw materials, freight, FX and inventory timing are paid.

### 4B
- 025860 fills the missing local 4B pocket. Fertilizer/agri-input price strength had already been capitalized by April 2022; without renewed pass-through and revision proof, the forward path became a deep drawdown.
- 001120 and 003030 also show the same transition: valid Stage2 spread evidence can later become a fully priced supercycle premium.

### 4C
- No hard accounting, reserve, or plant break is asserted.
- The C15 break mode is spread mean reversion: the commodity story may remain true, but product-price duration, input cost, inventory, working capital and revisions stop supporting the price already paid.

## 6. Raw component score breakdown

```json
{
  "C15_001120_LXINTL_20220211_COAL_TRADING_SPREAD_STAGE2": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 3,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 52,
    "valuation_rerating_runway": 8,
    "visibility_quality": 10
  },
  "C15_003030_SEAHHOLDINGS_20220225_STEELPIPE_OCTG_SPREAD_STAGE2": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 3,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 55,
    "valuation_rerating_runway": 9,
    "visibility_quality": 10
  },
  "C15_025860_NAMHAE_20220419_FERTILIZER_SPREAD_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 23,
    "valuation_rerating_runway": 1,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C15 guard:
```text
if material_spread_attention and volume_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if material_spread_price_premium and no spread_duration_input_cost_working_capital_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and spread_or_inventory_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual error:
```text
current_profile_error_count = 1
- 025860 / 2022-04-19: fertilizer/agri-input spread premium can be over-promoted if the model treats price heat as input-cost pass-through, inventory quality and revision proof.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -4.5, "MAE_30D_pct": -4.5, "MAE_90D_pct": -4.5, "MFE_180D_pct": 78.92, "MFE_30D_pct": 28.65, "MFE_90D_pct": 53.15, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_001120_LXINTL_20220211_COAL_TRADING_SPREAD_STAGE2", "case_role": "positive_resource_trading_coal_spread_stage2_success_with_later_4b", "company_name": "LX인터내셔널", "corporate_action_window_status": "clean_2022_forward_window; corporate-action candidates are 1996-01-03, 1999-07-19, 1999-12-24, 2006-12-01, all outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when coal/resource trading spread expansion and trading-margin visibility created a real earnings-revision route. Green still requires commodity-price duration, trading volume, freight/FX bridge, counterparty quality, working-capital and revision confirmation; after the September 2022 premium the same evidence required 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -24.77, "entry_date": "2022-02-11", "entry_price": 27750, "evidence_family": "coal_resource_trading_spread_export_margin_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "RESOURCE_TRADING_STEELPIPE_FERTILIZER_SPREAD_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-02-18", "low_price_180d": 26500, "peak_date": "2022-09-15", "peak_price": 49650, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/001/001120.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 3, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 52, "valuation_rerating_runway": 8, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C15_001120_LXINTL_20220211_COAL_TRADING_SPREAD_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["material_commodity_spread_attention", "export_or_resource_trading_margin_visibility", "product_price_input_cost_revision_route"], "stage3_evidence_fields": ["spread_duration_and_volume_required", "input_cost_pass_through_and_working_capital_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["material_spread_supercycle_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["commodity_spread_mean_reversion", "input_cost_inventory_or_working_capital_pressure", "margin_revision_bridge_failure"], "symbol": "001120", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001120/2022.csv", "trigger_date": "2022-02-11", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -11.02, "MAE_30D_pct": -11.02, "MAE_90D_pct": -11.02, "MFE_180D_pct": 59.84, "MFE_30D_pct": 16.54, "MFE_90D_pct": 31.89, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_003030_SEAHHOLDINGS_20220225_STEELPIPE_OCTG_SPREAD_STAGE2", "case_role": "positive_steelpipe_octg_spread_stage2_success_with_later_4b", "company_name": "세아제강지주", "corporate_action_window_status": "clean_2022_forward_window; corporate-action candidates are 2001-07-30, 2018-10-05, 2019-01-16, all outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when steel pipe/OCTG export spread and energy-infrastructure order visibility created margin leverage before the valuation fully capitalized the cycle. Green still requires order backlog quality, export ASP, steel input-cost pass-through, working-capital and revision bridge; after the August 2022 blowoff, the same evidence needed 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -36.45, "entry_date": "2022-02-25", "entry_price": 127000, "evidence_family": "steel_pipe_octg_energy_infrastructure_export_spread_margin_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "RESOURCE_TRADING_STEELPIPE_FERTILIZER_SPREAD_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-03-17", "low_price_180d": 113000, "peak_date": "2022-08-26", "peak_price": 203000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003030.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 3, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 10, "total": 55, "valuation_rerating_runway": 9, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C15_003030_SEAHHOLDINGS_20220225_STEELPIPE_OCTG_SPREAD_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["material_commodity_spread_attention", "export_or_resource_trading_margin_visibility", "product_price_input_cost_revision_route"], "stage3_evidence_fields": ["spread_duration_and_volume_required", "input_cost_pass_through_and_working_capital_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["material_spread_supercycle_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["commodity_spread_mean_reversion", "input_cost_inventory_or_working_capital_pressure", "margin_revision_bridge_failure"], "symbol": "003030", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003030/2022.csv", "trigger_date": "2022-02-25", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -45.29, "MAE_30D_pct": -26.44, "MAE_90D_pct": -45.29, "MFE_180D_pct": 3.34, "MFE_30D_pct": 3.34, "MFE_90D_pct": 3.34, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_025860_NAMHAE_20220419_FERTILIZER_SPREAD_PRICE_PREMIUM_4B", "case_role": "fertilizer_input_spread_price_premium_counterexample", "company_name": "남해화학", "corporate_action_window_status": "clean_2022_forward_window; corporate-action candidates are 1999-09-28, 2000-01-21, 2000-05-02, 2002-10-07, all outside selected test window", "current_profile_error": true, "current_profile_verdict": "Fertilizer/agri-input spread premium should route to local 4B or counterexample unless raw-material cost pass-through, product-price duration, inventory quality, volume and margin/revision evidence keep expanding after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -47.06, "entry_date": "2022-04-19", "entry_price": 16450, "evidence_family": "fertilizer_potash_urea_spread_price_premium_without_input_cost_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "RESOURCE_TRADING_STEELPIPE_FERTILIZER_SPREAD_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-07-04", "low_price_180d": 9000, "peak_date": "2022-04-19", "peak_price": 17000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/025/025860.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 23, "valuation_rerating_runway": 1, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C15_025860_NAMHAE_20220419_FERTILIZER_SPREAD_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["material_commodity_spread_attention", "export_or_resource_trading_margin_visibility", "product_price_input_cost_revision_route"], "stage3_evidence_fields": ["spread_duration_and_volume_required", "input_cost_pass_through_and_working_capital_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["material_spread_supercycle_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["commodity_spread_mean_reversion", "input_cost_inventory_or_working_capital_pressure", "margin_revision_bridge_failure"], "symbol": "025860", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025860/2022.csv", "trigger_date": "2022-04-19", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "RESOURCE_TRADING_STEELPIPE_FERTILIZER_SPREAD_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "material_spread_supercycle_resource_trading_steelpipe_fertilizer_new_symbols_and_4b_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C15 material-spread supercycle rows should allow Stage2 when product/resource spread expansion is tied to export volume, trading margin, order backlog and revision visibility, but Stage3 Green requires spread duration, input-cost pass-through, inventory/working-capital quality, margin and revision bridge; material-spread price premium without duration and margin proof should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C15 + symbol + trigger_type + entry_date.
3. Add C15-specific material-spread / volume / input-cost / working-capital / 4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C15_STAGE2_ALLOWED_ON_SPREAD_VOLUME_MARGIN_REVISION_BRIDGE
- C15_GREEN_REQUIRES_SPREAD_DURATION_INPUT_COST_INVENTORY_WORKING_CAPITAL_REVISION
- C15_MATERIAL_SPREAD_PRICE_PREMIUM_LOCAL_4B
- C15_SPREAD_WITHOUT_INPUT_COST_PASS_THROUGH_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.


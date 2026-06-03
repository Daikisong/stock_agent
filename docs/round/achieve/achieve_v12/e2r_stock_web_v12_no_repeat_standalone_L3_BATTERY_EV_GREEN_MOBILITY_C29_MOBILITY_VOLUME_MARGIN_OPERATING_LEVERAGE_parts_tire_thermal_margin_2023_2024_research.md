# E2R V12 No-Repeat Standalone Residual Research
## R9 / L3 / C29 — Mobility volume / margin operating-leverage guard

metadata:
```text
selected_round: R9
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: MOBILITY_PARTS_TIRE_THERMAL_VOLUME_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_parts_tire_thermal_margin_2023_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE current coverage:
rows=36, symbols=15, date range=2020-08-14~2024-09-09, good/bad S2=10/7, 4B/4C=4/2
top covered symbols: 000270(10), 204320(6), 011210(5), 005380(4), 003490(1)
```

This run avoids those top-covered C29 symbols and adds 012330, 161390, and 018880.  
Each row uses a new `C29 + symbol + trigger_type + entry_date` hard key.

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
012330 현대모비스: 2024 forward window clean; corporate-action candidates are historical and outside the selected test window.
161390 한국타이어앤테크놀로지: corporate_action_candidate_count=0.
018880 한온시스템: 2024 forward window clean; historical corporate-action caveat is outside the selected test window.
```

## 3. Research thesis

C29 should not treat mobility volume as automatic margin leverage. It should test whether volume is high-quality enough to reach revisions:

```text
mobility volume / parts / tire / thermal-management attention
→ customer or channel volume durability
→ mix quality and pricing discipline
→ cost pass-through or input-cost relief
→ margin and revision bridge
→ rerating
```

Volume is the engine speed. Margin is the torque. The model should not pay for RPM alone; it should pay when volume turns the axle after costs, mix and customer schedules are absorbed.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C29_012330_MOBIS_20240201_PARTS_MIX_MARGIN_STAGE2 | 012330 | positive_mobility_parts_mix_margin_stage2_success_with_later_4b | 2024-02-01 | 219500 | 270000 on 2024-03-18 | 204000 on 2024-08-05 | 22.55% | 23.01% | 23.01% | -7.06% | -24.44% |
| C29_161390_HANKOOKTIRE_20231017_TIRE_VOLUME_RAW_MATERIAL_MARGIN_STAGE2 | 161390 | positive_tire_volume_raw_material_margin_stage2_success_with_later_4b | 2023-10-17 | 36250 | 63300 on 2024-04-16 | 35950 on 2023-10-17 | 28.83% | 45.38% | 74.62% | -0.83% | -33.41% |
| C29_018880_HANON_20240213_EV_THERMAL_VOLUME_MARGIN_FALSE_GREEN | 018880 | thermal_management_volume_margin_false_green_counterexample | 2024-02-13 | 6520 | 6590 on 2024-02-13 | 3800 on 2024-08-05 | 1.07% | 1.07% | 1.07% | -41.72% | -42.34% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Parts mix, aftermarket resilience, tire replacement demand, raw-material spread and pricing discipline can be valid Stage2 routes.
- 012330 is the large mobility-parts anchor: the February 2024 route produced a meaningful MFE, but later drawdown shows why Stage2 must mature into 4B discipline when the margin bridge stops expanding.
- 161390 is the clean tire margin anchor: volume, replacement demand and raw-material spread created a larger MFE before the April 2024 premium needed risk control.

### Stage3 / Green
- C29 Green should require volume durability, customer/channel schedule quality, cost pass-through, pricing/mix quality, operating leverage and revision confirmation.
- 018880 shows why EV thermal-management volume language should not be promoted when cost, leverage and revision evidence do not close.

### 4B
- 012330 and 161390 both required later risk control after valid Stage2 paths became priced.
- 018880 is the false-Green/Yellow guard: price confirmation was too weak and the following path argued for counterexample unless margin evidence repaired.

### 4C
- No hard accounting break is asserted.
- The C29 break mode is operating-leverage failure: volume or customer exposure may remain real, but mix, input cost, pricing, deleveraging and revisions do not support valuation.

## 6. Raw component score breakdown

```json
{
  "C29_012330_MOBIS_20240201_PARTS_MIX_MARGIN_STAGE2": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 3,
    "eps_fcf_explosion": 9,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 53,
    "valuation_rerating_runway": 8,
    "visibility_quality": 11
  },
  "C29_018880_HANON_20240213_EV_THERMAL_VOLUME_MARGIN_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 25,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C29_161390_HANKOOKTIRE_20231017_TIRE_VOLUME_RAW_MATERIAL_MARGIN_STAGE2": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 3,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 59,
    "valuation_rerating_runway": 9,
    "visibility_quality": 12
  }
}
```

## 7. Current calibrated profile stress test

Suggested C29 guard:
```text
if mobility_volume_attention and margin_mix_cost_bridge_visible:
    allow_stage2_actionable = true

if mobility_price_premium and no incremental_volume_mix_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if EV_thermal_or_parts_volume_claim and cost_deleveraging_revision_bridge_fails:
    cap_stage = Stage3-Yellow
    route_to_counterexample = true
```

Residual error:
```text
current_profile_error_count = 1
- 018880 / 2024-02-13: EV thermal-management volume recovery can be over-promoted if the model does not demand cost pass-through, deleveraging and margin revision evidence.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -7.06, "MAE_30D_pct": -5.24, "MAE_90D_pct": -5.24, "MFE_180D_pct": 23.01, "MFE_30D_pct": 22.55, "MFE_90D_pct": 23.01, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_012330_MOBIS_20240201_PARTS_MIX_MARGIN_STAGE2", "case_role": "positive_mobility_parts_mix_margin_stage2_success_with_later_4b", "company_name": "현대모비스", "corporate_action_window_status": "clean_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when parts mix, aftermarket resilience, and mobility margin normalization created a rerating route, but Green still requires volume durability, mix quality, customer/OE schedule, cost pass-through, margin and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -24.44, "entry_date": "2024-02-01", "entry_price": 219500, "evidence_family": "mobility_parts_aftermarket_mix_margin_operating_leverage_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "MOBILITY_PARTS_TIRE_THERMAL_VOLUME_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-08-05", "low_price_180d": 204000, "peak_date": "2024-03-18", "peak_price": 270000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/012/012330.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 3, "eps_fcf_explosion": 9, "information_confidence": 4, "market_mispricing": 10, "total": 53, "valuation_rerating_runway": 8, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C29_012330_MOBIS_20240201_PARTS_MIX_MARGIN_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_volume_or_parts_mix_attention", "margin_operating_leverage_signal", "customer_or_channel_volume_visibility"], "stage3_evidence_fields": ["volume_durability_required", "cost_pass_through_and_mix_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["mobility_volume_margin_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["volume_or_customer_schedule_disappointment", "input_cost_or_pricing_pressure", "margin_revision_bridge_failure"], "symbol": "012330", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv", "trigger_date": "2024-02-01", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -0.83, "MAE_30D_pct": -0.83, "MAE_90D_pct": -0.83, "MFE_180D_pct": 74.62, "MFE_30D_pct": 28.83, "MFE_90D_pct": 45.38, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_161390_HANKOOKTIRE_20231017_TIRE_VOLUME_RAW_MATERIAL_MARGIN_STAGE2", "case_role": "positive_tire_volume_raw_material_margin_stage2_success_with_later_4b", "company_name": "한국타이어앤테크놀로지", "corporate_action_window_status": "clean_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful where tire volume, replacement demand, raw-material spread and pricing discipline converged into margin leverage, but late-cycle Green still requires volume durability, channel inventory, FX/input-cost bridge and revision continuation.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -33.41, "entry_date": "2023-10-17", "entry_price": 36250, "evidence_family": "tire_volume_mix_raw_material_spread_operating_leverage_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "MOBILITY_PARTS_TIRE_THERMAL_VOLUME_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-17", "low_price_180d": 35950, "peak_date": "2024-04-16", "peak_price": 63300, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/161/161390.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 3, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 11, "total": 59, "valuation_rerating_runway": 9, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C29_161390_HANKOOKTIRE_20231017_TIRE_VOLUME_RAW_MATERIAL_MARGIN_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_volume_or_parts_mix_attention", "margin_operating_leverage_signal", "customer_or_channel_volume_visibility"], "stage3_evidence_fields": ["volume_durability_required", "cost_pass_through_and_mix_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["mobility_volume_margin_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["volume_or_customer_schedule_disappointment", "input_cost_or_pricing_pressure", "margin_revision_bridge_failure"], "symbol": "161390", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161390/2023.csv", "trigger_date": "2023-10-17", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -41.72, "MAE_30D_pct": -14.26, "MAE_90D_pct": -26.23, "MFE_180D_pct": 1.07, "MFE_30D_pct": 1.07, "MFE_90D_pct": 1.07, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_018880_HANON_20240213_EV_THERMAL_VOLUME_MARGIN_FALSE_GREEN", "case_role": "thermal_management_volume_margin_false_green_counterexample", "company_name": "한온시스템", "corporate_action_window_status": "clean_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "EV thermal-management volume recovery should stay Yellow or counterexample when customer volume, pricing, cost pass-through, deleveraging and margin/revision evidence do not close; price confirmation alone was a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -42.34, "entry_date": "2024-02-13", "entry_price": 6520, "evidence_family": "ev_thermal_management_volume_claim_without_margin_deleveraging_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "MOBILITY_PARTS_TIRE_THERMAL_VOLUME_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-08-05", "low_price_180d": 3800, "peak_date": "2024-02-13", "peak_price": 6590, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/018/018880.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 25, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C29_018880_HANON_20240213_EV_THERMAL_VOLUME_MARGIN_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_volume_or_parts_mix_attention", "margin_operating_leverage_signal", "customer_or_channel_volume_visibility"], "stage3_evidence_fields": ["volume_durability_required", "cost_pass_through_and_mix_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["mobility_volume_margin_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["volume_or_customer_schedule_disappointment", "input_cost_or_pricing_pressure", "margin_revision_bridge_failure"], "symbol": "018880", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv", "trigger_date": "2024-02-13", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "MOBILITY_PARTS_TIRE_THERMAL_VOLUME_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "mobility_volume_margin_operating_leverage_parts_tire_thermal_new_symbols",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R9",
  "shadow_rule_candidate": "C29 mobility volume/margin rows should allow Stage2 when volume durability, mix quality and cost/pass-through margin leverage are visible, but Stage3 Green requires customer/channel volume durability, cost pass-through, pricing/mix quality, margin and revision bridge; EV thermal or parts price confirmation without margin bridge should stay Yellow/local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C29 + symbol + trigger_type + entry_date.
3. Add C29-specific mobility volume / mix / margin / cost-pass-through guard only as a shadow candidate until more rows exist.

Candidate rule:
- C29_STAGE2_ALLOWED_ON_VOLUME_MIX_MARGIN_BRIDGE
- C29_GREEN_REQUIRES_VOLUME_DURABILITY_COST_PASS_THROUGH_PRICING_MIX_REVISION
- C29_MOBILITY_PRICE_PREMIUM_LOCAL_4B
- C29_THERMAL_VOLUME_WITHOUT_MARGIN_REVISION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.


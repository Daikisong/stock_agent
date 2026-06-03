# E2R V12 No-Repeat Standalone Residual Research
## R9 / L3 / C29 — Mobility volume margin operating-leverage guard

metadata:
```text
selected_round: R9
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: TIRE_EV_THERMAL_VOLUME_INPUT_COST_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_tire_volume_input_cost_margin_2023_2024_research.md
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

This run avoids those top-covered C29 symbols and adds 073240, 002350, and 018880.  
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
073240 금호타이어: 2024 forward window clean; corporate-action candidates are 2010-11-02, 2010-12-14, 2018-07-20 and outside selected test window.
002350 넥센타이어: 2023 forward window clean; profile corporate-action candidates are historical and outside selected test window.
018880 한온시스템: 2024 180D window clean; later 2025-01-09 and 2026-01-12 corporate-action candidates are outside selected 180D test window.
```

## 3. Research thesis

C29 should not treat auto/mobility volume recovery as enough by itself. It should test whether volume converts into operating margin:

```text
mobility volume recovery attention
→ OE/replacement or EV customer volume durability
→ utilization and price/mix
→ raw-material, freight, debt/capex absorption
→ operating margin and revision bridge
→ rerating or local 4B cap
```

Mobility volume is traffic. Green should not pay for traffic alone; it should ask whether tolls, fuel costs, lane utilization and maintenance bills leave actual margin.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C29_073240_KUMHOTIRE_20240125_TIRE_VOLUME_INPUTCOST_MARGIN_STAGE2 | 073240 | positive_tire_volume_input_cost_margin_stage2_success_with_later_4b | 2024-01-25 | 5900 | 6930 on 2024-06-26 | 4130 on 2024-09-09 | 16.61% | 16.61% | 17.46% | -30.0% | -40.4% |
| C29_002350_NEXENTIRE_20230515_TIRE_VOLUME_MARGIN_PRICE_PREMIUM_4B | 002350 | tire_volume_margin_price_premium_counterexample | 2023-05-15 | 9290 | 9300 on 2023-05-15 | 6930 on 2023-10-20 | 0.11% | 0.11% | 0.11% | -25.4% | -25.48% |
| C29_018880_HANON_20240213_EV_THERMAL_MARGIN_FALSE_GREEN | 018880 | ev_thermal_volume_margin_false_green_counterexample | 2024-02-13 | 6520 | 6590 on 2024-02-13 | 3800 on 2024-08-05 | 1.07% | 1.07% | 1.07% | -41.72% | -42.34% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Tire/mobility volume recovery can be a valid Stage2 route when it is backed by input-cost and freight relief, utilization and margin/revision evidence.
- 073240 is the positive anchor. The January 2024 volume-margin route produced meaningful 30D/180D MFE, but later required 4B discipline once the stock had paid for the margin recovery and evidence needed to refresh.

### Stage3 / Green
- C29 Green should require sustained OE/replacement or EV customer volume, price/mix, utilization, input-cost/freight pass-through, operating margin and revision confirmation.
- 018880 shows the false-Green guard. EV thermal-management volume/margin recovery looked plausible, but price confirmation was not enough without customer volume, utilization, debt/capex absorption and revision evidence.

### 4B
- 002350 fills the tire-volume price-premium 4B pocket. The trigger-day premium had almost no forward upside and then drew down as incremental volume and margin proof failed to expand.
- 018880 is the EV thermal-management version of the same failure: price confirmation without customer-volume and margin bridge became a large forward MAE.
- 073240 also moved from valid Stage2 into 4B watch after the positive margin story became capitalized.

### 4C
- No hard customer cancellation or bankruptcy/covenant break is asserted.
- The C29 break mode is operating-leverage disappointment: volume recovery remains plausible, but price/mix, input costs, utilization, debt/capex absorption and revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C29_002350_NEXENTIRE_20230515_TIRE_VOLUME_MARGIN_PRICE_PREMIUM_4B": {
    "information_confidence": 3,
    "input_cost_freight_tailwind": 5,
    "market_mispricing": 4,
    "operating_leverage": 5,
    "total": 27,
    "valuation_rerating_runway": 1,
    "visibility_quality": 4,
    "volume_recovery": 5
  },
  "C29_018880_HANON_20240213_EV_THERMAL_MARGIN_FALSE_GREEN": {
    "information_confidence": 3,
    "input_cost_freight_tailwind": 4,
    "market_mispricing": 5,
    "operating_leverage": 4,
    "total": 25,
    "valuation_rerating_runway": 1,
    "visibility_quality": 4,
    "volume_recovery": 4
  },
  "C29_073240_KUMHOTIRE_20240125_TIRE_VOLUME_INPUTCOST_MARGIN_STAGE2": {
    "information_confidence": 4,
    "input_cost_freight_tailwind": 9,
    "market_mispricing": 9,
    "operating_leverage": 9,
    "total": 57,
    "valuation_rerating_runway": 7,
    "visibility_quality": 9,
    "volume_recovery": 10
  }
}
```

## 7. Current calibrated profile stress test

Suggested C29 guard:
```text
if mobility_volume_recovery and input_cost_utilization_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if mobility_volume_margin_price_premium and no incremental_volume_price_mix_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and operating_leverage_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 002350 / 2023-05-15: tire volume-margin premium can be over-promoted if the model treats price heat as incremental volume, input-cost and revision proof.
- 018880 / 2024-02-13: EV thermal-management volume recovery can look like Green, but fails without customer-volume, utilization and margin bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -30.0, "MAE_30D_pct": -11.69, "MAE_90D_pct": -8.31, "MFE_180D_pct": 17.46, "MFE_30D_pct": 16.61, "MFE_90D_pct": 16.61, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_073240_KUMHOTIRE_20240125_TIRE_VOLUME_INPUTCOST_MARGIN_STAGE2", "case_role": "positive_tire_volume_input_cost_margin_stage2_success_with_later_4b", "company_name": "금호타이어", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2010-11-02, 2010-12-14, 2018-07-20 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when tire-volume recovery, raw-material/freight cost relief and operating-margin leverage were visible before the rerating was fully capitalized. Green still requires sustained OE/replacement volume, price/mix, input-cost pass-through, freight, utilization and revision bridge; after the June 2024 premium, the same evidence required 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -40.4, "entry_date": "2024-01-25", "entry_price": 5900, "evidence_family": "tire_export_volume_raw_material_cost_freight_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "TIRE_EV_THERMAL_VOLUME_INPUT_COST_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-09-09", "low_price_180d": 4130, "peak_date": "2024-06-26", "peak_price": 6930, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/073/073240.json", "raw_component_score_breakdown": {"information_confidence": 4, "input_cost_freight_tailwind": 9, "market_mispricing": 9, "operating_leverage": 9, "total": 57, "valuation_rerating_runway": 7, "visibility_quality": 9, "volume_recovery": 10}, "reuse_reason": null, "same_entry_group_id": "C29_073240_KUMHOTIRE_20240125_TIRE_VOLUME_INPUTCOST_MARGIN_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_volume_recovery_attention", "input_cost_freight_or_price_mix_signal", "utilization_operating_margin_revision_route"], "stage3_evidence_fields": ["sustained_OE_replacement_or_EV_customer_volume_required", "input_cost_freight_price_mix_pass_through_required", "utilization_operating_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["mobility_volume_margin_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_volume_or_utilization_disappointment", "input_cost_debt_capex_or_freight_pressure", "operating_margin_revision_bridge_failure"], "symbol": "073240", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv", "trigger_date": "2024-01-25", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -25.4, "MAE_30D_pct": -16.58, "MAE_90D_pct": -19.59, "MFE_180D_pct": 0.11, "MFE_30D_pct": 0.11, "MFE_90D_pct": 0.11, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_002350_NEXENTIRE_20230515_TIRE_VOLUME_MARGIN_PRICE_PREMIUM_4B", "case_role": "tire_volume_margin_price_premium_counterexample", "company_name": "넥센타이어", "corporate_action_window_status": "clean_2023_forward_window; profile corporate-action candidates are historical and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Tire-volume/margin price premium should route to local 4B or counterexample when the stock has already capitalized recovery and incremental OE/replacement volume, price/mix, input-cost and revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -25.48, "entry_date": "2023-05-15", "entry_price": 9290, "evidence_family": "tire_volume_margin_price_premium_without_incremental_volume_inputcost_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "TIRE_EV_THERMAL_VOLUME_INPUT_COST_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2023-10-20", "low_price_180d": 6930, "peak_date": "2023-05-15", "peak_price": 9300, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/002/002350.json", "raw_component_score_breakdown": {"information_confidence": 3, "input_cost_freight_tailwind": 5, "market_mispricing": 4, "operating_leverage": 5, "total": 27, "valuation_rerating_runway": 1, "visibility_quality": 4, "volume_recovery": 5}, "reuse_reason": null, "same_entry_group_id": "C29_002350_NEXENTIRE_20230515_TIRE_VOLUME_MARGIN_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_volume_recovery_attention", "input_cost_freight_or_price_mix_signal", "utilization_operating_margin_revision_route"], "stage3_evidence_fields": ["sustained_OE_replacement_or_EV_customer_volume_required", "input_cost_freight_price_mix_pass_through_required", "utilization_operating_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["mobility_volume_margin_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_volume_or_utilization_disappointment", "input_cost_debt_capex_or_freight_pressure", "operating_margin_revision_bridge_failure"], "symbol": "002350", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002350/2023.csv", "trigger_date": "2023-05-15", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -41.72, "MAE_30D_pct": -14.26, "MAE_90D_pct": -26.23, "MFE_180D_pct": 1.07, "MFE_30D_pct": 1.07, "MFE_90D_pct": 1.07, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_id": "C29_018880_HANON_20240213_EV_THERMAL_MARGIN_FALSE_GREEN", "case_role": "ev_thermal_volume_margin_false_green_counterexample", "company_name": "한온시스템", "corporate_action_window_status": "clean_2024_180D_forward_window; later 2025-01-09 and 2026-01-12 corporate-action candidates are outside selected 180D window", "current_profile_error": true, "current_profile_verdict": "EV thermal-management volume/margin recovery should stay Yellow when price confirmation is not followed by customer volume, utilization, pricing/mix, input-cost relief, debt/capex absorption and revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -42.34, "entry_date": "2024-02-13", "entry_price": 6520, "evidence_family": "ev_thermal_management_volume_margin_price_confirmation_without_customer_volume_inputcost_revision", "evidence_url_pending": false, "fine_archetype_id": "TIRE_EV_THERMAL_VOLUME_INPUT_COST_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "low_date_180d": "2024-08-05", "low_price_180d": 3800, "peak_date": "2024-02-13", "peak_price": 6590, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/018/018880.json", "raw_component_score_breakdown": {"information_confidence": 3, "input_cost_freight_tailwind": 4, "market_mispricing": 5, "operating_leverage": 4, "total": 25, "valuation_rerating_runway": 1, "visibility_quality": 4, "volume_recovery": 4}, "reuse_reason": null, "same_entry_group_id": "C29_018880_HANON_20240213_EV_THERMAL_MARGIN_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R9", "source_proxy_only": false, "stage2_evidence_fields": ["mobility_volume_recovery_attention", "input_cost_freight_or_price_mix_signal", "utilization_operating_margin_revision_route"], "stage3_evidence_fields": ["sustained_OE_replacement_or_EV_customer_volume_required", "input_cost_freight_price_mix_pass_through_required", "utilization_operating_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["mobility_volume_margin_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["customer_volume_or_utilization_disappointment", "input_cost_debt_capex_or_freight_pressure", "operating_margin_revision_bridge_failure"], "symbol": "018880", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv", "trigger_date": "2024-02-13", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "TIRE_EV_THERMAL_VOLUME_INPUT_COST_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "loop_contribution_label": "mobility_volume_margin_tire_ev_thermal_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R9",
  "shadow_rule_candidate": "C29 mobility volume-margin rows should allow Stage2 when volume recovery is backed by input-cost/freight relief, price/mix, utilization and margin/revision bridge, but Stage3 Green requires sustained OE/replacement or EV customer volume, operating leverage and revision confirmation; mobility volume-margin price premium without incremental volume or margin proof should route to local 4B or counterexample.",
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
3. Add C29-specific mobility volume / input-cost / utilization / operating-margin revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C29_STAGE2_ALLOWED_ON_VOLUME_INPUT_COST_UTILIZATION_MARGIN_REVISION_BRIDGE
- C29_GREEN_REQUIRES_SUSTAINED_VOLUME_PRICE_MIX_UTILIZATION_OPERATING_MARGIN_REVISION
- C29_VOLUME_MARGIN_PRICE_PREMIUM_LOCAL_4B
- C29_VOLUME_RECOVERY_WITHOUT_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.


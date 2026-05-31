# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C17 — Chemical commodity margin spread / alkali-silicone-petrochemical 4B guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: ALKALI_SILICONE_PETROCHEMICAL_SPREAD_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|spread_to_margin_guard|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_alkali_silicone_petrochemical_spread_4b_2024_research.md
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

This run avoids those top-covered C17 symbols and adds 014830, 002380, and 006650.  
Each row uses a new `C17 + symbol + trigger_type + entry_date` hard key:
```text
C17 + 014830 + Stage2-Actionable + 2024-01-25
C17 + 002380 + 4B-local-price-only + 2024-07-15
C17 + 006650 + Stage3-Yellow + 2024-01-25
```

## 2. Stock-Web source check

Manifest:
```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
symbol_count: 5414
active_like_symbol_count: 2868
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Selected profiles:
```text
014830 유니드: selected 2024 forward window clean; corporate-action candidate is 2022-11-28 and before selected trigger window.
002380 KCC: selected 2024 forward window clean; corporate-action candidate is 2000-04-17 and outside selected trigger window.
006650 대한유화: selected 2024 forward window clean; corporate-action candidate is 2010-07-13 and outside selected trigger window.
```

## 3. Research thesis

C17 should split **realized chemical spread discovery** from **late-cycle spread optionality already paid in price**:

```text
chemical commodity spread / product-margin recovery
→ realized spread duration and ASP/mix
→ shipment volume and customer demand
→ feedstock/input-cost pass-through
→ inventory and working-capital quality
→ gross margin and revision bridge
→ Stage2/Green or local 4B cap
```

A chemical spread is a tide through a plant. Stage2 can buy the first tide when throughput and margins are still being revised upward. Green should not keep paying for the same tide after the shoreline is crowded and the margin bridge has stopped widening.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C17_014830_UNID_20240125_ALKALI_SPREAD_STAGE2 | 014830 | positive_alkali_chemical_spread_stage2_success_with_later_4b_refresh | 2024-01-25 | 74900 | 118700 on 2024-06-11 | 59100 on 2024-11-14 | 12.15% | 58.48% | 58.48% | -21.09% | -50.21% |
| C17_002380_KCC_20240715_SILICONE_SPREAD_PREMIUM_4B | 002380 | silicone_chemical_spread_price_premium_counterexample | 2024-07-15 | 335000 | 345000 on 2024-07-17 | 224500 on 2024-11-15 | 2.99% | 2.99% | 2.99% | -32.99% | -34.93% |
| C17_006650_DAEHANPETRO_20240125_PETROCHEM_SPREAD_FALSE_GREEN | 006650 | petrochemical_spread_false_green_counterexample | 2024-01-25 | 144300 | 153800 on 2024-02-21 | 73300 on 2024-12-05 | 6.58% | 6.58% | 6.58% | -49.2% | -52.34% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- 014830 is the positive anchor. The January 2024 alkali/caustic-potash spread route produced strong 90D/180D MFE before the May-June premium required 4B refresh discipline.
- Stage2 is allowed only when spread salience maps to realized spread duration, volume/shipment bridge, ASP/input-cost pass-through and margin/revision visibility.

### Stage3 / Green
- C17 Green should require realized spread duration, volume shipment or customer demand, feedstock/input-cost pass-through, inventory quality and margin/revision confirmation.
- 006650 is the false-Green/Yellow guard: petrochemical rebound price confirmation was visible, but the spread-to-margin evidence did not refresh enough to survive the forward path.

### 4B
- 002380 fills the silicone/coating-material spread price-premium 4B pocket. The July 2024 trigger had small residual upside and then a much larger forward drawdown.
- 006650 shows the petrochemical version of the same failure: spread optionality can remain plausible while the price has already paid for too much without volume and revision proof.
- 014830 also demonstrates that valid Stage2 can become local 4B after the rerating capitalizes the chemical-spread pipeline.

### 4C
- No hard plant shutdown, inventory write-down, customer loss, or accounting break is asserted.
- The C17 break mode is spread-to-margin exhaustion: the commodity spread story may remain directionally real, but incremental spread duration, volume, input-cost and revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C17_002380_KCC_20240715_SILICONE_SPREAD_PREMIUM_4B": {
    "ASP_input_cost_bridge": 4,
    "chemical_spread_visibility": 7,
    "information_confidence": 3,
    "inventory_working_capital_quality": 3,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "realized_spread_duration": 4,
    "total": 33,
    "valuation_rerating_runway": 1,
    "volume_shipment_bridge": 4
  },
  "C17_006650_DAEHANPETRO_20240125_PETROCHEM_SPREAD_FALSE_GREEN": {
    "ASP_input_cost_bridge": 3,
    "chemical_spread_visibility": 6,
    "information_confidence": 3,
    "inventory_working_capital_quality": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "realized_spread_duration": 3,
    "total": 28,
    "valuation_rerating_runway": 1,
    "volume_shipment_bridge": 3
  },
  "C17_014830_UNID_20240125_ALKALI_SPREAD_STAGE2": {
    "ASP_input_cost_bridge": 8,
    "chemical_spread_visibility": 10,
    "information_confidence": 4,
    "inventory_working_capital_quality": 7,
    "margin_revision_bridge": 8,
    "market_mispricing": 9,
    "realized_spread_duration": 8,
    "total": 68,
    "valuation_rerating_runway": 7,
    "volume_shipment_bridge": 7
  }
}
```

## 7. Current calibrated profile stress test

Suggested C17 guard:
```text
if chemical_spread_recovery and realized_spread_volume_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if chemical_spread_price_premium and no incremental_spread_duration_volume_inputcost_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and spread_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 002380 / 2024-07-15: silicone/material spread premium can be over-promoted if price strength substitutes for realized spread duration and margin proof.
- 006650 / 2024-01-25: petrochemical spread confirmation can look like Yellow-to-Green, but fails without renewed shipment, input-cost and revision bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -21.09, "MAE_30D_pct": -8.95, "MAE_90D_pct": -7.61, "MFE_180D_pct": 58.48, "MFE_30D_pct": 12.15, "MFE_90D_pct": 58.48, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_014830_UNID_20240125_ALKALI_SPREAD_STAGE2", "case_role": "positive_alkali_chemical_spread_stage2_success_with_later_4b_refresh", "company_name": "유니드", "corporate_action_window_status": "selected 2024 forward window clean; corporate-action candidate is 2022-11-28 and before selected trigger window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when alkali/caustic-potash spread evidence, volume/ASP leverage and margin-revision optionality were visible before the rerating was fully capitalized. Green still requires realized spread duration, volume shipment, input-cost bridge, inventory/working-capital quality and revision confirmation; after the May-June 2024 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -50.21, "entry_date": "2024-01-25", "entry_price": 74900, "evidence_family": "alkali_caustic_potash_spread_volume_ASP_input_cost_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "ALKALI_SILICONE_PETROCHEMICAL_SPREAD_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2024-11-14", "low_price_180d": 59100, "peak_date": "2024-06-11", "peak_price": 118700, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/014/014830.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 8, "chemical_spread_visibility": 10, "information_confidence": 4, "inventory_working_capital_quality": 7, "margin_revision_bridge": 8, "market_mispricing": 9, "realized_spread_duration": 8, "total": 68, "valuation_rerating_runway": 7, "volume_shipment_bridge": 7}, "reuse_reason": null, "same_entry_group_id": "C17_014830_UNID_20240125_ALKALI_SPREAD_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_spread_visibility", "realized_spread_duration_and_volume_bridge", "ASP_input_cost_inventory_margin_revision_route"], "stage3_evidence_fields": ["realized_spread_duration_required", "volume_shipment_or_customer_demand_required", "input_cost_inventory_margin_revision_bridge_required"], "stage4b_evidence_fields": ["chemical_spread_price_premium", "spread_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion_or_demand_gap", "input_cost_or_inventory_quality_break", "margin_revision_bridge_failure"], "symbol": "014830", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014830/2024.csv", "trigger_date": "2024-01-25", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -32.99, "MAE_30D_pct": -12.99, "MAE_90D_pct": -22.99, "MFE_180D_pct": 2.99, "MFE_30D_pct": 2.99, "MFE_90D_pct": 2.99, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_002380_KCC_20240715_SILICONE_SPREAD_PREMIUM_4B", "case_role": "silicone_chemical_spread_price_premium_counterexample", "company_name": "KCC", "corporate_action_window_status": "clean_2024 forward window; corporate-action candidate is 2000-04-17 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Silicone/coating-material spread price premium should route to local 4B or counterexample when the stock has already capitalized spread recovery and incremental realized spread duration, ASP/input-cost pass-through, volume conversion and margin/revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -34.93, "entry_date": "2024-07-15", "entry_price": 335000, "evidence_family": "silicone_coating_material_spread_price_premium_without_incremental_spread_duration_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "ALKALI_SILICONE_PETROCHEMICAL_SPREAD_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2024-11-15", "low_price_180d": 224500, "peak_date": "2024-07-17", "peak_price": 345000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/002/002380.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 4, "chemical_spread_visibility": 7, "information_confidence": 3, "inventory_working_capital_quality": 3, "margin_revision_bridge": 3, "market_mispricing": 4, "realized_spread_duration": 4, "total": 33, "valuation_rerating_runway": 1, "volume_shipment_bridge": 4}, "reuse_reason": null, "same_entry_group_id": "C17_002380_KCC_20240715_SILICONE_SPREAD_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_spread_visibility", "realized_spread_duration_and_volume_bridge", "ASP_input_cost_inventory_margin_revision_route"], "stage3_evidence_fields": ["realized_spread_duration_required", "volume_shipment_or_customer_demand_required", "input_cost_inventory_margin_revision_bridge_required"], "stage4b_evidence_fields": ["chemical_spread_price_premium", "spread_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion_or_demand_gap", "input_cost_or_inventory_quality_break", "margin_revision_bridge_failure"], "symbol": "002380", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002380/2024.csv", "trigger_date": "2024-07-15", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -49.2, "MAE_30D_pct": -10.26, "MAE_90D_pct": -10.33, "MFE_180D_pct": 6.58, "MFE_30D_pct": 6.58, "MFE_90D_pct": 6.58, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_006650_DAEHANPETRO_20240125_PETROCHEM_SPREAD_FALSE_GREEN", "case_role": "petrochemical_spread_false_green_counterexample", "company_name": "대한유화", "corporate_action_window_status": "clean_2024 forward window; corporate-action candidate is 2010-07-13 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Petrochemical spread rebound should stay Yellow or route to local 4B when price confirmation is not followed by realized spread duration, volume/shipment recovery, naphtha/input-cost pass-through, inventory quality and margin/revision evidence. The early 2024 rebound had small residual upside and a much larger forward drawdown.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -52.34, "entry_date": "2024-01-25", "entry_price": 144300, "evidence_family": "petrochemical_spread_rebound_price_confirmation_without_realized_spread_volume_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "ALKALI_SILICONE_PETROCHEMICAL_SPREAD_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2024-12-05", "low_price_180d": 73300, "peak_date": "2024-02-21", "peak_price": 153800, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006650.json", "raw_component_score_breakdown": {"ASP_input_cost_bridge": 3, "chemical_spread_visibility": 6, "information_confidence": 3, "inventory_working_capital_quality": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "realized_spread_duration": 3, "total": 28, "valuation_rerating_runway": 1, "volume_shipment_bridge": 3}, "reuse_reason": null, "same_entry_group_id": "C17_006650_DAEHANPETRO_20240125_PETROCHEM_SPREAD_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_spread_visibility", "realized_spread_duration_and_volume_bridge", "ASP_input_cost_inventory_margin_revision_route"], "stage3_evidence_fields": ["realized_spread_duration_required", "volume_shipment_or_customer_demand_required", "input_cost_inventory_margin_revision_bridge_required"], "stage4b_evidence_fields": ["chemical_spread_price_premium", "spread_optional_value_already_capitalized", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion_or_demand_gap", "input_cost_or_inventory_quality_break", "margin_revision_bridge_failure"], "symbol": "006650", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2024.csv", "trigger_date": "2024-01-25", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "ALKALI_SILICONE_PETROCHEMICAL_SPREAD_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "chemical_commodity_margin_spread_alkali_silicone_petrochemical_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C17 chemical-spread rows should allow Stage2 when realized spread duration is backed by volume/shipment conversion, ASP/input-cost pass-through, inventory/working-capital quality and margin-revision bridge, but should route late-cycle silicone/petrochemical spread premiums to local 4B/Yellow when incremental spread-to-margin evidence has not refreshed.",
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
3. Add C17-specific chemical spread / realized spread duration / volume-shipment / ASP-input-cost / inventory / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C17_STAGE2_ALLOWED_ON_REALIZED_SPREAD_VOLUME_MARGIN_REVISION_BRIDGE
- C17_GREEN_REQUIRES_SPREAD_DURATION_VOLUME_INPUT_COST_INVENTORY_REVISION
- C17_CHEMICAL_SPREAD_PRICE_PREMIUM_LOCAL_4B
- C17_SPREAD_OPTIONALITY_WITHOUT_VOLUME_TO_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.


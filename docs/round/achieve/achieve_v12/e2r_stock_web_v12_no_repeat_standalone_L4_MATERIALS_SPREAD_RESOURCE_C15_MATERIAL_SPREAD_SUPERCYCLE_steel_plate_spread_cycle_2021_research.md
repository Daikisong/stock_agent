# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C15 — Material spread supercycle / steel plate spread-margin guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: STEEL_PLATE_SPREAD_VOLUME_INPUT_COST_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_steel_plate_spread_cycle_2021_research.md
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

This run avoids those top-covered C15 symbols and adds 004020, 005490, and 001230.  
Each row uses a new `C15 + symbol + trigger_type + entry_date` hard key.

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
004020 현대제철: selected 2021 forward window clean; latest corporate-action candidate is 2014-01-24 and outside selected test window.
005490 POSCO홀딩스: corporate_action_candidate_count=0.
001230 동국제강/동국홀딩스: selected 2021 forward window clean; 2023-06-16 and 2023-11-13 corporate-action candidates are after selected 180D window.
```

## 3. Research thesis

C15 should not treat a material spread supercycle as permanent margin by default. It should test whether the spread is realized through shipment volume, utilization and cost pass-through:

```text
material spread supercycle attention
→ realized spread duration
→ shipment volume and utilization
→ raw-material/input-cost pass-through
→ downstream demand and working-capital quality
→ gross margin and revision bridge
→ rerating or local 4B cap
```

A spread is a tide. Stage2 can ride the incoming tide, but Green should still check the ship: tonnage, utilization, input cost, and whether the tide has already lifted the stock too far.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C15_004020_HYUNDAISTEEL_20210329_STEEL_PLATE_SPREAD_STAGE2 | 004020 | positive_steel_plate_spread_stage2_success_with_later_4b_refresh | 2021-03-29 | 48400 | 63000 on 2021-05-11 | 37100 on 2021-11-30 | 30.17% | 30.17% | 30.17% | -23.35% | -41.11% |
| C15_005490_POSCO_20210405_INTEGRATED_STEEL_SPREAD_STAGE2 | 005490 | positive_integrated_steel_spread_stage2_success_with_later_4b_refresh | 2021-04-05 | 334500 | 413500 on 2021-05-10 | 260000 on 2021-11-30 | 23.62% | 23.62% | 23.62% | -22.27% | -37.12% |
| C15_001230_DONGKUKSTEEL_20210427_STEEL_SPREAD_PRICE_PREMIUM_4B | 001230 | steel_spread_price_premium_counterexample | 2021-04-27 | 25300 | 27850 on 2021-04-29 | 14050 on 2021-11-30 | 10.08% | 10.08% | 10.08% | -44.47% | -49.55% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Steel spread supercycle can be a valid Stage2 route when realized spread duration, shipment volume, utilization and margin revisions are visible before the valuation fully capitalizes the cycle.
- 004020 is the plate/rebar positive anchor. The March 2021 trigger produced strong MFE before the later spread premium required 4B discipline.
- 005490 is the integrated steel positive anchor. The April 2021 trigger captured the spread/margin rerating before the May peak and later mean reversion.

### Stage3 / Green
- C15 Green should require realized spread duration, downstream demand, shipment volume, capacity utilization, raw-material cost bridge and margin/revision confirmation.
- A commodity price move alone is not sufficient. The model should ask whether the spread becomes actual margin after input costs, inventory and volume are paid.

### 4B
- 001230 fills the missing C15 local 4B pocket. The stock had already paid for much of the spread cycle by the late-April 2021 trigger and then produced a large 180D MAE.
- 004020 and 005490 also demonstrate the transition from valid Stage2 to later 4B refresh once the spread was capitalized.

### 4C
- No hard plant shutdown, covenant issue, or accounting break is asserted.
- The C15 break mode here is spread mean-reversion/evidence exhaustion: spread strength may remain real, but incremental volume, input-cost and margin revision evidence no longer supports the price already paid.

## 6. Raw component score breakdown

```json
{
  "C15_001230_DONGKUKSTEEL_20210427_STEEL_SPREAD_PRICE_PREMIUM_4B": {
    "downstream_demand_quality": 4,
    "information_confidence": 3,
    "input_cost_pass_through": 4,
    "margin_revision_bridge": 3,
    "market_mispricing": 4,
    "spread_duration_quality": 5,
    "total": 29,
    "valuation_rerating_runway": 1,
    "volume_utilization": 5
  },
  "C15_004020_HYUNDAISTEEL_20210329_STEEL_PLATE_SPREAD_STAGE2": {
    "downstream_demand_quality": 8,
    "information_confidence": 4,
    "input_cost_pass_through": 8,
    "margin_revision_bridge": 9,
    "market_mispricing": 9,
    "spread_duration_quality": 10,
    "total": 64,
    "valuation_rerating_runway": 7,
    "volume_utilization": 9
  },
  "C15_005490_POSCO_20210405_INTEGRATED_STEEL_SPREAD_STAGE2": {
    "downstream_demand_quality": 8,
    "information_confidence": 4,
    "input_cost_pass_through": 8,
    "margin_revision_bridge": 8,
    "market_mispricing": 8,
    "spread_duration_quality": 10,
    "total": 60,
    "valuation_rerating_runway": 6,
    "volume_utilization": 8
  }
}
```

## 7. Current calibrated profile stress test

Suggested C15 guard:
```text
if material_spread_supercycle and realized_spread_volume_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if steel_spread_price_premium and no incremental_spread_duration_volume_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and spread_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual error:
```text
current_profile_error_count = 1
- 001230 / 2021-04-27: steel spread premium can be over-promoted if the model treats price heat as fresh spread-duration, shipment-volume and margin-revision proof.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -23.35, "MAE_30D_pct": -5.06, "MAE_90D_pct": -5.06, "MFE_180D_pct": 30.17, "MFE_30D_pct": 30.17, "MFE_90D_pct": 30.17, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_004020_HYUNDAISTEEL_20210329_STEEL_PLATE_SPREAD_STAGE2", "case_role": "positive_steel_plate_spread_stage2_success_with_later_4b_refresh", "company_name": "현대제철", "corporate_action_window_status": "clean_2021_forward_window; corporate-action candidates are 1997-01-03, 1997-10-16, 1999-03-25, 1999-07-14, 2000-04-12, 2014-01-24, all outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when steel plate/rebar spread strength, utilization and margin leverage were visible before the rerating was fully capitalized. Green still requires realized spread duration, shipment volume, raw-material cost pass-through, downstream demand and margin/revision confirmation; after the May 2021 premium the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.11, "entry_date": "2021-03-29", "entry_price": 48400, "evidence_family": "steel_plate_spread_supercycle_price_volume_input_cost_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "STEEL_PLATE_SPREAD_VOLUME_INPUT_COST_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-30", "low_price_180d": 37100, "peak_date": "2021-05-11", "peak_price": 63000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/004/004020.json", "raw_component_score_breakdown": {"downstream_demand_quality": 8, "information_confidence": 4, "input_cost_pass_through": 8, "margin_revision_bridge": 9, "market_mispricing": 9, "spread_duration_quality": 10, "total": 64, "valuation_rerating_runway": 7, "volume_utilization": 9}, "reuse_reason": null, "same_entry_group_id": "C15_004020_HYUNDAISTEEL_20210329_STEEL_PLATE_SPREAD_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["material_spread_supercycle_attention", "realized_spread_duration_and_volume_visibility", "input_cost_pass_through_margin_revision_route"], "stage3_evidence_fields": ["spread_duration_and_downstream_demand_required", "shipment_volume_utilization_required", "raw_material_input_cost_and_margin_revision_bridge_required"], "stage4b_evidence_fields": ["steel_spread_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "shipment_volume_or_downstream_demand_disappointment", "margin_revision_bridge_failure"], "symbol": "004020", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004020/2021.csv", "trigger_date": "2021-03-29", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -22.27, "MAE_30D_pct": -4.33, "MAE_90D_pct": -4.33, "MFE_180D_pct": 23.62, "MFE_30D_pct": 23.62, "MFE_90D_pct": 23.62, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_005490_POSCO_20210405_INTEGRATED_STEEL_SPREAD_STAGE2", "case_role": "positive_integrated_steel_spread_stage2_success_with_later_4b_refresh", "company_name": "POSCO홀딩스", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2021_forward_window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when integrated steel price/spread strength and operating leverage were visible before valuation caught up. Green still requires realized spread duration, export/domestic shipment volume, raw-material cost bridge, downstream demand and revision evidence; after the May 2021 high, fresh non-price evidence was required before treating the premium as still actionable.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -37.12, "entry_date": "2021-04-05", "entry_price": 334500, "evidence_family": "integrated_steel_spread_volume_price_input_cost_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "STEEL_PLATE_SPREAD_VOLUME_INPUT_COST_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-30", "low_price_180d": 260000, "peak_date": "2021-05-10", "peak_price": 413500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005490.json", "raw_component_score_breakdown": {"downstream_demand_quality": 8, "information_confidence": 4, "input_cost_pass_through": 8, "margin_revision_bridge": 8, "market_mispricing": 8, "spread_duration_quality": 10, "total": 60, "valuation_rerating_runway": 6, "volume_utilization": 8}, "reuse_reason": null, "same_entry_group_id": "C15_005490_POSCO_20210405_INTEGRATED_STEEL_SPREAD_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["material_spread_supercycle_attention", "realized_spread_duration_and_volume_visibility", "input_cost_pass_through_margin_revision_route"], "stage3_evidence_fields": ["spread_duration_and_downstream_demand_required", "shipment_volume_utilization_required", "raw_material_input_cost_and_margin_revision_bridge_required"], "stage4b_evidence_fields": ["steel_spread_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "shipment_volume_or_downstream_demand_disappointment", "margin_revision_bridge_failure"], "symbol": "005490", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv", "trigger_date": "2021-04-05", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -44.47, "MAE_30D_pct": -17.59, "MAE_90D_pct": -17.39, "MFE_180D_pct": 10.08, "MFE_30D_pct": 10.08, "MFE_90D_pct": 10.08, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_001230_DONGKUKSTEEL_20210427_STEEL_SPREAD_PRICE_PREMIUM_4B", "case_role": "steel_spread_price_premium_counterexample", "company_name": "동국제강", "corporate_action_window_status": "clean_2021_forward_window; corporate-action candidates are 1999-01-27, 1999-07-13, 1999-09-21, 2014-07-15, and later 2023-06-16/2023-11-13, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Steel spread price premium should route to local 4B or counterexample when the stock has already capitalized the spread supercycle and incremental spread duration, shipment volume, input-cost pass-through and margin/revision evidence do not keep expanding.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -49.55, "entry_date": "2021-04-27", "entry_price": 25300, "evidence_family": "steel_plate_rebar_spread_price_premium_without_incremental_spread_volume_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "STEEL_PLATE_SPREAD_VOLUME_INPUT_COST_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-30", "low_price_180d": 14050, "peak_date": "2021-04-29", "peak_price": 27850, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/001/001230.json", "raw_component_score_breakdown": {"downstream_demand_quality": 4, "information_confidence": 3, "input_cost_pass_through": 4, "margin_revision_bridge": 3, "market_mispricing": 4, "spread_duration_quality": 5, "total": 29, "valuation_rerating_runway": 1, "volume_utilization": 5}, "reuse_reason": null, "same_entry_group_id": "C15_001230_DONGKUKSTEEL_20210427_STEEL_SPREAD_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["material_spread_supercycle_attention", "realized_spread_duration_and_volume_visibility", "input_cost_pass_through_margin_revision_route"], "stage3_evidence_fields": ["spread_duration_and_downstream_demand_required", "shipment_volume_utilization_required", "raw_material_input_cost_and_margin_revision_bridge_required"], "stage4b_evidence_fields": ["steel_spread_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "shipment_volume_or_downstream_demand_disappointment", "margin_revision_bridge_failure"], "symbol": "001230", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001230/2021.csv", "trigger_date": "2021-04-27", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "counterexample_count": 1,
  "current_profile_error_count": 1,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "STEEL_PLATE_SPREAD_VOLUME_INPUT_COST_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "material_spread_supercycle_steel_plate_volume_margin_new_symbols_4b_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 2,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C15 material-spread rows should allow Stage2 when realized spread duration is backed by shipment volume, utilization, input-cost pass-through and margin/revision evidence, but should route to local 4B when the spread supercycle is already capitalized and incremental spread/volume evidence has not refreshed.",
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
3. Add C15-specific material spread / steel plate spread / volume / input-cost / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C15_STAGE2_ALLOWED_ON_REALIZED_SPREAD_VOLUME_MARGIN_REVISION_BRIDGE
- C15_GREEN_REQUIRES_SPREAD_DURATION_VOLUME_INPUT_COST_DEMAND_REVISION
- C15_STEEL_SPREAD_PRICE_PREMIUM_LOCAL_4B
- C15_SPREAD_HEAT_WITHOUT_INCREMENTAL_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 1 counterexample, and 1 current-profile residual error for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.


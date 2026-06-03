# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C15 — Material spread supercycle / steel and non-ferrous duration guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: STEEL_NONFERROUS_SPREAD_DURATION_REVISION_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_steel_nonferrous_spread_2021_research.md
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

This run avoids those top-covered C15 symbols and adds 005490, 004020, and 010130.  
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
005490 POSCO홀딩스: corporate_action_candidate_count=0.
004020 현대제철: 2021 forward window clean; corporate-action candidates are old, latest 2014-01-24.
010130 고려아연: corporate_action_candidate_count=0.
```

## 3. Research thesis

C15 should not treat every material price rally as durable EPS. It should test whether the spread itself stays alive long enough to reach revisions:

```text
material spread / steel / non-ferrous supercycle attention
→ product price versus raw-material cost spread
→ global restocking or export price visibility
→ shipment mix and cost pass-through
→ margin and revision bridge
→ rerating
```

The spread is a furnace. Stage2 can follow the heat early, but Green should require the furnace to keep running after fuel, ore, coal, energy and shipment mix are paid for.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C15_005490_POSCO_20210215_STEEL_SPREAD_SUPERCYCLE_STAGE2 | 005490 | positive_steel_spread_supercycle_stage2_success_with_later_4b | 2021-02-15 | 268000 | 413500 on 2021-05-10 | 260000 on 2021-11-30 | 23.51% | 54.29% | 54.29% | -2.99% | -37.12% |
| C15_004020_HYUNDAISTEEL_20210511_STEEL_SPREAD_LATE_4B | 004020 | late_steel_spread_price_premium_counterexample | 2021-05-11 | 61900 | 63000 on 2021-05-11 | 37100 on 2021-11-30 | 1.78% | 1.78% | 1.78% | -40.06% | -41.11% |
| C15_010130_KOREAZINC_20211018_NONFERROUS_SPREAD_LATE_4B | 010130 | late_nonferrous_metal_spread_counterexample | 2021-10-18 | 607000 | 624000 on 2021-10-18 | 482000 on 2021-11-22 | 2.8% | 2.8% | 2.8% | -20.59% | -22.76% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Material spread expansion, export price visibility, and restocking can be valid Stage2 routes.
- 005490 is the positive anchor: early 2021 steel-spread evidence produced a large MFE before the spread narrative matured into a late-cycle risk-control problem.

### Stage3 / Green
- C15 Green should require spread duration, raw-material pass-through, shipment mix, cost curve and revision confirmation.
- The model should not treat product-price headlines as sufficient. A steel price rise can be eaten by ore, coal, freight, energy or volume mix.

### 4B
- 004020 and 010130 fill the missing 4B pocket. Both rows show late spread-cycle price premium: the material story was real, but the easy rerating had already been capitalized.
- Local 4B should activate when price runs ahead of incremental spread-duration evidence.

### 4C
- No hard accounting break is asserted.
- The C15 break mode is spread mean reversion: the product price story remains plausible, but input-cost, energy, shipment mix, margin and revision evidence stop widening.

## 6. Raw component score breakdown

```json
{
  "C15_004020_HYUNDAISTEEL_20210511_STEEL_SPREAD_LATE_4B": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 30,
    "valuation_rerating_runway": 2,
    "visibility_quality": 6
  },
  "C15_005490_POSCO_20210215_STEEL_SPREAD_SUPERCYCLE_STAGE2": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 3,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 58,
    "valuation_rerating_runway": 9,
    "visibility_quality": 11
  },
  "C15_010130_KOREAZINC_20211018_NONFERROUS_SPREAD_LATE_4B": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 30,
    "valuation_rerating_runway": 2,
    "visibility_quality": 6
  }
}
```

## 7. Current calibrated profile stress test

Suggested C15 guard:
```text
if material_spread_expansion and early_cycle_restocking_export_price_visibility:
    allow_stage2_actionable = true

if material_spread_price_premium and no incremental_spread_duration_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and spread_or_input_cost_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 004020 / 2021-05-11: late steel spread premium can be over-promoted if the model treats price confirmation as fresh spread-duration evidence.
- 010130 / 2021-10-18: non-ferrous spread premium can become price-only when metal price duration, energy/cost and revision bridge do not expand further.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -2.99, "MAE_30D_pct": -4.66, "MAE_90D_pct": -4.66, "MFE_180D_pct": 54.29, "MFE_30D_pct": 23.51, "MFE_90D_pct": 54.29, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_005490_POSCO_20210215_STEEL_SPREAD_SUPERCYCLE_STAGE2", "case_role": "positive_steel_spread_supercycle_stage2_success_with_later_4b", "company_name": "POSCO홀딩스", "corporate_action_window_status": "clean_2021_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when steel product spread and global restocking visibility created a clear rerating route, but Green still requires spread duration, raw-material pass-through, shipment mix, export price and revision bridge; after the May 2021 peak the same evidence needed 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -37.12, "entry_date": "2021-02-15", "entry_price": 268000, "evidence_family": "steel_spread_raw_material_product_price_supercycle_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "STEEL_NONFERROUS_SPREAD_DURATION_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-30", "low_price_180d": 260000, "peak_date": "2021-05-10", "peak_price": 413500, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/005/005490.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 3, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 10, "total": 58, "valuation_rerating_runway": 9, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C15_005490_POSCO_20210215_STEEL_SPREAD_SUPERCYCLE_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["material_spread_supercycle_attention", "product_price_raw_material_spread_expansion", "global_restocking_or_export_price_visibility"], "stage3_evidence_fields": ["spread_duration_confirmation_required", "raw_material_pass_through_and_cost_curve_required", "shipment_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["material_spread_cycle_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "energy_or_input_cost_burden", "shipment_margin_revision_bridge_failure"], "symbol": "005490", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2021.csv", "trigger_date": "2021-02-15", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -40.06, "MAE_30D_pct": -18.26, "MAE_90D_pct": -40.06, "MFE_180D_pct": 1.78, "MFE_30D_pct": 1.78, "MFE_90D_pct": 1.78, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_004020_HYUNDAISTEEL_20210511_STEEL_SPREAD_LATE_4B", "case_role": "late_steel_spread_price_premium_counterexample", "company_name": "현대제철", "corporate_action_window_status": "clean_2021_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "Late steel-spread price premium should route to local 4B or counterexample unless incremental product-price spread, raw-material pass-through, shipment mix and revision duration remain visible after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.11, "entry_date": "2021-05-11", "entry_price": 61900, "evidence_family": "late_steel_spread_product_price_premium_without_incremental_margin_revision_duration", "evidence_url_pending": false, "fine_archetype_id": "STEEL_NONFERROUS_SPREAD_DURATION_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-30", "low_price_180d": 37100, "peak_date": "2021-05-11", "peak_price": 63000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/004/004020.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 4, "total": 30, "valuation_rerating_runway": 2, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C15_004020_HYUNDAISTEEL_20210511_STEEL_SPREAD_LATE_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["material_spread_supercycle_attention", "product_price_raw_material_spread_expansion", "global_restocking_or_export_price_visibility"], "stage3_evidence_fields": ["spread_duration_confirmation_required", "raw_material_pass_through_and_cost_curve_required", "shipment_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["material_spread_cycle_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "energy_or_input_cost_burden", "shipment_margin_revision_bridge_failure"], "symbol": "004020", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004020/2021.csv", "trigger_date": "2021-05-11", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -20.59, "MAE_30D_pct": -20.43, "MAE_90D_pct": -20.59, "MFE_180D_pct": 2.8, "MFE_30D_pct": 2.8, "MFE_90D_pct": 2.8, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "case_id": "C15_010130_KOREAZINC_20211018_NONFERROUS_SPREAD_LATE_4B", "case_role": "late_nonferrous_metal_spread_counterexample", "company_name": "고려아연", "corporate_action_window_status": "clean_2021_forward_window; corporate-action candidates none or old/outside selected test window", "current_profile_error": true, "current_profile_verdict": "Late non-ferrous metal spread premium should route to local 4B unless treatment charges, energy/cost burden, FX, metal price duration and revision evidence keep expanding after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -22.76, "entry_date": "2021-10-18", "entry_price": 607000, "evidence_family": "nonferrous_zinc_metal_spread_price_premium_without_cost_energy_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "STEEL_NONFERROUS_SPREAD_DURATION_REVISION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-11-22", "low_price_180d": 482000, "peak_date": "2021-10-18", "peak_price": 624000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/010/010130.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 4, "total": 30, "valuation_rerating_runway": 2, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C15_010130_KOREAZINC_20211018_NONFERROUS_SPREAD_LATE_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["material_spread_supercycle_attention", "product_price_raw_material_spread_expansion", "global_restocking_or_export_price_visibility"], "stage3_evidence_fields": ["spread_duration_confirmation_required", "raw_material_pass_through_and_cost_curve_required", "shipment_mix_margin_revision_bridge_required"], "stage4b_evidence_fields": ["material_spread_cycle_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "energy_or_input_cost_burden", "shipment_margin_revision_bridge_failure"], "symbol": "010130", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2021.csv", "trigger_date": "2021-10-18", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "STEEL_NONFERROUS_SPREAD_DURATION_REVISION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "material_spread_supercycle_steel_nonferrous_4b_gap_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C15 material spread-supercycle rows should allow Stage2 on early spread expansion and restocking/export-price visibility, but Stage3 Green requires spread duration, raw-material pass-through, cost curve, shipment mix, margin and revision bridge; late steel/nonferrous spread price premium should route to local 4B or counterexample.",
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
3. Add C15-specific spread-duration / cost-pass-through / shipment-mix / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C15_STAGE2_ALLOWED_ON_EARLY_SPREAD_EXPANSION_RESTOCKING_EXPORT_PRICE
- C15_GREEN_REQUIRES_SPREAD_DURATION_COST_PASS_THROUGH_SHIPMENT_MIX_REVISION
- C15_LATE_STEEL_NONFERROUS_SPREAD_PREMIUM_LOCAL_4B
- C15_SPREAD_MEAN_REVERSION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.


# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C17 — Chemical commodity margin spread guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CAUSTIC_PETROCHEM_FILM_SPREAD_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_caustic_petrochem_film_spread_2021_2022_research.md
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

This run avoids those top-covered C17 symbols and adds 014830, 006650, and 011790.  
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
014830 유니드: selected 2021/2022 window is before the 2022-11-28 corporate-action candidate; 2015 candidate is outside the selected test window.
006650 대한유화: selected 2022 window clean; corporate-action candidate is 2010-07-13, outside the selected test window.
011790 SKC: selected 2021/2022 window clean; corporate-action candidates are 1998/2001 and outside the selected test window.
```

## 3. Research thesis

C17 should not treat a chemical price rally as durable EPS. It should test whether the product-vs-feedstock spread survives long enough to reach revisions:

```text
chemical commodity / chlor-alkali / petrochemical / film spread attention
→ product price versus feedstock or energy cost spread
→ export price, shipment mix or inventory restocking
→ cost pass-through and spread duration
→ margin and revision bridge
→ rerating
```

The spread is a pipe, not a reservoir. Stage2 can follow pressure building in the pipe, but Green should require the pressure to keep flowing after raw materials, energy, freight and demand elasticity are paid.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C17_014830_UNID_20210419_CAUSTIC_POTASH_SPREAD_STAGE2 | 014830 | positive_caustic_potash_spread_stage2_success_with_later_4b | 2021-04-19 | 75700 | 159000 on 2021-09-16 | 72500 on 2021-04-19 | 26.42% | 90.89% | 110.04% | -4.23% | -51.82% |
| C17_006650_DAEHAN_20220107_PETROCHEM_SPREAD_FALSE_GREEN | 006650 | petrochemical_spread_false_green_counterexample | 2022-01-07 | 194000 | 196500 on 2022-01-10 | 102000 on 2022-09-28 | 1.29% | 1.29% | 1.29% | -47.42% | -48.09% |
| C17_011790_SKC_20220408_FILM_CHEMICAL_SPREAD_PRICE_PREMIUM_4B | 011790 | chemical_film_margin_spread_price_premium_counterexample | 2022-04-08 | 166500 | 168000 on 2022-04-08 | 83400 on 2022-09-30 | 0.9% | 0.9% | 0.9% | -49.91% | -50.36% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Chemical commodity spread expansion can be a valid Stage2 route when product pricing, export demand and feedstock cost leverage are visible before the valuation has fully capitalized the spread.
- 014830 is the positive anchor: caustic/potash spread expansion produced a large MFE, but after the September 2021 blowoff the same evidence no longer justified fresh Green without spread-duration and revision refresh.

### Stage3 / Green
- C17 Green should require spread duration, feedstock/energy pass-through, shipment mix, demand volume, margin and revision confirmation.
- 006650 shows why petrochemical spread recovery should not be promoted if naphtha/feedstock cost and product demand evidence are deteriorating.
- 011790 adds the film/copper-foil adjacent version: the stock can price a margin spread before utilization, input-cost and revision evidence remain strong.

### 4B
- 011790 fills a C17 local 4B gap. The April 2022 premium had little forward upside and a deep drawdown once input-cost and margin bridge stopped expanding.
- 014830 also required later 4B discipline after a valid Stage2 became a fully capitalized spread story.

### 4C
- No hard accounting or plant/event break is asserted.
- The C17 break mode is spread mean reversion: product-price headlines remain plausible, but feedstock, energy, freight, demand volume, shipment mix and revisions do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C17_006650_DAEHAN_20220107_PETROCHEM_SPREAD_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 26,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C17_011790_SKC_20220408_FILM_CHEMICAL_SPREAD_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 27,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C17_014830_UNID_20210419_CAUSTIC_POTASH_SPREAD_STAGE2": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 3,
    "eps_fcf_explosion": 11,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 57,
    "valuation_rerating_runway": 9,
    "visibility_quality": 11
  }
}
```

## 7. Current calibrated profile stress test

Suggested C17 guard:
```text
if chemical_spread_expansion and export_price_or_product_repricing_visibility:
    allow_stage2_actionable = true

if chemical_spread_price_premium and no incremental_spread_duration_feedstock_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and spread_or_input_cost_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 006650 / 2022-01-07: petrochemical spread recovery can be over-promoted if the model does not require naphtha/feedstock and product-demand confirmation.
- 011790 / 2022-04-08: film/chemical spread premium can become price-only when input-cost, utilization, margin and revision evidence fail to refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -4.23, "MAE_30D_pct": -4.23, "MAE_90D_pct": -4.23, "MFE_180D_pct": 110.04, "MFE_30D_pct": 26.42, "MFE_90D_pct": 90.89, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_014830_UNID_20210419_CAUSTIC_POTASH_SPREAD_STAGE2", "case_role": "positive_caustic_potash_spread_stage2_success_with_later_4b", "company_name": "유니드", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when caustic/potash chemical spread expansion and export-price visibility created a clear margin-revision route; after the September 2021 blowoff, the same evidence aged into 4B discipline because spread duration and revision support had to be refreshed.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.82, "entry_date": "2021-04-19", "entry_price": 75700, "evidence_family": "caustic_potash_chlor_alkali_export_spread_margin_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "CAUSTIC_PETROCHEM_FILM_SPREAD_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-04-19", "low_price_180d": 72500, "peak_date": "2021-09-16", "peak_price": 159000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/014/014830.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 3, "eps_fcf_explosion": 11, "information_confidence": 4, "market_mispricing": 10, "total": 57, "valuation_rerating_runway": 9, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C17_014830_UNID_20210419_CAUSTIC_POTASH_SPREAD_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_spread_attention", "product_price_vs_feedstock_spread_visibility", "export_price_or_inventory_restocking_signal"], "stage3_evidence_fields": ["spread_duration_confirmation_required", "feedstock_or_energy_cost_pass_through_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["chemical_spread_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "feedstock_energy_or_input_cost_burden", "margin_revision_bridge_failure"], "symbol": "014830", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014830/2021.csv", "trigger_date": "2021-04-19", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -47.42, "MAE_30D_pct": -26.03, "MAE_90D_pct": -33.76, "MFE_180D_pct": 1.29, "MFE_30D_pct": 1.29, "MFE_90D_pct": 1.29, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_006650_DAEHAN_20220107_PETROCHEM_SPREAD_FALSE_GREEN", "case_role": "petrochemical_spread_false_green_counterexample", "company_name": "대한유화", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": true, "current_profile_verdict": "Petrochemical spread recovery should stay Yellow when naphtha/feedstock burden, product spread duration, demand volume and margin/revision bridge are not improving; price confirmation alone was a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -48.09, "entry_date": "2022-01-07", "entry_price": 194000, "evidence_family": "petrochemical_product_spread_price_premium_without_naphtha_cost_margin_revision_duration", "evidence_url_pending": false, "fine_archetype_id": "CAUSTIC_PETROCHEM_FILM_SPREAD_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-09-28", "low_price_180d": 102000, "peak_date": "2022-01-10", "peak_price": 196500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006650.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 26, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C17_006650_DAEHAN_20220107_PETROCHEM_SPREAD_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_spread_attention", "product_price_vs_feedstock_spread_visibility", "export_price_or_inventory_restocking_signal"], "stage3_evidence_fields": ["spread_duration_confirmation_required", "feedstock_or_energy_cost_pass_through_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["chemical_spread_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "feedstock_energy_or_input_cost_burden", "margin_revision_bridge_failure"], "symbol": "006650", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2022.csv", "trigger_date": "2022-01-07", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -49.91, "MAE_30D_pct": -21.32, "MAE_90D_pct": -25.53, "MFE_180D_pct": 0.9, "MFE_30D_pct": 0.9, "MFE_90D_pct": 0.9, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_011790_SKC_20220408_FILM_CHEMICAL_SPREAD_PRICE_PREMIUM_4B", "case_role": "chemical_film_margin_spread_price_premium_counterexample", "company_name": "SKC", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": true, "current_profile_verdict": "Chemical film / copper-foil margin premium should route to local 4B when input-cost, utilization, shipment mix and revision evidence no longer expand after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -50.36, "entry_date": "2022-04-08", "entry_price": 166500, "evidence_family": "chemical_film_copper_foil_input_cost_spread_premium_without_incremental_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "CAUSTIC_PETROCHEM_FILM_SPREAD_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-09-30", "low_price_180d": 83400, "peak_date": "2022-04-08", "peak_price": 168000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/011/011790.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 27, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C17_011790_SKC_20220408_FILM_CHEMICAL_SPREAD_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_commodity_spread_attention", "product_price_vs_feedstock_spread_visibility", "export_price_or_inventory_restocking_signal"], "stage3_evidence_fields": ["spread_duration_confirmation_required", "feedstock_or_energy_cost_pass_through_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["chemical_spread_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "feedstock_energy_or_input_cost_burden", "margin_revision_bridge_failure"], "symbol": "011790", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2022.csv", "trigger_date": "2022-04-08", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "CAUSTIC_PETROCHEM_FILM_SPREAD_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "chemical_commodity_spread_caustic_petrochem_film_new_symbols_and_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C17 chemical commodity margin-spread rows should allow Stage2 on early product-vs-feedstock spread expansion and export/repricing visibility, but Stage3 Green requires spread duration, feedstock/energy cost pass-through, demand volume, shipment mix, margin and revision bridge; chemical spread price premium without incremental margin proof should route to local 4B or counterexample.",
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
3. Add C17-specific chemical spread / feedstock / energy / product-repricing / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C17_STAGE2_ALLOWED_ON_EARLY_PRODUCT_FEEDSTOCK_SPREAD_EXPANSION
- C17_GREEN_REQUIRES_SPREAD_DURATION_FEEDSTOCK_ENERGY_PASS_THROUGH_MARGIN_REVISION
- C17_CHEMICAL_SPREAD_PRICE_PREMIUM_LOCAL_4B
- C17_SPREAD_MEAN_REVERSION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.


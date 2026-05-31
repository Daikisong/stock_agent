# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C17 — Chemical commodity margin-spread duration guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: REFINING_PETROCHEMICAL_CAUSTIC_SPREAD_DURATION_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_refining_petrochemical_caustic_spread_2021_2023_research.md
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

This run avoids those top-covered C17 symbols and adds 010950, 006650, and 014830.  
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
010950 S-Oil: 2022 forward window clean; corporate-action candidate is old, outside the test window.
006650 대한유화: 2021 forward window clean; corporate-action candidate is 2010-07-13.
014830 유니드: 2023 forward window clean after the 2022-11-28 candidate; old 2015 candidate is outside the test window.
```

## 3. Research thesis

C17 should not be a generic chemical upcycle bucket. It should test whether a product/raw-material spread has enough duration to become EPS bodyweight:

```text
chemical/refining spread expansion
→ inventory or cost-lag operating leverage
→ cost pass-through and product-pricing durability
→ margin and revision bridge
→ rerating
```

The critical distinction is between a live spread and a photograph of a spread. Early in the cycle, the margin bridge can move like a conveyor belt. Late in the cycle, the same spread headline becomes a rear-view mirror.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C17_010950_SOIL_20220325_REFINING_CRACK_SPREAD_STAGE2_SUCCESS | 010950 | positive_refining_spread_stage2_success_with_later_4b | 2022-03-25 | 92200 | 123000 on 2022-06-13 | 77500 on 2022-09-28 | 19.85% | 33.41% | 33.41% | -15.94% | -36.99% |
| C17_006650_DAEHAN_20210427_PETROCHEMICAL_SPREAD_LATE_FALSE_GREEN | 006650 | late_petrochemical_spread_false_green_counterexample | 2021-04-27 | 363000 | 372500 on 2021-04-27 | 201000 on 2021-10-12 | 2.62% | 2.62% | 2.62% | -44.63% | -46.04% |
| C17_014830_UNID_20230116_CAUSTIC_POTASH_PRICE_NORMALIZATION_COUNTEREXAMPLE | 014830 | caustic_chemical_spread_normalization_counterexample | 2023-01-16 | 89000 | 92000 on 2023-01-17 | 61000 on 2023-07-07 | 3.37% | 3.37% | 3.37% | -31.46% | -33.7% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Refining crack spread, petrochemical product spread, and alkali/caustic spread attention are valid routing signals.
- 010950 is the positive anchor: the 2022 refining spread expansion produced a Stage2 path with meaningful MFE before the later spread unwind.

### Stage3 / Green
- C17 Green should require spread duration, cost pass-through, inventory quality, and margin/revision confirmation.
- 006650 and 014830 show why late spread-cycle price confirmation should stay Yellow/local 4B unless revision evidence is still expanding.

### 4B
- 010950 still required later 4B discipline after the June 2022 peak.
- 006650 and 014830 are late-cycle price-premium rows: price strength did not carry enough evidence-weighted runway after the spread evidence aged.

### 4C
- No hard accounting break is asserted.
- The C17 break mode is spread mean reversion and margin-duration failure. The operating story may remain plausible, but the non-price bridge stops widening.

## 6. Raw component score breakdown

```json
{
  "C17_006650_DAEHAN_20210427_PETROCHEMICAL_SPREAD_LATE_FALSE_GREEN": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 7,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 32,
    "valuation_rerating_runway": 2,
    "visibility_quality": 6
  },
  "C17_010950_SOIL_20220325_REFINING_CRACK_SPREAD_STAGE2_SUCCESS": {
    "bottleneck_pricing_power": 10,
    "capital_allocation": 3,
    "eps_fcf_explosion": 12,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 59,
    "valuation_rerating_runway": 8,
    "visibility_quality": 12
  },
  "C17_014830_UNID_20230116_CAUSTIC_POTASH_PRICE_NORMALIZATION_COUNTEREXAMPLE": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 29,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C17 guard:
```text
if chemical_spread_expansion and early_cycle_revision_bridge_visible:
    allow_stage2_actionable = true

if spread_cycle_price_run and no incremental_spread_duration_or_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and spread_or_inventory_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 006650 / 2021-04-27: late petrochemical spread price confirmation can be over-promoted if spread duration and revision evidence are not required.
- 014830 / 2023-01-16: alkali/caustic spread normalization can look like Green, but the later path argues for Yellow/4B/counterexample when margin duration fades.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -15.94, "MAE_30D_pct": -3.04, "MAE_90D_pct": -3.04, "MFE_180D_pct": 33.41, "MFE_30D_pct": 19.85, "MFE_90D_pct": 33.41, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_010950_SOIL_20220325_REFINING_CRACK_SPREAD_STAGE2_SUCCESS", "case_role": "positive_refining_spread_stage2_success_with_later_4b", "company_name": "S-Oil", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when refining crack spread and inventory leverage were expanding, but Green still requires spread duration, cost pass-through, inventory quality, and revision bridge; after June 2022 the case required 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -36.99, "entry_date": "2022-03-25", "entry_price": 92200, "evidence_family": "refining_crack_spread_inventory_margin_revision_route", "evidence_url_pending": false, "fine_archetype_id": "REFINING_PETROCHEMICAL_CAUSTIC_SPREAD_DURATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2022-09-28", "low_price_180d": 77500, "peak_date": "2022-06-13", "peak_price": 123000, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/010/010950.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 10, "capital_allocation": 3, "eps_fcf_explosion": 12, "information_confidence": 4, "market_mispricing": 10, "total": 59, "valuation_rerating_runway": 8, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C17_010950_SOIL_20220325_REFINING_CRACK_SPREAD_STAGE2_SUCCESS", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_or_refining_spread_attention", "inventory_or_cost_lag_operating_leverage", "raw_material_or_product_price_spread_signal"], "stage3_evidence_fields": ["spread_duration_confirmation_required", "cost_pass_through_and_inventory_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["spread_cycle_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "inventory_or_cost_lag_reversal", "margin_or_revision_duration_failure"], "symbol": "010950", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010950/2022.csv", "trigger_date": "2022-03-25", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -44.63, "MAE_30D_pct": -27.0, "MAE_90D_pct": -39.81, "MFE_180D_pct": 2.62, "MFE_30D_pct": 2.62, "MFE_90D_pct": 2.62, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_006650_DAEHAN_20210427_PETROCHEMICAL_SPREAD_LATE_FALSE_GREEN", "case_role": "late_petrochemical_spread_false_green_counterexample", "company_name": "대한유화", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": true, "current_profile_verdict": "Late petrochemical spread price confirmation should stay Yellow/local 4B unless spread duration and revision evidence remain fresh; price confirmation alone was a false-Green risk.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -46.04, "entry_date": "2021-04-27", "entry_price": 363000, "evidence_family": "late_petrochemical_spread_price_confirmation_without_spread_duration_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "REFINING_PETROCHEMICAL_CAUSTIC_SPREAD_DURATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2021-10-12", "low_price_180d": 201000, "peak_date": "2021-04-27", "peak_price": 372500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/006/006650.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 7, "information_confidence": 3, "market_mispricing": 5, "total": 32, "valuation_rerating_runway": 2, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C17_006650_DAEHAN_20210427_PETROCHEMICAL_SPREAD_LATE_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_or_refining_spread_attention", "inventory_or_cost_lag_operating_leverage", "raw_material_or_product_price_spread_signal"], "stage3_evidence_fields": ["spread_duration_confirmation_required", "cost_pass_through_and_inventory_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["spread_cycle_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "inventory_or_cost_lag_reversal", "margin_or_revision_duration_failure"], "symbol": "006650", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv", "trigger_date": "2021-04-27", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -31.46, "MAE_30D_pct": -10.22, "MAE_90D_pct": -20.34, "MFE_180D_pct": 3.37, "MFE_30D_pct": 3.37, "MFE_90D_pct": 3.37, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "case_id": "C17_014830_UNID_20230116_CAUSTIC_POTASH_PRICE_NORMALIZATION_COUNTEREXAMPLE", "case_role": "caustic_chemical_spread_normalization_counterexample", "company_name": "유니드", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": true, "current_profile_verdict": "Alkali/caustic spread normalization should not become Green unless pricing, cost, inventory and revision duration remain visible; otherwise the spread story is stale.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -33.7, "entry_date": "2023-01-16", "entry_price": 89000, "evidence_family": "alkali_caustic_potash_spread_normalization_without_margin_revision_duration", "evidence_url_pending": false, "fine_archetype_id": "REFINING_PETROCHEMICAL_CAUSTIC_SPREAD_DURATION_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-07-07", "low_price_180d": 61000, "peak_date": "2023-01-17", "peak_price": 92000, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/014/014830.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 29, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C17_014830_UNID_20230116_CAUSTIC_POTASH_PRICE_NORMALIZATION_COUNTEREXAMPLE", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["chemical_or_refining_spread_attention", "inventory_or_cost_lag_operating_leverage", "raw_material_or_product_price_spread_signal"], "stage3_evidence_fields": ["spread_duration_confirmation_required", "cost_pass_through_and_inventory_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["spread_cycle_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["spread_mean_reversion", "inventory_or_cost_lag_reversal", "margin_or_revision_duration_failure"], "symbol": "014830", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014830/2023.csv", "trigger_date": "2023-01-16", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "REFINING_PETROCHEMICAL_CAUSTIC_SPREAD_DURATION_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "chemical_commodity_spread_duration_counterexamples_added",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C17 chemical/refining commodity-spread rows should allow Stage2 on early spread expansion, but Stage3 Green requires spread duration, cost pass-through, inventory quality, margin and revision bridge; late spread-cycle price premium should route to local 4B or counterexample.",
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
3. Add C17-specific spread-duration / inventory-quality / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C17_GREEN_REQUIRES_SPREAD_DURATION_COST_PASS_THROUGH_MARGIN_REVISION
- C17_REFINING_SPREAD_EARLY_STAGE2_ALLOWED
- C17_LATE_CHEMICAL_SPREAD_PRICE_PREMIUM_LOCAL_4B
- C17_SPREAD_MEAN_REVERSION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.


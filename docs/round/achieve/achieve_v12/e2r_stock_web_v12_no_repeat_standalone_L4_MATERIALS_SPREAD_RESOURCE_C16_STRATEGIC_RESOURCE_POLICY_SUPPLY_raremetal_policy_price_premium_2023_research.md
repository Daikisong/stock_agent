# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C16 — Strategic resource policy supply / rare-metal export-control 4B guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: RARE_METAL_EXPORT_CONTROL_POLICY_4B_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_raremetal_policy_price_premium_2023_research.md
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

This run avoids those top-covered C16 symbols and adds 075970, 081150, and 037370.  
Each row uses a new `C16 + symbol + trigger_type + entry_date` hard key.

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
075970 동국알앤에스: selected 2023/2024 forward window clean; corporate-action candidates are 2006-06-02, 2006-06-13, 2008-06-10, outside selected test window.
081150 티플랙스: selected 2023/2024 forward window clean; corporate-action candidates are 2012-10-04 and 2012-10-25, outside selected test window.
037370 EG: selected 2023/2024 forward window clean; corporate-action candidates are 2000-04-24 and 2008-08-28, outside selected test window.
```

## 3. Research thesis

C16 should not treat every strategic-resource policy shock as direct earnings evidence. It should test whether the policy shock becomes company-specific supply, volume and margin:

```text
strategic resource policy / export-control attention
→ direct supply-chain exposure
→ secured offtake, inventory or processing capacity
→ resource price-duration and volume
→ input cost, working capital and margin revision bridge
→ rerating or local 4B cap
```

A policy shock is a siren. Green should not buy the siren; it should buy the company that actually owns the scarce gate, ships volume through it, and converts the spread into revisions.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C16_075970_DONGKUKRNS_20230704_RARE_EARTH_EXPORT_CONTROL_POLICY_4B | 075970 | protective_rare_earth_export_control_policy_price_premium_4b_success | 2023-07-04 | 4930 | 6350 on 2023-07-07 | 3220 on 2023-10-05 | 28.8% | 28.8% | 28.8% | -34.69% | -49.29% |
| C16_081150_TPLEX_20230818_RARE_METAL_POLICY_SPIKE_FALSE_GREEN | 081150 | rare_metal_policy_theme_false_green_counterexample | 2023-08-18 | 4610 | 5790 on 2023-08-21 | 2655 on 2024-04-11 | 25.6% | 25.6% | 25.6% | -42.41% | -54.15% |
| C16_037370_EG_20230725_RARE_EARTH_MAGNET_POLICY_PREMIUM_4B | 037370 | rare_earth_magnet_policy_price_premium_counterexample | 2023-07-25 | 17820 | 19500 on 2023-08-02 | 8130 on 2024-04-11 | 9.43% | 9.43% | 9.43% | -54.38% | -58.31% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C16 Green should require direct supply-chain exposure, secured offtake, inventory quality, processing capacity, price-duration, volume and margin/revision confirmation.
- 081150 is the false-Green/Yellow guard: rare-metal price confirmation produced short MFE, but forward MAE and drawdown show that price heat was not enough without non-price conversion evidence.

### 4B
- 075970 is the protective 4B anchor. The policy headline created a strong spike, but direct revenue and margin evidence did not refresh, so the forward path validated local 4B discipline.
- 037370 is the rare-earth/magnet policy premium counterexample. The price spike had little durable support once direct offtake, capacity and revision evidence failed to close.
- The core 4B rule is that strategic-resource salience must not be substituted for company-level inventory, offtake, capacity and margin proof.

### 4C
- No hard contract cancellation, mine/resource impairment or accounting break is asserted.
- The C16 break mode is policy-to-company conversion failure: the geopolitical supply issue can remain real while the listed company fails to convert it into durable revenue and revisions.

## 6. Raw component score breakdown

```json
{
  "C16_037370_EG_20230725_RARE_EARTH_MAGNET_POLICY_PREMIUM_4B": {
    "direct_resource_exposure": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 3,
    "offtake_inventory_quality": 2,
    "policy_supply_shock": 7,
    "price_duration_and_volume": 2,
    "total": 23,
    "valuation_rerating_runway": 1
  },
  "C16_075970_DONGKUKRNS_20230704_RARE_EARTH_EXPORT_CONTROL_POLICY_4B": {
    "direct_resource_exposure": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 3,
    "offtake_inventory_quality": 3,
    "policy_supply_shock": 8,
    "price_duration_and_volume": 3,
    "total": 26,
    "valuation_rerating_runway": 1
  },
  "C16_081150_TPLEX_20230818_RARE_METAL_POLICY_SPIKE_FALSE_GREEN": {
    "direct_resource_exposure": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "offtake_inventory_quality": 2,
    "policy_supply_shock": 7,
    "price_duration_and_volume": 3,
    "total": 25,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C16 guard:
```text
if strategic_resource_policy_attention and direct_supply_offtake_capacity_margin_bridge_visible:
    allow_stage2_actionable = true

if strategic_resource_policy_price_premium and no direct_offtake_inventory_capacity_volume_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and policy_to_company_conversion_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 081150 / 2023-08-18: rare-metal policy theme can be over-promoted if price confirmation substitutes for direct resource volume, inventory and margin proof.
- 037370 / 2023-07-25: rare-earth/magnet policy premium can become price-only when direct offtake, capacity and revision evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -34.69, "MAE_30D_pct": -18.76, "MAE_90D_pct": -34.69, "MFE_180D_pct": 28.8, "MFE_30D_pct": 28.8, "MFE_90D_pct": 28.8, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_075970_DONGKUKRNS_20230704_RARE_EARTH_EXPORT_CONTROL_POLICY_4B", "case_role": "protective_rare_earth_export_control_policy_price_premium_4b_success", "company_name": "동국알앤에스", "corporate_action_window_status": "clean_2023_2024_forward_window; corporate-action candidates are 2006-06-02, 2006-06-13, 2008-06-10, all outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B was useful when rare-earth/export-control policy attention had already been capitalized but direct offtake, inventory, processing capacity, price-duration and margin/revision evidence did not support the premium.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -49.29, "entry_date": "2023-07-04", "entry_price": 4930, "evidence_family": "rare_earth_export_control_policy_price_premium_without_direct_offtake_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "RARE_METAL_EXPORT_CONTROL_POLICY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2023-10-05", "low_price_180d": 3220, "peak_date": "2023-07-07", "peak_price": 6350, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/075/075970.json", "raw_component_score_breakdown": {"direct_resource_exposure": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 3, "offtake_inventory_quality": 3, "policy_supply_shock": 8, "price_duration_and_volume": 3, "total": 26, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C16_075970_DONGKUKRNS_20230704_RARE_EARTH_EXPORT_CONTROL_POLICY_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_or_export_control_attention", "direct_resource_supply_offtake_or_processing_capacity_required", "inventory_price_duration_volume_margin_revision_route"], "stage3_evidence_fields": ["direct_supply_chain_exposure_required", "offtake_inventory_and_price_duration_required", "processing_capacity_volume_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_policy_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_company_revenue_conversion_gap", "resource_price_duration_or_volume_failure", "margin_revision_bridge_failure"], "symbol": "075970", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/075/075970/2023.csv", "trigger_date": "2023-07-04", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -42.41, "MAE_30D_pct": -25.81, "MAE_90D_pct": -26.14, "MFE_180D_pct": 25.6, "MFE_30D_pct": 25.6, "MFE_90D_pct": 25.6, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_081150_TPLEX_20230818_RARE_METAL_POLICY_SPIKE_FALSE_GREEN", "case_role": "rare_metal_policy_theme_false_green_counterexample", "company_name": "티플랙스", "corporate_action_window_status": "clean_2023_2024_forward_window; corporate-action candidates are 2012-10-04 and 2012-10-25, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Rare-metal policy price confirmation should stay Yellow or local 4B when it lacks direct resource exposure, secured supply/offtake, inventory quality, price-duration, volume and margin/revision evidence.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -54.15, "entry_date": "2023-08-18", "entry_price": 4610, "evidence_family": "rare_metal_policy_theme_price_confirmation_without_direct_resource_volume_inventory_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "RARE_METAL_EXPORT_CONTROL_POLICY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2024-04-11", "low_price_180d": 2655, "peak_date": "2023-08-21", "peak_price": 5790, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/081/081150.json", "raw_component_score_breakdown": {"direct_resource_exposure": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "offtake_inventory_quality": 2, "policy_supply_shock": 7, "price_duration_and_volume": 3, "total": 25, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C16_081150_TPLEX_20230818_RARE_METAL_POLICY_SPIKE_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_or_export_control_attention", "direct_resource_supply_offtake_or_processing_capacity_required", "inventory_price_duration_volume_margin_revision_route"], "stage3_evidence_fields": ["direct_supply_chain_exposure_required", "offtake_inventory_and_price_duration_required", "processing_capacity_volume_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_policy_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_company_revenue_conversion_gap", "resource_price_duration_or_volume_failure", "margin_revision_bridge_failure"], "symbol": "081150", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/081/081150/2023.csv", "trigger_date": "2023-08-18", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -54.38, "MAE_30D_pct": -21.72, "MAE_90D_pct": -37.65, "MFE_180D_pct": 9.43, "MFE_30D_pct": 9.43, "MFE_90D_pct": 9.43, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_037370_EG_20230725_RARE_EARTH_MAGNET_POLICY_PREMIUM_4B", "case_role": "rare_earth_magnet_policy_price_premium_counterexample", "company_name": "EG", "corporate_action_window_status": "clean_2023_2024_forward_window; corporate-action candidates are 2000-04-24 and 2008-08-28, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Rare-earth/magnet policy premium should route to local 4B or counterexample unless direct offtake, processing capacity, price-duration, volume, inventory and margin/revision evidence keep expanding after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -58.31, "entry_date": "2023-07-25", "entry_price": 17820, "evidence_family": "rare_earth_magnet_policy_price_premium_without_direct_offtake_capacity_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "RARE_METAL_EXPORT_CONTROL_POLICY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2024-04-11", "low_price_180d": 8130, "peak_date": "2023-08-02", "peak_price": 19500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/037/037370.json", "raw_component_score_breakdown": {"direct_resource_exposure": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 3, "offtake_inventory_quality": 2, "policy_supply_shock": 7, "price_duration_and_volume": 2, "total": 23, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C16_037370_EG_20230725_RARE_EARTH_MAGNET_POLICY_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_or_export_control_attention", "direct_resource_supply_offtake_or_processing_capacity_required", "inventory_price_duration_volume_margin_revision_route"], "stage3_evidence_fields": ["direct_supply_chain_exposure_required", "offtake_inventory_and_price_duration_required", "processing_capacity_volume_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_policy_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_company_revenue_conversion_gap", "resource_price_duration_or_volume_failure", "margin_revision_bridge_failure"], "symbol": "037370", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/037/037370/2023.csv", "trigger_date": "2023-07-25", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "RARE_METAL_EXPORT_CONTROL_POLICY_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "strategic_resource_policy_supply_raremetal_export_control_new_symbols_4b_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C16 strategic-resource policy rows should block Stage3 Green when a policy/export-control headline lacks direct supply-chain exposure, secured offtake, inventory quality, processing capacity, price-duration, volume and margin/revision bridge; rare-metal policy price premiums should route to local 4B or counterexample unless non-price conversion evidence appears.",
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
3. Add C16-specific strategic-resource policy / direct exposure / offtake / inventory / processing-capacity / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C16_BLOCK_GREEN_WITHOUT_DIRECT_SUPPLY_OFFTAKE_CAPACITY_MARGIN_BRIDGE
- C16_STRATEGIC_RESOURCE_POLICY_PRICE_PREMIUM_LOCAL_4B
- C16_REQUIRE_RESOURCE_PRICE_DURATION_VOLUME_INVENTORY_REVISION
- C16_POLICY_SALIENCE_WITHOUT_COMPANY_CONVERSION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.


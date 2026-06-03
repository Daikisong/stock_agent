# E2R V12 No-Repeat Standalone Residual Research
## R4 / L4 / C16 — Strategic resource policy supply / second-wave rare-metal 4B guard

metadata:
```text
selected_round: R4
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: RARE_METAL_SECOND_WAVE_POLICY_4B_GUARD
loop_objective: coverage_gap_fill|new_trigger_family|counterexample_mining|positive_counterexample_balance|4B_refresh_second_wave_policy_premium|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_second_wave_raremetal_policy_4b_2024_research.md
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

This run uses a second-wave 2024 trigger family for 075970, 081150, and 037370.  
The hard keys are new relative to the index:
```text
C16 + 075970 + 4B-local-price-only + 2024-01-23
C16 + 081150 + Stage3-Yellow + 2024-01-23
C16 + 037370 + 4B-local-price-only + 2024-02-28
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
075970 동국알앤에스: selected 2024 forward window clean; corporate-action candidates are 2006-06-02, 2006-06-13, 2008-06-10, outside selected test window.
081150 티플랙스: selected 2024 forward window clean; corporate-action candidates are 2012-10-04 and 2012-10-25, outside selected test window.
037370 EG: selected 2024 forward window clean; corporate-action candidates are 2000-04-24 and 2008-08-28, outside selected test window.
```

## 3. Research thesis

C16 should treat strategic-resource policy shocks as a question of company-level conversion, not as automatic EPS evidence:

```text
strategic resource policy / export-control attention
→ direct supply-chain exposure
→ secured offtake, inventory or processing capacity
→ price-duration and volume
→ input cost, working capital and margin revision bridge
→ rerating or local 4B cap
```

A second policy shock is a second siren. Green should not buy the siren twice; it should buy the gate, the offtake, the inventory and the margin revision.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C16_075970_DONGKUKRNS_20240123_RARE_METAL_POLICY_SECOND_WAVE_4B | 075970 | protective_second_wave_rare_metal_policy_price_premium_4b_success | 2024-01-23 | 3605 | 4150 on 2024-05-21 | 2410 on 2024-08-06 | 13.18% | 15.12% | 15.12% | -33.15% | -41.93% |
| C16_081150_TPLEX_20240123_RARE_METAL_THEME_FALSE_GREEN | 081150 | rare_metal_theme_second_wave_false_green_counterexample | 2024-01-23 | 3240 | 3455 on 2024-01-23 | 2310 on 2024-08-05 | 6.64% | 6.64% | 6.64% | -28.7% | -33.14% |
| C16_037370_EG_20240228_RARE_EARTH_MAGNET_POLICY_4B | 037370 | rare_earth_magnet_policy_second_wave_price_premium_counterexample | 2024-02-28 | 10090 | 10570 on 2024-02-28 | 6310 on 2024-08-05 | 4.76% | 4.76% | 4.76% | -37.46% | -40.3% |

## 5. Stage evidence split

### Stage2 / Stage3
- No row in this MD is counted as a clean Stage2/Green positive.
- C16 Green should require direct supply-chain exposure, secured offtake, inventory quality, processing capacity, price-duration, volume and margin/revision confirmation.
- 081150 is the false-Green/Yellow guard: the 2024 price confirmation did not prevent a large forward MAE once direct resource conversion evidence failed to refresh.

### 4B
- 075970 is the protective 4B anchor. It had a meaningful second-wave MFE, but the post-peak drawdown confirms that rare-metal policy price heat needed non-price conversion evidence.
- 037370 is the rare-earth/magnet premium counterexample. The trigger produced a modest MFE and then a much larger forward MAE as the direct offtake/capacity/revision bridge failed to refresh.
- The core 4B rule is that second-wave policy salience must not be substituted for company-level inventory, offtake, processing capacity and margin proof.

### 4C
- No hard contract cancellation, mine/resource impairment or accounting break is asserted.
- The C16 break mode is policy-to-company conversion failure: the geopolitical supply issue can remain real while the listed company fails to convert it into durable revenue and revisions.

## 6. Raw component score breakdown

```json
{
  "C16_037370_EG_20240228_RARE_EARTH_MAGNET_POLICY_4B": {
    "direct_resource_exposure": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 3,
    "offtake_inventory_quality": 2,
    "policy_supply_shock": 7,
    "price_duration_and_volume": 2,
    "processing_capacity": 2,
    "total": 25,
    "valuation_rerating_runway": 1
  },
  "C16_075970_DONGKUKRNS_20240123_RARE_METAL_POLICY_SECOND_WAVE_4B": {
    "direct_resource_exposure": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 3,
    "offtake_inventory_quality": 3,
    "policy_supply_shock": 8,
    "price_duration_and_volume": 3,
    "processing_capacity": 3,
    "total": 29,
    "valuation_rerating_runway": 1
  },
  "C16_081150_TPLEX_20240123_RARE_METAL_THEME_FALSE_GREEN": {
    "direct_resource_exposure": 3,
    "information_confidence": 3,
    "margin_revision_bridge": 2,
    "market_mispricing": 4,
    "offtake_inventory_quality": 2,
    "policy_supply_shock": 7,
    "price_duration_and_volume": 2,
    "processing_capacity": 2,
    "total": 26,
    "valuation_rerating_runway": 1
  }
}
```

## 7. Current calibrated profile stress test

Suggested C16 guard:
```text
if strategic_resource_policy_attention and direct_supply_offtake_capacity_margin_bridge_visible:
    allow_stage2_actionable = true

if second_wave_resource_policy_price_premium and no direct_offtake_inventory_capacity_volume_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and policy_to_company_conversion_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 081150 / 2024-01-23: second-wave rare-metal policy confirmation can be over-promoted if price movement substitutes for direct resource volume, inventory and margin proof.
- 037370 / 2024-02-28: rare-earth/magnet policy premium can become price-only when direct offtake, capacity and revision evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -33.15, "MAE_30D_pct": -4.3, "MAE_90D_pct": -13.04, "MFE_180D_pct": 15.12, "MFE_30D_pct": 13.18, "MFE_90D_pct": 15.12, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_075970_DONGKUKRNS_20240123_RARE_METAL_POLICY_SECOND_WAVE_4B", "case_role": "protective_second_wave_rare_metal_policy_price_premium_4b_success", "company_name": "동국알앤에스", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2006-06-02, 2006-06-13, 2008-06-10, all outside selected test window", "current_profile_error": false, "current_profile_verdict": "Local 4B remained useful in the 2024 second-wave rare-metal policy rally. The price could spike again, but direct offtake, inventory, processing capacity, price-duration and margin/revision evidence still did not justify Stage3 Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.93, "entry_date": "2024-01-23", "entry_price": 3605, "evidence_family": "second_wave_rare_metal_policy_price_premium_without_direct_offtake_inventory_capacity_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "RARE_METAL_SECOND_WAVE_POLICY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2024-08-06", "low_price_180d": 2410, "peak_date": "2024-05-21", "peak_price": 4150, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/075/075970.json", "raw_component_score_breakdown": {"direct_resource_exposure": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 3, "offtake_inventory_quality": 3, "policy_supply_shock": 8, "price_duration_and_volume": 3, "processing_capacity": 3, "total": 29, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C16_075970_DONGKUKRNS_20240123_RARE_METAL_POLICY_SECOND_WAVE_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_or_export_control_attention", "direct_supply_chain_exposure_required", "offtake_inventory_processing_capacity_margin_revision_route"], "stage3_evidence_fields": ["direct_resource_supply_chain_exposure_required", "secured_offtake_inventory_quality_and_processing_capacity_required", "resource_price_duration_volume_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_policy_second_wave_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_company_revenue_conversion_gap", "resource_price_duration_or_volume_failure", "margin_revision_bridge_failure"], "symbol": "075970", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/075/075970/2024.csv", "trigger_date": "2024-01-23", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -28.7, "MAE_30D_pct": -3.7, "MAE_90D_pct": -18.06, "MFE_180D_pct": 6.64, "MFE_30D_pct": 6.64, "MFE_90D_pct": 6.64, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_081150_TPLEX_20240123_RARE_METAL_THEME_FALSE_GREEN", "case_role": "rare_metal_theme_second_wave_false_green_counterexample", "company_name": "티플랙스", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2012-10-04 and 2012-10-25, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Rare-metal theme price confirmation should remain Yellow or local 4B when the company-level bridge from policy salience to secured supply, inventory, volume and margin revisions is absent.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -33.14, "entry_date": "2024-01-23", "entry_price": 3240, "evidence_family": "second_wave_rare_metal_theme_price_confirmation_without_direct_resource_volume_inventory_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "RARE_METAL_SECOND_WAVE_POLICY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2024-08-05", "low_price_180d": 2310, "peak_date": "2024-01-23", "peak_price": 3455, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/081/081150.json", "raw_component_score_breakdown": {"direct_resource_exposure": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 4, "offtake_inventory_quality": 2, "policy_supply_shock": 7, "price_duration_and_volume": 2, "processing_capacity": 2, "total": 26, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C16_081150_TPLEX_20240123_RARE_METAL_THEME_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_or_export_control_attention", "direct_supply_chain_exposure_required", "offtake_inventory_processing_capacity_margin_revision_route"], "stage3_evidence_fields": ["direct_resource_supply_chain_exposure_required", "secured_offtake_inventory_quality_and_processing_capacity_required", "resource_price_duration_volume_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_policy_second_wave_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_company_revenue_conversion_gap", "resource_price_duration_or_volume_failure", "margin_revision_bridge_failure"], "symbol": "081150", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/081/081150/2024.csv", "trigger_date": "2024-01-23", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -37.46, "MAE_30D_pct": -10.6, "MAE_90D_pct": -25.87, "MFE_180D_pct": 4.76, "MFE_30D_pct": 4.76, "MFE_90D_pct": 4.76, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "case_id": "C16_037370_EG_20240228_RARE_EARTH_MAGNET_POLICY_4B", "case_role": "rare_earth_magnet_policy_second_wave_price_premium_counterexample", "company_name": "EG", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2000-04-24 and 2008-08-28, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Rare-earth/magnet policy premium should route to local 4B or counterexample unless direct offtake, processing capacity, resource price duration, sales volume and margin/revision evidence refresh after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -40.3, "entry_date": "2024-02-28", "entry_price": 10090, "evidence_family": "second_wave_rare_earth_magnet_policy_premium_without_direct_offtake_processing_capacity_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "RARE_METAL_SECOND_WAVE_POLICY_4B_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "low_date_180d": "2024-08-05", "low_price_180d": 6310, "peak_date": "2024-02-28", "peak_price": 10570, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/037/037370.json", "raw_component_score_breakdown": {"direct_resource_exposure": 3, "information_confidence": 3, "margin_revision_bridge": 2, "market_mispricing": 3, "offtake_inventory_quality": 2, "policy_supply_shock": 7, "price_duration_and_volume": 2, "processing_capacity": 2, "total": 25, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C16_037370_EG_20240228_RARE_EARTH_MAGNET_POLICY_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R4", "source_proxy_only": false, "stage2_evidence_fields": ["strategic_resource_policy_or_export_control_attention", "direct_supply_chain_exposure_required", "offtake_inventory_processing_capacity_margin_revision_route"], "stage3_evidence_fields": ["direct_resource_supply_chain_exposure_required", "secured_offtake_inventory_quality_and_processing_capacity_required", "resource_price_duration_volume_margin_revision_bridge_required"], "stage4b_evidence_fields": ["strategic_resource_policy_second_wave_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["policy_to_company_revenue_conversion_gap", "resource_price_duration_or_volume_failure", "margin_revision_bridge_failure"], "symbol": "037370", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/037/037370/2024.csv", "trigger_date": "2024-02-28", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "RARE_METAL_SECOND_WAVE_POLICY_4B_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "loop_contribution_label": "strategic_resource_policy_second_wave_raremetal_2024_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R4",
  "shadow_rule_candidate": "C16 strategic-resource policy rows should block Stage3 Green when a second-wave policy/export-control spike lacks direct supply-chain exposure, secured offtake, inventory quality, processing capacity, price-duration, volume and margin/revision bridge; second-wave rare-metal policy premiums should route to local 4B or counterexample unless non-price conversion evidence refreshes.",
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
3. Add C16-specific second-wave strategic-resource policy / direct exposure / offtake / inventory / processing-capacity / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C16_BLOCK_GREEN_WITHOUT_DIRECT_SUPPLY_OFFTAKE_CAPACITY_MARGIN_BRIDGE
- C16_SECOND_WAVE_RESOURCE_POLICY_PRICE_PREMIUM_LOCAL_4B
- C16_REQUIRE_RESOURCE_PRICE_DURATION_VOLUME_INVENTORY_REVISION
- C16_POLICY_SALIENCE_WITHOUT_COMPANY_CONVERSION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C16_STRATEGIC_RESOURCE_POLICY_SUPPLY.


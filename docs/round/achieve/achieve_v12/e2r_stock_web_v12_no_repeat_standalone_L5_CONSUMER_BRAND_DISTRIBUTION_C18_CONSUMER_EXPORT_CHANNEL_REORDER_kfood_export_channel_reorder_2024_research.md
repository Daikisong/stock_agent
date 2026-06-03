# E2R V12 No-Repeat Standalone Residual Research
## R5 / L5 / C18 — Consumer export channel reorder / K-food margin guard

metadata:
```text
selected_round: R5
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: KFOOD_EXPORT_CHANNEL_REORDER_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_kfood_export_channel_reorder_2024_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER current coverage:
rows=74, symbols=10, date range=2023-02-10~2024-12-16, good/bad S2=20/9, 4B/4C=4/5
top covered symbols: 003230(18), 005180(12), 004370(10), 383220(8), 161890(6)
```

This run avoids those top-covered C18 symbols and adds 003960, 011150, and 017810.  
Each row uses a new `C18 + symbol + trigger_type + entry_date` hard key.

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
003960 사조대림: 2024 forward window clean; corporate-action candidates are historical and latest 2019-06-26, outside selected test window.
011150 CJ씨푸드: 2024 forward window clean; corporate-action candidate is 2002-04-22, outside selected test window.
017810 풀무원: 2024 forward window clean; corporate-action candidates are historical and latest 2019-05-07, outside selected test window.
```

## 3. Research thesis

C18 should not treat an export buzzword as durable channel reorder. It should test whether overseas attention becomes repeat orders and margin:

```text
consumer export / K-food attention
→ distributor sell-through
→ repeat reorder and channel inventory quality
→ product mix and input-cost pass-through
→ gross margin and revision bridge
→ rerating
```

Export heat is the first truck leaving the warehouse. Green should require the second and third truck: repeat reorder, clean distributor inventory and a margin invoice that survives input costs.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C18_003960_SAJO_20240201_KFOOD_EXPORT_REORDER_STAGE2 | 003960 | positive_kfood_export_channel_reorder_stage2_success_with_later_4b | 2024-02-01 | 37000 | 109900 on 2024-07-09 | 32500 on 2024-02-01 | 10.27% | 116.22% | 197.03% | -12.16% | -67.02% |
| C18_011150_CJSEAFOOD_20240614_KFOOD_SEAWEED_EXPORT_PRICE_PREMIUM_4B | 011150 | seaweed_kfood_export_theme_price_premium_counterexample | 2024-06-14 | 6320 | 6490 on 2024-06-17 | 2530 on 2024-12-09 | 2.69% | 2.69% | 2.69% | -59.97% | -61.02% |
| C18_017810_PULMUONE_20240628_FROZEN_FOOD_EXPORT_CHANNEL_4B | 017810 | frozen_food_export_channel_reorder_price_premium_counterexample | 2024-06-28 | 15900 | 17250 on 2024-06-28 | 9500 on 2024-11-12 | 8.49% | 8.49% | 8.49% | -40.25% | -44.93% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- K-food export/channel reorder can be a valid Stage2 route when distributor sell-through, repeat order, product mix and gross-margin visibility appear before the full rerating.
- 003960 is the positive anchor: the February 2024 row produced a large MFE, but after the July spike the same channel-reorder story became a 4B discipline problem because repeat reorder, channel inventory and margin evidence needed a refresh.

### Stage3 / Green
- C18 Green should require repeat reorder, distributor sell-through, channel inventory quality, input-cost pass-through, product mix, gross margin and revision confirmation.
- The model should not turn a one-shot export/theme spike into Green. Export routes can be real while the stock has already paid for several reorder cycles.

### 4B
- 011150 is the clean local 4B counterexample. The K-food/seaweed export premium had little additional forward upside and then drew down deeply as repeat sell-through and margin proof did not keep expanding.
- 017810 is the frozen/plant-based channel variant. The June 2024 price premium required evidence refresh; without it, the forward path argued for counterexample rather than fresh Green.
- 003960 also required later 4B discipline after the Stage2 win matured into a priced channel-reorder premium.

### 4C
- No hard accounting break or channel cancellation is asserted.
- The C18 break mode is reorder exhaustion: the export story remains plausible, but distributor inventory, repeat reorder, product mix, input cost, gross margin and revisions stop carrying the price already paid.

## 6. Raw component score breakdown

```json
{
  "C18_003960_SAJO_20240201_KFOOD_EXPORT_REORDER_STAGE2": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 53,
    "valuation_rerating_runway": 9,
    "visibility_quality": 10
  },
  "C18_011150_CJSEAFOOD_20240614_KFOOD_SEAWEED_EXPORT_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 1,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 25,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C18_017810_PULMUONE_20240628_FROZEN_FOOD_EXPORT_CHANNEL_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 27,
    "valuation_rerating_runway": 2,
    "visibility_quality": 6
  }
}
```

## 7. Current calibrated profile stress test

Suggested C18 guard:
```text
if consumer_export_attention and reorder_sellthrough_margin_bridge_visible:
    allow_stage2_actionable = true

if kfood_export_price_premium and no repeat_reorder_channel_inventory_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and reorder_or_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 011150 / 2024-06-14: K-food/seaweed export theme can be over-promoted if the model treats price heat as repeat reorder and margin proof.
- 017810 / 2024-06-28: frozen/plant-based global-channel premium can become price-only when channel inventory, sell-through and gross-margin evidence do not refresh.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -12.16, "MAE_30D_pct": -12.16, "MAE_90D_pct": -12.16, "MFE_180D_pct": 197.03, "MFE_30D_pct": 10.27, "MFE_90D_pct": 116.22, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_id": "C18_003960_SAJO_20240201_KFOOD_EXPORT_REORDER_STAGE2", "case_role": "positive_kfood_export_channel_reorder_stage2_success_with_later_4b", "company_name": "사조대림", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are historical and latest 2019-06-26, outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when K-food export/channel-reorder attention attached to a real margin and distribution-route story before the full rerating. Green still requires repeat reorder, distributor sell-through, channel inventory, input-cost pass-through, gross margin and revision bridge; after the July 2024 spike, the same evidence needed local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -67.02, "entry_date": "2024-02-01", "entry_price": 37000, "evidence_family": "kfood_processed_seafood_export_channel_reorder_margin_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "KFOOD_EXPORT_CHANNEL_REORDER_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2024-02-01", "low_price_180d": 32500, "peak_date": "2024-07-09", "peak_price": 109900, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/003/003960.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 11, "total": 53, "valuation_rerating_runway": 9, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C18_003960_SAJO_20240201_KFOOD_EXPORT_REORDER_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["consumer_export_channel_reorder_attention", "distributor_sellthrough_or_repeat_order_signal", "gross_margin_or_revision_bridge_visibility"], "stage3_evidence_fields": ["repeat_reorder_and_sellthrough_required", "channel_inventory_and_distributor_quality_required", "input_cost_pass_through_gross_margin_revision_required"], "stage4b_evidence_fields": ["consumer_export_channel_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["reorder_or_distributor_sellthrough_gap", "channel_inventory_or_input_cost_pressure", "gross_margin_revision_bridge_failure"], "symbol": "003960", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003960/2024.csv", "trigger_date": "2024-02-01", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -59.97, "MAE_30D_pct": -29.43, "MAE_90D_pct": -48.26, "MFE_180D_pct": 2.69, "MFE_30D_pct": 2.69, "MFE_90D_pct": 2.69, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_id": "C18_011150_CJSEAFOOD_20240614_KFOOD_SEAWEED_EXPORT_PRICE_PREMIUM_4B", "case_role": "seaweed_kfood_export_theme_price_premium_counterexample", "company_name": "CJ씨푸드", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidate is 2002-04-22, outside selected test window", "current_profile_error": true, "current_profile_verdict": "K-food/seaweed export price premium should route to local 4B or counterexample unless repeat reorder, customer/distributor sell-through, channel inventory, product mix, margin and revision evidence keep expanding after the spike.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -61.02, "entry_date": "2024-06-14", "entry_price": 6320, "evidence_family": "seaweed_kfood_export_price_premium_without_reorder_channel_inventory_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "KFOOD_EXPORT_CHANNEL_REORDER_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2024-12-09", "low_price_180d": 2530, "peak_date": "2024-06-17", "peak_price": 6490, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/011/011150.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 1, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 25, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C18_011150_CJSEAFOOD_20240614_KFOOD_SEAWEED_EXPORT_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["consumer_export_channel_reorder_attention", "distributor_sellthrough_or_repeat_order_signal", "gross_margin_or_revision_bridge_visibility"], "stage3_evidence_fields": ["repeat_reorder_and_sellthrough_required", "channel_inventory_and_distributor_quality_required", "input_cost_pass_through_gross_margin_revision_required"], "stage4b_evidence_fields": ["consumer_export_channel_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["reorder_or_distributor_sellthrough_gap", "channel_inventory_or_input_cost_pressure", "gross_margin_revision_bridge_failure"], "symbol": "011150", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011150/2024.csv", "trigger_date": "2024-06-14", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -40.25, "MAE_30D_pct": -17.3, "MAE_90D_pct": -37.04, "MFE_180D_pct": 8.49, "MFE_30D_pct": 8.49, "MFE_90D_pct": 8.49, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_id": "C18_017810_PULMUONE_20240628_FROZEN_FOOD_EXPORT_CHANNEL_4B", "case_role": "frozen_food_export_channel_reorder_price_premium_counterexample", "company_name": "풀무원", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are historical and latest 2019-05-07, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Frozen/plant-based food export-channel premium should be capped at local 4B unless export sell-through, repeat reorder, distributor inventory, product mix, gross margin and revision evidence continue to improve after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -44.93, "entry_date": "2024-06-28", "entry_price": 15900, "evidence_family": "frozen_food_global_channel_reorder_price_premium_without_sellthrough_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "KFOOD_EXPORT_CHANNEL_REORDER_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2024-11-12", "low_price_180d": 9500, "peak_date": "2024-06-28", "peak_price": 17250, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/017/017810.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 4, "total": 27, "valuation_rerating_runway": 2, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C18_017810_PULMUONE_20240628_FROZEN_FOOD_EXPORT_CHANNEL_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["consumer_export_channel_reorder_attention", "distributor_sellthrough_or_repeat_order_signal", "gross_margin_or_revision_bridge_visibility"], "stage3_evidence_fields": ["repeat_reorder_and_sellthrough_required", "channel_inventory_and_distributor_quality_required", "input_cost_pass_through_gross_margin_revision_required"], "stage4b_evidence_fields": ["consumer_export_channel_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["reorder_or_distributor_sellthrough_gap", "channel_inventory_or_input_cost_pressure", "gross_margin_revision_bridge_failure"], "symbol": "017810", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv", "trigger_date": "2024-06-28", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "KFOOD_EXPORT_CHANNEL_REORDER_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "loop_contribution_label": "consumer_export_channel_reorder_kfood_new_symbols_and_4b_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R5",
  "shadow_rule_candidate": "C18 consumer export channel-reorder rows should allow Stage2 when export channel reorder, distributor sell-through and gross-margin evidence appear before the price fully capitalizes the route, but Stage3 Green requires repeat reorder, channel inventory quality, input-cost pass-through, product mix, gross margin and revision bridge; K-food price premium without repeat sell-through proof should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C18 + symbol + trigger_type + entry_date.
3. Add C18-specific consumer export / channel reorder / distributor sell-through / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C18_STAGE2_ALLOWED_ON_REORDER_SELLTHROUGH_MARGIN_BRIDGE
- C18_GREEN_REQUIRES_REPEAT_REORDER_CHANNEL_INVENTORY_INPUT_COST_PRODUCT_MIX_REVISION
- C18_KFOOD_EXPORT_PRICE_PREMIUM_LOCAL_4B
- C18_EXPORT_THEME_WITHOUT_REPEAT_REORDER_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER.


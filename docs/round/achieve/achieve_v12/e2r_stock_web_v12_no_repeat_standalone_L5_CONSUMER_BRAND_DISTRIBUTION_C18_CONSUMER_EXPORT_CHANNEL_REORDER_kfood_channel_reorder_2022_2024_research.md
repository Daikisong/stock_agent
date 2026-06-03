# E2R V12 No-Repeat Standalone Residual Research
## R5 / L5 / C18 — Consumer export channel reorder guard

metadata:
```text
selected_round: R5
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: KFOOD_SNACK_CONDIMENT_EXPORT_CHANNEL_REORDER_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_kfood_channel_reorder_2022_2024_research.md
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

This run avoids those top-covered C18 symbols and adds 271560, 280360, and 001680.  
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
271560 오리온: corporate_action_candidate_count=0.
280360 롯데웰푸드: 2024 forward window clean; corporate-action candidates are 2019-01-04 and 2022-07-20.
001680 대상: 2024 forward window clean; corporate-action candidates are old, outside the test window.
```

## 3. Research thesis

C18 should not be a generic K-food/export-theme bucket. It should test whether overseas demand becomes repeatable channel reorder:

```text
consumer export / overseas channel attention
→ sell-through or repeat order
→ inventory and channel quality
→ export mix or pricing/margin bridge
→ revision confirmation
→ rerating
```

The guard is simple: a product can go viral once, but the model should pay for the second order. The second order is where a story becomes a shelf space business.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C18_271560_ORION_20221013_GLOBAL_SNACK_CHANNEL_REORDER_STAGE2 | 271560 | positive_channel_reorder_stage2_success | 2022-10-13 | 97400 | 147800 on 2023-05-08 | 96300 on 2022-10-14 | 15.5% | 33.37% | 51.75% | -1.13% | -21.24% |
| C18_280360_LOTTEWELLFOOD_20240604_KFOOD_EXPORT_PRICE_PREMIUM_4B | 280360 | late_export_theme_4b_counterexample | 2024-06-04 | 156900 | 208500 on 2024-06-18 | 104000 on 2024-12-09 | 32.89% | 32.89% | 32.89% | -33.72% | -50.12% |
| C18_001680_DAESANG_20240612_SAUCE_KFOOD_EXPORT_FALSE_GREEN | 001680 | false_green_counterexample | 2024-06-12 | 28400 | 30900 on 2024-06-17 | 20700 on 2024-08-29 | 8.8% | 8.8% | 8.8% | -27.11% | -33.01% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Export/channel attention is a valid routing signal when the market begins to price overseas sell-through.
- 271560 is the positive anchor: a low-MAE entry path converted into a multi-month rerating when the overseas channel story had enough durability.

### Stage3 / Green
- C18 Green should require repeat reorder, sell-through confirmation, inventory/channel quality, margin bridge, and revision confirmation.
- Price movement alone is not enough because one noisy shipment can look like a full channel, even when reorder depth is still unproven.

### 4B
- 280360 is the local 4B guard: the K-food/confectionery price premium expanded quickly, then gave back the entire move.
- A strong export theme can still be a 4B row if the evidence becomes stale while valuation keeps running.

### 4C
- 001680 is the cleaner false-Green example: sauce/K-food export attention produced a short spike, then faded as the reorder/margin bridge did not keep up.
- The break mode is not an accounting failure. It is channel-quality failure: reorder, inventory, promotion burden, and revision do not support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C18_001680_DAESANG_20240612_SAUCE_KFOOD_EXPORT_FALSE_GREEN": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 29,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  },
  "C18_271560_ORION_20221013_GLOBAL_SNACK_CHANNEL_REORDER_STAGE2": {
    "bottleneck_pricing_power": 9,
    "capital_allocation": 3,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 11,
    "total": 59,
    "valuation_rerating_runway": 10,
    "visibility_quality": 12
  },
  "C18_280360_LOTTEWELLFOOD_20240604_KFOOD_EXPORT_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 2,
    "eps_fcf_explosion": 6,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 32,
    "valuation_rerating_runway": 3,
    "visibility_quality": 6
  }
}
```

## 7. Current calibrated profile stress test

Suggested C18 guard:
```text
if consumer_export_attention and no repeat_reorder_sellthrough_inventory_margin_revision_bridge:
    cap_stage = Stage2-Actionable or Stage3-Yellow
    block_stage3_green = true

if export_theme_price_premium and no incremental_channel_evidence:
    route_to_local_4B_watch = true

if post_peak_drawdown and reorder_or_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 280360 / 2024-06-04: K-food export premium can be over-promoted if repeat-order proof is not required.
- 001680 / 2024-06-12: sauce/K-food theme heat can look like Green, but the later path argues for Yellow/counterexample.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -1.13, "MAE_30D_pct": -1.13, "MAE_90D_pct": -1.13, "MFE_180D_pct": 51.75, "MFE_30D_pct": 15.5, "MFE_90D_pct": 33.37, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_id": "C18_271560_ORION_20221013_GLOBAL_SNACK_CHANNEL_REORDER_STAGE2", "case_role": "positive_channel_reorder_stage2_success", "company_name": "오리온", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": false, "current_profile_verdict": "Stage2 was valid when overseas channel reorder and margin durability were plausible; Green still requires reorder evidence, inventory/sell-through quality, margin and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -21.24, "entry_date": "2022-10-13", "entry_price": 97400, "evidence_family": "global_snack_export_channel_reorder_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "KFOOD_SNACK_CONDIMENT_EXPORT_CHANNEL_REORDER_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2022-10-14", "low_price_180d": 96300, "peak_date": "2023-05-08", "peak_price": 147800, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/271/271560.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 9, "capital_allocation": 3, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 11, "total": 59, "valuation_rerating_runway": 10, "visibility_quality": 12}, "reuse_reason": null, "same_entry_group_id": "C18_271560_ORION_20221013_GLOBAL_SNACK_CHANNEL_REORDER_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["consumer_export_channel_attention", "sell_through_or_channel_reorder_claim", "relative_strength_or_export_mix_signal"], "stage3_evidence_fields": ["confirmed_reorder_or_repeat_sell_through_required", "inventory_and_channel_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["export_theme_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["channel_reorder_fade", "inventory_or_promotion_burden", "margin_or_revision_break"], "symbol": "271560", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/271/271560/2022.csv", "trigger_date": "2022-10-13", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -33.72, "MAE_30D_pct": -4.27, "MAE_90D_pct": -12.81, "MFE_180D_pct": 32.89, "MFE_30D_pct": 32.89, "MFE_90D_pct": 32.89, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_id": "C18_280360_LOTTEWELLFOOD_20240604_KFOOD_EXPORT_PRICE_PREMIUM_4B", "case_role": "late_export_theme_4b_counterexample", "company_name": "롯데웰푸드", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "K-food export attention can produce a sharp local MFE, but without incremental reorder, channel sell-through, margin and revision proof it should route to local 4B/counterexample rather than Green.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -50.12, "entry_date": "2024-06-04", "entry_price": 156900, "evidence_family": "kfood_confectionery_export_theme_price_premium_without_reorder_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "KFOOD_SNACK_CONDIMENT_EXPORT_CHANNEL_REORDER_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2024-12-09", "low_price_180d": 104000, "peak_date": "2024-06-18", "peak_price": 208500, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/280/280360.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 2, "eps_fcf_explosion": 6, "information_confidence": 3, "market_mispricing": 5, "total": 32, "valuation_rerating_runway": 3, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C18_280360_LOTTEWELLFOOD_20240604_KFOOD_EXPORT_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["consumer_export_channel_attention", "sell_through_or_channel_reorder_claim", "relative_strength_or_export_mix_signal"], "stage3_evidence_fields": ["confirmed_reorder_or_repeat_sell_through_required", "inventory_and_channel_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["export_theme_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["channel_reorder_fade", "inventory_or_promotion_burden", "margin_or_revision_break"], "symbol": "280360", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv", "trigger_date": "2024-06-04", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -27.11, "MAE_30D_pct": -15.49, "MAE_90D_pct": -27.11, "MFE_180D_pct": 8.8, "MFE_30D_pct": 8.8, "MFE_90D_pct": 8.8, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "case_id": "C18_001680_DAESANG_20240612_SAUCE_KFOOD_EXPORT_FALSE_GREEN", "case_role": "false_green_counterexample", "company_name": "대상", "corporate_action_window_status": "clean_180d_by_profile_or_outside_candidate_dates", "current_profile_error": true, "current_profile_verdict": "Sauce/K-food export theme strength should stay Yellow if channel reorder, inventory normalization, and margin/revision bridge are not confirmed.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -33.01, "entry_date": "2024-06-12", "entry_price": 28400, "evidence_family": "sauce_kfood_export_theme_without_reorder_inventory_margin_bridge", "evidence_url_pending": false, "fine_archetype_id": "KFOOD_SNACK_CONDIMENT_EXPORT_CHANNEL_REORDER_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2024-08-29", "low_price_180d": 20700, "peak_date": "2024-06-17", "peak_price": 30900, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/001/001680.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 29, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C18_001680_DAESANG_20240612_SAUCE_KFOOD_EXPORT_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["consumer_export_channel_attention", "sell_through_or_channel_reorder_claim", "relative_strength_or_export_mix_signal"], "stage3_evidence_fields": ["confirmed_reorder_or_repeat_sell_through_required", "inventory_and_channel_quality_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["export_theme_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["channel_reorder_fade", "inventory_or_promotion_burden", "margin_or_revision_break"], "symbol": "001680", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001680/2024.csv", "trigger_date": "2024-06-12", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "KFOOD_SNACK_CONDIMENT_EXPORT_CHANNEL_REORDER_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "loop_contribution_label": "consumer_export_channel_reorder_new_symbols_and_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R5",
  "shadow_rule_candidate": "C18 consumer export/channel-reorder rerating should allow Stage2 on export/channel attention, but Stage3 Green requires repeat reorder, sell-through, inventory quality, margin and revision bridge; K-food price premium without reorder proof should route to local 4B or counterexample.",
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
3. Add C18-specific reorder/sell-through/inventory/margin bridge logic only as a shadow candidate until more rows exist.

Candidate rule:
- C18_GREEN_REQUIRES_REPEAT_REORDER_SELLTHROUGH_INVENTORY_MARGIN_REVISION
- C18_KFOOD_EXPORT_PRICE_PREMIUM_LOCAL_4B
- C18_THEME_WITHOUT_CHANNEL_REORDER_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C18_CONSUMER_EXPORT_CHANNEL_REORDER.


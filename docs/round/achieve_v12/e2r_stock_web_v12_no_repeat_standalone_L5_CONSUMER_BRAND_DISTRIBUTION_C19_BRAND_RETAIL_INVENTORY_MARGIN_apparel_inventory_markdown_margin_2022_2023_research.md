# E2R V12 No-Repeat Standalone Residual Research
## R5 / L5 / C19 — Brand retail inventory / markdown margin guard

metadata:
```text
selected_round: R5
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_BRAND_RETAIL_INVENTORY_MARKDOWN_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_apparel_inventory_markdown_margin_2022_2023_research.md
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Prompt / no-repeat basis

This MD follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as a standalone historical residual research artifact.  
`V12_Research_No_Repeat_Index.md` is used only for duplicate avoidance and coverage-gap selection.

No-Repeat selection:
```text
C19_BRAND_RETAIL_INVENTORY_MARGIN current coverage:
rows=39, symbols=8, date range=2022-05-16~2024-10-02, good/bad S2=8/8, 4B/4C=7/4
top covered symbols: UNKNOWN_SYMBOL(8), 036620(6), 298540(6), 383220(6), 337930(5)
```

This run avoids those top-covered C19 symbols and adds 081660, 020000, and 093050.  
Each row uses a new `C19 + symbol + trigger_type + entry_date` hard key.

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
081660 휠라홀딩스: 2023 forward window clean; corporate-action candidate is 2018-05-09, outside selected test window.
020000 한섬: 2022 forward window clean; corporate-action candidates are old and outside selected test window.
093050 LF: corporate_action_candidate_count=0.
```

## 3. Research thesis

C19 should not treat retail recovery as immediate margin recovery. It should test whether the store shelf becomes clean inventory and durable gross margin:

```text
brand / retail / apparel recovery attention
→ sell-through and channel inventory cleanup
→ inventory age and markdown cadence
→ channel mix and pricing discipline
→ gross margin and revision bridge
→ rerating
```

Inventory is a closet. Sales can look fine while the closet is full. Green should require evidence that the closet is emptying without burning gross margin.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C19_081660_FILA_20230102_BRAND_INVENTORY_MARGIN_STAGE2 | 081660 | positive_brand_inventory_margin_stage2_success_with_later_refresh_required | 2023-01-02 | 33450 | 40900 on 2023-03-02 | 32250 on 2023-01-02 | 19.13% | 22.27% | 22.27% | -3.59% | -16.75% |
| C19_020000_HANSOM_20220513_PREMIUM_APPAREL_MARKDOWN_FALSE_GREEN | 020000 | premium_apparel_inventory_markdown_false_green_counterexample | 2022-05-13 | 39200 | 39700 on 2022-05-13 | 24350 on 2022-09-28 | 1.28% | 1.28% | 1.28% | -37.88% | -38.66% |
| C19_093050_LF_20220725_APPAREL_CHANNEL_INVENTORY_4B | 093050 | apparel_channel_inventory_margin_price_premium_counterexample | 2022-07-25 | 17650 | 17700 on 2022-07-25 | 14400 on 2022-10-26 | 0.28% | 0.28% | 0.28% | -18.41% | -18.64% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Brand inventory normalization and margin recovery can be a valid Stage2 route when sell-through and channel inventory cleanup appear before valuation fully prices the recovery.
- 081660 is the positive anchor: early 2023 brand/inventory normalization gave a usable MFE with controlled early MAE. It still required later evidence refresh because the margin thesis was only as strong as the next channel-inventory and markdown update.

### Stage3 / Green
- C19 Green should require repeat sell-through, inventory age, markdown cadence, channel mix, gross margin and revision confirmation.
- 020000 shows why premium-apparel reopening or sales recovery language should stay Yellow when the stock has already priced recovery but inventory and markdown evidence are not carrying the margin bridge.

### 4B
- 093050 is the local 4B counterexample. Apparel/channel inventory premium had almost no forward upside and rolled into drawdown once sell-through and gross-margin proof did not arrive.
- 020000 also behaves like a false-Green-to-4B row: price was near the local peak, while the forward path punished missing inventory-quality evidence.

### 4C
- No hard accounting break or inventory write-down event is asserted.
- The C19 break mode is markdown pressure: the brand remains real, but inventory age, channel cleanup, markdown cadence, gross margin and revisions do not support the valuation already paid.

## 6. Raw component score breakdown

```json
{
  "C19_020000_HANSOM_20220513_PREMIUM_APPAREL_MARKDOWN_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 26,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  },
  "C19_081660_FILA_20230102_BRAND_INVENTORY_MARGIN_STAGE2": {
    "bottleneck_pricing_power": 7,
    "capital_allocation": 3,
    "eps_fcf_explosion": 8,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 50,
    "valuation_rerating_runway": 8,
    "visibility_quality": 10
  },
  "C19_093050_LF_20220725_APPAREL_CHANNEL_INVENTORY_4B": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 4,
    "information_confidence": 3,
    "market_mispricing": 4,
    "total": 25,
    "valuation_rerating_runway": 2,
    "visibility_quality": 5
  }
}
```

## 7. Current calibrated profile stress test

Suggested C19 guard:
```text
if brand_inventory_recovery_attention and sell_through_channel_cleanup_margin_bridge_visible:
    allow_stage2_actionable = true

if apparel_inventory_margin_price_premium and no repeat_sellthrough_inventory_age_markdown_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and markdown_or_inventory_quality_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 020000 / 2022-05-13: premium apparel reopening can be over-promoted if the model treats sales recovery as inventory-quality and gross-margin proof.
- 093050 / 2022-07-25: apparel channel-inventory price premium can become price-only when sell-through, markdown cadence and revision evidence are not refreshed.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -3.59, "MAE_30D_pct": -3.59, "MAE_90D_pct": -3.59, "MFE_180D_pct": 22.27, "MFE_30D_pct": 19.13, "MFE_90D_pct": 22.27, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "C19_081660_FILA_20230102_BRAND_INVENTORY_MARGIN_STAGE2", "case_role": "positive_brand_inventory_margin_stage2_success_with_later_refresh_required", "company_name": "휠라홀딩스", "corporate_action_window_status": "clean_2023_forward_window; corporate-action candidate is 2018-05-09 and outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when brand inventory normalization, channel cleanup and margin recovery plausibly connected to a rerating path. Green still requires sell-through, channel inventory, markdown intensity, gross margin and revision bridge.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -16.75, "entry_date": "2023-01-02", "entry_price": 33450, "evidence_family": "global_brand_inventory_normalization_margin_mix_reopening_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "APPAREL_BRAND_RETAIL_INVENTORY_MARKDOWN_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2023-01-02", "low_price_180d": 32250, "peak_date": "2023-03-02", "peak_price": 40900, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/081/081660.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 7, "capital_allocation": 3, "eps_fcf_explosion": 8, "information_confidence": 4, "market_mispricing": 10, "total": 50, "valuation_rerating_runway": 8, "visibility_quality": 10}, "reuse_reason": null, "same_entry_group_id": "C19_081660_FILA_20230102_BRAND_INVENTORY_MARGIN_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["brand_retail_or_apparel_inventory_attention", "sell_through_or_channel_inventory_cleanup_claim", "gross_margin_or_markdown_improvement_signal"], "stage3_evidence_fields": ["repeat_sell_through_required", "inventory_age_and_markdown_cadence_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["brand_retail_inventory_margin_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["sell_through_or_channel_inventory_gap", "markdown_pressure_or_inventory_write_down_risk", "gross_margin_revision_bridge_failure"], "symbol": "081660", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/081/081660/2023.csv", "trigger_date": "2023-01-02", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -37.88, "MAE_30D_pct": -21.81, "MAE_90D_pct": -37.88, "MFE_180D_pct": 1.28, "MFE_30D_pct": 1.28, "MFE_90D_pct": 1.28, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "C19_020000_HANSOM_20220513_PREMIUM_APPAREL_MARKDOWN_FALSE_GREEN", "case_role": "premium_apparel_inventory_markdown_false_green_counterexample", "company_name": "한섬", "corporate_action_window_status": "clean_2022_forward_window; corporate-action candidates are old and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Premium apparel reopening or brand-sales attention should stay Yellow if sell-through, inventory aging, markdown pressure, gross margin and revision evidence do not keep improving after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -38.66, "entry_date": "2022-05-13", "entry_price": 39200, "evidence_family": "premium_apparel_reopening_sales_price_premium_without_inventory_markdown_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "APPAREL_BRAND_RETAIL_INVENTORY_MARKDOWN_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2022-09-28", "low_price_180d": 24350, "peak_date": "2022-05-13", "peak_price": 39700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/020/020000.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 5, "total": 26, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C19_020000_HANSOM_20220513_PREMIUM_APPAREL_MARKDOWN_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["brand_retail_or_apparel_inventory_attention", "sell_through_or_channel_inventory_cleanup_claim", "gross_margin_or_markdown_improvement_signal"], "stage3_evidence_fields": ["repeat_sell_through_required", "inventory_age_and_markdown_cadence_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["brand_retail_inventory_margin_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["sell_through_or_channel_inventory_gap", "markdown_pressure_or_inventory_write_down_risk", "gross_margin_revision_bridge_failure"], "symbol": "020000", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020000/2022.csv", "trigger_date": "2022-05-13", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -18.41, "MAE_30D_pct": -7.93, "MAE_90D_pct": -18.41, "MFE_180D_pct": 0.28, "MFE_30D_pct": 0.28, "MFE_90D_pct": 0.28, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "C19_093050_LF_20220725_APPAREL_CHANNEL_INVENTORY_4B", "case_role": "apparel_channel_inventory_margin_price_premium_counterexample", "company_name": "LF", "corporate_action_window_status": "corporate_action_candidate_count=0", "current_profile_error": true, "current_profile_verdict": "Apparel/channel inventory recovery price premium should route to local 4B or counterexample unless sell-through, inventory quality, markdown cadence, channel mix and margin/revision bridge remain visible.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -18.64, "entry_date": "2022-07-25", "entry_price": 17650, "evidence_family": "apparel_channel_inventory_price_premium_without_sellthrough_markdown_margin_revision", "evidence_url_pending": false, "fine_archetype_id": "APPAREL_BRAND_RETAIL_INVENTORY_MARKDOWN_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2022-10-26", "low_price_180d": 14400, "peak_date": "2022-07-25", "peak_price": 17700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/093/093050.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 4, "information_confidence": 3, "market_mispricing": 4, "total": 25, "valuation_rerating_runway": 2, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C19_093050_LF_20220725_APPAREL_CHANNEL_INVENTORY_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["brand_retail_or_apparel_inventory_attention", "sell_through_or_channel_inventory_cleanup_claim", "gross_margin_or_markdown_improvement_signal"], "stage3_evidence_fields": ["repeat_sell_through_required", "inventory_age_and_markdown_cadence_required", "gross_margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["brand_retail_inventory_margin_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["sell_through_or_channel_inventory_gap", "markdown_pressure_or_inventory_write_down_risk", "gross_margin_revision_bridge_failure"], "symbol": "093050", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/093/093050/2022.csv", "trigger_date": "2022-07-25", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "APPAREL_BRAND_RETAIL_INVENTORY_MARKDOWN_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "loop_contribution_label": "brand_retail_inventory_margin_apparel_new_symbols_and_markdown_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R5",
  "shadow_rule_candidate": "C19 brand-retail inventory-margin rows should allow Stage2 on early sell-through/channel-inventory cleanup and gross-margin recovery evidence, but Stage3 Green requires repeat sell-through, inventory age, markdown cadence, channel mix, gross margin and revision bridge; apparel price premium without inventory-quality proof should route to local 4B or counterexample.",
  "source_proxy_only_count": 0
}
```


## 10. Deferred Coding Agent Handoff Prompt

Do not execute this handoff inside the research session.

```text
Read this standalone v12 residual research MD.
Before batch apply:
1. Verify all OHLC rows again from Songdaiki/stock-web tradable shards.
2. Check no hard duplicate exists for C19 + symbol + trigger_type + entry_date.
3. Add C19-specific brand-retail / inventory-age / markdown / gross-margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C19_STAGE2_ALLOWED_ON_SELLTHROUGH_CHANNEL_INVENTORY_CLEANUP_MARGIN_BRIDGE
- C19_GREEN_REQUIRES_REPEAT_SELLTHROUGH_INVENTORY_AGE_MARKDOWN_GROSS_MARGIN_REVISION
- C19_APPAREL_INVENTORY_MARGIN_PRICE_PREMIUM_LOCAL_4B
- C19_MARKDOWN_PRESSURE_WITHOUT_MARGIN_REVISION_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.


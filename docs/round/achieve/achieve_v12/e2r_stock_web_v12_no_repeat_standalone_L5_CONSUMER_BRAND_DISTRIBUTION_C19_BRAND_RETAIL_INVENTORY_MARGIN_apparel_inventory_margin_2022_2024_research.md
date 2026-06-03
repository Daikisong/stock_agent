# E2R V12 No-Repeat Standalone Residual Research
## R5 / L5 / C19 — Brand retail inventory-margin guard

metadata:
```text
selected_round: R5
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_INVENTORY_MARKDOWN_REORDER_MARGIN_GUARD
loop_objective: coverage_gap_fill|counterexample_mining|positive_counterexample_balance|4B_non_price_requirement_stress_test|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_apparel_inventory_margin_2022_2024_research.md
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

This run avoids those top-covered C19 symbols and adds 111770, 020000, and 081660.  
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
111770 영원무역: corporate_action_candidate_count=0.
020000 한섬: 2022 forward window clean; corporate-action candidates are old, outside the test window.
081660 휠라홀딩스: 2024 forward window clean; corporate-action candidate is 2018-05-09, outside the test window.
```

## 3. Research thesis

C19 should not be a generic consumer brand bucket. It should test whether inventory cleanup becomes margin power:

```text
brand / apparel / retail inventory normalization
→ sell-through and inventory turn
→ markdown discipline and channel mix
→ wholesale reorder or replenishment
→ margin and revision bridge
→ rerating
```

The important distinction is between clearing a closet and refilling a shelf. A one-time inventory cleanout can lift sentiment, but durable rerating needs reorder, not just relief.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C19_111770_YOUNGONE_20230515_APPAREL_OEM_INVENTORY_MARGIN_STAGE2 | 111770 | positive_inventory_margin_stage2_success_with_later_4b | 2023-05-15 | 47500 | 66700 on 2023-06-30 | 43550 on 2023-11-30 | 36.84% | 40.42% | 40.42% | -8.32% | -34.71% |
| C19_020000_HANDSOME_20220511_FASHION_REOPENING_INVENTORY_FALSE_GREEN | 020000 | fashion_reopening_inventory_false_green_counterexample | 2022-05-11 | 39100 | 39700 on 2022-05-13 | 23750 on 2022-10-12 | 1.53% | 1.53% | 1.53% | -39.26% | -40.18% |
| C19_081660_FILA_20240925_BRAND_INVENTORY_CLEANUP_PRICE_PREMIUM_4B | 081660 | brand_inventory_cleanup_price_premium_counterexample | 2024-09-25 | 43550 | 44950 on 2024-09-25 | 36900 on 2024-11-06 | 3.21% | 3.21% | 3.21% | -15.27% | -17.91% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Inventory normalization and margin relief can be valid Stage2 routes.
- 111770 is the positive anchor: apparel/OEM margin and inventory-normalization attention converted into a strong MFE before the evidence later aged and required 4B discipline.

### Stage3 / Green
- C19 Green should require inventory turn, sell-through, markdown discipline, channel mix, reorder, margin and revision confirmation.
- 020000 shows the reopening false-Green risk: traffic or brand quality alone does not protect the stock when inventory and markdown pressure dominate.

### 4B
- 081660 is the inventory-cleanup price-premium guard. The stock could price brand cleanup before enough reorder and margin-duration evidence arrived.
- 111770 also needed later 4B discipline after the June 2023 rerating exhausted much of the easy margin/inventory evidence.

### 4C
- No hard accounting break is asserted.
- The C19 break mode is retail execution failure: the goods exist, but sell-through, markdown discipline, channel mix, reorder, and margin revision do not pull together.

## 6. Raw component score breakdown

```json
{
  "C19_020000_HANDSOME_20220511_FASHION_REOPENING_INVENTORY_FALSE_GREEN": {
    "bottleneck_pricing_power": 5,
    "capital_allocation": 2,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 28,
    "valuation_rerating_runway": 3,
    "visibility_quality": 5
  },
  "C19_081660_FILA_20240925_BRAND_INVENTORY_CLEANUP_PRICE_PREMIUM_4B": {
    "bottleneck_pricing_power": 6,
    "capital_allocation": 3,
    "eps_fcf_explosion": 5,
    "information_confidence": 3,
    "market_mispricing": 5,
    "total": 31,
    "valuation_rerating_runway": 3,
    "visibility_quality": 6
  },
  "C19_111770_YOUNGONE_20230515_APPAREL_OEM_INVENTORY_MARGIN_STAGE2": {
    "bottleneck_pricing_power": 8,
    "capital_allocation": 3,
    "eps_fcf_explosion": 10,
    "information_confidence": 4,
    "market_mispricing": 10,
    "total": 54,
    "valuation_rerating_runway": 8,
    "visibility_quality": 11
  }
}
```

## 7. Current calibrated profile stress test

Suggested C19 guard:
```text
if brand_inventory_normalization and sellthrough_margin_bridge_visible:
    allow_stage2_actionable = true

if inventory_cleanup_price_premium and no reorder_markdown_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and inventory_turn_or_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 020000 / 2022-05-11: fashion reopening can be over-promoted if the model does not require inventory turn and markdown discipline.
- 081660 / 2024-09-25: brand cleanup premium can become price-only if reorder and margin-duration evidence are not visible.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -8.32, "MAE_30D_pct": -6.53, "MAE_90D_pct": -6.53, "MFE_180D_pct": 40.42, "MFE_30D_pct": 36.84, "MFE_90D_pct": 40.42, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "C19_111770_YOUNGONE_20230515_APPAREL_OEM_INVENTORY_MARGIN_STAGE2", "case_role": "positive_inventory_margin_stage2_success_with_later_4b", "company_name": "영원무역", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when apparel/OEM inventory normalization and margin leverage were plausible, but Green still requires sell-through, inventory turn, markdown discipline, FX/raw-material spread and revision durability.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -34.71, "entry_date": "2023-05-15", "entry_price": 47500, "evidence_family": "apparel_oem_inventory_normalization_fx_margin_revision_route", "evidence_url_pending": false, "fine_archetype_id": "APPAREL_INVENTORY_MARKDOWN_REORDER_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2023-11-30", "low_price_180d": 43550, "peak_date": "2023-06-30", "peak_price": 66700, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/111/111770.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 8, "capital_allocation": 3, "eps_fcf_explosion": 10, "information_confidence": 4, "market_mispricing": 10, "total": 54, "valuation_rerating_runway": 8, "visibility_quality": 11}, "reuse_reason": null, "same_entry_group_id": "C19_111770_YOUNGONE_20230515_APPAREL_OEM_INVENTORY_MARGIN_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["brand_or_apparel_inventory_normalization_attention", "sell_through_or_reorder_claim", "margin_or_markdown_improvement_signal"], "stage3_evidence_fields": ["inventory_turn_and_sell_through_required", "markdown_discipline_and_channel_mix_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["brand_inventory_cleanup_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["inventory_turn_failure", "markdown_or_promotion_burden", "reorder_margin_revision_break"], "symbol": "111770", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/111/111770/2023.csv", "trigger_date": "2023-05-15", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -39.26, "MAE_30D_pct": -21.61, "MAE_90D_pct": -28.01, "MFE_180D_pct": 1.53, "MFE_30D_pct": 1.53, "MFE_90D_pct": 1.53, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "C19_020000_HANDSOME_20220511_FASHION_REOPENING_INVENTORY_FALSE_GREEN", "case_role": "fashion_reopening_inventory_false_green_counterexample", "company_name": "한섬", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": true, "current_profile_verdict": "Fashion reopening and brand-retail traffic should not become Green if inventory, markdown, channel mix, and margin/revision evidence are not improving.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -40.18, "entry_date": "2022-05-11", "entry_price": 39100, "evidence_family": "fashion_reopening_retail_inventory_markdown_risk_without_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "APPAREL_INVENTORY_MARKDOWN_REORDER_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2022-10-12", "low_price_180d": 23750, "peak_date": "2022-05-13", "peak_price": 39700, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/020/020000.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 5, "capital_allocation": 2, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 28, "valuation_rerating_runway": 3, "visibility_quality": 5}, "reuse_reason": null, "same_entry_group_id": "C19_020000_HANDSOME_20220511_FASHION_REOPENING_INVENTORY_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["brand_or_apparel_inventory_normalization_attention", "sell_through_or_reorder_claim", "margin_or_markdown_improvement_signal"], "stage3_evidence_fields": ["inventory_turn_and_sell_through_required", "markdown_discipline_and_channel_mix_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["brand_inventory_cleanup_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["inventory_turn_failure", "markdown_or_promotion_burden", "reorder_margin_revision_break"], "symbol": "020000", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020000/2022.csv", "trigger_date": "2022-05-11", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -15.27, "MAE_30D_pct": -10.56, "MAE_90D_pct": -15.27, "MFE_180D_pct": 3.21, "MFE_30D_pct": 3.21, "MFE_90D_pct": 3.21, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "C19_081660_FILA_20240925_BRAND_INVENTORY_CLEANUP_PRICE_PREMIUM_4B", "case_role": "brand_inventory_cleanup_price_premium_counterexample", "company_name": "휠라홀딩스", "corporate_action_window_status": "clean_forward_window; corporate-action candidates old or outside selected test window", "current_profile_error": true, "current_profile_verdict": "Brand inventory-cleanup premium should route to local 4B or Yellow unless sell-through, markdown, wholesale reorder, channel mix and revision evidence continue to improve.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -17.91, "entry_date": "2024-09-25", "entry_price": 43550, "evidence_family": "brand_inventory_cleanup_price_premium_without_reorder_margin_revision_duration", "evidence_url_pending": false, "fine_archetype_id": "APPAREL_INVENTORY_MARKDOWN_REORDER_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2024-11-06", "low_price_180d": 36900, "peak_date": "2024-09-25", "peak_price": 44950, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/081/081660.json", "raw_component_score_breakdown": {"bottleneck_pricing_power": 6, "capital_allocation": 3, "eps_fcf_explosion": 5, "information_confidence": 3, "market_mispricing": 5, "total": 31, "valuation_rerating_runway": 3, "visibility_quality": 6}, "reuse_reason": null, "same_entry_group_id": "C19_081660_FILA_20240925_BRAND_INVENTORY_CLEANUP_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["brand_or_apparel_inventory_normalization_attention", "sell_through_or_reorder_claim", "margin_or_markdown_improvement_signal"], "stage3_evidence_fields": ["inventory_turn_and_sell_through_required", "markdown_discipline_and_channel_mix_required", "margin_or_revision_bridge_required"], "stage4b_evidence_fields": ["brand_inventory_cleanup_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["inventory_turn_failure", "markdown_or_promotion_burden", "reorder_margin_revision_break"], "symbol": "081660", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv", "trigger_date": "2024-09-25", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "APPAREL_INVENTORY_MARKDOWN_REORDER_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "loop_contribution_label": "brand_retail_inventory_margin_new_symbols_and_counterexamples",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R5",
  "shadow_rule_candidate": "C19 brand-retail inventory-margin rows should allow Stage2 on early sell-through/inventory-normalization/margin evidence, but Stage3 Green requires inventory turn, markdown discipline, channel mix, reorder, margin and revision bridge; inventory-cleanup price premium without reorder proof should route to local 4B or counterexample.",
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
3. Add C19-specific inventory-turn / sell-through / markdown / reorder / margin-revision guard only as a shadow candidate until more rows exist.

Candidate rule:
- C19_STAGE2_ALLOWED_ON_INVENTORY_NORMALIZATION_AND_MARGIN_RELIEF
- C19_GREEN_REQUIRES_INVENTORY_TURN_SELLTHROUGH_MARKDOWN_REORDER_REVISION
- C19_INVENTORY_CLEANUP_PRICE_PREMIUM_LOCAL_4B
- C19_RETAIL_REOPENING_WITHOUT_MARGIN_BRIDGE_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.


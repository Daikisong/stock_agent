# E2R V12 No-Repeat Standalone Residual Research
## R5 / L5 / C19 — Brand retail inventory-margin guard

metadata:
```text
selected_round: R5
scheduler_override_used: true
scheduled_round_inherited: false
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_BRAND_OEM_INVENTORY_MARGIN_GUARD
loop_objective: coverage_gap_fill|new_symbol_expansion|counterexample_mining|positive_counterexample_balance|4B_gap_fill|green_strictness_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_no_repeat_standalone_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_apparel_oem_inventory_guard_2023_2024_research.md
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

This run avoids those top-covered C19 symbols and adds 111770, 081660, and 241590.  
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
081660 휠라홀딩스: selected 2024/2025 forward window clean; corporate-action candidate is 2018-05-09, outside selected test window.
241590 화승엔터프라이즈: selected 2024 forward window clean; corporate-action candidates are 2018-06-08 and 2018-07-02, outside selected test window.
```

## 3. Research thesis

C19 should not treat inventory normalization as a complete margin rerating by itself. It should test whether normalized inventory becomes sell-through, customer orders and gross margin:

```text
brand / apparel inventory normalization
→ channel sell-through or OEM customer order recovery
→ product mix, input cost, FX and freight bridge
→ inventory quality and working-capital discipline
→ gross margin and revision bridge
→ rerating or local 4B cap
```

Inventory normalization is a cleared aisle in a warehouse. Green should not pay for the empty floor alone; it should require the next shipment, full-price sell-through and a margin invoice.

## 4. Case table

| case_id | symbol | role | entry | entry_price | peak | low_180d | MFE_30D | MFE_90D | MFE_180D | MAE_180D | post-peak DD |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C19_111770_YOUNGONE_20230309_APPAREL_OEM_INVENTORY_MARGIN_STAGE2 | 111770 | positive_apparel_oem_inventory_margin_stage2_success_with_later_4b_refresh | 2023-03-09 | 47450 | 67900 on 2023-08-16 | 43100 on 2023-04-07 | 1.37% | 40.57% | 43.1% | -9.17% | -30.85% |
| C19_081660_FILA_20240801_BRAND_INVENTORY_PRICE_PREMIUM_4B | 081660 | brand_inventory_margin_price_premium_counterexample | 2024-08-01 | 44450 | 44950 on 2024-09-25 | 33550 on 2025-04-09 | 0.22% | 1.12% | 1.12% | -24.52% | -25.36% |
| C19_241590_HSENTERPRISE_20241016_OEM_RESTOCK_MARGIN_FALSE_GREEN | 241590 | apparel_oem_restock_margin_false_green_counterexample | 2024-10-16 | 8990 | 9850 on 2024-11-08 | 8020 on 2024-11-21 | 9.57% | 9.57% | 9.57% | -10.79% | -18.58% |

## 5. Stage evidence split

### Stage2 / Stage2-Actionable
- Apparel/brand inventory normalization can be a valid Stage2 route when it is backed by sell-through, customer orders and gross-margin revision evidence.
- 111770 is the positive anchor. The March 2023 apparel OEM route produced a strong forward MFE as inventory normalization and order visibility converted into margin leverage. It later required 4B discipline after the August rerating because the same evidence needed fresh order and margin confirmation.

### Stage3 / Green
- C19 Green should require channel sell-through, customer order quality, inventory quality, input cost, FX/freight and revision confirmation.
- 241590 is the false-Green guard: restocking and price confirmation did not by itself prove durable utilization, labor/input-cost absorption and margin revision.

### 4B
- 081660 fills a brand inventory price-premium 4B pocket. The stock had already capitalized recovery, but sell-through and margin evidence did not refresh enough to protect the forward drawdown.
- 241590 shows the OEM restock variant: price confirmation existed, but customer-order and utilization evidence needed to be revalidated before Green.
- 111770 also transitioned from valid Stage2 to 4B watch after a strong rerating.

### 4C
- No hard inventory write-down or balance-sheet break is asserted.
- The C19 break mode is evidence exhaustion: inventory normalization remains plausible, but sell-through, customer orders, input cost, FX/freight, gross margin and revisions no longer support the price already paid.

## 6. Raw component score breakdown

```json
{
  "C19_081660_FILA_20240801_BRAND_INVENTORY_PRICE_PREMIUM_4B": {
    "channel_sellthrough_quality": 4,
    "gross_margin_bridge": 4,
    "information_confidence": 3,
    "inventory_normalization": 5,
    "market_mispricing": 3,
    "order_backlog_visibility": 3,
    "total": 23,
    "valuation_rerating_runway": 1
  },
  "C19_111770_YOUNGONE_20230309_APPAREL_OEM_INVENTORY_MARGIN_STAGE2": {
    "channel_sellthrough_quality": 7,
    "gross_margin_bridge": 9,
    "information_confidence": 4,
    "inventory_normalization": 10,
    "market_mispricing": 10,
    "order_backlog_visibility": 9,
    "total": 57,
    "valuation_rerating_runway": 8
  },
  "C19_241590_HSENTERPRISE_20241016_OEM_RESTOCK_MARGIN_FALSE_GREEN": {
    "channel_sellthrough_quality": 4,
    "gross_margin_bridge": 4,
    "information_confidence": 3,
    "inventory_normalization": 6,
    "market_mispricing": 4,
    "order_backlog_visibility": 4,
    "total": 27,
    "valuation_rerating_runway": 2
  }
}
```

## 7. Current calibrated profile stress test

Suggested C19 guard:
```text
if inventory_normalization and sellthrough_order_margin_revision_bridge_visible:
    allow_stage2_actionable = true

if brand_inventory_margin_price_premium and no incremental_sellthrough_customer_order_margin_revision_bridge:
    block_stage3_green = true
    route_to_local_4B_watch = true

if post_peak_drawdown and inventory_to_margin_bridge_fails:
    route_to_counterexample_or_4C_watch = true
```

Residual errors:
```text
current_profile_error_count = 2
- 081660 / 2024-08-01: brand inventory recovery can be over-promoted if the model treats price premium as sell-through and margin proof.
- 241590 / 2024-10-16: apparel OEM restock confirmation can look like Green, but fails without customer-order, utilization and margin bridge.
```

## 8. Machine-readable rows

```jsonl
{"MAE_180D_pct": -9.17, "MAE_30D_pct": -9.17, "MAE_90D_pct": -9.17, "MFE_180D_pct": 43.1, "MFE_30D_pct": 1.37, "MFE_90D_pct": 40.57, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "C19_111770_YOUNGONE_20230309_APPAREL_OEM_INVENTORY_MARGIN_STAGE2", "case_role": "positive_apparel_oem_inventory_margin_stage2_success_with_later_4b_refresh", "company_name": "영원무역", "corporate_action_window_status": "corporate_action_candidate_count=0; clean_2023_forward_window", "current_profile_error": false, "current_profile_verdict": "Stage2 was useful when apparel OEM inventory normalization, export order stability and margin leverage began to separate from generic consumer beta. Green still requires channel inventory, order backlog quality, FX/freight/input-cost bridge, customer concentration, gross margin and revision confirmation; after the August 2023 rerating, the same evidence required local 4B discipline.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -30.85, "entry_date": "2023-03-09", "entry_price": 47450, "evidence_family": "apparel_oem_inventory_normalization_export_order_margin_revision_stage2_route", "evidence_url_pending": false, "fine_archetype_id": "APPAREL_BRAND_OEM_INVENTORY_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2023-04-07", "low_price_180d": 43100, "peak_date": "2023-08-16", "peak_price": 67900, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/111/111770.json", "raw_component_score_breakdown": {"channel_sellthrough_quality": 7, "gross_margin_bridge": 9, "information_confidence": 4, "inventory_normalization": 10, "market_mispricing": 10, "order_backlog_visibility": 9, "total": 57, "valuation_rerating_runway": 8}, "reuse_reason": null, "same_entry_group_id": "C19_111770_YOUNGONE_20230309_APPAREL_OEM_INVENTORY_MARGIN_STAGE2", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["brand_or_apparel_inventory_normalization_attention", "channel_sellthrough_or_customer_order_visibility", "gross_margin_or_revision_route"], "stage3_evidence_fields": ["channel_inventory_and_sellthrough_required", "customer_order_or_backlog_quality_required", "input_cost_FX_freight_gross_margin_revision_bridge_required"], "stage4b_evidence_fields": ["brand_inventory_margin_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["sellthrough_or_customer_order_disappointment", "inventory_inputcost_FX_or_freight_pressure", "gross_margin_revision_bridge_failure"], "symbol": "111770", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/111/111770/2023.csv", "trigger_date": "2023-03-09", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -24.52, "MAE_30D_pct": -15.86, "MAE_90D_pct": -15.86, "MFE_180D_pct": 1.12, "MFE_30D_pct": 0.22, "MFE_90D_pct": 1.12, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "C19_081660_FILA_20240801_BRAND_INVENTORY_PRICE_PREMIUM_4B", "case_role": "brand_inventory_margin_price_premium_counterexample", "company_name": "휠라홀딩스", "corporate_action_window_status": "clean_2024_2025_forward_window; corporate-action candidate is 2018-05-09 and outside selected test window", "current_profile_error": true, "current_profile_verdict": "Brand inventory recovery price premium should route to local 4B or counterexample unless channel sell-through, wholesale inventory quality, direct-to-consumer mix, gross margin and revision evidence keep expanding after the price run.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -25.36, "entry_date": "2024-08-01", "entry_price": 44450, "evidence_family": "brand_inventory_recovery_price_premium_without_channel_sellthrough_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "APPAREL_BRAND_OEM_INVENTORY_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2025-04-09", "low_price_180d": 33550, "peak_date": "2024-09-25", "peak_price": 44950, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/081/081660.json", "raw_component_score_breakdown": {"channel_sellthrough_quality": 4, "gross_margin_bridge": 4, "information_confidence": 3, "inventory_normalization": 5, "market_mispricing": 3, "order_backlog_visibility": 3, "total": 23, "valuation_rerating_runway": 1}, "reuse_reason": null, "same_entry_group_id": "C19_081660_FILA_20240801_BRAND_INVENTORY_PRICE_PREMIUM_4B", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["brand_or_apparel_inventory_normalization_attention", "channel_sellthrough_or_customer_order_visibility", "gross_margin_or_revision_route"], "stage3_evidence_fields": ["channel_inventory_and_sellthrough_required", "customer_order_or_backlog_quality_required", "input_cost_FX_freight_gross_margin_revision_bridge_required"], "stage4b_evidence_fields": ["brand_inventory_margin_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["sellthrough_or_customer_order_disappointment", "inventory_inputcost_FX_or_freight_pressure", "gross_margin_revision_bridge_failure"], "symbol": "081660", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv", "trigger_date": "2024-08-01", "trigger_type": "4B-local-price-only", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -10.79, "MAE_30D_pct": -10.79, "MAE_90D_pct": -7.56, "MFE_180D_pct": 9.57, "MFE_30D_pct": 9.57, "MFE_90D_pct": 9.57, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "case_id": "C19_241590_HSENTERPRISE_20241016_OEM_RESTOCK_MARGIN_FALSE_GREEN", "case_role": "apparel_oem_restock_margin_false_green_counterexample", "company_name": "화승엔터프라이즈", "corporate_action_window_status": "clean_2024_forward_window; corporate-action candidates are 2018-06-08 and 2018-07-02, outside selected test window", "current_profile_error": true, "current_profile_verdict": "Apparel OEM restocking and margin recovery should stay Yellow when price confirmation is not followed by durable customer order, utilization, labor/input-cost, inventory and revision evidence. The later drawdown shows why restocking beta should not substitute for margin proof.", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -18.58, "entry_date": "2024-10-16", "entry_price": 8990, "evidence_family": "apparel_oem_restock_price_confirmation_without_customer_order_utilization_margin_revision_bridge", "evidence_url_pending": false, "fine_archetype_id": "APPAREL_BRAND_OEM_INVENTORY_MARGIN_GUARD", "forward_window_trading_days": 180, "independent_evidence_weight": 1.0, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "low_date_180d": "2024-11-21", "low_price_180d": 8020, "peak_date": "2024-11-08", "peak_price": 9850, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_path": "atlas/symbol_profiles/241/241590.json", "raw_component_score_breakdown": {"channel_sellthrough_quality": 4, "gross_margin_bridge": 4, "information_confidence": 3, "inventory_normalization": 6, "market_mispricing": 4, "order_backlog_visibility": 4, "total": 27, "valuation_rerating_runway": 2}, "reuse_reason": null, "same_entry_group_id": "C19_241590_HSENTERPRISE_20241016_OEM_RESTOCK_MARGIN_FALSE_GREEN", "schema_version": "v12_no_repeat_standalone_trigger_row_v1", "selected_round": "R5", "source_proxy_only": false, "stage2_evidence_fields": ["brand_or_apparel_inventory_normalization_attention", "channel_sellthrough_or_customer_order_visibility", "gross_margin_or_revision_route"], "stage3_evidence_fields": ["channel_inventory_and_sellthrough_required", "customer_order_or_backlog_quality_required", "input_cost_FX_freight_gross_margin_revision_bridge_required"], "stage4b_evidence_fields": ["brand_inventory_margin_price_premium", "valuation_or_positioning_overheat", "post_peak_drawdown"], "stage4c_evidence_fields": ["sellthrough_or_customer_order_disappointment", "inventory_inputcost_FX_or_freight_pressure", "gross_margin_revision_bridge_failure"], "symbol": "241590", "tradable_shard_path": "atlas/ohlcv_tradable_by_symbol_year/241/241590/2024.csv", "trigger_date": "2024-10-16", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
```

## 9. Aggregate row

```json
{
  "calibration_usable_case_count": 3,
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "evidence_url_pending_count": 0,
  "fine_archetype_id": "APPAREL_BRAND_OEM_INVENTORY_MARGIN_GUARD",
  "hard_duplicate_avoided": true,
  "index_update_needed": true,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "loop_contribution_label": "brand_retail_inventory_margin_apparel_oem_new_symbols_4b_false_green_guard",
  "new_independent_case_count": 3,
  "positive_case_count": 1,
  "reused_case_count": 0,
  "schema_version": "v12_no_repeat_standalone_aggregate_v1",
  "selected_round": "R5",
  "shadow_rule_candidate": "C19 brand/retail inventory-margin rows should allow Stage2 when inventory normalization is backed by channel sell-through, customer order visibility and gross-margin/revision bridge, but Stage3 Green requires sell-through, inventory quality, input-cost/FX/freight bridge and margin revision confirmation; brand inventory price premium without incremental sell-through or margin proof should route to local 4B or counterexample.",
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
3. Add C19-specific brand/apparel inventory / sell-through / customer-order / margin-revision / local-4B guard only as a shadow candidate until more rows exist.

Candidate rule:
- C19_STAGE2_ALLOWED_ON_INVENTORY_SELLTHROUGH_ORDER_MARGIN_REVISION_BRIDGE
- C19_GREEN_REQUIRES_CHANNEL_SELLTHROUGH_INPUT_COST_FX_FREIGHT_MARGIN_REVISION
- C19_BRAND_INVENTORY_MARGIN_PRICE_PREMIUM_LOCAL_4B
- C19_RESTOCK_WITHOUT_CUSTOMER_ORDER_MARGIN_COUNTEREXAMPLE

Do not lower global Stage3 Green thresholds.
Do not treat this single MD as production-ready.
```

## 11. Final contribution line

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.


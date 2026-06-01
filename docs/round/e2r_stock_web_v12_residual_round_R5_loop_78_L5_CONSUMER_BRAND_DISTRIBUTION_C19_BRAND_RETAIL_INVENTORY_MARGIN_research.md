# E2R Stock-Web v12 Residual Research — R5 Loop 78 / L5 / C19

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 78,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 78,
  "computed_next_round": "R6",
  "computed_next_loop": 78,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "fine_archetype_id": "RETAIL_APPAREL_INVENTORY_NORMALIZATION_CHANNEL_PRODUCTIVITY_MARGIN_BRIDGE_VS_APPAREL_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "brand_retail_inventory_margin_guardrail",
    "inventory_normalization_channel_productivity_margin_bridge",
    "apparel_OEM_brand_inventory_fade_boundary",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## Execution compliance note

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R4 / loop 78.

Therefore:

```text
scheduled_round = R5
scheduled_loop = 78
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
computed_next_round = R6
computed_next_loop = 78
```

R5 was routed to C19 because loop 77 used C18 and C20 remains heavily covered.  
This file tests retail/apparel inventory normalization and channel productivity rather than consumer export reorder or beauty/global distribution.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C19 is concentrated in:

```text
UNKNOWN_SYMBOL, 036620, 298540, 383220, 337930
```

This run uses three different symbols:

```text
023530 / 롯데쇼핑 / large-cap retail inventory-normalization lifecycle candidate
111770 / 영원무역 / apparel OEM inventory-margin fade
306040 / 에스제이그룹 / fashion-brand inventory-turnaround fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C19 is not “브랜드주가 올랐다.”

The mechanism must pass through:

```text
inventory normalization
→ channel productivity and sell-through
→ reorder or markdown control
→ cost discipline
→ margin conversion
→ durable rerating
```

브랜드 재고는 창고 안의 상자다.  
C19가 보려는 것은 그 상자가 실제 매장에서 팔리고, 할인율이 낮아지고, 다시 주문되고, 마진으로 돌아오는지다.

---

## Case 1 — Slow positive with lifecycle 4B: 023530 / 롯데쇼핑

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is retail inventory turnover, channel productivity, markdown discipline, cost control and margin bridge evidence.

```text
evidence_family = RETAIL_INVENTORY_NORMALIZATION_CHANNEL_PRODUCTIVITY_COST_CONTROL_MARGIN_BRIDGE
case_role = positive_slow_with_later_4b_watch
trigger_date = 2024-01-19
entry_date = 2024-01-22
entry_price = 68,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/023/023530/2024.csv`:

```text
2024-01-22,68500,72200,68000,71800
2024-01-31,79900,82400,79000,82200
2024-02-01,81200,86500,81200,86000
2024-02-08,91200,92000,89100,90100
2024-04-16,67000,67200,64500,65300
2024-08-05,63000,63100,58100,58300
2024-10-31,65200,66000,64200,66000
```

### Backtest

```text
MFE_30D  = +34.31%
MAE_30D  = -0.73%
MFE_90D  = +34.31%
MAE_90D  = -8.61%
MFE_180D = +34.31%
MAE_180D = -15.18%
peak_180 = 92,000 on 2024-02-08
trough_180 = 58,100 on 2024-08-05
peak_to_later_drawdown = -36.85%
```

### Interpretation

This is a C19 slow-positive lifecycle row.  
The entry risk was controlled and the first MFE was meaningful, but the later drawdown means inventory/margin evidence must refresh.

Correct treatment:

```text
verified inventory turnover / channel productivity / margin bridge → Stage2-Yellow possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 111770 / 영원무역

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests apparel OEM / restocking exposure without enough customer reorder and margin refresh.

```text
evidence_family = GLOBAL_APPAREL_OEM_ORDER_INVENTORY_RESTOCK_MARGIN_BRIDGE_WEAK_REFRESH
case_role = counterexample_apparel_OEM_inventory_local4b
trigger_date = 2024-01-30
entry_date = 2024-01-31
entry_price = 46,150
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/111/111770/2024.csv`:

```text
2024-01-31,46150,49400,45400,47900
2024-02-01,48250,52700,47550,52300
2024-03-25,41650,41850,40100,40300
2024-05-29,33250,33250,32100,32900
2024-07-18,39600,39650,38200,39600
2024-08-05,38300,38300,34850,36150
2024-10-16,43250,44950,42850,43700
```

### Backtest

```text
MFE_30D  = +14.19%
MAE_30D  = -8.99%
MFE_90D  = +14.19%
MAE_90D  = -30.44%
MFE_180D = +14.19%
MAE_180D = -30.44%
peak_180 = 52,700 on 2024-02-01
trough_180 = 32,100 on 2024-05-29
peak_to_later_drawdown = -39.09%
```

### Interpretation

This is a C19 apparel/OEM false-positive boundary.  
The first MFE was tradable, but it did not prove durable inventory normalization.

Correct treatment:

```text
apparel OEM / restocking beta
→ no verified reorder / inventory normalization / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 306040 / 에스제이그룹

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests fashion-brand inventory-turnaround beta without enough sell-through, markdown control and margin bridge.

```text
evidence_family = FASHION_BRAND_CHANNEL_INVENTORY_TURNAROUND_THEME_WITH_WEAK_SELLTHROUGH_MARGIN_BRIDGE
case_role = counterexample_brand_inventory_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 8,610
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/306/306040/2024.csv`:

```text
2024-02-01,8610,8730,8400,8610
2024-02-19,8440,9280,8440,8530
2024-02-29,8190,8190,7810,8130
2024-04-17,7230,7380,7160,7200
2024-06-21,6660,6660,6440,6450
2024-08-05,6280,6310,5350,5480
2024-10-25,6050,6050,5740,5800
```

### Backtest

```text
MFE_30D  = +7.78%
MAE_30D  = -9.29%
MFE_90D  = +7.78%
MAE_90D  = -18.70%
MFE_180D = +7.78%
MAE_180D = -37.86%
peak_180 = 9,280 on 2024-02-19
trough_180 = 5,350 on 2024-08-05
peak_to_later_drawdown = -42.35%
```

### Interpretation

This is a weak-MFE C19 false-positive row.  
Fashion-brand inventory-turnaround exposure did not become durable sell-through or margin conversion.

Correct treatment:

```text
brand inventory-turnaround beta
→ no sell-through / markdown / reorder / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C19_brand_inventory_weight = true
do_not_treat_all_inventory_normalization_MFE_as_Green = true
do_not_convert_brand_retail_drawdown_to_hard_4C_without_non_price_inventory_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
RETAIL_APPAREL_INVENTORY_NORMALIZATION_CHANNEL_PRODUCTIVITY_MARGIN_BRIDGE_VS_APPAREL_THEME_FADE
```

This fine archetype covers:

```text
1. large-cap retail inventory/channel productivity bridge → Stage2-Yellow possible after source repair
2. apparel OEM restocking beta without refreshed margin bridge → false Stage2 / local 4B
3. fashion-brand inventory-turnaround beta without sell-through bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R5L78-C19-023530-LOTTE-SHOPPING-RETAIL-INVENTORY-MARGIN-LIFECYCLE", "symbol": "023530", "company_name": "롯데쇼핑", "round": "R5", "loop": "78", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "RETAIL_APPAREL_INVENTORY_NORMALIZATION_CHANNEL_PRODUCTIVITY_MARGIN_BRIDGE_VS_APPAREL_THEME_FADE", "case_type": "brand_retail_inventory_margin", "positive_or_counterexample": "positive", "best_trigger": "Stage2-SlowPositive-RetailInventoryNormalizationMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C19 should allow large-cap retail inventory-normalization positives when channel productivity, inventory turnover, markdown discipline, cost control and margin bridge are visible. Lotte Shopping produced a meaningful MFE from a low-risk entry, but the later post-peak drawdown requires lifecycle local 4B if inventory/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy inventory turnover, markdown control, channel productivity, sell-through, reorder and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L78-C19-111770-YOUNGONE-APPAREL-OEM-INVENTORY-MARGIN-FADE", "symbol": "111770", "company_name": "영원무역", "round": "R5", "loop": "78", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "RETAIL_APPAREL_INVENTORY_NORMALIZATION_CHANNEL_PRODUCTIVITY_MARGIN_BRIDGE_VS_APPAREL_THEME_FADE", "case_type": "brand_retail_inventory_margin", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ApparelOEMInventoryMarginFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C19 should not treat apparel OEM or restocking exposure as durable Stage2 unless customer reorder, inventory normalization, shipment cadence, FX/cost spread and margin bridge refreshes. Youngone had a tradable early MFE, then a large drawdown into the spring/summer window.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy inventory turnover, markdown control, channel productivity, sell-through, reorder and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L78-C19-306040-SJ-GROUP-BRAND-INVENTORY-TURNAROUND-FADE", "symbol": "306040", "company_name": "에스제이그룹", "round": "R5", "loop": "78", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "RETAIL_APPAREL_INVENTORY_NORMALIZATION_CHANNEL_PRODUCTIVITY_MARGIN_BRIDGE_VS_APPAREL_THEME_FADE", "case_type": "brand_retail_inventory_margin", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / BrandInventoryTurnaroundFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C19 should not treat fashion-brand inventory-turnaround beta as durable Stage2 unless sell-through, channel productivity, inventory clearance, reorder and margin bridge are visible. SJ Group produced only small MFE, then persistent MAE and post-peak fade.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy inventory turnover, markdown control, channel productivity, sell-through, reorder and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R5L78-C19-023530-LOTTE-SHOPPING-RETAIL-INVENTORY-MARGIN-LIFECYCLE", "case_id": "R5L78-C19-023530-LOTTE-SHOPPING-RETAIL-INVENTORY-MARGIN-LIFECYCLE", "symbol": "023530", "company_name": "롯데쇼핑", "round": "R5", "loop": "78", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "RETAIL_APPAREL_INVENTORY_NORMALIZATION_CHANNEL_PRODUCTIVITY_MARGIN_BRIDGE_VS_APPAREL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|brand_retail_inventory_margin_guardrail", "trigger_type": "Stage2-SlowPositive-RetailInventoryNormalizationMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-19", "entry_date": "2024-01-22", "entry_price": 68500.0, "evidence_available_at_that_date": "RETAIL_INVENTORY_NORMALIZATION_CHANNEL_PRODUCTIVITY_COST_CONTROL_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LOTTE_SHOPPING_2024_RETAIL_INVENTORY_NORMALIZATION_CHANNEL_PRODUCTIVITY_MARGIN_BRIDGE", "stage2_evidence_fields": ["inventory_normalization_candidate", "channel_productivity_or_sellthrough_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "reorder_markdown_or_cost_control_candidate"], "stage4b_evidence_fields": ["brand_retail_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/023/023530/2024.csv", "profile_path": "atlas/symbol_profiles/023/023530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 34.31, "MFE_90D_pct": 34.31, "MFE_180D_pct": 34.31, "MAE_30D_pct": -0.73, "MAE_90D_pct": -8.61, "MAE_180D_pct": -15.18, "peak_date": "2024-02-08", "peak_price": 92000.0, "drawdown_after_peak_pct": -36.85, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_retail_inventory_peak_if_sellthrough_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_loss_inventory_buildup_markdown_spike_margin_or_financing_break", "trigger_outcome_label": "positive_slow_with_later_4b_watch", "current_profile_verdict": "C19 should allow large-cap retail inventory-normalization positives when channel productivity, inventory turnover, markdown discipline, cost control and margin bridge are visible. Lotte Shopping produced a meaningful MFE from a low-risk entry, but the later post-peak drawdown requires lifecycle local 4B if inventory/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C19_BRAND_RETAIL_023530_2024-01-22", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L78-C19-111770-YOUNGONE-APPAREL-OEM-INVENTORY-MARGIN-FADE", "case_id": "R5L78-C19-111770-YOUNGONE-APPAREL-OEM-INVENTORY-MARGIN-FADE", "symbol": "111770", "company_name": "영원무역", "round": "R5", "loop": "78", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "RETAIL_APPAREL_INVENTORY_NORMALIZATION_CHANNEL_PRODUCTIVITY_MARGIN_BRIDGE_VS_APPAREL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|brand_retail_inventory_margin_guardrail", "trigger_type": "Stage2-FalsePositive / ApparelOEMInventoryMarginFade", "trigger_date": "2024-01-30", "entry_date": "2024-01-31", "entry_price": 46150.0, "evidence_available_at_that_date": "GLOBAL_APPAREL_OEM_ORDER_INVENTORY_RESTOCK_MARGIN_BRIDGE_WEAK_REFRESH", "evidence_source": "source_proxy_manual_verification_required:YOUNGONE_2024_APPAREL_OEM_CUSTOMER_REORDER_INVENTORY_RESTOCK_FX_COST_MARGIN_BRIDGE", "stage2_evidence_fields": ["inventory_normalization_candidate", "channel_productivity_or_sellthrough_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "reorder_markdown_or_cost_control_candidate"], "stage4b_evidence_fields": ["brand_retail_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/111/111770/2024.csv", "profile_path": "atlas/symbol_profiles/111/111770.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.19, "MFE_90D_pct": 14.19, "MFE_180D_pct": 14.19, "MAE_30D_pct": -8.99, "MAE_90D_pct": -30.44, "MAE_180D_pct": -30.44, "peak_date": "2024-02-01", "peak_price": 52700.0, "drawdown_after_peak_pct": -39.09, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_retail_inventory_peak_if_sellthrough_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_loss_inventory_buildup_markdown_spike_margin_or_financing_break", "trigger_outcome_label": "counterexample_apparel_OEM_inventory_local4b", "current_profile_verdict": "C19 should not treat apparel OEM or restocking exposure as durable Stage2 unless customer reorder, inventory normalization, shipment cadence, FX/cost spread and margin bridge refreshes. Youngone had a tradable early MFE, then a large drawdown into the spring/summer window.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C19_BRAND_RETAIL_111770_2024-01-31", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L78-C19-306040-SJ-GROUP-BRAND-INVENTORY-TURNAROUND-FADE", "case_id": "R5L78-C19-306040-SJ-GROUP-BRAND-INVENTORY-TURNAROUND-FADE", "symbol": "306040", "company_name": "에스제이그룹", "round": "R5", "loop": "78", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "RETAIL_APPAREL_INVENTORY_NORMALIZATION_CHANNEL_PRODUCTIVITY_MARGIN_BRIDGE_VS_APPAREL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|brand_retail_inventory_margin_guardrail", "trigger_type": "Stage2-FalsePositive / BrandInventoryTurnaroundFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 8610.0, "evidence_available_at_that_date": "FASHION_BRAND_CHANNEL_INVENTORY_TURNAROUND_THEME_WITH_WEAK_SELLTHROUGH_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SJ_GROUP_2024_FASHION_BRAND_CHANNEL_INVENTORY_SELLTHROUGH_REORDER_MARGIN_BRIDGE", "stage2_evidence_fields": ["inventory_normalization_candidate", "channel_productivity_or_sellthrough_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "reorder_markdown_or_cost_control_candidate"], "stage4b_evidence_fields": ["brand_retail_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/306/306040/2024.csv", "profile_path": "atlas/symbol_profiles/306/306040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.78, "MFE_90D_pct": 7.78, "MFE_180D_pct": 7.78, "MAE_30D_pct": -9.29, "MAE_90D_pct": -18.7, "MAE_180D_pct": -37.86, "peak_date": "2024-02-19", "peak_price": 9280.0, "drawdown_after_peak_pct": -42.35, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_retail_inventory_peak_if_sellthrough_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_loss_inventory_buildup_markdown_spike_margin_or_financing_break", "trigger_outcome_label": "counterexample_brand_inventory_theme_local4b", "current_profile_verdict": "C19 should not treat fashion-brand inventory-turnaround beta as durable Stage2 unless sell-through, channel productivity, inventory clearance, reorder and margin bridge are visible. SJ Group produced only small MFE, then persistent MAE and post-peak fade.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C19_BRAND_RETAIL_306040_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L78-C19-023530-LOTTE-SHOPPING-RETAIL-INVENTORY-MARGIN-LIFECYCLE", "trigger_id": "TRG_R5L78-C19-023530-LOTTE-SHOPPING-RETAIL-INVENTORY-MARGIN-LIFECYCLE", "symbol": "023530", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"inventory_turnover_score": 13, "channel_productivity_score": 13, "sellthrough_reorder_score": 12, "markdown_control_score": 12, "margin_bridge_score": 13, "relative_strength_score": 10, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage2-Yellow candidate after source repair", "raw_component_scores_after": {"inventory_turnover_score": 15, "channel_productivity_score": 15, "sellthrough_reorder_score": 14, "markdown_control_score": 14, "margin_bridge_score": 15, "relative_strength_score": 9, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["inventory_turnover_score", "channel_productivity_score", "sellthrough_reorder_score", "markdown_control_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified inventory turnover, sell-through, channel productivity, markdown control and margin bridge; cap brand/retail inventory theme beta when evidence fails to refresh.", "MFE_90D_pct": 34.31, "MAE_90D_pct": -8.61, "score_return_alignment_label": "retail_inventory_positive_with_lifecycle_4b", "current_profile_verdict": "C19 should allow large-cap retail inventory-normalization positives when channel productivity, inventory turnover, markdown discipline, cost control and margin bridge are visible. Lotte Shopping produced a meaningful MFE from a low-risk entry, but the later post-peak drawdown requires lifecycle local 4B if inventory/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L78-C19-111770-YOUNGONE-APPAREL-OEM-INVENTORY-MARGIN-FADE", "trigger_id": "TRG_R5L78-C19-111770-YOUNGONE-APPAREL-OEM-INVENTORY-MARGIN-FADE", "symbol": "111770", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"inventory_turnover_score": 4, "channel_productivity_score": 3, "sellthrough_reorder_score": 2, "markdown_control_score": 2, "margin_bridge_score": 2, "relative_strength_score": 4, "execution_risk_score": 21, "source_confidence_score": 2}, "weighted_score_before": 46, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"inventory_turnover_score": 2, "channel_productivity_score": 1, "sellthrough_reorder_score": 1, "markdown_control_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["inventory_turnover_score", "channel_productivity_score", "sellthrough_reorder_score", "markdown_control_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified inventory turnover, sell-through, channel productivity, markdown control and margin bridge; cap brand/retail inventory theme beta when evidence fails to refresh.", "MFE_90D_pct": 14.19, "MAE_90D_pct": -30.44, "score_return_alignment_label": "false_positive_brand_inventory_bridge_gap", "current_profile_verdict": "C19 should not treat apparel OEM or restocking exposure as durable Stage2 unless customer reorder, inventory normalization, shipment cadence, FX/cost spread and margin bridge refreshes. Youngone had a tradable early MFE, then a large drawdown into the spring/summer window."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L78-C19-306040-SJ-GROUP-BRAND-INVENTORY-TURNAROUND-FADE", "trigger_id": "TRG_R5L78-C19-306040-SJ-GROUP-BRAND-INVENTORY-TURNAROUND-FADE", "symbol": "306040", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"inventory_turnover_score": 4, "channel_productivity_score": 3, "sellthrough_reorder_score": 2, "markdown_control_score": 2, "margin_bridge_score": 2, "relative_strength_score": 4, "execution_risk_score": 21, "source_confidence_score": 2}, "weighted_score_before": 46, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"inventory_turnover_score": 2, "channel_productivity_score": 1, "sellthrough_reorder_score": 1, "markdown_control_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["inventory_turnover_score", "channel_productivity_score", "sellthrough_reorder_score", "markdown_control_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified inventory turnover, sell-through, channel productivity, markdown control and margin bridge; cap brand/retail inventory theme beta when evidence fails to refresh.", "MFE_90D_pct": 7.78, "MAE_90D_pct": -18.7, "score_return_alignment_label": "false_positive_brand_inventory_bridge_gap", "current_profile_verdict": "C19 should not treat fashion-brand inventory-turnaround beta as durable Stage2 unless sell-through, channel productivity, inventory clearance, reorder and margin bridge are visible. SJ Group produced only small MFE, then persistent MAE and post-peak fade."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R5", "loop": 78, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "RETAIL_APPAREL_INVENTORY_NORMALIZATION_CHANNEL_PRODUCTIVITY_MARGIN_BRIDGE_VS_APPAREL_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 C19 retail/apparel symbols outside top-covered 036620/298540/383220/337930 set, +3 retail/apparel/OEM/fashion-brand inventory trigger families, +1 large-cap retail inventory lifecycle candidate, +2 apparel/brand inventory local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R5", "loop": 78, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "axis": "retail_apparel_inventory_normalization_channel_productivity_margin_bridge_vs_apparel_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C19 should split verified retail/brand inventory normalization and channel productivity rerating from generic apparel or inventory-turnaround beta. Stage2 requires inventory turnover, sell-through, reorder, markdown control, channel productivity and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["023530", "111770", "306040"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": 78, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C19 needs inventory turnover, sell-through, channel productivity and margin proof. Lotte Shopping shows a large-cap retail inventory-normalization MFE candidate after source repair; Youngone and SJ Group show apparel/brand inventory beta fading into local 4B when reorder, markdown and margin bridge are absent or stale."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward_window_basis = stock_web_manifest_max_date
all_selected_entry_dates_present_in_tradable_shards = true
all_selected_180D_windows_available = true
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
023530:
  name = 롯데쇼핑
  corporate_action_candidate_dates = none
  selected window = 2024-01-22~D+180
  contamination = false

111770:
  name = 영원무역
  corporate_action_candidate_dates = none
  selected window = 2024-01-31~D+180
  contamination = false

306040:
  name = 에스제이그룹
  corporate_action_candidate_dates = 2020-06-29, 2020-07-20
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C19 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C19 rule-shape discovery,
but coding-agent promotion requires non-proxy inventory turnover, sell-through, channel productivity, markdown control, reorder and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R5/C19 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
retail_apparel_inventory_normalization_channel_productivity_margin_bridge_vs_apparel_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 023530, 111770 and 306040.
4. Keep generic C19 brand/retail inventory weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - inventory normalization or inventory turnover is explicit,
   - sell-through and channel productivity are visible,
   - reorder or markdown control exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is brand/retail inventory beta only,
   - sell-through/reorder/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price channel loss, inventory buildup, markdown spike, liquidity/financing or margin break.
8. Emit before/after diagnostics and reject if verified inventory-normalization positives are overblocked.
```

---

## Final round state

```text
completed_round = R5
completed_loop = 78
next_round = R6
next_loop = 78
round_schedule_status = valid
round_sector_consistency = pass
```


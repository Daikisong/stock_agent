# E2R Stock-Web v12 Residual Research — R4 Loop 77 / L4 / C15

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 77,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 77,
  "computed_next_round": "R5",
  "computed_next_loop": 77,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_COPPER_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "copper_nonferrous_spread_margin_guardrail",
    "material_spread_vs_theme_beta",
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

Previous completed state in this interactive run: R3 / loop 77.

Therefore:

```text
scheduled_round = R4
scheduled_loop = 77
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
computed_next_round = R5
computed_next_loop = 77
```

R4 was routed to C15 because loop 76 used C17 and loop 75 used C16.  
This file tests copper/nonferrous price-spread and margin bridge behavior rather than strategic-resource policy or generic chemical spread.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C15 is concentrated in:

```text
006260, 011170, 103140, 006650, 011780
```

This run uses three different symbols:

```text
025820 / 이구산업 / copper processing spread inventory-margin bridge
012800 / 대창 / copper/brass spread theme fade
021050 / 서원 / copper-alloy spread theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C15 is not “구리 테마가 올랐다.”

The mechanism must pass through:

```text
commodity price / nonferrous spread
→ inventory revaluation or price pass-through
→ volume / order bridge
→ margin conversion
→ durable rerating
```

구리 가격은 파도다.  
C15가 보려는 것은 그 파도를 회사가 재고, 단가, 물량, 마진으로 바꾸는 능력이다.

---

## Case 1 — Positive with lifecycle 4B: 025820 / 이구산업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is copper price-cost spread, inventory revaluation, volume, price pass-through and margin bridge evidence.

```text
evidence_family = COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_VOLUME_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-04-11
entry_date = 2024-04-12
entry_price = 5,690
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv`:

```text
2024-04-12,5690,6090,5460,5700
2024-04-19,6640,7310,6410,6790
2024-05-20,7700,8420,7400,7880
2024-08-05,4365,4430,3795,3930
2024-09-06,4080,4100,3975,3990
```

### Backtest

```text
MFE_30D  = +47.98%
MAE_30D  = -4.04%
MFE_90D  = +47.98%
MAE_90D  = -33.30%
MFE_180D = +47.98%
MAE_180D = -33.30%
peak_180 = 8,420 on 2024-05-20
trough_180 = 3,795 on 2024-08-05
peak_to_later_drawdown = -54.93%
```

### Interpretation

This is the C15 lifecycle positive candidate.  
The MFE was strong and the early entry-basis MAE was controlled, but the post-peak drawdown shows why spread/margin evidence must refresh.

Correct treatment:

```text
verified copper spread / inventory / volume / margin bridge → Stage2 possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 012800 / 대창

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests copper/brass theme MFE without enough volume and margin bridge.

```text
evidence_family = COPPER_BRASS_PRICE_SPREAD_THEME_WITH_WEAK_VOLUME_MARGIN_BRIDGE
case_role = counterexample_copper_spread_beta_local4b
trigger_date = 2024-04-11
entry_date = 2024-04-12
entry_price = 1,470
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv`:

```text
2024-04-12,1470,1575,1450,1543
2024-05-20,1695,2080,1687,2080
2024-05-21,2185,2320,2080,2175
2024-08-05,1277,1283,1100,1161
2024-09-09,1190,1230,1183,1226
```

### Backtest

```text
MFE_30D  = +57.82%
MAE_30D  = -0.88%
MFE_90D  = +57.82%
MAE_90D  = -25.17%
MFE_180D = +57.82%
MAE_180D = -25.17%
peak_180 = 2,320 on 2024-05-21
trough_180 = 1,100 on 2024-08-05
peak_to_later_drawdown = -52.59%
```

### Interpretation

This is the dangerous copper-theme false positive.  
Large MFE occurred, but the later MAE and drawdown say it should not be permanent Green without spread/margin proof.

Correct treatment:

```text
copper/brass theme beta
→ no verified volume / price pass-through / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 021050 / 서원

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests copper-alloy / nonferrous theme MFE without enough order, inventory and margin bridge.

```text
evidence_family = COPPER_ALLOY_PRICE_SPREAD_THEME_WITH_WEAK_ORDER_VOLUME_MARGIN_BRIDGE
case_role = counterexample_copper_alloy_theme_local4b
trigger_date = 2024-04-12
entry_date = 2024-04-15
entry_price = 1,328
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/021/021050/2024.csv`:

```text
2024-04-15,1328,1410,1326,1359
2024-05-16,1454,1794,1454,1633
2024-05-20,1674,1999,1630,1916
2024-05-21,2000,2005,1700,1815
2024-09-09,1190,1230,1183,1226
```

### Backtest

```text
MFE_30D  = +51.00%
MAE_30D  = -1.20%
MFE_90D  = +51.00%
MAE_90D  = -10.92%
MFE_180D = +51.00%
MAE_180D = -10.92%
peak_180 = 2,005 on 2024-05-21
trough_180 = 1,183 on 2024-09-09
peak_to_later_drawdown = -40.99%
```

### Interpretation

This is another C15 theme-beta boundary.  
The price move was tradable, but the later fade means no durable Stage2 without order/volume/margin evidence.

Correct treatment:

```text
copper alloy theme
→ no order / inventory / margin bridge
→ local 4B-watch after peak
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
do_not_raise_generic_C15_copper_theme_weight = true
do_not_treat_all_nonferrous_MFE_as_Green = true
do_not_convert_metal_spread_drawdown_to_hard_4C_without_non_price_spread_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_COPPER_THEME_FADE
```

This fine archetype covers:

```text
1. copper processing price-spread / inventory bridge → Stage2 possible after source repair
2. copper/brass theme without volume/margin bridge → false Stage2 / local 4B
3. copper-alloy theme without order/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R4L77-C15-025820-IGOO-COPPER-SPREAD-INVENTORY-MARGIN-LIFECYCLE", "symbol": "025820", "company_name": "이구산업", "round": "R4", "loop": "77", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_COPPER_THEME_FADE", "case_type": "material_spread_supercycle", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-CopperSpreadInventoryMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C15 should allow nonferrous/copper processors when copper price/spread, inventory revaluation, volume and margin bridge are visible. Igoo Industry produced large MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if spread/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy copper/nonferrous spread, inventory, volume, price pass-through and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L77-C15-012800-DAECHANG-COPPER-BRASS-SPREAD-THEME-FADE", "symbol": "012800", "company_name": "대창", "round": "R4", "loop": "77", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_COPPER_THEME_FADE", "case_type": "material_spread_supercycle", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / CopperBrassSpreadThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C15 should not treat copper/brass price beta as durable Stage2 unless spread, inventory, volume, price pass-through and margin evidence refreshes. Daechang produced large tradable MFE, then opened high MAE and deep post-peak drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy copper/nonferrous spread, inventory, volume, price pass-through and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L77-C15-021050-SEOWON-COPPER-ALLOY-SPREAD-THEME-FADE", "symbol": "021050", "company_name": "서원", "round": "R4", "loop": "77", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_COPPER_THEME_FADE", "case_type": "material_spread_supercycle", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / CopperAlloySpreadThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C15 should not treat copper alloy or nonferrous theme spikes as durable Stage2 unless order, volume, inventory and margin bridge are visible. Seowon produced high MFE but then leaked back into a broad range, making it a local 4B-watch row rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy copper/nonferrous spread, inventory, volume, price pass-through and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R4L77-C15-025820-IGOO-COPPER-SPREAD-INVENTORY-MARGIN-LIFECYCLE", "case_id": "R4L77-C15-025820-IGOO-COPPER-SPREAD-INVENTORY-MARGIN-LIFECYCLE", "symbol": "025820", "company_name": "이구산업", "round": "R4", "loop": "77", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_COPPER_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|copper_nonferrous_spread_margin_guardrail", "trigger_type": "Stage2-Actionable-CopperSpreadInventoryMarginBridgeWithLifecycle4B", "trigger_date": "2024-04-11", "entry_date": "2024-04-12", "entry_price": 5690.0, "evidence_available_at_that_date": "COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_VOLUME_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:IGOO_INDUSTRY_2024_COPPER_PRICE_SPREAD_INVENTORY_VOLUME_MARGIN_BRIDGE", "stage2_evidence_fields": ["copper_nonferrous_price_spread_candidate", "inventory_volume_or_pass_through_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "order_or_customer_volume_bridge_candidate"], "stage4b_evidence_fields": ["material_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv", "profile_path": "atlas/symbol_profiles/025/025820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 47.98, "MFE_90D_pct": 47.98, "MFE_180D_pct": 47.98, "MAE_30D_pct": -4.04, "MAE_90D_pct": -33.3, "MAE_180D_pct": -33.3, "peak_date": "2024-05-20", "peak_price": 8420.0, "drawdown_after_peak_pct": -54.93, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_nonferrous_spread_peak_if_inventory_volume_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_inventory_impairment_order_volume_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C15 should allow nonferrous/copper processors when copper price/spread, inventory revaluation, volume and margin bridge are visible. Igoo Industry produced large MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if spread/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C15_COPPER_SPREAD_025820_2024-04-12", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L77-C15-012800-DAECHANG-COPPER-BRASS-SPREAD-THEME-FADE", "case_id": "R4L77-C15-012800-DAECHANG-COPPER-BRASS-SPREAD-THEME-FADE", "symbol": "012800", "company_name": "대창", "round": "R4", "loop": "77", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_COPPER_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|copper_nonferrous_spread_margin_guardrail", "trigger_type": "Stage2-FalsePositive / CopperBrassSpreadThemeFade", "trigger_date": "2024-04-11", "entry_date": "2024-04-12", "entry_price": 1470.0, "evidence_available_at_that_date": "COPPER_BRASS_PRICE_SPREAD_THEME_WITH_WEAK_VOLUME_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DAECHANG_2024_COPPER_BRASS_PRICE_SPREAD_VOLUME_MARGIN_BRIDGE", "stage2_evidence_fields": ["copper_nonferrous_price_spread_candidate", "inventory_volume_or_pass_through_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "order_or_customer_volume_bridge_candidate"], "stage4b_evidence_fields": ["material_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv", "profile_path": "atlas/symbol_profiles/012/012800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 57.82, "MFE_90D_pct": 57.82, "MFE_180D_pct": 57.82, "MAE_30D_pct": -0.88, "MAE_90D_pct": -25.17, "MAE_180D_pct": -25.17, "peak_date": "2024-05-21", "peak_price": 2320.0, "drawdown_after_peak_pct": -52.59, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_nonferrous_spread_peak_if_inventory_volume_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_inventory_impairment_order_volume_or_margin_break", "trigger_outcome_label": "counterexample_copper_spread_beta_local4b", "current_profile_verdict": "C15 should not treat copper/brass price beta as durable Stage2 unless spread, inventory, volume, price pass-through and margin evidence refreshes. Daechang produced large tradable MFE, then opened high MAE and deep post-peak drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C15_COPPER_SPREAD_012800_2024-04-12", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L77-C15-021050-SEOWON-COPPER-ALLOY-SPREAD-THEME-FADE", "case_id": "R4L77-C15-021050-SEOWON-COPPER-ALLOY-SPREAD-THEME-FADE", "symbol": "021050", "company_name": "서원", "round": "R4", "loop": "77", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_COPPER_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|copper_nonferrous_spread_margin_guardrail", "trigger_type": "Stage2-FalsePositive / CopperAlloySpreadThemeFade", "trigger_date": "2024-04-12", "entry_date": "2024-04-15", "entry_price": 1328.0, "evidence_available_at_that_date": "COPPER_ALLOY_PRICE_SPREAD_THEME_WITH_WEAK_ORDER_VOLUME_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SEOWON_2024_COPPER_ALLOY_PRICE_SPREAD_ORDER_VOLUME_MARGIN_BRIDGE", "stage2_evidence_fields": ["copper_nonferrous_price_spread_candidate", "inventory_volume_or_pass_through_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "order_or_customer_volume_bridge_candidate"], "stage4b_evidence_fields": ["material_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/021/021050/2024.csv", "profile_path": "atlas/symbol_profiles/021/021050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 51.0, "MFE_90D_pct": 51.0, "MFE_180D_pct": 51.0, "MAE_30D_pct": -1.2, "MAE_90D_pct": -10.92, "MAE_180D_pct": -10.92, "peak_date": "2024-05-21", "peak_price": 2005.0, "drawdown_after_peak_pct": -40.99, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_nonferrous_spread_peak_if_inventory_volume_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_inventory_impairment_order_volume_or_margin_break", "trigger_outcome_label": "counterexample_copper_alloy_theme_local4b", "current_profile_verdict": "C15 should not treat copper alloy or nonferrous theme spikes as durable Stage2 unless order, volume, inventory and margin bridge are visible. Seowon produced high MFE but then leaked back into a broad range, making it a local 4B-watch row rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C15_COPPER_SPREAD_021050_2024-04-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L77-C15-025820-IGOO-COPPER-SPREAD-INVENTORY-MARGIN-LIFECYCLE", "trigger_id": "TRG_R4L77-C15-025820-IGOO-COPPER-SPREAD-INVENTORY-MARGIN-LIFECYCLE", "symbol": "025820", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"commodity_spread_score": 14, "inventory_revaluation_score": 13, "volume_order_score": 12, "price_pass_through_score": 12, "margin_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"commodity_spread_score": 16, "inventory_revaluation_score": 15, "volume_order_score": 14, "price_pass_through_score": 14, "margin_bridge_score": 15, "relative_strength_score": 12, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["commodity_spread_score", "inventory_revaluation_score", "volume_order_score", "price_pass_through_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified copper/nonferrous spread, inventory/volume, price pass-through and margin bridge; cap metal theme beta when bridge evidence fails to refresh.", "MFE_90D_pct": 47.98, "MAE_90D_pct": -33.3, "score_return_alignment_label": "material_spread_positive_with_lifecycle_4b", "current_profile_verdict": "C15 should allow nonferrous/copper processors when copper price/spread, inventory revaluation, volume and margin bridge are visible. Igoo Industry produced large MFE with controlled entry-basis MAE, but later drawdown requires lifecycle local 4B if spread/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L77-C15-012800-DAECHANG-COPPER-BRASS-SPREAD-THEME-FADE", "trigger_id": "TRG_R4L77-C15-012800-DAECHANG-COPPER-BRASS-SPREAD-THEME-FADE", "symbol": "012800", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"commodity_spread_score": 8, "inventory_revaluation_score": 4, "volume_order_score": 3, "price_pass_through_score": 3, "margin_bridge_score": 2, "relative_strength_score": 13, "execution_risk_score": 20, "source_confidence_score": 2}, "weighted_score_before": 51, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"commodity_spread_score": 4, "inventory_revaluation_score": 2, "volume_order_score": 2, "price_pass_through_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_after": 37, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["commodity_spread_score", "inventory_revaluation_score", "volume_order_score", "price_pass_through_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified copper/nonferrous spread, inventory/volume, price pass-through and margin bridge; cap metal theme beta when bridge evidence fails to refresh.", "MFE_90D_pct": 57.82, "MAE_90D_pct": -25.17, "score_return_alignment_label": "false_positive_copper_theme_bridge_gap", "current_profile_verdict": "C15 should not treat copper/brass price beta as durable Stage2 unless spread, inventory, volume, price pass-through and margin evidence refreshes. Daechang produced large tradable MFE, then opened high MAE and deep post-peak drawdown."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L77-C15-021050-SEOWON-COPPER-ALLOY-SPREAD-THEME-FADE", "trigger_id": "TRG_R4L77-C15-021050-SEOWON-COPPER-ALLOY-SPREAD-THEME-FADE", "symbol": "021050", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"commodity_spread_score": 8, "inventory_revaluation_score": 4, "volume_order_score": 3, "price_pass_through_score": 3, "margin_bridge_score": 2, "relative_strength_score": 13, "execution_risk_score": 20, "source_confidence_score": 2}, "weighted_score_before": 51, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"commodity_spread_score": 4, "inventory_revaluation_score": 2, "volume_order_score": 2, "price_pass_through_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_after": 37, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["commodity_spread_score", "inventory_revaluation_score", "volume_order_score", "price_pass_through_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified copper/nonferrous spread, inventory/volume, price pass-through and margin bridge; cap metal theme beta when bridge evidence fails to refresh.", "MFE_90D_pct": 51.0, "MAE_90D_pct": -10.92, "score_return_alignment_label": "false_positive_copper_theme_bridge_gap", "current_profile_verdict": "C15 should not treat copper alloy or nonferrous theme spikes as durable Stage2 unless order, volume, inventory and margin bridge are visible. Seowon produced high MFE but then leaked back into a broad range, making it a local 4B-watch row rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R4", "loop": 77, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_NONFERROUS_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE_VS_COPPER_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 C15 nonferrous/copper symbols outside top-covered 006260/011170/103140 set, +3 copper-processing/brass/copper-alloy trigger families, +1 spread lifecycle positive, +2 copper theme local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R4", "loop": 77, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "axis": "copper_nonferrous_price_spread_inventory_margin_bridge_vs_copper_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C15 should split verified nonferrous/copper spread and margin recovery from generic copper-theme beta. Stage2 requires commodity price-cost spread, inventory/volume bridge, price pass-through and margin conversion. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["025820", "012800", "021050"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": 77, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C15 needs spread/inventory/margin proof. Igoo Industry shows a copper spread lifecycle MFE candidate after source repair; Daechang and Seowon show copper/brass theme MFE fading into local 4B when volume and margin bridge are absent."}
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
025820:
  corporate_action_candidate_dates = 1996-01-03, 2007-04-30, 2007-07-11
  selected window = 2024-04-12~D+180
  contamination = false

012800:
  corporate_action_candidate_dates = 1998-12-15, 2008-04-16
  selected window = 2024-04-12~D+180
  contamination = false

021050:
  corporate_action_candidate_dates = 1996-12-24, 1997-09-25, 2008-04-16, 2016-06-21
  selected window = 2024-04-15~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C15 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C15 rule-shape discovery,
but coding-agent promotion requires non-proxy copper/nonferrous spread, inventory, volume, price pass-through and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R4/C15 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
copper_nonferrous_price_spread_inventory_margin_bridge_vs_copper_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 025820, 012800 and 021050.
4. Keep generic C15 material-spread weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - commodity price-cost spread is explicit,
   - inventory revaluation, volume or order bridge is visible,
   - price pass-through and margin conversion exist,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is copper/nonferrous theme beta only,
   - spread/inventory/volume/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price spread collapse, inventory impairment, order/volume loss, financing or margin break.
8. Emit before/after diagnostics and reject if verified material spread positives are overblocked.
```

---

## Final round state

```text
completed_round = R4
completed_loop = 77
next_round = R5
next_loop = 77
round_schedule_status = valid
round_sector_consistency = pass
```


# E2R Stock-Web v12 Residual Research — R5 Loop 79 / L5 / C18

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 79,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 79,
  "computed_next_round": "R6",
  "computed_next_loop": 79,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_CHANNEL_REORDER_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "consumer_export_channel_reorder_guardrail",
    "K_food_global_channel_reorder_revenue_margin_bridge",
    "China_channel_reorder_reset_no_stage2_boundary",
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

Previous completed state in this interactive run: R4 / loop 79.

Therefore:

```text
scheduled_round = R5
scheduled_loop = 79
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
computed_next_round = R6
computed_next_loop = 79
```

R5 was routed to C18 because loop 78 used C19.  
This file tests consumer export / channel reorder bridges rather than brand inventory or beauty/food distribution mega-coverage.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C18 concentration in:

```text
003230, 005180, 004370, 383220, 161890
```

This run uses three different symbols:

```text
097950 / CJ제일제당 / K-food global channel reorder bridge
017810 / 풀무원 / global food channel reorder bridge
271560 / 오리온 / China channel reorder reset boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C18 is not “K-푸드가 잘 팔린다.”

The mechanism must pass through:

```text
consumer export or overseas channel attention
→ channel reorder / distribution expansion
→ volume and repeat purchase
→ price/mix and revenue conversion
→ margin bridge
→ durable rerating
```

수출 재주문은 매대 뒤 창고의 손이다.  
C18이 보려는 것은 그 손이 실제 물량, 매출, 믹스, 마진을 다시 채우는지다.

---

## Case 1 — Channel-reorder positive: 097950 / CJ제일제당

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is K-food overseas channel reorder, distribution expansion, volume, price/mix, revenue and margin bridge evidence.

```text
evidence_family = KFOOD_GLOBAL_CHANNEL_REORDER_OVERSEAS_DISTRIBUTION_VOLUME_REVENUE_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 289,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv`:

```text
2024-02-01,289000,299500,289000,297500
2024-02-21,307000,310000,305000,309500
2024-03-07,290000,291000,281500,283500
2024-04-22,338500,347000,335500,347000
2024-06-26,397500,407500,393000,398000
2024-07-31,379500,391000,377500,386500
2024-10-25,272500,274000,267500,269500
```

### Backtest

```text
MFE_30D  = +7.27%
MAE_30D  = -2.60%
MFE_90D  = +38.24%
MAE_90D  = -2.60%
MFE_180D = +41.00%
MAE_180D = -7.44%
peak_180 = 407,500 on 2024-06-26
trough_180 = 267,500 on 2024-10-25
peak_to_later_drawdown = -34.36%
```

### Interpretation

This is a C18 K-food / global channel positive.  
The MFE was meaningful and entry-basis MAE was controlled.

Correct treatment:

```text
verified overseas channel reorder / volume / price-mix / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Channel-reorder positive: 017810 / 풀무원

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is global food channel reorder, tofu/HMR distribution, repeat purchase, revenue conversion and margin bridge evidence.

```text
evidence_family = GLOBAL_FOOD_TOFU_HMR_CHANNEL_REORDER_VOLUME_REVENUE_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 10,320
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv`:

```text
2024-02-01,10320,10590,10230,10540
2024-02-29,10600,10790,10500,10610
2024-04-04,11180,12190,11000,12110
2024-07-24,14540,15050,14250,14320
2024-08-05,12660,12960,11000,11920
2024-09-09,10250,10430,10010,10320
2024-10-25,10350,10390,10160,10220
```

### Backtest

```text
MFE_30D  = +4.55%
MAE_30D  = -1.55%
MFE_90D  = +18.12%
MAE_90D  = -1.55%
MFE_180D = +45.83%
MAE_180D = -3.00%
peak_180 = 15,050 on 2024-07-24
trough_180 = 10,010 on 2024-09-09
peak_to_later_drawdown = -33.49%
```

### Interpretation

This is a C18 global food channel positive.  
The move did not have heavy entry-basis MAE, but the late drawdown says channel/revenue/margin evidence must refresh.

Correct treatment:

```text
verified distribution / repeat purchase / revenue / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Bounded no-Stage2 boundary: 271560 / 오리온

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests China-channel reorder/reset beta without enough high-conviction volume, revenue and margin bridge.

```text
evidence_family = CHINA_CONFECTIONERY_CHANNEL_REORDER_RESET_WITH_WEAK_VOLUME_REVENUE_MARGIN_RERATING_BRIDGE
case_role = counterexample_channel_reorder_no_durable_stage2_no_forced4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 91,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv`:

```text
2024-02-01,91000,91800,89800,91500
2024-02-19,98200,99400,96800,97700
2024-04-17,96300,98500,90800,91100
2024-06-18,105900,106700,99600,100900
2024-08-05,88600,89300,81800,83900
2024-09-27,96200,99900,96000,99600
2024-10-11,101600,102900,98500,99000
```

### Backtest

```text
MFE_30D  = +9.23%
MAE_30D  = -1.32%
MFE_90D  = +17.25%
MAE_90D  = -1.98%
MFE_180D = +17.25%
MAE_180D = -10.11%
peak_180 = 106,700 on 2024-06-18
trough_180 = 81,800 on 2024-08-05
peak_to_later_drawdown = -23.34%
```

### Interpretation

This is not durable Stage2, but it is also not forced local 4B.  
The price path was bounded and did not collapse, but C18 needs stronger channel reorder, volume/revenue and margin proof.

Correct treatment:

```text
China channel reset / reorder watch
bounded MAE
→ no forced 4B
→ no durable Stage2 without channel-volume-margin bridge
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
bounded_channel_reset_no_forced_4B_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C18_Kfood_channel_weight = true
do_not_treat_all_channel_reorder_MFE_as_Green = true
do_not_force_4B_on_bounded_channel_reset_rows = true
do_not_convert_consumer_export_drawdown_to_hard_4C_without_non_price_channel_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
KFOOD_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_CHANNEL_REORDER_FADE
```

This fine archetype covers:

```text
1. K-food global channel reorder + margin bridge → Stage2 possible after source repair
2. global food channel repeat-purchase / distribution bridge → Stage2 possible, lifecycle-managed
3. China channel reset with bounded MAE but weak rerating bridge → RiskWatch / no durable Stage2
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R5L79-C18-097950-CJ-CHEILJEDANG-KFOOD-GLOBAL-CHANNEL-REORDER", "symbol": "097950", "company_name": "CJ제일제당", "round": "R5", "loop": "79", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_CHANNEL_REORDER_FADE", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-KFoodGlobalChannelReorderRevenueMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should allow K-food/global food positives when overseas channel reorder, distribution expansion, volume growth, price/mix and margin bridge are visible. CJ CheilJedang produced strong MFE with bounded entry-basis MAE, but later drawdown means channel/revenue/margin evidence must refresh.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy overseas channel reorder, distribution expansion, volume, revenue conversion, price/mix and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L79-C18-017810-PULMUONE-GLOBAL-FOOD-CHANNEL-REORDER", "symbol": "017810", "company_name": "풀무원", "round": "R5", "loop": "79", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_CHANNEL_REORDER_FADE", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-GlobalFoodChannelReorderRevenueMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should preserve food-channel positives when overseas/online channel reorder, product mix, volume, revenue conversion and margin bridge are visible. Pulmuone produced high MFE with very bounded entry-basis MAE, but post-peak drawdown requires lifecycle management.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy overseas channel reorder, distribution expansion, volume, revenue conversion, price/mix and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L79-C18-271560-ORION-CHINA-CHANNEL-REORDER-RESET-BOUNDARY", "symbol": "271560", "company_name": "오리온", "round": "R5", "loop": "79", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_CHANNEL_REORDER_FADE", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "counterexample", "best_trigger": "RiskWatch-ChinaChannelReorderResetNoDurableStage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should not treat all confectionery or China-channel reorder resets as durable Stage2. Orion produced bounded MAE and a modest recovery MFE, so it should not be forced into 4B, but the price path did not validate a high-conviction export/channel rerating either.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy overseas channel reorder, distribution expansion, volume, revenue conversion, price/mix and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R5L79-C18-097950-CJ-CHEILJEDANG-KFOOD-GLOBAL-CHANNEL-REORDER", "case_id": "R5L79-C18-097950-CJ-CHEILJEDANG-KFOOD-GLOBAL-CHANNEL-REORDER", "symbol": "097950", "company_name": "CJ제일제당", "round": "R5", "loop": "79", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_CHANNEL_REORDER_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail", "trigger_type": "Stage2-Actionable-KFoodGlobalChannelReorderRevenueMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 289000.0, "evidence_available_at_that_date": "KFOOD_GLOBAL_CHANNEL_REORDER_OVERSEAS_DISTRIBUTION_VOLUME_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:CJ_CHEILJEDANG_2024_KFOOD_GLOBAL_CHANNEL_REORDER_VOLUME_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["overseas_channel_reorder_candidate", "volume_or_distribution_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "price_mix_or_repeat_purchase_candidate"], "stage4b_evidence_fields": ["channel_reorder_theme_beta", "bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv", "profile_path": "atlas/symbol_profiles/097/097950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.27, "MFE_90D_pct": 38.24, "MFE_180D_pct": 41.0, "MAE_30D_pct": -2.6, "MAE_90D_pct": -2.6, "MAE_180D_pct": -7.44, "peak_date": "2024-06-26", "peak_price": 407500.0, "drawdown_after_peak_pct": -34.36, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_channel_reorder_peak_if_volume_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_loss_reorder_collapse_inventory_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C18 should allow K-food/global food positives when overseas channel reorder, distribution expansion, volume growth, price/mix and margin bridge are visible. CJ CheilJedang produced strong MFE with bounded entry-basis MAE, but later drawdown means channel/revenue/margin evidence must refresh.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C18_CONSUMER_REORDER_097950_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L79-C18-017810-PULMUONE-GLOBAL-FOOD-CHANNEL-REORDER", "case_id": "R5L79-C18-017810-PULMUONE-GLOBAL-FOOD-CHANNEL-REORDER", "symbol": "017810", "company_name": "풀무원", "round": "R5", "loop": "79", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_CHANNEL_REORDER_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail", "trigger_type": "Stage2-Actionable-GlobalFoodChannelReorderRevenueMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 10320.0, "evidence_available_at_that_date": "GLOBAL_FOOD_TOFU_HMR_CHANNEL_REORDER_VOLUME_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:PULMUONE_2024_GLOBAL_FOOD_CHANNEL_REORDER_VOLUME_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["overseas_channel_reorder_candidate", "volume_or_distribution_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "price_mix_or_repeat_purchase_candidate"], "stage4b_evidence_fields": ["channel_reorder_theme_beta", "bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv", "profile_path": "atlas/symbol_profiles/017/017810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.55, "MFE_90D_pct": 18.12, "MFE_180D_pct": 45.83, "MAE_30D_pct": -1.55, "MAE_90D_pct": -1.55, "MAE_180D_pct": -3.0, "peak_date": "2024-07-24", "peak_price": 15050.0, "drawdown_after_peak_pct": -33.49, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_channel_reorder_peak_if_volume_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_loss_reorder_collapse_inventory_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C18 should preserve food-channel positives when overseas/online channel reorder, product mix, volume, revenue conversion and margin bridge are visible. Pulmuone produced high MFE with very bounded entry-basis MAE, but post-peak drawdown requires lifecycle management.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C18_CONSUMER_REORDER_017810_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L79-C18-271560-ORION-CHINA-CHANNEL-REORDER-RESET-BOUNDARY", "case_id": "R5L79-C18-271560-ORION-CHINA-CHANNEL-REORDER-RESET-BOUNDARY", "symbol": "271560", "company_name": "오리온", "round": "R5", "loop": "79", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_CHANNEL_REORDER_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail", "trigger_type": "RiskWatch-ChinaChannelReorderResetNoDurableStage2", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 91000.0, "evidence_available_at_that_date": "CHINA_CONFECTIONERY_CHANNEL_REORDER_RESET_WITH_WEAK_VOLUME_REVENUE_MARGIN_RERATING_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ORION_2024_CHINA_CHANNEL_REORDER_VOLUME_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["overseas_channel_reorder_candidate", "volume_or_distribution_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "price_mix_or_repeat_purchase_candidate"], "stage4b_evidence_fields": ["channel_reorder_theme_beta", "bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv", "profile_path": "atlas/symbol_profiles/271/271560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.23, "MFE_90D_pct": 17.25, "MFE_180D_pct": 17.25, "MAE_30D_pct": -1.32, "MAE_90D_pct": -1.98, "MAE_180D_pct": -10.11, "peak_date": "2024-06-18", "peak_price": 106700.0, "drawdown_after_peak_pct": -23.34, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_channel_reorder_peak_if_volume_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_loss_reorder_collapse_inventory_or_margin_break", "trigger_outcome_label": "counterexample_channel_reorder_no_durable_stage2_no_forced4b", "current_profile_verdict": "C18 should not treat all confectionery or China-channel reorder resets as durable Stage2. Orion produced bounded MAE and a modest recovery MFE, so it should not be forced into 4B, but the price path did not validate a high-conviction export/channel rerating either.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C18_CONSUMER_REORDER_271560_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L79-C18-097950-CJ-CHEILJEDANG-KFOOD-GLOBAL-CHANNEL-REORDER", "trigger_id": "TRG_R5L79-C18-097950-CJ-CHEILJEDANG-KFOOD-GLOBAL-CHANNEL-REORDER", "symbol": "097950", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"channel_reorder_score": 14, "distribution_expansion_score": 13, "volume_revenue_score": 13, "price_mix_score": 12, "margin_bridge_score": 13, "relative_strength_score": 11, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"channel_reorder_score": 16, "distribution_expansion_score": 15, "volume_revenue_score": 15, "price_mix_score": 14, "margin_bridge_score": 15, "relative_strength_score": 10, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_after": 83, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["channel_reorder_score", "distribution_expansion_score", "volume_revenue_score", "price_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified overseas channel reorder, volume/revenue, price/mix and margin bridge; avoid both durable Stage2 and forced 4B when channel reset is bounded but weak.", "MFE_90D_pct": 38.24, "MAE_90D_pct": -2.6, "score_return_alignment_label": "consumer_channel_reorder_positive_with_lifecycle_4b", "current_profile_verdict": "C18 should allow K-food/global food positives when overseas channel reorder, distribution expansion, volume growth, price/mix and margin bridge are visible. CJ CheilJedang produced strong MFE with bounded entry-basis MAE, but later drawdown means channel/revenue/margin evidence must refresh."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L79-C18-017810-PULMUONE-GLOBAL-FOOD-CHANNEL-REORDER", "trigger_id": "TRG_R5L79-C18-017810-PULMUONE-GLOBAL-FOOD-CHANNEL-REORDER", "symbol": "017810", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"channel_reorder_score": 14, "distribution_expansion_score": 13, "volume_revenue_score": 13, "price_mix_score": 12, "margin_bridge_score": 13, "relative_strength_score": 11, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"channel_reorder_score": 16, "distribution_expansion_score": 15, "volume_revenue_score": 15, "price_mix_score": 14, "margin_bridge_score": 15, "relative_strength_score": 10, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_after": 83, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["channel_reorder_score", "distribution_expansion_score", "volume_revenue_score", "price_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified overseas channel reorder, volume/revenue, price/mix and margin bridge; avoid both durable Stage2 and forced 4B when channel reset is bounded but weak.", "MFE_90D_pct": 18.12, "MAE_90D_pct": -1.55, "score_return_alignment_label": "consumer_channel_reorder_positive_with_lifecycle_4b", "current_profile_verdict": "C18 should preserve food-channel positives when overseas/online channel reorder, product mix, volume, revenue conversion and margin bridge are visible. Pulmuone produced high MFE with very bounded entry-basis MAE, but post-peak drawdown requires lifecycle management."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L79-C18-271560-ORION-CHINA-CHANNEL-REORDER-RESET-BOUNDARY", "trigger_id": "TRG_R5L79-C18-271560-ORION-CHINA-CHANNEL-REORDER-RESET-BOUNDARY", "symbol": "271560", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"channel_reorder_score": 6, "distribution_expansion_score": 4, "volume_revenue_score": 3, "price_mix_score": 4, "margin_bridge_score": 2, "relative_strength_score": 4, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_before": 52, "stage_label_before": "RiskWatch / no durable Stage2", "raw_component_scores_after": {"channel_reorder_score": 4, "distribution_expansion_score": 2, "volume_revenue_score": 2, "price_mix_score": 3, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 48, "stage_label_after": "RiskWatch / no Stage2 and no forced 4B", "changed_components": ["channel_reorder_score", "distribution_expansion_score", "volume_revenue_score", "price_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified overseas channel reorder, volume/revenue, price/mix and margin bridge; avoid both durable Stage2 and forced 4B when channel reset is bounded but weak.", "MFE_90D_pct": 17.25, "MAE_90D_pct": -1.98, "score_return_alignment_label": "bounded_channel_reset_no_durable_stage2", "current_profile_verdict": "C18 should not treat all confectionery or China-channel reorder resets as durable Stage2. Orion produced bounded MAE and a modest recovery MFE, so it should not be forced into 4B, but the price path did not validate a high-conviction export/channel rerating either."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R5", "loop": 79, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_CHANNEL_REORDER_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C18 consumer export/channel symbols outside top-covered 003230/005180/004370/383220/161890 set, +3 K-food/global food/China-channel trigger families, +2 channel reorder positives, +1 bounded channel-reset no-Stage2 boundary, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R5", "loop": 79, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "axis": "Kfood_global_channel_reorder_revenue_margin_bridge_vs_China_channel_reorder_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C18 should split verified overseas channel reorder / revenue-margin rerating from bounded channel-reset beta. Stage2 requires overseas/channel reorder, volume or distribution expansion, price/mix, revenue conversion and margin bridge. If MFE fades and post-peak drawdown opens without bridge refresh, route to local 4B-watch. Bounded channel reset should remain RiskWatch/no durable Stage2, not forced 4B.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["097950", "017810", "271560"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": 79, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "bounded_channel_reset_no_forced_4B_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C18 needs overseas channel reorder, distribution, volume/revenue and margin proof. CJ CheilJedang and Pulmuone show channel-reorder positives after source repair; Orion shows a bounded China-channel reset boundary where durable Stage2 is not validated but forced local 4B is also too harsh."}
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
097950:
  name = CJ제일제당
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

017810:
  name = 풀무원
  corporate_action_candidate_dates = 1996-01-03, 1999-03-17, 1999-07-19, 2008-07-29, 2008-09-29, 2019-05-07
  selected window = 2024-02-01~D+180
  contamination = false

271560:
  name = 오리온
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C18 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C18 rule-shape discovery,
but coding-agent promotion requires non-proxy overseas channel reorder, distribution expansion, volume, repeat purchase, price/mix, revenue and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R5/C18 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
Kfood_global_channel_reorder_revenue_margin_bridge_vs_China_channel_reorder_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 097950, 017810 and 271560.
4. Keep generic C18 export/channel-reorder weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - overseas/export channel reorder is explicit,
   - distribution expansion or repeat-purchase volume is visible,
   - revenue conversion and price/mix bridge exist,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is consumer export/channel reorder beta only,
   - channel/revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not force local 4B when channel-reset rows have bounded MAE and no confirmed margin break.
8. Do not convert local 4B-watch into full 4B/4C without non-price channel loss, reorder collapse, inventory issue, financing or margin break.
9. Emit before/after diagnostics and reject if verified channel-reorder positives or bounded channel-reset rows are overblocked.
```

---

## Final round state

```text
completed_round = R5
completed_loop = 79
next_round = R6
next_loop = 79
round_schedule_status = valid
round_sector_consistency = pass
```


# E2R Stock-Web v12 Residual Research — R5 Loop 77 / L5 / C18

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 77,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 77,
  "computed_next_round": "R6",
  "computed_next_loop": 77,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_GLOBAL_DISTRIBUTION_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "consumer_export_channel_reorder_guardrail",
    "largecap_food_channel_margin_bridge",
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

Previous completed state in this interactive run: R4 / loop 77.

Therefore:

```text
scheduled_round = R5
scheduled_loop = 77
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
computed_next_round = R6
computed_next_loop = 77
```

R5 was routed to C18 because loop 76 used C19, and C20 is already very heavily covered.  
This file tests large-cap food / snack / global distribution channel reorder behavior rather than pure beauty/global distribution or retail inventory.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C18 is concentrated in:

```text
003230, 005180, 004370, 383220, 161890
```

This run uses three different symbols:

```text
097950 / CJ제일제당 / K-food global channel and margin bridge
280360 / 롯데웰푸드 / global snack channel reorder and margin bridge
271560 / 오리온 / global distribution beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C18 is not “음식료주가 올랐다.”

The mechanism must pass through:

```text
overseas channel expansion / export channel
→ reorder and sell-through
→ distributor inventory and pricing/product mix
→ margin conversion
→ durable rerating
```

수출 뉴스는 매대에 상품을 올리는 일이다.  
C18이 보려는 것은 그 상품이 실제로 팔리고, 다시 주문되고, 마진으로 돌아오는지다.

---

## Case 1 — Slow positive with lifecycle 4B: 097950 / CJ제일제당

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is K-food global channel reorder, sell-through, product mix, price-cost spread and margin evidence.

```text
evidence_family = KFOOD_GLOBAL_CHANNEL_REORDER_PRODUCT_MIX_PRICE_COST_MARGIN_BRIDGE
case_role = positive_slow_with_later_4b_watch
trigger_date = 2024-03-29
entry_date = 2024-04-01
entry_price = 295,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv`:

```text
2024-04-01,295000,315000,292500,311000
2024-04-04,320000,327000,315500,323500
2024-07-24,380500,390000,376500,385000
2024-07-31,379500,391000,377500,386500
2024-08-05,361000,361500,335000,343000
2024-10-25,272500,274000,267500,269500
```

### Backtest

```text
MFE_30D  = +10.85%
MAE_30D  = -3.39%
MFE_90D  = +32.54%
MAE_90D  = -3.39%
MFE_180D = +32.54%
MAE_180D = -9.32%
peak_180 = 391,000 on 2024-07-31
trough_180 = 267,500 on 2024-10-25
peak_to_later_drawdown = -31.59%
```

### Interpretation

This is a large-cap C18 slow positive.  
The path was not explosive like small-cap K-food names, but it had controlled MAE and a visible mid-year MFE.

Correct treatment:

```text
verified reorder / mix / margin bridge → Stage2-Yellow possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Positive with lifecycle 4B: 280360 / 롯데웰푸드

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is global snack/ice-cream channel reorder, product mix, pricing and margin bridge evidence.

```text
evidence_family = GLOBAL_SNACK_ICECREAM_CHANNEL_REORDER_PRODUCT_MIX_PRICING_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-04-18
entry_date = 2024-04-19
entry_price = 124,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv`:

```text
2024-04-19,124000,129200,123100,127000
2024-05-22,143500,150000,140800,149800
2024-06-10,159000,185500,159000,177900
2024-06-18,199800,208500,191100,193300
2024-08-05,159900,159900,143500,148500
2024-11-04,126400,126400,117100,120500
```

### Backtest

```text
MFE_30D  = +22.18%
MAE_30D  = -0.73%
MFE_90D  = +68.15%
MAE_90D  = -0.73%
MFE_180D = +68.15%
MAE_180D = -5.56%
peak_180 = 208,500 on 2024-06-18
trough_180 = 117,100 on 2024-11-04
peak_to_later_drawdown = -43.84%
```

### Interpretation

This is a stronger C18 positive.  
It should be protected after source repair, but not left as permanent Green after the global channel/margin bridge fades.

Correct treatment:

```text
Stage2 possible after source repair
lifecycle local 4B if channel reorder or margin bridge decays
```

---

## Case 3 — Counterexample / local 4B-watch: 271560 / 오리온

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests global snack/distribution beta without enough reorder, sell-through and margin bridge.

```text
evidence_family = GLOBAL_SNACK_DISTRIBUTION_THEME_WITH_WEAK_REORDER_MARGIN_BRIDGE
case_role = counterexample_global_channel_beta_local4b
trigger_date = 2024-04-01
entry_date = 2024-04-02
entry_price = 95,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv`:

```text
2024-04-02,95400,95600,93200,93200
2024-04-08,96900,98600,95800,97200
2024-08-05,88600,89300,81800,83900
2024-09-27,96200,99900,96000,99600
2024-10-11,101600,102900,98500,99000
2024-10-25,98700,98700,96500,96800
```

### Backtest

```text
MFE_30D  = +3.35%
MAE_30D  = -5.56%
MFE_90D  = +6.39%
MAE_90D  = -6.92%
MFE_180D = +7.86%
MAE_180D = -14.26%
peak_180 = 102,900 on 2024-10-11
trough_180 = 81,800 on 2024-08-05
peak_to_later_drawdown = -18.56%
```

### Interpretation

This is not a hard failure, but it is a C18 false-positive boundary.  
Global distribution exposure alone did not produce durable rerating.

Correct treatment:

```text
global distribution beta
→ no verified reorder / sell-through / margin bridge
→ no durable Green
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
do_not_raise_generic_C18_Kfood_global_distribution_weight = true
do_not_treat_all_food_export_MFE_as_Green = true
do_not_convert_consumer_channel_drawdown_to_hard_4C_without_non_price_channel_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
KFOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_GLOBAL_DISTRIBUTION_BETA_FADE
```

This fine archetype covers:

```text
1. K-food/global channel reorder and product mix bridge → slow Stage2 possible after source repair
2. snack/ice-cream global channel reorder and pricing bridge → Stage2 possible, lifecycle-managed
3. global distribution beta without reorder/margin bridge → false Stage2 / no durable Green
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R5L77-C18-097950-CJ-CHEILJEDANG-KFOOD-CHANNEL-MARGIN-LIFECYCLE", "symbol": "097950", "company_name": "CJ제일제당", "round": "R5", "loop": "77", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_GLOBAL_DISTRIBUTION_BETA_FADE", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "positive", "best_trigger": "Stage2-SlowPositive-KFoodGlobalChannelMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should preserve large-cap food export/channel positives when global channel reorder, product mix, price-cost spread and margin bridge are visible. CJ CheilJedang produced moderate MFE with controlled MAE, then faded; it should be lifecycle-managed rather than treated as permanent Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy global channel reorder, sell-through, distributor inventory, pricing/product mix and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L77-C18-280360-LOTTE-WELLFOOD-GLOBAL-SNACK-CHANNEL-REORDER", "symbol": "280360", "company_name": "롯데웰푸드", "round": "R5", "loop": "77", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_GLOBAL_DISTRIBUTION_BETA_FADE", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-GlobalSnackChannelReorderMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should allow packaged-food/snack exporters when overseas channel reorder, category mix, pricing and margin bridge are visible. Lotte Wellfood produced high MFE with controlled MAE, but the later post-peak drawdown requires lifecycle local 4B if global channel/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy global channel reorder, sell-through, distributor inventory, pricing/product mix and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L77-C18-271560-ORION-GLOBAL-DISTRIBUTION-BETA-FADE", "symbol": "271560", "company_name": "오리온", "round": "R5", "loop": "77", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_GLOBAL_DISTRIBUTION_BETA_FADE", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / GlobalDistributionBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should not treat global snack distribution beta as durable Stage2 unless overseas reorder, sell-through, distributor inventory, pricing and margin bridge are visible. Orion had only limited MFE and a weak range-bound path, so it is a counterexample against generic global-distribution Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy global channel reorder, sell-through, distributor inventory, pricing/product mix and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R5L77-C18-097950-CJ-CHEILJEDANG-KFOOD-CHANNEL-MARGIN-LIFECYCLE", "case_id": "R5L77-C18-097950-CJ-CHEILJEDANG-KFOOD-CHANNEL-MARGIN-LIFECYCLE", "symbol": "097950", "company_name": "CJ제일제당", "round": "R5", "loop": "77", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_GLOBAL_DISTRIBUTION_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail", "trigger_type": "Stage2-SlowPositive-KFoodGlobalChannelMarginBridgeWithLifecycle4B", "trigger_date": "2024-03-29", "entry_date": "2024-04-01", "entry_price": 295000.0, "evidence_available_at_that_date": "KFOOD_GLOBAL_CHANNEL_REORDER_PRODUCT_MIX_PRICE_COST_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:CJ_CHEILJEDANG_2024_KFOOD_GLOBAL_CHANNEL_REORDER_PRODUCT_MIX_PRICE_COST_MARGIN_BRIDGE", "stage2_evidence_fields": ["global_channel_reorder_candidate", "sellthrough_or_distributor_inventory_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_product_mix_or_channel_expansion_candidate"], "stage4b_evidence_fields": ["global_distribution_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/097/097950/2024.csv", "profile_path": "atlas/symbol_profiles/097/097950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.85, "MFE_90D_pct": 32.54, "MFE_180D_pct": 32.54, "MAE_30D_pct": -3.39, "MAE_90D_pct": -3.39, "MAE_180D_pct": -9.32, "peak_date": "2024-07-31", "peak_price": 391000.0, "drawdown_after_peak_pct": -31.59, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_consumer_export_peak_if_reorder_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_loss_reorder_failure_inventory_margin_or_fx_break", "trigger_outcome_label": "positive_slow_with_later_4b_watch", "current_profile_verdict": "C18 should preserve large-cap food export/channel positives when global channel reorder, product mix, price-cost spread and margin bridge are visible. CJ CheilJedang produced moderate MFE with controlled MAE, then faded; it should be lifecycle-managed rather than treated as permanent Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C18_CONSUMER_EXPORT_097950_2024-04-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L77-C18-280360-LOTTE-WELLFOOD-GLOBAL-SNACK-CHANNEL-REORDER", "case_id": "R5L77-C18-280360-LOTTE-WELLFOOD-GLOBAL-SNACK-CHANNEL-REORDER", "symbol": "280360", "company_name": "롯데웰푸드", "round": "R5", "loop": "77", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_GLOBAL_DISTRIBUTION_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail", "trigger_type": "Stage2-Actionable-GlobalSnackChannelReorderMarginBridgeWithLifecycle4B", "trigger_date": "2024-04-18", "entry_date": "2024-04-19", "entry_price": 124000.0, "evidence_available_at_that_date": "GLOBAL_SNACK_ICECREAM_CHANNEL_REORDER_PRODUCT_MIX_PRICING_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LOTTE_WELLFOOD_2024_GLOBAL_SNACK_ICECREAM_CHANNEL_REORDER_PRODUCT_MIX_PRICING_MARGIN_BRIDGE", "stage2_evidence_fields": ["global_channel_reorder_candidate", "sellthrough_or_distributor_inventory_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_product_mix_or_channel_expansion_candidate"], "stage4b_evidence_fields": ["global_distribution_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv", "profile_path": "atlas/symbol_profiles/280/280360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.18, "MFE_90D_pct": 68.15, "MFE_180D_pct": 68.15, "MAE_30D_pct": -0.73, "MAE_90D_pct": -0.73, "MAE_180D_pct": -5.56, "peak_date": "2024-06-18", "peak_price": 208500.0, "drawdown_after_peak_pct": -43.84, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_consumer_export_peak_if_reorder_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_loss_reorder_failure_inventory_margin_or_fx_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C18 should allow packaged-food/snack exporters when overseas channel reorder, category mix, pricing and margin bridge are visible. Lotte Wellfood produced high MFE with controlled MAE, but the later post-peak drawdown requires lifecycle local 4B if global channel/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C18_CONSUMER_EXPORT_280360_2024-04-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L77-C18-271560-ORION-GLOBAL-DISTRIBUTION-BETA-FADE", "case_id": "R5L77-C18-271560-ORION-GLOBAL-DISTRIBUTION-BETA-FADE", "symbol": "271560", "company_name": "오리온", "round": "R5", "loop": "77", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_GLOBAL_DISTRIBUTION_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail", "trigger_type": "Stage2-FalsePositive / GlobalDistributionBetaFade", "trigger_date": "2024-04-01", "entry_date": "2024-04-02", "entry_price": 95400.0, "evidence_available_at_that_date": "GLOBAL_SNACK_DISTRIBUTION_THEME_WITH_WEAK_REORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ORION_2024_GLOBAL_SNACK_DISTRIBUTION_REORDER_SELLTHROUGH_PRICING_MARGIN_BRIDGE", "stage2_evidence_fields": ["global_channel_reorder_candidate", "sellthrough_or_distributor_inventory_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_product_mix_or_channel_expansion_candidate"], "stage4b_evidence_fields": ["global_distribution_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv", "profile_path": "atlas/symbol_profiles/271/271560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.35, "MFE_90D_pct": 6.39, "MFE_180D_pct": 7.86, "MAE_30D_pct": -5.56, "MAE_90D_pct": -6.92, "MAE_180D_pct": -14.26, "peak_date": "2024-10-11", "peak_price": 102900.0, "drawdown_after_peak_pct": -18.56, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_consumer_export_peak_if_reorder_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_loss_reorder_failure_inventory_margin_or_fx_break", "trigger_outcome_label": "counterexample_global_channel_beta_local4b", "current_profile_verdict": "C18 should not treat global snack distribution beta as durable Stage2 unless overseas reorder, sell-through, distributor inventory, pricing and margin bridge are visible. Orion had only limited MFE and a weak range-bound path, so it is a counterexample against generic global-distribution Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C18_CONSUMER_EXPORT_271560_2024-04-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L77-C18-097950-CJ-CHEILJEDANG-KFOOD-CHANNEL-MARGIN-LIFECYCLE", "trigger_id": "TRG_R5L77-C18-097950-CJ-CHEILJEDANG-KFOOD-CHANNEL-MARGIN-LIFECYCLE", "symbol": "097950", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"global_channel_score": 14, "reorder_sellthrough_score": 13, "distributor_inventory_score": 12, "pricing_product_mix_score": 13, "margin_bridge_score": 13, "relative_strength_score": 11, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2-Yellow candidate after source repair", "raw_component_scores_after": {"global_channel_score": 16, "reorder_sellthrough_score": 15, "distributor_inventory_score": 14, "pricing_product_mix_score": 15, "margin_bridge_score": 15, "relative_strength_score": 10, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["global_channel_score", "reorder_sellthrough_score", "pricing_product_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified overseas channel reorder, sell-through/distributor inventory, pricing/product mix and margin bridge; cap global distribution beta when reorder/margin evidence fails to refresh.", "MFE_90D_pct": 32.54, "MAE_90D_pct": -3.39, "score_return_alignment_label": "consumer_export_channel_positive_with_lifecycle_4b", "current_profile_verdict": "C18 should preserve large-cap food export/channel positives when global channel reorder, product mix, price-cost spread and margin bridge are visible. CJ CheilJedang produced moderate MFE with controlled MAE, then faded; it should be lifecycle-managed rather than treated as permanent Green."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L77-C18-280360-LOTTE-WELLFOOD-GLOBAL-SNACK-CHANNEL-REORDER", "trigger_id": "TRG_R5L77-C18-280360-LOTTE-WELLFOOD-GLOBAL-SNACK-CHANNEL-REORDER", "symbol": "280360", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"global_channel_score": 14, "reorder_sellthrough_score": 13, "distributor_inventory_score": 12, "pricing_product_mix_score": 13, "margin_bridge_score": 13, "relative_strength_score": 11, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2-Yellow candidate after source repair", "raw_component_scores_after": {"global_channel_score": 16, "reorder_sellthrough_score": 15, "distributor_inventory_score": 14, "pricing_product_mix_score": 15, "margin_bridge_score": 15, "relative_strength_score": 10, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["global_channel_score", "reorder_sellthrough_score", "pricing_product_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified overseas channel reorder, sell-through/distributor inventory, pricing/product mix and margin bridge; cap global distribution beta when reorder/margin evidence fails to refresh.", "MFE_90D_pct": 68.15, "MAE_90D_pct": -0.73, "score_return_alignment_label": "consumer_export_channel_positive_with_lifecycle_4b", "current_profile_verdict": "C18 should allow packaged-food/snack exporters when overseas channel reorder, category mix, pricing and margin bridge are visible. Lotte Wellfood produced high MFE with controlled MAE, but the later post-peak drawdown requires lifecycle local 4B if global channel/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L77-C18-271560-ORION-GLOBAL-DISTRIBUTION-BETA-FADE", "trigger_id": "TRG_R5L77-C18-271560-ORION-GLOBAL-DISTRIBUTION-BETA-FADE", "symbol": "271560", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"global_channel_score": 6, "reorder_sellthrough_score": 3, "distributor_inventory_score": 3, "pricing_product_mix_score": 3, "margin_bridge_score": 2, "relative_strength_score": 3, "execution_risk_score": 17, "source_confidence_score": 2}, "weighted_score_before": 48, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"global_channel_score": 3, "reorder_sellthrough_score": 2, "distributor_inventory_score": 1, "pricing_product_mix_score": 1, "margin_bridge_score": 1, "relative_strength_score": 2, "execution_risk_score": 20, "source_confidence_score": 2}, "weighted_score_after": 35, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["global_channel_score", "reorder_sellthrough_score", "pricing_product_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified overseas channel reorder, sell-through/distributor inventory, pricing/product mix and margin bridge; cap global distribution beta when reorder/margin evidence fails to refresh.", "MFE_90D_pct": 6.39, "MAE_90D_pct": -6.92, "score_return_alignment_label": "false_positive_global_distribution_bridge_gap", "current_profile_verdict": "C18 should not treat global snack distribution beta as durable Stage2 unless overseas reorder, sell-through, distributor inventory, pricing and margin bridge are visible. Orion had only limited MFE and a weak range-bound path, so it is a counterexample against generic global-distribution Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R5", "loop": 77, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "KFOOD_GLOBAL_CHANNEL_REORDER_MARGIN_BRIDGE_VS_GLOBAL_DISTRIBUTION_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C18 food/global-channel symbols outside top-covered Samyang/Binggrae/Nongshim set, +3 largecap-Kfood/snack/global-distribution trigger families, +2 channel-margin positives, +1 global distribution beta counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R5", "loop": 77, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "axis": "Kfood_global_channel_reorder_margin_bridge_vs_global_distribution_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C18 should split verified consumer export/channel reorder rerating from generic global distribution beta. Stage2 requires overseas channel reorder, sell-through or distributor inventory normalization, pricing/product mix and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["097950", "280360", "271560"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": 77, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C18 needs overseas channel reorder and margin proof. CJ CheilJedang and Lotte Wellfood show large-cap food/snack channel-margin candidates after source repair; Orion shows global distribution beta with weak MFE and no durable reorder/margin bridge."}
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
  corporate_action_candidate_dates = none
  selected window = 2024-04-01~D+180
  contamination = false

280360:
  name = 롯데웰푸드 from 2023-04-14, 롯데제과 before that
  corporate_action_candidate_dates = 2019-01-04, 2022-07-20
  selected window = 2024-04-19~D+180
  contamination = false

271560:
  corporate_action_candidate_dates = none
  selected window = 2024-04-02~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C18 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C18 rule-shape discovery,
but coding-agent promotion requires non-proxy global channel reorder, sell-through, distributor inventory, pricing/product mix and margin evidence.
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
Kfood_global_channel_reorder_margin_bridge_vs_global_distribution_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 097950, 280360 and 271560.
4. Keep generic C18 consumer-export/channel-reorder weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - overseas channel expansion or export exposure is explicit,
   - reorder and sell-through are visible,
   - distributor inventory, pricing/product mix or channel productivity bridge exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is K-food/global distribution beta only,
   - reorder/sell-through/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price channel loss, reorder failure, distributor inventory issue, pricing/margin collapse, FX or financing evidence.
8. Emit before/after diagnostics and reject if verified large-cap food channel positives are overblocked.
```

---

## Final round state

```text
completed_round = R5
completed_loop = 77
next_round = R6
next_loop = 77
round_schedule_status = valid
round_sector_consistency = pass
```


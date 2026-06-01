# E2R Stock-Web v12 Residual Research — R5 Loop 75 / L5 / C18

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 75,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 75,
  "computed_next_round": "R6",
  "computed_next_loop": 75,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_THEME_SPIKE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "channel_reorder_margin_bridge_guardrail",
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

Previous completed state in this interactive run: R4 / loop 75.

Therefore:

```text
scheduled_round = R5
scheduled_loop = 75
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
computed_next_round = R6
computed_next_loop = 75
```

R5 was routed to C18 because loop 74 used C19 and C20 remains heavily covered.  
This file tests K-food / consumer export channel reorder, not generic food/beauty distribution.

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
280360 / 롯데웰푸드 / confectionery export-channel margin bridge
017810 / 풀무원 / US tofu/HMR refrigerated channel reorder
011150 / CJ씨푸드 / K-food seafood theme spike fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate.
```

## Research thesis

C18 is not “food stock went up.”

The mechanism is:

```text
export/channel attention
→ sell-through and reorder cadence
→ product mix / utilization / logistics
→ margin conversion
→ durable rerating
```

A shelf listing is a door opening.  
A reorder is the customer coming back through the door.

---

## Case 1 — Positive with lifecycle 4B: 280360 / 롯데웰푸드

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is export channel reorder, overseas sell-through, confectionery product mix and margin bridge evidence.

```text
evidence_family = K_FOOD_CONFECTIONERY_EXPORT_CHANNEL_REORDER_PRODUCT_MIX_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-04-10
entry_date = 2024-04-11
entry_price = 122,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv`:

```text
2024-04-11,122000,125100,121500,124700
2024-04-18,120400,124700,120400,124000
2024-06-18,199800,208500,191100,193300
2024-08-05,159900,159900,143500,148500
2024-09-06,134300,134600,129000,129600
```

### Backtest

```text
MFE_30D  = +23.36%
MAE_30D  = -1.31%
MFE_90D  = +70.90%
MAE_90D  = -1.31%
MFE_180D = +70.90%
MAE_180D = -1.31%
peak_180 = 208,500 on 2024-06-18
trough_180 = 120,400 on 2024-04-18
peak_to_later_drawdown = -38.13%
```

### Interpretation

This is a strong C18 positive-shaped row.  
The early MAE was controlled and the MFE was large. But the later drawdown says the model should demand actual channel reorder and margin bridge before durable Green.

---

## Case 2 — Positive with later 4B-watch: 017810 / 풀무원

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is US tofu/HMR refrigerated channel reorder, utilization, logistics and margin bridge evidence.

```text
evidence_family = US_TOFU_HMR_REFRIGERATED_CHANNEL_REORDER_UTILIZATION_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-03-29
entry_date = 2024-04-01
entry_price = 10,670
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv`:

```text
2024-04-01,10670,11180,10650,11100
2024-04-11,11190,11190,10350,10960
2024-07-24,14540,15050,14250,14320
2024-08-05,12660,12960,11000,11920
2024-09-11,10150,10360,10010,10140
```

### Backtest

```text
MFE_30D  = +14.25%
MAE_30D  = -2.99%
MFE_90D  = +41.05%
MAE_90D  = -2.99%
MFE_180D = +41.05%
MAE_180D = -6.18%
peak_180 = 15,050 on 2024-07-24
trough_180 = 10,010 on 2024-09-11
peak_to_later_drawdown = -33.49%
```

### Interpretation

This is the slower channel-reorder version of C18.  
It should not be ignored just because it is less explosive than confectionery names. But it still needs non-price reorder and margin evidence before runtime promotion.

---

## Case 3 — Counterexample / local 4B: 011150 / CJ씨푸드

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests K-food / seafood export theme spike without enough visible reorder and margin bridge.

```text
evidence_family = KIM_SEAFOOD_KFOOD_EXPORT_THEME_SPIKE_WITH_WEAK_REORDER_MARGIN_BRIDGE
case_role = counterexample_theme_spike_local4b
trigger_date = 2024-04-11
entry_date = 2024-04-12
entry_price = 2,635
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/011/011150/2024.csv`:

```text
2024-04-12,2635,2985,2635,2750
2024-05-16,3045,3635,3025,3590
2024-05-24,4110,5370,4075,5050
2024-06-14,5140,6460,4920,6320
2024-08-05,3760,3795,3270,3420
2024-10-25,3090,3105,3030,3080
```

### Backtest

```text
MFE_30D  = +36.43%
MAE_30D  = +0.00%
MFE_90D  = +145.16%
MAE_90D  = +0.00%
MFE_180D = +145.16%
MAE_180D = +0.00%
peak_180 = 6,460 on 2024-06-14
post_peak_later_trough = 3,030 on 2024-10-25
peak_to_later_drawdown = -53.10%
```

### Interpretation

This is not a bad-entry counterexample.  
It is more dangerous: a huge tradable MFE that can fool a scoring model into calling the move durable Green.

C18 should treat this as:

```text
theme-spike MFE
→ source repair required
→ local 4B-watch after bridge fade
```

unless sell-through, reorder cadence and margin conversion are verified.

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
do_not_raise_generic_C18_Kfood_weight = true
do_not_treat_all_export_channel_MFE_as_Green = true
do_not_convert_theme_spike_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_THEME_SPIKE_FADE
```

This fine archetype covers:

```text
1. confectionery export channel reorder + product mix bridge → Stage2 possible after source repair
2. US tofu/HMR refrigerated channel reorder → Stage2 possible, with lifecycle decay
3. seafood/K-food theme spike without reorder bridge → false Stage2 / local 4B after peak
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R5L75-C18-280360-LOTTE-WELLFOOD-KFOOD-EXPORT-CHANNEL-MARGIN", "symbol": "280360", "company_name": "롯데웰푸드", "round": "R5", "loop": "75", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_THEME_SPIKE_FADE", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-KFoodExportChannelMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should allow Stage2 when K-food/export attention is tied to channel reorder, overseas sell-through, product mix and margin bridge. Lotte Wellfood produced large MFE with controlled early MAE, but post-peak drawdown requires lifecycle local 4B if channel reorder evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy channel reorder, sell-through, customer/channel expansion, product mix, utilization and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L75-C18-017810-PULMUONE-TOFU-HMR-US-CHANNEL-REORDER", "symbol": "017810", "company_name": "풀무원", "round": "R5", "loop": "75", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_THEME_SPIKE_FADE", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-USChannelReorderMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should include food names when overseas refrigerated channel reorder, utilization, logistics and margin conversion are visible. Pulmuone produced a clean multi-month MFE path, but later drawdown says the model needs lifecycle decay if reorder/margin evidence stalls.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy channel reorder, sell-through, customer/channel expansion, product mix, utilization and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L75-C18-011150-CJ-SEAFOOD-KFOOD-THEME-SPIKE-FADE", "symbol": "011150", "company_name": "CJ씨푸드", "round": "R5", "loop": "75", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_THEME_SPIKE_FADE", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / KFoodThemeSpikeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should not treat K-food or seafood export theme spikes as durable Stage2 unless sell-through, reorder cadence, customer/channel expansion and margin bridge are visible. CJ Seafood had an enormous tradable MFE but then a sharp post-peak drawdown, so it is a theme-spike local 4B row rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy channel reorder, sell-through, customer/channel expansion, product mix, utilization and margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R5L75-C18-280360-LOTTE-WELLFOOD-KFOOD-EXPORT-CHANNEL-MARGIN", "case_id": "R5L75-C18-280360-LOTTE-WELLFOOD-KFOOD-EXPORT-CHANNEL-MARGIN", "symbol": "280360", "company_name": "롯데웰푸드", "round": "R5", "loop": "75", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|channel_reorder_margin_bridge_guardrail", "trigger_type": "Stage2-Actionable-KFoodExportChannelMarginBridge", "trigger_date": "2024-04-10", "entry_date": "2024-04-11", "entry_price": 122000.0, "evidence_available_at_that_date": "K_FOOD_CONFECTIONERY_EXPORT_CHANNEL_REORDER_PRODUCT_MIX_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LOTTE_WELLFOOD_2024_KFOOD_CONFECTIONERY_EXPORT_CHANNEL_REORDER_PRODUCT_MIX_MARGIN_BRIDGE", "stage2_evidence_fields": ["export_channel_candidate", "reorder_or_sellthrough_candidate", "product_mix_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "channel_expansion_or_utilization_bridge_candidate"], "stage4b_evidence_fields": ["theme_spike", "bridge_stale_or_absent", "post_peak_drawdown", "reorder_fade"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv", "profile_path": "atlas/symbol_profiles/280/280360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 23.36, "MFE_90D_pct": 70.9, "MFE_180D_pct": 70.9, "MAE_30D_pct": -1.31, "MAE_90D_pct": -1.31, "MAE_180D_pct": -1.31, "peak_date": "2024-06-18", "peak_price": 208500.0, "drawdown_after_peak_pct": -38.13, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_export_channel_peak_if_reorder_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reorder_customer_channel_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C18 should allow Stage2 when K-food/export attention is tied to channel reorder, overseas sell-through, product mix and margin bridge. Lotte Wellfood produced large MFE with controlled early MAE, but post-peak drawdown requires lifecycle local 4B if channel reorder evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C18_EXPORT_REORDER_280360_2024-04-11", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L75-C18-017810-PULMUONE-TOFU-HMR-US-CHANNEL-REORDER", "case_id": "R5L75-C18-017810-PULMUONE-TOFU-HMR-US-CHANNEL-REORDER", "symbol": "017810", "company_name": "풀무원", "round": "R5", "loop": "75", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|channel_reorder_margin_bridge_guardrail", "trigger_type": "Stage2-Actionable-USChannelReorderMarginBridge", "trigger_date": "2024-03-29", "entry_date": "2024-04-01", "entry_price": 10670.0, "evidence_available_at_that_date": "US_TOFU_HMR_REFRIGERATED_CHANNEL_REORDER_UTILIZATION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:PULMUONE_2024_US_TOFU_HMR_REFRIGERATED_CHANNEL_REORDER_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["export_channel_candidate", "reorder_or_sellthrough_candidate", "product_mix_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "channel_expansion_or_utilization_bridge_candidate"], "stage4b_evidence_fields": ["theme_spike", "bridge_stale_or_absent", "post_peak_drawdown", "reorder_fade"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017810/2024.csv", "profile_path": "atlas/symbol_profiles/017/017810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.25, "MFE_90D_pct": 41.05, "MFE_180D_pct": 41.05, "MAE_30D_pct": -2.99, "MAE_90D_pct": -2.99, "MAE_180D_pct": -6.18, "peak_date": "2024-07-24", "peak_price": 15050.0, "drawdown_after_peak_pct": -33.49, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_export_channel_peak_if_reorder_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reorder_customer_channel_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C18 should include food names when overseas refrigerated channel reorder, utilization, logistics and margin conversion are visible. Pulmuone produced a clean multi-month MFE path, but later drawdown says the model needs lifecycle decay if reorder/margin evidence stalls.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C18_EXPORT_REORDER_017810_2024-04-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L75-C18-011150-CJ-SEAFOOD-KFOOD-THEME-SPIKE-FADE", "case_id": "R5L75-C18-011150-CJ-SEAFOOD-KFOOD-THEME-SPIKE-FADE", "symbol": "011150", "company_name": "CJ씨푸드", "round": "R5", "loop": "75", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|channel_reorder_margin_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / KFoodThemeSpikeFade", "trigger_date": "2024-04-11", "entry_date": "2024-04-12", "entry_price": 2635.0, "evidence_available_at_that_date": "KIM_SEAFOOD_KFOOD_EXPORT_THEME_SPIKE_WITH_WEAK_REORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:CJ_SEAFOOD_2024_KFOOD_SEAWEED_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE", "stage2_evidence_fields": ["export_channel_candidate", "reorder_or_sellthrough_candidate", "product_mix_or_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "channel_expansion_or_utilization_bridge_candidate"], "stage4b_evidence_fields": ["theme_spike", "bridge_stale_or_absent", "post_peak_drawdown", "reorder_fade"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011150/2024.csv", "profile_path": "atlas/symbol_profiles/011/011150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 36.43, "MFE_90D_pct": 145.16, "MFE_180D_pct": 145.16, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-06-14", "peak_price": 6460.0, "drawdown_after_peak_pct": -53.1, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_export_channel_peak_if_reorder_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_reorder_customer_channel_or_margin_break", "trigger_outcome_label": "counterexample_theme_spike_local4b", "current_profile_verdict": "C18 should not treat K-food or seafood export theme spikes as durable Stage2 unless sell-through, reorder cadence, customer/channel expansion and margin bridge are visible. CJ Seafood had an enormous tradable MFE but then a sharp post-peak drawdown, so it is a theme-spike local 4B row rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C18_EXPORT_REORDER_011150_2024-04-12", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L75-C18-280360-LOTTE-WELLFOOD-KFOOD-EXPORT-CHANNEL-MARGIN", "trigger_id": "TRG_R5L75-C18-280360-LOTTE-WELLFOOD-KFOOD-EXPORT-CHANNEL-MARGIN", "symbol": "280360", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"channel_expansion_score": 14, "reorder_sellthrough_score": 13, "product_mix_score": 12, "margin_bridge_score": 13, "relative_strength_score": 14, "customer_quality_score": 10, "execution_risk_score": 6, "source_confidence_score": 2}, "weighted_score_before": 84, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"channel_expansion_score": 16, "reorder_sellthrough_score": 15, "product_mix_score": 13, "margin_bridge_score": 15, "relative_strength_score": 13, "customer_quality_score": 11, "execution_risk_score": 6, "source_confidence_score": 2}, "weighted_score_after": 90, "stage_label_after": "Stage2/Green candidate after source repair + lifecycle 4B", "changed_components": ["channel_expansion_score", "reorder_sellthrough_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified export/channel reorder, sell-through, product mix and margin bridge; cap theme-spike MFE when reorder or margin bridge is absent.", "MFE_90D_pct": 70.9, "MAE_90D_pct": -1.31, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C18 should allow Stage2 when K-food/export attention is tied to channel reorder, overseas sell-through, product mix and margin bridge. Lotte Wellfood produced large MFE with controlled early MAE, but post-peak drawdown requires lifecycle local 4B if channel reorder evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L75-C18-017810-PULMUONE-TOFU-HMR-US-CHANNEL-REORDER", "trigger_id": "TRG_R5L75-C18-017810-PULMUONE-TOFU-HMR-US-CHANNEL-REORDER", "symbol": "017810", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"channel_expansion_score": 14, "reorder_sellthrough_score": 13, "product_mix_score": 12, "margin_bridge_score": 13, "relative_strength_score": 14, "customer_quality_score": 10, "execution_risk_score": 6, "source_confidence_score": 2}, "weighted_score_before": 84, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"channel_expansion_score": 16, "reorder_sellthrough_score": 15, "product_mix_score": 13, "margin_bridge_score": 15, "relative_strength_score": 13, "customer_quality_score": 11, "execution_risk_score": 6, "source_confidence_score": 2}, "weighted_score_after": 90, "stage_label_after": "Stage2/Green candidate after source repair + lifecycle 4B", "changed_components": ["channel_expansion_score", "reorder_sellthrough_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified export/channel reorder, sell-through, product mix and margin bridge; cap theme-spike MFE when reorder or margin bridge is absent.", "MFE_90D_pct": 41.05, "MAE_90D_pct": -2.99, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C18 should include food names when overseas refrigerated channel reorder, utilization, logistics and margin conversion are visible. Pulmuone produced a clean multi-month MFE path, but later drawdown says the model needs lifecycle decay if reorder/margin evidence stalls."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L75-C18-011150-CJ-SEAFOOD-KFOOD-THEME-SPIKE-FADE", "trigger_id": "TRG_R5L75-C18-011150-CJ-SEAFOOD-KFOOD-THEME-SPIKE-FADE", "symbol": "011150", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"channel_expansion_score": 7, "reorder_sellthrough_score": 3, "product_mix_score": 3, "margin_bridge_score": 2, "relative_strength_score": 14, "customer_quality_score": 3, "execution_risk_score": 17, "source_confidence_score": 2}, "weighted_score_before": 55, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"channel_expansion_score": 4, "reorder_sellthrough_score": 2, "product_mix_score": 2, "margin_bridge_score": 1, "relative_strength_score": 5, "customer_quality_score": 2, "execution_risk_score": 20, "source_confidence_score": 2}, "weighted_score_after": 42, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["channel_expansion_score", "reorder_sellthrough_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified export/channel reorder, sell-through, product mix and margin bridge; cap theme-spike MFE when reorder or margin bridge is absent.", "MFE_90D_pct": 145.16, "MAE_90D_pct": 0.0, "score_return_alignment_label": "false_positive_theme_spike_reorder_bridge_gap", "current_profile_verdict": "C18 should not treat K-food or seafood export theme spikes as durable Stage2 unless sell-through, reorder cadence, customer/channel expansion and margin bridge are visible. CJ Seafood had an enormous tradable MFE but then a sharp post-peak drawdown, so it is a theme-spike local 4B row rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R5", "loop": 75, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_FOOD_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_THEME_SPIKE_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C18 K-food/channel symbols outside top-covered set, +3 confectionery/tofu-HMR/seafood trigger families, +2 export-channel positives, +1 theme-spike local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R5", "loop": 75, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "axis": "k_food_export_channel_reorder_margin_bridge_vs_theme_spike_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C18 should split verified export/channel reorder and margin bridge from K-food theme spikes. Stage2 requires overseas channel expansion, reorder cadence, sell-through, product mix, utilization or margin conversion evidence. If MFE fades and post-peak drawdown opens without reorder evidence, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["280360", "017810", "011150"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": 75, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C18 needs channel-reorder proof. Lotte Wellfood and Pulmuone show export/channel margin positives after source repair; CJ Seafood shows K-food/seafood theme-spike MFE fading into local 4B when reorder/margin bridge is absent."}
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
280360:
  corporate_action_candidate_dates = 2019-01-04, 2022-07-20
  selected window = 2024-04-11~D+180
  contamination = false

017810:
  corporate_action_candidate_dates = 1996-01-03, 1999-03-17, 1999-07-19, 2008-07-29, 2008-09-29, 2019-05-07
  selected window = 2024-04-01~D+180
  contamination = false

011150:
  corporate_action_candidate_dates = 2002-04-22
  selected window = 2024-04-12~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C18 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C18 rule-shape discovery,
but coding-agent promotion requires non-proxy channel reorder, sell-through, customer/channel expansion, product mix, utilization and margin evidence.
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
k_food_export_channel_reorder_margin_bridge_vs_theme_spike_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 280360, 017810 and 011150.
4. Keep generic C18 K-food/export-channel weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - export/channel expansion is explicit,
   - sell-through or reorder cadence is visible,
   - product mix, utilization, logistics or margin bridge exists,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is K-food/export theme spike only,
   - reorder or margin evidence is weak/stale,
   - post-peak drawdown <= -35% even if entry-basis MAE is controlled.
7. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, channel destocking, reorder break, margin collapse, logistics or financing evidence.
8. Emit before/after diagnostics and reject if verified export-channel reorder positives are overblocked.
```

---

## Final round state

```text
completed_round = R5
completed_loop = 75
next_round = R6
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```


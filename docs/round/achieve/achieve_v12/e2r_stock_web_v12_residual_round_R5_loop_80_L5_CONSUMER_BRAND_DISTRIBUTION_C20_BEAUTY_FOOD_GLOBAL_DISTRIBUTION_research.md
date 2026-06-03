# E2R Stock-Web v12 Residual Research — R5 Loop 80 / L5 / C20

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 80,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 80,
  "computed_next_round": "R6",
  "computed_next_loop": 80,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION",
  "fine_archetype_id": "BEAUTY_ODM_BRAND_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_RECOVERY_BOUNDARY",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "beauty_food_global_distribution_guardrail",
    "beauty_ODM_brand_global_channel_reorder_revenue_margin_bridge",
    "China_recovery_bounded_no_forced4B_boundary",
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

Previous completed state in this interactive run: R4 / loop 80.

Therefore:

```text
scheduled_round = R5
scheduled_loop = 80
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
computed_next_round = R6
computed_next_loop = 80
```

R5 was routed to C20 because loop 79 R5 used C18 and loop 78 R5 used C19.  
This file tests beauty ODM / beauty brand / China recovery distribution bridges.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C20 concentration in:

```text
257720, 018290, 003230, 090430, 237880
```

This run uses three different symbols:

```text
192820 / 코스맥스 / beauty ODM global channel reorder bridge
214420 / 토니모리 / beauty brand global channel lifecycle
051900 / LG생활건강 / China beauty recovery bounded no-forced-4B boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C20 is not “K-뷰티가 잘 팔린다.”

The mechanism must pass through:

```text
global channel attention
→ reorder or sell-through
→ customer / distributor quality
→ revenue conversion and product mix
→ margin bridge
→ durable rerating
```

뷰티 유통은 쇼윈도의 조명이 아니다.  
C20이 보려는 것은 그 조명 아래에서 실제 재주문, 판매 회전, 믹스, 마진이 반복되는지다.

---

## Case 1 — ODM/global positive: 192820 / 코스맥스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is beauty ODM global customer reorder, US/China volume, revenue conversion and margin bridge evidence.

```text
evidence_family = BEAUTY_ODM_GLOBAL_BRAND_CUSTOMER_REORDER_US_CHINA_VOLUME_REVENUE_MARGIN_BRIDGE
case_role = positive_ODM_global_channel_reorder_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 115,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv`:

```text
2024-02-01,115000,116400,111700,113700
2024-02-07,117900,123800,116700,120400
2024-03-15,103100,103300,99800,100800
2024-05-21,164100,175000,163200,172400
2024-06-14,191400,208000,184900,184900
2024-08-13,134500,134500,116000,117700
2024-10-31,147300,150900,144600,150900
```

### Backtest

```text
MFE_30D  = +7.65%
MAE_30D  = -13.22%
MFE_90D  = +80.87%
MAE_90D  = -13.22%
MFE_180D = +80.87%
MAE_180D = -13.22%
peak_180 = 208,000 on 2024-06-14
trough_180 = 99,800 on 2024-03-15
peak_to_later_drawdown = -44.23%
```

### Interpretation

This is a C20 ODM/global distribution positive.  
The move validated tradable global channel MFE, but the post-peak drawdown requires lifecycle management.

Correct treatment:

```text
verified ODM customer reorder / global volume / revenue / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Beauty brand lifecycle positive: 214420 / 토니모리

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is beauty brand global channel reorder, offline/online sell-through, revenue conversion, product mix and margin bridge evidence.

```text
evidence_family = BEAUTY_BRAND_GLOBAL_CHANNEL_REORDER_OFFLINE_ONLINE_SELLTHROUGH_REVENUE_MARGIN_BRIDGE
case_role = positive_brand_channel_reorder_with_later_high_MAE_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 6,380
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv`:

```text
2024-02-01,6380,6410,5800,5940
2024-02-29,5730,6510,5550,6290
2024-03-13,5590,5640,5310,5490
2024-05-10,9170,11000,8880,9940
2024-06-14,15380,17190,15090,15700
2024-08-05,9000,9110,7500,8090
2024-10-31,7250,7440,7130,7360
```

### Backtest

```text
MFE_30D  = +5.33%
MAE_30D  = -16.77%
MFE_90D  = +169.44%
MAE_90D  = -16.77%
MFE_180D = +169.44%
MAE_180D = -16.77%
peak_180 = 17,190 on 2024-06-14
trough_180 = 5,310 on 2024-03-13
peak_to_later_drawdown = -58.52%
```

### Interpretation

This is a C20 brand-channel lifecycle row.  
The MFE was huge, but it cannot stay permanent Green without sell-through/revenue/margin refresh.

Correct treatment:

```text
verified channel reorder / sell-through / product mix / margin bridge → Stage2 possible
bridge stale after peak → local 4B-watch
```

---

## Case 3 — Bounded China recovery boundary: 051900 / LG생활건강

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests China beauty recovery beta with bounded MAE but incomplete durable bridge proof.

```text
evidence_family = BEAUTY_CHINA_CHANNEL_RECOVERY_BRAND_RESET_WITH_BOUNDED_MAE_AND_REQUIRES_SELLTHROUGH_MARGIN_BRIDGE
case_role = overbearish_counterexample_bounded_China_recovery_no_forced4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 302,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv`:

```text
2024-02-01,302500,307500,300000,305500
2024-02-15,312500,342000,309000,322000
2024-03-20,359000,372000,355500,365000
2024-04-01,388000,408000,385000,405000
2024-08-05,351000,352000,321000,327000
2024-09-27,367500,391500,367000,383500
2024-10-31,330000,331500,326000,331500
```

### Backtest

```text
MFE_30D  = +13.06%
MAE_30D  = -0.83%
MFE_90D  = +34.88%
MAE_90D  = -0.83%
MFE_180D = +34.88%
MAE_180D = -0.83%
peak_180 = 408,000 on 2024-04-01
trough_180 = 300,000 on 2024-02-01~2024-02-14
peak_to_later_drawdown = -21.32%
```

### Interpretation

This is not forced local 4B.  
It is also not durable Stage2 without sell-through, channel inventory, product mix and margin evidence.

Correct treatment:

```text
China beauty recovery watch
bounded MAE
→ no forced 4B
→ no durable Stage2 without sell-through / inventory / margin bridge
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
bounded_recovery_no_forced_4B_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C20_Kbeauty_distribution_weight = true
do_not_treat_all_beauty_MFE_as_Green = true
do_not_force_4B_on_bounded_China_recovery_rows = true
do_not_convert_beauty_distribution_drawdown_to_hard_4C_without_non_price_channel_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
BEAUTY_ODM_BRAND_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_RECOVERY_BOUNDARY
```

This fine archetype covers:

```text
1. ODM global channel reorder / revenue bridge → Stage2 possible after source repair
2. beauty brand global channel sell-through bridge → Stage2 possible, lifecycle-managed
3. China beauty recovery bounded MAE → RiskWatch / no durable Stage2 / no forced 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R5L80-C20-192820-COSMAX-BEAUTY-ODM-GLOBAL-REORDER-MARGIN", "symbol": "192820", "company_name": "코스맥스", "round": "R5", "loop": "80", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "BEAUTY_ODM_BRAND_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_RECOVERY_BOUNDARY", "case_type": "beauty_food_global_distribution", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-BeautyODMGlobalChannelReorderMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C20 should protect beauty ODM/OEM positives when global channel reorder, customer quality, US/China volume, revenue conversion and margin bridge are visible. Cosmax produced a large MFE but later drawdown means lifecycle 4B is needed if channel/revenue/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy global channel reorder, customer/sell-through, revenue, brand mix and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L80-C20-214420-TONYMOLY-BEAUTY-BRAND-GLOBAL-CHANNEL-LIFECYCLE", "symbol": "214420", "company_name": "토니모리", "round": "R5", "loop": "80", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "BEAUTY_ODM_BRAND_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_RECOVERY_BOUNDARY", "case_type": "beauty_food_global_distribution", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-BeautyBrandGlobalChannelReorderWithHighMAELifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C20 should allow beauty-brand positives when global channel reorder, offline/online sell-through, product mix, revenue and margin bridge are visible. TonyMoly produced a very large MFE, but its post-peak drawdown requires lifecycle local 4B if sell-through or margin proof fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy global channel reorder, customer/sell-through, revenue, brand mix and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L80-C20-051900-LG-HH-CHINA-BRAND-RECOVERY-BOUNDARY", "symbol": "051900", "company_name": "LG생활건강", "round": "R5", "loop": "80", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "BEAUTY_ODM_BRAND_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_RECOVERY_BOUNDARY", "case_type": "beauty_food_global_distribution", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-ChinaBeautyBrandRecoveryBoundedNoForced4BNoDurableStage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C20 should not force bounded large-cap China beauty recovery rows into 4B when MAE is controlled, but it also should not mark durable Stage2 without sell-through, channel inventory, brand mix, revenue and margin bridge. LG H&H is a bounded no-forced-4B boundary.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy global channel reorder, customer/sell-through, revenue, brand mix and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R5L80-C20-192820-COSMAX-BEAUTY-ODM-GLOBAL-REORDER-MARGIN", "case_id": "R5L80-C20-192820-COSMAX-BEAUTY-ODM-GLOBAL-REORDER-MARGIN", "symbol": "192820", "company_name": "코스맥스", "round": "R5", "loop": "80", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "BEAUTY_ODM_BRAND_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_RECOVERY_BOUNDARY", "loop_objective": "coverage_gap_fill|counterexample_mining|beauty_food_global_distribution_guardrail", "trigger_type": "Stage2-Actionable-BeautyODMGlobalChannelReorderMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 115000.0, "evidence_available_at_that_date": "BEAUTY_ODM_GLOBAL_BRAND_CUSTOMER_REORDER_US_CHINA_VOLUME_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:COSMAX_2024_BEAUTY_ODM_GLOBAL_CHANNEL_REORDER_CUSTOMER_VOLUME_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["global_channel_reorder_candidate", "sellthrough_or_customer_quality_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "brand_mix_or_distribution_expansion_candidate"], "stage4b_evidence_fields": ["beauty_global_distribution_theme_beta", "bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv", "profile_path": "atlas/symbol_profiles/192/192820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.65, "MFE_90D_pct": 80.87, "MFE_180D_pct": 80.87, "MAE_30D_pct": -13.22, "MAE_90D_pct": -13.22, "MAE_180D_pct": -13.22, "peak_date": "2024-06-14", "peak_price": 208000.0, "drawdown_after_peak_pct": -44.23, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_beauty_distribution_peak_if_reorder_sellthrough_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_loss_inventory_overhang_brand_failure_margin_or_financing_break", "trigger_outcome_label": "positive_ODM_global_channel_reorder_with_later_4b_watch", "current_profile_verdict": "C20 should protect beauty ODM/OEM positives when global channel reorder, customer quality, US/China volume, revenue conversion and margin bridge are visible. Cosmax produced a large MFE but later drawdown means lifecycle 4B is needed if channel/revenue/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C20_BEAUTY_GLOBAL_192820_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L80-C20-214420-TONYMOLY-BEAUTY-BRAND-GLOBAL-CHANNEL-LIFECYCLE", "case_id": "R5L80-C20-214420-TONYMOLY-BEAUTY-BRAND-GLOBAL-CHANNEL-LIFECYCLE", "symbol": "214420", "company_name": "토니모리", "round": "R5", "loop": "80", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "BEAUTY_ODM_BRAND_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_RECOVERY_BOUNDARY", "loop_objective": "coverage_gap_fill|counterexample_mining|beauty_food_global_distribution_guardrail", "trigger_type": "Stage2-Actionable-BeautyBrandGlobalChannelReorderWithHighMAELifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 6380.0, "evidence_available_at_that_date": "BEAUTY_BRAND_GLOBAL_CHANNEL_REORDER_OFFLINE_ONLINE_SELLTHROUGH_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:TONYMOLY_2024_BEAUTY_BRAND_GLOBAL_CHANNEL_REORDER_SELLTHROUGH_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["global_channel_reorder_candidate", "sellthrough_or_customer_quality_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "brand_mix_or_distribution_expansion_candidate"], "stage4b_evidence_fields": ["beauty_global_distribution_theme_beta", "bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv", "profile_path": "atlas/symbol_profiles/214/214420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.33, "MFE_90D_pct": 169.44, "MFE_180D_pct": 169.44, "MAE_30D_pct": -16.77, "MAE_90D_pct": -16.77, "MAE_180D_pct": -16.77, "peak_date": "2024-06-14", "peak_price": 17190.0, "drawdown_after_peak_pct": -58.52, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_beauty_distribution_peak_if_reorder_sellthrough_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_loss_inventory_overhang_brand_failure_margin_or_financing_break", "trigger_outcome_label": "positive_brand_channel_reorder_with_later_high_MAE_4b_watch", "current_profile_verdict": "C20 should allow beauty-brand positives when global channel reorder, offline/online sell-through, product mix, revenue and margin bridge are visible. TonyMoly produced a very large MFE, but its post-peak drawdown requires lifecycle local 4B if sell-through or margin proof fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C20_BEAUTY_GLOBAL_214420_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L80-C20-051900-LG-HH-CHINA-BRAND-RECOVERY-BOUNDARY", "case_id": "R5L80-C20-051900-LG-HH-CHINA-BRAND-RECOVERY-BOUNDARY", "symbol": "051900", "company_name": "LG생활건강", "round": "R5", "loop": "80", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "BEAUTY_ODM_BRAND_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_RECOVERY_BOUNDARY", "loop_objective": "coverage_gap_fill|counterexample_mining|beauty_food_global_distribution_guardrail", "trigger_type": "RiskWatch-ChinaBeautyBrandRecoveryBoundedNoForced4BNoDurableStage2", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 302500.0, "evidence_available_at_that_date": "BEAUTY_CHINA_CHANNEL_RECOVERY_BRAND_RESET_WITH_BOUNDED_MAE_AND_REQUIRES_SELLTHROUGH_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LG_HH_2024_CHINA_BEAUTY_BRAND_RECOVERY_CHANNEL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE", "stage2_evidence_fields": ["global_channel_reorder_candidate", "sellthrough_or_customer_quality_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "brand_mix_or_distribution_expansion_candidate"], "stage4b_evidence_fields": ["beauty_global_distribution_theme_beta", "bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051900/2024.csv", "profile_path": "atlas/symbol_profiles/051/051900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.06, "MFE_90D_pct": 34.88, "MFE_180D_pct": 34.88, "MAE_30D_pct": -0.83, "MAE_90D_pct": -0.83, "MAE_180D_pct": -0.83, "peak_date": "2024-04-01", "peak_price": 408000.0, "drawdown_after_peak_pct": -21.32, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_beauty_distribution_peak_if_reorder_sellthrough_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_loss_inventory_overhang_brand_failure_margin_or_financing_break", "trigger_outcome_label": "overbearish_counterexample_bounded_China_recovery_no_forced4b", "current_profile_verdict": "C20 should not force bounded large-cap China beauty recovery rows into 4B when MAE is controlled, but it also should not mark durable Stage2 without sell-through, channel inventory, brand mix, revenue and margin bridge. LG H&H is a bounded no-forced-4B boundary.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C20_BEAUTY_GLOBAL_051900_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L80-C20-192820-COSMAX-BEAUTY-ODM-GLOBAL-REORDER-MARGIN", "trigger_id": "TRG_R5L80-C20-192820-COSMAX-BEAUTY-ODM-GLOBAL-REORDER-MARGIN", "symbol": "192820", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"global_channel_reorder_score": 14, "customer_sellthrough_score": 13, "brand_mix_distribution_score": 12, "revenue_conversion_score": 13, "margin_bridge_score": 13, "relative_strength_score": 12, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"global_channel_reorder_score": 16, "customer_sellthrough_score": 15, "brand_mix_distribution_score": 14, "revenue_conversion_score": 15, "margin_bridge_score": 15, "relative_strength_score": 11, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["global_channel_reorder_score", "customer_sellthrough_score", "brand_mix_distribution_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified global channel reorder, sell-through/customer quality, revenue conversion, brand mix and margin bridge; avoid forced 4B when large-cap China recovery rows have bounded MAE but incomplete bridge proof.", "MFE_90D_pct": 80.87, "MAE_90D_pct": -13.22, "score_return_alignment_label": "beauty_global_distribution_positive_with_lifecycle_4b", "current_profile_verdict": "C20 should protect beauty ODM/OEM positives when global channel reorder, customer quality, US/China volume, revenue conversion and margin bridge are visible. Cosmax produced a large MFE but later drawdown means lifecycle 4B is needed if channel/revenue/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L80-C20-214420-TONYMOLY-BEAUTY-BRAND-GLOBAL-CHANNEL-LIFECYCLE", "trigger_id": "TRG_R5L80-C20-214420-TONYMOLY-BEAUTY-BRAND-GLOBAL-CHANNEL-LIFECYCLE", "symbol": "214420", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"global_channel_reorder_score": 14, "customer_sellthrough_score": 13, "brand_mix_distribution_score": 12, "revenue_conversion_score": 13, "margin_bridge_score": 13, "relative_strength_score": 12, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"global_channel_reorder_score": 16, "customer_sellthrough_score": 15, "brand_mix_distribution_score": 14, "revenue_conversion_score": 15, "margin_bridge_score": 15, "relative_strength_score": 11, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["global_channel_reorder_score", "customer_sellthrough_score", "brand_mix_distribution_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified global channel reorder, sell-through/customer quality, revenue conversion, brand mix and margin bridge; avoid forced 4B when large-cap China recovery rows have bounded MAE but incomplete bridge proof.", "MFE_90D_pct": 169.44, "MAE_90D_pct": -16.77, "score_return_alignment_label": "beauty_global_distribution_positive_with_lifecycle_4b", "current_profile_verdict": "C20 should allow beauty-brand positives when global channel reorder, offline/online sell-through, product mix, revenue and margin bridge are visible. TonyMoly produced a very large MFE, but its post-peak drawdown requires lifecycle local 4B if sell-through or margin proof fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L80-C20-051900-LG-HH-CHINA-BRAND-RECOVERY-BOUNDARY", "trigger_id": "TRG_R5L80-C20-051900-LG-HH-CHINA-BRAND-RECOVERY-BOUNDARY", "symbol": "051900", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"global_channel_reorder_score": 8, "customer_sellthrough_score": 6, "brand_mix_distribution_score": 5, "revenue_conversion_score": 5, "margin_bridge_score": 4, "relative_strength_score": 12, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no forced 4B", "raw_component_scores_after": {"global_channel_reorder_score": 7, "customer_sellthrough_score": 5, "brand_mix_distribution_score": 4, "revenue_conversion_score": 4, "margin_bridge_score": 3, "relative_strength_score": 5, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / no durable Stage2 and no forced 4B", "changed_components": ["global_channel_reorder_score", "customer_sellthrough_score", "brand_mix_distribution_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified global channel reorder, sell-through/customer quality, revenue conversion, brand mix and margin bridge; avoid forced 4B when large-cap China recovery rows have bounded MAE but incomplete bridge proof.", "MFE_90D_pct": 34.88, "MAE_90D_pct": -0.83, "score_return_alignment_label": "bounded_china_beauty_recovery_no_forced4b_boundary", "current_profile_verdict": "C20 should not force bounded large-cap China beauty recovery rows into 4B when MAE is controlled, but it also should not mark durable Stage2 without sell-through, channel inventory, brand mix, revenue and margin bridge. LG H&H is a bounded no-forced-4B boundary."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R5", "loop": 80, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "BEAUTY_ODM_BRAND_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_CHINA_RECOVERY_BOUNDARY", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "overbearish_counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C20 beauty/global distribution symbols outside top-covered 257720/018290/003230/090430/237880 set, +3 ODM/brand/China-recovery trigger families, +2 beauty distribution positives, +1 bounded China recovery no-forced-4B boundary, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R5", "loop": 80, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "axis": "beauty_ODM_brand_global_channel_reorder_revenue_margin_bridge_vs_China_recovery_boundary", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C20 should split verified beauty/global distribution revenue-margin rerating from generic K-beauty/China recovery beta. Stage2 requires global channel reorder, customer or sell-through quality, distribution expansion, revenue conversion, brand/product mix and margin bridge. If MFE fades and post-peak drawdown opens without bridge refresh, route to local 4B-watch. Bounded China recovery rows should remain RiskWatch/no durable Stage2, not forced 4B.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["192820", "214420", "051900"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": 80, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "bounded_recovery_no_forced_4B_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C20 needs global channel reorder, customer/sell-through, revenue conversion, brand mix and margin proof. Cosmax and TonyMoly show beauty distribution MFE candidates after source repair; LG H&H shows a bounded China recovery boundary where durable Stage2 is not validated but forced 4B is too harsh."}
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
192820:
  name = 코스맥스
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

214420:
  name = 토니모리
  corporate_action_candidate_dates = 2016-12-09, 2022-01-06
  selected window = 2024-02-01~D+180
  contamination = false

051900:
  name = LG생활건강
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C20 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C20 rule-shape discovery,
but coding-agent promotion requires non-proxy global channel reorder, customer/sell-through, distribution expansion, revenue conversion, brand/product mix and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R5/C20 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
beauty_ODM_brand_global_channel_reorder_revenue_margin_bridge_vs_China_recovery_boundary

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 192820, 214420 and 051900.
4. Keep generic C20 beauty/global-distribution weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - global channel reorder or sell-through is explicit,
   - customer/distributor quality is visible,
   - revenue conversion and product/brand mix bridge exist,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is beauty/global distribution theme beta only,
   - channel/revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not force local 4B when China recovery rows have bounded MAE and no confirmed channel/margin break.
8. Do not convert local 4B-watch into full 4B/4C without non-price channel loss, inventory overhang, brand failure, financing or margin break.
9. Emit before/after diagnostics and reject if verified beauty distribution positives or bounded China recovery rows are overblocked.
```

---

## Final round state

```text
completed_round = R5
completed_loop = 80
next_round = R6
next_loop = 80
round_schedule_status = valid
round_sector_consistency = pass
```


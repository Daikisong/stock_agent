# E2R Stock-Web v12 Residual Research — R5 Loop 82 / L5 / C18

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 82,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 82,
  "computed_next_round": "R6",
  "computed_next_loop": 82,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_SPIKE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "consumer_export_channel_reorder_guardrail",
    "K_beauty_ODM_export_channel_reorder_margin_bridge",
    "brand_theme_spike_fade_boundary",
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

Previous completed state in this interactive run: R4 / loop 82.

Therefore:

```text
scheduled_round = R5
scheduled_loop = 82
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
computed_next_round = R6
computed_next_loop = 82
```

R5 was routed to C18 because loop 82 R4 used C17 and loop 81 R5 used C19.  
This file tests consumer export channel reorder and K-beauty ODM/brand channel bridges rather than retail inventory or broad beauty-food global distribution.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C18 concentration in:

```text
003230, 005180, 004370, 383220, 097950, 161890
```

This run uses three different symbols:

```text
241710 / 코스메카코리아 / K-beauty ODM export-channel reorder bridge
192820 / 코스맥스 / global ODM export channel reorder bridge
214420 / 토니모리 / K-beauty brand theme spike fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected 180D window.
```

## Research thesis

C18 is not “K-beauty가 올랐다.”

The mechanism must pass through:

```text
consumer export / channel headline
→ channel sell-through
→ reorder cadence and customer quality
→ capacity utilization
→ revenue conversion
→ margin bridge
→ durable rerating
```

소비재 수출은 쇼핑백 사진이 아니라 다시 들어오는 발주서다.  
C18이 보려는 것은 첫 판매의 불꽃이 실제 재주문, 채널 회전, 매출, 마진으로 이어지는지다.

---

## Case 1 — K-beauty ODM reorder positive: 241710 / 코스메카코리아

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is export channel sell-through, ODM customer quality, reorder cadence, capacity utilization, revenue conversion and margin bridge evidence.

```text
evidence_family = K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_CUSTOMER_QUALITY_REVENUE_MARGIN_BRIDGE
case_role = positive_Kbeauty_ODM_export_reorder_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 36,600
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv`:

```text
2024-02-01,36600,37700,35900,37700
2024-02-22,42100,44400,41750,42250
2024-03-25,33950,33950,31000,31350
2024-05-29,53600,62500,53000,60300
2024-07-24,85900,92500,84800,88800
2024-09-27,96000,98500,88000,90500
2024-10-25,74400,74700,70300,72500
2024-10-31,77500,79700,75300,79600
```

### Backtest

```text
MFE_30D  = +21.31%
MAE_30D  = -3.96%
MFE_90D  = +101.91%
MAE_90D  = -15.30%
MFE_180D = +169.13%
MAE_180D = -15.30%
peak_180 = 98,500 on 2024-09-27
trough_180 = 31,000 on 2024-03-25
peak_to_later_drawdown = -28.63%
```

### Interpretation

This is a strong C18 ODM/export-channel candidate after source repair.  
The price path had large MFE, but the interim MAE means the system should demand real channel and reorder proof before promotion.

Correct treatment:

```text
verified export-channel sell-through / ODM customer quality / reorder / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Global ODM reorder positive: 192820 / 코스맥스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is global brand customer quality, export channel sell-through, reorder cadence, capacity utilization, revenue conversion and margin bridge evidence.

```text
evidence_family = K_BEAUTY_ODM_GLOBAL_BRAND_CUSTOMER_REORDER_EXPORT_CHANNEL_REVENUE_MARGIN_BRIDGE
case_role = positive_bounded_Kbeauty_ODM_global_reorder_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 115,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv`:

```text
2024-02-01,115000,116400,111700,113700
2024-02-27,109300,110000,106100,106900
2024-03-07,106000,106300,100100,103300
2024-04-01,122000,131000,121000,130000
2024-07-25,154500,161200,152700,154100
2024-08-05,140000,143900,123200,129900
2024-08-13,134500,134500,116000,117700
2024-10-31,147300,150900,144600,150900
```

### Backtest

```text
MFE_30D  = +7.65%
MAE_30D  = -7.74%
MFE_90D  = +14.70%
MAE_90D  = -12.96%
MFE_180D = +40.17%
MAE_180D = -12.96%
peak_180 = 161,200 on 2024-07-25
trough_180 = 100,100 on 2024-03-07
peak_to_later_drawdown = -28.04%
```

### Interpretation

This is a C18 global ODM/channel reorder candidate, but not an automatic Green.  
The bridge needs to prove that the rerating came from global customer reorder and margin conversion rather than generic K-beauty beta.

Correct treatment:

```text
verified global customer reorder / export channel sell-through / utilization / margin bridge → Stage2-Yellow possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Brand theme-spike fade: 214420 / 토니모리

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests K-beauty brand/channel theme spike without enough direct sell-through and reorder bridge.

```text
evidence_family = K_BEAUTY_BRAND_EXPORT_CHANNEL_THEME_WITH_WEAK_REORDER_SELLTHROUGH_REVENUE_MARGIN_BRIDGE
case_role = counterexample_Kbeauty_brand_theme_spike_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 6,380
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv`:

```text
2024-02-01,6380,6410,5800,5940
2024-02-27,5830,5910,5320,5420
2024-04-01,6450,7940,6400,7220
2024-07-24,10330,10630,10120,10150
2024-08-05,9000,9110,7500,8090
2024-09-25,9750,10230,9610,9770
2024-09-27,9870,10470,9870,9910
2024-10-29,7540,7540,7160,7250
```

### Backtest

```text
MFE_30D  = +5.33%
MAE_30D  = -16.61%
MFE_90D  = +24.45%
MAE_90D  = -16.61%
MFE_180D = +96.24%
MAE_180D = -16.61%
peak_180 = 12,520 on 2024-09-25
trough_180 = 5,320 on 2024-02-27
peak_to_later_drawdown = -42.81%
```

### Interpretation

This is a C18 brand theme-spike local-4B boundary.  
The MFE was huge, but durable Stage2 needs direct channel sell-through and reorder evidence.

Correct treatment:

```text
K-beauty brand theme beta
→ no verified export-channel sell-through / reorder / revenue / margin bridge
→ local 4B-watch after spike
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
export_channel_reorder_bridge_required = strengthen
customer_quality_sellthrough_revenue_margin_guard = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C18_Kbeauty_theme_weight = true
do_not_treat_all_Kbeauty_MFE_as_Green = true
do_not_convert_brand_theme_spike_drawdown_to_hard_4C_without_non_price_channel_reorder_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_SPIKE_FADE
```

This fine archetype covers:

```text
1. ODM export-channel reorder bridge → Stage2 possible after source repair
2. global ODM customer/reorder bridge → Stage2-Yellow possible after source repair
3. brand theme spike without direct sell-through/reorder proof → false durable Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R5L82-C18-241710-COSMECCA-KOREA-ODM-EXPORT-REORDER", "symbol": "241710", "company_name": "코스메카코리아", "round": "R5", "loop": "82", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_SPIKE_FADE", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-KBeautyODMExportChannelReorderMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should protect ODM/export positives only when export channel sell-through, customer quality, reorder cadence, revenue conversion and margin bridge are visible. Cosmecca Korea produced very large MFE with moderate interim MAE, but later drawdown requires lifecycle 4B if channel/reorder proof fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export channel sell-through, customer quality, reorder cadence, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L82-C18-192820-COSMAX-ODM-GLOBAL-CHANNEL-REORDER", "symbol": "192820", "company_name": "코스맥스", "round": "R5", "loop": "82", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_SPIKE_FADE", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Yellow-KBeautyODMGlobalChannelReorderMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should allow global ODM/channel positives when customer mix, export channel sell-through, reorder cadence, capacity utilization, revenue conversion and margin bridge are visible. Cosmax had strong MFE but not without MAE, so source repair is required before Stage2 promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export channel sell-through, customer quality, reorder cadence, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L82-C18-214420-TONYMOLY-KBEAUTY-BRAND-THEME-SPIKE-FADE", "symbol": "214420", "company_name": "토니모리", "round": "R5", "loop": "82", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_SPIKE_FADE", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / KBeautyBrandChannelThemeSpikeFadeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should not treat K-beauty brand/channel theme spikes as durable Stage2 unless export sell-through, channel restocking, repeat order cadence, revenue and margin bridge are visible. TonyMoly had large MFE but also sharp post-peak fade, so it is a theme-spike/local-4B boundary until direct channel proof is repaired.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export channel sell-through, customer quality, reorder cadence, revenue conversion and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R5L82-C18-241710-COSMECCA-KOREA-ODM-EXPORT-REORDER", "case_id": "R5L82-C18-241710-COSMECCA-KOREA-ODM-EXPORT-REORDER", "symbol": "241710", "company_name": "코스메카코리아", "round": "R5", "loop": "82", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail", "trigger_type": "Stage2-Actionable-KBeautyODMExportChannelReorderMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 36600.0, "evidence_available_at_that_date": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_CUSTOMER_QUALITY_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:COSMECCA_KOREA_2024_K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["export_channel_candidate", "reorder_or_sellthrough_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_capacity_utilization_candidate"], "stage4b_evidence_fields": ["Kbeauty_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/241/241710/2024.csv", "profile_path": "atlas/symbol_profiles/241/241710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.31, "MFE_90D_pct": 101.91, "MFE_180D_pct": 169.13, "MAE_30D_pct": -3.96, "MAE_90D_pct": -15.3, "MAE_180D_pct": -15.3, "peak_date": "2024-09-27", "peak_price": 98500.0, "drawdown_after_peak_pct": -28.63, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_Kbeauty_channel_peak_if_reorder_sellthrough_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_collapse_reorder_loss_customer_loss_margin_or_financing_break", "trigger_outcome_label": "positive_Kbeauty_ODM_export_reorder_with_later_4b_watch", "current_profile_verdict": "C18 should protect ODM/export positives only when export channel sell-through, customer quality, reorder cadence, revenue conversion and margin bridge are visible. Cosmecca Korea produced very large MFE with moderate interim MAE, but later drawdown requires lifecycle 4B if channel/reorder proof fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C18_KBEAUTY_EXPORT_CHANNEL_241710_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L82-C18-192820-COSMAX-ODM-GLOBAL-CHANNEL-REORDER", "case_id": "R5L82-C18-192820-COSMAX-ODM-GLOBAL-CHANNEL-REORDER", "symbol": "192820", "company_name": "코스맥스", "round": "R5", "loop": "82", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail", "trigger_type": "Stage2-Yellow-KBeautyODMGlobalChannelReorderMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 115000.0, "evidence_available_at_that_date": "K_BEAUTY_ODM_GLOBAL_BRAND_CUSTOMER_REORDER_EXPORT_CHANNEL_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:COSMAX_2024_K_BEAUTY_ODM_GLOBAL_CUSTOMER_EXPORT_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["export_channel_candidate", "reorder_or_sellthrough_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_capacity_utilization_candidate"], "stage4b_evidence_fields": ["Kbeauty_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv", "profile_path": "atlas/symbol_profiles/192/192820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.65, "MFE_90D_pct": 14.7, "MFE_180D_pct": 40.17, "MAE_30D_pct": -7.74, "MAE_90D_pct": -12.96, "MAE_180D_pct": -12.96, "peak_date": "2024-07-25", "peak_price": 161200.0, "drawdown_after_peak_pct": -28.04, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_Kbeauty_channel_peak_if_reorder_sellthrough_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_collapse_reorder_loss_customer_loss_margin_or_financing_break", "trigger_outcome_label": "positive_bounded_Kbeauty_ODM_global_reorder_with_later_4b_watch", "current_profile_verdict": "C18 should allow global ODM/channel positives when customer mix, export channel sell-through, reorder cadence, capacity utilization, revenue conversion and margin bridge are visible. Cosmax had strong MFE but not without MAE, so source repair is required before Stage2 promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C18_KBEAUTY_EXPORT_CHANNEL_192820_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L82-C18-214420-TONYMOLY-KBEAUTY-BRAND-THEME-SPIKE-FADE", "case_id": "R5L82-C18-214420-TONYMOLY-KBEAUTY-BRAND-THEME-SPIKE-FADE", "symbol": "214420", "company_name": "토니모리", "round": "R5", "loop": "82", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_SPIKE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|consumer_export_channel_reorder_guardrail", "trigger_type": "Stage2-FalsePositive / KBeautyBrandChannelThemeSpikeFadeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 6380.0, "evidence_available_at_that_date": "K_BEAUTY_BRAND_EXPORT_CHANNEL_THEME_WITH_WEAK_REORDER_SELLTHROUGH_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:TONYMOLY_2024_K_BEAUTY_BRAND_EXPORT_CHANNEL_SELLTHROUGH_REORDER_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["export_channel_candidate", "reorder_or_sellthrough_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_capacity_utilization_candidate"], "stage4b_evidence_fields": ["Kbeauty_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv", "profile_path": "atlas/symbol_profiles/214/214420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.33, "MFE_90D_pct": 24.45, "MFE_180D_pct": 96.24, "MAE_30D_pct": -16.61, "MAE_90D_pct": -16.61, "MAE_180D_pct": -16.61, "peak_date": "2024-09-25", "peak_price": 12520.0, "drawdown_after_peak_pct": -42.81, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_Kbeauty_channel_peak_if_reorder_sellthrough_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_collapse_reorder_loss_customer_loss_margin_or_financing_break", "trigger_outcome_label": "counterexample_Kbeauty_brand_theme_spike_local4b", "current_profile_verdict": "C18 should not treat K-beauty brand/channel theme spikes as durable Stage2 unless export sell-through, channel restocking, repeat order cadence, revenue and margin bridge are visible. TonyMoly had large MFE but also sharp post-peak fade, so it is a theme-spike/local-4B boundary until direct channel proof is repaired.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C18_KBEAUTY_EXPORT_CHANNEL_214420_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L82-C18-241710-COSMECCA-KOREA-ODM-EXPORT-REORDER", "trigger_id": "TRG_R5L82-C18-241710-COSMECCA-KOREA-ODM-EXPORT-REORDER", "symbol": "241710", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"export_channel_score": 14, "reorder_sellthrough_score": 14, "customer_quality_score": 13, "capacity_utilization_score": 12, "revenue_margin_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"export_channel_score": 16, "reorder_sellthrough_score": 16, "customer_quality_score": 15, "capacity_utilization_score": 14, "revenue_margin_bridge_score": 15, "relative_strength_score": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["export_channel_score", "reorder_sellthrough_score", "customer_quality_score", "capacity_utilization_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified export-channel sell-through, reorder cadence, customer quality, utilization, revenue conversion and margin bridge; cap K-beauty brand theme spikes when bridge fails to refresh.", "MFE_90D_pct": 101.91, "MAE_90D_pct": -15.3, "score_return_alignment_label": "consumer_export_channel_reorder_positive_with_lifecycle_4b", "current_profile_verdict": "C18 should protect ODM/export positives only when export channel sell-through, customer quality, reorder cadence, revenue conversion and margin bridge are visible. Cosmecca Korea produced very large MFE with moderate interim MAE, but later drawdown requires lifecycle 4B if channel/reorder proof fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L82-C18-192820-COSMAX-ODM-GLOBAL-CHANNEL-REORDER", "trigger_id": "TRG_R5L82-C18-192820-COSMAX-ODM-GLOBAL-CHANNEL-REORDER", "symbol": "192820", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"export_channel_score": 14, "reorder_sellthrough_score": 14, "customer_quality_score": 13, "capacity_utilization_score": 12, "revenue_margin_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"export_channel_score": 16, "reorder_sellthrough_score": 16, "customer_quality_score": 15, "capacity_utilization_score": 14, "revenue_margin_bridge_score": 15, "relative_strength_score": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["export_channel_score", "reorder_sellthrough_score", "customer_quality_score", "capacity_utilization_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified export-channel sell-through, reorder cadence, customer quality, utilization, revenue conversion and margin bridge; cap K-beauty brand theme spikes when bridge fails to refresh.", "MFE_90D_pct": 14.7, "MAE_90D_pct": -12.96, "score_return_alignment_label": "consumer_export_channel_reorder_positive_with_lifecycle_4b", "current_profile_verdict": "C18 should allow global ODM/channel positives when customer mix, export channel sell-through, reorder cadence, capacity utilization, revenue conversion and margin bridge are visible. Cosmax had strong MFE but not without MAE, so source repair is required before Stage2 promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L82-C18-214420-TONYMOLY-KBEAUTY-BRAND-THEME-SPIKE-FADE", "trigger_id": "TRG_R5L82-C18-214420-TONYMOLY-KBEAUTY-BRAND-THEME-SPIKE-FADE", "symbol": "214420", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"export_channel_score": 5, "reorder_sellthrough_score": 3, "customer_quality_score": 3, "capacity_utilization_score": 2, "revenue_margin_bridge_score": 1, "relative_strength_score": 13, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_before": 43, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"export_channel_score": 3, "reorder_sellthrough_score": 1, "customer_quality_score": 1, "capacity_utilization_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 25, "source_confidence_score": 2}, "weighted_score_after": 32, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["export_channel_score", "reorder_sellthrough_score", "customer_quality_score", "capacity_utilization_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified export-channel sell-through, reorder cadence, customer quality, utilization, revenue conversion and margin bridge; cap K-beauty brand theme spikes when bridge fails to refresh.", "MFE_90D_pct": 24.45, "MAE_90D_pct": -16.61, "score_return_alignment_label": "false_positive_brand_channel_theme_spike_bridge_gap", "current_profile_verdict": "C18 should not treat K-beauty brand/channel theme spikes as durable Stage2 unless export sell-through, channel restocking, repeat order cadence, revenue and margin bridge are visible. TonyMoly had large MFE but also sharp post-peak fade, so it is a theme-spike/local-4B boundary until direct channel proof is repaired."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R5", "loop": 82, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_ODM_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_BRAND_THEME_SPIKE_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C18 consumer export/channel symbols outside top-covered 003230/005180/004370/383220/097950/161890 set, +3 K-beauty ODM/brand trigger families, +2 export-channel reorder positives, +1 brand theme-spike local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R5", "loop": 82, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "axis": "K_beauty_ODM_export_channel_reorder_margin_bridge_vs_brand_theme_spike_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C18 should split verified K-beauty ODM/export-channel reorder and margin rerating from generic brand/theme spikes. Stage2 requires export channel sell-through, customer quality, reorder cadence, capacity utilization, revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["241710", "192820", "214420"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": 82, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "existing_axis_strengthened": ["stage2_required_bridge", "export_channel_reorder_bridge_required", "customer_quality_sellthrough_revenue_margin_guard", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C18 needs consumer export/channel MFE to map into sell-through, reorder cadence, customer quality, capacity utilization, revenue conversion and margin proof. Cosmecca Korea and Cosmax show K-beauty ODM/export-channel positives after source repair; TonyMoly shows a K-beauty brand theme spike where durable Stage2 requires direct channel/reorder proof."}
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
241710:
  name = 코스메카코리아
  corporate_action_candidate_dates = 2018-04-25, 2018-05-18
  selected window = 2024-02-01~D+180
  contamination = false

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
```

Data-quality caveat:

```text
All selected C18 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C18 consumer export channel reorder rule-shape discovery,
but coding-agent promotion requires non-proxy export channel sell-through, customer quality, reorder cadence, capacity utilization, revenue conversion and margin evidence.
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
K_beauty_ODM_export_channel_reorder_margin_bridge_vs_brand_theme_spike_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 241710, 192820 and 214420.
4. Keep generic C18 consumer export/K-beauty theme weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - export channel sell-through is explicit,
   - customer quality and reorder cadence are visible,
   - capacity utilization or production conversion exists,
   - revenue conversion and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is K-beauty brand/channel theme beta only,
   - reorder / sell-through / revenue / margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price channel collapse, reorder loss, customer loss, financing or margin break.
8. Emit before/after diagnostics and reject if verified ODM/export-channel reorder positives are overblocked.
```

---

## Final round state

```text
completed_round = R5
completed_loop = 82
next_round = R6
next_loop = 82
round_schedule_status = valid
round_sector_consistency = pass
```


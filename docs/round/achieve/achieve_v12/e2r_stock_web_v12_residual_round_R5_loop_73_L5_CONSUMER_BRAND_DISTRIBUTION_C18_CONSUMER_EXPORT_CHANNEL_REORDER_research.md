# E2R Stock-Web v12 Residual Research — R5 Loop 73 / L5 / C18

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 73,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 73,
  "computed_next_round": "R6",
  "computed_next_loop": 73,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "fine_archetype_id": "K_BEAUTY_EXPORT_CHANNEL_REORDER_AND_ODM_CUSTOMER_VISIBILITY_VS_ONE_CANDLE_CHANNEL_BETA",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
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
```

## Round / scope resolution

Previous completed state in this interactive run: R4 / loop 73.

Therefore:

```text
scheduled_round = R5
scheduled_loop = 73
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
computed_next_round = R6
computed_next_loop = 73
```

R5 was routed to C18 because loop 72 had already filled C19 and C20 is already heavily covered.  
This run avoids top-covered C18 symbols and tests K-beauty export/channel reorder through new or underused names.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C18 is concentrated in `003230`, `005180`, `004370`, `383220`, and `161890`.  
This run uses:

```text
214420 / 토니모리 / small-brand K-beauty export-channel reorder
192820 / 코스맥스 / cosmetic ODM global customer reorder
018250 / 애경산업 / one-candle export-channel rally fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C18 is not “consumer stock went up.”

The mechanism has to pass through the channel:

```text
export demand / distributor order / platform sell-through
→ reorder visibility
→ margin or operating leverage
→ durable rerating
```

A first order is a knock on the door.  
A reorder is someone getting the key.

The residual split is:

```text
C18 positive:
  export channel + reorder or customer visibility + margin conversion

C18 false positive:
  one-candle channel optimism + no sell-through/reorder refresh + later MAE/drawdown

C18 local 4B:
  peak formed before reorder evidence refreshes
```

---

## Case 1 — Positive with later 4B-watch: 214420 / 토니모리

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is K-beauty export-channel reorder, sell-through, and operating leverage evidence.

```text
evidence_family = K_BEAUTY_EXPORT_CHANNEL_REORDER_SMALL_BRAND_OPERATING_LEVERAGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-04-29
entry_date = 2024-04-30
entry_price = 7,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv`:

```text
2024-04-30,7700,8940,7630,8600
2024-05-31,10670,11330,10430,10690
2024-06-14,15380,17190,15090,15700
2024-07-18,9920,9990,9580,9820
```

### Backtest

```text
MFE_30D  = +47.14%
MAE_30D  = -0.91%
MFE_90D  = +123.25%
MAE_90D  = -0.91%
MFE_180D = +123.25%
MAE_180D = -0.91%
peak_180 = 17,190 on 2024-06-14
trough_after_peak = 9,580 on 2024-07-18
peak_to_later_drawdown = -44.27%
```

### Interpretation

This is a valid C18 positive-shaped path, but it has a lifecycle warning.  
The early entry had almost no MAE and a very large MFE. After the peak, the drawdown opened enough that local 4B-watch should fire if reorder evidence stops refreshing.

---

## Case 2 — Positive: 192820 / 코스맥스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is global ODM customer reorder, channel demand, product/customer mix and margin conversion evidence.

```text
evidence_family = COSMETIC_ODM_GLOBAL_CUSTOMER_REORDER_MARGIN_BRIDGE
case_role = positive
trigger_date = 2024-04-26
entry_date = 2024-04-29
entry_price = 137,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv`:

```text
2024-04-29,137200,141500,133700,135000
2024-05-22,176000,177800,171200,171500
2024-06-14,191400,208000,184900,184900
2024-08-13,134500,134500,116000,117700
```

### Backtest

```text
MFE_30D  = +29.59%
MAE_30D  = -2.55%
MFE_90D  = +51.60%
MAE_90D  = -15.45%
MFE_180D = +51.60%
MAE_180D = -15.45%
peak_180 = 208,000 on 2024-06-14
trough_after_peak = 116,000 on 2024-08-13
peak_to_later_drawdown = -44.23%
```

### Interpretation

This is the ODM version of the C18 positive.  
The system should reward it only if global customer reorder and margin bridge are verified. The later drawdown is not hard 4C, but it does argue for lifecycle local 4B after the channel peak if bridge evidence becomes stale.

---

## Case 3 — Counterexample: 018250 / 애경산업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests a household/beauty export-channel rally that fails to sustain.

```text
evidence_family = HOUSEHOLD_BEAUTY_EXPORT_CHANNEL_REORDER_BETA_WITH_WEAK_REORDER_REFRESH
case_role = counterexample
trigger_date = 2024-04-24
entry_date = 2024-04-25
entry_price = 20,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/018/018250/2024.csv`:

```text
2024-04-25,20700,20950,20150,20250
2024-05-31,24250,26650,24200,25200
2024-08-05,19300,19850,16000,17510
2024-12-10,12120,13280,12120,13240
```

### Backtest

```text
MFE_30D  = +28.74%
MAE_30D  = -4.44%
MFE_90D  = +28.74%
MAE_90D  = -22.71%
MFE_180D = +28.74%
MAE_180D = -41.45%
peak_180 = 26,650 on 2024-05-31
trough_180 = 12,120 on 2024-12-10
peak_to_later_drawdown = -54.52%
```

### Interpretation

This is the C18 false-positive / local 4B path.  
A channel rally can be real and still not be a durable reorder cycle. Without sell-through or reorder refresh, the later drawdown says the system should cap the positive stage.

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C18_export_weight = true
do_not_treat_all_K_beauty_channel_rallies_as_Green = true
do_not_convert_channel_fade_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
K_BEAUTY_EXPORT_CHANNEL_REORDER_AND_ODM_CUSTOMER_VISIBILITY_VS_ONE_CANDLE_CHANNEL_BETA
```

This fine archetype covers:

```text
1. small-brand K-beauty export channel reorder → Stage2 possible after source repair, later local 4B after peak
2. cosmetic ODM global customer reorder → Stage2 possible after source repair
3. household/beauty channel rally without reorder refresh → false Stage2 / local 4B-watch
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER", "symbol": "214420", "company_name": "토니모리", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_EXPORT_CHANNEL_REORDER_AND_ODM_CUSTOMER_VISIBILITY_VS_ONE_CANDLE_CHANNEL_BETA", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-KBeautyExportChannelReorder", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should allow Stage2 when small-brand export/channel reorder connects to operating leverage, but should add local 4B-watch after a blowoff if reorder evidence stops refreshing.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export channel, reorder, sell-through, customer mix and margin evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER", "symbol": "192820", "company_name": "코스맥스", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_EXPORT_CHANNEL_REORDER_AND_ODM_CUSTOMER_VISIBILITY_VS_ONE_CANDLE_CHANNEL_BETA", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-ODMGlobalCustomerReorder", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should reward ODM/customer reorder only when global customer demand and margin conversion are visible. Cosmax shows a strong MFE path with manageable entry-basis MAE, but source repair is required before promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export channel, reorder, sell-through, customer mix and margin evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE", "symbol": "018250", "company_name": "애경산업", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_EXPORT_CHANNEL_REORDER_AND_ODM_CUSTOMER_VISIBILITY_VS_ONE_CANDLE_CHANNEL_BETA", "case_type": "consumer_export_channel_reorder", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ExportChannelOneCandleFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C18 should not treat a short export/channel rally as durable Green when reorder, sell-through or margin evidence fails to refresh. Aekyung generated MFE but later opened deep MAE and drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export channel, reorder, sell-through, customer mix and margin evidence must be attached before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER", "case_id": "R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER", "symbol": "214420", "company_name": "토니모리", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_EXPORT_CHANNEL_REORDER_AND_ODM_CUSTOMER_VISIBILITY_VS_ONE_CANDLE_CHANNEL_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-KBeautyExportChannelReorder", "trigger_date": "2024-04-29", "entry_date": "2024-04-30", "entry_price": 7700.0, "evidence_available_at_that_date": "K_BEAUTY_EXPORT_CHANNEL_REORDER_SMALL_BRAND_OPERATING_LEVERAGE", "evidence_source": "source_proxy_manual_verification_required:TONYMOLY_2024_K_BEAUTY_EXPORT_CHANNEL_REORDER_OPERATING_LEVERAGE", "stage2_evidence_fields": ["export_channel", "reorder_candidate", "consumer_brand_distribution"], "stage3_evidence_fields": ["relative_strength", "customer_or_channel_reorder_candidate"], "stage4b_evidence_fields": ["later_local_4b_after_reorder_peak_if_bridge_stale"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/214/214420/2024.csv", "profile_path": "atlas/symbol_profiles/214/214420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 47.14, "MFE_90D_pct": 123.25, "MFE_180D_pct": 123.25, "MAE_30D_pct": -0.91, "MAE_90D_pct": -0.91, "MAE_180D_pct": -0.91, "peak_date": "2024-06-14", "peak_price": 17190.0, "drawdown_after_peak_pct": -44.27, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_export_reorder_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C18 should allow Stage2 when small-brand export/channel reorder connects to operating leverage, but should add local 4B-watch after a blowoff if reorder evidence stops refreshing.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18_EXPORT_CHANNEL_214420_2024-04-30", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER", "case_id": "R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER", "symbol": "192820", "company_name": "코스맥스", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_EXPORT_CHANNEL_REORDER_AND_ODM_CUSTOMER_VISIBILITY_VS_ONE_CANDLE_CHANNEL_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-ODMGlobalCustomerReorder", "trigger_date": "2024-04-26", "entry_date": "2024-04-29", "entry_price": 137200.0, "evidence_available_at_that_date": "COSMETIC_ODM_GLOBAL_CUSTOMER_REORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:COSMAX_2024_GLOBAL_ODM_CUSTOMER_REORDER_MARGIN_BRIDGE", "stage2_evidence_fields": ["export_channel", "reorder_candidate", "consumer_brand_distribution"], "stage3_evidence_fields": ["relative_strength", "customer_or_channel_reorder_candidate"], "stage4b_evidence_fields": ["later_local_4b_after_reorder_peak_if_bridge_stale"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/192/192820/2024.csv", "profile_path": "atlas/symbol_profiles/192/192820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 29.59, "MFE_90D_pct": 51.6, "MFE_180D_pct": 51.6, "MAE_30D_pct": -2.55, "MAE_90D_pct": -15.45, "MAE_180D_pct": -15.45, "peak_date": "2024-06-14", "peak_price": 208000.0, "drawdown_after_peak_pct": -44.23, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_export_reorder_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_or_margin_break", "trigger_outcome_label": "positive", "current_profile_verdict": "C18 should reward ODM/customer reorder only when global customer demand and margin conversion are visible. Cosmax shows a strong MFE path with manageable entry-basis MAE, but source repair is required before promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18_EXPORT_CHANNEL_192820_2024-04-29", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE", "case_id": "R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE", "symbol": "018250", "company_name": "애경산업", "round": "R5", "loop": "73", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_EXPORT_CHANNEL_REORDER_AND_ODM_CUSTOMER_VISIBILITY_VS_ONE_CANDLE_CHANNEL_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / ExportChannelOneCandleFade", "trigger_date": "2024-04-24", "entry_date": "2024-04-25", "entry_price": 20700.0, "evidence_available_at_that_date": "HOUSEHOLD_BEAUTY_EXPORT_CHANNEL_REORDER_BETA_WITH_WEAK_REORDER_REFRESH", "evidence_source": "source_proxy_manual_verification_required:AEKYUNG_INDUSTRIAL_2024_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_REFRESH", "stage2_evidence_fields": ["export_channel", "reorder_candidate", "consumer_brand_distribution"], "stage3_evidence_fields": ["relative_strength", "customer_or_channel_reorder_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018250/2024.csv", "profile_path": "atlas/symbol_profiles/018/018250.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 28.74, "MFE_90D_pct": 28.74, "MFE_180D_pct": 28.74, "MAE_30D_pct": -4.44, "MAE_90D_pct": -22.71, "MAE_180D_pct": -41.45, "peak_date": "2024-05-31", "peak_price": 26650.0, "drawdown_after_peak_pct": -54.52, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_export_reorder_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_channel_or_margin_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C18 should not treat a short export/channel rally as durable Green when reorder, sell-through or margin evidence fails to refresh. Aekyung generated MFE but later opened deep MAE and drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18_EXPORT_CHANNEL_018250_2024-04-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER", "trigger_id": "TRG_R5L73-C18-214420-TONYMOLY-KBEAUTY-EXPORT-CHANNEL-REORDER", "symbol": "214420", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 10, "revision_score": 10, "relative_strength_score": 16, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 12, "revision_score": 11, "relative_strength_score": 16, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Yellow/Green candidate after source repair", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Reward only verified export-channel reorder and margin bridge; cap one-candle or stale channel beta when sell-through evidence fails to refresh and drawdown opens.", "MFE_90D_pct": 123.25, "MAE_90D_pct": -0.91, "score_return_alignment_label": "aligned_positive_or_lifecycle_positive", "current_profile_verdict": "C18 should allow Stage2 when small-brand export/channel reorder connects to operating leverage, but should add local 4B-watch after a blowoff if reorder evidence stops refreshing."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER", "trigger_id": "TRG_R5L73-C18-192820-COSMAX-ODM-GLOBAL-CUSTOMER-REORDER", "symbol": "192820", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 10, "revision_score": 10, "relative_strength_score": 16, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 12, "revision_score": 11, "relative_strength_score": 16, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Yellow/Green candidate after source repair", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Reward only verified export-channel reorder and margin bridge; cap one-candle or stale channel beta when sell-through evidence fails to refresh and drawdown opens.", "MFE_90D_pct": 51.6, "MAE_90D_pct": -15.45, "score_return_alignment_label": "aligned_positive_or_lifecycle_positive", "current_profile_verdict": "C18 should reward ODM/customer reorder only when global customer demand and margin conversion are visible. Cosmax shows a strong MFE path with manageable entry-basis MAE, but source repair is required before promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE", "trigger_id": "TRG_R5L73-C18-018250-AEKYUNG-EXPORT-CHANNEL-ONE-CANDLE-FADE", "symbol": "018250", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 9, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 53, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 16, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 44, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_quality_score", "margin_bridge_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Reward only verified export-channel reorder and margin bridge; cap one-candle or stale channel beta when sell-through evidence fails to refresh and drawdown opens.", "MFE_90D_pct": 28.74, "MAE_90D_pct": -22.71, "score_return_alignment_label": "false_positive_reorder_bridge_gap", "current_profile_verdict": "C18 should not treat a short export/channel rally as durable Green when reorder, sell-through or margin evidence fails to refresh. Aekyung generated MFE but later opened deep MAE and drawdown."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R5", "loop": 73, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "K_BEAUTY_EXPORT_CHANNEL_REORDER_AND_ODM_CUSTOMER_VISIBILITY_VS_ONE_CANDLE_CHANNEL_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C18 symbols, +3 export-channel/reorder trigger families, +2 K-beauty/ODM positives, +1 one-candle channel fade counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R5", "loop": 73, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "axis": "k_beauty_export_channel_reorder_and_odm_customer_visibility_vs_one_candle_channel_beta", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C18 should split verified export-channel reorder/ODM customer visibility from one-candle channel beta. Stage2 requires reorder, sell-through, customer/channel quality and margin conversion evidence. If MFE is followed by stale reorder evidence and post-peak drawdown, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["214420", "192820", "018250"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": 73, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C18 needs export-channel reorder proof. 토니모리 and 코스맥스 show K-beauty/ODM reorder positives with later lifecycle guards; 애경산업 shows a channel-reorder rally fading into local 4B when sell-through or margin evidence fails to refresh."}
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
214420:
  corporate_action_candidate_dates = 2016-12-09, 2022-01-06
  selected window = 2024-04-30~D+180
  contamination = false

192820:
  corporate_action_candidate_dates = none
  selected window = 2024-04-29~D+180
  contamination = false

018250:
  corporate_action_candidate_dates = none
  selected window = 2024-04-25~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C18 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C18 rule-shape discovery,
but coding-agent promotion requires non-proxy export channel, reorder, customer quality, sell-through and margin evidence.
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
k_beauty_export_channel_reorder_and_odm_customer_visibility_vs_one_candle_channel_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 214420, 192820 and 018250.
4. Keep generic C18 export-channel weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - export-channel or distributor evidence is explicit,
   - reorder or sell-through is visible,
   - customer/channel quality is improving,
   - margin or operating leverage conversion is visible,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - the trigger is one-candle channel/export beta,
   - reorder or sell-through evidence fails to refresh,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
8. Emit before/after diagnostics and reject if verified export-reorder positives are overblocked.
```

---

## Final round state

```text
completed_round = R5
completed_loop = 73
next_round = R6
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```


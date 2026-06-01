# E2R Stock-Web v12 Residual Research — R5 Loop 76 / L5 / C19

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R5",
  "scheduled_loop": 76,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R5",
  "completed_loop": 76,
  "computed_next_round": "R6",
  "computed_next_loop": 76,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN",
  "fine_archetype_id": "APPAREL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_RETAIL_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "brand_retail_inventory_margin_guardrail",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "share_count_validation_queue_creation"
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

Previous completed state in this interactive run: R4 / loop 76.

Therefore:

```text
scheduled_round = R5
scheduled_loop = 76
allowed_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_large_sector = L5_CONSUMER_BRAND_DISTRIBUTION
selected_canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
computed_next_round = R6
computed_next_loop = 76
```

R5 was routed to C19 because loop 75 used C18 and C20 is over-covered.  
This file tests brand/apparel inventory normalization and margin bridge behavior.

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
093050 / LF / apparel brand inventory-margin bridge
081660 / 휠라홀딩스 / global brand inventory destocking/channel margin bridge
020000 / 한섬 / apparel retail inventory beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
081660 and 020000 show share-count changes inside the selected window and require coding-agent validation before runtime promotion.
```

## Research thesis

C19 is not “retail stock went up.”

The mechanism must pass through:

```text
inventory normalization
→ sell-through / markdown control
→ channel productivity / product mix
→ gross margin and operating leverage
→ durable rerating
```

A retail rally is the shop window lighting up.  
The bridge is whether old stock clears without burning margin.

---

## Case 1 — Slow positive: 093050 / LF

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is apparel inventory normalization, DTC/channel productivity, product mix, markdown control and margin bridge evidence.

```text
evidence_family = APPAREL_BRAND_INVENTORY_NORMALIZATION_DTC_CHANNEL_PRODUCT_MIX_MARGIN_BRIDGE
case_role = positive_slow_boundary
trigger_date = 2024-02-29
entry_date = 2024-03-04
entry_price = 13,170
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv`:

```text
2024-03-04,13170,13170,13060,13110
2024-03-08,13650,14240,13530,14170
2024-03-28,15600,15920,15350,15400
2024-08-05,14220,14220,13090,13180
2024-09-09,14390,14940,14360,14940
```

### Backtest

```text
MFE_30D  = +20.88%
MAE_30D  = -0.84%
MFE_90D  = +20.88%
MAE_90D  = -0.84%
MFE_180D = +20.88%
MAE_180D = -0.84%
peak_180 = 15,920 on 2024-03-28
trough_180 = 13,060 on 2024-03-04
peak_to_later_drawdown = -17.84%
```

### Interpretation

This is a slow C19 positive.  
It is not explosive, but the low-MAE path is useful because C19 should not overfit only to high-beta consumer rows.

Correct treatment:

```text
Stage2-Yellow possible after source repair
protect slow inventory-margin positives
```

---

## Case 2 — Slow positive with validation: 081660 / 휠라홀딩스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is global brand inventory destocking, channel mix, royalty/brand margin and capital-return evidence.

```text
evidence_family = GLOBAL_SPORTS_BRAND_INVENTORY_DESTOCKING_CHANNEL_MIX_MARGIN_BRIDGE
case_role = positive_slow_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 39,800
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv`:

```text
2024-02-01,39800,40700,39800,40050
2024-02-13,40900,41900,40500,41900
2024-04-05,37500,38000,37300,37300
2024-08-01,42400,44550,42400,44450
2024-10-29,39250,39300,37950,38150
```

### Backtest

```text
MFE_30D  = +5.40%
MAE_30D  = -3.52%
MFE_90D  = +8.04%
MAE_90D  = -6.28%
MFE_180D = +11.93%
MAE_180D = -6.28%
peak_180 = 44,550 on 2024-08-01
trough_180 = 37,300 on 2024-04-05
peak_to_later_drawdown = -14.70%
```

### Interpretation

This is another slow brand-margin row.  
The path is not enough for Green without evidence, but it should be preserved as a potential C19 Yellow after source repair and share-count validation.

---

## Case 3 — Counterexample / local 4B-watch: 020000 / 한섬

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests apparel retail / inventory normalization beta without enough sell-through and markdown margin evidence.

```text
evidence_family = APPAREL_RETAIL_INVENTORY_THEME_WITH_WEAK_SELLTHROUGH_MARKDOWN_MARGIN_BRIDGE
case_role = counterexample_inventory_margin_fade_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 18,600
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/020/020000/2024.csv`:

```text
2024-02-01,18600,19400,18600,19300
2024-02-07,20100,21650,20050,21550
2024-03-11,19140,19420,19030,19190
2024-08-05,17100,17180,15640,16290
2024-10-29,15570,15740,15500,15620
```

### Backtest

```text
MFE_30D  = +16.40%
MAE_30D  = +0.00%
MFE_90D  = +16.40%
MAE_90D  = -4.46%
MFE_180D = +16.40%
MAE_180D = -15.91%
peak_180 = 21,650 on 2024-02-07
trough_180 = 15,640 on 2024-08-05
peak_to_later_drawdown = -27.76%
```

### Interpretation

This is not a hard 4C.  
But it is a C19 false-positive boundary: the initial MFE was tradable, then the path leaked lower.

Correct treatment:

```text
retail/inventory beta
→ no sell-through / markdown / margin bridge
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
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C19_retail_beta_weight = true
do_not_treat_slow_retail_MFE_as_Green_without_margin_bridge = true
do_not_convert_apparel_retail_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
APPAREL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_RETAIL_BETA_FADE
```

This fine archetype covers:

```text
1. apparel brand inventory-margin bridge → slow Stage2 possible after source repair
2. global sports brand destocking/channel margin bridge → slow Stage2 possible, validation required
3. apparel retail inventory beta without sell-through/markdown bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R5L76-C19-093050-LF-APPAREL-BRAND-INVENTORY-MARGIN-RECOVERY", "symbol": "093050", "company_name": "LF", "round": "R5", "loop": "76", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_RETAIL_BETA_FADE", "case_type": "brand_retail_inventory_margin", "positive_or_counterexample": "positive", "best_trigger": "Stage2-SlowPositive-ApparelBrandInventoryMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C19 should allow slow brand/retail positives when inventory normalization, DTC/channel mix, markdown control and margin bridge are visible. LF produced a moderate MFE with controlled MAE; not explosive, but useful to avoid overfitting C19 only to high-beta consumer names.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy sell-through, inventory normalization, markdown control, channel productivity, product mix and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L76-C19-081660-FILA-HOLDINGS-GLOBAL-BRAND-INVENTORY-MARGIN", "symbol": "081660", "company_name": "휠라홀딩스", "round": "R5", "loop": "76", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_RETAIL_BETA_FADE", "case_type": "brand_retail_inventory_margin", "positive_or_counterexample": "positive", "best_trigger": "Stage2-SlowPositive-GlobalBrandInventoryMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C19 should preserve low-MAE global brand rerating candidates when inventory destocking, channel mix, royalty/brand margin and capital return evidence are visible. FILA Holdings had modest MFE but a controlled risk profile; it still needs lifecycle monitoring if inventory/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy sell-through, inventory normalization, markdown control, channel productivity, product mix and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R5L76-C19-020000-HANDSOME-APPAREL-RETAIL-INVENTORY-BETA-FADE", "symbol": "020000", "company_name": "한섬", "round": "R5", "loop": "76", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_RETAIL_BETA_FADE", "case_type": "brand_retail_inventory_margin", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ApparelRetailInventoryBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C19 should not treat apparel retail or inventory-normalization beta as durable Stage2 unless sell-through, markdown control, channel productivity and margin bridge are visible. Handsome had a brief MFE but later faded into a lower range; share-count movement inside the window requires validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy sell-through, inventory normalization, markdown control, channel productivity, product mix and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R5L76-C19-093050-LF-APPAREL-BRAND-INVENTORY-MARGIN-RECOVERY", "case_id": "R5L76-C19-093050-LF-APPAREL-BRAND-INVENTORY-MARGIN-RECOVERY", "symbol": "093050", "company_name": "LF", "round": "R5", "loop": "76", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_RETAIL_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|brand_retail_inventory_margin_guardrail", "trigger_type": "Stage2-SlowPositive-ApparelBrandInventoryMarginBridge", "trigger_date": "2024-02-29", "entry_date": "2024-03-04", "entry_price": 13170.0, "evidence_available_at_that_date": "APPAREL_BRAND_INVENTORY_NORMALIZATION_DTC_CHANNEL_PRODUCT_MIX_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LF_2024_APPAREL_BRAND_INVENTORY_NORMALIZATION_CHANNEL_PRODUCT_MIX_MARGIN_BRIDGE", "stage2_evidence_fields": ["brand_or_retail_inventory_normalization", "sellthrough_or_markdown_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "DTC_channel_or_product_mix_candidate"], "stage4b_evidence_fields": ["inventory_or_retail_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv", "profile_path": "atlas/symbol_profiles/093/093050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.88, "MFE_90D_pct": 20.88, "MFE_180D_pct": 20.88, "MAE_30D_pct": -0.84, "MAE_90D_pct": -0.84, "MAE_180D_pct": -0.84, "peak_date": "2024-03-28", "peak_price": 15920.0, "drawdown_after_peak_pct": -17.84, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_brand_retail_peak_if_inventory_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_sellthrough_inventory_markdown_channel_or_margin_break", "trigger_outcome_label": "positive_slow_boundary", "current_profile_verdict": "C19 should allow slow brand/retail positives when inventory normalization, DTC/channel mix, markdown control and margin bridge are visible. LF produced a moderate MFE with controlled MAE; not explosive, but useful to avoid overfitting C19 only to high-beta consumer names.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C19_BRAND_RETAIL_093050_2024-03-04", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L76-C19-081660-FILA-HOLDINGS-GLOBAL-BRAND-INVENTORY-MARGIN", "case_id": "R5L76-C19-081660-FILA-HOLDINGS-GLOBAL-BRAND-INVENTORY-MARGIN", "symbol": "081660", "company_name": "휠라홀딩스", "round": "R5", "loop": "76", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_RETAIL_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|brand_retail_inventory_margin_guardrail", "trigger_type": "Stage2-SlowPositive-GlobalBrandInventoryMarginBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 39800.0, "evidence_available_at_that_date": "GLOBAL_SPORTS_BRAND_INVENTORY_DESTOCKING_CHANNEL_MIX_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:FILA_HOLDINGS_2024_GLOBAL_BRAND_INVENTORY_DESTOCKING_CHANNEL_MARGIN_CAPITAL_RETURN_BRIDGE", "stage2_evidence_fields": ["brand_or_retail_inventory_normalization", "sellthrough_or_markdown_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "DTC_channel_or_product_mix_candidate"], "stage4b_evidence_fields": ["inventory_or_retail_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv", "profile_path": "atlas/symbol_profiles/081/081660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.4, "MFE_90D_pct": 8.04, "MFE_180D_pct": 11.93, "MAE_30D_pct": -3.52, "MAE_90D_pct": -6.28, "MAE_180D_pct": -6.28, "peak_date": "2024-08-01", "peak_price": 44550.0, "drawdown_after_peak_pct": -14.7, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_brand_retail_peak_if_inventory_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_sellthrough_inventory_markdown_channel_or_margin_break", "trigger_outcome_label": "positive_slow_with_later_4b_watch", "current_profile_verdict": "C19 should preserve low-MAE global brand rerating candidates when inventory destocking, channel mix, royalty/brand margin and capital return evidence are visible. FILA Holdings had modest MFE but a controlled risk profile; it still needs lifecycle monitoring if inventory/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C19_BRAND_RETAIL_081660_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R5L76-C19-020000-HANDSOME-APPAREL-RETAIL-INVENTORY-BETA-FADE", "case_id": "R5L76-C19-020000-HANDSOME-APPAREL-RETAIL-INVENTORY-BETA-FADE", "symbol": "020000", "company_name": "한섬", "round": "R5", "loop": "76", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_RETAIL_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|brand_retail_inventory_margin_guardrail", "trigger_type": "Stage2-FalsePositive / ApparelRetailInventoryBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 18600.0, "evidence_available_at_that_date": "APPAREL_RETAIL_INVENTORY_THEME_WITH_WEAK_SELLTHROUGH_MARKDOWN_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANDSOME_2024_APPAREL_RETAIL_INVENTORY_SELLTHROUGH_MARKDOWN_CHANNEL_MARGIN_BRIDGE", "stage2_evidence_fields": ["brand_or_retail_inventory_normalization", "sellthrough_or_markdown_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "DTC_channel_or_product_mix_candidate"], "stage4b_evidence_fields": ["inventory_or_retail_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020000/2024.csv", "profile_path": "atlas/symbol_profiles/020/020000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.4, "MFE_90D_pct": 16.4, "MFE_180D_pct": 16.4, "MAE_30D_pct": 0.0, "MAE_90D_pct": -4.46, "MAE_180D_pct": -15.91, "peak_date": "2024-02-07", "peak_price": 21650.0, "drawdown_after_peak_pct": -27.76, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_brand_retail_peak_if_inventory_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_sellthrough_inventory_markdown_channel_or_margin_break", "trigger_outcome_label": "counterexample_inventory_margin_fade_with_sharecount_validation", "current_profile_verdict": "C19 should not treat apparel retail or inventory-normalization beta as durable Stage2 unless sell-through, markdown control, channel productivity and margin bridge are visible. Handsome had a brief MFE but later faded into a lower range; share-count movement inside the window requires validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C19_BRAND_RETAIL_020000_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L76-C19-093050-LF-APPAREL-BRAND-INVENTORY-MARGIN-RECOVERY", "trigger_id": "TRG_R5L76-C19-093050-LF-APPAREL-BRAND-INVENTORY-MARGIN-RECOVERY", "symbol": "093050", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"inventory_normalization_score": 12, "sellthrough_markdown_score": 12, "channel_product_mix_score": 11, "margin_bridge_score": 12, "relative_strength_score": 10, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 72, "stage_label_before": "Stage2-Yellow candidate after source repair", "raw_component_scores_after": {"inventory_normalization_score": 14, "sellthrough_markdown_score": 14, "channel_product_mix_score": 13, "margin_bridge_score": 14, "relative_strength_score": 9, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 78, "stage_label_after": "Stage2-Yellow after source repair + validation", "changed_components": ["inventory_normalization_score", "sellthrough_markdown_score", "channel_product_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified inventory normalization, sell-through, markdown control, product/channel mix and margin bridge; cap retail/apparel beta without those bridges.", "MFE_90D_pct": 20.88, "MAE_90D_pct": -0.84, "score_return_alignment_label": "slow_positive_inventory_margin_bridge", "current_profile_verdict": "C19 should allow slow brand/retail positives when inventory normalization, DTC/channel mix, markdown control and margin bridge are visible. LF produced a moderate MFE with controlled MAE; not explosive, but useful to avoid overfitting C19 only to high-beta consumer names."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L76-C19-081660-FILA-HOLDINGS-GLOBAL-BRAND-INVENTORY-MARGIN", "trigger_id": "TRG_R5L76-C19-081660-FILA-HOLDINGS-GLOBAL-BRAND-INVENTORY-MARGIN", "symbol": "081660", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"inventory_normalization_score": 12, "sellthrough_markdown_score": 12, "channel_product_mix_score": 11, "margin_bridge_score": 12, "relative_strength_score": 8, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 72, "stage_label_before": "Stage2-Yellow candidate after source repair", "raw_component_scores_after": {"inventory_normalization_score": 14, "sellthrough_markdown_score": 14, "channel_product_mix_score": 13, "margin_bridge_score": 14, "relative_strength_score": 8, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 78, "stage_label_after": "Stage2-Yellow after source repair + validation", "changed_components": ["inventory_normalization_score", "sellthrough_markdown_score", "channel_product_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified inventory normalization, sell-through, markdown control, product/channel mix and margin bridge; cap retail/apparel beta without those bridges.", "MFE_90D_pct": 8.04, "MAE_90D_pct": -6.28, "score_return_alignment_label": "slow_positive_inventory_margin_bridge", "current_profile_verdict": "C19 should preserve low-MAE global brand rerating candidates when inventory destocking, channel mix, royalty/brand margin and capital return evidence are visible. FILA Holdings had modest MFE but a controlled risk profile; it still needs lifecycle monitoring if inventory/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R5L76-C19-020000-HANDSOME-APPAREL-RETAIL-INVENTORY-BETA-FADE", "trigger_id": "TRG_R5L76-C19-020000-HANDSOME-APPAREL-RETAIL-INVENTORY-BETA-FADE", "symbol": "020000", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"inventory_normalization_score": 5, "sellthrough_markdown_score": 3, "channel_product_mix_score": 3, "margin_bridge_score": 2, "relative_strength_score": 10, "execution_risk_score": 16, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"inventory_normalization_score": 3, "sellthrough_markdown_score": 2, "channel_product_mix_score": 2, "margin_bridge_score": 1, "relative_strength_score": 9, "execution_risk_score": 19, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 39, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["inventory_normalization_score", "sellthrough_markdown_score", "channel_product_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified inventory normalization, sell-through, markdown control, product/channel mix and margin bridge; cap retail/apparel beta without those bridges.", "MFE_90D_pct": 16.4, "MAE_90D_pct": -4.46, "score_return_alignment_label": "false_positive_inventory_margin_bridge_gap", "current_profile_verdict": "C19 should not treat apparel retail or inventory-normalization beta as durable Stage2 unless sell-through, markdown control, channel productivity and margin bridge are visible. Handsome had a brief MFE but later faded into a lower range; share-count movement inside the window requires validation."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R5", "loop": 76, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_RETAIL_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "current_profile_error_count": 1, "diversity_score_summary": "+3 C19 apparel/brand retail symbols outside top-covered C19 set, +3 inventory/markdown/channel trigger families, +2 slow inventory-margin positives, +1 apparel retail beta fade counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R5", "loop": 76, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "axis": "apparel_brand_inventory_normalization_margin_bridge_vs_retail_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C19 should split verified inventory normalization and margin bridges from generic apparel/retail beta. Stage2 requires sell-through, markdown control, DTC/channel productivity, product mix or margin bridge. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["093050", "081660", "020000"], "share_count_validation_required": ["081660", "020000"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": 76, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C19 needs inventory/sell-through/margin proof. LF and FILA Holdings show slow brand inventory-margin candidates after source repair; Handsome shows apparel retail beta fading when sell-through/markdown/margin bridge is not verified."}
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
093050:
  corporate_action_candidate_dates = none
  selected window = 2024-03-04~D+180
  contamination = false

081660:
  name = 휠라홀딩스 in 2024, 미스토홀딩스 after 2025-04-18
  corporate_action_candidate_dates = 2018-05-09
  selected window = 2024-02-01~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required

020000:
  corporate_action_candidate_dates = 1997-01-03, 1999-07-26, 2003-07-15, 2008-01-16
  selected window = 2024-02-01~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C19 rows are source_proxy_only / evidence_url_pending.
081660 and 020000 also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C19 rule-shape discovery,
but coding-agent promotion requires non-proxy sell-through, inventory normalization, markdown control, channel productivity, product mix and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R5/C19 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and two rows need share-count validation.

Candidate axis:
apparel_brand_inventory_normalization_margin_bridge_vs_retail_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 093050, 081660 and 020000.
4. Validate 081660 and 020000 share-count changes inside the selected window.
5. Keep generic C19 retail/apparel beta weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - inventory normalization is explicit,
   - sell-through or markdown control is visible,
   - DTC/channel productivity or product mix bridge exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is deliberately slow/lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is apparel/retail/inventory beta only,
   - sell-through/markdown/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -25~35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price inventory impairment, channel sell-through failure, markdown/margin collapse, liquidity or financing evidence.
9. Emit before/after diagnostics and reject if verified slow inventory-margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R5
completed_loop = 76
next_round = R6
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```


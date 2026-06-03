# E2R Stock-Web v12 Residual Research — R4 Loop 74 / L4 / C15

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 74,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 74,
  "computed_next_round": "R5",
  "computed_next_loop": 74,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "COPPER_ALUMINUM_INDUSTRIAL_METAL_SPREAD_BRIDGE_VS_PRICE_ONLY_BETA_FADE",
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
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R3 / loop 74.

Therefore:

```text
scheduled_round = R4
scheduled_loop = 74
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
computed_next_round = R5
computed_next_loop = 74
```

R4 was routed to C15 because loop 73 used C17 and prior loops had already touched C16.  
No-Repeat shows C15 is thinner than C17, so this run tests copper/aluminum industrial-metal spread mechanics.

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
025820 / 이구산업 / copper fabricator spread bridge
012800 / 대창 / copper-brass price beta fade
001780 / 알루코 / aluminum profile price beta local 4B
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
001780 shows share-count changes inside the 2024 window and therefore requires coding-agent validation before runtime promotion.
```

## Research thesis

C15 is not “metal price went up.”

The true chain is:

```text
industrial metal price
→ product-specific spread
→ inventory/export/customer bridge
→ margin/revision conversion
→ durable rerating
```

A copper candle is the lightning.  
The margin bridge is the transformer that turns it into usable power.

The residual split is:

```text
C15 positive:
  copper/aluminum spread + inventory/export/product mix bridge
  + controlled early MAE
  + visible margin conversion

C15 false positive:
  commodity price beta
  + no spread-to-margin refresh
  + later MAE or post-peak drawdown

C15 local 4B:
  metal price peak fades before margin evidence refreshes
```

---

## Case 1 — Positive with later 4B-watch: 025820 / 이구산업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is copper product spread, inventory valuation, export price, customer/order and margin bridge evidence.

```text
evidence_family = COPPER_PRICE_SPREAD_FABRICATOR_INVENTORY_EXPORT_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-04-11
entry_date = 2024-04-12
entry_price = 5,690
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv`:

```text
2024-04-12,5690,6090,5460,5700
2024-05-20,7700,8420,7400,7880
2024-08-05,4365,4430,3795,3930
2024-12-09,3720,3780,3545,3560
```

### Backtest

```text
MFE_30D  = +47.98%
MAE_30D  = -4.04%
MFE_90D  = +47.98%
MAE_90D  = -33.30%
MFE_180D = +47.98%
MAE_180D = -37.70%
peak_180 = 8,420 on 2024-05-20
trough_180 = 3,545 on 2024-12-09
peak_to_later_drawdown = -57.90%
```

### Interpretation

This is the C15 positive-shaped row.  
The copper fabricator path produced large MFE and initially controlled MAE. But the later collapse says the model needs lifecycle local 4B if the spread-to-margin evidence stops refreshing.

---

## Case 2 — Counterexample / local 4B: 012800 / 대창

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests copper/brass price beta without verified spread-to-margin refresh.

```text
evidence_family = COPPER_BRASS_PRICE_BETA_WITH_WEAK_SPREAD_TO_MARGIN_REFRESH
case_role = counterexample
trigger_date = 2024-04-11
entry_date = 2024-04-12
entry_price = 1,470
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv`:

```text
2024-04-12,1470,1575,1450,1543
2024-05-21,2185,2320,2080,2175
2024-08-05,1277,1283,1100,1161
2024-11-15,1097,1138,1090,1132
```

### Backtest

```text
MFE_30D  = +57.82%
MAE_30D  = -4.49%
MFE_90D  = +57.82%
MAE_90D  = -25.17%
MFE_180D = +57.82%
MAE_180D = -25.85%
peak_180 = 2,320 on 2024-05-21
trough_180 = 1,090 on 2024-11-15
peak_to_later_drawdown = -53.02%
```

### Interpretation

This is the dangerous version of C15: MFE was huge, but the bridge failed.  
The model must not confuse a tradable copper beta squeeze with durable spread rerating.

The correct label is:

```text
false Stage2 / local 4B-watch
```

unless margin and inventory/export evidence refreshes.

---

## Case 3 — Counterexample / local 4B: 001780 / 알루코

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests aluminum/profile/battery-material price beta without clear product-mix and margin bridge.

```text
evidence_family = ALUMINUM_PROFILE_BATTERY_MATERIAL_PRICE_BETA_WITH_WEAK_MARGIN_BRIDGE
case_role = counterexample
trigger_date = 2024-04-11
entry_date = 2024-04-12
entry_price = 3,215
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/001/001780/2024.csv`:

```text
2024-04-12,3215,3385,3195,3280
2024-04-18,3595,3650,3320,3360
2024-07-22,2775,2800,2705,2720
2024-12-09,1901,1921,1755,1766
```

### Backtest

```text
MFE_30D  = +13.53%
MAE_30D  = -4.51%
MFE_90D  = +13.53%
MAE_90D  = -15.86%
MFE_180D = +13.53%
MAE_180D = -45.41%
peak_180 = 3,650 on 2024-04-18
trough_180 = 1,755 on 2024-12-09
peak_to_later_drawdown = -51.92%
```

### Interpretation

This is not a spread rerating.  
It is a price-beta fade. The stock did not deliver enough MFE to justify the later drawdown.

C15 should keep this in local 4B-watch unless non-price product mix and margin evidence appears.

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
do_not_raise_generic_C15_metal_weight = true
do_not_treat_all_copper_or_aluminum_beta_as_Green = true
do_not_convert_material_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
COPPER_ALUMINUM_INDUSTRIAL_METAL_SPREAD_BRIDGE_VS_PRICE_ONLY_BETA_FADE
```

This fine archetype covers:

```text
1. copper fabricator spread / inventory / export margin bridge → Stage2 possible after source repair
2. copper-brass price beta without margin refresh → false Stage2 / local 4B
3. aluminum/profile price beta without product-mix bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE", "symbol": "025820", "company_name": "이구산업", "round": "R4", "loop": "74", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_ALUMINUM_INDUSTRIAL_METAL_SPREAD_BRIDGE_VS_PRICE_ONLY_BETA_FADE", "case_type": "material_spread_supercycle", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-CopperFabricatorSpreadBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C15 should allow Stage2 when copper rally is tied to product-specific spread, inventory effect, export price and margin bridge. Igu Industry produced a strong copper-cycle MFE, but the late-2024 collapse requires local 4B-watch if spread/margin evidence stops refreshing.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy spread, inventory, product mix, customer/order, export price and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE", "symbol": "012800", "company_name": "대창", "round": "R4", "loop": "74", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_ALUMINUM_INDUSTRIAL_METAL_SPREAD_BRIDGE_VS_PRICE_ONLY_BETA_FADE", "case_type": "material_spread_supercycle", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / CopperBrassPriceBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C15 should not treat copper/brass price beta as durable Stage2 unless spread-to-margin and inventory/export bridge refreshes. Daechang produced a large MFE but quickly fell into high MAE and post-peak drawdown, so it is a false Stage2 / local 4B-watch row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy spread, inventory, product mix, customer/order, export price and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B", "symbol": "001780", "company_name": "알루코", "round": "R4", "loop": "74", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_ALUMINUM_INDUSTRIAL_METAL_SPREAD_BRIDGE_VS_PRICE_ONLY_BETA_FADE", "case_type": "material_spread_supercycle", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / AluminumPriceBetaLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C15 should not treat aluminum or battery-material profile beta as Green unless product mix, customer order, spread and margin bridge are explicit. Aluko produced only small MFE and then severe late-2024 MAE, making it local 4B-watch rather than durable Stage2.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy spread, inventory, product mix, customer/order, export price and margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE", "case_id": "R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE", "symbol": "025820", "company_name": "이구산업", "round": "R4", "loop": "74", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_ALUMINUM_INDUSTRIAL_METAL_SPREAD_BRIDGE_VS_PRICE_ONLY_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-CopperFabricatorSpreadBridge", "trigger_date": "2024-04-11", "entry_date": "2024-04-12", "entry_price": 5690.0, "evidence_available_at_that_date": "COPPER_PRICE_SPREAD_FABRICATOR_INVENTORY_EXPORT_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:IGU_INDUSTRY_2024_COPPER_SPREAD_FABRICATOR_INVENTORY_EXPORT_MARGIN_BRIDGE", "stage2_evidence_fields": ["industrial_metal_spread_candidate", "inventory_or_export_price_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "spread_to_margin_conversion_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv", "profile_path": "atlas/symbol_profiles/025/025820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 47.98, "MFE_90D_pct": 47.98, "MFE_180D_pct": 47.98, "MAE_30D_pct": -4.04, "MAE_90D_pct": -33.3, "MAE_180D_pct": -37.7, "peak_date": "2024-05-20", "peak_price": 8420.0, "drawdown_after_peak_pct": -57.9, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_industrial_metal_spread_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_customer_inventory_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C15 should allow Stage2 when copper rally is tied to product-specific spread, inventory effect, export price and margin bridge. Igu Industry produced a strong copper-cycle MFE, but the late-2024 collapse requires local 4B-watch if spread/margin evidence stops refreshing.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C15_METAL_SPREAD_025820_2024-04-12", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE", "case_id": "R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE", "symbol": "012800", "company_name": "대창", "round": "R4", "loop": "74", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_ALUMINUM_INDUSTRIAL_METAL_SPREAD_BRIDGE_VS_PRICE_ONLY_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / CopperBrassPriceBetaFade", "trigger_date": "2024-04-11", "entry_date": "2024-04-12", "entry_price": 1470.0, "evidence_available_at_that_date": "COPPER_BRASS_PRICE_BETA_WITH_WEAK_SPREAD_TO_MARGIN_REFRESH", "evidence_source": "source_proxy_manual_verification_required:DAECHANG_2024_COPPER_BRASS_PRICE_BETA_SPREAD_MARGIN_REFRESH", "stage2_evidence_fields": ["industrial_metal_spread_candidate", "inventory_or_export_price_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "spread_to_margin_conversion_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv", "profile_path": "atlas/symbol_profiles/012/012800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 57.82, "MFE_90D_pct": 57.82, "MFE_180D_pct": 57.82, "MAE_30D_pct": -4.49, "MAE_90D_pct": -25.17, "MAE_180D_pct": -25.85, "peak_date": "2024-05-21", "peak_price": 2320.0, "drawdown_after_peak_pct": -53.02, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_industrial_metal_spread_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_customer_inventory_or_margin_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C15 should not treat copper/brass price beta as durable Stage2 unless spread-to-margin and inventory/export bridge refreshes. Daechang produced a large MFE but quickly fell into high MAE and post-peak drawdown, so it is a false Stage2 / local 4B-watch row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C15_METAL_SPREAD_012800_2024-04-12", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B", "case_id": "R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B", "symbol": "001780", "company_name": "알루코", "round": "R4", "loop": "74", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_ALUMINUM_INDUSTRIAL_METAL_SPREAD_BRIDGE_VS_PRICE_ONLY_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / AluminumPriceBetaLocal4B", "trigger_date": "2024-04-11", "entry_date": "2024-04-12", "entry_price": 3215.0, "evidence_available_at_that_date": "ALUMINUM_PROFILE_BATTERY_MATERIAL_PRICE_BETA_WITH_WEAK_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ALUKO_2024_ALUMINUM_PROFILE_BATTERY_MATERIAL_SPREAD_MARGIN_BRIDGE", "stage2_evidence_fields": ["industrial_metal_spread_candidate", "inventory_or_export_price_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "spread_to_margin_conversion_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001780/2024.csv", "profile_path": "atlas/symbol_profiles/001/001780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.53, "MFE_90D_pct": 13.53, "MFE_180D_pct": 13.53, "MAE_30D_pct": -4.51, "MAE_90D_pct": -15.86, "MAE_180D_pct": -45.41, "peak_date": "2024-04-18", "peak_price": 3650.0, "drawdown_after_peak_pct": -51.92, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_industrial_metal_spread_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_customer_inventory_or_margin_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C15 should not treat aluminum or battery-material profile beta as Green unless product mix, customer order, spread and margin bridge are explicit. Aluko produced only small MFE and then severe late-2024 MAE, making it local 4B-watch rather than durable Stage2.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C15_METAL_SPREAD_001780_2024-04-12", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE", "trigger_id": "TRG_R4L74-C15-025820-IGU-COPPER-FABRICATOR-SPREAD-BRIDGE", "symbol": "025820", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"spread_score": 14, "inventory_or_export_bridge_score": 10, "margin_bridge_score": 12, "revision_score": 9, "relative_strength_score": 14, "customer_quality_score": 5, "valuation_repricing_score": 11, "execution_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"spread_score": 15, "inventory_or_export_bridge_score": 12, "margin_bridge_score": 14, "revision_score": 10, "relative_strength_score": 13, "customer_quality_score": 5, "valuation_repricing_score": 10, "execution_risk_score": 6, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow candidate after source repair + lifecycle 4B", "changed_components": ["spread_score", "margin_bridge_score", "execution_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "Reward only verified spread-to-margin conversion; cap copper/aluminum price beta when product mix, inventory/export or margin bridge fails to refresh.", "MFE_90D_pct": 47.98, "MAE_90D_pct": -33.3, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C15 should allow Stage2 when copper rally is tied to product-specific spread, inventory effect, export price and margin bridge. Igu Industry produced a strong copper-cycle MFE, but the late-2024 collapse requires local 4B-watch if spread/margin evidence stops refreshing."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE", "trigger_id": "TRG_R4L74-C15-012800-DAECHANG-COPPER-BRASS-PRICE-BETA-FADE", "symbol": "012800", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"spread_score": 7, "inventory_or_export_bridge_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 52, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"spread_score": 5, "inventory_or_export_bridge_score": 2, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 5, "customer_quality_score": 2, "valuation_repricing_score": 4, "execution_risk_score": 18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 43, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["spread_score", "margin_bridge_score", "execution_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "Reward only verified spread-to-margin conversion; cap copper/aluminum price beta when product mix, inventory/export or margin bridge fails to refresh.", "MFE_90D_pct": 57.82, "MAE_90D_pct": -25.17, "score_return_alignment_label": "false_positive_metal_price_beta_bridge_gap", "current_profile_verdict": "C15 should not treat copper/brass price beta as durable Stage2 unless spread-to-margin and inventory/export bridge refreshes. Daechang produced a large MFE but quickly fell into high MAE and post-peak drawdown, so it is a false Stage2 / local 4B-watch row."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B", "trigger_id": "TRG_R4L74-C15-001780-ALUKO-ALUMINUM-PRICE-BETA-LOCAL4B", "symbol": "001780", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"spread_score": 7, "inventory_or_export_bridge_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 15, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 0}, "weighted_score_before": 52, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"spread_score": 5, "inventory_or_export_bridge_score": 2, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 5, "customer_quality_score": 2, "valuation_repricing_score": 4, "execution_risk_score": 18, "dilution_cb_risk_score": 8, "accounting_trust_risk_score": 0}, "weighted_score_after": 43, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["spread_score", "margin_bridge_score", "execution_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "Reward only verified spread-to-margin conversion; cap copper/aluminum price beta when product mix, inventory/export or margin bridge fails to refresh.", "MFE_90D_pct": 13.53, "MAE_90D_pct": -15.86, "score_return_alignment_label": "false_positive_metal_price_beta_bridge_gap", "current_profile_verdict": "C15 should not treat aluminum or battery-material profile beta as Green unless product mix, customer order, spread and margin bridge are explicit. Aluko produced only small MFE and then severe late-2024 MAE, making it local 4B-watch rather than durable Stage2."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R4", "loop": 74, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "COPPER_ALUMINUM_INDUSTRIAL_METAL_SPREAD_BRIDGE_VS_PRICE_ONLY_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 2, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C15 industrial-metal symbols, +2 copper/aluminum spread families, +1 copper-fabricator positive, +2 copper/aluminum price-beta fade counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R4", "loop": 74, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "axis": "copper_aluminum_industrial_metal_spread_bridge_vs_price_only_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C15 should split verified industrial-metal spread-to-margin bridge from copper/aluminum price beta. Stage2 requires product-specific spread, inventory effect, export price, customer/order or margin conversion evidence. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["025820", "012800", "001780"], "share_count_validation_required": ["001780"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": 74, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C15 needs spread-to-margin proof. Igu Industry shows a copper fabricator positive with later local 4B lifecycle; Daechang and Aluko show copper/aluminum price beta fading into local 4B when margin bridge fails to refresh."}
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

001780:
  corporate_action_candidate_dates = 1996-01-16, 1997-01-10, 1999-10-15, 2002-04-08, 2007-06-07, 2008-05-08
  selected window = 2024-04-12~D+180
  contamination = false
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C15 rows are source_proxy_only / evidence_url_pending.
001780 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C15 rule-shape discovery,
but coding-agent promotion requires non-proxy spread, inventory, product-mix, export/customer and margin evidence.
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
copper_aluminum_industrial_metal_spread_bridge_vs_price_only_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 025820, 012800 and 001780.
4. Validate 001780 share-count changes inside the selected window.
5. Keep generic C15 metal-price weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - product-specific spread evidence is explicit,
   - inventory/export/customer bridge is visible,
   - margin/revision conversion exists,
   - MAE remains controlled.
7. Consider local 4B-watch when:
   - the trigger is copper/aluminum price beta only,
   - spread or margin bridge is weak/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price contract/customer/inventory/margin deterioration evidence.
9. Emit before/after diagnostics and reject if verified spread-to-margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R4
completed_loop = 74
next_round = R5
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```


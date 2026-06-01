# E2R Stock-Web v12 Residual Research — R9 Loop 74 / L3 / C29

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 74,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 74,
  "computed_next_round": "R10",
  "computed_next_loop": 74,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "AUTO_PARTS_MODULE_LIGHTING_ELECTRIFICATION_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
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

Previous completed state in this interactive run: R8 / loop 74.

Therefore:

```text
scheduled_round = R9
scheduled_loop = 74
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 74
```

R9 was routed to C29 because R10 remains the construction/PF round.  
This file avoids the heavily covered OEM rows and loop-73 tire/logistics/thermal set. It tests module, lighting and auto-parts supplier paths.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C29 coverage is concentrated in:

```text
000270, 204320, 011210, 005380, 003490
```

This run uses three different symbols:

```text
012330 / 현대모비스 / module-electrification value-up margin bridge
005850 / 에스엘 / lighting/ADAS OEM mix margin bridge
033530 / SJG세종 / hydrogen/exhaust parts beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
012330 shows share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
```

## Research thesis

C29 is not “auto stock went up.”

The correct mechanism is:

```text
vehicle volume / module or parts program / OEM mix
→ pricing or customer-program bridge
→ margin conversion
→ durable rerating
```

A car has many gears.  
OEM volume is the engine.  
Module mix, lighting spec, A/S parts and pricing are the gearbox that turns motion into torque.

---

## Case 1 — Positive slow bridge: 012330 / 현대모비스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is A/S parts, electrification module mix, capital-return/value-up and margin bridge evidence.

```text
evidence_family = AUTO_MODULE_AS_PARTS_ELECTRIFICATION_VALUEUP_MARGIN_BRIDGE
case_role = positive_slow_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 208,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv`:

```text
2024-02-01,208000,222500,208000,219500
2024-03-15,265000,269000,263500,269000
2024-08-05,215000,215500,200500,204000
2024-10-18,244000,246000,241500,244500
```

### Backtest

```text
MFE_30D  = +29.33%
MAE_30D  = +0.00%
MFE_90D  = +29.33%
MAE_90D  = +0.00%
MFE_180D = +29.33%
MAE_180D = -3.61%
peak_180 = 269,000 on 2024-03-15
trough_180 = 200,500 on 2024-08-05
peak_to_later_drawdown = -25.47%
```

### Interpretation

This is a controlled-MAE C29 positive.  
It is not a high-beta OEM spike. The useful bridge is module/electrification/A/S parts margin plus capital-return/value-up discipline.

The share-count change means runtime promotion needs validation.

---

## Case 2 — Positive with later 4B-watch: 005850 / 에스엘

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is automotive lighting, ADAS mix, OEM order cadence, pricing and margin bridge evidence.

```text
evidence_family = AUTO_LIGHTING_ADAS_OEM_MIX_ORDER_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 32,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv`:

```text
2024-02-01,32200,34550,31900,33750
2024-06-17,43350,47650,42800,44200
2024-08-05,35600,35600,30950,32750
2024-09-04,31100,31300,30800,30850
```

### Backtest

```text
MFE_30D  = +13.20%
MAE_30D  = -0.93%
MFE_90D  = +47.98%
MAE_90D  = -8.54%
MFE_180D = +47.98%
MAE_180D = -8.54%
peak_180 = 47,650 on 2024-06-17
trough_180 = 30,800 on 2024-09-04
peak_to_later_drawdown = -35.36%
```

### Interpretation

This is the supplier-positive path.  
The price path says lighting/ADAS mix and margin bridge could matter. But after the June peak, the drawdown is large enough that local 4B-watch should activate if OEM mix or margin evidence fades.

---

## Case 3 — Counterexample / local 4B: 033530 / SJG세종

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests hydrogen/exhaust/auto-parts theme beta without enough customer-volume, OEM program or margin bridge.

```text
evidence_family = HYDROGEN_EXHAUST_AUTO_PARTS_THEME_BETA_WITH_WEAK_CUSTOMER_VOLUME_MARGIN_BRIDGE
case_role = counterexample
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,530
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/033/033530/2024.csv`:

```text
2024-02-01,5530,5880,5530,5860
2024-03-06,6240,6840,5970,5970
2024-07-03,5410,5440,5240,5260
2024-08-05,4995,4995,4085,4345
```

### Backtest

```text
MFE_30D  = +23.69%
MAE_30D  = +0.00%
MFE_90D  = +23.69%
MAE_90D  = +0.00%
MFE_180D = +23.69%
MAE_180D = -26.13%
peak_180 = 6,840 on 2024-03-06
trough_180 = 4,085 on 2024-08-05
peak_to_later_drawdown = -40.28%
```

### Interpretation

This is the C29 auto-parts beta failure.  
The early squeeze was real, but the customer-volume and margin bridge did not hold.

Correct treatment:

```text
false Stage2 / local 4B-watch
```

not durable Green.

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
do_not_raise_generic_C29_mobility_weight = true
do_not_treat_all_auto_parts_or_valueup_beta_as_Green = true
do_not_convert_auto-parts_drawdown_to_hard_4C_without_non-price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
AUTO_PARTS_MODULE_LIGHTING_ELECTRIFICATION_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE
```

This fine archetype covers:

```text
1. module/electrification/A/S parts margin bridge → Stage2 possible after source repair
2. lighting/ADAS OEM-mix margin bridge → Stage2 possible, later local 4B if bridge fades
3. hydrogen/exhaust parts theme beta without customer-volume bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN", "symbol": "012330", "company_name": "현대모비스", "round": "R9", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MODULE_LIGHTING_ELECTRIFICATION_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-AutoModuleElectrificationMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should allow Stage2 for non-OEM auto modules when value-up attention connects to A/S parts, electrification module mix, capital return and margin bridge. Hyundai Mobis produced controlled MAE and a clean MFE path, but shard share-count changes need validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy OEM/customer-volume, mix, electrification, A/S, order and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN", "symbol": "005850", "company_name": "에스엘", "round": "R9", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MODULE_LIGHTING_ELECTRIFICATION_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-AutoLightingADASMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should include lighting/ADAS suppliers when OEM mix, order cadence and margin conversion drive rerating. SL had strong MFE, but post-peak drawdown says lifecycle local 4B should fire if OEM mix or margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy OEM/customer-volume, mix, electrification, A/S, order and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE", "symbol": "033530", "company_name": "SJG세종", "round": "R9", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MODULE_LIGHTING_ELECTRIFICATION_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / HydrogenExhaustPartsBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not treat hydrogen/exhaust/auto-parts theme beta as durable Stage2 unless customer volume, OEM program, pricing or margin bridge is visible. SJG Sejong had a tradable spike but later MAE and post-peak drawdown opened.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy OEM/customer-volume, mix, electrification, A/S, order and margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN", "case_id": "R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN", "symbol": "012330", "company_name": "현대모비스", "round": "R9", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MODULE_LIGHTING_ELECTRIFICATION_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-AutoModuleElectrificationMarginBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 208000.0, "evidence_available_at_that_date": "AUTO_MODULE_AS_PARTS_ELECTRIFICATION_VALUEUP_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HYUNDAI_MOBIS_2024_AS_PARTS_ELECTRIFICATION_MODULE_CAPITAL_RETURN_MARGIN_BRIDGE", "stage2_evidence_fields": ["mobility_volume_or_customer_bridge", "mix_or_margin_candidate", "operating_leverage_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_mix_or_order_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv", "profile_path": "atlas/symbol_profiles/012/012330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 29.33, "MFE_90D_pct": 29.33, "MFE_180D_pct": 29.33, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": -3.61, "peak_date": "2024-03-15", "peak_price": 269000.0, "drawdown_after_peak_pct": -25.47, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_parts_or_margin_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_volume_program_or_margin_break", "trigger_outcome_label": "positive_slow_with_sharecount_validation", "current_profile_verdict": "C29 should allow Stage2 for non-OEM auto modules when value-up attention connects to A/S parts, electrification module mix, capital return and margin bridge. Hyundai Mobis produced controlled MAE and a clean MFE path, but shard share-count changes need validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C29_MOBILITY_PARTS_012330_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN", "case_id": "R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN", "symbol": "005850", "company_name": "에스엘", "round": "R9", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MODULE_LIGHTING_ELECTRIFICATION_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-AutoLightingADASMarginBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 32200.0, "evidence_available_at_that_date": "AUTO_LIGHTING_ADAS_OEM_MIX_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SL_CORP_2024_AUTO_LIGHTING_ADAS_OEM_MIX_ORDER_MARGIN_BRIDGE", "stage2_evidence_fields": ["mobility_volume_or_customer_bridge", "mix_or_margin_candidate", "operating_leverage_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_mix_or_order_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv", "profile_path": "atlas/symbol_profiles/005/005850.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.2, "MFE_90D_pct": 47.98, "MFE_180D_pct": 47.98, "MAE_30D_pct": -0.93, "MAE_90D_pct": -8.54, "MAE_180D_pct": -8.54, "peak_date": "2024-06-17", "peak_price": 47650.0, "drawdown_after_peak_pct": -35.36, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_parts_or_margin_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_volume_program_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C29 should include lighting/ADAS suppliers when OEM mix, order cadence and margin conversion drive rerating. SL had strong MFE, but post-peak drawdown says lifecycle local 4B should fire if OEM mix or margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_PARTS_005850_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE", "case_id": "R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE", "symbol": "033530", "company_name": "SJG세종", "round": "R9", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MODULE_LIGHTING_ELECTRIFICATION_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / HydrogenExhaustPartsBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5530.0, "evidence_available_at_that_date": "HYDROGEN_EXHAUST_AUTO_PARTS_THEME_BETA_WITH_WEAK_CUSTOMER_VOLUME_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SJG_SEJONG_2024_HYDROGEN_EXHAUST_AUTO_PARTS_CUSTOMER_VOLUME_MARGIN_BRIDGE", "stage2_evidence_fields": ["mobility_volume_or_customer_bridge", "mix_or_margin_candidate", "operating_leverage_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_mix_or_order_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/033/033530/2024.csv", "profile_path": "atlas/symbol_profiles/033/033530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 23.69, "MFE_90D_pct": 23.69, "MFE_180D_pct": 23.69, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": -26.13, "peak_date": "2024-03-06", "peak_price": 6840.0, "drawdown_after_peak_pct": -40.28, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_parts_or_margin_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_volume_program_or_margin_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C29 should not treat hydrogen/exhaust/auto-parts theme beta as durable Stage2 unless customer volume, OEM program, pricing or margin bridge is visible. SJG Sejong had a tradable spike but later MAE and post-peak drawdown opened.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_PARTS_033530_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN", "trigger_id": "TRG_R9L74-C29-012330-HYUNDAI-MOBIS-MODULE-ELECTRIFICATION-MARGIN", "symbol": "012330", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_utilization_score": 12, "pricing_mix_score": 12, "margin_bridge_score": 13, "capital_return_or_capacity_score": 10, "relative_strength_score": 12, "customer_quality_score": 11, "valuation_repricing_score": 11, "execution_risk_score": 5, "dilution_or_sharecount_risk_score": 7, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"volume_or_utilization_score": 13, "pricing_mix_score": 14, "margin_bridge_score": 15, "capital_return_or_capacity_score": 11, "relative_strength_score": 12, "customer_quality_score": 12, "valuation_repricing_score": 10, "execution_risk_score": 5, "dilution_or_sharecount_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 87, "stage_label_after": "Stage2/Yellow candidate after source repair + lifecycle 4B", "changed_components": ["pricing_mix_score", "margin_bridge_score", "execution_risk_score", "dilution_or_sharecount_risk_score"], "component_delta_explanation": "Reward only verified customer-volume/mix-to-margin bridge; cap auto-parts or hydrogen/exhaust theme beta when program, pricing or margin evidence fails to refresh.", "MFE_90D_pct": 29.33, "MAE_90D_pct": 0.0, "score_return_alignment_label": "aligned_positive_with_source_repair", "current_profile_verdict": "C29 should allow Stage2 for non-OEM auto modules when value-up attention connects to A/S parts, electrification module mix, capital return and margin bridge. Hyundai Mobis produced controlled MAE and a clean MFE path, but shard share-count changes need validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN", "trigger_id": "TRG_R9L74-C29-005850-SL-AUTO-LIGHTING-ADAS-MARGIN", "symbol": "005850", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_utilization_score": 12, "pricing_mix_score": 12, "margin_bridge_score": 13, "capital_return_or_capacity_score": 4, "relative_strength_score": 12, "customer_quality_score": 11, "valuation_repricing_score": 11, "execution_risk_score": 5, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"volume_or_utilization_score": 13, "pricing_mix_score": 14, "margin_bridge_score": 15, "capital_return_or_capacity_score": 3, "relative_strength_score": 12, "customer_quality_score": 12, "valuation_repricing_score": 10, "execution_risk_score": 5, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_after": 87, "stage_label_after": "Stage2/Yellow candidate after source repair + lifecycle 4B", "changed_components": ["pricing_mix_score", "margin_bridge_score", "execution_risk_score", "dilution_or_sharecount_risk_score"], "component_delta_explanation": "Reward only verified customer-volume/mix-to-margin bridge; cap auto-parts or hydrogen/exhaust theme beta when program, pricing or margin evidence fails to refresh.", "MFE_90D_pct": 47.98, "MAE_90D_pct": -8.54, "score_return_alignment_label": "aligned_positive_with_source_repair", "current_profile_verdict": "C29 should include lighting/ADAS suppliers when OEM mix, order cadence and margin conversion drive rerating. SL had strong MFE, but post-peak drawdown says lifecycle local 4B should fire if OEM mix or margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE", "trigger_id": "TRG_R9L74-C29-033530-SJG-SEJONG-HYDROGEN-EXHAUST-PARTS-BETA-FADE", "symbol": "033530", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_utilization_score": 5, "pricing_mix_score": 3, "margin_bridge_score": 3, "capital_return_or_capacity_score": 4, "relative_strength_score": 7, "customer_quality_score": 4, "valuation_repricing_score": 5, "execution_risk_score": 15, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_before": 52, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"volume_or_utilization_score": 3, "pricing_mix_score": 2, "margin_bridge_score": 2, "capital_return_or_capacity_score": 3, "relative_strength_score": 4, "customer_quality_score": 3, "valuation_repricing_score": 4, "execution_risk_score": 18, "dilution_or_sharecount_risk_score": 0, "source_confidence_score": 2}, "weighted_score_after": 42, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["pricing_mix_score", "margin_bridge_score", "execution_risk_score", "dilution_or_sharecount_risk_score"], "component_delta_explanation": "Reward only verified customer-volume/mix-to-margin bridge; cap auto-parts or hydrogen/exhaust theme beta when program, pricing or margin evidence fails to refresh.", "MFE_90D_pct": 23.69, "MAE_90D_pct": 0.0, "score_return_alignment_label": "false_positive_mobility_parts_beta_bridge_gap", "current_profile_verdict": "C29 should not treat hydrogen/exhaust/auto-parts theme beta as durable Stage2 unless customer volume, OEM program, pricing or margin bridge is visible. SJG Sejong had a tradable spike but later MAE and post-peak drawdown opened."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R9", "loop": 74, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_MODULE_LIGHTING_ELECTRIFICATION_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C29 mobility-parts symbols, +3 module/lighting/hydrogen-exhaust trigger families, +2 auto-parts margin positives, +1 auto-parts theme-beta local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R9", "loop": 74, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "axis": "auto_parts_module_lighting_electrification_margin_bridge_vs_parts_theme_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C29 should split verified auto-parts/module/lighting/electrification margin bridge from price-only mobility or hydrogen/exhaust parts beta. Stage2 requires customer volume, program mix, order cadence, pricing or margin conversion evidence. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["012330", "005850", "033530"], "share_count_validation_required": ["012330"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": 74, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C29 should not be limited to OEMs. Hyundai Mobis and SL show module/lighting margin positives after source repair; SJG Sejong shows hydrogen/exhaust parts beta fading into local 4B when customer-volume/margin bridge is absent."}
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
012330:
  corporate_action_candidate_dates = 1997-05-27, 1999-01-08, 1999-04-15, 1999-08-16, 1999-12-21
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

005850:
  corporate_action_candidate_dates = 2002-07-30, 2003-12-16, 2007-10-22, 2019-04-16
  selected window = 2024-02-01~D+180
  contamination = false

033530:
  corporate_action_candidate_dates = 1999-11-29
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C29 rows are source_proxy_only / evidence_url_pending.
012330 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C29 rule-shape discovery,
but coding-agent promotion requires non-proxy customer-volume, program mix, pricing, order cadence and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R9/C29 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
auto_parts_module_lighting_electrification_margin_bridge_vs_parts_theme_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 012330, 005850 and 033530.
4. Validate 012330 share-count changes inside the selected window.
5. Keep generic C29 mobility weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - customer volume or OEM program visibility is explicit,
   - mix, pricing, A/S parts, electrification or lighting/ADAS bridge exists,
   - margin conversion is visible,
   - MAE remains controlled.
7. Consider local 4B-watch when:
   - the trigger is auto-parts, hydrogen/exhaust or mobility theme beta only,
   - customer-volume or margin bridge is weak/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, order cut, program delay, pricing or margin break.
9. Emit before/after diagnostics and reject if verified module/lighting margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R9
completed_loop = 74
next_round = R10
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```


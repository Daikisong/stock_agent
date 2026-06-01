# E2R Stock-Web v12 Residual Research — R9 Loop 76 / L3 / C29

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 76,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 76,
  "computed_next_round": "R10",
  "computed_next_loop": 76,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "MODULE_LAMP_THERMAL_SYSTEM_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_THERMAL_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "mobility_supplier_volume_margin_guardrail",
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

Previous completed state in this interactive run: R8 / loop 76.

Therefore:

```text
scheduled_round = R9
scheduled_loop = 76
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 76
```

R9 was routed to mobility/transport rather than construction because R10 is the dedicated construction/PF round.  
This file tests mobility supplier volume/mix/margin bridges rather than construction balance-sheet breaks.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C29 concentration in:

```text
000270, 204320, 011210, 005380, 003490
```

This run uses three different symbols and avoids loop-75 R9 names:

```text
005850 / 에스엘 / lamp-module OEM mix margin bridge
012330 / 현대모비스 / module/A-S/electrification mix capital-return bridge
018880 / 한온시스템 / EV thermal utilization fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
018880 has a future 2025-01-09 corporate-action candidate; the selected 2024 measurement window must not cross it without adjustment.
```

## Research thesis

C29 is not “auto part stock went up.”

The mechanism must pass through:

```text
vehicle / OEM program volume
→ module, lamp, thermal or A/S product mix
→ utilization, pricing and customer cadence
→ margin conversion
→ durable operating leverage
```

A car-parts headline is a showroom light.  
The real C29 bridge is the purchase order, production slot and margin walking through the factory door.

---

## Case 1 — Positive with lifecycle 4B: 005850 / 에스엘

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is lamp/module OEM program volume, product mix, pricing and margin bridge evidence.

```text
evidence_family = AUTO_LAMP_MODULE_OEM_VOLUME_PRODUCT_MIX_PRICING_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 32,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv`:

```text
2024-02-01,32200,34550,31900,33750
2024-02-05,37400,37450,34450,36000
2024-04-17,30450,30600,30000,30000
2024-06-17,43350,47650,42800,44200
2024-08-05,35600,35600,30950,32750
```

### Backtest

```text
MFE_30D  = +16.30%
MAE_30D  = -3.11%
MFE_90D  = +47.98%
MAE_90D  = -6.83%
MFE_180D = +47.98%
MAE_180D = -6.83%
peak_180 = 47,650 on 2024-06-17
trough_180 = 30,000 on 2024-04-17
peak_to_later_drawdown = -35.05%
```

### Interpretation

This is a valid C29 supplier positive after source repair.  
The price path had a large MFE and bounded entry-basis MAE, but the post-peak drawdown means lifecycle local 4B is needed if volume/mix/margin evidence fades.

---

## Case 2 — Slow positive: 012330 / 현대모비스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is module/A-S mix, electrification exposure, customer program stability, capital-return and margin evidence.

```text
evidence_family = MOBILITY_MODULE_AS_ELECTRIFICATION_MIX_CAPITAL_RETURN_MARGIN_BRIDGE
case_role = positive_slow_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 208,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv`:

```text
2024-02-01,208000,222500,208000,219500
2024-03-14,252000,268000,251500,265000
2024-03-18,269500,270000,265500,268000
2024-08-05,215000,215500,200500,204000
2024-10-25,249500,267000,248000,256500
```

### Backtest

```text
MFE_30D  = +29.81%
MAE_30D  = +0.00%
MFE_90D  = +29.81%
MAE_90D  = +0.00%
MFE_180D = +29.81%
MAE_180D = -3.61%
peak_180 = 270,000 on 2024-03-18
trough_180 = 200,500 on 2024-08-05
peak_to_later_drawdown = -25.74%
```

### Interpretation

This is a large-cap slow C29 positive.  
It should not be overblocked just because it is less explosive than small-cap parts names.

Correct treatment:

```text
Stage2-Yellow possible after source repair
lifecycle local 4B if module/A-S/margin/capital-return bridge fades
```

---

## Case 3 — Counterexample / local 4B: 018880 / 한온시스템

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests EV thermal-management beta without customer-volume, utilization and margin bridge.

```text
evidence_family = EV_THERMAL_MANAGEMENT_THEME_WITH_WEAK_CUSTOMER_VOLUME_UTILIZATION_MARGIN_BRIDGE
case_role = counterexample_EV_thermal_beta_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 6,160
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv`:

```text
2024-02-01,6160,6420,6120,6360
2024-02-13,6470,6590,6400,6520
2024-05-07,6580,6800,5610,5620
2024-06-14,4735,4750,4655,4670
2024-08-05,4290,4300,3800,3870
2024-10-10,3840,3855,3730,3805
```

### Backtest

```text
MFE_30D  = +6.98%
MAE_30D  = -9.25%
MFE_90D  = +10.39%
MAE_90D  = -24.43%
MFE_180D = +10.39%
MAE_180D = -39.45%
peak_180 = 6,800 on 2024-05-07
trough_180 = 3,730 on 2024-10-10
peak_to_later_drawdown = -45.15%
```

### Interpretation

This is the EV thermal beta fade.  
The price path did not become durable operating leverage.

Correct treatment:

```text
false Stage2
local 4B-watch
no hard 4C without non-price customer/program/margin break
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
do_not_raise_generic_C29_auto_supplier_weight = true
do_not_treat_all_mobility_supplier_MFE_as_Green = true
do_not_convert_EV_thermal_or_supplier_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
MODULE_LAMP_THERMAL_SYSTEM_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_THERMAL_BETA_FADE
```

This fine archetype covers:

```text
1. lamp/module OEM program mix-margin bridge → Stage2 possible after source repair
2. module/A-S/electrification mix and capital-return bridge → slow Stage2 possible
3. EV thermal-management beta without customer-volume/utilization bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R9L76-C29-005850-SL-LAMP-MODULE-OEM-MIX-MARGIN-BRIDGE", "symbol": "005850", "company_name": "에스엘", "round": "R9", "loop": "76", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MODULE_LAMP_THERMAL_SYSTEM_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_THERMAL_BETA_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-LampModuleOEMMixMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should allow mobility supplier Stage2 when OEM program volume, lamp/module mix, pricing and margin bridge are visible. SL produced a large mid-year MFE with bounded entry-basis MAE, but the later drawdown requires lifecycle local 4B if volume/mix/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy OEM/customer volume, platform program, module/lamp/thermal mix, utilization, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L76-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MIX-CAPITAL-RETURN", "symbol": "012330", "company_name": "현대모비스", "round": "R9", "loop": "76", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MODULE_LAMP_THERMAL_SYSTEM_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_THERMAL_BETA_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-SlowPositive-ModuleASMixMarginCapitalReturnBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should preserve large-cap mobility supplier positives when module/A/S mix, electrification exposure, customer program stability, capital return and margin bridge are visible. Hyundai Mobis had a slow low-MAE rerating path rather than a theme spike.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy OEM/customer volume, platform program, module/lamp/thermal mix, utilization, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L76-C29-018880-HANON-SYSTEMS-EV-THERMAL-UTILIZATION-FADE", "symbol": "018880", "company_name": "한온시스템", "round": "R9", "loop": "76", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MODULE_LAMP_THERMAL_SYSTEM_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_THERMAL_BETA_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / EVThermalUtilizationMarginFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not treat EV thermal-management beta as durable Stage2 unless customer volume, platform program, utilization, pricing/mix and margin bridge are visible. Hanon Systems had limited MFE and then opened a high-MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy OEM/customer volume, platform program, module/lamp/thermal mix, utilization, pricing and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R9L76-C29-005850-SL-LAMP-MODULE-OEM-MIX-MARGIN-BRIDGE", "case_id": "R9L76-C29-005850-SL-LAMP-MODULE-OEM-MIX-MARGIN-BRIDGE", "symbol": "005850", "company_name": "에스엘", "round": "R9", "loop": "76", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MODULE_LAMP_THERMAL_SYSTEM_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_THERMAL_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-Actionable-LampModuleOEMMixMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 32200.0, "evidence_available_at_that_date": "AUTO_LAMP_MODULE_OEM_VOLUME_PRODUCT_MIX_PRICING_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SL_2024_AUTO_LAMP_MODULE_OEM_VOLUME_PROGRAM_MIX_PRICING_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_volume_or_OEM_program_candidate", "module_lamp_thermal_mix_or_pricing_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "program_award_utilization_or_capital_return_bridge_candidate"], "stage4b_evidence_fields": ["theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv", "profile_path": "atlas/symbol_profiles/005/005850.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.3, "MFE_90D_pct": 47.98, "MFE_180D_pct": 47.98, "MAE_30D_pct": -3.11, "MAE_90D_pct": -6.83, "MAE_180D_pct": -6.83, "peak_date": "2024-06-17", "peak_price": 47650.0, "drawdown_after_peak_pct": -35.05, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_supplier_peak_if_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_pricing_mix_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C29 should allow mobility supplier Stage2 when OEM program volume, lamp/module mix, pricing and margin bridge are visible. SL produced a large mid-year MFE with bounded entry-basis MAE, but the later drawdown requires lifecycle local 4B if volume/mix/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_before_future_CA", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_SUPPLIER_005850_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L76-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MIX-CAPITAL-RETURN", "case_id": "R9L76-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MIX-CAPITAL-RETURN", "symbol": "012330", "company_name": "현대모비스", "round": "R9", "loop": "76", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MODULE_LAMP_THERMAL_SYSTEM_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_THERMAL_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-SlowPositive-ModuleASMixMarginCapitalReturnBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 208000.0, "evidence_available_at_that_date": "MOBILITY_MODULE_AS_ELECTRIFICATION_MIX_CAPITAL_RETURN_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HYUNDAI_MOBIS_2024_MODULE_AS_ELECTRIFICATION_PROGRAM_MIX_CAPITAL_RETURN_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_volume_or_OEM_program_candidate", "module_lamp_thermal_mix_or_pricing_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "program_award_utilization_or_capital_return_bridge_candidate"], "stage4b_evidence_fields": ["theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv", "profile_path": "atlas/symbol_profiles/012/012330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 29.81, "MFE_90D_pct": 29.81, "MFE_180D_pct": 29.81, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": -3.61, "peak_date": "2024-03-18", "peak_price": 270000.0, "drawdown_after_peak_pct": -25.74, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_supplier_peak_if_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_pricing_mix_or_margin_break", "trigger_outcome_label": "positive_slow_with_later_4b_watch", "current_profile_verdict": "C29 should preserve large-cap mobility supplier positives when module/A/S mix, electrification exposure, customer program stability, capital return and margin bridge are visible. Hyundai Mobis had a slow low-MAE rerating path rather than a theme spike.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_before_future_CA", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_SUPPLIER_012330_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L76-C29-018880-HANON-SYSTEMS-EV-THERMAL-UTILIZATION-FADE", "case_id": "R9L76-C29-018880-HANON-SYSTEMS-EV-THERMAL-UTILIZATION-FADE", "symbol": "018880", "company_name": "한온시스템", "round": "R9", "loop": "76", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MODULE_LAMP_THERMAL_SYSTEM_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_THERMAL_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-FalsePositive / EVThermalUtilizationMarginFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 6160.0, "evidence_available_at_that_date": "EV_THERMAL_MANAGEMENT_THEME_WITH_WEAK_CUSTOMER_VOLUME_UTILIZATION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANON_SYSTEMS_2024_EV_THERMAL_MANAGEMENT_CUSTOMER_VOLUME_UTILIZATION_PRICING_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_volume_or_OEM_program_candidate", "module_lamp_thermal_mix_or_pricing_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "program_award_utilization_or_capital_return_bridge_candidate"], "stage4b_evidence_fields": ["theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv", "profile_path": "atlas/symbol_profiles/018/018880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.98, "MFE_90D_pct": 10.39, "MFE_180D_pct": 10.39, "MAE_30D_pct": -9.25, "MAE_90D_pct": -24.43, "MAE_180D_pct": -39.45, "peak_date": "2024-05-07", "peak_price": 6800.0, "drawdown_after_peak_pct": -45.15, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_supplier_peak_if_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_pricing_mix_or_margin_break", "trigger_outcome_label": "counterexample_EV_thermal_beta_local4b", "current_profile_verdict": "C29 should not treat EV thermal-management beta as durable Stage2 unless customer volume, platform program, utilization, pricing/mix and margin bridge are visible. Hanon Systems had limited MFE and then opened a high-MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_before_future_CA", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_SUPPLIER_018880_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L76-C29-005850-SL-LAMP-MODULE-OEM-MIX-MARGIN-BRIDGE", "trigger_id": "TRG_R9L76-C29-005850-SL-LAMP-MODULE-OEM-MIX-MARGIN-BRIDGE", "symbol": "005850", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 13, "OEM_program_visibility_score": 13, "mix_pricing_score": 13, "utilization_score": 12, "margin_bridge_score": 13, "relative_strength_score": 12, "execution_risk_score": 7, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2-Yellow candidate after source repair", "raw_component_scores_after": {"customer_volume_score": 15, "OEM_program_visibility_score": 15, "mix_pricing_score": 15, "utilization_score": 13, "margin_bridge_score": 15, "relative_strength_score": 11, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow-Green candidate after source repair + lifecycle 4B", "changed_components": ["customer_volume_score", "OEM_program_visibility_score", "mix_pricing_score", "utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified mobility customer-volume/program mix, utilization, pricing and margin bridge; cap EV thermal/module theme beta when OEM program or margin evidence fails to refresh.", "MFE_90D_pct": 47.98, "MAE_90D_pct": -6.83, "score_return_alignment_label": "positive_with_source_repair_and_lifecycle_4b", "current_profile_verdict": "C29 should allow mobility supplier Stage2 when OEM program volume, lamp/module mix, pricing and margin bridge are visible. SL produced a large mid-year MFE with bounded entry-basis MAE, but the later drawdown requires lifecycle local 4B if volume/mix/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L76-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MIX-CAPITAL-RETURN", "trigger_id": "TRG_R9L76-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MIX-CAPITAL-RETURN", "symbol": "012330", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 13, "OEM_program_visibility_score": 13, "mix_pricing_score": 13, "utilization_score": 12, "margin_bridge_score": 13, "relative_strength_score": 12, "execution_risk_score": 7, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2-Yellow candidate after source repair", "raw_component_scores_after": {"customer_volume_score": 15, "OEM_program_visibility_score": 15, "mix_pricing_score": 15, "utilization_score": 13, "margin_bridge_score": 15, "relative_strength_score": 11, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow-Green candidate after source repair + lifecycle 4B", "changed_components": ["customer_volume_score", "OEM_program_visibility_score", "mix_pricing_score", "utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified mobility customer-volume/program mix, utilization, pricing and margin bridge; cap EV thermal/module theme beta when OEM program or margin evidence fails to refresh.", "MFE_90D_pct": 29.81, "MAE_90D_pct": 0.0, "score_return_alignment_label": "positive_with_source_repair_and_lifecycle_4b", "current_profile_verdict": "C29 should preserve large-cap mobility supplier positives when module/A/S mix, electrification exposure, customer program stability, capital return and margin bridge are visible. Hyundai Mobis had a slow low-MAE rerating path rather than a theme spike."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L76-C29-018880-HANON-SYSTEMS-EV-THERMAL-UTILIZATION-FADE", "trigger_id": "TRG_R9L76-C29-018880-HANON-SYSTEMS-EV-THERMAL-UTILIZATION-FADE", "symbol": "018880", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 4, "OEM_program_visibility_score": 3, "mix_pricing_score": 3, "utilization_score": 2, "margin_bridge_score": 2, "relative_strength_score": 4, "execution_risk_score": 19, "source_confidence_score": 2}, "weighted_score_before": 49, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_volume_score": 2, "OEM_program_visibility_score": 2, "mix_pricing_score": 1, "utilization_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_after": 36, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_volume_score", "OEM_program_visibility_score", "mix_pricing_score", "utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified mobility customer-volume/program mix, utilization, pricing and margin bridge; cap EV thermal/module theme beta when OEM program or margin evidence fails to refresh.", "MFE_90D_pct": 10.39, "MAE_90D_pct": -24.43, "score_return_alignment_label": "false_positive_EV_thermal_bridge_gap", "current_profile_verdict": "C29 should not treat EV thermal-management beta as durable Stage2 unless customer volume, platform program, utilization, pricing/mix and margin bridge are visible. Hanon Systems had limited MFE and then opened a high-MAE drawdown path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R9", "loop": 76, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "MODULE_LAMP_THERMAL_SYSTEM_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_THERMAL_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C29 mobility supplier symbols outside loop-75 names and top-covered OEM set, +3 lamp/module/thermal trigger families, +2 supplier mix-margin positives, +1 EV thermal utilization-fade local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R9", "loop": 76, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "axis": "module_lamp_thermal_system_volume_mix_margin_bridge_vs_EV_thermal_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C29 should split verified mobility supplier volume/mix/margin bridges from EV thermal or auto-parts beta. Stage2 requires OEM program visibility, customer volume, module/lamp/thermal product mix, utilization, pricing or margin conversion. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["005850", "012330", "018880"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": 76, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C29 needs mobility volume/mix/margin proof. SL and Hyundai Mobis show lamp/module/mix-margin positives after source repair; Hanon Systems shows EV thermal beta fading into local 4B when customer utilization and margin bridge are absent."}
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
005850:
  corporate_action_candidate_dates = 2002-07-30, 2003-12-16, 2007-10-22, 2019-04-16
  selected window = 2024-02-01~D+180
  contamination = false

012330:
  corporate_action_candidate_dates = 1997-05-27, 1999-01-08, 1999-04-15, 1999-08-16, 1999-12-21
  selected window = 2024-02-01~D+180
  contamination = false

018880:
  corporate_action_candidate_dates = 2004-05-12, 2016-02-16, 2025-01-09, 2026-01-12
  selected window = 2024-02-01~D+180
  contamination = false for selected 2024 window
  caveat = extended validation must not cross 2025-01-09 without adjustment
```

Data-quality caveat:

```text
All selected C29 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C29 rule-shape discovery,
but coding-agent promotion requires non-proxy OEM/customer volume, platform program, module/lamp/thermal mix, utilization, pricing and margin evidence.
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
module_lamp_thermal_system_volume_mix_margin_bridge_vs_EV_thermal_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 005850, 012330 and 018880.
4. Keep generic C29 mobility/auto-parts weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - OEM customer volume or named program visibility is explicit,
   - module/lamp/thermal product mix or pricing bridge exists,
   - utilization and margin conversion is visible,
   - MAE remains controlled or the signal is explicitly slow/lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is auto-parts, EV thermal or mobility theme beta only,
   - OEM-volume/utilization/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, order cut, program delay, pricing/mix collapse, financing or margin break.
8. Emit before/after diagnostics and reject if verified mobility supplier mix-margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R9
completed_loop = 76
next_round = R10
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```


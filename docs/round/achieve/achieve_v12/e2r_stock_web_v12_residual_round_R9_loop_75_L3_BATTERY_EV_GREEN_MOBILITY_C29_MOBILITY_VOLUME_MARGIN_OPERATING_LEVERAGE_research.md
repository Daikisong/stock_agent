# E2R Stock-Web v12 Residual Research — R9 Loop 75 / L3 / C29

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 75,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 75,
  "computed_next_round": "R10",
  "computed_next_loop": 75,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "AUTO_MOTOR_THERMAL_BODY_MODULE_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE",
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

Previous completed state in this interactive run: R8 / loop 75.

Therefore:

```text
scheduled_round = R9
scheduled_loop = 75
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 75
```

R9 was routed to mobility/transport rather than construction because R10 is the dedicated construction/PF round.  
This file tests auto supplier volume/mix/margin bridges, not OEM headline beta.

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

This run uses three different symbols:

```text
064960 / SNT모티브 / motor-module mix margin bridge
023800 / 인지컨트롤스 / thermal-management theme beta fade
024900 / 덕양산업 / body-module battery-housing beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected 180D window.
```

## Research thesis

C29 is not “auto part stock went up.”

The mechanism must pass through:

```text
vehicle volume / OEM program
→ product mix, pricing or customer cadence
→ utilization and margin conversion
→ durable operating leverage
```

A parts theme is the showroom window.  
The real C29 bridge is the purchase order, production slot and gross margin walking through the factory door.

---

## Case 1 — Slow positive / boundary: 064960 / SNT모티브

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is motor/module mix, electrification component exposure, customer program stability, pricing and margin bridge evidence.

```text
evidence_family = AUTO_MOTOR_MODULE_ELECTRIFICATION_DEFENSE_MIX_MARGIN_CAPITAL_RETURN_BRIDGE
case_role = positive_slow_boundary_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 44,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/064/064960/2024.csv`:

```text
2024-02-01,44400,45950,44000,44600
2024-02-05,46350,47050,44950,45800
2024-06-13,46600,48250,46600,47150
2024-06-28,49950,50300,49350,49850
2024-08-05,41550,42550,39500,39900
```

### Backtest

```text
MFE_30D  = +5.97%
MAE_30D  = -2.82%
MFE_90D  = +8.67%
MAE_90D  = -2.82%
MFE_180D = +13.29%
MAE_180D = -11.04%
peak_180 = 50,300 on 2024-06-28
trough_180 = 39,500 on 2024-08-05
peak_to_later_drawdown = -21.47%
```

### Interpretation

This is not an explosive C29 winner.  
It is the slow supplier rerating shape. The row is useful because it prevents the model from overfitting only to high-beta mobility names.

Correct treatment:

```text
source repair first
then Stage2-Yellow candidate
lifecycle local 4B if mix/margin evidence fades
```

---

## Case 2 — Counterexample / local 4B: 023800 / 인지컨트롤스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests thermal-management / cooling auto-parts theme beta without customer-volume and margin bridge.

```text
evidence_family = THERMAL_MANAGEMENT_COOLING_AUTO_PARTS_THEME_WITH_WEAK_CUSTOMER_VOLUME_MARGIN_BRIDGE
case_role = counterexample_theme_beta_local4b
trigger_date = 2024-02-14
entry_date = 2024-02-15
entry_price = 8,340
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/023/023800/2024.csv`:

```text
2024-02-15,8340,10070,8160,9090
2024-02-27,8350,8480,8200,8210
2024-04-08,7600,7600,7470,7510
2024-07-24,6750,6900,6750,6840
2024-08-05,6530,6620,5510,5770
```

### Backtest

```text
MFE_30D  = +20.74%
MAE_30D  = -1.68%
MFE_90D  = +20.74%
MAE_90D  = -10.67%
MFE_180D = +20.74%
MAE_180D = -33.93%
peak_180 = 10,070 on 2024-02-15
trough_180 = 5,510 on 2024-08-05
peak_to_later_drawdown = -45.28%
```

### Interpretation

This is the thermal-management theme beta failure.  
The early move was tradable, but the bridge did not hold.

C29 should classify it as:

```text
false Stage2 / local 4B-watch
```

unless customer program, volume and margin evidence is repaired.

---

## Case 3 — Counterexample / local 4B: 024900 / 덕양산업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests body-module / battery-housing / interior auto-parts beta without durable OEM-volume and margin bridge.

```text
evidence_family = AUTO_INTERIOR_BODY_MODULE_BATTERY_HOUSING_THEME_WITH_WEAK_VOLUME_MARGIN_BRIDGE
case_role = counterexample_theme_beta_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 4,790
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/024/024900/2024.csv`:

```text
2024-02-01,4790,4960,4700,4930
2024-02-05,5520,6150,5400,5410
2024-03-21,4710,4820,4700,4780
2024-07-24,3975,4020,3930,3960
2024-08-05,3500,3605,2990,3155
```

### Backtest

```text
MFE_30D  = +28.39%
MAE_30D  = -6.16%
MFE_90D  = +28.39%
MAE_90D  = -6.89%
MFE_180D = +28.39%
MAE_180D = -37.58%
peak_180 = 6,150 on 2024-02-05
trough_180 = 2,990 on 2024-08-05
peak_to_later_drawdown = -51.38%
```

### Interpretation

This is a C29 beta-fade row.  
The body-module / battery-housing narrative produced MFE, but not durable operating leverage.

Correct treatment:

```text
theme beta
→ no OEM volume/mix/margin bridge
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
```

### What this does not justify

```text
do_not_raise_generic_C29_auto_parts_weight = true
do_not_treat_all_mobility_parts_MFE_as_Green = true
do_not_convert_auto_supplier_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
AUTO_MOTOR_THERMAL_BODY_MODULE_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE
```

This fine archetype covers:

```text
1. motor/module supplier mix-margin bridge → slow Stage2 possible after source repair
2. thermal-management/cooling theme beta without customer-volume bridge → false Stage2 / local 4B
3. body-module/battery-housing beta without OEM-volume bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R9L75-C29-064960-SNT-MOTIVE-MOTOR-DEFENSE-AUTO-MIX-MARGIN", "symbol": "064960", "company_name": "SNT모티브", "round": "R9", "loop": "75", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_MOTOR_THERMAL_BODY_MODULE_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-SlowPositive / MotorModuleMixMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should include slow mobility suppliers when motor/module mix, electrification component exposure, customer program stability and margin bridge are visible. SNT Motive is not an explosive beta row; it is a low-volatility supplier rerating candidate that should not be overblocked but still needs non-price mix/margin evidence.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer-volume, OEM program, motor/thermal/body-module mix, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L75-C29-023800-INZI-CONTROLS-THERMAL-MANAGEMENT-BETA-FADE", "symbol": "023800", "company_name": "인지컨트롤스", "round": "R9", "loop": "75", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_MOTOR_THERMAL_BODY_MODULE_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ThermalManagementThemeBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not treat thermal-management or cooling-system theme beta as durable Stage2 unless customer volume, OEM program, pricing/mix and margin bridge refreshes. Inzi Controls had a sharp tradable spike but later opened large MAE and drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer-volume, OEM program, motor/thermal/body-module mix, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L75-C29-024900-DY-DEOKYANG-BODY-BATTERY-HOUSING-BETA-FADE", "symbol": "024900", "company_name": "덕양산업", "round": "R9", "loop": "75", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_MOTOR_THERMAL_BODY_MODULE_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / BodyModuleBatteryHousingBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not treat body-module, interior or battery-housing beta as durable Stage2 unless OEM volume, product mix, program award, pricing and margin bridge are visible. Deokyang Industrial produced a strong early MFE but then opened high MAE and a deep drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer-volume, OEM program, motor/thermal/body-module mix, pricing and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R9L75-C29-064960-SNT-MOTIVE-MOTOR-DEFENSE-AUTO-MIX-MARGIN", "case_id": "R9L75-C29-064960-SNT-MOTIVE-MOTOR-DEFENSE-AUTO-MIX-MARGIN", "symbol": "064960", "company_name": "SNT모티브", "round": "R9", "loop": "75", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_MOTOR_THERMAL_BODY_MODULE_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-SlowPositive / MotorModuleMixMarginBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 44400.0, "evidence_available_at_that_date": "AUTO_MOTOR_MODULE_ELECTRIFICATION_DEFENSE_MIX_MARGIN_CAPITAL_RETURN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SNT_MOTIVE_2024_MOTOR_MODULE_ELECTRIFICATION_CUSTOMER_PROGRAM_MIX_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_volume_or_OEM_program_candidate", "mix_or_pricing_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "program_award_or_order_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "theme_beta", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064960/2024.csv", "profile_path": "atlas/symbol_profiles/064/064960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.97, "MFE_90D_pct": 8.67, "MFE_180D_pct": 13.29, "MAE_30D_pct": -2.82, "MAE_90D_pct": -2.82, "MAE_180D_pct": -11.04, "peak_date": "2024-06-28", "peak_price": 50300.0, "drawdown_after_peak_pct": -21.47, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_supplier_peak_if_volume_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_pricing_or_margin_break", "trigger_outcome_label": "positive_slow_boundary_with_later_4b_watch", "current_profile_verdict": "C29 should include slow mobility suppliers when motor/module mix, electrification component exposure, customer program stability and margin bridge are visible. SNT Motive is not an explosive beta row; it is a low-volatility supplier rerating candidate that should not be overblocked but still needs non-price mix/margin evidence.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_SUPPLIER_064960_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L75-C29-023800-INZI-CONTROLS-THERMAL-MANAGEMENT-BETA-FADE", "case_id": "R9L75-C29-023800-INZI-CONTROLS-THERMAL-MANAGEMENT-BETA-FADE", "symbol": "023800", "company_name": "인지컨트롤스", "round": "R9", "loop": "75", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_MOTOR_THERMAL_BODY_MODULE_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-FalsePositive / ThermalManagementThemeBetaFade", "trigger_date": "2024-02-14", "entry_date": "2024-02-15", "entry_price": 8340.0, "evidence_available_at_that_date": "THERMAL_MANAGEMENT_COOLING_AUTO_PARTS_THEME_WITH_WEAK_CUSTOMER_VOLUME_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:INZI_CONTROLS_2024_THERMAL_MANAGEMENT_COOLING_CUSTOMER_VOLUME_PROGRAM_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_volume_or_OEM_program_candidate", "mix_or_pricing_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "program_award_or_order_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "theme_beta", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/023/023800/2024.csv", "profile_path": "atlas/symbol_profiles/023/023800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.74, "MFE_90D_pct": 20.74, "MFE_180D_pct": 20.74, "MAE_30D_pct": -1.68, "MAE_90D_pct": -10.67, "MAE_180D_pct": -33.93, "peak_date": "2024-02-15", "peak_price": 10070.0, "drawdown_after_peak_pct": -45.28, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_supplier_peak_if_volume_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_pricing_or_margin_break", "trigger_outcome_label": "counterexample_theme_beta_local4b", "current_profile_verdict": "C29 should not treat thermal-management or cooling-system theme beta as durable Stage2 unless customer volume, OEM program, pricing/mix and margin bridge refreshes. Inzi Controls had a sharp tradable spike but later opened large MAE and drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_SUPPLIER_023800_2024-02-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L75-C29-024900-DY-DEOKYANG-BODY-BATTERY-HOUSING-BETA-FADE", "case_id": "R9L75-C29-024900-DY-DEOKYANG-BODY-BATTERY-HOUSING-BETA-FADE", "symbol": "024900", "company_name": "덕양산업", "round": "R9", "loop": "75", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_MOTOR_THERMAL_BODY_MODULE_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-FalsePositive / BodyModuleBatteryHousingBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 4790.0, "evidence_available_at_that_date": "AUTO_INTERIOR_BODY_MODULE_BATTERY_HOUSING_THEME_WITH_WEAK_VOLUME_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DEOKYANG_2024_AUTO_INTERIOR_BODY_MODULE_BATTERY_HOUSING_OEM_VOLUME_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_volume_or_OEM_program_candidate", "mix_or_pricing_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "program_award_or_order_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "theme_beta", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024900/2024.csv", "profile_path": "atlas/symbol_profiles/024/024900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 28.39, "MFE_90D_pct": 28.39, "MFE_180D_pct": 28.39, "MAE_30D_pct": -6.16, "MAE_90D_pct": -6.89, "MAE_180D_pct": -37.58, "peak_date": "2024-02-05", "peak_price": 6150.0, "drawdown_after_peak_pct": -51.38, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_supplier_peak_if_volume_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_pricing_or_margin_break", "trigger_outcome_label": "counterexample_theme_beta_local4b", "current_profile_verdict": "C29 should not treat body-module, interior or battery-housing beta as durable Stage2 unless OEM volume, product mix, program award, pricing and margin bridge are visible. Deokyang Industrial produced a strong early MFE but then opened high MAE and a deep drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_SUPPLIER_024900_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L75-C29-064960-SNT-MOTIVE-MOTOR-DEFENSE-AUTO-MIX-MARGIN", "trigger_id": "TRG_R9L75-C29-064960-SNT-MOTIVE-MOTOR-DEFENSE-AUTO-MIX-MARGIN", "symbol": "064960", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 12, "OEM_program_visibility_score": 12, "mix_pricing_score": 11, "margin_bridge_score": 11, "relative_strength_score": 8, "execution_risk_score": 6, "theme_beta_risk_score": 7, "source_confidence_score": 2}, "weighted_score_before": 72, "stage_label_before": "Stage2-Yellow candidate after source repair", "raw_component_scores_after": {"customer_volume_score": 13, "OEM_program_visibility_score": 13, "mix_pricing_score": 13, "margin_bridge_score": 13, "relative_strength_score": 8, "execution_risk_score": 6, "theme_beta_risk_score": 7, "source_confidence_score": 2}, "weighted_score_after": 78, "stage_label_after": "Stage2-Yellow candidate after source repair + lifecycle 4B", "changed_components": ["customer_volume_score", "OEM_program_visibility_score", "mix_pricing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified mobility customer-volume/program mix and margin bridge; cap thermal/body-module/battery-housing theme beta when OEM program or margin evidence fails to refresh.", "MFE_90D_pct": 8.67, "MAE_90D_pct": -2.82, "score_return_alignment_label": "slow_positive_with_source_repair", "current_profile_verdict": "C29 should include slow mobility suppliers when motor/module mix, electrification component exposure, customer program stability and margin bridge are visible. SNT Motive is not an explosive beta row; it is a low-volatility supplier rerating candidate that should not be overblocked but still needs non-price mix/margin evidence."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L75-C29-023800-INZI-CONTROLS-THERMAL-MANAGEMENT-BETA-FADE", "trigger_id": "TRG_R9L75-C29-023800-INZI-CONTROLS-THERMAL-MANAGEMENT-BETA-FADE", "symbol": "023800", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 5, "OEM_program_visibility_score": 4, "mix_pricing_score": 3, "margin_bridge_score": 2, "relative_strength_score": 9, "execution_risk_score": 17, "theme_beta_risk_score": 18, "source_confidence_score": 2}, "weighted_score_before": 52, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_volume_score": 3, "OEM_program_visibility_score": 2, "mix_pricing_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 20, "theme_beta_risk_score": 21, "source_confidence_score": 2}, "weighted_score_after": 39, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_volume_score", "OEM_program_visibility_score", "mix_pricing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified mobility customer-volume/program mix and margin bridge; cap thermal/body-module/battery-housing theme beta when OEM program or margin evidence fails to refresh.", "MFE_90D_pct": 20.74, "MAE_90D_pct": -10.67, "score_return_alignment_label": "false_positive_mobility_theme_beta_bridge_gap", "current_profile_verdict": "C29 should not treat thermal-management or cooling-system theme beta as durable Stage2 unless customer volume, OEM program, pricing/mix and margin bridge refreshes. Inzi Controls had a sharp tradable spike but later opened large MAE and drawdown."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L75-C29-024900-DY-DEOKYANG-BODY-BATTERY-HOUSING-BETA-FADE", "trigger_id": "TRG_R9L75-C29-024900-DY-DEOKYANG-BODY-BATTERY-HOUSING-BETA-FADE", "symbol": "024900", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 5, "OEM_program_visibility_score": 4, "mix_pricing_score": 3, "margin_bridge_score": 2, "relative_strength_score": 9, "execution_risk_score": 17, "theme_beta_risk_score": 18, "source_confidence_score": 2}, "weighted_score_before": 52, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_volume_score": 3, "OEM_program_visibility_score": 2, "mix_pricing_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 20, "theme_beta_risk_score": 21, "source_confidence_score": 2}, "weighted_score_after": 39, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_volume_score", "OEM_program_visibility_score", "mix_pricing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified mobility customer-volume/program mix and margin bridge; cap thermal/body-module/battery-housing theme beta when OEM program or margin evidence fails to refresh.", "MFE_90D_pct": 28.39, "MAE_90D_pct": -6.89, "score_return_alignment_label": "false_positive_mobility_theme_beta_bridge_gap", "current_profile_verdict": "C29 should not treat body-module, interior or battery-housing beta as durable Stage2 unless OEM volume, product mix, program award, pricing and margin bridge are visible. Deokyang Industrial produced a strong early MFE but then opened high MAE and a deep drawdown."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R9", "loop": 75, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_MOTOR_THERMAL_BODY_MODULE_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C29 mobility supplier symbols outside top-covered OEM/tire set, +3 motor/thermal/body-module trigger families, +1 slow supplier rerating candidate, +2 mobility theme-beta local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R9", "loop": 75, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "axis": "auto_motor_thermal_body_module_volume_mix_margin_bridge_vs_parts_theme_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C29 should split verified mobility supplier customer-volume/mix/margin bridges from auto-parts theme beta. Stage2 requires OEM program visibility, customer volume, product mix/pricing, motor/thermal/body-module order evidence or margin conversion. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["064960", "023800", "024900"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": 75, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C29 needs mobility volume/mix/margin proof. SNT Motive shows a slow motor/module supplier rerating candidate after source repair; Inzi Controls and Deokyang show thermal/body-module theme beta fading into local 4B when customer-volume and margin bridge are absent."}
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
064960:
  corporate_action_candidate_dates = 2002-12-24, 2012-12-26, 2025-01-24, 2025-02-26
  selected window = 2024-02-01~D+180
  contamination = false because 180D window ends before 2025 candidates

023800:
  corporate_action_candidate_dates = 1997-06-25, 1998-04-27
  selected window = 2024-02-15~D+180
  contamination = false

024900:
  corporate_action_candidate_dates = 1997-06-23, 1998-12-24, 1999-01-28, 2014-10-23
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C29 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C29 rule-shape discovery,
but coding-agent promotion requires non-proxy customer-volume, OEM program, motor/thermal/body-module mix, pricing and margin evidence.
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
auto_motor_thermal_body_module_volume_mix_margin_bridge_vs_parts_theme_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 064960, 023800 and 024900.
4. Keep generic C29 mobility/auto-parts weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - OEM customer volume or named program visibility is explicit,
   - product mix, pricing, motor/thermal/body-module bridge exists,
   - utilization and margin conversion is visible,
   - MAE remains controlled or the signal is explicitly slow/lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is auto-parts or mobility theme beta only,
   - OEM-volume or margin evidence is weak/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, order cut, program delay, pricing/mix collapse, financing or margin break.
8. Emit before/after diagnostics and reject if verified mobility supplier mix-margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R9
completed_loop = 75
next_round = R10
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```


# E2R Stock-Web v12 Residual Research — R9 Loop 80 / L3 / C29

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 80,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 80,
  "computed_next_round": "R10",
  "computed_next_loop": 80,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "AUTO_INTERIOR_CONNECTOR_MOTOR_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "mobility_supplier_volume_margin_guardrail",
    "auto_interior_connector_motor_volume_mix_margin_bridge",
    "bounded_no_forced4B_auto_supplier_boundary",
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

Previous completed state in this interactive run: R8 / loop 80.

Therefore:

```text
scheduled_round = R9
scheduled_loop = 80
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 80
```

R9 was routed to mobility/transport rather than construction because R10 is the dedicated construction/PF round.  
This file tests auto interior modules, connectors and motor/drivetrain supplier volume-margin bridges.

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

This run uses three different symbols and avoids loop-79 R9 names:

```text
200880 / 서연이화 / auto interior module volume-mix lifecycle
025540 / 한국단자 / auto connector/electronics theme local 4B
064960 / SNT모티브 / motor/drivetrain bounded RiskWatch no-forced-4B boundary
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected 180D window.
```

## Research thesis

C29 is not “자동차 부품주가 올랐다.”

The mechanism must pass through:

```text
customer program / mobility demand
→ module, connector, motor or drivetrain volume
→ product mix / content growth
→ utilization, pricing and operating leverage
→ margin bridge
→ durable rerating
```

모빌리티 supplier는 완성차의 심장 박동을 받아 움직이는 기어다.  
C29가 보려는 것은 그 기어가 실제 고객 프로그램, 물량, 믹스, 가동률, 마진으로 맞물리는지다.

---

## Case 1 — Auto interior lifecycle positive: 200880 / 서연이화

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is auto interior/module customer program volume, product mix, utilization, pricing and margin bridge evidence.

```text
evidence_family = AUTO_INTERIOR_MODULE_CUSTOMER_PROGRAM_VOLUME_PRODUCT_MIX_UTILIZATION_MARGIN_BRIDGE
case_role = positive_auto_interior_volume_mix_with_later_high_MAE_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 16,830
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/200/200880/2024.csv`:

```text
2024-02-01,16830,18320,16730,18000
2024-02-02,18830,23150,18500,22450
2024-02-07,23750,25000,22350,22550
2024-04-19,17350,17470,16450,16610
2024-06-17,19660,21400,19550,20900
2024-06-27,22100,23200,21550,21950
2024-08-05,14960,15000,12610,13150
```

### Backtest

```text
MFE_30D  = +48.54%
MAE_30D  = -0.59%
MFE_90D  = +48.54%
MAE_90D  = -2.26%
MFE_180D = +48.54%
MAE_180D = -25.07%
peak_180 = 25,000 on 2024-02-07
trough_180 = 12,610 on 2024-08-05
peak_to_later_drawdown = -49.56%
```

### Interpretation

This is a C29 auto-interior lifecycle candidate.  
The early MFE was large and entry-basis MAE was controlled, but the later MAE path means permanent Green would be wrong.

Correct treatment:

```text
verified customer program / module volume / product mix / margin bridge → Stage2 possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 025540 / 한국단자

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests connector/electronics auto-parts theme beta without enough customer program, content growth and margin bridge.

```text
evidence_family = AUTO_CONNECTOR_EV_ELECTRONICS_CUSTOMER_PROGRAM_VOLUME_THEME_WITH_WEAK_MARGIN_BRIDGE
case_role = counterexample_auto_connector_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 69,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/025/025540/2024.csv`:

```text
2024-02-01,69500,70000,68100,69800
2024-02-14,68800,74600,68500,73100
2024-02-29,65000,65000,63300,63500
2024-06-18,74900,75500,72900,73400
2024-08-05,59500,59500,53500,55200
2024-08-14,63800,81400,63700,73300
2024-09-09,65000,68500,65000,66600
```

### Backtest

```text
MFE_30D  = +7.34%
MAE_30D  = -8.92%
MFE_90D  = +8.63%
MAE_90D  = -12.66%
MFE_180D = +17.12%
MAE_180D = -23.02%
peak_180 = 81,400 on 2024-08-14
trough_180 = 53,500 on 2024-08-05
peak_to_later_drawdown = -20.15%
```

### Interpretation

This is a C29 connector/electronics theme boundary.  
The price path had bursts, but the bridge was not strong enough to call durable operating leverage without source repair.

Correct treatment:

```text
connector / EV electronics theme beta
→ no verified customer program / content growth / margin bridge
→ local 4B-watch, not durable Green
```

---

## Case 3 — Bounded no-forced-4B boundary: 064960 / SNT모티브

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests motor/drivetrain supplier beta with bounded MAE but incomplete rerating bridge.

```text
evidence_family = AUTO_MOTOR_DRIVETRAIN_EV_COMPONENT_VOLUME_MIX_MARGIN_WITH_BOUNDED_MAE_AND_WEAK_RERATING_BRIDGE
case_role = overbearish_counterexample_bounded_motor_drivetrain_no_forced4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 44,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/064/064960/2024.csv`:

```text
2024-02-01,44400,45950,44000,44600
2024-02-05,46350,47050,44950,45800
2024-02-14,43000,44350,42850,43900
2024-06-12,46250,47300,45800,46450
2024-06-21,47500,48950,47450,47800
2024-07-01,49800,50300,49550,50000
2024-08-05,41550,42550,39500,39900
```

### Backtest

```text
MFE_30D  = +5.97%
MAE_30D  = -3.49%
MFE_90D  = +6.53%
MAE_90D  = -3.49%
MFE_180D = +13.29%
MAE_180D = -11.04%
peak_180 = 50,300 on 2024-07-01
trough_180 = 39,500 on 2024-08-05
peak_to_later_drawdown = -21.47%
```

### Interpretation

This is not durable Stage2, but it is also not forced local 4B.  
The price path stayed bounded enough that the correct result is RiskWatch unless non-price bridge breaks.

Correct treatment:

```text
motor/drivetrain volume-mix watch
bounded MAE
→ no durable Stage2 without customer volume / mix / margin bridge
→ no forced 4B without non-price deterioration
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
bounded_MAE_no_forced_4B_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C29_mobility_parts_theme_weight = true
do_not_treat_all_auto_parts_MFE_as_Green = true
do_not_force_4B_on_bounded_motor_drivetrain_rows = true
do_not_convert_mobility_supplier_drawdown_to_hard_4C_without_non_price_customer_program_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
AUTO_INTERIOR_CONNECTOR_MOTOR_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_FADE
```

This fine archetype covers:

```text
1. auto interior/module customer program and mix bridge → Stage2 possible after source repair
2. connector/electronics theme beta without content-growth margin bridge → false Stage2 / local 4B
3. bounded motor/drivetrain supplier beta → RiskWatch / no durable Stage2 / no forced 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R9L80-C29-200880-SEOYON-EHWA-AUTO-INTERIOR-VOLUME-MIX-LIFECYCLE", "symbol": "200880", "company_name": "서연이화", "round": "R9", "loop": "80", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_CONNECTOR_MOTOR_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-AutoInteriorModuleVolumeMixMarginBridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should preserve auto interior/module positives when customer program volume, product mix, utilization, pricing and margin bridge are visible. Seoyon E-Hwa produced a very large early MFE but later high MAE requires lifecycle local 4B if volume/mix/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer program, module/connector/motor volume, product mix, utilization, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L80-C29-025540-KET-AUTO-CONNECTOR-THEME-LOCAL4B", "symbol": "025540", "company_name": "한국단자", "round": "R9", "loop": "80", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_CONNECTOR_MOTOR_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / AutoConnectorEVElectronicsVolumeMarginBridgeGap", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not treat auto connector/electronics theme beta as durable Stage2 unless customer program volume, connector content growth, utilization, pricing and margin bridge are visible. Korea Electric Terminal had modest MFE and later high MAE.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer program, module/connector/motor volume, product mix, utilization, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L80-C29-064960-SNT-MOTIV-MOTOR-DRIVETRAIN-BOUNDED-RISKWATCH", "symbol": "064960", "company_name": "SNT모티브", "round": "R9", "loop": "80", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_CONNECTOR_MOTOR_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-BoundedMotorDrivetrainVolumeMixNoForced4BNoDurableStage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not force bounded motor/drivetrain supplier rows into 4B when MAE is contained, but it also should not mark durable Stage2 without customer volume, mix, drivetrain content and margin bridge. SNT Motiv is a bounded RiskWatch row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer program, module/connector/motor volume, product mix, utilization, pricing and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R9L80-C29-200880-SEOYON-EHWA-AUTO-INTERIOR-VOLUME-MIX-LIFECYCLE", "case_id": "R9L80-C29-200880-SEOYON-EHWA-AUTO-INTERIOR-VOLUME-MIX-LIFECYCLE", "symbol": "200880", "company_name": "서연이화", "round": "R9", "loop": "80", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_CONNECTOR_MOTOR_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-Lifecycle-AutoInteriorModuleVolumeMixMarginBridgeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 16830.0, "evidence_available_at_that_date": "AUTO_INTERIOR_MODULE_CUSTOMER_PROGRAM_VOLUME_PRODUCT_MIX_UTILIZATION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SEOYON_EHWA_2024_AUTO_INTERIOR_MODULE_CUSTOMER_PROGRAM_VOLUME_MIX_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_program_or_volume_candidate", "product_mix_or_content_growth_candidate", "utilization_pricing_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "module_connector_motor_volume_bridge_candidate"], "stage4b_evidence_fields": ["mobility_parts_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/200/200880/2024.csv", "profile_path": "atlas/symbol_profiles/200/200880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 48.54, "MFE_90D_pct": 48.54, "MFE_180D_pct": 48.54, "MAE_30D_pct": -0.59, "MAE_90D_pct": -2.26, "MAE_180D_pct": -25.07, "peak_date": "2024-02-07", "peak_price": 25000.0, "drawdown_after_peak_pct": -49.56, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_volume_margin_peak_if_customer_program_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_volume_pricing_margin_or_financing_break", "trigger_outcome_label": "positive_auto_interior_volume_mix_with_later_high_MAE_4b_watch", "current_profile_verdict": "C29 should preserve auto interior/module positives when customer program volume, product mix, utilization, pricing and margin bridge are visible. Seoyon E-Hwa produced a very large early MFE but later high MAE requires lifecycle local 4B if volume/mix/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_VOLUME_MARGIN_200880_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L80-C29-025540-KET-AUTO-CONNECTOR-THEME-LOCAL4B", "case_id": "R9L80-C29-025540-KET-AUTO-CONNECTOR-THEME-LOCAL4B", "symbol": "025540", "company_name": "한국단자", "round": "R9", "loop": "80", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_CONNECTOR_MOTOR_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-FalsePositive / AutoConnectorEVElectronicsVolumeMarginBridgeGap", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 69500.0, "evidence_available_at_that_date": "AUTO_CONNECTOR_EV_ELECTRONICS_CUSTOMER_PROGRAM_VOLUME_THEME_WITH_WEAK_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KOREA_ELECTRIC_TERMINAL_2024_AUTO_CONNECTOR_EV_ELECTRONICS_CUSTOMER_VOLUME_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_program_or_volume_candidate", "product_mix_or_content_growth_candidate", "utilization_pricing_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "module_connector_motor_volume_bridge_candidate"], "stage4b_evidence_fields": ["mobility_parts_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025540/2024.csv", "profile_path": "atlas/symbol_profiles/025/025540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.34, "MFE_90D_pct": 8.63, "MFE_180D_pct": 17.12, "MAE_30D_pct": -8.92, "MAE_90D_pct": -12.66, "MAE_180D_pct": -23.02, "peak_date": "2024-08-14", "peak_price": 81400.0, "drawdown_after_peak_pct": -20.15, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_volume_margin_peak_if_customer_program_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_volume_pricing_margin_or_financing_break", "trigger_outcome_label": "counterexample_auto_connector_theme_local4b", "current_profile_verdict": "C29 should not treat auto connector/electronics theme beta as durable Stage2 unless customer program volume, connector content growth, utilization, pricing and margin bridge are visible. Korea Electric Terminal had modest MFE and later high MAE.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_VOLUME_MARGIN_025540_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L80-C29-064960-SNT-MOTIV-MOTOR-DRIVETRAIN-BOUNDED-RISKWATCH", "case_id": "R9L80-C29-064960-SNT-MOTIV-MOTOR-DRIVETRAIN-BOUNDED-RISKWATCH", "symbol": "064960", "company_name": "SNT모티브", "round": "R9", "loop": "80", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_CONNECTOR_MOTOR_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "RiskWatch-BoundedMotorDrivetrainVolumeMixNoForced4BNoDurableStage2", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 44400.0, "evidence_available_at_that_date": "AUTO_MOTOR_DRIVETRAIN_EV_COMPONENT_VOLUME_MIX_MARGIN_WITH_BOUNDED_MAE_AND_WEAK_RERATING_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SNT_MOTIV_2024_MOTOR_DRIVETRAIN_EV_COMPONENT_CUSTOMER_VOLUME_MIX_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_program_or_volume_candidate", "product_mix_or_content_growth_candidate", "utilization_pricing_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "module_connector_motor_volume_bridge_candidate"], "stage4b_evidence_fields": ["mobility_parts_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064960/2024.csv", "profile_path": "atlas/symbol_profiles/064/064960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.97, "MFE_90D_pct": 6.53, "MFE_180D_pct": 13.29, "MAE_30D_pct": -3.49, "MAE_90D_pct": -3.49, "MAE_180D_pct": -11.04, "peak_date": "2024-07-01", "peak_price": 50300.0, "drawdown_after_peak_pct": -21.47, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_volume_margin_peak_if_customer_program_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_volume_pricing_margin_or_financing_break", "trigger_outcome_label": "overbearish_counterexample_bounded_motor_drivetrain_no_forced4b", "current_profile_verdict": "C29 should not force bounded motor/drivetrain supplier rows into 4B when MAE is contained, but it also should not mark durable Stage2 without customer volume, mix, drivetrain content and margin bridge. SNT Motiv is a bounded RiskWatch row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_VOLUME_MARGIN_064960_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L80-C29-200880-SEOYON-EHWA-AUTO-INTERIOR-VOLUME-MIX-LIFECYCLE", "trigger_id": "TRG_R9L80-C29-200880-SEOYON-EHWA-AUTO-INTERIOR-VOLUME-MIX-LIFECYCLE", "symbol": "200880", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 14, "program_visibility_score": 13, "mix_content_growth_score": 13, "utilization_pricing_score": 12, "margin_bridge_score": 13, "relative_strength_score": 11, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"customer_volume_score": 16, "program_visibility_score": 15, "mix_content_growth_score": 15, "utilization_pricing_score": 14, "margin_bridge_score": 15, "relative_strength_score": 10, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["customer_volume_score", "program_visibility_score", "mix_content_growth_score", "utilization_pricing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer program, module/connector/motor volume, mix/content growth, utilization/pricing and margin bridge; cap mobility theme beta when bridge fails to refresh while preserving bounded RiskWatch rows from forced 4B.", "MFE_90D_pct": 48.54, "MAE_90D_pct": -2.26, "score_return_alignment_label": "mobility_volume_margin_positive_with_lifecycle_4b", "current_profile_verdict": "C29 should preserve auto interior/module positives when customer program volume, product mix, utilization, pricing and margin bridge are visible. Seoyon E-Hwa produced a very large early MFE but later high MAE requires lifecycle local 4B if volume/mix/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L80-C29-025540-KET-AUTO-CONNECTOR-THEME-LOCAL4B", "trigger_id": "TRG_R9L80-C29-025540-KET-AUTO-CONNECTOR-THEME-LOCAL4B", "symbol": "025540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 4, "program_visibility_score": 3, "mix_content_growth_score": 2, "utilization_pricing_score": 2, "margin_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_before": 43, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_volume_score": 3, "program_visibility_score": 1, "mix_content_growth_score": 1, "utilization_pricing_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_after": 33, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_volume_score", "program_visibility_score", "mix_content_growth_score", "utilization_pricing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer program, module/connector/motor volume, mix/content growth, utilization/pricing and margin bridge; cap mobility theme beta when bridge fails to refresh while preserving bounded RiskWatch rows from forced 4B.", "MFE_90D_pct": 8.63, "MAE_90D_pct": -12.66, "score_return_alignment_label": "false_positive_auto_parts_bridge_gap", "current_profile_verdict": "C29 should not treat auto connector/electronics theme beta as durable Stage2 unless customer program volume, connector content growth, utilization, pricing and margin bridge are visible. Korea Electric Terminal had modest MFE and later high MAE."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L80-C29-064960-SNT-MOTIV-MOTOR-DRIVETRAIN-BOUNDED-RISKWATCH", "trigger_id": "TRG_R9L80-C29-064960-SNT-MOTIV-MOTOR-DRIVETRAIN-BOUNDED-RISKWATCH", "symbol": "064960", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 7, "program_visibility_score": 6, "mix_content_growth_score": 5, "utilization_pricing_score": 5, "margin_bridge_score": 4, "relative_strength_score": 5, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no forced 4B", "raw_component_scores_after": {"customer_volume_score": 6, "program_visibility_score": 5, "mix_content_growth_score": 4, "utilization_pricing_score": 4, "margin_bridge_score": 3, "relative_strength_score": 5, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / no durable Stage2 and no forced 4B", "changed_components": ["customer_volume_score", "program_visibility_score", "mix_content_growth_score", "utilization_pricing_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer program, module/connector/motor volume, mix/content growth, utilization/pricing and margin bridge; cap mobility theme beta when bridge fails to refresh while preserving bounded RiskWatch rows from forced 4B.", "MFE_90D_pct": 6.53, "MAE_90D_pct": -3.49, "score_return_alignment_label": "bounded_mobility_supplier_no_forced4b", "current_profile_verdict": "C29 should not force bounded motor/drivetrain supplier rows into 4B when MAE is contained, but it also should not mark durable Stage2 without customer volume, mix, drivetrain content and margin bridge. SNT Motiv is a bounded RiskWatch row."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R9", "loop": 80, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_INTERIOR_CONNECTOR_MOTOR_VOLUME_MIX_MARGIN_BRIDGE_VS_PARTS_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 1, "overbearish_counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C29 mobility supplier symbols outside top-covered 000270/204320/011210/005380/003490 set and outside loop-79 R9 names, +3 interior/connector/motor trigger families, +1 auto-interior lifecycle positive, +1 connector local-4B counterexample, +1 bounded no-forced-4B motor/drivetrain boundary, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R9", "loop": 80, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "axis": "auto_interior_connector_motor_volume_mix_margin_bridge_vs_parts_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C29 should split verified module/connector/motor volume-margin rerating from generic auto/EV parts theme beta. Stage2 requires customer program volume, product mix or content growth, utilization, pricing and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Bounded motor/drivetrain supplier rows should remain RiskWatch/no durable Stage2, not forced 4B.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["200880", "025540", "064960"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": 80, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "bounded_MAE_no_forced_4B_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C29 needs customer program, volume, mix/content, utilization/pricing and margin proof. Seoyon E-Hwa shows an auto-interior module lifecycle candidate after source repair; Korea Electric Terminal shows connector theme fading into local 4B; SNT Motiv shows a bounded motor/drivetrain RiskWatch row where forced 4B would be too harsh."}
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
200880:
  name = 서연이화 from 2016-01-14, 한일이화 before that
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

025540:
  name = 한국단자 from 1996-10-16, 한국단자공업 before that
  corporate_action_candidate_dates = 1997-01-03, 1999-04-26
  selected window = 2024-02-01~D+180
  contamination = false

064960:
  name = SNT모티브 from 2021-03-12, S&T모티브 / S&T대우 / 대우정밀 before that
  corporate_action_candidate_dates = 2002-12-24, 2012-12-26, 2025-01-24, 2025-02-26
  selected 180D window = 2024-02-01~D+180
  contamination = false for 180D
  longer horizon should check 2025 corporate-action candidates
```

Data-quality caveat:

```text
All selected C29 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C29 rule-shape discovery,
but coding-agent promotion requires non-proxy customer program, module/connector/motor volume, product mix, utilization, pricing and margin bridge evidence.
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
auto_interior_connector_motor_volume_mix_margin_bridge_vs_parts_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 200880, 025540 and 064960.
4. Keep generic C29 mobility/auto-parts weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - customer program or mobility demand is explicit,
   - module / connector / motor / drivetrain volume is visible,
   - product mix or content-growth bridge exists,
   - utilization, pricing and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is auto-parts theme beta only,
   - customer program/volume/mix/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not force local 4B when bounded motor/drivetrain rows have controlled MAE and no confirmed non-price bridge break.
8. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, program delay, order cut, volume decline, pricing/mix collapse, financing or margin break.
9. Emit before/after diagnostics and reject if verified mobility volume-margin positives or bounded RiskWatch rows are overblocked.
```

---

## Final round state

```text
completed_round = R9
completed_loop = 80
next_round = R10
next_loop = 80
round_schedule_status = valid
round_sector_consistency = pass
```


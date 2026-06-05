# E2R Stock-Web v12 Residual Research — R9 Loop 90 / L3 / C29

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R9
loop: 90
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: PISTON_POWERTRAIN_VOLUME_MIX_BRIDGE_VS_SMALL_AUTOPARTS_COMPONENT_REBOUND_DECAY
sector: mobility / auto parts / powertrain / chassis / component supply / OEM volume / margin / cash conversion
output_file: e2r_stock_web_v12_residual_round_R9_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R8 loop 90`.

```text
scheduled_round = R9
scheduled_loop = 90
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

R9 is the mobility / auto-parts / EV operating-leverage lane.  
C29 remains the correct R9 archetype because the previous R9 loop also used C29, but the loop objective is residual expansion: fresh non-top symbols, new trigger dates, and bridge-vs-theme separation.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
rows = 60
symbols = 27
good/bad Stage2 = 26/13
4B/4C = 6/0
top-covered = 011210, 000270, 005380, 005850, 010690, 018880
```

This loop avoids the top-covered list and prior C29 loop sets:

```text
R9 loop84: 086280, 161390, 271940
R9 loop85: 000120, 003620, 215360
R9 loop86: 073240, 118990, 090080
R9 loop87: 004490, 009900, 024900
R9 loop88: 200880, 092200, 123040
R9 loop89: 064960, 067570, 012860
earlier known C29: 012330, 002350, 204320
```

Candidate hygiene note:

```text
During this execution path, a R8/C27 content-IP file was accidentally generated before the scheduler correction.
That file is not the valid output for this user request. The valid scheduled output is this R9/C29/loop90 MD.
```

Selected symbols:

```text
092780, 126640, 013870
```

The selected pocket is:

```text
powertrain/piston OEM volume + mix + cash bridge
vs
small chassis/precision auto-parts rebound without OEM volume / margin bridge
vs
thermal-management / pump auto-parts rebound without fresh customer volume / operating leverage bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"092780","company_name":"동양피스톤","current_or_latest_name":"DYP","profile_path":"atlas/symbol_profiles/092/092780.json","first_date":"2017-12-08","last_date":"2026-02-20","trading_day_count":2010,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Name changed from 동양피스톤 to DYP in 2025, outside the selected 2024 calibration window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"126640","company_name":"화신정공","profile_path":"atlas/symbol_profiles/126/126640.json","first_date":"2010-08-31","last_date":"2026-02-20","trading_day_count":3777,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2011-08-17"],"has_major_raw_discontinuity":true,"calibration_caveat":"SPAC/name-transition candidate exists long before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"013870","company_name":"지엠비코리아","profile_path":"atlas/symbol_profiles/013/013870.json","first_date":"2012-11-20","last_date":"2026-02-20","trading_day_count":3252,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"092780","trigger_type":"Stage2-Actionable-PowertrainPistonOEMVolumeMixCashBridge-Positive","entry_date":"2024-04-22","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"126640","trigger_type":"Stage2-FalsePositive-SmallChassisPartsRebound-NoFreshOEMVolumeMarginBridge","entry_date":"2024-01-02","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"013870","trigger_type":"Stage2-FalsePositive-ThermalPumpAutoPartsRebound-NoCustomerVolumeOperatingLeverageBridge","entry_date":"2024-01-02","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
```

## 4. Research question

C29 is not “자동차 부품주가 움직였다.”  
The useful mobility operating-leverage signal must prove the operating chain:

```text
fresh OEM/customer volume
program mix or model exposure
utilization recovery
price/cost pass-through
margin bridge
working-capital discipline
cash conversion
```

A parts supplier headline without this bridge is a crankshaft turning on a test bench. The motion is visible, but no torque reaches the road.

Residual question:

```text
Can C29 distinguish:
1. powertrain/piston supplier volume-mix-cash bridge with strong MFE and controlled early MAE,
2. small chassis/precision-parts rebound where no fresh OEM volume and margin bridge exists,
3. pump/thermal-management auto-parts rebound where the old auto theme does not prove customer volume, operating leverage or cash conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C29_R9L90_092780_DYP_POWERTRAIN_VOLUME_MIX","symbol":"092780","company_name":"동양피스톤","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"POWERTRAIN_PISTON_OEM_VOLUME_MIX_CASH_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-PowertrainPistonOEMVolumeMixCashBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_low_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_OEM_volume_mix_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Powertrain/piston supplier volume-mix proxy produced MFE90 above 50% with controlled early MAE. Later drawdown keeps Green strict and requires exact OEM program, utilization, margin and cash evidence."}
{"row_type":"case","case_id":"C29_R9L90_126640_HWASHIN_PRECISION_CHASSIS_REBOUND","symbol":"126640","company_name":"화신정공","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SMALL_CHASSIS_PRECISION_PARTS_REBOUND_WITHOUT_OEM_VOLUME_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallChassisPartsRebound-NoFreshOEMVolumeMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_no_volume_bridge","current_profile_verdict":"current_profile_false_positive_if_small_chassis_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Small chassis/precision-parts rebound had near-zero MFE and long drawdown without fresh OEM volume, program mix, margin or cash bridge."}
{"row_type":"case","case_id":"C29_R9L90_013870_GMB_THERMAL_PUMP_REBOUND","symbol":"013870","company_name":"지엠비코리아","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"THERMAL_PUMP_AUTOPARTS_REBOUND_WITHOUT_CUSTOMER_VOLUME_OPERATING_LEVERAGE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ThermalPumpAutoPartsRebound-NoCustomerVolumeOperatingLeverageBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_operating_leverage_bridge","current_profile_verdict":"current_profile_false_positive_if_pump_autoparts_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Thermal/pump auto-parts rebound had low MFE and later deep MAE without customer volume, utilization, mix, margin and cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 092780 동양피스톤 — powertrain/piston OEM volume-mix-cash bridge positive

Entry row: `2024-04-22 c=4585`.  
Observed path: early low `2024-04-22 l=4370`, peak `2024-06-21 h=7120`, and later low `2024-12-09 l=4250`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L90_C29_092780_20240422_STAGE2_POWERTRAIN_PISTON_VOLUME","case_id":"C29_R9L90_092780_DYP_POWERTRAIN_VOLUME_MIX","symbol":"092780","company_name":"동양피스톤","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"POWERTRAIN_PISTON_OEM_VOLUME_MIX_CASH_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-PowertrainPistonOEMVolumeMixCashBridge-Positive","trigger_date":"2024-04-22","entry_date":"2024-04-22","entry_price":4585.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_powertrain_piston_OEM_volume_mix_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; powertrain/piston OEM volume, program mix, utilization and margin/cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["OEM_volume_proxy","powertrain_program_mix_proxy","utilization_recovery_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_volume_source_pending","program_mix_source_pending","margin_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/092/092780/2024.csv","profile_path":"atlas/symbol_profiles/092/092780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.88,"MFE_90D_pct":55.29,"MFE_180D_pct":55.29,"MAE_30D_pct":-4.69,"MAE_90D_pct":-4.69,"MAE_180D_pct":-7.31,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-21","peak_price":7120.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":4250.0,"drawdown_after_peak_pct":-40.31,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.17,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_OEM_volume_program_mix_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_low_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_OEM_volume_mix_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_2024_window; 2025_name_change_outside_window","same_entry_group_id":"092780_2024-04-22_4585","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 can allow Stage2/Yellow when mobility strength is tied to OEM/customer volume, program mix, utilization, margin and cash conversion. Green requires exact source-grade evidence."}
```

### 6.2 126640 화신정공 — small chassis/precision-parts rebound without fresh OEM volume/margin bridge

Entry row: `2024-01-02 c=1711`.  
Observed path: high `2024-01-03 h=1735`, then long decay to `2024-12-09 l=1051`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L90_C29_126640_20240102_STAGE2_FALSE_POSITIVE_SMALL_CHASSIS","case_id":"C29_R9L90_126640_HWASHIN_PRECISION_CHASSIS_REBOUND","symbol":"126640","company_name":"화신정공","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SMALL_CHASSIS_PRECISION_PARTS_REBOUND_WITHOUT_OEM_VOLUME_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SmallChassisPartsRebound-NoFreshOEMVolumeMarginBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":1711.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_small_chassis_precision_parts_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; chassis/precision auto-parts rebound treated as insufficient without fresh OEM volume, program mix, utilization, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["small_autoparts_rebound","chassis_precision_parts_keyword"],"stage3_evidence_fields":["fresh_OEM_volume_missing","program_mix_missing","utilization_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["near_zero_MFE","volume_margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/126/126640/2024.csv","profile_path":"atlas/symbol_profiles/126/126640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.40,"MFE_90D_pct":1.40,"MFE_180D_pct":1.40,"MAE_30D_pct":-8.82,"MAE_90D_pct":-15.43,"MAE_180D_pct":-22.56,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-03","peak_price":1735.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1051.0,"drawdown_after_peak_pct":-39.42,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"small_chassis_parts_rebound_without_fresh_OEM_volume_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","volume_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_volume_bridge","current_profile_verdict":"current_profile_false_positive_if_small_chassis_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_SPAC_transition_pre_2024; selected_window_clean","same_entry_group_id":"126640_2024-01-02_1711","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not promote small auto-parts rebound without fresh OEM volume, program mix, utilization, margin and cash evidence. Near-zero MFE and persistent drawdown require Watch/4B routing."}
```

### 6.3 013870 지엠비코리아 — thermal/pump auto-parts rebound without customer-volume operating-leverage bridge

Entry row: `2024-01-02 c=4830`.  
Observed path: same-day high `2024-01-02 h=5000`, later low `2024-12-09 l=3480`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L90_C29_013870_20240102_STAGE2_FALSE_POSITIVE_THERMAL_PUMP","case_id":"C29_R9L90_013870_GMB_THERMAL_PUMP_REBOUND","symbol":"013870","company_name":"지엠비코리아","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"THERMAL_PUMP_AUTOPARTS_REBOUND_WITHOUT_CUSTOMER_VOLUME_OPERATING_LEVERAGE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-ThermalPumpAutoPartsRebound-NoCustomerVolumeOperatingLeverageBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":4830.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_thermal_pump_auto_parts_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; thermal/pump auto-parts rebound treated as insufficient without customer volume, operating leverage, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["thermal_pump_autoparts_rebound","legacy_auto_parts_keyword"],"stage3_evidence_fields":["fresh_customer_volume_missing","utilization_operating_leverage_missing","program_mix_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE_watch","operating_leverage_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013870/2024.csv","profile_path":"atlas/symbol_profiles/013/013870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.52,"MFE_90D_pct":5.59,"MFE_180D_pct":5.59,"MAE_30D_pct":-14.08,"MAE_90D_pct":-14.60,"MAE_180D_pct":-18.84,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":5100.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":3480.0,"drawdown_after_peak_pct":-31.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.63,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"thermal_pump_autoparts_rebound_without_customer_volume_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","operating_leverage_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_operating_leverage_bridge","current_profile_verdict":"current_profile_false_positive_if_pump_autoparts_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"013870_2024-01-02_4830","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not equate pump/thermal auto-parts rebound with operating leverage. Fresh customer volume, utilization, program mix, margin and cash bridge must be repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L90_092780_DYP_POWERTRAIN_VOLUME_MIX","trigger_id":"R9L90_C29_092780_20240422_STAGE2_POWERTRAIN_PISTON_VOLUME","symbol":"092780","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C29 requires OEM/customer volume, program mix, utilization, margin and cash bridge rather than mobility label alone","raw_component_scores_before":{"customer_volume_score":13,"program_mix_score":12,"operating_leverage_score":11,"utilization_score":10,"margin_bridge_score":10,"cash_conversion_score":8,"relative_strength_score":14,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"customer_volume_score":16,"program_mix_score":15,"operating_leverage_score":14,"utilization_score":12,"margin_bridge_score":12,"cash_conversion_score":10,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Powertrain/OEM volume bridge plus MFE90>50 supports Yellow-watch; exact OEM volume and margin/cash evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L90_126640_HWASHIN_PRECISION_CHASSIS_REBOUND","trigger_id":"R9L90_C29_126640_20240102_STAGE2_FALSE_POSITIVE_SMALL_CHASSIS","symbol":"126640","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"small chassis/precision-parts rebound without fresh OEM volume and margin bridge should be blocked","raw_component_scores_before":{"customer_volume_score":1,"program_mix_score":1,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_volume_score":0,"program_mix_score":0,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_repricing_score":0,"execution_risk_score":-20,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and persistent MAE expansion convert small auto-parts rebound into missing OEM-volume bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L90_013870_GMB_THERMAL_PUMP_REBOUND","trigger_id":"R9L90_C29_013870_20240102_STAGE2_FALSE_POSITIVE_THERMAL_PUMP","symbol":"013870","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"thermal/pump auto-parts rebound without customer volume and operating leverage should remain Watch/4B","raw_component_scores_before":{"customer_volume_score":2,"program_mix_score":1,"operating_leverage_score":1,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_volume_score":0,"program_mix_score":0,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-20,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and later drawdown require customer volume, utilization, margin and cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R9L90_C29_P0_CURRENT","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C29 needs explicit OEM volume, program mix, utilization, margin/cash and small-autoparts 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":20.76,"avg_MAE90_pct":-11.24,"avg_MFE180_pct":20.76,"avg_MAE180_pct":-16.24,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.60,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C29_OEM_volume_mix_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R9L90_C29_P1_SECTOR_SPECIFIC","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P1_L3_mobility_volume_mix_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 mobility signals need customer volume, program mix, utilization, operating leverage, margin or cash conversion before Stage2-Actionable","changed_axes":["customer_volume_required","program_mix_margin_required","small_autoparts_rebound_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_volume_program_mix_utilization_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":20.76,"avg_MAE90_pct":-11.24,"avg_MFE180_pct":20.76,"avg_MAE180_pct":-16.24,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R9L90_C29_P2_CANONICAL","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P2_C29_OEM_volume_mix_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C29 should reward OEM volume-to-margin mechanics, not small auto-parts rebound labels","changed_axes":["C29_OEM_volume_mix_margin_cash_bridge_required","C29_small_autoparts_component_rebound_local_4B_guard","C29_low_MFE_not_operating_leverage_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_volume_or_program_mix_plus_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":20.76,"avg_MAE90_pct":-11.24,"avg_MFE180_pct":20.76,"avg_MAE180_pct":-16.24,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R9L90_C29_P3_COUNTEREXAMPLE_GUARD","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P3_C29_low_MFE_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If OEM volume/margin bridge is missing, MFE90<10 should block Yellow/Green; if full-year MAE expands after low MFE, keep Watch/4B until exact evidence is repaired","changed_axes":["C29_low_MFE_guardrail","C29_bridge_missing_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_MFE90_lt_10"},"eligible_trigger_count":3,"avg_MFE90_pct":20.76,"avg_MAE90_pct":-11.24,"avg_MFE180_pct":20.76,"avg_MAE180_pct":-16.24,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_POWERTRAIN_POSITIVE_VS_SMALL_AUTOPARTS_REBOUND_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":20.76,"avg_MAE90_pct":-11.24,"avg_MFE180_pct":20.76,"avg_MAE180_pct":-16.24,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MFE90_lt10":0.67,"interpretation":"C29 needs bridge discipline. 동양피스톤 shows powertrain/OEM volume-mix bridge can support Yellow-watch, while 화신정공 and 지엠비코리아 show small auto-parts rebounds should not be promoted without fresh OEM volume, utilization, program mix, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"092780","trigger_type":"Stage2-Actionable-PowertrainPistonOEMVolumeMixCashBridge-Positive","entry_date":"2024-04-22","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_OEM_volume_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when OEM volume, program mix, utilization and margin/cash bridge exists; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"126640","trigger_type":"Stage2-FalsePositive-SmallChassisPartsRebound-NoFreshOEMVolumeMarginBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_bridge_missing","stage2_to_180D_outcome":"failed_small_chassis_rebound_deep_MAE","MFE90_ge20":false,"MFE90_lt10":true,"transition_note":"Small chassis/precision parts rebound without OEM volume and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"013870","trigger_type":"Stage2-FalsePositive-ThermalPumpAutoPartsRebound-NoCustomerVolumeOperatingLeverageBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"weak_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_thermal_pump_rebound_MAE_expansion","MFE90_ge20":false,"MFE90_lt10":true,"transition_note":"Thermal/pump auto-parts rebound without customer volume and operating leverage bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"small_autoparts_component_rebound_overcredit_without_OEM_volume_mix_margin_cash_bridge","contribution":"Adds two C29 4B counterexamples against one powertrain/OEM volume positive, avoiding C29 top-covered and prior C29 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"PISTON_POWERTRAIN_VOLUME_MIX_BRIDGE_VS_SMALL_AUTOPARTS_COMPONENT_REBOUND_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C29 now has non-top-symbol powertrain/piston OEM-volume positive and two small auto-parts weak-bridge counterexamples; next R9 loops should exact-URL repair OEM/customer volume, program mix, utilization, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_OEM_volume_mix_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"092780 worked when OEM volume/program-mix proxy existed; 126640 and 013870 failed when small auto-parts price action lacked fresh volume, utilization and margin bridge."}
{"row_type":"shadow_weight","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_small_autoparts_component_rebound_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Small chassis and thermal/pump auto-parts rows showed MFE90 below 10 when non-price OEM volume/margin evidence was missing."}
{"row_type":"shadow_weight","round":"R9","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_low_MFE_not_operating_leverage_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"126640 and 013870 show low MFE should not be used as operating-leverage validation unless fresh customer volume and margin evidence are repaired."}
```

## 11. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - small_autoparts_rebound_overcredit
  - low_MFE_volume_bridge_missing
  - OEM_customer_volume_bridge_missing
  - margin_cash_bridge_missing
new_axis_proposed:
  - C29_OEM_volume_mix_margin_cash_bridge_required_shadow_only
  - C29_small_autoparts_component_rebound_local_4B_guard_shadow_only
  - C29_low_MFE_not_operating_leverage_validation_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C29
  - full_4b_requires_non_price_evidence within C29
  - hard_4c_thesis_break_routes_to_4c within C29
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 12. Data-quality caveat

All selected triggers use Stock-Web tradable raw OHLC rows and clean selected 2024 entry windows.  
`126640` has a historical SPAC/name-transition candidate long before the selected window; `092780` has a 2025 name change outside the selected 2024 window. Both are usable for this 2024 price-path residual analysis.  
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
promotion should prefer hold / data-quality repair until exact URLs are added
```

## 13. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this MD through run-v12-calibration.
2. Confirm all trigger rows validate with:
   - price_data_source=Songdaiki/stock-web
   - price_basis=tradable_raw
   - price_adjustment_status=raw_unadjusted_marcap
3. Confirm R9 / L3 / C29 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C29 top-covered symbols
   - previous R9 loop84 symbols
   - previous R9 loop85 symbols
   - previous R9 loop86 symbols
   - previous R9 loop87 symbols
   - previous R9 loop88 symbols
   - previous R9 loop89 symbols
   - earlier known C29 symbols listed in this MD
6. Confirm accidentally generated R8/C27 file is not ingested as this request’s scheduled output.
7. If aggregate support remains stable after exact evidence URL repair, consider C29-scoped safe patch candidates:
   - C29_OEM_volume_mix_margin_cash_bridge_required
   - C29_small_autoparts_component_rebound_local_4B_guard
   - C29_low_MFE_not_operating_leverage_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R9
completed_loop = 90
next_round = R10
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.
```

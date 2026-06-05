# E2R Stock-Web v12 Residual Research — R9 Loop 89 / L3 / C29

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R9
loop: 89
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_MOTOR_PARTS_VOLUME_MIX_CASH_BRIDGE_VS_SMALL_AUTOPARTS_EV_THEME_REBOUND_DECAY
sector: mobility / auto parts / EV electronics / motor / volume / margin / operating leverage
output_file: e2r_stock_web_v12_residual_round_R9_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R8 loop 89`.

```text
scheduled_round = R9
scheduled_loop = 89
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

R9 is the mobility / auto-parts / EV operating-leverage lane.  
C29 remains the target because the No-Repeat Index shows it already has many rows but still carries false-positive risk around mobility theme rebounds that do not prove customer volume, utilization, margin or cash conversion.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
rows = 60
symbols = 27
good/bad Stage2 = 26/13
4B/4C = 6/0
top-covered = 011210, 000270, 005380, 005850, 010690, 018880
```

This loop avoids top-covered symbols and previous C29 loop sets:

```text
R9 loop88: 200880, 092200, 123040
R9 loop87: 004490, 009900, 024900
R9 loop86: 073240, 118990, 090080
R9 loop85: 000120, 003620, 215360
R9 loop84: 086280, 161390, 271940
earlier known C29: 012330, 002350, 204320
```

Selected symbols:

```text
064960, 067570, 012860
```

This loop tests:

```text
auto motor/parts customer volume + mix + cash bridge
vs
small auto interior/NVH late rebound without fresh OEM volume or margin bridge
vs
EV electronics / auto-parts price spike without durable orderbook, margin or cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"064960","company_name":"SNT모티브","profile_path":"atlas/symbol_profiles/064/064960.json","first_date":"2002-03-11","last_date":"2026-02-20","trading_day_count":5911,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2002-12-24","2012-12-26","2025-01-24","2025-02-26"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical and future corporate-action candidates are outside selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; 2025_candidates_outside_window"}
{"row_type":"price_source_validation","symbol":"067570","company_name":"엔브이에이치코리아","profile_path":"atlas/symbol_profiles/067/067570.json","first_date":"2013-12-03","last_date":"2026-02-20","trading_day_count":2997,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2023-08-16"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"012860","company_name":"모베이스전자","profile_path":"atlas/symbol_profiles/012/012860.json","first_date":"1996-07-01","last_date":"2026-02-20","trading_day_count":6912,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1999-01-06","2002-04-29","2011-12-27","2020-01-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"064960","trigger_type":"Stage2-Actionable-AutoMotorPartsVolumeMixCashBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"067570","trigger_type":"Stage2-FalsePositive-NVHInteriorPartsReboundNoFreshOEMVolumeMarginBridge","entry_date":"2024-02-06","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"012860","trigger_type":"Stage2-FalsePositive-AutoElectronicsEVThemeSpikeNoDurableOrderMarginBridge","entry_date":"2024-02-05","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
```

## 4. Research question

C29 is not “자동차 부품주가 움직였다.”  
The useful signal must prove the mechanical chain from price to operations:

```text
fresh OEM/customer volume
global model exposure
EV or motor program visibility
utilization
mix improvement
pricing
margin expansion
working-capital discipline
cash conversion
```

A theme spike without that bridge is an engine revving in neutral: sound exists, torque to the wheel does not.

Residual question:

```text
Can C29 distinguish:
1. stable auto motor/parts volume-mix-cash bridge with positive but still Green-strict rerating,
2. small auto interior/NVH rebound where later price spikes do not prove fresh OEM volume or margin conversion,
3. EV electronics price spike where initial MFE exists but durable orderbook, margin and cash bridge are missing?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C29_R9L89_064960_SNT_MOTIVE_VOLUME_MIX_CASH","symbol":"064960","company_name":"SNT모티브","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_MOTOR_PARTS_VOLUME_MIX_CASH_BRIDGE","case_type":"watch_positive_control","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-AutoMotorPartsVolumeMixCashBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_moderate_MFE_low_MAE_stability_case","current_profile_verdict":"current_profile_correct_if_volume_mix_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Auto motor/parts volume-mix-cash proxy produced a moderate MFE path with controlled early MAE. This is a Yellow-watch positive-control, not a Green-loosening case."}
{"row_type":"case","case_id":"C29_R9L89_067570_NVH_INTERIOR_REBOUND","symbol":"067570","company_name":"엔브이에이치코리아","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"NVH_INTERIOR_PARTS_REBOUND_WITHOUT_FRESH_OEM_VOLUME_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-NVHInteriorPartsReboundNoFreshOEMVolumeMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_NVH_interior_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"NVH/interior auto-parts rebound had limited MFE and later deep MAE. The late December spike is not original-entry validation without fresh OEM volume and margin bridge."}
{"row_type":"case","case_id":"C29_R9L89_012860_MOBASE_AUTO_ELECTRONICS_SPIKE","symbol":"012860","company_name":"모베이스전자","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_ELECTRONICS_EV_THEME_SPIKE_WITHOUT_DURABLE_ORDER_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-AutoElectronicsEVThemeSpikeNoDurableOrderMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_local_MFE_but_deep_MAE_no_order_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_auto_electronics_price_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Auto electronics/EV theme spike had local MFE but later deep MAE. Without durable customer orderbook, volume, margin and cash bridge, MFE remains price-only evidence."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 064960 SNT모티브 — auto motor/parts volume-mix-cash bridge positive-control

Entry row: `2024-01-29 c=43700`.  
Observed path: high `2024-06-28 h=50300`, late low `2024-12-09 l=39700`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L89_C29_064960_20240129_STAGE2_AUTOMOTOR_VOLUME_MIX_CASH","case_id":"C29_R9L89_064960_SNT_MOTIVE_VOLUME_MIX_CASH","symbol":"064960","company_name":"SNT모티브","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_MOTOR_PARTS_VOLUME_MIX_CASH_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-AutoMotorPartsVolumeMixCashBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":43700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_auto_motor_parts_volume_mix_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; auto motor/parts customer volume, mix and cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["customer_volume_proxy","motor_or_auto_parts_program_proxy","mix_margin_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_OEM_volume_pending","program_mix_pending","utilization_margin_pending","cash_conversion_pending"],"stage4b_evidence_fields":["moderate_MFE_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064960/2024.csv","profile_path":"atlas/symbol_profiles/064/064960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.21,"MFE_90D_pct":15.10,"MFE_180D_pct":15.10,"MAE_30D_pct":-1.26,"MAE_90D_pct":-1.26,"MAE_180D_pct":-9.15,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":50300.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":39700.0,"drawdown_after_peak_pct":-21.07,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"watch_positive_not_Green; Green requires exact OEM volume, mix, utilization, margin and cash evidence","four_b_evidence_type":["moderate_MFE_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_moderate_MFE_low_MAE_stability_case","current_profile_verdict":"current_profile_correct_if_volume_mix_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"2024_window_clean; 2025_candidates_outside_window","same_entry_group_id":"064960_2024-01-29_43700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 can allow Stage2/Yellow when mobility strength is tied to OEM/customer volume, program mix, utilization, margin and cash conversion. This row supports bridge discipline, not Green loosening."}
```

### 6.2 067570 엔브이에이치코리아 — NVH/interior parts rebound without fresh OEM volume/margin bridge

Entry row: `2024-02-06 c=2595`.  
Observed path: high `2024-02-06 h=2895`, later lows near `2024-11-13 l=2145`, followed by a late December spike that should not validate the original weak entry.

```jsonl
{"row_type":"trigger","trigger_id":"R9L89_C29_067570_20240206_STAGE2_FALSE_POSITIVE_NVH_REBOUND","case_id":"C29_R9L89_067570_NVH_INTERIOR_REBOUND","symbol":"067570","company_name":"엔브이에이치코리아","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"NVH_INTERIOR_PARTS_REBOUND_WITHOUT_FRESH_OEM_VOLUME_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-NVHInteriorPartsReboundNoFreshOEMVolumeMarginBridge","trigger_date":"2024-02-06","entry_date":"2024-02-06","entry_price":2595.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_auto_interior_NVH_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; NVH/interior auto-parts rebound treated as insufficient without fresh OEM volume, utilization, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["auto_parts_rebound","NVH_interior_keyword","relative_strength_spike"],"stage3_evidence_fields":["fresh_OEM_volume_missing","utilization_bridge_missing","margin_cash_bridge_missing","program_mix_missing"],"stage4b_evidence_fields":["price_only_local_peak","late_spike_not_entry_validation","volume_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067570/2024.csv","profile_path":"atlas/symbol_profiles/067/067570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.56,"MFE_90D_pct":11.56,"MFE_180D_pct":11.56,"MAE_30D_pct":-6.74,"MAE_90D_pct":-17.34,"MAE_180D_pct":-17.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-06","peak_price":2895.0,"max_drawdown_low_date":"2024-11-13","max_drawdown_low":2145.0,"drawdown_after_peak_pct":-25.91,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"NVH_interior_rebound_without_fresh_OEM_volume_margin_bridge_should_remain_4B_watch; late_December_spike_not_entry_validation","four_b_evidence_type":["price_only","late_spike_not_entry_validation","volume_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_late_spike_not_validation","current_profile_verdict":"current_profile_false_positive_if_NVH_interior_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"2024_window_clean","same_entry_group_id":"067570_2024-02-06_2595","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not promote NVH/interior auto-parts rebound without fresh OEM volume, utilization, program mix, margin and cash bridge. Late spike after deep drawdown should not validate the original entry."}
```

### 6.3 012860 모베이스전자 — auto electronics / EV theme spike without durable order-margin bridge

Entry row: `2024-02-05 c=2100`.  
Observed path: same-day high `2024-02-05 h=2390`, then deep low `2024-12-09 l=1285`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L89_C29_012860_20240205_STAGE2_FALSE_POSITIVE_AUTO_ELECTRONICS_SPIKE","case_id":"C29_R9L89_012860_MOBASE_AUTO_ELECTRONICS_SPIKE","symbol":"012860","company_name":"모베이스전자","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_ELECTRONICS_EV_THEME_SPIKE_WITHOUT_DURABLE_ORDER_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate;price_only_blowoff_stress_test","trigger_type":"Stage2-FalsePositive-AutoElectronicsEVThemeSpikeNoDurableOrderMarginBridge","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":2100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_auto_electronics_EV_theme_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; auto electronics/EV theme spike treated as insufficient without durable orderbook, OEM volume, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["auto_electronics_theme_spike","EV_parts_keyword","relative_strength_spike"],"stage3_evidence_fields":["durable_orderbook_missing","fresh_OEM_volume_missing","margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_MFE","order_margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012860/2024.csv","profile_path":"atlas/symbol_profiles/012/012860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.81,"MFE_90D_pct":13.81,"MFE_180D_pct":13.81,"MAE_30D_pct":-10.24,"MAE_90D_pct":-15.24,"MAE_180D_pct":-38.81,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":2390.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1285.0,"drawdown_after_peak_pct":-46.23,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"auto_electronics_EV_theme_spike_without_durable_order_margin_bridge_should_be_4B_watch_not_positive_even_with_local_MFE","four_b_evidence_type":["price_only","order_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_local_MFE_but_deep_MAE_no_order_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_auto_electronics_price_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"2024_window_clean","same_entry_group_id":"012860_2024-02-05_2100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not count EV auto-electronics local MFE as volume/margin evidence. Durable orderbook, OEM volume, margin and cash bridge must be repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L89_064960_SNT_MOTIVE_VOLUME_MIX_CASH","trigger_id":"R9L89_C29_064960_20240129_STAGE2_AUTOMOTOR_VOLUME_MIX_CASH","symbol":"064960","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C29 requires OEM volume, program mix, utilization, margin and cash bridge rather than mobility label alone","raw_component_scores_before":{"customer_volume_score":10,"program_mix_score":10,"operating_leverage_score":9,"utilization_score":8,"margin_bridge_score":8,"cash_conversion_score":7,"relative_strength_score":8,"valuation_repricing_score":5,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_before":63,"stage_label_before":"Stage2-Watch/Yellow-candidate","raw_component_scores_after":{"customer_volume_score":13,"program_mix_score":13,"operating_leverage_score":11,"utilization_score":10,"margin_bridge_score":10,"cash_conversion_score":9,"relative_strength_score":9,"valuation_repricing_score":6,"execution_risk_score":-3,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable/Stage3-Yellow-Watch","component_delta_explanation":"Moderate MFE plus low MAE supports Yellow-watch only when OEM volume/mix/margin/cash bridge exists; not enough for Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L89_067570_NVH_INTERIOR_REBOUND","trigger_id":"R9L89_C29_067570_20240206_STAGE2_FALSE_POSITIVE_NVH_REBOUND","symbol":"067570","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"NVH/interior rebound without fresh OEM volume and margin bridge should be blocked","raw_component_scores_before":{"customer_volume_score":2,"program_mix_score":1,"operating_leverage_score":1,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":9,"valuation_repricing_score":3,"execution_risk_score":-12,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_volume_score":0,"program_mix_score":0,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-20,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and later drawdown make this a missing OEM-volume/margin bridge failure; late spike is not entry validation."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L89_012860_MOBASE_AUTO_ELECTRONICS_SPIKE","trigger_id":"R9L89_C29_012860_20240205_STAGE2_FALSE_POSITIVE_AUTO_ELECTRONICS_SPIKE","symbol":"012860","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"auto electronics price-only EV theme spike without durable order/margin bridge should be 4B-watch","raw_component_scores_before":{"customer_volume_score":2,"program_mix_score":2,"operating_leverage_score":1,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":13,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_volume_score":0,"program_mix_score":0,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Local MFE is price-only; deep MAE and missing order/margin bridge block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R9L89_C29_P0_CURRENT","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C29 needs explicit OEM volume, program mix, utilization, margin, cash and late-spike validation taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":13.49,"avg_MAE90_pct":-11.28,"avg_MFE180_pct":13.49,"avg_MAE180_pct":-21.77,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.67,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C29_volume_mix_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R9L89_C29_P1_SECTOR_SPECIFIC","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P1_L3_mobility_volume_mix_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 mobility signals need customer volume, program mix, utilization, operating leverage, margin or cash conversion before Stage2-Actionable","changed_axes":["customer_volume_required","program_mix_margin_required","small_autoparts_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_volume_program_mix_utilization_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":13.49,"avg_MAE90_pct":-11.28,"avg_MFE180_pct":13.49,"avg_MAE180_pct":-21.77,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R9L89_C29_P2_CANONICAL","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P2_C29_volume_mix_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C29 should reward operating-leverage mechanics, not EV electronics / small auto-parts theme labels","changed_axes":["C29_volume_mix_margin_cash_bridge_required","C29_small_autoparts_EV_theme_local_4B_guard","C29_late_spike_not_entry_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_volume_or_orderbook_plus_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":13.49,"avg_MAE90_pct":-11.28,"avg_MFE180_pct":13.49,"avg_MAE180_pct":-21.77,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R9L89_C29_P3_COUNTEREXAMPLE_GUARD","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P3_C29_price_only_MFE_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If bridge is missing and MAE180<=-25, route to 4B-watch; if MFE90<15 and bridge is missing, do not count local MFE as positive evidence","changed_axes":["C29_price_only_MFE_guardrail","C29_late_spike_not_validation"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_MAE180_le_minus_25; no_positive_credit_if_MFE90_lt_15_and_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":13.49,"avg_MAE90_pct":-11.28,"avg_MFE180_pct":13.49,"avg_MAE180_pct":-21.77,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_MOTOR_POSITIVE_VS_SMALL_AUTOPARTS_EV_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":13.49,"avg_MAE90_pct":-11.28,"avg_MFE180_pct":13.49,"avg_MAE180_pct":-21.77,"stage2_hit_rate_MFE90_ge_15":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"price_only_local_MFE_count":2,"interpretation":"C29 needs bridge discipline. SNT모티브 is a watch-positive volume/mix/cash case, while 엔브이에이치코리아 and 모베이스전자는 local MFE or later spikes should not be promoted without fresh OEM volume, program mix, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"064960","trigger_type":"Stage2-Actionable-AutoMotorPartsVolumeMixCashBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"watch_positive_moderate_MFE_low_MAE","stage2_to_180D_outcome":"positive_control_but_Green_strict","MFE90_ge_15":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow only when OEM volume, program mix, margin and cash bridge exists; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"067570","trigger_type":"Stage2-FalsePositive-NVHInteriorPartsReboundNoFreshOEMVolumeMarginBridge","entry_date":"2024-02-06","stage2_to_90D_outcome":"weak_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"failed_NVH_rebound_late_spike_not_validation","MFE90_ge_20":false,"MAE180_le_minus_20":false,"transition_note":"NVH/interior parts rebound without fresh OEM volume and margin bridge should stay Watch/4B-risk; late spike is not original-entry validation."}
{"row_type":"stage_transition_summary","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"012860","trigger_type":"Stage2-FalsePositive-AutoElectronicsEVThemeSpikeNoDurableOrderMarginBridge","entry_date":"2024-02-05","stage2_to_90D_outcome":"price_only_local_MFE_without_bridge","stage2_to_180D_outcome":"failed_auto_electronics_spike_deep_MAE","MFE90_ge_20":false,"MAE180_le_minus_25":true,"transition_note":"EV/auto-electronics local MFE without durable orderbook and margin bridge should be treated as 4B-watch, not positive evidence."}
{"row_type":"residual_contribution","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"small_autoparts_EV_theme_overcredit_without_fresh_OEM_volume_margin_cash_bridge","contribution":"Adds two C29 local 4B/Watch counterexamples against one auto motor/parts volume-mix-cash positive-control, avoiding C29 top-covered and prior C29 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_MOTOR_PARTS_VOLUME_MIX_CASH_BRIDGE_VS_SMALL_AUTOPARTS_EV_THEME_REBOUND_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C29 now has non-top-symbol auto motor/parts positive-control and two small auto-parts / EV-electronics weak-bridge counterexamples; next R9 loops should exact-URL repair OEM volume, program mix, orderbook, utilization, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_volume_mix_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"064960 is usable only when OEM volume/mix/cash bridge exists; 067570 and 012860 demonstrate that price-only small auto-parts spikes should not be promoted."}
{"row_type":"shadow_weight","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_small_autoparts_EV_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"NVH/interior and EV auto-electronics rows showed local MFE without durable non-price order/volume/margin evidence."}
{"row_type":"shadow_weight","round":"R9","loop":"89","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_late_spike_not_entry_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"067570 shows late spike should not retroactively validate the original weak entry unless fresh OEM volume and margin evidence is repaired."}
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
  - small_autoparts_theme_overcredit
  - EV_auto_electronics_spike_overcredit
  - fresh_OEM_volume_bridge_missing
  - orderbook_margin_cash_bridge_missing
new_axis_proposed:
  - C29_volume_mix_margin_cash_bridge_required_shadow_only
  - C29_small_autoparts_EV_theme_local_4B_watch_guard_shadow_only
  - C29_late_spike_not_entry_validation_guard_shadow_only
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
The non-price evidence layer remains source-name/proxy level.

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
   - previous R9 loop88 symbols
   - previous R9 loop87 symbols
   - previous R9 loop86 symbols
   - previous R9 loop85 symbols
   - previous R9 loop84 symbols
   - earlier known C29 symbols listed in this MD
6. If aggregate support remains stable after exact evidence URL repair, consider C29-scoped safe patch candidates:
   - C29_volume_mix_margin_cash_bridge_required
   - C29_small_autoparts_EV_theme_local_4B_watch_guard
   - C29_late_spike_not_entry_validation_guard
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R9
completed_loop = 89
next_round = R10
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 watch-positive control, 2 counterexamples, and 2 local 4B-watch rows for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.
```

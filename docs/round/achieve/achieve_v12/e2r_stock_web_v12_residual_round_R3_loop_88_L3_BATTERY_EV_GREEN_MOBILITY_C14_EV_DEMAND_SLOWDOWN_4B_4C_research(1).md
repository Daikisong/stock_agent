# E2R Stock-Web v12 Residual Research — R3 Loop 88 / L3 / C14

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 88
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: ELECTROLYTE_AND_COPPERFOIL_DEMAND_SLOWDOWN_4B_PROTECTION_VS_BATTERY_EQUIPMENT_THEME_REBOUND_DECAY
sector: battery / EV / green mobility / demand slowdown / 4B-4C risk protection
output_file: e2r_stock_web_v12_residual_round_R3_loop_88_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R2 loop 88`.

```text
scheduled_round = R3
scheduled_loop = 88
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
```

R3 is restricted to battery / EV / green mobility.  
C14 is selected because recent R3 loops already covered:

```text
R3 loop85: C11_BATTERY_ORDERBOOK_RERATING
R3 loop86: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
R3 loop87: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

C14 is a risk-protection archetype, not a normal “buy signal” archetype.  
The No-Repeat Index snapshot shows:

```text
C14_EV_DEMAND_SLOWDOWN_4B_4C
rows = 21
symbols = 14
good/bad Stage2 = 3/3
4B/4C = 6/4
top-covered = 006400, 373220, 095500, 247540, 278280, 003670
```

This loop avoids those top-covered symbols and also avoids the recent R3 loop85/86/87 symbols:

```text
R3 loop85 C11: 078600, 247540, 393890
R3 loop86 C12: 317330, 066970, 361610
R3 loop87 C13: 096770, 011790, 051910
```

Selected symbols:

```text
093370, 336370, 382840
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"093370","company_name":"후성","profile_path":"atlas/symbol_profiles/093/093370.json","first_date":"2006-12-22","last_date":"2026-02-20","trading_day_count":4723,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"336370","company_name":"솔루스첨단소재","profile_path":"atlas/symbol_profiles/336/336370.json","first_date":"2019-10-18","last_date":"2026-02-20","trading_day_count":1557,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2024-01-08","2024-01-30"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist in January 2024. The selected entry is 2024-07-01 and avoids the candidate windows.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_entry_after_2024-01_candidates"}
{"row_type":"price_source_validation","symbol":"382840","company_name":"원준","profile_path":"atlas/symbol_profiles/382/382840.json","first_date":"2021-10-07","last_date":"2026-02-20","trading_day_count":1070,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2022-07-12","2022-07-29"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"093370","trigger_type":"4B-Protection-ElectrolyteDemandSlowdownDeepMAE-PositiveRiskCase","entry_date":"2024-01-26","duplicate_status":"new C14 symbol/trigger/date combination outside top-covered and recent R3 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"336370","trigger_type":"Stage2-FalsePositive-CopperFoilDemandSlowdownBlowoff-NoUtilizationCashBridge","entry_date":"2024-07-01","duplicate_status":"new C14 symbol/trigger/date combination outside top-covered and recent R3 loop sets; selected entry avoids January 2024 corporate-action candidate windows"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"382840","trigger_type":"Stage2-FalsePositive-BatteryEquipmentRebound-NoFreshOrderDemandBridge","entry_date":"2024-03-12","duplicate_status":"new C14 symbol/trigger/date combination outside top-covered and recent R3 loop sets"}
```

## 4. Research question

C14 is a risk gate. It should not ask “is EV/battery theme alive?” first.  
It should ask whether the bridge under the theme is still carrying weight: EV demand, OEM call-off, utilization, customer inventory, ASP, spread, subsidy or policy demand pull, margin, and cash conversion. When that bridge is missing, every rebound is like a battery cell with surface voltage but no capacity; it lights the meter, then collapses under load.

Residual question:

```text
Can C14 distinguish:
1. demand-slowdown protection success where 4B/Watch would save the model from deep MAE,
2. copper-foil / battery-material price blowoff that looks tradable but has no utilization or cash bridge,
3. battery-equipment rebound that lacks fresh order and demand bridge and decays into deep MAE?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C14_R3L88_093370_FOOSUNG_ELECTROLYTE_DEMAND_SLOWDOWN","symbol":"093370","company_name":"후성","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"ELECTROLYTE_DEMAND_SLOWDOWN_4B_PROTECTION","case_type":"risk_protection_success","positive_or_counterexample":"positive_risk_case","best_trigger":"4B-Protection-ElectrolyteDemandSlowdownDeepMAE-PositiveRiskCase","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"risk_positive_low_MFE_deep_MAE_correct_4B","current_profile_verdict":"current_profile_correct_if_C14_blocks_Yellow_Green_under_demand_slowdown","price_source":"Songdaiki/stock-web","notes":"Electrolyte/material demand slowdown row produced low MFE and deep forward MAE. This is a positive case for risk protection, not a buy-positive case."}
{"row_type":"case","case_id":"C14_R3L88_336370_SOLUS_COPPERFOIL_DEMAND_BLOWOFF","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"COPPERFOIL_DEMAND_SLOWDOWN_PRICE_BLOWOFF_WITHOUT_UTILIZATION_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CopperFoilDemandSlowdownBlowoff-NoUtilizationCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_only_blowoff_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_copperfoil_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Late copper-foil/battery-material blowoff had almost no MFE from the selected entry and collapsed without utilization, customer call-off, margin or cash bridge."}
{"row_type":"case","case_id":"C14_R3L88_382840_WONIK_BATTERY_EQUIPMENT_REBOUND","symbol":"382840","company_name":"원준","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_EQUIPMENT_REBOUND_WITHOUT_FRESH_ORDER_DEMAND_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-BatteryEquipmentRebound-NoFreshOrderDemandBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_without_order_bridge","current_profile_verdict":"current_profile_false_positive_if_battery_equipment_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Battery-equipment rebound had low MFE and deep MAE when fresh order, utilization and demand bridge failed to confirm."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 093370 후성 — electrolyte/material demand slowdown risk-protection success

Entry row: `2024-01-26 c=8640`.  
Observed path: 30D/90D high `2024-02-16 h=9240`, 90D low around `2024-05-23 l=6900`, and later low `2024-12-09 l=4605`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L88_C14_093370_20240126_4B_ELECTROLYTE_DEMAND_SLOWDOWN","case_id":"C14_R3L88_093370_FOOSUNG_ELECTROLYTE_DEMAND_SLOWDOWN","symbol":"093370","company_name":"후성","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"ELECTROLYTE_DEMAND_SLOWDOWN_4B_PROTECTION","loop_objective":"risk_protection_validation;4B_4C_guardrail_stress_test;canonical_archetype_rule_candidate","trigger_type":"4B-Protection-ElectrolyteDemandSlowdownDeepMAE-PositiveRiskCase","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":8640.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_electrolyte_demand_slowdown_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; electrolyte/material demand slowdown and inventory/spread pressure treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["EV_demand_slowdown_proxy","electrolyte_spread_pressure_proxy","inventory_destocking_proxy"],"stage3_evidence_fields":["OEM_calloff_recovery_missing","utilization_recovery_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE_watch","deep_MAE_watch","demand_slowdown_bridge_present"],"stage4c_evidence_fields":["structural_demand_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv","profile_path":"atlas/symbol_profiles/093/093370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.94,"MFE_90D_pct":6.94,"MFE_180D_pct":6.94,"MAE_30D_pct":-5.67,"MAE_90D_pct":-20.14,"MAE_180D_pct":-46.70,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-16","peak_price":9240.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":4605.0,"drawdown_after_peak_pct":-50.16,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"correct_4B_protection; low MFE and deep MAE validate blocking Yellow/Green under EV demand slowdown","four_b_evidence_type":["demand_slowdown_proxy","low_MFE","deep_MAE"],"four_c_protection_label":"4C_watch_only_if_OEM_calloff_and_margin_bridge_break_confirmed","trigger_outcome_label":"risk_positive_low_MFE_deep_MAE_correct_4B","current_profile_verdict":"current_profile_correct_if_C14_blocks_Yellow_Green_under_demand_slowdown","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"093370_2024-01-26_8640","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C14 should preserve this as a 4B/Watch protection success. It is not a positive buy signal; it is evidence that demand slowdown plus missing utilization/margin bridge should block Yellow/Green."}
```

### 6.2 336370 솔루스첨단소재 — copper-foil/battery-material price blowoff without utilization/cash bridge

Entry row: `2024-07-01 c=23050`.  
Observed path: same-day high `2024-07-01 h=23500`, then lows `2024-07-18 l=16790`, `2024-09-24 l=12240`, and `2024-12-09 l=7650`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L88_C14_336370_20240701_STAGE2_FALSE_POSITIVE_COPPERFOIL_BLOWOFF","case_id":"C14_R3L88_336370_SOLUS_COPPERFOIL_DEMAND_BLOWOFF","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"COPPERFOIL_DEMAND_SLOWDOWN_PRICE_BLOWOFF_WITHOUT_UTILIZATION_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-CopperFoilDemandSlowdownBlowoff-NoUtilizationCashBridge","trigger_date":"2024-07-01","entry_date":"2024-07-01","entry_price":23050.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_copperfoil_battery_material_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; copper-foil/material price spike treated as insufficient without utilization recovery, customer call-off, spread/margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["copperfoil_price_spike","battery_material_rebound_theme"],"stage3_evidence_fields":["utilization_recovery_missing","customer_calloff_missing","spread_margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","demand_slowdown_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv","profile_path":"atlas/symbol_profiles/336/336370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.95,"MFE_90D_pct":1.95,"MFE_180D_pct":1.95,"MAE_30D_pct":-27.16,"MAE_90D_pct":-46.90,"MAE_180D_pct":-66.81,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-01","peak_price":23500.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":7650.0,"drawdown_after_peak_pct":-67.45,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"copperfoil_price_blowoff_without_utilization_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","utilization_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_only_blowoff_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_copperfoil_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"selected_entry_after_2024-01-08_and_2024-01-30_candidates","same_entry_group_id":"336370_2024-07-01_23050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C14 should route copper-foil/battery-material price blowoff to 4B-watch when utilization, customer call-off, margin and cash bridge are missing. The path has almost no MFE and severe MAE."}
```

### 6.3 382840 원준 — battery-equipment rebound without fresh order/demand bridge

Entry row: `2024-03-12 c=20050`.  
Observed path: same-day high `2024-03-12 h=20650`, 30D low around `2024-04-12 l=15920`, and later low `2024-12-09 l=8750`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L88_C14_382840_20240312_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_REBOUND","case_id":"C14_R3L88_382840_WONIK_BATTERY_EQUIPMENT_REBOUND","symbol":"382840","company_name":"원준","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_EQUIPMENT_REBOUND_WITHOUT_FRESH_ORDER_DEMAND_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-BatteryEquipmentRebound-NoFreshOrderDemandBridge","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":20050.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_equipment_rebound_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; battery-equipment rebound treated as insufficient without fresh order, customer capex restart, utilization and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["battery_equipment_rebound","relative_strength_rebound"],"stage3_evidence_fields":["fresh_order_bridge_missing","customer_capex_restart_missing","utilization_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE_watch","fresh_order_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/382/382840/2024.csv","profile_path":"atlas/symbol_profiles/382/382840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.99,"MFE_90D_pct":2.99,"MFE_180D_pct":2.99,"MAE_30D_pct":-20.60,"MAE_90D_pct":-43.64,"MAE_180D_pct":-56.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-12","peak_price":20650.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":8750.0,"drawdown_after_peak_pct":-57.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"battery_equipment_rebound_without_fresh_order_demand_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","fresh_order_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_without_order_bridge","current_profile_verdict":"current_profile_false_positive_if_battery_equipment_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"382840_2024-03-12_20050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C14 should not promote battery-equipment rebounds without fresh order, customer capex restart, utilization and margin/cash bridge. Low MFE and deep MAE require 4B-watch routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C14_R3L88_093370_FOOSUNG_ELECTROLYTE_DEMAND_SLOWDOWN","trigger_id":"R3L88_C14_093370_20240126_4B_ELECTROLYTE_DEMAND_SLOWDOWN","symbol":"093370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_scope":"current_default_proxy","profile_hypothesis":"current profile is correct if C14 blocks Yellow/Green when EV demand, inventory, utilization and margin bridge are weak","raw_component_scores_before":{"EV_demand_recovery_score":1,"OEM_calloff_score":0,"utilization_score":0,"inventory_destocking_score":-12,"spread_margin_score":-10,"cash_conversion_score":-5,"relative_strength_score":2,"valuation_repricing_score":1,"4B_risk_score":18,"4C_risk_score":8,"information_confidence":5},"weighted_score_before":0,"stage_label_before":"4B-Watch/Protection","raw_component_scores_after":{"EV_demand_recovery_score":0,"OEM_calloff_score":0,"utilization_score":0,"inventory_destocking_score":-16,"spread_margin_score":-14,"cash_conversion_score":-7,"relative_strength_score":1,"valuation_repricing_score":0,"4B_risk_score":22,"4C_risk_score":10,"information_confidence":6},"weighted_score_after":0,"stage_label_after":"4B-Watch/4C-Watch","component_delta_explanation":"This is a correct risk-protection case. Low MFE and deep MAE confirm that Stage2/Yellow/Green should be blocked."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C14_R3L88_336370_SOLUS_COPPERFOIL_DEMAND_BLOWOFF","trigger_id":"R3L88_C14_336370_20240701_STAGE2_FALSE_POSITIVE_COPPERFOIL_BLOWOFF","symbol":"336370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_scope":"current_default_proxy","profile_hypothesis":"copper-foil/battery-material blowoff without utilization and margin bridge should be 4B-watch","raw_component_scores_before":{"EV_demand_recovery_score":2,"OEM_calloff_score":0,"utilization_score":0,"inventory_destocking_score":-10,"spread_margin_score":-8,"cash_conversion_score":-5,"relative_strength_score":10,"valuation_repricing_score":4,"4B_risk_score":16,"4C_risk_score":6,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"EV_demand_recovery_score":0,"OEM_calloff_score":0,"utilization_score":0,"inventory_destocking_score":-16,"spread_margin_score":-14,"cash_conversion_score":-8,"relative_strength_score":2,"valuation_repricing_score":0,"4B_risk_score":24,"4C_risk_score":10,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Almost no MFE and severe MAE convert the copper-foil rebound into missing utilization/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C14_R3L88_382840_WONIK_BATTERY_EQUIPMENT_REBOUND","trigger_id":"R3L88_C14_382840_20240312_STAGE2_FALSE_POSITIVE_BATTERY_EQUIPMENT_REBOUND","symbol":"382840","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_scope":"current_default_proxy","profile_hypothesis":"battery-equipment rebound without fresh order and demand bridge should remain Watch/blocked","raw_component_scores_before":{"EV_demand_recovery_score":2,"OEM_calloff_score":1,"utilization_score":0,"inventory_destocking_score":-8,"spread_margin_score":-5,"cash_conversion_score":-4,"relative_strength_score":7,"valuation_repricing_score":3,"4B_risk_score":14,"4C_risk_score":4,"information_confidence":3},"weighted_score_before":8,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"EV_demand_recovery_score":0,"OEM_calloff_score":0,"utilization_score":0,"inventory_destocking_score":-14,"spread_margin_score":-10,"cash_conversion_score":-7,"relative_strength_score":2,"valuation_repricing_score":0,"4B_risk_score":22,"4C_risk_score":8,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE require fresh order/utilization/margin evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L88_C14_P0_CURRENT","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C14 needs explicit EV demand/call-off/utilization/margin slowdown gate and late rebound non-validation","eligible_trigger_count":3,"avg_MFE90_pct":3.96,"avg_MAE90_pct":-36.89,"avg_MFE180_pct":3.96,"avg_MAE180_pct":-56.62,"false_positive_rate":0.67,"risk_protection_success_count":1,"late_green_count":0,"avg_four_b_local_peak_proximity":0.67,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"C14_4B_guard_required"}
{"row_type":"profile_comparison","comparison_id":"R3L88_C14_P1_SECTOR_SPECIFIC","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_id":"P1_L3_EV_demand_slowdown_guard_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 battery/EV signals need demand recovery, OEM call-off, utilization recovery, margin/spread or cash bridge before Stage2-Actionable; otherwise 4B/4C risk should dominate","changed_axes":["EV_demand_recovery_required","OEM_calloff_required","utilization_margin_required","battery_theme_rebound_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_OEM_calloff_utilization_margin_cash_or_demand_recovery_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":3.96,"avg_MAE90_pct":-36.89,"avg_MFE180_pct":3.96,"avg_MAE180_pct":-56.62,"false_positive_rate":0.0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R3L88_C14_P2_CANONICAL","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_id":"P2_C14_EV_demand_4B_4C_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C14 should reward correct risk routing, not battery-theme rebounds","changed_axes":["C14_demand_slowdown_4B_required","C14_rebound_without_calloff_block","C14_deep_MAE_4C_watch_guard"],"changed_thresholds":{"block_yellow_gate":"MFE90_lt_10_or_MAE90_le_minus20_when_calloff_utilization_margin_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":3.96,"avg_MAE90_pct":-36.89,"avg_MFE180_pct":3.96,"avg_MAE180_pct":-56.62,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R3L88_C14_P3_COUNTEREXAMPLE_GUARD","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_id":"P3_C14_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-20 while demand/call-off/utilization bridge is missing, block Yellow/Green and route to 4B-watch; if 4C thesis break is confirmed, escalate to 4C-watch","changed_axes":["C14_low_MFE_guardrail","C14_high_MAE_4B_guardrail","C14_4C_watch_escalation"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_20_with_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":3.96,"avg_MAE90_pct":-36.89,"avg_MFE180_pct":3.96,"avg_MAE180_pct":-56.62,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_ELECTROLYTE_COPPERFOIL_EQUIPMENT_DEMAND_SLOWDOWN","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"risk_protection_success_count":1,"good_stage2_count":0,"bad_stage2_count":2,"4B_case_count":3,"4C_case_count":1,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":3.96,"avg_MAE90_pct":-36.89,"avg_MFE180_pct":3.96,"avg_MAE180_pct":-56.62,"stage2_bad_entry_rate_MFE90_lt_10":1.0,"stage2_bad_entry_rate_MAE90_le_minus_20":1.0,"interpretation":"C14 is a risk-protection archetype. 후성 validates correct 4B/4C-style protection, while 솔루스첨단소재 and 원준 show that battery-material/equipment rebounds should not be promoted without demand recovery, OEM call-off, utilization, margin and cash bridge."}
{"row_type":"stage_transition_summary","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"093370","trigger_type":"4B-Protection-ElectrolyteDemandSlowdownDeepMAE-PositiveRiskCase","entry_date":"2024-01-26","stage2_to_90D_outcome":"correct_4B_low_MFE_high_MAE","stage2_to_180D_outcome":"correct_risk_protection_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"This is positive evidence for blocking Yellow/Green, not a buy-positive case."}
{"row_type":"stage_transition_summary","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"336370","trigger_type":"Stage2-FalsePositive-CopperFoilDemandSlowdownBlowoff-NoUtilizationCashBridge","entry_date":"2024-07-01","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_copperfoil_rebound_extreme_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Copper-foil rebound without utilization/margin/cash bridge should stay 4B-watch."}
{"row_type":"stage_transition_summary","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"382840","trigger_type":"Stage2-FalsePositive-BatteryEquipmentRebound-NoFreshOrderDemandBridge","entry_date":"2024-03-12","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_battery_equipment_rebound_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Battery-equipment rebound without fresh order/demand bridge should remain 4B-watch."}
{"row_type":"residual_contribution","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","residual_type":"EV_battery_rebound_overcredit_without_demand_calloff_utilization_margin_bridge","contribution":"Adds one C14 protection-positive and two Stage2 false-positive risk cases, avoiding C14 top-covered symbols and recent R3 C11/C12/C13 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"ELECTROLYTE_AND_COPPERFOIL_DEMAND_SLOWDOWN_4B_PROTECTION_VS_BATTERY_EQUIPMENT_THEME_REBOUND_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":3,"4C_case_count":1,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C14 now has non-top-symbol electrolyte, copper-foil and battery-equipment risk rows; next R3 loops should exact-URL repair OEM call-off, demand recovery, utilization, inventory, spread/margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","axis":"C14_demand_calloff_utilization_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"All three rows had low MFE and deep MAE when demand recovery, OEM call-off, utilization, margin and cash bridge were missing."}
{"row_type":"shadow_weight","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","axis":"C14_rebound_without_bridge_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Battery-material/equipment rebounds should not become Yellow/Green unless exact demand and margin bridge is repaired."}
{"row_type":"shadow_weight","round":"R3","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","axis":"C14_low_MFE_deep_MAE_4C_watch_escalation","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-20 while demand/call-off/utilization bridge is missing, block Stage2-Actionable/Yellow; if thesis break is source-confirmed, escalate to 4C-watch."}
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
  - EV_battery_rebound_overcredit
  - demand_recovery_bridge_missing
  - OEM_calloff_bridge_missing
  - utilization_margin_cash_bridge_missing
new_axis_proposed:
  - C14_demand_calloff_utilization_bridge_required_shadow_only
  - C14_rebound_without_bridge_4B_watch_guard_shadow_only
  - C14_low_MFE_deep_MAE_4C_watch_escalation_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C14
  - full_4b_requires_non_price_evidence within C14
  - hard_4c_thesis_break_routes_to_4c within C14
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

All selected triggers use actual Stock-Web tradable raw OHLC rows and clean selected forward windows.  
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
3. Confirm R3 / L3 / C14 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C14 top-covered symbols
   - previous R3 loop85 C11 symbols
   - previous R3 loop86 C12 symbols
   - previous R3 loop87 C13 symbols
6. Confirm that 336370 entry is after the January 2024 raw discontinuity candidates.
7. If aggregate support remains stable after exact evidence URL repair, consider C14-scoped safe patch candidates:
   - C14_demand_calloff_utilization_bridge_required
   - C14_rebound_without_bridge_4B_watch_guard
   - C14_low_MFE_deep_MAE_4C_watch_escalation
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R3
completed_loop = 88
next_round = R4
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 risk-protection positive, 2 counterexamples, 3 local 4B-watch rows, and 1 4C-watch escalation candidate for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.
```

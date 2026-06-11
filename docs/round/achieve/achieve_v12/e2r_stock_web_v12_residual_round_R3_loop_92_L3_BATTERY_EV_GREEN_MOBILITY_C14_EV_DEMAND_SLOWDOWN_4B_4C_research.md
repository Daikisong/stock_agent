# E2R Stock-Web v12 Residual Research — R3 Loop 92 / L3 / C14

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 92
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: EV_DEMAND_SLOWDOWN_VALID_4B_GUARD_VS_PRECURSOR_RAMP_FALSE_OVERBLOCK
sector: battery / EV / demand slowdown / capex delay / aluminum foil / battery equipment / precursor
output_file: e2r_stock_web_v12_residual_round_R3_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R2 loop 92`.

```text
scheduled_round = R3
scheduled_loop = 92
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
```

R3 is restricted to battery / EV / green mobility.
C14 is selected because the recent R3 sequence rotated:

```text
R3 loop85 C11
R3 loop86 C12
R3 loop87 C13
R3 loop88 C14
R3 loop89 C11
R3 loop90 C12
R3 loop91 C13
```

Therefore loop92 returns to `C14_EV_DEMAND_SLOWDOWN_4B_4C`.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C14_EV_DEMAND_SLOWDOWN_4B_4C
rows = 21
symbols = 14
good/bad Stage2 = 3/3
4B/4C = 6/4
top-covered = 006400, 373220, 095500, 247540, 278280, 003670
```

This loop avoids the C14 top-covered list and recent R3 loop symbols:

```text
R3 loop85 C11: 078600, 247540, 393890
R3 loop86 C12: 317330, 066970, 361610
R3 loop87 C13: 096770, 011790, 051910
R3 loop88 C14: 093370, 336370, 382840
R3 loop89 C11: 222080, 290670, 089980
R3 loop90 C12: 114190, 450080, 417200
R3 loop91 C13: 036830, 014820, 095500
```

Candidate hygiene note:

```text
During this execution path, stale R1/C02 and R2/C08 candidate rows were touched while checking alternatives.
Those rows are not used in this R3/C14 output.
```

Selected symbols:

```text
006110, 101360, 282880
```

The selected pocket is:

```text
EV-demand slowdown valid 4B guard
vs
battery precursor/customer-capacity ramp that should not be overblocked by broad EV slowdown vocabulary
vs
battery equipment/capex-delay valid 4B guard
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"006110","company_name":"삼아알미늄","profile_path":"atlas/symbol_profiles/006/006110.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7041,"corporate_action_candidate_count":16,"corporate_action_candidate_dates":["1998-07-15","1998-07-17","1998-09-03","1998-09-28","2000-06-29","2002-10-15","2003-01-08","2004-06-21","2005-05-04","2006-01-06","2006-08-16","2015-08-31","2020-06-15","2020-07-09","2020-07-27","2023-01-16"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"101360","company_name":"에코앤드림","profile_path":"atlas/symbol_profiles/101/101360.json","first_date":"2013-07-01","last_date":"2026-02-20","trading_day_count":2485,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2020-07-30","2024-08-01"],"has_major_raw_discontinuity":true,"calibration_caveat":"2024-08-01 corporate-action candidate occurs after selected entry; keep data-quality watch before production patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_entry_before_2024-08-01_candidate; data_quality_watch"}
{"row_type":"price_source_validation","symbol":"282880","company_name":"코윈테크","profile_path":"atlas/symbol_profiles/282/282880.json","first_date":"2019-08-05","last_date":"2026-02-20","trading_day_count":1606,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"006110","trigger_type":"Stage2-4B-Validated-EVAluminumFoilDemandSlowdownGuard","entry_date":"2024-01-02","duplicate_status":"new C14 symbol/trigger/date combination outside top-covered and previous R3 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"101360","trigger_type":"Stage2-FalsePositive-OverbroadEVDemandSlowdownWouldMissPrecursorRamp","entry_date":"2024-01-11","duplicate_status":"new C14 symbol/trigger/date combination outside top-covered and previous R3 loop symbols; data-quality watch due 2024-08-01 candidate"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"282880","trigger_type":"Stage2-4B-Validated-BatteryEquipmentCapexDelayDemandSlowdownGuard","entry_date":"2024-01-02","duplicate_status":"new C14 symbol/trigger/date combination outside top-covered and previous R3 loop symbols"}
```

## 4. Research question

C14 is not “배터리주가 빠졌다.”
The useful C14 guard must prove the slowdown chain:

```text
EV demand slowdown or inventory correction
customer call-off / capex delay
price pressure or ASP mix deterioration
utilization decline
order backlog quality deterioration
margin compression
working-capital drag
cash conversion pressure
```

But C14 must not become a blanket “battery = bad” filter.
A demand-slowdown alarm is like a circuit breaker. It is valuable when the line is overheating, but if it trips the whole factory while one clean production line is ramping, the guard itself becomes the error.

Residual question:

```text
Can C14 distinguish:
1. valid 4B risk where EV slowdown / capex delay led to low MFE and deep MAE,
2. false overblock where a precursor/customer-ramp bridge overcame broad EV-slowdown vocabulary,
3. valid 4B equipment/capex-delay risk where weak MFE and deep MAE confirmed the demand guard?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C14_R3L92_006110_SAM_A_ALUMINUM_FOIL_4B","symbol":"006110","company_name":"삼아알미늄","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_ALUMINUM_FOIL_DEMAND_SLOWDOWN_VALID_4B_GUARD","case_type":"validated_risk_guard","positive_or_counterexample":"positive_risk_guard","best_trigger":"Stage2-4B-Validated-EVAluminumFoilDemandSlowdownGuard","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"valid_4B_low_MFE_deep_MAE_EV_demand_slowdown_guard","current_profile_verdict":"current_profile_correct_if_demand_slowdown_calloff_margin_cash_drag_routes_to_4B","price_source":"Songdaiki/stock-web","notes":"Battery aluminum-foil demand slowdown / inventory correction guard was valid: MFE stayed weak while MAE expanded materially."}
{"row_type":"case","case_id":"C14_R3L92_101360_ECODREAM_PRECURSOR_RAMP_FALSE_OVERBLOCK","symbol":"101360","company_name":"에코앤드림","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"PRECURSOR_CUSTOMER_RAMP_FALSE_OVERBLOCK_BY_BROAD_EV_SLOWDOWN","case_type":"false_overblock","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-OverbroadEVDemandSlowdownWouldMissPrecursorRamp","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"counterexample_extreme_MFE_low_MAE_if_broad_slowdown_overblocked","current_profile_verdict":"current_profile_false_positive_if_EV_slowdown_guard_ignores_customer_capacity_ramp_bridge","price_source":"Songdaiki/stock-web","notes":"Precursor/customer-ramp bridge produced extreme MFE despite broad EV slowdown. This row warns against overbroad C14 blocking; data-quality watch remains due 2024-08-01 candidate."}
{"row_type":"case","case_id":"C14_R3L92_282880_COWINTECH_EQUIPMENT_CAPEX_DELAY_4B","symbol":"282880","company_name":"코윈테크","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_EQUIPMENT_CAPEX_DELAY_DEMAND_SLOWDOWN_VALID_4B_GUARD","case_type":"validated_risk_guard","positive_or_counterexample":"positive_risk_guard","best_trigger":"Stage2-4B-Validated-BatteryEquipmentCapexDelayDemandSlowdownGuard","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"valid_4B_low_MFE_deep_MAE_capex_delay_guard","current_profile_verdict":"current_profile_correct_if_capex_delay_backlog_margin_cash_drag_routes_to_4B","price_source":"Songdaiki/stock-web","notes":"Battery equipment/capex-delay vocabulary led to low MFE and large 180D drawdown, validating 4B risk routing."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 006110 삼아알미늄 — EV aluminum-foil demand slowdown valid 4B guard

Entry row: `2024-01-02 c=102900`.
Observed path: local high `2024-02-21 h=116400`, then persistent decline to `2024-09-24 l=46700` within the broad 180D review window and `2024-12-30 l=32600` full-year low.

```jsonl
{"row_type":"trigger","trigger_id":"R3L92_C14_006110_20240102_STAGE2_4B_EV_FOIL_SLOWDOWN","case_id":"C14_R3L92_006110_SAM_A_ALUMINUM_FOIL_4B","symbol":"006110","company_name":"삼아알미늄","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_ALUMINUM_FOIL_DEMAND_SLOWDOWN_VALID_4B_GUARD","loop_objective":"validated_risk_guard;4B_guardrail_stress_test;counterexample_balance","trigger_type":"Stage2-4B-Validated-EVAluminumFoilDemandSlowdownGuard","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":102900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_EV_demand_slowdown_inventory_correction_aluminum_foil_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; EV demand slowdown, battery foil inventory pressure, customer call-off, margin/cash drag treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["EV_demand_slowdown_proxy","inventory_correction_proxy","battery_foil_margin_pressure_proxy"],"stage3_evidence_fields":["customer_calloff_source_pending","utilization_decline_source_pending","ASP_margin_cash_bridge_pending"],"stage4b_evidence_fields":["low_MFE","deep_MAE","valid_4B_guard"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv","profile_path":"atlas/symbol_profiles/006/006110.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.13,"MFE_90D_pct":13.12,"MFE_180D_pct":13.12,"MAE_30D_pct":-22.06,"MAE_90D_pct":-28.28,"MAE_180D_pct":-54.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":116400.0,"max_drawdown_low_date":"2024-12-30","max_drawdown_low":32600.0,"drawdown_after_peak_pct":-71.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"valid_4B_guard_low_MFE_deep_MAE_EV_demand_slowdown_margin_cash_drag","four_b_evidence_type":["low_MFE","deep_MAE","valid_4B_guard"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"valid_4B_low_MFE_deep_MAE_EV_demand_slowdown_guard","current_profile_verdict":"current_profile_correct_if_demand_slowdown_calloff_margin_cash_drag_routes_to_4B","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"006110_2024-01-02_102900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C14 should hard-route EV demand slowdown / inventory correction / margin-cash drag rows to 4B when MFE is weak and MAE expands deeply."}
```

### 6.2 101360 에코앤드림 — precursor/customer-ramp bridge that should not be overblocked

Entry row: `2024-01-11 c=22800`.
Observed path: rapid high `2024-03-05 h=89900`, with entry-area low `2024-01-11 l=21000`. A 2024-08-01 corporate-action candidate remains outside the initial trigger but inside the year, so patch promotion requires repair.

```jsonl
{"row_type":"trigger","trigger_id":"R3L92_C14_101360_20240111_STAGE2_FALSE_OVERBLOCK_PRECURSOR_RAMP","case_id":"C14_R3L92_101360_ECODREAM_PRECURSOR_RAMP_FALSE_OVERBLOCK","symbol":"101360","company_name":"에코앤드림","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"PRECURSOR_CUSTOMER_RAMP_FALSE_OVERBLOCK_BY_BROAD_EV_SLOWDOWN","loop_objective":"false_overblock_mining;counterexample_mining;green_strictness_stress_test","trigger_type":"Stage2-FalsePositive-OverbroadEVDemandSlowdownWouldMissPrecursorRamp","trigger_date":"2024-01-11","entry_date":"2024-01-11","entry_price":22800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_precursor_customer_ramp_capacity_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; precursor/customer capacity ramp, order visibility and utilization bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["precursor_capacity_ramp_proxy","customer_order_or_offtake_proxy","utilization_ramp_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_offtake_source_pending","capacity_ramp_source_pending","margin_cash_bridge_pending","2024_CA_data_quality_repair_pending"],"stage4b_evidence_fields":["false_overblock_watch","data_quality_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/101/101360/2024.csv","profile_path":"atlas/symbol_profiles/101/101360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":255.26,"MFE_90D_pct":294.30,"MFE_180D_pct":294.30,"MAE_30D_pct":-7.89,"MAE_90D_pct":-7.89,"MAE_180D_pct":-7.89,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-05","peak_price":89900.0,"max_drawdown_low_date":"2024-12-30","max_drawdown_low":21400.0,"drawdown_after_peak_pct":-76.20,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.90,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"do_not_overblock_broad_EV_slowdown_if_customer_capacity_ramp_bridge_exists_but_Green_requires_exact_evidence_and_CA_repair","four_b_evidence_type":["false_overblock_watch","data_quality_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_extreme_MFE_low_MAE_if_broad_slowdown_overblocked","current_profile_verdict":"current_profile_false_positive_if_EV_slowdown_guard_ignores_customer_capacity_ramp_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["2024-08-01_corporate_action_candidate_after_entry_data_quality_watch"],"corporate_action_window_status":"selected_entry_before_2024-08-01_candidate; data_quality_watch","same_entry_group_id":"101360_2024-01-11_22800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"do_not_count_as_new_case":false,"current_profile_residual":"C14 must not become a blanket battery overblock. If a customer capacity-ramp / offtake / utilization bridge exists, broad EV-demand slowdown vocabulary should be overridden into evidence-repair rather than hard 4B."}
```

### 6.3 282880 코윈테크 — battery equipment / capex-delay demand slowdown valid 4B guard

Entry row: `2024-01-02 c=27750`.
Observed path: weak local high `2024-02-23 h=29450`, then long decline to `2024-09-24 l=14560` in the 180D review zone and `2024-12-09 l=11650` full-year low.

```jsonl
{"row_type":"trigger","trigger_id":"R3L92_C14_282880_20240102_STAGE2_4B_EQUIPMENT_CAPEX_DELAY","case_id":"C14_R3L92_282880_COWINTECH_EQUIPMENT_CAPEX_DELAY_4B","symbol":"282880","company_name":"코윈테크","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_EQUIPMENT_CAPEX_DELAY_DEMAND_SLOWDOWN_VALID_4B_GUARD","loop_objective":"validated_risk_guard;4B_guardrail_stress_test;canonical_archetype_rule_candidate","trigger_type":"Stage2-4B-Validated-BatteryEquipmentCapexDelayDemandSlowdownGuard","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":27750.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_equipment_capex_delay_order_slowdown_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; battery equipment capex delay, order conversion risk, backlog quality and margin/cash drag treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["battery_equipment_capex_delay_proxy","order_backlog_quality_risk_proxy","margin_cash_drag_proxy"],"stage3_evidence_fields":["customer_capex_delay_source_pending","backlog_conversion_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["low_MFE","deep_MAE","valid_4B_guard"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/282/282880/2024.csv","profile_path":"atlas/symbol_profiles/282/282880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.80,"MFE_90D_pct":6.13,"MFE_180D_pct":6.13,"MAE_30D_pct":-13.33,"MAE_90D_pct":-14.77,"MAE_180D_pct":-47.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-23","peak_price":29450.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":11650.0,"drawdown_after_peak_pct":-60.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.29,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"valid_4B_guard_low_MFE_deep_MAE_battery_equipment_capex_delay_order_slowdown","four_b_evidence_type":["low_MFE","deep_MAE","valid_4B_guard"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"valid_4B_low_MFE_deep_MAE_capex_delay_guard","current_profile_verdict":"current_profile_correct_if_capex_delay_backlog_margin_cash_drag_routes_to_4B","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"282880_2024-01-02_27750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C14 should hard-route battery equipment capex-delay / backlog-quality deterioration rows to 4B when local MFE is weak and MAE expands."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L92_006110_SAM_A_ALUMINUM_FOIL_4B","trigger_id":"R3L92_C14_006110_20240102_STAGE2_4B_EV_FOIL_SLOWDOWN","symbol":"006110","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C14 blocks battery demand slowdown rows where call-off/inventory/margin drag causes low MFE and deep MAE","raw_component_scores_before":{"EV_demand_slowdown_score":14,"inventory_correction_score":12,"customer_calloff_score":10,"capex_delay_score":7,"utilization_decline_score":9,"margin_pressure_score":11,"cash_drag_score":8,"relative_strength_score":-4,"execution_risk_score":-18,"theme_spike_risk":-10,"information_confidence":4},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/4B-Guard","raw_component_scores_after":{"EV_demand_slowdown_score":17,"inventory_correction_score":15,"customer_calloff_score":12,"capex_delay_score":8,"utilization_decline_score":11,"margin_pressure_score":14,"cash_drag_score":10,"relative_strength_score":-6,"execution_risk_score":-24,"theme_spike_risk":-12,"information_confidence":5},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Validated","component_delta_explanation":"Low MFE and deep MAE validate the 4B demand-slowdown guard rather than any positive stage."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L92_101360_ECODREAM_PRECURSOR_RAMP_FALSE_OVERBLOCK","trigger_id":"R3L92_C14_101360_20240111_STAGE2_FALSE_OVERBLOCK_PRECURSOR_RAMP","symbol":"101360","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_scope":"current_default_proxy","profile_hypothesis":"broad EV slowdown guard should not override exact customer capacity-ramp / offtake bridge","raw_component_scores_before":{"EV_demand_slowdown_score":2,"inventory_correction_score":0,"customer_calloff_score":0,"capex_delay_score":0,"utilization_decline_score":0,"margin_pressure_score":0,"cash_drag_score":0,"customer_capacity_ramp_override":16,"offtake_order_override":14,"relative_strength_score":16,"execution_risk_score":-6,"theme_spike_risk":-3,"information_confidence":4},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable/Yellow-Watch/DataQualityWatch","raw_component_scores_after":{"EV_demand_slowdown_score":0,"inventory_correction_score":0,"customer_calloff_score":0,"capex_delay_score":0,"utilization_decline_score":0,"margin_pressure_score":0,"cash_drag_score":0,"customer_capacity_ramp_override":18,"offtake_order_override":16,"relative_strength_score":17,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch/DataQualityWatch","component_delta_explanation":"Extreme MFE with low MAE shows overbroad C14 blocking would be wrong; exact evidence and CA repair still block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L92_282880_COWINTECH_EQUIPMENT_CAPEX_DELAY_4B","trigger_id":"R3L92_C14_282880_20240102_STAGE2_4B_EQUIPMENT_CAPEX_DELAY","symbol":"282880","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_scope":"current_default_proxy","profile_hypothesis":"battery equipment capex-delay and backlog-quality deterioration should route to 4B when MFE is weak and MAE expands","raw_component_scores_before":{"EV_demand_slowdown_score":11,"inventory_correction_score":6,"customer_calloff_score":8,"capex_delay_score":14,"utilization_decline_score":8,"margin_pressure_score":9,"cash_drag_score":7,"relative_strength_score":-3,"execution_risk_score":-16,"theme_spike_risk":-8,"information_confidence":4},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/4B-Guard","raw_component_scores_after":{"EV_demand_slowdown_score":13,"inventory_correction_score":7,"customer_calloff_score":10,"capex_delay_score":17,"utilization_decline_score":10,"margin_pressure_score":12,"cash_drag_score":9,"relative_strength_score":-6,"execution_risk_score":-24,"theme_spike_risk":-12,"information_confidence":5},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Validated","component_delta_explanation":"Low MFE and deep MAE validate capex-delay 4B risk routing."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L92_C14_P0_CURRENT","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails work if C14 is a precise 4B/4C risk guard and not a blanket battery overblock","eligible_trigger_count":3,"avg_MFE90_pct":104.52,"avg_MAE90_pct":-16.98,"avg_MFE180_pct":104.52,"avg_MAE180_pct":-36.68,"validated_4B_guard_count":2,"false_overblock_count":1,"score_return_alignment_verdict":"mixed_without_C14_specific_calloff_capex_delay_vs_capacity_ramp_override"}
{"row_type":"profile_comparison","comparison_id":"R3L92_C14_P1_SECTOR_SPECIFIC","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_id":"P1_L3_EV_demand_slowdown_guard_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 EV slowdown signals need customer call-off, inventory correction, capex delay, margin pressure or cash drag before hard 4B; customer capacity ramp overrides broad slowdown","changed_axes":["calloff_inventory_required","capex_delay_required","customer_ramp_override"],"changed_thresholds":{"4B_gate":"slowdown_or_calloff_or_capex_delay_plus_margin_or_cash_drag_required","overblock_override":"customer_capacity_ramp_or_offtake_bridge"},"eligible_trigger_count":3,"validated_4B_guard_count":2,"false_overblock_count":1,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R3L92_C14_P2_CANONICAL","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_id":"P2_C14_demand_slowdown_4B_and_ramp_override_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C14 should be a precise risk guard: hard 4B when call-off/capex-delay/margin-drag exists, but not when customer-ramp bridge is stronger","changed_axes":["C14_calloff_capex_delay_margin_cash_4B_guard","C14_customer_capacity_ramp_false_overblock_override","C14_CA_data_quality_guard"],"changed_thresholds":{"hard_4B_gate":"bridge_missing_and_(MFE90_lt_20_or_MAE180_le_minus35)","override_gate":"customer_capacity_ramp_plus_order_or_offtake_bridge"},"eligible_trigger_count":3,"validated_4B_guard_count":2,"false_overblock_count":1,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R3L92_C14_P3_COUNTEREXAMPLE_GUARD","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_id":"P3_C14_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If slowdown/capex-delay bridge exists and no customer-ramp override exists, MFE90<20 or MAE180<=-35 routes to 4B; if customer-ramp override exists, do not overblock","changed_axes":["C14_low_MFE_4B_guardrail","C14_deep_MAE_4B_guardrail","C14_overblock_override_guardrail"],"changed_thresholds":{"bad_entry_filter":"slowdown_bridge_present_and_no_override_and_(MFE90_lt_20_or_MAE180_le_minus35)"},"eligible_trigger_count":3,"validated_4B_guard_count":2,"false_overblock_count":1,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_DEMAND_SLOWDOWN_4B_GUARD_VS_PRECURSOR_RAMP_FALSE_OVERBLOCK","row_count":3,"unique_symbol_count":3,"positive_case_count":0,"positive_risk_guard_count":2,"counterexample_count":1,"validated_4B_guard_count":2,"false_overblock_count":1,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":104.52,"avg_MAE90_pct":-16.98,"avg_MFE180_pct":104.52,"avg_MAE180_pct":-36.68,"risk_guard_avg_MFE90_pct":9.63,"risk_guard_avg_MAE180_pct":-51.08,"false_overblock_MFE90_pct":294.30,"interpretation":"C14 works only as a precise risk guard. 삼아알미늄 and 코윈테크 validate 4B routing when EV demand slowdown / capex delay causes weak MFE and deep MAE. 에코앤드림 shows the opposite: broad EV-slowdown blocking would have missed a strong precursor/customer-ramp move, so customer-capacity/offtake bridge must override generic slowdown vocabulary."}
{"row_type":"stage_transition_summary","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"006110","trigger_type":"Stage2-4B-Validated-EVAluminumFoilDemandSlowdownGuard","entry_date":"2024-01-02","stage2_to_90D_outcome":"valid_4B_low_MFE_deep_MAE","stage2_to_180D_outcome":"validated_EV_demand_slowdown_guard","MFE90_ge20":false,"MAE180_le_minus35":true,"transition_note":"EV aluminum-foil slowdown/call-off/margin drag should stay Watch/4B-risk, not Yellow/Green."}
{"row_type":"stage_transition_summary","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"101360","trigger_type":"Stage2-FalsePositive-OverbroadEVDemandSlowdownWouldMissPrecursorRamp","entry_date":"2024-01-11","stage2_to_90D_outcome":"false_overblock_extreme_MFE_low_MAE","stage2_to_180D_outcome":"customer_capacity_ramp_override_but_CA_data_quality_watch","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Do not hard-block with generic EV slowdown when customer capacity ramp/offtake evidence exists; exact evidence and CA repair still required."}
{"row_type":"stage_transition_summary","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"282880","trigger_type":"Stage2-4B-Validated-BatteryEquipmentCapexDelayDemandSlowdownGuard","entry_date":"2024-01-02","stage2_to_90D_outcome":"valid_4B_low_MFE_capex_delay","stage2_to_180D_outcome":"validated_equipment_capex_delay_guard_deep_MAE","MFE90_ge20":false,"MAE180_le_minus35":true,"transition_note":"Battery equipment capex-delay/backlog-quality deterioration should route to Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","residual_type":"precise_EV_demand_slowdown_4B_guard_and_customer_ramp_false_overblock_override","contribution":"Adds two C14 validated 4B guards and one false-overblock counterexample, avoiding C14 top-covered and previous R3 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_VALID_4B_GUARD_VS_PRECURSOR_RAMP_FALSE_OVERBLOCK","positive_risk_guard_count":2,"counterexample_count":1,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":1,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C14 now has non-top-symbol EV foil and battery-equipment valid 4B guards plus a precursor/customer-ramp false-overblock case; next R3 C14 loops should exact-URL repair call-off, capex-delay, utilization, margin/cash drag and customer-ramp override evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","axis":"C14_calloff_capex_delay_margin_cash_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"006110 and 282880 validate 4B routing when EV demand slowdown or capex-delay proxy exists and MFE stays below 20 while MAE expands deeply."}
{"row_type":"shadow_weight","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","axis":"C14_customer_capacity_ramp_false_overblock_override","scope":"canonical_archetype","candidate_delta":1.0,"direction":"override_guard","apply_now":false,"shadow_only":true,"evidence_basis":"101360 shows broad EV slowdown blocking can be false if customer capacity-ramp/offtake bridge is stronger."}
{"row_type":"shadow_weight","round":"R3","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","axis":"C14_2024_CA_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"101360 has a 2024-08-01 corporate-action candidate after selected entry, so patch consideration requires price-path/evidence repair."}
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
  - EV_demand_slowdown_valid_4B_guard
  - battery_equipment_capex_delay_valid_4B_guard
  - broad_EV_slowdown_false_overblock
  - customer_capacity_ramp_override_needed
  - 2024_CA_data_quality_watch
new_axis_proposed:
  - C14_calloff_capex_delay_margin_cash_4B_guard_shadow_only
  - C14_customer_capacity_ramp_false_overblock_override_shadow_only
  - C14_2024_CA_data_quality_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows.
`006110` has historical corporate-action candidates before 2024; the selected 2024 window is usable.
`101360` has a 2024-08-01 corporate-action candidate after selected entry, so it remains data-quality-watch before production patching.
`282880` has no corporate-action candidate in its profile and the selected 2024 window is clean.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 101360
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
   - previous R3 loop88 C14 symbols
   - previous R3 loop89 C11 symbols
   - previous R3 loop90 C12 symbols
   - previous R3 loop91 C13 symbols
6. Confirm accidentally touched stale R1/C02 and R2/C08 candidate rows are not ingested from this MD.
7. Keep 101360 in 2024 corporate-action data-quality watch before patch consideration.
8. If aggregate support remains stable after exact evidence URL repair, consider C14-scoped safe patch candidates:
   - C14_calloff_capex_delay_margin_cash_4B_guard
   - C14_customer_capacity_ramp_false_overblock_override
   - C14_2024_CA_data_quality_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R3
completed_loop = 92
next_round = R4
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 validated 4B risk guards, 1 false-overblock counterexample, and 0 4C rows for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.
```

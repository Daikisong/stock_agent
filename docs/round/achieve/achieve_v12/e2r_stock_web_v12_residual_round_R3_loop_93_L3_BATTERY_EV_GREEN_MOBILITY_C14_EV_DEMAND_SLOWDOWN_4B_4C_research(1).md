# E2R Stock-Web v12 Residual Research — R3 Loop 93 / L3 / C14

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 93
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: BATTERY_EQUIPMENT_BACKLOG_FALSE_OVERBLOCK_VS_RECYCLING_AND_CELL_PARTS_DEMAND_SLOWDOWN_DECAY
sector: battery / EV / demand slowdown / capex deferral / battery equipment / recycling / battery can / utilization / margin / FCF
output_file: e2r_stock_web_v12_residual_round_R3_loop_93_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This is the valid output for the current execution.

```text
selected_round = R3
selected_loop = 93
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
```

Reason for selecting C14:

```text
v12 scheduler = coverage_index_first
sequential_round_cycle_required = false
coverage_gap_can_override_previous_round = true
selected_archetype_drives_round = true
```

Local-stream hygiene:

```text
The immediately preceding valid output was R2/L2/C09 tertiary.
A stale C09/C08 candidate trail was visible in this execution path, but those rows are excluded from this C14 output.
C14 remains an under-30 EV/battery risk archetype after local loop92 expansion and deserves a new non-overlapping R3 pocket.
```

No-Repeat / recent-symbol avoidance:

```text
Avoided recent R3 symbols:
R3 loop85 C11: 078600, 247540, 393890
R3 loop86 C12: 317330, 066970, 361610
R3 loop87 C13: 096770, 011790, 051910
R3 loop88 C14: 093370, 336370, 382840
R3 loop89 C11: 222080, 290670, 089980
R3 loop90 C12: 114190, 450080, 417200
R3 loop91 C13: 036830, 014820, 095500
R3 loop92 C14: 006110, 101360, 282880
R3 loop93 C11/C12/C13: 348370, 121600, 020150, 373220, 006400, 005070, 003670, 086520, 278280

Avoided stale semiconductor candidates touched in this execution path:
240810, 079370, 039440 and earlier C08/C09 symbols.
```

Selected symbols:

```text
137400, 365340, 091580
```

Selected pocket:

```text
battery-equipment backlog/capex false-overblock after EV destock reset
vs
battery recycling capacity/commercialization vocabulary that fails under EV demand slowdown and weak cash bridge
vs
battery-can/parts capacity vocabulary that fails when utilization, call-off and margin/FCF bridge are missing
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"137400","company_name":"피엔티","profile_path":"atlas/symbol_profiles/137/137400.json","first_date":"2012-07-06","last_date":"2026-02-20","trading_day_count":3346,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2012-11-30","2012-12-26","2019-05-07","2019-05-30"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window. Selected 2024 window is usable.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
{"row_type":"price_source_validation","symbol":"365340","company_name":"성일하이텍","profile_path":"atlas/symbol_profiles/365/365340.json","first_date":"2022-07-28","last_date":"2026-02-20","trading_day_count":870,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Recent listing relative to older corpus; selected 2024 window is clean.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window; recent_listing_watch"}
{"row_type":"price_source_validation","symbol":"091580","company_name":"상신이디피","profile_path":"atlas/symbol_profiles/091/091580.json","first_date":"2007-05-23","last_date":"2026-02-20","trading_day_count":4621,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2007-06-11","2010-01-26","2011-05-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 window. Selected 2024 window is usable.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"137400","trigger_type":"Stage2-FalsePositive-OverbroadEVDemandSlowdownWouldMissBatteryEquipmentBacklogBridge","entry_date":"2024-02-13","duplicate_status":"new C14 symbol/trigger/date combination outside recent R3 C14 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"365340","trigger_type":"Stage2-4B-Validated-RecyclingCapacityDemandSlowdownNoCommercialCashBridge","entry_date":"2024-02-21","duplicate_status":"new C14 symbol/trigger/date combination outside recent R3 C14 symbols; recent-listing watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"091580","trigger_type":"Stage2-FalsePositive-BatteryCanPartsCapacityVocabularyNoCalloffUtilizationCashBridge","entry_date":"2024-03-07","duplicate_status":"new C14 symbol/trigger/date combination outside recent R3 C14 symbols"}
```

## 4. Research question

C14 is not “EV 수요 둔화라서 무조건 막는다.”
The useful demand-slowdown guard must separate real thesis break from recoverable reset:

```text
EV demand slowdown / call-off risk
customer capex deferral or cancellation
equipment backlog cushion
utilization and shipment visibility
ASP / pass-through discipline
margin and working-capital bridge
FCF conversion
hard 4C evidence when demand thesis breaks
false-overblock override when backlog / order / margin bridge survives
```

A demand-slowdown headline is a red traffic light. Sometimes the whole road is closed; sometimes a truck is merely waiting at the gate with a signed delivery slot. C14 must tell the difference.

Residual question:

```text
Can C14 distinguish:
1. a battery-equipment backlog bridge that should not be overblocked by broad EV slowdown,
2. a recycling/capacity story that really lacks commercial cash conversion under EV slowdown,
3. a battery-can/parts capacity story where call-off/utilization/margin bridge fails after a price spike?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C14_R3L93_137400_PNT_FALSE_OVERBLOCK","symbol":"137400","company_name":"피엔티","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_EQUIPMENT_BACKLOG_CAPEX_FALSE_OVERBLOCK_AFTER_EV_DESTOCK_RESET","case_type":"false_overblock_recovery","positive_or_counterexample":"positive","best_trigger":"Stage2-FalsePositive-OverbroadEVDemandSlowdownWouldMissBatteryEquipmentBacklogBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_overblock_high_MFE180_low_MAE_if_battery_equipment_backlog_bridge_exists","current_profile_verdict":"current_profile_false_positive_if_broad_EV_slowdown_guard_blocks_backlog_order_margin_bridge_after_reset","price_source":"Songdaiki/stock-web","notes":"EV slowdown should not become a blanket veto. PNT showed post-reset high MFE when battery-equipment backlog/order bridge could still survive despite demand-slowdown vocabulary."}
{"row_type":"case","case_id":"C14_R3L93_365340_SUNGIL_RECYCLING_DEMAND_DECAY","symbol":"365340","company_name":"성일하이텍","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"RECYCLING_CAPACITY_COMMERCIALIZATION_VOCABULARY_WITHOUT_DEMAND_CASH_BRIDGE","case_type":"validated_4B_demand_slowdown","positive_or_counterexample":"counterexample","best_trigger":"Stage2-4B-Validated-RecyclingCapacityDemandSlowdownNoCommercialCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"validated_4B_low_MFE_deep_MAE_no_recycling_commercial_cash_bridge","current_profile_verdict":"current_profile_correct_if_recycling_capacity_vocabulary_routes_to_4B_when_EV_demand_and_cash_bridge_missing","price_source":"Songdaiki/stock-web","notes":"Recycling/capacity vocabulary did not protect price path when EV demand and commercial cash conversion were missing. This is a clean C14 4B risk row."}
{"row_type":"case","case_id":"C14_R3L93_091580_SANGSIN_PARTS_DECAY","symbol":"091580","company_name":"상신이디피","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_CAN_PARTS_CAPACITY_VOCABULARY_WITHOUT_CALLOFF_UTILIZATION_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-BatteryCanPartsCapacityVocabularyNoCalloffUtilizationCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_post_spike_sub20_MFE_extreme_MAE_no_calloff_utilization_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_battery_parts_capacity_vocabulary_overcredited_under_EV_slowdown","price_source":"Songdaiki/stock-web","notes":"Battery can/parts capacity vocabulary produced a short spike but failed badly when call-off, utilization and cash conversion did not appear."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 137400 피엔티 — EV demand slowdown false-overblock / backlog bridge

Entry row: `2024-02-13 c=39300`, after a deep January/February reset.
Observed path: `2024-03-06 h=48200` and later `2024-10-10 h=64100`, while early drawdown remained controlled.

```jsonl
{"row_type":"trigger","trigger_id":"R3L93_C14_137400_20240213_STAGE2_FALSE_OVERBLOCK_PNT_BACKLOG","case_id":"C14_R3L93_137400_PNT_FALSE_OVERBLOCK","symbol":"137400","company_name":"피엔티","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_EQUIPMENT_BACKLOG_CAPEX_FALSE_OVERBLOCK_AFTER_EV_DESTOCK_RESET","loop_objective":"false_overblock_mining;holdout_validation;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-OverbroadEVDemandSlowdownWouldMissBatteryEquipmentBacklogBridge","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":39300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_equipment_backlog_capex_reset_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; battery equipment backlog, customer capex, order visibility, delivery and margin bridge treated as non-price proxy","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["battery_equipment_backlog_proxy","capex_reset_proxy","order_visibility_proxy","relative_strength_after_reset"],"stage3_evidence_fields":["exact_customer_order_source_pending","delivery_schedule_source_pending","margin_FCF_source_pending","calloff_deferral_check_pending"],"stage4b_evidence_fields":["false_overblock_watch","MFE180_ge50_watch","Green_strict_watch"],"stage4c_evidence_fields":["demand_thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv","profile_path":"atlas/symbol_profiles/137/137400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.65,"MFE_90D_pct":22.65,"MFE_180D_pct":63.10,"MAE_30D_pct":-7.63,"MAE_90D_pct":-7.63,"MAE_180D_pct":-7.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-10","peak_price":64100.0,"max_drawdown_low_date":"2024-04-08","max_drawdown_low":36300.0,"drawdown_after_peak_pct":-38.30,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.35,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"do_not_hard_block_battery_equipment_after_EV_demand_reset_if_order_backlog_delivery_margin_bridge_survives","four_b_evidence_type":["false_overblock_watch","MFE180_ge50_watch","Green_strict_watch"],"four_c_protection_label":"demand_thesis_break_watch_only","trigger_outcome_label":"false_overblock_high_MFE180_low_MAE_if_battery_equipment_backlog_bridge_exists","current_profile_verdict":"current_profile_false_positive_if_broad_EV_slowdown_guard_blocks_backlog_order_margin_bridge_after_reset","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"137400_2024-02-13_39300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C14 should not overblock battery-equipment rows after a reset when backlog/order/delivery/margin evidence survives. Route to evidence repair rather than hard 4B/4C."}
```

### 6.2 365340 성일하이텍 — recycling/capacity commercialization vocabulary without demand-cash bridge

Entry row: `2024-02-21 c=96500`.
Observed path: small local high `2024-02-28 h=99700`, then deep decline to `2024-11-15 l=39750`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L93_C14_365340_20240221_STAGE2_4B_RECYCLING_DEMAND_DECAY","case_id":"C14_R3L93_365340_SUNGIL_RECYCLING_DEMAND_DECAY","symbol":"365340","company_name":"성일하이텍","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"RECYCLING_CAPACITY_COMMERCIALIZATION_VOCABULARY_WITHOUT_DEMAND_CASH_BRIDGE","loop_objective":"validated_4B_guard;residual_false_positive_mining;counterexample_mining","trigger_type":"Stage2-4B-Validated-RecyclingCapacityDemandSlowdownNoCommercialCashBridge","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":96500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_recycling_capacity_commercialization_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; recycling/capacity vocabulary treated as insufficient without EV demand recovery, feedstock volume, commercial margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["battery_recycling_capacity_vocabulary","commercialization_keyword","EV_recovery_theme"],"stage3_evidence_fields":["feedstock_volume_missing","commercial_contract_missing","margin_cash_bridge_missing","demand_recovery_missing"],"stage4b_evidence_fields":["low_MFE","deep_MAE","commercial_cash_bridge_missing_watch","recent_listing_watch"],"stage4c_evidence_fields":["demand_thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/365/365340/2024.csv","profile_path":"atlas/symbol_profiles/365/365340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.32,"MFE_90D_pct":3.32,"MFE_180D_pct":3.32,"MAE_30D_pct":-18.96,"MAE_90D_pct":-19.07,"MAE_180D_pct":-58.81,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-28","peak_price":99700.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":39750.0,"drawdown_after_peak_pct":-60.13,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"recycling_capacity_vocabulary_without_EV_demand_feedstock_margin_cash_bridge_should_route_to_4B_watch","four_b_evidence_type":["low_MFE","deep_MAE","commercial_cash_bridge_missing_watch","recent_listing_watch"],"four_c_protection_label":"demand_thesis_break_watch_only","trigger_outcome_label":"validated_4B_low_MFE_deep_MAE_no_recycling_commercial_cash_bridge","current_profile_verdict":"current_profile_correct_if_recycling_capacity_vocabulary_routes_to_4B_when_EV_demand_and_cash_bridge_missing","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["recent_listing_watch"],"corporate_action_window_status":"clean; recent_listing_watch","same_entry_group_id":"365340_2024-02-21_96500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C14 should route recycling/capacity rows to 4B when EV demand, feedstock volume, commercial contract, margin and cash bridge are missing."}
```

### 6.3 091580 상신이디피 — battery can/parts capacity vocabulary without call-off/utilization bridge

Entry row: `2024-03-07 c=18000`, after a battery parts capacity spike.
Observed path: `2024-03-20 h=20700`, then severe decline to `2024-11-15 l=7180` and `2024-12-09 l=6510`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L93_C14_091580_20240307_STAGE2_FALSE_POSITIVE_BATTERYCAN_PARTS","case_id":"C14_R3L93_091580_SANGSIN_PARTS_DECAY","symbol":"091580","company_name":"상신이디피","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_CAN_PARTS_CAPACITY_VOCABULARY_WITHOUT_CALLOFF_UTILIZATION_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;demand_slowdown_guard","trigger_type":"Stage2-FalsePositive-BatteryCanPartsCapacityVocabularyNoCalloffUtilizationCashBridge","trigger_date":"2024-03-07","entry_date":"2024-03-07","entry_price":18000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_can_parts_capacity_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; battery can/parts capacity vocabulary treated as insufficient without call-off volume, utilization, ASP/margin and cash bridge","evidence_source_type":"historical_public_theme_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["battery_can_parts_capacity_keyword","EV_parts_rebound_vocabulary","price_spike"],"stage3_evidence_fields":["calloff_volume_missing","utilization_bridge_missing","ASP_margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["sub20_MFE","extreme_MAE","calloff_utilization_missing_watch"],"stage4c_evidence_fields":["demand_thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/091/091580/2024.csv","profile_path":"atlas/symbol_profiles/091/091580.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.00,"MFE_90D_pct":15.00,"MFE_180D_pct":15.00,"MAE_30D_pct":-7.72,"MAE_90D_pct":-44.44,"MAE_180D_pct":-60.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-20","peak_price":20700.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":7180.0,"drawdown_after_peak_pct":-65.31,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"battery_parts_capacity_vocabulary_without_calloff_utilization_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["sub20_MFE","extreme_MAE","calloff_utilization_missing_watch"],"four_c_protection_label":"demand_thesis_break_watch_only","trigger_outcome_label":"counterexample_post_spike_sub20_MFE_extreme_MAE_no_calloff_utilization_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_battery_parts_capacity_vocabulary_overcredited_under_EV_slowdown","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"091580_2024-03-07_18000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C14 should route battery-can/parts capacity vocabulary to Watch/4B when call-off, utilization, ASP/margin and cash evidence are missing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L93_137400_PNT_FALSE_OVERBLOCK","trigger_id":"R3L93_C14_137400_20240213_STAGE2_FALSE_OVERBLOCK_PNT_BACKLOG","symbol":"137400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_scope":"current_default_proxy","profile_hypothesis":"C14 should block EV demand-slowdown thesis breaks but not overblock battery equipment rows where order backlog and margin bridge survive","raw_component_scores_before":{"EV_demand_slowdown_risk":-8,"customer_calloff_risk":-5,"capex_deferral_risk":-4,"order_backlog_buffer":10,"delivery_visibility":8,"utilization_visibility":7,"margin_bridge":8,"FCF_bridge":6,"relative_strength_after_reset":12,"information_confidence":4},"weighted_score_before":64,"stage_label_before":"Stage2-Watch/FalseOverblock","raw_component_scores_after":{"EV_demand_slowdown_risk":-6,"customer_calloff_risk":-4,"capex_deferral_risk":-3,"order_backlog_buffer":13,"delivery_visibility":11,"utilization_visibility":9,"margin_bridge":10,"FCF_bridge":8,"relative_strength_after_reset":13,"information_confidence":5},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable/Yellow-Watch/FalseOverblockOverride","component_delta_explanation":"Backlog/order bridge can override a blanket EV slowdown veto, but exact evidence is still required before Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L93_365340_SUNGIL_RECYCLING_DEMAND_DECAY","trigger_id":"R3L93_C14_365340_20240221_STAGE2_4B_RECYCLING_DEMAND_DECAY","symbol":"365340","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_scope":"current_default_proxy","profile_hypothesis":"recycling/capacity vocabulary without feedstock demand and commercial cash bridge should be blocked","raw_component_scores_before":{"EV_demand_slowdown_risk":-16,"customer_calloff_risk":-10,"capex_deferral_risk":-8,"order_backlog_buffer":0,"delivery_visibility":0,"utilization_visibility":0,"margin_bridge":0,"FCF_bridge":0,"relative_strength_after_reset":1,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage1/4B-Watch","raw_component_scores_after":{"EV_demand_slowdown_risk":-24,"customer_calloff_risk":-14,"capex_deferral_risk":-12,"order_backlog_buffer":0,"delivery_visibility":0,"utilization_visibility":0,"margin_bridge":0,"FCF_bridge":0,"relative_strength_after_reset":0,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Validated","component_delta_explanation":"Low MFE and deep MAE confirm demand/cash bridge absence; keep 4B until exact commercial evidence appears."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_R3L93_091580_SANGSIN_PARTS_DECAY","trigger_id":"R3L93_C14_091580_20240307_STAGE2_FALSE_POSITIVE_BATTERYCAN_PARTS","symbol":"091580","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","profile_scope":"current_default_proxy","profile_hypothesis":"battery parts/capacity vocabulary without call-off and utilization bridge should remain Watch/4B","raw_component_scores_before":{"EV_demand_slowdown_risk":-14,"customer_calloff_risk":-12,"capex_deferral_risk":-7,"order_backlog_buffer":1,"delivery_visibility":0,"utilization_visibility":0,"margin_bridge":0,"FCF_bridge":0,"relative_strength_after_reset":4,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"EV_demand_slowdown_risk":-26,"customer_calloff_risk":-18,"capex_deferral_risk":-10,"order_backlog_buffer":0,"delivery_visibility":0,"utilization_visibility":0,"margin_bridge":0,"FCF_bridge":0,"relative_strength_after_reset":0,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-20 MFE and extreme MAE require call-off/utilization/margin evidence before any positive stage."}
```

## 8. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_PNT_FALSE_OVERBLOCK_VS_RECYCLING_PARTS_DEMAND_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"false_overblock_count":1,"validated_4B_count":1,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":13.66,"avg_MAE90_pct":-23.71,"avg_MFE180_pct":27.14,"avg_MAE180_pct":-42.18,"stage2_bad_entry_rate_bridge_missing":0.67,"interpretation":"C14 needs two-sided discipline. 피엔티 shows a broad EV-slowdown veto can false-overblock battery-equipment backlog/order bridge after reset, while 성일하이텍 and 상신이디피 show recycling/capacity or battery-parts vocabulary should route to 4B when demand, call-off, utilization, margin and cash evidence are missing."}
{"row_type":"stage_transition_summary","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"137400","trigger_type":"Stage2-FalsePositive-OverbroadEVDemandSlowdownWouldMissBatteryEquipmentBacklogBridge","entry_date":"2024-02-13","stage2_to_90D_outcome":"false_overblock_MFE90_ge20_low_MAE","stage2_to_180D_outcome":"battery_equipment_backlog_bridge_survived_EV_slowdown_guard","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Do not hard-block EV/battery equipment after reset if order backlog, delivery and margin evidence survive."}
{"row_type":"stage_transition_summary","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"365340","trigger_type":"Stage2-4B-Validated-RecyclingCapacityDemandSlowdownNoCommercialCashBridge","entry_date":"2024-02-21","stage2_to_90D_outcome":"validated_4B_low_MFE_no_cash_bridge","stage2_to_180D_outcome":"recycling_capacity_vocabulary_failed_under_EV_demand_slowdown","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Recycling/capacity vocabulary without demand/feedstock/commercial cash bridge should stay 4B."}
{"row_type":"stage_transition_summary","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","symbol":"091580","trigger_type":"Stage2-FalsePositive-BatteryCanPartsCapacityVocabularyNoCalloffUtilizationCashBridge","entry_date":"2024-03-07","stage2_to_90D_outcome":"bad_stage2_sub20_MFE_extreme_MAE","stage2_to_180D_outcome":"battery_parts_capacity_vocabulary_failed_calloff_utilization_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Battery parts/capacity vocabulary without call-off/utilization/margin bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","residual_type":"EV_demand_slowdown_false_overblock_vs_validated_4B_capacity_decay","contribution":"Adds one C14 false-overblock recovery row and two validated demand-slowdown 4B rows, selected after discarding duplicate-prone C09/C08 stale paths from this execution.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_EQUIPMENT_BACKLOG_FALSE_OVERBLOCK_VS_RECYCLING_AND_CELL_PARTS_DEMAND_SLOWDOWN_DECAY","positive_case_count":1,"counterexample_count":2,"false_overblock_count":1,"validated_4B_count":1,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C14 now has a non-overlapping loop93 pocket: battery-equipment false-overblock plus recycling and battery-parts demand-slowdown 4B rows; next C14 loops should exact-URL repair call-off, capex deferral, utilization, margin and FCF evidence."}
```

## 9. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","axis":"C14_EV_slowdown_false_overblock_override_if_order_backlog_margin_bridge_survives","scope":"canonical_archetype","candidate_delta":1.0,"direction":"override_guard","apply_now":false,"shadow_only":true,"evidence_basis":"137400 shows post-reset battery-equipment backlog/order bridge can survive broad EV slowdown vocabulary."}
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","axis":"C14_capacity_recycling_parts_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"365340 and 091580 show recycling/capacity/parts vocabulary should route to 4B when demand, utilization, margin and cash bridge are absent."}
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","axis":"C14_calloff_utilization_margin_FCF_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"Weak rows fail specifically on call-off/utilization/margin/FCF bridge rather than on price alone."}
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","axis":"C14_recent_listing_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"365340 is a recent-listing row relative to older corpus; promotion requires price-quality and evidence repair."}
```

## 10. Residual Contribution Summary

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
  - EV_slowdown_false_overblock
  - recycling_capacity_vocabulary_overcredit
  - battery_parts_capacity_vocabulary_overcredit
  - calloff_utilization_margin_FCF_bridge_missing
  - recent_listing_data_quality_watch
new_axis_proposed:
  - C14_EV_slowdown_false_overblock_override_if_order_backlog_margin_bridge_survives_shadow_only
  - C14_capacity_recycling_parts_vocabulary_local_4B_guard_shadow_only
  - C14_calloff_utilization_margin_FCF_bridge_required_shadow_only
  - C14_recent_listing_data_quality_guard_shadow_only
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

## 11. Data-quality caveat

All selected triggers use Stock-Web tradable raw OHLC rows.
`137400` and `091580` have only historical corporate-action candidates before the selected 2024 windows; selected 2024 windows are usable.
`365340` has no corporate-action candidate and the selected window is clean, but it is a recent-listing/short-history row relative to the older corpus, so keep recent-listing data-quality watch.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for residual price-path analysis
evidence_url_pending = true
source_proxy_only = true
recent_listing_watch = true for 365340
promotion should prefer hold / exact evidence repair until exact URLs are added
```

## 12. Deferred Coding Agent Handoff Prompt

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
   - previous R3 loop88 C14 symbols
   - previous R3 loop92 C14 symbols
   - recent R3 loop93 C11/C12/C13 symbols
6. Confirm stale C09/C08 candidate rows touched earlier in this execution are not ingested from this MD.
7. Treat 137400 as false-overblock / evidence-repair row, not automatic Green.
8. Treat 365340 and 091580 as demand-slowdown 4B/Watch failure modes unless exact call-off, utilization, margin and cash evidence is added later.
9. Keep 365340 in recent-listing data-quality watch before patch consideration.
10. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C14-scoped safe patch candidates:
   - C14_EV_slowdown_false_overblock_override_if_order_backlog_margin_bridge_survives
   - C14_capacity_recycling_parts_vocabulary_local_4B_guard
   - C14_calloff_utilization_margin_FCF_bridge_required
   - C14_recent_listing_data_quality_guard
11. Do not loosen Stage3-Green.
12. Do not use future MFE/MAE in runtime scoring.
13. Use this MD only for calibration profile planning.
```

## 13. Round state

```text
completed_round = R3
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C08/C09/C01 only after reconciling local fatigue, otherwise rotate to remaining under-covered non-repeated archetype
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 14. Final one-line contribution

```text
This loop adds 3 new independent C14 cases, 1 EV-demand false-overblock recovery row, 2 demand-slowdown weak-bridge rows, and 2 local 4B-watch rows for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.
```

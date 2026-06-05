# E2R Stock-Web v12 Residual Research — R3 Loop 90 / L3 / C12

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 90
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: BATTERY_EQUIPMENT_CUSTOMER_CALLOFF_BRIDGE_VS_PRECURSOR_SUPERCAPACITOR_PRICE_ONLY_DECAY
sector: battery / EV / customer contract / call-off / equipment / precursor / supercapacitor
output_file: e2r_stock_web_v12_residual_round_R3_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R2 loop 90`.

```text
scheduled_round = R3
scheduled_loop = 90
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

R3 is restricted to battery / EV / green mobility.  
C12 is selected because the R3 lane just used C11 in loop89 and the natural rotation re-enters customer contract / call-off risk.

No-Repeat Index snapshot:

```text
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
rows = 28
symbols = 11
good/bad Stage2 = 9/6
4B/4C = 0/0
top-covered = 121600, 278280, 020150, 348370, 091580, 137400
```

This loop avoids the C12 top-covered list and recent R3 symbols:

```text
R3 loop85 C11: 078600, 247540, 393890
R3 loop86 C12: 317330, 066970, 361610
R3 loop87 C13: 096770, 011790, 051910
R3 loop88 C14: 093370, 336370, 382840
R3 loop89 C11: 222080, 290670, 089980
```

Candidate hygiene note:

```text
A duplicated R2/C06 file was accidentally generated during this execution path.
That file is not the valid output for this user request. The valid scheduled output is this R3/C12/loop90 MD.
```

Selected symbols:

```text
114190, 450080, 417200
```

This loop tests:

```text
battery equipment / material-handling customer call-off bridge
vs
battery precursor mega-theme rebound without durable call-off / margin bridge
vs
supercapacitor / EV-component IPO-cycle price decay without contract call-off evidence
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"114190","company_name":"강원에너지","profile_path":"atlas/symbol_profiles/114/114190.json","first_date":"2009-11-20","last_date":"2026-02-20","trading_day_count":3473,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2012-12-05","2012-12-26","2022-05-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"450080","company_name":"에코프로머티","profile_path":"atlas/symbol_profiles/450/450080.json","first_date":"2023-11-17","last_date":"2026-02-20","trading_day_count":548,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Recently listed in 2023; selected 2024 forward window is clean but IPO-cycle valuation memory should stay evidence-quality watch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window; recent_listing_watch"}
{"row_type":"price_source_validation","symbol":"417200","company_name":"LS머트리얼즈","profile_path":"atlas/symbol_profiles/417/417200.json","first_date":"2023-12-12","last_date":"2026-02-20","trading_day_count":531,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"Recently listed in 2023; selected 2024 forward window is clean but IPO-cycle price-memory watch is retained.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window; recent_listing_watch"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"114190","trigger_type":"Stage2-Actionable-BatteryEquipmentCustomerCalloffBridge-Positive","entry_date":"2024-01-26","duplicate_status":"new C12 symbol/trigger/date combination outside top-covered and previous R3 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"450080","trigger_type":"Stage2-FalsePositive-PrecursorMegaThemeRebound-NoDurableCalloffMarginBridge","entry_date":"2024-02-13","duplicate_status":"new C12 symbol/trigger/date combination outside top-covered and previous R3 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"417200","trigger_type":"Stage2-FalsePositive-SupercapacitorEVComponentIPOTheme-NoCustomerCalloffBridge","entry_date":"2024-01-02","duplicate_status":"new C12 symbol/trigger/date combination outside top-covered and previous R3 loop symbols"}
```

## 4. Research question

C12 is not “배터리 계약 뉴스가 있다.”  
The useful C12 signal must prove the conversion from headline contract to executable revenue:

```text
customer identity and credit quality
binding contract versus framework
call-off visibility
shipment schedule
qualification or acceptance
plant utilization
margin mix
working-capital discipline
cash conversion
```

A framework contract without call-off is a signed loading dock with no truck arriving. The paper is real, but the factory does not recognize revenue until the call-off, shipment and cash cycle actually move.

Residual question:

```text
Can C12 distinguish:
1. battery equipment / material-handling customer call-off bridge with high MFE but Green strictness,
2. precursor mega-theme rebound where local price action does not prove durable call-off or margin bridge,
3. supercapacitor / EV-component IPO-cycle price strength where the business bridge is missing and follow-through decays?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C12_R3L90_114190_KANGWON_ENERGY_CALLOFF_BRIDGE","symbol":"114190","company_name":"강원에너지","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_EQUIPMENT_CUSTOMER_CALLOFF_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-BatteryEquipmentCustomerCalloffBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_customer_calloff_shipment_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Battery equipment/material-handling proxy produced high MFE after a low-risk entry, but later drawdown keeps Green strict and requires exact customer call-off, shipment and margin evidence."}
{"row_type":"case","case_id":"C12_R3L90_450080_ECOPRO_MATERIALS_PRECURSOR_REBOUND","symbol":"450080","company_name":"에코프로머티","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"PRECURSOR_MEGA_THEME_REBOUND_WITHOUT_DURABLE_CALLOFF_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PrecursorMegaThemeRebound-NoDurableCalloffMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_recent_listing_watch","current_profile_verdict":"current_profile_false_positive_if_precursor_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Precursor mega-theme rebound after the January collapse had almost no MFE from the selected entry and deep later MAE; without durable call-off, shipment, margin and cash bridge it should remain 4B-watch."}
{"row_type":"case","case_id":"C12_R3L90_417200_LS_MATERIALS_IPO_EV_THEME","symbol":"417200","company_name":"LS머트리얼즈","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SUPERCAPACITOR_EV_COMPONENT_IPO_THEME_WITHOUT_CUSTOMER_CALLOFF_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SupercapacitorEVComponentIPOTheme-NoCustomerCalloffBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_extreme_MAE_IPO_decay","current_profile_verdict":"current_profile_false_positive_if_supercapacitor_EV_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Supercapacitor/EV-component IPO-cycle price strength had only local MFE and extreme later MAE without customer call-off, shipment, utilization and cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 114190 강원에너지 — battery equipment / customer call-off bridge positive

Entry row: `2024-01-26 c=13290`.  
Observed path: early low `2024-02-06 l=12400`, high `2024-02-28 h=21850`, and late low `2024-12-09 l=9010`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L90_C12_114190_20240126_STAGE2_BATTERY_EQUIPMENT_CALLOFF","case_id":"C12_R3L90_114190_KANGWON_ENERGY_CALLOFF_BRIDGE","symbol":"114190","company_name":"강원에너지","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_EQUIPMENT_CUSTOMER_CALLOFF_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-BatteryEquipmentCustomerCalloffBridge-Positive","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":13290.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_equipment_customer_calloff_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; battery equipment/material-handling customer call-off, shipment and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["customer_contract_proxy","calloff_visibility_proxy","shipment_schedule_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_calloff_pending","shipment_acceptance_pending","utilization_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/114/114190/2024.csv","profile_path":"atlas/symbol_profiles/114/114190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":64.41,"MFE_90D_pct":64.41,"MFE_180D_pct":64.41,"MAE_30D_pct":-6.70,"MAE_90D_pct":-6.70,"MAE_180D_pct":-32.20,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-28","peak_price":21850.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":9010.0,"drawdown_after_peak_pct":-58.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_late_drawdown_blocks_Green_without_exact_calloff_shipment_margin_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_customer_calloff_shipment_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"114190_2024-01-26_13290","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C12 can allow Stage2/Yellow when battery strength is tied to customer call-off, shipment schedule, utilization, margin and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 450080 에코프로머티 — precursor mega-theme rebound without durable call-off/margin bridge

Entry row: `2024-02-13 c=209500`, after the January collapse and February rebound.  
Observed path: next-day high `2024-02-14 h=211500`, then drawdown to `2024-12-27 l=64900`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L90_C12_450080_20240213_STAGE2_FALSE_POSITIVE_PRECURSOR_REBOUND","case_id":"C12_R3L90_450080_ECOPRO_MATERIALS_PRECURSOR_REBOUND","symbol":"450080","company_name":"에코프로머티","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"PRECURSOR_MEGA_THEME_REBOUND_WITHOUT_DURABLE_CALLOFF_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-PrecursorMegaThemeRebound-NoDurableCalloffMarginBridge","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":209500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_precursor_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; precursor mega-theme rebound treated as insufficient without durable customer call-off, shipment acceptance, utilization, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["battery_precursor_theme","relative_strength_rebound","recent_listing_momentum"],"stage3_evidence_fields":["durable_calloff_missing","shipment_acceptance_missing","utilization_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["near_zero_MFE","recent_listing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/450/450080/2024.csv","profile_path":"atlas/symbol_profiles/450/450080.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.95,"MFE_90D_pct":0.95,"MFE_180D_pct":0.95,"MAE_30D_pct":-35.51,"MAE_90D_pct":-46.49,"MAE_180D_pct":-69.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-14","peak_price":211500.0,"max_drawdown_low_date":"2024-12-27","max_drawdown_low":64900.0,"drawdown_after_peak_pct":-69.31,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"precursor_rebound_without_durable_calloff_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","recent_listing_watch","calloff_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_recent_listing_watch","current_profile_verdict":"current_profile_false_positive_if_precursor_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["recent_listing_price_memory_watch"],"corporate_action_window_status":"clean_recent_listing","same_entry_group_id":"450080_2024-02-13_209500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C12 should not promote precursor rebound unless durable call-off, shipment, utilization, margin and cash evidence are repaired. Near-zero MFE and extreme MAE force 4B-watch."}
```

### 6.3 417200 LS머트리얼즈 — supercapacitor / EV-component IPO-cycle theme without customer call-off bridge

Entry row: `2024-01-02 c=45800`, directly after the post-listing heat.  
Observed path: local high `2024-01-05 h=50300`, then lows through `2024-12-09 l=9600`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L90_C12_417200_20240102_STAGE2_FALSE_POSITIVE_SUPERCAP_IPO_THEME","case_id":"C12_R3L90_417200_LS_MATERIALS_IPO_EV_THEME","symbol":"417200","company_name":"LS머트리얼즈","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SUPERCAPACITOR_EV_COMPONENT_IPO_THEME_WITHOUT_CUSTOMER_CALLOFF_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate;IPO_cycle_decay_stress_test","trigger_type":"Stage2-FalsePositive-SupercapacitorEVComponentIPOTheme-NoCustomerCalloffBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":45800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_supercapacitor_EV_component_IPO_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; supercapacitor/EV-component IPO-cycle theme treated as insufficient without customer call-off, shipment schedule, utilization, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["supercapacitor_EV_component_theme","IPO_cycle_price_strength"],"stage3_evidence_fields":["customer_calloff_missing","shipment_schedule_missing","utilization_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_MFE","recent_listing_watch","extreme_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/417/417200/2024.csv","profile_path":"atlas/symbol_profiles/417/417200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.83,"MFE_90D_pct":9.83,"MFE_180D_pct":9.83,"MAE_30D_pct":-38.65,"MAE_90D_pct":-38.65,"MAE_180D_pct":-79.04,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-05","peak_price":50300.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":9600.0,"drawdown_after_peak_pct":-80.91,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"supercapacitor_EV_component_IPO_theme_without_customer_calloff_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","recent_listing_watch","customer_calloff_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_extreme_MAE_IPO_decay","current_profile_verdict":"current_profile_false_positive_if_supercapacitor_EV_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["recent_listing_price_memory_watch"],"corporate_action_window_status":"clean_recent_listing","same_entry_group_id":"417200_2024-01-02_45800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C12 should not count post-listing EV component MFE as customer call-off evidence. Customer call-off, shipment, utilization, margin and cash bridge must be repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_R3L90_114190_KANGWON_ENERGY_CALLOFF_BRIDGE","trigger_id":"R3L90_C12_114190_20240126_STAGE2_BATTERY_EQUIPMENT_CALLOFF","symbol":"114190","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C12 requires customer call-off, shipment schedule, qualification, utilization, margin and cash bridge rather than battery contract label alone","raw_component_scores_before":{"customer_contract_quality_score":12,"calloff_visibility_score":13,"shipment_schedule_score":11,"qualification_acceptance_score":8,"utilization_score":9,"margin_mix_score":8,"cash_conversion_score":6,"relative_strength_score":14,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"customer_contract_quality_score":15,"calloff_visibility_score":16,"shipment_schedule_score":14,"qualification_acceptance_score":10,"utilization_score":11,"margin_mix_score":10,"cash_conversion_score":8,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Call-off and shipment bridge plus high MFE supports Yellow/Green-candidate watch; exact source-grade evidence and late drawdown block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_R3L90_450080_ECOPRO_MATERIALS_PRECURSOR_REBOUND","trigger_id":"R3L90_C12_450080_20240213_STAGE2_FALSE_POSITIVE_PRECURSOR_REBOUND","symbol":"450080","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"precursor rebound without durable call-off and margin bridge should be blocked","raw_component_scores_before":{"customer_contract_quality_score":3,"calloff_visibility_score":0,"shipment_schedule_score":0,"qualification_acceptance_score":0,"utilization_score":1,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_contract_quality_score":1,"calloff_visibility_score":0,"shipment_schedule_score":0,"qualification_acceptance_score":0,"utilization_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-26,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE convert precursor rebound into missing call-off/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_R3L90_417200_LS_MATERIALS_IPO_EV_THEME","trigger_id":"R3L90_C12_417200_20240102_STAGE2_FALSE_POSITIVE_SUPERCAP_IPO_THEME","symbol":"417200","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"recent-listing EV component theme without customer call-off bridge should remain 4B-watch","raw_component_scores_before":{"customer_contract_quality_score":1,"calloff_visibility_score":0,"shipment_schedule_score":0,"qualification_acceptance_score":0,"utilization_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-18,"theme_spike_risk":-22,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_contract_quality_score":0,"calloff_visibility_score":0,"shipment_schedule_score":0,"qualification_acceptance_score":0,"utilization_score":0,"margin_mix_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-28,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Local MFE is price-only; extreme MAE and missing customer call-off bridge block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L90_C12_P0_CURRENT","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C12 needs explicit customer call-off, shipment, qualification, utilization, margin/cash and recent-listing price-memory taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":25.06,"avg_MAE90_pct":-30.61,"avg_MFE180_pct":25.06,"avg_MAE180_pct":-60.09,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C12_calloff_shipment_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R3L90_C12_P1_SECTOR_SPECIFIC","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_id":"P1_L3_battery_customer_calloff_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 battery contract signals need binding contract, call-off visibility, shipment schedule, qualification, utilization, margin or cash conversion before Stage2-Actionable","changed_axes":["customer_calloff_required","shipment_qualification_required","recent_listing_price_memory_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_calloff_shipment_qualification_utilization_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":25.06,"avg_MAE90_pct":-30.61,"avg_MFE180_pct":25.06,"avg_MAE180_pct":-60.09,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R3L90_C12_P2_CANONICAL","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_id":"P2_C12_calloff_shipment_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C12 should reward call-off-to-shipment mechanics, not battery mega-theme or IPO-cycle labels","changed_axes":["C12_calloff_shipment_margin_cash_bridge_required","C12_precursor_supercap_recent_listing_local_4B_guard","C12_price_only_MFE_not_calloff_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_calloff_or_shipment_plus_utilization_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":25.06,"avg_MAE90_pct":-30.61,"avg_MFE180_pct":25.06,"avg_MAE180_pct":-60.09,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R3L90_C12_P3_COUNTEREXAMPLE_GUARD","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_id":"P3_C12_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If call-off bridge is missing, MFE90<10 or MAE90<=-30 should block Yellow/Green; recent-listing rows require price-memory watch before any patch","changed_axes":["C12_low_MFE_guardrail","C12_deep_MAE_4B_guardrail","C12_recent_listing_watch_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE90_le_minus_30)"},"eligible_trigger_count":3,"avg_MFE90_pct":25.06,"avg_MAE90_pct":-30.61,"avg_MFE180_pct":25.06,"avg_MAE180_pct":-60.09,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_CALLOFF_BRIDGE_POSITIVE_VS_PRECURSOR_SUPERCAP_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":25.06,"avg_MAE90_pct":-30.61,"avg_MFE180_pct":25.06,"avg_MAE180_pct":-60.09,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"recent_listing_watch_count":2,"interpretation":"C12 needs bridge discipline. 강원에너지는 customer call-off/shipment bridge가 있을 때 Yellow-watch가 가능하지만, 에코프로머티 and LS머트리얼즈 show battery mega-theme or IPO-cycle price strength should not be promoted without durable call-off, shipment, utilization, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"114190","trigger_type":"Stage2-Actionable-BatteryEquipmentCustomerCalloffBridge-Positive","entry_date":"2024-01-26","stage2_to_90D_outcome":"good_stage2_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_calloff_bridge_but_late_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when contract strength is tied to call-off, shipment, qualification, utilization and margin bridge; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"450080","trigger_type":"Stage2-FalsePositive-PrecursorMegaThemeRebound-NoDurableCalloffMarginBridge","entry_date":"2024-02-13","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE","stage2_to_180D_outcome":"failed_precursor_rebound_extreme_MAE","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Precursor rebound without durable call-off/margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"417200","trigger_type":"Stage2-FalsePositive-SupercapacitorEVComponentIPOTheme-NoCustomerCalloffBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"price_only_low_MFE_extreme_MAE","stage2_to_180D_outcome":"failed_IPO_EV_component_theme_extreme_MAE","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Recent-listing EV component price strength without customer call-off bridge should be 4B-watch, not positive evidence."}
{"row_type":"residual_contribution","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","residual_type":"battery_precursor_supercap_theme_overcredit_without_customer_calloff_shipment_margin_bridge","contribution":"Adds two C12 4B/recent-listing-watch counterexamples against one battery-equipment call-off bridge positive, avoiding C12 top-covered and recent R3 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_EQUIPMENT_CUSTOMER_CALLOFF_BRIDGE_VS_PRECURSOR_SUPERCAPACITOR_PRICE_ONLY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C12 now has non-top-symbol call-off bridge positive and two recent-listing / mega-theme weak-bridge counterexamples; next R3 C12 loops should exact-URL repair binding contract, call-off, shipment schedule, qualification, utilization, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"C12_calloff_shipment_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"114190 worked when customer call-off/shipment proxy existed; 450080 and 417200 failed when price action lacked durable call-off, shipment, utilization and margin bridge."}
{"row_type":"shadow_weight","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"C12_precursor_supercap_recent_listing_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"450080 and 417200 show recent-listing or mega-theme price strength should remain 4B-watch unless exact call-off evidence is repaired."}
{"row_type":"shadow_weight","round":"R3","loop":"90","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"C12_price_only_MFE_not_calloff_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"Local MFE in 417200 and near-zero MFE in 450080 do not validate C12 without customer call-off and shipment bridge; deep MAE confirms the guard."}
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
  - battery_mega_theme_overcredit
  - recent_listing_price_memory_overcredit
  - customer_calloff_bridge_missing
  - shipment_margin_cash_bridge_missing
new_axis_proposed:
  - C12_calloff_shipment_margin_cash_bridge_required_shadow_only
  - C12_precursor_supercap_recent_listing_local_4B_guard_shadow_only
  - C12_price_only_MFE_not_calloff_validation_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C12
  - full_4b_requires_non_price_evidence within C12
  - hard_4c_thesis_break_routes_to_4c within C12
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
`450080` and `417200` are recent-listing rows; their price paths are usable for calibration, but patch promotion should keep recent-listing price-memory watch.  
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
recent_listing_watch = true for 450080 and 417200
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
3. Confirm R3 / L3 / C12 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C12 top-covered symbols
   - previous R3 loop85 C11 symbols
   - previous R3 loop86 C12 symbols
   - previous R3 loop87 C13 symbols
   - previous R3 loop88 C14 symbols
   - previous R3 loop89 C11 symbols
6. Keep 450080 and 417200 in recent-listing price-memory watch before patch consideration.
7. If aggregate support remains stable after exact evidence URL repair, consider C12-scoped safe patch candidates:
   - C12_calloff_shipment_margin_cash_bridge_required
   - C12_precursor_supercap_recent_listing_local_4B_guard
   - C12_price_only_MFE_not_calloff_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R3
completed_loop = 90
next_round = R4
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.
```

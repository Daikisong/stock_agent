# E2R Stock-Web v12 Residual Research — R3 Loop 91 / L3 / C13

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 91
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: ELECTROLYTE_JV_UTILIZATION_AMPC_BRIDGE_VS_BATTERY_PACKAGING_LITHIUM_MATERIALS_VOCABULARY_DECAY
sector: battery / EV / IRA / AMPC / JV utilization / electrolyte / packaging / lithium materials
output_file: e2r_stock_web_v12_residual_round_R3_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R2 loop 91`.

```text
scheduled_round = R3
scheduled_loop = 91
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

R3 is restricted to battery / EV / green mobility.  
C13 is selected because R3 loop90 used C12 battery customer call-off risk, and the next R3 slot rotates to JV utilization / AMPC / IRA residuals.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA
rows = 23
symbols = 16
good/bad Stage2 = 9/2
4B/4C = 2/0
top-covered = 005070, 020150, 003670, 025900, 348370, 002710
```

This loop avoids the C13 top-covered list and recent R3 loop symbols:

```text
R3 loop85 C11: 078600, 247540, 393890
R3 loop86 C12: 317330, 066970, 361610
R3 loop87 C13: 096770, 011790, 051910
R3 loop88 C14: 093370, 336370, 382840
R3 loop89 C11: 222080, 290670, 089980
R3 loop90 C12: 114190, 450080, 417200
```

Candidate hygiene note:

```text
During this execution path, R2/C07 semiconductor candidate rows were touched in the surrounding tool calls.
Those rows are not used in this R3/C13 output.
```

Selected symbols:

```text
036830, 014820, 095500
```

The selected pocket is:

```text
electrolyte / JV utilization / AMPC bridge positive-control
vs
battery packaging / can-material vocabulary without IRA utilization and margin bridge
vs
lithium-materials / IRA vocabulary rebound without JV utilization, AMPC visibility and cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"036830","company_name":"솔브레인홀딩스","profile_path":"atlas/symbol_profiles/036/036830.json","first_date":"2000-01-18","last_date":"2026-02-20","trading_day_count":6400,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2001-05-28","2004-05-10","2020-08-06","2020-12-30"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"014820","company_name":"동원시스템즈","profile_path":"atlas/symbol_profiles/014/014820.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7741,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1999-04-26","2002-05-31","2005-03-15","2013-01-28"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"095500","company_name":"미래나노텍","profile_path":"atlas/symbol_profiles/095/095500.json","first_date":"2007-10-01","last_date":"2026-02-20","trading_day_count":4535,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2007-10-24","2008-12-02","2009-01-05"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"036830","trigger_type":"Stage2-Actionable-ElectrolyteJVUtilizationAMPCBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C13 symbol/trigger/date combination outside C13 top-covered and recent R3 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"014820","trigger_type":"Stage2-FalsePositive-BatteryPackagingCanMaterialsVocabularyNoIRAUtilizationMarginBridge","entry_date":"2024-03-21","duplicate_status":"new C13 symbol/trigger/date combination outside C13 top-covered and recent R3 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"095500","trigger_type":"Stage2-FalsePositive-LithiumMaterialsIRAVocabularyNoJVUtilizationAMPCBridge","entry_date":"2024-02-29","duplicate_status":"new C13 symbol/trigger/date combination outside C13 top-covered and recent R3 loop symbols; C14 top-covered symbol used here only as a different C13 failure-mode stress case"}
```

## 4. Research question

C13 is not “배터리/IRA/AMPC 단어가 있다.”  
The useful signal must prove a utilization and subsidy-to-margin chain:

```text
JV or overseas production structure
customer offtake / nomination
AMPC or IRA exposure
plant utilization ramp
qualification / shipment acceptance
margin and subsidy recognition
working-capital discipline
cash conversion
```

A JV headline without utilization is a factory gate with the lights on but no shift running. The building exists; E2R needs the production line, customer release, subsidy recognition and cash register.

Residual question:

```text
Can C13 distinguish:
1. electrolyte / JV-utilization / AMPC bridge with very large MFE,
2. battery packaging vocabulary where the market labels it IRA-adjacent but no utilization/margin bridge is repaired,
3. lithium-materials / IRA rebound where price momentum does not prove JV utilization, AMPC visibility or cash conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C13_R3L91_036830_SOLBRAIN_HOLDINGS_ELECTROLYTE_JV","symbol":"036830","company_name":"솔브레인홀딩스","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"ELECTROLYTE_JV_UTILIZATION_AMPC_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ElectrolyteJVUtilizationAMPCBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE90_low_MAE90_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_JV_utilization_AMPC_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Electrolyte/JV utilization proxy produced very high MFE after a low-risk entry. Late-year drawdown keeps Green strict and requires exact customer offtake, AMPC/subsidy recognition, utilization and margin/cash evidence."}
{"row_type":"case","case_id":"C13_R3L91_014820_DONGWON_PACKAGING_CAN_MATERIALS","symbol":"014820","company_name":"동원시스템즈","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_PACKAGING_CAN_MATERIALS_WITHOUT_IRA_UTILIZATION_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-BatteryPackagingCanMaterialsVocabularyNoIRAUtilizationMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_utilization_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_packaging_can_materials_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Battery packaging/can-material vocabulary had only low MFE from the selected late-cycle entry and a sharp drawdown without utilization, customer release, subsidy recognition or margin bridge."}
{"row_type":"case","case_id":"C13_R3L91_095500_MIRAE_NANOTECH_LITHIUM_IRA_VOCABULARY","symbol":"095500","company_name":"미래나노텍","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"LITHIUM_MATERIALS_IRA_VOCABULARY_WITHOUT_JV_UTILIZATION_AMPC_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-LithiumMaterialsIRAVocabularyNoJVUtilizationAMPCBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub_Yellow_MFE_extreme_MAE_no_AMPC_bridge","current_profile_verdict":"current_profile_false_positive_if_lithium_IRA_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Lithium-materials / IRA vocabulary had sub-Yellow MFE and extreme later MAE without customer offtake, JV utilization, AMPC visibility or cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 036830 솔브레인홀딩스 — electrolyte / JV utilization / AMPC bridge positive-control

Entry row: `2024-01-29 c=39550`.  
Observed path: entry-area low `2024-01-29 l=38300`, peak `2024-02-21 h=87800`, and late-year drawdown to `2024-12-09 l=34000`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L91_C13_036830_20240129_STAGE2_ELECTROLYTE_JV_UTILIZATION_AMPC","case_id":"C13_R3L91_036830_SOLBRAIN_HOLDINGS_ELECTROLYTE_JV","symbol":"036830","company_name":"솔브레인홀딩스","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"ELECTROLYTE_JV_UTILIZATION_AMPC_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ElectrolyteJVUtilizationAMPCBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":39550.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_electrolyte_JV_utilization_AMPC_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; electrolyte/JV utilization, customer release, AMPC/IRA subsidy and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["JV_utilization_proxy","electrolyte_customer_ramp_proxy","AMPC_IRA_exposure_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_offtake_pending","utilization_source_pending","AMPC_subsidy_recognition_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036830/2024.csv","profile_path":"atlas/symbol_profiles/036/036830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":122.00,"MFE_90D_pct":122.00,"MFE_180D_pct":122.00,"MAE_30D_pct":-3.16,"MAE_90D_pct":-3.16,"MAE_180D_pct":-14.03,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":87800.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":34000.0,"drawdown_after_peak_pct":-61.28,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_customer_offtake_utilization_AMPC_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE90_low_MAE90_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_JV_utilization_AMPC_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"036830_2024-01-29_39550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C13 can allow Stage2/Yellow when battery strength is tied to JV utilization, customer ramp, AMPC/IRA subsidy recognition, margin and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 014820 동원시스템즈 — packaging/can-material vocabulary without utilization-margin bridge

Entry row: `2024-03-21 c=50700`.  
Observed path: local high `2024-03-21 h=52200`, later full-window high `2024-10-11 h=54200`, but the original entry had fast drawdown to `2024-04-16 l=37100`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L91_C13_014820_20240321_STAGE2_FALSE_POSITIVE_PACKAGING_CAN_MATERIALS","case_id":"C13_R3L91_014820_DONGWON_PACKAGING_CAN_MATERIALS","symbol":"014820","company_name":"동원시스템즈","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"BATTERY_PACKAGING_CAN_MATERIALS_WITHOUT_IRA_UTILIZATION_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;late_rebound_not_entry_validation","trigger_type":"Stage2-FalsePositive-BatteryPackagingCanMaterialsVocabularyNoIRAUtilizationMarginBridge","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":50700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_battery_packaging_can_materials_IRA_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; packaging/can-material IRA-adjacent vocabulary treated as insufficient without customer release, utilization ramp, subsidy recognition, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["battery_packaging_vocabulary","can_materials_IRA_keyword","relative_strength_spike"],"stage3_evidence_fields":["JV_utilization_missing","customer_release_missing","AMPC_subsidy_recognition_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE_watch","late_rebound_not_entry_validation","utilization_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014820/2024.csv","profile_path":"atlas/symbol_profiles/014/014820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.96,"MFE_90D_pct":2.96,"MFE_180D_pct":6.90,"MAE_30D_pct":-26.82,"MAE_90D_pct":-26.82,"MAE_180D_pct":-26.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-11","peak_price":54200.0,"max_drawdown_low_date":"2024-04-16","max_drawdown_low":37100.0,"drawdown_after_peak_pct":-31.55,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.43,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"packaging_can_materials_vocabulary_without_JV_utilization_AMPC_margin_bridge_should_be_4B_watch_not_positive; late_Q4_rebound_not_original_entry_validation","four_b_evidence_type":["low_MFE","late_rebound_not_entry_validation","utilization_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_utilization_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_packaging_can_materials_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"014820_2024-03-21_50700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C13 should not count packaging/can-material vocabulary as AMPC/JV utilization evidence. Customer release, utilization ramp, subsidy recognition, margin and cash bridge must be repaired before Yellow/Green."}
```

### 6.3 095500 미래나노텍 — lithium-materials / IRA vocabulary without JV utilization and AMPC bridge

Entry row: `2024-02-29 c=22350`.  
Observed path: high `2024-03-07 h=25250`, then persistent decline to `2024-12-09 l=7000`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L91_C13_095500_20240229_STAGE2_FALSE_POSITIVE_LITHIUM_IRA_VOCABULARY","case_id":"C13_R3L91_095500_MIRAE_NANOTECH_LITHIUM_IRA_VOCABULARY","symbol":"095500","company_name":"미래나노텍","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"LITHIUM_MATERIALS_IRA_VOCABULARY_WITHOUT_JV_UTILIZATION_AMPC_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-LithiumMaterialsIRAVocabularyNoJVUtilizationAMPCBridge","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":22350.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_lithium_materials_IRA_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; lithium-materials/IRA vocabulary treated as insufficient without JV utilization, customer offtake, AMPC/subsidy visibility, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["lithium_materials_keyword","IRA_vocabulary","relative_strength_spike"],"stage3_evidence_fields":["JV_utilization_missing","customer_offtake_missing","AMPC_visibility_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["sub_Yellow_MFE","AMPC_bridge_missing_watch","extreme_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095500/2024.csv","profile_path":"atlas/symbol_profiles/095/095500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.98,"MFE_90D_pct":12.98,"MFE_180D_pct":12.98,"MAE_30D_pct":-19.46,"MAE_90D_pct":-29.71,"MAE_180D_pct":-68.68,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":25250.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":7000.0,"drawdown_after_peak_pct":-72.28,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"lithium_materials_IRA_vocabulary_without_JV_utilization_AMPC_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["sub_Yellow_MFE","AMPC_bridge_missing_watch","extreme_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE_extreme_MAE_no_AMPC_bridge","current_profile_verdict":"current_profile_false_positive_if_lithium_IRA_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"095500_2024-02-29_22350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C13 should not promote lithium/IRA vocabulary unless JV utilization, customer offtake, AMPC visibility, margin and cash conversion are repaired. Sub-Yellow MFE and extreme MAE force Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L91_036830_SOLBRAIN_HOLDINGS_ELECTROLYTE_JV","trigger_id":"R3L91_C13_036830_20240129_STAGE2_ELECTROLYTE_JV_UTILIZATION_AMPC","symbol":"036830","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C13 requires JV/utilization, customer ramp, AMPC/IRA recognition, margin and cash bridge rather than battery/IRA label alone","raw_component_scores_before":{"JV_structure_score":12,"utilization_ramp_score":13,"customer_offtake_score":11,"AMPC_IRA_visibility_score":12,"qualification_shipment_score":9,"margin_bridge_score":10,"cash_conversion_score":7,"relative_strength_score":16,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"JV_structure_score":15,"utilization_ramp_score":16,"customer_offtake_score":14,"AMPC_IRA_visibility_score":15,"qualification_shipment_score":11,"margin_bridge_score":12,"cash_conversion_score":9,"relative_strength_score":17,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":89,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"JV/utilization/AMPC bridge plus very high MFE supports Yellow/Green-candidate watch; exact offtake, utilization and subsidy recognition evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L91_014820_DONGWON_PACKAGING_CAN_MATERIALS","trigger_id":"R3L91_C13_014820_20240321_STAGE2_FALSE_POSITIVE_PACKAGING_CAN_MATERIALS","symbol":"014820","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_scope":"current_default_proxy","profile_hypothesis":"battery packaging/can-material vocabulary without utilization and AMPC margin bridge should be blocked","raw_component_scores_before":{"JV_structure_score":1,"utilization_ramp_score":0,"customer_offtake_score":1,"AMPC_IRA_visibility_score":1,"qualification_shipment_score":1,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":7,"valuation_repricing_score":3,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"JV_structure_score":0,"utilization_ramp_score":0,"customer_offtake_score":0,"AMPC_IRA_visibility_score":0,"qualification_shipment_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and quick MAE expansion convert battery-packaging vocabulary into missing utilization/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C13_R3L91_095500_MIRAE_NANOTECH_LITHIUM_IRA_VOCABULARY","trigger_id":"R3L91_C13_095500_20240229_STAGE2_FALSE_POSITIVE_LITHIUM_IRA_VOCABULARY","symbol":"095500","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_scope":"current_default_proxy","profile_hypothesis":"lithium-materials/IRA vocabulary without JV utilization and AMPC recognition should remain Watch/4B","raw_component_scores_before":{"JV_structure_score":0,"utilization_ramp_score":0,"customer_offtake_score":1,"AMPC_IRA_visibility_score":1,"qualification_shipment_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-18,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"JV_structure_score":0,"utilization_ramp_score":0,"customer_offtake_score":0,"AMPC_IRA_visibility_score":0,"qualification_shipment_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-28,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-Yellow MFE and extreme MAE require utilization, offtake, AMPC and cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L91_C13_P0_CURRENT","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C13 needs explicit JV/utilization, offtake, AMPC recognition, margin/cash and late-rebound taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":45.98,"avg_MAE90_pct":-19.90,"avg_MFE180_pct":47.29,"avg_MAE180_pct":-36.51,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.81,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C13_JV_utilization_AMPC_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R3L91_C13_P1_SECTOR_SPECIFIC","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P1_L3_JV_utilization_AMPC_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 battery JV/IRA signals need utilization, customer offtake, qualification/shipment, subsidy recognition, margin or cash conversion before Stage2-Actionable","changed_axes":["JV_utilization_required","AMPC_subsidy_recognition_required","battery_materials_vocabulary_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_JV_utilization_customer_offtake_AMPC_qualification_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":45.98,"avg_MAE90_pct":-19.90,"avg_MFE180_pct":47.29,"avg_MAE180_pct":-36.51,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R3L91_C13_P2_CANONICAL","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P2_C13_JV_utilization_AMPC_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C13 should reward utilization-to-subsidy-to-margin mechanics, not battery/IRA vocabulary","changed_axes":["C13_JV_utilization_AMPC_margin_cash_bridge_required","C13_packaging_lithium_vocabulary_local_4B_guard","C13_late_rebound_not_entry_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"JV_or_utilization_plus_AMPC_or_margin_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":45.98,"avg_MAE90_pct":-19.90,"avg_MFE180_pct":47.29,"avg_MAE180_pct":-36.51,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R3L91_C13_P3_COUNTEREXAMPLE_GUARD","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","profile_id":"P3_C13_sub20_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If JV/utilization/AMPC bridge is missing, MFE90<20 or MAE90<=-20 should block Yellow/Green; MAE180<=-50 hard-routes to 4B-watch","changed_axes":["C13_sub20_MFE_guardrail","C13_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_20_or_MAE90_le_minus_20); hard_watch_if_MAE180_le_minus_50"},"eligible_trigger_count":3,"avg_MFE90_pct":45.98,"avg_MAE90_pct":-19.90,"avg_MFE180_pct":47.29,"avg_MAE180_pct":-36.51,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_ELECTROLYTE_JV_POSITIVE_VS_PACKAGING_LITHIUM_VOCABULARY_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":45.98,"avg_MAE90_pct":-19.90,"avg_MFE180_pct":47.29,"avg_MAE180_pct":-36.51,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE90_le_minus20":0.33,"interpretation":"C13 needs bridge discipline. 솔브레인홀딩스 shows electrolyte/JV utilization/AMPC bridge can support Yellow/Green-candidate-watch, while 동원시스템즈 and 미래나노텍 show battery packaging or lithium/IRA vocabulary should not be promoted without utilization, customer offtake, AMPC recognition, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"036830","trigger_type":"Stage2-Actionable-ElectrolyteJVUtilizationAMPCBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_very_high_MFE_low_MAE90","stage2_to_180D_outcome":"positive_JV_utilization_AMPC_bridge_but_late_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when battery strength is tied to JV utilization, customer offtake, AMPC/subsidy recognition, margin and cash bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"014820","trigger_type":"Stage2-FalsePositive-BatteryPackagingCanMaterialsVocabularyNoIRAUtilizationMarginBridge","entry_date":"2024-03-21","stage2_to_90D_outcome":"bad_stage2_low_MFE_quick_MAE_expansion","stage2_to_180D_outcome":"failed_packaging_can_materials_vocabulary_no_utilization_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Battery packaging/can-material vocabulary without utilization and margin bridge should stay Watch/4B-risk; late Q4 rebound does not validate original entry."}
{"row_type":"stage_transition_summary","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"095500","trigger_type":"Stage2-FalsePositive-LithiumMaterialsIRAVocabularyNoJVUtilizationAMPCBridge","entry_date":"2024-02-29","stage2_to_90D_outcome":"bad_stage2_sub_Yellow_MFE_deep_MAE","stage2_to_180D_outcome":"failed_lithium_IRA_vocabulary_extreme_MAE","MFE90_ge20":false,"MAE180_le_minus50":true,"transition_note":"Lithium/IRA vocabulary without JV utilization, AMPC visibility and cash bridge should be 4B-watch, not positive C13 evidence."}
{"row_type":"residual_contribution","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","residual_type":"battery_materials_IRA_vocabulary_overcredit_without_JV_utilization_AMPC_margin_cash_bridge","contribution":"Adds two C13 4B counterexamples against one electrolyte/JV utilization positive, avoiding C13 top-covered and recent R3 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"ELECTROLYTE_JV_UTILIZATION_AMPC_BRIDGE_VS_BATTERY_PACKAGING_LITHIUM_MATERIALS_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C13 now has non-top-symbol electrolyte/JV utilization positive and two battery-materials vocabulary weak-bridge counterexamples; next R3 C13 loops should exact-URL repair JV structure, customer offtake, utilization, AMPC/subsidy recognition, qualification/shipment, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_JV_utilization_AMPC_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"036830 worked when electrolyte/JV utilization/AMPC proxy existed; 014820 and 095500 failed when battery-materials vocabulary lacked utilization, offtake, subsidy recognition and margin/cash bridge."}
{"row_type":"shadow_weight","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_packaging_lithium_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Packaging/can-material and lithium-material rows showed low or sub-Yellow MFE with deep MAE when non-price JV/AMPC evidence was missing."}
{"row_type":"shadow_weight","round":"R3","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_late_rebound_not_entry_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"014820 shows a later Q4 rebound should not retroactively validate a weak original C13 entry unless a fresh trigger and fresh utilization/AMPC evidence exist."}
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
  - battery_materials_vocabulary_overcredit
  - packaging_can_materials_IRA_keyword_overcredit
  - lithium_materials_IRA_vocabulary_overcredit
  - JV_utilization_AMPC_bridge_missing
  - margin_cash_bridge_missing
new_axis_proposed:
  - C13_JV_utilization_AMPC_margin_cash_bridge_required_shadow_only
  - C13_packaging_lithium_vocabulary_local_4B_guard_shadow_only
  - C13_late_rebound_not_entry_validation_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C13
  - full_4b_requires_non_price_evidence within C13
  - hard_4c_thesis_break_routes_to_4c within C13
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
All three selected symbols have older corporate-action or name-transition candidates before 2024; those candidates are outside the selected windows and do not contaminate this residual price-path analysis.  
`095500` is a known C14 top-covered symbol, but this run uses it only as a different C13 failure-mode stress case, not as a duplicate C14 contribution.  
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
3. Confirm R3 / L3 / C13 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C13 top-covered symbols
   - previous R3 loop85 C11 symbols
   - previous R3 loop86 C12 symbols
   - previous R3 loop87 C13 symbols
   - previous R3 loop88 C14 symbols
   - previous R3 loop89 C11 symbols
   - previous R3 loop90 C12 symbols
6. Confirm accidentally touched R2/C07 candidate rows are not ingested from this MD.
7. Treat 095500 as C13 failure-mode stress only, not as a duplicate C14 contribution.
8. If aggregate support remains stable after exact evidence URL repair, consider C13-scoped safe patch candidates:
   - C13_JV_utilization_AMPC_margin_cash_bridge_required
   - C13_packaging_lithium_vocabulary_local_4B_guard
   - C13_late_rebound_not_entry_validation_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R3
completed_loop = 91
next_round = R4
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R3/L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA.
```

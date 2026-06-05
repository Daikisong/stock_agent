# E2R Stock-Web v12 Residual Research — R9 Loop 91 / L3 / C29

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R9
loop: 91
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: HYBRID_AUTO_PARTS_CUSTOMER_VOLUME_MIX_BRIDGE_VS_CHASSIS_CASTING_LEGACY_AUTOPARTS_DECAY
sector: mobility / auto parts / hybrid vehicle / fuel tank / chassis / casting / OEM customer volume / margin / operating leverage
output_file: e2r_stock_web_v12_residual_round_R9_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R8 loop 91`.

```text
scheduled_round = R9
scheduled_loop = 91
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

R9 is the mobility / auto-parts / EV operating-leverage lane.  
C29 remains the correct R9 archetype because this lane continues the mobility volume / margin / operating-leverage residual set.

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
R9 loop90: 092780, 126640, 013870
earlier known C29: 012330, 002350, 204320
```

Candidate hygiene note:

```text
During this execution path, a few unused candidate rows such as 009680 and unrelated prior-sector rows were touched while checking price paths.
Those rows are not used in this R9/C29 output.
```

Selected symbols:

```text
123410, 033250, 012280
```

The selected pocket is:

```text
hybrid auto-parts customer volume / program-mix bridge
vs
chassis-parts vocabulary without OEM customer volume and margin bridge
vs
casting auto-parts rebound without utilization / pricing / working-capital bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"123410","company_name":"코리아에프티","profile_path":"atlas/symbol_profiles/123/123410.json","first_date":"2010-08-27","last_date":"2026-02-20","trading_day_count":3763,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2012-03-02"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical SPAC/name-transition candidate exists long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"033250","company_name":"체시스","profile_path":"atlas/symbol_profiles/033/033250.json","first_date":"1999-08-11","last_date":"2026-02-20","trading_day_count":6535,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2001-02-06","2001-03-19","2015-12-16","2021-02-02"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"012280","company_name":"영화금속","profile_path":"atlas/symbol_profiles/012/012280.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7654,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1999-07-12","2001-04-23","2001-06-04"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"123410","trigger_type":"Stage2-Actionable-HybridAutoPartsCustomerVolumeMixBridge-Positive","entry_date":"2024-01-22","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"033250","trigger_type":"Stage2-FalsePositive-ChassisPartsVocabularyNoOEMVolumeMarginBridge","entry_date":"2024-01-02","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"012280","trigger_type":"Stage2-FalsePositive-CastingAutoPartsReboundNoUtilizationPricingCashBridge","entry_date":"2024-01-11","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
```

## 4. Research question

C29 is not “자동차 부품주가 움직였다.”  
The useful mobility operating-leverage signal must prove the operating chain:

```text
fresh OEM/customer volume
program mix or model exposure
hybrid/EV platform exposure
utilization recovery
price/cost pass-through
margin bridge
working-capital discipline
cash conversion
```

A parts-supplier headline without this bridge is a driveshaft spinning on the bench. The motion is visible, but no torque reaches the road until OEM volume, utilization, margin, and cash conversion engage.

Residual question:

```text
Can C29 distinguish:
1. hybrid auto-parts volume/program-mix bridge with high MFE and shallow entry MAE,
2. chassis-parts vocabulary with only a local spike and no OEM volume / margin bridge,
3. casting auto-parts rebound where no utilization, pricing, working-capital or cash bridge exists?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C29_R9L91_123410_KOREA_FT_HYBRID_VOLUME_MIX","symbol":"123410","company_name":"코리아에프티","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"HYBRID_AUTOPARTS_CUSTOMER_VOLUME_PROGRAM_MIX_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-HybridAutoPartsCustomerVolumeMixBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE90_low_MAE_customer_volume_mix_bridge","current_profile_verdict":"current_profile_correct_if_OEM_volume_program_mix_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Hybrid auto-parts / customer volume and program-mix proxy produced high MFE with shallow entry MAE. Green still requires exact OEM/customer volume, program mix, utilization, margin and cash evidence."}
{"row_type":"case","case_id":"C29_R9L91_033250_CHASYS_CHASSIS_PARTS_DECAY","symbol":"033250","company_name":"체시스","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CHASSIS_PARTS_VOCABULARY_WITHOUT_OEM_VOLUME_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ChassisPartsVocabularyNoOEMVolumeMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_OEM_volume_bridge","current_profile_verdict":"current_profile_false_positive_if_chassis_parts_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Chassis parts vocabulary had only a same-day local high and then deep MAE without fresh OEM/customer volume, utilization, program mix, margin or cash bridge."}
{"row_type":"case","case_id":"C29_R9L91_012280_YOUNGWHA_CASTING_AUTOPARTS","symbol":"012280","company_name":"영화금속","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CASTING_AUTOPARTS_REBOUND_WITHOUT_UTILIZATION_PRICING_CASH_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CastingAutoPartsReboundNoUtilizationPricingCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_no_utilization_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_casting_autoparts_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Casting auto-parts rebound had near-zero MFE and later MAE expansion without utilization recovery, price/cost pass-through, margin or working-capital bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 123410 코리아에프티 — hybrid auto-parts customer volume / program-mix bridge positive-control

Entry row: `2024-01-22 c=3855`.  
Observed path: entry-area low `2024-01-22 l=3650`, peak `2024-04-26 h=8190`, and late-year low after peak around `2024-12-30 l=4225`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L91_C29_123410_20240122_STAGE2_HYBRID_VOLUME_MIX","case_id":"C29_R9L91_123410_KOREA_FT_HYBRID_VOLUME_MIX","symbol":"123410","company_name":"코리아에프티","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"HYBRID_AUTOPARTS_CUSTOMER_VOLUME_PROGRAM_MIX_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-HybridAutoPartsCustomerVolumeMixBridge-Positive","trigger_date":"2024-01-22","entry_date":"2024-01-22","entry_price":3855.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_hybrid_autoparts_customer_volume_program_mix_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; hybrid vehicle parts, customer volume, program mix, utilization and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["OEM_customer_volume_proxy","hybrid_program_mix_proxy","utilization_recovery_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_volume_source_pending","program_mix_source_pending","margin_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/123/123410/2024.csv","profile_path":"atlas/symbol_profiles/123/123410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":68.09,"MFE_90D_pct":112.45,"MFE_180D_pct":112.45,"MAE_30D_pct":-5.32,"MAE_90D_pct":-5.32,"MAE_180D_pct":-5.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-26","peak_price":8190.0,"max_drawdown_low_date":"2024-12-30","max_drawdown_low":4225.0,"drawdown_after_peak_pct":-48.41,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.81,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_OEM_volume_program_mix_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_low_MAE_customer_volume_mix_bridge","current_profile_verdict":"current_profile_correct_if_OEM_volume_program_mix_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_SPAC_transition_pre_2024; selected_window_clean","same_entry_group_id":"123410_2024-01-22_3855","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 can allow Stage2/Yellow when mobility strength is tied to OEM/customer volume, hybrid program mix, utilization, margin and cash conversion. Green requires exact source-grade evidence."}
```

### 6.2 033250 체시스 — chassis-parts vocabulary without OEM/customer-volume and margin bridge

Entry row: `2024-01-02 c=1863`.  
Observed path: same-day high `2024-01-02 h=1970`, then deep drawdown to `2024-12-27 l=1060`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L91_C29_033250_20240102_STAGE2_FALSE_POSITIVE_CHASSIS_PARTS","case_id":"C29_R9L91_033250_CHASYS_CHASSIS_PARTS_DECAY","symbol":"033250","company_name":"체시스","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CHASSIS_PARTS_VOCABULARY_WITHOUT_OEM_VOLUME_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-ChassisPartsVocabularyNoOEMVolumeMarginBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":1863.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_chassis_parts_autoparts_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; chassis auto-parts vocabulary treated as insufficient without fresh OEM/customer volume, utilization recovery, program mix, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["chassis_parts_keyword","legacy_autoparts_rebound"],"stage3_evidence_fields":["fresh_OEM_volume_missing","program_mix_missing","utilization_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE","OEM_volume_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033250/2024.csv","profile_path":"atlas/symbol_profiles/033/033250.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.74,"MFE_90D_pct":5.74,"MFE_180D_pct":5.74,"MAE_30D_pct":-22.11,"MAE_90D_pct":-39.88,"MAE_180D_pct":-43.10,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":1970.0,"max_drawdown_low_date":"2024-12-27","max_drawdown_low":1060.0,"drawdown_after_peak_pct":-46.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"chassis_parts_vocabulary_without_OEM_volume_program_mix_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","OEM_volume_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_OEM_volume_bridge","current_profile_verdict":"current_profile_false_positive_if_chassis_parts_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"033250_2024-01-02_1863","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not promote chassis-parts vocabulary without fresh OEM/customer volume, program mix, utilization, margin and cash evidence. Low MFE and deep MAE require Watch/4B routing."}
```

### 6.3 012280 영화금속 — casting auto-parts rebound without utilization / pricing / cash bridge

Entry row: `2024-01-11 c=989`.  
Observed path: high `2024-02-01 h=1000`, then drawdown to `2024-10-24 l=736`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L91_C29_012280_20240111_STAGE2_FALSE_POSITIVE_CASTING_AUTOPARTS","case_id":"C29_R9L91_012280_YOUNGWHA_CASTING_AUTOPARTS","symbol":"012280","company_name":"영화금속","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CASTING_AUTOPARTS_REBOUND_WITHOUT_UTILIZATION_PRICING_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-CastingAutoPartsReboundNoUtilizationPricingCashBridge","trigger_date":"2024-01-11","entry_date":"2024-01-11","entry_price":989.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_casting_auto_parts_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; casting auto-parts rebound treated as insufficient without utilization recovery, customer volume, price/cost pass-through, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["casting_autoparts_keyword","legacy_autoparts_rebound"],"stage3_evidence_fields":["customer_volume_missing","utilization_recovery_missing","price_cost_pass_through_missing","working_capital_cash_missing"],"stage4b_evidence_fields":["near_zero_MFE","utilization_pricing_bridge_missing_watch","MAE_expansion"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012280/2024.csv","profile_path":"atlas/symbol_profiles/012/012280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.11,"MFE_90D_pct":1.11,"MFE_180D_pct":1.11,"MAE_30D_pct":-14.05,"MAE_90D_pct":-14.05,"MAE_180D_pct":-25.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-01","peak_price":1000.0,"max_drawdown_low_date":"2024-10-24","max_drawdown_low":736.0,"drawdown_after_peak_pct":-26.40,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"casting_autoparts_rebound_without_utilization_pricing_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","utilization_pricing_bridge_missing_watch","MAE_expansion"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_utilization_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_casting_autoparts_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"012280_2024-01-11_989","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not equate casting/legacy auto-parts vocabulary with operating leverage. Customer volume, utilization recovery, price/cost pass-through, margin and cash bridge must be repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L91_123410_KOREA_FT_HYBRID_VOLUME_MIX","trigger_id":"R9L91_C29_123410_20240122_STAGE2_HYBRID_VOLUME_MIX","symbol":"123410","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C29 requires OEM/customer volume, hybrid program mix, utilization recovery, margin and cash bridge rather than auto-parts label alone","raw_component_scores_before":{"customer_volume_score":13,"program_mix_score":13,"hybrid_platform_score":12,"operating_leverage_score":12,"utilization_score":10,"margin_bridge_score":10,"cash_conversion_score":7,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"customer_volume_score":16,"program_mix_score":16,"hybrid_platform_score":15,"operating_leverage_score":15,"utilization_score":12,"margin_bridge_score":12,"cash_conversion_score":9,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":88,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Hybrid/OEM volume and program-mix bridge plus high MFE supports Yellow/Green-candidate watch; exact customer-volume and margin evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L91_033250_CHASYS_CHASSIS_PARTS_DECAY","trigger_id":"R9L91_C29_033250_20240102_STAGE2_FALSE_POSITIVE_CHASSIS_PARTS","symbol":"033250","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"chassis-parts vocabulary without fresh OEM/customer volume and margin bridge should be blocked","raw_component_scores_before":{"customer_volume_score":1,"program_mix_score":1,"hybrid_platform_score":0,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_volume_score":0,"program_mix_score":0,"hybrid_platform_score":0,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE convert chassis-parts vocabulary into missing OEM-volume bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L91_012280_YOUNGWHA_CASTING_AUTOPARTS","trigger_id":"R9L91_C29_012280_20240111_STAGE2_FALSE_POSITIVE_CASTING_AUTOPARTS","symbol":"012280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"casting/legacy auto-parts rebound without utilization and price/cost bridge should remain Watch/4B","raw_component_scores_before":{"customer_volume_score":1,"program_mix_score":0,"hybrid_platform_score":0,"operating_leverage_score":0,"utilization_score":1,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_volume_score":0,"program_mix_score":0,"hybrid_platform_score":0,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_repricing_score":0,"execution_risk_score":-20,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and MAE expansion require utilization, price/cost pass-through, margin and cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R9L91_C29_P0_CURRENT","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C29 needs explicit OEM/customer volume, program mix, platform exposure, utilization, price/cost, margin/cash and legacy-autoparts 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":39.77,"avg_MAE90_pct":-19.75,"avg_MFE180_pct":39.77,"avg_MAE180_pct":-24.67,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.94,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C29_OEM_volume_mix_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R9L91_C29_P1_SECTOR_SPECIFIC","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P1_L3_mobility_volume_mix_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 mobility signals need customer volume, program mix, hybrid/EV platform exposure, utilization, operating leverage, margin or cash conversion before Stage2-Actionable","changed_axes":["customer_volume_required","program_mix_platform_required","legacy_autoparts_vocabulary_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_volume_program_mix_platform_utilization_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":39.77,"avg_MAE90_pct":-19.75,"avg_MFE180_pct":39.77,"avg_MAE180_pct":-24.67,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R9L91_C29_P2_CANONICAL","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P2_C29_OEM_volume_program_mix_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C29 should reward customer-volume-to-margin mechanics, not chassis/casting auto-parts vocabulary","changed_axes":["C29_OEM_volume_program_mix_margin_cash_bridge_required","C29_chassis_casting_legacy_autoparts_local_4B_guard","C29_low_MFE_not_operating_leverage_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_volume_or_program_mix_plus_utilization_or_margin_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":39.77,"avg_MAE90_pct":-19.75,"avg_MFE180_pct":39.77,"avg_MAE180_pct":-24.67,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R9L91_C29_P3_COUNTEREXAMPLE_GUARD","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P3_C29_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If OEM volume/margin bridge is missing, MFE90<10 or MAE90<=-20 should block Yellow/Green and route to Watch/4B","changed_axes":["C29_low_MFE_guardrail","C29_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE90_le_minus_20)"},"eligible_trigger_count":3,"avg_MFE90_pct":39.77,"avg_MAE90_pct":-19.75,"avg_MFE180_pct":39.77,"avg_MAE180_pct":-24.67,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_HYBRID_AUTOPARTS_POSITIVE_VS_CHASSIS_CASTING_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":39.77,"avg_MAE90_pct":-19.75,"avg_MFE180_pct":39.77,"avg_MAE180_pct":-24.67,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MFE90_lt10":0.67,"interpretation":"C29 needs bridge discipline. 코리아에프티 shows hybrid auto-parts customer volume/program-mix bridge can support Yellow/Green-candidate-watch, while 체시스 and 영화금속 show chassis/casting/legacy auto-parts vocabulary should not be promoted without fresh OEM volume, utilization, price/cost pass-through, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"123410","trigger_type":"Stage2-Actionable-HybridAutoPartsCustomerVolumeMixBridge-Positive","entry_date":"2024-01-22","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_hybrid_OEM_volume_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when OEM/customer volume, hybrid program mix, utilization and margin/cash bridge exists; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"033250","trigger_type":"Stage2-FalsePositive-ChassisPartsVocabularyNoOEMVolumeMarginBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_chassis_parts_vocabulary_no_OEM_volume_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Chassis-parts vocabulary without fresh OEM volume and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"012280","trigger_type":"Stage2-FalsePositive-CastingAutoPartsReboundNoUtilizationPricingCashBridge","entry_date":"2024-01-11","stage2_to_90D_outcome":"weak_stage2_near_zero_MFE_bridge_missing","stage2_to_180D_outcome":"failed_casting_autoparts_rebound_MAE_expansion","MFE90_ge20":false,"MAE180_le_minus20":true,"transition_note":"Casting auto-parts rebound without utilization, pricing and cash bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"chassis_casting_legacy_autoparts_vocabulary_overcredit_without_OEM_volume_mix_margin_cash_bridge","contribution":"Adds two C29 4B counterexamples against one hybrid auto-parts OEM-volume positive, avoiding C29 top-covered and previous C29 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"HYBRID_AUTO_PARTS_CUSTOMER_VOLUME_MIX_BRIDGE_VS_CHASSIS_CASTING_LEGACY_AUTOPARTS_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C29 now has non-top-symbol hybrid auto-parts customer-volume positive and two chassis/casting weak-bridge counterexamples; next R9 loops should exact-URL repair OEM/customer volume, hybrid/EV platform mix, utilization, price/cost pass-through, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_OEM_volume_program_mix_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"123410 worked when hybrid auto-parts customer-volume/program-mix proxy existed; 033250 and 012280 failed when legacy auto-parts vocabulary lacked OEM volume, utilization and margin bridge."}
{"row_type":"shadow_weight","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_chassis_casting_legacy_autoparts_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Chassis and casting auto-parts rows showed MFE90 below 10 and later MAE expansion when non-price OEM volume/margin evidence was missing."}
{"row_type":"shadow_weight","round":"R9","loop":"91","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_low_MFE_not_operating_leverage_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"033250 and 012280 show low MFE cannot validate operating leverage unless customer volume, utilization and margin/cash evidence are repaired."}
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
  - chassis_parts_vocabulary_overcredit
  - casting_autoparts_rebound_overcredit
  - OEM_customer_volume_bridge_missing
  - utilization_pricing_margin_cash_bridge_missing
new_axis_proposed:
  - C29_OEM_volume_program_mix_margin_cash_bridge_required_shadow_only
  - C29_chassis_casting_legacy_autoparts_local_4B_guard_shadow_only
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
`123410` has an old SPAC/name-transition candidate before 2024.  
`033250` and `012280` have historical corporate-action/name-transition candidates before 2024.  
Those candidates are outside the selected 2024 windows and do not contaminate this residual price-path analysis.  
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
   - previous R9 loop90 symbols
   - earlier known C29 symbols listed in this MD
6. Confirm accidentally touched 009680 and earlier-sector candidate rows are not ingested from this MD.
7. If aggregate support remains stable after exact evidence URL repair, consider C29-scoped safe patch candidates:
   - C29_OEM_volume_program_mix_margin_cash_bridge_required
   - C29_chassis_casting_legacy_autoparts_local_4B_guard
   - C29_low_MFE_not_operating_leverage_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R9
completed_loop = 91
next_round = R10
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.
```

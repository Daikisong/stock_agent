# E2R Stock-Web v12 Residual Research — R3 Loop 93 / L3 / C12

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R3
loop: 93
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: CELL_CUSTOMER_CALLOFF_STABILIZATION_VS_PREMIUM_CELL_AND_CATHODE_CONTRACT_VOCABULARY_DECAY
sector: battery / EV / customer contract / call-off / demand risk / cell maker / cathode material / ASP / utilization / margin / FCF
output_file: e2r_stock_web_v12_residual_round_R3_loop_93_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after recent loop93 expansions in C09, C01, C07, C06, C10, C11, C19, C27 and C24.

```text
selected_round = R3
selected_loop = 93
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

Reason for selecting C12:

```text
v12 scheduler = coverage_index_first
sequential_round_cycle_required = false
coverage_gap_can_override_previous_round = true
selected_archetype_drives_round = true
```

No-Repeat Index Priority 0 snapshot used as duplicate-avoidance ledger:

```text
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK = 27 rows / need_to_30 = 3
C13_BATTERY_JV_UTILIZATION_AMPC_IRA = 27 rows / need_to_30 = 3
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION = 27 rows / need_to_30 = 3
```

C12 can reach the 30-row stability threshold with exactly three additional representative rows. This loop avoids recent R3 symbols:

```text
R3 loop85 C11: 078600, 247540, 393890
R3 loop86 C12: 317330, 066970, 361610
R3 loop87 C13: 096770, 011790, 051910
R3 loop88 C14: 093370, 336370, 382840
R3 loop89 C11: 222080, 290670, 089980
R3 loop90 C12: 114190, 450080, 417200
R3 loop91 C13: 036830, 014820, 095500
R3 loop92 C14: 006110, 101360, 282880
R3 loop93 C11: 348370, 121600, 020150
```

Candidate hygiene note:

```text
During this execution path, C24 and earlier C27/C19/C11 candidates were touched in the stream.
They are excluded from this C12 output because the valid output must be R3/L3/C12.
```

Selected symbols:

```text
373220, 006400, 005070
```

The selected pocket is:

```text
large-cell customer call-off stabilization / contract-visibility positive-watch after a reset
vs
premium cylindrical/prismatic cell customer contract vocabulary where call-off/demand pressure returns
vs
cathode material customer contract vocabulary where ASP/mix/FCF bridge fails after a price spike
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"373220","company_name":"LG에너지솔루션","profile_path":"atlas/symbol_profiles/373/373220.json","first_date":"2022-01-27","last_date":"2026-02-20","trading_day_count":992,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"006400","company_name":"삼성SDI","profile_path":"atlas/symbol_profiles/006/006400.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7762,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1996-01-03","1998-11-03","2014-07-15"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
{"row_type":"price_source_validation","symbol":"005070","company_name":"코스모신소재","profile_path":"atlas/symbol_profiles/005/005070.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7706,"corporate_action_candidate_count":8,"corporate_action_candidate_dates":["2000-01-13","2001-02-02","2001-03-30","2002-07-02","2003-01-30","2005-05-04","2008-01-22","2019-11-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"373220","trigger_type":"Stage2-Actionable-LargeCellCustomerCalloffStabilizationContractVisibilityBridge-PositiveWatch","entry_date":"2024-09-10","duplicate_status":"new C12 symbol/trigger/date combination outside recent R3 C11/C12/C13/C14 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"006400","trigger_type":"Stage2-FalsePositive-PremiumCellCustomerContractVocabularyCalloffDemandPressure","entry_date":"2024-03-12","duplicate_status":"new C12 symbol/trigger/date combination outside recent R3 C11/C12/C13/C14 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"005070","trigger_type":"Stage2-FalsePositive-CathodeCustomerContractVocabularyNoASPFCFBridgeAfterSpike","entry_date":"2024-02-20","duplicate_status":"new C12 symbol/trigger/date combination outside recent R3 C11/C12/C13/C14 symbols"}
```

## 4. Research question

C12 is not “고객 계약이 있다.”
The useful customer-contract signal must prove the contract-to-cash chain:

```text
contract quality and customer identity
call-off / offtake schedule visibility
actual shipment conversion
ASP or pass-through discipline
utilization and yield
working-capital discipline
gross-margin / operating-margin bridge
FCF conversion
demand slowdown / deferral / cancellation risk containment
```

A battery contract headline without call-off visibility is an order form in a drawer. E2R needs the customer actually pulling volume, paying the price, and leaving margin/cash behind.

Residual question:

```text
Can C12 distinguish:
1. large-cell customer call-off stabilization after a reset that deserves only positive-watch,
2. premium-cell customer contract vocabulary that fails when EV demand/call-off pressure returns,
3. cathode material contract vocabulary that fails when ASP/mix/FCF bridge breaks after a spike?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C12_R3L93_373220_LGES_CALLOFF_STABILIZATION","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"LARGE_CELL_CUSTOMER_CALLOFF_STABILIZATION_CONTRACT_VISIBILITY_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-LargeCellCustomerCalloffStabilizationContractVisibilityBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_watch_moderate_MFE_low_MAE_after_calloff_reset","current_profile_verdict":"current_profile_correct_if_contract_visibility_calloff_ASP_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"After a long EV destock/call-off reset, large-cell contract visibility proxy produced moderate forward MFE with low MAE. This is positive-watch only; exact call-off volume, ASP, utilization, margin and FCF evidence are required before Green."}
{"row_type":"case","case_id":"C12_R3L93_006400_SDI_PREMIUM_CELL_CALLOFF_PRESSURE","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"PREMIUM_CELL_CUSTOMER_CONTRACT_VOCABULARY_WITH_CALLOFF_DEMAND_PRESSURE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PremiumCellCustomerContractVocabularyCalloffDemandPressure","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_customer_contract_vocabulary_no_calloff_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_premium_cell_contract_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Premium-cell/customer contract vocabulary after a March spike had low MFE and deep MAE when call-off, utilization, ASP and FCF bridge failed."}
{"row_type":"case","case_id":"C12_R3L93_005070_COSMO_CATHODE_SPIKE_DECAY","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_CUSTOMER_CONTRACT_VOCABULARY_WITHOUT_ASP_FCF_BRIDGE_AFTER_SPIKE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CathodeCustomerContractVocabularyNoASPFCFBridgeAfterSpike","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_post_spike_low_MFE_extreme_MAE_no_ASP_FCF_bridge","current_profile_verdict":"current_profile_false_positive_if_cathode_customer_contract_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Cathode/customer contract vocabulary after a February spike had low forward MFE and extreme drawdown when ASP/mix, utilization and FCF conversion were not repaired."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 373220 LG에너지솔루션 — call-off stabilization / customer-contract visibility positive-watch

Entry row: `2024-09-10 c=379500`, after a deep reset from first-half EV call-off pressure.
Observed path: high `2024-10-08 h=444000`, controlled low `2024-09-10 l=378000` and later low near `2024-11-15 l=371000`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L93_C12_373220_20240910_STAGE2_LARGE_CELL_CALLOFF_STABILIZATION","case_id":"C12_R3L93_373220_LGES_CALLOFF_STABILIZATION","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"LARGE_CELL_CUSTOMER_CALLOFF_STABILIZATION_CONTRACT_VISIBILITY_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-LargeCellCustomerCalloffStabilizationContractVisibilityBridge-PositiveWatch","trigger_date":"2024-09-10","entry_date":"2024-09-10","entry_price":379500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_large_cell_contract_calloff_stabilization_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; large-cell customer contract visibility, call-off stabilization, ASP/margin and FCF bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["customer_contract_visibility_proxy","calloff_stabilization_proxy","ASP_margin_proxy","relative_strength_after_reset"],"stage3_evidence_fields":["exact_calloff_volume_source_pending","customer_contract_source_pending","utilization_ASP_source_pending","margin_FCF_bridge_pending"],"stage4b_evidence_fields":["moderate_MFE_watch","Green_strict_watch"],"stage4c_evidence_fields":["calloff_reversal_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.99,"MFE_90D_pct":16.99,"MFE_180D_pct":16.99,"MAE_30D_pct":-0.40,"MAE_90D_pct":-2.24,"MAE_180D_pct":-2.24,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":371000.0,"drawdown_after_peak_pct":-16.44,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_only; moderate_MFE_requires_exact_calloff_contract_ASP_margin_FCF_evidence_before_Green","four_b_evidence_type":["moderate_MFE_watch","Green_strict_watch"],"four_c_protection_label":"calloff_reversal_watch_only","trigger_outcome_label":"positive_watch_moderate_MFE_low_MAE_after_calloff_reset","current_profile_verdict":"current_profile_correct_if_contract_visibility_calloff_ASP_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"373220_2024-09-10_379500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C12 can allow positive-watch after a reset when customer contract visibility and call-off stabilization are tied to ASP, utilization, margin and FCF bridge. Moderate MFE blocks automatic Green."}
```

### 6.2 006400 삼성SDI — premium-cell contract vocabulary with call-off / demand pressure

Entry row: `2024-03-12 c=459500`, during a March premium-cell rebound.
Observed path: high `2024-03-25 h=494500`, then a long decline to `2024-11-15 l=235500`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L93_C12_006400_20240312_STAGE2_FALSE_POSITIVE_PREMIUM_CELL_CALLOFF","case_id":"C12_R3L93_006400_SDI_PREMIUM_CELL_CALLOFF_PRESSURE","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"PREMIUM_CELL_CUSTOMER_CONTRACT_VOCABULARY_WITH_CALLOFF_DEMAND_PRESSURE","loop_objective":"residual_false_positive_mining;counterexample_mining;calloff_risk_stress_test","trigger_type":"Stage2-FalsePositive-PremiumCellCustomerContractVocabularyCalloffDemandPressure","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":459500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_premium_cell_customer_contract_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; premium-cell customer contract vocabulary treated as insufficient without call-off volume, shipment conversion, utilization, ASP/margin and FCF bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["premium_cell_contract_keyword","customer_mix_vocabulary","relative_strength_spike"],"stage3_evidence_fields":["calloff_volume_missing","shipment_conversion_missing","utilization_ASP_bridge_missing","FCF_bridge_missing"],"stage4b_evidence_fields":["low_MFE","deep_MAE","calloff_demand_pressure_watch"],"stage4c_evidence_fields":["demand_slowdown_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.62,"MFE_90D_pct":7.62,"MFE_180D_pct":7.62,"MAE_30D_pct":-12.73,"MAE_90D_pct":-21.44,"MAE_180D_pct":-48.75,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":494500.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":235500.0,"drawdown_after_peak_pct":-52.38,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"premium_cell_customer_contract_vocabulary_without_calloff_volume_ASP_margin_FCF_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","deep_MAE","calloff_demand_pressure_watch"],"four_c_protection_label":"demand_slowdown_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_customer_contract_vocabulary_no_calloff_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_premium_cell_contract_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"006400_2024-03-12_459500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C12 should not promote premium-cell customer-contract vocabulary unless call-off volume, shipment conversion, ASP/margin and FCF evidence are exact-repaired. Low MFE and deep MAE require Watch/4B."}
```

### 6.3 005070 코스모신소재 — cathode customer-contract vocabulary without ASP / FCF bridge

Entry row: `2024-02-20 c=185700`, after a cathode-material contract/mix price spike.
Observed path: local high `2024-02-21 h=194300`, followed by persistent decline to `2024-12-09 l=52000`.

```jsonl
{"row_type":"trigger","trigger_id":"R3L93_C12_005070_20240220_STAGE2_FALSE_POSITIVE_CATHODE_CONTRACT_SPIKE","case_id":"C12_R3L93_005070_COSMO_CATHODE_SPIKE_DECAY","symbol":"005070","company_name":"코스모신소재","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_CUSTOMER_CONTRACT_VOCABULARY_WITHOUT_ASP_FCF_BRIDGE_AFTER_SPIKE","loop_objective":"residual_false_positive_mining;counterexample_mining;post_spike_entry_guard","trigger_type":"Stage2-FalsePositive-CathodeCustomerContractVocabularyNoASPFCFBridgeAfterSpike","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":185700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_cathode_customer_contract_mix_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; cathode customer contract/mix vocabulary treated as insufficient without call-off volume, ASP pass-through, utilization, margin and FCF bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["cathode_customer_contract_keyword","high_nickel_mix_vocabulary","post_spike_relative_strength"],"stage3_evidence_fields":["calloff_volume_missing","ASP_pass_through_missing","margin_bridge_missing","FCF_conversion_missing"],"stage4b_evidence_fields":["low_MFE_after_spike","extreme_MAE","ASP_FCF_bridge_missing_watch"],"stage4c_evidence_fields":["demand_slowdown_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005070/2024.csv","profile_path":"atlas/symbol_profiles/005/005070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.63,"MFE_90D_pct":4.63,"MFE_180D_pct":4.63,"MAE_30D_pct":-18.42,"MAE_90D_pct":-31.56,"MAE_180D_pct":-72.00,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":194300.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":52000.0,"drawdown_after_peak_pct":-73.24,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"cathode_contract_vocabulary_without_calloff_ASP_margin_FCF_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE_after_spike","extreme_MAE","ASP_FCF_bridge_missing_watch"],"four_c_protection_label":"demand_slowdown_watch_only","trigger_outcome_label":"counterexample_post_spike_low_MFE_extreme_MAE_no_ASP_FCF_bridge","current_profile_verdict":"current_profile_false_positive_if_cathode_customer_contract_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"005070_2024-02-20_185700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C12 should not count cathode contract/mix vocabulary as positive unless call-off volume, ASP pass-through, margin and FCF evidence are repaired. Low MFE and extreme MAE force Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_R3L93_373220_LGES_CALLOFF_STABILIZATION","trigger_id":"R3L93_C12_373220_20240910_STAGE2_LARGE_CELL_CALLOFF_STABILIZATION","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C12 requires call-off volume, customer contract quality, shipment conversion, ASP/margin and FCF bridge rather than battery contract vocabulary alone","raw_component_scores_before":{"contract_quality_score":11,"customer_visibility_score":11,"calloff_volume_score":10,"shipment_conversion_score":9,"ASP_pass_through_score":8,"utilization_yield_score":8,"margin_bridge_score":8,"FCF_bridge_score":7,"relative_strength_score":8,"demand_slowdown_risk":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":62,"stage_label_before":"Stage2-Watch/PositiveControl","raw_component_scores_after":{"contract_quality_score":14,"customer_visibility_score":14,"calloff_volume_score":12,"shipment_conversion_score":11,"ASP_pass_through_score":10,"utilization_yield_score":10,"margin_bridge_score":10,"FCF_bridge_score":9,"relative_strength_score":9,"demand_slowdown_risk":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":77,"stage_label_after":"Stage2-Actionable/Yellow-Watch","component_delta_explanation":"Call-off stabilization and contract visibility supports Yellow-watch; moderate MFE and proxy-only evidence block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_R3L93_006400_SDI_PREMIUM_CELL_CALLOFF_PRESSURE","trigger_id":"R3L93_C12_006400_20240312_STAGE2_FALSE_POSITIVE_PREMIUM_CELL_CALLOFF","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"premium-cell contract vocabulary without call-off volume and ASP/margin bridge should be blocked","raw_component_scores_before":{"contract_quality_score":3,"customer_visibility_score":2,"calloff_volume_score":0,"shipment_conversion_score":0,"ASP_pass_through_score":0,"utilization_yield_score":0,"margin_bridge_score":0,"FCF_bridge_score":0,"relative_strength_score":4,"demand_slowdown_risk":-15,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"contract_quality_score":1,"customer_visibility_score":0,"calloff_volume_score":0,"shipment_conversion_score":0,"ASP_pass_through_score":0,"utilization_yield_score":0,"margin_bridge_score":0,"FCF_bridge_score":0,"relative_strength_score":1,"demand_slowdown_risk":-25,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE require call-off, ASP/margin and FCF evidence before any Yellow/Green promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_R3L93_005070_COSMO_CATHODE_SPIKE_DECAY","trigger_id":"R3L93_C12_005070_20240220_STAGE2_FALSE_POSITIVE_CATHODE_CONTRACT_SPIKE","symbol":"005070","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"cathode customer-contract vocabulary without ASP and FCF conversion should remain Watch/4B","raw_component_scores_before":{"contract_quality_score":2,"customer_visibility_score":1,"calloff_volume_score":0,"shipment_conversion_score":0,"ASP_pass_through_score":0,"utilization_yield_score":0,"margin_bridge_score":0,"FCF_bridge_score":0,"relative_strength_score":5,"demand_slowdown_risk":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"contract_quality_score":0,"customer_visibility_score":0,"calloff_volume_score":0,"shipment_conversion_score":0,"ASP_pass_through_score":0,"utilization_yield_score":0,"margin_bridge_score":0,"FCF_bridge_score":0,"relative_strength_score":0,"demand_slowdown_risk":-28,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Post-spike low MFE and extreme MAE require call-off, ASP pass-through, margin and FCF evidence before any promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R3L93_C12_P0_CURRENT","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C12 needs explicit call-off volume, shipment conversion, ASP/margin, FCF and demand slowdown taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":9.75,"avg_MAE90_pct":-18.41,"avg_MFE180_pct":9.75,"avg_MAE180_pct":-40.99,"false_positive_rate":0.67,"score_return_alignment_verdict":"mixed_without_C12_calloff_ASP_margin_FCF_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R3L93_C12_P1_SECTOR_SPECIFIC","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_id":"P1_L3_battery_customer_contract_calloff_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 customer-contract signals need call-off volume, shipment, ASP pass-through, utilization, margin or FCF conversion before Stage2-Actionable","changed_axes":["calloff_volume_required","ASP_margin_FCF_required","post_spike_contract_vocabulary_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_calloff_volume_shipment_ASP_margin_or_FCF_proxy"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R3L93_C12_P2_CANONICAL","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_id":"P2_C12_calloff_ASP_margin_FCF_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C12 should reward call-off-to-cash mechanics, not customer-contract vocabulary","changed_axes":["C12_calloff_volume_ASP_margin_FCF_bridge_required","C12_cell_cathode_contract_vocabulary_local_4B_guard","C12_post_spike_entry_guard","C12_moderate_MFE_Green_strict_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_contract_visibility_plus_calloff_or_ASP_margin_FCF_bridge_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R3L93_C12_P3_COUNTEREXAMPLE_GUARD","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","profile_id":"P3_C12_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If call-off/FCF bridge is missing, MFE90<10 or MAE180<=-25 blocks Yellow/Green and routes to Watch/4B","changed_axes":["C12_low_MFE_guardrail","C12_deep_MAE_4B_guardrail","C12_demand_slowdown_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE180_le_minus25)"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_CALLOFF_STABILIZATION_POSITIVE_VS_CELL_CATHODE_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":9.75,"avg_MAE90_pct":-18.41,"avg_MFE180_pct":9.75,"avg_MAE180_pct":-40.99,"stage2_hit_rate_MFE90_ge15":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE180_le_minus25":0.67,"interpretation":"C12 needs call-off discipline. LG에너지솔루션 shows post-reset customer call-off stabilization can support Yellow/positive-watch, while 삼성SDI and 코스모신소재 show cell/cathode contract vocabulary should not be promoted without call-off volume, shipment, ASP/margin and FCF evidence."}
{"row_type":"stage_transition_summary","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"373220","trigger_type":"Stage2-Actionable-LargeCellCustomerCalloffStabilizationContractVisibilityBridge-PositiveWatch","entry_date":"2024-09-10","stage2_to_90D_outcome":"positive_watch_moderate_MFE_low_MAE","stage2_to_180D_outcome":"calloff_stabilization_bridge_but_Green_strict","MFE90_ge15":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/positive-watch when call-off volume and contract visibility connect to ASP, margin and FCF; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"006400","trigger_type":"Stage2-FalsePositive-PremiumCellCustomerContractVocabularyCalloffDemandPressure","entry_date":"2024-03-12","stage2_to_90D_outcome":"bad_stage2_low_MFE_demand_pressure","stage2_to_180D_outcome":"failed_premium_cell_contract_vocabulary_deep_MAE","MFE90_ge15":false,"MAE180_le_minus25":true,"transition_note":"Premium-cell customer-contract vocabulary without call-off/margin/FCF bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","symbol":"005070","trigger_type":"Stage2-FalsePositive-CathodeCustomerContractVocabularyNoASPFCFBridgeAfterSpike","entry_date":"2024-02-20","stage2_to_90D_outcome":"bad_stage2_post_spike_low_MFE","stage2_to_180D_outcome":"failed_cathode_contract_vocabulary_extreme_MAE_no_ASP_FCF","MFE90_ge15":false,"MAE180_le_minus25":true,"transition_note":"Cathode customer-contract vocabulary after a spike without ASP/margin/FCF bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","residual_type":"cell_cathode_contract_vocabulary_overcredit_without_calloff_ASP_margin_FCF_bridge","contribution":"Adds two C12 4B counterexamples against one call-off stabilization positive-watch, bringing C12 from 27 toward the 30-row minimum stability threshold.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CELL_CUSTOMER_CALLOFF_STABILIZATION_VS_PREMIUM_CELL_AND_CATHODE_CONTRACT_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C12 now has one large-cell call-off stabilization positive-watch and two cell/cathode weak-bridge counterexamples; next C12 loops should exact-URL repair call-off volume, shipment conversion, ASP pass-through, utilization, margin and FCF evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"C12_calloff_volume_ASP_margin_FCF_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"373220 worked only as positive-watch when post-reset call-off stabilization proxy existed; 006400 and 005070 failed when call-off/ASP/FCF evidence was missing."}
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"C12_cell_cathode_contract_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"006400 and 005070 showed low MFE and deep MAE when cell/cathode contract vocabulary was not tied to shipment, ASP/margin and FCF."}
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"C12_post_spike_entry_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"005070 shows post-spike cathode contract vocabulary should not be promoted without fresh call-off and FCF evidence."}
{"row_type":"shadow_weight","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","axis":"C12_moderate_MFE_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"373220 is constructive but only moderate MFE; Green requires exact call-off volume, contract, ASP/margin and FCF evidence."}
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
  - cell_customer_contract_vocabulary_overcredit
  - cathode_contract_vocabulary_overcredit
  - calloff_volume_bridge_missing
  - ASP_margin_FCF_bridge_missing
  - post_spike_contract_entry_guard
new_axis_proposed:
  - C12_calloff_volume_ASP_margin_FCF_bridge_required_shadow_only
  - C12_cell_cathode_contract_vocabulary_local_4B_guard_shadow_only
  - C12_post_spike_entry_guard_shadow_only
  - C12_moderate_MFE_Green_strict_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows.
`373220` has no corporate-action candidate and the selected 2024 window is clean.
`006400` and `005070` have only historical corporate-action candidates before 2024; selected 2024 windows are usable.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
promotion should prefer hold / exact evidence repair until exact URLs are added
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
5. Confirm this loop was selected by coverage-index-first and brings C12 closer to the 30-row minimum stability threshold.
6. Confirm this loop avoided:
   - previous R3 loop85 C11 symbols
   - previous R3 loop86 C12 symbols
   - previous R3 loop87 C13 symbols
   - previous R3 loop88 C14 symbols
   - previous R3 loop89 C11 symbols
   - previous R3 loop90 C12 symbols
   - previous R3 loop91 C13 symbols
   - previous R3 loop92 C14 symbols
   - previous R3 loop93 C11 symbols
7. Confirm touched C24/C27/C19/C11 candidate rows are not ingested from this MD.
8. Treat 373220 as Yellow/positive-watch only, not Green, until exact call-off/ASP/margin/FCF evidence is repaired.
9. Treat 006400 and 005070 as weak-bridge failure modes unless exact shipment/call-off/margin/FCF evidence is added later.
10. If aggregate support remains stable after exact evidence URL repair, consider C12-scoped safe patch candidates:
   - C12_calloff_volume_ASP_margin_FCF_bridge_required
   - C12_cell_cathode_contract_vocabulary_local_4B_guard
   - C12_post_spike_entry_guard
   - C12_moderate_MFE_Green_strict_guard
11. Do not loosen Stage3-Green.
12. Do not use future MFE/MAE in runtime scoring.
13. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R3
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C13_BATTERY_JV_UTILIZATION_AMPC_IRA or C28_SOFTWARE_SECURITY_CONTRACT_RETENTION depending on newest coverage pressure and recent-loop avoidance
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 call-off stabilization positive-watch, 2 weak-bridge counterexamples, and 2 local 4B-watch rows for R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.
```

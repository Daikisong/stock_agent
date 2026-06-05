# E2R Stock-Web v12 Residual Research — R8 Loop 89 / L8 / C28

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R8
loop: 89
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: ERP_SAAS_CONTRACT_RETENTION_BRIDGE_VS_AI_SECURITY_THEME_BLOWOFF_DECAY
sector: platform / software / security / SaaS / ERP / AI software / cybersecurity
output_file: e2r_stock_web_v12_residual_round_R8_loop_89_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R7 loop 89`.

```text
scheduled_round = R8
scheduled_loop = 89
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

R8 is restricted to platform / content / software / security.  
C28 is selected because the recent R8 sequence already covered:

```text
R8 loop85: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
R8 loop86: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
R8 loop87: C27_CONTENT_IP_GLOBAL_MONETIZATION
R8 loop88: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

No-Repeat Index snapshot:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
rows = 26
symbols = 19
good/bad Stage2 = 10/4
4B/4C = 0/0
top-covered = 058970, 150900, 042510, 203650, 307950, 012510
```

This loop avoids the C28 top-covered list and the recent R8 loop symbols:

```text
R8 loop85 C26: 067160, 089600, 123570
R8 loop86 C28: 030520, 053800, 049480
R8 loop87 C27: 251270, 035900, 352820
R8 loop88 C26: 230360, 216050, 273060
```

Candidate hygiene note:

```text
A separate R7/C25 medical-device candidate sweep was accidentally touched during source lookup.
Those candidates are not used in this R8/C28 output.
```

Selected symbols:

```text
060850, 067920, 304100
```

This loop tests:

```text
ERP / SaaS contract-retention bridge
vs
cybersecurity theme spike without renewal, ARR or margin bridge
vs
AI software price-only blowoff without enterprise contract retention bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"060850","company_name":"영림원소프트랩","profile_path":"atlas/symbol_profiles/060/060850.json","first_date":"2020-08-12","last_date":"2026-02-20","trading_day_count":1353,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"067920","company_name":"이글루","profile_path":"atlas/symbol_profiles/067/067920.json","first_date":"2010-08-04","last_date":"2026-02-20","trading_day_count":3825,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2014-04-24"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"304100","company_name":"솔트룩스","profile_path":"atlas/symbol_profiles/304/304100.json","first_date":"2020-07-23","last_date":"2026-02-20","trading_day_count":1367,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2021-10-22","2021-11-11"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"060850","trigger_type":"Stage2-Actionable-ERPSaaSContractRetentionMaintenanceRevenueBridge-Positive","entry_date":"2024-01-02","duplicate_status":"new C28 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"067920","trigger_type":"Stage2-FalsePositive-CybersecurityThemeSpike-NoARRRenewalMarginBridge","entry_date":"2024-01-19","duplicate_status":"new C28 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"304100","trigger_type":"Stage2-FalsePositive-AISoftwarePriceOnlyBlowoff-NoEnterpriseContractRetentionBridge","entry_date":"2024-01-05","duplicate_status":"new C28 symbol/trigger/date combination outside top-covered and previous R8 loop symbols"}
```

## 4. Research question

C28 is not “소프트웨어나 보안 테마가 움직였다.”  
The useful C28 signal must prove software economics: recurring contract base, renewal rate, ARR/MRR quality, enterprise customer retention, backlog-to-revenue conversion, maintenance revenue, security-service renewal, gross-margin durability and cash conversion. Without that bridge, a software headline is like a login screen without a paid subscription behind it.

Residual question:

```text
Can C28 distinguish:
1. ERP/SaaS contract-retention bridge with usable MFE and controlled early MAE,
2. cybersecurity theme spike where no renewal, ARR, enterprise retention or margin bridge exists,
3. AI software price-only blowoff where local MFE is not enough because contract retention and cash bridge are missing?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C28_R8L89_060850_YOUNGLIMWON_ERP_SAAS_RETENTION","symbol":"060850","company_name":"영림원소프트랩","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ERP_SAAS_CONTRACT_RETENTION_MAINTENANCE_REVENUE_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ERPSaaSContractRetentionMaintenanceRevenueBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_ge20_controlled_90D_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_contract_retention_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"ERP/SaaS maintenance-revenue proxy produced MFE90 above 20% with limited early MAE. Later drawdown keeps Green strict and requires exact renewal/ARR/margin evidence."}
{"row_type":"case","case_id":"C28_R8L89_067920_IGLOO_SECURITY_THEME_SPIKE","symbol":"067920","company_name":"이글루","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_THEME_SPIKE_WITHOUT_ARR_RENEWAL_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CybersecurityThemeSpike-NoARRRenewalMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub_Yellow_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_security_theme_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Cybersecurity theme spike had sub-Yellow MFE90 and deep later MAE without ARR/renewal, enterprise retention, margin and cash bridge."}
{"row_type":"case","case_id":"C28_R8L89_304100_SALTUX_AI_SOFTWARE_BLOWOFF","symbol":"304100","company_name":"솔트룩스","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_SOFTWARE_PRICE_ONLY_BLOWOFF_WITHOUT_ENTERPRISE_CONTRACT_RETENTION_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-AISoftwarePriceOnlyBlowoff-NoEnterpriseContractRetentionBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_price_only_local_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_AI_software_blowoff_counted_as_contract_retention","price_source":"Songdaiki/stock-web","notes":"AI software blowoff had local MFE but severe forward MAE. Without enterprise contracts, renewal quality and margin/cash bridge, the move should be 4B-watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 060850 영림원소프트랩 — ERP/SaaS contract-retention bridge positive

Entry row: `2024-01-02 c=9000`.  
Observed path: early high `2024-01-19 h=10900`, later 90D high `2024-04-05 h=11270`, and late-year low `2024-12-27 l=5100`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L89_C28_060850_20240102_STAGE2_ERP_SAAS_RETENTION","case_id":"C28_R8L89_060850_YOUNGLIMWON_ERP_SAAS_RETENTION","symbol":"060850","company_name":"영림원소프트랩","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ERP_SAAS_CONTRACT_RETENTION_MAINTENANCE_REVENUE_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ERPSaaSContractRetentionMaintenanceRevenueBridge-Positive","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":9000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_ERP_SaaS_contract_retention_maintenance_revenue_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; ERP/SaaS maintenance revenue, renewal and enterprise customer retention bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["ERP_contract_base_proxy","maintenance_revenue_proxy","enterprise_retention_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_renewal_rate_pending","ARR_or_maintenance_revenue_pending","gross_margin_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/060/060850/2024.csv","profile_path":"atlas/symbol_profiles/060/060850.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.11,"MFE_90D_pct":25.22,"MFE_180D_pct":25.22,"MAE_30D_pct":-5.00,"MAE_90D_pct":-8.33,"MAE_180D_pct":-43.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-05","peak_price":11270.0,"max_drawdown_low_date":"2024-12-27","max_drawdown_low":5100.0,"drawdown_after_peak_pct":-54.75,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_late_drawdown_blocks_Green_without_exact_renewal_ARR_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE90_ge20_controlled_90D_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_contract_retention_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"060850_2024-01-02_9000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C28 can allow Stage2/Yellow when software strength is tied to ERP/SaaS contract base, renewal quality, maintenance revenue, gross margin and cash conversion. Green requires exact source-grade evidence because late drawdown can be large."}
```

### 6.2 067920 이글루 — cybersecurity theme spike without ARR/renewal/margin bridge

Entry row: `2024-01-19 c=7310`.  
Observed path: local high `2024-01-29 h=8680`, then long decay to `2024-11-15 l=4730`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L89_C28_067920_20240119_STAGE2_FALSE_POSITIVE_SECURITY_THEME","case_id":"C28_R8L89_067920_IGLOO_SECURITY_THEME_SPIKE","symbol":"067920","company_name":"이글루","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_THEME_SPIKE_WITHOUT_ARR_RENEWAL_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-CybersecurityThemeSpike-NoARRRenewalMarginBridge","trigger_date":"2024-01-19","entry_date":"2024-01-19","entry_price":7310.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_cybersecurity_theme_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; cybersecurity theme spike treated as insufficient without ARR, renewal, enterprise customer retention, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["cybersecurity_theme_spike","relative_strength_spike"],"stage3_evidence_fields":["ARR_bridge_missing","renewal_rate_missing","enterprise_retention_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","ARR_renewal_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067920/2024.csv","profile_path":"atlas/symbol_profiles/067/067920.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.74,"MFE_90D_pct":18.74,"MFE_180D_pct":18.74,"MAE_30D_pct":-11.08,"MAE_90D_pct":-23.67,"MAE_180D_pct":-35.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-29","peak_price":8680.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":4730.0,"drawdown_after_peak_pct":-45.51,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"security_theme_spike_without_ARR_renewal_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","ARR_renewal_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_security_theme_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"067920_2024-01-19_7310","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C28 should not promote cybersecurity theme spikes unless ARR, renewal quality, enterprise customer retention, margin and cash bridge are repaired. Sub-Yellow MFE and deep MAE force 4B-watch routing."}
```

### 6.3 304100 솔트룩스 — AI software blowoff without enterprise contract-retention bridge

Entry row: `2024-01-05 c=31450`.  
Observed path: local high `2024-01-08 h=35900`, later low `2024-09-24 l=15020`, and late-year AI-theme rebounds that should not validate the original weak entry.

```jsonl
{"row_type":"trigger","trigger_id":"R8L89_C28_304100_20240105_STAGE2_FALSE_POSITIVE_AI_SOFTWARE_BLOWOFF","case_id":"C28_R8L89_304100_SALTUX_AI_SOFTWARE_BLOWOFF","symbol":"304100","company_name":"솔트룩스","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_SOFTWARE_PRICE_ONLY_BLOWOFF_WITHOUT_ENTERPRISE_CONTRACT_RETENTION_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate;price_only_blowoff_stress_test","trigger_type":"Stage2-FalsePositive-AISoftwarePriceOnlyBlowoff-NoEnterpriseContractRetentionBridge","trigger_date":"2024-01-05","entry_date":"2024-01-05","entry_price":31450.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_AI_software_theme_blowoff_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; AI software blowoff treated as insufficient without enterprise contract retention, backlog-to-revenue, ARR, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["AI_software_theme_blowoff","relative_strength_spike"],"stage3_evidence_fields":["enterprise_contract_retention_missing","ARR_or_backlog_conversion_missing","gross_margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_MFE","late_rebound_not_entry_validation","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/304/304100/2024.csv","profile_path":"atlas/symbol_profiles/304/304100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.15,"MFE_90D_pct":14.15,"MFE_180D_pct":14.15,"MAE_30D_pct":-23.37,"MAE_90D_pct":-25.44,"MAE_180D_pct":-52.24,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-08","peak_price":35900.0,"max_drawdown_low_date":"2024-09-24","max_drawdown_low":15020.0,"drawdown_after_peak_pct":-58.16,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"AI_software_price_only_blowoff_without_enterprise_contract_retention_bridge_should_be_4B_watch_not_positive; late_rebound_not_entry_validation","four_b_evidence_type":["price_only","enterprise_contract_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_price_only_local_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_AI_software_blowoff_counted_as_contract_retention","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"304100_2024-01-05_31450","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C28 should not count AI software local MFE as contract-retention evidence. Enterprise contract retention, ARR/backlog conversion, margin and cash bridge must be exact-repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L89_060850_YOUNGLIMWON_ERP_SAAS_RETENTION","trigger_id":"R8L89_C28_060850_20240102_STAGE2_ERP_SAAS_RETENTION","symbol":"060850","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C28 requires recurring contract base, renewal rate, ARR/MRR quality, maintenance revenue, gross margin and cash bridge rather than software theme alone","raw_component_scores_before":{"contract_base_score":12,"renewal_rate_score":11,"ARR_quality_score":9,"maintenance_revenue_score":12,"enterprise_retention_score":10,"gross_margin_score":9,"cash_conversion_score":6,"relative_strength_score":12,"valuation_repricing_score":7,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"contract_base_score":15,"renewal_rate_score":14,"ARR_quality_score":11,"maintenance_revenue_score":15,"enterprise_retention_score":13,"gross_margin_score":11,"cash_conversion_score":8,"relative_strength_score":13,"valuation_repricing_score":8,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"ERP/SaaS renewal and maintenance-revenue bridge plus MFE90>20 supports Yellow-watch; late drawdown and proxy-only evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L89_067920_IGLOO_SECURITY_THEME_SPIKE","trigger_id":"R8L89_C28_067920_20240119_STAGE2_FALSE_POSITIVE_SECURITY_THEME","symbol":"067920","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"cybersecurity theme spike without ARR/renewal bridge should be blocked","raw_component_scores_before":{"contract_base_score":2,"renewal_rate_score":0,"ARR_quality_score":0,"maintenance_revenue_score":1,"enterprise_retention_score":0,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"contract_base_score":0,"renewal_rate_score":0,"ARR_quality_score":0,"maintenance_revenue_score":0,"enterprise_retention_score":0,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-Yellow MFE and deep MAE convert the cybersecurity theme spike into missing ARR/renewal bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L89_304100_SALTUX_AI_SOFTWARE_BLOWOFF","trigger_id":"R8L89_C28_304100_20240105_STAGE2_FALSE_POSITIVE_AI_SOFTWARE_BLOWOFF","symbol":"304100","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"AI software price-only blowoff without enterprise retention and margin bridge should be 4B-watch","raw_component_scores_before":{"contract_base_score":1,"renewal_rate_score":0,"ARR_quality_score":0,"maintenance_revenue_score":0,"enterprise_retention_score":0,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":14,"valuation_repricing_score":5,"execution_risk_score":-16,"theme_spike_risk":-22,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"contract_base_score":0,"renewal_rate_score":0,"ARR_quality_score":0,"maintenance_revenue_score":0,"enterprise_retention_score":0,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Local MFE is price-only; deep MAE and missing contract-retention bridge block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R8L89_C28_P0_CURRENT","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C28 needs explicit recurring contract, renewal, ARR, enterprise retention, gross margin, cash bridge and price-only AI/security 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":19.37,"avg_MAE90_pct":-19.15,"avg_MFE180_pct":19.37,"avg_MAE180_pct":-43.62,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C28_contract_retention_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R8L89_C28_P1_SECTOR_SPECIFIC","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P1_L8_software_contract_retention_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L8 software/security signals need contract base, renewal, ARR/MRR, enterprise retention, gross margin or cash conversion before Stage2-Actionable","changed_axes":["contract_retention_required","ARR_margin_required","AI_security_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_contract_base_renewal_ARR_enterprise_retention_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":19.37,"avg_MAE90_pct":-19.15,"avg_MFE180_pct":19.37,"avg_MAE180_pct":-43.62,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R8L89_C28_P2_CANONICAL","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P2_C28_contract_retention_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C28 should reward recurring-contract economics, not AI/security theme labels","changed_axes":["C28_contract_retention_margin_cash_bridge_required","C28_AI_security_theme_local_4B_guard","C28_late_rebound_not_contract_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"contract_base_or_renewal_plus_ARR_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":19.37,"avg_MAE90_pct":-19.15,"avg_MFE180_pct":19.37,"avg_MAE180_pct":-43.62,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R8L89_C28_P3_COUNTEREXAMPLE_GUARD","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P3_C28_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<20 and MAE180<=-30 while contract-retention bridge is missing, block Yellow/Green and route to 4B-watch","changed_axes":["C28_low_MFE_guardrail","C28_deep_MAE_4B_guardrail","C28_late_rebound_not_validation"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_20_and_MAE180_le_minus_30_with_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":19.37,"avg_MAE90_pct":-19.15,"avg_MFE180_pct":19.37,"avg_MAE180_pct":-43.62,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_ERP_SAAS_RETENTION_VS_AI_SECURITY_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":19.37,"avg_MAE90_pct":-19.15,"avg_MFE180_pct":19.37,"avg_MAE180_pct":-43.62,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_20":0.67,"stage2_bad_entry_rate_MAE180_le_minus30":1.0,"interpretation":"C28 needs bridge discipline. 영림원소프트랩 shows ERP/SaaS renewal and maintenance-revenue bridge can support Yellow-watch, while 이글루 and 솔트룩스 show security/AI software theme spikes should not be promoted without ARR, renewal, enterprise retention, gross-margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"060850","trigger_type":"Stage2-Actionable-ERPSaaSContractRetentionMaintenanceRevenueBridge-Positive","entry_date":"2024-01-02","stage2_to_90D_outcome":"good_stage2_MFE90_ge20_controlled_MAE","stage2_to_180D_outcome":"watch_positive_with_deep_late_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when contract retention, ARR/maintenance revenue, enterprise retention and margin bridge exists; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"067920","trigger_type":"Stage2-FalsePositive-CybersecurityThemeSpike-NoARRRenewalMarginBridge","entry_date":"2024-01-19","stage2_to_90D_outcome":"weak_stage2_sub_Yellow_MFE_deep_MAE","stage2_to_180D_outcome":"failed_security_theme_deep_MAE","MFE90_ge_20":false,"MAE180_le_minus_30":true,"transition_note":"Cybersecurity theme without ARR/renewal/margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"304100","trigger_type":"Stage2-FalsePositive-AISoftwarePriceOnlyBlowoff-NoEnterpriseContractRetentionBridge","entry_date":"2024-01-05","stage2_to_90D_outcome":"price_only_local_MFE_deep_MAE","stage2_to_180D_outcome":"failed_AI_software_blowoff_deep_MAE","MFE90_ge_20":false,"MAE180_le_minus_30":true,"transition_note":"AI software local MFE without enterprise contract-retention bridge should be treated as 4B-watch, not positive evidence."}
{"row_type":"residual_contribution","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_type":"AI_security_software_theme_overcredit_without_contract_retention_ARR_margin_bridge","contribution":"Adds two C28 local 4B/deep-MAE counterexamples against one ERP/SaaS retention positive, avoiding C28 top-covered and previous R8 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ERP_SAAS_CONTRACT_RETENTION_BRIDGE_VS_AI_SECURITY_THEME_BLOWOFF_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C28 now has non-top-symbol ERP/SaaS retention positive and two security/AI software weak-bridge counterexamples; next R8 loops should exact-URL repair renewal rate, ARR/MRR, enterprise retention, maintenance revenue, gross margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_contract_retention_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"060850 worked when ERP/SaaS maintenance and contract-retention proxy existed; 067920 and 304100 failed when only security/AI theme strength existed."}
{"row_type":"shadow_weight","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_AI_security_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Security and AI software rows showed sub-20 MFE90 and deep 180D MAE without non-price recurring-contract bridge."}
{"row_type":"shadow_weight","round":"R8","loop":"89","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_late_rebound_not_contract_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"304100 shows late AI-theme rebounds should not validate the original weak entry unless enterprise contract and retention evidence is repaired."}
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
  - software_theme_overcredit
  - cybersecurity_theme_overcredit
  - AI_software_blowoff_overcredit
  - contract_retention_ARR_margin_bridge_missing
new_axis_proposed:
  - C28_contract_retention_margin_cash_bridge_required_shadow_only
  - C28_AI_security_theme_local_4B_watch_guard_shadow_only
  - C28_late_rebound_not_contract_validation_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C28
  - full_4b_requires_non_price_evidence within C28
  - hard_4c_thesis_break_routes_to_4c within C28
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
3. Confirm R8 / L8 / C28 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C28 top-covered symbols
   - previous R8 loop85 C26 symbols
   - previous R8 loop86 C28 symbols
   - previous R8 loop87 C27 symbols
   - previous R8 loop88 C26 symbols
6. Confirm accidentally touched R7/C25 candidate rows are not ingested from this MD.
7. If aggregate support remains stable after exact evidence URL repair, consider C28-scoped safe patch candidates:
   - C28_contract_retention_margin_cash_bridge_required
   - C28_AI_security_theme_local_4B_watch_guard
   - C28_late_rebound_not_contract_validation_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R8
completed_loop = 89
next_round = R9
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.
```

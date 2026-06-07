# E2R Stock-Web v12 Residual Research — R8 Loop 92 / L8 / C28

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R8
loop: 92
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: ERP_CLOUD_CONTRACT_RETENTION_ARR_BRIDGE_VS_DATA_SECURITY_DIGITAL_ID_THEME_DECAY
sector: platform / software / security / ERP / cloud / ARR / renewal / identity security / contract retention
output_file: e2r_stock_web_v12_residual_round_R8_loop_92_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R7 loop 92`.

```text
scheduled_round = R8
scheduled_loop = 92
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

R8 is restricted to platform / content / software / security.
C28 is selected because R8 loop91 used C26 and the recent R8 rotation is:

```text
R8 loop85: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
R8 loop86: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
R8 loop87: C27_CONTENT_IP_GLOBAL_MONETIZATION
R8 loop88: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
R8 loop89: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
R8 loop90: C27_CONTENT_IP_GLOBAL_MONETIZATION
R8 loop91: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

No-Repeat Index snapshot used only as duplicate ledger:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
rows = 27
symbols = 15
good/bad Stage2 = 6/7
4B/4C = 4/2
top-covered = 053800, 030520, 136540, 047560, 060850, 356680
```

This loop avoids the C28 top-covered list and recent R8 loop symbols:

```text
R8 loop85 C26: 067160, 089600, 123570
R8 loop86 C28: 030520, 053800, 049480
R8 loop87 C27: 251270, 035900, 352820
R8 loop88 C26: 230360, 216050, 273060
R8 loop89 C28: 060850, 067920, 304100
R8 loop90 C27: 035760, 241840, 206560
R8 loop91 C26: 181710, 236810, 104200
```

Candidate hygiene note:

```text
During this execution path, stale R7/C25, R6/C22 and earlier-sector candidates were touched while checking alternatives.
Those rows are not used in this R8/C28 output.
```

Selected symbols:

```text
012510, 150900, 042510
```

The selected pocket is:

```text
ERP / cloud / enterprise software contract-retention and ARR-like operating leverage bridge
vs
data-security software vocabulary without fresh renewal / ARR / margin bridge
vs
digital-ID / authentication security theme spike without durable enterprise contract retention bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"012510","company_name":"더존비즈온","profile_path":"atlas/symbol_profiles/012/012510.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7742,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2002-04-22","2006-06-28","2009-12-09"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical name-transition/corporate-action candidates exist long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"150900","company_name":"파수","profile_path":"atlas/symbol_profiles/150/150900.json","first_date":"2013-10-18","last_date":"2026-02-20","trading_day_count":3029,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"042510","company_name":"라온시큐어","profile_path":"atlas/symbol_profiles/042/042510.json","first_date":"2001-01-03","last_date":"2026-02-20","trading_day_count":6153,"corporate_action_candidate_count":9,"corporate_action_candidate_dates":["2007-07-25","2008-10-16","2009-09-28","2009-11-13","2010-03-18","2011-05-19","2012-11-09","2023-12-18","2025-05-07"],"has_major_raw_discontinuity":true,"calibration_caveat":"A 2023-12-18 candidate exists before selected 2024 entry and 2025-05-07 candidate exists after the 2024 calibration window; keep data-quality watch before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_2024_window_usable; pre_entry_and_future_candidate_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"012510","trigger_type":"Stage2-Actionable-ERPCloudContractRetentionARRBridge-Positive","entry_date":"2024-01-08","duplicate_status":"new C28 symbol/trigger/date combination outside C28 top-covered and previous R8 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"150900","trigger_type":"Stage2-FalsePositive-DataSecuritySoftwareVocabularyNoFreshRenewalARRMarginBridge","entry_date":"2024-01-02","duplicate_status":"new C28 symbol/trigger/date combination outside C28 top-covered and previous R8 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"042510","trigger_type":"Stage2-FalsePositive-DigitalIDAuthenticationThemeNoEnterpriseContractRetentionBridge","entry_date":"2024-01-26","duplicate_status":"new C28 symbol/trigger/date combination outside C28 top-covered and previous R8 loop symbols; data-quality watch"}
```

## 4. Research question

C28 is not “보안·소프트웨어 단어가 있다.”
The useful signal must prove the contract-retention chain:

```text
enterprise customer contract or renewal
SaaS / cloud / subscription-like revenue visibility
ARR or recurring maintenance visibility
seat / module expansion
retention or renewal rate
implementation backlog or delivery schedule
gross-margin / operating-leverage bridge
working-capital discipline
cash conversion
```

A software headline without this bridge is a login screen with no active seat behind it. E2R needs the paid renewal, module expansion, ARR run-rate, margin leverage, and cash collection.

Residual question:

```text
Can C28 distinguish:
1. ERP/cloud enterprise software contract-retention bridge with strong MFE and shallow MAE,
2. data-security software vocabulary where no fresh renewal/ARR/margin evidence exists,
3. digital-ID/authentication theme spikes where price action does not prove durable enterprise contract retention?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C28_R8L92_012510_DOUZONE_ERP_CLOUD_CONTRACT","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ERP_CLOUD_CONTRACT_RETENTION_ARR_OPERATING_LEVERAGE_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ERPCloudContractRetentionARRBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_extreme_MFE90_and_MFE180_controlled_MAE_contract_retention_bridge","current_profile_verdict":"current_profile_correct_if_contract_renewal_ARR_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"ERP/cloud enterprise software retention and operating-leverage proxy produced very strong MFE with controlled MAE. Green still requires exact contract, ARR/renewal, module expansion, margin and cash evidence."}
{"row_type":"case","case_id":"C28_R8L92_150900_FASOO_SECURITY_VOCABULARY_DECAY","symbol":"150900","company_name":"파수","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"DATA_SECURITY_SOFTWARE_VOCABULARY_WITHOUT_FRESH_RENEWAL_ARR_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DataSecuritySoftwareVocabularyNoFreshRenewalARRMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_renewal_ARR_bridge","current_profile_verdict":"current_profile_false_positive_if_data_security_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Data-security software vocabulary had only low MFE and deep 90D/180D MAE without fresh renewal, ARR, seat/module expansion, margin and cash bridge."}
{"row_type":"case","case_id":"C28_R8L92_042510_RAON_DIGITAL_ID_THEME","symbol":"042510","company_name":"라온시큐어","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"DIGITAL_ID_AUTHENTICATION_THEME_WITHOUT_ENTERPRISE_CONTRACT_RETENTION_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DigitalIDAuthenticationThemeNoEnterpriseContractRetentionBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_low_MFE_deep_MAE_theme_spike_no_contract_retention_bridge","current_profile_verdict":"current_profile_false_positive_if_digital_ID_authentication_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Digital-ID/authentication theme spike had low MFE and large drawdown without durable enterprise contract, renewal, ARR or margin evidence. Pre-entry and future corporate-action candidates keep data-quality watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 012510 더존비즈온 — ERP/cloud contract-retention / ARR bridge

Entry row: `2024-01-08 c=34150`.
Observed path: entry low `2024-01-08 l=31050`, 90D path high around `2024-05-22 h=65300`, and full-window high `2024-07-08 h=78300`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L92_C28_012510_20240108_STAGE2_ERP_CLOUD_CONTRACT_RETENTION","case_id":"C28_R8L92_012510_DOUZONE_ERP_CLOUD_CONTRACT","symbol":"012510","company_name":"더존비즈온","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ERP_CLOUD_CONTRACT_RETENTION_ARR_OPERATING_LEVERAGE_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ERPCloudContractRetentionARRBridge-Positive","trigger_date":"2024-01-08","entry_date":"2024-01-08","entry_price":34150.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_ERP_cloud_AI_enterprise_contract_retention_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; ERP/cloud enterprise software contract, renewal, ARR-like recurring revenue and operating leverage treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["ERP_cloud_contract_proxy","enterprise_customer_retention_proxy","ARR_or_recurring_revenue_proxy","operating_leverage_proxy"],"stage3_evidence_fields":["exact_contract_source_pending","ARR_or_renewal_source_pending","module_expansion_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","Green_exact_evidence_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012510/2024.csv","profile_path":"atlas/symbol_profiles/012/012510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":64.86,"MFE_90D_pct":91.22,"MFE_180D_pct":129.28,"MAE_30D_pct":-9.08,"MAE_90D_pct":-9.08,"MAE_180D_pct":-9.08,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":78300.0,"max_drawdown_low_date":"2024-01-08","max_drawdown_low":31050.0,"drawdown_after_peak_pct":-39.97,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.83,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_contract_renewal_ARR_module_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","Green_exact_evidence_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_extreme_MFE90_and_MFE180_controlled_MAE_contract_retention_bridge","current_profile_verdict":"current_profile_correct_if_contract_renewal_ARR_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"012510_2024-01-08_34150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C28 can allow Stage2/Yellow or Green-candidate-watch when software strength is tied to enterprise contract retention, ARR/recurring revenue, module expansion, operating leverage and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 150900 파수 — data-security software vocabulary without renewal / ARR / margin bridge

Entry row: `2024-01-02 c=9470`.
Observed path: local high `2024-01-08 h=10100`, then persistent decline to `2024-07-04 l=5590`, `2024-09-24 l=5090`, and full-year low `2024-11-15 l=4110`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L92_C28_150900_20240102_STAGE2_FALSE_POSITIVE_DATA_SECURITY","case_id":"C28_R8L92_150900_FASOO_SECURITY_VOCABULARY_DECAY","symbol":"150900","company_name":"파수","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"DATA_SECURITY_SOFTWARE_VOCABULARY_WITHOUT_FRESH_RENEWAL_ARR_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-DataSecuritySoftwareVocabularyNoFreshRenewalARRMarginBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":9470.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_data_security_software_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; data-security / zero-trust / document security vocabulary treated as insufficient without fresh renewal, ARR, seat/module expansion, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["data_security_vocabulary","software_security_theme","relative_strength_rebound"],"stage3_evidence_fields":["fresh_contract_renewal_missing","ARR_visibility_missing","seat_module_expansion_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE","renewal_ARR_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/150/150900/2024.csv","profile_path":"atlas/symbol_profiles/150/150900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.65,"MFE_90D_pct":6.65,"MFE_180D_pct":6.65,"MAE_30D_pct":-12.46,"MAE_90D_pct":-34.00,"MAE_180D_pct":-46.25,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-08","peak_price":10100.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":4110.0,"drawdown_after_peak_pct":-59.31,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"data_security_software_vocabulary_without_renewal_ARR_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","renewal_ARR_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_renewal_ARR_bridge","current_profile_verdict":"current_profile_false_positive_if_data_security_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"150900_2024-01-02_9470","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C28 should not promote data-security vocabulary unless fresh renewal, ARR, seat/module expansion, operating-margin and cash evidence are exact-repaired. Low MFE and deep MAE require Watch/4B routing."}
```

### 6.3 042510 라온시큐어 — digital-ID / authentication theme without enterprise contract retention bridge

Entry row: `2024-01-26 c=2940`, after a digital-ID/authentication theme spike.
Observed path: same-day high `2024-01-26 h=3065`, then decline to `2024-07-24 l=2040`, with full-year low `2024-12-09 l=1650`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L92_C28_042510_20240126_STAGE2_FALSE_POSITIVE_DIGITAL_ID_AUTH","case_id":"C28_R8L92_042510_RAON_DIGITAL_ID_THEME","symbol":"042510","company_name":"라온시큐어","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"DIGITAL_ID_AUTHENTICATION_THEME_WITHOUT_ENTERPRISE_CONTRACT_RETENTION_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;data_quality_watch;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-DigitalIDAuthenticationThemeNoEnterpriseContractRetentionBridge","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":2940.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_digital_ID_authentication_security_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; digital ID / authentication / DID vocabulary treated as insufficient without enterprise contract, renewal, ARR, module expansion and margin/cash bridge","evidence_source_type":"historical_public_policy_theme_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["digital_ID_authentication_keyword","security_theme_spike","relative_strength_spike"],"stage3_evidence_fields":["enterprise_contract_missing","renewal_retention_missing","ARR_visibility_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE","theme_spike_watch","contract_retention_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042510/2024.csv","profile_path":"atlas/symbol_profiles/042/042510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.25,"MFE_90D_pct":4.25,"MFE_180D_pct":4.25,"MAE_30D_pct":-17.35,"MAE_90D_pct":-22.45,"MAE_180D_pct":-30.61,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-26","peak_price":3065.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1650.0,"drawdown_after_peak_pct":-46.17,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"digital_ID_authentication_theme_without_enterprise_contract_renewal_ARR_margin_cash_bridge_should_be_4B_watch_not_positive; data_quality_repair_needed_before_patch","four_b_evidence_type":["low_MFE","theme_spike_watch","contract_retention_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_theme_spike_no_contract_retention_bridge","current_profile_verdict":"current_profile_false_positive_if_digital_ID_authentication_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["pre_entry_2023-12-18_candidate_and_future_2025-05-07_candidate_watch"],"corporate_action_window_status":"2024_selected_window_usable; pre_entry_and_future_candidate_watch","same_entry_group_id":"042510_2024-01-26_2940","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C28 should not count digital-ID/authentication theme spikes as contract-retention evidence unless enterprise contract, renewal, ARR, module expansion, margin and cash evidence are repaired. Low MFE and deep MAE force Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L92_012510_DOUZONE_ERP_CLOUD_CONTRACT","trigger_id":"R8L92_C28_012510_20240108_STAGE2_ERP_CLOUD_CONTRACT_RETENTION","symbol":"012510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C28 requires enterprise contract, renewal/retention, ARR-like recurring revenue, module expansion, operating margin and cash bridge rather than software vocabulary alone","raw_component_scores_before":{"enterprise_contract_score":13,"renewal_retention_score":12,"ARR_recurring_revenue_score":13,"module_expansion_score":11,"implementation_backlog_score":10,"gross_margin_score":11,"operating_leverage_score":12,"cash_conversion_score":8,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"enterprise_contract_score":16,"renewal_retention_score":15,"ARR_recurring_revenue_score":16,"module_expansion_score":13,"implementation_backlog_score":12,"gross_margin_score":13,"operating_leverage_score":15,"cash_conversion_score":10,"relative_strength_score":17,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":91,"stage_label_after":"Stage3-Green-candidate-watch","component_delta_explanation":"ERP/cloud contract-retention and ARR bridge plus extreme MFE supports Green-candidate watch; exact contract/renewal/margin evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L92_150900_FASOO_SECURITY_VOCABULARY_DECAY","trigger_id":"R8L92_C28_150900_20240102_STAGE2_FALSE_POSITIVE_DATA_SECURITY","symbol":"150900","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"data-security software vocabulary without fresh renewal and ARR bridge should be blocked","raw_component_scores_before":{"enterprise_contract_score":1,"renewal_retention_score":0,"ARR_recurring_revenue_score":0,"module_expansion_score":0,"implementation_backlog_score":0,"gross_margin_score":0,"operating_leverage_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"enterprise_contract_score":0,"renewal_retention_score":0,"ARR_recurring_revenue_score":0,"module_expansion_score":0,"implementation_backlog_score":0,"gross_margin_score":0,"operating_leverage_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_repricing_score":0,"execution_risk_score":-28,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE require renewal, ARR, margin and cash evidence before any Yellow/Green promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L92_042510_RAON_DIGITAL_ID_THEME","trigger_id":"R8L92_C28_042510_20240126_STAGE2_FALSE_POSITIVE_DIGITAL_ID_AUTH","symbol":"042510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"digital-ID/authentication theme vocabulary without enterprise contract-retention bridge should remain Watch/4B","raw_component_scores_before":{"enterprise_contract_score":1,"renewal_retention_score":0,"ARR_recurring_revenue_score":0,"module_expansion_score":0,"implementation_backlog_score":0,"gross_margin_score":0,"operating_leverage_score":0,"cash_conversion_score":0,"relative_strength_score":4,"valuation_repricing_score":1,"execution_risk_score":-14,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"enterprise_contract_score":0,"renewal_retention_score":0,"ARR_recurring_revenue_score":0,"module_expansion_score":0,"implementation_backlog_score":0,"gross_margin_score":0,"operating_leverage_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Theme spike and data-quality watch are insufficient; exact enterprise renewal/ARR bridge is required before any promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R8L92_C28_P0_CURRENT","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C28 needs explicit enterprise contract, renewal/retention, ARR, module expansion, margin/cash and security-theme 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":34.04,"avg_MAE90_pct":-21.84,"avg_MFE180_pct":46.73,"avg_MAE180_pct":-28.65,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.94,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C28_contract_retention_ARR_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R8L92_C28_P1_SECTOR_SPECIFIC","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P1_L8_software_security_contract_retention_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L8 software/security signals need enterprise contract, renewal/retention, ARR/recurring revenue, module expansion, implementation backlog, operating leverage or cash conversion before Stage2-Actionable","changed_axes":["enterprise_contract_required","renewal_retention_required","ARR_margin_required","theme_security_vocabulary_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_enterprise_contract_renewal_ARR_module_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":34.04,"avg_MAE90_pct":-21.84,"avg_MFE180_pct":46.73,"avg_MAE180_pct":-28.65,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R8L92_C28_P2_CANONICAL","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P2_C28_contract_retention_ARR_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C28 should reward paid renewal/ARR-to-margin mechanics, not data-security or digital-ID vocabulary","changed_axes":["C28_enterprise_contract_renewal_ARR_margin_cash_bridge_required","C28_data_security_digital_ID_vocabulary_local_4B_guard","C28_theme_spike_not_contract_retention_validation_guard","C28_data_quality_repair_guard"],"changed_thresholds":{"stage2_yellow_gate":"enterprise_contract_or_renewal_plus_ARR_or_margin_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":34.04,"avg_MAE90_pct":-21.84,"avg_MFE180_pct":46.73,"avg_MAE180_pct":-28.65,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R8L92_C28_P3_COUNTEREXAMPLE_GUARD","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P3_C28_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If contract-retention/ARR bridge is missing, MFE90<10 or MAE90<=-20 should block Yellow/Green and route to Watch/4B","changed_axes":["C28_low_MFE_guardrail","C28_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE90_le_minus20)"},"eligible_trigger_count":3,"avg_MFE90_pct":34.04,"avg_MAE90_pct":-21.84,"avg_MFE180_pct":46.73,"avg_MAE180_pct":-28.65,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_ERP_CLOUD_POSITIVE_VS_DATA_SECURITY_DIGITAL_ID_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":34.04,"avg_MAE90_pct":-21.84,"avg_MFE180_pct":46.73,"avg_MAE180_pct":-28.65,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE90_le_minus20":0.67,"interpretation":"C28 needs bridge discipline. 더존비즈온 shows ERP/cloud enterprise contract-retention and ARR/margin bridge can support Green-candidate-watch, while 파수 and 라온시큐어 show security/digital-ID vocabulary should not be promoted without fresh renewal, ARR, seat/module expansion, operating leverage, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"012510","trigger_type":"Stage2-Actionable-ERPCloudContractRetentionARRBridge-Positive","entry_date":"2024-01-08","stage2_to_90D_outcome":"good_stage2_extreme_MFE_controlled_MAE","stage2_to_180D_outcome":"positive_contract_retention_ARR_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow/Green-candidate when software strength is tied to enterprise contract, renewal, ARR, module expansion and margin/cash bridge; exact evidence is required for Green."}
{"row_type":"stage_transition_summary","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"150900","trigger_type":"Stage2-FalsePositive-DataSecuritySoftwareVocabularyNoFreshRenewalARRMarginBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_data_security_vocabulary_no_renewal_ARR_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Data-security vocabulary without fresh renewal/ARR and margin/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"042510","trigger_type":"Stage2-FalsePositive-DigitalIDAuthenticationThemeNoEnterpriseContractRetentionBridge","entry_date":"2024-01-26","stage2_to_90D_outcome":"bad_stage2_low_MFE_theme_spike_bridge_missing","stage2_to_180D_outcome":"failed_digital_ID_authentication_theme_deep_MAE","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Digital-ID/authentication theme without enterprise contract-retention and ARR bridge should remain Watch/4B-risk; data-quality watch remains."}
{"row_type":"residual_contribution","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_type":"data_security_digital_ID_vocabulary_overcredit_without_contract_retention_ARR_margin_cash_bridge","contribution":"Adds two C28 4B counterexamples against one ERP/cloud contract-retention positive, avoiding C28 top-covered and recent R8 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ERP_CLOUD_CONTRACT_RETENTION_ARR_BRIDGE_VS_DATA_SECURITY_DIGITAL_ID_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C28 now has non-top-symbol ERP/cloud contract-retention positive and two data-security/digital-ID weak-bridge counterexamples; next R8 C28 loops should exact-URL repair enterprise contract, renewal/retention, ARR, seat/module expansion, gross-margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_enterprise_contract_renewal_ARR_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"012510 worked when ERP/cloud contract-retention and ARR/margin proxy existed; 150900 and 042510 failed when security vocabulary lacked renewal/ARR evidence."}
{"row_type":"shadow_weight","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_data_security_digital_ID_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Data-security and digital-ID/authentication rows showed low MFE and deep MAE when enterprise contract-retention bridge was missing."}
{"row_type":"shadow_weight","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_theme_spike_not_contract_retention_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"042510 shows authentication/security theme spikes should not validate C28 unless paid enterprise renewal/ARR evidence exists."}
{"row_type":"shadow_weight","round":"R8","loop":"92","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_data_quality_repair_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"042510 has pre-entry and future corporate-action candidates, so patch consideration requires price-path and evidence repair."}
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
  - data_security_software_vocabulary_overcredit
  - digital_ID_authentication_theme_overcredit
  - contract_renewal_bridge_missing
  - ARR_module_expansion_margin_cash_bridge_missing
  - theme_spike_not_contract_retention_validation
  - data_quality_watch
new_axis_proposed:
  - C28_enterprise_contract_renewal_ARR_margin_cash_bridge_required_shadow_only
  - C28_data_security_digital_ID_vocabulary_local_4B_guard_shadow_only
  - C28_theme_spike_not_contract_retention_validation_guard_shadow_only
  - C28_data_quality_repair_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows.
`012510` has old name-transition / corporate-action candidates before 2024; the selected 2024 window is usable.
`150900` has no corporate-action candidate in the profile.
`042510` has a pre-entry 2023-12-18 candidate and a future 2025-05-07 candidate outside the selected 2024 window, so it remains data-quality-watch before production patching.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 042510
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
   - previous R8 loop89 C28 symbols
   - previous R8 loop90 C27 symbols
   - previous R8 loop91 C26 symbols
6. Confirm stale R7/C25, R6/C22 and earlier-sector candidate rows are not ingested from this MD.
7. Keep 042510 in data-quality repair watch before patch consideration.
8. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C28-scoped safe patch candidates:
   - C28_enterprise_contract_renewal_ARR_margin_cash_bridge_required
   - C28_data_security_digital_ID_vocabulary_local_4B_guard
   - C28_theme_spike_not_contract_retention_validation_guard
   - C28_data_quality_repair_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R8
completed_loop = 92
next_round = R9
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.
```

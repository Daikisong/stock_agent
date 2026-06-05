# E2R Stock-Web v12 Residual Research — R8 Loop 84 / L8 / C28

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R8
loop: 84
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: OFFICE_AI_SW_CONTRACT_RETENTION_BRIDGE_VS_AI_THEME_SPIKE_HIGH_MAE
sector: platform/content/software/security / software-security contract retention
output_file: e2r_stock_web_v12_residual_round_R8_loop_84_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R7 loop 84`.

```text
scheduled_round = R8
scheduled_loop = 84
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

R8 is restricted to platform / content / software / security.  
C28 is selected because the No-Repeat ledger shows C28 has no explicit 4B/4C cases and still needs a sharper distinction between true software/security contract retention and AI/SW theme spikes.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"030520","company_name":"한글과컴퓨터","profile_path":"atlas/symbol_profiles/030/030520.json","first_date":"1996-09-24","last_date":"2026-02-20","trading_day_count":7226,"corporate_action_candidate_count":8,"corporate_action_candidate_dates":["1997-01-03","1998-10-01","1998-11-21","1999-08-23","2003-08-22","2004-12-09","2005-12-23","2006-12-05"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"047560","company_name":"이스트소프트","profile_path":"atlas/symbol_profiles/047/047560.json","first_date":"2008-07-01","last_date":"2026-02-20","trading_day_count":4351,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2015-05-06","2015-05-27"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"041020","company_name":"폴라리스오피스","profile_path":"atlas/symbol_profiles/041/041020.json","first_date":"2005-10-28","last_date":"2026-02-20","trading_day_count":5010,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["2010-03-12","2010-03-25","2010-04-02","2017-05-15"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
For C28, the top-covered symbols are `058970`, `150900`, `042510`, `203650`, `307950`, and `012510`. This run avoids that repeated set.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"030520","trigger_type":"Stage2-Actionable-OfficeAISWContractRetentionBridge-Positive","entry_date":"2024-04-18","duplicate_status":"new C28 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"047560","trigger_type":"Stage2-FalsePositive-AIAvatarSWThemeSpike-NoARRRetentionBridge","entry_date":"2024-01-26","duplicate_status":"new C28 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"041020","trigger_type":"Stage2-FalsePositive-AIOfficeThemeSpike-NoEnterpriseRetentionBridge","entry_date":"2024-05-09","duplicate_status":"new C28 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C28 should not read every AI software spike as contract retention. In software, the real engine is not a press release; it is renewal, ARR/RPO, paid conversion, enterprise seat expansion, and margin retention. A theme spike without those gears is like a dashboard light with no engine behind it.

Residual question:

```text
Can C28 distinguish:
1. office/AI software rerating with contract-retention and monetization bridge,
2. AI-avatar software theme spike with no ARR/retention bridge,
3. AI-office theme spike with no enterprise retention or paid-conversion bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C28_R8L84_030520_HNC_OFFICE_AI_RETENTION_BRIDGE","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"OFFICE_AI_SW_CONTRACT_RETENTION_MONETIZATION_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-OfficeAISWContractRetentionBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_contract_retention_bridge_required","price_source":"Songdaiki/stock-web","notes":"Office/software AI monetization path worked when contract-retention proxy and price path aligned. Supports Stage2/Yellow, not Green without exact ARR/retention evidence."}
{"row_type":"case","case_id":"C28_R8L84_047560_ESTSOFT_AI_AVATAR_THEME_SPIKE","symbol":"047560","company_name":"이스트소프트","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_AVATAR_SW_THEME_SPIKE_WITHOUT_ARR_RETENTION_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-AIAvatarSWThemeSpike-NoARRRetentionBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_AI_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"AI-avatar theme extension had local blowoff and deep MAE without ARR/retention bridge; C28 should route it to Watch/4B-risk."}
{"row_type":"case","case_id":"C28_R8L84_041020_POLARIS_AI_OFFICE_THEME_SPIKE","symbol":"041020","company_name":"폴라리스오피스","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_OFFICE_THEME_SPIKE_WITHOUT_ENTERPRISE_RETENTION_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-AIOfficeThemeSpike-NoEnterpriseRetentionBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_AI_office_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"AI-office theme spike had limited upside and large drawdown before later unrelated rebounds; C28 should require paid conversion and enterprise retention bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 030520 한글과컴퓨터 — office/AI SW contract-retention bridge positive

Entry row: `2024-04-18 c=22250`.  
Forward path: 30D/90D peak `2024-05-21 h=33400`; low within the forward window touched `2024-10-21 l=17050`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L84_C28_030520_20240418_STAGE2_OFFICE_AI_SW_RETENTION_BRIDGE","case_id":"C28_R8L84_030520_HNC_OFFICE_AI_RETENTION_BRIDGE","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"OFFICE_AI_SW_CONTRACT_RETENTION_MONETIZATION_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;yellow_threshold_stress_test","trigger_type":"Stage2-Actionable-OfficeAISWContractRetentionBridge-Positive","trigger_date":"2024-04-18","entry_date":"2024-04-18","entry_price":22250.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_SW_monetization_retention_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; office/AI SW monetization and contract-retention thesis treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["contract_retention_proxy","paid_conversion_proxy","office_SW_monetization_proxy","relative_strength_turn"],"stage3_evidence_fields":["ARR_or_RPO_bridge_pending","enterprise_seat_expansion_pending","margin_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv","profile_path":"atlas/symbol_profiles/030/030520.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":50.11,"MFE_90D_pct":50.11,"MFE_180D_pct":50.11,"MAE_30D_pct":-4.49,"MAE_90D_pct":-10.65,"MAE_180D_pct":-23.37,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":33400.0,"max_drawdown_low_date":"2024-10-21","max_drawdown_low":17050.0,"drawdown_after_peak_pct":-48.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_tolerable_initial_MAE","current_profile_verdict":"current_profile_correct_if_contract_retention_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"030520_2024-04-18_22250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C28 can support Stage2/Yellow when AI software theme is tied to paid conversion and retention bridge. Green still requires exact ARR/RPO, enterprise-seat, and margin evidence."}
```

### 6.2 047560 이스트소프트 — AI-avatar SW theme spike without ARR/retention bridge

Entry row: `2024-01-26 c=47200`.  
Forward path: local high `2024-01-29 h=49800`, then deep drawdown to `2024-06-27 l=18120` and later `2024-10-25 l=11990`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L84_C28_047560_20240126_STAGE2_FALSE_POSITIVE_AI_AVATAR_SW_THEME","case_id":"C28_R8L84_047560_ESTSOFT_AI_AVATAR_THEME_SPIKE","symbol":"047560","company_name":"이스트소프트","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_AVATAR_SW_THEME_SPIKE_WITHOUT_ARR_RETENTION_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-AIAvatarSWThemeSpike-NoARRRetentionBridge","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":47200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_AI_SW_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; AI-avatar/SW theme spike treated as insufficient without ARR, retention, enterprise contract, or paid-conversion bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["AI_theme_relative_strength","product_demo_or_PR_proxy"],"stage3_evidence_fields":["ARR_bridge_missing","contract_retention_missing","paid_conversion_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047560/2024.csv","profile_path":"atlas/symbol_profiles/047/047560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.51,"MFE_90D_pct":5.51,"MFE_180D_pct":5.51,"MAE_30D_pct":-43.22,"MAE_90D_pct":-61.61,"MAE_180D_pct":-74.60,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-29","peak_price":49800.0,"max_drawdown_low_date":"2024-10-25","max_drawdown_low":11990.0,"drawdown_after_peak_pct":-75.92,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"AI_theme_peak_without_retention_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_AI_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"047560_2024-01-26_47200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"AI software theme spike without ARR/retention bridge had tiny MFE and severe MAE. C28 needs a local retention/paid-conversion guard before Stage2-Actionable or Yellow."}
```

### 6.3 041020 폴라리스오피스 — AI-office theme spike without enterprise retention bridge

Entry row: `2024-05-09 c=9660`.  
Forward path: local high `2024-05-14 h=10550`, then drawdown to `2024-07-22 l=6720` and `2024-10-23 l=4640`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L84_C28_041020_20240509_STAGE2_FALSE_POSITIVE_AI_OFFICE_THEME","case_id":"C28_R8L84_041020_POLARIS_AI_OFFICE_THEME_SPIKE","symbol":"041020","company_name":"폴라리스오피스","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"AI_OFFICE_THEME_SPIKE_WITHOUT_ENTERPRISE_RETENTION_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-AIOfficeThemeSpike-NoEnterpriseRetentionBridge","trigger_date":"2024-05-09","entry_date":"2024-05-09","entry_price":9660.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_AI_office_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; AI-office theme spike treated as insufficient without enterprise retention, paid conversion, and contract-quality bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["AI_office_theme_spike","relative_strength_turn"],"stage3_evidence_fields":["enterprise_contract_missing","retention_bridge_missing","paid_conversion_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041020/2024.csv","profile_path":"atlas/symbol_profiles/041/041020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.21,"MFE_90D_pct":9.21,"MFE_180D_pct":9.21,"MAE_30D_pct":-17.70,"MAE_90D_pct":-30.43,"MAE_180D_pct":-51.97,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-14","peak_price":10550.0,"max_drawdown_low_date":"2024-10-23","max_drawdown_low":4640.0,"drawdown_after_peak_pct":-56.02,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"office_AI_theme_peak_without_enterprise_retention_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_AI_office_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"041020_2024-05-09_9660","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"AI-office theme spike had limited upside and high drawdown without enterprise retention and paid conversion bridge. C28 should keep it Watch/4B-risk rather than Stage2-Actionable."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L84_030520_HNC_OFFICE_AI_RETENTION_BRIDGE","trigger_id":"R8L84_C28_030520_20240418_STAGE2_OFFICE_AI_SW_RETENTION_BRIDGE","symbol":"030520","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C28 requires contract retention and paid conversion bridge","raw_component_scores_before":{"ARR_RPO_score":11,"contract_retention_score":12,"paid_conversion_score":11,"enterprise_customer_quality":10,"gross_margin_leverage":9,"relative_strength_score":14,"valuation_repricing_score":10,"execution_risk_score":-5,"theme_spike_risk":-3,"information_confidence":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"ARR_RPO_score":13,"contract_retention_score":15,"paid_conversion_score":14,"enterprise_customer_quality":12,"gross_margin_leverage":11,"relative_strength_score":15,"valuation_repricing_score":11,"execution_risk_score":-4,"theme_spike_risk":-2,"information_confidence":6},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Contract-retention and paid-conversion proxy upgrades C28 to Yellow-watch, but exact ARR/RPO and enterprise retention evidence still block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L84_047560_ESTSOFT_AI_AVATAR_THEME_SPIKE","trigger_id":"R8L84_C28_047560_20240126_STAGE2_FALSE_POSITIVE_AI_AVATAR_SW_THEME","symbol":"047560","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"AI software theme without ARR/retention bridge should be blocked","raw_component_scores_before":{"ARR_RPO_score":2,"contract_retention_score":2,"paid_conversion_score":2,"enterprise_customer_quality":3,"gross_margin_leverage":4,"relative_strength_score":18,"valuation_repricing_score":8,"execution_risk_score":-14,"theme_spike_risk":-15,"information_confidence":3},"weighted_score_before":33,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"ARR_RPO_score":0,"contract_retention_score":0,"paid_conversion_score":0,"enterprise_customer_quality":1,"gross_margin_leverage":2,"relative_strength_score":6,"valuation_repricing_score":3,"execution_risk_score":-20,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and deep MAE convert AI-avatar theme spike into evidence-quality failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L84_041020_POLARIS_AI_OFFICE_THEME_SPIKE","trigger_id":"R8L84_C28_041020_20240509_STAGE2_FALSE_POSITIVE_AI_OFFICE_THEME","symbol":"041020","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"AI-office theme without enterprise retention bridge should remain Watch/blocked","raw_component_scores_before":{"ARR_RPO_score":2,"contract_retention_score":3,"paid_conversion_score":3,"enterprise_customer_quality":3,"gross_margin_leverage":4,"relative_strength_score":14,"valuation_repricing_score":7,"execution_risk_score":-12,"theme_spike_risk":-13,"information_confidence":3},"weighted_score_before":31,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"ARR_RPO_score":0,"contract_retention_score":0,"paid_conversion_score":0,"enterprise_customer_quality":1,"gross_margin_leverage":2,"relative_strength_score":5,"valuation_repricing_score":3,"execution_risk_score":-18,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Missing enterprise retention and paid-conversion bridge plus high MAE block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R8L84_C28_P0_CURRENT","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C28 needs explicit ARR/retention/paid-conversion bridge distinction","eligible_trigger_count":3,"avg_MFE_90D_pct":21.61,"avg_MAE_90D_pct":-34.23,"avg_MFE_180D_pct":21.61,"avg_MAE_180D_pct":-49.98,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C28_retention_guard"}
{"row_type":"profile_comparison","comparison_id":"R8L84_C28_P1_SECTOR_SPECIFIC","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P1_L8_SW_retention_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L8 software signals need ARR/RPO, contract retention, paid conversion, or enterprise customer bridge before Stage2-Actionable","changed_axes":["ARR_RPO_bridge_required","contract_retention_required","paid_conversion_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_ARR_RPO_retention_or_paid_conversion_proxy"},"eligible_trigger_count":3,"avg_MFE_90D_pct":21.61,"avg_MAE_90D_pct":-34.23,"avg_MFE_180D_pct":21.61,"avg_MAE_180D_pct":-49.98,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R8L84_C28_P2_CANONICAL","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P2_C28_contract_retention_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C28 should reward recurring software contract quality, not AI theme spikes","changed_axes":["C28_ARR_retention_bridge_required","C28_paid_conversion_bridge_required","C28_AI_theme_spike_penalty"],"changed_thresholds":{"stage2_yellow_gate":"ARR_retention_or_paid_conversion_bridge_required"},"eligible_trigger_count":3,"avg_MFE_90D_pct":21.61,"avg_MAE_90D_pct":-34.23,"avg_MFE_180D_pct":21.61,"avg_MAE_180D_pct":-49.98,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R8L84_C28_P3_COUNTEREXAMPLE_GUARD","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P3_C28_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-30 while retention/ARR bridge is missing, block Yellow/Green","changed_axes":["C28_high_MAE_guardrail","C28_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_30"},"eligible_trigger_count":3,"avg_MFE_90D_pct":21.61,"avg_MAE_90D_pct":-34.23,"avg_MFE_180D_pct":21.61,"avg_MAE_180D_pct":-49.98,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_OFFICE_AI_SW_RETENTION_VS_AI_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":21.61,"avg_MAE90_pct":-34.23,"avg_MFE180_pct":21.61,"avg_MAE180_pct":-49.98,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":1.0,"interpretation":"C28 needs bridge discipline. 030520 shows a valid office/AI SW monetization bridge, while 047560 and 041020 show AI/SW theme spikes that fail without ARR/retention/paid-conversion bridge."}
{"row_type":"stage_transition_summary","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"030520","trigger_type":"Stage2-Actionable-OfficeAISWContractRetentionBridge-Positive","entry_date":"2024-04-18","stage2_to_90D_outcome":"good_stage2_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_re_rating_path_with_later_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when contract-retention and paid-conversion bridge exists; Green requires exact ARR/RPO and margin evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"047560","trigger_type":"Stage2-FalsePositive-AIAvatarSWThemeSpike-NoARRRetentionBridge","entry_date":"2024-01-26","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_entry_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"AI-avatar/SW theme spike without ARR/retention bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"041020","trigger_type":"Stage2-FalsePositive-AIOfficeThemeSpike-NoEnterpriseRetentionBridge","entry_date":"2024-05-09","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_entry_theme_spike","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"AI-office theme spike without enterprise retention and paid conversion should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_type":"AI_SW_theme_overcredit_without_ARR_retention_paid_conversion_bridge","contribution":"Adds two C28 high-MAE counterexamples against one SW-retention bridge positive, filling C28's 4B-watch gap outside top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"OFFICE_AI_SW_CONTRACT_RETENTION_BRIDGE_VS_AI_THEME_SPIKE_HIGH_MAE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C28 now has non-top-symbol high-MAE AI/SW theme-spike counterexamples; next R8 loops should exact-URL repair ARR/RPO, retention, renewal, and enterprise contract evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_ARR_retention_paid_conversion_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"030520 worked with SW monetization/retention proxy; 047560 and 041020 failed when ARR/retention/paid conversion bridge was missing."}
{"row_type":"shadow_weight","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_AI_SW_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"AI/SW theme spikes showed low MFE and high MAE without recurring contract or enterprise retention evidence."}
{"row_type":"shadow_weight","round":"R8","loop":"84","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-30 while retention/ARR/paid-conversion bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
residual_error_types_found:
  - AI_SW_theme_overcredit
  - ARR_retention_bridge_missing
  - enterprise_paid_conversion_bridge_missing
new_axis_proposed:
  - C28_ARR_retention_paid_conversion_bridge_required_shadow_only
  - C28_AI_SW_theme_local_4B_watch_guard_shadow_only
  - C28_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C28
  - full_4b_requires_non_price_evidence within C28
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
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
3. Confirm R8 / L8 / C28 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. If aggregate support remains stable after exact evidence URL repair, consider C28-scoped safe patch candidates:
   - C28_ARR_retention_paid_conversion_bridge_required
   - C28_AI_SW_theme_local_4B_watch_guard
   - C28_high_MAE_guardrail
6. Do not loosen Stage3-Green.
7. Do not use future MFE/MAE in runtime scoring.
8. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R8
completed_loop = 84
next_round = R9
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.
```

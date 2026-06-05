# E2R Stock-Web v12 Residual Research — R8 Loop 86 / L8 / C28

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R8
loop: 86
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: SOFTWARE_AI_CONTRACT_RETENTION_ARR_BRIDGE_VS_SECURITY_AI_THEME_REBOUND_WITHOUT_RECURRING_REVENUE
sector: platform / content / software / security / contract retention
output_file: e2r_stock_web_v12_residual_round_R8_loop_86_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R7 loop 86`.

```text
scheduled_round = R8
scheduled_loop = 86
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

R8 is restricted to platform / content / software / security.  
C28 is selected because the immediately previous R8 loop used C26 platform/ad-revenue operating leverage, while C28 still has no explicit 4B/4C coverage in the No-Repeat Index:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
rows = 26
symbols = 19
good/bad Stage2 = 10/4
4B/4C = 0/0
top-covered = 058970, 150900, 042510, 203650, 307950, 012510
```

This loop avoids the top-covered set and also avoids the previous R8 loop85 C26 symbols:

```text
067160, 089600, 123570
```

The target is not generic software momentum. It is whether the software/security signal is backed by contract retention, recurring revenue, ARR, renewal quality, enterprise customer stickiness, and margin conversion.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"030520","company_name":"한글과컴퓨터","profile_path":"atlas/symbol_profiles/030/030520.json","first_date":"1996-09-24","last_date":"2026-02-20","trading_day_count":7226,"corporate_action_candidate_count":8,"corporate_action_candidate_dates":["1997-01-03","1998-10-01","1998-11-21","1999-08-23","2003-08-22","2004-12-09","2005-12-23","2006-12-05"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"053800","company_name":"안랩","profile_path":"atlas/symbol_profiles/053/053800.json","first_date":"2001-09-13","last_date":"2026-02-20","trading_day_count":6027,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2005-03-31"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"049480","company_name":"오픈베이스","profile_path":"atlas/symbol_profiles/049/049480.json","first_date":"2001-01-09","last_date":"2026-02-20","trading_day_count":6196,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2006-04-17","2006-07-20"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"030520","trigger_type":"Stage2-Actionable-SoftwareAIContractRetentionARRBridge-Positive","entry_date":"2024-01-10","duplicate_status":"new C28 symbol/trigger/date combination outside top-covered list and previous R8 loop85 C26 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"053800","trigger_type":"Stage2-FalsePositive-SecurityThemeBeta-NoFreshContractRetentionBridge","entry_date":"2024-01-25","duplicate_status":"new C28 symbol/trigger/date combination outside top-covered list and previous R8 loop85 C26 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"049480","trigger_type":"Stage2-FalsePositive-SmallcapSecurityAITheme-NoARRRenewalBridge","entry_date":"2024-04-01","duplicate_status":"new C28 symbol/trigger/date combination outside top-covered list and previous R8 loop85 C26 symbols"}
```

## 4. Research question

C28 is not “software or security stock is strong.”  
The useful signal is the sticky contract: recurring subscription, renewal, enterprise seat expansion, ARR quality, maintenance retention, cloud conversion, and margin leverage. Without that bridge, AI/security headlines are only a login screen; they do not prove the user will keep paying.

Residual question:

```text
Can C28 distinguish:
1. software/AI contract-retention and recurring monetization bridge with large MFE,
2. security-theme beta with low MFE and later drawdown when fresh contract bridge is missing,
3. small-cap security/AI theme rebound where ARR renewal and enterprise customer bridge are absent?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C28_R8L86_030520_HANCOM_AI_SOFTWARE_CONTRACT_RETENTION","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_AI_CONTRACT_RETENTION_ARR_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-SoftwareAIContractRetentionARRBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_with_bridge_but_volatile_MAE","current_profile_verdict":"current_profile_correct_if_contract_retention_bridge_required","price_source":"Songdaiki/stock-web","notes":"Software/AI monetization and retention proxy produced high MFE. The drawdown risk means Green still requires exact ARR, renewal, enterprise-contract and margin evidence."}
{"row_type":"case","case_id":"C28_R8L86_053800_AHNLAB_SECURITY_THEME_NO_FRESH_RETENTION","symbol":"053800","company_name":"안랩","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_THEME_BETA_WITHOUT_FRESH_CONTRACT_RETENTION_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SecurityThemeBeta-NoFreshContractRetentionBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_security_beta_overcredited","price_source":"Songdaiki/stock-web","notes":"Security/value-up/theme beta had very low MFE and later high MAE without fresh enterprise contract, ARR or renewal bridge."}
{"row_type":"case","case_id":"C28_R8L86_049480_OPENBASE_SECURITY_AI_THEME_NO_ARR","symbol":"049480","company_name":"오픈베이스","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SMALLCAP_SECURITY_AI_THEME_WITHOUT_ARR_RENEWAL_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SmallcapSecurityAITheme-NoARRRenewalBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_medium_MAE","current_profile_verdict":"current_profile_false_positive_if_AI_security_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Small-cap AI/security theme had low MFE and mediocre forward path without ARR, renewal or enterprise retention bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 030520 한글과컴퓨터 — software/AI contract-retention bridge positive

Entry row: `2024-01-10 c=24750`.  
Observed path: high `2024-01-22 h=38450`, pullback lows around `2024-01-29 l=22850` and `2024-04-11 l=19750`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L86_C28_030520_20240110_STAGE2_SOFTWARE_AI_CONTRACT_RETENTION","case_id":"C28_R8L86_030520_HANCOM_AI_SOFTWARE_CONTRACT_RETENTION","symbol":"030520","company_name":"한글과컴퓨터","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_AI_CONTRACT_RETENTION_ARR_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-SoftwareAIContractRetentionARRBridge-Positive","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":24750.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_software_AI_contract_retention_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; software/AI contract retention and recurring monetization bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["AI_software_monetization_proxy","contract_retention_proxy","enterprise_customer_proxy","relative_strength_turn"],"stage3_evidence_fields":["ARR_bridge_pending","renewal_rate_pending","margin_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/030/030520/2024.csv","profile_path":"atlas/symbol_profiles/030/030520.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":55.35,"MFE_90D_pct":55.35,"MFE_180D_pct":55.35,"MAE_30D_pct":-7.68,"MAE_90D_pct":-20.20,"MAE_180D_pct":-20.20,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-22","peak_price":38450.0,"max_drawdown_low_date":"2024-04-11","max_drawdown_low":19750.0,"drawdown_after_peak_pct":-48.64,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_volatile; do not upgrade to Green without exact ARR/retention/margin evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_with_bridge_but_volatile_MAE","current_profile_verdict":"current_profile_correct_if_contract_retention_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"030520_2024-01-10_24750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C28 can allow Stage2/Yellow when software/AI strength is tied to contract retention, ARR and enterprise-customer bridge. However, volatility means Green must require exact non-price confirmation."}
```

### 6.2 053800 안랩 — security theme beta without fresh contract-retention bridge

Entry row: `2024-01-25 c=74000`.  
Observed path: local high `2024-01-29 h=75800`, later lows `2024-06-10 l=61000` and `2024-10-11 l=51800`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L86_C28_053800_20240125_STAGE2_FALSE_POSITIVE_SECURITY_THEME_BETA","case_id":"C28_R8L86_053800_AHNLAB_SECURITY_THEME_NO_FRESH_RETENTION","symbol":"053800","company_name":"안랩","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_THEME_BETA_WITHOUT_FRESH_CONTRACT_RETENTION_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SecurityThemeBeta-NoFreshContractRetentionBridge","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":74000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_security_theme_beta_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; security/value-up/policy beta treated as insufficient without fresh enterprise contract, ARR, retention and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["security_theme_beta","relative_strength_rebound"],"stage3_evidence_fields":["fresh_contract_bridge_missing","ARR_retention_missing","enterprise_customer_expansion_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","retention_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053800/2024.csv","profile_path":"atlas/symbol_profiles/053/053800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.43,"MFE_90D_pct":2.43,"MFE_180D_pct":2.43,"MAE_30D_pct":-5.81,"MAE_90D_pct":-17.57,"MAE_180D_pct":-30.00,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-29","peak_price":75800.0,"max_drawdown_low_date":"2024-10-11","max_drawdown_low":51800.0,"drawdown_after_peak_pct":-31.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"security_beta_without_fresh_contract_retention_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","retention_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_security_beta_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"053800_2024-01-25_74000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C28 should not upgrade security theme beta unless contract retention, ARR, enterprise-customer and margin bridge are verified. Low MFE and high 180D MAE support Watch/4B-risk."}
```

### 6.3 049480 오픈베이스 — small-cap security/AI theme without ARR renewal bridge

Entry row: `2024-04-01 c=2670`.  
Observed path: same-day high `2730`, later lows around `2024-10-18 l=2225` and `2024-12-06 l=2205`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L86_C28_049480_20240401_STAGE2_FALSE_POSITIVE_SECURITY_AI_THEME","case_id":"C28_R8L86_049480_OPENBASE_SECURITY_AI_THEME_NO_ARR","symbol":"049480","company_name":"오픈베이스","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SMALLCAP_SECURITY_AI_THEME_WITHOUT_ARR_RENEWAL_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-SmallcapSecurityAITheme-NoARRRenewalBridge","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":2670.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_smallcap_security_AI_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; small-cap security/AI theme treated as insufficient without ARR, renewal, enterprise customer and recurring maintenance bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["AI_security_theme","smallcap_relative_strength"],"stage3_evidence_fields":["ARR_bridge_missing","renewal_rate_missing","enterprise_contract_missing","maintenance_margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","ARR_renewal_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/049/049480/2024.csv","profile_path":"atlas/symbol_profiles/049/049480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.25,"MFE_90D_pct":2.25,"MFE_180D_pct":2.25,"MAE_30D_pct":-7.87,"MAE_90D_pct":-14.61,"MAE_180D_pct":-16.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":2730.0,"max_drawdown_low_date":"2024-10-18","max_drawdown_low":2225.0,"drawdown_after_peak_pct":-18.50,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smallcap_security_AI_theme_without_ARR_renewal_bridge_should_remain_watch_not_Yellow","four_b_evidence_type":["price_only","ARR_renewal_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_medium_MAE","current_profile_verdict":"current_profile_false_positive_if_AI_security_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"049480_2024-04-01_2670","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C28 should not treat a small-cap AI/security theme rebound as contract-retention evidence. Low MFE and missing ARR/renewal bridge should block Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C28_R8L86_030520_HANCOM_AI_SOFTWARE_CONTRACT_RETENTION","trigger_id":"R8L86_C28_030520_20240110_STAGE2_SOFTWARE_AI_CONTRACT_RETENTION","symbol":"030520","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C28 requires software contract retention and recurring monetization bridge rather than AI/security theme alone","raw_component_scores_before":{"contract_retention_score":13,"ARR_or_recurring_revenue_score":12,"enterprise_customer_score":12,"renewal_rate_score":9,"margin_bridge_score":9,"relative_strength_score":14,"valuation_repricing_score":9,"execution_risk_score":-6,"theme_spike_risk":-3,"information_confidence":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"contract_retention_score":16,"ARR_or_recurring_revenue_score":15,"enterprise_customer_score":14,"renewal_rate_score":11,"margin_bridge_score":11,"relative_strength_score":15,"valuation_repricing_score":10,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":6},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"AI/software monetization and contract-retention bridge support Yellow-watch; volatile MAE and proxy-only evidence block Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C28_R8L86_053800_AHNLAB_SECURITY_THEME_NO_FRESH_RETENTION","trigger_id":"R8L86_C28_053800_20240125_STAGE2_FALSE_POSITIVE_SECURITY_THEME_BETA","symbol":"053800","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"security beta without fresh contract/ARR bridge should be blocked","raw_component_scores_before":{"contract_retention_score":4,"ARR_or_recurring_revenue_score":2,"enterprise_customer_score":3,"renewal_rate_score":2,"margin_bridge_score":2,"relative_strength_score":9,"valuation_repricing_score":5,"execution_risk_score":-10,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":26,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"contract_retention_score":0,"ARR_or_recurring_revenue_score":0,"enterprise_customer_score":1,"renewal_rate_score":0,"margin_bridge_score":0,"relative_strength_score":3,"valuation_repricing_score":2,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high 180D MAE convert security beta into missing-retention bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C28_R8L86_049480_OPENBASE_SECURITY_AI_THEME_NO_ARR","trigger_id":"R8L86_C28_049480_20240401_STAGE2_FALSE_POSITIVE_SECURITY_AI_THEME","symbol":"049480","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"small-cap AI/security theme without ARR/renewal bridge should remain Watch/blocked","raw_component_scores_before":{"contract_retention_score":2,"ARR_or_recurring_revenue_score":1,"enterprise_customer_score":2,"renewal_rate_score":1,"margin_bridge_score":1,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-8,"theme_spike_risk":-10,"information_confidence":3},"weighted_score_before":22,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"contract_retention_score":0,"ARR_or_recurring_revenue_score":0,"enterprise_customer_score":0,"renewal_rate_score":0,"margin_bridge_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Watch-Blocked","component_delta_explanation":"Low MFE and missing recurring-revenue bridge should block Yellow/Green even before extreme MAE appears."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R8L86_C28_P0_CURRENT","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C28 needs explicit contract retention, ARR, renewal and enterprise-customer bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":20.01,"avg_MAE90_pct":-17.46,"avg_MFE180_pct":20.01,"avg_MAE180_pct":-22.29,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C28_contract_retention_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R8L86_C28_P1_SECTOR_SPECIFIC","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P1_L8_contract_retention_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L8 software/security signals need contract retention, ARR, renewal, enterprise customer or margin bridge before Stage2-Actionable","changed_axes":["contract_retention_required","ARR_renewal_required","AI_security_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_contract_retention_ARR_renewal_enterprise_customer_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":20.01,"avg_MAE90_pct":-17.46,"avg_MFE180_pct":20.01,"avg_MAE180_pct":-22.29,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R8L86_C28_P2_CANONICAL","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P2_C28_contract_retention_ARR_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C28 should reward retention and recurring monetization, not AI/security headline beta","changed_axes":["C28_contract_retention_ARR_bridge_required","C28_AI_security_theme_local_4B_guard","C28_renewal_margin_bridge_required"],"changed_thresholds":{"stage2_yellow_gate":"contract_retention_or_ARR_renewal_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":20.01,"avg_MAE90_pct":-17.46,"avg_MFE180_pct":20.01,"avg_MAE180_pct":-22.29,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R8L86_C28_P3_COUNTEREXAMPLE_GUARD","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P3_C28_low_MFE_missing_retention_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 while contract-retention/ARR bridge is missing, block Yellow/Green; if MAE180<=-30, force 4B-watch","changed_axes":["C28_low_MFE_guardrail","C28_high_180D_MAE_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_bridge_missing; hard_4B_if_MAE180_le_minus_30"},"eligible_trigger_count":3,"avg_MFE90_pct":20.01,"avg_MAE90_pct":-17.46,"avg_MFE180_pct":20.01,"avg_MAE180_pct":-22.29,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_RETENTION_ARR_BRIDGE_VS_AI_SECURITY_THEME","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":20.01,"avg_MAE90_pct":-17.46,"avg_MFE180_pct":20.01,"avg_MAE180_pct":-22.29,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_5":0.67,"stage2_bad_entry_rate_MAE180_le_minus_30":0.33,"interpretation":"C28 needs bridge discipline. 한글과컴퓨터 shows software/AI monetization can work when contract-retention and recurring bridge exists, while 안랩 and 오픈베이스 show AI/security theme beta can fail or stagnate without fresh contract, ARR, renewal and enterprise-customer evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"030520","trigger_type":"Stage2-Actionable-SoftwareAIContractRetentionARRBridge-Positive","entry_date":"2024-01-10","stage2_to_90D_outcome":"good_stage2_high_MFE_but_volatile_MAE","stage2_to_180D_outcome":"positive_bridge_with_drawdown_risk","MFE90_ge_20":true,"MAE90_le_minus_20":true,"transition_note":"Allow Stage2/Yellow when contract-retention/ARR bridge exists; Green requires exact renewal, enterprise customer and margin evidence."}
{"row_type":"stage_transition_summary","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"053800","trigger_type":"Stage2-FalsePositive-SecurityThemeBeta-NoFreshContractRetentionBridge","entry_date":"2024-01-25","stage2_to_90D_outcome":"weak_stage2_low_MFE","stage2_to_180D_outcome":"failed_security_beta_high_180D_MAE","MFE90_ge_20":false,"MAE180_le_minus_30":true,"transition_note":"Security theme beta without fresh contract/ARR bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"049480","trigger_type":"Stage2-FalsePositive-SmallcapSecurityAITheme-NoARRRenewalBridge","entry_date":"2024-04-01","stage2_to_90D_outcome":"weak_stage2_low_MFE_medium_MAE","stage2_to_180D_outcome":"failed_or_stagnant_AI_security_theme","MFE90_ge_20":false,"MAE180_le_minus_30":false,"transition_note":"Small-cap security/AI theme without ARR and renewal bridge should remain Watch/blocked from Yellow/Green."}
{"row_type":"residual_contribution","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_type":"software_security_theme_overcredit_without_contract_retention_ARR_renewal_bridge","contribution":"Adds two C28 local 4B/weak-bridge counterexamples against one software/AI contract-retention positive, avoiding C28 top-covered and previous R8 loop85 C26 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_AI_CONTRACT_RETENTION_ARR_BRIDGE_VS_SECURITY_AI_THEME_REBOUND_WITHOUT_RECURRING_REVENUE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C28 now has non-top-symbol AI/security theme counterexamples; next R8 loops should exact-URL repair ARR, renewal, contract-retention, enterprise customer and margin bridge evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_contract_retention_ARR_renewal_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"030520 worked when software/AI monetization was tied to contract-retention/ARR proxy; 053800 and 049480 failed or stagnated when only security/AI theme beta existed."}
{"row_type":"shadow_weight","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_AI_security_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"AI/security theme rows showed low MFE without fresh recurring-revenue or retention bridge."}
{"row_type":"shadow_weight","round":"R8","loop":"86","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_low_MFE_missing_retention_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<5 while contract-retention/ARR bridge is missing, block Stage2-Actionable/Yellow; if MAE180<=-30, route to 4B-watch."}
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
  - AI_security_theme_overcredit
  - contract_retention_bridge_missing
  - ARR_renewal_bridge_missing
  - low_MFE_without_recurring_revenue_bridge
new_axis_proposed:
  - C28_contract_retention_ARR_renewal_bridge_required_shadow_only
  - C28_AI_security_theme_local_4B_watch_guard_shadow_only
  - C28_low_MFE_missing_retention_guardrail_shadow_only
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
5. Confirm this loop avoided:
   - C28 top-covered symbols
   - previous R8 loop85 C26 symbols listed in the MD
6. If aggregate support remains stable after exact evidence URL repair, consider C28-scoped safe patch candidates:
   - C28_contract_retention_ARR_renewal_bridge_required
   - C28_AI_security_theme_local_4B_watch_guard
   - C28_low_MFE_missing_retention_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R8
completed_loop = 86
next_round = R9
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.
```

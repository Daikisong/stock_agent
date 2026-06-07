# E2R Stock-Web v12 Residual Research — R8 Loop 93 / L8 / C28

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R8
loop: 93
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: SCM_SAAS_CONTRACT_RETENTION_BRIDGE_VS_ENDPOINT_SECURITY_AND_CERTIFICATE_THEME_DECAY
sector: platform / software / security / SaaS / SCM / endpoint security / certificate security / contract renewal / retention / ARR / margin / cash conversion
output_file: e2r_stock_web_v12_residual_round_R8_loop_93_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after recent loop93 expansions in C09, C01, C07, C06, C10, C11, C19, C27, C24, C12, C13, C17 and C23.

```text
selected_round = R8
selected_loop = 93
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

Reason for selecting C28:

```text
v12 scheduler = coverage_index_first
sequential_round_cycle_required = false
coverage_gap_can_override_previous_round = true
selected_archetype_drives_round = true
```

No-Repeat Index under-30 snapshot used as duplicate-avoidance ledger:

```text
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION = 27 rows / need_to_30 = 3
```

Local stream note:

```text
C28 was expanded once in loop92, but the GitHub No-Repeat Index still shows C28 at 27 raw rows.
This run uses three new symbols / trigger families and avoids the already used local loop92 C28 symbols.
```

Avoided C28 top-covered and recent R8/C28 symbols:

```text
C28 top-covered = 053800, 030520, 136540, 047560, 060850, 356680

R8 loop86 C28: 030520, 053800, 049480
R8 loop89 C28: 060850, 067920, 304100
R8 loop92 C28: 012510, 150900, 042510
```

Candidate hygiene note:

```text
During this execution path, C23/C17/C13/C12 candidate rows were visible from the stream.
They are not used in this C28 output because the valid output must be R8/L8/C28.
```

Selected symbols:

```text
058970, 263860, 192250
```

The selected pocket is:

```text
SCM / procurement SaaS contract and renewal bridge positive-watch
vs
endpoint security vocabulary after a January price spike without durable renewal / ARR / margin bridge
vs
certificate / security theme spike with raw corporate-action contamination that blocks promotion
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"058970","company_name":"엠로","profile_path":"atlas/symbol_profiles/058/058970.json","first_date":"2016-05-04","last_date":"2026-02-20","trading_day_count":2224,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2022-01-17","2022-02-09"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window. Share-count movement appears in late 2024 and should be repaired before production patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_2024_entry_window_usable; late_2024_share_count_watch"}
{"row_type":"price_source_validation","symbol":"263860","company_name":"지니언스","profile_path":"atlas/symbol_profiles/263/263860.json","first_date":"2017-08-02","last_date":"2026-02-20","trading_day_count":2095,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2018-07-05","2018-07-24"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
{"row_type":"price_source_validation","symbol":"192250","company_name":"케이사인","profile_path":"atlas/symbol_profiles/192/192250.json","first_date":"2014-04-28","last_date":"2026-02-20","trading_day_count":2848,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2014-11-11","2024-11-01"],"has_major_raw_discontinuity":true,"calibration_caveat":"2024-11-01 corporate-action/share-count candidate contaminates raw forward-window prices; use only pre-candidate path for ordinary MFE/MAE and keep data-quality watch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"selected_entry_before_2024-11-01_candidate; post_candidate_price_blocked"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"058970","trigger_type":"Stage2-Actionable-SCMSaaSContractRetentionRevenueBridge-PositiveWatch","entry_date":"2024-02-27","duplicate_status":"new C28 symbol/trigger/date combination outside C28 top-covered and recent R8 C28 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"263860","trigger_type":"Stage2-FalsePositive-EndpointSecurityVocabularyNoDurableRenewalARRMarginBridge","entry_date":"2024-01-24","duplicate_status":"new C28 symbol/trigger/date combination outside C28 top-covered and recent R8 C28 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"192250","trigger_type":"Stage2-FalsePositive-CertificateSecurityThemeSpikeNoRetentionBridgeCAWatch","entry_date":"2024-03-26","duplicate_status":"new C28 symbol/trigger/date combination outside C28 top-covered and recent R8 C28 loop symbols; 2024-11-01 CA/share-count watch"}
```

## 4. Research question

C28 is not “소프트웨어/보안 테마가 있다.”
The useful software/security signal must prove the contract-retention-to-margin chain:

```text
named enterprise customer or vertical
contract renewal / subscription / license visibility
retention or ARR / recurring revenue
implementation / expansion path
module attach or upsell
gross-margin / operating leverage
working-capital discipline
cash conversion
security incident / public-sector theme risk containment
```

A software headline without this bridge is a login screen with no paid renewal behind it. E2R needs the invoice, renewal, user expansion, margin and cash.

Residual question:

```text
Can C28 distinguish:
1. SCM/procurement SaaS contract-retention bridge that can support positive-watch,
2. endpoint-security vocabulary where price spike lacks durable renewal / ARR / margin evidence,
3. certificate/security theme spike where corporate-action contamination and missing retention bridge block promotion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C28_R8L93_058970_EMRO_SCM_SAAS_RETENTION","symbol":"058970","company_name":"엠로","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SCM_SAAS_CONTRACT_RETENTION_REVENUE_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-SCMSaaSContractRetentionRevenueBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"score_price_alignment":"positive_watch_MFE90_ge40_low_entry_MAE_but_late_share_count_watch","current_profile_verdict":"current_profile_correct_if_contract_retention_ARR_margin_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"SCM/procurement SaaS contract-retention proxy after a reset produced MFE90 above 40 with shallow early MAE. Green still requires exact customer, subscription/renewal, ARR, margin and cash evidence; late share-count movement requires repair."}
{"row_type":"case","case_id":"C28_R8L93_263860_GENIANS_ENDPOINT_SECURITY_DECAY","symbol":"263860","company_name":"지니언스","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENDPOINT_SECURITY_VOCABULARY_WITHOUT_DURABLE_RENEWAL_ARR_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-EndpointSecurityVocabularyNoDurableRenewalARRMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_endpoint_security_vocabulary_no_retention_bridge","current_profile_verdict":"current_profile_false_positive_if_endpoint_security_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Endpoint/security vocabulary after a January spike had only tiny forward MFE and later deep MAE when renewal/ARR/module expansion evidence was missing."}
{"row_type":"case","case_id":"C28_R8L93_192250_KSIGN_CERT_SECURITY_CA_WATCH","symbol":"192250","company_name":"케이사인","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CERTIFICATE_SECURITY_THEME_SPIKE_WITHOUT_RETENTION_BRIDGE_CA_WATCH","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CertificateSecurityThemeSpikeNoRetentionBridgeCAWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"score_price_alignment":"counterexample_theme_spike_low_clean_MFE_deep_MAE_CA_contaminated_forward_window","current_profile_verdict":"current_profile_false_positive_if_certificate_security_theme_or_post_CA_price_counted_as_retention_evidence","price_source":"Songdaiki/stock-web","notes":"Certificate/security theme spike lacked renewal/ARR/margin bridge, and the raw 2024-11-01 corporate-action candidate contaminates later prices. Post-CA raw price must not validate the original entry."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 058970 엠로 — SCM / procurement SaaS contract-retention bridge positive-watch

Entry row: `2024-02-27 c=53300`, after a February reset.
Observed path: entry low `2024-02-27 l=52300`, local high `2024-03-27 h=72000`, MFE90 high `2024-05-31 h=76300`, and later raw low `2024-10-29 l=43500`. Late-year share-count movement appears in the row stream and is kept as a data-quality watch.

```jsonl
{"row_type":"trigger","trigger_id":"R8L93_C28_058970_20240227_STAGE2_SCM_SAAS_RETENTION","case_id":"C28_R8L93_058970_EMRO_SCM_SAAS_RETENTION","symbol":"058970","company_name":"엠로","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SCM_SAAS_CONTRACT_RETENTION_REVENUE_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test;data_quality_watch","trigger_type":"Stage2-Actionable-SCMSaaSContractRetentionRevenueBridge-PositiveWatch","trigger_date":"2024-02-27","entry_date":"2024-02-27","entry_price":53300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_SCM_SaaS_contract_retention_revenue_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; SCM/procurement software contract renewal, customer expansion, SaaS/subscription revenue, margin and cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["SCM_SaaS_contract_proxy","enterprise_customer_proxy","renewal_retention_proxy","margin_cash_proxy"],"stage3_evidence_fields":["exact_contract_source_pending","retention_or_ARR_source_pending","module_expansion_source_pending","margin_cash_source_pending","late_share_count_repair_pending"],"stage4b_evidence_fields":["MFE90_ge40_watch","late_drawdown_watch","Green_exact_evidence_watch","late_share_count_watch"],"stage4c_evidence_fields":["contract_churn_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058970/2024.csv","profile_path":"atlas/symbol_profiles/058/058970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":35.08,"MFE_90D_pct":43.15,"MFE_180D_pct":43.15,"MAE_30D_pct":-1.88,"MAE_90D_pct":-1.88,"MAE_180D_pct":-18.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":76300.0,"max_drawdown_low_date":"2024-10-29","max_drawdown_low":43500.0,"drawdown_after_peak_pct":-43.00,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_contract_retention_ARR_margin_cash_evidence_and_late_share_count_repair","four_b_evidence_type":["MFE90_ge40_watch","late_drawdown_watch","Green_exact_evidence_watch","late_share_count_watch"],"four_c_protection_label":"contract_churn_watch_only","trigger_outcome_label":"positive_watch_MFE90_ge40_low_entry_MAE_but_late_share_count_watch","current_profile_verdict":"current_profile_correct_if_contract_retention_ARR_margin_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["late_2024_share_count_movement_watch_before_patch"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_entry_window_usable; late_share_count_watch","same_entry_group_id":"058970_2024-02-27_53300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"do_not_count_as_new_case":false,"current_profile_residual":"C28 can allow Yellow/Green-candidate-watch when software strength is tied to customer contract, retention/ARR, module expansion, margin and cash conversion. Late drawdown and share-count watch block automatic Green."}
```

### 6.2 263860 지니언스 — endpoint-security vocabulary without durable renewal / ARR bridge

Entry row: `2024-01-24 c=15550`, after a January endpoint-security price spike.
Observed path: local high `2024-01-29 h=16000`, then decline to `2024-04-08 l=11740` and later `2024-12-09 l=8580`.

```jsonl
{"row_type":"trigger","trigger_id":"R8L93_C28_263860_20240124_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY","case_id":"C28_R8L93_263860_GENIANS_ENDPOINT_SECURITY_DECAY","symbol":"263860","company_name":"지니언스","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"ENDPOINT_SECURITY_VOCABULARY_WITHOUT_DURABLE_RENEWAL_ARR_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-EndpointSecurityVocabularyNoDurableRenewalARRMarginBridge","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":15550.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_endpoint_security_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; endpoint/EDR/NAC/security vocabulary treated as insufficient without enterprise renewal, ARR, module expansion, gross-margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["endpoint_security_vocabulary","security_spike_keyword","relative_strength_spike"],"stage3_evidence_fields":["enterprise_renewal_missing","ARR_retention_missing","module_expansion_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE","deep_MAE","retention_bridge_missing_watch"],"stage4c_evidence_fields":["contract_churn_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263860/2024.csv","profile_path":"atlas/symbol_profiles/263/263860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.89,"MFE_90D_pct":2.89,"MFE_180D_pct":2.89,"MAE_30D_pct":-15.95,"MAE_90D_pct":-24.50,"MAE_180D_pct":-38.84,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-29","peak_price":16000.0,"max_drawdown_low_date":"2024-10-04","max_drawdown_low":9510.0,"drawdown_after_peak_pct":-40.56,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"endpoint_security_vocabulary_without_enterprise_renewal_ARR_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","deep_MAE","retention_bridge_missing_watch"],"four_c_protection_label":"contract_churn_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_endpoint_security_vocabulary_no_retention_bridge","current_profile_verdict":"current_profile_false_positive_if_endpoint_security_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"263860_2024-01-24_15550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C28 should not promote endpoint/security vocabulary unless renewal, ARR retention, module expansion, gross-margin and cash evidence are exact-repaired. Low forward MFE and deep MAE require Watch/4B."}
```

### 6.3 192250 케이사인 — certificate-security theme spike, no retention bridge, raw CA watch

Entry row: `2024-03-26 c=1614`, the day of a certificate/security theme spike.
Observed clean pre-CA path: `2024-03-27 h=1736`, then decline to `2024-10-11 l=954`.
A raw corporate-action/share-count candidate appears on `2024-11-01`; post-candidate raw prices are blocked from validating the original trigger.

```jsonl
{"row_type":"trigger","trigger_id":"R8L93_C28_192250_20240326_STAGE2_FALSE_POSITIVE_CERT_SECURITY_CA","case_id":"C28_R8L93_192250_KSIGN_CERT_SECURITY_CA_WATCH","symbol":"192250","company_name":"케이사인","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CERTIFICATE_SECURITY_THEME_SPIKE_WITHOUT_RETENTION_BRIDGE_CA_WATCH","loop_objective":"residual_false_positive_mining;counterexample_mining;data_quality_watch;post_CA_price_block","trigger_type":"Stage2-FalsePositive-CertificateSecurityThemeSpikeNoRetentionBridgeCAWatch","trigger_date":"2024-03-26","entry_date":"2024-03-26","entry_price":1614.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_certificate_security_theme_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; certificate/security theme spike treated as insufficient without contract renewal, retention, ARR, margin and cash bridge","evidence_source_type":"historical_public_theme_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["certificate_security_keyword","theme_spike","price_MFE"],"stage3_evidence_fields":["renewal_contract_missing","ARR_retention_missing","margin_cash_bridge_missing","CA_repair_pending"],"stage4b_evidence_fields":["theme_spike_low_clean_MFE","deep_clean_MAE","post_CA_price_block","retention_bridge_missing_watch"],"stage4c_evidence_fields":["CA_contamination_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/192/192250/2024.csv","profile_path":"atlas/symbol_profiles/192/192250.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.56,"MFE_90D_pct":7.56,"MFE_180D_pct":7.56,"MAE_30D_pct":-20.57,"MAE_90D_pct":-28.19,"MAE_180D_pct":-40.89,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-27","peak_price":1736.0,"max_drawdown_low_date":"2024-10-11","max_drawdown_low":954.0,"drawdown_after_peak_pct":-45.05,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"certificate_security_theme_spike_without_contract_retention_margin_cash_bridge_should_be_4B_watch; post_2024-11-01_raw_CA_prices_must_not_validate_original_entry","four_b_evidence_type":["theme_spike_low_clean_MFE","deep_clean_MAE","post_CA_price_block","retention_bridge_missing_watch"],"four_c_protection_label":"CA_contamination_watch_only","trigger_outcome_label":"counterexample_theme_spike_low_clean_MFE_deep_MAE_CA_contaminated_forward_window","current_profile_verdict":"current_profile_false_positive_if_certificate_security_theme_or_post_CA_price_counted_as_retention_evidence","calibration_usable":true,"forward_window_trading_days":"clean_pre_2024-11-01_window_only_for_ordinary_MFE_MAE","calibration_block_reasons":["2024-11-01_corporate_action_share_count_candidate_blocks_post_candidate_price_validation"],"corporate_action_window_status":"selected_entry_before_2024-11-01_candidate; post_candidate_raw_price_blocked","same_entry_group_id":"192250_2024-03-26_1614","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"do_not_count_as_new_case":false,"current_profile_residual":"C28 should not count certificate/security theme spikes or post-CA raw prices as contract-retention validation. Renewal, ARR, margin and cash evidence must be exact-repaired before promotion."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L93_058970_EMRO_SCM_SAAS_RETENTION","trigger_id":"R8L93_C28_058970_20240227_STAGE2_SCM_SAAS_RETENTION","symbol":"058970","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C28 requires contract renewal, ARR retention, enterprise customer expansion, margin and cash bridge rather than software vocabulary alone","raw_component_scores_before":{"enterprise_customer_score":11,"contract_renewal_score":12,"ARR_retention_score":11,"module_expansion_score":10,"implementation_expansion_score":9,"gross_margin_score":9,"operating_leverage_score":8,"cash_conversion_score":7,"relative_strength_score":13,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"enterprise_customer_score":14,"contract_renewal_score":15,"ARR_retention_score":14,"module_expansion_score":12,"implementation_expansion_score":11,"gross_margin_score":11,"operating_leverage_score":10,"cash_conversion_score":9,"relative_strength_score":14,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"SCM SaaS contract-retention bridge plus MFE90 supports Green-candidate watch; exact evidence, late drawdown and share-count repair block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L93_263860_GENIANS_ENDPOINT_SECURITY_DECAY","trigger_id":"R8L93_C28_263860_20240124_STAGE2_FALSE_POSITIVE_ENDPOINT_SECURITY","symbol":"263860","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"endpoint/security vocabulary without durable renewal and ARR bridge should be blocked","raw_component_scores_before":{"enterprise_customer_score":2,"contract_renewal_score":0,"ARR_retention_score":0,"module_expansion_score":0,"implementation_expansion_score":0,"gross_margin_score":0,"operating_leverage_score":0,"cash_conversion_score":0,"relative_strength_score":2,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"enterprise_customer_score":0,"contract_renewal_score":0,"ARR_retention_score":0,"module_expansion_score":0,"implementation_expansion_score":0,"gross_margin_score":0,"operating_leverage_score":0,"cash_conversion_score":0,"relative_strength_score":0,"execution_risk_score":-24,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and deep MAE require renewal, ARR, module expansion and cash evidence before any Yellow/Green promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L93_192250_KSIGN_CERT_SECURITY_CA_WATCH","trigger_id":"R8L93_C28_192250_20240326_STAGE2_FALSE_POSITIVE_CERT_SECURITY_CA","symbol":"192250","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_scope":"current_default_proxy","profile_hypothesis":"certificate/security theme spike and post-corporate-action raw price should not validate missing retention bridge","raw_component_scores_before":{"enterprise_customer_score":0,"contract_renewal_score":0,"ARR_retention_score":0,"module_expansion_score":0,"implementation_expansion_score":0,"gross_margin_score":0,"operating_leverage_score":0,"cash_conversion_score":0,"relative_strength_score":5,"execution_risk_score":-18,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"enterprise_customer_score":0,"contract_renewal_score":0,"ARR_retention_score":0,"module_expansion_score":0,"implementation_expansion_score":0,"gross_margin_score":0,"operating_leverage_score":0,"cash_conversion_score":0,"relative_strength_score":0,"execution_risk_score":-28,"theme_spike_risk":-24,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Theme spike, deep clean MAE and post-CA contamination block promotion until renewal/ARR/margin evidence and raw-price repair are available."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R8L93_C28_P0_CURRENT","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C28 needs explicit contract-renewal, retention/ARR, module expansion, margin/cash and CA/data-quality taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":17.87,"avg_MAE90_pct":-18.19,"avg_MFE180_pct":17.87,"avg_MAE180_pct":-32.71,"false_positive_rate":0.67,"data_quality_watch_count":2,"score_return_alignment_verdict":"mixed_without_C28_contract_retention_ARR_margin_cash_guard"}
{"row_type":"profile_comparison","comparison_id":"R8L93_C28_P1_SECTOR_SPECIFIC","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P1_L8_software_security_contract_retention_candidate","profile_scope":"sector_specific","profile_hypothesis":"L8 software/security signals need contract renewal, retention/ARR, module expansion, gross margin or cash conversion before Stage2-Actionable","changed_axes":["contract_renewal_required","ARR_retention_required","security_theme_vocabulary_penalty","CA_raw_price_guard"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_contract_renewal_retention_ARR_module_margin_or_cash_proxy"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R8L93_C28_P2_CANONICAL","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P2_C28_retention_ARR_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C28 should reward renewal/retention-to-cash mechanics, not software/security vocabulary or raw post-CA price","changed_axes":["C28_contract_retention_ARR_margin_cash_bridge_required","C28_endpoint_certificate_security_vocabulary_local_4B_guard","C28_CA_post_price_nonvalidation_guard","C28_late_share_count_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"enterprise_customer_or_contract_plus_renewal_retention_or_margin_cash_bridge_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R8L93_C28_P3_COUNTEREXAMPLE_GUARD","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P3_C28_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If retention/ARR bridge is missing, MFE90<10 or MAE90<=-20 blocks Yellow/Green and routes to Watch/4B","changed_axes":["C28_low_MFE_guardrail","C28_deep_MAE_guardrail","C28_post_CA_raw_price_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_10_or_MAE90_le_minus20_or_post_CA_price_contaminated)"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate and transition rows

```jsonl
{"row_type":"aggregate_metric","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SCM_SAAS_POSITIVE_VS_SECURITY_CERTIFICATE_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":2,"avg_MFE90_pct":17.87,"avg_MAE90_pct":-18.19,"avg_MFE180_pct":17.87,"avg_MAE180_pct":-32.71,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE90_le_minus20":0.67,"interpretation":"C28 needs renewal/ARR discipline. 엠로 shows SCM SaaS contract-retention and margin bridge can support Green-candidate-watch, while 지니언스 and 케이사인 show security/certificate vocabulary should not be promoted without renewal, retention, ARR, margin and cash evidence. 케이사인은 post-CA raw price validation must be blocked."}
{"row_type":"stage_transition_summary","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"058970","trigger_type":"Stage2-Actionable-SCMSaaSContractRetentionRevenueBridge-PositiveWatch","entry_date":"2024-02-27","stage2_to_90D_outcome":"positive_watch_MFE90_ge40_low_entry_MAE","stage2_to_180D_outcome":"SCM_SaaS_retention_bridge_but_late_drawdown_and_share_count_watch","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/Green-candidate when software strength is tied to renewal, ARR, module expansion, margin and cash bridge; exact evidence and data-quality repair required."}
{"row_type":"stage_transition_summary","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"263860","trigger_type":"Stage2-FalsePositive-EndpointSecurityVocabularyNoDurableRenewalARRMarginBridge","entry_date":"2024-01-24","stage2_to_90D_outcome":"bad_stage2_low_MFE_deep_MAE","stage2_to_180D_outcome":"failed_endpoint_security_vocabulary_no_retention_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Endpoint/security vocabulary without renewal/ARR/margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","symbol":"192250","trigger_type":"Stage2-FalsePositive-CertificateSecurityThemeSpikeNoRetentionBridgeCAWatch","entry_date":"2024-03-26","stage2_to_90D_outcome":"bad_stage2_theme_spike_low_clean_MFE_deep_MAE","stage2_to_180D_outcome":"post_CA_raw_price_blocked_not_retention_validation","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"Certificate/security theme spike without retention bridge should stay Watch/4B; post-2024-11-01 raw corporate-action price is blocked from validation."}
{"row_type":"residual_contribution","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","residual_type":"endpoint_certificate_security_vocabulary_overcredit_without_contract_retention_ARR_margin_cash_bridge","contribution":"Adds two C28 4B counterexamples against one SCM/SaaS contract-retention positive-watch, bringing raw C28 from 27 toward the 30-row minimum stability threshold if reconciled into the No-Repeat Index.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SCM_SAAS_CONTRACT_RETENTION_BRIDGE_VS_ENDPOINT_SECURITY_AND_CERTIFICATE_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C28 now has one SCM SaaS contract-retention positive-watch and two endpoint/certificate weak-bridge counterexamples; next C28 loops should exact-URL repair enterprise contract renewal, ARR retention, module expansion, gross margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_contract_retention_ARR_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"058970 worked as positive-watch when SCM/SaaS contract-retention proxy existed; 263860 and 192250 failed when retention/ARR evidence was missing."}
{"row_type":"shadow_weight","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_endpoint_certificate_security_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"263860 and 192250 showed low forward MFE and deep MAE when security vocabulary was not tied to renewal, ARR, margin and cash evidence."}
{"row_type":"shadow_weight","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_CA_post_price_nonvalidation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"192250 has a 2024-11-01 corporate-action/share-count candidate; post-candidate raw price must not validate the pre-candidate trigger."}
{"row_type":"shadow_weight","round":"R8","loop":"93","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_late_share_count_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"058970 shows late-2024 share-count movement; Green or patch consideration requires price-path/evidence repair."}
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
  - endpoint_security_vocabulary_overcredit
  - certificate_security_theme_overcredit
  - contract_retention_ARR_bridge_missing
  - CA_post_price_nonvalidation
  - late_share_count_data_quality_watch
new_axis_proposed:
  - C28_contract_retention_ARR_margin_cash_bridge_required_shadow_only
  - C28_endpoint_certificate_security_vocabulary_local_4B_guard_shadow_only
  - C28_CA_post_price_nonvalidation_guard_shadow_only
  - C28_late_share_count_data_quality_guard_shadow_only
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
`058970` has older 2022 corporate-action candidates before selected 2024 entry, but visible late-2024 share-count movement appears and should be repaired before production patching.
`263860` has older 2018 corporate-action candidates before selected 2024 window; selected window is usable.
`192250` has a 2024-11-01 corporate-action/share-count candidate inside the 2024 row stream; post-candidate raw price is explicitly blocked from ordinary validation.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for residual price-path analysis
evidence_url_pending = true
source_proxy_only = true
late_share_count_watch = true for 058970
post_CA_price_block = true for 192250
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
3. Confirm R8 / L8 / C28 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop was selected by coverage-index-first and, if reconciled with the raw GitHub index, brings C28 toward the 30-row minimum stability threshold.
6. Confirm this loop avoided:
   - C28 top-covered symbols
   - previous R8 loop86 C28 symbols
   - previous R8 loop89 C28 symbols
   - previous R8 loop92 C28 symbols
7. Confirm recently touched C23/C17/C13/C12/C27/C19 candidate rows are not ingested from this MD.
8. Treat 058970 as Yellow/Green-candidate-watch only, not Green, until exact contract-retention/ARR/margin/cash evidence and late share-count quality are repaired.
9. Treat 263860 and 192250 as weak-bridge failure modes unless exact renewal/ARR/margin/cash evidence is added later.
10. Keep 192250 post-2024-11-01 raw prices blocked from original trigger validation.
11. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C28-scoped safe patch candidates:
   - C28_contract_retention_ARR_margin_cash_bridge_required
   - C28_endpoint_certificate_security_vocabulary_local_4B_guard
   - C28_CA_post_price_nonvalidation_guard
   - C28_late_share_count_data_quality_guard
12. Do not loosen Stage3-Green.
13. Do not use future MFE/MAE in runtime scoring.
14. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R8
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = recompute after reconciling local loop93 additions; if all under-30 axes are stabilized, rotate to next lowest residual gap outside recently repeated sectors
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 SCM/SaaS contract-retention positive-watch, 2 weak-bridge counterexamples, and 2 local 4B-watch rows for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.
```

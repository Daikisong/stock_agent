# E2R Stock-Web v12 Residual Research — R7 Loop 91 / L7 / C23

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R7
loop: 91
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: CNS_DRUG_COMMERCIALIZATION_REVENUE_BRIDGE_VS_CRL_APPROVAL_EXPECTATION_DIAGNOSTIC_VOCABULARY_DECAY
sector: bio / healthcare / regulatory approval / commercialization / CNS drug / CRL risk / diagnostics commercialization
output_file: e2r_stock_web_v12_residual_round_R7_loop_91_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R6 loop 91`.

```text
scheduled_round = R7
scheduled_loop = 91
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

R7 is restricted to bio / healthcare / medical.  
C23 is selected because the recent R7 path rotated C23 → C25 → C24 → C23 → C25 → C24, and R7 loop90 used C24.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
rows = 26
symbols = 14
good/bad Stage2 = 8/5
4B/4C = 0/2
top-covered = UNKNOWN_SYMBOL, 028300, 000100, 039200, 195940, 003850
```

This loop avoids the C23 top-covered list and recent R7 loop symbols:

```text
R7 loop85 C23: 145020, 302440, 086900
R7 loop86 C25: 335890, 228670, 065510
R7 loop87 C24: 196170, 206650, 950220
R7 loop88 C23: 000250, 019170, 095700
R7 loop89 C25: 200670, 119610, 290650
R7 loop90 C24: 237690, 365270, 256840
```

Candidate hygiene note:

```text
During this execution path, R6/C21 and several earlier financial/consumer/material candidate rows were accidentally touched or one stale file was regenerated.
Those rows are not used in this R7/C23 output.
```

Selected symbols:

```text
326030, 067630, 229000
```

The selected pocket is:

```text
CNS drug commercialization / revenue bridge
vs
approval-expectation / CRL event failure without regulatory de-risking
vs
diagnostic commercialization vocabulary without reimbursement/adoption/cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"326030","company_name":"SK바이오팜","profile_path":"atlas/symbol_profiles/326/326030.json","first_date":"2020-07-02","last_date":"2026-02-20","trading_day_count":1382,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"067630","company_name":"HLB생명과학","profile_path":"atlas/symbol_profiles/067/067630.json","first_date":"2008-11-25","last_date":"2026-02-20","trading_day_count":4242,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["2013-09-03","2015-11-10","2018-11-08","2019-04-04","2021-03-15","2021-04-01"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"229000","company_name":"젠큐릭스","profile_path":"atlas/symbol_profiles/229/229000.json","first_date":"2015-10-27","last_date":"2026-02-20","trading_day_count":2347,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2016-01-15","2023-05-08","2026-01-26"],"has_major_raw_discontinuity":true,"calibration_caveat":"2026 corporate-action candidate exists after selected 2024 calibration window; selected 2024 window is usable but future-candidate watch is retained.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean; 2026_candidate_outside_window"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"326030","trigger_type":"Stage2-Actionable-CNSDrugCommercializationRevenueBridge-Positive","entry_date":"2024-07-05","duplicate_status":"new C23 symbol/trigger/date combination outside top-covered and previous R7 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"067630","trigger_type":"Stage2-FalsePositive-ApprovalExpectationNoCRLProtectionCommercializationBridge","entry_date":"2024-04-22","duplicate_status":"new C23 symbol/trigger/date combination outside top-covered and previous R7 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"229000","trigger_type":"Stage2-FalsePositive-DiagnosticCommercializationVocabularyNoReimbursementAdoptionCashBridge","entry_date":"2024-01-02","duplicate_status":"new C23 symbol/trigger/date combination outside top-covered and previous R7 loop symbols; future-corporate-action-candidate outside selected window"}
```

## 4. Research question

C23 is not “허가나 상업화 단어가 있다.”  
The useful regulatory/commercialization signal must prove the bridge from regulatory event to monetizable business:

```text
approval or de-risked regulatory path
label / indication quality
launch readiness
payer or reimbursement path
physician / hospital adoption
partner or commercial infrastructure
manufacturing and supply readiness
revenue run-rate
cash runway and dilution risk
```

A regulatory headline without this bridge is a stamped document still sitting in the mailroom. It matters only after the product reaches the channel, gets reimbursed, and turns into repeat revenue.

Residual question:

```text
Can C23 distinguish:
1. CNS drug commercialization / revenue bridge with high MFE and low entry MAE,
2. approval-expectation cases where CRL or review failure risk was not protected,
3. diagnostic commercialization vocabulary where no reimbursement, adoption, or cash bridge exists?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C23_R7L91_326030_SKBP_CNS_COMMERCIALIZATION","symbol":"326030","company_name":"SK바이오팜","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CNS_DRUG_COMMERCIALIZATION_REVENUE_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-CNSDrugCommercializationRevenueBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE90_low_MAE_commercialization_revenue_bridge","current_profile_verdict":"current_profile_correct_if_launch_revenue_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"CNS drug commercialization / revenue bridge proxy produced high MFE with shallow MAE. Green still requires exact revenue run-rate, launch adoption, margin and cash evidence."}
{"row_type":"case","case_id":"C23_R7L91_067630_HLB_LS_APPROVAL_EXPECTATION_CRL","symbol":"067630","company_name":"HLB생명과학","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"APPROVAL_EXPECTATION_WITHOUT_CRL_PROTECTION_COMMERCIALIZATION_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ApprovalExpectationNoCRLProtectionCommercializationBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_extreme_MAE_4C_watch","current_profile_verdict":"current_profile_false_positive_if_approval_expectation_overcredited_without_CRL_protection","price_source":"Songdaiki/stock-web","notes":"Approval-expectation row had near-zero MFE and extreme MAE after regulatory failure risk materialized. This is 4C-watch, not simply weak 4B."}
{"row_type":"case","case_id":"C23_R7L91_229000_GENECURIX_DIAGNOSTIC_COMMERCIALIZATION","symbol":"229000","company_name":"젠큐릭스","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"DIAGNOSTIC_COMMERCIALIZATION_VOCABULARY_WITHOUT_REIMBURSEMENT_ADOPTION_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DiagnosticCommercializationVocabularyNoReimbursementAdoptionCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_near_zero_MFE_extreme_MAE_diagnostic_vocabulary_decay","current_profile_verdict":"current_profile_false_positive_if_diagnostic_commercialization_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Diagnostic commercialization vocabulary had near-zero MFE and extreme MAE without reimbursement, hospital adoption, sales run-rate or cash bridge. Future corporate-action candidate outside selected window remains data-quality watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 326030 SK바이오팜 — CNS drug commercialization / revenue bridge positive-control

Entry row: `2024-07-05 c=79000`.  
Observed path: entry low `2024-07-05 l=76700`, peak `2024-10-16 h=130000`, and no below-entry follow-through after the early entry-area low.

```jsonl
{"row_type":"trigger","trigger_id":"R7L91_C23_326030_20240705_STAGE2_CNS_COMMERCIALIZATION_REVENUE","case_id":"C23_R7L91_326030_SKBP_CNS_COMMERCIALIZATION","symbol":"326030","company_name":"SK바이오팜","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CNS_DRUG_COMMERCIALIZATION_REVENUE_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-CNSDrugCommercializationRevenueBridge-Positive","trigger_date":"2024-07-05","entry_date":"2024-07-05","entry_price":79000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_CNS_drug_commercialization_revenue_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; CNS drug launch, prescription/adoption, revenue run-rate and commercialization margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["commercial_revenue_runrate_proxy","launch_adoption_proxy","global_partner_channel_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_revenue_runrate_source_pending","payer_or_prescription_source_pending","margin_cash_bridge_pending","cash_runway_pending"],"stage4b_evidence_fields":["price_extension_watch","commercialization_execution_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/326/326030/2024.csv","profile_path":"atlas/symbol_profiles/326/326030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.76,"MFE_90D_pct":64.56,"MFE_180D_pct":64.56,"MAE_30D_pct":-2.91,"MAE_90D_pct":-2.91,"MAE_180D_pct":-2.91,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-16","peak_price":130000.0,"max_drawdown_low_date":"2024-07-05","max_drawdown_low":76700.0,"drawdown_after_peak_pct":-25.46,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.17,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_revenue_adoption_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","commercialization_execution_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_low_MAE_commercialization_revenue_bridge","current_profile_verdict":"current_profile_correct_if_launch_revenue_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"326030_2024-07-05_79000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C23 can allow Stage2/Yellow when regulatory/commercialization strength is tied to launch adoption, revenue run-rate, payer/channel visibility, margin and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 067630 HLB생명과학 — approval-expectation without CRL protection / commercialization bridge

Entry row: `2024-04-22 c=17310`.  
Observed path: local high `2024-04-25 h=18000`, then CRL-like regulatory failure drawdown to `2024-05-20 l=7700`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L91_C23_067630_20240422_STAGE2_FALSE_POSITIVE_APPROVAL_EXPECTATION_CRL","case_id":"C23_R7L91_067630_HLB_LS_APPROVAL_EXPECTATION_CRL","symbol":"067630","company_name":"HLB생명과학","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"APPROVAL_EXPECTATION_WITHOUT_CRL_PROTECTION_COMMERCIALIZATION_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4C_regulatory_failure_watch","trigger_type":"Stage2-FalsePositive-ApprovalExpectationNoCRLProtectionCommercializationBridge","trigger_date":"2024-04-22","entry_date":"2024-04-22","entry_price":17310.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_approval_expectation_commercialization_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; approval expectation treated as insufficient without CRL/deficiency protection, label quality, launch readiness and commercialization bridge","evidence_source_type":"historical_public_regulatory_event_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["approval_expectation_keyword","commercialization_expectation_vocabulary","relative_strength_event"],"stage3_evidence_fields":["CRL_protection_missing","label_quality_unverified","launch_readiness_missing","commercial_cash_bridge_missing"],"stage4b_evidence_fields":["near_zero_MFE","regulatory_failure_watch","extreme_MAE"],"stage4c_evidence_fields":["CRL_or_review_failure_risk_materialized_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067630/2024.csv","profile_path":"atlas/symbol_profiles/067/067630.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.99,"MFE_90D_pct":3.99,"MFE_180D_pct":3.99,"MAE_30D_pct":-55.52,"MAE_90D_pct":-55.52,"MAE_180D_pct":-55.52,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-25","peak_price":18000.0,"max_drawdown_low_date":"2024-05-20","max_drawdown_low":7700.0,"drawdown_after_peak_pct":-57.22,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"approval_expectation_without_CRL_protection_and_commercialization_bridge_should_be_4C_watch_not_positive","four_b_evidence_type":["near_zero_MFE","regulatory_failure_watch","extreme_MAE"],"four_c_protection_label":"CRL_or_review_failure_risk_materialized_watch","trigger_outcome_label":"counterexample_near_zero_MFE_extreme_MAE_4C_watch","current_profile_verdict":"current_profile_false_positive_if_approval_expectation_overcredited_without_CRL_protection","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["4C_regulatory_failure_watch"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"067630_2024-04-22_17310","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C23 should not promote approval expectation unless CRL/deficiency risk, label quality, launch readiness, payer/channel and cash bridge are repaired. Regulatory failure risk routes to hard 4C-watch."}
```

### 6.3 229000 젠큐릭스 — diagnostic commercialization vocabulary without reimbursement/adoption/cash bridge

Entry row: `2024-01-02 c=6270`.  
Observed path: same-week high `2024-01-02 h=6290`, then persistent decay to `2024-12-09 l=1131`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L91_C23_229000_20240102_STAGE2_FALSE_POSITIVE_DIAGNOSTIC_COMMERCIALIZATION","case_id":"C23_R7L91_229000_GENECURIX_DIAGNOSTIC_COMMERCIALIZATION","symbol":"229000","company_name":"젠큐릭스","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"DIAGNOSTIC_COMMERCIALIZATION_VOCABULARY_WITHOUT_REIMBURSEMENT_ADOPTION_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;diagnostic_commercialization_4B_stress_test","trigger_type":"Stage2-FalsePositive-DiagnosticCommercializationVocabularyNoReimbursementAdoptionCashBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":6270.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_diagnostic_commercialization_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; diagnostic commercialization vocabulary treated as insufficient without reimbursement, hospital adoption, order/revenue run-rate and cash bridge","evidence_source_type":"historical_public_regulatory_commercialization_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["diagnostic_commercialization_keyword","regulatory_or_sales_vocabulary","relative_strength_rebound"],"stage3_evidence_fields":["reimbursement_path_missing","hospital_adoption_missing","order_revenue_runrate_missing","cash_runway_missing"],"stage4b_evidence_fields":["near_zero_MFE","diagnostic_adoption_bridge_missing_watch","extreme_MAE"],"stage4c_evidence_fields":["dilution_or_cash_runway_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/229/229000/2024.csv","profile_path":"atlas/symbol_profiles/229/229000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.32,"MFE_90D_pct":0.32,"MFE_180D_pct":0.32,"MAE_30D_pct":-28.23,"MAE_90D_pct":-49.52,"MAE_180D_pct":-81.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":6290.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1131.0,"drawdown_after_peak_pct":-82.02,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"diagnostic_commercialization_vocabulary_without_reimbursement_adoption_revenue_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","diagnostic_adoption_bridge_missing_watch","extreme_MAE"],"four_c_protection_label":"cash_runway_or_dilution_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_extreme_MAE_diagnostic_vocabulary_decay","current_profile_verdict":"current_profile_false_positive_if_diagnostic_commercialization_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["future_2026_corporate_action_candidate_outside_window_watch"],"corporate_action_window_status":"2024_window_clean; 2026_candidate_outside_selected_window","same_entry_group_id":"229000_2024-01-02_6270","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C23 should not count diagnostic commercialization vocabulary as approval-to-revenue evidence unless reimbursement, hospital adoption, order run-rate and cash runway are exact-repaired. Near-zero MFE and extreme MAE force Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_R7L91_326030_SKBP_CNS_COMMERCIALIZATION","trigger_id":"R7L91_C23_326030_20240705_STAGE2_CNS_COMMERCIALIZATION_REVENUE","symbol":"326030","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C23 requires de-risked regulatory status, launch adoption, payer/channel path, revenue run-rate, margin and cash bridge rather than approval vocabulary alone","raw_component_scores_before":{"regulatory_derisking_score":12,"label_quality_score":10,"launch_readiness_score":12,"payer_reimbursement_score":9,"commercial_infrastructure_score":12,"revenue_runrate_score":13,"margin_cash_score":9,"relative_strength_score":14,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"regulatory_derisking_score":15,"label_quality_score":12,"launch_readiness_score":15,"payer_reimbursement_score":11,"commercial_infrastructure_score":15,"revenue_runrate_score":16,"margin_cash_score":11,"relative_strength_score":15,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":87,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Commercial revenue bridge plus high MFE90 supports Yellow/Green-candidate watch; exact revenue/adoption/margin evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_R7L91_067630_HLB_LS_APPROVAL_EXPECTATION_CRL","trigger_id":"R7L91_C23_067630_20240422_STAGE2_FALSE_POSITIVE_APPROVAL_EXPECTATION_CRL","symbol":"067630","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"approval expectation without CRL protection and commercialization bridge should be hard-blocked","raw_component_scores_before":{"regulatory_derisking_score":2,"label_quality_score":0,"launch_readiness_score":1,"payer_reimbursement_score":0,"commercial_infrastructure_score":1,"revenue_runrate_score":0,"margin_cash_score":0,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-22,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/4C-Watch","raw_component_scores_after":{"regulatory_derisking_score":0,"label_quality_score":0,"launch_readiness_score":0,"payer_reimbursement_score":0,"commercial_infrastructure_score":0,"revenue_runrate_score":0,"margin_cash_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-34,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4C-Watch","component_delta_explanation":"Near-zero MFE and extreme MAE after review-failure risk materialized require hard 4C-watch and evidence repair."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_R7L91_229000_GENECURIX_DIAGNOSTIC_COMMERCIALIZATION","trigger_id":"R7L91_C23_229000_20240102_STAGE2_FALSE_POSITIVE_DIAGNOSTIC_COMMERCIALIZATION","symbol":"229000","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"diagnostic commercialization vocabulary without reimbursement and adoption bridge should remain Watch/4B","raw_component_scores_before":{"regulatory_derisking_score":1,"label_quality_score":1,"launch_readiness_score":1,"payer_reimbursement_score":0,"commercial_infrastructure_score":0,"revenue_runrate_score":0,"margin_cash_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"regulatory_derisking_score":0,"label_quality_score":0,"launch_readiness_score":0,"payer_reimbursement_score":0,"commercial_infrastructure_score":0,"revenue_runrate_score":0,"margin_cash_score":0,"relative_strength_score":0,"valuation_repricing_score":0,"execution_risk_score":-30,"theme_spike_risk":-22,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and extreme MAE require reimbursement, hospital adoption, revenue run-rate and cash evidence before Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R7L91_C23_P0_CURRENT","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C23 needs explicit de-risked regulatory status, label quality, launch readiness, reimbursement/adoption, revenue, margin/cash and CRL-protection taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":22.96,"avg_MAE90_pct":-35.98,"avg_MFE180_pct":22.96,"avg_MAE180_pct":-46.80,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C23_regulatory_derisking_commercial_revenue_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R7L91_C23_P1_SECTOR_SPECIFIC","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P1_L7_regulatory_commercial_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L7 approval/commercialization signals need regulatory de-risking, label/reimbursement, launch readiness, adoption, revenue run-rate or cash bridge before Stage2-Actionable","changed_axes":["regulatory_derisking_required","commercial_revenue_required","CRL_failure_risk_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_derisked_regulatory_path_label_reimbursement_launch_adoption_revenue_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":22.96,"avg_MAE90_pct":-35.98,"avg_MFE180_pct":22.96,"avg_MAE180_pct":-46.80,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R7L91_C23_P2_CANONICAL","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P2_C23_approval_to_revenue_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C23 should reward approval-to-launch-to-revenue mechanics, not approval expectation or diagnostic commercialization vocabulary","changed_axes":["C23_regulatory_derisking_launch_revenue_bridge_required","C23_CRL_expectation_hard_4C_guard","C23_diagnostic_commercialization_local_4B_guard"],"changed_thresholds":{"stage2_yellow_gate":"regulatory_derisking_or_existing_launch_plus_revenue_or_adoption_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":22.96,"avg_MAE90_pct":-35.98,"avg_MFE180_pct":22.96,"avg_MAE180_pct":-46.80,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R7L91_C23_P3_COUNTEREXAMPLE_GUARD","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P3_C23_low_MFE_extreme_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If commercialization bridge is missing, MFE90<5 or MAE90<=-30 should block Yellow/Green; CRL/review failure routes to 4C-watch","changed_axes":["C23_low_MFE_guardrail","C23_extreme_MAE_4B_guardrail","C23_CRL_review_failure_4C_guard"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_5_or_MAE90_le_minus_30); hard_4C_if_CRL_or_review_failure_risk_materialized"},"eligible_trigger_count":3,"avg_MFE90_pct":22.96,"avg_MAE90_pct":-35.98,"avg_MFE180_pct":22.96,"avg_MAE180_pct":-46.80,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_CNS_COMMERCIALIZATION_POSITIVE_VS_APPROVAL_DIAGNOSTIC_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":1,"4C_case_count":1,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":22.96,"avg_MAE90_pct":-35.98,"avg_MFE180_pct":22.96,"avg_MAE180_pct":-46.80,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE90_le_minus30":0.67,"interpretation":"C23 needs bridge discipline. SK바이오팜 shows regulatory/commercialization revenue bridge can support Yellow/Green-candidate-watch, while HLB생명과학 and 젠큐릭스 show approval expectation or diagnostic commercialization vocabulary should not be promoted without CRL protection, launch readiness, reimbursement/adoption, revenue run-rate and cash evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"326030","trigger_type":"Stage2-Actionable-CNSDrugCommercializationRevenueBridge-Positive","entry_date":"2024-07-05","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_commercialization_revenue_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when commercialization strength is tied to launch adoption, revenue run-rate, payer/channel, margin and cash bridge; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"067630","trigger_type":"Stage2-FalsePositive-ApprovalExpectationNoCRLProtectionCommercializationBridge","entry_date":"2024-04-22","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_extreme_MAE","stage2_to_180D_outcome":"failed_approval_expectation_CRL_review_failure_4C_watch","MFE90_ge20":false,"MAE90_le_minus30":true,"transition_note":"Approval expectation without CRL protection and launch/commercialization bridge should be hard 4C-watch, not Stage2/Yellow."}
{"row_type":"stage_transition_summary","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"229000","trigger_type":"Stage2-FalsePositive-DiagnosticCommercializationVocabularyNoReimbursementAdoptionCashBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE","stage2_to_180D_outcome":"failed_diagnostic_commercialization_vocabulary_extreme_MAE","MFE90_ge20":false,"MAE180_le_minus50":true,"transition_note":"Diagnostic commercialization vocabulary without reimbursement, hospital adoption, revenue and cash bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","residual_type":"approval_expectation_diagnostic_commercialization_vocabulary_overcredit_without_regulatory_derisking_revenue_cash_bridge","contribution":"Adds one 4B diagnostic commercialization counterexample and one 4C approval-expectation/CRL counterexample against one CNS commercialization positive, avoiding C23 top-covered and recent R7 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CNS_DRUG_COMMERCIALIZATION_REVENUE_BRIDGE_VS_CRL_APPROVAL_EXPECTATION_DIAGNOSTIC_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":1,"4C_case_count":1,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C23 now has non-top-symbol CNS commercialization positive, one approval-expectation 4C-watch counterexample, and one diagnostic commercialization weak-bridge 4B counterexample; next R7 C23 loops should exact-URL repair regulatory de-risking, label quality, launch readiness, reimbursement/adoption, revenue run-rate, margin and cash evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","axis":"C23_regulatory_derisking_launch_revenue_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"326030 worked when commercialization/revenue proxy existed; 067630 and 229000 failed when approval or diagnostic vocabulary lacked de-risked regulatory and revenue/cash bridge."}
{"row_type":"shadow_weight","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","axis":"C23_CRL_expectation_hard_4C_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"hard_guard","apply_now":false,"shadow_only":true,"evidence_basis":"067630 shows approval expectation without CRL protection can produce near-zero MFE and extreme MAE, so it should route to 4C-watch."}
{"row_type":"shadow_weight","round":"R7","loop":"91","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","axis":"C23_diagnostic_commercialization_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"229000 shows diagnostic commercialization vocabulary should remain 4B-watch unless reimbursement, adoption, revenue run-rate and cash bridge are exact-repaired."}
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
  - approval_expectation_overcredit
  - CRL_or_review_failure_protection_missing
  - diagnostic_commercialization_vocabulary_overcredit
  - reimbursement_adoption_bridge_missing
  - revenue_cash_bridge_missing
new_axis_proposed:
  - C23_regulatory_derisking_launch_revenue_bridge_required_shadow_only
  - C23_CRL_expectation_hard_4C_guard_shadow_only
  - C23_diagnostic_commercialization_local_4B_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C23
  - full_4b_requires_non_price_evidence within C23
  - hard_4c_thesis_break_routes_to_4c within C23
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
`067630` has older corporate-action/name-transition candidates before 2024.  
`229000` has a 2026 corporate-action candidate outside the selected 2024 window, so it remains future-candidate data-quality watch before production patching.  
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
future_candidate_outside_window_watch = true for 229000
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
3. Confirm R7 / L7 / C23 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C23 top-covered symbols
   - previous R7 loop85 C23 symbols
   - previous R7 loop86 C25 symbols
   - previous R7 loop87 C24 symbols
   - previous R7 loop88 C23 symbols
   - previous R7 loop89 C25 symbols
   - previous R7 loop90 C24 symbols
6. Confirm accidentally touched R6/C21 and earlier R5/R4/R3/R2 candidate rows are not ingested from this MD.
7. Keep 067630 as 4C-watch regulatory-failure stress and 229000 as diagnostic 4B-watch data-quality repair case.
8. If aggregate support remains stable after exact evidence URL repair, consider C23-scoped safe patch candidates:
   - C23_regulatory_derisking_launch_revenue_bridge_required
   - C23_CRL_expectation_hard_4C_guard
   - C23_diagnostic_commercialization_local_4B_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R7
completed_loop = 91
next_round = R8
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, 1 local 4B-watch row and 1 4C-watch row for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.
```

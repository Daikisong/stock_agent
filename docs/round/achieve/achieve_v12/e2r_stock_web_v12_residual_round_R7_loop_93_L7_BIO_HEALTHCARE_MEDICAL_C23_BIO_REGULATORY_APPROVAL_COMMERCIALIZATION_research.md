# E2R Stock-Web v12 Residual Research — R7 Loop 93 / L7 / C23

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R7
loop: 93
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: COMMERCIAL_DRUG_EXPORT_ROYALTY_BRIDGE_VS_PIPELINE_APPROVAL_AND_CELL_THERAPY_COMMERCIALIZATION_DECAY
sector: bio / healthcare / pharma / regulatory approval / commercialization / export royalty / drug launch / pipeline / reimbursement / cash conversion
output_file: e2r_stock_web_v12_residual_round_R7_loop_93_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after recent loop93 expansions in C09, C01, C07, C06, C10, C11, C19, C27, C24, C12, C13 and C17.

```text
selected_round = R7
selected_loop = 93
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

Reason for selecting C23:

```text
v12 scheduler = coverage_index_first
sequential_round_cycle_required = false
coverage_gap_can_override_previous_round = true
selected_archetype_drives_round = true
```

No-Repeat Index under-30 snapshot used as duplicate-avoidance ledger:

```text
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION = 29 rows / need_to_30 = 1
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION = 27 rows / need_to_30 = 3 by raw index, but local loop92 already expanded C28 once
```

C23 can cross the 30-row minimum-stability threshold with one additional representative row, but this run keeps the normal 3-row positive/counterexample balance.

This loop avoids C23 top-covered and recent R7 symbols:

```text
C23 top-covered = 000250, 086900, 145020, 068270, 326030, 003850

R7 loop85 C23: 145020, 302440, 086900
R7 loop86 C25: 335890, 228670, 065510
R7 loop87 C24: 196170, 206650, 950220
R7 loop88 C23: 000250, 019170, 095700
R7 loop89 C25: 200670, 119610, 290650
R7 loop90 C24: 237690, 365270, 256840
R7 loop91 C23: 326030, 067630, 229000
R7 loop92 C25: 214150, 145720, 099190
R7 loop93 C24: 298380, 028300, 141080
```

Candidate hygiene note:

```text
During this execution path, C17 and C13/C12 candidate rows were touched while checking alternatives.
They are not used in this C23 output because the valid output must be R7/L7/C23.
```

Selected symbols:

```text
195940, 009420, 085660
```

The selected pocket is:

```text
approved/commercial drug export and royalty bridge positive-watch
vs
pipeline/regulatory vocabulary where commercialization bridge appears late and cannot validate the original entry
vs
cell-therapy/regenerative-medicine commercialization vocabulary without approval/reimbursement/cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"195940","company_name":"HK이노엔","profile_path":"atlas/symbol_profiles/195/195940.json","first_date":"2021-08-09","last_date":"2026-02-20","trading_day_count":1108,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"009420","company_name":"한올바이오파마","profile_path":"atlas/symbol_profiles/009/009420.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7757,"corporate_action_candidate_count":"profile_tail_not_fetched_in_this_run","corporate_action_candidate_dates":"historical_name_transition_before_2024","has_major_raw_discontinuity":true,"calibration_caveat":"Name changed from 한올제약 to 한올바이오파마 long before selected 2024 window; selected 2024 window usable for residual analysis.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; late_rebound_not_original_entry_validation_watch"}
{"row_type":"price_source_validation","symbol":"085660","company_name":"차바이오텍","profile_path":"atlas/symbol_profiles/085/085660.json","first_date":"2005-12-27","last_date":"2026-02-20","trading_day_count":4946,"corporate_action_candidate_count":8,"corporate_action_candidate_dates":["2006-01-06","2007-11-09","2008-03-17","2008-06-23","2008-12-24","2009-02-24","2014-06-02","2025-06-25"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 window; future 2025 candidate is outside selected forward window but retained as watch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; future_candidate_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"195940","trigger_type":"Stage2-Actionable-ApprovedDrugExportRoyaltyCommercializationBridge-PositiveWatch","entry_date":"2024-06-17","duplicate_status":"new C23 symbol/trigger/date combination outside C23 top-covered and recent R7 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"009420","trigger_type":"Stage2-FalsePositive-PipelineRegulatoryVocabularyLateReboundNoOriginalCommercialBridge","entry_date":"2024-05-16","duplicate_status":"new C23 symbol/trigger/date combination outside C23 top-covered and recent R7 loop symbols; late rebound requires fresh evidence"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"085660","trigger_type":"Stage2-FalsePositive-CellTherapyCommercializationVocabularyNoApprovalReimbursementCashBridge","entry_date":"2024-03-07","duplicate_status":"new C23 symbol/trigger/date combination outside C23 top-covered and recent R7 loop symbols; future-candidate watch"}
```

## 4. Research question

C23 is not “승인/상업화 단어가 있다.”
The useful C23 signal must prove the approval-to-cash chain:

```text
regulatory approval or clear approval path
label / indication / market scope
launch timing
partner or distributor economics
reimbursement / pricing / formulary path
manufacturing and supply readiness
sales conversion or royalty visibility
gross-margin / operating-margin bridge
cash conversion
post-approval execution risk
```

A regulatory approval headline without this bridge is a stamped passport with no ticket bought. E2R needs the route: launch, reimbursement, distributor economics, shipment, royalty, margin and cash.

Residual question:

```text
Can C23 distinguish:
1. approved/commercial drug export and royalty bridge that can support positive-watch,
2. pipeline/regulatory vocabulary where a later rebound needs a fresh trigger and cannot validate the original weak commercialization entry,
3. cell-therapy commercialization vocabulary where approval/reimbursement/cash bridge is missing and price path decays?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C23_R7L93_195940_HKINNO_KCAB_COMMERCIAL_BRIDGE","symbol":"195940","company_name":"HK이노엔","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"APPROVED_DRUG_EXPORT_ROYALTY_COMMERCIALIZATION_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-ApprovedDrugExportRoyaltyCommercializationBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_watch_MFE90_ge30_low_MAE_approved_drug_commercialization_bridge","current_profile_verdict":"current_profile_correct_if_approval_launch_reimbursement_royalty_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"Approved/commercial drug export and royalty proxy after June reset produced MFE90 above 30 with controlled MAE. Green still requires exact approval, launch, reimbursement, shipment, royalty and cash evidence."}
{"row_type":"case","case_id":"C23_R7L93_009420_HANALL_LATE_REBOUND_NONVALIDATION","symbol":"009420","company_name":"한올바이오파마","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"PIPELINE_REGULATORY_VOCABULARY_LATE_REBOUND_WITHOUT_ORIGINAL_COMMERCIAL_BRIDGE","case_type":"failed_entry_late_rebound_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PipelineRegulatoryVocabularyLateReboundNoOriginalCommercialBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_original_low_MFE_deep_MAE_late_rebound_needs_fresh_trigger","current_profile_verdict":"current_profile_false_positive_if_late_rebound_validates_original_pipeline_commercialization_entry","price_source":"Songdaiki/stock-web","notes":"Pipeline/regulatory vocabulary around May had weak original commercialization bridge and deep early MAE. The October rebound is a separate trigger candidate, not validation of the original entry."}
{"row_type":"case","case_id":"C23_R7L93_085660_CHABIO_CELL_THERAPY_DECAY","symbol":"085660","company_name":"차바이오텍","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CELL_THERAPY_REGENERATIVE_COMMERCIALIZATION_VOCABULARY_WITHOUT_APPROVAL_REIMBURSEMENT_CASH_BRIDGE","case_type":"failed_entry_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CellTherapyCommercializationVocabularyNoApprovalReimbursementCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_sub20_MFE_deep_MAE_no_approval_reimbursement_cash_bridge_future_candidate_watch","current_profile_verdict":"current_profile_false_positive_if_cell_therapy_commercialization_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Cell-therapy/regenerative commercialization vocabulary had only sub-20 MFE and later deep MAE without approval, reimbursement, manufacturing scale or cash bridge. Future corporate-action candidate remains watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 195940 HK이노엔 — approved/commercial drug export and royalty bridge positive-watch

Entry row: `2024-06-17 c=38000`, after a first-half reset and renewed commercial-drug export / royalty path.
Observed path: peak `2024-10-07 h=52000`, low `2024-06-21 l=34800`, and later low `2024-12-09 l=34300`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L93_C23_195940_20240617_STAGE2_DRUG_COMMERCIAL_BRIDGE","case_id":"C23_R7L93_195940_HKINNO_KCAB_COMMERCIAL_BRIDGE","symbol":"195940","company_name":"HK이노엔","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"APPROVED_DRUG_EXPORT_ROYALTY_COMMERCIALIZATION_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-ApprovedDrugExportRoyaltyCommercializationBridge-PositiveWatch","trigger_date":"2024-06-17","entry_date":"2024-06-17","entry_price":38000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_approved_drug_export_royalty_commercialization_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; approved/commercial drug export, launch, royalty, distributor economics and cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["approved_drug_commercialization_proxy","export_royalty_proxy","launch_reimbursement_proxy","relative_strength_after_reset"],"stage3_evidence_fields":["exact_approval_source_pending","launch_or_export_source_pending","royalty_reimbursement_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["positive_watch","Green_exact_evidence_watch"],"stage4c_evidence_fields":["commercial_execution_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/195/195940/2024.csv","profile_path":"atlas/symbol_profiles/195/195940.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.18,"MFE_90D_pct":36.84,"MFE_180D_pct":36.84,"MAE_30D_pct":-8.42,"MAE_90D_pct":-8.42,"MAE_180D_pct":-9.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-07","peak_price":52000.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":34300.0,"drawdown_after_peak_pct":-34.04,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.30,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_approval_launch_reimbursement_royalty_margin_cash_evidence","four_b_evidence_type":["positive_watch","Green_exact_evidence_watch"],"four_c_protection_label":"commercial_execution_watch_only","trigger_outcome_label":"positive_watch_MFE90_ge30_low_MAE_approved_drug_commercialization_bridge","current_profile_verdict":"current_profile_correct_if_approval_launch_reimbursement_royalty_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"195940_2024-06-17_38000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C23 can allow Yellow/positive-watch when approval or commercial-drug strength is tied to launch, reimbursement/export, royalty, margin and cash conversion. Green still requires exact source-grade evidence."}
```

### 6.2 009420 한올바이오파마 — pipeline/regulatory vocabulary where late rebound does not validate original commercialization entry

Entry row: `2024-05-16 c=36550`, during pipeline/regulatory optimism.
Observed path: local high `2024-05-22 h=37900`, sharp low `2024-05-31 l=29900`, and later October high `2024-10-22 h=52000`. The late rebound is not original-entry validation without a fresh trigger and fresh commercialization bridge.

```jsonl
{"row_type":"trigger","trigger_id":"R7L93_C23_009420_20240516_STAGE2_FALSE_POSITIVE_PIPELINE_LATE_REBOUND","case_id":"C23_R7L93_009420_HANALL_LATE_REBOUND_NONVALIDATION","symbol":"009420","company_name":"한올바이오파마","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"PIPELINE_REGULATORY_VOCABULARY_LATE_REBOUND_WITHOUT_ORIGINAL_COMMERCIAL_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;late_rebound_not_entry_validation","trigger_type":"Stage2-FalsePositive-PipelineRegulatoryVocabularyLateReboundNoOriginalCommercialBridge","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":36550.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_pipeline_regulatory_commercialization_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; pipeline/regulatory vocabulary treated as insufficient for C23 without approval path, launch timing, partner economics, reimbursement and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["pipeline_regulatory_vocabulary","partner_pipeline_keyword","relative_strength_rebound"],"stage3_evidence_fields":["approval_or_label_missing","launch_timing_missing","reimbursement_bridge_missing","commercial_cash_bridge_missing"],"stage4b_evidence_fields":["low_original_MFE","early_deep_MAE","late_rebound_not_entry_validation"],"stage4c_evidence_fields":["regulatory_failure_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009420/2024.csv","profile_path":"atlas/symbol_profiles/009/009420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.69,"MFE_90D_pct":5.75,"MFE_180D_pct":42.27,"MAE_30D_pct":-18.19,"MAE_90D_pct":-18.19,"MAE_180D_pct":-18.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-22","peak_price":52000.0,"max_drawdown_low_date":"2024-05-31","max_drawdown_low":29900.0,"drawdown_after_peak_pct":-39.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.26,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_rebound_requires_fresh_trigger_and_fresh_commercialization_bridge; original_entry_remains_4B_watch","four_b_evidence_type":["low_original_MFE","early_deep_MAE","late_rebound_not_entry_validation"],"four_c_protection_label":"regulatory_failure_watch_only","trigger_outcome_label":"counterexample_original_low_MFE_deep_MAE_late_rebound_needs_fresh_trigger","current_profile_verdict":"current_profile_false_positive_if_late_rebound_validates_original_pipeline_commercialization_entry","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_name_transition_pre_2024; selected_window_clean","same_entry_group_id":"009420_2024-05-16_36550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C23 should not let a later pipeline rebound validate an original entry that lacked approval, launch, reimbursement, partner economics and cash evidence. A later move needs its own trigger-date evidence."}
```

### 6.3 085660 차바이오텍 — cell-therapy commercialization vocabulary without approval / reimbursement / cash bridge

Entry row: `2024-03-07 c=19060`, after regenerative/cell-therapy commercialization vocabulary and price spike.
Observed path: local high `2024-03-27 h=21000`, then deterioration to `2024-12-09 l=13350`; later future corporate-action candidate remains a data-quality watch.

```jsonl
{"row_type":"trigger","trigger_id":"R7L93_C23_085660_20240307_STAGE2_FALSE_POSITIVE_CELL_THERAPY_COMMERCIALIZATION","case_id":"C23_R7L93_085660_CHABIO_CELL_THERAPY_DECAY","symbol":"085660","company_name":"차바이오텍","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CELL_THERAPY_REGENERATIVE_COMMERCIALIZATION_VOCABULARY_WITHOUT_APPROVAL_REIMBURSEMENT_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;data_quality_watch;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-CellTherapyCommercializationVocabularyNoApprovalReimbursementCashBridge","trigger_date":"2024-03-07","entry_date":"2024-03-07","entry_price":19060.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_cell_therapy_regenerative_commercialization_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; cell therapy/regenerative commercialization vocabulary treated as insufficient without approval, reimbursement, manufacturing scale, launch and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["cell_therapy_commercialization_vocabulary","regenerative_medicine_keyword","relative_strength_spike"],"stage3_evidence_fields":["approval_missing","reimbursement_path_missing","manufacturing_scale_missing","commercial_cash_bridge_missing"],"stage4b_evidence_fields":["sub20_MFE","deep_MAE","future_candidate_watch","approval_cash_bridge_missing_watch"],"stage4c_evidence_fields":["approval_failure_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/085/085660/2024.csv","profile_path":"atlas/symbol_profiles/085/085660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.18,"MFE_90D_pct":10.18,"MFE_180D_pct":10.18,"MAE_30D_pct":-8.34,"MAE_90D_pct":-20.46,"MAE_180D_pct":-29.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-27","peak_price":21000.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":13350.0,"drawdown_after_peak_pct":-36.43,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"cell_therapy_commercialization_vocabulary_without_approval_reimbursement_manufacturing_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["sub20_MFE","deep_MAE","future_candidate_watch","approval_cash_bridge_missing_watch"],"four_c_protection_label":"approval_failure_watch_only","trigger_outcome_label":"counterexample_sub20_MFE_deep_MAE_no_approval_reimbursement_cash_bridge_future_candidate_watch","current_profile_verdict":"current_profile_false_positive_if_cell_therapy_commercialization_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["future_2025-06-25_corporate_action_candidate_watch"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_usable; future_candidate_watch","same_entry_group_id":"085660_2024-03-07_19060","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C23 should not promote cell-therapy commercialization vocabulary unless approval, reimbursement, manufacturing scale, launch and cash evidence are exact-repaired. Sub-20 MFE and deep MAE force Watch/4B routing."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_R7L93_195940_HKINNO_KCAB_COMMERCIAL_BRIDGE","trigger_id":"R7L93_C23_195940_20240617_STAGE2_DRUG_COMMERCIAL_BRIDGE","symbol":"195940","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C23 requires approval path, launch timing, reimbursement/export, partner economics, royalty and cash bridge rather than approval vocabulary alone","raw_component_scores_before":{"approval_path_score":12,"label_market_scope_score":10,"launch_timing_score":10,"partner_distributor_score":11,"reimbursement_pricing_score":9,"royalty_visibility_score":10,"margin_bridge_score":9,"cash_conversion_score":8,"relative_strength_score":12,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":70,"stage_label_before":"Stage2-Watch/PositiveControl","raw_component_scores_after":{"approval_path_score":15,"label_market_scope_score":13,"launch_timing_score":12,"partner_distributor_score":14,"reimbursement_pricing_score":11,"royalty_visibility_score":12,"margin_bridge_score":11,"cash_conversion_score":10,"relative_strength_score":14,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Commercial drug launch/export/royalty bridge plus MFE90 supports Green-candidate watch; exact evidence required before Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_R7L93_009420_HANALL_LATE_REBOUND_NONVALIDATION","trigger_id":"R7L93_C23_009420_20240516_STAGE2_FALSE_POSITIVE_PIPELINE_LATE_REBOUND","symbol":"009420","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"pipeline/regulatory vocabulary without launch/reimbursement/cash bridge should be blocked; late rebound needs fresh trigger","raw_component_scores_before":{"approval_path_score":1,"label_market_scope_score":0,"launch_timing_score":0,"partner_distributor_score":2,"reimbursement_pricing_score":0,"royalty_visibility_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":2,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/LateReboundWatch","raw_component_scores_after":{"approval_path_score":0,"label_market_scope_score":0,"launch_timing_score":0,"partner_distributor_score":0,"reimbursement_pricing_score":0,"royalty_visibility_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"execution_risk_score":-22,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/LateReboundNotValidation","component_delta_explanation":"Original entry lacked commercialization bridge; October rebound cannot retroactively repair launch/reimbursement evidence."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_R7L93_085660_CHABIO_CELL_THERAPY_DECAY","trigger_id":"R7L93_C23_085660_20240307_STAGE2_FALSE_POSITIVE_CELL_THERAPY_COMMERCIALIZATION","symbol":"085660","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"cell-therapy commercialization vocabulary without approval and reimbursement bridge should remain Watch/4B","raw_component_scores_before":{"approval_path_score":1,"label_market_scope_score":0,"launch_timing_score":0,"partner_distributor_score":0,"reimbursement_pricing_score":0,"royalty_visibility_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":4,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"approval_path_score":0,"label_market_scope_score":0,"launch_timing_score":0,"partner_distributor_score":0,"reimbursement_pricing_score":0,"royalty_visibility_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":0,"execution_risk_score":-24,"theme_spike_risk":-20,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Sub-20 MFE, deep MAE, future candidate watch and missing approval/reimbursement/cash bridge block promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R7L93_C23_P0_CURRENT","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C23 needs explicit approval-to-launch-to-reimbursement/royalty/cash bridge, late-rebound nonvalidation and cell-therapy commercialization guard taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":17.59,"avg_MAE90_pct":-15.69,"avg_MFE180_pct":29.76,"avg_MAE180_pct":-19.30,"false_positive_rate":0.67,"late_rebound_not_validation_count":1,"data_quality_watch_count":1,"score_return_alignment_verdict":"mixed_without_C23_approval_launch_reimbursement_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R7L93_C23_P1_SECTOR_SPECIFIC","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P1_L7_bio_approval_commercialization_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L7 commercialization signals need approval/label, launch timing, reimbursement/pricing, partner economics, royalty visibility or cash conversion before Stage2-Actionable","changed_axes":["approval_launch_required","reimbursement_royalty_cash_required","late_rebound_nonvalidation","cell_therapy_vocabulary_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_approval_launch_reimbursement_partner_royalty_or_cash_proxy"},"eligible_trigger_count":3,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R7L93_C23_P2_CANONICAL","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P2_C23_approval_launch_reimbursement_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C23 should reward approval-to-cash mechanics, not pipeline or commercialization vocabulary","changed_axes":["C23_approval_launch_reimbursement_royalty_cash_bridge_required","C23_pipeline_cell_therapy_vocabulary_local_4B_guard","C23_late_rebound_not_entry_validation_guard","C23_future_candidate_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"approval_or_launch_plus_reimbursement_or_royalty_cash_bridge_required"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R7L93_C23_P3_COUNTEREXAMPLE_GUARD","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P3_C23_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If approval/commercial cash bridge is missing, MFE90<15 or MAE90<=-20 blocks Yellow/Green and routes to Watch/4B","changed_axes":["C23_low_MFE_guardrail","C23_deep_MAE_guardrail","C23_cash_bridge_missing_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_15_or_MAE90_le_minus20)"},"eligible_trigger_count":3,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate and transition rows

```jsonl
{"row_type":"aggregate_metric","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_DRUG_COMMERCIAL_POSITIVE_VS_PIPELINE_CELL_THERAPY_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":17.59,"avg_MAE90_pct":-15.69,"avg_MFE180_pct":29.76,"avg_MAE180_pct":-19.30,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"late_rebound_not_validation_count":1,"interpretation":"C23 needs approval-to-cash discipline. HK이노엔 shows commercial drug export/royalty bridge can support Yellow/Green-candidate-watch, while 한올바이오파마 and 차바이오텍 show pipeline/cell-therapy commercialization vocabulary should not be promoted without approval, launch, reimbursement, royalty, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"195940","trigger_type":"Stage2-Actionable-ApprovedDrugExportRoyaltyCommercializationBridge-PositiveWatch","entry_date":"2024-06-17","stage2_to_90D_outcome":"positive_watch_MFE90_ge30_low_MAE","stage2_to_180D_outcome":"commercial_drug_bridge_but_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/Green-candidate when approval or commercial strength is tied to launch, reimbursement/export, royalty and cash bridge; exact evidence required for Green."}
{"row_type":"stage_transition_summary","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"009420","trigger_type":"Stage2-FalsePositive-PipelineRegulatoryVocabularyLateReboundNoOriginalCommercialBridge","entry_date":"2024-05-16","stage2_to_90D_outcome":"bad_stage2_low_original_MFE_commercial_bridge_missing","stage2_to_180D_outcome":"late_rebound_needs_fresh_trigger_not_original_validation","MFE90_ge20":false,"late_rebound_not_validation":true,"transition_note":"Pipeline/regulatory vocabulary without launch/reimbursement/cash bridge should stay Watch/4B; late rebound needs fresh trigger evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"085660","trigger_type":"Stage2-FalsePositive-CellTherapyCommercializationVocabularyNoApprovalReimbursementCashBridge","entry_date":"2024-03-07","stage2_to_90D_outcome":"bad_stage2_sub20_MFE_bridge_missing","stage2_to_180D_outcome":"failed_cell_therapy_vocabulary_deep_MAE_future_candidate_watch","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Cell-therapy commercialization vocabulary without approval/reimbursement/cash bridge should remain Watch/4B; future candidate repair required."}
{"row_type":"residual_contribution","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","residual_type":"pipeline_cell_therapy_vocabulary_overcredit_without_approval_launch_reimbursement_cash_bridge","contribution":"Adds two C23 4B counterexamples against one commercial-drug positive-watch, bringing C23 from 29 beyond the 30-row minimum stability threshold.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"COMMERCIAL_DRUG_EXPORT_ROYALTY_BRIDGE_VS_PIPELINE_APPROVAL_AND_CELL_THERAPY_COMMERCIALIZATION_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C23 now has one approved/commercial drug bridge positive-watch and two pipeline/cell-therapy weak-bridge counterexamples; next C23 loops should exact-URL repair approval source, launch timing, reimbursement, partner economics, royalty visibility and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","axis":"C23_approval_launch_reimbursement_royalty_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"195940 worked as positive-watch only when approval/commercial-drug export/royalty proxy existed; 009420 and 085660 failed when launch/reimbursement/cash bridge was missing."}
{"row_type":"shadow_weight","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","axis":"C23_pipeline_cell_therapy_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"009420 and 085660 showed low original MFE or deep MAE when pipeline/cell-therapy vocabulary was not tied to approval-to-cash mechanics."}
{"row_type":"shadow_weight","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","axis":"C23_late_rebound_not_entry_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"009420 shows a later rebound cannot backfill original entry-date approval/launch/reimbursement evidence."}
{"row_type":"shadow_weight","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","axis":"C23_future_candidate_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"085660 has a future 2025 corporate-action candidate outside the selected window; production patching requires price-path/evidence repair."}
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
  - pipeline_regulatory_vocabulary_overcredit
  - cell_therapy_commercialization_vocabulary_overcredit
  - approval_launch_reimbursement_cash_bridge_missing
  - late_rebound_not_original_entry_validation
  - future_candidate_data_quality_watch
new_axis_proposed:
  - C23_approval_launch_reimbursement_royalty_cash_bridge_required_shadow_only
  - C23_pipeline_cell_therapy_vocabulary_local_4B_guard_shadow_only
  - C23_late_rebound_not_entry_validation_guard_shadow_only
  - C23_future_candidate_data_quality_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows.
`195940` has no corporate-action candidate and the selected 2024 window is clean.
`009420` has only historical name-transition before 2024; the selected 2024 window is usable.
`085660` has historical corporate-action/name-transition candidates before 2024 and a future 2025-06-25 candidate outside selected window; it remains future-candidate watch before production patching.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
future_candidate_watch = true for 085660
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
3. Confirm R7 / L7 / C23 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop was selected by coverage-index-first and brings C23 over the 30-row minimum stability threshold.
6. Confirm this loop avoided:
   - C23 top-covered symbols
   - previous R7 loop85 C23 symbols
   - previous R7 loop86 C25 symbols
   - previous R7 loop87 C24 symbols
   - previous R7 loop88 C23 symbols
   - previous R7 loop89 C25 symbols
   - previous R7 loop90 C24 symbols
   - previous R7 loop91 C23 symbols
   - previous R7 loop92 C25 symbols
   - previous R7 loop93 C24 symbols
7. Confirm recently touched C17/C13/C12/C27/C19 candidate rows are not ingested from this MD.
8. Treat 195940 as Yellow/Green-candidate-watch only, not Green, until exact approval/launch/reimbursement/royalty/cash evidence is repaired.
9. Treat 009420 as late-rebound non-validation failure mode unless fresh trigger evidence is added later.
10. Keep 085660 in future-candidate data-quality watch before patch consideration.
11. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C23-scoped safe patch candidates:
   - C23_approval_launch_reimbursement_royalty_cash_bridge_required
   - C23_pipeline_cell_therapy_vocabulary_local_4B_guard
   - C23_late_rebound_not_entry_validation_guard
   - C23_future_candidate_data_quality_guard
12. Do not loosen Stage3-Green.
13. Do not use future MFE/MAE in runtime scoring.
14. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R7
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION or any remaining under-30 archetype after reconciling local loop additions with GitHub No-Repeat Index
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 commercial-drug approval/royalty positive-watch, 2 weak-bridge counterexamples, and 2 local 4B-watch rows for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.
```

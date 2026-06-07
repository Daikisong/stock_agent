# E2R Stock-Web v12 Residual Research — R7 Loop 93 / L7 / C24

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R7
loop: 93
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: ADC_BISPECIFIC_DATA_LICENSE_BRIDGE_VS_REGULATORY_CRL_HARD_4C_AND_FALSE_OVERBLOCK
sector: bio / healthcare / clinical data / trial event / regulatory event / ADC / bispecific antibody / platform license / CRL / evidence repair
output_file: e2r_stock_web_v12_residual_round_R7_loop_93_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after recent loop93 expansions in C09, C01, C07, C06, C10, C11, C19 and C27.

```text
selected_round = R7
selected_loop = 93
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
```

Reason for selecting C24:

```text
v12 scheduler = coverage_index_first
sequential_round_cycle_required = false
coverage_gap_can_override_previous_round = true
selected_archetype_drives_round = true
```

No-Repeat Index Priority 0 / under-30 snapshot used as duplicate ledger:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK = 27 rows / 17 symbols
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION = 27 rows / 15 symbols
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK = 27 rows / 21 symbols
C13_BATTERY_JV_UTILIZATION_AMPC_IRA = 27 rows / 17 symbols
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD = 29 rows / 15 symbols
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION = 29 rows / 20 symbols
```

This loop avoids recent R7 symbols and C24 top-covered symbols:

```text
C24 top-covered = 196170, 950220, 039200, 206650, 235980, 365270

R7 loop85 C23: 145020, 302440, 086900
R7 loop86 C25: 335890, 228670, 065510
R7 loop87 C24: 196170, 206650, 950220
R7 loop88 C23: 000250, 019170, 095700
R7 loop89 C25: 200670, 119610, 290650
R7 loop90 C24: 237690, 365270, 256840
R7 loop91 C23: 326030, 067630, 229000
R7 loop92 C25: 214150, 145720, 099190
```

Candidate hygiene note:

```text
During this execution path, C27/C19/C11 candidate rows were touched while checking alternatives.
They are not used in this C24 output.
```

Selected symbols:

```text
298380, 028300, 141080
```

The selected pocket is:

```text
bispecific / ADC clinical-data and partner-validation bridge positive-control
vs
regulatory CRL / approval shock hard 4C
vs
ADC platform-license / data bridge false-overblock case with name-transition and share-count repair watch
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"298380","company_name":"에이비엘바이오","profile_path":"atlas/symbol_profiles/298/298380.json","first_date":"2018-12-19","last_date":"2026-02-20","trading_day_count":1759,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"028300","company_name":"HLB","profile_path":"atlas/symbol_profiles/028/028300.json","first_date":"1996-09-02","last_date":"2026-02-20","trading_day_count":7065,"corporate_action_candidate_count":18,"corporate_action_candidate_dates":["1997-01-03","1998-11-28","2000-04-10","2000-04-25","2000-07-14","2002-04-02","2003-10-28","2003-12-17","2005-02-22","2005-06-01","2007-01-08","2007-11-29","2008-12-02","2009-01-07","2010-02-23","2011-01-05","2021-03-15","2021-04-01"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidates exist before selected 2024 window. Selected 2024 CRL shock window is usable only as hard 4C regulatory-event stress.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_CRl_event_window_usable_as_hard_4C_stress"}
{"row_type":"price_source_validation","symbol":"141080","company_name":"리가켐바이오","profile_path":"atlas/symbol_profiles/141/141080.json","first_date":"2013-05-10","last_date":"2026-02-20","trading_day_count":3136,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2020-07-07","2024-04-23"],"has_major_raw_discontinuity":true,"calibration_caveat":"Name changed from 레고켐바이오 to 리가켐바이오 on 2024-04-19 and 2024-04-23 corporate-action/share-count candidate follows; selected pre-event entry is usable for residual analysis but patching requires data-quality repair.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_name_transition_and_share_count_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"298380","trigger_type":"Stage2-Actionable-BispecificADCDataPartnerValidationBridge-Positive","entry_date":"2024-02-22","duplicate_status":"new C24 symbol/trigger/date combination outside C24 top-covered and recent R7 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"028300","trigger_type":"Stage2-4C-Validated-RegulatoryCRLApprovalShockHardBreak","entry_date":"2024-05-16","duplicate_status":"new C24 symbol/trigger/date combination outside C24 top-covered and recent R7 loop symbols; hard 4C regulatory-event stress"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"141080","trigger_type":"Stage2-FalsePositive-OverbroadTrialEventRiskWouldMissADCPlatformLicenseBridge","entry_date":"2024-02-22","duplicate_status":"new C24 symbol/trigger/date combination outside C24 top-covered and recent R7 loop symbols; false-overblock with 2024 name-transition/share-count repair watch"}
```

## 4. Research question

C24 is not “바이오 이벤트가 있다.”
The useful trial/data-event signal must separate source-graded biology from headline volatility:

```text
clinical data quality or platform validation
trial endpoint / response / safety profile
partner validation or license economics
regulatory decision path
data release timing and comparator risk
cash runway / dilution risk
commercial or milestone bridge
hard failure / CRL / refusal-to-file event handling
```

A biotech headline without this bridge is a lab door with a bright sign but no dataset on the bench. E2R needs the dataset, comparator, regulator path, partner economics, and cash runway.

Residual question:

```text
Can C24 distinguish:
1. bispecific/ADC data + partner-validation bridge that can support positive-watch,
2. regulatory CRL / approval shock that must route to hard 4C even if local rebound appears,
3. overbroad trial-event risk blocking that would miss a platform-license/data bridge after reset, while still requiring data-quality repair?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C24_R7L93_298380_ABL_BISPECIFIC_ADC_DATA","symbol":"298380","company_name":"에이비엘바이오","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BISPECIFIC_ADC_DATA_PARTNER_VALIDATION_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-BispecificADCDataPartnerValidationBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_high_low_MAE_bispecific_ADC_data_partner_bridge","current_profile_verdict":"current_profile_correct_if_data_quality_partner_validation_cash_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"Bispecific/ADC data + partner-validation proxy produced strong forward MFE with low entry MAE. Green still requires exact clinical-data, partner economics, milestone and cash-runway evidence."}
{"row_type":"case","case_id":"C24_R7L93_028300_HLB_REGULATORY_CRL_HARD4C","symbol":"028300","company_name":"HLB","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"REGULATORY_CRL_APPROVAL_SHOCK_HARD_BREAK","case_type":"validated_4C_hard_break","positive_or_counterexample":"counterexample","best_trigger":"Stage2-4C-Validated-RegulatoryCRLApprovalShockHardBreak","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"score_price_alignment":"hard_4C_regulatory_CRL_shock_deep_MAE_not_bargain_rebound","current_profile_verdict":"current_profile_correct_if_CRL_or_regulatory_refusal_routes_to_hard_4C_not_4B_rebound","price_source":"Songdaiki/stock-web","notes":"Regulatory CRL/approval shock caused hard price break and deep MAE. Any local rebound is not positive evidence unless new regulatory path and data repair are available."}
{"row_type":"case","case_id":"C24_R7L93_141080_LCG_ADC_PLATFORM_FALSE_OVERBLOCK","symbol":"141080","company_name":"리가켐바이오","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"ADC_PLATFORM_LICENSE_DATA_BRIDGE_FALSE_OVERBLOCK_AFTER_RESET","case_type":"false_overblock_data_quality_watch","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-OverbroadTrialEventRiskWouldMissADCPlatformLicenseBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"score_price_alignment":"false_overblock_high_MFE_after_ADC_platform_bridge_but_name_transition_CA_watch","current_profile_verdict":"current_profile_false_positive_if_C24_guard_blocks_platform_license_data_bridge_after_reset","price_source":"Songdaiki/stock-web","notes":"Overbroad trial-event risk blocking would miss ADC platform/license bridge after reset. However the 2024 name transition and share-count/corporate-action candidate require data-quality repair before any production patch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 298380 에이비엘바이오 — bispecific/ADC data + partner-validation bridge

Entry row: `2024-02-22 c=21250`.
Observed path: local high `2024-04-29 h=26850` and later high `2024-07-05 h=31000`, with shallow entry MAE.

```jsonl
{"row_type":"trigger","trigger_id":"R7L93_C24_298380_20240222_STAGE2_BISPECIFIC_ADC_DATA","case_id":"C24_R7L93_298380_ABL_BISPECIFIC_ADC_DATA","symbol":"298380","company_name":"에이비엘바이오","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BISPECIFIC_ADC_DATA_PARTNER_VALIDATION_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-BispecificADCDataPartnerValidationBridge-Positive","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":21250.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_bispecific_ADC_data_partner_validation_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; bispecific/ADC platform data, partner validation, milestone economics and cash runway treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_trial_partner_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["bispecific_ADC_platform_proxy","clinical_data_quality_proxy","partner_validation_proxy","cash_runway_proxy"],"stage3_evidence_fields":["exact_trial_data_source_pending","partner_economics_source_pending","milestone_bridge_pending","cash_runway_source_pending"],"stage4b_evidence_fields":["Green_exact_evidence_watch","clinical_data_quality_watch"],"stage4c_evidence_fields":["trial_failure_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298380/2024.csv","profile_path":"atlas/symbol_profiles/298/298380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.35,"MFE_90D_pct":45.88,"MFE_180D_pct":45.88,"MAE_30D_pct":-2.82,"MAE_90D_pct":-2.82,"MAE_180D_pct":-2.82,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-05","peak_price":31000.0,"max_drawdown_low_date":"2024-02-22","max_drawdown_low":20650.0,"drawdown_after_peak_pct":-15.00,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.57,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_trial_data_partner_milestone_cash_runway_evidence","four_b_evidence_type":["Green_exact_evidence_watch","clinical_data_quality_watch"],"four_c_protection_label":"trial_failure_watch_only","trigger_outcome_label":"positive_MFE90_high_low_MAE_bispecific_ADC_data_partner_bridge","current_profile_verdict":"current_profile_correct_if_data_quality_partner_validation_cash_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"298380_2024-02-22_21250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C24 can allow Stage2/Yellow or Green-candidate-watch when clinical data quality is tied to partner validation, economics and cash-runway bridge. Green still requires exact source-grade evidence."}
```

### 6.2 028300 HLB — regulatory CRL / approval shock hard 4C

Entry row: `2024-05-16 c=95800`, just before the hard regulatory break.
Observed path: `2024-05-17 c=67100`, `2024-05-20 l=47000`, and high volatility rebound later. The original event is a hard regulatory failure mode, not an ordinary pullback.

```jsonl
{"row_type":"trigger","trigger_id":"R7L93_C24_028300_20240516_STAGE2_4C_REGULATORY_CRL","case_id":"C24_R7L93_028300_HLB_REGULATORY_CRL_HARD4C","symbol":"028300","company_name":"HLB","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"REGULATORY_CRL_APPROVAL_SHOCK_HARD_BREAK","loop_objective":"hard_4C_confirmation;regulatory_failure_event;data_quality_watch","trigger_type":"Stage2-4C-Validated-RegulatoryCRLApprovalShockHardBreak","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":95800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_regulatory_approval_binary_event_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; regulatory CRL/approval refusal shock treated as hard 4C event when new regulatory path is missing","evidence_source_type":"historical_public_regulatory_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["binary_approval_event_proxy","regulatory_decision_risk_proxy","pre_CRL_price_risk"],"stage3_evidence_fields":["new_regulatory_path_missing","data_repair_missing","commercial_bridge_missing","ordinary_price_quality_missing"],"stage4b_evidence_fields":["deep_MAE","high_volatility","not_bargain_rebound"],"stage4c_evidence_fields":["regulatory_CRL_hard_break","approval_failure_watch","ordinary_rebound_disallowed"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv","profile_path":"atlas/symbol_profiles/028/028300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.59,"MFE_90D_pct":11.59,"MFE_180D_pct":11.59,"MAE_30D_pct":-52.87,"MAE_90D_pct":-52.87,"MAE_180D_pct":-52.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":106900.0,"max_drawdown_low_date":"2024-05-21","max_drawdown_low":45150.0,"drawdown_after_peak_pct":-57.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"regulatory_CRL_approval_shock_routes_to_hard_4C_not_positive_even_if_later_rebound_exists","four_b_evidence_type":["deep_MAE","high_volatility","not_bargain_rebound"],"four_c_protection_label":"regulatory_CRL_hard_break_ordinary_rebound_disallowed","trigger_outcome_label":"hard_4C_regulatory_CRL_shock_deep_MAE_not_bargain_rebound","current_profile_verdict":"current_profile_correct_if_CRL_or_regulatory_refusal_routes_to_hard_4C_not_4B_rebound","calibration_usable":true,"forward_window_trading_days":"disrupted_by_hard_regulatory_event_watch","calibration_block_reasons":["hard_4C_regulatory_event_watch","ordinary_forward_window_not_clean"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_usable_as_event_stress","same_entry_group_id":"028300_2024-05-16_95800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.8,"do_not_count_as_new_case":false,"current_profile_residual":"C24 should hard-route CRL/regulatory refusal rows to 4C until a new source-graded regulatory path exists. Local rebound must not be treated as positive Stage2 evidence."}
```

### 6.3 141080 리가켐바이오 — ADC platform/license bridge false-overblock after reset

Entry row: `2024-02-22 c=56100`, before name transition and 2024-04-23 share-count/corporate-action candidate.
Observed path: high `2024-06-20 h=77400`, and later high `2024-07-09 h=87200`. This row is not a blanket C24 overblock; it is an evidence-repair / false-overblock case.

```jsonl
{"row_type":"trigger","trigger_id":"R7L93_C24_141080_20240222_STAGE2_FALSE_OVERBLOCK_ADC_PLATFORM_LICENSE","case_id":"C24_R7L93_141080_LCG_ADC_PLATFORM_FALSE_OVERBLOCK","symbol":"141080","company_name":"리가켐바이오","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"ADC_PLATFORM_LICENSE_DATA_BRIDGE_FALSE_OVERBLOCK_AFTER_RESET","loop_objective":"false_overblock_mining;counterexample_mining;data_quality_watch;green_strictness_stress_test","trigger_type":"Stage2-FalsePositive-OverbroadTrialEventRiskWouldMissADCPlatformLicenseBridge","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":56100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_ADC_platform_license_data_bridge_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; ADC platform validation, license economics, pipeline optionality and partner data treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_partner_trial_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["ADC_platform_validation_proxy","license_economics_proxy","partner_data_proxy","pipeline_optionality_proxy"],"stage3_evidence_fields":["exact_license_source_pending","partner_data_source_pending","milestone_cash_source_pending","name_transition_share_count_repair_pending"],"stage4b_evidence_fields":["false_overblock_watch","name_transition_watch","share_count_movement_watch","Green_exact_evidence_watch"],"stage4c_evidence_fields":["trial_failure_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv","profile_path":"atlas/symbol_profiles/141/141080.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":49.73,"MFE_90D_pct":37.97,"MFE_180D_pct":55.44,"MAE_30D_pct":-5.53,"MAE_90D_pct":-5.53,"MAE_180D_pct":-5.53,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-09","peak_price":87200.0,"max_drawdown_low_date":"2024-02-22","max_drawdown_low":53000.0,"drawdown_after_peak_pct":-11.70,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"do_not_overblock_if_ADC_platform_license_data_bridge_exists_but_exact_evidence_and_name_transition_share_count_repair_required","four_b_evidence_type":["false_overblock_watch","name_transition_watch","share_count_movement_watch","Green_exact_evidence_watch"],"four_c_protection_label":"trial_failure_watch_only","trigger_outcome_label":"false_overblock_high_MFE_after_ADC_platform_bridge_but_name_transition_CA_watch","current_profile_verdict":"current_profile_false_positive_if_C24_guard_blocks_platform_license_data_bridge_after_reset","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["2024-04-19_name_transition_watch","2024-04-23_corporate_action_share_count_candidate_watch"],"corporate_action_window_status":"selected_entry_before_name_transition_and_2024-04-23_candidate; data_quality_repair_required","same_entry_group_id":"141080_2024-02-22_56100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.85,"do_not_count_as_new_case":false,"current_profile_residual":"C24 should not become a blanket biotech event-risk veto. If platform validation, license economics and partner data bridge exist after a reset, route to evidence repair rather than hard 4B, while data-quality repair remains mandatory."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C24_R7L93_298380_ABL_BISPECIFIC_ADC_DATA","trigger_id":"R7L93_C24_298380_20240222_STAGE2_BISPECIFIC_ADC_DATA","symbol":"298380","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C24 requires data quality, partner validation, milestone economics and cash runway rather than biotech event vocabulary alone","raw_component_scores_before":{"clinical_data_quality_score":12,"mechanism_quality_score":11,"partner_validation_score":12,"license_economics_score":9,"regulatory_path_score":7,"cash_runway_score":8,"commercial_optionality_score":7,"relative_strength_score":10,"binary_event_risk":-6,"dilution_risk":-4,"information_confidence":4},"weighted_score_before":68,"stage_label_before":"Stage2-Watch/PositiveControl","raw_component_scores_after":{"clinical_data_quality_score":15,"mechanism_quality_score":14,"partner_validation_score":15,"license_economics_score":12,"regulatory_path_score":9,"cash_runway_score":10,"commercial_optionality_score":9,"relative_strength_score":12,"binary_event_risk":-5,"dilution_risk":-3,"information_confidence":5},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable/Yellow-Watch","component_delta_explanation":"Bispecific/ADC data and partner bridge supports Yellow/Green-candidate watch; exact source-grade evidence required before Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C24_R7L93_028300_HLB_REGULATORY_CRL_HARD4C","trigger_id":"R7L93_C24_028300_20240516_STAGE2_4C_REGULATORY_CRL","symbol":"028300","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"regulatory CRL or approval refusal should route to hard 4C even when local rebound appears","raw_component_scores_before":{"clinical_data_quality_score":0,"mechanism_quality_score":0,"partner_validation_score":0,"license_economics_score":0,"regulatory_path_score":0,"cash_runway_score":1,"commercial_optionality_score":0,"relative_strength_score":3,"binary_event_risk":-35,"dilution_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage1/4C-Watch","raw_component_scores_after":{"clinical_data_quality_score":0,"mechanism_quality_score":0,"partner_validation_score":0,"license_economics_score":0,"regulatory_path_score":0,"cash_runway_score":0,"commercial_optionality_score":0,"relative_strength_score":0,"binary_event_risk":-45,"dilution_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Hard-4C/RegulatoryEvent","component_delta_explanation":"CRL/regulatory refusal and deep MAE block positive stages until a new regulatory evidence path exists."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C24_R7L93_141080_LCG_ADC_PLATFORM_FALSE_OVERBLOCK","trigger_id":"R7L93_C24_141080_20240222_STAGE2_FALSE_OVERBLOCK_ADC_PLATFORM_LICENSE","symbol":"141080","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"overbroad trial-event risk should not block a reset plus ADC platform/license bridge, but data-quality repair is mandatory","raw_component_scores_before":{"clinical_data_quality_score":10,"mechanism_quality_score":13,"partner_validation_score":12,"license_economics_score":13,"regulatory_path_score":7,"cash_runway_score":8,"commercial_optionality_score":10,"relative_strength_score":11,"binary_event_risk":-6,"dilution_risk":-6,"information_confidence":4},"weighted_score_before":70,"stage_label_before":"Stage2-Watch/FalseOverblock/DataQualityWatch","raw_component_scores_after":{"clinical_data_quality_score":13,"mechanism_quality_score":16,"partner_validation_score":15,"license_economics_score":15,"regulatory_path_score":9,"cash_runway_score":10,"commercial_optionality_score":12,"relative_strength_score":12,"binary_event_risk":-5,"dilution_risk":-5,"information_confidence":5},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow/Green-candidate-watch/DataQualityWatch","component_delta_explanation":"Platform-license bridge would be falsely overblocked by a blunt C24 risk guard; exact license/data evidence and name-transition/share-count repair still block automatic Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R7L93_C24_P0_CURRENT","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C24 needs explicit clinical-data quality, partner-validation economics, hard regulatory 4C taxonomy and false-overblock platform-license override","eligible_trigger_count":3,"avg_MFE90_pct":31.81,"avg_MAE90_pct":-20.41,"avg_MFE180_pct":37.64,"avg_MAE180_pct":-20.41,"hard_4C_count":1,"false_overblock_count":1,"data_quality_watch_count":1,"score_return_alignment_verdict":"mixed_without_C24_data_bridge_CRL_hard4C_false_overblock_taxonomy"}
{"row_type":"profile_comparison","comparison_id":"R7L93_C24_P1_SECTOR_SPECIFIC","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P1_L7_bio_trial_data_partner_validation_candidate","profile_scope":"sector_specific","profile_hypothesis":"L7 trial/data signals need clinical-data quality, mechanism, partner economics, cash runway or regulatory path before Stage2-Actionable; CRL routes to hard 4C","changed_axes":["clinical_data_quality_required","partner_validation_required","hard_CRL_4C_guard","platform_license_false_overblock_override"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_data_quality_partner_validation_license_economics_cash_or_regulatory_path_proxy","hard_4C_gate":"CRL_or_regulatory_refusal_or_approval_hard_break"},"eligible_trigger_count":3,"hard_4C_count":1,"false_overblock_count":1,"score_return_alignment_verdict":"better_if_exact_evidence_and_data_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R7L93_C24_P2_CANONICAL","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P2_C24_data_partner_CRL_false_overblock_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C24 should reward source-grade data/partner bridge, hard-block CRL, and avoid overblocking platform-license bridge after reset","changed_axes":["C24_trial_data_partner_license_bridge_required","C24_CRL_regulatory_refusal_hard_4C_guard","C24_ADC_platform_license_false_overblock_override","C24_name_transition_share_count_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"clinical_data_quality_or_partner_validation_plus_cash_or_license_economics_bridge_required","hard_4C_gate":"CRL_or_refusal_or_regulatory_path_break"},"eligible_trigger_count":3,"hard_4C_count":1,"false_overblock_count":1,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R7L93_C24_P3_COUNTEREXAMPLE_GUARD","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P3_C24_binary_event_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If binary regulatory failure exists, route to hard 4C; if data bridge exists, do not overblock merely because bio event-risk vocabulary is high","changed_axes":["C24_binary_event_hard_4C_guardrail","C24_deep_MAE_guardrail","C24_false_overblock_override_guardrail"],"changed_thresholds":{"bad_entry_filter":"CRL_or_regulatory_refusal OR bridge_missing_and_MAE90_le_minus25","override_gate":"reset_plus_platform_license_or_partner_data_bridge"},"eligible_trigger_count":3,"hard_4C_count":1,"false_overblock_count":1,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_ADC_DATA_POSITIVE_VS_CRL_HARD4C_FALSE_OVERBLOCK","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"validated_4C_count":1,"false_overblock_count":1,"4B_case_count":0,"4C_case_count":1,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":31.81,"avg_MAE90_pct":-20.41,"avg_MFE180_pct":37.64,"avg_MAE180_pct":-20.41,"stage2_hit_rate_MFE90_ge20":2.0,"hard_4C_regulatory_event_count":1,"interpretation":"C24 needs source-grade event discipline. 에이비엘바이오 shows bispecific/ADC data plus partner-validation bridge can support Yellow/Green-candidate-watch, HLB shows CRL/approval shock must route to hard 4C, and 리가켐바이오 shows overbroad trial-event blocking can miss a platform-license/data bridge after reset if data-quality repair is available."}
{"row_type":"stage_transition_summary","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"298380","trigger_type":"Stage2-Actionable-BispecificADCDataPartnerValidationBridge-Positive","entry_date":"2024-02-22","stage2_to_90D_outcome":"positive_high_MFE_low_MAE","stage2_to_180D_outcome":"bispecific_ADC_partner_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/Green-candidate when data quality is tied to partner validation, license economics, milestone and cash-runway bridge; exact evidence required for Green."}
{"row_type":"stage_transition_summary","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"028300","trigger_type":"Stage2-4C-Validated-RegulatoryCRLApprovalShockHardBreak","entry_date":"2024-05-16","stage2_to_90D_outcome":"hard_4C_deep_MAE_regulatory_break","stage2_to_180D_outcome":"CRL_or_regulatory_failure_not_bargain_rebound","MFE90_ge20":false,"MAE90_le_minus25":true,"transition_note":"Regulatory CRL or approval refusal routes to hard 4C even when later rebound appears."}
{"row_type":"stage_transition_summary","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"141080","trigger_type":"Stage2-FalsePositive-OverbroadTrialEventRiskWouldMissADCPlatformLicenseBridge","entry_date":"2024-02-22","stage2_to_90D_outcome":"false_overblock_high_MFE_data_quality_watch","stage2_to_180D_outcome":"ADC_platform_license_bridge_but_name_transition_share_count_repair_required","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Do not hard-block reset plus platform-license/data bridge merely because biotech event-risk vocabulary is high; data-quality repair required."}
{"row_type":"residual_contribution","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","residual_type":"ADC_data_partner_bridge_vs_CRL_hard4C_and_platform_license_false_overblock","contribution":"Adds one C24 positive bridge, one hard 4C CRL/regulatory shock row, and one false-overblock/data-quality row, selected because C24 is under-30 coverage.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"ADC_BISPECIFIC_DATA_LICENSE_BRIDGE_VS_REGULATORY_CRL_HARD_4C_AND_FALSE_OVERBLOCK","positive_case_count":1,"counterexample_count":2,"4B_case_count":0,"4C_case_count":1,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C24 now has one bispecific/ADC data-positive row, one regulatory CRL hard 4C row, and one platform-license false-overblock row; next C24 loops should exact-URL repair clinical data, endpoint/comparator quality, partner economics, regulatory path, cash runway and share-count/name-transition quality."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"C24_trial_data_partner_license_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"298380 worked when bispecific/ADC data and partner-validation proxy existed; hard event risk alone should not be promoted."}
{"row_type":"shadow_weight","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"C24_CRL_regulatory_refusal_hard_4C_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"hard_4C_guard","apply_now":false,"shadow_only":true,"evidence_basis":"028300 shows regulatory CRL/approval shock should route to hard 4C, not ordinary 4B or bargain rebound."}
{"row_type":"shadow_weight","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"C24_ADC_platform_license_false_overblock_override","scope":"canonical_archetype","candidate_delta":1.0,"direction":"override_guard","apply_now":false,"shadow_only":true,"evidence_basis":"141080 shows overbroad biotech event-risk blocking can miss an ADC platform/license bridge after reset."}
{"row_type":"shadow_weight","round":"R7","loop":"93","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"C24_name_transition_share_count_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"141080 has 2024 name transition and 2024-04-23 corporate-action/share-count candidate; production patching requires price-path/evidence repair."}
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
  - regulatory_CRL_hard_4C
  - trial_data_partner_validation_bridge_required
  - ADC_platform_license_false_overblock
  - name_transition_share_count_data_quality_watch
new_axis_proposed:
  - C24_trial_data_partner_license_bridge_required_shadow_only
  - C24_CRL_regulatory_refusal_hard_4C_guard_shadow_only
  - C24_ADC_platform_license_false_overblock_override_shadow_only
  - C24_name_transition_share_count_data_quality_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C24
  - full_4b_requires_non_price_evidence within C24
  - hard_4c_thesis_break_routes_to_4c within C24
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
`298380` has no corporate-action candidate and the selected 2024 window is clean.
`028300` has many older corporate-action/name-transition candidates before 2024, but the selected 2024 regulatory shock window is usable as hard 4C stress only.
`141080` changed name from 레고켐바이오 to 리가켐바이오 on 2024-04-19 and has a 2024-04-23 corporate-action/share-count candidate after selected entry; it remains data-quality watch before production patching.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
hard_4C_regulatory_event_watch = true for 028300
name_transition_share_count_watch = true for 141080
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
3. Confirm R7 / L7 / C24 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop was selected by coverage-index-first after recent C08/C09/C01/C07/C06/C10/C11/C19/C27 local expansions.
6. Confirm this loop avoided:
   - C24 top-covered symbols
   - previous R7 loop85 C23 symbols
   - previous R7 loop86 C25 symbols
   - previous R7 loop87 C24 symbols
   - previous R7 loop88 C23 symbols
   - previous R7 loop89 C25 symbols
   - previous R7 loop90 C24 symbols
   - previous R7 loop91 C23 symbols
   - previous R7 loop92 C25 symbols
7. Confirm touched C27/C19/C11 candidate rows are not ingested from this MD.
8. Keep 028300 as hard 4C regulatory-event stress only.
9. Keep 141080 in name-transition/share-count data-quality watch before patch consideration.
10. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C24-scoped safe patch candidates:
   - C24_trial_data_partner_license_bridge_required
   - C24_CRL_regulatory_refusal_hard_4C_guard
   - C24_ADC_platform_license_false_overblock_override
   - C24_name_transition_share_count_data_quality_guard
11. Do not loosen Stage3-Green.
12. Do not use future MFE/MAE in runtime scoring.
13. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R7
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK or C13_BATTERY_JV_UTILIZATION_AMPC_IRA or C28_SOFTWARE_SECURITY_CONTRACT_RETENTION depending on newest coverage pressure and recent-loop avoidance
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 bispecific/ADC data-positive bridge, 1 hard 4C regulatory-event row, and 1 false-overblock/data-quality row for R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK.
```

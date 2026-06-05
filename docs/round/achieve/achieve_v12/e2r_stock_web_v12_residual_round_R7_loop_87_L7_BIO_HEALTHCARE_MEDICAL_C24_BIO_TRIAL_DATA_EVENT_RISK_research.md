# E2R Stock-Web v12 Residual Research — R7 Loop 87 / L7 / C24

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R7
loop: 87
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: PLATFORM_LICENSE_DATA_EVENT_BRIDGE_VS_VACCINE_IMMUNO_ONCOLOGY_DATA_THEME_DECAY
sector: bio / healthcare / trial data / platform event / event-risk
output_file: e2r_stock_web_v12_residual_round_R7_loop_87_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R6 loop 87`.

```text
scheduled_round = R7
scheduled_loop = 87
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
```

R7 is restricted to bio / healthcare / medical.  
C24 is selected because recent R7 loops used C23 approval/commercialization and C25 medical-device export/reimbursement, while C24 is the clinical/trial-data event-risk bucket.

The No-Repeat Index shows C24 as:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK
rows = 30
symbols = 20
good/bad Stage2 = 13/9
4B/4C = 0/2
top-covered = 298380, 323990, 007390, 087010, 141080, 226950
```

This loop avoids that top-covered set and also avoids the immediately previous R7 loops:

```text
R7 loop85 C23: 145020, 302440, 086900
R7 loop86 C25: 335890, 228670, 065510
```

Selected symbols:

```text
196170, 206650, 950220
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"196170","company_name":"알테오젠","profile_path":"atlas/symbol_profiles/196/196170.json","first_date":"2014-12-12","last_date":"2026-02-20","trading_day_count":2745,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["2017-12-07","2017-12-28","2020-07-23","2020-08-13","2021-04-12"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"206650","company_name":"유바이오로직스","profile_path":"atlas/symbol_profiles/206/206650.json","first_date":"2017-01-24","last_date":"2026-02-20","trading_day_count":2221,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"950220","company_name":"네오이뮨텍","profile_path":"atlas/symbol_profiles/950/950220.json","first_date":"2021-03-16","last_date":"2026-02-20","trading_day_count":1210,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2025-09-30"],"has_major_raw_discontinuity":true,"calibration_caveat":"Future 2025 corporate-action candidate is outside selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"196170","trigger_type":"Stage2-Actionable-PlatformLicenseClinicalEventBridge-Positive","entry_date":"2024-02-23","duplicate_status":"new C24 symbol/trigger/date combination outside top-covered and previous R7 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"206650","trigger_type":"Stage2-FalsePositive-VaccineClinicalEventTheme-NoDurableEfficacyRevenueBridge","entry_date":"2024-02-15","duplicate_status":"new C24 symbol/trigger/date combination outside top-covered and previous R7 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"950220","trigger_type":"Stage2-FalsePositive-ImmunoOncologyDataTheme-NoEfficacyPartnerBridge","entry_date":"2024-03-22","duplicate_status":"new C24 symbol/trigger/date combination outside top-covered and previous R7 loop symbols"}
```

## 4. Research question

C24 is not “bio stock moved on data.”  
The useful bio event signal needs a data-to-business bridge: clean efficacy/safety readout, partner validation, regulatory path, dose or endpoint quality, commercial optionality, cash runway, and financing risk control. Without that bridge, the event is only a bright lab result on a screen; it has not yet become an approved, funded, partnered asset.

Residual question:

```text
Can C24 distinguish:
1. platform/license/data-event bridge with very high MFE and tolerable MAE,
2. vaccine/clinical theme rebound without durable efficacy, revenue or partner bridge,
3. immuno-oncology data-theme spike that decays when efficacy, partner and financing bridge are missing?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C24_R7L87_196170_ALTEOGEN_PLATFORM_EVENT_BRIDGE","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"PLATFORM_LICENSE_CLINICAL_EVENT_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-PlatformLicenseClinicalEventBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_partnered_platform_data_bridge_required","price_source":"Songdaiki/stock-web","notes":"Platform/license/data-event proxy produced a very high MFE path. Green still requires exact partner, endpoint, regulatory and cash-runway evidence."}
{"row_type":"case","case_id":"C24_R7L87_206650_EUBIO_VACCINE_EVENT_NO_DURABLE_BRIDGE","symbol":"206650","company_name":"유바이오로직스","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"VACCINE_CLINICAL_EVENT_THEME_WITHOUT_DURABLE_EFFICACY_REVENUE_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-VaccineClinicalEventTheme-NoDurableEfficacyRevenueBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_initial_MFE_below_Yellow_with_late_MAE","current_profile_verdict":"current_profile_false_positive_if_vaccine_event_theme_promoted_without_partner_revenue_bridge","price_source":"Songdaiki/stock-web","notes":"Vaccine/clinical-event rebound had MFE below a robust Yellow threshold and later MAE opened when efficacy, revenue and partner bridge remained unverified."}
{"row_type":"case","case_id":"C24_R7L87_950220_NEOIMMUNETECH_DATA_THEME_DECAY","symbol":"950220","company_name":"네오이뮨텍","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"IMMUNO_ONCOLOGY_DATA_THEME_WITHOUT_EFFICACY_PARTNER_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ImmunoOncologyDataTheme-NoEfficacyPartnerBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_event_spike_then_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_data_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Immuno-oncology/data theme had an event spike but later deep MAE when efficacy, partner and financing bridge failed to confirm."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 196170 알테오젠 — platform/license clinical-event bridge positive

Entry row: `2024-02-23 c=131200`.  
Observed path: entry-day low `119000`, high `2024-06-27 h=298500`, and later high `2024-11-11 h=455500`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L87_C24_196170_20240223_STAGE2_PLATFORM_LICENSE_EVENT","case_id":"C24_R7L87_196170_ALTEOGEN_PLATFORM_EVENT_BRIDGE","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"PLATFORM_LICENSE_CLINICAL_EVENT_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-PlatformLicenseClinicalEventBridge-Positive","trigger_date":"2024-02-23","entry_date":"2024-02-23","entry_price":131200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_platform_license_clinical_event_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; platform/license clinical data bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["partner_validation_proxy","platform_event_proxy","regulatory_path_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_partner_source_pending","endpoint_quality_pending","regulatory_milestone_pending","cash_runway_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":71.88,"MFE_90D_pct":127.52,"MFE_180D_pct":247.18,"MAE_30D_pct":-9.30,"MAE_90D_pct":-9.30,"MAE_180D_pct":-9.30,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":455500.0,"max_drawdown_low_date":"2024-02-23","max_drawdown_low":119000.0,"drawdown_after_peak_pct":-38.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_price_extension_watch; do not upgrade to Green without exact partner/end-point/regulatory evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_partnered_platform_data_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"196170_2024-02-23_131200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C24 can allow Stage2/Yellow when bio event strength is tied to platform validation, partner economics, endpoint/regulatory bridge and cash-runway control. Green still requires exact evidence."}
```

### 6.2 206650 유바이오로직스 — vaccine/clinical-event theme without durable efficacy/revenue bridge

Entry row: `2024-02-15 c=12350`.  
Observed path: local high `2024-04-08 h=14500`, then later low `2024-08-05 l=9350`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L87_C24_206650_20240215_STAGE2_FALSE_POSITIVE_VACCINE_EVENT","case_id":"C24_R7L87_206650_EUBIO_VACCINE_EVENT_NO_DURABLE_BRIDGE","symbol":"206650","company_name":"유바이오로직스","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"VACCINE_CLINICAL_EVENT_THEME_WITHOUT_DURABLE_EFFICACY_REVENUE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-VaccineClinicalEventTheme-NoDurableEfficacyRevenueBridge","trigger_date":"2024-02-15","entry_date":"2024-02-15","entry_price":12350.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_vaccine_clinical_event_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; vaccine/clinical event theme treated as insufficient without durable efficacy, procurement/revenue, partner and regulatory bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["vaccine_event_theme","clinical_update_proxy","relative_strength_rebound"],"stage3_evidence_fields":["durable_efficacy_bridge_missing","partner_revenue_bridge_missing","regulatory_path_missing","cash_runway_missing"],"stage4b_evidence_fields":["event_theme_watch","late_MAE_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/206/206650/2024.csv","profile_path":"atlas/symbol_profiles/206/206650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.31,"MFE_90D_pct":17.41,"MFE_180D_pct":17.41,"MAE_30D_pct":-6.07,"MAE_90D_pct":-6.07,"MAE_180D_pct":-24.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":14500.0,"max_drawdown_low_date":"2024-08-05","max_drawdown_low":9350.0,"drawdown_after_peak_pct":-35.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"clinical_event_theme_without_durable_efficacy_revenue_bridge_should_remain_watch_not_Yellow","four_b_evidence_type":["event_theme_watch","late_MAE_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_initial_MFE_below_Yellow_with_late_MAE","current_profile_verdict":"current_profile_false_positive_if_vaccine_event_theme_promoted_without_partner_revenue_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"206650_2024-02-15_12350","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C24 should keep vaccine clinical-event rebounds in Watch unless efficacy, partner/procurement revenue, regulatory path and cash-runway bridge are exact-evidence repaired."}
```

### 6.3 950220 네오이뮨텍 — immuno-oncology data theme without efficacy/partner bridge

Entry row: `2024-03-22 c=1800`.  
Observed path: high `2024-05-14 h=2120`, later lows `2024-08-05 l=1200` and `2024-12-09 l=1009`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L87_C24_950220_20240322_STAGE2_FALSE_POSITIVE_IMMUNO_ONCOLOGY_DATA","case_id":"C24_R7L87_950220_NEOIMMUNETECH_DATA_THEME_DECAY","symbol":"950220","company_name":"네오이뮨텍","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"IMMUNO_ONCOLOGY_DATA_THEME_WITHOUT_EFFICACY_PARTNER_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-ImmunoOncologyDataTheme-NoEfficacyPartnerBridge","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":1800.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_immuno_oncology_data_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; immuno-oncology data theme treated as insufficient without endpoint strength, partner validation, regulatory path and financing bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["immuno_oncology_data_theme","relative_strength_event_spike"],"stage3_evidence_fields":["efficacy_endpoint_bridge_missing","partner_validation_missing","regulatory_path_missing","financing_risk_unresolved"],"stage4b_evidence_fields":["price_only_local_peak","data_theme_fade_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/950/950220/2024.csv","profile_path":"atlas/symbol_profiles/950/950220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.83,"MFE_90D_pct":17.78,"MFE_180D_pct":17.78,"MAE_30D_pct":-19.72,"MAE_90D_pct":-33.33,"MAE_180D_pct":-43.94,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-14","peak_price":2120.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":1009.0,"drawdown_after_peak_pct":-52.41,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"immuno_oncology_data_theme_without_efficacy_partner_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","data_theme_fade_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_event_spike_then_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_data_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window; 2025-09-30_candidate_outside_window","same_entry_group_id":"950220_2024-03-22_1800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C24 should route data-theme spikes to Watch/4B unless efficacy, partner validation, regulatory path and financing bridge are verified. Initial event MFE is not enough when MAE opens deeply."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C24_R7L87_196170_ALTEOGEN_PLATFORM_EVENT_BRIDGE","trigger_id":"R7L87_C24_196170_20240223_STAGE2_PLATFORM_LICENSE_EVENT","symbol":"196170","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C24 requires platform/partner/data-event bridge rather than event label alone","raw_component_scores_before":{"endpoint_quality_score":13,"partner_validation_score":15,"regulatory_path_score":12,"commercial_optionality_score":13,"cash_runway_score":8,"relative_strength_score":15,"valuation_repricing_score":10,"financing_risk_score":-4,"event_spike_risk":-2,"information_confidence":5},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"endpoint_quality_score":16,"partner_validation_score":18,"regulatory_path_score":14,"commercial_optionality_score":16,"cash_runway_score":10,"relative_strength_score":16,"valuation_repricing_score":11,"financing_risk_score":-3,"event_spike_risk":-1,"information_confidence":6},"weighted_score_after":90,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Partner/platform event bridge and very high MFE support Yellow/Green-candidate watch; exact partner, endpoint and regulatory evidence still block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C24_R7L87_206650_EUBIO_VACCINE_EVENT_NO_DURABLE_BRIDGE","trigger_id":"R7L87_C24_206650_20240215_STAGE2_FALSE_POSITIVE_VACCINE_EVENT","symbol":"206650","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"vaccine clinical-event theme without durable efficacy and revenue bridge should remain Watch","raw_component_scores_before":{"endpoint_quality_score":5,"partner_validation_score":1,"regulatory_path_score":3,"commercial_optionality_score":2,"cash_runway_score":3,"relative_strength_score":9,"valuation_repricing_score":4,"financing_risk_score":-10,"event_spike_risk":-10,"information_confidence":3},"weighted_score_before":18,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"endpoint_quality_score":1,"partner_validation_score":0,"regulatory_path_score":1,"commercial_optionality_score":0,"cash_runway_score":2,"relative_strength_score":4,"valuation_repricing_score":1,"financing_risk_score":-16,"event_spike_risk":-16,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Watch-Blocked","component_delta_explanation":"MFE below robust Yellow threshold and missing durable efficacy/revenue bridge should block Yellow/Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C24_R7L87_950220_NEOIMMUNETECH_DATA_THEME_DECAY","trigger_id":"R7L87_C24_950220_20240322_STAGE2_FALSE_POSITIVE_IMMUNO_ONCOLOGY_DATA","symbol":"950220","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"immuno-oncology data theme without efficacy/partner bridge should be 4B-watch","raw_component_scores_before":{"endpoint_quality_score":4,"partner_validation_score":0,"regulatory_path_score":1,"commercial_optionality_score":1,"cash_runway_score":1,"relative_strength_score":12,"valuation_repricing_score":5,"financing_risk_score":-16,"event_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"endpoint_quality_score":0,"partner_validation_score":0,"regulatory_path_score":0,"commercial_optionality_score":0,"cash_runway_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"financing_risk_score":-24,"event_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Initial event MFE is outweighed by missing efficacy/partner bridge and deep MAE."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R7L87_C24_P0_CURRENT","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C24 needs explicit endpoint, partner, regulatory, cash-runway and financing-risk bridge taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":54.24,"avg_MAE90_pct":-16.23,"avg_MFE180_pct":94.12,"avg_MAE180_pct":-25.84,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.67,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C24_endpoint_partner_financing_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R7L87_C24_P1_SECTOR_SPECIFIC","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P1_L7_bio_endpoint_partner_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L7 bio event signals need endpoint quality, partner validation, regulatory path, commercial optionality or cash-runway bridge before Stage2-Actionable","changed_axes":["endpoint_quality_required","partner_validation_required","data_theme_financing_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_endpoint_partner_regulatory_commercial_or_cash_runway_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":54.24,"avg_MAE90_pct":-16.23,"avg_MFE180_pct":94.12,"avg_MAE180_pct":-25.84,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R7L87_C24_P2_CANONICAL","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P2_C24_endpoint_partner_financing_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C24 should reward validated endpoint/partner/regulatory conversion, not data-event theme spikes","changed_axes":["C24_endpoint_partner_bridge_required","C24_data_theme_local_4B_watch_guard","C24_financing_risk_guard"],"changed_thresholds":{"stage2_yellow_gate":"endpoint_quality_plus_partner_or_regulatory_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":54.24,"avg_MAE90_pct":-16.23,"avg_MFE180_pct":94.12,"avg_MAE180_pct":-25.84,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R7L87_C24_P3_COUNTEREXAMPLE_GUARD","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P3_C24_event_spike_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If endpoint/partner bridge is missing and MFE90<20 with MAE90<=-20 or MAE180<=-35, block Yellow/Green","changed_axes":["C24_event_spike_high_MAE_guardrail","C24_low_MFE_no_partner_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_MFE90_lt_20_and_(MAE90_le_minus_20_or_MAE180_le_minus_35)"},"eligible_trigger_count":3,"avg_MFE90_pct":54.24,"avg_MAE90_pct":-16.23,"avg_MFE180_pct":94.12,"avg_MAE180_pct":-25.84,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_PLATFORM_LICENSE_EVENT_VS_DATA_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":1,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":54.24,"avg_MAE90_pct":-16.23,"avg_MFE180_pct":94.12,"avg_MAE180_pct":-25.84,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_bridge_missing_MFE90_lt20_and_MAE90_le_minus20_or_MAE180_le_minus35":0.33,"interpretation":"C24 needs bridge discipline. 알테오젠 shows platform/partner event bridge can rerate massively, while 유바이오로직스 and 네오이뮨텍 show clinical/data themes should stay Watch/4B unless efficacy, partner, regulatory and financing bridges are repaired."}
{"row_type":"stage_transition_summary","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"196170","trigger_type":"Stage2-Actionable-PlatformLicenseClinicalEventBridge-Positive","entry_date":"2024-02-23","stage2_to_90D_outcome":"good_stage2_very_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_platform_event_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when platform event is tied to partner validation, endpoint/regulatory path and cash-runway control; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"206650","trigger_type":"Stage2-FalsePositive-VaccineClinicalEventTheme-NoDurableEfficacyRevenueBridge","entry_date":"2024-02-15","stage2_to_90D_outcome":"weak_stage2_MFE_below_Yellow_threshold","stage2_to_180D_outcome":"late_MAE_without_partner_revenue_bridge","MFE90_ge_20":false,"MAE180_le_minus_20":true,"transition_note":"Vaccine event rebound without durable efficacy/revenue bridge should remain Watch."}
{"row_type":"stage_transition_summary","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"950220","trigger_type":"Stage2-FalsePositive-ImmunoOncologyDataTheme-NoEfficacyPartnerBridge","entry_date":"2024-03-22","stage2_to_90D_outcome":"bad_stage2_event_spike_deep_MAE","stage2_to_180D_outcome":"failed_data_theme_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Immuno-oncology data theme without efficacy/partner bridge should stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","residual_type":"bio_data_event_theme_overcredit_without_endpoint_partner_regulatory_financing_bridge","contribution":"Adds one C24 hard 4B data-theme counterexample and one weak-event Watch counterexample against one platform/partner event positive, avoiding C24 top-covered and previous R7 C23/C25 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"PLATFORM_LICENSE_DATA_EVENT_BRIDGE_VS_VACCINE_IMMUNO_ONCOLOGY_DATA_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":1,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C24 now has non-top-symbol platform positive and data-theme counterexamples; next R7 loops should exact-URL repair endpoint quality, partner validation, regulatory path, commercial optionality, cash runway and financing-risk evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"C24_endpoint_partner_regulatory_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"196170 worked when platform/partner event proxy was present; 206650 and 950220 were weak or failed when data-event theme lacked durable endpoint, partner, regulatory and financing bridge."}
{"row_type":"shadow_weight","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"C24_data_event_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Data-theme event rows showed MFE below robust Yellow threshold and later deep MAE without partner/evidence bridge."}
{"row_type":"shadow_weight","round":"R7","loop":"87","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"C24_financing_risk_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If endpoint/partner bridge is missing and MFE90<20 with MAE90<=-20 or MAE180<=-35, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - bio_data_event_theme_overcredit
  - endpoint_quality_bridge_missing
  - partner_validation_bridge_missing
  - financing_risk_unresolved
new_axis_proposed:
  - C24_endpoint_partner_regulatory_bridge_required_shadow_only
  - C24_data_event_theme_local_4B_watch_guard_shadow_only
  - C24_financing_risk_guardrail_shadow_only
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
3. Confirm R7 / L7 / C24 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C24 top-covered symbols
   - previous R7 loop85 C23 symbols
   - previous R7 loop86 C25 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C24-scoped safe patch candidates:
   - C24_endpoint_partner_regulatory_bridge_required
   - C24_data_event_theme_local_4B_watch_guard
   - C24_financing_risk_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R7
completed_loop = 87
next_round = R8
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 1 local 4B-watch row for R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK.
```

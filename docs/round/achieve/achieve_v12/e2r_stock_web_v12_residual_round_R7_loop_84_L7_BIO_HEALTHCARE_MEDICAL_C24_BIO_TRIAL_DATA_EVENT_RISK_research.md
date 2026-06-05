# E2R Stock-Web v12 Residual Research — R7 Loop 84 / L7 / C24

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R7
loop: 84
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_PLATFORM_TRIAL_EVENT_VALIDATION_BRIDGE_VS_CLINICAL_THEME_SPIKE_HIGH_MAE
sector: bio / healthcare / clinical data event risk
output_file: e2r_stock_web_v12_residual_round_R7_loop_84_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R6 loop 84`.

```text
scheduled_round = R7
scheduled_loop = 84
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
```

R7 is restricted to bio / healthcare / medical.  
C24 is selected because clinical/data-event risk needs stronger distinction between validated platform/event bridge and theme-only bio spikes. The selected symbols avoid the C24 top-covered list in the No-Repeat ledger: `298380`, `323990`, `007390`, `087010`, `141080`, and `226950`.

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"196170","company_name":"알테오젠","profile_path":"atlas/symbol_profiles/196/196170.json","first_date":"2014-12-12","last_date":"2026-02-20","trading_day_count":2745,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["2017-12-07","2017-12-28","2020-07-23","2020-08-13","2021-04-12"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"095700","company_name":"제넥신","profile_path":"atlas/symbol_profiles/095/095700.json","first_date":"2009-09-15","last_date":"2026-02-20","trading_day_count":4047,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["2012-11-19","2016-03-02","2016-03-24","2023-01-26","2023-02-02"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"206650","company_name":"유바이오로직스","profile_path":"atlas/symbol_profiles/206/206650.json","first_date":"2017-01-24","last_date":"2026-02-20","trading_day_count":2221,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.

Hard duplicate key rule applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"196170","trigger_type":"Stage2-Actionable-PlatformTrialEventValidationBridge-Positive","entry_date":"2024-02-22","duplicate_status":"new C24 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"095700","trigger_type":"Stage2-FalsePositive-ClinicalTrialRebound-NoDurableDataBridge","entry_date":"2024-03-18","duplicate_status":"new C24 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"206650","trigger_type":"Stage2-FalsePositive-VaccineClinicalThemeSpike-NoCommercialBridge","entry_date":"2024-04-15","duplicate_status":"new C24 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C24 is the event-risk chamber. In bio, a single spark can look like daylight: trial readout, platform validation, vaccine data, licensing optionality. E2R should only upgrade when the event is connected to durable validation, partner/customer credibility, regulatory path, funding runway, and eventually revenue/royalty bridge.

Residual question:

```text
Can C24 distinguish:
1. validated platform/trial event bridge with sustained MFE,
2. clinical theme rebound with no durable data bridge,
3. vaccine/clinical theme spike with no commercial or regulatory conversion bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C24_R7L84_196170_ALTEOGEN_PLATFORM_EVENT_VALIDATION_BRIDGE","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"PLATFORM_TRIAL_EVENT_VALIDATION_PARTNER_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-PlatformTrialEventValidationBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_high_initial_MAE","current_profile_verdict":"current_profile_correct_if_partner_validation_bridge_required","price_source":"Songdaiki/stock-web","notes":"Platform/event validation produced a very large forward MFE, but the same entry had high intraday MAE; C24 should permit Stage2/Yellow only when non-price validation bridge is present."}
{"row_type":"case","case_id":"C24_R7L84_095700_GENEXINE_TRIAL_REBOUND_NO_DATA_BRIDGE","symbol":"095700","company_name":"제넥신","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_TRIAL_THEME_REBOUND_WITHOUT_DURABLE_DATA_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ClinicalTrialRebound-NoDurableDataBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_trial_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Clinical rebound failed without durable data, partner, or commercialization bridge; high MAE argues for a C24 local guard."}
{"row_type":"case","case_id":"C24_R7L84_206650_EUBIOLOGICS_VACCINE_THEME_SPIKE_NO_COMMERCIAL_BRIDGE","symbol":"206650","company_name":"유바이오로직스","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"VACCINE_CLINICAL_THEME_SPIKE_WITHOUT_COMMERCIAL_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-VaccineClinicalThemeSpike-NoCommercialBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE_before_late_rebound","current_profile_verdict":"current_profile_false_positive_if_vaccine_theme_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Vaccine/clinical theme spike had limited near-term MFE and high MAE before a later unrelated rebound; C24 needs a bridge gate."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 196170 알테오젠 — platform/trial-event validation bridge positive

Entry row: `2024-02-22 c=105000`.  
Forward path: same-day low `85000`, 30D peak `2024-03-18/03-26 h=225500`, 90D peak `2024-06-13 h=291000`, 180D peak `2024-11-11 h=455500`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L84_C24_196170_20240222_STAGE2_PLATFORM_EVENT_VALIDATION_BRIDGE","case_id":"C24_R7L84_196170_ALTEOGEN_PLATFORM_EVENT_VALIDATION_BRIDGE","symbol":"196170","company_name":"알테오젠","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"PLATFORM_TRIAL_EVENT_VALIDATION_PARTNER_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-PlatformTrialEventValidationBridge-Positive","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":105000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_platform_validation_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; platform/trial event validation and partner-quality bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_disclosure_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["platform_validation_proxy","partner_quality_proxy","event_readthrough_strength"],"stage3_evidence_fields":["royalty_or_commercialization_bridge_pending","source_url_pending","multi_source_confirmation_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/196/196170/2024.csv","profile_path":"atlas/symbol_profiles/196/196170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":114.76,"MFE_90D_pct":177.14,"MFE_180D_pct":333.81,"MAE_30D_pct":-19.05,"MAE_90D_pct":-19.05,"MAE_180D_pct":-19.05,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-11","peak_price":455500.0,"max_drawdown_low_date":"2024-02-22","max_drawdown_low":85000.0,"drawdown_after_peak_pct":-39.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_high_initial_MAE","current_profile_verdict":"current_profile_correct_if_partner_validation_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"196170_2024-02-22_105000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C24 should not block all high-volatility bio events. Very high MFE can be valid when a platform/partner validation bridge exists, but Green still needs exact source repair and commercialization/royalty bridge."}
```

### 6.2 095700 제넥신 — clinical rebound without durable data bridge

Entry row: `2024-03-18 c=9180`.  
Forward path: same-day high `9760`, then lows reached `2024-06-24 l=6210` and `2024-12-09 l=4960`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L84_C24_095700_20240318_STAGE2_FALSE_POSITIVE_TRIAL_REBOUND_NO_DATA_BRIDGE","case_id":"C24_R7L84_095700_GENEXINE_TRIAL_REBOUND_NO_DATA_BRIDGE","symbol":"095700","company_name":"제넥신","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CLINICAL_TRIAL_THEME_REBOUND_WITHOUT_DURABLE_DATA_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-ClinicalTrialRebound-NoDurableDataBridge","trigger_date":"2024-03-18","entry_date":"2024-03-18","entry_price":9180.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_clinical_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; clinical trial/theme rebound treated as insufficient unless durable data, partner, runway, and commercialization bridge are verified","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["trial_theme_rebound","relative_strength_spike"],"stage3_evidence_fields":["durable_data_bridge_missing","partner_quality_missing","commercialization_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","thesis_break_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095700/2024.csv","profile_path":"atlas/symbol_profiles/095/095700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.32,"MFE_90D_pct":6.32,"MFE_180D_pct":11.44,"MAE_30D_pct":-25.49,"MAE_90D_pct":-32.35,"MAE_180D_pct":-45.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-17","peak_price":10230.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":4960.0,"drawdown_after_peak_pct":-51.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"theme_peak_without_data_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","thesis_break_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_trial_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"095700_2024-03-18_9180","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Trial/theme rebound without durable data bridge produced low MFE and deep MAE. C24 needs a data-quality/partner/commercialization bridge gate before Stage2-Actionable or Yellow."}
```

### 6.3 206650 유바이오로직스 — vaccine/clinical theme spike without commercial bridge

Entry row: `2024-04-15 c=13900`.  
Forward path: 30D/90D peak `2024-04-22 h=14500`, then low `2024-07-16 l=10700`; later unrelated rebound reached `2024-11-06 h=18800`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L84_C24_206650_20240415_STAGE2_FALSE_POSITIVE_VACCINE_THEME_SPIKE","case_id":"C24_R7L84_206650_EUBIOLOGICS_VACCINE_THEME_SPIKE_NO_COMMERCIAL_BRIDGE","symbol":"206650","company_name":"유바이오로직스","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"VACCINE_CLINICAL_THEME_SPIKE_WITHOUT_COMMERCIAL_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-VaccineClinicalThemeSpike-NoCommercialBridge","trigger_date":"2024-04-15","entry_date":"2024-04-15","entry_price":13900.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_vaccine_clinical_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; vaccine/clinical theme spike treated as insufficient without confirmed regulatory, commercial, and shipment bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["vaccine_clinical_theme_spike","relative_strength_rebound"],"stage3_evidence_fields":["regulatory_bridge_missing","commercial_bridge_missing","shipment_revenue_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/206/206650/2024.csv","profile_path":"atlas/symbol_profiles/206/206650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.32,"MFE_90D_pct":4.32,"MFE_180D_pct":35.25,"MAE_30D_pct":-7.41,"MAE_90D_pct":-23.02,"MAE_180D_pct":-23.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-06","peak_price":18800.0,"max_drawdown_low_date":"2024-07-16","max_drawdown_low":10700.0,"drawdown_after_peak_pct":-37.77,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"initial_theme_peak_should_remain_watch_until_commercial_bridge; later rebound should not rehabilitate initial weak bridge","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE_before_late_rebound","current_profile_verdict":"current_profile_false_positive_if_vaccine_theme_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"206650_2024-04-15_13900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"Vaccine/clinical theme spike had low 30/90D MFE and high 90D MAE before a later rebound. C24 should require regulatory/commercial bridge rather than using later price recovery to justify early entry."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C24_R7L84_196170_ALTEOGEN_PLATFORM_EVENT_VALIDATION_BRIDGE","trigger_id":"R7L84_C24_196170_20240222_STAGE2_PLATFORM_EVENT_VALIDATION_BRIDGE","symbol":"196170","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C24 requires partner/platform validation bridge rather than price-only event spike","raw_component_scores_before":{"clinical_event_quality":17,"data_durability":14,"partner_quality":17,"commercialization_bridge":9,"regulatory_path":10,"runway_quality":8,"relative_strength":18,"valuation_repricing":12,"event_failure_risk":-7,"information_confidence":5},"weighted_score_before":80,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"clinical_event_quality":19,"data_durability":16,"partner_quality":19,"commercialization_bridge":11,"regulatory_path":12,"runway_quality":9,"relative_strength":18,"valuation_repricing":13,"event_failure_risk":-6,"information_confidence":6},"weighted_score_after":87,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Platform/partner validation can overcome initial volatility, but exact evidence and commercialization bridge are needed before Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C24_R7L84_095700_GENEXINE_TRIAL_REBOUND_NO_DATA_BRIDGE","trigger_id":"R7L84_C24_095700_20240318_STAGE2_FALSE_POSITIVE_TRIAL_REBOUND_NO_DATA_BRIDGE","symbol":"095700","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"trial theme without durable data bridge should be blocked","raw_component_scores_before":{"clinical_event_quality":7,"data_durability":3,"partner_quality":2,"commercialization_bridge":1,"regulatory_path":3,"runway_quality":3,"relative_strength":11,"valuation_repricing":6,"event_failure_risk":-15,"information_confidence":3},"weighted_score_before":24,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"clinical_event_quality":4,"data_durability":0,"partner_quality":0,"commercialization_bridge":0,"regulatory_path":1,"runway_quality":2,"relative_strength":5,"valuation_repricing":2,"event_failure_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and deep MAE convert clinical rebound into evidence-quality failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C24_R7L84_206650_EUBIOLOGICS_VACCINE_THEME_SPIKE_NO_COMMERCIAL_BRIDGE","trigger_id":"R7L84_C24_206650_20240415_STAGE2_FALSE_POSITIVE_VACCINE_THEME_SPIKE","symbol":"206650","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"vaccine/clinical theme spike without commercial bridge should stay Watch even if later rebound appears","raw_component_scores_before":{"clinical_event_quality":8,"data_durability":4,"partner_quality":3,"commercialization_bridge":2,"regulatory_path":5,"runway_quality":4,"relative_strength":10,"valuation_repricing":7,"event_failure_risk":-12,"information_confidence":3},"weighted_score_before":34,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"clinical_event_quality":5,"data_durability":2,"partner_quality":1,"commercialization_bridge":0,"regulatory_path":3,"runway_quality":3,"relative_strength":5,"valuation_repricing":3,"event_failure_risk":-18,"information_confidence":2},"weighted_score_after":6,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Initial event spike had weak MFE and high MAE before later rebound; commercial bridge gate should block early upgrade."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R7L84_C24_P0_CURRENT","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C24 needs explicit partner/data/commercial bridge distinction","eligible_trigger_count":3,"avg_MFE_90D_pct":62.59,"avg_MAE_90D_pct":-24.81,"avg_MFE_180D_pct":126.83,"avg_MAE_180D_pct":-29.31,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C24_event_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R7L84_C24_P1_SECTOR_SPECIFIC","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P1_L7_clinical_event_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L7 bio event signals need durable data, partner, regulatory, or commercialization bridge before Stage2-Actionable","changed_axes":["data_durability_required","partner_quality_required","commercialization_bridge_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_partner_data_or_regulatory_bridge"},"eligible_trigger_count":3,"avg_MFE_90D_pct":62.59,"avg_MAE_90D_pct":-24.81,"avg_MFE_180D_pct":126.83,"avg_MAE_180D_pct":-29.31,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R7L84_C24_P2_CANONICAL","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P2_C24_data_partner_commercial_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C24 should reward validated event bridge, not clinical theme spikes","changed_axes":["C24_durable_data_bridge_required","C24_partner_quality_bridge_required","C24_theme_spike_penalty"],"changed_thresholds":{"stage2_yellow_gate":"data_partner_or_commercial_bridge_required"},"eligible_trigger_count":3,"avg_MFE_90D_pct":62.59,"avg_MAE_90D_pct":-24.81,"avg_MFE_180D_pct":126.83,"avg_MAE_180D_pct":-29.31,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R7L84_C24_P3_COUNTEREXAMPLE_GUARD","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P3_C24_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-20 while durable data/partner bridge is missing, block Yellow/Green","changed_axes":["C24_high_MAE_guardrail","C24_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_20"},"eligible_trigger_count":3,"avg_MFE_90D_pct":62.59,"avg_MAE_90D_pct":-24.81,"avg_MFE_180D_pct":126.83,"avg_MAE_180D_pct":-29.31,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_PLATFORM_VALIDATION_VS_CLINICAL_THEME_SPIKE","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":62.59,"avg_MAE90_pct":-24.81,"avg_MFE180_pct":126.83,"avg_MAE180_pct":-29.31,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MAE90_le_minus_20":0.67,"interpretation":"C24 needs bridge discipline. 196170 shows a valid platform/partner validation bridge, while 095700 and 206650 show clinical/vaccine theme spikes that fail without durable data or commercialization bridge."}
{"row_type":"stage_transition_summary","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"196170","trigger_type":"Stage2-Actionable-PlatformTrialEventValidationBridge-Positive","entry_date":"2024-02-22","stage2_to_90D_outcome":"good_stage2_very_high_MFE_with_high_initial_MAE","stage2_to_180D_outcome":"positive_re_rating_path","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when partner/platform validation exists; Green requires exact source and commercialization bridge."}
{"row_type":"stage_transition_summary","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"095700","trigger_type":"Stage2-FalsePositive-ClinicalTrialRebound-NoDurableDataBridge","entry_date":"2024-03-18","stage2_to_90D_outcome":"bad_stage2_high_MAE","stage2_to_180D_outcome":"failed_entry_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Clinical theme rebound without durable data/partner bridge should stay Watch/blocked."}
{"row_type":"stage_transition_summary","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"206650","trigger_type":"Stage2-FalsePositive-VaccineClinicalThemeSpike-NoCommercialBridge","entry_date":"2024-04-15","stage2_to_90D_outcome":"bad_stage2_high_MAE_before_late_rebound","stage2_to_180D_outcome":"mixed_late_rebound_not_entry_validation","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Later rebound should not validate the initial weak-bridge event; commercial/regulatory bridge is required."}
{"row_type":"residual_contribution","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","residual_type":"bio_event_theme_overcredit_without_data_partner_commercial_bridge","contribution":"Adds two C24 high-MAE counterexamples against one platform-validation positive, improving C24 local guardrail evidence outside the top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_TRIAL_EVENT_VALIDATION_BRIDGE_VS_CLINICAL_THEME_SPIKE_HIGH_MAE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C24 now has non-top-symbol theme-spike counterexamples; next R7 loops should exact-URL repair clinical data and partner/commercialization evidence and add true 4C trial-failure rows."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"C24_durable_data_partner_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"196170 worked with platform/partner validation bridge proxy; 095700 and 206650 failed or produced high MAE when data/commercialization bridge was missing."}
{"row_type":"shadow_weight","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"C24_theme_spike_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Clinical/vaccine theme spikes showed low 30/90D MFE and high MAE without durable data or commercialization evidence."}
{"row_type":"shadow_weight","round":"R7","loop":"84","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"C24_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<10 and MAE90<=-20 while durable data/partner/commercialization bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - bio_event_theme_overcredit
  - clinical_trial_rebound_no_durable_data_bridge
  - vaccine_clinical_theme_no_commercial_bridge
new_axis_proposed:
  - C24_durable_data_partner_bridge_required_shadow_only
  - C24_theme_spike_local_4B_watch_guard_shadow_only
  - C24_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C24
  - full_4b_requires_non_price_evidence within C24
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
3. Confirm R7 / L7 / C24 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. If aggregate support remains stable after exact evidence URL repair, consider C24-scoped safe patch candidates:
   - C24_durable_data_partner_bridge_required
   - C24_theme_spike_local_4B_watch_guard
   - C24_high_MAE_guardrail
6. Do not loosen Stage3-Green.
7. Do not use future MFE/MAE in runtime scoring.
8. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R7
completed_loop = 84
next_round = R8
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK.
```

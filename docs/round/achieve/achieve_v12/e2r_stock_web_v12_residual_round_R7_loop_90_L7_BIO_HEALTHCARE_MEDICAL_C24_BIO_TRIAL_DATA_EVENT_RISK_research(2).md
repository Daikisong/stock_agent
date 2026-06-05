# E2R Stock-Web v12 Residual Research — R7 Loop 90 / L7 / C24

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R7
loop: 90
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: RNA_PLATFORM_TRIAL_DATA_MANUFACTURING_BRIDGE_VS_VASCULAR_THERAPEUTIC_EVENT_PRICE_DECAY
sector: bio / healthcare / trial data / clinical catalyst / RNA therapeutics / vascular disease / regulatory event risk
output_file: e2r_stock_web_v12_residual_round_R7_loop_90_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R6 loop 90`.

```text
scheduled_round = R7
scheduled_loop = 90
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
```

R7 is restricted to bio / healthcare / medical.  
C24 is selected because recent R7 loops already covered:

```text
R7 loop85: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
R7 loop86: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
R7 loop87: C24_BIO_TRIAL_DATA_EVENT_RISK
R7 loop88: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
R7 loop89: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

After C25, the R7 lane returns to C24.

No-Repeat Index snapshot:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK
rows = 30
symbols = 20
good/bad Stage2 = 13/9
4B/4C = 0/2
top-covered = 298380, 323990, 007390, 087010, 141080, 226950
```

This loop avoids the C24 top-covered symbols and recent R7 loop symbols:

```text
R7 loop85 C23: 145020, 302440, 086900
R7 loop86 C25: 335890, 228670, 065510
R7 loop87 C24: 196170, 206650, 950220
R7 loop88 C23: 000250, 019170, 095700
R7 loop89 C25: 200670, 119610, 290650
```

Selected symbols:

```text
237690, 365270, 256840
```

This loop tests:

```text
RNA / oligonucleotide platform data and manufacturing bridge
vs
vascular-disease trial event spike without partner/regulatory/commercial bridge
vs
therapeutic event momentum without durable trial-to-regulatory and cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"237690","company_name":"에스티팜","profile_path":"atlas/symbol_profiles/237/237690.json","first_date":"2016-06-23","last_date":"2026-02-20","trading_day_count":2370,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"365270","company_name":"큐라클","profile_path":"atlas/symbol_profiles/365/365270.json","first_date":"2021-07-22","last_date":"2026-02-20","trading_day_count":1120,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2025-09-22"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists after the selected 2024 calibration window; selected 2024 window is usable.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; 2025_candidate_outside_window"}
{"row_type":"price_source_validation","symbol":"256840","company_name":"한국비엔씨","profile_path":"atlas/symbol_profiles/256/256840.json","first_date":"2016-12-28","last_date":"2026-02-20","trading_day_count":2174,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2019-12-03","2022-03-30"],"has_major_raw_discontinuity":true,"calibration_caveat":"SPAC/name-transition and corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"237690","trigger_type":"Stage2-Actionable-RNAPlatformTrialDataManufacturingBridge-Positive","entry_date":"2024-02-23","duplicate_status":"new C24 symbol/trigger/date combination outside top-covered and previous R7 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"365270","trigger_type":"Stage2-FalsePositive-VascularTherapeuticTrialEventNoPartnerRegulatoryBridge","entry_date":"2024-03-20","duplicate_status":"new C24 symbol/trigger/date combination outside top-covered and previous R7 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"256840","trigger_type":"Stage2-FalsePositive-TherapeuticEventMomentumNoRegulatoryCommercialBridge","entry_date":"2024-03-20","duplicate_status":"new C24 symbol/trigger/date combination outside top-covered and previous R7 loop symbols"}
```

## 4. Research question

C24 is not “바이오 이벤트가 있다.”  
The useful trial-data/event signal must prove a bridge from data to monetizable probability:

```text
trial endpoint quality
sample size and statistical clarity
safety/tolerability
mechanism consistency
regulatory pathway
partner or licensing validation
manufacturing or CMC readiness
commercial probability
cash runway and dilution risk
```

A bio catalyst without this bridge is a lab signal still inside a petri dish. It glows, but it has not crossed into regulator, partner, patient, and cash flow.

Residual question:

```text
Can C24 distinguish:
1. RNA / oligonucleotide platform plus manufacturing-capacity bridge where data/event momentum has follow-through,
2. vascular-disease clinical-event spike where partner/regulatory/commercial bridge is missing and the price path collapses,
3. therapeutic event momentum where local MFE exists but no durable regulatory/commercial and cash bridge exists?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C24_R7L90_237690_STPHARM_RNA_PLATFORM_BRIDGE","symbol":"237690","company_name":"에스티팜","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"RNA_PLATFORM_TRIAL_DATA_MANUFACTURING_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-RNAPlatformTrialDataManufacturingBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_low_MAE_platform_bridge","current_profile_verdict":"current_profile_correct_if_endpoint_partner_manufacturing_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"RNA/oligonucleotide platform plus manufacturing bridge proxy produced high forward MFE and shallow MAE. Green still requires exact endpoint/partner/manufacturing/cash evidence."}
{"row_type":"case","case_id":"C24_R7L90_365270_CURACLE_VASCULAR_EVENT_SPIKE","symbol":"365270","company_name":"큐라클","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"VASCULAR_THERAPEUTIC_EVENT_SPIKE_WITHOUT_PARTNER_REGULATORY_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-VascularTherapeuticTrialEventNoPartnerRegulatoryBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_sub_Yellow_MFE_extreme_MAE_no_regulatory_bridge","current_profile_verdict":"current_profile_false_positive_if_trial_event_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Vascular therapeutic event spike had sub-Yellow MFE and extreme later MAE without partner, regulatory pathway, endpoint durability or cash bridge."}
{"row_type":"case","case_id":"C24_R7L90_256840_KOREA_BNC_THERAPEUTIC_EVENT_MOMENTUM","symbol":"256840","company_name":"한국비엔씨","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"THERAPEUTIC_EVENT_MOMENTUM_WITHOUT_REGULATORY_COMMERCIAL_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-TherapeuticEventMomentumNoRegulatoryCommercialBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_local_MFE_deep_MAE_no_commercial_bridge","current_profile_verdict":"current_profile_false_positive_if_therapeutic_event_momentum_overcredited","price_source":"Songdaiki/stock-web","notes":"Therapeutic event momentum had local MFE but later deep MAE; without regulatory path, partner validation, commercial probability and cash runway, it should stay 4B-watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 237690 에스티팜 — RNA / oligonucleotide platform trial-data and manufacturing bridge positive

Entry row: `2024-02-23 c=66300`.  
Observed path includes visible follow-through from `2024-03-18 h=99000` and later autumn highs above `110000`, while the early post-entry low stayed close to entry.

```jsonl
{"row_type":"trigger","trigger_id":"R7L90_C24_237690_20240223_STAGE2_RNA_PLATFORM_BRIDGE","case_id":"C24_R7L90_237690_STPHARM_RNA_PLATFORM_BRIDGE","symbol":"237690","company_name":"에스티팜","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"RNA_PLATFORM_TRIAL_DATA_MANUFACTURING_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-RNAPlatformTrialDataManufacturingBridge-Positive","trigger_date":"2024-02-23","entry_date":"2024-02-23","entry_price":66300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_RNA_oligonucleotide_platform_trial_data_manufacturing_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; RNA/oligo platform, trial-data probability, manufacturing/CMC and partner bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["RNA_platform_proxy","clinical_data_probability_proxy","manufacturing_capacity_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_endpoint_quality_pending","partner_validation_pending","CMC_manufacturing_source_pending","cash_runway_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/237/237690/2024.csv","profile_path":"atlas/symbol_profiles/237/237690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":49.32,"MFE_90D_pct":49.32,"MFE_180D_pct":71.19,"MAE_30D_pct":-3.92,"MAE_90D_pct":-3.92,"MAE_180D_pct":-3.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-24","peak_price":113500.0,"max_drawdown_low_date":"2024-02-27","max_drawdown_low":63700.0,"drawdown_after_peak_pct":-33.39,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.58,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_endpoint_partner_CMC_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_low_MAE_platform_bridge","current_profile_verdict":"current_profile_correct_if_endpoint_partner_manufacturing_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"237690_2024-02-23_66300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C24 can allow Stage2/Yellow when bio-event strength is tied to endpoint quality, mechanism, partner validation, manufacturing/CMC readiness and cash runway. Green still requires exact source-grade evidence."}
```

### 6.2 365270 큐라클 — vascular therapeutic trial-event spike without partner/regulatory bridge

Entry row: `2024-03-20 c=18630`, on the event spike.  
Observed path had only sub-Yellow forward MFE before decaying to `2024-12-09 l=5130`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L90_C24_365270_20240320_STAGE2_FALSE_POSITIVE_VASCULAR_EVENT","case_id":"C24_R7L90_365270_CURACLE_VASCULAR_EVENT_SPIKE","symbol":"365270","company_name":"큐라클","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"VASCULAR_THERAPEUTIC_EVENT_SPIKE_WITHOUT_PARTNER_REGULATORY_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-VascularTherapeuticTrialEventNoPartnerRegulatoryBridge","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":18630.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_vascular_therapeutic_trial_event_spike_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; vascular therapeutic trial-event spike treated as insufficient without partner validation, regulatory path, durable endpoint data and cash bridge","evidence_source_type":"historical_public_trial_event_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["trial_event_spike","vascular_therapeutic_keyword","relative_strength_spike"],"stage3_evidence_fields":["endpoint_durability_missing","partner_validation_missing","regulatory_path_missing","cash_runway_missing"],"stage4b_evidence_fields":["price_only_local_MFE","partner_regulatory_bridge_missing_watch","extreme_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/365/365270/2024.csv","profile_path":"atlas/symbol_profiles/365/365270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.60,"MFE_90D_pct":14.60,"MFE_180D_pct":14.60,"MAE_30D_pct":-22.17,"MAE_90D_pct":-55.88,"MAE_180D_pct":-72.46,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":21350.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":5130.0,"drawdown_after_peak_pct":-75.97,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"vascular_trial_event_without_partner_regulatory_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","partner_regulatory_bridge_missing_watch","extreme_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE_extreme_MAE_no_regulatory_bridge","current_profile_verdict":"current_profile_false_positive_if_trial_event_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"2024_window_clean; 2025_candidate_outside_window","same_entry_group_id":"365270_2024-03-20_18630","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C24 should not promote trial-event price spikes unless endpoint durability, partner validation, regulatory path, commercial probability and cash runway are repaired. Sub-Yellow MFE and extreme MAE force 4B-watch."}
```

### 6.3 256840 한국비엔씨 — therapeutic event momentum without regulatory/commercial bridge

Entry row: `2024-03-20 c=7960`, after event momentum accelerated.  
Observed path had local MFE, then decayed to `2024-12-09 l=3575`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L90_C24_256840_20240320_STAGE2_FALSE_POSITIVE_THERAPEUTIC_EVENT","case_id":"C24_R7L90_256840_KOREA_BNC_THERAPEUTIC_EVENT_MOMENTUM","symbol":"256840","company_name":"한국비엔씨","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"THERAPEUTIC_EVENT_MOMENTUM_WITHOUT_REGULATORY_COMMERCIAL_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate;price_only_event_stress_test","trigger_type":"Stage2-FalsePositive-TherapeuticEventMomentumNoRegulatoryCommercialBridge","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":7960.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_therapeutic_event_momentum_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; therapeutic event momentum treated as insufficient without regulatory pathway, partner validation, commercial probability and cash runway bridge","evidence_source_type":"historical_public_trial_event_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["therapeutic_event_momentum","relative_strength_spike"],"stage3_evidence_fields":["regulatory_path_missing","partner_validation_missing","commercial_probability_missing","cash_runway_missing"],"stage4b_evidence_fields":["price_only_local_MFE","commercial_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/256/256840/2024.csv","profile_path":"atlas/symbol_profiles/256/256840.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.22,"MFE_90D_pct":18.22,"MFE_180D_pct":18.22,"MAE_30D_pct":-23.37,"MAE_90D_pct":-26.38,"MAE_180D_pct":-55.09,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-21","peak_price":9410.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":3575.0,"drawdown_after_peak_pct":-62.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"therapeutic_event_momentum_without_regulatory_commercial_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","regulatory_commercial_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_local_MFE_deep_MAE_no_commercial_bridge","current_profile_verdict":"current_profile_false_positive_if_therapeutic_event_momentum_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_SPAC_and_candidate_pre_2024; selected_window_clean","same_entry_group_id":"256840_2024-03-20_7960","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C24 should not count therapeutic event momentum as positive unless regulatory pathway, partner validation, commercial probability and cash runway evidence are exact-repaired. Local MFE with deep MAE remains 4B-watch."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C24_R7L90_237690_STPHARM_RNA_PLATFORM_BRIDGE","trigger_id":"R7L90_C24_237690_20240223_STAGE2_RNA_PLATFORM_BRIDGE","symbol":"237690","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C24 requires endpoint quality, mechanism consistency, partner validation, CMC/manufacturing readiness, regulatory path and cash runway rather than bio-event price momentum alone","raw_component_scores_before":{"endpoint_quality_score":12,"mechanism_consistency_score":11,"partner_validation_score":10,"regulatory_path_score":9,"CMC_manufacturing_score":12,"commercial_probability_score":9,"cash_runway_score":7,"relative_strength_score":14,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"endpoint_quality_score":15,"mechanism_consistency_score":13,"partner_validation_score":12,"regulatory_path_score":11,"CMC_manufacturing_score":15,"commercial_probability_score":11,"cash_runway_score":9,"relative_strength_score":15,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"RNA platform/CMC bridge plus high forward MFE supports Yellow/Green-candidate watch; exact endpoint/partner/regulatory evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C24_R7L90_365270_CURACLE_VASCULAR_EVENT_SPIKE","trigger_id":"R7L90_C24_365270_20240320_STAGE2_FALSE_POSITIVE_VASCULAR_EVENT","symbol":"365270","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"vascular therapeutic event spike without endpoint durability and partner/regulatory bridge should be blocked","raw_component_scores_before":{"endpoint_quality_score":3,"mechanism_consistency_score":3,"partner_validation_score":0,"regulatory_path_score":1,"CMC_manufacturing_score":0,"commercial_probability_score":1,"cash_runway_score":1,"relative_strength_score":12,"valuation_repricing_score":4,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"endpoint_quality_score":1,"mechanism_consistency_score":1,"partner_validation_score":0,"regulatory_path_score":0,"CMC_manufacturing_score":0,"commercial_probability_score":0,"cash_runway_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-28,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Sub-Yellow MFE and extreme MAE convert the trial-event spike into missing partner/regulatory/cash bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C24_R7L90_256840_KOREA_BNC_THERAPEUTIC_EVENT_MOMENTUM","trigger_id":"R7L90_C24_256840_20240320_STAGE2_FALSE_POSITIVE_THERAPEUTIC_EVENT","symbol":"256840","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_scope":"current_default_proxy","profile_hypothesis":"therapeutic event momentum without regulatory/commercial and cash bridge should remain Watch/4B even with local MFE","raw_component_scores_before":{"endpoint_quality_score":3,"mechanism_consistency_score":2,"partner_validation_score":0,"regulatory_path_score":1,"CMC_manufacturing_score":0,"commercial_probability_score":0,"cash_runway_score":0,"relative_strength_score":13,"valuation_repricing_score":5,"execution_risk_score":-16,"theme_spike_risk":-20,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"endpoint_quality_score":1,"mechanism_consistency_score":1,"partner_validation_score":0,"regulatory_path_score":0,"CMC_manufacturing_score":0,"commercial_probability_score":0,"cash_runway_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Local MFE is price-only; deep MAE and missing regulatory/commercial bridge block Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R7L90_C24_P0_CURRENT","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C24 needs explicit endpoint, partner, regulatory, CMC, commercial and cash-runway taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":27.38,"avg_MAE90_pct":-28.73,"avg_MFE180_pct":34.67,"avg_MAE180_pct":-43.82,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.86,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C24_trial_data_partner_regulatory_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R7L90_C24_P1_SECTOR_SPECIFIC","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P1_L7_trial_data_event_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L7 bio-event signals need endpoint quality, mechanism consistency, partner validation, regulatory path, CMC readiness or cash runway before Stage2-Actionable","changed_axes":["endpoint_quality_required","partner_regulatory_required","cash_runway_required"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_endpoint_mechanism_partner_regulatory_CMC_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":27.38,"avg_MAE90_pct":-28.73,"avg_MFE180_pct":34.67,"avg_MAE180_pct":-43.82,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R7L90_C24_P2_CANONICAL","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P2_C24_trial_data_partner_regulatory_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C24 should reward data-to-regulatory/partner mechanics, not bio-event price labels","changed_axes":["C24_trial_data_partner_regulatory_bridge_required","C24_event_spike_local_4B_guard","C24_price_only_MFE_not_trial_validation_guard"],"changed_thresholds":{"stage2_yellow_gate":"endpoint_or_mechanism_plus_partner_or_regulatory_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":27.38,"avg_MAE90_pct":-28.73,"avg_MFE180_pct":34.67,"avg_MAE180_pct":-43.82,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R7L90_C24_P3_COUNTEREXAMPLE_GUARD","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","profile_id":"P3_C24_sub20_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If partner/regulatory/cash bridge is missing, MFE90<20 or MAE90<=-20 should block Yellow/Green; MAE180<=-50 hard-routes to 4B-watch","changed_axes":["C24_sub20_MFE_guardrail","C24_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_20_or_MAE90_le_minus_20); hard_watch_if_MAE180_le_minus_50"},"eligible_trigger_count":3,"avg_MFE90_pct":27.38,"avg_MAE90_pct":-28.73,"avg_MFE180_pct":34.67,"avg_MAE180_pct":-43.82,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_RNA_PLATFORM_POSITIVE_VS_VASCULAR_THERAPEUTIC_EVENT_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":27.38,"avg_MAE90_pct":-28.73,"avg_MFE180_pct":34.67,"avg_MAE180_pct":-43.82,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE90_le_minus20":0.67,"interpretation":"C24 needs bridge discipline. 에스티팜 shows RNA/platform plus CMC/manufacturing bridge can support Yellow/Green-candidate-watch, while 큐라클 and 한국비엔씨 show bio-event price momentum should not be promoted without endpoint durability, partner validation, regulatory pathway, commercial probability and cash-runway evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"237690","trigger_type":"Stage2-Actionable-RNAPlatformTrialDataManufacturingBridge-Positive","entry_date":"2024-02-23","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_platform_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when trial-event strength is tied to endpoint quality, partner/regulatory path, CMC and cash bridge; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"365270","trigger_type":"Stage2-FalsePositive-VascularTherapeuticTrialEventNoPartnerRegulatoryBridge","entry_date":"2024-03-20","stage2_to_90D_outcome":"bad_stage2_sub_Yellow_MFE_deep_MAE","stage2_to_180D_outcome":"failed_vascular_trial_event_extreme_MAE","MFE90_ge20":false,"MAE180_le_minus50":true,"transition_note":"Trial-event spike without partner/regulatory/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"256840","trigger_type":"Stage2-FalsePositive-TherapeuticEventMomentumNoRegulatoryCommercialBridge","entry_date":"2024-03-20","stage2_to_90D_outcome":"price_only_local_MFE_deep_MAE","stage2_to_180D_outcome":"failed_therapeutic_event_momentum_deep_MAE","MFE90_ge20":false,"MAE180_le_minus50":true,"transition_note":"Therapeutic event momentum without regulatory/commercial/cash bridge should be treated as 4B-watch, not positive C24 evidence."}
{"row_type":"residual_contribution","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","residual_type":"bio_event_price_momentum_overcredit_without_trial_data_partner_regulatory_cash_bridge","contribution":"Adds two C24 4B counterexamples against one RNA/platform bridge positive, avoiding C24 top-covered and recent R7 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"RNA_PLATFORM_TRIAL_DATA_MANUFACTURING_BRIDGE_VS_VASCULAR_THERAPEUTIC_EVENT_PRICE_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C24 now has non-top-symbol RNA/platform/CMC positive and two event-spike weak-bridge counterexamples; next R7 C24 loops should exact-URL repair endpoint quality, sample/statistical clarity, safety, mechanism, partner validation, regulatory pathway, CMC readiness, commercial probability and cash-runway evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"C24_trial_data_partner_regulatory_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"237690 worked when platform/data/manufacturing bridge existed; 365270 and 256840 failed when event momentum lacked partner, regulatory, commercial and cash evidence."}
{"row_type":"shadow_weight","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"C24_event_spike_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"365270 and 256840 show sub-20 MFE90 and deep MAE when event-spike evidence is not connected to durable endpoint/regulatory bridge."}
{"row_type":"shadow_weight","round":"R7","loop":"90","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","axis":"C24_price_only_MFE_not_trial_validation_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"256840 shows local MFE should not validate C24 unless regulatory/commercial and cash evidence are repaired; 365270 confirms the deep-MAE failure mode."}
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
  - bio_event_price_momentum_overcredit
  - trial_event_spike_overcredit
  - partner_regulatory_bridge_missing
  - commercial_cash_bridge_missing
new_axis_proposed:
  - C24_trial_data_partner_regulatory_bridge_required_shadow_only
  - C24_event_spike_local_4B_guard_shadow_only
  - C24_price_only_MFE_not_trial_validation_guard_shadow_only
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

All selected triggers use Stock-Web tradable raw OHLC rows and clean selected 2024 entry windows.  
`365270` has a future 2025 corporate-action candidate outside the selected 2024 window; `256840` has older SPAC/name-transition and corporate-action candidates before 2024. Both selected 2024 windows remain usable for price-path residual calibration.  
The non-price evidence layer remains source-name/proxy level for all three rows.

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
   - previous R7 loop87 C24 symbols
   - previous R7 loop88 C23 symbols
   - previous R7 loop89 C25 symbols
6. If aggregate support remains stable after exact evidence URL repair, consider C24-scoped safe patch candidates:
   - C24_trial_data_partner_regulatory_bridge_required
   - C24_event_spike_local_4B_guard
   - C24_price_only_MFE_not_trial_validation_guard
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R7
completed_loop = 90
next_round = R8
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R7/L7_BIO_HEALTHCARE_MEDICAL/C24_BIO_TRIAL_DATA_EVENT_RISK.
```

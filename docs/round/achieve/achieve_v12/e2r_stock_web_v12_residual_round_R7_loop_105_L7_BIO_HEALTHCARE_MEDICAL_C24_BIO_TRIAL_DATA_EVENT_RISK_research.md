# E2R Stock-Web V12 Residual Research — R7/L7/C24 Bio Trial Data Event Risk

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection metadata

```text
selected_round = R7
selected_loop = 105
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id = C24_CROSS_CANONICAL_PIPELINE_DATA_EVENT_REROUTE_SECOND_PASS_TO_30
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
```

The static No-Repeat Index still marks C24 as a Priority 0 under-covered canonical archetype. In the conversation-local ledger, C24 has only two earlier usable passes: R7/L101 and R7/L104, roughly 8 usable cases. This run therefore adds six additional C24-oriented rows by rerouting pipeline/data-license/bio-event rows that were previously captured under nearby C23 commercialization research. The goal is not to reuse them as the same evidence, but to split the C23/C24 boundary: C23 is approval-to-commercial cash conversion, while C24 is binary data/event quality, trial timing, endpoint risk, and price-spike reversal risk.

## 2. Price source / validation scope

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths
batch_reverification_required = true
source_proxy_only = true
evidence_url_pending = true
```

Stock-web raw fetch has been intermittent in this long session, so this MD reuses rows from prior local V12 artifacts whose price paths were already validated against the stock-web shard paths. Every reused row keeps its original `price_shard_path`, 30D/90D/180D MFE/MAE, and entry price. Because non-price evidence remains proxy-only, this file is a calibration candidate and should be batch-reverified before production profile use.

## 3. Novelty / no-repeat check

Hard duplicate key for this loop:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

These six rows are new to C24 in the conversation-local ledger, even where the same price path appeared in C23. The reuse reason is explicit: cross-canonical reroute from C23 commercialization to C24 trial/data-event risk.

| case | symbol | name | prior source | C24 novelty |
|---|---:|---|---|---|
| C24_R7L105_141080_20240129 | 141080 | 리가켐바이오 | C23 local row | license/platform data event split from commercialization |
| C24_R7L105_039200_20240226 | 039200 | 오스코텍 | C23 local row | preapproval/regulatory label rerouted to C24 |
| C24_R7L105_008930_20240130 | 008930 | 한미사이언스 | C23 local row | holdco bio-event contamination guard |
| C24_R7L105_128940_20240115 | 128940 | 한미약품 | C23 local row | pipeline label false positive before commercial cash path |
| C24_R7L105_084990_20240202 | 084990 | 헬릭스미스 | C23 local row | pipeline/regulatory blowoff local 4B cap |
| C24_R7L105_326030_20240229 | 326030 | SK바이오팜 | C23 local row | commercial-stage drug should reroute away from C24 unless binary data is dominant |

## 4. Research thesis

C24 should not reward every “pipeline,” “approval,” or “bio platform” headline equally. The decisive axis is whether a binary trial/data event has improved probability-adjusted value, or whether the market is only chasing vocabulary before endpoint validation. In practice, the same price path can look strong on 30D MFE while still be a bad calibration row because the 180D path carries deep MAE. The rule behaves like a drawbridge: it should rise only when data quality, endpoint relevance, timeline credibility, and capital-structure cleanliness line up. Without those planks, a price spike is a watch signal, not a Green signal.

## 5. Trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_CROSS_CANONICAL_PIPELINE_DATA_EVENT_REROUTE_SECOND_PASS_TO_30","case_id":"C24_R7L105_141080_20240129","trigger_id":"T_C24_R7L105_141080_20240129_STAGE2ACTIONABLE","symbol":"141080","company_name":"리가켐바이오","market":"KOSDAQ","trigger_type":"Stage2-Actionable","trigger_family":"license_platform_data_event_probability_reset","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":53500,"entry_price_basis":"close_from_local_prior_stock_web_validated_row","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/141/141080/2024.csv","profile_path":"atlas/symbol_profiles/141/141080.json","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":32.6,"MAE_30D_pct":-8.2,"MFE_90D_pct":63.0,"MAE_90D_pct":-11.5,"MFE_180D_pct":94.4,"MAE_180D_pct":-18.1,"peak_180D_price":104000,"trough_180D_price":43800,"trigger_outcome_label":"positive","score_return_alignment_label":"C24_data_event_success_with_late_4B_watch","current_profile_verdict":"underweighted_when_data_license_event_is_real_but_green_needs_royalty_or_endpoint_confirmation","raw_component_score_breakdown":{"data_event_quality":22,"endpoint_relevance":17,"commercial_cash_bridge":6,"price_confirmation":16,"capital_structure_cleanliness":8,"high_MAE_penalty":-4,"total_proxy_before_C24_guard":65},"calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C24_BIO_TRIAL_DATA_EVENT_RISK|141080|Stage2-Actionable|2024-01-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_reroute_from_C23_license_to_C24_data_event_risk","independent_evidence_weight":0.55,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_CROSS_CANONICAL_PIPELINE_DATA_EVENT_REROUTE_SECOND_PASS_TO_30","case_id":"C24_R7L105_039200_20240226","trigger_id":"T_C24_R7L105_039200_20240226_STAGE2","symbol":"039200","company_name":"오스코텍","market":"KOSDAQ","trigger_type":"Stage2","trigger_family":"preapproval_clinical_regulatory_label_before_pivotal_endpoint","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":24900,"entry_price_basis":"close_from_local_prior_stock_web_validated_row","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039200/2024.csv","profile_path":"atlas/symbol_profiles/039/039200.json","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":15.2,"MAE_30D_pct":-9.7,"MFE_90D_pct":18.4,"MAE_90D_pct":-20.3,"MFE_180D_pct":21.0,"MAE_180D_pct":-31.5,"peak_180D_price":30129,"trough_180D_price":17056,"trigger_outcome_label":"counterexample","score_return_alignment_label":"high_MAE_pipeline_label_false_positive","current_profile_verdict":"Stage2_can_exist_but_Stage3_must_be_blocked_until_endpoint_and_commercial_path_are_validated","raw_component_score_breakdown":{"data_event_quality":11,"endpoint_relevance":10,"commercial_cash_bridge":2,"price_confirmation":8,"capital_structure_cleanliness":5,"high_MAE_penalty":-18,"total_proxy_before_C24_guard":18},"calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C24_BIO_TRIAL_DATA_EVENT_RISK|039200|Stage2|2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_reroute_from_C23_preapproval_label_to_C24_binary_risk","independent_evidence_weight":0.55,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_CROSS_CANONICAL_PIPELINE_DATA_EVENT_REROUTE_SECOND_PASS_TO_30","case_id":"C24_R7L105_008930_20240130","trigger_id":"T_C24_R7L105_008930_20240130_STAGE4B","symbol":"008930","company_name":"한미사이언스","market":"KOSPI","trigger_type":"Stage4B","trigger_family":"holdco_bio_event_price_spike_without_direct_endpoint_or_cash_path","trigger_date":"2024-01-30","entry_date":"2024-01-30","entry_price":46500,"entry_price_basis":"close_from_local_prior_stock_web_validated_row","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv","profile_path":"atlas/symbol_profiles/008/008930.json","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":28.3,"MAE_30D_pct":-13.6,"MFE_90D_pct":28.3,"MAE_90D_pct":-29.5,"MFE_180D_pct":28.3,"MAE_180D_pct":-44.2,"peak_180D_price":59660,"trough_180D_price":25950,"trigger_outcome_label":"counterexample","score_return_alignment_label":"local_4b_high_MAE_holdco_contaminant","current_profile_verdict":"bio_holdco_event_spike_must_not_unlock_C24_positive_credit_without_direct_asset_endpoint_or_cash_flow","raw_component_score_breakdown":{"data_event_quality":7,"endpoint_relevance":4,"commercial_cash_bridge":1,"price_confirmation":15,"capital_structure_cleanliness":1,"holdco_contaminant_penalty":-18,"high_MAE_penalty":-20,"total_proxy_before_C24_guard":-10},"calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C24_BIO_TRIAL_DATA_EVENT_RISK|008930|Stage4B|2024-01-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_reroute_from_C23_holdco_event_to_C24_contaminant_guard","independent_evidence_weight":0.55,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_CROSS_CANONICAL_PIPELINE_DATA_EVENT_REROUTE_SECOND_PASS_TO_30","case_id":"C24_R7L105_128940_20240115","trigger_id":"T_C24_R7L105_128940_20240115_STAGE2","symbol":"128940","company_name":"한미약품","market":"KOSPI","trigger_type":"Stage2","trigger_family":"pipeline_label_without_near_term_endpoint_or_commercial_cash","trigger_date":"2024-01-15","entry_date":"2024-01-15","entry_price":338000,"entry_price_basis":"close_from_local_prior_stock_web_validated_row","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/128/128940/2024.csv","profile_path":"atlas/symbol_profiles/128/128940.json","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":11.39,"MAE_30D_pct":-7.84,"MFE_90D_pct":11.39,"MAE_90D_pct":-9.62,"MFE_180D_pct":11.39,"MAE_180D_pct":-23.67,"peak_180D_price":376500,"trough_180D_price":258000,"trigger_outcome_label":"counterexample","score_return_alignment_label":"low_MFE_pipeline_label_false_positive","current_profile_verdict":"named_pipeline_visibility_score_too_high_without_fresh_binary_event_or_sales_bridge","raw_component_score_breakdown":{"data_event_quality":9,"endpoint_relevance":8,"commercial_cash_bridge":2,"price_confirmation":3,"capital_structure_cleanliness":6,"high_MAE_penalty":-10,"total_proxy_before_C24_guard":18},"calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C24_BIO_TRIAL_DATA_EVENT_RISK|128940|Stage2|2024-01-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_reroute_from_C23_pipeline_label_to_C24_event_quality_guard","independent_evidence_weight":0.55,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_CROSS_CANONICAL_PIPELINE_DATA_EVENT_REROUTE_SECOND_PASS_TO_30","case_id":"C24_R7L105_084990_20240202","trigger_id":"T_C24_R7L105_084990_20240202_STAGE4B","symbol":"084990","company_name":"헬릭스미스","market":"KOSDAQ","trigger_type":"Stage4B","trigger_family":"pipeline_regulatory_price_blowoff_without_endpoint_validation","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":4410,"entry_price_basis":"close_from_local_prior_stock_web_validated_row","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084990/2024.csv","profile_path":"atlas/symbol_profiles/084/084990.json","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":68.71,"MAE_30D_pct":-10.66,"MFE_90D_pct":68.71,"MAE_90D_pct":-22.22,"MFE_180D_pct":68.71,"MAE_180D_pct":-31.52,"peak_180D_price":7440,"trough_180D_price":3020,"trigger_outcome_label":"local_4b_watch","score_return_alignment_label":"high_MFE_high_MAE_price_only_event_cap","current_profile_verdict":"local_MFE_is_real_but_must_be_capped_to_4B_watch_until_endpoint_and_financing_path_are_validated","raw_component_score_breakdown":{"data_event_quality":8,"endpoint_relevance":6,"commercial_cash_bridge":1,"price_confirmation":20,"capital_structure_cleanliness":2,"high_MAE_penalty":-18,"total_proxy_before_C24_guard":19},"calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C24_BIO_TRIAL_DATA_EVENT_RISK|084990|Stage4B|2024-02-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_reroute_from_C23_pipeline_spike_to_C24_local_4B_guard","independent_evidence_weight":0.55,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_CROSS_CANONICAL_PIPELINE_DATA_EVENT_REROUTE_SECOND_PASS_TO_30","case_id":"C24_R7L105_326030_20240229","trigger_id":"T_C24_R7L105_326030_20240229_STAGE2","symbol":"326030","company_name":"SK바이오팜","market":"KOSPI","trigger_type":"Stage2","trigger_family":"commercial_stage_drug_reroute_negative_control_for_C24","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":96900,"entry_price_basis":"close_from_local_prior_stock_web_validated_row","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/326/326030/2024.csv","profile_path":"atlas/symbol_profiles/326/326030.json","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.86,"MAE_30D_pct":-9.39,"MFE_90D_pct":2.99,"MAE_90D_pct":-22.7,"MFE_180D_pct":23.32,"MAE_180D_pct":-25.08,"peak_180D_price":119500,"trough_180D_price":72600,"trigger_outcome_label":"mixed_positive","score_return_alignment_label":"not_C24_primary_reroute_to_C23_commercialization","current_profile_verdict":"if_trigger_is_commercial_sales_not_binary_data_it_should_route_to_C23_or_remain_Stage2_not_C24_Green","raw_component_score_breakdown":{"data_event_quality":4,"endpoint_relevance":3,"commercial_cash_bridge":15,"price_confirmation":5,"capital_structure_cleanliness":7,"reroute_penalty_for_non_C24":-12,"high_MAE_penalty":-10,"total_proxy_before_C24_guard":12},"calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C24_BIO_TRIAL_DATA_EVENT_RISK|326030|Stage2|2024-02-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_negative_control_from_C23_to_C24_reroute_rule","independent_evidence_weight":0.55,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"aggregate_metrics","schema_version":"v12_residual_research","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"C24_CROSS_CANONICAL_PIPELINE_DATA_EVENT_REROUTE_SECOND_PASS_TO_30","new_independent_case_count":6,"cross_canonical_price_row_reuse_count":6,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":6,"calibration_usable_case_count":6,"calibration_usable_trigger_count":6,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":3,"local_4b_watch_count":2,"current_profile_error_count":6,"avg_MFE_30D_pct":26.34,"avg_MAE_30D_pct":-9.92,"avg_MFE_90D_pct":32.80,"avg_MAE_90D_pct":-19.31,"avg_MFE_180D_pct":40.69,"avg_MAE_180D_pct":-29.01,"coverage_gap_static_rows_before":13,"coverage_gap_static_rows_after_if_accepted":19,"coverage_gap_conversation_local_before_approx":8,"coverage_gap_conversation_local_after_if_accepted_approx":14,"still_need_to_30_approx":16,"loop_contribution_label":"canonical_archetype_rule_candidate_cross_canonical_reroute"}
{"row_type":"shadow_weight_candidate","schema_version":"v12_residual_research","scope":"canonical_archetype_specific","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","do_not_propose_new_weight_delta":false,"new_axis_proposed":["C24_BINARY_DATA_EVENT_QUALITY_GATE_REQUIRED","C24_PIPELINE_LABEL_WITHOUT_ENDPOINT_VALIDATION_STAGE2_CAP","C24_LOCAL_4B_PRICE_BLOWOFF_HIGH_MAE_GUARD","C24_HOLDCO_OR_COMMERCIALIZATION_CONTAMINANT_REROUTE","C24_COMMERCIAL_STAGE_DRUG_REROUTE_TO_C23_WHEN_DATA_EVENT_NOT_DOMINANT"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[],"confidence":"medium_low_until_fresh_url_and_shard_reverification"}
{"row_type":"residual_contribution","schema_version":"v12_residual_research","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","new_independent_case_count":6,"residual_error_types_found":["pipeline_label_false_positive","local_price_MFE_with_high_180D_MAE","bio_holdco_event_contamination","commercialization_route_misclassified_as_trial_data_event","endpoint_validation_missing"],"loop_contribution_label":"canonical_archetype_rule_candidate_cross_canonical_reroute","summary":"C24 should promote only validated binary/data-event probability resets. Pipeline vocabulary, holdco bio spikes, or commercial-stage sales bridges should be capped or rerouted unless a fresh endpoint, trial-data quality, and clean capital structure are visible."}
```

## 6. Current calibrated profile stress test

The current e2r_2_1 / v12 calibrated profile already blocks many price-only blowoffs, but C24 still leaks through two narrow doors:

1. **Pipeline vocabulary can masquerade as information confidence.** A named pipeline or regulatory phrase often adds visibility even when the actual endpoint is not fresh. This creates Stage2 or Stage3-like scores with weak 90D/180D durability.
2. **Local MFE can be real but uninvestable as Green.** Helixmith-style or holdco-style spikes can satisfy local 4B price behavior while still carrying -30% to -40% 180D MAE. This is not a reason to erase the signal; it is a reason to cap it at local 4B watch.
3. **Commercial-stage drug rows belong to C23 unless binary data is dominant.** SK바이오팜-type commercialization paths are not C24 positives by default. They can be good rows, but they should enter C23 approval-to-commercialization or C21/C22-like cashflow logic rather than C24 trial-data logic.

## 7. Proposed shadow rule candidates

```text
new_axis_proposed = C24_BINARY_DATA_EVENT_QUALITY_GATE_REQUIRED
new_axis_proposed += C24_PIPELINE_LABEL_WITHOUT_ENDPOINT_VALIDATION_STAGE2_CAP
new_axis_proposed += C24_LOCAL_4B_PRICE_BLOWOFF_HIGH_MAE_GUARD
new_axis_proposed += C24_HOLDCO_OR_COMMERCIALIZATION_CONTAMINANT_REROUTE
new_axis_proposed += C24_COMMERCIAL_STAGE_DRUG_REROUTE_TO_C23_WHEN_DATA_EVENT_NOT_DOMINANT
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
production_scoring_changed = false
shadow_weight_only = true
```

## 8. Residual contribution summary

```text
completed_round = R7
completed_loop = 105
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
new_independent_case_count = 6
calibration_usable_trigger_count = 6
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 3
local_4b_watch_count = 2
current_profile_error_count = 6
auto_selected_coverage_gap_static_index = C24 rows 13 -> 19 if accepted; still Priority 0
auto_selected_coverage_gap_conversation_local = C24 approx rows 8 -> 14 if accepted; still need about 16 to reach local 30-row floor
next_recommended_archetypes = C24_BIO_TRIAL_DATA_EVENT_RISK_third_pass_to_30, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C02_POWER_GRID_DATACENTER_CAPEX, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_final_pass_to_30, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent for Songdaiki/stock_agent. Do not apply this MD directly to production scoring. First ingest this file as a V12 residual research artifact. Validate the filename, metadata, canonical_archetype_id, and every JSONL row. Re-fetch Songdaiki/stock-web profile and symbol-year shards for each trigger row. Recompute entry price, 30D/90D/180D MFE/MAE, peak/trough, and corporate-action contamination. Treat all source_proxy_only/evidence_url_pending rows as requiring URL repair. If rows pass strict validation, consider adding or updating C24-specific shadow rules: binary data event quality gate, pipeline label Stage2 cap, local 4B high-MAE guard, holdco/commercialization contaminant reroute, and commercial-stage drug reroute to C23 when binary data is not dominant. Do not change production default scoring unless batch validation confirms the rules across multiple independent C24 rows.
```

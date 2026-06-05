# E2R Stock-Web v12 Residual Research — R7 Loop 85 / L7 / C23

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R7
loop: 85
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_THEME_NO_REVENUE_CONVERSION
sector: bio / healthcare / regulatory approval / commercialization
output_file: e2r_stock_web_v12_residual_round_R7_loop_85_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R6 loop 85`.

```text
scheduled_round = R7
scheduled_loop = 85
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

R7 is restricted to bio / healthcare / medical.  
C23 is selected because the previous R7 loop used C24 trial/data-event risk, while C23 still needs a better split between true regulatory approval-to-commercialization bridge and approval/regulatory theme spikes that never convert into revenue, partner quality, shipment, reimbursement, or margin.

The No-Repeat Index shows C23 as:

```text
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
rows = 26
symbols = 14
good/bad Stage2 = 8/5
4B/4C = 0/2
top-covered = UNKNOWN_SYMBOL, 028300, 000100, 039200, 195940, 003850
```

This loop avoids those top-covered symbols and introduces three different symbols:

```text
145020, 302440, 086900
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"145020","company_name":"휴젤","profile_path":"atlas/symbol_profiles/145/145020.json","first_date":"2015-12-24","last_date":"2026-02-20","trading_day_count":2489,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2017-07-31","2020-07-08","2020-07-31"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"302440","company_name":"SK바이오사이언스","profile_path":"atlas/symbol_profiles/302/302440.json","first_date":"2021-03-18","last_date":"2026-02-20","trading_day_count":1208,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"086900","company_name":"메디톡스","profile_path":"atlas/symbol_profiles/086/086900.json","first_date":"2009-01-16","last_date":"2026-02-20","trading_day_count":4215,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"145020","trigger_type":"Stage2-Actionable-BotulinumRegulatoryApprovalCommercialBridge-Positive","entry_date":"2024-03-04","duplicate_status":"new C23 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"302440","trigger_type":"Stage2-FalsePositive-VaccineCommercializationTheme-NoRevenueBridge","entry_date":"2024-03-21","duplicate_status":"new C23 symbol/trigger/date combination outside top-covered list"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"086900","trigger_type":"Stage2-FalsePositive-BotulinumRegulatoryLegalTheme-NoCommercialMarginBridge","entry_date":"2024-06-27","duplicate_status":"new C23 symbol/trigger/date combination outside top-covered list"}
```

## 4. Research question

C23 is not “approval headline appeared.”  
A regulatory approval is only the gate opening. E2R should ask whether something actually walks through the gate: commercial launch, shipment, reimbursement, partner quality, physician/channel adoption, margin conversion, royalty/revenue visibility, and source-quality confirmation.

Residual question:

```text
Can C23 distinguish:
1. botulinum regulatory approval with commercialization bridge and strong MFE,
2. vaccine/commercialization theme where approval/commercial keywords fail to convert into revenue bridge,
3. botulinum regulatory/legal theme rebound where the legal/regulatory event does not yet prove commercial margin bridge?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C23_R7L85_145020_HUGEL_APPROVAL_COMMERCIAL_BRIDGE","symbol":"145020","company_name":"휴젤","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_REGULATORY_APPROVAL_COMMERCIALIZATION_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-BotulinumRegulatoryApprovalCommercialBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_with_tolerable_initial_MAE","current_profile_verdict":"current_profile_correct_if_commercialization_bridge_required","price_source":"Songdaiki/stock-web","notes":"Regulatory approval/commercialization proxy produced high forward MFE. Still, Green should require exact approval, launch, channel and margin evidence."}
{"row_type":"case","case_id":"C23_R7L85_302440_SKBIO_VACCINE_COMMERCIAL_THEME","symbol":"302440","company_name":"SK바이오사이언스","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"VACCINE_COMMERCIALIZATION_THEME_WITHOUT_REVENUE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-VaccineCommercializationTheme-NoRevenueBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_approval_commercial_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Vaccine/commercialization theme had tiny MFE and large forward MAE when revenue, shipment and margin bridge were missing."}
{"row_type":"case","case_id":"C23_R7L85_086900_MEDITOX_REGULATORY_LEGAL_THEME","symbol":"086900","company_name":"메디톡스","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_REGULATORY_LEGAL_THEME_WITHOUT_COMMERCIAL_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-BotulinumRegulatoryLegalTheme-NoCommercialMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_initial_MFE_then_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_regulatory_legal_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Regulatory/legal theme produced an initial tradable bounce but later deep MAE without clear commercial and margin bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 145020 휴젤 — regulatory approval to commercialization bridge positive

Entry row: `2024-03-04 c=202500`.  
Observed path: same-day high `219000`, early low `2024-03-21 l=172300`, 90D high `2024-06-11 h=262500`, and later full-window high `2024-11-07 h=326000`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L85_C23_145020_20240304_STAGE2_APPROVAL_COMMERCIAL_BRIDGE","case_id":"C23_R7L85_145020_HUGEL_APPROVAL_COMMERCIAL_BRIDGE","symbol":"145020","company_name":"휴젤","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_REGULATORY_APPROVAL_COMMERCIALIZATION_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-BotulinumRegulatoryApprovalCommercialBridge-Positive","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":202500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_botulinum_regulatory_approval_commercialization_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; regulatory approval-to-commercialization bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_disclosure_report_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["regulatory_approval_proxy","commercial_launch_route_proxy","partner_or_channel_quality_proxy","relative_strength_turn"],"stage3_evidence_fields":["shipment_or_revenue_bridge_pending","margin_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv","profile_path":"atlas/symbol_profiles/145/145020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.15,"MFE_90D_pct":29.63,"MFE_180D_pct":60.99,"MAE_30D_pct":-14.91,"MAE_90D_pct":-14.91,"MAE_180D_pct":-14.91,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-07","peak_price":326000.0,"max_drawdown_low_date":"2024-03-21","max_drawdown_low":172300.0,"drawdown_after_peak_pct":-27.30,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_with_tolerable_initial_MAE","current_profile_verdict":"current_profile_correct_if_commercialization_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"145020_2024-03-04_202500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C23 can allow Stage2/Yellow when approval is tied to commercial launch/channel/revenue bridge. Green still requires exact approval, shipment, margin and source-quality evidence."}
```

### 6.2 302440 SK바이오사이언스 — vaccine commercialization theme without revenue bridge

Entry row: `2024-03-21 c=62700`.  
Observed path: local high `2024-03-22 h=63100`, then lows `2024-06-24 l=49100` and `2024-11-15 l=43950`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L85_C23_302440_20240321_STAGE2_FALSE_POSITIVE_VACCINE_COMMERCIAL_THEME","case_id":"C23_R7L85_302440_SKBIO_VACCINE_COMMERCIAL_THEME","symbol":"302440","company_name":"SK바이오사이언스","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"VACCINE_COMMERCIALIZATION_THEME_WITHOUT_REVENUE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-VaccineCommercializationTheme-NoRevenueBridge","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":62700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_vaccine_commercialization_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; vaccine/commercialization theme treated as insufficient without revenue, shipment, partner and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["regulatory_or_commercialization_keyword_proxy","relative_strength_rebound"],"stage3_evidence_fields":["revenue_bridge_missing","shipment_visibility_missing","partner_quality_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","revenue_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/302/302440/2024.csv","profile_path":"atlas/symbol_profiles/302/302440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.64,"MFE_90D_pct":0.64,"MFE_180D_pct":0.64,"MAE_30D_pct":-9.57,"MAE_90D_pct":-21.69,"MAE_180D_pct":-29.90,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-22","peak_price":63100.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":43950.0,"drawdown_after_peak_pct":-30.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"commercialization_theme_peak_without_revenue_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","revenue_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_approval_commercial_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"302440_2024-03-21_62700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C23 should not upgrade vaccine/commercialization keyword strength without revenue and shipment bridge. Low MFE and high MAE support local 4B guard."}
```

### 6.3 086900 메디톡스 — regulatory/legal theme without commercial margin bridge

Entry row: `2024-06-27 c=158700`.  
Observed path: high `2024-07-22 h=178400`, then later lows `2024-10-22 l=164800` and `2024-12-09 l=116000`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L85_C23_086900_20240627_STAGE2_FALSE_POSITIVE_REGULATORY_LEGAL_THEME","case_id":"C23_R7L85_086900_MEDITOX_REGULATORY_LEGAL_THEME","symbol":"086900","company_name":"메디톡스","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BOTULINUM_REGULATORY_LEGAL_THEME_WITHOUT_COMMERCIAL_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-BotulinumRegulatoryLegalTheme-NoCommercialMarginBridge","trigger_date":"2024-06-27","entry_date":"2024-06-27","entry_price":158700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_botulinum_regulatory_legal_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; regulatory/legal theme treated as insufficient unless commercial launch, revenue, reimbursement/channel and margin bridge are verified","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["regulatory_legal_theme","relative_strength_rebound"],"stage3_evidence_fields":["commercial_revenue_bridge_missing","margin_bridge_missing","channel_quality_missing","source_url_pending"],"stage4b_evidence_fields":["initial_theme_peak","commercial_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086900/2024.csv","profile_path":"atlas/symbol_profiles/086/086900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.41,"MFE_90D_pct":12.41,"MFE_180D_pct":12.41,"MAE_30D_pct":-12.67,"MAE_90D_pct":-12.67,"MAE_180D_pct":-26.91,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-22","peak_price":178400.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":116000.0,"drawdown_after_peak_pct":-34.98,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"regulatory_legal_theme_bounce_without_commercial_margin_bridge_should_remain_watch","four_b_evidence_type":["price_only","commercial_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_initial_MFE_then_deep_180D_MAE","current_profile_verdict":"current_profile_false_positive_if_regulatory_legal_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"086900_2024-06-27_158700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C23 should separate legal/regulatory theme bounce from commercialization bridge. Initial MFE is not enough when 180D MAE deepens and commercial margin bridge is unverified."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_R7L85_145020_HUGEL_APPROVAL_COMMERCIAL_BRIDGE","trigger_id":"R7L85_C23_145020_20240304_STAGE2_APPROVAL_COMMERCIAL_BRIDGE","symbol":"145020","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C23 requires commercialization bridge after approval","raw_component_scores_before":{"regulatory_approval_score":17,"commercial_launch_score":13,"partner_channel_quality":12,"revenue_visibility_score":9,"margin_bridge_score":8,"relative_strength_score":13,"valuation_repricing_score":9,"execution_risk_score":-6,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"regulatory_approval_score":19,"commercial_launch_score":16,"partner_channel_quality":14,"revenue_visibility_score":11,"margin_bridge_score":10,"relative_strength_score":14,"valuation_repricing_score":10,"execution_risk_score":-5,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Approval plus commercialization bridge supports Yellow-watch; exact revenue and margin evidence still block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_R7L85_302440_SKBIO_VACCINE_COMMERCIAL_THEME","trigger_id":"R7L85_C23_302440_20240321_STAGE2_FALSE_POSITIVE_VACCINE_COMMERCIAL_THEME","symbol":"302440","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"vaccine/commercialization keyword without revenue bridge should be blocked","raw_component_scores_before":{"regulatory_approval_score":7,"commercial_launch_score":3,"partner_channel_quality":3,"revenue_visibility_score":1,"margin_bridge_score":1,"relative_strength_score":8,"valuation_repricing_score":5,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":24,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"regulatory_approval_score":3,"commercial_launch_score":0,"partner_channel_quality":1,"revenue_visibility_score":0,"margin_bridge_score":0,"relative_strength_score":3,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high MAE convert the commercialization keyword into revenue-bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C23_R7L85_086900_MEDITOX_REGULATORY_LEGAL_THEME","trigger_id":"R7L85_C23_086900_20240627_STAGE2_FALSE_POSITIVE_REGULATORY_LEGAL_THEME","symbol":"086900","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"regulatory/legal bounce without commercial margin bridge should remain Watch","raw_component_scores_before":{"regulatory_approval_score":9,"commercial_launch_score":3,"partner_channel_quality":4,"revenue_visibility_score":2,"margin_bridge_score":1,"relative_strength_score":11,"valuation_repricing_score":6,"execution_risk_score":-10,"theme_spike_risk":-10,"information_confidence":3},"weighted_score_before":35,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"regulatory_approval_score":5,"commercial_launch_score":1,"partner_channel_quality":2,"revenue_visibility_score":0,"margin_bridge_score":0,"relative_strength_score":5,"valuation_repricing_score":3,"execution_risk_score":-16,"theme_spike_risk":-16,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Watch-Blocked","component_delta_explanation":"Initial MFE cannot override missing commercial revenue and margin bridge when 180D MAE deepens."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R7L85_C23_P0_CURRENT","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C23 needs explicit approval-to-commercialization bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":14.23,"avg_MAE90_pct":-16.42,"avg_MFE180_pct":24.68,"avg_MAE180_pct":-23.91,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C23_commercialization_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R7L85_C23_P1_SECTOR_SPECIFIC","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P1_L7_regulatory_commercialization_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L7 approval/commercialization signals need revenue, launch, channel, reimbursement or margin bridge before Stage2-Actionable","changed_axes":["commercialization_bridge_required","revenue_visibility_required","approval_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_launch_revenue_channel_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":14.23,"avg_MAE90_pct":-16.42,"avg_MFE180_pct":24.68,"avg_MAE180_pct":-23.91,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R7L85_C23_P2_CANONICAL","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P2_C23_approval_to_revenue_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C23 should reward approval-to-commercialization conversion, not regulatory keyword spikes","changed_axes":["C23_commercial_revenue_bridge_required","C23_regulatory_theme_local_4B_guard","C23_margin_bridge_required_for_Yellow"],"changed_thresholds":{"stage2_yellow_gate":"approval_plus_commercialization_or_revenue_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":14.23,"avg_MAE90_pct":-16.42,"avg_MFE180_pct":24.68,"avg_MAE180_pct":-23.91,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R7L85_C23_P3_COUNTEREXAMPLE_GUARD","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P3_C23_high_MAE_or_low_MFE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<15 and MAE180<=-25 while commercialization bridge is missing, block Yellow/Green","changed_axes":["C23_high_MAE_guardrail","C23_low_MFE_no_commercial_bridge_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_15_and_MAE180_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":14.23,"avg_MAE90_pct":-16.42,"avg_MFE180_pct":24.68,"avg_MAE180_pct":-23.91,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_REGULATORY_THEME","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":14.23,"avg_MAE90_pct":-16.42,"avg_MFE180_pct":24.68,"avg_MAE180_pct":-23.91,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_15":0.67,"stage2_bad_entry_rate_MAE180_le_minus_25":0.67,"interpretation":"C23 needs bridge discipline. 145020 shows approval-to-commercialization bridge can work, while 302440 and 086900 show approval/commercial/regulatory keywords can fail without revenue, shipment, channel and margin conversion."}
{"row_type":"stage_transition_summary","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"145020","trigger_type":"Stage2-Actionable-BotulinumRegulatoryApprovalCommercialBridge-Positive","entry_date":"2024-03-04","stage2_to_90D_outcome":"good_stage2_high_MFE_with_tolerable_MAE","stage2_to_180D_outcome":"positive_approval_commercialization_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when approval is tied to commercial launch/channel/revenue bridge; Green requires exact source and margin evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"302440","trigger_type":"Stage2-FalsePositive-VaccineCommercializationTheme-NoRevenueBridge","entry_date":"2024-03-21","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_vaccine_commercial_theme","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Commercialization keyword without revenue/shipment bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"086900","trigger_type":"Stage2-FalsePositive-BotulinumRegulatoryLegalTheme-NoCommercialMarginBridge","entry_date":"2024-06-27","stage2_to_90D_outcome":"mixed_stage2_initial_MFE_but_weak_bridge","stage2_to_180D_outcome":"failed_regulatory_legal_theme_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":false,"transition_note":"Regulatory/legal rebound without commercial margin bridge should remain Watch; deep 180D MAE supports bridge guard."}
{"row_type":"residual_contribution","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","residual_type":"bio_regulatory_approval_theme_overcredit_without_commercial_revenue_margin_bridge","contribution":"Adds two C23 local 4B/weak-bridge counterexamples against one regulatory approval-to-commercialization positive, avoiding C23 top-covered symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_BRIDGE_VS_APPROVAL_THEME_NO_REVENUE_CONVERSION","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C23 now has non-top-symbol approval/commercialization bridge split; next R7 loops should exact-URL repair approval, launch, revenue, reimbursement/channel and margin evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","axis":"C23_commercial_revenue_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"145020 worked with approval-to-commercialization bridge proxy; 302440 and 086900 failed or weakened when revenue, shipment, channel and margin bridge were missing."}
{"row_type":"shadow_weight","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","axis":"C23_regulatory_keyword_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Regulatory/commercialization keywords produced low or unstable MFE without commercialization bridge; route to Watch/4B-risk."}
{"row_type":"shadow_weight","round":"R7","loop":"85","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","axis":"C23_low_MFE_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<15 and MAE180<=-25 while commercialization bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk or evidence-quality repair."}
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
  - approval_theme_overcredit
  - commercialization_keyword_no_revenue_bridge
  - regulatory_legal_theme_no_margin_bridge
  - low_MFE_or_deep_MAE_without_commercialization
new_axis_proposed:
  - C23_commercial_revenue_margin_bridge_required_shadow_only
  - C23_regulatory_keyword_local_4B_watch_guard_shadow_only
  - C23_low_MFE_high_MAE_guardrail_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C23
  - full_4b_requires_non_price_evidence within C23
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
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
3. Confirm R7 / L7 / C23 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided C23 top-covered symbols.
6. If aggregate support remains stable after exact evidence URL repair, consider C23-scoped safe patch candidates:
   - C23_commercial_revenue_margin_bridge_required
   - C23_regulatory_keyword_local_4B_watch_guard
   - C23_low_MFE_high_MAE_guardrail
7. Do not loosen Stage3-Green.
8. Do not use future MFE/MAE in runtime scoring.
9. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R7
completed_loop = 85
next_round = R8
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.
```

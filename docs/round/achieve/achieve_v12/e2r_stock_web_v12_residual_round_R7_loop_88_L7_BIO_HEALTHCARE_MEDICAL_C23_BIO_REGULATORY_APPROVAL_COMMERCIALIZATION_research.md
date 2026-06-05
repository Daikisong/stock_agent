# E2R Stock-Web v12 Residual Research — R7 Loop 88 / L7 / C23

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R7
loop: 88
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id: BIOSIMILAR_APPROVAL_COMMERCIAL_BRIDGE_VS_CLINICAL_REGULATORY_THEME_NO_REVENUE_MARGIN_BRIDGE
sector: bio / healthcare / regulatory approval / commercialization / revenue bridge
output_file: e2r_stock_web_v12_residual_round_R7_loop_88_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R6 loop 88`.

```text
scheduled_round = R7
scheduled_loop = 88
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

R7 is restricted to bio / healthcare / medical.  
C23 is selected because recent R7 loops already covered C23, C25, and C24, but C23 still needs more non-top-covered evidence on the split between true approval-to-commercialization bridge and regulatory / clinical theme rebounds that do not convert into revenue, partner quality, launch, reimbursement, shipment, or margin.

No-Repeat Index snapshot:

```text
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
rows = 26
symbols = 14
good/bad Stage2 = 8/5
4B/4C = 0/2
top-covered = UNKNOWN_SYMBOL, 028300, 000100, 039200, 195940, 003850
```

This loop avoids the C23 top-covered symbols and the recent R7 symbols:

```text
R7 loop85 C23: 145020, 302440, 086900
R7 loop86 C25: 335890, 228670, 065510
R7 loop87 C24: 196170, 206650, 950220
```

Selected symbols:

```text
000250, 019170, 095700
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"000250","company_name":"삼천당제약","profile_path":"atlas/symbol_profiles/000/000250.json","first_date":"2000-10-04","last_date":"2026-02-20","trading_day_count":6258,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2002-04-22"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists long before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"019170","company_name":"신풍제약","profile_path":"atlas/symbol_profiles/019/019170.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7734,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1997-12-06","2001-11-21","2011-05-04"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"095700","company_name":"제넥신","profile_path":"atlas/symbol_profiles/095/095700.json","first_date":"2009-09-15","last_date":"2026-02-20","trading_day_count":4047,"corporate_action_candidate_count":5,"corporate_action_candidate_dates":["2012-11-19","2016-03-02","2016-03-24","2023-01-26","2023-02-02"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; late_2024_share_count_drift_watch"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"000250","trigger_type":"Stage2-Actionable-BiosimilarApprovalCommercialPartnerBridge-Positive","entry_date":"2024-03-25","duplicate_status":"new C23 symbol/trigger/date combination outside top-covered and previous R7 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"019170","trigger_type":"Stage2-FalsePositive-ClinicalRegulatoryThemeSpike-NoCommercialRevenueBridge","entry_date":"2024-03-25","duplicate_status":"new C23 symbol/trigger/date combination outside top-covered and previous R7 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"095700","trigger_type":"Stage2-FalsePositive-PlatformClinicalTheme-NoApprovalCommercialBridge","entry_date":"2024-03-18","duplicate_status":"new C23 symbol/trigger/date combination outside top-covered and previous R7 loop symbols"}
```

## 4. Research question

C23 is not “bio stock moved on approval or clinical wording.”  
The useful signal is the approval-to-commercialization bridge: regulatory clarity, partner validation, commercial launch route, shipment or revenue bridge, reimbursement/channel quality, manufacturing readiness, margin path, and cash runway. Without that bridge, the market is reading a lab label, not an invoice.

Residual question:

```text
Can C23 distinguish:
1. biosimilar / approval / partner commercialization bridge with huge MFE but still Green-strict late drawdown,
2. clinical/regulatory theme spike where no revenue or commercialization bridge exists,
3. platform clinical theme rebound where approval, launch, partner, revenue and margin bridge are missing?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C23_R7L88_000250_SCD_BIOSIMILAR_APPROVAL_COMMERCIAL","symbol":"000250","company_name":"삼천당제약","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIOSIMILAR_APPROVAL_COMMERCIAL_PARTNER_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-BiosimilarApprovalCommercialPartnerBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_very_high_MFE_tolerable_90D_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_approval_partner_revenue_bridge_required","price_source":"Songdaiki/stock-web","notes":"Biosimilar/regulatory-commercial partner proxy produced very high forward MFE. Later 180D drawdown keeps Green strict and requires exact approval, launch, partner economics, revenue and margin evidence."}
{"row_type":"case","case_id":"C23_R7L88_019170_SHINPOONG_CLINICAL_THEME_NO_REVENUE","symbol":"019170","company_name":"신풍제약","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CLINICAL_REGULATORY_THEME_SPIKE_WITHOUT_COMMERCIAL_REVENUE_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ClinicalRegulatoryThemeSpike-NoCommercialRevenueBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_clinical_regulatory_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Clinical/regulatory theme spike had low forward MFE and high/deep MAE when approval, revenue, channel and margin bridge failed to confirm."}
{"row_type":"case","case_id":"C23_R7L88_095700_GENEXINE_PLATFORM_THEME_NO_APPROVAL_COMMERCIAL","symbol":"095700","company_name":"제넥신","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"PLATFORM_CLINICAL_THEME_WITHOUT_APPROVAL_COMMERCIAL_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PlatformClinicalTheme-NoApprovalCommercialBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_platform_clinical_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Platform/clinical theme rebound had low MFE and severe forward MAE without approval, partner, launch, revenue and margin bridge. Late share-count drift is noted as a data-quality watch but does not affect the core 90D failure."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 000250 삼천당제약 — biosimilar approval / commercialization partner bridge positive

Entry row: `2024-03-25 c=111100`.  
Observed path: `2024-03-25 h=111100`, fast repricing to `2024-04-01 h=151200`, 90D peak around `2024-07-10 h=230000`, and later low `2024-12-09 l=88200`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L88_C23_000250_20240325_STAGE2_BIOSIMILAR_APPROVAL_COMMERCIAL","case_id":"C23_R7L88_000250_SCD_BIOSIMILAR_APPROVAL_COMMERCIAL","symbol":"000250","company_name":"삼천당제약","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIOSIMILAR_APPROVAL_COMMERCIAL_PARTNER_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-BiosimilarApprovalCommercialPartnerBridge-Positive","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":111100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_biosimilar_approval_commercial_partner_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; approval-to-commercialization partner bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_disclosure_report_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["regulatory_approval_proxy","commercial_partner_proxy","launch_route_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_approval_source_pending","shipment_or_revenue_bridge_pending","reimbursement_channel_pending","margin_bridge_pending"],"stage4b_evidence_fields":["price_only_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000250/2024.csv","profile_path":"atlas/symbol_profiles/000/000250.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.09,"MFE_90D_pct":107.02,"MFE_180D_pct":107.02,"MAE_30D_pct":-14.13,"MAE_90D_pct":-14.13,"MAE_180D_pct":-20.61,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-10","peak_price":230000.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":88200.0,"drawdown_after_peak_pct":-61.65,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_price_extension_and_late_drawdown_watch; Green requires exact approval/revenue/margin bridge","four_b_evidence_type":["price_only_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_very_high_MFE_tolerable_90D_MAE_late_drawdown","current_profile_verdict":"current_profile_correct_if_approval_partner_revenue_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"000250_2024-03-25_111100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C23 can allow Stage2/Yellow when approval is tied to commercial partner, launch/revenue route, reimbursement/channel quality and margin bridge. Green remains strict because late drawdown can be large without exact evidence."}
```

### 6.2 019170 신풍제약 — clinical/regulatory theme spike without commercial revenue bridge

Entry row: `2024-03-25 c=18320`.  
Observed path: same-day high `2024-03-25 h=19850`, then lows `2024-06-13 l=11850`, `2024-07-22 l=11550`, and later `2024-12-09 l=9800`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L88_C23_019170_20240325_STAGE2_FALSE_POSITIVE_CLINICAL_THEME","case_id":"C23_R7L88_019170_SHINPOONG_CLINICAL_THEME_NO_REVENUE","symbol":"019170","company_name":"신풍제약","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"CLINICAL_REGULATORY_THEME_SPIKE_WITHOUT_COMMERCIAL_REVENUE_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-ClinicalRegulatoryThemeSpike-NoCommercialRevenueBridge","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":18320.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_clinical_regulatory_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; clinical/regulatory theme treated as insufficient without approval, partner, commercial launch, revenue and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["clinical_regulatory_theme","relative_strength_spike"],"stage3_evidence_fields":["approval_bridge_missing","commercial_revenue_bridge_missing","partner_channel_bridge_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","commercial_revenue_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/019/019170/2024.csv","profile_path":"atlas/symbol_profiles/019/019170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.35,"MFE_90D_pct":8.35,"MFE_180D_pct":8.35,"MAE_30D_pct":-27.95,"MAE_90D_pct":-36.95,"MAE_180D_pct":-46.51,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":19850.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":9800.0,"drawdown_after_peak_pct":-50.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"clinical_regulatory_theme_without_commercial_revenue_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","commercial_revenue_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_clinical_regulatory_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"019170_2024-03-25_18320","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C23 should not promote clinical/regulatory theme spikes unless approval, commercial launch, partner/channel, revenue and margin bridge are verified. Low MFE and deep MAE require 4B-watch routing."}
```

### 6.3 095700 제넥신 — platform clinical theme without approval/commercial bridge

Entry row: `2024-03-18 c=9180`.  
Observed path: same-day high `2024-03-18 h=9760`, 90D low `2024-07-05 l=2980`, and late-year path that still reflects severe drawdown from the original entry.

```jsonl
{"row_type":"trigger","trigger_id":"R7L88_C23_095700_20240318_STAGE2_FALSE_POSITIVE_PLATFORM_THEME","case_id":"C23_R7L88_095700_GENEXINE_PLATFORM_THEME_NO_APPROVAL_COMMERCIAL","symbol":"095700","company_name":"제넥신","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"PLATFORM_CLINICAL_THEME_WITHOUT_APPROVAL_COMMERCIAL_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-PlatformClinicalTheme-NoApprovalCommercialBridge","trigger_date":"2024-03-18","entry_date":"2024-03-18","entry_price":9180.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_platform_clinical_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; platform/clinical theme treated as insufficient without approval, partner validation, commercial launch, revenue and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["platform_clinical_theme","relative_strength_rebound"],"stage3_evidence_fields":["approval_bridge_missing","partner_validation_missing","commercial_launch_missing","revenue_margin_bridge_missing"],"stage4b_evidence_fields":["low_MFE_watch","approval_commercial_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095700/2024.csv","profile_path":"atlas/symbol_profiles/095/095700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.32,"MFE_90D_pct":6.32,"MFE_180D_pct":11.44,"MAE_30D_pct":-20.04,"MAE_90D_pct":-67.54,"MAE_180D_pct":-67.54,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-17","peak_price":10230.0,"max_drawdown_low_date":"2024-07-05","max_drawdown_low":2980.0,"drawdown_after_peak_pct":-70.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"platform_clinical_theme_without_approval_commercial_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","approval_commercial_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_platform_clinical_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["late_2024_share_count_drift_watch_before_patch"],"corporate_action_window_status":"clean_for_2024_entry; late_2024_share_count_drift_watch","same_entry_group_id":"095700_2024-03-18_9180","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C23 should block platform/clinical theme rebounds from Yellow/Green when approval, partner validation, commercial launch, revenue and margin bridge are missing. The 90D path already fails before any late-year noise."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C23_R7L88_000250_SCD_BIOSIMILAR_APPROVAL_COMMERCIAL","trigger_id":"R7L88_C23_000250_20240325_STAGE2_BIOSIMILAR_APPROVAL_COMMERCIAL","symbol":"000250","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C23 requires approval plus commercialization, partner, channel, revenue and margin bridge rather than approval label alone","raw_component_scores_before":{"regulatory_approval_score":16,"commercial_launch_score":13,"partner_channel_quality":14,"revenue_visibility_score":10,"reimbursement_channel_score":8,"margin_bridge_score":8,"cash_runway_score":6,"relative_strength_score":15,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable/Stage3-Yellow-Watch","raw_component_scores_after":{"regulatory_approval_score":19,"commercial_launch_score":16,"partner_channel_quality":17,"revenue_visibility_score":13,"reimbursement_channel_score":10,"margin_bridge_score":10,"cash_runway_score":7,"relative_strength_score":16,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":89,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Approval/commercial partner bridge and huge MFE support Yellow/Green-candidate watch; late drawdown and proxy-only evidence keep Green strict."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C23_R7L88_019170_SHINPOONG_CLINICAL_THEME_NO_REVENUE","trigger_id":"R7L88_C23_019170_20240325_STAGE2_FALSE_POSITIVE_CLINICAL_THEME","symbol":"019170","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"clinical/regulatory theme without approval and commercial revenue bridge should be blocked","raw_component_scores_before":{"regulatory_approval_score":5,"commercial_launch_score":1,"partner_channel_quality":1,"revenue_visibility_score":0,"reimbursement_channel_score":0,"margin_bridge_score":0,"cash_runway_score":2,"relative_strength_score":10,"valuation_repricing_score":4,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"regulatory_approval_score":1,"commercial_launch_score":0,"partner_channel_quality":0,"revenue_visibility_score":0,"reimbursement_channel_score":0,"margin_bridge_score":0,"cash_runway_score":1,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-24,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and high MAE convert the clinical/regulatory theme spike into missing commercialization bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C23_R7L88_095700_GENEXINE_PLATFORM_THEME_NO_APPROVAL_COMMERCIAL","trigger_id":"R7L88_C23_095700_20240318_STAGE2_FALSE_POSITIVE_PLATFORM_THEME","symbol":"095700","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_scope":"current_default_proxy","profile_hypothesis":"platform clinical theme without approval/commercial bridge should be 4B-watch","raw_component_scores_before":{"regulatory_approval_score":3,"commercial_launch_score":0,"partner_channel_quality":1,"revenue_visibility_score":0,"reimbursement_channel_score":0,"margin_bridge_score":0,"cash_runway_score":1,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"regulatory_approval_score":0,"commercial_launch_score":0,"partner_channel_quality":0,"revenue_visibility_score":0,"reimbursement_channel_score":0,"margin_bridge_score":0,"cash_runway_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-26,"theme_spike_risk":-24,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and extreme MAE require approval, partner, launch, revenue and margin bridge before any promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R7L88_C23_P0_CURRENT","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C23 needs exact approval/commercialization/revenue/margin bridge and clinical-theme 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":40.56,"avg_MAE90_pct":-39.54,"avg_MFE180_pct":42.27,"avg_MAE180_pct":-44.89,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.67,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C23_approval_commercial_revenue_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R7L88_C23_P1_SECTOR_SPECIFIC","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P1_L7_approval_commercial_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L7 approval/commercialization signals need approval clarity, partner validation, launch route, revenue visibility, channel/reimbursement quality or margin bridge before Stage2-Actionable","changed_axes":["approval_commercial_bridge_required","partner_revenue_required","clinical_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_approval_partner_launch_revenue_channel_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":40.56,"avg_MAE90_pct":-39.54,"avg_MFE180_pct":42.27,"avg_MAE180_pct":-44.89,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R7L88_C23_P2_CANONICAL","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P2_C23_approval_partner_revenue_margin_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C23 should reward approval-to-commercial mechanics, not clinical/regulatory price themes","changed_axes":["C23_approval_partner_revenue_bridge_required","C23_clinical_theme_local_4B_guard","C23_late_drawdown_Green_strict_guard"],"changed_thresholds":{"stage2_yellow_gate":"approval_or_partner_plus_revenue_or_margin_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":40.56,"avg_MAE90_pct":-39.54,"avg_MFE180_pct":42.27,"avg_MAE180_pct":-44.89,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R7L88_C23_P3_COUNTEREXAMPLE_GUARD","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","profile_id":"P3_C23_low_MFE_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<10 and MAE90<=-25 while approval/commercial bridge is missing, block Yellow/Green and route to 4B-watch","changed_axes":["C23_low_MFE_guardrail","C23_high_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_10_and_MAE90_le_minus_25_with_commercial_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":40.56,"avg_MAE90_pct":-39.54,"avg_MFE180_pct":42.27,"avg_MAE180_pct":-44.89,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"C23_BIOSIMILAR_APPROVAL_BRIDGE_VS_CLINICAL_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":40.56,"avg_MAE90_pct":-39.54,"avg_MFE180_pct":42.27,"avg_MAE180_pct":-44.89,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_10":0.67,"stage2_bad_entry_rate_MAE90_le_minus_25":0.67,"interpretation":"C23 needs bridge discipline. 삼천당제약 shows approval/commercial partner bridge can produce huge MFE, while 신풍제약 and 제넥신 show clinical/regulatory theme spikes should not be promoted without approval, launch, partner, revenue, channel and margin bridge."}
{"row_type":"stage_transition_summary","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"000250","trigger_type":"Stage2-Actionable-BiosimilarApprovalCommercialPartnerBridge-Positive","entry_date":"2024-03-25","stage2_to_90D_outcome":"good_stage2_very_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_approval_commercial_bridge_with_late_drawdown","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when approval is tied to commercial partner, launch route, revenue/channel and margin bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"019170","trigger_type":"Stage2-FalsePositive-ClinicalRegulatoryThemeSpike-NoCommercialRevenueBridge","entry_date":"2024-03-25","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_clinical_regulatory_theme_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Clinical/regulatory theme without commercial revenue and margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"095700","trigger_type":"Stage2-FalsePositive-PlatformClinicalTheme-NoApprovalCommercialBridge","entry_date":"2024-03-18","stage2_to_90D_outcome":"bad_stage2_low_MFE_extreme_MAE","stage2_to_180D_outcome":"failed_platform_clinical_theme_extreme_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Platform/clinical theme without approval/commercial bridge should stay Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","residual_type":"clinical_regulatory_theme_overcredit_without_approval_partner_revenue_margin_bridge","contribution":"Adds two C23 local 4B/high-MAE counterexamples against one biosimilar approval/commercial partner positive, avoiding C23 top-covered and previous R7 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","fine_archetype_id":"BIOSIMILAR_APPROVAL_COMMERCIAL_BRIDGE_VS_CLINICAL_REGULATORY_THEME_NO_REVENUE_MARGIN_BRIDGE","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C23 now has non-top-symbol biosimilar approval-commercial positive and two clinical/regulatory theme counterexamples; next R7 loops should exact-URL repair approval source, partner validation, launch/revenue route, reimbursement/channel quality, margin and cash-runway evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","axis":"C23_approval_partner_revenue_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"000250 worked when approval/commercial partner proxy was present; 019170 and 095700 failed when only clinical/regulatory or platform theme existed."}
{"row_type":"shadow_weight","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","axis":"C23_clinical_regulatory_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Clinical/regulatory theme rows showed low MFE and high/extreme MAE without commercial bridge."}
{"row_type":"shadow_weight","round":"R7","loop":"88","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","axis":"C23_late_drawdown_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"000250 was a strong positive but still had late 180D drawdown; Green should require exact approval, revenue, reimbursement/channel and margin evidence."}
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
  - clinical_regulatory_theme_overcredit
  - approval_bridge_missing
  - commercial_revenue_bridge_missing
  - partner_channel_margin_bridge_missing
new_axis_proposed:
  - C23_approval_partner_revenue_margin_bridge_required_shadow_only
  - C23_clinical_regulatory_theme_local_4B_watch_guard_shadow_only
  - C23_late_drawdown_Green_strict_guard_shadow_only
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
The non-price evidence layer remains source-name/proxy level.  
`095700` has a late-2024 share-count drift watch in the selected price path, so the 90D failure is usable, but any future production patch should exact-repair the price path and evidence URLs.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 095700 late-2024 share-count drift before patch
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
6. Keep 095700 in data-quality watch before patch consideration.
7. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C23-scoped safe patch candidates:
   - C23_approval_partner_revenue_margin_bridge_required
   - C23_clinical_regulatory_theme_local_4B_watch_guard
   - C23_late_drawdown_Green_strict_guard
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R7
completed_loop = 88
next_round = R8
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.
```

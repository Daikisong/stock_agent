# E2R Stock-Web v12 Residual Research — R7 Loop 89 / L7 / C25

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R7
loop: 89
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_CONTACT_LENS_BIOMATERIAL_REBOUND_DECAY
sector: bio / healthcare / medical device / export / reimbursement / installed base / margin bridge
output_file: e2r_stock_web_v12_residual_round_R7_loop_89_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R6 loop 89`.

```text
scheduled_round = R7
scheduled_loop = 89
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

R7 is restricted to bio / healthcare / medical.  
C25 is selected because recent R7 loops already covered:

```text
R7 loop85: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
R7 loop86: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
R7 loop87: C24_BIO_TRIAL_DATA_EVENT_RISK
R7 loop88: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

No-Repeat Index snapshot:

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
rows = 33
symbols = 16
good/bad Stage2 = 13/6
4B/4C = 3/2
top-covered = 336570, 100120, 060280, 099190, 145720, 214150
```

This loop avoids the C25 top-covered symbols and also avoids recent R7 loop symbols:

```text
R7 loop85 C23: 145020, 302440, 086900
R7 loop86 C25: 335890, 228670, 065510
R7 loop87 C24: 196170, 206650, 950220
R7 loop88 C23: 000250, 019170, 095700
```

Candidate rejection note:

```text
287410 / 제이시스메디칼 was checked but not used as representative because the 2024 path is heavily affected by tender/delisting behavior. It is useful for a C32/governance-tender row or a C25 data-quality row, but it would contaminate the pure medical-device export/reimbursement bridge in this loop.
041830 / 인바디 was checked but the selected 2024 path did not provide enough residual separation for this loop.
```

Selected symbols:

```text
200670, 119610, 290650
```

This loop tests:

```text
aesthetic medical device / injectable export-reimbursement margin bridge
vs
contact-lens export/accounting/suspension weak bridge
vs
biomaterial / regenerative-medical rebound without reimbursement, channel and margin bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"200670","company_name":"휴메딕스","profile_path":"atlas/symbol_profiles/200/200670.json","first_date":"2014-12-26","last_date":"2026-02-20","trading_day_count":2736,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"119610","company_name":"인터로조","profile_path":"atlas/symbol_profiles/119/119610.json","first_date":"2010-07-28","last_date":"2026-02-20","trading_day_count":3567,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2012-07-11","2012-08-03"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 window. The 2024 tradable shard shown to this runner ends early and is marked partial-window / suspension-accounting watch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_partial_window_data_quality_watch"}
{"row_type":"price_source_validation","symbol":"290650","company_name":"엘앤씨바이오","profile_path":"atlas/symbol_profiles/290/290650.json","first_date":"2018-11-01","last_date":"2026-02-20","trading_day_count":1793,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2020-10-12","2020-11-03"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"200670","trigger_type":"Stage2-Actionable-AestheticMedicalDeviceExportReimbursementMarginBridge-Positive","entry_date":"2024-03-25","duplicate_status":"new C25 symbol/trigger/date combination outside top-covered and previous R7 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"119610","trigger_type":"Stage2-FalsePositive-ContactLensExportThemeNoAccountingReimbursementBridge","entry_date":"2024-01-31","duplicate_status":"new C25 symbol/trigger/date combination outside top-covered and previous R7 loop symbols; partial-window data-quality watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"290650","trigger_type":"Stage2-FalsePositive-BiomaterialReboundNoReimbursementChannelMarginBridge","entry_date":"2024-01-02","duplicate_status":"new C25 symbol/trigger/date combination outside top-covered and previous R7 loop symbols"}
```

## 4. Research question

C25 is not “의료기기나 헬스케어 주가가 움직였다.”  
The useful C25 signal needs a conversion bridge: overseas channel quality, installed-base growth, distributor sell-through, reimbursement or regulatory-market access, consumable pull-through, ASP/mix, gross-margin durability, collection discipline and cash conversion. A medical device can be placed in the clinic, but E2R needs to know whether the clinic keeps using it, pays for it, and orders the profitable consumables.

Residual question:

```text
Can C25 distinguish:
1. aesthetic / injectable medical-device export-reimbursement margin bridge with high MFE and tolerable MAE,
2. contact-lens export theme where accounting/suspension and weak reimbursement evidence break the bridge,
3. biomaterial/regenerative-medical rebound where no reimbursement, channel quality, utilization, margin or cash bridge is confirmed?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C25_R7L89_200670_HUMEDIX_AESTHETIC_EXPORT_MARGIN","symbol":"200670","company_name":"휴메딕스","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-AestheticMedicalDeviceExportReimbursementMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_MFE90_ge25_MFE180_ge55_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_export_reimbursement_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Aesthetic/injectable medical-device export and margin proxy produced high 90D and 180D MFE with controlled early MAE. Green still requires exact export channel, reimbursement/market access, gross-margin and cash evidence."}
{"row_type":"case","case_id":"C25_R7L89_119610_INTEROJO_CONTACT_LENS_WEAK_BRIDGE","symbol":"119610","company_name":"인터로조","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"CONTACT_LENS_EXPORT_THEME_WITHOUT_ACCOUNTING_REIMBURSEMENT_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ContactLensExportThemeNoAccountingReimbursementBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"score_price_alignment":"counterexample_sub_Yellow_MFE_partial_window_deep_MAE_data_quality_watch","current_profile_verdict":"current_profile_false_positive_if_contact_lens_export_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Contact-lens export theme produced sub-Yellow MFE and meaningful drawdown before the shard becomes partial-window. Accounting/suspension and reimbursement/channel uncertainty must block Yellow/Green."}
{"row_type":"case","case_id":"C25_R7L89_290650_LNC_BIO_BIOMATERIAL_REBOUND","symbol":"290650","company_name":"엘앤씨바이오","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"BIOMATERIAL_REBOUND_WITHOUT_REIMBURSEMENT_CHANNEL_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-BiomaterialReboundNoReimbursementChannelMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_biomaterial_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Biomaterial/regenerative-medical rebound had near-zero MFE and deep MAE without reimbursement, distributor channel, utilization, gross-margin or cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 200670 휴메딕스 — aesthetic medical device / injectable export-reimbursement margin bridge

Entry row: `2024-03-25 c=29700`.  
Observed path: early low `2024-04-03 l=27500`, 90D high `2024-06-03 h=37200`, and full-window high `2024-12-23 h=46200`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L89_C25_200670_20240325_STAGE2_AESTHETIC_EXPORT_MARGIN","case_id":"C25_R7L89_200670_HUMEDIX_AESTHETIC_EXPORT_MARGIN","symbol":"200670","company_name":"휴메딕스","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-AestheticMedicalDeviceExportReimbursementMarginBridge-Positive","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":29700.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_aesthetic_medical_device_export_reimbursement_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; aesthetic medical-device/injectable export channel, reimbursement/market access and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["export_channel_proxy","installed_base_or_consumable_pullthrough_proxy","reimbursement_market_access_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_export_channel_pending","reimbursement_or_market_access_source_pending","gross_margin_mix_pending","cash_collection_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/200/200670/2024.csv","profile_path":"atlas/symbol_profiles/200/200670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.54,"MFE_90D_pct":25.25,"MFE_180D_pct":55.56,"MAE_30D_pct":-7.41,"MAE_90D_pct":-7.41,"MAE_180D_pct":-14.14,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-23","peak_price":46200.0,"max_drawdown_low_date":"2024-11-14","max_drawdown_low":25500.0,"drawdown_after_peak_pct":-9.20,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_export_reimbursement_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_MFE90_ge25_MFE180_ge55_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_export_reimbursement_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"200670_2024-03-25_29700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C25 can allow Stage2/Yellow when medical-device strength is tied to overseas channel quality, installed-base or consumable pull-through, reimbursement/market access, margin mix and cash collection. Green requires exact source-grade evidence."}
```

### 6.2 119610 인터로조 — contact-lens export theme without accounting/reimbursement bridge

Entry row: `2024-01-31 c=29400`.  
Observed path: high `2024-03-19 h=34550`, later partial-window low `2024-04-05 l=23300`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L89_C25_119610_20240131_STAGE2_FALSE_POSITIVE_CONTACT_LENS_WEAK_BRIDGE","case_id":"C25_R7L89_119610_INTEROJO_CONTACT_LENS_WEAK_BRIDGE","symbol":"119610","company_name":"인터로조","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"CONTACT_LENS_EXPORT_THEME_WITHOUT_ACCOUNTING_REIMBURSEMENT_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-ContactLensExportThemeNoAccountingReimbursementBridge","trigger_date":"2024-01-31","entry_date":"2024-01-31","entry_price":29400.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_contact_lens_export_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; contact-lens export theme treated as insufficient without clean accounting, distributor sell-through, reimbursement/market access, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["contact_lens_export_theme","relative_strength_rebound"],"stage3_evidence_fields":["clean_accounting_bridge_missing","distributor_sellthrough_missing","reimbursement_market_access_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["partial_window_watch","accounting_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/119/119610/2024.csv","profile_path":"atlas/symbol_profiles/119/119610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.46,"MFE_90D_pct":17.52,"MFE_180D_pct":17.52,"MAE_30D_pct":-3.40,"MAE_90D_pct":-20.75,"MAE_180D_pct":-20.75,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-19","peak_price":34550.0,"max_drawdown_low_date":"2024-04-05","max_drawdown_low":23300.0,"drawdown_after_peak_pct":-32.56,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"contact_lens_export_theme_without_clean_accounting_reimbursement_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["partial_window_watch","accounting_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub_Yellow_MFE_partial_window_deep_MAE_data_quality_watch","current_profile_verdict":"current_profile_false_positive_if_contact_lens_export_theme_overcredited","calibration_usable":true,"forward_window_trading_days":"partial_2024_window_only","calibration_block_reasons":["partial_window_data_quality_watch","accounting_or_suspension_watch_before_patch"],"corporate_action_window_status":"historical_candidates_pre_2024; 2024_partial_window_watch","same_entry_group_id":"119610_2024-01-31_29400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.75,"do_not_count_as_new_case":false,"current_profile_residual":"C25 should not promote contact-lens export strength when clean accounting, distributor sell-through, reimbursement/market access, margin and cash bridge are missing. Partial-window status requires data-quality watch before any patch."}
```

### 6.3 290650 엘앤씨바이오 — biomaterial rebound without reimbursement/channel/margin bridge

Entry row: `2024-01-02 c=29150`.  
Observed path: same-day high `2024-01-02 h=29500`, early low `2024-04-08 l=20200`, and late low `2024-11-14 l=15240`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L89_C25_290650_20240102_STAGE2_FALSE_POSITIVE_BIOMATERIAL_REBOUND","case_id":"C25_R7L89_290650_LNC_BIO_BIOMATERIAL_REBOUND","symbol":"290650","company_name":"엘앤씨바이오","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"BIOMATERIAL_REBOUND_WITHOUT_REIMBURSEMENT_CHANNEL_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-BiomaterialReboundNoReimbursementChannelMarginBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":29150.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_biomaterial_regenerative_medical_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; biomaterial/regenerative-medical rebound treated as insufficient without reimbursement, distributor channel, hospital utilization, gross-margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["biomaterial_rebound_theme","regenerative_medical_keyword"],"stage3_evidence_fields":["reimbursement_bridge_missing","hospital_channel_utilization_missing","gross_margin_bridge_missing","cash_conversion_missing"],"stage4b_evidence_fields":["price_only_local_peak","reimbursement_margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/290/290650/2024.csv","profile_path":"atlas/symbol_profiles/290/290650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.20,"MFE_90D_pct":1.20,"MFE_180D_pct":1.20,"MAE_30D_pct":-20.24,"MAE_90D_pct":-30.70,"MAE_180D_pct":-47.72,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":29500.0,"max_drawdown_low_date":"2024-11-14","max_drawdown_low":15240.0,"drawdown_after_peak_pct":-48.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"biomaterial_rebound_without_reimbursement_channel_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","reimbursement_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive_if_biomaterial_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"290650_2024-01-02_29150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C25 should not promote biomaterial/regenerative-medical rebound without reimbursement, hospital-channel utilization, distributor quality, gross-margin and cash-conversion bridge. Near-zero MFE and deep MAE force 4B-watch."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C25_R7L89_200670_HUMEDIX_AESTHETIC_EXPORT_MARGIN","trigger_id":"R7L89_C25_200670_20240325_STAGE2_AESTHETIC_EXPORT_MARGIN","symbol":"200670","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C25 requires export channel, reimbursement/market access, installed-base/consumable pull-through, margin and cash bridge rather than medical-device theme alone","raw_component_scores_before":{"export_channel_score":13,"reimbursement_market_access_score":11,"installed_base_score":10,"consumable_pullthrough_score":10,"gross_margin_score":10,"cash_collection_score":7,"relative_strength_score":12,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"export_channel_score":16,"reimbursement_market_access_score":14,"installed_base_score":13,"consumable_pullthrough_score":12,"gross_margin_score":13,"cash_collection_score":9,"relative_strength_score":13,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Export/reimbursement/margin bridge plus high 90D/180D MFE supports Yellow-watch; exact evidence still blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C25_R7L89_119610_INTEROJO_CONTACT_LENS_WEAK_BRIDGE","trigger_id":"R7L89_C25_119610_20240131_STAGE2_FALSE_POSITIVE_CONTACT_LENS_WEAK_BRIDGE","symbol":"119610","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_scope":"current_default_proxy","profile_hypothesis":"contact-lens export theme without clean accounting and reimbursement bridge should be blocked","raw_component_scores_before":{"export_channel_score":4,"reimbursement_market_access_score":1,"installed_base_score":2,"consumable_pullthrough_score":1,"gross_margin_score":1,"cash_collection_score":0,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-18,"theme_spike_risk":-14,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_channel_score":1,"reimbursement_market_access_score":0,"installed_base_score":0,"consumable_pullthrough_score":0,"gross_margin_score":0,"cash_collection_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-28,"theme_spike_risk":-20,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Sub-Yellow MFE, deep MAE and partial-window/accounting watch convert contact-lens export theme into weak bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C25_R7L89_290650_LNC_BIO_BIOMATERIAL_REBOUND","trigger_id":"R7L89_C25_290650_20240102_STAGE2_FALSE_POSITIVE_BIOMATERIAL_REBOUND","symbol":"290650","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_scope":"current_default_proxy","profile_hypothesis":"biomaterial rebound without reimbursement/channel/margin bridge should remain Watch/blocked","raw_component_scores_before":{"export_channel_score":1,"reimbursement_market_access_score":0,"installed_base_score":1,"consumable_pullthrough_score":0,"gross_margin_score":0,"cash_collection_score":0,"relative_strength_score":2,"valuation_repricing_score":1,"execution_risk_score":-16,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_channel_score":0,"reimbursement_market_access_score":0,"installed_base_score":0,"consumable_pullthrough_score":0,"gross_margin_score":0,"cash_collection_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE require reimbursement, channel, utilization, margin and cash bridge before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R7L89_C25_P0_CURRENT","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C25 needs explicit export-channel/reimbursement/installed-base/margin/cash and data-quality taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":14.66,"avg_MAE90_pct":-19.62,"avg_MFE180_pct":24.76,"avg_MAE180_pct":-27.54,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.67,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C25_export_reimbursement_margin_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R7L89_C25_P1_SECTOR_SPECIFIC","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_id":"P1_L7_medical_device_export_reimbursement_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L7 medical-device signals need export distributor quality, reimbursement/market access, installed-base, consumable pull-through, margin or cash collection before Stage2-Actionable","changed_axes":["export_channel_required","reimbursement_margin_required","device_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_export_channel_reimbursement_installed_base_consumable_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":14.66,"avg_MAE90_pct":-19.62,"avg_MFE180_pct":24.76,"avg_MAE180_pct":-27.54,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R7L89_C25_P2_CANONICAL","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_id":"P2_C25_export_reimbursement_margin_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C25 should reward export/reimbursement-to-margin mechanics, not contact-lens or biomaterial rebound labels","changed_axes":["C25_export_reimbursement_margin_bridge_required","C25_contact_lens_biomaterial_theme_local_4B_guard","C25_partial_window_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"export_channel_or_reimbursement_plus_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":14.66,"avg_MAE90_pct":-19.62,"avg_MFE180_pct":24.76,"avg_MAE180_pct":-27.54,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R7L89_C25_P3_COUNTEREXAMPLE_GUARD","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_id":"P3_C25_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<20 and MAE90<=-20 while reimbursement/channel/margin bridge is missing, block Yellow/Green and route to 4B-watch; partial-window rows require data-quality watch","changed_axes":["C25_low_MFE_guardrail","C25_deep_MAE_4B_guardrail","C25_partial_window_watch_guardrail"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_20_and_MAE90_le_minus_20_with_bridge_missing"},"eligible_trigger_count":3,"avg_MFE90_pct":14.66,"avg_MAE90_pct":-19.62,"avg_MFE180_pct":24.76,"avg_MAE180_pct":-27.54,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DEVICE_POSITIVE_VS_CONTACT_LENS_BIOMATERIAL_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":14.66,"avg_MAE90_pct":-19.62,"avg_MFE180_pct":24.76,"avg_MAE180_pct":-27.54,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"partial_window_data_quality_watch_count":1,"interpretation":"C25 needs bridge discipline. 휴메딕스 shows aesthetic medical-device/export-reimbursement margin bridge can support Yellow-watch, while 인터로조 and 엘앤씨바이오 show contact-lens/biomaterial rebounds should not be promoted without clean accounting, reimbursement, channel, utilization, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"200670","trigger_type":"Stage2-Actionable-AestheticMedicalDeviceExportReimbursementMarginBridge-Positive","entry_date":"2024-03-25","stage2_to_90D_outcome":"good_stage2_MFE90_ge25_tolerable_MAE","stage2_to_180D_outcome":"positive_export_reimbursement_margin_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when export channel, reimbursement/market access, installed-base or consumable pull-through and margin bridge exists; Green requires exact source-grade evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"119610","trigger_type":"Stage2-FalsePositive-ContactLensExportThemeNoAccountingReimbursementBridge","entry_date":"2024-01-31","stage2_to_90D_outcome":"bad_stage2_sub_Yellow_MFE_partial_window_deep_MAE","stage2_to_180D_outcome":"partial_window_data_quality_watch","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Contact-lens export theme without clean accounting/reimbursement/margin bridge should stay Watch/4B-risk and data-quality-watch."}
{"row_type":"stage_transition_summary","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"290650","trigger_type":"Stage2-FalsePositive-BiomaterialReboundNoReimbursementChannelMarginBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE","stage2_to_180D_outcome":"failed_biomaterial_rebound_deep_MAE","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Biomaterial/rebound without reimbursement/channel/margin bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","residual_type":"medical_device_contact_lens_biomaterial_rebound_overcredit_without_export_reimbursement_margin_bridge","contribution":"Adds two C25 local 4B/deep-MAE counterexamples against one aesthetic medical-device export/margin positive, avoiding C25 top-covered and previous R7 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_MARGIN_BRIDGE_VS_CONTACT_LENS_BIOMATERIAL_REBOUND_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C25 now has non-top-symbol aesthetic medical-device positive and two contact-lens/biomaterial weak-bridge counterexamples; next R7 loops should exact-URL repair export distributor quality, reimbursement/market access, installed-base, consumable pull-through, gross margin and cash collection evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","axis":"C25_export_reimbursement_margin_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"200670 worked when export/reimbursement/margin proxy existed; 119610 and 290650 failed or became weak when clean accounting, reimbursement, channel and margin bridges were missing."}
{"row_type":"shadow_weight","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","axis":"C25_contact_lens_biomaterial_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Contact-lens and biomaterial rows showed sub-20 MFE90 and MAE90<=-20 without non-price bridge."}
{"row_type":"shadow_weight","round":"R7","loop":"89","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","axis":"C25_partial_window_data_quality_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"119610 requires partial-window / accounting-suspension watch before any production consideration."}
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
  - medical_device_theme_overcredit
  - contact_lens_export_theme_overcredit
  - biomaterial_rebound_overcredit
  - reimbursement_channel_margin_bridge_missing
new_axis_proposed:
  - C25_export_reimbursement_margin_bridge_required_shadow_only
  - C25_contact_lens_biomaterial_theme_local_4B_watch_guard_shadow_only
  - C25_partial_window_data_quality_watch_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C25
  - full_4b_requires_non_price_evidence within C25
  - hard_4c_thesis_break_routes_to_4c within C25
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
`119610` is usable as a weak-bridge / data-quality-watch counterexample, but it must be exact-repaired before any production patch because the 2024 shown shard is partial and the business evidence layer needs clean accounting / suspension-context repair.  
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 119610 partial-window/accounting-suspension watch
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
3. Confirm R7 / L7 / C25 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C25 top-covered symbols
   - previous R7 loop85 C23 symbols
   - previous R7 loop86 C25 symbols
   - previous R7 loop87 C24 symbols
   - previous R7 loop88 C23 symbols
6. Confirm 287410 and 041830 were not used as representative rows for the reasons documented in this MD.
7. Keep 119610 in data-quality watch before patch consideration.
8. If aggregate support remains stable after exact evidence URL and data-quality repair, consider C25-scoped safe patch candidates:
   - C25_export_reimbursement_margin_bridge_required
   - C25_contact_lens_biomaterial_theme_local_4B_watch_guard
   - C25_partial_window_data_quality_watch_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R7
completed_loop = 89
next_round = R8
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.
```

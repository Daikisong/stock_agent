# E2R Stock-Web v12 Residual Research — R7 Loop 86 / L7 / C25

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R7
loop: 86
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DENTAL_OPHTHALMIC_DEVICE_EXPORT_THEME_DECAY
sector: bio / healthcare / medical device / export / reimbursement
output_file: e2r_stock_web_v12_residual_round_R7_loop_86_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R6 loop 86`.

```text
scheduled_round = R7
scheduled_loop = 86
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

R7 is restricted to bio / healthcare / medical.  
C25 is selected because the previous R7 loop used C23 approval/commercialization, while C25 still needs a cleaner split between true medical-device export/reimbursement/channel bridge and device-theme rebound without durable export, procedure-volume, reimbursement, distributor, or margin confirmation.

The No-Repeat Index shows C25 as:

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
rows = 33
symbols = 16
good/bad Stage2 = 13/6
4B/4C = 3/2
top-covered = 336570, 100120, 060280, 099190, 145720, 214150
```

This loop avoids those top-covered symbols and also avoids the immediately previous R7 loop85 C23 symbols:

```text
145020, 302440, 086900
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"335890","company_name":"비올","profile_path":"atlas/symbol_profiles/335/335890.json","first_date":"2019-12-03","last_date":"2025-12-09","trading_day_count":1399,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2020-11-26"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidate exists before the 2024 forward window used here. Status is inferred inactive_or_delisted_like after 2025, but the 2024 selected window is tradable and clean.","status_inferred":"inactive_or_delisted_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"228670","company_name":"레이","profile_path":"atlas/symbol_profiles/228/228670.json","first_date":"2019-08-08","last_date":"2026-02-20","trading_day_count":1603,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2021-06-03","2021-06-23"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"065510","company_name":"휴비츠","profile_path":"atlas/symbol_profiles/065/065510.json","first_date":"2003-10-31","last_date":"2026-02-20","trading_day_count":5506,"corporate_action_candidate_count":2,"corporate_action_candidate_dates":["2004-04-22","2004-05-21"],"has_major_raw_discontinuity":true,"calibration_caveat":"Corporate-action candidates exist before the 2024 forward window used here.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"335890","trigger_type":"Stage2-Actionable-AestheticDeviceExportChannelMarginBridge-Positive","entry_date":"2024-02-16","duplicate_status":"new C25 symbol/trigger/date combination outside top-covered list and previous R7 loop85 C23 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"228670","trigger_type":"Stage2-FalsePositive-DentalDeviceExportTheme-NoReimbursementChannelBridge","entry_date":"2024-01-08","duplicate_status":"new C25 symbol/trigger/date combination outside top-covered list and previous R7 loop85 C23 symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"065510","trigger_type":"Stage2-FalsePositive-OphthalmicDeviceExportRebound-NoDistributorMarginBridge","entry_date":"2024-02-15","duplicate_status":"new C25 symbol/trigger/date combination outside top-covered list and previous R7 loop85 C23 symbols"}
```

## 4. Research question

C25 is not “medical-device stock has export language.”  
The useful medical-device signal is the bridge between device demand and revenue quality: overseas procedure volume, distributor reorder, reimbursement or regulatory access, installed-base utilization, consumable pull-through, margin, and cash conversion.

A device headline without that bridge behaves like a clinic waiting room with no procedures booked. Price can fill the chairs for a few days, but revenue does not walk in.

Residual question:

```text
Can C25 distinguish:
1. aesthetic device export/channel/margin bridge with strong MFE and tolerable MAE,
2. dental-device export theme that collapses when reimbursement/channel and procedure volume do not confirm,
3. ophthalmic-device rebound where distributor reorder and margin bridge remain weak?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C25_R7L86_335890_VIOL_AESTHETIC_DEVICE_EXPORT_BRIDGE","symbol":"335890","company_name":"비올","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_CHANNEL_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-AestheticDeviceExportChannelMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_export_channel_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Aesthetic-device export/channel proxy produced strong MFE with tolerable MAE. Green still requires exact distributor, procedure-volume, reimbursement/regulatory and margin evidence."}
{"row_type":"case","case_id":"C25_R7L86_228670_RAY_DENTAL_EXPORT_THEME_NO_BRIDGE","symbol":"228670","company_name":"레이","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_DEVICE_EXPORT_THEME_WITHOUT_REIMBURSEMENT_CHANNEL_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DentalDeviceExportTheme-NoReimbursementChannelBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_device_export_theme_overcredited","price_source":"Songdaiki/stock-web","notes":"Dental-device export theme had near-zero MFE and extreme MAE when reimbursement/channel, procedure-volume and margin bridges were missing."}
{"row_type":"case","case_id":"C25_R7L86_065510_HUVITZ_OPHTHALMIC_REBOUND_NO_BRIDGE","symbol":"065510","company_name":"휴비츠","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"OPHTHALMIC_DEVICE_REBOUND_WITHOUT_DISTRIBUTOR_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-OphthalmicDeviceExportRebound-NoDistributorMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_device_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Ophthalmic-device rebound had almost no forward MFE and large MAE when distributor reorder, reimbursement and margin bridge remained weak."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 335890 비올 — aesthetic device export/channel/margin bridge positive

Entry row: `2024-02-16 c=8100`.  
Observed path: early low `2024-02-29 l=7300`, 30D high around `2024-03-29 h=11360`, 90D/180D high `2024-04-01 h=12030`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L86_C25_335890_20240216_STAGE2_AESTHETIC_DEVICE_EXPORT_BRIDGE","case_id":"C25_R7L86_335890_VIOL_AESTHETIC_DEVICE_EXPORT_BRIDGE","symbol":"335890","company_name":"비올","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_CHANNEL_MARGIN_BRIDGE","loop_objective":"residual_missed_structural_mining;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-AestheticDeviceExportChannelMarginBridge-Positive","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":8100.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_aesthetic_device_export_channel_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; aesthetic device export, distributor/channel and procedure-volume bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["export_channel_proxy","procedure_volume_proxy","installed_base_or_consumable_pullthrough_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_distributor_reorder_pending","reimbursement_or_regulatory_access_pending","margin_bridge_pending","source_url_pending"],"stage4b_evidence_fields":["price_only_extension_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/335/335890/2024.csv","profile_path":"atlas/symbol_profiles/335/335890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":40.25,"MFE_90D_pct":48.52,"MFE_180D_pct":48.52,"MAE_30D_pct":-9.88,"MAE_90D_pct":-9.88,"MAE_180D_pct":-9.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":12030.0,"max_drawdown_low_date":"2024-02-29","max_drawdown_low":7300.0,"drawdown_after_peak_pct":-44.89,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_extension_watch_not_full_4B_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_tolerable_MAE","current_profile_verdict":"current_profile_correct_if_export_channel_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window; status_inferred_inactive_after_2025_not_a_2024_blocker","same_entry_group_id":"335890_2024-02-16_8100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C25 can allow Stage2/Yellow when medical-device strength is tied to export channel, procedure volume, installed-base or reimbursement/margin bridge. Green still requires exact non-price evidence."}
```

### 6.2 228670 레이 — dental-device export theme without reimbursement/channel bridge

Entry row: `2024-01-08 c=24750`.  
Observed path: local high `2024-01-09 h=25100`, then lows `2024-02-21 l=16000`, `2024-04-25 l=13230`, and `2024-09-24 l=7830`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L86_C25_228670_20240108_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_THEME","case_id":"C25_R7L86_228670_RAY_DENTAL_EXPORT_THEME_NO_BRIDGE","symbol":"228670","company_name":"레이","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_DEVICE_EXPORT_THEME_WITHOUT_REIMBURSEMENT_CHANNEL_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-DentalDeviceExportTheme-NoReimbursementChannelBridge","trigger_date":"2024-01-08","entry_date":"2024-01-08","entry_price":24750.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_dental_device_export_theme_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; dental-device export theme treated as insufficient without reimbursement access, channel reorder, procedure volume and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["dental_device_export_theme","relative_strength_rebound"],"stage3_evidence_fields":["reimbursement_bridge_missing","distributor_channel_reorder_missing","procedure_volume_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","channel_reimbursement_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/228/228670/2024.csv","profile_path":"atlas/symbol_profiles/228/228670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.41,"MFE_90D_pct":1.41,"MFE_180D_pct":1.41,"MAE_30D_pct":-35.35,"MAE_90D_pct":-46.55,"MAE_180D_pct":-68.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-09","peak_price":25100.0,"max_drawdown_low_date":"2024-09-24","max_drawdown_low":7830.0,"drawdown_after_peak_pct":-68.80,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"dental_device_export_theme_without_reimbursement_channel_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","channel_reimbursement_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_extreme_MAE","current_profile_verdict":"current_profile_false_positive_if_device_export_theme_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"228670_2024-01-08_24750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C25 should not upgrade dental-device export theme without reimbursement, distributor reorder, procedure-volume and margin bridge. Near-zero MFE and extreme MAE force Watch/4B-risk."}
```

### 6.3 065510 휴비츠 — ophthalmic-device rebound without distributor/margin bridge

Entry row: `2024-02-15 c=18960`.  
Observed path: near-term high `2024-02-15 h=19170`, then lows `2024-04-08 l=12550`, `2024-06-25 l=11600`, and `2024-12-09 l=6610`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L86_C25_065510_20240215_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_REBOUND","case_id":"C25_R7L86_065510_HUVITZ_OPHTHALMIC_REBOUND_NO_BRIDGE","symbol":"065510","company_name":"휴비츠","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"OPHTHALMIC_DEVICE_REBOUND_WITHOUT_DISTRIBUTOR_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;canonical_archetype_rule_candidate","trigger_type":"Stage2-FalsePositive-OphthalmicDeviceExportRebound-NoDistributorMarginBridge","trigger_date":"2024-02-15","entry_date":"2024-02-15","entry_price":18960.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_ophthalmic_device_export_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; ophthalmic-device rebound treated as insufficient without distributor reorder, reimbursement/access, installed-base utilization and margin bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["ophthalmic_device_rebound","export_theme_proxy"],"stage3_evidence_fields":["distributor_reorder_missing","reimbursement_access_missing","installed_base_utilization_missing","margin_bridge_missing"],"stage4b_evidence_fields":["price_only_local_peak","distributor_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/065/065510/2024.csv","profile_path":"atlas/symbol_profiles/065/065510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.11,"MFE_90D_pct":1.11,"MFE_180D_pct":1.11,"MAE_30D_pct":-25.84,"MAE_90D_pct":-38.82,"MAE_180D_pct":-60.50,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-15","peak_price":19170.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":6610.0,"drawdown_after_peak_pct":-65.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"ophthalmic_device_rebound_without_distributor_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","distributor_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive_if_device_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_for_2024_window","same_entry_group_id":"065510_2024-02-15_18960","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C25 should keep ophthalmic-device rebound in Watch/4B unless distributor reorder, access/reimbursement, installed-base utilization and margin bridge are verified."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C25_R7L86_335890_VIOL_AESTHETIC_DEVICE_EXPORT_BRIDGE","trigger_id":"R7L86_C25_335890_20240216_STAGE2_AESTHETIC_DEVICE_EXPORT_BRIDGE","symbol":"335890","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C25 requires export channel/procedure/reimbursement bridge rather than device theme alone","raw_component_scores_before":{"export_channel_score":14,"reimbursement_or_access_score":10,"procedure_volume_score":12,"installed_base_pullthrough_score":12,"margin_bridge_score":10,"relative_strength_score":13,"valuation_repricing_score":9,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"export_channel_score":17,"reimbursement_or_access_score":13,"procedure_volume_score":15,"installed_base_pullthrough_score":14,"margin_bridge_score":12,"relative_strength_score":14,"valuation_repricing_score":10,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow-Watch","component_delta_explanation":"Export channel and procedure-volume bridge support Yellow-watch, but exact reimbursement/access and margin evidence still block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C25_R7L86_228670_RAY_DENTAL_EXPORT_THEME_NO_BRIDGE","trigger_id":"R7L86_C25_228670_20240108_STAGE2_FALSE_POSITIVE_DENTAL_EXPORT_THEME","symbol":"228670","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_scope":"current_default_proxy","profile_hypothesis":"dental-device export theme without reimbursement/channel bridge should be blocked","raw_component_scores_before":{"export_channel_score":6,"reimbursement_or_access_score":1,"procedure_volume_score":1,"installed_base_pullthrough_score":2,"margin_bridge_score":1,"relative_strength_score":9,"valuation_repricing_score":5,"execution_risk_score":-14,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_channel_score":1,"reimbursement_or_access_score":0,"procedure_volume_score":0,"installed_base_pullthrough_score":0,"margin_bridge_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-22,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and extreme MAE convert device-export theme into missing access/channel bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","case_id":"C25_R7L86_065510_HUVITZ_OPHTHALMIC_REBOUND_NO_BRIDGE","trigger_id":"R7L86_C25_065510_20240215_STAGE2_FALSE_POSITIVE_OPHTHALMIC_DEVICE_REBOUND","symbol":"065510","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_scope":"current_default_proxy","profile_hypothesis":"ophthalmic-device rebound without distributor/margin bridge should remain Watch/blocked","raw_component_scores_before":{"export_channel_score":4,"reimbursement_or_access_score":1,"procedure_volume_score":1,"installed_base_pullthrough_score":2,"margin_bridge_score":1,"relative_strength_score":8,"valuation_repricing_score":4,"execution_risk_score":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_channel_score":1,"reimbursement_or_access_score":0,"procedure_volume_score":0,"installed_base_pullthrough_score":0,"margin_bridge_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-20,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/Blocked","component_delta_explanation":"Low MFE and high MAE require distributor, access/reimbursement and margin bridge before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R7L86_C25_P0_CURRENT","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_id":"P0_e2r_2_2_rolling_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C25 needs explicit export channel, procedure volume, reimbursement/access and margin bridge distinction","eligible_trigger_count":3,"avg_MFE90_pct":17.01,"avg_MAE90_pct":-32.42,"avg_MFE180_pct":17.01,"avg_MAE180_pct":-46.25,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C25_export_reimbursement_channel_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R7L86_C25_P1_SECTOR_SPECIFIC","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_id":"P1_L7_medical_device_access_channel_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L7 medical-device signals need export channel, reimbursement/access, procedure volume, installed-base pull-through or margin bridge before Stage2-Actionable","changed_axes":["export_channel_bridge_required","reimbursement_access_required","procedure_volume_required","device_theme_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_export_channel_reimbursement_access_procedure_volume_installed_base_or_margin_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":17.01,"avg_MAE90_pct":-32.42,"avg_MFE180_pct":17.01,"avg_MAE180_pct":-46.25,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R7L86_C25_P2_CANONICAL","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_id":"P2_C25_export_reimbursement_margin_bridge_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C25 should reward access/channel/procedure conversion, not medical-device theme rebounds","changed_axes":["C25_export_reimbursement_channel_bridge_required","C25_device_theme_local_4B_guard","C25_procedure_volume_margin_bridge_required"],"changed_thresholds":{"stage2_yellow_gate":"export_channel_plus_reimbursement_or_procedure_volume_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":17.01,"avg_MAE90_pct":-32.42,"avg_MFE180_pct":17.01,"avg_MAE180_pct":-46.25,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R7L86_C25_P3_COUNTEREXAMPLE_GUARD","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_id":"P3_C25_high_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If MFE90<5 and MAE90<=-25 while export/access/channel bridge is missing, block Yellow/Green","changed_axes":["C25_high_MAE_guardrail","C25_local_4B_watch_guard"],"changed_thresholds":{"bad_entry_filter":"MFE90_lt_5_and_MAE90_le_minus_25"},"eligible_trigger_count":3,"avg_MFE90_pct":17.01,"avg_MAE90_pct":-32.42,"avg_MFE180_pct":17.01,"avg_MAE180_pct":-46.25,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_DEVICE_EXPORT_ACCESS_BRIDGE_VS_DEVICE_THEME_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":17.01,"avg_MAE90_pct":-32.42,"avg_MFE180_pct":17.01,"avg_MAE180_pct":-46.25,"stage2_hit_rate_MFE90_ge_20":0.33,"stage2_bad_entry_rate_MFE90_lt_5":0.67,"stage2_bad_entry_rate_MAE90_le_minus_25":0.67,"interpretation":"C25 needs bridge discipline. 비올 shows aesthetic-device export/channel bridge can rerate, while 레이 and 휴비츠 show dental/ophthalmic device themes can fail badly without reimbursement/access, distributor reorder, procedure volume and margin evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"335890","trigger_type":"Stage2-Actionable-AestheticDeviceExportChannelMarginBridge-Positive","entry_date":"2024-02-16","stage2_to_90D_outcome":"good_stage2_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_device_export_channel_rerating","MFE90_ge_20":true,"MAE90_le_minus_20":false,"transition_note":"Allow Stage2/Yellow when export channel, procedure volume, installed-base and margin bridge exists; Green requires exact reimbursement/access and margin evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"228670","trigger_type":"Stage2-FalsePositive-DentalDeviceExportTheme-NoReimbursementChannelBridge","entry_date":"2024-01-08","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_extreme_MAE","stage2_to_180D_outcome":"failed_dental_device_export_theme","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Dental-device export theme without reimbursement/channel and procedure-volume bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"065510","trigger_type":"Stage2-FalsePositive-OphthalmicDeviceExportRebound-NoDistributorMarginBridge","entry_date":"2024-02-15","stage2_to_90D_outcome":"bad_stage2_low_MFE_high_MAE","stage2_to_180D_outcome":"failed_ophthalmic_device_rebound","MFE90_ge_20":false,"MAE90_le_minus_20":true,"transition_note":"Ophthalmic-device rebound without distributor/access/margin bridge should stay Watch/blocked."}
{"row_type":"residual_contribution","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","residual_type":"medical_device_export_theme_overcredit_without_reimbursement_channel_procedure_margin_bridge","contribution":"Adds two C25 local 4B/high-MAE counterexamples against one aesthetic-device export/channel bridge positive, avoiding C25 top-covered and previous R7 loop85 C23 symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_REIMBURSEMENT_CHANNEL_BRIDGE_VS_DENTAL_OPHTHALMIC_DEVICE_EXPORT_THEME_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C25 now has non-top-symbol dental/ophthalmic device-theme counterexamples; next R7 loops should exact-URL repair reimbursement/access, distributor reorder, procedure volume, installed-base utilization and margin evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","axis":"C25_export_reimbursement_channel_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"335890 worked with export/channel/procedure-volume bridge proxy; 228670 and 065510 failed when device-theme strength lacked reimbursement/access, distributor reorder, procedure-volume and margin bridge."}
{"row_type":"shadow_weight","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","axis":"C25_device_theme_local_4B_watch_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Dental and ophthalmic device-theme rows showed near-zero/low MFE and high/extreme MAE without non-price bridge."}
{"row_type":"shadow_weight","round":"R7","loop":"86","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","axis":"C25_high_MAE_guardrail","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"If MFE90<5 and MAE90<=-25 while export/access/channel bridge is missing, block Stage2-Actionable/Yellow and route to Watch/4B-risk."}
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
  - medical_device_export_theme_overcredit
  - reimbursement_access_bridge_missing
  - distributor_channel_reorder_missing
  - procedure_volume_margin_bridge_missing
new_axis_proposed:
  - C25_export_reimbursement_channel_bridge_required_shadow_only
  - C25_device_theme_local_4B_watch_guard_shadow_only
  - C25_high_MAE_guardrail_shadow_only
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
3. Confirm R7 / L7 / C25 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C25 top-covered symbols
   - previous R7 loop85 C23 symbols listed in the MD
6. Confirm 335890's inactive_or_delisted_like inference is not a 2024 forward-window blocker before aggregate import.
7. If aggregate support remains stable after exact evidence URL repair, consider C25-scoped safe patch candidates:
   - C25_export_reimbursement_channel_bridge_required
   - C25_device_theme_local_4B_watch_guard
   - C25_high_MAE_guardrail
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R7
completed_loop = 86
next_round = R8
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 2 counterexamples, and 2 local 4B-watch rows for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.
```

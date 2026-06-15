# E2R Stock-Web v12 Residual Research — R7 Loop 92 / L7 / C25

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R7
loop: 92
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DEVICE_CONSUMABLE_EXPORT_BRIDGE_VS_DENTAL_CGM_REIMBURSEMENT_VOCABULARY_DECAY
sector: bio / healthcare / medical device / aesthetic device / dental implant / CGM / reimbursement / export channel / consumables / repeat revenue
output_file: e2r_stock_web_v12_residual_round_R7_loop_92_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R6 loop 92`.

```text
scheduled_round = R7
scheduled_loop = 92
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```

R7 is restricted to bio / healthcare / medical.
C25 is selected because the recent R7 sequence rotated:

```text
R7 loop85 C23
R7 loop86 C25
R7 loop87 C24
R7 loop88 C23
R7 loop89 C25
R7 loop90 C24
R7 loop91 C23
```

Therefore loop92 returns to `C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT`.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
rows = 33
symbols = 17
good/bad Stage2 = 11/6
4B/4C = 4/4
top-covered = 228670, 214450, 335890, 065510, 043150, 041830
```

This loop avoids the C25 top-covered list and recent R7 loop symbols:

```text
R7 loop85 C23: 145020, 302440, 086900
R7 loop86 C25: 335890, 228670, 065510
R7 loop87 C24: 196170, 206650, 950220
R7 loop88 C23: 000250, 019170, 095700
R7 loop89 C25: 200670, 119610, 290650
R7 loop90 C24: 237690, 365270, 256840
R7 loop91 C23: 326030, 067630, 229000
C25 top-covered: 228670, 214450, 335890, 065510, 043150, 041830
```

Candidate hygiene note:

```text
During this execution path, stale R6/C22 and earlier-sector candidate rows were touched while checking alternatives.
Those rows are not used in this R7/C25 output.
```

Selected symbols:

```text
214150, 145720, 099190
```

The selected pocket is:

```text
aesthetic medical device / consumables / export channel / procedure-volume bridge
vs
dental implant export vocabulary without repeat-order/reimbursement/margin bridge after the price spike
vs
CGM/reimbursement vocabulary without durable reimbursement adoption and consumables cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"214150","company_name":"클래시스","profile_path":"atlas/symbol_profiles/214/214150.json","first_date":"2015-04-03","last_date":"2026-02-20","trading_day_count":2608,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2017-12-28"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical SPAC/name-transition corporate-action candidate exists long before selected 2024 forward window. 2024 selected window is usable; share-count movement in 2024 remains price-quality watch before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry; share_count_movement_watch"}
{"row_type":"price_source_validation","symbol":"145720","company_name":"덴티움","profile_path":"atlas/symbol_profiles/145/145720.json","first_date":"2017-03-15","last_date":"2026-02-20","trading_day_count":2190,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"has_major_raw_discontinuity":false,"calibration_caveat":"","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"clean_2024_forward_window"}
{"row_type":"price_source_validation","symbol":"099190","company_name":"아이센스","profile_path":"atlas/symbol_profiles/099/099190.json","first_date":"2013-01-30","last_date":"2026-02-20","trading_day_count":3205,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["2015-10-02","2023-03-14","2023-04-10"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"214150","trigger_type":"Stage2-Actionable-AestheticDeviceConsumableExportProcedureVolumeBridge-Positive","entry_date":"2024-02-14","duplicate_status":"new C25 symbol/trigger/date combination outside C25 top-covered and previous R7 loop symbols; share-count movement watch"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"145720","trigger_type":"Stage2-FalsePositive-DentalImplantExportSpikeNoRepeatOrderReimbursementMarginBridge","entry_date":"2024-02-29","duplicate_status":"new C25 symbol/trigger/date combination outside C25 top-covered and previous R7 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"099190","trigger_type":"Stage2-FalsePositive-CGMReimbursementVocabularyNoDurableAdoptionConsumablesCashBridge","entry_date":"2024-01-11","duplicate_status":"new C25 symbol/trigger/date combination outside C25 top-covered and previous R7 loop symbols"}
```

## 4. Research question

C25 is not “의료기기 수출/리임버스먼트 단어가 있다.”
The useful signal must prove the export-to-repeat-revenue chain:

```text
medical device export channel
procedure volume or installed base
consumables / repeat revenue
reimbursement adoption or payer path
customer / distributor reorder
regulatory clearance or product mix quality
gross-margin bridge
working-capital discipline
cash conversion
```

A medical-device headline without this bridge is a device placed in a clinic room but not yet used on patients. E2R needs the procedure, the consumable pull-through, the reorder, reimbursement, margin, and cash collection.

Residual question:

```text
Can C25 distinguish:
1. aesthetic device / consumables / procedure-volume export bridge with high MFE and controlled entry MAE,
2. dental implant export vocabulary after a spike where repeat order and reimbursement/margin evidence are missing,
3. CGM/reimbursement vocabulary where no durable payer adoption, consumables utilization or cash bridge exists?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C25_R7L92_214150_CLASSYS_AESTHETIC_DEVICE_CONSUMABLE","symbol":"214150","company_name":"클래시스","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_CONSUMABLE_EXPORT_PROCEDURE_VOLUME_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-AestheticDeviceConsumableExportProcedureVolumeBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"score_price_alignment":"positive_high_MFE90_and_MFE180_low_MAE_device_consumable_export_bridge","current_profile_verdict":"current_profile_correct_if_procedure_volume_consumable_reorder_margin_cash_bridge_required_but_data_quality_repair_needed","price_source":"Songdaiki/stock-web","notes":"Aesthetic device/export/procedure-volume/consumables proxy produced high MFE90 and MFE180 with shallow entry MAE. Green still requires exact installed-base, procedure-volume, consumable reorder, margin and cash evidence; 2024 share-count movement watch remains."}
{"row_type":"case","case_id":"C25_R7L92_145720_DENTIUM_DENTAL_IMPLANT_SPIKE_DECAY","symbol":"145720","company_name":"덴티움","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMPLANT_EXPORT_SPIKE_WITHOUT_REPEAT_ORDER_REIMBURSEMENT_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-DentalImplantExportSpikeNoRepeatOrderReimbursementMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_extreme_MAE_after_export_spike_no_bridge","current_profile_verdict":"current_profile_false_positive_if_dental_export_spike_overcredited","price_source":"Songdaiki/stock-web","notes":"Dental implant/export vocabulary after the first spike had near-zero forward MFE and extreme MAE without repeat-order, reimbursement/market access, margin or cash bridge."}
{"row_type":"case","case_id":"C25_R7L92_099190_ISENS_CGM_REIMBURSEMENT_DECAY","symbol":"099190","company_name":"아이센스","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"CGM_REIMBURSEMENT_VOCABULARY_WITHOUT_DURABLE_ADOPTION_CONSUMABLES_CASH_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-CGMReimbursementVocabularyNoDurableAdoptionConsumablesCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_no_reimbursement_adoption_consumables_bridge","current_profile_verdict":"current_profile_false_positive_if_CGM_reimbursement_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"CGM/reimbursement vocabulary produced only near-zero MFE and then deep MAE without durable payer adoption, installed-base utilization, consumables pull-through or cash bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 214150 클래시스 — aesthetic device / consumables / procedure-volume export bridge

Entry row: `2024-02-14 c=30000`.
Observed path: entry-area low `2024-02-14 l=28050`, 90D peak `2024-06-19 h=56900`, and full-window peak `2024-10-21 h=62900`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L92_C25_214150_20240214_STAGE2_AESTHETIC_DEVICE_CONSUMABLE_EXPORT","case_id":"C25_R7L92_214150_CLASSYS_AESTHETIC_DEVICE_CONSUMABLE","symbol":"214150","company_name":"클래시스","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_CONSUMABLE_EXPORT_PROCEDURE_VOLUME_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-AestheticDeviceConsumableExportProcedureVolumeBridge-Positive","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":30000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_aesthetic_device_export_consumable_procedure_volume_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; aesthetic medical device export, installed base, procedure volume, consumables and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["aesthetic_device_export_proxy","procedure_volume_proxy","consumables_repeat_revenue_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_installed_base_source_pending","procedure_volume_source_pending","consumable_reorder_source_pending","margin_cash_bridge_pending"],"stage4b_evidence_fields":["price_extension_watch","share_count_movement_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.83,"MFE_90D_pct":89.67,"MFE_180D_pct":109.67,"MAE_30D_pct":-6.50,"MAE_90D_pct":-6.50,"MAE_180D_pct":-6.50,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-21","peak_price":62900.0,"max_drawdown_low_date":"2024-02-14","max_drawdown_low":28050.0,"drawdown_after_peak_pct":-36.41,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_installed_base_procedure_consumable_reorder_margin_cash_evidence_and_price_quality_repair","four_b_evidence_type":["price_extension_watch","share_count_movement_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_and_MFE180_low_MAE_device_consumable_export_bridge","current_profile_verdict":"current_profile_correct_if_procedure_volume_consumable_reorder_margin_cash_bridge_required_but_data_quality_repair_needed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["share_count_movement_watch_before_patch"],"corporate_action_window_status":"historical_SPAC_name_transition_pre_2024; selected_window_clean; 2024_share_count_movement_watch","same_entry_group_id":"214150_2024-02-14_30000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"do_not_count_as_new_case":false,"current_profile_residual":"C25 can allow Stage2/Yellow or Green-candidate-watch when medical-device strength is tied to installed base, procedure volume, consumable reorder, margin and cash conversion. Green still requires exact source-grade evidence and price-quality repair."}
```

### 6.2 145720 덴티움 — dental implant export spike without repeat-order / reimbursement-margin bridge

Entry row: `2024-02-29 c=144200`, after a dental implant/export price spike.
Observed path: local high `2024-03-06 h=148500`, then long decline to `2024-11-15 l=54000`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L92_C25_145720_20240229_STAGE2_FALSE_POSITIVE_DENTAL_IMPLANT_EXPORT_SPIKE","case_id":"C25_R7L92_145720_DENTIUM_DENTAL_IMPLANT_SPIKE_DECAY","symbol":"145720","company_name":"덴티움","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMPLANT_EXPORT_SPIKE_WITHOUT_REPEAT_ORDER_REIMBURSEMENT_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;post_spike_entry_guard","trigger_type":"Stage2-FalsePositive-DentalImplantExportSpikeNoRepeatOrderReimbursementMarginBridge","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":144200.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_dental_implant_export_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; dental implant export vocabulary treated as insufficient without repeat order, reimbursement/market-access, distributor sell-through, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["dental_implant_export_vocabulary","post_spike_relative_strength"],"stage3_evidence_fields":["repeat_order_missing","reimbursement_or_market_access_missing","distributor_sellthrough_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["near_zero_MFE","post_spike_entry_watch","extreme_MAE","repeat_order_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/145/145720/2024.csv","profile_path":"atlas/symbol_profiles/145/145720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.98,"MFE_90D_pct":2.98,"MFE_180D_pct":2.98,"MAE_30D_pct":-13.11,"MAE_90D_pct":-13.18,"MAE_180D_pct":-62.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-06","peak_price":148500.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":54000.0,"drawdown_after_peak_pct":-63.64,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"dental_implant_export_spike_without_repeat_order_reimbursement_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","post_spike_entry_watch","extreme_MAE","repeat_order_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_extreme_MAE_after_export_spike_no_bridge","current_profile_verdict":"current_profile_false_positive_if_dental_export_spike_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean","same_entry_group_id":"145720_2024-02-29_144200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C25 should not promote dental implant/export price spikes unless repeat order, distributor sell-through, reimbursement or market-access, margin and cash evidence are repaired. Near-zero MFE and extreme MAE route to Watch/4B."}
```

### 6.3 099190 아이센스 — CGM/reimbursement vocabulary without durable adoption / consumables-cash bridge

Entry row: `2024-01-11 c=30050`, on CGM/reimbursement vocabulary after a short price push.
Observed path: high `2024-01-12 h=30400`, then persistent decline to `2024-12-27 l=14970`.

```jsonl
{"row_type":"trigger","trigger_id":"R7L92_C25_099190_20240111_STAGE2_FALSE_POSITIVE_CGM_REIMBURSEMENT","case_id":"C25_R7L92_099190_ISENS_CGM_REIMBURSEMENT_DECAY","symbol":"099190","company_name":"아이센스","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"CGM_REIMBURSEMENT_VOCABULARY_WITHOUT_DURABLE_ADOPTION_CONSUMABLES_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;reimbursement_adoption_4B_stress_test","trigger_type":"Stage2-FalsePositive-CGMReimbursementVocabularyNoDurableAdoptionConsumablesCashBridge","trigger_date":"2024-01-11","entry_date":"2024-01-11","entry_price":30050.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_CGM_reimbursement_medical_device_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; CGM/reimbursement vocabulary treated as insufficient without payer adoption, installed-base utilization, consumables pull-through, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["CGM_reimbursement_vocabulary","medical_device_export_keyword","relative_strength_spike"],"stage3_evidence_fields":["durable_payer_adoption_missing","installed_base_utilization_missing","consumables_pullthrough_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["near_zero_MFE","reimbursement_adoption_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv","profile_path":"atlas/symbol_profiles/099/099190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.16,"MFE_90D_pct":1.16,"MFE_180D_pct":1.16,"MAE_30D_pct":-31.61,"MAE_90D_pct":-37.17,"MAE_180D_pct":-50.18,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-12","peak_price":30400.0,"max_drawdown_low_date":"2024-12-27","max_drawdown_low":14970.0,"drawdown_after_peak_pct":-50.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"CGM_reimbursement_vocabulary_without_durable_payer_adoption_consumables_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","reimbursement_adoption_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_reimbursement_adoption_consumables_bridge","current_profile_verdict":"current_profile_false_positive_if_CGM_reimbursement_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"099190_2024-01-11_30050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C25 should not treat CGM/reimbursement vocabulary as positive evidence unless payer adoption, installed-base utilization, consumables pull-through, margin and cash conversion are repaired. Near-zero MFE and deep MAE force Watch/4B."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C25_R7L92_214150_CLASSYS_AESTHETIC_DEVICE_CONSUMABLE","trigger_id":"R7L92_C25_214150_20240214_STAGE2_AESTHETIC_DEVICE_CONSUMABLE_EXPORT","symbol":"214150","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C25 requires export channel, installed base, procedure volume, consumables/reorder, reimbursement or market access, margin and cash bridge rather than medical-device vocabulary alone","raw_component_scores_before":{"export_channel_score":12,"procedure_volume_score":13,"installed_base_score":12,"consumables_reorder_score":13,"reimbursement_or_market_access_score":7,"regulatory_product_mix_score":9,"gross_margin_score":11,"cash_conversion_score":8,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"export_channel_score":15,"procedure_volume_score":16,"installed_base_score":15,"consumables_reorder_score":16,"reimbursement_or_market_access_score":9,"regulatory_product_mix_score":11,"gross_margin_score":13,"cash_conversion_score":10,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":89,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Device/export/procedure/consumables bridge plus high MFE supports Green-candidate watch; exact source evidence and price-quality repair block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C25_R7L92_145720_DENTIUM_DENTAL_IMPLANT_SPIKE_DECAY","trigger_id":"R7L92_C25_145720_20240229_STAGE2_FALSE_POSITIVE_DENTAL_IMPLANT_EXPORT_SPIKE","symbol":"145720","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_scope":"current_default_proxy","profile_hypothesis":"dental implant export price spike without repeat order and reimbursement/margin bridge should be blocked","raw_component_scores_before":{"export_channel_score":3,"procedure_volume_score":1,"installed_base_score":1,"consumables_reorder_score":0,"reimbursement_or_market_access_score":0,"regulatory_product_mix_score":1,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":5,"valuation_repricing_score":2,"execution_risk_score":-18,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_channel_score":1,"procedure_volume_score":0,"installed_base_score":0,"consumables_reorder_score":0,"reimbursement_or_market_access_score":0,"regulatory_product_mix_score":0,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-30,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and extreme MAE require repeat-order, reimbursement/market access, margin and cash evidence before any Yellow/Green promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C25_R7L92_099190_ISENS_CGM_REIMBURSEMENT_DECAY","trigger_id":"R7L92_C25_099190_20240111_STAGE2_FALSE_POSITIVE_CGM_REIMBURSEMENT","symbol":"099190","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_scope":"current_default_proxy","profile_hypothesis":"CGM/reimbursement vocabulary without durable payer adoption and consumables bridge should remain Watch/4B","raw_component_scores_before":{"export_channel_score":1,"procedure_volume_score":1,"installed_base_score":1,"consumables_reorder_score":0,"reimbursement_or_market_access_score":2,"regulatory_product_mix_score":1,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":3,"valuation_repricing_score":1,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"export_channel_score":0,"procedure_volume_score":0,"installed_base_score":0,"consumables_reorder_score":0,"reimbursement_or_market_access_score":0,"regulatory_product_mix_score":0,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":0,"valuation_repricing_score":0,"execution_risk_score":-28,"theme_spike_risk":-22,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE require durable reimbursement adoption, utilization, consumables and cash evidence before Yellow/Green."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R7L92_C25_P0_CURRENT","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C25 needs explicit installed-base, procedure-volume, consumables/reorder, reimbursement/adoption, margin/cash and post-spike 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":31.27,"avg_MAE90_pct":-19.28,"avg_MFE180_pct":37.94,"avg_MAE180_pct":-39.74,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":0.95,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C25_device_consumables_reimbursement_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R7L92_C25_P1_SECTOR_SPECIFIC","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_id":"P1_L7_medical_device_consumable_reimbursement_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L7 medical-device signals need export channel, procedure volume, installed base, consumables/reorder, reimbursement adoption, gross margin or cash conversion before Stage2-Actionable","changed_axes":["procedure_volume_required","consumables_reorder_required","reimbursement_adoption_required","post_spike_medtech_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_procedure_volume_installed_base_consumables_reorder_reimbursement_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":31.27,"avg_MAE90_pct":-19.28,"avg_MFE180_pct":37.94,"avg_MAE180_pct":-39.74,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_price_quality_repaired"}
{"row_type":"profile_comparison","comparison_id":"R7L92_C25_P2_CANONICAL","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_id":"P2_C25_device_consumables_reimbursement_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C25 should reward installed-base-to-consumables-to-cash mechanics, not medtech/export/reimbursement vocabulary","changed_axes":["C25_procedure_volume_consumable_reorder_margin_cash_bridge_required","C25_dental_CGM_vocabulary_local_4B_guard","C25_post_spike_entry_guard","C25_price_quality_repair_guard"],"changed_thresholds":{"stage2_yellow_gate":"export_or_device_channel_plus_installed_base_or_consumable_reorder_or_reimbursement_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":31.27,"avg_MAE90_pct":-19.28,"avg_MFE180_pct":37.94,"avg_MAE180_pct":-39.74,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R7L92_C25_P3_COUNTEREXAMPLE_GUARD","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","profile_id":"P3_C25_near_zero_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If installed-base/reimbursement/consumables bridge is missing, MFE90<5 or MAE90<=-20 should block Yellow/Green and route to 4B-watch","changed_axes":["C25_near_zero_MFE_guardrail","C25_deep_MAE_4B_guardrail","C25_post_spike_entry_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_5_or_MAE90_le_minus_20)"},"eligible_trigger_count":3,"avg_MFE90_pct":31.27,"avg_MAE90_pct":-19.28,"avg_MFE180_pct":37.94,"avg_MAE180_pct":-39.74,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_AESTHETIC_DEVICE_POSITIVE_VS_DENTAL_CGM_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":31.27,"avg_MAE90_pct":-19.28,"avg_MFE180_pct":37.94,"avg_MAE180_pct":-39.74,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE90_le_minus20":0.33,"interpretation":"C25 needs bridge discipline. 클래시스 shows aesthetic-device export/procedure-volume/consumables bridge can support Yellow/Green-candidate-watch, while 덴티움 and 아이센스 show dental/CGM/reimbursement vocabulary should not be promoted without repeat order, reimbursement adoption, consumables pull-through, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"214150","trigger_type":"Stage2-Actionable-AestheticDeviceConsumableExportProcedureVolumeBridge-Positive","entry_date":"2024-02-14","stage2_to_90D_outcome":"good_stage2_high_MFE_low_MAE","stage2_to_180D_outcome":"positive_device_consumable_export_bridge_but_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when device strength is tied to installed base, procedure volume, consumables/reorder, margin and cash bridge; Green requires exact source-grade evidence and price-quality repair."}
{"row_type":"stage_transition_summary","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"145720","trigger_type":"Stage2-FalsePositive-DentalImplantExportSpikeNoRepeatOrderReimbursementMarginBridge","entry_date":"2024-02-29","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_bridge_missing","stage2_to_180D_outcome":"failed_dental_implant_export_spike_extreme_MAE","MFE90_ge20":false,"MAE180_le_minus35":true,"transition_note":"Dental implant export spike without repeat order, reimbursement/market access and margin/cash bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"099190","trigger_type":"Stage2-FalsePositive-CGMReimbursementVocabularyNoDurableAdoptionConsumablesCashBridge","entry_date":"2024-01-11","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE","stage2_to_180D_outcome":"failed_CGM_reimbursement_vocabulary_no_consumables_cash_bridge","MFE90_ge20":false,"MAE90_le_minus20":true,"transition_note":"CGM/reimbursement vocabulary without durable payer adoption, installed-base utilization and consumables cash bridge should remain Watch/4B-risk."}
{"row_type":"residual_contribution","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","residual_type":"dental_CGM_reimbursement_vocabulary_overcredit_without_installed_base_consumables_margin_cash_bridge","contribution":"Adds two C25 4B counterexamples against one aesthetic-device consumables/procedure-volume positive, avoiding C25 top-covered and recent R7 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_CONSUMABLE_EXPORT_BRIDGE_VS_DENTAL_CGM_REIMBURSEMENT_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C25 now has non-top-symbol aesthetic-device procedure-volume/consumables positive and two dental/CGM weak-bridge counterexamples; next R7 C25 loops should exact-URL repair installed base, procedure volume, consumables reorder, reimbursement adoption, gross margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","axis":"C25_procedure_volume_consumable_reorder_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"214150 worked when aesthetic-device/procedure/consumables proxy existed; 145720 and 099190 failed when med-device vocabulary lacked repeat-order, reimbursement adoption and cash evidence."}
{"row_type":"shadow_weight","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","axis":"C25_dental_CGM_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Dental implant and CGM/reimbursement rows showed near-zero forward MFE and deep MAE when installed-base/reimbursement/consumables bridge was missing."}
{"row_type":"shadow_weight","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","axis":"C25_post_spike_entry_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"risk_guard","apply_now":false,"shadow_only":true,"evidence_basis":"145720 shows post-spike entries should not be promoted unless fresh repeat-order/reimbursement/margin evidence exists."}
{"row_type":"shadow_weight","round":"R7","loop":"92","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","axis":"C25_price_quality_repair_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"214150 has historical SPAC/name-transition and 2024 share-count movement watch; patch consideration requires price-quality repair."}
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
  - dental_implant_export_spike_overcredit
  - CGM_reimbursement_vocabulary_overcredit
  - repeat_order_reimbursement_bridge_missing
  - installed_base_consumables_margin_cash_bridge_missing
  - post_spike_entry_watch
  - price_quality_repair_watch
new_axis_proposed:
  - C25_procedure_volume_consumable_reorder_margin_cash_bridge_required_shadow_only
  - C25_dental_CGM_vocabulary_local_4B_guard_shadow_only
  - C25_post_spike_entry_guard_shadow_only
  - C25_price_quality_repair_guard_shadow_only
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
`214150` has an old SPAC/name-transition corporate-action candidate before 2024 and 2024 share-count movement watch; the selected 2024 price path is usable for residual analysis, but patch promotion requires price-quality repair.
`145720` has no corporate-action candidate and the selected 2024 window is clean.
`099190` has older corporate-action candidates before 2024; the selected 2024 window is usable.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
price_quality_watch = true for 214150
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
   - previous R7 loop89 C25 symbols
   - previous R7 loop90 C24 symbols
   - previous R7 loop91 C23 symbols
6. Confirm stale R6/C22 and earlier-sector candidate rows are not ingested from this MD.
7. Keep 214150 in price-quality repair watch before patch consideration.
8. If aggregate support remains stable after exact evidence URL and price-quality repair, consider C25-scoped safe patch candidates:
   - C25_procedure_volume_consumable_reorder_margin_cash_bridge_required
   - C25_dental_CGM_vocabulary_local_4B_guard
   - C25_post_spike_entry_guard
   - C25_price_quality_repair_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R7
completed_loop = 92
next_round = R8
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.
```

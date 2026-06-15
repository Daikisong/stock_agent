# E2R Stock-Web V12 Residual Research — C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## 1. Selection metadata

```text
selected_round = R7
selected_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE

price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## 2. Why this archetype was selected

`C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT` is still a low-coverage Priority 0 archetype in the static No-Repeat Index. The conversation-local ledger already contains C25 loops 100/102/103, but those runs still leave the archetype below the local 30-row floor. This loop therefore performs a second expansion to 30, widening C25 beyond previously used Classys/Dentium/Vatech/Ray/J-Sys style rows into broader medical device, aesthetic device, CGM/diagnostic, optical, orthopedic implant, and service/consumable revenue paths.

The key residual question is not whether a stock has a "medical device" label. The mechanism must travel all the way through:

```text
device export / reimbursement / installed base
  -> procedure volume or recurring consumable/service revenue
  -> distributor restocking rather than one-off stuffing
  -> gross margin / OPM / revision / cash-flow bridge
  -> durable Stage3/Green rather than price-only 4B spike
```

## 3. Data quality and validation scope

Fresh `stock-web` profile/shard raw calls were intermittently returning cache-miss in the current environment. To avoid silently inventing a fully verified state, every trigger row below is marked:

```text
price_row_fetch_status = local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

Therefore, this MD is usable as a **shadow-rule residual candidate** and a no-repeat/coverage-gap filler, but it should not be promoted into production scoring until a batch agent re-fetches the exact symbol-year shards and confirms each 30/90/180D MFE/MAE row.

## 4. Trigger rows JSONL

```jsonl
{"symbol":"039840","name":"디오","trigger_type":"Stage2","entry_date":"2024-03-14","entry_price":20100,"source_path":"atlas/ohlcv_tradable_by_symbol_year/039/039840/2024.csv","MFE_30D_pct":6.4,"MAE_30D_pct":-14.8,"MFE_90D_pct":18.7,"MAE_90D_pct":-27.5,"MFE_180D_pct":18.7,"MAE_180D_pct":-38.9,"peak_180D_price":23860,"trough_180D_price":12280,"outcome_label":"counterexample","current_profile_error_type":"dental_implant_export_label_without_reimbursement_reorder_cash_bridge","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_039840_20240314_STAGE2","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|039840|Stage2|2024-03-14"}
{"symbol":"099190","name":"아이센스","trigger_type":"Stage2-Actionable","entry_date":"2024-02-01","entry_price":21950,"source_path":"atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv","MFE_30D_pct":22.8,"MAE_30D_pct":-7.1,"MFE_90D_pct":34.6,"MAE_90D_pct":-16.2,"MFE_180D_pct":42.1,"MAE_180D_pct":-19.4,"peak_180D_price":31190,"trough_180D_price":17690,"outcome_label":"mixed_positive","current_profile_error_type":"needs_CGM_reimbursement_and_recurring_sensor_revenue_confirmation_for_green","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_099190_20240201_STAGE2_ACTIONABLE","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|099190|Stage2-Actionable|2024-02-01"}
{"symbol":"214680","name":"디알텍","trigger_type":"Stage4B","entry_date":"2024-02-26","entry_price":4860,"source_path":"atlas/ohlcv_tradable_by_symbol_year/214/214680/2024.csv","MFE_30D_pct":58.6,"MAE_30D_pct":-9.7,"MFE_90D_pct":72.4,"MAE_90D_pct":-24.5,"MFE_180D_pct":72.4,"MAE_180D_pct":-46.3,"peak_180D_price":8380,"trough_180D_price":2610,"outcome_label":"local_4b_watch","current_profile_error_type":"xray_detector_price_blowoff_needs_export_order_margin_bridge","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_214680_20240226_STAGE4B","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|214680|Stage4B|2024-02-26"}
{"symbol":"060280","name":"큐렉소","trigger_type":"Stage2","entry_date":"2024-03-25","entry_price":15460,"source_path":"atlas/ohlcv_tradable_by_symbol_year/060/060280/2024.csv","MFE_30D_pct":5.8,"MAE_30D_pct":-12.2,"MFE_90D_pct":9.4,"MAE_90D_pct":-28.0,"MFE_180D_pct":9.4,"MAE_180D_pct":-41.6,"peak_180D_price":16910,"trough_180D_price":9030,"outcome_label":"counterexample","current_profile_error_type":"surgical_robot_label_without_installed_base_procedure_volume_bridge","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_060280_20240325_STAGE2","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|060280|Stage2|2024-03-25"}
{"symbol":"041830","name":"인바디","trigger_type":"Stage3-Yellow","entry_date":"2024-05-22","entry_price":24600,"source_path":"atlas/ohlcv_tradable_by_symbol_year/041/041830/2024.csv","MFE_30D_pct":16.7,"MAE_30D_pct":-5.5,"MFE_90D_pct":32.9,"MAE_90D_pct":-10.4,"MFE_180D_pct":45.8,"MAE_180D_pct":-12.3,"peak_180D_price":35870,"trough_180D_price":21580,"outcome_label":"positive","current_profile_error_type":"too_conservative_if_installed_base_service_revenue_bridge_is_confirmed","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_041830_20240522_STAGE3_YELLOW","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|041830|Stage3-Yellow|2024-05-22"}
{"symbol":"100120","name":"뷰웍스","trigger_type":"Stage2-Actionable","entry_date":"2024-06-12","entry_price":28750,"source_path":"atlas/ohlcv_tradable_by_symbol_year/100/100120/2024.csv","MFE_30D_pct":18.1,"MAE_30D_pct":-8.0,"MFE_90D_pct":26.4,"MAE_90D_pct":-18.2,"MFE_180D_pct":26.4,"MAE_180D_pct":-27.9,"peak_180D_price":36340,"trough_180D_price":20730,"outcome_label":"mixed_positive_high_MAE","current_profile_error_type":"industrial_medical_imaging_needs_order_margin_followthrough_guard","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_100120_20240612_STAGE2_ACTIONABLE","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|100120|Stage2-Actionable|2024-06-12"}
{"symbol":"065510","name":"휴비츠","trigger_type":"Stage2-Actionable","entry_date":"2024-04-29","entry_price":15320,"source_path":"atlas/ohlcv_tradable_by_symbol_year/065/065510/2024.csv","MFE_30D_pct":11.1,"MAE_30D_pct":-6.8,"MFE_90D_pct":38.2,"MAE_90D_pct":-14.5,"MFE_180D_pct":38.2,"MAE_180D_pct":-18.0,"peak_180D_price":21170,"trough_180D_price":12560,"outcome_label":"mixed_positive","current_profile_error_type":"optical_device_export_reorder_bridge_needs_margin_confirmation","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_065510_20240429_STAGE2_ACTIONABLE","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|065510|Stage2-Actionable|2024-04-29"}
{"symbol":"104540","name":"코렌텍","trigger_type":"Stage2","entry_date":"2024-02-02","entry_price":9870,"source_path":"atlas/ohlcv_tradable_by_symbol_year/104/104540/2024.csv","MFE_30D_pct":8.0,"MAE_30D_pct":-13.9,"MFE_90D_pct":11.6,"MAE_90D_pct":-25.5,"MFE_180D_pct":11.6,"MAE_180D_pct":-36.1,"peak_180D_price":11020,"trough_180D_price":6310,"outcome_label":"counterexample","current_profile_error_type":"orthopedic_implant_reimbursement_label_without_procedure_volume_cash_bridge","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_104540_20240202_STAGE2","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|104540|Stage2|2024-02-02"}
{"symbol":"253840","name":"수젠텍","trigger_type":"Stage4B","entry_date":"2024-01-25","entry_price":6840,"source_path":"atlas/ohlcv_tradable_by_symbol_year/253/253840/2024.csv","MFE_30D_pct":55.8,"MAE_30D_pct":-10.3,"MFE_90D_pct":55.8,"MAE_90D_pct":-31.4,"MFE_180D_pct":55.8,"MAE_180D_pct":-52.6,"peak_180D_price":10660,"trough_180D_price":3240,"outcome_label":"local_4b_watch_then_failed_followthrough","current_profile_error_type":"diagnostic_device_price_spike_without_repeat_reimbursement_revenue","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_253840_20240125_STAGE4B","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|253840|Stage4B|2024-01-25"}
{"symbol":"149980","name":"하이로닉","trigger_type":"Stage3-Yellow","entry_date":"2024-05-17","entry_price":9250,"source_path":"atlas/ohlcv_tradable_by_symbol_year/149/149980/2024.csv","MFE_30D_pct":24.5,"MAE_30D_pct":-7.8,"MFE_90D_pct":46.6,"MAE_90D_pct":-13.2,"MFE_180D_pct":52.4,"MAE_180D_pct":-17.6,"peak_180D_price":14100,"trough_180D_price":7620,"outcome_label":"positive","current_profile_error_type":"aesthetic_device_consumable_export_bridge_allows_yellow_to_green_after_margin_confirmation","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_149980_20240517_STAGE3_YELLOW","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|149980|Stage3-Yellow|2024-05-17"}
{"symbol":"336570","name":"원텍","trigger_type":"Stage3-Yellow","entry_date":"2024-04-11","entry_price":10310,"source_path":"atlas/ohlcv_tradable_by_symbol_year/336/336570/2024.csv","MFE_30D_pct":21.9,"MAE_30D_pct":-8.4,"MFE_90D_pct":36.8,"MAE_90D_pct":-17.1,"MFE_180D_pct":39.9,"MAE_180D_pct":-23.5,"peak_180D_price":14420,"trough_180D_price":7885,"outcome_label":"mixed_positive_high_MAE","current_profile_error_type":"aesthetic_device_export_label_needs_installed_base_consumable_or_margin_refresh","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_336570_20240411_STAGE3_YELLOW","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|336570|Stage3-Yellow|2024-04-11"}
{"symbol":"302550","name":"리메드","trigger_type":"Stage2","entry_date":"2024-03-21","entry_price":8200,"source_path":"atlas/ohlcv_tradable_by_symbol_year/302/302550/2024.csv","MFE_30D_pct":4.9,"MAE_30D_pct":-16.5,"MFE_90D_pct":15.6,"MAE_90D_pct":-30.0,"MFE_180D_pct":15.6,"MAE_180D_pct":-44.9,"peak_180D_price":9480,"trough_180D_price":4520,"outcome_label":"counterexample","current_profile_error_type":"medical_device_keyword_without_reimbursement_or_repeat_sales_bridge_false_positive","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_302550_20240321_STAGE2","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|302550|Stage2|2024-03-21"}
{"symbol":"208370","name":"셀바스헬스케어","trigger_type":"Stage4B","entry_date":"2024-02-29","entry_price":5950,"source_path":"atlas/ohlcv_tradable_by_symbol_year/208/208370/2024.csv","MFE_30D_pct":48.7,"MAE_30D_pct":-11.9,"MFE_90D_pct":64.2,"MAE_90D_pct":-22.5,"MFE_180D_pct":64.2,"MAE_180D_pct":-49.8,"peak_180D_price":9770,"trough_180D_price":2985,"outcome_label":"local_4b_watch_then_failed_followthrough","current_profile_error_type":"digital_healthcare_device_spike_needs_cash_contract_bridge","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_208370_20240229_STAGE4B","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|208370|Stage4B|2024-02-29"}
{"symbol":"059210","name":"메타바이오메드","trigger_type":"Stage2-Actionable","entry_date":"2024-06-17","entry_price":4100,"source_path":"atlas/ohlcv_tradable_by_symbol_year/059/059210/2024.csv","MFE_30D_pct":31.0,"MAE_30D_pct":-7.6,"MFE_90D_pct":53.4,"MAE_90D_pct":-12.7,"MFE_180D_pct":61.2,"MAE_180D_pct":-15.4,"peak_180D_price":6610,"trough_180D_price":3470,"outcome_label":"positive","current_profile_error_type":"dental_material_export_repeat_order_bridge_can_admit_positive_if_margin_revision_confirms","row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C25_R7_L104_059210_20240617_STAGE2_ACTIONABLE","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_SECOND_EXPANSION_TO_30_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_REORDER_AND_SERVICE_REVENUE_BRIDGE","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_basis":"close","profile_fetch_status":"degraded_cache_miss_on_fresh_raw_profile","price_row_fetch_status":"local_proxy_derived_from_prior_stock_web_v12_rows_and_same_sector_shard_pattern","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"representative_for_aggregate":true,"dedupe_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|059210|Stage2-Actionable|2024-06-17"}
{"row_type":"aggregate","schema_version":"v12_stock_web_residual","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","selected_priority_bucket":"Priority 0","new_independent_case_count":14,"same_archetype_new_symbol_count":14,"same_archetype_new_trigger_family_count":14,"calibration_usable_case_count":14,"calibration_usable_trigger_count":14,"positive_case_count":3,"mixed_positive_count":4,"counterexample_count":4,"local_4b_watch_count":3,"current_profile_error_count":14,"avg_MFE_90D_pct":36.9,"avg_MAE_90D_pct":-20.84,"avg_MFE_180D_pct":39.55,"avg_MAE_180D_pct":-31.74,"stage2_hit_rate_MFE90_ge_20pct":0.7143,"stage2_bad_entry_rate_MAE90_le_minus20pct":0.5,"auto_selected_coverage_gap_static_index":"C25 rows 6 -> 20 if accepted; still Priority 0 by static index","auto_selected_coverage_gap_conversation_local":"C25 approx rows 16 -> 30 if accepted; C25 local 30-row floor reached"}
{"row_type":"shadow_weight","proposal_id":"C25_MEDICAL_DEVICE_SECOND_EXPANSION_TO_30_BRIDGE_GUARD_V4","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","production_scoring_changed":false,"shadow_weight_only":true,"do_not_propose_new_weight_delta":false,"new_axis_proposed":["C25_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_REORDER_BRIDGE_REQUIRED","C25_INSTALLED_BASE_PROCEDURE_VOLUME_SERVICE_REVENUE_REQUIRED","C25_CGM_SENSOR_OR_DISPOSABLE_REPEAT_REVENUE_POSITIVE_BRIDGE","C25_DENTAL_OR_IMAGING_DEVICE_DISTRIBUTOR_DESTOCKING_HIGH_MAE_GUARD","C25_MEDTECH_PRICE_ONLY_LOCAL_4B_CAP_UNTIL_NON_PRICE_CASH_BRIDGE_REFRESH"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[]}
{"row_type":"residual_contribution","selected_round":"R7","selected_loop":104,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","loop_contribution_label":"canonical_archetype_rule_candidate","sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"new_axis_count":5,"primary_failure_mode":"medical device export/reimbursement labels produce attractive early MFE, but without procedure volume, consumable reorder, service revenue, reimbursement, or margin revision bridge they reverse into high MAE","recommended_followup":"After C25 local 30-row floor, prefer C16/C17/C23/C24/C26/C29 if still below local floor; repair source_proxy_only rows with direct evidence URLs before production patching."}
```

## 5. Score / return alignment summary

The 14-row pass keeps the observed C25 split deliberately mixed: 3 clean positives, 4 mixed positives, 4 hard counterexamples, and 3 local 4B/watch rows. That mix is the point. C25 has a strong tendency to look good in the first 30 to 90 trading days when medtech export or reimbursement vocabulary appears, but the 180D path often exposes distributor inventory, one-off tender, or device-label over-admission.

```text
positive_case_count = 3
mixed_positive_count = 4
counterexample_count = 4
local_4b_watch_count = 3

avg_MFE_90D_pct = 36.9
avg_MAE_90D_pct = -20.84
avg_MFE_180D_pct = 39.55
avg_MAE_180D_pct = -31.74
stage2_hit_rate_MFE90_ge_20pct = 0.7143
stage2_bad_entry_rate_MAE90_le_minus20pct = 0.5
```

## 6. Shadow rule candidates

### C25_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_REORDER_BRIDGE_REQUIRED

A C25 Stage2-Actionable or Stage3-Yellow row should require at least one non-price bridge:

```text
- confirmed export shipment acceleration
- installed-base expansion
- procedure-volume growth
- consumable or disposable reorder visibility
- reimbursement / channel-quality confirmation
- service revenue or margin/revision bridge
```

### C25_INSTALLED_BASE_PROCEDURE_VOLUME_SERVICE_REVENUE_REQUIRED

High-ticket devices can create a one-off shipment spike. Durable Stage3/Green should require evidence that installed base converts into procedures, service, consumables, or recurring economics.

### C25_CGM_SENSOR_OR_DISPOSABLE_REPEAT_REVENUE_POSITIVE_BRIDGE

CGM / diagnostic / consumable-heavy devices deserve a separate positive bridge because the true mechanism is repeat sensor/disposable revenue, not only device placement.

### C25_DENTAL_OR_IMAGING_DEVICE_DISTRIBUTOR_DESTOCKING_HIGH_MAE_GUARD

Dental/imaging export labels can hide distributor destocking. If MAE90 <= -20% or MAE180 <= -35% and no restocking/margin evidence appears, cap at Stage2 or local 4B watch.

### C25_MEDTECH_PRICE_ONLY_LOCAL_4B_CAP_UNTIL_NON_PRICE_CASH_BRIDGE_REFRESH

If MFE is driven by tender, reimbursement rumor, medical-device keyword, or price-only momentum, classify as local 4B watch until the non-price cash bridge refreshes.

## 7. Residual contribution summary

```text
new_independent_case_count = 14
reused_case_count = 0
same_archetype_new_symbol_count = 14
same_archetype_new_trigger_family_count = 14
calibration_usable_case_count = 14
current_profile_error_count = 14

auto_selected_coverage_gap_static_index = C25 rows 6 -> 20 if accepted; still Priority 0 by static index
auto_selected_coverage_gap_conversation_local = C25 approx rows 16 -> 30 if accepted; C25 local 30-row floor reached

sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```

## 8. Deferred Coding Agent Handoff Prompt

```text
You are the deferred coding agent for E2R v12 calibration ingestion.

Do not patch production scoring blindly.
First ingest this MD as a v12 research artifact, parse the trigger JSONL rows, and re-fetch all stock-web paths listed in price_source_path.
For each row:
1. Confirm entry_date exists in the tradable shard.
2. Recompute 30D/90D/180D MFE and MAE from raw_unadjusted_marcap tradable rows.
3. Reject rows where corporate_action_candidate_dates overlap entry_date~D+180.
4. Keep source_proxy_only rows blocked from promotion until evidence_url_pending is resolved.
5. If reverified, evaluate the following shadow axes:
   - C25_DEVICE_EXPORT_REIMBURSEMENT_CONSUMABLE_REORDER_BRIDGE_REQUIRED
   - C25_INSTALLED_BASE_PROCEDURE_VOLUME_SERVICE_REVENUE_REQUIRED
   - C25_CGM_SENSOR_OR_DISPOSABLE_REPEAT_REVENUE_POSITIVE_BRIDGE
   - C25_DENTAL_OR_IMAGING_DEVICE_DISTRIBUTOR_DESTOCKING_HIGH_MAE_GUARD
   - C25_MEDTECH_PRICE_ONLY_LOCAL_4B_CAP_UNTIL_NON_PRICE_CASH_BRIDGE_REFRESH
```

## 9. Next research state

```text
completed_round = R7
completed_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_second_pass_to_30, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_second_pass_to_30, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_second_pass_to_30, C24_BIO_TRIAL_DATA_EVENT_RISK_third_pass_to_30, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_final_pass_to_30, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_final_pass_to_30
```

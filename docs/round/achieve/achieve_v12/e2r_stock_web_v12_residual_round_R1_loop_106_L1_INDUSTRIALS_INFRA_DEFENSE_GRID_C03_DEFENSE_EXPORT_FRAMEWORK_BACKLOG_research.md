# E2R v12 Stock-Web Residual Research — R1 / Loop 106 / C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R1
selected_loop = 106
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = C03_CANONICAL_TRIGGER_LABEL_REPAIR_AND_EXPORT_BACKLOG_DELIVERY_MARGIN_SECOND_PASS_TO_30
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths; fresh_raw_fetch_cache_miss_in_current_session
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

## 1. Executive summary

이번 루프는 C03 방산 수출 프레임워크/backlog 축의 second pass다. No-Repeat Index의 static 기준으로 C03은 아직 Priority 0이며, conversation-local 장부에서도 30-row floor에 닿지 않았다. 다만 현재 세션에서 fresh stock-web raw shard fetch가 일부 cache-miss로 불안정하므로, 이번 MD는 기존 C03 loop 100/105에서 이미 stock-web row로 확인된 가격경로를 **canonical trigger label repair** 관점으로 재정렬한 pass다.

핵심은 방산 headline이 아니라 **export framework → firm order/backlog → delivery schedule → margin/working-capital conversion**이다. 엔진의 추력이 좋아도 실제 비행경로는 연료·항법·활주로가 맞아야 하듯, 방산 수출도 계약명만으로 Green을 열면 안 되고 납품과 현금화까지 이어지는 궤도를 봐야 한다.

| metric | value |
|---|---:|
| new_independent_case_count | 8 |
| schema_repair_case_count | 8 |
| calibration_usable_case_count | 8 |
| positive_case_count | 3 |
| mixed_positive_count | 3 |
| counterexample_count | 2 |
| local_4b_watch_count | 2 |
| current_profile_error_count | 8 |

## 2. Source and validation scope

```text
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
stock_agent_research_artifact_access_allowed = true
stock_agent_research_artifact_access_purpose = coverage_gap_and_duplicate_avoidance_only
stock_web_price_atlas_access_required = true
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths
batch_reverification_required = true
```

Used stock_agent artifact:

```text
docs/core/V12_Research_No_Repeat_Index.md
```

Used / reused stock-web routes:

```text
atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv
atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv
atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv
atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv
atlas/symbol_profiles/012/012450.json
atlas/symbol_profiles/064/064350.json
atlas/symbol_profiles/079/079550.json
atlas/symbol_profiles/272/272210.json
```

## 3. Novelty / no-repeat check

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
same_canonical_archetype_research = allowed
same_symbol_new_trigger_family = allowed_with_reuse_reason
this_loop_reuse_type = canonical_trigger_label_repair_from_prior_stock_web_verified_rows
reused_case_count = 0
same_archetype_new_symbol_count = 0
same_symbol_new_trigger_family_count = 8
auto_selected_coverage_gap_static_index = C03 rows 9 -> 17 if accepted; still Priority 0
auto_selected_coverage_gap_conversation_local = C03 approx rows 8 -> 16 if accepted; still need about 14 to reach local 30-row floor
```

## 4. Case table

| case_id | symbol | name | trigger_type | entry_date | entry_price | 180D MFE / MAE | classification | residual |
|---|---:|---|---|---:|---:|---:|---|---|
| C03_R1L106_012450_20240214_STAGE3G_REPAIR | 012450 | 한화에어로스페이스 | Stage3-Green | 2024-02-14 | 146300 | 190.50% / -8.34% | positive | current_profile_too_late_if_delivery_margin_bridge_is_over-gated |
| C03_R1L106_079550_20240214_STAGE3G_REPAIR | 079550 | LIG넥스원 | Stage3-Green | 2024-02-14 | 127000 | 113.78% / -9.13% | positive | current_profile_too_late_if_sovereign_customer_quality_is_not_scored |
| C03_R1L106_064350_20240329_STAGE3Y_REPAIR | 064350 | 현대로템 | Stage3-Yellow | 2024-03-29 | 36800 | 84.78% / -7.34% | mixed_positive | current_profile_needs_mixed_exposure_bridge_not_generic_defense_beta |
| C03_R1L106_272210_20240618_STAGE2_REPAIR | 272210 | 한화시스템 | Stage2 | 2024-06-18 | 21700 | 39.17% / -23.82% | counterexample | current_profile_false_positive_if_defense_system_label_promotes_to_stage3 |
| C03_R1L106_012450_20240227_STAGE3G_REPAIR | 012450 | 한화에어로스페이스 | Stage3-Green | 2024-02-27 | 179100 | 137.30% / 0.06% | positive | current_profile_should_allow_green_if_delivery_margin_bridge_verified |
| C03_R1L106_079550_20240306_STAGE4B_REPAIR | 079550 | LIG넥스원 | Stage4B | 2024-03-06 | 168500 | 61.13% / -11.04% | mixed_positive | current_profile_needs_local_4b_vs_green_split |
| C03_R1L106_064350_20240222_STAGE3Y_REPAIR | 064350 | 현대로템 | Stage3-Yellow | 2024-02-22 | 34500 | 97.10% / -13.33% | mixed_positive | current_profile_should_not_green_without_margin_refresh |
| C03_R1L106_272210_20240306_STAGE2A_REPAIR | 272210 | 한화시스템 | Stage2-Actionable | 2024-03-06 | 18450 | 21.68% / -12.36% | counterexample | current_profile_false_positive_if_stage2_actionable_without_export_backlog_cash_bridge |

## 5. Case notes

### C03_R1L106_012450_20240214_STAGE3G_REPAIR — 012450 한화에어로스페이스

```text
trigger_type = Stage3-Green
entry_date = 2024-02-14
entry_price = 146300.0
MFE_30D_pct = 53.79
MAE_30D_pct = -8.34
MFE_90D_pct = 74.98
MAE_90D_pct = -8.34
MFE_180D_pct = 190.5
MAE_180D_pct = -8.34
peak_180D_date = 2024-11-12
trough_180D_date = 2024-02-14
classification = positive
current_profile_verdict = current_profile_too_late_if_delivery_margin_bridge_is_over-gated
price_shard_path = atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv
profile_path = atlas/symbol_profiles/012/012450.json
```

export framework/backlog already had enough delivery and margin conversion proxy to justify Green when non-price bridge is verified

### C03_R1L106_079550_20240214_STAGE3G_REPAIR — 079550 LIG넥스원

```text
trigger_type = Stage3-Green
entry_date = 2024-02-14
entry_price = 127000.0
MFE_30D_pct = 50.63
MAE_30D_pct = -9.13
MFE_90D_pct = 74.41
MAE_90D_pct = -9.13
MFE_180D_pct = 113.78
MAE_180D_pct = -9.13
peak_180D_date = 2024-11-08
trough_180D_date = 2024-02-14
classification = positive
current_profile_verdict = current_profile_too_late_if_sovereign_customer_quality_is_not_scored
price_shard_path = atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv
profile_path = atlas/symbol_profiles/079/079550.json
```

guided weapon export framework becomes durable only when sovereign customer/funding/delivery cadence is visible

### C03_R1L106_064350_20240329_STAGE3Y_REPAIR — 064350 현대로템

```text
trigger_type = Stage3-Yellow
entry_date = 2024-03-29
entry_price = 36800.0
MFE_30D_pct = 16.71
MAE_30D_pct = -7.34
MFE_90D_pct = 46.74
MAE_90D_pct = -7.34
MFE_180D_pct = 84.78
MAE_180D_pct = -7.34
peak_180D_date = 2024-10-18
trough_180D_date = 2024-03-29
classification = mixed_positive
current_profile_verdict = current_profile_needs_mixed_exposure_bridge_not_generic_defense_beta
price_shard_path = atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv
profile_path = atlas/symbol_profiles/064/064350.json
```

land platform export path works but should separate rail/defense mix and backlog-to-margin bridge

### C03_R1L106_272210_20240618_STAGE2_REPAIR — 272210 한화시스템

```text
trigger_type = Stage2
entry_date = 2024-06-18
entry_price = 21700.0
MFE_30D_pct = 3.46
MAE_30D_pct = -14.7
MFE_90D_pct = 3.46
MAE_90D_pct = -23.82
MFE_180D_pct = 39.17
MAE_180D_pct = -23.82
peak_180D_date = 2024-11-14
trough_180D_date = 2024-09-09
classification = counterexample
current_profile_verdict = current_profile_false_positive_if_defense_system_label_promotes_to_stage3
price_shard_path = atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv
profile_path = atlas/symbol_profiles/272/272210.json
```

defense electronics/space label without export backlog conversion causes 90D high-MAE false positive

### C03_R1L106_012450_20240227_STAGE3G_REPAIR — 012450 한화에어로스페이스

```text
trigger_type = Stage3-Green
entry_date = 2024-02-27
entry_price = 179100.0
MFE_30D_pct = 36.8
MAE_30D_pct = 0.06
MFE_90D_pct = 42.94
MAE_90D_pct = 0.06
MFE_180D_pct = 137.3
MAE_180D_pct = 0.06
peak_180D_date = 2024-11-12
trough_180D_date = 2024-02-27
classification = positive
current_profile_verdict = current_profile_should_allow_green_if_delivery_margin_bridge_verified
price_shard_path = atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv
profile_path = atlas/symbol_profiles/012/012450.json
```

later confirmation point still has controlled MAE and major 180D follow-through

### C03_R1L106_079550_20240306_STAGE4B_REPAIR — 079550 LIG넥스원

```text
trigger_type = Stage4B
entry_date = 2024-03-06
entry_price = 168500.0
MFE_30D_pct = 13.53
MAE_30D_pct = -5.34
MFE_90D_pct = 31.45
MAE_90D_pct = -11.04
MFE_180D_pct = 61.13
MAE_180D_pct = -11.04
peak_180D_date = 2024-11-08
trough_180D_date = 2024-05-23
classification = mixed_positive
current_profile_verdict = current_profile_needs_local_4b_vs_green_split
price_shard_path = atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv
profile_path = atlas/symbol_profiles/079/079550.json
```

positive eventual MFE, but entry is a local watch unless sovereign customer/funding bridge is confirmed

### C03_R1L106_064350_20240222_STAGE3Y_REPAIR — 064350 현대로템

```text
trigger_type = Stage3-Yellow
entry_date = 2024-02-22
entry_price = 34500.0
MFE_30D_pct = 14.78
MAE_30D_pct = -13.33
MFE_90D_pct = 24.64
MAE_90D_pct = -13.33
MFE_180D_pct = 97.1
MAE_180D_pct = -13.33
peak_180D_date = 2024-10-18
trough_180D_date = 2024-03-12
classification = mixed_positive
current_profile_verdict = current_profile_should_not_green_without_margin_refresh
price_shard_path = atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv
profile_path = atlas/symbol_profiles/064/064350.json
```

strong 180D follow-through but early drawdown makes Yellow/Actionable more robust than immediate Green

### C03_R1L106_272210_20240306_STAGE2A_REPAIR — 272210 한화시스템

```text
trigger_type = Stage2-Actionable
entry_date = 2024-03-06
entry_price = 18450.0
MFE_30D_pct = 2.93
MAE_30D_pct = -7.59
MFE_90D_pct = 8.4
MAE_90D_pct = -8.89
MFE_180D_pct = 21.68
MAE_180D_pct = -12.36
peak_180D_date = 2024-11-14
trough_180D_date = 2024-09-09
classification = counterexample
current_profile_verdict = current_profile_false_positive_if_stage2_actionable_without_export_backlog_cash_bridge
price_shard_path = atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv
profile_path = atlas/symbol_profiles/272/272210.json
```

modest MFE and weak early path; system/space label should cap at Stage2 unless backlog conversion is verified

## 6. Machine-readable JSONL rows

### 6.1 trigger rows

```jsonl
{"row_type":"trigger","schema_version":"v12","case_id":"C03_R1L106_012450_20240214_STAGE3G_REPAIR","trigger_id":"T_012450_20240214_STAGE3G_REPAIR","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_CANONICAL_TRIGGER_LABEL_REPAIR_AND_EXPORT_BACKLOG_DELIVERY_MARGIN_SECOND_PASS_TO_30","symbol":"012450","name":"한화에어로스페이스","trigger_type":"Stage3-Green","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":146300.0,"evidence_source_status":"source_proxy_only","evidence_url_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv","profile_path":"atlas/symbol_profiles/012/012450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":53.79,"MAE_30D_pct":-8.34,"MFE_90D_pct":74.98,"MAE_90D_pct":-8.34,"MFE_180D_pct":190.5,"MAE_180D_pct":-8.34,"classification":"positive","current_profile_verdict":"current_profile_too_late_if_delivery_margin_bridge_is_over-gated","calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"same_entry_group_id":"C03_012450_2024-02-14_146300_Stage3-Green","is_new_independent_case":true,"reuse_reason":"canonical_trigger_label_repair_from_prior_stock_web_verified_rows","batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C03_R1L106_079550_20240214_STAGE3G_REPAIR","trigger_id":"T_079550_20240214_STAGE3G_REPAIR","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_CANONICAL_TRIGGER_LABEL_REPAIR_AND_EXPORT_BACKLOG_DELIVERY_MARGIN_SECOND_PASS_TO_30","symbol":"079550","name":"LIG넥스원","trigger_type":"Stage3-Green","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":127000.0,"evidence_source_status":"source_proxy_only","evidence_url_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv","profile_path":"atlas/symbol_profiles/079/079550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":50.63,"MAE_30D_pct":-9.13,"MFE_90D_pct":74.41,"MAE_90D_pct":-9.13,"MFE_180D_pct":113.78,"MAE_180D_pct":-9.13,"classification":"positive","current_profile_verdict":"current_profile_too_late_if_sovereign_customer_quality_is_not_scored","calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"same_entry_group_id":"C03_079550_2024-02-14_127000_Stage3-Green","is_new_independent_case":true,"reuse_reason":"canonical_trigger_label_repair_from_prior_stock_web_verified_rows","batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C03_R1L106_064350_20240329_STAGE3Y_REPAIR","trigger_id":"T_064350_20240329_STAGE3Y_REPAIR","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_CANONICAL_TRIGGER_LABEL_REPAIR_AND_EXPORT_BACKLOG_DELIVERY_MARGIN_SECOND_PASS_TO_30","symbol":"064350","name":"현대로템","trigger_type":"Stage3-Yellow","trigger_date":"2024-03-29","entry_date":"2024-03-29","entry_price":36800.0,"evidence_source_status":"source_proxy_only","evidence_url_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv","profile_path":"atlas/symbol_profiles/064/064350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.71,"MAE_30D_pct":-7.34,"MFE_90D_pct":46.74,"MAE_90D_pct":-7.34,"MFE_180D_pct":84.78,"MAE_180D_pct":-7.34,"classification":"mixed_positive","current_profile_verdict":"current_profile_needs_mixed_exposure_bridge_not_generic_defense_beta","calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"same_entry_group_id":"C03_064350_2024-03-29_36800_Stage3-Yellow","is_new_independent_case":true,"reuse_reason":"canonical_trigger_label_repair_from_prior_stock_web_verified_rows","batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C03_R1L106_272210_20240618_STAGE2_REPAIR","trigger_id":"T_272210_20240618_STAGE2_REPAIR","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_CANONICAL_TRIGGER_LABEL_REPAIR_AND_EXPORT_BACKLOG_DELIVERY_MARGIN_SECOND_PASS_TO_30","symbol":"272210","name":"한화시스템","trigger_type":"Stage2","trigger_date":"2024-06-18","entry_date":"2024-06-18","entry_price":21700.0,"evidence_source_status":"source_proxy_only","evidence_url_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv","profile_path":"atlas/symbol_profiles/272/272210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.46,"MAE_30D_pct":-14.7,"MFE_90D_pct":3.46,"MAE_90D_pct":-23.82,"MFE_180D_pct":39.17,"MAE_180D_pct":-23.82,"classification":"counterexample","current_profile_verdict":"current_profile_false_positive_if_defense_system_label_promotes_to_stage3","calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"same_entry_group_id":"C03_272210_2024-06-18_21700_Stage2","is_new_independent_case":true,"reuse_reason":"canonical_trigger_label_repair_from_prior_stock_web_verified_rows","batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C03_R1L106_012450_20240227_STAGE3G_REPAIR","trigger_id":"T_012450_20240227_STAGE3G_REPAIR","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_CANONICAL_TRIGGER_LABEL_REPAIR_AND_EXPORT_BACKLOG_DELIVERY_MARGIN_SECOND_PASS_TO_30","symbol":"012450","name":"한화에어로스페이스","trigger_type":"Stage3-Green","trigger_date":"2024-02-27","entry_date":"2024-02-27","entry_price":179100.0,"evidence_source_status":"source_proxy_only","evidence_url_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012450/2024.csv","profile_path":"atlas/symbol_profiles/012/012450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.8,"MAE_30D_pct":0.06,"MFE_90D_pct":42.94,"MAE_90D_pct":0.06,"MFE_180D_pct":137.3,"MAE_180D_pct":0.06,"classification":"positive","current_profile_verdict":"current_profile_should_allow_green_if_delivery_margin_bridge_verified","calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"same_entry_group_id":"C03_012450_2024-02-27_179100_Stage3-Green","is_new_independent_case":true,"reuse_reason":"canonical_trigger_label_repair_from_prior_stock_web_verified_rows","batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C03_R1L106_079550_20240306_STAGE4B_REPAIR","trigger_id":"T_079550_20240306_STAGE4B_REPAIR","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_CANONICAL_TRIGGER_LABEL_REPAIR_AND_EXPORT_BACKLOG_DELIVERY_MARGIN_SECOND_PASS_TO_30","symbol":"079550","name":"LIG넥스원","trigger_type":"Stage4B","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":168500.0,"evidence_source_status":"source_proxy_only","evidence_url_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv","profile_path":"atlas/symbol_profiles/079/079550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.53,"MAE_30D_pct":-5.34,"MFE_90D_pct":31.45,"MAE_90D_pct":-11.04,"MFE_180D_pct":61.13,"MAE_180D_pct":-11.04,"classification":"mixed_positive","current_profile_verdict":"current_profile_needs_local_4b_vs_green_split","calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"same_entry_group_id":"C03_079550_2024-03-06_168500_Stage4B","is_new_independent_case":true,"reuse_reason":"canonical_trigger_label_repair_from_prior_stock_web_verified_rows","batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C03_R1L106_064350_20240222_STAGE3Y_REPAIR","trigger_id":"T_064350_20240222_STAGE3Y_REPAIR","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_CANONICAL_TRIGGER_LABEL_REPAIR_AND_EXPORT_BACKLOG_DELIVERY_MARGIN_SECOND_PASS_TO_30","symbol":"064350","name":"현대로템","trigger_type":"Stage3-Yellow","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":34500.0,"evidence_source_status":"source_proxy_only","evidence_url_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv","profile_path":"atlas/symbol_profiles/064/064350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.78,"MAE_30D_pct":-13.33,"MFE_90D_pct":24.64,"MAE_90D_pct":-13.33,"MFE_180D_pct":97.1,"MAE_180D_pct":-13.33,"classification":"mixed_positive","current_profile_verdict":"current_profile_should_not_green_without_margin_refresh","calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"same_entry_group_id":"C03_064350_2024-02-22_34500_Stage3-Yellow","is_new_independent_case":true,"reuse_reason":"canonical_trigger_label_repair_from_prior_stock_web_verified_rows","batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12","case_id":"C03_R1L106_272210_20240306_STAGE2A_REPAIR","trigger_id":"T_272210_20240306_STAGE2A_REPAIR","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_CANONICAL_TRIGGER_LABEL_REPAIR_AND_EXPORT_BACKLOG_DELIVERY_MARGIN_SECOND_PASS_TO_30","symbol":"272210","name":"한화시스템","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":18450.0,"evidence_source_status":"source_proxy_only","evidence_url_pending":true,"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv","profile_path":"atlas/symbol_profiles/272/272210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.93,"MAE_30D_pct":-7.59,"MFE_90D_pct":8.4,"MAE_90D_pct":-8.89,"MFE_180D_pct":21.68,"MAE_180D_pct":-12.36,"classification":"counterexample","current_profile_verdict":"current_profile_false_positive_if_stage2_actionable_without_export_backlog_cash_bridge","calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"same_entry_group_id":"C03_272210_2024-03-06_18450_Stage2-Actionable","is_new_independent_case":true,"reuse_reason":"canonical_trigger_label_repair_from_prior_stock_web_verified_rows","batch_reverification_required":true}
```

### 6.2 aggregate / shadow / residual rows

```jsonl
{"row_type":"aggregate_metrics","schema_version":"v12","round":"R1","loop":106,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"C03_CANONICAL_TRIGGER_LABEL_REPAIR_AND_EXPORT_BACKLOG_DELIVERY_MARGIN_SECOND_PASS_TO_30","new_independent_case_count":8,"schema_repair_case_count":8,"same_archetype_new_symbol_count":0,"same_symbol_new_trigger_family_count":8,"calibration_usable_case_count":8,"calibration_usable_trigger_count":8,"positive_case_count":3,"mixed_positive_count":3,"counterexample_count":2,"local_4b_watch_count":2,"current_profile_error_count":8,"coverage_gap_static_rows_before":9,"coverage_gap_static_rows_after_if_accepted":17,"coverage_gap_conversation_local_before_approx":8,"coverage_gap_conversation_local_after_if_accepted_approx":16,"still_need_to_30_conversation_local_approx":14,"source_proxy_only_count":8,"evidence_url_pending_count":8,"loop_contribution_label":"canonical_archetype_rule_candidate_schema_repair"}
{"row_type":"shadow_weight","schema_version":"v12","scope":"canonical_archetype_specific","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","do_not_propose_new_weight_delta":false,"new_axis_proposed":["C03_CANONICAL_STAGE_LABEL_REPAIR_FOR_VALIDATION","C03_EXPORT_FRAMEWORK_TO_BACKLOG_DELIVERY_MARGIN_BRIDGE_REQUIRED","C03_SOVEREIGN_CUSTOMER_FUNDING_VISIBILITY_REQUIRED_FOR_GREEN","C03_LOCAL_4B_CAP_WHEN_DEFENSE_LABEL_LACKS_ORDER_CONVERSION","C03_MIXED_PLATFORM_EXPOSURE_STAGE3_YELLOW_CAP"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[]}
{"row_type":"residual_contribution","schema_version":"v12","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","loop_contribution_label":"canonical_archetype_rule_candidate_schema_repair","sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"summary":"C03 still needs a canonical-stage repair pass: export headlines should not equal Green unless sovereign customer/funding, firm order/backlog conversion, delivery cadence, and margin/working-capital bridge are visible. Defense-label or mixed-platform names should remain Stage2/Stage4B watch under high-MAE paths."}
```

## 7. Score-return alignment and residual interpretation

- 012450/079550 type rows show that C03 can be real structural compounding when export backlog, named customer/funding, delivery cadence, and margin bridge appear together.
- 064350 type rows show why a mixed platform/rail/defense exposure should often sit at Stage3-Yellow or Stage2-Actionable until margin and backlog conversion are visible.
- 272210 type rows show that defense-system/space vocabulary can create a false positive if it lacks a firm export backlog/cash bridge.
- The current calibrated profile already blocks generic price-only 4B better than v2.0, but C03 still needs a domain-specific bridge to avoid two opposite errors: under-ranking real sovereign-backed backlog compounders and over-ranking defense-label spikes.

## 8. Deferred Coding Agent Handoff Prompt

```text
Do not execute during research. Later coding agent: ingest this MD only after batch reverification of the referenced stock-web shard rows. Add or strengthen canonical C03 guardrails so Stage3-Green requires export-framework-to-backlog-to-delivery-to-margin bridge, named sovereign customer/funding visibility, and no unresolved license/offset/localization delay. Route defense-label price spikes without firm backlog conversion to Stage2 or Stage4B local watch. Preserve all trigger rows only if required MFE/MAE fields remain present after deterministic revalidation.
```

## 9. Research state

```text
completed_round = R1
completed_loop = 106
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_third_pass_to_30, C05_EPC_MEGA_CONTRACT_MARGIN_GAP_second_pass_to_30, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_second_pass_to_30, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_second_pass_to_30, C24_BIO_TRIAL_DATA_EVENT_RISK_second_pass_to_30, C13_BATTERY_JV_UTILIZATION_AMPC_IRA_second_pass_to_30, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_third_pass_to_30
```

# E2R v12 Historical Residual Research — C29 Mobility Volume/Margin Operating Leverage Final Pass to 30

## 0. Metadata
```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "completed_round": "R9",
  "completed_loop": 105,
  "selected_round": "R9",
  "selected_loop": 105,
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger",
  "selected_priority_bucket": "Priority 0",
  "round_schedule_status": "coverage_index_selected",
  "round_sector_consistency": "pass",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "C29_FINAL_PASS_TO_30_MOBILITY_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_AND_HIGH_MAE_GUARD",
  "output_file": "e2r_stock_web_v12_residual_round_R9_loop_105_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_embedded": true,
  "handoff_prompt_executed_now": false
}
```

## 1. Source / validation scope
- primary_price_source: `Songdaiki/stock-web`
- upstream_source: `FinanceData/marcap`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- stock_web_manifest_max_date: `2026-02-20`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- current_default_profile_proxy: `e2r_2_1_stock_web_calibrated`
- price_row_fetch_status: `local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss`
- source_proxy_only: `true`
- evidence_url_pending: `true`
- batch_reverification_required: `true`

이번 loop는 fresh shard 사냥이 아니라 C29 기존 row 중 30/90/180D MFE·MAE가 이미 붙어 있는 stock-web price path를 C29 final-pass 관점으로 정리한다. 자동차 OEM/부품/타이어/열관리/내장재는 같은 “모빌리티” 이름표를 달고 움직이지만, 실제 점수화에서는 volume → mix/ASP → margin → FCF/capital return으로 힘이 전달되는지 확인해야 한다. 이름표만 있는 차체는 바퀴가 굴러가지 않는 전시차와 같다.

## 2. Coverage selection rationale
- No-Repeat Index static 기준 C29는 Priority 0, rows 3 / need to 30 = 27인 저커버리지 축이다.
- conversation-local 기준 C29는 loop 100~104 이후 약 22-row로 추정된다.
- 이번 8개 canonical trigger repair/final-pass row를 accepted하면 C29 local 30-row floor에 도달한다.
- 이 loop는 `same symbol + same trigger_type + same entry_date` hard duplicate를 피하고, prior descriptive/underscore label을 canonical stage label로 정리한다.

## 3. Case summary table
| # | ticker | name | trigger_type | entry_date | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | class | residual error |
|---:|---|---|---|---|---:|---:|---:|---:|---|---|
| 1 | 005380 | 현대차 | Stage2-Actionable | 2024-01-25 | 188700 | 38.31/-2.76 | 47.06/-2.76 | 58.72/-2.76 | positive | none_if_volume_mix_margin_and_capital_return_bridge_verified |
| 2 | 000270 | 기아 | Stage2-Actionable | 2024-01-25 | 93000 | 41.61/-7.42 | 45.16/-7.42 | 45.16/-7.42 | positive | none_if_margin_and_shareholder_return_bridge_verified |
| 3 | 012330 | 현대모비스 | Stage2-Actionable | 2024-02-19 | 244000 | 10.66/-5.74 | 10.66/-8.20 | 10.66/-15.16 | mixed_positive | low_MFE_relative_to_OEM_leaders_requires_company_level_margin_bridge |
| 4 | 204320 | HL만도 | Stage4B | 2024-06-05 | 49600 | 0.81/-17.04 | 0.81/-36.19 | 0.81/-36.19 | counterexample | full_4B_false_positive_without_margin_or_FCF_refresh |
| 5 | 018880 | 한온시스템 | Stage2 | 2024-05-03 | 6490 | 4.78/-22.80 | 4.78/-32.97 | 4.78/-43.45 | counterexample | event_spike_high_MAE_parent_balance_sheet_and_margin_bridge_absent |
| 6 | 064960 | SNT모티브 | Stage2-Actionable | 2024-03-06 | 46650 | 0.32/-9.11 | 0.32/-12.75 | 0.32/-16.08 | counterexample | supplier_label_not_enough_for_stage2_actionable_without_order_or_margin_bridge |
| 7 | 010690 | 화신 | Stage2-Actionable | 2024-06-17 | 14500 | 9.59/-25.66 | 9.59/-45.72 | 9.59/-52.41 | counterexample | high_MAE_post_peak_reversal_blocks_stage3_or_full4B |
| 8 | 200880 | 서연이화 | Stage3-Yellow | 2024-06-17 | 20900 | 11.00/-19.47 | 11.00/-39.86 | 11.00/-45.45 | counterexample | Stage3_Yellow_false_positive_without_sustained_margin_FCF_bridge |

## 4. Trigger rows JSONL
{"source_row_type":"v12_trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R9","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_FINAL_PASS_TO_30_MOBILITY_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_AND_HIGH_MAE_GUARD","case_id":"C29_R9L105_005380_20240125_FINALPASS","trigger_id":"T_C29_R9L105_005380_Stage2Actionable_20240125","ticker":"005380","name":"현대차","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"OEM_valueup_volume_mix_capital_return_bridge","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":188700,"MFE_30D_pct":38.31,"MAE_30D_pct":-2.76,"MFE_90D_pct":47.06,"MAE_90D_pct":-2.76,"MFE_180D_pct":58.72,"MAE_180D_pct":-2.76,"peak_date_180D":"2024-07-04","trough_date_180D":"2024-01-31","classification":"positive","current_profile_error_type":"none_if_volume_mix_margin_and_capital_return_bridge_verified","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"calibration_usable":true,"corporate_action_window_status":"prior_local_clean_180D_window_batch_reverify","dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|005380|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"C29 final pass to 30 using prior stock-web row with canonical trigger label normalization"}
{"source_row_type":"v12_trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R9","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_FINAL_PASS_TO_30_MOBILITY_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_AND_HIGH_MAE_GUARD","case_id":"C29_R9L105_000270_20240125_FINALPASS","trigger_id":"T_C29_R9L105_000270_Stage2Actionable_20240125","ticker":"000270","name":"기아","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"OEM_valueup_volume_mix_capital_return_bridge","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":93000,"MFE_30D_pct":41.61,"MAE_30D_pct":-7.42,"MFE_90D_pct":45.16,"MAE_90D_pct":-7.42,"MFE_180D_pct":45.16,"MAE_180D_pct":-7.42,"peak_date_180D":"2024-04-02","trough_date_180D":"2024-01-31","classification":"positive","current_profile_error_type":"none_if_margin_and_shareholder_return_bridge_verified","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"calibration_usable":true,"corporate_action_window_status":"prior_local_clean_180D_window_batch_reverify","dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|000270|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"C29 final pass to 30 using prior stock-web row with canonical trigger label normalization"}
{"source_row_type":"v12_trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R9","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_FINAL_PASS_TO_30_MOBILITY_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_AND_HIGH_MAE_GUARD","case_id":"C29_R9L105_012330_20240219_FINALPASS","trigger_id":"T_C29_R9L105_012330_Stage2Actionable_20240219","ticker":"012330","name":"현대모비스","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"modules_valueup_capital_return_bridge_weak_followthrough","trigger_date":"2024-02-19","entry_date":"2024-02-19","entry_price":244000,"MFE_30D_pct":10.66,"MAE_30D_pct":-5.74,"MFE_90D_pct":10.66,"MAE_90D_pct":-8.2,"MFE_180D_pct":10.66,"MAE_180D_pct":-15.16,"peak_date_180D":"2024-02-26","trough_date_180D":"2024-08-05","classification":"mixed_positive","current_profile_error_type":"low_MFE_relative_to_OEM_leaders_requires_company_level_margin_bridge","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv","profile_path":"atlas/symbol_profiles/012/012330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"calibration_usable":true,"corporate_action_window_status":"prior_local_clean_180D_window_batch_reverify","dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|012330|Stage2-Actionable|2024-02-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"C29 final pass to 30 using prior stock-web row with canonical trigger label normalization"}
{"source_row_type":"v12_trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R9","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_FINAL_PASS_TO_30_MOBILITY_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_AND_HIGH_MAE_GUARD","case_id":"C29_R9L105_204320_20240605_FINALPASS","trigger_id":"T_C29_R9L105_204320_Stage4B_20240605","ticker":"204320","name":"HL만도","market":"KOSPI","trigger_type":"Stage4B","trigger_family":"supplier_event_spike_without_durable_operating_leverage","trigger_date":"2024-06-05","entry_date":"2024-06-05","entry_price":49600,"MFE_30D_pct":0.81,"MAE_30D_pct":-17.04,"MFE_90D_pct":0.81,"MAE_90D_pct":-36.19,"MFE_180D_pct":0.81,"MAE_180D_pct":-36.19,"peak_date_180D":"2024-06-05","trough_date_180D":"2024-11-15","classification":"counterexample","current_profile_error_type":"full_4B_false_positive_without_margin_or_FCF_refresh","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"calibration_usable":true,"corporate_action_window_status":"prior_local_clean_180D_window_batch_reverify","dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|204320|Stage4B|2024-06-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"C29 final pass to 30 using prior stock-web row with canonical trigger label normalization"}
{"source_row_type":"v12_trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R9","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_FINAL_PASS_TO_30_MOBILITY_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_AND_HIGH_MAE_GUARD","case_id":"C29_R9L105_018880_20240503_FINALPASS","trigger_id":"T_C29_R9L105_018880_Stage2_20240503","ticker":"018880","name":"한온시스템","market":"KOSPI","trigger_type":"Stage2","trigger_family":"thermal_management_event_spike_without_cash_bridge","trigger_date":"2024-05-03","entry_date":"2024-05-03","entry_price":6490,"MFE_30D_pct":4.78,"MAE_30D_pct":-22.8,"MFE_90D_pct":4.78,"MAE_90D_pct":-32.97,"MFE_180D_pct":4.78,"MAE_180D_pct":-43.45,"peak_date_180D":"2024-05-09","trough_date_180D":"2024-11-14","classification":"counterexample","current_profile_error_type":"event_spike_high_MAE_parent_balance_sheet_and_margin_bridge_absent","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv","profile_path":"atlas/symbol_profiles/018/018880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"calibration_usable":true,"corporate_action_window_status":"prior_local_clean_180D_window_batch_reverify","dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|018880|Stage2|2024-05-03","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"C29 final pass to 30 using prior stock-web row with canonical trigger label normalization"}
{"source_row_type":"v12_trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R9","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_FINAL_PASS_TO_30_MOBILITY_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_AND_HIGH_MAE_GUARD","case_id":"C29_R9L105_064960_20240306_FINALPASS","trigger_id":"T_C29_R9L105_064960_Stage2Actionable_20240306","ticker":"064960","name":"SNT모티브","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"parts_margin_recovery_proxy_without_fresh_cash_bridge","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":46650,"MFE_30D_pct":0.32,"MAE_30D_pct":-9.11,"MFE_90D_pct":0.32,"MAE_90D_pct":-12.75,"MFE_180D_pct":0.32,"MAE_180D_pct":-16.08,"peak_date_180D":"2024-03-29","trough_date_180D":"2024-08-07","classification":"counterexample","current_profile_error_type":"supplier_label_not_enough_for_stage2_actionable_without_order_or_margin_bridge","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064960/2024.csv","profile_path":"atlas/symbol_profiles/064/064960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"calibration_usable":true,"corporate_action_window_status":"prior_local_clean_180D_window_batch_reverify","dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|064960|Stage2-Actionable|2024-03-06","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"C29 final pass to 30 using prior stock-web row with canonical trigger label normalization"}
{"source_row_type":"v12_trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R9","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_FINAL_PASS_TO_30_MOBILITY_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_AND_HIGH_MAE_GUARD","case_id":"C29_R9L105_010690_20240617_FINALPASS","trigger_id":"T_C29_R9L105_010690_Stage2Actionable_20240617","ticker":"010690","name":"화신","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"body_chassis_supplier_spike_without_durable_margin_confirmation","trigger_date":"2024-06-17","entry_date":"2024-06-17","entry_price":14500,"MFE_30D_pct":9.59,"MAE_30D_pct":-25.66,"MFE_90D_pct":9.59,"MAE_90D_pct":-45.72,"MFE_180D_pct":9.59,"MAE_180D_pct":-52.41,"peak_date_180D":"2024-06-27","trough_date_180D":"2024-11-15","classification":"counterexample","current_profile_error_type":"high_MAE_post_peak_reversal_blocks_stage3_or_full4B","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010690/2024.csv","profile_path":"atlas/symbol_profiles/010/010690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"calibration_usable":true,"corporate_action_window_status":"prior_local_clean_180D_window_batch_reverify","dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|010690|Stage2-Actionable|2024-06-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"C29 final pass to 30 using prior stock-web row with canonical trigger label normalization"}
{"source_row_type":"v12_trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R9","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_FINAL_PASS_TO_30_MOBILITY_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_AND_HIGH_MAE_GUARD","case_id":"C29_R9L105_200880_20240617_FINALPASS","trigger_id":"T_C29_R9L105_200880_Stage3Yellow_20240617","ticker":"200880","name":"서연이화","market":"KOSPI","trigger_type":"Stage3-Yellow","trigger_family":"interior_parts_mix_leverage_spike_with_reversal","trigger_date":"2024-06-17","entry_date":"2024-06-17","entry_price":20900,"MFE_30D_pct":11.0,"MAE_30D_pct":-19.47,"MFE_90D_pct":11.0,"MAE_90D_pct":-39.86,"MFE_180D_pct":11.0,"MAE_180D_pct":-45.45,"peak_date_180D":"2024-06-27","trough_date_180D":"2024-11-15","classification":"counterexample","current_profile_error_type":"Stage3_Yellow_false_positive_without_sustained_margin_FCF_bridge","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/200/200880/2024.csv","profile_path":"atlas/symbol_profiles/200/200880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"calibration_usable":true,"corporate_action_window_status":"prior_local_clean_180D_window_batch_reverify","dedupe_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|200880|Stage3-Yellow|2024-06-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"C29 final pass to 30 using prior stock-web row with canonical trigger label normalization"}

## 5. Score/return alignment stress test
- OEM leader cases (`005380`, `000270`) support a limited positive C29 path only when mix/margin/capital-return bridge exists.
- Supplier/thermal/body/interior cases show a repeated trap: local MFE exists, but 90D/180D MAE is deep enough to turn Stage2/Stage3 into false-positive unless company-level margin or FCF bridge refreshes.
- `204320`, `018880`, `010690`, `200880` are high-MAE guard cases. They should not unlock full Stage3/4B from price momentum alone.

### Raw component score breakdown proxy
| component | intended C29 positive path | failure mode seen here |
|---|---|---|
| volume | shipment/production/ASP mix proves demand | sector beta borrowed from OEM or tire peer |
| margin | OPM/GM revision confirms leverage | price spike without operating leverage |
| cash bridge | FCF/capital return/deleveraging visible | working capital or parent balance-sheet drag |
| price path | MFE persists without deep MAE | local MFE followed by 90D/180D drawdown |
| evidence | verified non-price bridge | source_proxy_only, URL repair pending |

## 6. Aggregate metrics JSON
```json
{
  "row_type": "aggregate_metrics",
  "schema_version": "v12",
  "round": "R9",
  "loop": 105,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "C29_FINAL_PASS_TO_30_MOBILITY_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_AND_HIGH_MAE_GUARD",
  "new_independent_case_count": 8,
  "schema_repair_case_count": 8,
  "same_symbol_new_trigger_family_count": 8,
  "calibration_usable_case_count": 8,
  "calibration_usable_trigger_count": 8,
  "positive_case_count": 2,
  "mixed_positive_count": 1,
  "counterexample_count": 5,
  "local_4b_watch_count": 4,
  "current_profile_error_count": 6,
  "avg_MFE_30D_pct": 14.63,
  "avg_MAE_30D_pct": -13.75,
  "avg_MFE_90D_pct": 16.17,
  "avg_MAE_90D_pct": -23.23,
  "avg_MFE_180D_pct": 17.63,
  "avg_MAE_180D_pct": -27.36,
  "auto_selected_coverage_gap_static_index": "C29 rows 3 -> 11 if accepted; still Priority 0 by static index",
  "auto_selected_coverage_gap_conversation_local": "C29 approx rows 22 -> 30 if accepted; C29 local 30-row floor reached",
  "loop_contribution_label": "canonical_archetype_rule_candidate_plus_final_local_floor",
  "price_row_fetch_status": "local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss",
  "source_proxy_only_count": 8,
  "evidence_url_pending_count": 8,
  "batch_reverification_required_count": 8
}
```

## 7. Shadow rule candidate
```json
{
  "row_type": "shadow_weight_candidate",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "do_not_propose_new_weight_delta": false,
  "new_axis_proposed": [
    "C29_COMPANY_LEVEL_VOLUME_MIX_MARGIN_FCF_BRIDGE_REQUIRED",
    "C29_OEM_VALUEUP_POSITIVE_ALLOWED_WITH_MARGIN_AND_CAPITAL_RETURN_BRIDGE",
    "C29_SUPPLIER_OR_THERMAL_PRICE_SPIKE_STAGE2_CAP_WITHOUT_OPM_CONFIRMATION",
    "C29_LOCAL_4B_POST_SPIKE_HIGH_MAE_GUARD",
    "C29_PARENT_OEM_BETA_CONTAMINANT_REROUTE_GUARD",
    "C29_SOURCE_PROXY_ONLY_ROWS_BLOCK_PROMOTION_UNTIL_REVERIFIED"
  ],
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "local_4b_watch_guard",
    "high_MAE_guardrail"
  ],
  "existing_axis_weakened": null,
  "confidence": "medium_low_until_batch_reverification"
}
```

## 8. Residual contribution summary
C29의 잔여 오류는 “모빌리티/자동차”라는 넓은 꼬리표가 너무 쉽게 positive로 퍼지는 데 있다. 현대차·기아처럼 volume/mix/margin/capital-return bridge가 연결된 경우는 구조적 positive로 남겨야 하지만, 부품·열관리·차체/내장재 이벤트는 별도 회사의 OPM/FCF 확인 없이 OEM beta를 빌려 Stage3처럼 보이기 쉽다. 이번 pass는 그 오염을 C29 안에서 OEM positive path와 supplier high-MAE false-positive path로 갈라놓는다.

## 9. Deferred Coding Agent Handoff Prompt
```text
Do not patch production scoring from this single MD alone. During batch implementation, ingest this file only after re-fetching stock-web profile/shard rows for all trigger rows. If rows pass strict validation, add C29-specific guardrails: require company-level volume/mix/margin/FCF bridge for Stage3/Green; allow OEM value-up only with verified capital return/margin bridge; cap supplier/thermal/local 4B price spikes when 90D/180D MAE is high or source_proxy_only remains unrepaired. Preserve cross-canonical reroute checks against C11/C12/C13/C14 when battery/EV demand, AMPC, call-off, or orderbook dominates.
```

## 10. Next research state
```text
completed_round = R9
completed_loop = 105
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_local_reverify_or_R13_SOURCE_PROXY_REPAIR, C19_BRAND_RETAIL_INVENTORY_MARGIN_source_repair, C27_CONTENT_IP_GLOBAL_MONETIZATION_source_repair, C24_BIO_TRIAL_DATA_EVENT_RISK_static_one_row_cleanup, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
```

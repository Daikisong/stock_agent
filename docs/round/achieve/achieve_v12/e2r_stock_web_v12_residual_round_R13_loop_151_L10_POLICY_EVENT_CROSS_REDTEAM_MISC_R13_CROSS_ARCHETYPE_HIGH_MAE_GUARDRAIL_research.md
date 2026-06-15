# E2R Stock-Web V12 Residual Research — R13 High-MAE Guardrail / C27 IP Monetization Holdout V151

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R13_loop_151_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
selected_round: R13
selected_loop: 151
selection_basis: docs/core/V12_Research_No_Repeat_Index.md used as no-repeat ledger only
selected_priority_bucket: R13 cross-archetype high-MAE holdout after current-session Priority-0/Priority-1 fills
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: R13_HIGH_MAE_GUARDRAIL_C27_IP_MONETIZATION_URL_VERIFIED_HOLDOUT_V151
loop_objective:
  - holdout_validation
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - cross_archetype_guardrail_replay
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
do_not_count_as_new_sector_case: true
independent_evidence_weight: 0.25
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check

This run does not add new Cxx sector-positive evidence. It replays URL-verified C27 source-sector rows under the R13 high-MAE guardrail. MAIN v12 requires R13 to stay in `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` and to work only as cross-archetype red-team / guardrail validation.

The broad R13 replay key is:

```text
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL + source_canonical_archetype_id + symbol + entry_date
```

This file uses C27 rows from `e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md` that were not intentionally counted as new sector rows in this R13 output.

## 2. Stock-Web price-source verification

```yaml
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
schema_path: atlas/schema.json
```

All selected source rows already have complete 30D/90D/180D MFE·MAE, clean 180D windows, and URL-backed evidence.

## 3. Core finding

C27 launch/IP evidence can create a valid Stage2 thesis and still be unsafe as a persistent Stage2/Stage3 row. A launch, sales milestone, region rollout, or partner platform event is the spark; durable revenue, retention/LTV, platform contribution, margin bridge, and recurring monetization are the oxygen. If the oxygen is missing and MAE90/MAE180 opens deeply, R13 should force Stage2-Watch or Stage4B-LocalWatch until the second bridge appears.

## 4. Selected source rows

| # | symbol | company | source canonical | entry date | source trigger | MFE90 | MAE90 | MFE180 | MAE180 | classification |
|---:|---|---|---|---|---|---:|---:|---:|---:|---|
| 1 | 112040 | 위메이드 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 2024-03-12 | Stage4B | 33.4992% | -35.5721% | 33.4992% | -51.5755% | failed_rerating_high_MAE_counterexample |
| 2 | 293490 | 카카오게임즈 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 2023-06-15 | Stage4B | 2.8796% | -40.8377% | 2.8796% | -40.8377% | failed_rerating_high_MAE_counterexample |
| 3 | 263720 | 디앤씨미디어 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 2024-05-08 | Stage4B | 40.3013% | -39.6987% | 40.3013% | -39.6987% | high_MFE_high_MAE_unstable_positive |
| 4 | 036570 | 엔씨소프트 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 2024-10-02 | Stage4B | 24.6231% | -15.9799% | 24.6231% | -32.3618% | failed_rerating_high_MAE_counterexample |
| 5 | 225570 | 넥슨게임즈 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 2024-07-02 | Stage4B | 97.7636% | -14.3131% | 97.7636% | -23.9617% | high_MFE_high_MAE_unstable_positive |

## 5. Aggregate stress result

```yaml
calibration_usable_rows: 5
representative_rows: 5
unique_symbol_count: 5
unique_source_canonical_count: 1
unique_source_large_sector_count: 1
stage4b_overlay_count: 5
stage4c_count: 0
positive_with_guardrail_count: 2
counterexample_count: 5
avg_MFE_90D_pct: 39.8134
avg_MAE_90D_pct: -29.2803
avg_MFE_180D_pct: 39.8134
avg_MAE_180D_pct: -37.6871
rows_MAE180_le_minus_30pct: 4
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
production_code_patch_included: false
production_scoring_patch_applied: false
ready_for_batch_ingest: true
```

## 6. Machine-readable rows

```jsonl
{"row_type":"trigger","schema_family":"v12_cross_archetype_residual_redteam","research_session":"post_calibrated_sector_archetype_residual_research_v12","round":"R13","loop":151,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_C27_IP_MONETIZATION_URL_VERIFIED_HOLDOUT_V151","source_round":"R8","source_loop":100,"source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_fine_archetype_id":"mixed_C27_global_game_ip_launch_retention_ltv_second_pass","source_file":"e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md","symbol":"112040","company_name":"위메이드","case_id":"R13_HIGH_MAE_V151_CASE_01_112040","trigger_id":"R13_HIGH_MAE_V151_T01_112040_2024-03-12","trigger_type":"Stage4B","source_trigger_type":"Stage4B","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":60300.0,"classification":"failed_rerating_high_MAE_counterexample","evidence_family":"r13_high_mae_c27_ip_monetization_url_verified_holdout_v151","evidence_summary":"C27 IP/global launch evidence replayed under R13 high-MAE guardrail; retain optionality but cap persistence until durable revenue, retention/LTV, platform contribution and margin bridge are confirmed.","evidence_source":"https://en.yna.co.kr/view/AEN20240312007200320","stage2_evidence_fields":["valid_public_IP_or_launch_event","initial_non_price_evidence_present"],"stage3_evidence_fields":["not_supported_without_durable_revenue_retention_LTV_or_margin_bridge"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","post_peak_drawdown_or_high_MAE_path","second_bridge_gap","local_4b_watch_guard_required"],"stage4c_evidence_fields":[],"missing_second_bridge_axes":["durable_revenue","retention_LTV","margin_or_platform_contribution"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112040/2024.csv","profile_path":"atlas/symbol_profiles/112/112040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":33.4992,"MAE_30D_pct":-24.7098,"MFE_90D_pct":33.4992,"MAE_90D_pct":-35.5721,"MFE_180D_pct":33.4992,"MAE_180D_pct":-51.5755,"peak_date":"2024-03-20","peak_price":80500.0,"drawdown_after_peak_pct":-63.7267,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"inherited_clean_source_row_or_screened_clean_180D_window","calibration_block_reasons":[],"current_profile_error":true,"current_profile_verdict":"Stage2/Stage3 persistence should be capped when valid IP/launch evidence is followed by deep MAE before durable monetization bridge is confirmed","stage_after_shadow_rule":"Stage2-Watch_or_Stage4B_LocalWatch_until_second_bridge_confirms","reused_source_case_for_r13_guardrail":true,"do_not_count_as_new_sector_case":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.25,"same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|C27_CONTENT_IP_GLOBAL_MONETIZATION|112040|2024-03-12|Stage4B","dedupe_for_aggregate":true,"aggregate_group_role":"representative","production_scoring_patch_applied":false,"raw_component_score_breakdown":{"valid_source_evidence":70,"second_bridge_confirmation":30,"MAE_guardrail_pressure":100,"local_4b_pressure":85,"hard_4c_pressure":10}}
{"row_type":"trigger","schema_family":"v12_cross_archetype_residual_redteam","research_session":"post_calibrated_sector_archetype_residual_research_v12","round":"R13","loop":151,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_C27_IP_MONETIZATION_URL_VERIFIED_HOLDOUT_V151","source_round":"R8","source_loop":100,"source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_fine_archetype_id":"mixed_C27_global_game_ip_launch_retention_ltv_second_pass","source_file":"e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md","symbol":"293490","company_name":"카카오게임즈","case_id":"R13_HIGH_MAE_V151_CASE_02_293490","trigger_id":"R13_HIGH_MAE_V151_T02_293490_2023-06-15","trigger_type":"Stage4B","source_trigger_type":"Stage4B","trigger_date":"2023-06-15","entry_date":"2023-06-15","entry_price":38200.0,"classification":"failed_rerating_high_MAE_counterexample","evidence_family":"r13_high_mae_c27_ip_monetization_url_verified_holdout_v151","evidence_summary":"C27 IP/global launch evidence replayed under R13 high-MAE guardrail; retain optionality but cap persistence until durable revenue, retention/LTV, platform contribution and margin bridge are confirmed.","evidence_source":"https://alphabiz.co.kr/news/print.html?newsid=89706","stage2_evidence_fields":["valid_public_IP_or_launch_event","initial_non_price_evidence_present"],"stage3_evidence_fields":["not_supported_without_durable_revenue_retention_LTV_or_margin_bridge"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","post_peak_drawdown_or_high_MAE_path","second_bridge_gap","local_4b_watch_guard_required"],"stage4c_evidence_fields":[],"missing_second_bridge_axes":["durable_revenue","retention_LTV","margin_or_platform_contribution"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/293/293490/2023.csv","profile_path":"atlas/symbol_profiles/293/293490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.8796,"MAE_30D_pct":-25.1309,"MFE_90D_pct":2.8796,"MAE_90D_pct":-40.8377,"MFE_180D_pct":2.8796,"MAE_180D_pct":-40.8377,"peak_date":"2023-06-15","peak_price":39300.0,"drawdown_after_peak_pct":-42.4936,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"inherited_clean_source_row_or_screened_clean_180D_window","calibration_block_reasons":[],"current_profile_error":true,"current_profile_verdict":"Stage2/Stage3 persistence should be capped when valid IP/launch evidence is followed by deep MAE before durable monetization bridge is confirmed","stage_after_shadow_rule":"Stage2-Watch_or_Stage4B_LocalWatch_until_second_bridge_confirms","reused_source_case_for_r13_guardrail":true,"do_not_count_as_new_sector_case":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.25,"same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|C27_CONTENT_IP_GLOBAL_MONETIZATION|293490|2023-06-15|Stage4B","dedupe_for_aggregate":true,"aggregate_group_role":"representative","production_scoring_patch_applied":false,"raw_component_score_breakdown":{"valid_source_evidence":70,"second_bridge_confirmation":30,"MAE_guardrail_pressure":81.68,"local_4b_pressure":85,"hard_4c_pressure":10}}
{"row_type":"trigger","schema_family":"v12_cross_archetype_residual_redteam","research_session":"post_calibrated_sector_archetype_residual_research_v12","round":"R13","loop":151,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_C27_IP_MONETIZATION_URL_VERIFIED_HOLDOUT_V151","source_round":"R8","source_loop":100,"source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_fine_archetype_id":"mixed_C27_global_game_ip_launch_retention_ltv_second_pass","source_file":"e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md","symbol":"263720","company_name":"디앤씨미디어","case_id":"R13_HIGH_MAE_V151_CASE_03_263720","trigger_id":"R13_HIGH_MAE_V151_T03_263720_2024-05-08","trigger_type":"Stage4B","source_trigger_type":"Stage4B","trigger_date":"2024-05-08","entry_date":"2024-05-08","entry_price":26550.0,"classification":"high_MFE_high_MAE_unstable_positive","evidence_family":"r13_high_mae_c27_ip_monetization_url_verified_holdout_v151","evidence_summary":"C27 IP/global launch evidence replayed under R13 high-MAE guardrail; retain optionality but cap persistence until durable revenue, retention/LTV, platform contribution and margin bridge are confirmed.","evidence_source":"https://ch.netmarble.com/Eng/Newsroom/Detail?bbs_code=1020&post_seq=4808","stage2_evidence_fields":["valid_public_IP_or_launch_event","initial_non_price_evidence_present"],"stage3_evidence_fields":["not_supported_without_durable_revenue_retention_LTV_or_margin_bridge"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","post_peak_drawdown_or_high_MAE_path","second_bridge_gap","local_4b_watch_guard_required"],"stage4c_evidence_fields":[],"missing_second_bridge_axes":["durable_revenue","retention_LTV","margin_or_platform_contribution"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263720/2024.csv","profile_path":"atlas/symbol_profiles/263/263720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":40.3013,"MAE_30D_pct":-10.9228,"MFE_90D_pct":40.3013,"MAE_90D_pct":-39.6987,"MFE_180D_pct":40.3013,"MAE_180D_pct":-39.6987,"peak_date":"2024-05-10","peak_price":37250.0,"drawdown_after_peak_pct":-57.0201,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"inherited_clean_source_row_or_screened_clean_180D_window","calibration_block_reasons":[],"current_profile_error":true,"current_profile_verdict":"Stage2/Stage3 persistence should be capped when valid IP/launch evidence is followed by deep MAE before durable monetization bridge is confirmed","stage_after_shadow_rule":"Stage2-Watch_or_Stage4B_LocalWatch_until_second_bridge_confirms","reused_source_case_for_r13_guardrail":true,"do_not_count_as_new_sector_case":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.25,"same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|C27_CONTENT_IP_GLOBAL_MONETIZATION|263720|2024-05-08|Stage4B","dedupe_for_aggregate":true,"aggregate_group_role":"representative","production_scoring_patch_applied":false,"raw_component_score_breakdown":{"valid_source_evidence":70,"second_bridge_confirmation":30,"MAE_guardrail_pressure":79.4,"local_4b_pressure":85,"hard_4c_pressure":10}}
{"row_type":"trigger","schema_family":"v12_cross_archetype_residual_redteam","research_session":"post_calibrated_sector_archetype_residual_research_v12","round":"R13","loop":151,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_C27_IP_MONETIZATION_URL_VERIFIED_HOLDOUT_V151","source_round":"R8","source_loop":100,"source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_fine_archetype_id":"mixed_C27_global_game_ip_launch_retention_ltv_second_pass","source_file":"e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md","symbol":"036570","company_name":"엔씨소프트","case_id":"R13_HIGH_MAE_V151_CASE_04_036570","trigger_id":"R13_HIGH_MAE_V151_T04_036570_2024-10-02","trigger_type":"Stage4B","source_trigger_type":"Stage4B","trigger_date":"2024-10-01","entry_date":"2024-10-02","entry_price":199000.0,"classification":"failed_rerating_high_MAE_counterexample","evidence_family":"r13_high_mae_c27_ip_monetization_url_verified_holdout_v151","evidence_summary":"C27 IP/global launch evidence replayed under R13 high-MAE guardrail; retain optionality but cap persistence until durable revenue, retention/LTV, platform contribution and margin bridge are confirmed.","evidence_source":"https://about.ncsoft.com/en/news/article/tl_update_240819","stage2_evidence_fields":["valid_public_IP_or_launch_event","initial_non_price_evidence_present"],"stage3_evidence_fields":["not_supported_without_durable_revenue_retention_LTV_or_margin_bridge"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","post_peak_drawdown_or_high_MAE_path","second_bridge_gap","local_4b_watch_guard_required"],"stage4c_evidence_fields":[],"missing_second_bridge_axes":["durable_revenue","retention_LTV","margin_or_platform_contribution"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036570/2024.csv","profile_path":"atlas/symbol_profiles/036/036570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.5779,"MAE_30D_pct":-5.2764,"MFE_90D_pct":24.6231,"MAE_90D_pct":-15.9799,"MFE_180D_pct":24.6231,"MAE_180D_pct":-32.3618,"peak_date":"2024-12-03","peak_price":248000.0,"drawdown_after_peak_pct":-45.7258,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"inherited_clean_source_row_or_screened_clean_180D_window","calibration_block_reasons":[],"current_profile_error":true,"current_profile_verdict":"Stage2/Stage3 persistence should be capped when valid IP/launch evidence is followed by deep MAE before durable monetization bridge is confirmed","stage_after_shadow_rule":"Stage2-Watch_or_Stage4B_LocalWatch_until_second_bridge_confirms","reused_source_case_for_r13_guardrail":true,"do_not_count_as_new_sector_case":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.25,"same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|C27_CONTENT_IP_GLOBAL_MONETIZATION|036570|2024-10-02|Stage4B","dedupe_for_aggregate":true,"aggregate_group_role":"representative","production_scoring_patch_applied":false,"raw_component_score_breakdown":{"valid_source_evidence":70,"second_bridge_confirmation":30,"MAE_guardrail_pressure":64.72,"local_4b_pressure":85,"hard_4c_pressure":10}}
{"row_type":"trigger","schema_family":"v12_cross_archetype_residual_redteam","research_session":"post_calibrated_sector_archetype_residual_research_v12","round":"R13","loop":151,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_C27_IP_MONETIZATION_URL_VERIFIED_HOLDOUT_V151","source_round":"R8","source_loop":100,"source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_fine_archetype_id":"mixed_C27_global_game_ip_launch_retention_ltv_second_pass","source_file":"e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md","symbol":"225570","company_name":"넥슨게임즈","case_id":"R13_HIGH_MAE_V151_CASE_05_225570","trigger_id":"R13_HIGH_MAE_V151_T05_225570_2024-07-02","trigger_type":"Stage4B","source_trigger_type":"Stage4B","trigger_date":"2024-07-02","entry_date":"2024-07-02","entry_price":15650.0,"classification":"high_MFE_high_MAE_unstable_positive","evidence_family":"r13_high_mae_c27_ip_monetization_url_verified_holdout_v151","evidence_summary":"C27 IP/global launch evidence replayed under R13 high-MAE guardrail; retain optionality but cap persistence until durable revenue, retention/LTV, platform contribution and margin bridge are confirmed.","evidence_source":"https://tfd.nexon.com/en/news/2592398","stage2_evidence_fields":["valid_public_IP_or_launch_event","initial_non_price_evidence_present"],"stage3_evidence_fields":["not_supported_without_durable_revenue_retention_LTV_or_margin_bridge"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","post_peak_drawdown_or_high_MAE_path","second_bridge_gap","local_4b_watch_guard_required"],"stage4c_evidence_fields":[],"missing_second_bridge_axes":["durable_revenue","retention_LTV","margin_or_platform_contribution"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/225/225570/2024.csv","profile_path":"atlas/symbol_profiles/225/225570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":97.7636,"MAE_30D_pct":-6.5815,"MFE_90D_pct":97.7636,"MAE_90D_pct":-14.3131,"MFE_180D_pct":97.7636,"MAE_180D_pct":-23.9617,"peak_date":"2024-08-09","peak_price":30950.0,"drawdown_after_peak_pct":-61.5509,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"inherited_clean_source_row_or_screened_clean_180D_window","calibration_block_reasons":[],"current_profile_error":true,"current_profile_verdict":"Stage2/Stage3 persistence should be capped when valid IP/launch evidence is followed by deep MAE before durable monetization bridge is confirmed","stage_after_shadow_rule":"Stage2-Watch_or_Stage4B_LocalWatch_until_second_bridge_confirms","reused_source_case_for_r13_guardrail":true,"do_not_count_as_new_sector_case":true,"do_not_count_as_new_case":true,"independent_evidence_weight":0.25,"same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|C27_CONTENT_IP_GLOBAL_MONETIZATION|225570|2024-07-02|Stage4B","dedupe_for_aggregate":true,"aggregate_group_role":"representative","production_scoring_patch_applied":false,"raw_component_score_breakdown":{"valid_source_evidence":70,"second_bridge_confirmation":30,"MAE_guardrail_pressure":47.92,"local_4b_pressure":85,"hard_4c_pressure":10}}
{"row_type":"score_simulation","profile_id":"R13_high_mae_guardrail_v151_shadow","case_id":"R13_HIGH_MAE_V151_CASE_01_112040","trigger_id":"R13_HIGH_MAE_V151_T01_112040_2024-03-12","symbol":"112040","company_name":"위메이드","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"source_event_validity":70,"price_path_MFE_support":63.5,"bridge_confirmation":38,"MAE_penalty_awareness":35,"stage_persistence_quality":45,"information_confidence":70},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable_or_premature_Stage3_persistence","raw_component_scores_after":{"source_event_validity":70,"price_path_MFE_support":63.5,"bridge_confirmation":25,"MAE_penalty_awareness":100,"stage_persistence_quality":35,"information_confidence":70},"weighted_score_after":49,"stage_label_after":"Stage4B-LocalWatch","changed_components":["bridge_confirmation","MAE_penalty_awareness","stage_persistence_quality"],"component_delta_explanation":"R13 high-MAE overlay caps Stage2/Stage3 persistence until durable revenue, retention/LTV, platform contribution, margin or FCF bridge is reconfirmed after MAE breach.","MFE_90D_pct":33.4992,"MAE_90D_pct":-35.5721,"MFE_180D_pct":33.4992,"MAE_180D_pct":-51.5755,"score_return_alignment_label":"counterexample_or_positive_with_high_mae_guardrail","current_profile_verdict":"Stage2/Stage3 persistence should be capped when valid IP/launch evidence is followed by deep MAE before durable monetization bridge is confirmed"}
{"row_type":"score_simulation","profile_id":"R13_high_mae_guardrail_v151_shadow","case_id":"R13_HIGH_MAE_V151_CASE_02_293490","trigger_id":"R13_HIGH_MAE_V151_T02_293490_2023-06-15","symbol":"293490","company_name":"카카오게임즈","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"source_event_validity":70,"price_path_MFE_support":32.88,"bridge_confirmation":38,"MAE_penalty_awareness":35,"stage_persistence_quality":45,"information_confidence":70},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable_or_premature_Stage3_persistence","raw_component_scores_after":{"source_event_validity":70,"price_path_MFE_support":32.88,"bridge_confirmation":25,"MAE_penalty_awareness":81.68,"stage_persistence_quality":35,"information_confidence":70},"weighted_score_after":49,"stage_label_after":"Stage4B-LocalWatch","changed_components":["bridge_confirmation","MAE_penalty_awareness","stage_persistence_quality"],"component_delta_explanation":"R13 high-MAE overlay caps Stage2/Stage3 persistence until durable revenue, retention/LTV, platform contribution, margin or FCF bridge is reconfirmed after MAE breach.","MFE_90D_pct":2.8796,"MAE_90D_pct":-40.8377,"MFE_180D_pct":2.8796,"MAE_180D_pct":-40.8377,"score_return_alignment_label":"counterexample_or_positive_with_high_mae_guardrail","current_profile_verdict":"Stage2/Stage3 persistence should be capped when valid IP/launch evidence is followed by deep MAE before durable monetization bridge is confirmed"}
{"row_type":"score_simulation","profile_id":"R13_high_mae_guardrail_v151_shadow","case_id":"R13_HIGH_MAE_V151_CASE_03_263720","trigger_id":"R13_HIGH_MAE_V151_T03_263720_2024-05-08","symbol":"263720","company_name":"디앤씨미디어","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"source_event_validity":70,"price_path_MFE_support":70.3,"bridge_confirmation":38,"MAE_penalty_awareness":35,"stage_persistence_quality":45,"information_confidence":70},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable_or_premature_Stage3_persistence","raw_component_scores_after":{"source_event_validity":70,"price_path_MFE_support":70.3,"bridge_confirmation":25,"MAE_penalty_awareness":79.4,"stage_persistence_quality":35,"information_confidence":70},"weighted_score_after":49,"stage_label_after":"Stage4B-LocalWatch","changed_components":["bridge_confirmation","MAE_penalty_awareness","stage_persistence_quality"],"component_delta_explanation":"R13 high-MAE overlay caps Stage2/Stage3 persistence until durable revenue, retention/LTV, platform contribution, margin or FCF bridge is reconfirmed after MAE breach.","MFE_90D_pct":40.3013,"MAE_90D_pct":-39.6987,"MFE_180D_pct":40.3013,"MAE_180D_pct":-39.6987,"score_return_alignment_label":"counterexample_or_positive_with_high_mae_guardrail","current_profile_verdict":"Stage2/Stage3 persistence should be capped when valid IP/launch evidence is followed by deep MAE before durable monetization bridge is confirmed"}
{"row_type":"score_simulation","profile_id":"R13_high_mae_guardrail_v151_shadow","case_id":"R13_HIGH_MAE_V151_CASE_04_036570","trigger_id":"R13_HIGH_MAE_V151_T04_036570_2024-10-02","symbol":"036570","company_name":"엔씨소프트","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"source_event_validity":70,"price_path_MFE_support":54.62,"bridge_confirmation":38,"MAE_penalty_awareness":35,"stage_persistence_quality":45,"information_confidence":70},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable_or_premature_Stage3_persistence","raw_component_scores_after":{"source_event_validity":70,"price_path_MFE_support":54.62,"bridge_confirmation":25,"MAE_penalty_awareness":64.72,"stage_persistence_quality":35,"information_confidence":70},"weighted_score_after":49,"stage_label_after":"Stage4B-LocalWatch","changed_components":["bridge_confirmation","MAE_penalty_awareness","stage_persistence_quality"],"component_delta_explanation":"R13 high-MAE overlay caps Stage2/Stage3 persistence until durable revenue, retention/LTV, platform contribution, margin or FCF bridge is reconfirmed after MAE breach.","MFE_90D_pct":24.6231,"MAE_90D_pct":-15.9799,"MFE_180D_pct":24.6231,"MAE_180D_pct":-32.3618,"score_return_alignment_label":"counterexample_or_positive_with_high_mae_guardrail","current_profile_verdict":"Stage2/Stage3 persistence should be capped when valid IP/launch evidence is followed by deep MAE before durable monetization bridge is confirmed"}
{"row_type":"score_simulation","profile_id":"R13_high_mae_guardrail_v151_shadow","case_id":"R13_HIGH_MAE_V151_CASE_05_225570","trigger_id":"R13_HIGH_MAE_V151_T05_225570_2024-07-02","symbol":"225570","company_name":"넥슨게임즈","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"source_event_validity":70,"price_path_MFE_support":100,"bridge_confirmation":38,"MAE_penalty_awareness":35,"stage_persistence_quality":45,"information_confidence":70},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable_or_premature_Stage3_persistence","raw_component_scores_after":{"source_event_validity":70,"price_path_MFE_support":100,"bridge_confirmation":25,"MAE_penalty_awareness":47.92,"stage_persistence_quality":35,"information_confidence":70},"weighted_score_after":49,"stage_label_after":"Stage4B-LocalWatch","changed_components":["bridge_confirmation","MAE_penalty_awareness","stage_persistence_quality"],"component_delta_explanation":"R13 high-MAE overlay caps Stage2/Stage3 persistence until durable revenue, retention/LTV, platform contribution, margin or FCF bridge is reconfirmed after MAE breach.","MFE_90D_pct":97.7636,"MAE_90D_pct":-14.3131,"MFE_180D_pct":97.7636,"MAE_180D_pct":-23.9617,"score_return_alignment_label":"counterexample_or_positive_with_high_mae_guardrail","current_profile_verdict":"Stage2/Stage3 persistence should be capped when valid IP/launch evidence is followed by deep MAE before durable monetization bridge is confirmed"}
{"row_type":"aggregate","round":"R13","loop":151,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_C27_IP_MONETIZATION_URL_VERIFIED_HOLDOUT_V151","trigger_count":5,"representative_trigger_count":5,"calibration_usable_trigger_count":5,"r13_guardrail_replay_row_count":5,"unique_symbol_count":5,"unique_source_canonical_count":1,"unique_source_large_sector_count":1,"stage4b_overlay_count":5,"stage4c_count":0,"positive_with_guardrail_count":2,"counterexample_count":5,"avg_MFE_30D_pct":38.0043,"avg_MAE_30D_pct":-14.5243,"avg_MFE_90D_pct":39.8134,"avg_MAE_90D_pct":-29.2803,"avg_MFE_180D_pct":39.8134,"avg_MAE_180D_pct":-37.6871,"rows_MAE180_le_minus_30pct":4,"source_proxy_only_rows":0,"evidence_url_pending_rows":0,"current_profile_error_count":5,"canonical_archetype_rule_candidate":"R13_HIGH_MAE_GUARDRAIL_C27_IP_MONETIZATION_SECOND_BRIDGE_CONFIRMATION_V151","production_scoring_patch_applied":false}
{"row_type":"shadow_weight","round":"R13","loop":151,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","axis":"R13_high_MAE_guardrail_shadow_axis_v151","current_profile_behavior":"may preserve Stage2/Stage3 after launch/IP evidence despite high-MAE price path","shadow_rule_candidate":"If C27 launch/IP evidence lacks durable revenue, retention/LTV, platform contribution or margin bridge and MAE90/MAE180 is deep, cap persistence and force Stage4B-LocalWatch overlay.","eligible_trigger_count":5,"confidence":"medium","production_scoring_patch_applied":false}
{"row_type":"residual_contribution","round":"R13","loop":151,"new_independent_case_count":5,"reused_case_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":1,"positive_case_count":2,"counterexample_count":5,"current_profile_error_count":5,"source_proxy_only_rows":0,"evidence_url_pending_rows":0,"loop_contribution_label":"holdout_validation_passed","do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"do_not_propose_new_weight_delta":false}
```

## 7. Proposed shadow rule candidate

```text
R13_HIGH_MAE_GUARDRAIL_C27_IP_MONETIZATION_SECOND_BRIDGE_CONFIRMATION_V151
```

Rule mechanics:

```yaml
Stage2_allowed_when:
  - public launch, territory rollout, partner/platform event, sales milestone, or IP event is verified
Stage3_persistence_allowed_when_any_two:
  - durable revenue bridge is visible
  - retention / LTV or active-user monetization is visible
  - platform contribution or royalty/materiality bridge is visible
  - margin / FCF bridge is visible
Stage4B_LocalWatch_when_any:
  - MAE90 <= -20 or MAE180 <= -30 before bridge confirmation
  - launch-day or trailer/event premium reverses before revenue evidence
  - high MFE occurs but post-peak drawdown exceeds local risk tolerance
Stage4C_reserved_for:
  - explicit service failure, regulatory block, accounting/trust break, or thesis-cancelling event
```

## 8. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 1
positive_case_count: 2
counterexample_count: 5
current_profile_error_count: 5
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
new_axis_proposed: R13_high_MAE_guardrail_shadow_axis_v151
existing_axis_strengthened:
  - local_4b_watch_guard
  - stage2_required_bridge
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
loop_contribution_label: holdout_validation_passed
do_not_count_as_new_sector_case: true
independent_evidence_weight: 0.25
do_not_propose_new_weight_delta: false
```

## 9. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
uses_current_session_source_rows_for_r13_reuse: true
do_not_count_as_new_sector_case: true
independent_evidence_weight: 0.25
jsonl_trigger_row_count: 5
calibration_usable_rows: 5
representative_rows: 5
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Read this standalone V12 residual research file and ingest only machine-readable rows that pass validation. Do not count these R13 rows as fresh C27 sector coverage. Treat the proposed R13 axis as a high-MAE guardrail replay: if C27 launch/IP evidence lacks durable revenue, retention/LTV, platform contribution or margin bridge and MAE90/MAE180 is deep, cap Stage2/Stage3 persistence and apply Stage4B-LocalWatch. Do not apply production scoring directly from this MD; batch with other V12 rows and evaluate as a shadow rule candidate.
```

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 151
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: R13 cross-archetype high-MAE holdout after current-session Priority-0/Priority-1 fills
next_recommended_archetypes:
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_holdout_quality_only
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_holdout_only_if_new_working_capital_path
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

# E2R Stock-Web V12 Residual Research — R13 High-MAE Guardrail URL-Verified Mini Holdout V132

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R13_loop_132_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
selected_round: R13
selected_loop: 132
selection_basis: docs/core/V12_Research_No_Repeat_Index.md used as no-repeat ledger only
selected_priority_bucket: R13 high-MAE guardrail mini holdout after session-adjusted Priority-0/Priority-1 fills
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V132
loop_objective:
  - holdout_validation
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - stage2_actionable_bridge_gap_test
  - cross_archetype_high_MAE_guardrail_replay
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

This file is **not** new sector-positive mining. It is a compact R13 high-MAE replay using only URL-verified, non-R13 source rows that had not yet appeared in prior local `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` files under the broad key:

```text
source_canonical_archetype_id + symbol + entry_date
```

Source canonical coverage:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C27_CONTENT_IP_GLOBAL_MONETIZATION
```

Source large-sector coverage:

```text
L1_INDUSTRIALS_INFRA_DEFENSE_GRID, L3_BATTERY_EV_GREEN_MOBILITY, L8_PLATFORM_CONTENT_SW_SECURITY
```

The source-sector rows already carry complete entry date, entry price, 30D/90D/180D MFE/MAE, clean calibration status, and URL evidence. This R13 file does **not** double-count them as fresh Cxx sector coverage.

## 2. Core finding

A valid non-price event does not automatically deserve Stage2/Stage3 persistence after a deep drawdown path. The repeated failure chain is:

```text
valid event / contract / approval / capacity evidence exists
→ second bridge confirmation is weak or delayed
→ MAE90 or MAE180 breaches deeply
→ high MFE, if present, proves optionality but not persistence quality
→ Stage2-Watch or local Stage4B overlay is required until the bridge is confirmed
```

## 3. Selected source rows

| # | symbol | company | source canonical | entry date | source trigger | R13 route | MFE90 | MAE90 | MFE180 | MAE180 | classification |
|---:|---|---|---|---|---|---|---:|---:|---:|---:|---|
| 1 | 002410 | 범양건영 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 2023-02-28 | Stage4B | Stage4B | 11.34% | -24.27% | 11.34% | -43.43% | deep_mae_low_or_moderate_mfe_stage2_false_positive_cap |
| 2 | 376300 |  | C27_CONTENT_IP_GLOBAL_MONETIZATION | 2023-04-12 | Stage3-Yellow | Stage4B | 34.29% | -17.86% | 35.00% | -39.29% | high_mfe_high_mae_stage3_persistence_requires_local_4b_overlay |
| 3 | 253450 |  | C27_CONTENT_IP_GLOBAL_MONETIZATION | 2023-05-08 | Stage4B-LocalWatch | Stage4B | 11.48% | -20.93% | 14.10% | -37.35% | deep_mae_low_or_moderate_mfe_stage2_false_positive_cap |
| 4 | 041510 |  | C27_CONTENT_IP_GLOBAL_MONETIZATION | 2023-07-12 | Stage2-Actionable | Stage4B | 21.81% | -17.54% | 21.81% | -34.52% | moderate_mae_stage2_watch_bridge_reconfirmation_required |
| 5 | 001260 | 남광토건 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 2024-02-05 | Stage2-Actionable | Stage4B | 4.64% | -22.68% | 16.80% | -22.68% | moderate_mae_stage2_watch_bridge_reconfirmation_required |
| 6 | 259630 | 엠플러스 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 2023-04-17 | Stage2-Actionable | Stage4B | 21.91% | -19.37% | 49.59% | -20.12% | moderate_mae_stage2_watch_bridge_reconfirmation_required |


## 4. Aggregate stress result

```yaml
calibration_usable_rows: 6
representative_rows: 6
unique_symbols: 6
unique_source_canonical_count: 3
unique_source_large_sector_count: 3
stage4b_overlay_count: 6
stage4c_count: 0
positive_with_guardrail_count: 2
counterexample_count: 4
rows_MAE180_le_minus_40pct: 1
rows_MAE180_le_minus_30pct: 4
rows_MFE180_ge_30pct: 2
avg_MFE_90D_pct: 17.5794
avg_MAE_90D_pct: -20.4421
avg_MFE_180D_pct: 24.7732
avg_MAE_180D_pct: -32.8979
median_MAE_180D_pct: -35.935
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
```

## 5. Proposed shadow rule candidate

```text
R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V132
```

Rule candidate:

```text
If MAE90 <= -25% or MAE180 <= -30% and confirmed delivery / revenue recognition / margin / FCF / utilization / cash / retention bridge is absent, cap positive persistence at Stage2-Watch or force local Stage4B overlay. If explicit non-price thesis break is confirmed, keep Stage4C. If MFE180 is high, preserve the thesis as watch/local 4B rather than deleting it, but do not allow Stage3 persistence without second bridge confirmation.
```

## 6. Machine-readable rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":132,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V132","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_fine_archetype_id":"mixed_C05_pf_liquidity_revenue_margin_cash_collection_holdout_v118","symbol":"002410","company_name":"범양건영","case_id":"R13_HIGHMAE_V132_CASE_01_002410","trigger_id":"R13_HIGHMAE_V132_T01_002410","trigger_type":"Stage4B","source_trigger_type":"Stage4B","trigger_date":"2023-02-28","entry_date":"2023-02-28","entry_price":3440.0,"classification":"deep_mae_low_or_moderate_mfe_stage2_false_positive_cap","evidence_family":"unused_url_verified_source_row_high_MAE_guardrail_replay_v132","evidence_source":"https://www.businesspost.co.kr/BP?command=article_view&num=307702","source_file":"e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","source_case_id":"C05_R1_L118_002410_BUMYANG_2022_COST_OVERRUN_DELAY_PENALTY_LOCAL_4B","evidence_summary":"URL-verified source-sector row replayed for R13 high-MAE guardrail validation.","stage2_evidence_fields":["revenue_growth_headline"],"stage3_evidence_fields":["not_supported_without_confirmed_delivery_revenue_margin_or_cash_bridge"],"stage4b_evidence_fields":["raw_material_cost_overrun","delay_penalty","operating_loss_transition","cash_collection_and_margin_gap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002410/2023.csv","profile_path":"atlas/symbol_profiles/002/002410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.0349,"MAE_30D_pct":-22.3837,"MFE_90D_pct":11.3372,"MAE_90D_pct":-24.2733,"MFE_180D_pct":11.3372,"MAE_180D_pct":-43.4302,"peak_date":"2023-05-22","peak_price":3830.0,"drawdown_after_peak_pct":-49.1906,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"inherited_clean_source_row_or_screened_clean_180D_window","current_profile_error":true,"current_profile_verdict":"cap Stage2/Stage3 persistence after high-MAE path unless confirmed bridge is present; keep hard 4C only for explicit thesis break","stage_after_shadow_rule":"Stage4B_local_overlay_or_Stage2_Watch_cap","reused_source_case_for_r13_guardrail":true,"do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_002410_2023-02-28_Stage4B","high_mae_guardrail_reason":"MAE90/MAE180 breach without confirmed Stage3 bridge; force local 4B or Stage2-Watch cap","production_scoring_patch_applied":false,"calibration_block_reasons":[]}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":132,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V132","source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_fine_archetype_id":"C27_FAN_PLATFORM_SUBSCRIPTION_RECURRING_REVENUE","symbol":"376300","company_name":"","case_id":"R13_HIGHMAE_V132_CASE_02_376300","trigger_id":"R13_HIGHMAE_V132_T02_376300","trigger_type":"Stage4B","source_trigger_type":"Stage3-Yellow","trigger_date":"2023-04-12","entry_date":"2023-04-12","entry_price":42000.0,"classification":"high_mfe_high_mae_stage3_persistence_requires_local_4b_overlay","evidence_family":"unused_url_verified_source_row_high_MAE_guardrail_replay_v132","evidence_source":"https://www.businesskorea.co.kr/news/articleView.html?idxno=112700","source_file":"e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md","source_case_id":"C27_R8_L100_06","evidence_summary":"URL-verified source-sector row replayed for R13 high-MAE guardrail validation.","stage2_evidence_fields":["valid_non_price_event_present","bridge_reconfirmation_required"],"stage3_evidence_fields":["not_supported_without_confirmed_delivery_revenue_margin_or_cash_bridge"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","bridge_gap","local_4b_watch_guard"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/376/376300/2023.csv","profile_path":"atlas/symbol_profiles/376/376300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.57,"MAE_30D_pct":-4.52,"MFE_90D_pct":34.29,"MAE_90D_pct":-17.86,"MFE_180D_pct":35.0,"MAE_180D_pct":-39.29,"peak_date":"2023-06-19","peak_price":56700.0,"drawdown_after_peak_pct":null,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"inherited_clean_source_row_or_screened_clean_180D_window","current_profile_error":true,"current_profile_verdict":"cap Stage2/Stage3 persistence after high-MAE path unless confirmed bridge is present; keep hard 4C only for explicit thesis break","stage_after_shadow_rule":"Stage4B_local_overlay_or_Stage2_Watch_cap","reused_source_case_for_r13_guardrail":true,"do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_C27_CONTENT_IP_GLOBAL_MONETIZATION_376300_2023-04-12_Stage4B","high_mae_guardrail_reason":"MAE90/MAE180 breach without confirmed Stage3 bridge; force local 4B or Stage2-Watch cap","production_scoring_patch_applied":false,"calibration_block_reasons":[]}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":132,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V132","source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_fine_archetype_id":"C27_GLOBAL_OTT_VOLUME_DEAL_DELIVERY_MARGIN_GAP","symbol":"253450","company_name":"","case_id":"R13_HIGHMAE_V132_CASE_03_253450","trigger_id":"R13_HIGHMAE_V132_T03_253450","trigger_type":"Stage4B","source_trigger_type":"Stage4B-LocalWatch","trigger_date":"2023-05-08","entry_date":"2023-05-08","entry_price":68800.0,"classification":"deep_mae_low_or_moderate_mfe_stage2_false_positive_cap","evidence_family":"unused_url_verified_source_row_high_MAE_guardrail_replay_v132","evidence_source":"https://studiodragon.irplus.co.kr/fileupload/analyst_e/202305/20230508_sd3.pdf","source_file":"e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md","source_case_id":"C27_R8_L100_05","evidence_summary":"URL-verified source-sector row replayed for R13 high-MAE guardrail validation.","stage2_evidence_fields":["valid_non_price_event_present","bridge_reconfirmation_required"],"stage3_evidence_fields":["not_supported_without_confirmed_delivery_revenue_margin_or_cash_bridge"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","bridge_gap","local_4b_watch_guard"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/253/253450/2023.csv","profile_path":"atlas/symbol_profiles/253/253450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.23,"MAE_30D_pct":-7.41,"MFE_90D_pct":11.48,"MAE_90D_pct":-20.93,"MFE_180D_pct":14.1,"MAE_180D_pct":-37.35,"peak_date":"2023-06-05","peak_price":78500.0,"drawdown_after_peak_pct":null,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"inherited_clean_source_row_or_screened_clean_180D_window","current_profile_error":true,"current_profile_verdict":"cap Stage2/Stage3 persistence after high-MAE path unless confirmed bridge is present; keep hard 4C only for explicit thesis break","stage_after_shadow_rule":"Stage4B_local_overlay_or_Stage2_Watch_cap","reused_source_case_for_r13_guardrail":true,"do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_C27_CONTENT_IP_GLOBAL_MONETIZATION_253450_2023-05-08_Stage4B","high_mae_guardrail_reason":"MAE90/MAE180 breach without confirmed Stage3 bridge; force local 4B or Stage2-Watch cap","production_scoring_patch_applied":false,"calibration_block_reasons":[]}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":132,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V132","source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_fine_archetype_id":"C27_ALBUM_PREORDER_TO_DURABLE_IP_MONETIZATION_GAP","symbol":"041510","company_name":"","case_id":"R13_HIGHMAE_V132_CASE_04_041510","trigger_id":"R13_HIGHMAE_V132_T04_041510","trigger_type":"Stage4B","source_trigger_type":"Stage2-Actionable","trigger_date":"2023-07-12","entry_date":"2023-07-12","entry_price":116900.0,"classification":"moderate_mae_stage2_watch_bridge_reconfirmation_required","evidence_family":"unused_url_verified_source_row_high_MAE_guardrail_replay_v132","evidence_source":"https://www.linkedin.com/posts/smentertainment_nct-dream-has-broken-their-own-record-by-activity-7085425044612370432-cWUL","source_file":"e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md","source_case_id":"C27_R8_L100_03","evidence_summary":"URL-verified source-sector row replayed for R13 high-MAE guardrail validation.","stage2_evidence_fields":["valid_non_price_event_present","bridge_reconfirmation_required"],"stage3_evidence_fields":["not_supported_without_confirmed_delivery_revenue_margin_or_cash_bridge"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","bridge_gap","local_4b_watch_guard"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.91,"MAE_30D_pct":-5.62,"MFE_90D_pct":21.81,"MAE_90D_pct":-17.54,"MFE_180D_pct":21.81,"MAE_180D_pct":-34.52,"peak_date":"2023-08-08","peak_price":142400.0,"drawdown_after_peak_pct":null,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"inherited_clean_source_row_or_screened_clean_180D_window","current_profile_error":true,"current_profile_verdict":"cap Stage2/Stage3 persistence after high-MAE path unless confirmed bridge is present; keep hard 4C only for explicit thesis break","stage_after_shadow_rule":"Stage4B_local_overlay_or_Stage2_Watch_cap","reused_source_case_for_r13_guardrail":true,"do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_C27_CONTENT_IP_GLOBAL_MONETIZATION_041510_2023-07-12_Stage4B","high_mae_guardrail_reason":"MAE90/MAE180 breach without confirmed Stage3 bridge; force local 4B or Stage2-Watch cap","production_scoring_patch_applied":false,"calibration_block_reasons":[]}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":132,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V132","source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_fine_archetype_id":"mixed_C05_pf_liquidity_revenue_margin_cash_collection_holdout_v118","symbol":"001260","company_name":"남광토건","case_id":"R13_HIGHMAE_V132_CASE_05_001260","trigger_id":"R13_HIGHMAE_V132_T05_001260","trigger_type":"Stage4B","source_trigger_type":"Stage2-Actionable","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":7320.0,"classification":"moderate_mae_stage2_watch_bridge_reconfirmation_required","evidence_family":"unused_url_verified_source_row_high_MAE_guardrail_replay_v132","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240205000376&docno=&method=search&viewerhost=","source_file":"e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","source_case_id":"C05_R1_L118_001260_NAMKWANG_CONTRACT_EXTENSION_STAGE2_HEADLINE_CAP","evidence_summary":"URL-verified source-sector row replayed for R13 high-MAE guardrail validation.","stage2_evidence_fields":["public_contract_disclosure","project_duration_visibility","order_backlog_related_event"],"stage3_evidence_fields":["not_supported_without_confirmed_delivery_revenue_margin_or_cash_bridge"],"stage4b_evidence_fields":["contract_revision_not_margin_bridge","MAE90_below_minus_20","cash_collection_not_confirmed"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001260/2024.csv","profile_path":"atlas/symbol_profiles/001/001260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.6448,"MAE_30D_pct":-13.5246,"MFE_90D_pct":4.6448,"MAE_90D_pct":-22.6776,"MFE_180D_pct":16.8033,"MAE_180D_pct":-22.6776,"peak_date":"2024-07-30","peak_price":8550.0,"drawdown_after_peak_pct":-30.4094,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"inherited_clean_source_row_or_screened_clean_180D_window","current_profile_error":true,"current_profile_verdict":"cap Stage2/Stage3 persistence after high-MAE path unless confirmed bridge is present; keep hard 4C only for explicit thesis break","stage_after_shadow_rule":"Stage4B_local_overlay_or_Stage2_Watch_cap","reused_source_case_for_r13_guardrail":true,"do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_001260_2024-02-05_Stage4B","high_mae_guardrail_reason":"MAE90/MAE180 breach without confirmed Stage3 bridge; force local 4B or Stage2-Watch cap","production_scoring_patch_applied":false,"calibration_block_reasons":[]}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":132,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V132","source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","source_fine_archetype_id":"mixed_C12_equipment_material_customer_contract_revenue_calloff_holdout_v108","symbol":"259630","company_name":"엠플러스","case_id":"R13_HIGHMAE_V132_CASE_06_259630","trigger_id":"R13_HIGHMAE_V132_T06_259630","trigger_type":"Stage4B","source_trigger_type":"Stage2-Actionable","trigger_date":"2023-04-17","entry_date":"2023-04-17","entry_price":13370.0,"classification":"moderate_mae_stage2_watch_bridge_reconfirmation_required","evidence_family":"unused_url_verified_source_row_high_MAE_guardrail_replay_v132","evidence_source":"https://securities.miraeasset.com/bbs/download/2108748.pdf?attachmentId=2108748","source_file":"e2r_stock_web_v12_residual_round_R3_loop_108_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md","source_case_id":"C12_R3_L108_259630_MPLUS_20230417_313BN_ASSEMBLY_EQUIPMENT_ORDER","evidence_summary":"URL-verified source-sector row replayed for R13 high-MAE guardrail validation.","stage2_evidence_fields":["named_battery_equipment_contract_amount","assembly_process_equipment_contract","delivery_window_visible"],"stage3_evidence_fields":["order_to_revenue_bridge_partial"],"stage4b_evidence_fields":["contract_period_long","customer_name_confidentiality","calloff_or_delay_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/259/259630/2023.csv","profile_path":"atlas/symbol_profiles/259/259630.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.9312,"MAE_30D_pct":-19.3717,"MFE_90D_pct":21.9147,"MAE_90D_pct":-19.3717,"MFE_180D_pct":49.5886,"MAE_180D_pct":-20.1197,"peak_date":"2023-09-06","peak_price":20000.0,"drawdown_after_peak_pct":-46.6,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"corporate_action_window_status":"inherited_clean_source_row_or_screened_clean_180D_window","current_profile_error":true,"current_profile_verdict":"cap Stage2/Stage3 persistence after high-MAE path unless confirmed bridge is present; keep hard 4C only for explicit thesis break","stage_after_shadow_rule":"Stage4B_local_overlay_or_Stage2_Watch_cap","reused_source_case_for_r13_guardrail":true,"do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_259630_2023-04-17_Stage4B","high_mae_guardrail_reason":"MAE90/MAE180 breach without confirmed Stage3 bridge; force local 4B or Stage2-Watch cap","production_scoring_patch_applied":false,"calibration_block_reasons":[]}
{"row_type":"score_simulation","round":"R13","loop":132,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","symbol":"002410","company_name":"범양건영","entry_date":"2023-02-28","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_trigger_type":"Stage4B","baseline_current_profile_proxy_stage":"Stage2_or_Stage3_if_bridge_not_rechecked","shadow_rule_corrected_stage":"Stage4B_local_overlay_or_Stage2_Watch_cap","score_component_snapshot":{"stage2_required_bridge":"recheck delivery/revenue recognition/margin/FCF/utilization/cash bridge before persistence","price_path_risk":"MAE90_or_MAE180_breach","MFE_90D_pct":11.3372,"MAE_90D_pct":-24.2733,"MFE_180D_pct":11.3372,"MAE_180D_pct":-43.4302,"local_4b_watch_guard":"force_on","mfe_quality":"weak_or_moderate"},"score_return_alignment":"reduces false Stage2/Stage3 persistence after URL-verified deep-MAE path","production_scoring_patch_applied":false}
{"row_type":"score_simulation","round":"R13","loop":132,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","symbol":"376300","company_name":"","entry_date":"2023-04-12","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_trigger_type":"Stage3-Yellow","baseline_current_profile_proxy_stage":"Stage2_or_Stage3_if_bridge_not_rechecked","shadow_rule_corrected_stage":"Stage4B_local_overlay_or_Stage2_Watch_cap","score_component_snapshot":{"stage2_required_bridge":"recheck delivery/revenue recognition/margin/FCF/utilization/cash bridge before persistence","price_path_risk":"MAE90_or_MAE180_breach","MFE_90D_pct":34.29,"MAE_90D_pct":-17.86,"MFE_180D_pct":35.0,"MAE_180D_pct":-39.29,"local_4b_watch_guard":"force_on","mfe_quality":"high_but_unstable"},"score_return_alignment":"reduces false Stage2/Stage3 persistence after URL-verified deep-MAE path","production_scoring_patch_applied":false}
{"row_type":"score_simulation","round":"R13","loop":132,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","symbol":"253450","company_name":"","entry_date":"2023-05-08","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_trigger_type":"Stage4B-LocalWatch","baseline_current_profile_proxy_stage":"Stage2_or_Stage3_if_bridge_not_rechecked","shadow_rule_corrected_stage":"Stage4B_local_overlay_or_Stage2_Watch_cap","score_component_snapshot":{"stage2_required_bridge":"recheck delivery/revenue recognition/margin/FCF/utilization/cash bridge before persistence","price_path_risk":"MAE90_or_MAE180_breach","MFE_90D_pct":11.48,"MAE_90D_pct":-20.93,"MFE_180D_pct":14.1,"MAE_180D_pct":-37.35,"local_4b_watch_guard":"force_on","mfe_quality":"weak_or_moderate"},"score_return_alignment":"reduces false Stage2/Stage3 persistence after URL-verified deep-MAE path","production_scoring_patch_applied":false}
{"row_type":"score_simulation","round":"R13","loop":132,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","symbol":"041510","company_name":"","entry_date":"2023-07-12","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_trigger_type":"Stage2-Actionable","baseline_current_profile_proxy_stage":"Stage2_or_Stage3_if_bridge_not_rechecked","shadow_rule_corrected_stage":"Stage4B_local_overlay_or_Stage2_Watch_cap","score_component_snapshot":{"stage2_required_bridge":"recheck delivery/revenue recognition/margin/FCF/utilization/cash bridge before persistence","price_path_risk":"MAE90_or_MAE180_breach","MFE_90D_pct":21.81,"MAE_90D_pct":-17.54,"MFE_180D_pct":21.81,"MAE_180D_pct":-34.52,"local_4b_watch_guard":"force_on","mfe_quality":"weak_or_moderate"},"score_return_alignment":"reduces false Stage2/Stage3 persistence after URL-verified deep-MAE path","production_scoring_patch_applied":false}
{"row_type":"score_simulation","round":"R13","loop":132,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","symbol":"001260","company_name":"남광토건","entry_date":"2024-02-05","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_trigger_type":"Stage2-Actionable","baseline_current_profile_proxy_stage":"Stage2_or_Stage3_if_bridge_not_rechecked","shadow_rule_corrected_stage":"Stage4B_local_overlay_or_Stage2_Watch_cap","score_component_snapshot":{"stage2_required_bridge":"recheck delivery/revenue recognition/margin/FCF/utilization/cash bridge before persistence","price_path_risk":"MAE90_or_MAE180_breach","MFE_90D_pct":4.6448,"MAE_90D_pct":-22.6776,"MFE_180D_pct":16.8033,"MAE_180D_pct":-22.6776,"local_4b_watch_guard":"force_on","mfe_quality":"weak_or_moderate"},"score_return_alignment":"reduces false Stage2/Stage3 persistence after URL-verified deep-MAE path","production_scoring_patch_applied":false}
{"row_type":"score_simulation","round":"R13","loop":132,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","symbol":"259630","company_name":"엠플러스","entry_date":"2023-04-17","source_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","source_trigger_type":"Stage2-Actionable","baseline_current_profile_proxy_stage":"Stage2_or_Stage3_if_bridge_not_rechecked","shadow_rule_corrected_stage":"Stage4B_local_overlay_or_Stage2_Watch_cap","score_component_snapshot":{"stage2_required_bridge":"recheck delivery/revenue recognition/margin/FCF/utilization/cash bridge before persistence","price_path_risk":"MAE90_or_MAE180_breach","MFE_90D_pct":21.9147,"MAE_90D_pct":-19.3717,"MFE_180D_pct":49.5886,"MAE_180D_pct":-20.1197,"local_4b_watch_guard":"force_on","mfe_quality":"high_but_unstable"},"score_return_alignment":"reduces false Stage2/Stage3 persistence after URL-verified deep-MAE path","production_scoring_patch_applied":false}
{"row_type":"aggregate","round":"R13","loop":132,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V132","trigger_count":6,"representative_trigger_count":6,"calibration_usable_trigger_count":6,"source_sector_new_independent_case_count":0,"r13_guardrail_replay_row_count":6,"reused_source_case_count":6,"unique_symbol_count":6,"unique_source_canonical_count":3,"unique_source_large_sector_count":3,"stage4b_overlay_count":6,"stage4c_count":0,"positive_with_guardrail_count":2,"counterexample_count":4,"rows_MAE180_le_minus_40pct":1,"rows_MAE180_le_minus_30pct":4,"rows_MFE180_ge_30pct":2,"avg_MFE_90D_pct":17.5794,"avg_MAE_90D_pct":-20.4421,"avg_MFE_180D_pct":24.7732,"avg_MAE_180D_pct":-32.8979,"median_MAE_180D_pct":-35.935,"current_profile_error_count":6,"source_proxy_only_rows":0,"evidence_url_pending_rows":0,"sector_specific_rule_candidate":"no_new_sector_specific_rule","canonical_archetype_rule_candidate":"R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V132","production_scoring_patch_applied":false}
{"row_type":"shadow_weight","round":"R13","loop":132,"scope":"cross_archetype_guardrail_shadow_axis","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","axis":"R13_high_MAE_guardrail_shadow_axis_v132","current_profile_behavior":"may keep Stage2/Stage3 positive after deep MAE when delivery/revenue/margin/cash bridge is not rechecked","shadow_rule_candidate":"If MAE90 <= -25% or MAE180 <= -30% and confirmed delivery/revenue recognition/margin/FCF/utilization/cash bridge is absent, cap at Stage2-Watch or force local Stage4B overlay. Keep hard thesis-break rows as Stage4C. High MFE does not cancel the overlay; it only preserves the case as watch rather than deletion.","expected_effect":"reduce URL-verified high-drawdown false persistence while preserving high-MFE structural cases as watch/local 4B rather than full thesis deletion","eligible_trigger_count":6,"confidence":"medium","proposal_type":"shadow_only_for_later_batch_agent","production_scoring_patch_applied":false}
{"row_type":"residual_contribution","round":"R13","loop":132,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","contribution_label":"unused_URL_verified_high_MAE_residual_error_found_v132","summary":"6 unused URL-verified source-sector rows across 3 source canonical archetypes show high-MAE persistence risk after valid non-price evidence. R13 should separate thesis validity, entry/path risk, and hard thesis break.","new_axis_proposed":"R13_high_MAE_guardrail_shadow_axis_v132","existing_axis_strengthened":["local_4b_watch_guard","stage2_required_bridge","hard_4c_thesis_break_routes_to_4c"],"existing_axis_weakened":null,"do_not_count_as_new_sector_case":true,"production_scoring_patch_applied":false}
```

## 7. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
uses_current_session_source_rows_for_r13_reuse: true
do_not_count_as_new_sector_case: true
independent_evidence_weight: 0.25
jsonl_trigger_row_count: 6
calibration_usable_rows: 6
representative_rows: 6
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

## 8. Deferred Coding Agent Handoff Prompt

```text
Ingest this MD as an R13 guardrail file only. Do not count rows as fresh Cxx sector coverage. Parse JSONL rows and test whether local_4b_watch_guard / stage2_required_bridge should be strengthened when MAE90 <= -25% or MAE180 <= -30% without second bridge confirmation. Keep hard thesis-break rows as Stage4C. Produce patch specs only after dedupe across all R13 scopes.
```

## 9. Completed research state

```text
completed_round = R13
completed_loop = 132
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = R13 high-MAE guardrail mini holdout after session-adjusted Priority-0/Priority-1 fills
next_recommended_archetypes = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_holdout_quality_only | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path | C05_EPC_MEGA_CONTRACT_MARGIN_GAP_holdout_only_if_new_working_capital_path
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

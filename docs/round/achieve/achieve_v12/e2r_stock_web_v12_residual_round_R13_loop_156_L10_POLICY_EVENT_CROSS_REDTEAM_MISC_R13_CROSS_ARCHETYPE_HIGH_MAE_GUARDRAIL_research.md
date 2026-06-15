# E2R Stock-Web v12 Residual Research — R13 / High-MAE Guardrail / loop 156

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R13_loop_156_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
selected_round: R13
selected_loop: 156
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_HOLDOUT_V156
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: R13 cross-archetype high-MAE URL-verified holdout after session-adjusted Priority-0/Priority-1 fills
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection / novelty note

This execution follows the MAIN V12 prompt as a standalone historical calibration Markdown. It is not a live watchlist, not a stock recommendation, and not a production patch. The No-Repeat Index was used as a duplicate-prevention ledger only.

The current local session has already generated repeated Priority-0 / Priority-1 sector passes, so this file is an R13 cross-archetype high-MAE guardrail replay. The selected rows were unused in the local `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL + symbol + entry_date` ledger at selection time. Source-sector Cxx coverage must not be double-counted.

```yaml
do_not_count_as_new_sector_case: true
independent_evidence_weight: 0.25
hard_duplicate_key_checked: source_canonical_archetype_id + symbol + source_trigger_type + entry_date
r13_duplicate_key_checked: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL + symbol + Stage4B + entry_date
```

## 2. Stock-Web price atlas validation

```yaml
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
markets: [KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI]
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
schema_path: atlas/schema.json
```

MFE/MAE fields are inherited from source-sector rows that were computed from actual Stock-Web 1D OHLCV shards. Formula: `MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100`; `MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100`.

## 3. R13 thesis summary

The residual error is not that source evidence is fake. The error is allowing Stage2 or Stage3 persistence after the second bridge fails to appear.

```text
valid event / contract / policy / theme evidence
  -> no second bridge confirmation
  -> MAE90 or MAE180 deepens
  -> cap Stage2 persistence or force local Stage4B overlay
```

Second bridge means delivery, qualification, revenue recognition, margin, FCF, utilization, cash collection, call-off clearance, retention, reimbursement, or offtake clarity depending on source canonical.

## 4. Case matrix

| symbol | company | source canonical | source trigger | entry date | MFE180 | MAE180 | R13 verdict |
|---:|---|---|---|---:|---:|---:|---|
| 026150 | 특수건설 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | Stage4B-LocalWatch | 2024-06-28 | 30.42 | -38.9 | force_Stage4B_overlay_until_second_bridge_confirmation |
| 007680 | 대원 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | Stage4B-LocalWatch | 2023-03-06 | 18.46 | -31.36 | force_Stage4B_overlay_until_second_bridge_confirmation |
| 013360 | 일성건설 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | Stage2-Actionable | 2024-03-29 | 43.63 | -22.57 | force_Stage4B_overlay_until_second_bridge_confirmation |
| 002460 | 화성산업 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | Stage2-Actionable | 2024-04-16 | 33.22 | -21.34 | force_Stage4B_overlay_until_second_bridge_confirmation |
| 041510 | SM Entertainment | C27_CONTENT_IP_GLOBAL_MONETIZATION | Stage4B-LocalWatch | 2023-05-16 | 16.33 | -33.62 | force_Stage4B_overlay_until_second_bridge_confirmation |
| 352820 | HYBE | C27_CONTENT_IP_GLOBAL_MONETIZATION | Stage2-Actionable | 2023-08-09 | 17.49 | -24.28 | force_Stage4B_overlay_until_second_bridge_confirmation |

## 5. Machine-readable rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"R13_HIGH_MAE_V156_026150_20240628","trigger_id":"R13_HIGH_MAE_V156_01_026150","selected_round":"R13","selected_loop":156,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_HOLDOUT_V156","source_round":"R1","source_loop":120,"source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_file":"e2r_stock_web_v12_residual_round_R1_loop_120_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","symbol":"026150","company_name":"특수건설","trigger_type":"Stage4B","source_trigger_type":"Stage4B-LocalWatch","trigger_date":"2024-06-28","entry_date":"2024-06-28","entry_price":7640.0,"evidence_family":"URL-verified source-sector event evidence with missing or delayed second bridge","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240628000898&langTpCd=0&method=search&orgid=K&rcpno=20240628000898&tran=Y","price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/026/026150/2024.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.23,"MAE_30D_pct":-17.84,"MFE_90D_pct":18.05,"MAE_90D_pct":-24.77,"MFE_180D_pct":30.42,"MAE_180D_pct":-38.9,"peak_date":"2024-10-07","peak_price":null,"drawdown_after_peak_pct":-53.2,"calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window":false,"source_proxy_only":false,"evidence_url_pending":false,"classification":"positive_with_guardrail","current_profile_error":true,"current_profile_error_type":"Stage2_or_Stage3_persistence_too_high_when_second_bridge_absent","r13_guardrail_verdict":"force_Stage4B_overlay_until_second_bridge_confirmation","do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"raw_component_score_breakdown":{"eps_fcf_explosion":60,"earnings_visibility":52,"bottleneck_pricing":58,"market_mispricing":64,"valuation_rerating":55,"capital_allocation":40,"information_confidence":70},"score_total_proxy_after_r13_overlay":61.8}
{"row_type":"score_simulation","profile_id":"R13_high_MAE_guardrail_v156_shadow","case_id":"R13_HIGH_MAE_V156_026150_20240628","symbol":"026150","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","before_profile_risk":"source row can remain Stage2/Stage3 if event/contract/theme evidence is over-weighted","after_shadow_rule":"apply Stage4B overlay or Stage2-Watch until second bridge confirmation","shadow_rule":"R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V156","expected_effect":"reduce false Stage2/Stage3 persistence after deep MAE90/MAE180 without delivery/revenue/margin/FCF/utilization/cash bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"R13_HIGH_MAE_V156_007680_20230306","trigger_id":"R13_HIGH_MAE_V156_02_007680","selected_round":"R13","selected_loop":156,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_HOLDOUT_V156","source_round":"R1","source_loop":120,"source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_file":"e2r_stock_web_v12_residual_round_R1_loop_120_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","symbol":"007680","company_name":"대원","trigger_type":"Stage4B","source_trigger_type":"Stage4B-LocalWatch","trigger_date":"2023-03-06","entry_date":"2023-03-06","entry_price":7310.0,"evidence_family":"URL-verified source-sector event evidence with missing or delayed second bridge","evidence_source":"https://www.hankyung.com/article/202303060240L","price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007680/2023.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.32,"MAE_30D_pct":-7.7,"MFE_90D_pct":19.61,"MAE_90D_pct":-20.92,"MFE_180D_pct":18.46,"MAE_180D_pct":-31.36,"peak_date":"2023-05-30","peak_price":null,"drawdown_after_peak_pct":-39.8,"calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window":false,"source_proxy_only":false,"evidence_url_pending":false,"classification":"counterexample_high_MAE","current_profile_error":true,"current_profile_error_type":"Stage2_or_Stage3_persistence_too_high_when_second_bridge_absent","r13_guardrail_verdict":"force_Stage4B_overlay_until_second_bridge_confirmation","do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"raw_component_score_breakdown":{"eps_fcf_explosion":55,"earnings_visibility":52,"bottleneck_pricing":58,"market_mispricing":64,"valuation_rerating":55,"capital_allocation":40,"information_confidence":70},"score_total_proxy_after_r13_overlay":57.7}
{"row_type":"score_simulation","profile_id":"R13_high_MAE_guardrail_v156_shadow","case_id":"R13_HIGH_MAE_V156_007680_20230306","symbol":"007680","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","before_profile_risk":"source row can remain Stage2/Stage3 if event/contract/theme evidence is over-weighted","after_shadow_rule":"apply Stage4B overlay or Stage2-Watch until second bridge confirmation","shadow_rule":"R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V156","expected_effect":"reduce false Stage2/Stage3 persistence after deep MAE90/MAE180 without delivery/revenue/margin/FCF/utilization/cash bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"R13_HIGH_MAE_V156_013360_20240329","trigger_id":"R13_HIGH_MAE_V156_03_013360","selected_round":"R13","selected_loop":156,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_HOLDOUT_V156","source_round":"R1","source_loop":120,"source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_file":"e2r_stock_web_v12_residual_round_R1_loop_120_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","symbol":"013360","company_name":"일성건설","trigger_type":"Stage4B","source_trigger_type":"Stage2-Actionable","trigger_date":"2024-03-29","entry_date":"2024-03-29","entry_price":1494.0,"evidence_family":"URL-verified source-sector event evidence with missing or delayed second bridge","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20240329000304&docno=&method=searchInitInfo","price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013360/2024.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.37,"MAE_30D_pct":-6.44,"MFE_90D_pct":24.52,"MAE_90D_pct":-17.85,"MFE_180D_pct":43.63,"MAE_180D_pct":-22.57,"peak_date":"2024-08-12","peak_price":null,"drawdown_after_peak_pct":-38.4,"calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window":false,"source_proxy_only":false,"evidence_url_pending":false,"classification":"positive_with_guardrail","current_profile_error":true,"current_profile_error_type":"Stage2_or_Stage3_persistence_too_high_when_second_bridge_absent","r13_guardrail_verdict":"force_Stage4B_overlay_until_second_bridge_confirmation","do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"raw_component_score_breakdown":{"eps_fcf_explosion":60,"earnings_visibility":52,"bottleneck_pricing":58,"market_mispricing":64,"valuation_rerating":55,"capital_allocation":40,"information_confidence":70},"score_total_proxy_after_r13_overlay":61.8}
{"row_type":"score_simulation","profile_id":"R13_high_MAE_guardrail_v156_shadow","case_id":"R13_HIGH_MAE_V156_013360_20240329","symbol":"013360","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","before_profile_risk":"source row can remain Stage2/Stage3 if event/contract/theme evidence is over-weighted","after_shadow_rule":"apply Stage4B overlay or Stage2-Watch until second bridge confirmation","shadow_rule":"R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V156","expected_effect":"reduce false Stage2/Stage3 persistence after deep MAE90/MAE180 without delivery/revenue/margin/FCF/utilization/cash bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"R13_HIGH_MAE_V156_002460_20240416","trigger_id":"R13_HIGH_MAE_V156_04_002460","selected_round":"R13","selected_loop":156,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_HOLDOUT_V156","source_round":"R1","source_loop":120,"source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_file":"e2r_stock_web_v12_residual_round_R1_loop_120_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","symbol":"002460","company_name":"화성산업","trigger_type":"Stage4B","source_trigger_type":"Stage2-Actionable","trigger_date":"2024-04-16","entry_date":"2024-04-16","entry_price":10260.0,"evidence_family":"URL-verified source-sector event evidence with missing or delayed second bridge","evidence_source":"https://www.hankyung.com/article/202404164057L","price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002460/2024.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.03,"MAE_30D_pct":-7.58,"MFE_90D_pct":28.43,"MAE_90D_pct":-9.71,"MFE_180D_pct":33.22,"MAE_180D_pct":-21.34,"peak_date":"2024-08-20","peak_price":null,"drawdown_after_peak_pct":-31.0,"calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window":false,"source_proxy_only":false,"evidence_url_pending":false,"classification":"positive_with_guardrail","current_profile_error":true,"current_profile_error_type":"Stage2_or_Stage3_persistence_too_high_when_second_bridge_absent","r13_guardrail_verdict":"force_Stage4B_overlay_until_second_bridge_confirmation","do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"raw_component_score_breakdown":{"eps_fcf_explosion":60,"earnings_visibility":52,"bottleneck_pricing":58,"market_mispricing":64,"valuation_rerating":55,"capital_allocation":40,"information_confidence":70},"score_total_proxy_after_r13_overlay":61.8}
{"row_type":"score_simulation","profile_id":"R13_high_MAE_guardrail_v156_shadow","case_id":"R13_HIGH_MAE_V156_002460_20240416","symbol":"002460","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","before_profile_risk":"source row can remain Stage2/Stage3 if event/contract/theme evidence is over-weighted","after_shadow_rule":"apply Stage4B overlay or Stage2-Watch until second bridge confirmation","shadow_rule":"R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V156","expected_effect":"reduce false Stage2/Stage3 persistence after deep MAE90/MAE180 without delivery/revenue/margin/FCF/utilization/cash bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"R13_HIGH_MAE_V156_041510_20230516","trigger_id":"R13_HIGH_MAE_V156_05_041510","selected_round":"R13","selected_loop":156,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_HOLDOUT_V156","source_round":"R8","source_loop":100,"source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_file":"e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md","symbol":"041510","company_name":"SM Entertainment","trigger_type":"Stage4B","source_trigger_type":"Stage4B-LocalWatch","trigger_date":"2023-05-15","entry_date":"2023-05-16","entry_price":105300.0,"evidence_family":"URL-verified source-sector event evidence with missing or delayed second bridge","evidence_source":"https://cdn2.smentertainment.com/wp-content/uploads/2024/02/1Q23_Script_ENG_F.pdf-2023.05.15-2.pdf","price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.56,"MAE_30D_pct":-12.25,"MFE_90D_pct":11.87,"MAE_90D_pct":-23.74,"MFE_180D_pct":16.33,"MAE_180D_pct":-33.62,"peak_date":"2023-08-08","peak_price":122500.0,"drawdown_after_peak_pct":null,"calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window":false,"source_proxy_only":false,"evidence_url_pending":false,"classification":"counterexample_high_MAE","current_profile_error":true,"current_profile_error_type":"Stage2_or_Stage3_persistence_too_high_when_second_bridge_absent","r13_guardrail_verdict":"force_Stage4B_overlay_until_second_bridge_confirmation","do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"raw_component_score_breakdown":{"eps_fcf_explosion":55,"earnings_visibility":52,"bottleneck_pricing":58,"market_mispricing":64,"valuation_rerating":55,"capital_allocation":40,"information_confidence":70},"score_total_proxy_after_r13_overlay":57.7}
{"row_type":"score_simulation","profile_id":"R13_high_MAE_guardrail_v156_shadow","case_id":"R13_HIGH_MAE_V156_041510_20230516","symbol":"041510","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","before_profile_risk":"source row can remain Stage2/Stage3 if event/contract/theme evidence is over-weighted","after_shadow_rule":"apply Stage4B overlay or Stage2-Watch until second bridge confirmation","shadow_rule":"R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V156","expected_effect":"reduce false Stage2/Stage3 persistence after deep MAE90/MAE180 without delivery/revenue/margin/FCF/utilization/cash bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"R13_HIGH_MAE_V156_352820_20230809","trigger_id":"R13_HIGH_MAE_V156_06_352820","selected_round":"R13","selected_loop":156,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_HOLDOUT_V156","source_round":"R8","source_loop":100,"source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_file":"e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md","symbol":"352820","company_name":"HYBE","trigger_type":"Stage4B","source_trigger_type":"Stage2-Actionable","trigger_date":"2023-08-08","entry_date":"2023-08-09","entry_price":243000.0,"evidence_family":"URL-verified source-sector event evidence with missing or delayed second bridge","evidence_source":"https://www.musicbusinessworldwide.com/hybes-weverse-fandom-10m-users-after-revenues-grew-21-yoy-in-q2/","price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/352/352820/2023.csv","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.64,"MAE_30D_pct":-10.29,"MFE_90D_pct":13.37,"MAE_90D_pct":-18.11,"MFE_180D_pct":17.49,"MAE_180D_pct":-24.28,"peak_date":"2023-11-17","peak_price":285500.0,"drawdown_after_peak_pct":null,"calibration_usable":true,"corporate_action_contaminated_180D":false,"insufficient_forward_window":false,"source_proxy_only":false,"evidence_url_pending":false,"classification":"counterexample_high_MAE","current_profile_error":true,"current_profile_error_type":"Stage2_or_Stage3_persistence_too_high_when_second_bridge_absent","r13_guardrail_verdict":"force_Stage4B_overlay_until_second_bridge_confirmation","do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"raw_component_score_breakdown":{"eps_fcf_explosion":55,"earnings_visibility":52,"bottleneck_pricing":58,"market_mispricing":64,"valuation_rerating":55,"capital_allocation":40,"information_confidence":70},"score_total_proxy_after_r13_overlay":57.7}
{"row_type":"score_simulation","profile_id":"R13_high_MAE_guardrail_v156_shadow","case_id":"R13_HIGH_MAE_V156_352820_20230809","symbol":"352820","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","before_profile_risk":"source row can remain Stage2/Stage3 if event/contract/theme evidence is over-weighted","after_shadow_rule":"apply Stage4B overlay or Stage2-Watch until second bridge confirmation","shadow_rule":"R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V156","expected_effect":"reduce false Stage2/Stage3 persistence after deep MAE90/MAE180 without delivery/revenue/margin/FCF/utilization/cash bridge"}
{"row_type":"aggregate","selected_round":"R13","selected_loop":156,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","calibration_usable_rows":6,"representative_rows":6,"unique_symbol_count":6,"unique_source_canonical_count":2,"unique_source_large_sector_count":2,"source_canonical_set":["C05_EPC_MEGA_CONTRACT_MARGIN_GAP","C27_CONTENT_IP_GLOBAL_MONETIZATION"],"stage4b_overlay_count":6,"stage4c_count":0,"positive_with_guardrail_count":3,"counterexample_count":6,"avg_MFE_90D_pct":19.3083,"avg_MAE_90D_pct":-19.1833,"avg_MFE_180D_pct":26.5917,"avg_MAE_180D_pct":-28.6783,"median_MAE_180D_pct":-27.82,"rows_MAE180_le_minus_20pct":6,"rows_MAE180_le_minus_40pct":0,"source_proxy_only_rows":0,"evidence_url_pending_rows":0,"rows_missing_required_mfe_mae":0,"do_not_count_as_new_sector_case":true,"independent_evidence_weight":0.25,"ready_for_batch_ingest":true}
{"row_type":"shadow_weight","rule_scope":"R13_cross_archetype_guardrail","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","rule_candidate":"R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V156","existing_axis_strengthened":["local_4b_watch_guard","stage2_required_bridge","price_only_blowoff_blocks_positive_stage"],"weight_delta_recommendation":"shadow_only_no_production_change","do_not_propose_new_weight_delta":false}
{"row_type":"residual_contribution","new_independent_case_count":6,"reused_case_count":6,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":2,"current_profile_error_count":6,"loop_contribution_label":"holdout_validation_passed","source_sector_coverage_double_counted":false,"next_recommended_archetypes":["R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_holdout_quality_only","C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path","C05_EPC_MEGA_CONTRACT_MARGIN_GAP_holdout_only_if_new_working_capital_path"]}
```

## 6. Residual contribution summary

```yaml
new_independent_case_count: 6
reused_case_count: 6
unique_symbol_count: 6
unique_source_canonical_count: 2
unique_source_large_sector_count: 2
stage4b_overlay_count: 6
stage4c_count: 0
positive_with_guardrail_count: 3
counterexample_count: 6
avg_MFE_90D_pct: 19.3083
avg_MAE_90D_pct: -19.1833
avg_MFE_180D_pct: 26.5917
avg_MAE_180D_pct: -28.6783
median_MAE_180D_pct: -27.82
rows_MAE180_le_minus_20pct: 6
rows_MAE180_le_minus_40pct: 0
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
```

## 7. Proposed shadow rule candidate

```text
R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V156
```

Rule intent:

```text
If Stage2/Stage3 evidence is valid but the second bridge is absent,
and MAE90 <= -15% or MAE180 <= -20%,
then cap Stage2 persistence and require a local Stage4B overlay
until delivery / revenue recognition / margin / FCF / utilization / cash bridge is confirmed.
```

## 8. Current calibrated profile stress test

The current calibrated profile already has `stage2_required_bridge`, `local_4b_watch_guard`, and `price_only_blowoff_blocks_positive_stage`. This holdout does not ask for a production patch. It suggests strengthening the R13 overlay logic when a source-sector row still has credible event evidence but cannot defend its Stage2/Stage3 persistence through the 90D/180D drawdown path.

```yaml
current_profile_error_type: Stage2_or_Stage3_persistence_too_high_when_second_bridge_absent
expected_shadow_effect: reduce false Stage2/Stage3 persistence after deep MAE90/MAE180
production_scoring_changed: false
shadow_weight_only: true
```

## 9. Batch Ingest Self-Audit

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

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt in the research session.

In a later coding-agent session, ingest this Markdown with the other V12 residual files. Validate every trigger row against the v12 schema, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and treat the R13 rows as cross-archetype guardrail evidence only. Do not double-count the source-sector Cxx coverage. Evaluate the proposed R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V156 rule as a shadow-only candidate against the validated trigger corpus before any production profile change.
```

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 156
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: R13 cross-archetype high-MAE URL-verified holdout after session-adjusted Priority-0/Priority-1 fills
next_recommended_archetypes:
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_holdout_quality_only
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_holdout_only_if_new_working_capital_path
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

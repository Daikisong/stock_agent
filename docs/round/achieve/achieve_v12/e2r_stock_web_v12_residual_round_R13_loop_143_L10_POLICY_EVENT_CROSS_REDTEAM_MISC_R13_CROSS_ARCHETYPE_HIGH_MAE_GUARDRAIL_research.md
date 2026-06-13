# E2R Stock-Web V12 Residual Research — R13 High-MAE Guardrail Mini Holdout v143

## 0. Research Metadata
```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R13_loop_143_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
selected_round: R13
selected_loop: 143
selection_basis: docs/core/V12_Research_No_Repeat_Index.md used as no-repeat ledger only
selected_priority_bucket: R13 cross-archetype high-MAE mini holdout after session-adjusted Priority-0/Priority-1 fills
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V143
loop_objective:
  - holdout_validation
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - Stage2_Stage3_persistence_MAE_cap
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
production_code_patch_included: false
production_scoring_patch_applied: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check

The MAIN prompt requires coverage-index-first selection and treats `R13` as a cross-archetype checkpoint, not a sector-positive mining round. The static No-Repeat Index still shows Priority 0/1 gaps, but this long session has already added repeated C02/C05/C06/C07/C09/C10/C11/C12/C14/C28 and R13 passes. Therefore this loop uses URL-verified source-sector rows that had not yet been used under the local `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` key.

```yaml
hard_duplicate_key_checked: canonical_archetype_id + symbol + trigger_type + entry_date
source_sector_rows_reused_for_r13: 6
do_not_count_as_new_sector_case: true
independent_evidence_weight: 0.25
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
```

## 2. Price source validation

Stock-Web manifest basis: `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`. MFE/MAE follows the Stock-Web schema: max high / min low from entry date through the 30/90/180 tradable-row window. The six rows below are source-sector rows with complete 30D/90D/180D MFE/MAE and no evidence URL pending flag.

## 3. Core finding

High-MAE holdouts keep showing a narrow but important failure mode: **valid evidence is not the same thing as persistence quality**. A game/IP success, a battery recovery narrative, or an EPC/engineering backlog can deserve Stage2, but if the second bridge is absent and the price path breaks sharply, the row should be capped.

```text
valid source-sector evidence
  -> no second bridge yet
  -> MAE90 or MAE180 breach
  -> Stage2-Watch / Stage4B-LocalWatch
  -> only re-open Stage3 after delivery, revenue recognition, margin, FCF, utilization, retention, sell-through, or cash-collection confirmation
```

## 4. Selected trigger rows

| # | symbol | company | source canonical | source trigger | entry_date | MFE90 | MAE90 | MFE180 | MAE180 | R13 verdict |
|---:|---|---|---|---|---|---:|---:|---:|---:|---|
| 1 | 112040 | 위메이드 | C27_CONTENT_IP_GLOBAL_MONETIZATION | Stage3-Yellow | 2021-11-12 | 35.10% | -45.60% | 35.10% | -66.70% | Stage4B overlay until second bridge confirmation |
| 2 | 241840 | 에이스토리 | C27_CONTENT_IP_GLOBAL_MONETIZATION | Stage3-Yellow | 2022-07-20 | 55.20% | -36.80% | 55.20% | -55.70% | Stage4B overlay until second bridge confirmation |
| 3 | 278280 | 천보 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | Stage2-Actionable | 2025-01-08 | 6.04% | -24.40% | 28.55% | -24.40% | Stage4B overlay until second bridge confirmation |
| 4 | 054930 | 유신 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | Stage2 | 2024-08-13 | 10.76% | -20.35% | 10.76% | -23.68% | Stage4B overlay until second bridge confirmation |
| 5 | 023350 | 한국종합기술 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | Stage2 | 2024-05-17 | 11.52% | -21.21% | 44.42% | -23.13% | Stage4B overlay until second bridge confirmation |
| 6 | 100090 | SK오션플랜트 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | Stage4B | 2024-08-22 | 13.52% | -22.14% | 55.22% | -22.14% | Stage4B overlay until second bridge confirmation |

## 5. Aggregate stress result

```yaml
selected_round: R13
selected_loop: 143
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
calibration_usable_rows: 6
representative_rows: 6
unique_symbol_count: 6
unique_source_canonical_count: 4
unique_source_large_sector_count: 3
stage4b_overlay_count: 6
stage4c_count: 0
positive_with_guardrail_count: 4
counterexample_count: 6
current_profile_error_count: 6
avg_MFE_30D_pct: 18.1017
avg_MAE_30D_pct: -9.9992
avg_MFE_90D_pct: 22.0231
avg_MAE_90D_pct: -28.4169
avg_MFE_180D_pct: 38.2101
avg_MAE_180D_pct: -35.9580
median_MAE_180D_pct: -24.0408
rows_MAE180_le_minus_20pct: 6
rows_MAE180_le_minus_30pct: 2
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rule_candidate: R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V143
```

## 6. Machine-readable rows

```jsonl
{"row_type":"trigger","trigger_id":"R13_HIGHMAE_L143_112040_20211112_TRG","case_id":"R13_HIGHMAE_L143_112040_20211112","symbol":"112040","company_name":"위메이드","round":"R13","loop":143,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V143","sector":"cross_archetype_redteam_misc","primary_archetype":"cross_archetype_high_mae_guardrail","loop_objective":"holdout_validation|counterexample_mining|4B_non_price_requirement_stress_test|Stage2_Stage3_persistence_MAE_cap","trigger_type":"Stage4B","trigger_date":"2021-11-12","entry_date":"2021-11-12","entry_price":180600.0,"source_round":"R8","source_loop":null,"source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_trigger_type":"Stage3-Yellow","evidence_source":"https://www.asiae.co.kr/en/article/2021111211022190852","evidence_available_at_that_date":"MIR4 exceeded one million concurrent users and continued global traffic expansion.","stage2_evidence_fields":["public_event_or_disclosure","valid_source_sector_evidence"],"stage3_evidence_fields":["not_supported_without_second_bridge_confirmation"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","Stage2_Stage3_persistence_cap_required","second_bridge_confirmation_missing_or_late","local_4B_overlay_required"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.4,"MAE_30D_pct":-10.8,"MFE_90D_pct":35.1,"MAE_90D_pct":-45.6,"MFE_180D_pct":35.1,"MAE_180D_pct":-66.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"peak_date":null,"peak_price":244000.0,"drawdown_after_peak_pct":-75.3,"four_b_timing_verdict":"force_local_4B_overlay_until_second_bridge_confirmation","four_b_evidence_type":"price_path_high_MAE_plus_non_price_bridge_gap","four_c_protection_label":"not_hard_4c_no_confirmed_thesis_break","trigger_outcome_label":"positive_with_guardrail","current_profile_verdict":"current_profile_false_positive_or_persistence_error_if_Stage2_Stage3_not_capped","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_source_sector_row","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_112040_2021-11-12","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"R13_high_MAE_guardrail_replay_of_unused_URL_verified_source_sector_row","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"do_not_count_as_new_sector_case":true,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false,"source_file":"e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md"}
{"row_type":"trigger","trigger_id":"R13_HIGHMAE_L143_241840_20220720_TRG","case_id":"R13_HIGHMAE_L143_241840_20220720","symbol":"241840","company_name":"에이스토리","round":"R13","loop":143,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V143","sector":"cross_archetype_redteam_misc","primary_archetype":"cross_archetype_high_mae_guardrail","loop_objective":"holdout_validation|counterexample_mining|4B_non_price_requirement_stress_test|Stage2_Stage3_persistence_MAE_cap","trigger_type":"Stage4B","trigger_date":"2022-07-20","entry_date":"2022-07-20","entry_price":23600.0,"source_round":"R8","source_loop":null,"source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_trigger_type":"Stage3-Yellow","evidence_source":"https://en.yna.co.kr/view/AEN20220720002700315","evidence_available_at_that_date":"Extraordinary Attorney Woo topped Netflix's non-English viewership chart for a second week.","stage2_evidence_fields":["public_event_or_disclosure","valid_source_sector_evidence"],"stage3_evidence_fields":["not_supported_without_second_bridge_confirmation"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","Stage2_Stage3_persistence_cap_required","second_bridge_confirmation_missing_or_late","local_4B_overlay_required"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":46.2,"MAE_30D_pct":-5.7,"MFE_90D_pct":55.2,"MAE_90D_pct":-36.8,"MFE_180D_pct":55.2,"MAE_180D_pct":-55.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"peak_date":null,"peak_price":36650.0,"drawdown_after_peak_pct":-71.5,"four_b_timing_verdict":"force_local_4B_overlay_until_second_bridge_confirmation","four_b_evidence_type":"price_path_high_MAE_plus_non_price_bridge_gap","four_c_protection_label":"not_hard_4c_no_confirmed_thesis_break","trigger_outcome_label":"positive_with_guardrail","current_profile_verdict":"current_profile_false_positive_or_persistence_error_if_Stage2_Stage3_not_capped","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_source_sector_row","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_241840_2022-07-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"R13_high_MAE_guardrail_replay_of_unused_URL_verified_source_sector_row","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"do_not_count_as_new_sector_case":true,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false,"source_file":"e2r_stock_web_v12_residual_round_R8_loop_100_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md"}
{"row_type":"trigger","trigger_id":"R13_HIGHMAE_L143_278280_20250108_TRG","case_id":"R13_HIGHMAE_L143_278280_20250108","symbol":"278280","company_name":"천보","round":"R13","loop":143,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V143","sector":"cross_archetype_redteam_misc","primary_archetype":"cross_archetype_high_mae_guardrail","loop_objective":"holdout_validation|counterexample_mining|4B_non_price_requirement_stress_test|Stage2_Stage3_persistence_MAE_cap","trigger_type":"Stage4B","trigger_date":"2025-01-08","entry_date":"2025-01-08","entry_price":39750.0,"source_round":null,"source_loop":null,"source_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","source_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","source_trigger_type":"Stage2-Actionable","evidence_source":"https://www.dailyinvest.kr/news/articleView.html?idxno=62801","evidence_available_at_that_date":"January 2025 coverage still described customer inventory adjustment and volume decline in LiPO2F2 while expecting 2025 recovery. Price path opened MFE later, but initial MAE and absent call-off clearance argue for Stage2-Watch before Stage3.","stage2_evidence_fields":["public_event_or_disclosure","valid_source_sector_evidence"],"stage3_evidence_fields":["not_supported_without_second_bridge_confirmation"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","Stage2_Stage3_persistence_cap_required","second_bridge_confirmation_missing_or_late","local_4B_overlay_required"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.0377,"MAE_30D_pct":-13.5849,"MFE_90D_pct":6.0377,"MAE_90D_pct":-24.4025,"MFE_180D_pct":28.5535,"MAE_180D_pct":-24.4025,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"peak_date":"2025-07-21","peak_price":51100.0,"drawdown_after_peak_pct":-20.5479,"four_b_timing_verdict":"force_local_4B_overlay_until_second_bridge_confirmation","four_b_evidence_type":"price_path_high_MAE_plus_non_price_bridge_gap","four_c_protection_label":"not_hard_4c_no_confirmed_thesis_break","trigger_outcome_label":"counterexample_high_MAE_bridge_gap","current_profile_verdict":"current_profile_false_positive_or_persistence_error_if_Stage2_Stage3_not_capped","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_source_sector_row","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_278280_2025-01-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"R13_high_MAE_guardrail_replay_of_unused_URL_verified_source_sector_row","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"do_not_count_as_new_sector_case":true,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false,"source_file":"e2r_stock_web_v12_residual_round_R3_loop_109_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md"}
{"row_type":"trigger","trigger_id":"R13_HIGHMAE_L143_054930_20240813_TRG","case_id":"R13_HIGHMAE_L143_054930_20240813","symbol":"054930","company_name":"유신","round":"R13","loop":143,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V143","sector":"cross_archetype_redteam_misc","primary_archetype":"cross_archetype_high_mae_guardrail","loop_objective":"holdout_validation|counterexample_mining|4B_non_price_requirement_stress_test|Stage2_Stage3_persistence_MAE_cap","trigger_type":"Stage4B","trigger_date":"2024-08-13","entry_date":"2024-08-13","entry_price":25550.0,"source_round":"R1","source_loop":119,"source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_trigger_type":"Stage2","evidence_source":"https://m.kisrating.com/fileDown.do?fileName=rs20240813-15.pdf&gubun=2&menuCd=R8","evidence_available_at_that_date":"신용평가 자료는 유신이 토목엔지니어링 분야에서 수주실적·기술인력·수주경쟁력을 보유한다고 평가했다. 하지만 이는 반복 용역/공공 SOC exposure이지 mega EPC margin bridge가 아니므로 C05 Stage3 과승격을 막아야 한다.","stage2_evidence_fields":["public_event_or_disclosure","valid_source_sector_evidence"],"stage3_evidence_fields":["not_supported_without_second_bridge_confirmation"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","Stage2_Stage3_persistence_cap_required","second_bridge_confirmation_missing_or_late","local_4B_overlay_required"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.9354,"MAE_30D_pct":-20.3523,"MFE_90D_pct":10.7632,"MAE_90D_pct":-20.3523,"MFE_180D_pct":10.7632,"MAE_180D_pct":-23.6791,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"peak_date":"2024-11-13","peak_price":28300.0,"drawdown_after_peak_pct":-31.0954,"four_b_timing_verdict":"force_local_4B_overlay_until_second_bridge_confirmation","four_b_evidence_type":"price_path_high_MAE_plus_non_price_bridge_gap","four_c_protection_label":"not_hard_4c_no_confirmed_thesis_break","trigger_outcome_label":"counterexample_high_MAE_bridge_gap","current_profile_verdict":"current_profile_false_positive_or_persistence_error_if_Stage2_Stage3_not_capped","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_dates_or_no_overlap","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_054930_2024-08-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"R13_high_MAE_guardrail_replay_of_unused_URL_verified_source_sector_row","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"do_not_count_as_new_sector_case":true,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false,"source_file":"e2r_stock_web_v12_residual_round_R1_loop_119_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md"}
{"row_type":"trigger","trigger_id":"R13_HIGHMAE_L143_023350_20240517_TRG","case_id":"R13_HIGHMAE_L143_023350_20240517","symbol":"023350","company_name":"한국종합기술","round":"R13","loop":143,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V143","sector":"cross_archetype_redteam_misc","primary_archetype":"cross_archetype_high_mae_guardrail","loop_objective":"holdout_validation|counterexample_mining|4B_non_price_requirement_stress_test|Stage2_Stage3_persistence_MAE_cap","trigger_type":"Stage4B","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":5470.0,"source_round":"R1","source_loop":119,"source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","source_trigger_type":"Stage2","evidence_source":"https://m.kisrating.com/fileDown.do?fileName=rs20240517-12.pdf&gubun=2&menuCd=R8","evidence_available_at_that_date":"한국기업평가 리포트는 종합엔지니어링 사업기반, 주요 사업 수주 증대, 시공부문 확대를 통한 외형 성장을 언급했다. C05에서는 안정적 order backlog evidence로 인정하되, 단일 mega EPC contract가 아니라 Stage2/Stage3-Yellow 후보로 제한한다.","stage2_evidence_fields":["public_event_or_disclosure","valid_source_sector_evidence"],"stage3_evidence_fields":["not_supported_without_second_bridge_confirmation"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","Stage2_Stage3_persistence_cap_required","second_bridge_confirmation_missing_or_late","local_4B_overlay_required"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.5174,"MAE_30D_pct":-3.1079,"MFE_90D_pct":11.5174,"MAE_90D_pct":-21.2066,"MFE_180D_pct":44.4241,"MAE_180D_pct":-23.1261,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"peak_date":"2024-12-13","peak_price":7900.0,"drawdown_after_peak_pct":-35.1899,"four_b_timing_verdict":"force_local_4B_overlay_until_second_bridge_confirmation","four_b_evidence_type":"price_path_high_MAE_plus_non_price_bridge_gap","four_c_protection_label":"not_hard_4c_no_confirmed_thesis_break","trigger_outcome_label":"positive_with_guardrail","current_profile_verdict":"current_profile_false_positive_or_persistence_error_if_Stage2_Stage3_not_capped","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_dates_or_no_overlap","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_023350_2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"R13_high_MAE_guardrail_replay_of_unused_URL_verified_source_sector_row","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"do_not_count_as_new_sector_case":true,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false,"source_file":"e2r_stock_web_v12_residual_round_R1_loop_119_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md"}
{"row_type":"trigger","trigger_id":"R13_HIGHMAE_L143_100090_20240822_TRG","case_id":"R13_HIGHMAE_L143_100090_20240822","symbol":"100090","company_name":"SK오션플랜트","round":"R13","loop":143,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"R13_HIGH_MAE_GUARDRAIL_UNUSED_URL_VERIFIED_MINI_HOLDOUT_V143","sector":"cross_archetype_redteam_misc","primary_archetype":"cross_archetype_high_mae_guardrail","loop_objective":"holdout_validation|counterexample_mining|4B_non_price_requirement_stress_test|Stage2_Stage3_persistence_MAE_cap","trigger_type":"Stage4B","trigger_date":"2024-08-22","entry_date":"2024-08-22","entry_price":14270.0,"source_round":"R1","source_loop":115,"source_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","source_canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","source_trigger_type":"Stage4B","evidence_source":"https://www.hanaw.com/download/research/FileServer/WEB/industry/enterprise/2024/08/21/SKO_240822_Initiation.pdf","evidence_available_at_that_date":"source-sector evidence row replayed for R13 high-MAE guardrail","stage2_evidence_fields":["public_event_or_disclosure","valid_source_sector_evidence"],"stage3_evidence_fields":["not_supported_without_second_bridge_confirmation"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","Stage2_Stage3_persistence_cap_required","second_bridge_confirmation_missing_or_late","local_4B_overlay_required"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.52,"MAE_30D_pct":-6.45,"MFE_90D_pct":13.52,"MAE_90D_pct":-22.14,"MFE_180D_pct":55.22,"MAE_180D_pct":-22.14,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"peak_date":"2025-05-19","peak_price":22150.0,"drawdown_after_peak_pct":-20.5,"four_b_timing_verdict":"force_local_4B_overlay_until_second_bridge_confirmation","four_b_evidence_type":"price_path_high_MAE_plus_non_price_bridge_gap","four_c_protection_label":"not_hard_4c_no_confirmed_thesis_break","trigger_outcome_label":"positive_with_guardrail","current_profile_verdict":"current_profile_false_positive_or_persistence_error_if_Stage2_Stage3_not_capped","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_from_source_sector_row","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_100090_2024-08-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"R13_high_MAE_guardrail_replay_of_unused_URL_verified_source_sector_row","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"do_not_count_as_new_sector_case":true,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false,"source_file":"e2r_stock_web_v12_residual_round_R1_loop_115_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md"}
{"row_type":"score_simulation","case_id":"R13_HIGHMAE_L143_112040_20211112","symbol":"112040","company_name":"위메이드","profile_id_before":"e2r_2_2_rolling_calibrated_proxy","profile_id_after":"R13_high_MAE_shadow_profile_v143","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"evidence_bridge_score":55,"price_path_quality_score":33.3,"relative_strength_score":50,"non_price_confirmation_score":45,"execution_risk_score":70,"accounting_trust_risk_score":25,"local_4b_pressure_score":88},"weighted_score_before":60,"stage_label_before":"Stage2_or_Stage3_persistence_possible_under_source_sector_profile","raw_component_scores_after":{"evidence_bridge_score":42,"price_path_quality_score":33.3,"relative_strength_score":38,"non_price_confirmation_score":36,"execution_risk_score":82,"accounting_trust_risk_score":25,"local_4b_pressure_score":95},"weighted_score_after":46,"stage_label_after":"Stage2-Watch_or_Stage4B-LocalWatch_until_second_bridge_confirmation","component_delta_explanation":"R13 high-MAE guardrail caps Stage2/Stage3 persistence when MAE90/MAE180 breaches without delivery/revenue/margin/FCF/utilization/retention bridge."}
{"row_type":"score_simulation","case_id":"R13_HIGHMAE_L143_241840_20220720","symbol":"241840","company_name":"에이스토리","profile_id_before":"e2r_2_2_rolling_calibrated_proxy","profile_id_after":"R13_high_MAE_shadow_profile_v143","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"evidence_bridge_score":55,"price_path_quality_score":44.3,"relative_strength_score":50,"non_price_confirmation_score":45,"execution_risk_score":70,"accounting_trust_risk_score":25,"local_4b_pressure_score":88},"weighted_score_before":60,"stage_label_before":"Stage2_or_Stage3_persistence_possible_under_source_sector_profile","raw_component_scores_after":{"evidence_bridge_score":42,"price_path_quality_score":44.3,"relative_strength_score":38,"non_price_confirmation_score":36,"execution_risk_score":82,"accounting_trust_risk_score":25,"local_4b_pressure_score":95},"weighted_score_after":46,"stage_label_after":"Stage2-Watch_or_Stage4B-LocalWatch_until_second_bridge_confirmation","component_delta_explanation":"R13 high-MAE guardrail caps Stage2/Stage3 persistence when MAE90/MAE180 breaches without delivery/revenue/margin/FCF/utilization/retention bridge."}
{"row_type":"score_simulation","case_id":"R13_HIGHMAE_L143_278280_20250108","symbol":"278280","company_name":"천보","profile_id_before":"e2r_2_2_rolling_calibrated_proxy","profile_id_after":"R13_high_MAE_shadow_profile_v143","source_canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"evidence_bridge_score":55,"price_path_quality_score":75.6,"relative_strength_score":44,"non_price_confirmation_score":45,"execution_risk_score":62,"accounting_trust_risk_score":25,"local_4b_pressure_score":78},"weighted_score_before":52,"stage_label_before":"Stage2_or_Stage3_persistence_possible_under_source_sector_profile","raw_component_scores_after":{"evidence_bridge_score":42,"price_path_quality_score":75.6,"relative_strength_score":38,"non_price_confirmation_score":36,"execution_risk_score":72,"accounting_trust_risk_score":25,"local_4b_pressure_score":95},"weighted_score_after":43,"stage_label_after":"Stage2-Watch_or_Stage4B-LocalWatch_until_second_bridge_confirmation","component_delta_explanation":"R13 high-MAE guardrail caps Stage2/Stage3 persistence when MAE90/MAE180 breaches without delivery/revenue/margin/FCF/utilization/retention bridge."}
{"row_type":"score_simulation","case_id":"R13_HIGHMAE_L143_054930_20240813","symbol":"054930","company_name":"유신","profile_id_before":"e2r_2_2_rolling_calibrated_proxy","profile_id_after":"R13_high_MAE_shadow_profile_v143","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"evidence_bridge_score":55,"price_path_quality_score":76.32,"relative_strength_score":44,"non_price_confirmation_score":45,"execution_risk_score":62,"accounting_trust_risk_score":25,"local_4b_pressure_score":78},"weighted_score_before":52,"stage_label_before":"Stage2_or_Stage3_persistence_possible_under_source_sector_profile","raw_component_scores_after":{"evidence_bridge_score":42,"price_path_quality_score":76.32,"relative_strength_score":38,"non_price_confirmation_score":36,"execution_risk_score":72,"accounting_trust_risk_score":25,"local_4b_pressure_score":95},"weighted_score_after":43,"stage_label_after":"Stage2-Watch_or_Stage4B-LocalWatch_until_second_bridge_confirmation","component_delta_explanation":"R13 high-MAE guardrail caps Stage2/Stage3 persistence when MAE90/MAE180 breaches without delivery/revenue/margin/FCF/utilization/retention bridge."}
{"row_type":"score_simulation","case_id":"R13_HIGHMAE_L143_023350_20240517","symbol":"023350","company_name":"한국종합기술","profile_id_before":"e2r_2_2_rolling_calibrated_proxy","profile_id_after":"R13_high_MAE_shadow_profile_v143","source_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"evidence_bridge_score":55,"price_path_quality_score":76.87,"relative_strength_score":50,"non_price_confirmation_score":45,"execution_risk_score":62,"accounting_trust_risk_score":25,"local_4b_pressure_score":78},"weighted_score_before":60,"stage_label_before":"Stage2_or_Stage3_persistence_possible_under_source_sector_profile","raw_component_scores_after":{"evidence_bridge_score":42,"price_path_quality_score":76.87,"relative_strength_score":38,"non_price_confirmation_score":36,"execution_risk_score":72,"accounting_trust_risk_score":25,"local_4b_pressure_score":95},"weighted_score_after":51,"stage_label_after":"Stage2-Watch_or_Stage4B-LocalWatch_until_second_bridge_confirmation","component_delta_explanation":"R13 high-MAE guardrail caps Stage2/Stage3 persistence when MAE90/MAE180 breaches without delivery/revenue/margin/FCF/utilization/retention bridge."}
{"row_type":"score_simulation","case_id":"R13_HIGHMAE_L143_100090_20240822","symbol":"100090","company_name":"SK오션플랜트","profile_id_before":"e2r_2_2_rolling_calibrated_proxy","profile_id_after":"R13_high_MAE_shadow_profile_v143","source_canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"evidence_bridge_score":55,"price_path_quality_score":77.86,"relative_strength_score":50,"non_price_confirmation_score":45,"execution_risk_score":62,"accounting_trust_risk_score":25,"local_4b_pressure_score":78},"weighted_score_before":60,"stage_label_before":"Stage2_or_Stage3_persistence_possible_under_source_sector_profile","raw_component_scores_after":{"evidence_bridge_score":42,"price_path_quality_score":77.86,"relative_strength_score":38,"non_price_confirmation_score":36,"execution_risk_score":72,"accounting_trust_risk_score":25,"local_4b_pressure_score":95},"weighted_score_after":51,"stage_label_after":"Stage2-Watch_or_Stage4B-LocalWatch_until_second_bridge_confirmation","component_delta_explanation":"R13 high-MAE guardrail caps Stage2/Stage3 persistence when MAE90/MAE180 breaches without delivery/revenue/margin/FCF/utilization/retention bridge."}
{"row_type":"aggregate","case_id":"R13_HIGHMAE_L143_AGGREGATE","round":"R13","loop":143,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","calibration_usable_rows":6,"representative_rows":6,"unique_symbol_count":6,"unique_source_canonical_count":4,"unique_source_large_sector_count":3,"stage4b_overlay_count":6,"stage4c_count":0,"positive_with_guardrail_count":4,"counterexample_count":6,"avg_MFE_30D_pct":18.1017,"avg_MAE_30D_pct":-9.9992,"avg_MFE_90D_pct":22.0231,"avg_MAE_90D_pct":-28.4169,"avg_MFE_180D_pct":38.2101,"avg_MAE_180D_pct":-35.958,"median_MAE_180D_pct":-24.0408,"rows_MAE180_le_minus_20pct":6,"rows_MAE180_le_minus_30pct":2,"source_proxy_only_rows":0,"evidence_url_pending_rows":0,"rule_candidate":"R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V143"}
{"row_type":"shadow_weight","axis":"R13_high_MAE_guardrail_shadow_axis","rule_candidate":"R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V143","suggested_action":"cap Stage2/Stage3 persistence to Stage2-Watch or Stage4B-LocalWatch when MAE90<=-20 or MAE180<=-25 and second bridge is missing","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","residual_error_found":true,"current_profile_error_count":6,"new_axis_proposed":"R13_high_MAE_guardrail_shadow_axis_v143","existing_axis_strengthened":["local_4b_watch_guard","stage2_required_bridge"],"existing_axis_weakened":[]}
{"row_type":"narrative_only","summary":"Mini holdout of URL-verified source-sector rows not yet used in R13 high-MAE guardrail. Valid evidence alone should not preserve Stage2/Stage3 when MAE90/MAE180 breaches before a second bridge confirms delivery, revenue, margin, cash, retention, or utilization."}
```

## 7. Shadow rule candidate

```text
R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V143
```

Rule logic:

```text
if source-sector Stage2 or Stage3 evidence exists
and MAE_90D_pct <= -20 or MAE_180D_pct <= -25
and delivery/revenue/margin/FCF/utilization/retention/sell-through/cash bridge is not confirmed:
    cap stage persistence to Stage2-Watch or Stage4B-LocalWatch
else:
    keep source-sector stage logic unchanged
```

## 8. Residual contribution summary

```yaml
loop_contribution_label: holdout_validation_passed
new_axis_proposed: R13_high_MAE_guardrail_shadow_axis_v143
existing_axis_strengthened:
  - local_4b_watch_guard
  - stage2_required_bridge
existing_axis_weakened: []
do_not_propose_new_weight_delta: false
production_scoring_changed: false
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
Do not execute in this research session.

In a later stock_agent implementation session, ingest this MD with the other V12 research files. Validate all trigger rows, preserve do_not_count_as_new_sector_case=true for R13 replay rows, and evaluate the shadow rule candidate R13_HIGH_MAE_GUARDRAIL_REQUIRE_SECOND_BRIDGE_CONFIRMATION_OR_STAGE4B_OVERLAY_V143 as a local guardrail only. Do not change production scoring unless batch validation confirms that the rule improves false-positive control without blocking verified late-stage positives.
```

## 11. Next research state

```text
completed_round = R13
completed_loop = 143
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = R13 cross-archetype high-MAE mini holdout after session-adjusted Priority-0/Priority-1 fills
next_recommended_archetypes = R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_holdout_quality_only | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path | C05_EPC_MEGA_CONTRACT_MARGIN_GAP_holdout_only_if_new_working_capital_path
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

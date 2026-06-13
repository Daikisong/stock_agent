# E2R Stock-Web v12 Residual Research — R2 / L2 / C07 HBM Equipment Order Relative Strength / loop 140

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_patch_allowed: false
current_stock_discovery_allowed: false
price_route_hunt_allowed: false
output_format: one_standalone_markdown_file
completed_round: R2
completed_loop: 140
selected_round: R2
selected_loop: 140
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: mixed_c07_tcbonder_refow_cleaning_tester_second_pass_leaf_set
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
new_independent_case_count: 6
usable_trigger_row_count: 8
representative_trigger_count: 8
positive_case_count: 3
counterexample_count: 5
stage4b_watch_or_overlay_count: 6
current_profile_error_count: 7
index_baseline_coverage_before: C07 rows 18
index_baseline_coverage_after_if_accepted: C07 rows 26
session_aware_after_loop130_and_loop140: about C07 rows 31
do_not_propose_new_weight_delta: false
canonical_archetype_rule_candidate: C07_ORDER_SIZE_TIMING_AND_STAGED_ENTRY_MAE_GATE_V2
loop_contribution_label: canonical_archetype_rule_candidate
```

## 1. Selection rationale

No-Repeat Index 기준 C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH는 Priority 0 / 18 rows / need to 30 = 12로 남아 있다. 이 세션에서는 loop 130에서 와이씨·테크윙·엑시콘을 이미 사용했으므로, 이번 loop 140은 042700·039440·031980·451220·079370·003160으로 구성했다. Round는 R2/L2로 파생했고, R1~R13 순환은 사용하지 않았다.

이번 연구의 질문은 단순하다. C07에서 signed order는 항상 좋은가? 아니면 signed order라도 이미 상대강도가 과열된 뒤라면 4B/high-MAE guard가 먼저 와야 하는가? 장비주에서는 수주가 엔진이지만, 너무 늦게 들은 엔진 소리는 이미 지나간 열차의 메아리일 수 있다.

## 2. Stock-Web validation

- primary_price_source: Songdaiki/stock-web
- price_basis: tradable_raw
- price_adjustment_status: raw_unadjusted_marcap
- stock_web_manifest_max_date: 2026-02-20
- MFE/MAE rule: entry_date의 close를 entry_price로 사용하고, entry row 포함 이후 30/90/180 tradable rows의 max high와 min low를 비교했다.
- 180D forward window: all trigger rows usable.

| ticker | profile corporate-action note |
|---|---|
| 042700 | profile corporate_action_candidate_dates=[2006-11-10,2017-05-11,2022-04-06]; no overlap with 2024 entry~D180 windows. |
| 039440 | profile corporate_action_candidate_dates=[2002-11-11,2006-01-24,2018-04-20]; no overlap with 2023/2024 entry~D180 windows. |
| 031980 | profile corporate_action_candidate_dates=[1998-07-28,2000-04-20,2007-03-16,2019-05-10,2020-02-21]; no overlap with 2024 entry~D180 window. |
| 451220 | profile corporate_action_candidate_dates=[]; no overlap. |
| 079370 | profile corporate_action_candidate_dates=[2024-01-16,2024-02-08]; selected entry 2024-05-23 so no overlap with entry~D180 window. |
| 003160 | profile corporate_action_candidate_dates=[1997-01-03,1998-07-03,1999-10-18]; no overlap with 2025 entry~D180 window. |

## 3. Case table

| case | ticker | trigger | entry | MFE90 | MAE90 | MFE180 | MAE180 | verdict | residual |
|---|---:|---|---:|---:|---:|---:|---:|---|---|
| C07_L140_CASE01_HANMI_202402_SKHYNIX_TCBONDER_860BN | 042700 | Stage2-Actionable | 2024-02-05 / 58800 | 233.67 | -0.68 | 233.67 | -0.68 | positive | none_or_minor_too_late_risk |
| C07_L140_CASE02_HANMI_202406_SKHYNIX_TCBONDER_1499BN_LATE | 042700 | Stage4B-Watch | 2024-06-10 / 160000 | 22.63 | -42.94 | 22.63 | -56.62 | counterexample | false_positive_without_timing_mae_guard |
| C07_L140_CASE03_STI_202308_HBM_REFLOW_ORDER | 039440 | Stage2-Actionable | 2023-08-07 / 24900 | 51.0 | -4.22 | 73.69 | -4.22 | positive | too_conservative_if_named_hbm_reflow_order_not_actionable |
| C07_L140_CASE04_STI_202405_HBM_REFLOW_MARGIN_LATE | 039440 | Stage4B-Watch | 2024-05-22 / 34150 | 23.28 | -45.53 | 23.28 | -60.12 | counterexample | false_positive_late_relative_strength_decay |
| C07_L140_CASE05_PSKH_202405_MICRON_REFLOW_SUPPLY | 031980 | Stage2-Actionable | 2024-05-31 / 54900 | 55.37 | -34.24 | 55.37 | -49.54 | positive_with_4b_overlay | positive_but_requires_4b_overlay_after_fast_mfe |
| C07_L140_CASE06_IMT_202404_MICRON_SMALL_HBM_CLEANING_ORDER | 451220 | Stage2-Watch | 2024-04-30 / 20050 | 25.94 | -62.54 | 25.94 | -69.53 | counterexample | false_positive_small_order_size_missing_revenue_bridge |
| C07_L140_CASE07_ZEUS_202405_HBM_CLEANING_ORDER_ESTIMATE | 079370 | Stage2-Watch | 2024-05-23 / 19010 | 2.84 | -44.77 | 2.84 | -46.29 | counterexample | false_positive_estimate_only_and_relative_strength_decay |
| C07_L140_CASE08_DI_202502_SKHYNIX_HBM_DDR5_TESTER_ORDER | 003160 | Stage2-Watch | 2025-02-24 / 16400 | 7.32 | -33.72 | 69.51 | -33.72 | counterexample_with_late_recovery | false_positive_without_staged_entry_despite_signed_order |

## 4. Trigger rows JSONL

```jsonl
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_140_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":140,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_TCBONDER_SIGNED_ORDER_NAMED_CUSTOMER_EARLY_PHASE","case_id":"C07_L140_CASE01_HANMI_202402_SKHYNIX_TCBONDER_860BN","ticker":"042700","company_name":"한미반도체","trigger_type":"Stage2-Actionable","observed_label":"positive","evidence_date":"2024-02-02","entry_date":"2024-02-05","entry_price":58800.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":83.33,"MAE_30D_pct":-0.68,"MFE_90D_pct":233.67,"MAE_90D_pct":-0.68,"MFE_180D_pct":233.67,"MAE_180D_pct":-0.68,"peak_30D_date":"2024-03-07","trough_30D_date":"2024-02-06","peak_90D_date":"2024-06-14","trough_90D_date":"2024-02-06","peak_180D_date":"2024-06-14","trough_180D_date":"2024-02-06","evidence_summary":"SK하이닉스향 860억원 규모 HBM TC본더 수주. 고객명, 계약금액, 납기, HBM capacity expansion narrative가 동시에 확인된 early order-backed relative strength case.","evidence_url":"https://www.etnews.com/20240202000111","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":21,"earnings_visibility":21,"bottleneck_pricing":20,"market_mispricing":14,"valuation_rerating":12,"capital_allocation":5,"information_confidence":7},"current_profile_expected_stage":"Stage2-Actionable","residual_error_type":"none_or_minor_too_late_risk","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|042700|Stage2-Actionable|2024-02-05","raw_score_total":100}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_140_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":140,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_TCBONDER_LATE_MEGA_ORDER_HIGH_MAE","case_id":"C07_L140_CASE02_HANMI_202406_SKHYNIX_TCBONDER_1499BN_LATE","ticker":"042700","company_name":"한미반도체","trigger_type":"Stage4B-Watch","observed_label":"counterexample","evidence_date":"2024-06-07","entry_date":"2024-06-10","entry_price":160000.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":22.63,"MAE_30D_pct":-7.13,"MFE_90D_pct":22.63,"MAE_90D_pct":-42.94,"MFE_180D_pct":22.63,"MAE_180D_pct":-56.62,"peak_30D_date":"2024-06-14","trough_30D_date":"2024-07-18","peak_90D_date":"2024-06-14","trough_90D_date":"2024-09-19","peak_180D_date":"2024-06-14","trough_180D_date":"2024-12-11","evidence_summary":"SK하이닉스향 1499억원 HBM TC본더 추가 수주. 계약 bridge는 강하지만 이미 2024년 상반기 상대강도가 과열되어 이후 D90/D180 MAE가 매우 커진 late order case.","evidence_url":"https://www.yna.co.kr/view/AKR20240607063600003","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":22,"earnings_visibility":21,"bottleneck_pricing":20,"market_mispricing":8,"valuation_rerating":6,"capital_allocation":5,"information_confidence":8},"current_profile_expected_stage":"Stage2-Actionable","residual_error_type":"false_positive_without_timing_mae_guard","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|042700|Stage4B-Watch|2024-06-10","raw_score_total":90}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_140_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":140,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_REFLOW_SIGNED_ORDER_EARLY_REVENUE_CONVERSION","case_id":"C07_L140_CASE03_STI_202308_HBM_REFLOW_ORDER","ticker":"039440","company_name":"에스티아이","trigger_type":"Stage2-Actionable","observed_label":"positive","evidence_date":"2023-08-04","entry_date":"2023-08-07","entry_price":24900.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/039/039440/2023.csv","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":38.96,"MAE_30D_pct":-4.22,"MFE_90D_pct":51.0,"MAE_90D_pct":-4.22,"MFE_180D_pct":73.69,"MAE_180D_pct":-4.22,"peak_30D_date":"2023-09-12","trough_30D_date":"2023-08-28","peak_90D_date":"2023-11-15","trough_90D_date":"2023-08-28","peak_180D_date":"2024-03-13","trough_180D_date":"2023-08-28","evidence_summary":"글로벌 반도체 기업향 HBM3용 플럭스 리플로우 장비 수주. HBM 장비 vocabulary가 아니라 실제 납품 장비와 공정 용도가 확인된 early positive.","evidence_url":"https://www.thelec.kr/news/articleView.html?idxno=22391","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":19,"earnings_visibility":20,"bottleneck_pricing":18,"market_mispricing":15,"valuation_rerating":13,"capital_allocation":5,"information_confidence":8},"current_profile_expected_stage":"Stage2-Watch","residual_error_type":"too_conservative_if_named_hbm_reflow_order_not_actionable","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|039440|Stage2-Actionable|2023-08-07","raw_score_total":98}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_140_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":140,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_REFLOW_LATE_MARGIN_STORY_HIGH_MAE","case_id":"C07_L140_CASE04_STI_202405_HBM_REFLOW_MARGIN_LATE","ticker":"039440","company_name":"에스티아이","trigger_type":"Stage4B-Watch","observed_label":"counterexample","evidence_date":"2024-05-21","entry_date":"2024-05-22","entry_price":34150.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/039/039440/2024.csv","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":23.28,"MAE_30D_pct":-9.22,"MFE_90D_pct":23.28,"MAE_90D_pct":-45.53,"MFE_180D_pct":23.28,"MAE_180D_pct":-60.12,"peak_30D_date":"2024-06-26","trough_30D_date":"2024-06-03","peak_90D_date":"2024-06-26","trough_90D_date":"2024-09-19","peak_180D_date":"2024-06-26","trough_180D_date":"2024-12-10","evidence_summary":"HBM용 플럭스/플럭스리스 리플로우 장비와 고마진 수주 narrative가 재부각. 그러나 2023년 order-backed run 이후 2024년 5월 진입은 D90/D180 MAE가 커서 late headline guard가 필요했다.","evidence_url":"https://www.dailyinvest.kr/news/articleView.html?idxno=58804","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":18,"earnings_visibility":18,"bottleneck_pricing":17,"market_mispricing":9,"valuation_rerating":7,"capital_allocation":5,"information_confidence":7},"current_profile_expected_stage":"Stage2-Actionable","residual_error_type":"false_positive_late_relative_strength_decay","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|039440|Stage4B-Watch|2024-05-22","raw_score_total":81}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_140_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":140,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_REFLOW_MULTI_CUSTOMER_SUPPLY_HIGH_BETA","case_id":"C07_L140_CASE05_PSKH_202405_MICRON_REFLOW_SUPPLY","ticker":"031980","company_name":"피에스케이홀딩스","trigger_type":"Stage2-Actionable","observed_label":"positive_with_4b_overlay","evidence_date":"2024-05-30","entry_date":"2024-05-31","entry_price":54900.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":55.37,"MAE_30D_pct":-3.64,"MFE_90D_pct":55.37,"MAE_90D_pct":-34.24,"MFE_180D_pct":55.37,"MAE_180D_pct":-49.54,"peak_30D_date":"2024-06-19","trough_30D_date":"2024-06-03","peak_90D_date":"2024-06-19","trough_90D_date":"2024-09-19","peak_180D_date":"2024-06-19","trough_180D_date":"2024-12-09","evidence_summary":"마이크론향 HBM 양산용 리플로우 장비 공급이 뒤늦게 확인. 삼성전자·SK하이닉스·마이크론 3사 공급 레퍼런스라는 customer-breadth bridge가 있었지만 D90/D180 drawdown도 커서 staged-entry overlay가 필요했다.","evidence_url":"https://www.thelec.kr/news/articleView.html?idxno=28196","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":20,"earnings_visibility":19,"bottleneck_pricing":18,"market_mispricing":14,"valuation_rerating":11,"capital_allocation":5,"information_confidence":8},"current_profile_expected_stage":"Stage2-Actionable","residual_error_type":"positive_but_requires_4b_overlay_after_fast_mfe","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|031980|Stage2-Actionable|2024-05-31","raw_score_total":95}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_140_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":140,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_SMALL_SIGNED_ORDER_NOT_ENOUGH_FOR_ACTIONABLE","case_id":"C07_L140_CASE06_IMT_202404_MICRON_SMALL_HBM_CLEANING_ORDER","ticker":"451220","company_name":"아이엠티","trigger_type":"Stage2-Watch","observed_label":"counterexample","evidence_date":"2024-04-29","entry_date":"2024-04-30","entry_price":20050.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/451/451220/2024.csv","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":25.94,"MAE_30D_pct":-11.17,"MFE_90D_pct":25.94,"MAE_90D_pct":-62.54,"MFE_180D_pct":25.94,"MAE_180D_pct":-69.53,"peak_30D_date":"2024-05-29","trough_30D_date":"2024-05-21","peak_90D_date":"2024-05-29","trough_90D_date":"2024-09-09","peak_180D_date":"2024-05-29","trough_180D_date":"2024-12-09","evidence_summary":"마이크론향 HBM용 Wafer 세정장비 공급계약은 실제 공시였지만 8.7억원 규모로 작고, 이후 추가 수주/매출 bridge가 약해 D90/D180 MAE가 매우 컸다.","evidence_url":"https://www.hankyung.com/article/202404294914L","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":12,"earnings_visibility":12,"bottleneck_pricing":15,"market_mispricing":9,"valuation_rerating":7,"capital_allocation":4,"information_confidence":7},"current_profile_expected_stage":"Stage2-Actionable","residual_error_type":"false_positive_small_order_size_missing_revenue_bridge","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|451220|Stage2-Watch|2024-04-30","raw_score_total":66}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_140_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":140,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_ESTIMATED_ORDER_SIZE_WITHOUT_CONFIRMED_CONVERSION","case_id":"C07_L140_CASE07_ZEUS_202405_HBM_CLEANING_ORDER_ESTIMATE","ticker":"079370","company_name":"제우스","trigger_type":"Stage2-Watch","observed_label":"counterexample","evidence_date":"2024-05-22","entry_date":"2024-05-23","entry_price":19010.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/079/079370/2024.csv","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":2.84,"MAE_30D_pct":-12.26,"MFE_90D_pct":2.84,"MAE_90D_pct":-44.77,"MFE_180D_pct":2.84,"MAE_180D_pct":-46.29,"peak_30D_date":"2024-05-23","trough_30D_date":"2024-07-03","peak_90D_date":"2024-05-23","trough_90D_date":"2024-08-05","peak_180D_date":"2024-05-23","trough_180D_date":"2024-12-09","evidence_summary":"HBM 세정장비 매출 인식과 대규모 수주 추정 narrative. 그러나 확인된 고객·계약·납기 bridge가 약했고, 2024년 초 corporate action 이후에도 5월 entry의 D90/D180 MAE가 매우 컸다.","evidence_url":"https://www.dailyinvest.kr/news/articleView.html?idxno=58834","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":11,"earnings_visibility":11,"bottleneck_pricing":15,"market_mispricing":8,"valuation_rerating":6,"capital_allocation":4,"information_confidence":5},"current_profile_expected_stage":"Stage2-Actionable","residual_error_type":"false_positive_estimate_only_and_relative_strength_decay","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|079370|Stage2-Watch|2024-05-23","raw_score_total":60}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_140_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":140,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_SIGNED_TESTER_ORDER_BUT_STAGED_ENTRY_REQUIRED","case_id":"C07_L140_CASE08_DI_202502_SKHYNIX_HBM_DDR5_TESTER_ORDER","ticker":"003160","company_name":"디아이","trigger_type":"Stage2-Watch","observed_label":"counterexample_with_late_recovery","evidence_date":"2025-02-21","entry_date":"2025-02-24","entry_price":16400.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/003/003160/2025.csv","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":7.32,"MAE_30D_pct":-33.72,"MFE_90D_pct":7.32,"MAE_90D_pct":-33.72,"MFE_180D_pct":69.51,"MAE_180D_pct":-33.72,"peak_30D_date":"2025-02-24","trough_30D_date":"2025-03-11","peak_90D_date":"2025-02-24","trough_90D_date":"2025-03-11","peak_180D_date":"2025-11-13","trough_180D_date":"2025-03-11","evidence_summary":"자회사 디지털프론티어가 SK하이닉스와 약 870억원 규모 HBM·DDR5 tester 공급계약. signed order는 강하지만 진입 직후 D30/D90 MAE가 -33%대라 C07에서는 order-only actionable보다 staged-entry guard가 맞다.","evidence_url":"https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2025/02/20/250221_DI_Comment.pdf","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":18,"earnings_visibility":17,"bottleneck_pricing":17,"market_mispricing":8,"valuation_rerating":7,"capital_allocation":5,"information_confidence":8},"current_profile_expected_stage":"Stage2-Actionable","residual_error_type":"false_positive_without_staged_entry_despite_signed_order","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|003160|Stage2-Watch|2025-02-24","raw_score_total":80}
```

## 5. Score-return alignment

```jsonl
{"row_type":"score_return_alignment","case_id":"C07_L140_CASE01_HANMI_202402_SKHYNIX_TCBONDER_860BN","ticker":"042700","raw_score_total":100,"current_profile_expected_stage":"Stage2-Actionable","observed_label":"positive","MFE_90D_pct":233.67,"MAE_90D_pct":-0.68,"MFE_180D_pct":233.67,"MAE_180D_pct":-0.68,"alignment_comment":"aligned_positive"}
{"row_type":"score_return_alignment","case_id":"C07_L140_CASE02_HANMI_202406_SKHYNIX_TCBONDER_1499BN_LATE","ticker":"042700","raw_score_total":90,"current_profile_expected_stage":"Stage2-Actionable","observed_label":"counterexample","MFE_90D_pct":22.63,"MAE_90D_pct":-42.94,"MFE_180D_pct":22.63,"MAE_180D_pct":-56.62,"alignment_comment":"needs_stage_guard_or_staged_entry"}
{"row_type":"score_return_alignment","case_id":"C07_L140_CASE03_STI_202308_HBM_REFLOW_ORDER","ticker":"039440","raw_score_total":98,"current_profile_expected_stage":"Stage2-Watch","observed_label":"positive","MFE_90D_pct":51.0,"MAE_90D_pct":-4.22,"MFE_180D_pct":73.69,"MAE_180D_pct":-4.22,"alignment_comment":"aligned_positive"}
{"row_type":"score_return_alignment","case_id":"C07_L140_CASE04_STI_202405_HBM_REFLOW_MARGIN_LATE","ticker":"039440","raw_score_total":81,"current_profile_expected_stage":"Stage2-Actionable","observed_label":"counterexample","MFE_90D_pct":23.28,"MAE_90D_pct":-45.53,"MFE_180D_pct":23.28,"MAE_180D_pct":-60.12,"alignment_comment":"needs_stage_guard_or_staged_entry"}
{"row_type":"score_return_alignment","case_id":"C07_L140_CASE05_PSKH_202405_MICRON_REFLOW_SUPPLY","ticker":"031980","raw_score_total":95,"current_profile_expected_stage":"Stage2-Actionable","observed_label":"positive_with_4b_overlay","MFE_90D_pct":55.37,"MAE_90D_pct":-34.24,"MFE_180D_pct":55.37,"MAE_180D_pct":-49.54,"alignment_comment":"needs_stage_guard_or_staged_entry"}
{"row_type":"score_return_alignment","case_id":"C07_L140_CASE06_IMT_202404_MICRON_SMALL_HBM_CLEANING_ORDER","ticker":"451220","raw_score_total":66,"current_profile_expected_stage":"Stage2-Actionable","observed_label":"counterexample","MFE_90D_pct":25.94,"MAE_90D_pct":-62.54,"MFE_180D_pct":25.94,"MAE_180D_pct":-69.53,"alignment_comment":"needs_stage_guard_or_staged_entry"}
{"row_type":"score_return_alignment","case_id":"C07_L140_CASE07_ZEUS_202405_HBM_CLEANING_ORDER_ESTIMATE","ticker":"079370","raw_score_total":60,"current_profile_expected_stage":"Stage2-Actionable","observed_label":"counterexample","MFE_90D_pct":2.84,"MAE_90D_pct":-44.77,"MFE_180D_pct":2.84,"MAE_180D_pct":-46.29,"alignment_comment":"needs_stage_guard_or_staged_entry"}
{"row_type":"score_return_alignment","case_id":"C07_L140_CASE08_DI_202502_SKHYNIX_HBM_DDR5_TESTER_ORDER","ticker":"003160","raw_score_total":80,"current_profile_expected_stage":"Stage2-Actionable","observed_label":"counterexample_with_late_recovery","MFE_90D_pct":7.32,"MAE_90D_pct":-33.72,"MFE_180D_pct":69.51,"MAE_180D_pct":-33.72,"alignment_comment":"needs_stage_guard_or_staged_entry"}
```

## 6. Current calibrated profile stress test

Current calibrated profile proxy는 price-only blowoff block과 Stage2 evidence bonus를 이미 갖고 있다고 가정한다. 그런데 C07에서는 signed order 자체가 너무 강한 evidence로 작동할 수 있다. 한미반도체 2024-02-05와 에스티아이 2023-08-07은 order-backed early phase였기 때문에 Stage2-Actionable이 맞았다. 반대로 한미반도체 2024-06-10, 에스티아이 2024-05-22, 디아이 2025-02-24는 signed/order narrative가 있어도 entry timing이 늦거나 MAE가 커서 staged-entry 또는 local 4B-watch가 먼저 와야 한다.

아이엠티와 제우스는 더 노골적이다. 작은 공급계약, 수주 추정, HBM 세정장비 vocabulary는 C07로 들어오지만, contract size·named customer conversion·delivery cadence·margin bridge가 약하면 Stage2-Actionable이 아니라 Stage2-Watch에 머물러야 한다.

## 7. Shadow rule candidate

```json
{
  "row_type": "shadow_weight_rule_candidate",
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "rule_id": "C07_ORDER_SIZE_TIMING_AND_STAGED_ENTRY_MAE_GATE_V2",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "positive_gate": [
    "named_customer_confirmed",
    "contract_amount_or_repeat_order_confirmed",
    "delivery_or_revenue_recognition_window_known",
    "HBM_capacity_expansion_or_customer_CAPA_bridge_confirmed",
    "margin_or_revision_bridge_present"
  ],
  "watch_or_4b_guard": [
    "late_headline_after_large_relative_strength_run",
    "D30_MFE_exhausted_before_D90_or_D180_follow_through",
    "contract_size_small_relative_to_revenue_or_market_cap",
    "estimate_or_qualification_only_without_signed_order",
    "MAE90_below_minus_30_or_MAE180_below_minus_35"
  ],
  "do_not_green_unlock": true,
  "suggested_effect": "Stage2-Actionable requires order quality plus timing bridge; late mega-order and small/estimate-only HBM equipment stories remain Stage2-Watch or local 4B-watch."
}
```

## 8. Aggregate / residual contribution

```json
{
  "row_type": "aggregate_summary",
  "research_file": "e2r_stock_web_v12_residual_round_R2_loop_140_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md",
  "selected_round": "R2",
  "selected_loop": 140,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "usable_trigger_row_count": 8,
  "representative_trigger_count": 8,
  "unique_symbol_count": 6,
  "positive_case_count": 3,
  "counterexample_count": 5,
  "stage4b_watch_or_overlay_count": 6,
  "current_profile_error_count": 7,
  "coverage_before_index_baseline": "18",
  "coverage_after_index_baseline_if_accepted": "26",
  "coverage_after_session_aware_if_accepted": "about_31",
  "residual_contribution": "C07 second pass separates early named-customer order from late mega-order, small order, estimate-only HBM equipment stories, and adds staged-entry MAE guard."
}
```

## 9. Novelty / dedupe check

- Hard duplicate key = canonical_archetype_id + symbol + trigger_type + entry_date.
- This loop avoids loop 130 symbols 232140, 089030, 092870.
- Same canonical reuse is intentional because C07 remains under 30 rows in the No-Repeat Index.
- Hanmi/042700 has two rows, but entry dates and trigger types differ: early signed-order positive vs late mega-order 4B-watch.
- Zeus/079370 has 2024 corporate-action candidates before the selected 2024-05-23 entry window; entry~D180 overlap is false.

## 10. Evidence URL ledger

- C07_L140_CASE01_HANMI_202402_SKHYNIX_TCBONDER_860BN — https://www.etnews.com/20240202000111
- C07_L140_CASE02_HANMI_202406_SKHYNIX_TCBONDER_1499BN_LATE — https://www.yna.co.kr/view/AKR20240607063600003
- C07_L140_CASE03_STI_202308_HBM_REFLOW_ORDER — https://www.thelec.kr/news/articleView.html?idxno=22391
- C07_L140_CASE04_STI_202405_HBM_REFLOW_MARGIN_LATE — https://www.dailyinvest.kr/news/articleView.html?idxno=58804
- C07_L140_CASE05_PSKH_202405_MICRON_REFLOW_SUPPLY — https://www.thelec.kr/news/articleView.html?idxno=28196
- C07_L140_CASE06_IMT_202404_MICRON_SMALL_HBM_CLEANING_ORDER — https://www.hankyung.com/article/202404294914L
- C07_L140_CASE07_ZEUS_202405_HBM_CLEANING_ORDER_ESTIMATE — https://www.dailyinvest.kr/news/articleView.html?idxno=58834
- C07_L140_CASE08_DI_202502_SKHYNIX_HBM_DDR5_TESTER_ORDER — https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2025/02/20/250221_DI_Comment.pdf

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session. In a later coding-agent batch session, ingest this MD as a standard v12 result file. Validate trigger_rows JSONL, enforce required 30/90/180D MFE/MAE fields, dedupe by canonical_archetype_id + ticker + trigger_type + entry_date, and consider the shadow-only rule candidate C07_ORDER_SIZE_TIMING_AND_STAGED_ENTRY_MAE_GATE_V2. Do not loosen Stage3-Green. Keep production scoring changes gated by batch validation and promotion decisions only.
```

## 12. Next research state

```text
completed_round = R2
completed_loop = 140
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING|C01_ORDER_BACKLOG_MARGIN_BRIDGE|C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF|C14_EV_DEMAND_SLOWDOWN_4B_4C|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

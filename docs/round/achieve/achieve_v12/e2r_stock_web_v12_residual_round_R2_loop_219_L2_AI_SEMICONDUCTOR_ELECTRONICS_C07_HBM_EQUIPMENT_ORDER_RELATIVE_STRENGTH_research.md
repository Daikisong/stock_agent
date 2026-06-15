# E2R Stock-Web v12 Residual Research — R2 / L2 / C07 HBM Equipment Order Relative Strength / loop 219

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
completed_loop: 219
selected_round: R2
selected_loop: 219
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: C07_QUALIFICATION_TO_ORDER_REVENUE_CONVERSION_AND_PROXY_GUARD_V3
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 in original index; session-aware quality-repair after C06 loop218
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
new_independent_case_count: 8
usable_trigger_row_count: 8
representative_trigger_count: 8
positive_case_count: 4
counterexample_count: 4
stage4b_watch_or_overlay_count: 5
current_profile_error_count: 6
index_baseline_coverage_before: C07 rows 18
index_baseline_coverage_after_if_accepted: C07 rows 26
session_aware_note: new C07 pass after loops 130/140; no repeated C07 exact dedupe key
do_not_propose_new_weight_delta: false
canonical_archetype_rule_candidate: C07_QUALIFICATION_TO_ORDER_REVENUE_CONVERSION_AND_PROXY_GUARD_V3
loop_contribution_label: canonical_archetype_rule_candidate
```

## 1. Selection rationale

No-Repeat Index 원본 기준 C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH는 Priority 0 / 18 rows / need to 30 = 12 / need to 50 = 32로 남아 있다. 이 세션에서는 이미 C07 loop 130과 loop 140에서 와이씨·테크윙·엑시콘·한미반도체·에스티아이·PSK홀딩스·아이엠티·제우스·디아이를 다뤘으므로, 이번 loop 219는 같은 canonical 안에서 **qualification-to-order ladder**, **test handler/HBM inspection boundary**, **source-proxy rumor**, **late entry high-MAE guard**를 새로 압축한다.

Round는 C07에서 파생되어 R2/L2로 고정했다. R1~R13 순환은 사용하지 않았다. 이번 질문은 단순하다. HBM 장비라는 단어가 보이면 Stage2-Actionable을 열어도 되는가, 아니면 고객·계약·납기·매출인식·마진 다리가 붙기 전에는 Stage2-Watch나 local 4B로 식혀야 하는가? 장비주는 불씨보다 산소가 중요하다. 불씨는 기술이고, 산소는 주문과 매출이다.

## 2. Stock-Web validation

- primary_price_source: Songdaiki/stock-web
- price_basis: tradable_raw
- price_adjustment_status: raw_unadjusted_marcap
- stock_web_manifest_max_date: 2026-02-20
- entry_price rule: entry_date close `c`
- MFE/MAE rule: entry row 포함 이후 30/90/180 tradable rows의 max high와 min low를 entry price와 비교
- 180D forward window: all trigger rows usable
- corporate action contamination: no selected entry~D180 window marked contaminated in this research pass

| ticker | profile path | price shard | corporate action note |
|---|---|---|---|
| 025560 | atlas/symbol_profiles/025/025560.json | atlas/ohlcv_tradable_by_symbol_year/025/025560/YYYY.csv | clean_180D_window_assumed_from_profile_check |
| 089030 | atlas/symbol_profiles/089/089030.json | atlas/ohlcv_tradable_by_symbol_year/089/089030/YYYY.csv | clean_180D_window_assumed_from_profile_check |
| 168360 | atlas/symbol_profiles/168/168360.json | atlas/ohlcv_tradable_by_symbol_year/168/168360/YYYY.csv | clean_180D_window_assumed_from_profile_check |
| 322310 | atlas/symbol_profiles/322/322310.json | atlas/ohlcv_tradable_by_symbol_year/322/322310/YYYY.csv | clean_180D_window_assumed_from_profile_check |
| 417840 | atlas/symbol_profiles/417/417840.json | atlas/ohlcv_tradable_by_symbol_year/417/417840/YYYY.csv | clean_180D_window_assumed_from_profile_check |

## 3. Case table

| case | ticker | trigger | entry | MFE90 | MAE90 | MFE180 | MAE180 | verdict | residual |
|---|---:|---|---:|---:|---:|---:|---:|---|---|
| C07_L219_CASE01_TECHWING_202401_HBM_HANDLER_DEV_DONE | 089030 | Stage2 | 2024-01-22 / 17760 | 145.5 | -7.66 | 298.65 | -7.66 | positive | current_profile_too_late_if_waits_for_signed_order_only |
| C07_L219_CASE02_PEMTRON_202412_HBM_QUAL_TEST | 168360 | Stage2-Watch | 2024-12-24 / 6900 | 96.38 | -16.38 | 119.86 | -25.22 | positive_with_staged_entry | current_profile_missed_structural_if_qualification_ladder_disallowed |
| C07_L219_CASE03_PEMTRON_202502_HBM_REPORT | 168360 | Stage2-Watch | 2025-02-26 / 7640 | 98.56 | -12.04 | 103.8 | -29.19 | positive_with_4b_overlay | requires_qualification_to_order_transition_not_auto_actionable |
| C07_L219_CASE04_MIRAE_202405_HANDLER_DEV | 025560 | Stage2-Watch | 2024-05-27 / 2180 | 48.17 | -16.97 | 61.47 | -33.49 | watch_positive_not_actionable | handler_development_has_MFE_but_order_bridge_missing |
| C07_L219_CASE05_MIRAE_202406_SUPPLY_COMMITTEE_RUMOR | 025560 | Stage4B-Watch | 2024-06-27 / 2440 | 21.31 | -38.52 | 21.31 | -52.05 | counterexample | supply_committee_rumor_without_PO_or_revenue_bridge_false_positive |
| C07_L219_CASE06_MIRAE_202505_ALL_IN_ONE_CARRIER | 025560 | Stage2-Watch | 2025-05-08 / 2920 | 63.36 | -18.15 | 146.23 | -22.26 | delayed_positive | technology_patent_pre_order_can_be_watch_but_not_actionable_until_order |
| C07_L219_CASE07_AUROS_202406_SAMSUNG_HBM_TEST_EQUIP | 322310 | Stage4B-Watch | 2024-06-17 / 24600 | 16.26 | -43.9 | 16.26 | -55.69 | counterexample | small_order_or_metrology_vocabulary_not_enough_after_prior_blowoff |
| C07_L219_CASE08_JUSTEM_202411_JFS_IDM_SUPPLY | 417840 | Stage2-Watch | 2024-11-27 / 7810 | 42.89 | -28.17 | 78.23 | -39.31 | positive_with_high_mae_guard | IDM_supply_quality_visible_but_not_HBM_order_specific |

## 4. Trigger rows JSONL

```jsonl
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_219_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":219,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"CUBE_PROBER_DEVELOPMENT_COMPLETION_PRE_ORDER_ROUTE","case_id":"C07_L219_CASE01_TECHWING_202401_HBM_HANDLER_DEV_DONE","ticker":"089030","company_name":"테크윙","trigger_type":"Stage2","observed_label":"positive","evidence_date":"2024-01-19","entry_date":"2024-01-22","entry_price":17760.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":31.76,"MAE_30D_pct":-7.66,"MFE_90D_pct":145.5,"MAE_90D_pct":-7.66,"MFE_180D_pct":298.65,"MAE_180D_pct":-7.66,"peak_30D_date":"2024-02-27","trough_30D_date":"2024-01-31","peak_90D_date":"2024-04-12","trough_90D_date":"2024-01-31","peak_180D_date":"2024-07-11","trough_180D_date":"2024-01-31","evidence_summary":"HBM 전수검사용 Cube Prober 개발 완료·품질 테스트·3Q 출시 계획. 아직 signed order 전이지만 C07에서는 demo-to-volume route가 너무 늦게 인식되면 구조적 MFE를 놓친다.","evidence_url":"https://www.newspim.com/news/view/20240119000147","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":16,"earnings_visibility":17,"bottleneck_pricing":19,"market_mispricing":15,"valuation_rerating":12,"capital_allocation":4,"information_confidence":6},"current_profile_expected_stage":"Stage2-Watch","residual_error_type":"current_profile_too_late_if_waits_for_signed_order_only","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|089030|Stage2|2024-01-22","same_entry_group_id":"C07_L219|089030|2024-01-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","raw_score_total":89}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_219_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":219,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_INSPECTION_QUALIFICATION_TEST_PRE_ORDER_ROUTE","case_id":"C07_L219_CASE02_PEMTRON_202412_HBM_QUAL_TEST","ticker":"168360","company_name":"펨트론","trigger_type":"Stage2-Watch","observed_label":"positive_with_staged_entry","evidence_date":"2024-12-23","entry_date":"2024-12-24","entry_price":6900.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/168/168360/2024.csv","profile_path":"atlas/symbol_profiles/168/168360.json","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":24.78,"MAE_30D_pct":-16.38,"MFE_90D_pct":96.38,"MAE_90D_pct":-16.38,"MFE_180D_pct":119.86,"MAE_180D_pct":-25.22,"peak_30D_date":"2025-01-16","trough_30D_date":"2025-01-03","peak_90D_date":"2025-04-04","trough_90D_date":"2025-01-03","peak_180D_date":"2025-06-27","trough_180D_date":"2025-01-03","evidence_summary":"HBM용 검사장비 퀄 테스트가 진행 중이라는 evidence. signed order 전이라 Green은 금지지만, 8800WI-HBM 장비가 고객 검증 단계로 들어간 것은 Stage2-Watch를 열 수 있었다.","evidence_url":"https://www.dailyinvest.kr/news/articleView.html?idxno=62546","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":14,"earnings_visibility":15,"bottleneck_pricing":18,"market_mispricing":14,"valuation_rerating":10,"capital_allocation":4,"information_confidence":7},"current_profile_expected_stage":"Stage2-Watch","residual_error_type":"current_profile_missed_structural_if_qualification_ladder_disallowed","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|168360|Stage2-Watch|2024-12-24","same_entry_group_id":"C07_L219|168360|2024-12-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","raw_score_total":82}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_219_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":219,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_8800WI_QUALIFICATION_AND_REVENUE_OPTIONALITY","case_id":"C07_L219_CASE03_PEMTRON_202502_HBM_REPORT","ticker":"168360","company_name":"펨트론","trigger_type":"Stage2-Watch","observed_label":"positive_with_4b_overlay","evidence_date":"2025-02-26","entry_date":"2025-02-26","entry_price":7640.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/168/168360/2025.csv","profile_path":"atlas/symbol_profiles/168/168360.json","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":43.59,"MAE_30D_pct":-8.64,"MFE_90D_pct":98.56,"MAE_90D_pct":-12.04,"MFE_180D_pct":103.8,"MAE_180D_pct":-29.19,"peak_30D_date":"2025-03-28","trough_30D_date":"2025-03-05","peak_90D_date":"2025-06-27","trough_90D_date":"2025-03-05","peak_180D_date":"2025-07-15","trough_180D_date":"2025-08-06","evidence_summary":"하나증권은 8800WI-HBM 장비가 국내 IDM 대상으로 퀄 테스트 중이고, 통과 시 기술 우위와 매출 기여가 가능하다고 설명했다. 가격경로는 좋았지만 D180 MAE가 커서 clean Actionable보다 staged-entry가 맞다.","evidence_url":"https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2025/02/25/250226_Pemtron_F.pdf","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":16,"earnings_visibility":16,"bottleneck_pricing":19,"market_mispricing":13,"valuation_rerating":9,"capital_allocation":4,"information_confidence":8},"current_profile_expected_stage":"Stage2-Watch","residual_error_type":"requires_qualification_to_order_transition_not_auto_actionable","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|168360|Stage2-Watch|2025-02-26","same_entry_group_id":"C07_L219|168360|2025-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","raw_score_total":85}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_219_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":219,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"TEST_HANDLER_DEVELOPMENT_WITHOUT_HBM_ORDER","case_id":"C07_L219_CASE04_MIRAE_202405_HANDLER_DEV","ticker":"025560","company_name":"미래산업","trigger_type":"Stage2-Watch","observed_label":"watch_positive_not_actionable","evidence_date":"2024-05-24","entry_date":"2024-05-27","entry_price":2180.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/025/025560/2024.csv","profile_path":"atlas/symbol_profiles/025/025560.json","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":22.94,"MAE_30D_pct":-8.72,"MFE_90D_pct":48.17,"MAE_90D_pct":-16.97,"MFE_180D_pct":61.47,"MAE_180D_pct":-33.49,"peak_30D_date":"2024-06-26","trough_30D_date":"2024-06-03","peak_90D_date":"2024-07-11","trough_90D_date":"2024-08-05","peak_180D_date":"2024-10-24","trough_180D_date":"2024-12-09","evidence_summary":"테스트핸들러 장비 개발과 흑자전환 evidence는 있었지만, HBM-specific named customer/order bridge는 없었다. C07에서는 Stage2-Watch까지는 가능하지만 Actionable은 과하다.","evidence_url":"https://www.topdaily.kr/articles/97502","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":11,"earnings_visibility":12,"bottleneck_pricing":13,"market_mispricing":14,"valuation_rerating":9,"capital_allocation":3,"information_confidence":6},"current_profile_expected_stage":"Stage2-Watch","residual_error_type":"handler_development_has_MFE_but_order_bridge_missing","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|025560|Stage2-Watch|2024-05-27","same_entry_group_id":"C07_L219|025560|2024-05-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","raw_score_total":68}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_219_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":219,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"SUPPLY_COMMITTEE_RUMOR_NOT_SIGNED_ORDER","case_id":"C07_L219_CASE05_MIRAE_202406_SUPPLY_COMMITTEE_RUMOR","ticker":"025560","company_name":"미래산업","trigger_type":"Stage4B-Watch","observed_label":"counterexample","evidence_date":"2024-06-27","entry_date":"2024-06-27","entry_price":2440.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/025/025560/2024.csv","profile_path":"atlas/symbol_profiles/025/025560.json","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":13.11,"MAE_30D_pct":-18.03,"MFE_90D_pct":21.31,"MAE_90D_pct":-38.52,"MFE_180D_pct":21.31,"MAE_180D_pct":-52.05,"peak_30D_date":"2024-07-03","trough_30D_date":"2024-07-31","peak_90D_date":"2024-07-11","trough_90D_date":"2024-09-09","peak_180D_date":"2024-07-11","trough_180D_date":"2024-12-20","evidence_summary":"삼성전자·SK하이닉스 후공정 장비 공급 논의 보도는 상대강도를 만들었지만, issuer-level PO·장비명·납기·마진 bridge가 없어 D90/D180 MAE가 크게 열렸다.","evidence_url":"https://www.thebigdata.co.kr/view.php?ud=202406270535522259cd1e7f0bdf_23","source_proxy_only":true,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":8,"earnings_visibility":8,"bottleneck_pricing":12,"market_mispricing":9,"valuation_rerating":4,"capital_allocation":2,"information_confidence":4},"current_profile_expected_stage":"Stage2-Watch","residual_error_type":"supply_committee_rumor_without_PO_or_revenue_bridge_false_positive","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|025560|Stage4B-Watch|2024-06-27","same_entry_group_id":"C07_L219|025560|2024-06-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","raw_score_total":47}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_219_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":219,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_ALL_IN_ONE_CARRIER_PATENT_PRE_ORDER_ROUTE","case_id":"C07_L219_CASE06_MIRAE_202505_ALL_IN_ONE_CARRIER","ticker":"025560","company_name":"미래산업","trigger_type":"Stage2-Watch","observed_label":"delayed_positive","evidence_date":"2025-05-07","entry_date":"2025-05-08","entry_price":2920.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/025/025560/2025.csv","profile_path":"atlas/symbol_profiles/025/025560.json","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":26.03,"MAE_30D_pct":-11.99,"MFE_90D_pct":63.36,"MAE_90D_pct":-18.15,"MFE_180D_pct":146.23,"MAE_180D_pct":-22.26,"peak_30D_date":"2025-06-10","trough_30D_date":"2025-05-19","peak_90D_date":"2025-08-06","trough_90D_date":"2025-05-19","peak_180D_date":"2025-12-05","trough_180D_date":"2025-05-19","evidence_summary":"HBM 테스트 효율을 높이는 올인원 캐리어와 신규 4세대 핸들러 개발 evidence. 기술 route는 살아 있었지만 계약·수주·매출 인식이 없어 Stage2-Watch가 맞고, 이후 가격경로가 열리면 staged-entry로 평가한다.","evidence_url":"https://www.thevaluenews.co.kr/news/190214","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":13,"earnings_visibility":13,"bottleneck_pricing":16,"market_mispricing":13,"valuation_rerating":8,"capital_allocation":3,"information_confidence":6},"current_profile_expected_stage":"Stage2-Watch","residual_error_type":"technology_patent_pre_order_can_be_watch_but_not_actionable_until_order","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|025560|Stage2-Watch|2025-05-08","same_entry_group_id":"C07_L219|025560|2025-05-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","raw_score_total":72}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_219_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":219,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"SMALL_HBM_TEST_EQUIPMENT_ORDER_AFTER_PRIOR_BLOWOFF","case_id":"C07_L219_CASE07_AUROS_202406_SAMSUNG_HBM_TEST_EQUIP","ticker":"322310","company_name":"오로스테크놀로지","trigger_type":"Stage4B-Watch","observed_label":"counterexample","evidence_date":"2024-06-14","entry_date":"2024-06-17","entry_price":24600.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv","profile_path":"atlas/symbol_profiles/322/322310.json","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":16.26,"MAE_30D_pct":-17.89,"MFE_90D_pct":16.26,"MAE_90D_pct":-43.9,"MFE_180D_pct":16.26,"MAE_180D_pct":-55.69,"peak_30D_date":"2024-06-24","trough_30D_date":"2024-07-31","peak_90D_date":"2024-06-24","trough_90D_date":"2024-09-09","peak_180D_date":"2024-06-24","trough_180D_date":"2024-12-09","evidence_summary":"삼성전자향 HBM 테스트 장비 48억원 공급 공시가 있었다는 보도. signed order 성격은 있지만 규모와 revenue bridge가 작고 이미 C09/C07 테마가 선반영되어 high-MAE counterexample이 됐다.","evidence_url":"https://v.daum.net/v/20240614060125384?f=p","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":10,"earnings_visibility":11,"bottleneck_pricing":14,"market_mispricing":8,"valuation_rerating":3,"capital_allocation":3,"information_confidence":7},"current_profile_expected_stage":"Stage2-Watch","residual_error_type":"small_order_or_metrology_vocabulary_not_enough_after_prior_blowoff","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|322310|Stage4B-Watch|2024-06-17","same_entry_group_id":"C07_L219|322310|2024-06-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","raw_score_total":56}
{"row_type":"trigger","research_file":"e2r_stock_web_v12_residual_round_R2_loop_219_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":219,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"FOUP_HUMIDITY_CONTROL_IDM_SUPPLY_BOUNDARY","case_id":"C07_L219_CASE08_JUSTEM_202411_JFS_IDM_SUPPLY","ticker":"417840","company_name":"저스템","trigger_type":"Stage2-Watch","observed_label":"positive_with_high_mae_guard","evidence_date":"2024-11-26","entry_date":"2024-11-27","entry_price":7810.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard":"atlas/ohlcv_tradable_by_symbol_year/417/417840/2024.csv","profile_path":"atlas/symbol_profiles/417/417840.json","corporate_action_overlap_180D":false,"calibration_usable":true,"MFE_30D_pct":28.55,"MAE_30D_pct":-13.7,"MFE_90D_pct":42.89,"MAE_90D_pct":-28.17,"MFE_180D_pct":78.23,"MAE_180D_pct":-39.31,"peak_30D_date":"2024-12-19","trough_30D_date":"2024-12-09","peak_90D_date":"2025-02-12","trough_90D_date":"2025-01-03","peak_180D_date":"2025-04-21","trough_180D_date":"2025-01-03","evidence_summary":"JFS/습도제어 장비는 FOUP 내부 습도를 낮춰 수율을 높이는 HBM-adjacent bottleneck 장비다. 고객/공급 품질은 있지만 HBM-specific order가 아니어서 Actionable보다 Watch + high-MAE guard가 맞다.","evidence_url":"https://www.justem.co.kr/main/sub02_05_view.php?bo_uid=370&ps_page=1","source_proxy_only":false,"evidence_url_pending":false,"raw_component_score_breakdown":{"eps_fcf_explosion":12,"earnings_visibility":13,"bottleneck_pricing":15,"market_mispricing":12,"valuation_rerating":8,"capital_allocation":3,"information_confidence":6},"current_profile_expected_stage":"Stage2-Watch","residual_error_type":"IDM_supply_quality_visible_but_not_HBM_order_specific","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|417840|Stage2-Watch|2024-11-27","same_entry_group_id":"C07_L219|417840|2024-11-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","raw_score_total":69}
```

## 5. Score-return alignment

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_L219_CASE01_TECHWING_202401_HBM_HANDLER_DEV_DONE","ticker":"089030","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_score_total_before":89,"stage_label_before":"Stage2-Watch","raw_score_total_after_shadow_rule":94,"stage_label_after_shadow_rule":"Stage2-Actionable","changed_components":["qualification_ladder_gate","order_revenue_conversion_required","late_entry_high_mae_guard"],"MFE_90D_pct":145.5,"MAE_90D_pct":-7.66,"MFE_180D_pct":298.65,"MAE_180D_pct":-7.66,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late_if_waits_for_signed_order_only"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_L219_CASE02_PEMTRON_202412_HBM_QUAL_TEST","ticker":"168360","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_score_total_before":82,"stage_label_before":"Stage2-Watch","raw_score_total_after_shadow_rule":82,"stage_label_after_shadow_rule":"Stage2-Watch","changed_components":["qualification_ladder_gate","order_revenue_conversion_required","late_entry_high_mae_guard"],"MFE_90D_pct":96.38,"MAE_90D_pct":-16.38,"MFE_180D_pct":119.86,"MAE_180D_pct":-25.22,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural_if_qualification_ladder_disallowed"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_L219_CASE03_PEMTRON_202502_HBM_REPORT","ticker":"168360","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_score_total_before":85,"stage_label_before":"Stage2-Watch","raw_score_total_after_shadow_rule":85,"stage_label_after_shadow_rule":"Stage2-Watch","changed_components":["qualification_ladder_gate","order_revenue_conversion_required","late_entry_high_mae_guard"],"MFE_90D_pct":98.56,"MAE_90D_pct":-12.04,"MFE_180D_pct":103.8,"MAE_180D_pct":-29.19,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"requires_qualification_to_order_transition_not_auto_actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_L219_CASE04_MIRAE_202405_HANDLER_DEV","ticker":"025560","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_score_total_before":68,"stage_label_before":"Stage2-Watch","raw_score_total_after_shadow_rule":68,"stage_label_after_shadow_rule":"Stage2-Watch","changed_components":["qualification_ladder_gate","order_revenue_conversion_required","late_entry_high_mae_guard"],"MFE_90D_pct":48.17,"MAE_90D_pct":-16.97,"MFE_180D_pct":61.47,"MAE_180D_pct":-33.49,"score_return_alignment_label":"bridge_gap_or_late_entry_false_positive","current_profile_verdict":"handler_development_has_MFE_but_order_bridge_missing"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_L219_CASE05_MIRAE_202406_SUPPLY_COMMITTEE_RUMOR","ticker":"025560","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_score_total_before":47,"stage_label_before":"Stage2-Watch","raw_score_total_after_shadow_rule":35,"stage_label_after_shadow_rule":"Stage1","changed_components":["qualification_ladder_gate","order_revenue_conversion_required","late_entry_high_mae_guard"],"MFE_90D_pct":21.31,"MAE_90D_pct":-38.52,"MFE_180D_pct":21.31,"MAE_180D_pct":-52.05,"score_return_alignment_label":"bridge_gap_or_late_entry_false_positive","current_profile_verdict":"supply_committee_rumor_without_PO_or_revenue_bridge_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_L219_CASE06_MIRAE_202505_ALL_IN_ONE_CARRIER","ticker":"025560","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_score_total_before":72,"stage_label_before":"Stage2-Watch","raw_score_total_after_shadow_rule":77,"stage_label_after_shadow_rule":"Stage2-Actionable","changed_components":["qualification_ladder_gate","order_revenue_conversion_required","late_entry_high_mae_guard"],"MFE_90D_pct":63.36,"MAE_90D_pct":-18.15,"MFE_180D_pct":146.23,"MAE_180D_pct":-22.26,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"technology_patent_pre_order_can_be_watch_but_not_actionable_until_order"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_L219_CASE07_AUROS_202406_SAMSUNG_HBM_TEST_EQUIP","ticker":"322310","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_score_total_before":56,"stage_label_before":"Stage2-Watch","raw_score_total_after_shadow_rule":44,"stage_label_after_shadow_rule":"Stage1","changed_components":["qualification_ladder_gate","order_revenue_conversion_required","late_entry_high_mae_guard"],"MFE_90D_pct":16.26,"MAE_90D_pct":-43.9,"MFE_180D_pct":16.26,"MAE_180D_pct":-55.69,"score_return_alignment_label":"bridge_gap_or_late_entry_false_positive","current_profile_verdict":"small_order_or_metrology_vocabulary_not_enough_after_prior_blowoff"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C07_L219_CASE08_JUSTEM_202411_JFS_IDM_SUPPLY","ticker":"417840","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","raw_score_total_before":69,"stage_label_before":"Stage2-Watch","raw_score_total_after_shadow_rule":69,"stage_label_after_shadow_rule":"Stage2-Watch","changed_components":["qualification_ladder_gate","order_revenue_conversion_required","late_entry_high_mae_guard"],"MFE_90D_pct":42.89,"MAE_90D_pct":-28.17,"MFE_180D_pct":78.23,"MAE_180D_pct":-39.31,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"IDM_supply_quality_visible_but_not_HBM_order_specific"}
```

## 6. Case notes

### C07_L219_CASE01_TECHWING_202401_HBM_HANDLER_DEV_DONE — 테크윙 / 089030

HBM 전수검사용 Cube Prober 개발 완료·품질 테스트·3Q 출시 계획. 아직 signed order 전이지만 C07에서는 demo-to-volume route가 너무 늦게 인식되면 구조적 MFE를 놓친다.

- evidence_url: https://www.newspim.com/news/view/20240119000147
- price verdict: MFE90 145.5%, MAE90 -7.66%, MFE180 298.65%, MAE180 -7.66%
- E2R residual: current_profile_too_late_if_waits_for_signed_order_only

### C07_L219_CASE02_PEMTRON_202412_HBM_QUAL_TEST — 펨트론 / 168360

HBM용 검사장비 퀄 테스트가 진행 중이라는 evidence. signed order 전이라 Green은 금지지만, 8800WI-HBM 장비가 고객 검증 단계로 들어간 것은 Stage2-Watch를 열 수 있었다.

- evidence_url: https://www.dailyinvest.kr/news/articleView.html?idxno=62546
- price verdict: MFE90 96.38%, MAE90 -16.38%, MFE180 119.86%, MAE180 -25.22%
- E2R residual: current_profile_missed_structural_if_qualification_ladder_disallowed

### C07_L219_CASE03_PEMTRON_202502_HBM_REPORT — 펨트론 / 168360

하나증권은 8800WI-HBM 장비가 국내 IDM 대상으로 퀄 테스트 중이고, 통과 시 기술 우위와 매출 기여가 가능하다고 설명했다. 가격경로는 좋았지만 D180 MAE가 커서 clean Actionable보다 staged-entry가 맞다.

- evidence_url: https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2025/02/25/250226_Pemtron_F.pdf
- price verdict: MFE90 98.56%, MAE90 -12.04%, MFE180 103.8%, MAE180 -29.19%
- E2R residual: requires_qualification_to_order_transition_not_auto_actionable

### C07_L219_CASE04_MIRAE_202405_HANDLER_DEV — 미래산업 / 025560

테스트핸들러 장비 개발과 흑자전환 evidence는 있었지만, HBM-specific named customer/order bridge는 없었다. C07에서는 Stage2-Watch까지는 가능하지만 Actionable은 과하다.

- evidence_url: https://www.topdaily.kr/articles/97502
- price verdict: MFE90 48.17%, MAE90 -16.97%, MFE180 61.47%, MAE180 -33.49%
- E2R residual: handler_development_has_MFE_but_order_bridge_missing

### C07_L219_CASE05_MIRAE_202406_SUPPLY_COMMITTEE_RUMOR — 미래산업 / 025560

삼성전자·SK하이닉스 후공정 장비 공급 논의 보도는 상대강도를 만들었지만, issuer-level PO·장비명·납기·마진 bridge가 없어 D90/D180 MAE가 크게 열렸다.

- evidence_url: https://www.thebigdata.co.kr/view.php?ud=202406270535522259cd1e7f0bdf_23
- price verdict: MFE90 21.31%, MAE90 -38.52%, MFE180 21.31%, MAE180 -52.05%
- E2R residual: supply_committee_rumor_without_PO_or_revenue_bridge_false_positive

### C07_L219_CASE06_MIRAE_202505_ALL_IN_ONE_CARRIER — 미래산업 / 025560

HBM 테스트 효율을 높이는 올인원 캐리어와 신규 4세대 핸들러 개발 evidence. 기술 route는 살아 있었지만 계약·수주·매출 인식이 없어 Stage2-Watch가 맞고, 이후 가격경로가 열리면 staged-entry로 평가한다.

- evidence_url: https://www.thevaluenews.co.kr/news/190214
- price verdict: MFE90 63.36%, MAE90 -18.15%, MFE180 146.23%, MAE180 -22.26%
- E2R residual: technology_patent_pre_order_can_be_watch_but_not_actionable_until_order

### C07_L219_CASE07_AUROS_202406_SAMSUNG_HBM_TEST_EQUIP — 오로스테크놀로지 / 322310

삼성전자향 HBM 테스트 장비 48억원 공급 공시가 있었다는 보도. signed order 성격은 있지만 규모와 revenue bridge가 작고 이미 C09/C07 테마가 선반영되어 high-MAE counterexample이 됐다.

- evidence_url: https://v.daum.net/v/20240614060125384?f=p
- price verdict: MFE90 16.26%, MAE90 -43.9%, MFE180 16.26%, MAE180 -55.69%
- E2R residual: small_order_or_metrology_vocabulary_not_enough_after_prior_blowoff

### C07_L219_CASE08_JUSTEM_202411_JFS_IDM_SUPPLY — 저스템 / 417840

JFS/습도제어 장비는 FOUP 내부 습도를 낮춰 수율을 높이는 HBM-adjacent bottleneck 장비다. 고객/공급 품질은 있지만 HBM-specific order가 아니어서 Actionable보다 Watch + high-MAE guard가 맞다.

- evidence_url: https://www.justem.co.kr/main/sub02_05_view.php?bo_uid=370&ps_page=1
- price verdict: MFE90 42.89%, MAE90 -28.17%, MFE180 78.23%, MAE180 -39.31%
- E2R residual: IDM_supply_quality_visible_but_not_HBM_order_specific

## 7. Current calibrated profile stress test

Current calibrated profile proxy는 price-only blowoff block과 Stage2 evidence bonus를 이미 갖고 있다고 가정한다. 그런데 C07에서는 signed order 또는 qualification wording 자체가 너무 강한 evidence로 작동할 수 있다. 테크윙 2024-01-22, 펨트론 2024-12/2025-02, 미래산업 2025-05처럼 formal order 전 단계라도 고객 검증·장비 독자성·매출 전환 가능성이 비교적 선명하면 Stage2-Watch를 일찍 허용해야 한다. 반대로 미래산업 2024-06 supply committee rumor, 오로스테크놀로지 small HBM tester order after prior blowoff, 저스템의 HBM-adjacent IDM supply는 C07 vocabulary가 있어도 issuer-level order/revenue/margin bridge가 약하거나 high-MAE가 커서 Stage2-Actionable을 제한해야 한다.

## 8. Shadow rule candidate

```json
{
  "row_type": "shadow_weight_rule_candidate",
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "rule_id": "C07_QUALIFICATION_TO_ORDER_REVENUE_CONVERSION_AND_PROXY_GUARD_V3",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "positive_or_watch_gate": [
    "named_customer_or_IDM_quality_test_confirmed",
    "tool_function_specific_to_HBM_or_memory_back_end",
    "qualification_or_demo_to_volume_route_visible",
    "revenue_recognition_or_delivery_window_plausible",
    "margin_or_revision_bridge_not_contradicted"
  ],
  "actionable_required_bridge": [
    "signed_order_or_PO_or_customer acceptance",
    "contract_amount_or repeat-order cadence",
    "delivery/revenue recognition timing",
    "HBM CAPA/customer production bridge",
    "margin/revision conversion"
  ],
  "watch_or_4b_guard": [
    "supply committee rumor only",
    "patent/product-category exposure without order",
    "small order after prior valuation blowoff",
    "late order after relative strength exhaustion",
    "MAE90 below -25% unless MFE180 above +60% and hard bridge exists"
  ],
  "do_not_green_unlock": true,
  "suggested_effect": "C07 allows early Stage2-Watch for qualification-to-volume route, but Stage2-Actionable requires order/revenue conversion and late-entry/high-MAE guard."
}
```

## 9. Aggregate / residual contribution

```json
{
  "row_type": "aggregate_summary",
  "research_file": "e2r_stock_web_v12_residual_round_R2_loop_219_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md",
  "selected_round": "R2",
  "selected_loop": 219,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "usable_trigger_row_count": 8,
  "representative_trigger_count": 8,
  "unique_symbol_count": 6,
  "positive_case_count": 4,
  "counterexample_count": 4,
  "stage4b_watch_or_overlay_count": 5,
  "current_profile_error_count": 6,
  "coverage_before_index_baseline": "18",
  "coverage_after_index_baseline_if_accepted": "26",
  "residual_contribution": "C07 third-pass quality repair separates qualification-to-order route from source-proxy rumor and late-entry high-MAE HBM equipment stories."
}
```

## 10. Novelty / dedupe check

- Hard duplicate key = canonical_archetype_id + ticker + trigger_type + entry_date.
- This loop does not repeat C07 loop130 exact keys: 232140/2024-04-25, 232140/2024-07-30, 089030/2024-03-14, 089030/2025-01-17, 092870/2024-09-30.
- This loop does not repeat C07 loop140 exact keys: 042700/2024-02-05, 042700/2024-06-10, 039440/2023-08-07, 039440/2024-05-22, 031980/2024-05-31, 451220/2024-04-30, 079370/2024-05-23, 003160/2025-02-24.
- Same ticker reuse is allowed only for a new trigger family and new entry date. Techwing 2024-01-22 is a pre-order development-completion route, not the loop130 2024-03-14 demo note or 2025-01-17 Samsung first-order row.
- C09/C08/C10 boundary rows are included only because the evidence explicitly tests C07 compression limits.

## 11. Evidence URL ledger

- C07_L219_CASE01_TECHWING_202401_HBM_HANDLER_DEV_DONE — https://www.newspim.com/news/view/20240119000147 — HBM 전수검사용 Cube Prober 개발 완료·품질 테스트·3Q 출시 계획. 아직 signed order 전이지만 C07에서는 demo-to-volume route가 너무 늦게 인식되면 구조적 MFE를 놓친다.
- C07_L219_CASE02_PEMTRON_202412_HBM_QUAL_TEST — https://www.dailyinvest.kr/news/articleView.html?idxno=62546 — HBM용 검사장비 퀄 테스트가 진행 중이라는 evidence. signed order 전이라 Green은 금지지만, 8800WI-HBM 장비가 고객 검증 단계로 들어간 것은 Stage2-Watch를 열 수 있었다.
- C07_L219_CASE03_PEMTRON_202502_HBM_REPORT — https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2025/02/25/250226_Pemtron_F.pdf — 하나증권은 8800WI-HBM 장비가 국내 IDM 대상으로 퀄 테스트 중이고, 통과 시 기술 우위와 매출 기여가 가능하다고 설명했다. 가격경로는 좋았지만 D180 MAE가 커서 clean Actionable보다 staged-entry가 맞다.
- C07_L219_CASE04_MIRAE_202405_HANDLER_DEV — https://www.topdaily.kr/articles/97502 — 테스트핸들러 장비 개발과 흑자전환 evidence는 있었지만, HBM-specific named customer/order bridge는 없었다. C07에서는 Stage2-Watch까지는 가능하지만 Actionable은 과하다.
- C07_L219_CASE05_MIRAE_202406_SUPPLY_COMMITTEE_RUMOR — https://www.thebigdata.co.kr/view.php?ud=202406270535522259cd1e7f0bdf_23 — 삼성전자·SK하이닉스 후공정 장비 공급 논의 보도는 상대강도를 만들었지만, issuer-level PO·장비명·납기·마진 bridge가 없어 D90/D180 MAE가 크게 열렸다.
- C07_L219_CASE06_MIRAE_202505_ALL_IN_ONE_CARRIER — https://www.thevaluenews.co.kr/news/190214 — HBM 테스트 효율을 높이는 올인원 캐리어와 신규 4세대 핸들러 개발 evidence. 기술 route는 살아 있었지만 계약·수주·매출 인식이 없어 Stage2-Watch가 맞고, 이후 가격경로가 열리면 staged-entry로 평가한다.
- C07_L219_CASE07_AUROS_202406_SAMSUNG_HBM_TEST_EQUIP — https://v.daum.net/v/20240614060125384?f=p — 삼성전자향 HBM 테스트 장비 48억원 공급 공시가 있었다는 보도. signed order 성격은 있지만 규모와 revenue bridge가 작고 이미 C09/C07 테마가 선반영되어 high-MAE counterexample이 됐다.
- C07_L219_CASE08_JUSTEM_202411_JFS_IDM_SUPPLY — https://www.justem.co.kr/main/sub02_05_view.php?bo_uid=370&ps_page=1 — JFS/습도제어 장비는 FOUP 내부 습도를 낮춰 수율을 높이는 HBM-adjacent bottleneck 장비다. 고객/공급 품질은 있지만 HBM-specific order가 아니어서 Actionable보다 Watch + high-MAE guard가 맞다.

### narrative-only blocked / forward-window note

- PEMTRON_202509_SKHYNIX_8800WI_HBM_ORDER — https://www.thelec.kr/news/articleView.html?idxno=43790 — SK하이닉스향 HBM 검사장비 수주로는 매우 강한 evidence지만, 2025-09-05 trigger는 stock-web manifest max_date 2026-02-20 기준 180 trading-day forward window가 부족하므로 정규 trigger row에서 제외했다.

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session. In a later coding-agent batch session, ingest this MD as a standard v12 result file. Validate all trigger JSONL rows, enforce required 30/90/180D MFE/MAE fields, dedupe by canonical_archetype_id + ticker + trigger_type + entry_date, and consider the shadow-only rule candidate C07_QUALIFICATION_TO_ORDER_REVENUE_CONVERSION_AND_PROXY_GUARD_V3. Do not loosen Stage3-Green. Keep production scoring changes gated by batch validation and promotion decisions only.
```

## 13. Next research state

```text
completed_round = R2
completed_loop = 219
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 in original index; session-aware quality-repair after C06 loop218
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING|C01_ORDER_BACKLOG_MARGIN_BRIDGE|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

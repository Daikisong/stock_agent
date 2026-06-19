# E2R Stock-Web v12 Residual Research — R2/L2/C07 HBM Equipment Order Relative Strength Follow-up

```text
filename = e2r_stock_web_v12_residual_round_R2_loop_127_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
selected_round = R2
selected_loop = 127
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under_30_representative_rows / C07 rows 18 need_to_30 12 before local follow-up
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = HBM_EQUIPMENT_ORDER_CONVERSION_VS_PRODUCT_IDENTITY_AND_LATE_REPEAT_ORDER_PROXY
loop_objective = coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | stage2_actionable_bonus_stress_test | canonical_archetype_compression | source_proxy_replacement
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection and novelty check

The coverage ledger still places `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` in Priority 0. Existing local C07 loops already covered the obvious HBM winners and common proxies such as Hanmi Semiconductor, Techwing, PSK Holdings, YC, DI, STI, Oros Technology, Intekplus, HPSP, NeoSem, LaserCell, KC Tech, Genesem, Femto, Mirae Industry, Protec, and EO Technics. This follow-up therefore avoids repeating the same TC-bonder / Cube Prober / YC tester set and instead tests the boundary between:

- real named-customer HBM or advanced-memory equipment orders,
- late repeat-order confirmation after the first reprice,
- product-identity proxies such as HBM cleaning, environment control, reliability testing, and memory/CXL tester capability.

Hard duplicate key checked: `canonical_archetype_id + symbol + trigger_type + entry_date`.

```text
new_independent_case_count = 7
reused_case_count = 1
same_archetype_new_symbol_count = 6
same_archetype_new_trigger_family_count = 7
new_symbol_count = 6
positive_case_count = 1
counterexample_count = 6
stage4b_overlay_count = 6
current_profile_error_count = 6
```

## 2. Price source validation

Stock-Web manifest fields used:

```text
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

All representative trigger rows below use the entry-date close from the `c` column and 30/90/180 trading-day windows from `Songdaiki/stock-web`. Share count was stable inside the local 180D windows used for aggregate rows. `122640 / 예스티` is kept as narrative-only because the 180D window requires profile-level corporate-action verification before representative aggregate use.

## 3. Evidence and price alignment summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | role |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C07-L127-01 | 110990 | 디아이티 | Stage2-Actionable | 2024-02-01 | 18980 | 33.8 | 0.2 | 70.4 | -11.7 | 70.4 | -31.9 | positive |
| C07-L127-02 | 110990 | 디아이티 | Stage4B | 2024-07-05 | 24300 | 1.9 | -43.6 | 1.9 | -56.0 | 1.9 | -60.1 | counterexample_4b |
| C07-L127-03 | 451220 | 아이엠티 | Stage2 | 2024-04-17 | 23100 | 9.3 | -22.9 | 9.3 | -59.1 | 9.3 | -73.5 | counterexample |
| C07-L127-04 | 089790 | 제이티 | Stage2 | 2024-03-11 | 9830 | 15.6 | -7.8 | 15.6 | -30.7 | 15.6 | -67.3 | counterexample |
| C07-L127-05 | 396470 | 워트 | Stage2 | 2024-08-23 | 10790 | 12.5 | -16.6 | 12.5 | -40.0 | 12.5 | -41.5 | counterexample |
| C07-L127-06 | 405100 | 큐알티 | Stage2 | 2024-05-28 | 22350 | 10.1 | -18.3 | 10.1 | -46.7 | 10.1 | -55.8 | counterexample |
| C07-L127-07 | 086390 | 유니테스트 | Stage2 | 2024-08-09 | 10210 | 7.1 | -18.2 | 12.6 | -26.8 | 48.2 | -26.8 | counterexample_boundary |

### Interpretation

DIT's first 2024 SK Hynix equipment contract is the clean positive control: it had a named customer, contract amount, advanced process equipment route, and fast 90D upside. The later July repeat contract shows the other half of the rule. Once the first rerating has already happened, another order headline may be real but should act as `Stage4B-local` rather than a fresh Stage2-Actionable unlock.

IMT, JT, WOT, QRT, and Unitest mark the boundary. They all have plausible HBM/advanced-memory vocabulary, but the price path punishes the cases where the evidence is not a named HBM equipment order with revenue or margin conversion. In this archetype, vocabulary is the scent of smoke; named customer order and conversion bridge are the fire.

## 4. Machine-readable trigger rows JSONL

```jsonl
{"case_id":"C07-L127-01","symbol":"110990","company_name":"디아이티","trigger_date":"2024-01-31","entry_date":"2024-02-01","entry_price":18980,"trigger_type":"Stage2-Actionable","fine_archetype_id":"LASER_ANNEALING_SKHYNIX_ORDER_CONVERSION","MFE_30D_pct":33.8,"MAE_30D_pct":0.2,"MFE_90D_pct":70.4,"MAE_90D_pct":-11.7,"MFE_180D_pct":70.4,"MAE_180D_pct":-31.9,"peak_date":"2024-04-26","peak_price":32350,"trough_date_180D":"2024-10-18","trough_price_180D":12920,"max_drawdown_after_peak_180D_pct":-60.1,"positive_or_counterexample":"positive","current_profile_verdict":"correct_to_allow_actionable_but_later_order_confirmations_need_4b_overlay","evidence_url":"https://mobile.newsis.com/view_amp.html?ar_id=NISX20240131_0002611571","evidence_summary":"SK하이닉스와 149.4억원 규모 반도체 제조장비 공급계약. 레이저 어닐링 route는 HBM/선단공정 장비 역할로 해석 가능하나 첫 reprice 후에는 4B가 필요하다.","row_type":"trigger","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative_for_aggregate":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C07|110990|2024-02-01","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|110990|Stage2-Actionable|2024-02-01","profile_path":"atlas/symbol_profiles/110/110990.json","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv","source_proxy_only":false,"current_profile_error":false,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"case_id":"C07-L127-02","symbol":"110990","company_name":"디아이티","trigger_date":"2024-07-04","entry_date":"2024-07-05","entry_price":24300,"trigger_type":"Stage4B","fine_archetype_id":"LASER_ANNEALING_REPEAT_ORDER_LATE_CONFIRMATION","MFE_30D_pct":1.9,"MAE_30D_pct":-43.6,"MFE_90D_pct":1.9,"MAE_90D_pct":-56.0,"MFE_180D_pct":1.9,"MAE_180D_pct":-60.1,"peak_date":"2024-07-09","peak_price":24750,"trough_date_180D":"2024-11-29","trough_price_180D":9700,"max_drawdown_after_peak_180D_pct":-60.8,"positive_or_counterexample":"counterexample_4b","current_profile_verdict":"repeat_order_after_first_rerating_should_be_local_4b_not_fresh_actionable","evidence_url":"https://www.dnews.co.kr/uhtml/view.jsp?idxno=202407041301360140228","evidence_summary":"SK하이닉스향 107.6억원 장비 공급계약. 계약 자체는 real order지만, 주가가 앞서 rerating된 뒤 나온 후행 확인 row는 fresh Stage2-Actionable보다 local 4B/profit-lock이 더 맞다.","row_type":"trigger","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative_for_aggregate":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C07|110990|2024-07-05","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|110990|Stage4B|2024-07-05","profile_path":"atlas/symbol_profiles/110/110990.json","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/110/110990/2024.csv","source_proxy_only":true,"current_profile_error":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_late_4B","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"case_id":"C07-L127-03","symbol":"451220","company_name":"아이엠티","trigger_date":"2024-04-16","entry_date":"2024-04-17","entry_price":23100,"trigger_type":"Stage2","fine_archetype_id":"HBM_CO2_CLEANING_MICRON_DELIVERY_BUT_NO_MARGIN_BRIDGE","MFE_30D_pct":9.3,"MAE_30D_pct":-22.9,"MFE_90D_pct":9.3,"MAE_90D_pct":-59.1,"MFE_180D_pct":9.3,"MAE_180D_pct":-73.5,"peak_date":"2024-05-29","peak_price":25250,"trough_date_180D":"2024-12-09","trough_price_180D":6110,"max_drawdown_after_peak_180D_pct":-75.8,"positive_or_counterexample":"counterexample","current_profile_verdict":"delivery_or_qual_language_without_repeat_order_and_margin_bridge_should_not_be_actionable","evidence_url":"https://m.newsprime.co.kr/section_view.html?no=635889","evidence_summary":"Micron HBM cleaning equipment delivery and SK Hynix burn-in socket cleaner development route. The product role is real but the entry behaved like a source-proxy/high-MAE trap.","row_type":"trigger","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative_for_aggregate":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C07|451220|2024-04-17","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|451220|Stage2|2024-04-17","profile_path":"atlas/symbol_profiles/451/451220.json","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/451/451220/2024.csv","source_proxy_only":true,"current_profile_error":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"case_id":"C07-L127-04","symbol":"089790","company_name":"제이티","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":9830,"trigger_type":"Stage2","fine_archetype_id":"HBM_HANDLER_SALES_ATTEMPT_VS_CONFIRMED_ORDER","MFE_30D_pct":15.6,"MAE_30D_pct":-7.8,"MFE_90D_pct":15.6,"MAE_90D_pct":-30.7,"MFE_180D_pct":15.6,"MAE_180D_pct":-67.3,"peak_date":"2024-04-12","peak_price":11360,"trough_date_180D":"2024-12-04","trough_price_180D":3215,"max_drawdown_after_peak_180D_pct":-71.7,"positive_or_counterexample":"counterexample","current_profile_verdict":"sales_attempt_and_memory_tester_identity_must_stay_stage2_watch_until_customer_order","evidence_url":"https://www.theinvest.co.kr/article/765","evidence_summary":"HBM handler sales attempt and burn-in sorter strength were described, but this was not a named HBM order/revenue conversion row.","row_type":"trigger","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative_for_aggregate":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C07|089790|2024-03-11","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|089790|Stage2|2024-03-11","profile_path":"atlas/symbol_profiles/089/089790.json","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089790/2024.csv","source_proxy_only":true,"current_profile_error":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"case_id":"C07-L127-05","symbol":"396470","company_name":"워트","trigger_date":"2024-08-22","entry_date":"2024-08-23","entry_price":10790,"trigger_type":"Stage2","fine_archetype_id":"HBM_ENVIRONMENT_CONTROL_COMPONENT_PROXY","MFE_30D_pct":12.5,"MAE_30D_pct":-16.6,"MFE_90D_pct":12.5,"MAE_90D_pct":-40.0,"MFE_180D_pct":12.5,"MAE_180D_pct":-41.5,"peak_date":"2024-08-30","peak_price":12140,"trough_date_180D":"2025-04-09","trough_price_180D":6310,"max_drawdown_after_peak_180D_pct":-48.0,"positive_or_counterexample":"counterexample","current_profile_verdict":"component_environment_control_proxy_should_not_count_as_C07_order_conversion","evidence_url":"https://alphasquare.co.kr/home/stock-summary?code=396470","evidence_summary":"THC/TCU environmental-control equipment can touch HBM processes, but named HBM order, PO, shipment, and margin bridge were absent at the trigger.","row_type":"trigger","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative_for_aggregate":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C07|396470|2024-08-23","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|396470|Stage2|2024-08-23","profile_path":"atlas/symbol_profiles/396/396470.json","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/396/396470/2024.csv","source_proxy_only":true,"current_profile_error":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"case_id":"C07-L127-06","symbol":"405100","company_name":"큐알티","trigger_date":"2024-05-27","entry_date":"2024-05-28","entry_price":22350,"trigger_type":"Stage2","fine_archetype_id":"HBM_RELIABILITY_TEST_SERVICE_NOT_EQUIPMENT_ORDER","MFE_30D_pct":10.1,"MAE_30D_pct":-18.3,"MFE_90D_pct":10.1,"MAE_90D_pct":-46.7,"MFE_180D_pct":10.1,"MAE_180D_pct":-55.8,"peak_date":"2024-06-13","peak_price":24600,"trough_date_180D":"2024-12-10","trough_price_180D":9880,"max_drawdown_after_peak_180D_pct":-59.8,"positive_or_counterexample":"counterexample","current_profile_verdict":"reliability_testing_service_should_be_stage2_watch_or_C08_boundary_not_C07_actionable","evidence_url":"https://securities.miraeasset.com/bbs/download/2127468.pdf?attachmentId=2127468","evidence_summary":"HBM/AI/recycle keywords and HBM3E reliability testing demand were highlighted, but this is service/test exposure rather than named equipment order conversion.","row_type":"trigger","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative_for_aggregate":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C07|405100|2024-05-28","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|405100|Stage2|2024-05-28","profile_path":"atlas/symbol_profiles/405/405100.json","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/405/405100/2024.csv","source_proxy_only":true,"current_profile_error":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"case_id":"C07-L127-07","symbol":"086390","company_name":"유니테스트","trigger_date":"2024-08-08","entry_date":"2024-08-09","entry_price":10210,"trigger_type":"Stage2","fine_archetype_id":"CXL_MEMORY_TESTER_CUSTOMER_CERTIFICATION_BOUNDARY","MFE_30D_pct":7.1,"MAE_30D_pct":-18.2,"MFE_90D_pct":12.6,"MAE_90D_pct":-26.8,"MFE_180D_pct":48.2,"MAE_180D_pct":-26.8,"peak_date":"2025-01-22","peak_price":15130,"trough_date_180D":"2024-12-09","trough_price_180D":7470,"max_drawdown_after_peak_180D_pct":-43.4,"positive_or_counterexample":"counterexample_boundary","current_profile_verdict":"CXL_customer_certification_is_memory_test_positive_but_not_clean_C07_HBM_order_until_HBM_burn_in_order_occurs","evidence_url":"https://www.uni-test.com/","evidence_summary":"Company IR noted CXL 2.0 tester customer-certification shipment. This is memory-test capability but not yet named HBM equipment order/revenue conversion in 2024.","row_type":"trigger","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","calibration_usable":true,"representative_for_aggregate":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C07|086390|2024-08-09","dedupe_key":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|086390|Stage2|2024-08-09","profile_path":"atlas/symbol_profiles/086/086390.json","tradable_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086390/2024.csv","source_proxy_only":true,"current_profile_error":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

## 5. Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","case_id":"C07-L127-01","symbol":"110990","trigger_type":"Stage2-Actionable","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","eps_fcf_revision":13,"earnings_visibility":13,"bottleneck_pricing":12,"market_mispricing":9,"valuation_rerating":9,"capital_allocation":4,"information_confidence":12,"raw_total":72,"stage_before_shadow":"Stage2-Actionable","stage_after_shadow":"Stage2-Actionable","why_stage_after_shadow":"named customer contract plus process-role bridge; not Green until repeat order/margin conversion"}
{"row_type":"score_simulation","case_id":"C07-L127-02","symbol":"110990","trigger_type":"Stage4B","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","eps_fcf_revision":9,"earnings_visibility":9,"bottleneck_pricing":10,"market_mispricing":7,"valuation_rerating":8,"capital_allocation":3,"information_confidence":10,"raw_total":56,"stage_before_shadow":"Stage2-Actionable","stage_after_shadow":"Stage4B-local","why_stage_after_shadow":"late repeat order after first reprice produced severe MAE"}
{"row_type":"score_simulation","case_id":"C07-L127-03","symbol":"451220","trigger_type":"Stage2","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","eps_fcf_revision":7,"earnings_visibility":7,"bottleneck_pricing":8,"market_mispricing":7,"valuation_rerating":7,"capital_allocation":2,"information_confidence":7,"raw_total":45,"stage_before_shadow":"Stage2","stage_after_shadow":"Stage2-watch","why_stage_after_shadow":"source-proxy/product identity without named HBM order/revenue bridge"}
{"row_type":"score_simulation","case_id":"C07-L127-04","symbol":"089790","trigger_type":"Stage2","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","eps_fcf_revision":7,"earnings_visibility":7,"bottleneck_pricing":8,"market_mispricing":7,"valuation_rerating":7,"capital_allocation":2,"information_confidence":7,"raw_total":45,"stage_before_shadow":"Stage2","stage_after_shadow":"Stage2-watch","why_stage_after_shadow":"source-proxy/product identity without named HBM order/revenue bridge"}
{"row_type":"score_simulation","case_id":"C07-L127-05","symbol":"396470","trigger_type":"Stage2","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","eps_fcf_revision":7,"earnings_visibility":7,"bottleneck_pricing":8,"market_mispricing":7,"valuation_rerating":7,"capital_allocation":2,"information_confidence":7,"raw_total":45,"stage_before_shadow":"Stage2","stage_after_shadow":"Stage2-watch","why_stage_after_shadow":"source-proxy/product identity without named HBM order/revenue bridge"}
{"row_type":"score_simulation","case_id":"C07-L127-06","symbol":"405100","trigger_type":"Stage2","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","eps_fcf_revision":7,"earnings_visibility":7,"bottleneck_pricing":8,"market_mispricing":7,"valuation_rerating":7,"capital_allocation":2,"information_confidence":7,"raw_total":45,"stage_before_shadow":"Stage2","stage_after_shadow":"Stage2-watch","why_stage_after_shadow":"source-proxy/product identity without named HBM order/revenue bridge"}
{"row_type":"score_simulation","case_id":"C07-L127-07","symbol":"086390","trigger_type":"Stage2","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","eps_fcf_revision":8,"earnings_visibility":8,"bottleneck_pricing":9,"market_mispricing":7,"valuation_rerating":8,"capital_allocation":2,"information_confidence":8,"raw_total":50,"stage_before_shadow":"Stage2","stage_after_shadow":"Stage2-watch","why_stage_after_shadow":"adjacent memory-test capability but not C07 HBM order conversion"}
```

## 6. Aggregate / shadow rule / residual rows JSONL

```jsonl
{"row_type":"aggregate","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","case_count":7,"trigger_count":7,"representative_trigger_count":7,"positive_case_count":1,"counterexample_count":6,"stage4b_overlay_count":6,"stage4c_case_count":0,"avg_MFE_90D_pct":18.9,"avg_MAE_90D_pct":-38.7,"median_MFE_180D_pct":12.5,"median_MAE_180D_pct":-55.8,"current_profile_error_count":6,"rule_candidate":"C07_ORDER_CONVERSION_REQUIRES_NAMED_HBM_CUSTOMER_AND_REPEAT_REVENUE_BRIDGE_WITH_LATE_CONFIRMATION_4B_CAP"}
{"row_type":"shadow_weight","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","rule_candidate":"C07_ORDER_CONVERSION_REQUIRES_NAMED_HBM_CUSTOMER_AND_REPEAT_REVENUE_BRIDGE_WITH_LATE_CONFIRMATION_4B_CAP","suggested_direction":"scope_rule_not_global_weight_change","production_scoring_changed":false,"shadow_weight_only":true,"positive_increment_condition":"named HBM process equipment order/PO/shipment to memory customer plus revenue or margin bridge before large reprice","negative_condition":"sales attempt, product identity, reliability-service, environmental-control component, or late repeat contract after first reprice","stage_effect":"Stage2-watch stays watch until order conversion; Stage2-Actionable only for named customer order; late repeat orders become Stage4B-local overlay."}
{"row_type":"residual_contribution","round":"R2","loop":"127","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","new_independent_case_count":7,"reused_case_count":1,"new_symbol_count":6,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":7,"positive_case_count":1,"counterexample_count":6,"current_profile_error_count":6,"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"one_line_summary":"This loop adds 7 independent C07 rows, 6 counterexamples, and 6 residual errors around order conversion versus product/proxy/late-confirmation traps."}
{"row_type":"narrative_only","symbol":"122640","company_name":"예스티","trigger_date":"2024-06-03","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"HBM_PRESSURE_EQUIPMENT_CUMULATIVE_ORDER","source_url":"https://yest.co.kr/Jsource/Jboard/content.asp?jb_idx=14&ji_num=9","reason_blocked":"share_count_changed_inside_180D_window_requires_profile_level_corporate_action_check_before_representative_aggregate","calibration_usable":false,"note":"Useful C07 evidence; not used as representative row in this MD."}
```

## 7. Canonical rule candidate

```text
canonical_archetype_rule_candidate = C07_ORDER_CONVERSION_REQUIRES_NAMED_HBM_CUSTOMER_AND_REPEAT_REVENUE_BRIDGE_WITH_LATE_CONFIRMATION_4B_CAP
```

Proposed C07-specific shadow rule:

```text
if canonical_archetype_id == C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH:
    if evidence has named HBM/advanced-memory customer + order/PO/contract + process role + shipment/revenue/margin bridge:
        allow Stage2-Actionable
    if evidence is product identity, sample, sales attempt, reliability-service exposure, environment-control component exposure, or generic HBM vocabulary:
        cap at Stage2-watch
    if evidence is a repeat order after a major local reprice or after 30D/90D MFE has already been captured:
        attach Stage4B-local/profit-lock overlay
    Stage3-Yellow requires repeat order or revenue conversion, not relative strength alone
```

This is not a global scoring change. It is a C07 scope rule candidate.

## 8. Batch ingest self-audit

```text
filename_matches_standard_v12_pattern = true
metadata_round_loop_matches_filename = true
row_type_trigger_rows_have_entry_date = true
row_type_trigger_rows_have_entry_price = true
trigger_type_in_canonical_stage_label_set = true
MFE_30D_pct / MFE_90D_pct / MFE_180D_pct present = true
MAE_30D_pct / MAE_90D_pct / MAE_180D_pct present = true
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
round_sector_consistency = pass
calibration_usable_trigger_count = 7
representative_trigger_count = 7
narrative_only_blocked_count = 1
```

## 9. Deferred Coding Agent Handoff Prompt — do not execute now

```text
You are the later stock_agent coding agent. Ingest this standalone v12 residual MD together with the full batch of R1~R13 residual files. Parse trigger rows, score simulations, aggregate rows, shadow weight rows, and residual contribution rows. Do not change production scoring from this single MD. Only promote the C07 rule candidate if the broader C07 batch confirms that named-customer order/conversion rows outperform product-identity, sample, sales-attempt, and late-repeat-order proxy rows on MFE/MAE and false-positive rate.
```

## 10. Completion state

```text
completed_round = R2
completed_loop = 127
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C07 under_30 follow-up
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING_followup_margin_FCF_bridge; C01_ORDER_BACKLOG_MARGIN_BRIDGE_followup_new_symbol_only; C06_HBM_MEMORY_CUSTOMER_CAPACITY_followup_new_customer_route; C02_POWER_GRID_DATACENTER_CAPEX_followup_new_symbols_only; R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_if_source_proxy_repair_needed
```

This loop adds 7 usable C07 trigger rows, 6 counterexamples, and 6 residual errors for R2/L2/C07.

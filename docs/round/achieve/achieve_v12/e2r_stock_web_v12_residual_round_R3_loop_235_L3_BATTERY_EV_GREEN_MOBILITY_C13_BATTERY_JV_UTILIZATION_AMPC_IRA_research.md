# E2R Stock-Web v12 Residual Research — R3 loop 235 / C13 battery equipment-material route guard

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R3
selected_loop = 235
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = C13_BATTERY_EQUIPMENT_MATERIAL_ROUTE_TO_UTILIZATION_CASHFLOW_GUARD
output_file = e2r_stock_web_v12_residual_round_R3_loop_235_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
price_source = Songdaiki/stock-web / atlas/ohlcv_tradable_by_symbol_year
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## 1. Required first-read / selection basis

`docs/core/V12_Research_No_Repeat_Index.md` 기준으로 현재 corpus는 단순 row-fill 단계가 아니다. C01~C32는 모두 80 row 이상이고, 이번 선택은 Priority 1의 C13 품질 보강과 Priority 0의 direct URL / proxy / MFE-MAE repair를 함께 따른다. 직전 사용자 노출 산출물의 C01 반복을 피하고, local archive의 C13 max loop 234 다음 값인 loop 235를 사용했다.

핵심 부족점은 **battery route headline → customer/order finality → utilization/calloff → ex-credit cashflow**의 사다리를 덜 분리한다는 점이다. 배터리 장비·부품·소재 route는 파이프를 설치했다는 소식이고, utilization/cashflow는 그 파이프 안으로 실제 물이 흐르는지다. 이번 loop는 바로 그 중간 밸브를 본다.

## 2. Stock-Web manifest / schema check

- `manifest.max_date = 2026-02-20`
- `price_adjustment_status = raw_unadjusted_marcap`
- `tradable_row_count = 14,354,401`
- `raw_row_count = 15,214,118`
- tradable shard columns: `d,o,h,l,c,v,a,mc,s,m`
- MFE/MAE rule: entry 이후 N개 tradable row의 max high / min low 기반
- entry price basis: same-or-next tradable day open
- corporate-action gate: 180D window 내 shares change >=20% 후보는 trigger 제외

## 3. Novelty and anti-duplicate audit

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_key_count_vs_local_C13_archive = 0
calibration_usable_trigger_count = 8
strict_new_symbol_count_vs_local_C13_archive = 6
under_used_symbol_reused_with_new_trigger_family = 2
narrative_only_or_rejected_count = 2
minimum_new_symbol_count = pass
minimum_positive_case_count = pass
minimum_counterexample_count = pass
```

Narrative-only로 분리한 후보는 `340930`과 `267320`이다. 둘 다 배터리 route evidence는 있었지만 Stock-Web raw/unadjusted shares 기준으로 180D window corporate-action contamination gate에 걸려 calibration trigger에는 넣지 않았다.

## 4. Case matrix

| symbol | symbol_name | trigger_family | event_summary | evidence_quality | current_profile_stage | recommended_stage_after_shadow_rule |
|---|---|---|---|---|---|---|
| 382480 | 지아이텍 | slot_die_product_route_without_order_conversion | InterBattery 2024 slot-die product route without order finality | company_site_news_proxy | Stage2-Actionable | Stage2-watch |
| 148930 | 에이치와이티씨 | precision_parts_customer_rnd_route_after_reset | 4Q24 IR precision battery parts and customer co-development route | company_ir_pdf | Stage3-Yellow | Stage3-Yellow |
| 333620 | 엔시스 | inspection_equipment_order_growth_without_cash_conversion | battery inspection equipment new-order and solid-state line-up route | broker_report_url_proxy | Stage2-Actionable | Stage2-watch |
| 161580 | 필옵틱스 | battery_automation_business_route_with_semiconductor_mix | shareholder-meeting notice confirms EV battery automation process route | official_disclosure_business_route | Stage3-Green | Stage3-Yellow+4B-watch |
| 095500 | 미래나노텍 | lithium_hydroxide_material_route_high_mae_phase_guard | subsidiary lithium hydroxide mass-production route for cathode material | news_direct_company_route | Stage3-Green | Stage4B-watch |
| 051490 | 나라엠앤디 | battery_pack_ess_component_customer_route_positive | EV battery-pack / ESS component sales-expansion route | news_report_with_customer_route | Stage3-Green | Stage3-Green |
| 217820 | 원익피앤이 | direct_equipment_contract_after_capex_slowdown_high_mae | KRW 33.8bn secondary-battery manufacturing equipment contract | news_direct_disclosure_proxy | Stage2-Actionable | Stage4B-watch |
| 378340 | 필에너지 | equipment_backlog_recognition_lag_after_rerating | battery equipment order-recognition lag and all-solid-state optionality report | broker_report_url_proxy | Stage2-Actionable | Stage4B-watch |

## 5. Trigger-level Stock-Web backtest

| symbol | symbol_name | trigger_type | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | case_result |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 382480 | 지아이텍 | Stage2 | 2024-03-06 | 3070 | 16.12 | -10.1 | 16.12 | -16.45 | 16.12 | -37.13 | counterexample |
| 148930 | 에이치와이티씨 | Stage3-Yellow | 2025-02-19 | 3640 | 31.73 | -2.2 | 31.73 | -2.75 | 31.73 | -13.46 | positive |
| 333620 | 엔시스 | Stage2-Actionable | 2024-07-29 | 11100 | 17.84 | -29.46 | 17.84 | -37.84 | 17.84 | -43.15 | counterexample |
| 161580 | 필옵틱스 | Stage3-Yellow | 2025-03-10 | 39150 | 23.37 | -28.86 | 23.37 | -28.86 | 50.96 | -28.86 | positive |
| 095500 | 미래나노텍 | Stage4B | 2023-06-27 | 22300 | 37.67 | -4.04 | 37.67 | -32.74 | 37.67 | -41.75 | positive_with_guardrail |
| 051490 | 나라엠앤디 | Stage3-Green | 2020-07-13 | 7320 | 21.04 | -10.52 | 91.26 | -10.52 | 100.14 | -10.52 | positive |
| 217820 | 원익피앤이 | Stage4B | 2024-03-13 | 5760 | 6.6 | -13.02 | 6.6 | -36.11 | 6.6 | -60.42 | counterexample |
| 378340 | 필에너지 | Stage4B | 2024-04-19 | 26700 | 5.99 | -21.35 | 5.99 | -55.51 | 5.99 | -58.05 | counterexample |

## 6. Residual profile stress test

현재 profile의 잔여 오류는 세 갈래다.

1. **Route-only를 conversion처럼 읽는 오류**: `382480`, `333620`처럼 제품 route·검사장비 route는 있지만 order/calloff/cash bridge가 약하면 Stage2-watch가 맞다.
2. **Direct order라도 cycle/phase가 나쁘면 Green이 아닌 오류**: `217820`, `378340`은 직접 수주나 수주잔고 인식 기대가 있었지만 180D MAE가 깊다. 이 경우 hard 4C가 아니라 4B-watch다.
3. **Material/product route positive도 cashflow 전까지 cap이 필요한 오류**: `095500`, `161580`처럼 MFE는 열렸지만 MAE가 깊거나 사업 mix가 섞이면 Green 대신 Yellow/4B overlay가 맞다.

## 7. Sector-specific rule candidate

`L3_BATTERY_EV_GREEN_MOBILITY`에서는 정책/JV/offtake/product-route headline, customer/order finality, utilization/calloff, ex-credit margin/cash conversion, price phase를 분리해야 한다. 배터리 route evidence는 에너지 통로를 열지만, promotion은 실제 전류가 흐르는지까지 보아야 한다.

## 8. Canonical archetype rule candidate

`C13_BATTERY_JV_UTILIZATION_AMPC_IRA` should use a **route-to-utilization-to-cashflow ladder**:

```text
MOU / product route / equipment capability
→ named customer or order finality
→ calloff / shipment / utilization
→ ex-credit profit or cash conversion
→ price-phase sanity
```

Stage2는 direct route에서 시작할 수 있다. Stage2-Actionable은 고객·주문 경로가 있어야 한다. Stage3-Yellow는 finality와 가격 phase가 맞을 때만 허용한다. Stage3-Green은 utilization/cash conversion이 보여야 한다. High-MAE with surviving route는 hard 4C가 아니라 4B-watch다.

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C13_R3L235_CASE001_382480","symbol":"382480","symbol_name":"지아이텍","case_result":"counterexample","calibration_usable":true,"novelty_basis":"strict-new or under-used C13 symbol plus new trigger family"}
{"row_type":"case","case_id":"C13_R3L235_CASE002_148930","symbol":"148930","symbol_name":"에이치와이티씨","case_result":"positive","calibration_usable":true,"novelty_basis":"strict-new or under-used C13 symbol plus new trigger family"}
{"row_type":"case","case_id":"C13_R3L235_CASE003_333620","symbol":"333620","symbol_name":"엔시스","case_result":"counterexample","calibration_usable":true,"novelty_basis":"strict-new or under-used C13 symbol plus new trigger family"}
{"row_type":"case","case_id":"C13_R3L235_CASE004_161580","symbol":"161580","symbol_name":"필옵틱스","case_result":"positive","calibration_usable":true,"novelty_basis":"strict-new or under-used C13 symbol plus new trigger family"}
{"row_type":"case","case_id":"C13_R3L235_CASE005_095500","symbol":"095500","symbol_name":"미래나노텍","case_result":"positive_with_guardrail","calibration_usable":true,"novelty_basis":"strict-new or under-used C13 symbol plus new trigger family"}
{"row_type":"case","case_id":"C13_R3L235_CASE006_051490","symbol":"051490","symbol_name":"나라엠앤디","case_result":"positive","calibration_usable":true,"novelty_basis":"strict-new or under-used C13 symbol plus new trigger family"}
{"row_type":"case","case_id":"C13_R3L235_CASE007_217820","symbol":"217820","symbol_name":"원익피앤이","case_result":"counterexample","calibration_usable":true,"novelty_basis":"strict-new or under-used C13 symbol plus new trigger family"}
{"row_type":"case","case_id":"C13_R3L235_CASE008_378340","symbol":"378340","symbol_name":"필에너지","case_result":"counterexample","calibration_usable":true,"novelty_basis":"strict-new or under-used C13 symbol plus new trigger family"}
{"row_type":"trigger","case_id":"C13_R3L235_CASE001_382480","selected_round":"R3","selected_loop":235,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_BATTERY_EQUIPMENT_MATERIAL_ROUTE_TO_UTILIZATION_CASHFLOW_GUARD","symbol":"382480","symbol_name":"지아이텍","trigger_type":"Stage2","trigger_family":"slot_die_product_route_without_order_conversion","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":3070,"entry_price_basis":"next_or_same_tradable_open","price_source":"Songdaiki/stock-web:atlas/ohlcv_tradable_by_symbol_year","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"evidence_url":"https://www.gitech.com/bbs/board.php?bo_table=board&wr_id=47","evidence_quality":"company_site_news_proxy","event_summary":"InterBattery 2024 slot-die product route without order finality","source_note":"InterBattery 2024에서 2차전지 코팅 공정 핵심부품 slot-die 제품군을 공개한 route evidence. 고객 call-off/order가 아니라 제품 route다.","case_result":"counterexample","current_profile_stage":"Stage2-Actionable","recommended_stage_after_shadow_rule":"Stage2-watch","current_profile_error":true,"MFE_30D_pct":16.12,"MAE_30D_pct":-10.1,"peak_30D_date":"2024-03-12","trough_30D_date":"2024-04-17","MFE_90D_pct":16.12,"MAE_90D_pct":-16.45,"peak_90D_date":"2024-03-12","trough_90D_date":"2024-05-30","MFE_180D_pct":16.12,"MAE_180D_pct":-37.13,"peak_180D_date":"2024-03-12","trough_180D_date":"2024-08-05","window_180D_end":"2024-11-28","shares_change_180D_max_pct":0.0,"return_close_180D_pct":-30.78}
{"row_type":"trigger","case_id":"C13_R3L235_CASE002_148930","selected_round":"R3","selected_loop":235,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_BATTERY_EQUIPMENT_MATERIAL_ROUTE_TO_UTILIZATION_CASHFLOW_GUARD","symbol":"148930","symbol_name":"에이치와이티씨","trigger_type":"Stage3-Yellow","trigger_family":"precision_parts_customer_rnd_route_after_reset","trigger_date":"2025-02-19","entry_date":"2025-02-19","entry_price":3640,"entry_price_basis":"next_or_same_tradable_open","price_source":"Songdaiki/stock-web:atlas/ohlcv_tradable_by_symbol_year","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"evidence_url":"https://file.alphasquare.co.kr/media/pdfs/company-ir/20250219%EC%97%90%EC%9D%B4%EC%B9%98%EC%99%80%EC%9D%B4%ED%8B%B0%EC%94%A8_%EC%A3%BC%EC%9A%94_%EA%B2%BD%EC%98%81%ED%98%84%ED%99%A9_%EC%84%A4%EB%AA%85.pdf","evidence_quality":"company_ir_pdf","event_summary":"4Q24 IR precision battery parts and customer co-development route","source_note":"고객 공동개발/초정밀 2차전지 부품 route가 있으나 이용률·현금전환 확인 전이라 Yellow cap.","case_result":"positive","current_profile_stage":"Stage3-Yellow","recommended_stage_after_shadow_rule":"Stage3-Yellow","current_profile_error":false,"MFE_30D_pct":31.73,"MAE_30D_pct":-2.2,"peak_30D_date":"2025-02-24","trough_30D_date":"2025-04-01","MFE_90D_pct":31.73,"MAE_90D_pct":-2.75,"peak_90D_date":"2025-02-24","trough_90D_date":"2025-04-07","MFE_180D_pct":31.73,"MAE_180D_pct":-13.46,"peak_180D_date":"2025-02-24","trough_180D_date":"2025-11-06","window_180D_end":"2025-11-13","shares_change_180D_max_pct":0.0,"return_close_180D_pct":-9.34}
{"row_type":"trigger","case_id":"C13_R3L235_CASE003_333620","selected_round":"R3","selected_loop":235,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_BATTERY_EQUIPMENT_MATERIAL_ROUTE_TO_UTILIZATION_CASHFLOW_GUARD","symbol":"333620","symbol_name":"엔시스","trigger_type":"Stage2-Actionable","trigger_family":"inspection_equipment_order_growth_without_cash_conversion","trigger_date":"2024-07-29","entry_date":"2024-07-29","entry_price":11100,"entry_price_basis":"next_or_same_tradable_open","price_source":"Songdaiki/stock-web:atlas/ohlcv_tradable_by_symbol_year","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"evidence_url":"https://kbthink.com/securities-view.html?docId=20240726153732160K","evidence_quality":"broker_report_url_proxy","event_summary":"battery inspection equipment new-order and solid-state line-up route","source_note":"신규 수주 호조와 전고체 라인업 route가 있었지만 90/180D 경로는 높은 MAE로 변했다.","case_result":"counterexample","current_profile_stage":"Stage2-Actionable","recommended_stage_after_shadow_rule":"Stage2-watch","current_profile_error":true,"MFE_30D_pct":17.84,"MAE_30D_pct":-29.46,"peak_30D_date":"2024-08-26","trough_30D_date":"2024-08-05","MFE_90D_pct":17.84,"MAE_90D_pct":-37.84,"peak_90D_date":"2024-08-26","trough_90D_date":"2024-12-09","MFE_180D_pct":17.84,"MAE_180D_pct":-43.15,"peak_180D_date":"2024-08-26","trough_180D_date":"2025-04-09","window_180D_end":"2025-04-25","shares_change_180D_max_pct":0.0,"return_close_180D_pct":-32.07}
{"row_type":"trigger","case_id":"C13_R3L235_CASE004_161580","selected_round":"R3","selected_loop":235,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_BATTERY_EQUIPMENT_MATERIAL_ROUTE_TO_UTILIZATION_CASHFLOW_GUARD","symbol":"161580","symbol_name":"필옵틱스","trigger_type":"Stage3-Yellow","trigger_family":"battery_automation_business_route_with_semiconductor_mix","trigger_date":"2025-03-10","entry_date":"2025-03-10","entry_price":39150,"entry_price_basis":"next_or_same_tradable_open","price_source":"Songdaiki/stock-web:atlas/ohlcv_tradable_by_symbol_year","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"evidence_url":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250310000360&langTpCd=0&method=search&orgid=F&rcpno=20250310000332&tran=Y","evidence_quality":"official_disclosure_business_route","event_summary":"shareholder-meeting notice confirms EV battery automation process route","source_note":"공식 공고의 사업 route는 직접성이 있으나 반도체/디스플레이 mix와 30D high-MAE 때문에 Green은 보류.","case_result":"positive","current_profile_stage":"Stage3-Green","recommended_stage_after_shadow_rule":"Stage3-Yellow+4B-watch","current_profile_error":true,"MFE_30D_pct":23.37,"MAE_30D_pct":-28.86,"peak_30D_date":"2025-03-13","trough_30D_date":"2025-04-08","MFE_90D_pct":23.37,"MAE_90D_pct":-28.86,"peak_90D_date":"2025-03-13","trough_90D_date":"2025-04-08","MFE_180D_pct":50.96,"MAE_180D_pct":-28.86,"peak_180D_date":"2025-11-04","trough_180D_date":"2025-04-08","window_180D_end":"2025-12-01","shares_change_180D_max_pct":2.42,"return_close_180D_pct":5.24}
{"row_type":"trigger","case_id":"C13_R3L235_CASE005_095500","selected_round":"R3","selected_loop":235,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_BATTERY_EQUIPMENT_MATERIAL_ROUTE_TO_UTILIZATION_CASHFLOW_GUARD","symbol":"095500","symbol_name":"미래나노텍","trigger_type":"Stage4B","trigger_family":"lithium_hydroxide_material_route_high_mae_phase_guard","trigger_date":"2023-06-27","entry_date":"2023-06-27","entry_price":22300,"entry_price_basis":"next_or_same_tradable_open","price_source":"Songdaiki/stock-web:atlas/ohlcv_tradable_by_symbol_year","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"evidence_url":"https://www.electimes.com/news/articleView.html?idxno=322147","evidence_quality":"news_direct_company_route","event_summary":"subsidiary lithium hydroxide mass-production route for cathode material","source_note":"수산화리튬 양산 route는 명확했지만 raw-lithium/material cycle과 가격 phase가 180D MAE로 역전됐다.","case_result":"positive_with_guardrail","current_profile_stage":"Stage3-Green","recommended_stage_after_shadow_rule":"Stage4B-watch","current_profile_error":true,"MFE_30D_pct":37.67,"MAE_30D_pct":-4.04,"peak_30D_date":"2023-07-26","trough_30D_date":"2023-06-27","MFE_90D_pct":37.67,"MAE_90D_pct":-32.74,"peak_90D_date":"2023-07-26","trough_90D_date":"2023-10-26","MFE_180D_pct":37.67,"MAE_180D_pct":-41.75,"peak_180D_date":"2023-07-26","trough_180D_date":"2024-02-01","window_180D_end":"2024-03-20","shares_change_180D_max_pct":0.0,"return_close_180D_pct":-13.23}
{"row_type":"trigger","case_id":"C13_R3L235_CASE006_051490","selected_round":"R3","selected_loop":235,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_BATTERY_EQUIPMENT_MATERIAL_ROUTE_TO_UTILIZATION_CASHFLOW_GUARD","symbol":"051490","symbol_name":"나라엠앤디","trigger_type":"Stage3-Green","trigger_family":"battery_pack_ess_component_customer_route_positive","trigger_date":"2020-07-13","entry_date":"2020-07-13","entry_price":7320,"entry_price_basis":"next_or_same_tradable_open","price_source":"Songdaiki/stock-web:atlas/ohlcv_tradable_by_symbol_year","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"evidence_url":"https://www.g-enews.com/article/Securities/2020/07/202007131049481873442088f476_1","evidence_quality":"news_report_with_customer_route","event_summary":"EV battery-pack / ESS component sales-expansion route","source_note":"LG계열 배터리팩/ESS 부품 route와 매출비중 전환이 함께 확인된 reset-cycle positive.","case_result":"positive","current_profile_stage":"Stage3-Green","recommended_stage_after_shadow_rule":"Stage3-Green","current_profile_error":false,"MFE_30D_pct":21.04,"MAE_30D_pct":-10.52,"peak_30D_date":"2020-08-10","trough_30D_date":"2020-08-21","MFE_90D_pct":91.26,"MAE_90D_pct":-10.52,"peak_90D_date":"2020-09-23","trough_90D_date":"2020-08-21","MFE_180D_pct":100.14,"MAE_180D_pct":-10.52,"peak_180D_date":"2021-01-04","trough_180D_date":"2020-08-21","window_180D_end":"2021-04-05","shares_change_180D_max_pct":0.0,"return_close_180D_pct":40.71}
{"row_type":"trigger","case_id":"C13_R3L235_CASE007_217820","selected_round":"R3","selected_loop":235,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_BATTERY_EQUIPMENT_MATERIAL_ROUTE_TO_UTILIZATION_CASHFLOW_GUARD","symbol":"217820","symbol_name":"원익피앤이","trigger_type":"Stage4B","trigger_family":"direct_equipment_contract_after_capex_slowdown_high_mae","trigger_date":"2024-03-13","entry_date":"2024-03-13","entry_price":5760,"entry_price_basis":"next_or_same_tradable_open","price_source":"Songdaiki/stock-web:atlas/ohlcv_tradable_by_symbol_year","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"evidence_url":"https://alphasquare.co.kr/home/stock-issue?code=217820&type=news","evidence_quality":"news_direct_disclosure_proxy","event_summary":"KRW 33.8bn secondary-battery manufacturing equipment contract","source_note":"직접 수주 공시는 강하지만 전방 capex 둔화와 phase가 나쁘면 direct order도 곧장 Green으로 갈 수 없다.","case_result":"counterexample","current_profile_stage":"Stage2-Actionable","recommended_stage_after_shadow_rule":"Stage4B-watch","current_profile_error":true,"MFE_30D_pct":6.6,"MAE_30D_pct":-13.02,"peak_30D_date":"2024-03-13","trough_30D_date":"2024-04-19","MFE_90D_pct":6.6,"MAE_90D_pct":-36.11,"peak_90D_date":"2024-03-13","trough_90D_date":"2024-07-18","MFE_180D_pct":6.6,"MAE_180D_pct":-60.42,"peak_180D_date":"2024-03-13","trough_180D_date":"2024-12-04","window_180D_end":"2024-12-05","shares_change_180D_max_pct":0.0,"return_close_180D_pct":-60.24}
{"row_type":"trigger","case_id":"C13_R3L235_CASE008_378340","selected_round":"R3","selected_loop":235,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_BATTERY_EQUIPMENT_MATERIAL_ROUTE_TO_UTILIZATION_CASHFLOW_GUARD","symbol":"378340","symbol_name":"필에너지","trigger_type":"Stage4B","trigger_family":"equipment_backlog_recognition_lag_after_rerating","trigger_date":"2024-04-19","entry_date":"2024-04-19","entry_price":26700,"entry_price_basis":"next_or_same_tradable_open","price_source":"Songdaiki/stock-web:atlas/ohlcv_tradable_by_symbol_year","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true,"window_180D_corporate_action_contaminated":false,"evidence_url":"https://ssl.pstatic.net/imgstock/upload/research/company/1713482263156.pdf","evidence_quality":"broker_report_url_proxy","event_summary":"battery equipment order-recognition lag and all-solid-state optionality report","source_note":"2023년말 수주가 2024년 실적에 반영될 가능성은 있었지만 rerating 뒤라 4B watch가 먼저였다.","case_result":"counterexample","current_profile_stage":"Stage2-Actionable","recommended_stage_after_shadow_rule":"Stage4B-watch","current_profile_error":true,"MFE_30D_pct":5.99,"MAE_30D_pct":-21.35,"peak_30D_date":"2024-04-24","trough_30D_date":"2024-05-31","MFE_90D_pct":5.99,"MAE_90D_pct":-55.51,"peak_90D_date":"2024-04-24","trough_90D_date":"2024-08-08","MFE_180D_pct":5.99,"MAE_180D_pct":-58.05,"peak_180D_date":"2024-04-24","trough_180D_date":"2024-12-10","window_180D_end":"2025-01-15","shares_change_180D_max_pct":0.18,"return_close_180D_pct":-47.57}
{"row_type":"score_simulation","case_id":"C13_R3L235_CASE001_382480","symbol":"382480","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","component_order":"EPS/Vis/Bott/Mis/Val/Cap/Info","EPS":12,"Vis":14,"Bott":13,"Mis":8,"Val":7,"Cap":4,"Info":12,"raw_total_score":70,"current_profile_stage":"Stage2-Actionable","shadow_recommended_stage":"Stage2-watch","alignment_label":"residual_error"}
{"row_type":"score_simulation","case_id":"C13_R3L235_CASE002_148930","symbol":"148930","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","component_order":"EPS/Vis/Bott/Mis/Val/Cap/Info","EPS":16,"Vis":16,"Bott":12,"Mis":11,"Val":8,"Cap":8,"Info":13,"raw_total_score":84,"current_profile_stage":"Stage3-Yellow","shadow_recommended_stage":"Stage3-Yellow","alignment_label":"aligned_or_guarded"}
{"row_type":"score_simulation","case_id":"C13_R3L235_CASE003_333620","symbol":"333620","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","component_order":"EPS/Vis/Bott/Mis/Val/Cap/Info","EPS":13,"Vis":15,"Bott":12,"Mis":8,"Val":7,"Cap":6,"Info":12,"raw_total_score":73,"current_profile_stage":"Stage2-Actionable","shadow_recommended_stage":"Stage2-watch","alignment_label":"residual_error"}
{"row_type":"score_simulation","case_id":"C13_R3L235_CASE004_161580","symbol":"161580","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","component_order":"EPS/Vis/Bott/Mis/Val/Cap/Info","EPS":17,"Vis":15,"Bott":13,"Mis":10,"Val":6,"Cap":7,"Info":14,"raw_total_score":82,"current_profile_stage":"Stage3-Green","shadow_recommended_stage":"Stage3-Yellow+4B-watch","alignment_label":"residual_error"}
{"row_type":"score_simulation","case_id":"C13_R3L235_CASE005_095500","symbol":"095500","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","component_order":"EPS/Vis/Bott/Mis/Val/Cap/Info","EPS":18,"Vis":13,"Bott":14,"Mis":9,"Val":5,"Cap":6,"Info":15,"raw_total_score":80,"current_profile_stage":"Stage3-Green","shadow_recommended_stage":"Stage4B-watch","alignment_label":"residual_error"}
{"row_type":"score_simulation","case_id":"C13_R3L235_CASE006_051490","symbol":"051490","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","component_order":"EPS/Vis/Bott/Mis/Val/Cap/Info","EPS":20,"Vis":18,"Bott":15,"Mis":13,"Val":9,"Cap":9,"Info":15,"raw_total_score":99,"current_profile_stage":"Stage3-Green","shadow_recommended_stage":"Stage3-Green","alignment_label":"aligned_or_guarded"}
{"row_type":"score_simulation","case_id":"C13_R3L235_CASE007_217820","symbol":"217820","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","component_order":"EPS/Vis/Bott/Mis/Val/Cap/Info","EPS":13,"Vis":16,"Bott":12,"Mis":7,"Val":4,"Cap":5,"Info":13,"raw_total_score":70,"current_profile_stage":"Stage2-Actionable","shadow_recommended_stage":"Stage4B-watch","alignment_label":"residual_error"}
{"row_type":"score_simulation","case_id":"C13_R3L235_CASE008_378340","symbol":"378340","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","component_order":"EPS/Vis/Bott/Mis/Val/Cap/Info","EPS":14,"Vis":15,"Bott":12,"Mis":7,"Val":4,"Cap":5,"Info":12,"raw_total_score":69,"current_profile_stage":"Stage2-Actionable","shadow_recommended_stage":"Stage4B-watch","alignment_label":"residual_error"}
{"row_type":"aggregate","selected_round":"R3","selected_loop":235,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_BATTERY_EQUIPMENT_MATERIAL_ROUTE_TO_UTILIZATION_CASHFLOW_GUARD","calibration_usable_trigger_count":8,"positive_case_count":4,"counterexample_count":4,"current_profile_error_count":6,"strict_new_symbol_count_vs_local_C13_archive":6,"narrative_only_or_rejected_count":2,"rows_missing_required_mfe_mae":0,"hard_duplicate_key_count_vs_local_C13_archive":0}
{"row_type":"shadow_weight","selected_round":"R3","selected_loop":235,"canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","axis":"c13_route_to_utilization_cashflow_and_phase_guard","production_scoring_changed":false,"shadow_weight_only":true,"proposed_effect":"Cap route-only evidence below Green unless customer/order finality and utilization/cash conversion are visible; high-MAE with surviving route goes 4B-watch not hard4C."}
{"row_type":"residual_contribution","selected_round":"R3","selected_loop":235,"canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"c13_battery_equipment_material_route_to_utilization_cashflow_guard","existing_axis_strengthened":"stage2_required_bridge; stage3_green_revision_min_by_ex_credit_cashflow; local_4b_watch_guard","existing_axis_weakened":"hard_4c_thesis_break_routes_to_4c qualified for high-MAE rows with surviving route only"}
{"row_type":"narrative_only","case_id":"C13_R3L235_NARRATIVE01_340930","selected_round":"R3","selected_loop":235,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"340930","symbol_name":"유일에너테크","trigger_date":"2024-03-26","entry_date":"2024-03-26","entry_price":15010,"calibration_usable":false,"reject_reason":"corporate_action_contaminated_180D_window","shares_change_180D_max_pct":198.26,"evidence_url":"https://m.irgo.co.kr/IR-COMP/340930/","event_summary":"recycling MOU / turnkey equipment route but 180D stock-count contamination"}
{"row_type":"narrative_only","case_id":"C13_R3L235_NARRATIVE02_267320","selected_round":"R3","selected_loop":235,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"267320","symbol_name":"나인테크","trigger_date":"2024-11-18","entry_date":"2024-11-18","entry_price":1991,"calibration_usable":false,"reject_reason":"corporate_action_contaminated_180D_window","shares_change_180D_max_pct":29.83,"evidence_url":"https://m.irgo.co.kr/IR-ROOM/267320","event_summary":"3Q24 battery-equipment recovery route but 180D stock-count contamination"}
```

## 10. Shadow weight / promotion implication

```text
production_scoring_changed = false
shadow_weight_only = true
new_axis_proposed = c13_battery_equipment_material_route_to_utilization_cashflow_guard
existing_axis_strengthened = stage2_required_bridge; stage3_green_revision_min_by_ex_credit_cashflow; local_4b_watch_guard
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c qualified for high-MAE rows with surviving route only
```

No immediate production patch is proposed. The coding agent should only use this as a batch candidate after multiple loops confirm the same route/finality/utilization split.

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff inside the research session.

When batch-applying v12 residual calibration artifacts, ingest this MD as a standalone historical calibration file. Parse only machine-readable JSONL rows with row_type in [case, trigger, score_simulation, aggregate, shadow_weight, residual_contribution, narrative_only]. Do not treat narrative_only rows as promotion evidence. For C13_BATTERY_JV_UTILIZATION_AMPC_IRA, evaluate whether a scoped rule can separate product-route/order-finality/utilization/ex-credit cashflow. Preserve production scoring unless multiple validated artifacts support the same axis. Never loosen Stage3-Green globally. Use local 4B-watch for high-MAE rows where the customer/product route survives and reserve hard 4C for confirmed route death, funding death, customer loss, or repeated cashflow damage.
```

## 12. Final research state

```text
completed_round = R3
completed_loop = 235
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C13 balance-quality reinforcement + Priority 0 direct URL/proxy/MFE-MAE repair
next_recommended_archetypes = C10 strict-new order-conversion rows; C15 spread freshness rows; C31 non-semi/battery awarded-cashflow rows; C01/C05 direct FCF or cash-conversion rows; R13 only for genuinely new taxonomy compression
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

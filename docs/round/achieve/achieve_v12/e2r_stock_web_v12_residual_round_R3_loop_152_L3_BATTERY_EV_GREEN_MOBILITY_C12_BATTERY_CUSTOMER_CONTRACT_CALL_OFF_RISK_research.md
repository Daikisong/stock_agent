# E2R Stock-Web v12 Residual Research — R3 / loop 152 / C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK

```text
selected_round = R3
selected_loop = 152
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = mixed_c12_customer_calloff_offset_visibility_exit_guard_leaf_set
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection / novelty

No-Repeat Index 원본 기준 C12는 Priority 1의 가장 큰 남은 shortage 구역이었다. 직전 loop 151에서 C12를 1차 보강했으나, 세션 누적 기준으로도 50-row 실전 보정권에는 아직 부족하다고 보고 2차 패스를 수행했다.

이번 loop는 loop151의 상신이디피, TCC스틸, 동원시스템즈, 나노팀, 삼기이브이, 에스피시스템스, 대주전자재료 조합을 피했다. 새 구성은 세아메카닉스, 알멕, 신흥에스이씨, 나라엠앤디, SNT모티브, 유일에너테크, 삼성SDI다.

```text
auto_selected_coverage_gap = index baseline C12 rows 32 -> 39 if accepted; session-aware after loop151 + loop152 ≈ C12 rows 46
need_to_50_after_if_accepted_session_aware = about 4
new_independent_case_count = 7
reused_case_count = 0
same_archetype_new_symbol_count = 7
same_archetype_new_trigger_family_count = 7
calibration_usable_trigger_count = 7
```

## 2. Price source validation

Manifest/schema basis:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
schema_path = atlas/schema.json
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

모든 entry는 tradable shard에서 entry date close `c`를 사용했다. 30D/90D/180D는 entry row 포함 후속 N개 tradable row window 기준으로 계산했다. Corporate-action 후보가 entry~D180 window와 겹치는 row는 쓰지 않았다.

## 3. Case table

|ticker|symbol_name|entry_date|entry_price|trigger_type|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|expected_alignment|
|---|---|---|---|---|---|---|---|---|---|---|---|
|396300|세아메카닉스|2024-06-27|3370.0|Stage2-Actionable|9.35|-31.45|20.92|-31.45|20.92|-40.65|counterexample_with_4B_exit_guard|
|354320|알멕|2024-12-17|23150.0|Stage2|33.26|-3.46|47.73|-9.5|47.73|-9.5|positive_relief_after_contract_risk_reset|
|243840|신흥에스이씨|2024-07-25|7600.0|Stage2|27.37|-16.05|27.37|-35.53|27.37|-50.13|counterexample_high_mae_after_short_mfe|
|051490|나라엠앤디|2024-07-03|4980.0|Stage2|14.26|-24.5|25.1|-24.5|25.1|-33.73|counterexample_derivative_supplier_theme|
|064960|SNT모티브|2024-04-02|44650.0|4C|5.71|-1.01|12.65|-11.65|12.65|-12.32|false_4C_due_to_offset|
|340930|유일에너테크|2022-04-06|19550.0|4C|8.44|-19.95|8.44|-37.6|20.46|-37.6|true_negative_customer_loss|
|006400|삼성SDI|2025-01-24|226500.0|Stage2|9.71|-11.7|9.71|-30.38|30.91|-30.38|positive_after_high_mae_staged_entry|

## 4. Case notes

### C12_152_001_396300_LGES_ENDPLATE_BACKLOG_HIGH_MAE — 세아메카닉스 (396300)

- event_date: `2024-06-27`
- entry_date: `2024-06-27` / entry_price: `3370.0`
- trigger_type: `Stage2-Actionable`
- evidence_url: https://www.thelec.kr/news/articleView.html?idxno=28787
- profile_check: corporate_action_candidate_count=0; window_180D_corporate_action_contaminated=false
- evidence_summary: LG전자/LG에너지솔루션 관계, 자동차부품 수주잔고 5000억원, 올해 매출 목표 1000억~1200억원, 증설과 매출 인식 시점이 제시되었다. 그러나 가격경로는 30D 이후 급락과 180D -40%대 MAE를 보여, 계약/backlog 단어만으로 actionable을 유지하면 안 되는 사례다.
- residual_error: Stage2-Actionable bridge는 인정하지만 30D 이후 high-MAE exit guard가 늦다.

### C12_152_002_354320_ALMAC_EV_CHASM_RELIEF_POSITIVE — 알멕 (354320)

- event_date: `2024-12-17`
- entry_date: `2024-12-17` / entry_price: `23150.0`
- trigger_type: `Stage2`
- evidence_url: https://stock.pstatic.net/stock-research/company/74/20241217_company_744802000.pdf
- profile_check: corporate_action_candidate_count=0; window_180D_corporate_action_contaminated=false
- evidence_summary: EV 부품/배터리 모듈 케이스 고객 기반과 2024년 EV chasm에 따른 고객 투자 축소·발주 지연 리스크가 같이 드러난 상태였다. 이미 가격이 충분히 압축된 entry에서는 hard 4C보다 Stage2-Watch/relief guard가 더 맞았다.
- residual_error: C12를 무조건 call-off negative로만 처리하면 90D/180D +47.7% relief path를 놓친다.

### C12_152_003_243840_SHINHEUNG_SDI_CHAIN_HIGH_MAE — 신흥에스이씨 (243840)

- event_date: `2024-07-25`
- entry_date: `2024-07-25` / entry_price: `7600.0`
- trigger_type: `Stage2`
- evidence_url: https://stock.pstatic.net/stock-research/company/72/20240726_company_586478000.pdf
- profile_check: corporate_action_candidate_date=2024-04-26, entry~D180 밖; window_180D_corporate_action_contaminated=false
- evidence_summary: 삼성SDI를 통한 전기차 배터리 수요 체인과 중대형 각형/원형 배터리 부품 노출이 존재했다. 단기 MFE는 있었으나 90D와 180D MAE가 크게 확대되어, 고객사 demand/call-off 확인 전 Stage2-Actionable로 끌어올리면 위험한 사례다.
- residual_error: customer exposure vocabulary는 bridge가 아니며, high-MAE guard가 필요하다.

### C12_152_004_051490_NARAMND_LGES_THEME_DERIVATIVE_HIGH_MAE — 나라엠앤디 (051490)

- event_date: `2024-07-03`
- entry_date: `2024-07-03` / entry_price: `4980.0`
- trigger_type: `Stage2`
- evidence_url: https://www.globalepic.co.kr/view.php?ud=20240703133449975abe7dc9896_29
- profile_check: corporate_action_candidate_date=2001-12-10 only; window_180D_corporate_action_contaminated=false
- evidence_summary: LG에너지솔루션의 르노향 LFP 대형 수주 뉴스가 나라엠앤디 배터리팩 공급사 테마로 연결됐다. 그러나 회사 자체 call-off, 납품 schedule, margin bridge가 약했고 180D MAE가 -33%대로 커졌다.
- residual_error: 고객사의 대형계약을 2차/3차 derivative supplier에 그대로 pass-through하면 false positive가 된다.

### C12_152_005_064960_SNTMOTIVE_GM_BOLT_STOP_OFFSET_FALSE_4C — SNT모티브 (064960)

- event_date: `2024-04-02`
- entry_date: `2024-04-02` / entry_price: `44650.0`
- trigger_type: `4C`
- evidence_url: https://www.dailyinvest.kr/news/articleView.html?idxno=57958
- profile_check: corporate_action candidates 2025-01-24/2025-02-26 are outside entry~D180; window_180D_corporate_action_contaminated=false
- evidence_summary: GM Bolt향 모터 공급 중단으로 EV program cliff가 발생했지만, HEV/오일펌프/방산 등 offset이 있어 hard 4C로 바로 보내면 과잉반응이 된다. 180D MAE는 제한적이고 MFE도 완만했다.
- residual_error: single EV program stop을 entity-wide hard 4C로 과잉 확장하면 안 된다.

### C12_152_006_340930_YUILENERTECH_SKON_NOTCHING_LOSS_TRUE_NEGATIVE — 유일에너테크 (340930)

- event_date: `2022-04-06`
- entry_date: `2022-04-06` / entry_price: `19550.0`
- trigger_type: `4C`
- evidence_url: https://www.thelec.kr/news/articleView.html?idxno=16607
- profile_check: corporate_action candidates 2024/2026; entry~D180 unaffected; window_180D_corporate_action_contaminated=false
- evidence_summary: SK온 의존도가 매우 높은 장비사에서 노칭 장비 공급 지위가 흔들리고, 주요 물량을 경쟁사에 빼앗길 가능성이 확인됐다. 이것은 단순 EV tape 둔화가 아니라 고객/제품 지위 훼손이다.
- residual_error: hard 4C confirmation should trigger when customer share loss and order displacement are explicit.

### C12_152_007_006400_SAMSUNGSDI_INVENTORY_ADJUSTMENT_ESS_OFFSET — 삼성SDI (006400)

- event_date: `2025-01-24`
- entry_date: `2025-01-24` / entry_price: `226500.0`
- trigger_type: `Stage2`
- evidence_url: https://samsungsdi.co.kr/sdi-now/sdi-news/4222.html
- profile_check: corporate_action candidate dates are historical 1996/1998/2014 only; window_180D_corporate_action_contaminated=false
- evidence_summary: 4Q24 battery segment loss and customer inventory adjustment were explicit, but ESS record sales, US JV progress, OEM projects and multiple product offsets existed. Immediate hard 4C보다 staged entry + high-MAE guard가 맞았다.
- residual_error: negative customer inventory adjustment만 보면 90D MAE를 맞지만, offset 확인 후 D180 recovery를 놓치면 too-late/false-4C가 된다.


## 5. Trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_version":"e2r_v12_trigger_row_v1","case_id":"C12_152_001_396300_LGES_ENDPLATE_BACKLOG_HIGH_MAE","round":"R3","loop":152,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"LGES_ENDPLATE_BACKLOG_BUT_ORDER_TIMING_AND_MAE_GUARD","ticker":"396300","symbol_name":"세아메카닉스","event_date":"2024-06-27","entry_date":"2024-06-27","entry_price":3370.0,"trigger_type":"Stage2-Actionable","MFE_30D_pct":9.35,"MAE_30D_pct":-31.45,"MFE_90D_pct":20.92,"MAE_90D_pct":-31.45,"MFE_180D_pct":20.92,"MAE_180D_pct":-40.65,"peak_30D_date":"2024-07-18","trough_30D_date":"2024-08-05","peak_90D_date":"2024-10-10","trough_90D_date":"2024-08-05","peak_180D_date":"2024-10-10","trough_180D_date":"2024-12-10","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|396300|Stage2-Actionable|2024-06-27","evidence_url":"https://www.thelec.kr/news/articleView.html?idxno=28787","evidence_summary":"LG전자/LG에너지솔루션 관계, 자동차부품 수주잔고 5000억원, 올해 매출 목표 1000억~1200억원, 증설과 매출 인식 시점이 제시되었다. 그러나 가격경로는 30D 이후 급락과 180D -40%대 MAE를 보여, 계약/backlog 단어만으로 actionable을 유지하면 안 되는 사례다.","expected_alignment":"counterexample_with_4B_exit_guard","current_profile_error":"Stage2-Actionable bridge는 인정하지만 30D 이후 high-MAE exit guard가 늦다.","source_quality":"verified_or_direct_url","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"e2r_v12_trigger_row_v1","case_id":"C12_152_002_354320_ALMAC_EV_CHASM_RELIEF_POSITIVE","round":"R3","loop":152,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"EV_MODULE_CASE_CUSTOMER_CONCENTRATION_BUT_CAPITULATION_RELIEF","ticker":"354320","symbol_name":"알멕","event_date":"2024-12-17","entry_date":"2024-12-17","entry_price":23150.0,"trigger_type":"Stage2","MFE_30D_pct":33.26,"MAE_30D_pct":-3.46,"MFE_90D_pct":47.73,"MAE_90D_pct":-9.5,"MFE_180D_pct":47.73,"MAE_180D_pct":-9.5,"peak_30D_date":"2024-12-23","trough_30D_date":"2024-12-19","peak_90D_date":"2025-03-12","trough_90D_date":"2025-04-09","peak_180D_date":"2025-03-12","trough_180D_date":"2025-04-09","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|354320|Stage2|2024-12-17","evidence_url":"https://stock.pstatic.net/stock-research/company/74/20241217_company_744802000.pdf","evidence_summary":"EV 부품/배터리 모듈 케이스 고객 기반과 2024년 EV chasm에 따른 고객 투자 축소·발주 지연 리스크가 같이 드러난 상태였다. 이미 가격이 충분히 압축된 entry에서는 hard 4C보다 Stage2-Watch/relief guard가 더 맞았다.","expected_alignment":"positive_relief_after_contract_risk_reset","current_profile_error":"C12를 무조건 call-off negative로만 처리하면 90D/180D +47.7% relief path를 놓친다.","source_quality":"research_pdf_url","source_proxy_only":true,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"e2r_v12_trigger_row_v1","case_id":"C12_152_003_243840_SHINHEUNG_SDI_CHAIN_HIGH_MAE","round":"R3","loop":152,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SAMSUNG_SDI_SUPPLIER_DEMAND_CHAIN_AND_CUSTOMER_CALL_OFF_RISK","ticker":"243840","symbol_name":"신흥에스이씨","event_date":"2024-07-25","entry_date":"2024-07-25","entry_price":7600.0,"trigger_type":"Stage2","MFE_30D_pct":27.37,"MAE_30D_pct":-16.05,"MFE_90D_pct":27.37,"MAE_90D_pct":-35.53,"MFE_180D_pct":27.37,"MAE_180D_pct":-50.13,"peak_30D_date":"2024-08-13","trough_30D_date":"2024-08-05","peak_90D_date":"2024-08-13","trough_90D_date":"2024-12-06","peak_180D_date":"2024-08-13","trough_180D_date":"2025-04-09","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|243840|Stage2|2024-07-25","evidence_url":"https://stock.pstatic.net/stock-research/company/72/20240726_company_586478000.pdf","evidence_summary":"삼성SDI를 통한 전기차 배터리 수요 체인과 중대형 각형/원형 배터리 부품 노출이 존재했다. 단기 MFE는 있었으나 90D와 180D MAE가 크게 확대되어, 고객사 demand/call-off 확인 전 Stage2-Actionable로 끌어올리면 위험한 사례다.","expected_alignment":"counterexample_high_mae_after_short_mfe","current_profile_error":"customer exposure vocabulary는 bridge가 아니며, high-MAE guard가 필요하다.","source_quality":"research_pdf_url","source_proxy_only":true,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"e2r_v12_trigger_row_v1","case_id":"C12_152_004_051490_NARAMND_LGES_THEME_DERIVATIVE_HIGH_MAE","round":"R3","loop":152,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"LGES_LFP_CONTRACT_DERIVATIVE_PACK_SUPPLIER_THEME_ONLY","ticker":"051490","symbol_name":"나라엠앤디","event_date":"2024-07-03","entry_date":"2024-07-03","entry_price":4980.0,"trigger_type":"Stage2","MFE_30D_pct":14.26,"MAE_30D_pct":-24.5,"MFE_90D_pct":25.1,"MAE_90D_pct":-24.5,"MFE_180D_pct":25.1,"MAE_180D_pct":-33.73,"peak_30D_date":"2024-07-03","trough_30D_date":"2024-08-06","peak_90D_date":"2024-10-16","trough_90D_date":"2024-08-06","peak_180D_date":"2024-10-16","trough_180D_date":"2024-12-09","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|051490|Stage2|2024-07-03","evidence_url":"https://www.globalepic.co.kr/view.php?ud=20240703133449975abe7dc9896_29","evidence_summary":"LG에너지솔루션의 르노향 LFP 대형 수주 뉴스가 나라엠앤디 배터리팩 공급사 테마로 연결됐다. 그러나 회사 자체 call-off, 납품 schedule, margin bridge가 약했고 180D MAE가 -33%대로 커졌다.","expected_alignment":"counterexample_derivative_supplier_theme","current_profile_error":"고객사의 대형계약을 2차/3차 derivative supplier에 그대로 pass-through하면 false positive가 된다.","source_quality":"verified_or_direct_url","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"e2r_v12_trigger_row_v1","case_id":"C12_152_005_064960_SNTMOTIVE_GM_BOLT_STOP_OFFSET_FALSE_4C","round":"R3","loop":152,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"EV_PROGRAM_STOP_BUT_HEV_OIL_PUMP_OFFSET","ticker":"064960","symbol_name":"SNT모티브","event_date":"2024-04-02","entry_date":"2024-04-02","entry_price":44650.0,"trigger_type":"4C","MFE_30D_pct":5.71,"MAE_30D_pct":-1.01,"MFE_90D_pct":12.65,"MAE_90D_pct":-11.65,"MFE_180D_pct":12.65,"MAE_180D_pct":-12.32,"peak_30D_date":"2024-05-16","trough_30D_date":"2024-04-08","peak_90D_date":"2024-06-28","trough_90D_date":"2024-08-07","peak_180D_date":"2024-06-28","trough_180D_date":"2024-12-12","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|064960|4C|2024-04-02","evidence_url":"https://www.dailyinvest.kr/news/articleView.html?idxno=57958","evidence_summary":"GM Bolt향 모터 공급 중단으로 EV program cliff가 발생했지만, HEV/오일펌프/방산 등 offset이 있어 hard 4C로 바로 보내면 과잉반응이 된다. 180D MAE는 제한적이고 MFE도 완만했다.","expected_alignment":"false_4C_due_to_offset","current_profile_error":"single EV program stop을 entity-wide hard 4C로 과잉 확장하면 안 된다.","source_quality":"verified_or_direct_url","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"e2r_v12_trigger_row_v1","case_id":"C12_152_006_340930_YUILENERTECH_SKON_NOTCHING_LOSS_TRUE_NEGATIVE","round":"R3","loop":152,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SINGLE_CUSTOMER_SKON_EQUIPMENT_SHARE_LOSS_TRUE_THESIS_BREAK","ticker":"340930","symbol_name":"유일에너테크","event_date":"2022-04-06","entry_date":"2022-04-06","entry_price":19550.0,"trigger_type":"4C","MFE_30D_pct":8.44,"MAE_30D_pct":-19.95,"MFE_90D_pct":8.44,"MAE_90D_pct":-37.6,"MFE_180D_pct":20.46,"MAE_180D_pct":-37.6,"peak_30D_date":"2022-04-21","trough_30D_date":"2022-05-13","peak_90D_date":"2022-04-21","trough_90D_date":"2022-07-04","peak_180D_date":"2022-12-02","trough_180D_date":"2022-07-04","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|340930|4C|2022-04-06","evidence_url":"https://www.thelec.kr/news/articleView.html?idxno=16607","evidence_summary":"SK온 의존도가 매우 높은 장비사에서 노칭 장비 공급 지위가 흔들리고, 주요 물량을 경쟁사에 빼앗길 가능성이 확인됐다. 이것은 단순 EV tape 둔화가 아니라 고객/제품 지위 훼손이다.","expected_alignment":"true_negative_customer_loss","current_profile_error":"hard 4C confirmation should trigger when customer share loss and order displacement are explicit.","source_quality":"verified_or_direct_url","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"e2r_v12_trigger_row_v1","case_id":"C12_152_007_006400_SAMSUNGSDI_INVENTORY_ADJUSTMENT_ESS_OFFSET","round":"R3","loop":152,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_INVENTORY_ADJUSTMENT_BUT_ESS_AND_US_JV_OFFSET","ticker":"006400","symbol_name":"삼성SDI","event_date":"2025-01-24","entry_date":"2025-01-24","entry_price":226500.0,"trigger_type":"Stage2","MFE_30D_pct":9.71,"MAE_30D_pct":-11.7,"MFE_90D_pct":9.71,"MAE_90D_pct":-30.38,"MFE_180D_pct":30.91,"MAE_180D_pct":-30.38,"peak_30D_date":"2025-02-24","trough_30D_date":"2025-02-10","peak_90D_date":"2025-02-24","trough_90D_date":"2025-05-22","peak_180D_date":"2025-10-24","trough_180D_date":"2025-05-22","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","window_30D_corporate_action_contaminated":false,"window_90D_corporate_action_contaminated":false,"window_180D_corporate_action_contaminated":false,"calibration_usable":true,"dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|006400|Stage2|2025-01-24","evidence_url":"https://samsungsdi.co.kr/sdi-now/sdi-news/4222.html","evidence_summary":"4Q24 battery segment loss and customer inventory adjustment were explicit, but ESS record sales, US JV progress, OEM projects and multiple product offsets existed. Immediate hard 4C보다 staged entry + high-MAE guard가 맞았다.","expected_alignment":"positive_after_high_mae_staged_entry","current_profile_error":"negative customer inventory adjustment만 보면 90D MAE를 맞지만, offset 확인 후 D180 recovery를 놓치면 too-late/false-4C가 된다.","source_quality":"verified_or_direct_url","source_proxy_only":false,"evidence_url_pending":false}
```

## 6. Score simulation rows JSONL

These are shadow simulations only. They are not production scoring changes.

```jsonl
{"row_type":"score_simulation","case_id":"C12_152_001_396300_LGES_ENDPLATE_BACKLOG_HIGH_MAE","ticker":"396300","component_score_breakdown_raw":{"eps_fcf_explosion":45,"visibility":48,"bottleneck_pricing":38,"mispricing":46,"valuation_rerating":42,"capital_allocation":35,"information_confidence":68},"current_profile_proxy_stage_before_shadow_rule":"Stage2-Actionable","shadow_rule_adjusted_stage":"Stage2","rule_effect":"require_calloff_visibility_and_offset_confirmation_before_actionable_or_4c","do_not_apply_now":true}
{"row_type":"score_simulation","case_id":"C12_152_002_354320_ALMAC_EV_CHASM_RELIEF_POSITIVE","ticker":"354320","component_score_breakdown_raw":{"eps_fcf_explosion":62,"visibility":66,"bottleneck_pricing":58,"mispricing":60,"valuation_rerating":50,"capital_allocation":46,"information_confidence":72},"current_profile_proxy_stage_before_shadow_rule":"Stage2","shadow_rule_adjusted_stage":"Stage2_Actionable_after_reset","rule_effect":"require_calloff_visibility_and_offset_confirmation_before_actionable_or_4c","do_not_apply_now":true}
{"row_type":"score_simulation","case_id":"C12_152_003_243840_SHINHEUNG_SDI_CHAIN_HIGH_MAE","ticker":"243840","component_score_breakdown_raw":{"eps_fcf_explosion":45,"visibility":48,"bottleneck_pricing":38,"mispricing":46,"valuation_rerating":42,"capital_allocation":35,"information_confidence":68},"current_profile_proxy_stage_before_shadow_rule":"Stage2-Actionable","shadow_rule_adjusted_stage":"Stage2","rule_effect":"require_calloff_visibility_and_offset_confirmation_before_actionable_or_4c","do_not_apply_now":true}
{"row_type":"score_simulation","case_id":"C12_152_004_051490_NARAMND_LGES_THEME_DERIVATIVE_HIGH_MAE","ticker":"051490","component_score_breakdown_raw":{"eps_fcf_explosion":45,"visibility":48,"bottleneck_pricing":38,"mispricing":46,"valuation_rerating":42,"capital_allocation":35,"information_confidence":68},"current_profile_proxy_stage_before_shadow_rule":"Stage2-Actionable","shadow_rule_adjusted_stage":"Stage2","rule_effect":"require_calloff_visibility_and_offset_confirmation_before_actionable_or_4c","do_not_apply_now":true}
{"row_type":"score_simulation","case_id":"C12_152_005_064960_SNTMOTIVE_GM_BOLT_STOP_OFFSET_FALSE_4C","ticker":"064960","component_score_breakdown_raw":{"eps_fcf_explosion":58,"visibility":62,"bottleneck_pricing":52,"mispricing":56,"valuation_rerating":48,"capital_allocation":55,"information_confidence":74},"current_profile_proxy_stage_before_shadow_rule":"4C","shadow_rule_adjusted_stage":"Stage2_offset_watch","rule_effect":"require_calloff_visibility_and_offset_confirmation_before_actionable_or_4c","do_not_apply_now":true}
{"row_type":"score_simulation","case_id":"C12_152_006_340930_YUILENERTECH_SKON_NOTCHING_LOSS_TRUE_NEGATIVE","ticker":"340930","component_score_breakdown_raw":{"eps_fcf_explosion":45,"visibility":48,"bottleneck_pricing":38,"mispricing":46,"valuation_rerating":42,"capital_allocation":35,"information_confidence":68},"current_profile_proxy_stage_before_shadow_rule":"4C","shadow_rule_adjusted_stage":"4C","rule_effect":"require_calloff_visibility_and_offset_confirmation_before_actionable_or_4c","do_not_apply_now":true}
{"row_type":"score_simulation","case_id":"C12_152_007_006400_SAMSUNGSDI_INVENTORY_ADJUSTMENT_ESS_OFFSET","ticker":"006400","component_score_breakdown_raw":{"eps_fcf_explosion":60,"visibility":64,"bottleneck_pricing":54,"mispricing":58,"valuation_rerating":50,"capital_allocation":48,"information_confidence":78},"current_profile_proxy_stage_before_shadow_rule":"4C_or_Stage2","shadow_rule_adjusted_stage":"Stage2_with_4B_exit_guard","rule_effect":"require_calloff_visibility_and_offset_confirmation_before_actionable_or_4c","do_not_apply_now":true}
```

## 7. Aggregate / shadow / residual rows JSONL

```jsonl
{"row_type":"aggregate","round":"R3","loop":152,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":7,"usable_trigger_row_count":7,"representative_trigger_count":7,"positive_case_count":3,"counterexample_count":4,"stage4b_watch_or_overlay_count":5,"stage4c_or_false4c_count":3,"current_profile_error_count":5,"avg_MFE_90D_pct":21.7,"avg_MAE_90D_pct":-25.8,"avg_MFE_180D_pct":26.45,"avg_MAE_180D_pct":-30.62}
{"row_type":"shadow_weight","axis":"C12_CUSTOMER_CALLOFF_OFFSET_VISIBILITY_AND_EXIT_GATE_V2","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","proposed_rule":"Stage2-Actionable requires named customer + call-off visibility + revenue timing or margin/revision bridge. Hard 4C requires confirmed customer share loss, contract cancellation, or utilization collapse; broad EV chasm vocabulary alone should remain Stage2/4B watch when ESS/HEV/geography/customer offset exists.","shadow_weight_only":true,"production_scoring_changed":false,"do_not_propose_global_delta":true}
{"row_type":"residual_contribution","new_axis_proposed":"c12_calloff_visibility_offset_and_exit_guard_v2","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","hard_4c_confirmation"],"existing_axis_weakened":["hard_4c_should_not_fire_on_single_program_stop_when_offset_is_material"],"residual_error_types":["derivative_customer_contract_false_positive","single_customer_share_loss_true_4c","relief_after_chasm_reset_missed_positive","high_mae_after_contract_backlog"],"coding_agent_handoff_priority":"medium"}
```

## 8. Interpretation

C12의 핵심 오차는 두 갈래다.

첫째, 고객사 계약 또는 대형 수주가 존재해도 실제 call-off, revenue timing, margin bridge가 없으면 supplier derivative theme이 된다. 나라엠앤디와 세아메카닉스는 고객사 또는 관계사 단위 수주/잔고 headline이 있었지만, 자체 납품 확인과 90D/180D exit guard가 약하면 high-MAE가 먼저 나온다. 신흥에스이씨도 삼성SDI 수요 chain만으로는 actionable bridge가 부족했다.

둘째, EV program stop 또는 고객 재고조정이라는 부정 단어가 있어도 entity-wide hard 4C로 바로 보내면 틀릴 수 있다. SNT모티브는 GM Bolt향 motor cliff가 있었지만 HEV/oil-pump/방산 offset이 있었다. 삼성SDI는 4Q24 battery segment loss와 customer inventory adjustment가 뚜렷했지만 ESS, 미주 JV, OEM 프로젝트 offset이 있어 D180 회복이 가능했다.

유일에너테크는 반대로 진짜 hard 4C에 가깝다. 단일 고객 의존도가 높고, 핵심 장비 지위 상실 또는 수주 share loss가 확인되면 단순 sector slowdown이 아니라 thesis break다.

## 9. Proposed shadow rule

```text
rule_id = C12_CUSTOMER_CALLOFF_OFFSET_VISIBILITY_AND_EXIT_GATE_V2
scope = canonical_archetype_specific
production_scoring_changed = false
shadow_weight_only = true
```

Proposed logic:

```text
Stage2-Actionable positive gate:
  require named customer + one of:
    - explicit call-off / PO / shipment / delivery schedule
    - revenue-recognition timing
    - margin or revision bridge
    - customer diversification that reduces single-customer risk

Derivative supplier block:
  if evidence is only customer-of-customer mega contract or theme linkage:
    cap at Stage2
    add local 4B/high-MAE watch when price already spiked

Hard 4C confirmation:
  allow 4C only if one of:
    - contract cancellation / material volume reduction
    - confirmed customer share loss
    - utilization collapse without offset
    - customer inventory adjustment plus no ESS/HEV/geography/product offset

False 4C offset guard:
  if EV program stop exists but offset is material:
    route to Stage2 or 4B-watch, not hard 4C
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent. Do not use this single MD as a standalone production patch. Batch it together with other v12 research files and run the existing v12 calibration ingestion. If this MD validates, evaluate a canonical-specific shadow patch named C12_CUSTOMER_CALLOFF_OFFSET_VISIBILITY_AND_EXIT_GATE_V2.

Required parser checks:
- every trigger row has entry_date, entry_price, trigger_type, 30/90/180D MFE/MAE
- price_data_source == Songdaiki/stock-web
- price_basis == tradable_raw
- price_adjustment_status == raw_unadjusted_marcap
- canonical_archetype_id == C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
- large_sector_id == L3_BATTERY_EV_GREEN_MOBILITY
- dedupe by canonical_archetype_id + ticker + trigger_type + entry_date

Patch candidate, if supported by batch evidence:
- add C12-specific Stage2-Actionable bridge requiring call-off/revenue timing/margin confirmation
- add derivative supplier block for customer-of-customer mega-contract pass-through
- add false-4C offset guard when EV program stop is offset by ESS/HEV/geography/product/customer diversification
- keep hard 4C only for explicit customer share loss, contract reduction, cancellation, or utilization collapse without offset
```

## 11. Next research state

```text
completed_round = R3
completed_loop = 152
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|C05_EPC_MEGA_CONTRACT_MARGIN_GAP|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|C27_CONTENT_IP_GLOBAL_MONETIZATION
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
```

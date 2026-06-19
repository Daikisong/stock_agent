---
title: E2R Stock-Web v12 Residual Research — R2 C08 Semi Test Socket Customer Quality
output_filename: e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
selected_round: R2
selected_loop: 131
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C08 URL/proxy quality repair, 4C-thin path, customer-quality/repeat-demand bridge split
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
must_use_actual_stock_web_1D_OHLC: true
must_include_complete_30_90_180_mfe_mae_in_every_trigger_row: true
trigger_rows_missing_required_price_fields_are_forbidden: true
created_at_kst: 2026-06-15
---

# E2R Stock-Web v12 Residual Research — R2 / C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY

## 1. Executive Summary

이번 연구는 **C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY**의 잔여 오류를 보강한다. C08은 이미 row 수가 부족한 구역이 아니라, 직접 URL과 proxy-only row 품질, 그리고 4B/4C taxonomy가 얇은 구역이다. No-Repeat 장부상 C08은 `235 rows / 63 symbols / positives-counter 39·51 / 4B·4C 35·2 / weights 22/21/16/14/12/6/9`로 잡혀 있으므로, 이번 loop는 단순 row 적립이 아니라 **test socket 노출**과 **고객 품질·반복 수요·current revenue bridge**를 분리하는 품질 보강으로 수행했다.

핵심 결론은 다음과 같다.

```text
new_axis_proposed: C08_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_GATE
sector_specific_rule_candidate: L2 semi-test-socket 계열에서는 제품 노출/테마만으로 Stage2-Actionable 또는 Green을 열지 않고, named customer 또는 고객군 품질, repeat demand, R&D/양산 socket order, current revenue/OP bridge 중 최소 2개 이상을 요구한다.
canonical_archetype_rule_candidate: C08은 소켓이 소모품이라는 구조적 장점이 있지만, small-cap proxy row는 customer/order/revenue bridge가 없으면 4B watch cap; 영업이익 붕괴·고객 capex cut·CB/BW/이자보상 break가 동시에 나오면 4C.
```

### Run Counts

```text
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 3
counterexample_count: 3
stage4b_case_count: 2
stage4c_case_count: 1
source_proxy_only_count: 3
evidence_url_pending_count: 0
rows_missing_required_mfe_mae: 0
current_profile_error_count: 5
```

## 2. Selection / No-Repeat Check

직전 산출물 묶음은 C05, C01, C13, C15, C10, C02, C16, R13, C17, C07, C06, C14, C11, C12, C09, C03, C04를 이미 사용했다. 이번에는 같은 symbol/date/trigger family 반복을 피하고, 아직 이번 묶음에서 다루지 않은 C08로 이동했다.

| check | result |
|---|---|
| selected_round | R2 |
| selected_loop | 131 |
| selected_archetype | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY |
| loop_basis | docs/round root에서 C08 표준 파일의 최대 loop가 R2 loop 130으로 확인되어 +1 |
| duplicate check | no same symbol + trigger_type + entry_date within this generated session |
| novelty check | 6 symbols / 6 trigger families / positive+counter balanced |

## 3. Price Source Validation

Stock-Web manifest 기준 가격원은 `FinanceData/marcap` 변환 shard이고, 기본 calibration shard는 `atlas/ohlcv_tradable_by_symbol_year`, 가격 기준은 `tradable_raw`, 조정 상태는 `raw_unadjusted_marcap`, manifest `max_date`는 `2026-02-20`이다. 모든 usable row는 entry 이후 180 trading-row window가 manifest max_date 안에 존재하고, corporate-action candidate date가 entry~D+180 안에 겹치지 않는다.

| item | value |
|---|---|
| source_repo | Songdaiki/stock-web |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| stock_web_manifest_max_date | 2026-02-20 |
| MFE/MAE rule | entry close 대비 entry-inclusive forward N trading rows의 max high / min low |

## 4. Case Grid

| symbol | company | trigger_date | entry_date | trigger_type | role | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | DD_after_peak | proxy_only |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 095340 | ISC | 2025-02-11 | 2025-02-12 | Stage4B | counterexample | 7.33 | -21.44 | 7.33 | -41.93 | 15.33 | -41.93 | 2025-10-16 | -18.0 | N |
| 058470 | LEENO Industrial | 2025-05-15 | 2025-05-16 | Stage3-Yellow | positive | 30.52 | -4.84 | 37.72 | -4.84 | 183.62 | -4.84 | 2026-01-30 | -21.08 | Y |
| 131290 | TSE | 2021-02-24 | 2021-02-25 | Stage2-Actionable | positive | 14.39 | -19.42 | 22.3 | -19.42 | 44.78 | -19.42 | 2021-08-10 | -36.02 | N |
| 425420 | TFE | 2023-12-22 | 2023-12-26 | Stage4B | counterexample | 9.17 | -17.47 | 27.95 | -17.47 | 27.95 | -57.82 | 2024-03-21 | -67.03 | Y |
| 098120 | Micro Contact Solution | 2024-12-03 | 2024-12-04 | Stage2-Actionable | positive | 39.39 | -7.11 | 158.21 | -7.11 | 435.01 | -7.11 | 2025-07-31 | -36.61 | Y |
| 080580 | O Kins Electronics | 2024-04-02 | 2024-04-03 | Stage4C | counterexample | 6.16 | -25.3 | 6.16 | -46.48 | 6.16 | -59.46 | 2024-04-03 | -61.81 | N |

## 5. Case Notes


### 5.1. ISC (095340) — Stage4B / counterexample

- **Trigger / entry:** 2025-02-11 → 2025-02-12 close 73,700
- **Evidence family:** `parent_official_operating_result_test_socket_rebound`
- **Evidence summary:** SKC 공식 뉴스는 2024년 ISC가 test socket investee로서 매출 +25%, 영업이익 +320% YoY를 기록했다고 밝혔다. 동시에 ISC/SEMI booth는 IC chip testing socket total solution provider 성격을 확인한다. 그러나 entry 이후 90D MAE가 -41.93%로, direct evidence만으로 Green을 여는 것은 과했다.
- **Path:** 30D MFE/MAE 7.33% / -21.44%, 90D 7.33% / -41.93%, 180D 15.33% / -41.93%; peak 2025-10-16 15.33%, drawdown-after-peak -18.0%.
- **Source URLs:** https://www.skc.kr/m/eng/Conmmunication/news/newsDetail.do?seq=1625; https://isc21.kr/; https://expo.semi.org/korea2025/Public/eBooth.aspx?BoothID=595300&IndexInList=213&ListByBooth=true&Nav=False
- **Profile interpretation:** `false_positive_or_too_early_green_risk`


### 5.2. LEENO Industrial (058470) — Stage3-Yellow / positive

- **Trigger / entry:** 2025-05-15 → 2025-05-16 close 40,300
- **Evidence family:** `earnings_beat_rd_socket_order_and_customer_recovery`
- **Evidence summary:** 2025년 1Q 매출 784억원, 영업이익 349억원, OPM 44.6%와 신규 R&D socket 주문·주요 고객사 매출 개선이 동시에 확인됐다. 180D MFE가 +183.62%, MAE가 -4.84%로 C08의 clean positive 표본이다.
- **Path:** 30D MFE/MAE 30.52% / -4.84%, 90D 37.72% / -4.84%, 180D 183.62% / -4.84%; peak 2026-01-30 183.62%, drawdown-after-peak -21.08%.
- **Source URLs:** https://www.globalepic.co.kr/view.php?ud=2025051510502735245ebfd494dd_29
- **Profile interpretation:** `none_or_current_profile_too_slow_if_waiting_for_official_ir_only`


### 5.3. TSE (131290) — Stage2-Actionable / positive

- **Trigger / entry:** 2021-02-24 → 2021-02-25 close 55,600
- **Evidence family:** `named_hbm_die_carrier_socket_supply`
- **Evidence summary:** The Elec는 TSE가 HBM2/HBM3용 die carrier socket을 공급한다고 보도했고, 고객이 기존 tester/handler/burn-in 장비를 활용할 수 있다는 제품-고객 효용을 제시했다. 180D MFE +44.78%이지만 30D MAE -19.42%라 drawdown-aware confirmation이 필요하다.
- **Path:** 30D MFE/MAE 14.39% / -19.42%, 90D 22.3% / -19.42%, 180D 44.78% / -19.42%; peak 2021-08-10 44.78%, drawdown-after-peak -36.02%.
- **Source URLs:** https://www.thelec.net/news/articleView.html?idxno=2419
- **Profile interpretation:** `stage2_valid_but_green_should_wait_until_mae_absorbed`


### 5.4. TFE (425420) — Stage4B / counterexample

- **Trigger / entry:** 2023-12-22 → 2023-12-26 close 34,350
- **Evidence family:** `package_test_total_solution_hbm_ddr5_proxy`
- **Evidence summary:** IBK 자료는 TFE를 패키지 테스트 부품 토탈 솔루션 업체로 설명하고 DDR5/HBM 신제품 효과를 제시했다. 그러나 named customer/order/revenue bridge 없이 180D MAE -57.82%와 peak 이후 -67.03% drawdown이 발생해 4B cap이 필요하다.
- **Path:** 30D MFE/MAE 9.17% / -17.47%, 90D 27.95% / -17.47%, 180D 27.95% / -57.82%; peak 2024-03-21 27.95%, drawdown-after-peak -67.03%.
- **Source URLs:** https://file.alphasquare.co.kr/media/pdfs/company-report/IBK20231222%ED%8B%B0%EC%97%90%ED%94%84%EC%9D%B4.pdf
- **Profile interpretation:** `source_proxy_only_false_positive`


### 5.5. Micro Contact Solution (098120) — Stage2-Actionable / positive

- **Trigger / entry:** 2024-12-03 → 2024-12-04 close 4,570
- **Evidence family:** `samsung_burnin_socket_demand_recovery_hbm_proxy`
- **Evidence summary:** KIRS/DailyInvest 계열 자료는 삼성전자향 burn-in socket demand recovery와 HBM capex 관련 기대를 제시했다. 180D MFE +435.01%, MAE -7.11%로 가격경로는 매우 강하지만, 공식 customer/order bridge가 약하므로 promotion에는 source-quality cap을 둔다.
- **Path:** 30D MFE/MAE 39.39% / -7.11%, 90D 158.21% / -7.11%, 180D 435.01% / -7.11%; peak 2025-07-31 435.01%, drawdown-after-peak -36.61%.
- **Source URLs:** https://w4.kirs.or.kr/download/research/241203_%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%BB%A8%ED%85%8D%EC%86%94.pdf; https://www.dailyinvest.kr/news/articleView.html?idxno=62248
- **Profile interpretation:** `current_profile_may_underweight_tiny_socket_winner_but_source_quality_blocks_green`


### 5.6. O Kins Electronics (080580) — Stage4C / counterexample

- **Trigger / entry:** 2024-04-02 → 2024-04-03 close 9,090
- **Evidence family:** `operating_profit_collapse_customer_investment_cut`
- **Evidence summary:** IB토마토는 2023년 영업이익 85.7% 감소, 주요 고객사 투자 축소, 소켓 관련 매출 감소, 이자보상배율 1 미만, CB/BW 부담을 보도했다. CXL/DDR5 narrative가 있어도 180D MAE -59.46%로 hard 4C 보호가 맞다.
- **Path:** 30D MFE/MAE 6.16% / -25.3%, 90D 6.16% / -46.48%, 180D 6.16% / -59.46%; peak 2024-04-03 6.16%, drawdown-after-peak -61.81%.
- **Source URLs:** https://www.ibtomato.com/ExternalView.aspx?no=11875&type=1
- **Profile interpretation:** `hard_4c_correct_or_should_trigger_earlier`


## 6. Residual Pattern Analysis

C08의 어려움은 소켓이 본질적으로 **소모품/품질/반복수요** business인 동시에, 주식시장에서는 너무 쉽게 “HBM·DDR5·CXL·AI test socket”이라는 작은 단어 하나로 가격이 먼저 폭발한다는 점이다. 이때 E2R이 분리해야 할 것은 다음 세 가지다.

1. **Clean customer-quality winner:** LEENO처럼 R&D socket order, 주요 고객사 매출 개선, 영업이익률, 180D 가격경로가 같이 선다.
2. **Structural but drawdown-heavy winner:** TSE처럼 HBM die-carrier socket이라는 named product/customer utility가 있으나, 초기 MAE가 커서 Stage3-Green은 지연 확인이 필요하다.
3. **Proxy-only blowoff / hard break:** TFE, MCS, O’Kins처럼 제품 노출은 맞지만 direct customer/order/current revenue bridge가 약하거나, 영업이익·현금흐름·고객 capex가 깨진다. MCS는 price path가 매우 강해 positive support로 남기되, 공식 customer/order source가 없으면 promotion에는 cap을 둔다.

## 7. Positive vs Counterexample Balance

| bucket | cases | interpretation |
|---|---:|---|
| clean positive | 1 | LEENO: earnings + R&D socket order + customer revenue recovery + shallow MAE |
| positive but confirmation needed | 2 | TSE: HBM socket direct product but early MAE; MCS: enormous path but proxy-only source cap |
| 4B watch | 2 | ISC: direct evidence but very deep MAE; TFE: package-test proxy blowoff then collapse |
| hard 4C | 1 | O’Kins: customer capex cut + OP collapse + debt/CB/BW pressure |

## 8. Proposed Shadow Gate

```text
C08_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_GATE:
  raise_visibility_credit_if:
    - named customer or credible customer group is present
    - R&D socket / mass-production socket repeat demand is dated
    - current-quarter revenue or OP bridge is visible
    - product is explicitly socket/probe/pin/burn-in/test-socket, not broad HBM equipment only
  cap_at_watch_or_stage2_if:
    - only HBM/DDR5/CXL/AI theme vocabulary is present
    - source is broker/report/news proxy only and no official customer/order/revenue bridge is present
    - valuation/price extension is already extreme before trigger
  route_to_4c_if:
    - customer capex cut and socket revenue decline are explicit
    - operating profit collapses or interest coverage/CB/BW burden breaks financial quality
    - thesis depends on future product mix while current cash/OP bridge is broken
```

## 9. Shadow Weight Candidate

| component | before | after | delta | reason |
|---|---:|---:|---:|---|
| EPS/FCF | 22 | 22 | 0 | keep earnings evidence important |
| Visibility | 21 | 23 | +2 | customer/repeat-demand bridge should matter more |
| Bottleneck/Pricing | 16 | 15 | -1 | socket product exposure alone is not enough |
| Mispricing | 14 | 12 | -2 | small-cap socket proxy can overheat quickly |
| Valuation | 12 | 11 | -1 | late blowoff needs cap |
| Capital allocation | 6 | 6 | 0 | limited change |
| Info confidence / risk | 9 | 11 | +2 | proxy-only and financial-quality breaks need stronger penalty |

```text
suggested_shadow_weight_delta:
  before: 22/21/16/14/12/6/9
  after:  22/23/15/12/11/6/11
  delta:  0/+2/-1/-2/-1/0/+2
production_scoring_changed: false
shadow_weight_only: true
```

## 10. Current Calibrated Profile Stress Test

Current `e2r_2_2_rolling_calibrated`는 이미 Stage2 bridge와 local 4B guard를 갖고 있으나, C08에서는 아래 잔여 오류가 남는다.

- **Too-early positive:** ISC처럼 direct evidence가 좋아도 entry 위치가 비싸고 고객/order/revenue bridge가 이미 가격에 반영되면 90D MAE가 -40%대까지 열린다.
- **Proxy-only positive ambiguity:** MCS처럼 source quality는 약하지만 가격경로가 매우 좋은 row가 있다. 이런 row는 rule discovery에는 가치가 있지만 promotion support에는 direct URL/customer/order 보강이 필요하다.
- **Hard 4C clarity:** O’Kins처럼 소켓 narrative가 살아 있어도 고객 투자축소·영업이익 collapse·이자보상/CB burden이 같이 오면 C08 positive가 아니라 4C다.

## 11. Batch-Ingest Self Audit

| hard gate | result |
|---|---|
| standard v12 filename | pass |
| selected_round/filename round match | pass |
| selected_loop/filename loop match | pass |
| large_sector/canonical mapping | pass: C08 → R2/L2 |
| trigger_type canonical stage label only | pass |
| all usable triggers include MFE_30D/MFE_90D/MFE_180D and MAE_30D/MAE_90D/MAE_180D | pass |
| price source is Stock-Web tradable_raw | pass |
| corporate-action overlap in D+180 | none |
| production scoring changed | false |
| handoff prompt embedded but not executed | pass |

## 12. Machine-Readable Rows

### 12.x price_source_validation_jsonl

```jsonl
{"row_type":"price_source_validation","case_id":"C08_095340_20250211_ISC_PARENT_RESULTS_HIGH_MAE","symbol":"095340","profile_checked":true,"available_years_used":[2025],"profile_last_date_assumed":"2026-02-20 or symbol-specific latest within downloaded shards","entry_date":"2025-02-12","D180_last_window_date":"2025-11-07","corporate_action_candidate_dates":["2014-12-26","2023-10-20"],"corporate_action_overlap_180D":false,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true}
{"row_type":"price_source_validation","case_id":"C08_058470_20250515_LEENO_Q1_RD_SOCKET_ORDER","symbol":"058470","profile_checked":true,"available_years_used":[2025,2026],"profile_last_date_assumed":"2026-02-20 or symbol-specific latest within downloaded shards","entry_date":"2025-05-16","D180_last_window_date":"2026-02-09","corporate_action_candidate_dates":["2013-06-13","2013-07-08","2025-04-25"],"corporate_action_overlap_180D":false,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true}
{"row_type":"price_source_validation","case_id":"C08_131290_20210224_TSE_HBM_DIE_CARRIER_SOCKET","symbol":"131290","profile_checked":true,"available_years_used":[2021],"profile_last_date_assumed":"2026-02-20 or symbol-specific latest within downloaded shards","entry_date":"2021-02-25","D180_last_window_date":"2021-11-17","corporate_action_candidate_dates":["2011-04-05","2011-04-28"],"corporate_action_overlap_180D":false,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true}
{"row_type":"price_source_validation","case_id":"C08_425420_20231222_TFE_PACKAGE_TEST_PROXY_BLOWOFF","symbol":"425420","profile_checked":true,"available_years_used":[2023,2024],"profile_last_date_assumed":"2026-02-20 or symbol-specific latest within downloaded shards","entry_date":"2023-12-26","D180_last_window_date":"2024-09-23","corporate_action_candidate_dates":[],"corporate_action_overlap_180D":false,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true}
{"row_type":"price_source_validation","case_id":"C08_098120_20241203_MCS_BURNIN_SOCKET_DEMAND_RECOVERY","symbol":"098120","profile_checked":true,"available_years_used":[2024,2025],"profile_last_date_assumed":"2026-02-20 or symbol-specific latest within downloaded shards","entry_date":"2024-12-04","D180_last_window_date":"2025-09-02","corporate_action_candidate_dates":["2011-04-19","2011-05-17"],"corporate_action_overlap_180D":false,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true}
{"row_type":"price_source_validation","case_id":"C08_080580_20240402_OKINS_OP_COLLAPSE_CUSTOMER_CAPEX_CUT","symbol":"080580","profile_checked":true,"available_years_used":[2024],"profile_last_date_assumed":"2026-02-20 or symbol-specific latest within downloaded shards","entry_date":"2024-04-03","D180_last_window_date":"2024-12-30","corporate_action_candidate_dates":["2021-01-07","2021-01-29"],"corporate_action_overlap_180D":false,"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true}
```

### 12.x case_jsonl

```jsonl
{"row_type":"case","case_id":"C08_095340_20250211_ISC_PARENT_RESULTS_HIGH_MAE","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY","symbol":"095340","company":"ISC","trigger_date":"2025-02-11","entry_date":"2025-02-12","case_role":"counterexample","evidence_family":"parent_official_operating_result_test_socket_rebound","source_proxy_only":false,"evidence_url_pending":false,"calibration_usable":true,"representative_for_aggregate":true,"novelty_claim":"new symbol/date/trigger-family within current session and not same as recent generated C05/C01/C13/C15/C10/C02/C16/R13/C17/C07/C06/C14/C11/C12/C09/C03/C04 files"}
{"row_type":"case","case_id":"C08_058470_20250515_LEENO_Q1_RD_SOCKET_ORDER","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY","symbol":"058470","company":"LEENO Industrial","trigger_date":"2025-05-15","entry_date":"2025-05-16","case_role":"positive","evidence_family":"earnings_beat_rd_socket_order_and_customer_recovery","source_proxy_only":true,"evidence_url_pending":false,"calibration_usable":true,"representative_for_aggregate":true,"novelty_claim":"new symbol/date/trigger-family within current session and not same as recent generated C05/C01/C13/C15/C10/C02/C16/R13/C17/C07/C06/C14/C11/C12/C09/C03/C04 files"}
{"row_type":"case","case_id":"C08_131290_20210224_TSE_HBM_DIE_CARRIER_SOCKET","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY","symbol":"131290","company":"TSE","trigger_date":"2021-02-24","entry_date":"2021-02-25","case_role":"positive","evidence_family":"named_hbm_die_carrier_socket_supply","source_proxy_only":false,"evidence_url_pending":false,"calibration_usable":true,"representative_for_aggregate":true,"novelty_claim":"new symbol/date/trigger-family within current session and not same as recent generated C05/C01/C13/C15/C10/C02/C16/R13/C17/C07/C06/C14/C11/C12/C09/C03/C04 files"}
{"row_type":"case","case_id":"C08_425420_20231222_TFE_PACKAGE_TEST_PROXY_BLOWOFF","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY","symbol":"425420","company":"TFE","trigger_date":"2023-12-22","entry_date":"2023-12-26","case_role":"counterexample","evidence_family":"package_test_total_solution_hbm_ddr5_proxy","source_proxy_only":true,"evidence_url_pending":false,"calibration_usable":true,"representative_for_aggregate":true,"novelty_claim":"new symbol/date/trigger-family within current session and not same as recent generated C05/C01/C13/C15/C10/C02/C16/R13/C17/C07/C06/C14/C11/C12/C09/C03/C04 files"}
{"row_type":"case","case_id":"C08_098120_20241203_MCS_BURNIN_SOCKET_DEMAND_RECOVERY","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY","symbol":"098120","company":"Micro Contact Solution","trigger_date":"2024-12-03","entry_date":"2024-12-04","case_role":"positive","evidence_family":"samsung_burnin_socket_demand_recovery_hbm_proxy","source_proxy_only":true,"evidence_url_pending":false,"calibration_usable":true,"representative_for_aggregate":true,"novelty_claim":"new symbol/date/trigger-family within current session and not same as recent generated C05/C01/C13/C15/C10/C02/C16/R13/C17/C07/C06/C14/C11/C12/C09/C03/C04 files"}
{"row_type":"case","case_id":"C08_080580_20240402_OKINS_OP_COLLAPSE_CUSTOMER_CAPEX_CUT","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY","symbol":"080580","company":"O Kins Electronics","trigger_date":"2024-04-02","entry_date":"2024-04-03","case_role":"counterexample","evidence_family":"operating_profit_collapse_customer_investment_cut","source_proxy_only":false,"evidence_url_pending":false,"calibration_usable":true,"representative_for_aggregate":true,"novelty_claim":"new symbol/date/trigger-family within current session and not same as recent generated C05/C01/C13/C15/C10/C02/C16/R13/C17/C07/C06/C14/C11/C12/C09/C03/C04 files"}
```

### 12.x trigger_rows_jsonl

```jsonl
{"row_type":"trigger","case_id":"C08_095340_20250211_ISC_PARENT_RESULTS_HIGH_MAE","same_entry_group_id":"C08::095340::Stage4B::2025-02-12","representative_for_aggregate":true,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY","symbol":"095340","company":"ISC","trigger_type":"Stage4B","trigger_date":"2025-02-11","entry_date":"2025-02-12","entry_price":73700.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":7.33,"MFE_90D_pct":7.33,"MFE_180D_pct":15.33,"MAE_30D_pct":-21.44,"MAE_90D_pct":-41.93,"MAE_180D_pct":-41.93,"peak_return_pct":15.33,"peak_date":"2025-10-16","drawdown_after_peak_pct":-18.0,"calibration_usable":true,"corporate_action_overlap_180D":false,"source_proxy_only":false,"evidence_url_pending":false,"current_profile_error":true,"observed_price_path_label":"direct_quality_evidence_but_early_entry_high_mae"}
{"row_type":"trigger","case_id":"C08_058470_20250515_LEENO_Q1_RD_SOCKET_ORDER","same_entry_group_id":"C08::058470::Stage3-Yellow::2025-05-16","representative_for_aggregate":true,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY","symbol":"058470","company":"LEENO Industrial","trigger_type":"Stage3-Yellow","trigger_date":"2025-05-15","entry_date":"2025-05-16","entry_price":40300.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":30.52,"MFE_90D_pct":37.72,"MFE_180D_pct":183.62,"MAE_30D_pct":-4.84,"MAE_90D_pct":-4.84,"MAE_180D_pct":-4.84,"peak_return_pct":183.62,"peak_date":"2026-01-30","drawdown_after_peak_pct":-21.08,"calibration_usable":true,"corporate_action_overlap_180D":false,"source_proxy_only":true,"evidence_url_pending":false,"current_profile_error":false,"observed_price_path_label":"clean_positive_customer_quality_repeat_demand"}
{"row_type":"trigger","case_id":"C08_131290_20210224_TSE_HBM_DIE_CARRIER_SOCKET","same_entry_group_id":"C08::131290::Stage2-Actionable::2021-02-25","representative_for_aggregate":true,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY","symbol":"131290","company":"TSE","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-24","entry_date":"2021-02-25","entry_price":55600.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":14.39,"MFE_90D_pct":22.3,"MFE_180D_pct":44.78,"MAE_30D_pct":-19.42,"MAE_90D_pct":-19.42,"MAE_180D_pct":-19.42,"peak_return_pct":44.78,"peak_date":"2021-08-10","drawdown_after_peak_pct":-36.02,"calibration_usable":true,"corporate_action_overlap_180D":false,"source_proxy_only":false,"evidence_url_pending":false,"current_profile_error":true,"observed_price_path_label":"early_drawdown_structural_positive"}
{"row_type":"trigger","case_id":"C08_425420_20231222_TFE_PACKAGE_TEST_PROXY_BLOWOFF","same_entry_group_id":"C08::425420::Stage4B::2023-12-26","representative_for_aggregate":true,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY","symbol":"425420","company":"TFE","trigger_type":"Stage4B","trigger_date":"2023-12-22","entry_date":"2023-12-26","entry_price":34350.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":9.17,"MFE_90D_pct":27.95,"MFE_180D_pct":27.95,"MAE_30D_pct":-17.47,"MAE_90D_pct":-17.47,"MAE_180D_pct":-57.82,"peak_return_pct":27.95,"peak_date":"2024-03-21","drawdown_after_peak_pct":-67.03,"calibration_usable":true,"corporate_action_overlap_180D":false,"source_proxy_only":true,"evidence_url_pending":false,"current_profile_error":true,"observed_price_path_label":"package_test_solution_proxy_blowoff_then_collapse"}
{"row_type":"trigger","case_id":"C08_098120_20241203_MCS_BURNIN_SOCKET_DEMAND_RECOVERY","same_entry_group_id":"C08::098120::Stage2-Actionable::2024-12-04","representative_for_aggregate":true,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY","symbol":"098120","company":"Micro Contact Solution","trigger_type":"Stage2-Actionable","trigger_date":"2024-12-03","entry_date":"2024-12-04","entry_price":4570.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":39.39,"MFE_90D_pct":158.21,"MFE_180D_pct":435.01,"MAE_30D_pct":-7.11,"MAE_90D_pct":-7.11,"MAE_180D_pct":-7.11,"peak_return_pct":435.01,"peak_date":"2025-07-31","drawdown_after_peak_pct":-36.61,"calibration_usable":true,"corporate_action_overlap_180D":false,"source_proxy_only":true,"evidence_url_pending":false,"current_profile_error":true,"observed_price_path_label":"proxy_positive_with_direct_customer_confirmation_needed"}
{"row_type":"trigger","case_id":"C08_080580_20240402_OKINS_OP_COLLAPSE_CUSTOMER_CAPEX_CUT","same_entry_group_id":"C08::080580::Stage4C::2024-04-03","representative_for_aggregate":true,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY","symbol":"080580","company":"O Kins Electronics","trigger_type":"Stage4C","trigger_date":"2024-04-02","entry_date":"2024-04-03","entry_price":9090.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":6.16,"MFE_90D_pct":6.16,"MFE_180D_pct":6.16,"MAE_30D_pct":-25.3,"MAE_90D_pct":-46.48,"MAE_180D_pct":-59.46,"peak_return_pct":6.16,"peak_date":"2024-04-03","drawdown_after_peak_pct":-61.81,"calibration_usable":true,"corporate_action_overlap_180D":false,"source_proxy_only":false,"evidence_url_pending":false,"current_profile_error":true,"observed_price_path_label":"financial_quality_break_customer_capex_cut_hard_4c"}
```

### 12.x score_simulation_jsonl

```jsonl
{"row_type":"score_simulation","case_id":"C08_095340_20250211_ISC_PARENT_RESULTS_HIGH_MAE","symbol":"095340","baseline_profile_proxy":"e2r_2_2_rolling_calibrated","raw_component_score_breakdown_before":{"EPS":16,"Visibility":19,"Bottleneck":13,"Mispricing":10,"Valuation":7,"Capital":5,"Info":8},"total_before":78,"raw_component_score_breakdown_after_shadow_gate":{"EPS":15,"Visibility":16,"Bottleneck":12,"Mispricing":8,"Valuation":6,"Capital":5,"Info":12},"total_after_shadow_gate":74,"shadow_gate_action":"require customer/order/repeat-demand bridge; cap proxy-only/test-socket theme rows; route financial-quality break to 4C","production_scoring_changed":false}
{"row_type":"score_simulation","case_id":"C08_058470_20250515_LEENO_Q1_RD_SOCKET_ORDER","symbol":"058470","baseline_profile_proxy":"e2r_2_2_rolling_calibrated","raw_component_score_breakdown_before":{"EPS":22,"Visibility":22,"Bottleneck":15,"Mispricing":13,"Valuation":11,"Capital":5,"Info":8},"total_before":96,"raw_component_score_breakdown_after_shadow_gate":{"EPS":22,"Visibility":23,"Bottleneck":15,"Mispricing":13,"Valuation":11,"Capital":5,"Info":8},"total_after_shadow_gate":97,"shadow_gate_action":"require customer/order/repeat-demand bridge; cap proxy-only/test-socket theme rows; route financial-quality break to 4C","production_scoring_changed":false}
{"row_type":"score_simulation","case_id":"C08_131290_20210224_TSE_HBM_DIE_CARRIER_SOCKET","symbol":"131290","baseline_profile_proxy":"e2r_2_2_rolling_calibrated","raw_component_score_breakdown_before":{"EPS":17,"Visibility":19,"Bottleneck":14,"Mispricing":13,"Valuation":10,"Capital":5,"Info":7},"total_before":85,"raw_component_score_breakdown_after_shadow_gate":{"EPS":17,"Visibility":20,"Bottleneck":14,"Mispricing":12,"Valuation":10,"Capital":5,"Info":8},"total_after_shadow_gate":86,"shadow_gate_action":"require customer/order/repeat-demand bridge; cap proxy-only/test-socket theme rows; route financial-quality break to 4C","production_scoring_changed":false}
{"row_type":"score_simulation","case_id":"C08_425420_20231222_TFE_PACKAGE_TEST_PROXY_BLOWOFF","symbol":"425420","baseline_profile_proxy":"e2r_2_2_rolling_calibrated","raw_component_score_breakdown_before":{"EPS":14,"Visibility":15,"Bottleneck":10,"Mispricing":11,"Valuation":8,"Capital":5,"Info":8},"total_before":71,"raw_component_score_breakdown_after_shadow_gate":{"EPS":12,"Visibility":12,"Bottleneck":9,"Mispricing":8,"Valuation":6,"Capital":5,"Info":12},"total_after_shadow_gate":64,"shadow_gate_action":"require customer/order/repeat-demand bridge; cap proxy-only/test-socket theme rows; route financial-quality break to 4C","production_scoring_changed":false}
{"row_type":"score_simulation","case_id":"C08_098120_20241203_MCS_BURNIN_SOCKET_DEMAND_RECOVERY","symbol":"098120","baseline_profile_proxy":"e2r_2_2_rolling_calibrated","raw_component_score_breakdown_before":{"EPS":16,"Visibility":15,"Bottleneck":12,"Mispricing":14,"Valuation":10,"Capital":4,"Info":6},"total_before":77,"raw_component_score_breakdown_after_shadow_gate":{"EPS":16,"Visibility":16,"Bottleneck":12,"Mispricing":13,"Valuation":10,"Capital":4,"Info":8},"total_after_shadow_gate":79,"shadow_gate_action":"require customer/order/repeat-demand bridge; cap proxy-only/test-socket theme rows; route financial-quality break to 4C","production_scoring_changed":false}
{"row_type":"score_simulation","case_id":"C08_080580_20240402_OKINS_OP_COLLAPSE_CUSTOMER_CAPEX_CUT","symbol":"080580","baseline_profile_proxy":"e2r_2_2_rolling_calibrated","raw_component_score_breakdown_before":{"EPS":8,"Visibility":8,"Bottleneck":6,"Mispricing":9,"Valuation":5,"Capital":4,"Info":9},"total_before":49,"raw_component_score_breakdown_after_shadow_gate":{"EPS":5,"Visibility":5,"Bottleneck":4,"Mispricing":6,"Valuation":4,"Capital":3,"Info":17},"total_after_shadow_gate":44,"shadow_gate_action":"require customer/order/repeat-demand bridge; cap proxy-only/test-socket theme rows; route financial-quality break to 4C","production_scoring_changed":false}
```

### 12.x aggregate_jsonl

```jsonl
{"row_type":"aggregate","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE_VS_SMALL_CAP_PROXY","trigger_count":6,"positive_case_count":3,"counterexample_count":3,"stage4b_case_count":2,"stage4c_case_count":1,"source_proxy_only_count":3,"evidence_url_pending_count":0,"rows_missing_required_mfe_mae":0,"current_profile_error_count":5,"new_axis_proposed":"C08_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_GATE"}
```

### 12.x shadow_weight_jsonl

```jsonl
{"row_type":"shadow_weight","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","before_weights_EPS_Vis_Bott_Mis_Val_Cap_Info":"22/21/16/14/12/6/9","after_weights_EPS_Vis_Bott_Mis_Val_Cap_Info":"22/23/15/12/11/6/11","delta":"0/+2/-1/-2/-1/0/+2","new_axis_proposed":"C08_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_GATE","rationale":"raise visibility/customer-quality and information-quality penalties; lower mispricing/valuation credit for small-cap socket proxy rows without dated customer/order/revenue bridge","production_scoring_changed":false,"shadow_weight_only":true}
```

### 12.x residual_contribution_jsonl

```jsonl
{"row_type":"residual_contribution","case_id":"C08_095340_20250211_ISC_PARENT_RESULTS_HIGH_MAE","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"095340","residual_error_type":"false_positive_or_too_early_green_risk","suggested_bucket":"guardrail_support","rule_axis":"C08_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_GATE","contribution_weight":"high"}
{"row_type":"residual_contribution","case_id":"C08_058470_20250515_LEENO_Q1_RD_SOCKET_ORDER","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"058470","residual_error_type":"none_or_current_profile_too_slow_if_waiting_for_official_ir_only","suggested_bucket":"positive_support","rule_axis":"C08_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_GATE","contribution_weight":"high"}
{"row_type":"residual_contribution","case_id":"C08_131290_20210224_TSE_HBM_DIE_CARRIER_SOCKET","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"131290","residual_error_type":"stage2_valid_but_green_should_wait_until_mae_absorbed","suggested_bucket":"positive_support","rule_axis":"C08_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_GATE","contribution_weight":"medium"}
{"row_type":"residual_contribution","case_id":"C08_425420_20231222_TFE_PACKAGE_TEST_PROXY_BLOWOFF","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"425420","residual_error_type":"source_proxy_only_false_positive","suggested_bucket":"guardrail_support","rule_axis":"C08_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_GATE","contribution_weight":"high"}
{"row_type":"residual_contribution","case_id":"C08_098120_20241203_MCS_BURNIN_SOCKET_DEMAND_RECOVERY","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"098120","residual_error_type":"current_profile_may_underweight_tiny_socket_winner_but_source_quality_blocks_green","suggested_bucket":"positive_support","rule_axis":"C08_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_GATE","contribution_weight":"high"}
{"row_type":"residual_contribution","case_id":"C08_080580_20240402_OKINS_OP_COLLAPSE_CUSTOMER_CAPEX_CUT","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","symbol":"080580","residual_error_type":"hard_4c_correct_or_should_trigger_earlier","suggested_bucket":"guardrail_support","rule_axis":"C08_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_GATE","contribution_weight":"high"}
```


## 13. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for stock_agent E2R calibration. Do not rerun live scans. Read this standalone MD together with the full v12 calibration corpus. If the rows pass parser validation, treat the proposed axis C08_TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_GATE as a shadow-only candidate for C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

Implementation intent:
- Do not change production scoring directly from this single MD.
- Aggregate with other C08 rows first.
- Consider increasing C08 visibility/customer-quality and information-confidence weights while reducing price/mispricing credit for proxy-only test-socket theme rows.
- Add rule text that C08 Stage2-Actionable requires at least two of: named customer/customer group, R&D or mass-production socket repeat demand, current revenue/OP bridge, direct socket/probe/pin/burn-in product relevance.
- Cap source-proxy-only HBM/DDR5/CXL socket rows at Stage2/Watch unless direct official customer/order/revenue confirmation exists.
- Route customer-capex-cut + operating-profit-collapse + financing/interest-coverage break to 4C even if DDR5/CXL/HBM vocabulary remains positive.
```

## 14. Next Round State

```text
completed_round = R2
completed_loop = 131
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0/1 quality repair — C08 URL/proxy quality repair, 4C-thin path, customer-quality/repeat-demand bridge split
next_recommended_archetypes = C18_CONSUMER_EXPORT_CHANNEL_REORDER; C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN; C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION; C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

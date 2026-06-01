# V12 Research No-Repeat Index

이 문서는 새 자동연구 세션을 시작할 때 먼저 읽는 중복 방지 장부다.
목적은 같은 대섹터/아키타입 안에서 **같은 종목, 같은 날짜, 같은 trigger**를 반복 연구하지 않게 하는 것이다.

쉬운 예시:

```text
이미 C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / 257720 / Stage3-Green / 2024-05-10 이 여러 번 들어왔다.
다음 연구는 같은 조합을 다시 쓰지 말고,
새 종목, 새 날짜, 새 trigger family, 또는 4B/4C/반례를 찾아야 한다.
```

last_updated: `2026-06-01`

## 원본 데이터

| source | role |
|---|---|
| `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl` | 중복제거 후 대표 trigger row |
| `data/e2r/calibration/v12/v12_trigger_rows_validated.jsonl` | 검증 통과 raw row. 반복 조합 확인용 |
| `data/e2r/calibration/v12/v12_aggregate_metrics.json` | 대섹터/아키타입 집계 |
| `data/e2r/calibration/v12/stage_transition_summary.jsonl` | Stage2, Green, 4B, 4C 전이 요약 |
| `data/e2r/calibration/v12/v12_promotion_decisions.jsonl` | apply / hold / block 결정 |
| `reports/e2r_calibration/v12/coverage_matrix.md` | 최신 scope별 coverage 요약 |

## 이번 배치 반영 메모

| item | result |
|---|---|
| run command | `run-v12-calibration --md-input-root docs/round` |
| v12 result MD | 648 |
| parser failures | 0 |
| representative rows | 3699 |
| validated rows | 4334 |
| raw aggregate metric rows | 219 |
| raw shadow weight rows | 1569 |
| active profile | `e2r_2_2_rolling_calibrated` |
| R13 cross checkpoint rows | `r13_cross_case`는 `trigger`로 수용하되 `do_not_count_as_new_case=true`로 중복 가중치 차단 |

R13 교차검증 row는 새 독립 케이스로 세지 않는다. 예를 들어 R5에서 이미 다룬 코스맥스 row가 R13 guardrail 검증에 다시 나오면, "검증 근거"로는 읽지만 "새 C20 positive 1개"로 중복 계산하지 않는다.

## 현재 Corpus Snapshot

| metric | value |
|---|---:|
| representative row_count | 3699 |
| validated row_count | 4334 |
| stage_transition_summary rows | 2778 |
| aggregate metric rows | 2442 |
| raw aggregate metric rows | 219 |
| raw shadow weight rows | 1569 |
| unique_case_count | 2391 |
| unique_symbol_count | 492 |
| unique_round_count | 13 |
| positive_case_count | 670 |
| counterexample_count | 754 |
| 4B_case_count | 721 |
| 4C_case_count | 254 |
| good_stage2_count | 1112 |
| bad_stage2_count | 463 |
| source_proxy_only_count | 523 |
| evidence_url_pending_count | 525 |
| exact duplicate key count in validated rows | 976 |
| extra repeated raw rows before dedupe | 1555 |
| apply_next_patch decisions | 112 |
| hold/block decisions | 13 |


## 반영된 safe patch 축

| axis | applied decisions |
|---|---:|
| earlier_thesis_break_watch | 36 |
| local_4b_watch_guard | 32 |
| stage2_required_bridge | 44 |

## 주요 rejected reason

Rejected row는 버리는 데이터가 아니라 다음 정규화 TODO다. 예를 들어 `missing_required_mfe_mae`는 가격경로 30D/90D/180D가 부족해서 score 보정에 못 쓴다는 뜻이다.

| reason | rows |
|---|---:|
| not_representative_for_aggregate | 1773 |
| missing_required_mfe_mae | 1510 |
| not_usable_for_promotion | 663 |
| price_only_no_evidence | 303 |
| missing_entry_price | 182 |
| missing_entry_date | 180 |
| missing_trigger_type | 136 |
| insufficient_forward_window | 34 |
| corporate_action_contaminated | 5 |

## 연구 시작 전 중복 판정 규칙

| 구분 | 판정 | 행동 |
|---|---|---|
| Hard duplicate | `canonical_archetype_id + symbol + trigger_type + entry_date`가 이미 있음 | 연구 금지. 새 케이스로 세지 말 것 |
| Soft duplicate | 같은 `canonical_archetype_id + symbol`이지만 날짜/trigger가 다름 | 새 증거 family, 새 Stage transition, 4B/4C, 반례일 때만 허용 |
| Useful expansion | 같은 archetype의 새 symbol 또는 새 failure mode | 우선 연구 |
| Data-quality repair | 기존 row가 `evidence_url_pending` 또는 `source_proxy_only` | 같은 케이스라도 URL/공시/리포트 검증 보강이면 허용 |
| Bad expansion | 가격만 있고 비가격 증거가 없음 | Stage2/Green 연구로 쓰지 말고 4B watch/반례 목적만 허용 |
| Unknown symbol | symbol이 `UNKNOWN_SYMBOL` 또는 비어 있음 | 새 연구보다 먼저 symbol 정규화 보강 |

## 아키타입별 현재 커버리지

| archetype | rows | symbols | date range | good/bad S2 | 4B/4C | URL/proxy | top covered symbols |
|---|---:|---:|---|---|---|---|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 23 | 12 | 2023-01-04~2024-07-31 | 14/1 | 2/0 | 15/18 | 010620(4), 329180(3), 009540(2), 010140(2), 077970(2), 082740(2) |
| C02_POWER_GRID_DATACENTER_CAPEX | 64 | 11 | 2023-01-27~2024-07-24 | 33/1 | 17/0 | 17/17 | 010120(18), 267260(14), 298040(9), 006340(5), 103590(5), 017040(3) |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 89 | 13 | 2022-01-17~2024-11-12 | 40/7 | 20/1 | 15/15 | 064350(22), 272210(11), UNKNOWN_SYMBOL(9), 012450(8), 010820(7), 003570(6) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 62 | 14 | 2022-02-28~2025-01-10 | 9/9 | 21/1 | 9/9 | 032820(10), 094820(9), 105840(9), 006910(7), 034020(6), 052690(5) |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 19 | 12 | 2022-01-12~2024-03-27 | 3/7 | 0/5 | 3/3 | 006360(4), 047040(4), 000720(3), 028050(3), 375500(3), 034300(1) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 37 | 5 | 2023-05-25~2024-10-08 | 10/2 | 8/4 | 3/3 | 000660(18), 005930(11), UNKNOWN_SYMBOL(5), 007660(1), 222800(1), 353200(1) |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 68 | 22 | 2023-09-25~2024-10-17 | 28/4 | 16/0 | 12/12 | UNKNOWN_SYMBOL(10), 232140(8), 031980(6), 042700(6), 003160(5), 089030(5) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 78 | 13 | 2023-03-30~2024-09-26 | 24/9 | 16/1 | 12/12 | 098120(13), 080580(9), 058470(8), 095340(7), 131290(7), 219130(6) |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 56 | 17 | 2024-01-19~2024-07-11 | 7/0 | 19/2 | 6/6 | 240810(8), 036930(7), 039030(4), 403870(4), 003160(3), 042700(3) |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 31 | 10 | 2023-03-17~2024-06-07 | 15/4 | 2/0 | 9/9 | 036930(6), 240810(6), 084370(4), 095610(4), 테스(2), 000660(1) |
| C11_BATTERY_ORDERBOOK_RERATING | 79 | 21 | 2022-08-17~2024-07-22 | 31/9 | 17/5 | 12/12 | 247540(11), 003670(8), 393890(8), 222080(6), 348370(6), 066970(5) |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 68 | 18 | 2023-01-26~2024-07-25 | 15/2 | 15/5 | 11/11 | 361610(10), 393890(10), 336370(6), 006110(5), 011790(5), 003670(4) |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 43 | 11 | 2022-05-25~2025-04-08 | 10/9 | 7/2 | 6/6 | 373220(14), 006400(13), 096770(5), 003670(2), 020150(2), 051910(2) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 76 | 15 | 2023-02-22~2024-12-20 | 0/0 | 33/29 | 6/6 | 247540(13), 003670(10), 066970(10), 361610(8), 373220(7), 393890(6) |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 71 | 25 | 2020-08-10~2025-02-21 | 21/8 | 15/0 | 12/12 | 005490(12), 004020(9), 012800(5), 025820(5), 001430(4), 018470(4) |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 67 | 23 | 2019-05-20~2024-10-10 | 17/7 | 19/0 | 13/13 | 001570(8), 005490(8), 000910(7), 075970(5), 005290(4), 081150(4) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 140 | 23 | 2020-08-03~2024-07-15 | 51/18 | 25/3 | 19/15 | 298020(23), 011780(21), 006650(15), 011170(12), 014830(9), 010950(7) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 126 | 20 | 2020-03-17~2024-12-16 | 41/14 | 25/8 | 18/18 | 003230(20), 005180(14), 004370(13), 192820(9), 097950(8), 271560(8) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 89 | 17 | 2021-05-17~2024-10-16 | 17/14 | 18/7 | 21/25 | 111770(11), 081660(10), 383220(9), UNKNOWN_SYMBOL(8), 020000(7), 036620(7) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 200 | 18 | 2021-05-10~2025-06-25 | 67/20 | 40/12 | 3/3 | 257720(48), 090430(21), 003230(19), 018290(19), 051900(14), 192820(14) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 235 | 24 | 2021-08-06~2025-06-24 | 86/24 | 29/5 | 26/23 | 105560(56), 323410(34), 086790(26), UNKNOWN_SYMBOL(21), 006220(16), 055550(10) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 162 | 11 | 2023-05-15~2025-05-30 | 53/29 | 22/5 | 32/32 | 000810(34), 005830(33), 088350(17), 001450(16), 032830(13), 085620(13) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 139 | 15 | 2019-02-07~2025-03-27 | 39/7 | 22/23 | 9/9 | 000100(35), 028300(34), UNKNOWN_SYMBOL(20), 145020(16), 196170(13), 068270(3) |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 83 | 19 | 2019-08-01~2024-11-20 | 30/7 | 6/20 | 15/22 | 000100(10), 215600(9), 009420(8), 298380(8), 028300(7), 039200(7) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 101 | 21 | 2022-05-11~2024-07-01 | 41/8 | 17/4 | 18/18 | 338220(17), 214150(14), 099190(11), 145720(8), 228670(6), 043150(5) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 137 | 16 | 2020-04-24~2024-10-28 | 50/17 | 20/6 | 12/12 | 067160(24), 035420(17), 035720(16), 089600(8), SOOP(8), NAVER(8) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 114 | 25 | 2016-03-24~2024-08-21 | 42/11 | 24/7 | 15/15 | 035900(12), 194480(10), 259960(10), 352820(9), 225570(7), 253450(7) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 102 | 22 | 2019-05-27~2024-08-13 | 28/6 | 20/2 | 15/15 | 012510(20), 053800(16), 263860(12), 030520(7), 131370(6), 136540(6) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 203 | 36 | 2020-08-14~2024-09-09 | 68/46 | 32/10 | 46/42 | UNKNOWN_SYMBOL(20), 000270(19), 161390(14), 012330(13), 005380(12), 018880(12) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 159 | 29 | 2021-03-11~2024-09-30 | 15/21 | 29/29 | 42/42 | 047040(15), 006360(13), UNKNOWN_SYMBOL(13), 294870(12), 005960(9), 000720(8) |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 206 | 77 | 2020-01-20~2024-07-31 | 41/38 | 43/0 | 39/40 | UNKNOWN_SYMBOL(15), 004090(8), 036460(8), 112610(7), 005860(6), 008970(6) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 157 | 23 | 2020-03-27~2025-04-29 | 51/23 | 42/11 | 34/28 | 010130(30), 041510(26), 008930(13), 011200(11), UNKNOWN_SYMBOL(8), 003920(7) |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 368 | 137 | 2019-08-01~2025-03-27 | 104/68 | 74/42 | 0/0 | 247540(10), 028300(9), 105560(8), 000100(7), 003670(7), 006360(7) |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 12 | 12 | 2021-02-23~2024-06-28 | 5/3 | 0/1 | 0/0 | 003230(1), 005490(1), 010780(1), 011200(1), 011790(1), 025950(1) |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 23 | 21 | 2020-11-06~2024-07-22 | 3/7 | 5/3 | 0/0 | 028300(3), 001390(1), 001570(1), 003070(1), 003310(1), 006220(1) |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 12 | 12 | 2021-07-06~2024-05-29 | 3/3 | 1/1 | 0/0 | 005930(1), 006340(1), 010120(1), 011170(1), 019170(1), 021320(1) |

## 반복 위험이 높은 symbol/archetype 조합

아래 조합은 이미 대표 row가 많이 쌓여 있다. 같은 날짜/같은 trigger 반복은 피한다.

| archetype | symbol | representative rows | date range | main trigger types |
|---|---|---:|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | 56 | 2024-01-26~2025-05-26 | Stage2-Actionable(28), Stage3-Green(15), Stage4B(11), 4B(1), Stage3-Yellow(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 257720 | 48 | 2023-05-09~2024-11-14 | Stage2-Actionable(20), Stage4B(15), Stage3-Green(11), 4B overlay(1), 4B(1) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | 35 | 2024-08-20~2024-12-17 | Stage3-Green(12), Stage2-Actionable(11), Stage4B(10), 4B(1), Stage3-Yellow(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 323410 | 34 | 2021-08-06~2025-06-24 | Stage2-Actionable(12), Stage4B(4), 4C(2), Stage2-FalsePositive(2), Stage2-PolicyOnly(2) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 000810 | 34 | 2023-05-15~2025-05-30 | Stage2-Actionable(19), Stage3-Green(9), Stage4B(6) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 028300 | 34 | 2024-03-08~2024-05-20 | Stage3-Green(9), Stage4C(9), 4C(9), Stage2-Actionable(2), Stage3-Yellow(2) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 005830 | 33 | 2023-05-15~2025-05-15 | Stage2-Actionable(19), Stage3-Green(9), Stage4B(5) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 010130 | 30 | 2024-09-13~2024-12-06 | Stage2-Actionable(16), Stage4B(11), 4B(3) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 086790 | 26 | 2024-01-26~2024-10-25 | Stage2-Actionable(17), Stage3-Green(7), Stage3-Yellow(1), Stage4B(1) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 041510 | 26 | 2023-02-10~2023-03-08 | Stage2-Actionable(14), Stage4B(9), 4B(2), Stage2-CapGuard(1) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 067160 | 24 | 2021-04-30~2024-07-11 | Stage2-Actionable(11), Stage4B(6), Stage3-Green(4), 4B(2), Stage3-Yellow(1) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 298020 | 23 | 2020-10-30~2024-05-17 | Stage2-Actionable(10), Stage4B(9), Stage3-Green(4) |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 064350 | 22 | 2022-07-27~2024-02-22 | Stage2-Actionable(16), Stage4B(5), Stage3-Yellow(1) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 011780 | 21 | 2020-08-03~2024-07-15 | Stage2-Actionable(11), Stage3-Green(5), Stage4B(5) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 090430 | 21 | 2021-05-10~2025-06-05 | Stage2-Actionable(5), Stage3-Yellow(3), Stage4C(3), Stage2(2), Stage4B(2) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | UNKNOWN_SYMBOL | 21 | 2021-08-06~2025-05-26 | Stage2-Actionable(10), Stage3-Green(3), Stage2(2), Stage3-Yellow(2), Price-only / IPO platform-bank rerating(1) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 003230 | 20 | 2023-11-15~2024-12-16 | Stage2-Actionable(9), Stage3-Green(5), Stage4B(5), 4B(1) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | UNKNOWN_SYMBOL | 20 | 2019-02-07~2024-11-06 | Stage2-Actionable(9), 4C(3), Stage3-Green(3), Stage3-Yellow(2), 4B(1) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 012510 | 20 | 2019-05-27~2024-07-08 | Stage2-Actionable(10), Stage3-Green(6), Stage4B(3), Stage3-Yellow(1) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | UNKNOWN_SYMBOL | 20 | 2020-08-14~2024-06-27 | Stage2-Actionable(13), Stage4B(5), Stage4C(2) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 003230 | 19 | 2023-11-15~2024-12-17 | Stage2-Actionable(10), Stage3-Green(4), Stage4B(3), 4B(2) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 018290 | 19 | 2023-08-14~2024-09-20 | Stage2-Actionable(11), Stage3-Green(7), Stage4B(1) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 000270 | 19 | 2020-10-26~2024-06-19 | Stage2-Actionable(9), Stage3-Green(4), Stage4B(4), Stage2-rumor-redteam(1), Stage4C(1) |
| C02_POWER_GRID_DATACENTER_CAPEX | 010120 | 18 | 2024-01-03~2024-07-24 | Stage4B(8), Stage2-Actionable(7), 4B(1), Stage3-Green(1), Stage3-Yellow(1) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 | 18 | 2023-05-25~2024-07-11 | Stage2-Actionable(8), Stage4B(7), Stage3-Green(3) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 088350 | 17 | 2024-01-24~2025-02-13 | Stage2-Actionable(10), 4B(2), 4B overlay(1), Stage2(1), Stage2-FalsePositive(1) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 338220 | 17 | 2023-02-24~2023-09-07 | Stage2-Actionable(8), Stage4B(6), 4B(1), Stage3-Green(1), Stage3-Yellow(1) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 035420 | 17 | 2020-04-24~2024-05-03 | Stage2-Actionable(11), Stage3-Green(4), Stage2-Watch(1), Stage3-Yellow(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 006220 | 16 | 2023-01-17~2024-04-19 | Stage4B(5), 4B(2), Price-only-blowoff / blocked Stage2 candidate(2), Stage2-Actionable(2), Price-only Stage2 Candidate(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 001450 | 16 | 2023-05-15~2025-02-14 | Stage2-Actionable(11), 4C protection(1), Stage2-candidate-rejected(1), Stage2-or-Yellow stress(1), Stage3-Green(1) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 145020 | 16 | 2024-03-04~2024-11-06 | Stage2-Actionable(10), Stage4B(5), Stage3-Green(1) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 035720 | 16 | 2020-05-07~2024-01-11 | Stage2-Actionable(7), Stage4C(3), Stage3-Green(2), 4B overlay(1), 4B(1) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 053800 | 16 | 2022-01-05~2022-04-15 | Stage4B(6), False-Stage2-Actionable(2), Stage2-FalsePositiveCandidate(2), Price-only Stage2-blocked(1), Stage2-Actionable(1) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 006650 | 15 | 2021-01-06~2024-01-25 | Stage2-Actionable(5), Stage4C(3), Stage3-Yellow(3), Stage3-Green(2), Stage2(1) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 047040 | 15 | 2021-03-11~2024-07-18 | Stage2-Actionable(4), Stage3-Yellow(3), Stage2-RiskWatch / LargeBuilderNoFull4B(2), Stage2-risk-watch(2), RiskWatch-BoundedLargeBuilderPFNoForced4BNoHard4C(1) |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | UNKNOWN_SYMBOL | 15 | 2020-01-21~2024-02-27 | Stage2-Actionable(11), Stage4B(3), Stage3-Green(1) |
| C02_POWER_GRID_DATACENTER_CAPEX | 267260 | 14 | 2023-01-27~2024-07-24 | Stage2-Actionable(11), Stage4B(3) |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 373220 | 14 | 2022-08-12~2025-04-08 | Stage2-Actionable(9), Stage4B(2), Stage4C(2), Stage3-Yellow(1) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 005180 | 14 | 2024-04-01~2024-06-11 | Stage2-Actionable(7), Stage4B(5), 4B(1), Stage3-Green(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 051900 | 14 | 2021-06-24~2024-05-23 | Stage2-Actionable(4), 4C(2), Stage4C(2), RiskWatch-ChinaBeautyBrandRecoveryBoundedNoForced4BNoDurableStage2(1), Stage2 false reopen(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 192820 | 14 | 2023-05-15~2025-06-25 | Stage2-Actionable(9), Stage3-Yellow(3), Stage4B(2) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 214150 | 14 | 2023-05-02~2024-05-09 | Stage2-Actionable(8), Stage3-Green(5), Stage4B(1) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 161390 | 14 | 2023-04-12~2024-04-16 | Stage2-Actionable(10), Stage4B(2), Stage2-FalsePositive / TireOEMReplacementMixMarginFade(1), Stage2-Lifecycle-TireVolumeMixCostSpreadMarginBridgeWithLocal4B(1) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 098120 | 13 | 2023-03-30~2024-09-26 | Stage3-Yellow(5), Stage2-Actionable(4), Stage4B(2), Stage2-FalsePositive / ICSocketCustomerQualityFade(1), Stage2-FalsePositive / TestSocketCustomerQualityBridgeFade(1) |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 006400 | 13 | 2022-05-25~2024-12-03 | Stage2-Actionable(5), 4B(2), Stage2-Headline-JV(2), Stage3-Yellow(2), Stage2-Theme-Watch(1) |

## 이미 많이 반복된 exact key 예시

아래는 검증 row 기준으로 이미 여러 번 등장한 exact key다. 새 연구에서 그대로 반복하면 dedupe 이후 기여도가 거의 없다.

| count | archetype | symbol | trigger_type | date | sample files |
|---:|---|---|---|---|---|
| 21 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 010130 | Stage2-Actionable | 2024-09-13 | e2r_stock_web_v12_residual_round_R11_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TEN..., e2r_stock_web_v12_residual_round_R11_loop_12_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TEN... |
| 16 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 041510 | Stage2-Actionable | 2023-02-10 | e2r_stock_web_v12_residual_round_R11_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TEN..., e2r_stock_web_v12_residual_round_R11_loop_12_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TEN... |
| 14 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 028300 | 4C | 2024-05-17 | e2r_stock_web_v12_residual_round_R7_loop_14_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION..., e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATIO... |
| 14 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 145020 | Stage2-Actionable | 2024-03-04 | e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATIO..., e2r_stock_web_v12_residual_round_R7_loop_10_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION... |
| 13 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | Stage2-Actionable | 2024-08-21 | e2r_stock_web_v12_residual_round_R7_loop_10_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION..., e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATIO... |
| 12 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage2-Actionable | 2024-02-26 | e2r_stock_web_v12_residual_round_R6_loop_10_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETUR..., e2r_stock_web_v12_residual_round_R13_loop_25_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETU... |
| 11 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 257720 | Stage4B | 2024-06-19 | e2r_stock_web_v12_residual_round_R5_loop_10_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_rese..., e2r_stock_web_v12_residual_round_R13_loop_24_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_res... |
| 11 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage3-Green | 2024-04-26 | e2r_stock_web_v12_residual_round_R6_loop_15_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETUR..., e2r_stock_web_v12_residual_round_R6_loop_60_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETUR... |
| 11 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage4B | 2024-10-25 | e2r_stock_web_v12_residual_round_R6_loop_45_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETUR..., e2r_stock_web_v12_residual_round_R6_loop_60_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETUR... |
| 11 | C22_INSURANCE_RATE_CYCLE_RESERVE | 000810 | Stage2-Actionable | 2024-02-23 | e2r_stock_web_v12_residual_round_R13_loop_20_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_r..., e2r_stock_web_v12_residual_round_R6_loop_10_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_re... |
| 10 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 257720 | Stage3-Green | 2024-05-10 | e2r_stock_web_v12_residual_round_R13_loop_46_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_res..., e2r_stock_web_v12_residual_round_R13_loop_55_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_res... |
| 10 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage2-Actionable | 2024-02-08 | e2r_stock_web_v12_residual_round_R6_loop_15_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETUR..., e2r_stock_web_v12_residual_round_R6_loop_16_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETUR... |
| 10 | C22_INSURANCE_RATE_CYCLE_RESERVE | 000810 | Stage3-Green | 2024-05-16 | e2r_stock_web_v12_residual_round_R6_loop_36_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_re..., e2r_stock_web_v12_residual_round_R6_loop_41_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_re... |
| 10 | C22_INSURANCE_RATE_CYCLE_RESERVE | 005830 | Stage2-Actionable | 2024-02-23 | e2r_stock_web_v12_residual_round_R13_loop_20_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_r..., e2r_stock_web_v12_residual_round_R6_loop_10_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_re... |
| 10 | C22_INSURANCE_RATE_CYCLE_RESERVE | 005830 | Stage3-Green | 2024-05-16 | e2r_stock_web_v12_residual_round_R6_loop_36_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_re..., e2r_stock_web_v12_residual_round_R6_loop_41_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_re... |
| 9 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 067160 | Stage2-Actionable | 2023-12-07 | e2r_stock_web_v12_residual_round_R8_loop_11_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVER..., e2r_stock_web_v12_residual_round_R8_loop_13_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVER... |
| 8 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 | Stage4B | 2024-07-11 | e2r_stock_web_v12_residual_round_R2_loop_15_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_resear..., e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_hbm_custome... |
| 8 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 298020 | Stage4B | 2021-07-16 | e2r_stock_web_v12_residual_round_R13_loop_26_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_rese..., e2r_stock_web_v12_residual_round_R4_loop_13_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_resea... |
| 8 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 028300 | Stage4C | 2024-05-17 | e2r_stock_web_v12_residual_round_R7_loop_11_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION..., e2r_stock_web_v12_residual_round_R7_loop_14_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION... |
| 8 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 008930 | Stage2-Actionable | 2024-01-15 | e2r_stock_web_v12_residual_round_R11_loop_12_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TEN..., e2r_stock_web_v12_residual_round_R13_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TEN... |
| 8 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 041510 | Stage4B | 2023-03-07 | e2r_stock_web_v12_residual_round_R12_loop_1_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TEND..., e2r_stock_web_v12_residual_round_R11_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TEN... |
| 7 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 064350 | Stage2-Actionable | 2022-07-29 | e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_defen..., e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_armor... |
| 7 | C22_INSURANCE_RATE_CYCLE_RESERVE | 000370 | Stage2-Actionable | 2024-02-01 | e2r_stock_web_v12_residual_round_R13_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_..., e2r_stock_web_v12_residual_round_R13_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARD... |
| 7 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 196170 | Stage2-Actionable | 2024-02-23 | e2r_stock_web_v12_residual_round_R7_loop_14_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION..., e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVE... |
| 7 | C24_BIO_TRIAL_DATA_EVENT_RISK | 009420 | Stage2-Actionable | 2023-09-27 | e2r_stock_web_v12_residual_round_R13_loop_32_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md, e2r_stock_web_v12_residual_round_R7_loop_15_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research(1).md |
| 6 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 247540 | Stage4B | 2023-07-26 | e2r_stock_web_v12_residual_round_R3_loop_11_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md, e2r_stock_web_v12_residual_round_R13_loop_55_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md |
| 6 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 257720 | Stage4B | 2024-06-21 | e2r_stock_web_v12_residual_round_R13_loop_46_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_res..., e2r_stock_web_v12_residual_round_R13_loop_55_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_res... |
| 6 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 086790 | Stage2-Actionable | 2024-02-26 | e2r_stock_web_v12_residual_round_R6_loop_10_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETUR..., e2r_stock_web_v12_residual_round_R13_loop_18_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETU... |
| 6 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 323410 | Stage2-Actionable | 2024-02-26 | e2r_stock_web_v12_residual_round_R6_loop_10_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETUR..., e2r_stock_web_v12_residual_round_R13_loop_18_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETU... |
| 6 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | UNKNOWN_SYMBOL | Stage2-Actionable | 2025-04-25 | e2r_stock_web_v12_residual_round_R13_loop_23_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETU..., e2r_stock_web_v12_residual_round_R13_loop_22_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETU... |
| 6 | C22_INSURANCE_RATE_CYCLE_RESERVE | 003690 | Stage2-Actionable | 2024-02-01 | e2r_stock_web_v12_no_repeat_standalone_L6_FINANCIALS_CAPITAL_RETURN_C22_INSURANCE_RATE_CYCLE_RESERVE_life_reinsuran..., e2r_stock_web_v12_residual_round_R6_loop_15_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_re... |
| 6 | C22_INSURANCE_RATE_CYCLE_RESERVE | 088350 | Stage2-Actionable | 2024-02-23 | e2r_stock_web_v12_residual_round_R13_loop_20_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_r..., e2r_stock_web_v12_residual_round_R6_loop_13_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_re... |
| 6 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | Stage3-Green | 2024-08-28 | e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATIO..., e2r_stock_web_v12_residual_round_R7_loop_14_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION... |
| 6 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | Stage4B | 2024-10-15 | e2r_stock_web_v12_residual_round_R7_loop_14_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION..., e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVE... |
| 6 | C24_BIO_TRIAL_DATA_EVENT_RISK | 215600 | Stage4C | 2019-08-02 | e2r_stock_web_v12_residual_round_R13_loop_32_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md, e2r_stock_web_v12_residual_round_R7_loop_15_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research(1).md |
| 6 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 225570 | Stage2-Actionable | 2024-07-03 | e2r_stock_web_v12_residual_round_R8_loop_71_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_rese..., e2r_stock_web_v12_residual_round_R13_loop_71_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_... |
| 6 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 294870 | 4C | 2022-01-12 | e2r_stock_web_v12_residual_round_R10_loop_10_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_B..., e2r_stock_web_v12_residual_round_R10_loop_12_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_B... |
| 5 | C02_POWER_GRID_DATACENTER_CAPEX | 267260 | Stage2-Actionable | 2024-01-03 | e2r_stock_web_v12_residual_round_R1_loop_15_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_resea..., e2r_stock_web_v12_residual_round_R1_loop_10_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_resea... |
| 5 | C02_POWER_GRID_DATACENTER_CAPEX | 298040 | Stage2-Actionable | 2024-01-03 | e2r_stock_web_v12_residual_round_R1_loop_15_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_resea..., e2r_stock_web_v12_residual_round_R1_loop_10_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_resea... |
| 5 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 272210 | Stage3-Yellow | 2022-07-29 | e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_snt_h..., e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_defen... |
| 5 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 240810 | Stage2-Actionable | 2024-02-29 | e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_memory_r..., e2r_stock_web_v12_residual_round_R13_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_... |
| 5 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 003230 | Stage2-Actionable | 2023-11-15 | e2r_stock_web_v12_residual_round_R5_loop_11_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_rese..., e2r_stock_web_v12_residual_round_R12_loop_10_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_res... |
| 5 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 005180 | Stage2-Actionable | 2024-05-17 | e2r_stock_web_v12_residual_round_R5_loop_11_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_rese..., e2r_stock_web_v12_residual_round_R5_loop_12_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_rese... |
| 5 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 003230 | Stage2-Actionable | 2024-05-17 | e2r_stock_web_v12_residual_round_R5_loop_10_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_rese..., e2r_stock_web_v12_residual_round_R5_loop_11_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_rese... |
| 5 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 003230 | Stage4B | 2024-06-18 | e2r_stock_web_v12_residual_round_R13_loop_46_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_res..., e2r_stock_web_v12_residual_round_R13_loop_55_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_res... |

## 다음 연구 우선순위

새 연구는 아래 순서로 고른다.

1. `hold_for_more_evidence` 또는 `blocked_by_data_quality`가 남은 scope의 **새 symbol**.
2. 이미 positive가 많은 archetype의 **반례/counterexample/4C**.
3. 4B가 막힌 scope의 **비가격 4B timing evidence**.
4. `evidence_url_pending` 또는 `source_proxy_only`를 해소하는 정확한 URL/공시/IR/리포트 보강.
5. `UNKNOWN_SYMBOL` row의 symbol 정규화.

### 현재 hold/block scope

| scope | axis | decision | missing_to_promote | recommended action |
|---|---|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| C22_INSURANCE_RATE_CYCLE_RESERVE | stage2_bonus_candidate_delta | blocked_by_logic_risk | bad_stage2_or_high_mae_rate_too_high | keep_green_restricted_and_add_red_team_guard |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | full_4b_overlay_candidate | hold_for_more_evidence | need_more_good_non_price_4b_timing_cases | collect_non_overlapping_cases |

## 새 연구 MD 작성 지침

새 v12 MD를 만들 때는 파일명과 본문 metadata에 아래 필드를 반드시 남긴다.

```text
round 또는 selected_round
loop 또는 standalone
large_sector_id
canonical_archetype_id
fine_archetype_id
symbol
trigger_type
trigger_date
entry_date
entry_price
MFE/MAE 30D/90D/180D
evidence_url_pending
source_proxy_only
```

R13 cross checkpoint처럼 원천 row를 재검증하는 경우에도 가능하면 `entry_date`, `entry_price`, `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`를 같이 남긴다. 값이 빠지면 parser는 row를 읽어도 가격경로 검증에는 제한된다.

그리고 새 연구 프롬프트에는 이 문장을 넣는다.

```text
Before selecting cases, read docs/core/V12_Research_No_Repeat_Index.md.
Do not reuse the same canonical_archetype_id + symbol + trigger_type + entry_date combination.
Prefer new symbols, new trigger families, counterexamples, 4B/4C paths, or data-quality repairs.
```

## 빠른 중복 확인 명령

특정 조합이 이미 있는지 확인하려면 아래처럼 본다.

```bash
python - <<'PY2'
import json
import re
from pathlib import Path
ARCH='C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION'
SYMBOL='257720'
DATE='2024-05-10'
TRIGGER='Stage3-Green'
p=Path('data/e2r/calibration/v12/v12_trigger_rows_validated.jsonl')
hits=[]
for line in p.read_text(encoding="utf-8").splitlines():
    row=json.loads(line)
    raw_symbol=str(row.get('symbol') or row.get('company_name') or '')
    match=re.search(r'\d{6}', raw_symbol)
    symbol=match.group(0) if match else raw_symbol.split()[0] if raw_symbol else ''
    date=row.get('entry_date') or row.get('trigger_date')
    if row.get('canonical_archetype_id')==ARCH and symbol==SYMBOL and date==DATE and row.get('trigger_type')==TRIGGER:
        hits.append((row.get('source_file'), row.get('case_id'), row.get('trigger_id')))
print(len(hits))
for hit in hits[:20]:
    print(hit)
PY2
```

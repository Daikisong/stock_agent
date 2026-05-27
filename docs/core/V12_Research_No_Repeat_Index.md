# V12 Research No-Repeat Index

이 문서는 새 자동연구 세션을 시작할 때 먼저 읽는 중복 방지 장부다.
목적은 같은 대섹터/아키타입 안에서 **같은 종목, 같은 날짜, 같은 trigger**를 반복 연구하지 않게 하는 것이다.

쉬운 예시:

```text
이미 C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / 257720 / Stage3-Green / 2024-05-10 이 여러 번 들어왔다.
다음 연구는 같은 조합을 다시 쓰지 말고,
새 종목, 새 날짜, 새 trigger family, 또는 4B/4C/반례를 찾아야 한다.
```

## 원본 데이터

| source | role |
|---|---|
| `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl` | 중복제거 후 대표 trigger row |
| `data/e2r/calibration/v12/v12_trigger_rows_validated.jsonl` | 검증 통과 raw row. 반복 조합 확인용 |
| `data/e2r/calibration/v12/v12_aggregate_metrics.json` | 대섹터/아키타입 집계 |
| `data/e2r/calibration/v12/stage_transition_summary.jsonl` | Stage2, Green, 4B, 4C 전이 요약 |

## 현재 Corpus Snapshot

| metric | value |
|---|---:|
| row_count | 1176 |
| unique_case_count | 588 |
| unique_symbol_count | 202 |
| unique_round_count | 13 |
| positive_case_count | 145 |
| counterexample_count | 114 |
| 4B_case_count | 93 |
| 4C_case_count | 54 |
| good_stage2_count | 371 |
| bad_stage2_count | 136 |
| source_proxy_only_count | 15 |
| evidence_url_pending_count | 8 |
| exact duplicate key count in validated rows | 373 |
| extra repeated raw rows before dedupe | 612 |

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
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 7 | 4 | 2022-07-29~2024-11-12 | 4/1 | 0/0 | 0/0 | 012450(3), 079550(2), 047810(1), 065450(1) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 9 | 5 | 2024-07-18~2024-12-03 | 1/5 | 1/0 | 0/0 | 034020(3), 051600(2), 052690(2), 000720(1), 083650(1) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 10 | 2 | 2023-10-27~2024-10-08 | 2/2 | 0/1 | 0/0 | UNKNOWN_SYMBOL(5), 000660(3), 005930(2) |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 8 | 5 | 2024-01-19~2024-06-13 | 2/0 | 1/0 | 0/0 | 042700(3), 089030(2), 039030(1), 058470(1), 095340(1) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 10 | 3 | 2024-03-08~2024-04-26 | 4/0 | 0/0 | 0/0 | 058470(2), 131290(2), 리노공업(2), 티에스이(2), 095340(1) |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 16 | 5 | 2024-01-19~2024-06-21 | 3/0 | 2/1 | 0/0 | 039030(2), 042700(2), 095340(2), 이오테크닉스(2), 한미반도체(2) |
| C11_BATTERY_ORDERBOOK_RERATING | 14 | 6 | 2023-01-31~2024-06-24 | 6/2 | 0/1 | 0/0 | 247540(6), 003670(3), 348370(2), 066970(1), 373220(1) |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 15 | 9 | 2023-01-31~2024-07-25 | 4/0 | 0/0 | 0/0 | UNKNOWN_SYMBOL(4), 247540(2), 278280(2), 003670(1), 005070(1) |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 16 | 3 | 2022-05-25~2025-04-08 | 2/9 | 1/0 | 0/0 | 006400(7), 373220(7), 096770(2) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 23 | 5 | 2023-07-26~2024-12-20 | 0/0 | 3/5 | 0/0 | 066970(6), 247540(6), 003670(5), 373220(4), 006400(2) |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 10 | 7 | 2020-08-10~2024-05-21 | 4/0 | 0/0 | 0/0 | 006260(2), 011170(2), 103140(2), 006650(1), 011780(1) |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 7 | 4 | 2019-05-20~2023-10-23 | 2/0 | 0/0 | 0/0 | 005290(2), 027580(2), 047400(2), 093370(1) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 29 | 8 | 2020-08-03~2024-07-15 | 10/5 | 0/0 | 0/0 | 298020(7), 011780(5), 010060(3), 011170(3), 004000(2) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 74 | 10 | 2023-02-10~2024-12-16 | 20/9 | 4/5 | 0/0 | 003230(18), 005180(12), 004370(10), 383220(8), 161890(6) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 39 | 8 | 2022-05-16~2024-10-02 | 8/8 | 7/4 | 0/0 | UNKNOWN_SYMBOL(8), 036620(6), 298540(6), 383220(6), 337930(5) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 133 | 16 | 2022-11-15~2024-11-14 | 47/8 | 11/5 | 0/0 | 257720(38), 018290(16), 003230(14), 090430(12), 237880(12) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 150 | 19 | 2021-08-06~2025-05-26 | 52/16 | 7/0 | 0/0 | 105560(42), 323410(22), UNKNOWN_SYMBOL(21), 086790(19), 006220(11) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 103 | 8 | 2023-05-15~2025-05-30 | 35/16 | 5/1 | 8/8 | 000810(28), 005830(28), 088350(15), 001450(12), 000400(8) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 68 | 11 | 2019-02-07~2024-12-17 | 18/3 | 5/7 | 0/0 | 000100(20), 028300(17), UNKNOWN_SYMBOL(14), 145020(9), 196170(3) |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 39 | 14 | 2019-08-02~2024-11-20 | 15/2 | 1/5 | 0/7 | 000100(6), 028300(5), 009420(4), 039200(4), UNKNOWN_SYMBOL(4) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 54 | 10 | 2022-05-16~2024-02-20 | 23/7 | 4/2 | 0/0 | 338220(15), 214150(12), 145720(7), 228670(6), 328130(4) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 65 | 10 | 2020-04-27~2024-07-11 | 28/6 | 7/1 | 0/0 | 067160(11), 035420(7), 035720(7), 089600(6), 216050(5) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 51 | 19 | 2016-03-24~2024-05-10 | 16/3 | 8/4 | 0/0 | 035900(7), 253450(5), 352820(5), 122870(4), 036420(3) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 64 | 12 | 2019-05-27~2024-04-29 | 18/4 | 9/2 | 0/0 | 012510(15), 053800(13), 263860(11), 131370(5), 030520(3) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 36 | 15 | 2020-08-14~2024-09-09 | 10/7 | 4/2 | 0/0 | 000270(10), 204320(6), 011210(5), 005380(4), 003490(1) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 28 | 6 | 2022-01-12~2024-08-27 | 5/0 | 0/4 | 0/0 | 006360(6), 294870(5), 375500(4), UNKNOWN_SYMBOL(3), 000720(2) |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 34 | 14 | 2020-07-15~2024-07-18 | 10/10 | 1/0 | 0/0 | 112610(6), 034020(4), 336260(4), UNKNOWN_SYMBOL(4), 036460(3) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 64 | 10 | 2020-11-16~2024-12-06 | 22/13 | 12/4 | 0/0 | 010130(18), 041510(14), 000240(5), 고려아연(5), 에스엠(4) |

## 반복 위험이 높은 symbol/archetype 조합

아래 조합은 이미 대표 row가 많이 쌓여 있다. 같은 날짜/같은 trigger 반복은 피한다.

| archetype | symbol | representative rows | date range | main trigger types |
|---|---|---:|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | 42 | 2024-01-26~2025-05-26 | Stage2-Actionable(20), Stage3-Green(12), Stage4B(5), Stage4B-Overlay(2) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 257720 | 38 | 2023-05-09~2024-11-14 | Stage2-Actionable(16), Stage3-Green(9), Stage4B(4), 4B-overlay(2) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 000810 | 28 | 2023-05-15~2025-05-30 | Stage2-Actionable(15), Stage3-Green(7), 4B-local-price-only(2), Stage3-Green-label-comparison(2) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 005830 | 28 | 2023-05-15~2025-05-15 | Stage2-Actionable(15), Stage3-Green(6), 4B-local-price-only(2), 4B-overlay(2) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 323410 | 22 | 2021-08-06~2024-06-27 | Stage2-Actionable(6), Stage2-PolicyOnly(2), Stage2-Watch(2), Price-only / IPO platform-bank rerating(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | UNKNOWN_SYMBOL | 21 | 2021-08-06~2025-05-26 | Stage2-Actionable(10), Stage3-Green(3), Stage2(2), Stage3-Yellow(2) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | 20 | 2024-08-20~2024-12-17 | Stage2-Actionable(7), Stage3-Green(5), Stage4B(3), 4B(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 086790 | 19 | 2024-01-26~2024-07-03 | Stage2-Actionable(12), Stage3-Green(6), Stage3-Yellow(1) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 003230 | 18 | 2023-11-15~2024-12-16 | Stage2-Actionable(8), Stage3-Green(4), 4B-overlay(2), Stage4B-Overlay(2) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 010130 | 18 | 2024-09-13~2024-12-06 | Stage2-Actionable(9), Stage4B(4), 4B(2), 4B-overlay(1) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 028300 | 17 | 2024-03-08~2024-05-20 | 4C(6), Stage3-Green-candidate-blocked(2), Stage4C(2), Stage2-Actionable/False-Green stress(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 018290 | 16 | 2023-08-14~2024-06-13 | Stage2-Actionable(10), Stage3-Green(5), Stage4B(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 088350 | 15 | 2024-01-24~2025-02-13 | Stage2-Actionable(7), 4B(2), 4B overlay(1), Stage2(1) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 338220 | 15 | 2023-02-24~2023-09-07 | Stage2-Actionable(7), Stage4B(3), Stage4B-Overlay(2), 4B(1) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 012510 | 15 | 2019-05-27~2024-04-29 | Stage2-Actionable(7), Stage3-Green(4), Stage4B-Overlay(2), Stage3-Green-label-comparison(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 003230 | 14 | 2023-11-15~2024-06-18 | Stage2-Actionable(7), Stage3-Green(4), Stage4B(2), 4B(1) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | UNKNOWN_SYMBOL | 14 | 2019-02-07~2024-10-15 | Stage2-Actionable(6), 4C(3), 4B(1), Stage2-Actionable/False-Green stress(1) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 041510 | 14 | 2023-02-10~2023-03-08 | Stage2-Actionable(7), Stage4B(4), 4B(1), 4B-overlay(1) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 053800 | 13 | 2022-01-05~2022-04-15 | Stage4B(3), False-Stage2-Actionable(2), Stage4B-Overlay(2), 4B-overlay / false-positive-check(1) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 005180 | 12 | 2024-04-01~2024-06-11 | Stage2-Actionable(6), 4B-overlay(2), 4B(1), 4B-overlay/label-comparison(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 090430 | 12 | 2024-04-26~2024-08-07 | Stage3-Yellow / false Green candidate(2), Stage4C(2), 4C-ThesisBreak(1), Stage2(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 237880 | 12 | 2023-08-10~2024-11-11 | Stage2-Actionable(6), Stage4C(3), Stage2(1), Stage3-Yellow(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 001450 | 12 | 2023-05-15~2025-02-14 | Stage2-Actionable(6), 4C protection(1), Stage2-Actionable(false)(1), Stage2-Actionable_false_positive_test(1) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 214150 | 12 | 2023-05-02~2023-09-06 | Stage2-Actionable(7), Stage3-Green(5) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 006220 | 11 | 2024-01-24~2024-04-19 | Stage4B-Overlay(2), 4B(1), 4B-overlay(1), Price-only Stage2 Candidate(1) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 067160 | 11 | 2021-05-03~2024-07-11 | Stage2-Actionable(5), 4B(2), 4B-overlay(1), Stage3-Green(1) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 263860 | 11 | 2023-01-25~2023-06-13 | Stage2-Actionable(5), Stage4B-Overlay(2), Stage3-Green(1), Stage3-Yellow(1) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 004370 | 10 | 2023-02-10~2024-11-15 | Stage2-Actionable(4), 4C(1), Stage2-Watch(1), Stage3-Yellow(1) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 000270 | 10 | 2020-10-27~2024-02-29 | Stage2-Actionable(4), Stage3-Green(4), Stage4B(1), Stage4B-price-local-only(1) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 145020 | 9 | 2024-03-04~2024-11-06 | Stage2-Actionable(5), Stage4B(3), Stage3-Green(1) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 383220 | 8 | 2023-08-01~2024-08-05 | Stage2-Actionable(3), Stage4C-Watch(2), 4C(1), Stage2-Actionable-candidate(1) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | UNKNOWN_SYMBOL | 8 | 2022-05-16~2024-02-23 | 4B(3), Stage2-Actionable(3), 4C(1), Stage3-Green-candidate(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 000400 | 8 | 2023-09-18~2024-06-28 | 4B-overlay(2), Stage2-Actionable(2), 4B event-premium overlay(1), 4C event-break protection(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 032830 | 8 | 2024-01-25~2024-11-18 | Stage2-Actionable(3), Stage3-Yellow-label-comparison(2), 4B(1), Stage3-Green(1) |

## 이미 많이 반복된 exact key 예시

아래는 검증 row 기준으로 이미 여러 번 등장한 exact key다. 새 연구에서 그대로 반복하면 dedupe 이후 기여도가 거의 없다.

| count | archetype | symbol | trigger_type | date | sample files |
|---:|---|---|---|---|---|
| 12 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 010130 | Stage2-Actionable | 2024-09-13 | e2r_stock_web_v12_residual_round_R11_loop_11_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md, e2r_stock_web_v12_residual_round_R13_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md |
| 11 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 028300 | 4C | 2024-05-17 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md, e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md |
| 10 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage2-Actionable | 2024-02-26 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md, e2r_stock_web_v12_residual_round_R13_loop_18_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md |
| 10 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | Stage2-Actionable | 2024-08-21 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md, e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md |
| 9 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 257720 | Stage3-Green | 2024-05-10 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md, e2r_stock_web_v12_residual_round_R13_loop_40_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md |
| 9 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage3-Green | 2024-04-26 | e2r_stock_web_v12_residual_round_R13_loop_30_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md, e2r_stock_web_v12_residual_round_R13_loop_47_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md |
| 9 | C22_INSURANCE_RATE_CYCLE_RESERVE | 000810 | Stage2-Actionable | 2024-02-23 | e2r_stock_web_v12_residual_round_R13_loop_20_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md, e2r_stock_web_v12_residual_round_R13_loop_20_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md |
| 9 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 145020 | Stage2-Actionable | 2024-03-04 | e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md, e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md |
| 8 | C22_INSURANCE_RATE_CYCLE_RESERVE | 005830 | Stage2-Actionable | 2024-02-23 | e2r_stock_web_v12_residual_round_R13_loop_20_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md, e2r_stock_web_v12_residual_round_R13_loop_20_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md |
| 7 | C22_INSURANCE_RATE_CYCLE_RESERVE | 000810 | Stage3-Green | 2024-05-16 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md, e2r_stock_web_v12_residual_round_R6_loop_11_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md |
| 7 | C22_INSURANCE_RATE_CYCLE_RESERVE | 005830 | Stage3-Green | 2024-05-16 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md, e2r_stock_web_v12_residual_round_R6_loop_11_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md |
| 7 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 041510 | Stage2-Actionable | 2023-02-10 | e2r_stock_web_v12_residual_round_R11_loop_11_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md, e2r_stock_web_v12_residual_round_R12_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md |
| 6 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | UNKNOWN_SYMBOL | Stage2-Actionable | 2025-04-25 | e2r_stock_web_v12_residual_round_R13_loop_22_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md, e2r_stock_web_v12_residual_round_R13_loop_22_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md |
| 6 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | Stage3-Green | 2024-08-28 | e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md, e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md |
| 5 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 237880 | Stage4C | 2024-11-11 | e2r_stock_web_v12_residual_round_R13_loop_46_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md, e2r_stock_web_v12_residual_round_R13_loop_46_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md |
| 5 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 257720 | Stage2-Actionable | 2023-11-15 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md, e2r_stock_web_v12_residual_round_R5_loop_10_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md |
| 5 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 086790 | Stage2-Actionable | 2024-02-26 | e2r_stock_web_v12_residual_round_R13_loop_18_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md, e2r_stock_web_v12_residual_round_R6_loop_10_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research(1).md |
| 5 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 086790 | Stage3-Green | 2024-04-26 | e2r_stock_web_v12_residual_round_R13_loop_47_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md, e2r_stock_web_v12_residual_round_R6_loop_60_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md |
| 5 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage2-Actionable | 2024-02-08 | e2r_stock_web_v12_residual_round_R13_loop_30_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md, e2r_stock_web_v12_residual_round_R13_loop_47_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md |
| 5 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage4B | 2024-10-25 | e2r_stock_web_v12_residual_round_R13_loop_16_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md, e2r_stock_web_v12_residual_round_R13_loop_18_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md |
| 5 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | 4B | 2024-10-15 | e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md, e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md |
| 5 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 028300 | Stage3-Green-candidate | 2024-04-25 | e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md, e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md |
| 5 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 069620 | Stage2-Actionable | 2019-02-07 | e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md, e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md |
| 5 | C24_BIO_TRIAL_DATA_EVENT_RISK | 009420 | Stage2-Actionable | 2023-09-27 | e2r_stock_web_v12_residual_round_R13_loop_32_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md, e2r_stock_web_v12_residual_round_R13_loop_32_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md |
| 5 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 000240 | Stage2-Actionable | 2023-12-05 | e2r_stock_web_v12_residual_round_R11_loop_11_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md, e2r_stock_web_v12_residual_round_R13_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md |
| 4 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 003230 | Stage2-Actionable | 2023-11-15 | e2r_stock_web_v12_residual_round_R12_loop_10_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md, e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md |
| 4 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 003230 | Stage2-Actionable | 2024-05-17 | e2r_stock_web_v12_residual_round_R5_loop_13_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md, e2r_stock_web_v12_residual_round_R5_loop_15_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md |
| 4 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 004370 | Stage2-Actionable | 2024-05-17 | e2r_stock_web_v12_residual_round_R5_loop_11_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md, e2r_stock_web_v12_residual_round_R5_loop_11_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md |
| 4 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 005180 | Stage2-Actionable | 2024-05-17 | e2r_stock_web_v12_residual_round_R5_loop_11_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md, e2r_stock_web_v12_residual_round_R5_loop_11_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md |
| 4 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 003230 | Stage2-Actionable | 2024-03-21 | e2r_stock_web_v12_residual_round_R13_loop_46_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md, e2r_stock_web_v12_residual_round_R13_loop_46_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md |

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
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | full_4b_overlay_candidate | hold_for_more_evidence | ['need_more_good_non_price_4b_timing_cases'] | collect_non_overlapping_cases |
| L7_BIO_HEALTHCARE_MEDICAL | full_4b_overlay_candidate | blocked_by_data_quality | ['full_4b_overlay_needs_verified_non_proxy_evidence'] | verify_evidence_urls_or_replace_source_proxy_rows |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | stage2_required_bridge | hold_for_more_evidence | ['guardrail_support_below_minimum'] | collect_non_overlapping_cases |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | full_4b_overlay_candidate | hold_for_more_evidence | ['need_more_good_non_price_4b_timing_cases'] | collect_non_overlapping_cases |
| C15_MATERIAL_SPREAD_SUPERCYCLE | stage2_bonus_candidate_delta | hold_for_more_evidence | ['need_3_positive_symbols_2_counterexamples_8_rows_3_transitions'] | collect_non_overlapping_cases |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | stage2_bonus_candidate_delta | hold_for_more_evidence | ['need_3_positive_symbols_2_counterexamples_8_rows_3_transitions'] | collect_non_overlapping_cases |
| C24_BIO_TRIAL_DATA_EVENT_RISK | full_4b_overlay_candidate | blocked_by_data_quality | ['full_4b_overlay_needs_verified_non_proxy_evidence'] | verify_evidence_urls_or_replace_source_proxy_rows |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | full_4b_overlay_candidate | hold_for_more_evidence | ['need_more_good_non_price_4b_timing_cases'] | collect_non_overlapping_cases |

## 새 연구 MD 작성 지침

새 v12 MD를 만들 때는 파일명과 본문 metadata에 아래 필드를 반드시 남긴다.

```text
round
loop
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

그리고 새 연구 프롬프트에는 이 문장을 넣는다.

```text
Before selecting cases, read docs/core/V12_Research_No_Repeat_Index.md.
Do not reuse the same canonical_archetype_id + symbol + trigger_type + entry_date combination.
Prefer new symbols, new trigger families, counterexamples, 4B/4C paths, or data-quality repairs.
```

## 빠른 중복 확인 명령

특정 조합이 이미 있는지 확인하려면 아래처럼 본다.

```bash
python - <<'PY'
import json
from pathlib import Path
ARCH='C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION'
SYMBOL='257720'
DATE='2024-05-10'
TRIGGER='Stage3-Green'
p=Path('data/e2r/calibration/v12/v12_trigger_rows_validated.jsonl')
hits=[]
for line in p.read_text(encoding="utf-8").splitlines():
    row=json.loads(line)
    symbol=str(row.get("symbol") or row.get("company_name") or "")
    symbol=symbol[:6] if symbol[:6].isdigit() else symbol
    date=row.get("entry_date") or row.get("trigger_date")
    if row.get("canonical_archetype_id")==ARCH and symbol==SYMBOL and date==DATE and row.get("trigger_type")==TRIGGER:
        hits.append(row.get("source_file"))
print(len(hits), hits[:5])
PY
```

## 운영 원칙

- 연구자료는 많아질수록 좋지만, 같은 exact key 반복은 거의 도움이 안 된다.
- 같은 종목을 다시 볼 수는 있다. 단, 다른 날짜, 다른 trigger family, 다른 stage transition, 4B/4C, 반례, 또는 URL 보강 목적이어야 한다.
- case label은 candidate generation input이 아니다. 이 문서는 연구 선택과 보정 검증용이다.
- 미래 가격경로는 runtime 판단에 직접 쓰지 않고, 보정 검증과 MFE/MAE 평가에만 쓴다.
- 투자 권고 문구를 만들지 않는다. Stage/monitoring 언어만 쓴다.

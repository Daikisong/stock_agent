# V12 Research No-Repeat Index

이 문서는 새 자동연구 세션을 시작할 때 먼저 읽는 중복 방지 장부다.
목적은 같은 대섹터/아키타입 안에서 **같은 종목, 같은 날짜, 같은 trigger**를 반복 연구하지 않게 하는 것이다.

쉬운 예시:

```text
이미 C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / 257720 / Stage3-Green / 2024-05-10 이 여러 번 들어왔다.
다음 연구는 같은 조합을 다시 쓰지 말고,
새 종목, 새 날짜, 새 trigger family, 또는 4B/4C/반례를 찾아야 한다.
```

last_updated: `2026-05-31`

## 원본 데이터

| source | role |
|---|---|
| `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl` | 중복제거 후 대표 trigger row |
| `data/e2r/calibration/v12/v12_trigger_rows_validated.jsonl` | 검증 통과 raw row. 반복 조합 확인용 |
| `data/e2r/calibration/v12/v12_aggregate_metrics.json` | 대섹터/아키타입 집계 |
| `data/e2r/calibration/v12/stage_transition_summary.jsonl` | Stage2, Green, 4B, 4C 전이 요약 |
| `data/e2r/calibration/v12/v12_promotion_decisions.jsonl` | apply / hold / block 결정 |

## 현재 Corpus Snapshot

| metric | value |
|---|---:|
| representative row_count | 3148 |
| validated row_count | 3667 |
| stage_transition_summary rows | 2251 |
| aggregate metric rows | 1859 |
| unique_case_count | 1971 |
| unique_symbol_count | 473 |
| unique_round_count | 13 |
| positive_case_count | 823 |
| counterexample_count | 783 |
| 4B_case_count | 679 |
| 4C_case_count | 261 |
| good_stage2_count | 945 |
| bad_stage2_count | 400 |
| source_proxy_only_count | 40 |
| evidence_url_pending_count | 27 |
| exact duplicate key count in validated rows | 746 |
| extra repeated raw rows before dedupe | 1168 |
| apply_next_patch decisions | 111 |
| hold/block decisions | 8 |

## 반영된 safe patch 축

| axis | applied decisions |
|---|---:|
| earlier_thesis_break_watch | 34 |
| full_4b_overlay_candidate | 12 |
| local_4b_watch_guard | 20 |
| stage2_bonus_candidate_delta | 2 |
| stage2_required_bridge | 43 |

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
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 8 | 6 | 2023-01-04~2024-07-31 | 5/1 | 2/0 | 0/3 | 009540(2), 010620(2), 001440(1), 010120(1), 010140(1), 267260(1) |
| C02_POWER_GRID_DATACENTER_CAPEX | 49 | 8 | 2023-01-27~2024-07-24 | 24/1 | 15/0 | 4/4 | 010120(16), 267260(12), 298040(7), 006340(4), 103590(4), UNKNOWN_SYMBOL(3) |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 74 | 14 | 2022-01-17~2024-11-12 | 30/7 | 20/1 | 0/0 | 064350(19), 272210(9), UNKNOWN_SYMBOL(9), 012450(8), 047810(5), 079550(5) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 53 | 12 | 2022-02-28~2025-01-10 | 5/9 | 21/1 | 0/0 | 094820(9), 105840(8), 032820(7), 006910(6), 034020(6), 052690(5) |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 19 | 12 | 2022-01-12~2024-03-27 | 3/7 | 0/5 | 3/3 | 006360(3), 047040(3), 000720(2), 028050(2), 375500(2), 034300(1) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 34 | 3 | 2023-05-25~2024-10-08 | 9/2 | 8/4 | 0/0 | 000660(18), 005930(11), UNKNOWN_SYMBOL(5) |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 56 | 21 | 2023-09-25~2024-10-17 | 20/4 | 16/0 | 0/0 | UNKNOWN_SYMBOL(10), 031980(6), 042700(6), 232140(6), 089030(5), 003160(4) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 66 | 14 | 2023-03-30~2024-09-26 | 21/7 | 16/1 | 0/0 | 098120(11), 058470(8), 080580(7), 095340(7), 131290(7), 219130(6) |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 50 | 21 | 2024-01-19~2024-07-11 | 6/0 | 19/2 | 0/0 | 240810(6), 036930(5), 039030(4), 003160(3), 042700(3), 095340(3) |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 22 | 13 | 2023-03-17~2024-06-07 | 9/4 | 2/0 | 0/0 | 095610(4), 036930(3), 240810(3), 084370(2), 테스(2), 000660(1) |
| C11_BATTERY_ORDERBOOK_RERATING | 67 | 23 | 2022-08-17~2024-07-22 | 24/5 | 17/5 | 0/0 | 247540(11), 003670(8), 393890(8), 348370(6), 066970(5), 222080(4) |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 53 | 17 | 2023-01-26~2024-07-25 | 13/2 | 10/5 | 0/0 | 393890(9), 361610(7), 011790(5), 336370(5), 006110(4), UNKNOWN_SYMBOL(4) |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 37 | 7 | 2022-05-25~2025-04-08 | 8/9 | 7/2 | 0/0 | 373220(14), 006400(13), 096770(5), 003670(2), 005070(1), 020150(1) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 70 | 15 | 2023-02-22~2024-12-20 | 0/0 | 29/32 | 0/0 | 247540(13), 003670(10), 066970(10), 373220(7), 361610(6), 011790(5) |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 56 | 23 | 2020-08-10~2024-09-13 | 20/3 | 15/0 | 0/0 | 005490(9), 004020(7), 001430(4), 018470(4), 001230(3), 011170(3) |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 52 | 20 | 2019-05-20~2024-02-28 | 14/5 | 17/0 | 4/4 | 001570(7), 005490(6), 000910(5), 005290(4), 075970(4), 009520(3) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 125 | 22 | 2020-08-03~2024-07-15 | 46/15 | 26/3 | 4/0 | 298020(23), 011780(21), 006650(15), 011170(12), 010950(5), 014830(5) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 108 | 18 | 2020-03-17~2024-12-16 | 31/11 | 25/8 | 0/0 | 003230(20), 005180(14), 004370(13), 383220(8), 097950(6), 161890(6) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 68 | 13 | 2021-05-17~2024-10-16 | 15/14 | 16/7 | 0/4 | 383220(9), 111770(8), UNKNOWN_SYMBOL(8), 036620(7), 081660(7), 298540(7) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 192 | 23 | 2021-05-10~2024-12-17 | 63/20 | 38/12 | 0/0 | 257720(48), 090430(20), 003230(19), 018290(19), 051900(13), 237880(13) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 209 | 26 | 2021-08-06~2025-05-26 | 73/20 | 29/5 | 0/0 | 105560(56), 323410(31), 086790(26), UNKNOWN_SYMBOL(21), 006220(16), 055550(9) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 138 | 11 | 2023-05-15~2025-05-30 | 45/20 | 22/5 | 8/8 | 000810(34), 005830(33), 088350(17), 001450(16), 000400(11), 032830(11) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 130 | 12 | 2019-02-07~2025-03-27 | 36/5 | 22/23 | 0/0 | 000100(35), 028300(34), UNKNOWN_SYMBOL(20), 145020(16), 196170(13), 039200(2) |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 62 | 17 | 2019-08-01~2024-11-20 | 22/3 | 6/18 | 0/7 | 000100(8), 009420(8), 215600(8), 028300(7), 039200(7), 019170(4) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 83 | 17 | 2022-05-11~2024-05-09 | 35/8 | 15/4 | 0/0 | 338220(17), 214150(14), 145720(8), 099190(6), 228670(6), 335890(5) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 125 | 24 | 2020-04-24~2024-07-11 | 47/17 | 20/6 | 0/0 | 067160(24), 035420(17), 035720(16), 089600(8), NAVER(8), 216050(7) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 93 | 23 | 2016-03-24~2024-07-04 | 31/8 | 24/7 | 0/0 | 035900(12), 352820(9), 194480(7), 253450(7), 122870(6), 293490(6) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 87 | 18 | 2019-05-27~2024-07-22 | 26/6 | 21/3 | 0/0 | 012510(20), 053800(16), 263860(12), 030520(7), 131370(6), 042510(4) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 157 | 33 | 2020-08-14~2024-09-09 | 51/40 | 30/10 | 4/0 | UNKNOWN_SYMBOL(20), 000270(19), 005380(12), 204320(10), 018880(8), 161390(8) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 113 | 34 | 2021-03-11~2024-09-30 | 15/18 | 14/28 | 0/0 | 006360(13), UNKNOWN_SYMBOL(13), 294870(12), 047040(11), 000720(8), 375500(6) |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 155 | 63 | 2020-01-20~2024-07-31 | 38/32 | 35/0 | 0/7 | UNKNOWN_SYMBOL(15), 036460(8), 112610(7), 005380(5), 005860(5), 218150(5) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 122 | 20 | 2020-11-16~2024-12-06 | 45/23 | 35/11 | 0/0 | 010130(31), 041510(26), 011200(11), 008930(9), UNKNOWN_SYMBOL(8), 000240(5) |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 368 | 153 | 2019-08-01~2025-03-27 | 104/63 | 81/47 | 0/0 | 247540(10), 028300(9), 105560(8), 000100(7), 003670(7), 006360(7) |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 12 | 12 | 2021-02-23~2024-06-28 | 5/3 | 0/1 | 0/0 | 003230(1), 005490(1), 010780(1), 011200(1), 011790(1), 025950(1) |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 23 | 21 | 2020-11-06~2024-07-22 | 3/5 | 5/4 | 0/0 | 028300(3), 001390(1), 001570(1), 003070(1), 003310(1), 006220(1) |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 12 | 12 | 2021-07-06~2024-05-29 | 3/3 | 1/1 | 0/0 | 005930(1), 006340(1), 010120(1), 011170(1), 019170(1), 021320(1) |

## 반복 위험이 높은 symbol/archetype 조합

아래 조합은 이미 대표 row가 많이 쌓여 있다. 같은 날짜/같은 trigger 반복은 피한다.

| archetype | symbol | representative rows | date range | main trigger types |
|---|---|---:|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | 56 | 2024-01-26~2025-05-26 | Stage2-Actionable(28), Stage3-Green(13), Stage4B(5), Stage3-Green-label-comparison(2), Stage4B-Overlay(2) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 257720 | 48 | 2023-05-09~2024-11-14 | Stage2-Actionable(20), Stage3-Green(10), Stage4B(7), Stage4B-Overlay(3), 4B-overlay(2) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | 35 | 2024-08-20~2024-12-17 | Stage2-Actionable(11), Stage3-Green(10), Stage4B(4), 4B-overlay(2), Stage4B-Overlay(2) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 000810 | 34 | 2023-05-15~2025-05-30 | Stage2-Actionable(19), Stage3-Green(7), Stage4B(5), Stage3-Green-label-comparison(2), Stage4B-Overlay(1) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 028300 | 34 | 2024-03-08~2024-05-20 | 4C(9), Stage4C(6), Stage3-Green-candidate(4), Stage3-Green-candidate-blocked(2), 4C-Hard(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 005830 | 33 | 2023-05-15~2025-05-15 | Stage2-Actionable(19), Stage3-Green(7), Stage4B(3), 4B-overlay(2), Stage3-Green-label-comparison(2) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 323410 | 31 | 2021-08-06~2024-07-22 | Stage2-Actionable(9), 4C(2), Stage2-FalsePositive(2), Stage2-PolicyOnly(2), Stage2-Watch(2) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 010130 | 31 | 2024-09-13~2024-12-06 | Stage2-Actionable(16), Stage4B(6), 4B(3), 4B-overlay(3), Stage4B-Overlay(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 086790 | 26 | 2024-01-26~2024-10-25 | Stage2-Actionable(17), Stage3-Green(7), 4B-overlay(1), Stage3-Yellow(1) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 041510 | 26 | 2023-02-10~2023-03-08 | Stage2-Actionable(14), Stage4B(6), 4B(2), 4B-overlay(2), Stage2-CapGuard(1) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 067160 | 24 | 2021-04-30~2024-07-11 | Stage2-Actionable(11), Stage3-Green(4), 4B(2), Stage4B(2), Stage4B-Overlay(2) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 298020 | 23 | 2020-10-30~2024-05-17 | Stage2-Actionable(10), Stage4B(4), Stage3-Green(4), Stage4B-Overlay(2), 4B-Overlay(1) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 011780 | 21 | 2020-08-03~2024-07-15 | Stage2-Actionable(11), Stage3-Green(5), Stage4B(3), 4B-Overlay-SpreadPeak(1), Stage4B-Overlay(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | UNKNOWN_SYMBOL | 21 | 2021-08-06~2025-05-26 | Stage2-Actionable(10), Stage3-Green(3), Stage2(2), Stage3-Yellow(2), Price-only / IPO platform-bank rerating(1) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 003230 | 20 | 2023-11-15~2024-12-16 | Stage2-Actionable(9), Stage3-Green(4), Stage4B-Overlay(3), 4B-overlay(2), 4B(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 090430 | 20 | 2021-05-10~2024-08-07 | Stage2-Actionable(5), Stage2(2), Stage3-Yellow / false Green candidate(2), Stage4C(2), 4C(1) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | UNKNOWN_SYMBOL | 20 | 2019-02-07~2024-11-06 | Stage2-Actionable(8), 4C(3), Stage3-Green(2), Stage3-Yellow(2), 4B(1) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 012510 | 20 | 2019-05-27~2024-07-08 | Stage2-Actionable(10), Stage3-Green(5), Stage4B-Overlay(2), Stage3-Green-label-comparison(1), Stage3-Yellow(1) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | UNKNOWN_SYMBOL | 20 | 2020-08-14~2024-06-27 | Stage2-Actionable(13), Stage4B-Overlay(3), Stage4B(2), Stage4C-ThesisBreak(2) |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 064350 | 19 | 2022-07-27~2023-07-05 | Stage2-Actionable(13), Stage4B(5), Stage3-Yellow(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 003230 | 19 | 2023-11-15~2024-12-17 | Stage2-Actionable(10), Stage3-Green(4), 4B(2), Stage4B(2), 4B_overlay(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 018290 | 19 | 2023-08-14~2024-09-20 | Stage2-Actionable(11), Stage3-Green(7), Stage4B(1) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 000270 | 19 | 2020-10-26~2024-06-19 | Stage2-Actionable(9), Stage3-Green(4), Stage4B(2), 4C-thesis-break(1), Stage2-rumor-redteam(1) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 | 18 | 2023-05-25~2024-07-11 | Stage2-Actionable(8), Stage4B(5), Stage3-Green(3), Stage4B-Overlay(1), Stage4B-Watch(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 088350 | 17 | 2024-01-24~2025-02-13 | Stage2-Actionable(7), 4B(2), 4B overlay(1), Stage2(1), Stage2-Actionable / watch(1) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 338220 | 17 | 2023-02-24~2023-09-07 | Stage2-Actionable(8), Stage4B(4), Stage4B-Overlay(2), 4B(1), Stage3-Green(1) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 035420 | 17 | 2020-04-24~2024-05-03 | Stage2-Actionable(11), Stage3-Green(4), Stage2-Watch(1), Stage3-Yellow(1) |
| C02_POWER_GRID_DATACENTER_CAPEX | 010120 | 16 | 2024-01-03~2024-07-24 | Stage2-Actionable(7), Stage4B(5), 4B(1), Stage3-Green(1), Stage3-Yellow(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 006220 | 16 | 2023-01-17~2024-04-19 | 4B(2), Price-only-blowoff / blocked Stage2 candidate(2), Stage2-Actionable(2), Stage4B-Overlay(2), 4B-overlay(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 001450 | 16 | 2023-05-15~2025-02-14 | Stage2-Actionable(6), Stage2-Actionable_false(2), 4C protection(1), Stage2-Actionable(false)(1), Stage2-Actionable_ca... |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 145020 | 16 | 2024-03-04~2024-11-06 | Stage2-Actionable(10), Stage4B(4), 4B-overlay(1), Stage3-Green(1) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 035720 | 16 | 2020-05-07~2024-01-11 | Stage2-Actionable(7), Stage4C-ThesisBreak(2), 4B overlay(1), 4B(1), 4C(1) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 053800 | 16 | 2022-01-05~2022-04-15 | Stage4B(3), False-Stage2-Actionable(2), Stage2-FalsePositiveCandidate(2), Stage4B-Overlay(2), 4B-overlay / false-posi... |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 006650 | 15 | 2021-01-06~2024-01-25 | Stage2-Actionable(5), Stage4C(3), Stage3-Yellow(3), Stage3-Green(2), Stage2(1) |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | UNKNOWN_SYMBOL | 15 | 2020-01-21~2024-02-27 | Stage2-Actionable(11), Stage4B(3), Stage3-Green(1) |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 373220 | 14 | 2022-08-12~2025-04-08 | Stage2-Actionable(9), 4C-Thesis-Break-Watch(2), Stage3-Yellow(1), Stage4B-Overlay(1), Stage4B-Watch(1) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 005180 | 14 | 2024-04-01~2024-06-11 | Stage2-Actionable(7), 4B-overlay(2), Stage4B(2), 4B(1), 4B-overlay/label-comparison(1) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 214150 | 14 | 2023-05-02~2024-05-09 | Stage2-Actionable(8), Stage3-Green(5), Stage4B(1) |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 006400 | 13 | 2022-05-25~2024-12-03 | Stage2-Actionable(5), 4B(2), Stage2-Headline-JV(2), Stage3-Yellow(2), 4B-Overlay-PriceOnly-LocalPeak(1) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 247540 | 13 | 2023-07-26~2024-11-06 | Stage4B(4), Stage4C(2), 4B-Overlay-PriceOnly-LocalPeak(1), 4C-Thesis-Break-Watch(1), 4C-Thesis-Break-Watch-ReusedComp... |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 004370 | 13 | 2020-03-17~2024-11-15 | Stage2-Actionable(6), 4C(1), Stage2-Watch(1), Stage3-Green(1), Stage3-Yellow(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 051900 | 13 | 2021-06-24~2024-05-23 | Stage2-Actionable(4), 4C(2), Stage4C(2), Stage2 false reopen(1), Stage2-Watch(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 237880 | 13 | 2023-08-10~2024-11-11 | Stage2-Actionable(7), Stage4C(3), Stage2(1), Stage3-Yellow(1), Stage4B(1) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 196170 | 13 | 2024-02-22~2025-03-27 | Stage2-Actionable(8), Stage3-Green(2), Stage4B-Overlay(2), Stage4B(1) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 006360 | 13 | 2023-04-21~2024-08-27 | 4B-overlay(3), Stage4C(3), 4C(2), Stage2-Actionable(2), Stage2-Actionable-Cap(1) |

## 이미 많이 반복된 exact key 예시

아래는 검증 row 기준으로 이미 여러 번 등장한 exact key다. 새 연구에서 그대로 반복하면 dedupe 이후 기여도가 거의 없다.

| count | archetype | symbol | trigger_type | date | sample files |
|---:|---|---|---|---|---|
| 21 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 010130 | Stage2-Actionable | 2024-09-13 | e2r_stock_web_v12_residual_round_R11_loop_11_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDE... |
| 16 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 041510 | Stage2-Actionable | 2023-02-10 | e2r_stock_web_v12_residual_round_R11_loop_11_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDE... |
| 14 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 028300 | 4C | 2024-05-17 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT... |
| 14 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 145020 | Stage2-Actionable | 2024-03-04 | e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_... |
| 13 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | Stage2-Actionable | 2024-08-21 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT... |
| 12 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage2-Actionable | 2024-02-26 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT... |
| 11 | C22_INSURANCE_RATE_CYCLE_RESERVE | 000810 | Stage2-Actionable | 2024-02-23 | e2r_stock_web_v12_residual_round_R13_loop_20_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_res... |
| 10 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 257720 | Stage3-Green | 2024-05-10 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT... |
| 10 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage2-Actionable | 2024-02-08 | e2r_stock_web_v12_residual_round_R13_loop_30_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN... |
| 10 | C22_INSURANCE_RATE_CYCLE_RESERVE | 005830 | Stage2-Actionable | 2024-02-23 | e2r_stock_web_v12_residual_round_R13_loop_20_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_res... |
| 9 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage3-Green | 2024-04-26 | e2r_stock_web_v12_residual_round_R13_loop_30_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN... |
| 9 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 067160 | Stage2-Actionable | 2023-12-07 | e2r_stock_web_v12_residual_round_R13_loop_16_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERA... |
| 8 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 008930 | Stage2-Actionable | 2024-01-15 | e2r_stock_web_v12_residual_round_R11_loop_11_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDE... |
| 7 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 064350 | Stage2-Actionable | 2022-07-29 | e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_armored... |
| 7 | C22_INSURANCE_RATE_CYCLE_RESERVE | 000810 | Stage3-Green | 2024-05-16 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT... |
| 7 | C22_INSURANCE_RATE_CYCLE_RESERVE | 005830 | Stage3-Green | 2024-05-16 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT... |
| 7 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 196170 | Stage2-Actionable | 2024-02-23 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT... |
| 7 | C24_BIO_TRIAL_DATA_EVENT_RISK | 009420 | Stage2-Actionable | 2023-09-27 | e2r_stock_web_v12_residual_round_R13_loop_32_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md, e2r... |
| 6 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 086790 | Stage2-Actionable | 2024-02-26 | e2r_stock_web_v12_residual_round_R13_loop_18_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN... |
| 6 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | UNKNOWN_SYMBOL | Stage2-Actionable | 2025-04-25 | e2r_stock_web_v12_residual_round_R13_loop_22_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN... |
| 6 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | Stage3-Green | 2024-08-28 | e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_... |
| 6 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 028300 | Stage4C | 2024-05-17 | e2r_stock_web_v12_residual_round_R7_loop_26_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_r... |
| 6 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 294870 | 4C | 2022-01-12 | e2r_stock_web_v12_residual_round_R10_loop_10_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BRE... |
| 5 | C02_POWER_GRID_DATACENTER_CAPEX | 267260 | Stage2-Actionable | 2024-01-03 | e2r_stock_web_v12_residual_round_R1_loop_10_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_researc... |
| 5 | C02_POWER_GRID_DATACENTER_CAPEX | 298040 | Stage2-Actionable | 2024-01-03 | e2r_stock_web_v12_residual_round_R1_loop_10_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_researc... |
| 5 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 272210 | Stage3-Yellow | 2022-07-29 | e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_defense... |
| 5 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 | Stage4B | 2024-07-11 | e2r_stock_web_v12_no_repeat_standalone_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_hbm_customer_... |
| 5 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 247540 | Stage4B | 2023-07-26 | e2r_stock_web_v12_residual_round_R13_loop_55_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md, e... |
| 5 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 003230 | Stage2-Actionable | 2023-11-15 | e2r_stock_web_v12_residual_round_R12_loop_10_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_resea... |
| 5 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 005180 | Stage2-Actionable | 2024-05-17 | e2r_stock_web_v12_residual_round_R5_loop_11_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_resear... |
| 5 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 003230 | Stage2-Actionable | 2024-05-17 | e2r_stock_web_v12_residual_round_R5_loop_11_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_resear... |
| 5 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 237880 | Stage4C | 2024-11-11 | e2r_stock_web_v12_residual_round_R13_loop_46_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_resea... |
| 5 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 257720 | Stage2-Actionable | 2023-11-15 | e2r_stock_web_v12_residual_round_R13_loop_14_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT... |
| 5 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 257720 | Stage4B | 2024-06-19 | e2r_stock_web_v12_residual_round_R5_loop_14_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_resear... |
| 5 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 055550 | Stage2-Actionable | 2024-02-26 | e2r_stock_web_v12_residual_round_R13_loop_25_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN... |
| 5 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 086790 | Stage2-Actionable | 2024-02-27 | e2r_stock_web_v12_residual_round_R6_loop_35_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_... |
| 5 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 086790 | Stage3-Green | 2024-04-26 | e2r_stock_web_v12_residual_round_R13_loop_47_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN... |
| 5 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage2-Actionable | 2024-02-27 | e2r_stock_web_v12_residual_round_R6_loop_35_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_... |
| 5 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage4B | 2024-10-25 | e2r_stock_web_v12_residual_round_R13_loop_16_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN... |
| 5 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000100 | 4B | 2024-10-15 | e2r_stock_web_v12_residual_round_R13_loop_31_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_... |

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
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| L3_BATTERY_EV_GREEN_MOBILITY | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| L5_CONSUMER_BRAND_DISTRIBUTION | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| L7_BIO_HEALTHCARE_MEDICAL | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | full_4b_overlay_candidate | hold_for_more_evidence | need_more_good_non_price_4b_timing_cases | collect_non_overlapping_cases |
| C11_BATTERY_ORDERBOOK_RERATING | full_4b_overlay_candidate | hold_for_more_evidence | need_more_good_non_price_4b_timing_cases | collect_non_overlapping_cases |
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

# V12 Research No-Repeat Index

이 문서는 새 자동연구 세션을 시작할 때 먼저 읽는 중복 방지 장부다.
목적은 같은 대섹터/아키타입 안에서 **같은 종목, 같은 날짜, 같은 trigger**를 반복 연구하지 않게 하는 것이다.

쉬운 예시:

```text
이미 C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / 257720 / Stage3-Green / 2024-05-10 이 들어왔다.
다음 연구는 같은 조합을 다시 쓰지 말고, 새 종목, 새 날짜, 새 trigger family, 또는 4B/4C/반례를 찾아야 한다.
```

last_updated: `2026-06-03`

## 원본 데이터

| source | role |
|---|---|
| `data/e2r/calibration/v12/v12_md_registry.jsonl` | 이번 실행에 실제 ingest된 연구 MD 목록 |
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
| v12 result MD | 284 |
| parser failures | 0 |
| metadata missing docs | 0 |
| unknown large sector docs | 0 |
| unknown archetype docs | 0 |
| archive docs included | 0 |
| suffix-named docs included | 131 |
| representative rows | 1121 |
| validated rows | 1216 |
| raw trigger rows | 1915 |
| raw aggregate metric rows | 3 |
| raw shadow weight rows | 646 |
| active profile selector | `e2r_2_2` |
| rolling profile id | `e2r_2_2_rolling_calibrated` |
| rollback profile | `calibrated` |
| production default scoring changed | `true` |
| archive policy | `docs/round/achieve`와 `docs/round/achieve_v12`는 완료 보관분으로 제외 |
| suffix policy | 파일명 `(1)`, `(2)`, `(3)`은 제외 기준이 아님. 내용이 다르면 각각 ingest |
| R13 review rows | `r13_cross_case`, `r13_review_trigger`는 `trigger`로 수용하되 `do_not_count_as_new_case=true`로 중복 가중치 차단 |

예를 들어 같은 loop에 `research.md`, `research(1).md`, `research(2).md`가 있어도 파일명만 보고 버리지 않는다. 실제 중복 여부는 row의 `canonical_archetype_id + symbol + trigger_type + entry_date`와 dedupe 결과로 판단한다.

R13 교차검증 row는 새 독립 케이스로 세지 않는다. 예를 들어 R5에서 이미 다룬 코스맥스 row가 R13 guardrail 검증에 다시 나오면, 검증 근거로는 읽지만 새 C20 positive 1개로 중복 계산하지 않는다.

## 현재 Corpus Snapshot

| metric | value |
|---|---:|
| representative row_count | 1121 |
| validated row_count | 1216 |
| stage_transition_summary rows | 963 |
| aggregate metric rows | 787 |
| raw aggregate metric rows | 3 |
| raw shadow weight rows | 646 |
| unique_case_count | 705 |
| unique_symbol_count | 448 |
| unique_round_count | 13 |
| large_sectors_covered | 10 |
| canonical_archetypes_covered | 36 |
| positive_case_count | 221 |
| counterexample_count | 269 |
| 4B_case_count | 70 |
| 4C_case_count | 18 |
| good_stage2_count | 428 |
| bad_stage2_count | 250 |
| source_proxy_only_count | 303 |
| evidence_url_pending_count | 327 |
| exact duplicate key count in validated rows | 159 |
| extra repeated raw rows before dedupe | 173 |
| apply_next_patch decisions | 89 |
| hold/block decisions | 4 |

## 반영된 safe patch 축

| axis | applied decisions |
|---|---:|
| earlier_thesis_break_watch | 10 |
| hard_4c_confirmation | 2 |
| local_4b_watch_guard | 31 |
| stage2_bonus_candidate_delta | 1 |
| stage2_required_bridge | 45 |

## 주요 rejected reason

Rejected row는 버리는 데이터가 아니라 다음 정규화 TODO다. 예를 들어 `missing_required_mfe_mae`는 가격경로 30D/90D/180D가 부족해서 score 보정에 못 쓴다는 뜻이다.

| reason | rows |
|---|---:|
| missing_required_mfe_mae | 467 |
| missing_trigger_type | 465 |
| not_usable_for_promotion | 272 |
| not_representative_for_aggregate | 208 |
| price_only_no_evidence | 97 |
| missing_entry_price | 28 |
| invalid_price_source | 24 |
| missing_entry_date | 24 |
| insufficient_forward_window | 4 |
| corporate_action_contaminated | 1 |

## 연구 시작 전 중복 판정 규칙

| 구분 | 판정 | 행동 |
|---|---|---|
| Hard duplicate | `canonical_archetype_id + symbol + trigger_type + entry_date`가 이미 있음 | 연구 금지. 새 케이스로 세지 말 것 |
| Soft duplicate | 같은 `canonical_archetype_id + symbol`이지만 날짜/trigger가 다름 | 새 증거 family, 새 Stage transition, 4B/4C, 반례일 때만 허용 |
| Useful expansion | 같은 archetype의 새 symbol 또는 새 failure mode | 우선 연구 |
| Data-quality repair | 기존 row가 `evidence_url_pending` 또는 `source_proxy_only` | 같은 케이스라도 URL/공시/리포트 검증 보강이면 허용 |
| Bad expansion | 가격만 있고 비가격 증거가 없음 | Stage2/Green 연구로 쓰지 말고 4B watch/반례 목적만 허용 |
| Unknown symbol | symbol이 `UNKNOWN_SYMBOL` 또는 비어 있음 | 새 연구보다 먼저 symbol 정규화 보강 |
| Filename suffix | `(1)`, `(2)`, `(3)` suffix만으로 중복 취급하지 않음 | 내용/row key 기준으로 판정 |

## 아키타입별 현재 커버리지

| archetype | rows | symbols | date range | good/bad S2 | 4B/4C | URL pending/proxy | top covered symbols |
|---|---:|---:|---|---|---|---|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 25 | 14 | 2023-01-31~2024-08-30 | 16/4 | 1/0 | 8/8 | 042660(5), 071970(3), 100090(3), 329180(3), 010140(2), 009540(1) |
| C02_POWER_GRID_DATACENTER_CAPEX | 22 | 12 | 2024-01-03~2024-07-09 | 11/4 | 2/0 | 6/6 | 000500(3), 006340(3), 033100(3), 001440(2), 017040(2), 189860(2) |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 21 | 12 | 2022-07-28~2024-09-20 | 11/3 | 0/0 | 7/7 | 079550(4), 047810(3), 065450(3), 005870(2), 103140(2), 003570(1) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 12 | 7 | 2022-03-10~2025-01-17 | 5/3 | 1/0 | 0/0 | 011700(4), 083650(3), 006910(1), 034020(1), 042370(1), 046120(1) |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 10 | 9 | 2023-03-31~2024-07-12 | 3/4 | 0/0 | 0/0 | 053690(2), 002150(1), 011560(1), 023350(1), 023960(1), 054930(1) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 7 | 6 | 2023-09-14~2024-07-05 | 4/1 | 0/0 | 3/0 | 000660(2), 005930(1), 009150(1), 014680(1), 067310(1), 402340(1) |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 11 | 9 | 2024-02-13~2024-06-14 | 7/0 | 1/0 | 0/0 | 042700(2), 064760(2), 003160(1), 036200(1), 036540(1), 039440(1) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 21 | 11 | 2024-01-23~2024-08-01 | 9/5 | 2/0 | 3/3 | UNKNOWN_SYMBOL(6), 089030(2), 095340(2), 131290(2), 252990(2), 058470(1) |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 17 | 11 | 2023-07-14~2024-09-24 | 7/3 | 1/0 | 7/7 | 322310(3), 348210(3), 089030(2), 140860(2), 031980(1), 064290(1) |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 29 | 18 | 2023-03-31~2024-06-14 | 15/5 | 1/0 | 16/10 | 089970(3), 281820(3), 319660(3), 042700(2), 064290(2), 079370(2) |
| C11_BATTERY_ORDERBOOK_RERATING | 21 | 14 | 2023-01-31~2024-06-21 | 8/4 | 1/0 | 10/10 | 137400(4), 299030(3), 003670(2), 302430(2), 001570(1), 005070(1) |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 28 | 11 | 2022-01-13~2024-07-02 | 9/6 | 0/0 | 13/9 | 121600(7), 278280(5), 020150(4), 348370(3), 091580(2), 137400(2) |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 23 | 16 | 2023-01-31~2024-07-16 | 9/2 | 2/0 | 10/10 | 005070(3), 020150(3), 003670(2), 025900(2), 348370(2), 002710(1) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 21 | 14 | 2023-01-31~2025-03-05 | 3/3 | 6/4 | 3/3 | 006400(3), 373220(3), 095500(2), 247540(2), 278280(2), 003670(1) |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 28 | 11 | 2024-01-10~2024-05-21 | 13/0 | 3/0 | 9/9 | 103140(6), 012800(5), 025820(5), 004560(3), 021050(3), 001780(1) |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 36 | 23 | 2022-10-20~2024-10-11 | 14/9 | 2/0 | 17/17 | 047400(6), 005490(3), 012320(3), 001570(2), 081150(2), 101670(2) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 21 | 15 | 2020-08-07~2024-03-21 | 8/3 | 4/0 | 0/0 | 004000(3), 006650(2), 011780(2), 014680(2), 298020(2), 001390(1) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 38 | 19 | 2023-01-18~2024-06-26 | 17/9 | 0/0 | 10/10 | 001680(4), 280360(4), UNKNOWN_SYMBOL(4), 049770(3), 271560(3), 003960(2) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 38 | 13 | 2022-02-11~2024-09-27 | 8/9 | 3/0 | 23/17 | 282330(9), 004170(4), 007070(4), 093050(4), 337930(4), 139480(3) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 19 | 11 | 2023-01-30~2024-06-14 | 8/2 | 4/0 | 7/0 | 226320(3), 161890(2), 192820(2), 214420(2), 241710(2), 439090(2) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 51 | 19 | 2021-08-06~2024-09-26 | 22/11 | 7/0 | 11/14 | 006220(5), 016360(5), 071050(4), 105560(4), 138040(4), 139130(4) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 37 | 12 | 2024-01-24~2024-08-22 | 10/11 | 2/0 | 10/10 | 000370(7), 003690(7), 082640(6), 000540(4), 000810(3), 005830(3) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 26 | 14 | 2022-06-29~2024-08-21 | 8/5 | 0/2 | 0/0 | UNKNOWN_SYMBOL(6), 028300(4), 000100(2), 039200(2), 195940(2), 003850(1) |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 30 | 20 | 2022-01-12~2024-08-26 | 13/9 | 0/2 | 10/10 | 298380(3), 323990(3), 007390(2), 087010(2), 141080(2), 226950(2) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 33 | 16 | 2023-02-13~2024-07-16 | 13/6 | 3/2 | 13/7 | 336570(6), 100120(3), 060280(2), 099190(2), 145720(2), 214150(2) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 13 | 10 | 2023-12-06~2024-07-23 | 2/6 | 0/1 | 0/0 | 042000(2), 214270(2), 237820(2), 030000(1), 035420(1), 035720(1) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 39 | 15 | 2021-01-22~2024-09-26 | 20/6 | 3/1 | 6/6 | 263750(5), 112040(4), 122870(4), 293490(4), 259960(3), 376300(3) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 26 | 19 | 2022-03-23~2024-09-04 | 10/4 | 0/0 | 10/10 | 058970(3), 150900(3), 042510(2), 203650(2), 307950(2), 012510(1) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 60 | 27 | 2021-01-08~2024-08-26 | 26/13 | 6/0 | 3/3 | 011210(7), 000270(5), 005380(5), 005850(5), 010690(5), 018880(3) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 81 | 31 | 2022-01-12~2024-08-26 | 16/29 | 3/4 | 20/25 | 002990(6), 294870(6), 375500(6), 004960(5), 013580(5), 006360(4) |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 97 | 70 | 2020-01-23~2025-01-17 | 35/25 | 5/0 | 25/25 | 013990(4), 003550(3), 015760(3), 032350(3), 114090(3), 000270(2) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 41 | 22 | 2020-02-12~2024-10-31 | 16/12 | 3/0 | 8/8 | 010130(4), 036560(4), 000150(3), 041510(3), 241560(3), 000990(2) |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 35 | 29 | 2020-02-26~2025-01-17 | 10/18 | 4/2 | 0/0 | 263750(3), 007390(2), 136480(2), 294870(2), 950140(2), 000990(1) |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 19 | 16 | 2022-10-11~2024-10-31 | 8/5 | 2/0 | 0/0 | 006220(2), 010130(2), 041510(2), 005380(1), 017040(1), 025820(1) |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 30 | 29 | 2022-03-10~2024-10-14 | 9/9 | 0/0 | 8/8 | 014790(2), 000670(1), 002780(1), 002990(1), 003230(1), 006910(1) |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 55 | 47 | 2024-01-03~2024-09-12 | 25/2 | 0/0 | 51/51 | 000150(3), 001040(2), 001470(2), 003550(2), 013990(2), 034730(2) |

## 반복 위험이 높은 symbol/archetype 조합

아래 조합은 이미 대표 row가 많이 쌓여 있다. 같은 날짜/같은 trigger 반복은 피한다.

| archetype | symbol | representative rows | date range | main trigger types |
|---|---|---:|---|---|
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 282330 | 9 | 2022-02-11~2024-07-12 | Stage2-Actionable(5), Stage3-Yellow(2), Stage2-FalsePositive-Candidate(1), Stage4B(1) |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 121600 | 7 | 2024-02-13~2024-07-02 | Stage2-Actionable(4), Stage2-FalsePositive(1), Stage2-FalsePositive-Candidate(1), Stage3-Yellow(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 000370 | 7 | 2024-01-25~2024-02-27 | Stage2-Actionable(5), Stage2-FalsePositive(1), Stage4B(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 003690 | 7 | 2024-01-24~2024-02-27 | Stage2-Actionable(7) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 011210 | 7 | 2021-01-21~2024-02-02 | Stage2-Actionable(5), Stage2 theme candidate(1), Stage2-FalsePositive(1) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | UNKNOWN_SYMBOL | 6 | 2024-02-13~2024-04-26 | Stage2-Actionable(4), Stage4B(2) |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 103140 | 6 | 2024-02-22~2024-04-26 | Stage2-Actionable(6) |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 047400 | 6 | 2023-04-10~2024-07-15 | Stage2-Actionable(3), Stage2-FalsePositive-Candidate(2), Stage2-FalsePositive(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 082640 | 6 | 2024-01-29~2024-06-27 | Stage2-Actionable(4), Stage2-FalsePositive(1), Stage2-FalsePositive-Candidate(1) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | UNKNOWN_SYMBOL | 6 | 2024-02-21~2024-08-21 | Stage2-Actionable(3), Stage3-Green(2), Stage4C(1) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 336570 | 6 | 2023-02-13~2024-03-26 | Stage2-Actionable(5), Stage2-FalsePositive(1) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 002990 | 6 | 2024-01-02~2024-03-15 | Stage2-Actionable(2), Stage2-FalsePositive(2), Stage2-FalsePositive-Candidate(1), Stage2-FalsePositive-PF-Overhang-NoRepairBridge(1) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 294870 | 6 | 2022-01-12~2024-08-26 | Stage2-Actionable(2), Stage4C(2), Stage3-Green(1), Stage4B(1) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 375500 | 6 | 2022-10-24~2024-07-12 | Stage2-Actionable(3), Stage2-FalsePositive(1), Stage2-Watch(1), Stage4B(1) |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 042660 | 5 | 2024-02-27~2024-08-30 | Stage2-Actionable(4), Stage4B(1) |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 278280 | 5 | 2024-01-03~2024-04-25 | Stage2-FalsePositive / CustomerCallOffRisk(2), Stage2-FalsePositive(2), Stage2-Actionable(1) |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 012800 | 5 | 2024-03-15~2024-05-21 | Stage4B(2), Stage2-Actionable(1), Stage2-FalsePositive(1), Stage2-PriceOnlyWatch(1) |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 025820 | 5 | 2024-03-15~2024-05-20 | Stage2-Actionable(2), Stage2-FalsePositive(1), Stage2-PriceOnlyWatch(1), Stage4B(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 006220 | 5 | 2022-12-16~2024-02-01 | Stage4B(3), Stage2-Actionable(2) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 016360 | 5 | 2024-01-29~2024-02-13 | Stage2-Actionable(5) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 263750 | 5 | 2021-08-26~2024-03-25 | Stage2-Actionable(3), Stage2-WatchOnly(1), Stage4B(1) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 000270 | 5 | 2023-01-26~2024-06-19 | Stage2-Actionable(3), Stage4B(2) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 005380 | 5 | 2023-01-26~2024-06-27 | Stage2-Actionable(3), Stage4B(2) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 005850 | 5 | 2023-03-23~2024-04-29 | Stage2-Actionable(5) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 010690 | 5 | 2023-03-09~2024-02-13 | Stage2-Actionable(4), Stage2-FalsePositive(1) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 004960 | 5 | 2024-01-02~2024-07-12 | Stage2-Actionable(5) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 013580 | 5 | 2024-01-02~2024-07-15 | Stage2-Actionable(5) |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 079550 | 4 | 2024-02-14~2024-09-20 | Stage2-Actionable(4) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 011700 | 4 | 2022-03-10~2024-07-18 | Stage2-Actionable(1), Stage2-FalsePositive(1), Stage2-ThemeSpike(1), Stage4B(1) |
| C11_BATTERY_ORDERBOOK_RERATING | 137400 | 4 | 2024-02-21~2024-05-29 | Stage2-Actionable(4) |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 020150 | 4 | 2024-02-13~2024-04-25 | Stage2-Actionable(2), Stage2-RiskWatch / Local4B(2) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 001680 | 4 | 2024-04-22~2024-06-10 | Stage2-Actionable(3), Stage2-Watch(1) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 280360 | 4 | 2024-04-22~2024-06-04 | Stage2-Actionable(4) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | UNKNOWN_SYMBOL | 4 | 2023-01-18~2024-05-17 | Stage2-Actionable(4) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 004170 | 4 | 2024-01-29~2024-09-27 | Stage2-Actionable(3), Stage2-FalsePositive(1) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 007070 | 4 | 2023-02-08~2024-04-18 | Stage2-Actionable(4) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 093050 | 4 | 2024-01-29~2024-03-22 | Stage2-Actionable(3), Stage2-FalsePositive(1) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 337930 | 4 | 2024-05-16~2024-07-10 | Stage2-Actionable(3), Stage4B(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 071050 | 4 | 2024-01-29~2024-02-13 | Stage2-Actionable(4) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | 4 | 2024-02-08~2024-02-08 | Stage2-Actionable(3), Stage4B(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 138040 | 4 | 2023-04-26~2024-09-26 | Stage2-Actionable(2), Stage4B(2) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 139130 | 4 | 2024-01-26~2024-02-27 | Stage2-Actionable(3), Stage2-FalsePositive(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 175330 | 4 | 2024-01-26~2024-02-27 | Stage2-Actionable(4) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 323410 | 4 | 2021-08-06~2024-02-08 | Stage2-Actionable(3), Stage4B(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 000540 | 4 | 2024-02-13~2024-02-14 | Stage2-Actionable(2), Stage2-FalsePositive(2) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 028300 | 4 | 2024-02-21~2024-05-17 | Stage4C(2), Stage2-Actionable(1), Stage2-PreApprovalBinaryEvent(1) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 112040 | 4 | 2024-02-13~2024-03-12 | Stage2-Actionable(3), Stage2-FalsePositive-Candidate(1) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 122870 | 4 | 2023-05-12~2024-02-13 | Stage2-Actionable(2), Stage2-FalsePositive(1), Stage4B(1) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 293490 | 4 | 2021-06-29~2024-01-29 | Stage2-Actionable(4) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 006360 | 4 | 2023-07-05~2024-07-17 | Stage4C(2), Stage2-Actionable(1), Stage4B(1) |

## 이미 많이 반복된 exact key 예시

아래는 검증 row 기준으로 이미 여러 번 등장한 exact key다. 새 연구에서 그대로 반복하면 dedupe 이후 기여도가 거의 없다.

| count | archetype | symbol | trigger_type | date | sample files |
|---:|---|---|---|---|---|
| 4 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 013990 | Stage2-Actionable | 2024-01-03 | e2r_stock_web_v12_residual_round_R11_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLI..., e2r_stock_web_v12_residual_round_R11_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLI..., e2r_stock_web_v12_residual_round_R12_loop_73_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLI... |
| 3 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 003160 | Stage2-Actionable | 2024-02-13 | e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP..., e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP..., e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP... |
| 3 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 036540 | Stage2-Theme | 2024-02-13 | e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP..., e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP..., e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP... |
| 3 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 042700 | Stage2-Actionable | 2024-02-13 | e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP..., e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP..., e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP... |
| 3 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 042700 | Stage4B | 2024-06-14 | e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP..., e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP..., e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP... |
| 3 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 089030 | Stage2-Actionable | 2024-02-13 | e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP..., e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP..., e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIP... |
| 3 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 281820 | Stage2-Actionable | 2024-02-27 | e2r_stock_web_v12_residual_round_R2_loop_72_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE..., e2r_stock_web_v12_residual_round_R2_loop_74_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE..., e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE... |
| 3 | C11_BATTERY_ORDERBOOK_RERATING | 137400 | Stage2-Actionable | 2024-05-29 | e2r_stock_web_v12_residual_round_R3_loop_73_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDE..., e2r_stock_web_v12_residual_round_R3_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDE..., e2r_stock_web_v12_residual_round_R9_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDE... |
| 3 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 105560 | Stage2-Actionable | 2024-02-08 | e2r_stock_web_v12_residual_round_R6_loop_72_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINAN..., e2r_stock_web_v12_residual_round_R6_loop_73_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINAN..., e2r_stock_web_v12_residual_round_R6_loop_76_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINAN... |
| 3 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | UNKNOWN_SYMBOL | Stage2-Actionable | 2024-02-21 | e2r_stock_web_v12_residual_round_R7_loop_72_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_..., e2r_stock_web_v12_residual_round_R7_loop_72_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_..., e2r_stock_web_v12_residual_round_R7_loop_72_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_... |
| 3 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 294870 | Stage4C | 2022-01-12 | e2r_stock_web_v12_residual_round_R10_loop_72_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONST..., e2r_stock_web_v12_residual_round_R10_loop_72_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONST..., e2r_stock_web_v12_residual_round_R10_loop_75_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONST... |
| 3 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 003550 | Stage2-FalsePositive-Candidate | 2024-02-27 | e2r_stock_web_v12_residual_round_R11_loop_72_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLI..., e2r_stock_web_v12_residual_round_R11_loop_76_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLI..., e2r_stock_web_v12_residual_round_R12_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLI... |
| 3 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 036560 | Stage2-Actionable | 2024-09-13 | e2r_stock_web_v12_residual_round_R11_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVE..., e2r_stock_web_v12_residual_round_R11_loop_84_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVE..., e2r_stock_web_v12_residual_round_R11_loop_86_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVE... |
| 2 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 014620 | Stage2-Actionable | 2024-07-12 | e2r_stock_web_v12_residual_round_R1_loop_85_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_B..., e2r_stock_web_v12_residual_round_R1_loop_85_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_B... |
| 2 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 023160 | Stage2-Actionable | 2024-07-12 | e2r_stock_web_v12_residual_round_R1_loop_85_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_B..., e2r_stock_web_v12_residual_round_R1_loop_85_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_B... |
| 2 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 042660 | Stage2-Actionable | 2024-02-27 | e2r_stock_web_v12_residual_round_R1_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_B..., e2r_stock_web_v12_residual_round_R1_loop_76_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_B... |
| 2 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 100090 | Stage2-FalsePositive | 2024-07-12 | e2r_stock_web_v12_residual_round_R1_loop_85_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_B..., e2r_stock_web_v12_residual_round_R1_loop_85_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_B... |
| 2 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 010820 | Stage2-Theme / high-MAE guard | 2022-10-04 | e2r_stock_web_v12_residual_round_R11_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENS..., e2r_stock_web_v12_residual_round_R11_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENS... |
| 2 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 012450 | Stage2-Actionable | 2022-07-28 | e2r_stock_web_v12_residual_round_R11_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENS..., e2r_stock_web_v12_residual_round_R11_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENS... |
| 2 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 064350 | Stage2-Actionable | 2022-07-28 | e2r_stock_web_v12_residual_round_R11_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENS..., e2r_stock_web_v12_residual_round_R11_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENS... |
| 2 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 065450 | Stage2-Theme / not Stage2-Actionable | 2022-10-04 | e2r_stock_web_v12_residual_round_R11_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENS..., e2r_stock_web_v12_residual_round_R11_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENS... |
| 2 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 079550 | Stage2-Actionable | 2024-02-14 | e2r_stock_web_v12_residual_round_R11_loop_73_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENS..., e2r_stock_web_v12_residual_round_R11_loop_76_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENS... |
| 2 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 011700 | Stage2-FalsePositive | 2024-07-18 | e2r_stock_web_v12_residual_round_R1_loop_86_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR..., e2r_stock_web_v12_residual_round_R1_loop_86_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR... |
| 2 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 046120 | Stage2-FalsePositive | 2024-07-18 | e2r_stock_web_v12_residual_round_R1_loop_86_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR..., e2r_stock_web_v12_residual_round_R1_loop_86_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR... |
| 2 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 083650 | Stage2-Actionable | 2024-07-18 | e2r_stock_web_v12_residual_round_R1_loop_86_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR..., e2r_stock_web_v12_residual_round_R1_loop_86_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR... |
| 2 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 | Stage2-Actionable | 2023-10-27 | e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR..., e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR... |
| 2 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 | Stage2-Actionable | 2024-02-13 | e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR..., e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR... |
| 2 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 005930 | Stage2-Actionable | 2024-07-05 | e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR..., e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR... |
| 2 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 009150 | Stage2-Actionable | 2024-02-13 | e2r_stock_web_v12_residual_round_R2_loop_87_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR..., e2r_stock_web_v12_residual_round_R2_loop_87_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR... |
| 2 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 014680 | Stage2-FalsePositive | 2024-02-13 | e2r_stock_web_v12_residual_round_R2_loop_87_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR..., e2r_stock_web_v12_residual_round_R2_loop_87_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR... |
| 2 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 067310 | Stage2-Theme | 2023-09-14 | e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR..., e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR... |
| 2 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 402340 | Stage2-Actionable | 2024-02-13 | e2r_stock_web_v12_residual_round_R2_loop_87_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR..., e2r_stock_web_v12_residual_round_R2_loop_87_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMOR... |
| 2 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 089030 | Stage2-Actionable | 2024-02-13 | e2r_stock_web_v12_residual_round_R2_loop_73_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST..., e2r_stock_web_v12_residual_round_R2_loop_85_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST... |
| 2 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 003160 | Stage2-Actionable | 2024-02-13 | e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE..., e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE... |
| 2 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 031980 | Stage2-Actionable | 2024-02-22 | e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE..., e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE... |
| 2 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 036540 | Stage2-Theme | 2024-02-13 | e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE..., e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE... |
| 2 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 042700 | Stage2-Actionable | 2024-02-13 | e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE..., e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE... |
| 2 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 042700 | Stage4B | 2024-06-14 | e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE..., e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE... |
| 2 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 064290 | Stage2-FalsePositive | 2024-02-20 | e2r_stock_web_v12_residual_round_R2_loop_83_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE..., e2r_stock_web_v12_residual_round_R2_loop_83_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE... |
| 2 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 079370 | Stage2-FalsePositive | 2024-02-22 | e2r_stock_web_v12_residual_round_R2_loop_83_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE..., e2r_stock_web_v12_residual_round_R2_loop_83_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE... |
| 2 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 080220 | Stage2-Actionable | 2024-01-24 | e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE..., e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE... |
| 2 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 089030 | Stage2-Actionable | 2024-02-13 | e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE..., e2r_stock_web_v12_residual_round_R2_loop_75_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE... |
| 2 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 319660 | Stage2-Actionable | 2024-02-29 | e2r_stock_web_v12_residual_round_R2_loop_83_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE..., e2r_stock_web_v12_residual_round_R2_loop_83_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RE... |
| 2 | C11_BATTERY_ORDERBOOK_RERATING | 302430 | Stage2-FalsePositive-Candidate | 2024-03-11 | e2r_stock_web_v12_residual_round_R3_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDE..., e2r_stock_web_v12_residual_round_R9_loop_76_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDE... |
| 2 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 020150 | Stage2-RiskWatch / Local4B | 2024-04-25 | e2r_stock_web_v12_residual_round_R3_loop_83_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUST..., e2r_stock_web_v12_residual_round_R3_loop_83_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUST... |

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
| canonical_archetype:C11_BATTERY_ORDERBOOK_RERATING | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |

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

가능하면 다음 운영 지표도 같이 남긴다. 지금 점수 엔진이 모든 항목을 즉시 직접 쓰는 것은 아니지만, 일주일 단위로 정규화할 때 “성장 재고”와 “채널스터핑/마진 훼손”을 구분하는 근거가 된다.

```text
inventory_growth_yoy_pct
revenue_growth_yoy_pct
opm_margin_yoy_delta_ppt
receivables_growth_yoy_pct
export_growth_yoy_pct
channel_inventory_comment
```

예를 들어 재고가 +10%인데 매출 +40%, OPM 상승이면 성장 재고일 수 있다. 반대로 재고 +45%, 매출 둔화, OPM 하락, 매출채권 증가가 같이 나오면 채널스터핑 또는 마진 훼손 위험으로 별도 guardrail 후보가 된다.

R13 cross/review checkpoint처럼 원천 row를 재검증하는 경우에도 가능하면 `entry_date`, `entry_price`, `MFE_30D_pct`, `MFE_90D_pct`, `MFE_180D_pct`, `MAE_30D_pct`, `MAE_90D_pct`, `MAE_180D_pct`를 같이 남긴다. 값이 일부만 있어도 parser는 row를 읽지만, 가격경로 검증 강도는 낮아진다.

그리고 새 연구 프롬프트에는 이 문장을 넣는다.

```text
Before selecting cases, read docs/core/V12_Research_No_Repeat_Index.md.
Do not reuse the same canonical_archetype_id + symbol + trigger_type + entry_date combination.
Prefer new symbols, new trigger families, counterexamples, 4B/4C paths, or data-quality repairs.
Do not treat filename suffixes like (1), (2), or (3) as duplicates by themselves; inspect row keys and evidence content.
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

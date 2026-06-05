# V12 Research No-Repeat Index

이 문서는 새 자동연구 세션을 시작할 때 먼저 읽는 중복 방지 장부다.
목적은 같은 대섹터/아키타입 안에서 **같은 종목, 같은 날짜, 같은 trigger**를 반복 연구하지 않게 하는 것이다.

쉬운 예시:

```text
이미 C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / 257720 / Stage3-Green / 2024-05-10 이 들어왔다.
다음 연구는 같은 조합을 다시 쓰지 말고, 새 종목, 새 날짜, 새 trigger family, 또는 4B/4C/반례를 찾아야 한다.
```

last_updated: `2026-06-06`

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
| v12 result MD | 404 |
| parser failures | 0 |
| metadata missing docs | 0 |
| unknown large sector docs | 0 |
| unknown archetype docs | 0 |
| archive docs included | 0 |
| zero trigger docs | 0 |
| suffix-named docs included | 125 |
| raw trigger rows | 2137 |
| validated rows | 1639 |
| representative rows | 1621 |
| raw aggregate metric rows | 258 |
| raw shadow weight rows | 736 |
| stage transition rows | 1591 |
| apply_next_patch decisions | 82 |
| active profile selector | `e2r_2_2` |
| rolling profile id | `e2r_2_2_rolling_calibrated` |
| rollback profile | `calibrated` |
| production default scoring changed | `true` |
| archetype weight count | 36 |
| large sector weight count | 10 |
| compact case rows synthesized | 332 |
| trigger_case rows accepted | 6 |
| cross/review rows accepted | 402 |
| review-only audit rows | 1 |
| archive policy | `docs/round/achieve`와 `docs/round/achieve_v12`는 완료 보관분으로 제외 |
| suffix policy | 파일명 `(1)`, `(2)`, `(3)`은 제외 기준이 아님. 내용이 다르면 각각 ingest |

예를 들어 같은 loop에 `research.md`, `research(1).md`, `research(2).md`가 있어도 파일명만 보고 버리지 않는다. 실제 중복 여부는 row의 `canonical_archetype_id + symbol + trigger_type + entry_date`와 dedupe 결과로 판단한다.

compact case row도 이번부터 반영된다. 예를 들어 `row_type=case`에 `entry_close`, `mfe_90d_pct`, `classification=counterexample_high_mae`가 있으면 parser가 trigger audit row로 승격하고, 반례는 positive weight 근거로 세지 않는다.

R13 교차검증 row는 새 독립 케이스로 세지 않는다. 예를 들어 R5에서 이미 다룬 코스맥스 row가 R13 guardrail 검증에 다시 나오면, 검증 근거로는 읽지만 새 C20 positive 1개로 중복 계산하지 않는다.

## 현재 Corpus Snapshot

| metric | value |
|---|---:|
| representative row_count | 1621 |
| validated row_count | 1639 |
| raw trigger rows | 2137 |
| stage_transition_summary rows | 1591 |
| aggregate metric rows | 1342 |
| raw aggregate metric rows | 258 |
| raw shadow weight rows | 736 |
| unique_case_count | 1274 |
| unique_symbol_count | 539 |
| unique_round_count | 13 |
| large_sectors_covered | 10 |
| canonical_archetypes_covered | 35 |
| positive_case_count | 141 |
| counterexample_count | 640 |
| 4B_case_count | 221 |
| 4C_case_count | 122 |
| good_stage2_count | 401 |
| bad_stage2_count | 517 |
| source_proxy_only_count | 1066 |
| evidence_url_pending_count | 1390 |
| exact duplicate key count in validated rows | 53 |
| extra repeated raw rows before dedupe | 57 |
| apply_next_patch decisions | 82 |
| hold/block decisions | 52 |

## 다음 연구 우선순위

이제 자동연구원은 R1~R13을 기계적으로 순환하지 말고, 이 문서의 아키타입별 수량과 중복 상태를 먼저 본다. Round는 연구 대상을 고른 뒤 파일명/대섹터 일관성을 맞추기 위해 따라오는 metadata다.

쉬운 예:

```text
C08은 14 row뿐이고 C29는 86 row다.
다음 연구에서 R9 순서가 왔다고 C29를 또 늘리기보다, C08/C09/C01처럼 얇은 아키타입을 먼저 채우는 편이 점수 정규화에 더 도움이 된다.
```

목표 수량 기준:

| target | meaning | current shortage |
|---|---|---:|
| 30 rows per archetype | 최소 안정권. stage/guardrail 방향성을 보기 시작할 수 있음 | 123 |
| 50 rows per archetype | 실전 보정권. positive/counterexample/4B/4C 균형을 보기 좋음 | 631 |
| 80 rows per archetype | 꽤 탄탄한 권역. 새 row 10~20개로 weight가 크게 흔들리지 않음 | 1522 |

### Priority 0: 30 row 미만부터 채우기

아래 아키타입은 아직 최소 안정권이 얇다. 새 symbol, 새 trigger family, 반례, 4B/4C path, URL 검증 보강을 우선한다.

| priority | archetype | rows | need to 30 | need to 50 | 조사 포인트 |
|---:|---|---:|---:|---:|---|
| 1 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 14 | 16 | 36 | 고객 qualification, 소모품 반복수요, socket/test margin, 납품 전환 반례 |
| 2 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 15 | 15 | 35 | 장비 valuation 과열, 수주 없는 price blowoff, 4B/4C 전환 |
| 3 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 16 | 14 | 34 | 수주잔고와 margin bridge가 같이 있는 성공/실패 분리 |
| 4 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 18 | 12 | 32 | HBM 장비 상대강도와 실제 order/revision 연결 여부 |
| 5 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 21 | 9 | 29 | 고객 CAPA, HBM mix, ASP/FCF 전환, cycle 반례 |
| 6 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 21 | 9 | 29 | 메모리 회복 beta와 실제 장비 order 전환 구분 |
| 7 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 21 | 9 | 29 | EV 수요 둔화, utilization, call-off, hard 4C 확인 |
| 8 | C11_BATTERY_ORDERBOOK_RERATING | 23 | 7 | 27 | 배터리 orderbook이 FCF/마진으로 전환되는지 검증 |
| 9 | C02_POWER_GRID_DATACENTER_CAPEX | 24 | 6 | 26 | 전력기기/데이터센터 CAPEX, backlog, CAPA lock, ASP |
| 10 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 24 | 6 | 26 | 재고/매출채권/OPM/sell-through로 성장 재고와 channel stuffing 분리 |
| 11 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 24 | 6 | 26 | IP 매출화, 글로벌 플랫폼 전환, 일회성 흥행 반례 |
| 12 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 27 | 3 | 23 | 고객 계약과 call-off/demand risk, AMPC/IRA와 분리 |
| 13 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 27 | 3 | 23 | JV 가동률, AMPC, utilization, cash conversion |
| 14 | C24_BIO_TRIAL_DATA_EVENT_RISK | 27 | 3 | 23 | 임상 데이터 이벤트, 승인 전 price spike, 실패/지연 반례 |
| 15 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 27 | 3 | 23 | 보안 계약, retention, ARR/renewal, theme beta 반례 |
| 16 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 29 | 1 | 21 | 원자재 가격과 실제 spread/margin/FCF 분리 |
| 17 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 29 | 1 | 21 | 승인 이후 상업화, 매출 전환, 보험/채널/가격 반례 |

### Priority 1: 50 row까지 끌어올리기

아래는 최소권은 거의 채웠지만 실전 보정권은 아직 부족하다. Priority 0을 먼저 채운 뒤 50 row를 목표로 보강한다.

| archetype | rows | need to 50 | 조사 포인트 |
|---|---:|---:|---|
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 30 | 20 | 방산 수출 계약, backlog, delivery schedule, margin conversion |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 30 | 20 | 전략자원 정책과 실제 offtake/margin/공급망 실행 |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 31 | 19 | 우선협상/정책 headline과 최종계약/법적 지연 분리 |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 33 | 17 | Mega EPC 계약, 원가초과, working capital, margin gap |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 33 | 17 | spread supercycle과 회사별 ASP/volume/margin 전환 |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 33 | 17 | 수출 채널, reorder, repeat demand, 재고 부담 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 33 | 17 | K-food/K-beauty 글로벌 유통, sell-through, OPM/revision |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 33 | 17 | 의료기기 수출, reimbursement, 반복 소모품 매출 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 36 | 14 | 광고/플랫폼 매출 회복과 operating leverage 확인 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 42 | 8 | 보험 rate cycle, reserve quality, capital return |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 48 | 2 | ROE/PBR/value-up과 실제 자본정책 실행 |

### Priority 2: 이미 많은 구역은 새 근거가 있을 때만

아래는 이미 50 row 이상이므로 무조건 반복하지 않는다. 새 failure mode, 새 market regime, 검증 URL 보강, hard 4C 확인처럼 중복을 줄이는 목적일 때만 추가한다.

| archetype | rows | guidance |
|---|---:|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 86 | 새 volume/mix/margin 반례가 아니면 낮은 우선순위 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 97 | PF/유동성/재무제표 hard break 검증 위주 |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 77 | 정책 headline이 실제 법/예산/회사 action으로 전환되는지 검증 |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 55 | 지배구조 premium, tender cap, minority risk 보강 |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 351 | R13 일반 반복 금지. cross-case hard 4C/4B guardrail 검증만 |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 129 | high-MAE guardrail의 새 반례/누락 검증만 |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 57 | Stage2 false positive의 새 failure family만 |

운영 규칙:

```text
1. 먼저 Priority 0에서 가장 rows가 낮은 canonical_archetype_id를 고른다.
2. 같은 symbol + trigger_type + entry_date 조합은 반복하지 않는다.
3. 새 symbol, 새 trigger family, counterexample, 4B/4C path, evidence URL 보강 순서로 가치가 높다.
4. R13은 순서가 와서 하는 round가 아니라 cross-archetype guardrail 검증이 필요할 때만 한다.
5. 연구원이 애매하면 이 문서의 Priority 0/1 표를 근거로 selected_round와 selected_archetype을 선택한다.
```

## 반영된 safe patch 축

| axis | applied decisions |
|---|---:|
| hard_4c_confirmation | 44 |
| stage2_required_bridge | 38 |

## 주요 rejected reason

Rejected row는 버리는 데이터가 아니라 다음 정규화 TODO다. 예를 들어 `missing_required_mfe_mae`는 가격경로 30D/90D/180D가 부족해서 score 보정에 못 쓴다는 뜻이다.

| reason | rows |
|---|---:|
| not_representative_for_aggregate | 573 |
| missing_required_mfe_mae | 489 |
| not_usable_for_promotion | 267 |
| missing_entry_price | 74 |
| missing_entry_date | 74 |
| price_only_no_evidence | 17 |
| missing_trigger_type | 10 |

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
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 16 | 12 | 2024-01-17~2024-07-24 | 7/3 | 2/2 | 16/9 | 082740(4), 267270(2), 010660(1), 044450(1), 054540(1), 064820(1) |
| C02_POWER_GRID_DATACENTER_CAPEX | 24 | 13 | 2024-01-24~2024-09-26 | 8/3 | 3/1 | 21/18 | 199820(4), 103590(3), 267260(3), 298040(3), 010120(2), 237750(2) |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 30 | 16 | 2024-01-03~2024-07-24 | 10/6 | 5/1 | 30/27 | 012450(3), 064350(3), 099320(3), 272210(3), 010820(2), 013810(2) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 31 | 13 | 2024-01-02~2025-04-25 | 9/7 | 3/1 | 27/21 | 052690(6), 051600(5), 105840(4), 130660(4), 094820(3), 019990(2) |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 33 | 17 | 2022-10-07~2025-01-22 | 9/6 | 5/3 | 30/24 | 028050(8), 000720(3), 100840(3), 006360(2), 028100(2), 045100(2) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 21 | 16 | 2024-01-18~2024-07-04 | 6/4 | 2/2 | 18/12 | 005290(2), 036540(2), 080220(2), 222800(2), 353200(2), 000660(1) |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 18 | 16 | 2024-01-24~2024-09-26 | 5/3 | 2/1 | 18/15 | 084370(2), 232140(2), 036200(1), 036930(1), 039030(1), 039440(1) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 14 | 11 | 2024-01-23~2024-08-01 | 4/4 | 2/2 | 14/9 | 098120(3), 080580(2), 058470(1), 067310(1), 092870(1), 097800(1) |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 15 | 11 | 2024-01-19~2024-07-04 | 6/3 | 1/2 | 15/9 | 039030(2), 084370(2), 140860(2), 240810(2), 036810(1), 036930(1) |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 21 | 18 | 2024-01-18~2024-06-26 | 6/6 | 3/3 | 18/12 | 036930(3), 074600(2), 003160(1), 031980(1), 036540(1), 039030(1) |
| C11_BATTERY_ORDERBOOK_RERATING | 23 | 16 | 2024-01-04~2024-09-23 | 7/5 | 3/4 | 23/15 | 006110(3), 382840(3), 008730(2), 078600(2), 290670(2), 020150(1) |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 27 | 21 | 2024-01-02~2025-03-05 | 9/4 | 3/3 | 24/18 | 066970(3), 361610(3), 011790(2), 078600(2), 002710(1), 003670(1) |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 27 | 17 | 2024-01-22~2024-12-16 | 6/6 | 3/3 | 24/18 | 373220(3), 393890(3), 006400(2), 014820(2), 051910(2), 096770(2) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 21 | 17 | 2023-07-26~2024-07-08 | 3/3 | 5/7 | 21/15 | 336370(3), 222080(2), 361610(2), 011790(1), 014820(1), 025900(1) |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 33 | 24 | 2024-01-02~2024-06-11 | 6/7 | 3/4 | 33/18 | 004020(3), 006110(3), 001430(2), 006260(2), 008350(2), 010060(2) |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 30 | 20 | 2023-03-03~2024-09-02 | 9/4 | 3/7 | 30/18 | 006260(4), 009520(4), 011810(3), 025820(2), 036460(2), 000670(1) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 29 | 15 | 2023-06-19~2025-02-05 | 8/6 | 3/3 | 26/21 | 009830(4), 011170(4), 010060(3), 298000(3), 001340(2), 002380(2) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 33 | 22 | 2024-01-09~2024-07-24 | 11/8 | 4/3 | 33/21 | 005180(4), 005610(3), 003230(2), 004370(2), 007310(2), 011150(2) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 24 | 12 | 2024-01-22~2024-04-12 | 5/4 | 3/3 | 21/15 | 008770(3), 023530(3), 031430(3), 069960(3), 383220(3), 020000(2) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 33 | 17 | 2024-02-01~2024-09-03 | 10/6 | 4/2 | 33/21 | 003230(4), 051900(4), 090430(4), 004370(3), 003350(2), 005180(2) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 48 | 23 | 2024-01-02~2024-08-05 | 15/10 | 6/4 | 45/30 | 006800(4), 055550(4), 086790(4), 316140(4), 001510(3), 039490(3) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 42 | 9 | 2024-01-23~2024-11-15 | 10/13 | 5/2 | 42/27 | 032830(9), 088350(9), 000400(6), 001450(6), 085620(3), 211050(3) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 29 | 20 | 2024-01-02~2024-07-24 | 11/7 | 3/2 | 26/18 | 000250(4), 086900(3), 145020(3), 068270(2), 326030(2), 003850(1) |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 27 | 17 | 2024-02-01~2024-11-20 | 11/4 | 3/3 | 27/18 | 196170(5), 950220(3), 039200(2), 206650(2), 235980(2), 365270(2) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 33 | 17 | 2024-01-02~2024-08-07 | 11/6 | 4/4 | 30/21 | 228670(7), 214450(5), 335890(4), 065510(3), 043150(2), 041830(1) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 36 | 16 | 2024-01-03~2024-05-09 | 11/6 | 3/4 | 33/21 | 067160(5), 089600(5), 230360(4), 123570(3), 216050(3), 236810(3) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 24 | 17 | 2024-01-02~2024-07-12 | 6/7 | 3/3 | 24/15 | 035760(3), 251270(3), 035900(2), 194480(2), 419530(2), 036420(1) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 27 | 15 | 2024-01-02~2024-06-25 | 6/7 | 4/2 | 27/21 | 053800(5), 030520(4), 136540(3), 047560(2), 060850(2), 356680(2) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 86 | 53 | 2023-03-31~2025-05-19 | 20/23 | 7/10 | 82/56 | 073240(5), 204320(5), 064960(4), 092200(4), 002350(3), 009900(3) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 97 | 45 | 2024-01-02~2025-03-21 | 19/27 | 12/10 | 91/64 | 034300(5), 000720(4), 005960(4), 010780(4), 047040(4), 001260(3) |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 77 | 57 | 2022-08-11~2025-06-05 | 22/17 | 8/13 | 69/36 | 052690(4), 053290(3), 130660(3), 009830(2), 034020(2), 034230(2) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 55 | 32 | 2020-02-12~2024-09-24 | 12/14 | 8/5 | 52/36 | 008930(5), 028260(4), 001040(3), 003240(3), 004990(3), 034730(3) |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 351 | 286 | 2023-10-25~2025-06-05 | 80/188 | 40/31 | 190/190 | 034300(4), 001040(3), 001260(3), 008930(3), 010780(3), 028050(3) |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 129 | 117 | 2021-07-01~2025-01-22 | 23/66 | 29/3 | 129/129 | 001470(2), 010120(2), 021320(2), 028050(2), 051900(2), 052690(2) |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 57 | 57 | 2024-01-02~2024-07-17 | 0/24 | 24/0 | 48/48 | 000240(1), 001040(1), 002290(1), 002410(1), 002780(1), 003470(1) |

## 반복 위험이 높은 symbol/archetype 조합

아래 조합은 이미 대표 row가 많이 쌓여 있다. 같은 날짜/같은 trigger 반복은 피한다.

| archetype | symbol | representative rows | date range | main trigger types |
|---|---|---:|---|---|
| C22_INSURANCE_RATE_CYCLE_RESERVE | 032830 | 9 | 2024-01-24~2024-02-28 | Stage2-Actionable(4), Stage2(3), Stage4B(1), insurance_rate_reserve_capital_return_bridge(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 088350 | 9 | 2024-01-23~2024-02-28 | Stage2(3), Stage2-Actionable(2), Stage2-FalsePositive-LifeInsuranceBetaSpike-NoCSMReturnBridge(1), Stage2-FalsePositive-LifeInsurancePriceSpikeNoDurableReservePayoutBridge(1) |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 028050 | 8 | 2023-01-31~2024-06-11 | Stage2-Actionable(5), Stage2-FalsePositive-LargeEPCRebrandContractVocabularyNoFreshMarginBridge(1), Stage2-FalsePositive-MegaContractMarginGap-WorkingCapitalBreak(1), Stage4C(1) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 228670 | 7 | 2024-01-08~2024-04-01 | Stage2-Actionable(2), Stage4C(2), Stage2-FalsePositive-Candidate(1), Stage2-FalsePositive-DentalDeviceExportSpike-NoBridge(1) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 052690 | 6 | 2024-02-01~2025-04-25 | Stage2-Actionable(3), Stage2(2), Stage2-ThemeSpike-PreferredBidder-NoFinalContract(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 000400 | 6 | 2024-02-13~2024-06-26 | Stage4B(2), Stage4C(2), Stage2-FalsePositive-NonlifeInsuranceMNAThemeNoReserveCycleCapitalReturnBridge(1), Stage2-FalsePositive-SmallcapInsuranceMnaBeta-NoReserveCapitalBridge(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 001450 | 6 | 2024-01-24~2024-02-28 | Stage2-Actionable(3), Stage2(1), Stage2-FalsePositive-NonLifeValueupSpike-ReserveQualityUnverified(1), pnc_insurance_rate_cycle_without_reserve_quality_bridge(1) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 051600 | 5 | 2024-01-24~2024-07-18 | Stage2(2), Stage2-Actionable(2), Stage2-Watch-PreferredBidder-ServiceAffiliate(1) |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 196170 | 5 | 2024-02-01~2024-11-20 | Stage2-Actionable(3), Stage2(2) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 214450 | 5 | 2024-02-23~2024-08-07 | Stage2-Actionable(5) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 067160 | 5 | 2024-01-08 | Stage2-Actionable(4), traffic_migration_plus_platform_operating_leverage(1) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 089600 | 5 | 2024-01-24~2024-04-11 | Stage4C(2), Stage2-Actionable(1), Stage2-FalsePositive-AdTechRecovery-NoOperatingLeverageBridge(1), Stage2-FalsePositive-DigitalAdAgencyBeta-NoOperatingLeverageBridge(1) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 053800 | 5 | 2024-01-22~2024-04-11 | Stage2-Actionable(2), Stage2(1), Stage2-FalsePositive-SecurityThemeBeta-NoFreshContractRetentionBridge(1), Stage4C(1) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 073240 | 5 | 2023-03-31~2025-05-19 | Stage2-Actionable(3), Stage2(1), Stage4C(1) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 204320 | 5 | 2023-07-31~2024-06-26 | Stage2-Actionable(1), Stage2-FalsePositive-ADAS-EVComponentSpike-NoMarginBridge(1), Stage2-FalsePositive-Candidate(1), Stage4B(1) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 034300 | 5 | 2024-02-07~2024-05-29 | Stage4B(3), Stage2(1), Stage2-Actionable(1) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 008930 | 5 | 2024-01-12~2024-03-28 | Stage2-Actionable(2), Stage4B(1), Stage4C(1), family_governance_control_premium_merger_headline(1) |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 082740 | 4 | 2024-02-01~2024-04-16 | Stage2-Actionable(3), Stage2(1) |
| C02_POWER_GRID_DATACENTER_CAPEX | 199820 | 4 | 2024-06-28~2024-09-20 | Stage2-Actionable(2), Stage2-FalsePositive-SwitchgearThemeSpike-NoDatacenterCapexOrderMarginBridge(1), price_only_switchgear_theme_after_split(1) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 105840 | 4 | 2024-01-15~2024-05-22 | Stage2-Actionable(2), Stage2-FalsePositive-NuclearInstrumentTheme-NoProjectBridge(1), Stage2-FalsePositive-NuclearInstrumentationThemePriceMFE-NoProjectLegalMarginBridge(1) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 130660 | 4 | 2024-04-22~2024-07-24 | Stage2-Actionable(2), Stage2-FalsePositive-PreferredBidder-ThemeProxy(1), Stage4C(1) |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 006260 | 4 | 2024-01-24~2024-04-11 | Stage2-Actionable(3), Stage2(1) |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 009520 | 4 | 2023-03-03~2024-06-11 | Stage4C(2), Stage2-Actionable(1), Stage2-FalsePositive-LithiumMaterialsThemeNoFreshSupplyMarginBridge(1) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 009830 | 4 | 2024-01-10~2024-04-01 | Stage2(1), Stage2-FalsePositive-SolarChemicalCommodityBeta-NoSpreadRecoveryBridge(1), Stage2-FalsePositive-SolarChemicalSpreadRebound-NoFCFBridge(1), Stage4C(1) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 011170 | 4 | 2024-01-24~2024-02-16 | Stage2-Actionable(1), Stage2-FalsePositive(1), Stage2-FalsePositive-PetrochemicalSpreadRebound-NoMarginBridge(1), Stage4C(1) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 005180 | 4 | 2024-02-01~2024-04-15 | Stage2-Actionable(3), Stage2(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 003230 | 4 | 2024-03-04~2024-05-17 | Stage2-Actionable(3), Stage2(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 051900 | 4 | 2024-03-21~2024-05-10 | Stage2(1), Stage2-Actionable(1), Stage2-FalsePositive-BeautyChinaReopeningRebound-NoGlobalSellthroughBridge(1), Stage2-FalsePositive-LegacyBeautyGlobalChannelVocabularyNoFreshSellthroughMarginBridge(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 090430 | 4 | 2024-04-11~2024-05-31 | Stage2-Actionable(1), Stage2-FalsePositive-BeautyLargecapChannelSpike-NoMarginReorderBridge(1), Stage2-FalsePositive-KBeauty-ChinaReboundNoRepeatSellthrough(1), Stage4C(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 006800 | 4 | 2024-01-25~2024-02-28 | Stage2-Actionable(2), Stage2-FalsePositive-Brokerage-Beta-PriceSpike-NoROEBridge(1), Stage4C(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 055550 | 4 | 2024-01-24~2024-02-02 | Stage2(2), Stage2-Actionable(2) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 086790 | 4 | 2024-01-02~2024-02-02 | Stage2-Actionable(3), Stage2(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 316140 | 4 | 2024-01-24~2024-07-26 | Stage2(1), Stage2-Actionable(1), Stage2-FalsePositive-LateBankValueupExtension-NoIncrementalCapitalReturnBridge(1), Stage2-Watch-CapitalReturnBridgeInsufficient(1) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000250 | 4 | 2024-02-01~2024-03-25 | Stage2-Actionable(3), Stage2(1) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 335890 | 4 | 2024-02-16~2024-04-25 | Stage2-Actionable(2), Stage2(1), Stage4B(1) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 230360 | 4 | 2024-02-01~2024-04-11 | Stage2(2), Stage2-Actionable(1), Stage2-FalsePositive-PerformanceMarketingRecovery-ChannelInstability(1) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 030520 | 4 | 2024-01-05~2024-04-18 | Stage2-Actionable(4) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 064960 | 4 | 2023-05-16~2024-02-06 | Stage2-Actionable(3), Stage2(1) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 092200 | 4 | 2024-02-01~2024-06-26 | Stage2-Actionable(2), Stage2(1), Stage2-FalsePositive-EVDrivetrainLateSpike-NoFreshVolumeMarginBridge(1) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 000720 | 4 | 2024-01-24~2025-01-22 | Stage2-Actionable(3), Stage2-FalsePositive-LargecapConstructionPFTheme-NoLiquidityMarginBridge(1) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 005960 | 4 | 2024-02-01~2024-04-25 | Stage2(1), Stage2-Actionable(1), Stage2-FalsePositive-ConstructionLowLiquidity-NoRepairBridge(1), Stage2-FalsePositive-PF-PolicySupport-NoRepairBridge(1) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 010780 | 4 | 2024-01-18~2024-03-27 | Stage2-Actionable(2), Stage2-FalsePositive-MixedRealEstate-NoRepairBridge(1), Stage4C(1) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 047040 | 4 | 2024-01-02~2024-07-15 | Stage2-Actionable(2), C30_POLICY_SUPPORT_PF_LIQUIDITY_BETA_WITHOUT_COMPANY_BRIDGE(1), Stage2-FalsePositive-PF-ReliefPriceSpike-NoBalanceSheetBridge(1) |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 052690 | 4 | 2024-07-10~2025-06-05 | Stage2-Actionable(2), Stage2-FalsePositive-Candidate / PreferredBidderOnlyLegalOverhang(2) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 028260 | 4 | 2024-01-24~2024-02-01 | Stage2-Actionable(4) |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 034300 | 4 | 2024-02-07~2024-05-29 | Stage4B(2), R13-Review / PriceOnlyLocal4BWatch / NonPrice4BMissing(1), Stage2(1) |
| C02_POWER_GRID_DATACENTER_CAPEX | 103590 | 3 | 2024-02-14~2024-07-15 | Stage2(1), Stage2-Actionable(1), Stage2-FalsePositive-WireTransformerBetaExtension-NoFreshOrderMarginBridge(1) |
| C02_POWER_GRID_DATACENTER_CAPEX | 267260 | 3 | 2024-01-24~2024-03-13 | Stage2-Actionable(2), transformer_backlog_margin_bridge(1) |
| C02_POWER_GRID_DATACENTER_CAPEX | 298040 | 3 | 2024-02-20~2024-03-04 | Stage2-Actionable(2), transformer_capacity_margin_bridge(1) |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 012450 | 3 | 2024-02-14~2024-02-26 | Stage2-Actionable(3) |

## 이미 많이 반복된 exact key 예시

아래는 검증 row 기준으로 이미 여러 번 등장한 exact key다. 새 연구에서 그대로 반복하면 dedupe 이후 기여도가 거의 없다.

| count | archetype | symbol | trigger_type | date | sample files |
|---:|---|---|---|---|---|
| 4 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 067160 | Stage2-Actionable | 2024-01-08 | e2r_stock_web_v12_residual_round_R8_loop_83_L8_PLATFORM_CONTENT_SW_SECURI..., e2r_stock_web_v12_residual_round_R8_loop_85_L8_PLATFORM_CONTENT_SW_SECURI..., e2r_stock_web_v12_residual_round_R8_loop_89_L8_PLATFORM_CONTENT_SW_SECURI... |
| 3 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 100840 | Stage2-Actionable | 2024-06-03 | e2r_stock_web_v12_residual_round_R1_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_..., e2r_stock_web_v12_residual_round_R1_loop_93_L1_INDUSTRIALS_INFRA_DEFENSE_..., e2r_stock_web_v12_residual_round_R1_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE_... |
| 3 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 005180 | Stage2-Actionable | 2024-04-15 | e2r_stock_web_v12_residual_round_R5_loop_84_L5_CONSUMER_BRAND_DISTRIBUTIO..., e2r_stock_web_v12_residual_round_R5_loop_89_L5_CONSUMER_BRAND_DISTRIBUTIO..., e2r_stock_web_v12_residual_round_R5_loop_96_L5_CONSUMER_BRAND_DISTRIBUTIO... |
| 2 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 012450 | Stage2-Actionable | 2024-02-14 | e2r_stock_web_v12_residual_round_R11_loop_86_L1_INDUSTRIALS_INFRA_DEFENSE..., e2r_stock_web_v12_residual_round_R11_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE... |
| 2 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 024740 | Stage4B | 2024-01-17 | e2r_stock_web_v12_residual_round_R11_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE..., e2r_stock_web_v12_residual_round_R1_loop_94_L1_INDUSTRIALS_INFRA_DEFENSE_... |
| 2 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 064350 | Stage2 | 2024-02-22 | e2r_stock_web_v12_residual_round_R1_loop_95_L1_INDUSTRIALS_INFRA_DEFENSE_..., e2r_stock_web_v12_residual_round_R1_loop_95_L1_INDUSTRIALS_INFRA_DEFENSE_... |
| 2 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 272210 | Stage2 | 2024-07-24 | e2r_stock_web_v12_residual_round_R1_loop_95_L1_INDUSTRIALS_INFRA_DEFENSE_..., e2r_stock_web_v12_residual_round_R1_loop_95_L1_INDUSTRIALS_INFRA_DEFENSE_... |
| 2 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 448710 | Stage4C | 2024-04-09 | e2r_stock_web_v12_residual_round_R1_loop_95_L1_INDUSTRIALS_INFRA_DEFENSE_..., e2r_stock_web_v12_residual_round_R1_loop_95_L1_INDUSTRIALS_INFRA_DEFENSE_... |
| 2 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 028050 | Stage2-Actionable | 2024-04-03 | e2r_stock_web_v12_residual_round_R1_loop_88_L1_INDUSTRIALS_INFRA_DEFENSE_..., e2r_stock_web_v12_residual_round_R1_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE_... |
| 2 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 031980 | Stage2-Actionable | 2024-02-06 | e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONI..., e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONI... |
| 2 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 036540 | Stage2-Actionable | 2024-01-24 | e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONI..., e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONI... |
| 2 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 080220 | Stage4B | 2024-01-25 | e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONI..., e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONI... |
| 2 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 080580 | Stage4B | 2024-01-23 | e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONI..., e2r_stock_web_v12_residual_round_R2_loop_96_L2_AI_SEMICONDUCTOR_ELECTRONI... |
| 2 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 036810 | Stage2 | 2024-04-09 | e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONI..., e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONI... |
| 2 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 084370 | Stage2-Actionable | 2024-03-21 | e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONI..., e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONI... |
| 2 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 240810 | Stage4C | 2024-03-20 | e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONI..., e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONI... |
| 2 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 003670 | Stage2-FalsePositive-Cathode-Orderbook-CallOff-DemandBreak | 2024-03-22 | e2r_stock_web_v12_residual_round_R3_loop_83_L3_BATTERY_EV_GREEN_MOBILITY_..., e2r_stock_web_v12_residual_round_R3_loop_83_L3_BATTERY_EV_GREEN_MOBILITY_... |
| 2 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 066970 | Stage2-FalsePositive-Cathode-Offtake-CallOff-NoMarginBridge | 2024-03-22 | e2r_stock_web_v12_residual_round_R3_loop_83_L3_BATTERY_EV_GREEN_MOBILITY_..., e2r_stock_web_v12_residual_round_R3_loop_83_L3_BATTERY_EV_GREEN_MOBILITY_... |
| 2 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 348370 | Stage2-Actionable | 2024-01-12 | e2r_stock_web_v12_residual_round_R3_loop_83_L3_BATTERY_EV_GREEN_MOBILITY_..., e2r_stock_web_v12_residual_round_R3_loop_83_L3_BATTERY_EV_GREEN_MOBILITY_... |
| 2 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 393890 | Stage4B | 2024-02-22 | e2r_stock_web_v12_residual_round_R3_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_..., e2r_stock_web_v12_residual_round_R9_loop_89_L3_BATTERY_EV_GREEN_MOBILITY_... |
| 2 | C15_MATERIAL_SPREAD_SUPERCYCLE | 001430 | Stage4C | 2024-02-23 | e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_..., e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_... |
| 2 | C15_MATERIAL_SPREAD_SUPERCYCLE | 004020 | Stage4C | 2024-02-07 | e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_..., e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_... |
| 2 | C15_MATERIAL_SPREAD_SUPERCYCLE | 004020 | steel_spread_recovery_headline | 2024-02-07 | e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_..., e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_... |
| 2 | C15_MATERIAL_SPREAD_SUPERCYCLE | 006260 | copper_cable_spread_capacity_beta | 2024-04-12 | e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_..., e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_... |
| 2 | C15_MATERIAL_SPREAD_SUPERCYCLE | 010060 | polysilicon_spread_rebound_headline | 2024-01-10 | e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_..., e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_... |
| 2 | C15_MATERIAL_SPREAD_SUPERCYCLE | 306200 | Stage2 | 2024-01-24 | e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_..., e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_... |
| 2 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 001340 | Stage2-Actionable | 2024-05-22 | e2r_stock_web_v12_residual_round_R4_loop_89_L4_MATERIALS_SPREAD_RESOURCE_..., e2r_stock_web_v12_residual_round_R4_loop_97_L4_MATERIALS_SPREAD_RESOURCE_... |
| 2 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 055550 | Stage2 | 2024-02-01 | e2r_stock_web_v12_residual_round_R6_loop_94_L6_FINANCIAL_CAPITAL_RETURN_D..., e2r_stock_web_v12_residual_round_R6_loop_97_L6_FINANCIAL_CAPITAL_RETURN_D... |
| 2 | C22_INSURANCE_RATE_CYCLE_RESERVE | 000400 | Stage4C | 2024-04-23 | e2r_stock_web_v12_residual_round_R6_loop_93_L6_FINANCIAL_CAPITAL_RETURN_D..., e2r_stock_web_v12_residual_round_R6_loop_96_L6_FINANCIAL_CAPITAL_RETURN_D... |
| 2 | C22_INSURANCE_RATE_CYCLE_RESERVE | 032830 | Stage2-Actionable | 2024-01-24 | e2r_stock_web_v12_residual_round_R6_loop_90_L6_FINANCIAL_CAPITAL_RETURN_D..., e2r_stock_web_v12_residual_round_R6_loop_93_L6_FINANCIAL_CAPITAL_RETURN_D... |
| 2 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 000250 | Stage2-Actionable | 2024-03-25 | e2r_stock_web_v12_residual_round_R7_loop_88_L7_BIO_HEALTHCARE_MEDICAL_C23..., e2r_stock_web_v12_residual_round_R7_loop_95_L7_BIO_HEALTHCARE_MEDICAL_C23... |
| 2 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 145020 | Stage2-Actionable | 2024-03-04 | e2r_stock_web_v12_residual_round_R7_loop_85_L7_BIO_HEALTHCARE_MEDICAL_C23..., e2r_stock_web_v12_residual_round_R7_loop_92_L7_BIO_HEALTHCARE_MEDICAL_C23... |
| 2 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 099190 | Stage2-FalsePositive-CGMReimbursementCommercialization-NoBridge | 2024-01-10 | e2r_stock_web_v12_residual_round_R7_loop_83_L7_BIO_HEALTHCARE_MEDICAL_C25..., e2r_stock_web_v12_residual_round_R7_loop_83_L7_BIO_HEALTHCARE_MEDICAL_C25... |
| 2 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 214450 | Stage2-Actionable | 2024-03-25 | e2r_stock_web_v12_residual_round_R7_loop_88_L7_BIO_HEALTHCARE_MEDICAL_C25..., e2r_stock_web_v12_residual_round_R7_loop_91_L7_BIO_HEALTHCARE_MEDICAL_C25... |
| 2 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 214450 | Stage2-Actionable | 2024-04-01 | e2r_stock_web_v12_residual_round_R7_loop_83_L7_BIO_HEALTHCARE_MEDICAL_C25..., e2r_stock_web_v12_residual_round_R7_loop_83_L7_BIO_HEALTHCARE_MEDICAL_C25... |
| 2 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 228670 | Stage2-FalsePositive-DentalDeviceExportSpike-NoBridge | 2024-04-01 | e2r_stock_web_v12_residual_round_R7_loop_83_L7_BIO_HEALTHCARE_MEDICAL_C25..., e2r_stock_web_v12_residual_round_R7_loop_83_L7_BIO_HEALTHCARE_MEDICAL_C25... |
| 2 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 228670 | Stage4C | 2024-03-12 | e2r_stock_web_v12_residual_round_R7_loop_91_L7_BIO_HEALTHCARE_MEDICAL_C25..., e2r_stock_web_v12_residual_round_R7_loop_94_L7_BIO_HEALTHCARE_MEDICAL_C25... |
| 2 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 030520 | Stage2-Actionable | 2024-01-05 | e2r_stock_web_v12_residual_round_R8_loop_88_L8_PLATFORM_CONTENT_SW_SECURI..., e2r_stock_web_v12_residual_round_R8_loop_94_L8_PLATFORM_CONTENT_SW_SECURI... |
| 2 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 200880 | Stage2-Actionable | 2024-02-01 | e2r_stock_web_v12_residual_round_R9_loop_88_L3_BATTERY_EV_GREEN_MOBILITY_..., e2r_stock_web_v12_residual_round_R9_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_... |
| 2 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 000720 | Stage2-Actionable | 2025-01-22 | e2r_stock_web_v12_residual_round_R10_loop_87_L9_CONSTRUCTION_REALESTATE_H..., e2r_stock_web_v12_residual_round_R10_loop_89_L9_CONSTRUCTION_REALESTATE_H... |
| 2 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 028050 | Stage2-Actionable | 2024-02-01 | e2r_stock_web_v12_residual_round_R10_loop_88_L9_CONSTRUCTION_REALESTATE_H..., e2r_stock_web_v12_residual_round_R10_loop_96_L9_CONSTRUCTION_REALESTATE_H... |
| 2 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 034300 | Stage4B | 2024-05-29 | e2r_stock_web_v12_residual_round_R10_loop_87_L9_CONSTRUCTION_REALESTATE_H..., e2r_stock_web_v12_residual_round_R10_loop_95_L9_CONSTRUCTION_REALESTATE_H... |
| 2 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 051600 | Stage2-Actionable | 2025-06-05 | e2r_stock_web_v12_residual_round_R12_loop_87_L10_POLICY_EVENT_CROSS_REDTE..., e2r_stock_web_v12_residual_round_R12_loop_87_L10_POLICY_EVENT_CROSS_REDTE... |
| 2 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 052690 | Stage2-Actionable | 2025-06-05 | e2r_stock_web_v12_residual_round_R12_loop_87_L10_POLICY_EVENT_CROSS_REDTE..., e2r_stock_web_v12_residual_round_R12_loop_87_L10_POLICY_EVENT_CROSS_REDTE... |
| 2 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 052690 | Stage2-FalsePositive-Candidate / PreferredBidderOnlyLegalOverhang | 2024-07-10 | e2r_stock_web_v12_residual_round_R12_loop_87_L10_POLICY_EVENT_CROSS_REDTE..., e2r_stock_web_v12_residual_round_R12_loop_87_L10_POLICY_EVENT_CROSS_REDTE... |
| 2 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 071320 | Stage2-Actionable | 2024-01-26 | e2r_stock_web_v12_residual_round_R12_loop_89_L10_POLICY_EVENT_CROSS_REDTE..., e2r_stock_web_v12_residual_round_R12_loop_89_L10_POLICY_EVENT_CROSS_REDTE... |
| 2 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 130660 | Stage2-FalsePositive-Candidate / PolicyThemeNoCashflowBridge | 2024-07-10 | e2r_stock_web_v12_residual_round_R12_loop_87_L10_POLICY_EVENT_CROSS_REDTE..., e2r_stock_web_v12_residual_round_R12_loop_87_L10_POLICY_EVENT_CROSS_REDTE... |
| 2 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 003240 | Stage4C | 2024-02-01 | e2r_stock_web_v12_residual_round_R11_loop_94_L10_POLICY_EVENT_CROSS_REDTE..., e2r_stock_web_v12_residual_round_R12_loop_98_L10_POLICY_EVENT_CROSS_REDTE... |
| 2 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 028260 | Stage2-Actionable | 2024-01-29 | e2r_stock_web_v12_residual_round_R12_loop_84_L10_POLICY_EVENT_CROSS_REDTE..., e2r_stock_web_v12_residual_round_R12_loop_86_L10_POLICY_EVENT_CROSS_REDTE... |
| 2 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 000720 | Stage2 | 2024-04-29 | e2r_stock_web_v12_residual_round_R13_loop_86_L10_POLICY_EVENT_CROSS_REDTE..., e2r_stock_web_v12_residual_round_R13_loop_86_L10_POLICY_EVENT_CROSS_REDTE... |
| 2 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 003240 | Stage4C | 2024-02-01 | e2r_stock_web_v12_residual_round_R13_loop_94_L10_POLICY_EVENT_CROSS_REDTE..., e2r_stock_web_v12_residual_round_R13_loop_98_L10_POLICY_EVENT_CROSS_REDTE... |
| 2 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 004980 | Stage2 | 2024-02-01 | e2r_stock_web_v12_residual_round_R13_loop_89_L10_POLICY_EVENT_CROSS_REDTE..., e2r_stock_web_v12_residual_round_R13_loop_98_L10_POLICY_EVENT_CROSS_REDTE... |
| 2 | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 034300 | Stage4B | 2024-05-29 | e2r_stock_web_v12_residual_round_R13_loop_93_L10_POLICY_EVENT_CROSS_REDTE..., e2r_stock_web_v12_residual_round_R13_loop_95_L10_POLICY_EVENT_CROSS_REDTE... |

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
| large_sector:L10_POLICY_EVENT_CROSS_REDTEAM_MISC | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| large_sector:L1_INDUSTRIALS_INFRA_DEFENSE_GRID | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| large_sector:L2_AI_SEMICONDUCTOR_ELECTRONICS | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| large_sector:L3_BATTERY_EV_GREEN_MOBILITY | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| large_sector:L4_MATERIALS_SPREAD_RESOURCE | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| large_sector:L5_CONSUMER_BRAND_DISTRIBUTION | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| large_sector:L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| large_sector:L7_BIO_HEALTHCARE_MEDICAL | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| large_sector:L8_PLATFORM_CONTENT_SW_SECURITY | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| large_sector:L9_CONSTRUCTION_REALESTATE_HOUSING | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C01_ORDER_BACKLOG_MARGIN_BRIDGE | stage2_bonus_candidate_delta | blocked_by_data_quality | evidence_url_pending_or_source_proxy_rate_above_25pct | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C01_ORDER_BACKLOG_MARGIN_BRIDGE | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C02_POWER_GRID_DATACENTER_CAPEX | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | stage2_bonus_candidate_delta | blocked_by_data_quality | evidence_url_pending_or_source_proxy_rate_above_25pct | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C05_EPC_MEGA_CONTRACT_MARGIN_GAP | stage2_bonus_candidate_delta | blocked_by_data_quality | evidence_url_pending_or_source_proxy_rate_above_25pct | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C05_EPC_MEGA_CONTRACT_MARGIN_GAP | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C06_HBM_MEMORY_CUSTOMER_CAPACITY | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | stage2_bonus_candidate_delta | blocked_by_data_quality | evidence_url_pending_or_source_proxy_rate_above_25pct | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C11_BATTERY_ORDERBOOK_RERATING | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C13_BATTERY_JV_UTILIZATION_AMPC_IRA | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C14_EV_DEMAND_SLOWDOWN_4B_4C | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C15_MATERIAL_SPREAD_SUPERCYCLE | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | stage2_bonus_candidate_delta | blocked_by_data_quality | evidence_url_pending_or_source_proxy_rate_above_25pct | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C18_CONSUMER_EXPORT_CHANNEL_REORDER | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C19_BRAND_RETAIL_INVENTORY_MARGIN | stage2_bonus_candidate_delta | blocked_by_data_quality | evidence_url_pending_or_source_proxy_rate_above_25pct | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C19_BRAND_RETAIL_INVENTORY_MARGIN | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | stage2_bonus_candidate_delta | blocked_by_data_quality | evidence_url_pending_or_source_proxy_rate_above_25pct | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C22_INSURANCE_RATE_CYCLE_RESERVE | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C24_BIO_TRIAL_DATA_EVENT_RISK | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C27_CONTENT_IP_GLOBAL_MONETIZATION | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C31_POLICY_SUBSIDY_LEGISLATION_EVENT | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |
| canonical_archetype:R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | full_4b_overlay_candidate | blocked_by_data_quality | full_4b_overlay_needs_verified_non_proxy_evidence | verify_evidence_urls_or_replace_source_proxy_rows |

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

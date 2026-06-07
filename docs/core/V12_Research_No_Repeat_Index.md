# V12 Research No-Repeat Index

이 문서는 새 자동연구 세션을 시작할 때 먼저 읽는 중복 방지 장부다.
목적은 같은 대섹터/아키타입 안에서 같은 종목, 같은 날짜, 같은 trigger를 반복 연구하지 않게 하는 것이다.

쉬운 예시:

```text
이미 C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / 257720 / Stage3-Green / 2024-05-10 이 들어왔다.
다음 연구는 같은 조합을 다시 쓰지 말고, 새 종목, 새 날짜, 새 trigger family, 또는 4B/4C/반례를 찾아야 한다.
```

last_updated: `2026-06-07`

## 현재 결론

`docs/core/goal.md`의 표준 명령은 현재 기준으로 정규화 가능한 V12 연구 row를 모두 사용한다.
추가로 goal 명령 자체를 고칠 필요는 없다. 다만 입력 row가 필수 칸을 빼먹으면 deterministic scorer가 임의 추정하지 않고 제외한다.

서브에이전트 리뷰 반영으로 `source_row_type`이 compact/review 계열이어도 30D/90D/180D MFE·MAE 6개가 모두 없으면 valid row가 아니다.

쉬운 예시:

```text
사용 가능: entry_date, entry_price, trigger_type, 30/90/180D MFE/MAE, large_sector_id, canonical_archetype_id가 모두 있음
사용 불가: 종목 설명과 180D 수익률만 있고 MFE_30D_pct/MAE_90D_pct가 없음
이 경우 중간에 -30%를 맞고 회복했는지 알 수 없어 점수 정규화에 넣지 않는다.
```

## 원본 데이터

| source | role |
|---|---|
| `data/e2r/calibration/v12/v12_md_registry.jsonl` | 이번 실행에 실제 ingest된 연구 MD 목록 |
| `data/e2r/calibration/v12/v12_extracted_triggers_raw.jsonl` | 파서가 읽은 raw trigger row |
| `data/e2r/calibration/v12/v12_trigger_rows_validated.jsonl` | 검증 통과 row |
| `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl` | 중복제거 후 대표 trigger row |
| `data/e2r/calibration/v12/rejected_v12_rows.jsonl` | 정규화에서 제외된 row와 사유 |
| `data/e2r/calibration/v12/v12_aggregate_metrics.json` | 대섹터/아키타입 집계 |
| `data/e2r/calibration/v12/stage_transition_summary.jsonl` | Stage2, Green, 4B, 4C 전이 요약 |
| `data/e2r/calibration/v12/v12_promotion_decisions.jsonl` | apply / hold / block 결정 |
| `data/e2r/calibration/v12/v12_patch_specs.jsonl` | 실제 profile 반영 후보 및 적용 specs |
| `reports/e2r_calibration/v12/coverage_matrix.md` | scope별 coverage 요약 |
| `reports/e2r_calibration/v12/archetype_weight_runtime_report.md` | 아키타입별 점수비중 산출 결과 |

## 이번 배치 반영 메모

| item | result |
|---|---:|
| run command | `run-v12-calibration --md-input-root docs/round` |
| discovered markdown docs | 302 |
| v12 result MD | 279 |
| parser failures | 0 |
| zero trigger result docs | 0 |
| compact/non-result docs with trigger rows | 23 |
| compact/non-result raw trigger rows | 109 |
| compact rows validated if force-included | 0 |
| raw trigger rows | 1348 |
| validated rows | 542 |
| representative rows | 527 |
| validated rows missing any required MFE/MAE field | 0 |
| representative rows missing any required MFE/MAE field | 0 |
| rejected rows | 981 |
| stage transition rows | 515 |
| promotion decisions | 83 |
| apply_next_patch decisions | 44 |
| blocked_by_data_quality decisions | 37 |
| hold_for_more_evidence decisions | 2 |
| applied patch specs | 44 |
| active profile selector | `e2r_2_2` |
| rolling profile id | `e2r_2_2_rolling_calibrated` |
| production default scoring changed | true |
| archetype weight count | 36 |
| large sector weight count | 10 |

`docs/round/achieve`와 `docs/round/achieve_v12`는 완료 보관분이라 discovery에서 제외한다. 파일명 `(1)`, `(2)`, `(3)` suffix는 제외 기준이 아니며, 내용/row key/dedupe 결과로 판단한다.

## Corpus Snapshot

| metric | value |
|---|---:|
| representative row_count | 527 |
| unique_case_count | 488 |
| unique_symbol_count | 265 |
| unique_round_count | 12 |
| positive_case_count | 46 |
| counterexample_count | 97 |
| 4B_case_count | 43 |
| 4C_case_count | 27 |
| good_stage2_count | 182 |
| bad_stage2_count | 153 |
| source_proxy_only_count | 258 |
| evidence_url_pending_count | 390 |
| current_profile_error_count | 420 |
| current_profile_false_positive_count | 224 |
| current_profile_too_late_count | 147 |
| stage2 hit rate MFE90 >= 20% | 0.5819 |
| stage2 bad entry rate MAE90 <= -20% | 0.3158 |
| avg Stage2 MFE90 | 50.8 |
| avg Stage2 MAE90 | -15.8 |
| exact duplicate groups after validation | 15 |
| duplicate member rows removed by representative dedupe | 15 |
| canonical_archetypes_covered by representative rows | 32 |

## Goal 사용 범위 점검

| 구분 | row/docs | 현재 처리 | 판단 |
|---|---:|---|---|
| 표준 V12 result MD | 279 docs | ingest 대상 | 사용됨 |
| 표준 result MD 안 raw trigger | 1348 rows | validation 수행 | 조건 통과분만 사용 |
| validated trigger | 542 rows | dedupe 후보 | 사용됨 |
| representative trigger | 527 rows | aggregate/weight/profile 입력 | 최종 사용 |
| valid/representative 중 필수 MFE/MAE 누락 | 0/0 rows | strict gate | 사용되지 않음 |
| compact short filename docs | 23 docs / 109 rows | result 파일명이 아니어서 제외 | 강제 포함해도 validated 0개 |
| compact 제외 핵심 사유 | 109 rows | `missing_required_mfe_mae` | 30/90/180D MFE/MAE 보강 전까지 정규화 불가 |

즉 지금 goal은 “쓸 수 있는 것은 다 쓰고, 숫자로 검증할 수 없는 것은 멈추는” 상태다. compact 109개와 result MD 안 partial path row는 가격경로를 재계산해 30/90/180D MFE/MAE를 붙여야만 정규화에 들어간다.

## 주요 rejected reason

Rejected row는 버리는 데이터가 아니라 다음 정규화 TODO다. 예를 들어 `missing_required_mfe_mae`는 가격경로 30D/90D/180D가 부족해서 score 보정에 못 쓴다는 뜻이다.

| reason | rows | 쉬운 뜻 |
|---|---:|---|
| `missing_required_mfe_mae` | 794 | 30/90/180일 MFE/MAE가 모두 없어 성공/실패 경로 비교 불가 |
| `not_representative_for_aggregate` | 152 | 중복 그룹의 대표 row가 아니거나 aggregate 제외 표시 |
| `not_usable_for_promotion` | 120 | positive 승격 근거로 쓰기에는 비가격 증거/품질이 부족 |
| `missing_entry_price` | 47 | 진입가 없음 |
| `missing_trigger_type` | 44 | Stage2/4B/4C 등 trigger 종류 없음 |
| `missing_entry_date` | 43 | 진입일 없음 |
| `price_only_no_evidence` | 23 | 가격 움직임만 있고 공시/실적/계약/뉴스 같은 비가격 증거 부족 |
| `insufficient_forward_window` | 4 | as_of 이후 충분한 forward window가 없음 |

### missing_required_mfe_mae 세부 출처

| source_row_type | rows |
|---|---:|
| `trigger` | 629 |
| `v12_compact_case` | 94 |
| `r13_review_trigger` | 36 |
| `r13_cross_case` | 12 |
| `review_case` | 12 |
| `v12_review_only_audit` | 8 |
| `trigger_case` | 3 |

## 반영된 safe patch 축

| axis | applied specs | 쉬운 뜻 |
|---|---:|---|
| `stage2_required_bridge` | 32 | Stage2로 올리려면 가격 말고 수주/실적/계약/마진 같은 bridge를 요구 |
| `earlier_thesis_break_watch` | 8 | 논리 훼손 조짐을 더 일찍 watch로 표시 |
| `local_4b_watch_guard` | 4 | 가격만 오른 4B는 full 4B보다 watch로 제한 |

## Promotion Decision 요약

| decision | count | 의미 |
|---|---:|---|
| `apply_next_patch` | 44 | 지금 profile에 작은 scope patch로 반영 |
| `blocked_by_data_quality` | 37 | URL/proxy/가격경로 등 품질 보강 필요 |
| `hold_for_more_evidence` | 2 | 근거 수가 더 필요 |

## 대섹터별 대표 row 수

| large_sector | rows | symbols | positives/counter | 4B/4C | URL pending/proxy |
|---|---:|---:|---:|---:|---:|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 6 | 6 | 2/4 | 0/0 | 6/6 |
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 83 | 44 | 8/19 | 5/0 | 53/37 |
| L2_AI_SEMICONDUCTOR_ELECTRONICS | 185 | 78 | 17/29 | 13/0 | 139/63 |
| L3_BATTERY_EV_GREEN_MOBILITY | 105 | 36 | 7/19 | 6/24 | 65/43 |
| L4_MATERIALS_SPREAD_RESOURCE | 30 | 24 | 2/6 | 5/1 | 27/24 |
| L5_CONSUMER_BRAND_DISTRIBUTION | 30 | 20 | 2/4 | 5/0 | 24/18 |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 12 | 11 | 1/2 | 3/0 | 12/12 |
| L7_BIO_HEALTHCARE_MEDICAL | 31 | 21 | 3/6 | 3/2 | 28/22 |
| L8_PLATFORM_CONTENT_SW_SECURITY | 42 | 28 | 3/6 | 3/0 | 33/30 |
| L9_CONSTRUCTION_REALESTATE_HOUSING | 3 | 3 | 1/2 | 0/0 | 3/3 |

## 다음 연구 우선순위

자동연구원은 R1~R13을 기계적으로 순환하지 말고, 아래 아키타입별 수량을 먼저 본다. Round는 연구 대상을 고른 뒤 파일명/대섹터 일관성을 맞추기 위해 따라오는 metadata다.

| target | meaning | current shortage |
|---|---|---:|
| 30 rows per archetype | 최소 안정권. 방향성을 보기 시작 | 480 |
| 50 rows per archetype | 실전 보정권. positive/counterexample/4B/4C 균형 확인 | 1073 |
| 80 rows per archetype | 탄탄한 권역. 새 row가 들어와도 weight가 덜 흔들림 | 2033 |

### Priority 0: 30 row 미만부터 채우기

| priority | archetype | rows | need to 30 | need to 50 | 조사 포인트 |
|---:|---|---:|---:|---:|---|
| 1 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 3 | 27 | 47 | 수출 채널, reorder, repeat demand, 재고 부담 |
| 2 | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 3 | 27 | 47 | 광고/플랫폼 매출 회복과 operating leverage 확인 |
| 3 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 3 | 27 | 47 | volume/mix/margin과 operating leverage, 자본정책 |
| 4 | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 3 | 27 | 47 | PF/유동성/재무제표 hard break와 bargain rebound 구분 |
| 5 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 3 | 27 | 47 | 정책 headline이 법/예산/회사 cashflow로 전환되는지 |
| 6 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 3 | 27 | 47 | 지배구조 premium, tender cap, minority risk, FCF/return 확인 |
| 7 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 6 | 24 | 44 | 원전 정책 headline과 최종계약/법적 지연/프로젝트 경제성 분리 |
| 8 | C15_MATERIAL_SPREAD_SUPERCYCLE | 6 | 24 | 44 | spread supercycle과 회사별 ASP/volume/margin 전환 |
| 9 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 6 | 24 | 44 | K-food/K-beauty 글로벌 유통, sell-through, OPM/revision |
| 10 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 6 | 24 | 44 | ROE/PBR/value-up과 실제 자본정책 실행 |
| 11 | C22_INSURANCE_RATE_CYCLE_RESERVE | 6 | 24 | 44 | 보험 rate cycle, reserve quality, CSM, capital return |
| 12 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 6 | 24 | 44 | 의료기기 수출, reimbursement, 반복 소모품 매출 |
| 13 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 9 | 21 | 41 | 방산 수출계약, 정부 고객, 납품 일정, 수주잔고와 margin conversion |
| 14 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 12 | 18 | 38 | 전략자원 정책과 offtake/margin/공급망 실행 |
| 15 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 12 | 18 | 38 | 원재료 가격과 실제 spread/margin/FCF 분리 |
| 16 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 12 | 18 | 38 | 승인 이후 상업화, 매출/royalty/reimbursement 전환 |
| 17 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 13 | 17 | 37 | EPC mega 계약, 원가초과, working capital, margin gap |
| 18 | C24_BIO_TRIAL_DATA_EVENT_RISK | 13 | 17 | 37 | 임상 데이터 이벤트, 승인 전 price spike, 실패/지연 반례 |
| 19 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 15 | 15 | 35 | JV utilization, AMPC, IRA 지속성, cash conversion |
| 20 | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 16 | 14 | 34 | 고객 계약과 call-off/demand risk, AMPC/IRA와 분리 |
| 21 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 18 | 12 | 32 | 보안 계약, ARR, retention, renewal, margin leverage |
| 22 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 21 | 9 | 29 | 재고/매출채권/OPM/sell-through로 성장 재고와 channel stuffing 분리 |
| 23 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 21 | 9 | 29 | IP 매출화, 글로벌 플랫폼 전환, 일회성 흥행 반례 |
| 24 | C02_POWER_GRID_DATACENTER_CAPEX | 24 | 6 | 26 | 전력망/데이터센터 CAPEX, backlog, CAPA lock, ASP와 납기 visibility |

### Priority 1: 50 row까지 끌어올리기

| archetype | rows | need to 50 | 조사 포인트 |
|---|---:|---:|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 31 | 19 | 수주잔고 + 마진 bridge + FCF 전환이 같이 있는 성공/실패 분리 |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 32 | 18 | HBM 장비 상대강도와 실제 order/revenue conversion 연결 |
| C11_BATTERY_ORDERBOOK_RERATING | 32 | 18 | 배터리 orderbook이 margin/FCF로 전환되는지 검증 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 33 | 17 | HBM 고객, CAPA, mix, ASP, revision, cycle 반례 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 37 | 13 | 메모리 회복 beta와 실제 장비 order cycle reversal 분리 |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 39 | 11 | EV 수요 둔화, utilization, call-off, hard 4C 확인 |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 40 | 10 | 장비 valuation 과열, 수주 없는 price blowoff, 4B/4C 전환 |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 43 | 7 | 고객 qualification, 반복 소모품 수요, socket/test margin 전환 |

### Priority 2: 이미 많은 구역은 새 근거가 있을 때만

현재 C01~C32 중 50 row 이상인 아키타입은 없다. 그래서 이번 주는 Priority 0/1 보강이 더 중요하다.

### R13 특수 범위

R13은 일반 Green unlock 연구가 아니다. cross-archetype guardrail 검증이 필요할 때만 한다. 이번 strict gate 후 R13 대표 row는 0개라서, R13을 쓰려면 30/90/180D MFE·MAE를 모두 갖춘 guardrail row로 다시 조사해야 한다.

| R13 scope | rows | guidance |
|---|---:|---|
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 0 | 필수 6개 가격경로를 갖춘 Stage2 false positive/accounting trust/high MAE 검증용으로만 추가 |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 0 | 필수 6개 가격경로를 갖춘 Stage2 false positive/accounting trust/high MAE 검증용으로만 추가 |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 0 | 필수 6개 가격경로를 갖춘 Stage2 false positive/accounting trust/high MAE 검증용으로만 추가 |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 0 | 필수 6개 가격경로를 갖춘 Stage2 false positive/accounting trust/high MAE 검증용으로만 추가 |

## 아키타입별 현재 커버리지와 점수비중

| archetype | rows | symbols | positives/counter | 4B/4C | S2 hit/bad | weights EPS/Vis/Bott/Mis/Val/Cap/Info | top covered symbols |
|---|---:|---:|---:|---:|---:|---|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 31 | 21 | 4/5 | 0/0 | 0.73/0.04 | 20/25/18/12/12/8/5 | 010620(4), 329180(4), 010120(2), 042670(2), 071970(2), 097230(2) |
| C02_POWER_GRID_DATACENTER_CAPEX | 24 | 15 | 1/7 | 1/0 | 0.81/0.19 | 21/24/20/13/12/5/5 | 267260(4), 010120(3), 033100(2), 037030(2), 103590(2), 298040(2) |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 9 | 8 | 1/1 | 2/0 | 0.57/0.29 | 20/24/17/14/14/6/5 | 103140(2), 005870(1), 042660(1), 047810(1), 065450(1), 077970(1) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 6 | 5 | 0/2 | 1/0 | 0.60/0.40 | 15/22/10/15/18/10/10 | 046120(2), 019990(1), 034020(1), 083650(1), 126720(1) |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 13 | 10 | 2/4 | 1/0 | 0.44/0.00 | 18/22/10/12/10/8/20 | 000720(2), 028050(2), 047040(2), 006360(1), 011930(1), 023350(1) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 33 | 19 | 2/4 | 1/0 | 0.54/0.25 | 24/21/19/15/12/4/5 | 000660(6), 005930(5), 009150(4), 222800(2), 356860(2), 000990(1) |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 32 | 22 | 1/2 | 3/0 | 0.63/0.52 | 22/22/19/14/12/6/5 | 042700(6), 089030(4), 110990(2), 412350(2), 003160(1), 031980(1) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 43 | 26 | 7/9 | 4/0 | 0.70/0.39 | 22/21/16/14/12/6/9 | 095340(5), 131290(5), 425420(4), 424980(3), 058470(2), 080580(2) |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 40 | 30 | 4/11 | 3/0 | 0.52/0.52 | 22/20/18/13/11/6/10 | 089970(2), 095340(2), 101490(2), 131290(2), 281820(2), 322310(2) |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 37 | 18 | 3/3 | 2/0 | 0.74/0.26 | 22/18/14/12/10/5/19 | 240810(6), 319660(6), 095610(3), 014680(2), 036200(2), 039440(2) |
| C11_BATTERY_ORDERBOOK_RERATING | 32 | 18 | 1/5 | 2/0 | 0.45/0.50 | 20/20/15/12/10/8/15 | 137400(5), 222080(4), 299030(3), 006400(2), 121600(2), 247540(2) |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 16 | 11 | 1/2 | 1/4 | 0.40/0.20 | 20/18/14/10/10/8/20 | 005070(3), 020150(2), 078600(2), 121600(2), 003670(1), 006400(1) |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 15 | 12 | 1/2 | 1/2 | 0.57/0.29 | 20/18/14/12/10/10/16 | 051910(2), 066970(2), 373220(2), 003670(1), 005070(1), 006400(1) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 39 | 18 | 3/8 | 2/18 | 0.44/0.44 | 15/12/10/8/8/7/40 | 247540(7), 373220(6), 006400(3), 066970(3), 361610(3), 003670(2) |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 6 | 6 | 0/2 | 1/0 | 0.80/0.20 | 20/12/20/10/10/8/20 | 001390(1), 001550(1), 005490(1), 009520(1), 025860(1), 103140(1) |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 12 | 10 | 1/2 | 3/0 | 0.43/0.14 | 18/18/18/12/12/7/15 | 000910(2), 001120(2), 001550(1), 012800(1), 024840(1), 024890(1) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 12 | 9 | 1/2 | 1/1 | 0.50/0.38 | 20/12/18/10/10/5/25 | 011780(3), 011170(2), 004000(1), 006650(1), 014680(1), 014830(1) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 3 | 3 | 0/0 | 1/0 | 0.50/0.50 | 22/23/12/16/13/4/10 | 003230(1), 011150(1), 383220(1) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 21 | 12 | 2/4 | 2/0 | 0.35/0.29 | 18/18/8/15/14/7/20 | 004170(4), 036620(3), 282330(3), 023530(2), 298540(2), 007070(1) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 6 | 6 | 0/0 | 2/0 | 0.50/0.50 | 22/23/12/16/13/4/10 | 018250(1), 114840(1), 192820(1), 214420(1), 237880(1), 406820(1) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 6 | 5 | 0/0 | 2/0 | 0.50/0.50 | 15/20/5/15/25/15/5 | 323410(2), 003530(1), 024110(1), 030610(1), 086790(1) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 6 | 6 | 1/2 | 1/0 | 0.33/0.00 | 12/22/5/14/24/18/5 | 000540(1), 000810(1), 001450(1), 003690(1), 085620(1), 138930(1) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 12 | 9 | 1/2 | 1/0 | 0.44/0.11 | 12/24/5/12/10/7/30 | 195940(3), 145020(2), 000100(1), 009420(1), 067630(1), 068270(1) |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 13 | 8 | 1/2 | 1/2 | 0.50/0.25 | 5/15/5/10/5/5/55 | 028300(4), 141080(2), 298380(2), 039200(1), 115180(1), 215600(1) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 6 | 4 | 1/2 | 1/0 | 0.67/0.33 | 20/22/13/14/12/9/10 | 145720(2), 214150(2), 099190(1), 336570(1) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 3 | 3 | 0/0 | 1/0 | 0.50/0.50 | 20/22/8/16/14/10/10 | 035420(1), 042000(1), 237820(1) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 21 | 12 | 1/2 | 1/0 | 0.42/0.42 | 20/18/8/14/12/8/20 | 352820(4), 253450(3), 259960(3), 041510(2), 263750(2), 035900(1) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 18 | 13 | 2/4 | 1/0 | 0.57/0.29 | 20/24/8/16/14/8/10 | 307950(3), 012510(2), 042510(2), 058970(2), 012750(1), 041020(1) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 3 | 3 | 1/2 | 0/0 | 1.00/0.00 | 20/18/10/15/17/15/5 | 005710(1), 007860(1), 033530(1) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 3 | 3 | 1/2 | 0/0 | 0.00/0.00 | 18/12/8/12/10/10/30 | 009410(1), 034300(1), 183190(1) |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 3 | 3 | 1/2 | 0/0 | 1.00/0.00 | 12/15/8/15/15/10/25 | 034230(1), 068290(1), 086790(1) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 3 | 3 | 1/2 | 0/0 | 1.00/0.00 | 12/18/5/20/25/15/5 | 000670(1), 010130(1), 180640(1) |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 0 | 0 | 0/0 | 0/0 | -/- | 8/12/8/10/8/4/50 | - |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 0 | 0 | 0/0 | 0/0 | -/- | 8/12/5/10/8/20/37 | - |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 0 | 0 | 0/0 | 0/0 | -/- | 10/14/8/12/10/6/40 | - |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 0 | 0 | 0/0 | 0/0 | -/- | 10/14/8/12/10/6/40 | - |

## 반복 위험이 높은 symbol/archetype 조합

아래 조합은 이미 대표 row가 많이 쌓여 있다. 같은 날짜/같은 trigger 반복은 피한다.

| archetype | symbol | representative rows | date range | main trigger types |
|---|---|---:|---|---|
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 247540 | 7 | 2024-01-22~2024-05-22 | Stage4C(4), CATHODE_EV_DEMAND_SLOWDOWN_CALL_OFF_RISK(1), Stage2(1) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 373220 | 6 | 2024-01-22~2024-04-08 | Stage2(2), Stage4C(2), EV_DEMAND_SLOWDOWN_MARGIN_UTILIZATION_WARNING(1) |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 319660 | 6 | 2024-02-29~2024-06-07 | Stage2-Actionable(4), process_equipment_recovery_with_order_conversion_proxy(1), retest_after_memory_recovery_order_bridge(1) |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 240810 | 6 | 2024-02-29~2024-07-04 | Stage2-Actionable(2), Stage2(1), Stage4B(1) |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 042700 | 6 | 2024-02-08~2024-06-14 | Stage2-Actionable(3), Stage2(2), Stage4B(1) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 000660 | 6 | 2024-02-06~2024-06-14 | Stage2-Actionable(4), hbm_customer_capacity_mix_asp_bridge(1), late_hbm_capacity_extension_after_strong_price_run(1) |
| C11_BATTERY_ORDERBOOK_RERATING | 137400 | 5 | 2024-02-21~2024-06-12 | Stage2-Actionable(3), late_orderbook_chase_after_vertical_move(1), orderbook_delivery_acceptance_momentum(1) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 131290 | 5 | 2024-02-01~2024-04-26 | Stage2-Actionable(3), Stage2(1), Stage2-FalsePositive-ProbeCardTestInterfacePostSpikeNoRenewalRevisionMarginBridge(1) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 095340 | 5 | 2024-02-15~2024-03-28 | Stage2-Actionable(3), Stage2-FalsePositive-TestSocketPriceMFEWithoutDurableCustomerQualificationMarginBridge(1), Stage4B(1) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 005930 | 5 | 2024-03-06~2024-07-05 | Stage2(2), Stage2-Actionable(1), late_memory_hbm_beta_chase(1) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 352820 | 4 | 2024-03-06~2024-04-18 | Stage2-Actionable(2), Stage2(1), kpop_ip_global_fandom_label_pre_break(1) |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 028300 | 4 | 2024-05-16~2024-05-16 | Stage4C(2), Stage2-4C-Validated-RegulatoryCRLApprovalShockHardBreak(1), late_stage_binary_data_regulatory_event_risk(1) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 004170 | 4 | 2024-01-29~2024-03-06 | Stage2(1), Stage2-Actionable(1), Stage2-FalsePositive-DepartmentStoreBrandInventoryVocabularyNoSellThroughMarginBridge(1) |
| C11_BATTERY_ORDERBOOK_RERATING | 222080 | 4 | 2024-02-16~2024-03-06 | Stage2(2), early_equipment_orderbook_reacceleration(1), equipment_orderbook_theme_spike(1) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 425420 | 4 | 2024-03-06~2024-03-20 | Stage2(3), Stage4B(1) |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 089030 | 4 | 2024-02-22~2024-07-11 | Stage2-Actionable(2), Stage2(1), Stage4B(1) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 009150 | 4 | 2024-03-06~2024-07-05 | Stage2-Actionable(2), late_substrate_hbm_beta_chase(1), substrate_capacity_hbm_sympathy_bridge_test(1) |
| C02_POWER_GRID_DATACENTER_CAPEX | 267260 | 4 | 2024-01-29~2024-07-24 | Stage2(2), Stage2-Actionable(2) |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 329180 | 4 | 2024-03-06~2024-04-18 | Stage2-Actionable(4) |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 010620 | 4 | 2024-03-06~2024-04-18 | Stage2-Actionable(3), Stage2-FalsePositive-OverbroadMarginGapWouldMissPostResetOrderbookMarginBridge(1) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 307950 | 3 | 2024-01-02~2024-07-03 | Stage2-Actionable(1), enterprise_software_contract_bridge(1), software_revision_followthrough(1) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 259960 | 3 | 2024-02-13~2024-08-13 | Stage2-Actionable(1), game_ip_liveops_global_monetization_bridge(1), late_liveops_rerating_extension(1) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 253450 | 3 | 2024-01-02~2024-05-09 | Stage2(1), Stage2-FalsePositive-StudioContentPipelineVocabularyNoFreshHitLicensingMarginBridge(1), content_studio_windowing_spike(1) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 195940 | 3 | 2024-01-03~2024-06-17 | Stage2-Actionable(2), Stage2(1) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 282330 | 3 | 2024-01-16~2024-07-05 | Stage2-Actionable(2), Stage2(1) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 036620 | 3 | 2024-02-14~2024-02-21 | Stage2-Actionable(3) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 011780 | 3 | 2024-01-24~2024-03-06 | Stage2-Actionable(3) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 361610 | 3 | 2024-01-22~2024-03-06 | SEPARATOR_EV_DEMAND_SLOWDOWN_UTILIZATION_BREAK(1), Stage2(1), Stage4C(1) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 066970 | 3 | 2024-01-29~2024-03-06 | CATHODE_MATERIAL_DEMAND_SLOWDOWN_MARGIN_BREAK(1), Stage2(1), Stage4C(1) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 006400 | 3 | 2024-03-06~2024-03-25 | Stage4C(2), Stage2(1) |

## 연구 시작 전 중복 판정 규칙

| 구분 | 판정 | 행동 |
|---|---|---|
| Hard duplicate | `canonical_archetype_id + symbol + trigger_type + entry_date`가 이미 있음 | 새 케이스로 세지 말 것 |
| Soft duplicate | 같은 `canonical_archetype_id + symbol`이지만 날짜/trigger가 다름 | 새 evidence family, 새 Stage transition, 4B/4C, 반례일 때만 허용 |
| Useful expansion | 같은 archetype의 새 symbol 또는 새 failure mode | 우선 연구 |
| Data-quality repair | 기존 row가 `evidence_url_pending` 또는 `source_proxy_only` | 같은 케이스라도 URL/공시/리포트 검증 보강이면 허용 |
| Bad expansion | 가격만 있고 비가격 증거가 없음 | Stage2/Green 연구로 쓰지 말고 4B watch/반례 목적만 허용 |
| Unknown symbol | symbol이 `UNKNOWN_SYMBOL` 또는 비어 있음 | 새 연구보다 먼저 symbol 정규화 보강 |
| Filename suffix | `(1)`, `(2)`, `(3)` suffix만으로 중복 취급하지 않음 | 내용/row key 기준으로 판정 |

## 다음 연구 row 필수 칸

앞으로 대표 샘플로 쓰려면 row마다 아래 칸이 들어와야 한다.

| field | why | example |
|---|---|---|
| `entry_date` | as_of 기준과 forward window 계산 기준 | `2024-05-10` |
| `entry_price` | MFE/MAE 계산 기준 가격 | `21700` |
| `trigger_type` | Stage2/4B/4C/반례 분류 | `Stage2` |
| `MFE_30D_pct`, `MAE_30D_pct` | 단기 성공/위험 경로 | `12.4`, `-6.8` |
| `MFE_90D_pct`, `MAE_90D_pct` | 주요 정규화 경로 | `28.1`, `-13.2` |
| `MFE_180D_pct`, `MAE_180D_pct` | 중기 durability 확인 | `42.0`, `-19.5` |
| `large_sector_id`, `canonical_archetype_id` | runtime weight 직접 매칭 | `L5_CONSUMER_BRAND_DISTRIBUTION`, `C19_BRAND_RETAIL_INVENTORY_MARGIN` |
| `evidence_source` 또는 `source_url` | 가격만 오른 row 차단 | 공시 URL, 실적발표, 수출 데이터, 계약 뉴스 |
| `inventory_growth_pct`, `revenue_growth_pct`, `opm_change_pctp`, `receivables_growth_pct` | 재고 증가가 성장인지 channel stuffing인지 분리 | 재고 +10%, 매출 +40%, OPM 상승이면 성장 재고 가능 |

## TODO

- compact short filename 23개는 원본 가격경로에서 30/90/180D MFE/MAE를 재계산해 표준 V12 result MD 형식으로 repair할 때만 반영한다.
- result MD 안에서도 `mfe_pct/mae_pct`만 있거나 90D만 있는 partial path row는 이제 valid가 아니다. 새 연구/repair에서 6개 필드를 모두 채운다.
- 자동연구 프롬프트는 표준 파일명과 필수 MFE/MAE를 강제한다. 새 연구에서 이 형식을 깨면 goal 전에 repair 대상이 된다.
- C26, C18, C29~C32, C04, C15, C20, C21, C22, C25처럼 10 row 미만 또는 30 row 미만인 아키타입을 먼저 채운다.
- 재고율, 매출성장률, OPM 변화, 매출채권 변화는 가능한 모든 소비재/유통/제조 row에 같이 넣는다.
- Stage 3-Green 완화보다 Stage2 bridge, 4B watch, hard 4C 확인 품질을 우선한다.

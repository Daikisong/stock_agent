# V12 Research No-Repeat Index

이 문서는 새 자동연구 세션을 시작할 때 먼저 읽는 중복 방지 장부다.
목적은 같은 대섹터/아키타입 안에서 같은 종목, 같은 날짜, 같은 trigger를 반복 연구하지 않게 하는 것이다.

쉬운 예시:

```text
이미 C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / 257720 / Stage3-Green / 2024-05-10 이 들어왔다.
다음 연구는 같은 조합을 다시 쓰지 말고, 새 종목, 새 날짜, 새 trigger family, 또는 4B/4C/반례를 찾아야 한다.
```

last_updated: `2026-06-11`

## 현재 결론

`docs/core/goal.md`의 표준 명령은 현재 기준으로 정규화 가능한 V12 연구 row를 모두 사용한다.
`docs/round/achieve`와 `docs/round/achieve_v12`는 완료 보관분이라 discovery에서 제외한다.
파일명이 표준 v12 research 결과라면 제목에 Prompt가 있어도 ingest한다. 실제 prompt/spec 파일명만 제외한다.
가격경로나 trigger 종류가 부족한 row는 deterministic scorer가 임의 추정하지 않고 rejected ledger에 남긴다.

쉬운 예시:

```text
사용 가능: entry_date, entry_price, trigger_type, 30/90/180D MFE/MAE, large_sector_id, canonical_archetype_id가 모두 있음
사용 불가: 종목 설명과 entry_price만 있고 MFE_30D_pct/MAE_90D_pct가 없음
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
| `data/e2r/calibration/v12/v12_patch_specs.jsonl` | 실제 profile 반영 specs |
| `reports/e2r_calibration/v12/coverage_matrix.md` | scope별 coverage 요약 |
| `reports/e2r_calibration/v12/archetype_weight_runtime_report.md` | 아키타입별 점수비중 산출 결과 |

## 이번 배치 반영 메모

| item | result |
|---|---:|
| run command | `run-v12-calibration --md-input-root docs/round` |
| discovered markdown docs | 373 |
| v12 result MD | 373 |
| prompt/spec excluded | 0 |
| parser failures | 0 |
| metadata only docs | 0 |
| zero trigger result docs | 0 |
| raw trigger rows | 3248 |
| validated rows | 2988 |
| representative rows | 2416 |
| valid/representative rows missing required MFE/MAE | 0/0 |
| rejected rows | 1059 |
| stage transition rows | 1990 |
| promotion decisions | 67 |
| apply_next_patch decisions | 52 |
| blocked_by_data_quality decisions | 15 |
| hold_for_more_evidence decisions | 0 |
| applied patch specs | 52 |
| active profile selector | `e2r_2_2` |
| rolling profile id | `e2r_2_2_rolling_calibrated` |
| production default scoring changed | true |
| archetype weight count | 36 |
| large sector weight count | 10 |
| unknown canonical archetype before runtime profile | 0 |
| unknown large sector before runtime profile | 0 |

## Corpus Snapshot

| metric | value |
|---|---:|
| representative row_count | 2416 |
| unique_case_count | 1389 |
| unique_symbol_count | 443 |
| unique_round_count | 13 |
| positive_case_count | 45 |
| counterexample_count | 395 |
| 4B_case_count | 210 |
| 4C_case_count | 55 |
| good_stage2_count | 562 |
| bad_stage2_count | 526 |
| source_proxy_only_count | 1340 |
| evidence_url_pending_count | 1506 |
| current_profile_error_count | 706 |
| current_profile_false_positive_count | 598 |
| current_profile_too_late_count | 48 |
| stage2 hit rate MFE90 >= 20% | 0.4774 |
| stage2 bad entry rate MAE90 <= -20% | 0.3801 |
| avg Stage2 MFE90 | 26.0161 |
| avg Stage2 MAE90 | -17.5391 |
| canonical_archetypes_covered by representative rows | 36 |

## Goal 사용 범위 점검

| 구분 | row/docs | 현재 처리 | 판단 |
|---|---:|---|---|
| 표준 V12 result MD | 373 docs | ingest 대상 | 사용됨 |
| prompt/spec excluded | 0 docs | 파일명 기준 제외만 적용 | 현재 제외 없음 |
| archive docs | - | `achieve`, `achieve_v12` 제외 | 사용 안 함 |
| raw trigger | 3248 rows | validation 수행 | 조건 통과분만 사용 |
| validated trigger | 2988 rows | dedupe 후보 | 사용됨 |
| representative trigger | 2416 rows | aggregate/weight/profile 입력 | 최종 사용 |
| valid/representative 중 필수 MFE/MAE 누락 | 0/0 rows | strict gate | 사용되지 않음 |
| unknown canonical archetype | 0 | runtime seed 직접 매칭 | 통과 |
| unknown large sector | 0 | runtime seed 직접 매칭 | 통과 |

## 주요 rejected reason

Rejected row는 버리는 데이터가 아니라 다음 정규화 TODO다. 예를 들어 `missing_required_mfe_mae`는 가격경로 30D/90D/180D가 부족해서 score 보정에 못 쓴다는 뜻이다.

| reason | rows | 쉬운 뜻 |
|---|---:|---|
| `not_representative_for_aggregate` | 490 | 중복 그룹의 대표 row가 아니거나 aggregate 제외 표시 |
| `not_usable_for_promotion` | 315 | positive 승격 근거로 쓰기에는 비가격 증거/품질이 부족 |
| `missing_required_mfe_mae` | 217 | 30/90/180일 MFE/MAE가 모두 없어 성공/실패 경로 비교 불가 |
| `missing_trigger_type` | 184 | Stage2/4B/4C 등 trigger 종류 없음 |
| `corporate_action_contaminated` | 36 | 액면분할/합병 등 corporate action 영향 가능성 |
| `price_only_no_evidence` | 20 | 가격 움직임만 있고 비가격 증거 부족 |
| `missing_entry_date` | 13 | 진입일 없음 |
| `missing_entry_price` | 10 | 진입가 없음 |
| `insufficient_forward_window` | 4 | as_of 이후 충분한 forward window가 없음 |

### missing_required_mfe_mae 세부 출처

| source_row_type | rows |
|---|---:|
| `trigger` | 207 |
| `v12_review_only_audit` | 10 |

## 반영된 safe patch 축

| axis | applied specs | 쉬운 뜻 |
|---|---:|---|
| `earlier_thesis_break_watch` | 2 | 논리 훼손 조짐을 더 일찍 watch로 표시 |
| `hard_4c_confirmation` | 1 | 비가격 thesis break가 확인되면 4C를 더 명확히 표시 |
| `local_4b_watch_guard` | 13 | 가격만 오른 4B는 full 4B보다 watch로 제한 |
| `stage2_required_bridge` | 36 | Stage2로 올리려면 가격 말고 수주/실적/계약/마진 같은 bridge를 요구 |

## Promotion Decision 요약

| decision | count | 의미 |
|---|---:|---|
| `apply_next_patch` | 52 | 지금 profile에 작은 scope patch로 반영 |
| `blocked_by_data_quality` | 15 | URL/proxy/가격경로 등 품질 보강 필요 |

## 대섹터별 대표 row 수

| large_sector | rows | symbols | positives/counter | 4B/4C | URL pending/proxy |
|---|---:|---:|---:|---:|---:|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 859 | 213 | 12/104 | 63/27 | 449/430 |
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 209 | 63 | 0/44 | 37/3 | 142/136 |
| L2_AI_SEMICONDUCTOR_ELECTRONICS | 108 | 48 | 0/40 | 7/0 | 108/58 |
| L3_BATTERY_EV_GREEN_MOBILITY | 209 | 43 | 12/76 | 33/19 | 153/146 |
| L4_MATERIALS_SPREAD_RESOURCE | 226 | 70 | 1/23 | 11/3 | 130/130 |
| L5_CONSUMER_BRAND_DISTRIBUTION | 225 | 47 | 7/16 | 23/0 | 145/121 |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 139 | 29 | 7/23 | 8/0 | 96/72 |
| L7_BIO_HEALTHCARE_MEDICAL | 174 | 53 | 1/22 | 12/0 | 142/117 |
| L8_PLATFORM_CONTENT_SW_SECURITY | 182 | 69 | 2/33 | 11/2 | 103/99 |
| L9_CONSTRUCTION_REALESTATE_HOUSING | 85 | 20 | 3/14 | 5/1 | 38/31 |

## 다음 연구 우선순위

자동연구원은 R1~R13을 기계적으로 순환하지 말고, 아래 아키타입별 수량을 먼저 본다. Round는 연구 대상을 고른 뒤 파일명/대섹터 일관성을 맞추기 위해 따라오는 metadata다.

| target | meaning | current shortage |
|---|---|---:|
| 30 rows per C01~C32 archetype | 최소 안정권. 방향성을 보기 시작 | 126 |
| 50 rows per C01~C32 archetype | 실전 보정권. positive/counterexample/4B/4C 균형 확인 | 331 |
| 80 rows per C01~C32 archetype | 탄탄한 권역. 새 row가 들어와도 weight가 덜 흔들림 | 903 |

### Priority 0: 30 row 미만부터 채우기

| priority | archetype | rows | need to 30 | need to 50 | 조사 포인트 |
|---:|---|---:|---:|---:|---|
| 1 | C02_POWER_GRID_DATACENTER_CAPEX | 10 | 20 | 40 | 전력망/데이터센터 CAPEX, backlog, CAPA lock, ASP와 납기 visibility |
| 2 | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 10 | 20 | 40 | 장비 valuation 과열, 수주 없는 price blowoff, 4B/4C 전환 |
| 3 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 11 | 19 | 39 | EV 수요 둔화, utilization, call-off, hard 4C 확인 |
| 4 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 13 | 17 | 37 | 메모리 회복 beta와 실제 장비 order cycle reversal 분리 |
| 5 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 17 | 13 | 33 | HBM 고객, CAPA, mix, ASP, revision, cycle 반례 |
| 6 | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 18 | 12 | 32 | HBM 장비 상대강도와 실제 order/revenue conversion |
| 7 | C11_BATTERY_ORDERBOOK_RERATING | 18 | 12 | 32 | 배터리 orderbook이 margin/FCF로 전환되는지 검증 |
| 8 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 19 | 11 | 31 | 수주잔고 + 마진 bridge + FCF 전환 |
| 9 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 28 | 2 | 22 | 보안 계약, ARR, retention, renewal, margin leverage |

### Priority 1: 50 row까지 끌어올리기

| archetype | rows | need to 50 | 조사 포인트 |
|---|---:|---:|---|
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 32 | 18 | 고객 계약과 call-off/demand risk, AMPC/IRA와 분리 |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 47 | 3 | EPC mega 계약, 원가초과, working capital, margin gap |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 48 | 2 | 승인 이후 상업화, 매출/royalty/reimbursement 전환 |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 48 | 2 | IP 매출화, 글로벌 플랫폼 전환, 일회성 흥행 반례 |

### Priority 2: 50 row 이상은 품질 보강 중심

| archetype | rows | guidance |
|---|---:|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 118 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 106 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 97 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 94 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 90 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 85 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 82 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 79 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 78 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 73 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 71 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 71 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 69 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 62 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 60 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 58 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 57 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 50 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 50 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |

### R13 특수 범위

R13은 일반 Green unlock 연구가 아니다. cross-archetype guardrail 검증이 필요할 때만 한다.

| R13 scope | rows | guidance |
|---|---:|---|
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 153 | Stage2 false positive, accounting trust, high MAE, 4B/4C red-team 검증용으로만 추가 |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 191 | Stage2 false positive, accounting trust, high MAE, 4B/4C red-team 검증용으로만 추가 |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 143 | Stage2 false positive, accounting trust, high MAE, 4B/4C red-team 검증용으로만 추가 |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 160 | Stage2 false positive, accounting trust, high MAE, 4B/4C red-team 검증용으로만 추가 |

## 아키타입별 현재 커버리지와 점수비중

| archetype | rows | symbols | positives/counter | 4B/4C | S2 hit/bad | weights EPS/Vis/Bott/Mis/Val/Cap/Info | top covered symbols |
|---|---:|---:|---:|---:|---:|---|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 19 | 16 | 0/0 | 3/0 | 0.3333/0.25 | 20/25/18/12/12/8/5 | 012450(2), 064350(2), 079550(2), 000720(1), 004960(1), 006360(1) |
| C02_POWER_GRID_DATACENTER_CAPEX | 10 | 10 | 0/0 | 0/0 | 1/0 | 21/24/20/13/12/5/5 | 000500(1), 001440(1), 006260(1), 010120(1), 017510(1), 024840(1) |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 62 | 16 | 0/12 | 15/2 | 0.7/0.1667 | 20/24/17/14/14/6/5 | 012450(12), 079550(11), 064350(10), 272210(7), 047810(4), 003570(3) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 71 | 16 | 0/32 | 12/0 | 0.3784/0.4865 | 15/22/10/15/18/10/10 | 051600(11), 052690(11), 034020(6), 105840(6), 011700(4), 032820(4) |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 47 | 21 | 0/0 | 7/1 | 0.1429/0.2143 | 18/22/10/12/10/8/20 | 000720(5), 006360(5), 028050(5), 047040(5), 375500(5), 294870(4) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 17 | 17 | 0/17 | 2/0 | 0.8462/0.2308 | 24/21/19/15/12/4/5 | 031980(1), 036810(1), 036930(1), 039030(1), 042700(1), 067310(1) |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 18 | 18 | 0/0 | 0/0 | 0.8571/0.2143 | 22/22/19/14/12/6/5 | 031980(1), 036810(1), 036930(1), 039030(1), 042700(1), 067310(1) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 50 | 43 | 0/0 | 0/0 | 0.5/0.5 | 22/21/16/14/12/6/9 | 058470(2), 067310(2), 092870(2), 095340(2), 131970(2), 232140(2) |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 10 | 10 | 0/10 | 3/0 | 0.75/0.5 | 22/20/18/13/11/6/10 | 031980(1), 036810(1), 039030(1), 042700(1), 079370(1), 089030(1) |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 13 | 13 | 0/13 | 2/0 | 0.9091/0.1818 | 22/18/14/12/10/5/19 | 036810(1), 036930(1), 067310(1), 079370(1), 084370(1), 095610(1) |
| C11_BATTERY_ORDERBOOK_RERATING | 18 | 18 | 0/18 | 6/3 | 0.5556/0.4444 | 20/20/15/12/10/8/15 | 002710(1), 005070(1), 011790(1), 020150(1), 051910(1), 066970(1) |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 32 | 20 | 1/16 | 4/2 | 0.4286/0.5714 | 20/18/14/10/10/8/20 | 373220(4), 011790(3), 361610(3), 006400(2), 020150(2), 066970(2) |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 58 | 24 | 3/9 | 11/7 | 0.6/0.36 | 20/18/14/12/10/10/16 | 011790(4), 066970(4), 121600(4), 361610(4), 373220(4), 001570(3) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 11 | 11 | 0/11 | 3/4 | -/- | 15/12/10/8/8/7/40 | 001570(1), 002710(1), 020150(1), 051910(1), 066970(1), 078600(1) |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 73 | 35 | 1/16 | 3/3 | 0.5227/0.3409 | 20/12/20/10/10/8/20 | 103140(6), 010130(5), 010950(4), 011790(4), 002380(3), 006110(3) |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 82 | 37 | 0/3 | 8/0 | 0.4444/0.5111 | 18/18/18/12/12/7/15 | 047050(6), 001120(4), 005490(4), 006260(4), 000500(3), 001440(3) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 71 | 39 | 0/4 | 0/0 | 0.4615/0.3846 | 20/12/18/10/10/5/25 | 010950(5), 011790(5), 002380(4), 009830(4), 051910(4), 161000(4) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 97 | 39 | 4/2 | 7/0 | 0.4906/0.283 | 22/23/12/16/13/4/10 | 003230(7), 004370(6), 005180(6), 383220(6), 090430(5), 097950(5) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 50 | 34 | 0/0 | 6/0 | 0.4737/0.1053 | 18/18/8/15/14/7/20 | 383220(4), 069960(3), 005390(2), 007980(2), 031430(2), 036620(2) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 78 | 34 | 3/14 | 10/0 | 0.641/0.1795 | 22/23/12/16/13/4/10 | 003230(7), 090430(7), 005180(5), 161890(5), 192820(5), 004370(4) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 79 | 23 | 0/8 | 1/0 | 0.2708/0.0417 | 15/20/5/15/25/15/5 | 105560(9), 055550(7), 316140(7), 005940(6), 005830(5), 006800(4) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 60 | 17 | 7/15 | 7/0 | 0.3462/0.0769 | 12/22/5/14/24/18/5 | 005830(9), 088350(8), 032830(7), 003690(6), 000810(5), 001450(5) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 48 | 21 | 0/0 | 0/0 | 0.4571/0.2286 | 12/24/5/12/10/7/30 | 006280(5), 170900(5), 326030(5), 069620(3), 084990(3), 128940(3) |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 69 | 34 | 0/0 | 9/0 | 0.4/0.4444 | 5/15/5/10/5/5/55 | 128940(5), 141080(5), 196170(5), 084990(4), 028300(3), 069620(3) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 57 | 25 | 1/22 | 3/0 | 0.4444/0.6111 | 20/22/13/14/12/9/10 | 043150(5), 228670(4), 335890(4), 041830(3), 065510(3), 099190(3) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 106 | 30 | 2/4 | 2/0 | 0.4603/0.3968 | 20/22/8/16/14/10/10 | 067160(11), 030000(10), 035720(10), 216050(9), 214270(8), 035420(7) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 48 | 30 | 0/9 | 4/2 | 0.3333/0.625 | 20/18/8/14/12/8/20 | 293490(3), 352820(3), 035760(2), 035900(2), 036420(2), 041510(2) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 28 | 23 | 0/20 | 5/0 | 0.375/0.5625 | 20/24/8/16/14/8/10 | 012510(2), 030520(2), 042510(2), 047560(2), 263860(2), 018260(1) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 90 | 17 | 8/22 | 9/3 | 0.439/0.2439 | 20/18/10/15/17/15/5 | 204320(11), 005380(10), 011210(9), 000270(8), 012330(8), 010690(7) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 85 | 20 | 3/14 | 5/1 | 0.2051/0.2564 | 18/12/8/12/10/10/30 | 047040(16), 294870(11), 000720(10), 375500(8), 006360(6), 002990(5) |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 118 | 58 | 9/9 | 1/0 | 0.4286/0.1786 | 12/15/8/15/15/10/25 | 105560(8), 005830(6), 316140(6), 088350(5), 000810(4), 055550(4) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 94 | 45 | 0/0 | 1/0 | 0.46/0.36 | 12/18/5/20/25/15/5 | 028260(6), 040300(6), 041510(6), 010130(5), 036560(5), 005940(4) |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 153 | 95 | 2/38 | 33/18 | 0.5909/0.4773 | 8/12/8/10/8/4/50 | 003230(4), 034020(4), 294870(4), 361610(4), 000270(3), 005380(3) |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 191 | 113 | 0/27 | 16/2 | 0.6705/0.3864 | 8/12/5/10/8/20/37 | 003230(7), 294870(7), 005380(6), 035420(6), 028300(4), 034020(4) |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 143 | 93 | 0/16 | 12/7 | 0.5484/0.5645 | 10/14/8/12/10/6/40 | 034020(4), 003230(3), 006110(3), 010690(3), 051910(3), 214270(3) |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 160 | 109 | 1/14 | 0/0 | 0.431/0.6897 | 10/14/8/12/10/6/40 | 003230(4), 051910(4), 005380(3), 006800(3), 009830(3), 011170(3) |

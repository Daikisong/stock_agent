# V12 Research No-Repeat Index

이 문서는 새 자동연구 세션을 시작할 때 먼저 읽는 중복 방지 장부다.
목적은 같은 대섹터/아키타입 안에서 같은 종목, 같은 날짜, 같은 trigger를 반복 연구하지 않게 하는 것이다.

쉬운 예시:

```text
이미 C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / 257720 / Stage3-Green / 2024-05-10 이 들어왔다.
다음 연구는 같은 조합을 다시 쓰지 말고, 새 종목, 새 날짜, 새 trigger family, 또는 4B/4C/반례를 찾아야 한다.
```

last_updated: `2026-06-13`

## 현재 결론

`docs/core/goal.md`의 표준 명령을 `docs/round`에 대해 실행했고, `docs/round/achieve`와 `docs/round/achieve_v12`는 discovery 단계에서 제외됐다.
파일명이 표준 v12 research 결과라면 ingest 대상이고, 이번에 섞여 있던 메모장/프롬프트 성격의 MD 4개는 prompt/spec로 분류되어 제외됐다.
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
| discovered markdown docs | 234 |
| v12 result MD | 230 |
| prompt/spec excluded | 4 |
| non-result non-prompt docs | 0 |
| parser failures | 0 |
| metadata only docs | 0 |
| zero trigger result docs | 0 |
| raw trigger rows | 2548 |
| validated rows | 2245 |
| representative rows | 2222 |
| valid/representative rows missing required MFE/MAE | 0/0 |
| rejected rows | 721 |
| raw aggregate metric rows | 115 |
| raw shadow weight rows | 203 |
| stage transition rows | 2127 |
| promotion decisions | 89 |
| apply_next_patch decisions | 84 |
| blocked_by_data_quality decisions | 1 |
| blocked_by_logic_risk decisions | 0 |
| hold_for_more_evidence decisions | 4 |
| applied patch specs | 84 |
| active profile selector | `e2r_2_2` |
| rolling profile id | `e2r_2_2_rolling_calibrated` |
| production default scoring changed | true |
| stage3 green not loosened | true |
| archetype weight count | 36 |
| large sector weight count | 10 |
| unknown canonical archetype before runtime profile | 0 |
| unknown large sector before runtime profile | 0 |

## Corpus Snapshot

| metric | value |
|---|---:|
| representative row_count | 2222 |
| unique_case_count | 1923 |
| unique_symbol_count | 559 |
| unique_round_count | 13 |
| positive_case_count | 200 |
| counterexample_count | 451 |
| 4B_case_count | 573 |
| 4C_case_count | 100 |
| good_stage2_count | 454 |
| bad_stage2_count | 438 |
| source_proxy_only_count | 36 |
| evidence_url_pending_count | 34 |
| current_profile_error_count | 1074 |
| current_profile_false_positive_count | 651 |
| current_profile_too_late_count | 142 |
| stage2 hit rate MFE90 >= 20% | 0.5349 |
| stage2 bad entry rate MAE90 <= -20% | 0.4557 |
| avg Stage2 MFE90 | 35.8708 |
| avg Stage2 MAE90 | -19.6927 |
| canonical_archetypes_covered by representative rows | 36 |

## Goal 사용 범위 점검

| 구분 | row/docs | 현재 처리 | 판단 |
|---|---:|---|---|
| 표준 V12 result MD | 230 docs | ingest 대상 | 사용됨 |
| prompt/spec excluded | 4 docs | 파일명/제목 기준 제외 | 사용 안 함 |
| archive docs | - | `achieve`, `achieve_v12` 제외 | 사용 안 함 |
| raw trigger | 2548 rows | validation 수행 | 조건 통과분만 사용 |
| validated trigger | 2245 rows | dedupe 후보 | 사용됨 |
| representative trigger | 2222 rows | aggregate/weight/profile 입력 | 최종 사용 |
| valid/representative 중 필수 MFE/MAE 누락 | 0/0 rows | strict gate | 사용되지 않음 |
| unknown canonical archetype | 0 | runtime seed 직접 매칭 | 통과 |
| unknown large sector | 0 | runtime seed 직접 매칭 | 통과 |

## 주요 rejected reason

Rejected row는 버리는 데이터가 아니라 다음 정규화 TODO다. 예를 들어 `missing_required_mfe_mae`는 가격경로 30D/90D/180D가 부족해서 score 보정에 못 쓴다는 뜻이다.

| reason | rows | 쉬운 뜻 |
|---|---:|---|
| `not_usable_for_promotion` | 335 | positive 승격 근거로 쓰기에는 비가격 증거/품질이 부족 |
| `missing_trigger_type` | 224 | Stage2/4B/4C 등 trigger 종류 없음 |
| `missing_required_mfe_mae` | 154 | 30/90/180일 MFE/MAE가 모두 없어 성공/실패 경로 비교 불가 |
| `price_only_no_evidence` | 81 | 가격 움직임만 있고 비가격 증거 부족 |
| `not_representative_for_aggregate` | 29 | 중복 그룹의 대표 row가 아니거나 aggregate 제외 표시 |
| `corporate_action_contaminated` | 19 | 액면분할/합병 등 corporate action 영향 가능성 |
| `raw_all_basis` | 12 | raw all basis라 tradable raw 기준이 아님 |
| `missing_entry_price` | 12 | 진입가 없음 |
| `missing_entry_date` | 12 | 진입일 없음 |
| `invalid_price_source` | 5 | 허용된 Stock-Web 가격 출처가 아님 |
| `insufficient_forward_window` | 1 | as_of 이후 충분한 forward window가 없음 |

### missing_required_mfe_mae 세부 출처

| source_row_type | rows |
|---|---:|
| `trigger` | 135 |
| `v12_review_only_audit` | 12 |
| `v12_compact_case` | 7 |

## 반영된 safe patch 축

| axis | applied specs | 쉬운 뜻 |
|---|---:|---|
| `earlier_thesis_break_watch` | 14 | 논리 훼손 조짐을 더 일찍 watch로 표시 |
| `full_4b_overlay_candidate` | 2 | full 4B는 비가격 증거가 있을 때만 후보로 인정 |
| `hard_4c_confirmation` | 3 | 비가격 thesis break가 확인되면 4C를 더 명확히 표시 |
| `local_4b_watch_guard` | 23 | 가격만 오른 4B는 full 4B보다 watch로 제한 |
| `stage2_bonus_candidate_delta` | 1 | 비가격 증거가 있을 때 해당 scope Stage2 근처에 제한적 보너스 후보 |
| `stage2_required_bridge` | 41 | Stage2로 올리려면 가격 말고 수주/실적/계약/마진 같은 bridge를 요구 |

## Promotion Decision 요약

| decision | count | 의미 |
|---|---:|---|
| `apply_next_patch` | 84 | 지금 profile에 작은 scope patch로 반영 |
| `hold_for_more_evidence` | 4 | 근거 수나 전이 경로가 부족 |
| `blocked_by_data_quality` | 1 | URL/proxy/가격경로 등 품질 보강 필요 |

## 대섹터별 대표 row 수

| large_sector | rows | symbols | positives/counter | 4B/4C | URL pending/proxy |
|---|---:|---:|---:|---:|---:|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 1090 | 376 | 35/233 | 401/51 | 13/23 |
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 238 | 115 | 35/38 | 33/5 | 21/3 |
| L2_AI_SEMICONDUCTOR_ELECTRONICS | 256 | 92 | 43/52 | 44/2 | 0/1 |
| L3_BATTERY_EV_GREEN_MOBILITY | 235 | 87 | 45/63 | 49/21 | 0/5 |
| L4_MATERIALS_SPREAD_RESOURCE | 69 | 35 | 3/3 | 9/5 | 0/4 |
| L5_CONSUMER_BRAND_DISTRIBUTION | 72 | 41 | 13/11 | 10/1 | 0/0 |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 48 | 21 | 0/0 | 1/2 | 0/0 |
| L7_BIO_HEALTHCARE_MEDICAL | 70 | 39 | 7/7 | 6/3 | 0/0 |
| L8_PLATFORM_CONTENT_SW_SECURITY | 105 | 58 | 13/38 | 14/3 | 0/0 |
| L9_CONSTRUCTION_REALESTATE_HOUSING | 39 | 18 | 6/6 | 6/7 | 0/0 |

## 아키타입별 row와 점수비중

weight 표기는 `EPS/Vis/Bott/Mis/Val/Cap/Info` 순서다. diff는 기본형 `20/20/20/15/15/5/5` 대비 변화다.

| archetype | rows | symbols | positives/counter | 4B/4C | weights | diff | top symbols |
|---|---:|---:|---:|---:|---|---|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 53 | 24 | 12/6 | 5/1 | 20/25/18/12/12/8/5 | 0/+5/-2/-3/-3/+3/0 | 033500(5), 075580(5), 443060(4), 042660(3), 073010(3), 097230(3) |
| C02_POWER_GRID_DATACENTER_CAPEX | 59 | 25 | 11/9 | 18/0 | 21/24/20/13/12/5/5 | +1/+4/0/-2/-3/0/0 | 033100(5), 103590(5), 267260(5), 006340(4), 017040(4), 298040(4) |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 46 | 21 | 0/8 | 0/0 | 20/24/17/14/14/6/5 | 0/+4/-3/-1/-1/+1/0 | 012450(5), 047810(4), 064350(4), 079550(4), 003570(3), 010820(3) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 25 | 15 | 0/0 | 0/1 | 15/22/10/15/18/10/10 | -5/+2/-10/0/+3/+5/+5 | 034020(3), 052690(3), 083650(3), 011700(2), 032820(2), 051600(2) |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 55 | 36 | 12/15 | 10/3 | 18/22/10/12/10/8/20 | -2/+2/-10/-3/-5/+3/+15 | 000720(4), 047040(4), 375500(4), 006360(3), 013580(2), 001260(1) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 46 | 21 | 6/11 | 8/1 | 24/21/19/15/12/4/5 | +4/+1/-1/0/-3/-1/0 | 000660(12), 005930(12), 007660(2), 009150(2), 353200(2), 007810(1) |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 32 | 24 | 5/5 | 12/0 | 22/22/19/14/12/6/5 | +2/+2/-1/-1/-3/+1/0 | 025560(3), 042700(3), 031980(2), 039440(2), 168360(2), 322310(2) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 28 | 16 | 9/7 | 8/0 | 22/21/16/14/12/6/9 | +2/+1/-4/-1/-3/+1/+4 | 058470(4), 095340(4), 098120(2), 131290(2), 131970(2), 252990(2) |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 96 | 41 | 16/19 | 9/1 | 22/20/18/13/11/6/10 | +2/0/-2/-2/-4/+1/+5 | 064290(5), 403870(5), 110990(4), 272110(4), 036810(3), 084370(3) |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 54 | 35 | 7/10 | 7/0 | 22/18/14/12/10/5/19 | +2/-2/-6/-3/-5/0/+14 | 064760(3), 084370(3), 095610(3), 067310(2), 074600(2), 089970(2) |
| C11_BATTERY_ORDERBOOK_RERATING | 56 | 46 | 3/4 | 7/1 | 20/20/15/12/10/8/15 | 0/0/-5/-3/-5/+3/+10 | 302430(3), 003670(2), 079810(2), 251630(2), 254120(2), 333620(2) |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 68 | 58 | 15/25 | 10/4 | 20/18/14/10/10/8/20 | 0/-2/-6/-5/-5/+3/+15 | 002710(2), 014820(2), 078600(2), 079810(2), 091580(2), 093370(2) |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 23 | 12 | 2/6 | 3/3 | 20/18/14/12/10/10/16 | 0/-2/-6/-3/-5/+5/+11 | 006400(2), 051910(2), 096770(2), 373220(2), 003670(1), 011790(1) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 62 | 34 | 17/24 | 26/11 | 15/12/10/8/8/7/40 | -5/-8/-10/-7/-7/+2/+35 | 020150(3), 066970(3), 393890(3), 003670(2), 005070(2), 006400(2) |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 24 | 16 | 3/3 | 6/1 | 20/12/20/10/10/8/20 | 0/-8/0/-5/-5/+3/+15 | 005490(4), 004020(3), 002710(2), 103140(2), 306200(2), 001430(1) |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 21 | 14 | 0/0 | 3/0 | 18/18/18/12/12/7/15 | -2/-2/-2/-3/-3/+2/+10 | 005490(4), 010130(3), 001120(2), 011810(2), 002360(1), 006260(1) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 24 | 10 | 0/0 | 0/4 | 20/12/18/10/10/5/25 | 0/-8/-2/-5/-5/0/+20 | 011170(4), 051910(4), 004000(2), 006650(2), 009830(2), 010060(2) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 27 | 16 | 5/5 | 3/0 | 22/23/12/16/13/4/10 | +2/+3/-8/+1/-2/-1/+5 | 280360(3), 001680(2), 003230(2), 004370(2), 017810(2), 105630(2) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 22 | 15 | 3/3 | 5/1 | 18/18/8/15/14/7/20 | -2/-2/-12/0/-1/+2/+15 | 004170(2), 020000(2), 023530(2), 031430(2), 069960(2), 139480(2) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 23 | 13 | 5/3 | 2/0 | 22/23/12/16/13/4/10 | +2/+3/-8/+1/-2/-1/+5 | 214420(3), 257720(3), 003230(2), 051900(2), 090430(2), 192820(2) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 25 | 10 | 0/0 | 0/0 | 15/20/5/15/25/15/5 | -5/0/-15/0/+10/+10/0 | 039490(4), 138040(4), 086790(3), 138930(3), 175330(3), 024110(2) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 23 | 12 | 0/0 | 1/2 | 12/22/5/14/24/18/5 | -8/+2/-15/-1/+9/+13/0 | 000370(3), 000400(2), 000540(2), 000810(2), 001450(2), 003690(2) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 27 | 14 | 0/0 | 2/0 | 12/24/5/12/10/7/30 | -8/+4/-15/-3/-5/+2/+25 | 006280(3), 069620(3), 000100(2), 068270(2), 128940(2), 145020(2) |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 22 | 13 | 4/4 | 4/3 | 5/15/5/10/5/5/55 | -15/-5/-15/-5/-10/0/+50 | 028300(5), 196170(4), 009420(2), 039200(2), 000100(1), 084990(1) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 21 | 15 | 3/3 | 0/0 | 20/22/13/14/12/9/10 | 0/+2/-7/-1/-3/+4/+5 | 099190(3), 145720(2), 206640(2), 214150(2), 338220(2), 039860(1) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 36 | 14 | 5/18 | 5/0 | 20/22/8/16/14/10/10 | 0/+2/-12/+1/-1/+5/+5 | 035420(6), 035720(4), 067160(4), 030000(3), 237820(3), 273060(3) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 28 | 15 | 4/9 | 5/2 | 20/18/8/14/12/8/20 | 0/-2/-12/-1/-3/+3/+15 | 122870(3), 194480(3), 251270(3), 259960(3), 095660(2), 112040(2) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 41 | 29 | 4/11 | 4/1 | 20/24/8/16/14/8/10 | 0/+4/-12/+1/-1/+3/+5 | 042510(3), 263860(3), 067920(2), 079940(2), 136540(2), 150900(2) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 26 | 14 | 8/4 | 3/2 | 20/18/10/15/17/15/5 | 0/-2/-10/0/+2/+10/0 | 000270(3), 073240(3), 161390(3), 002350(2), 005380(2), 011210(2) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 39 | 18 | 6/6 | 6/7 | 18/12/8/12/10/10/30 | -2/-8/-12/-3/-5/+5/+25 | 047040(5), 375500(5), 006360(3), 014790(3), 294870(3), 002990(2) |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 24 | 24 | 5/4 | 0/0 | 12/15/8/15/15/10/25 | -8/-5/-12/0/0/+5/+20 | 000990(1), 015760(1), 032620(1), 032850(1), 036540(1), 041190(1) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 46 | 13 | 0/0 | 7/3 | 12/18/5/20/25/15/5 | -8/-2/-15/+5/+10/+10/0 | 241560(7), 000150(6), 454910(6), 008930(5), 041510(5), 028260(4) |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 216 | 159 | 15/33 | 53/18 | 8/12/8/10/8/4/50 | -12/-8/-12/-5/-7/-1/+45 | 028300(4), 051910(4), 196170(4), 393890(4), 006280(3), 069620(3) |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 339 | 238 | 12/55 | 144/23 | 8/12/5/10/8/20/37 | -12/-8/-15/-5/-7/+15/+32 | 035420(5), 035720(5), 005930(4), 028300(4), 047560(4), 196170(4) |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 291 | 209 | 3/93 | 168/5 | 10/14/8/12/10/6/40 | -10/-6/-12/-3/-5/+1/+35 | 028300(4), 196170(4), 033500(3), 069620(3), 079810(3), 222800(3) |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 174 | 143 | 0/48 | 29/2 | 10/14/8/12/10/6/40 | -10/-6/-12/-3/-5/+1/+35 | 028300(4), 196170(4), 099190(3), 000100(2), 002710(2), 003230(2) |

## 다음 연구 우선순위

자동연구원은 R1~R13을 기계적으로 순환하지 말고, 아래 아키타입별 수량을 먼저 본다. Round는 연구 대상을 고른 뒤 파일명/대섹터 일관성을 맞추기 위해 따라오는 metadata다.

| target | meaning | current shortage |
|---|---|---:|
| 30 rows per C01~C32 archetype | 최소 안정권. 방향성을 보기 시작 | 97 |
| 50 rows per C01~C32 archetype | 실전 보정권. positive/counterexample/4B/4C 균형 확인 | 501 |
| 80 rows per C01~C32 archetype | 탄탄한 권역. 새 row가 들어와도 weight가 덜 흔들림 | 1374 |

### Priority 0: 30 row 미만부터 채우기

| priority | archetype | rows | need to 30 | need to 50 | need to 80 | 조사 포인트 |
|---:|---|---:|---:|---:|---:|---|
| 1 | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 21 | 9 | 29 | 59 | 전략자원 정책과 실제 supply/contract economics |
| 2 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 21 | 9 | 29 | 59 | 의료기기 수출, reimbursement, consumable/service 반복매출 |
| 3 | C19_BRAND_RETAIL_INVENTORY_MARGIN | 22 | 8 | 28 | 58 | 브랜드/리테일 sell-through, 재고, margin bridge |
| 4 | C24_BIO_TRIAL_DATA_EVENT_RISK | 22 | 8 | 28 | 58 | 임상 데이터 이벤트와 매출 전환 부재/실패 반례 |
| 5 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 23 | 7 | 27 | 57 | JV utilization, AMPC/IRA 지속성, capex/FCF 부담 |
| 6 | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 23 | 7 | 27 | 57 | K-food/K-beauty 글로벌 유통, 반복수요, OPM, EPS revision |
| 7 | C22_INSURANCE_RATE_CYCLE_RESERVE | 23 | 7 | 27 | 57 | reserve/rate cycle, ROE/PBR, 자본환원 지속성 |
| 8 | C15_MATERIAL_SPREAD_SUPERCYCLE | 24 | 6 | 26 | 56 | 소재 spread supercycle과 cost curve/reversal 반례 |
| 9 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 24 | 6 | 26 | 56 | 화학/commodity spread, inventory cycle, reversal guard |
| 10 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 24 | 6 | 26 | 56 | 정책/보조금/입법 이벤트가 cashflow로 바뀌는지 확인 |
| 11 | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 25 | 5 | 25 | 55 | 원전 정책 이벤트와 최종계약/인허가/소송 지연 구분 |
| 12 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 25 | 5 | 25 | 55 | ROE/PBR, credit cost, 실제 자본환원 |
| 13 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 26 | 4 | 24 | 54 | 모빌리티 volume/mix/margin, capital return |
| 14 | C18_CONSUMER_EXPORT_CHANNEL_REORDER | 27 | 3 | 23 | 53 | 수출 채널 reorder, 반복수요, OPM/EPS revision |
| 15 | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 27 | 3 | 23 | 53 | 승인 이후 상업화, 매출/royalty/reimbursement 전환 |
| 16 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 28 | 2 | 22 | 52 | 테스트소켓/부품 customer qualification, repeat demand, margin conversion |
| 17 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 28 | 2 | 22 | 52 | IP 매출화, 글로벌 플랫폼 전환, 일회성 흥행 반례 |

### Priority 1: 50 row까지 끌어올리기

| archetype | rows | need to 50 | need to 80 | 조사 포인트 |
|---|---:|---:|---:|---|
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 32 | 18 | 48 | HBM 장비 상대강도와 실제 order/revenue conversion |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 36 | 14 | 44 | 플랫폼 광고/ARPU/monetization과 영업레버리지 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 39 | 11 | 41 | 건설 PF/미분양/credit balance sheet break |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 41 | 9 | 39 | 보안 계약, ARR, retention, renewal, margin leverage |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 46 | 4 | 34 | 방산/정부 고객 수주, 납품 visibility, framework backlog |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 46 | 4 | 34 | HBM 고객, CAPA, mix, ASP, revision, cycle 반례 |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 46 | 4 | 34 | 지배구조/공개매수 premium과 FCF/return 전환 구분 |

### Priority 2: 50 row 이상은 품질 보강 중심

| archetype | rows | need to 80 | guidance |
|---|---:|---:|---|
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 96 | 0 | 새 종목보다 URL/proxy 보강, 반례/4B/4C 균형 확인 우선 |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 68 | 12 | 80 row까지는 새 symbol/trigger family를 추가하되, URL/proxy 품질과 반례/4B/4C 균형도 같이 보강 |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 62 | 18 | 80 row까지는 새 symbol/trigger family를 추가하되, URL/proxy 품질과 반례/4B/4C 균형도 같이 보강 |
| C02_POWER_GRID_DATACENTER_CAPEX | 59 | 21 | 80 row까지는 새 symbol/trigger family를 추가하되, URL/proxy 품질과 반례/4B/4C 균형도 같이 보강 |
| C11_BATTERY_ORDERBOOK_RERATING | 56 | 24 | 80 row까지는 새 symbol/trigger family를 추가하되, URL/proxy 품질과 반례/4B/4C 균형도 같이 보강 |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 55 | 25 | 80 row까지는 새 symbol/trigger family를 추가하되, URL/proxy 품질과 반례/4B/4C 균형도 같이 보강 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 54 | 26 | 80 row까지는 새 symbol/trigger family를 추가하되, URL/proxy 품질과 반례/4B/4C 균형도 같이 보강 |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 53 | 27 | 80 row까지는 새 symbol/trigger family를 추가하되, URL/proxy 품질과 반례/4B/4C 균형도 같이 보강 |

## 다음 실행 지침

- 연구 에이전트는 이 파일의 Priority 0/1을 먼저 보고 target archetype을 고른다.
- 같은 symbol/date/trigger family 조합을 반복하지 않는다.
- `docs/round/achieve`와 `docs/round/achieve_v12`는 완료 보관분이므로 새 실행의 입력으로 세지 않는다.
- 메모장/프롬프트 파일은 연구 result MD가 아니므로 `run-v12-calibration`에서 제외되는 것이 정상이다.
- Stage 3-Green 완화보다 Stage2 bridge, 4B watch guard, hard 4C 확인을 우선한다.

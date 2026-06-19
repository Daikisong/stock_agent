# V12 Research No-Repeat Index

이 문서는 새 자동연구 세션을 시작할 때 먼저 읽는 중복 방지 장부다.
목적은 같은 대섹터/아키타입 안에서 같은 종목, 같은 날짜, 같은 trigger를 반복 연구하지 않게 하는 것이다.

쉬운 예:

```text
이미 C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / 257720 / Stage3-Green / 2024-05-10 이 들어왔다.
다음 연구는 같은 조합을 다시 쓰지 말고, 새 종목, 새 날짜, 새 trigger family, 또는 4B/4C/반례를 찾아야 한다.
```

last_updated: `2026-06-19`

## 현재 결론

`docs/core/goal.md`의 표준 명령을 누적 기준으로 실행했다.
이번 실행은 `docs/round` root의 연구 MD와 `docs/round/achieve` 보관 연구 MD를 함께 읽기 위해 `--include-archive`를 사용했다.

누적 재계산 표준:

```bash
PYTHONPATH=src python -m e2r.calibration.cli run-v12-calibration \
  --md-input-root docs/round \
  --include-archive \
  --data-directory data/e2r/calibration/v12 \
  --report-directory reports/e2r_calibration/v12
```

이번 배치 전 preflight에서 새 root MD 182개는 모두 표준 V12 result 파일이었다.
기존 representative row와 같은 strict trigger key 중복은 0개였고, 동일 SHA 파일도 0개였다.
다만 파일명만 같은 문서 1개와 새 배치 내부 중복 trigger key 57개가 있었고, dedupe가 대표 row로 접는다.

이번에 `evidence_family`가 list로 들어온 row가 있어 dedupe key를 hash 가능한 값으로 정규화했다.
예를 들어 `["orderbook", "margin_bridge"]`와 `["margin_bridge", "orderbook"]`는 같은 evidence family로 본다.

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

## 이번 누적 배치 반영 메모

| item | result |
|---|---:|
| run command | `run-v12-calibration --md-input-root docs/round --include-archive` |
| discovered markdown docs | 2341 |
| v12 result MD | 2263 |
| prompt/spec excluded | 0 |
| non-result non-prompt docs | 78 |
| root MD under `docs/round` | 339 |
| archive MD under `docs/round/achieve` | 2002 |
| ingested root V12 result MD | 339 |
| ingested archive V12 result MD | 1924 |
| archive non-result docs excluded from ingest | 78 |
| newly untracked root MD before run | 182 |
| parser failures | 0 |
| metadata only docs | 0 |
| zero trigger result docs | 0 |
| raw trigger rows | 18760 |
| validated rows | 13738 |
| representative rows | 12471 |
| rejected rows | 8186 |
| raw aggregate metric rows | 951 |
| raw shadow weight rows | 3741 |
| stage transition rows | 10660 |
| promotion decisions | 133 |
| apply_next_patch decisions | 112 |
| blocked_by_data_quality decisions | 21 |
| applied patch specs | 112 |
| active profile selector | `e2r_2_2` |
| rolling profile id | `e2r_2_2_rolling_calibrated` |
| production default scoring changed | true |
| stage3 green not loosened | true |
| archetype weight count | 36 |
| large sector weight count | 10 |

## Corpus Snapshot

| metric | value |
|---|---:|
| representative row_count | 12471 |
| unique_case_count | 9161 |
| unique_symbol_count | 1003 |
| unique_round_count | 13 |
| positive_case_count | 1495 |
| counterexample_count | 2628 |
| 4B_case_count | 2123 |
| 4C_case_count | 572 |
| good_stage2_count | 3329 |
| bad_stage2_count | 2438 |
| source_proxy_only_count | 3723 |
| evidence_url_pending_count | 3906 |
| current_profile_error_count | 6257 |
| current_profile_false_positive_count | 3559 |
| current_profile_too_late_count | 1680 |
| stage2 hit rate MFE90 >= 20% | 0.5846 |
| stage2 bad entry rate MAE90 <= -20% | 0.3385 |
| avg Stage2 MFE90 | 42.418 |
| avg Stage2 MAE90 | -16.3247 |
| canonical_archetypes_covered by representative rows | 36 |

## Goal 사용 범위 점검

| 구분 | row/docs | 현재 처리 | 판단 |
|---|---:|---|---|
| 표준 V12 result MD | 2263 docs | ingest 대상 | 사용됨 |
| prompt/spec excluded | 0 docs | 파일명/제목 기준 확인 | 없음 |
| non-result non-prompt docs | 78 docs | 표준 v12 result 파일명이 아님 | 사용 안 함 |
| root docs | 339 docs | root 전체 markdown | 표준 V12 result 339 docs 사용됨 |
| archive docs | 2002 docs | `docs/round/achieve` 전체 markdown | 표준 V12 result 1924 docs 사용됨 |
| raw trigger | 18760 rows | validation 수행 | 조건 통과분만 사용 |
| validated trigger | 13738 rows | dedupe 후보 | 사용됨 |
| representative trigger | 12471 rows | aggregate/weight/profile 입력 | 최종 사용 |
| newly added rows duplicate existing representative | 0 rows | strict trigger key 기준 | 중복 없음 |
| newly added identical SHA docs against archive | 0 docs | root/archive SHA 기준 | 중복 없음 |
| newly added identical SHA docs inside root | 1 group | 같은 내용 파일 2개 | dedupe 주의 항목 |
| newly added same basename docs | 1 doc | 파일명 기준 | 주의 |
| newly added internal duplicate keys | 57 keys | dedupe 대표 row로 압축 | 처리됨 |
| cumulative representative rows with duplicate members | 905 rows | 전체 누적 corpus 기준 | extra 1267 rows 접힘 |

## 주요 rejected reason

Rejected row는 버리는 데이터가 아니라 다음 정규화 TODO다.
예를 들어 `missing_required_mfe_mae`는 가격경로 30D/90D/180D가 부족해서 score 보정에 못 쓴다는 뜻이다.

| reason | rows | 쉬운 뜻 |
|---|---:|---|
| `missing_required_mfe_mae` | 4337 | 30/90/180일 MFE/MAE가 없어 성공/실패 경로 비교 불가 |
| `not_representative_for_aggregate` | 3100 | 중복 그룹의 대표 row가 아니거나 aggregate 제외 표시 |
| `not_usable_for_promotion` | 1598 | positive 승격 근거로 쓰기에는 비가격 증거/품질이 부족 |
| `missing_trigger_type` | 1244 | Stage2/4B/4C 등 trigger 종류 없음 |
| `price_only_no_evidence` | 585 | 가격 움직임만 있고 비가격 증거 부족 |
| `missing_entry_price` | 331 | 진입가 없음 |
| `missing_entry_date` | 321 | 진입일 없음 |
| `corporate_action_contaminated` | 141 | 액면분할/합병 등 corporate action 영향 가능성 |
| `insufficient_forward_window` | 43 | as_of 이후 충분한 forward window가 없음 |
| `invalid_price_source` | 13 | 허용된 Stock-Web 가격 출처가 아님 |
| `raw_all_basis` | 12 | raw all basis라 tradable raw 기준이 아님 |

## 반영된 safe patch 축

| axis | applied specs | 쉬운 뜻 |
|---|---:|---|
| `earlier_thesis_break_watch` | 40 | 논리 훼손 조짐을 더 일찍 watch로 표시 |
| `hard_4c_confirmation` | 1 | 비가격 thesis break가 확인되면 4C를 더 명확히 표시 |
| `local_4b_watch_guard` | 25 | 가격만 오른 4B는 full 4B보다 watch로 제한 |
| `stage2_required_bridge` | 46 | Stage2로 올리려면 가격 말고 수주/실적/계약/마진 같은 bridge를 요구 |

## 대섹터별 대표 row 수

| large_sector | rows | symbols | positives/counter | 4B/4C | URL pending/proxy |
|---|---:|---:|---:|---:|---:|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 1347 | 172 | 251/304 | 228/28 | 405/386 |
| L2_AI_SEMICONDUCTOR_ELECTRONICS | 1384 | 138 | 246/349 | 238/22 | 414/319 |
| L3_BATTERY_EV_GREEN_MOBILITY | 1527 | 157 | 239/418 | 295/163 | 526/517 |
| L4_MATERIALS_SPREAD_RESOURCE | 855 | 149 | 102/176 | 132/20 | 279/285 |
| L5_CONSUMER_BRAND_DISTRIBUTION | 889 | 79 | 110/133 | 127/27 | 295/269 |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 740 | 45 | 91/93 | 79/16 | 257/227 |
| L7_BIO_HEALTHCARE_MEDICAL | 781 | 112 | 94/133 | 78/58 | 311/282 |
| L8_PLATFORM_CONTENT_SW_SECURITY | 882 | 112 | 107/198 | 126/26 | 268/278 |
| L9_CONSTRUCTION_REALESTATE_HOUSING | 374 | 51 | 35/64 | 48/28 | 156/149 |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 3692 | 704 | 220/760 | 772/184 | 995/1011 |

## 아키타입별 대표 row 수

| archetype | rows | symbols | positives/counter | 4B/4C | Stage2 hit | bad entry |
|---|---:|---:|---:|---:|---:|---:|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 288 | 89 | 70/50 | 40/3 | 0.6587 | 0.2814 |
| C02_POWER_GRID_DATACENTER_CAPEX | 277 | 44 | 50/58 | 54/0 | 0.8683 | 0.3174 |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 267 | 30 | 47/65 | 41/5 | 0.7059 | 0.2222 |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 220 | 21 | 33/75 | 46/4 | 0.5306 | 0.4388 |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 295 | 88 | 51/56 | 47/16 | 0.4113 | 0.1631 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 229 | 58 | 32/56 | 30/8 | 0.6124 | 0.2868 |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 237 | 54 | 56/60 | 46/1 | 0.806 | 0.3657 |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 247 | 63 | 39/53 | 38/3 | 0.6781 | 0.3904 |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 305 | 77 | 59/101 | 58/4 | 0.6933 | 0.4533 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 366 | 102 | 60/79 | 66/6 | 0.6766 | 0.4255 |
| C11_BATTERY_ORDERBOOK_RERATING | 286 | 75 | 33/73 | 48/9 | 0.6471 | 0.3647 |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 262 | 69 | 45/92 | 45/22 | 0.4924 | 0.4848 |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 307 | 58 | 46/81 | 61/33 | 0.5238 | 0.4558 |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 264 | 56 | 51/80 | 96/87 | 0.4474 | 0.5 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 324 | 96 | 47/72 | 56/7 | 0.5915 | 0.2317 |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 234 | 64 | 24/51 | 45/2 | 0.5462 | 0.3866 |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 297 | 47 | 31/53 | 31/11 | 0.5843 | 0.2711 |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 308 | 58 | 42/47 | 40/7 | 0.5952 | 0.2679 |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 223 | 44 | 26/41 | 33/9 | 0.4206 | 0.2617 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 358 | 50 | 42/45 | 54/11 | 0.7841 | 0.2557 |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 413 | 38 | 44/43 | 40/6 | 0.5546 | 0.0873 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 327 | 20 | 47/50 | 39/10 | 0.5422 | 0.1506 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 269 | 38 | 27/24 | 21/19 | 0.5735 | 0.2353 |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 253 | 63 | 36/41 | 30/33 | 0.6378 | 0.2913 |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 259 | 52 | 31/68 | 27/6 | 0.6144 | 0.3922 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 334 | 37 | 35/65 | 30/5 | 0.5568 | 0.3027 |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 263 | 40 | 33/46 | 47/15 | 0.6154 | 0.3769 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 285 | 52 | 39/87 | 49/6 | 0.5662 | 0.3382 |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 411 | 59 | 66/93 | 45/14 | 0.5721 | 0.1703 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 377 | 51 | 36/66 | 48/31 | 0.3654 | 0.1538 |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 478 | 180 | 64/102 | 51/0 | 0.5779 | 0.3443 |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 378 | 67 | 25/50 | 59/15 | 0.6978 | 0.4011 |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 1023 | 430 | 72/172 | 203/93 | 0.5163 | 0.4187 |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 619 | 326 | 29/104 | 176/42 | 0.6106 | 0.3894 |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 715 | 394 | 15/202 | 227/26 | 0.5065 | 0.513 |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 473 | 299 | 12/127 | 56/3 | 0.3833 | 0.5784 |

## 다음 연구 우선순위

자동연구원은 이제 단순히 30/50/80 row를 채우는 단계가 아니다.
모든 C01~C32 canonical archetype이 80 row를 넘었으므로 다음 우선순위는 품질 보강이다.

| target | meaning | current shortage |
|---|---|---:|
| 30 rows per C01~C32 archetype | 최소 안정권 | 0 |
| 50 rows per C01~C32 archetype | 실전 보정권 | 0 |
| 80 rows per C01~C32 archetype | 탄탄한 권역 | 0 |

### Priority 0: URL/proxy 품질 보강

| priority | target | why |
|---:|---|---|
| 1 | `missing_required_mfe_mae=4337` | 가격경로 30/90/180D가 없으면 weight/support 보정에 못 쓴다 |
| 2 | `evidence_url_pending_count=3906` | 직접 URL이 없으면 promotion에서 `blocked_by_data_quality`가 늘어난다 |
| 3 | `source_proxy_only_count=3723` | broker/report/news proxy만으로는 Stage2/4B/4C 근거 강도가 낮다 |
| 4 | `missing_trigger_type=1244` | Stage2/4B/4C 전이 판단에 직접 못 쓴다 |
| 5 | `missing_entry_price=331`, `missing_entry_date=321` | 진입 기준이 없으면 as_of 재현과 MFE/MAE 계산이 불가능하다 |

### Priority 1: 균형 보강

| target | 현재 상태 | 다음 연구 방향 |
|---|---:|---|
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 220 rows | 정책 이벤트와 실제 계약/법적 리스크 전환을 분리 |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 223 rows | 재고 정상화와 채널 reorder 실패 반례 보강 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 229 rows | 고객 승인/CAPA 잠김과 실적 전환 bridge 품질 보강 |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 234 rows | 정책/공급 쇼크와 실제 ASP/마진 전환 분리 |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 237 rows | 장비 order conversion과 late-cycle 4B/4C 분리 |

### Priority 2: 과다 반복 점검

| target | 현재 상태 | 다음 연구 방향 |
|---|---:|---|
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 1023 rows | 새 row보다 중복 symbol/date/trigger family 정리 |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 715 rows | high-MAE 반복 케이스를 대표 row 중심으로 압축 |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 619 rows | 회계/신뢰성 이슈의 직접 공시/감사 출처 보강 |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 473 rows | false positive 원인 taxonomy 정리 |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 478 rows | 정책 이벤트가 cashflow로 전환되는 직접 증거 중심으로 압축 |

## 다음 실행 지침

- 누적 재계산은 반드시 `--include-archive`를 붙인다.
- 새 연구만 임시 진단할 때만 `--include-archive` 없이 돌린다.
- 같은 symbol/date/trigger family 조합을 반복하지 않는다.
- 파일명이 표준 v12 result 패턴이 아닌 MD는 ingest되지 않는다.
- 직접 URL이 없는 source proxy row가 많으므로, 다음 연구는 URL/proxy 품질도 같이 보강한다.
- Stage 3-Green 완화보다 Stage2 bridge, 4B watch guard, hard 4C 확인을 우선한다.

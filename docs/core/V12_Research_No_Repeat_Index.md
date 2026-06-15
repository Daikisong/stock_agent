# V12 Research No-Repeat Index

이 문서는 새 자동연구 세션을 시작할 때 먼저 읽는 중복 방지 장부다.
목적은 같은 대섹터/아키타입 안에서 같은 종목, 같은 날짜, 같은 trigger를 반복 연구하지 않게 하는 것이다.

쉬운 예시:

```text
이미 C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / 257720 / Stage3-Green / 2024-05-10 이 들어왔다.
다음 연구는 같은 조합을 다시 쓰지 말고, 새 종목, 새 날짜, 새 trigger family, 또는 4B/4C/반례를 찾아야 한다.
```

last_updated: `2026-06-15`

## 현재 결론

`docs/core/goal.md`의 표준 명령을 누적 기준으로 실행했다.
이번 실행은 `docs/round` root의 새 연구 MD와 `docs/round/achieve` 보관 연구 MD를 함께 읽기 위해 `--include-archive`를 사용했다.

이전 실수는 `docs/round/achieve`가 discovery 기본값에서 제외되는데도, 그 안에 과거 누적 연구자료가 들어가 있었다는 점이다.
따라서 단순 `run-v12-calibration --md-input-root docs/round`는 현재 root snapshot만 재계산하고, 누적 장부가 아니다.

누적 재계산 표준:

```bash
PYTHONPATH=src python -m e2r.calibration.cli run-v12-calibration \
  --md-input-root docs/round \
  --include-archive \
  --data-directory data/e2r/calibration/v12 \
  --report-directory reports/e2r_calibration/v12
```

쉬운 예시:

```text
docs/round/root에 새 연구 157개가 있고, docs/round/achieve에 과거 연구 2002개가 있으면
--include-archive 없이 돌리면 157개만 계산한다.
--include-archive로 돌리면 둘을 합쳐 누적 corpus로 계산한다.
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

## 이번 누적 배치 반영 메모

| item | result |
|---|---:|
| run command | `run-v12-calibration --md-input-root docs/round --include-archive` |
| discovered markdown docs | 2159 |
| v12 result MD | 2081 |
| prompt/spec excluded | 0 |
| non-result non-prompt docs | 78 |
| root MD under `docs/round` | 157 |
| archive MD under `docs/round/achieve` | 2002 |
| parser failures | 0 |
| metadata only docs | 0 |
| zero trigger result docs | 0 |
| raw trigger rows | 16802 |
| validated rows | 12410 |
| representative rows | 11200 |
| valid/representative rows missing required MFE/MAE | 0/0 |
| rejected rows | 7473 |
| raw aggregate metric rows | 882 |
| raw shadow weight rows | 3575 |
| stage transition rows | 9516 |
| promotion decisions | 131 |
| apply_next_patch decisions | 108 |
| blocked_by_data_quality decisions | 23 |
| blocked_by_logic_risk decisions | 0 |
| hold_for_more_evidence decisions | 0 |
| applied patch specs | 108 |
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
| representative row_count | 11200 |
| unique_case_count | 8154 |
| unique_symbol_count | 962 |
| unique_round_count | 13 |
| positive_case_count | 1326 |
| counterexample_count | 2385 |
| 4B_case_count | 1878 |
| 4C_case_count | 463 |
| good_stage2_count | 3017 |
| bad_stage2_count | 2183 |
| source_proxy_only_count | 3611 |
| evidence_url_pending_count | 3888 |
| current_profile_error_count | 5746 |
| current_profile_false_positive_count | 3245 |
| current_profile_too_late_count | 1605 |
| stage2 hit rate MFE90 >= 20% | 0.5885 |
| stage2 bad entry rate MAE90 <= -20% | 0.3342 |
| avg Stage2 MFE90 | 43.2743 |
| avg Stage2 MAE90 | -16.088 |
| canonical_archetypes_covered by representative rows | 36 |

## Goal 사용 범위 점검

| 구분 | row/docs | 현재 처리 | 판단 |
|---|---:|---|---|
| 표준 V12 result MD | 2081 docs | ingest 대상 | 사용됨 |
| prompt/spec excluded | 0 docs | 파일명/제목 기준 확인 | 없음 |
| non-result non-prompt docs | 78 docs | 표준 v12 result 파일명이 아님 | 사용 안 함 |
| root docs | 157 docs | 새 연구자료 | 사용됨 |
| archive docs | 2002 docs | `--include-archive`로 포함 | 사용됨 |
| raw trigger | 16802 rows | validation 수행 | 조건 통과분만 사용 |
| validated trigger | 12410 rows | dedupe 후보 | 사용됨 |
| representative trigger | 11200 rows | aggregate/weight/profile 입력 | 최종 사용 |
| valid/representative 중 필수 MFE/MAE 누락 | 0/0 rows | strict gate | 통과 |
| unknown canonical archetype | 0 | runtime seed 직접 매칭 | 통과 |
| unknown large sector | 0 | runtime seed 직접 매칭 | 통과 |

## 주요 rejected reason

Rejected row는 버리는 데이터가 아니라 다음 정규화 TODO다.
예를 들어 `missing_required_mfe_mae`는 가격경로 30D/90D/180D가 부족해서 score 보정에 못 쓴다는 뜻이다.

| reason | rows | 쉬운 뜻 |
|---|---:|---|
| `missing_required_mfe_mae` | 3755 | 30/90/180일 MFE/MAE가 모두 없어 성공/실패 경로 비교 불가 |
| `not_representative_for_aggregate` | 3053 | 중복 그룹의 대표 row가 아니거나 aggregate 제외 표시 |
| `not_usable_for_promotion` | 1596 | positive 승격 근거로 쓰기에는 비가격 증거/품질이 부족 |
| `missing_trigger_type` | 803 | Stage2/4B/4C 등 trigger 종류 없음 |
| `price_only_no_evidence` | 541 | 가격 움직임만 있고 비가격 증거 부족 |
| `missing_entry_price` | 323 | 진입가 없음 |
| `missing_entry_date` | 320 | 진입일 없음 |
| `corporate_action_contaminated` | 125 | 액면분할/합병 등 corporate action 영향 가능성 |
| `insufficient_forward_window` | 43 | as_of 이후 충분한 forward window가 없음 |
| `raw_all_basis` | 12 | raw all basis라 tradable raw 기준이 아님 |
| `invalid_price_source` | 5 | 허용된 Stock-Web 가격 출처가 아님 |

### missing_required_mfe_mae 세부 출처

| source_row_type | rows |
|---|---:|
| `trigger` | 2960 |
| `v12_compact_case` | 420 |
| `r13_review_trigger` | 108 |
| `review_case` | 102 |
| `r13_cross_case` | 101 |
| `v12_review_only_audit` | 31 |
| `cross_review_trigger` | 24 |
| `trigger_case` | 9 |

## 반영된 safe patch 축

| axis | applied specs | 쉬운 뜻 |
|---|---:|---|
| `earlier_thesis_break_watch` | 38 | 논리 훼손 조짐을 더 일찍 watch로 표시 |
| `hard_4c_confirmation` | 1 | 비가격 thesis break가 확인되면 4C를 더 명확히 표시 |
| `local_4b_watch_guard` | 23 | 가격만 오른 4B는 full 4B보다 watch로 제한 |
| `stage2_required_bridge` | 46 | Stage2로 올리려면 가격 말고 수주/실적/계약/마진 같은 bridge를 요구 |

## Promotion Decision 요약

| decision | count | 의미 |
|---|---:|---|
| `apply_next_patch` | 108 | 지금 profile에 작은 scope patch로 반영 |
| `blocked_by_data_quality` | 23 | URL/proxy/가격경로 등 품질 보강 필요 |

## 대섹터별 대표 row 수

| large_sector | rows | symbols | positives/counter | 4B/4C | URL pending/proxy |
|---|---:|---:|---:|---:|---:|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | 1104 | 160 | 205/268 | 180/18 | 405/370 |
| L2_AI_SEMICONDUCTOR_ELECTRONICS | 1175 | 128 | 209/298 | 189/11 | 408/298 |
| L3_BATTERY_EV_GREEN_MOBILITY | 1370 | 153 | 209/370 | 253/141 | 520/506 |
| L4_MATERIALS_SPREAD_RESOURCE | 715 | 117 | 87/159 | 97/13 | 279/270 |
| L5_CONSUMER_BRAND_DISTRIBUTION | 858 | 79 | 110/121 | 123/24 | 295/259 |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | 719 | 45 | 86/91 | 76/14 | 257/227 |
| L7_BIO_HEALTHCARE_MEDICAL | 746 | 112 | 91/122 | 73/50 | 305/281 |
| L8_PLATFORM_CONTENT_SW_SECURITY | 845 | 112 | 107/191 | 118/18 | 268/270 |
| L9_CONSTRUCTION_REALESTATE_HOUSING | 366 | 51 | 35/64 | 48/28 | 156/149 |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | 3302 | 671 | 187/701 | 721/146 | 995/981 |

## 아키타입별 row와 점수비중

weight 표기는 `EPS/Vis/Bott/Mis/Val/Cap/Info` 순서다.
diff는 기본형 `20/20/20/15/15/5/5` 대비 변화다.

| archetype | rows | symbols | positives/counter | 4B/4C | weights | diff | top symbols |
|---|---:|---:|---:|---:|---|---|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 188 | 60 | 46/31 | 23/2 | 20/25/18/12/12/8/5 | 0/+5/-2/-3/-3/+3/0 | 010620(12), 329180(12), 097230(10), 010140(9), 082740(9), 009540(8) |
| C02_POWER_GRID_DATACENTER_CAPEX | 263 | 44 | 50/58 | 50/0 | 21/24/20/13/12/5/5 | +1/+4/0/-2/-3/0/0 | 010120(30), 267260(29), 298040(21), 103590(17), 006340(13), 033100(13) |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 260 | 30 | 47/65 | 41/3 | 20/24/17/14/14/6/5 | 0/+4/-3/-1/-1/+1/0 | 064350(42), 012450(32), 079550(26), 272210(26), 047810(18), 003570(15) |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 213 | 21 | 33/75 | 43/3 | 15/22/10/15/18/10/10 | -5/+2/-10/0/+3/+5/+5 | 052690(28), 105840(25), 051600(23), 034020(20), 032820(19), 094820(19) |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 180 | 54 | 29/39 | 23/10 | 18/22/10/12/10/8/20 | -2/+2/-10/-3/-5/+3/+15 | 028050(20), 006360(19), 000720(18), 047040(17), 375500(14), 294870(5) |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 215 | 58 | 28/54 | 29/7 | 24/21/19/15/12/4/5 | +4/+1/-1/0/-3/-1/0 | 000660(56), 005930(41), 009150(7), 222800(7), 007660(6), 353200(6) |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 224 | 54 | 56/60 | 42/0 | 22/22/19/14/12/6/5 | +2/+2/-1/-1/-3/+1/0 | 042700(18), 232140(15), 089030(13), 031980(12), 084370(11), 003160(9) |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 235 | 63 | 39/51 | 35/2 | 22/21/16/14/12/6/9 | +2/+1/-4/-1/-3/+1/+4 | 098120(21), 058470(19), 095340(19), 131290(16), 080580(15), 425420(14) |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 291 | 77 | 59/101 | 56/2 | 22/20/18/13/11/6/10 | +2/0/-2/-2/-4/+1/+5 | 403870(14), 036930(12), 240810(12), 039030(9), 322310(9), 036810(8) |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 210 | 68 | 27/32 | 27/0 | 22/18/14/12/10/5/19 | +2/-2/-6/-3/-5/0/+14 | 240810(17), 084370(14), 095610(14), 036930(12), 319660(10), 166090(8) |
| C11_BATTERY_ORDERBOOK_RERATING | 280 | 75 | 30/70 | 47/8 | 20/20/15/12/10/8/15 | 0/0/-5/-3/-5/+3/+10 | 247540(18), 137400(16), 222080(16), 003670(14), 393890(13), 066970(12) |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 249 | 69 | 43/88 | 41/20 | 20/18/14/10/10/8/20 | 0/-2/-6/-5/-5/+3/+15 | 361610(18), 393890(15), 373220(12), 011790(11), 003670(10), 006400(9) |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 189 | 38 | 24/43 | 32/19 | 20/18/14/12/10/10/16 | 0/-2/-6/-3/-5/+5/+11 | 373220(26), 006400(21), 096770(12), 051910(11), 011790(8), 066970(8) |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 251 | 56 | 48/77 | 88/82 | 15/12/10/8/8/7/40 | -5/-8/-10/-7/-7/+2/+35 | 247540(26), 066970(20), 003670(17), 361610(17), 373220(16), 006400(11) |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 208 | 60 | 32/55 | 27/4 | 20/12/20/10/10/8/20 | 0/-8/0/-5/-5/+3/+15 | 005490(20), 004020(18), 103140(14), 018470(9), 010130(8), 025820(8) |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 217 | 63 | 24/51 | 41/0 | 18/18/18/12/12/7/15 | -2/-2/-2/-3/-3/+2/+10 | 005490(17), 000910(12), 010130(12), 001570(11), 001120(9), 006260(9) |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 290 | 47 | 31/53 | 29/9 | 20/12/18/10/10/5/25 | 0/-8/-2/-5/-5/0/+20 | 011780(35), 298020(28), 011170(25), 006650(21), 010950(18), 014830(13) |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 296 | 58 | 42/41 | 39/6 | 22/23/12/16/13/4/10 | +2/+3/-8/+1/-2/-1/+5 | 003230(32), 005180(24), 004370(22), 383220(17), 097950(16), 192820(14) |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 217 | 44 | 26/35 | 31/8 | 18/18/8/15/14/7/20 | -2/-2/-12/0/-1/+2/+15 | 383220(20), 020000(15), 081660(15), 036620(14), 111770(14), 298540(12) |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 345 | 50 | 42/45 | 53/10 | 22/23/12/16/13/4/10 | +2/+3/-8/+1/-2/-1/+5 | 257720(56), 090430(34), 003230(33), 192820(23), 018290(22), 051900(19) |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 399 | 38 | 44/43 | 38/5 | 15/20/5/15/25/15/5 | -5/0/-15/0/+10/+10/0 | 105560(67), 086790(39), 323410(39), 316140(21), 055550(20), 138930(18) |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 320 | 20 | 42/48 | 38/9 | 12/22/5/14/24/18/5 | -8/+2/-15/-1/+9/+13/0 | 005830(48), 000810(46), 088350(37), 001450(33), 032830(31), 003690(21) |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 263 | 38 | 24/21 | 21/18 | 12/24/5/12/10/7/30 | -8/+4/-15/-3/-5/+2/+25 | 000100(42), 028300(37), 145020(26), 196170(17), 068270(10), 069620(10) |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 239 | 63 | 36/41 | 28/28 | 5/15/5/10/5/5/55 | -15/-5/-15/-5/-10/0/+50 | 028300(20), 039200(16), 084990(15), 141080(15), 215600(15), 000100(14) |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 244 | 52 | 31/60 | 24/4 | 20/22/13/14/12/9/10 | 0/+2/-7/-1/-3/+4/+5 | 099190(24), 214150(22), 338220(19), 228670(17), 043150(16), 145720(16) |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 327 | 37 | 35/58 | 28/3 | 20/22/8/16/14/10/10 | 0/+2/-12/+1/-1/+5/+5 | 067160(43), 035420(34), 035720(33), 216050(21), 089600(20), 214270(18) |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 248 | 40 | 33/46 | 42/12 | 20/18/8/14/12/8/20 | 0/-2/-12/-1/-3/+3/+15 | 352820(22), 035900(20), 194480(18), 259960(18), 253450(16), 122870(13) |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 270 | 52 | 39/87 | 48/3 | 20/24/8/16/14/8/10 | 0/+4/-12/+1/-1/+3/+5 | 012510(27), 053800(24), 263860(21), 030520(15), 042510(12), 067920(11) |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 404 | 59 | 66/93 | 45/14 | 20/18/10/15/17/15/5 | 0/-2/-10/0/+2/+10/0 | 000270(32), 204320(29), 012330(27), 005380(26), 161390(26), 011210(20) |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 369 | 51 | 36/66 | 48/31 | 18/12/8/12/10/10/30 | -2/-8/-12/-3/-5/+5/+25 | 047040(42), 294870(27), 000720(23), 006360(23), 375500(20), 005960(17) |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 422 | 155 | 55/86 | 45/0 | 12/15/8/15/15/10/25 | -8/-5/-12/0/0/+5/+20 | 036460(12), 105560(12), 052690(9), 112610(9), 316140(9), 004090(8) |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 360 | 66 | 25/50 | 52/12 | 12/18/5/20/25/15/5 | -8/-2/-15/+5/+10/+10/0 | 010130(41), 041510(39), 008930(28), 011200(17), 040300(14), 028260(13) |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 967 | 419 | 67/162 | 189/78 | 8/12/8/10/8/4/50 | -12/-8/-12/-5/-7/-1/+45 | 028300(17), 247540(12), 105560(11), 257720(11), 294870(11), 006360(10) |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 556 | 310 | 20/93 | 163/30 | 8/12/5/10/8/20/37 | -12/-8/-15/-5/-7/+15/+32 | 035420(11), 003230(10), 294870(10), 028300(9), 005380(6), 005930(6) |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 580 | 354 | 12/193 | 218/18 | 10/14/8/12/10/6/40 | -10/-6/-12/-3/-5/+1/+35 | 028300(9), 066970(7), 003230(6), 041510(6), 010690(5), 051910(5) |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 411 | 274 | 5/114 | 54/3 | 10/14/8/12/10/6/40 | -10/-6/-12/-3/-5/+1/+35 | 003230(6), 011170(5), 028300(5), 196170(5), 005380(4), 006800(4) |

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
| 1 | `evidence_url_pending_count=3888` | 직접 URL이 없으면 promotion에서 `blocked_by_data_quality`가 늘어난다 |
| 2 | `source_proxy_only_count=3611` | broker/report/news proxy만으로는 Stage2/4B/4C 근거 강도가 낮다 |
| 3 | `missing_required_mfe_mae=3755` | 가격경로 30/90/180D가 없으면 weight/support 보정에 못 쓴다 |
| 4 | `missing_entry_price=323`, `missing_entry_date=320` | 진입 기준이 없으면 as_of 재현과 MFE/MAE 계산이 불가능하다 |

### Priority 1: 균형 보강

| target | 현재 상태 | 다음 연구 방향 |
|---|---:|---|
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 180 rows | margin/working-capital 실패 반례와 4C 전환 타이밍 보강 |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 188 rows | backlog가 실제 FCF로 전환되지 않는 반례 보강 |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 189 rows | AMPC/IRA 지속성, JV utilization 실패 사례 보강 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 208 rows | spread reversal, inventory cycle 반례 보강 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 210 rows | 회복 cycle 초입 false positive와 order conversion 확인 |

### Priority 2: 과다 반복 점검

| target | 현재 상태 | 다음 연구 방향 |
|---|---:|---|
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 967 rows | 새 row보다 중복 symbol/date/trigger family 정리 |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 580 rows | high-MAE 반복 케이스를 대표 row 중심으로 압축 |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 556 rows | 회계/신뢰성 이슈의 직접 공시/감사 출처 보강 |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 411 rows | false positive 원인 taxonomy 정리 |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 422 rows | 정책 이벤트가 cashflow로 전환되는 직접 증거 중심으로 압축 |

## 다음 실행 지침

- 누적 재계산은 반드시 `--include-archive`를 붙인다.
- 새 연구만 임시 진단할 때만 `--include-archive` 없이 돌린다.
- 같은 symbol/date/trigger family 조합을 반복하지 않는다.
- 파일명이 표준 v12 result 패턴이 아닌 MD는 ingest되지 않는다.
- 직접 URL이 없는 source proxy row가 많으므로, 다음 연구는 URL/proxy 품질도 같이 보강한다.
- Stage 3-Green 완화보다 Stage2 bridge, 4B watch guard, hard 4C 확인을 우선한다.

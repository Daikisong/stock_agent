# Research Green Runtime Coverage Gap - 2026-06-19

## 결론

연구가 부족해서 삼전/하닉이 낮게 나온 것이 아니다.

누적 연구에는 `Stage3-Green` row가 381개 있고, C06 HBM뿐 아니라 C21 금융, C22 보험, C23 바이오, C28 SW/security에도 Green 사례가 있다.

하지만 현재 production runtime에는 세 가지 단절이 있다.

1. 누적 연구 Green은 weight와 guardrail에는 반영됐지만 positive score unlock으로 거의 적용되지 않았다.
2. 현재 benchmark 120개는 C21/C22/C23/C28 같은 Green 연구가 많은 아키타입을 거의 실행하지 않는다.
3. 실행된 runtime 후보들은 대부분 Green gate에서 `bottleneck`, `visibility`, `contract/domain evidence`가 비어 있다.

쉬운 예:

```text
연구 장부:
"보험 CSM/K-ICS + reserve quality면 Green 가능"

실제 runtime:
그 보험 케이스가 benchmark 후보로 안 들어옴
또는 들어와도 CSM/K-ICS가 source-backed field로 안 들어오면 점수판에는 0점
```

## 사용한 원천

| source | 의미 |
| --- | --- |
| `data/e2r/calibration/v12/v12_trigger_rows_representative.jsonl` | 누적 연구 대표 row 12,471개 |
| `data/e2r/calibration/v12/v12_promotion_decisions.jsonl` | 연구를 실제 patch로 승격할지 결정한 장부 |
| `reports/e2r_calibration/v12/apply_next_patch_plan.md` | 실제 적용된 112개 patch 목록 |
| `output/0619_asof_stage_promotion_benchmark_current_2023_2026/score_components_by_candidate.csv` | 현재 benchmark runtime 120개 점수 |
| `output/0619_asof_stage_promotion_benchmark_current_2023_2026/stage_gate_matrix.csv` | 현재 benchmark runtime gate 실패 |

## 누적 연구 Green은 있었다

대표 row 전체:

| metric | count |
| --- | ---: |
| representative rows | 12,471 |
| Stage2-Actionable | 4,704 |
| Stage3-Green | 381 |
| Stage3-Yellow | 886 |
| Stage4B | 2,472 |
| Stage4C | 699 |

Green row가 많은 주요 아키타입:

| archetype | research rows | Green rows | weight usable | source proxy / url pending | runtime rows | runtime stage mix | avg runtime score | runtime bridge state |
| --- | ---: | ---: | ---: | ---: | ---: | --- | ---: | --- |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 413 | 37 | 241 | 100 / 123 | 0 | - | - | benchmark 미실행 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 358 | 33 | 184 | 76 / 91 | 22 | Stage1:22 | 57.10 | backlog 0%, contract 0%, customer 0%, domain>=60 50% |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 269 | 30 | 170 | 74 / 87 | 0 | - | - | benchmark 미실행 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 327 | 28 | 173 | 127 / 134 | 0 | - | - | benchmark 미실행 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 334 | 19 | 179 | 89 / 106 | 0 | - | - | benchmark 미실행 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 285 | 14 | 142 | 105 / 84 | 0 | - | - | benchmark 미실행 |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 308 | 14 | 181 | 101 / 105 | 0 | - | - | benchmark 미실행 |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 259 | 12 | 165 | 91 / 94 | 0 | - | - | benchmark 미실행 |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 247 | 10 | 163 | 47 / 118 | 0 | - | - | benchmark 미실행 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 229 | 9 | 145 | 63 / 78 | 19 | Yellow:12, Stage1:7 | 75.23 | backlog 0%, contract 0%, customer 100%, domain>=60 100% |
| C02_POWER_GRID_DATACENTER_CAPEX | 277 | 5 | 158 | 66 / 50 | 44 | Stage2:33, Stage1:11 | 66.10 | backlog 75%, contract 50%, customer 50%, domain>=60 0% |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 366 | 4 | 240 | 63 / 69 | 1 | Stage2:1 | 68.68 | backlog 0%, contract 0%, customer 0%, domain>=60 100% |

이 표의 뜻:

- 하닉 C06은 benchmark에 들어오지만 `backlog/contract` bridge가 0이라 Green이 막힌다.
- 삼성 C10은 memory recovery로 들어오지만 `customer/backlog/contract`가 0이라 HBM Green이 아니다.
- C21/C22/C23/C28은 연구 Green row가 있는데 benchmark 120개에는 거의 안 들어온다.

즉 삼전/하닉만의 문제가 아니다. 더 큰 문제는 "연구 Green을 runtime 후보와 field로 재현하는 경로"다.

## 실제 적용 patch는 대부분 방어형이었다

`v12_promotion_decisions.jsonl` 기준:

| decision | count |
| --- | ---: |
| apply_next_patch | 112 |
| blocked_by_data_quality | 21 |

적용된 axis:

| axis | count | 성격 |
| --- | ---: | --- |
| stage2_required_bridge | 46 | price-only/약한 Stage2 방지 |
| earlier_thesis_break_watch | 40 | 4C를 더 일찍 watch하되 hard 4C는 조심 |
| local_4b_watch_guard | 25 | price-only 4B를 full 4B로 과승격하지 않음 |
| hard_4c_confirmation | 1 | non-price thesis break 확인 |

핵심:

```text
연구가 누적됨
-> yes, 12,471 대표 row

weight가 바뀜
-> yes, 36개 canonical archetype weight 적용

좋은 증거를 Green 점수로 올리는 positive unlock이 적용됨
-> 거의 no

적용된 patch 성격
-> 대부분 guardrail only
```

쉬운 예:

```text
운전 데이터를 보고 배운 것:
"과속하면 위험하다"는 브레이크 규칙은 많이 들어감

아직 덜 들어간 것:
"좋은 도로 + 시야 확보 + 연료 충분이면 정상 속도를 내도 된다"는 엑셀 규칙
```

그래서 좋은 연구 사례가 쌓였는데도 runtime 점수는 보수적으로 남는다.

## 현재 runtime Green gate 실패

benchmark 120개 기준:

| failed gate | count |
| --- | ---: |
| failed_stage3_total_score | 120 |
| failed_stage3_bottleneck | 120 |
| failed_stage3_visibility | 87 |
| failed_stage3_valuation | 67 |
| failed_stage2_information_confidence | 63 |
| failed_stage3_market_mispricing | 56 |
| failed_sector_bottleneck | 56 |
| failed_stage2_eps_fcf | 45 |
| failed_green_cross_evidence | 40 |
| failed_stage3_contract_quality | 37 |
| failed_structural_visibility_quality | 33 |
| failed_domain_specific_evidence | 33 |
| failed_stage3_revision | 22 |

이건 단순히 "점수 기준이 높다"가 아니다.

모든 후보가 `failed_stage3_bottleneck`에 걸린다. 즉 구조적 병목, 고객 lock, backlog, 계약, CAPA, ASP 같은 Green 핵심축이 runtime component까지 충분히 올라오지 않는다.

## 삼전/하닉을 다시 보면

### 하닉

하닉은 연구 장부 기준으로 Green이어야 한다는 주장이 맞다.

누적 연구 C06에는 SK하이닉스 Green row가 있다.

- 2024-03-19: HBM3E 양산, Nvidia shipment, 2024 HBM capacity booked
- 2024-04-25: Q1 surprise, HBM sold/booked-out capacity, revision visibility
- 2024-05-02: 2024 sold out, 2025 almost booked

그런데 current runtime 하닉은:

| item | value |
| --- | ---: |
| stage | Stage3-Yellow |
| score | 76.7639 |
| weighted bottleneck | 11.0522 / 14.2500 |
| bottleneck raw | 58.1697 / 75.0000 |
| backlog bridge | 0 |
| contract bridge | 0 |

즉 outlook, EPS/FCF, revision은 무시된 게 아니다. 깎인 위치는 `HBM 구조적 병목을 증명하는 backlog/contract/CAPA lock bridge`다.

### 삼성

삼성은 두 문제가 섞여 있다.

1. 일부 as-of에서는 cheap scan 후보 단계에서 약하게 잡힌다.
2. 잡히더라도 HBM C06이 아니라 C10 memory recovery로 남는다.

현재 삼성 2024-04-01:

| item | value |
| --- | ---: |
| stage | Stage2 |
| score | 68.6752 |
| archetype | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE |
| customer/backlog/contract bridge | 0 |

이건 삼성에 불리하게 이름으로 막은 것이 아니다. HBM customer qualification, capacity lock, 장기계약/수주잔고가 source-backed로 들어오지 않으면 C06 Green으로 올리면 안 된다.

다만 삼성처럼 이미 흑자인 mega-cap이 "전망 급증"을 보일 때 cheap scan이 충분히 후보로 올리는지는 별도 문제다. 이건 HBM 문제가 아니라 candidate funnel 문제다.

## 이번 패치 후에도 남는 미검증 구멍

이번에 `FINANCIAL_CAPITAL_RETURN`, `INSURANCE_RESERVE`, `BIO_COMMERCIALIZATION`, `SOFTWARE_SECURITY` profile을 추가해서 C21/C22/C23/C28이 `GENERIC`에 갇히는 문제는 줄였다.

하지만 이걸로 끝이 아니다.

남은 구멍:

1. C21/C22/C23/C28 Green 연구 row를 실제 as-of runtime replay로 돌리는 fixture가 없다.
2. benchmark 120개가 전체 36개 archetype Green recall을 대표하지 않는다.
3. patch planner가 positive unlock보다 guardrail 승격에 치우쳐 있다.
4. source proxy/url pending row가 많아서 positive patch가 data quality 단계에서 멈춘다.
5. parser가 뽑은 primitive가 component/gate로 충분히 들어가는지 아키타입별 truth table이 아직 부족하다.

## 다음에 필요한 구현

1. 연구 Green row에서 runtime replay fixture를 자동 생성한다.
   - C06 하닉
   - C21 금융 capital return
   - C22 보험 CSM/K-ICS
   - C23 바이오 approval-to-revenue
   - C28 SW/security ARR/retention

2. 각 positive fixture마다 guard pair를 같이 둔다.
   - 하닉 positive vs 삼성 catch-up/qualification guard
   - 금융 capital return execution vs value-up beta only
   - 보험 reserve quality vs rate-cycle beta only
   - 바이오 approval-to-revenue vs PDUFA/binary event only
   - SW ARR/retention vs security theme only

3. patch planner에 positive unlock 후보를 별도 축으로 만든다.
   - 지금은 `stage2_required_bridge`, `local_4b_watch_guard`처럼 방어형이 많다.
   - `green_positive_bridge_unlock_candidate` 같은 축이 필요하다.

4. candidate funnel을 별도로 고친다.
   - 삼성처럼 이미 흑자인 mega-cap의 전망 급증은 `turnaround`가 아니어도 후보로 들어와야 한다.
   - 단, price-only나 HBM catch-up headline만으로 Green은 안 된다.

## 현재 완료/미완료 판정

완료된 것:

- 누적 연구가 실제로 쌓였다는 증거 확인.
- 적용 patch가 guardrail 중심이라는 증거 확인.
- 하닉이 어디서 깎이는지 field/gate 단위로 확인.
- 삼성은 후보 funnel과 C10/C06 route 문제가 섞여 있다는 점 확인.
- 비-HBM 아키타입 일부의 `GENERIC` profile 압축 문제를 완화.

미완료:

- 전체 36개 archetype에 대해 Green 연구 row를 runtime replay로 재현하지 못했다.
- positive unlock patch planner는 아직 없다.
- benchmark 120개는 전체 연구 Green coverage를 대표하지 않는다.
- 운영 replay에서 Stage3-Green 0개 문제는 아직 남아 있다.

따라서 현재 결론은 "원인을 찾는 작업은 많이 진행됐지만 완료는 아니다."다.

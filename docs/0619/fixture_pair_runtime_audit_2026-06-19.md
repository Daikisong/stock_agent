# Fixture Pair Runtime Audit - 2026-06-19

## 결론

삼전/하닉 사례는 HBM 전용으로 과적합하라는 뜻이 아니다.

이번 점검의 목적은 더 일반적이다.

```text
좋은 연구 증거가 있다
-> parser가 source-backed field로 뽑는다
-> feature adapter가 component 점수로 바꾼다
-> archetype weight와 gate가 판단한다
```

이 연결이 모든 아키타입에서 되는지 확인했다.

쉬운 예:

- 하닉: "고객 물량 배정 + CAPA 잠김 + 실적 전환"이 있으면 Green 후보가 되어야 한다.
- 삼성: "HBM 기대감은 있지만 qualification/대량공급 확인이 부족"하면 같이 Green이 되면 안 된다.
- 바이오도 같다. "FDA 승인 후 매출/로열티 경로"는 positive지만, "PDUFA 전 기대감"은 guard다.
- 금융도 같다. "저PBR + ROE + 자사주 소각 실행"은 positive지만, "밸류업 기대감"만으로는 guard다.

## 이번에 확인한 runtime 상태

수정 후 synthetic positive/guard 쌍을 같은 rule engine으로 돌렸다.

| archetype | case | sector profile | runtime archetype | stage | score | 핵심 해석 |
| --- | --- | --- | --- | --- | ---: | --- |
| C06 HBM | positive | MEMORY_HBM | C06 | Stage 3-Green | 90.4997 | strong capacity/customer/backlog/contract 증거가 있으면 Green 가능 |
| C06 HBM | guard | MEMORY_HBM | C06 | Stage 3-Yellow | 79.8662 | 기대감만으로 Green까지는 못 감 |
| C21 financial | positive | FINANCIAL_CAPITAL_RETURN | C21 | Stage 2 | 71.7379 | finance profile과 capital-return primitive는 먹지만 Green unlock은 아직 부족 |
| C21 financial | guard | FINANCIAL_CAPITAL_RETURN | C21 | Stage 0 | 58.4927 | value-up 기대감 guard penalty는 작동 |
| C22 insurance | positive | INSURANCE_RESERVE | C22 | Stage 2 | 70.7124 | CSM/K-ICS/reserve profile은 먹지만 Green gate까지는 부족 |
| C22 insurance | guard | INSURANCE_RESERVE | C22 | Stage 0 | 50.0021 | rate-cycle beta guard penalty는 작동 |
| C23 bio | positive | BIO_COMMERCIALIZATION | C23 | Stage 3-Yellow | 76.5544 | approval-to-revenue/royalty bridge는 Yellow까지 먹지만 Green에는 부족 |
| C23 bio | guard | BIO_COMMERCIALIZATION | C23 | Stage 0 | 61.2748 | binary-event guard penalty는 작동 |
| C28 software/security | positive | SOFTWARE_SECURITY | C28 | Stage 2 | 70.5909 | ARR/retention profile은 먹지만 recurring revenue Green unlock은 부족 |
| C28 software/security | guard | SOFTWARE_SECURITY | C28 | Stage 0 | 54.4161 | political-theme guard penalty는 작동 |

핵심은 두 가지다.

1. HBM positive만 살리는 패치가 아니다.
2. 비-HBM 아키타입은 이제 `GENERIC`에 덜 갇히지만, positive unlock은 아직 충분하지 않다.

## C06에서 새로 잡은 버그

강한 HBM positive fixture를 넣었을 때, `capa_utilization_pct`와 `order_backlog_to_sales`가 같이 있으면 sector profile이 먼저 `POWER_EQUIPMENT`로 빠질 수 있었다.

이건 좋은 증거를 잘못된 업종 계산기로 보내는 문제다.

쉬운 예:

```text
하닉 리포트에 "CAPA 100%, backlog"가 있다
-> 전력기기 수주잔고처럼 해석됨
-> HBM 고객/CAPA 아키타입 점수가 아니라 전력기기 점수로 계산됨
```

수정 후에는 memory/HBM context가 먼저 이기고, 그 다음에야 power-equipment fallback이 적용된다.

## Guard risk도 점수에 연결했다

기존에는 일부 guard 신호를 진단으로 볼 수 있어도 점수를 충분히 누르지 못했다.

이번에 `research_axis_bridge_guard_risk_penalty_points`를 추가했다.

| guard signal | 의미 |
| --- | --- |
| `binary_event_unresolved`, `approval_not_confirmed` | 바이오 승인 전 이벤트 기대감 |
| `political_theme_risk`, `policy_headline_only` | 정책/정치 테마만 있는 경우 |
| `capital_return_unconfirmed` | 자사주 소각/배당 실행 없이 밸류업 기대만 있는 경우 |
| `reserve_quality_unconfirmed`, `insurance_rate_cycle_beta_only` | 보험료율 사이클 기대만 있고 CSM/reserve 품질이 없는 경우 |
| `inventory_overhang` | 소비재 sell-through가 아니라 재고 부담이 있는 경우 |

쉬운 예:

- 좋은 금융 positive: "ROE 높고 PBR 낮고 자사주 소각을 실행했다."
- 막아야 할 금융 guard: "밸류업 기대감으로 올랐다."

둘 다 `금융`처럼 보이지만, 두 번째는 실제 현금 환원 bridge가 없으므로 penalty가 들어가야 한다.

## Benchmark replay에는 왜 아직 Green이 0개인가

이번 수정 후에도 benchmark stage 분포는 그대로다.

| Stage | count |
| --- | ---: |
| Stage 0 | 7 |
| Stage 1 | 67 |
| Stage 2 | 34 |
| Stage 3-Yellow | 12 |
| Stage 3-Green | 0 |

이건 의도한 결과다.

Green 문턱을 낮추지 않았고, 실제 replay 자료에서 하닉은 여전히 `backlog=0`, `contract=0`으로 남는다.

즉:

```text
parser primitive와 diagnostics는 늘었다
하지만 실제 replay source에서 핵심 bridge field가 아직 충분히 안 들어온다
```

하닉 2024-05-01은 최신 autopsy 기준으로:

| item | value |
| --- | ---: |
| stage | Stage 3-Yellow |
| total | 76.7639 |
| weighted bottleneck | 11.0522 / 14.2500 |
| bottleneck deficit | 3.1978 |
| bridge margin/customer/valuation | 100 |
| bridge backlog/contract | 0 |

삼성 2024-04-01은:

| item | value |
| --- | ---: |
| stage | Stage 2 |
| total | 68.6752 |
| weighted bottleneck | 6.9400 / 10.5000 |
| visibility deficit | 2.3037 |
| bridge margin/valuation | 100 |
| bridge customer/backlog/contract | 0 |

## 다음 구현 의미

이제 방향은 명확하다.

나쁜 방향:

```text
if HBM:
  score += 5
```

맞는 방향:

```text
if source-backed positive bridge exists:
  relevant primitive = true
  archetype adapter converts primitive into component score
  guard primitive blocks shallow/theme/binary cases
```

다음 구현은 C06 하나가 아니라 fixture pair matrix 기준으로 가야 한다.

| group | 살려야 할 것 | 막아야 할 것 |
| --- | --- | --- |
| C06 HBM | customer allocation + capacity lock + backlog/contract + FCF/revision | HBM catch-up 기대감, qualification failure |
| C21 금융 | ROE/PBR + 자사주 소각/배당 실행 + 신용비용 안정 | value-up beta only |
| C22 보험 | CSM + K-ICS + reserve/loss ratio quality | rate-cycle beta only |
| C23 바이오 | approval-to-revenue + royalty/reimbursement | pre-PDUFA binary event |
| C28 SW/security | ARR/NRR + renewal/retention + recurring margin | political/security theme only |

## 완료 기준 업데이트

아직 구현 완료가 아니다.

현재 완료된 것:

- parser가 cross-archetype primitive를 더 많이 추출한다.
- autopsy가 bridge presence와 guard risk를 보여준다.
- C06 strong positive와 C06 guard를 구분할 수 있는 방향은 확인했다.
- guard risk penalty가 C21/C22/C23/C28 shallow case를 누르기 시작했다.

아직 남은 것:

- C21/C22/C23/C28 전용 feature adapter가 부족하다.
- 실제 replay source에서 positive bridge가 source-backed field로 더 안정적으로 들어와야 한다.
- fixture pair를 정식 regression fixture로 고정해야 한다.
- 운영 replay에서 Green 0개가 사라지는지, 동시에 false-positive guard가 무너지지 않는지 봐야 한다.

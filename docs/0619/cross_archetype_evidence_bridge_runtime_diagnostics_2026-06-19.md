# Cross-Archetype Evidence Bridge Runtime Diagnostics - 2026-06-19

## 결론

이번 패치는 HBM 점수 가산이 아니다.

연구자료에서 반복적으로 나온 축이 runtime primitive로 실제 들어왔는지 확인하는 진단층을 추가했다.

흐름은 이렇다.

```text
research phrase
-> parser primitive
-> research_axis_bridge_* diagnostic
-> existing component formula
-> weighted stage gate
```

쉬운 예:

- 연구 문장: "하닉 HBM은 고객 물량이 잠겼고 실적 전망이 올라간다."
- 새 진단: `margin=100`, `customer=100`, `valuation_repricing=100`
- 아직 0인 진단: `backlog=0`, `contract=0`
- 의미: 좋은 전망과 고객 신호는 들어왔지만, Green 병목을 여는 backlog/CAPA-lock/계약 품질 primitive가 부족하다.

## 새 진단 컬럼

`score_components_by_candidate.csv`에 다음 컬럼을 추가했다.

| column | 의미 |
| --- | --- |
| `research_axis_bridge_present_count_capped` | 들어온 bridge 그룹 수 |
| `research_axis_bridge_margin` | OPM, FCF, mix, actual profit conversion |
| `research_axis_bridge_customer` | customer allocation, government/hyperscaler/customer quality |
| `research_axis_bridge_backlog` | backlog/RPO/ARR/capacity precommit |
| `research_axis_bridge_contract` | multi-year, prepayment, non-cancellable, revenue visibility |
| `research_axis_bridge_valuation_repricing` | ROE/PBR, target multiple, market frame shift |
| `research_axis_bridge_capital_return` | buyback execution, cancellation, dividend/shareholder return execution |
| `research_axis_bridge_insurance_quality` | CSM, K-ICS, reserve/loss-ratio quality |
| `research_axis_bridge_bio_commercialization` | approval plus revenue/royalty/reimbursement route |
| `research_axis_bridge_software_retention` | ARR, NRR, renewal, retention, recurring margin |
| `research_axis_bridge_consumer_sell_through` | sell-through, reorder, repeat order |
| `research_axis_bridge_guard_risk` | binary event, policy headline-only, inventory overhang, unconfirmed capital/reserve |

주의:

- ROE/PBR은 자본환원이 아니다.
- 그래서 `valuation_repricing`과 `capital_return`을 분리했다.
- 자본환원은 소각, 배당, 주주환원 실행이 있어야 켜진다.

## Benchmark 재생성 결과

명령:

```bash
PYTHONPATH=src python -m e2r.cli.analyze_asof_stage_promotion \
  --asof-output output/0619_asof_replay_benchmark_current_2023_2026/2023-01-01_to_2026-05-14 \
  --output-directory output/0619_asof_stage_promotion_benchmark_current_2023_2026 \
  --top-candidates 120 \
  --max-queries-per-candidate 8 \
  --max-results-per-query 10 \
  --report-date 2026-06-19
```

Stage 분포는 바뀌지 않았다.

| Stage | count |
| --- | ---: |
| Stage 0 | 7 |
| Stage 1 | 67 |
| Stage 2 | 34 |
| Stage 3-Yellow | 12 |
| Stage 3-Green | 0 |

즉 이번 패치는 Green 문턱을 낮춘 패치가 아니다.

## 하닉/삼전에서 새로 보이는 것

### SK하이닉스 2024-05-01

| item | value |
| --- | ---: |
| stage | Stage 3-Yellow |
| canonical archetype | C06_HBM_MEMORY_CUSTOMER_CAPACITY |
| total | 76.7639 |
| weighted bottleneck | 11.0522 / 14.2500 |
| total deficit | 10.2361 |
| bottleneck deficit | 3.1978 |

Bridge 진단:

| bridge | value |
| --- | ---: |
| margin | 100 |
| customer | 100 |
| valuation_repricing | 100 |
| backlog | 0 |
| contract | 0 |
| capital_return | 0 |
| guard_risk | 0 |

해석:

- 하닉은 HBM 전망, 고객 신호, valuation/revision 신호는 들어온다.
- 하지만 backlog/RPO/capacity-precommit/contract field가 충분히 source-backed로 안 들어온다.
- 그래서 C06 weight가 적용돼도 bottleneck gate가 `11.05/14.25`에서 멈춘다.

### 삼성전자 2024-04-01

| item | value |
| --- | ---: |
| stage | Stage 2 |
| canonical archetype | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE |
| total | 68.6752 |
| weighted bottleneck | 6.9400 / 10.5000 |
| total deficit | 18.3248 |
| bottleneck deficit | 3.5600 |
| visibility deficit | 2.3037 |

Bridge 진단:

| bridge | value |
| --- | ---: |
| margin | 100 |
| valuation_repricing | 100 |
| customer | 0 |
| backlog | 0 |
| contract | 0 |
| capital_return | 0 |
| guard_risk | 0 |

해석:

- 삼성은 memory recovery와 margin/valuation 신호는 있다.
- 하지만 C06 Green에 필요한 customer allocation, capacity lock, backlog/contract bridge가 없다.
- 그래서 삼성은 C06으로 강제하기보다 C10 recovery로 남는 것이 맞다.

## 전 아키타입 관찰

120개 benchmark에서 sector별 bridge rate는 다음과 같다.

| sector profile | n | bridge pattern |
| --- | ---: | --- |
| DEFENSE | 12 | margin/customer/backlog/contract/valuation 모두 1.00 |
| POWER_EQUIPMENT | 48 | backlog 0.69, contract 0.46, margin/customer 0.46 |
| MEMORY_HBM | 20 | margin 1.00, customer 0.95, backlog/contract 0 |
| K_BEAUTY_EXPORT | 11 | margin 1.00, consumer sell-through 1.00 |
| GENERIC | 29 | valuation only 0.38, other bridge mostly 0 |

이 숫자가 보여주는 문제:

- HBM만 문제가 아니다.
- `GENERIC`과 아직 전용 profile이 약한 C21/C22/C23/C28 계열은 bridge가 0으로 남기 쉽다.
- POWER/HBM도 연구축 일부는 들어오지만 Green gate 핵심인 backlog/contract/CAPA-lock이 부족하다.

## 왜 이게 과적합 방지인가

나쁜 패치:

```text
if HBM:
  bottleneck += 5
```

이번 패치:

```text
if source says sold-out/capacity/customer/contract:
  normalized fields are visible
  bridge diagnostics show which fields exist
  existing formula still decides the score
```

다른 아키타입에도 같은 방식으로 적용된다.

예:

- C22 보험: `CSM`, `K-ICS`, `reserve`, `loss ratio`가 있어야 `insurance_quality`가 켜진다.
- C23 바이오: `FDA 승인`만으로 부족하고 `상업화`, `로열티`, `급여/매출 경로`가 있어야 `bio_commercialization`이 켜진다.
- C28 SW/security: `ARR`, `NRR`, `renewal`, `retention`이 있어야 `software_retention`이 켜진다.

## 남은 구현

이번 패치는 설명 가능성을 높인 첫 단계다.

아직 완료가 아닌 이유:

1. `research_axis_bridge_*`가 켜져도 모든 아키타입별 feature adapter가 있는 것은 아니다.
2. C21/C22/C23/C28 positive/guard fixture 쌍을 아직 runtime replay fixture로 고정하지 않았다.
3. HBM capacity lock을 `backlog/contract/capa_constraint`로 얼마나 줄지에 대한 positive/guard 검증이 아직 필요하다.
4. Green 0개 문제는 유지된다. threshold를 낮추지 않았기 때문이다.

다음 단계는 fixture 쌍이다.

```text
C06: 하닉 capacity/customer positive vs 삼성 catch-up/qualification guard
C21: ROE/PBR+capital return execution vs value-up beta only
C22: CSM/K-ICS/reserve quality vs rate-cycle beta only
C23: approval-to-revenue vs pre-PDUFA expectation
C28: ARR/retention vs political/theme security rally
```

이 쌍을 통과해야 실제 score unlock을 늘릴 수 있다.

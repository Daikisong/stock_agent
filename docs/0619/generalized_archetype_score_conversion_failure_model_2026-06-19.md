# Generalized Archetype Score Conversion Failure Model - 2026-06-19

## 결론

삼전/하닉은 HBM 전용 보정을 만들기 위한 사례가 아니다.

이번 사례의 의미는 더 일반적이다.

연구자료는 아키타입별로 "무엇을 보면 Green인지"를 많이 쌓았지만, 운영 runtime은 그 연구축을 source-backed normalized field로 충분히 번역하지 못한다. 그래서 HBM뿐 아니라 금융, 보험, 바이오, 플랫폼, 정책, 지배구조, 건설/PF에서도 같은 종류의 점수 손실이 생길 수 있다.

쉬운 예:

- 연구 판단: "하닉은 고객 lock, sold-out CAPA, revision, FCF 방향이 같이 있어서 Green 가능."
- 잘못된 해결: "HBM이면 bottleneck을 더 준다."
- 맞는 해결: "`고객 lock`, `CAPA lock`, `revision`, `FCF bridge`라는 공통 증거를 source-backed field로 번역하고, C06뿐 아니라 C21/C22/C23/C28 같은 다른 아키타입에도 각자 맞는 field bridge를 만든다."

즉 고쳐야 할 곳은 Green threshold나 HBM 점수 가산이 아니라, 연구축을 런타임 점수 재료로 바꾸는 변환층이다.

## 왜 전체 문제인가

현재 확인한 숫자는 다음과 같다.

| 항목 | 값 | 의미 |
| --- | ---: | --- |
| representative trigger rows | 12,471 | 누적 연구 장부 규모 |
| runtime archetype weight profiles | 36 | 아키타입별 weight는 존재 |
| runtime sector profiles | 13 | C21/C22/C23/C28용 profile을 추가했지만 36개 archetype보다 아직 적음 |
| raw Stage3-Green trigger rows | 381 | 원본 trigger label 기준 Green |
| fixture-usable Green rows | 320 | `false_green`/`false_positive`/`policy_only` marker를 제외한 positive fixture 후보 |
| clean fixture Green rows | 259 | source/proxy 문제가 없어 runtime replay fixture로 쓰기 쉬운 Green 후보 |
| parsed score simulation rows | 9,903 | 연구 문서에서 읽은 점수 시뮬레이션 row |
| Green-like score rows | 1,175 | Green 또는 Green 후보 성격의 score row |
| unique research score axes | 1,855 | 연구가 사용한 세부 점수축 |
| direct runtime/profile axis overlap | 10 | 런타임이 직접 아는 축은 매우 적음 |
| raw shadow weight rows | 3,741 | 연구가 제안한 shadow axis/guardrail |
| production changed shadow rows | 0 | shadow row 자체는 운영 점수 변경이 아님 |

이 숫자의 의미:

- 연구가 부족한 것이 아니다.
- weight 파일에 아키타입별 비중이 없는 것도 아니다.
- 문제는 연구에서 쌓인 세부축이 runtime parser/feature/gate field로 충분히 승격되지 않은 것이다.

쉬운 예:

- C22 보험 연구는 `CSM`, `K-ICS`, `reserve quality`, `capital return`을 본다.
- 이제 보험 profile은 추가됐지만, 실제 문서에서 이 단어들이 source-backed primitive로 뽑혀야 점수에 들어간다.
- 결과적으로 profile 추가만으로는 부족하고, 좋은 보험 Green과 약한 보험 이벤트를 positive/guard fixture로 같이 검증해야 한다.

## 하닉/삼전 사례에서 보인 일반 패턴

### 하닉: 후보는 들어왔지만 연구축이 점수로 약하게 번역됨

SK하이닉스 2024-04-30 replay:

| 항목 | 값 |
| --- | ---: |
| runtime stage | Stage3-Yellow |
| weighted total | 76.7639 |
| Green total threshold | 87.0000 |
| failed gates | total, bottleneck |
| revision_score | 100.0 |
| domain_specific_evidence_score | 80.0 |
| contract_quality | 0.0 |
| backlog_rpo_visibility | 15.0 |
| capa_constraint | 0.0 |
| fcf_quality_score | 0.0 |

연구는 `HBM sold-out capacity`, `Nvidia/customer allocation`, `revision visibility`를 봤다. runtime도 HBM 관련성은 일부 잡았다. 하지만 Green gate에서 필요한 `capa_constraint`, `backlog_rpo_visibility`, `contract_quality`, `FCF bridge`로 충분히 들어가지 않았다.

이건 HBM 특수 문제가 아니라 "강한 도메인 연구축이 final component로 약하게 압축되는 문제"다.

비슷한 예:

- C23 바이오: FDA 승인은 잡았지만 `approval -> royalty/revenue` field가 없으면 Green이 늦어진다.
- C21 금융: ROE/PBR rerating은 잡았지만 `buyback/cancellation execution`이 없으면 자본환원 Green이 약해진다.
- C28 SW/security: 수주/RPO는 잡았지만 `retention`, `NRR`, `renewal`, `margin leverage`가 없으면 recurring revenue Green이 약해진다.

### 삼성: 후보 승격 단계에서 강한 개선을 충분히 못 봄

삼성전자 2024-04-30은 Green gate에서 떨어진 것이 아니라 cheap scan 후보 승격에서 빠졌다.

| symbol | cheap total | next layer | financial score | reason |
| --- | ---: | --- | ---: | --- |
| SK하이닉스 | 34.75 | event_search | 95.0 | OP turnaround, OPM expansion, FCF turnaround |
| 삼성전자 | 6.25 | none | 0.0 | price near high only |

삼성은 OP와 FCF가 크게 좋아졌지만 이미 흑자였기 때문에 `turnaround` rule에 덜 잡혔다. 이 역시 HBM 문제가 아니라 candidate funnel 문제가 될 수 있다.

비슷한 예:

- 보험사가 이미 흑자인 상태에서 K-ICS/CSM/자본환원이 좋아지는 경우
- 금융주가 이미 이익이 나는데 ROE와 배당/자사주가 구조적으로 바뀌는 경우
- 바이오가 적자라도 승인/로열티 경로가 열리는 경우
- 정책/지배구조 이벤트가 손익계산서보다 먼저 가격 프레임을 바꾸는 경우

따라서 후보 funnel도 "적자에서 흑자"만 강하게 보지 말고, 아키타입별 구조 변화 이벤트를 source-backed signal로 받을 수 있어야 한다.

## 연구축과 런타임 필드의 차이

Green-like score row에서 많이 나온 연구축은 다음과 같다.

| research axis | count | 현재 상태 |
| --- | ---: | --- |
| `relative_strength_score` | 2,138 | price signal은 있으나 Green 단독 승격 금지 |
| `execution_risk_score` | 2,115 | red-team으로 세분화 필요 |
| `margin_bridge_score` | 1,964 | OPM/FCF/mix/cash bridge field로 번역 필요 |
| `valuation_repricing_score` | 1,725 | multiple/frame shift field로 번역 필요 |
| `customer_quality_score` | 1,683 | named customer, renewal, allocation, government/customer quality 필요 |
| `policy_or_regulatory_score` | 1,597 | policy headline과 cashflow bridge 분리 필요 |
| `revision_score` | 1,592 | runtime에 일부 있음 |
| `backlog_visibility_score` | 1,589 | backlog/RPO/delivery/reorder field 필요 |
| `contract_score` | 1,588 | duration, amount/sales, prepayment, cancellation field 필요 |
| `accounting_trust_risk_score` | 1,581 | trust/accounting hard guard 필요 |

여기서 중요한 점은 `revision_score` 같은 일부를 빼면 대부분 연구 전용 축이라는 것이다.

쉬운 예:

- 연구가 "고객 질 9점"이라고 썼다고 해서 runtime 점수가 자동으로 오른다.
- runtime은 "그 고객이 누구인지, 재주문인지, 장기계약인지, 취소불가인지, 매출로 이어지는지" 같은 normalized field가 있어야 점수로 쓴다.

## 전체 아키타입에서 생길 수 있는 같은 문제

| archetype group | 연구가 본 핵심 | runtime 변환 결손 |
| --- | --- | --- |
| C01/C02/C03/C05 infra/defense/EPC | backlog, delivery, margin bridge, contract quality | 일부 profile은 있지만 margin/FCF/delivery freshness가 얇음 |
| C06/C07/C08/C10 semis/HBM/equipment | customer qualification, capacity, shipment, ASP, revision | HBM profile은 있어도 capacity/customer/qualification 번역이 약함 |
| C11/C12/C13/C14 battery/EV | orderbook, call-off, JV utilization, AMPC, ex-credit margin | battery profile이 mostly overheat guard라 Green unlock field 부족 |
| C15/C16/C17 materials | spread, utilization, inventory, offtake, policy supply | materials 전용 profile 없음 |
| C18/C19/C20 consumer export | sell-through, reorder, channel quality, inventory, margin | K-food/K-beauty 일부만 있고 inventory/sell-through가 약함 |
| C21 financial | ROE/PBR, credit cost, capital return execution | profile은 추가됐지만 execution primitive와 positive unlock 검증 필요 |
| C22 insurance | CSM, K-ICS, reserve quality, rate cycle, shareholder return | profile은 추가됐지만 reserve/loss-ratio/CSM source-backed 변환 필요 |
| C23/C24/C25 bio/medical | approval, trial quality, royalty, reimbursement, commercialization | commercialization profile은 추가됐지만 trial/medical-device 세부 bridge 필요 |
| C26/C27/C28 platform/content/SW | ARPU, ARR, RPO, retention, IP monetization, margin leverage | SW/security profile은 추가됐지만 content/platform 세부 bridge 필요 |
| C29/C30/C31/C32 mobility/PF/policy/governance | volume/mix/cash, PF repair, policy-to-cash, tender/minority cash path | 대부분 generic/guard 성격으로 압축 |
| R13 guardrail | accounting trust, high MAE, price-only 4B/4C guard | guard 연구는 많지만 production field 승격이 제한적 |

## 해결 원칙

### 1. Green threshold를 낮추지 않는다

하닉을 살리려고 bottleneck 기준을 낮추면 삼성식 catch-up headline도 같이 올라올 수 있다.

쉬운 예:

- 좋은 케이스: "고객이 물량을 선점했고, CAPA가 잠겼고, 실적 revision이 확인됨."
- 나쁜 케이스: "HBM 진출 기대감이 있고 주가가 올랐지만 고객/물량/마진 증거는 약함."

둘을 가르는 것은 threshold 완화가 아니라 evidence translation이다.

### 2. 공통 EvidenceBridgeSpec을 둔다

아키타입별 연구축을 runtime field로 옮기는 명세가 필요하다.

예:

| research axis | normalized runtime evidence |
| --- | --- |
| `margin_bridge_score` | `opm_expansion_pctp`, `actual_op_yoy_pct`, `actual_fcf_yoy_pct`, `fcf_quality_score`, mix improvement |
| `customer_quality_score` | named customer, hyperscaler/government/customer tier, repeat order, allocation, renewal |
| `backlog_visibility_score` | `order_backlog_to_sales`, `rpo_to_sales`, `delivery_schedule`, channel reorder |
| `contract_score` | duration, amount/sales, prepayment, non-cancellable terms |
| `policy_or_regulatory_score` | direct company cash route, subsidy capture, approval-to-revenue bridge |
| `accounting_trust_risk_score` | auditor, restatement, share count drift, source quality, disclosure conflict |

이 명세는 검색어 하드코딩이 아니다. LLM이 찾은 문서와 source-backed evidence를 점수 필드로 번역하는 사전이다.

### 3. 아키타입별 feature adapter를 추가한다

36개 weight를 소수 sector profile로만 처리하면 계속 손실이 난다.

이번 패치로 C21/C22/C23/C28 profile은 추가했지만, 이것은 끝이 아니라 시작이다. 예를 들어 C23 profile이 있어도 실제 문서에서 `approval_to_revenue_bridge`, `royalty_route`, `reimbursement_confirmed`가 안 뽑히면 Green gate는 여전히 약하다.

우선순위:

1. C06/C07/C08/C10 semi conversion: customer/capacity/qualification/margin bridge
2. C21/C22 finance/insurance profile: ROE/PBR/capital return/CSM/K-ICS/reserve
3. C23/C24/C25 bio/medical profile: approval-to-revenue/royalty/reimbursement/trial guard
4. C27/C28 content/SW/security profile: ARR/RPO/retention/IP monetization
5. C30/C31/C32 guard/profile: PF cash bridge, policy-to-cash, tender/minority cash path

### 4. positive와 false-positive를 쌍으로 고정한다

하닉 Green만 fixture로 넣으면 과적합된다. 항상 반례를 같이 넣어야 한다.

최신 fixture 후보 장부는 raw Stage3-Green 381개 중 marker 61개를 guard 쪽으로 분리한다. 쉬운 예로, 라벨은 Green이어도 case_id가 `FALSE_GREEN`이면 positive fixture가 아니라 guard fixture 후보가 된다.

예:

- C06 positive: SK하이닉스 sold-out HBM/capacity/revision
- C06 guard: 삼성 generic HBM optimism/catch-up headline without direct qualification
- C22 positive: capital surplus + reserve quality + shareholder return
- C22 guard: rate-cycle headline without reserve/loss-ratio/capital-return bridge
- C23 positive: approval + commercialization/royalty route
- C23 guard: approval headline without revenue/reimbursement/partner economics

### 5. Green 실패 설명을 field-level로 바꾼다

지금처럼 `failed_stage3_total_score`, `failed_stage3_bottleneck`만 보여주면 원인을 알기 어렵다.

필요한 설명:

```text
연구축: HBM sold-out capacity
번역 기대 field: hbm_capacity_pre_sold, hbm_capacity_constraint, customer_preorder_or_allocation
현재 field: customer_preorder_or_allocation only
점수 손실: capa_constraint 0, backlog_rpo_visibility 15, bottleneck gate fail
```

다른 예:

```text
연구축: insurance reserve quality
번역 기대 field: reserve_quality_score, K-ICS, CSM growth, loss_ratio_quality
현재 field: 없음 또는 generic valuation/capital
점수 손실: earnings_visibility/capital_allocation은 일부 반영, Green confidence 부족
```

## 최종 판단

삼전/하닉 문제의 본질은 HBM 과적합이 아니다.

본질은 다음 두 가지다.

1. candidate funnel이 일부 구조 변화 이벤트를 초기에 못 올린다.
2. 올라온 후보도 연구축이 runtime field로 충분히 번역되지 않아 Green gate에서 막힌다.

따라서 다음 구현은 HBM 전용 가산이 아니라 다음 순서가 맞다.

1. 공통 연구축-런타임 field bridge 작성
2. Green-heavy 아키타입별 feature adapter 추가
3. positive/false-positive 쌍 fixture로 replay 검증
4. score explanation을 field-level 손실 설명으로 개선

한 줄로 말하면, 지금까지 쌓은 연구자료는 쓸모가 있다. 다만 그 연구자료를 운영 점수 계산기가 읽을 수 있는 언어로 번역하는 층이 부족하다.

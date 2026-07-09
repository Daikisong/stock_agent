# E2R Reconstruction Phase 4 — Executable EvidenceRecipe OS

## 판정

`EVIDENCE_RECIPE_OS_COMPILER_PASS`

이 판정은 189개 required `(archetype, primitive)` 쌍이 상세 executable recipe 또는 명시적 unsupported reason으로 빠짐없이 분류됐다는 뜻이다. 현재 executable coverage는 31/189, 16.4021%이므로 `production_runtime_ready=false`다.

## recipe가 검색어와 다른 점

검색어는 “무엇을 입력할까”만 말한다. EvidenceRecipe는 “어떤 사실이면 질문이 닫히는가”까지 말한다.

예를 들어 C06 `customer_preorder_or_allocation` recipe는 다음을 요구한다.

- 질문: 식별 가능한 고객이 target HBM 물량을 특정 제품·기간에 preorder 또는 allocation 받았는가?
- 필수 entity: target memory producer, customer, HBM generation
- 필수 value: commitment/allocation type, disclosed volume/share, covered period
- 합격: target-direct source에 customer commitment/allocation과 기간이 같이 있음
- 탈락: AI 수요 전망뿐이고 고객 commitment가 없음
- counter: 취소 가능, 조건부, evaluation forecast인지 확인
- lifecycle: 취소·축소·납품완료·만료·신규 update로 supersede됐는지 확인
- source: DART/IssuerIR/earnings call 우선, full article/research report 보조
- 금지: search snippet, price move, theme label, source proxy

코드는 이 recipe로 literal query를 만들지 않는다. 이후 LLM planner가 current evidence와 target을 보고 query를 만들고, deterministic 코드는 recipe 제약을 검증한다.

## canonical schema

EvidenceRecipe에는 다음이 모두 들어간다.

- archetype, primitive, role
- economic mechanism
- question to answer
- accepted claim predicates
- required entities, values, units, time
- target directness와 current lifecycle
- preferred source families, document types, sections
- discovery source와 forbidden score source
- positive, counter, wrong-subject examples
- source success/failure examples
- rejection conditions
- counter/supersession questions
- query intent constraints
- stop/source exhaustion conditions
- supporting historical case IDs
- verified source success IDs와 source failure IDs
- planning-only source-proxy case IDs

recipe 자체는 `runtime_score_eligible=false`다. recipe는 증거가 무엇이어야 하는지를 정의할 뿐, 점수를 만들지 않는다.

## 상세 지원 범위

| archetype | recipe 수 |
|---|---:|
| C06 HBM customer/capacity | 6 |
| C08 test/socket customer quality | 5 |
| C15 material spread | 5 |
| C17 chemical spread | 5 |
| C24 biotech trial event risk | 5 |
| C28 software contract/retention | 5 |
| 합계 | 31 |

판례의 역할도 유지한다.

- C17 `raw_material_cost_risk`: 현재 margin bridge를 막는 `GUARD`
- C24 `binary_event_unresolved`, `approval_not_confirmed`, `safety_signal`, `cash_runway_risk`: current + quorum일 때의 `HARD_BREAK`
- C15 spread: output price만 보지 않고 input cost, inventory, utilization, OPM, FCF 연결을 요구
- C28: security/AI product keyword만으로는 ARR/NRR/renewal/RPO/margin recipe가 닫히지 않음

## unsupported를 숨기지 않는 이유

나머지 158개 pair에는 `UNSUPPORTED_PENDING_SEMANTIC_RECIPE`를 부여했다.

쉬운 예로, detailed semantics가 없는 `contract_quality`를 코드가 `{company} contract quality` 같은 검색어로 바꾸면 겉보기에는 route가 생긴다. 하지만 금융계약, 자사주 신탁, 담보계약도 잘못 잡을 수 있다. 그래서 reviewed mechanism, predicate, examples, rejection/lifecycle rule이 생길 때까지 runtime route를 열지 않는다.

각 unsupported record는 다음을 보장한다.

- planning-only
- runtime route unavailable
- exact reason
- 추가로 필요한 semantic input 목록

## hard acceptance

| 검사 | 결과 |
|---|---:|
| required pair without recipe/unsupported | 0 |
| URL-backed case recipe example missing | 0 |
| source-proxy example not planning-only | 0 |
| generic query-only recipe | 0 |
| primitive substring production routing | 0 |
| acceptance/rejection missing | 0 |
| counter question/example missing | 0 |
| lifecycle/supersession missing | 0 |
| literal query in recipe | 0 |
| recipe direct score eligibility | 0 |
| unsupported runtime route available | 0 |

## 출력

공식 compile CLI는 `recipes/` 아래에 다음을 쓴다.

- `evidence_recipes.jsonl`
- `unsupported_evidence_recipes.jsonl`
- `evidence_recipe_manifest.json`
- `evidence_recipe_report.md`

full registry 실행에서도 31개 recipe, 158개 unsupported, pair coverage 100%, critical count 0이 재현됐다.

## 아직 통과하지 않은 것

Phase 5에서는 case·recipe·primitive·source를 graph로 연결하고 positive/guard/source-success/source-failure를 균형 있게 retrieval해야 한다. 또한 최종 runtime readiness 전에 현재 unsupported 158개 중 실제 운영에 필요한 primitive semantics를 추가로 검토해야 한다. unsupported reason은 안전한 경계이지 완료된 runtime route가 아니다.

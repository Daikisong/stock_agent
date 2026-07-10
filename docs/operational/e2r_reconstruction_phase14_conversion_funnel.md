# E2R Reconstruction Phase 14 — Conversion Funnel Observability

## 판정

`CONVERSION_FUNNEL_OBSERVABILITY_PASS`

Research Brain의 진척을 task 개수나 accepted claim 총량으로 말하지 않고, 실제 leaf 계보가 어디까지 이어졌는지 candidate와 archetype별로 다시 계산하는 관측 경로를 만들었다.

```text
candidate
→ hypothesis
→ retrieval
→ recipe
→ SourceTask
→ query
→ result
→ fetched document
→ relevant document
→ assertion
→ claim
→ primitive
→ score
→ full thesis / pending / disproved
```

이번 결과는 deterministic fixture와 Phase 7~12 canonical 객체 연결 테스트다. 실제 daily 전체 실행의 비용과 conversion을 관측한 것은 아니므로 `production_runtime_ready=false`다.

## 왜 단순 개수로는 부족한가

다음 두 실행을 비교해 보자.

```text
실행 A: SourceTask 10개, accepted claim 5개, 원래 gap 직접 closure 0개
실행 B: SourceTask 2개, accepted claim 1개, 원래 gap 직접 closure 1개
```

실행 A가 더 바빠 보이지만 원래 질문은 하나도 해결하지 못했다. 실행 B는 적은 작업으로 실제 material gap 하나를 닫았다. Phase 14에서는 B의 meaningful progress가 1이고 A는 0이다.

고정 fixture도 같은 차이를 의도적으로 만든다.

| 항목 | 수 |
|---|---:|
| candidate | 5 |
| SourceTask shell | 5 |
| claim | 4 |
| accepted claim | 3 |
| direct original-gap closure | 1 |
| rerouted accepted claim | 1 |
| mapping rejection | 1 |

accepted claim 3개를 progress 3으로 쓰지 않는다. 직접 원래 gap을 닫은 task가 1개이므로 `meaningful_progress_count=1`이다. SourceTask shell의 progress credit은 항상 0이다.

같은 original gap을 재시도하는 SourceTask가 여러 개여도 gap 분모는 하나다. 예를 들어 같은 FCF 질문에 task가 3개 생겼다면 `SourceTask shell=3`, `distinct original gap=1`로 기록한다.

## Leaf 그래프와 계보

각 단계는 단순 숫자가 아니라 `leaf_id`, `candidate_id`, `parent_ids`를 가진다. stage별로 허용하는 부모도 정해져 있다.

쉬운 예:

```text
CLAIM-101
  parent = ASSERTION-101
  task = TASK-7
  original_gap = OGAP-7
  recipe = contract_quality_recipe
  primitive = contract_quality
```

audit는 `ASSERTION-101 → RELEVANT-DOC → FETCHED-DOC → RESULT → QUERY → TASK-7`을 거슬러 올라간다. 중간 부모가 없거나 다른 candidate의 문서를 붙이면 실패한다.

중복 ID뿐 아니라 같은 task/query/document/claim/score decision을 다른 leaf ID로 복제해 분모나 분자를 부풀리는 것도 별도 lineage 중복으로 탐지한다.

## Relevant document rate

고정 fixture는 문서 5개를 full fetch했고 그중 recipe 질문과 직접 연결된 relevant document가 4개다.

```text
relevant document rate = 4 / 5 = 0.8
```

검색 결과 snippet이나 URL 개수는 분모가 아니다. `FETCHED_DOCUMENT` leaf가 있어야 분모에 들어가며, selector를 통과한 `RELEVANT_DOCUMENT` leaf만 분자에 들어간다.

한 fetched document를 두 개의 relevant leaf로 복제하면 document lineage 중복과 metric projection mismatch가 발생한다.

## Accepted claim rate와 direct closure

claim 4개의 상태는 다음과 같다.

- 원래 task를 정확히 닫은 direct support 1개
- 다른 recipe/primitive로 매핑된 rerouted support 1개
- current direct counter claim 1개
- mapping rejection 1개

accepted claim rate는 `3 / 4 = 0.75`다. 하지만 direct original-gap closure rate는 `1 / 5 SourceTask = 0.2`다.

두 비율은 목적이 다르다.

- accepted claim rate: 문서에서 유효한 claim을 얼마나 만들었는가
- direct closure rate: 처음 풀려고 한 material 질문을 얼마나 직접 해결했는가

운영 진척의 primary metric은 두 번째다.

## Rerouted claim은 유용하지만 원래 gap을 닫지 않는다

예를 들어 `contract_quality`를 찾다가 유효한 `capacity_lock` claim을 발견할 수 있다. 이 claim은 버리지 않고 `ACCEPTED_REROUTED`로 남기며 해당 archetype/primitive 관측에도 포함한다.

```text
original task: contract_quality
accepted mapping: capacity_lock
→ accepted claim +1
→ rerouted claim +1
→ contract_quality direct closure +0
→ original gap remains open
```

rerouted route는 원래 task와 recipe, primitive 또는 archetype이 실제로 달라야 한다. 같은 route인데 rerouted라고 쓰거나, rerouted claim을 direct로 바꿔 progress를 올리면 audit가 잡는다.

또한 rerouted claim 뒤에 100점 score를 위조해도 원래 SourceTask gap이 열려 있으면 `full_thesis_with_open_original_gap`으로 실패한다.

## Terminal outcome과 pending reason

5개 candidate는 각각 terminal leaf 하나를 가진다.

| outcome | 수 |
|---|---:|
| `FULL_THESIS` | 1 |
| `DISPROVED` | 1 |
| `SOURCE_PENDING` | 2 |
| `PROVIDER_PENDING` | 1 |
| `BUDGET_PENDING` | 0 |

pending은 하나로 뭉개지 않고 이유를 보존한다.

```text
mapping_rejected_original_gap_open: 1
original_gap_open_after_rerouted_claim: 1
official_provider_timeout: 1
```

`FULL_THESIS`는 final `FULL_E2R_100` score와 모든 원래 SourceTask의 direct closure가 있어야 한다. `DISPROVED`는 hard-break `NO_SCORE`가 있어야 한다. `PROVIDER_PENDING`은 ancestor RESULT에 정확한 provider error가 있어야 한다.

## Candidate·archetype별 독립 지표

동일 leaf에서 다음 세 scope를 다시 만든다.

- `GLOBAL`: 전체 funnel
- `CANDIDATE`: 후보별 funnel
- `ARCHETYPE`: stage leaf에 기록된 archetype별 funnel

고정 fixture는 candidate row 5개, archetype row 6개, global row 1개로 총 metric 12행이다. rerouted claim이 대체 archetype으로 연결됐기 때문에 candidate는 5개여도 관측 archetype은 6개다.

저장된 metric을 신뢰하지 않는다. audit가 candidates, stage leaves, usage leaves에서 metric을 다시 만들고 scope별 projection을 비교한다. metric 숫자만 손으로 바꾸면 leaf와 맞지 않아 실패한다.

## 비용과 runtime

각 provider 사용은 별도 `FunnelUsageRecord`를 가진다.

- query/result/fetch 수
- input/output token
- cost USD
- runtime seconds
- 실제 operation leaf IDs

고정 fixture의 합계는 query 5, result 5, fetch 5, input token 533, output token 266, 비용 `$0.55`, runtime 28초다.

같은 operation leaf를 두 usage record에서 다시 청구할 수 없다. usage의 query/result/fetch 합도 실제 stage leaf 수와 맞아야 한다. 비용만 `$0.55`에서 `$99`로 바꾸면 leaf hash와 metric projection이 함께 깨진다.

## Canonical Phase 연결

별도 integration fixture에서 다음 실제 canonical ID를 한 경로에 보존했다.

```text
Phase 7 QuestionSourceTask.task_id
→ LLM literal query
→ Phase 8 AcquiredDocument.document_id
→ Phase 9 RawAssertion.raw_assertion_id
→ Phase 9 ClaimLedgerEvent.claim_id / mapped recipe / primitive
→ Phase 12 AtomicStageDecision.decision_id
→ FULL_THESIS terminal
```

`original_gap_id`가 기존 task에 별도 필드로 없기 때문에 context ID, recipe, primitive, `missing_information` 전체를 hash해 deterministic `OGAP-*` ID를 만든다. retry마다 달라지는 task ID는 hash에서 뺀다. 종목명이나 primitive 이름별 조건문으로 gap을 만들지 않는다.

이 연결은 test fixture다. 같은 객체 ID가 보존됐다는 뜻이지 실제 provider 비용이나 production daily completion을 증명하지 않는다.

## Known-bad 변이

다음 변이를 실제로 넣어 감사기가 잡는지 확인했다.

- leaf ID 복제
- RECIPE 부모를 RETRIEVAL 대신 CANDIDATE로 변경
- ASSERTION의 terminal CLAIM 삭제
- rerouted claim을 direct claim으로 위조
- SourceTask 5개를 meaningful progress 5로 위조
- `FULL_THESIS`의 full score 제거
- provider error를 지우고 `PROVIDER_PENDING` 유지
- rerouted original gap이 열린 후보를 full thesis로 위조
- usage 비용만 변경
- usage query 수와 실제 QUERY leaf 수를 다르게 변경
- result audit 객체를 0으로 교체

정상 실행은 48개 critical 조건이 모두 0이다. leaf hash는 `823fc6436371fa503b94fdebfbb23eba68fc5f7b0e3427cbe04e1d60adaafe36`, metric hash는 `e42d30e850722d9100fbf03dbd9d7c18df236c147f1757980654efaf308a8239`다.

## 주요 파일

- `runtime/conversion_funnel.py`: stage leaf, usage leaf, candidate/archetype metric, 독립 audit와 writer
- `runtime/__init__.py`: Phase 14 public API
- `tests/test_conversion_funnel_observability.py`: 정상 funnel, canonical Phase 연결, known-bad 검사
- `e2r_reconstruction_phase14_acceptance.json`: 고정 Phase 14 acceptance

## 검증 경계와 다음 단계

Phase 14는 “얼마나 많이 시도했는가”와 “원래 material gap을 얼마나 직접 닫았는가”를 분리했다. 하지만 실제 daily run 전체가 이 leaf를 내보냈다는 production credit은 아직 없다.

다음 Phase 15에서는 지금까지 각 Phase에서 막은 known-bad를 하나의 통합 suite로 모은다. file-level case collapse, source proxy, wrong subject, rerouted gap closure, provider failure Red, replay contamination, event score full score, Stage/trace mismatch 등을 한 번에 검증해야 한다.

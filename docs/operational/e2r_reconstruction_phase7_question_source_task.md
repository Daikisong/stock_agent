# E2R Reconstruction Phase 7 — Question-Centric SourceTask

## 판정

`QUESTION_SOURCE_TASK_CONTRACT_PASS`

이 판정은 SourceTask가 primitive 이름만 가진 작업표가 아니라, 질문·성공조건·반증조건·source 경로·LLM literal query·budget·중단조건을 모두 가진 실행 계약이 되었다는 뜻이다. 아직 Phase 8 acquisition에 production cutover하지 않았고 query benchmark도 fixture provider이므로 `production_runtime_ready=false`다.

## 이전 task의 문제

기존 task는 대체로 다음 정도였다.

```text
primitive_gap = revenue_visibility_contract
preferred_source = DART
max_fetches = 5
```

이 정보만으로는 “어떤 claim이면 성공인가”, “고객 계약이 취소 가능하면 실패인가”, “어느 문서의 어느 section을 봐야 하는가”를 알 수 없다. 실행기는 문서를 하나 찾았다는 이유만으로 gap을 닫을 위험이 있다.

새 task는 다음 질문을 중심에 둔다.

```text
대상 회사의 현재 계약이 취소·감액 가능한 단순 forecast가 아니라,
기준일 현재 구속력 있는 매출 가시성을 제공하는가?
```

그리고 이 질문에 필요한 accepted predicate, target 직접성, lifecycle, counter question과 rejection condition을 함께 저장한다.

## canonical 구조

| 계약 | 역할 |
|---|---|
| `QuestionAcceptanceContract` | accepted predicates, entity/value/unit/time, target 직접성, lifecycle, counter, rejection |
| `SourceRouteContract` | official-first source, document type, section, discovery와 forbidden source |
| `QueryIntent` | LLM이 현재 context에서 만든 literal queries와 prompt/response hash |
| `SourceBudget` | `max_queries`, `max_candidates`, `max_fetches`의 양수 상한 |
| `StopCondition` | claim 해결 시 중단하는 조건과 source exhaustion 조건 |
| `QuestionSourceTask` | 위 계약을 recipe, context ID, current fact ID, 대상·기준일에 연결한 canonical task |

31개 executable EvidenceRecipe 모두 QuestionSourceTask로 변환했고 필수 계약 누락은 0개였다.

## literal query는 누가 만드는가

deterministic 코드는 literal query를 만들지 않는다. LLM provider가 다음 current context를 보고 query를 제안한다.

- 대상 회사명·symbol·alias
- `as_of_date`
- 현재 fact
- missing information
- 아직 답하지 못한 질문과 accepted predicates
- counter/rejection 조건
- official source/document/section 경로
- 이미 실행한 query와 bounded budget

코드는 제안된 query를 검증만 한다.

쉬운 예:

- 허용 예: `테스트기업 2025 1Q 공식 공시 IR 고객 계약 취소 조건`
- 거절 예: `verify primitive customer_preorder_or_allocation`
- 거절 예: `테스트기업 latest contract news`
- 거절 예: `as_of_date=2025-03-31`인데 `테스트기업 2026 Q1 earnings`
- 거절 예: 대상 이름 없이 `HBM allocation contract`

거절된 query를 코드가 다른 템플릿으로 바꾸지 않는다. 대신 실패 사유와 rejected query만 다음 LLM prompt에 돌려주고 최대 3회 bounded 재시도한다. 예를 들어 첫 query의 `2026 Q1`이 기준일 이후라면 두 번째 prompt에는 “future reporting quarter”라는 validator feedback이 들어간다. 코드는 대신 `2025 Q1`을 만들지 않는다. 세 번 모두 유효하지 않거나 provider 자체가 실패하면 `QuestionTaskPending`이다.

## query validator

다음 조건을 deterministic하게 검사한다.

- 대상 회사명·symbol·alias 중 하나 포함
- 명시적 reporting year 포함
- `as_of_date` 이후 ISO date, year, quarter 없음
- `latest`, `today`, `최신`, `오늘` 같은 상대시점 없음
- 같은 run의 중복 및 이미 실행한 query 중복 없음
- primitive ID와 canonical archetype ID 복사 없음
- score, E2R Stage, outcome, MFE/MAE 누출 없음
- task의 `max_queries` 이내

예를 들어 장기계약이 2030년까지라는 과거 공시를 확인해야 한다면 LLM은 기준 문서의 발표 기간을 query에 명시해야 한다. 미래에 발표될 2030년 실적을 찾는 식의 query는 허용하지 않는다.

## official-first와 budget

모든 canonical task의 첫 preferred source는 DART/KIND/KRX/issuer IR/공식 registry 같은 official family여야 한다. Naver와 general web은 recipe가 허용한 discovery 경로일 뿐 첫 source가 될 수 없다.

상한은 다음과 같다.

- `max_queries <= 10`
- `max_candidates <= 100`
- `max_fetches <= 20`

FCF, 계약, 수주잔고 질문을 Naver-first로 보내는 task는 생성 단계에서 거절한다. 실제 stop-on-resolution과 source exhaustion의 실행 의미는 Phase 8 acquisition runner가 소비한다.

## guard task의 방향

recipe role이 `GUARD` 또는 `HARD_BREAK`이면 positive verification task로 포장할 수 없다. red-team, contradiction resolution, lifecycle follow-up처럼 방어적 task type을 사용해야 한다.

쉬운 예: “임상 binary event가 아직 해결되지 않았다”는 hard-break recipe를 positive evidence 찾기 task로 만들면 위험하다. 새 validator는 이를 `defensive task type` 불일치로 거절한다.

## legacy migration

기존 `SourceTask` reader와 audit는 남겼다. 하지만 다음 항목을 adapter에 명시적으로 주지 않으면 `INVALID_LEGACY_TASK`다.

- `recipe_id`
- `question_to_answer`
- `why_material`
- LLM query intent

legacy task는 diagnostic payload로 읽을 수 있지만 canonical production router의 기본 호출은 거절한다. 즉, 낡은 task를 필드가 채워진 것처럼 가장해 production에 흘리지 않는다.

## 31-recipe 감사

| 항목 | 결과 |
|---|---:|
| QuestionSourceTask | 31 |
| empty question | 0 |
| empty accepted predicate | 0 |
| empty rejection condition | 0 |
| generic verify-primitive task | 0 |
| official-first violation | 0 |
| FCF/contract/backlog Naver-first | 0 |
| unbounded query/fetch | 0 |
| missing LLM literal query | 0 |

31개 query는 fixture LLM으로 만든 test-mode 결과다. 따라서 production execution allowed count는 0이고, 이 결과만으로 실제 provider 성능이나 production readiness를 선언하지 않는다.

## 검증 결과

- Phase 0~7 compiler/planner targeted chain: 124개 통과
- legacy SourceTask 관련 별도 회귀: 12개 통과
- full suite: 5,431개 실행, 기존 기준선과 동일한 18개 실패
- Phase 7 신규 실패: 0개

18개는 Phase 0부터 기록된 mutable goal4 research-to-runtime snapshot 불일치다. 이를 전체 통과로 숨기지는 않지만 Phase 7 회귀로도 세지 않는다.

## 주요 파일

- `planning/source_task.py`: canonical schema, LLM query provider, decoder, validator, audit
- `planning/source_task_bridge.py`: legacy adapter와 canonical router payload
- `source_task_bridge.py`: legacy diagnostic reader/audit
- `tests/test_question_source_task.py`: 31-recipe coverage와 hard acceptance

## 다음 경계

Phase 7은 “무슨 질문을 어떤 조건으로 찾는가”를 완성했다. Phase 8은 이 task를 `PRODUCTION_BOUNDED`, `HISTORICAL_REPLAY`, `SOURCE_REPAIR_BACKFILL`, `CONTROLLED_SMOKE` 모드에서 실제 source/document로 연결하고, snippet·무날짜 문서·snapshot-as-live를 차단한다.

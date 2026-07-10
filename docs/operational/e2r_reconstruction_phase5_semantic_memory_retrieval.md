# E2R Reconstruction Phase 5 — Semantic Memory Graph와 Balanced Retrieval

## 판정

`SEMANTIC_MEMORY_RETRIEVAL_COMPILER_PASS`

이 판정은 historical case, EvidenceRecipe, primitive, archetype, source를 stable ID graph로 연결하고, blind benchmark에서 goal.md의 retrieval 기준을 넘었다는 뜻이다. 아직 Phase 6 two-pass planner에 production cutover하지 않았으므로 `production_runtime_ready=false`다.

## 왜 단순 memory 검색과 다른가

이전 방식은 같은 archetype의 record를 저장 순서대로 `limit=20`처럼 잘랐다. record가 많은 archetype이나 먼저 들어온 record가 유리할 수 있었다.

새 방식은 node 수나 입력 순서를 점수에 쓰지 않는다. current evidence와 graph의 고유 semantic concept가 얼마나 맞는지를 보고 archetype과 recipe를 찾는다. 같은 node를 세 번 복제하거나 index 순서를 완전히 뒤집어도 결과가 같다.

쉬운 예:

- 입력: “화학 제품 가격은 올랐지만 나프타·운임·환율 비용이 더 빨리 올라 segment margin이 축소됐다.”
- direct recipe: C17 `raw_material_cost_risk`
- positive evidence: 대상 회사가 원재료 비용과 margin 압박을 직접 설명
- counter: hedge와 판가 전가로 비용이 완전히 상쇄됐는가
- semantic guard: 나프타 지수 상승만 있고 대상 회사 연결이 없는가
- source success: 대상 segment 실적표·IR·컨콜의 직접 anchor
- source failure: 업종 headline이나 snippet만 있고 target margin bridge가 없음

positive 한 줄만 주는 것이 아니라 반증과 source 실패까지 같은 묶음으로 반환한다.

## graph 구조

Node type은 다음 10개다.

- `ARCHETYPE`, `PRIMITIVE`, `CASE`, `RECIPE`, `SOURCE`
- `POSITIVE`, `COUNTER`, `HARD_BREAK`
- `SOURCE_SUCCESS`, `SOURCE_FAILURE`

Edge type은 goal.md의 9개를 그대로 구현했다.

- `SUPPORTS`, `COUNTERS`, `CAPS`, `REQUIRES`
- `BEST_FOUND_IN`, `FAILED_IN`, `SUPERSEDES`
- `WRONG_SUBJECT_EXAMPLE`, `SAME_MECHANISM`

full registry 결과:

| 항목 | 수 |
|---|---:|
| historical case | 10,920 |
| source verification | 14,201 |
| executable recipe | 31 |
| graph node | 25,532 |
| graph edge | 44,221 |
| planner-visible node | 23,337 |
| outcome identity 때문에 planner-hidden | 2,195 |

graph에 node를 숨겼다고 삭제한 것은 아니다. identity와 audit 연결은 보존하고 `planner_visible=false`로 차단했다.

## historical outcome 차단

HistoricalOutcome 19,031개는 graph compiler 입력 자체에 없다. MFE, MAE, expected stage, future return, outcome label이 planner-visible node나 index concept에 들어가면 schema가 즉시 실패한다.

특히 canonical taxonomy에 `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL`이 존재한다. 이 ID를 planner에 그대로 주는 것 자체가 MAE 정보를 노출하므로 다음처럼 처리했다.

- graph identity: 보존
- planner-visible retrieval: 차단
- benchmark archetype 분모: exact reason과 함께 제외
- 향후 해결: outcome-derived taxonomy를 planner-safe ontology와 evaluator overlay로 분리

쉬운 예: 시험지 정답 보관함에는 “정답률”을 남길 수 있지만, 문제를 푸는 학생 책상에는 그 정답률 표를 올려놓지 않는 것과 같다.

## as_of_date

case와 source node에는 `available_from_date`가 있다. retrieval은 `available_from_date > as_of_date`인 node를 제외한다.

예: `as_of_date=2025-01-01`이면 2030년에 만들어진 historical case analogy는 반환하지 않는다. recipe와 ontology는 날짜 없는 정책 node이고, 실제 과거 사례·source만 point-in-time 필터를 받는다.

## blind benchmark

raw evidence에는 expected archetype ID나 primitive ID를 넣지 않았다. evaluator label은 request 생성 후 별도 비교한다.

| 지표 | 결과 | 기준 |
|---|---:|---:|
| registry archetype coverage | 36/36 | 전체 registry |
| top-3 archetype | 60/60 = 100% | 95% 이상 |
| required recipe | 31/31 = 100% | 95% 이상 |
| positive+guard pair | 31/31 = 100% | 90% 이상 |
| future leakage | 0 | 0 |
| first-N-only | 0 | 0 |
| popularity bias critical | 0 | 0 |

top-3 분모가 61이 아닌 60인 이유는 위의 outcome-derived R13 ID 1개를 planner에서 숨겼기 때문이다. recipe 분모 31은 Phase 4에서 reviewed executable semantics가 있는 6개 archetype의 31개 primitive다. 나머지 30개 archetype recipe는 성능 실패로 숨기지 않고 `UNSUPPORTED_PENDING_SEMANTIC_RECIPE` 상태를 유지한다.

## 출력

공식 compile CLI는 `retrieval/` 아래에 다음을 쓴다.

- `research_memory_nodes.jsonl`
- `research_memory_edges.jsonl`
- `semantic_memory_index.jsonl`
- `semantic_memory_manifest.json`
- `blind_retrieval_results.jsonl`
- `balanced_retrieval_acceptance.json`
- graph/retrieval Markdown report

## 아직 통과하지 않은 것

Phase 5는 compiler와 deterministic graph retrieval의 의미·안전 경계를 증명한다. 실제 current evidence를 blind Pass A가 읽고 top-k hypothesis를 만들며, Pass B가 이 balanced memory로 비판하는 경로는 Phase 6에서 구현한다. 따라서 이 결과만으로 current production full-thesis나 `PRODUCTION_READY`를 선언하지 않는다.

# E2R EVIDENCE INTELLIGENCE RECONSTRUCTION PROGRAM v1
## Research Corpus Semantic Compiler / Evidence Recipe OS / Unified Research Brain / Adaptive Claim Closure / Historical Replay & Current Operation

너는 `Daikisong/stock_agent` 레포를 원래 의도대로 다시 작동시키는 수석 아키텍트이자 구현 에이전트다.

이번 작업은 기존 Goal4 위에 감사 게이트를 하나 더 붙이는 일이 아니다.
이번 작업은 **연구자료를 운영 지능으로 바꾸는 핵심 계층을 재건**하는 작업이다.

현재 레포에는 다음 자산이 이미 존재한다.

- 수백 개의 historical research MD와 machine-readable JSONL/CSV/table row
- C01~C32 canonical archetype과 R13 cross-archetype registry
- Evidence Contract, deterministic score engine, StageCourt
- Evidence OS의 claim/primitive/score ledger 철학
- OpenDART/KIND/KRX/CompanyGuide/IR/TrustedNews/Naver/Web connector
- Research Brain, Memory Store, LLM planner/provider, Census, Production Cutover
- 광범위한 테스트와 known-bad regression

하지만 현재 official verdict는 `MEANINGFUL_RUNTIME_PARITY_NOT_READY`다.

현재의 근본 결함은 다음이다.

1. historical research 파일을 case 단위로 의미 있게 컴파일하지 않고,
   파일 앞부분, 키워드, 첫 종목코드, primitive 문자열 출현 여부로 얕게 축약한다.

2. 연구 MD 안에 이미 존재하는 `case`, `trigger`, `score_simulation`, `shadow_weight`,
   `residual_contribution`, `stage_transition_summary`, source URL과 날짜를 충분히 보존하지 않는다.

3. `research_brain`이라는 기존 계층과,
   Goal4에서 추가한 `research_reverse` / `source_routing` 계층이 병렬로 존재한다.
   같은 연구자료를 서로 다른 schema와 heuristic으로 읽어 두 개 이상의 두뇌가 생겼다.

4. MemoryCard가 historical positive/counterexample의 의미를 학습한 카드라기보다
   기존 Evidence Contract의 required/positive/green primitive를 다시 포장한 카드에 가깝다.

5. Source Route가 historical research에서 실제 성공한 문서·섹션·claim 경로를 복원한 것이 아니라,
   primitive 이름에 `contract`, `margin`, `hbm` 등이 들어가는지를 보고 자료실을 추정한다.

6. Research Brain planner가 실제 연구자처럼 사고하는 것이 아니라,
   event text와 archetype 이름의 토큰을 매칭하고,
   generic한 “이 primitive를 source-backed하게 확인하라”는 작업을 만든다.

7. 검색 결과에서 문서는 가져오지만,
   원래 질문을 직접 충족하는 claim이 아니라 generic company fact나 다른 primitive claim을 얻는 경우가 많다.
   `rerouted claim accepted`가 원래 gap을 닫은 것처럼 보일 위험이 있다.

8. `until_pass` 실행기는 코드를 고치는 self-repair가 아니다.
   같은 manifest/run을 재실행하고, blocker가 남으면 코드나 route repair가 필요하다고 멈추는 runtime retry다.

9. “전 아키타입 시스템이 이해하는가?”를 검증하는 historical replay와
   “현재 시장에 어떤 종목이 좋은가?”를 판단하는 current operation이 섞여 있다.
   현재 시장에 없는 아키타입까지 억지 종목 materialization을 시도하면서 이상한 routing과 C05 편향이 발생했다.

10. audit/report/manifest의 개수는 늘었지만,
    핵심 conversion funnel인
    `research case → evidence recipe → source task → fetched document → direct accepted claim → primitive closure → full thesis`
    가 충분히 닫히지 않았다.

이번 Goal은 위 문제를 뿌리부터 해결한다.

---

# 0. 최종 목표

원래 의도한 시스템은 다음이어야 한다.

[Historical Research Intelligence]

historical research MD/JSONL
→ case-level semantic compiler
→ historical case graph
→ positive / counterexample / guard / source-success / source-failure memory
→ primitive별 executable Evidence Recipe
→ archetype별 Runtime Intelligence Pack
→ frozen historical replay benchmark

[Current Runtime Operation]

현재 시장 CandidateEvent / Census state / existing claim ledger
→ contract-blind current hypothesis generation
→ Research Memory retrieval
→ LLM Research Brain critique / top-k archetype / missing evidence questions
→ bounded official-first SourceTask
→ DART / KIND / KRX / CompanyGuide / IR / report / Naver/Web acquisition
→ full source document / table / API record
→ contract-blind RawAssertion extraction
→ subject / target / time / lifecycle adjudication
→ primitive mapping
→ append-only accepted claim ledger
→ PrimitiveState
→ ScoreContribution
→ deterministic scorer
→ StageCourt
→ Stage + score + evidence + missing conditions

역할은 다음처럼 고정한다.

Historical research:
현재 점수의 증거가 아니라, 무엇을 어떻게 찾아야 하는지 가르치는 판례집

LLM Research Brain:
아키타입 가설, 조사 질문, source route, query intent, claim extraction, 반례 탐색

Code:
source/date/scope/current lifecycle/duplicate/conflict/primitive eligibility 검증

Deterministic scorer / StageCourt:
점수와 Stage 계산

현재 source-backed claim:
점수에 들어가는 유일한 증거

---

# 1. 최우선 금지사항

다음은 어떤 Phase에서도 금지한다.

1. scoring weight 또는 Stage threshold를 변경해서 통과하지 마라.
2. C05, 삼성전자, SK하이닉스 같은 특정 종목/아키타입 예외를 하드코딩하지 마라.
3. source_proxy_only / evidence_url_pending / price_path_only / shadow_only research row를 current score evidence로 쓰지 마라.
4. historical MFE/MAE/outcome label을 current planner나 claim extractor prompt에 넣지 마라.
5. LLM이 score/stage를 직접 출력하거나 FeatureInput/ScoreContribution을 mutate하지 못하게 하라.
6. primitive 이름을 보고 고정 query string을 만드는 deterministic query template를 만들지 마라.
7. 뉴스 headline/snippet을 score evidence로 쓰지 마라.
8. Naver/Web search result가 full article fetch 없이 점수로 들어가지 못하게 하라.
9. provider failure, source gap, runtime budget exhaustion을 낮은 점수나 Red로 확정하지 마라.
10. accepted claim이 없는데 nonzero score를 만들지 마라.
11. 원래 primitive와 다른 rerouted claim이 accepted되었다고 원래 source task를 satisfied 처리하지 마라.
12. old risk를 current OPEN 확인 없이 현재 penalty/hard break로 쓰지 마라.
13. report summary 숫자를 leaf artifact보다 우선하지 마라.
14. PASS 라벨을 report-only commit으로 바꾸지 마라.
15. 실패한 test를 삭제하거나 threshold를 낮춰 통과하지 마라.
16. 동일 runtime 명령 재실행만 하고 self-repair라고 부르지 마라.
17. 현재 시장에 각 아키타입 후보가 없다는 이유로 억지 종목을 materialize하지 마라.
18. historical replay와 current operation의 결과를 같은 production row로 섞지 마라.
19. 기존 research MD를 수정·삭제해 의미를 바꾸지 마라.
20. 새로운 historical research round를 시작하지 마라. 연구는 끝났고, 기존 연구를 제대로 컴파일하는 것이 이번 목표다.

---

# 2. 실행 프로토콜

코딩을 시작하기 전에 반드시 아래 순서로 진행한다.

## 2.1 최초 Read-Only Forensic

먼저 코드를 고치지 말고 다음을 읽고 call graph를 만든다.

- `AGENTS.md`
- `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`
- `docs/core/V12_Research_No_Repeat_Index.md`
- `docs/operational/research_to_runtime_acceptance_report.md`
- `docs/operational/research_to_runtime_readiness_verdict.md`
- `docs/0701/*`
- `docs/0703/*`
- `docs/0705/*`
- `src/e2r/research_brain/**`
- `src/e2r/research_reverse/**`
- `src/e2r/source_routing/**`
- `src/e2r/production/**`
- `src/e2r/census/**`
- `src/e2r/evidence/**`
- `src/e2r/scoring/**`
- `src/e2r/stage/**`
- 관련 CLI와 tests

생성:

docs/operational/e2r_reconstruction_forensic_baseline.md
docs/operational/e2r_runtime_call_graph_before.json
docs/operational/e2r_duplicate_brain_stack_inventory.json
docs/operational/e2r_current_conversion_funnel_baseline.json

반드시 기록할 것:

- production에서 실제 호출되는 entrypoint
- 각 entrypoint가 어떤 parser/memory/planner/router/extractor를 사용하는지
- `research_brain`과 `research_reverse/source_routing` 중복 경로
- production reachable / test-only / dead code
- summary artifact를 다시 읽는 경로
- source task → accepted claim → primitive → score → StageCourt 연결부
- 현재 failure funnel
- current official verdict와 blockers

## 2.2 내부 Master Plan

그 다음에 아래 문서를 작성한다.

docs/operational/e2r_reconstruction_master_plan.md

각 Phase마다 다음을 적는다.

- 문제
- root cause file/function
- 제거할 legacy path
- 새 schema/API
- migration 방식
- 구현 파일
- 테스트
- runtime acceptance
- rollback point
- commit message

Master Plan 작성 후 질문하거나 확인을 요구하지 말고 즉시 구현에 들어간다.

## 2.3 Phase Commit 규칙

각 Phase는 독립적인 한글 커밋으로 남긴다.

예:

Phase 0: E2R 중복 두뇌 경로와 기준선 감사
Phase 1: Research Brain 단일 실행 경로 통합
Phase 2: 연구 JSONL case 단위 의미 컴파일러 구현
...

규칙:

- Phase별 unit test 통과 후 커밋
- 전체 integration test는 주요 Phase마다 실행
- 최종 full test 전에 report-only PASS commit 금지
- 최종 HEAD에서 working tree clean
- 모든 commit SHA를 final report에 기록

## 2.4 실패 시 행동

Phase 또는 end-to-end 실행이 실패하면:

실패
→ failure cluster 생성
→ 가장 많은 실패를 만드는 root cause file/function 식별
→ 코드/schema/prompt/source recipe 패치
→ focused unit test
→ 같은 frozen replay/current run 재실행
→ conversion funnel before/after 비교

다음을 금지한다.

실패 → report에 NOT_READY 쓰고 Goal 완료
실패 → 같은 query 그대로 재실행
실패 → threshold 완화
실패 → 특정 종목 예외

외부 API/유료 source/네트워크 장애만 `EXTERNAL_SOURCE_BLOCKER_NOT_READY`로 남길 수 있다.
그 경우에도 외부 blocker와 무관한 모든 코드 Phase는 끝까지 완료한다.

---

# 3. Phase 0 — 현재 결과 재분류와 안전한 기준선

현재 Goal4 산출물을 삭제하지 않되 의미를 정확히 낮춘다.

현재 공식 상태는 다음과 같이 유지한다.

MEANINGFUL_RUNTIME_PARITY_NOT_READY

생성:

docs/operational/e2r_reconstruction_phase0_baseline.md
docs/operational/e2r_legacy_artifact_classification.json

분류:

- VALID_SAFETY_INFRASTRUCTURE
- VALID_DETERMINISTIC_SCORING_INFRASTRUCTURE
- PROVISIONAL_RESEARCH_MEMORY
- HEURISTIC_RESEARCH_REVERSE
- HEURISTIC_SOURCE_ROUTE
- REPORT_OR_PLAN_ONLY
- RUNTIME_PROOF
- DEPRECATED
- TEST_ONLY

Hard acceptance:

- 현재 11,394 research case count를 meaningful case count로 간주하지 않음
- 현재 1,855 source route pattern을 recovered route count로 간주하지 않음
- 111 task shell을 evidence count로 간주하지 않음
- current promoted full thesis 0개 상태를 정직하게 보존
- report label을 올리지 않음

---

# 4. Phase 1 — Research Brain 단일 Source of Truth 통합

현재 `src/e2r/research_brain`과 `src/e2r/research_reverse`, `src/e2r/source_routing`이 병렬로 존재한다.

`src/e2r/research_brain`을 canonical intelligence layer로 정한다.

구현 전략:

src/e2r/research_brain/
    corpus/
    compiler/
    recipes/
    retrieval/
    planning/
    replay/
    runtime/

기존:

src/e2r/research_reverse/**
src/e2r/source_routing/**

처리:

- production import 금지
- 새 canonical 구현으로 forward하는 compatibility adapter만 허용
- deprecation warning
- 새로운 schema를 복제하지 않음
- production reachable legacy count = 0

새 모듈 예:

src/e2r/research_brain/corpus/research_corpus_parser.py
src/e2r/research_brain/corpus/research_case_linker.py
src/e2r/research_brain/compiler/semantic_case_compiler.py
src/e2r/research_brain/compiler/source_verification_compiler.py
src/e2r/research_brain/recipes/evidence_recipe_compiler.py
src/e2r/research_brain/recipes/evidence_recipe_catalog.py
src/e2r/research_brain/retrieval/semantic_memory_index.py
src/e2r/research_brain/retrieval/balanced_case_retriever.py
src/e2r/research_brain/planning/two_pass_brain_planner.py
src/e2r/research_brain/runtime/adaptive_investigation_controller.py

공식 CLI:

python -m e2r.cli.compile_e2r_research_intelligence
python -m e2r.cli.run_e2r_historical_replay
python -m e2r.cli.run_e2r_current_operation
python -m e2r.cli.audit_e2r_evidence_intelligence

legacy CLI는 production-ready 라벨을 만들 수 없게 한다.

Hard acceptance:

- duplicate brain schema source of truth count = 1
- production reachable legacy research_reverse count = 0
- production reachable primitive-name route guesser count = 0
- old CLI pass-label capability count = 0
- all current tests migrated or adapter로 보존

Tests:

tests/test_research_brain_single_source_of_truth.py
tests/test_legacy_research_reverse_not_production_reachable.py
tests/test_legacy_source_route_not_production_reachable.py
tests/test_legacy_cli_cannot_claim_ready.py

---

# 5. Phase 2 — Research Corpus Semantic Compiler

기존 `research_case_extractor.py`의 다음 방식은 production에서 완전히 제거한다.

- text[:24000]
- 파일명/본문에서 archetype 문자열 탐색
- 첫 번째 6자리 symbol
- company_name=None
- trigger_date=None
- 파일 전체 URL을 case URL로 사용
- primitive 문자열 출현 여부로 positive/missing 결정
- 파일 하나를 archetype별 record 하나로 압축

## 5.1 Structured Row First

historical research MD는 다음 순서로 읽는다.

1. YAML front matter
2. fenced JSON
3. fenced JSONL
4. fenced CSV
5. Markdown table
6. narrative section
7. handoff prompt는 별도 metadata이며 case evidence로 읽지 않음

이미 machine-readable row가 있으면 해당 row가 source of truth다.
LLM으로 다시 추정하지 않는다.

## 5.2 새 canonical schema

HistoricalResearchArtifact, HistoricalResearchCase, HistoricalOutcome, HistoricalRuleCandidate를 구현한다.

HistoricalResearchCase에는 최소 다음 필드를 둔다.

- case_id
- artifact_id
- source_file
- source line range
- symbol
- company_name
- trigger_type
- trigger_date
- entry_date
- canonical/fine archetype
- large sector
- case role
- classification
- evidence family
- evidence URLs/summaries
- declared source quality
- positive/missing/counter evidence fields
- stage caps/hard breaks/false-positive patterns
- price metrics ref
- score simulation refs
- shadow rule refs
- transition refs
- runtime_score_eligible=false

HistoricalOutcome은 evaluator-only로 분리하고 runtime prompt에 노출하지 않는다.

## 5.3 Row Linking

다음을 실제 ID로 연결한다.

- case.case_id
- trigger.case_id / trigger_id
- score_simulation.case_id / trigger_id
- shadow_weight.trigger_ids / evidence_case_ids
- stage_transition_summary.symbol + entry_date
- residual_contribution.archetype
- source map rows

하나의 파일에 8개 case가 있으면 8개 HistoricalResearchCase를 만든다.
첫 symbol만 뽑지 않는다.

## 5.4 Narrative Fallback

machine-readable row가 없는 narrative만 LLM semantic compiler를 사용한다.

LLM은 case 후보·uncertainty·source span을 출력하고 score/stage는 계산하지 않는다.
LLM row는 `LLM_DERIVED_UNVERIFIED`로 quarantine review에 보낸다.

## 5.5 Quarantine

- malformed JSONL
- conflicting duplicate
- missing symbol/date
- URL-case association ambiguous
- inconsistent archetype
- outcome only
- handoff prompt accidental parsing

출력:

output/research_intelligence/corpus/historical_cases.jsonl
output/research_intelligence/corpus/historical_outcomes.jsonl
output/research_intelligence/corpus/historical_rules.jsonl
output/research_intelligence/corpus/quarantine.jsonl
output/research_intelligence/corpus/linkage_errors.jsonl

Hard acceptance:

- valid structured JSONL row preservation = 100%
- golden files case count exact
- present company_name loss = 0
- present trigger_date loss = 0
- first-symbol collapse = 0
- 24k truncation = 0
- handoff prompt parsed as case = 0
- duplicate conflict silent overwrite = 0

Golden corpus 최소:

- C06 URL-backed research
- C08 URL-backed research
- C15 URL-backed research
- C17 source-proxy research
- C24 source-proxy research
- C28 source-proxy research
- registry 전체 샘플

---

# 6. Phase 3 — Case-Level Source Verification Compiler

파일에 URL 하나가 있다고 case 전체가 A2가 되어서는 안 된다.

새 source state:

SOURCE_PROXY_ONLY
EVIDENCE_URL_PENDING
URL_PRESENT_UNVERIFIED
URL_FETCH_FAILED
URL_FETCHED_NO_ANCHOR
URL_FETCHED_WRONG_SUBJECT
URL_FETCHED_DATE_INVALID
URL_FETCHED_ANCHORED
URL_FETCHED_ANCHORED_CASE_MATCH
HISTORICAL_REPLAY_READY

A2/HISTORICAL_REPLAY_READY는 다음을 모두 만족해야 한다.

- URL 또는 official document id
- fetch 또는 valid provider snapshot
- content hash
- published date
- historical as-of 이전
- target/subject directness
- exact quote/table/API locator
- case/trigger와 의미적으로 연결
- evidence summary와 source가 모순되지 않음
- current score evidence와 분리

source_proxy/evidence_url_pending row는 URL repair queue로 보낸다.

Hard acceptance:

- case-level URL association 없는 A2 = 0
- URL string only A2 = 0
- wrong-subject replay fixture = 0
- source_proxy replay ready = 0
- 모든 URL-backed golden case는 replay ready 또는 exact blocker
- source proxy는 repair/planning only

---

# 7. Phase 4 — Executable Evidence Recipe OS

“primitive 이름을 source-backed하게 확인”하는 generic route를 폐기한다.

EvidenceRecipe는 최소 다음을 포함한다.

- archetype/primitive/role
- economic mechanism
- question to answer
- accepted claim predicates
- required entities/values/units/time
- required target directness/current lifecycle
- preferred source families/document types/sections
- discovery source
- forbidden score source
- positive examples
- counterexamples
- wrong-subject examples
- source success/failure examples
- rejection conditions
- counter/supersession questions
- query intent constraints
- stop/source-exhaustion conditions
- supporting case IDs

C06, C08, C15, C17, C24, C28의 세밀한 판례를 반영한다.

recipe는 Evidence Contract + historical case + verified source success/failure를 결합해서 만든다.
primitive 이름 substring으로 route를 결정하지 않는다.

Hard acceptance:

- registry 모든 required primitive에 recipe 또는 explicit unsupported reason
- URL-backed case recipe example 비어 있지 않음
- source proxy example planning-only
- generic query-only recipe = 0
- primitive substring production routing = 0
- acceptance/rejection/counter/lifecycle 누락 = 0

---

# 8. Phase 5 — Semantic Memory Graph와 Retrieval

ResearchMemoryGraph node/edge를 구현한다.

Node:

- case
- recipe
- primitive
- archetype
- source
- positive/counter/hard-break/source-success/source-failure

Edge:

- SUPPORTS
- COUNTERS
- CAPS
- REQUIRES
- BEST_FOUND_IN
- FAILED_IN
- SUPERSEDES
- WRONG_SUBJECT_EXAMPLE
- SAME_MECHANISM

retrieval은 first-N이나 memory count 우선이 아니라 다음을 균형 있게 반환한다.

- positive
- counterexample/guard
- source success
- source failure
- semantic guard
- direct recipe

historical MFE/MAE는 planner에서 숨긴다.

Acceptance:

- top-3 archetype retrieval hit >= 95%
- required recipe hit >= 95%
- positive+guard pair >= 90%
- future leakage = 0
- first-N-only retrieval = 0
- popularity bias critical = 0

---

# 9. Phase 6 — Two-Pass LLM Research Brain

Pass A는 source_primary/archetype label/score/Stage/outcome을 보지 않고 current evidence만으로 top-k hypothesis를 만든다.

Pass B에서 balanced memory와 recipes를 이용해 critique한다.

출력:

- top-k archetype
- supporting/contradicting current facts
- positive thesis
- counter thesis
- must-verify questions
- red-team questions
- source task drafts
- do-not-promote
- abstention/ambiguity

코드는 다음을 검증한다.

- score/stage output 없음
- source-primary copy 없음
- target/sector plausibility
- recipe coverage
- official-first/budget
- outcome leakage
- unsupported ambiguity abstention

Acceptance:

- planner score/stage mutation = 0
- source-primary copy without reason = 0
- ambiguous abstention 지원
- blind top-3 >= 95%
- top-1 >= 85%
- critical guard misroute = 0
- impossible archetype assignment = 0
- prompt/response hash 보존
- provider failure는 PlannerPending

---

# 10. Phase 7 — Question-Centric SourceTask

SourceTask는 단순 primitive label이 아니라 실제 질문과 성공조건을 가진다.

필수 필드:

- recipe_id
- question_to_answer
- why_material
- accepted predicates
- entities/values/time scope
- counter questions
- rejection conditions
- source/document/section
- discovery/forbidden source
- LLM query intent
- bounded budgets
- stop/exhaustion condition

literal query는 LLM이 current context를 보고 생성하고 code가 검증한다.

Acceptance:

- empty question = 0
- empty accepted predicate = 0
- empty rejection condition = 0
- generic verify-primitive task = 0
- official-first violation = 0
- FCF/contract/backlog Naver-first = 0
- unbounded query/fetch = 0

---

# 11. Phase 8 — Source Acquisition와 Document Selection

모드:

- PRODUCTION_BOUNDED
- HISTORICAL_REPLAY
- SOURCE_REPAIR_BACKFILL
- CONTROLLED_SMOKE

공식 source 우선 후 public report/industry/TrustedNews/Naver discovery를 사용한다.

Naver/Web:

- discovery only
- full article fetch
- original source
- snippet score 금지
- repost/wrong-subject guard

recipe에 맞는 문서 섹션을 선택한다.

Acceptance:

- snapshot-as-live = 0
- snippet-as-document = 0
- no content hash fetched = 0
- provider failure masked = 0
- source class/document mismatch = 0
- report replay counted real fetch = 0
- docs linked to task/recipe
- Naver result has full fetch or rejection

---

# 12. Phase 9 — Contract-Blind Claim Compiler

Raw extractor는 target identity, as-of, source document만 보고 assertion을 뽑는다.

primitive gap, desired archetype, score, Stage, historical outcome을 보지 않는다.

순서:

Anchor
→ Entity/subject
→ Target directness
→ Temporal/effective period
→ Lifecycle
→ Contradiction/supersession
→ Recipe/primitive mapping
→ Score eligibility

SourceTask satisfaction을 분리한다.

- DIRECT_TASK_SATISFIED
- REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN
- BASELINE_CLAIM_REUSED
- LIFECYCLE_REFRESH_ONLY
- COUNTER_CLAIM_FOUND
- NO_RELEVANT_CLAIM
- WRONG_SUBJECT
- STALE_ONLY
- PROVIDER_FAILED
- SOURCE_EXHAUSTED

rerouted claim은 ledger에는 넣되 원래 gap을 닫지 않는다.

Hard acceptance:

- accepted claim missing anchor/source/date/subject/target = 0
- source proxy current claim = 0
- wrong subject score = 0
- old unknown risk penalty = 0
- rerouted original gap closure = 0
- unstructured rule fallback score = 0
- recipe mapping 없는 score claim = 0
- parser mention direct score = 0

---

# 13. Phase 10 — Adaptive Investigation Controller

실패 이유별 next action을 만든다.

- NO_DOCUMENT_FOUND
- WRONG_SUBJECT
- STALE_ONLY
- GENERIC_CONTEXT_ONLY
- REROUTED_PRIMITIVE
- MAPPING_REJECTED
- CONTRADICTION_OPEN
- PROVIDER_FAILED
- SOURCE_EXHAUSTED

각 failure는 query/source/document/target constraint를 다르게 바꾼다.

동일 query 재실행을 금지한다.

Runtime adaptive investigation과 coding-agent systemic repair를 분리한다.

`until_pass`라는 이름으로 단순 rerun을 self-repair라고 부르지 않는다.

Acceptance:

- failure reason 없는 retry = 0
- identical retry = 0
- rerouted feedback 반영
- rejection → next action trace
- material unresolved → score_valid false
- round limit → pending
- systemic failure cluster와 code repair history 존재

---

# 14. Phase 11 — Historical Replay와 Current Operation 분리

Historical Replay:

- 전 registry 아키타입 system parity 검증
- frozen as-of
- positive/guard/wrong-subject/old-risk/source-missing
- outcome/expected stage/archetype는 prompt에서 숨김

Current Operation:

- 현재 evidence가 있는 후보만
- archetype quota 강제 금지
- current claim만 score

Historical acceptance:

- registry 100%
- each archetype parity row
- NOT_ATTEMPTED without reason = 0
- URL-backed replay or blocker
- critical guards 100%
- source proxy score 0
- top-3 >=95%, top-1 >=85%
- mapping precision >=95%
- positive recall >=90%
- guard accuracy >=95%
- future leakage 0

Current acceptance:

- full-universe baseline
- real trigger pool
- bounded selective deep
- each deep candidate ends in:
  full thesis / disproved / source pending / provider pending / budget pending
- current market에 없는 archetype은 row가 없어도 정상

---

# 15. Phase 12 — Deterministic Score/Stage 재검증

점수 종류:

- EVENT_EVIDENCE_PARTIAL
- FULL_E2R_100
- NO_SCORE

full score는 material primitive assessment와 accepted current claims, contradiction resolution, score_valid, StageCourt trace가 있어야 한다.

한 AtomicStageDecision에서 stage/score/status/claims/contributions/trace/risk/missing gaps를 가져온다.

score delta는 claim/config 변경으로 설명한다.

hard break는 target-direct, current OPEN, source-backed, material, unresolved 조건을 모두 만족해야 한다.

Acceptance:

- claimless score = 0
- material gap full score = 0
- event score as full = 0
- stage/score/trace mismatch = 0
- pending final low score = 0
- hard break without current direct OPEN = 0
- unexplained score delta = 0
- fingerprint mismatch concealed = 0

---

# 16. Phase 13 — Census / Daily Operation

전 종목:

Universe
→ official/price/risk/existing-ledger baseline
→ SourceTimeline
→ LastEffectiveThesis
→ DepthPolicy
→ selected deep
→ CensusStageStatus

최근 lookback을 Stage cutoff로 쓰지 않는다.

모든 종목에 LLM/Naver를 돌리지 않는다.

- L0/L1 전 종목
- L2 official light
- L3 Brain
- L4 acquisition
- L5 full thesis

Daily trigger는 official/earnings/IR/report/news/market/risk/existing ledger를 포함한다.
시장·뉴스는 trigger이지 score evidence가 아니다.

Watchlist는 score type, confidence, claims, missing conditions, gaps, next action을 보여준다.

---

# 17. Phase 14 — Conversion Funnel Observability

다음을 archetype/candidate별로 기록한다.

candidate
→ hypothesis
→ retrieval
→ recipe
→ source task
→ query
→ result
→ fetched doc
→ relevant doc
→ assertion
→ claim
→ primitive
→ score
→ full thesis/pending/disproved

핵심 지표:

- relevant document rate
- accepted claim rate
- original-gap direct closure
- rerouted claim
- mapping rejection
- full thesis
- pending reason
- cost/runtime

task shell 수를 progress로 말하지 않는다.
accepted claim 총량보다 direct original-gap closure를 우선한다.
leaf artifact에서 독립 재계산한다.

---

# 18. Phase 15 — Known-Bad Suite

반드시 잡아야 할 것:

- file-level case collapse
- first symbol extraction
- company/date loss
- one URL whole-file A2
- handoff prompt as case
- source proxy promoted
- C05 context copy
- product profile as order
- HBM keyword positive
- security keyword ARR
- commodity headline margin
- snippet score
- wrong subject
- customer CAPA as target CAPA
- industry demand as issuer order
- financial contract as commercial contract
- stale risk penalty
- rerouted gap closure
- provider failure Red
- replay as real fetch
- event score full score
- stage/trace mismatch
- historical outcome leakage
- historical replay current watchlist contamination
- forced current archetype materialization

---

# 19. Phase 16 — Test / Runtime Commands

Full tests:

PYTHONPATH=src python -m unittest discover -s tests -v

Compile:

PYTHONPATH=src python -m e2r.cli.compile_e2r_research_intelligence \
  --repo-root . \
  --output-root output/research_intelligence/v1 \
  --strict true

Replay:

PYTHONPATH=src python -m e2r.cli.run_e2r_historical_replay \
  --registry canonical \
  --mode blind_frozen_replay \
  --output-root output/historical_replay/v1 \
  --fail-on-critical true

Current:

PYTHONPATH=src python -m e2r.cli.run_e2r_current_operation \
  --as-of-date <current as-of> \
  --mode production_bounded \
  --universe krx \
  --output-root output/current_operation/v1 \
  --fail-on-critical true

Census:

PYTHONPATH=src python -m e2r.cli.run_e2r_census_mode \
  --as-of-date <current as-of> \
  --mode census_selective_deep \
  --brain canonical_v1 \
  --output-root output/census_v_next \
  --fail-on-critical true

각 실행은 commit/config/corpus/memory/recipe/prompt/source hash와 dirty status를 남긴다.

---

# 20. 완료 라벨

필수 단계:

- UNIFIED_RESEARCH_BRAIN_ARCHITECTURE_PASS
- RESEARCH_CORPUS_SEMANTIC_COMPILER_PASS
- CASE_LEVEL_SOURCE_VERIFICATION_PASS
- EVIDENCE_RECIPE_OS_PASS
- SEMANTIC_RESEARCH_BRAIN_PASS
- ADAPTIVE_EVIDENCE_CLOSURE_PASS
- HISTORICAL_REPLAY_PARITY_PASS
- CURRENT_OPERATIONAL_BRAIN_PASS

최종:

MEANINGFUL_E2R_RUNTIME_READY

외부 blocker:

EXTERNAL_SOURCE_BLOCKER_NOT_READY

외부 blocker가 있어도 내부 코드 Phase를 생략하지 않는다.

---

# 21. 절대 완료가 아닌 상태

- report 문구만 READY
- research case count만 증가
- MemoryCard 수만 증가
- Source Route pattern 수만 증가
- task shell만 증가
- 동일 query rerun
- rerouted claim 원래 gap closure
- full thesis 0인데 준비 완료
- replay/current 혼합
- current archetype quota 강제
- source proxy score
- `until_pass` runtime retry만 수행
- known-bad 통과
- leaf artifact 없는 summary
- legacy Brain production reachable
- threshold/weight 변경

---

# 22. 최종 독립 감사

Reviewer A: Corpus Fidelity  
Reviewer B: Recipe/Retrieval  
Reviewer C: Source/Claim Realness  
Reviewer D: Score/Stage Integrity  
Reviewer E: Historical/Current Separation

각 reviewer는 report generator counters를 공유하지 않고 leaf artifacts를 읽는다.
critical 1개면 FAIL이다.

---

# 23. 최종 응답 형식

1. Final status
2. Phase별 commit/push/worktree
3. Full tests와 known-bad
4. Architecture 통합
5. Corpus compiler 수치
6. Source verification
7. Recipe coverage
8. Retrieval/Brain benchmark
9. Source/Claim closure
10. Historical replay
11. Current operation
12. Conversion funnel before/after
13. Systemic root causes repaired
14. Reviewer A~E
15. Final verdict와 blockers

---

# 24. 마지막 완료 명령

이번 작업의 성공은 문서 수, MemoryCard 수, SourceTask 수, 테스트 개수로 판단하지 않는다.

성공은 다음 사슬이 닫힐 때만 인정한다.

historical structured case
→ verified case-level memory
→ executable evidence recipe
→ balanced semantic retrieval
→ LLM investigation plan
→ question-specific SourceTask
→ real fetched source
→ direct current claim
→ primitive closure
→ deterministic score
→ StageCourt

전 아키타입 이해 여부는 historical blind replay로 검증한다.

현재 좋은 종목 판단은 current operation에서 실제 current evidence가 있는 후보만 평가한다.

실패하면 report에 남기고 끝내지 마라.
가장 큰 failure cluster의 root cause를 코드에서 수정하고,
같은 frozen replay와 current operation을 다시 실행하고,
conversion funnel이 실제로 개선될 때까지 반복하라.

scoring weights와 Stage threshold는 건드리지 마라.

최종적으로 `MEANINGFUL_E2R_RUNTIME_READY`가 아니면 Goal 완료라고 말하지 마라.
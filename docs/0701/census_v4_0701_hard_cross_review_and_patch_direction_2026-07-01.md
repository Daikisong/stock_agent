# Census v4 Hard Cross Review And Patch Direction - 2026-07-01

작성 목적:

```text
사용자 질문:
  뭔가 잘못되고 있는 거 맞지?
  stage가 있는 애들이 있긴 해?
  다음 에이전트가 빡세게 리뷰할 수 있게 0701에 완벽하게 문서화해라.
```

이 문서는 현재 산출물, 코드 경로, 남은 병목을 한 번 더 교차검증해
다음 패치 방향을 고정한다.

## 0. 최종 결론

짧게 말하면:

```text
Stage가 있는 종목은 있다.
하지만 지금 있는 Stage는 full thesis 운영 Stage가 아니다.
```

현재 `output/census_v4/2026-07-01`의 Stage는 전부 아래 범위다.

```text
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
full_thesis_stage = FULL_THESIS_NOT_RUN
verified_score = null
full_e2r_verified_score = null
```

쉬운 예:

```text
지금 Stage0/Stage1/Stage2-Watch는 병원 접수/문진 상태판이다.
삼성전자 HBM thesis를 100점 만점으로 다 채점한 최종 진단서가 아니다.
```

따라서 현재 문장은 이렇게 써야 맞다.

```text
맞는 말:
  3,391개 종목에 Census event-board 상태가 붙어 있다.
  그중 85개는 Stage0이 아닌 event-board label이다.
  67개는 source-backed event partial score row다.

틀린 말:
  85개 종목의 full E2R thesis Stage가 끝났다.
  삼성전자/하이닉스 HBM/C06 운영 점수가 나왔다.
  Brain/Web LLM evidence pass가 됐다.
```

## 1. 현재 산출물 검산값

검산 기준:

```text
output/census_v4/2026-07-01
```

사용한 명령:

```bash
wc -l \
  output/census_v4/2026-07-01/census_stage_status.jsonl \
  output/census_v4/2026-07-01/accepted_claims.jsonl \
  output/census_v4/2026-07-01/score_contributions.jsonl \
  output/census_v4/2026-07-01/stagecourt_traces.jsonl \
  output/census_v4/2026-07-01/planner_runs.jsonl \
  output/census_v4/2026-07-01/web_search_tasks.jsonl \
  output/census_v4/2026-07-01/web_search_results.jsonl \
  output/census_v4/2026-07-01/web_fetched_documents.jsonl \
  output/census_v4/2026-07-01/claim_extractor_runs.jsonl
```

결과:

```text
census_stage_status.jsonl: 3391
accepted_claims.jsonl:       92
score_contributions.jsonl:   92
stagecourt_traces.jsonl:     92
planner_runs.jsonl:           0
web_search_tasks.jsonl:       0
web_search_results.jsonl:     0
web_fetched_documents.jsonl:  0
claim_extractor_runs.jsonl:   0
```

`jq`는 로컬에 없어서 JSONL 분포는 파이썬 read-only 집계로 확인했다.

```text
base_stage:
  Stage0:       3306
  Stage1:         54
  Stage2-Watch:   30
  Red:             1

canonical_stage:
  0:       3306
  1:         54
  2:         30
  3-Red:      1

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391

stage_scope:
  CENSUS_EVENT_BOARD: 3391

score_scale:
  NO_SCORE:                 3324
  EVENT_WEIGHTED_PARTIAL:     67

operator_stage_use:
  NOT_FULL_THESIS_STAGE: 3391

verified_score_present:          0
full_e2r_verified_score_present: 0
```

해석:

```text
Stage label은 있다.
운영 thesis 점수는 없다.
```

## 2. Readiness / Goal 교차검증

`readiness_verdict.json` 핵심:

```text
verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
brain_web_mode: disabled
brain_web_evidence_pass: false
meaningful_operational_stage_pass: false
full_thesis_smoke_pass: false
```

`goal_completion_audit.json` 핵심:

```text
goal_completion_ready: false
blockers:
  - brain_web_evidence_pass_false
  - full_thesis_smoke_pending
```

`brain_web_readiness_gate_audit.json` 핵심:

```text
verdict: NOT_REQUESTED
brain_web_mode: disabled
llm_planner_call_count: 0
source_task_execution_count: 0
web_search_task_count: 0
web_fetched_document_count: 0
llm_claim_extractor_attempt_count: 0
web_or_llm_accepted_claim_count: 0
brain_web_evidence_pass_allowed: false
```

`web_naver_acquisition_audit.json` 핵심:

```text
verdict: DISABLED_HONESTY_PASS
pass_scope: disabled_honesty
web_search_task_count: 0
web_search_result_count: 0
web_fetched_document_count: 0
```

주의:

```text
DISABLED_HONESTY_PASS는 "안 했는데 했다고 거짓말하지 않았다"는 뜻이다.
"web/Naver로 원문을 가져와 점수에 반영했다"는 뜻이 아니다.
```

쉬운 예:

```text
배달앱에서 "주문 안 함"이라고 정확히 표시한 상태다.
"음식 배달 완료"가 아니다.
```

## 3. 삼성전자 / 하이닉스 현재 상태

`samsung_hynix_full_thesis_smoke.json`과 audit 기준:

```text
full_thesis_status: PENDING_FULL_THESIS_REFRESH
daily_event_and_full_thesis_separated: true
```

SK하이닉스:

```text
symbol: 000660
base_stage: Stage1
canonical_stage: 1
daily_event_score_contribution_ids: 1개
full_thesis_claim_ids: []
full_thesis_score_contribution_ids: []
full_thesis_stagecourt_trace_ids: []
blocking_reason: full_thesis_source_tasks_planned_but_not_executed
```

삼성전자:

```text
symbol: 005930
base_stage: Stage1
canonical_stage: 1
full_thesis_claim_ids: []
full_thesis_score_contribution_ids: []
full_thesis_stagecourt_trace_ids: []
blocking_reason: full_thesis_source_tasks_planned_but_not_executed
```

둘 다 빠진 full thesis primitive:

```text
named_customer_or_customer_quality
qualification_status
capacity_allocation_or_pre_sold
hbm_shipment_or_revenue_mix
cash_or_revision_conversion
repeat_evidence_family
source_quorum
```

해석:

```text
삼성전자/하이닉스에 Stage1 label은 있다.
하지만 이것은 daily event-board label이다.
HBM/C06 전체 thesis 점수와 Green/Yellow 판정은 아직 실행되지 않았다.
```

## 4. accepted_claims 92개와 partial score 67개의 의미

현재 대표 산출물에는:

```text
accepted_claims.jsonl:     92
score_contributions.jsonl: 92
stagecourt_traces.jsonl:   92
```

하지만 `census_stage_status.jsonl`의 대표 partial score row는 67개다.

이 차이는 full thesis 누락이 아니라,
대표 row에 반영하지 않은 non-representative claim과 semantic guard 차단 row가 있기 때문이다.

쉬운 예:

```text
채점지가 92장 있지만,
성적표 대표 행에 들어간 것은 67장이다.
나머지는 보관은 됐지만 최종 대표 점수로 누수되면 안 되는 장부다.
```

대표 row에 들어간 67개도 full thesis가 아니다.

```text
score_scale = EVENT_WEIGHTED_PARTIAL
full_e2r_verified_score = null
```

## 5. 코드 교차검증: Stage 과장 방지

대표 row에는 Stage 범위 분리 필드가 들어간다.

관련 코드:

```text
src/e2r/census/census_runner_v4.py
  stage_scope 기본값: CENSUS_EVENT_BOARD
  full_thesis_stage 기본값: FULL_THESIS_NOT_RUN
  operator_stage_use 계산
```

확인 포인트:

```text
Stage label이 있어도 stage_scope가 FULL_THESIS가 아니면 운영 thesis Stage가 아니다.
operator_stage_use가 NOT_FULL_THESIS_STAGE이면 UI/리포트에서 운영 Stage처럼 쓰면 안 된다.
```

이 guard는 방향이 맞다.
다음 패치에서도 제거하면 안 된다.

## 6. 코드 교차검증: live_full_bounded web leaf

`src/e2r/research_brain/v4_source_acquisition_runner.py`에는 최근 패치로
아래 흐름이 생겼다.

```text
task.query_intents
-> target-scoped query 검증
-> external web/Naver/trusted news 요청 여부 확인
-> bounded search/fetch
-> web_search_tasks/results/fetched/rejected leaf 생성
```

중요 guard:

```text
회사명/티커 없는 query:
  web_query_not_target_scoped 로 reject

official로 풀어야 하는 gap:
  official_solvable_gap_sent_to_general_web 로 reject

FCF gap을 news/web으로 보내는 경우:
  fcf_gap_sent_to_news_or_general_web 로 reject
```

이 패치는 필요하고 방향도 맞다.

다만 현재 canonical output은 Brain/Web disabled run이라:

```text
web_search_tasks.jsonl: 0
web_search_results.jsonl: 0
web_fetched_documents.jsonl: 0
```

즉 코드 능력과 canonical 산출물은 분리해서 말해야 한다.

## 7. 코드 교차검증: 가장 큰 병목은 unstructured claim extraction

`src/e2r/research_brain/v4_evidence_extraction_bridge.py`의 현재 핵심 흐름:

```text
execute_source_tasks_with_evidence_os_v4()
-> SourceAcquisitionRunnerV4.acquire()
-> documents / anchors 수집
-> _append_claims_for_task()
-> _extract_signals()
-> RawAssertion
-> AdjudicatedClaim
-> PrimitiveMappingProposal
-> derive_score_eligibility()
```

병목:

```python
normalized = anchor.normalized_value if isinstance(anchor.normalized_value, Mapping) else {}
row = normalized.get("row") if isinstance(normalized.get("row"), Mapping) else {}
if not row:
    return ()
```

즉 `_extract_signals()`는 현재 구조화 row가 없으면 signal을 만들지 않는다.

영향:

```text
web/news/IR/report 원문이 fetch되어 EvidenceDocument와 EvidenceAnchor가 생겨도,
anchor.normalized_value["row"]가 없으면 accepted claim까지 못 간다.
```

쉬운 예:

```text
택배 상자는 도착했는데, 상자를 열어 물건명/수량을 적는 사람이 없다.
그래서 창고 장부에는 "상자 도착"만 있고, 채점표 칸에는 아무것도 못 쓴다.
```

따라서 다음 큰 패치는 web fetch가 아니라:

```text
unstructured text
-> contract-blind assertion extraction
-> target/temporal adjudication
-> primitive mapping
-> eligibility guard
-> score contribution
-> StageCourt
```

이다.

## 8. `contract_blind_extractor` 현재 상태

`src/e2r/production/claim_extraction/contract_blind_extractor.py`는
방향은 맞는 구조를 이미 갖고 있다.

좋은 점:

```text
score/stage/current_score_eligible/verified/source_tier/primitive_gap 같은 금지 context를 차단한다.
RawAssertionRecord는 subject/predicate/object/polarity/modality/date/quote만 담는다.
점수 eligibility를 LLM/extractor가 결정하지 않는다.
```

하지만 현재 구현은 LLM provider가 아니라 제한적인 문장/키워드 기반 추출기다.

위험:

```text
감사의견, 계약, 수주, EPS, FCF 같은 predicate 감지는 아직 token 기반이다.
이걸 그대로 운영 핵심으로 쓰면 또 "키워드 -> 점수" 냄새가 난다.
```

정확한 다음 방향:

```text
이 파일의 schema와 금지 context guard는 살린다.
하지만 실제 extractor는 LLM provider 호출로 확장해야 한다.
LLM은 primitive/score/gap을 보지 않고 원문 claim만 작성해야 한다.
코드는 exact quote/span, 날짜, 주체, 현재성, mapping, eligibility를 검증한다.
```

쉬운 예:

```text
나쁜 방식:
  "감사의견" 글자가 있으면 accounting_trust_break.

좋은 방식:
  LLM이 "월덱스 감사의견은 적정"이라는 raw assertion을 만든다.
  Adjudicator가 subject=월덱스, target=삼성전자, polarity=NORMAL로 판정한다.
  Mapper가 accounting_trust_break를 reject한다.
  점수는 0이다.
```

## 9. `primitive_mapper` 현재 상태

`src/e2r/production/claim_extraction/primitive_mapper.py`는
extractor와 mapper를 분리한 점은 맞다.

좋은 guard:

```text
audit_or_accounting_claim AND polarity != NEGATIVE
-> accounting_trust_break reject
```

시설투자 정정 guard도 있다.

```text
기재정정/정정신고/종료일 연장/연기/취소
-> positive capacity로 매핑하지 않음
```

하지만 mapper의 predicate-to-primitive map은 아직 좁고 정적이다.

다음 방향:

```text
아키타입별 Evidence Contract v2 registry에서 allowed primitives와 mapping rubric을 로드한다.
코드에 종목별 예외를 넣지 않는다.
LLM extractor가 primitive를 직접 확정하지 않는다.
Primitive Mapper가 accepted/rejected rationale을 leaf로 남긴다.
```

## 10. 다음 패치 우선순위

### P0. 산출물 표현 동결

절대 건드리면 안 되는 guard:

```text
stage_scope
score_scope
operator_stage_use
operator_score_use
full_thesis_stage
verified_score / event_evidence_score / full_e2r_verified_score 분리
Brain/Web disabled는 NOT_REQUESTED
```

이 guard가 있어야 "안 했는데 했다"는 거짓 완료를 막는다.

### P1. canonical output과 latest code 차이 명시

현재 code에는 web leaf patch가 들어갔지만 canonical output은 disabled run이다.

다음 에이전트는 반드시 둘을 분리해야 한다.

```text
code capability:
  target-scoped web query/fetch leaf 가능

current canonical artifact:
  web leaf 0개
```

### P2. contract-blind LLM Claim Extractor Provider 추가

요구사항:

```text
입력:
  target entity identity/aliases
  as_of_date
  document text
  document metadata

금지 입력:
  score
  stage
  primitive_gap
  missing_primitive
  green gate
  target score
  현재 점수 부족분
```

출력:

```text
raw assertions only:
  subject
  predicate
  object/value
  polarity proposal
  modality
  event date/effective period
  exact quote
  related entities
```

금지 출력 신뢰:

```text
verified
current_score_eligible
source_tier
final primitive
final score
final stage
```

`claim_extractor_runs.jsonl`에는 반드시 다음을 남긴다.

```text
run_id
provider/model
prompt_hash
document_id
anchor_id
input_context_keys
forbidden_context_seen
raw_assertion_ids
accepted_count
rejected_count
provider_error
```

### P3. Evidence bridge에 unstructured text branch 추가

현재 `_extract_signals()`가 `normalized_value["row"]`만 본다.

다음 구조로 바꿔야 한다.

```text
if structured row exists:
  기존 structured extraction 유지
else if anchor_type == TEXT_SPAN and document_text exists:
  contract-blind extractor 실행
  RawAssertionRecord -> RawAssertion adapter
  target/temporal adjudicator
  primitive mapper
  eligibility guard
else:
  mention_only
```

주의:

```text
LLM extractor가 만든 assertion이 곧 점수는 아니다.
exact quote가 원문에 실제로 있어야 한다.
subject가 target 직접이어야 한다.
as_of_date 이후 자료는 막아야 한다.
current/open lifecycle이 아니면 score-ineligible이다.
```

### P4. Adjudicator와 mapper를 hardcoded score path로 만들지 말 것

허용되는 deterministic code:

```text
quote/span 검증
날짜 검증
target entity/directness 검증
source anchor 검증
future leakage 차단
Evidence Contract allowed primitive 검증
score eligibility 파생
```

금지되는 deterministic code:

```text
종목명 예외
아키타입별 검색어 하드코딩
키워드 하나로 risk/score 확정
LLM이 못 찾았다고 0점 확정
provider failure를 낮은 점수로 확정
```

### P5. full thesis smoke는 source task 실행까지 가야 한다

현재 삼성전자/하이닉스 full thesis task는 planning-only다.

다음 목표:

```text
full_thesis_source_tasks
-> bounded official-first execution
-> web/news fallback if allowed
-> fetched documents
-> LLM raw assertions
-> accepted/rejected claim ledger
-> score contribution
-> StageCourt trace
-> full_thesis_stage or material pending
```

결과가 Green이어야 한다는 뜻이 아니다.

정확한 성공 기준:

```text
Green/Yellow/Stage2/4B/Red 중 무엇이든,
claim-backed로 설명되거나
material source gap 때문에 pending이어야 한다.
```

### P6. Brain/Web strict promotion

Brain/Web Stage가 대표 `census_stage_status.jsonl`로 승격되려면
아래가 모두 필요하다.

```text
real planner provider success > 0
source task executions > 0
real fetched documents > 0
LLM/extractor attempts > 0
accepted Brain/Web claims > 0
claim-backed score contributions > 0
StageCourt traces > 0
brain_to_claim_trace 연결
snapshot:// promoted evidence 0
fake provider 0
provider failure final score 0
strict promotion verdict = PROMOTION_APPLIED
```

하나라도 빠지면:

```text
NOT_READY / BLOCKED / PENDING
```

이지 낮은 점수 확정이 아니다.

## 11. 다음 에이전트 공격 질문

다음 에이전트는 아래를 먼저 공격해야 한다.

```text
1. Stage label 85개를 full thesis로 오해할 여지가 아직 남아 있는가?
2. canonical output이 latest code capability를 과장하고 있지 않은가?
3. web_search_tasks만 있어도 REAL_ACQUISITION_PASS가 되는 우회가 남아 있는가?
4. web_fetched_documents가 있어도 accepted claim 없이 score/stage가 올라가는 길이 있는가?
5. claim_extractor_runs 없이 Brain/Web evidence pass가 가능한가?
6. LLM extractor가 primitive_gap/score_gap_context를 볼 수 있는가?
7. LLM 출력의 verified/current_score_eligible/source_tier를 신뢰하는 코드가 있는가?
8. old/historical risk가 current risk로 들어갈 수 있는가?
9. wrong subject claim이 direct target으로 들어갈 수 있는가?
10. provider failure가 final low score로 굳는 길이 있는가?
11. 삼성전자/하이닉스 full thesis task가 planning-only인데 Stage가 나온 것처럼 보이는가?
12. accepted_claims 92개와 representative partial score 67개의 차이가 누수 없이 설명되는가?
```

## 12. 금지 문장

아래 문장은 현재 상태에서는 쓰면 안 된다.

```text
Census v4가 운영 Stage를 완성했다.
삼성전자와 하이닉스 full thesis Stage가 나왔다.
Brain/Web evidence pass가 됐다.
web/Naver 원문이 canonical run에 반영됐다.
4948개 테스트가 통과했으니 goal.md 완료다.
accepted_claims 92개가 full thesis 92개라는 뜻이다.
Stage2-Watch 30개가 운영 Stage2 후보 확정이라는 뜻이다.
Red 1개가 4C thesis break라는 뜻이다.
```

허용 문장:

```text
Census v4는 anti-fake full-universe 상태판은 통과했다.
Stage label은 있으나 full thesis Stage는 전부 not-run이다.
Brain/Web disabled run은 NOT_REQUESTED로 정직하게 표시된다.
web leaf code path는 생겼지만 canonical output에는 아직 web leaf가 없다.
다음 핵심 패치는 unstructured text -> contract-blind LLM assertion -> adjudication/mapping/eligibility bridge다.
```

## 13. 패치 성공 기준

다음 패치가 끝났다고 말하려면 최소 이 조건을 만족해야 한다.

```text
1. claim_extractor_runs.jsonl > 0
2. extractor input에 forbidden context 0
3. web/news/IR/report fetched doc에서 RawAssertion 생성
4. exact quote/span 검증 실패 claim은 rejected
5. wrong subject claim은 rejected
6. normal audit opinion은 accounting_trust_break rejected
7. old/historical unresolved risk는 current score 0 또는 follow-up
8. accepted Brain/Web claim -> contribution -> StageCourt -> brain_to_claim_trace 연결
9. promoted row가 있다면 stage_scope가 BRAIN_WEB_PARTIAL 또는 FULL_THESIS로 명시되고 strict gate PASS
10. provider failure/material gap은 낮은 점수 확정이 아니라 pending
11. 삼성전자/하이닉스 full thesis smoke가 planning-only에서 executed/pending truth state로 이동
12. 전체 테스트 통과
```

성공 예:

```text
삼성전자 HBM 문서를 fetch했다.
LLM extractor가 "삼성전자는 2026년 특정 고객 HBM 공급 qualification 관련 내용을 밝혔다" 같은 raw assertion을 만든다.
코드가 quote가 원문에 있는지 확인한다.
target=삼성전자, as_of_date 이전, current 여부를 판정한다.
mapper가 C06 primitive 중 qualification_status에 매핑한다.
source quorum/cash bridge가 부족하면 Green이 아니라 pending 또는 Stage2/Yellow로 남긴다.
그 이유가 claim ID와 missing primitive로 남는다.
```

실패 예:

```text
월덱스 기사에 "삼성전자"와 "감사의견 적정"이 같이 있다.
코드가 "감사의견" 키워드만 보고 삼성전자 accounting_trust_break로 넣는다.
이건 subject/polarity/target/current 모두 실패이므로 hard fail이다.
```

## 14. 현재 워킹트리 주의

현재 워킹트리는 깨끗하지 않다.

```text
수정/삭제/추가 파일이 많다.
docs/0701/은 untracked folder다.
src/e2r/census/census_runner_v4.py도 untracked로 보이는 상태에서 수정되어 있다.
```

다음 에이전트는 절대 임의로 reset/revert하면 안 된다.

```text
해야 할 일:
  필요한 파일만 읽고 이어서 패치한다.

하면 안 되는 일:
  git reset --hard
  git checkout -- .
  사용자 변경분 되돌리기
  아직 goal 미완료인데 한글 커밋/푸시
```

## 15. 한 줄 판정

현재 상태는:

```text
anti-fake 상태판으로는 의미가 있다.
운영 full thesis pipeline으로는 아직 미완성이다.
가장 큰 다음 병목은 원문을 LLM contract-blind raw assertion으로 바꾸는 Evidence OS extractor bridge다.
```


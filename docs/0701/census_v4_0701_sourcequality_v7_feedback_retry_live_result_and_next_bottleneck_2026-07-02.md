# Census v4 0701 Sourcequality v7 Feedback Retry Live Result / Next Bottleneck

작성 시점: 2026-07-02 KST

대상 실행:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v7
```

관련 패치:

```text
src/e2r/research_brain/v4_schemas.py
src/e2r/research_brain/v4_production_orchestrator.py
src/e2r/research_brain/v4_planner_runtime.py
tests/test_research_brain_v4_operational_modes.py
```

## 결론

```text
v7은 READY가 아니다.
하지만 병목은 v6보다 한 단계 뒤로 이동했다.
```

쉬운 예:

```text
v6:
  접수창구에 들어온 서류가 전부 전단지라서 문 앞에서 탈락했다.

v7:
  원문 서류 9개를 실제로 가져와 LLM이 읽었다.
  하지만 그 안의 claim이 target/direct/current/primitive 조건을 통과하지 못해 점수표에는 0개도 들어가지 못했다.
```

## v6 -> v7 핵심 변화

```text
metric                             v6      v7
verdict                            BLOCKED BLOCKED
brain_accepted_claim_count          1       0
official_accepted_claim_count       1       0
web_or_llm_accepted_claim_count     0       0
brain_stage_trace_count             1       0
brain_promoted_stage_row_count      0       0
web_search_task_count               2       7
web_search_result_count             11      50
web_fetched_document_count          0       9
web_rejected_document_count         11      24
llm_claim_extractor_attempt_count   0       9
planner_runs                        21      22
llm_prompts                         1       2
llm_responses                       1       2
```

해석:

```text
v6의 문제:
  좋은 web 원문을 못 가져와 extractor가 0회였다.

v7의 변화:
  web 원문 9개를 가져왔고 LLM extractor 9회가 성공했다.

v7의 남은 문제:
  accepted brain/web claim은 여전히 0개다.
```

## 이번 코드 패치가 닫은 것

### 1. source rejection feedback 경로

추가한 schema:

```text
PlannerRunV4.source_rejection_feedback_count
```

추가한 context:

```text
existing_evidence_summary.source_rejection_feedback
```

추가한 retry:

```text
_retry_planner_for_source_rejection_feedback(...)
```

추가한 helper:

```text
_source_rejection_feedback_from_bundle(...)
```

추가한 planner rule:

```text
If existing_evidence_summary.source_rejection_feedback is non-empty,
previous source candidates were rejected before extraction.
Do not repeat the same URL/source pattern.
```

목적:

```text
검색 결과가 전부 stock list, channel, archive, sitemap이면
코드가 새 query를 하드코딩하지 않고,
LLM planner에게 "이런 소스 패턴은 탈락했다"는 feedback을 넘긴다.
```

### 2. claim-level rejected feedback은 그대로 유지

v7 live run에서는 source rejection retry가 아니라 기존 claim-level retry가 관측됐다.

```text
planner_runs = 22
initial planner runs = 21
feedback_retry planner runs = 1
rejected_claim_feedback_item_count = 8
source_rejection_feedback_item_count = 0
```

이유:

```text
v7에서는 모든 source가 metadata 단계에서 탈락하지 않았다.
web full-source 문서 9개가 fetch됐고,
claim extractor 9회가 실행됐다.
따라서 "source 후보 전부 접수 전 탈락"이 아니라
"claim까지 만들었지만 점수 전 단계에서 탈락"한 상황이다.
```

쉬운 예:

```text
source rejection retry:
  시험지가 접수창구에 오기도 전에 전부 잘못된 서류였을 때.

rejected claim retry:
  시험지는 받았고 답도 읽었는데, 답이 문제 조건에 맞지 않았을 때.

v7은 두 번째다.
```

## v7 live artifact 증거

원본:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v7/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v7/planner_runs.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v7/web_fetched_documents.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v7/claim_extractor_runs.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v7/raw_assertion_rejections.jsonl
```

readiness:

```text
verdict = BLOCKED
brain_accepted_claim_count = 0
official_accepted_claim_count = 0
web_or_llm_accepted_claim_count = 0
brain_stage_trace_count = 0
brain_promoted_stage_row_count = 0
web_search_task_count = 7
web_search_result_count = 50
web_fetched_document_count = 9
web_rejected_document_count = 24
llm_claim_extractor_attempt_count = 9
source_task_execution_count = 7
```

blockers:

```text
Brain/Web accepted claim count is zero
web/LLM accepted claim count is zero
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
Brain/Web operational minimum planner runs not met: 22/30
Brain/Web operational minimum web search tasks not met: 7/20
Brain/Web operational minimum web/news search calls not met: 7/20
Brain/Web operational minimum fetched documents not met: 9/10
```

LLM extraction:

```text
llm_claim_extraction_audit = REAL_EXTRACTION_PASS
claim_extractor_runs = 9
provider_name = codex_cli_contract_blind_extractor
status = SUCCESS for 9 runs
```

중요:

```text
LLM extractor는 실제로 돌았다.
하지만 extractor success != accepted score claim 이다.
```

## v7에서 claim이 탈락한 이유

집계:

```text
raw_assertion_rejections = 56

rejection_reason:
  target_scope_or_directness_rejected = 38
  primitive_mapping_rejected = 18

target_scope_status:
  UNRELATED = 38
  DIRECT = 18

mapping_status:
  REJECTED = 56

mapped_primitive_id:
  volume_growth_visible = 54
  official_disclosure_status_current = 2
```

해석:

```text
1. 38개는 target/directness/semantic 쪽에서 탈락했다.
   예: 대웅 대상인데 문서가 mirror page, 업계 기사, 타사/주변 기사처럼 읽힘.

2. 18개는 direct/current claim은 맞지만 primitive가 안 맞아 탈락했다.
   예: DART 정정공시는 "투자기간 종료일 연장"은 말하지만
       "volume_growth_visible"을 직접 증명하지 못한다.
```

쉬운 예:

```text
대웅 공시가 "나보타 3공장 일정이 2027년으로 연장됐다"라고 말한다.
이건 일정 정보다.
하지만 "생산량이 늘었고 매출/마진으로 연결된다"는 증거는 아니다.
그래서 C29 volume growth 점수 칸에는 못 들어간다.
```

## v7 retry가 실제로 본 feedback

retry planner run:

```text
planner_run_role = feedback_retry
planner_feedback = ["previous_claims_rejected_before_score"]
rejected_claim_feedback_count = 8
source_rejection_feedback_count = 0
real_provider_success = true
```

retry prompt의 existing evidence summary에는 다음이 들어갔다.

```text
planner_feedback:
  previous_claims_rejected_before_score

rejected_claim_feedback examples:
  - DART 정정 공시 claim은 volume_growth_visible primitive로 mapping rejected
  - PlumSEC mirror 문서 claim은 target_scope/directness rejected
  - quote/source_url/document_id/anchor_id/rejection_summary 포함
```

retry response의 방향:

```text
Do not reuse the rejected Plumsec mirror/source pattern.
Use original issuer, DART/KIND, IR, report PDF, or trusted original article sources.
Separate 대웅 parent-scope evidence from 대웅제약 subsidiary evidence.
Treat schedule extension as delay risk unless usable capacity/demand proof exists.
```

이건 좋은 변화다.

```text
LLM이 점수를 올리려고 아무 문서나 끼워 맞춘 게 아니라,
거절된 근거를 보고 더 정확한 source route를 제안했다.
```

## 아직 READY가 아닌 이유

v7은 아래를 아직 못 닫았다.

```text
1. accepted brain/web claim = 0
2. brain score contribution = 0
3. brain StageCourt trace = 0
4. representative census row promotion = 0
5. FULL_THESIS row = 0
6. FULL_E2R_100 verified score row = 0
```

따라서 다음 표현은 금지한다.

```text
틀린 표현:
  v7에서 LLM extractor가 9회 성공했으니 Brain/Web evidence pass다.

맞는 표현:
  v7에서 LLM extractor는 실제로 돌았지만,
  accepted claim이 0개라 Brain/Web evidence pass는 계속 실패다.
```

## 다음 병목

v7 기준 다음 병목은 P1이다.

```text
P1. claim rejected feedback after extraction loop 강화
P2. target/directness adjudication 개선
P3. primitive mapper가 이벤트 유형과 primitive gap을 더 정확히 구분하도록 개선
P4. source quality router가 mirror/roundup/full-source라도 score-eligible 원문인지 더 잘 구분
P5. official detail/prior filing comparison task 강화
```

특히 대웅 예시에서 필요한 구분:

```text
정정공시:
  종료일 연장, GMP 승인 예정일, 투자기간 변경
  -> implementation_timeline / delay risk / official status claim 가능

volume_growth_visible:
  생산능력 증가 수치, 상업가동, 수요/수출/고객, 출하/매출 전환
  -> 별도 source-backed claim 필요

따라서 정정공시만으로 volume growth를 열면 안 된다.
```

쉬운 예:

```text
"공장 완공 일정이 늦어졌다"는 문장은 일정표다.
"새 공장 때문에 생산량이 2배가 되고 주문이 잡혔다"는 문장은 volume growth다.
둘은 점수 칸이 다르다.
```

## 추가 테스트 결과

패치 후 타깃 테스트:

```text
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
Ran 23 tests / OK

PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate -v
Ran 81 tests / OK
```

새로 확인하는 테스트:

```text
source_rejection_feedback is added to evidence context
source_rejection_feedback rows do not contain score/stage/current_score_eligible
source_rejection_feedback is visible to planner prompt payload
source_rejection_feedback retries planner once
direct source task acceptance blocks source rejection retry
retry_max=1 blocks source rejection retry
```

## 다음 에이전트 공격 질문

다음 리뷰어는 아래를 공격한다.

```text
1. source_rejection_feedback_count가 live v7에서 0인데 패치가 죽은 코드 아닌가?
   답: unit/controlled path에서는 동작한다. live v7은 all-results-rejected가 아니라 post-extraction rejected 상황이라 claim feedback retry가 맞다.

2. v7에서 web_fetched=9인데 왜 accepted claim이 0인가?
   답: 38개는 wrong target/directness/semantic, 18개는 primitive mapping rejected다.

3. DART 정정공시를 volume_growth_visible로 받아주면 되지 않나?
   답: 안 된다. 일정 연장은 volume growth 직접 증거가 아니다.

4. PlumSEC mirror 문서를 source로 인정하면 되지 않나?
   답: mirror/summary는 원문 역할이 제한적이고, target/directness/semantic 검증에서 탈락한 claim이 많다.

5. claim extractor success를 Brain/Web pass로 볼 수 있나?
   답: 아니다. extractor success는 원문 독해 성공이고, Brain/Web pass는 accepted claim + contribution + StageCourt trace까지 필요하다.
```

## 최종 판정

```text
SOURCE_REJECTION_FEEDBACK_CODE_PATH = IMPLEMENTED_AND_UNIT_TESTED
LIVE_V7_SOURCE_REJECTION_RETRY_OBSERVED = NO
LIVE_V7_CLAIM_REJECTION_RETRY_OBSERVED = YES
LIVE_V7_WEB_FETCH = IMPROVED
LIVE_V7_LLM_EXTRACTION = IMPROVED
LIVE_V7_ACCEPTED_BRAIN_CLAIM = FAIL
LIVE_V7_STAGE_PROMOTION = FAIL
READY = NO
```

한 문장:

```text
v7은 "웹 원문을 못 가져오는 문제"를 일부 넘어서
"가져온 원문을 score-eligible claim으로 닫는 문제"를 드러낸 진단이다.
다음 패치는 점수 완화가 아니라 target/directness/primitive mapping과 source route 품질을 더 정밀하게 고쳐야 한다.
```

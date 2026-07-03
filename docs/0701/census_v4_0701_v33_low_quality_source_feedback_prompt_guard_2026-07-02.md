# Census v4 0701 v33 Low-Quality Source Feedback Prompt Guard

작성일: 2026-07-02

## 결론

v32는 블로그/소셜성 source route를 점수 source로 못 쓰게 막았다.

v33은 그 다음 연결을 고정한다.

```text
블로그/소셜 source reject
  -> web_rejected_documents
  -> source_rejection_feedback
  -> planner prompt payload existing_evidence_summary
  -> feedback_retry planner run
```

즉 블로그를 단순히 버리는 것이 아니라,
LLM planner에게 "이 route는 실패했으니 같은 source pattern을 반복하지 말고
DART/KIND 상세, IR, 리포트 PDF, 회사 newsroom, trusted article original 같은 다른 route를 찾아라"는
피드백으로 되돌리는 경로를 테스트로 고정했다.

쉽게 말하면:

```text
나쁜 방식:
  블로그 글을 버림
  -> 왜 버렸는지 다음 조사자가 모름
  -> LLM이 또 블로그를 찾음

좋은 방식:
  블로그 글을 버림
  -> "개인 블로그라 score source 아님" 영수증을 남김
  -> LLM에게 그 영수증을 보여 줌
  -> 다음 검색은 IR/공시/리포트 원문으로 돌리게 함
```

## 현재 Stage 진실은 바뀌지 않음

이번 패치도 운영 FULL_THESIS Stage를 만든 패치가 아니다.

최신 기준은 그대로다.

```text
latest valid output =
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30

CENSUS_EVENT_BOARD stage row = 3391
CENSUS_EVENT_BOARD non-Stage0 = 85
FULL_THESIS stage row = 0
FULL_E2R_100 verified score row = 0
FULL_THESIS refresh queue = 85
verdict = NOT_READY
```

따라서 v33을 보고도 아래처럼 말하면 안 된다.

```text
운영 Stage가 생겼다.
삼성전자/하이닉스 Stage가 확정됐다.
Brain/Web accepted claim이 생겼다.
FULL_THESIS queue가 닫혔다.
```

말할 수 있는 것은 이것뿐이다.

```text
블로그/소셜성 source reject가 source-level feedback으로 planner에 전달되는 경로가 테스트로 고정됐다.
```

## 왜 이게 goal.md/goal2.md/goal3.md에 맞나

goal 문서들의 공통 요구는 다음이다.

```text
1. snippet/headline/blog/source_proxy는 score evidence가 아니다.
2. LLM은 점수를 직접 만들지 않고 source task/query/claim extraction을 돕는다.
3. 실패한 source route는 낮은 점수나 Red가 아니라 pending/feedback이어야 한다.
4. 같은 잘못된 source pattern을 반복하지 않게 planner context에 실패 사유를 되돌려야 한다.
5. 점수 source가 되려면 원문 anchor, accepted claim, score contribution, StageCourt trace가 닫혀야 한다.
```

v33은 이 중 3번과 4번을 좁게 고정한다.

```text
web_result_low_quality_blog_or_social_not_score_source
  -> score로 가지 않음
  -> stage로 가지 않음
  -> current_score_eligible로 가지 않음
  -> planner feedback으로 감
```

## 코드 변경

수정 파일:

```text
tests/test_research_brain_v4_operational_modes.py
docs/0701/README.md
docs/0701/census_v4_0701_v33_low_quality_source_feedback_prompt_guard_2026-07-02.md
```

테스트 추가:

```text
test_low_quality_blog_source_rejection_feedback_is_visible_to_planner_prompt_payload
test_low_quality_blog_source_rejection_feedback_retries_planner_once
```

테스트 fixture:

```text
_low_quality_blog_source_rejected_bundle(event)
```

fixture가 표현하는 상황:

```text
candidate = 삼성전자 C06 HBM 고객 배정 primitive gap
query = 삼성전자 HBM 고객 배정 개인 블로그
url = https://some-personal-blog.tistory.com/1234
rejection_reason = web_result_low_quality_blog_or_social_not_score_source
fetch_attempts = 0
accepted_claim_ids = 없음
score/stage/current_score_eligible = 없음
```

## 테스트가 확인하는 것

### 1. Planner prompt payload에 들어가는가

검증:

```text
payload["events"][0]["existing_evidence_summary"]["source_rejection_feedback"][0]
```

기대:

```text
source_task_id = TASK-UNIT-LOW-QUALITY-BLOG
rejection_reason_distribution.web_result_low_quality_blog_or_social_not_score_source = 1
score 없음
stage 없음
current_score_eligible 없음
```

그리고 prompt rule에 다음 방향이 살아 있어야 한다.

```text
issuer IR
DART/KIND detail
report PDF
company newsroom
trusted article original
```

쉬운 예:

```text
LLM에게 "블로그는 틀렸다"만 말하는 게 아니라,
"다음에는 공식 원문 쪽으로 가라"는 표지판을 같이 보여준다.
```

### 2. Feedback retry planner가 한 번 도는가

검증:

```text
_retry_planner_for_source_rejection_feedback(...)
```

기대:

```text
retry_run is not None
planner_run_role = feedback_retry
planner_feedback = previous_sources_rejected_before_extraction
source_rejection_feedback_count > 0
provider.call_count = 1
```

그리고 retry context에는 같은 rejection reason이 보존된다.

```text
web_result_low_quality_blog_or_social_not_score_source = 1
```

쉬운 예:

```text
첫 번째 조사:
  개인 블로그라 실패

두 번째 조사:
  그 실패 이유를 보고 IR/리포트 route를 다시 계획
```

## 검증 결과

타깃 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_low_quality_blog_source_rejection_feedback_is_visible_to_planner_prompt_payload \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_low_quality_blog_source_rejection_feedback_retries_planner_once -v
```

결과:

```text
Ran 2 tests
OK
```

운영 모드 전체 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
```

결과:

```text
Ran 41 tests
OK
```

확장 교차검증:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_run_mode_honesty -v
```

결과:

```text
Ran 104 tests
OK
```

## 이번 패치가 막은 것

막은 것:

```text
1. low-quality blog/social reject가 source row에만 남고 planner prompt로 안 가는 회귀
2. low-quality blog/social reject feedback에 score/stage/current_score_eligible이 섞이는 회귀
3. feedback_retry가 stock-list reject만 알고 blog/social reject를 모르는 회귀
4. LLM planner가 같은 블로그 route를 반복해도 테스트가 못 잡는 회귀
```

막지 않은 것:

```text
1. 실제 live diagnostic에서 LLM이 정말 더 좋은 route를 선택하는지
2. trusted news / report / issuer newsroom source lineage를 완전히 분리하는 것
3. FULL_THESIS queue 85개를 source-backed claim으로 닫는 것
4. web_or_llm_accepted_claim_count를 0에서 올리는 것
5. FULL_E2R_100 verified score를 생성하는 것
```

## 다음 에이전트 공격 질문

다음 검토자는 이 패치를 이렇게 공격해야 한다.

```text
1. unit fixture에서는 feedback_retry가 돌지만 live run에서도 같은 reason이 planner prompt에 들어가나?
2. planner가 실제로 기존 블로그 URL/source pattern을 반복하지 않는가?
3. "blog.naver.com 회사 공식 채널" 같은 특수 케이스는 어떻게 issuer official로 승격/구분할 것인가?
4. trusted article original과 Naver 재배포/블로그 인용을 source lineage로 구분하는가?
5. feedback_retry가 route를 바꿨는데도 accepted claim이 계속 0이면 pending으로 남고 점수 확정은 막히는가?
6. 이 feedback이 score context가 아니라 source context에만 남는가?
```

## 다음 패치 방향

P0-G3:

```text
source lineage / trusted origin guard.
```

필요한 구분:

```text
Reuters/공식 보도 원문
Naver 재배포
블로그 인용
회사 공식 newsroom
증권사 report PDF
```

점수 source 조건:

```text
original source 또는 공식 source anchor가 있어야 한다.
재배포/블로그/커뮤니티는 source task hint일 수는 있지만 score evidence가 아니다.
```

P0-L:

```text
FULL_THESIS refresh queue 85개 실행 경로.
```

단, unbounded crawl 금지:

```text
각 queue row
  -> bounded SourceTask
  -> official-first
  -> source-backed primitive close
  -> accepted claim
  -> score contribution
  -> StageCourt
  -> FULL_THESIS row or material pending
```

## 최종 판단

v33은 운영 준비 완료가 아니다.

하지만 v32에서 만든 source reject 방어선이 실제 planner feedback까지 이어진다는 점을 테스트로 고정했다.

현재 상태는:

```text
상태판 Stage는 있음.
운영 FULL_THESIS Stage는 아직 없음.
블로그/소셜성 source는 점수로 못 들어감.
그 실패 사유는 LLM planner 재시도 context로 들어감.
```


# Census v4 0701 v35 Source Lineage Feedback Retry Guard

작성일: 2026-07-02 KST

## 0. 결론

v34는 일반 웹/Naver에서 발견한 뉴스/리포트/IR성 문서를 원문 lineage 검증 없이 score source로 쓰지 못하게 막았다.

v35는 그 다음 연결을 고정한다.

```text
source_lineage_unverified_original reject
  -> web_rejected_documents
  -> source_rejection_feedback.not_eligible_reason_distribution
  -> planner prompt rule
  -> feedback_retry planner feedback tag
```

쉽게 말하면:

```text
나쁜 방식:
  네이버 뉴스 fetch
  -> 원문 lineage 미검증이라 reject
  -> 다음 planner가 왜 실패했는지 모름
  -> 다시 같은 네이버 뉴스 route 반복

좋은 방식:
  네이버 뉴스 fetch
  -> 원문 lineage 미검증이라 reject
  -> "이건 discovery-only이고 원문 검증 source가 아니다"를 planner에게 보여 줌
  -> 다음 retry는 DART/KIND 상세, issuer IR/newsroom, report PDF original, trusted article original 쪽으로 계획
```

## 1. 왜 필요한가

goal 문서들의 핵심 요구는 다음이다.

```text
1. snippet/headline/blog/source_proxy는 score evidence가 아니다.
2. 일반 검색 결과는 조사 route일 수 있지만, 곧바로 score source가 아니다.
3. LLM은 점수를 직접 주지 않고 다음 source route와 claim extraction을 도와야 한다.
4. 실패한 source route는 낮은 점수/Red가 아니라 planner feedback이어야 한다.
5. 같은 실패 route를 반복하지 않게 rejection reason을 prompt에 되돌려야 한다.
```

v34만 있으면 2번은 막지만 4~5번은 약하다.

```text
원문 lineage 미검증 source를 점수에서 막음
  -> 좋음

하지만 그 이유가 planner feedback으로 안 감
  -> LLM이 같은 generic web/news route를 반복할 수 있음
```

v35는 이 연결을 테스트로 고정했다.

## 2. 코드 변경

수정 파일:

```text
src/e2r/research_brain/v4_planner_runtime.py
src/e2r/research_brain/v4_production_orchestrator.py
tests/test_research_brain_v4_operational_modes.py
docs/0701/README.md
docs/0701/census_v4_0701_v35_source_lineage_feedback_retry_guard_2026-07-02.md
```

### Planner prompt rule 추가

추가된 의미:

```text
source_rejection_feedback.not_eligible_reason_distribution에
source_lineage_unverified_original이 있으면,
이전 결과는 verified original source가 아니라 discovery-only로 취급한다.

다음에는 official detail URL, issuer-hosted IR/newsroom, report PDF original,
trusted article original을 우선한다.
```

이건 검색어 하드코딩이 아니다.

```text
나쁜 하드코딩:
  C06이면 "HBM 고객 배정" 검색어를 코드가 고정 생성

이번 패치:
  이전 source가 원문 lineage 미검증이라 실패했음을 LLM prompt에 알려줌
  실제 다음 query/source task는 LLM이 생성
```

### Feedback tag 추가

source lineage rejection이 있으면 retry planner run에 다음 feedback tag가 붙는다.

```text
previous_source_lineage_unverified_original
previous_sources_failed_before_or_after_extraction
```

쉬운 예:

```text
"네이버가 찾아준 기사 URL은 봤지만, 원문/신뢰 source로 검증되지 않았다"
라는 실패 표식을 retry planner가 직접 받는다.
```

### Source rejection summary 보강

기존에는 `source_rejection_summary`가 phase/rejection_reason 중심이었다.

v35에서는 `not_eligible_reason_distribution`의 상위 reason도 summary에 포함한다.

따라서 다음 reason이 prompt payload에서 더 잘 보인다.

```text
source_lineage_unverified_original:TrustedNews:general_web_search_provider
```

## 3. 추가 테스트

추가 테스트:

```text
test_source_lineage_unverified_original_feedback_is_visible_to_planner_prompt_payload
test_source_lineage_unverified_original_feedback_retries_planner_once
```

fixture:

```text
_source_lineage_unverified_original_rejected_bundle(event)
```

fixture가 표현하는 상황:

```text
candidate = 삼성전자 C06 HBM 고객 배정 primitive gap
source task = TrustedNews preferred, CompanyNewsroom/ReportPDF fallback
query = 삼성전자 HBM 고객 배정 뉴스
provider = NaverFreeSearchProvider
document = fetched
accepted_claim_ids = []
not_eligible_reasons =
  source_task_provider_error_score_block:general_search_not_score_source
  source_provider_document_type_mismatch:TrustedNews:general_web_search_provider
  source_lineage_unverified_original:TrustedNews:general_web_search_provider
```

중요한 점:

```text
fetch까지 됐지만 score source는 아니다.
이유는 "문서가 없어서"가 아니라 "일반 웹 경유 source라 원문 lineage가 검증되지 않아서"다.
```

## 4. 테스트가 확인하는 것

### 1. Planner prompt payload

검증:

```text
payload["events"][0]["existing_evidence_summary"]["source_rejection_feedback"][0]
```

기대:

```text
source_task_id = TASK-UNIT-SOURCE-LINEAGE
not_eligible_reason_distribution.source_lineage_unverified_original:TrustedNews:general_web_search_provider = 1
source_rejection_summary contains source_lineage_unverified_original
score 없음
stage 없음
current_score_eligible 없음
```

Planner rule에도 다음 의미가 있어야 한다.

```text
source_lineage_unverified_original
verified original source
```

### 2. Feedback retry planner run

검증:

```text
_retry_planner_for_source_rejection_feedback(...)
```

기대:

```text
retry_run.planner_run_role = feedback_retry
retry_run.planner_feedback =
  previous_source_lineage_unverified_original
  previous_sources_failed_before_or_after_extraction
provider.call_count = 1
source_rejection_feedback_count > 0
```

그리고 retry context에도 같은 reason이 보존된다.

```text
source_lineage_unverified_original:TrustedNews:general_web_search_provider = 1
```

## 5. 검증 결과

타깃 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_source_lineage_unverified_original_feedback_is_visible_to_planner_prompt_payload \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_source_lineage_unverified_original_feedback_retries_planner_once -v
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
Ran 43 tests
OK
```

확장 교차검증:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_run_mode_honesty -v
```

결과:

```text
Ran 122 tests
OK
```

참고:

```text
v34 직후 전체 unittest는 Ran 5063 tests OK였다.
v35 이후에는 source/operational/readiness 관련 확장 묶음 122개를 재검증했다.
```

## 6. 이번 패치가 막은 것

막은 것:

```text
1. source_lineage_unverified_original reason이 web_rejected_documents에만 남고 planner prompt로 안 가는 회귀
2. 원문 lineage 미검증 source reject 이후 LLM이 같은 generic web/news route를 반복하는 회귀
3. retry planner가 source lineage 문제를 단순 post-extraction 실패로만 보고 원문 route를 못 바꾸는 회귀
4. source rejection feedback에 score/stage/current_score_eligible이 섞이는 회귀
```

막지 않은 것:

```text
1. 실제 TrustedNews connector 구현
2. 실제 report PDF original resolver 구현
3. 실제 company newsroom crawler 구현
4. FULL_THESIS production run 성공
5. web_or_llm accepted claim 생성
```

## 7. 현재 Stage 진실은 바뀌지 않음

이번 v35도 운영 FULL_THESIS Stage를 만든 패치가 아니다.

최신 진실은 그대로다.

```text
CENSUS_EVENT_BOARD 상태판 Stage:
  rows = 3391
  non_Stage0 = 85

FULL_THESIS 운영 Stage:
  rows = 0

FULL_E2R_100 verified score:
  rows = 0

Brain/Web enabled v28:
  verdict = BLOCKED
  web_or_llm_accepted_claim_count = 0

Queue/timeout v30:
  Brain/Web = disabled / NOT_REQUESTED
  full_thesis_refresh_queue_candidate_count = 85
```

쉬운 예:

```text
v35는 "조사원이 같은 잘못된 뉴스 길을 반복하지 않게 안내판을 붙인 것"이다.
아직 "그 조사원이 원문을 찾아와서 FULL_THESIS 성적표를 완성한 것"은 아니다.
```

## 8. 다음 패치 방향

다음 우선순위:

```text
P0. source_lineage feedback이 실제 live planner output의 source task route를 바꾸는지 bounded smoke로 확인
P1. TrustedNews / ReportPDF / CompanyNewsroom original resolver 중 하나를 실제 connector로 닫기
P2. FULL_THESIS refresh queue 85개 중 1~3개를 production bounded mode로 실행해 accepted web/LLM claim 생성
P3. provider/source pending이 낮은 점수/Red로 확정되지 않는지 다시 검증
P4. 삼성전자/하이닉스는 상태판 Stage1이 아니라 FULL_THESIS_NOT_RUN임을 operator digest에도 반복 표시
```

완료 기준은 아직 아니다.

```text
goal.md/goal2.md/goal3.md 전체 완료 조건:
  FULL_THESIS 운영 row 생성
  Brain/Web accepted claim 생성
  source-backed score contribution
  StageCourt trace
  subagent 5명 99점 이상 리뷰

현재 v35:
  source rejection feedback 경로 보강
  운영 readiness = NOT_READY
```

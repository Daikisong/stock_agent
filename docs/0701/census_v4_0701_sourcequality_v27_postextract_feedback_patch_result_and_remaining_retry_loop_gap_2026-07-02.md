# Census v4 0701 Sourcequality v27 Post-Extraction Feedback Patch Result

작성일: 2026-07-02 KST

기준 산출물:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v27
```

비교 기준:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v26
```

## 0. 결론

v27도 `NOT_READY`가 맞다.

다만 이번 패치로 하나는 분명히 좋아졌다.

```text
v26:
  source_rejection_feedback_count = 0
  rejected_claim_feedback_count = 8
  feedback_retry는 있었지만 provider_error로 막힘

v27:
  source_rejection_feedback_count = 1
  rejected_claim_feedback_count = 0
  feedback_retry planner run이 real_provider_success=true로 성공
```

쉽게 말하면:

```text
이전에는 "나쁜 source를 잡았다"는 실패가 LLM에게 제대로 안 돌아가거나,
claim-level retry가 policy에 걸려 막혔다.

이제는 source-level 실패가 LLM에게 돌아갔고,
LLM이 다른 source route를 실제로 다시 계획했다.
```

하지만 아직 운영 Stage는 없다.

```text
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
web/LLM accepted claim = 0
Brain/Web readiness = BLOCKED
```

## 1. 이번 코드 패치

변경 파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
src/e2r/research_brain/v4_planner_runtime.py
tests/test_research_brain_v4_operational_modes.py
```

핵심 변경:

```text
기존:
  _source_rejection_feedback_from_bundle이
  rejection_phase == post_extraction_evidence_os row를 무조건 continue로 버림

변경:
  post_extraction_evidence_os row도 source_rejection_feedback에 포함
  rejection_phase_distribution / not_eligible_reason_distribution / provider_error_distribution을 기록
  feedback에는 score, stage, current_score_eligible을 넣지 않음
```

왜 필요한가:

```text
웹 문서를 fetch하고 LLM extractor까지 돌았는데,
accepted claim이 0이면 그 실패 이유를 LLM planner가 알아야 한다.

그래야 같은 블로그/포털/채널 route를 반복하지 않고,
IR/DART 상세/리포트 PDF/회사 newsroom/원문 기사 같은 더 좋은 source를 찾는다.
```

쉬운 예:

```text
나쁜 방식:
  블로그를 읽었지만 점수 claim으로 못 닫음
  -> 그냥 종료

좋은 방식:
  블로그는 score source가 아니었고 mapping도 실패했다고 기록
  -> LLM에게 되돌려 회사 IR/원문 PDF/공시 상세로 다시 계획하게 함
```

## 2. 테스트 결과

추가/강화된 테스트:

```text
test_post_extraction_source_rejection_becomes_source_feedback
test_post_extraction_source_rejection_retries_planner_with_post_tag
test_direct_acceptance_does_not_block_post_extraction_source_feedback_retry
```

Targeted:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_post_extraction_source_rejection_becomes_source_feedback \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_post_extraction_source_rejection_retries_planner_with_post_tag \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_direct_acceptance_does_not_block_post_extraction_source_feedback_retry -v

result:
  Ran 3 tests / OK
```

Operational modes:

```text
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v

result:
  Ran 38 tests / OK
```

Related module suite:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_census_v4_brain_web_readiness_gate -v

result:
  Ran 94 tests / OK
```

Full unittest:

```text
command:
  PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
    --artifact output/test_full_repo_0701/full_unittest_after_p0f_postextract_feedback_artifact.json \
    --log output/test_full_repo_0701/full_unittest_after_p0f_postextract_feedback.log \
    -- python -m unittest discover -s tests -v

status = OK
test_count = 5054
failed_count = 0
error_count = 0
duration_seconds = 191.2057
artifact =
  output/test_full_repo_0701/full_unittest_after_p0f_postextract_feedback_artifact.json
log_sha256 =
  33d2eb5087e5306a7c2b8a89855f39a860621559e6b267c1f4ddebc2f7b67248
```

## 3. v26 -> v27 지표 변화

### v26

```text
readiness = NOT_READY
Brain/Web readiness = BLOCKED

llm_planner_call_count = 22
llm_real_provider_success_count = 1
source_task_execution_count = 13
official_accepted_claim_count = 24
web_or_llm_accepted_claim_count = 0

web_search_task_count = 4
web_search_call_count = 4
web_search_result_count = 38
web_fetched_document_count = 2
web_rejected_document_count = 28
llm_claim_extractor_attempt_count = 2

planner retry:
  feedback_retry count = 1
  source_rejection_feedback_count = 0
  rejected_claim_feedback_count = 8
  retry provider_error = FCF/DART-solvable gap sent to general web/news: contract_visibility
```

### v27

```text
readiness = NOT_READY
Brain/Web readiness = BLOCKED

llm_planner_call_count = 22
llm_real_provider_success_count = 2
source_task_execution_count = 10
official_accepted_claim_count = 8
web_or_llm_accepted_claim_count = 0

web_search_task_count = 6
web_search_call_count = 6
web_search_result_count = 33
web_fetched_document_count = 1
web_rejected_document_count = 24
llm_claim_extractor_attempt_count = 1

planner retry:
  feedback_retry count = 1
  source_rejection_feedback_count = 1
  rejected_claim_feedback_count = 0
  retry real_provider_success = true
```

해석:

```text
source rejection feedback retry 자체는 live v27에서 성공했다.
하지만 그 retry가 accepted web/LLM claim을 만들지는 못했다.
```

## 4. v27 후보와 차단 사유

v27 FULL_THESIS production runner:

```text
candidate_row_count = 1
promoted_full_thesis_row_count = 0
blocked symbol = 003090
blocked archetype = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
present_primitives =
  implementation_timeline
missing_green_primitives =
  direct_company_cash_route
  policy_or_regulatory_confirmed
  subsidy_capture_visible
blocker =
  missing_green_gate_primitives
```

쉬운 예:

```text
대웅의 신규시설투자 정정 공시에서 일정/implementation 쪽 일부는 확인됐다.
하지만 정책 보조금, 직접 현금 유입, 회사별 수혜 경로는 아직 확인되지 않았다.

그래서 C31 FULL_THESIS로 올리면 안 된다.
```

## 5. v27 웹/LLM 실패 내용

v27에서 실제 fetch된 웹 문서:

```text
http://www.doctorstimes.com/news/articleView.html?idxno=222694
title = [제약업계 소식] 4월28일
```

이 문서는 post-extraction에서 거절됐다.

```text
rejection_phase = post_extraction_evidence_os
rejection_reason = post_extraction_no_score_eligible_claim
not_eligible_reasons =
  source_task_provider_error_score_block:general_search_not_score_source
  source_provider_document_type_mismatch:IndustryMedia:general_web_search_provider
  semantic_rejected
  target_scope_not_allowed:UNRELATED
  target_not_direct:NOT_TARGET_SCOPED
  temporal_not_allowed:HISTORICAL
  mapping_not_accepted:REJECTED
  primitive_mapping_rejected:adjudication_not_passed
```

이 거절은 맞다.

```text
제약업계 소식 모음 기사를 대웅의 직접 정책/보조금/현금유입 claim으로 쓰면 안 된다.
```

## 6. 남은 retry-loop 병목

이번 코드 패치로 post-extraction rejection을 feedback row로 만들 수 있게 됐다.

테스트에서도 아래가 증명됐다.

```text
post_extraction_evidence_os rejection
-> source_rejection_feedback에 포함
-> planner retry 입력으로 전달
-> score/stage/current_score_eligible 미포함
```

하지만 v27 live run에서는 post-extraction rejection이 `feedback_retry` 실행 뒤에 생겼다.

현재 production shadow 흐름은:

```text
initial planner
-> source tasks 실행
-> rejected mapping 또는 source rejection이면 1회 feedback_retry
-> retry source tasks 실행
-> merge
-> 종료
```

따라서 retry source task에서 새 post-extraction failure가 생기면,
그 실패는 산출물에는 남지만 같은 run 안에서 다시 planner에게 돌아가지는 않는다.

이걸 완료로 과장하면 안 된다.

현재 정확한 상태:

```text
P0-F code path:
  implemented and unit-tested.

P0-F first-level live feedback:
  source_rejection_feedback retry success로 일부 증명됨.

P0-F chained post-extraction live retry:
  아직 미구현/미검증.
```

## 7. 다음 패치 방향

### P0-J. bounded feedback retry loop

목표:

```text
initial 이후 1회 retry만 고정하지 말고,
config.retry_max 안에서 feedback retry를 반복한다.
```

원칙:

```text
무제한 retry 금지.
retry_max=None 금지 유지.
동일 URL/source pattern 반복 금지.
accepted claim이 생겨도 별도 external web/LLM 실패가 있으면 다음 retry 후보로 남길 수 있음.
score/stage/current_score_eligible은 feedback에 넣지 않음.
```

쉬운 예:

```text
1차 검색: 텔레그램/블로그만 나옴
  -> source feedback

2차 검색: 업계 기사 fetch, LLM 읽음, target unrelated로 거절
  -> post-extraction feedback

3차 검색: 회사 IR 또는 공시 상세로 재계획
```

단, 운영에서는 아래처럼 bounded여야 한다.

```text
retry_max = 3이면 최대 initial + 2 retries
같은 URL/도메인/소스 패턴 반복 금지
새 accepted claim 또는 no_new_feedback이면 stop
```

### P0-G 계속: source route 품질 개선

v27 검색 결과 도메인:

```text
t.me = 10
blog.kakaocdn.net = 3
blog.naver.com = 2
kind.krx.co.kr = 2
www.yhs.co.kr = 2
www.daewoong.co.kr = 1
www.daewoong.com = 1
doctorstimes.com = 1
broker/report domains 일부
```

여전히 낮은 품질 source가 많다.

다음에는:

```text
web discovery 결과가 official/issuer/report 원문이면 resolver로 승격
블로그/채널/시황 모음은 더 빨리 reject
company newsroom / IR / DART detail route를 우선 fetch
```

## 8. 다음 에이전트 공격 질문

```text
1. v27 source_rejection_feedback_count=1이 실제 planner prompt에 들어갔는가?
2. retry planner output이 이전 source pattern을 피했는가?
3. post_extraction_evidence_os row가 feedback row로 변환되는 code path는 unit test뿐 아니라 live chained retry에서도 검증되는가?
4. retry_max를 늘릴 때 무제한 fetch가 열리지 않는가?
5. doctorstimes 업계소식 기사를 점수 source로 열지 않고 reject한 것이 유지되는가?
6. C31에서 implementation_timeline 하나로 FULL_THESIS 승격하지 않는가?
7. web/LLM accepted claim이 0인데 Brain/Web ready라고 쓰는 report가 남아 있는가?
```

## 9. 현재 판정

```text
NOT_READY 유지가 맞다.

이번 패치는 source feedback loop의 한 병목을 줄였다.
하지만 운영 FULL_THESIS Stage는 아직 없다.

다음 핵심은 bounded multi-step feedback retry와 source route 품질 개선이다.
```

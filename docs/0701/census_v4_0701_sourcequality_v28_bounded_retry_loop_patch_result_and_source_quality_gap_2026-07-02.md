# Census v4 0701 Sourcequality v28 Bounded Retry Loop Patch Result

작성일: 2026-07-02 KST

기준 산출물:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v28
```

비교 기준:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v27
```

## 0. 결론

v28도 `NOT_READY`가 맞다.

하지만 bounded feedback retry loop는 실제로 작동했다.

```text
v27:
  planner rows = 22
  feedback_retry = 1
  real_provider_success = 2
  source_rejection_feedback_count_sum = 1

v28:
  planner rows = 23
  feedback_retry = 2
  real_provider_success = 3
  source_rejection_feedback_count_sum = 4
```

쉽게 말하면:

```text
v27은 "나쁜 source였어"를 LLM에게 한 번 돌려줬다.
v28은 retry_max=3 안에서 한 번 더 돌릴 수 있게 됐다.
```

하지만 아직 목표에는 못 갔다.

```text
web/LLM accepted claim = 0
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
Brain/Web readiness = BLOCKED
```

즉 이번 패치는:

```text
재조사 루프 배선 개선 = 성공
운영 Stage 생성 = 아직 실패
```

## 1. 이번 코드 패치

변경 파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
src/e2r/research_brain/v4_schemas.py
src/e2r/census/census_runner_v4.py
src/e2r/cli/run_e2r_census_v4_until_pass.py
tests/test_research_brain_v4_operational_modes.py
```

핵심 변경:

```text
기존:
  initial planner
  -> source task 실행
  -> feedback_retry 1회
  -> 종료

변경:
  initial planner
  -> source task 실행
  -> config.retry_max 안에서 bounded feedback retry 반복
  -> 동일 retry output signature 반복 시 중단
  -> retry_max=None / retry_max<=0 금지
```

CLI 추가:

```text
--brain-retry-max
```

기본값:

```text
2
```

따라서 기존 기본 동작은 바뀌지 않는다.

v28은 진단 목적으로 아래처럼 실행했다.

```text
--brain-retry-max 3
```

## 2. 왜 필요한가

v27에서 드러난 병목:

```text
initial source 실패
-> planner retry 성공
-> retry source task에서 post_extraction_evidence_os 실패 발생
-> 하지만 run 종료
```

쉬운 예:

```text
1차 검색:
  블로그/시황 페이지라 실패

2차 검색:
  업계 기사 원문을 fetch하고 LLM도 읽었지만 target unrelated라 실패

이때 3차 검색:
  회사 IR/DART 상세/리포트 PDF 쪽으로 다시 가야 하는데,
  기존 구조는 2차에서 멈췄다.
```

v28 패치는 이 구조를 `retry_max` 안에서 반복 가능하게 만들었다.

## 3. 테스트 결과

추가/강화된 테스트:

```text
test_feedback_retry_loop_can_chain_post_extraction_feedback_until_retry_max
test_unbounded_top_results_and_retry_are_rejected
```

Targeted:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_feedback_retry_loop_can_chain_post_extraction_feedback_until_retry_max \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_unbounded_top_results_and_retry_are_rejected -v

result:
  Ran 2 tests / OK
```

Operational modes:

```text
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v

result:
  Ran 39 tests / OK
```

Related module suite:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_cli_uses_v4_runner \
  tests.test_census_v4_run_mode_honesty -v

result:
  Ran 114 tests / OK
```

Full unittest:

```text
command:
  PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
    --artifact output/test_full_repo_0701/full_unittest_after_p0f_p0j_postextract_bounded_retry_artifact.json \
    --log output/test_full_repo_0701/full_unittest_after_p0f_p0j_postextract_bounded_retry.log \
    -- python -m unittest discover -s tests -v

status = OK
test_count = 5055
failed_count = 0
error_count = 0
duration_seconds = 193.9391
artifact =
  output/test_full_repo_0701/full_unittest_after_p0f_p0j_postextract_bounded_retry_artifact.json
log_sha256 =
  5f852f4608b0cdc42dc0b0c35d92e009b31b645eefb87c3c6b8669374c930262
```

## 4. v27 -> v28 지표 변화

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

feedback_retry = 1
```

### v28

```text
readiness = NOT_READY
Brain/Web readiness = BLOCKED

llm_planner_call_count = 23
llm_real_provider_success_count = 3
source_task_execution_count = 23
official_accepted_claim_count = 48
web_or_llm_accepted_claim_count = 0

web_search_task_count = 6
web_search_call_count = 6
web_search_result_count = 20
web_fetched_document_count = 1
web_rejected_document_count = 14
llm_claim_extractor_attempt_count = 1

feedback_retry = 2
```

해석:

```text
bounded retry loop는 더 많은 planner/source-task 실행으로 이어졌다.
하지만 source 품질이 여전히 낮아서 accepted web/LLM claim은 0이다.
```

## 5. v28 후보와 차단 사유

v28 FULL_THESIS production runner:

```text
candidate_row_count = 1
promoted_full_thesis_row_count = 0
blocked symbol = 114450
blocked archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
missing_green_primitives =
  margin_bridge_visible
blocker =
  missing_green_gate_primitives
```

쉬운 예:

```text
계약 금액/기간 같은 공식 공시 claim은 더 많이 닫혔다.
하지만 "이 계약이 마진/현금흐름 개선으로 이어진다"는 bridge는 아직 없다.
```

그래서 FULL_THESIS 승격 차단은 여전히 맞다.

## 6. v28 웹 source 품질

v28 웹 검색 도메인:

```text
timeli.tistory.com = 10
report.hangyeong.com = 3
blog.naver.com = 2
www.seoul.co.kr:8888 = 1
t.me = 1
economic7.tistory.com = 1
academic.naver.com = 1
www.equity.co.kr = 1
```

fetch된 문서:

```text
https://economic7.tistory.com/.../250617-특징-상한가-및-급등종목
title = 250617 특징 상한가 및 급등종목
```

이 문서는 score source로 인정되면 안 된다.

```text
상한가/급등종목 정리 글은 margin_bridge_visible의 원문 증거가 아니다.
```

따라서 `web/LLM accepted claim = 0`은 현재 guard 관점에서 맞다.

## 7. 다음 병목

현재 병목은 retry loop가 아니라 source route 품질이다.

```text
retry는 더 돌 수 있다.
하지만 계속 Tistory, 텔레그램, 블로그, 급등종목 정리 글을 가져오면 accepted claim은 0이다.
```

다음 패치는 P0-G 쪽이다.

```text
1. Naver result가 official/issuer/report 원문이면 resolver로 승격
2. 블로그/채널/급등종목/시황 모음은 더 빨리 reject
3. company newsroom / IR / DART detail / public report PDF 우선 fetch
4. 일반 웹 provider 문서를 score source로 직접 허용하지 않음
```

쉬운 예:

```text
나쁜 패치:
  economic7.tistory.com 급등종목 글도 LLM이 읽었으니 점수 source로 인정

좋은 패치:
  급등종목 글은 source failure로 기록
  같은 query pattern 반복을 막고
  회사 공시 상세, IR, 리포트 PDF, 신뢰 뉴스 원문으로 route를 좁힘
```

## 8. 다음 에이전트 공격 질문

```text
1. --brain-retry-max 3이 run_metadata/reproduction command에 남는가?
2. retry loop가 retry_max를 넘지 않는가?
3. 동일 retry output signature 반복 시 멈추는가?
4. source feedback에 score/stage/current_score_eligible이 들어가지 않는가?
5. web/LLM accepted claim 0인데 Brain/Web ready로 표시하는 경로가 없는가?
6. 공식 accepted claim 48개를 web/LLM accepted로 착각하지 않는가?
7. 114450 C05 margin_bridge_visible을 급등종목 글로 채우지 않는가?
8. source route 품질 개선 없이 operational minimum count만 늘리는 패치로 도망치지 않는가?
```

## 9. 현재 판정

```text
P0-J bounded feedback retry loop:
  implemented.
  tested.
  live v28에서 feedback_retry 2회로 확인됨.

Brain/Web evidence pass:
  still blocked.

FULL_THESIS operation:
  still 0 rows.

Next:
  P0-G source route quality improvement.
```

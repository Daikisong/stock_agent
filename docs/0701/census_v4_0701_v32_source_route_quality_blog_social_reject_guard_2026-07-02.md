# Census v4 0701 v32 Source Route Quality Blog/Social Reject Guard

작성일: 2026-07-02

## 결론

이번 패치는 운영 FULL_THESIS Stage를 만든 패치가 아니다.

이번 패치의 목적은 더 좁다.

```text
개인 블로그, Tistory, Naver blog/cafe/post, Telegram, 포럼, 리딩방성 글을
점수 source로 fetch/claim/score 경로에 태우지 않고,
명시적인 reject row와 planner feedback으로 남긴다.
```

현재 최신 유효 산출물 기준 진실은 그대로다.

```text
latest valid output =
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30

event_board_stage_row_count = 3391
event_board_non_stage0_count = 85
FULL_THESIS stage row = 0
FULL_E2R_100 verified score row = 0
FULL_THESIS refresh queue = 85

verdict = NOT_READY
```

쉽게 말하면:

```text
출석부 상태 스티커는 3391명에게 붙어 있다.
그중 "뭔가 볼 만한 애"는 85명이다.
하지만 각 종목을 운영용 full thesis로 다시 조사하고
검증 claim, score contribution, StageCourt까지 닫은 성적표는 아직 0개다.
```

## 왜 이 패치가 필요했나

직전 흐름에서 가장 위험했던 실패 패턴은 이것이다.

```text
LLM이 만든 검색어
  -> Naver web 결과
  -> Tistory/블로그/급등주 정리 글
  -> target 이름이 들어 있으니 fetch
  -> 본문 일부를 LLM이 그럴듯하게 claim으로 읽음
  -> 점수 source처럼 보이는 row가 생김
```

이건 사용자가 계속 지적한 문제와 같은 계열이다.

```text
나쁜 예:
  "월덱스 감사의견 적정" 글에 삼성전자가 고객사로 언급됨
  -> 삼성전자 회계 리스크로 오귀속

이번에 막는 예:
  "삼성전자 HBM 개인 블로그 투자아이디어"
  -> 삼성전자 HBM 고객 배정 증거처럼 오인
```

둘 다 원인은 같다.

```text
문서가 어느 source route에서 왔는지,
그 source route가 점수 source로 admissible한지,
원문 anchor가 실제 점수 primitive를 지지하는지
분리하지 않으면 LLM이 "검색 대상 회사" 기준으로 문서를 끼워 맞출 수 있다.
```

## 이게 하드코딩인가?

검색어 하드코딩은 아니다.

금지되는 하드코딩은 이런 것이다.

```python
if archetype == "C06":
    query = f"{company} HBM long term contract prepayment"

if symbol == "005930":
    ignore_risk = True
```

이번 패치는 그런 방식이 아니다.

이번 패치는 source admissibility 정책이다.

```text
Tistory 개인 블로그
Naver blog/cafe/post
Telegram
포럼/커뮤니티성 페이지
리딩방/관심종목/급등주 정리 글

이런 route는 어느 종목이든 점수 원문 source가 아니다.
```

쉬운 예:

```text
학교 성적을 매길 때 학생이 쓴 답안지는 채점할 수 있다.
신문 공식 기사나 학교 공문도 참고할 수 있다.
하지만 옆 반 친구 블로그의 "이 학생 공부 잘하는 듯" 글은 성적표 점수 근거가 아니다.
그 글은 "선생님, 공식 성적표나 시험지를 찾아보세요"라는 조사 힌트일 수는 있다.
```

따라서 이번 reject는 점수를 만들기 위한 deterministic query synthesis가 아니라,
점수에 들어갈 수 없는 source route를 점수 전에 차단하는 전역 정책이다.

## 코드 변경

수정 파일:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
tests/test_research_brain_v4_real_source_acquisition.py
docs/0701/README.md
docs/0701/census_v4_0701_v32_source_route_quality_blog_social_reject_guard_2026-07-02.md
```

핵심 변경 1:

```text
_official_detail_route_from_url(url) 추가
```

이유:

```text
_looks_like_low_quality_blog_or_social_page()
  -> 공식 DART/KIND 상세 URL은 블로그/소셜 필터 예외로 둬야 함
  -> 이를 위해 _official_detail_route_from_url(url)을 호출함
  -> 그런데 helper가 없으면 Tistory/블로그 검증 경로에서 NameError 가능
```

패치 후:

```text
url host가 정확히 dart.fss.or.kr이고 rcpNo/rcept_no 계열이 있으면 DART 공식 상세 route
url host가 정확히 kind.krx.co.kr이고 acptno/acpt_no 계열이 있으면 KIND 공식 상세 route
그 외는 공식 detail route 아님
```

주의:

```text
example.com/archive/kind.krx.co.kr/fake-disclosure
```

같은 URL은 KIND로 인정하지 않는다. host가 정확히 `kind.krx.co.kr`일 때만 공식 route다.

핵심 변경 2:

```text
검색 결과 metadata 단계 reject:
  web_result_low_quality_blog_or_social_not_score_source

fetch 후 본문 단계 reject:
  web_fetch_low_quality_blog_or_social_not_score_source
```

즉 같은 품질 문제라도 어디서 잡혔는지 구분한다.

```text
검색 결과 URL/title/snippet만 봐도 블로그다
  -> fetch_attempts = 0
  -> REJECTED_NON_EVIDENCE_RESULT_METADATA

URL만으로는 몰랐지만 본문이 개인 투자글이다
  -> fetch_attempts = 1
  -> REJECTED_NON_EVIDENCE_CONTENT_AFTER_FETCH
```

## 추가 테스트

추가 테스트 1:

```text
test_live_full_bounded_rejects_low_quality_blog_before_fetch
```

검증 내용:

```text
url = https://some-personal-blog.tistory.com/1234
title = 삼성전자 HBM 고객 배정 개인 블로그 정리

expected:
  status = PROVIDER_FAILED
  fetched_document_ids = ()
  selection_status = REJECTED_NON_EVIDENCE_RESULT_METADATA
  rejection_reason = web_result_low_quality_blog_or_social_not_score_source
  fetch_attempts = 0
```

쉬운 예:

```text
문패부터 "개인 블로그"면 문을 열고 본문을 읽지 않는다.
그 대신 "이 route는 실패"라고 기록하고 더 좋은 route를 찾게 한다.
```

추가 테스트 2:

```text
test_live_full_bounded_rejects_low_quality_blog_content_after_fetch
```

검증 내용:

```text
url = https://news.example.com/samsung-hbm-commentary
metadata만 보면 블로그인지 확정 불가
fetch text = 삼성전자 HBM ... 개인블로그 투자아이디어 ...

expected:
  status = PROVIDER_FAILED
  fetched_document_ids = ()
  selection_status = REJECTED_NON_EVIDENCE_CONTENT_AFTER_FETCH
  rejection_reason = web_fetch_low_quality_blog_or_social_not_score_source
  fetch_attempts = 1
```

쉬운 예:

```text
겉표지는 기사처럼 보였는데 열어 보니 개인 투자 메모였다.
그러면 그 문서는 점수 칸에 쓰지 않고 reject row로 남긴다.
```

## 검증 결과

타깃 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_real_source_acquisition -v
```

결과:

```text
Ran 28 tests
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
Ran 102 tests
OK
```

이 확장 테스트가 같이 본 것:

```text
1. source acquisition의 official/web/fallback 행위가 깨지지 않았는가
2. source rejection feedback이 planner context로 들어가는 기존 경로가 유지되는가
3. Brain/Web readiness gate가 source row 숫자만 보고 READY를 만들지 않는가
4. CLI partial output guard가 유지되는가
```

## 최신 산출물 교차검증

`jq`가 환경에 없어 `rg/sed`로 확인했다.

확인 파일:

```text
output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/audit_summary.json
output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/full_thesis_refresh_queue_audit.json
output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/llm_claim_extraction_audit.json
output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/brain_web_readiness_gate_audit.json
```

핵심 수치:

```text
eligible_symbol_count = 3391
event_board_stage_row_count = 3391
event_board_non_stage0_count = 85

base_stage_distribution:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

canonical_stage_distribution:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE = 3391

operator_score_use_distribution:
  NOT_FULL_E2R_SCORE = 3391

full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
full_e2r_verified_score_present_count = 0
full_thesis_refresh_queue_candidate_count = 85
```

FULL_THESIS refresh queue audit:

```text
verdict = PASS
queue_candidate_count = 85
event_board_non_stage0_count = 85
full_thesis_stage_row_count = 0

critical_counts:
  hardcoded_query_count = 0
  operator_stage_copy_count = 0
  queue_missing_event_board_count = 0
  score_allowed_before_execution_count = 0
  stage_promotion_allowed_before_execution_count = 0
  unbounded_budget_count = 0
```

LLM claim extraction audit for v30 ledger-refresh run:

```text
verdict = DISABLED_HONESTY_PASS
requested_by_brain_web_mode = false
requested_by_run_mode = false
configured_timeout_seconds = 60.0
llm_claim_extractor_attempt_count = 0
llm_claim_extractor_provider_error_count = 0
llm_claim_extractor_timeout_count = 0
```

Brain/Web readiness gate for v30 ledger-refresh run:

```text
verdict = NOT_REQUESTED
brain_web_mode = disabled
run_mode = LEDGER_REFRESH_CENSUS
brain_web_evidence_pass_allowed = false
web_search_task_count = 0
web_fetched_document_count = 0
web_or_llm_accepted_claim_count = 0
```

중요:

```text
DISABLED_HONESTY_PASS나 NOT_REQUESTED는 Brain/Web 성공이 아니다.
이 run은 "꺼져 있는데 성공으로 과장하지 않았음"을 검증한 것이다.
```

## 현재 Stage 질문에 대한 답

질문:

```text
stage가 있는 애들이 있긴 해?
```

정확한 답:

```text
CENSUS_EVENT_BOARD stage는 있다.
  row_count = 3391
  non-Stage0 = 85

운영용 FULL_THESIS stage는 아직 없다.
  row_count = 0

검증된 FULL_E2R_100 score도 아직 없다.
  row_count = 0
```

쉬운 예:

```text
CENSUS_EVENT_BOARD:
  "이 종목은 오늘 볼 만한 이벤트가 있나?"를 표시한 상태판

FULL_THESIS:
  "원문 증거를 다 읽고 점수표 칸별로 claim이 닫혔나?"를 계산한 운영 판정

현재는 상태판은 있는데 운영 판정은 없다.
```

따라서 지금 누구에게도:

```text
삼성전자 운영 Stage1
SK하이닉스 운영 Stage1
어떤 종목 운영 3-Yellow
```

라고 말하면 안 된다.

말할 수 있는 것은 이 정도다.

```text
삼성전자와 SK하이닉스는 CENSUS_EVENT_BOARD 쪽 Stage1 샘플에 보일 수 있다.
하지만 FULL_THESIS_NOT_RUN이고 verified_score=None이면 운영 점수/Stage가 아니다.
```

## 이번 패치가 막은 것

막은 것:

```text
1. Tistory/개인 블로그를 fetch해서 점수 source처럼 보이게 만드는 경로
2. URL은 애매하지만 본문이 개인 투자글인 문서를 score source로 넘기는 경로
3. 공식 DART/KIND 상세 URL을 블로그/소셜 reject와 섞어 잘못 막는 경로
4. low-quality filter가 helper 부재로 NameError를 내는 경로
```

막지 않은 것:

```text
1. 실제 FULL_THESIS queue 85개를 source-backed claim으로 닫는 것
2. LLM extractor provider가 live에서 충분히 안정적으로 claim을 닫는 것
3. 일반 뉴스 중 어떤 도메인이 trusted source인지 domain/source lineage로 판단하는 것
4. accepted claim을 score contribution으로 연결해 FULL_E2R_100 점수를 만드는 것
5. 삼성전자/하이닉스 bounded live smoke를 운영 판정으로 완성하는 것
```

## 다음 에이전트가 공격해야 할 질문

다음 에이전트는 이 문서를 믿지 말고 아래를 확인해야 한다.

```text
1. low-quality reject row가 실제 planner feedback prompt에 들어가나?
2. planner가 "블로그 실패"를 보고 DART/KIND/IR/report/news original route를 새로 제안하나?
3. rejection reason이 source row에는 남지만 score context에는 들어가지 않는가?
4. Tistory reject가 너무 넓어서 issuer official blog/newsroom까지 막지 않는가?
5. blog.naver.com은 막지만, 회사 공식 newsroom이 Naver post에 있는 특수 케이스는 어떻게 처리할 것인가?
6. source admissibility reject가 "증거 없음"과 구분되어 Source Pending 또는 route retry로 남는가?
7. official DART/KIND URL은 exact host만 인정되고 fake path는 계속 막히는가?
8. v32 이후 live diagnostic에서 Tistory fetch_attempt가 줄고 official/report/news original fetch가 늘어나는가?
9. web_or_llm_accepted_claim_count가 0에서 늘더라도 snippet-only나 blog-origin claim은 0으로 유지되는가?
10. FULL_THESIS stage row가 생기면 support_claim_ids, score_contribution_ids, stagecourt_trace_id가 모두 닫히는가?
```

## 다음 패치 방향

P0-G2:

```text
low-quality source rejection feedback을 명시적으로 planner prompt payload에 넣는 regression test 추가.
```

현재는 일반 source rejection feedback 테스트가 있지만,
`web_result_low_quality_blog_or_social_not_score_source`를 특정해서 planner에게 전달되는지까지는 별도 테스트가 약하다.

P0-G3:

```text
trusted news / report / issuer newsroom source lineage를 더 엄격하게 분리.
```

예:

```text
Reuters 원문
  -> source family 1
Naver 재배포
  -> 원문 lineage가 Reuters면 같은 family
블로그 인용
  -> score source 아님
회사 newsroom
  -> issuer official 가능
```

P0-L:

```text
FULL_THESIS refresh queue 85개를 bounded production daily 방식으로 실행.
각 SourceTask는 budget, stop condition, official-first route를 가져야 한다.
```

주의:

```text
85개를 한꺼번에 unbounded web crawl로 처리하면 안 된다.
각 queue row는 source-backed primitive를 닫거나 material pending을 남기는 방향이어야 한다.
```

P0-M:

```text
삼성전자/하이닉스 bounded live smoke를 다시 돌릴 때,
provisional_score와 verified_score를 분리해서 출력.
```

운영 판정은 verified_score만 사용해야 한다.

## 최종 판단

이번 v32 패치는 작지만 필요한 방어선이다.

하지만 이 패치를 운영 준비 완료로 해석하면 안 된다.

현재 상태를 한 줄로 쓰면:

```text
상태판 Stage는 있고, 운영 full-thesis Stage는 아직 없으며,
블로그/소셜성 웹 route가 점수 source로 새어 들어가는 경로 하나를 더 막았다.
```

다음 에이전트는 이 문서의 핵심을 이렇게 검증하면 된다.

```text
1. stage_scope를 먼저 본다.
2. FULL_THESIS row가 0이면 운영 Stage가 없다고 말한다.
3. accepted claim 없이 score가 생긴 row가 있는지 본다.
4. blog/social/source_proxy/snippet-only가 score contribution으로 들어갔는지 본다.
5. v32 source reject가 planner retry로 이어지는지 본다.
```


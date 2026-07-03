# Census v4 0701 Sourcequality v6 Source Router Patch Result

작성 시점: 2026-07-02 KST

## 결론

```text
source router 품질은 개선됐다.
하지만 live web/LLM accepted claim은 여전히 0개다.
운영 FULL_THESIS Stage는 아직 없다.
```

다음 패치 기준 문서:

```text
docs/0701/census_v4_0701_sourcequality_v6_hard_review_and_p0_patch_direction_2026-07-02.md
```

이 문서는 sourcequality-v6의 결과 요약이고,
위 hard-review 문서는 v1~v6 교차검증, 코드상 단절 위치,
all-results-rejected feedback retry 설계, P0 acceptance test까지 포함한다.

쉬운 예:

```text
전에는 종목 시세판, 공시 모음, 사이트 아카이브 같은 종이를 채점 선생님에게 넘겼다.
이제 그런 종이는 더 일찍 버린다.
하지만 아직 좋은 원문 답안지를 충분히 찾아오지는 못했다.
```

## 이번 패치

파일:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
tests/test_research_brain_v4_real_source_acquisition.py
```

변경:

```text
1. web search result를 원문 가능성이 높은 순서로 정렬한다.
2. 대상회사명이 제목에 없는 generic 주요공시/공시뽑기/공시정리 라운드업을 source document로 보지 않는다.
3. sitemap/archive/기사목록 페이지를 source document로 보지 않는다.
4. 같은 URL은 source family를 늘리는 증거가 아니므로 중복 fetch하지 않는다.
5. rejected reason을 leaf에 남긴다.
```

이건 점수 하드코딩이 아니다.

```text
나쁜 방식:
  대웅제약이면 kdpress를 막는다.

이번 방식:
  어떤 종목이든 "대상회사명이 제목에 없는 주요공시 모음"은 원문 evidence가 아니다.
```

## v5와 v6 비교

### sourcequality-v5

```text
output = output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v5
verdict = NOT_READY

brain_accepted_claim_count = 1
official_accepted_claim_count = 1
web_or_llm_accepted_claim_count = 0
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 0

web_search_task_count = 5
web_search_result_count = 35
web_fetched_document_count = 7
web_rejected_document_count = 26
llm_claim_extractor_attempt_count = 7

source_task_realness = LIVE_SOURCE_PASS
```

v5에서 선택된 문제성 URL:

```text
https://biz.heraldcorp.com/sitemap/archive/2020/20200423
https://plumsec.com/ko/report/detail?rcept_no=20260630801612  # 반복 fetch
https://kind.krx.co.kr/common/disclsviewer.do?...              # 반복 fetch
```

### sourcequality-v6

```text
output = output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v6
verdict = NOT_READY

brain_accepted_claim_count = 1
official_accepted_claim_count = 1
web_or_llm_accepted_claim_count = 0
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 0

web_search_task_count = 2
web_search_result_count = 11
web_fetched_document_count = 0
web_rejected_document_count = 11
llm_claim_extractor_attempt_count = 0

source_task_realness = LIVE_SOURCE_PASS
source_task_executions = 98
source_task identity missing count = 0
```

v6 rejection:

```text
web_result_stock_list_or_channel_page_not_source_document = 10
web_result_site_archive_or_sitemap_not_source_document = 1
```

해석:

```text
v6는 나쁜 web source를 더 일찍 막았다.
그래서 이번 live run에서는 web full-source fetch가 0개가 됐다.
즉 source hygiene은 좋아졌지만, LLM planner/query가 좋은 원문을 찾는 능력은 아직 부족하다.
```

## 현재 Stage 상태

v6 기준:

```text
census_stage_status rows = 3391
FULL_THESIS live row = 0
FULL_E2R_100 verified score row = 0
BRAIN_WEB_PARTIAL promoted row = 0
web/LLM accepted claim = 0
```

쉬운 예:

```text
문지기는 더 똑똑해졌다.
하지만 접수창구가 아직 올바른 서류를 못 가져온다.
그래서 합격자는 0명이다.
```

## 통과한 테스트

```text
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_real_source_acquisition -v
  Ran 20 tests / OK

PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_run_mode_honesty -v
  Ran 55 tests / OK

PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate -v
  Ran 20 tests / OK
```

전체 회귀 테스트:

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v

status = OK
test_count = 5024
duration_seconds = 196.2862
artifact sha256 = b0d9032319072e7767c3f929a8da3cd31f5599017a7d0b55f53a64b35d0e3b32
log sha256 = f9dedcbbaf1fb2fde184e15084bdb3e05aae48b073b009ddeef76814b1757273
```

## 아직 막힌 이유

readiness blocker:

```text
Brain/Web acquisition mode requires fetched full-source web/news documents
web/LLM accepted claim count is zero
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED
planner runs minimum not met: 21/30
web search tasks minimum not met: 2/20
web/news search calls minimum not met: 2/20
fetched documents minimum not met: 0/10
claim extractor attempts minimum not met: 0/10
web/LLM accepted claims minimum not met: 0/3
```

핵심:

```text
gate가 잘못 막는 게 아니다.
좋은 웹 원문이 없으니 LLM extractor도 돌 수 없고,
web/LLM accepted claim도 없다.
```

## 다음 패치 방향

### P0. all-results-rejected feedback retry

현재 v6는 모든 web result가 metadata 단계에서 거절됐다.
이때 deterministic query template을 만들면 안 된다.
대신 LLM planner에게 다음 feedback을 넘겨 재계획시켜야 한다.

```text
previous_query
rejection_reason_distribution
selected_source_count = 0
examples:
  web_result_stock_list_or_channel_page_not_source_document
  web_result_site_archive_or_sitemap_not_source_document

instruction:
  이번에는 site archive, stock list, price board가 아니라
  issuer IR, DART/KIND detail, report PDF, company newsroom, trusted article 원문을 찾을 것.
```

쉬운 예:

```text
검색 결과가 전부 전단지였다.
코드가 새 검색어를 하드코딩하지 말고,
LLM에게 "전단지만 나왔으니 다음엔 원문 서류함을 찾아라"라고 피드백해야 한다.
```

### P0. source class retry widening

LLM이 external web만 계속 내면, official/source class 실패 이력을 같이 줘서
`IssuerIR`, `KIND detail`, `ReportPDF`, `TrustedNews` 쪽 source task를 만들게 해야 한다.

금지:

```text
if primitive == volume_growth_visible:
    query = "{company} 신규시설투자 생산능력 IR PDF"
```

허용:

```text
LLM planner가 rejection feedback을 보고 source_task_drafts를 다시 제안한다.
코드는 query safety, as_of_date, target scope, duplicate만 검증한다.
```

### P0. accepted web claim replay fixture

source router가 좋은 원문을 통과시키는지 controlled fixture를 더 만들어야 한다.
단, source_proxy_only 연구자료는 쓰면 안 된다.

필수 fixture:

```text
1. target-specific issuer/news article passes to EvidenceDocument
2. generic roundup rejects
3. archive rejects
4. duplicate URL does not refetch
5. accepted unstructured claim requires LLM extractor output + anchor
```

## 최종 판단

이번 패치는 운영 가능 완료가 아니다.

```text
완료된 것:
  나쁜 웹 source를 더 일찍 거절한다.
  같은 URL 반복 fetch를 막는다.
  source task identity는 유지된다.
  strict gate는 계속 거짓 승격을 막는다.

남은 것:
  rejection feedback을 LLM planner 재계획으로 연결
  좋은 web/IR/report 원문 획득
  LLM extractor accepted claim 생성
  Brain/Web StageCourt trace promotion
  production FULL_THESIS row 생성
```

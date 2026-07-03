# Census v4 0701 Source Quality Live Diagnostic / Cross Validation

작성 시점: 2026-07-02 KST

대상 실행:

```text
canonical output:
  output/census_v4/2026-07-01

latest live diagnostic:
  output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v8

previous live diagnostic:
  output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v7
```

> 2026-07-02 최신 정정:
> 이 문서는 처음 `sourcequality-v1` 기준으로 작성됐고, 이후 `sourcequality-v8`까지 교차검증했다.
> 최신 단일 진실은
> `docs/0701/census_v4_0701_sourcequality_v8_task_budget_split_live_result_and_next_bottleneck_2026-07-02.md`를 먼저 읽는다.
> 그 다음 직전 병목은
> `docs/0701/census_v4_0701_sourcequality_v7_feedback_retry_live_result_and_next_bottleneck_2026-07-02.md`에서 확인한다.
> v6 원인과 P0 패치 의도는
> `docs/0701/census_v4_0701_sourcequality_v6_source_router_patch_result_2026-07-02.md`와
> `docs/0701/census_v4_0701_sourcequality_v6_hard_review_and_p0_patch_direction_2026-07-02.md`로 확인한다.
> 아래의 v1 숫자는 중간 스냅샷으로만 해석한다.

## sourcequality-v8 최신 결론

```text
verdict = NOT_READY
readiness gate = BLOCKED

census_stage_status rows = 3391
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0

Brain/Web:
  brain_accepted_claim_count = 0
  official_accepted_claim_count = 0
  web_or_llm_accepted_claim_count = 0
  brain_stage_trace_count = 0
  brain_promoted_stage_row_count = 0

web activity:
  web_search_tasks = 4
  web_search_results = 31
  web_fetched_documents = 2
  web_rejected_documents = 21
  claim_extractor_runs = 2
  raw_assertion_rejections = 23

planner:
  planner_runs = 22
  feedback_retry_planner_runs = 1
  rejected_claim_feedback_count = 8
  source_rejection_feedback_count = 0
```

해석:

```text
v6 병목:
  source router가 나쁜 검색 결과를 원문 fetch 전에 막았다.
  좋은 원문 fetch와 claim extraction이 거의 없었다.

v7 병목:
  web full-source 9개를 fetch했고 LLM extractor도 9회 실행됐다.
  하지만 추출 claim이 target/directness 또는 primitive mapping에서 전부 탈락했다.
  즉 병목은 "원문을 못 읽음"에서 "읽은 claim이 운영 점수 칸에 못 들어감"으로 이동했다.

v8 병목:
  max_fetches_per_task와 source task count를 분리해 LLM 조사 경로는 더 보존됐다.
  하지만 fetched full-source는 2개이고 accepted brain/web claim은 여전히 0개다.
  즉 병목은 "조사 경로 보존" 이후에도 "score-eligible claim 부재"에 남아 있다.
```

쉬운 예:

```text
v6 = 서류 접수 전 탈락.
v7 = 서류를 읽었지만, 대상 회사 서류가 아니거나 점수 항목 답안이 아니라서 탈락.
v8 = 여러 서류함을 열어 보게 고쳤지만, 채점표에 들어갈 답안은 아직 못 찾음.
```

중요:

```text
v8에서도 운영 Stage가 생긴 것은 아니다.
FULL_THESIS row = 0이고 FULL_E2R_100 verified score row = 0이다.
따라서 "stage가 있는 애들"은 event-board 상태판에는 있지만,
실제 운영 파이프라인에서 쓸 수 있는 full-thesis stage는 아직 없다.
```

## sourcequality-v7 직전 결론

```text
verdict = NOT_READY
readiness gate = BLOCKED

census_stage_status rows = 3391
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0

Brain/Web:
  brain_accepted_claim_count = 0
  official_accepted_claim_count = 0
  web_or_llm_accepted_claim_count = 0
  brain_stage_trace_count = 0
  brain_promoted_stage_row_count = 0

web activity:
  web_search_tasks = 7
  web_search_results = 50
  web_fetched_documents = 9
  web_rejected_documents = 24
  claim_extractor_runs = 9
  raw_assertion_rejections = 56
```

## sourcequality-v6 중간 결론

```text
verdict = NOT_READY
readiness gate = BLOCKED

census_stage_status rows = 3391
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0

Brain/Web:
  brain_accepted_claim_count = 1
  official_accepted_claim_count = 1
  web_or_llm_accepted_claim_count = 0
  brain_stage_trace_count = 1
  brain_promoted_stage_row_count = 0

source task identity:
  source_task_executions = 98
  missing source_class = 0
  missing provider_name = 0
  missing source_task_origin = 0
  missing requested_source_classes = 0
  missing symbol/company/primitive_gap = 0

web activity:
  web_search_tasks = 2
  web_search_results = 11
  web_fetched_documents = 0
  web_rejected_documents = 11
  claim_extractor_runs = 0
```

해석:

```text
source router가 나쁜 결과를 더 일찍 막았다.
하지만 좋은 웹 원문을 못 찾았기 때문에 web/LLM accepted claim은 0개다.
```

쉬운 예:

```text
쓰레기 서류는 접수하지 않게 됐다.
하지만 아직 진짜 서류를 가져오지는 못했다.
```

## sourcequality-v3 중간 결론

```text
verdict = NOT_READY
readiness gate = BLOCKED

census_stage_status rows = 3391
canonical stages:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

stage_scope = CENSUS_EVENT_BOARD only
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0

Brain/Web:
  brain_accepted_claim_count = 0
  official_accepted_claim_count = 0
  web_or_llm_accepted_claim_count = 0
  brain_stage_trace_count = 0
  brain_promoted_stage_row_count = 0

source task identity:
  source_task_executions = 99
  missing source_class = 0
  missing provider_name = 0
  missing source_task_origin = 0
  missing requested_source_classes = 0
  missing symbol/company/primitive_gap = 0

web/LLM activity:
  planner_runs = 22
  llm_prompts = 2
  llm_responses = 2
  web_search_tasks = 4
  web_search_results = 30
  web_fetched_documents = 6
  web_rejected_documents = 30
  claim_extractor_runs = 6
  raw_assertions = 113
  raw_assertion_rejections = 30
```

해석:

```text
source task leaf는 이제 리뷰 가능한 수준으로 정체성이 채워졌다.
하지만 live Brain/Web accepted claim은 0개이므로 운영 Stage 승격은 여전히 없다.
```

쉬운 예:

```text
택배 송장에는 이제 발송지/배송사/받는 사람이 다 적힌다.
하지만 아직 실제로 합격 처리할 물건은 도착하지 않았다.
```

## sourcequality-v1/v2/v3 차이

```text
v1:
  official DART claim 1개가 Brain trace까지 연결됨
  web/LLM accepted claim 0개
  source_task_executions 99개 identity 대부분 누락

v2:
  새 Brain execution 일부 identity는 채움
  기존 baseline/event-board 병합 row 92개 identity 누락 유지

v3:
  병합된 source_task_executions까지 identity backfill 완료
  identity missing count 0
  live accepted claim 0개
```

따라서 최종 결론은 이렇다.

```text
v3는 "성공"이 아니다.
v3는 "왜 아직 성공이 아닌지 추적할 수 있게 된 상태"다.
```

## 직접 답

```text
Stage label이 붙은 row는 있다.
하지만 운영 FULL_THESIS Stage가 끝난 row는 아직 없다.
```

정확한 구분:

```text
canonical census_stage_status rows = 3391

event-board Stage row:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  3-Red = 1
  non-Stage0 event-board row = 85

operational full-thesis Stage:
  FULL_THESIS row = 0
  FULL_E2R_100 verified score row = 0
  verified_score_present = 0
```

쉬운 예:

```text
event-board Stage1:
  "오늘 공시/이벤트가 있어서 watch board에 올렸다"에 가깝다.

FULL_THESIS Stage3-Green:
  "원문 claim -> primitive -> score contribution -> StageCourt까지 끝난 투자 thesis"다.

지금 있는 것은 앞쪽이고, 사용자가 기대한 것은 뒤쪽이다.
```

따라서 지금 상태를 이렇게 말하면 안 된다.

```text
틀린 표현:
  Stage가 85개 생겼으니 운영 가능하다.

맞는 표현:
  event-board 상태 row는 85개 있지만 full-thesis 운영 Stage는 0개다.
```

## sourcequality-v1 결론

`sourcequality-v1`은 `NOT_READY`로 끝났다.

하지만 의미 있는 변화는 있었다.

```text
sourcefilter-v1:
  brain_accepted_claim_count = 0
  official_accepted_claim_count = 0
  web_or_llm_accepted_claim_count = 0
  brain_stage_trace_count = 0
  brain_promoted_stage_row_count = 0

sourcequality-v1:
  brain_accepted_claim_count = 1
  official_accepted_claim_count = 1
  web_or_llm_accepted_claim_count = 0
  brain_stage_trace_count = 1
  brain_promoted_stage_row_count = 0
```

해석:

```text
공식 DART claim 하나는 Brain trace와 StageCourt까지 연결됐다.
하지만 그 claim은 web/LLM accepted claim이 아니고 full-thesis claim도 아니다.
그래서 strict promotion gate가 대표 Stage 승격을 막았다.
```

쉬운 예:

```text
대웅제약 신규시설투자 정정 공시에서
"투자/시행 일정이 있다"는 claim 하나는 확인됐다.

하지만 이것만으로
"생산량 증가가 확인됐다"
"매출/현금흐름으로 이어졌다"
"revision이 붙었다"
까지 말할 수는 없다.

그래서 점수표 전체 thesis가 열린 게 아니다.
```

## sourcequality-v1 중간 숫자

`output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v1/brain_web_readiness_gate_audit.json`

주의:

```text
이 블록은 최신값이 아니다.
최신 Brain/Web 보조 진단은 sourcequality-v7이고,
v1은 source-quality 개선 초기에 "공식 claim 1개는 연결됐지만 web/LLM claim은 0개"였음을 보여 주는 과거 스냅샷이다.
```

```text
verdict = BLOCKED
brain_web_evidence_pass_allowed = false

brain_accepted_claim_count = 1
official_accepted_claim_count = 1
web_or_llm_accepted_claim_count = 0
web_news_accepted_claim_count = 0
llm_extracted_accepted_claim_count = 0

brain_stage_trace_count = 1
brain_promoted_stage_row_count = 0

web_search_task_count = 2
web_search_result_count = 20
web_fetched_document_count = 4
web_rejected_document_count = 7

llm_claim_extractor_attempt_count = 4
llm_planner_call_count = 22
llm_real_provider_success_count = 2

llm_prompts.jsonl = 3 rows
llm_responses.jsonl = 3 rows
planner_raw/prompts/*.json = 3 files
planner_raw/responses/*.json = 3 files
```

Strict gate blockers:

```text
1. web/LLM accepted claim count is zero
2. Brain/Web StageCourt traces are not promoted into census_stage_status
3. brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
4. planner runs minimum not met: 22 / 30
5. web search tasks minimum not met: 2 / 20
6. web/news search calls minimum not met: 2 / 20
7. fetched documents minimum not met: 4 / 10
8. claim extractor attempts minimum not met: 4 / 10
9. web/LLM accepted claims minimum not met: 0 / 3
```

쉬운 예:

```text
숙제 한 장은 제출됐다.
하지만 운영 승격 조건은 "공식/웹/LLM 증거가 여러 개 연결된 묶음"이다.
한 장으로는 대표 성적표에 올리지 않는다.
```

## accepted claim 1개의 정체

`accepted_claims.jsonl` 마지막 Brain claim:

```text
symbol = 069620
company = 대웅제약
claim_id = CLM-c1ad04fdbe2c3dd95418
source_provider = OpenDART
document_id = DOC-4bfe1c4e74db9667d534
anchor_id = ANCH-3e63350e20e67f9247a0
primitive_id = implementation_timeline
source URL = https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801610
```

연결 trace:

```text
brain_to_claim_trace.jsonl rows = 1
stagecourt_trace_id = SCT-BRAIN-7e6e48950d4a47e3af60
score_contribution_ids = 5개
score_status = FINAL
```

하지만 promotion audit:

```text
brain_stage_trace_without_web_or_llm_claim_count = 1
web_or_llm_accepted_claim_count = 0
brain_promoted_stage_row_count = 0
verdict = BLOCKED
```

해석:

```text
이 claim은 "공식 공시 기반 일정 claim"으로는 의미가 있다.
하지만 web/LLM evidence operating path가 성공했다는 증거는 아니다.
그리고 full-thesis Stage를 닫을 만큼의 primitive coverage도 아니다.
```

## Web acquisition cross-check

`web_search_results.jsonl`:

```text
rows = 20
SELECTED_FOR_FETCH = 7
NOT_SELECTED_BUDGET_EXHAUSTED = 13

source:
  Naver webkr = 19
  Naver news = 1

is_news:
  False = 17
  True = 3
```

`web_fetched_documents.jsonl`:

```text
rows = 4

1. kdpress 주요공시 모음
2. KIND 대웅제약 분기보고서 viewer
3. KIND 대웅제약 정정 신규시설투자 viewer
4. ntoday 공시뽑기 기사
```

`web_rejected_documents.jsonl`:

```text
rows = 7

post_extraction_no_score_eligible_claim = 4
live_pdf_text_extraction_failed = 3
```

해석:

```text
웹 fetch 자체는 됐다.
하지만 가져온 문서가 점수 primitive를 채우지 못했거나,
브로커 PDF 텍스트 추출이 실패했다.
```

쉬운 예:

```text
"공시 모음 기사"는 대웅제약 이름이 들어 있어도
대웅제약의 생산량/매출/FCF bridge를 증명하지 못한다.

PDF 리포트가 검색됐어도 텍스트 추출이 실패하면
LLM이 읽을 수 있는 원문 anchor가 없으므로 점수에 쓰면 안 된다.
```

## Raw assertion rejection cross-check

`raw_assertion_rejections.jsonl`:

```text
rows = 25

primitive_mapping_rejected = 15
target_scope_or_directness_rejected = 8
temporal_status_rejected = 2
```

해석:

```text
LLM extractor가 raw assertion은 만들었다.
하지만 대부분이 현재 점수 primitive와 맞지 않거나,
대상회사 직접 claim이 아니거나,
현재성 판단에서 탈락했다.
```

이건 현재 방향에서는 맞는 차단이다.

```text
무조건 점수를 만들려고 했다면 이 25개 중 일부가 억지 accepted claim이 됐을 것이다.
지금은 탈락 사유가 남고 점수로 넘어가지 않는다.
```

## source-quality patch 검증

이번 코드 패치의 핵심:

```text
1. Naver webkr provider URL에 "news"가 들어 있다는 이유만으로 결과를 news로 분류하지 않는다.
2. finance.naver.com / Npay 증권 같은 시세/프로필 페이지는 EvidenceDocument로 넘기지 않는다.
3. 상승률 TOP30, 주식공시정리 채널, 태그 목록, 텔레그램 채널, 스프레드시트 첨부 같은 목록/채널/시세판 결과를 pre-fetch에서 거절한다.
```

관련 코드:

```text
src/e2r/research/search_provider.py
src/e2r/research_brain/v4_source_acquisition_runner.py
tests/test_research_brain_v4_real_source_acquisition.py
```

검증된 테스트:

```text
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_real_source_acquisition -v
Ran 16 tests / OK

PYTHONPATH=src python -m unittest tests.test_sources -v
Ran 14 tests / OK

PYTHONPATH=src python -m unittest \
  tests.test_census_v4_event_separation \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate -v
Ran 23 tests / OK

PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v

status = OK
test_count = 5024
failed_count = 0
error_count = 0
duration_seconds = 196.2862
test_result_artifact_file_sha256 = b0d9032319072e7767c3f929a8da3cd31f5599017a7d0b55f53a64b35d0e3b32
json_internal_log_sha256 = 4c58b02c8c3873752c38114c7db7324f6eea7d5c80117a596b5b5e76f6b66ded
```

주의:

```text
sourcequality-v1 live result에는 새 metadata rejection reason이 대량으로 나타나지는 않았다.
이번 live 검색 결과가 시세판/상승률 목록 페이지를 많이 선택하지 않았기 때문이다.

따라서 패치 검증은 unit regression이 담당하고,
live diagnostic은 "그래도 운영 Stage는 아직 아니다"를 보여 주는 증거로 읽는다.
```

## 왜 아직 문제가 해결된 게 아닌가

### 1. Official-only claim은 Brain/Web pass가 아니다

이번 accepted claim 1개는 OpenDART다.

```text
official_accepted_claim_count = 1
web_or_llm_accepted_claim_count = 0
```

이건 좋은 진전이지만 `BRAIN_WEB_PARTIAL` 승격 조건과는 다르다.

쉬운 예:

```text
DART 공시 한 줄은 출생신고 같은 공식 문서다.
하지만 투자 thesis는 그 뒤의 매출, 물량, 현금흐름, revision까지 이어져야 한다.
```

### 2. Web result quality가 아직 낮다

이번에 fetch된 문서 4개는 대부분 다음 유형이다.

```text
공시 모음 기사
KIND viewer/list HTML
공시뽑기 기사
```

이런 문서들은 이름은 맞아도 primitive를 채우기 어렵다.

필요한 방향:

```text
공시 목록/뷰어 HTML
  -> 상세 원문/첨부/공식 API anchor로 변환

공시 모음 기사
  -> candidate trigger로만 사용
  -> 점수는 공시 원문으로 다시 확인

브로커 PDF
  -> 텍스트 추출 실패 시 score evidence 불가
  -> PDF download/extraction adapter 개선 또는 대체 공식/IR source route 필요
```

### 3. Planner feedback가 source failure를 충분히 다음 검색으로 바꾸지 못한다

현재 blocker는 단순히 "LLM이 멍청하다"가 아니다.

```text
LLM planner prompt/response leaf는 생겼다.
하지만 rejected feedback을 받아도
충분히 다른 source class, 공식 detail source, IR/source route로 회수하지 못했다.
```

다음 패치 방향:

```text
rejection feedback:
  PDF extraction failed
  post extraction no score eligible claim
  KIND viewer/list is not enough
  budget exhausted before useful document

LLM planner가 받아야 할 다음 과제:
  같은 general query 반복 금지
  official detail/IR/company/source route 우선
  primitive를 채우는 데 필요한 원문 유형을 다시 제안
```

### 4. Full-thesis runner가 아직 닫히지 않았다

`FULL_THESIS row = 0`은 여전히 가장 중요한 사실이다.

```text
claim 하나가 StageCourt trace를 만들었다.
하지만 accepted claim set이 full thesis coverage를 만들지는 못했다.
대표 census_stage_status row로 promotion도 되지 않았다.
```

## 다음 패치 방향

### P0. SourceTask leaf 품질 보강

현재 `source_task_executions.jsonl`에서 많은 row의 `source_class`, `provider_name`이 top-level `null`이다.

다음 에이전트가 추적하기 쉽게:

```text
source_class
provider_name
search_provider_name
connector_name
source_task_origin
preferred_source_classes
fallback_source_classes
```

를 source task execution top-level에 남겨야 한다.

쉬운 예:

```text
"NO_EVIDENCE_FOUND"만 보면 어디가 막혔는지 모른다.
"KIND viewer를 읽었지만 detail anchor를 못 만들었다"라고 남아야 고칠 수 있다.
```

### P1. Official detail adapter 개선

이번 run에서 web으로 KIND viewer URL이 들어왔다.

문제:

```text
KIND viewer/list page HTML은 점수 원문으로 약하다.
```

방향:

```text
KIND/OpenDART/KRX URL을 발견하면
  general web document로 처리하지 말고
  official connector/detail fetch route로 reroute한다.

단, title/snippet만으로 점수를 주지 않는다.
반드시 detail text/API/table anchor를 만든다.
```

### P2. PDF extraction failure를 planner feedback로 승격

이번 run:

```text
live_pdf_text_extraction_failed = 3
```

방향:

```text
PDF가 좋은 source일 수는 있다.
하지만 텍스트 추출 실패는 accepted claim 0이다.

planner feedback에는 다음처럼 들어가야 한다.
  "broker PDF found but extraction failed; propose official IR/html/report alternative"
```

절대 하면 안 되는 것:

```text
PDF 제목이 좋아 보인다고 claim을 만든다.
```

### P3. Web quality ranker

나쁜 하드코딩:

```text
if company == "대웅제약": 특정 URL 우대
if primitive == "capacity": 특정 검색어 생성
```

좋은 deterministic source hygiene:

```text
official detail document > issuer IR > broker PDF with extractable text > tier news original
공시 모음 기사 < 공식 detail
시세/프로필/목록/태그/channel page = score source 불가
```

이건 종목별 하드코딩이 아니라 source class 품질 규칙이다.

### P4. LLM planner retry contract 강화

LLM에게 점수나 Stage를 묻지 않는다.

LLM에게 물어야 할 것:

```text
이전 source attempts:
  - 어떤 문서를 읽었는가
  - 왜 탈락했는가
  - 어떤 primitive가 아직 UNKNOWN인가

다음 source tasks:
  - 어떤 source class로 갈 것인가
  - 왜 그 source가 이 primitive에 맞는가
  - 기존 실패 query와 어떻게 다른가
```

코드는:

```text
as_of_date
target scope
중복 query
source quality
무제한 fetch 금지
```

만 검증하고 실행한다.

### P5. FULL_THESIS 승격은 끝까지 보수적으로 유지

이번 run에서 strict gate가 막은 것은 맞다.

다음 패치가 해서는 안 되는 일:

```text
official claim 1개가 있으니 BRAIN_WEB_PARTIAL로 승격
StageCourt trace 1개가 있으니 FULL_THESIS로 승격
web fetched document가 있으니 accepted claim으로 간주
```

다음 패치가 해야 할 일:

```text
web/LLM accepted claim >= 3
score contribution support claim 모두 resolve
StageCourt trace와 contribution id 연결
representative census row promotion id 연결
FULL_E2R_100 score scope 확인
```

## Cross-validation checklist for next agent

다음 에이전트는 최소한 아래를 공격적으로 확인해야 한다.

```text
1. sourcequality-v1 accepted claim 1개가 정말 OpenDART인지
2. 그 claim이 web_or_llm accepted로 잘못 집계되지 않는지
3. Brain StageCourt trace 1개가 representative row로 promotion되지 않았는지
4. FULL_THESIS row가 여전히 0인지
5. EVENT_WEIGHTED_PARTIAL 67개가 FULL_E2R_100으로 오해되지 않는지
6. CensusAssessmentEvent / CandidateEvent가 score evidence로 쓰이지 않았는지
7. web fetched document 4개가 왜 accepted claim이 안 됐는지
8. PDF extraction failure가 claim으로 둔갑하지 않았는지
9. Naver webkr provider URL 때문에 is_news가 오염되지 않는지
10. 시세/프로필/목록 페이지가 EvidenceDocument로 넘어가지 않는지
11. source_task_executions의 top-level source_class/provider_name null이 감사 장애인지
12. planner retry가 rejected feedback을 실제 새 source route로 바꾸는지
13. all-archetype source-backed replay ready가 여전히 6/32인지
14. source_proxy_only 자료가 운영 점수로 들어가지 않았는지
15. 같은 run을 다시 돌렸을 때 claim id가 증식하지 않는지
```

## Reproduction command

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v1 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --research-brain-report-dir docs/operational \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 1 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-fetches-per-task 1 \
  --brain-claim-extractor-provider codex_cli \
  --brain-stage-promotion-mode strict \
  --full-thesis-smoke-mode disabled \
  --target-gate brain_web \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim false \
  --fail-on-atomic-mismatch false \
  --fail-on-semantic-guard false \
  --fail-on-critical-audit false \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --write-operational-docs false
```

Expected:

```text
exit code = 1
stdout = NOT_READY
```

이 실패는 정상적인 차단이다.

```text
운영 Stage가 아직 없는데 READY라고 하면 안 된다.
```

## 현재 완료/미완료 판정

완료된 것:

```text
1. event-board Stage와 full-thesis Stage를 분리해서 감사한다.
2. CensusAssessmentEvent/CandidateEvent score leakage critical counter가 0이다.
3. Planner prompt/response leaf가 남는다.
4. LLM extractor run과 raw assertion rejection이 남는다.
5. 공식 DART claim 하나가 Brain trace까지 연결되는 path가 관측됐다.
6. web/LLM accepted claim이 0이면 strict promotion이 막힌다.
7. 시세/프로필/목록 페이지 source hygiene regression test가 생겼다.
```

미완료:

```text
1. FULL_THESIS production row = 0
2. FULL_E2R_100 verified score row = 0
3. web_or_llm_accepted_claim_count = 0
4. all-archetype source-backed replay ready = 6 / 32
5. missing required archetype = 26
6. Brain/Web operational minimum gate 미달
7. source task leaf의 source_class/provider_name 감사성이 약함
8. official detail reroute, PDF extraction fallback, planner retry 품질 개선 필요
```

최종 결론:

```text
현재 시스템은 "잘못된 Stage를 올리지 않는 안전장치"는 점점 좋아지고 있다.
하지만 "실제 운영 full-thesis Stage를 충분히 만들어 내는 능력"은 아직 부족하다.

다음 패치는 Stage label을 더 많이 찍는 작업이 아니다.
source route -> readable document -> accepted claim -> primitive -> contribution -> StageCourt -> promoted FULL_THESIS row
이 체인을 실제 source-backed로 닫는 작업이어야 한다.
```

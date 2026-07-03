# Census v4 0701 Stage Presence / Sourcequality v3 Final Review Packet

작성 시점: 2026-07-02 KST

이 문서는 다음 에이전트가 강하게 반박 리뷰할 수 있도록 현재 상태를 숨기지 않고 정리한 최신 패킷이다.

> 2026-07-02 추가 주의:
> 이 문서는 `sourcequality-v3` 기준으로 작성된 stage/scope 리뷰 패킷이다.
> 최신 source router 패치 결과와 Brain/Web 진단 숫자는
> `docs/0701/census_v4_0701_sourcequality_v6_source_router_patch_result_2026-07-02.md`를 먼저 읽는다.

## 한 줄 결론

```text
Stage label은 있다.
하지만 운영 live pipeline에서 FULL_THESIS Stage를 닫은 종목은 아직 없다.
```

정확히는 세 층을 분리해야 한다.

```text
1. CENSUS_EVENT_BOARD
   전 종목 상태판이다. Stage0/Stage1/Stage2-Watch/Red가 여기 찍힌다.

2. FULL_THESIS controlled smoke
   삼성전자/하이닉스 URL-backed fixture로 배선만 검증한 테스트 행이다.
   운영 live evidence 성공이 아니다.

3. FULL_THESIS production/live
   실제 운영으로 원문 수집 -> claim -> primitive -> score -> StageCourt까지 닫힌 행이다.
   현재 live diagnostic 기준 0개다.
```

쉬운 예:

```text
출석부에 "검사 완료" 도장이 찍힌 학생은 많다.
하지만 졸업시험 전체 채점지가 완성된 학생은 아직 없다.

Stage0/Stage1/Stage2-Watch event-board row는 출석부/상태판이고,
FULL_THESIS production row가 졸업시험 채점지다.
```

## 사용한 산출물

```text
canonical output:
  output/census_v4/2026-07-01

latest Brain/Web live diagnostic:
  output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v3

controlled full-thesis smoke unit output:
  output/test_census_v4_cached

full unittest artifact:
  output/test_full_repo_0701/full_unittest_result_artifact.json
```

중요:

```text
sourcequality-v3는 Brain/Web live diagnostic이다.
controlled smoke는 단위 테스트용 URL-backed fixture replay다.
두 결과를 합쳐서 "운영 FULL_THESIS가 있다"고 말하면 안 된다.
```

## 직접 답: Stage가 있는 애들이 있나?

있다. 다만 범위가 다르다.

### sourcequality-v3 live diagnostic

`output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v3/census_stage_status.jsonl`

```text
rows = 3391

canonical_stage_distribution:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391

FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
verified_score_present_count = 0
```

해석:

```text
전 종목 상태판 Stage는 있다.
하지만 sourcequality-v3 live diagnostic에서 종합 thesis Stage는 없다.
```

쉬운 예:

```text
Stage0:
  "이번 census에서 현재 catalyst가 없음"이라는 상태다.
  "100점 만점 E2R에서 0점"이라는 뜻이 아니다.

Stage1/Stage2-Watch:
  "공식 이벤트나 일부 material claim이 있어 watch board에 올림"이다.
  "Green/Yellow thesis가 완성됨"이라는 뜻이 아니다.
```

### controlled full-thesis smoke unit output

`output/test_census_v4_cached/census_stage_summary.json`

```text
stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3389
  FULL_THESIS = 2

FULL_E2R_100 row = 2
stage_distribution:
  Stage2-Watch = 31
  Stage3-Yellow = 1
```

해석:

```text
삼성전자/하이닉스 C06 URL-backed fixture smoke가 FULL_THESIS 배선을 검증했다.
하지만 이건 production/live row가 아니다.
```

쉬운 예:

```text
시험지 채점 프로그램이 동작하는지 샘플 답안지 2개로 확인한 것이다.
그 샘플 답안지가 오늘 운영에서 실제로 제출된 답안지는 아니다.
```

`full_thesis_production_audit.json`도 같은 결론이다.

```text
verdict = PENDING_FULL_THESIS_PRODUCTION
production_full_thesis_row_count = 0
blocker = production_full_thesis_not_requested_or_no_rows
```

## sourcequality-v1/v2/v3 교차검증

### v1

```text
brain_accepted_claim_count = 1
official_accepted_claim_count = 1
web_or_llm_accepted_claim_count = 0
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 0

web_search_task_count = 2
web_search_result_count = 20
web_fetched_document_count = 4
web_rejected_document_count = 7
llm_claim_extractor_attempt_count = 4

source_task_executions = 99
source task identity missing:
  source_class = 99
  provider_name = 99
  source_task_origin = 99
  requested_source_classes = 99
```

해석:

```text
공식 DART claim 하나가 Brain trace까지 연결됐지만 web/LLM claim은 0개였다.
또 source_task_executions의 정체성 필드가 대부분 비어 있어 리뷰가 어렵다.
```

### v2

```text
brain_accepted_claim_count = 1
official_accepted_claim_count = 1
web_or_llm_accepted_claim_count = 0
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 0

web_search_task_count = 3
web_search_result_count = 25
web_fetched_document_count = 4
web_rejected_document_count = 23
llm_claim_extractor_attempt_count = 4

source_task_executions = 98
source task identity missing:
  source_class = 92
  provider_name = 92
  source_task_origin = 92
  requested_source_classes = 92
```

해석:

```text
새 Brain 쪽 source task 일부에는 정체성이 붙었지만,
기존 baseline/event-board에서 병합된 92개 execution row는 여전히 비어 있었다.
```

### v3

```text
brain_accepted_claim_count = 0
official_accepted_claim_count = 0
web_or_llm_accepted_claim_count = 0
brain_stage_trace_count = 0
brain_promoted_stage_row_count = 0

web_search_task_count = 4
web_search_result_count = 30
web_fetched_document_count = 6
web_rejected_document_count = 30
llm_claim_extractor_attempt_count = 6

source_task_executions = 99
source task identity missing:
  source_class = 0
  provider_name = 0
  source_task_origin = 0
  requested_source_classes = 0
  symbol = 0
  company_name = 0
  primitive_gap = 0
```

해석:

```text
source task identity backfill은 고쳐졌다.
하지만 Brain/Web accepted claim은 live 실행 결과 0개라 promotion은 계속 막혔다.
```

이건 단순 퇴보로만 보면 안 된다.

```text
v1은 공식 claim 하나를 잡았다.
v3은 같은 live source 조건에서 accepted claim이 0개였다.

하지만 두 실행 모두 운영 FULL_THESIS 승격은 0개다.
따라서 결론은 동일하다.
  "아직 live Brain/Web path가 운영 stage를 닫지 못한다."
```

쉬운 예:

```text
v1에서는 숙제 한 장을 제출했지만 졸업 조건 미달이었다.
v3에서는 숙제를 하나도 제출하지 못했다.
둘 다 졸업자는 0명이다.
차이는 "왜 졸업자가 0명인지"를 더 잘 추적할 수 있게 된 점이다.
```

## sourcequality-v3 readiness blocker

`brain_web_readiness_gate_audit.json`

```text
verdict = BLOCKED
run_mode = BRAIN_AND_WEB_ACQUISITION_ENABLED

blockers:
  Brain/Web accepted claim count is zero
  web/LLM accepted claim count is zero
  Brain/Web StageCourt traces are not promoted into census_stage_status
  brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
  planner runs minimum not met: 22 / 30
  web search tasks minimum not met: 4 / 20
  web/news search calls minimum not met: 4 / 20
  fetched documents minimum not met: 6 / 10
  claim extractor attempts minimum not met: 6 / 10
  web/LLM accepted claims minimum not met: 0 / 3
```

가장 중요한 blocker는 이것이다.

```text
web_or_llm_accepted_claim_count = 0
```

쉬운 예:

```text
검색하고, 웹페이지를 열고, LLM extractor도 시도했다.
하지만 점수표 칸에 넣을 수 있는 원문 claim은 하나도 통과하지 못했다.
그래서 낮은 점수로 확정하지 않고 NOT_READY로 막는 것이 맞다.
```

## Web acquisition / rejection 현실

`sourcequality-v3` leaf count:

```text
web_search_tasks = 4
web_search_results = 30
web_fetched_documents = 6
web_rejected_documents = 30
claim_extractor_runs = 6
raw_assertions = 113
raw_assertion_rejections = 30
llm_prompts = 2
llm_responses = 2
planner_runs = 22
```

`web_rejected_documents.jsonl` 주요 사유:

```text
web_result_stock_list_or_channel_page_not_source_document = 18
post_extraction_no_score_eligible_claim = 6
live_fetch_failed:ConnectionResetError = 5
web_fetch_target_not_in_title_snippet_or_lead = 1
```

해석:

```text
검색 결과 상당수가 종목 리스트/채널/시세성 페이지다.
이런 페이지는 회사 이름이 있어도 사업 claim 원문이 아니다.
```

쉬운 예:

```text
네이버 증권 시세 페이지에 "삼성전자"가 있다.
그건 현재가/거래량 화면이지,
"HBM 고객 allocation이 확인됐다"는 증거가 아니다.

따라서 extractor로 보내서 억지 claim을 만들면 안 되고,
source acquisition 단계에서 거절하는 게 맞다.
```

## 이번 코드 패치로 확인된 것

### 1. Naver webkr is_news 오분류 수정

패치:

```text
src/e2r/research/search_provider.py
```

검증:

```text
test_naver_webkr_provider_url_does_not_make_result_news ... ok
```

의미:

```text
Naver web 검색 provider URL에 naver.com이 들어간다는 이유만으로
모든 webkr 결과를 news로 보지 않는다.
```

### 2. 종목 시세/프로필/리스트 페이지 source rejection

패치:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
tests/test_research_brain_v4_real_source_acquisition.py
```

검증:

```text
test_live_full_bounded_rejects_stock_quote_profile_page_even_with_target ... ok
test_live_full_bounded_rejects_stock_list_result_before_fetch ... ok
```

의미:

```text
가격판, 종목 프로필, 종목 리스트, 텔레그램/채널성 페이지를
사업 증거 문서로 extractor에 넘기지 않는다.
```

### 3. source_task_executions identity backfill

패치:

```text
src/e2r/research_brain/v4_schemas.py
src/e2r/research_brain/v4_evidence_extraction_bridge.py
src/e2r/census/census_runner_v4.py
src/e2r/production/official_live_shadow.py
tests/test_census_v4_brain_bundle_export.py
```

검증:

```text
sourcequality-v3 source_task_executions = 99
missing source_class = 0
missing provider_name = 0
missing source_task_origin = 0
missing requested_source_classes = 0
missing symbol = 0
missing company_name = 0
missing primitive_gap = 0
```

의미:

```text
source task가 어떤 회사, 어떤 primitive gap, 어떤 source class/provider로 실행됐는지
이제 leaf row만 보고도 추적할 수 있다.
```

### 4. controlled smoke replay source identity

패치:

```text
src/e2r/census/census_runner_v4.py
```

검증:

```text
tests.test_census_v4_goal_required_audits
tests.test_census_v4_source_task_satisfaction_chain
```

결과:

```text
Ran 8 tests / OK

output/test_census_v4_cached/source_task_realness_audit.json:
  verdict = PASS_LEDGER_REFRESH_REALNESS
  critical_count = 0
  classification_distribution:
    EXISTING_ACCEPTED_CLAIM_LIFECYCLE_REFRESH = 32
    FRESH_PROVIDER_CACHE = 60
    URL_BACKED_FULL_THESIS_SMOKE_REPLAY = 14
```

의미:

```text
삼성전자/하이닉스 controlled smoke replay 14개 source task가
source_class=URL_BACKED_FIXTURE, provider_name=ControlledFixtureReplay로 분리된다.
따라서 live fetch로 과장되지 않는다.
```

## 현재까지 통과한 타깃 테스트

```text
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_bundle_export -v
  Ran 7 tests / OK

PYTHONPATH=src python -m unittest tests.test_census_v4_goal_required_audits tests.test_census_v4_source_task_satisfaction_chain -v
  Ran 8 tests / OK

PYTHONPATH=src python -m unittest tests.test_research_brain_v4_real_source_acquisition tests.test_research_brain_v4_operational_modes tests.test_census_v4_run_mode_honesty -v
  Ran 51 tests / OK

PYTHONPATH=src python -m unittest tests.test_sources -v
  Ran 14 tests / OK
```

전체 회귀 테스트:

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v

status = OK
test_count = 5013
duration_seconds = 194.464
artifact sha256 = f660f28b2123bec95304766388ee439dcce2a71876fa8ece334a8113c6e2ce72
log sha256 = fa82cac1ca2b3195f9d619cb2bd4a87f5f7feff8949e2ee986240dd8ac9ec3d0
```

## 지금 잘못되고 있는 핵심

### 문제 1. 상태판 Stage와 운영 Stage가 계속 섞인다

현재 row는 대부분 다음 범위다.

```text
stage_scope = CENSUS_EVENT_BOARD
score_scope = NO_SCORE 또는 EVENT_WEIGHTED_PARTIAL
operator_stage_use = NOT_FULL_THESIS_STAGE
```

이걸 운영 Stage처럼 말하면 안 된다.

쉬운 예:

```text
"공시가 하나 있어서 Stage2-Watch"는 watch board다.
"C06 thesis가 Yellow/Green"은 full thesis다.
두 개는 같은 Stage 숫자처럼 보여도 의미가 다르다.
```

### 문제 2. live Brain/Web claim 생산이 아직 없다

sourcequality-v3 기준:

```text
web_or_llm_accepted_claim_count = 0
brain_stage_trace_count = 0
brain_promoted_stage_row_count = 0
```

이 말은 LLM을 호출하지 않았다는 뜻이 아니다.

```text
llm_prompts = 2
llm_responses = 2
claim_extractor_runs = 6
raw_assertions = 113
```

LLM/extractor는 움직였지만, admissible claim으로 닫히지 못했다.

쉬운 예:

```text
면접은 봤다.
하지만 합격 판정을 받은 지원자가 없다.
```

### 문제 3. source route가 아직 너무 약하다

거절 사유를 보면 source quality 문제가 크다.

```text
종목 리스트/채널 페이지 = 18
score eligible claim 없음 = 6
fetch 실패 = 5
target scope 실패 = 1
```

즉 현재는 LLM claim extractor만 개선해도 부족하다.
먼저 extractor에 들어가는 문서가 진짜 원문이어야 한다.

쉬운 예:

```text
좋은 채점 선생님을 붙여도,
시험지가 아니라 종목 시세판을 주면 답안을 만들 수 없다.
```

### 문제 4. official-first detail extraction이 아직 운영 완성도가 낮다

sourcequality-v1에서는 OpenDART 공식 claim 하나가 잡혔다.
sourcequality-v3에서는 live accepted claim이 0개다.

이 변동 자체가 문제다.
같은 run이 exact replay는 아니지만, 운영형으로는 다음이 필요하다.

```text
official candidate event
-> detail document fetch
-> anchor
-> raw assertion
-> accepted claim
-> primitive
-> score contribution
-> StageCourt trace
```

이 사슬이 흔들리면 Stage가 계속 변한다.

## 다음 패치 방향

### P0. source acquisition을 "진짜 원문 우선"으로 더 강하게 만든다

목표:

```text
검색 결과 30개 중 리스트/채널/시세판 18개 같은 낭비를 줄인다.
```

해야 할 일:

```text
1. Naver/KRX/KIND/DART result ranker에 source document score를 둔다.
2. 회사명 포함 여부만 보지 말고 title/snippet URL path가 원문형인지 먼저 본다.
3. finance quote/profile/list/channel은 fetch 전 reject한다.
4. official source로 풀 수 있는 primitive는 general web fallback을 늦춘다.
5. fetch 실패와 no-score-eligible claim을 planner feedback에 구조화해서 돌려준다.
```

하지 말아야 할 일:

```text
특정 종목명 예외를 넣지 않는다.
"삼성전자는 이런 URL 허용" 같은 코드는 금지다.
```

### P0. official detail document path를 닫는다

목표:

```text
DART/KIND/IR/CompanyGuide로 풀 수 있는 claim은 general web보다 먼저 닫는다.
```

해야 할 일:

```text
1. OpenDART list-only 공시를 detail 문서 없이 claim으로 쓰지 않는다.
2. detail document XML/HTML/PDF fetch 실패 시 source task는 ProviderPending으로 남긴다.
3. detail 성공 시 EvidenceDocument/EvidenceAnchor를 반드시 만든다.
4. accepted claim이 없으면 score contribution을 만들지 않는다.
```

쉬운 예:

```text
"단일판매공급계약체결" 목록 제목만 봤다.
  -> CandidateEvent는 가능.

계약 상대방, 금액, 기간, 현재성이 원문 anchor로 확인됐다.
  -> accepted claim과 점수 가능.
```

### P0. LLM planner retry를 rejection reason 중심으로 강화한다

현재 LLM이 할 일:

```text
점수를 직접 부르는 게 아니라,
왜 이전 문서가 탈락했는지를 보고 다음에 어떤 원문을 찾아야 하는지 query/task를 제안한다.
```

입력해야 할 feedback:

```text
web_result_stock_list_or_channel_page_not_source_document
post_extraction_no_score_eligible_claim
target_scope_or_directness_rejected
temporal_status_rejected
primitive_mapping_rejected
fetch_failed
```

쉬운 예:

```text
이전 검색이 종목 시세판만 가져왔다.
LLM은 다음 round에서 "회사 IR PDF", "DART 정정공시 원문", "컨콜 transcript"처럼
원문성이 높은 경로를 찾아야 한다.
```

코드가 하면 안 되는 일:

```text
if primitive_gap == contract_quality:
    query = "{company} 장기공급계약 선수금"
```

이건 다시 deterministic query 하드코딩으로 돌아가는 길이다.

### P0. promotion gate는 절대 완화하지 않는다

현재 strict gate가 막은 것은 좋은 신호다.

```text
web/LLM accepted claim = 0
Brain/Web promoted row = 0
```

이 상태에서 gate를 낮추면 다시 다음 문제가 생긴다.

```text
검색했다 = 점수
LLM이 말해줬다 = 점수
공시 제목이 있다 = Stage2/Yellow
```

쉬운 예:

```text
문을 못 통과한다고 문턱을 없애면,
가짜 증거가 Green으로 들어온다.
지금은 문턱을 유지하고 증거 작성 능력을 고쳐야 한다.
```

### P1. full-thesis production runner를 controlled smoke에서 live로 확장한다

현재:

```text
controlled smoke:
  삼성전자/하이닉스 URL-backed fixture -> FULL_THESIS 2개

production live:
  production_full_thesis_row_count = 0
```

다음 단계:

```text
1. controlled smoke fixture 없이도 source task가 직접 원문을 찾는다.
2. C06 primitive coverage를 source-backed claim으로 채운다.
3. verified_score와 score_interval을 만든다.
4. StageCourt가 FULL_THESIS row를 대표 출력에 올린다.
5. source task identity와 claim delta audit이 모두 남는다.
```

### P1. all archetype source-backed replay 확대

현재 all archetype matrix 요약:

```text
required_archetype_count = 32
source_backed_ready_count = 6
guard_replay_ready_count = 6
missing_required_archetype_count = 26
```

방향:

```text
C06/C08/C15/C17/C24/C28처럼 source-backed replay가 붙은 축을 늘린다.
source_proxy_only 연구자료는 운영 점수 정답으로 쓰지 않는다.
```

쉬운 예:

```text
연구 md에 "좋은 사례"라고 적혀 있어도,
원문 URL/anchor/claim이 없으면 production score fixture가 아니다.
```

## 리뷰어가 공격해야 할 체크리스트

다음 질문에 하나라도 답이 불명확하면 완료가 아니다.

```text
1. 이 Stage row의 stage_scope는 CENSUS_EVENT_BOARD인가 FULL_THESIS인가?
2. 이 score는 FULL_E2R_100인가 EVENT_WEIGHTED_PARTIAL인가?
3. nonzero score contribution이 support_claim_ids를 갖는가?
4. support_claim_ids가 accepted_claims.jsonl에 실제 존재하는가?
5. accepted claim이 EvidenceDocument/EvidenceAnchor를 갖는가?
6. source task execution에 symbol/company/primitive/source_class/provider/requested_source_classes가 있는가?
7. source task가 live fetch인지, provider cache인지, URL-backed fixture replay인지 구분되는가?
8. web/LLM accepted claim count가 0인데 Brain/Web PASS라고 쓰지 않았는가?
9. controlled smoke FULL_THESIS 2개를 production FULL_THESIS처럼 말하지 않았는가?
10. Stage0을 "나쁜 종목 0점"으로 해석하지 않았는가?
11. CandidateEvent를 score evidence로 쓴 흔적이 없는가?
12. source_proxy_only/evidence_url_pending 자료가 production score로 들어가지 않았는가?
13. old diagnostic v1/v2 숫자를 latest v3 숫자로 착각하지 않았는가?
14. gate를 통과시키려고 threshold를 낮추지 않았는가?
15. LLM query 생성 실패를 deterministic query template 추가로 덮지 않았는가?
```

## 현재 완료로 말할 수 있는 것

```text
1. CensusAssessmentEvent와 CandidateEvent를 score evidence로 쓰지 않는 audit은 유지되고 있다.
2. event-board Stage와 full-thesis Stage scope는 분리되어 있다.
3. sourcequality-v3 기준 source_task_executions identity 누락은 0이다.
4. source quote/profile/list/channel page를 evidence document로 넘기는 일부 경로는 차단됐다.
5. controlled smoke replay는 live fetch로 과장되지 않도록 URL_BACKED_FIXTURE로 분류된다.
6. 타깃 테스트 80개가 통과했다.
```

## 아직 완료로 말하면 안 되는 것

```text
1. live Brain/Web accepted claim 생산 성공
2. live Brain/Web StageCourt trace promotion
3. production FULL_THESIS row 생성
4. live FULL_E2R_100 verified score 생성
5. Samsung/Hynix live operating pipeline Stage 확정
6. 전 아키타입 source-backed replay parity
7. 웹/LLM claim extraction이 운영 최소 수량을 만족한다는 주장
```

쉬운 예:

```text
"소방훈련 통과"와 "실제 화재 대응 완료"는 다르다.
controlled smoke는 소방훈련이다.
production live FULL_THESIS가 실제 대응이다.
```

## 다음 실행에서 기대하는 성공 형태

정상 성공은 숫자가 이렇게 바뀌어야 한다.

```text
brain_web_readiness_gate_audit:
  verdict = PASS 또는 evidence pass allowed true
  web_or_llm_accepted_claim_count >= 3
  brain_stage_trace_count > 0
  brain_promoted_stage_row_count > 0
  operational minimum counts satisfied

census_stage_summary:
  stage_scope_distribution에 FULL_THESIS row가 live/prod 근거로 존재
  score_scope_distribution에 FULL_E2R_100 row 존재
  operator_stage_use_distribution에 FULL_THESIS_STAGE row 존재

source_task_realness_audit:
  live_source_pass_allowed는 실제 REAL_PROVIDER_FETCH claim이 있을 때만 true
  URL_BACKED_FULL_THESIS_SMOKE_REPLAY는 live fetch로 카운트하지 않음
```

그리고 실패 시에도 이렇게 남아야 한다.

```text
ProviderPending:
  source가 막혀서 판단 보류

NoCurrentCatalyst:
  전 종목 census는 했지만 현재 catalyst 없음

PendingMaterialGaps:
  claim 일부는 있으나 Stage 경계에 필요한 primitive가 부족

NOT_READY:
  운영 proof를 과장하지 않고 차단
```

## 최종 판단

현재 시스템은 예전처럼 아무 문서나 읽고 점수를 붙이는 방향으로는 많이 막혔다.
하지만 아직 반대쪽 문제가 남아 있다.

```text
가짜 승격은 막고 있다.
진짜 승격을 만들지는 못하고 있다.
```

그래서 다음 패치의 핵심은 threshold 완화가 아니다.

```text
1. source router가 진짜 원문을 더 잘 찾게 한다.
2. LLM planner가 rejection reason을 보고 다음 source task를 더 정확히 제안하게 한다.
3. official detail document -> anchor -> accepted claim 사슬을 안정화한다.
4. 그 claim이 primitive와 score contribution으로 이어질 때만 FULL_THESIS로 승격한다.
```

이 상태를 쉽게 말하면:

```text
문지기는 생겼다.
이제 진짜 서류를 제대로 가져오는 접수창구를 고쳐야 한다.
```

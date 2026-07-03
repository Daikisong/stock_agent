# Census v4 0701 Sourcequality v6 Hard Review / P0 Patch Direction

작성 시점: 2026-07-02 KST

대상:

```text
canonical output:
  output/census_v4/2026-07-01

latest Brain/Web live diagnostic:
  output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v6

latest full unittest artifact:
  output/test_full_repo_0701/full_unittest_result_artifact.json
```

## 한 줄 결론

```text
Stage label이 붙은 종목은 있다.
하지만 운영 FULL_THESIS Stage가 끝난 종목은 아직 없다.
```

쉬운 예:

```text
전 종목 건강검진 접수표에는 "정상/주의/재검" 같은 상태가 붙었다.
하지만 정밀검사, 원문서류 확인, 의사 판정까지 끝난 최종 진단서는 아직 0장이다.
```

현재 숫자로 쓰면 이렇다.

```text
event-board stage rows = 3391
non-Stage0 event-board rows = 85

FULL_THESIS rows = 0
FULL_E2R_100 verified score rows = 0
web/LLM accepted claims = 0
brain-promoted stage rows = 0
```

따라서 다음 표현은 금지한다.

```text
틀린 표현:
  Stage가 85개 있으니 운영 Stage가 있다.

맞는 표현:
  상태판 Stage는 85개 non-Stage0가 있지만,
  운영 full-thesis Stage는 0개다.
```

## 지금 시스템이 잘하는 것과 못하는 것

잘하는 것:

```text
1. CensusAssessmentEvent와 CandidateEvent를 score evidence로 바로 쓰지 않는다.
2. nonzero ScoreContribution은 support claim을 갖고 있다.
3. FULL_THESIS와 EVENT_BOARD stage scope를 분리한다.
4. web/LLM accepted claim이 0이면 strict promotion을 막는다.
5. stock list, channel, archive, sitemap 같은 페이지를 source document로 조기 거절한다.
6. source_task_execution identity 누락은 최신 v6에서 0개다.
```

못하는 것:

```text
1. 좋은 web/news/IR 원문을 아직 가져오지 못한다.
2. v6에서는 web result 11개가 전부 metadata 단계에서 거절되어 fetch가 0개다.
3. fetch가 0개라 LLM claim extractor도 0회다.
4. claim extractor가 0회라 web/LLM accepted claim도 0개다.
5. all-results-rejected 상황을 LLM planner에게 되돌려 재계획시키는 루프가 없다.
6. source-backed replay ready는 required 32개 중 6개뿐이다.
```

쉬운 예:

```text
문지기는 좋아졌다.
전단지, 시세표, 사이트 목차 같은 것은 이제 문 앞에서 잘 막는다.

그런데 접수 담당자가 아직 진짜 서류함을 못 찾는다.
그래서 최종 합격자는 계속 0명이다.
```

## 교차검증 1: canonical output 상태

원본:

```text
output/census_v4/2026-07-01/census_stage_status.jsonl
output/census_v4/2026-07-01/acceptance_report.md
output/census_v4/2026-07-01/readiness_verdict.json
```

집계:

```text
census_stage_status rows = 3391

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391
  FULL_THESIS = 0

canonical_stage_distribution:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

score_scope_distribution:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

assessment_depth_distribution:
  CHEAP_BASELINE = 3309
  VERIFIED_STAGE = 67
  OFFICIAL_LIGHT = 15
```

해석:

```text
Stage0 3306개:
  "현재 catalyst가 확인되지 않은 상태판 row"다.
  "100점 만점에서 0점 받은 나쁜 종목"이 아니다.

Stage1/Stage2/3-Red 85개:
  공식 이벤트나 candidate event가 있어서 watch board에 올라온 row다.
  full-thesis score/stage가 아니다.

EVENT_WEIGHTED_PARTIAL 67개:
  이벤트 가중 상태 점수다.
  FULL_E2R_100 verified score가 아니다.
```

## 교차검증 2: sourcequality-v1~v6 변화

원본:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v1
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v2
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v3
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v4
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v5
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v6
```

요약표:

```text
run   brain accepted  official accepted  web/LLM accepted  stage trace  promoted  web tasks  web results  fetched  rejected  extractor
v1    1               1                  0                 1            0         2          20           4        7         4
v2    1               1                  0                 1            0         3          25           4        23        4
v3    0               0                  0                 0            0         4          30           6        30        6
v4    0               0                  0                 0            0         5          46           6        46        6
v5    1               1                  0                 1            0         5          35           7        26        7
v6    1               1                  0                 1            0         2          11           0        11        0
```

해석:

```text
1. web/LLM accepted claim은 v1부터 v6까지 계속 0개다.
2. v1/v2/v5/v6의 accepted claim 1개는 official DART claim이다.
3. v6는 나쁜 web result를 더 일찍 거절해서 fetched document가 0개가 됐다.
4. v6의 실패는 "LLM extractor가 틀렸다"가 아니라 "extractor까지 갈 좋은 원문이 없다"에 가깝다.
```

쉬운 예:

```text
v5:
  나쁜 서류도 접수창구 안까지 들어왔다가 나중에 탈락했다.

v6:
  나쁜 서류를 문 앞에서 막았다.
  대신 좋은 서류가 아직 하나도 안 들어왔다.
```

## 교차검증 3: v6 최신 readiness blocker

원본:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v6/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v6/brain_stage_promotion_audit.json
```

핵심 숫자:

```text
brain_web_readiness_gate = BLOCKED
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
source_task_execution_count = 6
```

blocker:

```text
Brain/Web acquisition mode requires fetched full-source web/news documents
web/LLM accepted claim count is zero
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
Brain/Web operational minimum planner runs not met: 21/30
Brain/Web operational minimum web search tasks not met: 2/20
Brain/Web operational minimum web/news search calls not met: 2/20
fetched documents minimum not met: 0/10
claim extractor attempts minimum not met: 0/10
web/LLM accepted claims minimum not met: 0/3
```

중요:

```text
strict gate가 억지로 막은 게 아니다.
운영 Stage로 올릴 web/LLM source-backed claim이 실제로 0개다.
```

## 교차검증 4: v6 web rejection 내용

원본:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v6/web_rejected_documents.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v6/web_search_results.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v6/web_search_tasks.jsonl
```

거절 사유:

```text
web_result_stock_list_or_channel_page_not_source_document = 10
web_result_site_archive_or_sitemap_not_source_document = 1
```

대표 예:

```text
query:
  대웅 003090 2026 신규시설투자 자회사 정정 공시 투자 목적 완공 시점

rejected urls:
  https://codestockers.com/tag/...
  https://blog.naver.com/pjws3/224331251010
  https://t.me/s/alexppark?before=2326
  https://biz.heraldcorp.com/sitemap/archive/2020/20200423
```

해석:

```text
이 URL들은 source evidence가 아니다.
시세/태그/채널/아카이브/목록 페이지는 원문 claim의 anchor가 될 수 없다.
```

쉬운 예:

```text
대웅 공시를 확인해야 하는데,
검색 결과가 "급등주 정리", "텔레그램 채널", "사이트 아카이브"만 나온 상황이다.
이걸 읽어서 점수를 만들면 다시 월덱스/삼성 같은 오귀속 사고가 난다.
```

## 교차검증 5: v6 Brain trace의 정체

원본:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v6/brain_to_claim_trace.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v6/accepted_claims.jsonl
```

v6에서 Brain trace까지 연결된 claim:

```text
symbol = 003090
company = 대웅
source_provider = OpenDART
source_url = https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801612
primitive_id = implementation_timeline
archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
score_eligible = true
satisfaction_type = REROUTED_ACCEPTED_CLAIM
satisfies_source_task = false
full_thesis_claim = false
```

해석:

```text
공식 DART claim 하나가 Brain trace와 StageCourt까지 연결된 것은 맞다.
하지만 이것은 web/LLM accepted claim이 아니고, full-thesis claim도 아니다.
따라서 대표 census row로 promotion하지 않는 것이 맞다.
```

쉬운 예:

```text
공식 서류 한 장에서 "일정 연장"은 확인했다.
하지만 이것만으로 "매출/현금흐름까지 연결된 완성 thesis"라고 하면 안 된다.
```

## 교차검증 6: score contribution 안전성

원본:

```text
output/census_v4/2026-07-01/score_contributions.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v6/score_contributions.jsonl
```

집계:

```text
canonical output:
  score_contributions = 92
  nonzero contributions = 92
  nonzero_without_support_claim = 0

sourcequality-v6:
  score_contributions = 97
  nonzero contributions = 97
  nonzero_without_support_claim = 0
```

해석:

```text
현재 산출물 기준으로는 "claim 없는 점수"는 관측되지 않았다.
이 부분은 좋은 방어선이다.
```

다만 한계:

```text
support claim이 있다고 해서 FULL_THESIS score라는 뜻은 아니다.
EVENT_WEIGHTED_PARTIAL과 FULL_E2R_100을 계속 분리해야 한다.
```

쉬운 예:

```text
영수증이 붙은 간식비 지출은 맞다.
하지만 그 영수증 하나가 회사 전체 결산보고서는 아니다.
```

## 교차검증 7: all-archetype replay 상태

원본:

```text
output/census_v4/2026-07-01/all_archetype_replay_matrix.json
output/census_v4/2026-07-01/controlled_semantic_replay_audit.json
```

집계:

```text
all_archetype_replay_pass = false
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 6
missing_required_archetype_count = 26

status_counts:
  SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY = 6
  SOURCE_GAP_PENDING = 26
  GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY = 4
```

source-backed ready:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
C15_MATERIAL_SPREAD_SUPERCYCLE
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
C24_BIO_TRIAL_DATA_EVENT_RISK
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

해석:

```text
대표 6개 아키타입의 source-backed semantic replay는 좋아졌다.
하지만 전체 required 32개 아키타입 중 26개는 아직 source-backed positive + guard replay가 없다.
```

쉬운 예:

```text
국어, 영어, 수학, 과학, 사회, 역사 6과목은 모의고사 답안지가 있다.
하지만 졸업요건 32과목 중 26과목은 아직 실제 답안지가 없다.
```

## 현재 코드상 단절 위치

관련 코드:

```text
src/e2r/research_brain/v4_production_orchestrator.py
src/e2r/research_brain/v4_planner_runtime.py
src/e2r/research_brain/v4_schemas.py
```

현재 있는 retry:

```text
_retry_planner_for_rejected_mapping_feedback
```

이 retry가 처리하는 상황:

```text
source task 실행
-> 문서 fetch
-> raw assertion / claim 생성
-> primitive mapping 또는 eligibility에서 rejected
-> rejected_claim_feedback을 planner에게 반환
-> planner가 다른 bounded source task/query를 제안
```

현재 없는 retry:

```text
source task 실행
-> web search result 전부 metadata 단계에서 rejected
-> fetched_document = 0
-> claim_extractor_run = 0
-> rejected_claim_feedback = empty
-> planner에게 실패 이유가 돌아가지 않음
```

v6는 정확히 두 번째 상황이다.

쉬운 예:

```text
현재 retry는 "답안지를 받아서 채점했는데 틀렸을 때"만 다시 물어본다.
v6는 "답안지가 접수창구까지 오지도 못했을 때"다.
그래서 지금 retry가 작동하지 않는다.
```

## P0 패치 목표

P0는 점수나 Stage를 올리는 패치가 아니다.

목표:

```text
all web results rejected
-> rejection reason distribution + examples
-> LLM planner feedback
-> 새 bounded source task/query
-> source route 재실행
```

금지:

```text
if company == "대웅": query = "대웅 신규시설투자 IR PDF"
if primitive_gap == "policy_or_regulatory_confirmed": query = "{company} 보조금 인허가"
if v6 rejection == archive: hardcoded naver query 변경
```

허용:

```text
LLM planner에게 실패 이력을 준다.
코드는 LLM query/source task가 안전한지 검증하고 실행한다.
```

쉬운 예:

```text
나쁜 방식:
  선생님이 학생 대신 정답을 써 준다.

좋은 방식:
  선생님이 "네가 낸 답안은 전부 문제지 목차였다"라고 피드백한다.
  학생이 새 답안을 쓰고,
  선생님은 그 답안이 규칙을 어기지 않았는지만 본다.
```

## P0 구현 설계

### 1. PlannerRunV4 schema

추가:

```text
source_rejection_feedback_count: int = 0
```

이유:

```text
rejected_claim_feedback_count는 claim까지 만든 뒤 탈락한 경우다.
source_rejection_feedback_count는 fetch/claim 이전에 source 후보가 탈락한 경우다.
둘을 섞으면 어디서 막혔는지 다시 흐려진다.
```

### 2. Evidence summary

현재:

```text
planner_feedback
rejected_claim_feedback
```

추가:

```text
source_rejection_feedback
```

포함할 내용:

```text
candidate_event_id
source_task_id
primitive_gap
query
provider_name
rejection_reason_distribution
sample_rejected_urls
sample_titles
selected_source_count
fetched_document_count
```

포함하면 안 되는 내용:

```text
score
stage
current_score_eligible
verified final
accepted claim final
```

### 3. New helper

추가 후보:

```text
_source_rejection_feedback_from_bundle(bundle, limit=8)
```

동작:

```text
1. bundle.web_rejected_documents를 본다.
2. accepted claim이 없는 source task 중심으로 rejection reason을 모은다.
3. query/url/title/provider/source_task_id/primitive_gap 예시를 남긴다.
4. score/stage/current_score_eligible는 절대 넣지 않는다.
```

### 4. New retry

추가 후보:

```text
_retry_planner_for_source_rejection_feedback(...)
```

전제:

```text
provider exists
planner_provider != none/fake
retry_max > 1
live_full_bounded external web required
planner_run.output exists
bundle has no direct source task accepted claim
source rejection feedback exists
```

planner feedback tag:

```text
previous_sources_rejected_before_extraction
```

### 5. Planner prompt rule

추가 rule:

```text
If existing_evidence_summary.source_rejection_feedback is non-empty,
previous source candidates were rejected before extraction.
Do not repeat the same URL/source pattern.
Plan a different bounded source_task/query that targets issuer IR, DART/KIND detail,
report PDF, company newsroom, trusted article original, or another source class
that can prove the primitive directly.
Still do not output score, stage, verified final, current_score_eligible, or accepted claim final.
```

### 6. Retry task dedupe

현재 feedback retry task reason은 rejected-claim mapping 중심이다.

추가:

```text
feedback_retry:source_rejection
```

이유:

```text
나중에 artifact를 볼 때 "claim rejection 재시도"와 "source rejection 재시도"를 구분해야 한다.
```

## P0 acceptance tests

최소 테스트:

```text
1. source rejection feedback이 evidence context에 들어간다.
2. source rejection feedback에는 score/stage/current_score_eligible이 없다.
3. all-results-rejected bundle에서 planner retry가 1회 돈다.
4. direct source task accepted claim이 이미 있으면 source rejection retry는 돌지 않는다.
5. retry_max=1이면 source rejection retry는 돌지 않는다.
6. planner provider none/fake이면 source rejection retry는 돌지 않는다.
7. source rejection feedback retry run은 planner_run_role=feedback_retry를 남긴다.
8. source_rejection_feedback_count > 0이 planner_runs.jsonl에 남는다.
9. prompt payload에 source_rejection_feedback이 포함된다.
10. prompt rule에 source rejection before extraction 문구가 있다.
```

회귀 테스트:

```text
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v

PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate -v
```

최종 확인:

```text
sourcequality-v7 diagnostic를 다시 실행한다.
```

성공 판정은 두 단계로 나눈다.

```text
P0 functional success:
  all-results-rejected feedback retry가 artifact에 남는다.

P0 operational success:
  retry 후 fetched full-source web/news document > 0
  claim_extractor_attempt_count > 0
  web_or_llm_accepted_claim_count > 0
```

첫 단계만으로는 운영 준비가 아니다.

2026-07-02 v7 후속 확인:

```text
output_root = output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v7
verdict = NOT_READY

P0 functional success:
  source rejection feedback retry path = implemented and unit-tested
  live v7에서 source_rejection_feedback_count = 0
  이유: 모든 source 후보가 fetch 전 탈락한 케이스가 아니라,
        full-source fetch와 LLM extraction 이후 claim mapping에서 탈락했기 때문이다.

P0 operational success:
  web_fetched_documents = 9
  claim_extractor_runs = 9
  raw_assertion_rejections = 56
  web_or_llm_accepted_claim_count = 0
  FULL_THESIS row = 0
```

해석:

```text
v6의 병목은 "좋은 원문을 못 가져옴"이었다.
v7의 병목은 "가져온 원문에서 추출한 claim이 target/directness 또는 primitive mapping을 통과하지 못함"이다.

따라서 source rejection retry만으로는 끝나지 않는다.
다음 패치는 claim rejection feedback을 이용해
아키타입/primitive 라우팅과 source task를 다시 고르는 경로를 검증해야 한다.
```

쉬운 예:

```text
v6:
  서류 접수 창구에서 "이건 서류가 아니다"라고 돌려보냄.

v7:
  서류는 받아서 읽었지만,
  "이 문장은 대상 회사 직접 claim이 아니다" 또는
  "이 문장은 지금 점수 칸에 들어갈 primitive가 아니다"라고 탈락함.
```

## P0를 잘못 구현하면 생기는 문제

나쁜 패치 1:

```text
metadata rejection이 많으니 source filter를 느슨하게 한다.
```

왜 나쁜가:

```text
다시 시세표, 채널, 아카이브가 EvidenceDocument로 들어온다.
월덱스/삼성식 주체 오귀속 사고가 재발한다.
```

나쁜 패치 2:

```text
web/LLM accepted claim이 0이니 official claim만으로 BRAIN_WEB_PARTIAL 승격한다.
```

왜 나쁜가:

```text
BRAIN_WEB_PARTIAL은 Brain/Web 경로 검증용이다.
official-only claim을 web/LLM claim처럼 승격하면 readiness gate가 거짓 통과한다.
```

나쁜 패치 3:

```text
코드가 primitive_gap별 query template을 직접 만든다.
```

왜 나쁜가:

```text
AGENTS.md의 LLM Agent Workflow를 위반한다.
새 섹터/새 아키타입이 들어올 때마다 코드 템플릿을 늘리는 죽은 시스템이 된다.
```

나쁜 패치 4:

```text
fetch가 1개라도 있으면 accepted claim으로 간주한다.
```

왜 나쁜가:

```text
fetch는 문서를 가져온 것뿐이다.
점수에는 anchor -> raw assertion -> adjudicated claim -> primitive mapping -> score contribution이 필요하다.
```

## P1 이후 방향

P0가 통과하면 다음 순서다.

```text
P1. official detail reroute 강화
    DART/KIND 원문 detail을 먼저 닫을 수 있는 task는 web으로 보내지 않는다.

P2. readable document path 확장
    issuer IR, report PDF, company newsroom, trusted article original을 source class로 명확히 구분한다.

P3. LLM extractor live acceptance
    unstructured document에서 target/direct/current/primitive claim을 뽑아 accepted claim까지 닫는다.

P4. Brain/Web promotion
    web/LLM accepted claim이 StageCourt trace를 만들고 representative row promotion까지 연결되는지 확인한다.

P5. full-thesis production smoke
    FULL_THESIS row와 FULL_E2R_100 verified score row가 실제로 생기는지 확인한다.

P6. all-archetype source-backed replay 확장
    required 32개 아키타입을 모두 source-backed positive + guard replay로 닫는다.
```

중요:

```text
P0~P5는 live pipeline 연결 문제다.
P6는 전 아키타입 coverage 문제다.
둘 중 하나만 해결해도 goal completion은 아니다.
```

## 다음 에이전트 공격 질문

다음 에이전트는 아래를 먼저 공격한다.

```text
1. FULL_THESIS row가 정말 0인지, 아니면 문서가 stale인지?
2. EVENT_WEIGHTED_PARTIAL 67개를 FULL_E2R_100으로 오해한 곳이 없는지?
3. v6 accepted claim 1개가 web/LLM claim으로 잘못 집계되지 않는지?
4. v6 Brain trace 1개가 representative census row로 promotion되지 않았는지?
5. v7에서 web_fetched_document_count=9, claim_extractor_runs=9인데 accepted claim이 0인 이유가 target/directness/mapping artifact로 설명되는지?
6. v7 raw_assertion_rejections 56개가 너무 공격적으로 좋은 claim까지 막은 건 아닌지?
7. rejected claim reason이 LLM planner feedback으로 되돌아가는 코드가 실제로 있는지?
8. planner retry가 source rejection과 claim rejection을 구분하는지?
9. sourcequality-v7에서 feedback_retry planner run artifact가 남고, claim feedback 8개가 붙었는지?
10. retry 후에도 deterministic query template을 새로 만들지 않았는지?
11. source filters가 종목명 예외를 쓰지 않는지?
12. source_proxy_only 연구자료가 운영 score fixture로 들어가지 않았는지?
13. source-backed ready 6/32가 최신인지?
14. 26개 missing archetype을 pending으로 남긴 이유가 artifact에 남는지?
15. nonzero contribution support claim 0 누락이 유지되는지?
16. same document rerun 시 claim idempotency가 깨지지 않는지?
17. full repo test artifact가 최신인지?
18. canonical output과 diagnostic output을 섞어 READY라고 말하지 않았는지?
```

## 재현 명령

최신 Brain/Web v7 계열 진단 재현 형태:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v7 \
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

기대:

```text
exit code = 1
stdout = NOT_READY
```

이 실패는 정상 차단이다.

```text
운영 FULL_THESIS Stage가 없는데 READY라고 하면 안 된다.
```

최신 full unittest:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v
```

현재 최신 증거:

```text
status = OK
test_count = 5024
duration_seconds = 196.2862
artifact sha256 = b0d9032319072e7767c3f929a8da3cd31f5599017a7d0b55f53a64b35d0e3b32
log sha256 = f9dedcbbaf1fb2fde184e15084bdb3e05aae48b073b009ddeef76814b1757273
```

## 최종 판정

현재 상태:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS = PASS
CLAIM_BACKED_NONZERO_SCORE_SUPPORT = PASS
STAGE_SCOPE_SEPARATION = PASS
SOURCE_TASK_IDENTITY_AUDIT = PASS
SOURCE_HYGIENE_ROUTER = IMPROVED

BRAIN_WEB_EVIDENCE_PASS = FAIL
FULL_THESIS_PRODUCTION_PASS = FAIL
FULL_E2R_100_VERIFIED_SCORE = FAIL
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS = FAIL
GOAL_COMPLETION_READY = FAIL
```

다음 패치의 가장 작은 올바른 목표:

```text
sourcequality-v8에서
claim rejection feedback이 planner에게 들어가고,
planner가 기존 C29/volume_growth_visible 경로를 무작정 반복하지 않고,
target-direct current claim이 닫힐 수 있는 아키타입/primitive/source task로 재계획하며,
그 retry run과 rejected->new-task 연결이 artifact로 남는 것.
```

다음 패치의 운영 목표:

```text
좋은 원문 fetch
-> LLM extractor run
-> target/direct/current adjudication pass
-> primitive mapping pass
-> web/LLM accepted claim
-> primitive state
-> score contribution
-> StageCourt trace
-> representative FULL_THESIS row
```

한 문장으로 정리:

```text
지금은 "가짜 Stage를 막는 안전장치"는 좋아지고 있지만,
"살아 있는 source-backed full-thesis Stage를 만들어 내는 경로"는 아직 닫히지 않았다.
다음 패치는 점수를 올리는 패치가 아니라,
claim rejection을 LLM planner 재계획으로 되돌려
대상회사 직접 claim과 맞는 primitive/source task를 다시 찾게 만드는 패치여야 한다.
```

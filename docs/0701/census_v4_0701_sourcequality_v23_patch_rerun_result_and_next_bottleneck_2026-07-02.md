# Census v4 0701 SourceQuality v23 Patch Rerun Result / Next Bottleneck

작성일: 2026-07-02 KST

> 최신 상태 아님. 이 문서는 v23 재실행 결과다.
> 최신 hard review packet은
> `docs/0701/census_v4_0701_sourcequality_v26_external_feedback_sourceclass_patch_and_stage_truth_2026-07-02.md`다.
> v26에서는 v24의 `web_claimed_but_zero_search_count` critical이 해소되어
> 실제 web search/fetch/LLM extractor가 실행됐지만,
> `web_or_llm_accepted_claim_count=0`, `FULL_THESIS row=0`이라 운영 Stage는 여전히 없다.

대상 산출물:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v22
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v23
```

## 1. 직접 답

```text
Stage가 있는 애들은 있다.
하지만 운영 FULL_THESIS Stage가 있는 애들은 아직 없다.
```

v23 기준 숫자:

```text
census_stage_status row = 3391
stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391
  BRAIN_WEB_PARTIAL = 0
  FULL_THESIS = 0

base_stage_distribution:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

score_scope_distribution:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

verified_score rows = 0
full_e2r_verified_score rows = 0
operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391
```

쉬운 예:

```text
전 종목 출석부에는 "관심 / 추가확인 / 리스크 검토" 같은 상태 메모가 붙었다.
하지만 정식 100점 성적표, 즉 운영 FULL_THESIS 점수표는 아직 한 장도 없다.
```

## 2. v21, v22, v23 비교

| 항목 | v21 기준선 | v22 패치 후 실패 | v23 schema 수정 후 재실행 |
|---|---:|---:|---:|
| readiness | NOT_READY | NOT_READY | NOT_READY |
| planner_run_count | 21 | 21 | 22 |
| real_provider_success_count | 1 | 0 | 2 |
| source_task_execution_count | 13 | 0 | 13 |
| web_search_task_count | 2 | 0 | 4 |
| web_fetched_document_count | 1 | 0 | 2 |
| llm_claim_extractor_attempt_count | 1 | 0 | 2 |
| accepted_claim_count | 24 | 0 | 4 |
| official_accepted_claim_count | 24 | 0 | 4 |
| web_or_llm_accepted_claim_count | 0 | 0 | 0 |
| brain_stage_trace_count | 1 | 0 | 1 |
| brain_promoted_stage_row_count | 0 | 0 | 0 |
| FULL_THESIS candidate_row_count | 0 | 0 | 1 |
| promoted_full_thesis_row_count | 0 | 0 | 0 |
| leaf critical_count | 0 | 2 | 0 |
| runtime plausibility | PASS | FAIL | PASS |

해석:

```text
v22는 기능 검증 실행이 아니라 schema regression 실행이다.
v23은 그 schema regression을 고친 뒤의 유효한 재실행이다.
v23에서 FULL_THESIS 후보 스캔은 0 -> 1로 살아났지만,
최종 FULL_THESIS 승격은 여전히 0이다.
```

## 3. v22에서 실제로 깨진 것

v22의 모든 real planner call은 strict JSON schema에서 실패했다.

```text
provider_error:
  Missing 'query_intents'.
  strict schema requires every key in properties to be present in required
```

원인:

```text
source_task_drafts[*].query_intents를 schema properties에는 추가했지만
strict provider가 요구하는 required 목록에는 넣지 않았다.
```

패치:

```text
src/e2r/research_brain/v4_planner_runtime.py
  PLANNER_BATCH_OUTPUT_SCHEMA
    source_task_drafts.items.required += query_intents

tests/test_research_brain_v4_real_planner_provider.py
  test_planner_batch_schema_requires_every_declared_object_property_for_strict_provider
```

쉬운 예:

```text
양식에 "연락처" 칸을 새로 만들었는데,
제출 시스템에는 "모든 칸은 필수" 규칙이 있었다.
그런데 필수 칸 목록에 연락처를 빼먹어서 접수 자체가 거절된 것이다.
```

## 4. v23에서 새로 증명된 것

### 4.1 P0-A 후보 스캔은 살아났다

v23의 `full_thesis_production_runner_audit.json`:

```text
candidate_row_count = 1
blocked_candidate_count = 1
promoted_full_thesis_row_count = 0
verdict = PENDING_PRODUCTION_FULL_THESIS
```

후보는 `BRAIN_WEB_PARTIAL` row가 아니라 `stagecourt_traces.jsonl` 직접 스캔으로 잡혔다.

```text
candidate_source = stagecourt_trace_direct_scan
symbol = 003090
primary_archetype = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
stagecourt_trace_id = SCT-BRAIN-f6943ccc426950b84dae
present_primitives = implementation_timeline
missing_green_primitives:
  direct_company_cash_route
  policy_or_regulatory_confirmed
  subsidy_capture_visible
blocker:
  missing_green_gate_primitives
```

즉 P0-A 패치의 목적은 일부 달성됐다.

```text
패치 전:
  BRAIN_WEB_PARTIAL row가 0이면 FULL_THESIS 후보도 0.

패치 후:
  Research Brain StageCourt trace 자체를 FULL_THESIS 후보로 검사.
  단 green gate가 닫히지 않으면 승격하지 않음.
```

### 4.2 Brain/Web evidence pass는 여전히 아니다

v23의 `brain_web_readiness_gate_audit.json`:

```text
verdict = BLOCKED
web_or_llm_accepted_claim_count = 0
official_accepted_claim_count = 4
brain_accepted_claim_count = 4
web_fetched_document_count = 2
llm_claim_extractor_attempt_count = 2
```

blockers:

```text
web/LLM accepted claim count is zero
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
planner runs 22/30
web search tasks 4/20
```

중요한 분리:

```text
official-only claim으로 FULL_THESIS 후보가 될 수는 있다.
하지만 official-only claim만으로 BRAIN_WEB_EVIDENCE_PASS라고 부르면 안 된다.
Brain/Web pass는 web/LLM accepted claim minimum을 따로 만족해야 한다.
```

쉬운 예:

```text
DART 서류만으로도 어떤 논문 심사 후보가 될 수는 있다.
하지만 "웹/LLM 추가조사가 빈칸을 메웠다"는 별도 시험을 통과한 것은 아니다.
```

## 5. v23의 Research Brain trace 내용

`stagecourt_traces.jsonl`의 유일한 `research_brain_v4_attempt` trace:

```text
symbol = 003090
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
base_stage = 0
score_interval = 19.5 ~ 19.5
score_status = FINAL
investigation_status = COMPLETE
hard_break_status = NONE
accepted_claim_ids = 4
score_contribution_ids = 5
present_green_primitives:
  implementation_timeline
missing_green_primitives:
  policy_or_regulatory_confirmed
  direct_company_cash_route
  subsidy_capture_visible
not_promoted_to_census_stage_status = true
```

해석:

```text
대웅 003090에 대해 Research Brain trace는 생겼다.
하지만 C31 green gate 중 "정책/규제 확정", "대상회사 현금 유입 경로",
"보조금 포착 가능성"이 비어 있어서 FULL_THESIS로 올리지 않는 것이 맞다.
```

이건 좋아진 점이다.

```text
예전 문제:
  trace가 있으면 stage처럼 보이거나,
  공식 claim만 있어도 Brain/Web 성공처럼 보일 위험.

현재 v23:
  trace는 후보로는 잡히지만,
  green gate 미충족이면 FULL_THESIS row를 만들지 않는다.
```

## 6. v23에서 아직 막힌 이유

### 6.1 web/LLM accepted claim이 0이다

v23은 웹 문서 2개를 fetch했고 LLM extractor도 2번 돌았다.
하지만 accepted claim은 전부 OpenDART official claim이다.

```text
accepted_claims.jsonl:
  total = 96
  research_brain_v4_attempt = 4
  source_provider = OpenDART 96
  web_or_llm accepted = 0

raw_assertion_rejections.jsonl:
  total = 24
  source_origin = research_brain_v4_attempt 24
  source_provider:
    OpenDART = 16
    Naver web search API = 8
  mapping_status = REJECTED 24
  target_scope_status:
    DIRECT = 19
    UNRELATED = 5
```

쉬운 예:

```text
웹 기사와 공시를 읽기는 했다.
하지만 "이 문장이 대상회사 현재 점수 primitive에 들어갈 수 있다"는 통과 도장은 0개다.
```

### 6.2 source task가 늘었지만 품질 병목은 남았다

v23 source task:

```text
source_task_execution_count = 13
source_class:
  DART = 94 total corpus rows 중 94
  KRX = 4
  KIND = 2
  TrustedNews = 1
  Official = 1
  CompanyGuide = 1
  IR = 1
```

Research Brain attempt 안에서는:

```text
web_fetched_documents = 2
web_search_task_count = 4
naver_search_call_count = 4
trusted_news_search_call_count = 0
general_web_search_call_count = 0
```

남은 병목:

```text
1. Naver가 official URL을 찾아도 KIND/DART 상세 resolver로 안정적으로 넘기는 경로가 아직 P0.
2. full fetched article/report와 search snippet/source provider mismatch를 더 명확히 분리해야 함.
3. rejected primitive/source feedback은 planner retry로 돌아가지만,
   아직 web/LLM accepted claim을 만들 정도로 source selection을 바꾸지 못함.
4. FCF/DART-solvable gap을 web/news로 보내는 validator rejection이 여전히 1건 발생.
```

## 7. 지금 방향이 맞는 부분과 틀리면 안 되는 부분

맞는 부분:

```text
1. Stage/score scope는 정직하게 분리된다.
2. CENSUS_EVENT_BOARD Stage가 운영 FULL_THESIS Stage처럼 승격되지 않는다.
3. score_contribution_without_accepted_claim_support_count = 0.
4. event/assessment/market anomaly가 score evidence로 들어가는 critical count = 0.
5. source_proxy/evidence_url_pending/snippet-only 점수 유입 critical count = 0.
6. v23 runtime plausibility는 PASS다.
7. P0-A patch로 official-only trace도 FULL_THESIS 후보 심사 대상이 됐다.
```

틀리면 안 되는 부분:

```text
1. candidate_row_count = 1을 운영 Stage 1개라고 말하면 안 된다.
2. OpenDART accepted claim 4개를 Brain/Web pass라고 말하면 안 된다.
3. web_fetched_document_count = 2를 web/LLM accepted claim이라고 말하면 안 된다.
4. score_status = FINAL을 FULL_E2R_100 verified score라고 말하면 안 된다.
5. C31 base_stage 0 trace를 삼성전자/하이닉스 C06 thesis 결과처럼 해석하면 안 된다.
```

쉬운 예:

```text
candidate_row_count = 1
  -> 심사대에 올라온 서류 1건.

promoted_full_thesis_row_count = 0
  -> 최종 합격 서류 0건.

web_fetched_document_count = 2
  -> 읽은 웹 문서 2건.

web_or_llm_accepted_claim_count = 0
  -> 그중 점수 칸에 들어간 웹/LLM claim 0건.
```

## 8. 다음 P0 패치 방향

### P0-1. KIND/DART official detail resolver

목표:

```text
Naver result가 exact official hostname이면:
  Naver 자체를 score source로 쓰지 않는다.
  KIND/DART official resolver로 넘긴다.
  acptno/rcpNo/첨부/본문/table anchor를 직접 resolve한다.
  resolve 실패는 official_detail_resolve_failed로 남긴다.
```

예:

```text
나쁜 방식:
  네이버 검색결과 snippet에 "KIND 공시"가 보이니 점수 재료로 사용.

좋은 방식:
  네이버는 길 안내만 한다.
  실제 점수 근거는 KIND/DART 원문 anchor에서 나온다.
```

2026-07-02 부분 패치:

```text
patched:
  src/e2r/research_brain/v4_source_acquisition_runner.py
  tests/test_research_brain_v4_real_source_acquisition.py

implemented:
  1. web/Naver search result URL의 exact hostname이 dart.fss.or.kr이면 DART official detail route로 표시
  2. web/Naver search result URL의 exact hostname이 kind.krx.co.kr이면 KIND official detail route로 표시
  3. fake path like example.com/.../kind.krx.co.kr/... 는 official route로 승격하지 않음
  4. successful fetch:
     - EvidenceDocument.source_name = DART 또는 KIND
     - EvidenceDocument.source_type = FILING
     - web_search_results/web_fetched_documents에 official_detail_resolution_status = RESOLVED
     - official_document_id를 leaf에 기록
  5. failed fetch:
     - provider_errors에 official_detail_resolve_failed 기록
     - web_rejected_documents.rejection_reason이 official_detail_resolve_failed:* 로 남음
```

쉬운 예:

```text
네이버 검색 결과:
  https://kind.krx.co.kr/common/disclsviewer.do?...acptno=20260630001612

패치 전:
  "네이버가 찾은 웹 문서"처럼 보일 수 있음.

패치 후:
  "네이버가 KIND 공식 원문 주소를 발견했고,
   그 원문 resolve가 성공/실패했는지"가 별도 필드로 남음.
```

검증:

```text
targeted official resolver tests:
  test_web_discovered_kind_document_keeps_official_kind_source_class
  test_web_discovered_dart_document_keeps_official_dart_resolution_metadata
  test_web_discovered_official_detail_fetch_failure_is_a_resolver_failure
  test_web_discovered_fake_kind_path_does_not_become_official_kind_source_class
  test_web_discovered_kind_full_source_is_not_rejected_as_general_search_provider_error
  -> Ran 5 tests / OK

related source/evidence modules:
  PYTHONPATH=src python -m unittest \
    tests.test_research_brain_v4_real_source_acquisition \
    tests.test_research_brain_v4_evidence_extraction_from_real_document -v
  -> Ran 41 tests / OK

gate/feedback regression:
  PYTHONPATH=src python -m unittest \
    tests.test_census_v4_brain_web_readiness_gate \
    tests.test_research_brain_v4_operational_modes -v
  -> Ran 47 tests / OK
```

주의:

```text
이 P0-B 패치는 아직 새 live diagnostic artifact로 증명된 것이 아니다.
latest v23 artifact는 이 패치 전 산출물이다.
따라서 다음 diagnostic에서 official_detail_resolution_* 필드가 실제 leaf에 생기는지 확인해야 한다.
```

### P0-2. source admissibility를 full source와 search provider로 분리

목표:

```text
검색 provider = Naver
문서 origin = trusted news / company newsroom / official disclosure / blog
score admissibility = origin과 anchor 기준으로 판정
```

주의:

```text
Naver를 통과했다고 점수 가능도 아니고,
Naver에서 발견됐다고 무조건 점수 불가능도 아니다.
다만 원문 origin, domain allowlist, source class, anchor가 닫혀야 한다.
```

### P0-3. rejected assertion feedback의 실제 효과 검증

v23은 retry가 돌았지만 accepted web/LLM claim은 0이다.
다음 패치는 retry가 실제로 쿼리와 source class를 바꾸는지 검증해야 한다.

필수 로그:

```text
previous rejected predicate
previous rejected primitive
previous source_provider/source_class failure
new query_intents
new source_task_drafts[*].query_intents
new accepted/rejected delta
```

예:

```text
"계약 기사"를 읽었는데 margin bridge가 없었다.
다음 검색도 "계약 기사"면 실패다.
다음 검색은 IR/실적발표/사업보고서/CompanyGuide에서 매출총이익률,
영업이익률, 현금흐름 전환을 찾도록 바뀌어야 한다.
```

### P0-4. FULL_THESIS candidate와 Brain/Web pass를 계속 분리

규칙:

```text
official-only complete thesis:
  FULL_THESIS 후보 또는 승격 가능
  Brain/Web evidence pass는 아님

web/LLM supported thesis:
  FULL_THESIS 후보 또는 승격 가능
  Brain/Web evidence pass도 별도 minimum 충족 시 가능
```

이 분리를 깨면 v12식 가짜 `BRAIN_WEB_PARTIAL`이 다시 생긴다.

### P0-5. operational minimum은 resolver와 feedback 효과 확인 후 확장

v23은 아직 small diagnostic이다.

```text
planner 22/30
web search task 4/20
web fetched 2/10
LLM extractor 2/10
web/LLM accepted 0/3
```

하지만 지금 바로 30/20/10만 맞추려고 크게 돌리면 안 된다.

```text
먼저:
  official resolver
  source admissibility split
  rejected feedback effect
  FULL_THESIS candidate blocker trace

그 다음:
  operational minimum diagnostic
```

## 9. 다음 에이전트 공격 질문

다음 리뷰어는 아래를 먼저 공격해야 한다.

```text
1. v23의 candidate_row_count=1이 실제로 stagecourt_trace_direct_scan에서 왔는가?
2. 그 candidate가 왜 FULL_THESIS로 승격되지 않았는지 blocker가 claim/primitive 기준으로 설명되는가?
3. official-only candidate가 Brain/Web evidence pass로 오염되지 않았는가?
4. web_fetched_documents 2개가 accepted web/LLM claim 0개로 끝난 이유가 raw_assertion_rejections에 충분히 남았는가?
5. v22 strict schema regression이 다시 생기지 않게 schema required test가 있는가?
6. planner retry가 이전 rejection을 실제 query/source task 변화로 바꾸는가?
7. Naver-discovered official URL이 official resolver로 넘어가는가?
8. FCF/DART-solvable gap이 general web/news로 흘러가면 validator가 막고 feedback으로 되돌리는가?
9. non-Stage0 85개가 UI/report에서 운영 Stage처럼 보이는 경로가 아직 있는가?
10. FULL_E2R_100 verified score 0개인데 readiness 문서가 pass처럼 읽히는 문구가 남아 있는가?
```

## 10. 검증 기록

패치 후 targeted/unit 검증:

```text
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
  -> Ran 33 tests / OK

PYTHONPATH=src python -m unittest tests.test_research_brain_v4_real_planner_provider -v
  -> Ran 6 tests / OK

PYTHONPATH=src python -m unittest tests.test_census_v4_brain_stage_promotion_gate -v
  -> Ran 12 tests / OK

PYTHONPATH=src python -m unittest tests.test_census_v4_full_thesis_smoke_tasks -v
  -> Ran 7 tests / OK

PYTHONPATH=src python -m unittest tests.test_census_v4_run_mode_honesty -v
  -> Ran 18 tests / OK

PYTHONPATH=src python -m unittest tests.test_census_v4_brain_web_readiness_gate -v
  -> Ran 14 tests / OK
```

최신 full unittest:

```text
command:
  PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
    --artifact output/test_full_repo_0701/full_unittest_after_p0b_official_detail_resolver_artifact.json \
    --log output/test_full_repo_0701/full_unittest_after_p0b_official_detail_resolver.log \
    -- python -m unittest discover -s tests -v

status = OK
test_count = 5048
failed_count = 0
error_count = 0
duration_seconds = 188.0978
artifact = output/test_full_repo_0701/full_unittest_after_p0b_official_detail_resolver_artifact.json
artifact_sha256 = 71f444f03cfe7f6ef0f5da5f8b285fa37ab51a611a15ce143ed7d3d1ad2a6a1a
log_sha256 = 12b0088e9ddb22995994770e8d8cd5962c724ab141339b201d0f7a12f9521d2c
```

주의:

```text
5048 tests OK는 코드 regression 방지 증거다.
운영 readiness가 READY라는 뜻은 아니다.
v23 readiness는 여전히 NOT_READY이고 FULL_THESIS row는 0이다.
```

## 11. 현재 판정

```text
Stage existence:
  event-board Stage exists
  operational FULL_THESIS Stage does not exist

P0-A candidate scan:
  partially fixed
  candidate_row_count 0 -> 1
  promotion 0

P0-C query feedback plumbing:
  partially fixed
  task-specific query_intents are supported
  external web/LLM failure can trigger retry despite direct official acceptance
  accepted web/LLM claim still 0

P0-B official detail resolver:
  partially fixed in code/tests
  exact KIND/DART official URLs now carry official_detail_resolution metadata
  latest v23 live artifact still predates this patch

Brain/Web:
  attempted
  not evidence-pass

Full thesis production:
  candidate visible
  not promotable yet

Goal completion:
  false
```

한 줄 결론:

```text
v23은 "아예 후보도 못 찾는 상태"에서는 벗어났다.
하지만 실제 운영 Stage/score가 있는 상태는 아니다.
다음 병목은 official resolver, source admissibility, rejected feedback effect,
그리고 green gate primitive를 claim-backed로 닫는 것이다.
```

# Census v4 0701 v26 Deep Cross Audit / Stage Truth / Next Patch Direction

작성일: 2026-07-02 KST

이 문서는 다음 에이전트가 `0701` 상태를 빡세게 검토할 수 있게 만든 최신 교차검증 패킷이다.

검증 기준 산출물:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v26
```

관련 최신 문서:

```text
docs/0701/census_v4_0701_sourcequality_v26_external_feedback_sourceclass_patch_and_stage_truth_2026-07-02.md
docs/0701/README.md
```

## 0. 최종 결론

현재 상태를 한 문장으로 말하면:

```text
Stage 상태판은 있다.
하지만 사용자가 원하는 운영 FULL_THESIS 점수/Stage는 아직 0개다.
```

쉽게 말하면:

```text
전교생 명단에 "출석 확인 / 상담 필요 / 결석" 같은 상태 라벨은 붙어 있다.
하지만 실제 시험 답안지를 채점해서 "90점, A등급"을 확정한 학생은 아직 없다.
```

따라서 지금 사용자에게 말해야 하는 답은 아래다.

```text
뭔가 잘못되고 있는 건 맞다:
  목표였던 운영 full thesis Stage까지는 아직 못 갔다.

하지만 거짓으로 Green/Yellow를 뽑는 방향으로 망가진 것은 아니다:
  현재 guard가 승격을 막고 있어서 FULL_THESIS row는 0개로 남아 있다.
```

## 1. Stage가 있는가?

있다. 다만 범위가 다르다.

`census_stage_status.jsonl` 기준:

```text
row count = 3391
stage_scope = CENSUS_EVENT_BOARD 3391
operator_stage_use = NOT_FULL_THESIS_STAGE 3391

base_stage_distribution:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1
```

이 수치만 보면 "Stage가 있네?"라고 착각할 수 있다.

하지만 같은 산출물은 아래도 말한다.

```text
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
verified_score_present_count = 0
```

즉:

```text
CENSUS_EVENT_BOARD Stage:
  전 종목을 census 모드에서 훑고 붙인 상태판 라벨

FULL_THESIS Stage:
  source-backed claim -> primitive -> score contribution -> StageCourt를 통과한 운영 Stage
```

현재 있는 것은 전자뿐이다.

## 2. 왜 Stage 상태판을 운영 Stage로 보면 안 되는가

`census_stage_status.jsonl` 첫 행만 봐도 의미가 드러난다.

```text
candidate_event_scope = ASSESSMENT_ONLY
census_assessment_event_score_evidence_allowed = false
accepted_claim_count = 0
base_stage = Stage0
canonical_stage = 0
full_thesis_not_run = true
full_thesis_missing_primitives = full_thesis_refresh_task_not_run
```

쉬운 예:

```text
"이 종목도 오늘 전체지도에서 확인했다"는 CensusAssessmentEvent가 있다.
하지만 이것은 점수 재료가 아니다.

점수에 들어가려면 원문 claim이 필요하다.
예: 공시 원문에서 계약금액, 기간, 상대방, 현재성이 accepted_claim으로 닫혀야 한다.
```

따라서 `Stage1`, `Stage2-Watch`, `Red`가 일부 보여도 현재는 아래처럼 읽어야 한다.

```text
운영 투자 논리 Stage가 아니라,
전체지도 상태판의 event-board label이다.
```

## 3. v26 readiness 교차검증

`readiness_verdict.json`:

```text
verdict = NOT_READY
target_gate_verdict = TARGET_GATE_BLOCKED
brain_web_mode = enabled
meaningful_operational_stage_pass = false
operational_stage_use_allowed = false
event_board_non_stage0_count = 85
event_board_stage_rows_are_operational_full_thesis = false
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
brain_web_evidence_pass = false
```

핵심 blockers:

```text
web/LLM accepted claim count is zero
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
planner runs not met: 22/30
web search tasks not met: 4/20
web/news search calls not met: 4/20
fetched documents not met: 2/10
claim extractor attempts not met: 2/10
web/LLM accepted claims not met: 0/3
```

이 중 제일 중요한 것은 숫자 부족보다 이것이다.

```text
web/LLM accepted claim = 0
```

검색/LLM이 돈 것은 맞지만, 점수에 넣을 수 있는 웹/LLM claim은 아직 하나도 없다.

## 4. Brain/Web은 실제로 돌았는가?

돌았다.

`brain_web_readiness_gate_audit.json`:

```text
llm_planner_call_count = 22
llm_real_provider_success_count = 1
source_task_execution_count = 13
official_accepted_claim_count = 24
web_search_task_count = 4
web_search_call_count = 4
web_search_result_count = 38
web_fetched_document_count = 2
llm_claim_extractor_attempt_count = 2
llm_claim_extractor_real_provider_count = 2
web_or_llm_accepted_claim_count = 0
verdict = BLOCKED
```

`runtime_plausibility_audit.json`도 라이브 실행 자체는 인정한다.

```text
verdict = PASS_LIVE_RUNTIME_PLAUSIBILITY
runtime_seconds = 276.9504
provider_call_count = 8
source_task_real_fetch_count = 8
web_search_task_count = 4
web_fetched_document_count = 2
evidence_extraction_count = 2
```

따라서 이전처럼 "웹 한다고 해놓고 웹 검색 0개"는 아니다.

현재 문제는:

```text
웹/LLM 경로가 실행은 됐지만,
score-eligible accepted claim까지 못 닫았다.
```

## 5. v24 -> v26에서 실제로 좋아진 점

v24의 핵심 문제:

```text
web_claimed_but_zero_search_count = 1
web_search_task_count = 0
web_fetched_document_count = 0
llm_claim_extractor_attempt_count = 0
```

원인:

```text
LLM planner가 외부 source task를 만들었지만,
official-solvable primitive에 붙였다.
policy validator가 막았다.
그 policy rejection이 LLM feedback으로 돌아가지 않았다.
```

v25/v26 패치 후:

```text
policy-rejected external task가 source_rejection_feedback으로 올라감
feedback_retry planner run 발생
web_search_task_count > 0
web_fetched_document_count > 0
llm_claim_extractor_attempt_count > 0
```

v26에서 또 좋아진 점:

```text
source_class_document_type_mismatch:DART:NEWS 오귀속 제거
```

쉬운 예:

```text
DART 공시와 뉴스가 같은 task 바구니에 같이 담겼다고 해서,
뉴스를 DART 문서처럼 검사하면 안 된다.

v26에서는 NEWS 문서를 DART로 오인하지 않는다.
```

## 6. v26에서 실제로 가져온 웹 문서

`web_fetched_documents.jsonl`:

```text
1. https://mynews0497.tistory.com/201
   title = 그린생명과학 (114450) 2025년 1분기 실적 기반 심층 투자분석 보고서

2. https://www.topstarnews.net/news/articleView.html?idxno=15881893
   title = [특징주 분석] 독감 대유행 이슈에… 그린생명과학 백신관련주 변동성 확대
```

이 둘은 LLM extractor까지 갔지만 accepted claim이 되지 않았다.

이것은 현재 guard 관점에서는 맞는 동작이다.

```text
Tistory 블로그나 일반 포털 특종/특징주 기사를 바로 점수 source로 열면,
예전 월덱스/2020 감사의견 오귀속 같은 문제가 재발할 수 있다.
```

따라서 다음 패치는:

```text
일반 웹 문서를 점수 source로 느슨하게 인정하는 패치가 아니다.
```

해야 할 일은:

```text
일반 검색 실패 패턴을 LLM planner에게 되돌려 주고,
공식 원문/회사 IR/리포트 PDF/신뢰 뉴스 원문 같은 더 좋은 route를 다시 계획하게 하는 것.
```

## 7. 웹 검색 결과 품질

`web_search_results.jsonl` 도메인 분포:

```text
timeli.tistory.com = 21
comp.wisereport.co.kr = 3
codestockers.com = 3
blog.kakaocdn.net = 2
t.me = 2
mynews0497.tistory.com = 1
stockrank.co.kr = 1
goodp7.tistory.com = 1
topstarnews.net = 1
fmkorea.com = 1
blog.naver.com = 1
report.hangyeong.com = 1
```

selection 결과:

```text
REJECTED_NON_EVIDENCE_RESULT_METADATA = 25
NOT_SELECTED_BUDGET_EXHAUSTED = 10
SELECTED_FOR_FETCH = 2
REJECTED_NON_EVIDENCE_CONTENT_AFTER_FETCH = 1
```

해석:

```text
검색은 실제로 했지만 결과 품질이 낮다.
상승률 정리, 종목 리스트, 블로그, 커뮤니티, 포털성 기사 위주다.
```

특히 114450 C05에서 필요한 것은 `margin_bridge_visible`이다.

필요한 문장은 대략 이런 것이다.

```text
이번 계약은 고마진 API/중간체 공급이며,
기존 설비 가동률 상승으로 원가율이 개선된다.

또는:
계약 단가/원가 구조가 확정되어 매출총이익률 개선이 예상된다.
```

반대로 이런 문장은 부족하다.

```text
주가가 올랐다.
독감 유행 관련주다.
공급계약 공시가 있었다.
```

계약 자체는 후보를 만들지만, 마진 bridge는 아직 못 닫은 것이다.

## 8. raw assertion rejection 교차검증

`raw_assertion_rejections.jsonl` 중 Brain/Web attempt:

```text
total = 67
source_provider:
  https://openapi.naver.com/v1/search/webkr.json = 51
  OpenDART = 16

primitive_gap:
  margin_bridge_visible = 34
  cost_overrun = 19
  contract_amount_to_prior_sales = 4
  contract_duration_months = 4
  delivery_schedule = 4
  official_disclosure_status_current = 2

rejection_reason:
  primitive_mapping_rejected = 37
  anchor_validation:quote_not_found_in_document_text = 22
  score_eligibility_rejected = 5
  temporal_status_rejected = 2
  target_scope_or_directness_rejected = 1
```

웹/LLM rejection만 보면:

```text
web/llm total = 51
primitive_gap:
  margin_bridge_visible = 34
  cost_overrun = 17

rejection_reason:
  anchor_validation:quote_not_found_in_document_text = 22
  primitive_mapping_rejected = 21
  score_eligibility_rejected = 5
  temporal_status_rejected = 2
  target_scope_or_directness_rejected = 1
```

중요한 의미:

```text
LLM이 문장을 많이 뽑긴 했다.
하지만 quote anchor가 실제 원문에 없거나,
mapping이 허용 primitive와 맞지 않거나,
general web search provider라 score source로 차단됐다.
```

이건 좋은 guard이기도 하고, 동시에 다음 패치의 방향을 말한다.

```text
LLM 추출 자체보다 source route와 rejection feedback loop가 더 급하다.
```

## 9. FULL_THESIS candidate 114450 교차검증

`full_thesis_production_runner_audit.json`:

```text
candidate_row_count = 1
blocked_candidate_count = 1
promoted_full_thesis_row_count = 0

blocked symbol = 114450
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
candidate_source = stagecourt_trace_direct_scan
stagecourt_trace_id = SCT-BRAIN-ded41e478e7424525c7f

present_primitives:
  contract_amount_to_prior_sales
  contract_duration_months
  delivery_schedule

missing_green_primitives:
  margin_bridge_visible

blockers:
  missing_green_gate_primitives
```

쉬운 예:

```text
계약서에서 "금액, 기간, 납품일정"은 확인됐다.
하지만 "이 계약이 이익률/현금흐름을 좋게 만든다"는 증거가 없다.
```

그래서 StageCourt trace는 있어도 운영 FULL_THESIS로 승격하면 안 된다.

현재 승격 차단은 맞다.

## 10. 겉보기 PASS와 실제 NOT_READY가 충돌하지 않는 이유

다음 audit들은 PASS다.

```text
leaf_artifact_audit = PASS
runtime_plausibility = PASS_LIVE_RUNTIME_PLAUSIBILITY
source_task_realness = LIVE_SOURCE_PASS
source_task_satisfaction = PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
source_coverage = PASS_LEDGER_REFRESH_COVERAGE
known_bad_regression = PASS
controlled_semantic_replay = PASS
```

하지만 이것은 goal completion과 다르다.

예:

```text
source_task_satisfaction PASS:
  기존 ledger/leaf-refresh row가 source task -> claim -> score/stage chain을 가진다는 뜻

Brain/Web readiness BLOCKED:
  이번 live Brain/Web 운영 경로가 웹/LLM accepted claim과 FULL_THESIS Stage를 만들지는 못했다는 뜻
```

즉 PASS 범위가 다르다.

```text
ledger refresh honesty = 일부 통과
live full thesis operation = 미통과
```

다음 에이전트가 이 둘을 섞으면 안 된다.

## 11. 현재 코드상 가장 의심스러운 다음 병목

현재 `_source_rejection_feedback_from_bundle`은 아래를 건너뛴다.

```text
rejection_phase == post_extraction_evidence_os
```

관련 위치:

```text
src/e2r/research_brain/v4_production_orchestrator.py
```

문제:

```text
문서 fetch 전 metadata/content rejection은 planner에게 feedback으로 돌아간다.
하지만 "문서는 fetch했고 LLM extractor도 돌았는데 score-eligible claim이 0개"인 실패는
post_extraction_evidence_os라서 source feedback에서 제외된다.
```

쉬운 예:

```text
택배가 아예 배달 실패한 건 배달기사에게 다시 알려준다.
그런데 물건은 왔지만 내용물이 주문과 안 맞았다는 사실은 안 알려준다.

그러면 다음 주문도 같은 잘못된 가게에서 시키게 된다.
```

v26의 핵심 실패가 바로 이것이다.

```text
웹 문서 2개 fetch
LLM extractor 2회 실행
accepted web/LLM claim 0
post_extraction_no_score_eligible_claim 2건
```

따라서 다음 P0 후보는:

```text
post-extraction score/admissibility rejection도 source-level feedback으로 요약해 planner retry에 넣기
```

단, 조심할 점:

```text
LLM에게 score/stage/current_score_eligible을 보여주면 안 된다.
feedback은 source route 실패 패턴만 보여야 한다.
```

허용되는 feedback 예:

```json
{
  "source_task_id": "ST-...",
  "primitive_gap": "margin_bridge_visible",
  "fetched_document_count": 1,
  "rejection_phase": "post_extraction_evidence_os",
  "rejection_reason_distribution": {
    "post_extraction_no_score_eligible_claim": 1
  },
  "not_eligible_reason_distribution": {
    "source_task_provider_error_score_block:general_search_not_score_source": 1,
    "source_provider_document_type_mismatch:IndustryMedia:general_web_search_provider": 1,
    "primitive_mapping_rejected:no_allowed_primitive_for_predicate": 1
  },
  "sample_rejected_sources": [
    {
      "url": "https://mynews0497.tistory.com/201",
      "title": "...",
      "rejection_reason": "post_extraction_no_score_eligible_claim"
    }
  ]
}
```

금지되는 feedback 예:

```text
이 문서를 인정하면 4점 오른다.
Green까지 6점 남았다.
current_score_eligible=false를 true로 바꿔라.
```

## 12. 다음 패치 방향

### P0-F. post-extraction rejection feedback retry

목표:

```text
fetch + LLM extraction까지 갔지만 accepted claim이 0인 웹 문서 실패를
planner source_rejection_feedback으로 되돌린다.
```

수락조건:

```text
post_extraction_evidence_os rejection이 source_rejection_feedback에 포함된다.
feedback에는 score/stage/final eligibility가 없다.
feedback_retry planner run이 발생한다.
동일 URL/source pattern 반복을 피하라는 prompt rule이 유지된다.
retry_max는 계속 bounded다.
```

반드시 막아야 할 회귀:

```text
post-extraction rejection을 score gap으로 오염시키지 말 것.
general web 문서를 점수 source로 바로 허용하지 말 것.
accepted official claim이 있어도 별도 web/LLM task 실패는 retry 가능해야 함.
```

### P0-G. source route 품질 개선

목표:

```text
일반 검색 결과를 점수 source로 느슨하게 풀지 않고,
결과를 더 좋은 원문 route로 연결한다.
```

허용 방향:

```text
Naver result가 DART/KIND/issuer IR/company newsroom/trusted report PDF 원문이면
정확한 hostname allowlist와 resolver를 거쳐 해당 source class로 재수집한다.

블로그/포털/커뮤니티/주식 채널은 diagnostic rejection으로 남기고,
LLM planner에게 "이 route는 점수 source가 아니었다"고 되돌린다.
```

금지 방향:

```text
Tistory 블로그도 LLM이 좋다고 하면 TrustedNews로 인정
TopStarNews 특징주 기사도 margin_bridge source로 인정
Naver general search provider면 다 score source 허용
```

### P0-H. 114450 C05 margin bridge route

목표:

```text
C05 margin_bridge_visible을 닫을 수 있는 source route를 실제로 찾는다.
```

우선순위:

```text
1. DART 정정공시 상세/계약 조건 원문
2. 회사 IR/홈페이지/사업보고서의 수익성/원가/설비 가동률 설명
3. public broker report PDF
4. 신뢰 가능한 원문 뉴스
```

중요:

```text
LLM이 query를 만들어야 한다.
코드는 "C05면 이런 검색어"를 하드코딩하지 않는다.
코드는 source class, as_of_date, target scope, 중복, provider score eligibility만 검증한다.
```

### P0-I. Brain/Web operational minimum 확대 run

v26은 smoke 성격이라 minimum counts를 못 채웠다.

```text
planner 22/30
web task 4/20
web call 4/20
fetch 2/10
extractor 2/10
web/LLM accepted 0/3
```

단, count만 늘리면 안 된다.

먼저 P0-F/P0-G를 넣고 rerun해야 한다.

안 그러면:

```text
나쁜 source를 더 많이 긁고 accepted claim은 계속 0개
```

가 된다.

## 13. 다음 에이전트 공격 질문

다음 리뷰어는 아래를 먼저 확인해야 한다.

```text
1. "Stage가 있다"는 말이 CENSUS_EVENT_BOARD와 FULL_THESIS를 섞고 있지 않은가?
2. FULL_THESIS row 0인데 사용자에게 운영 Stage가 있는 것처럼 말하는 경로가 남아 있는가?
3. accepted_claim_count 116 / score_contribution 94를 운영 full thesis 증거로 오해하지 않았는가?
4. web/LLM accepted claim 0인데 Brain/Web ready라고 표현하는 문서나 리포트가 남아 있는가?
5. post_extraction_evidence_os rejection이 planner feedback에서 빠지는 것이 실제 병목이 맞는가?
6. P0-F를 넣었을 때 LLM에게 score/stage/current_score_eligible을 노출하지 않는가?
7. 일반 Naver result를 score source로 열어 월덱스식 오귀속을 재발시키지 않는가?
8. source_class가 문서별로 검사되는가, task 바구니 전체 source_class로 오귀속되지 않는가?
9. 114450 C05의 margin_bridge_visible을 계약 공시 제목이나 주가 기사로 억지 충족하지 않는가?
10. FULL_THESIS 승격 조건은 accepted web/LLM claim 0에서 계속 막히는가?
11. all-archetype replay는 6/32만 source-backed ready인데 goal complete로 말하지 않는가?
12. operational minimum count를 채우기 위해 production daily에서 unbounded fetch를 열지 않는가?
```

## 14. 교차검증 파일 지도

다음 파일들을 같이 봐야 한다.

```text
readiness_verdict.json
  최종 NOT_READY와 blockers

goal_completion_audit.json
  goal completion false와 pending gate

goal_requirement_matrix_audit.json
  17개 goal gate 중 13 PASS, 4 PENDING

brain_web_readiness_gate_audit.json
  Brain/Web 실행 수치와 web/LLM accepted claim 0

brain_stage_promotion_audit.json
  StageCourt trace는 있지만 promotion BLOCKED

full_thesis_production_runner_audit.json
  114450 C05 candidate 1개, FULL_THESIS promotion 0개

census_stage_status.jsonl
  3391 event-board Stage row, 모두 NOT_FULL_THESIS_STAGE

stagecourt_traces.jsonl
  StageCourt trace 자체는 존재하지만 일부는 pending material gaps

web_search_results.jsonl
  검색 결과 품질과 선택/거절 상태

web_fetched_documents.jsonl
  실제 fetch된 웹 문서 2개

claim_extractor_runs.jsonl
  LLM extractor 2회 성공, raw assertion 생성

raw_assertion_rejections.jsonl
  why LLM/web assertions did not become accepted claims

web_rejected_documents.jsonl
  pre-fetch/post-extraction rejection details

source_task_executions.jsonl
  official accepted vs baseline-only vs no evidence/provider failed
```

## 15. 현재 상태를 사용자에게 쉽게 설명하는 문장

사용자에게는 이렇게 말해야 한다.

```text
지금 Stage 라벨이 있는 종목은 있습니다.
하지만 그건 전체 종목을 훑으면서 붙인 상태판입니다.

실제 운영 파이프라인처럼 "원문 claim이 점수에 들어가고 StageCourt가 확정한 FULL_THESIS Stage"는 아직 0개입니다.

현재는 웹 검색과 LLM 추출까지는 실제로 돌게 됐지만,
가져온 웹 문서가 점수 source로 인정될 수준이 아니라서 accepted web/LLM claim이 0개입니다.

그래서 Green/Yellow를 억지로 만들지 않고 막힌 것은 맞고,
다음 패치는 일반 웹 문서를 점수로 풀어주는 게 아니라
실패 이유를 LLM planner에게 되돌려 더 좋은 원문 source route를 찾게 만드는 것입니다.
```

## 16. 현재 완료/미완료 판정

완료:

```text
CensusAssessmentEvent와 score evidence 분리
event-board Stage와 full thesis Stage 분리
claim 없는 score contribution 차단
source class DART:NEWS 오귀속 제거
policy rejected external task feedback retry
known-bad / controlled semantic replay 일부 통과
full unittest 5051 OK
```

미완료:

```text
Brain/Web evidence pass
web/LLM accepted claim >= 3
production FULL_THESIS row > 0
Samsung/Hynix full-thesis smoke
all-archetype source-backed replay parity
post-extraction rejection feedback retry
trusted/official source route quality improvement
```

최종 판정:

```text
NOT_READY가 맞다.
하지만 guard가 작동해서 잘못된 운영 Stage를 내보내지 않는 상태다.
다음 작업은 "점수를 느슨하게 열기"가 아니라 "더 좋은 source route를 찾아 accepted claim을 닫기"다.
```

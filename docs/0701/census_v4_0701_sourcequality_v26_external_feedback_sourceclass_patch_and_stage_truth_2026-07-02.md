# Census v4 0701 Sourcequality v26 External Feedback / Source-Class Patch

작성일: 2026-07-02 KST

## 0. 결론

v26 기준 결론은 냉정하게 아래다.

```text
READY 아님.
FULL_THESIS 운영 Stage 없음.
FULL_E2R_100 verified score 없음.
web/LLM accepted claim 없음.

다만 v24에서 끊기던 "Brain/Web 모드인데 웹 검색 0개" 문제는 일부 풀렸다.
v25/v26에서는 실제 web search, full-source fetch, LLM extractor까지 실행됐다.
```

쉽게 말하면:

```text
예전 상태:
  "웹까지 보겠다"고 해 놓고 실제 웹 검색을 한 번도 안 함.

현재 상태:
  웹 검색과 LLM 추출은 실제로 함.
  하지만 가져온 웹 문서가 점수에 넣을 수 있는 source-backed claim까지는 못 됨.
```

따라서 사용자에게 말할 수 있는 현재 상태는:

```text
Stage가 있는 애들이 있긴 하다:
  CENSUS_EVENT_BOARD 상태판 Stage는 있다.

하지만 운영 점수로 쓸 수 있는 FULL_THESIS Stage는 없다:
  verified_score / FULL_E2R_100 / FULL_THESIS row = 0.
```

## 1. v24 -> v25 -> v26 핵심 변화

### v24

산출물:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v24
```

핵심 수치:

```text
readiness = NOT_READY
leaf_artifact_audit = FAIL
leaf critical = web_claimed_but_zero_search_count: 1

planner_run_count = 21
real_provider_success_count = 1
source_task_execution_count = 13

web_search_task_count = 0
web_fetched_document_count = 0
llm_claim_extractor_attempt_count = 0
web_or_llm_accepted_claim_count = 0

FULL_THESIS candidate_row_count = 1
promoted_full_thesis_row_count = 0
```

v24의 직접 원인:

```text
LLM planner가 외부 확인 태스크를 만들긴 했다.
하지만 그 태스크를 delivery_schedule에 붙였다.
delivery_schedule은 DART 계약 공시로 풀 수 있는 official-solvable primitive다.
그래서 policy validator가 official_solvable_gap_sent_to_general_web로 막았다.
그런데 이 policy rejection이 source_rejection_feedback으로 LLM에 되돌아가지 않았다.
```

쉬운 예:

```text
납품일정은 계약서/DART 원문에서 확인해야 한다.
그걸 뉴스 검색으로 보내면 정책상 막는 게 맞다.

문제는 "막았다"에서 끝난 것이다.
LLM에게 "납품일정 말고 마진/현금흐름 bridge처럼 외부 보강이 필요한 슬롯으로 다시 짜라"를
되돌려 줬어야 했다.
```

### v25

산출물:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v25
```

패치 후 변화:

```text
leaf_artifact_audit = PASS
critical_count = 0

planner_run_count = 22
real_provider_success_count = 2
planner_run_role:
  initial = 21
  feedback_retry = 1
planner_feedback:
  previous_sources_rejected_before_extraction = 1

web_search_task_count = 7
web_search_result_count = 51
web_fetched_document_count = 2
web_rejected_document_count = 29
llm_claim_extractor_attempt_count = 2

official_accepted_claim_count = 36
web_or_llm_accepted_claim_count = 0
```

v25에서 좋아진 점:

```text
정책으로 막힌 외부 태스크가 조용히 사라지지 않았다.
source-level feedback으로 올라갔다.
LLM planner가 feedback_retry를 한 번 실행했다.
그 결과 margin_bridge_visible 쪽 외부 검색 태스크가 실제 실행됐다.
```

v25에서 남은 문제:

```text
외부 문서 2개를 가져오고 LLM extractor도 돌았지만,
accepted web/LLM claim은 0개였다.

대표 차단 이유:
  source_task_provider_error_score_block:general_search_not_score_source
  source_provider_document_type_mismatch:IndustryMedia:general_web_search_provider
  primitive_mapping_rejected:no_allowed_primitive_for_predicate
  margin_bridge_visible 직접 증거 부족
```

### v26

산출물:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v26
```

핵심 수치:

```text
readiness = NOT_READY
leaf_artifact_audit = PASS
critical_count = 0
runtime_plausibility = PASS_LIVE_RUNTIME_PLAUSIBILITY

source_task_execution_count = 13
official_accepted_claim_count = 24
web_or_llm_accepted_claim_count = 0

web_search_task_count = 4
web_search_call_count = 4
web_search_result_count = 38
web_fetched_document_count = 2
web_rejected_document_count = 28
llm_claim_extractor_attempt_count = 2

FULL_THESIS candidate_row_count = 1
promoted_full_thesis_row_count = 0
```

v26의 FULL_THESIS candidate:

```text
symbol = 114450
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
candidate_source = stagecourt_trace_direct_scan
present_primitives =
  contract_amount_to_prior_sales
  contract_duration_months
  delivery_schedule
missing_green_primitives =
  margin_bridge_visible
blocker =
  missing_green_gate_primitives
```

v26에서 고친 점:

```text
v25 raw rejection에 보이던 source_class_document_type_mismatch:DART:NEWS 오귀속을 제거했다.
```

왜 문제였나:

```text
같은 SourceTask 안에서 DART 공식자료와 웹 뉴스가 함께 병합될 수 있다.
이때 result 전체 source_class를 DART 하나로 들고 가면,
웹 뉴스 claim도 DART 문서처럼 검사되어 DART:NEWS mismatch가 찍힌다.
```

쉬운 예:

```text
계약 공시 원문 = DART 문서
추가 기사 = NEWS 문서

둘을 같은 바구니에 담았다고 해서
기사까지 DART 공시로 취급하면 안 된다.
문서별 source_type에 맞춰 검사해야 한다.
```

v26에서는 이 오귀속이 아래처럼 바뀌었다.

```text
source_class_document_type_mismatch:DART:NEWS
  -> 사라짐

남은 차단:
  source_provider_document_type_mismatch:TrustedNews:general_web_search_provider = 17
  source_task_provider_error_score_block:general_search_not_score_source = 12
  source_provider_document_type_mismatch:IndustryMedia:general_web_search_provider = 12
```

즉 이제 차단 이유는 더 정직하다.

```text
뉴스가 DART로 오인되어 막힌 것이 아니라,
Naver general search로 찾은 블로그/뉴스가 아직 score source로 인정되지 않아서 막힌다.
```

## 2. 이번 패치 내용

### P0-D. policy-rejected external task feedback

파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
tests/test_research_brain_v4_operational_modes.py
```

수정:

```text
기존:
  web_rejected_documents가 없으면 source_rejection_feedback = ()
  policy validator에서 막힌 외부 태스크는 feedback 없이 종료

변경:
  REJECTED_BY_POLICY인 외부 태스크도 source-level feedback으로 기록
  예: official_solvable_gap_sent_to_general_web
  accepted official claim이 있어도 별도 external task 실패가 있으면 retry 가능
```

이 패치가 막는 문제:

```text
공식자료 claim 1개가 accepted됨
외부 web task는 정책으로 실패함
그런데 accepted claim이 있다는 이유로 retry가 멈춤
-> Brain/Web 모드인데 web_search_task_count = 0
```

### P0-E. mixed official/web document source-class scoring guard

파일:

```text
src/e2r/research_brain/v4_evidence_extraction_bridge.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
```

수정:

```text
기존:
  SourceAcquisitionResult.source_class 하나로 모든 document score admissibility를 검사

변경:
  document.source_type이 NEWS인데 acquisition_source_class가 DART/KIND/KRX 같은 공식 class이면
  같은 task의 requested source classes 중 NEWS를 허용하는 class로 검사
  예: CompanyNewsroom / IndustryMedia / TrustedNews
```

이 패치가 막는 문제:

```text
웹 뉴스 문서를 DART 공시처럼 검사해서 source_class_document_type_mismatch:DART:NEWS가 찍힘
```

유지한 보호장치:

```text
BrokerReportPublicPDF 태스크에 일반 NEWS가 들어오면 여전히 차단된다.
general search provider가 가져온 IndustryMedia/TrustedNews 문서는 아직 score source로 인정하지 않는다.
```

## 3. 현재 Stage 존재 여부

v26 `census_stage_status.jsonl` 기준:

```text
stage_scope = CENSUS_EVENT_BOARD 3391
operator_stage_use = NOT_FULL_THESIS_STAGE 3391
verified_score_rows = 0
FULL_THESIS row = 0
FULL_E2R_100 row = 0
```

해석:

```text
Stage0/Stage1/Stage2-Watch/Red 같은 상태판 라벨은 있다.
하지만 이것은 전 종목 census board 상태다.
운영 점수로 쓸 수 있는 FULL_THESIS Stage는 없다.
```

쉬운 예:

```text
학교 전체 학생 명단에 "출석 확인됨 / 결석 / 상담 필요" 같은 상태가 붙은 것과,
실제 시험 답안지를 채점해서 90점, A등급을 확정한 것은 다르다.

현재 Census Event Board Stage는 전자다.
사용자가 원하는 FULL_THESIS 운영 Stage는 후자인데 아직 0개다.
```

## 4. 왜 114450은 승격되지 않았나

114450은 C05 계약 이벤트 후보로는 올라왔다.

확인된 것:

```text
contract_amount_to_prior_sales
contract_duration_months
delivery_schedule
```

아직 못 닫은 것:

```text
margin_bridge_visible
```

C05에서 중요한 이유:

```text
계약이 있다
  -> 후보/가시성 일부

계약금액과 기간이 크다
  -> 매출 가시성 일부

그 계약이 실제 마진/현금흐름/실적 개선으로 이어진다
  -> Green/FULL_THESIS에 필요한 bridge
```

즉:

```text
계약 공시만으로 Green을 주면 안 된다.
마진 bridge가 없으면 Stage 승격을 막는 게 맞다.
```

## 5. 아직 남은 핵심 병목

### 병목 1. web/LLM accepted claim = 0

v25/v26에서 웹 fetch와 LLM extractor는 실제로 돌았다.
하지만 accepted claim이 0이다.

가능한 원인:

```text
1. 가져온 문서가 블로그/일반 뉴스라 score source로 불허됨
2. LLM이 뽑은 claim이 primitive mapping에서 no_allowed_primitive_for_predicate로 reject됨
3. margin_bridge_visible에 필요한 원가/마진/현금흐름 직접 문장이 없음
4. TrustedNews / BrokerReport / CompanyNewsroom connector가 실제 trusted source로 닫히지 않음
```

다음 패치 방향:

```text
general Naver search 결과를 바로 score source로 풀지 말 것.
대신 source router가 결과를 다음 중 하나로 승격해야 한다.

  공식/회사 newsroom 원문
  실제 public broker report PDF
  독립 trusted news domain allowlist
  원문 fetch + source lineage + document type 검증

그 전까지는 fetch/LLM extraction은 diagnostic이며 score는 0이 맞다.
```

### 병목 2. operational minimum 미달

v26 readiness blockers:

```text
planner runs 22/30
web search tasks 4/20
web/news search calls 4/20
fetched documents 2/10
claim extractor attempts 2/10
web/LLM accepted claim 0
```

해석:

```text
이번 smoke 설정은 universe_limit=1, planner_success_limit=1이라
운영 minimum 30 planner runs / 20 web tasks를 채우지 못하는 게 자연스럽다.
```

다만:

```text
accepted web/LLM claim 0은 단순 규모 문제가 아니다.
source admissibility와 primitive mapping이 아직 못 닫힌 것이다.
```

### 병목 3. FULL_THESIS 승격은 계속 막혀야 한다

현재 상태에서 FULL_THESIS로 승격하면 안 된다.

승격 금지 이유:

```text
verified_score = 0 rows
web/LLM accepted = 0
margin_bridge_visible missing
StageCourt trace가 census_stage_status로 promoted되지 않음
```

## 6. 다음 에이전트 공격 질문

다음 리뷰어는 아래 질문을 먼저 때리면 된다.

```text
1. v26의 web/LLM extractor 성공 2건이 왜 accepted claim 0으로 끝났는가?
2. raw_assertion_rejections의 no_allowed_primitive_for_predicate가 맞는가, mapper가 너무 좁은가?
3. Naver general search로 가져온 문서를 어떤 조건에서 TrustedNews/CompanyNewsroom/BrokerReport로 승격할 수 있는가?
4. general web provider 문서를 score source로 바로 열면 월덱스/2020 감사 같은 오귀속이 재발하지 않는가?
5. 114450 C05에서 margin_bridge_visible을 공시/IR/리포트 중 어떤 source route로 닫아야 하는가?
6. source_task_executions 105/110개 중 공식 accepted claim은 충분한데 왜 FULL_THESIS score row는 0인가?
7. StageCourt trace direct scan 후보가 census_stage_status로 승격되려면 어떤 exact primitive/source quorum이 더 필요한가?
8. CENSUS_EVENT_BOARD Stage 라벨이 UI/report에서 운영 Stage처럼 보이는 경로가 남아 있는가?
9. v26에서 DART:NEWS 오귀속이 정말 사라졌는가?
10. policy-rejected external task feedback이 실제 planner prompt에 들어가고 query/source task 변화로 이어지는가?
```

## 7. 검증

Targeted tests:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_policy_rejected_external_task_becomes_source_feedback_without_web_rows \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_direct_acceptance_does_not_block_policy_rejected_external_task_retry \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_source_rejection_feedback_retries_planner_once \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_direct_source_task_acceptance_does_not_block_failed_external_source_feedback_retry -v

result:
  Ran 4 tests / OK
```

Module tests:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_census_v4_brain_web_readiness_gate -v

result:
  Ran 91 tests / OK
```

Full unittest:

```text
command:
  PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
    --artifact output/test_full_repo_0701/full_unittest_after_p0d_p0e_external_feedback_sourceclass_artifact.json \
    --log output/test_full_repo_0701/full_unittest_after_p0d_p0e_external_feedback_sourceclass.log \
    -- python -m unittest discover -s tests -v

status = OK
test_count = 5051
failed_count = 0
error_count = 0
duration_seconds = 190.5442
artifact =
  output/test_full_repo_0701/full_unittest_after_p0d_p0e_external_feedback_sourceclass_artifact.json
log_sha256 =
  4d31c61b2a03eb97ed1ef4b4cd189a4ab63742b841f3d11b98bd570802a045cc
```

## 8. 현재 판정

```text
P0-D policy-rejected external task feedback:
  fixed and live-proven by v25/v26.

P0-E mixed official/web source-class guard:
  fixed and live-proven by v26.

Brain/Web actual execution:
  improved.
  web search/fetch/extractor now actually run.

Brain/Web evidence pass:
  not passed.
  web_or_llm_accepted_claim_count = 0.

FULL_THESIS operation:
  not ready.
  FULL_THESIS row = 0.

User-facing answer:
  "Stage 상태판은 있지만 운영 FULL_THESIS Stage가 있는 종목은 아직 없다."
```

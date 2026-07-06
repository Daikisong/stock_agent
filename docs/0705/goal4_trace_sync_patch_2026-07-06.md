# Goal4 Trace Sync Patch - 2026-07-06

이 문서는 `goal4_runtime_attempt_after_source_task_guard_2026-07-06.md` 이후 진행한 추가 패치와 검증을 기록한다.

이번 작업도 Goal4 완료가 아니다. 이번 패치의 범위는 `unsafe promotion` 장부 오류를 줄이는 것이다.

쉬운 예:

```text
이전 상태:
임시 접수번호를 여러 장에 찍음
→ 최종 합격증은 일부만 발급됨
→ 그런데 임시 접수 장부에는 나머지도 "합격증 번호 있음"으로 남음
→ 감사가 dangling/mismatched promoted reference로 막음

이번 패치:
최종 합격증 목록을 기준으로 장부를 다시 맞춤
→ 최종 stage row에 없는 trace는 promoted=false / not_promoted=true로 정리
→ 최종 stage row에 있는 trace만 census_stage_status_id 유지
```

## 고친 문제

최신 Goal4 run의 `brain_stage_promotion_audit.json`에는 다음 blocker가 있었다.

```text
brain StageCourt trace is missing explicit not-promoted marker
brain_to_claim_trace promoted references are dangling or mismatched: 37
```

원인은 실행 순서였다.

```text
1. _promote_brain_stage_rows
   partial Brain trace를 census stage row로 올리고
   stagecourt_traces / brain_to_claim_trace에 promoted 표시를 씀

2. _apply_production_full_thesis_from_brain
   일부 partial row를 FULL_THESIS row로 바꾸거나 최종 stage row를 줄임

3. 최종 audit
   이전 partial promotion 표시가 그대로 남아 있어
   최종 stage row에 없는 trace도 promoted처럼 보임
```

즉 실제 증거가 좋아진 문제가 아니라 장부 동기화 문제였다.

## 코드 패치

파일:

```text
src/e2r/census/census_runner_v4.py
```

추가 함수:

```text
_sync_brain_trace_promotion_markers
```

역할:

```text
최종 stage_rows를 기준으로:
- 최종 stage row에 있는 SCT-BRAIN trace만 promoted=true 유지
- 최종 stage row에 없는 SCT-BRAIN trace는 promoted=false, not_promoted=true
- brain_to_claim_trace의 stale census_stage_status_id 제거
- 대표 score claim/contribution/primitive에 포함되지 않는 trace는 non-representative로 유지
```

호출 위치:

```text
run_census_mode_v4
→ full thesis / smoke / atomic merge / operator alias 이후
→ final output과 audit 작성 전에 호출
```

주의:

```text
이 패치는 점수나 Stage를 새로 만들지 않는다.
이미 최종 stage row로 남은 것과 trace ledger를 맞추는 정합성 패치다.
```

## 테스트

추가 테스트:

```text
tests/test_census_v4_brain_stage_promotion_gate.py
  test_final_stage_row_sync_clears_stale_brain_promotion_refs
```

검증 내용:

```text
stale promoted trace를 일부러 만든다.
최종 stage row에는 SCT-BRAIN-A 하나만 둔다.
sync 후 SCT-BRAIN-STALE은 census_stage_status_id=None이 된다.
brain_stage_trace_not_promoted_marker_missing_count=0
brain_trace_promoted_reference_error_count=0
```

실행한 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_stage_promotion_gate -v
```

결과:

```text
Ran 28 tests
OK
```

추가 관련 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_run_mode_honesty -v
```

결과:

```text
Ran 59 tests
OK
```

## 실제 run 검증

### 1. 전체 Goal4 재실행

명령:

```text
output_root:
output/census_v4/2026-07-06-goal4-runtime-attempt-after-trace-sync
```

이 실행은 2번째 planner batch에서 장시간 provider 대기 상태에 머물렀다.

관찰:

```text
planner_runs: 5
latest_phase: planner_batch_start
latest_event_index: 5
process state: do_sys_poll
하위 codex provider process 존재
파일 갱신 없음
```

처리:

```text
Ctrl-C로 중단
exit_code: 130
stdout: INVALID_PARTIAL_OUTPUT
```

해석:

```text
이건 Goal4 pass/fail 판정이 아니라 provider stall이다.
최종 audit까지 도달하지 못했으므로 전체 Goal4 완료 증거로 사용할 수 없다.
```

### 2. Bounded trace-sync smoke

목적:

```text
전체 Goal4 완료가 아니라,
trace-sync 패치가 실제 run 종료 구간에서 동작하는지 확인
```

명령 조건:

```text
output_root:
output/census_v4/2026-07-06-goal4-trace-sync-bounded-smoke

brain_universe_limit: 5
brain_planner_success_limit: 5
brain_max_distinct_candidate_attempts: 5
brain_accepted_claim_target: 5
write_operational_docs: false
```

결과:

```text
exit_code: 1
status: INVALID_PARTIAL_OUTPUT
```

중요한 점:

```text
이 smoke도 Goal4 완료가 아니다.
작은 실행이라 Brain/Web 운영 최소 수량을 일부러 만족하지 않는다.
```

하지만 trace-sync 관련 audit은 개선됐다.

`brain_stage_promotion_audit.json`:

```text
verdict: PROMOTION_APPLIED
blockers: []
brain_promoted_stage_row_count: 2
unsafe_promoted_stage_row_count: 0
brain_stage_trace_not_promoted_marker_missing_count: 0
brain_trace_promoted_reference_error_count: 0
web_or_llm_accepted_claim_count: 0
```

장부 상태:

```text
brain_stagecourt: 4
not_promoted=true: 2
not_promoted=false: 2
missing marker: 0
brain_to_claim css refs: 4
final SCT-BRAIN stage rows: 2
```

즉 stale promoted reference 문제는 bounded run에서 재현되지 않았다.

## 남은 blocker

bounded smoke의 `brain_web_readiness_gate_audit.json`은 여전히 `BLOCKED`다.

주요 blocker:

```text
Brain/Web acquisition mode requires web/news search task rows
Brain/Web acquisition mode requires fetched full-source web/news documents
web/LLM accepted claim count is zero
Brain/Web operational minimum planner calls not met: 5/30
Brain/Web operational minimum web search tasks not met: 0/20
Brain/Web operational minimum web/news search calls not met: 0/20
Brain/Web operational minimum fetched documents not met: 0/10
Brain/Web operational minimum claim extractor attempts not met: 0/10
Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

이건 정상적인 blocker다.

쉬운 예:

```text
장부 번호 꼬임은 고쳤다.
하지만 웹/뉴스/LLM이 실제로 새 증거 claim을 만든 것은 아직 0개다.
따라서 운영 합격은 여전히 줄 수 없다.
```

## 추가 원인 분석: web/LLM accepted claim 0

bounded smoke를 더 추적해 보니 `web/LLM accepted claim count = 0`은 단순히 claim extractor가 약한 문제가 아니었다.

관찰된 상태:

```text
claim_extractor_runs.jsonl: 0 rows
web_search_tasks.jsonl: 0 rows
web_fetched_documents.jsonl: 0 rows
source_task_executions.jsonl: 외부 원문 task는 존재
```

대표 예:

```text
task:
  preferred_source_classes:
    - BrokerReportPublicPDF
    - ReportPDF
    - CompanyNewsroom
  fallback_source_classes:
    - IssuerIR
    - CompanyGuide
  primitive_gap:
    customer_preorder_or_allocation
  query_intents:
    SK하이닉스 000660 HBM customer allocation report ...

기대:
  LLM이 만든 target-scoped query로 bounded web/report fetch 실행

실제:
  먼저 live_official_source_provider_registry를 호출
  fallback official connector가 query budget을 소비
  남은 web budget이 0
  web_search_tasks/web_fetched_documents가 생성되지 않음
```

쉬운 예:

```text
리포트 원문을 찾으라고 "증권사 리포트 창구" 티켓을 끊었다.
그런데 입구에서 "공식 IR 창구도 fallback에 있네"라고 보고
IR 창구에 먼저 줄을 세웠다.
티켓이 1장뿐이면 IR 창구에서 실패한 뒤
정작 리포트 창구에는 가보지도 못한다.
```

이 문제는 LLM query를 코드가 새로 만드는 문제가 아니다.

```text
LLM query_intents는 이미 존재했다.
문제는 그 query를 실행하는 bounded web leaf까지 도달하지 못한 것이다.
```

따라서 deterministic fallback 검색어를 추가하지 않았다.

## 추가 코드 패치: external-original web-first leaf

파일:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
```

추가/변경:

```text
_EXTERNAL_WEB_SOURCE_CLASSES
_task_prefers_external_web
```

새 규칙:

```text
LIVE_FULL_BOUNDED에서
preferred_source_classes의 첫 source class가 외부 원문 계열이면
공식 fallback connector보다 bounded web acquisition을 먼저 실행한다.
```

외부 원문 계열:

```text
NaverSearch
GeneralWebSearch
TrustedNews
News
IndustryMedia
CompanyNewsroom
ReportPDF
BrokerReportPublicPDF
```

유지되는 기존 규칙:

```text
preferred_source_classes가 DART / CompanyGuide / IssuerIR 같은 공식 source로 시작하면
기존처럼 official-first로 실행한다.

official-solvable contract/fcf gap을 general web으로 보내는 정책 차단은 유지한다.
target-scoped LLM query가 없으면 web search를 실행하지 않는다.
top_results=None 같은 무제한 검색도 도입하지 않는다.
```

쉬운 예:

```text
BrokerReportPublicPDF -> IssuerIR
  리포트 원문을 먼저 찾는다.
  IR은 fallback 성격이다.

DART -> TrustedNews
  공시를 먼저 본다.
  뉴스는 남은 budget 안에서만 본다.
```

web fetch 상태 라벨도 같이 정리했다.

```text
검색 결과가 아예 없음
  -> NO_EVIDENCE_FOUND

검색 결과는 있었지만 target 불일치, 저품질 블로그, 주가 프로필 페이지 등으로 모두 탈락
  -> PROVIDER_FAILED
```

쉬운 예:

```text
아무 문서도 못 찾음
  -> 빈 서랍

문서는 찾았지만 모두 점수 증거로 못 씀
  -> 서랍에는 종이가 있는데 답안지가 아님
```

## 추가 테스트

추가 테스트:

```text
tests/test_research_brain_v4_real_source_acquisition.py
  test_live_full_bounded_external_preferred_preserves_single_query_budget_for_web
```

검증 내용:

```text
preferred_source_classes = BrokerReportPublicPDF
fallback_source_classes = IssuerIR, CompanyGuide
max_queries = 1

이전:
  CompanyGuide fallback이 query budget 1개를 먼저 소비
  web/report fetch가 실행되지 않음

패치 후:
  CompanyGuide connector는 호출되지 않음
  LLM query_intent로 bounded web search 실행
  BrokerReportPublicPDF 문서 1개 fetch
```

같이 확인한 회귀:

```text
tests/test_research_brain_v4_real_source_acquisition.py
  test_live_full_bounded_keeps_official_first_and_web_fallback_leafs

tests/test_research_brain_v4_operational_modes.py
  test_live_full_bounded_web_fallback_uses_remaining_task_budget_after_official
```

이 두 테스트는 공식-first 혼합 task가 그대로 유지되는지 본다.

실행:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_real_source_acquisition -v
```

결과:

```text
Ran 45 tests
OK
```

추가 관련 묶음:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_brain_stage_promotion_gate -v
```

결과:

```text
Ran 141 tests
OK
```

## 현재까지의 판단

이번 0705 패치 세트로 줄인 문제:

```text
1. 최종 stage row와 Brain trace promotion marker 불일치
2. 외부 원문 preferred task가 공식 fallback에 query budget을 빼앗겨 web leaf까지 못 가는 문제
3. web rejected 문서를 단순 no-evidence로 흐리는 상태 라벨 문제
```

아직 해결되지 않은 문제:

```text
1. 전체 Goal4 run은 provider stall 때문에 최종 audit까지 못 감
2. 실제 full Goal4에서 web_search_tasks/web_fetched_documents/LLM accepted claim이 충분히 생기는지 미검증
3. claim_extractor_runs가 live full bounded 실제 run에서 의미 있게 발생하는지 미검증
4. C05 외 전체 아키타입 runtime parity matrix는 아직 완료 아님
```

따라서 지금 상태는:

```text
patch verified
Goal4 complete 아님
production full-thesis parity ready 아님
```

## 추가 bounded smoke: external web route 확인

external-original web-first 패치 후 작은 bounded smoke를 다시 실행했다.

명령 요약:

```text
output_root:
output/census_v4/2026-07-06-goal4-external-web-route-bounded-smoke

run_mode: BRAIN_AND_WEB_ACQUISITION_ENABLED
brain_source_acquisition: live_full_bounded
brain_universe_limit: 5
brain_planner_success_limit: 5
brain_max_distinct_candidate_attempts: 5
brain_accepted_claim_target: 5
write_operational_docs: false
target_gate: full_thesis
```

결과:

```text
exit_code: 1
stdout: NOT_READY
```

중요한 artifact count:

```text
planner_runs.jsonl: 50
source_tasks.jsonl: 127
source_task_executions.jsonl: 127
web_search_tasks.jsonl: 3
web_search_results.jsonl: 1
web_fetched_documents.jsonl: 0
web_rejected_documents.jsonl: 1
claim_extractor_runs.jsonl: 0
accepted_claims.jsonl: 96
brain_to_claim_trace.jsonl: 13
stagecourt_traces.jsonl: 96
```

이전 bounded smoke와 비교:

```text
이전:
  web_search_tasks = 0
  web_fetched_documents = 0
  web/LLM accepted claims = 0

패치 후:
  web_search_tasks = 3
  web_fetched_documents = 0
  web/LLM accepted claims = 0
```

해석:

```text
external-original task가 bounded web acquisition leaf까지 내려가는 문제는 일부 개선됐다.
하지만 실제 fetched full-source web/news document는 아직 0이다.
따라서 LLM claim extractor도 실행되지 않았고, web/LLM accepted claim도 0이다.
```

대표 web task:

```text
005930 Samsung Electronics HBM customer allocation preorder capacity sold out broker report PDF before 2026-07-05
005930 Samsung Electronics HBM capacity constraint allocation sold out broker report PDF before 2026-07-05
033100 lead time extended delivery backlog datacenter power grid broker report PDF before 2026-07-05
```

web result/rejection:

```text
MiraeAsset PDF 1건 검색됨
rejection_reason:
  web_fetch_target_not_in_title_snippet_or_lead
```

readiness blocker:

```text
Brain/Web acquisition mode requires fetched full-source web/news documents
web/LLM accepted claim count is zero
Brain/Web operational minimum planner calls not met: 5/30
Brain/Web operational minimum web search tasks not met: 3/20
Brain/Web operational minimum fetched documents not met: 0/10
Brain/Web operational minimum claim extractor attempts not met: 0/10
Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

trace-sync 쪽은 여전히 깨지지 않았다.

```text
brain_stage_promotion_audit.verdict: PROMOTION_APPLIED
blockers: []
unsafe_promoted_stage_row_count: 0
brain_trace_promoted_reference_error_count: 0
brain_stage_trace_not_promoted_marker_missing_count: 0
```

남은 문제를 더 구체화하면 다음과 같다.

```text
1. LLM planner가 web query를 만들고 web_search_tasks까지는 내려간다.
2. 검색 결과가 없거나, fetched text relevance gate에서 막혀 web_fetched_documents가 0이다.
3. fetched document가 없으므로 LLM claim extractor가 실행되지 않는다.
4. web/LLM accepted claim이 0이라 Brain/Web readiness는 계속 BLOCKED다.
```

쉬운 예:

```text
이전:
  리포트 창구로 가는 문 자체가 안 열렸다.

지금:
  리포트 창구까지는 갔다.
  그런데 서류를 못 찾거나, 가져온 서류가 대상 회사 본문 증거로 인정되지 않았다.
  그래서 채점 가능한 새 claim은 아직 없다.
```

주의할 추가 관찰:

```text
web_search_tasks 일부 row에서 company_name이 실제 회사명이 아니라 target archetype ID처럼 보인다.
예:
  symbol: 005930
  company_name: C06_HBM_MEMORY_CUSTOMER_CAPACITY

query에는 Samsung Electronics가 들어 있어 search는 실행됐지만,
target alias/relevance 판정에는 이 seed metadata가 영향을 줄 수 있다.
다음 작업에서 seed event의 company_name/entity identity가 실제 회사명으로 유지되는지 확인해야 한다.
```

## 다음 작업

1. 전체 Goal4 run의 provider stall 원인을 분리한다.
   - 2번째 planner batch에서 provider subprocess가 대기한 이유 확인
   - planner call timeout 또는 batch-level timeout 감사 필요

2. web/news/LLM accepted claim 0 문제를 직접 추적한다.
   - external-original web-first 패치 후 source_task_drafts가 web/news route까지 실제 execution으로 내려가는지 재확인
   - web_search_tasks는 생기기 시작했으므로, 이제 web_fetched_documents가 0인 원인을 URL/alias/relevance gate 단위로 분해한다
   - seed event의 company_name/entity identity가 archetype id로 오염되는지 확인한다
   - claim_extractor_runs가 왜 0 또는 accepted 0으로 남는지 확인
   - 공식-only accepted claim과 Brain/Web accepted claim을 계속 분리한다

3. source_task budget cap exceeded는 전체 run에서 다시 확인한다.
   - bounded smoke에서는 0이었다
   - 이전 전체 run에서는 6이었다
   - cap 초과가 어떤 task에서 발생하는지 task_id 단위로 출력해야 한다

4. 최종 목표는 여전히 그대로다.

```text
C05 외 C01~C32/C36 전체에 대해:
- attempt 존재
- source route 존재
- source execution 존재
- accepted claim 존재 또는 명시적 source/provider blocker 존재
- full thesis 상태가 전수 matrix로 증명됨
```

이번 패치는 그중 `promotion trace ledger가 최종 stage row와 불일치하는 문제`를 줄인 것이다.

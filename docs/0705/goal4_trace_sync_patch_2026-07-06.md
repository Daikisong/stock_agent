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

## 추가 패치: seed company_name 아키타입 오염 차단

위 관찰은 실제 코드 경로의 버그였다.

문제 경로:

```text
seed row:
  symbol: 005930
  company_name: null
  target_archetype: C06_HBM_MEMORY_CUSTOMER_CAPACITY

기존 fallback:
  company_name = payload.company_name
              or structured_payload.target_archetype
              or payload.target_archetype
              or symbol

결과:
  company_name = C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

쉬운 예:

```text
삼성전자를 조사해야 하는데,
접수 장부의 이름 칸에 "삼성전자"가 아니라
"C06_HBM_MEMORY_CUSTOMER_CAPACITY"라고 적힌 상태였다.

검색어에는 LLM이 Samsung Electronics를 넣을 수 있어도,
후속 target alias/relevance 판정에서는 회사 정체성이 흐려질 수 있다.
```

수정:

```text
src/e2r/research_brain/v4_production_orchestrator.py
  - _candidate_seed_events_from_config(repo_root)로 instrument registry를 읽는다.
  - company_name이 비어 있거나 Cxx_/R13_ 아키타입 ID처럼 보이면:
      1. symbol이 있으면 registry.names_by_symbol[symbol] 사용
      2. registry에 없으면 symbol 사용
      3. symbol 없는 archetype-level discovery seed만 target_archetype 사용 허용
```

즉 종목별 seed에서는 아키타입 ID가 회사명으로 들어가지 못하게 막았다.

예:

```text
005930 + company_name null + C06 target
  이전: C06_HBM_MEMORY_CUSTOMER_CAPACITY
  이후: 삼성전자

031980 + registry name 없음
  이전: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
  이후: 031980
```

두 번째 예시는 완전한 회사명 복구는 아니지만, 적어도 아키타입을 회사명으로 오인하지 않는다.
registry 보강은 별도 데이터 품질 작업이다.

추가 테스트:

```text
tests/test_research_brain_v4_operational_modes.py
  test_candidate_event_seed_path_resolves_missing_company_name_from_registry_not_archetype
```

검증 내용:

```text
임시 universe registry:
  005930 -> 삼성전자

seed:
  symbol=005930
  company_name=None
  target_archetype=C06_HBM_MEMORY_CUSTOMER_CAPACITY

기대:
  CandidateEvent.company_name == 삼성전자
  CandidateEvent.company_name != C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_real_source_acquisition -v
```

결과:

```text
Ran 124 tests
OK
```

추가 관련 묶음:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_brain_stage_promotion_gate -v
```

결과:

```text
Ran 63 tests
OK
```

seed materialization 확인:

```text
docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl
→ _candidate_seed_events_from_config 재해석

events: 111
symbol-specific row 중 company_name이 Cxx_/R13_ 아키타입 ID인 row: 0
blank company_name: 0
```

대표 row:

```text
052400 -> 코나아이 / C01_ORDER_BACKLOG_MARGIN_BRIDGE
033100 -> 제룡전기 / C02_POWER_GRID_DATACENTER_CAPEX
005930 -> 삼성전자 / C06_HBM_MEMORY_CUSTOMER_CAPACITY
035760 -> CJ ENM / C27_CONTENT_IP_GLOBAL_MONETIZATION
```

주의:

```text
"CJ ENM"처럼 회사명이 C로 시작하는 정상 케이스는 있다.
그래서 단순 startswith("C")가 아니라 ^(C\d{2}|R13)_ 패턴만 아키타입 오염으로 본다.
```

## 추가 bounded smoke: seed company resolver 확인

패치 후 같은 작은 bounded smoke를 다시 실행했다.

명령 요약:

```text
output_root:
output/census_v4/2026-07-06-goal4-seed-company-resolver-bounded-smoke

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

artifact count:

```text
planner_runs.jsonl: 50
source_tasks.jsonl: 132
source_task_executions.jsonl: 132
web_search_tasks.jsonl: 5
web_search_results.jsonl: 15
web_fetched_documents.jsonl: 0
web_rejected_documents.jsonl: 13
claim_extractor_runs.jsonl: 0
accepted_claims.jsonl: 96
brain_to_claim_trace.jsonl: 18
stagecourt_traces.jsonl: 96
```

회사명 오염 확인:

```text
research_brain_candidate_seed_events_used.jsonl:
  rows: 111
  bad_archetype_company_names: 0

web_search_tasks.jsonl:
  rows: 5
  bad_archetype_company_names: 0

source_tasks.jsonl:
  rows: 132
  bad_archetype_company_names: 0
```

대표 web task:

```text
005930 / 삼성전자:
  삼성전자 005930 HBM 고객 allocation 선주문 물량 배정 리포트 PDF 2025 2026
  삼성전자 005930 HBM customer allocation preorder capacity sold out broker report PDF 2025 2026
  삼성전자 005930 HBM 고객사 qualification 물량 배정 공급계약 리포트 2025 2026

033100 / 제룡전기:
  제룡전기 033100 리포트 변압기 납기 장기화 리드타임 수주잔고 2025
```

즉 이번 patch의 직접 목표였던 `company_name=아키타입 ID` 문제는 smoke artifact에서도 사라졌다.

하지만 Brain/Web readiness는 여전히 막혔다.

```text
brain_web_readiness_gate_audit.verdict: BLOCKED

blockers:
  Brain/Web acquisition mode requires fetched full-source web/news documents
  web/LLM accepted claim count is zero
  Brain/Web operational minimum planner calls not met: 5/30
  Brain/Web operational minimum web search tasks not met: 5/20
  Brain/Web operational minimum fetched documents not met: 0/10
  Brain/Web operational minimum claim extractor attempts not met: 0/10
  Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

trace promotion 쪽은 계속 깨지지 않았다.

```text
brain_stage_promotion_audit.verdict: PROMOTION_APPLIED
blockers: []
unsafe_promoted_stage_row_count: 0
brain_stage_trace_not_promoted_marker_missing_count: 0
brain_trace_promoted_reference_error_count: 0
```

이번 smoke의 rejected web document 원인:

```text
web_result_low_quality_blog_or_social_not_score_source: 7
live_pdf_text_extraction_failed:pypdf extraction failed: Stream has ended unexpectedly: 3
web_result_stock_list_or_channel_page_not_source_document: 2
web_fetch_target_not_in_title_snippet_or_lead: 1
```

쉬운 예:

```text
이전:
  이름표부터 "삼성전자"가 아니라 "C06..."이라 잘못 붙어 있었다.

이번:
  이름표는 "삼성전자"로 고쳤다.
  검색도 5번 실행됐다.
  그런데 가져온 후보는 블로그/목록 페이지이거나,
  PDF 본문 추출이 실패해서 아직 답안지로 인정된 문서가 0개다.
```

PDF 추출 상태:

```text
src/e2r/research/pdf_text_extractor.py는
PyMuPDF -> pdfplumber -> pypdf 순서로 fallback하도록 되어 있다.

현재 환경:
  PyMuPDF 없음
  pdfplumber 없음
  pypdf 있음

따라서 특이하거나 일부 깨진 증권사 PDF가 pypdf에서 실패하면
web_fetched_documents로 승격되지 못한다.
```

이건 이번 seed identity patch와 별개의 다음 source acquisition 문제다.

## 추가 패치: live PDF body cap 분리

위 smoke에서 남은 핵심 blocker 중 하나는 PDF 원문 fetch가 중간에서 깨지는 문제였다.

관찰:

```text
web_rejected_documents:
  live_pdf_text_extraction_failed:pypdf extraction failed: Stream has ended unexpectedly
```

초기 해석은 "pypdf가 약하다"였지만, 코드를 확인하니 더 앞단 문제가 있었다.

기존 `PageFetcher`:

```text
모든 live response body를 max_body_bytes=2,000,000 기준으로 읽음
길면 2MB에서 잘라냄
PDF도 잘린 bytes를 그대로 PDFTextExtractor에 전달
```

쉬운 예:

```text
책을 200쪽까지 읽어야 목차와 끝 인덱스가 맞는데,
앞 80쪽만 찢어서 PDF 리더에게 넘긴 상태였다.
그러면 "문서 끝 구조가 없다"는 식의 오류가 날 수 있다.
```

수정:

```text
src/e2r/research/page_fetcher.py
  - max_pdf_body_bytes 기본값 25,000,000 추가
  - PDF URL 또는 PDF content-type이면 PDF 전용 cap으로 읽음
  - PDF가 cap을 넘으면 live_fetch_body_too_large:pdf:<cap>로 실패 처리
  - cap을 넘은 PDF를 잘라서 추출기에 넘기지 않음
```

중요한 점:

```text
무제한 fetch가 아니다.
HTML 일반 cap은 유지한다.
PDF만 bounded cap을 따로 둔다.
너무 큰 PDF는 score evidence가 아니라 명시적 source/provider blocker가 된다.
```

추가 테스트:

```text
tests/test_web_research_runner.py
  test_page_fetcher_live_pdf_uses_pdf_body_cap_not_html_body_cap
  test_page_fetcher_live_pdf_too_large_fails_without_truncated_extraction
```

검증 내용:

```text
max_body_bytes=10, max_pdf_body_bytes=200인 경우:
  90바이트 PDF는 10바이트로 잘리지 않고 전체 payload가 extractor에 전달된다.

max_pdf_body_bytes=20인 경우:
  90바이트 PDF는 extractor에 전달되지 않고 live_fetch_body_too_large로 실패한다.
```

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_web_research_runner.WebResearchRunnerTests.test_page_fetcher_live_extracts_pdf_text_and_uses_cache \
  tests.test_web_research_runner.WebResearchRunnerTests.test_page_fetcher_live_pdf_uses_pdf_body_cap_not_html_body_cap \
  tests.test_web_research_runner.WebResearchRunnerTests.test_page_fetcher_live_pdf_too_large_fails_without_truncated_extraction -v
```

결과:

```text
Ran 3 tests
OK
```

직접 URL 확인:

```text
https://stock.pstatic.net/stock-research/industry/2/20250521_industry_331196000.pdf
  ok=True
  content_type=application/octet-stream
  text_len=122295

https://files-scs.pstatic.net/2026/03/06/zTRK9jeXuU/260306(%EA%B8%88)%20Signal%20Report.pdf
  ok=True
  content_type=application/pdf
  text_len=70054
```

이 두 URL은 이전 smoke에서 `Stream has ended unexpectedly` 계열로 탈락했던 URL과 같은 계열이다.

## 추가 bounded smoke: PDF body cap 확인

패치 후 같은 작은 bounded smoke를 다시 실행했다.

명령 요약:

```text
output_root:
output/census_v4/2026-07-06-goal4-pdf-body-cap-bounded-smoke

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

artifact count:

```text
planner_runs.jsonl: 50
source_tasks.jsonl: 127
source_task_executions.jsonl: 127
web_search_tasks.jsonl: 5
web_search_results.jsonl: 45
web_fetched_documents.jsonl: 5
web_rejected_documents.jsonl: 27
claim_extractor_runs.jsonl: 5
accepted_claims.jsonl: 97
brain_to_claim_trace.jsonl: 14
stagecourt_traces.jsonl: 96
```

직전 smoke와 비교:

```text
이전 seed-company-resolver smoke:
  web_search_tasks: 5
  web_fetched_documents: 0
  claim_extractor_runs: 0
  web/LLM accepted claims: 0

이번 PDF body cap smoke:
  web_search_tasks: 5
  web_fetched_documents: 5
  claim_extractor_runs: 5
  web/LLM accepted claims: 1
```

즉 이전 blocker였던:

```text
Brain/Web acquisition mode requires fetched full-source web/news documents
web/LLM accepted claim count is zero
```

는 작은 smoke 수준에서는 각각 다음 상태까지 전진했다.

```text
fetched full-source web/news documents: 5
web/LLM accepted claim count: 1
```

대표 accepted claim:

```text
symbol: 005930
company_name: 삼성전자
archetype: C06_HBM_MEMORY_CUSTOMER_CAPACITY
primitive_id: customer_preorder_or_allocation
source_provider: BrokerReportDomain
source_url: https://stock.pstatic.net/stock-research/industry/40/20250903_industry_798204000.pdf
raw_assertion_id: RAWLLM-a1aee2235034cb87a83c
satisfaction_type: DIRECT_ACCEPTED_CLAIM
score_eligible: true
quote:
  삼성전자는 서버 및 HBM 비중의 점진적 확대로 힘입어 ...
```

쉬운 예:

```text
이전:
  검색은 했지만 PDF를 못 열어서 답안지 작성자가 한 번도 일하지 못함.

이번:
  PDF 5개를 실제 텍스트로 열었고,
  LLM extractor도 5번 돌았고,
  그중 삼성전자 C06 customer/allocation 계열 accepted claim 1건이 생김.
```

아직 남은 blocker:

```text
brain_web_readiness_gate_audit.verdict: BLOCKED

blockers:
  Brain/Web operational minimum planner calls not met: 5/30
  Brain/Web operational minimum web search tasks not met: 5/20
  Brain/Web operational minimum web/news search calls not met: 5/20
  Brain/Web operational minimum fetched documents not met: 5/10
  Brain/Web operational minimum claim extractor attempts not met: 5/10
  Brain/Web operational minimum web/LLM accepted claims not met: 1/3
```

trace promotion 쪽은 여전히 깨지지 않았다.

```text
brain_stage_promotion_audit.verdict: PROMOTION_APPLIED
blockers: []
unsafe_promoted_stage_row_count: 0
brain_stage_trace_not_promoted_marker_missing_count: 0
brain_trace_promoted_reference_error_count: 0
```

현재 상태 해석:

```text
PDF fetch/extraction 경로는 0에서 5 fetched + 1 accepted claim까지 전진했다.
하지만 Goal4 완료는 아니다.
전수 matrix 목표에는 아직 최소 운영 수량과 C01~C32/C36 전체 아키타입 coverage가 부족하다.
```

## 추가 패치: C06 HBM 비중 문장 과잉 매핑 차단

위 PDF body cap smoke에서 생긴 `web/LLM accepted claim 1건`은 다시 검토해야 했다.

대표 accepted claim은 다음이었다.

```text
primitive_id:
  customer_preorder_or_allocation

quote:
  삼성전자는 서버 및 HBM 비중의 점진적 확대로 힘입어 ...
```

문제:

```text
HBM 비중 확대
  -> 제품/매출 mix 또는 profile 증거일 수 있음

고객 물량 배정 / 선주문 / capacity allocation
  -> customer_preorder_or_allocation 증거
```

둘은 같은 말이 아니다.

쉬운 예:

```text
"가게 매출에서 커피 비중이 늘었다"
  -> 커피가 잘 팔렸다는 말일 수 있다.

"A 고객이 다음 달 커피 물량 1만 잔을 선주문했다"
  -> 고객 배정/선주문 증거다.

첫 문장을 두 번째 문장처럼 점수에 넣으면 안 된다.
```

원인:

```text
LLM extractor가 predicate를 customer_allocation_or_qualification_claim으로 붙이면
기존 mapper가 그 predicate만 보고
customer_preorder_or_allocation / qualification_status / revenue_visibility_contract 중
첫 허용 primitive로 매핑할 수 있었다.
```

즉 원문 quote에 고객 배정이나 qualification 표현이 없어도,
LLM 라벨이 강하면 C06 customer allocation 칸으로 들어갈 여지가 있었다.

수정:

```text
src/e2r/production/claim_extraction/primitive_mapper.py
  - customer_allocation_or_qualification_claim 전용 guard 추가
  - 원문 quote/object에 명시적인 고객 배정/선주문/capacity allocation 표현이 있어야
    customer_preorder_or_allocation 허용
  - "고객 allocation"처럼 한국어 고객 + 영어 allocation이 같이 있는 혼합 표현도 허용
  - 원문 quote/object에 명시적인 고객 qualification/인증/승인/검증 표현이 있어야
    qualification_status 허용
  - predicate 문자열 자체는 원문 증거로 사용하지 않음
  - HBM 비중 확대만 있으면 REJECTED
```

중요한 점:

```text
이건 종목 하드코딩이 아니다.
삼성전자 예외도 아니고, C06을 무조건 낮추는 것도 아니다.

증거 칸의 의미를 지킨 것이다.
customer_preorder_or_allocation 칸에는 "고객 배정/선주문" 증거가 들어가야 한다.
HBM 매출 비중 확대는 다른 primitive로 검토할 수 있지만,
고객 배정 증거로 둔갑하면 안 된다.
```

추가 테스트:

```text
tests/test_cutover_contract_blind_extraction.py
  test_hbm_mix_text_does_not_map_to_customer_allocation_primitive
  test_explicit_customer_allocation_text_maps_to_customer_allocation_primitive

tests/test_research_brain_v4_evidence_extraction_from_real_document.py
  test_hbm_mix_quote_does_not_satisfy_customer_allocation_task
```

검증 내용:

```text
"삼성전자는 서버 및 HBM 비중의 점진적 확대로 2위를 유지했다."
  -> customer_preorder_or_allocation REJECTED

"삼성전자는 2026년 HBM 고객 물량 배정이 확정됐다고 밝혔다."
  -> customer_preorder_or_allocation ACCEPTED

"SK하이닉스는 HBM 수요 증가와 고객 allocation이 확대되고 있다."
  -> customer_preorder_or_allocation ACCEPTED
```

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_cutover_contract_blind_extraction \
  tests.test_research_brain_v4_evidence_extraction_from_real_document -v
```

결과:

```text
Ran 51 tests
OK
```

관련 웹/소스 획득 회귀:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_web_research_runner \
  tests.test_research_brain_v4_real_source_acquisition -v
```

결과:

```text
Ran 92 tests
OK
```

추가로 전체 테스트에서 C06 source-backed replay가 한 번 깨졌다.

원인:

```text
fixture quote:
  SK하이닉스는 HBM 수요 증가와 고객 allocation이 확대되고 있다.

초기 guard:
  영어 customer + allocation
  또는 한국어 고객 + 배정
  만 허용

결과:
  한국어 고객 + 영어 allocation 혼합 표현을 놓침
```

이건 HBM 비중 확대를 허용해야 한다는 뜻이 아니다.

쉬운 예:

```text
"HBM 비중이 늘었다"
  -> 고객 배정 증거 아님

"고객 allocation이 확대됐다"
  -> 고객 배정/allocation 증거
```

보정:

```text
고객 allocation
고객사 allocation
또는 원문에 "고객"과 "allocation"이 같이 있는 경우
customer_preorder_or_allocation으로 허용
```

재검증:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_cutover_contract_blind_extraction.CutoverContractBlindExtractionTests.test_hbm_mix_text_does_not_map_to_customer_allocation_primitive \
  tests.test_cutover_contract_blind_extraction.CutoverContractBlindExtractionTests.test_explicit_customer_allocation_text_maps_to_customer_allocation_primitive \
  tests.test_cutover_contract_blind_extraction.CutoverContractBlindExtractionTests.test_korean_customer_with_english_allocation_maps_to_customer_allocation \
  tests.test_census_v4_all_archetype_replay_matrix.CensusV4AllArchetypeReplayMatrixTests.test_c06_source_backed_semantic_replay_passes_without_treating_smoke_as_production \
  tests.test_census_v4_all_archetype_replay_matrix.CensusV4AllArchetypeReplayMatrixTests.test_c06_guard_replay_blocks_qualification_lag_false_positive -v
```

결과:

```text
Ran 5 tests
OK
```

직접 C06 replay 산출 확인:

```text
c06_source_backed_semantic_replay.positive_replay_pass: true
accepted_primitive_ids: [customer_preorder_or_allocation]
accepted_claim_count: 1
document_urls:
  https://ssl.pstatic.net/imgstock/upload/research/company/sk_hynix_memory_20240401.pdf

c06_guard_replay_audit.guard_replay_pass: true
positive_replay_ready: true
source_backed_positive_replay_ready: true
positive_semantic_replay_ready: true
```

실패했던 Goal4 감사 묶음 재검증:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_all_archetype_replay_matrix \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_run_mode_honesty -v
```

결과:

```text
Ran 54 tests
OK
```

최종 전체 회귀:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5277 tests in 430.496s
OK
```

## 추가 bounded smoke: allocation guard 반영 확인

semantic guard 적용 후 같은 작은 bounded smoke를 다시 실행했다.

명령 요약:

```text
output_root:
output/census_v4/2026-07-06-goal4-pdf-cap-allocation-guard-bounded-smoke

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
runtime_budget_exhausted: false
latest_phase: completed
```

artifact count:

```text
planner_runs.jsonl: 50
source_tasks.jsonl: 127
source_task_executions.jsonl: 127
web_search_tasks.jsonl: 3
web_search_results.jsonl: 4
web_fetched_documents.jsonl: 2
web_rejected_documents.jsonl: 4
claim_extractor_runs.jsonl: 2
accepted_claims.jsonl: 96
brain_to_claim_trace.jsonl: 15
stagecourt_traces.jsonl: 96
```

readiness audit:

```text
brain_web_readiness_gate_audit.verdict: BLOCKED

blockers:
  web/LLM accepted claim count is zero
  Brain/Web operational minimum planner calls not met: 5/30
  Brain/Web operational minimum web search tasks not met: 3/20
  Brain/Web operational minimum web/news search calls not met: 3/20
  Brain/Web operational minimum fetched documents not met: 2/10
  Brain/Web operational minimum claim extractor attempts not met: 2/10
  Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

trace promotion audit:

```text
brain_stage_promotion_audit.verdict: PROMOTION_APPLIED
blockers: []
unsafe_promoted_stage_row_count: 0
brain_stage_trace_not_promoted_marker_missing_count: 0
brain_trace_promoted_reference_error_count: 0
```

해석:

```text
PDF fetch/extraction 자체는 동작한다.
LLM extractor도 실제 full-source 문서 2건에서 실행됐다.
하지만 새 guard 기준에서는 web/LLM accepted claim이 0으로 돌아갔다.
```

이건 후퇴가 아니라 정확도 보정이다.

쉬운 예:

```text
이전 채점:
  "커피 매출 비중 증가"를 "A고객 선주문" 칸에 넣어 1점을 얻음

이번 채점:
  그 칸에는 못 넣게 막음
  진짜 선주문 문서가 나오면 그때 점수로 인정
```

따라서 현재 상태는 다음처럼 봐야 한다.

```text
PDF body cap 문제:
  일부 해결. PDF가 잘려서 extractor까지 못 가는 문제는 줄었다.

C06 customer allocation accepted claim:
  이전 1건은 weak semantic match로 보고 폐기하는 것이 맞다.

Goal4:
  여전히 미완료.
  최소 운영 수량과 전체 아키타입 matrix 증명이 남아 있다.
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

추가로 `external web route가 실제 fetch/extractor까지 내려가지 못하는 문제`, `PDF body가 잘려 PDF 추출이 깨지는 문제`, `HBM 비중 확대 문장을 고객 배정 claim으로 과잉 인정하는 문제`도 각각 좁혔다.

# Goal4 Next Runtime Attempt V3 Final Audit

작성일: 2026-07-07

대상 goal 문서: `docs/core/goal4.md`

출력 루트:

```text
output/census_v4/2026-07-07-goal4-all-archetype-next-runtime-attempt-seed-feedback-v3
```

## 결론

이번 v3 실행은 이전 `INVALID_PARTIAL_OUTPUT` 상태에서 한 단계 전진했다.

```text
이전 문제:
claim_id collision으로 runtime attempt가 중간에 죽음

이번 상태:
runtime attempt는 끝까지 완료됐고 Brain/Web evidence pass는 충족

최종 verdict:
MEANINGFUL_RUNTIME_PARITY_NOT_READY
```

쉬운 예:

```text
전에는 시험 도중 답안지 번호 충돌로 시험장이 멈췄다.
이번에는 시험은 끝까지 봤고 채점표도 일부 나왔다.
하지만 제출된 답안지 6장 모두 필수 첨부서류가 빠져 있어 합격은 아니다.
```

따라서 이번 결과는 Goal4 완료가 아니다. 정확한 상태는 다음이다.

```text
Brain/Web evidence collection path: pass
Production FULL_E2R score path: 일부 pass
Meaningful full thesis evidence: fail
All archetype runtime parity: fail
Goal4 completion: fail
```

## 이번에 실제로 개선된 것

### 1. claim_id collision으로 run이 죽는 문제를 막았다

수정 파일:

```text
src/e2r/agentic/evidence_os.py
tests/test_agentic_evidence_os.py
```

패치 요지:

```text
같은 claim_id가 다시 들어왔는데 내용이 다르면
기존 claim을 덮어쓰거나 run을 죽이지 않는다.

대신 append-only ledger에
UPDATES / claim_id_collision_existing_claim_retained
event를 남기고 기존 claim을 유지한다.
```

쉬운 예:

```text
한 번 접수된 서류 번호 123번이 있는데,
다른 내용의 123번 서류가 또 들어왔다.

예전:
채점기 전체 중단

현재:
기존 서류는 유지하고,
"번호 충돌이 있었다"는 감사 메모를 남긴 뒤 다음 서류 채점을 계속함
```

이 패치는 점수를 좋게 만들기 위한 것이 아니다. 전수 runtime attempt가 한 claim 충돌 때문에 전체 중단되지 않게 만들기 위한 ledger 안정화 패치다.

### 2. 최신 runtime 결과와 리포트 문구 불일치를 고쳤다

수정 파일:

```text
src/e2r/census/research_to_runtime_parity.py
docs/operational/research_to_runtime_acceptance_report.md
docs/operational/research_to_runtime_root_cause_2026-07-05.md
```

이전 생성 문구에는 `7개` 아키타입이라는 하드코딩성 설명이 남아 있었다.

v3 최신 결과는 다음이 맞다.

```text
promoted full-thesis rows = 6
distinct promoted archetypes = 6
promoted archetypes =
  C01
  C03
  C05
  C06
  C08
  C17
```

따라서 생성기를 동적으로 바꿨다.

```text
예전:
"현재는 7개 과목..."

현재:
runtime audit의 distinct_full_thesis_archetype_count를 읽어 문구 생성
```

쉬운 예:

```text
점수표에는 실제로 6과목만 올라왔는데
설명서가 7과목이라고 말하면 다음 에이전트가 잘못된 결론을 낸다.
그래서 설명서는 숫자를 직접 쓰지 않고 감사 JSON에서 읽게 만들었다.
```

## v3 실행 주요 숫자

### Runtime 진행

```text
seed_event_count = 105
planner_runs = 452
full_thesis_seed_planner_run_count = 105
real_provider_success_seed_count = 104
runtime_budget_exhausted = false
source_task_execution_count = 787
web_search_task_count = 128
web_fetched_document_count = 112
```

파일 row 기준:

```text
full_thesis_seed_materialization_trace.jsonl = 105
stagecourt_traces.jsonl = 113
score_contributions.jsonl = 157
accepted_claims.jsonl = 144
source_task_executions.jsonl = 879
planner_runs.jsonl = 452
```

주의:

```text
audit JSON의 source_task_execution_count = 787
raw exported source_task_executions.jsonl row = 879
```

이 차이는 감사 범위와 export row 범위가 다르기 때문이다. operator 판단에는 각 audit의 정의를 기준으로 읽어야 한다.

### Brain/Web readiness

파일:

```text
brain_web_readiness_gate_audit.json
```

결과:

```text
verdict = READY_FOR_BRAIN_WEB_EVIDENCE_PASS
blockers = []
brain_web_evidence_pass_allowed = true
```

주요 통과 근거:

```text
llm_planner_success_count = 104
llm_claim_extractor_attempt_count = 134
llm_claim_extractor_provider_error_count = 0
web_or_llm_accepted_claim_count = 43
official_accepted_claim_count = 9
snippet_to_score_count = 0
fake_provider_used_count = 0
promoted_snapshot_document_count = 0
```

해석:

```text
이번 v3는 "LLM planner/source/claim extractor가 실운영 경로로 움직였는가?"라는 질문에는 YES다.
하지만 "그 증거로 모든 아키타입 full thesis가 닫혔는가?"라는 질문에는 NO다.
```

## Full-thesis seed materialization 상태

파일:

```text
full_thesis_seed_materialization_audit.json
```

결과:

```text
verdict = FAIL
operator_materialization_status = PENDING_FULL_THESIS_MATERIALIZATION
trace_row_count = 105
critical_count = 48
full_thesis_promoted_seed_count = 6
```

status count:

```text
ACCEPTED_CLAIM_NOT_CREATED = 83
FULL_THESIS_PROMOTED = 6
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 1
STAGECOURT_READY_NOT_PROMOTED = 15
```

primary failure axis:

```text
PRIMITIVE_GAP_UNSATISFIED = 67
NO_FETCHED_DOCUMENT = 7
NO_SCORE_ELIGIBLE_REAL_CLAIM = 7
PROVIDER_ERROR_RECORDED = 2
```

쉬운 예:

```text
105개 과목별 보충문제를 냈다.
6개는 답안지 형태까지 갔다.
15개는 채점대까지 갔지만 최종 답안지로 승격되지 않았다.
83개는 점수에 쓸 수 있는 claim이 아직 만들어지지 않았다.
1개는 planner provider 단계에서 성공하지 못했다.
```

## Production full-thesis 상태

파일:

```text
full_thesis_production_audit.json
research_to_runtime_parity_matrix_2026-07-05.json
```

결과:

```text
status = PENDING_FULL_THESIS_PRODUCTION
verdict = PENDING_FULL_THESIS_PRODUCTION
production_full_thesis_row_count = 6
production_pass_allowed = false
```

promoted row:

| symbol | archetype | target gap | final stage | 의미 |
|---|---|---|---|---|
| 052400 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | contract_quality | 0 | score path only |
| 047810 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | export_contract | 0 | score path only |
| 003380 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | contract_duration_months | 0 | score path only |
| 005930 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | revenue_visibility_contract | 0 | score path only |
| 058470 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | named_customer_quality | 1 | score path only |
| 011170 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | utilization_rate | 2 | score path only |

중요:

```text
위 6개는 final_score_scale = FULL_E2R_100
위 6개는 final_operator_score_use = FULL_E2R_SCORE
위 6개는 final_operator_stage_use = FULL_THESIS_STAGE

하지만 위 6개 모두 required_positive_missing 또는 Green gap이 남아 있다.
따라서 meaningful full thesis가 아니다.
```

운영 audit 집계:

```text
production_full_thesis_row_with_required_positive_missing_primitives_count = 6
production_full_thesis_row_with_green_gap_primitives_count = 6
production_symbols_without_required_positive_missing_primitives = []
production_symbols_without_green_gap_primitives = []
```

쉬운 예:

```text
점수 계산기를 통과한 답안지 6장이 있다.
그런데 6장 모두 필수 증빙 첨부란이 비어 있다.
그래서 "채점기는 돌았다"라고 말할 수는 있지만
"운영 thesis가 완성됐다"라고 말하면 안 된다.
```

## All-archetype parity 상태

파일:

```text
all_archetype_runtime_status_matrix_2026-07-05.json
all_archetype_runtime_parity_summary.md
```

전체 registry:

```text
registry_contract_count = 36
canonical C archetype = 32
R13 cross-archetype = 4
exact registry row coverage = true
all contracts have memory card = true
all contracts have source route patterns = true
```

runtime proof status:

```text
NOT_PROVEN_SCORE_PATH_ONLY = 6
NOT_PROVEN_BLOCKED_BY_MATERIAL_GAP = 2
NOT_PROVEN_PLANNER_ONLY = 1
NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM = 24
NOT_PROVEN_TARGET_MATERIALIZATION_REQUIRED = 3
```

아키타입별 핵심 상태:

```text
C01, C03, C05, C06, C08, C17
  -> score path only
  -> full thesis 완료 아님

C10, C31
  -> accepted claim은 있으나 material/Green gap 때문에 full row 승격 안 됨

C24
  -> planner only
  -> source task materialization이 아직 안 됨

C15, C28 포함 다수
  -> source task는 실행됐지만 accepted claim/full thesis로 이어지지 않음

R13 3개
  -> target materialization required

R13 high MAE guardrail
  -> source executed but no accepted claim
```

쉬운 예:

```text
36개 과목 전체 명단과 교재는 준비됐다.
하지만 실제 채점 가능한 답안지는 6과목뿐이고,
그 6과목도 필수 첨부서류가 빠져 있다.
나머지는 자료를 못 찾았거나, 자료는 봤지만 점수 claim으로 못 바꿨거나, 대상 종목부터 더 찾아야 하는 상태다.
```

## Goal completion blocker

파일:

```text
goal_completion_audit.json
goal_requirement_matrix_audit.json
```

Goal4 완료 blocker:

```text
full_thesis_smoke_pending
full_thesis_smoke_execution_pending
full_thesis_production_pass_false
full_thesis_seed_materialization_audit_not_pass
machine_readable_test_result_artifact_missing
goal_requirement_matrix_pass_false
```

Goal requirement matrix:

```text
goal_completion_minimum_pass = false
required_goal_completion_count = 22
required_goal_completion_pass_count = 18
required_goal_completion_pending_count = 3
required_goal_completion_fail_count = 1
```

fail gate:

```text
FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS
```

pending gates:

```text
FULL_THESIS_SMOKE_PASS
FULL_THESIS_PRODUCTION_PASS
FULL_TEST_ARTIFACT_PASS
```

## 삼성전자/하이닉스 해석

삼성전자 `005930`은 이번 v3에서 production score-path row로 올라왔다.

```text
symbol = 005930
archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
target gap = revenue_visibility_contract
final_score_scale = FULL_E2R_100
final_stage = 0
meaningful pass = false
```

즉 삼성전자는 이제 controlled smoke와만 존재하는 상태는 아니다. production score path row가 있다.

하지만 이 row도 다음 이유로 운영 합격이 아니다.

```text
required_positive_missing_primitives 남음
green_gap_primitives 남음
score path only
```

SK하이닉스는 이번 production full-thesis row 6개에는 없다. controlled smoke와 production row는 계속 분리해서 봐야 한다.

쉬운 예:

```text
삼성전자:
실제 시험장에 답안지를 냈지만 필수 첨부서류가 빠진 상태

하이닉스:
이번 실제 시험장 답안지 명단에는 없음
모의고사/controlled smoke 결과를 실제 합격으로 섞으면 안 됨
```

## 왜 아직 "완료"라고 하면 안 되는가

이번 실행은 다음을 증명했다.

```text
1. real planner가 105개 seed 대부분에서 돈다.
2. bounded source acquisition이 실제로 돈다.
3. LLM claim extractor도 돈다.
4. snippet-only/fake-provider/snapshot leakage 없이 Brain/Web evidence gate를 통과할 수 있다.
5. 일부 아키타입은 FULL_E2R_100 score path까지 닫힌다.
```

하지만 Goal4가 요구하는 것은 이것보다 더 강하다.

```text
C01~C32와 R13 전체에서
attempt -> source route -> fetched document -> accepted claim -> primitive -> score contribution -> StageCourt -> meaningful full thesis
까지 모두 증명해야 한다.
```

현재는:

```text
36개 중 6개만 score path only
6개 모두 required-positive/Green gap 존재
24개는 source executed no accepted claim
1개는 planner only
3개는 target materialization required
```

따라서 최종 상태는 계속:

```text
MEANINGFUL_RUNTIME_PARITY_NOT_READY
```

## 다음 작업 우선순위

1. `PRIMITIVE_GAP_UNSATISFIED` 67개를 먼저 줄인다.
   - 단순 검색량 확대가 아니라 primitive-specific accepted claim으로 닫아야 한다.
   - 예: C06이면 HBM 뉴스를 더 긁는 것이 아니라 `revenue_visibility_contract`를 score-eligible claim으로 연결해야 한다.

2. `NO_FETCHED_DOCUMENT` 7개와 `NO_SCORE_ELIGIBLE_REAL_CLAIM` 7개를 분리 처리한다.
   - 문서를 못 가져온 문제와 문서는 가져왔지만 점수 claim이 안 된 문제는 원인이 다르다.

3. C24 planner-only 상태를 source task 생성/실행까지 밀어야 한다.
   - 지금 C24는 아직 full-thesis source route 검증이라고 부르기 어렵다.

4. C15/C28 mandatory archetype은 promoted row가 없다.
   - 기존 연구에서 중요하게 본 C15/C28이 runtime full-thesis row로 올라오는지 별도 확인해야 한다.

5. machine-readable test artifact를 생성해야 한다.
   - 현재 `test_result_evidence_audit.json`은 `STRING_SUMMARY_ONLY`다.
   - 테스트를 돌렸다는 문자열 요약은 Goal 완료 증거가 아니다.

6. score path only와 meaningful thesis pass를 계속 분리한다.
   - `PRODUCTION_FULL_E2R_SCORE_PATH_PASS`는 진행 증거다.
   - `MEANINGFUL_FULL_THESIS_EVIDENCE_PASS`가 실제 운영 합격 기준이다.

## 이번 문서와 함께 읽어야 할 파일

최신 generated summary:

```text
docs/operational/research_to_runtime_acceptance_report.md
docs/operational/research_to_runtime_root_cause_2026-07-05.md
docs/operational/all_archetype_runtime_parity_summary.md
docs/operational/research_to_runtime_parity_matrix_2026-07-05.json
docs/operational/all_archetype_runtime_status_matrix_2026-07-05.json
```

최신 v3 output audit:

```text
output/census_v4/2026-07-07-goal4-all-archetype-next-runtime-attempt-seed-feedback-v3/readiness_verdict.json
output/census_v4/2026-07-07-goal4-all-archetype-next-runtime-attempt-seed-feedback-v3/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-07-goal4-all-archetype-next-runtime-attempt-seed-feedback-v3/full_thesis_seed_materialization_audit.json
output/census_v4/2026-07-07-goal4-all-archetype-next-runtime-attempt-seed-feedback-v3/full_thesis_production_audit.json
output/census_v4/2026-07-07-goal4-all-archetype-next-runtime-attempt-seed-feedback-v3/goal_completion_audit.json
output/census_v4/2026-07-07-goal4-all-archetype-next-runtime-attempt-seed-feedback-v3/goal_requirement_matrix_audit.json
```

한 줄 결론:

```text
이번 v3는 "실제 Brain/Web 경로가 돈다"는 증거는 만들었지만,
"전 아키타입에서 의미 있는 FULL_THESIS 운영 stage가 닫힌다"는 증거는 아직 만들지 못했다.
```

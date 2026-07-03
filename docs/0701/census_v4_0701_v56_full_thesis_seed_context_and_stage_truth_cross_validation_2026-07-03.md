# Census v4 2026-07-01 v56 Full-Thesis Seed Context / Stage Truth Cross-Validation

작성일: 2026-07-03 KST

## 결론

질문은 이거였다.

```text
뭔가 잘못되고 있는 거 맞지?
Stage가 있는 애들이 있긴 해?
```

정확한 답은 다음이다.

```text
Stage row는 있다.
하지만 운영용 FULL_THESIS Stage는 아직 없다.
```

현재 canonical output 기준:

```text
output/census_v4/2026-07-01

CENSUS_EVENT_BOARD 상태판 Stage row = 3391
non-Stage0 상태판 Stage row = 85
운영 FULL_THESIS Stage row = 0
FULL_E2R_100 verified score row = 0
production full-thesis row = 0
```

쉬운 예:

```text
병원 접수표에 "검사 필요"라고 찍힌 환자가 85명 있다.
하지만 정밀검사 결과지까지 나온 환자는 아직 0명이다.

CENSUS_EVENT_BOARD Stage = 접수표/상태판
FULL_THESIS Stage = 정밀검사 결과지
```

따라서 “Stage가 완전히 0개”라고 말하면 틀리고, “운영 Stage가 있다”고 말해도 틀린다.

## 이번 v56 패치의 목적

v55에서 full-thesis refresh seed 85개가 Research Brain 선택 예산 앞쪽으로 오도록 고쳤다.

하지만 seed payload가 너무 빈약하면 실제 provider가 켜졌을 때도 planner가 무슨 맥락에서 조사해야 하는지 모른다.

그래서 v56은 seed에 다음 정보를 추가했다.

```text
source_primary_archetype
source_secondary_archetypes
source_large_sector_id
source_score_contribution_ids
source_missing_primitives
source_material_gap_ids
source_failed_stage_gates
```

중요한 점:

```text
target_archetype = None
target_archetype_status = BRAIN_HYPOTHESIS_REQUIRED
score_evidence_allowed = False
stage_promotion_allowed_before_execution = False
```

즉 이 패치는 “이 종목은 C05다/C06이다”라고 확정하지 않는다.

이전 상태판에서 어떤 힌트가 있었는지만 planner에게 넘긴다.

## 왜 이 패치가 필요한가

v55까지는 full-thesis seed가 실제 Research Brain 입구로 먼저 들어가긴 했다.

그런데 seed의 의미는 거의 이 정도였다.

```text
이 종목은 full thesis refresh가 필요하다.
아키타입은 Brain이 다시 가설을 세워라.
source-backed primitive coverage가 필요하다.
```

이 정보만으로는 planner가 너무 막막하다.

예를 들어 000660 SK하이닉스 seed는 canonical 상태판에서 이미 다음 힌트를 갖고 있었다.

```text
source_primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
source_large_sector_id = 메모리/HBM
source_missing_primitives = repeat_evidence_family, cash_or_revision_conversion
source_material_gap_ids = repeat_evidence_family, cash_or_revision_conversion, multi_source_confirmation
source_failed_stage_gates = missing_green_bridge
```

이 힌트는 점수 재료가 아니다.

하지만 planner에게는 매우 중요하다.

쉬운 예:

```text
나쁜 방식:
  "하이닉스니까 C06 HBM으로 확정하고 HBM 계약 검색어를 코드가 만든다."

이번 방식:
  "이전 상태판에는 메모리/HBM 맥락과 cash/revision bridge gap이 있었다.
   그래도 target archetype은 아직 미정이다.
   LLM planner가 원문 조사 계획을 다시 세워라."
```

## 코드 변경

### 1. full-thesis refresh queue에 source context 추가

파일:

```text
src/e2r/census/census_runner_v4.py
```

함수:

```text
_full_thesis_refresh_queue()
```

추가된 queue row 필드:

```text
source_primary_archetype
source_secondary_archetypes
source_large_sector_id
source_score_contribution_ids
source_missing_primitives
source_material_gap_ids
source_failed_stage_gates
```

### 2. Research Brain seed event structured_payload에 context 추가

파일:

```text
src/e2r/census/census_runner_v4.py
```

함수:

```text
_write_full_thesis_refresh_seed_events()
```

추가된 payload 필드:

```text
structured_payload.source_primary_archetype
structured_payload.source_secondary_archetypes
structured_payload.source_large_sector_id
structured_payload.source_score_contribution_ids
structured_payload.source_missing_primitives
structured_payload.source_material_gap_ids
structured_payload.source_failed_stage_gates
structured_payload.target_archetype_status
structured_payload.target_archetype
```

### 3. Research Brain planner evidence context에 seed context 노출

파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
```

추가:

```text
_full_thesis_queue_context_from_structured_payload()
```

planner context에는 다음 형태로 들어간다.

```text
existing_evidence_by_event_id[event_id].full_thesis_queue_context
```

단, provider가 `none`이면 실제 prompt가 생성되지 않으므로 `planner_runs.jsonl`에는 `prompt_hash=null`, `raw_prompt_path=null`이 맞다.

### 4. materialization trace에도 source context 복사

파일:

```text
src/e2r/census/census_runner_v4.py
```

함수:

```text
_write_full_thesis_seed_materialization_trace()
```

이유:

```text
research_brain_full_thesis_seed_events.jsonl만 보면 context가 보이지만,
full_thesis_seed_materialization_trace.jsonl만 보면 왜 이 seed가 생겼는지 바로 안 보였다.
```

이제 trace row에도 다음 필드가 보인다.

```text
source_primary_archetype
source_secondary_archetypes
source_large_sector_id
source_missing_primitives
source_material_gap_ids
source_failed_stage_gates
source_score_contribution_ids
target_archetype_status
target_archetype
```

## 중요한 안전장치

이번 패치는 점수나 Stage를 올리지 않는다.

```text
score_evidence_allowed = False
stage_promotion_allowed_before_execution = False
target_archetype = None
```

이 세 가지가 핵심이다.

쉬운 예:

```text
source_primary_archetype=C05
```

이 값은 “과거 상태판에서 C05처럼 보였다”는 메모다.

아래와 같으면 위험하다.

```text
target_archetype=C05
```

이러면 planner가 새로 판단하기 전에 아키타입을 확정한 꼴이다.

v56은 이 위험을 피한다.

## v56 diagnostic run

명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-seed-context-v56 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_TRIAGE_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider none \
  --brain-source-acquisition live_official_first \
  --brain-universe-limit 2 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-stage-promotion-mode strict \
  --target-gate anti_fake \
  --write-operational-docs false \
  --fail-on-critical-audit false \
  --test-result-artifact output/census_v4/2026-07-01/full_unittest_result_artifact.json
```

결과:

```text
exit code = 1
stdout = NOT_READY
```

이건 정상이다.

provider를 `none`으로 둔 실행이므로 production ready가 되면 안 된다.

## v56 diagnostic 핵심 수치

산출물:

```text
output/census_v4/2026-07-01-seed-context-v56
```

```text
brain_web_attempt_audit.json:
  verdict = ATTEMPTED_NOT_CUTOVER_READY
  source_task_execution_count = 0
  full_thesis_seed_event_count = 85
  full_thesis_seed_planner_attempted_event_count = 21
  full_thesis_seed_planner_run_row_count = 21

brain_web_readiness_gate_audit.json:
  verdict = BLOCKED
  llm_planner_call_count = 21
  llm_real_provider_success_count = 0
  source_task_execution_count = 0
  brain_accepted_claim_count = 0
  web_or_llm_accepted_claim_count = 0
  brain_promoted_stage_row_count = 0
  full_thesis_seed_event_count = 85
  full_thesis_seed_planner_attempted_event_count = 21
  full_thesis_seed_planner_run_row_count = 21

full_thesis_seed_materialization_audit.json:
  verdict = PASS
  critical_count = 0
  status_counts:
    PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 21
    PLANNER_NOT_RUN = 64
```

해석:

```text
85개 seed는 만들어졌다.
그중 21개가 planner attempt row까지 갔다.
하지만 provider none이라 real provider success는 0이다.
source task, accepted claim, stage promotion은 0이 맞다.
```

쉬운 예:

```text
정밀검사 예약표 85개를 만들었다.
21개는 접수창구까지 갔다.
하지만 의사가 없는 모드로 돌렸기 때문에 실제 검사 결과지는 0개다.
```

## 첫 seed row 확인

파일:

```text
output/census_v4/2026-07-01-seed-context-v56/research_brain_full_thesis_seed_events.jsonl
```

첫 row:

```text
symbol = 000660
candidate_event_id = CEV4-FTQUEUE-000660-9563b2a7a852fc0c
source_family = CensusFullThesisQueue
seed_role = planner_input_only
score_evidence_allowed = False
stage_promotion_allowed_before_execution = False

structured_payload.queue_task_id = FTQUEUE-2026-07-01-000660-0031
structured_payload.source_primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
structured_payload.source_large_sector_id = 메모리/HBM
structured_payload.source_missing_primitives = [repeat_evidence_family, cash_or_revision_conversion]
structured_payload.source_material_gap_ids = [repeat_evidence_family, cash_or_revision_conversion, multi_source_confirmation]
structured_payload.source_failed_stage_gates = [missing_green_bridge]
structured_payload.source_score_contribution_ids = [SCON-8da68431606c7699ece3]
structured_payload.target_archetype_status = BRAIN_HYPOTHESIS_REQUIRED
structured_payload.target_archetype = None
structured_payload.official_first_required = True
```

이 row는 점수 재료가 아니다.

이 row는 planner에게 “이전 상태판의 힌트와 빠진 칸”을 전달하는 작업표다.

## 첫 materialization trace row 확인

파일:

```text
output/census_v4/2026-07-01-seed-context-v56/full_thesis_seed_materialization_trace.jsonl
```

첫 row:

```text
symbol = 000660
candidate_event_id = CEV4-FTQUEUE-000660-9563b2a7a852fc0c
queue_task_id = FTQUEUE-2026-07-01-000660-0031

source_primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
source_large_sector_id = 메모리/HBM
source_missing_primitives = [repeat_evidence_family, cash_or_revision_conversion]
source_material_gap_ids = [repeat_evidence_family, cash_or_revision_conversion, multi_source_confirmation]
source_failed_stage_gates = [missing_green_bridge]
source_score_contribution_ids = [SCON-8da68431606c7699ece3]

target_archetype_status = BRAIN_HYPOTHESIS_REQUIRED
target_archetype = None

materialization_status = PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS
planner_run_count = 1
planner_real_provider_success_count = 0
source_task_execution_count = 0
accepted_claim_count = 0

final_stage_scope = CENSUS_EVENT_BOARD
final_operator_stage_use = NOT_FULL_THESIS_STAGE
final_full_thesis_stage = FULL_THESIS_NOT_RUN
```

이 trace가 보여주는 것:

```text
seed는 Research Brain 쪽으로 들어갔다.
하지만 real provider가 없어서 source task와 claim은 없다.
최종 Stage는 여전히 상태판 Stage일 뿐이다.
```

## trace 전체 분포

파일:

```text
output/census_v4/2026-07-01-seed-context-v56/full_thesis_seed_materialization_trace.jsonl
```

```text
trace_rows = 85

materialization_status:
  PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 21
  PLANNER_NOT_RUN = 64

target_archetype_status:
  BRAIN_HYPOTHESIS_REQUIRED = 85

target_archetype:
  None = 85

source_primary_archetype non-null = 74
source_large_sector_id non-null = 13
source_missing_primitives non-empty = 82
```

이 분포는 의도와 맞다.

```text
이전 상태판 힌트는 최대한 전달한다.
하지만 target archetype 확정은 0개다.
```

## canonical stage truth 재확인

파일:

```text
output/census_v4/2026-07-01/census_stage_summary.json
output/census_v4/2026-07-01/census_stage_status.jsonl
```

기존 v54와 같은 결론이다.

```text
stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN = 3391

production_full_thesis_row_count = 0
full_e2r_verified_score_row_count = 0
goal_completion_ready = false
```

## 산출물 해시

canonical:

```text
output/census_v4/2026-07-01/census_stage_summary.json
sha256 = 9ff67f6dc7f006be793045a2ab93b779901873a9b19b091f819a9f1e809f20d0

output/census_v4/2026-07-01/census_stage_status.jsonl
sha256 = e821f3e948a8b1372c3fdd33d182d91e921f5d1ee13571c4255dc2635287ab97
```

v56 diagnostic:

```text
output/census_v4/2026-07-01-seed-context-v56/brain_web_attempt_audit.json
sha256 = 37821b5ab79ff8d81c86755f1ccabe5b0770e608d7bf9d3414e6aa057e053308

output/census_v4/2026-07-01-seed-context-v56/brain_web_readiness_gate_audit.json
sha256 = decff31a47a4b6f8a420ddb772b875c9f05c1c924febea4c9319da41c02b9136

output/census_v4/2026-07-01-seed-context-v56/research_brain_full_thesis_seed_events.jsonl
sha256 = adcf19724834de5e1fba4fe4cca041bd6e6d5c09470234ced69d89ed9b41c353

output/census_v4/2026-07-01-seed-context-v56/full_thesis_seed_materialization_trace.jsonl
sha256 = 7dee4bd29f7ac9971900f0d1a42723d38cbe853878b4bc3ac39f4892f28e8ee9

output/census_v4/2026-07-01-seed-context-v56/planner_runs.jsonl
sha256 = dd5f0dffe49e121d2fcb5c3af680bf903e0ac92e17994581a6c73e0a122908ff
```

## 테스트 검증

targeted:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_full_thesis_smoke_tasks -v
```

결과:

```text
Ran 11 tests in 21.741s
OK
```

targeted:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
```

결과:

```text
Ran 50 tests in 3.336s
OK
```

compile:

```bash
PYTHONPATH=src python -m py_compile \
  src/e2r/census/census_runner_v4.py \
  src/e2r/research_brain/v4_production_orchestrator.py
```

결과:

```text
OK
```

full suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5079 tests in 203.141s
OK
```

특히 다음 회귀 테스트들이 통과했다.

```text
test_wrong_subject_normal_audit_opinion_is_not_assigned_to_target
test_worldex_audit_opinion_with_samsung_customer_mention_does_not_create_samsung_4c
test_old_positive_document_without_current_confirmation_is_historical_not_scored
test_wrong_subject_document_is_rejected_not_scored
test_source_proxy_and_price_path_never_enter_score_or_extraction_prompt
test_source_task_without_unbounded_general_search_guard_is_rejected
```

이 테스트들은 월덱스/삼성 감사의견 오귀속, 오래된 risk 재사용, source_proxy 점수 누수 같은 문제를 다시 막는 역할을 한다.

## 교차검증 공격 포인트와 현재 답

### 공격 1. source_primary_archetype이 target_archetype으로 새는 것 아닌가?

현재 답:

```text
target_archetype = None
target_archetype_status = BRAIN_HYPOTHESIS_REQUIRED
```

trace 85개 모두 동일하다.

따라서 source context는 힌트이고, 목표 아키타입 확정이 아니다.

### 공격 2. seed row가 score evidence로 쓰이는 것 아닌가?

현재 답:

```text
score_evidence_allowed = False
stage_promotion_allowed_before_execution = False
```

seed row는 score contribution을 만들 수 없다.

### 공격 3. provider none인데 왜 planner row가 21개 있는가?

현재 답:

```text
planner row는 "attempted but provider not configured" 기록이다.
prompt_hash = null
raw_prompt_path = null
real_provider_success = false
provider_error = planner_provider_not_configured
```

이건 success가 아니라 pending trace다.

### 공격 4. v56이 운영 Stage를 만든 것 아닌가?

현재 답:

```text
production FULL_THESIS row = 0
brain_promoted_stage_row_count = 0
accepted_claim_count = 0
source_task_execution_count = 0
```

운영 Stage는 아직 없다.

### 공격 5. 상태판 Stage가 있는데 왜 Stage가 없다고 했나?

정정 답:

```text
상태판 Stage는 있다.
운영 Full Thesis Stage는 없다.
```

앞으로는 “Stage 있음/없음”이라고 말하지 말고 반드시 scope를 붙인다.

```text
CENSUS_EVENT_BOARD Stage
FULL_THESIS Stage
SMOKE_ONLY Stage
```

## 남은 블로커

v56 이후에도 목표 완료는 아니다.

```text
FULL_THESIS_PRODUCTION_PASS = false
BRAIN_WEB_EVIDENCE_PASS = false
MEANINGFUL_OPERATIONAL_STAGE_PASS = false
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS = false
```

구체적 블로커:

```text
1. real planner provider success가 없는 seed는 source task로 못 간다.
2. source_task_execution_count = 0이면 accepted claim도 없다.
3. accepted claim이 없으면 ScoreContribution과 StageCourt가 없다.
4. StageCourt가 없으면 FULL_THESIS Stage promotion은 금지된다.
5. source-backed replay는 6/32만 준비됐고 26/32는 source gap pending이다.
```

## 다음 패치 방향

다음 패치는 seed context 문서화에서 끝나면 안 된다.

실제 목표는 이 순서다.

```text
1. real provider가 켜진 run에서 full-thesis seed context가 실제 prompt에 들어가는지 raw_prompt_path로 증명한다.
2. planner가 target_archetype을 확정하지 않고 hypothesis 후보와 bounded official-first SourceTask를 내는지 확인한다.
3. source task가 DART/KIND/IR/CompanyGuide/ReportPDF 등 admissible source를 실제 fetch한다.
4. LLM extractor 또는 structured extractor가 source-backed accepted claim을 만든다.
5. accepted claim -> primitive mapping -> score contribution -> StageCourt trace가 닫힌다.
6. 그때만 FULL_THESIS row를 promotion한다.
```

가장 먼저 볼 후보:

```text
000660 SK하이닉스:
  source_large_sector_id = 메모리/HBM
  source_missing_primitives = repeat_evidence_family, cash_or_revision_conversion
  materialization_status = PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS

해야 할 일:
  provider success가 있는 run에서 이 seed가 raw prompt에 들어가는지 확인
  공식/IR/보고서 원문 task가 생기는지 확인
  accepted claim이 없으면 Stage 확정 금지
```

쉬운 예:

```text
지금은 "하이닉스 정밀검사 예약표"가 있다.
다음은 "의사가 실제로 검사 지시서를 냈는지"를 확인해야 한다.
그 다음은 "검사 결과지가 실제 원문 claim으로 닫혔는지"다.
```

## 최종 판정

v56은 운영 완성이 아니다.

v56의 정확한 성과는 다음이다.

```text
full-thesis seed가 Research Brain 입구로 먼저 들어간다.
seed는 이전 상태판 context를 planner에게 전달한다.
하지만 target_archetype은 강제하지 않는다.
seed/trace만으로는 score와 Stage를 만들 수 없다.
provider none 진단에서는 NOT_READY가 정상이다.
전체 테스트 5079개는 통과했다.
```

따라서 현재 답은 유지한다.

```text
Stage가 있는 애들은 있다.
하지만 그것은 CENSUS_EVENT_BOARD 상태판 Stage다.
실제 운영 FULL_THESIS Stage는 아직 0개다.
```

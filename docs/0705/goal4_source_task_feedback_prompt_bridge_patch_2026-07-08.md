# Goal4 Source Task Feedback Prompt Bridge Patch

작성일: 2026-07-08

## 결론

이번 패치는 Goal4 완료가 아니다.

이번 패치의 목적은 직전 `all_archetype_runtime_status_matrix`와 `all_archetype_next_runtime_attempt_plan`에 추가한 source-task 실패 진단이 실제 Research Brain v4 planner prompt까지 도달하게 만드는 것이다.

쉬운 예:

```text
기존:
C24가 DART/CompanyGuide/TrustedNews를 봤지만 score-eligible claim을 못 만들었다.
그런데 다음 LLM planner prompt에는 "이전 source task가 왜 실패했는지"가 약하게 전달됐다.

패치 후:
previous_source_task_primary_failure_axis = NO_SCORE_ELIGIBLE_REAL_CLAIM
previous_source_task_repair_hint = FETCH_SOURCE_WITH_CURRENT_DIRECT_ANCHORED_CLAIM
previous_source_task_top_source_classes = DART / IR / CompanyGuide ...
previous_source_task_top_primitive_gaps = trial_quality_visible / approval_not_confirmed ...

이 정보가 seed ingestion -> evidence context -> planner prompt rules까지 통과한다.
```

즉 산출물에만 적힌 감사 정보가 아니라, 다음 runtime attempt에서 LLM planner가 같은 generic source route를 반복하지 않도록 실제 입력으로 들어간다.

## 왜 필요했나

직전 패치로 아래 산출물에는 source-task 실패 축이 생겼다.

```text
docs/operational/all_archetype_runtime_status_matrix_2026-07-05.json
docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.json
docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl
docs/operational/all_archetype_next_runtime_source_tasks_2026-07-05.jsonl
```

하지만 실제 planner prompt 배관에는 아직 구멍이 있었다.

```text
_full_thesis_queue_context_from_structured_payload
→ previous_claim_failure / previous_seed_materialization만 통과
→ previous_source_task_*는 context allowlist에 없음

_planner_failure_feedback_context_from_structured_payload
→ previous_source_task_* allowlist 없음

build_v4_planner_prompt_payload rules
→ source-task 실패 축을 직접 언급하지 않음
```

그러면 다음 실행에서 C24 같은 행이 이렇게 될 수 있었다.

```text
matrix/plan:
"이전 DART/CompanyGuide route는 score-eligible claim을 못 만들었다"

planner prompt:
"이전 claim/seed 실패는 있음"

결과:
LLM이 같은 일반 공시/리포트 경로를 다시 고를 위험
```

이건 Goal4의 핵심인 "연구자료와 runtime source route를 실제로 연결"하는 데 부족하다.

## 코드 패치

수정 파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
src/e2r/research_brain/v4_planner_runtime.py
tests/test_research_brain_v4_operational_modes.py
```

### 1. full thesis queue context allowlist 확장

아래 필드를 planner context로 통과시킨다.

```text
previous_source_task_primary_failure_axis
previous_source_task_repair_hint
previous_source_task_top_failure_axes
previous_source_task_top_source_classes
previous_source_task_top_primitive_gaps
previous_source_task_failure_sample_refs
source_task_repair_required
source_task_repair_actions
```

### 2. planner_failure_feedback allowlist 확장

`planner_failure_feedback` 내부에서도 같은 source-task repair 정보를 통과시킨다.

단, 아래 필드는 계속 제거된다.

```text
score_evidence_allowed_from_previous_source_task_failures
```

이유:

```text
score/evidence eligibility 결론은 planner prompt에 넣으면 안 된다.
planner는 실패 원인과 다음 source route만 보고,
score/stage/eligibility 최종 판단은 deterministic Evidence OS와 StageCourt가 한다.
```

### 3. planner prompt rule 보강

이제 planner rule은 아래 축도 명시한다.

```text
previous_source_task_primary_failure_axis
previous_source_task_top_source_classes
previous_source_task_top_primitive_gaps
source_task_repair_actions
```

핵심 규칙:

```text
PRIMITIVE_GAP_UNSATISFIED:
  이전 source task가 source까지 갔지만 requested primitive를 못 닫았다.
  같은 source class를 일반 context로 반복하지 말고 primitive 자체를 겨냥하라.

NO_SCORE_ELIGIBLE_REAL_CLAIM:
  현재 직접 target-company source anchor가 없으면 score path를 닫을 수 없다.

PROVIDER_ERROR_RECORDED / PROVIDER_FAILED:
  낮은 점수나 부재로 확정하지 말고 source-pending 또는 다른 bounded source class를 선택하라.
```

## 검증

추가/수정 테스트:

```text
test_goal4_repair_feedback_seed_context_is_visible_to_planner_without_score_context
test_goal4_operational_seed_file_carries_source_task_failure_feedback_to_planner
```

두 번째 테스트는 실제 운영 seed 파일을 읽는다.

```text
docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl
```

그리고 C24 seed가 아래 경로를 통과하는지 검증한다.

```text
seed JSONL
→ _candidate_seed_events_from_config
→ _evidence_context_by_event
→ build_v4_planner_prompt_payload
→ planner rules
```

검증된 핵심 값:

```text
previous_source_task_primary_failure_axis = NO_SCORE_ELIGIBLE_REAL_CLAIM
previous_source_task_repair_hint = FETCH_SOURCE_WITH_CURRENT_DIRECT_ANCHORED_CLAIM
source_task_repair_required = true
KEEP_RESULT_PENDING_IF_ONLY_NON_ELIGIBLE_CLAIMS_EXIST 포함
score_evidence_allowed_from_previous_source_task_failures는 prompt에서 제거
```

## 중간 live attempt 감사

패치 후 실제 bounded live attempt도 시작했다.

실행 목적:

```text
docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl
→ patched planner context
→ real planner
→ live_full_bounded source acquisition
```

실행 경로:

```text
output/census_v4/2026-07-05-goal4-source-task-feedback-bridge-attempt
```

중간 결과:

```text
progress_status = RUNNING 상태에서 수동 중단
latest_phase = planner_batch_start
real planner success = 4
remaining_success_budget = 107
planner provider error = 0
```

planner가 실제 처리한 행:

```text
257720 / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION / 3회
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM / 1회
```

생성된 중간 산출물:

```text
source_tasks = 92
source_task_executions = 92
raw_assertions = 92
adjudicated_claims = 92
accepted_claims = 92
```

주의해야 할 점:

```text
accepted_claims=92만 보고 성공으로 보면 안 된다.
```

이유는 두 가지다.

```text
1. planner는 111개 목표 중 4개만 real provider로 처리한 상태였다.
2. source_task_executions에는 EVIDENCE_OS_BASELINE_ONLY도 포함되어 있었다.
```

즉 이 중간 실행은 아래만 증명한다.

```text
패치된 source-task feedback이 실제 live planner attempt 입력까지 들어간다.
real planner가 provider_error 없이 일부 seed를 처리한다.
```

아직 증명하지 못한 것:

```text
전 아키타입 RUNTIME_PARITY_PROVEN
source-task repair 후 required primitive closure
meaningful FULL_THESIS production pass
C05 외 archetype의 production parity
삼성전자/하이닉스 같은 controlled smoke와 production row의 일치
```

쉬운 예:

```text
택배 송장 92장이 생겼다고 배송 완료가 아니다.
아직 111개 주소 중 4개 주소만 실제 배차가 시작됐고,
일부 송장은 이전 baseline 확인표에 가까우므로
"전수 배송 완료"가 아니라 "배차 시스템에 새 안내문이 들어간 것 확인"으로 봐야 한다.
```

## 현재 Goal4 상태

아직 완료가 아니다.

현재 matrix 기준:

```text
meaningful_runtime_parity_ready = false
runtime_parity_not_proven_count = 36
RUNTIME_PARITY_PROVEN = 0
```

이번 패치는 다음 attempt가 실패 원인을 더 잘 소비하게 만든다.

하지만 아직 필요한 것은 다음이다.

```text
1. 이 bridge가 반영된 상태로 next runtime attempt 실행
2. source task가 accepted claim을 실제로 만드는지 확인
3. accepted claim이 required/Green primitive closure로 이어지는지 확인
4. C01~C32/R13 4개 전수 matrix에서 RUNTIME_PARITY_PROVEN 행 생성
5. score path only pass와 meaningful full thesis pass를 계속 분리
```

즉 이번 패치는 "진단이 실제 planner brain으로 들어가게 한 배관 수리"이고, Goal4의 최종 증명은 아직 남아 있다.

# Goal4 All-Archetype Source Route Diagnosis Patch

작성일: 2026-07-08

대상:

```text
docs/operational/all_archetype_runtime_status_matrix_2026-07-05.json
docs/operational/all_archetype_runtime_parity_matrix.json
docs/operational/all_archetype_runtime_parity_summary.md
```

## 결론

이번 패치는 Goal4 완료가 아니다.

이번 패치의 목적은 C01~C32와 R13 4개, 총 36개 runtime parity matrix가 source route 실패를 더 직접적으로 보여주게 만드는 것이다.

쉬운 예:

```text
기존:
C24 accepted claim 0개

패치 후:
C24는 DART/CompanyGuide/TrustedNews route까지 실행됐고,
trial_quality_visible / approval_not_confirmed 같은 primitive gap에서
NO_SCORE_ELIGIBLE_REAL_CLAIM, PRIMITIVE_GAP_UNSATISFIED가 주된 실패 축이다.
```

즉 "안 됐다"에서 멈추지 않고 "어느 source class, 어느 primitive gap, 어느 실패 축에서 막혔는지"를 다음 agent가 바로 볼 수 있게 했다.

## 추가한 matrix 필드

각 아키타입 row에 아래 필드를 추가했다.

```text
source_task_source_class_counts
source_task_top_source_classes
source_task_provider_name_counts
source_task_top_provider_names
source_task_primitive_gap_counts
source_task_top_primitive_gaps
source_task_primary_failure_axis
source_task_primary_repair_hint
source_task_failure_samples
source_task_accepted_samples
```

matrix 상단 summary에는 아래 집계를 추가했다.

```text
source_task_primary_failure_axis_counts
```

현재 재생성된 matrix의 핵심 집계:

```json
{
  "meaningful_runtime_parity_ready": false,
  "runtime_parity_proof_status_counts": {
    "NOT_PROVEN_BLOCKED_BY_MATERIAL_GAP": 5,
    "NOT_PROVEN_SCORE_PATH_ONLY": 6,
    "NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM": 22,
    "NOT_PROVEN_TARGET_MATERIALIZATION_REQUIRED": 3
  },
  "source_task_primary_failure_axis_counts": {
    "NO_SCORE_ELIGIBLE_REAL_CLAIM": 5,
    "PRIMITIVE_GAP_UNSATISFIED": 27,
    "PROVIDER_ERROR_RECORDED": 1
  }
}
```

## 왜 이게 Goal4에 필요한가

Goal4 요구는 단순히 "C05 외에도 row가 있다"가 아니다.

```text
아키타입별로:
attempt가 있었는지
source route가 실행됐는지
accepted claim이 생겼는지
score/full thesis까지 닫혔는지
왜 못 닫혔는지
```

를 전수 matrix로 증명해야 한다.

기존 matrix는 attempt/source/claim/full thesis 축은 있었지만, source task가 왜 accepted claim으로 닫히지 않았는지 operator가 바로 읽기에는 부족했다.

이번 패치는 이 빈칸을 줄인다.

## 현재 주요 blocker 해석

### C24

```text
runtime_attempt_status = SOURCE_TASK_EXECUTED
runtime_source_route_execution_status = SOURCE_TASK_EXECUTED_NO_ACCEPTED_CLAIMS
accepted_claim_status = REPLAY_ACCEPTED_CLAIM_ONLY
full_thesis_status = NO_PRODUCTION_FULL_THESIS_ROW
primary_blocker_class = ACCEPTED_CLAIM_NOT_CREATED
source_task_primary_failure_axis = NO_SCORE_ELIGIBLE_REAL_CLAIM
```

해석:

```text
연구 replay에는 C24 판례가 있다.
운영 source task도 실제 실행됐다.
하지만 현재 직접 anchor가 있는 score-eligible C24 claim을 만들지 못했다.
```

쉬운 예:

```text
임상 논문을 찾아야 하는데, 분기보고서/컨센서스/오래된 리포트만 잡히면
endpoint, safety, approval primitive는 닫히지 않는다.
```

### C15

```text
runtime_source_route_execution_status = SOURCE_TASK_EXECUTED_WITH_ACCEPTED_CLAIMS
accepted_claim_status = ACCEPTED_CLAIM_PRESENT_NOT_FULL_THESIS_CLOSED
full_thesis_status = FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP
```

해석:

```text
accepted claim은 생겼지만 spread_expansion, inventory_cycle, utilization_rate 같은 required/Green primitive가 닫히지 않아 full thesis row로 못 올라갔다.
```

### C28

```text
runtime_source_route_execution_status = SOURCE_TASK_EXECUTED_WITH_ACCEPTED_CLAIMS
accepted_claim_status = ACCEPTED_CLAIM_PRESENT_NOT_FULL_THESIS_CLOSED
full_thesis_status = FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP
```

해석:

```text
ARR 관련 accepted claim은 일부 생겼지만 nrr, retention_or_renewal, rpo_to_sales, recurring_margin_leverage가 닫히지 않아 full thesis가 막혔다.
```

## 수정 파일

```text
src/e2r/census/all_archetype_runtime_status_matrix.py
src/e2r/census/all_archetype_next_attempt_planner.py
tests/test_all_archetype_runtime_status_matrix.py
tests/test_all_archetype_runtime_parity_matrix.py
tests/test_all_archetype_next_attempt_plan.py
docs/operational/all_archetype_runtime_status_matrix_2026-07-05.json
docs/operational/all_archetype_runtime_status_matrix_2026-07-05.md
docs/operational/all_archetype_runtime_status_matrix.json
docs/operational/all_archetype_runtime_parity_matrix.json
docs/operational/all_archetype_runtime_parity_summary.md
docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.json
docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.md
docs/operational/all_archetype_next_runtime_attempt_plan.json
docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl
docs/operational/all_archetype_next_runtime_source_tasks_2026-07-05.jsonl
```

## 다음 attempt 입력 연결

matrix에만 진단을 적으면 다음 실행이 같은 실패를 반복할 수 있다.

그래서 `all_archetype_next_attempt_planner`에도 아래 필드를 연결했다.

```text
previous_source_task_primary_failure_axis
previous_source_task_repair_hint
previous_source_task_top_source_classes
previous_source_task_top_primitive_gaps
previous_source_task_failure_sample_refs
source_task_repair_required
source_task_repair_actions
```

이 필드는 plan row, source task, seed event structured payload, planner_failure_feedback에 모두 들어간다.

재생성된 next attempt plan 요약:

```json
{
  "plan_row_count": 36,
  "source_task_count": 111,
  "source_task_repair_task_count": 102,
  "source_task_primary_failure_axis_counts": {
    "NO_SCORE_ELIGIBLE_REAL_CLAIM": 18,
    "PRIMITIVE_GAP_UNSATISFIED": 81,
    "PROVIDER_ERROR_RECORDED": 3
  },
  "all_tasks_score_blocked_before_execution": true
}
```

쉬운 예:

```text
C24가 이전 run에서 DART/CompanyGuide로 trial primitive를 못 닫았다면,
다음 seed에는 "이전 source task가 NO_SCORE_ELIGIBLE_REAL_CLAIM으로 실패했다"가 들어간다.
LLM planner는 같은 일반 문서를 반복하는 대신 current/direct/anchor가 있는 clinical/regulatory source를 찾아야 한다.
```

## 검증

```bash
PYTHONPATH=src python -m unittest \
  tests.test_all_archetype_runtime_status_matrix \
  tests.test_all_archetype_runtime_parity_matrix -v
```

결과:

```text
Ran 12 tests
OK
```

추가 planner 연결 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_all_archetype_next_attempt_plan -v
```

결과:

```text
Ran 12 tests
OK
```

## 남은 작업

이번 패치는 감사/진단을 강화한 것이다. 아직 다음 조건은 충족되지 않았다.

```text
meaningful_runtime_parity_ready = false
runtime_parity_not_proven_count = 36
C24 production accepted claim = 0
C15/C28 accepted claim은 있으나 full thesis 미완성
6개 production full thesis row는 모두 required-positive/Green gap 보유
```

다음 실제 패치 방향:

```text
1. source_task_primary_failure_axis=PRIMITIVE_GAP_UNSATISFIED인 27개 아키타입의 source route를 primitive-specific query/task로 보강
2. C24는 current direct anchored clinical/regulatory source route를 먼저 고쳐 accepted claim 1개 이상 생성
3. C15/C28은 accepted claim을 required-positive/Green primitive closure로 연결
4. matrix에서 RUNTIME_PARITY_PROVEN이 아닌 행을 Goal4 완료 증거로 쓰지 않도록 계속 유지
```

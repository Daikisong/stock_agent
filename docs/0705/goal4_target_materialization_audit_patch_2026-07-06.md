# Goal4 Target Materialization Audit Patch - 2026-07-06

이 문서는 Goal4 runtime parity matrix의 `000000` placeholder / targetless source shell 문제를 고정한다.

## 결론

이번 패치는 Goal4를 완료시키는 패치가 아니다. 대신 이전 matrix가 잘못 읽힐 수 있던 부분을 바로잡았다.

```text
이전 표현:
  C08/C15/C24/C28 등 = SOURCE_TASK_EXECUTED

정확한 표현:
  C08/C15/C24/C28 등 = ARCHETYPE_DISCOVERY_TARGET_MATERIALIZATION_REQUIRED
```

쉬운 예:

```text
이전:
  "C08 환자 검사를 했다"처럼 보임

실제:
  C08 진료과 예약표만 있고, 아직 실제 환자 주민번호가 없음
  그래서 검사를 했다고 하면 안 되고, 먼저 실제 환자 식별이 필요함
```

## 고친 문제

2026-07-05 patched-v2 산출물에서 114개 seed 중 96개가 `000000`으로 materialization trace에 남아 있었다.

이 값은 실제 KRX 종목이 아니라, 아키타입 수준 discovery seed가 빈 symbol로 들어간 뒤 문서화 과정에서 fake ticker처럼 보인 것이다.

문제점:

```text
000000 source task 실행
-> runtime_source_task_execution_count 증가
-> matrix에서 SOURCE_TASK_EXECUTED로 표시
-> 실제 target-company source route를 실행한 것처럼 오해 가능
```

이건 Goal4의 핵심 요구와 맞지 않는다.

```text
Goal4 요구:
research -> source route -> accepted claim -> full thesis

정확한 상태:
research -> archetype-level discovery seed
-> target company materialization 아직 안 됨
-> accepted claim / full thesis 불가
```

## 코드 변경

추가:

```text
src/e2r/census/placeholder_symbols.py
```

주요 변경:

```text
1. 000000, 0000000, UNKNOWN, N/A, NONE, NULL, 빈 문자열을 placeholder symbol로 통일
2. census seed materialization trace에서 placeholder symbol을 null로 기록
3. target_symbol_mode와 target_materialization_status를 trace에 명시
4. parity matrix에서 targetless source shell을 실제 runtime_source_task_execution_count와 분리
5. all-archetype runtime status matrix에 TARGET_MATERIALIZATION_REQUIRED 상태 추가
6. next attempt plan에서 ARCHETYPE_TARGET_MATERIALIZATION attempt type 추가
7. archetype-level discovery query intent를 "direct target-company evidence 검증"이 아니라 "실제 target symbol materialize"로 수정
```

## 새 상태

재생성 후 핵심 수치:

```text
runtime_attempt_status_counts:
  ARCHETYPE_DISCOVERY_TARGET_MATERIALIZATION_REQUIRED = 32
  PLANNER_ATTEMPTED_ONLY = 1
  PRODUCTION_FULL_THESIS_ATTEMPTED = 2
  SOURCE_TASK_EXECUTED = 1

runtime_source_route_execution_status_counts:
  TARGETLESS_SOURCE_SHELL_EXECUTED_NO_TARGET = 24
  TARGET_MATERIALIZATION_REQUIRED_BEFORE_SOURCE_EXECUTION = 8
  SOURCE_TASK_EXECUTED_WITH_ACCEPTED_CLAIMS = 2
  SOURCE_TASK_EXECUTED_NO_ACCEPTED_CLAIMS = 1
  ROUTE_RECOVERED_NOT_EXECUTED = 1

runtime_parity_proof_status_counts:
  NOT_PROVEN_TARGET_MATERIALIZATION_REQUIRED = 32
  NOT_PROVEN_SCORE_PATH_ONLY = 2
  NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM = 1
  NOT_PROVEN_PLANNER_ONLY = 1
```

해석:

```text
36개 아키타입 중 32개는 아직 실제 target symbol materialization이 필요하다.
즉 source route가 "실제 종목"에 대해 증명된 것이 아니다.
```

대표 canary:

```text
C08:
  runtime_source_task_execution_count = 0
  targetless_source_task_execution_count = 14
  target_materialization_required_seed_count = 10

C15:
  runtime_source_task_execution_count = 0
  targetless_source_task_execution_count = 14
  target_materialization_required_seed_count = 10

C17:
  runtime_source_task_execution_count = 0
  targetless_source_task_execution_count = 0
  target_materialization_required_seed_count = 3

C24:
  runtime_source_task_execution_count = 0
  targetless_source_task_execution_count = 14
  target_materialization_required_seed_count = 10

C28:
  runtime_source_task_execution_count = 0
  targetless_source_task_execution_count = 14
  target_materialization_required_seed_count = 10

C29:
  runtime_source_task_execution_count = 28
  targetless_source_task_execution_count = 0
  symbols_sample = 017670, 024110
```

쉬운 예:

```text
C08/C15/C24/C28:
  진료과 예약표는 있음
  실제 환자 식별 전 shell 검사는 있었음
  환자별 검사 결과지는 없음

C29:
  실제 환자 017670, 024110에 대해 검사는 했음
  다만 accepted claim이 없어서 결과지는 아직 없음
```

## 다음 실행 plan 변화

next-attempt plan:

```text
plan_row_count = 36
source_task_count = 111
seed_event_count = 111
target_materialization_required_task_count = 96

attempt_type_counts:
  ARCHETYPE_TARGET_MATERIALIZATION = 32
  PROMOTED_SCORE_PATH_GAP_CLOSURE = 2
  SOURCE_EXECUTION_REPAIR = 1
  PLANNER_TO_SOURCE_TASK_MATERIALIZATION = 1
```

의미:

```text
대부분의 다음 작업은 source를 더 긁는 것이 아니라,
아키타입별로 실제 current target company/ticker를 먼저 materialize하는 일이다.
```

2026-07-05 후속 보정:

```text
research_reverse_case_inventory 기반 target 후보 물질화 후:
target_symbol_mode_counts:
  ARCHETYPE_LEVEL_DISCOVERY = 3
  RESEARCH_MEMORY_TARGET_CANDIDATE = 29
  SYMBOL_SPECIFIC = 4

research_memory_target_materialized_archetype_count = 29
research_memory_target_materialized_task_count = 87
target_materialization_unresolved_archetype_count = 3
target_materialization_required_task_count = 9
```

해석:

```text
이 문서가 지적한 "32개는 실제 target symbol materialization 필요" 문제 중
C01~C32는 연구자료 기반 후보 심볼이 붙었다.

다만 이것은 점수 근거가 아니다.
모든 후보는 current source-backed Evidence OS claim을 새로 통과해야 한다.
```

세부 후보 목록과 테스트 결과는 다음 문서에 고정했다.

```text
docs/0705/goal4_research_memory_target_materialization_plan_2026-07-05.md
```

## 검증

실행한 감사 명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_research_to_runtime_parity_until_pass --as-of-date 2026-07-05 --fail-on-c05-monoculture true --fail-on-unknown-target-promoted true --fail-on-required-positive-missing-over-threshold true --fail-on-research-proxy-score true
```

결과:

```text
exit code = 2
final_status = MEANINGFUL_RUNTIME_PARITY_NOT_READY
failed_on = C05_FULL_THESIS_MONOCULTURE, REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS
```

이 실패는 정상이다. 이번 패치는 완료 선언이 아니라 미완료 원인을 더 정확하게 분리했다.

실행한 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_research_to_runtime_parity_goal4 tests.test_all_archetype_runtime_status_matrix tests.test_all_archetype_next_attempt_plan -v
-> Ran 19 tests, OK

PYTHONPATH=src python -m unittest tests.test_census_v4_full_thesis_smoke_tasks tests.test_research_brain_v4_operational_modes -v
-> Ran 90 tests, OK

PYTHONPATH=src python -m unittest tests.test_planner_bias_audit tests.test_research_to_runtime_parity_goal4 -v
-> Ran 9 tests, OK

PYTHONPATH=src python -m unittest discover -s tests -v
-> Ran 5254 tests, OK

git diff --check
-> OK
```

## 남은 Goal4 blocker

아직 완료가 아닌 이유:

```text
1. meaningful_full_thesis_evidence_pass = false
2. full_thesis row는 C05 2개, C06 1개뿐
3. full_thesis row 3개 전부 required-positive/Green gap이 남음
4. C08/C15/C17/C24/C28 등은 production full-thesis가 아니라 target materialization 전 단계
5. C01~C32/C36 전체에 대해 accepted claim/full thesis parity가 아직 증명되지 않음
```

다음 실질 작업:

```text
ARCHETYPE_TARGET_MATERIALIZATION 32개를 실제 current target ticker 후보로 변환하는 단계가 필요하다.
그 다음에야 source-backed Evidence OS claim과 full thesis StageCourt를 다시 검증할 수 있다.
```

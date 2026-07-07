# Goal4 Self-Repair CLI Targetless Source Guard - 2026-07-07

## 결론

Goal4는 아직 완료가 아니다.

이번 작업에서 확인한 것은 두 가지다.

1. `run_research_to_runtime_parity_until_pass`가 이제 `max_iterations > 1`일 때 next-runtime manifest를 실제 Census v4 실행으로 넘긴다.
2. 실제 self-repair 실행 중 `symbol`이 없는 R13 archetype-level seed가 source execution으로 들어가 provider를 오래 붙잡는 문제가 확인되어 guard를 추가했다.

쉬운 예:

```text
나쁜 흐름:
R13 회계 신뢰 리스크를 볼 "회사"가 아직 없음
→ 그래도 DART/KIND/IR source task 실행
→ 어느 회사 공시를 볼지 모르는 상태로 provider 대기

고친 흐름:
R13 회계 신뢰 리스크를 볼 "회사"가 아직 없음
→ source execution 전 TARGET_MATERIALIZATION_REQUIRED로 종료
→ 먼저 실제 종목을 materialize하라고 다음 attempt에 남김
```

## 실제 실행 증거

실행 명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_research_to_runtime_parity_until_pass \
  --as-of-date 2026-07-05 \
  --mode full_thesis_balanced \
  --mandatory-archetypes C06,C08,C15,C17,C24,C28 \
  --max-iterations 2 \
  --fail-on-c05-monoculture true \
  --fail-on-unknown-target-promoted true \
  --fail-on-required-positive-missing-over-threshold true \
  --fail-on-research-proxy-score true
```

실행 산출물:

```text
output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01
```

실행 중 확인된 사실:

```text
planner_runs.jsonl: 108 rows
llm_prompts.jsonl: 108 rows
llm_responses.jsonl: 108 rows
latest stuck phase before interrupt:
  source_execution_start
  primary_archetype=R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
  symbol=""
  source_task_count=9
```

해당 run은 중간 산출물만 있으므로 score/stage/readiness 증거로 쓰면 안 된다.

```text
partial_run_invalid.json:
  verdict=INVALID_PARTIAL_OUTPUT
  status=INTERRUPTED
  score_or_stage_evidence_allowed=false
  full_thesis_promotion_allowed=false
```

## 패치 내용

### 1. Parity CLI self-repair 실행 연결

파일:

```text
src/e2r/cli/run_research_to_runtime_parity_until_pass.py
```

변경:

```text
max_iterations <= 1
→ 기존처럼 현재 output_root 감사만 수행

max_iterations > 1
→ 현재 감사
→ next runtime execution manifest 실행
→ 새 output_root를 다시 감사
→ self_repair_history 출력
```

또한 self-repair output_root는 timestamp를 붙여 매 실행마다 새 디렉터리를 사용하게 했다.

이유:

```text
같은 output_root를 재사용하면
이전 partial jsonl과 새 실행 결과가 섞여
accepted_claim/source_task/stage 증거가 오염될 수 있다.
```

### 2. Execution Manifest 상태 수정

파일:

```text
src/e2r/census/all_archetype_runtime_execution_manifest.py
```

기존 상태:

```text
READY_FOR_RESEARCH_BRAIN_INPUT_NOT_EXECUTED_BY_PARITY_CLI
```

새 상태:

```text
READY_FOR_RESEARCH_BRAIN_INPUT_PARITY_SELF_REPAIR_EXECUTABLE
```

이유:

이제 manifest는 단순 실행 안내서가 아니라 parity self-repair CLI가 실제로 사용할 수 있는 실행 입력이다.

### 3. Targetless Source Execution Guard

파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
```

변경:

```text
if event.symbol is empty:
    source task 생성/실행 금지
    phase=source_execution_skipped_target_materialization_required 기록
    watchlist item은 PENDING_EVIDENCE_OS_CLAIMS 유지
```

이유:

`ARCHETYPE_LEVEL_DISCOVERY` seed는 조사 대상을 찾기 위한 행정/계획 이벤트다. 실제 종목이 없으면 DART, KIND, IR, CompanyGuide 같은 source route를 실행할 수 없다.

## 현재 Goal4 상태

정상 v3 output 기준 stable docs는 복원했다.

```text
output_root:
output/census_v4/2026-07-07-goal4-all-archetype-next-runtime-attempt-seed-feedback-v3

final_status:
MEANINGFUL_RUNTIME_PARITY_NOT_READY

score-path rows:
6 archetypes

remaining blockers:
GREEN_GAP_ON_PROMOTED_ROWS
MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING
PRODUCTION_SCORE_PATH_IS_NOT_MEANINGFUL_FULL_THESIS_PASS
REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS
```

즉 이번 패치는 Goal4 완료가 아니라, self-repair 실행 경로와 targetless source hang을 고친 진행 패치다.

## 테스트

1차 targeted 실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_targetless_archetype_seed_does_not_execute_source_tasks \
  tests.test_research_to_runtime_parity_goal4 \
  tests.test_all_archetype_runtime_execution_manifest \
  tests.test_meaningful_full_thesis_production_acceptance \
  -v
```

결과:

```text
16 tests OK
```

전체 회귀 실행:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5289 tests in 450.022s
OK
```

추가 단위 테스트:

```text
test_targetless_archetype_seed_does_not_execute_source_tasks
```

이 테스트는 `symbol=None`인 archetype-level seed가 planner까지는 가되 source task를 실행하지 않고 `source_execution_skipped_target_materialization_required`로 남는지 검증한다.

## 다음 작업

다음 self-repair 재실행은 timestamp output_root를 쓰므로 stale partial 파일과 섞이지 않는다.

다음 확인 포인트:

```text
1. targetless R13 seed가 source execution으로 들어가지 않는지
2. self-repair run이 partial 없이 final readiness까지 끝나는지
3. C15/C24/C28 mandatory full-thesis row가 생기는지
4. promoted row required_positive_missing_rate가 내려가는지
5. 의미 있는 pass가 안 되면 source/provider/code blocker가 정확히 분류되는지
```

# Goal4 Manifest Runtime Attempt Patched-v2 Final Audit - 2026-07-05

이 문서는 Goal4 전 아키타입 runtime parity 실행의 두 번째 patched run 결과를 고정한다.

핵심 결론부터 말하면, 이번 실행은 **완료가 아니다.** 다만 이전 patched run에서 보였던 "planner/source/claim trace가 0으로 사라지는 문제"는 상당 부분 고쳤다. 이제는 실패가 사라지지 않고 장부에 남는다.

추가 후속 패치 기준:

```text
patched-v2 실행 자체는 114 seed로 수행됐다.
하지만 후속 코드 보정 후 next-attempt plan 재생성 결과는 111 seed/source task다.
차이는 placeholder symbol 000000을 실제 종목으로 취급하지 않도록 막았기 때문이다.

현재 재생성된 next-attempt plan:
- plan_row_count = 36
- seed_event_count = 111
- source_task_count = 111
- target_symbol_mode_counts = {"ARCHETYPE_LEVEL_DISCOVERY": 32, "SYMBOL_SPECIFIC": 4}

2026-07-05 후속 보정:
- `docs/0705/goal4_research_memory_target_materialization_plan_2026-07-05.md`에서 연구자료 reverse case inventory를 반영해 next-attempt plan을 다시 물질화했다.
- 최신 next-attempt plan의 target_symbol_mode_counts는 `{"ARCHETYPE_LEVEL_DISCOVERY": 3, "RESEARCH_MEMORY_TARGET_CANDIDATE": 29, "SYMBOL_SPECIFIC": 4}`다.
- 이 보정은 점수 합격이 아니라, C01~C32 다음 실행에 실제 심볼 후보를 붙이는 패치다.

추가로 C06 follow-up task는 source_pending 일부만 보지 않고
missing_required / green gap 전체를 포함한다.
현재 research_memory_followup_task_count = 7
  - C05 = 3
  - C06 = 4

검증:
PYTHONPATH=src python -m unittest discover -s tests -v
-> Ran 5254 tests in 424.029s, OK
```

쉬운 예:

```text
이전 실패:
  시험을 봤는데 답안지가 사라져서
  누가 몇 문제를 풀었는지도 모름

이번 실패:
  답안지는 남음
  114문제 중 planner가 78문제는 풀었고
  source task도 285개 실행됨
  하지만 정답 근거와 stage 승급 조건이 부족해 최종 합격은 아님
```

## 1. 실행 산출물

```text
output_root:
output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-patched-v2

seed source:
docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl

stdout:
INVALID_PARTIAL_OUTPUT

partial marker:
output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-patched-v2/PARTIAL_RUN_INVALID.md
```

최종 runtime progress:

```text
phase = completed
runtime_budget_exhausted = true
runtime_elapsed_seconds = 7281.392162
planner_run_count = 461
real_provider_success_count = 78
source_task_execution_count = 285
accepted_claim_count = 26
```

중요한 해석:

- `completed`는 프로세스가 종료됐다는 뜻이다.
- `INVALID_PARTIAL_OUTPUT`은 Goal4를 통과했다는 뜻이 아니다.
- runtime budget이 소진됐으므로 남은 seed들은 `planner_not_attempted_after_runtime_budget_exhausted`로 닫혔다.

## 2. 이번에 고친 코드 경로

### 2.1 Planner row-level reject

파일:

```text
src/e2r/research_brain/v4_planner_runtime.py
```

이전에는 Codex planner가 한 배치 안에서 한 row라도 forbidden self-check를 내면 전체 배치가 예외로 죽을 수 있었다.

예:

```text
5개 후보를 planner에 보냄
1개 후보가 score/stage key를 섞음
-> 예외 발생
-> 나머지 4개 성공 계획도 사라짐
```

패치 후:

```text
잘못된 row = rejected_by_validator=true
정상 row = real_provider_success=true
```

즉 한 후보가 틀려도 배치 전체를 버리지 않는다.

### 2.2 Planner leaf intermediate flush

파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
```

이전에는 source 단계에서 실패하면 `planner_runs.jsonl` 자체가 남지 않을 수 있었다. 그래서 `brain_web_runtime_progress.json`에는 planner 성공이 보이는데 공식 audit leaf에는 planner row가 0인 모순이 생겼다.

패치 후 planner batch가 끝날 때마다 다음 leaf를 중간 flush한다.

```text
planner_runs.jsonl
llm_prompts.jsonl
llm_responses.jsonl
```

단, 최종 성공 반환 후에는 `planner_runs.jsonl`을 최종 결과로 덮어쓴다. 중간 flush row와 최종 merge row가 중복되어 planner count가 2배가 되는 문제를 막기 위해서다.

### 2.3 Required-positive gap production PASS 차단

파일:

```text
src/e2r/census/census_runner_v4.py
```

이번 실행 산출물 자체는 패치 전 코드로 생성되어 아래처럼 남아 있다.

```text
full_thesis_production_audit.verdict = FULL_THESIS_PRODUCTION_PASS
production_full_thesis_row_count = 3
production_symbols = 002460, 003380, 005930
production_full_thesis_row_with_required_positive_missing_primitives_count = 3
production_full_thesis_row_with_green_gap_primitives_count = 3
```

이 라벨은 위험하다. 3개 row 전부 required-positive gap이 있는데도 PASS가 찍혔다.

패치 후에는 다음 blocker가 생긴다.

```text
production_full_thesis_rows_with_required_positive_missing_primitives
```

따라서 앞으로 같은 상태는 `FULL_THESIS_PRODUCTION_PASS`가 아니라 `PENDING_FULL_THESIS_PRODUCTION`이어야 한다.

쉬운 예:

```text
나쁜 판정:
  계약 thesis인데 계약 기간/마진 bridge가 비어 있음
  그래도 점수 경로가 닫혔으니 PASS

수정 판정:
  점수 경로는 닫혔지만 필수 positive 증거가 비어 있음
  full thesis complete가 아니라 pending
```

## 3. 이번 실행의 실제 수치

### 3.1 Brain/Web attempt

```text
verdict = ATTEMPTED_NOT_CUTOVER_READY
full_thesis_seed_event_count = 114
full_thesis_seed_planner_run_count = 114
full_thesis_seed_real_provider_success_count = 78
real_provider_failure_count = 36
full_thesis_seed_source_task_execution_count = 285
full_thesis_seed_accepted_claim_count = 26
full_thesis_seed_stagecourt_trace_count = 40
unique_accepted_claim_count = 7
deterministic_scorer_output_count = 7
brain_to_census_stage_exported_count = 0
```

blocker:

```text
Research Brain StageCourt traces are not promoted into census_stage_status rows
```

해석:

- Research Brain 내부에서는 claim과 StageCourt trace가 일부 생겼다.
- 하지만 그 결과가 Census의 공식 `census_stage_status` row로 안전하게 승격되지 않았다.
- 그러므로 운영 stage로 쓰면 안 된다.

### 3.2 Brain/Web readiness gate

```text
verdict = BLOCKED
llm_planner_call_count = 114
llm_planner_success_count = 78
source_task_execution_count = 285
web_search_call_count = 28
web_search_task_count = 29
web_fetched_document_count = 7
llm_claim_extractor_attempt_count = 85
web_or_llm_accepted_claim_count = 0
official_accepted_claim_count = 7
brain_promoted_stage_row_count = 3
```

blockers:

```text
LLM claim extractor provider errors are unresolved: 3
web/LLM accepted claim count is zero
Brain/Web source task budget caps were exceeded: 30
Brain/Web evidence documents include snapshot:// sources
Brain/Web stage row was promoted despite blockers
brain stage promotion verdict is not PROMOTION_APPLIED: FAIL_UNSAFE_PROMOTION
Brain/Web operational minimum fetched documents not met: 7/10
Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

해석:

- planner는 돌았다.
- source task도 돌았다.
- 하지만 운영 web/LLM claim은 0개다.
- 일부 stage row가 blocker가 남은 상태에서 promotion되어 `FAIL_UNSAFE_PROMOTION`이 났다.
- 따라서 운영 cutover는 금지다.

## 4. Seed materialization 상태

```text
verdict = FAIL
operator_materialization_status = PENDING_FULL_THESIS_MATERIALIZATION
seed_event_count = 114
planner_run_seed_count = 114
real_provider_success_seed_count = 78
source_task_execution_seed_count = 40
accepted_claim_seed_count = 7
stagecourt_trace_seed_count = 7
actual_materialization_pass_allowed = false
full_thesis_seed_promotion_pass = false
```

상태 분포:

| status | count | 의미 |
| --- | ---: | --- |
| `PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS` | 36 | planner가 성공 답을 못 냄 |
| `SOURCE_TASK_NOT_EXECUTED` | 38 | planner 이후 source 실행까지 못 감 |
| `ACCEPTED_CLAIM_NOT_CREATED` | 33 | source는 갔지만 accepted claim이 안 생김 |
| `STAGECOURT_READY_NOT_PROMOTED` | 4 | StageCourt는 생겼지만 승격 불가 |
| `FULL_THESIS_PROMOTED` | 3 | full-thesis row로 승격됐지만 아래 PASS 문제 때문에 완료 아님 |

아키타입별 예:

| archetype | status |
| --- | --- |
| `C06_HBM_MEMORY_CUSTOMER_CAPACITY` | `FULL_THESIS_PROMOTED=1`, `STAGECOURT_READY_NOT_PROMOTED=2` |
| `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY` | `ACCEPTED_CLAIM_NOT_CREATED=1`, `SOURCE_TASK_NOT_EXECUTED=2` |
| `C15_MATERIAL_SPREAD_SUPERCYCLE` | `ACCEPTED_CLAIM_NOT_CREATED=1`, `PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS=1`, `SOURCE_TASK_NOT_EXECUTED=1` |
| `C24_BIO_TRIAL_DATA_EVENT_RISK` | `ACCEPTED_CLAIM_NOT_CREATED=1`, `SOURCE_TASK_NOT_EXECUTED=2` |
| `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` | `ACCEPTED_CLAIM_NOT_CREATED=1`, `PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS=1`, `SOURCE_TASK_NOT_EXECUTED=1` |

중요한 점:

```text
전 아키타입 seed가 planner 입력으로 들어간 것은 맞다.
하지만 전 아키타입 runtime full thesis가 닫힌 것은 아니다.
```

## 5. 왜 아직 Goal4 완료가 아닌가?

Goal4의 목표는 이게 아니다.

```text
planner를 많이 호출했다
source task가 몇 개 돌았다
일부 row가 점수를 냈다
```

Goal4의 목표는 이거다.

```text
모든 아키타입에서
과거 연구가 만든 evidence contract에 맞춰
실제 source-backed claim이 생기고
claim -> primitive -> score contribution -> StageCourt -> census stage row까지
운영 장부로 닫히는 것
```

이번 실행은 다음 지점에서 막혔다.

```text
114 seed selected
-> 78 planner success
-> 285 source task execution
-> 26 accepted claim, unique 7
-> 7 deterministic scorer output
-> census stage export 0
-> readiness BLOCKED
```

따라서 상태는:

```text
Goal4 = NOT_COMPLETE
Runtime trace materialization = PARTIALLY_FIXED
Production full thesis = NOT_READY
Meaningful all-archetype parity = NOT_READY
```

## 6. 이번 실행에서 새로 드러난 문제

### 6.1 Synthetic seed가 회사처럼 쓰이는 문제

진행 중 source log에 이런 row가 반복됐다.

```text
company_name = C19_BRAND_RETAIL_INVENTORY_MARGIN
symbol = ""
primary_archetype = C19_BRAND_RETAIL_INVENTORY_MARGIN
```

이건 실제 운영 후보가 아니다. 아키타입 이름을 회사명처럼 쓰면 source acquisition이 제대로 된 issuer-scoped evidence를 만들 수 없다.

쉬운 예:

```text
정상:
  company_name = 삼성전자
  symbol = 005930
  primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY

문제:
  company_name = C06_HBM_MEMORY_CUSTOMER_CAPACITY
  symbol = ""
  primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

아키타입 parity를 보려면 seed는 "아키타입 이름"이 아니라 "그 아키타입을 실제로 대표할 수 있는 issuer 후보"로 materialize되어야 한다.

### 6.2 Planner not attempted after runtime budget

최종 `planner_runs.jsonl`은 808행이다.

```text
real planner success = 78
codex_cli_timeout = 30
R13 primary invalid reject = 6
planner_not_attempted_after_runtime_budget_exhausted = 694
```

이 808행은 114 seed만 뜻하지 않는다. runtime budget 이후 남은 watchlist item을 pending planner row로 닫으면서 늘어난 것이다.

중요한 점:

- 114 seed는 실제 planner attempt 대상이었다.
- 그중 real-provider success는 78개다.
- 전체 output row 808을 "808개 후보가 정상 연구됐다"로 읽으면 안 된다.

### 6.3 `FULL_THESIS_PRODUCTION_PASS` 낡은 라벨

이번 산출물의 `full_thesis_production_audit.json`은 아직 다음처럼 말한다.

```text
verdict = FULL_THESIS_PRODUCTION_PASS
production_symbols = 002460, 003380, 005930
required_positive_missing_primitives = 3/3
green_gap_primitives = 3/3
```

이건 산출물 생성 당시 코드의 문제다. 이번 패치로 required-positive gap이 있으면 blocker가 생기도록 바꿨다.

따라서 이 산출물을 읽을 때는 다음처럼 해석해야 한다.

```text
기계 파일 라벨:
  FULL_THESIS_PRODUCTION_PASS

감사상 실제 의미:
  score path 일부 close
  meaningful full thesis complete 아님
  전체 run은 INVALID_PARTIAL_OUTPUT
```

## 7. 검증

통과:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
```

결과:

```text
Ran 75 tests in 10.206s
OK
```

통과:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_goal_required_audits tests.test_census_v4_full_thesis_smoke_tasks -v
```

결과:

```text
Ran 19 tests in 93.910s
OK
```

추가로 targeted tests:

```text
test_codex_planner_forbidden_self_check_rejects_row_without_aborting_batch
test_runtime_planner_leaf_flush_survives_source_execution_exception
test_real_planner_success_limit_skips_failed_attempts_and_continues
test_production_audit_blocks_required_positive_missing_primitives
test_green_gap_follow_up_trace_does_not_replace_representative_full_thesis_row
test_provider_failed_green_gap_blocks_production_full_thesis_final_score
```

핵심 목적:

- invalid planner row가 배치 전체를 죽이지 않는지 확인.
- source 단계 예외가 나도 planner leaf가 남는지 확인.
- required-positive missing primitive가 production PASS를 막는지 확인.
- green gap follow-up은 representative row를 덮어쓰지 않는지 확인.

## 8. 다음 패치 우선순위

1. Synthetic archetype-only seed를 실제 issuer-backed seed로 바꿔야 한다.
   - `company_name=C06...`, `symbol=""` 같은 row는 source-backed runtime parity 증거가 될 수 없다.

2. Accepted claim을 web/LLM path에서 0개로 만드는 원인을 분리해야 한다.
   - provider error 3개
   - source budget cap exceeded 30개
   - snapshot source 포함
   - official-only accepted claim과 web/LLM accepted claim 분리

3. Stage promotion은 readiness blocker가 0일 때만 허용해야 한다.
   - 이번 run은 `brain_stage_promotion_unsafe_promoted_count=3`이다.

4. Production audit label은 score-path와 meaningful-thesis를 계속 분리해야 한다.
   - required-positive gap이 있으면 PASS 금지.
   - green gap은 Green 승격에는 금지이며, Stage2/Yellow면 별도 follow-up gap으로 남긴다.

5. Runtime resume가 필요하다.
   - 2시간 budget에서 78 planner success, 36 failure/pending으로 끝났다.
   - 처음부터 다시 돌리기보다 existing planner/source leaf를 이어받아 남은 seed만 처리해야 한다.

## 9. 최종 판정

```text
Goal4 final completion:
  NO

All-archetype runtime attempt:
  YES, attempted

Planner/source/claim trace disappearance bug:
  PARTIALLY_FIXED

Production full thesis readiness:
  NO

Meaningful all-archetype parity:
  NO

Safe to use 002460/003380/005930 rows as operator full-thesis stage:
  NO
```

한 줄 결론:

> 이번 작업은 Goal4를 완료한 게 아니라, Goal4가 왜 아직 완료가 아닌지 더 정직하게 드러나도록 planner/source/claim 장부와 production PASS gate를 고친 단계다.

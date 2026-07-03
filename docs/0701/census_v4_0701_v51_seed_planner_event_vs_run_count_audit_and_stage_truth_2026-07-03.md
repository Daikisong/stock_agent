# Census v4 0701 v51 Seed Planner Event Vs Run Count Audit And Stage Truth

작성일: 2026-07-03 KST

## v52 최신화 주의

이 문서는 v51 시점의 seed planner event/run count 분리를 설명한다.
이후 v52에서 machine-readable full unittest artifact를 생성하고 canonical Census v4에 연결했다.

최신 기준 문서:

```text
docs/0701/census_v4_0701_v52_machine_readable_test_artifact_gate_clear_and_remaining_goal_blockers_2026-07-03.md
```

v52 이후 변경:

```text
FULL_TEST_ARTIFACT_PASS = PASS
machine_readable_test_result_artifact_missing blocker 제거
required_goal_completion_pass_count = 14
required_goal_completion_pending_count = 5
```

v51의 핵심 결론은 유지된다.

```text
상태판 Stage는 있다.
운영 FULL_THESIS Stage는 0개다.
seed planner event count와 planner run row count는 분리해서 봐야 한다.
```

## 0. 최종 결론

현재 2026-07-01 canonical Census v4 산출물에는 Stage처럼 보이는 row가 있다.
하지만 운영에 써도 되는 `FULL_THESIS` Stage row는 아직 0개다.

정확히 나누면 아래와 같다.

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS:
  PASS

CENSUS_EVENT_BOARD 상태판 Stage:
  row_count = 3391
  non_Stage0 = 85

operator-admissible FULL_THESIS Stage:
  row_count = 0

verified FULL_E2R_100 score:
  row_count = 0

FULL_THESIS refresh queue:
  row_count = 85

FULL_THESIS seed materialization audit:
  verdict = PASS
  seed_event_count = 85
  trace_row_count = 85
  status_counts = PLANNER_NOT_RUN 85
  full_thesis_promoted_seed_count = 0
  full_thesis_seed_promotion_pass = false

FULL_THESIS production runner:
  verdict = NOT_REQUESTED
  production_mode_requested = false
  candidate_row_count = 0
  promoted_full_thesis_row_count = 0
```

쉬운 예:

```text
3391명 전체 명단에 접수 상태가 붙었다.
그중 85명은 "진료가 필요해 보임"으로 대기열에 올라갔다.
하지만 의사가 검사하고 진단서를 끝까지 쓴 사람은 0명이다.

따라서 "상태판은 있다"가 맞고,
"운영 진단 Stage가 있다"는 아직 아니다.
```

이번 v51 패치는 이 현재 진실을 더 잘 숨기지 않기 위한 것이다.
특히 `planner_run_count`라는 이름 하나로 seed 이벤트 수와 planner 실행 row 수를 섞어 보지 않도록
runtime audit 필드를 분리했다.

## 1. 왜 v51이 필요한가

v50에서 이미 아래 둘을 분리했다.

```text
FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS
  = seed/trace 장부가 정상이다.

FULL_THESIS_SEED_PROMOTION_PASS
  = 적어도 하나의 seed가 production FULL_THESIS로 실제 승격됐다.
```

그런데 남은 오해 가능성이 하나 있었다.

```text
full_thesis_seed_planner_run_count = 2
```

이 숫자를 보면 다음 둘 중 무엇인지 헷갈릴 수 있다.

```text
1. planner를 탄 seed 이벤트가 2개다.
2. planner 실행 row가 2개다.
```

둘은 다르다.

쉬운 예:

```text
seed A:
  initial planner run 1번
  retry planner run 1번

seed B:
  initial planner run 1번

결과:
  planner를 탄 seed 이벤트 = 2개
  planner 실행 row = 3개
```

이게 섞이면 다음 에이전트가 이렇게 공격할 수 있다.

```text
"2개 seed가 실행됐다는 뜻인가?"
"2번 호출됐다는 뜻인가?"
"retry까지 실제로 row가 남았는가?"
"event board row를 planner run으로 잘못 세고 있는가?"
```

따라서 v51에서는 audit count를 아래처럼 분리했다.

```text
full_thesis_seed_planner_attempted_event_count
  = planner가 실제로 닿은 distinct seed event 수

full_thesis_seed_planner_run_row_count
  = seed 관련 planner run row 수

full_thesis_seed_planner_run_count
  = 기존 호환 필드. 현재는 distinct seed event count와 같은 의미로 유지한다.
```

## 2. 이번 코드 패치

핵심 변경 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_full_thesis_smoke_tasks.py
```

### 2.1 `_full_thesis_seed_runtime_counts()`

기존에는 seed planner run count가 사실상 distinct seed count로 쓰였다.
이번 패치에서는 seed event와 planner run row를 따로 센다.

```text
planner_attempted_event_count:
  seed planner run row에서 candidate_event_id를 distinct로 센 값

planner_run_row_count:
  full-thesis seed로 판정된 planner run row 전체 개수

planner_run_count:
  backward compatibility 필드.
  현재는 planner_attempted_event_count와 같은 값이다.
```

full-thesis seed 여부는 아래 조건으로 판정한다.

```text
event.source_family == CensusFullThesisQueue
OR event.event_type == full_thesis_refresh_seed
OR event.structured_payload.seed_role == planner_input_only
```

중요:

```text
일반 daily planner row는 seed runtime count에 섞이면 안 된다.
retry row는 planner_run_row_count에는 들어가지만,
distinct event count에는 한 seed로만 들어가야 한다.
```

### 2.2 readiness / brain web audit 전파

아래 audit 결과에 새 필드를 노출했다.

```text
brain_web_attempt
brain_web_readiness_gate
readiness_verdict
brain_web_readiness_gate_audit.json
```

새 필드:

```text
full_thesis_seed_planner_attempted_event_count
full_thesis_seed_planner_run_row_count
full_thesis_seed_planner_run_count
```

현재 canonical disabled run에서는 모두 0이어야 한다.
이유는 Brain/Web이 disabled라서 seed 85개가 queue에는 있어도 planner가 실제 실행되지 않았기 때문이다.

```text
full_thesis_seed_event_count = 85
full_thesis_seed_planner_attempted_event_count = 0
full_thesis_seed_planner_run_row_count = 0
full_thesis_seed_planner_run_count = 0
full_thesis_seed_accepted_claim_count = 0
full_thesis_seed_stagecourt_trace_count = 0
```

쉬운 예:

```text
대기표 85장이 있다.
하지만 의사에게 실제로 넘어간 대기표는 0장이다.
따라서 planner attempted도 0, planner run row도 0이다.
```

### 2.3 테스트 추가

추가/보강한 핵심 테스트:

```text
test_seed_runtime_counts_split_attempted_seed_events_from_planner_rows
```

테스트 시나리오:

```text
seed A:
  initial planner run
  retry planner run

seed B:
  initial planner run

daily C:
  일반 daily planner run

기대값:
  planner_attempted_event_count = 2
  planner_run_row_count = 3
  planner_run_count = 2
  daily C는 seed count에서 제외
```

이 테스트가 막는 버그:

```text
retry를 distinct seed로 잘못 세는 버그
일반 daily planner row를 full-thesis seed run으로 섞는 버그
planner event 수와 run row 수를 같은 숫자로 오해하는 버그
```

## 3. canonical output 재검증

명령:

```text
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
  --target-gate anti_fake \
  --write-operational-docs true \
  --fail-on-critical-audit true
```

결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

현재 readiness label:

```text
IMPLEMENTATION_MERGED
V3_FORENSIC_REVIEW_COMPLETE
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
ATOMIC_STAGE_DECISION_PASS
SCORE_SCALE_PASS
STAGE_SEMANTICS_PASS
SEMANTIC_PRIMITIVE_GUARD_PASS
DAILY_EVENT_FULL_THESIS_SEPARATION_PASS
CENSUS_ASSESSMENT_CANDIDATE_EVENT_SEPARATION_PASS
FULL_THESIS_SMOKE_PENDING
FULL_THESIS_REFRESH_QUEUE_PRESENT
FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS
FULL_THESIS_SEED_PROMOTION_PENDING
OFFICIAL_BASELINE_OR_LEDGER_REFRESH_ONLY
OFFICIAL_BASELINE_EVIDENCE_CLAIM_PAYLOAD_PRESENT
KNOWN_BAD_REGRESSION_PASS
SELF_REPAIR_LOOP_PASS
RESEARCH_BRAIN_V4_REPORT_BRIDGE_IMPORTED
```

현재 remaining operational gaps:

```text
full thesis EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt path not run
event-board non-Stage0 rows exist but are not operational full-thesis stages
full-thesis refresh queue exists but production full-thesis StageCourt paths are not closed
full-thesis seed materialization audit shows no promoted FULL_THESIS seed
source-backed replay parity across all archetypes is not proven
Brain/Web/LLM acquisition artifacts are not produced in this disabled ledger-refresh run
Research Brain v4 imported report bundle is shadow/import-only and not admissible as Census production cutover evidence
```

해석:

```text
ANTI_FAKE는 통과했다.
하지만 goal 완료는 아니다.
운영 Stage도 아직 아니다.
```

## 4. 현재 Stage 존재 여부 답변

사용자 질문:

```text
뭔가 잘못되고있는거맞지? stage가 있는애들이 있긴해?
```

정확한 답:

```text
상태판 Stage는 있다.
운영 FULL_THESIS Stage는 없다.
```

현재 queue 분포:

```text
full_thesis_refresh_queue row_count = 85

priority_bucket:
  P2_EVENT_WATCH_REFRESH = 36
  P1_MATERIAL_STAGE_REFRESH = 30
  P1_PENDING_MATERIAL_REFRESH = 18
  P0_RISK_REVIEW_REFRESH = 1

source_base_stage:
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

source_stage_decision_status:
  FINAL = 36
  PENDING_MATERIAL_GAPS = 30
  SOURCE_PENDING = 18
  RISK_REVIEW = 1
```

이 85개는 운영 Stage가 아니라 `FULL_THESIS` 재조사 후보 seed다.

예:

```text
삼성전자:
  queue에는 있음
  source_base_stage = Stage1
  source_stage_decision_status = FINAL
  priority_bucket = P2_EVENT_WATCH_REFRESH
  하지만 materialization_blocker = full_thesis_refresh_task_has_no_research_brain_stagecourt_trace
  따라서 운영 FULL_THESIS Stage 아님
```

SK하이닉스도 같은 구조다.

```text
SK하이닉스:
  queue에는 있음
  source_base_stage = Stage1
  source_stage_decision_status = FINAL
  priority_bucket = P2_EVENT_WATCH_REFRESH
  하지만 FULL_THESIS refresh task는 아직 실제 Research Brain / StageCourt trace로 닫히지 않음
  따라서 운영 FULL_THESIS Stage 아님
```

중요:

```text
Stage1 / Stage2-Watch / Red라는 문자열이 보인다고 해서
그게 곧 운영 투자 thesis Stage는 아니다.

현재 값은 "재조사 우선순위와 현재 상태판"이다.
운영 점수/Stage로 쓰려면 accepted claim -> primitive -> score contribution -> StageCourt -> FULL_THESIS row가 닫혀야 한다.
```

## 5. 산출물 해시

현재 canonical output에서 다음 artifact를 확인했다.

```text
artifact_manifest.json
  byte_size = 27339
  sha256 = be159c3b91ca1e2db5f6aab2e71e5cc5b8900c405d764dfa80389c97dda1f78f

readiness_verdict.json
  byte_size = 9786
  sha256 = e057e2feee603b374a7f5c624c4e4718567e711d68ad82bba6d106a0993e91fb

brain_web_readiness_gate_audit.json
  byte_size = 3806
  sha256 = 66d13485c72d0002e9ca81f7e4088c044dd0e94582547f569f4a61b5e131cf8a

acceptance_report.md
  byte_size = 7010
  sha256 = 1c627b36d3b92461b1b75bc65b91d62642f6ef41caaa2a28ebc0c6e4365747ed

full_thesis_seed_materialization_audit.json
  byte_size = 2007
  sha256 = 42d6a14baeb189701ab68d5eabe54d5d62e0c878cbc2d24e3464fbdd8b78d839

full_thesis_seed_materialization_trace.jsonl
  byte_size = 93707
  row_count = 85
  sha256 = 3ab2e02534db83b207614d13e751d8557b00a982901e372b307988e6f0cdc56c

full_thesis_production_runner_audit.json
  byte_size = 10618
  sha256 = ad34274d1c2679f4674cb38e1d525e9383890d2e464a9b2a4cf0565d7957779a

goal_requirement_matrix_audit.json
  byte_size = 11956
  sha256 = d05126e75c637642e70e92295c1d9fb4e07c4b1ff6ec093ce939c2b1d1db83f9

goal_completion_audit.json
  byte_size = 2744
  sha256 = 444d6ecb0705f43160013a0f7751b3750925eaae4b0306222d95a14830cc386c
```

주의:

```text
v50 문서에 적힌 readiness_verdict / manifest hash는 v51 canonical rerun 이후 일부 바뀌었다.
다음 에이전트는 v51의 hash를 최신 기준으로 봐야 한다.
```

## 6. 테스트 결과

### 6.1 targeted tests

명령:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_controlled_smoke_is_disabled_by_default \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_enabled_provider_none_measures_seed_planner_consumption_without_materialization \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_seed_runtime_counts_split_attempted_seed_events_from_planner_rows \
  -v
```

결과:

```text
Ran 3 tests
OK
```

### 6.2 related audit suite

명령:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_manifest_counts_match_report \
  -v
```

결과:

```text
Ran 47 tests in 34.933s
OK
```

### 6.3 full suite

명령:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5077 tests in 211.027s
OK
```

## 7. 교차검증 결론

### 7.1 지금 좋아진 점

이번 상태는 과거보다 정직하다.

```text
이전 위험:
  Stage row가 있으니 운영 Stage가 있는 것처럼 보일 수 있음.

현재:
  stage_scope_notice = NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST
  operational_stage_use_allowed = false
  full_thesis_stage_row_count = 0
  full_e2r_verified_score_row_count = 0
```

`FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS`도 이제 승격 완료로 읽히지 않는다.

```text
labels contains FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS
labels contains FULL_THESIS_SEED_PROMOTION_PENDING
labels does not contain FULL_THESIS_SEED_PROMOTION_PASS
```

planner count도 더 이상 한 숫자로 뭉개지 않는다.

```text
attempted_event_count:
  seed 몇 개가 planner를 탔는가

run_row_count:
  retry 포함 planner row가 몇 개인가
```

### 7.2 아직 안 된 점

운영 pipeline으로 보면 핵심은 아직 안 됐다.

```text
Brain/Web disabled canonical run:
  full_thesis_seed_event_count = 85
  planner attempted event = 0
  planner run row = 0
  source task execution = 0
  accepted claim = 0
  stagecourt trace = 0
  promoted FULL_THESIS = 0
```

쉬운 예:

```text
대기표는 85장 있다.
하지만 의사에게 아직 한 장도 전달되지 않았다.
검사도 0건이고, 진단서도 0건이다.
```

따라서 지금 완료라고 말하면 안 된다.

```text
가능한 말:
  "anti-fake ledger/status-board gate는 통과했다."
  "FULL_THESIS refresh queue는 85개 생성됐다."
  "seed audit은 정상이다."
  "하지만 운영 FULL_THESIS Stage는 0개다."

불가능한 말:
  "daily 운영 Stage가 나왔다."
  "삼성전자/하이닉스 FULL_THESIS Stage가 확정됐다."
  "goal.md가 완료됐다."
  "Brain/Web evidence path가 운영 통과했다."
```

## 8. 다음 패치 방향

다음 패치는 count 명확화가 아니라 실제 materialization을 닫아야 한다.

우선순위:

```text
P0. production FULL_THESIS mode를 명시적으로 켠 실행에서 seed 85개 중 최소 하나를
    real planner -> bounded source task -> accepted claim -> primitive -> score contribution -> StageCourt까지 닫는다.

P1. Brain/Web disabled canonical run에서는 계속 promotion이 0이어야 한다.
    disabled run에서 갑자기 FULL_THESIS row가 생기면 critical fail이다.

P2. Brain/Web enabled strict run에서는 planner/source/provider 실패를 낮은 점수로 확정하지 말고
    Source/Provider Pending으로 남긴다.

P3. queue row만으로 Stage를 승격하지 못하게 유지한다.
    queue는 접수표이고, accepted claim이 없으면 점수 evidence가 아니다.

P4. 삼성전자/하이닉스 smoke는 별도 FULL_THESIS run에서만 판단한다.
    현재 canonical disabled run의 Stage1 queue status를 C06/HBM 운영 Stage로 해석하면 안 된다.
```

필수 acceptance:

```text
1. `production_mode_requested=true`인 run에서만 production runner가 FULL_THESIS candidate를 본다.
2. candidate는 queue row가 아니라 Research Brain 또는 official full-thesis StageCourt trace에서 온다.
3. nonzero FULL_E2R_100 score는 accepted_claim_id 없는 contribution을 허용하지 않는다.
4. hard break는 direct target, current, source quorum, valid anchor가 없으면 만들 수 없다.
5. planner retry는 run row에는 남지만 seed event distinct count를 부풀리지 않는다.
6. source/provider failure는 낮은 Stage 확정이 아니라 Pending이다.
7. disabled ledger-refresh run은 계속 `FULL_THESIS row = 0`이어야 한다.
```

## 9. 다음 에이전트 공격 포인트

다음 에이전트는 아래를 빡세게 확인해야 한다.

```text
1. `FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS`를 완료로 과장한 곳이 남아 있는가?
2. `FULL_THESIS_SEED_PROMOTION_PASS` 없이 goal completion이 true가 되는 경로가 있는가?
3. `planner_run_count`를 planner row count처럼 해석하는 문서/코드가 남아 있는가?
4. queue row 85개를 production candidate로 직접 승격하는 경로가 있는가?
5. disabled run에서 source task / accepted claim / StageCourt trace가 생기는가?
6. enabled run에서 provider failure를 낮은 점수로 확정하는가?
7. 삼성전자/하이닉스 queue Stage1을 C06 FULL_THESIS Stage로 출력하는 경로가 있는가?
8. `EVENT_WEIGHTED_PARTIAL` score를 FULL_E2R_100 점수처럼 보여 주는 경로가 있는가?
9. `BRAIN_WEB_PARTIAL` shadow/import row를 production row처럼 세는 경로가 남아 있는가?
10. retry row가 많을 때 seed event count와 run row count가 idempotent하게 유지되는가?
```

## 10. 최종 판단

이번 v51의 의미는 아래 하나다.

```text
"Stage가 있는 척하지 않는다"에서 한 단계 더 나아가,
"planner를 돌린 척하지 않는다"까지 audit count를 쪼갰다.
```

하지만 운영 목표는 아직 미완료다.

```text
현재 완료:
  anti-fake full universe status board
  seed queue / seed trace 장부 정상성
  materialization audit honesty
  promotion gate 분리
  seed planner event count와 run row count 분리

현재 미완료:
  real Brain/Web/official full-thesis materialization
  accepted claim-backed FULL_E2R_100 score
  production FULL_THESIS Stage
  all-archetype source-backed replay parity
  삼성전자/하이닉스 운영 smoke Stage
```

따라서 다음 작업의 핵심은 새 숫자를 더 만드는 것이 아니라,
85개 seed 중 실제로 source-backed claim chain을 닫는 것이다.

```text
접수표 -> 진료 -> 검사 -> 진단서

현재는 접수표와 접수표 감사까지다.
다음은 실제 진료 경로를 닫아야 한다.
```

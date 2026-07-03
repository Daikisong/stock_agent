# Census v4 0701 v50 Seed Promotion Gate Split Cross-Validation And Next Patch Direction

작성일: 2026-07-03 KST

## v51 최신화 주의

이 문서는 v50 시점의 seed promotion gate split을 설명한다.
이후 v51에서 seed planner count가 다시 분리됐다.

최신 기준 문서:

```text
docs/0701/census_v4_0701_v51_seed_planner_event_vs_run_count_audit_and_stage_truth_2026-07-03.md
```

v51 이후에는 아래 필드를 최신 기준으로 본다.

```text
full_thesis_seed_planner_attempted_event_count
full_thesis_seed_planner_run_row_count
full_thesis_seed_planner_run_count
```

또한 v50에 기록된 일부 canonical artifact hash는 v51 canonical rerun hash로 대체된다.
v50의 핵심 결론은 유지된다.

```text
상태판 Stage는 있다.
운영 FULL_THESIS Stage는 0개다.
FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS는 완료가 아니라 장부 정상성이다.
FULL_THESIS_SEED_PROMOTION_PASS는 아직 pending이다.
```

## 0. 최종 결론

이번 v50 패치는 `FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS`와 `FULL_THESIS_SEED_PROMOTION_PASS`를 분리했다.

현재 canonical output 기준 사실은 아래와 같다.

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS:
  PASS

leaf_artifact_audit:
  verdict = PASS
  critical_count = 0

CENSUS_EVENT_BOARD 상태판 Stage:
  row_count = 3391
  non_Stage0 = 85

operator-admissible FULL_THESIS Stage:
  row_count = 0

verified FULL_E2R_100 score:
  row_count = 0

FULL_THESIS seed materialization audit:
  verdict = PASS
  seed_event_count = 85
  trace_row_count = 85
  status_counts = PLANNER_NOT_RUN 85
  full_thesis_promoted_seed_count = 0
  full_thesis_seed_promotion_pass = false
```

쉬운 예:

```text
85명의 환자가 접수표에는 올라왔다.
접수표 누락이나 중복은 없다.
하지만 실제 진단서가 끝까지 작성된 환자는 0명이다.

따라서 "접수표 감사 PASS"는 맞지만,
"진단 완료 PASS"는 아니다.
```

이 상태를 운영 용어로 쓰면:

```text
Stage가 전혀 없는 것은 아니다.
하지만 지금 존재하는 Stage는 CENSUS_EVENT_BOARD 상태판 Stage다.
운영용 FULL_THESIS Stage는 아직 없다.
```

## 1. v49의 남은 오해 가능성

v49는 `full_thesis_seed_materialization_audit.json`을 readiness와 goal audit에 연결했다. 그 자체는 맞았다.

하지만 v49만 보면 다음 오해가 가능했다.

```text
FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS
  -> required goal gate PASS

그러면 seed materialization이 완료된 것인가?
```

정답은 아니다.

`FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS`는 아래를 보장한다.

```text
seed_event_count와 trace_row_count가 맞는다.
실행 전 score evidence가 새지 않았다.
실행 전 stage promotion이 새지 않았다.
source task / accepted claim / StageCourt 순서 위반이 없다.
잘못 promoted된 FULL_THESIS seed가 없다.
```

반대로 이것은 아래를 보장하지 않는다.

```text
real planner가 돌았다.
bounded source task가 실행됐다.
accepted claim이 생겼다.
primitive mapping이 됐다.
score contribution이 생겼다.
StageCourt가 운영 FULL_THESIS Stage를 냈다.
```

따라서 v50에서는 실제 승격을 별도 gate로 분리했다.

```text
FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS
  = 감사표가 정상이다.

FULL_THESIS_SEED_PROMOTION_PASS
  = 적어도 하나의 seed가 production FULL_THESIS로 실제 승격됐다.
```

## 2. 이번 코드 패치

핵심 변경 파일:

```text
src/e2r/census/census_runner_v4.py
```

### 2.1 readiness verdict

`_readiness_verdict()`에서 seed promotion 여부를 계산한다.

```text
full_thesis_seed_promotion_pass =
  full_thesis_promoted_seed_count > 0
```

readiness label은 이제 둘로 나뉜다.

```text
FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS
FULL_THESIS_SEED_PROMOTION_PENDING
```

promotion count가 0이면 `FULL_THESIS_SEED_PROMOTION_PASS`를 붙이지 않는다.

현재 canonical output:

```text
labels contains:
  FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS
  FULL_THESIS_SEED_PROMOTION_PENDING

labels does not contain:
  FULL_THESIS_SEED_PROMOTION_PASS
```

### 2.2 goal requirement matrix

`_goal_requirement_matrix_audit()`에 별도 required gate를 추가했다.

```text
gate_id = FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS
status = PASS

gate_id = FULL_THESIS_SEED_PROMOTION_PASS
status = PENDING
blocker = full_thesis_seed_promotion_pass_false
```

현재 canonical output:

```text
required_goal_completion_pass_count = 13
required_goal_completion_pending_count = 6
required_goal_completion_fail_count = 0

pending_gate_ids:
  FULL_THESIS_SMOKE_PASS
  FULL_THESIS_PRODUCTION_PASS
  FULL_THESIS_SEED_PROMOTION_PASS
  BRAIN_WEB_EVIDENCE_PASS
  ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
  FULL_TEST_ARTIFACT_PASS
```

중요:

```text
FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS는 pending이 아니다.
FULL_THESIS_SEED_PROMOTION_PASS는 pending이다.
```

### 2.3 goal completion audit

`_goal_completion_audit()`에 별도 blocker를 추가했다.

```text
full_thesis_seed_materialization_audit_pass_allowed = true
full_thesis_seed_promotion_pass_allowed = false
blockers contains full_thesis_seed_promotion_pass_false
```

현재 canonical blockers:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_production_pass_false
full_thesis_seed_promotion_pass_false
source_backed_replay_parity_all_archetypes_pending
machine_readable_test_result_artifact_missing
goal_requirement_matrix_pass_false
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

해석:

```text
anti-fake leaf 기준으로는 통과다.
하지만 target_gate=anti_fake였기 때문에 운영 완료를 뜻하지 않는다.
```

쉬운 예:

```text
장부 위조 여부 검사는 통과했다.
하지만 실제 영업 준비 완료 검사는 아직 통과하지 못했다.
```

## 4. Stage 존재 여부 교차검증

`leaf_artifact_audit.json` 기준:

```text
eligible_symbol_count = 3391
stage_status_count = 3391
event_board_non_stage0_count = 85

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391

operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE = 3391

full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
full_e2r_verified_score_present_count = 0
```

현재 상태판 Stage 분포:

```text
Stage0 = 3306
Stage1 = 54
Stage2-Watch = 30
Red = 1
```

현재 status 분포:

```text
FINAL = 36
NO_CURRENT_CATALYST = 3306
PENDING_MATERIAL_GAPS = 30
RISK_REVIEW = 1
SOURCE_PENDING = 18
```

이 숫자의 올바른 해석:

```text
Stage1 / Stage2-Watch / Red가 일부 있다.
하지만 이것은 CensusEvent 기반 상태판 Stage다.
FULL_THESIS 운영 Stage가 아니다.
```

나쁜 해석:

```text
Stage1이 54개 있으니 운영 파이프라인이 Stage를 냈다.
```

좋은 해석:

```text
54개는 상태판에서 official event watch 수준으로 표시된 것이다.
이 종목들이 FULL_THESIS StageCourt까지 통과했다는 뜻은 아니다.
```

## 5. Seed materialization 교차검증

`full_thesis_seed_materialization_audit.json` 기준:

```text
verdict = PASS
seed_event_count = 85
trace_row_count = 85
status_counts = PLANNER_NOT_RUN 85
final_stage_scope_counts = CENSUS_EVENT_BOARD 85
full_thesis_promoted_seed_count = 0
critical_count = 0
```

`readiness_verdict.json` 기준:

```text
full_thesis_seed_materialization_audit.verdict = PASS
full_thesis_seed_materialization_audit.status_counts = PLANNER_NOT_RUN 85
full_thesis_seed_materialization_audit.full_thesis_promoted_seed_count = 0
full_thesis_seed_materialization_audit.full_thesis_seed_promotion_pass = false

remaining_operational_gaps contains:
  full-thesis seed materialization audit shows no promoted FULL_THESIS seed
```

`self_repair_log.json` 기준:

```text
completion_eligible = true
unresolved_failures = []

deferred_goal_blockers contains:
  brain_web_evidence_pass_false
  full_thesis_smoke_pending
  full_thesis_production_pass_false
  full_thesis_seed_materialization_not_promoted
  source_backed_replay_parity_all_archetypes_pending
```

중요:

```text
self_repair completion_eligible = true
```

는 self-repair loop 자체가 감사 실패를 남기지 않았다는 뜻이다. goal completion이 true라는 뜻이 아니다.

## 6. Artifact hash

`artifact_manifest.json` 기준 최신 hash:

```text
acceptance_report.md
  byte_size = 7010
  sha256 = 7a5c48abaaf8901e86e0f2c0b23c90a20672dd02512c550978e1195e2490d4c4

full_thesis_seed_materialization_audit.json
  byte_size = 2007
  sha256 = 42d6a14baeb189701ab68d5eabe54d5d62e0c878cbc2d24e3464fbdd8b78d839

readiness_verdict.json
  byte_size = 9574
  sha256 = 3d5ba8dc3c43ffca89a023e261d689b347f28b0f50484fd66daa880a791e7c69

goal_completion_audit.json
  byte_size = 2744
  sha256 = 444d6ecb0705f43160013a0f7751b3750925eaae4b0306222d95a14830cc386c

goal_requirement_matrix_audit.json
  byte_size = 11956
  sha256 = d05126e75c637642e70e92295c1d9fb4e07c4b1ff6ec093ce939c2b1d1db83f9

self_repair_log.json
  byte_size = 4009
  sha256 = bf35b48f941d17b903592b76bda8835f51b418230cdcced1ca376fccf84dacef
```

## 7. 테스트

타깃 검증:

```text
PYTHONPATH=src python -m py_compile src/e2r/census/census_runner_v4.py

PYTHONPATH=src python -m unittest \
  tests.test_census_v4_goal_required_audits.CensusV4GoalRequiredAuditsTests.test_goal_required_runtime_audit_files_exist_and_pass_honesty_gates \
  tests.test_census_v4_brain_web_readiness_gate.CensusV4BrainWebReadinessGateTests.test_canonical_disabled_run_records_not_requested_not_pass \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_event_board_non_stage0_rows_are_queued_for_full_thesis_refresh_not_promoted -v

Ran 3 tests
OK
```

관련 audit suite:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_manifest_counts_match_report \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_goal_required_audits -v

Ran 94 tests in 38.236s
OK
```

전체 suite:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 5076 tests in 203.491s
OK
```

주의:

```text
전체 테스트는 통과했지만 goal_completion_audit의 FULL_TEST_ARTIFACT_PASS는 아직 pending이다.
이유는 canonical run에 machine-readable test result artifact를 넘긴 실행이 아니기 때문이다.

다음 단계에서 goal completion까지 닫으려면 run_test_command_with_artifact로 만든 JSON artifact를
canonical run의 --test-result-artifact로 넘겨야 한다.
```

## 8. 현재 남은 goal blockers

현재 `goal_completion_ready = false`다.

남은 blocker:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_production_pass_false
full_thesis_seed_promotion_pass_false
source_backed_replay_parity_all_archetypes_pending
machine_readable_test_result_artifact_missing
goal_requirement_matrix_pass_false
```

각 blocker 의미:

```text
brain_web_evidence_pass_false:
  real Brain/Web/LLM acquisition이 canonical disabled run에서 실행되지 않았다.

full_thesis_smoke_pending:
  canonical disabled run은 controlled smoke pass 실행이 아니다.

full_thesis_production_pass_false:
  production FULL_THESIS row가 없다.

full_thesis_seed_promotion_pass_false:
  85개 seed 중 production FULL_THESIS로 승격된 row가 0개다.

source_backed_replay_parity_all_archetypes_pending:
  모든 required archetype의 source-backed positive + guard replay가 닫히지 않았다.

machine_readable_test_result_artifact_missing:
  canonical run에 테스트 성적표 JSON이 연결되지 않았다.

goal_requirement_matrix_pass_false:
  위 pending gate들이 남아 있어 goal matrix 전체가 false다.
```

## 9. 다음 패치 방향

절대 하면 안 되는 패치:

```text
1. full_thesis_promoted_seed_count = 0인데 FULL_THESIS_SEED_PROMOTION_PASS를 붙이기
2. CENSUS_EVENT_BOARD Stage를 FULL_THESIS Stage처럼 복사하기
3. EVENT_WEIGHTED_PARTIAL score를 FULL_E2R_100 verified score로 승격하기
4. provider/source 실패를 낮은 점수나 Red로 확정하기
5. controlled smoke row를 production row로 세기
6. 감사 PASS를 운영 완료 PASS로 합치기
```

필요한 다음 구현:

```text
seed row
  -> real planner attempt
  -> bounded source task execution
  -> source-backed accepted claim
  -> primitive mapping
  -> score contribution
  -> StageCourt decision
  -> production FULL_THESIS promotion or explicit blocker
```

seed materialization status는 최소 아래처럼 전이되어야 한다.

```text
PLANNER_NOT_RUN
PLANNER_ATTEMPTED
SOURCE_TASK_EXECUTED
CLAIM_ACCEPTED
PRIMITIVE_MAPPED
SCORE_CONTRIBUTED
STAGECOURT_DECIDED
FULL_THESIS_PROMOTED
BLOCKED_MATERIAL_GAP
PROVIDER_PENDING
SOURCE_PENDING
```

중요한 운영 원칙:

```text
LLM은 다음에 무엇을 찾을지 판단하고, 문서에서 claim을 구조화한다.
코드는 source/date/entity/anchor/currentness/mapping을 검증하고 score/stage를 deterministic하게 계산한다.
```

쉬운 예:

```text
LLM:
  "이 공급계약은 금액과 기간은 보이지만 margin bridge가 없다. IR이나 분기보고서에서 매출 인식과 마진 영향을 찾아야 한다."

코드:
  그 query가 as_of_date를 넘지 않는지, source budget 안인지, source class가 admissible인지 검증하고 실행한다.
  원문 anchor가 없으면 score에 넣지 않는다.
```

## 10. 다음 에이전트 공격 질문

다음 리뷰어는 아래 질문으로 먼저 때리면 된다.

```text
1. FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS를 운영 완료로 해석하지 않았나?
2. FULL_THESIS_SEED_PROMOTION_PASS가 별도 required gate로 들어갔나?
3. 현재 `full_thesis_promoted_seed_count = 0`인데 goal completion이 true가 되지 않나?
4. readiness labels에 FULL_THESIS_SEED_PROMOTION_PENDING이 있고 PASS가 없는가?
5. goal matrix pending_gate_ids에 FULL_THESIS_SEED_PROMOTION_PASS가 있는가?
6. goal completion blockers에 full_thesis_seed_promotion_pass_false가 있는가?
7. self_repair completion_eligible을 goal completion으로 착각하지 않았나?
8. controlled smoke FULL_THESIS row를 production seed materialization으로 세지 않았나?
9. Stage1/Stage2-Watch/Red 상태판 row를 FULL_THESIS Stage로 세지 않았나?
10. full_e2r_verified_score_row_count가 0인데 점수 완성이라고 말하지 않았나?
11. machine-readable full test artifact 없이 FULL_TEST_ARTIFACT_PASS를 닫지 않았나?
12. Brain/Web disabled canonical run을 Brain/Web evidence pass로 착각하지 않았나?
13. source-backed replay parity가 전 아키타입에서 닫혔다고 과장하지 않았나?
14. provider/source 실패를 낮은 점수 확정으로 바꾸지 않았나?
15. seed를 실행하지 않았는데 score contribution이나 StageCourt decision을 만든 흔적이 없나?
```

## 11. 최종 판단

v50 이후 현재 상태는 더 솔직해졌다.

```text
감사표는 정상이다.
상태판 Stage는 있다.
85개 full-thesis refresh seed도 있다.
하지만 production FULL_THESIS Stage는 아직 0개다.
FULL_E2R_100 verified score도 아직 0개다.
```

따라서 다음 목표는 새 gate를 억지로 통과시키는 것이 아니다.

```text
85개 seed를 실제 운영 경로로 하나씩 materialize하고,
각 seed가 promoted / blocked / pending 중 어디서 멈췄는지
source-backed claim chain으로 증명하는 것이다.
```

이 문서의 현재 판정:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS:
  PASS

FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS:
  PASS

FULL_THESIS_SEED_PROMOTION_PASS:
  PENDING

FULL_THESIS_PRODUCTION_PASS:
  PENDING

BRAIN_WEB_EVIDENCE_PASS:
  PENDING

ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS:
  PENDING

Goal completion:
  FALSE
```

# Census v4 0701 v49 Seed Materialization Audit Readiness Goal Gate Link

작성일: 2026-07-03 KST

최신 주의:

```text
이 문서는 v49 시점의 연결 패치 기록이다.
최신 canonical hash와 goal gate 해석은 v50 문서를 우선한다.

v50에서 FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS와
FULL_THESIS_SEED_PROMOTION_PASS를 분리했다.

따라서 이 문서의 "seed materialization audit PASS"를
"production FULL_THESIS seed 승격 완료"로 읽으면 안 된다.
```

## 0. 결론

v48에서 만든 `full_thesis_seed_materialization_audit.json`을 이제 단순 leaf가 아니라 readiness와 goal completion 판단에 연결했다.

핵심 변화:

```text
readiness_verdict.json
  -> full_thesis_seed_materialization_audit 요약 포함
  -> FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS label 포함
  -> promoted FULL_THESIS seed가 없으면 remaining_operational_gaps에 명시

goal_requirement_matrix_audit.json
  -> FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS gate 추가

goal_completion_audit.json
  -> full_thesis_seed_materialization_audit_pass_allowed 포함
  -> full_thesis_seed_materialization_summary 포함
```

쉬운 예:

```text
전에는 검사표 파일은 있었지만 접수 데스크 화면에는 안 보였다.
이제 접수 데스크 화면에도 "진료 진행표 검증 PASS, 하지만 진단서 완료 0명"이라고 표시된다.
```

## 1. 왜 필요했나

v48까지는 다음 파일을 직접 열어야 seed materialization 상태를 알 수 있었다.

```text
full_thesis_seed_materialization_audit.json
full_thesis_seed_materialization_trace.jsonl
```

그런데 운영자는 보통 아래 파일을 먼저 본다.

```text
readiness_verdict.json
goal_completion_audit.json
goal_requirement_matrix_audit.json
```

따라서 seed audit이 이 세 파일에 연결되지 않으면, 다음 실수가 가능했다.

```text
anti-fake pass만 보고 운영 준비 완료처럼 오해
goal completion blocker에서 seed materialization 상태 누락
controlled smoke FULL_THESIS와 production seed materialization 혼동
```

## 2. controlled smoke 분리

이번 패치에서 중요한 보정이 하나 있었다.

`full_thesis_smoke_mode=controlled_replay`에서는 삼성전자/하이닉스 2개가 smoke용 `FULL_THESIS` row로 대체될 수 있다.

하지만 이것은 production seed materialization이 아니다.

따라서 seed audit은 controlled smoke 최종 scope를 이렇게 다룬다.

```text
final_stage_scope = FULL_THESIS
final_stage_scope_is_controlled_smoke = true
promoted_to_full_thesis = false
materialization_status = PLANNER_NOT_RUN
```

즉 controlled smoke는 경로 테스트이지 운영 seed 승격이 아니다.

쉬운 예:

```text
모의 진료 훈련에서 진단서를 써 봤다고 해서,
실제 접수 환자 85명이 진료 완료된 것은 아니다.
```

## 3. canonical rerun

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

## 4. canonical seed audit 상태

```text
seed_event_count = 85
trace_row_count = 85
status_counts = PLANNER_NOT_RUN 85
final_stage_scope_counts = CENSUS_EVENT_BOARD 85
full_thesis_promoted_seed_count = 0
critical_count = 0
verdict = PASS
```

해석:

```text
seed audit 자체는 정상이다.
하지만 promoted FULL_THESIS seed는 0개다.
따라서 운영 FULL_THESIS Stage는 아직 없다.
```

## 5. readiness 연결 결과

`readiness_verdict.json`에 추가된 의미:

```text
labels contains:
  FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS

full_thesis_seed_materialization_audit:
  verdict = PASS
  seed_event_count = 85
  trace_row_count = 85
  status_counts = PLANNER_NOT_RUN 85
  full_thesis_promoted_seed_count = 0
  critical_count = 0

remaining_operational_gaps contains:
  full-thesis seed materialization audit shows no promoted FULL_THESIS seed
```

중요:

```text
FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS
!= 운영 FULL_THESIS Stage pass

이 label은 "감사표가 정상"이라는 뜻이다.
"진단서가 완성됐다"는 뜻이 아니다.
```

## 6. goal gate 연결 결과

`goal_requirement_matrix_audit.json`에 추가된 gate:

```text
gate_id = FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS
status = PASS
required_for_goal_completion = true
```

이 gate는 아래를 보장한다.

```text
seed/trace count mismatch 없음
실행 전 score evidence 누수 없음
실행 전 stage promotion 누수 없음
source task / claim / StageCourt 순서 위반 없음
잘못된 FULL_THESIS_PROMOTED 없음
```

하지만 아직 아래 gate들은 pending이다.

```text
FULL_THESIS_PRODUCTION_PASS
BRAIN_WEB_EVIDENCE_PASS
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
FULL_TEST_ARTIFACT_PASS
```

## 7. goal completion 연결 결과

`goal_completion_audit.json`에 추가된 요약:

```text
full_thesis_seed_materialization_audit_pass_allowed = true

full_thesis_seed_materialization_summary:
  verdict = PASS
  seed_event_count = 85
  trace_row_count = 85
  status_counts = PLANNER_NOT_RUN 85
  full_thesis_promoted_seed_count = 0
  critical_count = 0
```

현재 goal completion은 여전히 false다.

대표 blocker:

```text
brain_web_evidence_pass_false
full_thesis_production_pass_false
source_backed_replay_parity_all_archetypes_pending
machine_readable_test_result_artifact_missing
goal_requirement_matrix_pass_false
```

## 8. manifest 변경

새 canonical hash:

```text
full_thesis_seed_materialization_audit.json
  byte_size = 2007
  sha256 = 42d6a14baeb189701ab68d5eabe54d5d62e0c878cbc2d24e3464fbdd8b78d839

readiness_verdict.json
  byte_size = 9486
  sha256 = 8824cc423dbc472348be61607f680bceb7a46b2f7988b5d59cf1d2dee353457b

goal_completion_audit.json
  byte_size = 2606
  sha256 = 6158e6c41d5799e3d95a0687a14f853d31906054859ab2cac8f3c527f4cf6f59

goal_requirement_matrix_audit.json
  byte_size = 11354
  sha256 = 79eccc2fc8aefd0e4507c9b7291a4779f44e8a27f2a8fe52284cd00aebb7fa5a
```

## 9. 테스트

타깃 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_goal_required_audits.CensusV4GoalRequiredAuditsTests.test_goal_required_runtime_audit_files_exist_and_pass_honesty_gates \
  tests.test_census_v4_brain_web_readiness_gate.CensusV4BrainWebReadinessGateTests.test_canonical_disabled_run_records_not_requested_not_pass \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_event_board_non_stage0_rows_are_queued_for_full_thesis_refresh_not_promoted -v

Ran 3 tests in 7.380s
OK
```

관련 감사 suite:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_manifest_counts_match_report \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_goal_required_audits -v

Ran 94 tests in 36.828s
OK
```

전체 unittest:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 5076 tests in 200.894s
OK
```

## 10. 다음 패치 방향

현재는 이렇게 닫혔다.

```text
seed materialization trace/audit visibility:
  PASS

seed materialization readiness/goal gate:
  PASS

actual production seed materialization:
  NOT READY
```

다음 패치는 실제 경로를 진전시켜야 한다.

```text
full thesis seed
  -> real planner success
  -> bounded official-first source task
  -> fetched document + anchor
  -> accepted score-eligible claim
  -> primitive mapping
  -> score contribution
  -> StageCourt trace
  -> production FULL_THESIS promotion
```

현재 hard truth:

```text
상태판 Stage는 있다.
운영 FULL_THESIS Stage는 없다.
이번 패치는 그 미완료 상태가 readiness/goal 화면에서도 숨지 못하게 만든 것이다.
```

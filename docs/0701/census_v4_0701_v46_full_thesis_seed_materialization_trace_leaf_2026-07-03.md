# Census v4 0701 v46 Full Thesis Seed Materialization Trace Leaf

작성일: 2026-07-03 KST

## 0. 결론

v45까지는 seed materialization을 count로만 봤다.

v46은 한 단계 더 보강했다.

```text
full_thesis_seed_materialization_trace.jsonl
```

를 leaf artifact로 추가해서, full-thesis refresh seed 85개 각각이 어디서 멈췄는지 row 단위로 남긴다.

현재 canonical disabled run의 결론은 그대로다.

```text
상태판 Stage는 있다.
FULL_THESIS 운영 Stage는 없다.
```

하지만 이제 이 말이 seed별 trace로도 검증된다.

## 1. 왜 필요했나

이전 문서에는 아래 숫자가 있었다.

```text
full_thesis_seed_event_count = 85
full_thesis_seed_planner_run_count = 0
full_thesis_seed_source_task_execution_count = 0
full_thesis_seed_accepted_claim_count = 0
full_thesis_seed_stagecourt_trace_count = 0
```

이 숫자는 맞지만, 리뷰어가 다시 물을 수 있다.

```text
그럼 85개 seed 각각은 어디서 멈췄는데?
SK하이닉스 seed는 planner까지 갔나?
삼성제약 seed는 source task가 있었나?
```

v46은 이 질문에 row 단위로 답하게 만든다.

쉬운 예:

```text
전에는 병원 접수자 85명과 "진료 완료 0명"이라는 합계만 있었다.

이제는 접수자별로:
  접수됨
  의사에게 배정됨
  검사 오더 있음
  검사 결과 있음
  진단서 있음
  최종 판정 있음
중 어디까지 갔는지 표가 생겼다.
```

## 2. 새 leaf artifact

추가 output:

```text
output/census_v4/2026-07-01/full_thesis_seed_materialization_trace.jsonl
docs/operational/census_mode_v4_full_thesis_seed_materialization_trace.jsonl
```

각 row 주요 필드:

```text
candidate_event_id
symbol
company_name
queue_task_id
seed_role
score_evidence_allowed
stage_promotion_allowed_before_execution
planner_run_ids
planner_run_count
planner_real_provider_success_count
source_task_ids
source_task_execution_count
accepted_claim_ids
accepted_claim_count
score_contribution_ids
score_contribution_count
stagecourt_trace_ids
stagecourt_trace_count
final_stage_scope
final_operator_stage_use
final_full_thesis_stage
final_score_scale
materialized_to_stagecourt
promoted_to_full_thesis
materialization_status
materialization_blockers
```

## 3. 상태값

현재 상태값은 아래처럼 단계별로 나눈다.

```text
PLANNER_NOT_RUN
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS
SOURCE_TASK_NOT_EXECUTED
ACCEPTED_CLAIM_NOT_CREATED
STAGECOURT_TRACE_NOT_CREATED
STAGECOURT_READY_NOT_PROMOTED
FULL_THESIS_PROMOTED
```

이렇게 나누는 이유:

```text
planner row가 있음
!= source task가 실행됨
!= accepted claim이 생김
!= StageCourt trace가 생김
!= FULL_THESIS row로 승격됨
```

## 4. canonical disabled rerun 결과

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

trace 직접 카운트:

```text
full_thesis_seed_materialization_trace rows = 85

materialization_status:
  PLANNER_NOT_RUN = 85

final_stage_scope:
  CENSUS_EVENT_BOARD = 85

planner_run_count sum = 0
source_task_execution_count sum = 0
accepted_claim_count sum = 0
stagecourt_trace_count sum = 0
```

첫 row 예:

```text
symbol = 000660
company_name = SK하이닉스
materialization_status = PLANNER_NOT_RUN
materialization_blockers = full_thesis_seed_has_no_planner_run
final_stage_scope = CENSUS_EVENT_BOARD
final_operator_stage_use = NOT_FULL_THESIS_STAGE
final_full_thesis_stage = FULL_THESIS_NOT_RUN
```

해석:

```text
SK하이닉스 full thesis refresh seed는 있다.
하지만 canonical disabled run에서는 planner도 안 돌았다.
따라서 C06/HBM 운영 Stage로 말하면 안 된다.
```

## 5. manifest 확인

`docs/operational/census_mode_v4_artifact_manifest.json`에 새 leaf가 들어갔다.

```text
name = full_thesis_seed_materialization_trace.jsonl
row_count = 85
byte_size = 89627
sha256 = 9f48ac0117dd6779adcbc965fe9b22ebacdefcc3807b38ccae94f3d62a27deb1
```

즉 다음 에이전트는 report 문구를 믿지 말고 이 leaf를 직접 세면 된다.

## 6. 테스트

타깃 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_event_board_non_stage0_rows_are_queued_for_full_thesis_refresh_not_promoted \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_enabled_provider_none_measures_seed_planner_consumption_without_materialization \
  tests.test_census_v4_artifact_manifest.CensusV4ArtifactManifestTests.test_manifest_has_hash_size_and_row_count_for_every_leaf -v

Ran 3 tests in 11.369s
OK
```

관련 Census v4 / Research Brain 감사 suite:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_manifest_counts_match_report \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_goal_required_audits -v

Ran 93 tests in 40.287s
OK
```

전체 unittest:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 5075 tests in 214.423s
OK
```

## 7. 아직 안 된 것

v46도 운영 완료가 아니다.

현재 canonical trace는 전부:

```text
PLANNER_NOT_RUN
```

이다.

따라서 다음 패치는 아래 상태를 실제로 만들어야 한다.

```text
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS
  -> provider none/provider error일 때 정확히 보류

SOURCE_TASK_NOT_EXECUTED
  -> planner는 됐지만 source task가 안 생길 때 정확히 보류

ACCEPTED_CLAIM_NOT_CREATED
  -> source task는 했지만 Evidence OS claim이 없을 때 정확히 보류

STAGECOURT_TRACE_NOT_CREATED
  -> claim은 있지만 StageCourt trace가 없을 때 정확히 보류

STAGECOURT_READY_NOT_PROMOTED
  -> StageCourt trace는 있지만 green/full-thesis gate 때문에 승격 차단

FULL_THESIS_PROMOTED
  -> source-backed full thesis 조건을 실제로 모두 닫았을 때만 허용
```

## 8. 다음 패치 방향

다음 코드는 다음을 닫아야 한다.

```text
seed event
  -> real/frozen-live planner output
  -> bounded source task execution
  -> accepted claim
  -> score contribution
  -> StageCourt trace
  -> FULL_THESIS candidate audit
```

주의:

```text
seed trace가 생겼다는 이유로 운영 Stage가 생긴 것이 아니다.
PLANNER_NOT_RUN 85개가 더 정확히 보일 뿐이다.
```

## 9. 최종 판정

```text
v46 patch verdict:
  PASS for seed materialization trace visibility

operational FULL_THESIS verdict:
  NOT READY

current hard truth:
  상태판 Stage는 있다.
  FULL_THESIS 운영 Stage는 없다.
  이제 seed별로 어디서 멈췄는지는 leaf artifact로 추적 가능하다.
```

# Census v4 0701 v44 Full Thesis Seed Materialization Runtime Counts

작성일: 2026-07-03 KST

## 0. 결론

v43은 `full_thesis_refresh_queue` 85개를 Research Brain seed event로 넘기는 배선을 만들었다.

v44는 그 다음 약한 지점을 고쳤다.

```text
seed file이 있다
!= Research Brain이 실제로 seed를 planner 입력으로 소비했다
!= source task가 실행됐다
!= accepted claim이 생겼다
!= StageCourt trace가 생겼다
```

이제 readiness에는 아래가 분리되어 기록된다.

```text
full_thesis_seed_event_count
full_thesis_seed_consumed_by_research_brain
full_thesis_seed_planner_run_count
full_thesis_seed_real_provider_success_count
full_thesis_seed_source_task_execution_count
full_thesis_seed_accepted_claim_count
full_thesis_seed_stagecourt_trace_count
full_thesis_seed_materialized_to_stagecourt
```

쉬운 예:

```text
접수표 85명 있음:
  full_thesis_seed_event_count = 85

의사가 접수표에서 실제로 환자를 봄:
  full_thesis_seed_real_provider_success_count > 0
  그때만 full_thesis_seed_consumed_by_research_brain = true

접수 시스템에 예약 row만 생김:
  full_thesis_seed_planner_run_count > 0
  full_thesis_seed_real_provider_success_count = 0
  full_thesis_seed_consumed_by_research_brain = false

검사 오더가 실행됨:
  full_thesis_seed_source_task_execution_count > 0

검사 결과로 진단서 근거가 생김:
  full_thesis_seed_accepted_claim_count > 0

진단서가 최종 판정으로 이어짐:
  full_thesis_seed_stagecourt_trace_count > 0
```

## 1. 왜 패치했나

v43 직후에는 enabled path에서 아래처럼 보일 수 있었다.
이 줄은 현재 기준값이 아니라 `OLD WRONG pre-v44 behavior` 설명이다.

```text
OLD WRONG pre-v44 behavior:
full_thesis_seed_consumed_by_research_brain = full_thesis_seed_event_count > 0
```

로 보일 수 있었다.

이건 너무 약하다.

```text
seed 파일을 만들었다
```

와

```text
planner_runs.jsonl 안에서 CensusFullThesisQueue event가 실제 처리됐다
```

는 다른 말이다.

v44는 `planner_runs.event.source_family == CensusFullThesisQueue`,
`event_type == full_thesis_refresh_seed`, 또는 `structured_payload.seed_role == planner_input_only`를 직접 세고,
그중 real-provider success가 있을 때만 consumed로 판정한다.

## 2. 코드 변경

수정:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_full_thesis_smoke_tasks.py
```

추가 helper:

```text
_full_thesis_seed_runtime_counts()
_planner_run_event_is_full_thesis_seed()
```

추가 audit fields:

```text
brain_web_attempt.full_thesis_seed_planner_run_count
brain_web_attempt.full_thesis_seed_real_provider_success_count
brain_web_attempt.full_thesis_seed_source_task_execution_count
brain_web_attempt.full_thesis_seed_accepted_claim_count
brain_web_attempt.full_thesis_seed_stagecourt_trace_count
brain_web_attempt.full_thesis_seed_materialized_to_stagecourt

brain_web_readiness_gate.full_thesis_seed_planner_run_count
brain_web_readiness_gate.full_thesis_seed_real_provider_success_count
brain_web_readiness_gate.full_thesis_seed_source_task_execution_count
brain_web_readiness_gate.full_thesis_seed_accepted_claim_count
brain_web_readiness_gate.full_thesis_seed_stagecourt_trace_count
brain_web_readiness_gate.full_thesis_seed_materialized_to_stagecourt
```

## 3. canonical disabled 재생성

명령:

```bash
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

canonical disabled 숫자:

```text
full_thesis_seed_event_count = 85
full_thesis_seed_consumed_by_research_brain = false
full_thesis_seed_planner_run_count = 0
full_thesis_seed_real_provider_success_count = 0
full_thesis_seed_source_task_execution_count = 0
full_thesis_seed_accepted_claim_count = 0
full_thesis_seed_stagecourt_trace_count = 0
full_thesis_seed_materialized_to_stagecourt = false
```

해석:

```text
canonical ledger-refresh run은 seed를 생성하지만 Brain/Web이 disabled다.
따라서 seed는 아직 소비되지 않았다.
이 run은 Brain/Web pass가 아니다.
```

## 4. enabled provider-none wiring smoke

점수/Stage를 만들지 않고 배선만 보기 위한 smoke:

```text
brain_web_mode = enabled
brain_planner_provider = none
brain_universe_limit = 2
brain_planner_success_limit = 1
brain_planner_batch_size = 1
write_operational_docs = false
fail_on_critical_audit = false
```

결과:

```text
full_thesis_seed_event_count = 85
full_thesis_seed_consumed_by_research_brain = false
full_thesis_seed_planner_run_count = 2
full_thesis_seed_real_provider_success_count = 0
full_thesis_seed_source_task_execution_count = 0
full_thesis_seed_accepted_claim_count = 0
full_thesis_seed_stagecourt_trace_count = 0
full_thesis_seed_materialized_to_stagecourt = false
planner_run_count = 21
source_task_execution_count = 0
accepted_claim_count = 0
brain_web_readiness_gate.verdict = BLOCKED
brain_web_readiness_gate.blockers includes
  full-thesis seed planner runs have no real-provider success
```

해석:

```text
Research Brain planner queue에는 seed pending row가 생긴다.
하지만 provider none이라 실제 LLM/Research Brain 소비는 아니다.
따라서 source task/claim/StageCourt도 생기지 않는다.
그러므로 BLOCKED가 맞다.
```

이 blocker는 중요하다.

```text
일반 Brain/Web이 막혔다
```

가 아니라,

```text
full-thesis queue seed는 pending planner row까지만 생겼고 real-provider success가 없었다
```

를 바로 보여준다.

## 5. 테스트

타깃:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_event_board_non_stage0_rows_are_queued_for_full_thesis_refresh_not_promoted -v

OK
```

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_enabled_provider_none_measures_seed_planner_consumption_without_materialization -v

OK
```

관련 묶음:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_manifest_counts_match_report -v

Ran 93 tests in 36.941s
OK
```

전체 suite:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 5075 tests in 205.207s
OK
```

## 6. 아직 안 된 것

이번 패치도 운영 완료가 아니다.

아직 0인 것:

```text
full_thesis_seed_source_task_execution_count = 0
full_thesis_seed_accepted_claim_count = 0
full_thesis_seed_stagecourt_trace_count = 0
full_thesis_seed_materialized_to_stagecourt = false
```

즉 현재는:

```text
queue -> seed -> planner input
```

까지 더 정직하게 증명했고,

```text
planner -> source task -> Evidence OS accepted claim -> score contribution -> StageCourt trace -> FULL_THESIS row
```

는 아직 닫지 못했다.

## 7. 다음 패치 방향

v45에서 할 일:

```text
1. real/frozen-live provider path에서 seed planner output이 source task를 생성하는지 확인한다.
2. seed source task execution이 source_task_executions.jsonl에 candidate_event_id와 함께 남는지 확인한다.
3. accepted claim이 생긴 seed만 StageCourt trace로 이어지는지 확인한다.
4. source task/claim/stage trace 중 하나라도 비면 FULL_THESIS로 승격하지 않는다.
5. provider failure면 낮은 점수 확정이 아니라 ProviderPending/BLOCKED로 남긴다.
```

절대 하면 안 되는 것:

```text
seed_planner_run_count > 0 이라는 이유로 FULL_THESIS 승격
source_task_execution_count = 0인데 materialized 처리
accepted_claim_count = 0인데 StageCourt trace가 있다고 주장
provider none 결과를 Brain/Web evidence pass로 해석
```

## 8. 최종 판정

```text
v44 patch verdict:
  PASS for seed runtime-count honesty

operational FULL_THESIS verdict:
  NOT READY

Brain/Web evidence verdict:
  canonical disabled = NOT_REQUESTED
  enabled provider-none smoke = BLOCKED

current hard truth:
  상태판 Stage는 있다.
  FULL_THESIS 운영 Stage는 아직 없다.
  seed는 planner 입력까지는 갈 수 있지만, source task 이후 full chain은 아직 0이다.
```

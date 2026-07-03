# Census v4 0701 v48 Full Thesis Seed Materialization Audit Leaf

작성일: 2026-07-03 KST

## 0. 결론

v48은 v46/v47의 seed trace를 한 단계 더 잠갔다.

새 artifact:

```text
full_thesis_seed_materialization_audit.json
```

이 audit은 아래를 기계적으로 검증한다.

```text
seed row 수와 trace row 수가 같은가
seed가 실행 전 점수/Stage 증거로 새지 않았는가
planner/source/claim/StageCourt/FULL_THESIS 단계가 순서대로 닫혔는가
FULL_THESIS_PROMOTED라고 적힌 row가 실제 StageCourt와 FULL_E2R_100 score scale을 갖는가
```

현재 canonical run의 결론은 바뀌지 않았다.

```text
상태판 Stage는 있다.
운영 FULL_THESIS Stage는 없다.
seed 85개는 모두 PLANNER_NOT_RUN이다.
```

쉬운 예:

```text
v46은 접수자 85명 각각의 "진료 진행표"를 만들었다.
v48은 그 진행표를 다시 세서 "의사 진료 전인데 진단서로 둔갑한 사람이 없는지" 검사하는 감사표를 추가했다.
```

## 1. 코드 패치

수정 파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/census/census_v4_auditor.py
tests/test_census_v4_full_thesis_smoke_tasks.py
tests/test_census_v4_artifact_manifest.py
```

핵심 변경:

```text
_write_full_thesis_seed_materialization_trace()
  -> full_thesis_seed_materialization_trace.jsonl 작성
  -> full_thesis_seed_materialization_audit.json 작성

_full_thesis_seed_materialization_audit()
  -> trace 상태 분포
  -> critical count
  -> 다음 조치 매핑
  -> operator rule
```

새 audit가 잡는 critical 항목:

```text
seed_trace_count_mismatch_count
score_evidence_allowed_before_execution_count
stage_promotion_allowed_before_execution_count
source_task_before_real_provider_success_count
accepted_claim_without_source_task_count
stagecourt_without_accepted_claim_count
full_thesis_promoted_missing_stagecourt_count
full_thesis_promoted_missing_full_e2r_score_count
full_thesis_scope_without_promoted_status_count
```

## 2. canonical rerun

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

## 3. 새 audit 직접 카운트

파일:

```text
output/census_v4/2026-07-01/full_thesis_seed_materialization_audit.json
docs/operational/census_mode_v4_full_thesis_seed_materialization_audit.json
```

결과:

```text
seed_event_count = 85
trace_row_count = 85

status_counts:
  PLANNER_NOT_RUN = 85

final_stage_scope_counts:
  CENSUS_EVENT_BOARD = 85

planner_run_seed_count = 0
real_provider_success_seed_count = 0
source_task_execution_seed_count = 0
accepted_claim_seed_count = 0
stagecourt_trace_seed_count = 0
full_thesis_promoted_seed_count = 0

critical_count = 0
verdict = PASS
```

해석:

```text
seed는 85개 있다.
하지만 canonical disabled run에서는 planner도 source task도 accepted claim도 StageCourt도 없다.
그러므로 FULL_THESIS로 말하면 안 된다.
```

## 4. manifest 확인

새 manifest row:

```text
name = full_thesis_seed_materialization_audit.json
row_count = null
byte_size = 2007
sha256 = 42d6a14baeb189701ab68d5eabe54d5d62e0c878cbc2d24e3464fbdd8b78d839
```

기존 trace row:

```text
name = full_thesis_seed_materialization_trace.jsonl
row_count = 85
byte_size = 89627
sha256 = 9f48ac0117dd6779adcbc965fe9b22ebacdefcc3807b38ccae94f3d62a27deb1
```

## 5. 상태 전이 테스트

새 테스트는 아래 모든 상태를 하나씩 만든다.

```text
PLANNER_NOT_RUN
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS
SOURCE_TASK_NOT_EXECUTED
ACCEPTED_CLAIM_NOT_CREATED
STAGECOURT_TRACE_NOT_CREATED
STAGECOURT_READY_NOT_PROMOTED
FULL_THESIS_PROMOTED
```

목적:

```text
나중에 실제 live run에서 어느 단계까지 도달하든
trace와 audit이 그 상태를 정확히 표현해야 한다.
```

쉬운 예:

```text
검사실에 갔는지, 검사 결과가 나왔는지, 의사가 진단서를 썼는지, 최종 확정했는지를
모두 같은 "진료 완료"로 뭉개지 않고 단계별로 적는 것이다.
```

## 6. 테스트

타깃 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_seed_materialization_trace_and_audit_cover_all_runtime_statuses \
  tests.test_census_v4_full_thesis_smoke_tasks.CensusV4FullThesisSmokeTaskTests.test_event_board_non_stage0_rows_are_queued_for_full_thesis_refresh_not_promoted \
  tests.test_census_v4_artifact_manifest.CensusV4ArtifactManifestTests.test_manifest_has_hash_size_and_row_count_for_every_leaf -v

Ran 3 tests in 7.100s
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

Ran 94 tests in 37.769s
OK
```

전체 unittest:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 5076 tests in 209.671s
OK
```

## 7. 다음 패치 방향

v48은 아직 운영 FULL_THESIS를 만들지 않는다.

다음 패치가 실제로 닫아야 할 경로:

```text
full thesis seed
  -> real planner success
  -> bounded official-first source task
  -> fetched document + anchor
  -> accepted score-eligible claim
  -> primitive mapping
  -> score contribution
  -> StageCourt trace
  -> FULL_THESIS promotion
```

현재 canonical은 첫 단계에서 멈춘다.

```text
full thesis seed
  -> PLANNER_NOT_RUN
```

따라서 다음 에이전트가 공격해야 할 질문은 이것이다.

```text
1. 실제 run에서 PLANNER_NOT_RUN이 아닌 seed가 생겼는가?
2. real provider success 없이 source task가 생기지는 않았는가?
3. source task 없이 accepted claim이 생기지는 않았는가?
4. accepted claim 없이 StageCourt가 생기지는 않았는가?
5. FULL_THESIS_PROMOTED라면 stage_scope=FULL_THESIS, score_scale=FULL_E2R_100인가?
6. 이 모든 것이 manifest와 docs/operational에도 같은 hash/count로 남았는가?
```

## 8. 최종 판정

```text
v48 patch verdict:
  PASS for seed materialization audit visibility

operational FULL_THESIS verdict:
  NOT READY

current hard truth:
  상태판 Stage는 있다.
  운영 FULL_THESIS Stage는 없다.
  seed별 진행 상태와 그 aggregate audit은 이제 모두 leaf artifact로 검증 가능하다.
```

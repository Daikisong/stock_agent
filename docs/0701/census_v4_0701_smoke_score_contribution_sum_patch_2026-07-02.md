# Census v4 0701 Smoke Score Contribution Sum Patch

작성 시점: 2026-07-02 KST

이 문서는 `census_v4_0701_controlled_smoke_production_split_patch_2026-07-02.md` 이후 추가 패치 결과를 고정한다.

후속 업데이트:

```text
이 문서 작성 후 all-archetype replay matrix 패치가 추가됐다.
최신 단일 진실은 아래 문서를 우선한다.

docs/0701/census_v4_0701_all_archetype_replay_matrix_patch_2026-07-02.md

변경:
  all_archetype_replay_matrix.json 추가
  C01~C32 + R13 guard 계약 36개 전부 matrix에 표시
  controlled smoke output 기준 C06만 source_backed_ready_count=1
  all_archetype_replay_pass는 여전히 false
  최신 전체 테스트 artifact는 4982개 OK
```

한 줄 결론:

> 삼성전자/하이닉스 controlled full-thesis smoke의 72/88점은 더 이상 `FULL_THESIS_SMOKE_SCORES` 총점 상수에서 오지 않는다. 각 primitive별 `ScoreContribution.raw_points` 합계가 `full_thesis_verified_score`, StageCourt score interval, AtomicStageDecision score로 들어간다.

쉬운 예:

```text
이전:
하이닉스 = 88점이라고 답안지 맨 위에 써둠

현재:
고객/qualification/capacity/revenue/cash/repeat/source_quorum 점수를 각각 더해서 88점
```

## 1. 코드 변경

변경 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_full_thesis_smoke_tasks.py
```

제거한 상수:

```text
FULL_THESIS_SMOKE_SCORES
FULL_THESIS_SMOKE_STAGES
```

새 계산 방식:

```text
fixture primitive
  -> accepted claim
  -> ScoreContribution.raw_points
  -> sum(raw_points)
  -> stagecourt_trace.score_interval
  -> AtomicStageDecision.full_e2r_verified_score
  -> CensusStageStatus.full_thesis_verified_score
```

Stage 결정도 종목명 상수가 아니라 아래 규칙으로 계산한다.

```text
score >= 90 and no missing_green_primitives -> Stage3-Green
score >= 80                                -> Stage3-Yellow
score >= 65                                -> Stage2-Watch
score > 0                                  -> Stage1
otherwise                                  -> Stage0
```

## 2. 검산 결과

산출물:

```text
output/test_census_v4_verified_full_tests_smoke
```

삼성전자:

```text
symbol = 005930
full_thesis_verified_score = 72.0
sum(score_contributions.raw_points) = 72.0
base_stage = Stage2-Watch
score_source = SCORE_CONTRIBUTION_SUM
score_build_method = primitive_score_contribution_sum

contributions:
  named_customer_or_customer_quality = 10.0
  qualification_status = 9.0
  capacity_allocation_or_pre_sold = 8.0
  hbm_shipment_or_revenue_mix = 12.0
  cash_or_revision_conversion = 12.0
  repeat_evidence_family = 11.0
  source_quorum = 10.0
```

SK하이닉스:

```text
symbol = 000660
full_thesis_verified_score = 88.0
sum(score_contributions.raw_points) = 88.0
base_stage = Stage3-Yellow
score_source = SCORE_CONTRIBUTION_SUM
score_build_method = primitive_score_contribution_sum

contributions:
  named_customer_or_customer_quality = 14.0
  qualification_status = 12.0
  capacity_allocation_or_pre_sold = 16.0
  hbm_shipment_or_revenue_mix = 14.0
  cash_or_revision_conversion = 12.0
  repeat_evidence_family = 10.0
  source_quorum = 10.0
```

중요:

```text
controlled smoke 점수 합산 경로가 닫혔다는 뜻이지,
production full thesis pass가 됐다는 뜻은 아니다.
```

## 3. 테스트

Targeted:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_score_field_split \
  tests.test_census_v4_stage_signal_split \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_manifest_counts_match_report \
  -v
```

결과:

```text
Ran 24 tests
OK
```

Census v4 suite:

```bash
PYTHONPATH=src python -m unittest $(printf '%s ' tests/test_census_v4_*.py | sed 's#/#.#g; s#.py##g') -v
```

결과:

```text
Ran 98 tests
OK
```

전체 repo:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v
```

결과:

```text
status = OK
test_count = 4982
failed_count = 0
error_count = 0
duration_seconds = 169.2521
log_sha256 = a6e1f673c5275c2b86e960042b8176e51a61708851c9081eedce103e6fa0b96d
```

## 4. 현재 최종 상태

기본 production-style output:

```text
output/test_census_v4_verified_full_tests
stage_scope_distribution = {"CENSUS_EVENT_BOARD": 3391}
score_scope_distribution = {"EVENT_WEIGHTED_PARTIAL": 67, "NO_SCORE": 3324}
verified_score_present_count = 0
full_e2r_verified_score_count = 0
full_thesis_smoke_pass = false
full_thesis_production_pass = false
meaningful_operational_stage_pass = false
```

Controlled smoke output:

```text
output/test_census_v4_verified_full_tests_smoke
stage_scope_distribution = {"CENSUS_EVENT_BOARD": 3389, "FULL_THESIS": 2}
score_scope_distribution = {"EVENT_WEIGHTED_PARTIAL": 65, "FULL_E2R_100": 2, "NO_SCORE": 3324}
verified_score_present_count = 2
full_e2r_verified_score_count = 2
full_thesis_smoke_pass = true
full_thesis_production_pass = false
meaningful_operational_stage_pass = false
```

남은 핵심 blocker:

```text
brain_web_evidence_pass = false
all_archetype_replay_pass = false
full_thesis_production_pass = false
goal_completion_ready = false

goal completion blocker에는 `full_thesis_production_pass_false`가 별도로 남는다.
controlled smoke 통과는 production full thesis pass가 아니다.
후속 패치로 `full_thesis_production_audit.json`도 추가되어 이 구분이 leaf artifact로 남는다.
```

## 5. 다음 공격 지점

다음 에이전트는 아래를 먼저 봐야 한다.

```text
1. primitive별 smoke point가 EvidenceContract rubric으로 더 일반화되어 있는가?
   -> 아직 controlled fixture rubric point다. production proof는 아니다.

2. all_archetype_replay_matrix.json이 있는가?
   -> 후속 패치 후 있다. 단 pass는 false다.

3. Brain/Web enabled run이 real acquisition accepted claim까지 닫혔는가?
   -> 아직 아니다.

4. full_thesis_production_pass가 true가 되는 경로가 있는가?
   -> 아직 없다.
```

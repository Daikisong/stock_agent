# Census v4 Goal Requirement Matrix Audit Patch

> 최신 기준에서는 이 문서가 부분 superseded됐다. 현재 단일 진실은
> `census_v4_0701_latest_c06_source_backed_replay_stage_truth_and_next_patch_packet_2026-07-02.md`와
> `output/census_v4/2026-07-01/goal_requirement_matrix_audit.json`을 우선한다.
> 특히 `C06_GUARD_REPLAY_PASS`와 `FULL_TEST_ARTIFACT_PASS`는 최신 canonical output에서 pass이고,
> goal matrix는 17개 중 12 pass / 5 pending이다.

작성 시점: 2026-07-02 KST

## 결론

`goal.md`, `goal2.md`, `goal3.md`의 하드 게이트를 항목별 JSON matrix로 고정했다.

새 산출물:

```text
output/census_v4/2026-07-01/goal_requirement_matrix_audit.json
docs/operational/census_mode_v4_goal_requirement_matrix_audit.json
```

현재 결과:

```text
goal_completion_minimum_pass: false
meaningful_operational_stage_requirement_pass: false
brain_web_requirement_pass: false
production_full_thesis_requirement_pass: false

required_goal_completion_count: 17
required_goal_completion_pass_count: 11
required_goal_completion_pending_count: 6
required_goal_completion_fail_count: 0
```

대기 중인 gate:

```text
FULL_THESIS_SMOKE_PASS
FULL_THESIS_PRODUCTION_PASS
BRAIN_WEB_EVIDENCE_PASS
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
CONTROLLED_SEMANTIC_REPLAY_PASS
C06_GUARD_REPLAY_PASS
```

쉬운 예:

```text
이전:
  "goal_completion_ready=false"만 보고 어디가 부족한지 사람이 추적해야 했다.

이후:
  17개 체크박스 중 11개는 체크, 6개는 미체크라고 artifact가 직접 말한다.
```

## 왜 필요했나

이전 구조는 `goal_completion_audit.json`에 blockers가 있었지만, goal 문서의 요구사항 전체를 한 줄씩 검증하는 장부는 없었다.

그래서 다음 같은 착시가 남을 수 있었다.

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS니까 goal도 거의 끝난 것 아닌가?
full tests OK니까 운영 가능 아닌가?
controlled smoke가 있으니까 production full thesis도 된 것 아닌가?
```

이번 matrix는 그 착시를 막는다.

```text
anti-fake pass
!= goal completion pass

full tests pass
!= Brain/Web evidence pass

controlled smoke pass
!= production full thesis pass
```

## 코드 패치

수정 파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/census/census_v4_auditor.py
tests/test_census_v4_goal_required_audits.py
tests/test_census_v4_artifact_manifest.py
tests/test_census_v4_report_generated_from_leaf_audit.py
docs/0701/README.md
```

핵심 구현:

```text
_goal_requirement_matrix_audit(...)
```

이 함수는 다음을 행 단위로 평가한다.

```text
V3_FORENSIC_REVIEW_COMPLETE
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
ATOMIC_STAGE_DECISION_PASS
SCORE_SCALE_PASS
STAGE_SEMANTICS_PASS
SEMANTIC_PRIMITIVE_GUARD_PASS
SOURCE_TASK_SATISFACTION_PASS
LEDGER_REUSE_AND_SOURCE_COVERAGE_PASS
FULL_THESIS_SMOKE_PASS
FULL_THESIS_PRODUCTION_PASS
BRAIN_WEB_EVIDENCE_PASS
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
CONTROLLED_SEMANTIC_REPLAY_PASS
C06_GUARD_REPLAY_PASS
KNOWN_BAD_REGRESSION_PASS
SELF_REPAIR_LOOP_PASS
FULL_TEST_ARTIFACT_PASS
```

각 row는 다음 필드를 가진다.

```text
gate_id
title
required_for_goal_completion
status: PASS / PENDING / FAIL
blocker
evidence
```

## 생성 순서

leaf auditor가 필수 파일 존재를 검사하므로 파일 생성 순서가 중요했다.

현재 순서:

```text
1. pre-leaf goal_requirement_matrix_audit.json 작성
2. leaf_artifact_audit 실행
3. leaf 결과를 반영해 goal_requirement_matrix_audit.json 재작성
4. goal_completion_audit.json 재작성
5. readiness/acceptance/manifest 생성
```

이렇게 해야:

```text
leaf audit은 goal_requirement_matrix_audit.json 존재를 확인하고,
manifest는 최종 matrix hash를 기록한다.
```

## Acceptance report 노출

`acceptance_report.md`에 line `5e`를 추가했다.

현재 canonical output:

```text
5e. Goal requirement matrix:
  minimum_pass=False
  pass=11/17
  pending=6
  fail=0
```

`goal_completion_audit.json` blockers에도 다음이 추가됐다.

```text
goal_requirement_matrix_pass_false
```

즉 개별 blockers를 실수로 제거하더라도 matrix가 false면 goal completion이 될 수 없다.

## 최신 검증

Targeted:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_report_generated_from_leaf_audit -v

Ran 6 tests
OK
```

V4 suite:

```text
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v

Ran 111 tests
OK
```

Full suite:

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v

status: OK
test_count: 4992
failed_count: 0
error_count: 0
duration_seconds: 174.133
log_sha256: 60bb4c92382b9a66a097b74d1678a0624081ce98f1df5c400463c201a2a7424c
```

재생성한 output:

```text
output/test_census_v4_verified_full_tests
output/test_census_v4_verified_full_tests_smoke
output/census_v4/2026-07-01
docs/operational/census_mode_v4_*.*
```

## 현재 해석

현재는 다음 상태다.

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
but
goal_completion_minimum_pass=false
and
meaningful_operational_stage_requirement_pass=false
```

정확히 말하면:

```text
가짜 완료를 막는 장치와 상태판 audit은 많이 통과했다.
하지만 production full thesis, Brain/Web, all-archetype replay는 아직 대기다.
```

## 다음 패치 우선순위

다음에 할 일은 matrix의 pending 6개를 실제로 줄이는 것이다.

우선순위:

```text
1. FULL_THESIS_SMOKE_PASS를 canonical target에서 어떻게 다룰지 명확화
2. C06_GUARD_REPLAY_PASS를 source-backed semantic replay로 닫기
3. CONTROLLED_SEMANTIC_REPLAY_PASS의 pending 6개를 순차 source-backed replay로 닫기
4. BRAIN_WEB_EVIDENCE_PASS를 실제 production mode에서 planner/web/extractor/claim trace로 닫기
5. FULL_THESIS_PRODUCTION_PASS를 controlled smoke가 아닌 production rows로 닫기
6. ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS를 C01~C32 전체로 확장
```

절대 하면 안 되는 shortcut:

```text
controlled smoke를 production으로 인정
event-board Stage를 full thesis Stage로 인정
Brain/Web disabled run을 Brain/Web pass로 인정
source_proxy_only 연구자료를 운영 replay pass로 인정
```

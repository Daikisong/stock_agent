# Census v4 0701 v53 Controlled Smoke Operator Use Guard

작성일: 2026-07-03 KST

## 0. 최종 결론

v53에서는 controlled full-thesis smoke row가 production 운영 Stage처럼 보이는 혼선을 막았다.

이전 smoke run 문제:

```text
FULL_THESIS_SMOKE_PASS = true
controlled smoke row stage_scope = FULL_THESIS
operator_stage_use = FULL_THESIS_STAGE
operator_score_use = FULL_E2R_SCORE

하지만 full_thesis_production_audit:
  production_full_thesis_row_count = 0
```

이 상태는 다음 오해를 만든다.

```text
"production audit은 0개라는데,
 operator_stage_use는 FULL_THESIS_STAGE니까 운영 Stage가 있는 것 아닌가?"
```

v53 이후:

```text
controlled smoke row stage_scope = FULL_THESIS
operator_stage_use = SMOKE_ONLY_STAGE_NOT_PRODUCTION
operator_score_use = SMOKE_ONLY_SCORE_NOT_PRODUCTION
operator_scope_note = controlled_smoke_full_thesis_not_production
is_full_thesis_stage = false
is_full_e2r_score = false
is_controlled_smoke_full_thesis_stage = true
```

쉬운 예:

```text
모의 진단 테스트는 통과했다.
하지만 병원 운영 진단서로 발급된 것은 아니다.

그래서 "진단 로직은 작동한다"는 증거로는 쓰지만,
"실제 운영 Stage 확정"으로는 쓰지 않는다.
```

## 1. 왜 이 패치가 필요한가

`FULL_THESIS_SMOKE_PASS`는 삼성전자/하이닉스 C06/HBM full-thesis leaf path가
claim-backed score contribution과 StageCourt까지 닫힐 수 있는지 보는 smoke gate다.

하지만 이 smoke는 production run이 아니다.

```text
허용:
  C06/HBM full-thesis claim -> primitive -> score contribution -> StageCourt smoke path 검증

금지:
  이 smoke row를 production FULL_THESIS Stage로 운영 사용
```

기존 production audit은 controlled smoke row를 production row에서 제외했다.
하지만 row 자체의 operator alias가 production처럼 보였다.

```text
production_full_thesis_row_count = 0
controlled_smoke_full_thesis_row_count = 2

그런데 operator_stage_use = FULL_THESIS_STAGE
```

이건 감사 문서와 row 필드가 서로 다른 말을 하는 상태다.
v53은 row 필드까지 production 아님을 명시하게 고쳤다.

## 2. 코드 패치

핵심 변경 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_stage_signal_split.py
tests/test_census_v4_full_thesis_smoke_tasks.py
```

### 2.1 `_with_operator_scope_aliases()`

controlled smoke row를 감지한다.

```text
_is_controlled_smoke_full_thesis_stage(row) == true
```

조건:

```text
stage_scope == FULL_THESIS
score_source == SCORE_CONTRIBUTION_SUM
score_build_method == primitive_score_contribution_sum
full_thesis_source_task_ids 중 FTSMOKE-* 존재
```

이 경우 operator alias를 production alias로 만들지 않는다.

```text
operator_stage_use = SMOKE_ONLY_STAGE_NOT_PRODUCTION
operator_score_use = SMOKE_ONLY_SCORE_NOT_PRODUCTION
operator_scope_note = controlled_smoke_full_thesis_not_production
is_full_thesis_stage = false
is_full_e2r_score = false
is_controlled_smoke_full_thesis_stage = true
```

real production FULL_THESIS row는 그대로 유지한다.

```text
operator_stage_use = FULL_THESIS_STAGE
operator_score_use = FULL_E2R_SCORE
is_full_thesis_stage = true
is_full_e2r_score = true
```

### 2.2 테스트 보강

수정/보강한 테스트:

```text
tests.test_census_v4_stage_signal_split
tests.test_census_v4_full_thesis_smoke_tasks
tests.test_census_v4_brain_stage_promotion_gate
```

검증한 것:

```text
1. controlled smoke row 2개는 operator production alias를 쓰지 않는다.
2. smoke target gate는 여전히 명시적 smoke gate로만 PASS 가능하다.
3. real production fixture는 여전히 FULL_THESIS_STAGE / FULL_E2R_SCORE를 쓴다.
```

## 3. 검증 결과

### 3.1 관련 테스트

명령:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_stage_signal_split \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_brain_stage_promotion_gate \
  -v
```

결과:

```text
Ran 36 tests in 33.398s
OK
```

### 3.2 전체 테스트 artifact

명령:

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/census_v4/2026-07-01/full_unittest_result_artifact.json \
  --log output/census_v4/2026-07-01/full_unittest_result_artifact.log \
  -- python -m unittest discover -s tests -v
```

결과:

```text
schema_version = e2r_test_result_artifact_v1
command_string = python -m unittest discover -s tests -v
exit_code = 0
status = OK
test_count = 5077
failed_count = 0
error_count = 0
duration_seconds = 208.1238
log_sha256 = e719c2aa9d8248613ca82ef4eb02e3eab00924123ba80e7629f0b1d41b226620
```

## 4. canonical disabled run 재검증

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
  --fail-on-critical-audit true \
  --test-result-summary "full unittest artifact: Ran 5077 tests OK" \
  --test-result-artifact output/census_v4/2026-07-01/full_unittest_result_artifact.json
```

결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

canonical disabled run의 stage truth:

```text
stage_scope_distribution = {'CENSUS_EVENT_BOARD': 3391}
operator_stage_use_distribution = {'NOT_FULL_THESIS_STAGE': 3391}
operator_score_use_distribution = {'NOT_FULL_E2R_SCORE': 3391}
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
```

goal matrix:

```text
required_goal_completion_pass_count = 14
required_goal_completion_pending_count = 5
required_goal_completion_fail_count = 0

pending_gate_ids:
  FULL_THESIS_SMOKE_PASS
  FULL_THESIS_PRODUCTION_PASS
  FULL_THESIS_SEED_PROMOTION_PASS
  BRAIN_WEB_EVIDENCE_PASS
  ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
```

해석:

```text
기본 canonical run은 smoke를 켜지 않았으므로 FULL_THESIS row가 0개다.
이 상태가 daily ledger-refresh의 정직한 기본값이다.
```

## 5. explicit smoke run 재검증

명령:

```text
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-full-thesis-smoke-v52 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
  --full-thesis-smoke-mode controlled_replay \
  --target-gate full_thesis_smoke \
  --write-operational-docs false \
  --fail-on-critical-audit true \
  --test-result-summary "full unittest artifact: Ran 5077 tests OK" \
  --test-result-artifact output/census_v4/2026-07-01/full_unittest_result_artifact.json
```

결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
FULL_THESIS_SMOKE_PASS = true
```

smoke run stage truth:

```text
stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3389
  FULL_THESIS = 2

operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE = 3389
  SMOKE_ONLY_STAGE_NOT_PRODUCTION = 2

operator_score_use_distribution:
  NOT_FULL_E2R_SCORE = 3389
  SMOKE_ONLY_SCORE_NOT_PRODUCTION = 2

full_thesis_stage_row_count = 2
full_e2r_verified_score_row_count = 2
```

controlled smoke rows:

```text
SK하이닉스:
  full_thesis_stage = Stage3-Yellow
  full_e2r_verified_score = 88.0
  operator_stage_use = SMOKE_ONLY_STAGE_NOT_PRODUCTION
  operator_score_use = SMOKE_ONLY_SCORE_NOT_PRODUCTION
  is_full_thesis_stage = false
  is_full_e2r_score = false
  is_controlled_smoke_full_thesis_stage = true

삼성전자:
  full_thesis_stage = Stage2-Watch
  full_e2r_verified_score = 72.0
  operator_stage_use = SMOKE_ONLY_STAGE_NOT_PRODUCTION
  operator_score_use = SMOKE_ONLY_SCORE_NOT_PRODUCTION
  is_full_thesis_stage = false
  is_full_e2r_score = false
  is_controlled_smoke_full_thesis_stage = true
```

production audit:

```text
verdict = PENDING_FULL_THESIS_PRODUCTION
production_pass_allowed = false
production_mode_requested = false
controlled_smoke_full_thesis_row_count = 2
production_full_thesis_row_count = 0
blockers = ['production_full_thesis_not_requested_or_no_rows']
```

goal matrix in smoke run:

```text
required_goal_completion_pass_count = 15
required_goal_completion_pending_count = 4
required_goal_completion_fail_count = 0

pending_gate_ids:
  FULL_THESIS_PRODUCTION_PASS
  FULL_THESIS_SEED_PROMOTION_PASS
  BRAIN_WEB_EVIDENCE_PASS
  ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
```

해석:

```text
smoke gate는 통과한다.
하지만 production full-thesis gate는 통과하지 않는다.
```

## 6. 최신 hash

canonical disabled run:

```text
full_unittest_result_artifact.json
  byte_size = 624
  sha256 = e085b0c2ff6bb5f2d00ab4aaec6786d83dde1734de7afeed3f636e3e3723825d

full_unittest_result_artifact.log
  byte_size = 749433
  sha256 = e719c2aa9d8248613ca82ef4eb02e3eab00924123ba80e7629f0b1d41b226620

census_stage_summary.json
  byte_size = 2281
  sha256 = 9ff67f6dc7f006be793045a2ab93b779901873a9b19b091f819a9f1e809f20d0

test_result_evidence_audit.json
  byte_size = 1348
  sha256 = 75e823457a4a26dcc931add3688b8d5daf160c0c388cc20ee3b647d1c6df9469

artifact_manifest.json
  byte_size = 27895
  sha256 = 6c1ecbbbff956e61ff5499c8214834c4312b93a6624f2004dd656a5fce0a2dfa

acceptance_report.md
  byte_size = 6977
  sha256 = dc83a5eb2407b5e1fd0eb364645c98de289df02cca0ce3f4ed000619c7b25d1d
```

explicit smoke run:

```text
census_stage_summary.json
  byte_size = 2679
  sha256 = 98653f000ea805e442c868a9facd86e1de233e43a6ea1d0b1b78f74fa0998a57

samsung_hynix_full_thesis_smoke.json
  byte_size = 21655
  sha256 = 4ce328b8152d2353f1c27955c5b2f478748de073c64fec7adf22bc3ee95378f1

goal_requirement_matrix_audit.json
  byte_size = 12077
  sha256 = 8bad577a13aa6e42e2f2d860664e94f6f3e071a4ddcb27c725180c0fd1b1cde6

goal_completion_audit.json
  byte_size = 2612
  sha256 = 488360ed63c4afc12fd326008c75e388a615aba95071fe4c3755a1582be95f4d

full_thesis_production_audit.json
  byte_size = 1108
  sha256 = 0a42851c66701230283c20476ebe07d23cbd972a0d4da328df28625921d83c62

artifact_manifest.json
  byte_size = 28665
  sha256 = bc7bc38711727c4e5f1ab322512942b04f03c36d8c462746a2bb6ec9ba15bc76

acceptance_report.md
  byte_size = 7177
  sha256 = 4d54493bbbebf8e05ca797a5081b1709d895322557559327cec434bf200b3597
```

## 7. 다음 패치 방향

v53 이후 remaining blockers는 더 선명해졌다.

기본 canonical run:

```text
FULL_THESIS_SMOKE_PASS:
  pending, because smoke mode is disabled

FULL_THESIS_PRODUCTION_PASS:
  pending

FULL_THESIS_SEED_PROMOTION_PASS:
  pending

BRAIN_WEB_EVIDENCE_PASS:
  pending

ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS:
  pending
```

explicit smoke run:

```text
FULL_THESIS_SMOKE_PASS:
  pass

FULL_THESIS_PRODUCTION_PASS:
  pending

FULL_THESIS_SEED_PROMOTION_PASS:
  pending

BRAIN_WEB_EVIDENCE_PASS:
  pending

ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS:
  pending
```

다음 실제 운영 패치:

```text
1. Brain/Web enabled strict run에서 real planner/source/fetch/extractor/accepted claim/StageCourt path를 닫는다.
2. queue 85개 중 최소 하나를 production FULL_THESIS candidate로 materialize한다.
3. controlled smoke row를 production substitute로 쓰지 않는 현재 guard를 유지한다.
4. all-archetype source-backed replay parity를 C01~C36 전체로 확장한다.
```

## 8. 다음 에이전트 공격 포인트

다음 에이전트는 아래를 봐야 한다.

```text
1. controlled smoke row가 `operator_stage_use=FULL_THESIS_STAGE`로 되돌아가지 않았는가?
2. controlled smoke row가 `operator_score_use=FULL_E2R_SCORE`로 되돌아가지 않았는가?
3. real production fixture는 여전히 `FULL_THESIS_STAGE`로 승격 가능한가?
4. production audit이 controlled smoke를 production row로 세지 않는가?
5. goal matrix에서 smoke pass와 production pass가 분리되어 있는가?
6. canonical disabled run에서는 FULL_THESIS row가 여전히 0개인가?
7. explicit smoke run에서는 smoke-only operator alias가 정확히 2개인가?
```

## 9. 최종 판단

v53은 운영 production을 완성한 패치가 아니다.
하지만 smoke 검증과 운영 Stage를 더 정확히 분리했다.

한 문장:

```text
controlled smoke는 "로직 검사 통과"이지 "운영 진단서 발급"이 아니다.
```

현재 목표 상태:

```text
FULL_TEST_ARTIFACT_PASS:
  PASS

FULL_THESIS_SMOKE_PASS:
  explicit smoke run에서는 PASS
  canonical disabled run에서는 PENDING

FULL_THESIS_PRODUCTION_PASS:
  PENDING

FULL_THESIS_SEED_PROMOTION_PASS:
  PENDING

BRAIN_WEB_EVIDENCE_PASS:
  PENDING

ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS:
  PENDING
```

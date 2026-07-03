# Census v4 0701 Controlled Smoke / Production Split Patch

작성 시점: 2026-07-02 KST

이 문서는 `census_v4_0701_verified_stage_truth_and_next_agent_attack_packet_2026-07-02.md` 이후 추가 패치 결과를 고정한다.

후속 업데이트:

```text
이 문서 작성 후 smoke score-sum 패치와 all-archetype replay matrix 패치가 추가됐다.
최신 단일 진실은 아래 문서를 우선한다.

docs/0701/census_v4_0701_all_archetype_replay_matrix_patch_2026-07-02.md

변경:
  FULL_THESIS_SMOKE_SCORES / FULL_THESIS_SMOKE_STAGES 총점·Stage 상수 제거
  controlled smoke 점수는 ScoreContribution.raw_points 합산으로 계산
  score_source = SCORE_CONTRIBUTION_SUM
  score_build_method = primitive_score_contribution_sum
  all_archetype_replay_matrix.json 추가
  all_archetype_replay_pass는 여전히 false

최신 전체 테스트 artifact:
  output/test_full_repo_0701/full_unittest_result_artifact.json
  test_count = 4982
  status = OK
```

한 줄 결론:

> 삼성전자/하이닉스 C06/HBM full-thesis smoke는 이제 production 기본 실행에서 자동으로 붙지 않는다. 기본 실행은 `FULL_THESIS=0`이고, 명시적으로 `full_thesis_smoke_mode=controlled_replay`를 켠 별도 실행에서만 `FULL_THESIS=2`가 된다.

## 0. 교차검증 요약

이 문서는 아래 네 축을 서로 대조해서 작성했다.

```text
1. code/config:
   src/e2r/census/census_runner_v4.py
   src/e2r/cli/run_e2r_census_v4_until_pass.py

2. default production-style output:
   output/test_census_v4_verified_full_tests

3. explicit controlled smoke output:
   output/test_census_v4_verified_full_tests_smoke

4. machine-readable test artifact:
   output/test_full_repo_0701/full_unittest_result_artifact.json
```

검산표:

```text
기본 production-style 실행:
  full_thesis_smoke_mode = disabled
  stage_scope_distribution = {"CENSUS_EVENT_BOARD": 3391}
  score_scope_distribution = {"EVENT_WEIGHTED_PARTIAL": 67, "NO_SCORE": 3324}
  verified_score_present_count = 0
  full_e2r_verified_score_count = 0
  full_thesis_smoke_pass = false
  full_thesis_production_pass = false

명시 controlled smoke 실행:
  full_thesis_smoke_mode = controlled_replay
  stage_scope_distribution = {"CENSUS_EVENT_BOARD": 3389, "FULL_THESIS": 2}
  score_scope_distribution = {"EVENT_WEIGHTED_PARTIAL": 65, "FULL_E2R_100": 2, "NO_SCORE": 3324}
  verified_score_present_count = 2
  full_e2r_verified_score_count = 2
  full_thesis_smoke_pass = true
  full_thesis_production_pass = false

전체 테스트:
  status = OK
  test_count = 4982
  failed_count = 0
  error_count = 0
```

리뷰어가 가장 먼저 공격해야 할 지점:

```text
1. FULL_THESIS=2가 production 기본 실행에도 자동으로 붙는가?
   -> 현재는 아니어야 한다. 기본 실행에서는 0이어야 한다.

2. full_thesis_smoke_pass=true를 full_thesis_production_pass=true로 오해하는가?
   -> 현재는 아니어야 한다. production pass는 false다.

3. 72/88 smoke 점수가 ScoreContribution 합산인지, 상수인지?
   -> 후속 패치 후 ScoreContribution.raw_points 합산이다. 다만 controlled fixture rubric이므로 production proof는 아니다.

4. Brain/Web disabled run을 Brain/Web production pass로 과장하는가?
   -> 현재 brain_web_evidence_pass=false가 맞다.

5. all-archetype replay matrix 없이 goal_completion_ready가 true가 되는가?
   -> 현재 false가 맞다.
```

쉬운 예:

```text
이전:
차 시동만 걸었는데 시험장 주행까지 자동으로 기록됐다.

현재:
차 시동 = production/ledger-refresh 기본 실행
시험장 주행 = controlled smoke 명시 실행

두 기록을 서로 다른 버튼으로 분리했다.
```

## 1. 왜 패치했나

이 문서 작성 직전 상태의 가장 큰 위험은 이거였다.

```text
FULL_THESIS_SMOKE_SYMBOLS = ("005930", "000660")
FULL_THESIS_SMOKE_SCORES = {"005930": 72.0, "000660": 88.0}
FULL_THESIS_SMOKE_STAGES = {"005930": "Stage2-Watch", "000660": "Stage3-Yellow"}
```

이 controlled smoke는 leaf chain 검증용으로는 유용하지만, production 기본 실행에서 자동으로 붙으면 다음 오해가 생긴다.

```text
삼성/하이닉스 smoke pass
→ full thesis production pass
→ meaningful operational stage pass
```

이건 틀렸다.

따라서 이번 패치는 smoke를 production proof가 아니라 명시적 replay/smoke proof로 분리한다.

## 2. 코드 변경

변경 파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/cli/run_e2r_census_v4_until_pass.py
tests/census_v4_test_helpers.py
tests/test_census_v4_full_thesis_smoke_tasks.py
tests/test_census_v4_goal_required_audits.py
tests/test_census_v4_run_mode_honesty.py
```

핵심 변경:

```text
1. CensusV4RunConfig.full_thesis_smoke_mode 추가
   default = "disabled"

2. _apply_full_thesis_smoke_replay()
   full_thesis_smoke_mode != "controlled_replay"이면 stage row를 바꾸지 않고 pending 유지

3. CLI 옵션 추가
   --full-thesis-smoke-mode disabled|controlled_replay

4. CLI target gate 분리
   --target-gate full_thesis        -> production full thesis pass, 현재 false
   --target-gate full_thesis_smoke  -> controlled smoke pass

5. readiness_verdict에 full_thesis_production_pass 추가
   현재 항상 false

6. tests/census_v4_test_helpers.py는 controlled_replay를 명시 사용
   기존 smoke chain 테스트는 계속 가능

7. 새 테스트 추가
   default 실행에서는 FULL_THESIS row가 0이고 full_thesis_smoke_pending이 남는지 확인
```

## 3. 최신 테스트

Targeted:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_stage_signal_split \
  tests.test_census_v4_score_field_split \
  tests.test_census_v4_manifest_counts_match_report \
  -v
```

결과:

```text
Ran 38 tests
OK
```

Census v4 suite:

```bash
PYTHONPATH=src python -m unittest $(printf '%s ' tests/test_census_v4_*.py | sed 's#/#.#g; s#.py##g') -v
```

결과:

```text
Ran 96 tests
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
duration_seconds = 168.4677
log_sha256 = e34783bb9bed0192ecca1ee823c597bf1300557f45cd28c7d3dfc91f79c68134
```

## 4. 기본 production-style verified output

산출물:

```text
output/test_census_v4_verified_full_tests
```

검산에 사용한 핵심 파일:

```text
output/test_census_v4_verified_full_tests/census_stage_summary.json
output/test_census_v4_verified_full_tests/readiness_verdict.json
output/test_census_v4_verified_full_tests/goal_completion_audit.json
output/test_census_v4_verified_full_tests/samsung_hynix_full_thesis_smoke.json
output/test_census_v4_verified_full_tests/test_result_evidence_audit.json
```

실행 의미:

```text
full_thesis_smoke_mode = disabled
test_result_artifact = output/test_full_repo_0701/full_unittest_result_artifact.json
```

Stage scope:

```text
CENSUS_EVENT_BOARD = 3391
FULL_THESIS = 0
```

Score scope:

```text
EVENT_WEIGHTED_PARTIAL = 67
NO_SCORE = 3324
FULL_E2R_100 = 0
```

Canonical stage:

```text
0 = 3306
1 = 54
2 = 30
3-Red = 1
```

Readiness:

```text
verdict = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
brain_web_evidence_pass = false
full_thesis_smoke_pass = false
full_thesis_production_pass = false
all_archetype_replay_pass = false
meaningful_operational_stage_pass = false
```

Goal blockers:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
source_backed_replay_parity_all_archetypes_pending
```

해석:

```text
기본 실행은 이제 삼성/하이닉스 smoke를 자동으로 붙이지 않는다.
따라서 FULL_THESIS/FULL_E2R_100 row는 0개가 맞다.
```

## 5. Controlled smoke verified output

산출물:

```text
output/test_census_v4_verified_full_tests_smoke
```

검산에 사용한 핵심 파일:

```text
output/test_census_v4_verified_full_tests_smoke/census_stage_summary.json
output/test_census_v4_verified_full_tests_smoke/readiness_verdict.json
output/test_census_v4_verified_full_tests_smoke/goal_completion_audit.json
output/test_census_v4_verified_full_tests_smoke/samsung_hynix_full_thesis_smoke.json
output/test_census_v4_verified_full_tests_smoke/test_result_evidence_audit.json
```

실행 의미:

```text
full_thesis_smoke_mode = controlled_replay
test_result_artifact = output/test_full_repo_0701/full_unittest_result_artifact.json
```

Stage scope:

```text
CENSUS_EVENT_BOARD = 3389
FULL_THESIS = 2
```

Score scope:

```text
EVENT_WEIGHTED_PARTIAL = 65
FULL_E2R_100 = 2
NO_SCORE = 3324
```

Canonical stage:

```text
0 = 3306
1 = 52
2 = 31
3-Red = 1
3-Yellow = 1
```

Readiness:

```text
verdict = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
brain_web_evidence_pass = false
full_thesis_smoke_pass = true
full_thesis_production_pass = false
all_archetype_replay_pass = false
meaningful_operational_stage_pass = false
```

Goal blockers:

```text
brain_web_evidence_pass_false
source_backed_replay_parity_all_archetypes_pending
```

해석:

```text
controlled smoke는 leaf chain smoke로는 통과한다.
하지만 production full thesis pass는 여전히 false다.
```

## 6. CLI 의미 변경

이제 CLI target gate는 이렇게 읽어야 한다.

```text
--target-gate anti_fake
  anti-fake 상태판 통과 여부

--target-gate brain_web
  실제 Brain/Web evidence gate 통과 여부

--target-gate full_thesis
  production full thesis pass 여부
  현재는 false라 exit 1이 맞다.

--target-gate full_thesis_smoke
  controlled smoke pass 여부
  --full-thesis-smoke-mode controlled_replay를 같이 켠 경우에만 exit 0 가능

--target-gate meaningful
  Brain/Web + production full thesis + all-archetype replay까지 모두 통과해야 함
```

쉬운 예:

```text
full_thesis_smoke:
  시험장 코스 주행 성공

full_thesis:
  실제 도로 주행 운영 가능

meaningful:
  실제 도로 주행 + 전체 노선 검증 + 안전 감사까지 완료
```

## 7. 현재 최종 판정

인정 가능한 말:

```text
Census v4 anti-fake 상태판은 통과한다.
기본 실행에서 controlled smoke가 production row로 자동 유입되지 않는다.
명시 controlled smoke 실행에서는 삼성/하이닉스 C06/HBM leaf chain이 닫힌다.
전체 repo 4982개 테스트가 통과했다.
```

금지해야 할 말:

```text
FULL_THESIS_SMOKE_PASS가 production full thesis pass다.
target_gate=full_thesis가 smoke pass와 같다.
기본 production/ledger-refresh 실행에 FULL_THESIS row가 있다.
meaningful operational stage가 통과했다.
모든 아키타입 source-backed replay가 끝났다.
Brain/Web live acquisition이 production cutover됐다.
```

최종 상태:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS = true
CONTROLLED_FULL_THESIS_SMOKE_PASS = true only when explicitly enabled
FULL_THESIS_PRODUCTION_PASS = false
BRAIN_WEB_EVIDENCE_PASS = false
ALL_ARCHETYPE_REPLAY_PASS = false
MEANINGFUL_OPERATIONAL_STAGE_PASS = false
GOAL_COMPLETION_READY = false
```

다음 패치:

```text
1. Brain/Web enabled run의 real acquisition/claim promotion blocker 닫기
2. primitive별 controlled smoke rubric point를 EvidenceContract rubric으로 일반화
3. shared output root race 방지
4. SOURCE_GAP_PENDING 아키타입을 source-backed positive/guard replay로 채우기
```

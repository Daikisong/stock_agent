# Census v4 0701 C06 Guard Replay Patch

작성 시점: 2026-07-02 KST

> 최신 주의: 이 문서의 "controlled smoke 기준 C06 source-backed positive+guard ready" 표현은
> `census_v4_0701_external_reviewer_final_attack_packet_after_c06_overclaim_fix_2026-07-02.md` 이후 superseded됐다.
> 현재 C06은 `CONTROLLED_WIRING_SMOKE_ONLY_SEMANTIC_REPLAY_PENDING`이며,
> `controlled_wiring_smoke_ready_count=1`, `source_backed_ready_count=0`, `guard_replay_ready_count=0`이다.

한 줄 결론:

> C06/HBM controlled smoke는 이제 positive replay뿐 아니라 qualification-lag guard replay도 통과한다. 하지만 이것은 controlled replay 한 조각이고, production full thesis나 C01~C32 전체 parity는 여전히 아니다.

쉬운 예:

```text
이전:
C06은 좋은 사례만 통과했다.
하지만 삼성 qualification lag 같은 나쁜/혼합 사례를 4C로 오독하지 않는지는 matrix에 반영되지 않았다.

현재:
C06 positive 사례 2개와 guard 사례 3개가 같이 통과한다.
하지만 나머지 31개 required archetype은 아직 positive+guard replay가 없다.
```

## 1. 코드 변경

변경 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_all_archetype_replay_matrix.py
tests/test_census_v4_artifact_manifest.py
tests/test_census_v4_goal_required_audits.py
```

새 산출물:

```text
output/.../c06_guard_replay_audit.json
docs/operational/census_mode_v4_c06_guard_replay_audit.json
```

matrix 반영:

```text
C06 replay_status:
  SOURCE_BACKED_SMOKE_AND_GUARD_REPLAY_READY

C06 replay_scope:
  controlled_smoke_and_guard_only

C06:
  positive_replay_pass = true
  guard_replay_pass = true
  guard_case_count = 3
  guard_case_pass_count = 3
```

## 2. Guard fixture 의미

추가된 guard case:

```text
1. C06-GUARD-SAMSUNG-QUALIFICATION-LAG-NOT-4C
   삼성 HBM qualification lag는 current direct cancellation이 아니면 4C가 아니다.

2. C06-GUARD-SAMSUNG-PARTIAL-CLEARANCE-SUPERSEDES-ABSOLUTE-FAILURE
   일부 clearance/follow-up은 과거 absolute failure 서사를 약화시키지만, Green unlock 자체는 아니다.

3. C06-GUARD-SAMSUNG-SUPPLY-DELAY-NOT-GREEN-OR-4C
   Nvidia AI chip supply delay는 Green을 막는 watch 사유일 수 있지만, 그 자체로 hard 4C나 Green 증거가 아니다.
```

공통 원칙:

```text
score_contribution_ids = []
expected_current_score_eligible = false
expected_hard_break_allowed = false
expected_green_unlock_allowed = false
source_proxy_only = false
evidence_url_pending = false
```

즉 guard fixture는 점수를 올리거나 내리는 장치가 아니다.

```text
나쁜 해석:
삼성 HBM lag 기사 발견 -> hard break -> 4C

정확한 해석:
삼성 HBM lag 기사 발견 -> 현재 direct cancellation인지 후속 확인 필요
-> 현재 점수에는 직접 반영하지 않음
-> Green unlock도 아님
-> watch/follow-up context
```

## 3. 최신 검산값

기본 production-style:

```text
output/test_census_v4_verified_full_tests
output/census_v4/2026-07-01

FULL_THESIS = 0
source_backed_ready_count = 0
guard_replay_ready_count = 0
missing_required_archetype_count = 32
c06_guard_replay_pass_allowed = false
c06_guard_replay_status = C06_GUARD_REPLAY_PENDING
```

기본 output에서 C06 guard가 false인 이유:

```text
positive_replay_ready = false
blockers = ["c06_positive_replay_required_before_guard_pass"]
```

즉 기본 production-style에 controlled smoke를 섞지 않았다는 뜻이다.

Controlled smoke:

```text
output/test_census_v4_verified_full_tests_smoke

FULL_THESIS = 2
source_backed_ready_count = 1
guard_replay_ready_count = 1
missing_required_archetype_count = 31
c06_guard_replay_pass_allowed = true
c06_guard_replay_status = C06_GUARD_REPLAY_PASS
```

C06 row:

```text
replay_status = SOURCE_BACKED_SMOKE_AND_GUARD_REPLAY_READY
replay_scope = controlled_smoke_and_guard_only
accepted_claim_count = 14
score_contribution_count = 14
guard_case_count = 3
guard_case_pass_count = 3
source_proxy_leak_count = 0
```

## 4. 테스트

Targeted:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_all_archetype_replay_matrix \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_full_thesis_smoke_tasks \
  -v
```

결과:

```text
Ran 14 tests
OK
```

Census v4 suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v
```

결과:

```text
Ran 102 tests
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
test_count = 4983
failed_count = 0
error_count = 0
duration_seconds = 166.9824
log_sha256 = 18e7629f2f6d299c706361d9f0819d251474218fa826d2e45a3a2a0438387979
```

## 5. 남은 blocker

여전히 완료가 아니다.

```text
brain_web_evidence_pass_false
full_thesis_production_pass_false
source_backed_replay_parity_all_archetypes_pending
```

기본 production-style에는 smoke를 켜지 않았으므로 아래도 남는다.

```text
full_thesis_smoke_pending
```

남은 핵심:

```text
1. Brain/Web live acquisition -> accepted claim -> score -> Stage promotion
2. production full thesis runner
3. C01~C32 전체 positive+guard replay parity
4. R13 guard contract source-backed/adversarial replay
```

최종 한 문장:

> C06 guard false-positive 방어는 controlled smoke에서 닫혔다. 하지만 이것은 "삼성/하이닉스 C06 예제 하나가 positive+guard를 통과했다"는 뜻이지, 운영 full-thesis나 전체 아키타입 replay가 완료됐다는 뜻은 아니다.

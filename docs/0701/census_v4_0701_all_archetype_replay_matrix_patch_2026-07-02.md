# Census v4 0701 All-Archetype Replay Matrix Patch

작성 시점: 2026-07-02 KST

> 최신 주의: 이 문서의 "controlled smoke 기준 C06 ready 1개" 표현은
> `census_v4_0701_external_reviewer_final_attack_packet_after_c06_overclaim_fix_2026-07-02.md` 이후 superseded됐다.
> 현재 C06 smoke는 source-backed semantic replay가 아니라 wiring smoke로만 인정한다.
> 최신 controlled smoke matrix는 `source_backed_ready_count=0`, `guard_replay_ready_count=0`,
> `controlled_wiring_smoke_ready_count=1`, `missing_required_archetype_count=32`이다.

이 문서는 `census_v4_0701_smoke_score_contribution_sum_patch_2026-07-02.md` 이후 추가 패치 결과를 고정한다.

한 줄 결론:

> `all_archetype_replay_pass=false`가 더 이상 설명 없는 boolean이 아니다. `all_archetype_replay_matrix.json`이 C01~C32와 R13 guard 계약 36개를 모두 펼쳐서, 어떤 아키타입이 source-backed replay ready이고 어떤 아키타입이 source gap인지 보여준다.

쉬운 예:

```text
이전:
"전 과목 replay 아직 아님"이라고만 적힘

현재:
36개 과목 표가 생김
C06은 삼성/하이닉스 smoke 예제 2개가 있음
나머지는 source-backed positive/guard replay가 아직 없다고 명시됨
```

## 1. 코드 변경

변경 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_artifact_manifest.py
tests/test_census_v4_all_archetype_replay_matrix.py
```

새 leaf artifact:

```text
output/.../all_archetype_replay_matrix.json
output/.../c06_guard_replay_audit.json
```

운영 docs 복사 대상:

```text
docs/operational/census_mode_v4_all_archetype_replay_matrix.json
docs/operational/census_mode_v4_c06_guard_replay_audit.json
```

matrix는 아래 정보를 포함한다.

```text
archetype_id
contract_loaded
replay_status
replay_scope
fixture_count
source_backed_fixture_count
positive_replay_pass
guard_replay_pass
source_proxy_leak_count
accepted_claim_count
score_contribution_count
full_thesis_symbols
unsupported_reason
required_before_goal_completion
```

## 2. 검산 결과

기본 production-style output:

```text
output/test_census_v4_verified_full_tests

all_archetype_replay_pass = false
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 0
guard_replay_ready_count = 0
missing_required_archetype_count = 32
status_counts = {
  "GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY": 4,
  "SOURCE_GAP_PENDING": 32
}
```

기본 production-style에서 C06 guard audit:

```text
guard_replay_pass = false
positive_replay_ready = false
guard_case_count = 3
guard_case_pass_count = 3
blockers = ["c06_positive_replay_required_before_guard_pass"]
```

Controlled smoke output:

```text
output/test_census_v4_verified_full_tests_smoke

all_archetype_replay_pass = false
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 1
guard_replay_ready_count = 1
missing_required_archetype_count = 31
status_counts = {
  "GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY": 4,
  "SOURCE_BACKED_SMOKE_AND_GUARD_REPLAY_READY": 1,
  "SOURCE_GAP_PENDING": 31
}
```

C06 row:

```text
archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
replay_status = SOURCE_BACKED_SMOKE_AND_GUARD_REPLAY_READY
replay_scope = controlled_smoke_and_guard_only
source_backed_fixture_count = 2
full_thesis_symbols = ["000660", "005930"]
accepted_claim_count = 14
score_contribution_count = 14
positive_replay_pass = true
guard_replay_pass = true
guard_case_count = 3
guard_case_pass_count = 3
```

중요:

```text
C06 positive+guard controlled replay가 1개 ready라는 뜻이지,
all_archetype_replay_pass가 true라는 뜻이 아니다.
```

## 3. 테스트

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

## 4. 현재 최종 상태

기본 production-style:

```text
FULL_THESIS = 0
FULL_E2R_100 = 0
full_thesis_smoke_pass = false
full_thesis_production_pass = false
all_archetype_replay_pass = false
meaningful_operational_stage_pass = false
```

Controlled smoke:

```text
FULL_THESIS = 2
FULL_E2R_100 = 2
full_thesis_smoke_pass = true
full_thesis_production_pass = false
all_archetype_replay_pass = false
meaningful_operational_stage_pass = false
source_backed_ready_count = 1
guard_replay_ready_count = 1
missing_required_archetype_count = 31
```

남은 blocker:

```text
brain_web_evidence_pass_false
full_thesis_production_pass_false
source_backed_replay_parity_all_archetypes_pending
```

기본 production-style에는 smoke를 켜지 않았으므로 아래 blocker도 추가로 남는다.

```text
full_thesis_smoke_pending
full_thesis_production_pass_false
```

추가 후속 보강:

```text
full_thesis_production_audit.json이 artifact manifest와 docs/operational에 추가됐다.
기본 production-style:
  verdict = PENDING_FULL_THESIS_PRODUCTION
  production_full_thesis_row_count = 0
  blockers = ["production_full_thesis_runner_not_implemented"]

controlled smoke:
  controlled_smoke_full_thesis_row_count = 2
  production_full_thesis_row_count = 0
  verdict = PENDING_FULL_THESIS_PRODUCTION
```

## 5. 다음 공격 지점

다음 에이전트가 먼저 볼 것:

```text
1. matrix의 SOURCE_GAP_PENDING 31개를 실제 source-backed fixture/replay로 채웠는가?
2. C06도 guard_replay_pass=false인데 이걸 어떻게 채울 것인가?
3. R13 guard contracts 4개는 어떤 adversarial replay로 검증할 것인가?
4. matrix가 true가 되기 전에 goal_completion_ready가 true가 되는 우회가 있는가?
5. Brain/Web enabled acquisition 없이 meaningful pass가 true가 되는 우회가 있는가?
```

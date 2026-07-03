# Census v4 0701 Controlled Smoke Gate Production Guard Patch

작성일: 2026-07-02 KST
repo: `/home/eorb915/projects/stock_agent`
as_of_date: `2026-07-01`

## 한 줄 결론

```text
controlled smoke는 계속 실행할 수 있다.
하지만 production/live/meaningful gate를 대신 만족시키는 길은 더 강하게 막았다.
```

쉬운 예:

```text
모의시험은 모의시험 점수표에만 쓴다.
모의시험에서 88점이 나와도 정식 시험을 본 것으로 처리하지 않는다.
```

## 왜 이 패치가 필요했나

이전 상태에서도 `full_thesis_production_audit.json`은 production runner 미구현을 blocker로 잡고 있었다.
하지만 사람이 산출물을 볼 때 다음 오독 가능성이 남아 있었다.

```text
controlled smoke에서 삼성전자/하이닉스 FULL_THESIS 2개가 생성됨
→ full_thesis_smoke_pass = true
→ 혹시 production/meaningful 준비로 착각
```

특히 다음 조합은 더 위험하다.

```text
run_mode = FULL_LIVE_BRAIN_CENSUS
full_thesis_smoke_mode = controlled_replay
target_gate = meaningful 또는 full_thesis_smoke
```

이 경우 smoke row가 있더라도 운영 live run의 증거가 아니다.
따라서 gate를 더 명확히 나눴다.

## 코드 패치

변경 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_full_thesis_smoke_tasks.py
docs/0701/README.md
docs/0701/census_v4_0701_controlled_smoke_gate_production_guard_patch_2026-07-02.md
```

핵심 변경:

```text
1. readiness_verdict.json에 full_thesis_smoke_gate_pass_allowed 추가
2. readiness_verdict.json에 full_thesis_smoke_gate_blockers 추가
3. full_thesis_production_audit.json에 production_mode_requested 추가
4. full_thesis_production_audit.json에 controlled_smoke_substitution_rejected_count 추가
5. acceptance_report.md에 "5d. Full thesis smoke gate" 라인 추가
6. target_gate=full_thesis_smoke도 production/live run_mode에서는 smoke로 통과하지 못하게 함
```

## 새 규칙

### 1. Smoke 실행 여부와 smoke gate 통과 여부를 분리

```text
full_thesis_smoke_pass
= controlled smoke row가 배관상 성공했는가

full_thesis_smoke_gate_pass_allowed
= 이 실행 문맥에서 그 smoke pass를 target gate 통과로 인정해도 되는가
```

예:

```text
LEDGER_REFRESH_CENSUS + target_gate=full_thesis_smoke:
  full_thesis_smoke_pass = true
  full_thesis_smoke_gate_pass_allowed = true

FULL_LIVE_BRAIN_CENSUS + target_gate=meaningful:
  full_thesis_smoke_pass = true일 수 있음
  full_thesis_smoke_gate_pass_allowed = false
```

### 2. Production full thesis audit이 smoke 대체를 명시적으로 거부

새 필드:

```text
production_mode_requested
controlled_smoke_substitution_rejected_count
controlled_smoke_substitution_allowed = false
```

예:

```text
FULL_LIVE_BRAIN_CENSUS에서 smoke row 2개가 생기면:
  production_full_thesis_row_count = 0
  controlled_smoke_full_thesis_row_count = 2
  controlled_smoke_substitution_rejected_count = 2
  blockers includes controlled_smoke_rows_rejected_as_production_substitute
```

의미:

```text
smoke row가 있다고 production row로 세지 않는다.
오히려 production 문맥에서는 "대체 시도 거부"로 표시한다.
```

## 최신 산출물 확인

### 기본 production-style output

경로:

```text
output/test_census_v4_verified_full_tests
output/census_v4/2026-07-01
```

`readiness_verdict.json`:

```text
target_gate = anti_fake
target_gate_pass = true
full_thesis_smoke_pass = false
full_thesis_smoke_gate_pass_allowed = false
full_thesis_smoke_gate_blockers =
  - full_thesis_smoke_not_passed
  - full_thesis_smoke_gate_not_requested
full_thesis_production_pass = false
```

`full_thesis_production_audit.json`:

```text
run_mode = LEDGER_REFRESH_CENSUS
target_gate = anti_fake
full_thesis_smoke_mode = disabled
production_mode_requested = false
production_pass_allowed = false
production_full_thesis_row_count = 0
controlled_smoke_full_thesis_row_count = 0
controlled_smoke_substitution_rejected_count = 0
blockers =
  - production_full_thesis_runner_not_implemented
```

### controlled smoke output

경로:

```text
output/test_census_v4_verified_full_tests_smoke
```

`readiness_verdict.json`:

```text
target_gate = full_thesis_smoke
target_gate_pass = true
full_thesis_smoke_pass = true
full_thesis_smoke_gate_pass_allowed = true
full_thesis_smoke_gate_blockers = []
full_thesis_production_pass = false
```

`full_thesis_production_audit.json`:

```text
run_mode = LEDGER_REFRESH_CENSUS
target_gate = full_thesis_smoke
production_mode_requested = false
production_pass_allowed = false
production_full_thesis_row_count = 0
controlled_smoke_full_thesis_row_count = 2
controlled_smoke_substitution_rejected_count = 0
blockers =
  - production_full_thesis_runner_not_implemented
```

의미:

```text
명시적 smoke gate에서는 smoke pass를 인정한다.
하지만 production full thesis pass는 여전히 false다.
```

### 새 회귀 테스트 시나리오

테스트에서 직접 확인한 시나리오:

```text
run_mode = FULL_LIVE_BRAIN_CENSUS
brain_web_mode = enabled
full_thesis_smoke_mode = controlled_replay
target_gate = meaningful
```

기대 결과:

```text
smoke.verdict = FULL_THESIS_SMOKE_PASS
readiness.full_thesis_smoke_pass = true
readiness.full_thesis_smoke_gate_pass_allowed = false
readiness.target_gate_pass = false
readiness.meaningful_operational_stage_pass = false
production.production_full_thesis_row_count = 0
production.controlled_smoke_full_thesis_row_count = 2
production.controlled_smoke_substitution_rejected_count = 2
production.blockers includes controlled_smoke_rows_rejected_as_production_substitute
```

## 테스트 결과

관련 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_goal_required_audits -v

Ran 27 tests in 48.408s
OK
```

V4 전체 테스트:

```text
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v

Ran 105 tests in 59.465s
OK
```

전체 테스트 artifact:

```text
artifact = output/test_full_repo_0701/full_unittest_result_artifact.json
log = output/test_full_repo_0701/full_unittest.log

status = OK
exit_code = 0
test_count = 4986
failed_count = 0
error_count = 0
duration_seconds = 177.3705
log_sha256 = 26028de27493e5e0ee9ebe4a10917e98a4900f58fdf0acb96b0ef4cbf5dfe274
```

## 현재 남은 blocker

이번 패치는 smoke 오독을 막은 것이지 운영 완성을 만든 것이 아니다.

여전히 남은 blocker:

```text
brain_web_evidence_pass_false
full_thesis_production_pass_false
source_backed_replay_parity_all_archetypes_pending
controlled_semantic_replay_pending
```

기본 output은 여전히:

```text
FULL_THESIS row = 0
full_e2r_verified_score_count = 0
Brain/Web = disabled
production_full_thesis_runner_not_implemented
```

controlled smoke output은 여전히:

```text
FULL_THESIS row = 2
production_full_thesis_row_count = 0
controlled smoke는 production 대체 불가
```

## 다음 패치 방향

다음 작업은 smoke 방어가 아니라 실제 운영 쪽이다.

우선순위:

```text
1. production full thesis runner를 controlled smoke와 별도 경로로 구현
2. selected candidate에 Brain/Web official-first SourceTask 실행
3. LLM planner/extractor trace를 accepted claim, score contribution, StageCourt trace까지 연결
4. C06/C08/C15/C17/C24/C28 source-backed semantic replay를 실제 URL anchor로 승격
5. source_proxy_only/evidence_url_pending research row가 production fixture로 새지 않는지 계속 차단
```

최종 완료 기준은 그대로다.

```text
controlled smoke pass != production pass
event board Stage != full thesis Stage
Brain/Web disabled != operational Brain/Web pass
source-backed semantic replay pending != all-archetype replay pass
```


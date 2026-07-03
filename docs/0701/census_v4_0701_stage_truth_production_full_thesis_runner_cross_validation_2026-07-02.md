# Census v4 0701 Stage Truth / Production Full Thesis Runner Cross Validation

작성 시각: 2026-07-02 KST

이 문서는 다음 에이전트가 빡세게 반박할 수 있도록 현재 상태를 숨기지 않고 적은 공격용 검증 패킷이다.

## 한 줄 결론

Stage row는 있다. 하지만 현재 canonical output의 Stage는 전부 `CENSUS_EVENT_BOARD` 상태판이고, 운영 확정용 `FULL_THESIS / FULL_E2R_100` Stage는 0개다.

쉽게 말하면:

```text
있는 것:
  전 종목 현재 상태판
  예: 새 공시 없음, 공식 이벤트 watch, material claim watch, risk review

아직 없는 것:
  모든 종목에 대해 Evidence OS가 원문 claim을 모아 full thesis 점수와 Stage를 확정한 운영 지도
```

`Stage0`은 "나쁜 종목 0점"이 아니다. `CensusAssessmentEvent`로 한 번 확인했지만 현재 catalyst가 확인되지 않았다는 상태다.

## 이번에 확인한 직접 답

질문: "stage가 있는 애들이 있긴 해?"

답:

```text
canonical output: output/census_v4/2026-07-01

census_stage_status.jsonl rows = 3391
stage_scope_distribution = {"CENSUS_EVENT_BOARD": 3391}
canonical_stage_distribution = {"0": 3306, "1": 54, "2": 30, "3-Red": 1}
base_stage_distribution = {"Stage0": 3306, "Stage1": 54, "Stage2-Watch": 30, "Red": 1}
score_scale_distribution = {"NO_SCORE": 3324, "EVENT_WEIGHTED_PARTIAL": 67}
operator_stage_use_distribution = {"NOT_FULL_THESIS_STAGE": 3391}
FULL_E2R_100 rows = 0
```

즉 Stage label은 3391개가 있다. 그러나 운영 full thesis Stage는 아니다.

쉬운 예:

```json
{
  "symbol": "000660",
  "company_name": "SK하이닉스",
  "canonical_stage": "1",
  "base_stage": "Stage1",
  "stage_scope": "CENSUS_EVENT_BOARD",
  "stage_signal": "OFFICIAL_EVENT_WATCH",
  "score_scale": "EVENT_WEIGHTED_PARTIAL",
  "event_evidence_score": 4.0,
  "verified_score": null,
  "operator_stage_use": "NOT_FULL_THESIS_STAGE",
  "operator_score_use": "NOT_FULL_E2R_SCORE"
}
```

이 뜻은 "SK하이닉스 HBM thesis를 100점 기준으로 평가해 Stage1이 확정됐다"가 아니다.

뜻은:

```text
공식/기존 ledger 이벤트가 있어서 watch row가 생겼다.
하지만 full thesis Evidence OS refresh는 아직 안 돌았다.
그래서 operator가 이 값을 FULL_E2R stage/score로 쓰면 안 된다.
```

Red 예시도 같다:

```json
{
  "symbol": "030350",
  "company_name": "드래곤플라이",
  "canonical_stage": "3-Red",
  "base_stage": "Red",
  "stage_scope": "CENSUS_EVENT_BOARD",
  "stage_signal": "RISK_REVIEW",
  "score_scale": "EVENT_WEIGHTED_PARTIAL",
  "operator_stage_use": "NOT_FULL_THESIS_STAGE"
}
```

이것도 full thesis Red 확정이 아니라 현재 event board risk review row다.

## 패치/검증에서 바로잡은 것

### 1. Production full thesis runner 감사 경로

`src/e2r/census/census_runner_v4.py`에는 production full thesis promotion 경로가 생겼다.

핵심 조건:

```text
stage_scope == BRAIN_WEB_PARTIAL
stage_source == research_brain_v4_attempt
real planner provider
production live source acquisition
accepted claim ids 존재
score contribution ids 존재
primitive state ids 존재
Evidence Contract green gate primitive coverage 충족
claim이 direct/current/score_eligible
document/anchor 존재
stagecourt score_status FINAL 또는 FINAL_WITH_NONMATERIAL_GAPS
```

위 조건을 모두 통과한 row만:

```text
stage_scope = FULL_THESIS
score_scale = FULL_E2R_100
score_scope = FULL_E2R_100
score_source = BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT
operator_stage_use = FULL_THESIS_STAGE
operator_score_use = FULL_E2R_SCORE
```

로 승격된다.

반대로 partial row는 그대로 partial이다.

### 2. Controlled smoke가 production pass를 대신하지 못하게 차단

`full_thesis_smoke_mode=controlled_replay`는 배관 테스트다. 삼성전자/하이닉스 controlled fixture 2개가 `FULL_THESIS` row를 만들 수 있지만, 이건 production row가 아니다.

검증된 smoke output:

```text
output/test_census_v4_verified_full_tests_smoke

full_thesis_smoke_pass = true
full_thesis_smoke_gate_pass_allowed = true
full_thesis_production_pass = false
full_thesis_production_audit.production_full_thesis_row_count = 0
full_thesis_production_audit.controlled_smoke_full_thesis_row_count = 2
```

즉 smoke gate를 명시적으로 요청한 비운영 배관 테스트에서는 smoke pass가 가능하다. 그러나 production full thesis pass는 여전히 false다.

쉬운 예:

```text
controlled smoke = 소방훈련
production full thesis = 실제 화재 대응 기록

소방훈련이 성공했다고 실제 화재 대응 실적이 생긴 것은 아니다.
```

### 3. Production/live 문맥에서 controlled smoke 대체 금지

`FULL_LIVE_BRAIN_CENSUS`, `meaningful`, `full_thesis` 같은 production/live 문맥에서는 controlled smoke를 full thesis 대체로 쓰지 못한다.

관련 테스트:

```text
test_controlled_smoke_cannot_satisfy_full_live_or_meaningful_gate
test_full_thesis_smoke_target_is_allowed_only_as_explicit_non_production_smoke_gate
```

## 이번에 실제로 고친 테스트 fixture 오류

작업 중 깨졌던 테스트는 운영 로직 자체보다 fixture helper가 섞인 문제였다.

문제:

```text
_write_live_brain_promotion_fixture
  partial Brain/Web Stage fixture여야 함

_write_live_brain_full_thesis_fixture
  green gate가 모두 닫힌 full thesis fixture여야 함
```

그런데 두 helper가 한 함수 안에 섞여서 partial fixture가 source task 한 줄만 쓰고 끝났다. 그래서 기존 Stage promotion 테스트가 claim, primitive, stagecourt trace를 읽지 못했다.

수정:

```text
tests/test_census_v4_brain_stage_promotion_gate.py

partial helper:
  CLM-A / PRIM-A / SCON-A / SCT-BRAIN-A만 가진 PENDING_MATERIAL_GAPS row
  C06 archetype은 있지만 green gate primitive 부족
  결과: BRAIN_WEB_PARTIAL 유지

full helper:
  C06 green gate primitive 4개를 모두 가진 FINAL row
  결과: production FULL_THESIS 승격 가능
```

이 테스트가 중요한 이유:

```text
partial row가 실수로 FULL_THESIS로 승격되면,
"Stage 있는 애들이 있긴 하냐" 질문에 가짜로 "있다"고 답하게 된다.
```

## 검증 결과

### Targeted tests

명령:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_artifact_manifest -v
```

결과:

```text
Ran 22 tests
OK
```

확인한 핵심:

```text
partial Brain/Web row는 green gate coverage가 부족하면 FULL_THESIS가 되지 않는다.
green gate가 모두 닫힌 live/source-backed row는 FULL_THESIS로 승격될 수 있다.
controlled smoke는 production full thesis pass를 대신하지 않는다.
full_thesis_production_runner_audit.json이 artifact manifest에 포함된다.
```

### Census v4 tests

명령:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v
```

결과:

```text
Ran 107 tests in 60.209s
OK
```

### Full repo tests

명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v
```

결과:

```text
status = OK
exit_code = 0
test_count = 4992
failed_count = 0
error_count = 0
duration_seconds = 184.878
log_sha256 = 2207625b90762539d78da558bdcfb16a129f50d493375d3f3e8bf4485f5a4043
```

## 재생성한 산출물

### Canonical anti-fake output

명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --target-gate anti_fake \
  --write-operational-docs auto \
  --test-result-summary full_repo_unittest_ok \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json
```

결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

중요: 이 pass는 "가짜 completion 방어막 통과"이지 "운영 full thesis pass"가 아니다.

### Verified anti-fake output

```text
output/test_census_v4_verified_full_tests
```

결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

### Controlled smoke output

```text
output/test_census_v4_verified_full_tests_smoke
```

결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
target_gate = full_thesis_smoke
full_thesis_smoke_pass = true
full_thesis_smoke_gate_pass_allowed = true
full_thesis_production_pass = false
```

## Canonical readiness 현재값

파일:

```text
output/census_v4/2026-07-01/readiness_verdict.json
output/census_v4/2026-07-01/goal_completion_audit.json
output/census_v4/2026-07-01/full_thesis_production_audit.json
output/census_v4/2026-07-01/full_thesis_production_runner_audit.json
```

핵심값:

```text
target_gate = anti_fake
target_gate_pass = true
meaningful_operational_stage_pass = false
brain_web_evidence_pass = false
full_thesis_smoke_pass = false
full_thesis_smoke_gate_pass_allowed = false
full_thesis_production_pass = false
```

Goal blockers:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_production_pass_false
source_backed_replay_parity_all_archetypes_pending
controlled_semantic_replay_pending
```

Production full thesis audit:

```text
verdict = PENDING_FULL_THESIS_PRODUCTION
production_runner_implemented = true
production_mode_requested = false
production_full_thesis_row_count = 0
controlled_smoke_full_thesis_row_count = 0
blockers = ["production_full_thesis_not_requested_or_no_rows"]
```

Production full thesis runner audit:

```text
verdict = NOT_REQUESTED
production_mode_requested = false
candidate_row_count = 0
promoted_full_thesis_row_count = 0
```

## 공격 관점 교차검증

### 공격 1. "Stage가 있으면 운영 Stage 완료 아닌가?"

반박:

```text
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
score_scale = NO_SCORE 또는 EVENT_WEIGHTED_PARTIAL
full_e2r_verified_score rows = 0
```

따라서 운영 full thesis 완료가 아니다.

### 공격 2. "controlled smoke에서 FULL_THESIS 2개가 있으니 production pass 아닌가?"

반박:

```text
output/test_census_v4_verified_full_tests_smoke/full_thesis_production_audit.json

production_full_thesis_row_count = 0
controlled_smoke_full_thesis_row_count = 2
production_pass_allowed = false
```

smoke는 배관 테스트다.

### 공격 3. "production full thesis runner가 구현된 척만 한 것 아닌가?"

반박:

관련 targeted test가 있다.

```text
test_full_green_gate_brain_stage_can_be_promoted_to_production_full_thesis
```

이 fixture는 C06 green gate primitive를 모두 채운 live/source-backed claim 장부를 만들고, 실제로 `FULL_THESIS / FULL_E2R_100`으로 승격되는지 본다.

동시에 반대 테스트도 있다.

```text
test_brain_partial_stage_is_not_production_full_thesis_without_green_gate_coverage
```

이 fixture는 C06 archetype은 있지만 green gate primitive가 부족하므로 `BRAIN_WEB_PARTIAL`에 남는다.

### 공격 4. "테스트 fixture라서 실제 운영 준비와 무관한 것 아닌가?"

맞다. 그래서 goal completion은 여전히 false다.

현재 runner는 승격 조건과 감사를 갖췄지만, canonical run에서는 Brain/Web production full thesis 후보 자체가 없다.

운영 준비가 되려면:

```text
real provider
production live source acquisition
contract-blind extractor
direct/current/score_eligible accepted claims
primitive mapping
source-backed C01~C36 replay parity
controlled semantic replay pass
```

가 실제 output에서 닫혀야 한다.

### 공격 5. "이제 meaningful gate를 통과시켜도 되는가?"

아니다.

현재 `target_gate=anti_fake`만 통과한다.

```text
meaningful_operational_stage_pass = false
full_thesis_production_pass = false
brain_web_evidence_pass = false
```

## 다음 패치 방향

우선순위는 다음 순서가 맞다.

### P1. Canonical production full thesis 후보 만들기

지금 canonical output은 `production_mode_requested=false`다.

다음 패치는 production/live 설정에서:

```text
Brain/Web enabled
real planner provider
live official-first source acquisition
strict stage promotion
target_gate meaningful 또는 full_thesis
```

를 걸고, 실제 accepted claim -> primitive state -> score contribution -> stagecourt trace -> FULL_THESIS row가 생기는지 확인해야 한다.

주의:

```text
controlled smoke로 대체 금지
CENSUS_EVENT_BOARD row를 FULL_THESIS로 이름만 바꾸기 금지
```

### P2. Source-backed replay parity 확장

현재:

```text
all_archetype_replay_pass = false
blocker = source_backed_replay_parity_all_archetypes_pending
```

다음은 C01~C36 각 Evidence Contract에 대해 최소 하나 이상의 source-backed positive/guard replay를 운영 장부 형태로 닫아야 한다.

source_proxy_only 연구자료는 정답 fixture로 쓰면 안 된다.

### P3. Controlled semantic replay pending 6개 닫기

현재 pending:

```text
C06_HBM_POSITIVE_AND_QUALIFICATION_LAG_GUARD
C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD
C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD
C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
C24_CLINICAL_BINARY_EVENT_GUARD
C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

이건 단순 score weight 문제가 아니다. 각 case에서 원문 claim이 어느 primitive로 가고, 무엇이 guard인지 증거 장부로 보여야 한다.

### P4. Brain/Web readiness를 실제 claim 장부로 통과시키기

현재:

```text
brain_web_evidence_pass_allowed = false
brain_web_attempt verdict = NOT_REQUESTED
```

필요한 것은:

```text
source_task_executions
evidence_documents
evidence_anchors
accepted_claims
primitive_states
score_contributions
stagecourt_traces
brain_to_claim_trace
```

가 모두 같은 claim chain으로 연결되는 output이다.

### P5. 의미 있는 운영 Stage pass는 마지막에만 선언

다음 조건 전에는 완료라고 하면 안 된다.

```text
brain_web_evidence_pass_allowed = true
full_thesis_production_pass = true
source_backed_replay_parity_all_archetypes = true
controlled_semantic_replay_pass = true
frozen/live bounded smoke repeatable
```

## 다음 에이전트가 반드시 공격해야 할 질문

1. `full_thesis_production_runner_audit.json`이 실제 production/live run에서 `PRODUCTION_FULL_THESIS_PROMOTED`를 만든 사례가 있는가?
2. 그 사례의 accepted claim은 source task, document, anchor, primitive state, score contribution, stagecourt trace로 닫혀 있는가?
3. `FULL_THESIS` row가 controlled smoke task id(`FTSMOKE-*`)에서 온 것은 아닌가?
4. `CENSUS_EVENT_BOARD` row를 operator가 full thesis로 오해할 여지가 출력에 남아 있는가?
5. Stage2-Watch 30개가 full thesis Stage2처럼 보이는 UI/리포트 문구가 있는가?
6. C06 positive replay가 guard replay URL을 재사용해서 overclaim하지 않는가?
7. C08/C15/C17/C24/C28 pending semantic replay가 source-backed fixture로 닫혔는가?
8. source_proxy_only 연구 row가 production score contribution으로 새는 경로가 있는가?
9. 일반 웹 검색 fallback이 production daily mode에서 무제한으로 열리는 경로가 있는가?
10. provider failure가 낮은 점수 확정으로 바뀌는 경로가 남아 있는가?

## 최종 판단

현재 상태를 정확히 표현하면:

```text
Anti-fake Census status board: 통과
Stage row existence: 있음
Event-board stage/score chain: 있음
Controlled full-thesis wiring smoke: 별도 smoke 실행에서 통과 가능
Production full-thesis operation: 아직 미통과
Meaningful operational stage map: 아직 미통과
Goal completion: false
```

따라서 다음 에이전트에게 넘길 정직한 문장은 이것이다.

> 지금은 Stage가 없는 게 문제가 아니다. Stage의 의미가 두 층으로 분리되어 있고, 현재 canonical output의 Stage는 운영 full thesis가 아니라 Census event board다. 다음 패치는 이 분리를 유지한 채 실제 Brain/Web production claim chain으로 FULL_THESIS row를 만드는 것이다.

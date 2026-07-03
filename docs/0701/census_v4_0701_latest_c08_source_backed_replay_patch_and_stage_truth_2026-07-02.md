# Census v4 0701 Latest C08 Source-Backed Replay Patch / Stage Truth

작성 시점: 2026-07-02 KST  
repo: `/home/eorb915/projects/stock_agent`  
canonical output: `output/census_v4/2026-07-01`  
as_of_date: `2026-07-01`

## 한 줄 결론

```text
C08 source-backed semantic replay가 추가로 닫혔다.
이제 C06, C08 두 아키타입은 source-backed positive + guard replay ready다.

하지만 canonical output의 운영 FULL_THESIS / FULL_E2R_100 Stage row는 여전히 0개다.
```

쉬운 예:

```text
채점표 전체가 끝난 게 아니다.
C06 과목에 이어 C08 과목에서도 "원문 PDF 문장 -> claim -> primitive" 경로가 1개 더 검증된 것이다.

전교생 정식 시험 채점지는 아직 없고,
과목별 채점 규칙이 실제 원문을 읽는지 확인하는 replay가 하나 더 통과한 상태다.
```

## 이번 패치로 바뀐 것

### 1. C08 replay source socket 추가

새 데이터:

```text
data/replay_source_snapshots/replay_source_snapshots.jsonl
data/replay_source_snapshots/qrt_c08_positive_20240108.txt
data/replay_source_snapshots/qrt_c08_profile_guard_20240108.txt
```

새 source class:

```text
ReplaySourceSnapshot
```

의미:

```text
실제 PDF URL에서 뽑은 짧은 source excerpt를 task_id 단위로 고정해서
positive replay와 guard replay가 서로 다른 문장 조각을 읽게 한다.
```

왜 이렇게 했는가:

```text
같은 PDF 전체를 무조건 읽으면 profile-only guard가 positive 문장까지 같이 먹을 수 있다.
그래서 source_task_id로 어떤 replay task가 어떤 source excerpt를 읽는지 고정했다.
이건 C08 전용 하드코딩이 아니라 C15/C17/C24/C28에도 재사용할 수 있는 데이터 기반 replay socket이다.
```

### 2. C08 source-backed semantic replay 추가

새 산출물:

```text
output/census_v4/2026-07-01/c08_source_backed_semantic_replay.json
```

현재 값:

```text
positive_replay_pass = true
guard_replay_pass = true
accepted_claim_count = 4

positive_accepted_primitive_ids:
  socket_or_test_demand_visible
  named_customer_quality

guard_accepted_primitive_ids:
  socket_or_test_demand_visible

profile_only_guard_leaked_primitives = []
document_urls:
  https://ssl.pstatic.net/imgstock/upload/research/company/1704669223541.pdf

blockers = []
```

해석:

```text
QRT 원문 PDF 조각에서 C08 positive bridge 두 개를 뽑았다.
1. 신뢰성 평가 / 반도체 테스트 서비스 profile -> socket_or_test_demand_visible
2. 고객사 다변화 / 리벨리온 업무협약 -> named_customer_quality

그리고 profile-only 조각은 socket/test profile까지만 열고,
named_customer_quality, qualification_confirmed, repeat_order_confirmed, margin_bridge_visible로 새지 않았다.
```

중요한 제한:

```text
replay_only = true
production_score_evidence_allowed = false
score_contribution_count = 0
```

즉 이것은:

```text
원문 PDF에서 C08 semantic primitive를 뽑는 경로 검증
```

이지, 아래 뜻이 아니다.

```text
나쁜 해석:
  QRT 2026-07-01 운영 점수 확정
  C08 전체 Green 조건 충족
  모든 C08 primitive coverage 완료
  full thesis production Stage 생성
```

### 3. `Capacitor` -> `capa` 오분류 방지

수정 파일:

```text
src/e2r/production/claim_extraction/contract_blind_extractor.py
```

문제:

```text
"Capacitor" 안의 "capa" 때문에 전자부품 profile 문장이 capacity_allocation_claim으로 오분류될 수 있었다.
```

수정:

```text
capa는 독립 토큰일 때만 CAPA/capacity로 본다.
Capacitor 같은 단어 안의 부분 문자열은 capacity claim으로 보지 않는다.
```

쉬운 예:

```text
나쁜 판정:
  "Capacitor 품질 신뢰성 평가"
  -> capa 발견
  -> capacity allocation claim

수정 후:
  "Capacitor"는 전자부품명일 뿐이다.
  CAPA/capacity claim이 아니다.
```

### 4. test artifact ambiguity 제거

문제:

```text
이전에는 acceptance report는 외부 full test artifact 4992개를 보는데,
output/census_v4/2026-07-01/test_result_artifact.json 안에는 오래된 4951개 artifact가 남아 있었다.
```

수정:

```text
--test-result-artifact를 넘긴 실행에서는 해당 artifact를 output root의 test_result_artifact.json으로 동기화한다.
```

현재 값:

```text
output/census_v4/2026-07-01/test_result_artifact.json:
  status = OK
  test_count = 4993
  failed_count = 0
  error_count = 0
  duration_seconds = 180.7913
  log_sha256 = dba6674e76355fc2c1ebffd67124bd04b9f472201612cec814d7e53512d514d2

output/test_full_repo_0701/full_unittest_result_artifact.json:
  status = OK
  test_count = 4993
  failed_count = 0
  error_count = 0
  duration_seconds = 180.7913
  log_sha256 = dba6674e76355fc2c1ebffd67124bd04b9f472201612cec814d7e53512d514d2
```

## 최신 숫자

### Stage truth

파일:

```text
output/census_v4/2026-07-01/census_stage_status.jsonl
```

현재 값:

```text
census_stage_status rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3391
  FULL_THESIS = 0

score_scope / score_scale:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

canonical_stage:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

verified_score_present = 0
full_e2r_verified_score rows = 0
```

해석:

```text
Stage label은 있다.
하지만 운영 full thesis Stage는 아직 없다.
```

### All-archetype replay matrix

파일:

```text
output/census_v4/2026-07-01/all_archetype_replay_matrix.json
```

현재 값:

```text
all_archetype_replay_pass = false
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 2
guard_replay_ready_count = 2
missing_required_archetype_count = 30

READY:
  C06_HBM_MEMORY_CUSTOMER_CAPACITY
  C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY

PENDING priority:
  C15_MATERIAL_SPREAD_SUPERCYCLE
  C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  C24_BIO_TRIAL_DATA_EVENT_RISK
  C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

### Controlled semantic replay

파일:

```text
output/census_v4/2026-07-01/controlled_semantic_replay_audit.json
```

현재 값:

```text
controlled_semantic_replay_pass = false
case_count = 10
pass_count = 6
pending_count = 4
fail_count = 0

PASS:
  C06_HBM_POSITIVE_AND_QUALIFICATION_LAG_GUARD
  C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD
  WRONG_SUBJECT_RISK_FIXTURE
  OLD_RISK_RESOLVED_FIXTURE
  PROVIDER_FAILURE_PENDING_FIXTURE
  SEMANTIC_CONTRACT_GUARD_FIXTURE

PENDING:
  C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD
  C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
  C24_CLINICAL_BINARY_EVENT_GUARD
  C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

### Goal matrix

파일:

```text
output/census_v4/2026-07-01/goal_requirement_matrix_audit.json
```

현재 값:

```text
goal_completion_minimum_pass = false
required_goal_completion_count = 17
required_goal_completion_pass_count = 12
required_goal_completion_pending_count = 5
required_goal_completion_fail_count = 0

pending_gate_ids:
  FULL_THESIS_SMOKE_PASS
  FULL_THESIS_PRODUCTION_PASS
  BRAIN_WEB_EVIDENCE_PASS
  ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
  CONTROLLED_SEMANTIC_REPLAY_PASS
```

왜 pass_count가 늘지 않았는가:

```text
C08 case 하나는 닫혔지만,
CONTROLLED_SEMANTIC_REPLAY_PASS 전체 gate는 C15/C17/C24/C28이 남아 있어 아직 pending이다.
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS도 required 32개 중 30개가 남아 있어 pending이다.
```

## 검증

타깃 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_all_archetype_replay_matrix \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_artifact_manifest -v

Ran 10 tests
OK
```

Census v4 전체 테스트:

```text
PYTHONPATH=src python -m unittest $(rg --files tests | rg 'tests/test_census_v4_.*\.py$' | sed 's#/#.#g; s#\.py$##') -v

Ran 112 tests
OK
```

Full repo test artifact:

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v

status = OK
test_count = 4993
failed_count = 0
error_count = 0
duration_seconds = 180.7913
log_sha256 = dba6674e76355fc2c1ebffd67124bd04b9f472201612cec814d7e53512d514d2
```

Canonical output 재생성:

```text
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --target-gate anti_fake \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json

ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

## 아직 남은 핵심 작업

다음 순서:

```text
1. C15 source-backed replay
   issuer pass-through / spread / margin bridge positive
   raw commodity headline guard

2. C17 source-backed replay
   realized spread / margin bridge positive
   spread-only or raw material-only guard

3. C24 source-backed replay
   endpoint / regulatory / partner / runway bridge
   binary-event-only guard

4. C28 source-backed replay
   ARR / RPO / renewal / retention bridge
   software/security keyword-only guard

5. FULL_THESIS smoke/prod source task execution

6. Real Brain/Web evidence gate
```

## 다음 에이전트 공격 포인트

완료라고 주장하면 아래를 먼저 확인한다.

```text
1. FULL_THESIS row가 생겼는가? 현재 0개다.
2. FULL_E2R_100 score row가 생겼는가? 현재 0개다.
3. Brain/Web/LLM planner call이 실제로 0보다 큰가? 현재 ledger refresh canonical은 0이다.
4. C15/C17/C24/C28 controlled semantic replay가 source-backed로 닫혔는가? 현재 pending이다.
5. all-archetype required 32개가 모두 source-backed ready인가? 현재 2/32다.
6. C08 replay가 production score로 새지 않았는가? score_contribution_count는 0이어야 한다.
7. profile-only guard가 named customer / qualification / margin bridge로 새지 않았는가?
8. `Capacitor`가 CAPA/capacity로 오분류되지 않는가?
9. output root의 test_result_artifact.json과 외부 full test artifact가 같은가?
```

## 최종 판정

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS:
  PASS

C06 source-backed replay:
  PASS

C08 source-backed replay:
  PASS

CONTROLLED_SEMANTIC_REPLAY_PASS:
  FALSE, 6/10 pass

ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS:
  FALSE, 2/32 ready

MEANINGFUL_OPERATIONAL_STAGE_PASS:
  FALSE

FULL_THESIS_PRODUCTION_PASS:
  FALSE

BRAIN_WEB_EVIDENCE_PASS:
  FALSE

Goal completion:
  FALSE
```


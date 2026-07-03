# Census v4 0701 Latest C17 Source-Backed Replay / Stage Truth Review Packet

작성 시점: 2026-07-02 KST  
repo: `/home/eorb915/projects/stock_agent`  
canonical output: `output/census_v4/2026-07-01`  
as_of_date: `2026-07-01`

> 최신 수치 주의: 이 문서는 C17 패치 직후 스냅샷이다. C24 source-backed replay 이후 최신 단일 진실은 `census_v4_0701_stage_existence_c24_patch_cross_review_packet_2026-07-02.md`와 `README.md`를 기준으로 한다. 최신 replay matrix는 `source_backed_ready_count=5`, `guard_replay_ready_count=5`, `missing_required_archetype_count=27`, controlled semantic replay는 `9/10 pass`다. Stage truth 자체는 변하지 않았다. 운영 `FULL_THESIS` row는 여전히 0개다.

## 한 줄 결론

```text
C17 source-backed semantic replay가 닫혔다.
이제 C06, C08, C15, C17 네 아키타입은 source-backed positive + guard replay ready다.

하지만 운영 FULL_THESIS / FULL_E2R_100 Stage row는 아직 0개다.
```

쉬운 예:

```text
원문 읽기 시험은 32과목 중 4과목이 통과했다.
하지만 전 종목 정식 E2R 100점 채점지는 아직 배포되지 않았다.
```

즉 "Stage가 있는 애들이 있긴 해?"에 대한 답은 둘로 나뉜다.

```text
상태판 Stage:
  있다. 3391개 row 전부 CENSUS_EVENT_BOARD stage다.

운영 full-thesis Stage:
  없다. FULL_THESIS row와 FULL_E2R_100 verified score row는 0개다.
```

## 현재 Stage Truth

`output/census_v4/2026-07-01/census_stage_summary.json` 기준:

```text
stage_status_count = 3391

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391

full_thesis_stage_distribution:
  FULL_THESIS_NOT_RUN = 3391

operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE = 3391

canonical_stage_distribution:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

verified_score_present_count = 0
full_e2r_verified_score_count = 0
```

해석:

```text
Stage0/1/2/3-Red 라벨은 존재한다.
그러나 이것은 daily census event-board 상태다.
아직 E2R 100점 verified score로 산출한 운영 thesis Stage가 아니다.
```

쉬운 예:

```text
Stage0:
  이번 전체 census에서 현재 catalyst가 확인되지 않았다는 상태판.
  "정식 E2R 점수가 낮아서 나쁜 종목"이라는 뜻이 아니다.

Stage1/Stage2:
  공시/이벤트/부분 claim 때문에 watch 상태로 올라온 row.
  C06 전체 thesis를 검증해서 Green/Yellow를 낸 것이 아니다.
```

## C17 패치 내용

새 canonical 산출물:

```text
output/census_v4/2026-07-01/c17_source_backed_semantic_replay.json
```

현재 값:

```text
positive_replay_pass = true
guard_replay_pass = true
accepted_claim_count = 10

positive_support_primitive_ids:
  opm_expansion_pctp
  spread_expansion
  utilization_rate

guard_support_primitive_ids:
  spread_expansion

spread_only_guard_leaked_support_primitives = []
blockers = []
replay_only = true
production_score_evidence_allowed = false
```

사용한 source-backed replay URLs:

```text
positive:
  https://www.s-oil.com/common/page/FileDownload.aspx?FileName=638977732335971792.pdf&PIndex=4&PathType=BOARD&TFileName=3Q+2025+S-OIL+Earnings+Release.pdf

guard:
  https://www.s-oil.com/common/page/FileDownload.aspx?FileName=638917284006185071.pdf&PIndex=4&PathType=BOARD&TFileName=2Q25++Earnings+Release+FN.pdf
```

positive fixture 의미:

```text
S-OIL Q3 2025 IR excerpt는 정제마진, 영업이익 흑자 전환, 가동률 문장을 같이 제공한다.
그래서 C17에서 spread_expansion + opm_expansion_pctp + utilization_rate를 SUPPORT로 열 수 있다.
```

guard fixture 의미:

```text
S-OIL Q2 2025 IR excerpt는 정제마진 회복 문장이 있지만,
재고/lagging 영향 때문에 영업손실이 발생한 guard 사례다.

따라서 spread_expansion만 SUPPORT로 열리고,
opm_expansion_pctp / utilization_rate / inventory_cycle positive support로 새면 안 된다.
```

쉬운 예:

```text
"정제마진이 좋아졌다"
  -> C17 조사 트리거 또는 spread primitive 가능
  -> 이것만으로 영업이익 개선 점수까지 주면 안 됨

"정제마진이 좋아졌고, 실제 영업이익이 흑자 전환했고, 가동률도 높았다"
  -> realized margin bridge가 있으므로 C17 positive primitive 가능

"정제마진은 좋아졌지만 재고/시차 영향으로 영업손실"
  -> spread-only guard
  -> margin conversion positive로 승격 금지
```

## All-Archetype Replay Matrix

`output/census_v4/2026-07-01/all_archetype_replay_matrix.json` 기준:

```text
all_archetype_replay_pass = false
archetype_count = 36
required_archetype_count = 32

source_backed_ready_count = 4
guard_replay_ready_count = 4
missing_required_archetype_count = 28

controlled_wiring_smoke_ready_count = 0
```

READY:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
C15_MATERIAL_SPREAD_SUPERCYCLE
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```

PENDING priority:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

주의:

```text
canonical output은 full_thesis_smoke_mode 없이 생성되어 controlled_wiring_smoke_ready_count = 0이다.
unit test helper는 controlled_replay mode에서 C06 smoke fixture를 별도로 켜므로 1로 보일 수 있다.

둘 다 운영 full-thesis pass가 아니다.
운영 판단에는 source-backed semantic replay와 production full-thesis path만 인정해야 한다.
```

## Controlled Semantic Replay

`output/census_v4/2026-07-01/controlled_semantic_replay_audit.json` 기준:

```text
controlled_semantic_replay_pass = false
case_count = 10
pass_count = 8
pending_count = 2
fail_count = 0

blockers:
  C24_CLINICAL_BINARY_EVENT_GUARD
  C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

PASS:

```text
C06_HBM_POSITIVE_AND_QUALIFICATION_LAG_GUARD
C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD
C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD
C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
WRONG_SUBJECT_RISK_FIXTURE
OLD_RISK_RESOLVED_FIXTURE
PROVIDER_FAILURE_PENDING_FIXTURE
SEMANTIC_CONTRACT_GUARD_FIXTURE
```

PENDING:

```text
C24_CLINICAL_BINARY_EVENT_GUARD
C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

## Goal Completion Truth

`output/census_v4/2026-07-01/goal_completion_audit.json` 기준:

```text
goal_completion_ready = false

blockers:
  brain_web_evidence_pass_false
  full_thesis_smoke_pending
  full_thesis_production_pass_false
  source_backed_replay_parity_all_archetypes_pending
  controlled_semantic_replay_pending
  goal_requirement_matrix_pass_false

brain_web_evidence_pass_allowed = false
full_thesis_production_pass_allowed = false
controlled_semantic_replay_pass_allowed = false
all_archetype_replay_pass_allowed = false
```

`output/census_v4/2026-07-01/goal_requirement_matrix_audit.json` 기준:

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

해석:

```text
C17은 닫혔다.
그러나 goal 전체는 아직 완료가 아니다.
특히 C24/C28 replay, full-thesis production, Brain/Web evidence gate가 남아 있다.
```

## 검증 기록

Targeted tests:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_all_archetype_replay_matrix \
  tests.test_census_v4_goal_required_audits -v

Ran 11 tests
OK
```

Census v4 tests:

```text
PYTHONPATH=src python -m unittest $(rg --files tests | rg 'tests/test_census_v4_.*\.py$' | sed 's#/#.#g; s#\.py$##') -v

Ran 114 tests
OK
```

Full repo test artifact:

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v

status = OK
test_count = 4995
failed_count = 0
error_count = 0
duration_seconds = 178.9812
log_sha256 = e924cbdd0595d7559a7851172d5a2263e68d8e3f870f119d2291afe50f3b5042
artifact_sha256 = 845de1c5a0d8efc49934cd86f034e95880401201674a2ec556647a40b83b6e50
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

## 다음 패치 방향

우선순위:

```text
1. C24 source-backed replay
   positive: endpoint / regulatory / partner economics / runway bridge
   guard: binary event headline만으로 Green bridge를 열지 않기

2. C28 source-backed replay
   positive: ARR / RPO / renewal / retention / churn bridge
   guard: software/security 키워드만으로 contract retention을 열지 않기

3. FULL_THESIS smoke/prod source task execution
   replay-only가 아니라 full-thesis accepted claim -> primitive -> score contribution -> StageCourt path를 닫기

4. Real Brain/Web evidence gate
   disabled ledger-refresh가 아니라 실제 planner/search/fetch/claim extraction trace를 만들기
```

하지 말아야 할 것:

```text
가중치나 Stage threshold를 먼저 고치면 안 된다.
source-backed claim 없이 점수만 올리면 90점/60점 흔들림 문제가 재발한다.
```

## 다음 에이전트 공격 질문

완료라고 주장하면 아래를 먼저 확인한다.

```text
1. FULL_THESIS row가 생겼는가? 현재 0개다.
2. FULL_E2R_100 verified score row가 생겼는가? 현재 0개다.
3. Brain/Web/LLM planner call이 canonical output에서 실제 evidence로 이어졌는가?
4. C24/C28 controlled semantic replay가 source-backed로 닫혔는가?
5. required 32개 아키타입이 모두 source-backed positive + guard ready인가? 현재 4/32다.
6. C17 spread-only guard가 realized margin positive로 새지 않았는가?
7. C08 profile-only guard가 named customer / qualification / margin bridge로 새지 않았는가?
8. C15 raw commodity headline guard가 pass-through / spread / FCF bridge로 새지 않았는가?
9. canonical output과 unit controlled smoke mode를 섞어 결론 내지 않았는가?
10. 과거 문서의 stale ready_count나 stale test_count를 최신 값으로 오해하지 않았는가?
```

## 현재 판정

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS:
  PASS

C06 source-backed replay:
  PASS

C08 source-backed replay:
  PASS

C15 source-backed replay:
  PASS

C17 source-backed replay:
  PASS

CONTROLLED_SEMANTIC_REPLAY_PASS:
  FALSE, C17 snapshot 8/10 pass
  Latest after C24 patch: FALSE, 9/10 pass

ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS:
  FALSE, C17 snapshot 4/32 ready
  Latest after C24 patch: FALSE, 5/32 ready

MEANINGFUL_OPERATIONAL_STAGE_PASS:
  FALSE

FULL_THESIS_PRODUCTION_PASS:
  FALSE

BRAIN_WEB_EVIDENCE_PASS:
  FALSE

Goal completion:
  FALSE
```

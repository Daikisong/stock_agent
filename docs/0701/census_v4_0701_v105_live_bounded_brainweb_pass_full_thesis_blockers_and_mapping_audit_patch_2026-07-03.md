# Census v4 2026-07-01 v105 Live Bounded Brain/Web Pass / FULL_THESIS Blocker / Mapping Audit Patch

작성일: 2026-07-03

대상 산출물:

```text
output/census_v4/2026-07-01-v105-live-bounded-rerun-after-extractor-retry
```

## 한 줄 결론

v105는 `Brain/Web evidence pass`까지는 처음으로 닫았다.  
하지만 `FULL_THESIS` 운영 Stage와 `FULL_E2R_100` 운영 점수는 아직 0개다.

쉽게 말하면:

```text
Brain/Web evidence pass = 일부 검사 결과가 실제 원문/claim/StageCourt trace까지 이어짐
FULL_THESIS = 최종 진단서

v105는 일부 검사 결과는 통과했다.
하지만 최종 진단서는 아직 0장이다.
```

따라서 아래 표현은 틀리다.

```text
"삼성전자 운영 Stage1이다"
"SK하이닉스 운영 Stage2다"
"v105에서 운영 점수가 나왔다"
```

정확한 표현은 이렇다.

```text
삼성전자와 SK하이닉스는 BRAIN_WEB_PARTIAL 상태 row가 있다.
둘 다 operator_stage_use = NOT_FULL_THESIS_STAGE 이다.
둘 다 full_thesis_stage = FULL_THESIS_NOT_RUN 이다.
즉 운영자가 투자 Stage로 쓰는 최종 FULL_THESIS row는 아니다.
```

## 실행 명령

v105 live bounded rerun:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-v105-live-bounded-rerun-after-extractor-retry \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider real \
  --brain-source-acquisition live_full_bounded \
  --brain-candidate-event-seed-path output/census_v4/2026-07-01-v97-seed-source/research_brain_full_thesis_seed_events.jsonl \
  --brain-universe-limit 30 \
  --brain-planner-success-limit 30 \
  --brain-planner-batch-size 5 \
  --brain-max-source-tasks-per-plan 3 \
  --brain-max-fetches-per-task 2 \
  --brain-retry-max 1 \
  --brain-claim-extractor-provider auto \
  --brain-claim-extractor-timeout-seconds 120 \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --write-operational-docs false \
  --fail-on-critical-audit false
```

주의:

```text
아래 primitive mapping audit patch와 goal audit 재계산은 v105 live fetch를 다시 돌린 것이 아니다.
기존 v105 leaf artifact를 현재 코드로 audit replay 한 것이다.
```

## 최신 verdict

`readiness_verdict.json`:

```text
verdict = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
target_gate = brain_web
target_gate_pass = true
brain_web_evidence_pass = true
meaningful_operational_stage_pass = false
full_thesis_production_pass = false
blockers = []
```

해석:

```text
target_gate=brain_web 기준은 통과했다.
하지만 goal.md/goal2.md/goal3.md의 최종 목표인 FULL_THESIS 운영 준비는 아니다.
```

`brain_web_readiness_gate_audit.json`:

```text
verdict = READY_FOR_BRAIN_WEB_EVIDENCE_PASS
blockers = []
```

`goal_completion_audit.json` 재계산 후:

```text
goal_completion_ready = false
target_gate = brain_web

blockers:
  - full_thesis_smoke_pending
  - full_thesis_smoke_execution_pending
  - full_thesis_production_pass_false
  - full_thesis_seed_promotion_pass_false
  - source_backed_replay_parity_all_archetypes_pending
  - goal_requirement_matrix_pass_false
```

`goal_requirement_matrix_audit.json` 재계산 후:

```text
required_goal_completion_pass_count = 17
required_goal_completion_pending_count = 4
required_goal_completion_fail_count = 0

pending_gate_ids:
  - FULL_THESIS_SMOKE_PASS
  - FULL_THESIS_PRODUCTION_PASS
  - FULL_THESIS_SEED_PROMOTION_PASS
  - ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
```

가장 중요한 변화:

```text
source_connector_capability_pending은 더 이상 blocker가 아니다.
primitive_state_chain도 더 이상 fail이 아니다.
남은 blocker는 전부 FULL_THESIS 운영화와 전체 아키타입 replay 쪽이다.
```

## Stage / score 분포

`census_stage_status.jsonl` 기준:

```text
total rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD      3368
  BRAIN_OFFICIAL_PARTIAL    19
  BRAIN_WEB_PARTIAL          4
  FULL_THESIS                0

score_scale:
  NO_SCORE               3321
  EVENT_WEIGHTED_PARTIAL   70
  FULL_E2R_100              0

operator_stage_use:
  NOT_FULL_THESIS_STAGE   3391

operator_score_use:
  NOT_FULL_E2R_SCORE      3391
```

`canonical_stage` 분포:

```text
0        3324
1          46
2          20
3-Red      1
```

이 숫자를 읽을 때 주의:

```text
canonical_stage 1/2/3-Red row가 있다고 해서 운영 Stage가 있다는 뜻이 아니다.
stage_scope가 FULL_THESIS가 아니고 operator_stage_use가 NOT_FULL_THESIS_STAGE이면
그 row는 상태판/부분검사 row다.
```

쉬운 예:

```text
병원 접수표에 "검사 필요"가 찍힌 것과
의사가 최종 진단서를 낸 것은 다르다.

CENSUS_EVENT_BOARD / BRAIN_*_PARTIAL은 접수표 또는 일부 검사 결과다.
FULL_THESIS가 최종 진단서다.
```

## 삼성전자 / SK하이닉스 v105 row

삼성전자 `005930`:

```text
stage_scope = BRAIN_WEB_PARTIAL
canonical_stage = 1
base_stage = 1
score_scale = EVENT_WEIGHTED_PARTIAL
score_scope = BRAIN_WEB_CLAIM_BACKED_PARTIAL
event_evidence_score = 44.1667
accepted_claim_count = 3
accepted_web_llm_claim_count = 2
accepted_official_claim_count = 1
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
stage_decision_status = FINAL
investigation_status = COMPLETE
```

SK하이닉스 `000660`:

```text
stage_scope = BRAIN_WEB_PARTIAL
canonical_stage = 2
base_stage = 2
score_scale = EVENT_WEIGHTED_PARTIAL
score_scope = BRAIN_WEB_CLAIM_BACKED_PARTIAL
event_evidence_score = 75.8333
accepted_claim_count = 6
accepted_web_llm_claim_count = 6
accepted_official_claim_count = 0
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
stage_decision_status = FINAL
investigation_status = COMPLETE
```

해석:

```text
삼성전자와 SK하이닉스는 "Stage row가 있긴 하다".
하지만 이 Stage는 운영 FULL_THESIS Stage가 아니다.

따라서 v105로 "삼성 Stage1, 하이닉스 Stage2 확정"이라고 말하면 안 된다.
정확히는 "Brain/Web partial row가 생성됐고, full thesis는 아직 미실행"이다.
```

## Brain/Web leaf counts

v105 leaf 기준:

```text
planner_runs = 300
llm_prompts = 35
llm_responses = 35
source_tasks = 327
source_task_executions = 327
evidence_documents = 171
evidence_anchors = 258
web_search_tasks = 70
web_search_results = 997
web_fetched_documents = 47
claim_extractor_runs = 47
accepted_claims = 191
score_contributions = 153
stagecourt_traces = 115
brain_to_claim_trace = 99
```

Claim extractor:

```text
claim_extractor_runs = 47
status SUCCESS = 47
provider_error = 0
timeout = 0
```

v101 계열의 blocker였던 claim extractor timeout/provider_error 5개는 v105에서 사라졌다.

## 이번 코드 패치로 닫은 audit 이슈

### 1. Source connector capability gate

이전 문제:

```text
IssuerIR 같은 source class 하나가 placeholder라는 이유로
전체 FULL_THESIS source connector capability가 pending으로 보일 수 있었다.
```

패치 후 원칙:

```text
FULL_THESIS SourceTask가 실행 가능한 대체 source path를 하나라도 가지면
그 task는 connector capability blocker가 아니다.

source class placeholder 여부와
source task 실행 가능 여부를 분리한다.
```

재계산 결과:

```text
source_connector_capability_audit:
  verdict = SOURCE_CONNECTOR_CAPABILITY_PASS
  source_connector_capability_pass_allowed = true
  blocking_full_thesis_source_classes = []
  non_executable_full_thesis_source_classes = ["IssuerIR"]
```

해석:

```text
IssuerIR 자체는 아직 placeholder다.
하지만 해당 FULL_THESIS task들이 DART/KIND/ReportPDF/TrustedNews 같은 실행 가능한 경로도 갖고 있으면
전체 source connector gate를 막지는 않는다.
```

### 2. Goal matrix leaf audit wiring

이전 문제:

```text
goal_requirement_matrix_audit 재계산 시 실제 leaf_artifact_audit.json을 넘기지 않아
이미 PASS인 anti-fake/atomic/score-scale 계열 gate가 pending처럼 보일 수 있었다.
```

패치 후:

```text
_write_goal_v4_audits가 output_root/leaf_artifact_audit.json을 읽어
_goal_requirement_matrix_audit에 전달한다.
```

### 3. Primitive state multi-mapping audit

이전 문제:

```text
accepted_claims.jsonl은 claim_id compatibility view다.
같은 claim_id가 여러 accepted primitive mapping을 가질 수 있는데,
merge 후 대표 primitive_id 하나만 남을 수 있다.

그 상태에서 primitive_state_chain_audit가 accepted_claims.primitive_id 하나만 보면
정상 다중 mapping을 primitive mismatch로 오판할 수 있다.
```

실제 v105 예:

```text
claim_id = CLM-8ddce9e969f82ee7e85b
accepted mapping 1 = delivery_schedule
accepted mapping 2 = contract_duration_months

accepted_claims.jsonl 대표 primitive_id = delivery_schedule
primitive_states.jsonl state primitive_id = contract_duration_months
```

이건 무조건 오류가 아니다.

```text
같은 공시 문장이 납기 일정도 말하고, 계약 기간/수행 기간도 말할 수 있다.
중요한 것은 state primitive가 해당 claim의 accepted mapping ledger 안에 있느냐이다.
```

패치 후 원칙:

```text
PrimitiveState.primitive_id는 해당 claim의 accepted primitive mapping row 중 하나와 맞으면 통과한다.
accepted_claims.jsonl 단일 primitive_id만 맞아야 한다고 보지 않는다.
brain_claim_mapping_trace.jsonl의 accepted mapping ledger를 같이 본다.

단, 너무 느슨하게 보지 않는다.

```text
brain_claim_mapping_trace.accepted_primitive_ids는 task/execution 단위 summary다.
따라서 그 목록만으로 PrimitiveState.primitive_id를 통과시키지 않는다.

Brain trace가 있는 claim은 아래 4개가 직접 닫혀야 한다.

claim_id
+ primitive_state_id
+ symbol
+ trace row primitive_id
```

쉬운 예:

```text
"가능한 검사 항목 목록"에 혈액검사가 있다고 해서
그 환자가 실제 혈액검사를 완료한 것은 아니다.

실제 완료 판정은 해당 환자, 해당 검사 ID, 해당 결과 row가 직접 이어질 때만 가능하다.
```
```

그렇다고 느슨하게 통과시키지는 않는다.

```text
accepted mapping ledger 어디에도 없는 primitive로 PrimitiveState를 만들면 여전히 FAIL이다.
```

재계산 결과:

```text
primitive_state_chain_audit:
  verdict = PASS
  critical_count = 0
  claim_with_multi_accepted_primitive_count = 3
```

테스트:

```text
test_multi_mapping_claim_can_support_each_accepted_primitive_state = OK
test_state_primitive_without_accepted_mapping_still_fails = OK
test_accepted_primitive_summary_does_not_prove_state_mapping = OK
test_brain_mapping_trace_must_reference_same_primitive_state_id = OK
test_brain_mapping_trace_symbol_must_match_state_symbol = OK
```

## 검증

Focused tests:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_primitive_state_chain \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_brain_stage_promotion_gate -v

Ran 30 tests
OK
```

Full unittest artifact:

```text
artifact = output/census_v4/2026-07-01-v105-live-bounded-rerun-after-extractor-retry/test_result_artifact.json
log = output/census_v4/2026-07-01-v105-live-bounded-rerun-after-extractor-retry/test_result_full_unittest.log

status = OK
test_count = 5139
failed_count = 0
error_count = 0
duration_seconds = 231.2116
```

## 교차검증 반영

별도 검토에서 받은 지적:

```text
accepted_claims.jsonl 단일 primitive_id 오탐을 줄이는 방향은 맞다.
하지만 brain_claim_mapping_trace.accepted_primitive_ids까지 proof로 쓰면 너무 넓다.
accepted_primitive_ids는 task/execution summary일 수 있으므로 hard guard에는 쓰면 안 된다.
```

반영한 최종 guard:

```text
1. accepted_primitive_ids는 primitive_state_chain_audit proof에서 제외한다.
2. Brain trace가 있는 claim은 claim_id + primitive_state_id + symbol + trace row primitive_id가 직접 맞아야 한다.
3. trace row가 같은 primitive_id를 말해도 primitive_state_id가 다르면 FAIL이다.
4. trace row가 같은 primitive_state_id를 말해도 symbol이 다르면 FAIL이다.
5. accepted mapping set이 비어 있거나 state primitive가 accepted mapping row 어디에도 없으면 FAIL이다.
```

추가 회귀 테스트:

```text
test_accepted_primitive_summary_does_not_prove_state_mapping = OK
test_brain_mapping_trace_must_reference_same_primitive_state_id = OK
test_brain_mapping_trace_symbol_must_match_state_symbol = OK
```

## 현재 남은 진짜 blocker

### Blocker 1. FULL_THESIS smoke가 아직 pending

현재 상태:

```text
FULL_THESIS_SMOKE_PASS = pending
full_thesis_smoke_pending
full_thesis_smoke_execution_pending
```

의미:

```text
삼성전자/하이닉스 같은 대표 종목에 대해
EvidenceClaim -> PrimitiveState -> ScoreContribution -> ScoreInterval -> StageCourt -> FULL_THESIS row
까지 닫힌 smoke가 없다.
```

쉬운 예:

```text
지금은 혈액검사 일부 결과표가 있다.
하지만 의사가 모든 검사 결과를 묶어 최종 진단서를 쓰는 단계가 아직 안 돈 것이다.
```

### Blocker 2. FULL_THESIS production pass false

현재 상태:

```text
FULL_THESIS_PRODUCTION_PASS = pending
full_thesis_production_pass_false
FULL_THESIS stage rows = 0
FULL_E2R_100 score rows = 0
```

의미:

```text
Production daily mode에서 운영자가 쓸 수 있는 full thesis score/stage row가 아직 생성되지 않는다.
```

### Blocker 3. FULL_THESIS seed promotion false

현재 상태:

```text
FULL_THESIS_SEED_PROMOTION_PASS = pending
full_thesis_seed_promotion_pass_false
```

의미:

```text
full thesis refresh queue / seed event가 실제 FULL_THESIS row로 승격되는 끝단이 아직 닫히지 않았다.
```

### Blocker 4. All-archetype source-backed replay pending

현재 상태:

```text
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS = pending
source_backed_replay_parity_all_archetypes_pending
```

의미:

```text
모든 아키타입에서 source-backed fixture가
문서 -> claim -> primitive -> score contribution -> stage
까지 닫히는 replay가 아직 아니다.
```

주의:

```text
source_proxy_only 연구자료는 운영 점수 정답 fixture가 아니다.
실제 URL/source anchor가 있는 fixture만 replay parity로 인정해야 한다.
```

## 다음 패치 방향

### P0. FULL_THESIS smoke runner를 실제 실행 경로로 닫기

필요한 산출물:

```text
full_thesis_stage_row_count > 0
full_e2r_verified_score_present_count > 0
score_scale = FULL_E2R_100
operator_stage_use = FULL_THESIS_STAGE
operator_score_use = FULL_E2R_SCORE
```

단, 억지 승격은 금지한다.

```text
BRAIN_WEB_PARTIAL row를 FULL_THESIS로 이름만 바꾸면 안 된다.
```

필수 chain:

```text
FULL_THESIS seed event
-> bounded official-first SourceTask
-> EvidenceDocument / EvidenceAnchor
-> accepted EvidenceClaim
-> accepted PrimitiveMapping
-> PrimitiveState
-> ScoreContribution
-> ScoreInterval
-> StageCourt
-> census_stage_status FULL_THESIS row
```

### P1. Seed promotion failure를 trace로 분해

현재 문서화해야 할 질문:

```text
seed event는 만들어졌는가?
planner는 seed event를 받았는가?
source task는 실행됐는가?
accepted claim은 생겼는가?
primitive coverage가 Green/Yellow gate에 충분한가?
score interval lower/upper가 stage materiality를 닫는가?
StageCourt가 FULL_THESIS promotion을 허용했는가?
```

다음 패치에서는 위 질문마다 leaf artifact를 남겨야 한다.

### P2. All-archetype replay를 source-backed 기준으로 재정의

아키타입별로 아래 상태를 명시해야 한다.

```text
SOURCE_BACKED_REPLAY_PASS
SOURCE_BACKED_REPLAY_FAIL
SOURCE_BACKED_FIXTURE_MISSING
SOURCE_PROXY_ONLY_NOT_SCORE_FIXTURE
```

목표:

```text
C01~C36 전체가 source-backed replay pass이거나,
아직 source-backed fixture가 없다는 unsupported/source-gap 상태로 정직하게 표시되어야 한다.
```

### P3. Multi-mapping claim ledger를 compatibility view 밖으로 승격

이번 patch는 audit 오판을 막았다.
하지만 근본적으로는 `accepted_claims.jsonl` 단일 `primitive_id`가 다중 mapping claim을 표현하기 부족하다.

다음 구조가 더 낫다.

```text
accepted_claims.jsonl:
  claim 자체의 entity/date/polarity/currentness

accepted_claim_mappings.jsonl:
  claim_id
  mapping_id
  primitive_id
  mapping_status
  support_direction
  source_task_id
  satisfies_source_task
```

그러면 `accepted_claims.jsonl`에 어떤 representative primitive가 남았는지로 audit가 흔들리지 않는다.

## 외부 리뷰어 공격 체크리스트

다음 질문을 일부러 세게 던져야 한다.

```text
1. BRAIN_WEB_PARTIAL을 FULL_THESIS처럼 표현한 문구가 남아 있는가?
2. event_evidence_score를 full E2R score처럼 읽게 하는 필드명이 남아 있는가?
3. 삼성전자/하이닉스 partial row를 운영 Stage라고 말한 곳이 있는가?
4. source_connector PASS가 IssuerIR 구현 완료처럼 오해되지 않는가?
5. primitive_state_chain PASS가 모든 primitive semantics 검증 완료처럼 과장되지 않는가?
6. same claim multi-mapping이 정당한 경우와 과잉 mapping인 경우를 구분하는 테스트가 더 필요한가?
7. FULL_THESIS seed가 실제 StageCourt까지 갔는지, 아니면 planning-only인지 leaf로 증명되는가?
8. all-archetype replay에서 source_proxy_only가 정답 fixture로 섞이지 않는가?
9. Provider/source pending이 낮은 점수 확정으로 바뀌는 경로가 남아 있는가?
10. Stage3-Red/4B/4C가 prior thesis 없이 transition overlay처럼 쓰이는 경로가 남아 있는가?
```

## 최종 판단

v105는 중요한 진전이다.

```text
Brain/Web real path:
  planner -> source task -> web/official fetch -> claim extractor -> accepted claim -> StageCourt trace
  이 경로는 pass했다.

Extractor timeout/provider_error:
  v101의 5건 blocker는 v105에서 0건이 됐다.

Primitive/source connector audit:
  오판성 blocker는 제거했다.
```

하지만 아직 운영 완성은 아니다.

```text
FULL_THESIS row = 0
FULL_E2R_100 score row = 0
operator_stage_use FULL_THESIS_STAGE = 0
all-archetype source-backed replay = pending
```

따라서 다음 에이전트의 목표는 Brain/Web pass를 다시 증명하는 것이 아니라,
`BRAIN_WEB_PARTIAL`에서 멈춘 evidence chain을 `FULL_THESIS` 운영 row까지 닫는 것이다.

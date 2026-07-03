# Census v4 v87 - Stage는 있으나 운영 Stage는 아직 0개인 상태 교차검증

작성일: 2026-07-03

목적: 사용자의 질문인 "뭔가 잘못되고 있는 거 맞지? stage가 있는 애들이 있긴 해?"에 대해, 현재 산출물을 다시 확인하고 다음 에이전트가 강하게 피드백할 수 있도록 근거와 패치 방향을 남긴다.

## 결론

Stage row 자체는 있다. 다만 지금 있는 Stage row는 운영 full-thesis Stage가 아니다.

쉽게 말하면:

```text
출석부는 전 종목에 붙었다.
일부 종목에는 "공시/이벤트가 있으니 더 봐야 함" 메모도 붙었다.
하지만 종목별 투자논리 전체 답안지(FULL_THESIS_100점)는 아직 한 장도 완성되지 않았다.
```

현재 검증 산출물 기준:

```text
stage row = 3,391개
non-Stage0 표시 = 85개
FULL_THESIS row = 0개
BRAIN_WEB_PARTIAL row = 0개
FULL_E2R_100 verified score row = 0개
meaningful_operational_stage_pass = false
brain_web_evidence_pass = false
full_thesis_production_pass = false
all_archetype_replay_pass = false
```

따라서 지금 상태를 "Stage가 전혀 없다"고 말하면 틀리고, "운영 Stage가 있다"고 말해도 틀리다. 정확한 표현은:

```text
Census event-board Stage/status는 있다.
운영 FULL_THESIS/FULL_E2R Stage는 아직 없다.
```

## 검증한 산출물

이번 문서는 다음 산출물을 직접 교차 확인했다.

```text
output/test_census_v4_verified_full_tests/readiness_verdict.json
output/test_census_v4_verified_full_tests/census_stage_map.jsonl
output/test_census_v4_verified_full_tests/leaf_artifact_audit.json
output/test_census_v4_verified_full_tests/source_task_realness_audit.json
output/test_census_v4_verified_full_tests/source_task_satisfaction_audit.json
output/test_census_v4_verified_full_tests/brain_web_readiness_gate_audit.json
output/test_census_v4_verified_full_tests/runtime_plausibility_audit.json
output/test_census_v4_verified_full_tests/full_thesis_production_audit.json
output/test_census_v4_verified_full_tests/full_thesis_production_runner_audit.json
output/test_census_v4_verified_full_tests/samsung_hynix_full_thesis_smoke.json
output/test_census_v4_verified_full_tests/all_archetype_replay_matrix.json
output/test_census_v4_verified_full_tests/controlled_semantic_replay_audit.json

output/census_v4/2026-07-01/census_stage_map.jsonl
output/census_v4/2026-07-01/readiness_verdict.json
```

추가로 코드 근거를 확인했다.

```text
src/e2r/census/census_runner_v4.py:2083
src/e2r/census/census_runner_v4.py:2459
src/e2r/census/census_runner_v4.py:7208
src/e2r/production/source_connectors/issuer_ir_connector.py:1
src/e2r/production/source_connectors/trusted_news_connector.py:1
src/e2r/production/source_connectors/source_provider_registry.py:188
```

## 숫자 검증

`output/test_census_v4_verified_full_tests/census_stage_map.jsonl` 기준:

| 항목 | 값 | 의미 |
| --- | ---: | --- |
| 전체 stage map row | 3,391 | 전체 universe 상태판 row |
| Stage0 | 3,306 | 현재 촉매 없음 또는 score 없음 |
| Stage1 | 54 | event-board watch 수준 |
| Stage2-Watch | 30 | canonical Stage2 확정이 아니라 material claim watch |
| Red | 1 | risk review 표시 |
| stage_scope=CENSUS_EVENT_BOARD | 3,391 | 전부 event-board scope |
| stage_scope=FULL_THESIS | 0 | 운영 full thesis row 없음 |
| stage_scope=BRAIN_WEB_PARTIAL | 0 | 이번 ledger-refresh 출력에는 partial도 없음 |
| operator_stage_use=NOT_FULL_THESIS_STAGE | 3,391 | 운영 Stage로 쓰지 말라는 표시 |
| score_scale=EVENT_WEIGHTED_PARTIAL | 67 | 부분 이벤트 점수 |
| score_scale=NO_SCORE | 3,324 | full score 없음 |
| full_e2r_verified_score row | 0 | 100점 운영 E2R 점수 없음 |

`output/census_v4/2026-07-01/census_stage_map.jsonl`도 같은 분포였다.

```text
stage_scope = CENSUS_EVENT_BOARD 3,391
FULL_THESIS = 0
BRAIN_WEB_PARTIAL = 0
full_e2r_verified_score row = 0
```

주의: 기존 `docs/0701/README.md`에는 v82 bounded live 기준으로 `BRAIN_WEB_PARTIAL 1개`가 기록되어 있다. 이번 v86/v87 검증 산출물은 `LEDGER_REFRESH_CENSUS` 계열이라 Brain/Web이 disabled 상태이고, 그래서 `BRAIN_WEB_PARTIAL 0개`다. 두 결과의 공통 결론은 같다.

```text
v82 bounded live: BRAIN_WEB_PARTIAL 1개, FULL_THESIS 0개
v86/v87 verified full tests: BRAIN_WEB_PARTIAL 0개, FULL_THESIS 0개

둘 다 운영 FULL_THESIS Stage는 0개다.
```

## Readiness 판정

`readiness_verdict.json` 기준:

```text
verdict = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
meaningful_operational_stage_pass = false
brain_web_evidence_pass = false
full_thesis_production_pass = false
all_archetype_replay_pass = false
target_gate = anti_fake
target_gate_pass = true
```

이건 좋은 pass와 나쁜 pass를 분리한 결과다.

좋은 점:

```text
ANTI_FAKE는 통과했다.
즉 claim 없는 nonzero 점수, source_proxy score, provider failure final score 같은 가짜 Stage는 막고 있다.
```

아직 안 된 점:

```text
MEANINGFUL_OPERATIONAL_STAGE는 false다.
즉 실제 운영에서 "이 종목은 Stage2/Green/Yellow"라고 말할 수 있는 full-thesis 경로는 닫히지 않았다.
```

`remaining_operational_gaps`는 다음을 직접 말한다.

```text
full thesis EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt path not run
source-backed replay parity across all archetypes is not proven
goal3 controlled semantic replay cases are not all source-backed and lifecycle-clean
Brain/Web/LLM acquisition artifacts are not produced in this disabled ledger-refresh run
Research Brain v4 imported report bundle is shadow/import-only and not admissible as Census production cutover evidence
```

## 왜 Stage2-Watch 30개가 운영 Stage2가 아닌가

예시:

```text
001470 삼부토건:
base_stage = Stage2-Watch
stage_signal = MATERIAL_CLAIM_WATCH
score_scale = EVENT_WEIGHTED_PARTIAL
full_thesis_stage = FULL_THESIS_NOT_RUN
operator_stage_use = NOT_FULL_THESIS_STAGE
```

이건 "공시/이벤트 상으로 더 봐야 하는 후보"라는 뜻이지, "E2R full thesis에서 Stage2가 확정됐다"는 뜻이 아니다.

쉬운 예:

```text
학교에서 "이 학생 숙제 검사 필요"라고 표시한 것과
"시험 100점 만점에 87점"은 다르다.

Stage2-Watch는 검사 필요 메모에 가깝고,
FULL_THESIS/FULL_E2R_100이 진짜 시험 점수다.
```

## 삼성전자/하이닉스 질문에 대한 현재 답

`census_stage_map.jsonl` 샘플:

```text
000660 SK하이닉스:
stage_scope = CENSUS_EVENT_BOARD
base_stage = Stage1
stage_signal = OFFICIAL_EVENT_WATCH
score_scale = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.0
full_thesis_stage = FULL_THESIS_NOT_RUN
full_e2r_verified_score = null
operator_stage_use = NOT_FULL_THESIS_STAGE
```

이번 산출물에서 삼성전자/하이닉스 C06/HBM full thesis 점수는 없다.

`samsung_hynix_full_thesis_smoke.json`:

```text
verdict = PENDING_FULL_THESIS_REFRESH
full_thesis_status = PENDING_FULL_THESIS_REFRESH
```

따라서 삼성전자/하이닉스를 놓고 "현재 운영 파이프라인에서 Stage 몇 점이냐"라고 물으면, 현재 정직한 답은:

```text
운영 FULL_THESIS로는 아직 계산되지 않았다.
event-board에서는 일부 공시/이벤트 watch 상태만 있다.
```

이걸 60점, 90점, Green/Yellow로 말하면 다시 같은 혼란이 생긴다.

## Source task chain이 닫혔다는 말의 한계

`source_task_satisfaction_audit.json`은 다음처럼 좋아 보인다.

```text
verdict = PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
source_task_execution_count = 92
representative_score_claim_count = 67
source_task_chain_closed_to_representative_stage_count = 67
critical_count = 0
```

하지만 scope가 중요하다.

```text
verdict_scope = LEDGER_REFRESH_SOURCE_TASK_SATISFACTION_PASS
live_source_task_satisfaction_pass_allowed = false
```

즉 이 감사는 "기존 ledger-refresh 이벤트 보드의 id chain이 끊기지 않았다"는 뜻이다. live production source acquisition이 성공했다는 뜻이 아니다.

쉬운 예:

```text
기존 창고에 있던 서류 67장의 문서번호-청구서번호-검토표번호가 서로 맞는지는 확인했다.
하지만 오늘 새로 거래처에 전화해서 최신 원본을 받아온 것은 아니다.
```

## Source task realness도 live pass가 아니다

`source_task_realness_audit.json`:

```text
verdict = PASS_LEDGER_REFRESH_REALNESS
source_task_execution_count = 92
source_task_claim_producing_count = 60
source_task_fresh_provider_cache_count = 60
source_task_lifecycle_refresh_count = 32
source_task_real_fetch_count = 0
live_source_pass_allowed = false
```

이건 "ledger-refresh로 claim-producing chain을 재사용했다"는 뜻이다. live provider fetch가 있었다는 뜻은 아니다.

현재 source task origin도 전부:

```text
source_task_execution_origin = production_cutover_v3_leaf_artifact 92개
```

planner/web/extractor 쪽은:

```text
planner_runs = 0
claim_extractor_runs = 0
web_search_tasks = 0
web_fetched_documents = 0
```

## Brain/Web gate

`brain_web_readiness_gate_audit.json`:

```text
verdict = NOT_REQUESTED
brain_web_evidence_pass_allowed = false
llm_planner_call_count = 0
web_search_task_count = 0
web_search_call_count = 0
web_fetched_document_count = 0
llm_claim_extractor_attempt_count = 0
web_or_llm_accepted_claim_count = 0
source_task_execution_count = 0
```

중요한 점:

```text
NOT_REQUESTED는 PASS가 아니다.
NOT_REQUESTED는 "이번 run에서 Brain/Web을 켜지 않았고, 켰다고 거짓말하지 않았다"는 honesty 상태다.
```

## 코드 근거

### 1. readiness가 운영 gap을 직접 만든다

`src/e2r/census/census_runner_v4.py:2083`의 `_readiness_verdict`는 다음 조건을 본다.

```text
full_thesis_stage_row_count
full_e2r_verified_score_row_count
event_board_non_stage0_count
full_thesis_refresh_queue_candidate_count
brain_web_requested
brain_web_pass
full_thesis_production_pass
all_archetype_replay_pass
```

그리고 full thesis 실행이 없으면 다음 gap을 넣는다.

```text
full thesis EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt path not run
event-board non-Stage0 rows exist but are not operational full-thesis stages
```

이 코드의 의미는 맞다. 문제는 pass가 아니라 기능 미완료다.

### 2. source_task_satisfaction은 ledger-refresh scope로 제한된다

`src/e2r/census/census_runner_v4.py:2459`의 `_source_task_satisfaction_audit`는 id chain을 검사한다.

검사하는 chain:

```text
SourceTaskExecution
-> accepted_claim
-> EvidenceDocument
-> EvidenceAnchor
-> ScoreContribution
-> StageCourt trace
-> representative census_stage_status row
```

하지만 반환값은 다음을 명시한다.

```text
verdict_scope = LEDGER_REFRESH_SOURCE_TASK_SATISFACTION_PASS
live_source_task_satisfaction_pass_allowed = false
```

따라서 이 PASS를 live/operational pass로 읽으면 안 된다.

### 3. Brain/Web gate는 disabled를 pass로 취급하지 않는다

`src/e2r/census/census_runner_v4.py:7208`의 Brain/Web readiness gate는 `requested=false`면:

```text
verdict = NOT_REQUESTED
brain_web_evidence_pass_allowed = false
rule = NOT_REQUESTED is not Brain/Web PASS
```

이 코드도 방향은 맞다.

### 4. IR/TrustedNews connector는 아직 placeholder다

`src/e2r/production/source_connectors/issuer_ir_connector.py:1`:

```text
Issuer IR connector placeholder with explicit provider failure
```

`src/e2r/production/source_connectors/trusted_news_connector.py:1`:

```text
Trusted-news fallback connector placeholder with explicit provider failure
```

둘 다 live mode에서 `PROVIDER_FAILED`를 반환한다.

기본 registry에는 이 둘이 포함되어 있다.

```text
src/e2r/production/source_connectors/source_provider_registry.py:188
OpenDART, KIND, KRX, CompanyGuide, IssuerIR, TrustedNews
```

따라서 full thesis가 IR/뉴스/리포트/회사 newsroom claim을 요구하면 지금은 실제 운영 claim 생성까지 닫히지 않는다.

## 지금 "잘못되고 있는" 부분

정확히 말하면 두 층이 있다.

### 고쳐진 부분

현재 코드는 적어도 event-board를 운영 Stage처럼 과장하지 않게 막고 있다.

```text
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
meaningful_operational_stage_pass = false
```

이건 좋은 방향이다.

### 아직 잘못된 또는 미완성인 부분

아래는 아직 실제 제품 관점에서 못 쓴다.

```text
1. FULL_THESIS production runner가 실제 row를 만들지 못한다.
2. Brain/Web/LLM acquisition이 disabled 또는 NOT_REQUESTED 상태다.
3. live provider fetch가 0개다.
4. source task satisfaction은 ledger-refresh scope에 머문다.
5. C01~C36 전체 source-backed replay parity가 없다.
6. goal3 controlled semantic replay 6개 핵심 guard가 source-backed/lifecycle-clean 상태가 아니다.
7. 삼성전자/하이닉스 C06/HBM full thesis smoke는 pending이다.
```

즉 "가짜 pass 방지"는 발전했지만, "실제 운영 Stage 생성"은 아직 시작점에 가깝다.

## 다음 에이전트가 공격해야 할 포인트

다음 에이전트는 아래 질문으로 이 문서를 검증하면 된다.

1. `census_stage_map.jsonl`에서 `stage_scope=FULL_THESIS` row가 1개라도 있는가?
2. `full_e2r_verified_score`가 null이 아닌 row가 있는가?
3. `operator_stage_use=FULL_THESIS_STAGE` row가 있는가?
4. Brain/Web gate가 `READY_FOR_BRAIN_WEB_EVIDENCE_PASS`인가, 아니면 `NOT_REQUESTED/BLOCKED`인가?
5. `source_task_real_fetch_count`가 0보다 큰가?
6. source task origin이 실제 live source acquisition인가, `production_cutover_v3_leaf_artifact`인가?
7. `planner_runs`, `claim_extractor_runs`, `web_fetched_documents`가 0보다 큰가?
8. full thesis production audit가 `FULL_THESIS_PRODUCTION_PASS`인가?
9. 삼성전자/하이닉스 smoke가 `FULL_THESIS_REFRESH_RAN`이고 per-symbol StageCourt까지 닫혔는가?
10. all-archetype replay matrix가 32/32 source-backed pass인가?

현재 답은 전부 운영 ready 쪽이 아니다.

## 패치 방향

Green gate 완화, 점수 가중치 조정, 삼성전자/하이닉스 예외처리는 답이 아니다.

다음 패치는 아래 순서가 맞다.

### P0. Full thesis production path를 실제 실행 경로로 닫기

목표:

```text
full_thesis_refresh_queue
-> Research Brain planner
-> bounded official-first SourceTask
-> fetched EvidenceDocument/EvidenceAnchor
-> contract-blind claim extraction
-> target/temporal adjudication
-> primitive mapping
-> ScoreContribution
-> StageCourt
-> stage_scope=FULL_THESIS row
```

완료 조건:

```text
full_thesis_production_pass = true
FULL_THESIS row > 0
full_e2r_verified_score row > 0
operator_stage_use=FULL_THESIS_STAGE row > 0
```

쉬운 예:

```text
하이닉스 HBM을 보려면 "최근 공시 하나"가 아니라
고객 배정, capacity sold-out, shipment/revenue mix, FCF/revision bridge를
각각 source-backed claim으로 채운 뒤 StageCourt로 보내야 한다.
```

### P1. Placeholder connector capability를 readiness blocker로 명시하기

현재 IR/TrustedNews는 placeholder다. 이 자체는 정직하게 provider failure를 내므로 나쁜 구현은 아니다. 하지만 다음 문서/감사에서는 이걸 더 명확히 보여야 한다.

추가해야 할 audit:

```text
source_connector_capability_audit.json
```

필수 필드:

```text
provider_name
source_class
capability_status:
  LIVE_FETCH_CAPABLE
  SNAPSHOT_ONLY
  PLACEHOLDER_PROVIDER_FAILED
  LOCAL_CACHE_ONLY
  NOT_CONFIGURED
required_by_full_thesis_task_count
blocking_full_thesis_task_count
```

완료 조건:

```text
full thesis가 필요한 source class가 PLACEHOLDER_PROVIDER_FAILED이면
READY_FOR_FULL_THESIS_OPERATION 금지
```

### P2. Brain/Web를 켜는 run과 ledger-refresh run을 분리해서 비교하기

현재 `output/test_census_v4_verified_full_tests`는 ledger-refresh honesty 검증이다. 이 산출물로 live Brain/Web 성공을 주장하면 안 된다.

필요한 산출물:

```text
output/census_v4/<date>-full-thesis-production-live/
```

이 산출물은 최소한:

```text
planner_runs > 0
source_task_executions > 0
evidence_documents > 0
claim_extractor_runs > 0 또는 structured official extractor accepted claims > 0
score_contributions > 0
stagecourt_traces > 0
FULL_THESIS rows > 0
```

를 가져야 한다.

### P3. Source-backed replay를 전 아키타입으로 확장

현재 all-archetype replay는 pass가 아니다.

```text
all_archetype_replay_pass = false
blocker = source_backed_replay_parity_all_archetypes_pending
```

다음 목표:

```text
C01~C36 각 아키타입에 source-backed positive/guard replay가 있거나,
명시적으로 unsupported/source-gap 상태를 둔다.
```

중요:

```text
source_proxy_only 연구자료는 replay 정답으로 쓰지 않는다.
직접 URL/anchor가 있는 원문 snapshot만 운영 replay 정답으로 쓴다.
```

### P4. Controlled semantic replay 6개 guard를 source-backed/lifecycle-clean으로 닫기

현재 blocker:

```text
C06_HBM_POSITIVE_AND_QUALIFICATION_LAG_GUARD
C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD
C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD
C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
C24_CLINICAL_BINARY_EVENT_GUARD
C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

이 guard들은 단순 테스트 문장이 아니라, 운영 사고를 막는 핵심 경계다.

예:

```text
C15에서 원자재 가격 상승 기사만 보고 spread/margin 점수를 주면 안 된다.
issuer-level 판가 전가와 realized margin bridge claim이 있어야 한다.
```

### P5. 삼성전자/하이닉스 smoke를 "점수 산출"이 아니라 "pending이면 pending"으로 유지

다음 실행에서 삼성전자/하이닉스가 다시 60점/90점으로 흔들리면 실패다.

정상 출력은 둘 중 하나여야 한다.

```text
1. source-backed full thesis가 모두 닫힘
   -> verified_score / score_interval / StageCourt / missing primitive / claim ids 출력

2. source-backed full thesis가 안 닫힘
   -> PENDING_FULL_THESIS_REFRESH 또는 PROVIDER/SOURCE_PENDING
   -> raw 참고점수로 운영 Stage 확정 금지
```

## 다음 패치 acceptance

다음 패치가 끝났다고 말하려면 최소한 아래가 필요하다.

```text
1. source_connector_capability_audit가 존재한다.
2. placeholder connector가 full thesis task를 막는지 readiness에 드러난다.
3. ledger-refresh PASS와 live-source PASS가 label에서 섞이지 않는다.
4. full thesis production runner가 NOT_REQUESTED가 아니거나, NOT_REQUESTED라면 운영 ready를 절대 주장하지 않는다.
5. FULL_THESIS row가 생긴 경우:
   - source_task_execution_id
   - accepted_claim_id
   - document_id
   - anchor_id
   - score_contribution_id
   - stagecourt_trace_id
   전부 같은 representative decision으로 연결된다.
6. FULL_THESIS row가 0개라면:
   - final answer는 "운영 Stage 없음"이라고 말한다.
   - event-board Stage 숫자를 운영 Stage로 보여주지 않는다.
```

## 최종 판정

현재 상태는:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS = true
MEANINGFUL_OPERATIONAL_STAGE_PASS = false
READY_FOR_FULL_THESIS_OPERATION = false
```

다시 쉬운 말로:

```text
가짜 점수 방지용 전체 상태판은 있다.
진짜 운영 Stage 엔진은 아직 full thesis source acquisition부터 StageCourt까지 닫히지 않았다.
```

이 문서를 읽는 다음 에이전트는 "Stage row가 85개 있으니 됐다"라고 하면 안 된다. 반대로 "아무것도 없다"라고 해도 안 된다. 지금 필요한 패치는 Stage 이름을 바꾸는 것이 아니라, full thesis source-backed evidence chain을 실제로 만들고 그 전까지는 pending을 유지하는 것이다.

# Census v4 2026-07-01 v106 Stage Existence / FULL_THESIS Gap Cross Review

작성일: 2026-07-03

대상 산출물:

```text
output/census_v4/2026-07-01-v105-live-bounded-rerun-after-extractor-retry
```

관련 코드 패치:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_stage_promotion_gate.py
```

## 결론

Stage가 아예 없는 것은 아니다.

하지만 운영자가 투자 Stage로 쓸 수 있는 `FULL_THESIS` Stage는 아직 0개다.

쉽게 말하면:

```text
CENSUS_EVENT_BOARD = 전 종목 상태판 / 접수표
BRAIN_OFFICIAL_PARTIAL = 공식자료 일부 검사 결과
BRAIN_WEB_PARTIAL = 웹/LLM 일부 검사 결과
FULL_THESIS = 최종 진단서

v105에는 접수표와 일부 검사 결과는 있다.
최종 진단서는 아직 0장이다.
```

따라서 아래 표현은 틀리다.

```text
"삼성전자 운영 Stage1 확정"
"SK하이닉스 운영 Stage2 확정"
"v105에서 FULL_E2R_100 점수가 나왔다"
```

정확한 표현은 이렇다.

```text
삼성전자와 SK하이닉스는 BRAIN_WEB_PARTIAL 상태 row가 있다.
둘 다 operator_stage_use = NOT_FULL_THESIS_STAGE 이다.
둘 다 full_thesis_stage = FULL_THESIS_NOT_RUN 이다.
```

## 직접 재검산한 Stage 분포

`census_stage_map.jsonl` 직접 집계:

```text
total_rows = 3391

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

FULL_THESIS row = 0
FULL_E2R_100 row = 0
FULL_THESIS_STAGE operator row = 0
```

`canonical_stage` 분포:

```text
0        3324
1          46
2          20
3-Red       1
```

중요한 해석:

```text
canonical_stage 1/2/3-Red가 있다고 해서 운영 Stage가 있다는 뜻이 아니다.
stage_scope가 FULL_THESIS가 아니고 operator_stage_use가 NOT_FULL_THESIS_STAGE이면
그 row는 최종 투자 Stage가 아니라 상태판 또는 부분검사 row다.
```

## 삼성전자 / SK하이닉스 현재 상태

삼성전자 `005930`:

```text
stage_scope = BRAIN_WEB_PARTIAL
canonical_stage = 1
event_evidence_score = 44.1667
score_scale = EVENT_WEIGHTED_PARTIAL
operator_stage_use = NOT_FULL_THESIS_STAGE
full_thesis_stage = FULL_THESIS_NOT_RUN
accepted_claim_count = 3
accepted_web_llm_claim_count = 2
accepted_official_claim_count = 1
```

SK하이닉스 `000660`:

```text
stage_scope = BRAIN_WEB_PARTIAL
canonical_stage = 2
event_evidence_score = 75.8333
score_scale = EVENT_WEIGHTED_PARTIAL
operator_stage_use = NOT_FULL_THESIS_STAGE
full_thesis_stage = FULL_THESIS_NOT_RUN
accepted_claim_count = 6
accepted_web_llm_claim_count = 6
accepted_official_claim_count = 0
```

쉬운 예:

```text
하이닉스는 검사 결과가 삼성보다 많이 쌓여서 partial score가 높다.
하지만 "최종 진단서"에 해당하는 FULL_THESIS row는 둘 다 없다.
```

## v105가 실제로 통과한 것

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

`brain_web_readiness_gate_audit.json`:

```text
verdict = READY_FOR_BRAIN_WEB_EVIDENCE_PASS
blockers = []
```

Brain/Web leaf count:

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
brain_claim_mapping_trace = 1319
```

이 숫자가 의미하는 것:

```text
이번에는 "LLM/웹이 하나도 안 돈 것"은 아니다.
실제 planner, web search, fetch, extractor, accepted claim, StageCourt trace가 있다.

다만 그것은 Brain/Web evidence pass이고,
FULL_THESIS 운영 Stage pass가 아니다.
```

## v105가 아직 통과하지 못한 것

`goal_completion_audit.json`:

```text
goal_completion_ready = false

blockers:
  - full_thesis_smoke_pending
  - full_thesis_smoke_execution_pending
  - full_thesis_production_pass_false
  - full_thesis_seed_promotion_pass_false
  - source_backed_replay_parity_all_archetypes_pending
  - goal_requirement_matrix_pass_false
```

`goal_requirement_matrix_audit.json`:

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

해석:

```text
fail은 0개다.
하지만 pending 4개가 전부 핵심 운영화 gate라서 goal complete가 아니다.
```

## FULL_THESIS production runner가 막힌 위치

`full_thesis_production_runner_audit.json`:

```text
verdict = PENDING_PRODUCTION_FULL_THESIS
production_mode_requested = true
candidate_row_count = 23
blocked_candidate_count = 23
promoted_full_thesis_row_count = 0
promoted_symbols = []

candidate_source_counts:
  brain_web_partial_stage_row = 4
  stagecourt_trace_direct_scan = 19

blocker for all 23 candidates:
  missing_green_gate_primitives
```

missing primitive count:

```text
margin_bridge_visible              19
contract_duration_months           17
contract_amount_to_prior_sales     13
hbm_capacity_constraint             2
customer_preorder_or_allocation      1
hbm_capacity_pre_sold                1
customer_contract                    1
order_backlog_to_sales               1
```

샘플:

```text
SK하이닉스 / C06:
  present =
    customer_preorder_or_allocation
    hbm_capacity_pre_sold
    medium_term_revision_visibility
    revenue_visibility_contract
  missing =
    hbm_capacity_constraint

삼성전자 / C06:
  present =
    medium_term_revision_visibility
    revenue_visibility_contract
  missing =
    customer_preorder_or_allocation
    hbm_capacity_constraint
    hbm_capacity_pre_sold

대우건설 / C05:
  present =
    delivery_schedule
    margin_bridge_visible
  missing =
    contract_amount_to_prior_sales
    contract_duration_months
```

중요한 판단:

```text
여기서 Green gate를 낮춰서 승격시키면 안 된다.
막힌 이유가 source linkage 실패나 score interval 실패가 아니라,
아키타입 Evidence Contract가 요구하는 Green primitive가 아직 안 닫힌 것이다.
```

쉬운 예:

```text
하이닉스는 "고객 배정/선판매/매출 가시성"은 잡혔다.
하지만 "capacity constraint"라는 필수 칸이 아직 비어 있다.
이 상태에서 Green/FULL_THESIS로 승격하면 다시 예전처럼 점수 칸을 억지로 채우는 문제가 된다.
```

## follow-up seed 55개 의미

v105는 막힌 Green primitive를 다음 Research Brain 입력으로 넘기기 위해 follow-up seed를 만들었다.

```text
full_thesis_blocker_follow_up_source_tasks.jsonl = 55 rows
full_thesis_blocker_follow_up_seed_events.jsonl = 55 rows
```

각 seed의 안전장치:

```text
score_evidence_allowed = false
stage_promotion_allowed_before_execution = false
seed_role = planner_input_only
official_first_required = true
llm_query_required = true
llm_query_allowed = true
hardcoded_query_count = 0
hardcoded_queries = []
query_intents = []
max_queries = 3
max_candidates = 20
max_fetches = 3
general_search_allowed = false
forbidden_source_classes includes:
  snippet_only_score
  source_proxy_only
  evidence_url_pending
  unbounded_general_search
```

즉 follow-up seed는 점수 재료가 아니다.

```text
follow-up seed = "이 빈칸을 조사해라"라는 작업지시서
accepted claim = 실제 점수 재료
```

## 이번 v106 코드 패치

문제:

```text
v105 follow-up seed row에는 follow_up_primitive_gap / follow_up_archetype_id가
structured_payload 안에는 있었지만 top-level에는 없었다.

다음 에이전트가 단순 집계를 하면 primitive/archetype이 None처럼 보일 수 있다.
```

패치:

```text
_full_thesis_blocker_follow_up_seed_events()가 아래 필드를 top-level에도 쓴다.

follow_up_task_id
follow_up_archetype_id
follow_up_primitive_gap
```

이 패치는 점수나 Stage 승격 조건을 바꾸지 않는다.

```text
BRAIN_WEB_PARTIAL -> FULL_THESIS 승격 조건 완화 없음
Green gate 완화 없음
종목명 예외 없음
하드코딩 query 추가 없음
```

검증:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_stage_promotion_gate -v
```

결과:

```text
Ran 17 tests
OK
```

주의:

```text
기존 v105 산출물은 패치 전 만들어진 파일이라 top-level follow_up_* 필드가 없다.
v105의 해당 정보는 structured_payload 안에 있다.
이 패치 이후 새 run부터 top-level에도 노출된다.
```

## 코드 경로 교차검증

`run_census_mode_v4()` 순서:

```text
1. v3 leaf 복사
2. stage_rows 생성
3. full_thesis_refresh_queue 생성
4. research_brain_full_thesis_seed_events.jsonl 생성
5. _run_brain_web_attempt() 1회 실행
6. BRAIN_*_PARTIAL promotion
7. _apply_production_full_thesis_from_brain()
8. 막힌 후보에서 full_thesis_blocker_follow_up_* 생성
9. smoke replay
10. audits/write outputs
```

핵심 병목:

```text
full_thesis_blocker_follow_up_seed_events.jsonl은 8번에서 생성된다.
하지만 _run_brain_web_attempt()는 5번에서 이미 끝났다.

따라서 v105 한 번 실행 안에서는 follow-up seed 55개가 다시 Research Brain에 소비되지 않는다.
```

CLI에는 외부 seed 입력이 있다.

```bash
--brain-candidate-event-seed-path output/.../full_thesis_blocker_follow_up_seed_events.jsonl
```

하지만 현재 내부 루프는 아니다.

```text
max_iterations는 현재 self-repair/audit log에 기록되지만,
v105 run 안에서 follow-up seed를 자동으로 2차 Brain/Web attempt에 먹이는 루프는 아직 없다.
```

다음 패치가 건드려야 할 핵심은 이 부분이다.

## All-archetype replay 상태

`all_archetype_replay_matrix.json`:

```text
required_archetype_count = 32
source_backed_ready_count = 6
missing_required_archetype_count = 26
all_archetype_replay_pass = false

status_counts:
  SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY = 6
  SOURCE_GAP_PENDING = 26
  GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY = 4
```

ready:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
C15_MATERIAL_SPREAD_SUPERCYCLE
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
C24_BIO_TRIAL_DATA_EVENT_RISK
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

missing required archetypes:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE
C02_POWER_GRID_DATACENTER_CAPEX
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
C11_BATTERY_ORDERBOOK_RERATING
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
C13_BATTERY_JV_UTILIZATION_AMPC_IRA
C14_EV_DEMAND_SLOWDOWN_4B_4C
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
C18_CONSUMER_EXPORT_CHANNEL_REORDER
C19_BRAND_RETAIL_INVENTORY_MARGIN
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
C22_INSURANCE_RATE_CYCLE_RESERVE
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
C27_CONTENT_IP_GLOBAL_MONETIZATION
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

해석:

```text
삼성/하이닉스 C06만 닫는다고 전체 목표가 끝나지 않는다.
모든 required archetype이 source-backed positive + guard replay를 가져야 한다.
```

## 다음 패치 방향

### P0. follow-up seed를 실제 2차 Brain/Web attempt로 연결

현재:

```text
1차 Brain/Web attempt
-> FULL_THESIS candidate 23개 발견
-> Green primitive gap 55개 seed 생성
-> run 종료
```

목표:

```text
1차 Brain/Web attempt
-> Green primitive gap 55개 seed 생성
-> bounded 2차 Brain/Web attempt
-> 새 accepted claim append
-> primitive coverage 재계산
-> production FULL_THESIS promotion 재시도
```

안전조건:

```text
append-only로 leaf를 추가한다.
기존 accepted claim을 조용히 삭제하거나 LLM field 전체 재작성 금지.
iteration별 output suffix 또는 attempt_id를 남긴다.
무한 반복 금지. max_iterations와 per-task budget을 반드시 사용한다.
follow-up seed는 score_evidence_allowed=false인 planner input이어야 한다.
점수는 새 accepted claim이 생긴 뒤에만 들어간다.
```

쉬운 예:

```text
검사 결과표를 보고 "추가 피검사 3개 필요"가 나오면,
같은 진료 안에서 추가 검사를 실제로 돌리고 다시 진단해야 한다.
지금은 추가 검사 오더만 발행하고 진료가 끝난 상태다.
```

### P1. 삼성전자/SK하이닉스 full-thesis smoke를 실제 실행

현재:

```text
samsung_hynix_full_thesis_smoke:
  verdict = PENDING_FULL_THESIS_REFRESH
  blocking_reason = full_thesis_source_tasks_planned_but_not_executed
  full_thesis_claim_ids = []
  full_thesis_score_contribution_ids = []
  full_thesis_stagecourt_trace_ids = []
```

목표:

```text
005930 / 000660에 대해
FULL_THESIS seed -> source task -> accepted claim -> primitive -> score contribution -> StageCourt -> FULL_THESIS row
를 실제로 닫는다.
```

주의:

```text
controlled smoke row는 production pass가 아니다.
BRAIN_WEB_PARTIAL row를 FULL_THESIS로 이름만 바꾸면 안 된다.
```

### P2. C05 계열 systemic gap 먼저 수리

v105 blocked candidates는 C05 contract 계열이 많다.

대표 missing:

```text
margin_bridge_visible
contract_duration_months
contract_amount_to_prior_sales
```

다음 패치에서 확인할 것:

```text
DART 단일판매공급계약 공시에 계약금액/최근매출대비/계약기간이 있는데도 primitive mapping이 못 닫는지
공시에는 있는데 extractor/mapper가 빠뜨리는지
원문 자체가 실제로 없어서 follow-up source task가 필요한지
```

쉬운 예:

```text
공시에 "계약금액 1,000억, 최근 매출의 15%, 계약기간 2026~2028"이 있으면
contract_amount_to_prior_sales와 contract_duration_months는 웹뉴스 없이도 DART에서 닫혀야 한다.
그게 안 닫히면 source 문제가 아니라 extractor/mapper 문제다.
```

### P3. All-archetype replay fixture 확장

현재 6/32만 source-backed ready다.

다음 목표:

```text
각 required archetype마다 최소:
  positive source-backed replay 1개
  guard source-backed replay 1개
  source_proxy_only leak 0개
```

단, source_proxy_only 연구자료는 운영 점수 fixture로 쓰면 안 된다.

```text
source_proxy_only = ontology 참고자료
source-backed URL/anchor = 운영 replay fixture
```

### P4. 금지할 지름길

아래는 절대 패치 방향이 아니다.

```text
Green gate primitive를 줄여서 23개 후보를 승격
삼성전자/하이닉스 종목명 예외 추가
missing primitive를 UNKNOWN인데 PRESENT로 간주
BRAIN_WEB_PARTIAL score를 FULL_E2R_100으로 복사
follow-up seed를 score evidence로 사용
source_proxy_only 연구자료를 replay 정답으로 사용
무제한 general web search로 gap을 메움
```

## 다음 에이전트가 공격해야 할 질문

1. v105의 `BRAIN_WEB_PARTIAL` 4개 중 어떤 row가 실제 source-backed claim chain을 갖고 있고, 어떤 primitive가 아직 부족한가?
2. 23개 FULL_THESIS 후보의 blocker가 정말 전부 `missing_green_gate_primitives`뿐인가?
3. C05의 계약금액/계약기간/margin bridge는 DART/KIND 원문에서 바로 닫을 수 있는데 mapper가 놓친 것인가?
4. 55개 follow-up seed를 다음 run 입력으로 넣었을 때 planner prompt에 primitive gap은 보이되 점수/Stage 답안지는 보이지 않는가?
5. follow-up seed 2차 실행 후 새 accepted claim이 기존 claim을 덮어쓰지 않고 append-only로 붙는가?
6. score delta가 생기면 added/removed/superseded/contradicted claim delta로 설명되는가?
7. 삼성전자/하이닉스 full thesis smoke는 controlled replay가 아니라 production source task execution으로 닫히는가?
8. all-archetype replay 26개 pending은 진짜 source fixture 부재인가, 아니면 이미 docs/round에 URL-backed fixture가 있는데 census output으로 못 끌고 온 것인가?
9. `max_iterations > 1`을 줬을 때 실제 반복 실행이 되는가, 아니면 로그에만 기록되는가?
10. 어떤 경우에도 `operator_stage_use=FULL_THESIS_STAGE`가 source-backed claim 없는 row에 붙지 않는가?

## 최종 판단

지금 잘못되고 있는 부분은 "Stage가 완전히 없다"가 아니다.

정확한 문제는:

```text
부분검사 Stage는 생기기 시작했다.
하지만 FULL_THESIS 최종 Stage로 닫는 loop가 아직 끊겨 있다.
```

v105는 중요한 전진이다.

```text
Brain/Web evidence pass
claim extractor timeout 해소
source connector capability blocker 해소
primitive multi-mapping audit 해소
```

하지만 목표는 아직 아니다.

```text
운영 FULL_THESIS row = 0
FULL_E2R_100 score = 0
삼성/하이닉스 smoke = pending
seed promotion = 0
all-archetype replay = 6/32
```

다음 패치는 gate를 낮추는 것이 아니라,
막힌 Green primitive를 follow-up seed로 실제 다시 조사하고
source-backed accepted claim으로 닫은 뒤
StageCourt를 재실행하는 방향이어야 한다.


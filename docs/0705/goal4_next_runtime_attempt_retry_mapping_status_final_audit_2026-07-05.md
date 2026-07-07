# Goal4 0705 Runtime Retry Final Audit

작성일: 2026-07-07  
평가 기준일: 2026-07-05  
기준 커밋: `2e2acea`  
실행 output: `output/census_v4/2026-07-07-goal4-all-archetype-next-runtime-attempt-retry-mapping-status`

## 결론

이번 재시도는 **런타임은 끝까지 완료됐지만 Goal4는 아직 NOT_READY**다.

쉽게 말하면:

- 차가 공장 밖으로 나오기는 했다.
- 실제 도로 주행 허가를 받기에는 아직 서류가 부족하다.
- 특히 전체 아키타입 중 일부만 StageCourt/full-thesis까지 갔고, 대부분은 accepted claim 또는 material primitive가 부족하다.

중요한 점은 이전 실패였던 `mapping_id collision`은 해결됐다는 것이다. 이번 실행은 그 지점을 지나 111개 seed 전체를 처리했다.

## 실행 결과 요약

실행 종료:

```text
process exit code: 1
stdout: NOT_READY
runtime progress status: COMPLETED
latest phase: completed
```

핵심 감사값:

| 항목 | 값 |
|---|---:|
| seed event count | 111 |
| real planner/provider success | 111 |
| runtime budget exhausted | 0 |
| source task execution count | 805 |
| fetched real documents | 750 |
| unique fetched real documents | 147 |
| accepted claim count | 110 |
| unique accepted claim count | 70 |
| StageCourt trace exported | 21 |
| Brain promoted stage rows | 11 |
| production FULL_THESIS rows | 6 |
| final verdict | `NOT_READY` |

참조 audit:

- `brain_web_attempt_audit.json`
- `readiness_verdict.json`
- `goal_completion_audit.json`
- `goal_requirement_matrix_audit.json`
- `full_thesis_production_audit.json`
- `full_thesis_seed_materialization_audit.json`
- `full_thesis_production_runner_audit.json`

## 무엇은 좋아졌나

### 1. mapping collision은 해결됨

이전 실행은 같은 claim/archetype/primitive/support direction에 대해 `ACCEPTED`와 `REJECTED` mapping이 동시에 생기면서 같은 mapping id를 공유해 죽었다.

패치:

```text
mapping_id = stable_id(
  claim_id,
  archetype_id,
  primitive_id,
  support_direction,
  mapping_status
)
```

즉 같은 claim이라도 `ACCEPTED`와 `REJECTED`는 서로 다른 ledger row가 된다.

검증:

```text
PYTHONPATH=src python -m unittest \
  tests.test_agentic_evidence_os.AgenticEvidenceOSTests.test_mapping_id_ignores_llm_rule_and_rationale_noise \
  tests.test_agentic_evidence_os.AgenticEvidenceOSTests.test_mapping_id_separates_accepted_and_rejected_status -v

Ran 2 tests OK
```

관련 operational 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_goal_required_audits \
  tests.test_full_thesis_score_path_not_meaningful_pass -v

Ran 85 tests OK
```

최종 full regression:

```text
PYTHONPATH=src python -m unittest discover -s tests -v

Ran 5283 tests in 426.571s
OK
```

주의할 점:

```text
터미널 full regression은 통과했다.
하지만 이번 Goal4 runtime output에는 e2r_test_result_artifact_v1 machine-readable artifact가 아직 연결되지 않았다.
따라서 FULL_TEST_ARTIFACT_PASS gate는 런타임 completion 기준으로는 아직 pending이다.
```

쉬운 예:

```text
시험은 실제로 봤고 합격 점수도 받았다.
다만 심사 시스템에 제출할 공식 성적표 JSON을 이번 runtime output에 붙이지 못했다.
그래서 "테스트 자체 실패"가 아니라 "공식 증빙 artifact 미연결" blocker로 남는다.
```

### 2. 111개 seed 전체가 실제 provider 경로를 탔다

`brain_web_attempt_audit.json` 기준:

```text
full_thesis_seed_event_count = 111
full_thesis_seed_planner_attempted_event_count = 111
full_thesis_seed_real_provider_success_count = 111
full_thesis_seed_runtime_budget_exhausted_count = 0
fake_provider_used_count = 0
```

이전처럼 중간 예외로 끊긴 실행이 아니다.

### 3. C05 독점 문제는 이번 실행에서 줄어듦

이전 감사의 핵심 질문은 “왜 production FULL_THESIS가 전부 C05인가?”였다. 이번 실행의 production FULL_THESIS 6개는 전부 C05가 아니다.

| symbol | company | archetype | stage | score | accepted score claims | present green | missing green |
|---|---|---|---:|---:|---:|---|---|
| 000100 | 유한양행 | C24_BIO_TRIAL_DATA_EVENT_RISK | 3-Green | 90.0 | 1 | trial_quality_visible | - |
| 003380 | 하림지주 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 0 | 14.0002 | 1 | delivery_schedule | contract_amount_to_prior_sales, contract_duration_months, margin_bridge_visible |
| 005930 | 삼성전자 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 0 | 39.8333 | 1 | revenue_visibility_contract | customer_preorder_or_allocation, hbm_capacity_constraint, hbm_capacity_pre_sold |
| 011170 | 롯데케미칼 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 0 | 18.75 | 1 | spread_expansion | utilization_rate, inventory_cycle, opm_expansion_pctp |
| 047810 | 한국항공우주 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 0 | 37.0 | 2 | export_contract, delivery_schedule | government_customer, order_backlog_to_sales |
| 052400 | 코나아이 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 1 | 46.0 | 3 | contract_quality, delivery_schedule, fcf_quality_score | order_backlog_to_sales, named_customer_quality, opm_expansion_pctp |

따라서 현재 문제는 “C05만 나오는 문제”라기보다, **대부분의 아키타입이 accepted claim 또는 required positive primitive를 못 닫아 production full thesis로 승격되지 못하는 문제**다.

## 왜 NOT_READY인가

`goal_completion_audit.json`의 blockers:

```text
full_thesis_smoke_pending
full_thesis_smoke_execution_pending
full_thesis_production_pass_false
full_thesis_seed_materialization_audit_not_pass
machine_readable_test_result_artifact_missing
```

`goal_requirement_matrix_audit.json`:

```text
fail_gate_ids:
- FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS

pending_gate_ids:
- FULL_THESIS_SMOKE_PASS
- FULL_THESIS_PRODUCTION_PASS
- FULL_TEST_ARTIFACT_PASS
```

핵심은 `brain_web_evidence_pass=true`여도 `meaningful_full_thesis_evidence_pass=false`라는 점이다.

쉬운 예:

```text
책상 위에 자료가 쌓였다 = brain_web_evidence_pass
그 자료가 각 점수 칸에 맞게 채점표를 완성했다 = meaningful_full_thesis_evidence_pass
```

이번에는 첫 번째는 됐고, 두 번째는 아직 아니다.

## Seed materialization 상태

`full_thesis_seed_materialization_audit.json`:

```text
verdict = FAIL
seed_event_count = 111
trace_row_count = 111
full_thesis_promoted_seed_count = 6
critical_count = 48
```

상태 분포:

| materialization status | count | 의미 |
|---|---:|---|
| FULL_THESIS_PROMOTED | 6 | production FULL_THESIS까지 승격 |
| STAGECOURT_READY_NOT_PROMOTED | 15 | StageCourt trace는 있으나 production full thesis 조건 미충족 |
| ACCEPTED_CLAIM_NOT_CREATED | 88 | source task는 실행됐지만 accepted claim 없음 |
| STAGECOURT_TRACE_NOT_CREATED | 2 | StageCourt trace도 생성 안 됨 |

즉 111개 중 6개만 production full thesis까지 갔다.

## Stage가 있는 애들이 있나?

있다. 다만 매우 적다.

전체 `census_stage_map.jsonl` 기준:

```text
Stage0: 3299
Stage1: 51
Stage2-Watch: 29
3-Green: 1
Red: 1
기타 canonical 0/1/2 row: 소수
```

Research Brain StageCourt trace 기준으로는 아래 11개가 실제 claim-backed trace를 만들었다.

| symbol | company | archetype | stage | score | production row? | present green | missing green |
|---|---|---|---:|---:|---|---|---|
| 000100 | 유한양행 | C24_BIO_TRIAL_DATA_EVENT_RISK | 3-Green | 90.0 | yes | trial_quality_visible | - |
| 001390 | KG케미칼 | C15_MATERIAL_SPREAD_SUPERCYCLE | 0 | 34.4 | no | fcf_quality_score | spread_expansion, utilization_rate, inventory_cycle, pricing_power_confirmed |
| 003380 | 하림지주 | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 0 | 14.0002 | yes | delivery_schedule | contract_amount_to_prior_sales, contract_duration_months, margin_bridge_visible |
| 005930 | 삼성전자 | C06_HBM_MEMORY_CUSTOMER_CAPACITY | 0 | 39.8333 | yes | revenue_visibility_contract | customer_preorder_or_allocation, hbm_capacity_constraint, hbm_capacity_pre_sold |
| 011170 | 롯데케미칼 | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 0 | 18.75 | yes | spread_expansion | utilization_rate, inventory_cycle, opm_expansion_pctp |
| 017670 | SK텔레콤 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 0 | 33.0 | no | fcf_quality_score | volume_growth_visible, mix_improvement, operating_leverage_visible, pricing_power_confirmed |
| 047810 | 한국항공우주 | C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 0 | 37.0 | yes | export_contract, delivery_schedule | government_customer, order_backlog_to_sales |
| 051910 | LG화학 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 0 | 19.5 | no | implementation_timeline | policy_or_regulatory_confirmed, direct_company_cash_route, subsidy_capture_visible |
| 052400 | 코나아이 | C01_ORDER_BACKLOG_MARGIN_BRIDGE | 1 | 46.0 | yes | contract_quality, delivery_schedule, fcf_quality_score | order_backlog_to_sales, named_customer_quality, opm_expansion_pctp |
| 058470 | 리노공업 | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 2 | 65.2 | no | named_customer_quality, socket_or_test_demand_visible, margin_bridge_visible | qualification_confirmed, repeat_order_confirmed |
| 064760 | 티씨케이 | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 0 | 12.6969 | no | - | memory_price_increase_mentioned, supply_discipline_mentioned, cycle_demand_visibility, end_market_demand_visibility, supply_demand_tightness, cycle_to_revenue_bridge, advanced_packaging_bottleneck, equipment_order_recovery, order_to_revenue_bridge, inventory_cycle_repair |

주의:

- `production row? = no`는 점수가 아예 없다는 뜻이 아니다.
- StageCourt trace는 있으나, production full thesis row로 승격되지 않았다는 뜻이다.
- 예: 리노공업은 C08에서 65.2점 Stage 2 trace가 있지만 `qualification_confirmed`, `repeat_order_confirmed`가 비어 production full thesis pass에는 못 들어갔다.

## 삼성전자와 하이닉스 상태

### 삼성전자

삼성전자는 이번 production FULL_THESIS row에 들어왔다.

```text
symbol = 005930
archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
score = 39.8333
stage = 0
present_green = revenue_visibility_contract
missing_green = customer_preorder_or_allocation, hbm_capacity_constraint, hbm_capacity_pre_sold
```

쉽게 말하면:

```text
매출/가시성 관련 claim 하나는 잡혔다.
하지만 C06 Green에 필요한 고객 선주문/배정, HBM capacity constraint, pre-sold capacity claim은 못 닫았다.
그래서 높은 Stage로 올리지 않았다.
```

이전의 “90점대였다가 60점대로 흔들림” 문제와 다르게, 이번 결과는 claim-backed trace 기준이다. 다만 39.8333이 최종 품질이라는 뜻은 아니다. C06 필수 증거가 아직 닫히지 않았다는 보수적 결과다.

### SK하이닉스

SK하이닉스는 production FULL_THESIS row로 올라오지 못했다.

`full_thesis_production_runner_audit.json`의 refresh queue sample:

```text
symbol = 000660
company_name = SK하이닉스
blocked_reason = full_thesis_refresh_task_not_run
materialization_blocker = full_thesis_refresh_task_has_no_research_brain_stagecourt_trace
source_base_stage = Stage1
source_stage_signal = OFFICIAL_EVENT_WATCH
priority_bucket = P2_EVENT_WATCH_REFRESH
```

쉽게 말하면:

```text
SK하이닉스는 "다음에 full thesis refresh를 해야 하는 후보"로 큐에는 있다.
하지만 이번 111 seed 재시도 안에서 source-backed StageCourt trace가 닫히지 않아 production row가 아니다.
```

## 전체 아키타입 materialization matrix

| archetype | promoted | stagecourt ready not promoted | no accepted claim | no stagecourt trace | accepted claims | source task exec |
|---|---:|---:|---:|---:|---:|---:|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 1 | 2 | 0 | 0 | 11 | 21 |
| C02_POWER_GRID_DATACENTER_CAPEX | 0 | 0 | 3 | 0 | 0 | 21 |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 1 | 2 | 0 | 0 | 9 | 21 |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 0 | 0 | 3 | 0 | 0 | 21 |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 1 | 2 | 0 | 0 | 6 | 22 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 1 | 2 | 0 | 0 | 3 | 22 |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 0 | 0 | 3 | 0 | 0 | 23 |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 0 | 1 | 2 | 0 | 9 | 22 |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 0 | 0 | 3 | 0 | 0 | 22 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 0 | 1 | 2 | 0 | 2 | 21 |
| C11_BATTERY_ORDERBOOK_RERATING | 0 | 0 | 3 | 0 | 0 | 22 |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 0 | 0 | 3 | 0 | 0 | 22 |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 0 | 0 | 3 | 0 | 0 | 22 |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 0 | 0 | 3 | 0 | 0 | 22 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 0 | 1 | 2 | 0 | 4 | 22 |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 0 | 0 | 3 | 0 | 0 | 22 |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 1 | 0 | 2 | 0 | 2 | 22 |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 0 | 0 | 3 | 0 | 0 | 22 |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 0 | 0 | 3 | 0 | 0 | 22 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 0 | 0 | 3 | 0 | 0 | 21 |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 0 | 0 | 3 | 0 | 0 | 21 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 0 | 0 | 3 | 0 | 0 | 21 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 0 | 0 | 3 | 0 | 0 | 22 |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 1 | 0 | 2 | 0 | 3 | 21 |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 0 | 0 | 3 | 0 | 0 | 22 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 0 | 0 | 3 | 0 | 0 | 22 |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 0 | 0 | 3 | 0 | 0 | 21 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 0 | 0 | 3 | 0 | 0 | 21 |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 0 | 1 | 3 | 2 | 36 | 43 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 0 | 0 | 3 | 0 | 0 | 22 |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 0 | 3 | 0 | 0 | 3 | 23 |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 0 | 0 | 3 | 0 | 0 | 23 |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 0 | 0 | 3 | 0 | 0 | 24 |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 0 | 0 | 3 | 0 | 0 | 21 |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 0 | 0 | 3 | 0 | 0 | 21 |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 0 | 0 | 3 | 0 | 0 | 22 |

이 표의 핵심:

- 모든 아키타입이 source task 실행까지는 갔다.
- 하지만 대부분은 accepted claim이 0이다.
- C01/C03/C05/C06/C17/C24만 production row로 일부 승격됐다.
- C08/C10/C15/C29/C31은 StageCourt trace는 생겼지만 production row로는 막혔다.
- C02/C04/C07/C09/C11~C14/C16/C18~C23/C25~C28/C30/C32/R13 대부분은 accepted claim 미생성 상태다.

## 왜 production pass가 막혔나

`full_thesis_production_audit.json`:

```text
production_full_thesis_row_count = 6
production_full_thesis_row_with_required_positive_missing_primitives_count = 5
production_full_thesis_row_with_green_gap_primitives_count = 5
production_symbols_without_required_positive_missing_primitives = ["000100"]
production_symbols_without_green_gap_primitives = ["000100"]
production_pass_allowed = false
```

즉 유한양행 C24만 required positive/green gap이 없다. 나머지 5개 production row는 score path는 닫혔지만, 의미 있는 full thesis라고 부르기에는 핵심 positive primitive가 남아 있다.

쉬운 예:

```text
삼성전자 C06:
revenue_visibility_contract는 있음.
하지만 HBM capacity pre-sold, customer allocation, capacity constraint가 없음.
따라서 "C06 thesis가 완성됐다"라고 하면 안 됨.
```

## 27.9998 / 77.9998 문제에 대한 현재 위치

이전 감사에서 문제가 된 `27.9998 / 77.9998` 같은 값은 score path closed와 meaningful full thesis를 섞어 읽은 것이 핵심 문제였다.

이번 실행의 audit은 이 둘을 명확히 분리한다.

```text
production_full_e2r_score_path_pass_allowed = true
meaningful_full_thesis_evidence_pass_allowed = false
```

뜻:

- `production_full_e2r_score_path_pass_allowed=true`: claim-backed score contribution -> StageCourt 계산 경로가 동작함.
- `meaningful_full_thesis_evidence_pass_allowed=false`: required positive/Green primitive까지 충분히 닫힌 thesis는 아직 부족함.

예:

```text
하림지주 C05 14.0002:
delivery_schedule claim 하나로 점수는 계산됨.
하지만 contract_amount_to_prior_sales, contract_duration_months, margin_bridge_visible이 비어 있어 full thesis 완성으로 보지 않음.
```

## 남은 문제의 성격

### 문제 1. accepted claim 미생성

88/111 seed가 `ACCEPTED_CLAIM_NOT_CREATED`다.

이건 LLM planner가 source task를 만들고 실행까지 했지만, Evidence OS가 점수 가능한 current/direct/anchored claim을 만들지 못했다는 뜻이다.

좋은 점:

- 없는 증거를 억지로 점수에 넣지는 않았다.

나쁜 점:

- 실제 운영에 필요한 primitive를 닫을 만큼 source acquisition/extraction이 아직 강하지 않다.

### 문제 1-1. accepted claim 미생성 원인 분해

이번 패치 후 `full_thesis_seed_materialization_trace.jsonl`와 `full_thesis_seed_materialization_audit.json`은 `ACCEPTED_CLAIM_NOT_CREATED`를 한 덩어리로 두지 않고 seed별 source task 실패축을 기록한다.

현재 88개 accepted-claim 미생성 seed의 primary failure axis:

| primary failure axis | seed count | 쉬운 의미 |
|---|---:|---|
| `PRIMITIVE_GAP_UNSATISFIED` | 78 | 문서는 찾았지만 그 문장이 해당 primitive 빈칸을 직접 채우지 못함 |
| `NO_FETCHED_DOCUMENT` | 7 | fetch 가능한 원문을 충분히 잡지 못함 |
| `NO_SCORE_ELIGIBLE_REAL_CLAIM` | 2 | claim 후보는 있었지만 current/direct/anchor 조건을 통과하지 못함 |
| `PROVIDER_ERROR_RECORDED` | 1 | provider 문제를 먼저 해결해야 함 |

전체 failure axis 누적에는 다음도 같이 보인다.

```text
PRIMITIVE_GAP_UNSATISFIED = 482
NO_SCORE_ELIGIBLE_REAL_CLAIM = 485
PRIMITIVE_MAPPING_REJECTED = 299
MAPPING_NOT_ACCEPTED = 299
TEMPORAL_NOT_CURRENT = 174
NO_FETCHED_DOCUMENT = 157
```

쉬운 예:

```text
C02 datacenter_customer를 찾으라고 했는데
가져온 DART/KIND/리포트 문서가 회사 일반 공시, 과거 리포트, 다른 primitive 문장에 가까움
→ source task는 실행됐지만 datacenter_customer accepted claim은 0
→ 다음에는 "공시 아무거나"가 아니라 datacenter customer를 직접 말하는 원문 구간을 찾아야 함
```

따라서 다음 병목은 단순 provider 장애가 아니다. 가장 큰 병목은 **source task가 primitive-specific 원문 claim을 찾아오지 못하는 것**이다.

### 문제 1-2. seed 실패축을 다음 runtime attempt 입력으로 연결

추가 패치 후 seed materialization 실패축은 단순 감사 문서에만 남지 않는다.

연결된 경로:

```text
full_thesis_seed_materialization_trace.jsonl
→ all_archetype_runtime_status_matrix_2026-07-05.json
→ all_archetype_next_runtime_attempt_plan_2026-07-05.json
→ all_archetype_next_runtime_source_tasks_2026-07-05.jsonl
→ all_archetype_next_runtime_seed_events_2026-07-05.jsonl
→ Research Brain v4 planner prompt payload
```

현재 matrix 요약:

```text
seed_materialization_trace_count = 111
seed_materialization_accepted_claim_not_created_count = 88
seed_materialization_primary_failure_axis_counts =
  NO_FETCHED_DOCUMENT: 3
  PRIMITIVE_GAP_UNSATISFIED: 33
```

현재 next attempt plan 요약:

```text
plan_row_count = 35
source_task_count = 105
seed_event_count = 105
seed_materialization_repair_task_count = 105
seed_materialization_primary_failure_axis_counts =
  NO_FETCHED_DOCUMENT: 9
  PRIMITIVE_GAP_UNSATISFIED: 96
```

쉬운 예:

```text
C02 datacenter_customer seed가 실패함
→ matrix row에 previous seed failure = PRIMITIVE_GAP_UNSATISFIED 기록
→ next source task planner_failure_feedback에 같은 값과 repair hint 기록
→ LLM planner는 다음 질의에서 generic 사업보고서/상태확인 문서가 아니라
   datacenter_customer를 직접 말하는 current/direct/source-backed 문장을 찾아야 함
```

중요한 안전장치:

```text
score_evidence_allowed_from_previous_seed_failures = false
```

즉 seed 실패 sample은 점수 근거가 아니다. 다음 LLM query/source route를 고치는 피드백일 뿐이다.

runtime prompt 연결도 확인했다.

```text
structured_payload.planner_failure_feedback.previous_seed_materialization_primary_failure_axis
→ _planner_failure_feedback_context_from_structured_payload
→ existing_evidence_summary.full_thesis_queue_context.planner_failure_feedback
→ build_v4_planner_prompt_payload rules
```

planner rule에는 다음 의미가 들어간다.

```text
PRIMITIVE_GAP_UNSATISFIED면
이전 일반 문서/인접 문맥을 다시 점수 근거로 쓰지 말고
원래 primitive_gap을 직접 말하는 source route/query_intent를 새로 만들어라.
```

### 문제 2. StageCourt trace와 production row의 분리

15개는 `STAGECOURT_READY_NOT_PROMOTED`다.

이건 계산 trace는 생겼지만, production full thesis로 쓰기에는 scope/score/Green gap 조건이 닫히지 않았다는 뜻이다.

### 문제 3. refresh queue 81개 미실행

`full_thesis_refresh_queue_audit.json`:

```text
queue_candidate_count = 81
full_thesis_stage_row_count = 6
verdict = PASS
```

큐 자체는 잘 만들어졌다. 하지만 queue row는 stage/score가 아니다.

예:

```text
SK하이닉스가 큐에 있다는 뜻은 "다음 조사 대상"이라는 뜻이다.
"운영 full thesis 결과"라는 뜻이 아니다.
```

## 다음 패치 방향

1. `ACCEPTED_CLAIM_NOT_CREATED` 88개 중 `PRIMITIVE_GAP_UNSATISFIED` primary 78개 병목은 matrix/next plan 피드백으로 연결됐다.
   - generic DART/KIND/CompanyGuide status check가 primitive claim으로 둔갑하지 않게 유지한다.
   - next source task에는 `previous_seed_materialization_primary_failure_axis`, `previous_seed_materialization_repair_hint`, compact sample ref가 들어간다.
   - 다음 실제 실행에서는 LLM planner가 이 피드백을 받아 primitive-specific 원문 구간을 찾아오는지 검증해야 한다.

2. C02/C04/C07/C09/C11~C14/C16/C18~C23/C25~C28/C30/C32/R13처럼 accepted claim이 0인 아키타입부터 source task 실행 결과를 역추적해야 한다.

3. C08/C10/C15/C29/C31처럼 StageCourt trace는 있지만 production row가 아닌 아키타입은 promotion blocker를 좁혀야 한다.

4. production row 5개의 required positive/Green gap은 follow-up SourceTask로 다시 닫아야 한다.

5. `machine_readable_test_result_artifact_missing`은 테스트 실행 결과를 machine-readable artifact로 남기는 연결을 추가해야 한다.
   - 이번 터미널 full regression은 `5283 OK`다.
   - 하지만 Goal4 gate가 요구하는 것은 `e2r_test_result_artifact_v1` JSON과 log hash다.
   - 다음 runtime 또는 검증 패치에서는 `run_test_command_with_artifact` wrapper로 동일 테스트를 실행하고 그 artifact를 Goal4 output에 연결해야 한다.

## 운영 판단

이번 실행은 **실패가 아니라 유효한 NOT_READY 감사 산출물**이다.

폐기해야 할 invalid partial output은 아니다. 이유:

```text
partial_run_invalid.json 없음
brain_web_runtime_progress.status = COMPLETED
111/111 real provider success
runtime_budget_exhausted = false
audit들이 정상 생성됨
```

다만 Goal4 완료로 표시하면 안 된다.

최종 판단:

```text
Goal4 status: NOT_READY
runtime attempt: completed
mapping collision regression: fixed
all-archetype source execution: attempted
all-archetype full-thesis parity: not proven
meaningful operational full thesis: not proven
```

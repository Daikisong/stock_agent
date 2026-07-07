# Goal4 Self-Repair Attempt 01 Runtime Parity Audit - 2026-07-05

작성 시점: 2026-07-07 KST

이 문서는 `docs/core/goal4.md`를 실제 runtime으로 돌린 뒤, 현재 무엇이 통과했고 무엇이 아직 안 닫혔는지 0705 기준 산출물로 정리한다.

핵심 결론:

```text
Planner C05-only 쏠림: 해소됨
전 아키타입 runtime 시도: 36개 row 모두 존재
production score path: 일부 닫힘
meaningful full thesis evidence: 아직 실패
최종 Goal4: 완료 아님
```

쉬운 예:

```text
전에는 시험지가 C05 과목만 10장 나온 문제였다.
이번에는 36개 과목 모두 시험장에는 들어왔다.
하지만 실제 합격 답안지는 6장뿐이고, 그중 5장은 필수 첨부서류가 비어 있다.
따라서 "시험장 입장 성공"이지 "졸업 합격"은 아니다.
```

## 실행 기준

실행한 기본 명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_research_to_runtime_parity_until_pass \
  --as-of-date 2026-07-05 \
  --mode full_thesis_balanced \
  --mandatory-archetypes C06,C08,C15,C17,C24,C28 \
  --max-iterations 10 \
  --fail-on-c05-monoculture true \
  --fail-on-unknown-target-promoted true \
  --fail-on-required-positive-missing-over-threshold true \
  --fail-on-research-proxy-score true
```

완료된 runtime 산출물:

```text
output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01-20260707T130702Z
```

감사 재현 명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_research_to_runtime_parity_until_pass \
  --as-of-date 2026-07-05 \
  --mode full_thesis_balanced \
  --mandatory-archetypes C06,C08,C15,C17,C24,C28 \
  --max-iterations 1 \
  --output-root output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01-20260707T130702Z \
  --fail-on-c05-monoculture true \
  --fail-on-unknown-target-promoted true \
  --fail-on-required-positive-missing-over-threshold true \
  --fail-on-research-proxy-score true
```

이 감사 재현은 exit code `2`로 끝났다. 이유는 runtime 자체가 죽은 것이 아니라, 아래 필수 acceptance가 아직 실패했기 때문이다.

## Attempt 구분

완료 attempt:

```text
self-repair-01
status = COMPLETED
latest_phase = completed
event_count = 644
```

증거로 쓰면 안 되는 attempt:

```text
self-repair-02
status = RUNNING
latest_phase = planner_batch_start
event_count = 5
```

`self-repair-02`는 `self-repair-01` 감사 후 parent CLI가 같은 조건으로 다음 runtime을 다시 시작한 상태에서 중단된 partial run이다. 완료 산출물이 아니므로 Goal4 증거로 쓰면 안 된다.

운영적으로는 이것도 다음 패치 대상이다. 같은 blocker가 남아 있는데 manifest나 repair plan이 바뀌지 않은 상태로 다음 attempt를 자동 재실행하면, 실제 수리가 아니라 같은 시험을 다시 보는 일이 된다.

## Planner 감사

기준 파일:

```text
docs/operational/planner_bias_and_archetype_routing_audit_2026-07-05.json
```

결과:

```text
status = PLANNER_ARCHETYPE_ROUTING_BIAS_PASS
hypothesis_run_count = 108
real_success_hypothesis_count = 108
distinct_top1_archetype_count = 33
c05_top1_count = 3
c05_top1_share = 0.027778
planner_output_score_stage_key_count = 0
```

판정:

```text
C05-only planner 쏠림은 현재 산출물 기준으로 해소됐다.
Planner 출력에 score/stage 답안지가 섞인 흔적도 없다.
```

쉬운 예:

```text
옛날에는 선생님이 모든 학생에게 C05 문제지만 나눠준 상태였다.
이번에는 C01~C32와 R13 검사용 문제지가 골고루 배정됐다.
```

## Runtime 산출물 수

완료 attempt 01 기준:

```text
planner_runs.jsonl = 455
llm_prompts.jsonl = 108
llm_responses.jsonl = 108
source_tasks.jsonl = 827
source_task_executions.jsonl = 827
accepted_claims.jsonl = 158
claim_extractor_runs.jsonl = 112
raw_assertions.jsonl = 1710
adjudicated_claims.jsonl = 1781
stagecourt_traces.jsonl = 114
```

이 숫자는 "많이 돌렸다"는 증거일 뿐, 곧바로 "Goal4 완료"를 뜻하지 않는다. Goal4는 많은 페이지를 긁는 것이 아니라, 모든 아키타입의 운영 score/stage가 source-backed claim으로 닫히는지를 요구한다.

## 최종 Acceptance

기준 파일:

```text
docs/operational/research_to_runtime_parity_matrix_2026-07-05.json
docs/operational/census_mode_v4_full_thesis_evidence_completion_audit_v2.json
docs/operational/meaningful_full_thesis_production_acceptance.json
docs/operational/full_thesis_candidate_selection_audit_v2.json
```

현재 판정:

```text
final_status = MEANINGFUL_RUNTIME_PARITY_NOT_READY
production_full_e2r_score_path_pass = true
meaningful_full_thesis_evidence_pass = false
archetype_balanced_full_thesis_pass = false
```

중요한 분리:

```text
PRODUCTION_FULL_E2R_SCORE_PATH_PASS
= 점수 계산 경로가 닫힌 row가 있다.

MEANINGFUL_FULL_THESIS_EVIDENCE_PASS
= 필수 positive primitive와 Green gap까지 source-backed claim으로 닫힌 운영 thesis다.
```

쉬운 예:

```text
score path pass는 "답안지 양식에 점수가 적혔다"는 뜻이다.
meaningful pass는 "답안지에 근거 서류까지 붙어서 채점 가능한 상태"라는 뜻이다.
이번 결과는 첫 번째만 일부 통과했다.
```

## 핵심 수치

```text
registry_archetype_count = 36
parity_row_count = 36
full_thesis_row_count = 6
distinct_full_thesis_archetype_count = 6
c05_full_thesis_share = 0.166667
required_positive_missing_full_thesis_row_count = 5
required_positive_missing_full_thesis_row_rate = 0.833333
green_gap_full_thesis_row_count = 5
green_gap_full_thesis_row_rate = 0.833333
```

Promoted full-thesis row:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE = 1
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG = 1
C05_EPC_MEGA_CONTRACT_MARGIN_GAP = 1
C06_HBM_MEMORY_CUSTOMER_CAPACITY = 1
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD = 1
C24_BIO_TRIAL_DATA_EVENT_RISK = 1
```

필수 대표 아키타입 중 production full-thesis row가 아직 없는 항목:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
C15_MATERIAL_SPREAD_SUPERCYCLE
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

현재 hard fail:

```text
mandatory_archetype_full_thesis_missing
required_positive_missing_any_promoted_row
green_gap_any_promoted_row
balanced_candidate_selection_not_pass
```

## Mandatory Archetype 상태

| archetype | 현재 상태 | source route | full rows | runtime claims | source task claims | 차단 이유 |
|---|---|---|---:|---:|---:|---|
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | PRODUCTION_FULL_E2R_SCORE_PATH_ONLY | FULL_THESIS_SCORE_PATH_CLOSED | 1 | 5 | 7 | promoted row가 있지만 required-positive와 Green gap이 남음 |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 0 | 0 | 0 | source task는 돌았지만 accepted full-thesis claim이 없음 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | FULL_THESIS_BLOCKED_BY_REQUIRED_OR_GREEN_GAP | BLOCKED_FULL_THESIS_CANDIDATE | 0 | 3 | 3 | 일부 claim은 있으나 required/Green gap을 못 닫음 |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | PRODUCTION_FULL_E2R_SCORE_PATH_ONLY | FULL_THESIS_SCORE_PATH_CLOSED | 1 | 13 | 13 | promoted row가 있지만 required-positive와 Green gap이 남음 |
| C24_BIO_TRIAL_DATA_EVENT_RISK | MEANINGFUL_FULL_THESIS_EVIDENCE_PASS | FULL_THESIS_SCORE_PATH_CLOSED | 1 | 1 | 1 | mandatory 중 유일하게 row-level meaningful 상태 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 0 | 0 | 0 | source task는 돌았지만 accepted full-thesis claim이 없음 |

판정:

```text
필수 6개 중 C06/C17/C24는 full-thesis row까지 올라왔다.
하지만 C06/C17은 필수 증빙 gap 때문에 meaningful pass가 아니다.
C08/C15/C28은 아직 production full-thesis row가 없다.
```

## 전 아키타입 Matrix

| archetype | status | source route | seed attempts | planner top1 | source exec | runtime claims | source task claims | full rows | req missing rows | green gap rows | blockers |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | PRODUCTION_FULL_E2R_SCORE_PATH_ONLY | FULL_THESIS_SCORE_PATH_CLOSED | 3 | 3 | 42 | 33 | 39 | 1 | 1 | 1 | FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP, GREEN_GAP_ON_PROMOTED_ROW, REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROW, SOURCE_PENDING_REQUIRED_OR_GREEN_PRIMITIVES |
| C02_POWER_GRID_DATACENTER_CAPEX | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 44 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | PRODUCTION_FULL_E2R_SCORE_PATH_ONLY | FULL_THESIS_SCORE_PATH_CLOSED | 3 | 3 | 46 | 9 | 18 | 1 | 1 | 1 | FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP, GREEN_GAP_ON_PROMOTED_ROW, REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROW, SOURCE_PENDING_REQUIRED_OR_GREEN_PRIMITIVES |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 46 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | PRODUCTION_FULL_E2R_SCORE_PATH_ONLY | FULL_THESIS_SCORE_PATH_CLOSED | 3 | 3 | 44 | 6 | 12 | 1 | 1 | 1 | FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP, GREEN_GAP_ON_PROMOTED_ROW, REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROW, SOURCE_PENDING_REQUIRED_OR_GREEN_PRIMITIVES |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | PRODUCTION_FULL_E2R_SCORE_PATH_ONLY | FULL_THESIS_SCORE_PATH_CLOSED | 3 | 3 | 48 | 5 | 7 | 1 | 1 | 1 | FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP, GREEN_GAP_ON_PROMOTED_ROW, REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROW, SOURCE_PENDING_REQUIRED_OR_GREEN_PRIMITIVES |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 46 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 42 | 0 | 0 | 0 | 0 | 0 | MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW, PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 44 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 42 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C11_BATTERY_ORDERBOOK_RERATING | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 46 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 46 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 46 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 50 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C15_MATERIAL_SPREAD_SUPERCYCLE | FULL_THESIS_BLOCKED_BY_REQUIRED_OR_GREEN_GAP | BLOCKED_FULL_THESIS_CANDIDATE | 3 | 3 | 46 | 3 | 3 | 0 | 0 | 0 | FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP, MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW, SOURCE_PENDING_REQUIRED_OR_GREEN_PRIMITIVES |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 44 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | PRODUCTION_FULL_E2R_SCORE_PATH_ONLY | FULL_THESIS_SCORE_PATH_CLOSED | 3 | 3 | 42 | 13 | 13 | 1 | 1 | 1 | GREEN_GAP_ON_PROMOTED_ROW, REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROW |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 42 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 46 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 42 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 42 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C22_INSURANCE_RATE_CYCLE_RESERVE | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 42 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 44 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C24_BIO_TRIAL_DATA_EVENT_RISK | MEANINGFUL_FULL_THESIS_EVIDENCE_PASS | FULL_THESIS_SCORE_PATH_CLOSED | 3 | 3 | 46 | 1 | 1 | 1 | 0 | 0 |  |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 44 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 44 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 46 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 44 | 0 | 0 | 0 | 0 | 0 | MANDATORY_ARCHETYPE_NO_PRODUCTION_FULL_THESIS_ROW, PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | FULL_THESIS_BLOCKED_BY_REQUIRED_OR_GREEN_GAP | BLOCKED_FULL_THESIS_CANDIDATE | 3 | 3 | 44 | 11 | 11 | 0 | 0 | 0 | FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP, SOURCE_PENDING_REQUIRED_OR_GREEN_PRIMITIVES |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 46 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | FULL_THESIS_BLOCKED_BY_REQUIRED_OR_GREEN_GAP | BLOCKED_FULL_THESIS_CANDIDATE | 3 | 3 | 44 | 3 | 7 | 0 | 0 | 0 | FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP, SOURCE_PENDING_REQUIRED_OR_GREEN_PRIMITIVES |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 46 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | ARCHETYPE_DISCOVERY_TARGET_MATERIALIZATION_REQUIRED | PLANNER_ATTEMPTED_NO_SOURCE_CLOSURE | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM, TARGET_MATERIALIZATION_REQUIRED |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | ARCHETYPE_DISCOVERY_TARGET_MATERIALIZATION_REQUIRED | PLANNER_ATTEMPTED_NO_SOURCE_CLOSURE | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM, TARGET_MATERIALIZATION_REQUIRED |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | ARCHETYPE_DISCOVERY_TARGET_MATERIALIZATION_REQUIRED | PLANNER_ATTEMPTED_NO_SOURCE_CLOSURE | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM, TARGET_MATERIALIZATION_REQUIRED |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | SOURCE_ROUTE_ATTEMPTED_BUT_NO_ACCEPTED_FULL_THESIS_CLAIM | SOURCE_ROUTE_ATTEMPTED_NO_ACCEPTED_CLAIM | 3 | 3 | 44 | 0 | 0 | 0 | 0 | 0 | PLANNER_ATTEMPT_NO_ACCEPTED_CLAIM |

## 지금 무엇이 좋아졌나

1. C05 monoculture는 해소됐다.

   `c05_top1_share=0.027778`, `c05_full_thesis_share=0.166667`이다. 예전처럼 10개 production row가 전부 C05인 상태가 아니다.

2. target 없는 R13 source routing은 막혔다.

   R13 일부 row는 `TARGET_MATERIALIZATION_REQUIRED`로 멈췄다. 예전처럼 실제 종목 없이 source task나 score/stage로 넘어가는 경로를 막는 방향이 맞다.

3. source_proxy production score leak은 현재 감사에서 0이다.

   연구자료 기억이나 proxy row가 곧바로 운영 점수로 들어간 흔적은 현재 acceptance 기준에서 막혀 있다.

## 아직 무엇이 안 됐나

1. 36개 중 24개는 source route를 시도했지만 accepted full-thesis claim이 0이다.

   예: C08과 C28은 source task가 각각 42개, 44개 실행됐지만 accepted claim이 0이다. "찾아보긴 했지만 점수 칸에 들어갈 검증 claim을 못 만들었다"는 뜻이다.

2. promoted full-thesis 6개 중 5개는 required-positive 또는 Green gap이 남아 있다.

   예: C06은 full-thesis row가 1개 있지만 required-positive와 Green gap이 둘 다 남아 있다. 삼성/하이닉스 같은 C06 live 평가를 믿으려면 이 gap이 source-backed claim으로 닫혀야 한다.

3. C15는 claim 3개가 있어도 full-thesis로 승급하지 못했다.

   이건 "원자재 가격 기사" 같은 주변 claim은 잡았지만, 실제 판가 전가, realized spread, OPM/FCF bridge 같은 필수 사슬이 닫히지 않았을 가능성을 우선 봐야 한다.

4. self-repair CLI가 같은 실패 조건에서 attempt 02를 다시 시작했다.

   이건 운영 낭비이자 감사 혼선이다. blocker가 `MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING` 같은 구조적 실패이면, 다음 runtime 전에는 manifest/source task/claim extraction 수리 여부를 증명해야 한다.

## 다음 패치 우선순위

1. C08, C28의 accepted claim 0 원인을 source acquisition, claim extraction, adjudication, primitive mapping 단계별로 쪼개야 한다.

   쉬운 예: 검색 결과가 있었는데 claim이 0이면 "기사 없음"이 아니라 "기사 문장을 점수 primitive로 번역하는 과정"이 막혔을 수 있다.

2. C15의 blocked candidate를 score contribution ledger까지 추적해야 한다.

   accepted claim 3개가 어느 primitive까지 갔고, 어떤 required/Green primitive에서 멈췄는지 보여야 한다.

3. promoted row 5개는 `score path only`로만 표시하고, meaningful pass로 승격하면 안 된다.

   지금 감사 파일은 이 구분을 하고 있다. 다음 에이전트도 `PRODUCTION_FULL_E2R_SCORE_PATH_PASS`를 Goal4 완료로 읽으면 안 된다.

4. self-repair runner는 동일 manifest 재실행 방지 또는 partial attempt invalid marker를 남겨야 한다.

   완료 attempt와 partial attempt가 섞이면 나중에 "어느 run이 정답인가"가 다시 흔들린다.

5. R13 cross-archetype row는 실제 target materialization 이후에만 source route를 열어야 한다.

   쉬운 예: "회계 리스크 검사"라는 검사 과목만 있고 실제 환자 이름이 없으면 검사를 시작하면 안 된다.

## 최종 판정

이번 0705 self-repair 01은 다음을 증명했다.

```text
전 아키타입 planner 시도와 source task 실행 장부는 만들어졌다.
C05-only production 쏠림은 현재 기준으로 해소됐다.
source_proxy를 운영 점수로 쓰는 obvious leak은 현재 acceptance에서 막혔다.
```

하지만 다음은 아직 증명하지 못했다.

```text
모든 필수 대표 아키타입 C06/C08/C15/C17/C24/C28이 meaningful full thesis로 닫힘
전 C01~C32 아키타입이 source-backed claim으로 운영 score/stage까지 닫힘
required-positive/Green gap 없는 promoted row
partial run 없이 반복 가능한 self-repair 완료 루프
```

따라서 현재 Goal4 상태는:

```text
MEANINGFUL_RUNTIME_PARITY_NOT_READY
```

이다. 이 문서는 완료 보고가 아니라, 다음 패치가 어디서 시작해야 하는지 고정하는 감사 장부다.

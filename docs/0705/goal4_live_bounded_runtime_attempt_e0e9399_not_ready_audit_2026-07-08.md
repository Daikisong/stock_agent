# Goal4 Live Bounded Runtime Attempt e0e9399 NOT_READY Audit - 2026-07-08

작성 시점: 2026-07-08 KST

이 문서는 `goal4.md` 이행 상태를 확인하기 위해 2026-07-05 기준으로 실제 `BRAIN_AND_WEB_ACQUISITION_ENABLED` 경로를 다시 돌린 결과를 기록한다.

핵심 결론:

```text
이번 실행은 실제 live bounded Brain/Web 런이다.
Planner 111개, source execution 789개, claim extractor 113개, accepted claim 101개까지 실행됐다.

하지만 Goal4는 아직 완료가 아니다.
최종 verdict = NOT_READY
target_gate = full_thesis
target_gate_pass = false
```

쉬운 예:

```text
이전에는 시험 접수표만 있었는지 의심했다.
이번에는 실제로 시험장에 들어가 문제를 풀었다.
하지만 111장 중 운영용 합격 답안지는 6장뿐이고,
그 6장도 필수 첨부서류가 빠져 있어서 최종 합격은 아니다.
```

## 실행

실행 커밋:

```text
e0e9399c17ac921f1ee1b40b421c3fe7ba23c2b3
```

실행 output:

```text
output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-e0e9399
```

명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-05 \
  --universe krx \
  --output-root output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-e0e9399 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --research-brain-report-dir docs/operational \
  --brain-planner-provider real \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 111 \
  --brain-planner-success-limit 111 \
  --brain-planner-batch-size 1 \
  --brain-max-source-tasks-per-plan 5 \
  --brain-max-fetches-per-task 3 \
  --brain-accepted-claim-target 36 \
  --brain-max-distinct-candidate-attempts 111 \
  --brain-retry-max 1 \
  --brain-claim-extractor-provider auto \
  --brain-claim-extractor-timeout-seconds 180.0 \
  --brain-runtime-budget-seconds 14400.0 \
  --brain-candidate-event-seed-path docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl \
  --brain-stage-promotion-mode strict \
  --full-thesis-smoke-mode disabled \
  --target-gate full_thesis \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim true \
  --fail-on-atomic-mismatch true \
  --fail-on-semantic-guard true \
  --fail-on-critical-audit true \
  --write-operational-docs true
```

결과:

```text
returncode = 1
stdout = NOT_READY
runtime_seconds = 11241.64
```

## 무엇이 실제로 실행됐나

이번 실행은 planner-only가 아니다.

```text
seed_event_count = 111
planner_run_count = 111
planner_real_provider_success_count = 111
source_task_execution_count = 789
web_search_task_count = 158
web_fetched_document_count = 113
claim_extractor_run_count = 113
claim_extractor_provider_error_count = 0
claim_extractor_timeout_count = 0
brain_web_attempt_accepted_claim_count = 101
unique_brain_web_accepted_claim_count = 47
total_accepted_claims_jsonl_count = 139
```

좋아진 점:

```text
1. C05-only planner bias는 해소됐다.
2. C01~C32/R13 seed가 111개로 분산됐다.
3. C24 replay target인 009420 한올바이오파마가 실제 source stage에 들어갔다.
4. C28 더존비즈온도 source stage에 들어갔다.
5. LLM claim extractor는 113회 모두 real provider로 실행됐고 timeout/provider_error는 0이다.
6. leaf artifact audit는 PASS다.
```

하지만 좋아진 점은 Goal4 완료와 다르다.

```text
실제 실행됨
!= 모든 아키타입 meaningful full thesis 완성
```

## 최종 NOT_READY 이유

`readiness_verdict.json`의 최종 blockers:

```text
1. full thesis seed materialization audit failed
2. Brain/Web official-first violations reached score evidence: 1
```

`goal_completion_audit.json`의 blockers:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_smoke_execution_pending
full_thesis_production_pass_false
full_thesis_seed_materialization_audit_not_pass
machine_readable_test_result_artifact_missing
goal_requirement_matrix_pass_false
```

쉬운 예:

```text
실제 자료를 많이 가져오고 claim도 만들었다.
그런데 운영 합격 기준은 "자료를 가져왔다"가 아니라
"전 아키타입에서 필수 primitive가 source-backed claim으로 닫혔다"이다.
이 기준은 아직 통과하지 못했다.
```

## 111개 seed materialization 상태

`full_thesis_seed_materialization_audit.json` 기준:

```text
seed_event_count = 111
planner_run_seed_count = 111
real_provider_success_seed_count = 111
source_task_execution_seed_count = 102
accepted_claim_seed_count = 25
stagecourt_trace_seed_count = 24
full_thesis_promoted_seed_count = 6
verdict = FAIL
operator_materialization_status = PENDING_FULL_THESIS_MATERIALIZATION
```

상태 분포:

| status | count | 의미 |
|---|---:|---|
| FULL_THESIS_PROMOTED | 6 | StageCourt까지 가서 FULL_THESIS row가 생김 |
| STAGECOURT_READY_NOT_PROMOTED | 18 | claim/score/StageCourt는 있으나 promotion 조건 미충족 |
| ACCEPTED_CLAIM_NOT_CREATED | 77 | source는 돌았지만 score-eligible accepted claim 없음 |
| SOURCE_TASK_NOT_EXECUTED | 9 | source task 실행까지 못 감 |
| STAGECOURT_TRACE_NOT_CREATED | 1 | claim 이후 StageCourt trace가 없음 |

가장 큰 실패 축:

```text
accepted_claim_not_created_primary_failure_axis_counts:
  PRIMITIVE_GAP_UNSATISFIED = 64
  NO_SCORE_ELIGIBLE_REAL_CLAIM = 8
  NO_CLAIM_EXTRACTED = 2
  NO_FETCHED_DOCUMENT = 2
  PROVIDER_ERROR_RECORDED = 1
```

해석:

```text
대부분은 "문서를 못 가져옴"이 아니라
"가져온 문서가 해당 primitive gap을 닫는 claim으로 인정되지 않음"이다.
```

예:

```text
C28에서 소프트웨어 회사 자료를 찾았더라도
ARR, retention, renewal, RPO 같은 primitive에 직접 매핑되지 않으면 accepted claim이 아니다.
```

## 아키타입별 materialization 상태

| archetype | seeds | full | StageCourt not promoted | accepted claim not created | source not executed | trace not created | executions | accepted claims |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | 3 | 1 | 2 | 0 | 0 | 0 | 22 | 2 |
| C02_POWER_GRID_DATACENTER_CAPEX | 3 | 0 | 0 | 3 | 0 | 0 | 22 | 0 |
| C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG | 3 | 1 | 2 | 0 | 0 | 0 | 23 | 3 |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | 3 | 0 | 0 | 3 | 0 | 0 | 22 | 0 |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | 3 | 1 | 2 | 0 | 0 | 0 | 23 | 2 |
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | 3 | 1 | 2 | 0 | 0 | 0 | 24 | 1 |
| C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | 3 | 0 | 0 | 3 | 0 | 0 | 24 | 0 |
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | 3 | 1 | 0 | 2 | 0 | 0 | 24 | 6 |
| C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | 3 | 0 | 0 | 3 | 0 | 0 | 23 | 0 |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 3 | 0 | 2 | 1 | 0 | 0 | 22 | 5 |
| C11_BATTERY_ORDERBOOK_RERATING | 3 | 0 | 0 | 3 | 0 | 0 | 23 | 0 |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | 3 | 0 | 0 | 3 | 0 | 0 | 24 | 0 |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 3 | 0 | 0 | 3 | 0 | 0 | 24 | 0 |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | 3 | 0 | 0 | 3 | 0 | 0 | 24 | 0 |
| C15_MATERIAL_SPREAD_SUPERCYCLE | 3 | 0 | 1 | 2 | 0 | 0 | 23 | 1 |
| C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | 3 | 0 | 0 | 3 | 0 | 0 | 23 | 0 |
| C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | 3 | 1 | 2 | 0 | 0 | 0 | 23 | 16 |
| C18_CONSUMER_EXPORT_CHANNEL_REORDER | 3 | 0 | 0 | 3 | 0 | 0 | 24 | 0 |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | 3 | 0 | 0 | 3 | 0 | 0 | 24 | 0 |
| C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | 3 | 0 | 0 | 3 | 0 | 0 | 23 | 0 |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | 3 | 0 | 0 | 3 | 0 | 0 | 23 | 0 |
| C22_INSURANCE_RATE_CYCLE_RESERVE | 3 | 0 | 0 | 3 | 0 | 0 | 21 | 0 |
| C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | 3 | 0 | 0 | 3 | 0 | 0 | 23 | 0 |
| C24_BIO_TRIAL_DATA_EVENT_RISK | 6 | 0 | 0 | 6 | 0 | 0 | 48 | 0 |
| C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 3 | 0 | 0 | 3 | 0 | 0 | 24 | 0 |
| C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | 3 | 0 | 0 | 3 | 0 | 0 | 22 | 0 |
| C27_CONTENT_IP_GLOBAL_MONETIZATION | 3 | 0 | 0 | 3 | 0 | 0 | 24 | 0 |
| C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 3 | 0 | 1 | 2 | 0 | 0 | 23 | 2 |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 3 | 0 | 1 | 1 | 0 | 1 | 23 | 8 |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 3 | 0 | 0 | 3 | 0 | 0 | 24 | 0 |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 3 | 0 | 3 | 0 | 0 | 0 | 24 | 1 |
| C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 3 | 0 | 0 | 3 | 0 | 0 | 24 | 0 |
| R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL | 3 | 0 | 0 | 3 | 0 | 0 | 22 | 0 |
| R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |

해석:

```text
C05-only 문제는 아니다.
오히려 거의 모든 아키타입이 source execution까지 내려갔다.

하지만 대부분은 "실제 primitive에 맞는 accepted claim"을 만들지 못했다.
```

## FULL_THESIS로 승격된 6개 row

중요:

```text
아래 6개는 score path가 닫힌 row다.
하지만 meaningful full thesis pass가 아니다.
6개 전부 required_positive_missing_primitives와 green_gap_primitives가 남아 있다.
```

| symbol | company | archetype | score | stage | accepted claims | missing required positive primitives |
|---|---|---|---:|---|---:|---|
| 003380 | 하림지주 | C05 | 27.9998 | 0 | 2 | contract_amount_to_prior_sales, margin_bridge_visible |
| 005930 | 삼성전자 | C06 | 39.8333 | 0 | 1 | customer_preorder_or_allocation, hbm_capacity_constraint, hbm_capacity_pre_sold, medium_term_revision_visibility, memory_price_increase_mentioned |
| 011170 | 롯데케미칼 | C17 | 37.5 | 0 | 2 | inventory_cycle, opm_expansion_pctp |
| 047810 | 한국항공우주 | C03 | 37.0 | 0 | 2 | government_customer, order_backlog_to_sales |
| 052400 | 코나아이 | C01 | 11.9999 | 0 | 1 | contract_quality, fcf_quality_score, named_customer_quality, opm_expansion_pctp, order_backlog_to_sales |
| 058470 | 리노공업 | C08 | 50.8 | 1 | 2 | qualification_confirmed, repeat_order_confirmed, socket_or_test_demand_visible |

쉬운 예:

```text
삼성전자 C06은 HBM 관련 "무언가"가 들어와서 C06 score path는 열렸다.
하지만 고객 배정, HBM capacity pre-sold, 중기 revision visibility가 아직 검증 claim으로 닫히지 않았다.
따라서 Green은커녕 Stage2/Yellow로 말하면 안 된다.
```

## C24와 C28 상태

### C24

이번 run에서 C24는 replay-backed target으로 실제 source stage에 들어갔다.

```text
target symbols = 009420 한올바이오파마, 215600 신라젠
seed count = 6
source execution count = 48
accepted claim count = 0
status = ACCEPTED_CLAIM_NOT_CREATED 6
```

해석:

```text
C24는 이제 planner-only가 아니다.
하지만 trial quality, binary event, approval 관련 source-backed accepted claim을 아직 만들지 못했다.
```

### C28

```text
seed count = 3
source execution count = 23
accepted claim count = 2
StageCourt ready not promoted = 1
accepted claim not created = 2
full thesis promoted = 0
```

해석:

```text
C28은 accepted claim이 0이던 이전 상태보다는 전진했다.
하지만 ARR/retention/renewal/RPO 같은 required primitive를 닫는 full thesis까지는 아직 못 갔다.
```

## Brain/Web readiness gate 실패: official-first violation 1건

`brain_web_readiness_gate_audit.json` 기준:

```text
verdict = BLOCKED
official_first_violation_count = 1
```

위반 row:

```json
{
  "symbol": "001390",
  "primitive_gap": "utilization_rate",
  "source_class": "BrokerReportPublicPDF",
  "status": "EVIDENCE_OS_ACCEPTED",
  "stop_reason": "rerouted_claim_accepted_original_gap_unsatisfied",
  "task_id": "ST-001390-C15-UTIL-NEWSROOM-ORIGINAL-002"
}
```

관련 accepted claim:

```text
symbol = 001390 KG케미칼
archetype = C15_MATERIAL_SPREAD_SUPERCYCLE
source_url = https://www.hanaw.com/download/research/FileServer/WEB/info/small_cap/2017/12/11/edit_171206kgch_5.pdf
quote = "2018년도 전사 영업이익 기여는 6%로 추정하며, 증설 물량이 반영되는 2019년도는 10%"
source_task_primitive_gap = utilization_rate
accepted primitive = fcf_quality_score
satisfies_source_task = false
temporal_status = CURRENT
```

이건 문제다.

쉬운 예:

```text
원래 찾던 서류:
  "2026년 현재 KG케미칼 가동률/utilization이 어떤가?"

실제로 점수에 들어간 문장:
  "2018/2019년 영업이익 기여 추정"

그런데 파이프라인은 이걸 2026-07-05 CURRENT fcf_quality_score로 받아들였다.
```

이 문제는 예전의 "2020년 감사 이슈를 2026년 현재 hard risk로 넣는 문제"와 같은 계열이다.

```text
과거 문장을 현재 claim으로 잘못 살림
원래 primitive gap과 다른 primitive로 reroute한 뒤 score evidence로 사용
official-first gap을 일반 broker PDF claim으로 닫은 것처럼 처리
```

따라서 다음 패치에서 이 row는 반드시 점수 기여에서 제외되어야 한다.

## 현재 Stage가 있는가?

있다. 하지만 운영 stage로 쓰면 안 된다.

현재 distribution:

```text
full_thesis_stage_row_count = 6
full_e2r_verified_score_row_count = 6
event_board_non_stage0_count = 81
operational_stage_use_allowed = false
meaningful_operational_stage_pass = false
```

쉬운 예:

```text
전 종목 Census 상태판은 있다.
몇몇 종목은 claim-backed StageCourt row도 있다.
하지만 "오늘 운영 watchlist에 stage를 확정해도 된다"는 뜻은 아니다.
```

## 다음 패치 우선순위

### 1. rerouted claim 점수 사용 차단

현재 KG케미칼 사례처럼:

```text
source_task_primitive_gap = utilization_rate
accepted primitive = fcf_quality_score
satisfies_source_task = false
stop_reason = rerouted_claim_accepted_original_gap_unsatisfied
```

이런 claim은 다음 중 하나로 내려야 한다.

```text
non_representative_claim
diagnostic_only_claim
not_score_contributing_until_original_gap_closed
```

원래 task gap을 만족하지 못한 claim이 operator score에 직접 들어가면 안 된다.

### 2. 과거 broker report의 현재성 판정 강화

2017년 PDF 안의 2018/2019 추정 문장이 2026년 현재 `CURRENT`가 되면 안 된다.

패치 원칙:

```text
document_date / event_date / effective_period / as_of_date를 분리
오래된 추정치는 historical 또는 superseded/followup_required
현재 score eligible은 최신 current anchor가 있을 때만 true
```

### 3. FULL_THESIS_PROMOTED와 meaningful pass 분리 강화

현재 6개 FULL_THESIS row는 audit에서 막히지만 `operator_stage_use=FULL_THESIS_STAGE`로 표시된다.

다음 패치에서는 아래 둘을 더 분명히 나눠야 한다.

```text
score_path_closed_full_thesis_skeleton
meaningful_full_thesis_operator_stage
```

필수 positive primitive가 남아 있으면 operator stage로 쓰지 않는 것이 더 안전하다.

### 4. primitive-specific claim extraction 개선

가장 큰 실패축은 `PRIMITIVE_GAP_UNSATISFIED = 64`다.

즉 LLM과 Evidence OS는 문서를 읽었지만 이런 판단을 많이 했다.

```text
"문장은 있음"
하지만
"지금 찾던 primitive를 직접 닫는 문장은 아님"
```

다음 패치는 deterministic query 템플릿을 늘리는 것이 아니라:

```text
planner feedback에 rejected primitive/mapping reason을 더 잘 넣고
LLM이 다음 검색에서 진짜 primitive-specific source를 찾도록 해야 한다.
```

### 5. source class/provider gap 분리

현재 connector/capability audit은 pass지만, 실제 failure axis에는 다음이 많다.

```text
NO_FETCHED_DOCUMENT
PROVIDER_FAILED
SOURCE_CLASS_DOCUMENT_TYPE_MISMATCH
issuer_ir_discovery_not_configured
```

특히 C24/C23 같은 바이오 계열은 clinical trial registry, 회사 IR, 규제/승인 source route가 약하면 accepted claim이 거의 생기지 않는다.

### 6. R13 target materialization

R13 3개 그룹은 source task not executed 상태다.

```text
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM = 3 source not executed
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION = 3 source not executed
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW = 3 source not executed
```

R13은 종목형 아키타입이 아니라 cross-archetype guard라서 target materialization 규칙을 별도로 보강해야 한다.

## 다음 실행 전 완료 조건

다음 패치 후 재실행은 아래를 통과해야 한다.

```text
1. official_first_violation_count = 0
2. rerouted accepted claim이 original gap unsatisfied 상태로 score contribution에 들어가지 않음
3. old broker report historical quote가 CURRENT score evidence가 되지 않음
4. FULL_THESIS row가 required_positive_missing_primitives를 갖고 있으면 operator_stage_use를 막음
5. C24 accepted claim count > 0 또는 C24가 명확한 provider/source pending으로 남음
6. C28 StageCourt ready row가 required retention/ARR primitive gap으로 어디서 막혔는지 machine-readable하게 남음
7. R13 source task not executed 9개가 target materialization 또는 guard-runner 실행으로 닫힘
8. machine-readable test result artifact가 runner output에 포함됨
```

## 이번 결과로 절대 말하면 안 되는 것

```text
Goal4 완료
전 아키타입 runtime parity 완료
운영 stage 사용 가능
삼성전자 Green/Yellow 운영 판단 가능
C24/C28 완료
production FULL_THESIS meaningful pass
```

이번 결과로 말할 수 있는 것:

```text
실제 live bounded Brain/Web 런은 수행됐다.
Planner C05-only 편향은 해소됐다.
Source execution은 C01~C32 대부분에 도달했다.
Accepted claim과 StageCourt 일부는 생성됐다.
하지만 primitive-specific closure와 official-first/currentness guard가 아직 막고 있다.
```


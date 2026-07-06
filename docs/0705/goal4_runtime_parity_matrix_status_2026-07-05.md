# Goal4 Runtime Parity Matrix Status - 2026-07-05

## 결론

이번 패치는 goal4를 완료시킨 것이 아니라, **전 아키타입 runtime 상태판을 더 정확하게 만든 작업**이다.

쉬운 예로, 예전 표는 "환자 36명이 접수됐는지" 중심이었다. 새 표는 환자마다:

- 연구자료가 얼마나 있는지
- URL-backed 판례가 있는지
- source task가 실제로 실행됐는지
- accepted claim이 생겼는지
- full thesis row까지 닫혔는지
- 막힌 이유가 무엇인지

를 한 줄로 붙인다.

추가 패치로 source task 실행 로그의 실패 축도 붙였다. 이제 `accepted claim 0`에서 멈추지 않고, 다음처럼 왜 실패했는지까지 볼 수 있다.

```text
NO_ACCEPTED_CLAIM
NO_SCORE_ELIGIBLE_REAL_CLAIM
PRIMITIVE_GAP_UNSATISFIED
PRIMITIVE_MAPPING_REJECTED
PROVIDER_ERROR_RECORDED
```

이번 추가 패치로 `brain_claim_mapping_trace`도 매트릭스에 붙였다. 이제 source task 단위가 아니라 claim 매핑 단위로도 볼 수 있다.

```text
claim_mapping_trace_log_count
claim_mapping_accepted_trace_count
claim_mapping_rejected_trace_count
claim_mapping_top_rejection_reasons
claim_mapping_rejected_samples
claim_failure_top_modes
claim_failure_primary_mode
claim_failure_repair_hint
```

쉬운 예:

```text
source task failure axis
= 검사실에서 "검사 결과지 없음/부적합"이라고 표시한 상태

claim mapping rejected sample
= 실제 결과지 문구, 검사 항목, 불합격 사유까지 붙은 상태
```

## 새 산출물

- `docs/operational/all_archetype_runtime_parity_matrix.json`
- `docs/operational/all_archetype_runtime_parity_summary.md`
- 기존 `docs/operational/all_archetype_runtime_status_matrix*.json`에도 같은 goal4 감사 필드를 포함한다.

## 현재 전 아키타입 상태

`all_archetype_runtime_parity_matrix.json` 기준:

- registered contract: `36`
- C01~C32: `32`
- R13 cross-archetype: `4`
- memory card ready: `36`
- source route ready: `36`
- meaningful_runtime_parity_ready: `false`

runtime status 분포:

```text
SCORE_PATH_CLOSED_WITH_THESIS_GAPS: 4
SOURCE_REPAIR_REQUIRED: 28
TARGET_MATERIALIZATION_REQUIRED: 3
PLANNING_ONLY: 1
```

primary blocker 분포:

```text
ACCEPTED_CLAIM_NOT_CREATED: 27
REQUIRED_POSITIVE_MISSING: 5
CANDIDATE_SELECTOR_DID_NOT_ATTEMPT: 3
SOURCE_TASK_NOT_CREATED: 1
```

## 중요한 해석

`SCORE_PATH_CLOSED_WITH_THESIS_GAPS`는 "좋은 full thesis 통과"가 아니다.

쉬운 예:

```text
시험 답안지는 채점됐지만
필수 서술형 문제가 비어 있는 상태
```

현재 해당 상태인 대표 행:

- C01: accepted claim과 full row는 있으나 required-positive/Green gap 남음
- C03: accepted claim과 full row는 있으나 required-positive/Green gap 남음
- C05: accepted claim과 full row는 있으나 required-positive/Green gap 남음
- C06: accepted claim과 full row는 있으나 required-positive/Green gap 남음

따라서 C06도 "운영 full thesis가 의미 있게 Green/Yellow를 낸 상태"가 아니라, **점수 경로가 닫혔지만 필수 증거가 부족한 상태**다.

## 주요 canary 상태

```text
C05: SCORE_PATH_CLOSED_WITH_THESIS_GAPS / REQUIRED_POSITIVE_MISSING
C06: SCORE_PATH_CLOSED_WITH_THESIS_GAPS / REQUIRED_POSITIVE_MISSING
C08: SOURCE_REPAIR_REQUIRED / ACCEPTED_CLAIM_NOT_CREATED
C15: SOURCE_REPAIR_REQUIRED / ACCEPTED_CLAIM_NOT_CREATED
C17: SOURCE_REPAIR_REQUIRED / ACCEPTED_CLAIM_NOT_CREATED
C24: SOURCE_REPAIR_REQUIRED / ACCEPTED_CLAIM_NOT_CREATED
C28: SOURCE_REPAIR_REQUIRED / ACCEPTED_CLAIM_NOT_CREATED
```

예를 들어 C08은 연구 case `300`, URL-backed case `61`, source task `28`까지 있다. 그런데 accepted claim은 `0`이다. 즉 연구자료가 부족한 문제가 아니라, **운영 source task가 현재 원문에서 score-eligible accepted claim을 만들지 못한 문제**다.

source task execution log 기준 C08의 실제 실패 축:

```text
execution_log_count: 14
claim_mapping_trace_log_count: 53
claim_mapping_accepted_trace_count: 0
claim_mapping_rejected_trace_count: 53
claim_failure_primary_mode: ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE
claim_failure_repair_hint: REROUTE_TO_PRIMITIVE_SPECIFIC_SECTION_OR_SOURCE
NO_ACCEPTED_CLAIM: 14
NO_SCORE_ELIGIBLE_REAL_CLAIM: 11
PRIMITIVE_GAP_UNSATISFIED: 11
PRIMITIVE_MAPPING_REJECTED: 7
MAPPING_NOT_ACCEPTED: 7
PROVIDER_ERROR_RECORDED: 5
top claim rejection:
  primitive_mapping_rejected: 263
  mapping_not_accepted: 53
  source_class_document_type_mismatch: 17
```

C24/C28도 같은 패턴이다.

```text
C24:
  execution_log_count: 21
  claim_mapping_trace_log_count: 78
  claim_mapping_accepted_trace_count: 0
  claim_mapping_rejected_trace_count: 78
  claim_failure_primary_mode: ROUTE_SIGNAL_FAMILY_MISMATCH
  claim_failure_repair_hint: REPLAN_SOURCE_TASK_TO_MATCH_PRIMITIVE_FAMILY
  NO_ACCEPTED_CLAIM: 21
  NO_SCORE_ELIGIBLE_REAL_CLAIM: 15
  PRIMITIVE_GAP_UNSATISFIED: 15
  PROVIDER_ERROR_RECORDED: 9
  top claim rejection:
    primitive_mapping_rejected: 416
    mapping_not_accepted: 78

C28:
  execution_log_count: 21
  claim_mapping_trace_log_count: 60
  claim_mapping_accepted_trace_count: 0
  claim_mapping_rejected_trace_count: 60
  claim_failure_primary_mode: ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE
  claim_failure_repair_hint: REROUTE_TO_PRIMITIVE_SPECIFIC_SECTION_OR_SOURCE
  NO_ACCEPTED_CLAIM: 21
  NO_SCORE_ELIGIBLE_REAL_CLAIM: 15
  PRIMITIVE_GAP_UNSATISFIED: 15
  PROVIDER_ERROR_RECORDED: 9
  top claim rejection:
    primitive_mapping_rejected: 248
    mapping_not_accepted: 60
```

쉬운 예:

```text
source task 실행
→ 병원 검사는 예약하고 일부 검체도 채취함
→ 하지만 검사 결과지가 해당 질병 항목에 맞지 않음
→ accepted claim 0
```

따라서 다음 작업은 "source task를 더 많이 실행"이 아니라, `no_score_eligible_real_claim`과 `primitive_mapping_rejected`가 왜 생기는지 원문/primitive/source-class 단위로 좁히는 것이다.

매트릭스 JSON의 각 row에는 이제 실제 샘플도 들어간다.

```json
{
  "claim_id": "...",
  "symbol": "058470",
  "primitive_gap": "repeat_order_confirmed",
  "primitive_id": "repeat_order_confirmed",
  "mapping_status": "REJECTED",
  "source_provider": "OpenDART",
  "source_url": "https://dart.fss.or.kr/...",
  "failure_modes": [
    "ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE",
    "PRIMITIVE_MAPPING_REJECTED",
    "MAPPING_NOT_ACCEPTED"
  ],
  "repair_hint": "REROUTE_TO_PRIMITIVE_SPECIFIC_SECTION_OR_SOURCE",
  "rejection_reasons": [
    "mapping_not_accepted:REJECTED",
    "primitive_mapping_rejected:..."
  ],
  "quote_excerpt": "분기보고서 ..."
}
```

이 말은 C08의 현재 병목이 "리노공업 원문을 못 찾음"이 아니라, 찾은 DART 분기보고서 문구가 `repeat_order_confirmed` 같은 C08 필수 primitive로 accepted 되지 못했다는 뜻이다. 즉 다음 패치는 source route가 IR/고객사/수주/반복 주문 원문으로 향하게 만들거나, 현재 원문에서 실제 C08 claim이 있는데 mapper가 놓치는지 분해해야 한다.

`claim_failure_primary_mode`로 보면 다음 행동이 더 분명하다.

```text
C08:
  ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE
  → DART 표지/개요 말고 repeat order/customer quality를 직접 말하는 source/section으로 reroute 필요

C24:
  ROUTE_SIGNAL_FAMILY_MISMATCH
  → trial_quality_visible을 찾는데 공급계약 공시가 들어왔으므로 trial/endpoint/regulatory source로 source task 재계획 필요

C28:
  ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE
  → DART 표지/개요 말고 ARR/RPO/renewal/retention이 있는 IR/실적자료/리포트 route 필요
```

## next attempt planner 연결

이번 추가 패치에서는 위 failure mode를 문서에만 남기지 않고 다음 실행 입력에도 실었다.

생성/갱신된 파일:

```text
docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.json
docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.md
docs/operational/all_archetype_next_runtime_attempt_plan.json
docs/operational/all_archetype_next_runtime_source_tasks_2026-07-05.jsonl
docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl
```

새로 들어간 필드:

```text
previous_claim_failure_primary_mode
previous_claim_failure_repair_hint
previous_claim_failure_top_modes
source_route_repair_required
source_route_repair_actions
planner_failure_feedback
```

쉬운 예:

```text
이전 상태:
  C08 source task
  → "named_customer_quality를 찾아라"

이번 상태:
  C08 source task
  → "named_customer_quality를 찾아라"
  → "지난번에는 DART 표지/개요 같은 generic disclosure만 잡혀서 실패했다"
  → "generic disclosure를 점수 근거로 재사용하지 말고 primitive-specific source/section을 LLM이 다시 찾게 하라"
```

현재 next attempt plan 요약:

```text
source_task_count: 111
source_route_repair_task_count: 99
REROUTE_TO_PRIMITIVE_SPECIFIC_SECTION_OR_SOURCE: 63
REPLAN_SOURCE_TASK_TO_MATCH_PRIMITIVE_FAMILY: 12
TIGHTEN_TARGET_ENTITY_FILTER_OR_RELATION_ADJUDICATION: 9
FIX_SOURCE_CLASS_OR_DOCUMENT_TYPE_ROUTE: 3
INSPECT_MAPPER_VS_EVIDENCE_CONTRACT_FOR_THIS_PRIMITIVE: 12
```

대표 행:

```text
C08:
  previous_claim_failure_primary_mode: ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE
  repair_hint: REROUTE_TO_PRIMITIVE_SPECIFIC_SECTION_OR_SOURCE
  source_route_repair_actions:
    - DO_NOT_ACCEPT_GENERIC_DISCLOSURE_PROFILE_AS_PRIMITIVE_EVIDENCE
    - ASK_LLM_FOR_PRIMITIVE_SPECIFIC_SOURCE_OR_SECTION_ROUTE
    - FETCH_FULL_SOURCE_ANCHOR_BEFORE_MAPPING_RETRY

C24:
  previous_claim_failure_primary_mode: ROUTE_SIGNAL_FAMILY_MISMATCH
  repair_hint: REPLAN_SOURCE_TASK_TO_MATCH_PRIMITIVE_FAMILY
  source_route_repair_actions:
    - ASK_LLM_TO_MATCH_SOURCE_FAMILY_TO_PRIMITIVE_FAMILY
    - REJECT_PREVIOUS_MISMATCHED_SOURCE_FAMILY_AS_SCORE_INPUT
    - REPLAN_SOURCE_TASK_BEFORE_MAPPING_RETRY
```

중요한 점:

```text
이전 rejected claim은 점수 근거가 아니다.
이전 rejected claim은 다음 LLM planner가 같은 실패를 반복하지 않도록 주는 feedback이다.
```

## Research Brain planner context 연결

위 feedback은 seed/source task 파일에만 있는 것이 아니라 실제 Research Brain v4 planner prompt context에도 들어가도록 연결했다.

패치된 경로:

```text
all_archetype_next_runtime_seed_events_2026-07-05.jsonl
→ CandidateEventV2.structured_payload
→ _evidence_context_by_event()
→ full_thesis_queue_context
→ build_v4_planner_prompt_payload()
→ LLM planner prompt
```

planner context에 노출되는 안전 필드:

```text
previous_claim_failure_primary_mode
previous_claim_failure_repair_hint
previous_claim_failure_top_modes
source_route_repair_required
source_route_repair_actions
planner_failure_feedback
```

단, `planner_failure_feedback` 안에서도 점수/Stage로 오해될 수 있는 `score_evidence_allowed_from_previous_rejected_claims` 같은 필드는 prompt context에서 제외한다.

쉬운 예:

```text
C08 seed:
  previous_claim_failure_primary_mode = ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE

LLM planner가 보게 되는 의미:
  "지난번에는 DART 표지/회사 개요 같은 일반 문서로 실패했다.
   이번에는 repeat_order/customer_quality를 직접 말하는 IR/원문/리포트 section을 찾아라."
```

추가 prompt rule:

```text
If existing_evidence_summary.full_thesis_queue_context.planner_failure_feedback is non-empty,
treat it as source-route repair guidance only. It is not score evidence.
```

## 2026-07-05 next-attempt 실제 실행 결과

위 next attempt seed/source task를 실제 Census/Research Brain 경로에 넣어 한 번 돌렸다.

실행 루트:

```text
output/census_v4/2026-07-05-goal4-repair-feedback-next-runtime-attempt
```

실행 조건 요약:

```text
as_of_date: 2026-07-05
run_mode: BRAIN_AND_WEB_ACQUISITION_ENABLED
brain_web_mode: enabled
planner_provider: real
source_acquisition: live_full_bounded
seed_events: docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl
target_gate: full_thesis
```

최종 runtime progress:

```text
status: COMPLETED
runtime_elapsed_seconds: 4704.916067
runtime_budget_exhausted: false
planner_run_count: 458
real_provider_success_count: 64
source_task_execution_count: 450
accepted_claim_count: 28
watchlist_item_count: 458
```

중요한 해석:

```text
이 실행은 "완료"가 아니라 "실패 위치를 실제 runtime에서 더 좁힌 실행"이다.
```

쉬운 예:

```text
예전:
  "C08은 claim이 없다"

이번:
  "C08은 planner seed 3개가 들어갔고,
   일부 source task까지 갔지만,
   named_customer_quality/repeat_order_confirmed claim을 못 만들었다"
```

## 최신 acceptance verdict

`docs/operational/census_mode_v4_acceptance_report.md` 기준 최종 판정:

```text
Final verdict: NOT_READY
target_gate_pass: false
goal_completion_ready: false
Brain/Web attempt verdict: ATTEMPTED_NOT_CUTOVER_READY
Brain/Web readiness gate: BLOCKED
full_thesis_production_pass_allowed: false
```

대표 blocker:

```text
web/LLM accepted claim count is zero
Brain/Web source task budget caps were exceeded: 2
Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

추가 감사 패치 후 promoted row 자체의 snapshot 오귀속 blocker는 제거됐다.
현재 promoted 삼성전자 row가 참조한 문서는 CompanyGuide와 OpenDART이고, snapshot 문서 2개는 unpromoted 후보 쪽에만 남아 있다.

즉 111개 seed를 실제로 넣고 돌렸지만, 운영 cutover 기준에서는 아직 통과가 아니다.

쉬운 예:

```text
서류 접수 111건
→ 64건은 담당자가 실제로 봄
→ 450개 source task 실행
→ 일부 claim은 생김
→ 하지만 "웹/LLM이 직접 찾아낸 운영 admissible claim"은 0
→ 운영 합격은 차단
```

## seed materialization 결과

`docs/operational/census_mode_v4_full_thesis_seed_materialization_audit.json` 기준:

```text
seed_event_count: 111
planner_run_seed_count: 111
real_provider_success_seed_count: 64
source_task_execution_seed_count: 64
stagecourt_trace_seed_count: 9
accepted_claim_seed_count: 9
full_thesis_promoted_seed_count: 1
actual_materialization_pass_allowed: false
ledger_integrity_pass_allowed: false
verdict: FAIL
```

status 분포:

```text
ACCEPTED_CLAIM_NOT_CREATED: 55
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS: 47
STAGECOURT_READY_NOT_PROMOTED: 8
FULL_THESIS_PROMOTED: 1
```

아키타입별 canary:

```text
C06:
  3 seed
  FULL_THESIS_PROMOTED: 1
  STAGECOURT_READY_NOT_PROMOTED: 2

C08:
  3 seed
  ACCEPTED_CLAIM_NOT_CREATED: 2
  PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS: 1

C15:
  3 seed
  ACCEPTED_CLAIM_NOT_CREATED: 2
  PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS: 1

C17:
  3 seed
  ACCEPTED_CLAIM_NOT_CREATED: 2
  PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS: 1

C24:
  3 seed
  ACCEPTED_CLAIM_NOT_CREATED: 3

C28:
  3 seed
  ACCEPTED_CLAIM_NOT_CREATED: 2
  PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS: 1

C31:
  3 seed
  STAGECOURT_READY_NOT_PROMOTED: 3
```

해석:

```text
C05만 돌던 문제는 최신 실행에서 그대로 반복되지는 않았다.
실제로 C06/C08/C15/C17/C24/C28/C31 등 여러 아키타입 seed가 runtime에 들어갔다.

하지만 대부분은 accepted claim을 만들지 못하거나,
StageCourt까지 가도 production full thesis로 승격되지 못했다.
```

## production full-thesis row 최신 상태

`docs/operational/census_mode_v4_full_thesis_production_audit.json` 기준:

```text
production_full_thesis_row_count: 1
production_symbols: [005930]
production_pass_allowed: false
production_full_thesis_row_with_required_positive_missing_primitives_count: 1
production_full_thesis_row_with_green_gap_primitives_count: 1
```

실제 production row:

```text
symbol: 005930
company: 삼성전자
primary_archetype: C06_HBM_MEMORY_CUSTOMER_CAPACITY
stage_scope: FULL_THESIS
score_scope: FULL_E2R_100
operator_stage_use: FULL_THESIS_STAGE
operator_score_use: FULL_E2R_SCORE
verified_score: 44.1667
canonical_stage/base_stage: 1
score_valid_status: FINAL
score_source: BRAIN_WEB_PRODUCTION_FULL_THESIS_STAGECOURT
stagecourt_trace_id: SCT-BRAIN-1e999f3308d1bc0f3d6b
candidate_event_id: CEV4-RTATTEMPT-7f33db04360ffa26109b
```

하지만 C06 Green primitive는 아직 비어 있다.

```text
present_green_primitives:
  revenue_visibility_contract

missing_green_primitives:
  customer_preorder_or_allocation
  hbm_capacity_constraint
  hbm_capacity_pre_sold
```

쉬운 예:

```text
"삼성전자 C06 full-thesis row가 하나 생김"
은 맞다.

하지만
"삼성전자 C06 thesis가 충분히 검증되어 Yellow/Green 후보가 됨"
은 아니다.

현재는 한 장의 답안지가 채점대에 올라갔지만,
핵심 서술형 3문제가 비어 있는 상태다.
```

## 삼성전자/하이닉스 최신 분리

`docs/operational/census_mode_v4_sample_leaf_bundle.jsonl` 기준:

```text
삼성전자 005930:
  stage_scope: FULL_THESIS
  primary_archetype: C06_HBM_MEMORY_CUSTOMER_CAPACITY
  verified_score: 44.1667
  operator_stage_use: FULL_THESIS_STAGE

SK하이닉스 000660:
  stage_scope: CENSUS_EVENT_BOARD
  primary_archetype: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  verified_score: None
  score_scope: EVENT_WEIGHTED_PARTIAL
  operator_stage_use: NOT_FULL_THESIS_STAGE
```

즉 하이닉스는 최신 실행에서도 production full-thesis row가 아니다. event board row일 뿐이다.

쉬운 예:

```text
삼성전자:
  정식 시험지 1장이 생겼지만 점수가 낮고 핵심 문항이 비어 있음

하이닉스:
  출석부/관찰 기록은 있지만 정식 시험지가 아직 없음
```

## score formula trace 재검증

promoted 삼성전자 full-thesis row는 `verified_score=44.1667`로 표시된다.

해당 trace가 참조하는 score contribution ID:

```text
SCON-bfd7a3d6631bb56363d3
SCON-d7019aca95b85d4c2f1d
SCON-a4e2031c4cd3cfea3aed
SCON-16f929b96dd4c8288ac2
SCON-be2c2c174d0496c5bd90
SCON-f662a81b9edd62c4b24f
```

persisted `score_contributions.jsonl`에서 확인되는 raw component:

```text
eps_fcf_explosion: 20.0 / 20.0
earnings_visibility: 6.6667 / 20.0
bottleneck_pricing: 5.0 / 20.0
market_mispricing: 3.75 / 15.0
valuation_rerating: 3.75 / 15.0
information_confidence: 1.6667 / 5.0
raw sum: 40.8334
```

처음 수동 감사에서는 `44.1667 != 40.8334`만 보고 score trace closure 문제처럼 보였다.
하지만 이는 단순 raw 합계와 총점의 비교라서 정확한 검사가 아니었다.
C06 아키타입 runtime weight를 적용해 DeterministicScorer로 재채점하면 다음처럼 StageCourt 점수와 일치한다.

```text
stagecourt trace score_interval: 44.1667
referenced persisted contribution raw sum: 40.8334
deterministic recompute verified_score: 44.1667
weighted component sum: 44.1667
scoring_version: census-v4-audit-recompute:e2r_2_2_rolling_calibrated:archetype_weight:C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

따라서 이 row의 점수 숫자 자체는 `raw component -> C06 runtime weight -> deterministic clamp` 경로로 재현된다.
이번 패치에서 감사 기준도 `raw sum == total`이 아니라 `referenced score_contributions를 deterministic 재채점한 값 == score_interval.lower`로 바꿨다.

쉬운 예:

```text
과목 원점수 합은 40.8334다.
그런데 이 시험은 C06 전용 배점표를 쓰기 때문에 weighted 총점은 44.1667이 된다.

따라서 과목 원점수 합과 총점이 다르다는 사실만으로 오류라고 보면 안 된다.
반드시 같은 배점표로 다시 채점했을 때 총점이 재현되는지를 봐야 한다.
```

다만 latest production row도 Goal4 완료 증거로 쓰면 안 된다.
이유는 점수 산식 불일치나 promoted snapshot 오귀속이 아니라, required positive primitive 부족과 Brain/Web readiness gate 미통과다.
즉 계산기는 같은 답을 다시 내고 promoted row의 직접 source도 DART/CompanyGuide로 확인됐지만, 아직 전 아키타입 meaningful runtime parity가 증명되지 않았다.

## 이전 C05-only 문제에 대한 최신 답

이전 감사 질문:

```text
왜 production FULL_THESIS 10개가 전부 C05인가?
```

최신 실행 기준으로는 이 상태가 그대로 유지되지는 않는다.

```text
latest production_full_thesis_row_count: 1
latest production_symbols: [005930]
latest production primary_archetype: C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

다만 이것이 문제가 해결됐다는 뜻은 아니다.

정확한 현재 문제:

```text
예전 문제:
  full thesis row가 C05에 편중됨

현재 문제:
  C05 편중은 깨졌지만,
  production full-thesis row가 1개뿐이고,
  그 1개도 required-positive/Green primitive가 비어 있으며,
  score formula trace도 추가 감사가 필요함
```

주요 아키타입 blocked reason:

```text
C06:
  삼성전자 row 1개 promoted.
  하지만 customer_preorder_or_allocation, hbm_capacity_constraint, hbm_capacity_pre_sold가 UNKNOWN.

C08:
  named_customer_quality/repeat_order_confirmed가 accepted claim으로 닫히지 않음.

C15:
  spread_expansion/utilization_rate가 accepted claim으로 닫히지 않음.

C17:
  raw assertion은 많이 뽑았지만 spread_expansion/utilization_rate accepted claim이 0.

C24:
  approval_not_confirmed/binary_event_unresolved/trial_quality_visible 모두 accepted claim 0.

C28:
  nrr/retention_or_renewal accepted claim 0, arr_growth_visible은 planner success 미달.

C31:
  accepted claim은 일부 있으나 StageCourt_READY_NOT_PROMOTED.
```

## 성공과 실패를 분리한 결론

성공한 것:

```text
1. next attempt feedback이 seed/source task/planner prompt까지 실제로 전달됐다.
2. 111개 seed가 Research Brain에 소비됐다.
3. real planner call 111개, 성공 64개가 기록됐다.
4. source task 450개가 실행됐다.
5. C05 외 C06/C08/C15/C17/C24/C28/C31 등이 runtime에 들어갔다.
6. production full-thesis row가 하나 materialized 됐다.
```

실패한 것:

```text
1. Goal4 target_gate=full_thesis는 여전히 blocked.
2. web/LLM accepted claim은 0개라 Brain/Web cutover 불가.
3. full thesis production pass_allowed=false.
4. 삼성전자 production row도 C06 Green/required-positive primitive가 비어 있다.
5. 하이닉스는 production full-thesis row가 아니다.
6. persisted score contribution 합과 stagecourt score_interval이 수동 감사에서 맞지 않는다.
```

한 줄 결론:

> 최신 실행은 C05-only 편중을 일부 깨고 C06 production row까지 만들었지만, 운영 가능한 full thesis 완성은 아니다. 지금은 "실제 runtime이 어디서 막히는지"가 더 명확해진 상태이며, 다음 패치는 accepted claim 생성과 score trace closure를 동시에 고쳐야 한다.

## 자기참조 버그 수정

새로 만든 parity matrix/summary가 연구 reverse scanner에 다시 흡수되는 문제가 발견됐다.

잘못된 흐름:

```text
all_archetype_runtime_parity_matrix.json 생성
→ docs/operational/*.json scanner가 이를 연구자료로 읽음
→ research_reverse_case_inventory record_count가 11425에서 11466으로 부풀어 오름
```

패치:

```text
GENERATED_GOAL4_PREFIXES에 all_archetype_runtime_parity_ 추가
```

검증:

```text
research_case_count: 11425
documented_corpus_size: 2659
parity matrix가 research inventory source_file로 재흡수되지 않음
```

## 남은 실제 Goal4 blocker

아직 goal4 complete가 아닌 이유:

1. C08/C15/C17/C24/C28 등 대부분 아키타입은 source task는 실행됐지만 accepted claim이 0이다.
2. C01/C03/C05/C06/C31 일부는 accepted claim이 있거나 StageCourt까지 갔지만 required-positive/Green primitive가 남아 있다.
3. R13 일부는 실제 target symbol materialization 전 단계에 머물러 있다.
4. 최신 production full-thesis row는 1개뿐이고, 그 1개도 required-positive/Green gap이 남아 있다.
5. full thesis refresh queue 후보는 84개지만, queue row는 운영 Stage가 아니다.
6. blocked production candidate 8개는 follow-up source task/seed로 다시 내려갔고 아직 점수/Stage credit을 받으면 안 된다.

## 테스트

통과:

```bash
PYTHONPATH=src python -m unittest tests.test_all_archetype_next_attempt_plan tests.test_all_archetype_runtime_execution_manifest tests.test_research_to_runtime_parity_goal4 -v
```

관련 테스트 결과:

```text
Ran 21 tests in 20.887s
OK
```

planner context 연결 추가 검증:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes tests.test_all_archetype_next_attempt_plan tests.test_all_archetype_runtime_execution_manifest tests.test_research_to_runtime_parity_goal4 -v
```

결과:

```text
Ran 97 tests in 30.476s
OK
```

이후 전체 테스트도 통과했다.

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

전체 결과:

```text
Ran 5260 tests in 437.389s
OK
```

## 다음 작업 방향

이번 패치에서 `claim_failure_primary_mode`는 next attempt planner와 seed/source task feedback까지 연결됐다. 하지만 아직 다음 실행에서 accepted claim이 실제로 생성된 것은 아니므로 Goal4 완료는 아니다.

우선순위:

1. next attempt seed/source task를 실제 Census/Brain 실행에 넣어 C08/C15/C17/C24/C28 canary부터 accepted claim 1개 이상을 만든다.
2. `ROUTE_GENERIC_DISCLOSURE_NOT_PRIMITIVE_EVIDENCE` 행에서 generic DART cover/profile이 다시 들어오면 실행 실패로 audit한다.
3. `ROUTE_SIGNAL_FAMILY_MISMATCH` 행에서 primitive family와 source family가 계속 어긋나면 planner feedback loop를 더 강하게 만든다.
4. `source_class_document_type_mismatch`와 `source_task_provider_error_score_block`을 source family별로 external blocker인지 route 설계 문제인지 분리한다.
5. required-positive gap이 남은 C01/C03/C05/C06/C31의 missing primitive별 follow-up task를 actual source/claim으로 연결한다.

한 줄로 말하면:

> 지금은 전 아키타입에 "어느 단계와 어떤 실패 축에서 막혔는지"뿐 아니라 "어떤 claim/quote가 왜 rejected 됐고 어떤 계층을 고쳐야 하는지"가 붙었고, 그 정보가 다음 seed/source task까지 전달된다. 다음은 이 feedback을 실제 실행해서 canary부터 accepted claim을 만들어야 한다.

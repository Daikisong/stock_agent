# 2026-07-01 Census v4 Readiness / Audit Packet

이 폴더는 `output/census_v4/2026-07-01`을 다음 에이전트가 빡세게 검증할 수 있게 만든 감사 패킷이다.

## 2026-07-03 v106 최신 교차검증 패킷

최신 상세 문서:

```text
docs/0701/census_v4_0701_v106_stage_existence_full_thesis_gap_cross_review_and_patch_direction_2026-07-03.md
```

대상 산출물:

```text
output/census_v4/2026-07-01-v105-live-bounded-rerun-after-extractor-retry
```

핵심 결론:

```text
Stage가 아예 없는 것은 아니다.
하지만 운영자가 투자 Stage로 쓸 수 있는 FULL_THESIS Stage는 아직 0개다.

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
```

삼성전자 / SK하이닉스:

```text
삼성전자 005930:
  stage_scope = BRAIN_WEB_PARTIAL
  canonical_stage = 1
  event_evidence_score = 44.1667
  operator_stage_use = NOT_FULL_THESIS_STAGE
  full_thesis_stage = FULL_THESIS_NOT_RUN

SK하이닉스 000660:
  stage_scope = BRAIN_WEB_PARTIAL
  canonical_stage = 2
  event_evidence_score = 75.8333
  operator_stage_use = NOT_FULL_THESIS_STAGE
  full_thesis_stage = FULL_THESIS_NOT_RUN
```

FULL_THESIS production runner:

```text
candidate_row_count = 23
blocked_candidate_count = 23
promoted_full_thesis_row_count = 0

all blocker = missing_green_gate_primitives

missing primitive top:
  margin_bridge_visible              19
  contract_duration_months           17
  contract_amount_to_prior_sales     13
  hbm_capacity_constraint             2
```

follow-up:

```text
full_thesis_blocker_follow_up_seed_events = 55
full_thesis_blocker_follow_up_source_tasks = 55

이 seed들은 점수 재료가 아니라 다음 Research Brain planner input이다.
score_evidence_allowed = false
stage_promotion_allowed_before_execution = false
```

v106 코드 패치:

```text
full-thesis blocker follow-up seed row에 top-level 감사 필드를 추가했다.

follow_up_task_id
follow_up_archetype_id
follow_up_primitive_gap

점수/Stage 승격 조건은 바꾸지 않았다.
```

검증:

```text
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_stage_promotion_gate -v

Ran 17 tests
OK
```

다음 패치 방향:

```text
P0. v105에서 만든 follow-up seed 55개를 실제 2차 Brain/Web attempt로 연결한다.
P1. 삼성전자/SK하이닉스 FULL_THESIS smoke를 planned task가 아니라 executed source-backed chain으로 닫는다.
P2. C05 계약금액/계약기간/margin bridge가 DART/KIND 원문에서 닫히는지 먼저 조사한다.
P3. all-archetype replay를 6/32에서 32/32 source-backed positive + guard replay로 확장한다.
```

쉬운 예:

```text
지금은 "추가 검사 필요" 오더가 55개 발행된 상태다.
하지만 그 추가 검사가 같은 run 안에서 아직 실행되지 않았다.
다음 패치는 오더를 실제 검사로 돌리고, 결과가 나오면 최종 진단서(FULL_THESIS)를 다시 쓰는 것이다.
```

## 2026-07-03 v105 최신 상태

최신 상세 문서:

```text
docs/0701/census_v4_0701_v105_live_bounded_brainweb_pass_full_thesis_blockers_and_mapping_audit_patch_2026-07-03.md
```

대상 산출물:

```text
output/census_v4/2026-07-01-v105-live-bounded-rerun-after-extractor-retry
```

최신 결론:

```text
Brain/Web evidence pass는 됐다.
하지만 운영용 FULL_THESIS Stage row는 아직 0개다.

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

쉬운 예:

```text
BRAIN_WEB_PARTIAL = 일부 검사 결과
FULL_THESIS = 최종 진단서

v105는 일부 검사 결과가 실제 원문/claim/StageCourt trace까지 이어지는 것은 증명했다.
하지만 최종 진단서는 아직 0장이다.
```

삼성전자 / SK하이닉스:

```text
삼성전자 005930:
  stage_scope = BRAIN_WEB_PARTIAL
  canonical_stage = 1
  event_evidence_score = 44.1667
  accepted_claim_count = 3
  operator_stage_use = NOT_FULL_THESIS_STAGE
  full_thesis_stage = FULL_THESIS_NOT_RUN

SK하이닉스 000660:
  stage_scope = BRAIN_WEB_PARTIAL
  canonical_stage = 2
  event_evidence_score = 75.8333
  accepted_claim_count = 6
  operator_stage_use = NOT_FULL_THESIS_STAGE
  full_thesis_stage = FULL_THESIS_NOT_RUN
```

주의:

```text
위 canonical_stage 1/2는 운영 Stage가 아니다.
둘 다 BRAIN_WEB_CLAIM_BACKED_PARTIAL 상태 row다.
```

v105에서 닫은 것:

```text
readiness_verdict:
  target_gate = brain_web
  target_gate_pass = true
  brain_web_evidence_pass = true
  meaningful_operational_stage_pass = false
  full_thesis_production_pass = false

claim extractor:
  runs = 47
  SUCCESS = 47
  provider_error = 0
  timeout = 0

source_connector_capability:
  verdict = SOURCE_CONNECTOR_CAPABILITY_PASS
  blocking_full_thesis_source_classes = []
  non_executable_full_thesis_source_classes = ["IssuerIR"]

primitive_state_chain:
  verdict = PASS
  critical_count = 0
  claim_with_multi_accepted_primitive_count = 3
```

이번 추가 패치:

```text
accepted_claims.jsonl은 claim_id compatibility view라서
같은 claim의 여러 accepted primitive mapping을 대표 primitive_id 하나로 찌그러뜨릴 수 있다.

primitive_state_chain_audit가 accepted_claims.primitive_id 하나만 보던 문제를 고쳐,
brain_claim_mapping_trace.jsonl의 accepted mapping ledger까지 보고 검증하게 했다.

즉 PrimitiveState.primitive_id가 해당 claim의 accepted mapping row 중 하나와 맞으면 통과한다.
accepted mapping row 어디에도 없는 primitive이면 여전히 FAIL이다.

주의:
  brain_claim_mapping_trace.accepted_primitive_ids는 task/execution summary라서 proof로 쓰지 않는다.
  Brain trace가 있는 claim은 claim_id + primitive_state_id + symbol + row primitive_id가 직접 맞아야 통과한다.
```

남은 blocker:

```text
goal_completion_ready = false

blockers:
  - full_thesis_smoke_pending
  - full_thesis_smoke_execution_pending
  - full_thesis_production_pass_false
  - full_thesis_seed_promotion_pass_false
  - source_backed_replay_parity_all_archetypes_pending
  - goal_requirement_matrix_pass_false

goal_requirement_matrix:
  pass = 17
  pending = 4
  fail = 0

pending_gate_ids:
  - FULL_THESIS_SMOKE_PASS
  - FULL_THESIS_PRODUCTION_PASS
  - FULL_THESIS_SEED_PROMOTION_PASS
  - ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
```

검증:

```text
Focused tests after mapping audit hardening = 30 OK

Full unittest artifact:
  status = OK
  test_count = 5139
  failed_count = 0
  error_count = 0
  duration_seconds = 231.2116
```

다음 패치의 방향:

```text
Brain/Web pass를 다시 증명하는 것이 아니라,
BRAIN_WEB_PARTIAL에서 멈춘 evidence chain을 FULL_THESIS 운영 row까지 닫아야 한다.

필수 chain:
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

## 2026-07-03 v104 이전 상태

최신 상세 문서:

```text
docs/0701/census_v4_0701_v104_stage_existence_extractor_retry_patch_and_final_review_packet_2026-07-03.md
```

최신 결론:

```text
Stage map/status row는 있다.
하지만 운영용 FULL_THESIS Stage row는 0개다.

v101/v102/v103 stage_scope:
  CENSUS_EVENT_BOARD      3369
  BRAIN_OFFICIAL_PARTIAL    16
  BRAIN_WEB_PARTIAL          6
  FULL_THESIS                0

operator_stage_use:
  NOT_FULL_THESIS_STAGE   3391

operator_score_use:
  NOT_FULL_E2R_SCORE      3391
```

쉽게 말하면:

```text
출석부/상태판은 있다.
일부 검사 결과도 있다.
하지만 최종 진단서, 즉 FULL_THESIS 운영 Stage는 아직 없다.
```

v103에서 닫은 것:

```text
Brain/Web trace rows missing stagecourt_trace_id 4개는
비대표 accepted claim이라 StageCourt가 없어도 되는 행으로 분리했다.

v103 readiness replay:
  brain_trace_missing_stagecourt_ref_count = 0
  brain_trace_nonrepresentative_missing_stagecourt_ref_count = 4
```

v104에서 코드로 고친 것:

```text
production claim extractor가 긴 문서를 source_text[:12000]으로 단순 절단하던 문제 수정.
contract-blind head/signal/tail compact prompt를 쓰고,
timeout 시 3600자 compact prompt로 한 번 재시도한다.

점수/Stage/Green gate/primitive_gap은 여전히 extractor prompt에 넣지 않는다.
```

남은 blocker:

```text
v101/v102/v103 Brain/Web artifact 기준:
  LLM claim extractor timeout rows = 5
  same rows counted as provider_error = 5

v104 코드는 이 blocker를 줄이기 위한 패치다.
하지만 v104 live rerun 전까지 artifact blocker가 사라진 것은 아니다.

운영 readiness 기준:
  FULL_THESIS row = 0
  FULL_E2R_100 score row = 0
  operator_stage_use FULL_THESIS_STAGE = 0
  all-archetype source-backed replay = 6/32 수준
```

검증:

```text
Focused extractor tests = 16 OK
Related Research Brain / readiness tests = 55 OK
Review-fix focused tests = 36 OK
Full unittest after v104 review fixes = 5134 OK
  Ran 5134 tests in 234.621s
```

주의:

```text
아래의 v102/v101 섹션은 당시 기준 기록이다.
특히 v101 policy replay 숫자(BRAIN_WEB_PARTIAL=2, BRAIN_OFFICIAL_PARTIAL=19)는
v101 live bounded rerun 숫자(BRAIN_WEB_PARTIAL=6, BRAIN_OFFICIAL_PARTIAL=16)와
기준 artifact가 다르다.
외부 리뷰에서는 항상 문서가 가리키는 output path를 같이 인용해야 한다.
```

## 2026-07-03 v102 최신 상태

최신 상세 문서:

```text
docs/0701/census_v4_0701_v102_live_bounded_rerun_official_partial_audit_patch_and_remaining_blockers_2026-07-03.md
```

최신 사실표:

```text
v101 live bounded rerun =
  output/census_v4/2026-07-01-v101-live-bounded-rerun

v102 audit replay from v101 =
  output/census_v4/2026-07-01-v102-stage-scope-audit-replay-from-v101

v101 live verdict =
  NOT_READY

v101 live stage_scope =
  CENSUS_EVENT_BOARD      3369
  BRAIN_WEB_PARTIAL          6
  BRAIN_OFFICIAL_PARTIAL    16
  FULL_THESIS                0

v101 live leaf audit critical =
  stage_scope_invalid_count = 16
  official_claim_but_recent_official_event_zero_count = 19

v102 replay leaf audit after count + sample regeneration =
  PASS
  critical_nonzero = {}

full thesis =
  promoted_full_thesis_row_count = 0
  operator_stage_use = NOT_FULL_THESIS_STAGE for all 3391 rows
  operator_score_use = NOT_FULL_E2R_SCORE for all 3391 rows
```

쉽게 말하면:

```text
Stage가 있는 애들은 있다.
하지만 아직 "운영 최종 Stage"가 있는 것은 아니다.

삼성전자:
  CENSUS_EVENT_BOARD Stage1, event score 4.0, not FULL_THESIS

SK하이닉스:
  BRAIN_WEB_PARTIAL Stage1, event score 60.0, not FULL_THESIS
```

v102에서 고친 것:

```text
1. leaf auditor가 BRAIN_OFFICIAL_PARTIAL을 invalid scope로 오판하던 문제 수정.
2. official claim 기반 partial row에 official_source_task_count/document_count를 0으로 쓰던 문제 수정.
3. 전체 테스트 5127개 OK.
```

아직 남은 blocker:

```text
1. LLM claim extractor timeout/provider_error 5개.
2. Brain/Web trace rows missing stagecourt_trace_id 4개.
3. FULL_THESIS production row 0개.
4. all-archetype source-backed replay 6/32.
```

가장 중요한 원칙은 하나다.

```text
Stage row가 있다고 해서 FULL_THESIS 운영 Stage가 있다는 뜻은 아니다.
최신 v101 policy replay 기준에는 Brain StageCourt trace 21개가
부분 Stage row로 상태판에 보인다.
`BRAIN_WEB_PARTIAL` 2개, `BRAIN_OFFICIAL_PARTIAL` 19개다.
하지만 `FULL_THESIS`는 여전히 0개다.
모든 row의 `operator_stage_use`는 `NOT_FULL_THESIS_STAGE`이고,
모든 row의 `operator_score_use`는 `NOT_FULL_E2R_SCORE`다.
즉 v101은 "부분 Stage 존재를 상태판에 올리는 문제"를 고쳤지만,
운영 full thesis 점수/Stage를 만든 것은 아니다.
v100의 핵심 blocker였던 official-only trace의 run-global promotion 차단은
v101에서 lane 분리로 해소됐다. 다만 이것은 replay 검증이며,
v101 코드로 full live bounded rerun을 다시 해야 최종 산출물 truth가 갱신된다.
```

점수 증거 원칙도 반드시 같이 읽어야 한다.

```text
CensusAssessmentEvent / CandidateEvent / CensusEvent는 행정적 발견, 분류, 라우팅 이벤트다.
이 객체 자체는 score evidence가 아니다.
score_contribution은 반드시 accepted_claim_id를 support로 가져야 한다.
EVENT_WEIGHTED_PARTIAL도 예외가 아니며, 공식 이벤트 제목/메타데이터만으로 nonzero score를 만들면 critical fail이다.
```

쉬운 예:

```text
DART에서 "단일판매공급계약" 공시를 발견했다.
  -> 이건 후보를 열어 주는 CandidateEvent다.

점수에 들어가려면 공시 원문에서 금액, 기간, 상대방, 대상회사 직접성, 현재성이
accepted_claim으로 닫혀야 한다.
  -> 공시 제목만 보고 contract_quality +4점을 주면 안 된다.
```

2026-07-03 최신 교차검증 기준:

```text
latest v101 official partial promotion lane patch / replay / Stage truth =
  docs/0701/census_v4_0701_v101_official_partial_promotion_lane_patch_replay_and_stage_truth_2026-07-03.md

latest v100 bounded ramp Stage existence / promotion blocker forensic =
  docs/0701/census_v4_0701_v100_bounded_ramp_stage_existence_promotion_blocker_forensic_and_patch_direction_2026-07-03.md

latest v99 real LLM claim extractor smoke result =
  docs/0701/census_v4_0701_v99_real_llm_claim_extractor_smoke_result_2026-07-03.md

latest v98 seed materialization operator-use trace patch =
  docs/0701/census_v4_0701_v98_seed_materialization_operator_use_trace_patch_2026-07-03.md

latest v97 external seed real Brain smoke cross validation / next patch direction =
  docs/0701/census_v4_0701_v97_external_seed_real_brain_smoke_cross_validation_and_next_patch_direction_2026-07-03.md

latest v96 external follow-up seed to Census Brain patch =
  docs/0701/census_v4_0701_v96_external_follow_up_seed_to_census_brain_patch_2026-07-03.md

latest v95 seed materialization scope split patch =
  docs/0701/census_v4_0701_v95_seed_materialization_scope_split_patch_2026-07-03.md

latest v94 Stage existence truth / seed execution gap cross validation =
  docs/0701/census_v4_0701_v94_stage_existence_truth_and_seed_execution_gap_2026-07-03.md

latest v93 follow-up seed CLI entrypoint patch / cross validation =
  docs/0701/census_v4_0701_v93_follow_up_seed_cli_entrypoint_patch_2026-07-03.md

latest v92 FULL_THESIS blocker follow-up seed event patch / cross validation =
  docs/0701/census_v4_0701_v92_full_thesis_blocker_follow_up_seed_event_patch_2026-07-03.md

latest v91 FULL_THESIS blocker follow-up source task patch / cross validation =
  docs/0701/census_v4_0701_v91_full_thesis_blocker_follow_up_source_tasks_cross_validation_2026-07-03.md

latest v90 operational Stage truth cross validation / next patch direction =
  docs/0701/census_v4_0701_v90_operational_stage_truth_cross_validation_and_next_patch_direction_2026-07-03.md

latest v89 source acquisition capability split patch =
  docs/0701/census_v4_0701_v89_source_acquisition_capability_split_patch_2026-07-03.md

latest v88 source connector capability gate patch =
  docs/0701/census_v4_0701_v88_source_connector_capability_gate_patch_2026-07-03.md

latest v87 Stage exists but no operational Stage cross-review / patch direction =
  docs/0701/census_v4_0701_v87_stage_exists_but_no_operational_stage_cross_review_and_patch_direction_2026-07-03.md

latest live Brain/Web v82 verified report original route-whitelist hardening / stage truth =
  docs/0701/census_v4_0701_v82_verified_report_original_route_whitelist_stage_truth_cross_validation_2026-07-03.md

latest v82 operational stage existence deep audit / next patch direction =
  docs/0701/census_v4_0701_v82_operational_stage_existence_deep_audit_and_next_patch_direction_2026-07-03.md

latest v83 FULL_THESIS source-linkage / score-interval guard patch =
  docs/0701/census_v4_0701_v83_full_thesis_source_linkage_and_score_interval_guard_patch_2026-07-03.md

latest v84 operational Stage zero root-cause / cross-review / patch direction =
  docs/0701/census_v4_0701_v84_operational_stage_zero_root_cause_cross_review_and_patch_direction_2026-07-03.md

latest v85 FULL_THESIS smoke honesty/execution split patch =
  docs/0701/census_v4_0701_v85_full_thesis_smoke_honesty_execution_split_patch_2026-07-03.md

latest v86 full-field smoke honesty guard patch =
  docs/0701/census_v4_0701_v86_full_field_smoke_honesty_guard_patch_2026-07-03.md

latest v82 bounded live smoke =
  output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v82

latest v97 external seed real Brain smoke =
  output/census_v4/2026-07-01-v97-external-seed-real-brain-smoke

latest v99 real LLM claim extractor smoke =
  output/census_v4/2026-07-01-v99-external-seed-real-extractor-smoke

latest v100 real extractor bounded ramp =
  output/census_v4/2026-07-01-v100-external-seed-real-extractor-bounded-ramp

latest v101 policy replay from v100 =
  output/census_v4/2026-07-01-v101-promotion-policy-replay-from-v100

artifact_truth_version = v100_real_extractor_bounded_ramp
latest_policy_replay_version = v101
latest_code_guard_patch_version = v101
latest_cross_validation_doc_version = v101
v83_live_rerun_required = true
v85_live_rerun_required = true
v86_live_rerun_required = true
v89_live_rerun_required = true
v91_live_rerun_required = true
v92_live_rerun_required = true
v93_live_rerun_required = true
v94_live_closure_required = true
v95_live_closure_required = true
v96_live_closure_required = true
v97_live_closure_required = true
v98_live_closure_required = true
v99_live_closure_required = true
v100_live_closure_required = true
v101_live_rerun_required = true

v101 policy replay truth:
  source = v100 artifacts replayed with v101 promotion policy
  verdict = PARTIAL_STAGE_VISIBILITY_FIXED_BY_REPLAY
  operational_readiness = NOT_READY
  promoted_stage_row_count = 21
  promoted_web_llm_stage_row_count = 2
  promoted_official_stage_row_count = 19
  skipped_unsupported_trace_count = 0
  brain_stage_promotion_audit.verdict = PROMOTION_APPLIED
  brain_stage_trace_count = 21
  brain_promoted_stage_row_count = 21
  brain_stage_trace_with_web_or_llm_claim_count = 2
  brain_stage_trace_with_official_claim_count = 20
  brain_stage_trace_without_supported_claim_count = 0
  unsafe_promoted_stage_row_count = 0
  replayed stage_scope =
    CENSUS_EVENT_BOARD = 3370
    BRAIN_OFFICIAL_PARTIAL = 19
    BRAIN_WEB_PARTIAL = 2
  replayed score_scale =
    NO_SCORE = 3320
    EVENT_WEIGHTED_PARTIAL = 71
  replayed operator_stage_use =
    NOT_FULL_THESIS_STAGE = 3391
  replayed operator_score_use =
    NOT_FULL_E2R_SCORE = 3391
  replayed full_thesis_stage =
    FULL_THESIS_NOT_RUN = 3391
  full thesis attempt after replay =
    candidate_row_count = 21
    promoted_full_thesis_row_count = 0
    blocked_candidate_count = 21
    blocked_candidate_follow_up_source_task_count = 53
    production_pass_allowed = false
  operator truth =
    Stage rows exist at partial level.
    FULL_THESIS operational Stage rows still do not exist.
    Samsung 005930 = BRAIN_OFFICIAL_PARTIAL canonical_stage 0, not FULL_THESIS.
    SK Hynix 000660 = BRAIN_WEB_PARTIAL canonical_stage 0, not FULL_THESIS.
  caveat =
    v101 replay folder's base brain_web_readiness_gate_audit.json is copied from v100 and still says BLOCKED.
    Use *_after_v101_policy_replay artifacts for v101 replay truth.
    A full live bounded rerun with v101 code is still required.
  verification =
    targeted brain promotion 17 tests OK
    related gates 34 tests OK
    census_v4 141 tests OK
    full unittest 5126 tests OK

v100 truth:
  verdict = NOT_READY
  census_stage_status rows = 3391
  canonical_stage = 0:3306, 1:54, 2:30, 3-Red:1
  stage_scope = CENSUS_EVENT_BOARD 3391, BRAIN_WEB_PARTIAL 0, FULL_THESIS 0
  score_scale = NO_SCORE 3324, EVENT_WEIGHTED_PARTIAL 67, FULL_E2R_100 0
  operator_stage_use = NOT_FULL_THESIS_STAGE 3391
  operator_score_use = NOT_FULL_E2R_SCORE 3391
  real LLM claim extractor path is proven at ramp size:
    claim_extractor_runs = 31
    provider_mode = llm
    provider_name includes codex_cli_contract_blind_extractor
    provider_error = 0
  Brain/Web operational minimum counts are now met:
    planner real provider success = 30
    source_task_execution_count = 228
    web_search_tasks = 37
    web_search_calls = 37
    web_fetched_documents = 31
    Brain accepted claims = 93
    Brain score contributions = 53
    Brain StageCourt traces = 21
  remaining blockers =
    Brain/Web trace rows missing stagecourt_trace_id: 3
    Brain/Web StageCourt traces are not promoted into census_stage_status
    brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
  root cause =
    Brain StageCourt trace 21개 중 19개가 OpenDART official-only이고,
    현재 promotion audit은 official-only trace를 BRAIN_WEB_PARTIAL로 올리지 않는 것을
    run-global blocker로 잡는다.
    그래서 LLM/web claim이 포함된 2개 trace까지 함께 0개 승격된다.
  operator truth =
    v100 proves real LLM extraction and live bounded acquisition are working.
    It does not create BRAIN_WEB_PARTIAL or FULL_THESIS rows in census_stage_status.
    Samsung 005930 is still CENSUS_EVENT_BOARD partial event state, not FULL_THESIS.
    SK Hynix 000660 has C06 LLM claims but remains not promoted and not FULL_THESIS.
  next patch direction =
    official-only direct/current claim-backed StageCourt는 BRAIN_OFFICIAL_PARTIAL 또는
    BRAIN_CLAIM_PARTIAL로 per-trace partial promotion해야 한다.
    web/LLM claim-backed trace는 BRAIN_WEB_PARTIAL로 per-trace promotion해야 한다.
    둘 다 operator-use는 NOT_FULL_THESIS_STAGE/NOT_FULL_E2R_SCORE로 유지한다.
    FULL_THESIS/Green은 source linkage, score interval, source quorum, Green primitive coverage가
    모두 닫힐 때만 허용한다.

v99 truth:
  verdict = NOT_READY
  real LLM claim extractor path is now proven in live smoke:
    claim_extractor_runs = 1
    provider_mode = llm
    provider_name = codex_cli_contract_blind_extractor
    status = SUCCESS
    provider_error = null
  removed v97 blocker:
    LLM claim extractor has no real LLM provider runs
  remaining blockers =
    Brain/Web operational minimum planner runs not met: 21/30
    Brain/Web operational minimum web search tasks not met: 3/20
    Brain/Web operational minimum web/news search calls not met: 3/20
    Brain/Web operational minimum fetched documents not met: 1/10
    Brain/Web operational minimum claim extractor attempts not met: 1/10
  Brain/Web current attempt counts:
    planner_runs = 21, but real provider success = 1
    web_search_tasks = 3
    web_search_results = 30
    web_fetched_documents = 1
    claim_extractor_runs = 1, provider_mode = llm
    accepted Brain/Web claims = 19
    Brain/Web score contributions = 6
    Brain/Web stagecourt traces = 1
  seed materialization:
    PLANNER_NOT_RUN = 64
    PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 20
    STAGECOURT_READY_NOT_PROMOTED = 1
    FULL_THESIS_PROMOTED = 0
  operator truth =
    v99 proves real LLM extraction can run.
    It does not create FULL_THESIS rows.
    SK Hynix is still BRAIN_WEB_PARTIAL, not FULL_THESIS.
    Samsung was not real-planner-success materialized in this small smoke.

v98 patch truth:
  scope = code guard / audit trace hardening, not live closure
  changed files =
    src/e2r/census/census_runner_v4.py
    tests/test_census_v4_full_thesis_smoke_tasks.py
  full_thesis_seed_materialization_trace now exposes:
    final_operator_score_use
    final_full_thesis_score_scale
    final_is_full_thesis_stage
    final_is_full_e2r_score
  full_thesis_seed_materialization_audit now exposes:
    final_operator_stage_use_counts
    final_operator_score_use_counts
  new critical guards include:
    final_operator_stage_use_missing_count
    final_operator_score_use_missing_count
    event_or_partial_stage_operator_use_allowed_count
    event_or_partial_score_operator_use_allowed_count
    full_thesis_promoted_operator_stage_use_not_full_count
    full_thesis_promoted_operator_score_use_not_full_count
  verification =
    targeted 30 tests OK
    census v4 140 tests OK
    full unittest 5125 tests OK
  operator truth =
    v98 makes partial/event-board overclaim harder.
    It does not create FULL_THESIS rows.
    v97 live truth remains NOT_READY until real LLM extractor and full thesis materialization close.

v97 truth:
  verdict = NOT_READY
  external seed was consumed by Census Brain:
    full_thesis_seed_source = external_candidate_event_seed_path
    research_brain_candidate_seed_events_used.jsonl rows = 85
  stage map rows = 3391
  canonical_stage = 0:3307, 1:53, 2:30, 3-Red:1
  stage_scope = CENSUS_EVENT_BOARD 3390, BRAIN_WEB_PARTIAL 1, FULL_THESIS 0
  score_scale = NO_SCORE 3324, EVENT_WEIGHTED_PARTIAL 67, FULL_E2R_100 0
  operator_stage_use = NOT_FULL_THESIS_STAGE 3391
  operator_score_use = NOT_FULL_E2R_SCORE 3391
  full_thesis_stage = FULL_THESIS_NOT_RUN 3391
  seed materialization trace = 85 rows
    PLANNER_NOT_RUN = 64
    PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 20
    STAGECOURT_READY_NOT_PROMOTED = 1
  Brain/Web current attempt counts:
    planner_runs = 21, but real provider success = 1
    web_search_tasks = 3
    web_fetched_documents = 1
    claim_extractor_runs = 1, provider_mode = rule_fallback
    accepted Brain/Web claims = 1
    Brain/Web stagecourt traces = 1
  remaining blockers =
    LLM claim extractor has no real LLM provider runs
    Brain/Web operational minimum planner runs not met: 21/30
    Brain/Web operational minimum web search tasks not met: 3/20
    Brain/Web operational minimum web/news search calls not met: 3/20
    Brain/Web operational minimum fetched documents not met: 1/10
    Brain/Web operational minimum claim extractor attempts not met: 1/10
    Brain/Web operational minimum web/LLM accepted claims not met: 1/3
  operator truth =
    external seed wiring works, but FULL_THESIS materialization is still pending.
    Samsung 005930 is CENSUS_EVENT_BOARD Stage1, not FULL_THESIS.
    SK Hynix 000660 is BRAIN_WEB_PARTIAL, not FULL_THESIS.
    Dragonfly 030350 3-Red is event-board risk review, not operator Red.

v82 truth:
  verdict = NOT_READY
  leaf_artifact_audit = PASS
  primitive_state_chain_audit = PASS
  source_task_satisfaction_audit = PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
  runtime_plausibility_audit = PASS_LIVE_RUNTIME_PLAUSIBILITY
  brain_stage_promotion_audit = PROMOTION_APPLIED
  brain_web_readiness_gate_audit = BLOCKED
  stage_scope = CENSUS_EVENT_BOARD 3390, BRAIN_WEB_PARTIAL 1, FULL_THESIS 0
  operator_stage_use = NOT_FULL_THESIS_STAGE 3391
  operator_score_use = NOT_FULL_E2R_SCORE 3391
  FULL_E2R_100 verified score row = 0
  SK하이닉스 BRAIN_WEB_PARTIAL event_evidence_score = 60.0, not FULL_E2R_100
  삼성전자/하이닉스 full thesis smoke = PENDING_FULL_THESIS_REFRESH
  all-archetype source-backed replay = 6/32 ready, 26 required archetypes missing
  remaining blockers =
    Brain/Web operational minimum planner runs not met: 21/30
    Brain/Web operational minimum web search tasks not met: 3/20
    Brain/Web operational minimum web/news search calls not met: 3/20
    Brain/Web operational minimum fetched documents not met: 1/10
    Brain/Web operational minimum claim extractor attempts not met: 1/10
    full_thesis_production_pass_false
    source_backed_replay_parity_all_archetypes_pending

v83 patch note:
  FULL_THESIS 승급 전 accepted_claim_id -> document_id/anchor_id -> source_task_execution.fetched_document_ids
  직접 연결을 요구한다.
  score_interval도 lower와 upper가 모두 닫히지 않으면 승급 차단한다.
  이 패치는 거짓 승급 방지 패치이며, FULL_THESIS row 0개라는 v82 운영 truth를 READY로 바꾸지 않는다.

v91 patch note:
  FULL_THESIS 후보가 missing Green primitive로 막힐 때
  `full_thesis_blocker_follow_up_source_tasks.jsonl`을 생성한다.
  이 task는 점수 재료가 아니라 다음 Research Brain LLM planner 입력이다.
  hardcoded query는 0개이고, bounded official-first source classes와 max_queries/max_candidates/max_fetches만 가진다.
  source_connector_capability_audit도 이 새 task 파일을 full-thesis requirement로 읽는다.
  이 패치는 SK하이닉스 같은 BRAIN_WEB_PARTIAL 후보를 FULL_THESIS로 승격하지 않는다.

v92 patch note:
  v91 task shell을 다음 Research Brain 실행에서 읽을 수 있는
  `full_thesis_blocker_follow_up_seed_events.jsonl`로 변환한다.
  seed는 `planner_input_only`이며 `score_evidence_allowed=false`,
  `stage_promotion_allowed_before_execution=false`다.
  Brain planner가 보는 structured_payload에는 score/stage/current_score_eligible 키를 넣지 않는다.
  이 패치도 FULL_THESIS row를 만들지 않는다. live source fetch와 accepted_claim closure는 다음 검증 대상이다.

v93 patch note:
  Research Brain v4 CLI에 `--candidate-event-seed-path`를 추가했다.
  이제 v92의 `full_thesis_blocker_follow_up_seed_events.jsonl`을
  `ProductionShadowV4Config.candidate_event_seed_path`로 넘길 수 있다.
  이 패치도 score/Stage를 만들지 않는다. seed를 실제 live planner/source/claim closure로 소비하는 실행 검증이 남아 있다.

v94 cross-validation note:
  `census_stage_map.csv`를 직접 다시 세어 Stage row 3,391개, canonical_stage nonzero 85개,
  stage_scope FULL_THESIS 0개, score_scale FULL_E2R_100 0개를 재확인했다.
  즉 Stage처럼 보이는 행은 있지만 운영 FULL_THESIS Stage는 아직 0개다.
  다음 패치는 seed -> planner -> source -> accepted_claim -> score_contribution -> StageCourt
  실제 live closure를 증명해야 한다.

v95 patch note:
  `full_thesis_seed_materialization_audit.verdict=PASS`의 의미를 장부 무결성 PASS로 분리했다.
  새 필드:
    verdict_scope
    ledger_integrity_pass_allowed
    actual_materialization_pass_allowed
    operator_materialization_status
  `actual_materialization_pass_allowed=false`이면 운영 FULL_THESIS seed closure가 아니다.
  현재 기본 상태는 `LEDGER_INTEGRITY_ONLY` / `PENDING_FULL_THESIS_MATERIALIZATION`로 남아야 한다.

v96 patch note:
  Census v4 CLI/config에 `--brain-candidate-event-seed-path`를 추가했다.
  이전 run의 `full_thesis_blocker_follow_up_seed_events.jsonl`을 다음 Census Brain run에 직접 넣을 수 있다.
  실제 Brain에 투입된 seed는 항상 `research_brain_candidate_seed_events_used.jsonl`로 복사된다.
  audit에는 `full_thesis_seed_source`, `full_thesis_seed_original_path`가 남는다.
  이 패치도 FULL_THESIS row를 만들지는 않는다. live planner/source/claim closure 검증은 계속 남아 있다.

Stage 존재 질문의 최신 답:
  Stage row 자체는 3,391개 있다.
  Stage0이 아닌 표시도 85개 있다.
  하지만 운영 FULL_THESIS/FULL_E2R Stage는 0개다.
  모든 row가 operator_stage_use=NOT_FULL_THESIS_STAGE,
  operator_score_use=NOT_FULL_E2R_SCORE다.

FULL_THESIS_SMOKE_PASS라는 표현은 앞으로 둘로 나눠야 한다.
  FULL_THESIS_SMOKE_HONESTY_PASS =
    pending/미실행을 거짓 Stage로 말하지 않음
  FULL_THESIS_SMOKE_EXECUTION_PASS =
    source task -> accepted claim -> score contribution -> StageCourt -> FULL_THESIS row 실제 성공
  현재 v82/v83 상태는 honesty guard 쪽은 강화됐지만 execution pass는 아니다.
  goal_completion_ready는 execution pass 없이 true가 되면 안 된다.

v85 patch note:
  census_runner_v4.py와 관련 tests에서 smoke 판정을 실제로 분리했다.
  readiness_verdict:
    full_thesis_smoke_honesty_pass
    full_thesis_smoke_execution_pass
  goal_completion_audit:
    full_thesis_smoke_honesty_pass_allowed
    full_thesis_smoke_execution_pass_allowed
    full_thesis_smoke_summary
  goal_requirement_matrix:
    FULL_THESIS_SMOKE_HONESTY_PASS gate 추가
    기존 FULL_THESIS_SMOKE_PASS는 execution pass 의미로 고정
  검증:
    targeted smoke/goal audit tests = 15 tests OK
    census v4 test_census_v4_* = 139 tests OK
    full unittest discover = 5122 tests OK

v86 patch note:
  v85의 남은 취약점이던 summary-only / legacy-minimal smoke honesty pass를 제거했다.
  이제 `full_thesis_smoke_honesty_pass_allowed=True` 요약값만으로는 pass가 아니다.
  필수 원 필드가 모두 있어야 한다.
    score_allowed_before_execution == False
    hardcoded_query_count == 0
    daily_event_and_full_thesis_separated == True
  execution pass도 `full_thesis_smoke_execution_pass_allowed=True` 요약값만 믿지 않고,
  full_thesis_status와 per_symbol smoke_pass_allowed를 다시 확인한다.
  검증:
    targeted smoke/goal audit tests = 15 tests OK
    census v4 test_census_v4_* = 139 tests OK
    full unittest discover = 5122 tests OK

v88 patch note:
  FULL_THESIS가 요구하는 source class를 production connector registry가 감당 가능한지
  `source_connector_capability_audit.json`으로 장부화했다.
  이 audit는 네트워크를 부르지 않는 정적 capability gate다.
  현재 검증 artifact:
    output/test_census_v4_cached/source_connector_capability_audit.json
  write_operational_docs=True 실행 시 export 경로:
    docs/operational/census_mode_v4_source_connector_capability_audit.json
  현재 판정:
    verdict = PENDING_SOURCE_CONNECTOR_CAPABILITY
    source_connector_capability_pass_allowed = False
    registered live connector = DART, KIND, KRX, CompanyGuide
    placeholder connector = IssuerIR, TrustedNews
    missing connector = BrokerReportPublicPDF, CompanyNewsroom, GeneralWebSearch, IssuerOfficial, NaverSearch, ReportPDF
    blocking_full_thesis_source_class_count = 7
    blocking_full_thesis_task_count = 97
  goal gate:
    SOURCE_CONNECTOR_CAPABILITY_PASS 추가
    source_connector_capability_pending blocker 추가
  쉬운 예:
    FULL_THESIS가 리포트 PDF와 회사 newsroom 증거를 요구하는데,
    현재 운영 registry에 그 우편함이 없으면 "서류가 아직 안 왔다"가 아니라
    "서류를 받을 통로부터 없다"로 막아야 한다.
  검증:
    targeted goal/source tests = 17 tests OK
    census v4 test_census_v4_* = 139 tests OK
    full unittest discover = 5122 tests OK

v89 patch note:
  v88의 source connector capability audit를 registry-only에서
  registry + bounded SourceAcquisitionRunnerV4 capability split으로 정교화했다.
  현재 검증 artifact:
    output/test_census_v4_cached/source_connector_capability_audit.json
  현재 판정:
    verdict = PENDING_SOURCE_CONNECTOR_CAPABILITY
    source_connector_capability_pass_allowed = False
    blocking_full_thesis_source_class_count = 2
    blocking_full_thesis_source_classes = IssuerIR, TrustedNews
    blocking_full_thesis_task_count = 0
    full_thesis_task_executable_source_path_pass_allowed = True
    full_thesis_task_with_blocking_source_class_count = 83
    acquisition_capability_count = 5
    bounded_web_acquisition_source_classes =
      BrokerReportPublicPDF, CompanyNewsroom, GeneralWebSearch, NaverSearch, ReportPDF
    registry_missing_but_acquisition_covered_source_classes =
      BrokerReportPublicPDF, CompanyNewsroom, GeneralWebSearch, NaverSearch, ReportPDF
    missing_connector_source_classes = IssuerOfficial
  쉬운 예:
    네이버/회사 뉴스룸/리포트 PDF는 "받을 통로 자체가 없음"이 아니라,
    bounded search/fetch/lineage 검증 통로는 있다.
    하지만 실제 문서 fetch와 accepted claim이 없으면 여전히 점수 0이고 FULL_THESIS pass가 아니다.
    FTSMOKE controlled smoke task는 production source capability blocker 계산에서 제외한다.
  검증:
    tests.test_census_v4_goal_required_audits = 4 tests OK
    census v4 test_census_v4_* = 139 tests OK
    full unittest discover = 5122 tests OK

v90 cross-validation note:
  현재 질문 "Stage가 있는 애들이 있긴 해?"에 대한 최신 답을 별도 문서로 고정했다.
  직접 재계산 기준:
    census_stage_map.csv rows = 3391
    canonical_stage != 0 rows = 85
    stage_scope = CENSUS_EVENT_BOARD 3390
    stage_scope = BRAIN_WEB_PARTIAL 1
    stage_scope = FULL_THESIS 0
    score_scale = NO_SCORE 3324, EVENT_WEIGHTED_PARTIAL 67, FULL_E2R_100 0
    operator_stage_use = NOT_FULL_THESIS_STAGE 3391
    operator_score_use = NOT_FULL_E2R_SCORE 3391
  삼성전자:
    canonical_stage = 1
    stage_scope = CENSUS_EVENT_BOARD
    event_evidence_score = 4.0
    score_scale = EVENT_WEIGHTED_PARTIAL
    full_thesis_stage = FULL_THESIS_NOT_RUN
  SK하이닉스:
    canonical_stage = 1
    stage_scope = BRAIN_WEB_PARTIAL
    event_evidence_score = 60.0
    score_scale = EVENT_WEIGHTED_PARTIAL
    full_thesis_stage = FULL_THESIS_NOT_RUN
  결론:
    Stage row는 있다.
    하지만 운영 FULL_THESIS Stage와 FULL_E2R_100 verified score는 0개다.
  다음 패치 방향:
    full_thesis_refresh_queue 84개를 실제 bounded SourceTaskExecution,
    EvidenceDocument, EvidenceAnchor, accepted claim, ScoreContribution,
    StageCourt, promoted FULL_THESIS row까지 닫아야 한다.
    IssuerIR/TrustedNews placeholder와 all-archetype source-backed replay 6/32도 남은 blocker다.
  검증:
    py_compile census_runner_v4.py = OK
    tests.test_census_v4_goal_required_audits = 4 tests OK
    census v4 test_census_v4_* = 139 tests OK
    full unittest discover = 5122 tests OK

Production/backfill 수집 폭도 반드시 분리한다.
  Backfill =
    연구자료 URL 복구/source repair용. 넓은 검색 가능. 운영 점수로 직행 금지.
  Production daily =
    모든 SourceTask는 budget과 stop_condition 필요.
    top_results=None, retry_max=None, 무제한 page fetch 금지.
    provider/source gap은 낮은 점수 확정이 아니라 pending.

Source acquisition root cause:
  IssuerIRLiveConnector = 아직 placeholder
  TrustedNewsLiveConnector = 아직 placeholder
  ReportPDF = verified original route에서만 부분 작동
  CompanyNewsroom = as-of safe issuer official domain authority 필요
  configs/e2r_issuer_official_domains_v1.json의 2026-07-03 SK하이닉스 entry는
    2026-07-01 replay에 쓰면 미래누수라서 사용 금지가 맞다.

다음 패치의 방향은 Green gate 완화나 삼성전자/하이닉스 예외가 아니다.
실제 official/newsroom/report source capability를 as-of 안전하게 열고,
LLM query provenance와 source lineage를 닫는 것이다.

아래에 남아 있는 v80/v81/v77 등 과거 블록은 historical record다.
최신 판단에는 이 v82 truth block과 v82 상세 문서를 우선한다.

latest Brain/Web enabled diagnostic =
  output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v28

latest queue / timeout ledger-refresh verification =
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30

latest review packet =
  docs/0701/census_v4_0701_sourcequality_v28_bounded_retry_loop_patch_result_and_source_quality_gap_2026-07-02.md

latest stage-existence truth packet =
  docs/0701/census_v4_0701_v28_stage_existence_truth_cross_review_and_full_thesis_queue_direction_2026-07-02.md

latest full-thesis refresh queue patch =
  docs/0701/census_v4_0701_v29_full_thesis_refresh_queue_patch_result_and_provider_stall_note_2026-07-02.md

latest provider timeout guard / queue cross-validation patch =
  docs/0701/census_v4_0701_v30_provider_timeout_guard_and_full_thesis_queue_cross_validation_2026-07-02.md

latest invalid partial output CLI guard =
  docs/0701/census_v4_0701_v31_invalid_partial_output_cli_guard_2026-07-02.md

latest source route quality / blog-social reject guard =
  docs/0701/census_v4_0701_v32_source_route_quality_blog_social_reject_guard_2026-07-02.md

latest low-quality source feedback prompt guard =
  docs/0701/census_v4_0701_v33_low_quality_source_feedback_prompt_guard_2026-07-02.md

latest source lineage/original guard and README correction =
  docs/0701/census_v4_0701_v34_stage_truth_cross_validation_source_lineage_patch_2026-07-02.md

latest source lineage feedback retry guard =
  docs/0701/census_v4_0701_v35_source_lineage_feedback_retry_guard_2026-07-02.md

latest source lineage retry execution guard =
  docs/0701/census_v4_0701_v36_source_lineage_retry_execution_guard_2026-07-02.md

latest source lineage retry drop leaf audit patch =
  docs/0701/census_v4_0701_v37_source_lineage_retry_drop_leaf_audit_patch_2026-07-02.md

latest retry drop readiness audit patch =
  docs/0701/census_v4_0701_v38_retry_drop_readiness_audit_patch_2026-07-02.md

latest source lineage good retry acceptance chain =
  docs/0701/census_v4_0701_v39_source_lineage_good_retry_acceptance_chain_2026-07-02.md

latest source lineage retry outcome readiness counts =
  docs/0701/census_v4_0701_v40_source_lineage_retry_outcome_readiness_counts_2026-07-02.md

latest stage truth hard review =
  docs/0701/census_v4_0701_v41_stage_truth_hard_review_2026-07-02.md

latest full thesis queue materialization audit =
  docs/0701/census_v4_0701_v42_full_thesis_queue_materialization_audit_2026-07-02.md

latest full thesis queue seed -> Research Brain input patch =
  docs/0701/census_v4_0701_v43_full_thesis_queue_seed_to_research_brain_input_2026-07-02.md

latest full thesis seed materialization runtime counts =
  docs/0701/census_v4_0701_v44_full_thesis_seed_materialization_runtime_counts_2026-07-03.md

latest stage-existence / seed-materialization hard cross-audit =
  docs/0701/census_v4_0701_v45_stage_existence_seed_materialization_cross_audit_2026-07-03.md

latest full thesis seed materialization trace leaf =
  docs/0701/census_v4_0701_v46_full_thesis_seed_materialization_trace_leaf_2026-07-03.md

latest stage-existence answer / next patch direction =
  docs/0701/census_v4_0701_v47_stage_existence_answer_and_next_patch_direction_2026-07-03.md

latest full thesis seed materialization audit leaf =
  docs/0701/census_v4_0701_v48_full_thesis_seed_materialization_audit_leaf_2026-07-03.md

latest seed materialization audit readiness / goal gate link =
  docs/0701/census_v4_0701_v49_seed_materialization_audit_readiness_goal_gate_link_2026-07-03.md

latest seed promotion gate split / cross-validation =
  docs/0701/census_v4_0701_v50_seed_promotion_gate_split_cross_validation_and_next_patch_direction_2026-07-03.md

latest seed planner event/run count split and stage truth =
  docs/0701/census_v4_0701_v51_seed_planner_event_vs_run_count_audit_and_stage_truth_2026-07-03.md

latest machine-readable test artifact gate clear =
  docs/0701/census_v4_0701_v52_machine_readable_test_artifact_gate_clear_and_remaining_goal_blockers_2026-07-03.md

latest controlled smoke operator use guard =
  docs/0701/census_v4_0701_v53_controlled_smoke_operator_use_guard_2026-07-03.md

latest full-thesis seed context / stage truth cross-validation =
  docs/0701/census_v4_0701_v56_full_thesis_seed_context_and_stage_truth_cross_validation_2026-07-03.md

latest real planner source-order patch / full-thesis blocker audit =
  docs/0701/census_v4_0701_v59_real_planner_source_order_patch_and_full_thesis_blocker_audit_2026-07-03.md

latest CompanyGuide consensus claim compiler / stage truth cross-audit =
  docs/0701/census_v4_0701_v60_companyguide_consensus_claim_compiler_cross_audit_and_next_patch_packet_2026-07-03.md

latest CompanyGuide claim dedupe / stage truth / next patch packet =
  docs/0701/census_v4_0701_v61_companyguide_claim_dedupe_stage_truth_and_next_patch_packet_2026-07-03.md

latest rerouted feedback source filter / stage truth / next patch packet =
  docs/0701/census_v4_0701_v64_rerouted_feedback_source_filter_stage_truth_and_next_patch_packet_2026-07-03.md

latest planner candidate context sanitizer / stage truth / next patch packet =
  docs/0701/census_v4_0701_v67_planner_candidate_context_sanitizer_stage_truth_and_next_patch_packet_2026-07-03.md

latest live Brain/Web v69 stage truth / alias patch / next router bottleneck =
  docs/0701/census_v4_0701_v69_live_brain_web_stage_truth_alias_patch_and_next_router_bottleneck_2026-07-03.md

latest live Brain/Web v70 source router alias patch / stage truth / next agent attack packet =
  docs/0701/census_v4_0701_v70_source_router_alias_patch_live_smoke_stage_truth_and_next_agent_attack_packet_2026-07-03.md

latest live Brain/Web v71 verified issuer original source-lineage patch / stage truth / next agent attack packet =
  docs/0701/census_v4_0701_v71_verified_issuer_original_source_lineage_patch_stage_truth_and_next_agent_attack_packet_2026-07-03.md

latest live Brain/Web v73 contract visibility policy alignment / verified issuer domain hardening / stage truth =
  docs/0701/census_v4_0701_v73_contract_visibility_policy_alignment_verified_issuer_domain_hardening_and_stage_truth_2026-07-03.md

latest live Brain/Web v74 issuer official domain registry / stage truth cross-validation / next patch packet =
  docs/0701/census_v4_0701_v74_issuer_official_domain_registry_stage_truth_cross_validation_and_next_patch_packet_2026-07-03.md

latest live Brain/Web v77 verified report original / representative score claim / stage truth / next patch packet =
  docs/0701/census_v4_0701_v77_verified_report_original_representative_score_claim_stage_truth_and_next_patch_packet_2026-07-03.md

latest v77 bounded live smoke =
  output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v77

v77 truth:
  verdict = NOT_READY
  leaf_artifact_audit = PASS
  primitive_state_chain_audit = PASS
  source_task_satisfaction_audit = PASS
  brain_stage_promotion_audit = PROMOTION_APPLIED
  brain_web_readiness_gate_audit = BLOCKED
  stage_scope = CENSUS_EVENT_BOARD 3390, BRAIN_WEB_PARTIAL 1, FULL_THESIS 0
  operator_stage_use = NOT_FULL_THESIS_STAGE 3391
  FULL_E2R_100 verified score row = 0
  SK하이닉스 BRAIN_WEB_PARTIAL event_evidence_score = 75.8333, not FULL_E2R_100
  삼성전자 CENSUS_EVENT_BOARD event_evidence_score = 4.0, not FULL_E2R_100
  remaining blockers =
    Brain/Web operational minimum planner runs not met: 22/30
    Brain/Web operational minimum web search tasks not met: 7/20
    Brain/Web operational minimum web/news search calls not met: 7/20
    Brain/Web operational minimum fetched documents not met: 2/10
    Brain/Web operational minimum claim extractor attempts not met: 2/10

latest deep cross-audit / next patch packet =
  docs/0701/census_v4_0701_v26_deep_cross_audit_stage_truth_and_next_patch_direction_2026-07-02.md

verdict = NOT_READY
leaf_artifact_audit = PASS
leaf critical_count = 0
runtime_plausibility = PASS_LIVE_RUNTIME_PLAUSIBILITY

stage_scope = CENSUS_EVENT_BOARD 3391
operator_stage_use = NOT_FULL_THESIS_STAGE 3391
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
verified_score_present_count = 0

v74 live smoke:
  web_search_task_count = 6
  web_search_call_count = 6
  web_fetched_document_count = 2
  llm_claim_extractor_attempt_count = 2
  web_or_llm_accepted_claim_count = 0
  brain_promoted_stage_row_count = 0

Real planner source-order patch, v59:
  v58에서 official_first rejected mapping feedback retry는 열렸지만,
  retry source task도 registry connector 순서 때문에 DART 유상증자 문서로 반복되는 문제가 있었다.
  v59는 live official connector 실행 순서를 registry 순서가 아니라 SourceTask preferred/fallback 순서로 고정했다.
  또한 LLM이 내는 IssuerIR source class를 실제 IR connector와 매칭한다.
  targeted tests:
    tests.test_research_brain_v4_real_source_acquisition: Ran 29 tests OK
    tests.test_research_brain_v4_operational_modes: Ran 51 tests OK
  full suite:
    PYTHONPATH=src python -m unittest discover -s tests -v
    Ran 5081 tests in 207.192s
    OK
  diff check:
    git diff --check
    OK
  real planner smoke:
    output/census_v4/2026-07-01-real-planner-source-order-v59
    exit code = 1 / NOT_READY
    planner_runs = 22
    real_provider_success_count = 2
    Full Thesis seed 000660 source_task_execution_count = 9
    Full Thesis seed accepted_claim_count = 0
    retry cash_or_revision_conversion task now fetched CompanyGuide, not DART
  current blocker:
    CompanyGuide fetch is provider coverage-only:
      provider_coverage_only_until_numeric_revision_parser_accepts_claims
    Therefore CompanyGuide/IR numeric revision and issuer-source claim compiler is still missing.
  current truth remains:
    CENSUS_EVENT_BOARD state rows exist
    FULL_THESIS rows = 0
    FULL_E2R_100 rows = 0

CompanyGuide consensus claim compiler, v60:
  v59에서 CompanyGuide가 SourceTask 순서대로 fetch되기 시작했지만,
  문서가 provider coverage-only로 막혀 숫자 claim이 만들어지지 않았다.
  v60은 CompanyGuide "투자의견 컨센서스" 표에서
  CONSENSUS_AS_OF_DATE, TARGET_PRC, EPS, FORWARD_PER, CONSENSUS_PROVIDER_COUNT를 읽고
  as_of_date 이후 컨센서스는 score evidence로 차단한다.
  TARGET_PRC/EPS는 medium_term_revision_visibility claim으로만 매핑한다.
  다만 TARGET_PRC/EPS 개별 필드 존재만으로 POSITIVE polarity를 만들지 않고,
  CONSENSUS_AS_OF_DATE + EPS/목표가 + 추정기관수 조합으로 current consensus visibility
  composite signal을 만든다.
  cash_or_revision_conversion, hbm_capacity_pre_sold, customer_preorder_or_allocation 같은
  원래 C06 material gap은 그대로 unsatisfied로 남긴다.
  targeted tests:
    tests.test_research_brain_v4_real_source_acquisition
    tests.test_research_brain_v4_evidence_extraction_from_real_document
    tests.test_research_brain_v4_operational_modes
    Ran 99 tests in 3.597s
    OK
  full suite:
    PYTHONPATH=src python -m unittest discover -s tests -v
    Ran 5084 tests in 216.741s
    OK
  real planner smoke:
    output/census_v4/2026-07-01-real-planner-companyguide-claims-v60
    exit code = 1 / NOT_READY
    Full Thesis seed 000660 trace accepted_claim_count = 4
    Full Thesis seed source-task accepted refs = 6
    accepted primitive = medium_term_revision_visibility only
    direct_accepted_claim_count = 0
    direct_source_task_satisfied_count = 0
    full_thesis_claim_count = 0
    brain_promoted_stage_row_count = 0
    verdict = BLOCKED
  current blocker:
    CompanyGuide numeric consensus can now produce source-backed visibility claims,
    but no direct C06 Full Thesis primitive has been satisfied yet.
  current truth remains:
    CENSUS_EVENT_BOARD state rows exist
    FULL_THESIS rows = 0
    FULL_E2R_100 rows = 0

CompanyGuide claim dedupe, v61:
  v60에서 CompanyGuide 컨센서스 표 하나가 여러 SourceTask를 지나며
  task/request별 anchor_id와 claim_id로 불어나는 문제가 확인됐다.
  v61은 live official EvidenceAnchor.normalized_value에서
  volatile source_fetch_result 전체 dict를 제거하고,
  official_document_id / provider_request_id / structured row 같은 안정 값만 남겼다.
  targeted tests:
    tests.test_research_brain_v4_evidence_extraction_from_real_document
    tests.test_research_brain_v4_real_source_acquisition
    Ran 49 tests
    OK
  extended targeted tests:
    tests.test_research_brain_v4_evidence_extraction_from_real_document
    tests.test_research_brain_v4_real_source_acquisition
    tests.test_research_brain_v4_operational_modes
    tests.test_census_v4_brain_web_readiness_gate
    tests.test_census_v4_full_thesis_smoke_tasks
    Ran 128 tests in 32.592s
    OK
  full suite:
    PYTHONPATH=src python -m unittest discover -s tests -v
    Ran 5085 tests in 206.731s
    OK
  real planner smoke:
    output/census_v4/2026-07-01-real-planner-companyguide-dedupe-v61
    exit code = 1 / NOT_READY
    verdict = BLOCKED
    v60 Full Thesis seed accepted refs / unique claims = 6 / 4
    v61 Full Thesis seed accepted refs / unique claims = 4 / 1
    accepted primitive = medium_term_revision_visibility only
    direct_accepted_claim_count = 0
    direct_source_task_satisfied_count = 0
    brain_promoted_stage_row_count = 0
    full_thesis_claim_count = 0
    llm_claim_extractor_attempt_count = 0
    web_fetched_document_count = 0
  current blocker:
    CompanyGuide consensus duplicate fan-out는 줄었지만,
    C06 직접 primitive인 customer allocation, capacity pre-sold,
    shipment/revenue mix, cash/FCF conversion은 아직 source-backed로 닫히지 않았다.
    LLM contract-blind claim extractor live path도 이번 smoke에서는 0회다.
  current truth remains:
    CENSUS_EVENT_BOARD state rows exist
    FULL_THESIS rows = 0
    FULL_E2R_100 rows = 0
  next attack points:
    same CompanyGuide anchor/primitive claim dedupe,
    CompanyGuide absolute consensus vs real revision delta separation,
    IssuerIR provider repair,
    C06 customer/capacity/revenue/cash direct primitive acquisition,
    live contract-blind LLM extractor activation.

Rerouted feedback source filter, v64:
  v61은 같은 CompanyGuide 컨센서스 표가 여러 claim으로 증식하는 문제를 줄였다.
  하지만 원래 C06 gap은 여전히 비어 있는데, retry planner가 다시 CompanyGuide를 내면
  같은 medium_term_revision_visibility claim이 hbm_capacity_pre_sold,
  cash_or_revision_conversion, revenue_visibility_contract 같은 빈칸에 반복 accepted되는 문제가 남았다.
  v64는 rerouted accepted claim feedback을 planner context에 넣고,
  특정 primitive gap을 직접 닫지 못한 source class를 같은 unsatisfied primitive retry에서 제거한다.
  제거 후 남은 source class가 없으면 조용히 사라지지 않고
  REJECTED_BY_POLICY source_task_execution row를 남긴다.
  targeted tests:
    tests.test_research_brain_v4_operational_modes
    Ran 58 tests in 3.482s
    OK
  extended targeted tests:
    tests.test_research_brain_v4_evidence_extraction_from_real_document
    tests.test_research_brain_v4_real_source_acquisition
    tests.test_research_brain_v4_operational_modes
    tests.test_census_v4_brain_web_readiness_gate
    tests.test_census_v4_full_thesis_smoke_tasks
    Ran 135 tests in 34.096s
    OK
  full suite:
    PYTHONPATH=src python -m unittest discover -s tests -v
    Ran 5092 tests in 211.923s
    OK
    This is regression evidence only, not operational readiness evidence.
  real planner smoke:
    output/census_v4/2026-07-01-real-planner-rerouted-source-filter-v64
    exit code = 1 / NOT_READY
    verdict = BLOCKED
    planner_runs = 22
    real_provider_success_count = 2
    Full Thesis seed 000660 rows = 12
    accepted refs / unique claims = 2 / 1
    accepted primitive = medium_term_revision_visibility only
    rerouted_source_task_claim_count = 1
    direct_accepted_claim_count = 1
    policy_rejected_source_task_execution_count = 1
    brain_promoted_stage_row_count = 0
    full_thesis_claim_count = 0
    llm_claim_extractor_attempt_count = 0
    web_fetched_document_count = 0
  current truth remains:
    CENSUS_EVENT_BOARD state rows exist
    census_stage_status.stage = None for 3391 rows
    FULL_THESIS rows = 0
    FULL_E2R_100 rows = 0
  current blocker:
    CompanyGuide consensus can satisfy medium_term_revision_visibility only.
    C06 material primitives such as customer allocation, capacity pre-sold,
    qualification, revenue mix, cash/FCF bridge remain UNKNOWN.
    LLM contract-blind claim extractor live path and web acquisition are still 0회 in this smoke.
  next attack points:
    recursive planner context forbidden-key sanitizer,
    full_thesis_queue_context stage/score-like key leakage review,
    direct accepted claim that does not close material primitive gap,
    live LLM claim extractor activation,
    IssuerIR/company source acquisition repair,
    material primitive quorum gate,
    source lineage dedupe across wrapper sources,
    bounded 삼성전자/SK하이닉스 Full Thesis smoke.

Planner candidate context sanitizer, v67:
  v64 cross-review에서 맞게 지적된 남은 구멍은
  existing_evidence_summary가 아니라 candidate_event 원본이었다.
  planner raw prompt의 candidate_event.event_summary / structured_payload / raw_reason_codes에
  source_stage_signal, source_stage_decision_status, source_base_stage,
  source_score_contribution_ids, event_board_non_stage0... 같은 event-board 판정 힌트가 남아 있었다.
  v67은 candidate_event 자체를 planner prompt에 넣기 전에 재귀적으로 sanitize한다.
  유지:
    missing_full_thesis_primitives
    source_missing_primitives
    source_material_gap_ids
    preferred/fallback source classes
    official_first_required
  제거:
    score/stage류 key
    source_stage_* key/value assignment
    source_base_stage
    source_score_contribution_ids
    raw_reason_code의 stage/score류 코드
  focused tests:
    tests.test_research_brain_v4_operational_modes.
      test_prompt_payload_sanitizes_candidate_event_score_stage_context
    tests.test_research_brain_v4_operational_modes.
      test_prompt_payload_sanitizes_direct_existing_evidence_summary_input
    tests.test_research_brain_v4_operational_modes.
      test_full_thesis_seed_context_is_visible_to_planner_without_forcing_target_archetype
    Ran 3 tests
    OK
  related tests:
    tests.test_research_brain_v4_operational_modes
    tests.test_research_brain_v4_real_planner_provider
    tests.test_census_v4_full_thesis_smoke_tasks
    Ran 78 tests in 26.580s
    OK
  full suite:
    PYTHONPATH=src python -m unittest discover -s tests -v
    Ran 5095 tests in 207.773s
    OK
  diff check:
    git diff --check
    OK
  real planner smoke:
    output/census_v4/2026-07-01-real-planner-context-sanitizer-v67
    exit code = 1 / NOT_READY
    verdict = BLOCKED
    llm_planner_call_count = 22
    llm_real_provider_success_count = 2
    source_task_execution_count = 12
    real_document_fetched_count = 4
    accepted refs / unique claims = 2 / 1
    accepted primitive = medium_term_revision_visibility only
    direct_accepted_claim_count = 0
    direct_source_task_satisfied_count = 0
    brain_promoted_stage_row_count = 0
    full_thesis_claim_count = 0
    llm_claim_extractor_attempt_count = 0
    web_fetched_document_count = 0
  raw prompt check:
    candidate_event.event_summary no longer contains source_stage_signal/source_stage_decision_status/source_base_stage.
    raw_reason_codes no longer contains event_board_non_stage0_needs_full_thesis_refresh.
    candidate_event.structured_payload no longer contains source_base_stage/source_stage_signal/source_stage_decision_status/source_score_contribution_ids.
    Remaining "score"/"stage" strings are only in forbidden_output_keys/rules, not score evidence.
  current truth remains:
    census_stage_status rows = 3391
    stage_scope = CENSUS_EVENT_BOARD 3391
    operator_stage_use = NOT_FULL_THESIS_STAGE 3391
    census_stage_status.stage = None 3391
    base_stage memo distribution:
      Stage0 3306 / Stage1 54 / Stage2-Watch 30 / Red 1
    FULL_THESIS rows = 0
    FULL_E2R_100 rows = 0
    verified_score_present_count = 0
  current blocker:
    v67 fixes planner input contamination, not source-backed thesis completion.
    CompanyGuide consensus creates medium_term_revision_visibility only.
    C06 material primitives such as customer allocation, capacity pre-sold,
    qualification, revenue mix, cash/FCF bridge remain UNKNOWN.
    LLM contract-blind claim extractor live path is still 0회 in this smoke.
  next attack points:
    live contract-blind LLM claim extractor activation,
    IssuerIR/company source acquisition repair,
    C06 direct primitive acquisition,
    event_board_* context further minimization review,
    bounded 삼성전자/SK하이닉스 Full Thesis smoke.

Brain/Web enabled diagnostic, sourcequality-v28:
  source_task_execution_count = 23
  official_accepted_claim_count = 48
  web_or_llm_accepted_claim_count = 0
  web_search_task_count = 6
  web_search_call_count = 6
  web_search_result_count = 20
  web_fetched_document_count = 1
  web_rejected_document_count = 14
  llm_claim_extractor_attempt_count = 1
  llm_planner_call_count = 23
  verdict = BLOCKED

Source lineage retry guard, v36:
  source_lineage_unverified_original feedback 이후에도 retry planner가
  NaverSearch/GeneralWeb/IndustryMedia/News/Web 같은 discovery-only source task만 다시 내면 실행하지 않는다.
  CompanyNewsroom/ReportPDF/IR/DART/KIND/TrustedNews처럼 원문 또는 원문 검증 가능 source class를 포함한 retry task는 유지한다.
  이것은 검색어 템플릿 하드코딩이 아니라 source admissibility 정책 검증이다.
  쉬운 예: 네이버 검색으로 찾은 뉴스가 원문 lineage 미검증으로 reject됐는데,
  다음 retry가 다시 네이버/업계매체 검색만 가져오면 버리고,
  회사 뉴스룸/IR PDF 원문을 가져오면 실행한다.
  latest full unittest after v36:
    PYTHONPATH=src python -m unittest discover -s tests -v
    Ran 5067 tests in 213.319s
    OK

Source lineage retry drop leaf audit, v37:
  v36에서 discovery-only retry task를 실행 전 드롭했지만,
  조용히 사라지면 다음 감사자가 왜 조사가 멈췄는지 추적하기 어렵다.
  v37은 드롭된 retry task를 REJECTED_BY_POLICY source_task_execution으로 bundle에 붙여
  source_task_executions.jsonl과 source_tasks.jsonl에 남긴다.
  쉬운 예: "네이버 원문 미검증이라 reject" 뒤에 LLM이 다시 NaverSearch/IndustryMedia만 내면,
  실행은 안 하지만 dropped:source_lineage_retry_discovery_only_after_unverified_original row가 남는다.
  targeted tests:
    source lineage retry drop audit row + Census bundle export
    Ran 2 tests
    OK
  related module tests:
    tests.test_research_brain_v4_operational_modes: Ran 46 tests OK
    tests.test_census_v4_brain_bundle_export: Ran 8 tests OK
  expanded source/readiness tests:
    real source acquisition + evidence extraction + operational modes + brain bundle export + readiness/run-mode honesty
    Ran 133 tests in 42.317s
    OK
  full suite:
    PYTHONPATH=src python -m unittest discover -s tests -v
    Ran 5069 tests in 205.543s
    OK
  current Stage truth:
    CENSUS_EVENT_BOARD stage rows exist: 3391
    FULL_THESIS operating stage rows: 0
    FULL_E2R verified score rows: 0

Retry drop readiness audit, v38:
  v37은 drop row를 leaf에 남겼고,
  v38은 같은 drop을 brain_web_readiness_gate_audit.json과 readiness_verdict.json 요약에도 count로 노출한다.
  추가 fields:
    policy_rejected_source_task_execution_count
    zero_budget_policy_rejected_source_task_execution_count
    source_lineage_feedback_retry_dropped_count
    discovery_only_retry_after_unverified_original_count
  쉬운 예: source_task_executions.jsonl에 zero-budget REJECTED_BY_POLICY retry drop이 있으면,
  readiness gate도 source_lineage_feedback_retry_dropped_count = 1로 보여준다.
  targeted test:
    tests.test_census_v4_brain_web_readiness_gate.CensusV4BrainWebReadinessGateTests.test_source_lineage_retry_drop_is_counted_in_readiness_gate
    Ran 1 test
    OK
  related tests:
    tests.test_census_v4_brain_web_readiness_gate + tests.test_census_v4_brain_bundle_export + tests.test_census_v4_run_mode_honesty
    Ran 44 tests in 43.109s
    OK
  full suite:
    PYTHONPATH=src python -m unittest discover -s tests -v
    Ran 5070 tests in 213.234s
    OK

Source lineage good retry acceptance chain, v39:
  v35~v38은 source_lineage_unverified_original 이후 discovery-only retry를 막고 감사에 남겼다.
  v39는 반대로 좋은 retry, 즉 DART/IR/CompanyNewsroom/ReportPDF 같은 원문 가능 source task가 나오면
  버리지 않고 실행해서 accepted claim까지 갈 수 있음을 테스트로 고정한다.
  쉬운 예: 일반검색 뉴스가 원문 lineage 미검증으로 reject된 뒤,
  LLM retry가 DART 원문 계약 공시로 방향을 바꾸면 계약금액/기간 anchor에서 accepted_claim_ids가 생긴다.
  추가 테스트:
    tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_source_lineage_feedback_retry_can_execute_original_source_and_accept_claim
  targeted test:
    Ran 1 test in 0.521s
    OK
  operational mode tests:
    tests.test_research_brain_v4_operational_modes
    Ran 47 tests in 2.470s
    OK
  expanded source/readiness tests:
    real source acquisition + evidence extraction + operational modes + brain bundle export + readiness/run-mode honesty
    Ran 137 tests in 40.700s
    OK
  full suite:
    PYTHONPATH=src python -m unittest discover -s tests -v
    Ran 5071 tests in 219.963s
    OK
  current Stage truth remains unchanged:
    CENSUS_EVENT_BOARD stage rows exist
    FULL_THESIS operating stage rows: 0
    FULL_E2R verified score rows: 0
  next attack point:
    unit runner가 아니라 실제 connector/frozen live snapshot에서
    source-lineage retry accepted claim -> score contribution -> primitive state -> StageCourt -> FULL_THESIS row
    전체 leaf chain을 검증해야 한다.

Source lineage retry outcome readiness counts, v40:
  v39는 good retry가 accepted claim까지 갈 수 있음을 테스트했고,
  v40은 그 결과를 brain_web_readiness_gate_audit.json과 readiness_verdict.json에 분리 count로 노출한다.
  추가 fields:
    source_lineage_feedback_retry_execution_count
    source_lineage_feedback_retry_accepted_execution_count
    source_lineage_feedback_retry_no_evidence_execution_count
    source_lineage_feedback_retry_dropped_count
    discovery_only_retry_after_unverified_original_count
  쉬운 예: 원문 미검증으로 탈락한 일반검색 뒤에 LLM이 DART 원문 retry를 내고 accepted claim이 생기면,
  accepted_execution_count = 1로 보인다. 다시 못 찾으면 no_evidence_execution_count, 정책상 버리면 dropped_count로 보인다.
  targeted tests:
    source-lineage drop count + good/no-evidence retry outcome count
    Ran 2 tests in 0.002s
    OK
  related tests:
    tests.test_census_v4_brain_web_readiness_gate + tests.test_census_v4_run_mode_honesty + tests.test_census_v4_brain_bundle_export + tests.test_research_brain_v4_operational_modes
    Ran 92 tests in 41.515s
    OK
  full tests:
    PYTHONPATH=src python -m unittest discover -s tests -v > /tmp/census_v40_full_unittest.log 2>&1
    Ran 5072 tests in 222.590s
    OK
  current Stage truth remains unchanged:
    CENSUS_EVENT_BOARD stage rows exist
    FULL_THESIS operating stage rows: 0
    FULL_E2R verified score rows: 0
  next attack point:
    accepted retry execution이 실제 connector/frozen live snapshot에서
    accepted_claims -> score_contributions -> primitive_states -> stagecourt_traces -> census_stage_status까지 이어지는지 검증해야 한다.

Stage truth hard review, v41:
  doc:
    docs/0701/census_v4_0701_v41_stage_truth_hard_review_2026-07-02.md
  결론:
    Stage처럼 보이는 row는 있다.
    하지만 그 row는 CENSUS_EVENT_BOARD 상태판 row이고, 운영에 쓸 FULL_THESIS Stage row는 현재 0개다.
  교차검증:
    readiness verdict:
      stage_scope_notice = NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST
      brain_web_readiness_gate.verdict = NOT_REQUESTED
    sample leaf bundle:
      rows = 67
      stage_scope = CENSUS_EVENT_BOARD 67
      score_scale = EVENT_WEIGHTED_PARTIAL 67
      operator_stage_use = NOT_FULL_THESIS_STAGE 67
    FULL_THESIS marker search:
      stage_scope=FULL_THESIS / operator_stage_use=FULL_THESIS_STAGE / score_scale=FULL_E2R_100 match 없음
    full thesis production:
      PENDING_FULL_THESIS_PRODUCTION
      promoted_full_thesis_row_count = 0
  쉬운 예:
    SK하이닉스에 Stage1이 보여도 그것은 "공식 이벤트 상태판 watch"이지
    "C06 HBM FULL_THESIS 운영 Stage"가 아니다.
  다음 패치 방향:
    v40 이후 operational artifact를 재생성하고,
    source-lineage retry accepted claim이
    score contribution -> primitive state -> StageCourt trace -> FULL_THESIS row까지 이어지는지 닫아야 한다.

Full thesis queue materialization audit, v42:
  doc:
    docs/0701/census_v4_0701_v42_full_thesis_queue_materialization_audit_2026-07-02.md
  patch:
    full_thesis_production_runner_audit.json에 queue -> production candidate materialization 상태를 분리 count로 노출한다.
    readiness_verdict.md.json에도 full_thesis_production_runner_audit 요약을 노출한다.
  added audit fields:
    candidate_source_counts
    refresh_queue_materialized_candidate_count
    refresh_queue_unmaterialized_candidate_count
    refresh_queue_unmaterialized_sample
    refresh_queue_to_candidate_rule
  canonical rerun:
    ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
    full_thesis_refresh_queue_candidate_count = 85
    candidate_row_count = 0
    candidate_source_counts = {}
    refresh_queue_materialized_candidate_count = 0
    refresh_queue_unmaterialized_candidate_count = 85
    promoted_full_thesis_row_count = 0
    readiness.full_thesis_production_runner_audit.refresh_queue_unmaterialized_candidate_count = 85
  쉬운 예:
    85개 후보가 "정밀 평가 대기열"에 있지만,
    아직 Research Brain/official-full-thesis StageCourt trace가 없어서 production FULL_THESIS candidate는 0개다.
  tests:
    tests.test_census_v4_brain_stage_promotion_gate
      Ran 13 tests in 4.438s
      OK
    related full-thesis/manifest/report tests
      Ran 27 tests in 29.737s
      OK
    readiness exposure target
      Ran 8 tests in 20.052s
      OK
    full suite
      Ran 5073 tests in 202.898s
      OK
  next patch:
    queue를 실제 Research Brain planner/source task/Evidence OS/StageCourt trace로 materialize해야 한다.

Full thesis queue seed to Research Brain input, v43:
  doc:
    docs/0701/census_v4_0701_v43_full_thesis_queue_seed_to_research_brain_input_2026-07-02.md
  patch:
    run_census_mode_v4()가 Research Brain 실행 전에 CENSUS_EVENT_BOARD stage row와
    full_thesis_refresh_queue를 먼저 만들고,
    queue row를 research_brain_full_thesis_seed_events.jsonl로 변환한다.
    ProductionShadowV4Config.candidate_event_seed_path로 seed path를 넘기고,
    Research Brain planner candidate order에서 CensusFullThesisQueue seed를 먼저 보게 한다.
  why:
    v42까지는 queue가 Research Brain 실행 뒤에 생겼다.
    그래서 "full-thesis refresh queue 85개"가 있어도 Research Brain은 그 입력을 본 적이 없었다.
  canonical rerun:
    ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
    CENSUS_EVENT_BOARD rows = 3391
    FULL_THESIS rows = 0
    FULL_E2R_100 verified score rows = 0
    full_thesis_refresh_queue rows = 85
    research_brain_full_thesis_seed_events rows = 85
    brain_web_attempt.full_thesis_seed_event_count = 85
    brain_web_attempt.full_thesis_seed_consumed_by_research_brain = false
    brain_web_readiness_gate.full_thesis_seed_event_count = 85
    brain_web_readiness_gate.full_thesis_seed_consumed_by_research_brain = false
  enabled wiring smoke:
    brain_web_mode=enabled, brain_planner_provider=none
    full_thesis_seed_event_count = 85
    full_thesis_seed_consumed_by_research_brain = false
    full_thesis_seed_planner_run_count = 2
    full_thesis_seed_real_provider_success_count = 0
    first_planner_source_family = CensusFullThesisQueue
    accepted_claim_count = 0
    gate verdict = BLOCKED
  쉬운 예:
    접수표 85명을 이제 의사에게 먼저 넘긴다.
    하지만 접수표 자체는 진단서가 아니다.
    seed event는 score evidence가 아니고, accepted claim/StageCourt trace 없이 Stage로 승격하지 않는다.
  tests:
    targeted seed priority + queue seed artifact tests
      OK
    related Research Brain / full-thesis / readiness / manifest tests
      Ran 93 tests in 36.941s
      OK
    full suite
      Ran 5075 tests in 205.207s
      OK
  next patch:
    seed가 real planner/source task/Evidence OS/StageCourt trace로 이어지는 full chain을 닫아야 한다.

Full thesis seed materialization runtime counts, v44:
  doc:
    docs/0701/census_v4_0701_v44_full_thesis_seed_materialization_runtime_counts_2026-07-03.md
  patch:
    `full_thesis_seed_consumed_by_research_brain`을 seed_count > 0으로 보지 않고,
    실제 planner_runs 안의 CensusFullThesisQueue/full_thesis_refresh_seed event와
    real-provider success 여부로 계산한다.
    source task, accepted claim, StageCourt trace까지 각각 분리 count를 추가했다.
  added fields:
    full_thesis_seed_planner_run_count
    full_thesis_seed_real_provider_success_count
    full_thesis_seed_source_task_execution_count
    full_thesis_seed_accepted_claim_count
    full_thesis_seed_stagecourt_trace_count
    full_thesis_seed_materialized_to_stagecourt
  canonical disabled rerun:
    ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
    full_thesis_seed_event_count = 85
    full_thesis_seed_consumed_by_research_brain = false
    full_thesis_seed_planner_run_count = 0
    full_thesis_seed_source_task_execution_count = 0
    full_thesis_seed_accepted_claim_count = 0
    full_thesis_seed_stagecourt_trace_count = 0
    full_thesis_seed_materialized_to_stagecourt = false
  enabled provider-none wiring smoke:
    full_thesis_seed_event_count = 85
    full_thesis_seed_consumed_by_research_brain = false
    full_thesis_seed_planner_run_count = 2
    full_thesis_seed_real_provider_success_count = 0
    full_thesis_seed_source_task_execution_count = 0
    full_thesis_seed_accepted_claim_count = 0
    full_thesis_seed_stagecourt_trace_count = 0
    full_thesis_seed_materialized_to_stagecourt = false
    brain_web_readiness_gate.verdict = BLOCKED
    blocker includes:
      full-thesis seed planner runs have no real-provider success
  쉬운 예:
    접수표가 있다고 의사가 봤다는 뜻이 아니고,
    접수 시스템에 예약 row가 있다고 실제 의사가 본 것도 아니다.
    의사가 실제로 봤다고 해도 검사/진단서/최종 판정이 끝났다는 뜻은 아니다.
    v44는 이 단계를 각각 따로 센다.
  tests:
    targeted seed materialization tests OK
    related Research Brain / full-thesis / readiness / manifest tests
      Ran 93 tests in 36.941s
      OK
    full suite
      Ran 5075 tests in 205.207s
      OK
  next patch:
    seed planner output이 real/frozen-live source task execution과 accepted claim, StageCourt trace로 이어지는 full chain을 닫아야 한다.

Stage existence and seed-materialization hard cross-audit, v45:
  doc:
    docs/0701/census_v4_0701_v45_stage_existence_seed_materialization_cross_audit_2026-07-03.md
  direct answer:
    상태판 Stage는 있다.
    운영 FULL_THESIS Stage는 없다.
  verified counts:
    census_stage_status rows = 3391
    stage_scope = CENSUS_EVENT_BOARD 3391
    operator_stage_use = NOT_FULL_THESIS_STAGE 3391
    base_stage = Stage0 3306, Stage1 54, Stage2-Watch 30, Red 1
    non-Stage0 event-board rows = 85
    FULL_THESIS rows = 0
    FULL_E2R_100 verified score rows = 0
    full_thesis_stage = FULL_THESIS_NOT_RUN 3391
  seed chain:
    refresh queue rows = 85
    research_brain_full_thesis_seed_events rows = 85
    canonical brain_web_attempt = NOT_REQUESTED
    canonical full_thesis_seed_consumed_by_research_brain = false
    canonical full_thesis_seed_planner_run_count = 0
    canonical full_thesis_seed_source_task_execution_count = 0
    canonical full_thesis_seed_accepted_claim_count = 0
    canonical full_thesis_seed_stagecourt_trace_count = 0
  review rule:
    base_stage만 보고 Stage가 있다고 말하면 fail이다.
    stage_scope, operator_stage_use, full_thesis_stage, score_scale을 같이 봐야 한다.
  verification:
    related suite:
      Ran 93 tests in 36.941s
      OK
    full suite:
      Ran 5075 tests in 205.207s
      OK

Full thesis seed materialization trace leaf, v46:
  doc:
    docs/0701/census_v4_0701_v46_full_thesis_seed_materialization_trace_leaf_2026-07-03.md
  patch:
    `full_thesis_seed_materialization_trace.jsonl`을 output leaf와 docs/operational에 추가했다.
    이제 seed 85개 각각이 planner/source task/accepted claim/StageCourt/FULL_THESIS 중 어디에서 멈췄는지 row 단위로 보인다.
  canonical disabled rerun:
    ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
    full_thesis_seed_materialization_trace rows = 85
    materialization_status = PLANNER_NOT_RUN 85
    final_stage_scope = CENSUS_EVENT_BOARD 85
    final_operator_stage_use = NOT_FULL_THESIS_STAGE 85
    final_full_thesis_stage = FULL_THESIS_NOT_RUN 85
    planner/source/claim/stagecourt sum = 0/0/0/0
  manifest:
    full_thesis_seed_materialization_trace.jsonl row_count = 85
    sha256 = 9f48ac0117dd6779adcbc965fe9b22ebacdefcc3807b38ccae94f3d62a27deb1
  쉬운 예:
    전에는 접수표 85명만 있었다.
    이제는 접수표 85명 각각에 "아직 의사에게 가지 않음"이라는 상태표가 붙었다.
    아직 진단서가 생긴 것은 아니다.
  tests:
    targeted trace/manifest tests:
      Ran 3 tests in 11.369s
      OK
    related audit suite:
      Ran 93 tests in 40.287s
      OK
    full suite:
      Ran 5075 tests in 214.423s
      OK

Stage existence answer / next patch direction, v47:
  doc:
    docs/0701/census_v4_0701_v47_stage_existence_answer_and_next_patch_direction_2026-07-03.md
  hard answer:
    Stage label은 있다.
    하지만 현재 canonical run에는 운영 FULL_THESIS Stage가 0개다.
  direct count:
    census_stage_status rows = 3391
    stage_scope = CENSUS_EVENT_BOARD 3391
    operator_stage_use = NOT_FULL_THESIS_STAGE 3391
    base_stage = Stage0 3306, Stage1 54, Stage2-Watch 30, Red 1
    full_thesis_stage = FULL_THESIS_NOT_RUN 3391
    score_scale = NO_SCORE 3324, EVENT_WEIGHTED_PARTIAL 67
    FULL_THESIS rows = 0
    FULL_E2R_100 verified score rows = 0
    non-Stage0 event-board rows = 85
  seed trace:
    full_thesis_seed_materialization_trace rows = 85
    materialization_status = PLANNER_NOT_RUN 85
    planner/source/claim/stagecourt sum = 0/0/0/0
  쉬운 예:
    접수표에는 상태가 적혀 있지만, 의사 진단서는 아직 없다.
    현재 Stage1/Stage2-Watch/Red는 접수표 상태이고 FULL_THESIS 진단서가 아니다.
  next patch:
    seed -> real planner -> bounded source task -> accepted claim -> score contribution -> StageCourt -> FULL_THESIS promotion decision

Full thesis seed materialization audit leaf, v48:
  doc:
    docs/0701/census_v4_0701_v48_full_thesis_seed_materialization_audit_leaf_2026-07-03.md
  patch:
    `full_thesis_seed_materialization_audit.json`을 output leaf와 docs/operational에 추가했다.
    seed trace를 다시 세서 실행 전 점수/Stage 누수, 단계 순서 위반, 잘못된 FULL_THESIS_PROMOTED를 잡는다.
  canonical disabled rerun:
    ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
    seed_event_count = 85
    trace_row_count = 85
    status_counts = PLANNER_NOT_RUN 85
    final_stage_scope_counts = CENSUS_EVENT_BOARD 85
    critical_count = 0
    verdict = PASS
  manifest:
    full_thesis_seed_materialization_audit.json byte_size = 2007
    sha256 = 42d6a14baeb189701ab68d5eabe54d5d62e0c878cbc2d24e3464fbdd8b78d839
  tests:
    targeted trace/audit/manifest tests:
      Ran 3 tests in 7.100s
      OK
    related audit suite:
      Ran 94 tests in 37.769s
      OK
    full suite:
      Ran 5076 tests in 209.671s
      OK
  current truth:
    상태판 Stage는 있다.
    운영 FULL_THESIS Stage는 없다.
    audit은 완료 증명이 아니라 미완료 지점을 못 속이게 하는 증거다.

Seed materialization audit readiness / goal gate link, v49:
  doc:
    docs/0701/census_v4_0701_v49_seed_materialization_audit_readiness_goal_gate_link_2026-07-03.md
  patch:
    `full_thesis_seed_materialization_audit.json`을 readiness_verdict, goal_requirement_matrix, goal_completion_audit에 연결했다.
    controlled smoke FULL_THESIS row는 production seed materialization으로 보지 않도록 분리했다.
  canonical disabled rerun:
    ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
  readiness:
    label includes FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS
    remaining_operational_gaps includes "full-thesis seed materialization audit shows no promoted FULL_THESIS seed"
    full_thesis_seed_materialization_audit.status_counts = PLANNER_NOT_RUN 85
    full_thesis_seed_materialization_audit.full_thesis_promoted_seed_count = 0
  goal matrix:
    gate FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS = PASS
  goal completion:
    full_thesis_seed_materialization_audit_pass_allowed = true
    goal_completion_ready = false
  tests:
    targeted readiness/goal/seed tests:
      Ran 3 tests in 7.380s
      OK
    related audit suite:
      Ran 94 tests in 36.828s
      OK
    full suite:
      Ran 5076 tests in 200.894s
      OK
  current truth:
    seed audit는 readiness/goal에도 노출된다.
    그러나 promoted FULL_THESIS seed는 아직 0개다.

Seed promotion gate split / cross-validation, v50:
  doc:
    docs/0701/census_v4_0701_v50_seed_promotion_gate_split_cross_validation_and_next_patch_direction_2026-07-03.md
  patch:
    `FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS`와
    `FULL_THESIS_SEED_PROMOTION_PASS`를 분리했다.
    audit pass는 "seed/trace 장부가 정상"이라는 뜻이고,
    promotion pass는 "적어도 하나의 seed가 production FULL_THESIS로 실제 승격"됐다는 뜻이다.
  canonical disabled rerun:
    ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
  readiness:
    label includes FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS
    label includes FULL_THESIS_SEED_PROMOTION_PENDING
    label does not include FULL_THESIS_SEED_PROMOTION_PASS
    full_thesis_seed_materialization_audit.status_counts = PLANNER_NOT_RUN 85
    full_thesis_seed_materialization_audit.full_thesis_promoted_seed_count = 0
    full_thesis_seed_materialization_audit.full_thesis_seed_promotion_pass = false
  goal matrix:
    gate FULL_THESIS_SEED_MATERIALIZATION_AUDIT_PASS = PASS
    gate FULL_THESIS_SEED_PROMOTION_PASS = PENDING
    required_goal_completion_pass_count = 13
    required_goal_completion_pending_count = 6
    required_goal_completion_fail_count = 0
  goal completion:
    full_thesis_seed_materialization_audit_pass_allowed = true
    full_thesis_seed_promotion_pass_allowed = false
    blocker includes full_thesis_seed_promotion_pass_false
    goal_completion_ready = false
  manifest:
    readiness_verdict.json byte_size = 9574
    sha256 = 3d5ba8dc3c43ffca89a023e261d689b347f28b0f50484fd66daa880a791e7c69
    goal_completion_audit.json byte_size = 2744
    sha256 = 444d6ecb0705f43160013a0f7751b3750925eaae4b0306222d95a14830cc386c
    goal_requirement_matrix_audit.json byte_size = 11956
    sha256 = d05126e75c637642e70e92295c1d9fb4e07c4b1ff6ec093ce939c2b1d1db83f9
  tests:
    targeted seed-promotion gate tests:
      Ran 3 tests
      OK
    related audit suite:
      Ran 94 tests in 38.236s
      OK
    full suite:
      Ran 5076 tests in 203.491s
      OK
  current truth:
    상태판 Stage row는 3391개다.
    상태판 non-Stage0 row는 85개다.
    production FULL_THESIS row는 0개다.
    FULL_E2R_100 verified score row는 0개다.
    85개 seed는 접수표에 올라왔지만 아직 real planner/source/claim/StageCourt 경로를 통과하지 않았다.

Seed planner event/run count split and stage truth, v51:
  doc:
    docs/0701/census_v4_0701_v51_seed_planner_event_vs_run_count_audit_and_stage_truth_2026-07-03.md
  patch:
    FULL_THESIS seed runtime audit에서 seed event count와 planner run row count를 분리했다.
    `full_thesis_seed_planner_attempted_event_count`는 planner가 닿은 distinct seed event 수다.
    `full_thesis_seed_planner_run_row_count`는 retry 포함 planner run row 수다.
    기존 `full_thesis_seed_planner_run_count`는 backward compatibility로 distinct seed event count 의미를 유지한다.
  easy example:
    seed A가 initial+retry로 planner row 2개를 만들고,
    seed B가 planner row 1개를 만들면
    attempted_event_count = 2,
    planner_run_row_count = 3이어야 한다.
  canonical disabled rerun:
    ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
  readiness:
    full_thesis_seed_event_count = 85
    full_thesis_seed_planner_attempted_event_count = 0
    full_thesis_seed_planner_run_row_count = 0
    full_thesis_seed_planner_run_count = 0
    full_thesis_seed_accepted_claim_count = 0
    full_thesis_seed_stagecourt_trace_count = 0
    full_thesis_seed_materialization_audit.status_counts = PLANNER_NOT_RUN 85
    full_thesis_seed_materialization_audit.full_thesis_promoted_seed_count = 0
  stage truth:
    상태판 Stage row는 3391개다.
    상태판 non-Stage0 row는 85개다.
    production FULL_THESIS row는 0개다.
    FULL_E2R_100 verified score row는 0개다.
  queue truth:
    full_thesis_refresh_queue row_count = 85
    priority_bucket:
      P2_EVENT_WATCH_REFRESH = 36
      P1_MATERIAL_STAGE_REFRESH = 30
      P1_PENDING_MATERIAL_REFRESH = 18
      P0_RISK_REVIEW_REFRESH = 1
    source_base_stage:
      Stage1 = 54
      Stage2-Watch = 30
      Red = 1
  current truth:
    Stage가 전혀 없는 것은 아니다.
    하지만 지금 존재하는 Stage는 CENSUS_EVENT_BOARD 상태판 Stage다.
    운영 FULL_THESIS Stage는 없다.
    85개 seed는 접수표에 올라왔지만 아직 real planner/source/claim/StageCourt 경로를 통과하지 않았다.
  manifest:
    artifact_manifest.json byte_size = 27339
    sha256 = be159c3b91ca1e2db5f6aab2e71e5cc5b8900c405d764dfa80389c97dda1f78f
    readiness_verdict.json byte_size = 9786
    sha256 = e057e2feee603b374a7f5c624c4e4718567e711d68ad82bba6d106a0993e91fb
    brain_web_readiness_gate_audit.json byte_size = 3806
    sha256 = 66d13485c72d0002e9ca81f7e4088c044dd0e94582547f569f4a61b5e131cf8a
    acceptance_report.md byte_size = 7010
    sha256 = 1c627b36d3b92461b1b75bc65b91d62642f6ef41caaa2a28ebc0c6e4365747ed
  tests:
    targeted seed runtime count tests:
      Ran 3 tests
      OK
    related audit suite:
      Ran 47 tests in 34.933s
      OK
    full suite:
      Ran 5077 tests in 211.027s
      OK
  next patch direction:
    count 정밀화는 완료됐지만 운영 목표는 아직 미완료다.
    다음은 production FULL_THESIS mode에서 seed -> real planner -> bounded source task -> accepted claim -> primitive -> score contribution -> StageCourt 경로를 실제로 닫아야 한다.
    disabled ledger-refresh run에서 FULL_THESIS row가 생기면 critical fail이어야 한다.

Machine-readable test artifact gate clear, v52:
  doc:
    docs/0701/census_v4_0701_v52_machine_readable_test_artifact_gate_clear_and_remaining_goal_blockers_2026-07-03.md
  patch/result:
    공식 test artifact runner로 `e2r_test_result_artifact_v1` JSON과 log hash를 생성했다.
    Census v4 canonical rerun에 `--test-result-artifact`를 연결했다.
  test artifact:
    command = python -m unittest discover -s tests -v
    status = OK
    test_count = 5077
    failed_count = 0
    error_count = 0
    duration_seconds = 211.8717
    log_sha256 = 1ea3a71a886354ee470ab6fb3d3b7f76513c68786c7a7c9530cbacb8c457d220
  canonical rerun:
    ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
  test evidence audit:
    verdict = MACHINE_READABLE_TEST_ARTIFACT_PASS
    completion_eligible = true
    artifact_valid = true
    artifact_test_count = 5077
  goal matrix:
    FULL_TEST_ARTIFACT_PASS is no longer pending
    required_goal_completion_pass_count = 14
    required_goal_completion_pending_count = 5
    required_goal_completion_fail_count = 0
    pending_gate_ids =
      FULL_THESIS_SMOKE_PASS
      FULL_THESIS_PRODUCTION_PASS
      FULL_THESIS_SEED_PROMOTION_PASS
      BRAIN_WEB_EVIDENCE_PASS
      ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
  goal completion:
    goal_completion_ready = false
    blocker removed = machine_readable_test_result_artifact_missing
    remaining blockers =
      brain_web_evidence_pass_false
      full_thesis_smoke_pending
      full_thesis_production_pass_false
      full_thesis_seed_promotion_pass_false
      source_backed_replay_parity_all_archetypes_pending
      goal_requirement_matrix_pass_false
  stage truth:
    상태판 Stage row는 3391개다.
    상태판 non-Stage0 row는 85개다.
    production FULL_THESIS row는 0개다.
    FULL_E2R_100 verified score row는 0개다.
  manifest:
    full_unittest_result_artifact.json byte_size = 624
    sha256 = ba3a2eb0f471d115b5be9dfc19d7660f61e80716c32f469d7c7300bba16c235a
    full_unittest_result_artifact.log byte_size = 749433
    sha256 = 1ea3a71a886354ee470ab6fb3d3b7f76513c68786c7a7c9530cbacb8c457d220
    test_result_evidence_audit.json byte_size = 1348
    sha256 = 12fb9a2e8d5f1e2666fa9d86122e75558d63f50d6a4aeafae474476fa15f293e
    goal_requirement_matrix_audit.json byte_size = 11879
    sha256 = 1f49d1a584ba1bc2dc22572f366d3dd380723f2e2c842d5bcdb30fba1ff814b9
    goal_completion_audit.json byte_size = 2674
    sha256 = 1e465e971e2abcb79a5f9d01c157256b8d823db97668b3097ed9ddb87c576eb2
    artifact_manifest.json byte_size = 27895
    sha256 = 317b059cd2ebc2757ff5caa934d91ee10d7720882f17c1b9e706c079e13fb687
    acceptance_report.md byte_size = 6977
    sha256 = a9612f1bc82897b8ec13ca07cc42c8c44d2417e49507fb79b8ce729eb19d2e2b
  current truth:
    테스트 증거 gate는 닫혔다.
    하지만 운영 FULL_THESIS Stage는 아직 0개다.

Controlled smoke operator use guard, v53:
  doc:
    docs/0701/census_v4_0701_v53_controlled_smoke_operator_use_guard_2026-07-03.md
  patch:
    controlled full-thesis smoke row가 production 운영 Stage처럼 보이지 않도록 operator alias를 분리했다.
  previous risk:
    smoke row stage_scope = FULL_THESIS
    operator_stage_use = FULL_THESIS_STAGE
    operator_score_use = FULL_E2R_SCORE
    but production_full_thesis_row_count = 0
  current smoke-only alias:
    operator_stage_use = SMOKE_ONLY_STAGE_NOT_PRODUCTION
    operator_score_use = SMOKE_ONLY_SCORE_NOT_PRODUCTION
    operator_scope_note = controlled_smoke_full_thesis_not_production
    is_full_thesis_stage = false
    is_full_e2r_score = false
    is_controlled_smoke_full_thesis_stage = true
  canonical disabled run:
    ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
    stage_scope_distribution = CENSUS_EVENT_BOARD 3391
    operator_stage_use_distribution = NOT_FULL_THESIS_STAGE 3391
    operator_score_use_distribution = NOT_FULL_E2R_SCORE 3391
    full_thesis_stage_row_count = 0
    full_e2r_verified_score_row_count = 0
    goal_matrix pass/pending/fail = 14/5/0
  explicit smoke run:
    output_root = output/census_v4/2026-07-01-full-thesis-smoke-v52
    FULL_THESIS_SMOKE_PASS = true
    stage_scope_distribution = CENSUS_EVENT_BOARD 3389, FULL_THESIS 2
    operator_stage_use_distribution = NOT_FULL_THESIS_STAGE 3389, SMOKE_ONLY_STAGE_NOT_PRODUCTION 2
    operator_score_use_distribution = NOT_FULL_E2R_SCORE 3389, SMOKE_ONLY_SCORE_NOT_PRODUCTION 2
    SK하이닉스 smoke full_thesis_stage = Stage3-Yellow, score = 88.0
    삼성전자 smoke full_thesis_stage = Stage2-Watch, score = 72.0
    production_full_thesis_row_count = 0
    controlled_smoke_full_thesis_row_count = 2
    goal_matrix pass/pending/fail = 15/4/0
  tests:
    related smoke/operator/production suite:
      Ran 36 tests in 33.398s
      OK
    full suite artifact:
      Ran 5077 tests
      OK
      log_sha256 = e719c2aa9d8248613ca82ef4eb02e3eab00924123ba80e7629f0b1d41b226620
  manifest:
    canonical artifact_manifest.json byte_size = 27895
    sha256 = 6c1ecbbbff956e61ff5499c8214834c4312b93a6624f2004dd656a5fce0a2dfa
    canonical acceptance_report.md byte_size = 6977
    sha256 = dc83a5eb2407b5e1fd0eb364645c98de289df02cca0ce3f4ed000619c7b25d1d
    smoke artifact_manifest.json byte_size = 28665
    sha256 = bc7bc38711727c4e5f1ab322512942b04f03c36d8c462746a2bb6ec9ba15bc76
    smoke acceptance_report.md byte_size = 7177
    sha256 = 4d54493bbbebf8e05ca797a5081b1709d895322557559327cec434bf200b3597
  current truth:
    controlled smoke는 "로직 검사 통과"이지 "운영 진단서 발급"이 아니다.
    production FULL_THESIS Stage는 아직 0개다.

FULL_THESIS production runner, sourcequality-v28:
  candidate_row_count = 1
  blocked_candidate_count = 1
  promoted_full_thesis_row_count = 0
  blocked symbol = 114450
  blocked archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  missing_green_primitives =
    margin_bridge_visible

Queue / timeout ledger-refresh, provider-timeout-v30:
  brain_web_mode = disabled
  brain_web_readiness verdict = NOT_REQUESTED
  full_thesis_refresh_queue_candidate_count = 85
  production_mode_requested = false
  production runner candidate_row_count = 0
  production runner promoted_full_thesis_row_count = 0
  source_task_execution_count in brain_web_readiness_gate_audit = 0
```

중요: v28과 v30 숫자를 한 실행처럼 섞으면 안 된다.

```text
v28 = Brain/Web enabled attempt. BLOCKED지만 실제 web/search/extractor 시도 숫자가 있다.
v30 = queue/timeout guard ledger-refresh. Brain/Web은 disabled/NOT_REQUESTED이고 queue 85개를 검증한다.

둘 다 공통 결론은 같다.
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
```

현재 Stage 존재 여부를 정확히 나누면:

```text
CENSUS_EVENT_BOARD 상태판 Stage:
  exists.
  row_count = 3391
  non_Stage0 = 85

operator-admissible FULL_THESIS Stage:
  does not exist yet.
  row_count = 0

verified FULL_E2R_100 score:
  does not exist yet.
  row_count = 0

FULL_THESIS refresh queue:
  exists.
  row_count = 85
  audit = PASS

Provider timeout guard:
  claim_extractor_timeout_seconds = 60.0
  llm_claim_extractor_provider_error_count is audited
  llm_claim_extractor_timeout_count is audited
  Brain/Web READY is blocked when unresolved extractor provider_error/timeout exists

Invalid partial output guard:
  KeyboardInterrupt writes partial_run_invalid.json
  runner exception writes partial_run_invalid.json
  stdout = INVALID_PARTIAL_OUTPUT
  interrupted exit_code = 130
  failed exit_code = 1
  readiness_evidence_allowed = false
  score_or_stage_evidence_allowed = false
  full_thesis_promotion_allowed = false

Source route quality guard:
  Tistory/Naver blog/cafe/Telegram/forum/social-style pages are rejected as non-score sources.
  Metadata rejection reason = web_result_low_quality_blog_or_social_not_score_source.
  Fetched-content rejection reason = web_fetch_low_quality_blog_or_social_not_score_source.
  Official DART/KIND detail URLs remain exempt through exact host resolution.
  This is source admissibility, not deterministic query generation.
  Rejected source rows remain planner feedback so the LLM can choose a better route.

Source lineage/original guard:
  General web/Naver-discovered NEWS, IR, report-like pages are not treated as score-admissible original sources
  just because they were fetched.
  Rejection reason = source_lineage_unverified_original:<source_class>:general_web_search_provider.
  Official DART/KIND/KRX/IssuerOfficial FILING detail URLs remain exempt when the resolved document type is FILING.
  This blocks "Naver found an article, so TrustedNews/CompanyNewsroom is satisfied" style false positives.

Source lineage feedback retry guard:
  source_lineage_unverified_original now appears in source_rejection_feedback.not_eligible_reason_distribution.
  Planner prompt rules explicitly say this is discovery-only, not a verified original source.
  feedback_retry planner_run gets planner_feedback =
    previous_source_lineage_unverified_original
    previous_sources_failed_before_or_after_extraction.
  This keeps the LLM from repeating the same generic web/news route after a lineage rejection.
```

쉬운 예:

```text
삼성전자와 SK하이닉스도 상태판 Stage1 샘플에 보인다.
하지만 둘 다 full_thesis_stage = FULL_THESIS_NOT_RUN 이고,
full_thesis_verified_score = None 이다.
따라서 운영 점수/Stage로 말하면 안 된다.
```

v28에서 확인된 진전:

```text
--brain-retry-max가 CLI/config/reproduction command에 추가됐다.
retry_max=3 진단에서 feedback_retry가 1회에서 2회로 늘었다.
source_rejection_feedback_count_sum이 1에서 4로 늘었다.
real_provider_success_count가 2에서 3으로 늘었다.
```

v28에서 아직 막힌 것:

```text
web/LLM accepted claim = 0
general Naver search 문서는 아직 score source가 아니다.
검색 결과가 여전히 Tistory/블로그/급등종목 정리 글 위주다.
FULL_THESIS 승격은 계속 0이어야 한다.
```

쉬운 예:

```text
지금은 "웹 자료를 실제로 찾고 LLM이 읽는 단계"까지는 왔다.
하지만 그 자료가 "점수표 칸에 들어갈 수 있는 검증 claim"은 아직 아니다.

그린생명과학 114450에서 계약 관련 공식 claim은 더 많이 닫혔지만,
margin_bridge_visible이 닫히지 않았다.
급등종목 정리 글이나 블로그로는 C05 Green/FULL_THESIS를 열면 안 된다.
```

다음 패치 방향 요약:

```text
일반 웹 문서를 점수 source로 느슨하게 풀지 않는다.

bounded feedback retry loop는 들어갔다.
FULL_THESIS refresh queue도 leaf artifact로 들어갔다.
다음은 source route 품질 개선과 provider timeout/pending 처리다.
Tistory/텔레그램/급등종목 정리 글을 더 빨리 reject하고,
IR/DART 상세/리포트 PDF/회사 newsroom/신뢰 뉴스 원문 같은 route를 더 우선해야 한다.
CENSUS_EVENT_BOARD 비 Stage0 행은 운영 Stage로 복사하지 말고,
bounded FULL_THESIS refresh queue에 올려서 source-backed primitive를 닫아야 한다.
```

v29 참고:

```text
queue verification output =
  output/census_v4/2026-07-01-full-thesis-refresh-queue-v29

full_thesis_refresh_queue_candidate_count = 85
queue critical counts = 0
expanded tests = 59 OK

sourcequality-v29 live attempt =
  INVALID_PARTIAL_OUTPUT
  codex_cli claim extractor provider 대기로 KeyboardInterrupt 중단
  readiness 증거로 사용 금지
```

v30 참고:

```text
queue / timeout guard verification output =
  output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30

full_thesis_refresh_queue_candidate_count = 85
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
llm_claim_extraction_audit.configured_timeout_seconds = 60.0
llm_claim_extractor_provider_error_count = 0 in disabled ledger-refresh verification
llm_claim_extractor_timeout_count = 0 in disabled ledger-refresh verification

targeted tests =
  tests.test_research_brain_v4_operational_modes
  tests.test_census_v4_brain_web_readiness_gate

result = 54 OK
```

v31 참고:

```text
CLI failure guard:
  KeyboardInterrupt -> partial_run_invalid.status = INTERRUPTED, exit_code = 130
  runner exception -> partial_run_invalid.status = FAILED, exit_code = 1

targeted test:
  PYTHONPATH=src python -m unittest tests.test_census_v4_run_mode_honesty -v

result = 20 OK
```

쉬운 예:

```text
나쁜 패치:
  Tistory 블로그도 LLM이 그럴듯하게 읽었으니 margin_bridge 점수로 인정.

좋은 패치:
  Tistory는 score source가 아니었다고 기록.
  LLM에게 "이 source route는 실패했다"고 알려 주고
  회사 IR, 공시 상세, public report PDF 같은 원문 route를 다시 찾게 함.
```

v32 참고:

```text
patched files =
  src/e2r/research_brain/v4_source_acquisition_runner.py
  tests/test_research_brain_v4_real_source_acquisition.py
  docs/0701/README.md
  docs/0701/census_v4_0701_v32_source_route_quality_blog_social_reject_guard_2026-07-02.md

bug fixed =
  low-quality blog/social filter referenced _official_detail_route_from_url
  before that helper existed.
  A Tistory/blog route could therefore crash instead of producing a clean reject row.

targeted test =
  PYTHONPATH=src python -m unittest tests.test_research_brain_v4_real_source_acquisition -v
  result = 28 OK

expanded cross-check =
  PYTHONPATH=src python -m unittest \
    tests.test_research_brain_v4_real_source_acquisition \
    tests.test_research_brain_v4_operational_modes \
    tests.test_census_v4_brain_web_readiness_gate \
    tests.test_census_v4_run_mode_honesty -v
  result = 102 OK
```

v33 참고:

```text
patched files =
  tests/test_research_brain_v4_operational_modes.py
  docs/0701/README.md
  docs/0701/census_v4_0701_v33_low_quality_source_feedback_prompt_guard_2026-07-02.md

behavior =
  web_result_low_quality_blog_or_social_not_score_source is now specifically tested
  as source_rejection_feedback.
  The feedback appears in planner prompt payload existing_evidence_summary.
  The feedback retry planner runs once and carries the same rejection_reason_distribution.
  The feedback row remains source-level only and does not contain score/stage/current_score_eligible.

targeted test =
  PYTHONPATH=src python -m unittest \
    tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_low_quality_blog_source_rejection_feedback_is_visible_to_planner_prompt_payload \
    tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_low_quality_blog_source_rejection_feedback_retries_planner_once -v
  result = 2 OK

module test =
  PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
  result = 41 OK

expanded cross-check =
  PYTHONPATH=src python -m unittest \
    tests.test_research_brain_v4_real_source_acquisition \
    tests.test_research_brain_v4_operational_modes \
    tests.test_census_v4_brain_web_readiness_gate \
    tests.test_census_v4_run_mode_honesty -v
  result = 104 OK
```

최신 테스트 증거:

```text
full unittest artifact =
  output/test_full_repo_0701/full_unittest_after_p0f_p0j_postextract_bounded_retry_artifact.json

status = OK
test_count = 5055
failed_count = 0
error_count = 0
duration_seconds = 193.9391
log_sha256 =
  5f852f4608b0cdc42dc0b0c35d92e009b31b645eefb87c3c6b8669374c930262
```

2026-07-02 P0-A/P0-C/P0-B 패치 재실행 이전 기준(v23, superseded by v26):

```text
latest patched Brain/Web diagnostic =
  output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v23

latest patched rerun packet =
  docs/0701/census_v4_0701_sourcequality_v23_patch_rerun_result_and_next_bottleneck_2026-07-02.md

verdict = NOT_READY
stage_scope = CENSUS_EVENT_BOARD 3391
BRAIN_WEB_PARTIAL row = 0
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
verified_score_present_count = 0

base_stage_distribution:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

Brain/Web attempt:
  planner_run_count = 22
  real_provider_success_count = 2
  real_provider_failure_count = 1
  source_task_execution_count = 13
  web_search_task_count = 4
  web_fetched_document_count = 2
  llm_claim_extractor_attempt_count = 2
  accepted_claim_count = 4
  official_accepted_claim_count = 4
  web_or_llm_accepted_claim_count = 0

FULL_THESIS production runner:
  candidate_row_count = 1
  blocked_candidate_count = 1
  promoted_full_thesis_row_count = 0
  blocker = missing_green_gate_primitives

v23 candidate:
  symbol = 003090
  archetype = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  present_green_primitives = implementation_timeline
  missing_green_primitives =
    direct_company_cash_route
    policy_or_regulatory_confirmed
    subsidy_capture_visible

v22 regression found and fixed:
  strict planner schema rejected source_task_drafts[*].query_intents because
  it existed in properties but not required.
  v23 rerun confirms real provider success recovered from 0 to 2.
```

쉬운 예:

```text
v23은 "정식 심사장에 올릴 후보 1건"은 찾았다.
하지만 그 후보가 green gate 필수 증빙을 못 닫아서
정식 운영 FULL_THESIS Stage는 아직 0건이다.

즉 Stage 메모가 있는 종목은 있지만,
사용자가 원하는 운영 점수/Stage가 완성된 종목은 아직 없다.
```

2026-07-02 source-class guard 기준선(v21):

```text
latest Brain/Web diagnostic =
  output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21

latest attack packet =
  docs/0701/census_v4_0701_sourcequality_v21_guardtight_stage_truth_and_next_patch_packet_2026-07-02.md

latest deep stage-existence audit =
  docs/0701/census_v4_0701_sourcequality_v21_stage_existence_deep_audit_and_patch_direction_2026-07-02.md

verdict = NOT_READY
stage_scope = CENSUS_EVENT_BOARD 3391
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
verified_score_present_count = 0
web_or_llm_accepted_claim_count = 0

base_stage_distribution:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

important scope split:
  base_stage row = 3391
  non-Stage0 event-board row = 85
  EVENT_WEIGHTED_PARTIAL row = 67
  operator-admissible full thesis row = 0
  operator-admissible full E2R score row = 0

web_search_tasks = 2
web_search_results = 10
web_fetched_documents = 1
claim_extractor_runs = 1

source-class / guard-tight patch result:
  Naver-discovered official URL is classified by exact hostname allowlist only.
  fake path like example.com/.../kind.krx.co.kr/... does not become KIND.
  Naver-discovered NEWS may be labeled IndustryMedia for provenance,
  but it remains score-blocked until trusted news connector/domain allowlist exists.
  v21 Naver NEWS rejection includes general_search_not_score_source and
  source_provider_document_type_mismatch:IndustryMedia:general_web_search_provider.

latest full unittest after source-class guard-tight patch:
  status = OK
  test_count = 5042
  failed_count = 0
  error_count = 0
  duration_seconds = 199.1275
  artifact = output/test_full_repo_0701/full_unittest_after_sourceclass_v21_guardtight_artifact.json
  artifact_sha256 = e259f571feb672804c739628d93929844b08cc91ccf3a3325ab6a3712bc3ca71
  log_sha256 = 1e96b0edee72f47e6c93280e5338c7547dd6e331f5f035d0e74c1c8180739be9

latest local partial patch after deep stage audit:
  scope =
    P0-A FULL_THESIS candidate scan split
    P0-B official detail resolver metadata
    P0-C feedback/query plumbing
    P0-D policy-rejected external task source feedback
    P0-E mixed official/web source-class score guard
  test_result_leaf =
    docs/0701/census_v4_0701_p0c_query_feedback_patch_test_result_2026-07-02.json
  patched_files =
    src/e2r/research_brain/v4_planner_runtime.py
    src/e2r/research_brain/v4_production_orchestrator.py
    src/e2r/research_brain/v4_source_acquisition_runner.py
    src/e2r/research_brain/v4_evidence_extraction_bridge.py
    src/e2r/census/census_runner_v4.py
    tests/test_research_brain_v4_operational_modes.py
    tests/test_research_brain_v4_real_source_acquisition.py
    tests/test_research_brain_v4_evidence_extraction_from_real_document.py
    tests/test_census_v4_brain_stage_promotion_gate.py
    docs/0701/census_v4_0701_sourcequality_v21_stage_existence_deep_audit_and_patch_direction_2026-07-02.md
    docs/0701/census_v4_0701_sourcequality_v23_patch_rerun_result_and_next_bottleneck_2026-07-02.md
    docs/0701/census_v4_0701_sourcequality_v26_external_feedback_sourceclass_patch_and_stage_truth_2026-07-02.md
  behavior =
    task-specific source_task_drafts[*].query_intents override global query_intents
    global query_intents remain fallback only
    direct official accepted claim no longer blocks failed external web/LLM task feedback retry
    policy-rejected external tasks now become source_rejection_feedback instead of silent stops
    FULL_THESIS production runner scans live research_brain_v4_attempt StageCourt traces directly, not only BRAIN_WEB_PARTIAL rows
    official-only complete thesis can be FULL_THESIS candidate without satisfying the separate BRAIN_WEB_EVIDENCE_PASS gate
    Naver/Web-discovered exact KIND/DART official URLs now carry official_detail_resolution metadata
    successful official URL fetches are represented as KIND/DART FILING documents, not Naver score evidence
    failed official URL fetches are rejected as official_detail_resolve_failed, not silent generic web misses
    mixed official/web acquisition no longer checks NEWS documents as DART/KIND filings
  verification =
    targeted 4 tests OK
    tests.test_research_brain_v4_operational_modes 33 tests OK
    tests.test_research_brain_v4_real_planner_provider 6 tests OK
    official detail resolver targeted 5 tests OK
    tests.test_research_brain_v4_real_source_acquisition + tests.test_research_brain_v4_evidence_extraction_from_real_document 41 tests OK
    tests.test_census_v4_brain_web_readiness_gate + tests.test_research_brain_v4_operational_modes 47 tests OK
    tests.test_census_v4_brain_stage_promotion_gate 12 tests OK
    tests.test_census_v4_full_thesis_smoke_tasks 7 tests OK
    tests.test_census_v4_run_mode_honesty 18 tests OK
    tests.test_census_v4_brain_web_readiness_gate 14 tests OK
    P0-D targeted 4 tests OK
    P0-D/P0-E module suite 91 tests OK
    full unittest after P0-B official detail resolver patch:
      status = OK
      test_count = 5048
      failed_count = 0
      error_count = 0
      duration_seconds = 188.0978
      artifact = output/test_full_repo_0701/full_unittest_after_p0b_official_detail_resolver_artifact.json
      artifact_sha256 = 71f444f03cfe7f6ef0f5da5f8b285fa37ab51a611a15ce143ed7d3d1ad2a6a1a
      log_sha256 = 12b0088e9ddb22995994770e8d8cd5962c724ab141339b201d0f7a12f9521d2c
    latest full unittest after P0-D/P0-E:
      status = OK
      test_count = 5051
      failed_count = 0
      error_count = 0
      duration_seconds = 190.5442
      artifact = output/test_full_repo_0701/full_unittest_after_p0d_p0e_external_feedback_sourceclass_artifact.json
      log_sha256 = 4d31c61b2a03eb97ed1ef4b4cd189a4ab63742b841f3d11b98bd570802a045cc
  still_not_ready =
    v26 FULL_THESIS row is still 0
    v26 web_or_llm_accepted_claim_count is still 0
    v26 FULL_THESIS candidate scan split produces 1 candidate, but promotion is blocked by missing margin_bridge_visible
    KIND/DART detail resolver metadata is patched and unit-tested, but v24-v26 did not exercise an exact official URL web discovery route
```

쉬운 예:

```text
v21에서 Stage1/Stage2-Watch/Red가 보이는 85개는
"정식 E2R 100점 성적표"가 아니라 "일일 상태판에서 더 볼 후보"다.

네이버로 KIND 공시를 찾았으면 점수 근거는 네이버가 아니라 KIND다.
v20 패치는 이 source-class 오분류를 고쳤다.

하지만 KIND에서 가져온 본문이 상세 계약본문이 아니라
"최종 정정문서 확인 / 공시내용 기재 불충분" 안내문이면
margin bridge 점수를 주면 안 된다.

v21 패치는 여기서 한 번 더 보수화했다.
네이버로 찾은 일반 뉴스는 IndustryMedia로 분류될 수는 있어도,
trusted news connector/domain allowlist가 없으면 점수 증거로 쓰지 않는다.

그래서 source-class 버그는 고쳤지만 운영 FULL_THESIS Stage는 여전히 0개다.
```

이 아래 v17 기록은 이전 기준선으로 남긴다.

2026-07-02 이전 보조 진단 기준:

```text
previous Brain/Web diagnostic =
  output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v17

verdict = NOT_READY
BRAIN_WEB_PARTIAL row = 0
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
accepted web/news score claim = 0
brain_accepted_claim_count = 21
official_accepted_claim_count = 21
web_or_llm_accepted_claim_count = 0
web_search_tasks = 0
web_search_results = 0
web_fetched_documents = 0
web_rejected_documents = 0
llm_claim_extractor_attempt_count = 0
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 0
planner_runs = 21
source_task_executions = 13
brain_trace_missing_score_contribution_ref_count = 0
historical local targeted regression after v17 patches = Ran 76 tests / OK
historical local full unittest before later v10-v12 code patches = Ran 5027 tests in 209.1532s / OK
historical full unittest after v17 code patches = Ran 5036 tests in 202.213s / OK
full_unittest artifact status = OK
full_unittest artifact test_count = 5036
full_unittest artifact failed_count = 0
full_unittest artifact error_count = 0
full_unittest artifact duration_seconds = 204.0577
full_unittest artifact sha256 = 7fcf62f0a622f14ff91bdc6f26d2936e3b4e733844303b5c6dbae574ace06717
full_unittest log sha256 = 1ee5fc3667f9d438b933023e907e72010bc9d6c4f1872ba8c731becdcc6268b5
```

쉬운 예:

```text
웹 문서를 읽었고 LLM raw assertion도 만들었다.
v12에서는 웹/뉴스 claim 1개가 accepted까지 갔다.
하지만 그 1개는 source class/provider error와 score fan-out 문제가 있어 운영 점수로 신뢰하면 안 된다.
즉 "웹을 읽었다", "claim이 accepted됐다", "운영 점수 증거로 admissible하다"는 서로 다르다.
postextract-v1부터는 "왜 점수로 못 썼는지"가 web_rejected_documents에 문서 단위로 남는다.
metricsplit-v1부터는 official accepted와 web/LLM accepted가 gate에서 분리된다.
promotionguard-v1부터는 official-only claim이 BRAIN_WEB_PARTIAL row로 승격되지 않는다.
rawreject-v3부터는 rejected RAW assertion 단위로 primitive/target/temporal 중심의 탈락 사유가 남는다.
rawreject-v4부터는 claim별 raw rejection reason이 planner feedback retry context에 우선 반영된다.
promptleaf-v1부터는 PlannerRun prompt/response hash와 raw artifact path를 만들고
llm_prompts.jsonl / llm_responses.jsonl leaf를 export한다.
sourcefilter-v1부터는 종목 시세/프로필 페이지를 source document로 넘기지 않는다.
sourcequality-v1에서는 공식 DART claim 1개가 Brain trace까지 연결됐지만,
web/LLM accepted claim 0개라 strict promotion이 계속 막혔다.
sourcequality-v2에서는 일부 새 execution row에 source identity가 붙었지만,
기존 baseline/event-board execution 92개는 여전히 source_class/provider가 비어 있었다.
sourcequality-v3에서는 source_task_executions 99개의 source identity 누락이 0개로 줄었다.
다만 live Brain/Web accepted claim은 0개라 운영 승격은 계속 0개다.
sourcequality-v5에서는 공식 accepted claim 1개와 Brain trace 1개가 다시 생겼지만,
web/LLM accepted claim은 0개였다.
sourcequality-v6에서는 주요공시 라운드업, site archive, 중복 URL fetch를 더 강하게 막았다.
그 결과 web fetched document는 0개가 되었고, 좋은 web 원문 획득은 다음 P0로 남았다.
sourcequality-v7에서는 web full-source 9개와 LLM extractor 9회까지 진행됐다.
다만 56개 raw assertion이 target/directness 또는 primitive mapping에서 탈락했고,
accepted brain/web claim은 여전히 0개라 운영 승격은 계속 차단된다.
sourcequality-v8에서는 max_fetches_per_task와 source task count를 분리했다.
그 결과 대웅 003090 기준 source task 경로는 12개로 늘었지만,
web/LLM accepted claim은 여전히 0개라 운영 승격은 계속 차단된다.
sourcequality-v9에서는 candidate evidence-likelihood ordering과
accepted-claim-target 기반 continuation이 동작했다.
첫 실제 후보가 그린생명과학 공급계약 공시로 바뀌었고,
accepted target 미달 후 대웅 시설투자 정정까지 추가 시도했다.
Brain accepted official claim 2개와 StageCourt trace 1개가 생겼지만,
web/LLM accepted claim은 여전히 0개라 운영 승격은 계속 차단된다.
새 병목은 직접 공급계약 공시가 contract_quality 쪽이 아니라
C29 volume/mix/leverage primitive 쪽으로 오배정되는 router/planner compatibility 문제다.
sourcequality-v12에서는 직접 공급계약 공시가 C05로 route되는 것은 개선됐지만,
BRAIN_WEB_PARTIAL 1개가 source admissibility / score fan-out 버그로 생겼다.
sourcequality-v17에서는 이 가짜 승격이 다시 0개로 차단됐다.
동시에 공식 DART 계약 원문은 `contract_amount_to_prior_sales`,
`contract_duration_months`, `delivery_schedule` 3개 primitive로 구조화되지만,
`margin_bridge_visible`은 UNKNOWN으로 남아 병목/오판/밸류 점수로 퍼지지 않는다.
```

직접 답:

```text
Stage가 있는 애들은 있다.
Stage1/Stage2-Watch/Red event-board row는 있다.

하지만 운영 FULL_THESIS Stage가 있는 애들은 없다.
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0

v12의 BRAIN_WEB_PARTIAL row = 1은 운영 Stage가 아니며 폐기한다.
v17 기준 BRAIN_WEB_PARTIAL row = 0이고, FULL_THESIS row = 0이다.
```

쉬운 예:

```text
Stage0:
  "이번 census에서 현재 catalyst가 확인되지 않음"이라는 상태판이다.
  "E2R 100점 채점에서 나쁜 종목 0점"이라는 뜻이 아니다.

Stage1/Stage2:
  공식 이벤트나 단일 material claim 때문에 watch 상태로 올라온 row일 수 있다.
  C06/C08/C15 같은 전체 thesis Stage 확정과 섞으면 안 된다.
```

## 읽는 순서

최신 검토자는 아래 16개를 먼저 읽는다. 그 아래 긴 목록은 historical only다.

```text
1. census_v4_0701_sourcequality_v21_stage_existence_deep_audit_and_patch_direction_2026-07-02.md
2. census_v4_0701_sourcequality_v21_guardtight_stage_truth_and_next_patch_packet_2026-07-02.md
3. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/readiness_verdict.json
4. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/leaf_artifact_audit.json
5. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/census_stage_status.jsonl
6. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/brain_web_readiness_gate_audit.json
7. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/brain_stage_promotion_audit.json
8. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/full_thesis_production_audit.json
9. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/full_thesis_production_runner_audit.json
10. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/stagecourt_traces.jsonl
11. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/accepted_claims.jsonl
12. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/source_task_executions.jsonl
13. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/web_fetched_documents.jsonl
14. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/raw_assertion_rejections.jsonl
15. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/goal_completion_audit.json
16. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/goal_requirement_matrix_audit.json
```

Historical only:

```text
1. census_v4_0701_sourcequality_v17_patch_result_stage_truth_and_next_agent_attack_packet_2026-07-02.md
2. census_v4_0701_sourcequality_v12_stage_truth_hard_cross_review_and_next_patch_direction_2026-07-02.md
3. census_v4_0701_sourcequality_v9_candidate_order_continuation_patch_result_and_next_router_bottleneck_2026-07-02.md
3. census_v4_0701_sourcequality_v8_deep_cross_validation_and_v9_patch_direction_2026-07-02.md
4. census_v4_0701_sourcequality_v8_task_budget_split_live_result_and_next_bottleneck_2026-07-02.md
5. census_v4_0701_sourcequality_v7_feedback_retry_live_result_and_next_bottleneck_2026-07-02.md
6. census_v4_0701_sourcequality_v6_hard_review_and_p0_patch_direction_2026-07-02.md
7. census_v4_0701_sourcequality_v6_source_router_patch_result_2026-07-02.md
8. census_v4_0701_stage_presence_sourcequality_v3_final_review_packet_2026-07-02.md
9. census_v4_0701_sourcequality_live_diagnostic_cross_validation_and_next_patch_direction_2026-07-02.md
10. census_v4_0701_sourcefilter_promptleaf_live_diagnostic_2026-07-02.md
11. census_v4_0701_raw_assertion_rejection_audit_patch_and_stage_truth_2026-07-02.md
12. census_v4_0701_brain_web_promotion_guard_patch_result_2026-07-02.md
13. census_v4_0701_next_agent_hard_review_after_metricsplit_2026-07-02.md
14. census_v4_0701_brain_web_metric_split_patch_result_2026-07-02.md
15. census_v4_0701_postextract_web_rejection_patch_result_2026-07-02.md
16. census_v4_0701_feedback_v1_hard_cross_review_and_next_patch_packet_2026-07-02.md
17. census_v4_0701_stage_scope_current_truth_and_next_patch_attack_packet_2026-07-02.md
18. census_v4_0701_c28_source_backed_replay_final_cross_review_packet_2026-07-02.md
19. census_v4_0701_stage_existence_c24_patch_cross_review_packet_2026-07-02.md
20. census_v4_0701_latest_c17_source_backed_replay_stage_truth_and_review_packet_2026-07-02.md
21. census_v4_0701_stage_existence_vs_operational_stage_deep_cross_review_2026-07-02.md
22. census_v4_0701_latest_c15_source_backed_replay_patch_and_stage_truth_2026-07-02.md
23. census_v4_0701_operational_stage_truth_deep_audit_and_next_patch_direction_2026-07-02.md
24. census_v4_0701_latest_c08_source_backed_replay_patch_and_stage_truth_2026-07-02.md
25. census_v4_0701_operational_stage_reality_cross_validation_and_patch_direction_2026-07-02.md
26. census_v4_0701_latest_c06_source_backed_replay_stage_truth_and_next_patch_packet_2026-07-02.md
26. output/census_v4/2026-07-01/goal_requirement_matrix_audit.json
27. output/census_v4/2026-07-01/c28_source_backed_semantic_replay.json
28. output/census_v4/2026-07-01/c24_source_backed_semantic_replay.json
29. output/census_v4/2026-07-01/c17_source_backed_semantic_replay.json
30. output/census_v4/2026-07-01/c15_source_backed_semantic_replay.json
31. output/census_v4/2026-07-01/c08_source_backed_semantic_replay.json
32. output/census_v4/2026-07-01/c06_source_backed_semantic_replay.json
33. output/census_v4/2026-07-01/c06_guard_replay_audit.json
34. output/census_v4/2026-07-01/all_archetype_replay_matrix.json
35. output/census_v4/2026-07-01/controlled_semantic_replay_audit.json
37. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v17/census_stage_status.jsonl
38. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v17/census_stage_summary.json
39. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v17/brain_web_readiness_gate_audit.json
40. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v17/brain_stage_promotion_audit.json
41. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v17/accepted_claims.jsonl
42. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v17/brain_to_claim_trace.jsonl
43. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v17/primitive_states.jsonl
44. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v17/score_contributions.jsonl
45. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v17/stagecourt_traces.jsonl
46. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v12/accepted_claims.jsonl
47. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v12/score_contributions.jsonl
48. output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v12/stagecourt_traces.jsonl
49. output/test_full_repo_0701/full_unittest_result_artifact.json
```

주의:

```text
이 폴더의 다른 문서들은 작업 중간 스냅샷이다.
예전 문서에 test_count=4942/4951/4954/4957/4959/4975/4983/4992 같은 값이 있으면
그 문서 작성 시점의 과거 값으로 읽는다.

최신 기준은 이 README 상단과 v21 최신 문서, 그리고
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21/*.json이다.
Brain/Web enabled 경로의 최신 보조 진단은
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v21 이다.

`schema-v2`는 Codex extractor schema failure가 해결됐음을 보여 주는 직전 진단이다.
`feedback-v1`은 accepted claim 2건이 모두 OpenDART였고 web rejection ledger가 비어 있던 직전 진단이다.
`postextract-v1`은 web rejection ledger가 생긴 진단이다.
`metricsplit-v1`은 official accepted와 web/LLM accepted metric이 분리된 진단이다.
`promotionguard-v1`은 official-only BRAIN_WEB_PARTIAL 승격이 막힌 진단이다.
`rawreject-v4`은 raw assertion rejection feedback이 붙은 직전 진단이다.
`promptleaf-v1`은 prompt/response leaf가 실제 live 진단에서 생성됨을 보인 진단이다.
`sourcefilter-v1`은 종목 시세/프로필 페이지 source filter 직전 최신 Brain/Web readiness 숫자를 담은 진단이다.
`sourcequality-v1`은 source-quality 필터 테스트 반영 후 공식 claim 1개가 Brain trace까지 연결됐지만
web/LLM claim 0개라 promotion이 계속 차단됨을 보인 중간 진단이다.
`sourcequality-v2`는 새 Brain execution 일부에 source identity가 붙었지만 기존 병합 row 92개 identity 누락이 남은 중간 진단이다.
`sourcequality-v3`는 병합된 source_task_executions까지 identity backfill이 적용된 최신 진단이다.
v3 기준 live Brain/Web accepted claim은 0개이므로 운영 승격은 0개다.
`sourcequality-v6`는 주요공시 라운드업, site archive, 중복 URL fetch를 막은 직전 진단이다.
v6 기준 official accepted claim은 1개지만 web/LLM accepted claim은 0개이고 운영 승격은 여전히 0개다.
`sourcequality-v7`은 web full-source fetch와 LLM claim extraction이 실제로 실행된 최신 진단이다.
v7 기준 web full-source 9개와 extractor 9회가 남았지만 accepted brain/web claim은 0개이고 운영 승격은 여전히 0개다.
`sourcequality-v8`은 source task count와 max_fetches_per_task를 분리한 진단이다.
v8 기준 source task 경로 보존은 개선됐지만 accepted brain/web claim은 0개이고 운영 승격은 여전히 0개다.
`sourcequality-v9`는 candidate evidence-likelihood ordering과 accepted-claim-target continuation을 붙인 진단이다.
v9 기준 Brain accepted official claim 2개와 StageCourt trace 1개가 생겼지만,
web/LLM accepted claim은 0개이고 운영 승격은 0개였다.
`sourcequality-v12`는 직접 공급계약 공시가 C05로 route되는 것은 개선됐지만,
Naver web NEWS claim이 source class/provider error를 가진 채 accepted되고
margin_bridge_visible 하나가 여러 score contribution으로 퍼지는 새 P0 문제를 드러낸 중간 진단이다.
v12 기준에도 FULL_THESIS 운영 Stage는 0개다.
`sourcequality-v17`는 v12의 가짜 BRAIN_WEB_PARTIAL 승격을 다시 차단했고,
공식 DART 계약 claim은 계약금액/기간/납품일정 visibility로만 남긴 중간 진단이다.
v17 기준에도 FULL_THESIS 운영 Stage는 0개다.
`sourcequality-v20`는 Naver-discovered KIND URL source-class를 KIND로 정정했지만,
NEWS full source까지 너무 넓게 열 수 있다는 교차검증 지적이 있었다.
`sourcequality-v21`는 official hostname exact allowlist와 NEWS score-block을 다시 적용한 최신 진단이다.
v21 기준에도 FULL_THESIS 운영 Stage는 0개다.
```

숫자 해석 주의:

```text
all_archetype_replay_matrix.json의 total row는 36개다.
C01~C32 required archetype은 32개이고,
R13_* cross-archetype guard contract row가 4개 별도로 있다.

따라서 missing_required_archetype_count=26과
R13까지 포함한 non-ready row 30개는 모순이 아니다.
```

## Canonical Baseline 단일 진실

주의:

```text
이 섹션은 output/census_v4/2026-07-01 canonical baseline 기준이다.
Brain/Web sourcequality-v21 보조 진단과 별도다.
최신 Brain/Web 해석은 이 README 상단과
census_v4_0701_sourcequality_v21_guardtight_stage_truth_and_next_patch_packet_2026-07-02.md를 우선한다.
```

작성 기준:

```text
as_of_date = 2026-07-01
canonical output = output/census_v4/2026-07-01
latest source-backed replay patch = C28
```

### Stage / Score

```text
census_stage_status rows = 3391

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391
  FULL_THESIS = 0

score_scope_distribution:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

base_stage_display_distribution:
  EVENT_BOARD_STAGE0 = 3306
  EVENT_BOARD_STAGE1 = 54
  EVENT_BOARD_STAGE2_WATCH = 30
  EVENT_BOARD_RED = 1

canonical_stage_distribution:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

verified_score_present = 0
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0

operator warning:
  stage_scope_notice = NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST
  operational_stage_use_allowed = false
  event_board_non_stage0_count = 85
  event_board_stage_rows_are_operational_full_thesis = false
```

해석:

```text
Stage label은 있다.
하지만 전부 Census 상태판 범위다.
운영 full thesis 채점지는 아직 없다.
```

### Historical Brain/Web Diagnostic: sourcequality-v9

주의:

```text
이 섹션은 sourcequality-v17 이전 단계인 v9 기록이다.
최신 Brain/Web 보조 진단은 sourcequality-v21이다.
v9는 candidate ordering / continuation 병목을 설명하는 historical baseline으로만 읽는다.
```

v9 보조 진단:

```text
output_root = output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v9
run_mode = BRAIN_AND_WEB_ACQUISITION_ENABLED
brain_web_mode = enabled
target_gate = brain_web
verdict = NOT_READY
```

결과:

```text
stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391
  BRAIN_WEB_PARTIAL = 0
  FULL_THESIS = 0

operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE = 3391

score_scope_distribution:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

Brain/Web:
  planner_run_row_count = 22
  planner_prompt_response_leaf_count = 2
  real_provider_success_count = 3
  current_attempt_source_task_execution_count = 21
  llm_claim_extractor_attempt_count = 3
  llm_claim_extractor_real_provider_count = 3
  llm_claim_extractor_success_count = 3
  llm_claim_extractor_provider_error_count = 0
  web_search_task_count = 10
  web_search_call_count = 10
  web_search_result_count = 66
  web_fetched_document_count = 3
  web_rejected_document_count = 53
  raw_assertion_rejections = 36
  llm_prompts_jsonl_rows = 2
  llm_responses_jsonl_rows = 2
  brain_accepted_claim_count = 2
  official_accepted_claim_count = 2
  web_or_llm_accepted_claim_count = 0
  brain_stage_trace_count = 1
  brain_promoted_stage_row_count = 0
  source_task_execution_count = 113
  source_task_identity_missing_count = 0
```

Prompt/response audit patch:

```text
PlannerRunV4 now carries:
  planner_run_id
  prompt_hash
  response_hash
  raw_prompt_path
  raw_response_path

Census export now writes:
  llm_prompts.jsonl
  llm_responses.jsonl
  planner_raw/prompts/*.json
  planner_raw/responses/*.json
```

직전 스냅샷 주의:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-rawreject-v4 자체는
promptleaf-v1 패치 전에 생성된 live diagnostic이라 llm_prompts/llm_responses가 0행이다.

sourcefilter-v1에서는 llm_prompts/llm_responses가 각각 2행이고
planner_raw/prompts/*.json, planner_raw/responses/*.json도 각각 2개다.

sourcequality-v1에서는 llm_prompts/llm_responses가 각각 3행이고
planner_raw/prompts/*.json, planner_raw/responses/*.json도 각각 3개다.
공식 DART claim 1개가 Brain StageCourt trace까지 연결됐지만,
web_or_llm_accepted_claim_count=0이라 대표 Stage 승격은 계속 차단됐다.

sourcequality-v3에서는 llm_prompts/llm_responses가 각각 2행이고
claim_extractor_runs는 6행, raw_assertions는 113행, rejected raw assertion은 30행이다.
source_task_executions 99개는 모두 source_class/provider/source_task_origin/requested_source_classes를 갖는다.
하지만 Brain/Web accepted claim은 0개라 대표 Stage 승격은 여전히 0개다.

sourcequality-v6에서는 llm_prompts/llm_responses가 각각 1행이고
web result 11개가 전부 metadata 단계에서 거절되어 claim_extractor_runs는 0행이다.
공식 accepted claim 1개와 Brain StageCourt trace 1개는 있지만,
web/LLM accepted claim은 0개라 대표 Stage 승격은 여전히 0개다.

sourcequality-v7에서는 llm_prompts/llm_responses가 각각 2행이고
web full-source 9개가 fetch되어 claim_extractor_runs는 9행이다.
하지만 raw assertion 56개가 target/directness 또는 primitive mapping에서 전부 탈락했고,
web/LLM accepted claim은 0개라 대표 Stage 승격은 여전히 0개다.

sourcequality-v8에서는 max_source_tasks_per_plan과 max_fetches_per_task를 분리했다.
source_task_executions는 104행이고, 대웅 003090의 current attempt source task는 12개로 늘었다.
다만 web full-source fetch는 2개, claim_extractor_runs는 2행이고,
raw assertion 23개가 target/directness 또는 primitive mapping에서 전부 탈락했다.
web/LLM accepted claim은 0개라 대표 Stage 승격은 여전히 0개다.

sourcequality-v9에서는 candidate evidence-likelihood ordering과
accepted-claim-target 기반 continuation이 동작했다.
첫 실제 후보는 그린생명과학 114450의 `[기재정정]단일판매ㆍ공급계약체결`이었고,
accepted target 미달 후 대웅 003090의 `[기재정정]신규시설투자등`까지 추가 시도했다.
source_task_executions는 113행이고, current attempt source task는 21행이다.
Brain accepted official claim 2개, score contribution 5개, StageCourt trace 1개가 생겼지만
web/LLM accepted claim은 0개라 대표 Stage 승격은 여전히 0개다.
핵심 새 병목은 그린생명과학 공급계약 공시 원문에서 계약금액/상대방/매출대비 41.18%가 보였는데도
planner가 contract-compatible primitive가 아니라 volume_growth_visible/cash_or_revision_conversion 쪽으로 열어
mapping에서 탈락했다는 점이다.
```

추가로 다음 감사 카운터가 생기거나 유지되어야 한다.

```text
assessment_event_used_as_score_evidence_count = 0
event_without_accepted_claim_nonzero_score_count = 0
score_contribution_without_accepted_claim_support_count = 0
```

이 숫자는 "event는 조사 문, claim은 점수 열쇠"라는 원칙을 기계적으로 지키기 위한 것이다.

중요한 해석:

```text
Codex LLM planner는 호출된다.
sourcequality-v9 기준 planner_runs.jsonl 장부는 22행이고,
raw prompt/response leaf는 2쌍이다.
web full-source 3개가 fetch되어 claim_extractor_runs도 3행이다.

따라서 이제 "LLM이 아예 못 읽었다"가 아니다.
읽은 뒤에 target/directness 또는 primitive mapping에서 전부 탈락했다.
web_or_llm_accepted_claim_count는 여전히 0건이다.
raw_assertion_rejections에는 primitive/target/temporal/anchor 탈락 사유가 남는다.
official-only claim은 더 이상 BRAIN_WEB_PARTIAL row로 승격되지 않는다.

따라서 "Brain/Web이 완전히 됐다"가 아니라
"Brain/Web이 원문 fetch와 LLM extraction까지 일부 도달했지만, accepted claim과 운영 full thesis cutover는 아직 막혀 있다"가 맞다.
```

planner count 주의:

```text
planner_run_row_count = 22는 planner_runs.jsonl 장부 행 수다.
sourcequality-v9에서 prompt/response leaf가 있는 planner call은 2개다.
brain_planner_audit 기준 real provider success count는 3개다.
나머지는 planner_not_attempted_after_real_planner_limit 또는 non-real attempt row로 읽어야 한다.
```

쉬운 예:

```text
출석부에는 22명이 적혀 있다.
하지만 실제로 raw prompt/response가 남은 발표자는 2명이고,
성공으로 집계된 real provider call은 2명이다.
```

쉬운 예:

```text
전에는 시험지가 인쇄도 안 됐다.
  -> Codex output schema 오류로 extractor 400 실패.

이제 시험지는 인쇄됐고 일부 답안도 읽었다.
  -> sourcequality-v9 기준 LLM planner prompt/response leaf 2쌍이 남음.
  -> 웹 full-source 3개가 fetch됨.
  -> claim extractor는 3회 실행됨.
  -> 하지만 web/LLM accepted claim은 0개임.
  -> 직접 공급계약 공시는 계약 primitive가 아니라 volume/mix/leverage primitive로 열려 탈락함.

하지만 채점표에 들어간 웹/뉴스 답은 아직 없다.
  -> 읽은 문장이 운영 점수 primitive로 accepted claim까지 닫히지 않았음.
```

### C06 Source-Backed Replay

```text
positive_replay_pass = true
guard_replay_pass = true
accepted_primitive_ids = ["customer_preorder_or_allocation"]
accepted_claim_count = 1
document_url = https://ssl.pstatic.net/imgstock/upload/research/company/sk_hynix_memory_20240401.pdf
replay_only = true
production_score_evidence_allowed = false
```

의미:

```text
C06은 실제 SK하이닉스 PDF 문장에서 source-backed positive primitive를 뽑는 경로와 guard replay가 통과했다.
이것은 C06 전체 운영 Green 판정이 아니라 replay 검증이다.
```

### C08 Source-Backed Replay

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
document_url = https://ssl.pstatic.net/imgstock/upload/research/company/1704669223541.pdf
replay_only = true
production_score_evidence_allowed = false
score_contribution_count = 0
```

의미:

```text
QRT 원문 PDF 조각에서 C08 positive bridge 두 개를 뽑았다.
profile-only guard는 named customer / qualification / margin bridge로 새지 않았다.
```

쉬운 예:

```text
"반도체 신뢰성 평가 회사다"
  -> socket_or_test_demand_visible 가능

"리벨리온과 AI 반도체 신뢰성 평가 MOU"
  -> named_customer_quality 가능

"Capacitor 품질 신뢰성 평가"
  -> Capacitor 안의 capa를 CAPA/capacity로 오해하면 안 됨
```

### C15 Source-Backed Replay

```text
positive_replay_pass = true
guard_replay_pass = true
accepted_claim_count = 6

positive_accepted_primitive_ids:
  fcf_quality_score
  pricing_power_confirmed
  spread_expansion

guard_accepted_primitive_ids = []
raw_commodity_guard_leaked_primitives = []
document_urls:
  https://en.yna.co.kr/view/AEN20210427007052320
  https://www.posco.co.kr/homepage/servlet/FileDownLoad?fileCategory=irDataFd&fileNum=407
  https://www.businesskorea.co.kr/news/articleView.html?idxno=60900
replay_only = true
production_score_evidence_allowed = false
```

의미:

```text
제품 판가/원재료/영업이익 bridge가 있는 Hyundai Steel/POSCO source는 C15 positive primitive를 열었다.
raw copper-price headline guard는 C15 점수 primitive로 새지 않았다.
```

### C17 Source-Backed Replay

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
document_urls:
  https://www.s-oil.com/common/page/FileDownload.aspx?FileName=638977732335971792.pdf&PIndex=4&PathType=BOARD&TFileName=3Q+2025+S-OIL+Earnings+Release.pdf
  https://www.s-oil.com/common/page/FileDownload.aspx?FileName=638917284006185071.pdf&PIndex=4&PathType=BOARD&TFileName=2Q25++Earnings+Release+FN.pdf
replay_only = true
production_score_evidence_allowed = false
```

의미:

```text
S-OIL Q3 2025 IR excerpt는 spread + realized OPM bridge + utilization을 열었다.
S-OIL Q2 2025 IR excerpt는 spread recovery가 있어도 inventory/lagging 영향으로 영업손실이면 realized margin positive로 새지 않는 guard를 통과했다.
```

### C24 Source-Backed Replay

```text
positive_replay_pass = true
guard_replay_pass = true
accepted_claim_count = 5

positive_support_primitive_ids:
  trial_quality_visible

guard_counter_primitive_ids:
  binary_event_unresolved

binary_event_guard_leaked_support_primitives = []
document_urls:
  https://www.prnewswire.com/news-releases/hanall-biopharma-reports-full-year-2023-financial-results-and-provides-business-update-302095695.html
  https://www.prnewswire.com/news-releases/sillajen-announces-conclusions-from-interim-futility-analysis-of-phase-3-phocus-trial-in-hcc-300895539.html
replay_only = true
production_score_evidence_allowed = false
```

의미:

```text
HanAll/Immunovant batoclimab press release excerpt는 Phase 2 response/safety 문맥으로 trial_quality_visible을 열었다.
SillaJen PHOCUS futility/discontinuation excerpt는 binary event guard로 읽히며 trial_quality_visible positive support로 새지 않았다.
```

쉬운 예:

```text
"Phase 2에서 response와 safety가 확인됐다"
  -> C24 trial_quality_visible replay positive 가능

"IDMC가 futility로 Phase 3 중단을 권고했다"
  -> C24 binary_event_unresolved/risk guard
  -> 이것을 trial_quality_visible positive로 쓰면 안 됨
```

### C28 Source-Backed Replay

```text
positive_replay_pass = true
guard_replay_pass = true
accepted_claim_count = 7

positive_support_primitive_ids:
  arr_growth_visible
  nrr
  retention_or_renewal
  rpo_to_sales
  recurring_margin_leverage

guard_support_primitive_ids = []
guard_accepted_claim_ids = []
keyword_only_guard_leaked_support_primitives = []
document_urls:
  https://www.sec.gov/Archives/edgar/data/1535527/000153552725000009/crwd-20250131.htm
  https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-announces-falcon-next-gen-siem-isv-ecosystem-open
replay_only = true
production_score_evidence_allowed = false
```

의미:

```text
CrowdStrike Form 10-K excerpt는 ARR/NRR/renewal/deferred revenue/subscription margin primitive를 모두 열었다.
CrowdStrike SIEM product press release는 보안 제품 키워드만 있으므로 retention/RPO/margin primitive로 새지 않았다.
```

쉬운 예:

```text
"ARR 23% 증가, net retention 112%, deferred revenue $3.7B"
  -> C28 recurring economics replay positive 가능

"AI-native SOC, SIEM ecosystem, security teams can retain data"
  -> 제품/보안 설명
  -> customer retention 또는 ARR 증거로 쓰면 안 됨
```

### All-Archetype Replay Matrix

```text
all_archetype_replay_pass = false
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 6
guard_replay_ready_count = 6
missing_required_archetype_count = 26
controlled_wiring_smoke_ready_count = 0

READY:
  C06_HBM_MEMORY_CUSTOMER_CAPACITY
  C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
  C15_MATERIAL_SPREAD_SUPERCYCLE
  C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  C24_BIO_TRIAL_DATA_EVENT_RISK
  C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

주의:

```text
canonical output은 full_thesis_smoke_mode 없이 생성되어 controlled_wiring_smoke_ready_count = 0이다.
unit test helper는 controlled_replay mode에서 C06 smoke fixture를 별도로 켜므로 1로 보일 수 있다.
둘 다 운영 full-thesis pass가 아니다.
```

### Controlled Semantic Replay

```text
controlled_semantic_replay_pass = true
case_count = 10
pass_count = 10
pending_count = 0
fail_count = 0

PASS:
  C06_HBM_POSITIVE_AND_QUALIFICATION_LAG_GUARD
  C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD
  C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD
  C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
  C24_CLINICAL_BINARY_EVENT_GUARD
  C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
  WRONG_SUBJECT_RISK_FIXTURE
  OLD_RISK_RESOLVED_FIXTURE
  PROVIDER_FAILURE_PENDING_FIXTURE
  SEMANTIC_CONTRACT_GUARD_FIXTURE
```

### Goal Matrix

```text
goal_completion_minimum_pass = false
required_goal_completion_count = 17
required_goal_completion_pass_count = 13
required_goal_completion_pending_count = 4
required_goal_completion_fail_count = 0

pending_gate_ids:
  FULL_THESIS_SMOKE_PASS
  FULL_THESIS_PRODUCTION_PASS
  BRAIN_WEB_EVIDENCE_PASS
  ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
```

## 검증 기록

최신 C28 반영 후:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_all_archetype_replay_matrix \
  tests.test_census_v4_goal_required_audits -v

Ran 13 tests
OK
```

Census v4 tests:

```text
PYTHONPATH=src python -m unittest $(rg --files tests | rg 'tests/test_census_v4_.*\.py$' | sed 's#/#.#g; s#\.py$##') -v

Ran 120 tests
OK
```

Historical full repo test artifact before source-class guard-tight patch:

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v

status = OK
test_count = 5036
failed_count = 0
error_count = 0
duration_seconds = 204.0577
test_result_artifact_file_sha256 = 7fcf62f0a622f14ff91bdc6f26d2936e3b4e733844303b5c6dbae574ace06717
json_internal_log_sha256 = 1ee5fc3667f9d438b933023e907e72010bc9d6c4f1872ba8c731becdcc6268b5
```

주의:

```text
최신 full unittest 증거는
output/test_full_repo_0701/full_unittest_after_sourceclass_v21_guardtight_artifact.json이다.
아래 full_unittest_result_artifact.json은 v17 계열 historical artifact다.

rawreject-v4 diagnostic output 안의
output/census_v4/2026-07-01-brain-web-diagnostic-rawreject-v4/test_result_artifact.json은
진단 실행 당시 복사된 이전 성적표라 test_count=4997이다.

따라서 rawreject-v4 readiness 산출물은 "진단 당시 스냅샷"으로 읽고,
최신 repo full-test 통과 증거는 v21 guard-tight artifact의 5042 OK로 읽어야 한다.
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
1. FULL_THESIS smoke/prod source task execution

2. Real Brain/Web evidence gate

3. 남은 26개 required archetype의 source-backed positive + guard replay 확장
```

주의:

```text
가중치나 Stage threshold를 먼저 고치면 안 된다.
먼저 "원문 -> anchor -> claim -> primitive -> score contribution" 경로가 전 아키타입에서 닫히는지 확인해야 한다.
```

## 다음 에이전트 공격 질문

완료라고 주장하면 아래를 먼저 확인한다.

```text
1. FULL_THESIS row가 생겼는가? 현재 0개다.
2. FULL_E2R_100 verified score row가 생겼는가? 현재 0개다.
3. Brain/Web/LLM planner call이 canonical output에서 실제 evidence로 이어졌는가?
4. C28 controlled semantic replay가 source-backed로 닫혔는가?
5. required 32개 아키타입이 모두 source-backed positive + guard ready인가? 현재 6/32다.
6. C08 replay가 production score로 새지 않았는가? score_contribution_count는 0이어야 한다.
7. profile-only guard가 named customer / qualification / margin bridge로 새지 않았는가?
8. `Capacitor`가 CAPA/capacity로 오분류되지 않는가?
9. output root의 test_result_artifact.json과 외부 full test artifact가 같은가?
10. 과거 문서의 stale test_count나 stale ready_count를 최신 값으로 오해하지 않았는가?
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

C24 source-backed replay:
  PASS

CONTROLLED_SEMANTIC_REPLAY_PASS:
  PASS, 10/10 pass

ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS:
  FALSE, 6/32 ready

MEANINGFUL_OPERATIONAL_STAGE_PASS:
  FALSE

FULL_THESIS_PRODUCTION_PASS:
  FALSE

BRAIN_WEB_EVIDENCE_PASS:
  FALSE

Goal completion:
  FALSE
```

## 2026-07-03 v54 Stage Existence And Brain/Web Blocker Cross Audit

최신 교차검증 문서:

```text
docs/0701/census_v4_0701_v54_stage_existence_and_brainweb_blocker_cross_audit_2026-07-03.md
```

핵심 결론:

```text
Stage가 아예 없는 것은 아니다.

canonical:
  non-Stage0 상태판 Stage = 85
  운영 FULL_THESIS Stage = 0
  FULL_E2R_100 verified score = 0

controlled smoke:
  삼성전자 Stage2-Watch / 72.0
  SK하이닉스 Stage3-Yellow / 88.0
  단 operator use = SMOKE_ONLY_STAGE_NOT_PRODUCTION

Brain/Web enabled diagnostic:
  planner/source/LLM extractor 일부 실행
  web_or_llm_accepted_claim_count = 0
  production FULL_THESIS row = 0

전 아키타입 replay:
  6/32 source-backed ready
  26/32 source gap pending
```

다음 패치 방향:

```text
1. full-thesis seed 85개를 실제 Research Brain input으로 소비한다.
2. C05 margin_bridge_visible 같은 source-quality gap을 official-first로 닫는다.
3. controlled smoke와 production operator alias 분리를 유지한다.
4. 26개 pending 아키타입의 source-backed positive + guard replay를 확장한다.
```

## 2026-07-03 v55 Full-Thesis Seed Selection Priority Patch

최신 패치 문서:

```text
docs/0701/census_v4_0701_v55_full_thesis_seed_selection_priority_patch_2026-07-03.md
```

핵심 변경:

```text
src/e2r/research_brain/v4_production_orchestrator.py
  _select_unique_candidate_events()

변경 전:
  CensusFullThesisQueue seed 1개만 family-diversity로 먼저 선택되고,
  나머지 seed는 CompanyGuide/Report/DART/IR/KRX 뒤로 밀릴 수 있었다.

변경 후:
  CensusFullThesisQueue seed를 selection budget 앞쪽에서 먼저 소비한다.
```

검증:

```text
tests.test_research_brain_v4_operational_modes:
  Ran 49 tests OK

tests.test_census_v4_full_thesis_smoke_tasks:
  Ran 11 tests OK
```

v55 diagnostic:

```text
output/census_v4/2026-07-01-seed-priority-v55

planner rows = 21
planner row 0~20 source_family = CensusFullThesisQueue

full_thesis_seed_event_count = 85
full_thesis_seed_planner_attempted_event_count = 21
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 21
PLANNER_NOT_RUN = 64
```

주의:

```text
provider none 실행이라 NOT_READY가 맞다.
이번 패치는 seed를 Research Brain 입구로 먼저 보내는 패치다.
production FULL_THESIS row는 아직 0개다.
```

## 2026-07-03 v56 Full-Thesis Seed Context / Stage Truth Cross-Validation

최신 교차검증 문서:

```text
docs/0701/census_v4_0701_v56_full_thesis_seed_context_and_stage_truth_cross_validation_2026-07-03.md
```

핵심 답:

```text
Stage row는 있다.
하지만 운영 FULL_THESIS Stage는 아직 없다.

상태판 Stage:
  CENSUS_EVENT_BOARD = 3391
  non-Stage0 = 85

운영 Stage:
  FULL_THESIS row = 0
  FULL_E2R_100 verified score row = 0
```

v56 패치:

```text
full-thesis seed에 이전 상태판 source context를 추가했다.

추가 context:
  source_primary_archetype
  source_secondary_archetypes
  source_large_sector_id
  source_score_contribution_ids
  source_missing_primitives
  source_material_gap_ids
  source_failed_stage_gates

안전장치:
  target_archetype = None
  target_archetype_status = BRAIN_HYPOTHESIS_REQUIRED
  score_evidence_allowed = False
  stage_promotion_allowed_before_execution = False
```

쉬운 예:

```text
이전 상태판에 "메모리/HBM 맥락, cash bridge gap"이 있었다고 planner에게 알려준다.
하지만 "이 종목은 C06이다"라고 확정하지 않는다.
점수와 Stage는 accepted claim과 StageCourt trace가 생긴 뒤에만 가능하다.
```

v56 diagnostic:

```text
output/census_v4/2026-07-01-seed-context-v56

run result = NOT_READY
full_thesis_seed_event_count = 85
full_thesis_seed_planner_attempted_event_count = 21
llm_real_provider_success_count = 0
source_task_execution_count = 0
brain_accepted_claim_count = 0
brain_promoted_stage_row_count = 0

materialization_status:
  PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 21
  PLANNER_NOT_RUN = 64

target_archetype:
  None = 85
```

검증:

```text
targeted:
  tests.test_census_v4_full_thesis_smoke_tasks
  Ran 11 tests OK

targeted:
  tests.test_research_brain_v4_operational_modes
  Ran 50 tests OK

full suite:
  PYTHONPATH=src python -m unittest discover -s tests -v
  Ran 5079 tests in 203.141s
  OK
```

다음 패치 방향:

```text
1. real provider success가 있는 run에서 seed context가 raw prompt에 들어가는지 증명한다.
2. planner가 bounded official-first SourceTask를 만들게 한다.
3. source-backed accepted claim이 생기기 전에는 Stage promotion 금지 상태를 유지한다.
4. accepted claim -> primitive -> score contribution -> StageCourt trace가 닫힌 뒤에만 FULL_THESIS row를 만든다.
```

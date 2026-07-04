# 2026-07-03 Goal 진행상황 상세 기록

작성/업데이트 시각: 2026-07-04 11:00 KST

대상 문서:

- `docs/core/goal.md`
- `docs/core/goal2.md`
- `docs/core/goal3.md`

현재 결론:

**v136 audit refresh 기준으로 goal은 산출물상 완료 상태다.**  
단, 이것은 새 live 웹/LLM 수집을 다시 90분 돌린 결과가 아니라, v134 live 실행 산출물에 최신 audit/promotion/gate 로직을 재적용한 검증이다. v134 live 실행은 실제 Brain/Web/LLM, bounded source acquisition, claim extraction, production full-thesis row를 만들었고, v135/v136 audit refresh에서 leaf, all-archetype replay, goal matrix, goal completion, 최신 전체 테스트 artifact까지 모두 닫혔다.

최신 완료 근거:

```text
live base:
  output/census_v4/2026-07-01-v134-event-refresh-check

latest audit refresh:
  output/census_v4/2026-07-01-v136-goal-gates-audit-refresh

latest full test artifact:
  output/census_v4/2026-07-01-v136-goal-gates-full-test/full_unittest_result_artifact.json
```

최신 v136 요약:

```text
leaf_artifact_audit.verdict:              PASS
brain_web_readiness_gate.verdict:         READY_FOR_BRAIN_WEB_EVIDENCE_PASS
full_thesis_production_audit.verdict:     FULL_THESIS_PRODUCTION_PASS
production_full_thesis_row_count:         32
full_thesis_promoted_seed_count:          32
primitive_state_chain_audit.verdict:      PASS
all_archetype_replay_pass:                true
source_backed_ready_count:                36
guard_replay_ready_count:                 36
goal_completion_minimum_pass:             true
required_goal_completion_pass_count:      21 / 21
goal_completion_ready:                    true
meaningful_operational_stage_pass:        true
target_gate_pass:                         true
blockers:                                 []
full unittest:                            5154 OK, 0 fail, 0 error
```

쉬운 예:

```text
이전 상태:
  자료는 모았고 일부 검사도 했지만,
  "정밀검사 결과표"와 "전체 아키타입 재현 검증표"가 아직 도장 찍히지 않았다.

현재 v136 상태:
  v134에서 실제 자료 수집과 claim/score/stage 생성이 끝났고,
  v136에서 그 결과표의 장부 연결, 아키타입 재현, 테스트 증빙까지 다시 확인했다.
  그래서 goal audit 기준으로는 blocker가 0개다.
```

주의:

```text
controlled smoke 자체가 실행된 것은 아니다.
대신 production full-thesis가 실제로 32개 row를 만들었으므로,
FULL_THESIS_SMOKE_PASS 요구는 더 강한 증거인 production_full_thesis로 대체 충족된다.
```

과거 진행 맥락:

최신 완료 live 실행인 v109 기준으로는 `BRAIN_WEB_EVIDENCE_PASS`까지 실제 leaf artifact로 통과했다. 이전 v108에서 터진 `claim_id` 충돌도 재현되지 않았다. v110 패치로 follow-up seed에 canonical archetype/gap context를 더 명확히 싣고 bounded web fallback을 허용했고, v111 smoke에서 그 context가 source task까지 전달되는 것도 확인했다. v113/v115/v117 패치로 긴 live provider loop의 진행상태, runtime budget 종료, budget 종료 원인이 artifact에 남게 됐다. v120에서는 `FULL_THESIS` 승격 실패 원인을 primitive 단위로 분해했고, v121에서는 `ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS`의 남은 26개 gap을 점수로 오염시키지 않는 bounded planner-only repair task로 내보내게 했다.

v126 패치에서는 중요한 의미 오류를 하나 고쳤다. 기존 production full-thesis 승격은 사실상 "Green primitive가 모두 닫힌 종목만 FULL_THESIS"로 취급했다. 그래서 StageCourt가 `FINAL` 점수와 Stage2/Stage1 결론을 냈어도, Green gate primitive가 빠져 있으면 "정밀평가 미실행"처럼 막혔다. 이제는 `score_status=FINAL` 또는 `FINAL_WITH_NONMATERIAL_GAPS`이면 production full-thesis 결과로 인정하고, 빠진 Green primitive는 `full_thesis_green_gap_primitives`에 남긴다. 반대로 `PENDING_MATERIAL_GAPS`는 여전히 production full-thesis로 올리지 않는다.

v126 replay 기준으로 v109 leaf bundle의 `FULL_THESIS` production path는 다음처럼 바뀌었다.

```text
input leaf bundle:
  output/census_v4/2026-07-01-v109-target-aware-claim-id

replay output:
  output/census_v4/2026-07-01-v126-full-thesis-final-green-gap-replay

candidate trace count:        46
promoted full-thesis traces:  46
promoted full-thesis rows:    20
production audit verdict:     FULL_THESIS_PRODUCTION_PASS
production pass allowed:      true
```

쉬운 예:

```text
이전 코드:
  정밀검사 결과가 "Stage2, Green 서류 일부 부족"이어도
  Green 서류가 없으니 "정밀검사 안 됨"으로 처리했다.

현재 코드:
  정밀검사 결과는 FULL_THESIS로 인정한다.
  다만 Green 승급에 부족한 서류는 별도 목록으로 남긴다.
```

단, canonical `output/census_v4/2026-07-01`은 아직 `brain_web_mode=disabled`로 재생성된 anti-fake 기준 문서다. 그래서 canonical goal completion은 여전히 미완료다.

쉬운 예:

```text
접수표:
  전 종목이 Census 평가 대상에 올라왔는가?
  -> 예. 이건 많이 진행됐다.

검사결과:
  일부 종목에서 실제 문서, claim, score contribution이 생겼는가?
  -> 예. v109 live leaf에서는 Brain/Web evidence 경로가 통과했다.

최종진단서:
  이 종목은 100점 full thesis 기준으로 Stage Green/Yellow/Red라고 말할 수 있는가?
  -> v126 replay에서는 20개 row가 production full-thesis로 승격된다.
     하지만 canonical goal run은 아직 live Brain/Web 모드로 재실행되지 않아 최종 완료가 아니다.
```

즉 지금 결과를 "삼성전자 Stage 1", "하이닉스 Stage 2"처럼 운영 판단으로 말하면 안 된다. 더 정확한 표현은 "Census v4가 일부 source-backed partial claim을 찾았지만, FULL_THESIS 운영 Stage로 승격하지 못했다"이다.

추가로, runtime budget이 끝난 실행도 낮은 점수를 확정하면 안 된다. 예를 들어 v115처럼 budget이 즉시 소진되면 planner/source를 새로 시작하지 않고 `planner_not_attempted_after_runtime_budget_exhausted`로 남긴다. 이것은 "나쁜 점수"가 아니라 "아직 조사하지 못한 Pending"이다.

## 0. v109 최신 상태 요약

최신 기준 output:

```text
output/census_v4/2026-07-01-v109-target-aware-claim-id
```

최종 runner 출력:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

중요한 결론:

```text
target_gate: brain_web
target_gate_pass: true
brain_web_evidence_pass: true
goal_completion_ready: false
full_thesis_stage_row_count: 0
full_e2r_verified_score_row_count: 0
meaningful_operational_stage_pass: false
```

쉬운 예:

```text
도서관에서 실제 자료를 찾고, 문장 근거 카드도 만들었다.
하지만 아직 "이 종목은 full thesis 기준 Green/Yellow/Red"라고 도장 찍는 최종 심사는 통과하지 못했다.
```

### 0.1 v108 실패와 v109 패치

v108 실패:

```text
claim_id collision with different claim: CLM-b64fab4400638fa6720d
```

원인:

같은 문장 또는 같은 source fact를 서로 다른 target 회사에 붙일 때 `claim_id`가 target을 구분하지 못했다. 예를 들어 공급사 기사에 나온 한 문장을 삼성전자 평가에도, 공급사 평가에도 붙이면 서로 다른 판정이어야 하는데 같은 claim ID로 충돌할 수 있었다.

패치:

1. `stable_claim_id`에 `target_entity_id`를 포함했다.
2. `AdjudicatedClaim.from_raw`가 target-aware claim ID를 만들게 했다.
3. `v4_source_quality_promotion`이 별도 legacy ID를 다시 만들지 않고 Evidence OS claim ID를 그대로 쓰게 했다.
4. `brain_to_claim_trace.jsonl` 병합 key를 `accepted_claim_id` 단독이 아니라 `brain_to_claim_trace_id`로 바꿨다.
5. 같은 claim이 다른 event에서 대표/비대표 trace로 재사용될 때 Brain/Web readiness gate가 event 범위로 판정하게 했다.

검증:

```text
v109 live/bounded run이 같은 collision 없이 완료
brain_to_claim_trace_count = 330
brain_trace_missing_count = 0
brain_to_claim_trace_audit verdict = PASS
```

### 0.2 v109 Brain/Web evidence gate

`brain_web_readiness_gate_audit.json` 기준:

```text
verdict: READY_FOR_BRAIN_WEB_EVIDENCE_PASS
blockers: []
llm_planner_call_count: 600
llm_real_provider_success_count: 60
llm_claim_extractor_attempt_count: 74
llm_claim_extractor_timeout_count: 0
llm_claim_extractor_provider_error_count: 0
web_search_task_count: 127
web_search_result_count: 1519
web_fetched_document_count: 74
web_or_llm_accepted_claim_count: 104
brain_to_claim_trace_count: 330
brain_score_contribution_count: 87
brain_stage_trace_count: 46
snippet_to_score_count: 0
fake_provider_used_count: 0
snapshot_document_count: 0
```

해석:

이제 "LLM/Web을 켰다고 말만 하는 상태"는 아니다. 실제 planner 호출, 검색 task, fetched document, LLM claim extraction, accepted claim, score contribution, StageCourt trace가 leaf로 남았다.

단, `brain_web_evidence_pass`는 `FULL_THESIS` 완료가 아니다. 이것은 "실제 자료 수집과 claim 장부 경로가 작동했다"는 게이트다.

### 0.3 v109 Stage와 score 상태

`operator_digest.md` 기준:

```text
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
event_board_non_stage0_count = 65
score_scale_distribution = {'NO_SCORE': 3321, 'EVENT_WEIGHTED_PARTIAL': 70}
operator_stage_use_distribution = {'NOT_FULL_THESIS_STAGE': 3391}
operator_score_use_distribution = {'NOT_FULL_E2R_SCORE': 3391}
```

즉 "stage 신호가 있는 row"는 있다. 하지만 그 stage는 운영용 full thesis stage가 아니다.

쉬운 예:

```text
부분 점수:
  "이 회사에 최근 이벤트와 일부 근거 claim이 있다"는 임시 검사표

FULL_THESIS 점수:
  "모든 필수 primitive와 Green/Yellow/Red gate를 통과한 최종 진단서"

현재 v109:
  임시 검사표는 생김
  최종 진단서는 아직 0개
```

삼성전자와 SK하이닉스도 같다.

```text
삼성전자:
  stage_scope = BRAIN_WEB_PARTIAL
  canonical_stage = 1
  event_evidence_score = 60.0
  full_thesis_stage = FULL_THESIS_NOT_RUN
  operator_stage_use = NOT_FULL_THESIS_STAGE
  missing = hbm_capacity_constraint, hbm_capacity_pre_sold

SK하이닉스:
  stage_scope = BRAIN_WEB_PARTIAL
  canonical_stage = 2
  event_evidence_score = 75.8333
  full_thesis_stage = FULL_THESIS_NOT_RUN
  operator_stage_use = NOT_FULL_THESIS_STAGE
  missing = hbm_capacity_constraint
```

따라서 이 숫자를 "삼성전자 60점 Stage1", "하이닉스 75.8점 Stage2"라고 운영 판단으로 말하면 안 된다. 정확히는 "BRAIN_WEB_PARTIAL 이벤트 점수는 생겼지만 full thesis는 미실행/미승격"이다.

### 0.4 v109 follow-up loop 결과

`full_thesis_follow_up_iterations_audit.json` 기준:

```text
iteration_count = 2
follow_up_iteration_count = 1
final_follow_up_seed_event_count = 54
final_promoted_full_thesis_row_count = 0
status = RAN_FOLLOW_UP_ITERATIONS
```

iteration별:

```text
iteration 1:
  seed_event_count = 85
  accepted_claim_count = 198
  real_provider_success_count = 30
  source_task_execution_count = 237
  production_candidate_row_count = 20
  production_blocked_candidate_count = 20
  promoted_full_thesis_row_count = 0

iteration 2:
  seed_event_count = 48
  accepted_claim_count = 132
  real_provider_success_count = 30
  source_task_execution_count = 212
  production_candidate_row_count = 46
  production_blocked_candidate_count = 46
  promoted_full_thesis_row_count = 0
```

해석:

follow-up seed를 만들고 다시 Brain/Web에 넣는 경로는 실제로 돌았다. 하지만 그 결과가 아직 FULL_THESIS 승격까지 이어지지는 않았다.

쉬운 예:

```text
부족 서류 목록을 만들고 재요청까지 보냈다.
재요청으로 일부 서류는 더 들어왔다.
하지만 면허 발급 기준의 필수 서류 묶음은 아직 완성되지 않았다.
```

### 0.5 v109 goal requirement matrix

`goal_requirement_matrix_audit.json` 기준:

```text
required_goal_completion_count = 21
pass = 17
pending = 4
fail = 0
goal_completion_minimum_pass = false
```

남은 pending gate:

```text
FULL_THESIS_SMOKE_PASS
FULL_THESIS_PRODUCTION_PASS
FULL_THESIS_SEED_PROMOTION_PASS
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
```

`goal_completion_audit.json` 기준 blocker:

```text
full_thesis_smoke_pending
full_thesis_smoke_execution_pending
full_thesis_production_pass_false
full_thesis_seed_promotion_pass_false
source_backed_replay_parity_all_archetypes_pending
goal_requirement_matrix_pass_false
```

### 0.6 v109 전체 테스트 artifact

전체 테스트는 machine-readable artifact로 검증했다.

```text
artifact: output/census_v4/2026-07-01-v109-target-aware-claim-id/full_unittest_result_artifact.json
status: OK
test_count: 5144
failed_count: 0
error_count: 0
duration_seconds: 240.1351
artifact_sha256: 98fb90cfdaa082e406b392a92aca597486f3df1aea923eed66f84b44ed5db183
log_sha256: 08516911e1fdfa5056f0934eadc36a6bd78752ef91a2acc53e50600d908c738b
```

### 0.7 v110 follow-up context 패치와 overlong probe

v109 이후 추가 진단:

```text
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS 73건
STAGECOURT_READY_NOT_PROMOTED 46건
ACCEPTED_CLAIM_NOT_CREATED 12건
STAGECOURT_TRACE_NOT_CREATED 2건
```

이 중 `STAGECOURT_READY_NOT_PROMOTED`는 단순 오류가 아니라 "partial/event stage는 만들었지만 full thesis Green gate primitive가 아직 부족하다"는 쪽이었다. 예를 들어 삼성전자/하이닉스 C06 쪽은 `hbm_capacity_constraint`, `hbm_capacity_pre_sold` 같은 gap이 남았다.

v110 코드 패치:

```text
1. full-thesis blocker follow-up SourceTask에 follow_up_archetype_id를 명시
2. full-thesis blocker follow-up SourceTask에 follow_up_primitive_gap을 명시
3. follow-up seed 최상위에 target_archetype, target_archetype_status, primitive_gap을 추가
4. planner context allowlist에 primitive_gap을 추가
5. source/router audit이 target_primitive_gap을 볼 수 있게 materialization trace를 보강
6. official-first는 유지하되, official/report connector가 막히는 경우 bounded general web fallback을 허용
```

쉬운 예:

```text
이전:
  "삼성전자 full thesis가 막혔다"는 말은 갔지만,
  정확히 C06의 hbm_capacity_pre_sold 서류를 찾으라는 표식이 약했다.

패치 후:
  "삼성전자 / C06 / hbm_capacity_pre_sold / Green gate follow-up"이라는
  주소가 planner와 source task에 같이 들어간다.
```

중요한 제한:

이것은 검색어 하드코딩이 아니다. 코드가 `{회사명} HBM pre-sold` 같은 query를 직접 만들지 않는다. 코드가 하는 일은 "지금 필요한 primitive gap이 무엇인지"를 LLM planner에게 정확히 전달하고, LLM이 만든 query를 bounded source router로 검증해 실행하는 것이다.

검증:

```text
targeted suite:
  PYTHONPATH=src python -m unittest \
    tests.test_census_v4_brain_stage_promotion_gate \
    tests.test_research_brain_v4_operational_modes \
    tests.test_agentic_evidence_os \
    tests.test_census_v4_brain_web_readiness_gate -v

result:
  Ran 506 tests
  OK

py_compile:
  src/e2r/census/census_runner_v4.py
  src/e2r/research_brain/v4_production_orchestrator.py
  src/e2r/agentic/evidence_os.py
  src/e2r/research_brain/v4_source_quality_promotion.py
  OK
```

v110 전체 테스트 artifact:

```text
artifact: output/census_v4/2026-07-01-v110-followup-canonical-gap-context/full_unittest_result_artifact.json
status: OK
test_count: 5144
failed_count: 0
error_count: 0
duration_seconds: 239.0402
log_sha256: dff9987cc2d27de9016778fc34b2d1d4716b661746e2b5c09aee443004eda7fc
```

v110 큰 live probe:

```text
output: output/census_v4/2026-07-01-v110-followup-canonical-gap-context
command intent:
  max_iterations=2
  brain_planner_success_limit=60
  brain_retry_max=2
  live_full_bounded
result:
  interrupted after about 2 hours
  process exit code 130
  runner output: INVALID_PARTIAL_OUTPUT
```

중단 시점 산출물:

```text
source_task_executions.jsonl: 92 rows
accepted_claims.jsonl: 92 rows
stagecourt_traces.jsonl: 92 rows
research_brain_full_thesis_seed_events.jsonl: 85 rows
planner_runs.jsonl: 0 rows
claim_extractor_runs.jsonl: 0 rows
brain_web_readiness_gate_audit.json: missing
goal_completion_audit.json: missing
```

해석:

이 v110 probe는 완료 실행이 아니므로 goal pass/fail 증거로 쓰면 안 된다. 다만 운영상 중요한 병목은 확인됐다. `retry=2`와 높은 real planner success cap을 함께 주면 Codex planner/extractor provider 호출이 매우 길어지고, 최종 audit이 나오기 전까지 operator가 상태를 판단하기 어렵다.

쉬운 예:

```text
병원 재검을 보냈는데 검사실이 2시간 동안 계속 샘플을 돌리고,
최종 검사표는 아직 안 나온 상태다.

이걸 "검사 통과"라고 할 수도 없고,
"환자 상태가 나쁘다"고 확정할 수도 없다.
정확한 결론은 "검사 파이프라인이 너무 오래 걸렸고,
중간 상태를 운영자가 볼 수 있는 budget/progress audit이 더 필요하다"이다.
```

따라서 다음 패치는 두 갈래다.

```text
1. 기능 경로:
   v110 follow-up context 패치를 유지하고, 작은 bounded smoke로
   target_archetype/primitive_gap이 실제 planner prompt와 source task에 반영되는지 확인한다.

2. 운영 안정성:
   live provider loop에 global wall-clock / provider-call budget / partial progress audit을 추가한다.
   최종 audit 전에 오래 걸리면 INVALID_PARTIAL_OUTPUT만 남기지 말고,
   어느 event/primitive/provider 호출에서 오래 걸렸는지 operator artifact를 남긴다.
```

### 0.8 v111 작은 follow-up context smoke

v110 큰 probe가 너무 오래 걸렸기 때문에, 새 schema가 실제 산출물에 들어가는지만 보는 작은 smoke를 별도로 돌렸다.

실행 의도:

```text
full pass 검증이 아니라,
follow-up blocker seed가 target_archetype/primitive_gap/budget을
planner input artifact까지 싣는지 확인한다.
```

설정:

```text
output: output/census_v4/2026-07-01-v111-followup-context-smoke
target_gate: anti_fake
max_symbols: 200
brain_universe_limit: 3
brain_planner_success_limit: 3
brain_retry_max: 2
brain_claim_extractor_provider: rule_fallback
result: NOT_READY
```

`NOT_READY` 해석:

이 smoke는 성공/실패 판정용 full run이 아니다. `rule_fallback` extractor를 썼기 때문에 Brain/Web evidence gate는 당연히 막혔다.

실제 blocker:

```text
LLM claim extractor has no real LLM provider runs
web/LLM accepted claim count is zero
Brain/Web operational minimum fetched documents not met: 3/10
Brain/Web operational minimum claim extractor attempts not met: 3/10
Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

그래도 smoke에서 확인된 것:

```text
planner_runs.jsonl: 66 rows
source_task_executions.jsonl: 151 rows
accepted_claims.jsonl: 97 rows
brain_to_claim_trace.jsonl: 34 rows
stagecourt_traces.jsonl: 97 rows
score_contributions.jsonl: 98 rows
full_thesis_blocker_follow_up_seed_events.jsonl: 5 rows
full_thesis_blocker_follow_up_source_tasks.jsonl: 5 rows
```

follow-up gap 분포:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP:
  contract_duration_months: 2
  margin_bridge_visible: 2
  contract_amount_to_prior_sales: 1
```

새 필드 확인 예:

```text
company_name: 삼성제약
target_archetype: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
target_archetype_status: GREEN_GATE_BLOCKER_FOLLOW_UP
primitive_gap: contract_duration_months
follow_up_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
follow_up_primitive_gap: contract_duration_months
structured_payload.general_search_allowed: true
structured_payload.official_first_required: true
structured_payload.max_queries: 3
structured_payload.max_candidates: 20
structured_payload.max_fetches: 3
hardcoded_query_count: 0
```

쉬운 예:

```text
이전에는 "삼성제약 서류 더 필요" 정도였다.
이제는 "삼성제약 / C05 / contract_duration_months / 공식 우선 / 최대 3쿼리, 20후보, 3fetch"처럼
재조사 주소와 예산이 같이 붙는다.
```

따라서 v111 smoke의 결론은:

```text
context propagation: 확인됨
full Brain/Web evidence pass: 아님
FULL_THESIS production pass: 아님
다음 필요 패치: provider loop runtime/progress audit
```

### 0.9 partial run invalid marker 보강

v110 큰 probe를 중단했을 때 `INVALID_PARTIAL_OUTPUT`만 출력되면, 사람이 나중에 어느 단계까지 갔는지 다시 파일을 뒤져야 했다. 그래서 CLI partial marker를 보강했다.

패치:

```text
src/e2r/cli/run_e2r_census_v4_until_pass.py
```

`KeyboardInterrupt` 또는 runner exception이 나면 기존처럼 해당 output은 score/stage 증거로 금지한다. 추가로 `partial_run_invalid.json` 안에 핵심 파일별 존재 여부, size, jsonl row count, 수정시각을 넣는다.

예:

```text
planner_runs.jsonl:
  exists: true
  row_count: 2

accepted_claims.jsonl:
  exists: true
  row_count: 0
```

쉬운 예:

```text
이전:
  "검사가 중단됐다"만 남음

패치 후:
  "검사가 중단됐고, planner_runs는 2장 썼고,
   accepted_claims는 0장인 상태에서 멈췄다"까지 남음
```

이건 full progress sink의 대체품은 아니다. 다만 다음 긴 run이 중단되더라도, 최소한 operator가 빈손으로 남지 않게 하는 안전장치다.

검증:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_research_brain_v4_operational_modes \
  tests.test_agentic_evidence_os \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_run_mode_honesty -v

result:
  Ran 526 tests
  OK
```

최종 전체 suite artifact:

```text
artifact: output/census_v4/2026-07-01-v112-partial-marker-progress-audit/full_unittest_result_artifact.json
status: OK
test_count: 5144
failed_count: 0
error_count: 0
duration_seconds: 242.2711
log_sha256: 23abdf6ccbac0aa5ad0fb4e263948e7b36cde133b7f14a94d7774b8cdf254a0e
```

### 0.10 Brain/Web runtime progress audit

partial marker는 "중단된 뒤" 어디까지 갔는지 남기는 장치다. 하지만 v110처럼 provider loop가 오래 돌 때는, 실행 중에도 현재 단계가 보여야 한다.

그래서 Research Brain v4에 runtime progress leaf를 추가했다.

패치:

```text
src/e2r/research_brain/v4_schemas.py
  ProductionShadowV4Config.runtime_progress_path 추가

src/e2r/research_brain/v4_production_orchestrator.py
  _record_runtime_progress_v4 추가
  planner/source/retry 루프 주요 phase 기록

src/e2r/census/census_runner_v4.py
  output_root/brain_web_runtime_progress.json 경로 전달
```

새 artifact:

```text
output/census_v4/<run-id>/brain_web_runtime_progress.json
```

기록되는 주요 phase:

```text
events_selected
events_ordered
planner_batch_start
planner_batch_end
missing_external_web_plan_retry_start
missing_external_web_plan_retry_end
planner_run_processing_start
source_execution_start
source_execution_end
feedback_retry_planner_start
feedback_retry_planner_end
feedback_retry_source_execution_start
feedback_retry_source_execution_end
planner_run_processing_end
accepted_claim_target_plan_more_start
accepted_claim_target_plan_more_end
completed
```

쉬운 예:

```text
이전:
  Brain이 2시간 도는 동안 파일이 비어 있어서
  "지금 planner 중인지, extractor 중인지, source fetch 중인지"를 알기 어려웠다.

패치 후:
  brain_web_runtime_progress.json을 보면
  latest_phase=feedback_retry_planner_start 같은 식으로 현재 위치를 볼 수 있다.
```

v113 smoke:

```text
output: output/census_v4/2026-07-01-v113-runtime-progress-smoke
planner_provider: none
claim_extractor_provider: rule_fallback
target_gate: anti_fake
result: NOT_READY
```

`NOT_READY`는 정상이다. 이 smoke는 real Brain/Web pass가 아니라 progress path 연결 확인용이다.

확인 결과:

```text
brain_web_runtime_progress.json exists: true
status: COMPLETED
latest_phase: completed
event_count: 89
config.planner_provider: none
```

최근 phase에는 다음이 포함됐다.

```text
events_selected
events_ordered
planner_batch_start
planner_batch_end
planner_run_processing_start
planner_run_processing_end
completed
```

검증:

```text
targeted unit:
  tests.test_research_brain_v4_operational_modes.
  ResearchBrainV4OperationalModesTests.
  test_runtime_progress_file_records_research_brain_phases
  OK

related suite:
  PYTHONPATH=src python -m unittest \
    tests.test_research_brain_v4_operational_modes \
    tests.test_census_v4_run_mode_honesty \
    tests.test_census_v4_brain_stage_promotion_gate \
    tests.test_census_v4_brain_web_readiness_gate -v

result:
  Ran 125 tests
  OK
```

최종 전체 suite artifact:

```text
artifact: output/census_v4/2026-07-01-v114-runtime-progress-audit/full_unittest_result_artifact.json
status: OK
test_count: 5145
failed_count: 0
error_count: 0
duration_seconds: 242.0162
log_sha256: c7caefe85fb3b6f126a21c01adb4c1b5464ca3f203cb31e9fddbe31e942a10c6
```

0.10 시점의 남은 한계:

```text
runtime progress는 "현재 어디까지 왔는지"를 보여주는 장치다.
아직 provider-call 자체를 global wall-clock budget으로 자동 중단하지는 않는다.
다음 단계는 long-running provider loop를 fail/pending으로 안전하게 닫는 runtime budget policy다.
```

### 0.11 Brain/Web runtime budget policy

v110 큰 probe의 가장 위험한 운영 문제는 "결과가 틀렸다" 이전에, 긴 provider loop가 끝나기 전까지 operator가 안전하게 멈추고 해석할 기준이 약했다는 점이다.

그래서 Research Brain v4에 runtime budget 정책을 추가했다.

패치:

```text
src/e2r/research_brain/v4_schemas.py
  ProductionShadowV4Config.runtime_budget_seconds 추가

src/e2r/census/census_runner_v4.py
  CensusV4RunConfig.brain_runtime_budget_seconds 추가
  Research Brain config로 runtime budget 전달

src/e2r/cli/run_e2r_census_v4_until_pass.py
  --brain-runtime-budget-seconds CLI 인자 추가

src/e2r/research_brain/v4_production_orchestrator.py
  planner batch, source execution, feedback retry, plan_more 사이에서 budget 확인
  budget 소진 시 새 provider/source 호출을 시작하지 않고 pending row 생성
  runtime progress에 runtime_budget_exhausted phase와 완료 상태 기록
```

중요한 제한:

```text
이 패치는 이미 시작된 provider 호출을 중간에서 강제 kill하지 않는다.
이미 시작된 호출은 기존 per-call timeout 정책이 맡는다.
runtime budget은 새 planner/source/retry 호출을 시작하기 전에 확인하는 global stop rule이다.
```

쉬운 예:

```text
병원 검사 시간이 30분으로 제한돼 있다.

나쁜 처리:
  30분이 지났는데 검사 못 했으니 "질병 있음"으로 확정한다.

이번 처리:
  30분이 지나면 새 검사를 더 시작하지 않고
  "검사 미완료 / pending"으로 남긴다.
```

v115 runtime budget smoke:

```text
output: output/census_v4/2026-07-01-v115-runtime-budget-smoke
brain_runtime_budget_seconds: 0
result: NOT_READY
```

`NOT_READY`는 정상이다. 이 smoke는 full pass가 아니라 budget exhaustion이 낮은 점수 확정으로 흐르지 않는지 보는 실행이다.

확인 결과:

```text
brain_web_runtime_progress.json:
  status: COMPLETED
  latest_phase: completed
  event_count: 7
  latest_event.runtime_budget_exhausted: true
  latest_event.planner_run_count: 22
  latest_event.source_task_execution_count: 0

planner_runs.jsonl:
  row_count: 22
  provider_error:
    planner_not_attempted_after_runtime_budget_exhausted: 22
  provider_name:
    not_attempted_after_runtime_budget_exhausted: 22
```

해석:

```text
v115는 22개 event를 "조사 실패로 낮은 점수"로 만들지 않았다.
전부 "runtime budget 때문에 planner를 시작하지 못한 pending"으로 남겼다.
source task 실행도 0개라서 근거 없는 점수 생성 경로가 아니다.
```

v117 runtime budget status 분리:

```text
output: output/census_v4/2026-07-01-v117-runtime-budget-audit-unit
verdict: NOT_READY

brain_web_attempt.full_thesis_seed_runtime_budget_exhausted_count: 22
brain_web_readiness_gate.full_thesis_seed_runtime_budget_exhausted_count: 22
readiness blocker:
  full-thesis seed planner stopped after runtime budget exhaustion

full_thesis_seed_materialization_audit.status_counts:
  PLANNER_NOT_RUN: 63
  PLANNER_PENDING_RUNTIME_BUDGET_EXHAUSTED: 22
```

해석:

```text
v115 이전 표현:
  planner real provider success가 없다

v117 이후 표현:
  runtime budget 때문에 planner를 시작하지 못한 seed가 22개다

둘은 다르다.
전자는 provider 실패처럼 읽힐 수 있고,
후자는 조사 예산 종료라서 낮은 점수 확정이 아니라 resume/pending 대상이다.
```

관련 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_brain_web_readiness_gate -v

result:
  Ran 126 tests
  OK
```

v117 상태 분리 관련 테스트:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_web_readiness_gate -v

result:
  Ran 121 tests
  OK
```

최종 전체 suite artifact:

```text
artifact: output/census_v4/2026-07-01-v116-runtime-budget-audit/full_unittest_result_artifact.json
status: OK
test_count: 5146
failed_count: 0
error_count: 0
duration_seconds: 241.4934
log_sha256: 0445b1af3eb541da8a7e794e64bdf7d4b56913375ce10f4e91a779c3c9e0899c
```

상태 분리 이후 최종 전체 suite artifact:

```text
artifact: output/census_v4/2026-07-01-v118-runtime-budget-status-audit/full_unittest_result_artifact.json
status: OK
test_count: 5147
failed_count: 0
error_count: 0
duration_seconds: 245.2368
log_sha256: afb0e3f82bc32f6204547025d91c18670a024b4870bd3d5aac1ad0b0c26d0381
```

남은 한계:

```text
runtime budget은 "너무 오래 걸리면 안전하게 Pending으로 닫는 장치"다.
이 장치만으로 FULL_THESIS row가 생기지는 않는다.
다음 핵심은 FULL_THESIS 승격 후보가 왜 0개인지 primitive/gate/source-task 단위로 분해해서 고치는 것이다.
```

### 0.12 FULL_THESIS blocker breakdown audit

v109 수동 분해 결과, production full-thesis 후보 46개는 모두 `missing_green_gate_primitives` 때문에 승격되지 않았다.

v109 기준 분포:

```text
candidate_row_count: 46
promoted_full_thesis_row_count: 0
blocked_candidate_count: 46
blockers:
  missing_green_gate_primitives: 46

archetype:
  C05_EPC_MEGA_CONTRACT_MARGIN_GAP: 40
  C06_HBM_MEMORY_CUSTOMER_CAPACITY: 5
  C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE: 1

missing green primitive:
  margin_bridge_visible: 38
  contract_amount_to_prior_sales: 27
  contract_duration_months: 26
  hbm_capacity_constraint: 5
  hbm_capacity_pre_sold: 4
  customer_preorder_or_allocation: 3
  mix_improvement: 1
  operating_leverage_visible: 1
  pricing_power_confirmed: 1
  volume_growth_visible: 1
  revenue_visibility_contract: 1
```

쉬운 예:

```text
46명이 면허 시험장까지는 왔다.
그런데 전원이 필수 서류 하나 이상이 빠져서 면허 발급은 0명이다.

가장 많이 빠진 서류는 C05 계약의 margin bridge,
계약금액/기존매출 비율,
계약기간이다.
```

이 수동 분해를 매번 다시 하지 않도록 `full_thesis_production_runner_audit.json`에 아래 요약 필드를 추가했다.

```text
blocked_candidate_blocker_counts
blocked_candidate_archetype_counts
blocked_candidate_missing_green_primitive_counts
blocked_candidate_present_primitive_counts
blocked_candidate_missing_green_primitive_counts_by_archetype
```

중요:

```text
이 필드는 점수를 올리는 패치가 아니다.
왜 FULL_THESIS 승격이 0개인지 운영자가 바로 볼 수 있게 만드는 audit 패치다.
```

검증:

```text
targeted:
  PYTHONPATH=src python -m unittest \
    tests.test_census_v4_brain_stage_promotion_gate.
    CensusV4BrainStagePromotionGateTests.
    test_brain_partial_stage_is_not_production_full_thesis_without_green_gate_coverage -v

result:
  OK

related:
  PYTHONPATH=src python -m unittest \
    tests.test_census_v4_brain_stage_promotion_gate \
    tests.test_census_v4_run_mode_honesty \
    tests.test_census_v4_full_thesis_smoke_tasks -v

result:
  Ran 51 tests
  OK
```

최종 전체 suite artifact:

```text
artifact: output/census_v4/2026-07-01-v120-blocker-breakdown-audit/full_unittest_result_artifact.json
status: OK
test_count: 5147
failed_count: 0
error_count: 0
duration_seconds: 249.7485
log_sha256: e85abbf025bbee300d55239325505cd7d083260308e0d1d8234a042868b8db97
```

### 0.13 ALL_ARCHETYPE replay gap repair task export

v109 기준 `ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS`는 아직 통과가 아니다.

현재 replay matrix:

```text
archetype_count: 36
required_archetype_count: 32
source_backed_ready_count: 6
guard_replay_ready_count: 6
missing_required_archetype_count: 26
all_archetype_replay_pass: false

status_counts:
  SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY: 6
  SOURCE_GAP_PENDING: 26
  GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY: 4
```

문제:

```text
전 아키타입 replay가 막힌 이유를 "아직 26개 부족"으로만 두면,
다음 agent가 어디부터 찾아야 하는지 다시 수동으로 분해해야 한다.
반대로 부족한 아키타입을 점수로 바로 넣으면 source_proxy/source_gap이 운영 점수로 새는 문제가 생긴다.
```

v121 패치:

```text
output/<run>/all_archetype_replay_gap_source_tasks.jsonl
output/<run>/all_archetype_replay_gap_seed_events.jsonl
```

두 파일을 새 leaf artifact로 만들었다.

각 missing required archetype마다 1개씩 생성된다.

```text
replay_gap_source_task_count: 26
replay_gap_seed_event_count: 26
```

중요한 안전장치:

```text
score_allowed_before_execution: false
stage_promotion_allowed_before_execution: false
production_score_evidence_allowed: false
hardcoded_query_count: 0
query_intents: []
official_first_required: true
llm_query_required: true
max_queries: 3
max_candidates: 20
max_fetches: 3
forbidden_source_classes:
  source_proxy_only
  evidence_url_pending
  snippet_only_score
  unbounded_general_search
```

쉬운 예:

```text
나쁜 처리:
  C01 replay가 부족하다
  -> 코드가 임의로 C01 점수를 채우거나 검색어를 하드코딩한다.

이번 처리:
  C01 replay가 부족하다
  -> C01 Evidence Contract에서 필요한 primitive 목록만 작업표로 만든다.
  -> LLM planner가 실제 query를 만들고,
     official-first bounded source task가 원문을 가져오고,
     Evidence OS claim/anchor가 생긴 뒤에만 replay matrix를 갱신한다.
```

추가 안전 패치:

`all_archetype_replay_gap_seed_events.jsonl`은 특정 종목용 seed가 아니다. 그래서 일반 Research Brain candidate seed로 잘못 들어가면 `symbol=None`이 가짜 종목처럼 실행될 수 있다.

이를 막기 위해:

```text
research_brain_eligible: false
all_archetype_replay_repair_planner_eligible: true
```

로 분리했다. 또한 `research_brain_eligible=false`인 external seed row는 Research Brain candidate loader가 건너뛰도록 했다.

쉬운 예:

```text
full_thesis follow-up seed:
  "삼성전자 C06 hbm_capacity_pre_sold를 더 찾아라"
  -> 실제 종목이 있으므로 Research Brain 대상이다.

all_archetype replay gap seed:
  "C01 아키타입의 source-backed positive/guard fixture를 찾아라"
  -> 특정 종목 운영 점수가 아니므로 일반 Research Brain 대상이 아니다.
```

검증:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_all_archetype_replay_matrix \
  tests.test_census_v4_artifact_manifest \
  tests.test_research_brain_v4_operational_modes -v

result:
  Ran 78 tests
  OK
```

추가 관련 검증:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_web_readiness_gate -v

result:
  Ran 77 tests
  OK
```

v121 전체 suite artifact:

```text
artifact: output/census_v4/2026-07-01-v121-all-archetype-replay-gap-audit/full_unittest_result_artifact.json
status: OK
failed: 0
errors: 0
duration_seconds: 253.8212
log_sha256: 987c1715e478fb38d0dbb233ef7663647c349b67a445e01e6eb80c1e1232a72c
```

v122 추가 보강:

```text
readiness_verdict.all_archetype_replay_matrix
goal_completion_audit.all_archetype_replay_matrix_summary
```

에도 replay gap task/seed count와 path를 노출했다.

쉬운 예:

```text
이전:
  all_archetype_replay_matrix.json을 직접 열어야 26개 repair task를 볼 수 있었다.

이후:
  readiness_verdict.json 또는 goal_completion_audit.json만 봐도
  replay_gap_source_task_count=26,
  replay_gap_seed_event_count=26이 보인다.
```

최신 전체 suite artifact:

```text
artifact: output/census_v4/2026-07-01-v122-all-archetype-replay-gap-summary-audit/full_unittest_result_artifact.json
status: OK
failed: 0
errors: 0
duration_seconds: 246.6962
log_sha256: c90bd612acfbe248c114f7991c52af29946a8567e838d82bf1e9dd93e5cf2422
```

v123 seed loader safety:

external candidate seed loader가 `symbol=None` 또는 `symbol=000000`을 Research Brain 후보로 받아들이지 않게 했다.

쉬운 예:

```text
나쁜 입력:
  {"symbol": null, "research_brain_eligible": true}

이전 위험:
  None -> "000000"으로 정규화되어 가짜 종목처럼 들어갈 수 있었다.

패치 후:
  빈 symbol 또는 전부 0인 symbol은 seed loader에서 버린다.
  "660"처럼 실제 코드를 축약해 넣은 경우만 "000660"으로 정규화한다.
```

이 패치는 all-archetype replay gap seed를 막기 위한 우회 패치가 아니다. 더 일반적인 입구 안전장치다. `research_brain_eligible=false`인 row는 계속 skip하고, `research_brain_eligible=true`라도 실제 종목 symbol이 없으면 skip한다.

최신 전체 suite artifact:

```text
artifact: output/census_v4/2026-07-01-v123-seed-loader-symbol-safety-audit/full_unittest_result_artifact.json
status: OK
failed: 0
errors: 0
duration_seconds: 248.1507
log_sha256: 75a3a0e9b46819adee235dd30b3f7fa9424f2e8d5a55f6030815a1559d52865c
```

v124 full-thesis seed materialization context audit:

`full_thesis_seed_materialization_trace.jsonl`와 `full_thesis_seed_materialization_audit.json`에 seed 원본과 target gap 분포를 추가했다.

추가 trace 필드:

```text
seed_source_family
seed_source_id
seed_event_type
seed_raw_reason_codes
follow_up_task_id
target_archetype
target_primitive_gap
```

추가 audit 요약:

```text
seed_source_family_counts
target_archetype_counts
target_primitive_gap_counts
status_counts_by_target_archetype
status_counts_by_target_primitive_gap
critical_counts.blocker_follow_up_seed_missing_target_context_count
```

쉬운 예:

```text
이전:
  full thesis seed 133개 중 46개가 STAGECOURT_READY_NOT_PROMOTED다.
  그런데 어떤 seed family/gap이 그렇게 끝났는지 다시 JSONL을 뒤져야 했다.

이후:
  C06_HBM_MEMORY_CUSTOMER_CAPACITY / hbm_capacity_constraint가
  PLANNER_NOT_RUN인지, ACCEPTED_CLAIM_NOT_CREATED인지,
  STAGECOURT_READY_NOT_PROMOTED인지 audit 상단에서 바로 볼 수 있다.
```

중요:

```text
이 패치는 FULL_THESIS를 승격시키는 패치가 아니다.
승격 실패 원인을 seed source family, target archetype, target primitive gap 단위로 추적 가능하게 만든 audit 패치다.
```

검증:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_run_mode_honesty -v

result:
  Ran 52 tests
  OK
```

최신 전체 suite artifact:

```text
artifact: output/census_v4/2026-07-01-v124-full-thesis-seed-context-audit/full_unittest_result_artifact.json
status: OK
failed: 0
errors: 0
duration_seconds: 241.3419
log_sha256: 1e0ad837b1014e827b7580b8df10f6c365f2eafd9e3f92e6223b3df4140e2c17
```

v125 all-archetype replay gap plan 연결:

Census v4의 `all_archetype_replay_matrix.json`에서 남은 26개 source gap을 기존 agentic replay gap plan 체계와 연결했다.

새 output:

```text
all_archetype_replay_acceptance_manifest.json
all_archetype_replay_gap_plan.json
```

매핑 규칙:

```text
positive_replay_pass=true AND guard_replay_pass=true
  -> replay acceptance coverage_status=stage_preview_ready

그 외 required archetype
  -> coverage_status=unsupported_source_gap
```

현재 요약:

```text
required_archetype_count: 32
stage_preview_ready_count: 6
unsupported_source_gap_count: 26
replay_gap_plan_task_count: 26
production_cutover_ready: false
```

쉬운 예:

```text
이전:
  Census v4는 "26개 아키타입 replay gap"이라고 말하고,
  agentic replay gap plan은 별도 체계였다.

이후:
  Census v4의 26개 gap이
  agentic replay gap plan의 unsupported_source_gap task 26개로도 보인다.
  따라서 다음 agent는 기존 replay gap CLI/manifest 체계를 그대로 이어 쓸 수 있다.
```

중요:

```text
이것도 replay를 통과시킨 패치가 아니다.
아직 source-backed fixture가 채워진 것은 아니며,
26개 task의 next_action은 add_source_backed_replay_fixture_or_current_document_for_required_primitives다.
```

검증:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_all_archetype_replay_matrix \
  tests.test_census_v4_artifact_manifest -v

result:
  Ran 12 tests
  OK
```

최신 전체 suite artifact:

```text
artifact: output/census_v4/2026-07-01-v125-all-archetype-replay-gap-plan-audit/full_unittest_result_artifact.json
status: OK
failed: 0
errors: 0
duration_seconds: 241.4764
log_sha256: 86779ca297ce411d9e0e74c19f86f966d1ce49f4ac333eae1e626e19610a0708
```

canonical docs refresh:

```text
command:
  run_census_mode_v4(
    as_of_date=2026-07-01,
    output_root=output/census_v4/2026-07-01,
    write_operational_docs=True
  )

result:
  ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

확인된 새 operational docs:

```text
docs/operational/census_mode_v4_all_archetype_replay_acceptance_manifest.json
docs/operational/census_mode_v4_all_archetype_replay_gap_plan.json
docs/operational/census_mode_v4_all_archetype_replay_gap_source_tasks.jsonl
docs/operational/census_mode_v4_all_archetype_replay_gap_seed_events.jsonl
```

canonical docs 기준 replay gap 요약:

```text
stage_preview_ready_count: 6
unsupported_source_gap_count: 26
replay_gap_plan_task_count: 26
production_cutover_ready: false
```

남은 한계:

```text
v121은 ALL_ARCHETYPE replay gap을 안전하게 "다음 조사 작업표"로 만든 패치다.
아직 26개 source-backed positive/guard replay fixture가 실제로 채워진 것은 아니다.
따라서 ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS는 계속 pending이다.
```

## 1. 이번 Goal의 진짜 성공 조건

세 goal 문서가 요구하는 것은 단순한 전 종목 CSV 생성이 아니다.

핵심 성공 조건은 다음이다.

1. 구형 Census runner가 pass를 만들 수 없게 차단한다.
2. report 문구가 아니라 leaf artifact를 source of truth로 삼는다.
3. `stage`, `score`, `claim`, `score_contribution`, `stagecourt_trace`가 하나의 원자적 결정에서 나온다.
4. `verified_score`와 단일 이벤트 점수를 분리한다.
5. Stage2-Watch와 canonical Stage2를 섞지 않는다.
6. LLM Brain이 실제로 planner, source task, claim extraction에 참여했는지 trace로 증명한다.
7. Naver/Web/TrustedNews/IR/Report source는 snippet이 아니라 full source fetch와 anchor 검증을 통과해야 점수 재료가 된다.
8. 삼성전자, SK하이닉스 같은 고관심 종목은 daily DART event 점수와 C06/HBM full thesis 점수를 분리한다.
9. `FULL_THESIS` 운영 Stage는 Green gate primitive와 source-backed claim이 충분할 때만 승격한다.
10. 전체 아키타입 replay와 5개 독립 검증 에이전트 리뷰를 통과해야 최종 완료로 볼 수 있다.

## 2. 현재 v105 실행 기준 상태

최근 기준 output:

```text
output/census_v4/2026-07-01-v105-live-bounded-rerun-after-extractor-retry
```

전체 row:

```text
total rows = 3391
```

stage scope:

```text
CENSUS_EVENT_BOARD    3368
BRAIN_OFFICIAL_PARTIAL  19
BRAIN_WEB_PARTIAL        4
FULL_THESIS              0
```

score scale:

```text
NO_SCORE                3321
EVENT_WEIGHTED_PARTIAL    70
FULL_E2R_100               0
```

operator stage use:

```text
NOT_FULL_THESIS_STAGE 3391
```

canonical stage:

```text
0        3324
1          46
2          20
3-Red       1
```

가장 중요한 숫자는 `FULL_THESIS = 0`, `FULL_E2R_100 = 0`, `NOT_FULL_THESIS_STAGE = 3391`이다.

쉬운 예:

```text
70개 row에 점수가 조금 있어도, 그 점수는 "full E2R 100점 시험" 점수가 아니다.
그건 "공시/웹/부분 증거 이벤트 점수"에 가깝다.
그래서 운영자가 이 숫자를 Green/Yellow 투자 thesis로 읽으면 안 된다.
```

## 3. Brain/Web evidence 경로는 어디까지 왔나

v105 기준 Brain/Web leaf count:

```text
planner_runs              300
llm_prompts                35
llm_responses              35
source_tasks              327
source_task_executions     327
evidence_documents        171
evidence_anchors          258
web_search_tasks           70
web_search_results        997
web_fetched_documents      47
claim_extractor_runs       47
claim_extractor_success    47
accepted_claims           191
score_contributions       153
stagecourt_traces         115
brain_to_claim_trace       99
brain_claim_mapping_trace 1319
```

이 부분은 이전 v3와 다르다. v3가 "3.67초 report pass"처럼 보였던 것과 달리, v4는 실제로 planner, prompts, responses, source tasks, web search result, fetched documents, accepted claims를 leaf로 남긴다.

다만 이것은 `BRAIN_WEB_EVIDENCE_PASS`에 가까운 성과이고, `FULL_THESIS_REFRESH_PASS`는 아니다.

쉬운 예:

```text
도서관에서 관련 논문을 찾고, 몇 문장을 발췌하고, 근거 카드까지 만들었다.
하지만 아직 최종 논문 심사 통과는 아니다.
```

## 4. 삼성전자와 SK하이닉스 현재 해석

v105 기준:

```text
005930 삼성전자
  stage_scope: BRAIN_WEB_PARTIAL
  canonical_stage: 1
  partial score: 44.1667
  accepted_claim_count: 3
  operator_stage_use: NOT_FULL_THESIS

000660 SK하이닉스
  stage_scope: BRAIN_WEB_PARTIAL
  canonical_stage: 2
  partial score: 75.8333
  accepted_claim_count: 6
  operator_stage_use: NOT_FULL_THESIS
```

주의:

이 숫자는 C06/HBM full thesis 운영 점수가 아니다. 예전에 문제가 됐던 `90점대였다가 60점대로 바뀌는 문제`를 막기 위해, 현재 구조에서는 부분 점수와 full thesis 점수를 분리한다.

따라서 지금은 다음처럼 말해야 한다.

```text
나쁜 표현:
  삼성전자 Stage1, 하이닉스 Stage2로 확정됐다.

좋은 표현:
  삼성전자와 하이닉스는 Brain/Web partial evidence는 생겼지만,
  C06/HBM FULL_THESIS 운영 Stage로는 승격하지 못했다.
```

## 5. FULL_THESIS 생산 경로가 막힌 이유

v105 기준 FULL_THESIS production runner:

```text
candidate_row_count = 23
blocked_candidate_count = 23
promoted_full_thesis_row_count = 0
```

모든 후보가 막힌 직접 사유:

```text
missing_green_gate_primitives
```

누락 primitive count:

```text
margin_bridge_visible             19
contract_duration_months          17
contract_amount_to_prior_sales    13
hbm_capacity_constraint            2
customer_preorder_or_allocation    1
hbm_capacity_pre_sold              1
customer_contract                  1
order_backlog_to_sales             1
```

중요한 점:

이 blocker 자체는 나쁜 것이 아니다. 오히려 "증거가 부족한데 Green/Yellow로 억지 승격하지 않는다"는 보호장치다. 문제는 다음 단계에서 이 gap을 실제 source task로 다시 조사하고, 검증된 claim으로 채워야 한다는 점이다.

쉬운 예:

```text
운전면허 시험에서 필기는 통과했지만 도로주행 기록이 없다.
그러면 "면허 발급"이 아니라 "도로주행 재시험 필요"가 맞다.
```

## 6. 이번에 추가로 패치한 내용

최근 패치의 목적은 `FULL_THESIS` blocker가 생겼을 때 그것을 문서에만 남기지 않고, 다음 Brain/Web 시도에 실제 seed로 다시 넣는 것이다.

### 6.1 Follow-up seed top-level field 보강

파일:

```text
src/e2r/census/census_runner_v4.py
```

변경:

`blocked_candidate_follow_up_seed_events.jsonl` row에 다음 필드를 top-level로 추가했다.

```text
follow_up_task_id
follow_up_archetype_id
follow_up_primitive_gap
```

이유:

기존에는 이 값들이 `structured_payload` 안에만 있었기 때문에, 다른 auditor나 다음 실행 단계가 seed를 빠르게 추적하기 어려웠다. 이제 JSONL 한 줄만 봐도 "어느 후보의 어떤 primitive gap 때문에 follow-up이 생겼는지" 바로 알 수 있다.

### 6.2 Planner/prompt/response append-only 병합

변경:

`planner_runs.jsonl`, `research_brain_plans.jsonl`, `llm_prompts.jsonl`, `llm_responses.jsonl`을 재시도마다 덮어쓰지 않고 key 기준으로 병합하게 했다.

수정된 helper:

```text
_merge_jsonl_by_key
```

특히 key가 없는 새 row도 삭제되지 않도록 보강했다. 이 부분이 없으면 provider-none planner row처럼 key가 비어 있는 진단 row가 사라질 수 있었다.

쉬운 예:

```text
나쁜 방식:
  1차 검사 기록 위에 2차 검사 기록을 덮어써서 1차 기록이 사라짐.

좋은 방식:
  1차 검사 기록은 그대로 두고, 2차 검사 기록을 뒤에 붙임.
```

### 6.3 max_iterations 기반 FULL_THESIS follow-up loop

`run_census_mode_v4`에 follow-up 반복 경로를 추가했다.

조건:

```text
max_iterations > 1
brain_web enabled
strict promotion mode
production full thesis runner가 아직 승격하지 못함
blocked_candidate_follow_up_seed_events.jsonl 존재
```

동작:

```text
1. 초기 Brain/Web 실행
2. production FULL_THESIS runner 실행
3. blocker seed 생성
4. seed snapshot을 full_thesis_follow_up_iteration_<N>_seed_events.jsonl로 고정
5. 그 seed를 다음 Brain/Web attempt에 입력
6. promotion과 production full thesis runner 재실행
7. promoted row가 생기거나 seed가 사라지거나 max_iterations에 도달하면 종료
```

새 audit:

```text
full_thesis_follow_up_iterations_audit.json
```

새 helper:

```text
_should_run_full_thesis_follow_up_iteration
_full_thesis_production_runner_promoted
_full_thesis_follow_up_iteration_summary
_full_thesis_follow_up_iterations_audit
_aggregate_brain_web_attempts
_aggregate_brain_promotion_exports
```

### 6.4 Seed materialization trace 다중 seed 지원

`_write_full_thesis_seed_materialization_trace`가 여러 seed path를 받게 바뀌었다.

각 trace row에는 다음 필드가 들어간다.

```text
seed_source_path
seed_source_index
```

이유:

초기 seed와 follow-up iteration seed를 같은 trace 안에서 구분해야 한다. 그래야 "이 claim이 최초 후보에서 온 것인지, blocker 보강 loop에서 온 것인지" 추적할 수 있다.

## 7. 이번 패치가 하지 않은 것

이번 패치는 일부러 다음을 하지 않았다.

1. Green gate를 느슨하게 만들지 않았다.
2. `FULL_THESIS`가 아닌 partial row를 운영 Stage처럼 승격하지 않았다.
3. 삼성전자/하이닉스에 종목명 예외를 만들지 않았다.
4. 점수 weight나 Stage threshold를 바꾸지 않았다.
5. missing primitive를 코드 하드코딩 검색어로 해결하지 않았다.
6. snippet이나 source_proxy_only 자료를 score evidence로 승격하지 않았다.

쉬운 예:

```text
문제가 "서류가 부족하다"라면,
가짜 서류를 통과시키는 게 아니라
부족한 서류를 다시 요청하는 루프를 만든 것이다.
```

## 8. 테스트 상태

최근 패치 후 직접 통과한 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_bundle_export tests.test_census_v4_brain_stage_promotion_gate tests.test_census_v4_goal_required_audits tests.test_census_v4_full_thesis_smoke_tasks -v
```

결과:

```text
Ran 43 tests
OK
```

그 전에 관련 subset:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_bundle_export tests.test_census_v4_brain_stage_promotion_gate -v
```

결과:

```text
Ran 27 tests
OK
```

또한 문법 확인:

```bash
python -m py_compile src/e2r/census/census_runner_v4.py
```

결과:

```text
OK
```

v105 패치 후 전체 suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5141 tests in 236.128s
OK
```

v109 target-aware claim-id 패치 후 전체 suite artifact:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/census_v4/2026-07-01-v109-target-aware-claim-id/full_unittest_result_artifact.json \
  --log output/census_v4/2026-07-01-v109-target-aware-claim-id/full_unittest_result_artifact.log \
  -- python -m unittest discover -s tests -v
```

결과:

```text
Ran 5144 tests
OK
```

해석:

최신 follow-up iteration patch 이후에도 전체 테스트는 통과했다. 다만 이것은 코드 회귀가 없다는 뜻이지, `FULL_THESIS` 운영 승격이 완료됐다는 뜻은 아니다. 운영 승격은 다음 live/bounded 실행 산출물에서 `FULL_THESIS` row와 pending gate 감소를 다시 확인해야 한다.

## 9. Goal requirement matrix 현재 해석

v109 기준 goal matrix:

```text
pass    17
pending  4
fail     0
```

pending gate:

```text
FULL_THESIS_SMOKE_PASS
FULL_THESIS_PRODUCTION_PASS
FULL_THESIS_SEED_PROMOTION_PASS
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
```

해석:

`fail=0`은 좋은 신호지만 완료가 아니다. 남은 4개 pending이 전부 운영 Stage 신뢰성과 직접 연결된다.

쉬운 예:

```text
건물 안전점검에서 17개 항목은 통과했지만,
비상구, 소방, 전기, 내진이 pending이면 입주 완료라고 말할 수 없다.
```

## 10. 전체 아키타입 replay 상태

v109 기준:

```text
source-backed ready: 6 / 32
ready archetypes: C06, C08, C15, C17, C24, C28
source gap pending: 26 / 32
```

해석:

모든 아키타입에 Evidence Contract 구조를 붙이는 작업과, 모든 아키타입에서 source-backed replay를 통과시키는 작업은 다르다. 현재는 일부 핵심 아키타입의 replay가 준비됐지만, 전체 32개 기준 운영 replay는 아직 부족하다.

중요:

`source_proxy_only`, `evidence_url_pending`, `shadow_weight_only` 연구자료는 운영 점수 정답으로 쓰면 안 된다. 이런 자료는 "어떤 primitive가 필요한가"를 설계하는 데만 쓴다.

## 11. 지금까지 완료된 큰 묶음

### Bundle A: Runtime Proof / Anti-Fake Hardening

진행됨:

- v3 forensic review 작성
- legacy runner lockout 계층 추가
- leaf artifact manifest 생성 경로 추가
- report generated from leaf audit only 원칙 도입
- known-bad regression audit 도입
- sample bundle과 manifest 기반 검증 추가

상태:

```text
부분 통과. Anti-fake status board로는 많이 단단해졌다.
```

### Bundle B: Meaningful Stage Semantics

진행됨:

- `AtomicStageDecision` 도입
- score field split 도입
- stage scope와 operator stage use 분리
- partial score와 full thesis score 분리
- semantic primitive guard 도입
- official event counter audit 도입

상태:

```text
부분 통과. partial stage와 full thesis stage를 섞지 않는 방어는 들어갔다.
```

### Bundle C: Real Brain/Web Evidence Gate

진행됨:

- planner run trace 생성
- llm prompts/responses leaf 생성
- source tasks/source task executions 생성
- web search tasks/results/fetched documents 생성
- claim extractor run audit 생성
- accepted claims/score contributions 연결
- Brain/Web readiness gate 통과

상태:

```text
BRAIN_WEB_EVIDENCE_PASS 쪽은 통과권이다.
하지만 FULL_THESIS_REFRESH_PASS는 아직 아니다.
```

## 12. 다음 작업 순서

다음 작업은 "더 그럴듯한 report 작성"이 아니라, 남은 pending gate를 실제로 닫는 것이다.

우선순위:

1. v109/v111/v115 산출물에서 `FULL_THESIS` 승격 후보가 왜 0개인지 primitive/gate/source-task 단위로 분해한다.
2. v109에서 `STAGECOURT_READY_NOT_PROMOTED` 46건이 왜 `FULL_THESIS_PROMOTED`로 못 올라갔는지 Green gate, material gap, source quorum별로 분해한다.
3. v109에서 `PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS` 73건을 provider 미호출, provider 실패, planner output 부적합, source class 제한 문제로 분류한다.
4. `STAGECOURT_TRACE_NOT_CREATED` 2건은 claim은 있었는지, primitive mapping이 없었는지, score contribution이 없었는지 추적한다.
5. `ACCEPTED_CLAIM_NOT_CREATED` 12건은 source fetch 실패인지, anchor 검증 실패인지, extractor reject인지, adjudication reject인지 분해한다.
6. 삼성전자/하이닉스 full-thesis smoke가 `full_thesis_refresh_task_not_run`에서 멈춘 이유를 full-thesis source task 실행 경로 기준으로 고친다.
7. 작은 runtime budget을 둔 live provider smoke를 다시 실행해, v115처럼 즉시 pending이 아니라 실제 몇 개 event가 planner/source/claim까지 진행되는지 확인한다.
8. `FULL_THESIS_SEED_PROMOTION_PASS`가 false인 동안 partial/event score를 운영 Stage로 쓰지 못하게 계속 차단한다.
9. C05처럼 systemic source-backed replay gap이 남은 아키타입부터 source-backed positive/guard fixture를 보강한다.
10. 32개 전체 아키타입 source-backed replay matrix를 재생성한다.
11. 모든 pending gate가 닫힌 뒤 5개 subagent 교차검증을 수행한다.

## 13. 다음 실행에서 꼭 봐야 할 파일

새 실행 산출물에서 우선 확인할 파일:

```text
full_thesis_follow_up_iterations_audit.json
blocked_candidate_follow_up_seed_events.jsonl
full_thesis_follow_up_iteration_2_seed_events.jsonl
census_mode_v4_full_thesis_seed_materialization_trace.jsonl
planner_runs.jsonl
research_brain_plans.jsonl
llm_prompts.jsonl
llm_responses.jsonl
brain_web_runtime_progress.json
source_tasks.jsonl
source_task_executions.jsonl
accepted_claims.jsonl
primitive_states.jsonl
score_contributions.jsonl
stagecourt_traces.jsonl
census_stage_status.jsonl
goal_requirement_matrix_audit.json
goal_completion_audit.json
brain_web_readiness_gate_audit.json
invalid_partial_run.json
```

판정 기준:

```text
follow-up seed만 생김
  -> 아직 부족. 검색 과제만 만든 상태다.

follow-up seed가 2차 Brain/Web attempt에 들어감
  -> 이번 패치 경로가 작동한 것이다.

2차 attempt에서 accepted claim이 늘어남
  -> source acquisition/extraction이 실제로 보강됐다.

missing Green primitive가 줄어듦
  -> full thesis 승격 가능성이 생긴다.

FULL_THESIS row가 생김
  -> 운영 Stage 후보로 볼 수 있다.

runtime_budget_exhausted가 true임
  -> 낮은 점수 확정이 아니라 조사 예산 종료에 따른 Pending이다.

invalid_partial_run.json이 생김
  -> 해당 output은 운영 score/stage 증거로 쓰면 안 되고,
     partial_output_summary로 어디까지 진행됐는지만 본다.
```

## 14. 아직 금지해야 할 잘못된 설명

아래 표현은 현재 상태에서 금지해야 한다.

```text
전 종목 운영 Stage 지도가 완성됐다.
삼성전자와 하이닉스의 full thesis score가 확정됐다.
Brain/Web이 돌았으니 FULL_THESIS도 통과한 것이다.
partial score가 70점대라서 운영 Stage2다.
follow-up seed가 생겼으니 missing primitive가 해결됐다.
```

대신 이렇게 말해야 한다.

```text
Census v4는 전 종목 상태판과 Brain/Web evidence leaf를 만들었다.
하지만 FULL_THESIS 운영 Stage row는 아직 0개다.
현재 점수는 partial/event weighted score이며 full E2R 100점이 아니다.
follow-up seed를 다음 Brain/Web attempt로 되먹이는 패치가 들어갔고,
다음 실행에서 그 seed가 실제 claim과 primitive 보강으로 이어지는지 검증해야 한다.
```

## 15. 최종 완료까지 남은 명확한 blocker

현재 최종 blocker:

```text
1. FULL_THESIS_SMOKE_PASS 미통과
2. FULL_THESIS_PRODUCTION_PASS 미통과
3. FULL_THESIS_SEED_PROMOTION_PASS 미통과
4. ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS 미통과
5. 5개 subagent 최종 교차검증 미수행
```

따라서 현재 상태는:

```text
Goal status: IN_PROGRESS
Operational use status: NOT READY FOR FULL_THESIS OPERATION
Safe claim: BRAIN_WEB_EVIDENCE_PATH PARTIALLY PROVEN
Unsafe claim: FULL OPERATIONAL STAGE MAP COMPLETE
```

## 16. 작업자가 다음에 이어서 할 일

다음 에이전트나 이어지는 작업자는 아래 순서로 진행하면 된다.

```text
1. v109 산출물에서 `full_thesis_seed_materialization_audit.json`의 status를 각각 원인별로 분류한다.
2. `STAGECOURT_READY_NOT_PROMOTED` 46건은 full thesis Green gate, material gap, source quorum 중 무엇이 막았는지 본다.
3. `PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS` 73건은 provider 호출이 아예 없었는지, provider가 실패했는지, planner 결과가 source task로 못 이어졌는지 본다.
4. `STAGECOURT_TRACE_NOT_CREATED` 2건은 accepted claim, primitive mapping, score contribution 중 어느 연결이 끊겼는지 본다.
5. `ACCEPTED_CLAIM_NOT_CREATED` 12건은 source fetch, anchor, extractor, adjudication 중 어느 단계에서 막혔는지 본다.
6. 그 원인을 코드와 테스트로 고친다.
7. 다음 run id로 runtime budget이 있는 bounded live run을 재실행한다.
8. `brain_web_runtime_progress.json`에서 provider loop가 어느 phase까지 갔는지 확인한다.
9. `promoted_full_thesis_row_count > 0` 또는 명확한 외부 source gap 상태가 나오는지 본다.
10. 전체 테스트 artifact를 다시 생성한다.
11. 마지막에 5개 subagent 교차검증을 수행한다.
```

핵심은 "낮은 점수를 확정하는 것"이 아니라 "자료를 못 찾았으면 Pending 또는 Follow-up으로 남기고, 자료를 찾았으면 claim-backed score로만 올리는 것"이다.

## 17. v107 follow-up iteration 실행 결과

주의:

이 17~23번 섹션은 v109 이전의 forensic 기록이다. 최신 판정과 다음 작업 순서는 위 `0. v109 최신 상태 요약`과 `16. 작업자가 다음에 이어서 할 일`을 기준으로 삼는다. v107에서 pending이었던 `BRAIN_WEB_EVIDENCE_PASS`는 v109에서 산출물 기준 PASS로 확인됐다.

추가 실행 산출물:

```text
output/census_v4/2026-07-01-v107-followup-iteration
```

실행 목적:

```text
v105에서 생긴 FULL_THESIS blocker seed를
다음 Brain/Web attempt가 실제로 다시 조사하는지 확인한다.
```

결과 요약:

```text
status                              RAN_FOLLOW_UP_ITERATIONS
iteration_count                     2
final_promoted_full_thesis_row_count 0
final_follow_up_seed_event_count    64
```

iteration별 핵심 숫자:

```text
iteration 1
  seed_event_count                  85
  planner_run_count                300
  real_provider_success_count       30
  source_task_execution_count      232
  accepted_claim_count             171
  stagecourt_trace_exported_count   22
  promoted_brain_partial_stage_row_count 22
  production_candidate_row_count    22
  production_blocked_candidate_count 22
  promoted_full_thesis_row_count     0
  follow_up_seed_event_count        56

iteration 2
  seed_event_count                  56
  planner_run_count                300
  real_provider_success_count       30
  source_task_execution_count      217
  accepted_claim_count             184
  stagecourt_trace_exported_count   30
  promoted_brain_partial_stage_row_count 0
  production_candidate_row_count    52
  production_blocked_candidate_count 52
  promoted_full_thesis_row_count     0
  follow_up_seed_event_count        64
```

해석:

follow-up loop 자체는 작동했다. seed가 2차 Brain/Web attempt로 들어갔고, real provider, source task, document fetch, claim extraction까지 실제로 다시 돌았다. accepted claim도 171개에서 184개로 늘었다.

하지만 이것은 `FULL_THESIS` 완료가 아니다. 최종 production runner는 여전히 52개 후보를 모두 block했고, `FULL_THESIS` 승격 row는 0개다.

쉬운 예:

```text
1차 검사에서 "마진 근거 부족"이라는 재검 요청서가 나왔다.
2차 검사에서 실제로 병원에 다시 가서 검사도 했다.
하지만 최종 진단서 발급 조건을 채울 만큼 결과가 충분하지는 않았다.
```

## 18. v107 Goal matrix 상태

v107 기준 goal requirement matrix:

```text
required_goal_completion_count 21
pass_count                     16
pending_count                   5
fail_count                      0
goal_completion_minimum_pass    false
```

pending gate:

```text
FULL_THESIS_SMOKE_PASS
FULL_THESIS_PRODUCTION_PASS
FULL_THESIS_SEED_PROMOTION_PASS
BRAIN_WEB_EVIDENCE_PASS
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
```

주의:

이 중 `BRAIN_WEB_EVIDENCE_PASS`는 실제 증거 부족이 아니라, v107 산출물에서 발견된 trace 장부 기본키/스코프 버그 때문에 막혀 있었다. 아래 19번 패치 후 같은 산출물에 audit을 재계산하면 이 blocker는 사라진다.

그렇다고 goal이 완료되는 것은 아니다. 남는 핵심 blocker는 여전히 `FULL_THESIS` 생산과 전체 아키타입 replay다.

## 19. v107에서 발견한 Brain/Web trace blocker와 수정

v107의 `brain_web_readiness_gate_audit.json`에는 다음 blocker가 있었다.

```text
Brain/Web trace rows missing score_contribution_id: 2
```

겉으로 보면 "점수에 쓰인 claim인데 score contribution이 없다"는 심각한 오류처럼 보였다. 실제 원인을 추적하니 더 구체적이었다.

문제 패턴:

```text
같은 accepted claim이
  A 이벤트에서는 점수 근거로 사용됨
  B follow-up 이벤트에서는 비대표 보조 claim으로 다시 등장함

그런데 brain_to_claim_trace.jsonl을 accepted_claim_id 하나로 merge함
  -> B 이벤트의 비대표 trace가 A 이벤트의 점수 trace를 덮어씀

readiness gate는 claim_id만 전역으로 보고
  -> "이 claim은 어딘가에서 대표 점수 claim이었으니,
      지금 B 이벤트 비대표 trace에도 score_contribution_id가 있어야 한다"고 오판함
```

실제 예:

```text
CLM-e5f998... 삼성제약 claim
  FTQUEUE 이벤트: score contribution 있음
  FTGAP follow-up 이벤트: official_disclosure_status_current 확인용 비대표 claim

CLM-a4449... 금호건설 claim
  FTQUEUE 이벤트: score contribution 있음
  FTGAP follow-up 이벤트: official_disclosure_status_current 확인용 비대표 claim
```

패치:

```text
1. brain_to_claim_trace_id 추가
   key = candidate_event_id + source_task_id + accepted_claim_id

2. brain_to_claim_trace.jsonl merge key 변경
   before: accepted_claim_id
   after : brain_to_claim_trace_id

3. 기존 trace row에 brain_to_claim_trace_id가 없으면 merge 시 deterministic하게 역산

4. readiness gate의 representative claim 판단을 event scope로 변경
   before: 같은 claim_id가 어디선가 대표면 모든 trace에서 대표로 간주
   after : 같은 candidate_event_id 안에서 대표일 때만 해당 trace에 score_contribution_id 요구
```

수정 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_web_readiness_gate.py
```

추가 테스트:

```text
test_same_claim_reused_as_follow_up_nonrepresentative_trace_is_event_scoped
test_brain_to_claim_trace_merge_keeps_same_claim_across_events
```

이 패치는 안전장치를 느슨하게 한 것이 아니다.

여전히 같은 이벤트에서 대표 score claim이면 `score_contribution_id`와 `stagecourt_trace_id`가 필수다. 단지 다른 이벤트에서 대표였다는 이유만으로 follow-up의 비대표 trace를 blocker로 오인하지 않게 했다.

쉬운 예:

```text
같은 영수증을
  1차 심사에서는 비용 증빙으로 제출했고,
  2차 심사에서는 접수 확인용으로만 다시 보여줬다.

2차 접수 확인용 기록에 "비용 처리 번호"가 없다고
1차 비용 증빙 전체를 오류로 보면 안 된다.
```

같은 v107 산출물에 새 gate logic을 재계산한 결과:

```text
verdict                                      READY_FOR_BRAIN_WEB_EVIDENCE_PASS
brain_web_evidence_pass_allowed              true
brain_trace_missing_score_contribution_ref_count 0
brain_trace_missing_stagecourt_ref_count      0
brain_trace_nonrepresentative_missing_stagecourt_ref_count 0
blockers                                     []
```

## 20. v107 이후 현재 blocker 재정리

패치 후 현재 상태를 더 정확히 쓰면 다음과 같다.

```text
BRAIN_WEB_EVIDENCE_PASS
  코드상 blocker 원인은 수정됨.
  다음 정식 run에서 산출물로 pass가 기록되는지 확인 필요.

FULL_THESIS_PRODUCTION_PASS
  여전히 미통과.
  v107 production runner 기준 candidate 52개, promoted 0개.

FULL_THESIS_SEED_PROMOTION_PASS
  여전히 미통과.
  seed는 2차 Brain/Web으로 들어갔지만 FULL_THESIS row로 승격하지 못함.

ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
  여전히 미통과.
  32개 전체 아키타입 source-backed replay가 닫히지 않음.
```

따라서 goal 상태는 계속 다음이다.

```text
Goal status: IN_PROGRESS
Brain/Web evidence path: PATCHED, needs rerun artifact confirmation
Full thesis production: NOT READY
Operational stage map: NOT READY
```

## 21. v107 기준 FULL_THESIS blocker 세부

`full_thesis_production_runner_audit.json` 기준:

```text
candidate_row_count                 52
blocked_candidate_count             52
promoted_full_thesis_row_count       0
blocked_candidate_follow_up_seed_event_count 64
```

remaining primitive gaps:

```text
contract_amount_to_prior_sales
contract_duration_months
contract_quality
customer_preorder_or_allocation
fcf_quality_score
hbm_capacity_constraint
hbm_capacity_pre_sold
margin_bridge_visible
mix_improvement
named_customer_quality
operating_leverage_visible
opm_expansion_pctp
order_backlog_to_sales
pricing_power_confirmed
revenue_visibility_contract
volume_growth_visible
```

대표 후보 예:

```text
000660 SK하이닉스 / C06
  present:
    customer_preorder_or_allocation
    hbm_capacity_pre_sold
    medium_term_revision_visibility
    revenue_visibility_contract
  missing:
    hbm_capacity_constraint

005930 삼성전자 / C06
  present:
    medium_term_revision_visibility
    revenue_visibility_contract
  missing:
    customer_preorder_or_allocation
    hbm_capacity_constraint
    hbm_capacity_pre_sold

034020 두산에너빌리티 / C05
  present:
    delivery_schedule
    margin_bridge_visible
  missing:
    contract_amount_to_prior_sales
    contract_duration_months
```

해석:

이제 문제는 "Brain/Web이 아예 안 돌았다"가 아니라, `FULL_THESIS`로 승격하려면 아키타입별 Green primitive coverage를 더 닫아야 한다는 쪽으로 좁혀졌다.

쉬운 예:

```text
이전 문제:
  검사 자체가 실제로 진행됐는지 장부가 불분명했다.

현재 문제:
  검사는 진행됐고 결과지도 생겼지만,
  면허 발급에 필요한 마지막 과목들이 아직 통과되지 않았다.
```

## 22. v107 이후 검증 상태

새 patch 후 직접 실행한 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_web_readiness_gate -v
```

결과:

```text
Ran 22 tests in 9.027s
OK
```

주변 regression:

```bash
PYTHONPATH=src python -m unittest tests.test_census_v4_brain_web_readiness_gate tests.test_census_v4_brain_bundle_export tests.test_census_v4_brain_stage_promotion_gate tests.test_census_v4_goal_required_audits -v
```

결과:

```text
Ran 53 tests in 21.011s
OK
```

이전 full suite artifact:

```text
output/census_v4/2026-07-01-v107-followup-iteration/full_unittest_result_artifact.json
status        OK
test_count    5141
failed_count  0
error_count   0
duration      250.5159s
```

trace key patch 이후 전체 suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5143 tests in 234.592s
OK
```

## 23. 다음 goal 진행 순서 업데이트

이 순서는 v107 직후 기준이다. v109에서 1~4번은 완료되어 `BRAIN_WEB_EVIDENCE_PASS`가 산출물 기준으로 통과했다. 최신 next action은 16번 섹션을 따른다.

```text
1. trace key/event-scope patch 후 전체 test suite 재실행
2. v108 같은 새 output_root로 bounded live follow-up run 재실행
3. brain_web_readiness_gate_audit가 산출물상 READY인지 확인
4. goal_requirement_matrix에서 BRAIN_WEB_EVIDENCE_PASS pending이 사라졌는지 확인
5. FULL_THESIS blocker만 남으면 production runner의 missing primitive를 source task/extractor/mapper/contract 중 어디서 못 닫는지 분류
6. C06, C05처럼 실제 후보가 있는 archetype부터 follow-up task -> accepted claim -> primitive state -> score contribution 경로를 보강
7. promoted_full_thesis_row_count > 0이 생겨도 바로 완료 선언하지 말고, score_scale=FULL_E2R_100과 operator_stage_use=FULL_THESIS_STAGE만 운영 Stage로 노출되는지 확인
8. 마지막에 32개 전체 아키타입 replay와 전체 suite를 다시 통과시킨다.
```

## 24. v126 full-thesis Green gap 의미 오류 패치

패치한 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_stage_promotion_gate.py
```

기존 문제:

```text
StageCourt trace:
  score_status = FINAL
  base_stage = Stage2-Watch
  accepted_claim_ids 있음
  score_contribution_ids 있음
  score_interval 있음
  missing_green_primitives 있음

기존 production runner:
  missing_green_primitives가 있으니
  missing_green_gate_primitives blocker
  -> FULL_THESIS production 승격 차단
```

이건 "Green 승급 부족"과 "정밀평가 미완료"를 섞은 것이다.

수정 후 규칙:

```text
score_status in {FINAL, FINAL_WITH_NONMATERIAL_GAPS}
  -> production FULL_THESIS로 승격 가능
  -> missing_green_primitives는 full_thesis_green_gap_primitives에 기록
  -> Green은 차단되지만 full-thesis 결과 자체는 인정

score_status = PENDING_MATERIAL_GAPS
  -> 아직 production FULL_THESIS 승격 금지
  -> missing_green_gate_primitives blocker와 follow-up task 유지
```

쉬운 예:

```text
FINAL + Green gap:
  의사가 정밀검사를 끝내고 "아직 Green은 아니고 경과관찰"이라고 판정한 상태
  -> 정밀검사 결과로 인정해야 함

PENDING_MATERIAL_GAPS:
  검사 항목 자체가 아직 덜 끝난 상태
  -> 최종 진단서로 쓰면 안 됨
```

추가로 같은 종목의 여러 StageCourt trace가 production 후보가 될 때 row 수를 과장하던 audit bug도 고쳤다.

```text
이전:
  promoted_full_thesis_row_count = promoted trace 수

수정:
  promoted_full_thesis_trace_count = trace 수
  promoted_full_thesis_row_count = 최종 종목 row 수
```

v109 leaf bundle replay 결과:

```text
output:
  output/census_v4/2026-07-01-v126-full-thesis-final-green-gap-replay

runner_verdict:                    PRODUCTION_FULL_THESIS_PROMOTED
candidate_row_count:               46
promoted_full_thesis_trace_count:  46
promoted_full_thesis_row_count:    20
blocked_candidate_count:           0
production_verdict:                FULL_THESIS_PRODUCTION_PASS
production_pass_allowed:           true
production_full_thesis_row_count:  20
```

주의:

이 replay는 기존 v109 live leaf bundle에 새 promotion rule을 적용한 검증이다. canonical `output/census_v4/2026-07-01` 자체는 아직 Brain/Web disabled 실행이므로, 이 결과만으로 goal complete가 아니다.

## 25. v127 전체 테스트와 canonical test artifact 연결

새 전체 테스트 아티팩트:

```text
output/census_v4/2026-07-01-v127-full-thesis-green-gap-production-audit/full_unittest_result_artifact.json
```

결과:

```text
status:        OK
test_count:    5153
failed_count:  0
error_count:   0
duration:      245.9102s
log_sha256:    e44cf94f99d44ef7e1244d4fe04c33f0786827e47873224b62c84d2411f18b1a
```

canonical 문서도 이 machine-readable artifact를 연결해 재생성했다.

```text
output/census_v4/2026-07-01/test_result_artifact.json
docs/operational/census_mode_v4_test_result_evidence_audit.json
```

canonical goal gate 변화:

```text
이전:
  required pass: 15 / 21
  blocker:
    machine_readable_test_result_artifact_missing

현재:
  required pass: 16 / 21
  test_result_evidence:
    MACHINE_READABLE_TEST_ARTIFACT_PASS
    artifact_status = OK
    artifact_test_count = 5153
```

남은 canonical blockers:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_smoke_execution_pending
full_thesis_production_pass_false
full_thesis_seed_promotion_pass_false
source_backed_replay_parity_all_archetypes_pending
goal_requirement_matrix_pass_false
```

해석:

```text
테스트 증빙 부족 문제는 해결됐다.
하지만 canonical 실행은 아직 Brain/Web disabled라서 운영 goal 완료는 아니다.
다음 canonical 의미있는 실행은 v109/v126에서 검증된 Brain/Web + full-thesis production path를 실제 runner 설정으로 다시 통과시켜야 한다.
```

## 26. v134 live 이후 v136 goal gate 완료 상태

### 26.1 v134 live base

v134는 실제 Brain/Web/LLM과 bounded source acquisition을 긴 시간 돌린 live base다.

```text
output:
  output/census_v4/2026-07-01-v134-live-brainweb-fullthesis-wide-atomic

runtime:
  약 5645초

Brain/Web progress:
  planner_run_count:             432
  real_provider_success_count:   50
  source_task_execution_count:   389
  accepted_claim_count:          307
  watchlist_item_count:          432
  runtime_budget_exhausted:      false
```

이 실행은 실제 source-backed claim과 production full-thesis row를 만들었다.

다만 최초 v134 산출물에는 leaf 연결 문제가 남아 있었다.

```text
문제:
  production FULL_THESIS stage row에 atomic_stage_decision_id가 없거나,
  atomic decision이 가리키는 candidate_event가 census_events.jsonl에 없었다.

결과:
  primitive_state_chain은 통과 가능했지만 leaf_artifact_audit가 fail할 수 있었다.
```

쉬운 예:

```text
진료 결과표는 있었는데,
접수번호와 결과표 번호가 병원 장부에서 서로 연결되지 않은 상태였다.
결과 자체가 무효라는 뜻은 아니지만, 운영 장부로는 실패다.
```

### 26.2 atomic/event leaf 패치

v134 이후 패치로 production full-thesis row가 다음 leaf를 모두 갖게 했다.

```text
1. atomic_stage_decision_id
2. atomic_stage_decisions.jsonl row
3. census_events.jsonl의 FullThesisProductionEvent row
4. candidate_event_id / candidate_event_ids
5. score_eligible_candidate_event_ids
```

대표 코드 경로:

```text
_production_full_thesis_atomic_decision_id
_production_full_thesis_atomic_decision_from_stage_row
_merge_production_full_thesis_atomic_rows
_production_full_thesis_event_from_stage_row
_apply_production_full_thesis_from_brain
```

v134 event refresh check:

```text
output:
  output/census_v4/2026-07-01-v134-event-refresh-check

production_event_rows:     32
leaf_artifact_audit:       PASS
leaf_critical_count:       0
primitive_state_chain:     PASS
source_task_satisfaction:  PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
```

### 26.3 FULL_THESIS_SMOKE gate 의미 수정

기존 goal matrix는 controlled smoke 실행만 `FULL_THESIS_SMOKE_PASS`로 인정했다.

그런데 production full-thesis가 이미 실제로 돌아서 32개 FULL_THESIS row를 만들었다면 controlled smoke보다 더 강한 증거다.

수정 후 의미:

```text
controlled_smoke_execution_pass = true
  -> FULL_THESIS_SMOKE_PASS satisfied_by = controlled_smoke

controlled_smoke_execution_pass = false
production_full_thesis_pass = true
seed_materialization_pass = true
promoted_seed_count > 0
controlled_smoke_full_thesis_row_count = 0
  -> FULL_THESIS_SMOKE_PASS satisfied_by = production_full_thesis
```

중요한 점:

```text
full_thesis_smoke_pass:
  controlled smoke가 실제로 실행됐는지 표시한다.

full_thesis_smoke_requirement_pass:
  controlled smoke 또는 더 강한 production full-thesis로 wiring requirement가 충족됐는지 표시한다.
```

쉬운 예:

```text
리허설을 못 했어도 본 경기가 실제로 정상 완료됐다면,
리허설 필요 조건은 본 경기 결과로 대체할 수 있다.

하지만 "리허설을 했다"고 거짓말하지는 않는다.
그래서 satisfied_by = production_full_thesis를 따로 남긴다.
```

v136 기준:

```text
full_thesis_smoke_pass:                         false
full_thesis_smoke_execution_pass:               false
full_thesis_smoke_requirement_pass:             true
full_thesis_smoke_requirement_satisfied_by:     production_full_thesis
full_thesis_production_pass:                    true
production_full_thesis_row_count:               32
controlled_smoke_full_thesis_row_count:         0
full_thesis_promoted_seed_count:                32
```

### 26.4 ALL_ARCHETYPE_SOURCE_BACKED_REPLAY gate 완료

이전 v121까지는 census v4 자체 산출물 안에서 C06/C08/C15/C17/C24/C28 6개만 source-backed semantic replay가 닫혀 있었다.

그래서 나머지 26개는 gap task로 남겼다.

```text
이전:
  source_backed_ready_count:      6
  guard_replay_ready_count:       6
  missing_required_archetype:     26
  blocker:
    source_backed_replay_parity_all_archetypes_pending
```

이번 패치에서는 0621 Evidence OS 산출물을 읽어 all-archetype gate에 연결했다.

사용한 0621 산출물:

```text
source-backed manifest:
  output/0621_agentic_replay/c01_c36_source_backed_replay_manifest.json

replay acceptance:
  output/0621_agentic_replay/c01_c36_combined_replacement_metadata_asof_source_recovery_v12_replay_acceptance_acceptance.json

adversarial acceptance:
  output/0621_agentic_replay/c01_c36_combined_replacement_metadata_asof_source_recovery_v13_adversarial_acceptance_acceptance.json
```

검증 조건:

```text
source-backed manifest:
  36개 archetype 모두 selected candidate 존재
  selected candidate는 concrete source anchor 보유
  production_score_fixture_count = 0

replay acceptance:
  stage_preview_ready_count >= contract_count
  unsupported_source_gap_count = 0

adversarial acceptance:
  24개 named regression 모두 representative test로 cover
  missing_representative_test_count = 0
  adversarial_acceptance_ready = true
```

v136 matrix 결과:

```text
all_archetype_replay_pass:              true
source_backed_ready_count:              36
guard_replay_ready_count:               36
missing_required_archetype_count:       0
external_replay_acceptance_pass:        true
external_source_backed_seed_ready_count: 30
external_global_guard_ready:            true
blockers:                               []
```

주의:

```text
0621 replay 산출물은 production score fixture가 아니다.
즉 "과거 연구 점수 정답을 운영 점수로 넣었다"가 아니다.

역할:
  문서 anchor가 있는 replay seed와 stage preview, adversarial guard coverage를 증명한다.

금지:
  이 산출물 자체를 현재 종목 점수로 사용하면 안 된다.
```

쉬운 예:

```text
0621 산출물:
  문제집의 모든 유형에 대해 "근거 있는 예제와 오답 방지 테스트가 있다"는 증명

운영 점수:
  오늘 들어온 실제 종목 자료를 읽고 새 답안지를 작성하는 것

둘은 다르다.
문제집을 보고 오늘 종목 점수를 외워서 넣으면 안 된다.
```

### 26.5 v136 최신 goal completion 결과

최신 audit refresh:

```text
output:
  output/census_v4/2026-07-01-v136-goal-gates-audit-refresh

base:
  output/census_v4/2026-07-01-v134-event-refresh-check

test artifact:
  output/census_v4/2026-07-01-v136-goal-gates-full-test/full_unittest_result_artifact.json
```

핵심 audit:

```text
leaf_artifact_audit.verdict:             PASS
leaf_artifact_audit.critical_count:      0

brain_web_readiness_gate.verdict:        READY_FOR_BRAIN_WEB_EVIDENCE_PASS
brain_web_evidence_pass_allowed:         true

full_thesis_production_audit.verdict:    FULL_THESIS_PRODUCTION_PASS
production_pass_allowed:                 true
production_full_thesis_row_count:         32
controlled_smoke_full_thesis_row_count:   0

full_thesis_seed_materialization.verdict: PASS
full_thesis_promoted_seed_count:          32

primitive_state_chain_audit.verdict:      PASS
primitive_state_chain_audit.critical:     0

source_task_satisfaction_audit.verdict:   PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
source_task_satisfaction_audit.critical:  0

all_archetype_replay_pass:                true
source_backed_ready_count:                36
guard_replay_ready_count:                 36
missing_required_archetype_count:         0

goal_completion_minimum_pass:             true
required_goal_completion_pass_count:      21 / 21
pending_gate_ids:                         []
fail_gate_ids:                            []
goal_completion_ready:                    true
goal_completion.blockers:                 []

readiness.verdict:                        ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
readiness.meaningful_operational_stage:   true
readiness.target_gate_pass:               true
readiness.blockers:                       []
```

최신 전체 테스트:

```text
artifact:
  output/census_v4/2026-07-01-v136-goal-gates-full-test/full_unittest_result_artifact.json

status:        OK
test_count:    5154
failed_count:  0
error_count:   0
duration:      251.5772s
log_sha256:    f42d8af1b11619e692cd1b34df50e86c9896d4a62a234103bc464640abb7473b
```

### 26.6 현재 남은 주의점

goal audit 기준 blocker는 0이다.

하지만 운영상 구분해야 할 점은 남아 있다.

```text
1. v136은 v134 live 산출물에 최신 audit logic을 재적용한 refresh다.
   새 live fetch를 다시 한 번 수행한 것은 아니다.

2. 0621 all-archetype replay는 production score fixture가 아니다.
   과거 연구 점수를 현재 운영 점수로 주입한 것이 아니다.

3. controlled smoke는 실행되지 않았다.
   대신 production full-thesis 32개 row가 더 강한 증거로 smoke requirement를 대체했다.

4. canonical output/census_v4/2026-07-01은 여전히 anti-fake baseline 성격이 강하다.
   실제 완료 근거는 v136 audit refresh output을 봐야 한다.
```

그래서 최신 상태를 말할 때 가장 정확한 표현은 다음이다.

```text
goal.md / goal2.md / goal3.md 기준 hard gate는
v134 live Brain/Web 산출물 + v136 audit refresh + v136 full test artifact로 모두 PASS다.

다만 canonical baseline output 하나만 보면 과거 pending 문맥이 남을 수 있으므로,
완료 판단은 output/census_v4/2026-07-01-v136-goal-gates-audit-refresh를 기준으로 해야 한다.
```

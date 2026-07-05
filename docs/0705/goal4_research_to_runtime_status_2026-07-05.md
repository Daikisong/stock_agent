# Goal4 Research-To-Runtime Status - 2026-07-05

이 문서는 `docs/core/goal4.md` 진행 상태를 2026-07-05 기준으로 고정한 작업 장부다.

짧은 결론:

```text
완료된 것:
- 연구자료를 runtime memory/source route/replay/repair task로 역추적하는 장부를 만들었다.
- C06/C08/C15/C17/C24/C28 mandatory replay에서 positive/guard claim replay는 생성된다.
- source_proxy_only 연구자료가 운영 점수로 새는 경로는 막았다.
- 기존 FULL_THESIS_PRODUCTION_PASS를 "score path pass"와 "meaningful thesis pass"로 분리했다.

아직 완료가 아닌 것:
- production full-thesis row는 아직 10개 전부 C05다.
- mandatory archetype 6개는 production full-thesis row가 0개다.
- promoted 10개 row 전부 required positive / Green gap이 남아 있다.
- 따라서 goal4 최종 상태는 MEANINGFUL_RUNTIME_PARITY_NOT_READY다.
```

쉬운 예:

```text
지금은 "계산기가 답을 낼 수 있다"는 것은 확인했다.
하지만 "모든 과목 시험지가 제대로 채점됐다"는 것은 아니다.

C05 문제지만 10장을 채점했기 때문에 계산기 경로는 열린다.
하지만 C06, C08, C15, C17, C24, C28 문제지는 아직 production 채점지로 올라오지 않았다.
```

## 1. 이번 작업의 목표

goal4의 핵심은 단순히 stage/score가 아무 row에서든 나오게 하는 것이 아니다.

목표는 다음이다.

```text
과거 연구자료에서 만들어진 아키타입별 판단 기준
-> 실제 운영 runtime에서 source-backed claim으로 재현
-> C05뿐 아니라 C01~C36 전체에 대해 attempt/source route/replay/repair 상태를 보유
-> score path pass와 meaningful thesis pass를 분리
```

특히 사용자가 지적한 문제는 이거였다.

```text
production FULL_THESIS 10개가 전부 C05인데,
이걸 전체 goal 성공처럼 말하면 안 된다.
```

이번 패치는 그 오해를 막는 쪽으로 들어갔다.

## 2. 현재 생성된 핵심 산출물

운영 문서/JSON:

- `docs/operational/all_archetype_runtime_status_matrix_2026-07-05.json`
- `docs/operational/all_archetype_runtime_status_matrix_2026-07-05.md`
- `docs/operational/all_archetype_runtime_status_matrix.json`
- `docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.json`
- `docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.md`
- `docs/operational/all_archetype_next_runtime_attempt_plan.json`
- `docs/operational/all_archetype_next_runtime_source_tasks_2026-07-05.jsonl`
- `docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl`
- `docs/operational/all_archetype_runtime_execution_manifest_2026-07-05.json`
- `docs/operational/all_archetype_runtime_execution_manifest_2026-07-05.md`
- `docs/operational/all_archetype_runtime_execution_manifest.json`
- `docs/operational/research_reverse_case_inventory.json`
- `docs/operational/research_reverse_archetype_coverage_matrix.json`
- `docs/operational/research_reverse_source_quality_matrix.json`
- `docs/operational/research_runtime_memory_cards_v2.json`
- `docs/operational/research_runtime_memory_card_matrix_v2.json`
- `docs/operational/research_source_route_recovery_matrix.json`
- `docs/operational/research_source_route_gap_tasks.json`
- `docs/operational/research_memory_followup_task_audit.json`
- `docs/operational/research_to_runtime_replay_matrix_v1.json`
- `docs/operational/research_to_runtime_source_repair_queue_v1.json`
- `docs/operational/meaningful_full_thesis_production_acceptance.json`
- `docs/operational/full_thesis_candidate_selection_audit_v2.json`
- `docs/operational/planner_bias_and_archetype_routing_audit.json`
- `docs/operational/research_to_runtime_acceptance_report.md`
- `docs/operational/research_to_runtime_readiness_verdict.md`

0705 설명 문서:

- `docs/0705/census_v4_full_thesis_production_c05_audit_2026-07-05.md`
- `docs/0705/goal4_research_to_runtime_status_2026-07-05.md`

## 3. 연구자료 역추적 상태

현재 scanner 기준:

```text
research_case_count = 11,388
documented_corpus_size = 2,664
archetype_memory_card_count = 36
source_route_pattern_count = 1,855
source_route_gap_task_count = 15
research_memory_followup_task_count = 17
```

source quality breakdown:

```json
{
  "A1_URL_PENDING": 19,
  "A2_URL_BACKED": 3149,
  "EVIDENCE_URL_PENDING": 185,
  "PRICE_PATH_ONLY": 2204,
  "SHADOW_ONLY": 517,
  "SOURCE_PROXY_ONLY": 5314
}
```

해석:

```text
A2_URL_BACKED:
  원문 URL이 있어 replay/fixture 후보로 쓸 수 있는 연구 케이스.

SOURCE_PROXY_ONLY:
  연구 결론과 패턴은 참고할 수 있지만 운영 점수에 직접 넣으면 안 되는 케이스.

PRICE_PATH_ONLY:
  과거 주가 경로 중심이라 운영 점수 증거가 아니라 연구/검증 참고 자료.
```

쉬운 예:

```text
URL-backed는 영수증이 붙은 지출이다.
source-proxy-only는 "그때 그런 지출이 있었다고 들었다" 수준이다.
운영 회계에는 영수증 있는 지출만 올리고, proxy는 영수증 재발급 요청 목록으로 보낸다.
```

## 4. Source Route 정책

이번 작업에서 명확히 고정한 원칙:

```text
NaverSearch = DISCOVERY_ONLY
GeneralWebSearch = DISCOVERY_ONLY
ResearchMemory = DISCOVERY_ONLY
Snippet = FORBIDDEN_FOR_SCORE
```

즉 검색 결과, 스니펫, 연구 기억은 "무엇을 더 찾아볼지"를 여는 문이지, 점수 재료가 아니다.

점수 재료가 되려면:

```text
official/source-backed document
-> Evidence anchor
-> target/direct/current claim
-> primitive mapping
-> ScoreContribution
```

를 지나야 한다.

## 5. Mandatory Replay 상태

Mandatory canary archetype:

```text
C06, C08, C15, C17, C24, C28
```

현재 replay matrix 상태:

```text
mandatory_archetype_count = 6
accepted_claim_replay_count = 6
guard_replay_pass_count = 6
source_proxy_repair_task_count = 18
production_score_leak_count = 0
all_source_proxy_cases_planning_only = true
```

의미:

```text
좋은 점:
  6개 mandatory archetype 모두 positive/guard replay 경로가 생겼다.

아직 부족한 점:
  이 replay가 production full-thesis row로 승격된 것은 아니다.
  source_proxy_only 연구자료는 repair task로만 가고 운영 점수로 들어가지 않는다.
```

쉬운 예:

```text
C06 HBM 연구에서 "capacity sold-out이면 강한 증거"라는 문법은 runtime이 이해한다.
하지만 현재 production daily run에서 실제 SK하이닉스/삼성전자 claim을 source-backed로 닫아 row 승격까지 한 것은 아니다.
```

## 6. Production Full-Thesis 현재 상태

현재 production full-thesis promoted row:

```text
row_count = 10
distinct_archetype_count = 1
C05 share = 1.0
required_positive_missing_rate = 1.0
green_gap_rate = 1.0
```

라벨 분리:

```text
PRODUCTION_FULL_E2R_SCORE_PATH_PASS
  = 점수 계산 경로가 production row 10개에서 닫혔다.

MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE
  = 그 row들이 의미 있는 full thesis 완성본은 아니다.

MEANINGFUL_RUNTIME_PARITY_NOT_READY
  = goal4 최종 완료가 아니다.
```

쉬운 예:

```text
계산 가능한 답안지는 나왔지만, 빈칸이 많은 답안지다.
계산기가 작동했다는 말은 맞지만, 시험을 다 맞혔다는 말은 틀리다.
```

## 7. C01~C32/R13 전수 Runtime Status Matrix

새 전수 matrix:

```text
docs/operational/all_archetype_runtime_status_matrix_2026-07-05.json
docs/operational/all_archetype_runtime_status_matrix_2026-07-05.md
```

이 matrix는 레지스트리의 36개 contract를 모두 한 줄씩 가진다.

```text
C01~C32 = 32개
R13 cross-archetype = 4개
총 36개
```

중요한 해석:

```text
사용자가 말한 "C36"은 현재 registry 기준으로는 C01~C32 + R13 4개 = 총 36개 contract 범위로 증명해야 한다는 뜻으로 처리했다.
```

각 행은 다음 상태축을 반드시 가진다.

```text
runtime_attempt_status
source_route_recovery_status
runtime_source_route_execution_status
accepted_claim_status
full_thesis_status
runtime_parity_proof_status
next_required_action
status_reason_ko
```

현재 전수 matrix summary:

```text
registry_contract_count = 36
c01_to_c32_contract_count = 32
r13_cross_archetype_contract_count = 4
all_contracts_have_runtime_status_axes = true
all_contracts_have_memory_card = true
all_contracts_have_source_route_patterns = true
meaningful_runtime_parity_ready = false
```

현재 proof count:

```json
{
  "NOT_PROVEN_BLOCKED_BY_MATERIAL_GAP": 2,
  "NOT_PROVEN_PLANNER_ONLY": 4,
  "NOT_PROVEN_REPLAY_ONLY": 28,
  "NOT_PROVEN_SCORE_PATH_ONLY": 1,
  "NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM": 1
}
```

쉬운 예:

```text
source_route_recovery_status = SOURCE_ROUTE_PATTERN_READY
  어디서 확인해야 하는지는 안다.

runtime_source_route_execution_status = ROUTE_RECOVERED_NOT_EXECUTED
  하지만 이번 production run에서 실제 확인하러 간 것은 아니다.

accepted_claim_status = REPLAY_ACCEPTED_CLAIM_ONLY
  과거 연구 replay claim은 만들 수 있지만 운영 점수로 쓰면 안 된다.
```

대표 행:

```text
C05:
  PRODUCTION_FULL_THESIS_ATTEMPTED
  PRODUCTION_SCORE_PATH_HAS_ACCEPTED_CLAIMS
  SCORE_PATH_ONLY_WITH_REQUIRED_OR_GREEN_GAPS
  NOT_PROVEN_SCORE_PATH_ONLY

C06:
  PRODUCTION_CANDIDATE_BLOCKED
  SOURCE_TASK_EXECUTED_WITH_ACCEPTED_CLAIMS
  ACCEPTED_CLAIM_PRESENT_NOT_FULL_THESIS_CLOSED
  FULL_THESIS_BLOCKED_REQUIRED_OR_GREEN_GAP

C08/C15/C17/C24/C28:
  REPLAY_READY_NOT_RUNTIME_ATTEMPTED
  REPLAY_ACCEPTED_CLAIM_ONLY
  NO_PRODUCTION_FULL_THESIS_ROW
  NOT_PROVEN_REPLAY_ONLY

C29:
  SOURCE_TASK_EXECUTED
  SOURCE_TASK_EXECUTED_NO_ACCEPTED_CLAIMS
  NO_ACCEPTED_CLAIM
  NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM
```

결론:

```text
이제 C01~C32/R13 전수 상태는 증명 장부로 보인다.
하지만 모든 행이 NOT_PROVEN 계열이므로 goal4 완료는 아니다.
```

## 8. Stage가 있는 row는 있는가?

있다. 하지만 현재 의미를 정확히 분리해야 한다.

기존 0705 C05 감사 기준 production promoted 10개 row에는 score/stage가 있다.

예:

```text
001360 삼성제약: score 27.9998, Stage0
043260 성호전자: score 50.0, Stage1
097230 HJ중공업: score 77.9998, Stage2
```

하지만 이것은 전부 C05 경로다.

따라서 답은 다음이다.

```text
stage row는 있다.
하지만 goal4가 요구하는 "모든 주요 아키타입에서 연구자료만큼 runtime stage가 나온다"는 상태는 아니다.
```

쉬운 예:

```text
수학 시험 점수표는 있다.
그렇다고 과학, 영어, 국어까지 다 채점됐다고 말할 수는 없다.
```

## 9. Next Runtime Attempt Plan

전수 status matrix의 `next_required_action`을 다음 실행 입력으로 바꾸는 plan도 생성했다.

```text
docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.json
docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.md
docs/operational/all_archetype_next_runtime_source_tasks_2026-07-05.jsonl
docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl
```

현재 plan summary:

```text
plan_row_count = 36
source_task_count = 114
seed_event_count = 114
```

attempt type:

```json
{
  "BLOCKED_CANDIDATE_GAP_CLOSURE": 2,
  "PLANNER_TO_SOURCE_TASK_MATERIALIZATION": 4,
  "PROMOTED_SCORE_PATH_GAP_CLOSURE": 1,
  "REPLAY_TO_PRODUCTION_RUNTIME_ATTEMPT": 28,
  "SOURCE_EXECUTION_REPAIR": 1
}
```

target symbol mode:

```json
{
  "ARCHETYPE_LEVEL_DISCOVERY": 32,
  "SYMBOL_SPECIFIC": 4
}
```

안전 조건:

```text
all_tasks_score_blocked_before_execution = true
all_tasks_require_llm_query_generation = true
all_tasks_have_no_hardcoded_queries = true
all_tasks_have_finite_budget = true
```

쉬운 예:

```text
C08은 지금 production symbol이 없다.
그래서 가짜 symbol로 점수를 만들지 않는다.
대신 C08 아키타입 자체를 다음 planner input으로 넣고,
LLM이 current candidate와 source-backed claim을 찾게 만든다.
```

대표 plan row:

```text
C05:
  PROMOTED_SCORE_PATH_GAP_CLOSURE
  contract_amount_to_prior_sales, contract_duration_months, margin_bridge_visible

C06:
  BLOCKED_CANDIDATE_GAP_CLOSURE
  customer_preorder_or_allocation, revenue_visibility_contract, hbm_capacity_constraint

C29:
  SOURCE_EXECUTION_REPAIR
  source task는 돌았지만 accepted claim이 없으므로 anchor/claim 재수리

C08/C15/C17/C24/C28:
  REPLAY_TO_PRODUCTION_RUNTIME_ATTEMPT
  replay 판례를 current production runtime attempt로 연결
```

주의:

```text
이 plan은 점수를 만들지 않는다.
source-backed Evidence OS claim이 생기기 전에는 score/stage promotion을 금지한다.
```

## 10. Runtime Execution Manifest

다음 attempt plan을 실제 Census v4 Research Brain 입력으로 연결하는 manifest도 생성했다.

```text
docs/operational/all_archetype_runtime_execution_manifest_2026-07-05.json
docs/operational/all_archetype_runtime_execution_manifest_2026-07-05.md
docs/operational/all_archetype_runtime_execution_manifest.json
```

현재 manifest summary:

```text
execution_status = READY_FOR_RESEARCH_BRAIN_INPUT_NOT_EXECUTED_BY_PARITY_CLI
seed_event_count = 114
source_task_shell_count = 114
brain_candidate_event_seed_path = docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl
target_gate = full_thesis
brain_stage_promotion_mode = strict
```

핵심은 이거다.

```text
parity CLI는 장부와 다음 실행 입력을 만든다.
실제 Research Brain/Census v4 실행은 manifest command로 별도 수행해야 한다.
```

쉬운 예:

```text
all_archetype_next_runtime_attempt_plan은 "진료가 필요한 환자 목록"이다.
all_archetype_runtime_execution_manifest는 "그 환자 목록을 실제 접수 시스템에 넣는 실행 명령"이다.
하지만 아직 진료가 끝난 것은 아니다.
```

대표 실행 명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-05 \
  --universe krx \
  --output-root output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --research-brain-report-dir docs/operational \
  --brain-planner-provider real \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 114 \
  --brain-planner-success-limit 114 \
  --brain-planner-batch-size 5 \
  --brain-max-source-tasks-per-plan 5 \
  --brain-max-fetches-per-task 3 \
  --brain-accepted-claim-target 36 \
  --brain-max-distinct-candidate-attempts 114 \
  --brain-retry-max 1 \
  --brain-claim-extractor-provider auto \
  --brain-claim-extractor-timeout-seconds 180.0 \
  --brain-runtime-budget-seconds 7200.0 \
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

주의:

```text
manifest와 seed event는 점수 재료가 아니다.
Research Brain이 실제 source-backed claim을 만들기 전에는 score/stage 승격을 허용하지 않는다.
```

## 11. Planner Bias 상태

Planner audit:

```text
planner_run_count = 350
hypothesis_run_count = 35
real_provider_success_count = 35
distinct_top1_archetype_count = 4
C05 top1 count = 29
C05 top1 share = 0.828571
```

Top1 counts:

```json
{
  "C01": 2,
  "C05": 29,
  "C06": 2,
  "C29": 2
}
```

판정:

```text
PLANNER_ARCHETYPE_ROUTING_BIAS_NOT_READY
```

왜 문제인가:

```text
C05가 실제로 많을 수는 있다.
하지만 goal4는 전 아키타입 parity를 확인해야 한다.
planner top1이 C05에 82.8571% 몰리면, 다른 아키타입 runtime 경로가 실제로 열렸는지 확인할 수 없다.
```

## 12. Candidate Selection 상태

Candidate selection audit:

```text
status = BALANCED_FULL_THESIS_SELECTION_NOT_READY
current_full_thesis_row_count = 10
current_distinct_full_thesis_archetype_count = 1
current_c05_full_thesis_share = 1.0
mandatory_archetype_attempt_missing = 5
mandatory_archetype_full_thesis_missing = 6
next_required_archetype_attempt_count = 12
meaningful_pass_allowed = false
```

해석:

```text
C06은 일부 production attempt가 있다.
하지만 C08/C15/C17/C24/C28은 production full-thesis row로 올라온 것이 없다.
다음 run에서는 mandatory missing archetype부터 강제로 attempt 목록에 들어가야 한다.
```

단, "강제로 score를 만들라"는 뜻이 아니다.

```text
강제해야 하는 것:
  attempt / source route / accepted claim 또는 source gap 설명

강제하면 안 되는 것:
  증거 없는 점수 / stage 승격
```

## 13. 삼성전자/하이닉스 분리

삼성전자/하이닉스 controlled smoke와 production row는 분리했다.

Controlled smoke:

```text
SK하이닉스: C06, score 88.0, Stage3-Yellow, SMOKE_ONLY
삼성전자: C06, score 72.0, Stage2-Watch, SMOKE_ONLY
```

Production 상태:

```text
삼성전자:
  C06 production blocked candidate.
  customer_preorder_or_allocation, hbm_capacity_pre_sold 등 source pending gap 때문에 promoted row 아님.

SK하이닉스:
  planner top1 C06 시도는 있으나 accepted claim이 없어 FULL_THESIS_NOT_RUN.
```

결론:

```text
smoke 점수는 "경로 테스트"다.
production 점수로 섞으면 안 된다.
```

## 14. 이번 코드 패치 요약

새로 추가된 핵심 모듈:

- `src/e2r/census/all_archetype_next_attempt_planner.py`
- `src/e2r/census/all_archetype_runtime_execution_manifest.py`
- `src/e2r/census/all_archetype_runtime_status_matrix.py`
- `src/e2r/research_reverse/*`
- `src/e2r/source_routing/*`
- `src/e2r/census/research_to_runtime_parity.py`
- `src/e2r/census/research_to_runtime_replay.py`
- `src/e2r/census/research_memory_followup_planner.py`
- `src/e2r/census/full_thesis_candidate_selector.py`
- `src/e2r/research_brain/planner_bias_audit.py`
- `src/e2r/cli/run_research_to_runtime_parity_until_pass.py`

새 테스트의 핵심:

```text
C01~C32/R13 36개 contract가 attempt/source route/accepted claim/full thesis 상태축을 모두 가진다.
전수 status matrix의 모든 NOT_PROVEN 행에 next runtime attempt/source-task shell이 생긴다.
next task는 score/stage promotion을 막고 LLM query generation과 finite budget을 강제한다.
execution manifest가 114개 seed event를 Census v4 strict full_thesis 실행 입력으로 연결한다.
C05-only promoted row는 meaningful pass가 아니다.
required_positive_missing이 있으면 meaningful pass가 아니다.
source_proxy_only는 score가 아니라 repair task다.
snippet은 score source가 아니다.
ResearchMemory는 discovery only다.
mandatory archetype replay는 production score로 새면 안 된다.
planner C05 편향은 별도 blocker로 남긴다.
```

## 15. 검증 결과

CLI 재실행:

```bash
PYTHONPATH=src python -m e2r.cli.run_research_to_runtime_parity_until_pass \
  --as-of-date 2026-07-05 \
  --mode full_thesis_balanced \
  --mandatory-archetypes C06,C08,C15,C17,C24,C28 \
  --max-iterations 10
```

결과:

```text
exit_code = 1
final_status = MEANINGFUL_RUNTIME_PARITY_NOT_READY
all_archetype_runtime_status_row_count = 36
all_archetype_next_attempt_plan_row_count = 36
all_archetype_next_source_task_count = 114
all_archetype_runtime_execution_seed_event_count = 114
meaningful_acceptance_status = MEANINGFUL_FULL_THESIS_EVIDENCE_PASS_FALSE
candidate_selection_status = BALANCED_FULL_THESIS_SELECTION_NOT_READY
planner_bias_status = PLANNER_ARCHETYPE_ROUTING_BIAS_NOT_READY
mandatory_replay_accepted_claim_count = 6
mandatory_replay_source_proxy_repair_task_count = 18
```

테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_to_runtime_parity_goal4 \
  tests.test_all_archetype_runtime_status_matrix \
  tests.test_all_archetype_next_attempt_plan \
  tests.test_all_archetype_runtime_execution_manifest \
  tests.test_research_reverse_case_extractor \
  tests.test_research_reverse_source_quality \
  tests.test_research_reverse_no_proxy_to_score \
  tests.test_research_runtime_memory_cards \
  tests.test_research_memory_no_future_outcome_in_prompt \
  tests.test_research_source_route_recovery \
  tests.test_research_source_route_official_first \
  tests.test_research_source_route_no_snippet_score \
  tests.test_research_memory_followup_planner \
  tests.test_followup_tasks_reduce_or_explain_missing_primitives \
  tests.test_research_to_runtime_replay_mandatory_archetypes \
  tests.test_research_to_runtime_proxy_becomes_repair_task \
  tests.test_full_thesis_evidence_completion_split \
  tests.test_full_thesis_score_path_not_meaningful_pass \
  tests.test_meaningful_full_thesis_production_acceptance \
  tests.test_no_c05_only_meaningful_pass \
  tests.test_required_positive_missing_blocks_meaningful_pass \
  tests.test_full_thesis_candidate_selection_diversity \
  tests.test_full_thesis_no_c05_monoculture \
  tests.test_full_thesis_target_archetype_provenance \
  tests.test_planner_bias_audit \
  tests.test_non_economic_mechanism_c05_requires_review \
  tests.test_census_v4_all_archetype_replay_matrix \
  -v
```

결과:

```text
Ran 70 tests
OK
```

문법 검증:

```bash
python -m py_compile \
  src/e2r/census/all_archetype_next_attempt_planner.py \
  src/e2r/census/all_archetype_runtime_execution_manifest.py \
  src/e2r/census/all_archetype_runtime_status_matrix.py \
  src/e2r/census/census_runner_v4.py \
  src/e2r/census/full_thesis_candidate_selector.py \
  src/e2r/census/research_memory_followup_planner.py \
  src/e2r/census/research_to_runtime_parity.py \
  src/e2r/census/research_to_runtime_replay.py \
  src/e2r/cli/run_research_to_runtime_parity_until_pass.py \
  src/e2r/research_brain/planner_bias_audit.py \
  src/e2r/research_reverse/*.py \
  src/e2r/source_routing/*.py
```

결과:

```text
OK
```

전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5249 tests
OK
```

## 16. 남은 작업

다음 단계는 점수를 억지로 올리는 작업이 아니다.

필요한 것은:

```text
1. `all_archetype_runtime_execution_manifest_2026-07-05.json`의 command를 실제 실행
2. LLM planner가 각 source-task shell에서 실제 query를 생성
3. source-backed Evidence OS claim을 만들고 accepted claim으로 검증
4. accepted claim을 score contribution/full thesis closure로 연결
5. C05 share를 낮추기 위해 arbitrary quota가 아니라 missing archetype route를 우선 실행
6. promoted row에서 target_archetype UNKNOWN/source_primary_context_only가 사라지는지 확인
7. required_positive_missing/green gap이 material하면 meaningful pass를 계속 막기
```

최종 완료 조건:

```text
MEANINGFUL_RUNTIME_PARITY_READY
```

가 나오려면 최소한 다음이 필요하다.

```text
- C05-only monoculture 해소
- mandatory archetype full-thesis row 또는 명시적 source-gap 상태 확보
- source_proxy_only production score leak 0 유지
- required positive / Green gap이 의미 있는 row에서 해소
- planner C05 top1 편향이 acceptance limit 아래로 내려감
- smoke score와 production score 혼동 0 유지
```

## 17. 다음 에이전트가 봐야 할 질문

피드백을 줄 때 가장 먼저 봐야 할 질문:

```text
1. next_required_archetype_attempts가 실제 다음 production run 입력으로 들어가는가?
2. C08/C15/C17/C24/C28은 왜 production attempt까지도 못 갔는가?
3. ResearchMemory card가 planner prompt에 discovery-only로 들어가되, 미래 성과/정답 label을 누출하지 않는가?
4. mandatory replay accepted claim이 production score로 새지 않는다는 테스트가 유지되는가?
5. source route gap task가 실제 source acquisition task로 이어지는가?
6. target_archetype UNKNOWN promoted row가 다음 run에서 차단되는가?
7. source_primary_archetype context가 non-binding reference로만 남고 final primary를 오염시키지 않는가?
```

이번 문서의 결론:

```text
0705 작업은 goal4 완료가 아니라, goal4를 거짓 완료로 표시하지 못하게 만든 감사/장부/테스트 패치다.
다음 작업은 이 장부를 사용해 C05 밖의 아키타입을 실제 production attempt와 source-backed claim으로 끌어올리는 것이다.
```

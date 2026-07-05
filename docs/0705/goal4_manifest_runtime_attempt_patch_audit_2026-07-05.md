# Goal4 Manifest Runtime Attempt Patch Audit - 2026-07-05

이 문서는 `docs/0705/goal4_research_to_runtime_status_2026-07-05.md`의 "manifest command를 실제 실행해야 한다" 다음 단계 결과를 기록한다.

검증 기준 산출물:

- `output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-patched/`
- `output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-patched/PARTIAL_RUN_INVALID.md`
- `output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-patched/partial_run_invalid.json`
- `output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-patched/brain_web_runtime_progress.json`
- `output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-patched/full_thesis_seed_materialization_audit.json`
- `output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-patched/full_thesis_production_audit.json`
- `docs/operational/census_mode_v4_*`

짧은 결론:

```text
고친 것:
- Goal4 전수 seed 114개가 Census v4 Research Brain 입력으로 실제 선택되게 했다.
- symbol=None인 ARCHETYPE_LEVEL_DISCOVERY seed 96개를 버리지 않게 했다.
- AllArchetypeRuntimeParityFollowUp seed가 daily 이벤트보다 먼저 planner budget을 쓰게 했다.

실행 결과:
- run은 INVALID_PARTIAL_OUTPUT으로 실패했다.
- 최신 audit 기준 production FULL_THESIS row는 10개 C05가 아니라 0개다.
- 따라서 이전의 FULL_THESIS_PRODUCTION_PASS 라벨은 더 이상 유지되지 않는다.
- 하지만 full thesis가 성공한 것도 아니다. 전수 seed 114개는 source-of-truth materialization audit에서 아직 PLANNER_NOT_RUN이다.
```

쉬운 예:

```text
예전 문제:
  병원 예약표 114장을 만들었는데, 접수창구가 symbol 없는 예약표 96장을 버렸다.

이번 패치:
  114장을 접수창구에 올리는 데는 성공했다.

아직 문제:
  진료 기록지가 아직 저장되지 않았다.
  대기 화면에는 95번째까지 부른 흔적이 있지만, 공식 진료 기록부에는 "진료 완료 0명"이다.
```

## 1. 코드 패치 내용

패치 파일:

- `src/e2r/research_brain/v4_production_orchestrator.py`
- `tests/test_research_brain_v4_operational_modes.py`

### 1-1. seed loader 수정

이전 loader는 `symbol=None` 또는 빈 symbol을 무조건 skip했다.

그 결과 `docs/operational/all_archetype_next_runtime_seed_events_2026-07-05.jsonl`의 114개 중 96개가 `ARCHETYPE_LEVEL_DISCOVERY`라서 버려졌다.

패치 후 허용 조건:

```text
target_symbol_mode == ARCHETYPE_LEVEL_DISCOVERY
AND seed_role == planner_input_only
AND source_family == AllArchetypeRuntimeParityFollowUp
```

이 조건을 만족하는 seed는:

```text
symbol = ""
issuer_directness = INDUSTRY
company_name = target_archetype
```

로 유지한다.

중요한 점:

```text
symbol 없는 seed를 점수 재료로 허용한 것이 아니다.
planner input only로 살린 것이다.
source-backed claim이 생기기 전에는 score/stage 승격 금지다.
```

### 1-2. seed selection 수정

이전 `_select_unique_candidate_events()`는 `CensusFullThesisQueue`만 우선 선택했다.

패치 후 `AllArchetypeRuntimeParityFollowUp`도 full-thesis refresh seed로 인정한다.

즉 다음 순서가 된다.

```text
1. Goal4/Full-thesis refresh seed 전부 먼저 선택
2. 남는 budget에 daily discovery 이벤트 선택
```

쉬운 예:

```text
이번 목표가 "36개 아키타입 전수 재검사"인데,
일반 뉴스 이벤트가 먼저 줄을 차지하면 안 된다.
전수 재검사 접수표 114장을 먼저 넣고, 남으면 일반 환자를 받는 구조로 바꾼 것이다.
```

## 2. 실행한 command

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-05 \
  --universe krx \
  --output-root output/census_v4/2026-07-05-goal4-all-archetype-next-runtime-attempt-patched \
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

결과:

```text
exit_code = 1
stdout = INVALID_PARTIAL_OUTPUT
verdict = INVALID_PARTIAL_OUTPUT
score_or_stage_evidence_allowed = false
readiness_evidence_allowed = false
next_action = rerun after resolving the provider/runtime failure; if provider failure persists, report ProviderPending/NotReady
```

## 3. seed 투입은 고쳐졌나?

고쳐졌다.

이번 patched output의 `research_brain_candidate_seed_events_used.jsonl` 기준:

```text
seed_event_count = 114
source_family = AllArchetypeRuntimeParityFollowUp 114
target_archetype_count = 36
blank_symbol_seed_count = 96
symbol_specific_seed_count = 18
```

이전 실패와 비교:

```text
이전:
  symbol=None seed 96개 skip
  실제 seed_event_count = 18

패치 후:
  symbol=None planner-only seed 유지
  실제 seed_event_count = 114
```

중요한 해석:

```text
이건 전 아키타입 attempt 입력이 들어갔다는 뜻이다.
전 아키타입 full thesis가 완료됐다는 뜻은 아니다.
```

## 4. progress 파일은 무엇을 보여 주나?

`brain_web_runtime_progress.json` 기준 마지막 상태:

```text
latest_phase = planner_batch_start
next_event_index = 95
real_success_count = 55
remaining_success_budget = 59
runtime_seconds ~= 2069.8
```

이 값은 "runtime 중간 대기판"이다.

주의:

```text
progress의 real_success_count는 공식 score/stage 증거가 아니다.
planner_runs.jsonl, source_tasks.jsonl, accepted_claims.jsonl, stagecourt_traces.jsonl에 남아야 materialization 증거가 된다.
```

이번 run에서는 그 연결이 안 됐다.

## 5. source-of-truth audit은 무엇을 말하나?

`full_thesis_seed_materialization_audit.json` 기준:

```text
seed_event_count = 114
planner_run_seed_count = 0
real_provider_success_seed_count = 0
source_task_execution_seed_count = 0
accepted_claim_seed_count = 0
stagecourt_trace_seed_count = 0
full_thesis_promoted_seed_count = 0
actual_materialization_pass_allowed = false
full_thesis_seed_promotion_pass = false
status_counts = {"PLANNER_NOT_RUN": 114}
```

즉 공식 장부 기준으로는 아직 전부 `PLANNER_NOT_RUN`이다.

왜 progress와 audit이 다르게 보이는가:

```text
progress:
  실행 중간 상태를 기록한다.
  95번째 seed 배치까지 들어갔고 일부 provider success처럼 보이는 숫자가 있었다.

materialization audit:
  실제 파일에 남은 planner/source/claim/stage trace를 기준으로 판단한다.
  이번 run은 planner_runs.jsonl이 0줄이라 materialization 증거가 없다.
```

쉬운 예:

```text
대기 화면에는 "55명 호출됨"이라고 떴다.
그런데 병원 공식 차트에는 진료 기록이 0건이다.
정산/진단에는 공식 차트만 써야 한다.
```

## 6. production FULL_THESIS는 지금 몇 개인가?

최신 patched run 기준:

```text
production_full_thesis_row_count = 0
production_pass_allowed = false
status = PENDING_FULL_THESIS_PRODUCTION
blockers = ["production_full_thesis_runner_no_eligible_rows"]
```

이전 커밋 상태와 비교:

```text
이전 HEAD:
  production_full_thesis_row_count = 10
  production_pass_allowed = true
  production_symbols = 001360,001470,002990,010960,034020,034730,043260,047040,060900,097230
  전부 C05
  required_positive_missing_primitives = 10/10

패치 실행 후:
  production_full_thesis_row_count = 0
  production_pass_allowed = false
```

결론:

```text
이제 "10개 C05라서 production pass"라고 말하는 상태는 아니다.
다만 그 대신 "아직 full thesis production 미완료"가 정확한 상태다.
```

## 7. 사용자가 물은 6개 질문의 최신 답

### Q1. 왜 production FULL_THESIS 10개가 전부 C05였나?

이전 HEAD 기준 원인은 다음이다.

```text
seed target_archetype = UNKNOWN/null
source_primary_archetype = C05 문맥이 refresh queue에 많음
planner top1 = promoted 10개 모두 C05
final assigned archetype = C05
```

따라서 C05는 `target_archetype`에서 온 게 아니라:

```text
event-board source_primary context
-> planner top1
-> final primary_archetype
```

경로로 왔다.

현재 patched run에서는 production row가 0개라 "10개 전부 C05 production pass" 상태가 사라졌다.

### Q2. target_archetype_counts가 UNKNOWN인데 C05로 나온 경로는?

이전 경로:

```text
target_archetype UNKNOWN
-> source_primary_archetype C05를 planner 참고 문맥으로 제공
-> planner output top_k_archetype_hypotheses[0] = C05
-> StageCourt/production row primary_archetype = C05
```

주의:

```text
UNKNOWN은 "아키타입 없음"이 아니라 "planner가 다시 판단해야 함"이다.
하지만 source_primary context가 C05로 강하게 기울면 C05 편향이 생긴다.
```

현재 patched run은 `AllArchetypeRuntimeParityFollowUp` seed가 `target_archetype`을 갖고 있지만, 공식 materialization audit에서는 아직 planner row가 저장되지 않아 final assignment가 없다.

### Q3. 27.9998 / 77.9998은 어디서 나왔나?

이전 C05 production 10개에서 나온 C05 weight 합산 점수다.

대표 공식:

```text
weighted_component = clamp(raw_component, 0, canonical_max) / canonical_max * C05_weight
final_score = clamp(sum(weighted_components) + calibration_bonus - risk_penalty, 0, 100)
```

27.9998:

```text
earnings_visibility = 13.3333 / 20 * 22 = 14.6666
information_confidence = 3.3333 / 5 * 20 = 13.3332
sum = 27.9998
```

77.9998:

```text
eps_fcf_explosion = 20 / 20 * 18 = 18
earnings_visibility = 13.3333 / 20 * 22 = 14.6666
bottleneck_pricing = 20 / 20 * 10 = 10
market_mispricing = 15 / 15 * 12 = 12
valuation_rerating = 15 / 15 * 10 = 10
information_confidence = 3.3333 / 5 * 20 = 13.3332
sum = 77.9998
```

현재 patched run에서는 production full-thesis score row가 0개라 새 27.9998/77.9998 production 점수는 없다.

### Q4. C05가 아닌 아키타입 후보는 왜 0개였나?

이전 HEAD 기준:

```text
C06/C01:
  후보는 있었지만 source_pending_required_or_green_primitives로 blocked.

C08/C15/C17/C24/C28:
  full-thesis refresh queue/materialization 안에 해당 아키타입 production 후보가 사실상 없었다.
```

현재 patched run 기준:

```text
C01~C32/R13 총 36개 seed가 모두 입력됐다.
하지만 materialization audit에서는 전부 PLANNER_NOT_RUN이다.
따라서 non-C05도 C05도 아직 production full-thesis 후보로 승격되지 않았다.
```

### Q5. required_positive_missing_primitives가 있는데 왜 PASS를 허용했나?

이전 HEAD의 잘못된 의미 분리:

```text
FULL_THESIS_PRODUCTION_PASS
= score path closed에 가까웠다.
!= meaningful full thesis completed
```

이번 patched run 후 최신 audit:

```text
production_pass_allowed = false
production_full_thesis_row_count = 0
```

즉 현재 산출물은 더 이상 required positive gap이 남은 10개 row를 production pass로 인정하지 않는다.

### Q6. 삼성전자/하이닉스는 왜 production full-thesis row가 아니었나?

이전 HEAD 기준:

```text
삼성전자:
  C06 production blocked candidate.
  customer_preorder_or_allocation, hbm_capacity_pre_sold 등 source pending gap 때문에 promoted row 아님.

SK하이닉스:
  controlled smoke에서는 C06 점수/Stage가 있었지만 production row가 아니다.
  production materialization에서는 accepted claim이 없어 FULL_THESIS_NOT_RUN.
```

현재 patched run 기준:

```text
production_full_thesis_row_count = 0
controlled_smoke_substitution_allowed = false
required_smoke_symbols = 005930, 000660
required_smoke_symbols_promoted_without_missing_primitives_count = 0
```

즉 삼전/하닉 smoke 점수는 여전히 production 점수가 아니다.

## 8. Stage가 있는 row는 있나?

있다. 하지만 전부 event-board stage다.

`census_stage_summary.json` 기준:

```text
stage_status_count = 3391
Stage0 = 3306
Stage1 = 55
Stage2-Watch = 29
Red = 1
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
stage_scope_distribution = {"CENSUS_EVENT_BOARD": 3391}
operator_stage_use_distribution = {"NOT_FULL_THESIS_STAGE": 3391}
operator_score_use_distribution = {"NOT_FULL_E2R_SCORE": 3391}
```

쉬운 예:

```text
전 종목 census 상태판은 있다.
하지만 이건 "현재 지도에서 봤을 때 관심 없음/공시 있음/자료 부족" 같은 상태판이다.
정밀 투자 thesis 점수표가 아니다.
```

따라서 답은:

```text
Stage row는 있다.
운영 full-thesis Stage row는 없다.
```

## 9. 이번 실패의 핵심 blocker

이번 실패의 핵심은 seed selection이 아니라 "planner/source/claim trace가 파일 장부로 남지 않는 것"이다.

감사 blocker:

```text
LLM planner run row count is zero
LLM planner real-provider success count is zero
Brain/Web source task execution count is zero
Brain/Web real fetched document count is zero
LLM claim extractor has zero attempts
Brain/Web accepted claim count is zero
Brain/Web StageCourt traces are not promoted
```

partial invalid에 명시된 operator rule:

```text
This output directory may contain partial leaf files, but it is not a completed census run.
Do not use it as readiness, score, or Stage evidence.
```

## 10. 다음 패치 방향

다음 작업은 점수를 만드는 게 아니라 trace를 닫는 것이다.

필수 패치:

```text
1. real planner subprocess를 호출하기 전에 planner_attempt row를 append한다.
2. subprocess 성공/실패/timeout/provider_error를 planner_runs.jsonl에 반드시 append한다.
3. progress real_success_count와 planner_runs row count가 불일치하면 audit failure로 즉시 드러낸다.
4. planner child process timeout을 명시한다. 무한 대기하면 ProviderPending으로 닫는다.
5. source task 생성 전/후도 source_tasks/source_task_executions에 append-only로 남긴다.
6. accepted claim이 없으면 낮은 점수 확정이 아니라 source/provider pending으로 남긴다.
7. stale v3 leaf 파일과 이번 run 파일은 mtime/source_run_id로 분리한다.
8. full-thesis promotion은 stagecourt trace + accepted claim + score contribution + full thesis scope가 모두 있을 때만 허용한다.
```

쉬운 예:

```text
다음 목표는 "95번째까지 부른 것처럼 보인다"가 아니다.
"누구를 불렀고, 어떤 문서를 가져왔고, 어떤 claim을 인정했고, 그래서 어떤 점수 칸을 채웠는지"가 장부에 남아야 한다.
```

## 11. 검증한 테스트

이번 패치에 대해 먼저 실행한 targeted test:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_candidate_event_seed_path_skips_missing_or_zero_symbol_rows \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_full_thesis_refresh_queue_consumes_selection_budget_before_daily_fill \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_goal4_all_archetype_runtime_parity_seeds_consume_selection_budget_before_daily_fill \
  tests.test_all_archetype_next_attempt_plan \
  tests.test_all_archetype_runtime_execution_manifest \
  -v
```

결과:

```text
Ran 12 tests
OK
```

추가 직접 loader check:

```text
loaded = 114
families = AllArchetypeRuntimeParityFollowUp 114
blank_symbol = 96
with_symbol = 18
selected = 114
selected_blank_symbol = 96
```

문법 검증:

```bash
python -m py_compile src/e2r/research_brain/v4_production_orchestrator.py
```

결과:

```text
OK
```

## 최종 판단

이번 0705 후속 작업의 정확한 상태:

```text
완료:
  Goal4 all-archetype seed가 Census v4 Research Brain 입력에서 버려지는 문제는 고쳤다.

미완료:
  Research Brain planner/source/claim/stage trace가 공식 장부로 materialize되지 않아 full thesis는 실패했다.

현재 운영 verdict:
  NOT_READY / INVALID_PARTIAL_OUTPUT

점수/Stage 사용 가능 여부:
  production full-thesis score/stage로 사용 금지.
```

즉 이제 문제는 "C05만 stage가 나와서 전 아키타입인 척하는 것"에서 한 단계 더 명확해졌다.

```text
전 아키타입 입력은 들어간다.
하지만 공식 trace 장부가 닫히지 않는다.
```

다음 에이전트는 score weight나 stage threshold를 건드리기 전에, planner/source/claim trace materialization부터 닫아야 한다.

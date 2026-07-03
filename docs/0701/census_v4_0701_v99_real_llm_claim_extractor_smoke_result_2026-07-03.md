# Census v4 0701 v99 Real LLM Claim Extractor Smoke 결과

작성일: 2026-07-03

대상 산출물:

```text
output/census_v4/2026-07-01-v99-external-seed-real-extractor-smoke
```

## 0. 결론

v99에서 v97의 핵심 blocker 하나는 실제로 닫혔다.

```text
v97 blocker:
  LLM claim extractor has no real LLM provider runs

v99 result:
  claim_extractor_runs.jsonl에
  provider_mode=llm
  provider_name=codex_cli_contract_blind_extractor
  status=SUCCESS
  가 기록됨
```

하지만 v99도 운영 READY는 아니다.

```text
verdict = NOT_READY
stage_scope=FULL_THESIS row = 0
score_scale=FULL_E2R_100 row = 0
operator usable Stage = 0
```

쉬운 예:

```text
이전에는 "LLM 독해 선생님이 시험장에 아예 안 들어왔다"가 문제였다.
v99에서는 선생님이 실제로 들어와서 답안을 읽었다.
하지만 시험 본 학생 수와 채점된 답안 수가 운영 기준보다 너무 적어서 아직 합격은 아니다.
```

## 1. 실행 명령

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-v99-external-seed-real-extractor-smoke \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider real \
  --brain-source-acquisition live_full_bounded \
  --brain-candidate-event-seed-path output/census_v4/2026-07-01-v97-seed-source/research_brain_full_thesis_seed_events.jsonl \
  --brain-universe-limit 2 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-source-tasks-per-plan 2 \
  --brain-max-fetches-per-task 1 \
  --brain-retry-max 1 \
  --brain-claim-extractor-provider auto \
  --brain-claim-extractor-timeout-seconds 180 \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --write-operational-docs false \
  --fail-on-critical-audit false
```

출력:

```text
NOT_READY
exit code = 1
```

이 실패는 정상이다.

이번 run은 일부러 작은 smoke 설정이다.

```text
brain_universe_limit = 2
brain_planner_success_limit = 1
max_source_tasks_per_plan = 2
max_fetches_per_task = 1
```

이 설정은 operational minimum을 채울 수 없다.

## 2. readiness verdict

파일:

```text
readiness_verdict.json
```

핵심 값:

```text
verdict = NOT_READY
run_mode = BRAIN_AND_WEB_ACQUISITION_ENABLED
brain_web_mode = enabled
```

남은 blockers:

```text
Brain/Web operational minimum planner runs not met: 21/30
Brain/Web operational minimum web search tasks not met: 3/20
Brain/Web operational minimum web/news search calls not met: 3/20
Brain/Web operational minimum fetched documents not met: 1/10
Brain/Web operational minimum claim extractor attempts not met: 1/10
```

중요 변화:

```text
"LLM claim extractor has no real LLM provider runs" blocker가 사라졌다.
```

## 3. Brain/Web attempt audit

파일:

```text
brain_web_attempt_audit.json
```

핵심 값:

```text
verdict = ATTEMPTED_WITH_SOURCE_TASKS
full_thesis_seed_source = external_candidate_event_seed_path
full_thesis_seed_original_path =
  output/census_v4/2026-07-01-v97-seed-source/research_brain_full_thesis_seed_events.jsonl
blockers = []
```

해석:

```text
외부 seed는 실제 Brain run에 들어갔다.
real planner/source/extractor까지 일부 실행됐다.
```

## 4. real LLM claim extractor 증거

파일:

```text
claim_extractor_runs.jsonl
```

count:

```text
claim_extractor_runs = 1
```

sample:

```text
extractor_run_id = EXT-RUN-7662ea3be30ce7e1606c9356
symbol = 000660
provider_name = codex_cli_contract_blind_extractor
provider_mode = llm
model = codex-cli-default
status = SUCCESS
provider_error = null
timeout_seconds = 180.0
raw_assertion_ids = 33개
source_origin = research_brain_v4_attempt
```

해석:

```text
이번에는 rule_fallback이 아니라 실제 Codex CLI 기반 contract-blind extractor가 실행됐다.
```

v97과 비교:

```text
v97:
  claim_extractor_runs = 1
  provider_mode = rule_fallback
  blocker = LLM claim extractor has no real LLM provider runs

v99:
  claim_extractor_runs = 1
  provider_mode = llm
  blocker 제거
```

## 5. source / web / claim counts

v99 current Brain/Web attempt 기준:

```text
planner_runs = 21
  provider_mode=real = 1
  provider_mode=none = 20
  real_provider_success = 1

web_search_tasks = 3
web_search_results = 30
web_fetched_documents = 1

claim_extractor_runs = 1
  provider_mode=llm = 1
  status=SUCCESS = 1

accepted_claims source_origin=research_brain_v4_attempt = 19
score_contributions source_origin=research_brain_v4_attempt = 6
stagecourt_traces source_origin=research_brain_v4_attempt = 1
```

주의:

```text
accepted_claims 전체 row는 111개지만, 이번 Brain/Web attempt claim은 19개다.
source_origin 필터를 봐야 한다.
```

쉬운 예:

```text
창고 전체 물건은 111개다.
이번 배송으로 들어온 물건은 19개다.
이번 run 성과는 19개로 봐야 한다.
```

## 6. FULL_THESIS seed materialization 상태

파일:

```text
full_thesis_seed_materialization_trace.jsonl
full_thesis_seed_materialization_audit.json
```

status counts:

```text
PLANNER_NOT_RUN = 64
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 20
STAGECOURT_READY_NOT_PROMOTED = 1
FULL_THESIS_PROMOTED = 0
```

audit:

```text
verdict = PASS
ledger_integrity_pass_allowed = true
actual_materialization_pass_allowed = false
operator_materialization_status = PENDING_FULL_THESIS_MATERIALIZATION
```

SK하이닉스 000660 seed:

```text
materialization_status = STAGECOURT_READY_NOT_PROMOTED
planner_run_count = 1
planner_real_provider_success_count = 1
source_task_execution_count = 7
accepted_claim_count = 19
score_contribution_count = 6
stagecourt_trace_count = 1
final_stage_scope = BRAIN_WEB_PARTIAL
final_score_scale = EVENT_WEIGHTED_PARTIAL
final_operator_stage_use = NOT_FULL_THESIS_STAGE
final_operator_score_use = NOT_FULL_E2R_SCORE
final_is_full_thesis_stage = false
final_is_full_e2r_score = false
```

blockers:

```text
full_thesis_seed_stagecourt_trace_not_promoted_to_full_thesis
final_stage_scope=BRAIN_WEB_PARTIAL
final_score_scale=EVENT_WEIGHTED_PARTIAL
```

해석:

```text
SK하이닉스는 real LLM extractor까지 통과해 partial score/stagecourt를 만들었다.
하지만 FULL_THESIS/FULL_E2R_100 승급 조건은 아직 닫히지 않았다.
```

## 7. 삼성전자 005930 상태

삼성전자 seed:

```text
symbol = 005930
candidate_event_id = CEV4-FTQUEUE-005930-443618f53c122b15
materialization_status = PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS
planner_run_count = 1
planner_real_provider_success_count = 0
source_task_execution_count = 0
accepted_claim_count = 0
score_contribution_count = 0
stagecourt_trace_count = 0
final_stage_scope = CENSUS_EVENT_BOARD
final_score_scale = EVENT_WEIGHTED_PARTIAL
final_operator_stage_use = NOT_FULL_THESIS_STAGE
final_operator_score_use = NOT_FULL_E2R_SCORE
```

해석:

```text
삼성전자는 이번 small smoke에서 real planner success 대상이 아니었다.
따라서 삼성전자 운영 Stage/score는 여전히 말하면 안 된다.
```

## 8. v99가 증명한 것과 증명하지 못한 것

### 증명한 것

```text
1. external seed path가 Census Brain run에 들어간다.
2. live_full_bounded + auto extractor 설정에서 Codex CLI claim extractor가 실제 실행된다.
3. LLM extractor output이 raw_assertions -> accepted_claims -> score_contributions 일부로 이어진다.
4. readiness gate가 작은 실행을 READY로 과장하지 않는다.
5. v98의 operator-use trace 보강이 live 산출물에서 작동한다.
```

### 아직 증명하지 못한 것

```text
1. operational minimum planner runs 30개 충족
2. web search tasks 20개 충족
3. fetched documents 10개 충족
4. claim extractor attempts 10개 충족
5. FULL_THESIS_PROMOTED seed 존재
6. stage_scope=FULL_THESIS row 존재
7. score_scale=FULL_E2R_100 row 존재
8. operator_stage_use=FULL_THESIS_STAGE row 존재
9. operator_score_use=FULL_E2R_SCORE row 존재
10. 삼성전자/하이닉스 C06/HBM full thesis live closure
```

## 9. 다음 패치/실행 방향

이제 blocker 성격이 바뀌었다.

v97에서는:

```text
real LLM extractor 자체가 안 돈다
```

v99에서는:

```text
real LLM extractor는 돈다.
하지만 실행 폭이 operational minimum보다 작고,
FULL_THESIS 승급 primitive/gate가 아직 닫히지 않는다.
```

다음 단계:

```text
1. planner_success_limit을 1에서 늘린 bounded run 실행
2. max_source_tasks_per_plan / max_fetches_per_task를 operational minimum에 맞게 확대
3. source-origin filtered current attempt count가 readiness gate를 만족하는지 확인
4. FULL_THESIS seed 중 최소 1개가 FULL_THESIS/FULL_E2R_100으로 승급 가능한지 확인
5. 승급이 안 되면 missing primitive / score interval / Green gate blocker를 seed별로 분해
```

단, 무제한으로 풀면 안 된다.

```text
top_results=None
retry_max=None
unbounded page fetch
```

같은 backfill 방식은 production daily goal과 맞지 않는다.

## 10. 한 줄 판단

v99는 real LLM claim extractor 경로가 실제로 작동함을 증명했다.

하지만 운영 READY는 아니다.

```text
v99 status:
  real extractor smoke = PASS
  Brain/Web operational minimum = NOT_READY
  FULL_THESIS materialization = PENDING
  operator usable Stage = 0개
```


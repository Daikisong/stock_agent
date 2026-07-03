# Census v4 0701 v97 External Seed Real Brain Smoke 교차검증 및 다음 패치 방향

작성일: 2026-07-03

대상 산출물:

```text
seed source run:
output/census_v4/2026-07-01-v97-seed-source

external seed real Brain smoke:
output/census_v4/2026-07-01-v97-external-seed-real-brain-smoke
```

## 0. 최종 결론

현재 상태는 이렇다.

```text
Stage 행은 있다.
Stage 0이 아닌 행도 있다.
Brain/Web partial 행도 1개 있다.

하지만 운영자가 써도 되는 FULL_THESIS / FULL_E2R_100 Stage는 아직 0개다.
```

즉 `stage가 있는 애들이 있긴 해?`에 대한 정확한 답은 다음이다.

```text
있다:
  Census event-board Stage와 Brain/Web partial Stage는 있다.

없다:
  실제 운영 full thesis Stage는 없다.
```

쉬운 예:

```text
출석 체크 점수표는 있다.
쪽지시험 기록도 1개 있다.
하지만 기말고사 성적표는 아직 없다.

지금 operator가 매수/관찰 판단에 써야 하는 것은 기말고사 성적표다.
그래서 현재 결과를 운영 Stage로 말하면 안 된다.
```

## 1. 실행 목적

v96에서 패치한 목적은 단순했다.

```text
이전 Census run에서 만든 FULL_THESIS blocker follow-up seed
→ 다음 Census Brain run에 외부 seed로 넣는다
→ 실제 Research Brain planner/source/claim/stagecourt 경로가 seed를 소비하는지 확인한다
```

이 실행은 운영 READY 선언이 아니라 wiring smoke다.

중요한 구분:

```text
seed가 Brain에 들어갔다
!=
FULL_THESIS Stage가 만들어졌다
```

## 2. 실행 명령

### 2.1 Seed source run

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-v97-seed-source \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
  --target-gate anti_fake \
  --write-operational-docs false \
  --fail-on-critical-audit false
```

확인 결과:

```text
exit = 0
printed status = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
research_brain_full_thesis_seed_events.jsonl rows = 85
research_brain_candidate_seed_events_used.jsonl rows = 85
```

이 run은 seed를 만드는 run이다. Brain/Web 실행 run이 아니다.

### 2.2 External seed real Brain smoke

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-v97-external-seed-real-brain-smoke \
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
  --brain-claim-extractor-provider rule_fallback \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --write-operational-docs false \
  --fail-on-critical-audit false
```

확인 결과:

```text
exit = 1
printed status = NOT_READY
```

이 실패는 일부 의도된 실패다.

```text
planner는 real provider로 1개만 성공하도록 제한했다.
claim extractor는 rule_fallback으로 둬서 real LLM extractor가 없게 했다.
```

그래서 이 run은 `external seed → real planner/source wiring`을 보는 smoke이지, 최종 운영 run이 아니다.

## 3. 파일 기준 교차검증

### 3.1 readiness verdict

파일:

```text
output/census_v4/2026-07-01-v97-external-seed-real-brain-smoke/readiness_verdict.json
```

핵심 값:

```text
verdict = NOT_READY
run_mode = BRAIN_AND_WEB_ACQUISITION_ENABLED
brain_web_mode = enabled
```

blockers:

```text
Brain/Web readiness gate blocked: LLM claim extractor has no real LLM provider runs
Brain/Web readiness gate blocked: Brain/Web operational minimum planner runs not met: 21/30
Brain/Web readiness gate blocked: Brain/Web operational minimum web search tasks not met: 3/20
Brain/Web readiness gate blocked: Brain/Web operational minimum web/news search calls not met: 3/20
Brain/Web readiness gate blocked: Brain/Web operational minimum fetched documents not met: 1/10
Brain/Web readiness gate blocked: Brain/Web operational minimum claim extractor attempts not met: 1/10
Brain/Web readiness gate blocked: Brain/Web operational minimum web/LLM accepted claims not met: 1/3
```

해석:

```text
현재 guard는 제대로 막고 있다.
거짓 READY가 아니다.
```

### 3.2 Brain/Web attempt audit

파일:

```text
output/census_v4/2026-07-01-v97-external-seed-real-brain-smoke/brain_web_attempt_audit.json
```

핵심 값:

```text
verdict = ATTEMPTED_WITH_SOURCE_TASKS
full_thesis_seed_source = external_candidate_event_seed_path
full_thesis_seed_original_path =
  output/census_v4/2026-07-01-v97-seed-source/research_brain_full_thesis_seed_events.jsonl
```

해석:

```text
v96에서 만든 외부 seed 입력 경로는 실제로 작동했다.
즉 "seed를 넘겨도 Brain이 안 봤다"는 문제는 일단 닫혔다.
```

하지만 이것은 운영 Stage 성공이 아니다.

### 3.3 Brain/Web readiness gate

파일:

```text
output/census_v4/2026-07-01-v97-external-seed-real-brain-smoke/brain_web_readiness_gate_audit.json
```

핵심 값:

```text
verdict = BLOCKED
brain_web_evidence_pass_allowed = false
full_thesis_seed_source = external_candidate_event_seed_path
```

해석:

```text
Brain/Web 시도는 있었지만, 운영 최소 증거량을 채우지 못했다.
```

좋은 점:

```text
부족한 상태를 낮은 점수나 Yellow/Red로 확정하지 않고 BLOCKED로 남겼다.
```

나쁜 점:

```text
아직 실제 운영 watchlist를 만들 수 있을 만큼 source/claim/stage closure가 없다.
```

### 3.4 FULL_THESIS seed materialization audit

파일:

```text
output/census_v4/2026-07-01-v97-external-seed-real-brain-smoke/full_thesis_seed_materialization_audit.json
```

핵심 값:

```text
verdict = PASS
ledger_integrity_pass_allowed = true
actual_materialization_pass_allowed = false
operator_materialization_status = PENDING_FULL_THESIS_MATERIALIZATION
```

중요:

```text
여기서 PASS는 장부 무결성 PASS다.
실제 FULL_THESIS 승급 PASS가 아니다.
```

쉬운 예:

```text
택배 송장 번호가 잘 만들어졌다.
하지만 택배가 도착한 것은 아니다.
```

### 3.5 goal completion audit

파일:

```text
output/census_v4/2026-07-01-v97-external-seed-real-brain-smoke/goal_completion_audit.json
```

핵심 blocker:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_smoke_execution_pending
full_thesis_production_pass_false
source_connector_capability_pending
full_thesis_seed_promotion_pass_false
source_backed_replay_parity_all_archetypes_pending
machine_readable_test_result_artifact_missing
goal_requirement_matrix_pass_false
```

해석:

```text
goal 완료 상태가 아니다.
다른 에이전트가 이 파일 하나만 봐도 완료 선언을 하면 안 된다.
```

## 4. Stage map 기준 교차검증

파일:

```text
output/census_v4/2026-07-01-v97-external-seed-real-brain-smoke/census_stage_map.csv
```

전체 row:

```text
rows = 3391
```

canonical_stage:

```text
0      = 3307
1      = 53
2      = 30
3-Red  = 1
```

stage_scope:

```text
CENSUS_EVENT_BOARD = 3390
BRAIN_WEB_PARTIAL  = 1
FULL_THESIS        = 0
```

score_scale:

```text
NO_SCORE               = 3324
EVENT_WEIGHTED_PARTIAL = 67
FULL_E2R_100           = 0
```

operator 사용 가능성:

```text
operator_stage_use = NOT_FULL_THESIS_STAGE 3391
operator_score_use = NOT_FULL_E2R_SCORE     3391
full_thesis_stage  = FULL_THESIS_NOT_RUN    3391
```

이게 가장 중요한 숫자다.

```text
모든 row가 operator_stage_use=NOT_FULL_THESIS_STAGE다.
따라서 운영자가 써도 되는 Stage는 0개다.
```

## 5. 예시 row 해석

### 5.1 삼성전자 005930

v97 stage map row 요약:

```text
symbol = 005930
company_name = 삼성전자
canonical_stage = 1
stage_scope = CENSUS_EVENT_BOARD
score_scale = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.0
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
is_full_thesis_stage = False
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
accepted_claim_count = 1
score_contribution_count = 1
```

해석:

```text
삼성전자에는 event-board Stage1 표시가 있다.
하지만 이것은 전체 투자 논리를 평가한 Stage1이 아니다.
공식 이벤트 하나를 확인한 상태판 Stage다.
```

쉬운 예:

```text
"삼성전자에 공시 하나가 있었음"은 확인했다.
하지만 "삼성전자가 HBM/C06 full thesis로 몇 점인지"는 아직 평가하지 않았다.
```

따라서 이 row를 보고 `삼성전자 Stage1`이라고 말하면 오해다.

정확한 표현:

```text
삼성전자 = Census event-board Stage1, 운영 FULL_THESIS 미실행
```

### 5.2 SK하이닉스 000660

v97 stage map row 요약:

```text
symbol = 000660
company_name = SK하이닉스
canonical_stage = 0
stage_scope = BRAIN_WEB_PARTIAL
score_scale = EVENT_WEIGHTED_PARTIAL
score_scope = BRAIN_WEB_CLAIM_BACKED_PARTIAL
event_evidence_score = 15.8333
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
is_full_thesis_stage = False
source_origin = research_brain_v4_attempt
accepted_claim_count = 1
score_contribution_count = 5
stage_signal = BRAIN_WEB_CLAIM_BACKED_STAGE
```

해석:

```text
SK하이닉스는 외부 seed가 Brain으로 들어가 partial claim-backed 점수까지 만들었다.
하지만 FULL_THESIS가 아니다.
```

특히 현재 row는 다음 이유로 운영 Stage가 아니다.

```text
claim extractor provider = rule_fallback
accepted Brain claim = 1개
source fetched document = 1개
full thesis missing primitives가 닫히지 않음
stage_scope = BRAIN_WEB_PARTIAL
score_scale = EVENT_WEIGHTED_PARTIAL
operator_stage_use = NOT_FULL_THESIS_STAGE
```

쉬운 예:

```text
HBM 관련 리포트 문장 하나를 찾아서 쪽지시험 점수는 냈다.
하지만 수주, capacity, 매출 mix, FCF/revision bridge를 모두 닫은 본시험은 아니다.
```

### 5.3 드래곤플라이 030350

v97 stage map row 요약:

```text
symbol = 030350
company_name = 드래곤플라이
canonical_stage = 3-Red
stage_scope = CENSUS_EVENT_BOARD
score_scale = EVENT_WEIGHTED_PARTIAL
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
stage_signal = RISK_REVIEW
event_evidence_score = 4.0
is_full_thesis_stage = False
full_thesis_stage = FULL_THESIS_NOT_RUN
```

해석:

```text
3-Red처럼 보이는 행도 운영 Red가 아니다.
event-board risk review 신호다.
```

따라서 다음처럼 말하면 안 된다.

```text
드래곤플라이 운영 Stage 3-Red 확정
```

정확한 표현:

```text
드래곤플라이 = Census event-board risk review, FULL_THESIS 미실행
```

## 6. Seed materialization trace 기준 교차검증

파일:

```text
output/census_v4/2026-07-01-v97-external-seed-real-brain-smoke/full_thesis_seed_materialization_trace.jsonl
```

row count:

```text
85
```

status count:

```text
PLANNER_NOT_RUN                         = 64
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 20
STAGECOURT_READY_NOT_PROMOTED            = 1
```

해석:

```text
85개 seed 중 1개만 real planner success -> source task -> accepted claim -> stagecourt까지 갔다.
그 1개도 FULL_THESIS로 승급하지 못했다.
```

### 6.1 STAGECOURT_READY_NOT_PROMOTED row

대상:

```text
symbol = 000660
candidate_event_id = CEV4-FTQUEUE-000660-9563b2a7a852fc0c
```

trace 요약:

```text
planner_run_count = 1
planner_real_provider_success_count = 1
source_task_execution_count = 7
accepted_claim_count = 1
score_contribution_count = 5
stagecourt_trace_count = 1
final_stage_scope = BRAIN_WEB_PARTIAL
final_score_scale = EVENT_WEIGHTED_PARTIAL
materialization_status = STAGECOURT_READY_NOT_PROMOTED
```

blockers:

```text
full_thesis_seed_stagecourt_trace_not_promoted_to_full_thesis
final_stage_scope=BRAIN_WEB_PARTIAL
final_score_scale=EVENT_WEIGHTED_PARTIAL
```

해석:

```text
Brain이 아예 멈춘 것은 아니다.
하지만 운영 Stage에 필요한 evidence closure가 부족해서 partial에서 멈췄다.
```

### 6.2 삼성전자 005930 seed row

대상:

```text
candidate_event_id = CEV4-FTQUEUE-005930-443618f53c122b15
symbol = 005930
```

trace 요약:

```text
materialization_status = PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS
planner_run_count = 1
planner_real_provider_success_count = 0
source_task_execution_count = 0
accepted_claim_count = 0
score_contribution_count = 0
stagecourt_trace_count = 0
final_stage_scope = CENSUS_EVENT_BOARD
final_score_scale = EVENT_WEIGHTED_PARTIAL
```

blocker:

```text
full_thesis_seed_planner_has_no_real_provider_success
```

해석:

```text
삼성전자는 이번 external seed smoke에서 full thesis Brain materialization을 실제로 못 했다.
따라서 삼성전자 운영 Stage/점수는 말하면 안 된다.
```

## 7. Brain/Web leaf artifact 기준 교차검증

v97 external seed smoke에서 주요 leaf count:

```text
research_brain_candidate_seed_events_used.jsonl = 85
planner_runs.jsonl                             = 21
source_task_executions.jsonl                   = 99
web_search_tasks.jsonl                         = 3
web_search_results.jsonl                       = 20
web_fetched_documents.jsonl                    = 1
evidence_documents.jsonl                       = 97
claim_extractor_runs.jsonl                     = 1
accepted_claims.jsonl                          = 93
score_contributions.jsonl                      = 97
stagecourt_traces.jsonl                        = 93
full_thesis_seed_materialization_trace.jsonl   = 85
```

주의:

```text
source_task_executions.jsonl = 99
accepted_claims.jsonl = 93
stagecourt_traces.jsonl = 93
```

이 숫자를 그대로 Brain/Web 성공 숫자로 읽으면 안 된다.

source_origin으로 필터링하면:

```text
source_task_executions source_origin=research_brain_v4_attempt = 7
accepted_claims source_origin=research_brain_v4_attempt        = 1
stagecourt_traces source_origin=research_brain_v4_attempt      = 1
```

쉬운 예:

```text
창고에 물건이 99개 있어도, 이번 택배로 온 물건은 7개뿐이다.
이번 run의 성과를 보려면 source_origin을 필터링해야 한다.
```

## 8. Planner / source / extractor 상세

### 8.1 Planner runs

파일:

```text
planner_runs.jsonl
```

count:

```text
total = 21
provider_mode none = 20
provider_mode real = 1
real_provider_success true = 1
real_provider_success false = 20
```

해석:

```text
--brain-planner-success-limit 1 설정 때문에 real planner 성공을 1개로 제한했다.
나머지 20개는 not_attempted_after_real_planner_limit 상태다.
```

즉 이것은 provider가 20번 실패했다는 뜻이 아니다.
이번 smoke 설정상 1개만 real planner로 열어 본 것이다.

### 8.2 Web/source acquisition

파일:

```text
web_search_tasks.jsonl
web_search_results.jsonl
web_fetched_documents.jsonl
source_task_executions.jsonl
```

Brain/Web attempt 기준:

```text
web_search_tasks = 3
web_search_results = 20
web_fetched_documents = 1
source_task_executions source_origin=research_brain_v4_attempt = 7
```

readiness gate 기준 최소치:

```text
web search tasks required = 20
web/news search calls required = 20
fetched documents required = 10
```

결론:

```text
현재 smoke는 source 수집량이 운영 최소치에 훨씬 못 미친다.
```

하지만 이것을 무작정 unbounded로 풀면 안 된다.

```text
production daily에서는 bounded SourceTask와 stop-on-resolution이 필요하다.
top_results=None, retry_max=None 같은 무제한 운영 run은 금지다.
```

### 8.3 Claim extractor

파일:

```text
claim_extractor_runs.jsonl
```

count:

```text
total = 1
provider_mode = rule_fallback
provider_name = rule_fallback_mention_extractor
status = SUCCESS
```

readiness blocker:

```text
LLM claim extractor has no real LLM provider runs
```

해석:

```text
이번 run은 LLM extractor 운영 검증이 아니다.
rule fallback으로 mention을 뽑았을 뿐이다.
```

다음 단계에서는 반드시 real LLM claim extractor를 붙여야 한다.

다만 LLM에게 점수를 직접 맡기면 안 된다.

```text
LLM 역할:
  문서에서 claim을 뽑고, 주체/시간/극성/관계 판단 재료를 낸다.

deterministic engine 역할:
  anchor/date/entity/temporal/mapping 검증 후 점수와 Stage를 계산한다.
```

### 8.4 Accepted Brain/Web claim

이번 run에서 Brain/Web attempt로 들어온 accepted claim sample:

```text
claim_id = CLM-2152d2804b4287169e70
symbol = 000660
source_provider = BrokerReportDomain
source_url = https://stock.pstatic.net/stock-research/company/17/20251031_company_162545000.pdf
primitive_id = customer_preorder_or_allocation
score_eligible = true
target_scope_status = DIRECT
temporal_status = CURRENT
source_origin = research_brain_v4_attempt
brain_web_claim = true
full_thesis_claim = false
```

해석:

```text
이 claim 하나는 Brain/Web partial score에 들어갔다.
하지만 full_thesis_claim=false다.
그래서 FULL_THESIS Stage로 승급하면 안 된다.
```

공격 포인트:

```text
1개 broker report claim만으로 C06/HBM full thesis를 닫을 수 없다.
고객 allocation, capacity, revenue mix, FCF/revision bridge, evidence family diversity가 더 필요하다.
```

## 9. 지금 잘 된 부분

### 9.1 거짓 READY를 막고 있다

현재 run은 `NOT_READY`로 끝났다.

이건 실패이지만 좋은 실패다.

```text
부족한 상태를 운영 Stage라고 포장하지 않았다.
```

예전 문제는 이런 식이었다.

```text
partial evidence
→ 높은 점수처럼 보임
→ Green/Yellow처럼 설명
→ 나중에 다른 run에서 60점/4C로 흔들림
```

현재 guard는 최소한 다음을 막는다.

```text
BRAIN_WEB_PARTIAL을 FULL_THESIS라고 부르기
EVENT_WEIGHTED_PARTIAL을 FULL_E2R_100이라고 부르기
rule_fallback claim extraction을 real LLM extraction이라고 부르기
```

### 9.2 외부 seed wiring은 닫혔다

v96 패치의 핵심이었던 외부 seed path는 실제로 소비됐다.

증거:

```text
brain_web_attempt_audit.full_thesis_seed_source = external_candidate_event_seed_path
brain_web_readiness_gate_audit.full_thesis_seed_source = external_candidate_event_seed_path
research_brain_candidate_seed_events_used.jsonl rows = 85
```

### 9.3 per-seed materialization blocker가 보인다

`full_thesis_seed_materialization_trace.jsonl`에서 seed별로 다음이 보인다.

```text
PLANNER_NOT_RUN
PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS
STAGECOURT_READY_NOT_PROMOTED
```

이제 막힌 위치를 숨기지 않는다.

## 10. 지금 잘못되고 있거나 아직 부족한 부분

### 10.1 운영 FULL_THESIS Stage는 0개다

가장 큰 문제:

```text
stage_scope=FULL_THESIS row = 0
score_scale=FULL_E2R_100 row = 0
operator_stage_use usable row = 0
```

따라서 현재 pipeline은 아직 운영 watchlist를 만들 수 없다.

### 10.2 Brain 실행 범위가 너무 작다

이번 smoke는 의도적으로 작게 돌렸다.

```text
brain_universe_limit = 2
brain_planner_success_limit = 1
max_source_tasks_per_plan = 2
max_fetches_per_task = 1
claim_extractor_provider = rule_fallback
```

이 설정으로는 운영 최소치를 채울 수 없다.

다만 해결책은 무제한 크롤링이 아니다.

필요한 것은:

```text
bounded but sufficient production preset
official-first source router
real LLM planner/extractor
stop-on-resolution
source-origin filtered readiness metrics
```

### 10.3 SK하이닉스 partial row의 archetype이 full thesis 의미로 신뢰되면 안 된다

SK하이닉스 row:

```text
large_sector_id = 메모리/HBM
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
stage_scope = BRAIN_WEB_PARTIAL
```

이 row는 full thesis archetype assignment로 보면 안 된다.

공격 포인트:

```text
HBM full thesis를 닫아야 하는데 partial row가 C05로 남아 있다.
이 상태에서 "하이닉스 HBM Stage"라고 말하면 또 의미가 흔들린다.
```

다음 patch에서는 Brain/Web partial archetype과 FULL_THESIS archetype을 분리해서 표시해야 한다.

### 10.4 materialization trace의 operator_score_use가 비어 있다

stage map에서는:

```text
operator_score_use = NOT_FULL_E2R_SCORE
```

하지만 materialization trace sample에서는:

```text
final_operator_score_use = null
```

이건 큰 scoring bug는 아니지만 audit schema gap이다.

다음 patch에서 trace에도 operator score/stage use를 같은 의미로 채워야 한다.

이유:

```text
다른 에이전트가 trace만 보고 "score use가 null이면 혹시 빠진 건가?"라고 공격할 수 있다.
```

### 10.5 source task total과 Brain/Web attempt count가 섞이면 오판한다

전체 source_task_executions는 99개다.
하지만 이번 Brain/Web attempt source task는 7개다.

따라서 모든 readiness metric과 문서는 반드시 다음 두 숫자를 분리해야 한다.

```text
all ledger artifact count
current Brain/Web attempt count
```

쉬운 예:

```text
기존 창고 재고와 오늘 입고량을 섞어 보면 안 된다.
```

## 11. 다음 패치 방향

### P0. Real LLM claim extractor 경로를 실제로 열기

현재 최대 blocker:

```text
LLM claim extractor has no real LLM provider runs
```

다음 run은 다음 중 하나여야 한다.

```text
--brain-claim-extractor-provider auto
또는 실제 Codex/LLM extractor provider
```

단, LLM 출력이 바로 score/stage를 결정하면 안 된다.

허용:

```text
LLM extracts assertion/claim candidates.
deterministic validator verifies anchor/date/entity/temporal/mapping.
deterministic scorer computes score.
```

금지:

```text
LLM says Green.
LLM says current_score_eligible=true.
LLM says 92점.
```

### P0. Seed materialization을 실제 FULL_THESIS closure까지 밀기

현재 seed trace는 이렇게 끝난다.

```text
85 seeds
→ 1 real planner success
→ 1 accepted Brain/Web claim
→ 1 BRAIN_WEB_PARTIAL StageCourt
→ 0 FULL_THESIS
```

다음 패치/실행은 이렇게 닫혀야 한다.

```text
seed
→ real planner
→ bounded source tasks
→ fetched source documents
→ real LLM claim extraction
→ accepted claims
→ primitive states
→ score contributions
→ score interval closure
→ StageCourt
→ stage_scope=FULL_THESIS
→ score_scale=FULL_E2R_100
→ operator_stage_use=USE_FULL_THESIS_STAGE
```

이 중 하나라도 빠지면 READY가 아니다.

### P0. partial과 full thesis를 출력 계층에서 더 강하게 분리

현재도 `operator_stage_use=NOT_FULL_THESIS_STAGE`로 막고 있지만, 사람이 `canonical_stage=1/2/3-Red`만 보면 헷갈릴 수 있다.

다음 패치 방향:

```text
canonical_stage_display에는 scope prefix 유지
operator-facing report는 full_thesis_stage 우선 표시
event-board Stage는 "상태판" 섹션으로만 출력
BRAIN_WEB_PARTIAL은 "부분 검증" 섹션으로만 출력
```

예:

```text
나쁜 출력:
  삼성전자 Stage1

좋은 출력:
  삼성전자: 운영 Stage 없음. Event-board Stage1 공시 감시만 존재.
```

### P1. materialization trace schema gap 보강

추가해야 할 필드:

```text
final_operator_stage_use
final_operator_score_use
final_full_thesis_stage
final_full_thesis_score_scale
final_is_full_e2r_score
final_is_full_thesis_stage
```

현재 stage map에는 있지만 trace에는 일부 빠져 있다.

### P1. current attempt metrics와 ledger total metrics 분리

모든 audit summary에 다음을 같이 둔다.

```text
total_ledger_count
current_attempt_count
current_attempt_source_origin_filter
```

예:

```text
source_task_executions_total = 99
source_task_executions_current_brain_attempt = 7
```

이렇게 해야 `99개나 돌았는데 왜 안 됐냐`와 `7개밖에 안 돌았다`를 구분할 수 있다.

### P1. FULL_THESIS archetype assignment와 partial archetype assignment 분리

현재 SK하이닉스는 HBM 섹터인데 partial primary_archetype이 C05로 보인다.

다음 필드를 분리해야 한다.

```text
event_board_primary_archetype
brain_partial_primary_archetype
full_thesis_primary_archetype
full_thesis_archetype_status
```

운영 출력은 `full_thesis_primary_archetype`만 full thesis 판단에 사용해야 한다.

### P2. 최소 운영 run preset 설계

현재 smoke는 너무 작고, backfill은 너무 넓다.

production daily용 중간 preset이 필요하다.

원칙:

```text
unbounded 금지
source task마다 max_queries/max_candidates/max_fetches 필수
official-first
web fallback 제한적 허용
real LLM planner/extractor 사용
stop-on-resolution
provider/source failure는 pending
```

예시:

```text
full_thesis_seed_count = 30
planner_real_success_target = 30
max_source_tasks_per_plan = 3
max_fetches_per_task = 2
claim_extractor_provider = real
minimum accepted Brain/Web claims = 3
minimum fetched documents = 10
```

숫자는 운영 비용과 provider 안정성을 보고 조정하되, readiness gate 숫자와 맞아야 한다.

## 12. 다음 에이전트 공격 체크리스트

다음 에이전트는 반드시 아래를 공격해야 한다.

```text
1. stage_scope=FULL_THESIS row가 실제로 생겼는가?
2. score_scale=FULL_E2R_100 row가 실제로 생겼는가?
3. operator_stage_use가 USE_FULL_THESIS_STAGE인 row가 있는가?
4. operator_score_use가 USE_FULL_E2R_SCORE인 row가 있는가?
5. BRAIN_WEB_PARTIAL을 FULL_THESIS처럼 말한 문서나 리포트가 남아 있는가?
6. rule_fallback claim extractor 결과를 real LLM 결과처럼 세고 있지 않은가?
7. source_task_executions total과 current attempt count를 섞고 있지 않은가?
8. accepted_claim 1개로 HBM/C06 Green 또는 full thesis를 닫고 있지 않은가?
9. event-board canonical_stage 1/2/3-Red를 운영 Stage로 출력하고 있지 않은가?
10. Samsung/Hynix row가 full thesis 미실행인데 운영 점수처럼 설명되고 있지 않은가?
11. materialization trace만 봐도 operator-use 불가가 명확한가?
12. source-backed replay parity all archetypes가 여전히 pending인데 READY라고 하지 않는가?
13. goal_completion_audit blockers가 남아 있는데 goal complete로 말하고 있지 않은가?
14. stage map과 readiness gate가 서로 다른 말을 하지 않는가?
15. as_of_date=2026-07-01 이후 문서가 score evidence에 들어가지 않는가?
```

## 13. 다음 실행에서 성공으로 인정할 수 있는 최소 조건

다음 중 하나라도 빠지면 성공이 아니다.

```text
readiness_verdict.verdict != NOT_READY
brain_web_readiness_gate_audit.brain_web_evidence_pass_allowed = true
full_thesis_seed_materialization_audit.actual_materialization_pass_allowed = true
at least one row with stage_scope=FULL_THESIS
at least one row with score_scale=FULL_E2R_100
at least one row with operator_stage_use=USE_FULL_THESIS_STAGE
at least one row with operator_score_use=USE_FULL_E2R_SCORE
claim_extractor_runs has real LLM provider run
full thesis row has nonzero ScoreContribution with accepted_claim_id support
score interval lower/upper closed for promoted row
source_origin filtered current Brain/Web attempt counts meet gate
```

운영 전체 목표 기준으로는 이것도 부족하다.

최종 goal은 여전히:

```text
모든 아키타입 source-backed replay parity
삼성전자/하이닉스 bounded live smoke
전역 adversarial suite
frozen corpus repeatability
parser keyword direct score path 0개
source_proxy_only production contribution 0개
```

까지 통과해야 한다.

## 14. 한 줄 판단

v97은 v96의 외부 seed 입력 경로가 실제 Brain run에 연결됐음을 증명했다.

하지만 현재 산출물은 아직:

```text
external seed wiring smoke PASS
Brain/Web readiness NOT_READY
FULL_THESIS materialization PENDING
operator usable Stage 0개
```

상태다.

따라서 다음 패치는 `더 그럴듯한 Stage 표시`가 아니라, 실제로 다음 사슬을 닫는 작업이어야 한다.

```text
external seed
→ real LLM planner
→ bounded source acquisition
→ real LLM claim extraction
→ deterministic validation
→ accepted claims
→ primitive states
→ score contributions
→ FULL_E2R_100 score
→ FULL_THESIS Stage
→ operator-use enabled row
```


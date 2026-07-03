# Census v4 2026-07-01 v102 Live Bounded Rerun Audit Patch And Remaining Blockers

작성일: 2026-07-03  
대상 run:

> 최신 후속 문서: `docs/0701/census_v4_0701_v104_stage_existence_extractor_retry_patch_and_final_review_packet_2026-07-03.md`  
> 이 v102 문서는 leaf audit/official partial replay 기준 문서다. v103에서 non-representative StageCourt trace blocker를 분리했고, v104에서 production claim extractor timeout compact/retry 패치를 추가했다. 최신 결론은 v104 문서를 우선한다.

```text
v101 live bounded rerun:
  output/census_v4/2026-07-01-v101-live-bounded-rerun

v102 audit replay from v101:
  output/census_v4/2026-07-01-v102-stage-scope-audit-replay-from-v101
```

## 한 줄 결론

Stage가 있는 애들은 있다. 하지만 아직 운영용 `FULL_THESIS` Stage는 0개다.

정확히는 다음 상태다.

```text
CENSUS_EVENT_BOARD:
  전 종목 상태판이다.
  예: "삼성전자도 이번 census에서 봤다", "공시 이벤트가 하나 있었다".
  이것만으로 운영 Stage/점수라고 말하면 안 된다.

BRAIN_WEB_PARTIAL / BRAIN_OFFICIAL_PARTIAL:
  Research Brain이 source-backed claim 일부를 받아 StageCourt까지 간 부분 Stage다.
  예: "하이닉스는 web/LLM claim 3개로 C06 일부 primitive가 닫혔다".
  이것도 full thesis가 아니므로 운영 점수/Stage라고 말하면 안 된다.

FULL_THESIS:
  운영에서 말하고 싶은 최종 thesis Stage다.
  현재 0개다.
```

쉬운 예:

```text
병원 접수표 = CENSUS_EVENT_BOARD
부분 검사 결과 = BRAIN_*_PARTIAL
최종 진단서 = FULL_THESIS

지금은 접수표와 부분 검사 결과는 생겼지만,
최종 진단서는 아직 한 장도 안 나온 상태다.
```

## 재현 명령

v101 live bounded rerun은 아래 조건으로 실행됐다.

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-v101-live-bounded-rerun \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider real \
  --brain-source-acquisition live_full_bounded \
  --brain-candidate-event-seed-path output/census_v4/2026-07-01-v97-seed-source/research_brain_full_thesis_seed_events.jsonl \
  --brain-universe-limit 30 \
  --brain-planner-success-limit 30 \
  --brain-planner-batch-size 5 \
  --brain-max-source-tasks-per-plan 3 \
  --brain-max-fetches-per-task 2 \
  --brain-retry-max 1 \
  --brain-claim-extractor-provider auto \
  --brain-claim-extractor-timeout-seconds 120 \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --write-operational-docs false \
  --fail-on-critical-audit false
```

결과:

```text
exit = 1
readiness_verdict.verdict = NOT_READY
target_gate = brain_web
target_gate_pass = false
```

즉 live path가 실제로 돌았지만, 목표 gate는 아직 통과하지 못했다.

## v101 Live 사실표

`output/census_v4/2026-07-01-v101-live-bounded-rerun/census_stage_status.jsonl`

```text
total rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD      3369
  BRAIN_WEB_PARTIAL          6
  BRAIN_OFFICIAL_PARTIAL    16
  FULL_THESIS                0

canonical_stage:
  0       3321
  1         47
  2         22
  3-Red      1

score_scale:
  NO_SCORE                3320
  EVENT_WEIGHTED_PARTIAL    71
  FULL_E2R_100               0

operator_stage_use:
  NOT_FULL_THESIS_STAGE   3391

operator_score_use:
  NOT_FULL_E2R_SCORE      3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN     3391
```

이 숫자의 의미:

```text
Stage row는 있다.
부분 Stage row도 22개 있다.
하지만 FULL_THESIS 운영 Stage row는 0개다.
```

## 삼성전자 / SK하이닉스 상태

v101 live와 v102 replay에서 동일하다.

```text
삼성전자 005930:
  stage_scope = CENSUS_EVENT_BOARD
  canonical_stage = 1
  base_stage = Stage1
  score_scale = EVENT_WEIGHTED_PARTIAL
  event_evidence_score = 4.0
  operator_stage_use = NOT_FULL_THESIS_STAGE
  operator_score_use = NOT_FULL_E2R_SCORE

SK하이닉스 000660:
  stage_scope = BRAIN_WEB_PARTIAL
  canonical_stage = 1
  base_stage = 1
  score_scale = EVENT_WEIGHTED_PARTIAL
  event_evidence_score = 60.0
  accepted_claim_count = 3
  accepted_web_llm_claim_count = 3
  operator_stage_use = NOT_FULL_THESIS_STAGE
  operator_score_use = NOT_FULL_E2R_SCORE
```

중요:

```text
삼성전자 Stage1은 Census/Event-board 상태다.
하이닉스 Stage1은 Brain/Web partial 상태다.
둘 다 FULL_THESIS 운영 Stage가 아니다.
```

따라서 지금 상태에서:

```text
"삼성전자 운영 Stage1이다"
"하이닉스 운영 점수 60점이다"
```

라고 말하면 과장이다.

정확한 표현은:

```text
삼성전자는 census/event-board 기준 Stage1 상태판 row가 있다.
하이닉스는 web/LLM claim-backed partial Stage1 row가 있다.
둘 다 full thesis refresh가 아직 안 끝났다.
```

## v101에서 실제로 확인된 Brain/Web 경로

`readiness_verdict.json` 기준:

```text
planner_run_count = 300
real_provider_success_count = 30
source_task_execution_count = 232
accepted_claim_count = 201
unique_accepted_claim_count = 123
brain_stagecourt_trace_exported_count = 22
brain_to_census_stage_exported_count = 22
```

Brain/Web readiness gate 세부:

```text
llm_planner_call_count = 300
llm_real_provider_success_count = 30
web_search_task_count = 73
web_search_call_count = 73
naver_search_call_count = 73
web_fetched_document_count = 51
llm_claim_extractor_attempt_count = 51
llm_claim_extractor_real_provider_count = 51
web_or_llm_accepted_claim_count = 80
official_accepted_claim_count = 43
brain_to_claim_trace_count = 123
brain_score_contribution_count = 64
brain_stage_trace_count = 22
snippet_to_score_count = 0
fake_provider_used_count = 0
provider_failure_final_score_count = 0
```

이 부분은 좋은 신호다.

```text
가짜 provider로 pass 처리한 것은 아니다.
snippet-only 점수도 없다.
provider failure를 final score로 확정하지도 않았다.
```

하지만 readiness는 아직 BLOCKED다.

```text
LLM claim extractor provider errors are unresolved: 5
LLM claim extractor timeouts are unresolved: 5
Brain/Web trace rows missing stagecourt_trace_id: 4
```

## v101 Leaf Audit 실패 원인

`output/census_v4/2026-07-01-v101-live-bounded-rerun/leaf_artifact_audit.json`

```text
verdict = FAIL
critical_count = 35

critical nonzero:
  stage_scope_invalid_count = 16
  official_claim_but_recent_official_event_zero_count = 19
```

이 실패는 두 가지 성격이다.

### 1. Auditor가 `BRAIN_OFFICIAL_PARTIAL`을 몰랐다

코드는 이미 official-only Brain trace를 `BRAIN_OFFICIAL_PARTIAL`로 올리고 있었다.

그런데 leaf auditor의 허용 scope 목록은 다음 세 개뿐이었다.

```text
CENSUS_EVENT_BOARD
BRAIN_WEB_PARTIAL
FULL_THESIS
```

그래서 `BRAIN_OFFICIAL_PARTIAL` 16개를 전부 invalid로 오판했다.

쉬운 예:

```text
새로운 "공식자료 부분검사" 양식이 생겼는데,
감사 체크리스트가 예전 "웹 부분검사" 양식만 알고 있어서
정상 서류를 "알 수 없는 서류"로 처리한 것이다.
```

### 2. 공식 claim row에 source task/document count가 0으로 남았다

`_promote_brain_stage_rows`는 partial row를 만들 때:

```text
accepted_official_claim_count > 0
```

을 넣으면서도:

```text
official_source_task_count = 0
official_evidence_document_count = 0
```

으로 고정했다.

그래서 auditor는 다음처럼 보는 게 맞았다.

```text
"공식 claim이 있다면서, 어떤 공식 source task/document에서 왔는지 상태판에는 0이다."
```

이건 점수 산식 문제가 아니라 provenance export 문제다.

## v102 패치 내용

패치 파일:

```text
src/e2r/census/census_v4_auditor.py
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_stage_promotion_gate.py
tests/test_census_v4_stage_signal_split.py
```

### Auditor 패치

`BRAIN_OFFICIAL_PARTIAL`을 정식 partial stage scope로 인정했다.

```text
허용 scope:
  CENSUS_EVENT_BOARD
  BRAIN_WEB_PARTIAL
  BRAIN_OFFICIAL_PARTIAL
  FULL_THESIS
```

또한 operator alias도 별도로 감사한다.

```text
brain_official_operator_alias_unscoped_count
```

### Promotion export 패치

`_promote_brain_stage_rows`에서 official claim ID를 기준으로 source task와 evidence document를 다시 연결한다.

새로 채우는 필드:

```text
official_source_task_count
official_evidence_document_count
official_source_task_ids
official_evidence_document_ids
```

이 패치는 점수를 올리지 않는다.

```text
나쁜 패치:
  official claim이 있으면 score +10

이번 패치:
  official claim이 있다면 그 claim이 어느 source task/document에서 왔는지 row에 남긴다.
```

즉 scoring rule이 아니라 감사 가능한 장부 보강이다.

## v102 Replay 검증

v102는 새 live run이 아니다.

```text
원본:
  v101 live bounded rerun artifact

적용:
  v102 코드의 official partial scope/source-count/sample bundle 규칙

출력:
  output/census_v4/2026-07-01-v102-stage-scope-audit-replay-from-v101
```

중간 replay:

```text
leaf_artifact_audit_after_v102_count_replay.json
  verdict = FAIL
  critical:
    sample_bundle_missing_scored_row_count = 19
```

이 실패는 stage row만 갱신하고 `sample_leaf_bundle.jsonl`을 같이 재생성하지 않아서 생긴 fingerprint mismatch다.

최종 replay:

```text
leaf_artifact_audit_after_v102_count_and_sample_replay.json
  verdict = PASS
  critical_nonzero = {}
  sample_leaf_bundle_count = 71

stage_scope:
  CENSUS_EVENT_BOARD      3369
  BRAIN_WEB_PARTIAL          6
  BRAIN_OFFICIAL_PARTIAL    16
```

이 replay가 증명하는 것:

```text
v101의 leaf audit critical 35개 중
stage_scope invalid / official source-count 누락은 코드 패치로 닫힌다.
```

이 replay가 증명하지 않는 것:

```text
Brain/Web readiness가 통과했다.
FULL_THESIS가 생겼다.
삼성/하이닉스 운영 Stage가 확정됐다.
```

## 전체 테스트

실행:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5127 tests in 236.755s
OK
```

Focused tests:

```text
tests.test_census_v4_brain_stage_promotion_gate
tests.test_census_v4_stage_signal_split

Ran 30 tests
OK
```

## 남은 blocker

### Blocker 1. Brain/Web readiness gate는 아직 BLOCKED

v101 live:

```text
brain_web_readiness_gate.verdict = BLOCKED

blockers:
  LLM claim extractor provider errors are unresolved: 5
  LLM claim extractor timeouts are unresolved: 5
  Brain/Web trace rows missing stagecourt_trace_id: 4
```

5개 timeout 문서:

```text
DOC-aae5960126bafd0a2b98
DOC-ca0a3349e430c1e3ee8f
DOC-ff56a163d7463e5f8db9
DOC-b14a824d662ef08fb230
DOC-5147052c9ccbbc98d48e
```

4개 missing stagecourt trace는 모두 `017670` 쪽 claim이다.

```text
symbol = 017670
source_task_id = CEV4-FTQUEUE-017670-68d3847c4d85f7ed-T2
score_contribution_id = None
trace_status = CLAIM_EXPORTED_STAGE_NOT_PROMOTED
```

다음 패치 방향:

```text
1. extractor timeout은 문서 chunk/compact payload/retry 정책을 확인한다.
   단, timeout 문서를 무시하고 pass 처리하면 안 된다.

2. stagecourt_trace_id 없는 claim은 두 갈래로 분리한다.
   - score contribution이 없는 non-representative claim이면
     "stage 미승격 보조 claim"으로 명시하고 readiness blocker에서 제외할 수 있다.
   - score contribution이 있거나 representative claim이면
     반드시 StageCourt trace를 만들거나 실행 실패로 남겨야 한다.

3. 위 판단도 claim/source row 기준으로 해야지, symbol 예외로 처리하면 안 된다.
```

쉬운 예:

```text
병원 검사에서 참고 메모 4개가 최종 진단서에 안 들어간 것은 정상일 수 있다.
하지만 그 메모가 실제 진단 점수에 쓰였는데 진단서 번호가 없다면 심각한 오류다.
따라서 "점수에 쓰인 claim인가?"를 먼저 봐야 한다.
```

### Blocker 2. FULL_THESIS production은 아직 0개

`full_thesis_production_runner_audit.json`

```text
verdict = PENDING_PRODUCTION_FULL_THESIS
candidate_row_count = 22
blocked_candidate_count = 22
promoted_full_thesis_row_count = 0
blocked_candidate_follow_up_source_task_count = 53
blocked_candidate_follow_up_seed_event_count = 53
```

주요 missing primitive:

```text
contract_amount_to_prior_sales
contract_duration_months
delivery_schedule
hbm_capacity_constraint
hbm_capacity_pre_sold
margin_bridge_visible
```

하이닉스 예:

```text
present_primitives:
  customer_preorder_or_allocation
  medium_term_revision_visibility
  revenue_visibility_contract

missing_green_primitives:
  hbm_capacity_constraint
  hbm_capacity_pre_sold

결론:
  C06 일부 증거는 있지만, Green/full thesis gate를 닫기에는 아직 부족하다.
```

주의:

```text
"하이닉스가 나쁘다"가 아니다.
"현재 운영 leaf 장부에서 full thesis gate를 닫을 claim이 아직 없다"가 맞다.
```

### Blocker 3. All-archetype source-backed replay는 아직 6/32

`all_archetype_replay_matrix.json`

```text
required_archetype_count = 32
source_backed_ready_count = 6
missing_required_archetype_count = 26
```

따라서 전 아키타입 운영 준비 완료라고 말하면 안 된다.

다음 패치 방향:

```text
source_proxy_only 연구자료를 운영 정답으로 쓰지 말고,
각 아키타입별 source-backed replay fixture를 Evidence OS 경로로 닫아야 한다.
```

## 다음 에이전트가 공격해야 할 질문

1. `017670`의 missing `stagecourt_trace_id` 4개는 정말 non-representative claim인가?

확인할 것:

```text
brain_to_claim_trace.jsonl
accepted_claims.jsonl
score_contributions.jsonl
stagecourt_traces.jsonl
source_task_executions.jsonl
```

판단 기준:

```text
score_contribution_id가 없고 representative score row에 쓰이지 않았으면
readiness blocker가 아니라 explicit non-representative trace로 내려야 한다.

score_contribution_id가 있거나 score support에 쓰였으면
StageCourt trace 누락이므로 critical blocker가 맞다.
```

2. extractor timeout 5개는 문서 크기/프롬프트 크기/CLI timeout 중 무엇 때문인가?

확인할 것:

```text
claim_extractor_runs.jsonl
llm_prompts.jsonl
llm_responses.jsonl
web_fetched_documents.jsonl
```

패치 원칙:

```text
timeout 문서를 조용히 폐기하지 않는다.
material source gap이면 Pending으로 남긴다.
다만 하나의 timeout이 전체 Brain/Web readiness를 막아야 하는지는
그 문서가 representative/material gap에 연결됐는지로 판단한다.
```

3. FULL_THESIS runner가 22개 candidate를 전부 막은 이유가 합리적인가?

확인할 것:

```text
full_thesis_production_runner_audit.json
full_thesis_blocker_follow_up_source_tasks.jsonl
full_thesis_blocker_follow_up_seed_events.jsonl
full_thesis_refresh_queue.jsonl
```

검증 기준:

```text
missing primitive가 실제 Green/full thesis 필수인지
이미 accepted claim으로 닫힌 primitive를 중복으로 missing 처리한 것은 아닌지
follow-up SourceTask가 official-first bounded shell로 남았는지
LLM planner가 실제 query를 생성할 수 있는 입력을 받는지
```

4. `CENSUS_EVENT_BOARD` Stage1/Stage2를 사용자가 운영 Stage로 오해하지 않게 출력이 충분히 방어적인가?

확인할 것:

```text
operator_stage_use
operator_score_use
operator_scope_note
base_stage_display
score_scale_display
full_thesis_stage
```

합격 기준:

```text
Event-board Stage는 항상 EVENT_BOARD_ prefix가 붙는다.
Partial Stage는 BRAIN_WEB_PARTIAL_ 또는 BRAIN_OFFICIAL_PARTIAL_ prefix가 붙는다.
FULL_THESIS가 아니면 operator_stage_use는 NOT_FULL_THESIS_STAGE다.
FULL_E2R_100이 아니면 operator_score_use는 NOT_FULL_E2R_SCORE다.
```

5. 삼성전자/하이닉스를 다시 운영처럼 말하지 않는가?

검증 기준:

```text
삼성전자 = CENSUS_EVENT_BOARD Stage1, event score 4.0, not full thesis
SK하이닉스 = BRAIN_WEB_PARTIAL Stage1, event score 60.0, not full thesis
```

이 둘을 운영 점수나 Green/Yellow 확정처럼 설명하면 실패다.

## 이번 패치가 하드코딩이 아닌 이유

이번 패치는 종목명, 아키타입명, 특정 키워드로 점수를 바꾸지 않는다.

하지 않은 것:

```text
if symbol == "005930": ...
if "HBM" in text: score += ...
if source_provider == "OpenDART": promote Green
```

한 것:

```text
accepted official claim ID
  -> source_task_executions의 accepted_claim_ids와 연결
  -> document_id와 연결
  -> stage row에 provenance count/id를 남김
```

즉 점수판을 바꾼 게 아니라, 이미 존재한 claim의 영수증 번호를 상태판에 붙인 것이다.

## 최종 상태

```text
v101 live:
  실제 Brain/Web/LLM 경로는 돌았다.
  partial Stage 22개가 있다.
  FULL_THESIS는 0개다.
  readiness는 NOT_READY다.
  leaf audit은 official partial scope/source-count export 문제로 FAIL이었다.

v102 code patch + replay:
  official partial scope/source-count 문제는 닫혔다.
  sample bundle까지 같이 재생성하면 leaf audit PASS다.
  전체 테스트 5127개 OK다.

아직 안 된 것:
  Brain/Web readiness BLOCKED
  FULL_THESIS production 0개
  all-archetype source-backed replay 6/32
  삼성/하이닉스 운영 Stage 확정 아님
```

다음 작업의 우선순위:

```text
1. 017670 missing stagecourt_trace_id 4개를 representative/material 여부로 분류하고 trace 상태를 고친다.
2. LLM extractor timeout 5개를 문서 크기/timeout/retry 정책 기준으로 처리한다.
3. FULL_THESIS blocked candidate 22개를 missing primitive별로 follow-up SourceTask -> LLM planner -> accepted claim -> StageCourt까지 닫는다.
4. C01~C32 source-backed replay coverage 6/32를 늘린다.
5. 그 뒤에야 삼성/하이닉스 같은 종목을 운영 파이프라인으로 다시 말할 수 있다.
```

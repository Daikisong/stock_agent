# Census v4 0701 Next Agent Hard Review After Metricsplit

작성 시점: 2026-07-02 KST  
repo: `/home/eorb915/projects/stock_agent`  
canonical output: `output/census_v4/2026-07-01`  
latest Brain/Web diagnostic: `output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1`  
as_of_date: `2026-07-01`

> 최신 주의: 이 문서는 `metricsplit-v1` 기준 공격 문서다.
> 이후 `census_v4_0701_brain_web_promotion_guard_patch_result_2026-07-02.md`에서
> official-only `BRAIN_WEB_PARTIAL` 승격을 차단했다.
> 이후 `census_v4_0701_raw_assertion_rejection_audit_patch_and_stage_truth_2026-07-02.md`에서
> rejected RAW assertion 단위 장부와 fallback reason 분류를 추가했다.
> 최신 Brain/Web diagnostic은 `rawreject-v4`이며, `BRAIN_WEB_PARTIAL row = 0`,
> `web_or_llm_accepted_claim_count = 0`, `FULL_THESIS row = 0`이다.

이 문서는 `metricsplit-v1` 당시 공격 문서다. 다음 에이전트는 README의 최신 읽는 순서를 우선한다.

## 직접 답

```text
Stage가 있는 애들은 있다.
하지만 운영 FULL_THESIS Stage가 있는 애들은 아직 없다.
```

숫자로 나누면:

```text
canonical output:
  CENSUS_EVENT_BOARD row = 3391
  event-board non-Stage0 row = 85
  FULL_THESIS row = 0
  FULL_E2R_100 verified score row = 0

latest metricsplit diagnostic:
  CENSUS_EVENT_BOARD row = 3390
  BRAIN_WEB_PARTIAL row = 1
  FULL_THESIS row = 0
  FULL_E2R_100 verified score row = 0
  web_or_llm_accepted_claim_count = 0
```

쉬운 예:

```text
지금 있는 Stage는 출석부 상태 표시다.
예: 오늘 확인함, 공시 있음, 자료 부족, 감시 필요.

우리가 원하는 Stage는 근거가 붙은 기말고사 채점지다.
예: C06 thesis의 고객 배정, capacity, revenue mix, FCF bridge가 확인되어 87점 Yellow.

출석부는 있다.
기말고사 채점지는 아직 없다.
```

## 최신 단일 진실

### 1. Canonical output은 아직 ledger-refresh 상태판이다

검증 파일:

```text
output/census_v4/2026-07-01/census_stage_summary.json
output/census_v4/2026-07-01/readiness_verdict.json
output/census_v4/2026-07-01/goal_completion_audit.json
output/census_v4/2026-07-01/goal_requirement_matrix_audit.json
```

핵심:

```text
stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391

operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE = 3391

score_scope_distribution:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
verified_score_present_count = 0
```

해석:

```text
Stage0/Stage1/Stage2-Watch/Red label은 있다.
그러나 이 label은 Census 상태판 label이다.
운영자가 Green/Yellow/Red thesis 판정으로 쓰면 안 된다.
```

### 2. Latest Brain/Web diagnostic은 web/LLM evidence pass가 아니다

검증 파일:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1/readiness_verdict.json
output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1/brain_stage_promotion_audit.json
output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1/census_stage_summary.json
output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1/accepted_claims.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1/raw_assertions.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1/claim_extractor_runs.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1/web_fetched_documents.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1/web_rejected_documents.jsonl
```

Gate 핵심:

```text
verdict = BLOCKED
brain_web_evidence_pass_allowed = false

brain_accepted_claim_count = 1
official_accepted_claim_count = 1
web_news_accepted_claim_count = 0
llm_extracted_accepted_claim_count = 0
web_or_llm_accepted_claim_count = 0
full_thesis_claim_count = 0

llm_planner_call_count = 22 / required 30
web_search_task_count = 3 / required 20
web_search_call_count = 3 / required 20
web_fetched_document_count = 4 / required 10
llm_claim_extractor_attempt_count = 4 / required 10
web_or_llm_accepted_claim_count = 0 / required 3
```

Blockers:

```text
web/LLM accepted claim count is zero
Brain/Web operational minimum planner runs not met: 22/30
Brain/Web operational minimum web search tasks not met: 3/20
Brain/Web operational minimum web/news search calls not met: 3/20
Brain/Web operational minimum fetched documents not met: 4/10
Brain/Web operational minimum claim extractor attempts not met: 4/10
Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

중요한 함정:

```text
accepted_claims.jsonl line count = 93
```

이 숫자를 그대로 Brain/Web accepted evidence로 읽으면 안 된다.
그 파일에는 canonical official/census ledger claim이 같이 있다.
Brain/Web readiness gate가 이번 Brain/Web cutover에 의미 있게 본 accepted claim은 1개이고,
그 1개도 OpenDART official claim이다.

쉬운 예:

```text
창고 전체 영수증은 93장이다.
그런데 "웹/LLM이 새로 찾아서 채점표에 붙인 영수증"은 0장이다.
창고 영수증 93장을 보고 "웹/LLM 성공"이라고 말하면 안 된다.
```

### 3. LLM extractor는 이제 호출 자체는 성공한다

`metricsplit-v1`에서:

```text
claim_extractor_runs.jsonl line count = 4
status = SUCCESS 4건
provider_name = codex_cli_contract_blind_extractor
raw_assertions.jsonl line count = 125
web_fetched_documents.jsonl line count = 4
```

해석:

```text
이전 문제:
  Codex extractor schema/provider 오류로 LLM extraction 자체가 실패.

현재 문제:
  LLM이 웹 문서에서 raw assertion은 만들지만,
  accepted score claim으로 통과한 web/news/LLM claim이 0개.
```

쉬운 예:

```text
전에는 답안지가 제출되지 않았다.
지금은 답안지가 제출된다.
하지만 채점 기준에 맞는 정답으로 인정된 문항은 아직 없다.
```

### 4. Web rejection ledger는 이제 남는다

`metricsplit-v1`에서:

```text
web_fetched_documents.jsonl line count = 4
web_rejected_documents.jsonl line count = 5
post_extraction_evidence_os rejection row = 4
```

대표 rejection:

```text
rejection_phase = post_extraction_evidence_os
rejection_reason = post_extraction_no_score_eligible_claim
accepted_claim_ids = []
raw_assertion_ids = [...]
snippet_score_forbidden = true
```

해석:

```text
웹 문서를 읽고도 왜 점수로 못 썼는지 문서 단위 영수증은 생겼다.
하지만 raw assertion 하나하나가 target/temporal/primitive/mapping 중 어디서 탈락했는지
다음 패치에서 더 세밀하게 쪼개야 한다.
```

## 이번 패치로 좋아진 점

### A. Post-extraction web rejection ledger

코드 위치:

```text
src/e2r/research_brain/v4_evidence_extraction_bridge.py
  _append_post_extraction_web_rejection_if_needed
  _post_extraction_web_rejection_reason
```

효과:

```text
웹 문서 fetch 성공
-> LLM extraction/adjudication/mapping 실행
-> accepted claim 없음
-> web_rejected_documents.jsonl에 post_extraction_evidence_os row 기록
```

이전에는 웹 문서가 조용히 사라질 수 있었다.
이제는 "읽었는데 왜 점수로 못 썼는지" 최소 문서 단위로 남는다.

### B. Official claim과 web/LLM claim split

코드 위치:

```text
src/e2r/census/census_runner_v4.py
  _brain_web_readiness_gate_audit
  _accepted_claim_is_web_news_source
  _accepted_claim_is_llm_extracted
  _accepted_claim_is_official_source
```

효과:

```text
OpenDART accepted claim 1개
-> brain_accepted_claim_count = 1
-> official_accepted_claim_count = 1
-> web_or_llm_accepted_claim_count = 0
-> Brain/Web evidence pass blocked
```

이전에는 `accepted claim 있음`이라는 말이 웹/LLM evidence 성공처럼 보일 수 있었다.
이제는 official-only claim이 gate를 통과시키지 못한다.

## 아직 위험한 지점

### P0-1. `BRAIN_WEB_PARTIAL` 1개가 official-only로도 승격된다

현재 `brain_stage_promotion_audit.json`:

```text
verdict = PROMOTION_APPLIED
brain_promoted_stage_row_count = 1
brain_claim_count = 1
```

하지만 readiness gate:

```text
official_accepted_claim_count = 1
web_or_llm_accepted_claim_count = 0
brain_web_evidence_pass_allowed = false
```

즉 이름은 `BRAIN_WEB_PARTIAL`인데 실제 accepted score claim은 official-only다.
운영 gate는 막지만, label이 과대해석될 수 있다.

다음 패치 방향:

```text
옵션 A:
  BRAIN_AND_WEB mode에서 web_or_llm_accepted_claim_count == 0이면
  BRAIN_WEB_PARTIAL promotion 자체를 막는다.

옵션 B:
  official-only이면 BRAIN_WEB_PARTIAL이 아니라
  BRAIN_OFFICIAL_PARTIAL 또는 OFFICIAL_REFRESH_PARTIAL로 별도 label을 쓴다.

권장:
  운영 혼선을 줄이려면 BRAIN_WEB_PARTIAL은 web/news 또는 LLM-extracted accepted claim이
  최소 1개 있을 때만 허용한다.
```

쉬운 예:

```text
"웹 조사반이 찾은 증거"라는 스티커를 붙였는데,
실제로는 DART 공시만 본 경우다.
스티커 이름이 틀리면 다음 사람이 "웹도 됐네"라고 오해한다.
```

필수 테스트:

```text
official-only accepted claim fixture:
  brain_stage_promotion_mode = strict
  web_or_llm_accepted_claim_count = 0
  expected:
    BRAIN_WEB_PARTIAL row = 0
    or stage_scope = OFFICIAL_REFRESH_PARTIAL
    readiness verdict = BLOCKED
```

### P0-2. Raw assertion 탈락 사유가 아직 너무 뭉뚱그려져 있다

현재 문서 단위 rejection은 생긴다.
하지만 다음 질문에 아직 바로 답하기 어렵다.

```text
RAWLLM-...는 왜 accepted claim이 안 됐나?
  target이 달랐나?
  날짜/current성이 안 맞았나?
  primitive mapping이 실패했나?
  source anchor는 있었는데 score eligibility가 false였나?
  gap과 무관한 claim이었나?
```

다음 패치 방향:

```text
llm_raw_assertion_rejection_audit.jsonl 추가

필드 예:
  raw_assertion_id
  document_id
  source_task_id
  symbol
  primitive_gap
  target_scope_status
  temporal_status
  polarity
  mapping_status
  score_eligibility_status
  rejection_reason
  rejected_by_stage
  accepted_claim_id_if_any
```

쉬운 예:

```text
웹 기사를 읽고 문장 10개를 뽑았다.
지금은 "이 기사 전체가 점수로 못 들어감"만 보인다.
다음에는 "10개 문장 중 7개는 타사 이야기, 2개는 과거 회고, 1개는 primitive mismatch"까지 보여야 한다.
```

### P0-3. FULL_THESIS production row는 여전히 0개다

현재 canonical:

```text
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
```

이 값은 정상적으로 보수적이다.
문제는 아직 생산 못 한다는 것이지, fake로 만들지 않았다는 점은 오히려 좋다.

다음 패치 방향:

```text
accepted claim
-> primitive state
-> score contribution
-> StageCourt trace
-> full_thesis_claim=true
-> FULL_THESIS / FULL_E2R_100 row
```

단, controlled smoke나 replay fixture를 production row로 바꾸면 안 된다.

쉬운 예:

```text
운전 연습장에서 차가 굴러간 것과 실제 도로 주행 허가는 다르다.
controlled smoke는 연습장이고, production FULL_THESIS는 실제 도로다.
```

### P0-4. All-archetype source-backed replay parity가 6/32다

현재:

```text
required_archetype_count = 32
source_backed_ready_count = 6
guard_replay_ready_count = 6
missing_required_archetype_count = 26
```

Ready:

```text
C06, C08, C15, C17, C24, C28
```

Pending:

```text
나머지 required archetype 26개
```

주의:

```text
all_archetype_replay_matrix.json total archetype row = 36
C01~C32 required = 32
R13_* cross-archetype guard = 4
```

따라서 26개 pending과 36개 total row는 모순이 아니다.

다음 패치 방향:

```text
source_proxy_only research row를 정답 fixture로 쓰지 않는다.
각 pending archetype마다 URL/source-backed positive replay와 guard replay를 만든다.
```

## 다음 에이전트 공격 질문

다음 에이전트는 최소 아래 질문에 답해야 한다.

```text
1. 왜 BRAIN_WEB_PARTIAL이 official-only claim으로 승격되는가?
2. BRAIN_WEB_PARTIAL label을 막거나 rename하지 않으면 사용자에게 어떤 오해가 생기는가?
3. RAWLLM raw assertion 29개가 왜 accepted claim 0개로 끝나는가?
4. post_extraction_no_score_eligible_claim 내부 사유를 raw assertion 단위로 복원할 수 있는가?
5. accepted_claims.jsonl 전체 93개와 gate의 brain_accepted_claim_count=1을 섞어 말하는 문서/코드가 없는가?
6. metricsplit diagnostic은 target_gate=brain_web 실행인데 canonical output처럼 말하는 곳은 없는가?
7. controlled smoke FULL_THESIS와 production FULL_THESIS를 섞는 문서/코드는 없는가?
8. event-board Stage 85개를 operational Stage처럼 쓰는 출력은 없는가?
9. web fetch count, extractor attempt count, web_or_llm accepted count가 minimum gate에 못 미치는 상태에서 NOT_READY가 확실히 유지되는가?
10. 다음 patch가 점수 threshold를 낮추거나 fake fixture를 넣는 방식으로 pass를 만들지 않는가?
```

## 재현 명령

최신 Brain/Web diagnostic 재실행:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01-brain-web-diagnostic-metricsplit-v1 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --research-brain-report-dir docs/operational \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 1 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-fetches-per-task 1 \
  --brain-claim-extractor-provider codex_cli \
  --brain-stage-promotion-mode strict \
  --full-thesis-smoke-mode disabled \
  --target-gate brain_web \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim false \
  --fail-on-atomic-mismatch false \
  --fail-on-semantic-guard false \
  --fail-on-critical-audit false \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --write-operational-docs false
```

현재 기대 결과:

```text
stdout = NOT_READY
readiness_verdict.verdict = NOT_READY
brain_web_readiness_gate.verdict = BLOCKED
web_or_llm_accepted_claim_count = 0
FULL_THESIS row = 0
```

이 상태에서 `READY`, `PASS`, `FULL_THESIS > 0`가 나오면 반드시 diff를 감사해야 한다.

## 테스트 명령

이번 문서 기준 패치와 관련된 최소 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_bundle_export \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_cutover_contract_blind_extraction \
  tests.test_research_brain_v4_operational_modes -v
```

문서 작성 시점의 최근 실행 결과:

```text
combined targeted regression:
  Ran 55 tests
  OK
```

최종 완료라고 말하려면 이 정도로는 부족하다.
전체 repo test artifact는 이미 canonical output에 `4997`개 통과로 남아 있지만,
goal completion blocker 4개가 남아 있다.

## 절대 하면 안 되는 것

```text
1. event-board Stage를 FULL_THESIS로 rename하기.
2. BRAIN_WEB_PARTIAL을 운영 Stage로 출력하기.
3. OpenDART official claim을 web/LLM accepted claim으로 세기.
4. source_proxy_only research row를 production score fixture로 쓰기.
5. controlled smoke row를 production FULL_THESIS row로 대체하기.
6. web_or_llm accepted claim이 0인데 Brain/Web pass를 true로 바꾸기.
7. threshold를 낮춰서 FULL_THESIS를 만들기.
8. 종목명 예외로 삼성전자/하이닉스만 통과시키기.
9. LLM raw assertion을 source anchor 없이 score contribution으로 넣기.
10. 검색 실패를 ABSENT 또는 낮은 점수 확정으로 처리하기.
```

## 다음 패치 우선순위

### Patch 1. Brain/Web partial promotion source-class guard

목표:

```text
BRAIN_WEB_PARTIAL이라는 label은 web/news 또는 LLM-extracted accepted claim이 있을 때만 허용한다.
official-only accepted claim은 BRAIN_WEB_PARTIAL로 승격하지 않는다.
```

검증:

```text
official-only fixture:
  web_or_llm_accepted_claim_count = 0
  expected BRAIN_WEB_PARTIAL row = 0

web/LLM accepted fixture:
  web_or_llm_accepted_claim_count >= 1
  expected BRAIN_WEB_PARTIAL row allowed, but still NOT FULL_THESIS
```

### Patch 2. Raw assertion rejection audit

목표:

```text
문서 단위 rejection을 raw assertion 단위 rejection으로 확장한다.
```

검증:

```text
web_fetched_documents 4개
claim_extractor_runs 4개
raw assertions 있음
accepted web/LLM claim 0개
-> raw assertion rejection audit가 raw assertion 수와 연결되어야 한다.
```

### Patch 3. Accepted web/LLM claim unblock

목표:

```text
LLM raw assertion 중 source-backed, direct target, current, primitive-mapped claim이
최소 1개 accepted claim으로 통과하는 실제 사례를 만든다.
```

주의:

```text
통과시키려고 기준을 낮추면 안 된다.
탈락 이유를 보고 planner/source acquisition/extractor/mapper 중 어디가 약한지 고친다.
```

### Patch 4. Production FULL_THESIS runner

목표:

```text
accepted claim -> primitive -> score contribution -> StageCourt trace가 닫힌 row만
FULL_THESIS / FULL_E2R_100로 승격한다.
```

### Patch 5. C01~C32 replay parity

목표:

```text
source_backed_ready_count 6/32 -> 32/32
guard_replay_ready_count 6/32 -> 32/32
```

## 최종 판단

```text
뭔가 잘못되고 있는가?
  일부는 맞다. BRAIN_WEB_PARTIAL label은 official-only claim으로도 생겨서 오해 소지가 있다.

Stage가 있는 애들이 있나?
  있다. event-board Stage 85개와 metricsplit BRAIN_WEB_PARTIAL 1개가 있다.

그 Stage를 운영 Stage로 써도 되나?
  아니다. FULL_THESIS row와 FULL_E2R_100 verified score는 0개다.

이번 패치로 나아진 점은?
  web 문서 rejection ledger가 남고,
  official accepted claim과 web/LLM accepted claim이 gate에서 분리됐다.

다음에 제일 먼저 고칠 것은?
  official-only BRAIN_WEB_PARTIAL promotion을 막거나 rename하고,
  RAWLLM raw assertion이 왜 accepted claim이 안 되는지 assertion 단위로 감사하는 것이다.
```

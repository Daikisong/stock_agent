# Census v4 0701 SourceQuality v8 Deep Cross-Validation And v9 Patch Direction

작성일: 2026-07-02

이 문서는 다음 에이전트가 강하게 반박할 수 있도록, 2026-07-01 Census v4 최신 Brain/Web 진단(`sourcequality-v8`)을 원본 산출물 기준으로 다시 대조한 감사 노트다.

결론부터 말하면:

```text
Stage label이 있는 row는 있다.
하지만 운영 FULL_THESIS Stage는 아직 없다.

v8에서는 LLM planner, live source acquisition, web full-source fetch, LLM claim extraction까지 일부 도달했다.
하지만 이번 Brain/Web attempt가 만든 accepted claim은 0개이고,
claim-backed score contribution도 0개이며,
Brain/Web StageCourt trace도 0개다.
```

쉬운 예:

```text
출석부에는 "Stage1", "Stage2"라고 적힌 학생이 있다.
하지만 그건 "오늘 출석/상태판"이고, 최종 시험 답안지를 채점한 점수가 아니다.

운영 Stage는 답안지 원문 claim -> primitive -> score contribution -> StageCourt까지 닫혀야 한다.
v8에서는 그 닫힌 경로가 아직 0개다.
```

## 1. 감사 대상 산출물

최신 진단:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v8
```

주요 파일:

```text
brain_web_readiness_gate_audit.json
brain_web_attempt_audit.json
brain_stage_promotion_audit.json
planner_runs.jsonl
source_tasks.jsonl
source_task_executions.jsonl
web_search_tasks.jsonl
web_fetched_documents.jsonl
web_rejected_documents.jsonl
claim_extractor_runs.jsonl
raw_assertion_rejections.jsonl
brain_claim_mapping_trace.jsonl
accepted_claims.jsonl
score_contributions.jsonl
stagecourt_traces.jsonl
census_stage_status.jsonl
goal_completion_audit.json
readiness_verdict.json
samsung_hynix_full_thesis_smoke.json
```

최신 테스트 증거:

```text
targeted local regression:
  tests.test_research_brain_v4_operational_modes
  selected census/brain tests
  Ran 24 + 84 tests / OK

full unittest:
  output/test_full_repo_0701/full_unittest_result_artifact.json
  status = OK
  test_count = 5024
  duration_seconds = 196.2862
  artifact sha256 = b0d9032319072e7767c3f929a8da3cd31f5599017a7d0b55f53a64b35d0e3b32
  log sha256 = f9dedcbbaf1fb2fde184e15084bdb3e05aae48b073b009ddeef76814b1757273
```

문서 작성 후 핵심 숫자 재검산:

```text
doc key assertions OK

검증한 항목:
  brain_web_readiness_gate_audit.verdict = BLOCKED
  brain_accepted_claim_count = 0
  web_or_llm_accepted_claim_count = 0
  web_fetched_document_count = 2
  llm_claim_extractor_attempt_count = 2
  brain_web_attempt_audit.accepted_claim_count = 0
  brain_web_attempt_audit.source_task_execution_count = 12
  brain_stage_promotion_audit.brain_stage_trace_count = 0
  census_stage_status rows = 3391
  accepted_claims / score_contributions / stagecourt_traces rows = 92 / 92 / 92
  brain_to_claim_trace rows = 0
  raw_assertion_rejections rows = 23
  web_rejected_documents rows = 21
  planner_runs rows = 22
```

## 2. Stage가 있긴 한가?

있다. 다만 전부 `CENSUS_EVENT_BOARD` 범위다.

`output/census_v4/2026-07-01/census_stage_status.jsonl` 기준:

```text
row_count = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3391
  FULL_THESIS = 0

score_scope:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

base_stage_display:
  EVENT_BOARD_STAGE0 = 3306
  EVENT_BOARD_STAGE1 = 54
  EVENT_BOARD_STAGE2_WATCH = 30
  EVENT_BOARD_RED = 1

canonical_stage:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

verified_score_present = 0
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
event_board_non_stage0_count = 85
```

해석:

```text
85개 종목은 상태판에서 Stage0보다 위 또는 Red로 표시된다.
하지만 이 85개는 full thesis 운영 Stage가 아니다.
```

쉬운 예:

```text
DART 공시가 있어서 "한 번 봐야 함" 상태가 됐다.
  -> Event-board Stage1 또는 Stage2-Watch 가능.

그 공시와 추가 자료를 읽고, 원문 claim을 채택하고, 점수 contribution과 StageCourt까지 닫았다.
  -> 운영 FULL_THESIS Stage.

현재는 첫 번째만 있고 두 번째는 0개다.
```

## 3. Brain/Web v8은 어디까지 갔나?

`brain_web_readiness_gate_audit.json` 기준:

```text
verdict = BLOCKED
run_mode = BRAIN_AND_WEB_ACQUISITION_ENABLED
brain_web_mode = enabled

llm_planner_call_count = 22
llm_real_provider_success_count = 2
source_task_execution_count = 12
web_search_task_count = 4
web_search_call_count = 4
web_search_result_count = 31
web_fetched_document_count = 2
web_rejected_document_count = 21
llm_claim_extractor_attempt_count = 2
llm_claim_extractor_real_provider_count = 2

brain_accepted_claim_count = 0
official_accepted_claim_count = 0
web_or_llm_accepted_claim_count = 0
brain_score_contribution_count = 0
brain_to_claim_trace_count = 0
brain_stage_trace_count = 0
brain_promoted_stage_row_count = 0
```

blockers:

```text
Brain/Web accepted claim count is zero
web/LLM accepted claim count is zero
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
Brain/Web operational minimum planner runs not met: 22/30
Brain/Web operational minimum web search tasks not met: 4/20
Brain/Web operational minimum web/news search calls not met: 4/20
Brain/Web operational minimum fetched documents not met: 2/10
Brain/Web operational minimum claim extractor attempts not met: 2/10
Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

해석:

```text
LLM이 아예 안 돈 것은 아니다.
웹 원문 fetch와 claim extraction도 일부 돈 것은 맞다.

하지만 점수에 들어간 Brain/Web accepted claim은 0개다.
따라서 운영 Stage로 승격되면 안 된다.
```

## 4. 헷갈리기 쉬운 accepted_claims 92건

`accepted_claims.jsonl`, `score_contributions.jsonl`, `stagecourt_traces.jsonl`에는 각각 92행이 있다.

하지만 이것은 최신 Brain/Web attempt의 성공이 아니다.

대조 결과:

```text
accepted_claims.jsonl:
  row_count = 92
  source_provider = OpenDART 92
  source_origin = census_v3_leaf 92
  brain_web_claim = false

score_contributions.jsonl:
  row_count = 92
  support_claim_ids 있음

stagecourt_traces.jsonl:
  row_count = 92
  source_cutover_date = 2026-06-24 계열 leaf trace

brain_to_claim_trace.jsonl:
  row_count = 0

brain_web_attempt_audit.json:
  accepted_claim_count = 0
  brain_score_contribution_exported_count = 0
  brain_stagecourt_trace_exported_count = 0
```

즉:

```text
"accepted claim 92개가 있네?"
  -> 맞다. 그러나 v3 leaf / production cutover artifact에서 온 공식 이벤트 claim이다.

"그러면 Brain/Web이 accepted claim을 만들었네?"
  -> 아니다. 이번 research_brain_v4_attempt accepted claim은 0개다.
```

쉬운 예:

```text
창고에 예전 계약서 92장이 있다.
오늘 LLM 조사원이 새로 작성해 통과시킨 계약서는 0장이다.
창고 계약서가 있다고 오늘 조사 경로가 성공한 것은 아니다.
```

## 5. v8에서 실제로 좋아진 부분

v8 직전 병목은 `max_fetches_per_task`가 source task 개수까지 잘라 버리는 것이었다.

패치 후 분리된 값:

```text
ProductionShadowV4Config.max_source_tasks_per_plan = 5
ProductionShadowV4Config.max_fetches_per_task = 3
```

코드 위치:

```text
src/e2r/research_brain/v4_schemas.py
  ProductionShadowV4Config.max_source_tasks_per_plan
  ProductionShadowV4Config.max_fetches_per_task

src/e2r/research_brain/v4_planner_runtime.py
  source_tasks_from_planner_output_v4(max_tasks, max_fetches_per_task)
  _bounded_task_fetches()

src/e2r/research_brain/v4_production_orchestrator.py
  source_tasks_from_planner_output_v4(
    max_tasks=config.max_source_tasks_per_plan,
    max_fetches_per_task=config.max_fetches_per_task,
  )

tests/test_research_brain_v4_operational_modes.py
  test_fetch_cap_does_not_truncate_planner_source_tasks
```

검증:

```text
max_fetches_per_task=1이어도 planner source task 3개는 유지된다.
각 task의 max_fetches만 1로 capped된다.
```

쉬운 예:

```text
잘못된 과거 동작:
  "문서 1개만 가져와"라고 했더니 조사 과제도 1개만 남김.

수정된 동작:
  조사 과제 3개는 유지하고, 각 과제마다 문서 1개만 가져오게 함.
```

v8 숫자상 개선:

```text
sourcequality-v7:
  web_fetched_documents = 9
  claim_extractor_runs = 9
  raw_assertion_rejections = 56
  brain_accepted_claim_count = 0

sourcequality-v8:
  source_task_executions = 104 total
  source_task_executions with execution_origin=research_brain_v4_attempt = 12
  web_fetched_documents = 2
  claim_extractor_runs = 2
  raw_assertion_rejections = 23
  brain_accepted_claim_count = 0
```

해석:

```text
task/fetch budget 혼동은 고쳐졌다.
하지만 accepted claim 병목은 아직 안 풀렸다.
```

## 6. v8에서 여전히 막힌 직접 원인

### 6.1 제한된 planner slot이 약한 후보에 먼저 쓰인다

`planner_runs.jsonl`에서 실제 Codex planner 성공 2회는 모두 같은 후보에 쓰였다.

```text
candidate_event_id = CE-LIVE-DART-003090-20260630801612
symbol = 003090
company_name = 대웅
event_title = [기재정정]신규시설투자등(자회사의 주요경영사항)

real provider success:
  initial = 1
  feedback_retry = 1
```

반면 같은 run의 candidate list에는 다음 같은 후보가 있었지만, real planner limit 때문에 시도되지 않았다.

```text
삼성전자 CompanyGuide report:
  "27년에 더욱 부각될 생산능력"
  "두렵지 않다"
  "재평가 국면의 시작"
  "성과급 반영해도 실적 전망치 상향"

SK하이닉스 CompanyGuide report:
  "실적과 멀티플 둘 다 열려 있다"
  "출격 SKHY US"
  "ADR(American Depositary Receipts) 발행을 위한 유상 증자"

그린생명과학 DART:
  "[기재정정]단일판매ㆍ공급계약체결"
```

현재 후보 정렬 코드:

```text
src/e2r/research_brain/v4_production_orchestrator.py
  _planner_candidate_order()
```

현재 sort key가 보는 것:

```text
production eligibility
fixture_like_symbol penalty
cached/snapshot source penalty
candidate_event_id
```

현재 sort key가 아직 보지 않는 것:

```text
이 이벤트가 accepted claim을 만들 가능성이 큰가
직접 공급계약/실적/리포트처럼 source-backed primitive로 닫히기 쉬운가
정정 공시/일정 연장처럼 후속 조사 없이는 primitive가 애매한가
첫 후보가 accepted 0이면 다음 후보를 계속 시도해야 하는가
```

쉬운 예:

```text
한 번만 면접 볼 수 있는데,
"공장 사용승인 종료일 연장 정정" 후보를 먼저 면접했다.
그 후보가 나쁘다는 뜻은 아니다.
다만 "당장 점수 claim이 닫힐 가능성"은 직접 공급계약이나 현재 실적 리포트보다 낮을 수 있다.
```

### 6.2 대웅 정정 공시는 guard가 막은 것이 맞다

`raw_assertion_rejections.jsonl` 기준:

```text
raw_assertion_rejections = 23

rejection_reason:
  primitive_mapping_rejected = 20
  target_scope_or_directness_rejected = 3
```

대표 예:

```text
source_url = https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801612
symbol = 003090
company_name = 대웅
event_title = 신규시설투자 정정
정정사유 = 종료일 연장
문장 내용 = GMP 승인예정일 기준으로 투자기간 종료일 판단
```

LLM/mapper는 다음 후보 primitive를 시도했다.

```text
volume_growth_visible
operating_leverage_visible
cash_or_revision_conversion
official_disclosure_status_current
```

하지만 accepted claim은 0이다.

이건 점수기가 너무 보수적인 것이 아니라, 현재 공시 조각만으로 다음을 확정하기 어렵기 때문이다.

```text
생산능력이 실제 증가했는가
가동이 매출로 전환됐는가
영업레버리지나 현금흐름으로 이어졌는가
자회사 시설투자가 대웅 연결 실적에 직접 얼마나 들어오는가
```

쉬운 예:

```text
"공장 완공 일정이 2027년으로 연장됐다"
  -> 현재 일정/투자 진행 claim은 될 수 있다.

"매출이 늘고 영업레버리지가 생겼다"
  -> 별도 수요, 가동, 매출, 마진 증거가 있어야 한다.

여기서 억지로 volume_growth_visible을 ACCEPT하면 또 잘못된 점수 흔들림이 생긴다.
```

### 6.3 웹 검색 결과 품질도 아직 낮다

`web_rejected_documents.jsonl` 기준:

```text
web_rejected_documents = 21

rejection_reason:
  web_result_stock_list_or_channel_page_not_source_document = 17
  post_extraction_no_score_eligible_claim = 2
  web_result_site_archive_or_sitemap_not_source_document = 1
  duplicate_web_result_url_not_refetched = 1
```

`web_fetched_documents.jsonl` 기준 실제 full-source fetch는 2개:

```text
1. Plum SEC 대웅 자회사 나보타 3공장 건설 투자기간 연장
2. KIND 분기보고서 viewer
```

해석:

```text
웹을 더 많이 긁으면 해결되는 문제가 아니다.
검색 결과가 주식 요약/채널/아카이브로 많이 새고,
fetch된 문서도 현재 primitive를 닫지 못했다.
```

## 7. 삼성전자/하이닉스는 어떻게 봐야 하나?

`samsung_hynix_full_thesis_smoke.json` 기준:

```text
verdict = PENDING_FULL_THESIS_REFRESH
target_full_thesis_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
score_allowed_before_execution = false
daily_event_and_full_thesis_separated = true

SK하이닉스:
  daily_event_claim_ids = 1개 있음
  full_thesis_claim_ids = []
  full_thesis_score_contribution_ids = []
  full_thesis_stagecourt_trace_ids = []
  blocking_reason = full_thesis_source_tasks_planned_but_not_executed

삼성전자:
  daily_event_claim_ids = 1개 있음
  full_thesis_claim_ids = []
  full_thesis_score_contribution_ids = []
  full_thesis_stagecourt_trace_ids = []
  blocking_reason = full_thesis_source_tasks_planned_but_not_executed
```

따라서:

```text
삼성전자/하이닉스에 daily event Stage row는 있을 수 있다.
하지만 C06 full thesis 운영 점수/Stage는 아직 없다.
```

쉬운 예:

```text
삼성전자 리포트가 발견됐다.
  -> "리포트 이벤트 있음" 상태판 row.

HBM 고객 배정, qualification, capacity allocation, revenue mix, FCF/revision bridge를
source-backed claim으로 닫았다.
  -> C06 full thesis Stage.

현재는 full thesis source task가 계획만 됐고 실행/채택이 안 됐다.
```

## 8. All-archetype 상태

`goal_completion_audit.json` 기준:

```text
required_archetype_count = 32
archetype_count including R13 guard rows = 36
source_backed_ready_count = 6
guard_replay_ready_count = 6
missing_required_archetype_count = 26

status_counts:
  SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY = 6
  SOURCE_GAP_PENDING = 26
  GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY = 4
```

해석:

```text
전 아키타입 운영 준비가 끝난 것이 아니다.
C06/C08/C15/C17/C24/C28 계열 replay가 일부 준비됐고,
나머지 required archetype은 source-backed replay gap이 남아 있다.
```

쉬운 예:

```text
36칸 표에서 6칸은 실제 원문 replay가 됐다.
나머지 26칸은 아직 "이 아키타입도 운영 원문으로 같은 결과가 나오는지"가 증명되지 않았다.
```

## 9. 현재 상태에 대한 판정

### 9.1 잘못되고 있는가?

운영 Stage가 나온다고 기대했다면, 맞다. 아직 잘못되고 있다.

정확한 문제:

```text
full thesis EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt 경로가 live에서 닫히지 않는다.
제한된 planner slot이 claim-rich 후보보다 약한 정정/일정 후보에 먼저 쓰인다.
web/source acquisition은 일부 돌지만 score-eligible accepted claim을 만들지 못한다.
삼성전자/하이닉스 C06 full thesis task는 계획만 있고 실행/채택이 없다.
전 아키타입 source-backed replay parity도 아직 6/32 수준이다.
```

### 9.2 그래도 좋아진 점은 있는가?

있다. fake/overclaim 방어는 동작한다.

```text
accepted claim이 0이면 Stage 승격도 0이다.
snippet만으로 점수를 주지 않는다.
source_proxy_only를 운영 점수로 쓰지 않는다.
대웅 시설투자 정정 공시를 억지로 volume growth로 받아들이지 않는다.
```

즉 현재 문제는:

```text
거짓 Stage를 만들고 있는 문제
```

보다는:

```text
진짜 Stage를 만들 수 있는 live evidence path가 아직 충분히 작동하지 않는 문제
```

에 가깝다.

## 10. v9 패치 방향

v9에서 하면 안 되는 것:

```text
대웅 시설투자 정정 claim을 억지로 volume_growth_visible로 ACCEPT하기
Green/Yellow gate를 낮추기
mapping rejected를 score로 흘리기
삼성전자/하이닉스를 종목명으로 우선순위 하드코딩하기
C06이면 정해진 검색어를 코드가 deterministic하게 만들기
```

v9에서 해야 하는 것:

```text
제한된 planner/source 슬롯을 accepted claim이 나올 가능성이 큰 후보에 먼저 쓰게 한다.
첫 후보가 real planner success였더라도 accepted claim 0이면, bounded budget 안에서 다음 후보로 넘어간다.
후보 선택/계속 시도/실패 사유를 artifact로 남긴다.
```

### P0-A. Candidate Evidence-Likelihood Ranking

현재 `_planner_candidate_order()`는 production eligibility, fixture/cache penalty, id만 본다.

다음 generic rank feature가 필요하다.

```text
source family:
  live official / issuer / report / trusted news 우선
  fixture/cache/snapshot 후순위

event document shape:
  직접 계약, 실적, 리포트, guidance/revision, current material disclosure처럼
  원문 claim으로 primitive가 닫힐 가능성이 높은 이벤트 우선

correction/admin shape:
  단순 정정, 일정 연장, 관리/상장 상태, channel/list page 성격은 후순위

structured payload richness:
  금액, 기간, 상대방, 품목, 실적기간, target directness 같은 구조화 필드가 있으면 우선

not score evidence:
  이 rank는 조사 순서만 바꾸며 점수나 Stage를 만들면 안 된다.
```

주의:

```text
종목명 조건 금지.
아키타입별 검색어 하드코딩 금지.
missing slot별 deterministic query synthesis 금지.
```

쉬운 예:

```text
나쁜 패치:
  if symbol in ("005930", "000660"): 먼저 조사

좋은 패치:
  "현재 리포트/공시가 있고, 원문 claim primitive로 닫힐 가능성이 높은 이벤트"를 먼저 조사
  그래서 어떤 종목이든 직접 공급계약/실적 revision/report가 단순 일정 정정보다 앞선다.
```

테스트:

```text
test_planner_candidate_order_prioritizes_claim_likely_live_events_without_dropping_corrections

입력:
  A = facility investment correction / end-date extension
  B = direct supply contract disclosure
  C = current research report with revision/capacity language

기대:
  B 또는 C가 A보다 먼저 온다.
  A는 삭제되지 않고 뒤에 남는다.
  symbol-specific branch는 없다.
```

### P0-B. Accepted-Claim-Aware Attempt Continuation

현재 v8은 planner real success 2회가 모두 대웅 동일 후보에 쓰였다.

필요한 정책:

```text
real planner success != evidence success

real planner가 성공했어도:
  source task accepted claim = 0
  score contribution = 0
이면, bounded attempt budget 안에서 다음 후보를 계속 시도한다.
```

새 설정 예:

```text
planner_success_limit:
  LLM planner call 성공 상한

accepted_claim_target:
  Brain/Web attempt가 최소 몇 개 accepted claim을 만들 때까지 계속 볼지

max_distinct_candidate_attempts:
  accepted 0 상태에서 몇 종목/이벤트까지 넓힐지
```

쉬운 예:

```text
첫 번째 면접자가 답안지를 못 냈다.
LLM 호출은 성공했지만 accepted claim은 0이다.
그러면 "면접 성공 1회"로 끝내지 말고,
정해진 최대 인원 안에서 두 번째, 세 번째 후보를 본다.
```

테스트:

```text
test_zero_accepted_claim_first_candidate_continues_to_next_candidate

입력:
  first candidate: planner success, source tasks run, accepted claim 0
  second candidate: planner success, accepted claim 1

기대:
  result planner_runs includes both
  brain_web_attempt_audit accepted_claim_count = 1
```

### P0-C. Source Route Effectiveness Ledger

현재 `web_rejected_documents`는 문서 단위 reject를 남긴다.
다음에는 task 단위로도 "왜 실패했는지"를 요약해야 한다.

필요한 artifact:

```text
source_task_effectiveness.jsonl

fields:
  candidate_event_id
  task_id
  primitive_gap
  preferred_source_classes
  attempted_source_classes
  fetched_document_count
  rejected_document_count
  raw_assertion_count
  accepted_claim_count
  dominant_rejection_reason
  next_action
```

쉬운 예:

```text
task: volume_growth_visible
fetched: 2
accepted: 0
dominant_rejection: primitive_mapping_rejected
next_action: do not widen same query; try next candidate or official operating data
```

### P0-D. Full Thesis Runner Execution Path

삼성전자/하이닉스는 현재 full thesis source task가 계획만 있고 실행되지 않았다.

필요한 것:

```text
full_thesis_source_tasks planned -> executed -> claim extraction -> accepted_claim_ids
```

다만 이것도 종목명 특례가 되면 안 된다.

좋은 구조:

```text
Stage row나 daily event가 있는 종목 중
full thesis archetype hypothesis가 있고
missing full thesis primitives가 material한 종목을
bounded full thesis refresh 대상으로 올린다.
```

쉬운 예:

```text
SK하이닉스라서 실행하는 게 아니다.
"C06 full thesis task가 계획됐는데 실행 안 됨" 상태라서 실행한다.
```

### P1. All-Archetype Source-Backed Replay Expansion

현재 6/32다.

P0 live path가 안정된 뒤:

```text
source-backed replay fixture를 C01~C32 전체로 확장
source_proxy_only row는 ontology 참고만 하고 운영 정답으로 쓰지 않음
각 아키타입 positive + guard + wrong-subject + historical/superseded case 최소 1개
```

## 11. v9 완료 기준

v9를 완료라고 부르려면 최소 아래가 필요하다.

```text
1. candidate ordering test 통과
2. first candidate accepted 0이면 다음 candidate로 진행하는 test 통과
3. v9 live diagnostic에서 distinct real planner candidate가 2개 이상 남음
4. research_brain_v4_attempt source_task_execution_origin row가 명확히 분리됨
5. Brain/Web accepted claim이 0이면 그대로 NOT_READY 유지
6. accepted claim이 생기면 support_claim_ids 있는 score contribution으로만 StageCourt 진입
7. v3 leaf accepted_claims 92건을 Brain/Web accepted로 세지 않음
8. 삼성전자/하이닉스 daily event row를 C06 full thesis row로 표시하지 않음
9. full unittest artifact 갱신
10. docs/0701 README와 최신 v9 문서에 숫자 반영
```

v9에서도 accepted claim이 0일 수 있다.
그 자체는 실패가 아니다.
실패는 다음이다.

```text
accepted 0인데 Stage 승격
accepted 0인데 완료 선언
accepted 0인데 어떤 후보/소스/primitive가 막혔는지 artifact가 없음
```

## 12. 다음 에이전트 공격 포인트

다음 에이전트는 아래를 먼저 공격해야 한다.

```text
1. accepted_claims.jsonl 92건을 최신 Brain/Web claim으로 오해한 부분이 없는가?
2. source_task_origin과 source_task_execution_origin을 섞어 accepted attempt count를 부풀린 부분이 없는가?
3. stagecourt_traces 92건을 Brain/Web StageCourt trace로 오해한 부분이 없는가?
4. Candidate ranking이 종목명/아키타입/검색어 하드코딩으로 새 오염을 만들지 않는가?
5. 대웅 시설투자 정정 claim을 억지로 ACCEPT하는 완화 패치가 들어가지 않았는가?
6. planner success를 evidence success로 착각하고 있지 않은가?
7. 삼성전자/하이닉스 C06 full thesis task가 실제 실행됐는가, 아니면 계획만 남았는가?
8. all-archetype replay 6/32를 전 아키타입 완료처럼 말하지 않는가?
9. test_count만 보고 운영 준비 완료라고 말하지 않는가?
10. event-board Stage를 운영 FULL_THESIS Stage로 다시 섞지 않는가?
```

## 13. 최종 판단

현재 상태:

```text
NOT_READY가 맞다.
운영 Stage가 있는 종목은 아직 없다.
상태판 Stage가 있는 종목은 있다.
Brain/Web live path는 일부 실행됐지만 accepted claim 0에서 막혔다.
```

다음 패치의 핵심:

```text
점수 기준을 낮추지 않는다.
rejected claim을 억지로 accepted로 바꾸지 않는다.
LLM query를 deterministic template로 대체하지 않는다.

대신:
  제한된 planner/source budget을 claim-rich 후보에 먼저 쓴다.
  첫 후보가 accepted 0이면 다음 후보로 계속 진행한다.
  task별 실패 이유를 더 선명하게 남긴다.
  full thesis planned task를 실제 실행 경로로 연결한다.
```

한 문장으로:

```text
v8의 문제는 "Stage를 너무 엄격하게 막는다"가 아니라
"운영 Stage를 만들 수 있는 후보와 증거까지 아직 충분히 도달하지 못한다"이다.
```

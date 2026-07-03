# Census v4 0701 Feedback-v1 Hard Cross Review / Next Patch Packet

작성 시점: 2026-07-02 KST  
repo: `/home/eorb915/projects/stock_agent`  
canonical output: `output/census_v4/2026-07-01`  
diagnostic captured in this document: `output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1`  
as_of_date: `2026-07-01`

이 문서는 `feedback-v1` 당시의 원인 분석 문서다.
최신 교차검증과 다음 패치 우선순위는 아래 문서를 우선한다.

2026-07-02 추가 패치 이후 우선 문서:

```text
docs/0701/census_v4_0701_next_agent_hard_review_after_metricsplit_2026-07-02.md
docs/0701/census_v4_0701_brain_web_metric_split_patch_result_2026-07-02.md
docs/0701/census_v4_0701_postextract_web_rejection_patch_result_2026-07-02.md
```

이 문서는 `feedback-v1` 당시의 원인 분석으로 유지한다.
최신 Brain/Web 산출물 수치는 `metricsplit-v1`을 우선한다.

## 한 줄 결론

```text
Stage label은 있다.
Brain/Web partial row도 1개 있다.
하지만 운영 FULL_THESIS Stage와 FULL_E2R_100 verified score는 아직 0개다.
```

쉽게 말하면:

```text
현재 시스템에는 "전 종목 상태판"은 있다.
하지만 "전 종목을 E2R 100점 채점표로 실제 운영 판정한 결과"는 아직 없다.
```

예:

```text
Stage0:
  "이번 census에서 현재 catalyst가 확인되지 않음"이라는 상태판이다.
  나쁜 종목 0점이라는 뜻이 아니다.

Stage2-Watch:
  공식 이벤트나 단일 claim 때문에 감시할 row라는 뜻일 수 있다.
  C06/C08/C15 같은 full thesis Stage2와 섞으면 안 된다.

BRAIN_WEB_PARTIAL:
  Research Brain/Web이 일부 claim을 만들고 partial row를 올렸다는 뜻이다.
  운영자가 써도 되는 Green/Yellow/Red full thesis Stage가 아니다.
```

## 이 문서가 supersede하는 것

기존 최신 문서 일부는 `schema-v2` 진단을 최신 Brain/Web 보조 진단으로 적고 있었다.
그 뒤에 `feedback-v1` 진단을 추가 실행했으므로 이 문서 당시 기준은 아래다.

```text
old latest diagnostic:
  output/census_v4/2026-07-01-brain-web-diagnostic-schema-v2

new latest diagnostic:
  output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1
```

`schema-v2`는 버리는 산출물이 아니다.
그 진단은 Codex claim extractor schema patch가 실제 provider error를 없앴다는 직전 증거다.
다만 이 문서 내부의 상태 판단 숫자는 `feedback-v1` 당시 기준이다.
현재 최신 숫자는 `metricsplit-v1` 문서를 우선한다.

## 직접 교차검증한 파일

Canonical:

```text
output/census_v4/2026-07-01/readiness_verdict.json
output/census_v4/2026-07-01/census_stage_status.jsonl
output/census_v4/2026-07-01/accepted_claims.jsonl
output/census_v4/2026-07-01/raw_assertions.jsonl
output/census_v4/2026-07-01/source_task_executions.jsonl
output/census_v4/2026-07-01/score_contributions.jsonl
output/census_v4/2026-07-01/stagecourt_traces.jsonl
```

Latest Brain/Web diagnostic:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/readiness_verdict.json
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/brain_web_attempt_audit.json
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/census_stage_status.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/planner_runs.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/source_tasks.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/source_task_executions.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/web_search_tasks.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/web_fetched_documents.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/web_rejected_documents.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/claim_extractor_runs.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/raw_assertions.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1/accepted_claims.jsonl
```

관련 코드/테스트:

```text
src/e2r/production/claim_extraction/extractor_provider.py
src/e2r/research_brain/v4_evidence_extraction_bridge.py
src/e2r/research_brain/v4_production_orchestrator.py
tests/test_cutover_contract_blind_extraction.py
tests/test_research_brain_v4_operational_modes.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
```

## Canonical output 현재 진실

`output/census_v4/2026-07-01/census_stage_status.jsonl` 직접 집계:

```text
rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3391

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

score_scope:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67
  FULL_E2R_100 = 0

base_stage:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

canonical_stage:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

full_thesis_stage:
  FULL_THESIS_NOT_RUN = 3391

candidate_event_scope:
  ASSESSMENT_ONLY = 3306
  CANDIDATE_EVENTS_PRESENT = 85

score_valid_status:
  NO_CURRENT_EVENT = 3306
  FINAL_WITH_NONMATERIAL_GAPS = 37
  PENDING_MATERIAL_GAPS = 30
  NOT_SCORED = 11
  INVALID_EVIDENCE = 7

stage_decision_status:
  NO_CURRENT_CATALYST = 3306
  FINAL = 36
  PENDING_MATERIAL_GAPS = 30
  SOURCE_PENDING = 18
  RISK_REVIEW = 1
```

Canonical claim/source 상태:

```text
accepted_claims.jsonl = 92 rows
accepted source_provider:
  OpenDART = 92
accepted raw id prefix:
  RAWPROD = 92

web_search_tasks.jsonl = 0
web_fetched_documents.jsonl = 0
web_rejected_documents.jsonl = 0
claim_extractor_runs.jsonl = 0

brain_web_readiness_gate.verdict = NOT_REQUESTED
brain_web_attempt.verdict = NOT_REQUESTED
```

해석:

```text
Canonical output은 Brain/Web disabled 상태다.
그래서 official/event-board 상태판으로만 읽어야 한다.
```

## Latest Brain/Web diagnostic 현재 진실

`output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1` 직접 집계:

```text
verdict = NOT_READY
brain_web_evidence_pass = false

stage rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3390
  BRAIN_WEB_PARTIAL = 1
  FULL_THESIS = 0

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

score_scope:
  NO_SCORE = 3323
  EVENT_WEIGHTED_PARTIAL = 67
  BRAIN_WEB_CLAIM_BACKED_PARTIAL = 1
  FULL_E2R_100 = 0

base_stage:
  Stage0 = 3306
  Stage1 = 53
  Stage2-Watch = 30
  0 = 1
  Red = 1

canonical_stage:
  0 = 3307
  1 = 53
  2 = 30
  3-Red = 1
```

Brain/Web gate:

```text
brain_web_readiness_gate.verdict = BLOCKED
brain_web_evidence_pass_allowed = false

llm_planner_call_count = 21 / required 30
web_search_task_count = 3 / required 20
web_search_call_count = 3 / required 20
web_fetched_document_count = 4 / required 10
llm_claim_extractor_attempt_count = 4 / required 10
web_or_llm_accepted_claim_count = 2 / required 3

attempt_real_document_fetched_count = 10
real_document_fetched_count = 7
```

주의:

```text
attempt_real_document_fetched_count와 real_document_fetched_count가 서로 다르다.
이 둘은 같은 의미로 섞어 쓰면 안 된다.
다음 패치에서 metric definition을 더 명확히 해야 한다.
```

Planner:

```text
planner_runs.jsonl = 21 rows
planner_run_role:
  initial = 21

provider_name:
  codex_cli_planner = 1
  not_attempted_after_real_planner_limit = 20

real_provider_success:
  True = 1
  False = 20

rejected_claim_feedback_count:
  0 = 21

planner_feedback nonempty rows = 0
```

해석:

```text
실제 Codex planner 성공은 1개다.
나머지 20개는 planner_success_limit 때문에 실행하지 않은 row다.
따라서 이 diagnostic은 "전 종목 Brain 실행"이 아니라 "bounded smoke/diagnostic"이다.
```

Claim extractor:

```text
claim_extractor_runs.jsonl = 4 rows
status:
  SUCCESS = 4
provider_error_count = 0
raw_assertion_count total = 17
```

Raw assertions:

```text
raw_assertions.jsonl = 108 rows

source_provider:
  OpenDART = 96
  https://openapi.naver.com/v1/search/webkr.json = 7
  https://openapi.naver.com/v1/search/news.json = 5

LLM/web/news raw rows exist.
하지만 accepted score claim으로 들어간 web/news claim은 없다.
```

Accepted claims:

```text
accepted_claims.jsonl = 94 rows

accepted source_provider:
  OpenDART = 94

accepted raw id prefix:
  RAWPROD = 92
  RAWASSERTV4 = 2

accepted web/news source_provider = 0
accepted RAWLLM source claim = 0
```

Source/Web:

```text
source_task_executions.jsonl = 98
execution status:
  EVIDENCE_OS_ACCEPTED = 62
  EVIDENCE_OS_BASELINE_ONLY = 32
  NO_EVIDENCE_FOUND = 3
  PROVIDER_FAILED = 1

web_search_tasks.jsonl = 3
web_fetched_documents.jsonl = 4
web_rejected_documents.jsonl = 0
```

## 003090 대웅 Brain/Web partial row 해석

`BRAIN_WEB_PARTIAL` 1개 row는 `003090` 대웅이다.

실제로 accepted된 Brain/Web 관련 claim:

```text
1. CLM-cc9766571975aff35a57
   primitive_id = implementation_timeline
   satisfaction_type = DIRECT_ACCEPTED_CLAIM
   satisfies_source_task = true
   source_provider = OpenDART
   source_url = https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801612

2. CLM-185ffe727e1f77f465cf
   primitive_id = implementation_timeline
   satisfaction_type = REROUTED_ACCEPTED_CLAIM
   satisfies_source_task = false
   source_provider = OpenDART
   source_url = https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260630801612
```

중요:

```text
둘 다 OpenDART 원문 claim이다.
웹/뉴스 claim이 accepted된 것이 아니다.
둘 다 full_thesis_claim=false다.
```

쉬운 예:

```text
대웅 공시에서 "투자기간 종료일이 2027-05-31로 연장됐다"는 사실은 잡았다.
하지만 이걸로 "정책 보조금, 직접 현금 유입, 매출/마진 전환까지 확인된 C31 full thesis"라고 말할 수는 없다.
```

웹 문서 상태:

```text
web_fetched_documents = 4
예:
  https://plumsec.com/ko/report/detail?rcept_no=20260630801612
  https://www.kdpress.co.kr/news/articleView.html?idxno=205605
  https://www.kdpress.co.kr/news/articleView.html?idxno=205554

snippet_score_forbidden = true
accepted web/news claim = 0
web_rejected_documents = 0
```

여기서 `web_rejected_documents=0`은 이상한 지점이다.
웹 문서가 fetch되었고 LLM raw assertion도 나왔고 rejected claim도 있는데,
post-extraction rejection이 `web_rejected_documents`에 남지 않았다.

## 지금 고친 것

### 1. Codex extractor schema failure는 해결됨

이전 `schema` diagnostic에서는 Codex extractor가 provider error로 실패했다.

원인:

```text
Codex structured output schema에서 required가 properties 전체를 포함하지 않았고,
uncertainty_reason이 빠져 있었다.
```

현재 코드 상태:

```text
src/e2r/production/claim_extraction/extractor_provider.py
  EXTRACTOR_OUTPUT_SCHEMA가 모든 properties를 required에 포함
  event_date / uncertainty_reason은 string
  allowed predicate enum 고정
  unknown predicate는 mention_only로 downgrade
  prompt에 score/stage/primitive/current_score_eligible 금지
```

검증:

```text
claim_extractor_runs = 4
SUCCESS = 4
provider_error_count = 0
raw_assertion_count total = 17
```

### 2. Contract-blind extractor 안전장치는 살아 있음

테스트로 확인한 것:

```text
primitive_gap, score_gap_context, current_score_eligible, hard_break, verified, green_gate는 extractor extra_context에 들어가면 실패한다.
정상 감사의견은 NORMAL이다.
시설투자 종료일 연장 정정은 positive capacity score로 매핑되지 않는다.
unknown predicate는 mention_only로 내려간다.
```

쉬운 예:

```text
문서에 "감사의견 적정"이라고 있으면 회계 hard break가 아니라 정상 문맥이다.
문서에 "신규시설투자 종료일 연장"이라고 있으면 곧바로 생산능력 확대 만점이 아니다.
```

### 3. Rerouted accepted claim이 feedback retry를 막지 않는 테스트는 있음

현재 코드:

```text
_bundle_has_direct_source_task_acceptance(bundle)
  execution.satisfies_source_task and execution.direct_accepted_claim_ids 가 있을 때만 true
```

테스트:

```text
test_rerouted_acceptance_does_not_block_rejected_claim_feedback_retry
test_direct_source_task_acceptance_blocks_rejected_claim_feedback_retry
```

의미:

```text
다른 primitive로 reroute된 accepted claim은 원래 gap을 닫은 것이 아니므로 feedback retry를 막으면 안 된다.
이 조건은 테스트상 통과한다.
```

## 아직 못 고친 것

### P0. 운영 FULL_THESIS가 0개다

```text
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
operator_stage_use = NOT_FULL_THESIS_STAGE 3391
```

따라서 현재 어떤 row도 운영 Green/Yellow/Red thesis로 쓰면 안 된다.

### P0. Brain/Web evidence pass가 막혀 있다

```text
planner 21/30
web task 3/20
web call 3/20
web fetched 4/10
extractor attempt 4/10
accepted claim 2/3
```

이건 단순 숫자 미달이 아니다.
내용상으로도 accepted claim이 OpenDART에만 있고, 웹/뉴스 LLM claim은 accepted되지 않았다.

### P0. 웹 fetch 후 rejection이 문서 단위로 드러나지 않는다

현재:

```text
web_fetched_documents = 4
web/news raw assertions = 12
rejected claim ids exist
web_rejected_documents = 0
```

문제:

```text
다음 에이전트/운영자가 "웹 문서가 왜 점수로 안 들어갔는지" 문서 단위로 추적하기 어렵다.
```

필요한 패치:

```text
post-extraction web rejection row를 남긴다.

예:
  rejection_phase = post_extraction_evidence_os
  rejection_reason = no_score_eligible_claim
  source_task_id
  document_id
  url
  title
  raw_assertion_ids
  rejected_claim_ids
  not_eligible_reasons
  snippet_score_forbidden = true
```

쉬운 예:

```text
웹 기사 4개를 읽었는데 점수로 못 썼다면,
"읽었지만 주체가 다름", "quote가 원문에 없음", "primitive가 안 맞음" 같은 영수증이 남아야 한다.
지금은 그 영수증이 source_task_execution 안에는 일부 있지만 web_rejected_documents에는 없다.
```

### P0. feedback retry가 bundle-level direct accepted 하나로 너무 쉽게 막힐 수 있다

`feedback-v1`에서:

```text
planner_run_role = initial 21
feedback_retry = 0
rejected_claim_feedback_count = 0
```

왜 그랬나:

```text
003090 bundle 안에 DIRECT_ACCEPTED_CLAIM 하나가 있다.
현재 _bundle_has_direct_source_task_acceptance(bundle)가 true이면 rejected mapping feedback retry를 전체 bundle에서 막는다.
```

이 조건은 테스트상 "direct accepted가 있으면 retry를 막는다"는 좁은 의미로 통과한다.
하지만 운영 관점에서는 더 정교해야 한다.

쉬운 예:

```text
대웅 공시에서 "투자기간 연장"은 확인했다.
하지만 "보조금", "직접 현금 유입", "매출/마진 전환"은 아직 확인되지 않았다.

투자기간 하나를 찾았다고 나머지 rejected web claims를 planner에게 되먹이지 않으면,
Brain이 다음에 무엇을 찾아야 하는지 학습하지 못한다.
```

필요한 패치:

```text
bundle-level any direct accepted로 retry 전체를 막지 않는다.
source task / primitive gap 단위로 판단한다.

block retry only when:
  해당 material primitive gap이 direct accepted로 닫힘
  또는 모든 material gaps가 resolved/nonmaterial로 판정됨

otherwise:
  rejected claim feedback을 planner에게 다시 제공한다.
```

### P1. planner limit 때문에 "실제 planner 1개 성공" 진단이다

현재 diagnostic config는 `planner_success_limit=1`이라서 실제 Codex planner 성공은 1개다.

```text
planner_provider_success = 1
planner_not_attempted_after_real_planner_limit = 20
```

이건 smoke diagnostic으로는 맞다.
하지만 운영 readiness를 주장하려면 더 넓은 성공 범위가 필요하다.

주의:

```text
이 숫자를 보고 "전 종목 LLM Brain이 돌았다"고 말하면 안 된다.
```

### P1. metric 이름이 헷갈린다

`feedback-v1`에서:

```text
attempt_real_document_fetched_count = 10
real_document_fetched_count = 7
web_fetched_document_count = 4
```

세 숫자는 서로 다른 집계일 가능성이 있다.
문서/리포트에서는 각각의 정의를 분리해야 한다.

필요한 패치:

```text
real_document_fetched_count_unique
real_document_fetch_event_count
web_fetched_document_count
official_fetched_document_count
```

처럼 이름을 명확히 나누거나 산식 주석을 audit JSON에 넣는다.

### P1. accepted claim count는 full thesis readiness가 아니다

`feedback-v1`은 accepted claim 2/3 기준에 하나 부족하다.
하지만 3/3을 채워도 그것만으로 FULL_THESIS가 되는 것은 아니다.

이유:

```text
accepted claims는 implementation_timeline 하나에 몰려 있다.
full thesis는 아키타입별 required primitive coverage, source quorum, cash/revision bridge, StageCourt gate가 필요하다.
```

쉬운 예:

```text
영수증 3장을 모았다고 기말고사 100점 채점이 끝나는 게 아니다.
필수 과목 답안이 맞는 칸에 들어가야 한다.
```

## 다음 패치 방향

### Patch 1. post-extraction web rejection ledger

목표:

```text
웹/뉴스 문서를 fetch한 뒤 accepted score claim이 없으면,
그 이유를 web_rejected_documents 또는 별도 post_extraction_rejected_documents에 남긴다.
```

추천 파일:

```text
src/e2r/research_brain/v4_evidence_extraction_bridge.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
```

Acceptance:

```text
web_fetched_document_count > 0이고 web accepted claim이 0이면
post-extraction rejection row가 0이면 안 된다.

각 row는 document_id, url, source_task_id, raw_assertion_ids, rejected_claim_ids, not_eligible_reasons를 가진다.
snippet_score_forbidden=true가 유지된다.
```

### Patch 2. feedback retry를 source-task/primitive 단위로 좁히기

목표:

```text
한 primitive가 direct accepted 됐다는 이유로,
다른 missing primitive의 rejected claim feedback까지 막지 않는다.
```

추천 파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
tests/test_research_brain_v4_operational_modes.py
```

새 테스트:

```text
direct implementation_timeline accepted
AND subsidy/direct_cash_route rejected or missing
THEN feedback_retry is generated for unsatisfied material gaps
```

반대로:

```text
all material gaps direct accepted
THEN feedback_retry is blocked
```

### Patch 3. Brain/Web readiness gate의 accepted claim 품질 강화

현재 `web_or_llm_accepted_claim_count`는 2지만 둘 다 OpenDART다.
이 이름은 오해를 만든다.

필요한 분리:

```text
official_accepted_claim_count
web_news_raw_assertion_count
web_news_accepted_claim_count
llm_extracted_accepted_claim_count
direct_source_task_accepted_claim_count
rerouted_accepted_claim_count
full_thesis_claim_count
```

Acceptance:

```text
BRAIN_WEB_EVIDENCE_PASS를 주장하려면,
web/news/IR/report full-source accepted claim 또는 명시적 official-only completion 사유가 있어야 한다.
```

### Patch 4. FULL_THESIS runner eligibility unblock

현재:

```text
full_thesis_production_audit.blockers:
  production_full_thesis_runner_no_eligible_rows
FULL_THESIS = 0
```

필요:

```text
event-board row와 full thesis refresh task를 분리한다.
full thesis smoke/production runner가 어떤 row를 eligible로 볼지 명확히 한다.
```

단, 주의:

```text
FULL_THESIS를 만들기 위해 EVENT_WEIGHTED_PARTIAL row를 억지 승격하면 안 된다.
```

### Patch 5. All-archetype source-backed replay 확장

현재:

```text
required_archetype_count = 32
source_backed_ready_count = 6
missing_required_archetype_count = 26
```

READY:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
C15_MATERIAL_SPREAD_SUPERCYCLE
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
C24_BIO_TRIAL_DATA_EVENT_RISK
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

남은 26개는 full thesis 운영 확정을 막는 큰 이유다.
source_proxy_only/evidence_url_pending 연구자료를 production score 정답으로 쓰면 안 된다.

## 다음 에이전트에게 주는 공격 질문

1. 왜 `web_fetched_documents=4`인데 `web_rejected_documents=0`인가?
2. 왜 웹/뉴스 raw assertion 12개가 accepted 0개인지 문서 단위 이유가 남는가?
3. `DIRECT_ACCEPTED_CLAIM` 하나가 왜 rejected feedback retry 전체를 막아도 되는가?
4. `web_or_llm_accepted_claim_count=2`라는 이름이 OpenDART accepted만 있는 상태를 과대포장하지 않는가?
5. `BRAIN_WEB_PARTIAL` row가 `operator_stage_use=NOT_FULL_THESIS_STAGE`로 확실히 보호되는가?
6. `attempt_real_document_fetched_count=10`, `real_document_fetched_count=7`, `web_fetched_document_count=4`의 차이를 리포트에서 설명하는가?
7. full thesis runner가 eligible row 0인 이유가 코드/정책적으로 설명되는가?
8. accepted claim 2개가 둘 다 `implementation_timeline`이면 C31 full thesis coverage는 어느 정도인가?
9. LLM extractor가 성공했다는 사실과 LLM claim이 score에 들어갔다는 사실을 문서/리포트가 분리하는가?
10. all-archetype replay 6/32 상태에서 운영 Stage를 주장하는 문구가 남아 있는가?

## 재현/검증 명령

문서 작성 중 다시 확인한 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_cutover_contract_blind_extraction \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_evidence_extraction_from_real_document -v
```

결과:

```text
Ran 38 tests
OK
```

최신 Brain/Web diagnostic 생성 명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01-brain-web-diagnostic-feedback-v1 \
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

결과:

```text
stdout = NOT_READY
runtime_seconds = 247.16
```

## 최종 판단

```text
지금 상태는 "망가진 것"이라기보다 "운영 full thesis라고 부르면 안 되는 상태"다.
```

된 것:

```text
전 종목 Census 상태판
claim 없는 점수 방지 상당 부분
Codex extractor schema 성공
LLM/web raw assertion 생성
Brain/Web partial row 1개
OpenDART source-backed partial claim 2개
```

안 된 것:

```text
FULL_THESIS row
FULL_E2R_100 verified score
web/news accepted score claim
post-extraction web rejection ledger
per-primitive feedback retry
all-archetype source-backed replay parity
production full thesis runner pass
```

따라서 다음 패치의 첫 목표는 점수나 Stage threshold가 아니다.

```text
웹/뉴스 문서를 읽고 버린 이유를 문서 단위로 남기고,
direct accepted 하나 때문에 다른 material gap feedback이 막히지 않게 하고,
Brain/Web gate에서 official accepted와 web/LLM accepted를 분리하는 것.
```

그 다음에야 FULL_THESIS runner와 all-archetype replay parity를 닫을 수 있다.

# Census v4 0701 v36 Source Lineage Retry Execution Guard

작성일: 2026-07-02 KST

## 0. 결론

현재 Stage가 있는 행은 있다.

하지만 운영에서 쓸 FULL_THESIS 점수/Stage는 아직 없다.

```text
CENSUS_EVENT_BOARD 상태판 Stage:
  rows = 3391
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1

operator-admissible FULL_THESIS Stage:
  rows = 0
  FULL_E2R_100 verified score rows = 0
  verified_score_present_count = 0
```

쉬운 예:

```text
CENSUS_EVENT_BOARD Stage = 병원 접수표
FULL_THESIS Stage = 의사가 원문 검사 결과까지 보고 서명한 진단서

지금은 접수표에 Stage1/Stage2-Watch 표시가 일부 있지만,
진단서에 해당하는 FULL_THESIS 점수/Stage는 아직 0개다.
```

v36 패치는 이 truth를 바꾸지 않는다.
대신 잘못된 source retry가 반복되는 구멍을 하나 더 막는다.

```text
v34:
  일반 검색/Naver로 발견한 뉴스/리포트/IR성 문서는
  원문 lineage 검증 없이 score source가 될 수 없게 막음

v35:
  source_lineage_unverified_original rejection reason을
  planner feedback과 prompt payload에 되돌림

v36:
  그 feedback을 받은 뒤에도 retry planner가 discovery-only route만 다시 내면
  실행 단계에서 해당 source task를 드롭함
```

한 줄 요약:

```text
"네이버 검색으로 찾았지만 원문 확인이 안 돼서 reject"된 뒤에는
다시 네이버/일반웹만 반복하지 못하게 막고,
회사 뉴스룸/IR 원문/리포트 PDF/공식 상세 같은 원문 검증 route로만 재시도를 살린다.
```

## 1. 왜 이 패치가 필요한가

v35까지는 실패 이유가 planner에게 보였다.

하지만 LLM planner가 그 feedback을 받고도 다음처럼 응답할 수 있다.

```text
previous_source_lineage_unverified_original 받음
  -> retry source task:
       preferred_source_classes = NaverSearch
       fallback_source_classes = IndustryMedia
       query = "삼성전자 HBM 고객 배정 기사"
```

이건 여전히 같은 문제다.

```text
처음 실패:
  일반 검색 경유라 original source lineage 미검증

재시도:
  또 일반 검색/업계매체 discovery-only route

결과:
  같은 reject loop 반복
```

LLM에게 "다음에는 원문 쪽을 봐라"라고 말하는 것만으로는 부족하다.
실행 직전에도 source class 정책을 검증해야 한다.

## 2. 하드코딩이 아닌 이유

이번 패치는 검색어를 만들지 않는다.

나쁜 방식:

```text
if archetype == C06:
  query = "{company} HBM 고객 배정 IR 원문"
```

이번 방식:

```text
LLM이 query/source task를 만든다.
코드는 source_lineage_unverified_original feedback 이후에
그 task가 또 discovery-only인지 검증한다.
```

즉 deterministic code는 다음만 판단한다.

```text
이 retry task가 원문 검증 가능 source class를 포함했나?
아니면 또 조사용 discovery source만 반복하나?
```

쉬운 예:

```text
허용되는 retry:
  preferred_source_classes = CompanyNewsroom
  fallback_source_classes = ReportPDF
  query = "삼성전자 HBM 고객 배정 IR 원문"

드롭되는 retry:
  preferred_source_classes = NaverSearch
  fallback_source_classes = IndustryMedia
  query = "삼성전자 HBM 고객 배정 기사"
```

여기서 query 문구는 LLM이 만든다.
코드는 "삼성전자/HBM" 같은 단어를 조건으로 보지 않는다.
코드는 source class admissibility만 본다.

## 3. 코드 변경

수정 파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
tests/test_research_brain_v4_operational_modes.py
docs/0701/README.md
docs/0701/census_v4_0701_v36_source_lineage_retry_execution_guard_2026-07-02.md
```

### 3.1 feedback reason tag 분리

추가 의미:

```text
retry_run.planner_feedback에 previous_source_lineage_unverified_original이 있으면
reason_tag = source_lineage_unverified_original
```

이전에는 source rejection retry가 대부분 `source_rejection`으로 뭉쳤다.
v36에서는 source lineage 실패를 별도 reason으로 실행 필터까지 전달한다.

### 3.2 discovery-only retry task 드롭

추가된 실행 정책:

```text
if reason_tag == source_lineage_unverified_original
and retry task source classes are discovery-only:
  drop retry task
```

discovery-only로 보는 source class:

```text
GeneralWeb
GeneralWebSearch
IndustryMedia
NaverSearch
News
Web
```

원문 또는 원문 검증 가능 source class:

```text
BrokerReportPublicPDF
CompanyNewsroom
DART
IR
IssuerOfficial
KIND
KRX
ReportPDF
TrustedNews
```

주의:

```text
TrustedNews 자체가 지금 완성 connector라는 뜻은 아니다.
여기서는 "generic search provider가 아니라 trusted article original을 검증할 수 있는 route"로 분류한다.
실제 connector/lineage verifier가 없으면 이후 source execution에서 다시 reject될 수 있다.
```

### 3.3 dedupe와 retry reason 보존

허용된 retry task는 기존처럼 중복 signature를 제거하고,
reason_from_memory에 다음 표식을 붙인다.

```text
feedback_retry:source_lineage_unverified_original
```

그래서 다음 감사에서 이 source task가 왜 생겼는지 추적할 수 있다.

## 4. 추가 테스트

새 테스트:

```text
test_source_lineage_feedback_retry_drops_discovery_only_source_task
test_source_lineage_feedback_retry_keeps_original_capable_source_task
```

기존 v35 테스트도 같이 유지:

```text
test_source_lineage_unverified_original_feedback_is_visible_to_planner_prompt_payload
test_source_lineage_unverified_original_feedback_retries_planner_once
```

테스트 의미:

```text
1. source_lineage_unverified_original feedback은 planner prompt에 보인다.
2. retry planner run에도 previous_source_lineage_unverified_original tag가 붙는다.
3. 그 tag가 붙은 retry에서 NaverSearch+IndustryMedia only task는 실행 대상에서 빠진다.
4. CompanyNewsroom+ReportPDF task는 실행 대상으로 남는다.
5. 이 feedback payload에는 score/stage/current_score_eligible이 들어가지 않는다.
```

## 5. 검증 결과

타깃 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_source_lineage_feedback_retry_drops_discovery_only_source_task \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_source_lineage_feedback_retry_keeps_original_capable_source_task \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_source_lineage_unverified_original_feedback_retries_planner_once -v
```

결과:

```text
Ran 3 tests
OK
```

운영 모드 전체 테스트:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
```

결과:

```text
Ran 45 tests
OK
```

확장 교차검증:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_run_mode_honesty -v
```

결과:

```text
Ran 124 tests in 41.500s
OK
```

전체 회귀 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5067 tests in 213.319s
OK
```

## 6. 산출물 교차검증

검증 대상:

```text
output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/census_stage_status.jsonl
output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/atomic_stage_decisions.jsonl
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v28/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v28/full_thesis_production_runner_audit.json
output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01-full-thesis-refresh-queue-provider-timeout-v30/full_thesis_refresh_queue_audit.json
```

### 6.1 census_stage_status.jsonl

직접 집계 결과:

```text
rows = 3391
stage_scope = {"CENSUS_EVENT_BOARD": 3391}
operator_stage_use = {"NOT_FULL_THESIS_STAGE": 3391}
full_thesis_stage = {"FULL_THESIS_NOT_RUN": 3391}
base_stage = {"Stage0": 3306, "Stage1": 54, "Stage2-Watch": 30, "Red": 1}
score_present = 0
```

해석:

```text
Stage1/Stage2-Watch/Red는 있다.
하지만 전부 상태판 Stage다.
운영 FULL_THESIS 점수는 0개다.
```

### 6.2 atomic_stage_decisions.jsonl

직접 집계 결과:

```text
rows = 92
stage_scope = {"CENSUS_EVENT_BOARD": 92}
base_stage = {"Stage1": 54, "Stage2-Watch": 37, "Red": 1}
representative = {"True": 74, "False": 18}
score_present = 0
```

해석:

```text
AtomicStageDecision에도 상태판 판단은 있다.
하지만 score_present = 0이고 FULL_THESIS scope가 아니다.
대표 row라도 FULL_THESIS 진단서가 아니다.
```

쉬운 예:

```text
접수표 대표 환자 74명
!= 진단서 발급 환자 74명
```

### 6.3 Brain/Web enabled diagnostic v28

직접 집계 결과:

```text
verdict = BLOCKED
brain_web_mode = enabled
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
```

해석:

```text
LLM planner와 web/search/extractor 시도는 있었다.
하지만 web_or_llm accepted claim은 0개다.
따라서 Brain/Web operating pass가 아니다.
```

### 6.4 FULL_THESIS production runner v28

직접 집계 결과:

```text
verdict = PENDING_PRODUCTION_FULL_THESIS
candidate_row_count = 1
blocked_candidate_count = 1
promoted_full_thesis_row_count = 0
production_mode_requested = true
```

blocked candidate:

```text
symbol = 114450
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
candidate_source = stagecourt_trace_direct_scan
present_primitives =
  contract_amount_to_prior_sales
  contract_duration_months
  delivery_schedule
missing_green_primitives =
  margin_bridge_visible
blockers =
  missing_green_gate_primitives
```

해석:

```text
계약 금액/기간/납품 일정 primitive는 닫혔다.
하지만 C05 Green/FULL_THESIS에는 margin_bridge_visible이 필요하다.
그래서 운영 Stage 승격은 0개인 게 맞다.
```

쉬운 예:

```text
"공급계약이 있다"는 확인됐다.
하지만 "이 계약이 마진을 얼마나 개선하는지"가 닫히지 않았다.
따라서 Green 진단서를 발급하면 안 된다.
```

### 6.5 Queue / timeout ledger-refresh v30

직접 집계 결과:

```text
brain_web_mode = disabled
brain_web_readiness verdict = NOT_REQUESTED
source_task_execution_count = 0
web_or_llm_accepted_claim_count = 0
full_thesis_refresh_queue_audit verdict = PASS
```

해석:

```text
v30은 Brain/Web enabled run이 아니다.
v30은 queue/timeout ledger-refresh를 검증한 run이다.
v28 숫자와 v30 숫자를 한 실행처럼 섞으면 안 된다.
```

## 7. "뭔가 잘못되고 있나?"에 대한 현재 답

맞다. 아직 잘못되고 있는 부분이 있다.

다만 잘못의 성격을 정확히 나눠야 한다.

### 이미 막힌 잘못

```text
1. 블로그/소셜/스톡리스트/사이트 아카이브를 score source로 쓰는 경로
2. 일반 검색 결과 snippet/headline만으로 점수를 주는 경로
3. source lineage 미검증 일반 웹 문서를 TrustedNews/ReportPDF처럼 취급하는 경로
4. BRAIN_WEB_PARTIAL 또는 CENSUS_EVENT_BOARD를 운영 FULL_THESIS처럼 출력하는 경로
5. source rejection feedback에 score/stage를 섞는 경로
```

### 아직 남은 잘못

```text
1. 실제 TrustedNews/ReportPDF/CompanyNewsroom connector가 충분히 닫히지 않았다.
2. Brain/Web enabled run에서 web_or_llm accepted claim이 아직 0개다.
3. FULL_THESIS production row가 아직 0개다.
4. 삼성전자/하이닉스 C06도 production FULL_THESIS live path로 닫힌 것이 아니다.
5. v36은 bad retry를 막지만, 좋은 retry를 실제 원문 claim으로 성공시키는 connector 구현은 아니다.
```

즉 현재 상태는:

```text
가짜 Stage를 막는 방어는 많이 좋아졌다.
하지만 진짜 운영 Stage를 만드는 공격력은 아직 부족하다.
```

## 8. 다음 에이전트가 공격해야 할 질문

다음 리뷰어는 아래를 세게 봐야 한다.

```text
1. source_lineage_unverified_original 이후 discovery-only task 드롭이 실제 production loop에 적용되는가?
2. discovery-only/source-original-capable 분류가 너무 좁거나 너무 넓지 않은가?
3. TrustedNews를 original-capable로 둔 것이 실제 connector 없이는 false confidence를 만들지 않는가?
4. source task가 드롭되면 provider/source pending으로 남는가, 아니면 낮은 점수로 확정되는가?
5. 모든 dropped retry task가 감사 로그에 남는가?
6. 원문 검증 가능한 retry task가 너무 보수적으로 드롭되는 경우는 없는가?
7. v28/v30처럼 서로 다른 run 숫자를 섞어 "운영 Stage가 있다"고 말하는 문서가 남아 있는가?
8. representative=true인 CENSUS_EVENT_BOARD row를 FULL_THESIS 대표 row로 읽는 UI/리포트 경로가 남아 있는가?
9. FULL_THESIS_NOT_RUN인데 verified_score가 붙는 경로가 남아 있는가?
10. web_or_llm accepted claim 없이 Brain/Web pass가 되는 경로가 남아 있는가?
```

## 9. 다음 패치 방향

우선순위는 Stage label을 더 만드는 것이 아니다.
source-backed claim이 실제로 닫히는 경로를 만들어야 한다.

### P0. dropped retry audit export

v36은 discovery-only retry task를 실행 전 드롭한다.
다음 패치는 이 드롭도 leaf artifact에 명시적으로 남겨야 한다.

필요 row:

```text
retry_task_id
candidate_event_id
symbol
reason_tag = source_lineage_unverified_original
drop_reason = discovery_only_retry_after_unverified_original
preferred_source_classes
fallback_source_classes
query_intents
```

왜 필요한가:

```text
드롭이 맞는지 다음 에이전트가 검사할 수 있어야 한다.
조용히 사라지면 "왜 조사가 안 됐나"를 다시 추적하기 어렵다.
```

### P1. original-capable connector 실제화

다음 source class부터 실제 원문 fetch/lineage 검증을 닫아야 한다.

```text
CompanyNewsroom
ReportPDF
BrokerReportPublicPDF
TrustedNews original URL
IR
KIND/DART web-discovered detail
```

주의:

```text
connector가 없으면 원문 가능 class라도 accepted claim까지 못 간다.
그 경우 낮은 점수 확정이 아니라 SourcePending / ProviderPending이어야 한다.
```

### P2. FULL_THESIS production row 생성 조건 닫기

FULL_THESIS row는 아래 chain이 전부 있어야 한다.

```text
SourceTask
  -> fetched original/source-backed document
  -> EvidenceAnchor
  -> accepted_claim
  -> PrimitiveState
  -> ScoreContribution
  -> StageCourt trace
  -> stage_scope = FULL_THESIS representative row
```

하나라도 없으면:

```text
FULL_THESIS_NOT_RUN
또는 PENDING_MATERIAL_GAPS
또는 ProviderPending / SourcePending
```

이어야 한다.

### P3. 삼성전자/하이닉스 C06 live smoke를 fake/smoke가 아닌 production path로 재실행

목표:

```text
005930 / 000660
  -> C06 hypothesis
  -> original-capable source tasks
  -> real source-backed accepted claims
  -> C06 primitive states
  -> deterministic score
  -> StageCourt
  -> FULL_THESIS row 또는 명시적 Pending
```

주의:

```text
점수가 낮아도 괜찮다.
중요한 것은 왜 낮은지 claim/gap으로 설명되는 것이다.
provider/source failure를 0점 확정으로 만들면 다시 실패다.
```

## 10. 최종 판정

현재 결론:

```text
Stage가 있는 애들은 있다.
하지만 운영 FULL_THESIS Stage가 있는 애들은 없다.
```

v36 패치 후 결론:

```text
source_lineage_unverified_original feedback 이후
동일한 discovery-only retry 반복은 차단된다.

하지만 아직 실제 운영 FULL_THESIS production success는 아니다.
```

다음 완료 기준:

```text
1. web_or_llm accepted claim > 0
2. FULL_THESIS production row > 0
3. FULL_E2R_100 verified score row > 0
4. 삼성전자/하이닉스 C06 production path 결과가 source-backed claim/gap으로 설명됨
5. dropped retry/source pending/accepted retry가 모두 leaf artifact로 추적됨
```

이 다섯 개가 닫히기 전에는 "운영 Stage가 완성됐다"고 말하면 안 된다.

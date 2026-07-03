# Census v4 0701 v84 Operational Stage Zero Root Cause / Cross Review / Patch Direction

작성일: 2026-07-03

대상 실행:

```text
output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v82
```

관련 코드 패치 상태:

```text
artifact_truth_version = v82
code_guard_patch_version = v83
v83_live_rerun_required = true
```

이 문서는 "Stage가 있는 애들이 있긴 해?"라는 질문에 대해 다음 에이전트가 강하게 반박할 수 있도록 만든 최신 감사/방향성 문서다.

## 0. 결론

있다. 하지만 운영자가 써도 되는 Stage는 없다.

```text
Stage처럼 보이는 표시:
  85개

운영 FULL_THESIS / FULL_E2R Stage:
  0개
```

쉬운 예:

```text
CENSUS_EVENT_BOARD = 출석부
BRAIN_WEB_PARTIAL = 몇 문제만 푼 쪽지시험
FULL_THESIS = 최종 성적표
```

현재 v82에는 출석부와 쪽지시험은 있다. 최종 성적표는 없다.

따라서 정확한 답은:

```text
Stage row는 3,391개 있다.
그중 Stage0이 아닌 표시도 85개 있다.
하지만 모든 row가 operator_stage_use=NOT_FULL_THESIS_STAGE다.
즉 운영에서 쓸 FULL_THESIS/FULL_E2R Stage는 0개다.
```

이 상태는 두 가지 의미를 동시에 가진다.

```text
좋은 점:
  가짜 FULL_THESIS 승급을 막는 guard는 작동하고 있다.

나쁜 점:
  실제 운영 pipeline으로 full thesis를 생성하는 capability는 아직 부족하다.
```

## 1. 최신 숫자

`census_stage_status.jsonl` 기준:

| 항목 | count |
|---|---:|
| total stage status rows | 3,391 |
| `stage_scope=CENSUS_EVENT_BOARD` | 3,390 |
| `stage_scope=BRAIN_WEB_PARTIAL` | 1 |
| `stage_scope=FULL_THESIS` | 0 |
| `operator_stage_use=NOT_FULL_THESIS_STAGE` | 3,391 |
| `operator_score_use=NOT_FULL_E2R_SCORE` | 3,391 |
| `full_thesis_stage=FULL_THESIS_NOT_RUN` | 3,391 |
| `full_e2r_verified_score_row_count` | 0 |
| `verified_score_present_count` | 0 |

`canonical_stage` 분포:

| canonical_stage | count | 운영 해석 |
|---|---:|---|
| `0` | 3,306 | 대부분 NoCurrentCatalyst 상태판 |
| `1` | 54 | event board 또는 brain partial |
| `2` | 30 | event board material watch |
| `3-Red` | 1 | event board risk review |

중요:

```text
canonical_stage=1/2/3-Red가 있어도 stage_scope가 FULL_THESIS가 아니면 운영 Stage가 아니다.
```

`readiness_verdict.json`:

```text
verdict = NOT_READY
operational_stage_use_allowed = false
meaningful_operational_stage_pass = false
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
event_board_non_stage0_count = 84
```

`census_stage_summary.json`:

```text
event_board_non_stage0_count = 84
event_evidence_score_count = 67
full_thesis_refresh_queue_candidate_count = 84
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
```

## 2. "뭔가 잘못되고 있는가?"

기대가 "실제 daily 운영 Stage를 뽑는다"라면 맞다. 아직 잘못되고 있다.

다만 잘못의 성격은 예전과 다르다.

예전 위험:

```text
부족한 근거로 stage/score를 확정해 버림
```

현재 위험:

```text
가짜 승급은 막았지만,
source acquisition -> accepted claim -> primitive -> StageCourt -> FULL_THESIS
사슬이 실제 운영에서 충분히 닫히지 않음
```

쉬운 예:

```text
예전 문제:
  검색 결과 snippet 하나 보고 "합격"이라고 써 버림.

현재 문제:
  snippet 합격은 막았지만,
  원문 서류를 충분히 가져와서 최종 합격증을 발급하는 단계가 아직 거의 안 돌아감.
```

## 3. Event 종류를 다시 고정한다

전 종목 Census에서는 모든 종목이 평가 대상에 오른다. 하지만 모든 종목에 사업/투자 트리거가 생긴 것은 아니다.

### 3.1 CensusAssessmentEvent

뜻:

```text
이번 Census에서 이 종목도 확인했다는 행정 스탬프
```

점수 재료인가:

```text
아니다.
```

예:

```text
삼성전자: CensusAssessmentEvent 있음
SK하이닉스: CensusAssessmentEvent 있음
아무 공시 없는 소형주: CensusAssessmentEvent 있음
```

이것은 출석 체크다. 성적표가 아니다.

### 3.2 CandidateEvent

뜻:

```text
공시, 리포트, 가격 이상, 위험 신호처럼 조사를 열 만한 사건
```

점수 재료인가:

```text
그 자체로는 아니다.
```

예:

```text
DART에서 "단일판매공급계약" 공시가 발견됐다.
  -> CandidateEvent다.

그 공시 원문에서 계약금액, 기간, 대상회사 직접성, 현재성이 accepted_claim으로 닫혔다.
  -> 그때 score contribution 가능.
```

### 3.3 AcceptedClaim / PrimitiveState / ScoreContribution

점수는 여기서부터 가능하다.

최소 사슬:

```text
EvidenceDocument
  -> EvidenceAnchor
  -> AcceptedClaim
  -> PrimitiveState
  -> ScoreContribution
  -> StageCourtTrace
```

운영 FULL_THESIS는 여기에 더해서:

```text
FULL_THESIS row
operator_stage_use=FULL_THESIS_STAGE
operator_score_use=FULL_E2R_SCORE
```

까지 닫혀야 한다.

## 4. 삼성전자 / SK하이닉스 현재 상태

### 4.1 삼성전자

`census_stage_status.jsonl`:

```text
symbol = 005930
company_name = 삼성전자
stage_scope = CENSUS_EVENT_BOARD
canonical_stage = 1
event_evidence_score = 4.0
accepted_claim_count = 1
score_contribution_count = 1
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
full_thesis_verified_score = null
```

`full_thesis_seed_materialization_trace.jsonl`:

```text
materialization_status = PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS
planner_run_count = 1
planner_real_provider_success_count = 0
source_task_execution_count = 0
accepted_claim_count = 0
score_contribution_count = 0
stagecourt_trace_count = 0
promoted_to_full_thesis = false
```

해석:

```text
삼성전자는 event board Stage1 표시가 있다.
하지만 full thesis source task가 실제 claim/StageCourt까지 가지 못했다.
운영 Stage/운영 점수는 없다.
```

쉬운 예:

```text
"삼성전자 관련 최근 공시/이벤트가 하나 있어서 봐야 한다"는 상태다.
"삼성전자 HBM thesis를 운영 점수로 평가했다"는 상태가 아니다.
```

### 4.2 SK하이닉스

`census_stage_status.jsonl`의 유일한 `BRAIN_WEB_PARTIAL`:

```text
symbol = 000660
company_name = SK하이닉스
stage_scope = BRAIN_WEB_PARTIAL
canonical_stage = 1
event_evidence_score = 60.0
score_scale = EVENT_WEIGHTED_PARTIAL
score_scope = BRAIN_WEB_CLAIM_BACKED_PARTIAL
accepted_claim_count = 3
score_contribution_count = 6
score_interval_lower = 60.0
score_interval_upper = 60.0
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
full_thesis_verified_score = null
```

`stagecourt_traces.jsonl`의 Brain trace:

```text
stagecourt_trace_id = SCT-BRAIN-c8a68b504ac586681b20
accepted_claim_ids = 3개
score_contribution_ids = 6개
score_interval = 60.0 ~ 60.0
missing_green_primitives =
  hbm_capacity_constraint
  hbm_capacity_pre_sold
```

`full_thesis_production_runner_audit.json`:

```text
candidate_source = brain_web_partial_stage_row
primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
blockers =
  missing_green_gate_primitives
present_primitives =
  customer_preorder_or_allocation
  medium_term_revision_visibility
  revenue_visibility_contract
missing_green_primitives =
  hbm_capacity_constraint
  hbm_capacity_pre_sold
promoted_full_thesis_row_count = 0
```

해석:

```text
SK하이닉스는 Research Brain이 원문 리포트 하나를 가져와 partial claim-backed stage를 만들었다.
하지만 C06 full thesis에 필요한 capacity constraint / pre-sold capacity claim이 direct/current/source-backed로 안 닫혔다.
그래서 FULL_THESIS 승급은 0이다.
```

쉬운 예:

```text
고객 물량 배정 관련 증거는 있다.
하지만 "생산능력이 잠겼는가"와 "이미 선판매/배정됐는가"가 아직 서류로 닫히지 않았다.
그래서 C06 최종 성적표는 못 준다.
```

## 5. Root Cause: FULL_THESIS 0의 사슬

현재 병목은 큐가 없는 것이 아니다.

```text
full thesis refresh queue candidate = 84개
```

문제는 큐 이후다.

```text
full thesis seed 있음
  -> planner run 일부 있음
  -> source task 일부 있음
  -> 실제 문서 일부 fetch
  -> accepted claim 극소수
  -> direct green primitive 부족
  -> StageCourt trace 부족
  -> FULL_THESIS 승급 0
```

v82 핵심 숫자:

```text
planner_run_seed_count = 21
real_provider_success_seed_count = 1
stagecourt_trace_seed_count = 1
full_thesis_promoted_seed_count = 0
```

`brain_web_readiness_gate_audit.json`:

```text
verdict = BLOCKED
planner runs = 21/30
web search tasks = 3/20
web/news calls = 3/20
fetched documents = 1/10
claim extractor attempts = 1/10
```

이것은 "LLM이 아예 없었다"가 아니라:

```text
LLM/planner가 실제 source-backed full thesis를 충분히 생산하지 못했다.
```

에 가깝다.

## 6. Source Acquisition Root Cause

### 6.1 IssuerIR

현재 `IssuerIRLiveConnector`는 placeholder다.

운영 의미:

```text
IssuerIR/IR source task는 source_task_execution row는 만들 수 있다.
하지만 live EvidenceDocument/AcceptedClaim으로 이어지지 않는다.
```

예:

```text
planner가 "IR에서 HBM capacity sold-out 확인" task를 만든다.
IssuerIR connector가 issuer_ir_discovery_not_configured로 끝난다.
그러면 claim이 없고 점수도 없다.
```

### 6.2 TrustedNews

현재 `TrustedNewsLiveConnector`도 placeholder다.

운영 의미:

```text
TrustedNews provider가 없으면 pending/provider failure가 맞다.
generic web 검색 결과를 TrustedNews 점수 증거로 바꾸면 안 된다.
```

예:

```text
네이버 검색 결과에 "SK하이닉스 HBM 공급"이 보인다.
  -> 조사 후보일 수는 있다.

원문 기사 URL, 게시일, 본문 anchor, source identity가 검증됐다.
  -> 그때 claim 후보가 된다.
```

### 6.3 ReportPDF

ReportPDF/BrokerReportPublicPDF는 현재 부분적으로 작동했다.

SK하이닉스 partial row는 다음 리포트 원문에서 나왔다.

```text
https://stock.pstatic.net/stock-research/company/17/20251031_company_162545000.pdf
```

하지만 리포트 한 개로 C06 full thesis 전체가 닫히지 않았다.

필요한 guard:

```text
verified report original URL
PDF text extraction success
target directness
as_of_date <= 2026-07-01
primitive mapping accepted
claim-document-source task linkage
```

### 6.4 CompanyNewsroom / Issuer Official Domain

현재 registry:

```text
configs/e2r_issuer_official_domains_v1.json
SK하이닉스 newsroom entries
valid_from = 2026-07-03
verified_as_of = 2026-07-03
```

v82 as-of:

```text
as_of_date = 2026-07-01
```

따라서 이 registry를 v82 실행에 쓰면 미래누수다.

쉬운 예:

```text
2026-07-01에 판단한다고 하면서
2026-07-03에 검증한 공식 도메인 장부를 쓰면 안 된다.
```

이건 코드가 막아야 하고, 현재 무시되는 것이 맞다. 다만 운영 capability를 늘리려면 domain authority 자체를 as-of 안전하게 backfill해야 한다.

## 7. Cross-Validation Findings

### 7.1 교차검증 A: Stage 존재 여부

결론:

```text
운영 FULL_THESIS/FULL_E2R Stage = 0개
비운영 이벤트/부분 Stage 표시 = 85개
```

핵심 문장:

```text
Stage처럼 보이는 표시는 85개 있지만,
운영에서 쓸 FULL_THESIS/FULL_E2R Stage는 v82에 0개다.
```

### 7.2 교차검증 B: Source acquisition

결론:

```text
FULL_THESIS=0의 핵심 원인은 queue 부재가 아니다.
queue 이후 source acquisition이 score-eligible accepted claim까지 거의 못 이어진다.
```

주요 병목:

```text
IssuerIRLiveConnector = placeholder
TrustedNewsLiveConnector = placeholder
ReportPDF = verified original일 때만 부분 작동
CompanyNewsroom = verified issuer domain 필요
2026-07-03 registry는 2026-07-01 replay에 사용 불가
```

### 7.3 교차검증 C: 문서/목표 구멍

다음 리뷰어가 공격할 지점:

```text
FULL_THESIS_SMOKE_PASS가 pending honesty와 execution success를 섞고 있음
CensusAssessmentEvent vs CandidateEvent schema/gate가 충분히 hard하지 않음
LLM query provenance가 hard gate로 승격되지 않음
production/backfill 수집 폭 지침이 충돌해 보임
v83은 guard patch이지 v83 runtime truth가 아님
all-archetype replay parity 6/32 ready, missing 26이 goal gate에 더 강하게 연결돼야 함
```

## 8. 반드시 고쳐야 할 문서/게이트 용어

### 8.1 FULL_THESIS smoke label 분리

현재 문제:

```text
FULL_THESIS_SMOKE_PASS가 "pending을 정직하게 표시함"과
"실제로 full thesis execution이 성공함"을 섞을 수 있다.
```

분리해야 한다.

```text
FULL_THESIS_SMOKE_HONESTY_PASS
  = full thesis 미실행/보류를 거짓 Stage로 말하지 않음

FULL_THESIS_SMOKE_EXECUTION_PASS
  = source task -> accepted claim -> score contribution -> StageCourt -> FULL_THESIS row까지 실제 실행 성공
```

현재 v82는:

```text
HONESTY 쪽은 상당 부분 pass
EXECUTION 쪽은 fail/pending
```

### 8.2 Stage row와 operator row 분리

문서/리포트에서 다음 표현을 금지해야 한다.

```text
Stage가 있다 = 운영 Stage가 있다
```

항상 이렇게 써야 한다.

```text
stage_status row count
event-board non-Stage0 count
brain-web partial count
FULL_THESIS row count
FULL_E2R verified score row count
operator_stage_use
operator_score_use
```

### 8.3 Query provenance hard gate

`hardcoded_query_count=0`만으로는 부족하다.

필요한 필드:

```text
planner_run_id
planner_provider
llm_prompt_id 또는 prompt_hash
llm_response_id 또는 response_hash
query_intent_id
llm_generated_query
query_validation_status
query_rejection_reason
```

운영 pass 조건:

```text
모든 live web SourceTask query는 LLM planner response에 provenance가 있어야 한다.
deterministic code는 target/as_of/date/duplicate/policy 검증만 한다.
```

나쁜 예:

```text
llm_generated_query 필드만 채워 놓고 실제로는 코드 템플릿에서 만든 query
```

좋은 예:

```text
planner response id PRSP-123에서 나온 query Q-456
-> target scoped 검증 PASS
-> as_of_date 검증 PASS
-> source task 실행
```

### 8.4 Production / Backfill 수집 폭 충돌 해소

상위 원칙:

```text
Backfill mode:
  source repair와 연구자료 URL 복구용이다.
  넓은 수집 가능.
  결과는 운영 점수로 바로 쓰지 않는다.

Production daily mode:
  SourceTask마다 max_queries, max_candidates, max_fetches, stop_condition이 있어야 한다.
  top_results=None, retry_max=None, 무제한 page fetch 금지.
  official-first.
  provider/source gap은 낮은 점수 확정이 아니라 pending.
```

쉬운 예:

```text
과거 C06 연구자료 URL을 복구하려고 넓게 찾는 것 = backfill
2026-07-01 daily stage를 내려고 뉴스 1,000개 긁는 것 = production 금지
```

## 9. 하면 안 되는 패치

### 9.1 종목별 예외

금지:

```python
if symbol == "005930":
    ...
if symbol == "000660":
    ...
```

### 9.2 아키타입 query 하드코딩

금지:

```python
if archetype == "C06":
    query = f"{company} HBM sold out capacity"
```

해야 하는 것:

```text
LLM planner가 현재 evidence/missing_information/score_gap_context를 보고 query를 제안한다.
deterministic code는 query 검증/예산/중복/as_of_date만 담당한다.
```

### 9.3 Green gate 완화

금지:

```text
C06 capacity primitive가 비어 있으니 Green 조건을 낮춘다.
```

해야 하는 것:

```text
capacity primitive를 채울 source route를 연다.
못 찾으면 pending/material gap으로 둔다.
```

### 9.4 Generic web을 score source로 승격

금지:

```text
네이버 검색 결과에 나왔으니 TrustedNews score evidence로 인정
```

해야 하는 것:

```text
원문 URL, source identity, published_at, fetched body, anchor, target directness가 닫혀야 한다.
```

### 9.5 as-of 미래 registry 사용

금지:

```text
2026-07-01 replay에 2026-07-03 verified_as_of registry를 사용
```

해야 하는 것:

```text
as_of_date 이전에 검증된 authority만 사용
또는 backfill로 authority evidence를 as-of 안전하게 생성
```

## 10. 맞는 패치 방향

### P0. 문서/게이트 의미 잠금

1. `FULL_THESIS_SMOKE_HONESTY_PASS`와 `FULL_THESIS_SMOKE_EXECUTION_PASS` 분리.
2. `goal_completion_ready`에는 execution pass만 사용.
3. `stage_status_count`와 `full_thesis_stage_row_count`를 모든 report에 같이 출력.
4. `FULL_THESIS row=0`이면 `operational_stage_use_allowed=false`가 hard fail이어야 한다.

### P0. Event schema hardening

Assessment-only row는 다음을 가져야 한다.

```text
census_assessment_event_id != null
census_assessment_event_score_evidence_allowed = false
candidate_event_scope = ASSESSMENT_ONLY
candidate_event_ids = []
score_contribution_count = 0
operator_score_use = NOT_FULL_E2R_SCORE
```

CandidateEvent row는 다음을 분리해야 한다.

```text
CandidateEvent exists
accepted_claim exists
score_contribution exists
```

CandidateEvent만 있고 accepted claim이 없으면:

```text
Stage0 / Stage1 / Pending / Watch 가능
운영 점수 확정 불가
```

### P0. Query provenance gate

운영 live web task pass 조건:

```text
query_intent came from real planner response
planner_provider not fake
prompt/response hash recorded
query target scoped
query as-of safe
query duplicate not already exhausted
```

### P1. IssuerIR capability

`IssuerIRLiveConnector`를 실제 bounded discovery/fetch connector로 만든다.

요구 조건:

```text
official-first
bounded budget
as_of_date safe
canonical URL
content_hash
published_at/available_at/fetched_at
symbol/company target directness
document text / table / PDF anchor
source lineage proof
```

주의:

```text
IR main page나 portal main page만 fetch해서 문서 수를 늘리면 안 된다.
symbol-specific, claim-specific 원문이어야 한다.
```

### P1. TrustedNews capability

`TrustedNewsLiveConnector`는 generic search alias가 아니라 trusted original article provider여야 한다.

요구 조건:

```text
trusted source identity
original article URL
published_at
full body fetched
anchor verified
target directness
source family dedupe
```

provider가 없으면:

```text
ProviderPending
낮은 점수 확정 금지
```

### P1. ReportPDF verifier 확장

방향:

```text
종목/아키타입 조건이 아니라
인정 가능한 report 원본 도메인, URL 패턴, PDF fetch, text extraction, title/date 검증을 확장
```

ReportPDF가 성공해도:

```text
단일 리포트 하나만으로 source quorum/green gate를 자동 통과시키지 않는다.
```

### P1. Issuer official domain authority backfill

현재 registry의 `2026-07-03` entry는 `2026-07-01` replay에서 못 쓴다.

필요:

```text
authority evidence 자체를 문서화
valid_from / verified_as_of / valid_to
source_url / source_anchor_text
as_of_date check
```

### P1. Full thesis attempt continuation

현재 accepted claim 목표가 충분히 강하지 않으면 0-claim 후보를 만나고 멈출 수 있다.

방향:

```text
production full-thesis refresh mode에서 bounded budget 안에
accepted_claim_target / stagecourt_trace_target / material_gap_target을 분리 검토
```

주의:

```text
accepted_claim_target을 올리는 것은 source coverage 개선책이다.
direct primitive 없이 FULL_THESIS 승급시키는 장치가 아니다.
```

## 11. 다음 patch acceptance

다음 패치는 최소 아래를 통과해야 한다.

```text
1. FULL_THESIS_SMOKE_HONESTY_PASS와 EXECUTION_PASS 분리.
2. goal completion은 EXECUTION_PASS 없으면 false.
3. stage row report가 stage_scope/operator_stage_use/operator_score_use를 항상 함께 표시.
4. Assessment-only row가 score contribution을 만들면 fail.
5. CandidateEvent-only row가 FULL_E2R score를 만들면 fail.
6. 모든 live web query가 planner_run_id/prompt_response_id provenance를 가짐.
7. deterministic query template count = 0.
8. IssuerIR placeholder provider failure가 low score로 확정되지 않음.
9. TrustedNews provider failure가 low score로 확정되지 않음.
10. verified_as_of > as_of_date registry entry가 사용되면 fail.
11. generic web result가 source lineage 없이 accepted claim으로 들어가면 fail.
12. ReportPDF는 verified original route 없으면 score source 불가.
13. SK하이닉스 partial row는 FULL_THESIS로 오인되지 않음.
14. 삼성전자 event-board Stage1은 FULL_THESIS로 오인되지 않음.
15. FULL_THESIS row가 0이면 readiness verdict는 NOT_READY.
```

## 12. 최종 목표 상태

최종적으로는 다음이 되어야 한다.

```text
전체 KRX universe
  -> CensusAssessmentEvent 부여
  -> cheap baseline scan
  -> CandidateEvent 또는 NoCurrentCatalyst 분리
  -> 필요한 종목만 Research Brain / Evidence OS deep
  -> source-backed accepted claim 생성
  -> primitive state aggregation
  -> deterministic score contribution
  -> StageCourt
  -> FULL_THESIS row 또는 명시적 Pending/NoCurrentCatalyst
```

출력 의미:

```text
아무 새 공시도 없는 종목:
  Stage0 / NoCurrentCatalyst
  점수 없음

공시/리포트는 있지만 claim 부족:
  Pending / Watch
  raw 참고점수와 운영 점수 분리

provider 실패:
  ProviderPending
  낮은 점수 확정 금지

claim이 충분히 닫힌 종목:
  FULL_THESIS / FULL_E2R score 가능
```

한 줄 원칙:

```text
트리거는 조사를 여는 문이고,
claim만 점수를 여는 열쇠다.
```

## 13. 현재 상태를 한 문장으로

```text
v82/v83 기준 시스템은 가짜 Stage를 막는 방향으로는 좋아졌지만,
운영 FULL_THESIS Stage를 실제로 생성하는 source acquisition capability와
LLM query/source provenance gate가 아직 부족해서,
현재 운영 Stage는 0개이고 goal.md/goal2.md/goal3.md는 완료가 아니다.
```


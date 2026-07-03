# Census v4 0701 Operational Stage Truth Deep Audit / Next Patch Direction

작성 시점: 2026-07-02 06:47 KST  
repo: `/home/eorb915/projects/stock_agent`  
canonical output: `output/census_v4/2026-07-01`  
as_of_date: `2026-07-01`

> 최신 수치 주의: 이 문서는 C15 패치 직후 스냅샷이다. C17 source-backed replay 이후 최신값은 `census_v4_0701_latest_c17_source_backed_replay_stage_truth_and_review_packet_2026-07-02.md`와 `README.md`를 기준으로 한다. 최신 replay matrix는 `source_backed_ready_count=4`, `guard_replay_ready_count=4`, `missing_required_archetype_count=28`, controlled semantic replay는 `8/10 pass`다. Stage truth 자체는 변하지 않았다. 운영 `FULL_THESIS` row는 여전히 0개다.

## 한 줄 결론

```text
Stage 라벨은 있다.
하지만 지금 canonical output에는 운영 full-thesis Stage가 없다.

현재 Stage1 54개, Stage2-Watch 30개, Red 1개는 전부 CENSUS_EVENT_BOARD 상태판이다.
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
verified_score_present_count = 0
```

쉬운 예:

```text
출석부에는 "관심 필요"라고 표시된 학생이 있다.
하지만 기말고사 100점 채점지가 나온 학생은 아직 0명이다.

지금 Stage1/Stage2-Watch는 출석부 상태표에 가깝고,
우리가 원하는 운영 E2R Stage는 기말고사 채점지에 가깝다.
```

따라서 지금 산출물을 보고:

```text
좋은 해석:
  전 종목 Census 상태판은 있고, 일부 공식 이벤트가 Stage1/Stage2-Watch 상태로 분리된다.

나쁜 해석:
  현재부터 실제 운영 파이프라인이 삼성전자/하이닉스 같은 종목을 full E2R 점수로 채점했다.
```

## 교차검증한 파일

직접 대조한 canonical 파일:

```text
output/census_v4/2026-07-01/census_stage_summary.json
output/census_v4/2026-07-01/census_stage_status.jsonl
output/census_v4/2026-07-01/accepted_claims.jsonl
output/census_v4/2026-07-01/score_contributions.jsonl
output/census_v4/2026-07-01/stagecourt_traces.jsonl
output/census_v4/2026-07-01/goal_completion_audit.json
output/census_v4/2026-07-01/goal_requirement_matrix_audit.json
output/census_v4/2026-07-01/readiness_verdict.json
output/census_v4/2026-07-01/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01/full_thesis_production_audit.json
output/census_v4/2026-07-01/samsung_hynix_full_thesis_smoke.json
output/census_v4/2026-07-01/all_archetype_replay_matrix.json
output/census_v4/2026-07-01/controlled_semantic_replay_audit.json
```

코드/워크트리 위험도 같이 확인한 파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/census/census_v4_auditor.py
src/e2r/production/claim_extraction/contract_blind_extractor.py
src/e2r/production/claim_extraction/primitive_mapper.py
tests/test_census_v4_all_archetype_replay_matrix.py
tests/test_census_v4_goal_required_audits.py
```

## 현재 Stage 존재 여부

`census_stage_summary.json`:

```text
stage_status_count = 3391
candidate_event_count = 226
score_eligible_candidate_event_count = 92
event_evidence_score_count = 67
full_e2r_verified_score_count = 0
verified_score_present_count = 0

stage_distribution:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 30
  Red = 1
```

`census_stage_status.jsonl` leaf row 집계:

```text
stage_scope:
  CENSUS_EVENT_BOARD = 3391

is_full_thesis_stage:
  false = 3391

is_full_e2r_score:
  false = 3391

score_scope:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67

score_valid_status:
  NO_CURRENT_EVENT = 3306
  FINAL_WITH_NONMATERIAL_GAPS = 37
  PENDING_MATERIAL_GAPS = 30
  NOT_SCORED = 11
  INVALID_EVIDENCE = 7
```

해석:

```text
Stage0 3306개:
  현재 event/catalyst 없음이라는 Census 상태다.
  "E2R 0점"이라는 뜻이 아니다.

Stage1 54개:
  공식 이벤트나 약한 material claim이 있어 WATCH가 열린 상태다.
  full thesis Stage1이 아니다.

Stage2-Watch 30개:
  direct official material claim은 있으나 multi-source/cash/revision bridge가 부족한 상태다.
  full thesis Stage2가 아니다.

Red 1개:
  current direct risk 신호가 있는 event-board Red다.
  과거 live-run의 잘못된 4C 같은 full thesis hard break와 섞으면 안 된다.
```

쉬운 예:

```text
"단일판매공급계약 공시가 있다"
  -> Stage2-Watch 상태판 가능

"그 계약이 수주잔고, 마진, FCF, EPS revision까지 이어져 C05/C06 thesis가 닫혔다"
  -> 아직 아님
```

## 삼성전자 / SK하이닉스 현재 canonical truth

### 삼성전자 `005930`

현재 row:

```text
base_stage = Stage1
canonical_stage = 1
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
is_full_thesis_stage = false
verified_score = null
full_thesis_stage = FULL_THESIS_NOT_RUN
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
candidate_event_count = 4
accepted_claim_count = 1
score_contribution_count = 1
score_valid_status = FINAL_WITH_NONMATERIAL_GAPS
stage_decision_status = FINAL
full_thesis_missing_primitives = ["full_thesis_refresh_task_not_run"]
```

현재 accepted claim:

```text
primitive_id = information_confidence
quote_text = 삼성전자(005930) 풍문또는보도에대한해명(미확정) OpenDART 접수번호 20260624801004 접수일 2026-06-24
source_url = https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260624801004
event_date = 2026-06-24
score_eligible = true
target_scope_status = DIRECT
temporal_status = CURRENT
```

현재 score contribution:

```text
component_key = information_confidence
raw_points = 1.0
max_points = 5.0
support_claim_ids = [CLM-9aaf6a921e683a2ee9b4]
```

해석:

```text
삼성전자 current canonical row는 HBM/C06 thesis 평가가 아니다.
단지 DART 해명 공시 1개를 상태판에 올린 것이다.
따라서 이 row로 "삼성전자 Stage1"이라고 운영 결론을 내리면 안 된다.
```

### SK하이닉스 `000660`

현재 row:

```text
base_stage = Stage1
canonical_stage = 1
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
is_full_thesis_stage = false
verified_score = null
full_thesis_stage = FULL_THESIS_NOT_RUN
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
candidate_event_count = 8
accepted_claim_count = 1
score_contribution_count = 1
score_valid_status = FINAL_WITH_NONMATERIAL_GAPS
stage_decision_status = FINAL
full_thesis_missing_primitives = ["full_thesis_refresh_task_not_run"]
```

현재 symbol-level accepted claims:

```text
1. primitive_id = capital_allocation_event
   quote_text = SK하이닉스(000660) 주요사항보고서(유상증자결정) OpenDART 접수번호 20260624000420 접수일 2026-06-24
   raw_points = 2.0 / 5.0

2. primitive_id = information_confidence
   quote_text = SK하이닉스(000660) 증권신고서(지분증권) OpenDART 접수번호 20260624000511 접수일 2026-06-24
   raw_points = 1.0 / 5.0
```

대표 Stage row에 실제 연결된 claim:

```text
accepted_claim_ids = [CLM-14057362610ae62c7e02]
score_contribution_ids = [SCON-8da68431606c7699ece3]
raw_contribution_score = 1.0
event_evidence_score = 4.0
```

추가 리뷰 포인트:

```text
전역 accepted_claims/score_contributions 파일에는 SK하이닉스 claim/contribution이 2개 존재한다.
하지만 대표 Stage row에는 1개만 연결된다.

이것이 "대표 atomic decision을 하나 고르는 정상 동작"인지,
아니면 symbol-level accepted claim이 대표 row에 누락되는 집계 문제인지는 다음 패치에서 확인해야 한다.
```

해석:

```text
SK하이닉스 current canonical row도 HBM/C06 thesis 평가가 아니다.
현재 row는 유상증자/증권신고서류 DART 이벤트 상태판이다.
```

## 현재 accepted claim / score contribution의 정체

`accepted_claims.jsonl`:

```text
accepted_claim_count = 92
source_provider:
  OpenDART = 92

primitive_id:
  contract_quality = 39
  capital_allocation_event = 32
  information_confidence = 16
  capacity_expansion = 5

semantic_status:
  PASS = 92

target_scope_status:
  DIRECT = 92

temporal_status:
  CURRENT = 92

unique_symbols = 74
```

`score_contributions.jsonl`:

```text
score_contribution_count = 92
```

`stagecourt_traces.jsonl`:

```text
stagecourt_trace_count = 92
```

중요한 관찰:

```text
현재 대표 Stage row에서 score_contribution_count > 0인 row는 67개다.
그 67개는 모두 primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP로 표시된다.
```

리뷰 포인트:

```text
OpenDART 이벤트를 너무 넓게 C05로 보내고 있는지 검증해야 한다.
계약/증자/해명/정보성 공시가 모두 C05로 몰리면, 다음 단계에서 잘못된 archetype별 Stage 판단으로 번질 수 있다.
```

쉬운 예:

```text
건설사가 단일판매계약을 공시했다
  -> C05 후보일 수 있다.

삼성전자가 풍문 해명 공시를 냈다
  -> information_confidence event일 수는 있어도 C05 EPC mega-contract thesis라고 보면 이상하다.
```

## Goal / readiness 상태

`goal_completion_audit.json` blockers:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_production_pass_false
source_backed_replay_parity_all_archetypes_pending
controlled_semantic_replay_pending
goal_requirement_matrix_pass_false
```

`readiness_verdict.json`:

```text
verdict = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
target_gate_pass = true
meaningful_operational_stage_pass = false
full_thesis_smoke_pass = false
full_thesis_production_pass = false
brain_web_evidence_pass = false
controlled_semantic_replay_pass = false
all_archetype_replay_pass = false
known_bad_regression_pass = true
```

해석:

```text
anti_fake full universe status board는 통과했다.
하지만 이것은 "가짜로 다 됐다고 말하지 않는다"는 통과다.
"운영 full thesis Stage가 된다"는 통과가 아니다.
```

쉬운 예:

```text
좋은 통과:
  "아직 본시험은 안 봤습니다"라고 정직하게 말한다.

아직 아닌 통과:
  본시험을 실제로 보고 채점까지 끝냈다.
```

## Brain/Web 상태

`brain_web_readiness_gate_audit.json`:

```text
run_mode = LEDGER_REFRESH_CENSUS
brain_web_mode = disabled
verdict = NOT_REQUESTED
brain_web_evidence_pass_allowed = false

llm_planner_call_count = 0
llm_real_provider_success_count = 0
source_task_execution_count = 0
web_search_task_count = 0
web_search_call_count = 0
web_fetched_document_count = 0
llm_claim_extractor_attempt_count = 0
web_or_llm_accepted_claim_count = 0
brain_to_claim_trace_count = 0
brain_score_contribution_count = 0
brain_stage_trace_count = 0
brain_promoted_stage_row_count = 0
```

해석:

```text
현재 canonical run은 Brain/Web live acquisition run이 아니다.
LLM planner가 검색을 만들고, 웹/공식자료를 가져오고, claim으로 승격하고, Stage row로 promotion한 증거가 없다.
```

따라서 다음 리뷰어가 공격해야 할 질문:

```text
1. Brain/Web disabled인데 왜 운영 Stage가 있다고 주장하는가?
2. planner/extractor call 0인데 왜 LLM agentic pipeline이 돌았다고 주장하는가?
3. source_task_execution_count 0인데 왜 live source acquisition이 됐다고 주장하는가?
```

현재 답:

```text
그런 주장을 하면 틀린 것이다.
현재 canonical output은 ledger-refresh 상태판이다.
```

## All-archetype replay 상태

`all_archetype_replay_matrix.json`:

```text
all_archetype_replay_pass = false
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 3
guard_replay_ready_count = 3
missing_required_archetype_count = 29

status_counts:
  SOURCE_BACKED_POSITIVE_AND_GUARD_REPLAY_READY = 3
  SOURCE_GAP_PENDING = 29
  GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY = 4
```

READY:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
C15_MATERIAL_SPREAD_SUPERCYCLE
```

Priority PENDING:

```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
C24_BIO_TRIAL_DATA_EVENT_RISK
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

해석:

```text
C06/C08/C15는 실제 source-backed positive + guard replay가 닫혔다.
하지만 32개 required archetype 전체 parity는 아직 아니다.
```

쉬운 예:

```text
32과목 중 3과목만 "원문 읽기 시험"을 통과했다.
전 과목 채점 시스템 완성이라고 말하면 안 된다.
```

## Controlled semantic replay 상태

`controlled_semantic_replay_audit.json`:

```text
case_count = 10
pass_count = 7
pending_count = 3
fail_count = 0
controlled_semantic_replay_pass = false
```

PASS:

```text
C06_HBM_POSITIVE_AND_QUALIFICATION_LAG_GUARD
C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD
C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD
WRONG_SUBJECT_RISK_FIXTURE
OLD_RISK_RESOLVED_FIXTURE
PROVIDER_FAILURE_PENDING_FIXTURE
SEMANTIC_CONTRACT_GUARD_FIXTURE
```

PENDING:

```text
C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
C24_CLINICAL_BINARY_EVENT_GUARD
C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

해석:

```text
월덱스/삼성 같은 wrong-subject risk, old risk resolved, provider failure pending 같은 전역 guard는 통과했다.
하지만 핵심 archetype별 semantic replay 3개가 아직 source-backed로 닫히지 않았다.
```

## 현재 로컬 워크트리 위험

`git status --short` 기준으로 워크트리가 매우 dirty다.

중요:

```text
아직 커밋/푸시하면 안 된다.
canonical output과 로컬 코드가 완전히 같은 완성 상태라고 보면 안 된다.
```

이번 패치로 C15 source-backed replay는 canonical output까지 닫혔다.

확인된 C15 완료 항목:

```text
c15_source_backed_semantic_replay.json 생성
positive_replay_pass = true
guard_replay_pass = true
accepted_claim_count = 6
raw_commodity_guard_leaked_primitives = []
all_archetype_replay_matrix C15 accepted_claim_count = 6
guard_case_count = 1
guard_case_pass_count = 1
controlled_semantic_replay pass_count = 7
```

남은 위험:

```text
C17/C24/C28 source-backed replay는 아직 pending이다.
FULL_THESIS production row는 아직 0개다.
Brain/Web evidence pass는 아직 false다.
```

따라서 이제 "C15는 닫힘"이라고 말할 수 있지만, "전체 controlled semantic replay가 닫힘"이라고 말하면 안 된다.

## 왜 지금 상태가 "잘못되고 있는 느낌"을 주는가

문제의 핵심은 Stage 라벨이 같은 단어를 쓰기 때문이다.

현재 한 파일 안에 아래 두 세계가 섞여 보인다.

```text
1. Census 상태판 Stage
   - Stage0 / Stage1 / Stage2-Watch / Red
   - 목적: 전 종목 현재 이벤트 유무 분류
   - score: 없거나 EVENT_WEIGHTED_PARTIAL
   - operator_stage_use = NOT_FULL_THESIS_STAGE

2. Full thesis 운영 Stage
   - Stage2-Actionable / Stage3-Yellow / Stage3-Green / 4B / 4C 등
   - 목적: 아키타입 thesis의 evidence-backed score/stage 판정
   - score: FULL_E2R_100
   - operator_stage_use = FULL_THESIS_STAGE
```

지금 canonical output은 1번만 있다.

쉬운 예:

```text
Stage2-Watch 라벨을 봤다
  -> "운영 Stage2구나"라고 읽으면 틀림

stage_scope를 같이 봤다
  -> CENSUS_EVENT_BOARD라면 상태판임
  -> FULL_THESIS라면 운영 후보임
```

## 다음 패치 방향

### Patch 0. 진실 표시 보호

목표:

```text
사용자가 Stage 라벨만 보고 운영 Stage로 오해하지 않게 모든 산출물/문서/리포트에서 scope를 강제 표시한다.
```

필수 조건:

```text
1. `stage_scope=CENSUS_EVENT_BOARD` row는 operator-facing report에서 "운영 Stage 아님" 문구를 붙인다.
2. `verified_score=null`이면 점수처럼 표시하지 않는다.
3. `EVENT_WEIGHTED_PARTIAL`은 full E2R score로 합산/정렬하지 않는다.
4. 삼성전자/하이닉스 current canonical row를 HBM/C06 thesis 평가로 보여주지 않는다.
```

예:

```text
삼성전자 Stage1
```

라고 쓰면 안 된다.

```text
삼성전자 Census Event Board: Stage1-like watch, FULL_THESIS_NOT_RUN, verified_score 없음
```

처럼 써야 한다.

### Patch 1. C15 source-backed replay 마감 - 완료

이번 패치에서 C15는 정리됐다.

완료 항목:

```text
1. `c15_source_backed_semantic_replay.json` canonical output 생성
2. `_all_archetype_replay_matrix` C15 accepted_claim_count / guard_case_count 집계 수정
3. `census_v4_auditor.py` REQUIRED_JSON에 C15 산출물 반영 여부 결정
4. tests:
   - C15 positive pass-through / spread / margin bridge positive
   - raw commodity headline guard
   - C15 matrix status
   - controlled_semantic_replay pass_count 6 -> 7
   - pending C17/C24/C28로 감소
5. canonical output 재생성
6. README 최신 수치 갱신
```

주의:

```text
원자재 가격 기사만으로 C15 점수를 주면 안 된다.
issuer-level product price pass-through, realized spread, margin bridge가 source-backed일 때만 primitive를 열어야 한다.
```

쉬운 예:

```text
"구리 가격 상승"
  -> 조사 트리거 또는 guard fixture
  -> 점수 0

"제품 판가 인상으로 원재료 상승에도 영업이익률 개선"
  -> C15 positive primitive 후보
```

### Patch 2. C17 / C24 / C28 replay parity - 다음

순서:

```text
1. C17: chemical spread -> realized margin/FCF bridge guard
2. C24: clinical endpoint/regulatory binary event guard
3. C28: ARR/RPO/renewal/retention bridge guard
```

각 패치마다 필요한 조건:

```text
source-backed positive fixture
source-backed guard fixture
wrong-subject/old/historical/future leakage 방지
score_contribution_count = 0 for replay-only
production_score_evidence_allowed = false
matrix count 반영
controlled_semantic_replay pending 감소
full test artifact 갱신
```

### Patch 3. Brain/Web production path 실제 실행

현재 Brain/Web은 disabled다.

운영형으로 인정하려면:

```text
llm_planner_call_count > 0
web_search_task_count > 0
web_fetched_document_count > 0
llm_claim_extractor_attempt_count > 0
web_or_llm_accepted_claim_count > 0
brain_to_claim_trace_count > 0
brain_score_contribution_count > 0
brain_stage_trace_count > 0
brain_promoted_stage_row_count > 0
```

하지만 무제한 fetch로 가면 안 된다.

운영 daily mode 조건:

```text
SourceTask별 max_queries / max_candidates / max_fetches / stop_condition 필요
official-first
general web fallback은 제한적으로만
provider failure는 낮은 점수 확정이 아니라 ProviderPending
```

### Patch 4. Full thesis production runner

현재:

```text
full_thesis_production_audit.status = PENDING_FULL_THESIS_PRODUCTION
production_full_thesis_row_count = 0
```

필요:

```text
1. CandidateEvent가 있는 종목만 full thesis refresh task 생성
2. archetype hypothesis를 evidence contract와 연결
3. source-backed claims -> primitive states -> score contributions -> StageCourt
4. `stage_scope=FULL_THESIS`, `score_scope=FULL_E2R_100`, `verified_score != null` row 생성
5. 모든 score delta는 claim delta로 설명
```

쉬운 예:

```text
삼성전자 풍문 해명 공시
  -> Census 상태판 event
  -> 이것만으로 C06 full thesis refresh를 완료하면 안 됨

SK하이닉스 HBM capacity/customer/revenue mix 관련 source-backed claims
  -> C06 full thesis refresh 후보
  -> required primitive coverage가 닫히면 FULL_THESIS row 가능
```

### Patch 5. OpenDART event archetype routing 정밀화

현재 non-Stage0 / scored rows가 C05로 과도하게 몰린다.

다음 검증이 필요하다:

```text
1. 단일판매계약/공급계약이면 C05 후보 가능
2. 유상증자/증권신고서면 capital_allocation_event일 수 있으나 C05 thesis로 고정하면 안 됨
3. 풍문/보도 해명은 information_confidence일 수 있으나 C05 EPC thesis로 고정하면 안 됨
4. primary_archetype=None 또는 event_type-specific pending 상태를 더 명확히 분리
```

목표:

```text
공식 이벤트는 조사 트리거가 될 수 있다.
하지만 아키타입 thesis는 source-backed primitive coverage가 있어야 열린다.
```

## 외부 리뷰어 공격 질문

다음 에이전트는 최소 이 질문을 공격해야 한다.

```text
1. Stage1/Stage2-Watch 85개가 실제 운영 Stage가 아니라는 것을 모든 report가 명확히 표시하는가?
2. 삼성전자/하이닉스 current row를 HBM/C06 thesis로 오해하게 만드는 출력이 남아 있는가?
3. EVENT_WEIGHTED_PARTIAL 67개가 FULL_E2R_100 점수처럼 섞이는 경로가 있는가?
4. accepted_claim 92개가 모두 OpenDART인데, LLM/Web evidence pass를 주장하는 문서가 남아 있는가?
5. C05 primary_archetype 과집중이 event-board용 임시 분류인지, production thesis routing 버그인지 구분되어 있는가?
6. C15 canonical output/test/docs가 모두 source-backed replay pass로 일치하는가?
7. all_archetype replay matrix가 C17/C24/C28 pending을 정확히 말하는가?
8. Brain/Web disabled run이 PRODUCTION_READY처럼 표시되는 경로가 있는가?
9. full_thesis_production_runner가 실제 source-backed Stage row를 만들기 전까지 goal_completion_ready가 false인가?
10. CENSUS_EVENT_BOARD Stage가 투자 판단용 Stage로 export되는 경로가 있는가?
11. 전역 accepted_claims와 대표 Stage row의 accepted_claim_ids 차이가 의도된 representative selection인지, 누락인지 설명되는가?
```

## 완료 기준

이 문서 기준으로 "다 됐다"고 말하려면 아래가 모두 참이어야 한다.

```text
1. FULL_THESIS row > 0
2. FULL_E2R_100 verified score row > 0
3. 삼성전자/하이닉스 smoke 또는 production full thesis가 source-backed claim으로 닫힘
4. Brain/Web evidence pass가 real planner/source/extractor/claim/score/stage trace로 닫힘
5. C06/C08/C15/C17/C24/C28 controlled semantic replay가 모두 source-backed pass
6. required archetype 32개 source-backed positive + guard replay parity pass
7. EVENT_WEIGHTED_PARTIAL과 FULL_E2R_100이 리포트/CSV/API에서 절대 섞이지 않음
8. provider failure/source gap은 낮은 점수 확정이 아니라 pending
9. 모든 nonzero score contribution에 accepted claim ID가 있음
10. 모든 score/stage delta가 claim delta로 설명됨
```

현재는 위 완료 기준 중 1~6이 아직 닫히지 않았다.

## 최종 판단

```text
지금 뭔가 잘못되고 있는 느낌은 맞다.
다만 "Stage가 아예 없다"가 아니라, "Stage라는 이름의 상태판은 있는데 운영 Stage가 아직 없다"가 정확하다.
```

가장 위험한 오해:

```text
Stage2-Watch 30개가 있으니 운영 Stage2가 생겼다.
```

정확한 말:

```text
Stage2-Watch 30개는 Census Event Board 상태판이다.
FULL_THESIS_NOT_RUN이고 verified_score도 없다.
운영 파이프라인으로 쓰려면 full thesis production runner와 Brain/Web evidence pass가 먼저 닫혀야 한다.
```

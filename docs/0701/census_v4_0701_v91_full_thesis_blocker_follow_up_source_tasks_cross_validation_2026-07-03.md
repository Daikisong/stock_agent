# Census v4 v91 - Full Thesis Blocker Follow-up Source Tasks Cross Validation

작성일: 2026-07-03

이 문서는 다음 에이전트가 `2026-07-01` Census v4 상태를 다시 공격적으로 검증할 때 먼저 읽어야 하는 v91 패치/검증 기록이다.

핵심 질문:

```text
Stage가 있는 애들이 있기는 한가?
있다면 그 Stage가 실제 운영 FULL_THESIS Stage인가?
막힌 FULL_THESIS 후보는 다음 Research Brain 루프로 이어지는가?
아니면 그냥 막힌 채로 끝나는가?
```

## 1. 결론

현재 최신 live truth인 v82 기준으로 Stage row는 있다.

하지만 운영자가 실제 투자 파이프라인의 full-thesis 판단처럼 써도 되는 `FULL_THESIS` Stage row는 아직 0개다.

```text
기준 output:
  output/census_v4/2026-07-01-real-brain-web-live-full-bounded-v82

census_stage_map.csv rows = 3391
canonical_stage != 0 rows = 85
stage_scope = CENSUS_EVENT_BOARD rows = 3390
stage_scope = BRAIN_WEB_PARTIAL rows = 1
stage_scope = FULL_THESIS rows = 0
score_scale = FULL_E2R_100 rows = 0
operator_stage_use = NOT_FULL_THESIS_STAGE rows = 3391
operator_score_use = NOT_FULL_E2R_SCORE rows = 3391
```

쉬운 예:

```text
CENSUS_EVENT_BOARD = 전교생 출석부에 "확인 필요" 표시
BRAIN_WEB_PARTIAL = 부분 쪽지시험 점수
FULL_THESIS = 정식 성적표

현재는 출석부 표시와 쪽지시험 1건은 있지만,
정식 성적표는 0장이다.
```

따라서 지금 "뭔가 잘못되고 있는 거 맞지?"의 정확한 답은:

```text
READY라고 말하면 잘못이다.
Stage 표시 자체는 있으나 운영 Stage는 없다.
다만 거짓 Green/Yellow를 막는 방향으로는 정상적으로 방어 중이다.
```

## 2. 현재 live v82 재검산

직접 재계산한 `census_stage_map.csv` 분포:

```text
row_count = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3390
  BRAIN_WEB_PARTIAL = 1

score_scale:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

canonical_stage:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

full_thesis_stage:
  FULL_THESIS_NOT_RUN = 3391
```

여기서 조심해야 할 점:

```text
canonical_stage 1/2/3-Red가 있어도
stage_scope가 FULL_THESIS가 아니면 운영 Stage가 아니다.
```

이 구분을 안 하면 예전처럼 `60점`, `90점`, `Yellow`, `4C` 같은 서로 다른 의미의 숫자와 Stage가 한 줄에서 섞인다.

## 3. 삼성전자 / SK하이닉스 상태

삼성전자:

```text
symbol = 005930
company_name = 삼성전자
canonical_stage = 1
stage_scope = CENSUS_EVENT_BOARD
score_scale = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.0
score_interval = 4.0 ~ 4.0
full_thesis_stage = FULL_THESIS_NOT_RUN
operator_stage_use = NOT_FULL_THESIS_STAGE
missing_primitives = repeat_evidence_family | cash_or_revision_conversion
failed_stage_gates = missing_green_bridge
accepted_claim_count = 1
score_contribution_count = 1
```

SK하이닉스:

```text
symbol = 000660
company_name = SK하이닉스
canonical_stage = 1
stage_scope = BRAIN_WEB_PARTIAL
score_scale = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 60.0
score_interval = 60.0 ~ 60.0
full_thesis_stage = FULL_THESIS_NOT_RUN
operator_stage_use = NOT_FULL_THESIS_STAGE
missing_primitives = hbm_capacity_constraint | hbm_capacity_pre_sold
failed_stage_gates = hbm_capacity_constraint | hbm_capacity_pre_sold
accepted_claim_count = 3
score_contribution_count = 6
```

중요:

```text
삼성전자 4.0은 FULL_E2R_100 점수가 아니다.
SK하이닉스 60.0도 FULL_E2R_100 점수가 아니다.
둘 다 EVENT_WEIGHTED_PARTIAL이다.
```

쉬운 예:

```text
SK하이닉스는 "HBM 관련 힌트가 있고 일부 claim도 있음"까지는 갔다.
하지만 "생산능력 자체가 병목인지"와 "그 생산능력이 pre-sold / sold-out인지"가
source-backed primitive로 닫히지 않았다.

그래서 Green은커녕 FULL_THESIS 승격 자체가 막힌다.
이건 낮게 후려친 게 아니라 과대평가를 막는 안전장치다.
```

## 4. FULL_THESIS production runner 상태

`full_thesis_production_runner_audit.json` 기준:

```text
verdict = PENDING_PRODUCTION_FULL_THESIS
production_mode_requested = true
full_thesis_refresh_queue_candidate_count = 84
candidate_row_count = 1
candidate_source_counts = {"brain_web_partial_stage_row": 1}
promoted_full_thesis_row_count = 0
blocked_candidate_count = 1
```

차단 후보:

```text
symbol = 000660
primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
candidate_source = brain_web_partial_stage_row
present_primitives:
  customer_preorder_or_allocation
  medium_term_revision_visibility
  revenue_visibility_contract

missing_green_primitives:
  hbm_capacity_constraint
  hbm_capacity_pre_sold

blockers:
  missing_green_gate_primitives
```

해석:

```text
현재 하이닉스는 "고객 배정/매출 가시성/리비전" 일부는 잡혔다.
하지만 C06 Green gate의 핵심인 capacity 병목과 pre-sold capacity가 닫히지 않았다.
```

여기서 절대 하면 안 되는 패치:

```text
customer_preorder_or_allocation이 있으니 hbm_capacity_pre_sold도 있다고 간주
```

이렇게 하면 다시 "그럴듯한 HBM 기사 하나를 Green 재료로 과대해석"하는 문제가 생긴다.

## 5. v91 패치 내용

v91 패치는 점수나 Stage를 올리지 않는다.

하는 일은 하나다.

```text
FULL_THESIS 승격 후보가 Green primitive 부족으로 막힘
-> 막힌 primitive별로 bounded official-first SourceTask shell 생성
-> query text는 코드가 만들지 않음
-> 다음 Research Brain LLM planner가 실제 query를 생성해야 함
```

수정된 주요 함수:

```text
src/e2r/census/census_runner_v4.py

_apply_production_full_thesis_from_brain
  - blocked candidate에서 follow-up source task를 생성해 audit에 연결

_full_thesis_blocker_follow_up_source_tasks
  - 새 helper
  - missing Green primitive마다 task shell 생성

_source_connector_requirement_rows
  - full_thesis_blocker_follow_up_source_tasks.jsonl도 source capability audit 입력으로 읽음

_write_operational_docs
  - docs/operational/census_mode_v4_full_thesis_blocker_follow_up_source_tasks.jsonl export 추가
```

새 산출물:

```text
full_thesis_blocker_follow_up_source_tasks.jsonl
```

`full_thesis_production_runner_audit.json`에 새로 남는 필드:

```text
blocked_candidate_follow_up_source_task_path
blocked_candidate_follow_up_source_task_count
blocked_candidate_follow_up_primitive_gaps
blocked_candidate_follow_up_rule
```

주의:

```text
이 산출물은 "점수 재료"가 아니다.
이 산출물은 "다음 조사를 열어 주는 계획 장부"다.
```

## 6. follow-up task 안전장치

각 follow-up task는 다음 속성을 가져야 한다.

```text
source_task_origin = full_thesis_green_gate_blocker_follow_up
task_type = green_closure
task_status = PLANNING_REQUIRED
planner_required = true
llm_query_required = true
llm_query_allowed = true
general_search_allowed = false
official_first_required = true

hardcoded_query_count = 0
hardcoded_queries = []
query_intents = []

preferred_source_classes:
  DART
  KIND
  KRX
  IssuerIR
  CompanyGuide

fallback_source_classes:
  TrustedNews
  ReportPDF
  BrokerReportPublicPDF
  CompanyNewsroom
  NaverSearch
  GeneralWebSearch

forbidden_source_classes:
  snippet_only_score
  source_proxy_only
  evidence_url_pending
  unbounded_general_search

max_queries = 3
max_candidates = 20
max_fetches = 3
score_allowed_before_execution = false
stage_promotion_allowed_before_execution = false
```

쉬운 예:

```text
나쁜 방식:
  코드가 "SK하이닉스 HBM sold out capacity" 같은 검색어를 직접 만든다.

v91 방식:
  코드가 "hbm_capacity_pre_sold가 비었다"까지만 적는다.
  그 다음 어떤 검색어가 맞는지는 LLM planner가 현재 evidence와 gap context를 보고 만든다.
  deterministic code는 query 검증, fetch, anchor/claim 검증, scoring만 한다.
```

## 7. source capability audit 연결

follow-up task 파일을 만들기만 하면 부족하다.

다음 감사도 이 task를 봐야 한다.

```text
_source_connector_requirement_rows
```

v91은 새 파일을 여기에 연결했다.

검증 포인트:

```text
full_thesis_blocker_follow_up_source_tasks.jsonl
-> source_connector_capability_audit의 full_thesis_requirement로 들어감
-> IssuerIR / TrustedNews placeholder는 blocking source class로 잡힘
-> 하지만 같은 task에 DART / KIND / KRX / bounded web/report path가 있으므로
   blocking_full_thesis_task_count는 0이어야 함
```

쉽게 말하면:

```text
차량에 아직 고장난 길이 하나 있어도,
다른 실제로 달릴 수 있는 길이 있으면 "완전 통행 불가"는 아니다.

다만 고장난 길이 있다는 사실은 계속 감사 장부에 남아야 한다.
```

## 8. 교차검증 결과

정적/단위 검증:

```text
PYTHONPATH=src python -m py_compile src/e2r/census/census_runner_v4.py
  PASS

PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_stage_promotion_gate.CensusV4BrainStagePromotionGateTests.test_brain_partial_stage_is_not_production_full_thesis_without_green_gate_coverage -v
  Ran 1 test
  OK

PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_artifact_manifest -v
  Ran 32 tests
  OK

PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v
  Ran 139 tests
  OK

PYTHONPATH=src python -m unittest discover -s tests -v
  Ran 5122 tests in 232.148s
  OK
```

새 테스트가 고정하는 내용:

```text
1. Green primitive 부족이면 FULL_THESIS로 승격하지 않는다.
2. blocked candidate에서 follow-up source task를 만든다.
3. follow-up task에는 hardcoded query가 없다.
4. follow-up task는 bounded budget을 가진다.
5. score_allowed_before_execution=false다.
6. stage_promotion_allowed_before_execution=false다.
7. source connector capability audit이 새 task id를 full-thesis requirement로 본다.
8. IssuerIR/TrustedNews placeholder를 기록하되, task 전체를 완전 blocking으로 오인하지 않는다.
```

## 9. 아직 통과하지 못한 것

v91은 READY 패치가 아니다.

아직 남은 큰 blocker:

```text
1. v82 live output은 v91 이후 재실행되지 않았다.
2. FULL_THESIS production row는 여전히 0개다.
3. FULL_E2R_100 verified score row도 0개다.
4. Brain/Web readiness gate는 아직 BLOCKED다.
5. all-archetype source-backed replay는 6/32만 ready다.
6. follow-up source task가 실제 Research Brain planner에 소비되어 query/fetch/claim/stagecourt까지 닫히는지는 다음 패치가 필요하다.
```

Brain/Web readiness blocker:

```text
planner runs not met: 21/30
web search tasks not met: 3/20
web/news search calls not met: 3/20
fetched documents not met: 1/10
claim extractor attempts not met: 1/10
```

all-archetype replay:

```text
required archetypes = 32
source-backed ready = 6
missing required archetypes = 26
```

이 뜻:

```text
현재는 C06 같은 일부 아키타입의 replay/guard는 있다.
하지만 "전체 아키타입에서 과거 연구만큼 점수 결과가 재현된다"는 목표에는 아직 멀다.
```

## 10. 다음 에이전트 공격 포인트

다음 에이전트는 아래를 먼저 찔러야 한다.

```text
1. full_thesis_blocker_follow_up_source_tasks.jsonl이 live rerun에서 실제 생성되는가?
2. 그 task가 Research Brain planner 입력으로 실제 소비되는가?
3. LLM planner가 primitive_gap별 query를 만들고, deterministic code가 query를 검증하는가?
4. query가 빈 값이거나 중복이면 다시 LLM에 gap context를 돌려보내는가?
5. source task execution이 accepted_claim_id, evidence_document_id, evidence_anchor_id와 닫히는가?
6. 새 claim이 기존 ledger를 덮어쓰지 않고 append-only로 추가되는가?
7. 해당 primitive만 재평가되고 전체 LLM field가 매번 갈아끼워지지 않는가?
8. FULL_THESIS 승격 전 source_linkage_proof와 score_interval lower/upper가 모두 닫히는가?
9. C06에서 customer allocation을 capacity pre-sold로 뭉개지 않는가?
10. 무제한 web fetch나 deterministic hardcoded query가 다시 생기지 않는가?
```

반드시 실패로 봐야 하는 경우:

```text
follow-up task가 생겼다는 이유만으로 score/stage가 올라감
query_intents에 코드가 만든 검색어가 들어감
source_proxy_only 또는 snippet-only가 score evidence로 들어감
missing Green primitive가 present로 자동 변환됨
stage_scope가 FULL_THESIS인데 full_e2r_verified_score가 없음
operator_stage_use가 FULL_THESIS_STAGE인데 source_linkage_proof가 비어 있음
```

## 11. 다음 패치 방향

v91 다음의 올바른 패치 순서:

```text
P1. live/prod run에서 full_thesis_blocker_follow_up_source_tasks.jsonl 생성 확인
P2. Research Brain planner가 이 task를 입력으로 받아 primitive_gap 중심 query를 생성
P3. deterministic code는 query 검증/중복 제거/as_of_date 검증만 수행
P4. bounded official-first source task 실행
P5. Evidence OS가 document -> anchor -> claim -> primitive -> score contribution을 append-only로 기록
P6. 영향받은 primitive만 StageCourt에 재투입
P7. FULL_THESIS promotion gate 재평가
P8. v82 이후 live rerun 산출물로 README 최신 truth 갱신
```

여기서도 금지:

```text
점수 산식 변경
Green gate 완화
종목명 예외 처리
검색어 deterministic template 추가
C06 전용 if 분기 추가
```

필요한 것은:

```text
막힌 gap을 LLM planner에게 정확히 넘기는 운영 장부
그 장부가 실제 source task execution으로 이어지는 폐루프
```

## 12. 최종 판단

v91은 운영 READY가 아니다.

하지만 v90에서 확인된 가장 큰 구조적 dead-end 하나를 줄였다.

```text
v90 문제:
  SK하이닉스 Brain/Web partial 후보가 FULL_THESIS로 못 올라감
  이유는 missing Green primitive
  그런데 이 blocker가 다음 source task로 명시적으로 materialize되지 않음

v91 개선:
  blocker를 그대로 유지
  점수/Stage는 올리지 않음
  missing primitive마다 bounded official-first follow-up task shell 생성
  hardcoded query는 0개
  source capability audit이 새 task를 봄
```

쉬운 한 줄 요약:

```text
지금까지는 "서류 두 장이 빠져서 합격 못 함"까지만 적었다.
v91은 "빠진 서류 두 장을 어디서, 어떤 제한 안에서, LLM에게 물어 찾아야 하는지"까지 장부에 남긴다.
하지만 서류가 실제로 제출된 것은 아직 아니다.
```

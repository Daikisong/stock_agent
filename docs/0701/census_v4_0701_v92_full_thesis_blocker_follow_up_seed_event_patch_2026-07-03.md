# Census v4 v92 - FULL_THESIS Blocker Follow-up Seed Event Patch / Cross Validation

작성일: 2026-07-03

이 문서는 다음 에이전트가 `2026-07-01` Census v4를 공격적으로 검증할 때 v91 이후 가장 먼저 읽어야 하는 기록이다.

핵심 질문은 하나다.

```text
FULL_THESIS 승격이 막힌 후보의 missing primitive가
다음 Research Brain 조사 입력으로 실제 전달되는가?
```

## 1. 최종 결론

v82 live output 기준으로 Stage row는 있다. 하지만 운영에서 써도 되는 `FULL_THESIS` Stage는 아직 없다.

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
CENSUS_EVENT_BOARD = 출석부에 "확인 필요" 표시
BRAIN_WEB_PARTIAL = 일부 문제만 푼 쪽지시험
FULL_THESIS = 채점 근거가 모두 붙은 정식 성적표

현재는 출석부 표시와 쪽지시험 1건은 있다.
하지만 정식 성적표는 0장이다.
```

따라서 지금 상태를 `Stage가 아예 없다`고 말하면 부정확하고, `운영 Stage가 있다`고 말하면 더 위험하다.

정확한 표현:

```text
상태판/부분 Stage는 있다.
운영 FULL_THESIS Stage는 없다.
```

## 2. v91에서 남아 있던 단절

v91은 `FULL_THESIS` 승격 후보가 Green primitive 부족으로 막히면 primitive별 `SourceTask shell`을 만들었다.

예를 들어 SK하이닉스가 C06 후보로 일부 claim을 갖고 있지만 아래가 부족했다.

```text
missing_green_primitives:
  hbm_capacity_constraint
  hbm_capacity_pre_sold
```

v91은 이 부족분을 다음처럼 작업표로 남겼다.

```text
task_status = PLANNING_REQUIRED
llm_query_required = true
official_first_required = true
general_search_allowed = false
max_queries = 3
max_candidates = 20
max_fetches = 3
query_intents = []
hardcoded_query_count = 0
```

하지만 단절이 있었다.

```text
막힌 primitive -> SourceTask shell 생성
여기까지는 됨.

SourceTask shell -> 다음 Research Brain candidate_event_seed_path 입력
이 연결은 없음.
```

쉬운 예:

```text
선생님이 "이 문제 다시 풀어와"라고 작업표는 써 줬는데,
그 작업표가 다음 시험지에 붙지 않은 상태였다.
```

그래서 v91만으로는 “다음 Brain이 알아서 이어서 조사한다”고 말하면 안 됐다.

## 3. v92 패치 내용

v92는 점수나 Stage를 올리지 않는다. Green gate를 느슨하게 만들지도 않는다.

하는 일은 하나다.

```text
blocked FULL_THESIS candidate
-> missing Green primitive별 bounded SourceTask shell
-> matching planner-input-only seed event
-> Research Brain planner context에서 primitive gap 확인 가능
```

수정된 파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/research_brain/v4_production_orchestrator.py
tests/test_census_v4_brain_stage_promotion_gate.py
tests/test_research_brain_v4_operational_modes.py
docs/0701/README.md
```

새 산출물:

```text
full_thesis_blocker_follow_up_seed_events.jsonl
docs/operational/census_mode_v4_full_thesis_blocker_follow_up_seed_events.jsonl
```

감사 필드:

```text
blocked_candidate_follow_up_seed_event_path
blocked_candidate_follow_up_seed_event_count
```

## 4. seed event 구조

seed event는 Research Brain의 `candidate_event_seed_path`로 읽을 수 있게 만든다.

예시:

```json
{
  "source_family": "CensusFullThesisBlockerFollowUp",
  "event_type": "full_thesis_blocker_follow_up_seed",
  "research_brain_eligible": true,
  "score_evidence_allowed": false,
  "stage_promotion_allowed_before_execution": false,
  "seed_role": "planner_input_only",
  "structured_payload": {
    "seed_role": "planner_input_only",
    "follow_up_task_id": "FTGAP-...",
    "follow_up_origin": "full_thesis_green_gate_blocker_follow_up",
    "follow_up_primitive_gap": "hbm_capacity_pre_sold",
    "follow_up_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "preferred_source_classes": ["DART", "KIND", "KRX", "IssuerIR", "CompanyGuide"],
    "fallback_source_classes": ["TrustedNews", "ReportPDF", "BrokerReportPublicPDF", "CompanyNewsroom", "NaverSearch", "GeneralWebSearch"],
    "official_first_required": true,
    "llm_query_required": true,
    "hardcoded_query_count": 0,
    "query_intents": [],
    "max_queries": 3,
    "max_candidates": 20,
    "max_fetches": 3
  }
}
```

중요한 점:

```text
top-level에는 감사용 score_evidence_allowed=false,
stage_promotion_allowed_before_execution=false가 있다.

하지만 Brain planner가 보는 structured_payload에는
score/stage/current_score_eligible 키가 없다.
```

왜 이렇게 했는가:

```text
LLM에게 "이 종목을 Green으로 올려라"를 주면 편향된다.
LLM에게 "이 primitive가 비었으니 공식자료 우선으로 어떤 source task/query가 필요한지 판단하라"만 줘야 한다.
```

## 5. Research Brain context 연결

`src/e2r/research_brain/v4_production_orchestrator.py`의 `_full_thesis_queue_context_from_structured_payload`가 follow-up seed context를 노출하도록 확장됐다.

노출되는 안전 context:

```text
follow_up_task_id
follow_up_origin
follow_up_primitive_gap
follow_up_archetype_id
present_primitives
missing_green_primitives
preferred_source_classes
fallback_source_classes
forbidden_source_classes
official_first_required
llm_query_required
llm_query_allowed
general_search_allowed
hardcoded_query_count
hardcoded_queries
query_intents
date_window
max_queries
max_candidates
max_fetches
max_queries_per_task
max_candidates_per_query
max_fetches_per_task
stop_condition
```

노출하지 않는 것:

```text
score_evidence_allowed
stage_promotion_allowed_before_execution
source_score_contribution_ids
source_stage_signal
source_stage_decision_status
current_score_eligible
```

쉬운 예:

```text
좋은 입력:
  "hbm_capacity_pre_sold가 비어 있다. 공식자료 우선으로 bounded source task를 계획하라."

나쁜 입력:
  "현재 60점이고 Green에 10점 부족하다. hbm_capacity_pre_sold를 찾아서 Stage를 올려라."
```

v92는 좋은 입력만 Research Brain context로 넘기게 한다.

## 6. 이번 패치가 일부러 하지 않은 것

v92는 아래를 하지 않는다.

```text
FULL_THESIS Stage 승격
FULL_E2R_100 점수 생성
C06 Green gate 완화
missing primitive를 다른 primitive로 대체 인정
query text 하드코딩
같은 run 안에서 자동 재조사 루프 실행
```

이유:

```text
같은 run 안에서 blocker 발견 -> seed 생성 -> Brain 재실행 -> Stage 재판정까지 자동으로 섞으면
예전 90점 -> 63점 문제처럼 서로 다른 입력 조건을 한 결과처럼 착각할 위험이 커진다.
```

따라서 v92는 다음-run seed를 명시적으로 남기는 선에서 끊는다.

다음 에이전트가 해야 할 일:

```text
1. full_thesis_blocker_follow_up_seed_events.jsonl을 candidate_event_seed_path로 Brain에 투입
2. LLM planner가 query_intents/source_tasks를 생성하는지 확인
3. bounded official-first source acquisition이 실제 문서를 fetch하는지 확인
4. Evidence OS accepted_claim이 missing primitive를 닫는지 확인
5. StageCourt를 다시 실행해 FULL_THESIS 승격 여부를 판단
```

## 7. 현재 SK하이닉스 예시 해석

현재 v82 live truth:

```text
SK하이닉스:
  stage_scope = BRAIN_WEB_PARTIAL
  score_scale = EVENT_WEIGHTED_PARTIAL
  event_evidence_score = 60.0
  full_thesis_stage = FULL_THESIS_NOT_RUN
  operator_stage_use = NOT_FULL_THESIS_STAGE
```

이것을 이렇게 읽으면 안 된다.

```text
SK하이닉스 운영 점수는 60점이다.
SK하이닉스 운영 Stage는 Stage1이다.
```

정확한 해석:

```text
SK하이닉스는 일부 source-backed claim이 있어 부분 평가까지는 갔다.
하지만 C06 Green gate의 capacity constraint / pre-sold capacity primitive가 닫히지 않아 FULL_THESIS 승격은 막혔다.
v92는 그 두 빈칸을 다음 Brain planner가 조사할 수 있게 seed로 넘긴다.
```

## 8. 테스트 및 검증

실행한 검증:

```text
PYTHONPATH=src python -m py_compile \
  src/e2r/census/census_runner_v4.py \
  src/e2r/research_brain/v4_production_orchestrator.py

PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_stage_promotion_gate.CensusV4BrainStagePromotionGateTests.test_brain_partial_stage_is_not_production_full_thesis_without_green_gate_coverage \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_full_thesis_blocker_follow_up_seed_context_is_visible_without_score_stage_context \
  -v

PYTHONPATH=src python -m unittest tests.test_census_v4_brain_stage_promotion_gate -v
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
focused 2 tests: OK
test_census_v4_brain_stage_promotion_gate: 16 tests OK
test_research_brain_v4_operational_modes: 63 tests OK
test_census_v4*.py sequential: 139 tests OK
full unittest suite: 5123 tests OK, 229.687s
```

주의:

```text
test_census_v4*.py와 일부 묶음 테스트를 병렬로 돌리면
tests/census_v4_test_helpers.py의 output/test_census_v4_cached 공유 산출물에 동시에 쓰면서
manifest hash mismatch 또는 JSONL decode error가 날 수 있다.

이건 v92 기능 실패가 아니라 테스트 캐시 race다.
검증은 순차 실행으로 해야 한다.
```

실제로 병렬 실행 중 아래 증상이 한 번 나왔다.

```text
manifest sha256 mismatch
census_events.jsonl JSONDecodeError
```

그 뒤 `output/test_census_v4_cached`를 지우고 순차 재실행하자:

```text
test_census_v4*.py = 139 tests OK
full suite = 5123 tests OK
```

## 9. 외부 리뷰어 공격 포인트

다음 에이전트는 아래를 반드시 공격적으로 봐야 한다.

### 9.1 이 seed가 실제 live run에서 생기는가

v92는 테스트 fixture에서 4개 seed 생성을 검증했다. 하지만 v82 live output은 v92 코드로 재실행된 산출물이 아니다.

확인해야 할 것:

```text
v92 코드로 2026-07-01 live bounded run 재실행
full_thesis_blocker_follow_up_seed_events.jsonl 생성 여부
blocked_candidate_follow_up_seed_event_count > 0 여부
```

### 9.2 seed가 Brain planner를 실제로 움직이는가

v92는 seed event를 만들고 Brain context로 열 수 있게 했다.

아직 검증되지 않은 것:

```text
candidate_event_seed_path=full_thesis_blocker_follow_up_seed_events.jsonl
-> planner_runs.jsonl 생성
-> planner output에 새 source_tasks/query_intents 생성
-> source acquisition 실행
-> accepted_claim이 missing primitive를 닫음
```

### 9.3 query 하드코딩이 숨어 있지 않은가

v92 seed는 `hardcoded_query_count=0`, `query_intents=[]`로 시작한다.

다음 run에서 확인할 것:

```text
query text가 코드 템플릿이 아니라 LLM planner output에서 왔는가
query validator가 as_of_date/entity/source budget을 검증했는가
```

### 9.4 official-first가 실제로 지켜지는가

seed에는:

```text
preferred_source_classes = DART, KIND, KRX, IssuerIR, CompanyGuide
fallback_source_classes = TrustedNews, ReportPDF, BrokerReportPublicPDF, CompanyNewsroom, NaverSearch, GeneralWebSearch
general_search_allowed = false
```

하지만 다음 run에서 LLM planner가 일반 웹만 제안하면 정책 위반이다.

확인할 것:

```text
official/source classes first
bounded max_queries/max_candidates/max_fetches
stop-on-resolution
snippet-only no score
```

### 9.5 FULL_THESIS 승격이 너무 쉽게 되지 않는가

missing primitive 하나가 닫혔다고 바로 FULL_THESIS가 되면 안 된다.

FULL_THESIS 승격에는 계속 아래가 필요하다.

```text
direct/current accepted_claim_ids
score_contribution_ids
primitive_state_ids
score_interval lower/upper
score_status FINAL or FINAL_WITH_NONMATERIAL_GAPS
source linkage proof
contract Green gate primitive coverage
```

## 10. 아직 NOT_READY인 이유

v92 이후에도 production ready가 아니다.

남은 blockers:

```text
v82 live truth에는 FULL_THESIS rows = 0
Brain/Web evidence gate는 아직 live minimum을 못 채움
all-archetype replay는 required 32 중 ready 6, missing 26
follow-up seed는 만들어졌지만 live rerun에서 실제 source/claim closure까지 아직 검증 안 됨
```

즉:

```text
v92는 배관을 한 칸 연결한 패치다.
운영 파이프라인 완성 선언이 아니다.
```

## 11. 다음 패치 방향

우선순위:

```text
1. v92 code로 live bounded run 재실행
2. full_thesis_blocker_follow_up_seed_events.jsonl이 live output에 생기는지 확인
3. 별도 Brain run 또는 다음 Census run에서 candidate_event_seed_path로 follow-up seed 투입
4. planner가 score/stage 없는 context로 bounded source task를 생성하는지 확인
5. SourceAcquisitionRunnerV4가 official-first/fallback 정책대로 fetch하는지 확인
6. Evidence OS accepted_claim -> primitive_state -> score_contribution -> StageCourt 경로가 닫히는지 확인
7. 그래도 FULL_THESIS rows가 0이면, 어느 단계에서 끊기는지 leaf artifact로 다시 분해
```

특히 1번과 3번을 섞어 말하면 안 된다.

쉬운 예:

```text
1번 = 다음 시험지를 만들 수 있는 보충문제 목록이 생기는지 확인
3번 = 그 보충문제를 실제로 풀게 해서 답안이 생기는지 확인
```

v92는 1번을 가능하게 하는 패치이고, 3~6번은 다음 검증 대상이다.

## 12. 한 줄 요약

```text
현재 stage 표시 자체는 있지만 운영 FULL_THESIS Stage는 0개다.
v91은 막힌 primitive의 SourceTask shell만 만들었다.
v92는 그 shell을 다음 Research Brain planner가 읽을 수 있는 score/stage-blind seed event로 연결했다.
하지만 live source fetch와 claim closure를 아직 검증하지 않았으므로 production ready는 아니다.
```

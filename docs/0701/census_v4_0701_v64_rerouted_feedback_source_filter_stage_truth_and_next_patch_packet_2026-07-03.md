# Census v4 0701 v64 Rerouted Feedback Source Filter, Stage Truth, And Next Patch Packet

작성일: 2026-07-03 KST

## 결론

이번 v64 확인의 결론은 다음이다.

```text
1. 상태판 Stage는 있다.
2. 운영 Full Thesis Stage는 아직 0개다.
3. v64는 "다른 primitive로 reroute된 CompanyGuide claim을 같은 C06 빈칸에 계속 재사용하는 문제"를 줄였다.
4. 하지만 Full Thesis 운영 파이프라인은 아직 NOT_READY / BLOCKED다.
```

쉬운 예:

```text
CompanyGuide 컨센서스 표는 "실적 전망이 있다"는 영수증이다.
그 영수증을 들고 "HBM 물량 배정도 됐다", "CAPA도 sold-out이다",
"FCF 전환도 확인됐다"고 말하면 안 된다.

v64는 이 영수증을 여러 C06 빈칸에 계속 다시 넣는 반복을 막기 시작했다.
하지만 HBM 고객 배정, 품질통과, 매출비중, 현금흐름 영수증은 아직 못 찾았다.
```

따라서 현재 상태를 한 문장으로 쓰면:

```text
CENSUS_EVENT_BOARD 상태표는 존재하지만, operator가 사용할 수 있는 FULL_THESIS / FULL_E2R_100 Stage는 아직 생성되지 않았다.
```

## 이번 패치가 겨냥한 문제

v61까지 고친 것은 claim dedupe였다.

```text
같은 CompanyGuide 컨센서스 문서
-> 여러 SourceTask
-> 여러 anchor/claim으로 증식
```

v61 이후에도 남은 문제는 더 운영적인 것이었다.

```text
SourceTask의 원래 요청:
  hbm_capacity_pre_sold
  cash_or_revision_conversion
  revenue_visibility_contract

CompanyGuide에서 실제 accepted된 claim:
  medium_term_revision_visibility

문제:
  원래 C06 gap은 그대로 UNKNOWN인데,
  retry가 다시 CompanyGuide를 가져오고,
  같은 medium_term_revision_visibility claim이 다시 accepted된다.
```

즉 dedupe만으로는 부족했다. 같은 claim ID가 유지돼도, 같은 출처가 원래 gap을 못 닫는다는 사실을 planner feedback과 source-task validation에 넣어야 했다.

## 패치 요약

### 1. rerouted claim feedback을 planner context에 추가

변경 파일:

```text
src/e2r/research_brain/v4_schemas.py
src/e2r/research_brain/v4_production_orchestrator.py
src/e2r/research_brain/v4_planner_runtime.py
```

핵심 추가:

```text
PlannerRunV4.rerouted_claim_feedback_count
existing_evidence_summary.rerouted_claim_feedback
_rerouted_claim_feedback_from_bundle(...)
_retry_planner_for_rerouted_claim_feedback(...)
```

중요한 안전장치:

```text
rerouted feedback에는 score, stage, current_score_eligible를 넣지 않는다.
LLM에게 "점수 올려라"가 아니라 "이전 claim은 다른 primitive로 accepted됐고 원래 gap은 아직 비었다"만 알려준다.
```

쉬운 예:

```text
나쁜 피드백:
  "하이닉스가 Green 되려면 hbm_capacity_pre_sold 8점이 필요하다."

v64 피드백:
  "이전 CompanyGuide claim은 medium_term_revision_visibility로 accepted됐다.
   요청했던 hbm_capacity_pre_sold는 아직 unsatisfied다.
   같은 source/document를 반복하지 말고 다른 bounded source task를 계획하라."
```

### 2. rerouted-only source class를 retry task에서 제거

변경 파일:

```text
src/e2r/research_brain/v4_production_orchestrator.py
```

핵심 추가:

```text
_rerouted_blocked_sources_by_primitive(...)
_remove_rerouted_only_sources_from_retry_task(...)
_rerouted_source_retry_drop_execution(...)
```

의미:

```text
어떤 source class가 특정 primitive gap을 요청받았는데
그 gap을 직접 닫지 못하고 다른 primitive claim만 만들었다면,
동일 unsatisfied primitive의 retry에서 그 source class를 제거한다.

제거 후 남은 source class가 없으면 조용히 사라지지 않고
REJECTED_BY_POLICY source_task_execution row를 남긴다.
```

쉬운 예:

```text
요청: hbm_capacity_pre_sold
출처: CompanyGuide
결과: medium_term_revision_visibility만 accepted

다음 retry에서:
  hbm_capacity_pre_sold를 다시 찾는데 CompanyGuide만 들고 오면 drop
  IR / 회사 공시 / 고객사 공식자료 / 원문 뉴스 등 다른 source class면 실행 가능
```

이것은 종목명이나 아키타입명을 하드코딩한 것이 아니라, 이전 실행 결과의 `requested_primitive_gap`, `accepted_primitive_ids`, `primitive_gap_unsatisfied_ids`, `source_class`를 보고 검증하는 source admissibility 정책이다.

### 3. prompt rule 추가

변경 파일:

```text
src/e2r/research_brain/v4_planner_runtime.py
```

추가 규칙 요지:

```text
existing_evidence_summary.rerouted_claim_feedback이 있으면
이전 accepted claim은 다른 primitive용이었다.
원래 primitive_gap은 아직 unsatisfied다.
같은 source class/document 반복을 피하고 다른 bounded source_task/query를 계획하라.
score, stage, verified final, current_score_eligible, accepted claim final은 출력하지 마라.
```

## 테스트

### targeted operational mode tests

명령:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
```

결과:

```text
Ran 58 tests in 3.482s
OK
```

추가된 핵심 테스트:

```text
test_rerouted_claim_feedback_is_added_to_evidence_context
test_rerouted_claim_feedback_rows_are_gap_level_not_score_context
test_rerouted_claim_feedback_retries_planner_once
test_direct_source_task_acceptance_blocks_rerouted_claim_feedback_retry
test_rerouted_claim_feedback_is_visible_to_planner_prompt_payload
test_rerouted_feedback_retry_removes_source_that_only_produced_other_primitive
test_rerouted_feedback_retry_drop_is_auditable_when_only_same_source_remains
```

### extended targeted tests

명령:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_full_thesis_smoke_tasks -v
```

결과:

```text
Ran 135 tests in 34.096s
OK
```

### full suite

명령:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5092 tests in 211.923s
OK
```

주의:

```text
이 테스트 통과는 코드 회귀가 없다는 증거다.
운영 readiness 통과 증거는 아니다.

v64 real smoke는 여전히 NOT_READY / BLOCKED이고,
FULL_THESIS rows = 0,
FULL_E2R_100 rows = 0,
llm_claim_extractor_attempt_count = 0,
web_fetched_document_count = 0이다.
```

## Real Planner Smoke

실행 명령:

```bash
rm -rf output/census_v4/2026-07-01-real-planner-rerouted-source-filter-v64
E2R_CODEX_PLANNER_TIMEOUT_SECONDS=120 PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-real-planner-rerouted-source-filter-v64 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_TRIAGE_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_official_first \
  --brain-universe-limit 1 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-source-tasks-per-plan 3 \
  --brain-max-fetches-per-task 1 \
  --brain-stage-promotion-mode strict \
  --target-gate anti_fake \
  --write-operational-docs false \
  --fail-on-critical-audit false \
  --test-result-artifact output/census_v4/2026-07-01/full_unittest_result_artifact.json
```

결과:

```text
exit code = 1
verdict = BLOCKED / NOT_READY
```

핵심 감사 파일:

```text
output/census_v4/2026-07-01-real-planner-rerouted-source-filter-v64/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01-real-planner-rerouted-source-filter-v64/brain_stage_promotion_audit.json
output/census_v4/2026-07-01-real-planner-rerouted-source-filter-v64/census_stage_summary.json
output/census_v4/2026-07-01-real-planner-rerouted-source-filter-v64/source_task_executions.jsonl
```

## v64 Real Smoke 핵심 숫자

`brain_web_readiness_gate_audit.json`:

```text
verdict = BLOCKED
blockers:
  - Brain/Web StageCourt traces are not promoted into census_stage_status
  - brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED

llm_planner_call_count = 22
llm_real_provider_success_count = 2
source_task_execution_count = 12
real_document_fetched_count = 4

full_thesis_seed_event_count = 85
full_thesis_seed_planner_attempted_event_count = 21
full_thesis_seed_planner_run_count = 21
full_thesis_seed_accepted_claim_count = 2

official_accepted_claim_count = 1
direct_accepted_claim_count = 1
direct_source_task_satisfied_count = 1
rerouted_source_task_claim_count = 1
policy_rejected_source_task_execution_count = 1

brain_score_contribution_count = 2
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 0

full_thesis_claim_count = 0
llm_claim_extractor_attempt_count = 0
web_fetched_document_count = 0
web_search_call_count = 0
```

해석:

```text
real planner와 official source task는 실제로 움직였다.
하지만 LLM claim extractor live path와 web acquisition은 이번 smoke에서 0회다.
Full Thesis claim도 0개다.
따라서 Stage 승격이 막힌 것은 정상이다.
```

## Stage Truth

`census_stage_status.jsonl` 재집계:

```text
rows = 3391

stage:
  None = 3391

base_stage:
  Stage0       = 3306
  Stage1       = 54
  Stage2-Watch = 30
  Red          = 1

stage_scope:
  CENSUS_EVENT_BOARD = 3391

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

score_scale:
  NO_SCORE               = 3324
  EVENT_WEIGHTED_PARTIAL = 67
```

`census_stage_summary.json`:

```text
event_board_stage_row_count = 3391
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
verified_score_present_count = 0
operator_stage_scope_notice = NO_FULL_THESIS_STAGE_ROWS_EVENT_BOARD_STAGE_ROWS_EXIST
full_thesis_stage_distribution = FULL_THESIS_NOT_RUN 3391
```

정확한 문장:

```text
Stage0/Stage1/Stage2-Watch/Red 같은 base_stage는 있다.
하지만 census_stage_status.stage는 전부 None이고,
operator_stage_use는 전부 NOT_FULL_THESIS_STAGE다.
```

쉬운 예:

```text
base_stage = 접수창구에서 붙인 상태 스티커
stage      = 심사 끝난 공식 등급

현재는 상태 스티커는 붙었지만 공식 등급은 비어 있다.
```

## 000660 Full Thesis Seed 비교

대상:

```text
symbol = 000660
candidate_event_id = CEV4-FTQUEUE-000660-9563b2a7a852fc0c
```

### v61

```text
path = output/census_v4/2026-07-01-real-planner-companyguide-dedupe-v61

Full Thesis seed rows = 11
status:
  EVIDENCE_OS_ACCEPTED = 4
  NO_EVIDENCE_FOUND    = 6
  PROVIDER_FAILED      = 1

satisfaction:
  REROUTED_ACCEPTED_CLAIM = 4
  NO_EVIDENCE_FOUND       = 7

source:
  CompanyGuide = 4
  DART         = 4
  KIND         = 1
  KRX          = 1
  IR           = 1

accepted refs = 4
unique refs   = 1
accepted primitive = medium_term_revision_visibility only
direct accepted claim = 0
```

### v63

```text
path = output/census_v4/2026-07-01-real-planner-rerouted-feedback-v63

Full Thesis seed rows = 11
status:
  EVIDENCE_OS_ACCEPTED = 5
  NO_EVIDENCE_FOUND    = 5
  PROVIDER_FAILED      = 1

satisfaction:
  REROUTED_ACCEPTED_CLAIM = 5
  NO_EVIDENCE_FOUND       = 6

source:
  CompanyGuide = 5
  DART         = 3
  KIND         = 1
  KRX          = 1
  IR           = 1

accepted refs = 5
unique refs   = 1
accepted primitive = medium_term_revision_visibility only
direct accepted claim = 0
```

v63에서 드러난 문제:

```text
rerouted feedback을 planner에 보여 줘도,
LLM이 다시 CompanyGuide를 내면 같은 medium_term_revision_visibility claim이 반복 accepted됐다.
```

### v64

```text
path = output/census_v4/2026-07-01-real-planner-rerouted-source-filter-v64

Full Thesis seed rows = 12
status:
  NO_EVIDENCE_FOUND    = 8
  EVIDENCE_OS_ACCEPTED = 2
  PROVIDER_FAILED      = 1
  REJECTED_BY_POLICY   = 1

satisfaction:
  NO_EVIDENCE_FOUND       = 10
  REROUTED_ACCEPTED_CLAIM = 1
  DIRECT_ACCEPTED_CLAIM   = 1

source:
  DART         = 6
  CompanyGuide = 2
  KIND         = 1
  KRX          = 1
  IR           = 1
  policy       = 1

origin:
  research_brain_v4_attempt = 11
  feedback_retry            = 1

accepted refs = 2
unique refs   = 1
accepted primitive = medium_term_revision_visibility only
```

v64에서 좋아진 점:

```text
CompanyGuide 반복 accepted refs:
  v63 = 5
  v64 = 2

CompanyGuide-only retry 중 원래 gap을 못 닫는 경우:
  REJECTED_BY_POLICY row로 감사에 남김

drop row:
  task_id = RSTASKV4RETRYDROP-69ca499fc00391005ae82d92
  stop_reason = rerouted_feedback_removed_all_candidate_source_classes
```

v64에서도 아직 안 된 점:

```text
accepted primitive는 여전히 medium_term_revision_visibility뿐이다.
C06 Full Thesis 직접 primitive는 대부분 UNKNOWN이다.
```

`primitive_states.jsonl`의 000660 Full Thesis seed 상태:

```text
PRESENT_CURRENT:
  medium_term_revision_visibility

UNKNOWN:
  cash_or_revision_conversion
  customer_preorder_or_allocation
  hbm_capacity_constraint
  hbm_capacity_pre_sold
  memory_price_increase_mentioned
  official_disclosure_status_current
  official_report_snapshot_current
  qualification_status
  revenue_visibility_contract
```

## 삼성전자 / 하이닉스 현재 해석

### 삼성전자 005930

이번 v64 output에서 삼성전자는 다음 정도만 확인된다.

```text
source_task_executions:
  source_class = DART
  primitive_gap = information_confidence
  status = EVIDENCE_OS_ACCEPTED

accepted_claims:
  primitive_id = information_confidence

score_contributions:
  raw_points = 1.0

stagecourt_traces:
  base_stage = 1
```

이걸 운영 Stage로 읽으면 안 된다.

```text
삼성전자 Full Thesis Stage = 없음
삼성전자 FULL_E2R_100 verified score = 없음
```

### SK하이닉스 000660

하이닉스는 두 종류가 섞여 있다.

```text
1. 일반 DART CandidateEvent:
   capital_allocation_event / information_confidence 일부 claim
   base_stage = 1

2. Full Thesis seed 000660:
   medium_term_revision_visibility claim 1개만 PRESENT_CURRENT
   C06 핵심 primitive는 UNKNOWN
   StageCourt base_stage = 0
```

이걸 운영 Stage로 읽으면 안 된다.

```text
SK하이닉스 Full Thesis Stage = 없음
SK하이닉스 FULL_E2R_100 verified score = 없음
```

## 공격 포인트

다음 에이전트가 빡세게 봐야 할 부분은 아래다.

### 교차검증 요약

읽기 전용 subagent 3개가 독립 확인했다.

```text
Stage semantics reviewer:
  운영 Full Thesis Stage row = 0
  현재 3391 rows는 모두 CENSUS_EVENT_BOARD 상태표
  "Stage rows=3391"이라고만 쓰면 과장

Rerouted feedback reviewer:
  rerouted_claim_feedback row 자체는 score/stage/current_score_eligible를 넣지 않는다.
  하지만 existing_evidence_summary 전체에는 recursive forbidden-key sanitizer가 없다.
  누군가 feedback dict에 stage/score 키를 섞으면 prompt에 들어갈 수 있다.

Next patch reviewer:
  v64는 거짓 승격 방지는 좋아졌지만 운영 파이프라인은 아니다.
  다음 P0는 Stage promotion이 아니라 IR/company/official 원문 획득 + live LLM claim extraction이다.
```

이 검토를 반영한 최신 문장:

```text
v64 artifact에는 Stage label row가 3391개 존재하지만,
이는 모두 stage_scope=CENSUS_EVENT_BOARD인 daily Census event-board/base_stage 상태표다.
운영용 Full Thesis / Full E2R Stage row는 0개이며,
모든 row가 operator_stage_use=NOT_FULL_THESIS_STAGE,
full_thesis_stage=FULL_THESIS_NOT_RUN로 표시된다.
따라서 Stage1, Stage2-Watch, 3-Red는 현재 full thesis 확정 Stage가 아니라
event-board watch/risk label로만 읽어야 한다.
```

### 공격 1. direct accepted claim 1개를 과대해석하지 말 것

v64에는 `direct_accepted_claim_count = 1`이 있다.

하지만 이 direct claim은:

```text
primitive = medium_term_revision_visibility
source = CompanyGuide consensus
```

이다.

이건 C06 Full Thesis에서 필요한 고객배정, CAPA sold-out, revenue mix, cash/FCF bridge를 닫지 않는다.

따라서:

```text
direct_accepted_claim_count > 0
```

만으로 Stage promotion을 허용하면 다시 과대승격 버그가 난다.

### 공격 2. rerouted feedback context sanitizer 부재

v64에서 새로 만든 `rerouted_claim_feedback` row 자체는 점수/Stage 키를 넣지 않는다.

테스트도 이 점을 확인한다.

```text
test_rerouted_claim_feedback_rows_are_gap_level_not_score_context
test_rerouted_claim_feedback_retries_planner_once
```

하지만 전체 `existing_evidence_summary`에는 recursive sanitizer가 없다.

위험 예:

```json
{
  "rerouted_claim_feedback": [
    {
      "requested_primitive_gap": "hbm_capacity_pre_sold",
      "accepted_primitive_ids": ["medium_term_revision_visibility"],
      "stage": "3-Green",
      "score": 92.0
    }
  ]
}
```

현재 생성 경로는 이런 row를 만들지 않지만, 방어적으로 보면 summary builder가 forbidden key를 재귀적으로 제거해야 한다.

다음 패치 요구:

```text
existing_evidence_summary 전체에 recursive forbidden-key sanitizer 추가
forbidden keys:
  score
  stage
  current_score_eligible
  verified_final
  accepted_claim_final
  target_stage
  green_unlock_score

테스트:
  malicious feedback dict에 stage/score가 있어도 planner prompt payload에는 안 들어가야 한다.
```

### 공격 3. full_thesis_queue_context의 stage/score 계열 키 명시

교차검증에서 `full_thesis_queue_context`가 다음 힌트를 포함한다는 지적이 나왔다.

```text
source_base_stage
source_stage_signal
source_score_contribution_ids
```

이 값들은 event-board routing 출처를 설명하는 감사 context일 수 있지만, LLM planner가 이를 목표 Stage처럼 읽으면 안 된다.

다음 패치에서 둘 중 하나를 선택해야 한다.

```text
선택 A:
  prompt에 들어가는 planner context에서는 이 키를 제거하고,
  raw audit leaf에만 보관한다.

선택 B:
  이름을 routing_source_*로 바꾸고,
  "target score/stage가 아니라 이전 상태표 출처"라는 rule과 테스트를 추가한다.
```

쉬운 예:

```text
이전 상태표에 Stage2-Watch라고 적혀 있었다.
  -> "조사 대상으로 올린 이유"일 수는 있다.
  -> LLM이 "Stage2가 정답이구나"라고 읽으면 안 된다.
```

### 공격 4. rerouted source filtering이 너무 넓게 막는지 확인

v64 source filter는 특정 primitive gap에 대해 이전에 rerouted-only였던 source class를 제거한다.

위험:

```text
CompanyGuide가 A primitive에는 부적합했지만,
B primitive에는 적합할 수 있다.
```

현재 패치는 `primitive_gap_unsatisfied_ids` 기준으로 막도록 설계돼야 한다. 다음 리뷰에서는 이 범위가 source class 전체 금지로 새지 않았는지 확인해야 한다.

다음 테스트 gap:

```text
CompanyGuide가 hbm_capacity_pre_sold에는 rerouted-only였지만,
medium_term_revision_visibility에는 direct accepted될 수 있는 케이스를 보존해야 한다.
source class 전체 ban이 아니라 primitive-gap별 ban이어야 한다.
```

### 공격 5. direct acceptance가 다른 primitive일 때 retry가 막히는지 확인

교차검증에서 다음 edge case가 나왔다.

```text
rerouted feedback retry는 direct accepted claim이 하나라도 있으면 중단한다.
하지만 그 direct acceptance가 원래 unsatisfied primitive를 채웠는지 확인해야 한다.
```

위험 예:

```text
원래 gap:
  hbm_capacity_pre_sold

새 direct accepted:
  medium_term_revision_visibility

잘못된 처리:
  direct accepted가 있으니 hbm_capacity_pre_sold retry 종료

올바른 처리:
  hbm_capacity_pre_sold가 아직 UNKNOWN이면 retry/follow-up은 계속 material gap으로 남아야 한다.
```

다음 테스트:

```text
direct acceptance가 rerouted feedback의 primitive_gap_unsatisfied_ids를 실제로 닫지 못하면
rerouted material gap follow-up을 차단하지 않는다.
```

### 공격 6. retry drop audit counter 이름이 헷갈릴 수 있음

v64의 rerouted retry drop도 readiness audit에서는 source-lineage drop 계열 counter와 함께 보일 수 있다.

운영 로그에서 원인을 명확히 하려면 별도 counter가 필요하다.

```text
rerouted_feedback_retry_dropped_count
rerouted_feedback_retry_removed_source_count
rerouted_feedback_retry_removed_all_sources_count
```

쉬운 예:

```text
source lineage drop:
  "네이버 검색결과 원문 lineage가 불명확해서 drop"

rerouted feedback drop:
  "CompanyGuide가 C06 gap을 못 닫고 revision claim만 반복해서 drop"

둘은 원인이 다르다.
```

### 공격 7. LLM planner가 여전히 같은 문서를 다른 이름으로 가져오는지 확인

v64는 source class 반복을 일부 막았지만, 다음 변형은 아직 공격해야 한다.

```text
CompanyGuide -> ReportPDF라고 이름만 바꿔 같은 consensus 표를 가져오는 경우
CompanyGuide -> TrustedNews가 같은 consensus 수치를 인용하는 경우
IssuerIR -> IR 미설정으로 provider failed 뒤 general web으로 튀는 경우
```

필요한 추가 감사:

```text
canonical_document_id / underlying_event_id / source_lineage 기반 dedupe
same consensus table reused across source classes
same source data quoted by news counted as independent family
```

### 공격 8. LLM claim extractor live path가 0회인 상태

`llm_claim_extraction_audit.json`:

```text
llm_claim_extractor_attempt_count = 0
verdict = DISABLED_HONESTY_PASS
```

Brain/Web mode가 켜져 있어도 이번 smoke에서는 LLM claim extractor가 실제로 문서를 읽어 claim을 뽑지 않았다.

이 상태에서는 사용자가 원하는:

```text
"연구자료처럼 실제 문서를 읽고 증거 칸을 채우는 운영 파이프라인"
```

이 아직 아니다.

### 공격 9. web acquisition도 0회다

`brain_web_readiness_gate_audit.json`:

```text
web_search_call_count = 0
web_fetched_document_count = 0
web_or_llm_accepted_claim_count = 0
```

따라서 v64는 "official-first routing / source-task filtering" 패치이지, "live web/LLM evidence acquisition" 완성 패치가 아니다.

## 다음 패치 방향

### P0. 현재 truth를 문서와 감사에서 계속 유지

절대 쓰면 안 되는 문장:

```text
Stage2 종목 30개가 운영 Stage로 나왔다.
하이닉스가 Stage0/Stage1/Stage2로 확정됐다.
Brain/Web이 stage를 만들었다.
```

써야 하는 문장:

```text
CENSUS_EVENT_BOARD base_stage rows는 있다.
FULL_THESIS operating stage rows는 0개다.
v64 Brain/Web trace는 StageCourt까지 1개 갔지만 census_stage_status로 promotion되지 않았다.
```

### P1. planner context sanitizer와 stage/score leakage 차단

v64 후속 최우선 방어 패치다.

필요한 작업:

```text
_evidence_summary 또는 planner payload 직전에서 recursive forbidden-key sanitizer를 적용한다.
full_thesis_queue_context의 source_base_stage/source_stage_signal/source_score_contribution_ids가
LLM 목표값으로 오염되지 않게 제거 또는 명확한 routing_source_* 네이밍으로 바꾼다.
```

추가 테스트:

```text
malicious feedback dict with score/stage/current_score_eligible
  -> planner prompt payload에는 해당 키가 없어야 한다.

full_thesis_queue_context stage-like fields
  -> target stage/score로 해석될 수 있는 이름이면 prompt payload에서 금지한다.
```

이 패치는 작은 안전 패치지만, live LLM claim extraction을 켜기 전에 먼저 해야 한다.

### P2. live LLM claim extractor activation

현재 가장 큰 병목:

```text
llm_claim_extractor_attempt_count = 0
full_thesis_claim_count = 0
```

필요한 작업:

```text
official source task가 raw document / PDF / IR / DART text를 fetch하면
contract-blind LLM claim extractor가 실제 문장 claim을 추출해야 한다.

단, extractor 입력에는 score/stage/gap 점수를 주면 안 된다.
document text, target entity, as_of_date, source metadata만 준다.
```

쉬운 예:

```text
IR PDF 본문:
  "2026년 HBM 생산능력 대부분이 고객 주문으로 확보..."

Extractor:
  문장이 실제로 뭘 말하는지 claim으로 뽑는다.

Mapper:
  그 claim이 hbm_capacity_pre_sold인지 나중에 판단한다.

Scorer:
  accepted claim ID가 있어야 점수를 준다.
```

### P3. IssuerIR / Company source acquisition repair

v64에서 IR source는 여전히 실질 claim을 못 만들었다.

필요한 작업:

```text
IssuerIR discovery / company newsroom / report PDF fetch를 실제 provider로 연결한다.
official-first 원칙을 유지한다.
IR provider가 없으면 곧장 낮은 점수로 확정하지 말고 Provider/Source Pending으로 남긴다.
```

### P4. direct material primitive coverage gate

`direct_accepted_claim_count`만으로는 부족하다.

Full Thesis C06 승격에는 적어도 다음이 구분돼야 한다.

```text
revision visibility only:
  medium_term_revision_visibility

material C06 bridge:
  customer_preorder_or_allocation
  hbm_capacity_pre_sold
  qualification_status
  revenue_visibility_contract
  cash_or_revision_conversion
```

다음 테스트:

```text
medium_term_revision_visibility만 있으면 Full Thesis Stage promotion 금지
medium_term_revision_visibility + C06 material primitive quorum이 있어야 promotion 가능
```

### P5. source family / source lineage dedupe 강화

CompanyGuide consensus가 다른 wrapper를 통해 들어와도 같은 underlying evidence family로 세야 한다.

필요한 식별자:

```text
canonical_document_id
underlying_event_id
source_lineage
official_document_id
provider_request_id
content_hash
```

### P6. bounded live smoke 확대

현재 smoke는 universe-limit 1, planner-success-limit 1이다.

다음 단계에서는:

```text
삼성전자 / SK하이닉스 직접 Full Thesis smoke
각 archetype별 source-backed replay smoke
provider failure pending smoke
same corpus repeatability smoke
```

를 분리해야 한다.

## 다음 acceptance 기준

다음 중 하나라도 안 되면 READY라고 쓰면 안 된다.

```text
1. FULL_THESIS row > 0을 만들더라도 score_scale = FULL_E2R_100이어야 한다.
2. operator_stage_use가 운영 사용 가능 상태여야 한다.
3. nonzero Full Thesis score contribution은 accepted_claim_id를 가져야 한다.
4. accepted_claim_id는 EvidenceAnchor / EvidenceDocument까지 닫혀야 한다.
5. medium_term_revision_visibility only는 C06 Full Thesis promotion을 만들 수 없다.
6. current_score_eligible, score, stage를 LLM feedback으로 주면 안 된다.
7. rerouted-only same-source retry는 감사 row 없이 조용히 사라지면 안 된다.
8. LLM claim extractor attempt가 0이면 Brain/Web evidence pass를 선언하면 안 된다.
9. web_or_llm_accepted_claim_count가 0이면 Brain/Web partial promotion을 허용하면 안 된다.
10. provider/source failure는 낮은 점수 확정이 아니라 Pending이어야 한다.
11. existing_evidence_summary 전체에서 forbidden score/stage key가 재귀적으로 제거되어야 한다.
12. direct accepted claim이 있어도 material primitive quorum을 닫지 못하면 Full Thesis promotion 금지다.
13. `full_thesis_seed_materialization_audit` PASS를 Full Thesis 완료 PASS로 해석하면 안 된다.
```

## 현재 최종 판정

```text
v64 verdict = NOT_READY / BLOCKED

좋아진 것:
  rerouted accepted claim feedback이 planner context에 들어간다.
  rerouted-only source class 반복을 source task validation에서 줄인다.
  제거된 retry task가 REJECTED_BY_POLICY로 감사에 남는다.

아직 안 된 것:
  FULL_THESIS Stage rows = 0
  FULL_E2R_100 verified score rows = 0
  full_thesis_claim_count = 0
  llm_claim_extractor_attempt_count = 0
  web_fetched_document_count = 0
  C06 material primitive 대부분 UNKNOWN

다음 패치의 핵심:
  official/IR/PDF/text 원문을 LLM contract-blind claim extractor로 연결하고,
  accepted claim -> primitive -> score -> StageCourt -> promotion까지 닫아야 한다.
```

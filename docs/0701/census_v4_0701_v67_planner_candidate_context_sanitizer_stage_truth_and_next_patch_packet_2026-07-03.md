# Census v4 0701 v67 Planner Candidate Context Sanitizer / Stage Truth / Next Patch Packet

작성일: 2026-07-03  
기준 실행일: 2026-07-01  
관련 출력:

```text
output/census_v4/2026-07-01-real-planner-context-sanitizer-v67
```

## 결론

v67에서 고친 핵심은 이것이다.

```text
LLM planner가 보는 candidate_event 원문에서
event-board의 stage/score 힌트를 제거했다.
```

v64까지는 `existing_evidence_summary`는 정리됐지만, 같은 프롬프트의 `candidate_event.to_dict()`가 원본을 그대로 들고 있었다.

쉬운 예:

```text
요약란에서는 "Stage1" 정답지를 지웠다.
그런데 첨부된 원본 사건 카드에는
source_stage_signal=OFFICIAL_EVENT_WATCH
source_stage_decision_status=FINAL
source_base_stage=Stage1
가 남아 있었다.
```

이 상태면 LLM planner가 원문 사실을 보고 조사 계획을 짜는 것이 아니라, 이전 event-board 판정 냄새를 맡고 그쪽으로 끌릴 수 있다.

v67은 이 누수를 막았다. 다만 이것은 운영 준비 완료가 아니다.

```text
verdict = NOT_READY / BLOCKED
FULL_THESIS 운영 Stage row = 0
FULL_E2R_100 verified score row = 0
verified_score_present_count = 0
```

즉 현재 상태는 다음과 같다.

```text
상태판 Stage 비슷한 행은 있다.
운영 full thesis stage는 아직 없다.
```

## 지금 Stage가 있는가

산출물 기준으로 정확히 나누면 다음이다.

```text
census_stage_status.jsonl rows = 3391
stage_scope = CENSUS_EVENT_BOARD 3391
operator_stage_use = NOT_FULL_THESIS_STAGE 3391
census_stage_status.stage = None 3391
display_stage_label = None 3391
```

`base_stage` 분포는 있다.

```text
Stage0       3306
Stage1         54
Stage2-Watch   30
Red             1
```

하지만 이 `base_stage`는 운영 점수 Stage가 아니다. `CensusAssessmentEvent`와 event-board 상태판이 만든 "현재 상태 분류"다.

쉬운 예:

```text
전체 학교 학생 3391명을 출석부에 올렸다.
몇 명은 "상담 필요", "관찰 필요" 같은 메모가 붙었다.
하지만 아직 시험 답안지를 채점한 점수/등급은 0명이다.
```

따라서 다음 표현은 틀리다.

```text
Stage가 3391개 있다.
Stage2-Watch가 30개 있으니 운영 Stage가 있다.
```

정확한 표현은 이거다.

```text
event-board 상태판 row는 3391개 있다.
그중 base_stage 메모는 나뉘어 있다.
하지만 FULL_THESIS 운영 Stage와 verified score는 아직 0개다.
```

## v64에서 남았던 실제 문제

v64의 교차검증 피드백은 맞았다.

v64는 다음은 정리했다.

```text
existing_evidence_summary.rerouted_claim_feedback
existing_evidence_summary.rejected_claim_feedback
existing_evidence_summary.full_thesis_queue_context 일부
```

하지만 planner raw prompt에는 여전히 이 경로가 남아 있었다.

```text
prompt_payload.events[0].candidate_event.event_summary
prompt_payload.events[0].candidate_event.structured_payload
prompt_payload.events[0].candidate_event.raw_reason_codes
```

문제 예:

```text
candidate_event.event_summary =
  SK하이닉스 requires full-thesis refresh ...
  source_stage_signal=OFFICIAL_EVENT_WATCH;
  source_stage_decision_status=FINAL;
  ...

candidate_event.structured_payload =
  source_base_stage = Stage1
  source_score_contribution_ids = [...]
  source_stage_signal = OFFICIAL_EVENT_WATCH
  source_stage_decision_status = FINAL

raw_reason_codes =
  event_board_non_stage0_needs_full_thesis_refresh
```

이건 점수/stage를 직접 출력하라는 말은 아니지만, LLM에게 "이전 판정의 방향"을 흘리는 힌트다.

## v67 패치 내용

수정 파일:

```text
src/e2r/research_brain/v4_planner_runtime.py
tests/test_research_brain_v4_operational_modes.py
```

핵심 변경:

```text
1. candidate_event planner sanitizer 추가
2. candidate_event.event_summary 안의 score/stage key=value 제거
3. candidate_event.structured_payload에서 score/stage류 key 제거
4. candidate_event.raw_reason_codes에서 score/stage류 reason 제거
5. existing_evidence_summary sanitizer는 유지
6. planner prompt builder와 minimal trace builder 모두 sanitizer 경유
7. 보강 테스트 추가
```

구체적으로 제거되는 예:

```text
source_stage_signal=OFFICIAL_EVENT_WATCH
source_stage_decision_status=FINAL
source_base_stage=Stage1
source_score_contribution_ids
operator_stage_use
event_board_non_stage0_needs_full_thesis_refresh
```

유지되는 예:

```text
missing_full_thesis_primitives
source_missing_primitives
source_material_gap_ids
preferred_source_classes
fallback_source_classes
official_first_required
source_primary_archetype
source_large_sector_id
```

이 유지 정보는 stage 정답이 아니라 조사할 빈칸이다.

쉬운 예:

```text
"이 학생은 1등급이었다"는 제거한다.
"수학 풀이 근거가 비어 있다"는 유지한다.
```

## 왜 전체 score/stage 문자열을 무조건 지우지 않았나

planner prompt에는 정상적인 금지 규칙도 들어간다.

```text
forbidden_output_keys = ["score", "stage", ...]
rules = "Do not output score, stage, ..."
```

이건 누수가 아니라 방어 장치다. raw prompt 검사에서 `"score"`, `"stage"` 문자열이 남는 것은 이 금지 목록 때문이다.

따라서 v67 검사 기준은 다음으로 잡았다.

```text
나쁜 것:
  candidate_event / existing_evidence_summary 데이터 안의
  source_stage_signal=...
  source_stage_decision_status=...
  source_base_stage=...
  source_score_contribution_ids

정상인 것:
  forbidden_output_keys 안의 "score", "stage"
  rules 안의 "Do not output score, stage"
```

## 실제 v67 smoke 결과

실행:

```bash
E2R_CODEX_PLANNER_TIMEOUT_SECONDS=120 \
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-real-planner-context-sanitizer-v67 \
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
stdout = NOT_READY
```

이 `NOT_READY`는 정상적인 honesty gate 결과다. 즉 패치가 실패했다는 뜻이 아니라, 아직 운영 stage로 승급할 증거 체인이 없다는 뜻이다.

주요 audit 숫자:

```text
brain_web_readiness_gate_audit.verdict = BLOCKED
brain_stage_promotion_audit.verdict = BLOCKED

llm_planner_call_count = 22
llm_real_provider_success_count = 2
source_task_execution_count = 12
real_document_fetched_count = 4

official_accepted_claim_count = 1
full_thesis_seed_accepted_claim_count = 2
direct_accepted_claim_count = 0
direct_source_task_satisfied_count = 0
rerouted_source_task_claim_count = 2
policy_rejected_source_task_execution_count = 1

brain_score_contribution_count = 2
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 0
full_thesis_claim_count = 0
llm_claim_extractor_attempt_count = 0
web_fetched_document_count = 0
web_search_call_count = 0
```

Full Thesis seed source task 분포:

```text
rows = 12

status:
  NO_EVIDENCE_FOUND     8
  EVIDENCE_OS_ACCEPTED  2
  PROVIDER_FAILED       1
  REJECTED_BY_POLICY    1

satisfaction:
  NO_EVIDENCE_FOUND          10
  REROUTED_ACCEPTED_CLAIM     2

source_class:
  DART          6
  CompanyGuide  2
  KIND          1
  KRX           1
  IR            1
  policy        1

accepted refs = 2
unique accepted claims = 1
```

accepted claim은 둘 다 같은 CompanyGuide consensus claim이다.

```text
accepted primitive = medium_term_revision_visibility
requested primitive examples:
  cash_or_revision_conversion
  official_report_snapshot_current

stop_reason:
  rerouted_claim_accepted_original_gap_unsatisfied
```

즉 이 claim은 "컨센서스/중기 visibility"는 줄 수 있지만, C06의 직접 빈칸인 cash/FCF bridge, customer allocation, HBM capacity pre-sold, shipment/revenue mix를 닫지는 못했다.

쉬운 예:

```text
"선생님들이 성적 전망을 올렸다"는 증거는 있다.
하지만 "실제 계약서, 고객 배정, 현금흐름 전환" 증거는 아직 없다.
그래서 Green/Yellow 운영 stage로 올리면 안 된다.
```

## v67 raw prompt 검증

v67 feedback retry prompt:

```text
planner_run_id = PLANV4-597b9d73949b7424561b999d
```

candidate event summary:

```text
SK하이닉스 requires full-thesis refresh from Census event-board row.
missing_full_thesis_primitives=full_thesis_refresh_task_not_run,
full_thesis_archetype_hypothesis_required,
source_backed_primitive_coverage_required
```

제거 확인:

```text
source_stage_signal=...          없음
source_stage_decision_status=... 없음
source_base_stage=...            없음
source_score_contribution_ids    없음
Stage1                           없음
```

raw reason codes:

```text
before:
  FULL_THESIS_REFRESH_QUEUE
  event_board_non_stage0_needs_full_thesis_refresh
  P2_EVENT_WATCH_REFRESH

after:
  FULL_THESIS_REFRESH_QUEUE
  P2_EVENT_WATCH_REFRESH
```

candidate structured payload keys:

```text
blocked_reason
fallback_source_classes
forbidden_source_classes
max_candidates_per_query
max_fetches_per_task
max_queries_per_task
max_source_tasks
missing_full_thesis_primitives
official_first_required
preferred_source_classes
queue_task_id
source_accepted_claim_ids
source_candidate_event_ids
source_large_sector_id
source_material_gap_ids
source_missing_primitives
source_primary_archetype
source_secondary_archetypes
target_archetype
target_archetype_status
```

이 중 다음은 없다.

```text
source_base_stage
source_stage_signal
source_stage_decision_status
source_score_contribution_ids
operator_stage_use
```

기존 `existing_evidence_summary`도 정리된 상태다.

```text
event_summary_preview:
  SK하이닉스 requires full-thesis refresh from Census event-board row.
  missing_full_thesis_primitives=...

full_thesis_queue_context:
  event_board_decision_status
  event_board_scope
  event_board_signal
  source_failed_gate_ids
  ...
```

여기에는 `event_board_*`로 이름을 바꾼 non-binding context가 남아 있다. 이건 "운영 stage로 쓰라"는 뜻이 아니라 "이 row가 event-board에서 왔다"는 출처 설명이다.

다음 에이전트가 공격적으로 볼 지점:

```text
event_board_signal 같은 이름도 LLM에게 과도한 힌트인가?
```

내 판단은 현재는 허용 가능하지만, 더 보수적으로 가려면 `event_board_signal`까지 제거하고 `source_missing_primitives`, `source_material_gap_ids`만 남기는 방향도 가능하다.

## 테스트 결과

집중 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_prompt_payload_sanitizes_candidate_event_score_stage_context \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_prompt_payload_sanitizes_direct_existing_evidence_summary_input \
  tests.test_research_brain_v4_operational_modes.ResearchBrainV4OperationalModesTests.test_full_thesis_seed_context_is_visible_to_planner_without_forcing_target_archetype \
  -v
```

결과:

```text
Ran 3 tests
OK
```

관련 묶음:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_real_planner_provider \
  tests.test_census_v4_full_thesis_smoke_tasks \
  -v
```

결과:

```text
Ran 78 tests in 26.580s
OK
```

전체 테스트:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5095 tests in 207.773s
OK
```

diff whitespace check:

```bash
git diff --check
```

결과:

```text
OK
```

## 코드 변경의 의도

이번 패치는 점수나 stage threshold를 바꾸지 않았다.

바꾼 것은 LLM planner 입력 위생이다.

```text
기존:
  planner가 candidate_event 원본에서 이전 event-board stage/score 힌트를 볼 수 있음

변경:
  planner는 "무엇이 비었는가"와 "어떤 source를 먼저 볼 것인가"만 봄
  이전 stage/score 판정값은 보지 않음
```

이게 중요한 이유:

```text
LLM은 증거를 찾는 역할이다.
LLM에게 기존 판정값을 보여 주면, 원문 증거보다 판정값을 따라갈 수 있다.
```

예:

```text
나쁜 입력:
  이 종목은 source_base_stage=Stage1이고 Green gate missing...
  -> LLM이 "Stage1을 Stage2로 올릴 자료"를 찾는 식으로 오염될 수 있음

좋은 입력:
  이 종목은 full thesis refresh가 필요하고,
  cash_or_revision_conversion, source_backed_primitive_coverage가 비어 있음
  -> LLM이 실제 증거 source task를 계획함
```

## 아직 해결 안 된 것

v67은 planner context 오염을 줄였을 뿐, 운영 Full Thesis를 만들지는 못했다.

남은 blockers:

```text
1. direct_accepted_claim_count = 0
2. direct_source_task_satisfied_count = 0
3. full_thesis_claim_count = 0
4. brain_promoted_stage_row_count = 0
5. llm_claim_extractor_attempt_count = 0
6. web_fetched_document_count = 0
7. C06 material primitive coverage가 여전히 UNKNOWN
```

가장 큰 원인:

```text
CompanyGuide consensus claim은 medium_term_revision_visibility로만 유효하다.
그 claim을 cash/FCF, customer allocation, capacity pre-sold, revenue mix로 쓰면 안 된다.
```

즉 v67의 BLOCKED는 맞다.

```text
틀린 결론:
  그래도 컨센서스 claim이 있으니 SK하이닉스 Stage가 생겼다.

맞는 결론:
  컨센서스 visibility claim 하나는 생겼지만,
  C06 Full Thesis 직접 primitive가 닫히지 않아 운영 Stage는 없다.
```

## 다음 패치 방향

다음 에이전트가 바로 공격해야 할 순서:

### P0. Direct primitive satisfaction guard 재검토

현재 accepted claim이 rerouted되면 audit은 남는다.

하지만 더 강하게 해야 한다.

```text
requested primitive gap을 닫지 못한 accepted claim은
해당 source task의 direct satisfaction으로 절대 계산하지 않는다.
```

현재 v67 숫자상 direct count는 0이라 결과는 맞다. 그래도 code path에서 향후 다른 source가 들어왔을 때 같은 문제가 반복되지 않는지 봐야 한다.

### P1. Live contract-blind LLM claim extractor 활성화

v67 smoke:

```text
llm_claim_extractor_attempt_count = 0
```

이건 아직 "LLM이 문서에서 claim을 직접 읽는 운영 경로"가 이 smoke에서 작동하지 않았다는 뜻이다.

다음 목표:

```text
official document / IR / report PDF / trusted article original
  -> contract-blind LLM extractor
  -> raw assertion
  -> adjudication
  -> primitive mapping
  -> accepted claim
```

LLM에게 점수를 묻는 것이 아니다. LLM에게 원문 사실을 뽑게 해야 한다.

### P2. IssuerIR / company source acquisition repair

현재 IR source task는 1개 있었지만 accepted claim으로 닫히지 않았다.

필요한 것:

```text
issuer IR page / earnings call / presentation PDF fetch
PDF text anchor
quote/span anchor 검증
source lineage original 확인
```

특히 C06에는 다음 원천이 필요하다.

```text
고객 배정 / qualification / capacity pre-sold / HBM 매출 비중 / cash 또는 EPS revision bridge
```

### P3. C06 material primitive acquisition

CompanyGuide visibility만으로는 부족하다.

닫아야 할 primitive 예:

```text
customer_preorder_or_allocation
hbm_capacity_pre_sold
qualification_status
revenue_visibility_contract
cash_or_revision_conversion
```

이 중 하나도 직접 닫지 못하면 Full Thesis Stage를 만들면 안 된다.

### P4. event_board_* context 더 보수화 검토

v67은 `source_stage_signal`을 `event_board_signal`로 바꿔 non-binding context로 남긴다.

장점:

```text
이 full thesis refresh seed가 왜 생겼는지 설명 가능
```

단점:

```text
LLM이 event_board_signal 자체를 stage 힌트로 받아들일 가능성
```

다음 에이전트는 이 필드를 제거해도 planner 품질이 유지되는지 테스트해도 된다.

보수적 대안:

```text
full_thesis_queue_context에는
source_missing_primitives
source_material_gap_ids
preferred_source_classes
fallback_source_classes
official_first_required
만 남긴다.
```

### P5. 삼성전자 / SK하이닉스 bounded Full Thesis smoke

v67은 universe limit 1이라 SK하이닉스 seed만 봤다.

다음에는 bounded 조건으로 둘 다 봐야 한다.

검증 질문:

```text
삼성전자에 월덱스 감사의견 같은 wrong-subject risk가 다시 붙지 않는가?
SK하이닉스 컨센서스 claim이 capacity/customer/cash primitive로 새지 않는가?
둘 다 source-backed direct primitive 없으면 stage가 pending/none으로 남는가?
```

## 다음 에이전트용 공격 체크리스트

반드시 다음을 다시 확인할 것.

```text
1. raw planner prompt에서 candidate_event에 score/stage hint가 남는가?
2. forbidden_output_keys의 "score"/"stage"를 누수로 오인하지 않았는가?
3. event_board_signal이 LLM planning bias를 만들지는 않는가?
4. source_primary_archetype이 target_archetype처럼 작동하지 않는가?
5. rerouted accepted claim이 direct source task satisfaction으로 승격되지 않는가?
6. CompanyGuide consensus claim이 C06 cash/capacity/customer primitive로 새지 않는가?
7. full_thesis_claim_count가 0인데 report가 stage 존재를 과장하지 않는가?
8. llm_claim_extractor_attempt_count가 0인 상태를 "LLM 운영 성공"으로 쓰지 않는가?
9. web_fetched_document_count가 0인데 Brain/Web readiness를 pass로 쓰지 않는가?
10. CENSUS_EVENT_BOARD base_stage를 FULL_THESIS 운영 Stage처럼 설명하지 않는가?
```

## 최종 현재 truth

v67 기준 최종 진실:

```text
Planner stage/score context leak:
  candidate_event 경로는 패치됨.

Tests:
  full suite 5095 OK.

Real planner:
  실제 Codex planner success 2회.

Source acquisition:
  real document fetched 4개.

Accepted claim:
  CompanyGuide consensus visibility claim 1개.

Direct material primitive:
  0개.

LLM claim extractor:
  0회.

Web fetched document:
  0개.

Operational Full Thesis Stage:
  0개.

Verdict:
  NOT_READY / BLOCKED.
```

한 문장으로 정리:

```text
v67은 "LLM planner에게 이전 stage/score 정답지를 보여 주는 문제"를 막았지만,
아직 "실제 문서에서 C06 직접 primitive를 LLM/anchor/claim 경로로 닫아 운영 Stage를 만드는 문제"는 남아 있다.
```

# Census v4 0701 Current Stage Truth Cross-Review and Patch Direction

작성 시점: 2026-07-02 KST

> 최신 주의: 이 문서는 FULL_THESIS row가 0개였던 패치 전 상태를 고정한 문서다. 이후 `census_v4_0701_full_thesis_smoke_patch_result_and_remaining_goal_gap_2026-07-02.md`에서 삼성전자/하이닉스 controlled full thesis smoke가 통과했다. 최신 숫자는 그 문서를 우선한다.

이 문서는 다음 에이전트가 빡세게 리뷰할 수 있도록 현재 상태를 숨기지 않고 고정한다.

한 줄 결론:

> Stage가 있는 종목은 있다. 하지만 현재 Stage 대부분은 `CENSUS_EVENT_BOARD` 상태판이고, 아직 `FULL_THESIS` 운영 Stage는 0개다.

쉽게 말하면 지금 파이프라인은 전 종목 출석부와 일부 일일 이벤트 표시는 만들었다. 하지만 삼성전자/하이닉스 같은 종목을 "HBM thesis 기준으로 100점 만점 full E2R Stage를 냈다"고 말할 상태는 아니다.

## 1. 검증 기준 산출물

최신으로 대조한 로컬 산출물:

```text
/tmp/census_v4_enabled_after_self_repair_and_trace_patch
```

핵심 파일:

```text
readiness_verdict.json
goal_completion_audit.json
samsung_hynix_full_thesis_smoke.json
brain_web_readiness_gate_audit.json
census_stage_status.jsonl
```

최신 전체 테스트 artifact:

```text
/tmp/census_v4_after_self_repair_full_tests.json
status = OK
test_count = 4976
failed_count = 0
error_count = 0
```

주의:

```text
4976 tests OK는 현재 구현의 감사/스코프 규칙이 통과했다는 뜻이다.
FULL_THESIS 운영 Stage가 생성됐다는 뜻이 아니다.
```

예시:

```text
자동차 정기검사에서 "브레이크 경고등 없음"은 통과했다.
그렇다고 "서울에서 부산까지 실제 주행 검증 완료"는 아니다.
```

## 2. Stage는 실제로 있는가?

있다. 최신 `census_stage_status.jsonl` 기준 row는 3391개다.

Stage 분포:

```text
canonical_stage:
0       3307
1         53
2         30
3-Red      1
```

base stage 분포:

```text
Stage0          3306
Stage1            53
Stage2-Watch      30
Red                1
0                  1
```

따라서 `Stage1`, `Stage2-Watch`, `3-Red`가 있긴 하다.

하지만 바로 아래가 더 중요하다.

Stage scope:

```text
CENSUS_EVENT_BOARD  3390
BRAIN_WEB_PARTIAL      1
FULL_THESIS            0
```

Score scale:

```text
NO_SCORE                3324
EVENT_WEIGHTED_PARTIAL    67
FULL_E2R_100               0
```

운영자가 읽어야 할 해석:

```text
Stage row 있음
!= full thesis 운영 점수 있음

EVENT_WEIGHTED_PARTIAL 있음
!= E2R 100점 만점 verified score 있음
```

## 3. 삼성전자/하이닉스 현재 의미

최신 row에서 삼성전자와 SK하이닉스는 둘 다 `Stage1`이다.

하지만 이것은 C06/HBM full thesis Stage가 아니다.

삼성전자:

```text
symbol = 005930
base_stage = Stage1
canonical_stage = 1
stage_scope = CENSUS_EVENT_BOARD
score_scale = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.0
daily_event_evidence_score = 4.0
full_thesis_stage = FULL_THESIS_NOT_RUN
full_thesis_verified_score = null
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
```

SK하이닉스:

```text
symbol = 000660
base_stage = Stage1
canonical_stage = 1
stage_scope = CENSUS_EVENT_BOARD
score_scale = EVENT_WEIGHTED_PARTIAL
event_evidence_score = 4.0
daily_event_evidence_score = 4.0
full_thesis_stage = FULL_THESIS_NOT_RUN
full_thesis_verified_score = null
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
```

쉬운 예:

```text
삼성전자 row의 Stage1은 "최근 공식 이벤트가 있어서 상태판에 표시됐다"는 뜻이다.
"HBM 고객 배정, capacity sold-out, revenue mix, cash/revision까지 검증해서 Stage1"이라는 뜻이 아니다.
```

따라서 지금 삼성전자/하이닉스에 대해 말할 수 있는 정확한 문장은 이것이다.

```text
둘 다 Census event-board Stage1은 있다.
둘 다 C06/HBM full thesis Stage는 아직 없다.
둘 다 FULL_E2R_100 verified score는 없다.
```

## 4. Full thesis smoke 현재 상태

`samsung_hynix_full_thesis_smoke.json` 기준:

```text
verdict = PENDING_FULL_THESIS_REFRESH
full_thesis_status = PENDING_FULL_THESIS_REFRESH
score_allowed_before_execution = false
hardcoded_query_count = 0
```

심볼별 missing primitive:

```text
named_customer_or_customer_quality
qualification_status
capacity_allocation_or_pre_sold
hbm_shipment_or_revenue_mix
cash_or_revision_conversion
repeat_evidence_family
source_quorum
```

각 심볼에 7개씩, 총 14개 full thesis smoke task가 계획되어 있다.

중요:

```text
task planned
!= source fetched
!= claim accepted
!= score contribution created
!= StageCourt full thesis decision
```

현재 smoke task는 planning-only다.

삼성전자/하이닉스 per-symbol 값:

```text
full_thesis_claim_ids = []
full_thesis_score_contribution_ids = []
full_thesis_stagecourt_trace_ids = []
smoke_pass_allowed = false
blocking_reason = full_thesis_source_tasks_planned_but_not_executed
```

## 5. Brain/Web은 어디까지 됐나?

최신 `brain_web_readiness_gate_audit.json` 기준 Brain/Web gate는 통과했다.

```text
verdict = READY_FOR_BRAIN_WEB_EVIDENCE_PASS
brain_web_evidence_pass_allowed = true
llm_planner_call_count = 43
llm_real_provider_success_count = 7
llm_claim_extractor_attempt_count = 23
llm_claim_extractor_real_provider_count = 23
web_search_task_count = 14
naver_search_call_count = 14
web_fetched_document_count = 23
brain_to_claim_trace_count = 2
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 1
direct_accepted_claim_count = 0
rerouted_accepted_claim_count = 2
snippet_to_score_count = 0
snapshot_document_count = 0
fake_provider_used_count = 0
```

이건 진전이다. 이전에는 LLM/web leaf가 있어도 accepted claim이나 Stage promotion이 0이었다.

하지만 이것도 full thesis 통과는 아니다.

정확한 표현:

```text
Brain/Web partial path는 실제 provider, web search, fetched document, extractor, claim trace, partial stage promotion까지 만들었다.
그러나 full thesis C06/HBM smoke는 아직 실행되지 않았다.
```

예시:

```text
뉴스를 읽는 직원은 실제로 배치됐다.
그 직원이 작성한 일부 메모는 상태판에 반영됐다.
하지만 삼성/하이닉스 HBM 전체 투자논문 채점표는 아직 작성하지 않았다.
```

## 6. Readiness와 goal completion이 왜 다르게 보이나?

`readiness_verdict.json`:

```text
verdict = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
brain_web_evidence_pass = true
full_thesis_smoke_pass = false
meaningful_operational_stage_pass = false
target_gate = meaningful
target_gate_pass = false
labels include FULL_THESIS_SMOKE_PENDING
```

`goal_completion_audit.json`:

```text
goal_completion_ready = false
meaningful_operational_stage_pass_allowed = false
brain_web_evidence_pass_allowed = true
full_thesis_smoke_pass_allowed = false
blockers = ["full_thesis_smoke_pending"]
test_result_evidence_verdict = MACHINE_READABLE_TEST_ARTIFACT_PASS
self_repair_status = RUN_COMPLETE
```

해석:

```text
Anti-fake 상태판은 통과했다.
Brain/Web partial evidence gate도 통과했다.
전체 테스트 artifact도 있다.
하지만 full thesis smoke가 pending이라 goal complete는 아니다.
```

쉬운 예:

```text
건물 출입명부, CCTV, 소방점검은 통과했다.
하지만 엘리베이터 하중 테스트가 아직 안 끝났다.
그러면 "건물 사용 전 최종 승인"은 아직 아니다.
```

## 7. 현재 코드 상태에서 확인한 위험

`src/e2r/census/census_runner_v4.py`에는 full thesis replay hook 호출이 들어가 있다.

```python
full_thesis_export = _apply_full_thesis_smoke_replay(...)
```

작성 시점에는 이 함수가 정의되지 않은 중간 상태였기 때문에, 최소 안전 패치로 no-op 정의를 추가했다.

현재 no-op 의미:

```text
status = PENDING_FULL_THESIS_REFRESH
symbols = []
atomic_rows = []
stage_rows = 원본 유지
```

이 패치는 full thesis를 통과시키지 않는다. 오히려 가짜 pass를 막기 위한 안전장치다.

다음 에이전트가 주의해야 할 점:

```text
no-op을 FULL_THESIS_SMOKE_PASS처럼 읽으면 안 된다.
이 함수의 다음 구현은 반드시 실제 SourceTask -> document/anchor -> claim -> primitive -> contribution -> StageCourt chain을 닫아야 한다.
```

## 8. 지금 코드가 아직 일부러 막고 있는 것

`_samsung_hynix_smoke(stage_rows)`는 현재 full thesis를 pending으로 유지한다.

현재 구조:

```text
daily_event_claim_ids = 기존 event-board accepted claim
full_thesis_claim_ids = []
full_thesis_score_contribution_ids = []
full_thesis_stagecourt_trace_ids = []
blocking_reason = full_thesis_source_tasks_planned_but_not_executed
```

`_goal_completion_audit()`도 full thesis blocker를 유지한다.

현재 구조:

```text
full_thesis_smoke_pass_allowed = false
goal_completion_ready = false
blockers includes full_thesis_smoke_pending
```

이건 현재로서는 맞다.

잘못된 패치는 다음과 같다.

```text
FULL_THESIS task가 계획됐으니 pass 처리
삼성/하이닉스 event-board Stage1을 C06/HBM full thesis Stage로 승격
과거 연구자료 MD의 점수 결과를 그대로 full thesis score로 주입
URL-backed replay fixture만 보고 live 운영 통과 선언
```

## 9. 다음 패치 방향

다음 패치의 목표는 `Stage가 있긴 하다`에서 `meaningful full thesis Stage도 있다`로 넘어가는 것이다.

단, 가짜로 넘기면 안 된다.

### 9.1 Full thesis task는 planning-only에서 executed로 바뀌어야 한다

현재:

```text
full_thesis_smoke_tasks.jsonl
task_status = PLANNING_REQUIRED
score_evidence = false
```

목표:

```text
source_task_executions.jsonl
task_status = EXECUTED_WITH_ACCEPTED_CLAIM or EXHAUSTED_WITH_MATERIAL_GAP
accepted_claim_ids present when scored
fetched_document_ids present
evidence_anchor_ids present
score_claim_ids present
```

### 9.2 Claim chain은 끊기면 안 된다

필수 연결:

```text
source_task
-> source_task_execution
-> evidence_document
-> evidence_anchor
-> raw_assertion
-> adjudicated_claim
-> accepted_claim
-> primitive_state
-> score_contribution
-> stagecourt_trace
-> atomic_stage_decision
-> census_stage_status
```

각 nonzero score contribution은 support claim id가 있어야 한다.

예시:

```text
capacity_allocation_or_pre_sold에 10점이 들어갔다면
어느 문서의 어느 anchor에서 capacity allocation claim이 나왔는지 보여야 한다.
```

### 9.3 Daily event와 full thesis는 같은 점수 칸에 넣으면 안 된다

현재 필드 분리 원칙은 유지해야 한다.

```text
daily event score -> event_evidence_score / daily_event_evidence_score
full thesis score -> full_e2r_verified_score / full_thesis_verified_score
```

삼성전자 예시:

```text
최근 DART 이벤트로 Stage1 event-board row가 있다.
그 row의 4.0점을 HBM thesis score 4.0점으로 재사용하면 안 된다.
```

### 9.4 FULL_THESIS row가 생기면 AtomicStageDecision도 같이 생겨야 한다

FULL_THESIS stage row만 덧씌우면 안 된다.

필수:

```text
stage_scope = FULL_THESIS
score_scale = FULL_E2R_100
operator_stage_use = FULL_THESIS_STAGE
operator_score_use = FULL_E2R_SCORE
atomic_stage_decision_id present
stagecourt_trace_id present
accepted_claim_ids present
score_contribution_ids present
primitive_state_ids present
```

기존 event-board atomic decision은 representative에서 내려야 한다.

```text
is_representative = false
representative_replaced_by = FULL_THESIS
```

### 9.5 Pending도 정상 결과여야 한다

모든 full thesis가 무조건 Green/Yellow가 되어야 하는 것은 아니다.

허용되는 결과:

```text
FULL_THESIS FINAL
FULL_THESIS PENDING_MATERIAL_GAPS
FULL_THESIS SOURCE_PENDING
FULL_THESIS PROVIDER_PENDING
```

하지만 pending이면 낮은 score 확정으로 둔갑하면 안 된다.

예시:

```text
cash_or_revision_conversion 문서를 못 가져왔다.
그러면 0점 확정이 아니라 material gap pending일 수 있다.
```

## 10. 외부 리뷰어 공격 질문

다음 에이전트는 아래 질문부터 때리면 된다.

1. `FULL_THESIS` row가 실제로 몇 개인가?
2. `FULL_E2R_100` score row가 실제로 몇 개인가?
3. 삼성전자/하이닉스 row의 `operator_stage_use`가 `FULL_THESIS_STAGE`인가?
4. `samsung_hynix_full_thesis_smoke.verdict`가 `FULL_THESIS_SMOKE_PASS`인가?
5. full thesis pass라면 `full_thesis_claim_ids`, `full_thesis_score_contribution_ids`, `full_thesis_stagecourt_trace_ids`가 비어 있지 않은가?
6. 그 claim들은 `evidence_documents.jsonl`과 `evidence_anchors.jsonl`에 실제로 연결되는가?
7. source task execution의 accepted claim id와 score contribution id가 StageCourt trace까지 닫히는가?
8. snippet, source_proxy_only, memory hint가 score evidence로 섞였는가?
9. daily event score가 full thesis score로 재사용됐는가?
10. `goal_completion_audit.blockers`가 빈 배열이 된 이유가 실제 full thesis execution 때문인가, 아니면 audit label만 바꾼 것인가?
11. 전체 테스트 통과가 full thesis absence를 허용하는 테스트 통과인지, full thesis presence를 검증하는 테스트 통과인지?
12. `readiness_verdict.blockers=[]`를 최종 완료로 오독하고 있지 않은가?

## 11. 패치 전 금지 사항

다음은 하지 말아야 한다.

```text
1. 삼성전자/하이닉스 종목명 예외처리
2. C06이면 고정 query를 코드에서 deterministic 생성
3. 과거 연구 MD 점수를 그대로 현재 score로 주입
4. source_proxy_only 자료를 score evidence로 승격
5. event-board Stage를 full thesis Stage로 이름만 바꾸기
6. pending blocker를 제거하고 pass label만 바꾸기
7. `verified_score`를 EVENT_WEIGHTED_PARTIAL row에 채우기
8. Naver/news snippet만으로 claim accepted 처리
9. source task execution 없이 accepted_claim_ids만 생성
10. StageCourt trace 없이 census_stage_status만 수정
```

## 12. 완료 기준

최소 완료 기준:

```text
leaf_artifact_audit.verdict = PASS
known_bad_regression_report.status = PASS
test_result_evidence_audit.verdict = MACHINE_READABLE_TEST_ARTIFACT_PASS
brain_web_readiness_gate_audit.verdict = READY_FOR_BRAIN_WEB_EVIDENCE_PASS
samsung_hynix_full_thesis_smoke.verdict = FULL_THESIS_SMOKE_PASS
goal_completion_audit.goal_completion_ready = true
readiness_verdict.meaningful_operational_stage_pass = true
```

추가로 숫자 검산:

```text
FULL_THESIS row count >= 2 for Samsung/Hynix smoke
FULL_E2R_100 score row count >= 2 for Samsung/Hynix smoke
full_thesis_claim_ids count > 0 for each smoke symbol
full_thesis_score_contribution_ids count > 0 for each smoke symbol
full_thesis_stagecourt_trace_ids count > 0 for each smoke symbol
orphan score contribution count = 0
snippet_to_score_count = 0
source_proxy_only production contribution count = 0
daily_event/full_thesis score mixing count = 0
```

## 13. 현재 최종 판정

이번 문서화 직후 로컬에서 확인한 명령:

```bash
python -m py_compile src/e2r/census/census_runner_v4.py
PYTHONPATH=src python -m unittest tests.test_census_v4_full_thesis_smoke_tasks tests.test_census_v4_score_field_split tests.test_census_v4_stage_signal_split -v
```

결과:

```text
py_compile PASS
Ran 16 tests
OK
```

주의:

```text
이번 문서화 턴에서 전체 테스트 4976개를 새로 다시 돌린 것은 아니다.
전체 테스트 기준은 기존 machine-readable artifact인 /tmp/census_v4_after_self_repair_full_tests.json을 참조한다.
```

현재 판정:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS = true
BRAIN_WEB_EVIDENCE_PASS = true
FULL_THESIS_SMOKE_PASS = false
MEANINGFUL_OPERATIONAL_STAGE_PASS = false
GOAL_COMPLETION_READY = false
```

질문에 대한 직접 답:

```text
뭔가 잘못되고 있는가?
-> full thesis 운영 Stage 관점에서는 아직 미완성이다. 다만 anti-fake 상태판과 Brain/Web partial gate는 진전이 있다.

Stage가 있는 애들이 있긴 한가?
-> 있다. 3391개 row 중 nonzero canonical stage가 84개 있다.

그 Stage를 운영 full thesis Stage로 믿어도 되는가?
-> 아니다. FULL_THESIS는 0개이고 FULL_E2R_100 score도 0개다.
```

다음 패치는 "더 예쁘게 보고서 쓰기"가 아니다.

다음 패치는 삼성전자/하이닉스 C06/HBM smoke부터 실제 SourceTask 실행, 문서/anchor, claim, primitive, score contribution, StageCourt trace를 닫는 것이다. 이 smoke가 통과해야 그 다음에 전 아키타입 replay와 live 운영으로 넓힐 수 있다.

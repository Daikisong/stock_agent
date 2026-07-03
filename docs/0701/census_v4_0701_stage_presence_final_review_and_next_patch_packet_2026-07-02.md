# Census v4 0701 Stage Presence Final Review And Next Patch Packet

작성일: 2026-07-02  
대상 repo: `/home/eorb915/projects/stock_agent`  
대상 as_of_date: `2026-07-01`

## 한 줄 결론

```text
Stage가 아예 없는 것은 아니다.
다만 현재 대부분의 Stage는 CENSUS_EVENT_BOARD, 즉 전 종목 상태판/일일 이벤트 Stage다.
BRAIN_WEB_PARTIAL은 일부 생겼지만, FULL_THESIS 운영 Stage는 아직 0개다.
```

쉬운 예:

```text
있는 것:
전교생 출석부 + 당일 쪽지시험 성적표

조금 생긴 것:
일부 학생은 선생님이 원문 답안지를 다시 읽고 부분 성적표를 붙임

아직 없는 것:
삼성전자/하이닉스 HBM처럼 전체 논문형 시험지를 다시 채점한 full thesis 성적표
```

## 이번 문서의 목적

이 문서는 다음 에이전트가 강하게 리뷰할 수 있도록 현재 상태를 숫자와 산출물 경로로 고정한다.

확인한 질문:

```text
1. Stage가 있는 종목이 실제로 있나?
2. 그 Stage가 full thesis 운영 Stage인가, event-board 상태판 Stage인가?
3. Brain/Web/LLM 경로가 실제로 claim과 Stage row까지 붙었나?
4. leaf audit와 non-representative audit은 통과했나?
5. goal.md / goal2.md / goal3.md 기준으로 아직 무엇이 남았나?
6. 다음 패치가 정확히 어디를 향해야 하나?
```

## 기준 goal 요약

`docs/core/goal.md`의 핵심:

```text
report 문구가 아니라 leaf artifact가 source of truth다.
accepted_claim_ids / score_contribution_ids / stagecourt_trace_id가 row 내부에서 닫혀야 한다.
legacy runner가 pass를 만들면 안 된다.
```

`docs/core/goal2.md`의 핵심:

```text
LLM planner, web/news/IR/report acquisition, LLM claim extractor가 실제 leaf로 남아야 한다.
snippet이나 memory card는 점수 근거가 아니다.
provider 실패는 낮은 점수 확정이 아니라 pending이다.
```

`docs/core/goal3.md`의 핵심:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS와 MEANINGFUL_OPERATIONAL_STAGE_PASS를 분리한다.
daily event score와 full thesis score를 섞지 않는다.
삼성전자/하이닉스 C06/HBM full thesis refresh는 별도 FULL_THESIS scope로 닫아야 한다.
```

## 산출물 기준 검산

### 1. `/tmp/census_v4_enabled_after_reroute_patch`

이 실행은 Brain/Web accepted claim과 promoted row가 처음 생긴 smoke다.

주요 수치:

```text
planner_runs.jsonl:              42
source_task_executions.jsonl:   124
evidence_documents.jsonl:       116
accepted_claims.jsonl:           96
score_contributions.jsonl:      102
stagecourt_traces.jsonl:         94
brain_to_claim_trace.jsonl:       4
brain_claim_mapping_trace.jsonl:239
claim_extractor_runs.jsonl:      21
web_search_tasks.jsonl:          18
web_fetched_documents.jsonl:     21
census_stage_status.jsonl:     3391
atomic_stage_decisions.jsonl:    92
```

Brain/Web readiness:

```text
brain_web_attempt_audit.verdict: ATTEMPTED_WITH_SOURCE_TASKS
brain_web_readiness_gate_audit:  READY_FOR_BRAIN_WEB_EVIDENCE_PASS
brain_web_evidence_pass:         true
brain_stage_trace_count:         2
brain_promoted_stage_row_count:  2
```

하지만 최종 readiness:

```text
readiness_verdict: NOT_READY
leaf_artifact_audit: FAIL
non_representative_claim_audit: FAIL
```

원인:

```text
Brain/Web row가 대표 row로 올라왔는데,
같은 symbol의 기존 event-board AtomicStageDecision도 is_representative=true로 남아 있었다.
```

쉬운 예:

```text
새 성적표가 대표가 됐는데,
옛 성적표에도 대표 도장이 남아 있던 상태다.
둘 다 대표이면 감사 실패가 맞다.
```

### 2. `/tmp/census_v4_enabled_after_atomic_demotion_patch`

이 실행은 대표 row demotion 패치 후 완료된 가장 중요한 smoke다.

최종 verdict:

```text
readiness_verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
meaningful_operational_stage_pass: false
brain_web_evidence_pass: true
full_thesis_smoke_pass: false
blockers: []
```

감사 결과:

```text
leaf_artifact_audit: PASS, critical_count=0
non_representative_claim_audit: PASS, critical_count=0
brain_web_readiness_gate_audit: READY_FOR_BRAIN_WEB_EVIDENCE_PASS
```

Stage 분포:

```text
canonical_stage:
  0:      3307
  1:        53
  2:        30
  3-Red:     1
```

Stage scope:

```text
CENSUS_EVENT_BOARD: 3390
BRAIN_WEB_PARTIAL:    1
FULL_THESIS:          0
```

Score scale:

```text
NO_SCORE:               3323
EVENT_WEIGHTED_PARTIAL:   68
FULL_E2R_100:              0
```

Decision status:

```text
NO_CURRENT_CATALYST:   3306
FINAL:                   37
PENDING_MATERIAL_GAPS:   30
SOURCE_PENDING:          17
RISK_REVIEW:              1
```

Brain/Web partial row sample:

```json
{
  "symbol": "069620",
  "company_name": "대웅제약",
  "canonical_stage": "0",
  "stage_scope": "BRAIN_WEB_PARTIAL",
  "score_scale": "EVENT_WEIGHTED_PARTIAL",
  "stage_decision_status": "FINAL",
  "accepted_claim_ids": [
    "CLM-e609385041d627a383ad",
    "CLM-b340b47a79fbd8149f13"
  ],
  "stagecourt_trace_id": "SCT-BRAIN-2b8a0899950da1bbc014"
}
```

대표 demotion sample:

```json
{
  "symbol": "069620",
  "company_name": "대웅제약",
  "canonical_stage": "1",
  "stage_scope": "CENSUS_EVENT_BOARD",
  "is_representative": false,
  "representative_replaced_by": "BRAIN_WEB_PARTIAL"
}
```

해석:

```text
Stage는 있다.
하지만 대부분은 전체 상태판/일일 이벤트 Stage다.
BRAIN_WEB_PARTIAL은 생겼지만, FULL_THESIS는 아직 없다.
따라서 운영용 full thesis Green/Yellow/4B/4C 지도라고 말하면 안 된다.
```

### 3. `/tmp/census_v4_after_self_repair_full_tests.json`

최신 machine-readable 전체 테스트 artifact:

```text
status: OK
exit_code: 0
test_count: 4976
failed_count: 0
error_count: 0
duration_seconds: 161.7905
log_path: /tmp/census_v4_after_self_repair_full_tests.log
log_sha256: 000445d1c3cc6c9cf1f7db3fc6f95bc32489f83ee29d581d14cfc86ac7af4c3e
```

의미:

```text
테스트는 통과했다.
하지만 테스트 통과는 full thesis 운영 Stage가 생겼다는 뜻이 아니다.
테스트 artifact는 gate 증거 중 하나이고, Stage/full-thesis 증거는 leaf artifact로 따로 확인해야 한다.
```

### 4. `/tmp/census_v4_enabled_after_self_repair_and_trace_patch`

이 실행은 다음을 확인하려고 돌린 최신 smoke다.

```text
1. machine-readable test artifact가 goal audit에 실제로 반영되는지
2. LIVE_SOURCE_PASS verdict가 self-repair unresolved로 오인되지 않는지
3. brain_to_claim_trace에 score_eligible, score_contribution_ids, primitive_state_ids가 붙는지
4. readiness gate에 direct/rerouted claim count가 노출되는지
```

최종 실행 결과:

```text
process exit_code: 1
stdout label: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS

readiness_verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
meaningful_operational_stage_pass: false
brain_web_evidence_pass: true
full_thesis_smoke_pass: false
readiness blockers: []

goal_completion_audit.blockers:
  - full_thesis_smoke_pending

self_repair_log.status:
  RUN_COMPLETE

test_result_evidence_audit.verdict:
  MACHINE_READABLE_TEST_ARTIFACT_PASS

leaf_artifact_audit:
  PASS, critical_count=0

non_representative_claim_audit:
  PASS, critical_count=0

source_task_realness_audit:
  LIVE_SOURCE_PASS, critical_count=0

samsung_hynix_full_thesis_smoke:
  PENDING_FULL_THESIS_REFRESH
```

주의:

```text
exit_code=1은 이번 명령이 --target-gate meaningful로 실행됐기 때문이다.
meaningful_operational_stage_pass=false라서 process는 1로 끝났지만,
anti-fake 상태판 기준 verdict는 ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS가 맞다.
```

최종 leaf row count:

```text
census_stage_status.jsonl:       3391
atomic_stage_decisions.jsonl:      92
stagecourt_traces.jsonl:           93
accepted_claims.jsonl:             94
score_contributions.jsonl:         97
brain_to_claim_trace.jsonl:         2
brain_claim_mapping_trace.jsonl:  248
planner_runs.jsonl:                43
claim_extractor_runs.jsonl:        23
web_search_tasks.jsonl:            14
web_search_results.jsonl:          94
web_fetched_documents.jsonl:       23
web_rejected_documents.jsonl:       6
source_task_executions.jsonl:     126
```

최종 Stage 분포:

```text
0:      3307
1:        53
2:        30
3-Red:     1
```

최종 Stage scope:

```text
CENSUS_EVENT_BOARD: 3390
BRAIN_WEB_PARTIAL:    1
FULL_THESIS:          0
```

최종 score scale:

```text
NO_SCORE:               3324
EVENT_WEIGHTED_PARTIAL:   67
FULL_E2R_100:              0
```

Brain/Web readiness gate:

```text
verdict: READY_FOR_BRAIN_WEB_EVIDENCE_PASS
llm_planner_call_count: 43
llm_real_provider_success_count: 7
llm_claim_extractor_attempt_count: 23
llm_claim_extractor_real_provider_count: 23
naver_search_call_count: 14
web_search_task_count: 14
web_fetched_document_count: 23
web_search_result_count: 94
brain_to_claim_trace_count: 2
brain_stage_trace_count: 1
brain_promoted_stage_row_count: 1
direct_accepted_claim_count: 0
rerouted_accepted_claim_count: 2
direct_source_task_satisfied_count: 0
rerouted_source_task_claim_count: 2
snippet_to_score_count: 0
provider_failure_final_score_count: 0
fake_provider_used_count: 0
snapshot_document_count: 0
```

Brain/Web partial row sample:

```json
{
  "symbol": "001360",
  "company_name": "삼성제약",
  "canonical_stage": "0",
  "stage_scope": "BRAIN_WEB_PARTIAL",
  "score_scale": "EVENT_WEIGHTED_PARTIAL",
  "stage_decision_status": "FINAL",
  "accepted_claim_ids": [
    "CLM-8ce2cfced49daa6809ff",
    "CLM-3549cbe8671ea9ee2ac0"
  ],
  "stagecourt_trace_id": "SCT-BRAIN-c13b78b6b8115be04788"
}
```

중요 해석:

```text
이번 실행으로 machine-readable test artifact와 self-repair blocker는 닫혔다.
즉 이전 goal_completion_audit에 있던
machine_readable_test_result_artifact_missing,
self_repair_unresolved_failures는 더 이상 남지 않는다.

남은 blocker는 full_thesis_smoke_pending 하나다.
```

## 현재 패치가 해결한 것

### 1. Rerouted claim 보존

패치 파일:

```text
src/e2r/research_brain/v4_schemas.py
src/e2r/research_brain/v4_evidence_extraction_bridge.py
```

추가 의미:

```text
DIRECT_ACCEPTED_CLAIM
= SourceTask가 찾으려던 primitive gap을 직접 채움

REROUTED_ACCEPTED_CLAIM
= 다른 유효 primitive claim이 나와서 점수 근거로 보존하지만,
  원래 SourceTask gap을 직접 닫은 것은 아님
```

쉬운 예:

```text
찾던 것: FCF bridge
문서에서 나온 것: 고객 배정 claim

이전 처리:
"FCF가 아니니 폐기"

현재 처리:
"고객 배정 claim으로 보존하되, FCF gap은 아직 미충족"
```

### 2. 대표 row demotion

패치 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_non_representative_claim_audit.py
```

해결한 문제:

```text
Brain/Web row가 대표 row로 승격된 뒤에도
기존 event-board AtomicStageDecision이 representative=true로 남던 문제를 막았다.
```

### 3. trace chain 강화

패치 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_bundle_export.py
tests/test_census_v4_brain_web_readiness_gate.py
```

강화한 필드:

```text
brain_to_claim_trace.score_eligible
brain_to_claim_trace.score_contribution_ids
brain_to_claim_trace.primitive_state_ids
brain_web_readiness_gate.direct_accepted_claim_count
brain_web_readiness_gate.rerouted_accepted_claim_count
brain_web_readiness_gate.direct_source_task_satisfied_count
brain_web_readiness_gate.rerouted_source_task_claim_count
```

의미:

```text
"claim이 있었다"에서 끝내지 않고,
그 claim이 실제 점수 contribution과 primitive state까지 연결됐는지 볼 수 있게 했다.
```

### 4. self-repair verdict 판정 수정

패치 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_goal_required_audits.py
```

문제:

```text
SOURCE_TASK_REALNESS_AUDIT가 LIVE_SOURCE_PASS를 냈는데,
기존 self-repair 판정은 PASS / PASS_*만 통과로 봐서 unresolved failure로 남겼다.
```

수정:

```text
*_PASS와 LIVE_SOURCE_PASS 계열을 audit pass로 인정하는 헬퍼를 추가했다.
```

쉬운 예:

```text
시험 결과표에 "실전 출처 통과"라고 적혀 있는데,
코드가 "PASS"라는 단어로만 시작해야 합격이라고 보던 문제다.
```

## 아직 해결되지 않은 것

### 1. FULL_THESIS 운영 Stage가 없다

가장 큰 남은 문제:

```text
FULL_THESIS: 0
FULL_E2R_100: 0
full_thesis_smoke_pass: false
meaningful_operational_stage_pass: false
```

이 상태에서 아래처럼 말하면 안 된다.

```text
삼성전자 C06/HBM 운영 Stage가 확정됐다.
SK하이닉스 C06/HBM 운영 Stage가 확정됐다.
전체 KRX의 full thesis score/stage가 완성됐다.
```

올바른 표현:

```text
전체 상태판과 event-board Stage는 있다.
Brain/Web partial trace는 일부 생겼다.
하지만 full thesis 운영 Stage는 아직 pending이다.
```

### 2. Brain/Web partial은 full thesis가 아니다

`BRAIN_WEB_PARTIAL`은 중요하지만, full thesis가 아니다.

쉬운 예:

```text
BRAIN_WEB_PARTIAL:
원문 몇 개를 읽고 특정 claim 몇 개를 점수표에 붙인 부분 성적표

FULL_THESIS:
아키타입 전체 evidence contract를 놓고
필수 primitive, gate, 반론, lifecycle, source quorum까지 확인한 전체 성적표
```

### 3. 현재 smoke가 끝나기 전까지 최신 self-repair / artifact 반영은 미확정

최신 smoke에서 확인된 상태:

```text
test_result_evidence_audit.verdict = MACHINE_READABLE_TEST_ARTIFACT_PASS
self_repair_log.status = RUN_COMPLETE
goal_completion_audit.blockers = ["full_thesis_smoke_pending"]
```

즉 이 부분은 해결됐다.
이제 최신 blocker는 full thesis 하나로 수렴했다.

계속 확인해야 할 파일:

```text
/tmp/census_v4_enabled_after_self_repair_and_trace_patch/readiness_verdict.json
/tmp/census_v4_enabled_after_self_repair_and_trace_patch/goal_completion_audit.json
/tmp/census_v4_enabled_after_self_repair_and_trace_patch/samsung_hynix_full_thesis_smoke.json
```

만약 다음 패치 후에도 `samsung_hynix_full_thesis_smoke.verdict`가
`PENDING_FULL_THESIS_REFRESH`이면 meaningful pass를 말하면 안 된다.

## 다음 에이전트 공격 질문

다음 에이전트는 아래 질문부터 공격하면 된다.

```text
1. latest smoke에서 goal_completion_audit.blockers가 왜 full_thesis_smoke_pending 하나만 남았나?
2. self_repair_log.status가 RUN_COMPLETE이고 unresolved failure 0이 맞나?
3. test_result_evidence_audit가 STRING_SUMMARY_ONLY가 아니라 MACHINE_READABLE_TEST_ARTIFACT_PASS를 봤나?
4. brain_to_claim_trace의 score_contribution_ids가 실제 score_contributions.jsonl에 존재하나?
5. rerouted claim이 원래 primitive gap을 해결한 것처럼 과장 집계되지 않나?
6. BRAIN_WEB_PARTIAL row 승격 시 기존 event-board representative가 확실히 내려가나?
7. FULL_THESIS scope row가 0인 상태에서 meaningful_operational_stage_pass가 true가 되는 경로는 없나?
8. 삼성전자/하이닉스 smoke는 daily event와 분리된 FULL_THESIS row를 만들고 있나?
9. provider failure가 low score / Red로 확정되는 경로는 없는가?
10. score scale이 EVENT_WEIGHTED_PARTIAL인데 FULL_E2R_100처럼 비교되는 경로는 없는가?
```

## 다음 패치 방향

### P0. 최신 smoke blocker는 full thesis 하나로 수렴했는지 계속 고정

현재 확인값:

```text
goal_completion_audit.blockers = ["full_thesis_smoke_pending"]
self_repair_log.status = RUN_COMPLETE
test_result_evidence_audit.verdict = MACHINE_READABLE_TEST_ARTIFACT_PASS
```

이 값을 다음 패치 전 baseline으로 둔다.

계속 유지해야 하는 성공 기준:

```text
machine_readable_test_result_artifact_missing 없음
self_repair_unresolved_failures 없음
leaf_artifact_audit PASS
non_representative_claim_audit PASS
brain_web_evidence_pass true 유지
```

### P1. FULL_THESIS smoke를 실제 실행으로 바꾸기

현재 가장 중요한 미완성은 full thesis다.

필요한 구조:

```text
삼성전자/하이닉스 같은 controlled target
→ daily event row와 별도 FULL_THESIS SourceTask 생성
→ official-first bounded acquisition
→ 필요 시 web/news/IR/report bounded fallback
→ LLM claim extractor / structured official extractor
→ Evidence OS accepted claim
→ primitive state
→ score contribution
→ StageCourt trace
→ stage_scope=FULL_THESIS row
```

주의:

```text
심볼명을 scoring/staging/red-team 조건문에 넣으면 안 된다.
smoke target 선택은 가능하지만 점수 로직 예외는 금지다.
```

쉬운 예:

```text
허용:
"이번 smoke 대상은 005930, 000660으로 선택한다."

금지:
"if symbol == '005930': accounting risk 무시"
"if symbol == '000660': C06 점수 가산"
```

### P2. FULL_THESIS 결과의 정직한 상태 구분

full thesis를 실행했는데 증거가 부족하면 낮은 점수로 확정하지 않는다.

올바른 상태:

```text
accepted claim 충분:
  FULL_THESIS + FINAL

material gap 남음:
  FULL_THESIS + PENDING_MATERIAL_GAPS

provider/source 실패:
  FULL_THESIS + PROVIDER_PENDING 또는 SOURCE_PENDING
```

금지:

```text
증거 부족 → 0점 Red
provider 실패 → Stage0 확정
old negative 기사 하나 → 4C 확정
```

### P3. meaningful gate는 마지막에만 true

`MEANINGFUL_OPERATIONAL_STAGE_PASS`는 아래가 모두 닫혀야 true다.

```text
1. leaf_artifact_audit PASS
2. non_representative_claim_audit PASS
3. machine-readable full test artifact PASS
4. self-repair unresolved failure 0
5. Brain/Web evidence pass
6. FULL_THESIS smoke pass
7. known-bad regression pass
8. score scale / stage scope 혼동 없음
```

하나라도 빠지면 다음처럼 써야 한다.

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
meaningful_operational_stage_pass=false
```

## 현재 문서 기준 최종 판정

```text
Stage가 있는 애들은 있다.
하지만 지금 Stage 대부분은 전 종목 상태판/일일 이벤트 Stage다.
Brain/Web partial Stage도 일부 생겼고 leaf audit까지 통과한 smoke가 있다.
그러나 FULL_THESIS 운영 Stage는 아직 0개다.
따라서 현재는 "잘못돼서 아무것도 없는 상태"가 아니라,
"가짜 완료 선언은 막았지만 full thesis 운영 실행이 아직 남은 상태"다.
```

다음 패치의 목표는 점수를 억지로 올리는 것이 아니다.

```text
daily event 상태판
Brain/Web partial 판단
FULL_THESIS 운영 판단
```

이 세 층을 끝까지 분리하고, FULL_THESIS 층에서 source-backed claim으로 StageCourt까지 닫는 것이다.

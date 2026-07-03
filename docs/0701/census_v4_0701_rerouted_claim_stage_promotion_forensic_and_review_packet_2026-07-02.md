# Census v4 0701 Rerouted Claim / Stage Promotion Forensic And Review Packet

작성일: 2026-07-02  
대상 repo: `/home/eorb915/projects/stock_agent`  
대상 실행일: `as_of_date=2026-07-01`

## 한 줄 결론

```text
이전에는 Brain/Web이 실제로 돌았어도 accepted claim이 0개였다.
이번 패치 후에는 Brain/Web accepted claim 4개, Brain StageCourt trace 2개, promoted Brain row 2개까지 처음으로 생겼다.
하지만 아직 MEANINGFUL_OPERATIONAL_STAGE_PASS는 아니다.
```

쉬운 예:

```text
전 상태:
출석부는 3391명 있는데, 실제 답안지가 붙은 새 Brain/Web 학생은 0명.

이번 상태:
새 Brain/Web 답안지 4장이 들어왔고, 그중 2개 종목이 대표 성적표 후보로 올라왔다.

아직 아닌 것:
전교생 종합성적표 합격, 삼성전자/하이닉스 HBM full thesis 확정, Green/Yellow 운영 판정.
```

## 이번 작업의 정확한 범위

이번 패치는 scoring weight, Stage threshold, 종목별 예외를 건드리지 않았다.

고친 것은 증거 배관이다.

```text
1. SourceTask primitive가 달라도 contract 안의 유효 claim은 버리지 않는다.
2. 단, 원래 SourceTask gap을 직접 채웠는지와 다른 primitive로 reroute됐는지를 분리한다.
3. planner feedback retry가 primary archetype을 바꾸면 새 archetype contract로 다시 실행할 수 있게 한다.
4. Brain/Web row가 대표 stage row로 승격되면, 기존 event-board AtomicStageDecision 대표 표시는 내려야 한다.
5. brain_to_claim_trace에도 score_eligible, score_contribution_ids, primitive_state_ids를 명시한다.
6. Brain/Web readiness gate에 direct/rerouted accepted claim 수와 direct/rerouted source task 수를 노출한다.
```

쉬운 예:

```text
원래 창구:
"medium_term_revision_visibility 서류만 받습니다"

실제 문서:
"HBM 고객 배정/qualification이 확인됩니다"

나쁜 처리:
"창구가 다르니 폐기"

현재 처리:
"점수 근거로는 보존하되, 원래 gap을 직접 채운 것은 아니므로 REROUTED_ACCEPTED_CLAIM으로 표시"
```

## 핵심 패치 파일

```text
src/e2r/research_brain/v4_schemas.py
src/e2r/research_brain/v4_evidence_extraction_bridge.py
src/e2r/research_brain/v4_production_orchestrator.py
src/e2r/census/census_runner_v4.py

tests/test_research_brain_v4_evidence_extraction_from_real_document.py
tests/test_research_brain_v4_operational_modes.py
tests/test_census_v4_non_representative_claim_audit.py
tests/test_census_v4_brain_bundle_export.py
```

## 새로 생긴 trace 의미

`SourceTaskExecutionV4`에 아래 필드를 추가했다.

```text
satisfies_source_task
satisfaction_type
direct_accepted_claim_ids
rerouted_accepted_claim_ids
score_claim_ids
accepted_primitive_ids
primitive_gap_satisfied_ids
primitive_gap_unsatisfied_ids
```

의미:

```text
DIRECT_ACCEPTED_CLAIM
= 이 SourceTask가 찾으려던 primitive gap을 직접 채웠다.

REROUTED_ACCEPTED_CLAIM
= 원문 claim은 유효하고 contract primitive에 매핑됐지만, 원래 SourceTask gap은 아직 못 채웠다.

NO_EVIDENCE_FOUND
= fetch/parse/검증을 했지만 점수 가능한 claim이 없다.

PROVIDER_FAILED
= LLM extractor/provider 자체가 실패했다. 낮은 점수로 확정하면 안 된다.
```

이 분리가 중요한 이유:

```text
rerouted claim은 버리면 안 된다.
하지만 rerouted claim을 원래 gap 해결로 세면 안 된다.
```

예:

```text
SourceTask: FCF bridge 확인
문서: 고객 배정 확인

이 문서는 점수 근거가 될 수 있지만,
FCF bridge를 닫은 것은 아니다.
```

## 첫 enabled smoke 결과

출처:

```text
/tmp/census_v4_enabled_after_reroute_patch
```

주요 결과:

```text
planner_runs.jsonl:             42
source_tasks.jsonl:             124
source_task_executions.jsonl:   124
evidence_documents.jsonl:       116
evidence_anchors.jsonl:         135
raw_assertions.jsonl:           299
adjudicated_claims.jsonl:       325
accepted_claims.jsonl:           96
score_contributions.jsonl:      102
primitive_states.jsonl:         104
stagecourt_traces.jsonl:         94
brain_to_claim_trace.jsonl:       4
brain_claim_mapping_trace.jsonl: 239
claim_extractor_runs.jsonl:      21
web_search_tasks.jsonl:          18
web_search_results.jsonl:       118
web_fetched_documents.jsonl:     21
web_rejected_documents.jsonl:    34
census_stage_status.jsonl:     3391
atomic_stage_decisions.jsonl:    92
```

Brain/Web attempt:

```text
brain_web_attempt_audit.verdict: ATTEMPTED_WITH_SOURCE_TASKS
accepted_claim_count:            4
brain_to_claim_trace_count:      4
real_provider_success_count:     6
source_task_execution_count:     32
real_document_fetched_count:     47
planner_run_count:               42
blockers:                        []
```

Brain/Web readiness gate:

```text
verdict:                         READY_FOR_BRAIN_WEB_EVIDENCE_PASS
brain_web_evidence_pass:          true
brain_stage_trace_count:          2
brain_promoted_stage_row_count:   2
source_task_execution_count:      32
real_document_fetched_count:      24
llm_claim_extractor_attempt_count:21
web_search_task_count:            18
web_fetched_document_count:       21
```

Stage scope:

```text
CENSUS_EVENT_BOARD: 3389
BRAIN_WEB_PARTIAL:    2
FULL_THESIS:          0
```

Canonical stage:

```text
0:      3308
1:        52
2:        30
3-Red:     1
```

중요:

```text
BRAIN_WEB_PARTIAL 2개는 full thesis Stage가 아니다.
EVENT_WEIGHTED_PARTIAL / BRAIN_WEB_CLAIM_BACKED_PARTIAL이다.
```

## 첫 smoke가 실패한 이유

최종 readiness:

```text
readiness_verdict: NOT_READY
meaningful_operational_stage_pass: false
brain_web_evidence_pass: true
full_thesis_smoke_pass: false
blockers:
  - leaf artifact audit failed
```

Leaf audit critical:

```text
leaf_artifact_audit.verdict: FAIL
critical_count: 1
non_representative_claim_audit_failed_count: 1
```

Non-representative audit critical:

```text
non_representative_claim_audit.verdict: FAIL
representative_atomic_claim_not_in_stage_row_count: 1
```

해석:

```text
Brain/Web row가 대표 census_stage_status row로 승격됐는데,
같은 symbol의 이전 event-board AtomicStageDecision도 is_representative=true로 남아 있었다.
```

쉬운 예:

```text
새 담임 선생님 성적표가 대표 성적표가 됐는데,
옛 담임 선생님 성적표도 아직 "대표" 도장이 찍힌 상태.

둘 중 하나만 대표여야 한다.
둘 다 대표이면 감사가 실패하는 게 맞다.
```

## 이 실패에 대한 패치

파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_non_representative_claim_audit.py
```

추가 함수:

```text
_demote_atomic_representatives_replaced_by_brain_stage
```

동작:

```text
stage_scope=BRAIN_WEB_PARTIAL 또는 CSS-BRAIN-* row가 대표 stage row가 되면,
같은 symbol의 기존 AtomicStageDecision 중 is_representative=true를 false로 내린다.
```

남기는 장부:

```text
representative_replaced_by: BRAIN_WEB_PARTIAL
non_representative_reason: superseded_by_promoted_brain_web_stage_row
```

즉 기존 atomic row를 삭제하지 않는다.
대표에서만 내린다.

## brain_to_claim_trace 보강 패치

첫 smoke 산출물에서 발견한 추가 약점:

```text
brain_claim_mapping_trace에는 score_contribution_ids 전체 목록이 있었다.
brain_to_claim_trace에는 score_contribution_id 단일 값만 있었다.
```

기존 audit는 단일 값만으로 subset 검증이 가능했지만, 다음 리뷰어가 보면 claim-to-score trace가 반쪽으로 보일 수 있다.

패치:

```text
brain_to_claim_trace row에 아래를 추가한다.

score_eligible
score_contribution_ids
primitive_state_ids
```

주의:

```text
score_eligible은 항상 true가 아니다.
accepted claim이라도 snapshot/source-gap 성격이면 score_eligible=false일 수 있다.
따라서 trace는 accepted_claim payload의 score_eligible 값을 그대로 복사해야 한다.
```

테스트:

```text
tests/test_census_v4_brain_bundle_export.py
```

## Brain/Web readiness direct/rerouted count 보강

추가 약점:

```text
accepted_claim_count 하나만 보면 direct claim과 rerouted claim이 섞인다.
```

패치:

```text
brain_web_readiness_gate_audit에 아래 필드를 추가한다.

direct_accepted_claim_count
rerouted_accepted_claim_count
direct_source_task_satisfied_count
rerouted_source_task_claim_count
```

의미:

```text
direct_accepted_claim_count
= 원래 SourceTask primitive gap을 직접 채운 accepted claim 수

rerouted_accepted_claim_count
= 유효한 claim이지만 원래 SourceTask gap이 아니라 다른 contract primitive로 매핑된 claim 수
```

이 필드는 아직 pass/fail 조건을 바꾸지 않는다.  
이번 단계의 목적은 숨기지 않는 것이다.

## Targeted 테스트 결과

실행:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_non_representative_claim_audit -v
```

결과:

```text
Ran 49 tests in 7.987s
OK
```

## 전체 테스트 결과

실행:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 4975 tests in 159.918s
OK
```

주의:

```text
전체 테스트 OK는 코드 회귀가 없다는 뜻이다.
MEANINGFUL_OPERATIONAL_STAGE_PASS가 true라는 뜻은 아니다.
```

이전 관련 targeted 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_bundle_export \
  tests.test_census_v4_brain_web_readiness_gate -v
```

결과:

```text
Ran 38 tests
OK
```

## atomic representative demotion 후 재검증 결과

다음 smoke는 atomic representative demotion 패치 후 실행했다.

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --mode HYBRID_CENSUS \
  --brain-web-mode enabled \
  --brain-planner-provider real \
  --brain-source-acquisition live_full_bounded \
  --brain-claim-extractor-provider auto \
  --brain-universe-limit 8 \
  --brain-planner-success-limit 4 \
  --brain-planner-batch-size 2 \
  --brain-max-fetches-per-task 2 \
  --brain-stage-promotion-mode strict \
  --target-gate meaningful \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim true \
  --fail-on-atomic-mismatch true \
  --fail-on-semantic-guard true \
  --output-root /tmp/census_v4_enabled_after_atomic_demotion_patch
```

결과:

```text
exit code: 1
stdout: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS

readiness_verdict.verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
meaningful_operational_stage_pass: false
brain_web_evidence_pass: true
full_thesis_smoke_pass: false
readiness_verdict.blockers: []

goal_completion_audit.blockers:
  - full_thesis_smoke_pending
  - self_repair_unresolved_failures
  - machine_readable_test_result_artifact_missing
```

핵심 감사:

```text
leaf_artifact_audit.verdict: PASS
leaf_artifact_audit.critical_count: 0

non_representative_claim_audit.verdict: PASS
non_representative_claim_audit.critical_count: 0
representative_atomic_claim_not_in_stage_row_count: 0
```

Brain/Web 결과:

```text
brain_web_attempt_audit.verdict: ATTEMPTED_WITH_SOURCE_TASKS
accepted_claim_count: 2
brain_to_claim_trace_count: 2
real_provider_success_count: 7
source_task_execution_count: 34
real_document_fetched_count: 52
planner_run_count: 43

brain_web_readiness_gate_audit.verdict: READY_FOR_BRAIN_WEB_EVIDENCE_PASS
brain_stage_trace_count: 1
brain_promoted_stage_row_count: 1
web_search_task_count: 16
web_fetched_document_count: 27
llm_claim_extractor_attempt_count: 27
```

Stage scope:

```text
CENSUS_EVENT_BOARD: 3390
BRAIN_WEB_PARTIAL:    1
FULL_THESIS:          0
```

대표 Brain row:

```text
symbol: 069620
company_name: 대웅제약
stage_scope: BRAIN_WEB_PARTIAL
canonical_stage: 0
accepted_claim_ids:
  - CLM-e609385041d627a383ad   DIRECT_ACCEPTED_CLAIM
  - CLM-b340b47a79fbd8149f13   REROUTED_ACCEPTED_CLAIM
stagecourt_trace_id: SCT-BRAIN-2b8a0899950da1bbc014
primitive_state_ids:
  - PRIM-BRAIN-7a10188c60893860f976
atomic representative replaced count: 1
```

이 smoke는 `brain_to_claim_trace` plural field와 readiness direct/rerouted count 패치 전에 시작됐으므로, 아래 필드는 아직 이 output에는 없다.

```text
brain_to_claim_trace.score_eligible
brain_to_claim_trace.score_contribution_ids
brain_web_readiness_gate.direct_accepted_claim_count
brain_web_readiness_gate.rerouted_accepted_claim_count
```

따라서 plural trace/count 패치까지 증명하려면 새 output root로 한 번 더 돌려야 한다.

## 교차검증 결과

기존 열린 subagent들의 read-only 검토 결과와 로컬 재검산을 반영했다.

### 해결된 지적

1. rejected mapping row가 score eligible처럼 보일 위험

현재 코드:

```text
score_eligible = accepted and not eligibility_reasons
```

따라서 rejected row는 eligibility reason이 비어 있어도 score eligible이 될 수 없다.

2. promoted brain_to_claim_trace가 stage row와 claim만 맞고 contribution/primitive는 안 맞을 위험

현재 코드:

```text
_brain_trace_promoted_reference_error_count
```

에서 아래 subset을 모두 검사한다.

```text
stagecourt_trace_id
accepted_claim_ids
score_contribution_ids
primitive_state_ids
```

3. Brain partial row에 `atomic_stage_decision_id=None`인 경우 primitive chain audit가 무조건 실패할 위험

현재 코드:

```text
stage_scope == BRAIN_WEB_PARTIAL
```

이면 `atomic_stage_decision_id`가 없어도 primitive_state_ids를 직접 chain으로 인정한다.

4. Brain/Web row가 대표가 됐는데 기존 atomic representative가 같이 남는 위험

이번 패치:

```text
_demote_atomic_representatives_replaced_by_brain_stage
```

로 내린다.

### 아직 남은 리스크

1. Web fetch target guard는 주체 판정이 아니다.

현재 guard는 본문 앞쪽에 target alias가 있는지를 본다.

```text
좋은 점:
검색 메타에만 target이 있고 본문에는 target이 없으면 reject한다.

남은 위험:
본문에 target이 고객사/공급사/비교대상으로 언급되면 fetch는 통과할 수 있다.
```

쉬운 예:

```text
월덱스 기사 본문에 "주요 고객사는 삼성전자"가 있으면
fetch guard는 통과할 수 있다.
하지만 이것은 삼성전자의 회계/계약 claim이 아니다.
최종 scoring은 adjudicator의 DIRECT target check가 막아야 한다.
```

다음 패치 방향:

```text
fetch guard는 "문서 후보"만 줄이고,
score gate는 반드시 claim-level target_scope_status=DIRECT, directness=DIRECT, semantic_status=PASS를 요구한다.
또한 web_fetched_document_count를 readiness positive evidence로 과하게 읽지 않게 해야 한다.
```

2. Rerouted accepted claim이 Brain/Web pass를 과장할 수 있다.

현재는 direct/rerouted가 분리되어 있지만, readiness 문구가 `accepted_claim_count=4`만 앞세우면 과장될 수 있다.

다음 패치 방향:

```text
Brain/Web readiness report에 direct_accepted_claim_count와 rerouted_accepted_claim_count를 따로 노출한다.
Green/full thesis gate에는 직접 채운 required primitive와 rerouted primitive를 분리해 사용한다.
```

3. Brain/Web partial stage는 full thesis가 아니다.

이번 smoke의 `BRAIN_WEB_PARTIAL=2`는 중요하지만, 삼성전자/하이닉스 HBM full thesis 같은 운영 판정과 다르다.

다음 패치 방향:

```text
FULL_THESIS_REFRESH_PASS를 별도 smoke로 닫는다.
삼성전자/하이닉스는 daily event row와 C06/HBM full thesis row를 절대 같은 필드에 섞지 않는다.
```

4. 이번 smoke는 `meaningful` target으로 실행 중이지만, `full_thesis_smoke_pass=false`가 남으면 정상적으로 NOT_READY여야 한다.

즉 Brain/Web evidence pass가 true여도 아래가 false면 완료가 아니다.

```text
MEANINGFUL_OPERATIONAL_STAGE_PASS
FULL_THESIS_SMOKE_PASS
FULL_E2R_100 verified score
```

## 다음 에이전트 공격 질문

다음 리뷰어는 아래 질문부터 공격하면 된다.

```text
1. /tmp/census_v4_enabled_after_atomic_demotion_patch의 leaf_artifact_audit critical_count가 0인가?
2. non_representative_claim_audit의 representative_atomic_claim_not_in_stage_row_count가 0으로 내려갔는가?
3. Brain/Web promoted row 2개가 여전히 있고, 기존 event-board representative는 정상적으로 demoted됐는가?
4. brain_to_claim_trace에 score_eligible, score_contribution_ids, primitive_state_ids가 모두 들어가는가?
5. Brain/Web accepted claim 4개 중 direct/rerouted 비율은 무엇인가?
6. rerouted claim을 원래 SourceTask gap 해결로 잘못 계산한 곳은 없는가?
7. web_fetched_document_count를 source-backed score evidence처럼 읽는 report 문구는 없는가?
8. BRAIN_WEB_PARTIAL을 FULL_THESIS나 FULL_E2R_100으로 읽게 만드는 operator alias가 없는가?
9. 삼성전자/하이닉스 HBM/C06 full thesis smoke는 여전히 pending이라고 정직하게 표시되는가?
10. 전체 테스트를 다시 돌렸는가?
```

## 다음 패치 순서

P0. 현재 실행 중인 smoke 완료 후 artifact 재검산

```text
root: /tmp/census_v4_enabled_after_atomic_demotion_patch
필수:
  leaf_artifact_audit.critical_count == 0
  non_representative_claim_audit.critical_count == 0
  brain_web_evidence_pass == true 또는 blocker 명시
```

P1. plural `brain_to_claim_trace` 패치 반영 후 같은 smoke 재실행

```text
현재 실행은 이 패치 전에 시작됐다.
따라서 이 필드까지 증명하려면 새 output root로 다시 돌려야 한다.
```

P2. Direct vs rerouted readiness summary 추가

```text
Brain/Web readiness에서:
  direct_accepted_claim_count
  rerouted_accepted_claim_count
  direct_source_task_satisfied_count
  rerouted_source_task_claim_count
를 분리한다.
```

P3. Web fetch target guard를 overclaim하지 않도록 report 문구 보정

```text
web fetch 통과 = 문서 후보 통과
claim score 통과 = claim-level DIRECT/semantic/current 검증 통과
```

P4. Samsung/Hynix C06/HBM full thesis smoke

```text
daily event row와 별도로 full thesis SourceTask를 열고,
claim-backed score/stage 또는 material pending을 남긴다.
```

P5. 전체 테스트와 external review packet 갱신

```text
PYTHONPATH=src python -m unittest discover -s tests -v
```

## 최종 판정

현재 결론:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS: 기존 범위에서 유지 가능
BRAIN_WEB_EVIDENCE_PASS: 첫 smoke 기준 true까지 진전
MEANINGFUL_OPERATIONAL_STAGE_PASS: 아직 false
FULL_THESIS_SMOKE_PASS: 아직 false
READY_FOR_OPERATIONAL_STAGE_USE: 아직 false
```

이 문서의 핵심은 “이번에 좋아졌다”가 아니라 아래다.

```text
Brain/Web이 0개였던 병목은 일부 풀렸다.
하지만 full thesis 운영 Stage를 말할 수 있는 상태는 아니다.
대표 row, direct/rerouted, trace contribution, target subject guard를 더 닫아야 한다.
```

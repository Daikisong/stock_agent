# E2R Reconstruction Phase 0 Baseline

## 상태

Phase 0의 목적은 기존 Goal4 결과를 폐기하는 것이 아니라, 증명 범위를 정확히 낮춰 안전한 출발점을 만드는 것이다.

공식 상태:

    MEANINGFUL_RUNTIME_PARITY_NOT_READY

## 보존한 사실

- 현재 promoted production FULL_THESIS row는 0개다.
- 현재 full E2R verified score row는 0개다.
- 11,394 research_reverse record를 meaningful semantic case로 부르지 않는다.
- 1,855 source route pattern을 recovered executable route로 부르지 않는다.
- 111 seed/task shell을 evidence로 부르지 않는다.
- historical replay 결과를 current watchlist row로 승격하지 않는다.
- report label을 READY로 올리지 않는다.

## 재분류

| 대상 | 분류 |
|---|---|
| Evidence OS document/anchor/claim/eligibility | VALID_SAFETY_INFRASTRUCTURE |
| deterministic scorer / canonical Stage | VALID_DETERMINISTIC_SCORING_INFRASTRUCTURE |
| 36개 기존 MemoryCard | PROVISIONAL_RESEARCH_MEMORY |
| research_reverse case inventory | HEURISTIC_RESEARCH_REVERSE |
| primitive-name source route matrix | HEURISTIC_SOURCE_ROUTE |
| 7월 진행 보고서와 next-attempt manifest | REPORT_OR_PLAN_ONLY |
| 최신 Census leaf output | RUNTIME_PROOF |
| v2/v3 Brain/Census CLI | DEPRECATED |
| controlled smoke/replay | TEST_ONLY |

상세 machine-readable 분류는 e2r_legacy_artifact_classification.json에 기록했다.

## 안전 인프라와 readiness의 분리

현재 시스템은 다음을 증명한다.

- real provider planner 호출 가능
- bounded source task 실행 가능
- full document fetch 가능
- contract-blind claim과 anchor 생성 가능
- primitive mapping과 StageCourt trace 생성 가능
- snippet/proxy/fake provider score leak 방어 존재

현재 시스템은 다음을 증명하지 못한다.

- historical case 의미 100% 보존
- case-level URL/anchor 검증
- recipe 기반 direct question closure
- balanced semantic retrieval benchmark
- current production full-thesis
- historical/current 완전 분리

쉬운 예: 수도관, 밸브, 계량기가 각각 작동한다는 시험은 통과했지만, 취수원에서 가정까지 한 경로로 깨끗한 물이 도달한다는 통합 증명은 아직 없다.

## 현재 failure cluster

가장 큰 구조적 실패는 task 개수 부족이 아니다.

    historical case
      -> verified source
      -> executable recipe
      -> question-specific task
      -> direct accepted claim
      -> original primitive closure

이 연결 identity가 없다. 그래서 generic fact, stale fact, wrong-subject fact, rerouted primitive가 중간 progress로 집계될 수 있다.

## Phase 0 산출물

- e2r_reconstruction_forensic_baseline.md
- e2r_runtime_call_graph_before.json
- e2r_duplicate_brain_stack_inventory.json
- e2r_current_conversion_funnel_baseline.json
- e2r_legacy_artifact_classification.json
- e2r_reconstruction_master_plan.md

## Acceptance

| 조건 | 결과 |
|---|---|
| 11,394 record를 meaningful case로 간주하지 않음 | PASS |
| 1,855 pattern을 recovered route로 간주하지 않음 | PASS |
| 111 task shell을 evidence로 간주하지 않음 | PASS |
| promoted full thesis 0개 보존 | PASS |
| official verdict NOT_READY 보존 | PASS |
| report label 상향 없음 | PASS |

Phase 1은 src/e2r/research_brain을 유일한 canonical intelligence namespace로 만들고, legacy reverse/routing을 compatibility adapter로 내리는 작업부터 시작한다.

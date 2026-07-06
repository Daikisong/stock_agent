# Goal4 Score Path Split Final Handoff - 2026-07-05

작성 시점: 2026-07-07 KST

이 문서는 2026-07-05 기준 Goal4 연구자료 -> runtime parity 작업의 최신 handoff다.

핵심 결론:

```text
Goal4는 아직 완료가 아니다.
PRODUCTION_FULL_E2R_SCORE_PATH_PASS = true
MEANINGFUL_FULL_THESIS_EVIDENCE_PASS = false
```

쉬운 예:

```text
7개 과목은 채점표가 만들어졌다.
하지만 7개 모두 필수 증빙 서류와 Green 증빙 서류가 빠져 있다.
그래서 "채점 경로가 작동함"은 맞지만 "운영 합격"은 아니다.
```

## Canonical 최신 산출물

현재 최신 판정은 아래 파일을 기준으로 본다.

```text
docs/operational/research_to_runtime_acceptance_report.md
docs/operational/research_to_runtime_readiness_verdict.md
docs/operational/research_to_runtime_parity_matrix_2026-07-05.json
docs/operational/all_archetype_runtime_status_matrix_2026-07-05.json
docs/operational/all_archetype_runtime_status_matrix_2026-07-05.md
docs/operational/all_archetype_next_runtime_attempt_plan_2026-07-05.json
docs/operational/research_to_runtime_root_cause_2026-07-05.md
```

이 문서보다 오래된 `docs/0705` 문서 중 C05 10개, row 3개, row 4개를 말하는 문서는 당시 스냅샷이다. 최신 운영 판정은 위 canonical 파일과 이 handoff를 우선한다.

## 현재 숫자

```text
final_status = MEANINGFUL_RUNTIME_PARITY_NOT_READY
production_full_e2r_score_path_pass = true
meaningful_full_thesis_evidence_pass = false
archetype_balanced_full_thesis_pass = true

full_thesis_row_count = 7
distinct_full_thesis_archetype_count = 7
c05_full_thesis_share = 0.142857

required_positive_missing_full_thesis_row_count = 7
green_gap_full_thesis_row_count = 7

target_archetype_unknown_promoted_count = 0
source_primary_context_promoted_count = 0
```

Promoted score-path rows:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE = 1
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG = 1
C05_EPC_MEGA_CONTRACT_MARGIN_GAP = 1
C06_HBM_MEMORY_CUSTOMER_CAPACITY = 1
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY = 1
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD = 1
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION = 1
```

Mandatory canary 상태:

```text
C06 = production score path row 있음, meaningful gap 있음
C08 = production score path row 있음, meaningful gap 있음
C15 = mandatory full-thesis row 없음
C17 = production score path row 있음, meaningful gap 있음
C24 = mandatory full-thesis row 없음
C28 = production score path row 있음, meaningful gap 있음
```

## 왜 아직 미완료인가

Blocker:

```text
GREEN_GAP_ON_PROMOTED_ROWS
MANDATORY_ARCHETYPE_FULL_THESIS_ROW_MISSING
PRODUCTION_SCORE_PATH_IS_NOT_MEANINGFUL_FULL_THESIS_PASS
REQUIRED_POSITIVE_MISSING_ON_PROMOTED_ROWS
```

의미:

```text
점수 계산기는 작동한다.
하지만 점수 칸에 들어간 claim이 아키타입 required-positive와 Green gate를 충분히 닫지 못했다.
따라서 Stage/score를 운영 합격처럼 말하면 안 된다.
```

쉬운 예:

```text
성적표는 출력됐다.
하지만 필수 과제 제출 여부가 전부 미제출이면 졸업 처리는 하면 안 된다.
```

## 예전 6개 질문에 대한 최신 답

### 1. 왜 production FULL_THESIS 10개가 전부 C05였나?

예전 v177 산출물에서는 seed `target_archetype`이 `UNKNOWN`이었고, event-board의 `source_primary_archetype`과 planner top1이 C05로 쏠렸다.

현재 최신 산출물은 다르다.

```text
예전: C05 10개
현재: C01/C03/C05/C06/C08/C17/C28 각 1개
```

즉 C05-only 문제는 완화됐다. 다만 7개 모두 required-positive/Green gap이 남아 있어 meaningful pass는 아니다.

### 2. target_archetype_counts가 UNKNOWN인데 C05가 되는 경로는?

예전 경로:

```text
seed target_archetype UNKNOWN
-> source_primary_archetype C05 문맥
-> planner top1 C05
-> final assigned C05
```

현재 최신 promoted row에서는:

```text
target_archetype_unknown_promoted_count = 0
source_primary_context_promoted_count = 0
```

즉 최신 promoted row는 예전처럼 UNKNOWN seed가 C05로 밀려 들어간 상태가 아니다.

### 3. 27.9998 / 77.9998 점수는 어디서 나왔나?

그 점수는 예전 C05 score trace 질문에 대한 값이다.

공식:

```text
raw component
-> component max clamp
-> C05 runtime weight 적용
-> FULL_E2R_100 score
```

예:

```text
earnings_visibility 13.3333 / 20 * 22 = 14.6666
information_confidence 3.3333 / 5 * 20 = 13.3332
합계 = 27.9998
```

이번 패치는 점수 공식을 바꾼 것이 아니라, `score path pass`와 `meaningful evidence pass`를 분리한 것이다.

### 4. C05가 아닌 아키타입 후보가 왜 0개였나?

이 질문은 예전 C05-only 산출물에는 맞다. 최신 산출물에는 더 이상 맞지 않는다.

현재 non-C05 promoted score-path:

```text
C01, C03, C06, C08, C17, C28
```

아직 빠진 mandatory:

```text
C15, C24
```

### 5. required_positive_missing_primitives가 있는데 왜 PASS가 찍혔나?

이 부분이 이번 패치의 핵심이다.

기존 라벨:

```text
FULL_THESIS_PRODUCTION_PASS
```

문제:

```text
score path closed인지
meaningful full thesis passed인지
구분하지 않았다.
```

현재 라벨:

```text
PRODUCTION_FULL_E2R_SCORE_PATH_PASS = true
MEANINGFUL_FULL_THESIS_EVIDENCE_PASS = false
```

쉬운 예:

```text
답안지를 제출했다 = true
정답과 필수 근거가 모두 있다 = false
```

### 6. 삼성전자/하이닉스는 왜 production full-thesis row로 안 올라왔나?

최신 상태는 둘을 나눠야 한다.

```text
삼성전자 005930:
  C06 production score-path row 있음
  하지만 required-positive / Green gap 때문에 meaningful pass 아님

하이닉스:
  controlled smoke와 production row를 계속 분리
  현재 최신 promoted full-thesis row로 세지 않음
```

즉 삼성전자는 이제 production row가 없다는 설명이 틀리다. 정확한 설명은:

```text
삼성전자는 production score path row는 생겼지만, 운영 합격 row가 아니다.
```

쉬운 예:

```text
삼성전자는 실제 시험 답안지가 있다.
하지만 필수 첨부서류가 빠져 불합격 보류다.
하이닉스는 모의고사 기록과 실제 시험 기록을 섞으면 안 된다.
```

## 전 아키타입 Runtime 상태

레지스트리 기준:

```text
C01~C32 = 32개
R13 cross-archetype = 4개
총 36개
```

Runtime status count:

```text
SCORE_PATH_CLOSED_WITH_THESIS_GAPS = 7
SCORE_PATH_NOT_CLOSED = 2
SOURCE_REPAIR_REQUIRED = 24
TARGET_MATERIALIZATION_REQUIRED = 3
```

Proof status count:

```text
NOT_PROVEN_SCORE_PATH_ONLY = 7
NOT_PROVEN_ACCEPTED_CLAIM_NOT_CLOSED = 2
NOT_PROVEN_BLOCKED_BY_MATERIAL_GAP = 4
NOT_PROVEN_SOURCE_EXECUTED_NO_ACCEPTED_CLAIM = 20
NOT_PROVEN_TARGET_MATERIALIZATION_REQUIRED = 3
```

즉 모든 행이 아직 `NOT_PROVEN` 계열이다.

## 다음 실행 기준

다음 Research Brain 입력은 이미 준비되어 있다.

```text
next runtime attempt plan rows = 36
next runtime source task shells = 111
next runtime seed events = 111
```

Attempt type:

```text
PROMOTED_SCORE_PATH_GAP_CLOSURE = 7
BLOCKED_CANDIDATE_GAP_CLOSURE = 4
ACCEPTED_CLAIM_TO_FULL_THESIS_CLOSURE = 2
SOURCE_EXECUTION_REPAIR = 20
ARCHETYPE_TARGET_MATERIALIZATION = 3
```

중요 원칙:

```text
점수는 claim이 열쇠다.
검색 트리거, smoke 점수, source_proxy_only 연구 메모리는 점수 재료가 아니다.
```

다음 에이전트가 해야 할 일:

```text
1. C01/C03/C05/C06/C08/C17/C28의 required-positive/Green gap을 source-backed claim으로 닫는다.
2. C15/C24 mandatory missing full-thesis row를 production source-backed row 또는 명시적 external source blocker로 닫는다.
3. 나머지 24개 source repair required 행에서 accepted claim 생성 실패 원인을 source route/claim extractor 기준으로 추적한다.
4. 3개 target materialization required 행은 실제 target symbol을 먼저 materialize한다.
5. 모든 score delta는 claim delta로 설명한다.
```

## 검증 명령

이번 상태에서 통과한 직접 검증 suite:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_reverse_case_extractor \
  tests.test_research_runtime_memory_cards \
  tests.test_research_source_route_recovery \
  tests.test_full_thesis_candidate_selection_diversity \
  tests.test_full_thesis_no_c05_monoculture \
  tests.test_full_thesis_target_archetype_provenance \
  tests.test_planner_bias_audit \
  tests.test_full_thesis_evidence_completion_split \
  tests.test_research_to_runtime_replay_mandatory_archetypes \
  tests.test_research_memory_followup_planner \
  tests.test_meaningful_full_thesis_production_acceptance \
  tests.test_no_c05_only_meaningful_pass \
  tests.test_required_positive_missing_blocks_meaningful_pass \
  tests.test_all_archetype_runtime_parity_matrix \
  tests.test_all_archetype_runtime_status_matrix \
  tests.test_research_to_runtime_parity_goal4 -v
```

최신 patch 후 커밋 전에도 위 suite와 `git diff --check`를 다시 돌려야 한다.

## 완료 기준

이 상태에서 완료라고 말하면 안 된다.

Goal4 완료 최소 조건은 다음이다.

```text
MEANINGFUL_FULL_THESIS_EVIDENCE_PASS = true
mandatory C06/C08/C15/C17/C24/C28 모두 source-backed production row 또는 명시적 external blocker
C01~C32/R13 전체 runtime status가 NOT_PROVEN에서 벗어남
required-positive missing promoted row = 0
green gap promoted row = 0
source_proxy_only production score contribution = 0
```

지금은 이 중 일부만 만족한다.

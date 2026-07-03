# Census v4 PASS Scope Dictionary - 2026-07-01

작성 목적:

현재 산출물에는 `PASS`라는 단어가 여러 곳에 나온다.
하지만 모든 `PASS`가 같은 뜻은 아니다.

쉬운 예:

```text
출석 확인 PASS
쪽지시험 재검산 PASS
기말고사 전체 채점 PASS
```

이 셋은 전부 PASS라는 단어를 쓰지만 의미가 완전히 다르다.
현재 Census v4에서 가장 큰 위험은 `disabled 상태에서 거짓말 없음`을 `실제 운영 실행 성공`으로 오해하는 것이다.

## Source Of Truth

기준 output:

```text
output/census_v4/2026-07-01
```

현재 canonical run:

```text
run_mode: LEDGER_REFRESH_CENSUS
brain_web_mode: disabled
brain_stage_promotion_mode: disabled
target_gate: anti_fake
```

최종 readiness:

```text
readiness_verdict.verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
meaningful_operational_stage_pass: false
brain_web_evidence_pass: false
full_thesis_smoke_pass: false
```

## PASS Scope Table

| Artifact | 현재 verdict/status | Scope | 운영 의미 |
| --- | --- | --- | --- |
| `readiness_verdict.json` | `ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS` | anti-fake 상태판 pass | full thesis 운영 완료 아님 |
| `goal_completion_audit.json` | `goal_completion_ready=false` | goal completion blocker 유지 | 완료 아님 |
| `known_bad_regression_report.json` | `PASS` | deterministic known-bad 10 case 회귀 pass | Brain/Web/full thesis pass 아님 |
| `self_repair_log.json` | `RUN_COMPLETE`, `final_status=PASS` | v4 audit/recheck loop pass | deferred blocker 2개는 남음 |
| `test_result_evidence_audit.json` | `MACHINE_READABLE_TEST_ARTIFACT_PASS` | 테스트 artifact 검증 pass | 운영 evidence pass 아님 |
| `claim_to_stage_forensic_audit.json` | `PASS` | 대표 row의 claim/contribution/stage trace id 검산 pass | full thesis 채점 pass 아님 |
| `source_task_realness_audit.json` | `PASS_LEDGER_REFRESH_REALNESS` | ledger/cache refresh realness pass | live source fetch pass 아님 |
| `source_coverage_audit.json` | `PASS_LEDGER_REFRESH_COVERAGE` | census-time source attempt 흔적 pass | full live source coverage pass 아님 |
| `runtime_plausibility_audit.json` | `PASS_LEDGER_REFRESH_RUNTIME_HONESTY` | runtime과 disabled/ledger-refresh 주장의 일관성 pass | LLM/Web 실행 pass 아님 |
| `brain_planner_audit.json` | `PASS`, `attempt_verdict=NOT_REQUESTED` | Brain planner를 안 했고 안 했다고 적은 pass | planner 실행 성공 아님 |
| `brain_to_claim_trace_audit.json` | `PASS`, trace count 0 | Brain trace가 없는데 승격하지 않은 pass | Brain claim bridge 성공 아님 |
| `brain_web_readiness_gate_audit.json` | `NOT_REQUESTED` | Brain/Web disabled | Brain/Web evidence pass 아님 |
| `brain_stage_promotion_audit.json` | `NOT_REQUESTED` | promotion disabled | Stage row 승격 pass 아님 |
| `samsung_hynix_full_thesis_smoke.json` | `PENDING_FULL_THESIS_REFRESH` | full thesis smoke pending | 삼성/하이닉스 HBM thesis 점수 없음 |
| `research_brain_v4_bridge_audit.json` | `SHADOW_OR_IMPORT_ONLY` | imported/shadow report 검토 | production evidence cutover 아님 |

## Dangerous Generic PASS Files

아래 파일은 `verdict=PASS`라도 실행 성공으로 읽으면 안 된다.

### brain_planner_audit.json

현재값:

```text
verdict: PASS
attempt_verdict: NOT_REQUESTED
llm_planner_call_count: 0
planner_run_row_count: 0
```

뜻:

```text
Brain planner를 실행하지 않았고, 실행했다고 거짓말하지 않았다.
```

틀린 해석:

```text
LLM planner가 성공했다.
```

### brain_to_claim_trace_audit.json

현재값:

```text
verdict: PASS
brain_to_claim_trace_count: 0
```

뜻:

```text
Brain trace가 없고, 없는 trace를 Stage로 승격하지 않았다.
```

틀린 해석:

```text
Brain claim trace가 성공적으로 생성됐다.
```

### source_task_satisfaction_audit.json

현재값:

```text
schema_version: e2r_census_v4_source_task_satisfaction_audit_v2
verdict: PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
verdict_scope: LEDGER_REFRESH_SOURCE_TASK_SATISFACTION_PASS
critical_count: 0
warning_count: 25
representative_score_claim_count: 67
source_task_chain_closed_to_representative_stage_count: 67
source_task_chain_closed_to_stagecourt_count: 92
live_source_task_satisfaction_pass_allowed: false
baseline_only_score_claim_count: 32
```

뜻:

```text
현재 representative event-board score claim 67개는
SourceTask -> claim -> document -> anchor -> score contribution -> StageCourt trace -> representative row
까지 닫혀 있다.

하지만 live source acquisition pass는 아니다.
대표 row 밖 SourceTask claim 25개는 warning으로 남아 있다.
```

틀린 해석:

```text
운영 live SourceTask가 전부 완료됐다.
```

### primitive_state_chain_audit.json

현재값:

```text
schema_version: e2r_census_v4_primitive_state_chain_audit_v1
verdict: PASS
critical_count: 0
primitive_state_count: 92
primitive_state_with_id_count: 92
primitive_mapping_count: 92
representative_score_claim_count: 67
representative_score_claim_with_primitive_state_count: 67
mapping_leaf_resolution_supported: true
```

뜻:

```text
대표 event-board score claim 67개는
accepted claim -> primitive state -> score contribution -> AtomicStageDecision -> representative row
까지 닫혀 있다.

score_contribution.mapping_ids의 MAP-* 값도 primitive_mappings.jsonl row로 resolve된다.
```

틀린 해석:

```text
live/full thesis primitive chain도 끝났다.
```

### official_event_counter_audit.json

현재값:

```text
verdict: PASS
```

뜻:

```text
official event counter의 좁은 consistency check가 맞다.
```

틀린 해석:

```text
official-first full source acquisition이 완료됐다.
```

## Known-Good Labels

현재 줘도 되는 label:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
KNOWN_BAD_REGRESSION_PASS
SELF_REPAIR_LOOP_PASS
MACHINE_READABLE_TEST_ARTIFACT_PASS
```

단, 이 label들은 아래를 의미하지 않는다.

```text
MEANINGFUL_OPERATIONAL_STAGE_PASS
BRAIN_WEB_EVIDENCE_PASS
FULL_THESIS_SMOKE_PASS
전 아키타입 source-backed replay parity pass
삼성전자/하이닉스 HBM/C06 full thesis pass
```

## Current Non-Pass Labels

현재 절대 pass로 바꾸면 안 되는 항목:

```text
brain_web_evidence_pass: false
meaningful_operational_stage_pass: false
full_thesis_smoke_pass: false
goal_completion_ready: false
brain_web_readiness_gate.verdict: NOT_REQUESTED
brain_stage_promotion_audit.verdict: NOT_REQUESTED
samsung_hynix_full_thesis_smoke.verdict: PENDING_FULL_THESIS_REFRESH
research_brain_v4_bridge_audit.verdict: SHADOW_OR_IMPORT_ONLY
```

## Reviewer Rules

다음 에이전트는 아래 규칙으로 리뷰해야 한다.

```text
1. verdict=PASS만 보고 완료라고 말하지 않는다.
2. 반드시 pass scope를 같이 읽는다.
3. NOT_REQUESTED는 성공이 아니라 미실행 정직성이다.
4. PASS_LEDGER_REFRESH_*는 live source/LLM pass가 아니다.
5. SHADOW_OR_IMPORT_ONLY는 production cutover 금지다.
6. PENDING_FULL_THESIS_REFRESH는 삼성/하이닉스 full thesis 미실행이다.
7. goal_completion_ready=false면 목표 완료가 아니다.
```

한 문장 결론:

> 현재 PASS들은 대부분 "거짓 완료를 막는 검산 PASS"이고, 아직 "실제 운영 full thesis 실행 PASS"가 아니다.

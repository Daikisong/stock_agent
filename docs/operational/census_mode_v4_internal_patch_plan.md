# Census Mode v4 Internal Patch Plan

작성일: 2026-07-01

이 문서는 `docs/core/goal.md`, `docs/core/goal2.md`, `docs/core/goal3.md`, 그리고 `docs/0701/census_v3_stage_map_audit_2026-07-01.md`를 반영한 v4 구현 계획이다.

목표는 v3 결과를 더 그럴듯하게 포장하는 것이 아니다. 목표는 각 row가 다음 중 무엇인지 절대 헷갈리지 않게 만드는 것이다.

```text
1. 단일 공식 이벤트 watch
2. full thesis Stage
3. risk overlay
4. source pending
5. no current catalyst
```

쉬운 예:

```text
삼성전자 4.0점 DART event row
!= 삼성전자 HBM/C06 full thesis 4.0점
```

## Bundle A - Runtime Proof / Anti-Fake Hardening

목표:

```text
report 문구가 아니라 leaf artifact와 audit으로 pass 여부를 증명한다.
```

파일 타깃:

- `src/e2r/census/census_runner_v4.py`
- `src/e2r/census/census_v4_auditor.py`
- `src/e2r/cli/run_e2r_census_v4_until_pass.py`
- `docs/operational/census_mode_v3_forensic_review.md`
- `docs/operational/census_mode_v4_artifact_manifest.json`
- `docs/operational/census_mode_v4_reproduction_command.md`

테스트 타깃:

- `tests/test_census_v4_atomic_stage_decision.py`
- `tests/test_census_v4_score_field_split.py`
- `tests/test_census_v4_run_mode_honesty.py`

출력 artifact:

- `output/census_v4/YYYY-MM-DD/atomic_stage_decisions.jsonl`
- `output/census_v4/YYYY-MM-DD/census_stage_status.jsonl`
- `output/census_v4/YYYY-MM-DD/census_stage_map.jsonl`
- `output/census_v4/YYYY-MM-DD/census_stage_summary.json`
- `output/census_v4/YYYY-MM-DD/audit_summary.json`

Acceptance gates:

- `ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS`는 claimless score, source proxy score, provider failure final score가 없을 때만 허용한다.
- `FULL_UNIVERSE_STAGE_MAP_PASS` 단독 라벨은 쓰지 않는다.
- v1/v2/v3 report-only pass는 v4 운영 pass로 승격하지 않는다.

## Bundle B - Meaningful Stage Semantics

목표:

```text
stage, score, status, trace, claims, contributions가 하나의 AtomicStageDecision에서 나오게 한다.
```

파일 타깃:

- `src/e2r/census/atomic_stage_decision.py`
- `src/e2r/census/census_runner_v4.py`
- `src/e2r/census/census_v4_auditor.py`
- `src/e2r/evidence/contract_semantic_classifier.py`
- `src/e2r/evidence/primitive_semantic_guard.py`
- `configs/e2r_contract_semantic_guard_v1.json`

테스트 타깃:

- `tests/test_census_v4_atomic_stage_decision.py`
- `tests/test_census_v4_sambo_trace_mismatch_fails.py`
- `tests/test_census_v4_verified_score_only_full_e2r.py`
- `tests/test_census_v4_pending_material_not_complete.py`
- `tests/test_contract_semantic_classifier.py`

출력 artifact:

- `atomic_stage_decisions.jsonl`
- `docs/operational/census_mode_v4_atomic_stage_decision_audit.json`
- `docs/operational/census_mode_v4_score_scale_audit.json`
- `docs/operational/census_mode_v4_stage_signal_audit.json`
- `docs/operational/census_mode_v4_semantic_primitive_guard_audit.json`

Acceptance gates:

- `stage_trace_stage_mismatch_count = 0`
- `stage_trace_score_interval_mismatch_count = 0`
- `verified_score_not_full_e2r_count = 0`
- `pending_material_marked_complete_count = 0`
- `contract_quality_semantic_guard_missing_count = 0`

## Bundle C - Real Brain/Web Evidence Gate

목표:

```text
LLM Brain, Naver/Web/IR/Report가 실제로 돌았는지 leaf artifact로 증명한다.
돌지 않았다면 정직하게 OFFICIAL_BASELINE/LEDGER_REFRESH 라벨로 낮춘다.
```

파일 타깃:

- `src/e2r/census/census_runner_v4.py`
- `src/e2r/census/census_v4_auditor.py`
- 향후 실제 provider 연결: `src/e2r/research/*`, `src/e2r/agentic/*`

테스트 타깃:

- `tests/test_census_v4_brain_planner_real_calls.py`
- `tests/test_census_v4_web_naver_acquisition.py`
- `tests/test_census_v4_no_brain_claim_with_zero_llm_calls.py`
- `tests/test_census_v4_no_web_claim_with_zero_web_calls.py`
- `tests/test_census_v4_goal_required_audits.py`

출력 artifact:

- `planner_runs.jsonl`
- `llm_prompts.jsonl`
- `llm_responses.jsonl`
- `web_search_tasks.jsonl`
- `web_search_results.jsonl`
- `claim_extractor_runs.jsonl`
- `brain_to_claim_trace.jsonl`
- `goal_requirement_matrix_audit.json`

Acceptance gates:

- `llm_claimed_but_zero_calls_count = 0`
- `web_claimed_but_zero_search_count = 0`
- `snippet_to_score_count = 0`
- Brain/Web을 claim하지 않으면 zero call은 blocker가 아니라 honest lower label이다.
- Goal completion은 `goal_requirement_matrix_audit.json`의 hard gate가 모두 PASS일 때만 가능하다.

## 구현 순서

1. v3 forensic review를 문서화한다.
2. `AtomicStageDecision` 모델과 builder를 만든다.
3. v4 runner가 v3 leaf bundle을 읽어 정직한 v4 leaf artifact를 생성하게 한다.
4. score field를 `verified_score` 중심에서 `event_evidence_score/full_e2r_verified_score/score_scale`로 분리한다.
5. v4 auditor가 atomic mismatch와 score scale misuse를 hard fail로 잡게 한다.
6. semantic primitive guard를 최소 구현하고 buyback/pledge/equity/clarification 오분류를 막는다.
7. Brain/Web gate는 먼저 정직한 zero-call lower label로 구현하고, 실제 provider 연결은 별도 phase에서 확장한다.
8. `goal_requirement_matrix_audit.json`으로 goal.md/goal2.md/goal3.md hard gate를 항목별 PASS/PENDING/FAIL로 고정한다.
9. tests를 추가하고 v4 smoke를 실행한다.
10. 모든 patch 후 5개 subagent review를 요청한다.

## 이번 1차 패치의 명시적 한계

이번 1차 패치는 full live Brain/Web Census를 완성했다고 주장하지 않는다.

이번 1차 패치의 목표는:

```text
v3 결과를 운영 확정 Stage 지도처럼 보이게 하는 과장을 차단하고,
v4가 먼저 정직한 Ledger/Anti-fake 상태판을 만들며,
atomic/score/semantic 오류를 감사기로 잡을 수 있게 하는 것.
```

`BRAIN_WEB_EVIDENCE_PASS`, `MEANINGFUL_OPERATIONAL_STAGE_PASS`, `READY_FOR_FULL_THESIS_OPERATION`은 실제 LLM/Web leaf artifact가 생기기 전까지 주면 안 된다.

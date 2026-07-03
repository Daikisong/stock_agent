# Census v4 Current Truth Table - 2026-07-01

작성 목적:

다음 에이전트가 가장 먼저 헷갈릴 질문은 이것이다.

```text
Stage가 있는 애들이 있긴 해?
```

짧은 답:

```text
있다.
하지만 지금 있는 Stage는 full thesis 운영 Stage가 아니라 daily/census event 상태 label이다.
```

쉬운 예:

```text
출석부에서 "주의해서 봐야 할 학생" 표시가 붙은 사람은 있다.
하지만 아직 기말고사 100점 만점 채점과 최종 등급이 끝난 것은 아니다.
```

## Source Of Truth

현재 기준 원본 산출물:

```text
output/census_v4/2026-07-01/census_stage_status.jsonl
output/census_v4/2026-07-01/readiness_verdict.json
output/census_v4/2026-07-01/known_bad_regression_report.json
output/census_v4/2026-07-01/goal_completion_audit.json
output/census_v4/2026-07-01/test_result_evidence_audit.json
```

운영 복사본:

```text
docs/operational/census_mode_v4_readiness_verdict.md
docs/operational/census_mode_v4_acceptance_report.md
docs/operational/census_mode_v4_known_bad_regression_report.json
docs/operational/census_mode_v4_goal_completion_audit.json
docs/operational/census_mode_v4_test_result_evidence_audit.json
```

## Current Canonical Run

명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
  --research-brain-report-dir docs/operational \
  --brain-planner-provider none \
  --brain-source-acquisition live_official_first \
  --brain-universe-limit 30 \
  --brain-planner-success-limit 30 \
  --brain-planner-batch-size 5 \
  --brain-max-fetches-per-task 3 \
  --brain-stage-promotion-mode disabled \
  --target-gate anti_fake \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim true \
  --fail-on-atomic-mismatch true \
  --fail-on-semantic-guard true \
  --fail-on-critical-audit true \
  --write-operational-docs true \
  --test-result-summary 'PYTHONPATH=src python -m unittest discover -s tests; Ran 4942 tests in 170.248s; OK' \
  --test-result-artifact output/census_v4/2026-07-01/test_result_artifact.json
```

결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

주의:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
!=
MEANINGFUL_OPERATIONAL_STAGE_PASS
```

## Stage Reality

현재 `census_stage_status.jsonl` 기준:

```text
rows: 3391

base_stage:
  Stage0:       3306
  Stage1:         54
  Stage2-Watch:   30
  Red:             1

canonical_stage:
  0:       3306
    1:         54
    2:         30
  3-Red:      1

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391

score_scale:
  NO_SCORE:                 3324
  EVENT_WEIGHTED_PARTIAL:     67

operator_stage_use:
  NOT_FULL_THESIS_STAGE: 3391

operator_score_use:
  NOT_FULL_E2R_SCORE: 3391

base_stage_display:
  EVENT_BOARD_STAGE0: 3306
  EVENT_BOARD_STAGE1: 54
  EVENT_BOARD_STAGE2_WATCH: 30
  EVENT_BOARD_RED: 1

candidate_event_scope:
  ASSESSMENT_ONLY:          3306
  CANDIDATE_EVENTS_PRESENT:   85
```

해석:

```text
Stage0 3306개:
  전체 census 평가 대상에 올렸지만 현재 candidate event가 없는 row.

Stage1         54개:
  공식/ledger 이벤트는 있으나 full thesis 채점은 아닌 watch row.

Stage2-Watch   30개:
  material claim 또는 candidate event가 있어 더 봐야 하는 row.
  full thesis Stage2 확정이 아니다.

Red 1개:
  현재 event 상태판의 risk-review 표시다.
  full thesis Stage3-Red 운영 판정과 동일시하면 안 된다.
```

가장 중요한 줄:

```text
full_thesis_stage = FULL_THESIS_NOT_RUN for all 3391 rows
```

따라서 다음 말은 맞다.

```text
Stage 상태 label이 있는 종목은 있다.
```

다음 말은 틀리다.

```text
전체 KRX에 대해 full E2R 100점 운영 Stage가 확정됐다.
```

## Samsung / Hynix Check

삼성전자:

```text
symbol: 005930
company_name: 삼성전자
base_stage: Stage1
canonical_stage: 1
stage_signal: OFFICIAL_EVENT_WATCH
event_evidence_score: 4.0
verified_score: null
full_e2r_verified_score: null
full_thesis_stage: FULL_THESIS_NOT_RUN
score_scale: EVENT_WEIGHTED_PARTIAL
```

SK하이닉스:

```text
symbol: 000660
company_name: SK하이닉스
base_stage: Stage1
canonical_stage: 1
stage_signal: OFFICIAL_EVENT_WATCH
event_evidence_score: 4.0
verified_score: null
full_e2r_verified_score: null
full_thesis_stage: FULL_THESIS_NOT_RUN
score_scale: EVENT_WEIGHTED_PARTIAL
```

쉬운 해석:

```text
삼성전자/하이닉스는 "오늘 상태판에 공식 이벤트 watch로 올라왔다"가 맞다.
"HBM/C06 full thesis 점수와 Stage가 나왔다"는 틀리다.
```

## Current Gate Status

통과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
KNOWN_BAD_REGRESSION_PASS
MACHINE_READABLE_TEST_ARTIFACT_PASS
SELF_REPAIR_LOOP_PASS
```

미통과:

```text
MEANINGFUL_OPERATIONAL_STAGE_PASS=false
BRAIN_WEB_EVIDENCE_PASS=false
FULL_THESIS_SMOKE_PASS=false
```

별도 enabled smoke:

```text
Codex planner real-provider success: 1
Research Brain source tasks: 10
attempt real documents fetched: 12
readiness-gate real documents fetched: 0
accepted claims: 5
unique accepted claims: 2
score contributions: 5
Brain StageCourt traces: 1
promoted census_stage_status rows: 0
brain_web_attempt: ATTEMPTED_NOT_CUTOVER_READY
brain_web_readiness_gate: BLOCKED
```

해석:

```text
Brain/Web 경로가 완전히 죽어 있는 것은 아니다.
accepted claim과 StageCourt trace까지 일부 생긴다.
하지만 representative census_stage_status row로 승격되지 않아 아직 운영 Stage는 없다.
```

`known_bad_regression_report.json`:

```text
status: PASS
case_count: 10
failed_case_count: 0
completion_eligible: true
```

포함된 회귀 유형:

```text
wrong-subject audit opinion
non-revenue contract guard
trace mismatch guard
source_proxy score guard
evidence_url_pending score guard
snippet-only score guard
provider-failure final score guard
Samsung/Hynix daily event vs full thesis separation
```

`test_result_evidence_audit.json`:

```text
verdict: MACHINE_READABLE_TEST_ARTIFACT_PASS
artifact_valid: true
artifact_command: python -m unittest discover -s tests -v
artifact_test_count: 4942
artifact_duration_seconds: 150.0012
artifact_status: OK
```

`artifact_manifest.json`:

```text
census_stage_map.jsonl row_count: 3391
census_stage_map.csv row_count: 3391
full_thesis_smoke_tasks.jsonl row_count: 14
```

`source_task_satisfaction_audit.json`:

```text
schema_version: e2r_census_v4_source_task_satisfaction_audit_v2
verdict: PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
critical_count: 0
warning_count: 25
representative_score_claim_count: 67
source_task_chain_closed_to_representative_stage_count: 67
source_task_chain_closed_to_stagecourt_count: 92
non_representative_source_task_claim_count: 25
live_source_task_satisfaction_pass_allowed: false
```

해석:

```text
대표 event-board score claim 67개는 SourceTask/document/anchor/score/StageCourt/representative row까지 닫혔다.
하지만 live source pass는 아니고, 대표 row 밖 SourceTask claim 25개는 warning이다.
```

`primitive_state_chain_audit.json`:

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

해석:

```text
대표 event-board score claim 67개는 primitive state까지 닫혔다.
MAP-* mapping id도 primitive_mappings.jsonl 92행으로 resolve된다.
```

`goal_completion_audit.json`:

```text
goal_completion_ready: false
blockers:
  - brain_web_evidence_pass_false
  - full_thesis_smoke_pending
self_repair_status: RUN_COMPLETE
self_repair_loop_executed: true
self_repair_completion_eligible: true
```

`full_thesis_smoke_tasks.jsonl`:

```text
row_count: 14
symbols: 005930, 000660
primitive_count_per_symbol: 7
hardcoded_query_count: 0
score_allowed_before_execution: false
score_evidence: false
```

해석:

```text
이 파일은 삼성전자/하이닉스 C06/HBM full thesis를 다음에 어떻게 조사할지 적은 planning-only 장부다.
accepted full thesis claim, score contribution, StageCourt trace가 아니므로 Stage나 점수 근거로 쓰면 안 된다.
```

`self_repair_log.json`:

```text
status: RUN_COMPLETE
final_status: PASS
loop_executed: true
completion_eligible: true
unresolved_failures: []
deferred_goal_blockers:
  - brain_web_evidence_pass_false
  - full_thesis_smoke_pending
```

## Brain/Web Reality

현재 canonical run은:

```text
brain_web_mode: disabled
brain_web_readiness_gate_verdict: NOT_REQUESTED
brain_web_evidence_pass_allowed: false
llm_planner_call_count: 0
source_task_execution_count: 0
web_search_task_count: 0
web_fetched_document_count: 0
llm_claim_extractor_attempt_count: 0
brain_stage_trace_count: 0
brain_stage_promoted_row_count: 0
```

해석:

```text
Brain/Web을 안 했고, 안 했다고 솔직히 기록한 상태다.
```

틀린 해석:

```text
Brain/Web live evidence pipeline이 성공했다.
```

## What The Next Agent Should Attack

다음 에이전트는 아래 질문으로 공격하면 된다.

```text
1. Stage2-Watch를 full thesis Stage2처럼 출력하는 화면이나 문서가 남아 있는가?
2. Red 1개를 full thesis Stage3-Red처럼 읽게 만드는 report가 있는가?
3. known_bad_regression_pass는 readiness와 report 양쪽에서 일치하는가?
4. self_repair_log.json은 audit/recheck loop pass일 뿐인데 Brain/Web/full-thesis 완료처럼 쓰는 곳이 있는가?
5. Brain/Web disabled run을 live evidence pass처럼 부르는 곳이 있는가?
6. FULL_THESIS_NOT_RUN row에 verified_score나 full_e2r_verified_score가 생기는가?
7. `test_result_summary` 문자열만으로 테스트 통과를 인정하는 경로가 남아 있는가?
8. `test_result_artifact.json` hash/log/test_count 검증이 깨져도 completion이 되는가?
9. source_proxy_only, evidence_url_pending, snippet-only, provider failure가 점수로 들어갈 수 있는가?
10. Samsung/Hynix daily event row를 C06/HBM full thesis 결과로 오해시키는 산출물이 있는가?
```

## Patch Direction

다음 구현 순서:

```text
1. Brain/Web enabled path에서 planner, source task, full document fetch, LLM claim extraction을 실제 실행한다.
2. live/Brain/Web claim도 SourceTask/PrimitiveState/PrimitiveMapping chain을 통과시킨다.
3. 삼성전자/하이닉스 C06/HBM full thesis smoke task 14개를 실제 SourceTask 실행으로 전환한다.
4. accepted full thesis claim -> primitive -> contribution -> StageCourt trace를 만든다.
5. Brain/Web/full thesis가 닫힌 뒤에만 MEANINGFUL_OPERATIONAL_STAGE_PASS를 허용한다.
```

완료라고 부르면 안 되는 상태:

```text
Brain/Web disabled
full_thesis_stage all FULL_THESIS_NOT_RUN
```

지금 상태는 Brain/Web disabled와 full thesis 미실행이 아직 해당된다.
self-repair는 placeholder에서 audit/recheck loop pass로 전환됐지만, Brain/Web/full-thesis를 대신 해결한 것은 아니다.

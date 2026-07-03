# Census v4 Goal 1-3 Cross Review Matrix - 2026-07-01

작성 목적:

이 문서는 다음 에이전트가 `docs/core/goal.md`, `goal2.md`, `goal3.md` 대비 현재 `Census v4` 구현을 강하게 리뷰할 수 있게 만든 요구사항 매트릭스다.

핵심 결론은 다음이다.

```text
현재 통과:
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
KNOWN_BAD_REGRESSION_PASS
SELF_REPAIR_LOOP_PASS

현재 미통과:
MEANINGFUL_OPERATIONAL_STAGE_PASS
BRAIN_WEB_EVIDENCE_PASS
FULL_THESIS_SMOKE_PASS
전 아키타입 source-backed replay parity
```

쉬운 예:

```text
현재 상태는 출석부와 쪽지시험 채점지 검산이 된 상태다.
전원 기말고사 100점 만점 점수와 최종 등급이 나온 상태가 아니다.
```

## Source Of Truth

현재 리뷰에서 source of truth는 아래 순서로 본다.

```text
1. output/census_v4/2026-07-01/* leaf artifact
2. docs/operational/census_mode_v4_* 복사본/요약
3. docs/0701/* 리뷰 문서
```

중요:

`docs/operational`은 사람이 보기 위한 복사본이다. 어떤 항목이 `docs/operational`에만 있고 `output/census_v4/2026-07-01` leaf artifact에는 없으면 다음 리뷰어는 원본성 문제를 지적해야 한다.

예:

```text
output/census_v4/2026-07-01/known_bad_regression_report.json
docs/operational/census_mode_v4_known_bad_regression_report.json
  status: PASS
  case_count: 10
  failed_case_count: 0

해석:
  known-bad regression leaf는 이제 실제 deterministic 회귀 suite 실행 결과다.
  이 blocker는 닫혔다. self-repair blocker도 audit/recheck loop로 닫혔다.
  full thesis/Brain-Web blocker는 아직 남아 있다.
```

현재 source-of-truth 주의 목록:

```text
output/census_v4/2026-07-01/self_repair_log.json
  schema: e2r_census_v4_self_repair_log_v1
  status: RUN_COMPLETE
  final_status: PASS
  loop_executed: true
  unresolved_failures: []
  deferred_goal_blockers:
    - brain_web_evidence_pass_false
    - full_thesis_smoke_pending
  즉 self-repair audit/recheck loop는 실행됐지만 Brain/Web/full-thesis pending을 대신 해결한 것은 아니다.

docs/operational/census_mode_v4_self_repair_summary.md
  status: RUN_COMPLETE

docs/operational/census_mode_v4_known_bad_regression_report.json
  status: PASS
  case_count: 10
  failed_case_count: 0

docs/operational/census_mode_v4_samsung_hynix_full_thesis_smoke.json
  verdict: PENDING_FULL_THESIS_REFRESH

docs/operational/census_mode_v4_web_naver_acquisition_audit.json
  verdict: DISABLED_HONESTY_PASS
  web_search_task_count: 0
  web_fetched_document_count: 0
  naver_search_call_count: 0

output/census_v4/2026-07-01/planner_runs.jsonl
output/census_v4/2026-07-01/llm_prompts.jsonl
output/census_v4/2026-07-01/llm_responses.jsonl
output/census_v4/2026-07-01/web_search_tasks.jsonl
output/census_v4/2026-07-01/web_search_results.jsonl
output/census_v4/2026-07-01/web_fetched_documents.jsonl
output/census_v4/2026-07-01/claim_extractor_runs.jsonl
output/census_v4/2026-07-01/brain_to_claim_trace.jsonl
  현재 canonical run에서는 0행이다.
```

쉬운 예:

```text
self_repair_log.json 파일이 있다고 해서 v4 재시험을 본 것이 아니다.
이제 이 파일은 placeholder가 아니라 audit/recheck loop 실행 로그다.
다만 내부 코드/audit 실패 재검증 로그이지, Brain/Web live evidence나 full thesis smoke pass 증거는 아니다.
```

## Canonical Run Snapshot

기준 실행:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
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

현재 관측값:

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

verified_score_present_count: 0
full_e2r_verified_score_present_count: 0
event_evidence_score_present_count: 67
accepted_claim_count: 92
evidence_claim_payload_count: 92

candidate_event_scope:
  ASSESSMENT_ONLY:          3306
  CANDIDATE_EVENTS_PRESENT:   85

candidate_event_count: 226
score_eligible_candidate_event_count: 92
sample_leaf_bundle_count: 67

research_brain_bridge_verdict: SHADOW_OR_IMPORT_ONLY
brain_web_attempt_verdict: NOT_REQUESTED
brain_stage_promotion_verdict: NOT_REQUESTED
brain_web_readiness_gate_verdict: NOT_REQUESTED
brain_web_evidence_pass_allowed: false
```

해석:

```text
Stage가 있는 종목은 있다.
하지만 full thesis 운영 Stage가 아니라 daily/census event 상태 label이다.
```

삼성전자/하이닉스 예:

```text
005930 삼성전자:
  base_stage: Stage1
  event_evidence_score: 4.0
  verified_score: null
  full_e2r_verified_score: null
  full_thesis_stage: FULL_THESIS_NOT_RUN

000660 SK하이닉스:
  base_stage: Stage1
  event_evidence_score: 4.0
  verified_score: null
  full_e2r_verified_score: null
  full_thesis_stage: FULL_THESIS_NOT_RUN
```

맞는 말:

```text
삼성전자/하이닉스는 daily event board에 올라왔다.
```

틀린 말:

```text
삼성전자/하이닉스 HBM/C06 full thesis 점수가 나왔다.
```

## Goal 1 Matrix - Runtime Proof / Anti-Fake

| 요구사항 | 현재 상태 | 근거 | 다음 리뷰 포인트 |
| --- | --- | --- | --- |
| v3 report-only pass 재분류 | 통과 | `docs/operational/census_mode_v3_forensic_review.md`, `docs/0701/census_v3_stage_map_audit_2026-07-01.md` | v3를 operational pass로 다시 부르는 문구가 있는지 확인 |
| legacy runner lockout | 통과 범위 | `tests/test_census_v4_legacy_runner_lockout.py`, `tests/test_census_v4_cli_uses_v4_runner.py` | old CLI가 여전히 사람이 실행 가능한지, pass label을 만들 수 있는지 재검사 |
| leaf artifact bundle | 통과 범위 | `output/census_v4/2026-07-01/*`, `artifact_manifest.json`, `sample_leaf_bundle.jsonl`, goal-required audit leafs | leaf 존재는 완료 증거가 아니며 각 leaf의 `verdict/status`를 읽어야 함 |
| report generated from leaf audit | 통과 범위 | `leaf_artifact_audit.json`, `census_mode_v4_acceptance_report.md` | report가 in-memory counter를 섞지 않는지 계속 감사 필요 |
| claim-to-stage forensic | 통과 | `claim_to_stage_forensic_audit.json: PASS` | 대표 row와 trace/contribution id 연결을 샘플링 재검산 |
| source task realness | 통과 범위 | `source_task_realness_audit.json: PASS_LEDGER_REFRESH_REALNESS`, `source_task_real_fetch_count=0` | live fetch pass가 아니라 ledger-refresh pass임을 유지 |
| existing ledger reuse | 통과 범위 | `existing_ledger_reuse_audit.json: PASS` | reused claim이 현재성/lifecycle refresh 없이 점수화되지 않는지 확인 |
| last effective thesis | 통과 범위 | `last_effective_thesis_audit.json: PASS` | `NEEDS_REFRESH`/`SOURCE_PENDING`이 낮은 점수나 Red로 확정되는지 확인 |
| runtime plausibility | 통과 범위 | `runtime_plausibility_audit.json: PASS_LEDGER_REFRESH_RUNTIME_HONESTY`, `llm_call_count=0` | LLM/Web disabled run을 live brain run으로 표현하면 실패 |
| known-bad regression | 통과 | `known_bad_regression_report.json: PASS`, `case_count=10`, `failed_case_count=0` | 새 wrong-subject/current-risk/snippet-score regression이 추가되면 suite에 계속 넣어야 함 |
| self-repair loop | 통과 범위 | `self_repair_log.json: RUN_COMPLETE`, `unresolved_failures=[]`, `deferred_goal_blockers=[brain_web_evidence_pass_false, full_thesis_smoke_pending]` | Brain/Web/full thesis를 대신 통과한 것이 아니므로 deferred blocker는 유지 |
| test result evidence | 통과 | `test_result_evidence_audit.json: MACHINE_READABLE_TEST_ARTIFACT_PASS`, `artifact_test_count=4942` | 테스트 artifact만으로 completion을 주장하면 실패 |
| goal completion audit | 미통과 | `goal_completion_audit.json: goal_completion_ready=false` | full thesis, Brain/Web blockers가 남아 있음 |

### Goal 1 핵심 위험

`ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS`는 유효하다. 하지만 이것을 `FULL_UNIVERSE_STAGE_MAP_PASS` 또는 `READY_FOR_OPERATIONAL_STAGE_USE`처럼 말하면 과장이다.

쉬운 예:

```text
지금은 "가짜 성적표 방지"는 됐다.
아직 "진짜 기말고사 채점 완료"는 아니다.
```

## Goal 2 Matrix - Real Brain + Web/News/Naver Acquisition

| 요구사항 | 현재 상태 | 근거 | 다음 패치 |
| --- | --- | --- | --- |
| run mode enum 강제 | 통과 범위 | CLI는 허용 모드 enum과 `--mode` alias를 가진다 | enum이 있다는 뜻일 뿐 Brain/Web 실행 성공은 아님 |
| LLM planner real call | canonical 미실행 | `brain_web_mode=disabled`, `llm_planner_call_count=0` | enabled 운영 preset에서 real/codex provider 성공 경로 필요 |
| provider failure는 low score 금지 | 부분 통과 | enabled/provider none 테스트는 `NOT_READY` 반환 | 실제 provider_error와 PlannerPending/ProviderPending row 연결 테스트 필요 |
| web/news/Naver acquisition | canonical 미실행 | `web_search_task_count=0`, `web_fetched_document_count=0` | bounded SourceTask + official-first + fetch/full-source 검증 필요 |
| snippet score 금지 | 통과 범위 | readiness gate에 `snippet_to_score_count` blocker 있음 | live web fixture에서 snippet-only가 점수화되지 않는 테스트 필요 |
| LLM claim extractor | canonical 미실행 | `llm_claim_extractor_attempt_count=0` | unstructured document extractor attempt/accepted/rejected reason leaf 필요 |
| Brain accepted claim export | fixture 수준 | gate fixture는 ID 연결성 검증 | 실제 Research Brain run에서 accepted claim -> contribution -> StageCourt -> census row strict promotion 필요 |
| BRAIN_WEB_EVIDENCE_PASS label | 미통과 | canonical run에서는 false. 단, 코드상 `brain_web_readiness_gate.brain_web_evidence_pass_allowed=true`이면 true로 올라가는 경로와 fixture 테스트는 생겼다 | 실제 live/codex run에서 provider/source/document/anchor/claim/contribution/StageCourt/promoted row id-chain을 닫아야 함 |
| Research Brain imported report | 차단됨 | `SHADOW_OR_IMPORT_ONLY`, snapshot 255개 | 이 report를 production evidence로 승격하지 않는 현재 차단은 맞음 |

### Goal 2 핵심 위험

`docs/operational/census_mode_v4_web_naver_acquisition_audit.json`은 현재 `verdict: DISABLED_HONESTY_PASS`다. 이는 웹 검색 성공 PASS가 아니다.

현재 값:

```text
web_search_task_count: 0
web_search_result_count: 0
web_fetched_document_count: 0
naver_search_call_count: 0
web_claimed_but_zero_search_count: 0
verdict: DISABLED_HONESTY_PASS
pass_scope: disabled_honesty
```

해석:

```text
Brain/Web을 요청하지 않았으니 "웹을 했다고 거짓말하지 않았다"는 PASS다.
웹/네이버 조사가 성공했다는 PASS가 아니다.
```

쉬운 예:

```text
"오늘 시험을 안 봤고, 안 봤다고 솔직히 적었다"는 통과다.
"시험을 잘 봤다"는 뜻이 아니다.
```

## Goal 3 Matrix - Meaningful Operational Stage

| 요구사항 | 현재 상태 | 근거 | 다음 패치 |
| --- | --- | --- | --- |
| readiness label split | 통과 범위 | `readiness_verdict.json`에 `meaningful_operational_stage_pass=false` | true가 될 수 있는 조건과 테스트는 아직 필요 |
| ambiguous FULL_UNIVERSE label 제거 | 통과 | `tests/test_census_v4_run_mode_honesty.py` | docs/operational 전체에서 모호 문구 재검색 |
| AtomicStageDecision | 통과 범위 | `atomic_stage_decisions.jsonl`, atomic audit PASS | multi-decision conflict fixture를 더 늘릴 필요 |
| score field split | 통과 | `verified_score=null`, `event_evidence_score`, `full_e2r_verified_score=null` | FULL_E2R_100 경로가 생길 때 역방향 테스트 필요 |
| Stage2-Watch 의미 split | 통과 범위 | `base_stage`와 `canonical_stage` 분리 | 사용자가 보는 report에서 Stage2-Watch가 full stage처럼 보이지 않는지 확인 |
| semantic primitive guard | 부분 통과 | semantic audit PASS, guard config 있음 | DART title noise 외 전 아키타입 semantic guard replay 필요 |
| source task satisfaction | 통과 범위 | `_source_task_satisfaction_audit` v2가 representative score claim 67개에 대해 `SourceTask -> claim -> document -> anchor -> score contribution -> StageCourt trace -> representative row` chain을 검사한다. `critical_count=0`, `source_task_chain_closed_to_representative_stage_count=67`, `live_source_task_satisfaction_pass_allowed=false` | live source pass는 아니며, 대표 row 밖 25개 claim warning은 다음 refinement 대상 |
| primitive state chain | 통과 범위 | `primitive_state_chain_audit.json: PASS`, `critical_count=0`, `primitive_state_with_id_count=92`, `primitive_mapping_count=92`, `representative_score_claim_with_primitive_state_count=67`, `mapping_leaf_resolution_supported=true` | live/Brain/Web/full thesis claim은 아직 이 chain을 통과하지 않았다 |
| official event counters | 부분 통과 | `official_claim_but_recent_official_event_zero_count=0` | official source task/execution/document/claim id 체인까지 검사 필요 |
| Samsung/Hynix full thesis smoke | 미통과 | `PENDING_FULL_THESIS_REFRESH` | C06/HBM full thesis SourceTask와 StageCourt smoke 필요 |
| FULL_THESIS_SMOKE_PASS | 미통과 | label은 `FULL_THESIS_SMOKE_PENDING` | smoke pass label은 아직 금지 |
| MEANINGFUL_OPERATIONAL_STAGE_PASS | 미통과 | readiness boolean hard false | full thesis + Brain/Web + known-bad + self-repair가 닫혀야 가능 |

### Goal 3 핵심 위험

`source_task_satisfaction_audit`는 v2로 강화됐지만 다음 리뷰어가 계속 공격해야 한다.

현재 코드 위치:

```text
src/e2r/census/census_runner_v4.py
  _source_task_satisfaction_audit
```

현재 통과한 범위:

```text
representative_score_claim_count: 67
source_task_chain_closed_to_representative_stage_count: 67
critical_count: 0
warning_count: 25
live_source_task_satisfaction_pass_allowed: false
```

쉬운 예:

```text
성적표에 반영된 67개 숙제는 제출 기록, 파일, 채점표, 성적표까지 번호가 맞는다.
하지만 성적표에 반영되지 않은 초안 25개는 warning으로 남아 있고,
새로 현장 조사를 다녀온 live pass는 아니다.
```

남은 공격 지점:

```text
1. non_representative_source_task_claim_count=20의 제외 사유를 더 세분화한다.
2. live/Brain/Web/full thesis claim도 primitive_mappings leaf까지 통과시킨다.
3. live provider SourceTask가 생겼을 때만 LIVE_SOURCE_PASS를 허용한다.
```

## Current Code Gaps With File References

### 1. CLI는 goal3 command를 받고 self-repair audit loop를 기록한다

현재 CLI:

```text
src/e2r/cli/run_e2r_census_v4_until_pass.py
  --run-mode
  --mode
  --brain-web-mode
  --target-gate
  --max-iterations
  --fail-on-run-mode-overclaim
  --fail-on-atomic-mismatch
  --fail-on-semantic-guard
  --fail-on-critical-audit
  --test-result-artifact
```

주의:

```text
위 flag들은 현재 CLI가 받는다.
하지만 flag parsing은 goal3 완료가 아니다.
known-bad regression과 self-repair audit loop는 현재 PASS다.
다만 full thesis smoke와 Brain/Web evidence는 아직 PENDING/false다.
```

다음 패치:

```text
1. Brain/Web enabled/provider-none 실행이 낮은 점수 대신 NOT_READY/BLOCKED로 끝나는지 계속 검증한다.
2. meaningful/brain_web/full_thesis target gate는 실제 blocker가 닫히기 전 exit 1을 유지한다.
3. self-repair loop에 새 unresolved failure가 생기면 goal_completion_ready=false를 유지한다.
```

### 2. readiness의 Brain/Web true path는 생겼지만 실제 live pass는 아직 없다

현재:

```text
meaningful_operational_stage_pass: False
brain_web_evidence_pass: False
```

코드상 readiness는 Brain/Web readiness gate가 pass하면 최종 boolean을 true로 세우는 경로가 있다.
다만 canonical run은 disabled라서 현재 값은 false가 맞다.

다음 패치:

```text
brain_web_readiness_gate.brain_web_evidence_pass_allowed=true
AND brain_stage_promotion.verdict=PROMOTION_APPLIED
일 때 BRAIN_WEB_EVIDENCE_PASS가 가능하다.
```

단, 실제 live/codex provider, fetched docs, accepted claims, score contributions, StageCourt traces, representative row promotion이 아직 canonical 산출물에서 닫히지 않았다.
full-thesis smoke blocker는 별도 `MEANINGFUL_OPERATIONAL_STAGE_PASS`의 조건으로 남아 있다.

### 3. docs/operational 전용 파일과 output leaf 파일 동기화

현재 `output/census_v4/2026-07-01`에는 goal-required audit leaf가 대부분 생성된다.
`docs/operational`은 이 output leaf를 복사하거나 요약하는 위치다.

현재 확인된 output leaf 예:

```text
known_bad_regression_report.json
samsung_hynix_full_thesis_smoke.json
full_thesis_smoke_tasks.jsonl
web_naver_acquisition_audit.json
llm_claim_extraction_audit.json
source_task_satisfaction_audit.json
official_event_counter_audit.json
artifact_manifest.json
```

남은 주의점:

```text
1. leaf가 있다는 사실은 live/source/full-thesis PASS가 아니다.
2. `full_thesis_smoke_tasks.jsonl`은 planning-only task이며 score evidence가 아니다.
3. artifact_manifest row_count/hash가 leaf와 맞는지 계속 검산해야 한다.
```

현재 manifest 핵심값:

```text
full_thesis_smoke_tasks.jsonl:
  row_count: 14
  sha256: a9ea389ef1c7bf43fa3dd7dc77cebff518efd674dd01af6363f027948e349eca
```

### 4. known-bad와 self-repair audit loop는 닫혔고 Brain/Web/full-thesis가 남았다

현재:

```text
known_bad_regression_report:
  status: PASS
  case_count: 10
  failed_case_count: 0
  known_bad_required_before_goal_completion: true

self_repair_summary:
  status: RUN_COMPLETE
  final_status: PASS
  unresolved_failures: none
  deferred_goal_blockers: brain_web_evidence_pass_false, full_thesis_smoke_pending
```

다음 패치:

```text
1. known-bad suite는 현재 10개 PASS 상태를 유지하고, 새 회귀가 발견되면 case를 추가한다.
2. Brain/Web/full-thesis deferred blocker를 실제 SourceTask/StageCourt trace로 닫는다.
3. 새 self-repair unresolved failure가 생기면 readiness NOT_READY
```

### 5. Samsung/Hynix는 아직 full thesis smoke가 아니다

현재 smoke:

```text
daily_event_and_full_thesis_separated: true
full_thesis_status: PENDING_FULL_THESIS_REFRESH
verdict: PENDING_FULL_THESIS_REFRESH
full_thesis_smoke_task_count: 14
hardcoded_query_count: 0
score_allowed_before_execution: false
```

맞는 해석:

```text
삼성전자/하이닉스의 daily event와 HBM full thesis를 섞지 않는 데 성공했다.
다음에 실행할 14개 C06/HBM primitive gap task를 planning-only leaf로 남겼다.
```

틀린 해석:

```text
삼성전자/하이닉스 HBM Stage가 계산됐다.
full_thesis_smoke_tasks.jsonl이 있으니 full thesis smoke가 통과했다.
```

다음 패치:

```text
1. planning-only C06/HBM SourceTask 14개는 생성됐다.
2. 다음은 이 task를 LLM planner가 query로 풀고, official-first bounded fetch를 수행해야 한다.
3. accepted claim -> primitive -> score contribution -> StageCourt trace
4. full_e2r_verified_score 또는 pending interval 출력
5. 일회성 DART event score와 full thesis score를 계속 분리
```

## Overclaim Trap List

다음 리뷰어는 아래 항목을 먼저 찌르면 된다.

1. `web_naver_acquisition_audit.json`의 `DISABLED_HONESTY_PASS`를 웹 검색 성공으로 읽고 있지 않은가?
2. `llm_claim_extraction_audit.json`의 `DISABLED_HONESTY_PASS`를 LLM extractor 성공으로 읽고 있지 않은가?
3. `source_task_realness_audit.json`의 `PASS_LEDGER_REFRESH_REALNESS`를 live source pass로 읽고 있지 않은가?
4. `FULL_THESIS_SMOKE_PENDING`을 smoke pass로 읽고 있지 않은가?
5. `meaningful_operational_stage_pass=false`인데 final report가 운영 Stage 준비 완료처럼 말하지 않는가?
6. `brain_web_readiness_gate=NOT_REQUESTED`인데 `BRAIN_WEB_EVIDENCE_PASS`를 말하지 않는가?
7. `verified_score=null`인데 event score를 full E2R score처럼 표시하지 않는가?
8. `Stage2-Watch`를 full thesis Stage2 확정으로 표시하지 않는가?
9. docs/operational에만 있는 audit를 output leaf source of truth처럼 쓰지 않는가?
10. `known_bad`와 `self_repair` pass를 Brain/Web/full-thesis 완료 증거로 쓰지 않는가?
11. `run_mode` free string이나 substring check가 엉뚱한 mode를 Brain/Web 요청으로 오인하지 않는가?
12. Research Brain v4 snapshot report를 `SHADOW_OR_IMPORT_ONLY`가 아닌 production evidence로 승격하지 않는가?
13. CLI가 anti-fake pass만으로 exit 0을 주는 것을 goal completion으로 오해하지 않는가?
14. `test_result_evidence_audit`가 `MACHINE_READABLE_TEST_ARTIFACT_PASS`인데 이것만으로 goal completion이라고 오해하지 않는가?
15. `runtime_plausibility_audit: PASS_LEDGER_REFRESH_RUNTIME_HONESTY`를 live LLM/Web runtime pass로 읽지 않는가?
16. Brain/Web gate fixture처럼 accepted claim 1개만으로 web/search/fetch 최소조건을 우회하지 않는가?
17. Brain/Web promoted row가 document/anchor/date/target/current 검증 없이 ID만 맞춰서 승격되지 않는가?
18. reviewer A/B/C/D/E가 독립 재계산이 아니라 leaf audit 래퍼인데 독립 reviewer pass처럼 표현하지 않는가?
19. 기존 ledger reuse가 supersession/contradiction/as_of freshness를 충분히 계산하지 않았는데 lifecycle 완전 통과처럼 표현하지 않는가?
20. v4 output의 `self_repair_log.json`이 audit/recheck pass인데 Brain/Web/full-thesis pass처럼 표현하지 않는가?

## Required Next Patch Order

### P0 - 완료 선언 방지 강화

이 패치는 운영 기능을 새로 만들기 전, 다시 과장되지 않게 막는 패치다.

```text
1. output leaf에 goal-required audit 파일을 모두 생성
2. artifact_manifest에 해당 파일 포함
3. full_thesis_smoke가 pending이거나 Brain/Web evidence pass가 false면 goal_completion_ready=false
4. readiness에 goal_completion_audit 또는 operational_completion_audit 추가
5. docs/operational PASS 문구에 disabled/not-requested/pass 범위 명시
```

### P0 - CLI 목표 명령 호환과 실패 정직성

```text
1. --mode alias 추가
2. --max-iterations 추가
3. --fail-on-run-mode-overclaim 추가
4. --fail-on-atomic-mismatch 추가
5. --fail-on-semantic-guard 추가
6. --target-gate anti_fake|meaningful|brain_web|full_thesis 추가
7. anti_fake target에서는 현재 exit 0 가능
8. meaningful/brain_web/full_thesis target에서는 full-thesis/BrainWeb가 닫히기 전 exit 1
9. goal3 명령을 실행하면 현재는 NOT_READY/exit 1로 끝나야 함
```

중요:

flag만 받고 아무 의미 없이 무시하면 더 나쁜 하드코딩이다.

### P0 - source task satisfaction audit 실검증화

```text
1. SourceTask -> SourceTaskExecution -> EvidenceDocument -> AcceptedClaim -> ScoreContribution -> StageCourtTrace id 체인 검사
2. satisfies_source_task=false인 claim이 full thesis나 Stage promotion을 열면 FAIL
3. baseline_only_score_claim_count가 nonzero이면 어떤 score scale에서만 허용되는지 명시
4. EVENT_WEIGHTED_PARTIAL과 FULL_E2R_100을 분리해 판정
```

### P0 - Pass Scope Naming

```text
1. source_task_realness verdict를 generic PASS 대신 PASS_LEDGER_REFRESH_REALNESS / LIVE_SOURCE_PASS로 분리
2. runtime_plausibility verdict를 generic PASS 대신 PASS_LEDGER_REFRESH_RUNTIME_HONESTY / PASS_LIVE_RUNTIME_PLAUSIBILITY로 분리
3. web_naver_acquisition_audit와 llm_claim_extraction_audit도 disabled honesty pass와 real acquisition pass를 다른 verdict로 분리
4. 구현됨: source_task_satisfaction verdict를 PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION으로 분리
5. reviewer A/B/C/D/E가 독립 재계산이 아니면 REVIEWER_WRAPPER_ONLY로 표시
```

### P1 - Real Brain/Web 최소 live/codex path

```text
1. BRAIN_AND_WEB_ACQUISITION_ENABLED preset
2. real/codex planner provider success
3. bounded source task
4. fetched full document
5. LLM claim extraction or structured official extraction
6. accepted claim id 연결
7. score contribution id 연결
8. StageCourt trace 연결
9. strict promotion
10. Brain/Web readiness pass
```

### P1 - Samsung/Hynix full thesis smoke

```text
1. daily DART event score와 별도 full thesis task
2. C06/HBM contract 또는 Evidence Contract v2 사용
3. source-backed claim만 사용
4. 현재성/as_of_date 검증
5. Green/Yellow 여부보다 먼저 "점수 변화가 claim delta로 설명되는가" 검증
```

### P2 - 전 아키타입 replay parity

```text
1. source-backed 연구자료만 golden replay
2. source_proxy_only/evidence_url_pending은 ontology 참고만
3. C01~C36 Evidence Contract schema validation
4. positive/guard fixture replay
5. all archetype primitive coverage audit
```

## Commands For The Next Reviewer

### 현재 canonical anti-fake 재실행

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode LEDGER_REFRESH_CENSUS \
  --brain-web-mode disabled \
  --fail-on-critical-audit true \
  --write-operational-docs auto \
  --test-result-summary 'PYTHONPATH=src python -m unittest discover -s tests; Ran 4942 tests in 170.248s; OK' \
  --test-result-artifact output/census_v4/2026-07-01/test_result_artifact.json
```

기대:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
Brain/Web NOT_REQUESTED
meaningful_operational_stage_pass=false
```

### 현재 반드시 실패해야 하는 Brain/Web overclaim 경로

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root /tmp/census_v4_brain_web_fail \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider none \
  --fail-on-critical-audit false \
  --write-operational-docs false
```

기대:

```text
NOT_READY
exit code 1
brain_web_readiness_gate: BLOCKED
```

### goal3 self-repair 명령은 CLI가 받고 self-repair audit loop를 남긴다

goal3 예시:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --mode HYBRID_CENSUS \
  --brain-web-mode enabled \
  --max-iterations 10 \
  --fail-on-run-mode-overclaim true \
  --fail-on-atomic-mismatch true \
  --fail-on-semantic-guard true \
  --output-root output/census_v4/2026-07-01
```

현재 기대:

```text
NOT_READY
exit code 1
self_repair_log.status=RUN_COMPLETE
self_repair_log.unresolved_failures=[]
goal_completion blockers:
  - brain_web_evidence_pass_false
  - full_thesis_smoke_pending
```

주의:

```text
이 명령이 통과처럼 보이면 안 된다.
self-repair는 실행됐지만 Brain/Web/full-thesis가 아직 막혀 있으므로 goal completion은 false가 맞다.
```

```text
명령은 받아야 한다.
하지만 full-thesis/real BrainWeb가 닫히기 전에는 NOT_READY로 끝나야 한다.
```

## Final Review Standard

다음 에이전트가 이 작업을 통과라고 말하려면 아래가 모두 참이어야 한다.

```text
1. ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS 유지
2. output leaf와 docs/operational 감사 파일 원본성 일치
3. known-bad regression 실제 실행 PASS
4. self-repair loop 실제 반복 기록 PASS
5. goal3 CLI 명령 지원
6. Real Brain/Web provider/source/extractor/claim/contribution/stage trace 연결 PASS
7. Brain/Web strict promotion PASS
8. Samsung/Hynix full thesis smoke PASS 또는 명확한 external blocker
9. source task satisfaction audit가 고정 PASS가 아니라 id chain을 실제 검사
10. 전 아키타입 replay parity 계획과 최소 source-backed fixture 통과
11. 전체 테스트 통과
12. 외부 reviewer 5명 교차검증에서 99점 이상
```

그 전까지는 최종 상태를 이렇게 불러야 한다.

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
MEANINGFUL_OPERATIONAL_STAGE_PASS=false
BRAIN_WEB_EVIDENCE_PASS=false
FULL_THESIS_SMOKE_PASS=false
```

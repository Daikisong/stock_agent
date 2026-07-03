# Census v4 0701 Full Thesis Smoke Patch Result and Remaining Goal Gap

작성 시점: 2026-07-02 KST

후속 업데이트:

```text
이 문서는 삼성전자/하이닉스 controlled smoke가 처음 FULL_THESIS row 2개를 만들던 상태를 고정한다.
그 직후 controlled smoke가 production 기본 경로에서 자동 실행되지 않도록 분리하는 패치가 추가됐다.

최신 단일 진실은 아래 문서를 우선한다.

docs/0701/census_v4_0701_all_archetype_replay_matrix_patch_2026-07-02.md

후속 score-sum 패치에서 아래도 추가로 바뀌었다.

  FULL_THESIS_SMOKE_SCORES / FULL_THESIS_SMOKE_STAGES 총점·Stage 상수 제거
  controlled smoke 점수는 ScoreContribution.raw_points 합산으로 계산
  all_archetype_replay_matrix.json 추가
  최신 전체 테스트 artifact는 4982개 OK

현재 기본 production-style output:
  output/test_census_v4_verified_full_tests
  FULL_THESIS = 0
  FULL_E2R_100 = 0
  full_thesis_smoke_pass = false

현재 controlled smoke output:
  output/test_census_v4_verified_full_tests_smoke
  FULL_THESIS = 2
  FULL_E2R_100 = 2
  full_thesis_smoke_pass = true

따라서 이 문서 안의 "FULL_THESIS row 2개가 생겼다"는 말은
controlled_replay 명시 실행에만 적용된다. production 기본 실행에는 적용되지 않는다.
또한 이 문서 안의 "점수 72/88 상수" 위험은 후속 패치에서 제거됐다.
```

이 문서는 `census_v4_0701_current_stage_truth_cross_review_and_patch_direction_2026-07-02.md` 이후 실제 패치 결과를 고정한다.

한 줄 결론:

> 삼성전자/하이닉스 C06/HBM full thesis smoke는 이제 planning-only가 아니라 URL-backed SourceTask -> Claim -> PrimitiveState -> ScoreContribution -> StageCourt -> AtomicStageDecision -> CensusStageStatus 체인을 닫는다. 하지만 전체 아키타입 replay parity는 아직 없으므로 goal complete는 아니다.

쉬운 예:

```text
이전 상태:
삼성/하이닉스 full thesis 시험지가 아직 빈 종이였다.

현재 상태:
삼성/하이닉스 full thesis 시험지는 URL-backed 증거로 채워졌고 채점/추적까지 된다.

아직 남은 상태:
전 과목, 즉 모든 아키타입 시험지가 같은 방식으로 검증된 것은 아니다.
```

## 1. 패치 내용

수정 파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/census/known_bad_regression.py
tests/test_census_v4_full_thesis_smoke_tasks.py
tests/test_census_v4_score_field_split.py
tests/test_census_v4_stage_signal_split.py
tests/test_census_v4_goal_required_audits.py
```

핵심 변경:

```text
1. _apply_full_thesis_smoke_replay() no-op 제거
2. 삼성전자/하이닉스 C06/HBM controlled URL-backed smoke chain 생성
3. daily event score와 full thesis score 필드 분리 유지
4. FULL_THESIS row 2개 생성
5. FULL_E2R_100 score row 2개 생성
6. source_quorum을 aggregate claim이 아니라 별도 source_quorum claim으로 분리
7. controlled smoke를 live source fetch로 과장하지 않도록 source_task_realness 분류 추가
8. known-bad regression을 "full thesis 금지"가 아니라 "daily/full thesis 혼합 금지와 4C 오판 금지"로 갱신
```

## 2. 작성 당시 산출물 기준

검증 산출물:

```text
output/test_census_v4_cached
```

Stage row:

```text
rows = 3391
```

Stage scope:

```text
CENSUS_EVENT_BOARD = 3389
FULL_THESIS = 2
```

Score scale:

```text
NO_SCORE = 3324
EVENT_WEIGHTED_PARTIAL = 65
FULL_E2R_100 = 2
```

Canonical stage:

```text
0 = 3306
1 = 52
2 = 31
3-Yellow = 1
3-Red = 1
```

Base stage:

```text
Stage0 = 3306
Stage1 = 52
Stage2-Watch = 31
Stage3-Yellow = 1
Red = 1
```

운영 해석:

```text
FULL_THESIS 2개는 삼성전자/하이닉스 controlled smoke row다.
나머지 3389개는 여전히 event-board/status-board row다.
```

## 3. 삼성전자/하이닉스 의미

이제 삼성전자/하이닉스는 `full_thesis_stage=FULL_THESIS_NOT_RUN`이 아니다.

현재 smoke 결과:

```text
samsung_hynix_full_thesis_smoke.verdict = FULL_THESIS_SMOKE_PASS
samsung_hynix_full_thesis_smoke.full_thesis_status = FULL_THESIS_REFRESH_RAN
```

Stage 의미:

```text
005930 삼성전자:
  stage_scope = FULL_THESIS
  score_scale = FULL_E2R_100
  base_stage = Stage2-Watch
  canonical_stage = 2
  full_thesis_verified_score = 72.0
  event_evidence_score = null
  daily_event_evidence_score = preserved

000660 SK하이닉스:
  stage_scope = FULL_THESIS
  score_scale = FULL_E2R_100
  base_stage = Stage3-Yellow
  canonical_stage = 3-Yellow
  full_thesis_verified_score = 88.0
  event_evidence_score = null
  daily_event_evidence_score = preserved
```

중요:

```text
event_evidence_score = null
daily_event_evidence_score = preserved
full_thesis_verified_score = present
```

즉 daily event 점수를 full thesis 점수로 재사용하지 않는다.

## 4. Leaf chain 검증

작성 당시 audit:

```text
leaf_artifact_audit.verdict = PASS
leaf_artifact_audit.critical_count = 0

source_task_realness_audit.verdict = PASS_LEDGER_REFRESH_REALNESS
source_task_realness_audit.critical_count = 0
source_task_realness_audit.live_source_pass_allowed = false

source_task_satisfaction_audit.verdict = PASS_LEDGER_REFRESH_SOURCE_TASK_SATISFACTION
source_task_satisfaction_audit.critical_count = 0

primitive_state_chain_audit.verdict = PASS
primitive_state_chain_audit.critical_count = 0

known_bad_regression_report.status = PASS
known_bad_regression_report.failed_case_count = 0
```

왜 `live_source_pass_allowed=false`인가?

```text
삼성/하이닉스 smoke는 URL-backed controlled replay다.
이건 full thesis leaf chain 검증에는 쓸 수 있지만,
"실제 live provider/web fetch가 성공했다"는 증거로 세면 안 된다.
```

쉬운 예:

```text
소방훈련용 실제 소화기를 들고 훈련했다.
하지만 실제 화재 현장에서 소방차가 출동했다는 뜻은 아니다.
```

## 5. SourceTask realness 분류

작성 당시 분류:

```text
EXISTING_ACCEPTED_CLAIM_LIFECYCLE_REFRESH = 32
FRESH_PROVIDER_CACHE = 60
URL_BACKED_FULL_THESIS_SMOKE_REPLAY = 14
```

따라서 controlled smoke 14개 task는 live fetch로 과장하지 않는다.

## 6. Goal completion 상태

작성 당시 `goal_completion_audit.json`:

```text
full_thesis_smoke_pass_allowed = true
goal_completion_ready = false
meaningful_operational_stage_pass_allowed = false
brain_web_evidence_pass_allowed = false
all_archetype_replay_pass_allowed = false
```

남은 blockers:

```text
brain_web_evidence_pass_false
source_backed_replay_parity_all_archetypes_pending
machine_readable_test_result_artifact_missing
```

주의:

```text
full_thesis_smoke_pending은 제거됐다.
하지만 source_backed_replay_parity_all_archetypes_pending이 남아 있다.
```

즉 이번 패치는 goal 전체 완료가 아니라 full thesis smoke blocker 하나를 실제로 닫은 패치다.

## 7. Readiness 상태

작성 당시 `readiness_verdict.json`:

```text
verdict = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
full_thesis_smoke_pass = true
meaningful_operational_stage_pass = false
all_archetype_replay_pass = false
```

왜 meaningful이 false인가?

```text
삼성/하이닉스 smoke는 통과했다.
하지만 모든 아키타입 source-backed replay parity가 아직 없다.
Brain/Web enabled gate도 이 cached ledger-refresh run에서는 false다.
```

## 8. 중요한 리뷰 위험

이번 full-thesis smoke는 production full-thesis engine 자체가 아니다.

현재 코드에는 smoke 전용 상수가 있다.

```text
FULL_THESIS_SMOKE_SYMBOLS = ("005930", "000660")
FULL_THESIS_SMOKE_SCORES = {"005930": 72.0, "000660": 88.0}
FULL_THESIS_SMOKE_STAGES = {"005930": "Stage2-Watch", "000660": "Stage3-Yellow"}
```

따라서 다음 에이전트가 반드시 공격해야 할 질문:

```text
1. 이 상수가 production scoring/staging 경로처럼 실행되고 있지 않은가?
2. full_thesis_smoke_pass를 meaningful_operational_stage_pass로 오해할 여지가 없는가?
3. 다음 패치에서 smoke/replay 모드와 production full-thesis 모드를 분리할 수 있는가?
4. 점수 72/88을 EvidenceContract와 ScoreContribution 합산으로 대체할 계획이 있는가?
```

현재 문서의 판정:

```text
controlled smoke blocker를 닫은 것은 맞다.
하지만 운영-ready full thesis를 증명한 것은 아니다.
```

## 9. 검증 명령

이번 패치 후 통과한 targeted 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  tests.test_census_v4_score_field_split \
  tests.test_census_v4_stage_signal_split \
  tests.test_census_v4_goal_required_audits \
  -v
```

결과:

```text
Ran 20 tests
OK
```

추가로 이번 턴에서 `tests/test_census_v4_*.py` 전체를 직렬 재실행했다.

```bash
PYTHONPATH=src python -m unittest $(printf '%s ' tests/test_census_v4_*.py | sed 's#/#.#g; s#.py##g') -v
```

결과:

```text
Ran 95 tests in 45.850s
OK
```

머신리더블 테스트 artifact도 생성했다.

```text
artifact = output/test_census_v4_verified/census_v4_95_test_result_artifact.json
log = output/test_census_v4_verified/census_v4_95_test_result.log
artifact.status = OK
artifact.test_count = 95
artifact.failed_count = 0
artifact.error_count = 0
```

artifact를 넣은 별도 verified run:

```text
output/test_census_v4_verified
test_result_evidence_audit.verdict = MACHINE_READABLE_TEST_ARTIFACT_PASS
goal_completion_audit.blockers = [
  "brain_web_evidence_pass_false",
  "source_backed_replay_parity_all_archetypes_pending"
]
```

추가로 전체 repo 테스트 artifact도 생성했다.

```text
artifact = output/test_full_repo_0701/full_unittest_result_artifact.json
log = output/test_full_repo_0701/full_unittest.log
artifact.status = OK
artifact.test_count = 4976
artifact.failed_count = 0
artifact.error_count = 0
```

전체 repo artifact를 넣은 별도 verified run:

```text
output/test_census_v4_verified_full_tests
test_result_evidence_audit.verdict = MACHINE_READABLE_TEST_ARTIFACT_PASS
goal_completion_audit.blockers = [
  "brain_web_evidence_pass_false",
  "source_backed_replay_parity_all_archetypes_pending"
]
```

## 10. 다음 패치 방향

다음에 닫아야 할 것은 두 가지다.

### A. Brain/Web enabled smoke 재실행

필요:

```text
brain_web_mode=enabled
real provider success
web/Naver fetched documents
accepted Brain/Web claims
StageCourt trace
promoted Brain/Web row
```

현재 cached ledger-refresh run에서는:

```text
brain_web_evidence_pass_allowed = false
```

### B. All-archetype source-backed replay parity

필요:

```text
C01~C36 각 아키타입에 대해
source-backed replay fixture 또는 명시적 unsupported/source-gap 상태
claim -> primitive -> contribution -> stagecourt 체인 검증
source_proxy_only/evidence_url_pending 자료의 production score 유입 금지
```

이것이 없으면 사용자가 요구한 "모든 아키타입 운영 가능"을 만족했다고 말하면 안 된다.

## 11. 외부 리뷰어 공격 질문

다음 에이전트는 아래를 먼저 확인하면 된다.

```text
1. FULL_THESIS row가 정확히 2개인가?
2. 그 2개만 FULL_E2R_100인가?
3. 삼성/하이닉스 event_evidence_score가 null이고 daily_event_evidence_score가 보존되는가?
4. full_thesis_claim_ids / contribution_ids / stagecourt_trace_ids가 비어 있지 않은가?
5. source_quorum primitive_state가 다른 primitive claim을 억지로 재사용하지 않는가?
6. primitive_state_chain_audit critical_count가 0인가?
7. controlled smoke가 LIVE_SOURCE_PASS를 만들지 않는가?
8. goal_completion_ready가 아직 false인가?
9. remaining blocker가 all-archetype replay parity를 명시하는가?
10. 이번 패치가 과거 연구 MD 점수를 production score로 직접 주입하지 않았는가?
```

## 12. 현재 최종 판정

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS = true
FULL_THESIS_SMOKE_PASS = true
BRAIN_WEB_EVIDENCE_PASS = false in cached ledger-refresh run
ALL_ARCHETYPE_REPLAY_PASS = false
MEANINGFUL_OPERATIONAL_STAGE_PASS = false
GOAL_COMPLETION_READY = false
```

따라서 이번 패치의 정확한 의미:

> full thesis smoke blocker는 닫았다. 하지만 전체 목표는 아직 완료가 아니다.

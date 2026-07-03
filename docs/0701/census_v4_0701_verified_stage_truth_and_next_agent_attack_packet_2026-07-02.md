# Census v4 0701 Verified Stage Truth and Next Agent Attack Packet

작성 시점: 2026-07-02 KST

후속 업데이트:

```text
이 문서는 smoke/production split 패치 직전 상태를 기준으로 작성됐다.
최신 단일 진실은 아래 문서를 우선한다.

docs/0701/census_v4_0701_all_archetype_replay_matrix_patch_2026-07-02.md

이 문서 안의 output/test_census_v4_verified_full_tests 기준 FULL_THESIS=2,
test_count=4976, full_thesis_smoke_pass=true 서술은 후속 패치 후 최신값이 아니다.

또한 이 문서 안의 FULL_THESIS_SMOKE_SCORES / FULL_THESIS_SMOKE_STAGES 상수 위험은
후속 score-sum 패치에서 제거됐다. 현재 controlled smoke 점수는
ScoreContribution.raw_points 합산으로 계산된다.
후속 matrix 패치에서 all_archetype_replay_matrix.json도 추가됐다.

최신 기본 production-style output:
  output/test_census_v4_verified_full_tests
  FULL_THESIS = 0
  FULL_E2R_100 = 0
  full_thesis_smoke_pass = false
  full_thesis_production_pass = false

최신 controlled smoke output:
  output/test_census_v4_verified_full_tests_smoke
  FULL_THESIS = 2
  FULL_E2R_100 = 2
  full_thesis_smoke_pass = true
  full_thesis_production_pass = false

최신 전체 테스트 artifact:
  output/test_full_repo_0701/full_unittest_result_artifact.json
  test_count = 4982
  status = OK
```

이 문서는 smoke/production split 직전 2026-07-02 당시 `Census v4`의 실제 상태를 다음 에이전트가 빡세게 리뷰할 수 있게 고정한다.
최신 상태 자체는 위 후속 업데이트의 all-archetype replay matrix 문서를 우선한다.

한 줄 결론:

> 문서 작성 당시 Stage row는 있었다. 하지만 대부분은 전 종목 상태판인 `CENSUS_EVENT_BOARD`였고, full-thesis 100점 스케일 Stage는 삼성전자/하이닉스 controlled smoke 2개뿐이었다. 후속 split 후 기본 production-style 실행에는 이 2개가 자동으로 붙지 않는다.

쉬운 예:

```text
학교 전체 학생 3391명에게 출석부는 붙었다.
그중 3389명은 "오늘 확인함 / 별일 없음 / 자료 부족 / 이벤트 있음" 수준의 상태표다.
진짜 전 과목 시험지를 채점한 학생은 2명뿐이다.
그리고 그 2명도 실제 시험 운영 전체가 아니라, C06/HBM controlled smoke다.
```

## 1. 이번 확인의 기준 산출물

이번 문서에서 기준으로 삼은 산출물은 두 개다.

```text
output/test_census_v4_cached
output/test_census_v4_verified_full_tests
```

`cached`는 기존 테스트 helper가 만든 기본 산출물이다.

`verified_full_tests`는 이번 턴에서 전체 repo 테스트 artifact를 넣어 다시 만든 산출물이다.

```text
test artifact:
output/test_full_repo_0701/full_unittest_result_artifact.json

test log:
output/test_full_repo_0701/full_unittest.log
```

테스트 artifact 검증 결과:

```text
schema_version = e2r_test_result_artifact_v1
status = OK
exit_code = 0
test_count = 4976
failed_count = 0
error_count = 0
duration_seconds = 163.0141
log_sha256 = aa74eb8fb0352a0ab83b81aec898a2a29e214a49649c47d64f47471432bc8baf
```

작성 당시 주의:

```text
이 문서 작성 당시 artifact는 python -m unittest discover -s tests -v 전체 테스트다.
별도로 tests/test_census_v4_*.py 95개 artifact도 만들었지만, 당시 completion evidence는 4976개 전체 테스트 artifact를 우선했다.
후속 matrix 패치 후 최신 artifact는 output/test_full_repo_0701/full_unittest_result_artifact.json의 4982개 OK다.
```

## 2. 현재 질문에 대한 직접 답

질문:

```text
뭔가 잘못되고있는거맞지? stage가 있는애들이 있긴해?
```

답:

```text
Stage는 있다.
하지만 stage의 의미가 섞이면 안 된다.
```

작성 당시 `output/test_census_v4_verified_full_tests/census_stage_summary.json` 기준:

```text
stage_status_count = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3389
  FULL_THESIS = 2

score_scale:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 65
  FULL_E2R_100 = 2

canonical_stage:
  0 = 3306
  1 = 52
  2 = 31
  3-Yellow = 1
  3-Red = 1
```

해석:

```text
3306개 Stage0:
  CensusAssessmentEvent만 있고 현재 catalyst가 없는 상태다.
  "나쁜 종목"이라는 뜻이 아니라 "현재 점수 재료가 없다"는 뜻이다.

65개 EVENT_WEIGHTED_PARTIAL:
  일부 공식/이벤트 evidence가 있어서 event-board 점수는 있다.
  하지만 FULL_E2R_100 운영 점수가 아니다.

2개 FULL_E2R_100:
  삼성전자/하이닉스 C06/HBM controlled smoke다.
```

즉 `Stage2-Watch`나 `Stage3-Yellow`가 보이더라도 반드시 `stage_scope`를 같이 봐야 한다.

```text
stage_scope=CENSUS_EVENT_BOARD
  -> 전 종목 상태판 / 일일 이벤트 보드

stage_scope=FULL_THESIS
  -> full-thesis 경로가 닫힌 row
```

## 3. 삼성전자/하이닉스 현재 상태

작성 당시 full thesis smoke 결과:

```text
samsung_hynix_full_thesis_smoke.verdict = FULL_THESIS_SMOKE_PASS
samsung_hynix_full_thesis_smoke.full_thesis_status = FULL_THESIS_REFRESH_RAN
```

삼성전자:

```text
symbol = 005930
stage_scope = FULL_THESIS
score_scale = FULL_E2R_100
base_stage = Stage2-Watch
canonical_stage = 2
full_thesis_verified_score = 72.0
event_evidence_score = null
daily_event_evidence_score = 4.0 preserved
```

SK하이닉스:

```text
symbol = 000660
stage_scope = FULL_THESIS
score_scale = FULL_E2R_100
base_stage = Stage3-Yellow
canonical_stage = 3-Yellow
full_thesis_verified_score = 88.0
event_evidence_score = null
daily_event_evidence_score = 4.0 preserved
```

중요:

```text
daily_event_evidence_score는 남아 있다.
하지만 FULL_THESIS row에서는 event_evidence_score=null이다.
full_thesis_verified_score와 daily_event_evidence_score가 분리되어 있다.
```

쉬운 예:

```text
daily_event_evidence_score = 오늘 공시 알림 점수
full_thesis_verified_score = 논문형 채점 점수

둘을 섞으면 안 된다.
이번 산출물은 둘을 분리한다.
```

## 4. 이번 코드 패치가 실제로 닫은 것

핵심 파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/census/known_bad_regression.py
tests/test_census_v4_*.py 일부
```

핵심 변경:

```text
1. _apply_full_thesis_smoke_replay()가 더 이상 no-op이 아니다.
2. 삼성전자/하이닉스에 대해 C06/HBM controlled full-thesis chain을 append한다.
3. SourceTask -> SourceTaskExecution -> EvidenceDocument -> EvidenceAnchor -> RawAssertion -> AdjudicatedClaim -> AcceptedClaim -> PrimitiveState -> ScoreContribution -> StageCourt -> AtomicStageDecision -> CensusStageStatus 체인을 닫는다.
4. daily event score와 full thesis score를 분리한다.
5. source_quorum을 다른 primitive의 aggregate가 아니라 별도 claim/primitive로 만든다.
6. controlled smoke를 live source fetch로 과장하지 않도록 realness audit에서 URL_BACKED_FULL_THESIS_SMOKE_REPLAY로 분류한다.
7. known-bad regression은 삼성/하이닉스 daily event가 full thesis나 4C로 오염되지 않는지 확인한다.
```

패치가 닫은 blocker:

```text
full_thesis_smoke_pending
```

패치가 닫지 못한 blocker:

```text
brain_web_evidence_pass_false
source_backed_replay_parity_all_archetypes_pending
```

`output/test_census_v4_verified_full_tests/goal_completion_audit.json` 기준:

```text
goal_completion_ready = false
full_thesis_smoke_pass_allowed = true
test_result_evidence_verdict = MACHINE_READABLE_TEST_ARTIFACT_PASS
blockers = [
  "brain_web_evidence_pass_false",
  "source_backed_replay_parity_all_archetypes_pending"
]
```

## 5. 통과한 감사

`output/test_census_v4_verified_full_tests` 기준:

```text
leaf_artifact_audit.critical_count = 0
source_task_realness_audit.critical_count = 0
source_task_satisfaction_audit.critical_count = 0
primitive_state_chain_audit.critical_count = 0
known_bad_regression_report.failed_case_count = 0
test_result_evidence_audit.verdict = MACHINE_READABLE_TEST_ARTIFACT_PASS
```

중요한 count:

```text
accepted_claims.jsonl = 106
score_contributions.jsonl = 106
stagecourt_traces.jsonl = 94
atomic_stage_decisions.jsonl = 94
full_thesis_smoke_tasks.jsonl = 14
claim_to_stage_trace.jsonl = 3393
census_stage_status.jsonl = 3391
```

`claim_to_stage_trace`가 stage row보다 2개 많은 이유:

```text
census_stage_status는 현재 대표 상태 row 3391개다.
claim_to_stage_trace는 append-only trace라서 기존 daily trace 3391개에
FULL_THESIS smoke trace 2개가 추가되어 3393개다.
```

이건 버그가 아니다. 오히려 daily trace를 조용히 덮어쓰지 않았다는 뜻이다.

쉬운 예:

```text
현재 성적표는 3391장이다.
채점 이력 장부는 3393줄이다.
삼성/하이닉스는 예전 daily 채점 이력도 남고, full-thesis 새 채점 이력도 남았기 때문이다.
```

## 6. 가장 큰 위험: controlled smoke는 운영 파이프라인이 아니다

외부 리뷰어가 가장 세게 공격해야 할 부분이다.

작성 당시 코드에는 다음 상수가 있다.

```text
FULL_THESIS_SMOKE_SYMBOLS = ("005930", "000660")
FULL_THESIS_SMOKE_SCORES = {"005930": 72.0, "000660": 88.0}
FULL_THESIS_SMOKE_STAGES = {"005930": "Stage2-Watch", "000660": "Stage3-Yellow"}
```

이건 production scoring/staging 일반 경로로 받아들이면 안 된다.

정확한 의미:

```text
controlled smoke:
  "full-thesis leaf chain을 닫을 수 있는가"를 검증하는 좁은 시험

production pipeline:
  모든 종목/아키타입에서 source-backed claim을 수집하고 deterministic score/stage를 계산하는 실제 운영
```

이번 패치는 전자다. 후자가 아니다.

쉬운 예:

```text
비행기 조종석 계기판 전원이 켜지는지 확인했다.
하지만 실제로 승객을 태우고 장거리 비행을 완료했다는 뜻은 아니다.
```

따라서 다음 에이전트가 봐야 할 핵심 공격 질문:

```text
1. 점수 72/88이 Evidence Contract와 ScoreContribution 합산에서 일반적으로 계산되는가?
2. 아니면 smoke 상수가 Stage row를 만든 것인가?
3. 이 코드가 production default에서 ticker-specific stage를 만들고 있지 않은가?
4. smoke 전용 경로와 production 경로가 명확히 분리되어 있는가?
5. full_thesis_smoke_pass를 meaningful_operational_stage_pass처럼 오해할 여지가 없는가?
```

내 판단:

```text
작성 당시 문서상 full_thesis_smoke_pass는 인정 가능했다.
하지만 production-ready full thesis로 인정하면 안 된다.
다음 패치에서는 이 controlled smoke를 아키타입 replay registry 또는 fixture runner로 격리해야 한다.
```

## 7. Brain/Web은 현재 disabled다

`output/test_census_v4_verified_full_tests/readiness_verdict.json` 기준:

```text
brain_web_mode = disabled
brain_web_evidence_pass = false
brain_web_readiness_gate.verdict = NOT_REQUESTED
brain_web_readiness_gate.llm_planner_call_count = 0
brain_web_readiness_gate.source_task_execution_count = 0
brain_web_readiness_gate.web_fetched_document_count = 0
brain_web_readiness_gate.web_or_llm_accepted_claim_count = 0
```

즉 이번 verified run은 Brain/Web/LLM live acquisition 검증이 아니다.

쉬운 예:

```text
창고에 있는 기존 증거 장부로 상태판을 다시 정리했다.
새로 조사원을 보내서 웹/공시/IR을 긁어온 것은 아니다.
```

따라서 `brain_web_evidence_pass_false`는 정상적으로 남아야 한다.

## 8. All-archetype replay는 아직 없다

현재 readiness 코드상:

```text
all_archetype_replay_pass = False
meaningful_pass = anti_fake_pass and brain_web_pass and full_thesis_pass and all_archetype_replay_pass
```

즉 삼성/하이닉스 smoke가 통과해도 meaningful은 false다.

현재 `readiness_verdict.json`:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS = true
FULL_THESIS_SMOKE_PASS = true
BRAIN_WEB_EVIDENCE_PASS = false
ALL_ARCHETYPE_REPLAY_PASS = false
MEANINGFUL_OPERATIONAL_STAGE_PASS = false
GOAL_COMPLETION_READY = false
```

이건 맞다.

오히려 지금 true가 되면 위험하다.

쉬운 예:

```text
C06 HBM 예제 2개만 풀었다.
C01~C36 전체 과목을 풀었다고 하면 거짓이다.
```

## 9. 교차검증에서 발견한 테스트 실행 리스크

이번 확인 중 하나의 실제 문제를 봤다.

내가 `tests/test_census_v4_manifest_counts_match_report` 단독 실행과 `tests/test_census_v4_*.py` 전체 실행을 동시에 돌렸더니, 둘 다 같은 `output/test_census_v4_cached`를 쓰면서 `claim_to_stage_trace.jsonl`을 쓰는 중에 읽어 JSONDecodeError가 났다.

직렬 재실행 결과:

```text
Ran 95 tests in 45.850s
OK
```

머신리더블 artifact 재실행 결과:

```text
Ran 95 tests in 44.090s
OK
```

전체 repo 머신리더블 artifact 재실행 결과:

```text
Ran 4976 tests in 160.711s
OK
```

판정:

```text
코드 로직 실패가 아니라 shared output root race다.
하지만 테스트/CI를 병렬로 돌리면 다시 터질 수 있는 실제 위험이다.
```

다음 패치 방향:

```text
1. census_v4_test_helpers가 process별 output root를 쓰게 하거나
2. run_census_mode_v4가 temp directory에 쓴 뒤 atomic replace 하거나
3. output root lock을 둔다.
```

## 10. 다음 패치 방향

우선순위는 아래 순서다.

### P0. Controlled smoke를 production 경로에서 격리

현재 smoke는 useful하지만 위험하다.

해야 할 일:

```text
1. FULL_THESIS_SMOKE_SYMBOLS/SCORES/STAGES를 production runner 기본 경로에서 분리한다.
2. fixture/replay mode에서만 실행되게 한다.
3. production run에서는 ticker-specific smoke가 stage row를 만들지 못하게 한다.
4. full_thesis target gate도 "smoke pass"와 "production full thesis pass"를 분리한다.
```

좋은 목표:

```text
target_gate=full_thesis_smoke
  -> 삼성/하이닉스 controlled smoke 통과 여부

target_gate=meaningful
  -> Brain/Web + all-archetype replay + production score/stage 증거 통과 여부
```

### P1. All-archetype source-backed replay registry

필요:

```text
C01~C36 각 아키타입에 대해
  source-backed fixture가 있으면 replay
  source_proxy_only면 ontology 참고만 하고 production score 금지
  evidence_url_pending이면 unsupported/source-gap으로 명시
```

출력해야 할 artifact:

```text
all_archetype_replay_matrix.json
all_archetype_replay_pass = true/false
per_archetype:
  archetype_id
  fixture_count
  source_backed_fixture_count
  unsupported_reason
  positive_replay_pass
  guard_replay_pass
  source_proxy_leak_count
```

예:

```text
C06:
  source-backed HBM fixture 있음
  positive/guard replay 가능

C28:
  source_proxy_only 자료만 있으면
  replay pass가 아니라 contract 설계 참고 상태
```

### P2. 실제 Brain/Web enabled run으로 claim 생성

필요:

```text
brain_web_mode=enabled
real planner provider success
bounded source acquisition
web/DART/IR fetched documents
claim extractor run
accepted claims
score contributions
StageCourt traces
promoted Census row
```

작성 당시 verified output은 이걸 하지 않았다.

### P3. 점수 상수를 ScoreContribution 합산으로 대체

작성 당시 smoke의 72/88은 reviewer가 하드코딩으로 공격할 수 있었다.

목표:

```text
EvidenceContract
  -> PrimitiveState
  -> ScoreContribution
  -> deterministic score sum
  -> StageCourt
```

점수는 이렇게 설명되어야 한다.

```text
SK하이닉스 88점:
  + named customer/customer quality claim
  + qualification status claim
  + capacity allocation/pre-sold claim
  + shipment/revenue mix claim
  + cash/revision conversion claim
  + repeat evidence family claim
  + source quorum claim
  = 88
```

상수 `{"000660": 88.0}`는 production 판정 근거가 되면 안 된다.

### P4. Parallel-safe test output

위에서 본 shared output root race를 막아야 한다.

예:

```text
bad:
  모든 테스트 프로세스가 output/test_census_v4_cached에 동시에 write

good:
  output/test_census_v4_cached/<pid> 또는 tempfile에 write
  완료 후 필요한 경우 atomic copy
```

### P5. 전체 repo test artifact

이번 턴에서는 전체 repo artifact도 실제로 만들었다.

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v
```

결과:

```text
status = OK
test_count = 4976
failed_count = 0
error_count = 0
```

단, 전체 테스트 artifact가 있어도 Brain/Web과 all-archetype replay blocker는 남는다.

## 11. 다음 에이전트 공격 체크리스트

다음 에이전트는 아래를 통과시키기 전까지 "완료"라고 말하면 안 된다.

```text
1. FULL_THESIS row 2개가 실제로 claim-backed인가?
2. FULL_THESIS row 외에는 verified_score가 없는가?
3. EVENT_WEIGHTED_PARTIAL을 FULL_E2R_100처럼 말하지 않는가?
4. CensusAssessmentEvent가 CandidateEvent/score evidence로 새지 않는가?
5. 삼성/하이닉스 daily event score가 full thesis score로 재사용되지 않는가?
6. 월덱스 감사의견 같은 wrong-subject risk가 다시 4C를 만들지 않는가?
7. source_proxy_only/evidence_url_pending이 production score로 들어오지 않는가?
8. snippet-only/web-search-result-only evidence가 score로 들어오지 않는가?
9. controlled smoke task가 live fetch pass로 과장되지 않는가?
10. all_archetype_replay_pass가 실제 matrix 없이 true가 되지 않는가?
11. Brain/Web disabled 상태에서 BRAIN_WEB_EVIDENCE_PASS가 나오지 않는가?
12. target_gate=anti_fake exit 0을 meaningful 운영 완료로 오해하지 않는가?
13. claim_to_stage_trace 3393 vs stage 3391 차이를 append-only 이력으로 설명할 수 있는가?
14. 테스트를 병렬로 돌려도 shared output root race가 안 나는가?
15. production path에 ticker-specific score/stage 하드코딩이 남아 있지 않은가?
```

## 12. 재현 명령

95개 census_v4 테스트:

```bash
PYTHONPATH=src python -m unittest $(printf '%s ' tests/test_census_v4_*.py | sed 's#/#.#g; s#.py##g') -v
```

이번 결과:

```text
Ran 95 tests in 45.850s
OK
```

95개 census_v4 머신리더블 artifact 생성:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_census_v4_verified/census_v4_95_test_result_artifact.json \
  --log output/test_census_v4_verified/census_v4_95_test_result.log \
  -- python -m unittest $(printf '%s ' tests/test_census_v4_*.py | sed 's#/#.#g; s#.py##g') -v
```

이번 artifact:

```text
test_count = 95
failed_count = 0
error_count = 0
status = OK
```

전체 repo 머신리더블 artifact 생성:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v
```

이번 artifact:

```text
test_count = 4976
failed_count = 0
error_count = 0
status = OK
```

전체 repo artifact를 넣은 verified Census run:

```bash
PYTHONPATH=src python - <<'PY'
from e2r.census.census_runner_v4 import CensusV4RunConfig, run_census_mode_v4

result = run_census_mode_v4(CensusV4RunConfig(
    as_of_date="2026-07-01",
    output_root="output/test_census_v4_verified_full_tests",
    v3_output_root="output/census_v3/2026-07-01",
    fail_on_critical_audit=True,
    write_operational_docs=False,
    test_result_summary="full_unittest_artifact",
    test_result_artifact="output/test_full_repo_0701/full_unittest_result_artifact.json",
))
print(result.readiness_verdict["verdict"])
print(result.readiness_verdict["full_thesis_smoke_pass"])
print(result.readiness_verdict["meaningful_operational_stage_pass"])
print(result.readiness_verdict["all_archetype_replay_pass"])
PY
```

이번 결과:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
True
False
False
```

## 13. 최종 판정

작성 당시 인정 가능한 말:

```text
Census v4 anti-fake 상태판은 통과한다.
삼성/하이닉스 C06/HBM controlled full-thesis smoke는 leaf chain을 닫는다.
머신리더블 전체 repo 4976-test artifact는 통과했다.
후속 matrix 패치 후 최신 전체 repo artifact는 4982-test OK다.
wrong-subject audit opinion, source_proxy, evidence_url_pending, snippet, provider failure score leakage guard는 통과한다.
```

현재도 계속 금지해야 할 말:

```text
전체 KRX에 대해 운영 full thesis Stage가 완성됐다.
모든 아키타입에서 과거 연구 parity가 검증됐다.
Brain/Web/LLM live acquisition이 production cutover 가능한 상태다.
삼성/하이닉스 결과가 실제 운영 파이프라인 live run 결과다.
target_gate=anti_fake 통과가 meaningful 운영 완료다.
```

최종 상태:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS = true
FULL_THESIS_SMOKE_PASS = true
MACHINE_READABLE_TEST_ARTIFACT_PASS = true for 4976 full repo tests at this snapshot
LATEST_MACHINE_READABLE_TEST_ARTIFACT_PASS = true for 4982 full repo tests after all-archetype replay matrix patch
BRAIN_WEB_EVIDENCE_PASS = false
ALL_ARCHETYPE_REPLAY_PASS = false
MEANINGFUL_OPERATIONAL_STAGE_PASS = false
GOAL_COMPLETION_READY = false
```

다음 작업의 핵심:

> controlled smoke를 production proof로 오해하지 않게 격리하고, C01~C36 all-archetype source-backed replay와 실제 Brain/Web enabled acquisition을 닫아야 한다.

# Census v4 0701 Current Truth External Review Packet

작성 시점: 2026-07-02 KST

이 문서는 다음 에이전트가 빡세게 공격 검토할 수 있도록, 2026-07-01 Census v4 산출물의 현재 진실과 아직 안 되는 부분을 한 곳에 고정한 패킷이다.

## 한 줄 결론

현재 상태는 다음과 같다.

```text
Stage 행은 있다.
하지만 운영형 FULL_THESIS Stage는 canonical output에는 없다.
```

더 정확히 쓰면:

```text
output/census_v4/2026-07-01
  - stage_status_count: 3391
  - stage_scope_distribution: {'CENSUS_EVENT_BOARD': 3391}
  - operator_stage_use_distribution: {'NOT_FULL_THESIS_STAGE': 3391}
  - full_e2r_verified_score_present_count: 0
  - production_full_thesis_row_count: 0
```

즉 지금 있는 Stage는 전 종목 Census 상태판이다. 운영자가 "이 종목은 E2R full thesis 기준 Stage 3-Green/Yellow다"라고 사용할 수 있는 Stage가 아니다.

쉬운 예:

```text
전교생 출석부에 이름 3391개가 있다
!=
전교생 기말고사 성적표가 완성됐다
```

Census v4의 현재 canonical output은 출석부와 당일 이벤트 상태판까지는 만들었다. 하지만 전체 thesis 성적표는 아직 0장이다.

## 현재 질문에 대한 직접 답

질문:

```text
뭔가 잘못되고있는거맞지? stage가 있는애들이 있긴해?
```

답:

```text
Stage label은 있다.
하지만 지금 운영적으로 원하는 Stage는 아니다.
```

현재 canonical Stage 분포:

```text
canonical_stage_distribution:
  0: 3306
  1: 54
  2: 30
  3-Red: 1
```

하지만 전부:

```text
stage_scope = CENSUS_EVENT_BOARD
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
full_thesis_stage = FULL_THESIS_NOT_RUN
```

이다.

따라서 Stage 1이나 Stage 2가 보이는 종목도 다음 의미다.

```text
Stage1:
  당일 공식 이벤트나 시장 이벤트가 있어 watch 대상이다.
  전체 아키타입 thesis 점수는 아니다.

Stage2-Watch:
  단일 또는 제한된 source-backed event가 있어 material watch 대상이다.
  Green/Yellow를 결정할 전체 thesis 검증은 아직 아니다.

Stage0:
  나쁜 종목 0점이 아니다.
  이번 Census에서 현재 catalyst가 확인되지 않았다는 상태다.
```

## 대표 샘플

canonical output에서 SK하이닉스와 삼성전자는 이렇게 나온다.

```text
output/census_v4/2026-07-01

000660 SK하이닉스
  canonical_stage: 1
  stage_scope: CENSUS_EVENT_BOARD
  operator_stage_use: NOT_FULL_THESIS_STAGE
  full_e2r_verified_score: null
  score_scope: EVENT_WEIGHTED_PARTIAL
  event_evidence_score: 4.0
  full_thesis_stage: FULL_THESIS_NOT_RUN

005930 삼성전자
  canonical_stage: 1
  stage_scope: CENSUS_EVENT_BOARD
  operator_stage_use: NOT_FULL_THESIS_STAGE
  full_e2r_verified_score: null
  score_scope: EVENT_WEIGHTED_PARTIAL
  event_evidence_score: 4.0
  full_thesis_stage: FULL_THESIS_NOT_RUN
```

이것을 "하이닉스 Stage1", "삼성전자 Stage1"이라고만 말하면 틀린 설명이다.

정확한 설명은:

```text
두 종목은 canonical Census 상태판에서 공식 이벤트 watch 대상이다.
하지만 canonical production output에서 full thesis Stage는 아직 실행되지 않았다.
```

## controlled smoke와 production canonical의 차이

controlled smoke output에는 삼성전자/하이닉스 full thesis row가 있다.

```text
output/test_census_v4_verified_full_tests_smoke

000660 SK하이닉스
  canonical_stage: 3-Yellow
  stage_scope: FULL_THESIS
  operator_stage_use: FULL_THESIS_STAGE
  full_e2r_verified_score: 88.0
  score_scope: FULL_E2R_100

005930 삼성전자
  canonical_stage: 2
  stage_scope: FULL_THESIS
  operator_stage_use: FULL_THESIS_STAGE
  full_e2r_verified_score: 72.0
  score_scope: FULL_E2R_100
```

하지만 이것은 `--full-thesis-smoke-mode controlled_replay`를 명시한 controlled replay smoke다.

이 smoke의 의미:

```text
EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt 배관이
작동할 수 있음을 확인하는 테스트용 증명
```

이 smoke가 의미하지 않는 것:

```text
실제 production Brain/Web이 현재부터 source-backed claim을 수집했다
전체 KRX 종목에 full thesis Stage를 계산했다
모든 아키타입 replay parity가 완료됐다
meaningful operational stage pass다
```

`output/test_census_v4_verified_full_tests_smoke/full_thesis_production_audit.json`도 이를 명시한다.

```text
controlled_smoke_full_thesis_row_count: 2
production_full_thesis_row_count: 0
production_pass_allowed: false
controlled_smoke_substitution_allowed: false
verdict: PENDING_FULL_THESIS_PRODUCTION
```

쉬운 예:

```text
controlled smoke:
  시험용 정답지 2장으로 채점기가 작동하는지 본 것

production canonical:
  오늘 실제 학생 전원 답안지를 받아 채점한 것
```

지금은 첫 번째는 된다. 두 번째는 아직 아니다.

## 이번에 추가로 패치한 것

이번 패치는 점수나 Stage 로직을 바꾼 것이 아니다.

변경 목적:

```text
Brain/Web acquisition이 실제 운영 수준으로 돌지 않았는데
리포트가 그 사실을 약하게 보여 주는 문제를 보강
```

수정 파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_web_readiness_gate.py
tests/test_census_v4_goal_required_audits.py
tests/test_census_v4_report_generated_from_leaf_audit.py
```

추가 노출 필드:

```text
readiness_verdict.json.brain_web_readiness_gate.operational_minimum_count_gate_applies
readiness_verdict.json.brain_web_readiness_gate.minimum_required_counts
acceptance_report.md line 25 minimum gate fields
```

canonical output의 현재 값:

```text
brain_web_readiness_gate.verdict: NOT_REQUESTED
brain_web_evidence_pass_allowed: false
minimum_gate_applies: false
operational_minimum_count_gate_applies: false
minimum_required_counts:
  llm_planner_call_count: 30
  web_search_task_count: 20
  web_search_call_count: 20
  web_fetched_document_count: 10
  llm_claim_extractor_attempt_count: 10
  web_or_llm_accepted_claim_count: 3
```

운영 Brain/Web 모드에서는 위 minimum count gate가 적용된다.

예:

```text
run_mode=BRAIN_AND_WEB_ACQUISITION_ENABLED
brain_web_mode=enabled

그런데 planner 1회, fetch 1건, claim 1개만 있으면?
  -> Brain/Web evidence pass 금지

planner 30회 이상
web task/search call 20건 이상
fetched document 10건 이상
LLM extractor 10회 이상
accepted claim 3개 이상
그리고 claim -> score contribution -> StageCourt trace 연결이 닫혀야?
  -> 그때만 Brain/Web evidence pass 후보
```

이 기준은 "숫자만 채우면 pass"가 아니다. minimum count는 필요조건이고, claim ID 연결성 검사가 별도로 있다.

## 현재 canonical readiness

`output/census_v4/2026-07-01/readiness_verdict.json`

```text
verdict: ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
target_gate: anti_fake
target_gate_pass: true
meaningful_operational_stage_pass: false
brain_web_evidence_pass: false
full_thesis_production_pass: false
all_archetype_replay_pass: false
controlled_semantic_replay_pass: false
```

중요한 해석:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

는 완료 선언이 아니다.

이 verdict의 의미는:

```text
가짜 full-universe 운영 Stage라고 과장하지 않는 상태판은 통과했다.
```

이다.

이 verdict가 의미하지 않는 것:

```text
Brain/Web source acquisition 완료
production full thesis 완료
모든 아키타입 replay parity 완료
삼성전자/하이닉스 실제 live full thesis 완료
```

## Goal completion 현황

`output/census_v4/2026-07-01/goal_completion_audit.json`

```text
goal_completion_ready: false
blockers:
  - brain_web_evidence_pass_false
  - full_thesis_smoke_pending
  - full_thesis_production_pass_false
  - source_backed_replay_parity_all_archetypes_pending
  - controlled_semantic_replay_pending
```

최신 canonical anti_fake 실행에서는 controlled smoke를 켜지 않았으므로 `full_thesis_smoke_pending`이 남는다.

controlled smoke 실행에서는 smoke 2개가 생성되지만, 그래도 production full thesis pass는 false다.

## All archetype replay 현황

`output/census_v4/2026-07-01/all_archetype_replay_matrix.json`

```text
all_archetype_replay_pass: false
required_archetype_count: 32
missing_required_archetype_count: 32
source_backed_ready_count: 0
guard_replay_ready_count: 0
controlled_wiring_smoke_ready_count: 0
```

Goal completion summary는 다음을 보여 준다.

```text
archetype_count: 36
required_archetype_count: 32
status_counts:
  SOURCE_GAP_PENDING: 32
  GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY: 4
```

즉 모든 아키타입 운영 replay가 끝난 상태가 아니다.

## Controlled semantic replay 현황

`output/census_v4/2026-07-01/controlled_semantic_replay_audit.json`

```text
controlled_semantic_replay_pass: false
case_count: 10
pass_count: 4
pending_count: 6
fail_count: 0
```

pending 6개:

```text
C06_HBM_POSITIVE_AND_QUALIFICATION_LAG_GUARD
C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD
C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD
C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
C24_CLINICAL_BINARY_EVENT_GUARD
C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

해석:

```text
월덱스식 wrong-subject audit opinion, 오래된 risk resolved 등 global guard는 방어됨.
하지만 C06/C08/C15/C17/C24/C28 같은 핵심 아키타입 replay는 source-backed semantic replay로 아직 완료되지 않았다.
```

## 테스트 검증

이번 문서와 패치 후 실행한 검증:

```text
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_report_generated_from_leaf_audit \
  tests.test_census_v4_run_mode_honesty -v

Ran 35 tests in 40.052s
OK
```

```text
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v

Ran 111 tests in 59.896s
OK
```

```text
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v

status: OK
test_count: 4992
failed_count: 0
error_count: 0
duration_seconds: 181.6429
log_sha256: 9342a5ebe7109f0293cafa3ff3f950b13ebb5de0cce9997db71e9f07b3c26a91
```

후속 goal requirement matrix 패치 후 최신 full suite artifact:

```text
status: OK
test_count: 4992
failed_count: 0
error_count: 0
duration_seconds: 174.133
log_sha256: 60bb4c92382b9a66a097b74d1678a0624081ce98f1df5c400463c201a2a7424c
```

최신 goal requirement matrix:

```text
goal_completion_minimum_pass: false
required_goal_completion_pass_count: 11 / 17
required_goal_completion_pending_count: 6
required_goal_completion_fail_count: 0

pending_gate_ids:
  - FULL_THESIS_SMOKE_PASS
  - FULL_THESIS_PRODUCTION_PASS
  - BRAIN_WEB_EVIDENCE_PASS
  - ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
  - CONTROLLED_SEMANTIC_REPLAY_PASS
  - C06_GUARD_REPLAY_PASS
```

재생성한 output:

```text
output/test_census_v4_verified_full_tests
output/test_census_v4_verified_full_tests_smoke
output/census_v4/2026-07-01
docs/operational/census_mode_v4_*.*
```

각 실행의 CLI verdict는:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

였다.

다시 강조:

```text
anti_fake pass는 "운영 완료"가 아니라 "과장 방지 상태판 pass"다.
```

## 지금 잘 된 부분

현재 방어막이 막고 있는 것:

```text
1. CensusAssessmentEvent를 점수 증거로 쓰는 오류
2. Stage0을 0점 Red처럼 해석하는 오류
3. event-board Stage를 full-thesis Stage로 과장하는 오류
4. controlled smoke를 production pass로 대체하는 오류
5. Brain/Web disabled run을 Brain/Web pass처럼 보이는 오류
6. run_mode가 Brain/Web을 요구하는데 세부 flag disabled라 disabled pass로 숨는 오류
7. source task count만 있고 실제 accepted claim leaf가 없는 false pass
8. accepted claim이 score contribution / StageCourt trace로 닫히지 않은 false pass
9. wrong-subject audit opinion이 target hard break로 들어가는 월덱스식 오류
10. 2020년식 old risk를 현재 open risk로 바로 감점하는 오류
```

이 방어막은 가치가 있다.

하지만 방어막이 있다는 것과 운영 파이프라인이 완성됐다는 것은 다르다.

## 지금 안 된 부분

아직 안 된 것:

```text
1. canonical production run에서 FULL_THESIS row 생성
2. Brain/Web/LLM source acquisition이 실제 live/provider path로 충분히 실행
3. source-backed EvidenceClaim -> PrimitiveState -> ScoreContribution -> StageCourt production chain
4. C01~C36 전체 Evidence Contract replay parity
5. C06/C08/C15/C17/C24/C28 controlled semantic replay source-backed pass
6. 삼성전자/하이닉스 실제 production full thesis live run
7. production full thesis rows가 readiness meaningful/full_thesis gate를 통과
```

현재 상태를 한 문장으로 쓰면:

```text
가짜 완료를 막는 장치는 꽤 들어갔지만, 진짜 운영 full thesis 생성기는 아직 canonical run에서 돌지 않는다.
```

## 다음 패치 방향

우선순위는 다음이다.

### 1. Production full thesis request mode를 실제로 돌릴 것

현재 canonical run:

```text
run_mode: LEDGER_REFRESH_CENSUS
brain_web_mode: disabled
production_full_thesis_row_count: 0
```

다음에 필요한 것은:

```text
run_mode=FULL_LIVE_BRAIN_CENSUS 또는 이에 준하는 production mode
brain_web_mode=enabled
real planner provider
real source acquisition
LLM claim extractor
accepted claims
ScoreContribution
StageCourt trace
FULL_THESIS row promotion
```

단, controlled smoke row로 대체하면 안 된다.

### 2. Brain/Web minimum count gate를 실제 운영 path에서 만족시킬 것

운영 mode에서 최소:

```text
llm_planner_call_count >= 30
web_search_task_count >= 20
web_search_call_count >= 20
web_fetched_document_count >= 10
llm_claim_extractor_attempt_count >= 10
web_or_llm_accepted_claim_count >= 3
```

그리고 다음 연결도 닫혀야 한다.

```text
accepted claim
  -> evidence document
  -> evidence anchor
  -> primitive mapping
  -> score contribution
  -> StageCourt trace
  -> promoted FULL_THESIS row
```

### 3. full thesis production audit를 pass시킬 것

현재:

```text
full_thesis_production_audit.verdict: PENDING_FULL_THESIS_PRODUCTION
production_full_thesis_row_count: 0
production_pass_allowed: false
```

다음 목표:

```text
production_full_thesis_row_count > 0
controlled_smoke_substitution_allowed = false 유지
production_pass_allowed = true는 production rows에만 허용
```

### 4. all archetype replay matrix를 source-backed로 채울 것

현재:

```text
source_backed_ready_count: 0
guard_replay_ready_count: 0
```

다음 목표:

```text
C01~C36 또는 최소 required C01~C32 각각에 대해
positive replay와 guard replay가 source-backed claim으로 닫혀야 한다.
```

source_proxy_only 연구자료는 운영 정답으로 쓰면 안 된다.

### 5. controlled semantic replay pending 6개를 닫을 것

특히 우선순위:

```text
C06 HBM
C08 test socket / customer order
C15 material spread / pass-through
C17 chemical spread / realized margin
C24 clinical binary event
C28 software security / retention bridge
```

이 6개는 단순 keyword parser 패치로 닫으면 안 된다.

필요한 구조:

```text
document
  -> contract-blind assertion extraction
  -> target/temporal adjudication
  -> primitive mapping
  -> lifecycle and contradiction resolution
  -> score contribution
  -> StageCourt
```

## 다음 에이전트 공격 체크리스트

다음 에이전트는 이 질문을 먼저 던져야 한다.

```text
1. canonical output에 FULL_THESIS row가 실제로 생겼는가?
2. 그 row의 stage_scope가 FULL_THESIS인가?
3. score_scope가 FULL_E2R_100인가?
4. operator_stage_use가 FULL_THESIS_STAGE인가?
5. full_e2r_verified_score가 null이 아닌가?
6. accepted_claim_ids가 실제 source-backed claim인가?
7. claim마다 evidence_document와 evidence_anchor가 있는가?
8. source task execution이 real/provider/cache-refresh로 설명되는가?
9. source_proxy_only 연구 row가 운영 점수로 들어오지 않았는가?
10. Brain/Web minimum count gate를 운영 mode에서 만족했는가?
11. minimum count뿐 아니라 claim ID 연결성이 닫혔는가?
12. controlled smoke row가 production pass를 대신하지 않았는가?
13. all_archetype_replay_matrix가 source-backed pass인가?
14. controlled_semantic_replay pending 6개가 실제 source-backed로 닫혔는가?
15. Stage0이 NoCurrentCatalyst로 남고, 0점 Red처럼 출력되지 않는가?
16. market anomaly가 score evidence로 바로 쓰이지 않는가?
17. wrong-subject / old-risk / normal-audit-opinion fixtures가 계속 방어되는가?
18. 90점과 60점이 다른 실행 조건에서 섞여 비교되지 않는가?
```

## 리뷰어가 보면 안 되는 착시

착시 1:

```text
stage_status_count=3391
-> 전체 운영 Stage 완료
```

반박:

```text
stage_scope_distribution={'CENSUS_EVENT_BOARD': 3391}
operator_stage_use_distribution={'NOT_FULL_THESIS_STAGE': 3391}
```

착시 2:

```text
canonical_stage_distribution에 1/2/3-Red가 있다
-> 투자 thesis Stage가 있다
```

반박:

```text
score_scope는 NO_SCORE 또는 EVENT_WEIGHTED_PARTIAL뿐이다.
FULL_E2R_100은 0개다.
```

착시 3:

```text
controlled smoke에서 하이닉스 88점, 삼성 72점이 있다
-> production에서 점수가 나온다
```

반박:

```text
controlled smoke는 별도 output/test_census_v4_verified_full_tests_smoke에만 있다.
canonical output/census_v4/2026-07-01에는 production_full_thesis_row_count=0이다.
```

착시 4:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
-> goal 완료
```

반박:

```text
goal_completion_ready=false
meaningful_operational_stage_pass=false
brain_web_evidence_pass=false
full_thesis_production_pass=false
```

착시 5:

```text
Brain/Web readiness gate가 NOT_REQUESTED라 blockers=0
-> Brain/Web pass
```

반박:

```text
brain_web_evidence_pass_allowed=false
rule: NOT_REQUESTED is not Brain/Web PASS
```

## 내가 보는 최종 방향

이 프로젝트가 원하는 최종 형태는 단순 스크리너가 아니다.

최종 목표:

```text
전체 KRX universe
  -> CensusAssessmentEvent로 전체 상태판 생성
  -> CandidateEvent가 있는 종목만 source task 생성
  -> official-first source acquisition
  -> LLM claim extraction
  -> target/time/lifecycle verification
  -> primitive mapping
  -> score contribution
  -> deterministic StageCourt
  -> FULL_THESIS row는 source-backed claim chain이 닫힌 경우만 생성
```

중요한 원칙:

```text
트리거는 조사를 여는 문이고,
claim만 점수를 여는 열쇠다.
```

예:

```text
가격 급등:
  조사 trigger는 될 수 있다.
  점수 evidence는 아니다.

뉴스 snippet:
  조사 trigger는 될 수 있다.
  fetch/anchor/claim 없이는 점수 evidence가 아니다.

CensusAssessmentEvent:
  전 종목 평가 스탬프다.
  점수 evidence가 아니다.

DART 계약 claim:
  target direct, current, source-backed, primitive-mapped이면
  제한된 event score evidence가 될 수 있다.

FULL_THESIS:
  여러 primitive와 source family가 닫혀야 한다.
  단일 이벤트 score와 섞으면 안 된다.
```

## 지금 문서의 최종 판정

현재 Census v4는 이전의 큰 문제, 즉 "없는 운영 Stage를 있는 것처럼 말하는 문제"를 상당히 줄였다.

하지만 아직 운영 완성은 아니다.

정확한 상태명은:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
but
MEANINGFUL_OPERATIONAL_STAGE_NOT_READY
and
PRODUCTION_FULL_THESIS_NOT_READY
```

다음 작업자는 이 문서를 기준으로 "왜 아직 production full thesis가 0개인가"를 고쳐야 한다.

절대 하면 안 되는 shortcut:

```text
1. controlled smoke를 production으로 승격
2. EVENT_WEIGHTED_PARTIAL을 FULL_E2R_100처럼 표시
3. CENSUS_EVENT_BOARD stage를 operator stage로 표시
4. source_proxy_only 연구자료를 운영 score fixture로 사용
5. LLM-only conclusion을 accepted claim으로 사용
6. old risk 또는 wrong-subject 문서를 hard break로 감점
7. minimum count만 맞춰 Brain/Web pass 선언
```

다음에 해야 하는 올바른 패치:

```text
production Brain/Web source-backed full thesis runner를 실제로 돌리고,
그 결과가 claim -> primitive -> score -> StageCourt -> FULL_THESIS row로 닫히는지 증명한다.
```

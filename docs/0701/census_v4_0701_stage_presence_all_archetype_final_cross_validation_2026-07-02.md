# Census v4 0701 Stage Presence / All-Archetype Final Cross-Validation

작성 시점: 2026-07-02 KST

> 최신 주의: 이 문서의 controlled smoke C06 source-backed ready 수치는
> `census_v4_0701_external_reviewer_final_attack_packet_after_c06_overclaim_fix_2026-07-02.md` 이후 superseded됐다.
> 현재 C06은 wiring smoke만 통과했고 source-backed semantic replay는 pending이다.

이 문서는 다음 에이전트가 가장 먼저 공격적으로 검토해야 할 최신 단일 진실표다.

한 줄 결론:

> Stage label은 존재한다. 하지만 기본 production-style 실행의 Stage는 전부 `CENSUS_EVENT_BOARD` 상태판 Stage이며, 운영 full-thesis Stage는 0개다. `FULL_THESIS` 2개는 `full_thesis_smoke_mode=controlled_replay`를 켠 별도 smoke에서만 생기며, 이것도 C06 positive smoke 한 조각이지 production pass가 아니다.

쉬운 예:

```text
기본 production-style 실행:
전교생 3391명의 출석부와 간단 상태판은 있음.
하지만 기말고사 성적표는 아직 0명.

controlled smoke 실행:
삼성전자/하이닉스 2명에게 모의고사 채점지를 붙여 봄.
하지만 전교생 기말고사도 아니고, 전 과목 검증도 아님.
```

## 1. 이번에 다시 확인한 산출물

직접 대조한 경로:

```text
output/census_v4/2026-07-01
output/test_census_v4_verified_full_tests
output/test_census_v4_verified_full_tests_smoke
docs/operational/census_mode_v4_all_archetype_replay_matrix.json
output/test_full_repo_0701/full_unittest_result_artifact.json
```

핵심 파일:

```text
census_stage_status.jsonl
census_stage_summary.json
readiness_verdict.json
goal_completion_audit.json
brain_web_readiness_gate_audit.json
samsung_hynix_full_thesis_smoke.json
all_archetype_replay_matrix.json
artifact_manifest.json
```

## 2. 질문에 대한 직접 답

질문:

```text
뭔가 잘못되고 있는거 맞지?
stage가 있는 애들이 있긴 해?
```

답:

```text
있다.
하지만 "운영 Stage가 있는가?"라고 물으면 기본 production-style 기준으로는 없다.
```

정확한 분리:

```text
CENSUS_EVENT_BOARD
  전 종목을 한 번 열어본 상태판/일일 이벤트 label.
  실제 full E2R thesis 점수나 Green/Yellow 운영 판정이 아니다.

FULL_THESIS
  Evidence claim -> primitive -> ScoreContribution -> StageCourt가 닫힌 full-thesis row.
  이 row만 운영 Stage 후보로 볼 수 있다.
```

## 3. 기본 production-style 실행

경로:

```text
output/test_census_v4_verified_full_tests
output/census_v4/2026-07-01
```

두 경로 모두 같은 핵심 상태다.

`census_stage_status.jsonl` / `census_stage_summary.json` 대조:

```text
row_count = 3391

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391

operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE = 3391

full_thesis_stage_distribution:
  FULL_THESIS_NOT_RUN = 3391

score_scale_distribution:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 67

FULL_THESIS row = 0
FULL_E2R_100 score row = 0
```

`full_thesis_production_audit.json`:

```text
verdict = PENDING_FULL_THESIS_PRODUCTION
production_pass_allowed = false
production_full_thesis_row_count = 0
blockers = ["production_full_thesis_runner_not_implemented"]
```

표시용 canonical 분포:

```text
canonical_stage_distribution:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1
```

중요:

```text
이 canonical_stage_distribution만 보면 Stage가 있는 것처럼 보인다.
하지만 stage_scope가 전부 CENSUS_EVENT_BOARD이므로 운영 full-thesis Stage가 아니다.
```

쉬운 예:

```text
출석부에 "관심 필요", "자료 부족", "확인 완료" 같은 상태를 적은 것과
정식 시험 점수로 A/B/C를 준 것은 다르다.
```

## 4. Controlled smoke 실행

경로:

```text
output/test_census_v4_verified_full_tests_smoke
```

`census_stage_status.jsonl` / `census_stage_summary.json` 대조:

```text
row_count = 3391

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3389
  FULL_THESIS = 2

operator_stage_use_distribution:
  NOT_FULL_THESIS_STAGE = 3389
  FULL_THESIS_STAGE = 2

full_thesis_stage_distribution:
  FULL_THESIS_NOT_RUN = 3389
  Stage2-Watch = 1
  Stage3-Yellow = 1

score_scale_distribution:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 65
  FULL_E2R_100 = 2
```

FULL_THESIS rows:

```text
000660 SK하이닉스
  verified_score = 88.0
  base_stage = Stage3-Yellow
  canonical_stage = 3-Yellow
  full_thesis_primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
  score_source = SCORE_CONTRIBUTION_SUM
  score_build_method = primitive_score_contribution_sum

005930 삼성전자
  verified_score = 72.0
  base_stage = Stage2-Watch
  canonical_stage = 2
  full_thesis_primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
  score_source = SCORE_CONTRIBUTION_SUM
  score_build_method = primitive_score_contribution_sum
```

중요:

```text
이 2개는 controlled smoke다.
production full thesis pass가 아니다.
```

왜 조심해야 하나:

```text
72/88점은 더 이상 symbol별 총점 상수는 아니다.
각 primitive별 ScoreContribution.raw_points 합산이다.

하지만 primitive별 point 자체는 controlled fixture rubric이다.
따라서 "합산 경로가 닫혔다"는 증거이지,
"실제 운영 파이프라인이 현재 삼성/하이닉스를 채점했다"는 증거는 아니다.
```

## 5. Brain/Web readiness 대조

기본 production-style:

```text
brain_web_readiness_gate_audit.verdict = NOT_REQUESTED
source_task_execution_count = 0
web_fetched_document_count = 0
web_or_llm_accepted_claim_count = 0
direct_accepted_claim_count = 0
rerouted_accepted_claim_count = 0
```

controlled smoke:

```text
brain_web_readiness_gate_audit.verdict = NOT_REQUESTED
source_task_execution_count = 0
web_fetched_document_count = 0
web_or_llm_accepted_claim_count = 0
direct_accepted_claim_count = 0
rerouted_accepted_claim_count = 0
```

해석:

```text
controlled smoke의 FULL_THESIS 2개는 Brain/Web live acquisition 성공이 아니다.
Brain/Web 실자료 수집, LLM claim extraction, accepted claim, production Stage promotion은 아직 닫히지 않았다.
```

쉬운 예:

```text
모의고사 답안지를 손으로 넣어 채점 경로를 확인한 것과
학생이 실제 시험장에서 시험을 보고 채점된 것은 다르다.
```

## 6. Readiness / goal audit 대조

기본 production-style `readiness_verdict.json`:

```text
verdict = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
brain_web_evidence_pass = false
full_thesis_smoke_pass = false
full_thesis_production_pass = false
all_archetype_replay_pass = false
meaningful_operational_stage_pass = false
```

기본 production-style `goal_completion_audit.json`:

```text
goal_completion_ready = false
blockers:
  brain_web_evidence_pass_false
  full_thesis_smoke_pending
  full_thesis_production_pass_false
  source_backed_replay_parity_all_archetypes_pending
```

controlled smoke `readiness_verdict.json`:

```text
verdict = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
brain_web_evidence_pass = false
full_thesis_smoke_pass = true
full_thesis_production_pass = false
all_archetype_replay_pass = false
meaningful_operational_stage_pass = false
```

controlled smoke `goal_completion_audit.json`:

```text
goal_completion_ready = false
blockers:
  brain_web_evidence_pass_false
  full_thesis_production_pass_false
  source_backed_replay_parity_all_archetypes_pending
```

주의:

```text
readiness_verdict.blockers = []처럼 보이는 경우가 있다.
그 필드만 보면 안 된다.

goal completion 판단은 아래 boolean들을 같이 봐야 한다.
brain_web_evidence_pass
full_thesis_production_pass
all_archetype_replay_pass
meaningful_operational_stage_pass
goal_completion_ready
```

## 7. All-archetype replay matrix 대조

기본 production-style:

```text
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 0
guard_replay_ready_count = 0
missing_required_archetype_count = 32
all_archetype_replay_pass = false

status_counts:
  GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY = 4
  SOURCE_GAP_PENDING = 32
```

controlled smoke:

```text
archetype_count = 36
required_archetype_count = 32
source_backed_ready_count = 1
guard_replay_ready_count = 1
missing_required_archetype_count = 31
all_archetype_replay_pass = false

status_counts:
  GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY = 4
  SOURCE_BACKED_SMOKE_AND_GUARD_REPLAY_READY = 1
  SOURCE_GAP_PENDING = 31
```

C06 row in controlled smoke:

```text
archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
replay_status = SOURCE_BACKED_SMOKE_AND_GUARD_REPLAY_READY
replay_scope = controlled_smoke_and_guard_only
fixture_count = 2
source_backed_fixture_count = 2
accepted_claim_count = 14
score_contribution_count = 14
full_thesis_symbols = ["000660", "005930"]
positive_replay_pass = true
guard_replay_pass = true
guard_case_count = 3
guard_case_pass_count = 3
source_proxy_leak_count = 0
```

해석:

```text
C06 positive+guard controlled replay 하나만 ready다.
C01~C32 전체 source-backed replay parity는 여전히 false다.
R13 guard 계약 4개도 source-backed/adversarial replay가 필요하다.
```

## 8. 테스트 artifact 대조

머신리더블 전체 테스트 artifact:

```text
output/test_full_repo_0701/full_unittest_result_artifact.json

status = OK
test_count = 4983
failed_count = 0
error_count = 0
duration_seconds = 166.9824
log_sha256 = 18e7629f2f6d299c706361d9f0819d251474218fa826d2e45a3a2a0438387979
```

해석:

```text
4983 tests OK는 "현재 guard와 문서화된 split이 깨지지 않는다"는 증거다.
goal completion 증거가 아니다.
```

쉬운 예:

```text
차량 계기판 경고등 테스트가 통과했다.
하지만 서울-부산 실제 주행 시험을 통과했다는 뜻은 아니다.
```

## 9. 현재 정말 잘못되기 쉬운 지점

### 9.1 canonical_stage만 보고 운영 Stage로 오독

위험한 읽기:

```text
canonical_stage_distribution에 3-Red 1개가 있으니 운영 Red가 있다.
```

정확한 읽기:

```text
stage_scope가 CENSUS_EVENT_BOARD이면 운영 full-thesis Stage가 아니다.
```

### 9.2 smoke 2개를 production proof로 오독

위험한 읽기:

```text
삼성/하이닉스 FULL_THESIS 2개가 있으니 운영 파이프라인이 된다.
```

정확한 읽기:

```text
controlled_replay smoke에서만 2개다.
Brain/Web live acquisition은 NOT_REQUESTED이고 full_thesis_production_pass=false다.
```

### 9.3 all_archetype_replay_pass=false를 설명 없는 blocker로 방치

이전 위험:

```text
all_archetype_replay_pass=false인데 무엇이 부족한지 모름.
```

현재 상태:

```text
all_archetype_replay_matrix.json이 생겼다.
36개 계약을 펼쳐서 어떤 아키타입이 SOURCE_GAP_PENDING인지 보여준다.
```

남은 문제:

```text
matrix가 생긴 것과 matrix가 pass된 것은 다르다.
```

### 9.4 readiness verdict 이름 오독

위험한 읽기:

```text
ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS면 운영 준비 완료다.
```

정확한 읽기:

```text
이 pass는 "가짜 완료 선언을 막는 상태판" pass다.
운영 준비 완료는 meaningful_operational_stage_pass=true가 되어야 한다.
```

## 10. 다음 패치 방향

### P0. 문서/출력 오독 방지

이미 상당 부분 됐지만 계속 지켜야 한다.

```text
stage_scope를 stage보다 먼저 표시
score_scale을 verified_score보다 먼저 표시
FULL_THESIS_NOT_RUN row에서 verified_score 금지
controlled smoke와 production path를 target_gate에서 분리
all_archetype_replay_matrix 없이 all_archetype_replay_pass=true 금지
```

### P1. Brain/Web live acquisition을 실제 claim까지 닫기

필요한 흐름:

```text
SourceTask 실행
-> 실제 document fetch
-> EvidenceDocument / EvidenceAnchor
-> contract-blind raw assertion
-> adjudicated claim
-> accepted claim
-> primitive mapping
-> ScoreContribution
-> StageCourt trace
-> representative row promotion
```

완료 기준:

```text
brain_web_readiness_gate_audit.verdict = READY_FOR_BRAIN_WEB_EVIDENCE_PASS
web_or_llm_accepted_claim_count > 0
score_contribution_count > 0
stagecourt_trace_count > 0
promoted_representative_row_count > 0
단, 이것만으로 full thesis production pass는 아님
```

### P2. Controlled smoke를 production full thesis로 대체

금지:

```text
fixture rubric point를 production 점수로 사용
controlled_replay를 기본 실행에 섞기
symbol별 특수 점수/Stage 상수 부활
```

필요:

```text
official-first bounded SourceTask
source-backed EvidenceAnchor
claim-backed ScoreContribution
source family / freshness / lifecycle 검증
score delta ledger
full_thesis_production_pass 별도 gate
```

### P3. C01~C32 source-backed replay parity 채우기

각 required archetype마다 필요:

```text
positive replay fixture
guard/adversarial replay fixture
source_proxy_only production score leak = 0
future leakage = 0
wrong subject hard break = 0
UNKNOWN을 PRESENT/ABSENT로 바꾸지 않음
```

현재 matrix 기준 우선순위:

```text
1. C06 guard replay부터 닫기
2. C08/C15/C17/C24/C28처럼 과거 연구에서 URL 경계가 강한 아키타입을 source-backed fixture로 승격
3. 나머지 C01~C32 positive/guard replay 확장
4. R13 guard contract 4개 adversarial replay 추가
```

### P4. 오래된/타사/정상 리스크 오귀속 방지 유지

반드시 유지할 원칙:

```text
오래된 사건 != 현재 OPEN risk
타사 사건 != target risk
정상 감사의견 != accounting hard break
검색 결과에 남아 있음 != 현재 유효
UNKNOWN != PRESENT
```

쉬운 예:

```text
2020년에 어떤 회사의 감사 이슈가 검색됐다고 해서
2026년 삼성전자 hard break로 넣으면 안 된다.

먼저 주체가 삼성전자인지,
현재도 OPEN인지,
최신 감사보고서나 후속 공시로 해소됐는지 확인해야 한다.
확인 못 하면 현재 risk 점수는 0이고 follow-up 대상이다.
```

## 11. 다음 에이전트 공격 질문

다음 에이전트는 아래 질문에 답하지 못하면 pass를 주면 안 된다.

```text
1. 기본 production-style output에서 FULL_THESIS row가 정말 0개인가?
2. controlled smoke output의 FULL_THESIS 2개가 production path와 분리되어 있는가?
3. 72/88점이 총점 상수에서 오지 않고 ScoreContribution.raw_points 합산인가?
4. primitive별 smoke point가 production 점수로 쓰일 수 없다는 표시가 충분한가?
5. stage_scope=CENSUS_EVENT_BOARD row를 운영 Stage로 읽는 출력/문서가 남아 있나?
6. readiness_verdict.blockers=[]를 goal completion으로 오해할 수 있나?
7. goal_completion_audit.goal_completion_ready는 여전히 false인가?
8. brain_web_evidence_pass=false인데 meaningful_operational_stage_pass가 true가 되는 우회가 있나?
9. full_thesis_production_pass=false인데 target_gate=full_thesis가 성공하는 우회가 있나?
10. all_archetype_replay_matrix 없이 all_archetype_replay_pass가 true가 되는 우회가 있나?
11. matrix가 36개 계약을 모두 포함하는가?
12. required 32개 중 source-backed positive/guard parity가 모두 닫혔는가?
13. source_proxy_only나 evidence_url_pending claim이 score contribution으로 들어오는가?
14. C06 positive smoke만 보고 C01~C32 전체 replay parity를 통과시키는가?
15. C06 guard_replay_pass=false인데 Green/production pass를 허용하는가?
16. Brain/Web live acquisition이 NOT_REQUESTED인데 production readiness로 포장되는가?
17. FULL_THESIS_NOT_RUN row에 verified_score가 붙는가?
18. EVENT_WEIGHTED_PARTIAL score를 FULL_E2R_100으로 읽는 alias가 있는가?
19. test_count=4983 OK를 goal completion proof로 쓰는 문구가 있는가?
20. docs/operational과 output/test_* 산출물이 서로 다른 최신 상태를 말하는가?
```

## 12. 현재 판정

현재 완료된 것:

```text
1. 기본 실행에서 fake FULL_THESIS row를 만들지 않음
2. controlled smoke와 production-style 실행 분리
3. controlled smoke 점수를 총점 상수 대신 ScoreContribution 합산으로 계산
4. all_archetype_replay_matrix.json 생성
5. matrix를 readiness/goal audit/manifest에 연결
6. full repo 4983 tests OK
```

아직 완료가 아닌 것:

```text
1. Brain/Web live acquisition -> accepted claim -> score -> Stage promotion
2. production full thesis pass
3. C01~C32 all-archetype source-backed positive/guard replay parity
4. C06 guard replay
5. R13 guard contract adversarial replay
6. meaningful_operational_stage_pass
7. goal_completion_ready
```

최종 한 문장:

> 지금 Census v4는 "틀린 Stage를 만들지 않게 막는 상태판"으로는 전진했지만, "실제 운영 Stage를 충분한 증거로 산출하는 파이프라인"은 아직 아니다. 다음 패치는 상태판을 더 꾸미는 것이 아니라, Brain/Web live source에서 claim-backed score contribution을 만들고 전 아키타입 replay matrix를 채우는 쪽이어야 한다.

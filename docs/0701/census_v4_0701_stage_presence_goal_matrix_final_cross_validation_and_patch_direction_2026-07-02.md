# Census v4 0701 Stage Presence / Goal Matrix Final Cross Validation

> 최신 기준에서는 이 문서가 부분 superseded됐다. 현재 단일 진실은
> `census_v4_0701_latest_c06_source_backed_replay_stage_truth_and_next_patch_packet_2026-07-02.md`를 우선한다.
> 특히 `C06_GUARD_REPLAY_PASS`는 최신 canonical output에서 pass이고,
> goal matrix는 17개 중 12 pass / 5 pending이다.

작성 시점: 2026-07-02 KST  
repo: `/home/eorb915/projects/stock_agent`  
as_of_date: `2026-07-01`

## 한 줄 결론

```text
Stage가 있는 행은 있다.
하지만 현재 canonical output의 Stage는 전부 CENSUS_EVENT_BOARD 상태판 Stage이고,
운영 FULL_THESIS / FULL_E2R_100 Stage row는 0개다.
```

쉽게 말하면:

```text
지금은 전 종목 출석부와 일일 이벤트 상태표는 만들어졌다.
하지만 각 종목의 정식 100점짜리 투자 논리 답안지는 아직 canonical run에서 0장이다.
```

따라서 현재 상태를 이렇게 부르면 안 된다.

```text
나쁜 표현:
  "전체 KRX 운영 Stage 지도 완성"
  "삼성전자/하이닉스 운영 점수 확정"
  "Brain/Web agentic evidence pass"

맞는 표현:
  "가짜 완료를 막는 Census event-board 상태판은 생성됨"
  "goal completion은 17개 hard gate 중 11개 pass, 6개 pending"
  "production full-thesis / Brain-Web / all-archetype replay는 아직 미완료"
```

## 이번에 직접 재검증한 산출물

기준 output:

```text
canonical:
  output/census_v4/2026-07-01

production-style anti-fake 검증 output:
  output/test_census_v4_verified_full_tests

controlled smoke output:
  output/test_census_v4_verified_full_tests_smoke

full unittest artifact:
  output/test_full_repo_0701/full_unittest_result_artifact.json
```

최신 full unittest artifact:

```text
status = OK
test_count = 4992
failed_count = 0
error_count = 0
duration_seconds = 174.133
log_sha256 = 60bb4c92382b9a66a097b74d1678a0624081ce98f1df5c400463c201a2a7424c
```

재생성 명령:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/test_census_v4_verified_full_tests \
  --v3-output-root output/census_v3/2026-07-01 \
  --target-gate anti_fake \
  --write-operational-docs false \
  --test-result-summary full_repo_unittest_ok \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json

PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/test_census_v4_verified_full_tests_smoke \
  --v3-output-root output/census_v3/2026-07-01 \
  --full-thesis-smoke-mode controlled_replay \
  --target-gate full_thesis_smoke \
  --write-operational-docs false \
  --test-result-summary full_repo_unittest_ok \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json

PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --target-gate anti_fake \
  --write-operational-docs auto \
  --test-result-summary full_repo_unittest_ok \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json
```

## Canonical output의 실제 Stage 상태

파일:

```text
output/census_v4/2026-07-01/census_stage_summary.json
```

현재 값:

```text
stage_status_count = 3391

stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3391

score_scope_distribution:
  EVENT_WEIGHTED_PARTIAL = 67
  NO_SCORE = 3324

canonical_stage_distribution:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

verified_score_present_count = 0
full_e2r_verified_score_count = 0
```

해석:

```text
Stage label은 3391개 있다.
하지만 모두 CENSUS_EVENT_BOARD다.
FULL_THESIS row는 canonical output에 없다.
FULL_E2R_100 verified score도 canonical output에 없다.
```

쉬운 예:

```text
Stage0:
  "이번 전체 점검에서 현재 catalyst가 확인되지 않음"
  != "나쁜 종목 0점"

Stage1:
  "공식 이벤트/일일 event watch가 있음"
  != "전체 투자 논리 Stage1"

Stage2:
  "material gap 또는 추가 확인이 필요한 이벤트 상태"
  != "Green 직전 thesis 후보 확정"

3-Red:
  "event-board risk review"
  != "기존 thesis가 깨진 4C"
```

## 샘플 row 교차검증

파일:

```text
output/census_v4/2026-07-01/census_stage_map.jsonl
```

현재 canonical row 예시:

```text
000660 SK하이닉스:
  canonical_stage = 1
  stage_scope = CENSUS_EVENT_BOARD
  operator_stage_use = NOT_FULL_THESIS_STAGE
  operator_score_use = NOT_FULL_E2R_SCORE
  score_scope = EVENT_WEIGHTED_PARTIAL
  daily_event_evidence_score = 4.0
  full_e2r_verified_score = null
  full_thesis_stage = FULL_THESIS_NOT_RUN
  full_thesis_score_valid_status = NOT_SCORED

005930 삼성전자:
  canonical_stage = 1
  stage_scope = CENSUS_EVENT_BOARD
  operator_stage_use = NOT_FULL_THESIS_STAGE
  operator_score_use = NOT_FULL_E2R_SCORE
  score_scope = EVENT_WEIGHTED_PARTIAL
  daily_event_evidence_score = 4.0
  full_e2r_verified_score = null
  full_thesis_stage = FULL_THESIS_NOT_RUN
  full_thesis_score_valid_status = NOT_SCORED

001470 삼부토건:
  canonical_stage = 2
  stage_scope = CENSUS_EVENT_BOARD
  stage_decision_status = PENDING_MATERIAL_GAPS
  daily_event_evidence_score = 4.4
  full_e2r_verified_score = null

030350 드래곤플라이:
  canonical_stage = 3-Red
  stage_scope = CENSUS_EVENT_BOARD
  stage_decision_status = RISK_REVIEW
  daily_event_evidence_score = 4.0
  full_e2r_verified_score = null
```

중요한 해석:

```text
삼성전자와 SK하이닉스가 canonical output에서 Stage1이라고 해서
C06/HBM thesis가 Stage1이라는 뜻이 아니다.

그 row는 "일일 공식 이벤트 watch" 상태다.
HBM 고객 배정, capacity sold-out, revenue mix, FCF bridge를 모두 평가한 full thesis row가 아니다.
```

## Controlled smoke output은 무엇을 증명하고 무엇을 증명하지 못하나

파일:

```text
output/test_census_v4_verified_full_tests_smoke/census_stage_summary.json
output/test_census_v4_verified_full_tests_smoke/samsung_hynix_full_thesis_smoke.json
output/test_census_v4_verified_full_tests_smoke/full_thesis_production_audit.json
```

controlled smoke summary:

```text
stage_scope_distribution:
  CENSUS_EVENT_BOARD = 3389
  FULL_THESIS = 2

score_scope_distribution:
  EVENT_WEIGHTED_PARTIAL = 65
  FULL_E2R_100 = 2
  NO_SCORE = 3324

verified_score_present_count = 2
full_e2r_verified_score_count = 2
```

controlled smoke의 두 row:

```text
000660 SK하이닉스:
  stage_scope = FULL_THESIS
  canonical_stage = 3-Yellow
  full_e2r_verified_score = 88.0
  score_scale = FULL_E2R_100
  accepted_claim_count = 7
  full_thesis_primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY

005930 삼성전자:
  stage_scope = FULL_THESIS
  canonical_stage = 2
  base_stage = Stage2-Watch
  full_e2r_verified_score = 72.0
  score_scale = FULL_E2R_100
  accepted_claim_count = 7
  full_thesis_primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

하지만 production audit:

```text
production_pass_allowed = false
production_full_thesis_row_count = 0
controlled_smoke_full_thesis_row_count = 2
status = PENDING_FULL_THESIS_PRODUCTION
blockers = ["production_full_thesis_not_requested_or_no_rows"]
```

해석:

```text
controlled smoke는 "FULL_THESIS 배관이 점수를 합산할 수 있다"를 확인한다.
하지만 "실제 운영에서 Brain/Web/공식 source가 원문을 수집하고,
LLM extractor가 claim을 뽑고,
그 claim으로 production full thesis를 확정했다"는 증거가 아니다.
```

쉬운 예:

```text
모의시험 답안지 2장을 채점해 본 것은 맞다.
하지만 실제 시험장에서 전교생 답안지를 걷은 것은 아니다.
```

## Goal requirement matrix 교차검증

파일:

```text
output/census_v4/2026-07-01/goal_requirement_matrix_audit.json
output/census_v4/2026-07-01/goal_completion_audit.json
docs/operational/census_mode_v4_goal_requirement_matrix_audit.json
```

현재 canonical matrix:

```text
goal_completion_minimum_pass = false
meaningful_operational_stage_requirement_pass = false
brain_web_requirement_pass = false
production_full_thesis_requirement_pass = false

required_goal_completion_count = 17
required_goal_completion_pass_count = 11
required_goal_completion_pending_count = 6
required_goal_completion_fail_count = 0
```

pending gate:

```text
FULL_THESIS_SMOKE_PASS
FULL_THESIS_PRODUCTION_PASS
BRAIN_WEB_EVIDENCE_PASS
ALL_ARCHETYPE_SOURCE_BACKED_REPLAY_PASS
CONTROLLED_SEMANTIC_REPLAY_PASS
C06_GUARD_REPLAY_PASS
```

`goal_completion_audit.json` blockers:

```text
brain_web_evidence_pass_false
full_thesis_smoke_pending
full_thesis_production_pass_false
source_backed_replay_parity_all_archetypes_pending
controlled_semantic_replay_pending
goal_requirement_matrix_pass_false
```

중요한 판단:

```text
현재 goal_completion_ready=false는 정상이다.
이 상태에서 true가 나오면 그게 버그다.
```

## Brain/Web Evidence gate 상태

파일:

```text
output/census_v4/2026-07-01/brain_web_readiness_gate_audit.json
```

현재 값:

```text
llm_planner_call_count = 0
web_search_task_count = 0
web_fetched_document_count = 0
llm_claim_extractor_attempt_count = 0
web_or_llm_accepted_claim_count = 0

minimum_required_counts:
  llm_planner_call_count = 30
  web_search_task_count = 20
  web_search_call_count = 20
  web_fetched_document_count = 10
  llm_claim_extractor_attempt_count = 10
  web_or_llm_accepted_claim_count = 3
```

해석:

```text
canonical run은 Brain/Web evidence pass를 시도한 run이 아니다.
따라서 Brain/Web pass라고 부르면 안 된다.
```

쉬운 예:

```text
인터넷 조사 시험을 아직 시작하지 않았는데,
"인터넷 조사 통과"라고 도장을 찍으면 안 된다.
```

## All-archetype / semantic replay 상태

파일:

```text
output/census_v4/2026-07-01/all_archetype_replay_matrix.json
output/census_v4/2026-07-01/controlled_semantic_replay_audit.json
output/census_v4/2026-07-01/c06_guard_replay_audit.json
```

현재 all-archetype replay:

```text
all_archetype_replay_pass = false
required_archetype_count = 32
source_backed_ready_count = 0
guard_replay_ready_count = 0
missing_required_archetype_count = 32
```

현재 controlled semantic replay:

```text
controlled_semantic_replay_pass = false
case_count = 10
pass_count = 4
pending_count = 6
fail_count = 0
```

pending controlled semantic cases:

```text
C06_HBM_POSITIVE_AND_QUALIFICATION_LAG_GUARD
C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD
C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD
C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
C24_CLINICAL_BINARY_EVENT_GUARD
C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

현재 C06 guard:

```text
guard_replay_pass = false
positive_semantic_replay_ready = false
blockers = ["c06_positive_replay_required_before_guard_pass"]
```

해석:

```text
현재는 known-bad 방어 일부가 통과했지만,
아키타입별 positive/guard source-backed replay parity는 아직 닫히지 않았다.
```

쉬운 예:

```text
"월덱스 감사의견을 삼성전자 회계 리스크로 오인하지 않음" 같은 방어 테스트는 통과했다.
하지만 "C06 HBM sold-out / qualification lag / revenue mix를 실제 source-backed claim으로 제대로 stage화함"은 아직 대기다.
```

## 그래서 지금 뭔가 잘못되고 있나?

정확히 나누면 이렇다.

```text
잘 되고 있는 부분:
  가짜 완료를 막는 audit는 작동한다.
  event-board Stage와 full-thesis Stage를 분리한다.
  controlled smoke를 production pass로 인정하지 않는다.
  full tests artifact가 machine-readable로 연결된다.

아직 안 된 부분:
  canonical run에서 production full-thesis row가 0개다.
  Brain/Web planner/search/fetch/extractor가 canonical evidence pass를 만들지 않았다.
  C01~C32 required archetype source-backed replay가 0/32이다.
  controlled semantic replay도 10개 중 6개가 pending이다.
```

그러므로 답은:

```text
"Stage가 아예 없는 것은 아니다."
"하지만 운영 Stage라고 부를 수 있는 애들은 canonical run 기준 아직 없다."
```

## 다음 패치 방향

### 1. 절대 하지 말아야 할 shortcut

```text
controlled smoke 2개를 production full-thesis row로 인정하지 말 것
event-board Stage1/2/Red를 full thesis Stage로 승격하지 말 것
Brain/Web disabled 또는 not-requested run을 Brain/Web pass로 처리하지 말 것
source_proxy_only 연구자료를 운영 replay 정답으로 쓰지 말 것
all-archetype replay 0/32 상태에서 threshold를 낮춰 goal completion을 true로 만들지 말 것
```

### 2. 먼저 닫아야 할 작은 루프

우선 `CONTROLLED_SEMANTIC_REPLAY_PASS`와 `C06_GUARD_REPLAY_PASS`부터 닫아야 한다.

필요 작업:

```text
1. C06 positive source-backed replay를 만든다.
2. C06 qualification-lag guard가 positive replay와 함께 통과하는지 확인한다.
3. C08, C15, C17, C24, C28 pending semantic cases를 source-backed fixture로 만든다.
4. 각 fixture는 EvidenceDocument + EvidenceAnchor + EvidenceClaim + PrimitiveMapping + ScoreContribution까지 이어져야 한다.
```

예:

```text
나쁜 replay:
  연구 MD에 "HBM sold-out"이라고 적혀 있으니 C06 pass.

좋은 replay:
  실제 원문 URL/PDF/table anchor에서 claim을 뽑고,
  subject가 대상 회사인지 확인하고,
  event_date/as_of_date가 맞고,
  C06 primitive에 mapping되고,
  그 claim id가 score contribution에 붙는다.
```

### 3. 그다음 Brain/Web evidence pass를 실제로 열어야 한다

필요 조건:

```text
llm_planner_call_count >= 30
web_search_task_count >= 20
web_search_call_count >= 20
web_fetched_document_count >= 10
llm_claim_extractor_attempt_count >= 10
web_or_llm_accepted_claim_count >= 3
```

단, 숫자만 채우면 안 된다.

```text
검색 task -> fetched document -> anchor -> claim -> mapping -> primitive -> score contribution
```

이 chain이 남아야 한다.

쉬운 예:

```text
뉴스 20개 URL만 긁어오면 pass가 아니다.
그 뉴스 중 원문 문장 하나가 어떤 claim이 됐고,
그 claim이 왜 삼성전자/하이닉스 또는 해당 회사에 직접 귀속되는지까지 남아야 한다.
```

### 4. production full-thesis row는 controlled smoke와 별도다

다음 패치는 canonical production full-thesis runner가 실제 후보에 대해 다음을 수행해야 한다.

```text
1. event-board row 중 full-thesis refresh 대상 후보를 고른다.
2. 기존 ledger와 source task를 가져온다.
3. 부족한 primitive를 Brain/Web 또는 official-first source task로 채운다.
4. source-backed claim이 충분하면 FULL_THESIS row를 만든다.
5. 부족하면 낮은 점수로 확정하지 않고 PENDING_FULL_THESIS_REFRESH로 남긴다.
```

예:

```text
삼성전자:
  "공식 이벤트 1개 있으니 Stage1"에서 멈추면 event-board다.
  C06/HBM full thesis를 하려면 고객 배정, capacity, revenue mix, FCF/revision bridge를 claim-backed로 다시 채워야 한다.
```

### 5. 마지막은 C01~C32 all-archetype replay다

현재는:

```text
required_archetype_count = 32
source_backed_ready_count = 0
guard_replay_ready_count = 0
```

목표는:

```text
각 required archetype마다
  positive source-backed replay
  guard/negative replay
  lifecycle/currentness check
  wrong-subject/polarity/future-leakage check
```

가 있어야 한다.

## 외부 리뷰어가 공격해야 할 체크리스트

다음 질문 중 하나라도 답이 "아니오"면 완료가 아니다.

```text
1. canonical output에 FULL_THESIS row가 있는가?
2. 그 row의 score_scope가 FULL_E2R_100인가?
3. full_e2r_verified_score가 null이 아닌가?
4. ScoreContribution마다 support claim id가 있는가?
5. support claim마다 EvidenceAnchor가 있는가?
6. anchor가 실제 원문 URL/PDF/table/API/XBRL record에 닿는가?
7. claim subject가 target company와 직접 scope인가?
8. event_date와 as_of_date가 분리되어 검증됐는가?
9. old negative claim이 current risk로 자동 승격되지 않는가?
10. 타사 정상 감사의견이 target 회계 risk로 들어가지 않는가?
11. Brain/Web pass가 disabled/not-requested run에서 나오지 않는가?
12. LLM planner/search/fetch/extractor count가 leaf artifact로 증명되는가?
13. controlled smoke가 production full-thesis pass로 대체되지 않는가?
14. source_proxy_only 연구자료가 운영 score contribution으로 들어가지 않는가?
15. C06 positive replay 없이 C06 guard pass가 true가 되지 않는가?
16. C08/C15/C17/C24/C28 semantic replay pending이 닫혔는가?
17. C01~C32 source-backed positive/guard replay가 모두 있는가?
18. Stage0이 "나쁜 종목"으로 해석되지 않게 operator labels가 남는가?
19. Stage1/2/Red event-board row가 full thesis row와 섞이지 않는가?
20. goal_requirement_matrix_audit.json이 17/17 pass가 아니면 goal_completion_ready가 false인가?
```

## 최종 판단

현재 Census v4는 이전처럼 아무 점수나 뱉는 상태보다는 훨씬 낫다.

하지만 이유는 "운영 점수/Stage가 잘 나와서"가 아니다.

이유는:

```text
운영 점수/Stage라고 부르면 안 되는 것을
artifact가 스스로 막고 있기 때문이다.
```

다음 패치의 목표는 gate를 완화하는 것이 아니라, pending 6개를 실제 evidence chain으로 닫는 것이다.

최종 궁극 목표:

```text
전 종목은 CensusAssessmentEvent로 상태판에 올라온다.
CandidateEvent와 source-backed claim이 있는 종목만 점수 재료를 얻는다.
FULL_THESIS는 claim-backed primitive가 충분할 때만 열린다.
부족하면 낮은 점수 확정이 아니라 Pending으로 남긴다.
Brain/Web/LLM은 점수를 직접 만들지 않고, 원문에서 claim을 작성한다.
deterministic StageCourt는 claim-backed contribution만 합산한다.
```

이 조건이 충족되기 전까지 `goal.md`, `goal2.md`, `goal3.md`는 완료가 아니다.

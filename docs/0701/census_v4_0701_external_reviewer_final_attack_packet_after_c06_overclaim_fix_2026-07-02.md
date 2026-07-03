# Census v4 0701 External Reviewer Final Attack Packet After C06 Overclaim Fix

작성일: 2026-07-02 KST
repo: `/home/eorb915/projects/stock_agent`
as_of_date: `2026-07-01`

## 한 줄 결론

```text
Stage label은 있다.
하지만 기본 production-style 산출물에는 운영 FULL_THESIS Stage가 0개다.

controlled smoke에는 삼성전자/하이닉스 FULL_THESIS 2개가 있지만,
그것은 배관 smoke일 뿐 source-backed semantic replay ready가 아니다.
```

쉬운 예:

```text
기본 production-style:
전교생 3391명의 출석부와 상태판은 있다.
하지만 정식 기말고사 답안지 채점은 0명이다.

controlled smoke:
삼성전자/하이닉스 2명에게 모의 답안지를 흘려서 채점 배관은 확인했다.
하지만 그 모의 답안지가 원문 의미 검증까지 통과한 정식 답안지는 아니다.
```

## 왜 이 문서를 새로 썼나

기존 0701 문서 중 일부는 `controlled smoke C06 positive+guard ready = 1`이라고 썼다.
이번 재검산에서 그 표현은 너무 강하다고 판단했다.

이유:

```text
1. C06 controlled smoke는 FULL_THESIS row, claim, ScoreContribution 배관을 만든다.
2. 하지만 smoke claim은 contract-blind extractor가 원문에서 새로 뽑은 claim이 아니다.
3. 특히 삼성전자 positive smoke claim 중 일부가 C06 guard URL과 같은 URL을 positive/current처럼 재사용했다.
4. 따라서 이것을 source-backed semantic replay ready로 세면 또 과장이다.
```

구체 예:

```text
삼성전자 smoke positive:
  primitive = named_customer_or_customer_quality
  source_url = Reuters 2024-05-23 Samsung HBM failing Nvidia tests
  smoke polarity = POSITIVE
  smoke temporal_status = CURRENT

같은 URL은 C06 guard case에서는:
  input_claim_class = qualification_lag
  expected_current_score_eligible = false
  expected_hard_break_allowed = false
  expected_green_unlock_allowed = false

즉 같은 자료를 한쪽에서는 positive/current 점수 재료처럼,
다른 한쪽에서는 guard/follow-up 자료처럼 보는 충돌이 있었다.
```

이번 패치의 핵심은 이것이다.

```text
controlled wiring smoke != source-backed semantic replay
```

배관 smoke는 남긴다. 다만 all-archetype replay ready에는 세지 않는다.

## 이번에 적용한 최소 패치

변경 파일:

```text
src/e2r/census/census_runner_v4.py
src/e2r/census/known_bad_regression.py
tests/test_census_v4_all_archetype_replay_matrix.py
tests/test_census_v4_goal_required_audits.py
tests/test_census_v4_artifact_manifest.py
tests/test_census_v4_known_bad_regression.py
docs/0701/README.md
docs/0701/census_v4_0701_external_reviewer_final_attack_packet_after_c06_overclaim_fix_2026-07-02.md
```

### 1. C06 guard audit 상태 분리

이전:

```text
positive_replay_ready = true
guard_replay_pass = true
```

문제:

```text
smoke fixture가 URL을 들고 있다는 이유만으로 semantic replay ready처럼 보였다.
```

현재:

```text
positive_wiring_smoke_ready = true
positive_semantic_replay_ready = false
guard_cases_pass = true
guard_replay_pass = false
```

의미:

```text
배관은 닫혔다.
guard fixture 자체도 score leak/hard break false positive 없이 통과했다.
하지만 positive source-backed semantic replay가 아직 아니므로 C06 replay pass는 아니다.
```

### 2. all-archetype matrix 카운트 분리

이전 controlled smoke:

```text
source_backed_ready_count = 1
guard_replay_ready_count = 1
missing_required_archetype_count = 31
C06 replay_status = SOURCE_BACKED_SMOKE_AND_GUARD_REPLAY_READY
```

현재 controlled smoke:

```text
source_backed_ready_count = 0
guard_replay_ready_count = 0
controlled_wiring_smoke_ready_count = 1
missing_required_archetype_count = 32
C06 replay_status = CONTROLLED_WIRING_SMOKE_ONLY_SEMANTIC_REPLAY_PENDING
```

의미:

```text
C06 smoke가 존재한다는 사실은 보존한다.
하지만 C06을 source-backed replay parity 완료로 세지 않는다.
```

## 최신 산출물 교차검증

### 0. Controlled semantic replay audit

새 artifact:

```text
controlled_semantic_replay_audit.json
docs/operational/census_mode_v4_controlled_semantic_replay_audit.json
```

이 artifact는 `docs/core/goal3.md`가 요구한 controlled replay 묶음을 기계가 읽을 수 있게 펼친다.

현재 controlled smoke 기준:

```text
controlled_semantic_replay_pass = false
case_count = 10
pass_count = 4
pending_count = 6
fail_count = 0

PASS:
  WRONG_SUBJECT_RISK_FIXTURE
  OLD_RISK_RESOLVED_FIXTURE
  PROVIDER_FAILURE_PENDING_FIXTURE
  SEMANTIC_CONTRACT_GUARD_FIXTURE

PENDING_SOURCE_BACKED_SEMANTIC_REPLAY:
  C06_HBM_POSITIVE_AND_QUALIFICATION_LAG_GUARD
  C08_TEST_SOCKET_CUSTOMER_ORDER_PROFILE_ONLY_GUARD
  C15_MATERIAL_SPREAD_PASS_THROUGH_RAW_COMMODITY_GUARD
  C17_CHEMICAL_SPREAD_REALIZED_MARGIN_BRIDGE_GUARD
  C24_CLINICAL_BINARY_EVENT_GUARD
  C28_SOFTWARE_SECURITY_RETENTION_BRIDGE_GUARD
```

쉬운 예:

```text
월덱스 감사의견 오귀속, 과거 리스크 해소, provider failure, 비매출 계약 오인 같은 전역 방어막은 있다.
하지만 C08/C15/C17/C24/C28 같은 실제 아키타입별 positive+guard 답안지는 아직 source-backed semantic replay로 작성되지 않았다.
```

추가된 old-risk-resolved 회귀:

```text
case_id = old_risk_resolved_not_current_hard_break
expected = resolved target accounting/trust risk is lifecycle context, not current score evidence or 4C hard break

observed:
  score_eligible = false
  eligibility_reasons includes temporal_not_allowed:RESOLVED
  primitive_status = RESOLVED
  support_claim_ids = []
  transition_overlay = NONE
```

의미:

```text
2020년에 어떤 회계/감사 이슈가 있었다는 자료가 있어도,
2026년 현재 최신 공시가 해소/정상 상태를 증명하면 현재 리스크 점수나 4C 전이로 쓰지 않는다.
```

### 1. 기본 production-style output

경로:

```text
output/test_census_v4_verified_full_tests
output/census_v4/2026-07-01
```

`census_stage_status.jsonl` 직접 집계:

```text
row_count = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3391

canonical_stage:
  0 = 3306
  1 = 54
  2 = 30
  3-Red = 1

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

operator_score_use:
  NOT_FULL_E2R_SCORE = 3391

FULL_THESIS row = 0
FULL_E2R_SCORE row = 0
```

`census_stage_summary.json`:

```text
full_thesis_stage_distribution = {"FULL_THESIS_NOT_RUN": 3391}
full_e2r_verified_score_count = 0
event_evidence_score_count = 67
candidate_event_count = 226
score_eligible_candidate_event_count = 92
```

`readiness_verdict.json`:

```text
verdict = ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
meaningful_operational_stage_pass = false
brain_web_evidence_pass = false
full_thesis_smoke_pass = false
full_thesis_production_pass = false
all_archetype_replay_pass = false
```

`goal_completion_audit.json`:

```text
goal_completion_ready = false
brain_web_evidence_pass_allowed = false
full_thesis_smoke_pass_allowed = false
full_thesis_production_pass_allowed = false
c06_guard_replay_pass_allowed = false
c06_guard_replay_status = C06_GUARD_REPLAY_PENDING
all_archetype_replay_pass_allowed = false

blockers:
  brain_web_evidence_pass_false
  full_thesis_smoke_pending
  full_thesis_production_pass_false
  source_backed_replay_parity_all_archetypes_pending
```

`all_archetype_replay_matrix.json`:

```text
required_archetype_count = 32
source_backed_ready_count = 0
guard_replay_ready_count = 0
controlled_wiring_smoke_ready_count = 0
missing_required_archetype_count = 32

status_counts:
  SOURCE_GAP_PENDING = 32
  GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY = 4
```

해석:

```text
기본 output은 전 종목 상태판으로는 안전하다.
하지만 운영 full-thesis Stage/점수 지도는 아니다.
```

### 2. Controlled smoke output

경로:

```text
output/test_census_v4_verified_full_tests_smoke
```

`census_stage_status.jsonl` 직접 집계:

```text
row_count = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3389
  FULL_THESIS = 2

canonical_stage:
  0 = 3306
  1 = 52
  2 = 31
  3-Red = 1
  3-Yellow = 1

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3389
  FULL_THESIS_STAGE = 2

operator_score_use:
  NOT_FULL_E2R_SCORE = 3389
  FULL_E2R_SCORE = 2
```

FULL_THESIS rows:

```text
000660 SK하이닉스:
  canonical_stage = 3-Yellow
  verified_score = 88.0
  full_thesis_primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY

005930 삼성전자:
  canonical_stage = 2
  base_stage_display = FULL_THESIS_STAGE2_WATCH
  verified_score = 72.0
  full_thesis_primary_archetype = C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

중요:

```text
이 두 row는 full thesis 배관 smoke다.
production full thesis row가 아니다.
semantic source-backed replay ready도 아니다.
```

`goal_completion_audit.json`:

```text
goal_completion_ready = false
brain_web_evidence_pass_allowed = false
full_thesis_smoke_pass_allowed = true
full_thesis_production_pass_allowed = false
c06_guard_replay_pass_allowed = false
c06_guard_replay_status = C06_GUARD_REPLAY_PENDING
all_archetype_replay_pass_allowed = false

blockers:
  brain_web_evidence_pass_false
  full_thesis_production_pass_false
  source_backed_replay_parity_all_archetypes_pending
```

`all_archetype_replay_matrix.json`:

```text
required_archetype_count = 32
source_backed_ready_count = 0
guard_replay_ready_count = 0
controlled_wiring_smoke_ready_count = 1
missing_required_archetype_count = 32

status_counts:
  CONTROLLED_WIRING_SMOKE_ONLY_SEMANTIC_REPLAY_PENDING = 1
  SOURCE_GAP_PENDING = 31
  GUARDRAIL_CONTRACT_ONLY_PENDING_SOURCE_BACKED_REPLAY = 4
```

C06 row:

```text
replay_status = CONTROLLED_WIRING_SMOKE_ONLY_SEMANTIC_REPLAY_PENDING
replay_scope = controlled_wiring_smoke_only
fixture_count = 2
url_backed_wiring_fixture_count = 2
source_backed_fixture_count = 0
controlled_wiring_smoke_pass = true
positive_replay_pass = false
guard_replay_pass = false

semantic_blockers:
  controlled_smoke_claims_are_fixture_mapped_not_contract_blind_extracted
  samsung_positive_smoke_reuses_c06_guard_urls
```

`c06_guard_replay_audit.json`:

```text
positive_wiring_smoke_ready = true
positive_semantic_replay_ready = false
guard_cases_pass = true
guard_replay_pass = false
guard_case_count = 3
guard_case_pass_count = 3
positive_guard_url_reuse_count = 3

semantic_blockers:
  controlled_smoke_claims_are_fixture_mapped_not_contract_blind_extracted
  samsung_positive_smoke_reuses_c06_guard_urls

blockers:
  c06_positive_semantic_replay_required_before_guard_pass
  controlled_smoke_claims_are_fixture_mapped_not_contract_blind_extracted
  samsung_positive_smoke_reuses_c06_guard_urls
```

해석:

```text
배관 smoke는 통과했다.
하지만 C06 semantic replay는 아직 pending이다.
```

## 테스트 증거

Targeted:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_all_archetype_replay_matrix \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_artifact_manifest \
  tests.test_census_v4_full_thesis_smoke_tasks \
  -v
```

결과:

```text
Ran 14 tests
OK
```

Census v4 suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_census_v4*.py' -v
```

결과:

```text
Ran 102 tests
OK
```

전체 repo:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v
```

결과:

```text
status = OK
test_count = 4984
failed_count = 0
error_count = 0
duration_seconds = 171.5112
log_sha256 = 059a04ec3d70271d1e94d123034c82bbadd7b12b39ea0734dfdb1092d3a5dad1
```

## 재현 명령

기본 production-style output:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/test_census_v4_verified_full_tests \
  --v3-output-root output/census_v3/2026-07-01 \
  --target-gate anti_fake \
  --write-operational-docs false \
  --test-result-summary full_repo_unittest_ok \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json
```

Controlled smoke output:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/test_census_v4_verified_full_tests_smoke \
  --v3-output-root output/census_v3/2026-07-01 \
  --full-thesis-smoke-mode controlled_replay \
  --target-gate full_thesis_smoke \
  --write-operational-docs false \
  --test-result-summary full_repo_unittest_ok \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json
```

Canonical output + `docs/operational` copy:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --v3-output-root output/census_v3/2026-07-01 \
  --target-gate anti_fake \
  --write-operational-docs auto \
  --test-result-summary full_repo_unittest_ok \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json
```

## 다음 에이전트가 먼저 공격해야 할 지점

### A. C06 smoke를 semantic replay로 승격하려 하지 말 것

현재 C06 smoke는 배관 검증이다.
다음 패치에서 해야 할 일은 점수를 또 조정하는 것이 아니다.

필요한 작업:

```text
1. C06 positive fixture를 contract-blind extraction으로 다시 만든다.
2. 원문 anchor span이 실제 quote와 일치하는지 검증한다.
3. subject/target/directness를 검증한다.
4. event_date, as_of_date, lifecycle/current status를 따로 판정한다.
5. qualification lag, partial clearance, supply delay는 positive/current score로 바로 쓰지 않는다.
6. positive claim과 guard claim이 같은 URL을 서로 반대 의미로 쓰면 replay fail이다.
```

쉬운 예:

```text
"Nvidia 테스트 실패" 기사는 고객명 문맥을 포함할 수 있다.
하지만 그것만으로 "named customer positive 점수"를 주면 안 된다.
그 기사의 핵심 claim은 qualification lag이므로 Green unlock이 아니라 guard/follow-up이다.
```

### B. goal3 controlled replay 묶음이 아직 대부분 비어 있음

`docs/core/goal3.md`가 요구한 controlled replay:

```text
C06 HBM positive and qualification-lag guard
C08 test socket customer/order/profile-only guard
C15 material spread pass-through and raw commodity false positive
C17 chemical spread realized margin bridge guard
C24 clinical binary event guard
C28 software/security retention bridge guard
wrong-subject risk fixture
old-risk-resolved fixture
provider failure pending fixture
semantic contract guard fixture
```

현재 상태:

```text
C06:
  wiring smoke exists
  guard cases exist
  semantic replay pending

C08/C15/C17/C24/C28:
  matrix status = SOURCE_GAP_PENDING
  positive_replay_pass = false
  guard_replay_pass = false

wrong-subject/provider failure/semantic contract:
  known_bad_regression에는 일부 deterministic guard가 있음
  all-archetype/source-backed replay matrix에는 아직 통합되지 않음

old-risk-resolved:
  명시 fixture가 아직 부족함
```

### C. Brain/Web gate는 아직 PASS가 아님

기본/controlled smoke 모두:

```text
brain_web_evidence_pass = false
brain_web_readiness_gate_audit.verdict = NOT_REQUESTED
brain_web_mode = disabled
```

즉:

```text
LLM이 실제 웹/IR/뉴스 원문을 읽고 claim을 만든 운영 pass가 아니다.
```

다음 패치에서 Brain/Web을 주장하려면 최소:

```text
llm_planner_call_count > 0
web/naver/trusted_news search task 존재
web_fetched_documents 존재
llm_claim_extractor_attempt_count > 0
accepted claim이 document/anchor/stage trace와 닫힘
snippet_to_score_count = 0
provider_failure_final_score_count = 0
```

이 전부가 leaf artifact로 보여야 한다.

### D. Production full thesis runner가 없음

현재:

```text
full_thesis_production_audit.verdict = PENDING_FULL_THESIS_PRODUCTION
production_full_thesis_row_count = 0
blockers = ["production_full_thesis_runner_not_implemented"]
```

controlled smoke 2개가 있어도 production full thesis pass가 아닌 이유:

```text
FTSMOKE-* source task는 배관 smoke용이다.
실제 production task는 Source Router / Evidence OS / contract-blind extractor / lifecycle adjudicator를 거쳐야 한다.
```

## 다음 패치 순서 제안

### 1. Controlled semantic replay audit 추가

새 artifact 제안:

```text
controlled_semantic_replay_audit.json
```

필드:

```text
case_id
archetype_id
case_type = positive | guard | global_guard
document_id
anchor_id
claim_id
primitive_id
target_scope_status
polarity
temporal_status
lifecycle_status
mapping_status
score_eligible
expected_stage_effect
actual_score_contribution_ids
case_pass
failure_reason
```

이 audit는 smoke fixture row를 그대로 pass시키면 안 된다.
반드시 raw document/anchor/assertion/adjudication/mapping을 거쳐야 한다.

### 2. C06부터 semantic replay로 다시 만들기

필수 C06 positive:

```text
SK하이닉스:
  named customer/customer quality
  qualification/current supply conversion
  capacity allocation/pre-sold
  HBM shipment or revenue mix
  cash/revision conversion

삼성전자:
  Green unlock이 아니라 mixed/Stage2-Watch가 맞는지 검증
  qualification lag는 hard 4C가 아님
  partial clearance는 absolute failure를 supersede할 수 있으나 Green unlock은 아님
```

필수 C06 guard:

```text
qualification lag -> current hard break 금지
supply delay -> current Green unlock 금지
partial clearance -> broad Green qualification으로 과잉 해석 금지
```

### 3. C08/C15/C17/C24/C28 priority replay 추가

우선순위 이유:

```text
goal3가 직접 요구한 아키타입이고,
과거 연구자료에서 positive/false-positive 경계가 비교적 명확하다.
```

각 아키타입의 최소 guard:

```text
C08:
  제품 프로필/수상/개발 성공만으로 customer/order conversion 점수 금지

C15:
  원자재 가격 상승 기사만으로 pass-through/spread/margin 점수 금지

C17:
  화학 spread headline만으로 issuer realized margin/FCF bridge 점수 금지

C24:
  임상 binary event만으로 endpoint/safety/regulatory/runway bridge 완성 금지

C28:
  보안/소프트웨어 키워드만으로 ARR/RPO/renewal/retention 점수 금지
```

### 4. Known-bad global replay를 matrix에 연결

이미 있는 known-bad:

```text
wrong_subject_audit_opinion_not_target_risk
non_revenue_contract_not_contract_quality
source_proxy_score_guard
evidence_url_pending_score_guard
snippet_score_guard
provider_failure_final_score_guard
samsung_hynix_daily_event_not_full_thesis_or_4c
```

추가 필요:

```text
old-risk-resolved fixture
current hard-break quorum fixture
claim lifecycle supersession fixture
positive claim expired/superseded fixture
```

이 guard들은 `known_bad_regression_report.json`에만 있으면 부족하다.
all-archetype/semantic replay readiness에도 연결해야 한다.

### 5. Production full thesis runner 구현

목표:

```text
CandidateEvent
-> SourceTask
-> fetched EvidenceDocument
-> EvidenceAnchor
-> contract-blind RawAssertion
-> target/temporal/lifecycle adjudication
-> primitive mapping
-> PrimitiveState
-> ScoreContribution
-> StageCourt
-> FULL_THESIS stage row
```

금지:

```text
smoke fixture의 rubric_points를 production score로 재사용
LLM-only 추론을 score로 사용
old URL을 current로 강제
query/template 하드코딩으로 missing primitive를 채우는 척하기
```

## 다음 에이전트 리뷰 체크리스트

반드시 물어볼 질문:

```text
1. 기본 output에 FULL_THESIS row가 0개라는 사실을 숨기지 않았나?
2. controlled smoke 2개를 production full thesis로 착각하지 않았나?
3. C06 smoke를 source-backed semantic replay ready로 세지 않았나?
4. 삼성 qualification lag URL이 positive score와 guard에 동시에 쓰이지 않나?
5. old-risk/current-risk lifecycle을 분리했나?
6. provider failure를 low score/Red로 확정하지 않나?
7. source_proxy_only/evidence_url_pending/snippet이 score로 들어가지 않나?
8. Stage0/NoCurrentCatalyst를 부정적 Red처럼 설명하지 않나?
9. C08/C15/C17/C24/C28 priority replay가 실제 claim/anchor/mapping을 거치나?
10. all-archetype replay pass가 false인데 goal_complete를 true로 만들지 않나?
```

## 현재 안전하게 말할 수 있는 것

```text
1. Census v4는 가짜 full universe production 점수/Stage를 기본 output에 넣지 않는다.
2. 전 종목 상태판 row는 3391개 생성된다.
3. 기본 output의 Stage는 CENSUS_EVENT_BOARD 상태판 Stage다.
4. controlled smoke는 삼성전자/하이닉스 FULL_THESIS row 2개 배관을 만든다.
5. controlled smoke 점수는 ScoreContribution 합산으로 만들어진다.
6. C06 guard fixture 3개는 score leak/hard break false positive 없이 평가된다.
7. 그러나 C06 semantic replay는 아직 pass가 아니다.
8. Brain/Web evidence pass, production full thesis pass, all-archetype replay pass는 아직 false다.
```

## 현재 절대 말하면 안 되는 것

```text
1. "전체 종목 운영 Stage/점수 지도가 완성됐다."
2. "삼성전자/하이닉스 운영 full thesis 결과가 production으로 확정됐다."
3. "C06 source-backed positive+guard replay가 완료됐다."
4. "C08/C15/C17/C24/C28 replay가 준비됐다."
5. "Brain/Web/LLM이 실제 원문을 읽고 pass했다."
6. "all-archetype parity가 끝났다."
7. "goal.md/goal2.md/goal3.md가 완료됐다."
```

## 최종 판단

현재 상태는 한 단계 더 정직해졌다.

이전에는:

```text
C06 controlled smoke가 URL을 갖고 있으므로 source-backed ready 1개처럼 보임
```

현재는:

```text
C06 controlled smoke는 wiring smoke 1개로만 인정
semantic replay/source-backed ready는 0개
```

이 방향이 맞다.
다음 패치는 점수표를 다시 만지는 것이 아니라,
raw document에서 claim을 뽑아 lifecycle과 primitive mapping을 거쳐
source-backed semantic replay를 실제로 채우는 쪽이어야 한다.

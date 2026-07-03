# Census v4 Latest Truth Review And Next Patch Plan - 2026-07-01

이 문서는 다음 에이전트가 바로 공격적으로 리뷰할 수 있도록 만든 최신 단일 패킷이다.

대상 질문:

```text
뭔가 잘못되고 있는 게 맞나?
Stage가 있는 애들이 있긴 한가?
있다면 그 Stage는 실제 운영 Stage인가?
0701 작업 후 어디까지 패치됐고, 다음에 무엇을 닫아야 하나?
```

## 한 줄 결론

현재 `output/census_v4/2026-07-01`에는 Stage row가 있다.

하지만 그 Stage는 전부 `CENSUS_EVENT_BOARD` 상태판 label이고,
`FULL_THESIS` 운영 Stage는 아직 0개다.

2026-07-01 최신 enabled Brain/Web smoke에서는 웹 검색, 원문 fetch, LLM claim extractor leaf가 실제로 생겼다.
하지만 웹/LLM accepted claim은 0개라 Brain/Web 운영 Stage로 승격된 row도 0개다.

최신 추가 forensic 문서:

```text
docs/0701/census_v4_enabled_brainweb_leaf_to_claim_gap_forensic_2026-07-01.md
```

쉬운 예:

```text
현재 상태:
  "출석부와 일부 사건 접수표는 잘 만들었다."

아직 아님:
  "모든 종목의 투자 논리 시험지를 끝까지 채점했다."
```

## 최신 검증 기준

최신 검증은 아래 순서로 다시 맞췄다.

```bash
PYTHONPATH=src python -m unittest discover -s tests -v

PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/census_v4/2026-07-01/test_result_artifact_after_claim_provider_patch.json \
  --log output/census_v4/2026-07-01/test_result_artifact_after_claim_provider_patch.log \
  -- python -m unittest discover -s tests -v

PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01 \
  --test-result-artifact output/census_v4/2026-07-01/test_result_artifact_after_claim_provider_patch.json \
  --target-gate anti_fake \
  --fail-on-critical-audit true
```

결과:

```text
manual full test:
  Ran 4959 tests in 156.646s
  OK

machine-readable test artifact:
  status: OK
  test_count: 4954
  failed_count: 0
  error_count: 0
  duration_seconds: 157.5068

Census v4 target gate:
  ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS
```

주의:

```text
일부 기존 0701 문서에는 4942 또는 4951 tests 기록이 남아 있다.
그 문서들은 이전 시점 forensic 기록이다.
이 문서의 최신 로컬 전체 테스트 기준은 4959 tests다.
단 `output/census_v4/2026-07-01/test_result_artifact_after_claim_provider_patch.json`는 이전 canonical artifact라 4954 tests일 수 있다.
```

## 최신 enabled Brain/Web smoke 추가 교차검증

최신 별도 smoke:

```text
/tmp/census_v4_enabled_provider_probe
```

핵심 row count:

```text
planner_runs.jsonl:              22
source_task_executions.jsonl:    106
web_search_tasks.jsonl:            4
web_search_results.jsonl:         40
web_fetched_documents.jsonl:       6
web_rejected_documents.jsonl:      5
claim_extractor_runs.jsonl:        6
accepted_claims.jsonl:            92
score_contributions.jsonl:        92
stagecourt_traces.jsonl:          92
brain_to_claim_trace.jsonl:        0
```

감사 결과:

```text
leaf_artifact_audit: PASS
web_naver_acquisition_audit: REAL_ACQUISITION_PASS
llm_claim_extraction_audit: REAL_EXTRACTION_PASS
brain_web_readiness_gate_audit: BLOCKED
brain_stage_promotion_audit: BLOCKED
readiness_verdict: NOT_READY
```

해석:

```text
웹/LLM leaf는 실제로 생겼다.
하지만 웹/LLM accepted claim은 0개다.
accepted_claims=92는 모두 OpenDART/event-board claim이다.
Brain/Web score contribution, StageCourt trace, promoted census row는 아직 0개다.
```

쉬운 예:

```text
자료를 찾아와서 LLM이 일부 메모까지 남겼지만,
그 메모가 "어느 문서의 어느 문장 때문에 몇 점"이라는 공식 채점지에 아직 붙지 않았다.
```

따라서 최신 올바른 label:

```text
BRAIN_WEB_LEAFS_REAL_BUT_NOT_CUTOVER_READY
```

금지 label:

```text
BRAIN_WEB_EVIDENCE_PASS
MEANINGFUL_OPERATIONAL_STAGE_PASS
FULL_THESIS_SMOKE_PASS
GOAL_COMPLETION_READY
```

### 추가 anchor/decoder 패치 후 smoke

추가 패치 후 별도 smoke:

```text
/tmp/census_v4_enabled_provider_probe_after_decoder_patch
```

핵심 변화:

```text
web_search_tasks: 6
web_search_results: 60
web_fetched_documents: 8
claim_extractor_runs: 8
raw_assertions: 138
adjudicated_claims: 138
Brain/Web raw assertions: 46
Brain/Web LLM raw assertions: 38
Brain/Web raw anchor_verified=True: 46
Brain/Web accepted claims: 0
brain_to_claim_trace: 0
readiness_verdict: NOT_READY
```

해석:

```text
웹/LLM 원문 -> raw/adjudicated claim 장부는 이전보다 좋아졌다.
하지만 아직 accepted mapping이 없으므로 점수와 Stage로 올리면 안 된다.
```

쉬운 예:

```text
이전에는 메모지에 출처가 불안정했다.
이제 메모지에 출처와 문장이 붙었다.
하지만 그 메모가 이번 점수 칸에 맞는 답은 아니어서 채점하지 않는다.
```

### 추가 mapping trace 패치 후 smoke

추가 패치 후 별도 smoke:

```text
/tmp/census_v4_enabled_provider_probe_after_mapping_trace_patch
```

핵심 변화:

```text
web_search_tasks: 4
web_search_results: 40
web_fetched_documents: 8
claim_extractor_runs: 8
raw_assertions: 146
adjudicated_claims: 146
Brain/Web raw assertions: 54
Brain/Web adjudicated claims with document_id: 54 / 54
Brain/Web adjudicated claims with anchor_id: 54 / 54
brain_claim_mapping_trace: 54
Brain/Web accepted claims: 0
brain_to_claim_trace: 0
readiness_verdict: NOT_READY
```

해석:

```text
이제 accepted claim이 0개인 이유가 claim 단위 trace로 보인다.
54개 모두 REJECTED_BEFORE_SCORE이고,
주요 rejection은 wrong-target/primitive mismatch다.
```

쉬운 예:

```text
이전에는 "왜 0점인지"가 시험지 전체 요약으로만 보였다.
이제는 각 답안 옆에 "문제와 맞지 않음", "다른 회사 이야기" 같은 채점 메모가 붙었다.
```

## 산출물 원본

검증 원본:

```text
output/census_v4/2026-07-01/census_stage_status.jsonl
output/census_v4/2026-07-01/census_stage_summary.json
output/census_v4/2026-07-01/readiness_verdict.json
output/census_v4/2026-07-01/goal_completion_audit.json
output/census_v4/2026-07-01/brain_web_readiness_gate_audit.json
output/census_v4/2026-07-01/samsung_hynix_full_thesis_smoke.json
output/census_v4/2026-07-01/test_result_artifact_after_claim_provider_patch.json
docs/operational/census_mode_v4_readiness_verdict.md.json
docs/operational/census_mode_v4_test_result_evidence_audit.json
```

## Stage가 있긴 한가

있다.

최신 `census_stage_status.jsonl` 기준:

```text
row_count: 3391

canonical_stage:
  0: 3306
  1: 54
  2: 30
  3-Red: 1

base_stage:
  Stage0: 3306
  Stage1: 54
  Stage2-Watch: 30
  Red: 1
```

하지만 이 값만 읽으면 오해한다.

같은 row들의 scope는 전부 아래와 같다.

```text
stage_scope:
  CENSUS_EVENT_BOARD: 3391

full_thesis_stage:
  FULL_THESIS_NOT_RUN: 3391

operator_stage_use:
  NOT_FULL_THESIS_STAGE: 3391

operator_score_use:
  NOT_FULL_E2R_SCORE: 3391
```

따라서 정확한 문장은:

```text
Stage label은 있다.
운영 full thesis Stage는 아직 없다.
```

틀린 문장:

```text
3391개 종목의 실제 E2R 100점 Stage가 나왔다.
30개 종목이 운영 Stage2로 확정됐다.
1개 종목이 운영 Stage3-Red로 확정됐다.
```

맞는 문장:

```text
3391개 종목에 Census 상태판 row가 생겼다.
67개 row에는 source-backed event partial score가 붙었다.
full thesis는 전부 아직 실행 전이다.
```

## 삼성전자 / SK하이닉스 교차검증

최신 row:

```text
005930 삼성전자:
  base_stage: Stage1
  canonical_stage: 1
  stage_scope: CENSUS_EVENT_BOARD
  event_evidence_score: 4.0
  daily_event_evidence_score: 4.0
  verified_score: null
  full_e2r_verified_score: null
  full_thesis_stage: FULL_THESIS_NOT_RUN
  full_thesis_score_valid_status: NOT_SCORED
  score_scope: EVENT_WEIGHTED_PARTIAL
  operator_stage_use: NOT_FULL_THESIS_STAGE
  operator_score_use: NOT_FULL_E2R_SCORE

000660 SK하이닉스:
  base_stage: Stage1
  canonical_stage: 1
  stage_scope: CENSUS_EVENT_BOARD
  event_evidence_score: 4.0
  daily_event_evidence_score: 4.0
  verified_score: null
  full_e2r_verified_score: null
  full_thesis_stage: FULL_THESIS_NOT_RUN
  full_thesis_score_valid_status: NOT_SCORED
  score_scope: EVENT_WEIGHTED_PARTIAL
  operator_stage_use: NOT_FULL_THESIS_STAGE
  operator_score_use: NOT_FULL_E2R_SCORE
```

쉬운 예:

```text
삼성전자 4.0점
!= 삼성전자 HBM/C06 투자 논리 4점

삼성전자 4.0점
= 2026-07-01 Census event-board에서 확인된 최근 event partial score
```

`samsung_hynix_full_thesis_smoke.json`도 같은 결론이다.

```text
verdict: PENDING_FULL_THESIS_REFRESH
score_allowed_before_execution: false
hardcoded_query_count: 0

required symbols:
  005930
  000660

per symbol:
  full_thesis_claim_ids: []
  full_thesis_score_contribution_ids: []
  full_thesis_stagecourt_trace_ids: []
  blocking_reason: full_thesis_source_tasks_planned_but_not_executed
```

필수 C06/HBM primitive도 아직 실행 claim으로 닫히지 않았다.

```text
named_customer_or_customer_quality
qualification_status
capacity_allocation_or_pre_sold
hbm_shipment_or_revenue_mix
cash_or_revision_conversion
repeat_evidence_family
source_quorum
```

따라서 현재 삼성전자/하이닉스에 대해 허용되는 표현은:

```text
daily event-board partial status: Stage1 / 4.0
full thesis: not run
HBM/C06 operating score: not available
```

## Brain/Web/LLM 상태

최신 canonical run은 Brain/Web disabled다.

`brain_web_readiness_gate_audit.json`:

```text
verdict: NOT_REQUESTED
brain_web_mode: disabled
brain_web_evidence_pass_allowed: false

llm_planner_call_count: 0
llm_real_provider_success_count: 0
llm_claim_extractor_attempt_count: 0
web_search_task_count: 0
web_fetched_document_count: 0
source_task_execution_count: 0
web_or_llm_accepted_claim_count: 0
brain_score_contribution_count: 0
brain_stage_trace_count: 0
brain_promoted_stage_row_count: 0
```

쉬운 예:

```text
NOT_REQUESTED
= "안 돌렸고, 안 돌렸다고 기록했다."

NOT_REQUESTED
!= "돌렸고 통과했다."
```

즉 현재 pass의 의미는 `거짓 완료 방지`다.
`Brain/Web evidence pass`가 아니다.

## Goal completion 상태

`goal_completion_audit.json`:

```text
goal_completion_ready: false
blockers:
  - brain_web_evidence_pass_false
  - full_thesis_smoke_pending

known_bad_regression_status: PASS
self_repair_status: RUN_COMPLETE
self_repair_completion_eligible: true
test_result_evidence_verdict: MACHINE_READABLE_TEST_ARTIFACT_PASS
```

해석:

```text
막아야 할 가짜 완료/가짜 점수 문제 일부는 막았다.
하지만 운영 목표 완료는 아니다.
```

## 이번에 실제로 닫은 코드 경로

이번 패치로 닫은 경로:

```text
TEXT_SPAN EvidenceDocument
-> contract-blind extractor run
-> RawAssertion
-> target/temporal adjudication
-> PrimitiveMapping
-> derive_score_eligibility
-> accepted/rejected claim
-> claim_extractor_runs.jsonl export
```

핵심 파일:

```text
src/e2r/research_brain/v4_evidence_extraction_bridge.py
src/e2r/census/census_runner_v4.py
src/e2r/production/claim_extraction/contract_blind_extractor.py
src/e2r/production/claim_extraction/primitive_mapper.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
tests/test_census_v4_brain_bundle_export.py
tests/test_census_v4_brain_web_readiness_gate.py
```

추가로 닫은 provider 선택 경로:

```text
ProductionShadowV4Config.claim_extractor_provider = auto

auto 선택:
  live_full_bounded + planner_provider not in {none, fake}
    -> CodexCLIExtractorProvider

  frozen/test/replay/disabled 성격
    -> RuleFallbackExtractorProvider
```

핵심 파일:

```text
src/e2r/research_brain/v4_schemas.py
src/e2r/research_brain/v4_production_orchestrator.py
src/e2r/cli/run_research_brain_v4_production_shadow.py
src/e2r/census/census_runner_v4.py
src/e2r/cli/run_e2r_census_v4_until_pass.py
tests/test_research_brain_v4_operational_modes.py
```

쉬운 예:

```text
실제 live/full-bounded web 문서:
  Codex LLM extractor가 원문 claim을 작성해야 한다.

냉동 replay/test fixture:
  외부 provider를 부르면 테스트가 흔들리므로 rule fallback으로 남긴다.
```

중요한 방어:

```text
extractor는 score/stage/primitive_gap/green gate를 보지 않는다.
LLM이 current_score_eligible을 직접 쓰지 않는다.
anchor validation은 코드가 한다.
eligibility는 deterministic guard가 파생한다.
provider error는 NO_EVIDENCE_FOUND가 아니라 PROVIDER_FAILED로 남긴다.
rule_fallback extractor는 Brain/Web 운영 pass로 인정하지 않는다.
```

쉬운 예:

```text
웹 문서:
  "삼성전자는 HBM 고객 배정과 qualification 진행 상황을 설명했다."

이전:
  원문은 왔지만 structured row가 없으면 mention-only로 끝났다.

패치 후:
  TEXT_SPAN이면 extractor가 raw assertion을 만들 수 있다.
  다만 rule fallback이면 운영 pass가 아니라 diagnostic이다.
```

검증 테스트:

```text
tests.test_research_brain_v4_evidence_extraction_from_real_document
tests.test_census_v4_brain_bundle_export
tests.test_census_v4_brain_web_readiness_gate
tests.test_cutover_contract_blind_extraction

Ran 28 tests
OK
```

전체 테스트:

```text
Ran 4959 tests
OK
```

## 아직 잘못되면 안 되는 지점

다음은 현재도 절대 완료라고 말하면 안 된다.

```text
1. Brain/Web evidence pass
2. live LLM extractor production success
3. web/news full-source accepted claim canonical reflection
4. Samsung/Hynix HBM/C06 full thesis score
5. Stage3-Green/Yellow/Red operating decision
6. 4B/4C lifecycle transition operating decision
7. all-archetype source-backed replay parity
8. meaningful operational stage pass
```

이걸 말하면 다시 같은 문제가 난다.

예:

```text
나쁜 보고:
  "삼성전자 Stage1 4점입니다."

좋은 보고:
  "삼성전자 event-board partial score는 4.0이고,
   full thesis score는 null이며,
   HBM/C06 operating Stage는 아직 not run입니다."
```

## 다음 패치 방향

### P0. Real LLM extractor provider 연결

목표:

```text
Brain/Web enabled run에서 실제 provider_mode=llm extractor run을 만든다.
prompt_hash, response_hash, model, raw_assertion_ids를 leaf로 남긴다.
```

현재 상태:

```text
provider selection 배관은 패치됨.
실제 canonical enabled run은 아직 아님.
```

pass 조건:

```text
claim_extractor_runs.jsonl 존재
provider_mode=llm row 존재
forbidden_context_seen=[]
provider_error 없음 또는 provider failure가 pending으로 기록됨
```

주의:

```text
rule_fallback 성공을 LLM 성공으로 세면 실패다.
```

### P1. Brain/Web strict promotion 연결

목표:

```text
accepted Brain/Web claim
-> score contribution
-> StageCourt trace
-> brain_to_claim_trace
-> promoted census_stage_status row
```

pass 조건:

```text
같은 claim_id가 모든 leaf에서 이어진다.
snapshot://, fake provider, snippet-only, source_proxy_only는 운영 pass로 못 쓴다.
```

### P2. Samsung/Hynix full thesis smoke 실행

목표:

```text
daily event score와 HBM/C06 full thesis score를 완전히 분리한 채
005930, 000660 full thesis SourceTask를 실제 executed/pending truth state로 만든다.
```

pass 조건:

```text
각 symbol마다:
  full_thesis_claim_ids 또는 material pending reason 존재
  full_thesis_score_contribution_ids 또는 score_status=PENDING_MATERIAL_GAP
  full_thesis_stagecourt_trace_ids 또는 explicit provider/source blocker
```

주의:

```text
low score 확정 금지.
증거가 없거나 provider가 실패하면 낮은 점수가 아니라 pending이다.
```

### P3. 전 아키타입 source-backed replay parity

목표:

```text
C01~C36 Evidence Contract가 모두 schema validation을 통과하고,
source-backed replay fixture 또는 explicit unsupported/source-gap 상태를 가진다.
```

pass 조건:

```text
source_proxy_only 연구 row가 production score로 들어가지 않는다.
미래 결과 label이 extraction prompt에 들어가지 않는다.
all-archetype replay가 claim-backed contribution으로 닫힌다.
```

### P4. canonical output 재생성

목표:

```text
anti_fake pass가 아니라 meaningful/brain_web/full_thesis target gate를 순서대로 닫는다.
```

pass 조건:

```text
target_gate=anti_fake: 이미 가능
target_gate=brain_web: 아직 불가
target_gate=full_thesis: 아직 불가
target_gate=meaningful: 아직 불가
```

## 다음 리뷰어 공격 질문

다음 에이전트는 아래 질문으로 깨면 된다.

```text
1. Stage label을 full thesis Stage로 읽을 수 있는 row가 하나라도 있는가?
2. operator_stage_use가 NOT_FULL_THESIS_STAGE인데 운영 Stage 문구를 출력하는가?
3. 005930/000660의 4.0이 HBM/C06 full thesis 점수로 출력되는가?
4. Brain/Web disabled인데 Brain/Web pass라고 주장하는가?
5. provider_mode=rule_fallback extractor run을 LLM success로 세는가?
6. accepted claim count만 보고 source/document/anchor/score/stage trace 연결 없이 pass하는가?
7. source_task_executions count만 있고 fetched document가 없는데 pass하는가?
8. source_proxy_only 또는 snapshot://이 production score contribution으로 들어가는가?
9. provider failure나 material source gap을 낮은 점수/Red로 확정하는가?
10. old risk 또는 wrong-subject claim이 current hard break로 들어가는가?
11. current_score_eligible을 LLM 출력 그대로 믿는가?
12. score/stage/green gate context가 extractor prompt에 들어가는가?
13. 4942 tests 같은 구 기록이 최신 기준처럼 남아 있는가?
14. test artifact와 docs/operational test evidence count가 서로 다른가?
15. target_gate=anti_fake exit 0을 goal completion으로 해석하는가?
```

## 최종 판단

현재 시스템은 이전보다 나아졌다.

이유:

```text
Stage/score overclaim을 막는 라벨과 audit가 생겼다.
CensusAssessmentEvent와 CandidateEvent가 분리됐다.
claim 없는 점수, wrong-subject risk, old-risk reuse, source_proxy score를 막는 테스트가 있다.
TEXT_SPAN 원문을 claim extraction path로 넘기는 배관이 생겼다.
live_full_bounded 운영형 실행에서 Codex LLM extractor provider를 선택하는 배관이 생겼다.
최신 로컬 전체 테스트도 4959개 OK로 다시 확인했다.
단 output에 남은 `test_result_artifact_after_claim_provider_patch.json`는 이전 canonical artifact라 4954개 OK로 남아 있다.
```

하지만 운영 완성은 아니다.

남은 핵심:

```text
실제 LLM provider가 원문을 읽고,
accepted claim을 만들고,
그 claim이 score contribution과 StageCourt로 이어지고,
그 Stage가 representative row로 승격되는 실제 Brain/Web run이 아직 canonical output에 없다.
```

따라서 다음 작업의 목표는 새 점수 튜닝이 아니다.

```text
목표:
  실제 source -> LLM claim -> deterministic eligibility -> score contribution -> StageCourt -> promoted row
  이 한 줄을 live/bounded/official-first 조건에서 닫는 것.
```

이 줄이 닫히기 전까지는 `ANTI_FAKE_FULL_UNIVERSE_STATUS_PASS`만 말할 수 있고,
`MEANINGFUL_OPERATIONAL_STAGE_PASS`는 말하면 안 된다.

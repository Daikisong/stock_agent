# Census v4 Rejected Mapping Feedback Retry Patch - 2026-07-01

이 문서는 P1 패치 결과를 다음 에이전트가 바로 검증할 수 있게 남긴 기록이다.

기준 실행:

```text
/tmp/census_v4_enabled_provider_probe_after_rejected_feedback_patch_v2
```

후속 업데이트:

```text
P2 planner contract primitive filter 패치 후 최신 실행은
/tmp/census_v4_enabled_provider_probe_after_planner_primitive_filter 이다.

최신 수치와 P2 결과는 아래 문서를 우선한다.
docs/0701/census_v4_0701_planner_contract_primitive_filter_cross_validation_2026-07-01.md
```

## 결론

P1은 의도대로 작동했다.

```text
이전:
  문서 fetch와 LLM extraction 후 mapping rejected가 생김
  -> planner에게 rejected 이유가 돌아가지 않음
  -> 그대로 NOT_READY

패치 후:
  mapping rejected가 생김
  -> rejected claim feedback 8개씩 planner에게 전달
  -> feedback_retry planner run 2개 생성
  -> follow-up source task 4개 실행
  -> web/search/fetch/extraction row 증가
  -> 그래도 accepted claim은 0개
  -> Stage 승격 없이 NOT_READY 유지
```

쉬운 예:

```text
오답 노트를 만든 뒤 선생님에게 다시 문제를 내달라고 요청하는 루프가 생겼다.
하지만 다시 푼 답도 채점 기준을 통과하지 못했으므로 성적표에는 아직 반영하지 않았다.
```

이게 맞는 방향이다. accepted를 억지로 늘린 것이 아니라, rejected 사유를 조사 계획으로 되돌렸고, 통과 못 한 결과는 계속 점수에서 차단했다.

## 코드 변경 요약

변경 파일:

```text
src/e2r/research_brain/v4_schemas.py
src/e2r/research_brain/v4_planner_runtime.py
src/e2r/research_brain/v4_production_orchestrator.py
tests/test_research_brain_v4_operational_modes.py
```

핵심 변경:

```text
1. PlannerRunV4에 planner_run_role, planner_feedback, rejected_claim_feedback_count 추가
2. planner prompt에 rejected_claim_feedback 규칙 추가
3. Evidence bundle에서 rejected claim feedback row 생성
4. source acquisition 후 feedback_retry planner run 1회 실행
5. retry source task id를 deterministic하게 재작성해 기존 task와 충돌 방지
6. follow-up EvidenceOSExecutionBundle을 append-only merge
7. planner report에서 initial run과 feedback retry run을 분리 집계
8. duplicate candidate audit는 initial planner 중복만 critical로 본다
```

금지 원칙 유지:

```text
accepted 판정 기준 완화 없음
mapping guard 완화 없음
종목명 예외 없음
deterministic query template 추가 없음
score/stage/eligibility를 LLM에게 맡기지 않음
event-board Stage를 full thesis Stage로 승격하지 않음
```

## 산출물 비교

이전 기준:

```text
/tmp/census_v4_enabled_provider_probe_after_mapping_trace_patch

planner_runs.jsonl:              22
source_task_executions.jsonl:    106
web_search_tasks.jsonl:            4
web_search_results.jsonl:         40
web_fetched_documents.jsonl:       8
claim_extractor_runs.jsonl:        8
raw_assertions.jsonl:            146
adjudicated_claims.jsonl:        146
brain_claim_mapping_trace.jsonl:  54
accepted_claims.jsonl:            92
brain_to_claim_trace.jsonl:        0
```

패치 후 기준:

```text
/tmp/census_v4_enabled_provider_probe_after_rejected_feedback_patch_v2

planner_runs.jsonl:              24
source_task_executions.jsonl:    110
web_search_tasks.jsonl:            9
web_search_results.jsonl:         50
web_fetched_documents.jsonl:      16
web_rejected_documents.jsonl:      3
claim_extractor_runs.jsonl:       16
raw_assertions.jsonl:            222
adjudicated_claims.jsonl:        237
brain_claim_mapping_trace.jsonl: 160
accepted_claims.jsonl:            92
score_contributions.jsonl:        92
stagecourt_traces.jsonl:          92
brain_to_claim_trace.jsonl:        0
census_stage_status.jsonl:      3391
```

해석:

```text
planner/source/web/LLM extraction은 실제로 늘었다.
accepted_claims 92개는 여전히 기존 OpenDART event-board 경로다.
Brain/Web accepted claim은 여전히 0개다.
```

## Planner Retry 증거

`planner_runs.jsonl`:

```text
planner_run_role:
  initial:        22
  feedback_retry: 2

provider_mode:
  none: 20
  real:  4

real_provider_success:
  true:  4
  false: 20

rejected_claim_feedback_count:
  0: 22
  8:  2
```

두 feedback retry 대상:

```text
CE-LIVE-DART-003090-20260630801612 / 대웅
CE-LIVE-DART-069620-20260630801610 / 대웅제약
```

retry planner output은 실제로 이전 rejection을 반영했다.

예:

```text
정정사항이 종료일 연장뿐이라면 volume_growth_visible 증거가 아니다.
이전 DART/KIND 패턴처럼 공시 뷰어 문구만 반복되면 다시 반려될 수 있다.
```

이건 좋은 신호다. LLM planner가 점수를 만들지 않고, rejected source pattern을 보고 다른 source/task를 계획했다.

## Follow-up SourceTask 증거

`source_task_executions.jsonl`:

```text
feedback_retry:rejected_claim_mapping 포함 execution: 4
```

retry task 예:

```text
primitive_gap: volume_growth_visible
preferred_source_classes: DART, KIND
fallback_source_classes: IssuerOfficial, IR
query_intents:
  "대웅" "003090" "신규시설투자" "자회사" "생산능력" "공장"
  "대웅" "003090" "2023.05.02" "신규시설투자" "투자목적" "생산"
  "대웅" "003090" "2026.06.30" "종료일 연장" "시설투자" "사용승인"
reason:
  이전에는 종료일 연장 문구가 volume_growth_visible로 매핑되어 반려됐다.
  이번에는 투자목적, 설비명, 제품, 생산능력 수치처럼 물량 증가를 직접 말하는 항목만 찾는다.
```

이 retry task는 deterministic template이 아니다. LLM이 rejected feedback을 보고 만든 query intent다.

## 왜 아직 NOT_READY인가

`brain_claim_mapping_trace.jsonl`:

```text
trace_status:
  REJECTED_BEFORE_SCORE: 160

accepted:
  False: 160

score_eligible:
  False: 160

mapping_status:
  REJECTED: 160

target_scope_status:
  UNRELATED: 100
  DIRECT:     60

rejection_reason:
  target_scope_not_direct:UNRELATED;mapping_not_accepted:REJECTED: 100
  mapping_not_accepted:REJECTED:                                   60
```

해석:

```text
retry 후에도 100개는 대상 회사 직접 claim이 아니었다.
60개는 직접 claim이지만 해당 primitive 점수 칸에 넣을 수 없었다.
따라서 accepted claim 0개가 맞고, Stage 승격 0개가 맞다.
```

쉬운 예:

```text
"시설투자 종료일 연장"은 일정 정보일 수는 있지만,
"생산량이 늘었다" 또는 "영업레버리지가 생겼다"는 증거는 아니다.
그래서 volume_growth_visible 점수로 넣으면 안 된다.
```

## Readiness 결과

핵심 감사:

```text
brain_web_attempt_audit.json:
  verdict: ATTEMPTED_NOT_CUTOVER_READY
  planner_run_count: 24
  real_provider_success_count: 4
  source_task_execution_count: 18
  real_document_fetched_count: 29
  brain_raw_assertion_exported_count: 142
  accepted_claim_count: 0
  brain_score_contribution_exported_count: 0
  brain_stagecourt_trace_exported_count: 0

brain_web_readiness_gate_audit.json:
  brain_web_evidence_pass_allowed: false
  blockers:
    - web/LLM accepted claim count is zero
    - Brain/Web StageCourt traces are not promoted into census_stage_status
    - brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED

brain_stage_promotion_audit.json:
  verdict: BLOCKED
  blockers:
    - accepted brain claim count is zero
    - brain score contribution count is zero
    - brain StageCourt trace count is zero

leaf_artifact_audit.json:
  critical_count: 0

readiness_verdict.json:
  verdict: NOT_READY
```

즉 P1은 "retry가 생겼다"는 의미에서는 성공이고, "운영 Brain/Web Stage가 생겼다"는 의미에서는 아직 실패다.

## Stage 상태

패치 후에도 stage 의미는 변하지 않았다.

```text
census_stage_status.jsonl: 3391
stage_scope: CENSUS_EVENT_BOARD 3391
full_thesis_stage: FULL_THESIS_NOT_RUN 3391
Brain/Web promoted row: 0
```

삼성전자/하이닉스도 아직 HBM/C06 full thesis Stage가 아니다.

## 검증

Targeted:

```text
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_operational_modes \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_daily_watchlist \
  tests.test_research_brain_v4_static_logic_audit \
  tests.test_research_brain_v4_provider_failure_pending \
  tests.test_census_v4_run_mode_honesty \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_brain_stage_promotion_gate \
  tests.test_census_v4_goal_required_audits \
  tests.test_census_v4_brain_bundle_export \
  tests.test_cutover_contract_blind_extraction \
  tests.test_cutover_v2_quote_anchor_validation \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_census_v4_artifact_manifest \
  -v

Ran 83 tests in 32.275s
OK
```

Full:

```text
PYTHONPATH=src python -m unittest discover -s tests -v
Ran 4963 tests in 161.557s
OK

log:
/tmp/stock_agent_full_tests_after_rejected_feedback_patch.log
```

Enabled smoke:

```text
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root /tmp/census_v4_enabled_provider_probe_after_rejected_feedback_patch_v2 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 8 \
  --brain-planner-success-limit 2 \
  --brain-planner-batch-size 2 \
  --brain-max-fetches-per-task 2 \
  --brain-claim-extractor-provider auto \
  --brain-stage-promotion-mode strict \
  --target-gate brain_web \
  --fail-on-critical-audit true \
  --write-operational-docs false

Result:
NOT_READY
```

이 `NOT_READY`는 정상이다. retry까지 했지만 accepted claim이 없기 때문이다.

## 다음 패치 P2

P1 후 남은 병목은 더 선명해졌다.

```text
LLM planner는 rejected feedback을 보고 더 구체적인 source task를 만들 수 있다.
Source runner도 실제 문서를 더 가져온다.
LLM extractor도 더 많이 돈다.
하지만 primitive mapper가 C06/CAPEX/시설투자 계열의 직접 positive bridge를 아직 충분히 만들지 못한다.
```

후속 상태:

```text
아래 P2 후보 중 "contract에 없는 implementation_timeline primitive가 planner/source task로 실행되는 문제"는
census_v4_0701_planner_contract_primitive_filter_cross_validation_2026-07-01.md에서 닫았다.

다만 Brain/Web accepted claim은 여전히 0개라 source relevance와 direct-but-no-bridge rejection taxonomy는 아직 남아 있다.
```

P2 후보로 적었던 항목:

```text
1. Direct current claim인데 mapping rejected 된 60개를 샘플링해 primitive mapper가 과차단인지 정상 차단인지 분류한다.
2. volume_growth_visible / implementation_timeline / operating_leverage_visible에 대해 Evidence Contract v2 rubric과 mapper allowed primitive를 점검한다.
3. 시설투자 정정 공시에서는 "종료일 연장"과 "생산능력/품목/CAPA/상업생산 개시"를 분리한다.
4. accepted를 늘리기 전에 positive bridge fixture를 만들고, wrong-subject/정정공시 guard fixture와 같이 테스트한다.
5. 그래도 accepted가 없으면 SourceTask가 어떤 official source를 더 찾아야 하는지 planner feedback에 material gap/exhaustion summary를 추가한다.
```

P2에서 하면 안 되는 것:

```text
"정정공시"를 무조건 implementation_timeline accepted로 넣기
"시설투자"를 무조건 capacity_expansion/volume_growth로 넣기
"대웅/대웅제약" 종목 예외 추가
mapping_not_accepted를 무시하고 score로 통과시키기
```

쉬운 예:

```text
공장 준공 지연 공시는 "일정 정보"일 수 있다.
하지만 "생산량 증가"나 "영업이익 개선" 점수는 품목, CAPA, 가동, 매출 연결 문장이 따로 있어야 한다.
```

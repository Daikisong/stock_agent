# Census v4 0701 v59 Real Planner Source Order Patch And Full Thesis Blocker Audit

작성일: 2026-07-03 KST

## 결론

이번 확인의 결론은 두 줄이다.

```text
1. 0701 산출물에 Stage 상태판은 있다.
2. 하지만 운영용 FULL_THESIS Stage와 FULL_E2R_100 verified score는 아직 0개다.
```

따라서 "Stage가 있는 애들이 있긴 해?"에 대한 정확한 답은 다음과 같다.

```text
있다:
  CENSUS_EVENT_BOARD base/canonical 상태판

없다:
  실제 운영 Full Thesis score/stage
```

쉬운 예:

```text
출석부에는 85명이 "검토 필요"로 표시돼 있다.
하지만 채점 가능한 답안지, 즉 source-backed Full Thesis 점수표는 아직 0장이다.
```

이 차이를 섞어 말하면 다시 같은 오류가 난다.

## Canonical 0701 Stage Truth

대상 산출물:

```text
output/census_v4/2026-07-01
```

직접 집계:

```text
census_stage_map.jsonl rows = 3391
census_stage_status.jsonl rows = 3391

stage field:
  None = 3391

base_stage:
  Stage0       = 3306
  Stage1       = 54
  Stage2-Watch = 30
  Red          = 1

canonical_stage:
  0     = 3306
  1     = 54
  2     = 30
  3-Red = 1

stage_scope:
  CENSUS_EVENT_BOARD = 3391

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

score_scale:
  NO_SCORE               = 3324
  EVENT_WEIGHTED_PARTIAL = 67

verified_score:
  None = 3391

FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
```

해석:

```text
base_stage/canonical_stage는 Census 상태판이다.
operator가 투자 논리 Stage로 써도 되는 FULL_THESIS가 아니다.
```

쉬운 예:

```text
Stage2-Watch 30개는 "이 종목은 더 확인할 만하다"에 가깝다.
"Full Thesis로 2단계 확정"이 아니다.
```

## Why v59 Was Needed

v56까지의 핵심 성과:

```text
Full Thesis refresh queue seed가 Research Brain planner 입력으로 들어감.
source_primary_archetype, source_missing_primitives, source_material_gap_ids 같은
non-binding source context가 planner prompt까지 보임.
```

v57 real planner smoke에서 확인한 문제:

```text
Codex planner는 실제로 C06 HBM 가설을 냈다.
하지만 source acquisition은 유상증자 DART 공시를 가져왔고,
그 claim은 HBM qualification/capacity/revenue primitive에 rejected됐다.
```

v58 패치에서 해결한 것:

```text
live_official_first에서도 rejected mapping feedback retry가 돌도록 수정.
```

v58 이후 남은 문제:

```text
feedback retry는 열렸지만 retry도 같은 DART 유상증자 문서로 다시 빨려 들어갔다.
```

이건 LLM 문제가 아니라 source runner의 실행 순서 문제였다.

## Root Cause

기존 `SourceAcquisitionRunnerV4._acquire_live_official_sources()` 흐름은 다음에 가까웠다.

```text
1. SourceTask preferred/fallback source class를 모음
2. registry.connectors 순서대로 필터링
3. 먼저 FETCHED 되는 공식 문서가 있으면 max_fetches까지 채움
```

문제는 registry 기본 순서가 다음이었다.

```text
OpenDART
KIND
KRX
CompanyGuide
IssuerIR
TrustedNews
```

따라서 SourceTask가 이렇게 말해도:

```text
preferred_source_classes = ["IssuerIR", "CompanyGuide", "DART"]
```

실제 connector 실행은 DART가 앞설 수 있었다.

쉬운 예:

```text
의사가 "IR 먼저 보고, 없으면 CompanyGuide, 그래도 없으면 DART"라고 했는데
접수대가 병원 내부 등록 순서 때문에 DART부터 꺼내 온 것이다.
```

이러면 이전 DART 문서가 rejected됐는데도 다음 retry에서 다시 DART 문서가 들어와
Full Thesis materialization이 닫히지 않는다.

## v59 Patch

패치 범위:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
tests/test_research_brain_v4_real_source_acquisition.py
```

수정한 것:

```text
1. live official connector 실행 순서를 registry 순서가 아니라 SourceTask requested order로 변경
2. LLM이 쓰는 "IssuerIR" source class를 실제 IR connector와 매칭
3. 이 동작을 단위테스트로 고정
```

코드 위치:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py
  _acquire_live_official_sources()
  _ordered_live_official_connectors()
  _connector_match_source_class()
  _normalize_source_class()

tests/test_research_brain_v4_real_source_acquisition.py
  test_live_official_respects_task_source_order_before_registry_order()
```

패치 후 핵심 규칙:

```text
SourceTask:
  IssuerIR -> CompanyGuide -> DART

Registry:
  DART -> CompanyGuide -> IR

실행:
  IssuerIR -> CompanyGuide
  DART는 CompanyGuide가 max_fetches를 채우면 실행하지 않음
```

이건 종목명 예외가 아니다.

```text
나쁜 하드코딩:
  if symbol == "000660": DART를 늦춘다

이번 패치:
  모든 종목에서 SourceTask의 source class 순서를 지킨다
```

## Unit Verification

명령:

```bash
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_real_source_acquisition -v
PYTHONPATH=src python -m unittest tests.test_research_brain_v4_operational_modes -v
git diff --check
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
tests.test_research_brain_v4_real_source_acquisition:
  Ran 29 tests
  OK

tests.test_research_brain_v4_operational_modes:
  Ran 51 tests
  OK

git diff --check:
  OK

full suite:
  Ran 5081 tests in 207.192s
  OK
```

새 테스트가 검증하는 상황:

```text
task preferred:
  IssuerIR, CompanyGuide

task fallback:
  DART

registry physical order:
  DART, CompanyGuide, IssuerIR

expected calls:
  IssuerIR, CompanyGuide

not expected:
  OpenDART call
```

이 테스트가 없으면 다음 리팩터에서 registry 순서가 다시 source task 의도를 덮을 수 있다.

## Real Planner Smoke v59

명령:

```bash
rm -rf output/census_v4/2026-07-01-real-planner-source-order-v59
E2R_CODEX_PLANNER_TIMEOUT_SECONDS=120 PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-real-planner-source-order-v59 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_TRIAGE_ENABLED \
  --brain-web-mode enabled \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_official_first \
  --brain-universe-limit 1 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-source-tasks-per-plan 3 \
  --brain-max-fetches-per-task 1 \
  --brain-stage-promotion-mode strict \
  --target-gate anti_fake \
  --write-operational-docs false \
  --fail-on-critical-audit false \
  --test-result-artifact output/census_v4/2026-07-01/full_unittest_result_artifact.json
```

종료:

```text
exit code = 1
stdout = NOT_READY
```

이 `NOT_READY`는 정상적인 실패다.

```text
이번 smoke의 목적은 readiness pass가 아니라
source order patch가 실제 leaf artifact에 반영되는지 확인하는 것이었다.
```

## v59 Artifact Hashes

```text
brain_web_attempt_audit.json
  b9af55a9da4e46cdfb89845c8ba106a03c9bac002c990415ed3f6c31ff77ca08

brain_web_readiness_gate_audit.json
  cf98eba121eb23da47c6e6f3891e5dbad151073ce1dec84b817edbeaa3ef3807

planner_runs.jsonl
  64c5dfc32367fd0b6f5c2ac7e1c051a95d7863e330cb656a206d6b6436fe8040

source_task_executions.jsonl
  b71da568d8964f588fb3caf4f9c8f4172c6e8886eff3934132de31d5b642c003

source_tasks.jsonl
  4fae62022de4a3599bc22ddc595a62c63a6a95bdf57a15d894694ff92ef203b0

full_thesis_seed_materialization_trace.jsonl
  9e62b64477ad4eb4cababdaa5c0bdc89eab15db4c388842c54b58a86cb06d7bc
```

## v59 Planner And Source Counts

전체 artifact 기준:

```text
planner_runs rows = 22
planner roles:
  initial        = 21
  feedback_retry = 1

real_provider_success_count = 2

source_tasks rows = 101
source_task_executions rows = 101
```

전체 source execution 분포:

```text
source_class:
  DART         = 93
  KRX          = 4
  CompanyGuide = 2
  KIND         = 1
  IR           = 1

status:
  EVIDENCE_OS_ACCEPTED  = 60
  EVIDENCE_OS_BASELINE_ONLY = 32
  NO_EVIDENCE_FOUND     = 8
  PROVIDER_FAILED       = 1
```

주의:

```text
위 accepted 60개는 전체 leaf artifact의 기존 official/event path까지 포함한다.
Full Thesis seed accepted claim과 섞어 말하면 안 된다.
```

Full Thesis seed `000660 / SK하이닉스` 기준:

```text
candidate_event_id = CEV4-FTQUEUE-000660-9563b2a7a852fc0c

source_task_execution_count = 9
accepted_claim_count = 0
materialization_status = ACCEPTED_CLAIM_NOT_CREATED
materialization_blockers:
  full_thesis_seed_source_tasks_have_no_accepted_claim

planner_run_count = 2
planner_real_provider_success_count = 2
target_archetype_status = BRAIN_HYPOTHESIS_REQUIRED
target_archetype = None
source_primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
source_large_sector_id = 메모리/HBM
source_missing_primitives:
  repeat_evidence_family
  cash_or_revision_conversion
source_material_gap_ids:
  repeat_evidence_family
  cash_or_revision_conversion
  multi_source_confirmation
```

Full Thesis seed source class 분포:

```text
DART         = 4
CompanyGuide = 2
KIND         = 1
KRX          = 1
IR           = 1

statuses:
  NO_EVIDENCE_FOUND = 8
  PROVIDER_FAILED   = 1

accepted_claim_count = 0
```

## v58 vs v59 Change

v58 seed:

```text
source_task_execution_count = 11
feedback_retry = 1
accepted_claim_count = 0
retry도 같은 DART 유상증자 공시를 다시 가져오는 문제가 관측됨
```

v59 seed:

```text
source_task_execution_count = 9
feedback_retry = 1
accepted_claim_count = 0
retry task가 CompanyGuide로 이동한 row가 관측됨
```

중요한 변화:

```text
RSTASKV4RETRY-149ea0b37046185788fe35d0
primitive_gap = cash_or_revision_conversion
preferred_source_classes = ["IssuerIR", "CompanyGuide", "DART"]
fallback_source_classes = ["KIND"]
source_class = CompanyGuide
document_urls = ["https://wcomp.fnguide.com"]
provider_errors = ["issuer_ir_discovery_not_configured; do not treat missing IR as no evidence"]
budget_used = {"queries": 2, "candidates": 2, "fetches": 1}
status = NO_EVIDENCE_FOUND
accepted_claim_ids = []
```

해석:

```text
v59 패치로 "IssuerIR 실패 -> CompanyGuide 시도"까지는 실제로 일어났다.
하지만 CompanyGuide 문서에서 cash/revision primitive claim을 만들지 못했다.
```

쉬운 예:

```text
전에는 접수대가 계속 DART 서류만 내줬다.
이제는 CompanyGuide 서류까지는 가져왔다.
하지만 그 서류의 EPS/리비전 숫자를 점수 칸에 옮겨 쓰는 사람이 아직 없다.
```

## Seed Row Detail

Full Thesis seed 000660 execution row 요약:

| task | primitive_gap | source_class | status | fetched | accepted | 핵심 해석 |
|---|---|---:|---:|---:|---:|---|
| ST-000660-C06-IR-HBM-VISIBILITY | qualification_status | DART | NO_EVIDENCE_FOUND | DART 유상증자 | 0 | 유상증자 시설자금 claim이 qualification primitive에 rejected |
| ST-000660-C06-CAPA-PRESOLD | hbm_capacity_pre_sold | DART | NO_EVIDENCE_FOUND | DART 유상증자 | 0 | capacity pre-sold가 아니라 financing/facility claim |
| ST-000660-C06-REVENUE-CONTRACT | revenue_visibility_contract | DART | NO_EVIDENCE_FOUND | DART 유상증자 | 0 | revenue contract primitive에 rejected |
| RSTASKV4CGSTATUS-* | official_report_snapshot_current | CompanyGuide | NO_EVIDENCE_FOUND | CompanyGuide portal | 0 | provider coverage only |
| RSTASKV4DARTSTATUS-* | official_disclosure_status_current | DART | NO_EVIDENCE_FOUND | DART 유상증자 | 0 | status check는 accepted primitive 아님 |
| RSTASKV4KIND-* | exchange_risk_status_current | KIND | NO_EVIDENCE_FOUND | KIND portal | 0 | provider portal coverage only |
| RSTASKV4KRX-* | listing_trading_status_current | KRX | NO_EVIDENCE_FOUND | KRX portal | 0 | provider portal coverage only |
| RSTASKV4IRSTATUS-* | issuer_official_update_current | IR | PROVIDER_FAILED | none | 0 | Issuer IR discovery not configured |
| RSTASKV4RETRY-* | cash_or_revision_conversion | CompanyGuide | NO_EVIDENCE_FOUND | CompanyGuide portal | 0 | v59 patch 효과는 있으나 numeric revision claim compiler 없음 |

## Critical Observation

`claim_extractor_runs.jsonl`:

```text
row count = 0
```

seed CompanyGuide document:

```text
canonical_url = https://wcomp.fnguide.com
source_name = CompanyGuide
source_type = API
score_block_reasons:
  provider_coverage_only_until_numeric_revision_parser_accepts_claims
```

해석:

```text
CompanyGuide는 live provider coverage 증거로 fetch된다.
하지만 EPS/revision/target price 같은 numeric fact를 raw assertion으로 컴파일하는 계층이 아직 없다.
따라서 cash_or_revision_conversion gap은 닫히지 않는다.
```

이것은 점수를 낮게 줘야 한다는 뜻이 아니다.

```text
정답:
  Full Thesis materialization pending / no accepted claim

오답:
  낮은 점수로 확정
```

쉬운 예:

```text
성적표 PDF를 받았지만 OCR/표 파서가 없어서 점수 칸을 못 읽었다.
학생이 0점이라는 뜻이 아니라, 채점 입력값을 아직 못 만든 것이다.
```

## What v59 Fixed

수정 완료:

```text
1. SourceTask order가 registry order에 덮이는 문제
2. IssuerIR source class가 IR connector에 매칭되지 않는 문제
3. official_first rejected mapping feedback retry가 실제 source class 순서에 영향을 주는지 단위테스트로 고정
```

해결된 오류:

```text
"LLM이 CompanyGuide/IR을 우선하라고 했는데 코드가 DART부터 가져오는 문제"
```

## What v59 Did Not Fix

아직 미해결:

```text
1. CompanyGuide HTML/API에서 EPS/revision/target price claim 생성
2. IssuerIR 실제 discovery/fetch connector
3. C06 HBM 고객 배정/qualification/capacity/revenue mix를 공식+bounded web으로 찾는 경로
4. 이전에 rejected된 동일 official_document_id를 같은 primitive retry에서 다시 쓰지 않는 document-level rejection memory
5. source_task max_fetches=1에서 provider coverage-only 문서가 fallback 기회를 소진하는 문제
6. FULL_THESIS seed accepted claim 생성
7. FULL_E2R_100 verified score 생성
```

## Next Patch Direction

### P0-1. CompanyGuide Numeric Revision Claim Compiler

해야 할 일:

```text
CompanyGuide provider가 단순 portal coverage만 반환하지 말고,
실제 추정치/리비전/목표가/컨센서스 변화를 구조화 claim으로 만들 수 있어야 한다.
```

단, 주의:

```text
HTML을 가져왔다는 이유만으로 score를 주면 안 된다.
숫자 또는 명시적 revision row가 anchor로 검증될 때만 raw assertion을 만든다.
```

예:

```text
좋은 claim:
  subject = SK하이닉스
  predicate = EPS estimate revised upward
  value = EPS_ACTION_TYP_NM=상향 또는 추정EPS 수치 변화
  source = CompanyGuide row/table anchor
  primitive = cash_or_revision_conversion 또는 medium_term_revision_visibility

나쁜 claim:
  CompanyGuide 페이지를 열었으니 revision visibility present
```

### P0-2. IssuerIR Discovery Connector

현재:

```text
IssuerIRLiveConnector = explicit provider failure
provider_error = issuer_ir_discovery_not_configured
```

필요:

```text
회사 IR/뉴스룸/실적발표/컨퍼런스콜/프레젠테이션을 bounded discovery로 찾고,
원문 URL/PDF/HTML anchor가 있을 때만 document를 만든다.
```

주의:

```text
issuer IR이 없으면 "증거 없음"이 아니라 Provider/Source Pending이다.
```

### P0-3. Rejected Document Memory

현재:

```text
DART 유상증자 문서가 hbm_capacity_pre_sold에 rejected돼도
다음 task 또는 retry에서 같은 document가 다시 들어올 수 있다.
```

필요:

```text
same symbol + same primitive_gap + same official_document_id/content_hash가 rejected되면
feedback retry에는 "이 문서는 이 primitive를 닫지 못했다"가 들어가야 한다.
```

단, 완전 차단하면 안 되는 경우:

```text
같은 문서라도 다른 primitive에는 유효할 수 있다.

예:
  유상증자 문서
    - hbm_capacity_pre_sold = rejected
    - capital_allocation_event = accepted 가능
```

따라서 key는 다음이어야 한다.

```text
symbol
primitive_gap
official_document_id 또는 content_hash
rejection_reason
```

### P0-4. Coverage-only Document Handling

현재:

```text
CompanyGuide/KIND/KRX portal coverage-only document가 max_fetches=1을 소비한다.
```

필요한 판단:

```text
score_block_reasons가 있는 coverage-only document를 fetched leaf로는 남기되,
stop-on-resolution에는 포함하지 않도록 할지 검토해야 한다.
```

쉬운 예:

```text
문 앞까지 갔다는 출입 기록은 남긴다.
하지만 실제 서류를 받은 것은 아니므로 "증거 확보"로 멈추면 안 된다.
```

주의:

```text
이 패치는 fetch budget 의미를 바꿀 수 있으므로
production daily budget test와 source_task_realness audit을 같이 바꿔야 한다.
```

### P0-5. C06 Live Full Bounded Route

C06 HBM 고객 배정/qualification/capacity/revenue mix는 DART만으로 안 닫히는 경우가 많다.

필요:

```text
official_first:
  DART/IR/CompanyGuide 먼저 확인

공식 소스로 gap 미해결:
  bounded web/report/issuer newsroom route를 LLM이 제안

코드:
  query를 만들지 않고 target/date/source quality만 검증
```

주의:

```text
다시 뉴스 1000개를 긁으면 안 된다.
SourceTask 단위 max_queries/max_candidates/max_fetches와 stop_condition이 있어야 한다.
```

## Reviewer Attack Checklist

다음 에이전트는 아래 질문으로 이 문서를 공격하면 된다.

```text
1. v59가 정말 registry order가 아니라 SourceTask order를 따르는가?
2. IssuerIR alias가 실제 IR connector와 매칭되는가?
3. v59 real smoke에서 retry task가 DART가 아니라 CompanyGuide로 이동했는가?
4. 그럼에도 accepted claim이 0인 이유가 문서에 정확히 설명됐는가?
5. CompanyGuide document가 provider coverage-only로 score_block된 근거가 있는가?
6. FULL_THESIS row가 0이라는 진실을 흐리지 않았는가?
7. 전체 artifact accepted claim 60개와 Full Thesis seed accepted claim 0개를 섞어 말하지 않았는가?
8. CENSUS_EVENT_BOARD Stage와 운영 Full Thesis Stage를 구분했는가?
9. 이번 패치가 종목명/아키타입명 하드코딩이 아닌 source class routing 규칙인가?
10. 다음 패치 방향이 deterministic query template 추가가 아니라 evidence compiler/source connector 보강인가?
```

## Acceptance Before Calling This Ready

아직 ready가 아니다.

최소 다음 조건이 필요하다.

```text
1. Full Thesis seed에서 accepted_claim_count > 0
2. accepted claim이 score_contribution으로 연결
3. score_scale = FULL_E2R_100 row 생성
4. operator_stage_use = FULL_THESIS row 생성
5. CompanyGuide/IR/Report/Web 중 적어도 하나가 source-backed primitive claim 생성
6. C06 HBM live smoke에서 유상증자 financing claim이 HBM customer/capacity/revenue primitive를 닫지 않음
7. 같은 rejected document가 같은 primitive retry에 반복 사용되면 audit에서 잡힘
8. frozen corpus 동일 실행 3회 score/stage 안정
```

## Final Verdict

```text
v59 verdict = NOT_READY
```

하지만 v59는 의미 있는 전진이다.

```text
고친 것:
  SourceTask가 요청한 official source order를 실제 connector 실행에 반영

드러난 다음 병목:
  CompanyGuide/IR 같은 실제 운영 source에서 primitive claim을 만드는 evidence compiler 부재

현재 운영 Stage:
  FULL_THESIS = 0
  FULL_E2R_100 = 0
```

이 문서를 다음 에이전트가 읽을 때 가장 조심해야 할 문장:

```text
Stage 상태판은 있다.
운영 Full Thesis Stage는 아직 없다.
```

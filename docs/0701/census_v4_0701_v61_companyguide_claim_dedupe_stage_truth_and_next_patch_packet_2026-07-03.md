# Census v4 0701 v61 CompanyGuide Claim Dedupe, Stage Truth, And Next Patch Packet

작성일: 2026-07-03 KST

## 결론

이번 확인의 결론은 명확하다.

```text
1. Stage처럼 보이는 상태값은 있다.
2. 하지만 운영자가 쓸 수 있는 FULL_THESIS Stage는 아직 0개다.
3. v61은 CompanyGuide 컨센서스 claim 증식 버그를 줄였지만, Full Thesis 운영 파이프라인은 아직 NOT_READY다.
```

쉬운 예:

```text
학교 출석부에 "검토 필요", "후속 확인 필요" 표시가 붙은 학생은 있다.
하지만 채점 완료된 시험지는 아직 없다.

CENSUS_EVENT_BOARD Stage = 출석부 상태표
FULL_THESIS Stage        = 채점 완료 답안지
```

따라서 사용자가 물은 "뭔가 잘못되고 있는 거 맞지? stage가 있는 애들이 있긴 해?"에 대한 정확한 답은 다음이다.

```text
상태판 Stage는 있다.
운영 Full Thesis Stage는 아직 없다.
현재 산출물을 "Stage2 종목 30개"처럼 운영 Stage로 읽으면 잘못이다.
```

## v61에서 실제로 고친 것

v60에서는 CompanyGuide 컨센서스 표 하나가 여러 SourceTask를 지나면서 서로 다른 claim으로 불어났다.

원인:

```text
EvidenceAnchor.normalized_value 안에 source_fetch_result 전체 dict가 들어갔다.
그 dict에는 task/request별로 달라지는 값이 포함된다.
같은 CompanyGuide 컨센서스 문서라도 anchor_id가 task마다 달라졌다.
claim_id도 anchor에 묶여 생성되므로 같은 숫자가 여러 claim으로 증식했다.
```

v61 패치:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py

normalized_value에서 volatile source_fetch_result 전체를 제거했다.
대신 안정적인 값만 남겼다.

남긴 값:
  symbol
  company_name
  provider
  source_class
  official_document_id
  provider_request_id
  row

제거한 값:
  source_fetch_result: result.to_dict()
```

핵심 코드 위치:

```text
src/e2r/research_brain/v4_source_acquisition_runner.py:231
```

추가 테스트:

```text
tests/test_research_brain_v4_evidence_extraction_from_real_document.py:203

test_repeated_companyguide_consensus_tasks_dedupe_to_one_claim
```

테스트 의미:

```text
같은 SK하이닉스 CompanyGuide 컨센서스 문서를
cash_or_revision_conversion task와 hbm_capacity_pre_sold task에 같이 넣는다.

기대 결과:
  accepted ref는 task 2개라서 2개
  unique claim은 1개
  accepted primitive는 medium_term_revision_visibility 하나뿐

즉 CompanyGuide EPS/목표가 컨센서스가
cash/FCF 또는 HBM capacity sold-out 증거로 둔갑하면 안 된다.
```

## Canonical 0701 Stage Truth

대상 산출물:

```text
output/census_v4/2026-07-01
```

재집계 결과:

```text
census_stage_map.jsonl rows = 3391

stage:
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

verified_score_present_count = 0
FULL_THESIS row              = 0
FULL_E2R_100 row             = 0
```

해석:

```text
Stage2-Watch 30개는 "운영 Stage2 종목 30개"가 아니다.
이건 Census 상태판에서 "관찰 후보"라는 뜻이다.

운영 점수/Stage로 쓰려면:
  stage_scope = FULL_THESIS
  score_scale = FULL_E2R_100
  verified_score 있음
  operator_stage_use가 운영 사용 가능 상태
가 되어야 한다.

현재는 모두 0개다.
```

## v60 vs v61 비교

비교 대상:

```text
v60:
  output/census_v4/2026-07-01-real-planner-companyguide-claims-v60

v61:
  output/census_v4/2026-07-01-real-planner-companyguide-dedupe-v61
```

Full Thesis seed 000660(SK하이닉스), Research Brain origin만 비교:

```text
v60:
  Full Thesis seed source task executions = 11
  EVIDENCE_OS_ACCEPTED refs              = 6
  unique accepted claims                 = 4
  accepted primitive                     = medium_term_revision_visibility only
  direct accepted claim                  = 0
  direct source task satisfied           = 0

v61:
  Full Thesis seed source task executions = 11
  EVIDENCE_OS_ACCEPTED refs              = 4
  unique accepted claims                 = 1
  accepted primitive                     = medium_term_revision_visibility only
  direct accepted claim                  = 0
  direct source task satisfied           = 0
```

좋아진 점:

```text
같은 CompanyGuide 컨센서스 문서가 task마다 새 claim으로 불어나는 문제가 줄었다.
v60의 unique 4개가 v61에서 unique 1개로 줄었다.
```

아직 안 된 점:

```text
그 1개 claim도 C06 직접 증거가 아니다.
CompanyGuide 컨센서스는 revision visibility 증거일 뿐이다.

아직 없는 직접 증거:
  customer_preorder_or_allocation
  hbm_capacity_pre_sold
  hbm_capacity_constraint
  shipment_or_revenue_mix
  cash_or_revision_conversion 중 실제 cash/FCF 쪽
```

쉬운 예:

```text
증권사 컨센서스 표에 EPS와 목표주가가 있다.
  -> "시장이 실적을 이렇게 보고 있다"는 증거는 된다.

하지만 이 표만 보고:
  -> "엔비디아가 물량을 배정했다"
  -> "HBM CAPA가 sold-out이다"
  -> "FCF 전환이 확인됐다"
라고 하면 안 된다.
```

## v61 Real Planner Smoke

명령:

```bash
rm -rf output/census_v4/2026-07-01-real-planner-companyguide-dedupe-v61
E2R_CODEX_PLANNER_TIMEOUT_SECONDS=120 PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-real-planner-companyguide-dedupe-v61 \
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

결과:

```text
exit code = 1
stdout    = NOT_READY
verdict   = BLOCKED
```

이 실패는 정상이다.

```text
v61의 목표는 "claim 증식 방지"다.
Full Thesis 승급이 목표가 아니었다.
```

v61 주요 수치:

```text
planner row count                  = 22
llm_real_provider_success_count    = 2
source_task_execution_count        = 11
real_document_fetched_count        = 4
brain_stage_trace_count            = 1
brain_score_contribution_count     = 2
brain_promoted_stage_row_count     = 0
full_thesis_claim_count            = 0
llm_claim_extractor_attempt_count  = 0
web_search_task_count              = 0
web_fetched_document_count         = 0
```

Full Thesis seed 000660 trace:

```text
materialization_status = STAGECOURT_READY_NOT_PROMOTED
accepted_claim_count   = 1
accepted_claim_ids     = CLM-b1dcabb4c05931f0f762
score_contribution_count = 2
final_full_thesis_stage  = FULL_THESIS_NOT_RUN
target_archetype_status  = BRAIN_HYPOTHESIS_REQUIRED
```

Full Thesis seed materialization audit:

```text
seed_event_count              = 85
planner_run_seed_count        = 21
real_provider_success_seed_count = 1
stagecourt_trace_seed_count   = 1
full_thesis_promoted_seed_count = 0

status_counts:
  PLANNER_NOT_RUN                   = 64
  PLANNER_PENDING_NO_REAL_PROVIDER_SUCCESS = 20
  STAGECOURT_READY_NOT_PROMOTED     = 1

final_stage_scope_counts:
  CENSUS_EVENT_BOARD = 85

final_score_scale_counts:
  EVENT_WEIGHTED_PARTIAL = 67
  NO_SCORE               = 18
```

Readiness blocker:

```text
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
```

중요한 주의:

```text
source_task_executions.jsonl에는 Research Brain seed 실행과 기존 production_cutover_v3_leaf_artifact 실행이 같이 들어 있다.

000660 전체 파일 기준 seed-like row = 13
Research Brain origin만 보면        = 11

문서와 readiness 판정에는 Research Brain origin 11개를 기준으로 쓴다.
이 origin 분리를 안 하면 "accepted claim이 더 있다"처럼 오독할 수 있다.
```

## v61 Artifact Hashes

```text
brain_web_attempt_audit.json:
  5cfe973844ea144c59b09b27aba67544fde81db421a1819decc91817e904bb25

brain_web_readiness_gate_audit.json:
  c4bbcdf918217e584798a349dc7148d1f79c55f4c3a90c8e8b4a1f530c5c3612

planner_runs.jsonl:
  e643d5cb1df4a9b6f38fd73118b54fc747ac4db3f619645e7bea35e830aa83e3

source_task_executions.jsonl:
  cf603d9743e76c6651b65d80ab8b3a0f41c372ba29309b4825a6367c5ec89ba5

source_tasks.jsonl:
  416273031ce2cdbceb7a90e1d011bcfd32c2cbc945ecb3a930f611f25986d531

full_thesis_seed_materialization_trace.jsonl:
  858ee2902436243d73bebac7354b3054cbb2cf315a7cf5204fedd7ad356d1628
```

## Verification

Targeted test:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_real_source_acquisition -v
```

결과:

```text
Ran 49 tests
OK
```

Extended targeted test:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_operational_modes \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_census_v4_full_thesis_smoke_tasks -v
```

결과:

```text
Ran 128 tests in 32.592s
OK
```

Full suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5085 tests in 206.731s
OK
```

## Cross-Audit Findings

### 1. v61은 claim dedupe 패치이지 Stage 승급 패치가 아니다

통과하면 안 되는 착각:

```text
CompanyGuide claim이 생겼다
-> score contribution이 2개 생겼다
-> StageCourt trace가 생겼다
-> Full Thesis Stage가 있다
```

정확한 흐름:

```text
CompanyGuide claim이 생겼다
-> revision visibility 일부만 채웠다
-> C06 직접 primitive는 아직 비어 있다
-> StageCourt trace는 promotion되지 않았다
-> FULL_THESIS row는 0개다
```

### 2. accepted ref와 unique claim을 구분해야 한다

v61에서는 같은 claim이 4개 SourceTask에서 참조된다.

```text
accepted refs  = 4
unique claim   = 1
```

이건 정상이다.

쉬운 예:

```text
한 장의 영수증이 네 개 체크리스트에서 참고될 수 있다.
하지만 영수증이 네 장 생긴 것은 아니다.
```

### 3. rerouted accepted claim은 원래 gap을 만족하지 않는다

v61 accepted claim은 모두 다음 primitive로만 인정된다.

```text
medium_term_revision_visibility
```

그런데 SourceTask가 요청한 gap은 예를 들어 다음이었다.

```text
customer_preorder_or_allocation
hbm_capacity_pre_sold
cash_or_revision_conversion
```

그래서 status는 다음이어야 한다.

```text
REROUTED_ACCEPTED_CLAIM
satisfies_source_task = False
direct_accepted_claim_count = 0
```

이게 맞다.

쉬운 예:

```text
"재무 예상치" 서류를 찾으러 갔다가 "컨센서스 EPS" 서류를 찾았다.
그 서류는 보관할 가치가 있지만,
"고객 주문서" 칸을 채우면 안 된다.
```

### 4. LLM claim extractor live path는 아직 증명되지 않았다

v61 smoke:

```text
llm_claim_extractor_attempt_count = 0
llm_claim_extractor_real_provider_count = 0
```

즉 이번 smoke에서 claim은 LLM이 자유 텍스트를 읽어서 만든 것이 아니다.
CompanyGuide structured parser와 bridge가 만든 claim이다.

따라서 다음 에이전트가 공격해야 할 지점:

```text
공시/IR/PDF 본문을 LLM이 contract-blind raw assertion으로 뽑고,
anchor/date/entity/temporal 검증을 거쳐 primitive에 매핑하는 live path가
실제 산출물에서 아직 보이지 않는다.
```

### 5. General web path도 이번 smoke에서는 증명되지 않았다

v61 smoke:

```text
web_search_task_count      = 0
web_fetched_document_count = 0
```

이건 실패라기보다 이번 설정이 `live_official_first`이고 universe-limit 1인 제한 smoke였기 때문이다.
하지만 운영 준비성 주장에는 쓰면 안 된다.

정확한 문장:

```text
v61은 official structured source 일부를 검증했다.
bounded general web fallback 운영성은 아직 별도 smoke가 필요하다.
```

## Current Not-Ready Reasons

현재 Full Thesis 운영 파이프라인이 아직 NOT_READY인 이유:

```text
1. FULL_THESIS row = 0
2. FULL_E2R_100 verified score row = 0
3. direct_accepted_claim_count = 0
4. direct_source_task_satisfied_count = 0
5. C06 직접 primitive가 아직 비어 있다.
6. llm_claim_extractor_attempt_count = 0
7. IR provider row가 PROVIDER_FAILED로 남아 있다.
8. StageCourt trace는 생겼지만 promotion verdict가 BLOCKED다.
9. general web fallback은 이번 smoke에서 실행되지 않았다.
```

이 상태에서 "Stage가 있다"고 보고하면 안 된다.

정확한 보고:

```text
Census 상태판은 있다.
Full Thesis 운영 Stage는 없다.
v61은 CompanyGuide consensus claim dedupe만 전진했다.
```

## Next Patch Direction

다음 패치는 "점수 올리기"가 아니라 "증거 경로를 실제 운영형으로 닫기"여야 한다.

### P0. SourceTask execution origin 분리

문제:

```text
source_task_executions.jsonl에 Research Brain seed 실행과 production_cutover_v3_leaf_artifact 실행이 섞여 있다.
```

필요 패치:

```text
origin_scope를 명시적으로 분리한다.
readiness audit에는 full_thesis_seed / representative_leaf / ledger_refresh를 따로 집계한다.
다음 문서 작성자가 전체 파일 count를 보고 잘못 해석하지 않게 한다.
```

Acceptance:

```text
full_thesis_seed_source_task_execution_count와 total_source_task_execution_count가 별도 출력된다.
000660처럼 total 13 / Brain seed 11인 경우도 audit가 혼동 없이 설명한다.
```

### P1. LLM contract-blind claim extractor live path를 실제 source task에 연결

문제:

```text
llm_claim_extractor_attempt_count = 0
```

필요 패치:

```text
official text/PDF/IR/DART 본문이 structured parser로 닫히지 않을 때,
contract-blind extractor를 호출한다.

Extractor 입력에는 score gap, Green 필요 점수, target primitive 답안지를 넣지 않는다.
문서 텍스트, target entity, as_of_date, source metadata만 넣는다.

그 뒤 코드가:
  anchor 검증
  date 검증
  entity directness 검증
  temporal status 검증
  primitive mapping 검증
을 한다.
```

쉬운 예:

```text
나쁜 방식:
  "HBM capacity gap이 비었으니 이 문서에서 capacity 증거를 찾아라"

좋은 방식:
  "이 문서가 말하는 사실을 그대로 뽑아라"
  그 다음 별도 mapper가 "이 claim이 capacity primitive에 해당하는가"를 판정한다.
```

Acceptance:

```text
llm_claim_extractor_attempt_count > 0
llm_claim_extractor_real_provider_count > 0 또는 provider_error가 pending으로 남음
LLM-only inference는 score contribution으로 들어가지 않음
accepted claim은 valid anchor를 가짐
```

### P2. Rerouted claim feedback을 planner에 되돌리기

문제:

```text
CompanyGuide consensus claim은 유용하지만 원래 C06 gap을 만족하지 않는다.
현재는 그 사실이 BLOCKED로 끝나고, 다음 source task 품질 개선으로 충분히 이어지지 않는다.
```

필요 패치:

```text
REROUTED_ACCEPTED_CLAIM을 planner feedback에 넣는다.
LLM에게 "이 claim은 revision visibility로만 인정됐고,
customer/capacity/cash gap은 아직 비어 있다"를 알려준다.

코드는 query를 만들지 않는다.
LLM이 다음 official-first source plan을 제안하고,
코드는 source class, as_of_date, target scope, budget만 검증한다.
```

Acceptance:

```text
replan context에 unsatisfied primitive와 rerouted primitive가 같이 기록된다.
중복 CompanyGuide task만 반복하지 않는다.
direct_source_task_satisfied_count가 0인 상태에서 promotion하지 않는다.
```

### P3. IR / issuer official provider 실패를 pending으로 끝내지 말고 원인별로 분해

문제:

```text
v61 Full Thesis seed에서 IR source class가 PROVIDER_FAILED다.
```

필요 패치:

```text
IR 실패 사유를 구체화한다.
  provider missing
  no document found
  fetch blocked
  parser unsupported
  attachment not parsed
  as_of_date 이후 문서

실패 사유별로 fallback source를 LLM planner에 feedback한다.
```

Acceptance:

```text
IR provider failure가 하나의 뭉뚱그린 문자열로 끝나지 않는다.
fallback이 필요하면 LLM source plan 재시도로 연결된다.
provider failure는 낮은 점수 확정이 아니라 pending/material gap으로 남는다.
```

### P4. Direct primitive 없이는 Stage promotion 금지 유지

문제:

```text
StageCourt trace가 생겼다는 사실만으로 promotion하면 다시 과거 오류가 반복된다.
```

필요 패치:

```text
promotion gate는 지금처럼 엄격해야 한다.
다만 blocked reason을 primitive 단위로 더 자세히 보여줘야 한다.
```

Acceptance:

```text
direct_accepted_claim_count = 0이면 brain_promoted_stage_row_count = 0
full_thesis_claim_count = 0이면 FULL_THESIS row = 0
rerouted accepted claim만으로 FULL_E2R_100 score를 만들지 않음
```

## Next Agent Attack Checklist

다음 에이전트는 아래를 우선 공격하면 된다.

```text
1. v61 문서가 accepted refs와 unique claims를 섞어 쓰지 않았는가?
2. source_task_executions 전체 count와 Brain origin count를 섞어 쓰지 않았는가?
3. CompanyGuide consensus를 cash/FCF 또는 HBM capacity 증거로 과장하지 않았는가?
4. llm_claim_extractor_attempt_count=0인데 "LLM Evidence OS가 살아 있다"고 말하지 않았는가?
5. web path count=0인데 "bounded web fallback이 검증됐다"고 말하지 않았는가?
6. StageCourt trace 1개를 FULL_THESIS Stage로 오해하지 않았는가?
7. score contribution 2개가 direct C06 primitive를 만족한다고 오해하지 않았는가?
8. FULL_THESIS row와 FULL_E2R_100 row가 여전히 0인지 재검산했는가?
9. v61 patch가 종목명 예외 하드코딩이 아닌 anchor identity 안정화인지 확인했는가?
10. 다음 패치가 deterministic query template 추가로 흐르지 않고 LLM planner feedback 개선으로 가는가?
```

## Final State

최종 상태:

```text
v61 code/test status = PASS
v61 real smoke       = NOT_READY / BLOCKED
운영 Full Thesis     = 0 rows
운영 verified score  = 0 rows
다음 목표           = LLM claim extractor live path + direct primitive source closure
```

이번 패치는 의미가 있다.
하지만 운영 가능 선언은 아직 하면 안 된다.


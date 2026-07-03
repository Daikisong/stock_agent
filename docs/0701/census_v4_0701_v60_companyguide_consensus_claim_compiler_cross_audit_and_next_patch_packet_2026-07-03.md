# Census v4 0701 v60 CompanyGuide Consensus Claim Compiler Cross Audit And Next Patch Packet

작성일: 2026-07-03 KST

## 결론

이번 확인의 결론은 세 줄이다.

```text
1. Stage 상태판은 있다.
2. 운영용 FULL_THESIS Stage는 아직 없다.
3. v60은 CompanyGuide 컨센서스 숫자를 claim으로 컴파일하는 첫 구멍을 뚫었지만, Full Thesis 승급은 여전히 막혀 있다.
```

정확히 나누면 다음과 같다.

```text
있는 것:
  CENSUS_EVENT_BOARD base/canonical stage
  예: Stage0, Stage1, Stage2-Watch, Red

없는 것:
  FULL_THESIS stage
  FULL_E2R_100 verified score
  운영 daily에서 쓸 수 있는 100점짜리 full thesis 판정
```

쉬운 예:

```text
출석부에는 "검토 필요" 표시가 있다.
하지만 채점 완료된 답안지는 아직 없다.
v60은 답안지의 "컨센서스/EPS 칸"을 읽기 시작한 것이고,
아직 HBM 고객배정, capacity sold-out, cash/FCF 전환 칸은 비어 있다.
```

## Why This Patch Was Needed

v59까지 확인된 병목은 다음이었다.

```text
Full Thesis seed 000660(SK하이닉스)이 Research Brain으로 들어간다.
LLM planner도 C06 HBM 관련 source task를 낸다.
Source runner도 v59 이후 SourceTask가 요청한 순서대로 CompanyGuide를 먼저 fetch한다.

하지만 CompanyGuide 문서는 provider coverage-only로 처리됐다.
즉 문서는 가져왔는데 숫자 claim으로 바꾸지 못했다.
```

v59 blocker:

```text
provider_coverage_only_until_numeric_revision_parser_accepts_claims
```

그래서 v60의 목표는 크지 않다.

```text
CompanyGuide의 투자의견 컨센서스 표에서
as_of_date 기준으로 유효한 숫자 anchor를 만들고,
그 숫자를 medium_term_revision_visibility claim으로만 인정한다.
```

중요한 제한:

```text
CompanyGuide 컨센서스 숫자만으로 cash_or_revision_conversion을 만족시키면 안 된다.
EPS/목표가 컨센서스는 revision visibility에 가까운 증거다.
실제 현금흐름, FCF, 매출인식, 고객 배정, capacity sold-out 증거가 아니다.
```

쉬운 예:

```text
증권사 컨센서스 표에 EPS 45,534원, 목표주가 501,458원이 있다.
  -> "시장이 실적/목표가를 이렇게 보고 있다"는 revision visibility claim 가능

그 표만 보고 "HBM 고객사가 capacity를 선점했다" 또는 "FCF 전환이 확인됐다"라고 하면 안 된다.
```

## v60 Patch

패치 범위:

```text
src/e2r/production/source_connectors/companyguide_live_connector.py
src/e2r/research_brain/v4_source_acquisition_runner.py
src/e2r/research_brain/v4_evidence_extraction_bridge.py
tests/test_research_brain_v4_real_source_acquisition.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
```

수정한 것:

```text
1. CompanyGuide live connector가 "투자의견 컨센서스" 표를 파싱한다.
2. CONSENSUS_AS_OF_DATE, INVESTMENT_OPINION_SCORE, TARGET_PRC, EPS,
   FORWARD_PER, CONSENSUS_PROVIDER_COUNT를 structured_payload로 넣는다.
3. 컨센서스 기준일이 as_of_date 이후면 score evidence로 막는다.
4. 컨센서스를 못 읽으면 기존처럼 coverage-only score_block_reason을 남긴다.
5. source acquisition anchor exact_text가 structured_payload.score_anchor_text를 우선 사용한다.
6. TARGET_PRC/EPS 숫자는 medium_term_revision_visibility primitive로만 매핑한다.
7. cash_or_revision_conversion 요청 task에서 CompanyGuide 숫자가 들어와도
   REROUTED_ACCEPTED_CLAIM으로 보존하고 원래 gap은 unsatisfied로 남긴다.
8. TARGET_PRC/EPS 개별 필드 존재만으로 POSITIVE polarity를 만들지 않는다.
   CONSENSUS_AS_OF_DATE + EPS/목표가 + 추정기관수 조합이 있을 때만
   "current consensus visibility" composite signal을 만든다.
```

이건 종목 예외 패치가 아니다.

```text
나쁜 방식:
  if symbol == "000660": CompanyGuide를 통과시킨다

이번 방식:
  모든 종목에서 CompanyGuide 컨센서스 표가 있고 날짜가 as_of_date 이하이면
  동일한 parser/anchor/primitive bridge를 적용한다.
```

## Canonical 0701 Stage Truth

대상 산출물:

```text
output/census_v4/2026-07-01
```

직접 집계:

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

verified_score:
  None = 3391

FULL_THESIS row = 0
FULL_E2R_100 row = 0
```

해석:

```text
Stage0/Stage1/Stage2-Watch/Red는 census 상태판이다.
운영자가 "이 종목은 Full Thesis Stage2다"라고 써도 되는 값이 아니다.
```

## v60 Real Planner Smoke

명령:

```bash
rm -rf output/census_v4/2026-07-01-real-planner-companyguide-claims-v60
E2R_CODEX_PLANNER_TIMEOUT_SECONDS=120 PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --output-root output/census_v4/2026-07-01-real-planner-companyguide-claims-v60 \
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
stdout = NOT_READY
```

이 실패는 정상이다.

```text
v60 목표는 "CompanyGuide 숫자 claim 생성"이지
"Full Thesis 운영 승급"이 아니다.
```

## v59 vs v60 Cross Validation

비교 대상:

```text
v59:
  output/census_v4/2026-07-01-real-planner-source-order-v59

v60:
  output/census_v4/2026-07-01-real-planner-companyguide-claims-v60
```

Full Thesis seed 000660 비교:

```text
v59:
  trace accepted_claim_count = 0
  seed source executions = 9
  seed execution accepted refs = 0
  unique accepted claim = 0

v60:
  trace accepted_claim_count = 4
  trace accepted_claim_ids:
    CLM-3bbdd1e2ec90bae35068
    CLM-5701834ef8d5258f1137
    CLM-5c800613790ceb8f3e48
    CLM-d11b99e702438321a892
  seed source executions = 11
  seed execution accepted refs = 6
  unique accepted claim = 4
  accepted primitive = medium_term_revision_visibility only
```

왜 `accepted refs=6`인데 `unique claim=4`인가:

```text
같은 CompanyGuide 컨센서스 claim이 여러 source task gap에서 재사용됐다.
장부에는 source task별 accepted reference가 5번 남지만,
고유 claim ID는 3개다.
```

쉬운 예:

```text
같은 성적표 한 장을
"실적 전망", "목표가 컨센서스", "revision 확인" 세 칸에서 참고할 수 있다.
하지만 성적표 자체가 세 장으로 늘어난 것은 아니다.
```

## v60 Seed Execution Details

Full Thesis seed:

```text
symbol = 000660
company_name = SK하이닉스
target_archetype_status = BRAIN_HYPOTHESIS_REQUIRED
final_full_thesis_stage = FULL_THESIS_NOT_RUN
materialization_status = STAGECOURT_READY_NOT_PROMOTED
score_contribution_count = 2
```

seed source task executions:

```text
total = 11

source_class:
  CompanyGuide = 6
  DART         = 2
  KIND         = 1
  KRX          = 1
  IR           = 1

status:
  EVIDENCE_OS_ACCEPTED = 6
  NO_EVIDENCE_FOUND    = 4
  PROVIDER_FAILED      = 1

accepted primitive refs:
  medium_term_revision_visibility = 6
```

중요한 세부:

```text
CompanyGuide task들은 accepted가 됐지만 모두 REROUTED_ACCEPTED_CLAIM이다.
원래 task gap인 hbm_capacity_pre_sold, customer_preorder_or_allocation,
cash_or_revision_conversion은 그대로 unsatisfied다.
```

예:

```text
task primitive_gap = cash_or_revision_conversion
CompanyGuide accepted primitive = medium_term_revision_visibility
satisfaction_type = REROUTED_ACCEPTED_CLAIM
primitive_gap_unsatisfied_ids = ["cash_or_revision_conversion"]
```

이 동작은 맞다.

```text
컨센서스 EPS는 revision visibility 증거일 수 있지만
현금흐름 전환 증거는 아니기 때문이다.
```

## Readiness Gate Result

대상:

```text
output/census_v4/2026-07-01-real-planner-companyguide-claims-v60/brain_web_readiness_gate_audit.json
```

핵심 값:

```text
verdict = BLOCKED

official_accepted_claim_count = 4
full_thesis_seed_accepted_claim_count = 6
rerouted_accepted_claim_count = 4
rerouted_source_task_claim_count = 6

direct_accepted_claim_count = 0
direct_source_task_satisfied_count = 0

brain_score_contribution_count = 2
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 0
full_thesis_claim_count = 0

llm_planner_call_count = 22
llm_real_provider_success_count = 2
llm_claim_extractor_attempt_count = 0

general_web_search_call_count = 0
web_search_call_count = 0
web_fetched_document_count = 0
web_or_llm_accepted_claim_count = 0
```

blockers:

```text
Brain/Web StageCourt traces are not promoted into census_stage_status
brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
```

해석:

```text
공식 소스 기반 claim 생성은 일부 성공했다.
하지만 원래 Full Thesis gap을 직접 만족한 claim은 0개다.
따라서 운영 Stage 승급은 막히는 것이 맞다.
```

쉬운 예:

```text
지원서에 성적표는 붙었다.
하지만 필수 제출서류인 계약서, 매출인식 증빙, 현금흐름표가 아직 없다.
그래서 심사창구까지는 갔지만 최종 합격 처리는 안 된다.
```

## Artifact Hashes

대상 산출물:

```text
output/census_v4/2026-07-01-real-planner-companyguide-claims-v60
```

해시:

```text
brain_web_attempt_audit.json:
  ad84341b33eba6c2e11a31a279e7b186ba51f1d3d4eb6eb2e16102421c08660d

brain_web_readiness_gate_audit.json:
  09486b6cc3b394d2d14e5e7e1e88ea7898345fb70cce97f254393a9a6cf08153

planner_runs.jsonl:
  b3104c5b75e0e22228191a2d568fe50810befba10b486b994a168f5f665c3b55

source_task_executions.jsonl:
  563ce731ddf99f8cc9a0eabc97bbff3e2c4e48109143c61721caa5cfe4e24c68

source_tasks.jsonl:
  a61aa5a452ebbf04b5ffd912f0e789ccc05728b488927c9418db740c8751f30b

full_thesis_seed_materialization_trace.jsonl:
  c007394145a5746f7d08b5123fa6a4ffe1755bc315b3b7b10710abed915a85e2
```

## Unit Verification

명령:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_research_brain_v4_real_source_acquisition \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_operational_modes \
  -v
```

결과:

```text
Ran 99 tests in 3.597s
OK
```

전체 suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

결과:

```text
Ran 5084 tests in 216.741s
OK
```

중간 회귀 확인:

```text
처음에는 TARGET_PRC/EPS 개별 숫자를 POSITIVE로 처리해서
test_structured_field_presence_is_not_positive가 실패했다.

최종 패치는 이를 되돌려
TARGET_PRC/EPS 개별 필드 = NORMAL,
현재 컨센서스 표 조합 = medium_term_revision_visibility composite signal
로 좁혔다.
```

v60 신규/핵심 테스트:

```text
tests.test_research_brain_v4_real_source_acquisition
  test_companyguide_live_connector_extracts_consensus_numeric_anchor
  test_companyguide_future_consensus_is_score_blocked

tests.test_research_brain_v4_evidence_extraction_from_real_document
  test_companyguide_consensus_numbers_create_revision_visibility_claim_not_cash_conversion
```

검증한 것:

```text
1. CompanyGuide 컨센서스 표에서 날짜와 숫자를 읽는다.
2. as_of_date 이후 컨센서스는 score evidence로 막는다.
3. TARGET_PRC/EPS는 medium_term_revision_visibility claim으로만 간다.
4. cash_or_revision_conversion은 만족시키지 않는다.
```

## What Is Still Wrong

v60 이후에도 운영 준비가 아닌 이유는 명확하다.

```text
1. FULL_THESIS row = 0
2. FULL_E2R_100 verified score row = 0
3. direct_accepted_claim_count = 0
4. direct_source_task_satisfied_count = 0
5. full_thesis_claim_count = 0
6. llm_claim_extractor_attempt_count = 0
7. web/general search path는 이번 smoke에서 0회
8. IR provider는 여전히 PROVIDER_FAILED
9. C06 필수 primitive인 고객 배정, capacity pre-sold, revenue/cash conversion은 직접 닫히지 않았다.
```

특히 `STAGECOURT_READY_NOT_PROMOTED`를 운영 Stage로 오해하면 안 된다.

```text
StageCourt trace가 생성됐다는 뜻:
  일부 claim과 score contribution으로 내부 판정 흔적은 만들었다.

운영 Stage가 생성됐다는 뜻:
  아니다. promotion gate가 BLOCKED다.
```

쉬운 예:

```text
심사위원이 메모를 썼다.
하지만 합격증을 발급하지 않았다.
메모를 합격증이라고 부르면 안 된다.
```

## Cross-Reviewer Attack Points

다음 에이전트는 아래를 공격적으로 확인해야 한다.

```text
1. CompanyGuide consensus claim이 너무 넓게 점수화되지 않는가?
   - 현재는 medium_term_revision_visibility로만 제한되어야 한다.

2. same CompanyGuide page에서 여러 claim ID가 생기는 것이 적절한가?
   - 현재 고유 claim 3개가 모두 medium_term_revision_visibility다.
   - 같은 문서/같은 anchor/같은 primitive라면 더 강한 dedupe가 필요할 수 있다.

3. source_task accepted refs=5와 unique claim=3을 리포트가 혼동하지 않는가?
   - 운영 설명에는 반드시 둘을 분리해야 한다.

4. score_contribution_count=2가 medium_term_revision_visibility만으로 과도한 점수 fan-out을 만들지 않는가?
   - v60은 full thesis promotion을 막았지만, contribution ledger 자체는 별도 감사 대상이다.

5. llm_claim_extractor_attempt_count=0이 괜찮은가?
   - CompanyGuide는 structured bridge라 LLM extractor 없이도 claim 생성 가능하다.
   - 하지만 IR/뉴스/PDF 원문 claim을 만들려면 contract-blind LLM extractor 경로가 실제로 돌아야 한다.

6. IR provider failure가 실제 source gap으로 남는가?
   - low score 확정이 아니라 ProviderPending/unsatisfied gap으로 남아야 한다.

7. C06 seed context가 target_archetype을 강제하지 않는가?
   - target_archetype_status는 BRAIN_HYPOTHESIS_REQUIRED로 유지되어야 한다.
```

## Next Patch Direction

우선순위는 다음이다.

```text
P0. CompanyGuide accepted claim dedupe 강화
    같은 canonical_url/content_hash/anchor/primitive/value에서 claim ID가 여러 개 생기면
    score fan-out 위험이 있다.

P1. CompanyGuide 컨센서스 수치의 delta 의미 분리
    TARGET_PRC/EPS의 절대값은 visibility다.
    "revision"이라고 부르려면 이전 consensus 또는 전기/전월 대비 변화가 필요하다.
    이름은 medium_term_revision_visibility지만 실제 설명에는 "consensus visibility"라고 써야 한다.

P2. C06 direct primitive source acquisition
    customer_preorder_or_allocation,
    hbm_capacity_pre_sold,
    hbm_revenue_or_shipment_mix,
    cash_or_revision_conversion을 직접 닫는 공식/IR/컨콜/신뢰뉴스 경로가 필요하다.

P3. IssuerIR provider 개선
    IR source_class가 PROVIDER_FAILED로 끝나면 C06 HBM 같은 thesis는 대부분 닫히지 않는다.

P4. contract-blind LLM extractor live path 활성 확인
    지금 v60 smoke는 structured official bridge만 썼고 llm_claim_extractor_attempt_count=0이다.
    원문 PDF/기사/컨콜에서 claim을 뽑는 경로가 실제로 돌아야 한다.

P5. Stage promotion 조건 감사
    REROUTED_ACCEPTED_CLAIM만으로 StageCourt trace가 생기는 것은 허용할 수 있지만,
    original material gap이 unsatisfied이면 promotion은 계속 막혀야 한다.
```

## Final Status

현재 상태:

```text
verdict = NOT_READY

v60 patch = useful but partial
official structured claim path = partially working
full thesis production stage = still 0
full E2R verified score = still 0
```

한 문장으로 정리:

```text
v60은 "문서를 가져왔는데 숫자로 못 읽던 문제"를 일부 고쳤지만,
"실제 운영 파이프라인이 Full Thesis Stage를 안정적으로 낸다"는 증거는 아직 없다.
```

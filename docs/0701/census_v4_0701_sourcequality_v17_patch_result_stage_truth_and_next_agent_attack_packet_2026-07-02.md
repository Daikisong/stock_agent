# Census v4 0701 SourceQuality v17 Patch Result / Stage Truth / Next Agent Attack Packet

작성일: 2026-07-02

이 문서는 다음 에이전트가 현재 상태를 빡세게 검증할 수 있게 남기는 최신 감사 패킷이다.

핵심 결론:

```text
뭔가 잘못되고 있던 것이 맞다.

v12에서는 BRAIN_WEB_PARTIAL 1개가 생겼지만,
그 row는 운영 Stage가 아니라 source admissibility와 score fan-out 버그를 보여 주는 진단 row였다.

v17 기준으로 그 가짜 승격은 다시 차단됐다.
현재 운영 FULL_THESIS Stage는 여전히 0개다.
```

쉬운 예:

```text
전에는 영수증 1장에 적힌 "계약이 있다"는 말을
"매출 가시성, 병목 가격결정력, 시장 오판, 밸류 리레이팅"까지 여러 과목 점수로 퍼뜨렸다.

패치 후에는 같은 계약 공시는
"계약금액/기간/납품일정이 확인됐다"는 visibility 재료로만 남고,
마진/현금흐름 bridge가 없으면 병목/오판/밸류 점수로 넘어가지 않는다.
```

## 1. 직접 답

질문:

```text
뭔가 잘못되고 있는 거 맞지?
stage가 있는 애들이 있긴 해?
```

답:

```text
맞다. 잘못되고 있던 부분이 있었다.

Stage label은 있다.
하지만 그 대부분은 CENSUS_EVENT_BOARD 상태판 Stage다.

운영 FULL_THESIS Stage는 아직 0개다.
FULL_E2R_100 verified score row도 아직 0개다.
```

v17 직접 집계:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v17

census_stage_status.jsonl rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3391
  BRAIN_WEB_PARTIAL = 0
  FULL_THESIS = 0

full_thesis_stage:
  FULL_THESIS_NOT_RUN = 3391

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

stage:
  None = 3391

census_stage_summary:
  event_board_non_stage0_count = 85
  full_thesis_stage_row_count = 0
  full_e2r_verified_score_row_count = 0
  verified_score_present_count = 0
```

해석:

```text
85개 non-Stage0 event-board row는 "현재 이벤트 상태판"이다.
운영 thesis score/stage가 아니다.

FULL_THESIS row 0개라는 사실은 변하지 않았다.
```

## 2. v12에서 잘못됐던 것

v12 최신 문서에서 이미 지적한 문제:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v12

BRAIN_WEB_PARTIAL row = 1
symbol = 114450
candidate_event = 그린생명과학 단일판매공급계약 정정
claim = CLM-02f237aeae0a3fb06e45
source = Naver / DigitalToday NEWS
source_task = BrokerReportPublicPDF 계열
primitive = margin_bridge_visible
score contribution = 6개 component로 fan-out
```

핵심 오류:

```text
1. BrokerReportPublicPDF task를 NEWS 문서가 만족한 것처럼 accepted됐다.
2. source provider error가 있었는데 score admissibility에서 막지 못했다.
3. margin_bridge_visible claim 하나가 EPS/FCF 20점 등 여러 component로 퍼졌다.
4. 그래서 BRAIN_WEB_PARTIAL 1개가 생겼지만 운영 증거로 신뢰할 수 없었다.
```

쉬운 예:

```text
"증권사 리포트 PDF를 찾아라"라는 과제였는데,
일반 뉴스 페이지를 가져와 놓고 리포트 증거처럼 점수에 넣은 것이다.
```

## 3. 이번 패치 요약

이번에 막은 경로:

```text
P1. SourceTask score admissibility guard
P2. OpenDART table-style contract parser
P3. guard primitive 양수 score rubric 유입 차단
P4. source family를 primitive 조각이 아니라 문서 단위로 dedupe
P5. C05 계약공시 score fan-out 축소
P6. source-family dedupe trace를 readiness audit이 false blocker로 보지 않게 표시
```

### P1. SourceTask admissibility guard

파일:

```text
src/e2r/research_brain/v4_evidence_extraction_bridge.py
tests/test_research_brain_v4_evidence_extraction_from_real_document.py
```

막은 것:

```text
BrokerReportPublicPDF / ReportPDF task
  -> RESEARCH_REPORT 문서만 score admissible
  -> NEWS 문서, general web provider, trusted_news_provider_not_configured 상태는 rejected

DART/KIND/KRX task
  -> FILING 문서만 score admissible

CompanyGuide task
  -> API record만 score admissible
```

v17 확인:

```text
v12의 suspicious NEWS claim은 더 이상 BRAIN_WEB_PARTIAL로 승격되지 않는다.
v17 brain_stage_promotion_audit:
  verdict = BLOCKED
  brain_promoted_stage_row_count = 0
```

### P2. OpenDART table-style parser

파일:

```text
src/e2r/sources/opendart.py
tests/test_sources.py
```

새로 읽는 값:

```text
매출액 대비(%)
41.18
  -> contract_amount_to_prior_sales = 0.4118

시작일
2025-11-17
종료일
2026-06-30
  -> contract_start = 2025-11-17
  -> contract_end = 2026-06-30
  -> contract_duration_months = 8

계약상대방 정정표
UPL Limited
  -> counterparty = UPL Limited
```

중요한 세부 수정:

```text
"최근매출액(원)" 같은 정정표 라벨을 counterparty로 오인하지 않게 막았다.
```

쉬운 예:

```text
표에
  계약상대방
  최근매출액(원)
  UPL Limited
가 섞여 있을 때,
"최근매출액(원)"이 회사명이 되는 버그를 막았다.
```

### P3. guard primitive 양수 점수 차단

파일:

```text
src/e2r/agentic/evidence_contract_v2.py
tests/test_agentic_evidence_os.py
```

이전 문제:

```text
전 아키타입 설정에서 guard primitive가 양수 score_rubric에 섞인 곳이 57개 있었다.

예:
  cost_overrun
  call_off_risk
  auditor_or_disclosure_risk
  price_only_blowoff

이런 것은 점수를 올리는 재료가 아니라 Green을 막거나 risk를 확인하는 재료다.
```

패치:

```text
Evidence Contract v2 loader가 guard_modes에 있는 primitive를 positive score_rubric에서 자동 제거한다.
```

쉬운 예:

```text
"공사비 초과 위험 있음"은
  visibility +점수
가 아니라
  Green 차단 또는 risk 검토
다.
```

### P4. source family 문서 단위 dedupe

파일:

```text
src/e2r/agentic/primitive_aggregator.py
tests/test_agentic_evidence_os.py
```

이전 문제:

```text
source_family_id가 archetype + primitive + direction + subject + target + anchor로 만들어졌다.
그래서 같은 DART 문서 1개가 primitive별로 여러 source family처럼 보일 수 있었다.
```

패치:

```text
PrimitiveState.support_source_family_ids는 claim.source_document_id를 우선 사용한다.
같은 문서 + 같은 primitive의 중복 support claim은 점수용 PrimitiveState에서 1개만 남긴다.
```

쉬운 예:

```text
DART 공시 1개에서
  계약금액
  계약기간
  납품일정
을 읽어도, 독립 문서 가족은 1개다.

같은 계약금액 claim이 7번 생겨도, 점수에는 대표 1개만 들어간다.
```

### P5. C05 계약공시 fan-out 축소

파일:

```text
configs/e2r_agentic_evidence_contracts_v2.json
tests/test_agentic_evidence_os.py
```

변경 전 C05:

```text
contract_amount_to_prior_sales
contract_duration_months
delivery_schedule

이 3개만 있어도:
  bottleneck_pricing
  market_mispricing
  valuation_rerating
까지 부분점수가 들어갔다.
```

변경 후 C05:

```text
계약금액/기간/일정:
  earnings_visibility
  information_confidence

margin_bridge_visible:
  eps_fcf_explosion
  bottleneck_pricing
  market_mispricing
  valuation_rerating
```

쉬운 예:

```text
"10억 계약이 있고 8개월 납품한다"
  -> 매출 가시성 증거

"그 계약이 고마진이고 FCF/EPS revision으로 이어진다"
  -> 병목/오판/밸류 증거

둘은 다르다.
```

### P6. source-family dedupe trace status

파일:

```text
src/e2r/census/census_runner_v4.py
tests/test_census_v4_brain_web_readiness_gate.py
```

이전 문제:

```text
중복 claim을 점수에서 대표 1개로 접으면,
나머지 accepted claim은 score_contribution_id가 비게 된다.

readiness audit은 이것을 "trace 끊김"으로 오해했다.
```

패치:

```text
trace row에 아래 필드를 추가한다.

score_support_status = SOURCE_FAMILY_DEDUPED
score_deduped_by_source_family = true

readiness audit은 이 row를 missing score contribution 오류로 세지 않는다.
```

쉬운 예:

```text
같은 영수증을 복사해서 20장 만든 경우,
대표 1장만 점수에 연결하고 나머지는 "같은 source라 접음"으로 표시한다.
이건 추적 끊김이 아니다.
```

## 4. v13 -> v17 변화

동일 진단 목적의 핵심 비교:

```text
v13:
  verdict = BLOCKED
  BRAIN_WEB_PARTIAL row = 0
  FULL_THESIS row = 0
  brain_accepted_claim_count = 18
  brain_score_contribution_count = 5
  web_or_llm_accepted_claim_count = 0

  114450 Brain contribution:
    rows = 5
    raw contribution sum = 52.5
    earnings_visibility = 12.0
    bottleneck_pricing = 15.0
    market_mispricing = 11.25
    valuation_rerating = 11.25
    information_confidence = 3.0
    source_family_ids = primitive/anchor 단위 SRC 여러 개

v14:
  verdict = BLOCKED
  BRAIN_WEB_PARTIAL row = 0
  FULL_THESIS row = 0
  brain_score_contribution_count = 2

  114450 Brain contribution:
    rows = 2
    raw contribution sum = 25.0
    earnings_visibility = 20.0
    information_confidence = 5.0
    source_family_ids = DOC-337c7f4d90cc1e30d015

v15:
  verdict = BLOCKED
  BRAIN_WEB_PARTIAL row = 0
  FULL_THESIS row = 0
  duplicate support claims reduced in PrimitiveState
  temporary false blocker:
    Brain/Web trace rows missing score_contribution_id: 21

v17:
  verdict = BLOCKED
  BRAIN_WEB_PARTIAL row = 0
  FULL_THESIS row = 0
  brain_trace_missing_score_contribution_ref_count = 0
  brain_score_contribution_count = 2
  web_or_llm_accepted_claim_count = 0
```

v17의 114450 상태:

```text
primitive_states:
  contract_amount_to_prior_sales = PRESENT_CURRENT, support claims = 1
  contract_duration_months = PRESENT_CURRENT, support claims = 1
  delivery_schedule = PRESENT_CURRENT, support claims = 1
  margin_bridge_visible = UNKNOWN

score_contributions:
  earnings_visibility = 20.0
    support_claim_ids = 3
    source_family_ids = [DOC-337c7f4d90cc1e30d015]

  information_confidence = 5.0
    support_claim_ids = 3
    source_family_ids = [DOC-337c7f4d90cc1e30d015]

  bottleneck_pricing = 0
  market_mispricing = 0
  valuation_rerating = 0
```

중요:

```text
v17 stagecourt trace score_interval = 42.0
score contribution raw sum = 25.0

이 차이는 DeterministicScorer의 runtime archetype weight profile 적용 때문이다.
다음 에이전트는 raw contribution과 weighted total을 섞어 설명하지 말아야 한다.
필요하면 "component raw -> weighted total" audit leaf를 별도로 추가해야 한다.
```

## 5. v17 readiness blockers

`brain_web_readiness_gate_audit.json`:

```text
verdict = BLOCKED

blockers:
  Brain/Web acquisition mode requires web/news search task rows
  Brain/Web acquisition mode requires fetched full-source web/news documents
  web/LLM accepted claim count is zero
  Brain/Web StageCourt traces are not promoted into census_stage_status
  brain stage promotion verdict is not PROMOTION_APPLIED: BLOCKED
  Brain/Web operational minimum planner runs not met: 21/30
  Brain/Web operational minimum web search tasks not met: 0/20
  Brain/Web operational minimum web/news search calls not met: 0/20
  Brain/Web operational minimum fetched documents not met: 0/10
  Brain/Web operational minimum claim extractor attempts not met: 0/10
  Brain/Web operational minimum web/LLM accepted claims not met: 0/3
```

핵심 수치:

```text
brain_accepted_claim_count = 21
official_accepted_claim_count = 21
web_or_llm_accepted_claim_count = 0
llm_extracted_accepted_claim_count = 0
brain_score_contribution_count = 2
brain_promoted_stage_row_count = 0
brain_trace_missing_score_contribution_ref_count = 0
```

해석:

```text
공식 DART claim만으로 Brain trace와 score contribution은 만들어진다.
하지만 이 실행 모드는 Brain/Web acquisition enabled이므로,
web/LLM claim이 0이면 BRAIN_WEB_PARTIAL 승격은 막힌다.
```

쉬운 예:

```text
DART 공시만 읽은 상태에서
"웹/LLM까지 같이 검증한 운영 Brain/Web Stage"라고 말하면 안 된다.
그래서 차단되는 것이 맞다.
```

## 6. 지금 남은 진짜 문제

### A. 운영 FULL_THESIS runner가 아직 없다

현재:

```text
FULL_THESIS row = 0
FULL_E2R_100 verified score row = 0
```

필요:

```text
SourceTask -> EvidenceDocument -> EvidenceAnchor -> RawAssertion
-> AdjudicatedClaim -> PrimitiveState -> ScoreContribution
-> StageCourt -> AtomicStageDecision -> CensusStageStatus

이 체인을 FULL_THESIS scope로 닫아야 한다.
```

### B. Brain/Web live path가 공식 DART에서 멈춘다

v17:

```text
web_search_task_count = 0
web_fetched_document_count = 0
llm_claim_extractor_attempt_count = 0
web_or_llm_accepted_claim_count = 0
```

이전 v14/v15에서는 web task가 2개 생긴 적도 있었지만, v17에서는 후보/LLM 계획 변동으로 0개다.

해석:

```text
공식 source task가 accepted claim target을 만족하면 web/LLM 경로가 조기 종료될 수 있다.
Brain/Web acquisition enabled 모드에서는 이것을 success로 보면 안 되고,
web/LLM minimum gate가 계속 BLOCKED해야 한다.
현재 차단은 맞다.
```

### C. weighted total 42점 설명 leaf가 부족하다

현재:

```text
raw score_contribution sum = 25.0
StageCourt score_interval.lower = 42.0
```

원인:

```text
DeterministicScorer가 Evidence Contract v2 contribution을 component로 변환한 뒤
runtime archetype weight profile을 적용한다.
```

남은 패치:

```text
score_contributions.jsonl:
  raw_points

stagecourt_traces.jsonl:
  weighted_total

사이에 component_weight_trace.jsonl 같은 leaf를 추가해야 한다.
```

쉬운 예:

```text
원점수 25점짜리 시험지가
과목별 가중치 때문에 최종 42점이 됐으면,
"어느 과목에 몇 배 가중이 들어갔는지" 표가 있어야 한다.
```

### D. accepted claim ledger는 아직 중복 row가 많다

v17:

```text
brain_accepted_claim_count = 21
PrimitiveState support claims after dedupe = 3
score contribution support claims = 3
SOURCE_FAMILY_DEDUPED trace rows = 18
```

해석:

```text
점수에는 대표 3개만 들어가게 막았다.
하지만 ledger에는 같은 DART 문서에서 나온 duplicate accepted claim이 아직 많이 남는다.
```

남은 패치:

```text
extraction 단계에서 source task별 반복 추출을 줄이거나,
ledger append 전에 document_id + primitive_id + normalized value 기준 duplicate를
명시적 duplicate event로 append해야 한다.
```

단, 지금은 점수 오염은 막았다.

### E. C05만 세밀하게 손봤고, 전 아키타입 component rubric은 아직 더 봐야 한다

이번 전역 패치:

```text
guard primitive가 positive score_rubric에 들어가는 것은 전 아키타입에서 자동 제거된다.
```

하지만 아직 남은 질문:

```text
C01, C03, C06, C07, C08, C11, C20, C25, C28 등에서
"bridge 없는 계약/고객/테마 primitive"가
market_mispricing / valuation_rerating으로 과하게 퍼지는지
전 아키타입 fixture로 다시 봐야 한다.
```

쉬운 예:

```text
C06에서 "HBM 고객사가 언급됐다"는 사실과
"HBM 매출/마진/FCF가 실제로 전환됐다"는 사실은 다르다.
이번 C05와 같은 fan-out 문제가 다른 아키타입에도 있을 수 있다.
```

## 7. 다음 에이전트가 반드시 공격할 질문

```text
1. FULL_THESIS row가 아직 0개인데, 어떤 문서도 운영 Stage라고 과장하지 않았나?

2. v17의 42점 total은 raw contribution 25점에서 어떻게 만들어졌나?
   component weight trace가 없는데 운영자가 설명 가능한가?

3. official-only DART claim 21개가 Brain/Web enabled 모드에서 왜 web/LLM accepted 0개로 끝났나?
   조기 종료 조건이 accepted_claim_target 때문에 web acquisition을 너무 일찍 멈추는가?

4. 같은 DART 문서 duplicate accepted claim 18개를 SOURCE_FAMILY_DEDUPED로 trace 처리했지만,
   ledger append 단계에서 duplicate event로 남기는 것이 더 맞지 않은가?

5. C05 fan-out은 막았지만 C01/C03/C06/C08/C11/C20/C25/C28에도 같은 fan-out이 남아 있지 않은가?

6. guard primitive positive score 제거가 모든 계약에서 맞는가?
   risk/guard primitive를 별도 negative contribution ledger로 옮기는 후속 구조가 있는가?

7. Brain/Web acquisition enabled 모드에서 web_search_task_count=0이 나오는 것이 정상인가?
   "공식 source로 충분하면 web을 생략"하는 모드와 "Brain/Web 필수 모드"를 분리해야 하지 않은가?

8. score_interval.status가 FINAL인데 promotion은 BLOCKED다.
   이 FINAL은 "official-only partial 내부 점수 final"이지 운영 final이 맞는가?
   명칭이 오해를 부르지 않는가?
```

## 8. 다음 패치 방향

우선순위:

```text
P0. component_weight_trace.jsonl 추가
    raw ScoreContribution -> weighted components -> total_score 변환을 leaf로 남긴다.

P0. Brain/Web acquisition mode 조기 종료 조건 분리
    official accepted target을 만족해도 web/LLM minimum이 필요한 모드에서는
    web source task / claim extractor를 계속 돌리거나,
    SourcePending으로 명확히 남겨야 한다.

P1. ledger duplicate event 도입
    같은 document_id + primitive_id + normalized value 중복은 accepted score claim으로 여러 번 남기지 말고
    DUPLICATES relation으로 append한다.

P1. 전 아키타입 score_rubric fan-out audit
    C05처럼 bridge 없는 primitive가 mispricing/valuation/rerating으로 넘어가는지 전체 검사한다.

P1. FULL_THESIS production runner
    현재 event-board/partial이 아니라 실제 FULL_THESIS scope row를 만드는 runner를 닫는다.

P2. risk/guard negative contribution ledger
    guard primitive를 positive rubric에서 제거한 다음,
    negative/risk contribution과 hard-break quorum으로 별도 처리한다.
```

## 9. 검증 명령과 결과

통과한 테스트:

```bash
PYTHONPATH=src python -m unittest \
  tests.test_census_v4_brain_web_readiness_gate \
  tests.test_agentic_evidence_os.AgenticEvidenceOSTests.test_evidence_contract_v2_loader_can_require_all_archetypes \
  tests.test_agentic_evidence_os.AgenticEvidenceOSTests.test_primitive_aggregation_counts_same_document_as_one_source_family_across_primitives \
  tests.test_agentic_evidence_os.AgenticEvidenceOSTests.test_c05_contract_only_does_not_fan_out_to_margin_or_rerating_components \
  tests.test_sources \
  tests.test_research_brain_v4_evidence_extraction_from_real_document \
  tests.test_research_brain_v4_operational_modes \
  -v
```

결과:

```text
Ran 76 tests in 9.463s
OK
```

전체 repo 테스트:

```bash
PYTHONPATH=src python -m e2r.cli.run_test_command_with_artifact \
  --artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --log output/test_full_repo_0701/full_unittest.log \
  -- python -m unittest discover -s tests -v
```

결과:

```text
status = OK
test_count = 5036
failed_count = 0
error_count = 0
duration_seconds = 204.0577

full_unittest.log tail:
Ran 5036 tests in 202.213s
OK

artifact sha256 = 7fcf62f0a622f14ff91bdc6f26d2936e3b4e733844303b5c6dbae574ace06717
log sha256 = 1ee5fc3667f9d438b933023e907e72010bc9d6c4f1872ba8c731becdcc6268b5
```

v17 스모크:

```bash
PYTHONPATH=src python -m e2r.cli.run_e2r_census_v4_until_pass \
  --as-of-date 2026-07-01 \
  --universe krx \
  --output-root output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v17 \
  --v3-output-root output/census_v3/2026-07-01 \
  --run-mode BRAIN_AND_WEB_ACQUISITION_ENABLED \
  --brain-web-mode enabled \
  --research-brain-report-dir docs/operational \
  --brain-planner-provider codex_cli \
  --brain-source-acquisition live_full_bounded \
  --brain-universe-limit 1 \
  --brain-planner-success-limit 1 \
  --brain-planner-batch-size 1 \
  --brain-max-source-tasks-per-plan 5 \
  --brain-max-fetches-per-task 1 \
  --brain-accepted-claim-target 1 \
  --brain-max-distinct-candidate-attempts 4 \
  --brain-claim-extractor-provider codex_cli \
  --brain-stage-promotion-mode strict \
  --full-thesis-smoke-mode disabled \
  --target-gate brain_web \
  --max-iterations 1 \
  --fail-on-run-mode-overclaim false \
  --fail-on-atomic-mismatch false \
  --fail-on-semantic-guard false \
  --fail-on-critical-audit false \
  --test-result-artifact output/test_full_repo_0701/full_unittest_result_artifact.json \
  --write-operational-docs false
```

결과:

```text
NOT_READY

이것은 이번 목적상 정상이다.
운영 조건을 못 채웠기 때문에 운영 Stage로 승격하지 않았다.
```

## 10. 최종 현재 상태

```text
잘못됐던 부분:
  v12 BRAIN_WEB_PARTIAL suspicious row
  NEWS가 BrokerReport task를 만족한 것처럼 accepted
  C05 계약공시 score fan-out
  same-document source family 부풀림
  guard primitive positive score 유입

이번에 바로잡은 부분:
  source task/document type/provider mismatch score 차단
  DART table 계약금액/기간 parser 개선
  guard primitive positive score 자동 제거
  same-document source family dedupe
  C05 contract-only fan-out 차단
  SOURCE_FAMILY_DEDUPED trace status 도입

아직 남은 부분:
  FULL_THESIS row = 0
  FULL_E2R_100 verified score row = 0
  web/LLM accepted claim = 0
  component raw -> weighted total leaf 부족
  accepted claim duplicate ledger 정리 필요
  전 아키타입 fan-out audit 필요
```

한 줄 결론:

```text
v17은 "운영 Stage가 생겼다"가 아니라
"가짜 Brain/Web partial 승격과 계약공시 점수 번짐을 다시 막았고,
진짜 운영 Stage는 아직 0개임을 더 정확히 드러낸 상태"다.
```

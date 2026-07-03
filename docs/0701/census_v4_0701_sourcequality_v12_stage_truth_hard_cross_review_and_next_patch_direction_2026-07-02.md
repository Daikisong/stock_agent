# Census v4 0701 SourceQuality v12 Stage Truth / Hard Cross-Review / Next Patch Direction

작성일: 2026-07-02

이 문서는 다음 에이전트가 빡세게 공격할 수 있도록 `sourcequality-v12` 산출물을 기준으로 현재 상태를 다시 정리한 감사 패킷이다.

핵심 결론:

```text
뭔가 잘못되고 있는 것 맞다.

Stage label은 있다.
하지만 운영 FULL_THESIS Stage는 아직 0개다.

v12에서 BRAIN_WEB_PARTIAL 1개가 새로 생겼지만,
그 row도 운영 Stage가 아니며 그대로 신뢰하면 안 된다.
```

쉬운 예:

```text
출석부에는 "Stage1", "Stage2-Watch"라고 적힌 학생이 있다.
하지만 답안지 원문 claim -> primitive -> score contribution -> StageCourt까지 닫힌
"정식 시험 점수"는 아직 없다.

v12에서 새로 생긴 BRAIN_WEB_PARTIAL 1건은
답안지 한 문장만 보고 여러 과목 점수를 준 상태라서,
정식 점수로 쓰면 안 된다.
```

## 1. 감사 대상

최신 진단 폴더:

```text
output/census_v4/2026-07-01-brain-web-diagnostic-sourcequality-v12
```

핵심 실행 조건:

```text
as_of_date = 2026-07-01
run_mode = BRAIN_AND_WEB_ACQUISITION_ENABLED
brain_web_mode = enabled
planner_provider = codex_cli
source_acquisition = live_full_bounded
claim_extractor_provider = codex_cli
stage_promotion_mode = strict
accepted_claim_target = 1
max_distinct_candidate_attempts = 4
full_thesis_smoke_mode = disabled
```

중요한 해석:

```text
이 실행은 full thesis 운영 채점 실행이 아니다.
daily census 상태판 + bounded Brain/Web acquisition 진단이다.
```

따라서 `Stage1`, `Stage2-Watch`, `BRAIN_WEB_PARTIAL`이 보여도 그것을 바로 E2R 운영 Stage로 말하면 안 된다.

## 2. 직접 답: Stage가 있는 애들이 있긴 한가?

있다. 하지만 범위를 나눠야 한다.

`census_stage_status.jsonl` 직접 집계:

```text
rows = 3391

stage_scope:
  CENSUS_EVENT_BOARD = 3390
  BRAIN_WEB_PARTIAL = 1
  FULL_THESIS = 0

base_stage:
  Stage0 = 3306
  Stage1 = 54
  Stage2-Watch = 29
  Red = 1
  0 = 1

full_thesis_stage:
  FULL_THESIS_NOT_RUN = 3391

operator_stage_use:
  NOT_FULL_THESIS_STAGE = 3391

score_scope:
  NO_SCORE = 3324
  EVENT_WEIGHTED_PARTIAL = 66
  BRAIN_WEB_CLAIM_BACKED_PARTIAL = 1
  FULL_E2R_100 = 0

score_valid_status:
  NO_CURRENT_EVENT = 3306
  FINAL_WITH_NONMATERIAL_GAPS = 37
  PENDING_MATERIAL_GAPS = 29
  NOT_SCORED = 11
  INVALID_EVIDENCE = 7
  FINAL = 1
```

`census_stage_summary.json` 직접 확인:

```text
full_thesis_stage_row_count = 0
full_e2r_verified_score_row_count = 0
```

판정:

```text
event-board Stage는 있다.
BRAIN_WEB_PARTIAL row도 1개 있다.
운영 FULL_THESIS Stage는 없다.
FULL_E2R_100 verified score도 없다.
```

쉬운 예:

```text
Stage1:
  "현재 이벤트가 있으니 watchlist에서 확인하라"는 상태판이다.

FULL_THESIS Stage:
  "원문 증거를 채택했고, 점수 기여가 claim으로 설명되고,
   StageCourt가 운영 기준으로 확정했다"는 정식 판단이다.

현재는 첫 번째만 있고, 두 번째는 0개다.
```

## 3. Brain/Web readiness 교차검증

`brain_web_readiness_gate_audit.json` 기준:

```text
verdict = BLOCKED

llm_planner_call_count = 22
llm_real_provider_success_count = 2
source_task_execution_count = 17
web_search_task_count = 4
web_search_result_count = 22
web_fetched_document_count = 2
web_rejected_document_count = 11
llm_claim_extractor_attempt_count = 2

brain_accepted_claim_count = 1
official_accepted_claim_count = 0
web_or_llm_accepted_claim_count = 1
brain_score_contribution_count = 6
brain_stage_trace_count = 1
brain_promoted_stage_row_count = 1
```

blockers:

```text
Brain/Web operational minimum planner runs not met: 22/30
Brain/Web operational minimum web search tasks not met: 4/20
Brain/Web operational minimum web/news search calls not met: 4/20
Brain/Web operational minimum fetched documents not met: 2/10
Brain/Web operational minimum claim extractor attempts not met: 2/10
Brain/Web operational minimum web/LLM accepted claims not met: 1/3
```

`brain_stage_promotion_audit.json` 기준:

```text
verdict = PROMOTION_APPLIED
brain_promoted_stage_row_count = 1
web_or_llm_accepted_claim_count = 1
official_accepted_claim_count = 0
```

해석:

```text
v12는 이전 v9보다 한 걸음 나아가서 BRAIN_WEB_PARTIAL 1개를 만들었다.
하지만 readiness는 여전히 BLOCKED다.
그리고 그 1개 partial row 자체도 아래 이유로 신뢰하면 안 된다.
```

## 4. v12에서 실제 승격된 1건

승격 row:

```text
symbol = 114450
company = 그린생명과학
candidate_event_id = CE-LIVE-DART-114450-20260630901605
event = [기재정정]단일판매ㆍ공급계약체결
stage_scope = BRAIN_WEB_PARTIAL
score_scope = BRAIN_WEB_CLAIM_BACKED_PARTIAL
base_stage = 0
canonical_stage = 0
full_thesis_stage = FULL_THESIS_NOT_RUN
operator_stage_use = NOT_FULL_THESIS_STAGE
operator_score_use = NOT_FULL_E2R_SCORE
accepted_claim_ids = [CLM-02f237aeae0a3fb06e45]
stagecourt_trace_id = SCT-BRAIN-8ccd957bb73ee71b698b
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

즉 이 row는 운영 Stage가 아니다.

쉬운 예:

```text
"계약 공시가 있어서 Brain/Web partial 진단 row를 만들었다"는 말은 가능하다.
"그린생명과학이 E2R 운영 Stage 0으로 확정됐다"는 말은 틀리다.
```

## 5. 승격 claim의 정체

`accepted_claims.jsonl`의 accepted claim:

```text
claim_id = CLM-02f237aeae0a3fb06e45
symbol = 114450
primitive_id = margin_bridge_visible
mapping_status = ACCEPTED
support_direction = SUPPORT
score_eligible = true
target_scope_status = DIRECT
directness = DIRECT
temporal_status = CURRENT
polarity = NORMAL
semantic_status = PASS
source_provider = https://openapi.naver.com/v1/search/webkr.json
source_url = https://www.digitaltoday.co.kr/news/articleView.html?idxno=665445
document_id = DOC-df35a94d9d715b2447ae
anchor_id = ANCH-031fd2b4c8becfa8c30b
raw_assertion_id = RAWLLM-7cfae954fb46ce9595ac
```

문서/앵커:

```text
evidence_document.source_type = NEWS
canonical_url = https://www.digitaltoday.co.kr/news/articleView.html?idxno=665445
published_at = 2026-07-01
available_at = 2026-07-01
anchor_type = TEXT_SPAN
normalized_value = null
```

claim quote 요지:

```text
그린생명과학이 2026년 5월 13일 AI반도체 소재 공급계약을 체결.
계약금액 100억5000만원.
최근 매출액 403억3962만2036원의 약 24.91%.
계약 상대방은 그린케미칼.
계약 기간은 2026년 5월 18일부터 12월 31일까지.
```

문제:

```text
이 문장은 계약 규모/기간/상대방 claim으로는 쓸 수 있다.
하지만 margin_bridge_visible, EPS/FCF 폭발성, bottleneck pricing까지 직접 증명한다고 보기 어렵다.
```

쉬운 예:

```text
"100억원 계약을 했다"는 말은
  contract_amount_to_prior_sales 증거다.

"그 계약 때문에 마진이 개선된다"는 말은
  margin_bridge_visible 증거다.

지금은 첫 번째 문장을 두 번째처럼 읽고,
다시 여러 점수 과목에 뿌린 상태다.
```

## 6. SourceTask 정합성 문제

같은 accepted claim을 만든 `source_task_executions.jsonl` row:

```text
symbol = 114450
archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
primitive_gap = margin_bridge_visible
source_class = BrokerReportPublicPDF
status = EVIDENCE_OS_ACCEPTED
provider_errors = ["trusted_news_provider_not_configured; general search is not a score source"]
accepted_claim_ids = [CLM-02f237aeae0a3fb06e45]
```

하지만 실제 accepted claim:

```text
source_provider = Naver web search API
source_url = DigitalToday news article
source_type = NEWS
```

판정:

```text
source task가 요구한 source_class와 실제 source_provider/source_type이 맞지 않는다.
provider_errors가 있는데 accepted claim과 score contribution으로 이어졌다.
```

이건 다음 패치에서 반드시 막아야 한다.

허용 가능한 상태:

```text
source_class = BrokerReportPublicPDF
  -> 실제 document.source_type이 REPORT/PDF 또는 public broker report여야 함

source_class = TrustedNews
  -> 실제 document.source_type이 NEWS이고 trusted news provider/fetch가 성공해야 함

provider_errors에 "general search is not a score source"가 있으면
  -> 그 execution에서 나온 claim은 score_eligible=false 또는 promotion blocked여야 함
```

## 7. Score contribution 과대 확산 문제

`score_contributions.jsonl`에서 `CLM-02f237aeae0a3fb06e45` 하나가 만든 contribution:

```text
eps_fcf_explosion      = 20.0
earnings_visibility   = 4.0
bottleneck_pricing    = 5.0
market_mispricing     = 3.75
valuation_rerating    = 3.75
information_confidence= 1.0
```

같은 claim 하나가 6개 component를 지지한다.

C05 contract score rubric 확인:

```text
C05 required_primitives:
  contract_amount_to_prior_sales
  contract_duration_months
  margin_bridge_visible
  cost_overrun
  delivery_schedule

C05 score_rubric:
  eps_fcf_explosion -> margin_bridge_visible
  earnings_visibility -> contract_amount_to_prior_sales, contract_duration_months, margin_bridge_visible, cost_overrun, delivery_schedule
  bottleneck_pricing -> contract_amount_to_prior_sales, contract_duration_months, margin_bridge_visible, delivery_schedule
  market_mispricing -> contract_amount_to_prior_sales, contract_duration_months, margin_bridge_visible, delivery_schedule
  valuation_rerating -> contract_amount_to_prior_sales, contract_duration_months, margin_bridge_visible, delivery_schedule
  information_confidence -> contract_amount_to_prior_sales, contract_duration_months, margin_bridge_visible, cost_overrun, delivery_schedule
```

문제:

```text
margin_bridge_visible 하나가 PRESENT_CURRENT가 되면
eps_fcf_explosion 20점이 바로 열릴 수 있다.
```

이건 운영에서 위험하다.

쉬운 예:

```text
"계약이 있다" 한 문장만으로
"이익/현금흐름 폭발성 만점"을 주면 안 된다.

이익/현금흐름 폭발성은
계약 규모, 매출 인식, 마진, 원가, 현금 전환 중 최소 복수 primitive가 닫혀야 한다.
```

다음 패치 원칙:

```text
1. one claim -> one primitive는 가능하지만,
   one weak primitive -> many high-point components는 제한해야 한다.

2. eps_fcf_explosion 같은 핵심 component는 k-of-n quorum 필요.
   예: contract_amount_to_prior_sales + margin_bridge_visible + cash_or_revision_conversion 중 2개 이상.

3. margin_bridge_visible은 원문에 "마진/수익성/원가/현금흐름 bridge"가 명시될 때만 ACCEPT.
   계약 규모만 있으면 margin_bridge_visible이 아니라 contract_amount_to_prior_sales로 가야 한다.

4. NORMAL polarity claim이 핵심 component 만점으로 이어지면 안 된다.
   최소 POSITIVE polarity 또는 numeric bridge/source quorum을 요구해야 한다.
```

## 8. 공식 DART에서 놓친 좋은 증거

v12의 가장 큰 역설:

```text
공식 DART 원문에는 좋은 구조화 증거가 있다.
하지만 Evidence OS가 이 값을 contract primitive로 채택하지 못했다.
```

DART anchor raw text에는 다음이 있다.

```text
확정 계약금액
10,238,670,000

계약금액 총액(원)
10,238,670,000

최근 매출액(원)
24,860,636,227

매출액 대비(%)
41.18

계약상대방
UPL Limited

계약기간
시작일
2025-11-17
종료일
2026-06-30
```

하지만 `evidence_anchors.jsonl`의 normalized row에는:

```text
contract_amount = 10238670000.0
contract_amount_to_prior_sales = missing
contract_duration_months = missing
contract_start = missing
contract_end = missing
```

그 결과 DART source tasks:

```text
contract_amount_to_prior_sales -> NO_EVIDENCE_FOUND
contract_duration_months -> NO_EVIDENCE_FOUND
delivery_schedule -> NO_EVIDENCE_FOUND
contract_visibility -> NO_EVIDENCE_FOUND
```

rejected claim 예:

```text
primitive_id = contract_amount_to_prior_sales
mapping_status = REJECTED
support_direction = SUPPORT
score_eligible = false
polarity = NORMAL
raw_assertion_id = RAWASSERTV4-724172f692221badca9e780e
```

왜 이런가:

```text
현재 DART parser는 "매출액 대비(%) 41.18"처럼 라벨과 값이 줄바꿈으로 나뉜 표형 텍스트를 충분히 못 읽는다.
계약기간도 "계약기간 / 시작일 / 종료일" 표형 구조를 못 읽는다.
```

쉬운 예:

```text
공식 답안지에는 "매출액 대비 41.18%"가 적혀 있다.
그런데 채점기가 "매출액 대비: 41.18%" 한 줄 형태만 찾아서 답을 못 읽었다.
그래서 옆에 있는 뉴스 문장을 억지로 마진 증거로 채택했다.
```

다음 패치 원칙:

```text
1. OpenDART detail raw_text에서 표형 key/value를 파싱해야 한다.
   - "매출액 대비(%)\\n41.18"
   - "시작일\\n2025-11-17\\n종료일\\n2026-06-30"
   - "계약금액 총액(원)\\n10,238,670,000"

2. parsed_fields/structured_payload에 다음을 넣어야 한다.
   - contract_amount_to_prior_sales = 0.4118
   - contract_start = 2025-11-17
   - contract_end = 2026-06-30
   - contract_duration_months = 8 또는 일수 기반 duration
   - counterparty = UPL Limited

3. structured field polarity는 numeric positive official bridge가 되어야 한다.
   - contract_amount_to_prior_sales > 0 -> POSITIVE
   - contract_duration_months > 0 -> POSITIVE

4. 이 값들이 accepted claim -> primitive_state -> score_contribution까지 이어져야 한다.
```

## 9. Planner/router는 개선됐다

v9의 병목은 직접 공급계약 공시가 C29/volume 쪽으로 빠지는 문제였다.

v12에서는 첫 planner가 다음처럼 개선됐다.

```text
candidate_event = CE-LIVE-DART-114450-20260630901605
event = [기재정정]단일판매ㆍ공급계약체결
primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
must_verify_primitives:
  contract_amount_to_prior_sales
  contract_duration_months
  contract_visibility
  delivery_schedule
  margin_bridge_visible
  cash_or_revision_conversion
```

판정:

```text
route는 좋아졌다.
문제는 source extraction / claim mapping / score fan-out 쪽으로 이동했다.
```

쉬운 예:

```text
이제 수학 시험지를 국어 선생님에게 보내는 문제는 줄었다.
하지만 수학 답안의 숫자를 못 읽고,
뉴스 문장 하나로 여러 수학 문제를 맞았다고 처리하는 문제가 남았다.
```

## 10. 삼성전자/하이닉스 관련 현재 진실

v12 `census_stage_status.jsonl`에서:

```text
005930 삼성전자:
  base_stage = Stage1
  stage_scope = CENSUS_EVENT_BOARD
  score_scope = EVENT_WEIGHTED_PARTIAL
  operator_stage_use = NOT_FULL_THESIS_STAGE
  full_thesis_stage = FULL_THESIS_NOT_RUN
  full_e2r_verified_score = null
  primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP

000660 SK하이닉스:
  base_stage = Stage1
  stage_scope = CENSUS_EVENT_BOARD
  score_scope = EVENT_WEIGHTED_PARTIAL
  operator_stage_use = NOT_FULL_THESIS_STAGE
  full_thesis_stage = FULL_THESIS_NOT_RUN
  full_e2r_verified_score = null
  primary_archetype = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

판정:

```text
삼성전자/하이닉스의 C06 HBM FULL_THESIS 운영 점수/Stage는 아직 없다.
현재 보이는 Stage1은 daily event-board 상태판이다.
```

쉬운 예:

```text
삼성전자/하이닉스에 "오늘 확인할 이벤트가 있다"는 스티커는 붙어 있다.
하지만 "HBM thesis를 C06 기준으로 채점 완료했다"는 도장은 아직 없다.
```

## 11. 외부 리뷰어가 공격해야 할 질문

다음 질문에 전부 답하지 못하면 완료라고 하면 안 된다.

```text
1. 왜 FULL_THESIS row가 0인데 Stage가 있다고 말할 수 있는가?
2. BRAIN_WEB_PARTIAL 1개를 운영 Stage로 오해하지 않게 막았는가?
3. source_task.source_class=BrokerReportPublicPDF인데 실제 provider가 Naver web인 이유는 무엇인가?
4. provider_errors에 "general search is not a score source"가 있는데 score_eligible=true가 된 이유는 무엇인가?
5. DigitalToday 뉴스 문장 하나가 margin_bridge_visible로 accepted된 근거는 충분한가?
6. margin_bridge_visible 하나가 eps_fcf_explosion 20점으로 이어져도 되는가?
7. 같은 claim 하나가 6개 score contribution을 지지해도 되는가?
8. 공식 DART 원문에 매출액 대비 41.18%가 있는데 왜 contract_amount_to_prior_sales가 UNKNOWN인가?
9. 공식 DART 원문에 계약 시작/종료일이 있는데 왜 contract_duration_months가 UNKNOWN인가?
10. 삼성전자/하이닉스 Stage1을 HBM/C06 운영 Stage처럼 읽는 문장이 남아 있는가?
```

## 12. P0 패치 방향

우선순위는 다음 순서다.

### P0-1. SourceTask admissibility guard

목표:

```text
source task가 허용한 source class와 실제 document/source provider가 맞지 않으면 score_eligible=false.
provider_errors가 score source 불가를 말하면 promotion blocked.
```

예:

```text
BrokerReportPublicPDF task에서 Naver web NEWS가 들어왔다.
  -> claim은 diagnostics로 남길 수 있다.
  -> score contribution과 BRAIN_WEB_PARTIAL promotion은 금지한다.
```

### P0-2. DART table-style field parser

목표:

```text
공식 DART 원문의 표형 key/value를 구조화한다.
```

필수 fixture:

```text
매출액 대비(%)\\n41.18 -> contract_amount_to_prior_sales = 0.4118
계약기간\\n시작일\\n2025-11-17\\n종료일\\n2026-06-30 -> contract_duration_months present
계약상대방\\nUPL Limited -> counterparty = UPL Limited
```

### P0-3. Primitive mapper contract specificity

목표:

```text
계약 규모/기간 문장은 margin_bridge_visible이 아니라
contract_amount_to_prior_sales / contract_duration_months / delivery_schedule로 간다.
```

예:

```text
"계약금액은 최근 매출의 24.91%" -> contract_amount_to_prior_sales
"계약기간은 2026-05-18부터 2026-12-31" -> contract_duration_months
"마진 개선이 예상된다" 또는 "고부가 제품 공급으로 수익성 개선" -> margin_bridge_visible 후보
```

### P0-4. Score contribution quorum / fan-out cap

목표:

```text
한 primitive 또는 한 claim이 고점수 component 여러 개를 자동으로 열지 못하게 한다.
```

규칙 예:

```text
eps_fcf_explosion:
  margin_bridge_visible alone -> max 0 또는 low cap
  contract_amount_to_prior_sales + margin_bridge_visible + cash/revision bridge 중 k-of-n 충족 -> 점수 허용

bottleneck_pricing:
  계약 존재만으로는 0
  capacity/shortage/pricing/pass-through claim 필요

market_mispricing / valuation_rerating:
  계약 claim alone으로는 낮은 cap
  consensus/revision/valuation evidence 필요
```

### P0-5. FULL_THESIS stage wording guard

목표:

```text
output/report/docs 어디에서도 CENSUS_EVENT_BOARD/BRAIN_WEB_PARTIAL을
FULL_THESIS 운영 Stage처럼 표현하지 않게 한다.
```

예:

```text
나쁜 문장:
  "삼성전자 Stage1"

좋은 문장:
  "삼성전자는 daily event-board Stage1이며,
   C06 FULL_THESIS Stage는 FULL_THESIS_NOT_RUN이다."
```

## 13. 다음 live run에서 기대하는 성공 형태

다음 패치 후 재실행하면 아래처럼 바뀌어야 한다.

```text
114450 DART official:
  contract_amount_to_prior_sales accepted
  contract_duration_months accepted
  delivery_schedule accepted
  margin_bridge_visible은 원문 근거 없으면 UNKNOWN

DigitalToday/Naver web:
  source class mismatch 또는 provider error가 있으면 score_eligible=false
  또는 TrustedNews task로 정합하게 들어온 경우에만 제한적으로 accepted

score contributions:
  contract_amount_to_prior_sales claim -> 관련 component에 제한 점수
  margin_bridge_visible absent -> eps_fcf_explosion 20점 금지

stage:
  BRAIN_WEB_PARTIAL은 source-backed partial로 남을 수 있지만
  FULL_THESIS는 여전히 full thesis runner가 닫히기 전까지 0이어야 함
```

## 14. 완료 기준

다음 조건을 만족하기 전에는 "운영 Stage가 있다"고 말하면 안 된다.

```text
1. full_thesis_stage_row_count > 0
2. full_e2r_verified_score_row_count > 0
3. 해당 row의 operator_stage_use = FULL_THESIS_STAGE_ALLOWED 또는 동등한 운영 허용 상태
4. score_scope = FULL_E2R_100
5. 모든 nonzero score_contribution에 accepted support_claim_ids 존재
6. accepted claim -> primitive_state -> score_contribution -> stagecourt_trace -> representative row trace가 끊기지 않음
7. source task class와 실제 source provider/type이 정합
8. provider_errors가 있는 source task에서 score contribution이 생기지 않음
9. 공식 DART 숫자/기간 primitive가 table-style 원문에서도 accepted
10. one weak claim이 eps_fcf_explosion 같은 고점수 component를 단독 개방하지 않음
```

## 15. 최종 판정

```text
v12는 "완료에 가까워졌다"가 아니다.
v12는 "진짜 병목이 어디인지 더 선명해졌다"에 가깝다.
```

좋아진 점:

```text
1. 직접 공급계약 공시를 C05로 route하는 방향은 개선됐다.
2. bounded live source task와 LLM claim extraction이 실제로 움직였다.
3. rejected/accepted claim 장부가 있어 오류를 추적할 수 있다.
```

나쁜 점:

```text
1. FULL_THESIS 운영 Stage는 여전히 0개다.
2. BRAIN_WEB_PARTIAL 1개는 source admissibility와 score fan-out 관점에서 의심스럽다.
3. 공식 DART에 있는 좋은 숫자 증거를 parser가 못 읽고 있다.
4. 뉴스 claim 하나가 너무 넓은 점수로 번졌다.
5. 삼성전자/하이닉스 C06 운영 Stage는 아직 전혀 계산되지 않았다.
```

한 문장 요약:

```text
현재 시스템은 상태판 Stage는 만들지만,
운영 full thesis Stage를 만들기에는 source admissibility, DART 구조화, primitive mapping, score quorum이 아직 부족하다.
```


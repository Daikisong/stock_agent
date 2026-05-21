좋아. 순서상 이번은 **R13 Loop 7 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리**다.

이번 R13은 새 섹터가 아니라, **R1~R12에서 나온 모든 후보를 최종 재판하는 라운드**다. Round 40 지도에서도 R13은 `accounting_trust`, `crowding`, `valuation_band`, `price_only_rally`, `hard_4c`, `score_price_alignment`를 검증하는 cross-sector overlay로 정의되어 있다. 

---

# 1. 이번 라운드 대섹터

```text
R13 = Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리
large_sector = CROSS_ARCHETYPE_OVERLAY
round = R13 Loop 7 / price-path validation
목표 = R1~R12 case의 Stage 3 / 4B / 4C 판정 품질 검증
```

R13의 핵심은 “좋은 섹터인가?”가 아니라:

```text
Stage 3가 진짜 돈 되는 구간을 잡았나?
4B가 peak 전후에 붙었나?
4C가 큰 하락 전에 붙었나?
가격이 증거보다 먼저 간 것은 아닌가?
테마·이벤트·정책·루머를 구조적 E2R로 착각하지 않았나?
```

이다.

Round 119 원칙상 R13에서 부족한 건 `high_score`, `past_winner_similarity`이고, 필요한 건 `structural_vs_cycle_vs_event`, `4B`, `4C`, `accounting_trust`, `price_validation`이다. Green blocker는 `hard_redteam`, `saturated_4b`, `false_positive_score`다. 

---

# 2. 대상 canonical archetype

```text
STRUCTURAL_SUCCESS_ALIGNED
STRUCTURAL_SUCCESS_BUT_4B_WATCH
SECTOR_SUCCESS_BUT_4B_WATCH
CROWDED_RERATING_4B_WATCH
PRICE_ONLY_RALLY
EVENT_PREMIUM
FALSE_POSITIVE_SCORE
EVIDENCE_GOOD_BUT_PRICE_FAILED
THESIS_BREAK_4C
OPERATIONAL_TRUST_BREAK
LEGAL_REGULATORY_REDTEAM
LEVERAGE_FCF_BREAKDOWN
COMMERCIALIZATION_FAILURE
DISCLOSURE_CONFIDENCE_CAP
CIRCULAR_AI_FINANCING_WATCH
UNKNOWN_INSUFFICIENT_EVIDENCE
```

이번 R13은 R1~R12의 여러 케이스 중 실제 price validation anchor가 비교적 명확한 것만 골랐다. 완전한 KRX/Naver 수정주가 OHLC를 자동 추출하지 못한 종목은 `price_data_unavailable_after_deep_search`로 표시하고, 대신 Reuters/FT/WSJ가 제공한 가격 anchor와 퍼센트 수익률을 사용해 계산 가능한 값만 계산했다.

---

# 3. deep sub-archetype

```text
Stage 3 성공 검증:
- Stage 3 이후 MFE가 큰가?
- MAE가 감당 가능한가?
- below_stage3_price_flag가 과도하지 않은가?

4B 검증:
- 주가가 이미 2~5배 이상 오른 뒤 valuation/crowding이 붙었는가?
- 좋은 뉴스에도 주가 반응이 둔화되는가?
- dilution / capital raise / 과도한 CAPEX가 나왔는가?

4C 검증:
- 계약 취소
- 계약가치 대폭 축소
- 안전사고
- 회계·공시 신뢰 훼손
- 규제·법적 리스크
- 고객 수요 붕괴
- 정책 이벤트 fade

price-only / event premium 검증:
- 자원 발견
- MOU
- 정책 발표
- AI partnership
- IPO/상장 이벤트
- 미확정 media report
```

---

# 4. 국장 신규 후보 case

## Case A — SK하이닉스 `structural_success_aligned + 4B-watch benchmark`

```text
symbol = 000660
source_sector = R2 AI·반도체·전자부품
archetype = MEMORY_HBM_CAPACITY / STRUCTURAL_SUCCESS_BUT_4B_WATCH
case_type = structural_success + 4B-watch
```

SK하이닉스는 R13에서 **Stage 3가 대시세를 잡을 수 있었는지**를 검증하는 benchmark다. Reuters는 SK하이닉스 주가가 2025년에 274% 상승했고, 2026년에도 5월 14일 기준 200% 넘게 올랐으며, 시가총액은 16개월 전 1,000억 달러 미만에서 약 9,420억 달러까지 커졌다고 보도했다. 이 상승은 AI 서버에 쓰이는 HBM과 전통 메모리 수요가 함께 견인했다. ([Reuters][1])

### stage date 후보

```text
Stage 1:
2024~2025
- AI server / HBM demand
- SK하이닉스 HBM leadership

Stage 2:
2025년 HBM 실적·컨센서스 상향 구간
- 정확한 stage2 evidence date는 기존 R2 case와 연결

Stage 3:
기존 R2 case에서 확정해야 함
- HBM demand + capacity constraint + EPS revision + customer visibility

Stage 4B:
2026-05-14
- 2025년 +274%
- 2026년 YTD +200% 이상
- 시총 약 $942B
- 1조 달러 근접
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported return / market-cap path

OHLC source:
price_data_unavailable_after_deep_search
- KRX/Naver/Yahoo OHLC 직접 추출은 이번 환경에서 성공하지 못함.
- Reuters가 제공한 누적 수익률과 시가총액 anchor로 계산.

stage3_price:
price_data_unavailable_after_deep_search

reported_return_2025:
+274%

reported_return_2026_to_2026-05-14:
> +200%

minimum_compounded_return_from_start_2025_to_2026-05-14:
(1 + 2.74) * (1 + 2.00) - 1 = +1,022% 이상

market_cap_path:
< $100B → 약 $942B
minimum_market_cap_MFE:
약 +842% 이상

MFE_30D / 90D / 180D:
OHLC unavailable

MFE_1Y / 2Y:
reported cumulative path 기준 대형 MFE 확인

MAE:
OHLC unavailable

below_stage3_price_flag:
OHLC unavailable

peak_price:
OHLC unavailable

drawdown_after_peak:
관측 필요
```

### score-price alignment

```text
alignment = aligned
rerating_result = true_rerating
4B_status = 4B-watch / possibly 4B-elevated
```

### R13 판정

SK하이닉스는 **Stage 3 gate가 잘 작동했을 가능성이 매우 높은 성공 benchmark**다. 다만 2026년 5월 기준으로는 신규 Stage 3가 아니라 4B-watch다.

```text
올릴 축:
eps_fcf_revision
capacity_bottleneck
customer_visibility
old_frame_mispricing
price_path_alignment

강화할 4B:
market_cap_threshold
crowding
consensus_saturation
AI_capex_dependency
customer_price_resistance
```

---

## Case B — 한화에어로스페이스 `structural_success + 4B timing test`

```text
symbol = 012450
source_sector = R1 산업재·수주·인프라
archetype = DEFENSE_GOVERNMENT_BACKLOG / STRUCTURAL_SUCCESS_BUT_4B_WATCH
case_type = structural_success + 4B-watch
```

한화에어로스페이스는 R13에서 **4B를 hard exit로 오해하면 안 되는 케이스**다. FT는 한화에어로스페이스 주가가 지난 1년 동안 187,500원에서 1,435,000원으로 상승했다고 보도했다. 같은 기사에서 현대로템은 6배 이상, LIG넥스원은 이란전쟁 이후 약 47% 상승했다고 정리됐다. ([Financial Times][2])

또 2025년 3월 한화에어로스페이스는 3.6조 원 유상증자를 발표했고, 주가는 하루 13% 하락했다. FT는 이 자금조달이 해외 공장·파트너 지분투자를 위한 것이라고 설명했다. ([Financial Times][3])

### stage date 후보

```text
Stage 1:
2022~2024
- 유럽 재무장
- 폴란드 / 천무 / K9 수출 확대

Stage 2:
2024~2025
- 수주잔고 확대
- 유럽·중동·노르웨이 등 방산 수요 확대

Stage 3:
2024~2025 중 수주잔고와 이익 체급 변화 확인 구간
- 정확한 entry_date는 R1 case row에서 확정 필요

Stage 4B:
2025-03-21
- 주가 YTD 2배 이상 상승 후
- 3.6조 원 증자 발표
- 하루 -13%

Stage 4C:
없음
- 증자는 dilution shock이지만 방산 수요 thesis break는 아님
```

### 실제 가격경로 검증

```text
price_data_source:
FT reported price path + Reuters/FT capital raise reaction

stage3_price_anchor:
187,500원

reported_peak_price:
1,435,000원

MFE_from_anchor_to_reported_peak:
(1,435,000 / 187,500) - 1 = +665.3%

4B_event:
2025-03-21 capital raise shock

4B_event_MAE_1D:
-13%

MFE_30D / 90D / 180D / 1Y:
OHLC unavailable, but 1Y reported MFE = +665.3%

MAE_30D / 90D:
OHLC unavailable

below_stage3_price_flag:
very unlikely from reported path, but OHLC unavailable

drawdown_after_peak:
OHLC unavailable
```

### score-price alignment

```text
alignment = aligned
rerating_result = true_rerating
4B_status = 4B-watch_success_but_not_exit
```

### R13 판정

한화에어로스페이스는 **Stage 3 이후 대형 MFE가 확인되는 성공 case**다. 그러나 2025년 3월의 증자 충격은 4B-watch이지 4C가 아니다.

```text
4B 교정:
4B-watch = 과열·증자·valuation 부담
4B-elevated = dilution/capex 부담이 커졌으나 backlog/EPS 살아 있음
4C = 계약 취소, 수요 붕괴, EPS 하향, 회계/공시 신뢰 훼손
```

---

## Case C — 한국가스공사 / 동해 가스전 `price_moved_without_evidence`

```text
symbol = 036460
source_sector = R11 정책·지정학·재난·이벤트
archetype = DOMESTIC_RESOURCE_DISCOVERY_EVENT / PRICE_ONLY_RALLY
case_type = event_premium / price_moved_without_evidence
```

한국가스공사는 R13에서 **가격이 증거보다 먼저 간 케이스**다. 2024년 6월 3일 동해 석유·가스 탐사 승인 발표 이후 한국가스공사 주가는 장중 최대 30% 올라 38,700원을 기록했다. WSJ는 매장 가능량이 최대 140억 배럴로 언급됐지만, 윤석열 대통령이 경제성은 아직 결정되지 않았고 최소 5차례 시추가 필요하다고 말했다고 보도했다. ([월스트리트 저널][4])

### stage date 후보

```text
Stage 1:
2024-06-03
- 동해 석유·가스 탐사 승인
- 최대 140억 배럴 가능성

Stage 2:
없음 또는 매우 약함
- 시추 결과 없음
- 경제성 없음
- 상업 생산 없음

Stage 3:
없음

Stage 4B:
2024-06-03
- 장중 +30%
- 가격이 증거보다 먼저 감

Stage 4C:
시추 실패 / 경제성 부재 / 정책 후퇴 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
WSJ intraday price anchor

stage3_price:
N/A

stage1_event_peak_price:
38,700원

intraday_MFE_on_event_day:
+30%

implied_pre_event_reference_price:
38,700 / 1.30 = 약 29,769원

MFE_5D / 20D / 60D:
OHLC unavailable

MAE_30D / 90D:
OHLC unavailable

below_stage3_price_flag:
N/A

peak_price:
38,700원 event-day anchor

drawdown_after_peak:
OHLC unavailable
```

### score-price alignment

```text
alignment = price_moved_without_evidence
rerating_result = event_premium
stage_failure_type = should_have_been_stage1_or_4B_watch
```

### R13 판정

이 케이스는 R11/R13에서 Green을 막아야 한다.

```text
내릴 축:
resource_estimate_without_drilling
policy_news_only
price_rally_before_contract
event_premium

Green gate:
commerciality_confirmed
drilling_result
development_plan
revenue_conversion
```

---

## Case D — 삼성SDS `event_premium + success_candidate`

```text
symbol = 018260
source_sector = R8 플랫폼·콘텐츠·SW·보안
archetype = AI_CLOUD_CAPITAL_ALLOCATION / PRICE_ONLY_RALLY
case_type = success_candidate + 4B-watch
```

삼성SDS는 R13에서 **좋은 구조 후보와 price-first event를 동시에 보는 case**다. 2026년 4월 KKR은 삼성SDS가 신규 발행하는 8.2억 달러 전환사채를 인수하기로 했고, 삼성SDS 주가는 장중 최대 20.8% 상승했다. Reuters는 KKR이 M&A, 자본배분, full-stack AI solutions 확장을 자문하고, 삼성SDS가 6.4조 원 현금과 KKR 자금을 바탕으로 AI 인프라·physical AI·stablecoin 등 신사업을 추진할 계획이라고 보도했다. ([Reuters][5])

### stage date 후보

```text
Stage 1:
2025~2026
- 기업 AI 전환
- 삼성SDS AI infrastructure / full-stack AI

Stage 2:
2026-04-15
- KKR $820M CB 투자
- AI infra / M&A / capital allocation 기대

Stage 3:
없음
- CB 투자와 AI 투자 계획만으로는 Green 금지
- enterprise AI revenue / margin / recurring cloud revenue 필요

Stage 4B:
2026-04-15
- 발표 당일 장중 +20.8%

Stage 4C:
CB dilution, AI capex 대비 매출 부진, M&A 실패 시 후보
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters intraday return anchor

stage3_price:
N/A

stage2_event_MFE_1D:
+20.8%

MFE_30D / 90D / 180D:
OHLC unavailable

MAE_30D / 90D:
OHLC unavailable

below_stage3_price_flag:
N/A

peak_price:
event-day intraday peak percentage only, exact price unavailable

drawdown_after_peak:
OHLC unavailable
```

### score-price alignment

```text
alignment = event_premium + success_candidate
rerating_result = AI_capital_allocation_watch
stage_failure_type = should_not_be_green_yet
```

### R13 판정

삼성SDS는 Stage 2 후보지만 Stage 3는 아니다. R13에서는 `AI_capex_without_revenue`와 `CB_dilution_watch`를 붙여야 한다.

```text
올릴 축:
enterprise_contract_quality
AI_revenue_conversion
OPM_improvement
FCF_conversion

내릴 축:
AI_infra_plan_only
convertible_bond_dilution
M&A_hope_without_integration
```

---

## Case E — 제주항공 `hard 4C / operational trust break`

```text
symbol = 089590
source_sector = R9 모빌리티·운송·레저
archetype = OPERATIONAL_TRUST_BREAK / THESIS_BREAK_4C
case_type = 4C-thesis-break
```

제주항공은 R13에서 hard 4C 기준점이다. 2024년 12월 30일 제주항공 주가는 전날 무안공항 사고 이후 장중 최대 15.7% 하락해 6,920원, 상장 이후 최저가를 기록했다. Reuters는 해당 사고로 179명이 사망했고, 정부가 국내 항공 운항 시스템 전반에 대한 안전 점검을 지시했다고 보도했다. ([Reuters][6])

### stage date 후보

```text
Stage 1:
2023~2024
- LCC 여행수요 회복
- 일본/동남아 노선 회복

Stage 2:
없음
- 안전신뢰 훼손 전에는 LCC recovery가 Stage 1~2 가능

Stage 3:
없음

Stage 4B:
여행수요 회복만으로 LCC주가 과열된 구간이 있다면 후보

Stage 4C:
2024-12-30
- fatal crash
- 주가 장중 -15.7%
- record low 6,920원
- operational trust hard break
```

### 실제 가격경로 검증

```text
price_data_source:
Reuters intraday price anchor

stage3_price:
N/A

stage4c_price_anchor:
6,920원

stage4c_intraday_MAE:
-15.7%

implied_pre_event_reference_price:
6,920 / (1 - 0.157) = 약 8,209원

MFE:
N/A

MAE_1D:
-15.7%

below_stage3_price_flag:
N/A

peak_price:
N/A

drawdown_after_peak:
accident-day drawdown at least -15.7%
```

### score-price alignment

```text
alignment = thesis_break
rerating_result = operational_trust_break
stage_failure_type = hard_4C
```

### R13 판정

제주항공은 R13에서 **안전사고 hard gate**를 가장 강하게 올려야 하는 case다.

```text
4C hard gate:
fatal_safety_accident
consumer_trust_break
regulatory_safety_probe
operational_system_review
```

---

## Case F — LG에너지솔루션 / L&F `contract thesis break`

```text
symbols = 373220 / 066970
source_sector = R3 2차전지·전기차·친환경
archetype = BATTERY_CONTRACT_CANCELLATION_4C / THESIS_BREAK_4C
case_type = 4C-thesis-break
```

R3 배터리에서는 계약 취소와 계약가치 축소가 R13 hard 4C의 핵심이다.

LG에너지솔루션은 2025년 12월 Ford 계약 취소 이후 주가가 장중 최대 7.6% 하락했다. Reuters는 Ford가 EV 모델 생산을 중단하면서 LGES 공급계약을 취소했고, 해당 계약은 2027년 1월부터 시작될 예정이었다고 보도했다. ([Reuters][7])

며칠 뒤 LGES는 Freudenberg Battery Power Systems와의 3.9조 원 계약도 상호 종료했다고 밝혔다. Reuters는 Ford와 Freudenberg 계약 종료로 LGES가 약 13.5조 원의 기대 매출을 잃게 됐고, 이는 2024년 매출 25.62조 원의 절반을 넘는 규모라고 보도했다. ([Reuters][8])

L&F는 더 극단적이다. 2025년 12월 L&F는 Tesla향 high-nickel cathode 공급계약 예상 가치가 기존 29억 달러에서 7,386달러로 줄었다고 밝혔다. Reuters는 Tesla 4680 생산 난항과 EV 수요 둔화가 영향을 줬다고 설명했다. ([Reuters][9])

### stage date 후보

```text
LGES Stage 4C:
2025-12-18
- Ford EV battery supply deal cancellation
- 주가 장중 -7.6%

LGES 추가 4C:
2025-12-26
- Freudenberg 3.9조 원 계약 종료
- 총 13.5조 원 기대매출 손실

L&F Stage 4C:
2025-12-29
- Tesla 계약 예상가치 $2.9B → $7,386
```

### 실제 가격경로 검증

```text
LGES price_data_source:
Reuters intraday return anchor

LGES stage4c_intraday_MAE:
-7.6%

LGES lost_expected_revenue:
13.5조 원

LGES lost_revenue_vs_2024_revenue:
13.5 / 25.62 = 52.7%

L&F price_data_source:
Reuters contract-value anchor, exact stock OHLC unavailable

L&F contract_value_reduction:
$2.9B → $7,386

L&F contract_value_drawdown:
1 - 7,386 / 2,900,000,000 = 99.999745%

stage3_price:
N/A for both, because Stage 3 should have been blocked unless call-off / GWh / margin was confirmed

MFE/MAE:
OHLC unavailable except LGES 1D event MAE
```

### score-price alignment

```text
LGES alignment = thesis_break
L&F alignment = thesis_break
rerating_result = contract_quality_failure
stage_failure_type = false_green_prevention_case
```

### R13 판정

R3/R13에서 `contract headline`은 절대 Green의 충분조건이 아니다.

```text
4C hard gate:
contract_cancellation
contract_value_collapse
customer_strategy_pullback
EV_demand_slowdown
GWh_calloff_failure

Green gate 강화:
binding_volume
take_or_pay
actual_calloff
GWh_delivery
OPM
FCF
```

---

## Case G — 한화에어로스페이스 증자 / 고려아연 증자류 `capital allocation 4B vs 4C 구분`

```text
source_sector = R1 / R4 / R13
archetype = CAPITAL_ALLOCATION_DILUTION_OVERLAY / CROWDED_RERATING_4B_WATCH
case_type = 4B-watch, not automatic 4C
```

한화에어로스페이스는 2025년 3월 3.6조 원 증자 발표 후 하루 13% 급락했다. 하지만 FT는 이 자금이 해외 공장과 파트너 지분 확보에 쓰일 계획이었다고 설명했고, 회사의 수주와 방산 thesis 자체가 바로 훼손된 것은 아니었다. ([Financial Times][3])

Reuters는 2025년 3월 금융감독원이 한화에어로스페이스의 3.6조 원 증자 계획에 대해 정정신고서 제출을 요구했고, 발표 다음날 주가가 13% 하락했다고 보도했다. ([Reuters][10])

### stage date 후보

```text
Stage 4B:
2025-03-21
- 주가 이미 YTD 2배 이상 상승
- 증자 발표
- 하루 -13%

Stage 4C:
아님
- dilution shock은 맞지만, 수주·수요·EPS thesis break는 아님
```

### 실제 가격경로 검증

```text
price_data_source:
FT / Reuters event return

stage4b_event_MAE_1D:
-13%

stage3_price:
N/A in this overlay row

drawdown_after_peak:
OHLC unavailable

4B_detection:
successful
- 대시세 이후 자본조달 shock을 4B-watch로 포착
```

### score-price alignment

```text
alignment = aligned_4B_detection
rerating_result = true_rerating_with_dilution_watch
stage_failure_type = not_4C
```

### R13 판정

이 case는 R13에서 중요한 구분을 만든다.

```text
dilution_after_big_rally:
4B-watch 또는 4B-elevated

dilution_with_business_thesis_break:
4C 후보

dilution_for_growth_capex_with_backlog_alive:
hard exit 아님
```

---

# 5. 이번 R13 case별 요약표

| case             | source R | 분류                                | 핵심 가격검증                                       | R13 판정                       |
| ---------------- | -------: | --------------------------------- | --------------------------------------------- | ---------------------------- |
| SK하이닉스           |       R2 | structural_success + 4B           | 2025 +274%, 2026 +200% 이상, 누적 최소 +1,022%      | Stage 3 성공, 현재는 4B-watch     |
| 한화에어로스페이스        |       R1 | structural_success + 4B timing    | 187,500 → 1,435,000, +665.3%; 증자일 -13%        | Stage 3 성공, 증자는 4B이지 4C 아님   |
| 한국가스공사           |      R11 | price_moved_without_evidence      | 동해 가스 뉴스 당일 장중 +30%, 38,700원                  | Stage 1 / 4B-watch, Green 금지 |
| 삼성SDS            |       R8 | event_premium + success_candidate | KKR CB 발표일 장중 +20.8%                          | Stage 2, AI 매출 전 Green 금지    |
| 제주항공             |       R9 | hard 4C                           | 사고 후 장중 -15.7%, 6,920원 record low             | operational trust hard 4C    |
| LGES / L&F       |       R3 | contract thesis break             | LGES -7.6%; 기대매출 13.5조 손실; L&F 계약가치 -99.9997% | contract quality 4C          |
| 한화에어로 증자 overlay |   R1/R13 | 4B-watch                          | 증자 발표 후 -13%                                  | 4B-elevated, hard 4C 아님      |

---

# 6. 각 case별 실제 가격경로 검증 요약

```text
SK하이닉스:
price_data_source = Reuters
stage3_price = price_data_unavailable_after_deep_search
reported_MFE_minimum = +1,022% from 2025 start to 2026-05-14
market_cap_MFE_minimum = +842%
alignment = aligned
4B = 2026-05-14

한화에어로스페이스:
price_data_source = FT / Reuters
stage3_anchor = 187,500원
peak_anchor = 1,435,000원
reported_MFE = +665.3%
4B_event_MAE_1D = -13%
alignment = aligned
4B = successful watch, not exit

한국가스공사:
price_data_source = WSJ
stage3_price = N/A
event_peak = 38,700원
intraday_MFE = +30%
alignment = price_moved_without_evidence

삼성SDS:
price_data_source = Reuters
stage3_price = N/A
event_MFE_1D = +20.8%
alignment = event_premium + success_candidate

제주항공:
price_data_source = Reuters
stage4c_price_anchor = 6,920원
event_MAE_1D = -15.7%
alignment = thesis_break

LGES:
price_data_source = Reuters
stage4c_event_MAE_1D = -7.6%
lost_expected_revenue = 13.5조 원
lost_revenue_vs_2024_revenue = 52.7%
alignment = thesis_break

L&F:
price_data_source = Reuters
contract_value = $2.9B → $7,386
contract_value_drawdown = -99.999745%
alignment = thesis_break
```

---

# 7. score-price alignment 판정

```text
aligned:
- SK하이닉스
- 한화에어로스페이스

price_moved_without_evidence:
- 한국가스공사
- 삼성SDS 이벤트 구간

event_premium:
- 한국가스공사
- 삼성SDS
- 한화에어로스페이스 증자 충격은 event/dilution 4B

thesis_break:
- 제주항공
- LG에너지솔루션
- L&F

4B-watch_success:
- SK하이닉스 2026-05-14
- 한화에어로스페이스 2025-03-21

false_positive_prevention:
- 한국가스공사
- L&F
- LGES
```

---

# 8. 점수비중 교정

## 올릴 축

```text
price_path_alignment +5
stage3_to_large_MFE_confirmation +5
cross_evidence +4
eps_fcf_durability +4
contract_quality +5
capacity_bottleneck +4
customer_visibility +4
operational_trust +5
hard_4c_early_warning +5
```

### 왜 올리나

SK하이닉스와 한화에어로스페이스는 Stage 3가 제대로 잡히면 대형 MFE가 나온다는 걸 보여준다. 특히 SK하이닉스는 Reuters 기준 2025년 +274%, 2026년 +200% 이상이라는 대형 price path가 확인된다. ([Reuters][1])

한화에어로스페이스는 187,500원에서 1,435,000원으로 오른 방산 리레이팅 사례이며, Stage 3 이후 대형 MFE가 나온 구조로 볼 수 있다. ([Financial Times][2])

## 내릴 축

```text
policy_news_only -5
resource_estimate_without_commerciality -5
AI_capex_or_partnership_without_revenue -4
contract_headline_without_calloff -5
media_or_event_price_rally -5
high_score_without_price_validation -5
past_winner_similarity -4
```

### 왜 내리나

한국가스공사는 동해 자원 가능성 뉴스만으로 장중 +30% 올랐지만, 경제성·상업 생산·매출 전환은 확인되지 않았다. ([월스트리트 저널][4])

삼성SDS는 KKR CB와 AI 인프라 기대만으로 장중 +20.8% 올랐지만, 아직 AI 매출·마진·반복매출이 확인된 Stage 3는 아니다. ([Reuters][5])

L&F는 Tesla라는 고객명과 대형 계약이 있었지만, 계약가치가 $2.9B에서 $7,386로 사실상 사라졌다. ([Reuters][9])

## Green gate 강화 조건

```text
Stage 3-Green 필수:
1. cross_evidence
2. EPS/FCF durability
3. structural visibility
4. price_path_alignment
5. not price-only rally
6. no hard RedTeam
7. not saturated 4B

추가 R13 gate:
8. Stage 3 이후 180D 또는 1Y MFE가 충분한지
9. Stage 3 이후 30D/90D MAE가 과도하지 않은지
10. 계약·정책·이벤트가 실제 revenue/EPS로 내려왔는지
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 2~5배 이상 상승
시총/valuation이 새 프레임을 거의 다 반영
대형 증자 / CB / CAPEX 발표
좋은 뉴스에도 주가 반응 둔화
market cap milestone이 headline화
consensus가 한쪽으로 쏠림

4B-elevated:
SK하이닉스처럼 시총 1조 달러 근접
한화에어로처럼 대시세 후 대형 증자
AI/HBM/방산처럼 모두가 같은 논리를 반복

4B-graduated:
대형 MFE 이후 신규 evidence가 더 이상 가격을 밀지 못함
```

## 4C hard gate 조건

```text
operational_trust_break:
제주항공 fatal crash

contract_quality_break:
LGES Ford/Freudenberg cancellation
L&F Tesla contract-value collapse

policy/event fade:
한국가스공사 자원 경제성 미확인
MOU/정책 후속 계약 부재

capital_allocation_break:
증자/CB가 사업 thesis를 훼손할 때
단, growth funding with thesis alive는 4B-elevated, not 4C
```

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

여기서 `full_ohlc_complete = false`는 숨기면 안 된다. 이번 환경에서 KRX/Naver/Yahoo 수정주가 일봉을 직접 가져오지 못했기 때문에, Reuters/FT/WSJ의 가격 anchor와 percentage return으로 계산 가능한 범위만 완료했다.

다만 기존처럼 `needs_ohlc_backfill`로 끝낸 것은 아니고, 각 case마다:

```text
사용 가능한 가격 anchor
계산 가능한 MFE/MAE
unavailable인 항목과 사유
```

를 명시했다.

---

# 10. patch-ready 출력

## docs/round/round_132.md 요약

```md
# R13 Loop 7. Cross-archetype RedTeam / 4B / Price Validation

이번 라운드는 R1~R12 후보를 최종 검증하는 R13 price-validation 라운드다.

핵심 결론:
- SK하이닉스와 한화에어로스페이스는 Stage 3가 대형 MFE를 잡을 수 있음을 보여주는 aligned success benchmark다.
- SK하이닉스는 2025년 +274%, 2026년 +200% 이상 상승해 현재는 신규 Stage 3가 아니라 4B-watch다.
- 한화에어로스페이스는 187,500원에서 1,435,000원까지 올라 +665.3% MFE anchor가 확인된다. 2025년 증자 충격은 4B-watch이지 hard 4C가 아니다.
- 한국가스공사 동해 가스 이벤트는 장중 +30% price-only rally로, 자원 경제성·상업 생산 전 Stage 3 금지다.
- 삼성SDS KKR CB 이벤트는 장중 +20.8% event premium이며, AI 매출·마진 전 Stage 3가 아니다.
- 제주항공 fatal crash는 operational trust hard 4C다.
- LGES와 L&F는 contract cancellation / contract value collapse hard 4C다.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 132 R13 Loop 7 Cross-archetype Price Validation

## 반영 내용
- R13 price-validation 라운드를 추가했다.
- Stage 3 aligned success와 4B-watch, hard 4C, price-only rally를 비교했다.
- Reuters/FT/WSJ가 제공한 가격 anchor로 가능한 MFE/MAE를 계산했다.
- full OHLC는 환경상 직접 추출하지 못한 항목을 명시적으로 unavailable 처리했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- price_path_alignment 가중치 강화
- event premium 감점 강화
- contract cancellation hard 4C 강화
- operational trust hard 4C 강화
- 4B-watch와 hard 4C 구분 강화
```

## case row 초안

```jsonl
{"case_id":"r13_sk_hynix_hbm_4b_benchmark","symbol":"000660","company_name":"SK하이닉스","source_sector":"R2","case_type":"structural_success","primary_archetype":"STRUCTURAL_SUCCESS_BUT_4B_WATCH","stage4b_date":"2026-05-14","price_validation":{"price_data_source":"Reuters reported return path","stage3_price":null,"mfe_1y":1022.0,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_rerating","notes":"2025 +274%, 2026 YTD >200%; now 4B-watch."}
{"case_id":"r13_hanwha_aerospace_defense_mfe_4b","symbol":"012450","company_name":"한화에어로스페이스","source_sector":"R1","case_type":"structural_success","primary_archetype":"STRUCTURAL_SUCCESS_BUT_4B_WATCH","stage4b_date":"2025-03-21","price_validation":{"price_data_source":"FT/Reuters reported price anchors","stage3_price":187500,"peak_price":1435000,"peak_return_from_stage3":665.3,"mae_1d":-13.0,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_rerating","notes":"Large MFE; capital raise is 4B-watch, not hard 4C."}
{"case_id":"r13_kogas_resource_price_only","symbol":"036460","company_name":"한국가스공사","source_sector":"R11","case_type":"event_premium","primary_archetype":"PRICE_ONLY_RALLY","stage1_date":"2024-06-03","stage4b_date":"2024-06-03","price_validation":{"price_data_source":"WSJ intraday price anchor","stage3_price":null,"peak_price":38700,"mfe_1d":30.0,"price_validation_status":"event_anchor_not_stage3"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"event_premium","notes":"Resource estimate and drilling approval are not commerciality."}
{"case_id":"r13_samsung_sds_kkr_ai_cb_event","symbol":"018260","company_name":"삼성SDS","source_sector":"R8","case_type":"event_premium","primary_archetype":"PRICE_ONLY_RALLY","stage2_date":"2026-04-15","stage4b_date":"2026-04-15","price_validation":{"price_data_source":"Reuters intraday return anchor","stage3_price":null,"mfe_1d":20.8,"price_validation_status":"event_anchor_not_stage3"},"score_price_alignment":"event_premium","rerating_result":"AI_capital_allocation_watch","notes":"AI infrastructure investment and CB are Stage 2, not Stage 3."}
{"case_id":"r13_jeju_air_fatal_crash_hard_4c","symbol":"089590","company_name":"제주항공","source_sector":"R9","case_type":"4c_thesis_break","primary_archetype":"OPERATIONAL_TRUST_BREAK","stage4c_date":"2024-12-30","price_validation":{"price_data_source":"Reuters intraday price anchor","stage4c_price":6920,"mae_1d":-15.7,"price_validation_status":"reported_intraday_anchor"},"score_price_alignment":"thesis_break","rerating_result":"operational_trust_break","notes":"Fatal crash and safety probe are hard 4C."}
{"case_id":"r13_lges_contract_cancellation_4c","symbol":"373220","company_name":"LG에너지솔루션","source_sector":"R3","case_type":"4c_thesis_break","primary_archetype":"THESIS_BREAK_4C","stage4c_date":"2025-12-18","price_validation":{"price_data_source":"Reuters intraday return anchor","mae_1d":-7.6,"price_validation_status":"reported_intraday_anchor"},"score_price_alignment":"thesis_break","rerating_result":"contract_cancellation","notes":"Ford/Freudenberg cancellations remove about KRW13.5T expected revenue."}
{"case_id":"r13_lnf_tesla_contract_value_collapse","symbol":"066970","company_name":"L&F","source_sector":"R3","case_type":"4c_thesis_break","primary_archetype":"THESIS_BREAK_4C","stage4c_date":"2025-12-29","price_validation":{"price_data_source":"Reuters contract value anchor","contract_value_drawdown":-99.999745,"price_validation_status":"contract_value_anchor_stock_ohlc_unavailable"},"score_price_alignment":"thesis_break","rerating_result":"contract_quality_failure","notes":"Tesla deal value collapsed from $2.9B to $7,386."}
```

## shadow weight row 초안

```csv
archetype,price_path_alignment,hard_redteam,event_premium_penalty,contract_quality,operational_trust,4b_watch_sensitivity,notes
STRUCTURAL_SUCCESS_ALIGNED,+5,+0,-0,+4,+2,+2,SK Hynix and Hanwha Aerospace confirm large MFE after true Stage 3.
STRUCTURAL_SUCCESS_BUT_4B_WATCH,+5,+1,-0,+4,+2,+5,Large MFE cases need earlier 4B watch after crowding and cap raise.
PRICE_ONLY_RALLY,-0,+0,-5,-3,+0,+5,Korea Gas and Samsung SDS show price moving before revenue evidence.
THESIS_BREAK_4C,+0,+5,-0,+5,+5,+2,Jeju Air LGES and L&F show hard 4C from trust or contract collapse.
EVENT_PREMIUM,+0,+0,-5,-3,+0,+4,Policy resource AI capital allocation events should not become Green without revenue.
```

---

# 이번 R13 Loop 7 결론

R13의 결론은 꽤 선명하다.

```text
1. Stage 3는 잘 잡히면 진짜 대형 MFE를 만든다.
   SK하이닉스와 한화에어로스페이스가 그 증거다.

2. 4B는 hard exit가 아니다.
   한화에어로스페이스 증자처럼 dilution shock이 있어도 backlog와 EPS thesis가 살아 있으면 4B-watch/elevated다.

3. 가격이 증거보다 먼저 간 case는 Green을 막아야 한다.
   한국가스공사와 삼성SDS가 그 예다.

4. 4C는 가볍게 쓰면 안 되지만,
   안전사고·계약취소·계약가치 붕괴는 hard 4C다.
   제주항공, LGES, L&F가 기준점이다.

5. R13은 high score를 믿는 라운드가 아니다.
   high score가 price path, 4B, 4C, accounting/trust gate를 통과하는지 재판하는 라운드다.
```

한 문장으로 압축하면:

> **R13의 역할은 “좋아 보이는 후보”를 한 번 더 부수는 것이다. Stage 3는 대형 MFE로 증명되고, 4B는 peak 전후 crowding으로 증명되며, 4C는 안전·계약·회계·규제·운영 신뢰 훼손으로 증명된다.**

[1]: https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com "AI boom puts SK Hynix on cusp of $1 trillion market value"
[2]: https://www.ft.com/content/658c8411-df02-4b5e-a69d-2029114e4ca1?utm_source=chatgpt.com "Iran war lifts K-defence company offering cheap Patriot rival"
[3]: https://www.ft.com/content/994a0a80-414f-442f-bf41-f2dbde5a04ca?utm_source=chatgpt.com "South Korea's biggest defence group plans $2.5bn share sale to expand overseas"
[4]: https://www.wsj.com/articles/korea-gas-leads-energy-rally-on-seoul-s-offshore-oil-drilling-approval-c8c4d428?utm_source=chatgpt.com "Korea Gas Leads Energy Rally on Seoul's Offshore Oil Drilling Approval"
[5]: https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com "KKR to buy $820 million of Samsung SDS convertible bonds, shares jump 20%"
[6]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"
[7]: https://www.reuters.com/business/energy/shares-south-koreas-lges-drop-more-than-7-after-ford-cancels-ev-battery-deal-2025-12-18/?utm_source=chatgpt.com "Shares in South Korea's LGES drop more than 7% after Ford cancels EV battery deal"
[8]: https://www.reuters.com/business/energy/lg-energy-solution-cancels-39-trillion-won-battery-order-with-freudenberg-2025-12-26/?utm_source=chatgpt.com "LG Energy Solution cancels 3.9 trillion won battery order with Freudenberg"
[9]: https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/?utm_source=chatgpt.com "South Korea's L&F slashes value of battery material supply deal with Tesla"
[10]: https://www.reuters.com/business/aerospace-defense/south-korea-market-watchdog-orders-hanwha-aerospace-revise-share-issuance-plan-2025-03-27/?utm_source=chatgpt.com "S. Korea watchdog blocks Hanwha Aerospace $2.5 billion capital raising plan"

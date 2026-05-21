순서상 이번은 **R13 Loop 9 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리**다.

이번 R13은 새 섹터가 아니라, **R1~R12 Loop 9에서 나온 후보를 다시 부수는 라운드**다. 특히 이번에는 “Stage 3가 실제 대형 MFE를 만들었는가”, “4B가 과열을 너무 늦지 않게 잡았는가”, “4C가 thesis break를 제대로 차단했는가”, “정책·이벤트 가격상승을 Green으로 착각하지 않았는가”를 한 번에 검증한다.

```text
round = R13 Loop 9
round_id = round_158
large_sector = CROSS_ARCHETYPE_REDTEAM_PRICE_VALIDATION
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
```

이번 환경에서는 KRX/Naver/Yahoo/Stooq 원시 수정주가 일봉 OHLC를 안정적으로 직접 확보하지 못했다. 그래서 Reuters / MarketWatch / FT / WSJ / Business Insider / Vogue 등에서 확인되는 **가격 anchor, 이벤트 수익률, 시총, 계약가치, 손실·보상비용 지표**만 계산했고, 원시 OHLC가 없는 구간은 `price_data_unavailable_after_deep_search`로 표시했다.

---

# 1. 이번 라운드 대섹터

```text
R13 = Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리
```

R13의 핵심 질문은 이거다.

```text
Stage 3가 대형 MFE로 증명됐나?
4B가 가격 선반영·crowding·event premium을 잘 잡았나?
4C가 계약·안전·보안·운영신뢰 훼손을 잘 차단했나?
```

---

# 2. 대상 canonical archetype

```text
STRUCTURAL_SUCCESS_ALIGNED
STRUCTURAL_SUCCESS_BUT_4B_WATCH
CROWDED_RERATING_4B_WATCH
PRICE_MOVED_WITHOUT_EVIDENCE
EVENT_PREMIUM
FALSE_POSITIVE_SCORE
EVIDENCE_GOOD_BUT_PRICE_FAILED
CONTRACT_QUALITY_BREAK
OPERATIONAL_TRUST_BREAK
SECURITY_PRIVACY_TRUST_BREAK
POLICY_INDUCED_CAPEX_FAILURE
POLICY_RESOURCE_EVENT_PREMIUM
DIGITAL_ASSET_POLICY_OVERHEAT
```

---

# 3. deep sub-archetype

```text
성공 검증:
- SK Hynix HBM / HBM4 / AI memory
- APR / Medicube K-beauty device
- Stage 3 이후 대형 MFE

4B 검증:
- SK Hynix market-cap milestone
- APR valuation crowding
- Samsung SDS KKR / AI capital allocation event
- stablecoin policy basket
- Korea Gas resource discovery event

4C 검증:
- LGES / L&F contract-quality break
- Jeju Air operational safety break
- SK Telecom cybersecurity trust break
- Hyundai Steel policy-induced capex failure

false Green 방지:
- 정책지원
- 자원발견 가능성
- 스테이블코인 정책
- M&A/CB/IPO 이벤트
- CAPEX headline
```

---

# 4. 국장 신규 후보 case

## Case A — SK하이닉스 `structural_success_aligned + 4B-watch`

```text
symbol = 000660
source_sector = R2
case_type = structural_success + 4B-watch
archetype = MEMORY_HBM_CAPACITY / STRUCTURAL_SUCCESS_BUT_4B_WATCH
```

### stage date

```text
Stage 1:
2024년 상반기
- AI server / HBM demand
- old commodity memory frame break

Stage 2:
2024-06-25
- Nomura가 2024 OP 30조 원, 2025 OP 53조 원으로 상향
- HBM dominance + DRAM price upcycle + EPS revision
- price anchor = 222,000원

Stage 3:
2024-06-25 후보
- HBM 지배력
- 메모리 가격 상승
- EPS revision
- AI server capacity bottleneck

Stage 4B:
2026-05-04
- AI capex 상향 기대에 1,447,000원 record high

추가 4B:
2026-05-14
- 2025년 +274%
- 2026년 +200% 이상
- market cap 약 $942B
- 1조 달러 근접
```

SK하이닉스는 R13에서 **Stage 3가 실제 대형 MFE를 만들 수 있음을 증명한 기준점**이다. 2024년 6월 Nomura가 HBM 지배력과 메모리 가격 상승을 이유로 영업이익 추정치를 크게 올렸고, 당시 주가 anchor는 222,000원이었다. 이후 2026년 5월에는 AI capex 기대에 1,447,000원 record high를 찍었고, Reuters는 SK하이닉스가 2025년에 274%, 2026년에 200% 넘게 상승하며 시총 약 9,420억 달러에 도달했다고 보도했다. ([마켓워치][1])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / Reuters reported price and return anchors

entry_date:
2024-06-25

stage3_price:
222,000원

reported_peak_price:
1,447,000원

MFE_from_stage3_to_reported_peak:
(1,447,000 / 222,000) - 1
= +551.8%

reported_return_2025:
+274%

reported_return_2026_to_2026-05-14:
> +200%

minimum_compounded_return_from_start_2025_to_2026-05-14:
(1 + 2.74) * (1 + 2.00) - 1
= +1,022% 이상

market_cap_path:
< $100B → 약 $942B

minimum_market_cap_MFE:
(942 / 100) - 1
= +842% 이상

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

below_stage3_price_flag:
price_data_unavailable_after_deep_search

drawdown_after_peak:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = aligned
rerating_result = true_rerating
4B_status = 4B-watch / 4B-elevated
```

SK하이닉스는 Stage 3 성공 benchmark다. 다만 지금은 신규 Stage 3가 아니라 **4B-watch / crowding watch**다.

---

## Case B — APR / Medicube `structural_success_aligned + 4B-watch`

```text
symbol = 278470
source_sector = R5
case_type = structural_success + 4B-watch
archetype = K_BEAUTY_DEVICE_GLOBAL_BRAND / STRUCTURAL_SUCCESS_BUT_4B_WATCH
```

### stage date

```text
Stage 1:
2024 IPO / 2025 K-beauty device virality
- Medicube beauty device
- TikTok / creator affiliate / U.S. beauty-tech demand

Stage 2:
2025-07-08
- APR stock 158,300원
- IPO 이후 +75% 이상
- market cap 약 $4.2B

Stage 3:
2025 Q4 후보
- Q4 revenue 약 $440M, +124% YoY
- overseas revenue 약 $362M, +203% YoY
- full-year revenue 약 $1.2B
- Medicube revenue 약 $1.1B

Stage 4B:
2025~2026
- market cap $4.2B
- overseas revenue growth와 valuation crowding 동시 발생
```

APR/Medicube는 R5에서 **viral이 매출로 내려온 드문 구조 후보**다. Business Insider는 APR 주가가 IPO 이후 75% 넘게 올라 158,300원에 거래됐고 시총이 약 42억 달러라고 보도했다. Vogue Business는 2025년 4분기 APR 매출이 약 4.4억 달러로 전년 대비 124% 늘고, 해외 매출은 203% 증가해 약 3.62억 달러가 됐다고 정리했다. 다만 Medicube가 전체 매출의 대부분을 차지하므로, single-brand/device concentration과 4B를 같이 붙인다. ([Business Insider][2])

### 실제 가격경로 검증

```text
price_data_source:
Business Insider / Vogue Business anchors

stage2_price:
158,300원

implied_IPO_reference_price_from_75pct_gain:
158,300 / 1.75
= 약 90,457원 이하

IPO_to_stage2_MFE_minimum:
> +75%

market_cap_July_2025:
$4.2B

Q4_2025_revenue:
$440M

Q4_2025_revenue_growth:
+124% YoY

Q4_2025_overseas_revenue:
$362M

Q4_2025_overseas_growth:
+203% YoY

FY_2025_revenue:
$1.2B

Medicube_FY_2025_revenue:
$1.1B

Medicube_share_of_APR_revenue:
1.1 / 1.2
= 91.7%

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = aligned
rerating_result = K_beauty_device_true_rerating_plus_4B_watch
stage_failure_type = green_success_candidate
```

APR은 R5의 좋은 Stage 3 후보지만, **매출 집중도와 이미 큰 주가상승 때문에 4B-watch가 필요하다.**

---

## Case C — 삼성SDS `4B-watch / AI capital allocation event`

```text
symbol = 018260
source_sector = R8
case_type = event_premium + success_candidate
archetype = AI_CLOUD_CAPITAL_ALLOCATION / CROWDED_RERATING_4B_WATCH
```

### stage date

```text
Stage 1:
2025~2026
- enterprise AI transformation
- Samsung group AI infra / IT services 기대

Stage 2:
2026-04-15
- KKR이 삼성SDS 신규 CB $820M 인수
- M&A / AI infra / capital allocation 기대
- 기존 현금 6.4조 원 + KKR funding

Stage 3:
없음
- CB 투자와 AI 투자계획만으로 Green 금지
- enterprise AI 계약, recurring cloud revenue, AI transformation revenue, margin, FCF 확인 필요

Stage 4B:
2026-04-15
- 장중 +20.8%
- KOSPI +3.0% 대비 강한 아웃퍼폼
```

삼성SDS는 KKR의 8.2억 달러 CB 투자와 AI/M&A 자본배분 기대만으로 장중 20.8% 급등했다. Reuters는 삼성SDS가 기존 현금 6.4조 원과 KKR 자금을 활용해 AI infrastructure, physical AI, stablecoin 등 신사업을 추진한다고 전했다. 이건 좋은 Stage 2 후보이지만, **AI 매출 전 +20.8%는 바로 4B-watch**다. ([Reuters][3])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event return anchor

stage3_price:
N/A

stage2_event_MFE_1D:
+20.8%

morning_trade_return:
+19.4%

KOSPI_same_context_return:
+3.0%

relative_intraday_outperformance_vs_KOSPI:
20.8 - 3.0
= +17.8pp

CB_investment:
$820M

KRW_equivalent_at_Reuters_FX_1472:
820M * 1,472
= 약 1.207T won

Samsung_SDS_existing_cash:
6.4T won

combined_cash_plus_CB:
6.4T + 1.207T
= 약 7.607T won

MFE_30D / 90D:
price_data_unavailable_after_deep_search

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = event_premium + success_candidate
rerating_result = AI_cloud_capital_allocation_watch
stage_failure_type = should_not_be_green_yet
```

삼성SDS는 R8에서 **Stage 2 + 4B-watch**다. AI revenue conversion 전 Stage 3는 금지다.

---

## Case D — 현대제철 U.S. CAPEX `false_positive_score prevention / policy-induced capex failure`

```text
symbol = 004020
source_sector = R4 / R11
case_type = failed_rerating / false_positive_score_prevention
archetype = POLICY_INDUCED_CAPEX_FAILURE
```

### stage date

```text
Stage 1:
2025-03
- U.S. tariff pressure
- Korean steel exporter seeks U.S. local investment

Stage 2:
약함
- $5.8B~$6B U.S. steel plant plan
- tariff hedge 목적

Stage 3:
없음
- 투자계획만으로 Green 금지
- funding, tariff benefit, margin, FCF 확인 필요

Stage 4C-watch:
2025-04-22
- investors criticized lack of funding detail
- Hyundai Steel shares dropped over 21% after announcement
- weak domestic demand / Chinese imports / labor disputes also present
```

현대제철의 미국 공장 계획은 겉으로는 tariff hedge처럼 보였지만, funding detail 부재와 전략 불확실성 때문에 투자자에게 받아들여지지 않았다. Reuters는 발표 이후 현대제철 주가가 21.2% 하락했고, POSCO Holdings와 KOSPI보다 크게 부진했다고 보도했다. 이건 R13에서 **정책 유도 CAPEX를 Green으로 주면 안 되는 대표적 false-positive 방지 case**다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters policy-induced capex / market-reaction anchor

stage3_price:
N/A

U.S._plant_investment:
$5.8B~$6B

Hyundai_Motor_Group_U.S._package:
$21B

reported_share_drop_after_announcement:
-21.2%

POSCO_Holdings_same_period:
-18.3%

benchmark_index_same_period:
-5.5%

relative_underperformance_vs_KOSPI:
-21.2 - (-5.5)
= -15.7pp

funding_plan:
half via borrowing, possible POSCO equity input

risk_factors:
funding uncertainty
domestic demand weakness
Chinese imports
labor disputes

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = false_positive_score_prevention
rerating_result = policy_capex_without_funding_failed
stage_failure_type = 4C_watch
```

정책·관세 대응 CAPEX는 funding·margin·FCF가 없으면 Green이 아니라 RedTeam이다.

---

## Case E — LGES / L&F `contract-quality hard 4C`

```text
symbols = 373220 / 066970
source_sector = R3
case_type = 4C-thesis-break
archetype = CONTRACT_QUALITY_BREAK
```

### stage date

```text
LGES Stage 4C:
2025-12-17~18
- Ford EV battery supply deal cancellation
- 9.6조 원 / $6.5B contract lost

LGES 추가 4C:
2025-12-26
- Freudenberg 3.9조 원 contract cancellation
- total lost expected revenue = 13.5조 원

L&F Stage 4C:
2025-12-29
- Tesla cathode deal value $2.9B → $7,386
```

LGES는 Ford와 Freudenberg 계약 취소로 10일도 안 되는 기간에 약 13.5조 원의 기대매출을 잃었다. 이는 LGES 2024년 매출 25.62조 원의 절반을 넘는 규모다. L&F는 Tesla향 cathode 공급계약 가치가 29억 달러에서 7,386달러로 사실상 붕괴했다. R13에서 이 둘은 **계약 headline과 고객명만으로 Stage 3를 주면 안 되는 hard 4C 기준점**이다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported event and contract-value anchors

stage3_price:
N/A

LGES_Ford_cancelled_contract:
9.6T won / $6.5B

LGES_Freudenberg_cancelled_contract:
3.9T won / $2.7B

LGES_total_lost_expected_revenue:
13.5T won

LGES_2024_revenue:
25.62T won

lost_revenue_vs_2024_revenue:
13.5 / 25.62
= 52.7%

L&F_initial_contract_value:
$2.9B

L&F_revised_contract_value:
$7,386

L&F_contract_value_drawdown:
1 - 7,386 / 2,900,000,000
= 99.999745% collapse

stock_OHLC:
price_data_unavailable_after_deep_search beyond reported anchors
```

### R13 판정

```text
score_price_alignment = thesis_break
rerating_result = contract_quality_failure
stage_failure_type = hard_4C
```

R3의 Green gate는 `고객명`이 아니라 **actual call-off, take-or-pay, volume, OPM, FCF**다.

---

## Case F — 제주항공 `operational safety hard 4C`

```text
symbol = 089590
source_sector = R9
case_type = 4C-thesis-break
archetype = OPERATIONAL_TRUST_BREAK
```

### stage date

```text
Stage 1:
2023~2024
- LCC travel recovery
- Japan / Southeast Asia leisure demand

Stage 2:
없음

Stage 3:
없음

Stage 4C:
2024-12-30
- fatal crash
- 179 fatalities
- Jeju Air intraday -15.7%
- market cap wipeout up to 95.7B won
```

제주항공은 무안공항 사고 이후 장중 15.7% 하락해 record low를 기록했고, 약 957억 원의 시가총액이 증발했다. Reuters는 이 사고로 179명이 사망했고, 저가항공사 소비자 신뢰가 훼손될 수 있다고 보도했다. 이는 R13에서 **operational trust hard 4C의 가장 깨끗한 기준점**이다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported price/event anchors

stage3_price:
N/A

Jeju_Air_event_MAE_1D:
-15.7%

event_low_price:
6,920원

implied_pre_event_reference_price:
6,920 / (1 - 0.157)
= 약 8,209원

market_cap_wipeout:
95.7B won

fatalities:
179

AK_Holdings_MAE:
-12%

Korean_Air_MAE:
-1.3%

Asiana_MAE:
-0.8%

Hanatour_MAE:
-7%

Very_Good_Tour_MAE:
-11%

MFE:
N/A

below_stage3_price_flag:
N/A
```

### R13 판정

```text
score_price_alignment = thesis_break
rerating_result = operational_safety_trust_break
stage_failure_type = hard_4C
```

여행수요가 좋아도 fatal accident가 나오면 Green은 즉시 차단한다.

---

## Case G — SK텔레콤 `security/privacy 4C-watch`

```text
symbol = 017670
source_sector = R8 / R12-like 생활서비스 trust
case_type = 4C-watch
archetype = SECURITY_PRIVACY_TRUST_BREAK
```

### stage date

```text
Stage 1:
2024~2025
- telecom subscription base
- AI telecom / data platform 기대

Stage 2:
없음
- cybersecurity breach 이후 positive stage 부여 금지

Stage 3:
없음

Stage 4C-watch:
2025-04-28
- cyberattack / customer data leak
- shares intraday -8.5%, close -6.7%
- 23M users free USIM replacement

추가 4C-watch:
2025-07-04
- government says negligent
- 26.96M pieces of user data leaked
- revenue forecast cut by 800B won
- 700B won security investment over five years
```

SK텔레콤 데이터 유출은 R8/R13에서 **보안·개인정보 신뢰가 실제 매출전망과 보상비용으로 연결되는 사례**다. Reuters는 정부가 SK텔레콤의 USIM 데이터 보호 실패를 지적했고, 회사가 5년간 7,000억 원 보안투자를 하며 2025년 매출전망을 8,000억 원 낮췄다고 보도했다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported price / breach / cost anchors

stage3_price:
N/A

2025-04-28_event_intraday_MAE:
-8.5%

2025-04-28_close_MAE:
-6.7%

affected_users_initial:
23M

leaked_user_data_pieces:
26.96M

security_investment:
700B won over 5 years

annualized_security_investment:
700 / 5
= 140B won/year

2025_revenue_forecast_cut:
800B won

customer_benefit_package_cost:
about 500B won

USIM_replacement_users_by_late_June:
9.39M

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = thesis_break_watch
rerating_result = cybersecurity_operational_trust_break
stage_failure_type = strong_4C_watch
```

보안사고는 단순 one-day issue가 아니라 **매출전망·보상비용·신뢰비용으로 이어지는 4C gate**다.

---

## Case H — 정책·자원·디지털자산 price-only cluster

```text
symbols = 036460 / 377300 / LG CNS / Aton / ME2ON
source_sector = R6 / R11
case_type = price_moved_without_evidence
archetype = POLICY_RESOURCE_DIGITAL_ASSET_EVENT_PREMIUM
```

### stage date

```text
Korea Gas Stage 1:
2024-06-03
- East Sea oil/gas exploration approval
- up to 14B barrels resource possibility

Korea Gas Stage 4B:
2024-06-03
- Korea Gas +30% to 38,700원
- economic viability not confirmed
- drilling cost about 100B won per attempt

Stablecoin basket Stage 1:
2025-06
- won stablecoin policy pledge
- digital-asset reform 기대

Stablecoin basket Stage 4B:
2025-06
- Kakao Pay >2x
- LG CNS +70%
- Aton +80%
- ME2ON 3x

Stage 3:
없음
- resource commerciality / regulated revenue / issuer license / reserve income 전 Green 금지
```

한국가스공사는 동해 석유·가스 탐사 승인 발표만으로 장중 30% 올라 38,700원을 기록했다. 그러나 경제성은 확인되지 않았고, 최소 5차례 시추가 필요하며 시추 1회당 약 1,000억 원이 필요하다고 보도됐다. 원화 스테이블코인 basket도 실제 발행권·reserve income·수수료 수익 없이 Kakao Pay가 한 달에 2배 이상, ME2ON이 3배 상승했다. 둘 다 R13에서 **price_moved_without_evidence**의 정석이다. ([월스트리트저널][8])

### 실제 가격경로 검증

```text
price_data_source:
WSJ / FT reported event-return anchors

Korea_Gas:
stage3_price = N/A
event_peak_price = 38,700원
event_MFE_1D = +30.0%

implied_pre_event_reference_price:
38,700 / 1.30
= 약 29,769원

estimated_resource_possibility:
up to 14B barrels oil/gas

drilling_cost_per_attempt:
about 100B won

economic_viability:
not confirmed

Stablecoin basket:
Kakao_Pay_reported_MFE_month = > +100%
LG_CNS_reported_MFE_month = +70%
Aton_reported_MFE_month = +80%
ME2ON_reported_MFE_month = +200%

regulated_revenue_confirmed:
false

issuer_license_confirmed:
false

reserve_income_confirmed:
false

MFE_30D / 90D:
price_data_unavailable_after_deep_search beyond reported anchors

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = price_moved_without_evidence
rerating_result = policy_resource_digital_asset_event_premium
stage_failure_type = should_have_been_stage1_or_4B_watch
```

정책·자원·디지털자산 이벤트는 **실제 계약·경제성·규제수익 전에는 Green 금지**다.

---

# 5. 이번 R13 case별 요약표

| case                           | source R | 분류                                |                                                             실제 가격검증 | R13 판정                       |
| ------------------------------ | -------: | --------------------------------- | ------------------------------------------------------------------: | ---------------------------- |
| SK하이닉스                         |       R2 | structural_success + 4B           |           222,000원 → 1,447,000원, +551.8%; 2025 +274%, 2026 +200% 이상 | Stage 3 성공, 현재 4B            |
| APR / Medicube                 |       R5 | structural_success + 4B           |             158,300원, IPO 이후 >75%; Q4 revenue +124%, overseas +203% | Stage 3 후보 성공, 4B            |
| 삼성SDS                          |       R8 | event premium + success_candidate |                           KKR CB $820M, 장중 +20.8%, relative +17.8pp | Stage 2 + 4B                 |
| 현대제철 U.S. CAPEX                |   R4/R11 | false_positive 방지                 |                                      $5.8~6B U.S. plant 후 주가 -21.2% | policy capex failure         |
| LGES / L&F                     |       R3 | hard 4C                           |             LGES lost revenue 13.5T; L&F contract value -99.999745% | contract-quality 4C          |
| 제주항공                           |       R9 | hard 4C                           |                                          -15.7%, 6,920원, 시총 957억 증발 | safety hard 4C               |
| SK텔레콤                          |       R8 | strong 4C-watch                   | -8.5% intraday, revenue forecast cut 800B, security investment 700B | security/privacy 4C-watch    |
| Korea Gas / stablecoin cluster |   R6/R11 | price-only                        |                             Korea Gas +30%; Kakao Pay >2x, ME2ON 3x | price_moved_without_evidence |

---

# 6. score-price alignment 판정

```text
aligned:
- SK하이닉스
- APR / Medicube

4B-watch_success:
- SK하이닉스 market-cap milestone
- APR valuation / single-brand concentration
- 삼성SDS KKR/AI capital allocation +20.8%
- Korea Gas +30%
- stablecoin basket 2~3배

false_positive_score_prevention:
- 현대제철 U.S. CAPEX
- policy-induced capex without funding/margin

price_moved_without_evidence:
- Korea Gas resource event
- Kakao Pay / stablecoin basket
- any policy/resource/digital-asset rally before revenue bridge

hard_4C:
- LGES / L&F contract-quality break
- 제주항공 fatal safety accident

strong_4C_watch:
- SK텔레콤 cybersecurity / privacy trust break
```

---

# 7. 점수비중 교정

## 올릴 축

```text
price_path_alignment +5
stage3_to_large_MFE_confirmation +5
revenue_or_EPS_revision +5
order_to_revenue_conversion +5
commercial_revenue_conversion +5
actual_contract_quality +5
actual_calloff_or_take_or_pay +5
operational_trust +5
security_privacy_trust +5
hard_4c_early_warning +5
```

### 왜 올리나

SK하이닉스와 APR은 Stage 3 또는 Stage 3 후보가 실제 대형 가격경로로 이어질 수 있음을 보여준다. SK하이닉스는 EPS revision과 HBM capacity bottleneck이 +551.8% reported MFE로 연결됐고, APR은 해외 매출 +203%와 실제 매출 확대가 주가 재평가를 뒷받침했다. ([마켓워치][1])

## 내릴 축

```text
policy_news_only -5
resource_estimate_without_commerciality -5
stablecoin_policy_theme_only -5
AI_capital_allocation_without_revenue -5
contract_headline_without_calloff -5
capex_without_funding_or_margin -5
M&A_or_CB_event_without_revenue -4
IPO_or_debut_premium -4
high_score_without_price_validation -5
```

### 왜 내리나

Korea Gas와 stablecoin basket은 실제 경제성·규제수익 없이 가격이 먼저 뛰었다. 현대제철은 관세 대응 CAPEX처럼 보였지만 funding·margin clarity가 없어 주가가 크게 깨졌다. 삼성SDS는 좋은 AI Stage 2 후보지만, AI 매출 전 +20.8%는 Green이 아니라 4B다. ([월스트리트저널][8])

## Green gate 강화 조건

```text
R13 공통 Stage 3-Green 필수:
1. 회사 단위 evidence가 있음
2. revenue / EPS / FCF로 내려오는 경로가 있음
3. price path가 evidence 이후 따라옴
4. Stage 3 이후 MFE가 의미 있게 큼
5. MAE가 과도하지 않음
6. 4B saturation 상태가 아님
7. hard RedTeam 없음
8. contract / operational / governance / security trust 통과
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 2~5배 이상 상승
시총 milestone이 headline화
대형 CB / 증자 / M&A event
뉴스 발표일 20~30% 급등
정책·MOU·자원발견·stablecoin 테마 급등
IPO/debut 후 단기 2배
좋은 뉴스에도 주가 반응 둔화 또는 하락
valuation이 evidence보다 먼저 감

4B-elevated:
SK하이닉스처럼 1조 달러 근접
APR처럼 single-brand/device 매출 집중 속 valuation 급등
삼성SDS처럼 AI revenue 전 +20%급 상승
Korea Gas처럼 commerciality 전 +30%
stablecoin처럼 regulated revenue 전 2~3배 상승
```

## 4C hard gate 조건

```text
contract_cancellation
contract_value_collapse
fatal_safety_accident
operational_trust_break
security_or_privacy_breach_with_revenue_cut
major_governance_legal_break
PF_workout_or_credit_break
regulatory_reversal
commercialization_failure
financing_failure
capex_without_funding_clarity
```

이번 R13에서 확정 hard 4C는 **LGES/L&F contract-quality break**와 **제주항공 fatal safety accident**다. SK텔레콤은 hard 4C에 가까운 강한 4C-watch지만, 향후 매출·보상비용·규제제재가 확정되는 정도에 따라 hard 4C로 승격한다.

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_158.md 요약

```md
# R13 Loop 9. Cross-archetype RedTeam / 4B / Price Validation

이번 라운드는 R1~R12 Loop 9를 다시 검증한 R13 price-validation 라운드다.

핵심 결론:
- SK Hynix and APR/Medicube are aligned structural-success benchmarks. SK Hynix moved from 222,000 won Stage 3 anchor to 1,447,000 won reported record close, +551.8%. APR’s real overseas revenue growth supports a Stage 3 candidate but requires 4B-watch due to valuation and concentration.
- Samsung SDS is Stage 2 + 4B-watch. KKR $820M CB and AI capital allocation drove +20.8% before recurring AI revenue was proven.
- Hyundai Steel’s U.S. plant is false-positive prevention. A $5.8~6B U.S. capex plan without funding/margin clarity led to >21% share drop.
- LGES and L&F are hard 4C contract-quality anchors. LGES lost 13.5T won expected revenue, and L&F’s Tesla contract value collapsed from $2.9B to $7,386.
- Jeju Air is hard 4C operational-safety anchor. Fatal crash caused -15.7% intraday move and 95.7B won market-cap wipeout.
- SK Telecom is strong 4C-watch for security/privacy trust. Data leak caused revenue forecast cut of 800B won and 700B won security investment.
- Korea Gas and stablecoin basket are price_moved_without_evidence cases. Korea Gas +30% before commerciality; Kakao Pay >2x and ME2ON 3x before licensed revenue.
```

## checkpoint 요약

```md
# Checkpoint 28A Round 158 R13 Loop 9 Cross-archetype Price Validation

## 반영 내용
- R13 Loop 9 cross-archetype price-validation 라운드를 추가했다.
- Structural success, 4B timing, contract hard 4C, operational-safety hard 4C, security/privacy 4C-watch, policy/resource/digital-asset price-only rally를 비교했다.
- Reuters/MarketWatch/FT/WSJ/Business Insider/Vogue reported anchors로 가능한 MFE/MAE 및 event/contract/trust metrics를 계산했다.
- full OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- price_path_alignment, stage3_to_large_MFE_confirmation, revenue/EPS conversion, actual contract quality, operational/security trust 가중치 강화
- policy news-only, resource estimate without commerciality, stablecoin policy theme-only, AI capex/CB without revenue, capex without funding/margin 감점 강화
- 4B-watch와 hard 4C 구분 강화
```

## case row 초안

```jsonl
{"case_id":"r13_loop9_sk_hynix_hbm_stage3_4b","symbol":"000660","company_name":"SK하이닉스","source_sector":"R2","case_type":"structural_success","primary_archetype":"STRUCTURAL_SUCCESS_BUT_4B_WATCH","stage3_date":"2024-06-25","stage4b_date":"2026-05-04/2026-05-14","price_validation":{"price_data_source":"MarketWatch/Reuters reported anchors","stage3_price":222000,"reported_peak_price":1447000,"peak_return_from_stage3_pct":551.8,"reported_return_2025_pct":274,"reported_return_2026_ytd_pct":200,"minimum_compounded_return_from_2025_start_pct":1022,"market_cap_mfe_minimum_pct":842,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_rerating","notes":"HBM dominance and EPS revision produced large MFE; current state is 4B-watch."}
{"case_id":"r13_loop9_apr_medicube_structural_4b","symbol":"278470","company_name":"APR / Medicube","source_sector":"R5","case_type":"structural_success","primary_archetype":"K_BEAUTY_DEVICE_GLOBAL_BRAND","stage2_date":"2025-07-08","stage3_date":"2025-Q4_candidate","stage4b_date":"2025-2026","price_validation":{"price_data_source":"Business Insider/Vogue Business anchors","stage2_price":158300,"implied_ipo_reference_price_max":90457,"ipo_to_stage2_mfe_min_pct":75,"market_cap_july_2025_usd_bn":4.2,"q4_2025_revenue_usd_mn":440,"q4_2025_revenue_growth_pct":124,"q4_2025_overseas_revenue_usd_mn":362,"q4_2025_overseas_growth_pct":203,"fy_2025_revenue_usd_bn":1.2,"medicube_fy_2025_revenue_usd_bn":1.1,"medicube_revenue_share_pct":91.7,"price_validation_status":"reported_price_and_revenue_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"K_beauty_device_true_rerating_plus_4B_watch","notes":"Revenue conversion supports structural success, but single-brand/device concentration and valuation require 4B-watch."}
{"case_id":"r13_loop9_samsung_sds_kkr_ai_event_4b","symbol":"018260","company_name":"삼성SDS","source_sector":"R8","case_type":"success_candidate","primary_archetype":"AI_CLOUD_CAPITAL_ALLOCATION","stage2_date":"2026-04-15","stage4b_date":"2026-04-15","price_validation":{"price_data_source":"Reuters reported event return anchor","stage3_price":null,"event_mfe_1d_pct":20.8,"morning_trade_return_pct":19.4,"kospi_same_context_pct":3.0,"relative_intraday_outperformance_pp":17.8,"cb_investment_usd_mn":820,"cb_investment_krw_trn":1.207,"existing_cash_krw_trn":6.4,"combined_cash_plus_cb_krw_trn":7.607,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"AI_cloud_capital_allocation_watch","notes":"AI/KKR capital allocation is Stage 2 and 4B-watch; recurring AI revenue and FCF required before Green."}
{"case_id":"r13_loop9_hyundai_steel_policy_capex_failure","symbol":"004020","company_name":"현대제철","source_sector":"R4/R11","case_type":"failed_rerating","primary_archetype":"POLICY_INDUCED_CAPEX_FAILURE","stage4c_date":"2025-04-22","price_validation":{"price_data_source":"Reuters policy-induced capex / market-reaction anchor","stage3_price":null,"us_plant_investment_usd_bn":"5.8-6.0","hyundai_motor_group_us_package_usd_bn":21,"reported_share_drop_after_announcement_pct":-21.2,"posco_holdings_same_period_pct":-18.3,"benchmark_index_same_period_pct":-5.5,"relative_underperformance_vs_kospi_pp":-15.7,"funding_plan":"half_borrowing_possible_posco_equity","risk_factors":["funding_uncertainty","domestic_demand_weakness","Chinese_imports","labor_disputes"],"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"false_positive_score_prevention","rerating_result":"policy_capex_without_funding_failed","notes":"Tariff-hedge capex without funding/margin clarity is 4C-watch, not Green."}
{"case_id":"r13_loop9_lges_lnf_contract_quality_hard_4c","symbol":"373220/066970","company_name":"LGES / L&F","source_sector":"R3","case_type":"4c_thesis_break","primary_archetype":"CONTRACT_QUALITY_BREAK","stage4c_date":"2025-12","price_validation":{"price_data_source":"Reuters reported contract/event anchors","stage3_price":null,"lges_ford_cancelled_contract_krw_trn":9.6,"lges_freudenberg_cancelled_contract_krw_trn":3.9,"lges_total_lost_expected_revenue_krw_trn":13.5,"lges_2024_revenue_krw_trn":25.62,"lost_revenue_vs_2024_revenue_pct":52.7,"lnf_initial_contract_value_usd_bn":2.9,"lnf_revised_contract_value_usd":7386,"lnf_contract_value_drawdown_pct":-99.999745,"price_validation_status":"reported_event_and_contract_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"contract_quality_failure","notes":"Customer name and contract headline cannot be Green without actual call-off/take-or-pay/delivery/margin."}
{"case_id":"r13_loop9_jeju_air_operational_safety_hard_4c","symbol":"089590","company_name":"제주항공","source_sector":"R9","case_type":"4c_thesis_break","primary_archetype":"OPERATIONAL_TRUST_BREAK","stage4c_date":"2024-12-30","price_validation":{"price_data_source":"Reuters reported price/event anchors","stage3_price":null,"event_mae_1d_pct":-15.7,"event_low_price":6920,"implied_pre_event_reference_price":8209,"market_cap_wipeout_krw_bn":95.7,"fatalities":179,"ak_holdings_mae_pct":-12,"hanatour_mae_pct":-7,"very_good_tour_mae_pct":-11,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"operational_safety_trust_break","notes":"Fatal accident is hard 4C and blocks travel-demand Green."}
{"case_id":"r13_loop9_skt_security_privacy_4c_watch","symbol":"017670","company_name":"SK텔레콤","source_sector":"R8","case_type":"4c_watch","primary_archetype":"SECURITY_PRIVACY_TRUST_BREAK","stage4c_date":"2025-04-28/2025-07-04","price_validation":{"price_data_source":"Reuters reported breach/cost anchors","stage3_price":null,"event_intraday_mae_pct":-8.5,"event_close_mae_pct":-6.7,"affected_users_initial_mn":23,"leaked_user_data_pieces_mn":26.96,"security_investment_krw_bn":700,"annualized_security_investment_krw_bn":140,"revenue_forecast_cut_2025_krw_bn":800,"customer_benefit_package_cost_krw_bn":500,"usim_replacement_users_by_late_june_mn":9.39,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break_watch","rerating_result":"cybersecurity_operational_trust_break","notes":"Security/privacy breach affects revenue guidance and compensation cost; strong 4C-watch."}
{"case_id":"r13_loop9_policy_resource_stablecoin_price_only","symbol":"036460/377300/LG_CNS/Aton/ME2ON","company_name":"Korea Gas / stablecoin policy basket","source_sector":"R6/R11","case_type":"overheat","primary_archetype":"POLICY_RESOURCE_DIGITAL_ASSET_EVENT_PREMIUM","stage1_date":"2024-06/2025-06","stage4b_date":"2024-06/2025-06","price_validation":{"price_data_source":"WSJ/FT reported event-return anchors","stage3_price":null,"kogas_event_peak_price":38700,"kogas_event_mfe_1d_pct":30,"kogas_implied_pre_event_reference_price":29769,"resource_possibility_bbl_bn":14,"drilling_cost_per_attempt_krw_bn":100,"economic_viability_confirmed":false,"kakao_pay_mfe_month_pct":100,"lg_cns_mfe_month_pct":70,"aton_mfe_month_pct":80,"me2on_mfe_month_pct":200,"regulated_revenue_confirmed":false,"issuer_license_confirmed":false,"reserve_income_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"policy_resource_digital_asset_event_premium","notes":"Resource estimate and stablecoin policy are Stage 1/4B until commerciality or regulated revenue is confirmed."}
```

## shadow weight row 초안

```csv
archetype,price_path_alignment,stage3_mfe_confirmation,revenue_eps_conversion,actual_contract_quality,operational_trust,security_privacy_trust,event_penalty,capex_funding_redteam,governance_redteam,4b_watch_sensitivity,hard_4c_sensitivity,notes
STRUCTURAL_SUCCESS_ALIGNED,+5,+5,+5,+4,+3,+2,0,+0,+0,+4,+2,SK Hynix and APR prove Stage 3 can produce large MFE when revenue/EPS conversion exists.
STRUCTURAL_SUCCESS_BUT_4B_WATCH,+5,+5,+5,+4,+3,+2,-1,+1,+1,+5,+3,Large MFE plus market-cap/valuation milestone requires 4B-watch.
AI_CLOUD_CAPITAL_ALLOCATION,+3,+2,+3,+2,+3,+2,-5,+3,+2,+5,+3,Samsung SDS KKR event is Stage 2 and 4B before AI revenue/FCF.
POLICY_INDUCED_CAPEX_FAILURE,+0,+0,+0,+1,+2,+1,-5,+5,+2,+4,+4,Hyundai Steel shows policy capex without funding/margin can fail.
CONTRACT_QUALITY_BREAK,+0,+0,+0,+5,+2,+1,0,+1,+1,+3,+5,LGES/L&F contract cancellation/value collapse is hard 4C.
OPERATIONAL_TRUST_BREAK,+0,+0,+0,+0,+5,+2,0,+0,+2,+3,+5,Jeju Air fatal crash is hard operational trust 4C.
SECURITY_PRIVACY_TRUST_BREAK,+0,+0,+0,+0,+4,+5,0,+1,+3,+4,+5,SK Telecom data breach is strong 4C-watch with revenue/cost impact.
POLICY_RESOURCE_DIGITAL_ASSET_EVENT_PREMIUM,+0,+0,+0,+0,+1,+1,-5,+2,+2,+5,+4,Korea Gas/stablecoin rallies are price_moved_without_evidence until commerciality/revenue.
```

---

# 이번 R13 Loop 9 결론

R13의 결론은 분명하다.

```text
1. Stage 3는 잘 잡히면 진짜 대형 MFE를 만든다.
   SK하이닉스와 APR이 그 증거다.

2. 하지만 대형 MFE 이후에는 4B-watch가 빨리 붙어야 한다.
   SK하이닉스의 시총 milestone, APR의 single-brand concentration이 그렇다.

3. 좋은 Stage 2라도 Green은 아니다.
   삼성SDS의 KKR/AI capital allocation은 좋은 후보지만 +20.8%는 4B다.

4. 정책 유도 CAPEX는 Green이 아니라 RedTeam일 수 있다.
   현대제철 U.S. plant가 그 반례다.

5. 계약 headline은 actual call-off 없으면 무너질 수 있다.
   LGES와 L&F는 R3 hard 4C 기준점이다.

6. 안전사고는 가장 강한 hard 4C다.
   제주항공은 operational trust가 깨지면 여행수요가 아무 의미 없음을 보여준다.

7. 보안·개인정보 신뢰는 R8의 핵심 4C gate다.
   SK텔레콤은 데이터 유출이 매출전망과 비용으로 연결된 사례다.

8. 정책·자원·디지털자산 테마는 price-only rally가 가장 많다.
   Korea Gas와 stablecoin basket은 commerciality / regulated revenue 전 Green 금지다.
```

한 문장으로 압축하면:

> **R13의 역할은 “좋아 보이는 후보”를 한 번 더 부수는 것이다. Stage 3는 대형 MFE로 증명되고, 4B는 가격 선반영·crowding·자본조달·event premium으로 증명되며, 4C는 계약·안전·보안·운영·규제·신뢰 훼손으로 증명된다.**

[1]: https://www.marketwatch.com/story/sk-hynix-s-hbm-dominance-higher-chip-prices-could-lift-earnings-market-talk-6508cbf8?utm_source=chatgpt.com "SK Hynix's HBM Dominance, Higher Chip Prices Could Lift Earnings -- Market Talk"
[2]: https://www.businessinsider.com/south-korea-kim-byung-hoon-beauty-billionaire-kylie-jenner-fan-2025-7?utm_source=chatgpt.com "Meet South Korea's new millennial beauty billionaire, who counts Kylie Jenner as a fan of his skincare gadgets"
[3]: https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com "KKR to buy $820 million of Samsung SDS convertible bonds, shares jump 20%"
[4]: https://www.reuters.com/business/autos-transportation/hyundai-steels-6-bln-us-investment-draws-investor-ire-tests-seouls-tariff-2025-04-22/?utm_source=chatgpt.com "Hyundai Steel's $6 billion US investment draws investor ire, tests Seoul's tariff strategy"
[5]: https://www.reuters.com/business/finance/south-koreas-lg-energy-solution-ends-65-billion-ev-battery-supply-deal-with-ford-2025-12-17/?utm_source=chatgpt.com "Ford cancels EV battery deal worth $6.5 billion with South Korea's LG Energy Solution"
[6]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"
[7]: https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-orders-sk-telecom-strengthen-data-security-after-leak-2025-07-04/?utm_source=chatgpt.com "South Korea penalises 'negligent' SK Telecom over major data leak"
[8]: https://www.wsj.com/articles/korea-gas-leads-energy-rally-on-seoul-s-offshore-oil-drilling-approval-c8c4d428?utm_source=chatgpt.com "Korea Gas Leads Energy Rally on Seoul's Offshore Oil Drilling Approval"

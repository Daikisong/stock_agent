순서상 이번은 **R13 Loop 11 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리**다.

```text
round = R13 Loop 11
round_id = round_184
large_sector = CROSS_ARCHETYPE_REDTEAM_PRICE_VALIDATION
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
```

이번 R13은 R1~R12 Loop 11을 다시 부수는 라운드다. 핵심 질문은 하나다.

> **Stage 3가 진짜 대형 MFE를 만들었는가, 4B가 과열·선반영을 제때 잡았는가, 4C가 계약·보안·공장·거시 리스크를 큰 하락 전에 막았는가.**

---

# 1. 이번 라운드 대섹터

```text
R13 = Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리
```

R13은 섹터가 아니라 **검문소**다.
좋아 보이는 모든 Stage 2·3 후보를 다시 세 줄로 판정한다.

```text
1. 실제 돈으로 닫혔나?
2. 가격이 먼저 달렸나?
3. 한 번 깨지면 회복 어려운 hard gate가 있었나?
```

---

# 2. 대상 canonical archetype

```text
STRUCTURAL_SUCCESS_ALIGNED
STRUCTURAL_SUCCESS_BUT_4B_WATCH
CONTRACT_HEADLINE_STAGE2_NOT_GREEN
AI_CAPITAL_ALLOCATION_EVENT_PREMIUM
POLICY_DIGITAL_ASSET_PRICE_ONLY
EVIDENCE_GOOD_BUT_PRICE_FAILED
CONTRACT_QUALITY_HARD_4C
OPERATIONAL_TRUST_HARD_4C
MACRO_GEOPOLITICAL_HARD_4C
```

---

# 3. deep sub-archetype

```text
성공 benchmark:
- SK Hynix HBM / EUV / AI memory capacity
- APR / Medicube K-beauty global sell-through

4B / event premium:
- Samsung E&A Saudi EPC contract rally
- Samsung SDS KKR / AI capital allocation
- KRW stablecoin policy basket
- IPO / cloud-AI price fail

evidence-good-but-price-failed:
- LG CNS cloud/AI IPO
- Samsung Biologics U.S. CDMO facility

hard 4C:
- LGES Ford/Freudenberg contract cancellation
- L&F Tesla cathode contract collapse
- SK Telecom data breach
- Kumho Tire factory fire
- Hormuz/Iran macro energy shock
```

---

# 4. 국장 신규 후보 case

## Case A — SK하이닉스 `structural_success_aligned + 4B-watch`

```text
symbol = 000660
source_sector = R2
case_type = structural_success + 4B-watch
archetype = STRUCTURAL_SUCCESS_ALIGNED / STRUCTURAL_SUCCESS_BUT_4B_WATCH
```

### stage date

```text
Stage 1:
2024년 상반기
- HBM demand
- DRAM price upcycle
- AI server memory bottleneck

Stage 2:
2024-06-25
- Nomura raises 2024 OP forecast to 30T won
- 2025 OP forecast to 53T won
- target price 290,000 won
- stock anchor 222,000 won

Stage 3:
2024-06-25 후보
- HBM dominance + EPS revision + memory price upcycle

Stage 3 validation:
2026-03-24
- ASML EUV order 11.95T won / $7.97B
- SK Hynix shares +5.7%
- equipment for HBM / advanced DRAM

Stage 4B:
2026-05-04
- shares close +12.52% at 1,447,000 won record high

Stage 4B-elevated:
2026-05-14
- shares +274% in 2025
- shares >+200% in 2026
- market cap about $942B
- less than $100B just 16 months earlier
```

SK하이닉스는 이번 Loop 11 전체의 **Stage 3 성공 benchmark**다. 2024년 6월에는 HBM 지배력과 메모리 가격 상승으로 영업이익 revision이 나왔고, 주가 anchor는 222,000원이었다. 이후 2026년 3월 ASML EUV 장비 11.95조 원 주문, 2026년 5월 1,447,000원 record high, 2025년 +274%와 2026년 +200% 이상이라는 가격경로가 이어졌다. 이제는 신규 Green보다 **4B-watch**가 맞다. ([마켓워치][1])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / Reuters reported anchors

stage3_price:
222,000 won

record_high_price:
1,447,000 won

MFE_from_stage3_to_record_high:
1,447,000 / 222,000 - 1
= +551.8%

ASML_EUV_order:
11.95T won / $7.97B

ASML_order_event_return:
+5.7%

reported_2025_return:
+274%

reported_2026_return:
> +200%

minimum_compounded_return_from_start_2025:
(1 + 2.74) * (1 + 2.00) - 1
= +1,022% 이상

market_cap:
about $942B

market_cap_from_under_100B:
942 / 100 - 1
= +842% 이상

MFE_30D / 90D / 180D:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = aligned
rerating_result = true_structural_rerating
current_state = 4B_watch
```

**교정 포인트:** Stage 3 Green은 가능했다. 다만 Stage 3 이후 5배 이상 MFE가 나오면, 다음 scoring은 Green 추가가 아니라 4B/watch 전환이어야 한다.

---

## Case B — APR / Medicube `structural_success_aligned + concentration 4B-watch`

```text
symbol = 278470
source_sector = R5
case_type = structural_success + 4B-watch
archetype = STRUCTURAL_SUCCESS_BUT_4B_WATCH
```

### stage date

```text
Stage 1:
2024~2025
- K-beauty revival
- beauty device + skincare hybrid
- TikTok / Amazon / Ulta channel expansion

Stage 2:
2025
- Medicube viral demand
- TikTok Shop / Amazon Prime Day / Ulta expansion
- creator-affiliate channel traction

Stage 3:
2025 Q4 후보
- Q4 revenue about $440M, +124% YoY
- overseas revenue about $362M, +203% YoY
- overseas share 87%
- FY revenue about $1.2B
- Medicube revenue about $1.1B

Stage 4B:
- Medicube concentration around 91.7% of APR revenue
- device / single-brand concentration
- valuation premium after rapid growth
```

APR/Medicube는 R5의 진짜 structural success 후보다. 단순 viral이 아니라 Q4 매출 +124%, 해외매출 +203%, TikTok Shop $102.9M, Amazon Prime Day $22M, Ulta 1,400개 이상 매장 확장이 확인됐다. 다만 FY 매출 약 $1.2B 중 Medicube가 약 $1.1B로 91.7%를 차지하므로, Stage 3 후보와 동시에 **single-brand 4B-watch**가 필요하다. ([Vogue][2])

### 실제 가격경로 검증

```text
price_data_source:
Vogue Business reported revenue/channel anchors

stage3_price:
price_data_unavailable_after_deep_search

Q4_2025_revenue:
$440M

Q4_2025_revenue_growth:
+124% YoY

Q4_2025_overseas_revenue:
$362M

Q4_2025_overseas_growth:
+203% YoY

overseas_revenue_share:
87%

FY_2025_revenue:
$1.2B

Medicube_FY_2025_revenue:
$1.1B

Medicube_revenue_share:
1.1 / 1.2
= 91.7%

TikTok_Shop_revenue:
$102.9M

Amazon_Prime_Day_sales:
$22M

Ulta_store_expansion:
1,400+ stores

MFE / MAE:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = aligned_partial
rerating_result = K_beauty_structural_rerating
current_state = 4B_concentration_watch
```

**교정 포인트:** sell-through와 해외매출이 실제로 찍히면 Green을 줄 수 있다. 그러나 revenue concentration 80~90% 이상이면 Green 점수와 별개로 4B-risk를 동시에 올린다.

---

## Case C — Samsung E&A Fadhili `contract Stage 2 + 4B-watch`

```text
symbol = 028050
source_sector = R1 / R10
case_type = success_candidate + event_premium
archetype = CONTRACT_HEADLINE_STAGE2_NOT_GREEN
```

### stage date

```text
Stage 1:
2024-04-02
- Saudi gas infra expansion
- Middle East EPC order cycle

Stage 2:
2024-04-03
- Samsung E&A wins about $6B Saudi Aramco Fadhili contract
- total Fadhili package $7.7B
- shares +8.5% to 26,750 won
- KOSPI -1.4%

Stage 3:
없음
- signed mega-order는 강한 Stage 2
- 공정률, 매출 인식, margin, working capital, cash collection 전 Green 금지

Stage 4B:
2024-04-03
- contract headline before margin / cash conversion
```

Samsung E&A는 “수주 headline”과 Stage 3를 분리하는 기준점이다. 약 $6B 계약은 매우 강한 Stage 2지만, 발표일 +8.5%와 KOSPI 대비 +9.9pp 아웃퍼폼은 아직 공정률·마진·현금회수 전 가격 선반영이다. ([월스트리트저널][3])

### 실제 가격경로 검증

```text
price_data_source:
WSJ reported contract / event-return anchor

stage2_event_price:
26,750 won

event_MFE:
+8.5%

implied_prior_price:
26,750 / 1.085
= 24,654 won

KOSPI_same_context:
-1.4%

relative_outperformance:
8.5 - (-1.4)
= +9.9pp

contract_value:
about $6B

total_Fadhili_package:
$7.7B

contract_share_of_total:
6.0 / 7.7
= 77.9%

target_price:
35,000 won

target_upside_from_event_price:
35,000 / 26,750 - 1
= +30.8%

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = event_premium_success_candidate
rerating_result = EPC_order_stage2_not_green
current_state = 4B_watch
```

**교정 포인트:** R1/R10 수주는 signed contract까지는 Stage 2다. Green은 `progress_revenue + EPC margin + cash collection`이 들어와야 한다.

---

## Case D — Samsung SDS + stablecoin basket `AI/digital event premium`

```text
symbols = 018260 / 377300 / LG CNS / Aton / ME2ON
source_sector = R6 / R8
case_type = event_premium + price_moved_without_evidence
archetype = AI_CAPITAL_ALLOCATION_EVENT_PREMIUM / POLICY_DIGITAL_ASSET_PRICE_ONLY
```

### stage date

```text
Samsung SDS Stage 2:
2026-04-15
- KKR buys $820M convertible bonds
- Samsung SDS has existing cash 6.4T won
- AI infrastructure / physical AI / stablecoin / M&A narrative

Samsung SDS Stage 4B:
2026-04-15
- shares +20.8% intraday
- morning +19.4%
- KOSPI +3.0%

Stablecoin basket Stage 1:
2025-06
- won stablecoin policy pledge
- digital-asset reform expectation

Stablecoin basket Stage 4B:
2025-06
- Kakao Pay >2x
- LG CNS +70%
- Aton +80%
- ME2ON 3x
- issuer license / reserve income / fee revenue not confirmed
```

Samsung SDS는 좋은 Stage 2지만, AI revenue 전 +20.8%는 4B다. Stablecoin basket은 더 깨끗한 price-only case다. Kakao Pay, LG CNS, Aton, ME2ON은 실제 issuer license·reserve income·fee revenue가 확인되기 전 2~3배 움직였다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / FT reported event-return anchors

Samsung_SDS_event_MFE:
+20.8%

Samsung_SDS_morning_return:
+19.4%

KOSPI_same_context:
+3.0%

Samsung_SDS_relative_outperformance:
20.8 - 3.0
= +17.8pp

KKR_CB_investment:
$820M

Samsung_SDS_existing_cash:
6.4T won

combined_cash_plus_CB:
6.4T + 1.207T
= about 7.607T won

Stablecoin_Kakao_Pay_MFE:
> +100%

Stablecoin_LG_CNS_MFE:
+70%

Stablecoin_Aton_MFE:
+80%

Stablecoin_ME2ON_MFE:
+200%

margin_loan_context:
20.5T won

issuer_license_confirmed:
false

reserve_income_confirmed:
false

fee_revenue_confirmed:
false
```

### R13 판정

```text
score_price_alignment = price_moved_without_evidence / event_premium
rerating_result = AI_digital_policy_4B
current_state = 4B_elevated
```

**교정 포인트:** `AI capital allocation`, `stablecoin policy`, `M&A funding`은 Stage 2일 수 있지만, revenue 전 +20~200%는 Green이 아니라 4B다.

---

## Case E — LG CNS + Samsung Biologics `evidence_good_but_price_failed`

```text
symbols = LG CNS / 207940
source_sector = R7 / R8
case_type = evidence_good_but_price_failed
archetype = EVIDENCE_GOOD_BUT_PRICE_FAILED
```

### stage date

```text
LG CNS Stage 2:
2025-02-05
- IPO price 61,900 won
- cloud/AI services > half of sales
- 1Q~3Q 2024 revenue about 4T won
- OP 313B won

LG CNS price validation:
2025-02-05
- debut trade 59,700 won
- -3.55% vs IPO price

Samsung Biologics Stage 2:
2025-12-21
- buys GSK Rockville facility for $280M
- first U.S. production site
- 60,000L drug substance capacity

Samsung Biologics price validation:
2025-12-22
- shares -0.4%
- KOSPI +2.0%
```

LG CNS와 Samsung Biologics는 둘 다 “뉴스는 좋은데 가격은 실패”한 case다. LG CNS는 cloud/AI 매출비중이 높았지만 IPO 첫날 공모가 대비 -3.55%였다. Samsung Biologics는 미국 첫 생산시설 확보라는 좋은 Stage 2에도 주가는 -0.4%, KOSPI는 +2.0%였다. ([Reuters][5])

### 실제 가격경로 검증

```text
price_data_source:
Reuters reported IPO/facility event anchors

LG_CNS_IPO_price:
61,900 won

LG_CNS_debut_trade:
59,700 won

LG_CNS_debut_MAE:
59,700 / 61,900 - 1
= -3.55%

LG_CNS_1Q_3Q_2024_revenue:
about 4T won

LG_CNS_1Q_3Q_2024_OP:
313B won

LG_CNS_OP_margin:
313B / 4T
= 7.8%

Samsung_Biologics_GSK_facility_value:
$280M

Samsung_Biologics_facility_capacity:
60,000L

Samsung_Biologics_event_MAE:
-0.4%

KOSPI_same_context:
+2.0%

Samsung_Biologics_relative_underperformance:
-0.4 - 2.0
= -2.4pp
```

### R13 판정

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = good_evidence_but_no_fresh_rerating
current_state = wait_for_revenue_margin_FCF
```

**교정 포인트:** 좋은 사업 evidence가 있어도 가격이 실패하면 Green threshold를 낮추면 안 된다. `fresh rerating response` 축을 따로 봐야 한다.

---

## Case F — LGES / L&F `contract-quality hard 4C`

```text
symbols = 373220 / 066970
source_sector = R3 / R4
case_type = 4C-thesis-break
archetype = CONTRACT_QUALITY_HARD_4C
```

### stage date

```text
LGES Stage 4C:
2025-12
- Ford cancels 9.6T won EV battery contract
- Freudenberg cancels 3.9T won battery order
- total expected revenue loss 13.5T won
- more than half of 2024 revenue 25.62T won

L&F Stage 4C:
2025-12-29
- Tesla cathode supply deal value $2.9B → $7,386
- 4680 yield issue / EV demand slowdown / Cybertruck weakness
```

LGES와 L&F는 R3/R4에서 가장 강한 contract-quality hard 4C다. LGES는 10일도 안 돼 13.5조 원 기대매출을 잃었고, 이는 2024년 매출 25.62조 원의 절반 이상이다. L&F는 Tesla cathode deal 가치가 $2.9B에서 $7,386으로 사실상 사라졌다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters contract-cancellation / contract-value-collapse anchors

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

L&F_contract_value_collapse:
1 - 7,386 / 2,900,000,000
= 99.999745%

MFE:
N/A

MAE_30D / 90D:
price_data_unavailable_after_deep_search
```

### R13 판정

```text
score_price_alignment = thesis_break
rerating_result = battery_contract_quality_failure
current_state = hard_4C
```

**교정 포인트:** 고객명·계약금액 headline은 Green이 아니다. `actual call-off`, `volume`, `take-or-pay`, `margin`, `cash collection`이 없으면 contract score를 강하게 제한한다.

---

## Case G — SK Telecom + Kumho Tire `operational-trust hard 4C`

```text
symbols = 017670 / 073240
source_sector = R8 / R9
case_type = 4C-thesis-break
archetype = OPERATIONAL_TRUST_HARD_4C
```

### stage date

```text
SK Telecom Stage 4C:
2025-04-28
- cyberattack / data breach disclosed
- shares intraday -8.5%
- close -6.7%
- KOSPI +0.1%
- 23M users offered free USIM replacement

SK Telecom Stage 4C 강화:
2025-07-04 / 2025-08-28
- 26.96M pieces of user data leaked
- shares -5.6% on July 4
- 700B won / 5-year security investment
- 2025 revenue forecast cut by 800B won
- 134B won fine

Kumho Tire Stage 4C:
2025-05-17 / 2025-05-19
- Gwangju factory fire
- production suspended
- annual capacity 12M tires
- nearly 20% of global output
- shares -8%
```

SK Telecom은 보안 신뢰 hard 4C다. Kumho Tire는 공장화재·생산차질 hard 4C다. 둘 다 수요가 아니라 **운영 신뢰**가 깨지는 순간이다. SKT는 보안사고가 주가, 매출전망, 보상비용, 벌금으로 내려왔고, Kumho는 글로벌 생산능력 약 20% 공장이 멈췄다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters breach / fine / factory-fire anchors

SKT_initial_intraday_MAE:
-8.5%

SKT_initial_close_MAE:
-6.7%

KOSPI_same_context:
+0.1%

SKT_relative_underperformance:
-6.7 - 0.1
= -6.8pp

SKT_users_initially_affected:
23M

SKT_data_leak:
26.96M pieces of user data

SKT_July4_MAE:
-5.6%

SKT_security_investment:
700B won over 5 years

SKT_annualized_security_investment:
140B won/year

SKT_revenue_forecast_cut:
800B won

SKT_fine:
134B won / $96.53M

Kumho_event_MAE:
-8.0%

Kumho_Gwangju_capacity:
12M tires/year

Kumho_share_of_global_capacity:
nearly 20%

Kumho_revenue_target_risk:
2025 revenue target may need downward revision
```

### R13 판정

```text
score_price_alignment = thesis_break
rerating_result = operational_trust_break
current_state = hard_4C
```

**교정 포인트:** R8/R9/R10에서 보안·공장·안전·품질 사고는 일반 RedTeam이 아니라 hard gate다. 매출성장 점수보다 먼저 차단한다.

---

## Case H — Hormuz / Iran shock `macro hard 4C`

```text
symbol = KOSPI / KRW / 005380 / 005930 / 000660
source_sector = R11
case_type = macro hard 4C
archetype = MACRO_GEOPOLITICAL_HARD_4C
```

### stage date

```text
Stage 1:
2026-03-04
- Iran conflict escalation
- Hormuz / Gulf energy risk
- Korea oil-import dependency exposed

Stage 2:
없음

Stage 3:
없음

Stage 4C:
2026-03-04
- KOSPI -12.06%
- close 5,093.54
- two-day market-cap wipeout $553.82B
- won touches 1,505.8/USD
- Hyundai Motor -15.8%
- Samsung Electronics -11.7%
- SK Hynix -9.6%
```

Hormuz/Iran shock은 이번 Loop 11 전체에서 가장 강한 macro hard 4C다. 한국은 중동 원유 의존도가 약 70%이고, KOSPI가 하루 -12.06%, 원화가 17년 저점, 자동차·반도체 대형주가 동시에 급락했다. 이건 개별 종목 RedTeam이 아니라 **모든 sector scoring 위에 덮는 macro overlay**다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters / Barron's macro-market anchors

KOSPI_event_MAE:
-12.06%

KOSPI_close:
5,093.54

market_cap_wipeout_2D:
$553.82B

KRW_intraday_low:
1,505.8/USD

Hyundai_Motor_MAE:
-15.8%

Samsung_Electronics_MAE:
-11.7%

SK_Hynix_MAE:
-9.6%

oil_import_dependency:
about 70% from Middle East

MFE:
N/A

Stage 4C 큰 하락 이전 포착 여부:
hard macro event itself
```

### R13 판정

```text
score_price_alignment = thesis_break
rerating_result = macro_energy_security_hard_4C
current_state = hard_4C_overlay
```

**교정 포인트:** Hormuz/energy/FX shock은 sector-neutral 악재가 아니다. 한국 시장에서는 자동차·반도체·항공·화학·소비재까지 동시에 누르는 macro hard gate다.

---

# 5. 이번 R13 case별 요약표

| case                     | source R | 분류                             |                                                  실제 가격검증 | R13 판정                     |
| ------------------------ | -------: | ------------------------------ | -------------------------------------------------------: | -------------------------- |
| SK Hynix                 |       R2 | structural_success + 4B        |    222,000 → 1,447,000, +551.8%; 2025 +274%, 2026 +200%+ | aligned / now 4B           |
| APR / Medicube           |       R5 | structural_success + 4B        |   Q4 revenue +124%, overseas +203%, Medicube share 91.7% | aligned / concentration 4B |
| Samsung E&A              |   R1/R10 | contract Stage 2 + 4B          |                             +8.5%, 26,750원, contract $6B | Stage 2, not Green         |
| Samsung SDS / stablecoin |    R6/R8 | event premium / price-only     |                      SDS +20.8%; Kakao Pay >2x, ME2ON 3x | 4B elevated                |
| LG CNS / SamsungBio      |    R7/R8 | evidence_good_but_price_failed |             LG CNS -3.55%; SamsungBio -0.4% vs KOSPI +2% | price failed               |
| LGES / L&F               |    R3/R4 | hard 4C                        |       LGES lost 13.5T expected revenue; L&F $2.9B→$7,386 | contract hard 4C           |
| SKT / Kumho              |    R8/R9 | hard 4C                        | SKT -6.7%, revenue cut 800B; Kumho -8%, 20% capacity hit | operational hard 4C        |
| Hormuz / Iran            |      R11 | macro hard 4C                  |               KOSPI -12.06%, KRW 1,505.8, Hyundai -15.8% | macro hard 4C              |

---

# 6. score-price alignment 판정

```text
aligned:
- SK Hynix
- APR / Medicube

aligned_but_now_4B:
- SK Hynix
- APR / Medicube

success_candidate_stage2_not_green:
- Samsung E&A
- Samsung SDS
- Samsung Biologics
- LG CNS
- Samsung E&A / overseas EPC contract
- SamsungBio / U.S. CDMO facility

event_premium:
- Samsung SDS KKR / AI capital allocation
- KRW stablecoin basket
- Samsung E&A Fadhili contract rally

price_moved_without_evidence:
- stablecoin basket
- AI capital allocation before recurring AI revenue
- EPC contract rally before margin/cash collection

evidence_good_but_price_failed:
- LG CNS
- Samsung Biologics GSK facility

hard_4C:
- LGES / L&F contract-quality break
- SK Telecom cybersecurity operational trust break
- Kumho Tire factory fire
- Hormuz / Iran macro energy shock

macro_overlay:
- Hormuz / Iran shock
```

---

# 7. 점수비중 교정

## 올릴 축

```text
stage3_to_large_MFE_confirmation +5
revenue_or_EPS_conversion +5
commercial_revenue_conversion +5
actual_calloff_or_take_or_pay +5
cash_collection_quality +5
price_path_alignment +5
fresh_rerating_response +4
operational_trust +5
security_privacy_trust +5
macro_risk_overlay +5
```

### 왜 올리나

SK하이닉스는 Stage 3 이후 대형 MFE가 실제로 나왔다. APR도 해외매출·채널 sell-through가 숫자로 내려왔다. 반대로 LG CNS와 SamsungBio는 좋은 evidence가 있었지만 가격이 실패했다. 이 차이를 점수표가 분리해야 한다.

## 내릴 축

```text
contract_headline_without_margin -5
AI_capital_allocation_without_revenue -5
stablecoin_policy_theme_only -5
IPO_debut_or_listing_story -5
M&A_or_facility_without_utilization -5
customer_name_without_calloff -5
good_news_but_price_failed -4
data_breach_or_security_failure -5
factory_fire_or_supply_disruption -5
macro_energy_FX_shock -5
```

### 왜 내리나

Samsung E&A는 수주가 좋지만 margin/cash collection 전에는 Stage 2다. Samsung SDS와 stablecoin basket은 가격이 매출보다 먼저 갔다. LGES/L&F는 계약 headline이 실제 call-off로 닫히지 못하면 hard 4C가 된다는 기준점이다. SKT와 Kumho는 운영 신뢰가 깨지면 성장논리가 바로 무너진다.

## Green gate 강화 조건

```text
R13 공통 Stage 3-Green 필수:
1. revenue / EPS / FCF conversion 확인
2. price path가 evidence 이후 따라옴
3. Stage 3 이후 MFE가 의미 있게 큼
4. MAE가 과도하지 않음
5. contract는 actual call-off / margin / cash collection 확인
6. platform은 paid usage / ARPU / trust 확인
7. 제조는 capacity / utilization / supply continuity 확인
8. hard 4C 없음
9. macro hard overlay 없음
```

## 4B 조기감지 조건

```text
4B-watch:
Stage 3 이후 3~5배 이상 상승
market-cap milestone headline화
대형 계약 발표일 +5~10% 급등
AI/M&A/CB event로 +20%급 상승
스테이블코인/정책 테마로 2~3배 상승
IPO/debut 후 실적 전 valuation 확장
좋은 뉴스에도 price reaction 둔화 또는 하락

4B-elevated:
SK Hynix처럼 1조 달러 근접
APR처럼 단일 브랜드 매출 집중 90%+
Samsung SDS처럼 AI revenue 전 +20.8%
stablecoin처럼 regulated revenue 전 2~3배
Samsung E&A처럼 margin/cashflow 전 계약 rally
```

## 4C hard gate 조건

```text
contract cancellation
contract value collapse
actual call-off failure
data breach with revenue/fine/compensation impact
factory fire / production suspension
fatal safety accident
security/privacy trust break
major regulatory/governance break
PF or credit break
geopolitical energy chokepoint shock
KRW disorderly depreciation
macro circuit breaker / index crash
```

이번 R13 Loop 11의 hard 4C는 네 개로 확정한다.

```text
1. LGES / L&F contract-quality hard 4C
2. SK Telecom security/privacy hard 4C
3. Kumho Tire factory-fire hard 4C
4. Hormuz / Iran macro hard 4C
```

---

# 8. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
```

---

# 9. patch-ready 출력

## docs/round/round_184.md 요약

```md
# R13 Loop 11. Cross-archetype RedTeam / 4B / Price Validation

이번 라운드는 R1~R12 Loop 11 전체를 다시 검증한 R13 price-validation 라운드다.

핵심 결론:
- SK Hynix is the clean structural-success benchmark. Stage 3 anchor was 222,000 won, and later record high was 1,447,000 won, implying +551.8% MFE. It also gained +274% in 2025 and >+200% in 2026, with market cap around $942B. Current state is 4B-watch.
- APR / Medicube is R5 structural-success benchmark. Q4 2025 revenue +124%, overseas revenue +203%, FY revenue about $1.2B, Medicube about $1.1B. Concentration means 4B-watch.
- Samsung E&A Fadhili is signed-contract Stage 2 plus 4B-watch. Contract about $6B, stock +8.5%, but margin, progress revenue and cash collection are required before Green.
- Samsung SDS / stablecoin basket is event premium / price_moved_without_evidence. Samsung SDS +20.8% before recurring AI revenue; stablecoin basket moved 2~3x before licensing, reserve income or fee revenue.
- LG CNS / Samsung Biologics are evidence_good_but_price_failed. LG CNS debuted -3.55% below IPO price; SamsungBio’s U.S. facility news produced -0.4% vs KOSPI +2.0%.
- LGES / L&F are contract-quality hard 4C. LGES lost 13.5T won expected revenue from Ford/Freudenberg cancellations; L&F Tesla cathode deal collapsed from $2.9B to $7,386.
- SK Telecom / Kumho Tire are operational-trust hard 4C. SKT breach caused stock drawdown, 800B won revenue forecast cut, 700B won security investment and 134B won fine; Kumho fire shut a plant with nearly 20% global capacity.
- Hormuz/Iran shock is macro hard 4C. KOSPI -12.06%, KRW 1,505.8/USD, Hyundai -15.8%, Samsung -11.7%, SK Hynix -9.6%.
```

## docs/checkpoints/checkpoint_28a_round184_r13_loop11.md 요약

```md
# Checkpoint 28A Round 184 R13 Loop 11 Cross-archetype Validation

## 반영 내용
- R13 Loop 11 cross-archetype price-validation 라운드를 추가했다.
- Structural success, Stage 2 contract headline, AI/digital event premium, evidence-good-but-price-failed, contract hard 4C, operational trust hard 4C, macro hard 4C를 비교했다.
- Reuters / FT / WSJ / Vogue Business / MarketWatch anchors로 가능한 MFE/MAE 및 event metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- stage3_to_large_MFE_confirmation, revenue/EPS conversion, actual call-off, cash collection, price-path alignment, operational/security trust, macro overlay 가중치 강화
- AI/stablecoin policy-only, contract headline without margin, IPO story, M&A/facility without utilization, good news but price failed, data breach, factory fire, macro energy shock 감점 강화
```

## data/e2r_case_library/cases_r13_loop11_round184.jsonl 초안

```jsonl
{"case_id":"r13_loop11_sk_hynix_structural_success_4b","symbol":"000660","company_name":"SK Hynix","source_sector":"R2","case_type":"structural_success","primary_archetype":"STRUCTURAL_SUCCESS_BUT_4B_WATCH","stage3_date":"2024-06-25","stage4b_date":"2026-05-04/2026-05-14","price_validation":{"price_data_source":"MarketWatch/Reuters reported anchors","stage3_price":222000,"record_high_price":1447000,"mfe_from_stage3_to_record_high_pct":551.8,"asml_euv_order_krw_trn":11.95,"asml_euv_order_usd_bn":7.97,"asml_order_event_return_pct":5.7,"reported_return_2025_pct":274,"reported_return_2026_ytd_pct":200,"minimum_compounded_return_from_start_2025_pct":1022,"market_cap_usd_bn":942,"market_cap_mfe_from_under_100b_pct":842,"price_validation_status":"reported_price_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_structural_rerating","notes":"Stage 3 worked; now 4B-watch due massive MFE and market-cap milestone."}
{"case_id":"r13_loop11_apr_medicube_structural_success_concentration","symbol":"278470","company_name":"APR / Medicube","source_sector":"R5","case_type":"structural_success","primary_archetype":"STRUCTURAL_SUCCESS_BUT_4B_WATCH","stage3_date":"2025-Q4_candidate","stage4b_date":"2025-2026","price_validation":{"price_data_source":"Vogue Business revenue/channel anchors","stage3_price":null,"q4_2025_revenue_usd_mn":440,"q4_2025_revenue_growth_pct":124,"q4_2025_overseas_revenue_usd_mn":362,"q4_2025_overseas_growth_pct":203,"overseas_revenue_share_pct":87,"fy_2025_revenue_usd_bn":1.2,"medicube_fy_2025_revenue_usd_bn":1.1,"medicube_revenue_share_pct":91.7,"tiktok_shop_revenue_usd_mn":102.9,"amazon_prime_day_sales_usd_mn":22,"ulta_store_expansion_count":1400,"price_validation_status":"reported_revenue_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial","rerating_result":"K_beauty_structural_rerating","notes":"Revenue conversion is strong; single-brand/device concentration requires 4B-watch."}
{"case_id":"r13_loop11_samsung_ea_fadhili_contract_stage2_4b","symbol":"028050","company_name":"Samsung E&A","source_sector":"R1/R10","case_type":"success_candidate","primary_archetype":"CONTRACT_HEADLINE_STAGE2_NOT_GREEN","stage2_date":"2024-04-03","stage4b_date":"2024-04-03","price_validation":{"price_data_source":"WSJ reported contract/event anchor","stage3_price":null,"stage2_event_price_krw":26750,"event_mfe_pct":8.5,"implied_prior_price_krw":24654,"kospi_same_context_pct":-1.4,"relative_outperformance_pp":9.9,"contract_value_usd_bn":6.0,"total_fadhili_package_usd_bn":7.7,"contract_share_of_total_pct":77.9,"target_price_krw":35000,"target_upside_from_event_price_pct":30.8,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"EPC_order_stage2_not_green","notes":"Signed mega-order is Stage 2; progress revenue, margin, working capital and cash collection required before Green."}
{"case_id":"r13_loop11_samsung_sds_stablecoin_event_premium","symbol":"018260/377300/LG_CNS/Aton/ME2ON","company_name":"Samsung SDS / stablecoin policy basket","source_sector":"R6/R8","case_type":"overheat","primary_archetype":"AI_CAPITAL_ALLOCATION_EVENT_PREMIUM","stage2_date":"2026-04-15/2025-06","stage4b_date":"2026-04-15/2025-06","price_validation":{"price_data_source":"Reuters/FT event anchors","stage3_price":null,"samsung_sds_event_mfe_pct":20.8,"samsung_sds_relative_outperformance_pp":17.8,"kkr_cb_investment_usd_mn":820,"samsung_sds_existing_cash_krw_trn":6.4,"combined_cash_plus_cb_krw_trn":7.607,"kakao_pay_mfe_month_pct":100,"lg_cns_stablecoin_mfe_month_pct":70,"aton_mfe_month_pct":80,"me2on_mfe_month_pct":200,"issuer_license_confirmed":false,"reserve_income_confirmed":false,"fee_revenue_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence_event_premium","rerating_result":"AI_digital_policy_4B","notes":"AI capital allocation and stablecoin policy moved prices before regulated revenue or recurring AI revenue."}
{"case_id":"r13_loop11_lg_cns_samsung_bio_evidence_good_price_failed","symbol":"LG_CNS/207940","company_name":"LG CNS / Samsung Biologics","source_sector":"R7/R8","case_type":"evidence_good_but_price_failed","primary_archetype":"EVIDENCE_GOOD_BUT_PRICE_FAILED","stage2_date":"2025-02-05/2025-12-21","price_validation":{"price_data_source":"Reuters IPO/facility anchors","stage3_price":null,"lg_cns_ipo_price_krw":61900,"lg_cns_debut_trade_krw":59700,"lg_cns_debut_mae_pct":-3.55,"lg_cns_revenue_1q_3q_2024_krw_trn":4.0,"lg_cns_op_1q_3q_2024_krw_bn":313,"lg_cns_op_margin_pct":7.8,"samsung_bio_gsk_facility_value_usd_mn":280,"samsung_bio_facility_capacity_liters":60000,"samsung_bio_event_mae_pct":-0.4,"kospi_same_context_pct":2.0,"samsung_bio_relative_underperformance_pp":-2.4,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"good_evidence_but_no_fresh_rerating","notes":"Good business evidence but price action failed; wait for revenue/margin/FCF."}
{"case_id":"r13_loop11_lges_lnf_contract_quality_hard_4c","symbol":"373220/066970","company_name":"LG Energy Solution / L&F","source_sector":"R3/R4","case_type":"4c_thesis_break","primary_archetype":"CONTRACT_QUALITY_HARD_4C","stage4c_date":"2025-12","price_validation":{"price_data_source":"Reuters contract-cancellation/value-collapse anchors","stage3_price":null,"lges_ford_cancelled_contract_krw_trn":9.6,"lges_freudenberg_cancelled_contract_krw_trn":3.9,"lges_total_lost_expected_revenue_krw_trn":13.5,"lges_2024_revenue_krw_trn":25.62,"lost_revenue_vs_2024_revenue_pct":52.7,"lnf_initial_contract_value_usd_bn":2.9,"lnf_revised_contract_value_usd":7386,"lnf_contract_value_collapse_pct":99.999745,"price_validation_status":"reported_contract_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"battery_contract_quality_failure","notes":"Contract headlines failed actual call-off/volume; hard 4C."}
{"case_id":"r13_loop11_skt_kumho_operational_trust_hard_4c","symbol":"017670/073240","company_name":"SK Telecom / Kumho Tire","source_sector":"R8/R9","case_type":"4c_thesis_break","primary_archetype":"OPERATIONAL_TRUST_HARD_4C","stage4c_date":"2025-04-28/2025-05-19/2025-08-28","price_validation":{"price_data_source":"Reuters breach/factory-fire anchors","stage3_price":null,"skt_initial_intraday_mae_pct":-8.5,"skt_initial_close_mae_pct":-6.7,"skt_relative_underperformance_pp":-6.8,"skt_users_affected_initial_mn":23,"skt_data_leak_pieces_mn":26.96,"skt_revenue_forecast_cut_krw_bn":800,"skt_security_investment_krw_bn":700,"skt_fine_krw_bn":134,"kumho_event_mae_pct":-8.0,"kumho_gwangju_capacity_mn_tires":12,"kumho_share_of_global_capacity_pct":20,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"operational_trust_break","notes":"Security breach and factory fire are hard operating gates that override growth narratives."}
{"case_id":"r13_loop11_hormuz_iran_macro_hard_4c","symbol":"KOSPI/KRW/005380/005930/000660","company_name":"Hormuz / Iran macro energy shock","source_sector":"R11","case_type":"4c_thesis_break","primary_archetype":"MACRO_GEOPOLITICAL_HARD_4C","stage4c_date":"2026-03-04","price_validation":{"price_data_source":"Reuters/Barron's macro-market anchors","stage3_price":null,"kospi_event_mae_pct":-12.06,"kospi_close":5093.54,"market_cap_wipeout_2d_usd_bn":553.82,"krw_intraday_low_per_usd":1505.8,"hyundai_motor_mae_pct":-15.8,"samsung_electronics_mae_pct":-11.7,"sk_hynix_mae_pct":-9.6,"middle_east_oil_import_dependency_pct":70,"price_validation_status":"reported_market_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"macro_energy_security_hard_4C","notes":"Hormuz/Iran energy shock is hard macro overlay across Korean equities."}
```

## data/sector_taxonomy/score_weight_profiles_round184_r13_loop11_v1.csv 초안

```csv
archetype,stage3_mfe_confirmation,revenue_eps_conversion,commercial_revenue,actual_calloff,cash_collection,price_path_alignment,fresh_rerating_response,operational_trust,security_privacy_trust,macro_overlay,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
STRUCTURAL_SUCCESS_ALIGNED,+5,+5,+5,+4,+4,+5,+4,+3,+2,+2,-1,+4,+3,SK Hynix and APR show true Stage 3 candidates when revenue/EPS conversion and price path align.
STRUCTURAL_SUCCESS_BUT_4B_WATCH,+5,+5,+5,+4,+4,+5,+4,+3,+2,+2,-2,+5,+4,Large MFE or concentration requires 4B-watch even when Stage 3 worked.
CONTRACT_HEADLINE_STAGE2_NOT_GREEN,+2,+2,+2,+5,+5,+3,+4,+3,+1,+1,-5,+5,+5,Samsung E&A shows signed contract is Stage 2 until margin/cash collection confirm.
AI_CAPITAL_ALLOCATION_EVENT_PREMIUM,+2,+3,+3,+1,+2,+3,+5,+3,+2,+2,-5,+5,+4,Samsung SDS KKR event is 4B before recurring AI revenue.
POLICY_DIGITAL_ASSET_PRICE_ONLY,+0,+0,+1,+0,+0,+2,+5,+2,+3,+4,-5,+5,+4,Stablecoin basket rallied before licensing/reserve income/fee revenue.
EVIDENCE_GOOD_BUT_PRICE_FAILED,+2,+3,+3,+2,+2,+5,+5,+3,+2,+2,-4,+4,+3,LG CNS/SamsungBio show good evidence can fail price validation.
CONTRACT_QUALITY_HARD_4C,+0,+0,+0,+5,+5,+0,+0,+2,+1,+2,0,+3,+5,LGES/L&F contract failures are hard 4C.
OPERATIONAL_TRUST_HARD_4C,+0,+0,+0,+0,+0,+0,+0,+5,+5,+2,0,+4,+5,SKT/Kumho show security/factory trust breaks override growth.
MACRO_GEOPOLITICAL_HARD_4C,+0,+0,+0,+0,+0,+0,+0,+3,+2,+5,0,+5,+5,Hormuz/Iran shock is macro overlay hard 4C.
```

---

# 이번 R13 Loop 11 결론

```text
1. SK Hynix는 Stage 3가 제대로 작동한 benchmark다.
   하지만 지금은 Green 추가가 아니라 4B-watch다.

2. APR/Medicube도 구조적 성공 후보다.
   그러나 매출 집중도 91.7% 때문에 concentration 4B-watch가 붙는다.

3. Samsung E&A는 signed mega-order가 있어도 Stage 2다.
   margin/cash collection 전 +8.5%는 4B다.

4. Samsung SDS와 stablecoin basket은 event premium이다.
   AI revenue / regulated revenue 전 가격이 먼저 갔다.

5. LG CNS와 SamsungBio는 evidence_good_but_price_failed다.
   좋은 뉴스가 있어도 가격이 실패하면 Green threshold를 낮추면 안 된다.

6. LGES와 L&F는 contract-quality hard 4C다.
   고객명·계약금액 headline은 actual call-off 없으면 무너진다.

7. SK Telecom과 Kumho Tire는 operational trust hard 4C다.
   보안·공장·안전 사고는 성장논리를 즉시 닫는다.

8. Hormuz/Iran shock은 macro hard 4C다.
   한국 시장에서는 에너지·환율 shock이 모든 섹터 위에 덮인다.
```

한 문장으로 압축하면:

> **R13의 역할은 “좋아 보이는 후보”를 다시 부수는 것이다. Stage 3는 revenue/EPS/FCF와 대형 MFE로 증명되고, 4B는 가격 선반영·event premium·valuation concentration으로 잡히며, 4C는 계약·보안·공장·안전·거시 shock이 실제 손실로 내려올 때 즉시 발동된다.**

* [Reuters](https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/sk-hynix-shares-rally-12-after-us-tech-firms-signal-strong-spending-ai-data-2026-05-04/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/south-koreas-lf-says-value-battery-material-supply-deal-with-tesla-cut-7386-2025-12-29/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/south-korea-agency-fines-sk-telecom-97-million-over-major-data-leak-2025-08-28/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/korean-stocks-dive-won-hits-17-year-low-iran-conflict-2026-03-04/?utm_source=chatgpt.com)

[1]: https://www.marketwatch.com/story/sk-hynix-s-hbm-dominance-higher-chip-prices-could-lift-earnings-market-talk-6508cbf8?utm_source=chatgpt.com "SK Hynix's HBM Dominance, Higher Chip Prices Could Lift Earnings -- Market Talk"
[2]: https://www.vogue.com/article/how-k-beauty-brand-medicube-pulled-off-its-global-breakout?utm_source=chatgpt.com "How K-Beauty Brand Medicube Pulled Off Its Global Breakout"
[3]: https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com "Samsung E&A Shares Rise on $6 Billion Saudi Contract Win"
[4]: https://www.reuters.com/world/asia-pacific/kkr-buy-820-million-samsung-sds-convertible-bonds-shares-jump-20-2026-04-15/?utm_source=chatgpt.com "KKR to buy $820 million of Samsung SDS convertible bonds, shares jump 20%"
[5]: https://www.reuters.com/technology/skorean-tech-services-firm-lg-cns-falls-stock-market-debut-2025-02-05/?utm_source=chatgpt.com "South Korean tech services firm LG CNS drops in market debut"
[6]: https://www.reuters.com/business/energy/lg-energy-solution-cancels-39-trillion-won-battery-order-with-freudenberg-2025-12-26/?utm_source=chatgpt.com "LG Energy Solution cancels 3.9 trillion won battery order with Freudenberg"
[7]: https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/?utm_source=chatgpt.com "SK Telecom shares plunge after data breach due to cyberattack"
[8]: https://www.reuters.com/world/asia-pacific/korean-stocks-dive-won-hits-17-year-low-iran-conflict-2026-03-04/?utm_source=chatgpt.com "Korean stocks record worst day, won sinks on Iran conflict"

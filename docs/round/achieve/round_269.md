순서상 이번은 **R13 Loop 12 — Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리**다.

```text
round = R13 Loop 12
round_id = round_197
large_sector = CROSS_ARCHETYPE_REDTEAM_PRICE_VALIDATION
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R1 Loop 13
```

이번 R13은 R1~R12 Loop 12 전체를 다시 부수는 라운드다. 목적은 새 테마를 늘리는 게 아니라, **Stage 3를 너무 쉽게 줬는지, 4B가 너무 늦게 떴는지, 4C hard gate가 실제 하락 전에 작동했는지**를 교정하는 것이다.

---

# 1. 이번 라운드 대섹터

```text
R13 = Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리
```

R13의 핵심 질문은 세 개다.

```text
1. Stage 3가 실제 MFE를 만들었나?
2. 4B가 고점 전후에서 과열·선반영을 잡았나?
3. 4C가 계약취소·보안사고·안전사고·매크로 쇼크를 큰 하락 전에 막았나?
```

---

# 2. 대상 canonical archetype

```text
TRUE_STRUCTURAL_RERATING
STRUCTURAL_SUCCESS_NOW_4B
CONTRACT_HEADLINE_STAGE2_NOT_GREEN
POLICY_CAPEX_FALSE_POSITIVE
DIGITAL_POLICY_PRICE_ONLY
PLATFORM_TRUST_4C_WATCH
CONTRACT_QUALITY_HARD_4C
OPERATIONAL_TRUST_HARD_4C
MACRO_GEOPOLITICAL_HARD_4C
```

---

# 3. deep sub-archetype

```text
성공 benchmark:
- SK Hynix HBM / AI memory structural rerating
- Samyang Foods Buldak export / ASP / capacity

Stage 2 but not Green:
- Samsung E&A Saudi Fadhili EPC
- Naver Financial / Dunamu platform M&A
- Samsung / strike risk as systemic labor 4C-watch

False positive / event premium:
- Hyundai Steel U.S. policy CAPEX
- Stablecoin policy basket
- Kyochon / Cherrybro / celebrity event

Hard 4C:
- LGES Ford/Freudenberg contract cancellation
- SK Telecom cybersecurity breach
- Jeju Air fatal crash
- Middle East / Iran energy macro shock
```

---

# 4. 국장 신규 후보 case

## Case A — SK하이닉스 `structural_success + now 4B-watch`

```text
symbol = 000660
case_type = structural_success + 4B-watch
archetype = TRUE_STRUCTURAL_RERATING / STRUCTURAL_SUCCESS_NOW_4B
```

### stage date

```text
Stage 1:
2024-05~06
- HBM sold-out / AI memory bottleneck
- DRAM price recovery

Stage 2:
2024-06-25
- Nomura raises 2024 OP estimate to 30T won
- 2025 OP estimate to 53T won
- target price 290,000 won
- shares around 222,000 won

Stage 3:
2024-06-25 candidate
- HBM dominance + DRAM price revision + OP revision

Stage 3 validation:
2024-07-25
- Q2 OP 5.47T won, highest since 2018
- revenue 16.4T won, +125% YoY
- HBM shipments expected to more than double next year

Stage 4B:
2026-05-14
- 2025 return +274%
- 2026 return > +200%
- market cap about $942B
- under $100B about 16 months earlier
```

SK하이닉스는 R13에서 가장 깨끗한 **Stage 3 성공 benchmark**다. 2024년 6월에는 HBM 지배력과 메모리 가격 상승을 근거로 OP revision이 있었고, 당시 주가 anchor는 222,000원이었다. 2024년 7월에는 Q2 영업이익이 5.47조 원으로 2018년 이후 최고였고, 2026년에는 시총이 약 $942B까지 올라 2025년 +274%, 2026년 +200% 이상 상승했다. 이제 이 case는 Green 추가가 아니라 **4B-watch**다. ([마켓워치][1])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / Reuters reported anchors

entry_date:
2024-06-25

stage3_price:
222,000 won

target_price:
290,000 won

target_upside:
290,000 / 222,000 - 1
= +30.6%

2024_OP_estimate:
30T won

2025_OP_estimate:
53T won

Q2_2024_OP:
5.47T won

Q2_2024_revenue:
16.4T won

Q2_2024_revenue_growth:
+125% YoY

reported_2025_return:
+274%

reported_2026_return:
> +200%

market_cap_2026-05:
about $942B

market_cap_from_under_100B:
942 / 100 - 1
= +842% 이상

MFE_30D / 90D / 180D / 1Y / 2Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned
rerating_result = true_structural_rerating
current_state = 4B_watch
```

---

## Case B — Samyang Foods `structural_success_candidate`

```text
symbol = 003230
case_type = structural_success_candidate
archetype = TRUE_STRUCTURAL_RERATING
```

### stage date

```text
Stage 1:
2024
- Buldak global export demand
- ASP 상승
- U.S. / Europe shipment 증가

Stage 2:
2024-06-14
- Kiwoom raises 2Q OP estimate to 81.2B won
- +84% YoY operating profit estimate
- target price 830,000 won
- shares close +5.7% at 647,000 won

Stage 3:
2024-06-14 candidate
- export + ASP + capacity + OP revision이 동시에 확인됨

Stage 4B:
single-SKU / Buldak concentration premium 과열 시 watch
```

Samyang은 R5/R12의 K-food benchmark다. 2024년 6월 14일 Kiwoom은 Buldak 수출, ASP 상승, U.S./Europe shipment 증가, 생산능력 확대를 근거로 2Q 영업이익 추정치를 812억 원으로 올렸고, 주가는 647,000원에 마감했다. 이건 단순 K-food label이 아니라 **수출·ASP·capacity·OP revision**이 같이 붙은 Stage 3 후보로 본다. ([마켓워치][2])

### 실제 가격경로 검증

```text
price_data_source:
MarketWatch / WSJ Market Talk reported anchor

entry_date:
2024-06-14

stage3_price:
647,000 won

event_MFE_1D:
+5.7%

implied_prior_close:
647,000 / 1.057
= 611,921 won

target_price:
830,000 won

target_upside_from_stage3_price:
830,000 / 647,000 - 1
= +28.3%

Q2_OP_estimate:
81.2B won

OP_growth_estimate:
+84% YoY

MFE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search

MAE_30D / 90D / 180D / 1Y:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = aligned_partial
rerating_result = K_food_export_ASP_capacity_rerating_candidate
risk = single_SKU_4B_watch
```

---

## Case C — Samsung E&A Fadhili `contract Stage 2, not Green`

```text
symbol = 028050
case_type = success_candidate + event_premium
archetype = CONTRACT_HEADLINE_STAGE2_NOT_GREEN
```

### stage date

```text
Stage 1:
2024-04-03
- Saudi gas infrastructure expansion
- EPC order-cycle headline

Stage 2:
2024-04-03
- Samsung E&A wins estimated $6B Fadhili contract
- Aramco total project $7.7B
- gas processing capacity +60%
- shares +8.5% to 26,750 won
- KOSPI -1.4%

Stage 3:
없음
- signed mega-order는 Stage 2
- progress revenue / EPC margin / working capital / cash collection 전 Green 금지

Stage 4B:
2024-04-03
- contract headline만으로 +8.5% rally
```

Samsung E&A는 “수주 headline = Green”을 막는 기준점이다. 약 $6B Saudi Aramco Fadhili contract는 강한 Stage 2지만, 주가가 당일 +8.5% 뛰는 동안 아직 공정률·원가율·운전자본·현금회수는 확인되지 않았다. ([월스트리트저널][3])

### 실제 가격경로 검증

```text
price_data_source:
WSJ reported contract and event-return anchor

entry_date:
N/A, no Stage 3

stage3_price:
N/A

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

total_project_value:
$7.7B

contract_share_of_total:
6.0 / 7.7
= 77.9%

target_price:
35,000 won

target_upside_from_event_price:
35,000 / 26,750 - 1
= +30.8%
```

### alignment

```text
score_price_alignment = event_premium_success_candidate
rerating_result = EPC_order_stage2_not_green
stage_failure_type = contract_headline_without_margin_cash
```

---

## Case D — Hyundai Steel U.S. plant `false_positive_score`

```text
symbol = 004020
case_type = failed_rerating
archetype = POLICY_CAPEX_FALSE_POSITIVE
```

### stage date

```text
Stage 1:
2025-03-24
- U.S. tariff pressure
- Hyundai Motor Group U.S. investment package
- low-carbon steel localization

Stage 2:
2025-03-25
- $5.8B Louisiana steel plant plan
- part of $21B U.S. package
- tariff hedge / U.S. localization story

Stage 4C-watch:
2025-04-22
- stock lost 21.2% since announcement
- POSCO -18.3%
- KOSPI -5.5%
- funding details unclear
- project may be political signaling
```

Hyundai Steel은 R4/R10의 대표 false positive다. 미국 공장, tariff hedge, low-carbon steel이라는 문장은 좋아 보였지만, 발표 후 주가는 -21.2%까지 밀렸고 KOSPI 대비 -15.7pp 언더퍼폼했다. Reuters는 투자자들이 funding detail과 장기 tariff benefit을 의심했다고 보도했다. ([Reuters][4])

### 실제 가격경로 검증

```text
price_data_source:
Reuters U.S. steel plant / investor backlash anchor

stage3_price:
N/A

plant_investment:
$5.8B

group_U.S._investment_package:
$21B

post_announcement_drawdown:
-21.2%

POSCO_same_period:
-18.3%

KOSPI_same_period:
-5.5%

relative_underperformance_vs_KOSPI:
-21.2 - (-5.5)
= -15.7pp

funding_plan:
50% borrowing, remaining funding unclear at that stage

possible_POSCO_equity:
under discussion

MFE:
N/A

MAE:
reported anchor only
```

### alignment

```text
score_price_alignment = false_positive_score
rerating_result = policy_CAPEX_failed_rerating
stage_failure_type = CAPEX_without_ROI_and_funding
```

---

## Case E — Stablecoin basket `overheat / price_moved_without_evidence`

```text
symbols = Kakao Pay / LG CNS / Aton / ME2ON / KRW
case_type = overheat + 4C-watch
archetype = DIGITAL_POLICY_PRICE_ONLY / STABLECOIN_FX_POLICY_OVERHEAT
```

### stage date

```text
Stage 1:
2025-06
- won stablecoin policy expectation
- digital-asset reform
- retail leverage expansion

Stage 4B:
2025-06
- Kakao Pay >2x
- LG CNS +70%
- Aton +80%
- ME2ON 3x
- margin loans 20.5T won

Stage 4C-watch:
2025-06~07
- issuer license / reserve income / fee revenue not confirmed
- BOK FX / capital-flow concern
- proposed issuer equity threshold only 500M won
- Q1 stablecoin-related capital outflow context >$19B
```

Stablecoin basket은 R6/R11의 대표 `price_moved_without_evidence`다. 관련주들은 실제 issuer license, reserve income, fee revenue가 확인되기 전에 70%~3배 움직였고, 동시에 BOK는 비은행 stablecoin 발행이 통화정책과 자본유출 관리에 혼란을 줄 수 있다고 경고했다. ([Financial Times][5])

### 실제 가격경로 검증

```text
price_data_source:
FT / Reuters stablecoin policy and FX-risk anchors

stage3_price:
N/A

Kakao_Pay_MFE:
> +100%

LG_CNS_MFE:
+70%

Aton_MFE:
+80%

ME2ON_MFE:
+200%

margin_loans:
20.5T won

proposed_minimum_issuer_equity:
500M won

capital_outflow_context:
>$19B

issuer_license_confirmed:
false

reserve_income_confirmed:
false

fee_revenue_confirmed:
false

MFE_30D / 90D:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = price_moved_without_evidence
rerating_result = stablecoin_policy_overheat
stage_failure_type = 4B_before_regulated_revenue
```

---

## Case F — NAVER Financial / Dunamu `platform Stage 2 + trust 4C-watch`

```text
symbol = 035420
case_type = success_candidate + event_premium + 4C-watch
archetype = DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE
```

### stage date

```text
Stage 1:
2025-11-27
- NAVER Financial / Dunamu all-stock deal
- Upbit / Naver Pay / digital asset synergy

Stage 2:
2025-11-27
- deal value 15.13T won / $10.27B
- exchange ratio 2.54 Naver Financial shares per Dunamu share
- Upbit market share about 70%

Stage 4B:
2025-11-27
- NAVER initially +7%+

Stage 4C-watch:
2025-11-27
- abnormal withdrawal 54B won from Upbit
- NAVER later -4.2%
- Upbit to cover loss with own assets

Stage 3:
없음
- closing / regulatory approval / trust recovery / revenue bridge 전 Green 금지
```

NAVER/Dunamu는 “플랫폼 M&A가 좋아도 trust gate가 먼저”라는 R8/R6 calibration이다. 거래 규모는 15.13조 원으로 크고 Upbit 점유율도 높지만, 같은 날 540억 원 abnormal withdrawal이 보도되면서 NAVER 주가는 +7%에서 -4.2%로 뒤집혔다. ([Reuters][6])

### 실제 가격경로 검증

```text
price_data_source:
Reuters deal / event-return / trust-risk anchor

stage3_price:
N/A

deal_value:
15.13T won / $10.27B

exchange_ratio:
2.54 Naver Financial shares per Dunamu share

Upbit_market_share:
about 70%

event_initial_MFE:
> +7%

event_later_MAE:
-4.2%

event_swing:
-11.2pp

abnormal_withdrawal:
54B won

loss_coverage:
Upbit to cover using own assets
```

### alignment

```text
score_price_alignment = event_premium_trust_watch
rerating_result = digital_asset_platform_merger_watch
stage_failure_type = platform_stage2_with_exchange_trust_4C_watch
```

---

## Case G — LG Energy Solution `contract-quality hard 4C`

```text
symbol = 373220
case_type = 4C-thesis-break
archetype = CONTRACT_QUALITY_HARD_4C
```

### stage date

```text
Stage 1:
2024~2025
- EV battery supply backlog headline
- Ford / Freudenberg customer exposure

Stage 4C:
2025-12
- Ford terminates 9.6T won EV battery supply deal
- Freudenberg cancels 3.9T won battery order
- total expected revenue loss 13.5T won
- LGES 2024 revenue 25.62T won

Stage 3:
없음
- contract headline이 actual call-off로 닫히지 못함
```

LGES는 R3의 가장 강한 hard 4C다. Ford와 Freudenberg 계약 취소로 13.5조 원 기대매출이 사라졌고, 이는 2024년 매출 25.62조 원의 절반 이상이다. 이 case는 “고객명·계약금액 headline”만으로 Stage 3를 주면 안 된다는 기준이다. ([Reuters][7])

### 실제 가격경로 검증

```text
price_data_source:
Reuters contract-cancellation anchor

stage3_price:
N/A

Ford_cancelled_contract:
9.6T won

Freudenberg_cancelled_contract:
3.9T won

total_lost_expected_revenue:
13.5T won

LGES_2024_revenue:
25.62T won

lost_revenue_vs_2024_revenue:
13.5 / 25.62
= 52.7%

MFE:
N/A

MAE:
price_data_unavailable_after_deep_search
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = battery_contract_quality_failure
stage_failure_type = hard_4C
```

---

## Case H — Hard 4C reference pack: Jeju Air / SK Telecom / Middle East energy shock

```text
symbols = 089590 / 017670 / KOSPI / KRW
case_type = 4C-thesis-break
archetype = OPERATIONAL_TRUST_HARD_4C / MACRO_GEOPOLITICAL_HARD_4C
```

### stage date

```text
Jeju Air Stage 4C:
2024-12-30
- fatal crash, 179 deaths
- shares as much as -15.7% to 6,920 won
- market cap wipeout up to 95.7B won

SK Telecom Stage 4C:
2025-04-28 / 2025-07-04 / 2025-08-28
- cyberattack data breach
- shares -8.5% intraday, close -6.7%
- 23M subscribers USIM replacement
- 26.96M pieces of user data leaked
- 700B won data-protection investment
- 2025 revenue forecast cut by 800B won
- 134B won fine

Middle East / Iran Stage 4C:
2026-03-04
- KOSPI -12.06%
- close 5,093.54
- market cap wipeout $553.82B over two days
- KRW touches 1,505.8/USD
- Hyundai -15.8%, Samsung -11.7%, SK Hynix -9.6%
```

이 pack은 R13의 hard gate 기준이다. Jeju Air는 안전 신뢰가 깨진 case, SKT는 데이터·보안 신뢰가 비용과 매출전망 하향으로 내려온 case, Middle East/Iran은 특정 종목이 아니라 시장 전체를 덮은 macro hard 4C다. 각각 -15.7%, -8.5%/-6.7%, KOSPI -12.06%라는 가격경로가 확인된다. ([Reuters][8])

### 실제 가격경로 검증

```text
price_data_source:
Reuters hard-4C reported anchors

Jeju_Air:
event_low_price = 6,920 won
event_intraday_MAE = -15.7%
market_cap_wipeout = 95.7B won

SK_Telecom:
initial_intraday_MAE = -8.5%
initial_close_MAE = -6.7%
KOSPI_same_context = +0.1%
relative_underperformance = -6.8pp
affected_users = 23M
leaked_data_pieces = 26.96M
data_protection_investment = 700B won
revenue_forecast_cut = 800B won
fine = 134B won

Middle_East_Iran:
KOSPI_MAE = -12.06%
KOSPI_close = 5,093.54
market_cap_wipeout_2D = $553.82B
KRW_low = 1,505.8/USD
Hyundai_Motor_MAE = -15.8%
Samsung_Electronics_MAE = -11.7%
SK_Hynix_MAE = -9.6%
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = hard_4C_reference_pack
stage_failure_type = safety_security_macro_hard_gate
```

---

# 5. 이번 R13 case별 stage date 요약

| case                 | Stage 1         | Stage 2                | Stage 3              | Stage 4B         | Stage 4C          |
| -------------------- | --------------- | ---------------------- | -------------------- | ---------------- | ----------------- |
| SK Hynix             | 2024-05~06      | 2024-06-25             | 2024-06-25 candidate | 2026-05-14       | N/A               |
| Samyang Foods        | 2024 export/ASP | 2024-06-14             | 2024-06-14 candidate | single-SKU watch | N/A               |
| Samsung E&A          | 2024-04-03      | 2024-04-03             | N/A                  | 2024-04-03       | N/A               |
| Hyundai Steel        | 2025-03         | 2025-03-25             | N/A                  | N/A              | 2025-04-22 watch  |
| Stablecoin basket    | 2025-06         | N/A                    | N/A                  | 2025-06          | FX 4C-watch       |
| NAVER/Dunamu         | 2025-11-27      | 2025-11-27             | N/A                  | 2025-11-27       | 2025-11-27 watch  |
| LGES                 | 2024~2025       | weak contract headline | N/A                  | N/A              | 2025-12           |
| Jeju/SKT/Middle East | varies          | N/A                    | N/A                  | N/A              | hard 4C confirmed |

---

# 6. 실제 가격경로 검증 총괄

| case                 |               anchor price / return | MFE / MAE 해석                                | below_stage3_price_flag |
| -------------------- | ----------------------------------: | ------------------------------------------- | ----------------------- |
| SK Hynix             | 222,000원 → market cap $942B context | Stage 3 gate 성공, now 4B                     | unavailable             |
| Samyang Foods        |                     647,000원, +5.7% | export/ASP/capacity evidence와 가격 반응 aligned | unavailable             |
| Samsung E&A          |                      26,750원, +8.5% | contract headline event premium             | N/A                     |
| Hyundai Steel        |              announcement 이후 -21.2% | false_positive_score                        | N/A                     |
| Stablecoin basket    |             Kakao Pay >2x, ME2ON 3x | price_moved_without_evidence                | N/A                     |
| NAVER/Dunamu         |                         +7% → -4.2% | trust gate가 event premium을 즉시 되돌림           | N/A                     |
| LGES                 |              lost revenue 13.5T won | contract hard 4C                            | N/A                     |
| Jeju/SKT/Middle East |  -15.7%, -8.5%/-6.7%, KOSPI -12.06% | hard 4C 작동                                  | N/A                     |

```text
full_adjusted_ohlc_status:
- Reuters / FT / WSJ / MarketWatch reported anchors 기준으로 직접 계산
- 30D / 90D / 180D / 1Y / 2Y full adjusted OHLC는 이번 pass에서 unavailable
- 계산 불가능한 숫자는 만들지 않았고, patch row에는 price_validation_status로 명시
```

---

# 7. score-price alignment 판정

```text
aligned:
- SK Hynix
- Samyang Foods

aligned_but_now_4B:
- SK Hynix

success_candidate_stage2_not_green:
- Samsung E&A
- NAVER/Dunamu
- Samsung strike / AI fiscal room / policy relief cases from R11

false_positive_score:
- Hyundai Steel U.S. CAPEX

price_moved_without_evidence:
- Stablecoin basket
- Kyochon / Cherrybro Jensen event
- policy CAPEX rallies before ROI

event_premium:
- Samsung E&A contract rally
- Stablecoin basket
- NAVER/Dunamu initial +7%
- KOSPI 7,000 confidence event

thesis_break:
- LGES contract cancellations
- Jeju Air crash
- SK Telecom breach
- Middle East / Iran macro shock

thesis_break_watch:
- Samsung strike
- NAVER/Dunamu abnormal withdrawal
- rare-earth end-use restrictions
- construction safety regulation
```

---

# 8. 점수비중 교정

## 올릴 축

```text
stage3_evidence_to_price_alignment +5
revenue_EPS_FCF_conversion +5
actual_calloff_or_delivery +5
cash_collection_quality +5
operating_leverage +4
platform_trust +5
safety_security_trust +5
macro_energy_FX_overlay +5
hard_4C_prevention +5
```

### 이유

SK하이닉스와 Samyang은 evidence가 가격과 맞았다. 반면 Samsung E&A는 계약 headline만으로는 아직 Stage 3가 아니고, Hyundai Steel은 policy CAPEX가 오히려 -21.2% false positive가 됐다. Stablecoin과 NAVER/Dunamu는 규제수익·trust gate가 핵심이고, LGES·Jeju·SKT·Middle East는 hard 4C가 수익률을 즉시 꺾었다.

## 내릴 축

```text
contract_headline_only -5
policy_CAPEX_without_ROI -5
stablecoin_policy_theme_only -5
M&A_without_trust_or_closing -4
IPO_or_event_pop_only -5
single_product_or_single_theme_concentration -4
unconfirmed_revenue_bridge -5
data_breach_or_safety_failure -5
macro_shock_unhedged -5
```

### 이유

Samsung E&A는 signed mega-order라도 margin/cash 전 Green이 아니다. Hyundai Steel은 미국 CAPEX가 funding/ROI 없이 발표되면 false positive가 된다. Stablecoin은 license·reserve income 전 2~3배 상승했다. NAVER/Dunamu는 M&A와 동시에 abnormal withdrawal이 발생했다. LGES·SKT·Jeju·Middle East는 hard gate가 아닌 일반 RedTeam으로 처리하면 너무 늦다.

## Green gate 강화 조건

```text
공통 Stage 3-Green 필수:
1. revenue / EPS / FCF conversion 확인
2. price path가 evidence 이후 따라옴
3. contract는 actual call-off / delivery / margin / cash collection 확인
4. platform은 trust / data / security issue 없음
5. policy는 법/예산/계약/수익모델로 닫힘
6. CAPEX는 ROI / funding / utilization 확인
7. 4B overheat signal 없음
8. hard 4C 없음
```

## 4B 조기감지 조건

```text
4B-watch:
- Stage 3 이후 3~5배 이상 상승
- market-cap milestone headline화
- 계약 발표일 +5~10% 급등
- 정책/스테이블코인/AI fiscal story로 2~3배 상승
- M&A announcement 후 regulatory/trust gate 미확인
- IPO / celebrity / policy event pop
- 수익모델 없이 index/sector FOMO로 상승
```

## 4C hard gate 조건

```text
hard_4C:
- contract cancellation / value collapse
- data breach / security failure
- fatal safety accident
- exchange abnormal withdrawal / hack
- macro energy chokepoint shock
- FX disorderly depreciation
- labor strike that threatens national exports
- legal block on final contract
- CAPEX funding failure
```

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 10. 레포 반영용 patch-ready 출력

## docs/round/round_197.md 요약

```md
# R13 Loop 12. Cross-archetype RedTeam / 4B / Price Validation

이번 라운드는 R1~R12 Loop 12 전체를 다시 검문한 R13 price-validation 라운드다.

핵심 결론:
- SK Hynix is the clearest Stage 3 success benchmark. 2024-06-25 stage3 anchor was 222,000 won with OP revision to 30T won for 2024 and 53T won for 2025. By 2026-05, market cap was about $942B after +274% in 2025 and >+200% in 2026. Current state is 4B-watch.
- Samyang Foods is R5/R12 K-food aligned candidate. Stage3 anchor 647,000 won, +5.7%, target 830,000 won, Q2 OP estimate +84% YoY. Single-SKU concentration remains 4B-watch.
- Samsung E&A Fadhili is contract Stage 2, not Green. Event price 26,750 won, +8.5%, contract about $6B, but progress revenue, margin and cash collection are required.
- Hyundai Steel U.S. plant is policy CAPEX false positive. Stock lost -21.2% since announcement vs KOSPI -5.5%; funding and ROI were unclear.
- Stablecoin basket is price_moved_without_evidence. Kakao Pay >2x, LG CNS +70%, Aton +80%, ME2ON 3x before issuer license, reserve income or fee revenue.
- NAVER/Dunamu is platform M&A Stage 2 plus trust 4C-watch. Deal value 15.13T won; Naver initially +7% but later -4.2% after 54B won abnormal withdrawal from Upbit.
- LGES is contract-quality hard 4C. Ford and Freudenberg cancellations removed 13.5T won expected revenue, 52.7% of 2024 revenue.
- Hard 4C reference pack: Jeju Air crash, SK Telecom breach, Middle East/Iran energy shock. These confirm safety/security/macro hard gates.
```

## docs/checkpoints/checkpoint_28a_round197_r13_loop12.md 요약

```md
# Checkpoint 28A Round 197 R13 Loop 12 Cross-archetype Price Validation

## 반영 내용
- R1~R12 Loop 12 전체를 cross-archetype 관점에서 재검증했다.
- Stage 3 success, contract Stage 2, policy CAPEX false positive, stablecoin overheat, platform trust gate, contract hard 4C, operational hard 4C, macro hard 4C를 비교했다.
- Reuters / FT / WSJ / MarketWatch reported anchors로 가능한 event MFE/MAE와 가격 anchor를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- revenue/EPS/FCF conversion, actual call-off/delivery, cash collection, price-path alignment, platform trust, safety/security trust, macro energy/FX overlay 가중치 강화
- contract headline-only, policy CAPEX without ROI, stablecoin theme-only, M&A without trust/closing, IPO/event pop-only, data breach/safety failure 감점 강화
```

## data/e2r_case_library/cases_r13_loop12_round197.jsonl 초안

```jsonl
{"case_id":"r13_loop12_sk_hynix_true_stage3_now_4b","symbol":"000660","company_name":"SK Hynix","case_type":"structural_success","primary_archetype":"TRUE_STRUCTURAL_RERATING","stage2_date":"2024-06-25","stage3_date":"2024-06-25_candidate","stage4b_date":"2026-05-14","price_validation":{"price_data_source":"MarketWatch/Reuters reported anchors","stage3_price_krw":222000,"target_price_krw":290000,"target_upside_pct":30.6,"op_estimate_2024_krw_trn":30,"op_estimate_2025_krw_trn":53,"q2_2024_op_krw_trn":5.47,"q2_2024_revenue_krw_trn":16.4,"q2_2024_revenue_growth_pct":125,"reported_return_2025_pct":274,"reported_return_2026_min_pct":200,"market_cap_2026_usd_bn":942,"market_cap_mfe_from_under_100b_pct":842,"price_validation_status":"reported_anchor_not_full_ohlc"},"score_price_alignment":"aligned","rerating_result":"true_structural_rerating","notes":"Stage 3 worked; now 4B-watch due massive MFE and market-cap milestone."}
{"case_id":"r13_loop12_samyang_kfood_export_stage3_candidate","symbol":"003230","company_name":"Samyang Foods","case_type":"structural_success_candidate","primary_archetype":"TRUE_STRUCTURAL_RERATING","stage3_date":"2024-06-14_candidate","price_validation":{"price_data_source":"MarketWatch/WSJ Market Talk anchor","stage3_price_krw":647000,"event_mfe_1d_pct":5.7,"implied_prior_close_krw":611921,"target_price_krw":830000,"target_upside_pct":28.3,"q2_op_estimate_krw_bn":81.2,"op_growth_estimate_pct":84,"price_validation_status":"reported_anchor_not_full_ohlc"},"score_price_alignment":"aligned_partial","rerating_result":"K_food_export_ASP_capacity_rerating_candidate","notes":"Export, ASP, capacity and OP revision aligned; single-SKU risk remains 4B-watch."}
{"case_id":"r13_loop12_samsung_ea_fadhili_contract_stage2","symbol":"028050","company_name":"Samsung E&A","case_type":"event_premium","primary_archetype":"CONTRACT_HEADLINE_STAGE2_NOT_GREEN","stage2_date":"2024-04-03","stage4b_date":"2024-04-03","price_validation":{"price_data_source":"WSJ contract/event-return anchor","stage3_price":null,"event_price_krw":26750,"event_mfe_pct":8.5,"implied_prior_price_krw":24654,"kospi_same_context_pct":-1.4,"relative_outperformance_pp":9.9,"contract_value_usd_bn":6.0,"total_project_value_usd_bn":7.7,"contract_share_pct":77.9,"target_price_krw":35000,"target_upside_pct":30.8,"price_validation_status":"reported_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_success_candidate","rerating_result":"EPC_contract_stage2_not_green","notes":"Signed contract is Stage 2; progress revenue, margin, working capital and cash collection required."}
{"case_id":"r13_loop12_hyundai_steel_us_capex_false_positive","symbol":"004020","company_name":"Hyundai Steel","case_type":"failed_rerating","primary_archetype":"POLICY_CAPEX_FALSE_POSITIVE","stage2_date":"2025-03-25","stage4c_date":"2025-04-22_watch","price_validation":{"price_data_source":"Reuters investor-backlash anchor","stage3_price":null,"plant_investment_usd_bn":5.8,"group_us_package_usd_bn":21,"post_announcement_drawdown_pct":-21.2,"posco_same_period_pct":-18.3,"kospi_same_period_pct":-5.5,"relative_underperformance_vs_kospi_pp":-15.7,"funding_plan":"50% borrowing; remaining funding unclear at that stage","price_validation_status":"reported_anchor_not_full_ohlc"},"score_price_alignment":"false_positive_score","rerating_result":"policy_CAPEX_failed_rerating","notes":"Policy CAPEX without funding/ROI failed price validation."}
{"case_id":"r13_loop12_stablecoin_policy_overheat","symbol":"KakaoPay/LG_CNS/Aton/ME2ON/KRW","company_name":"Stablecoin policy basket","case_type":"overheat","primary_archetype":"DIGITAL_POLICY_PRICE_ONLY","stage4b_date":"2025-06","stage4c_date":"FX_watch","price_validation":{"price_data_source":"FT/Reuters stablecoin policy and FX-risk anchors","stage3_price":null,"kakao_pay_mfe_pct":100,"lg_cns_mfe_pct":70,"aton_mfe_pct":80,"me2on_mfe_pct":200,"margin_loans_krw_trn":20.5,"proposed_issuer_equity_krw_mn":500,"capital_outflow_context_usd_bn":19,"issuer_license_confirmed":false,"reserve_income_confirmed":false,"fee_revenue_confirmed":false,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"price_moved_without_evidence","rerating_result":"stablecoin_policy_overheat","notes":"Stablecoin policy moved prices before regulated revenue and before FX gate cleared."}
{"case_id":"r13_loop12_naver_dunamu_platform_trust_watch","symbol":"035420","company_name":"NAVER / NAVER Financial / Dunamu","case_type":"success_candidate_4c_watch","primary_archetype":"DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE","stage2_date":"2025-11-27","stage4b_date":"2025-11-27","stage4c_date":"2025-11-27_watch","price_validation":{"price_data_source":"Reuters deal/event-return/trust-risk anchor","stage3_price":null,"deal_value_krw_trn":15.13,"deal_value_usd_bn":10.27,"exchange_ratio":2.54,"upbit_market_share_pct":70,"event_initial_mfe_pct":7,"event_later_mae_pct":-4.2,"event_swing_pp":-11.2,"abnormal_withdrawal_krw_bn":54,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_trust_watch","rerating_result":"digital_asset_platform_merger_watch","notes":"M&A is Stage 2; abnormal withdrawal creates platform trust 4C-watch."}
{"case_id":"r13_loop12_lges_contract_quality_hard_4c","symbol":"373220","company_name":"LG Energy Solution","case_type":"4c_thesis_break","primary_archetype":"CONTRACT_QUALITY_HARD_4C","stage4c_date":"2025-12","price_validation":{"price_data_source":"Reuters contract-cancellation anchor","stage3_price":null,"ford_cancelled_contract_krw_trn":9.6,"freudenberg_cancelled_contract_krw_trn":3.9,"total_lost_expected_revenue_krw_trn":13.5,"lges_2024_revenue_krw_trn":25.62,"lost_revenue_vs_2024_revenue_pct":52.7,"price_validation_status":"reported_contract_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"battery_contract_quality_failure","notes":"Contract headline failed actual call-off; hard 4C."}
{"case_id":"r13_loop12_hard_4c_reference_pack_jeju_skt_macro","symbol":"089590/017670/KOSPI/KRW","company_name":"Jeju Air / SK Telecom / Middle East-Iran shock","case_type":"4c_thesis_break","primary_archetype":"OPERATIONAL_TRUST_AND_MACRO_HARD_4C","stage4c_date":"2024-12-30/2025-04-28/2026-03-04","price_validation":{"price_data_source":"Reuters hard-4C anchors","jeju_event_low_price_krw":6920,"jeju_intraday_mae_pct":-15.7,"jeju_market_cap_wipeout_krw_bn":95.7,"skt_intraday_mae_pct":-8.5,"skt_close_mae_pct":-6.7,"skt_relative_underperformance_pp":-6.8,"skt_affected_users_mn":23,"skt_leaked_data_pieces_mn":26.96,"skt_revenue_forecast_cut_krw_bn":800,"skt_fine_krw_bn":134,"kospi_mae_pct":-12.06,"kospi_close":5093.54,"krw_low_per_usd":1505.8,"hyundai_motor_mae_pct":-15.8,"samsung_mae_pct":-11.7,"sk_hynix_mae_pct":-9.6,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"safety_security_macro_hard_gate","notes":"Safety, cybersecurity and macro energy shock confirm hard 4C gates."}
```

## data/sector_taxonomy/score_weight_profiles_round197_r13_loop12_v1.csv 초안

```csv
archetype,stage3_evidence_price_alignment,revenue_eps_fcf,actual_calloff_delivery,cash_collection,operating_leverage,platform_trust,safety_security_trust,macro_energy_fx_overlay,hard_4c_prevention,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
TRUE_STRUCTURAL_RERATING,+5,+5,+4,+4,+5,+2,+2,+2,+3,-1,+4,+3,SK Hynix and Samyang show evidence-to-price alignment.
STRUCTURAL_SUCCESS_NOW_4B,+5,+5,+4,+4,+5,+2,+2,+2,+4,-2,+5,+4,Large MFE or market-cap milestone requires 4B-watch.
CONTRACT_HEADLINE_STAGE2_NOT_GREEN,+3,+3,+5,+5,+3,+1,+2,+1,+4,-5,+5,+5,Samsung E&A and LGES show contract headline must clear call-off/margin/cash.
POLICY_CAPEX_FALSE_POSITIVE,+2,+2,+1,+2,+2,+1,+2,+2,+4,-5,+5,+5,Hyundai Steel shows CAPEX headline without ROI can fail.
DIGITAL_POLICY_PRICE_ONLY,+1,+1,+0,+0,+1,+5,+3,+5,+5,-5,+5,+5,Stablecoin basket moved before regulated revenue and FX gate.
DIGITAL_ASSET_PLATFORM_M_AND_A_TRUST_GATE,+3,+3,+1,+2,+4,+5,+5,+4,+5,-5,+5,+5,Naver/Dunamu shows M&A needs closing and trust recovery.
CONTRACT_QUALITY_HARD_4C,+0,+0,+5,+5,+0,+1,+2,+2,+5,0,+3,+5,LGES contract cancellations are hard 4C.
OPERATIONAL_TRUST_HARD_4C,+0,+0,+0,+0,+0,+5,+5,+3,+5,0,+4,+5,Jeju and SKT show safety/security hard gates.
MACRO_GEOPOLITICAL_HARD_4C,+0,+0,+0,+0,+0,+2,+3,+5,+5,0,+5,+5,Middle East/Iran shock confirms macro hard 4C overlay.
```

---

# 이번 R13 Loop 12 결론

```text
1. SK Hynix는 Stage 3 성공 benchmark다.
   하지만 지금은 Green 추가가 아니라 4B-watch다.

2. Samyang은 K-food export Stage 3 후보로 인정할 수 있다.
   export, ASP, capacity, OP revision이 함께 붙었다.

3. Samsung E&A는 signed contract Stage 2다.
   margin/cash collection 전 +8.5%는 event premium이다.

4. Hyundai Steel은 policy CAPEX false positive다.
   CAPEX headline이 funding/ROI 없이 나오면 score를 깎아야 한다.

5. Stablecoin basket은 price_moved_without_evidence다.
   regulated revenue 전 2~3배 상승했고 FX gate가 남아 있다.

6. NAVER/Dunamu는 platform Stage 2와 trust 4C-watch가 동시에 떴다.
   +7%에서 -4.2%로 뒤집힌 가격경로가 신뢰 gate를 보여준다.

7. LGES는 contract-quality hard 4C다.
   actual call-off가 없으면 계약금액 headline은 무너진다.

8. Jeju Air, SK Telecom, Middle East/Iran shock은 hard 4C reference pack이다.
   안전·보안·매크로 shock은 일반 RedTeam이 아니라 즉시 hard gate다.
```

한 문장으로 압축하면:

> **R13의 결론은 간단하다. Stage 3는 “좋은 이야기”가 아니라 revenue/EPS/FCF와 가격경로가 함께 닫히는 순간이고, 4B는 그보다 가격이 먼저 달릴 때, 4C는 계약·안전·보안·매크로가 thesis 자체를 끊을 때 즉시 발동해야 한다.**

* [Reuters](https://www.reuters.com/world/asia-pacific/ai-boom-puts-sk-hynix-cusp-1-trillion-market-value-2026-05-14/?utm_source=chatgpt.com)
* [마켓워치](https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com)
* [월스트리트저널](https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/autos-transportation/hyundai-steels-6-bln-us-investment-draws-investor-ire-tests-seouls-tariff-2025-04-22/?utm_source=chatgpt.com)
* [Financial Times](https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/energy/lg-energy-solution-cancels-39-trillion-won-battery-order-with-freudenberg-2025-12-26/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/sk-telecom-shares-plunge-after-data-breach-due-cyberattack-2025-04-28/?utm_source=chatgpt.com)
* [Reuters](https://www.reuters.com/world/asia-pacific/korean-stocks-dive-won-hits-17-year-low-iran-conflict-2026-03-04/?utm_source=chatgpt.com)

[1]: https://www.marketwatch.com/story/sk-hynix-s-hbm-dominance-higher-chip-prices-could-lift-earnings-market-talk-6508cbf8?utm_source=chatgpt.com "SK Hynix's HBM Dominance, Higher Chip Prices Could Lift Earnings -- Market Talk"
[2]: https://www.marketwatch.com/story/samyang-foods-set-to-post-strong-2q-earnings-market-talk-d654e045?utm_source=chatgpt.com "Samyang Foods Set to Post Strong 2Q Earnings -- Market Talk"
[3]: https://www.wsj.com/articles/samsung-e-a-shares-rise-on-6-billion-saudi-contract-win-10a5b2f4?utm_source=chatgpt.com "Samsung E&A Shares Rise on $6 Billion Saudi Contract Win"
[4]: https://www.reuters.com/business/autos-transportation/hyundai-steels-6-bln-us-investment-draws-investor-ire-tests-seouls-tariff-2025-04-22/?utm_source=chatgpt.com "Hyundai Steel's $6 billion US investment draws investor ire, tests Seoul's tariff strategy"
[5]: https://www.ft.com/content/4b19bf90-4202-4fe7-8caf-d7db6deeb768?utm_source=chatgpt.com "Crypto-crazy investors make South Korea the best-performing market in Asia"
[6]: https://www.reuters.com/world/asia-pacific/navers-payment-arm-acquire-south-korean-crypto-exchange-operator-10-bln-deal-2025-11-27/?utm_source=chatgpt.com "Naver's payment arm to acquire South Korean crypto exchange operator in $10 bln deal"
[7]: https://www.reuters.com/business/energy/lg-energy-solution-cancels-39-trillion-won-battery-order-with-freudenberg-2025-12-26/?utm_source=chatgpt.com "LG Energy Solution cancels 3.9 trillion won battery order with Freudenberg"
[8]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/?utm_source=chatgpt.com "Jeju Air shares plummet to record low after deadly plane crash"

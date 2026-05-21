순서상 이번은 **R9 Loop 13 — 모빌리티·운송·레저 가격경로 검증 라운드**다.

```text
round = R9 Loop 13
round_id = round_206
large_sector = MOBILITY_TRANSPORT_LEISURE
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
next_round = R10 Loop 13
```

이번 R9는 자동차·항공·해운·여행을 같이 본다. 핵심은 “수요가 좋다”가 아니라 **판매 mix, 관세 비용, fleet / capacity, 안전 신뢰, 운임 cycle, 관광객 실제 소비, capex ROI, shareholder return**이 가격경로와 맞았는지다.

이번 환경에서는 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC를 표 형태로 안정적으로 확보하지 못했다. 그래서 30D/90D/180D/1Y full MFE·MAE는 만들지 않고, Reuters/MarketWatch가 제공한 **event return, event low, IPO price, deal value, capacity, tariff cost, market-cap wipeout** 기준으로만 계산했다. full OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R9 = 모빌리티·운송·레저
```

R9에서 진짜 Stage 3는 “하이브리드”, “중국 관광객”, “항공 합병”, “해운 운임”, “인도 IPO”, “미국 공장”, “여행주”라는 단어가 아니다.

진짜 Stage 3는 아래가 닫히는 순간이다.

```text
자동차:
판매 mix / 하이브리드·SUV 비중 / 관세 pass-through / 인센티브 / OP margin / shareholder return

항공:
통합 시너지 / 노선·slot / fleet capex / safety trust / 유류비 / 수요 회복

해운:
운임 cycle / Red Sea rerouting / capacity normalization / bunker cost / contract freight / FCF

레저:
관광객 수가 아니라 객단가 / occupancy / 카지노 drop / 여행상품 booking / cancellation / margin
```

---

# 2. 대상 canonical archetype

```text
HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2
AUTO_TARIFF_MARGIN_4C_WATCH
INDIA_AUTO_IPO_CAPITAL_RECYCLING
AIRLINE_CONSOLIDATION_STAGE2
AVIATION_SAFETY_HARD_4C
AUTO_PARTS_PORTFOLIO_RECYCLING
RED_SEA_FREIGHT_CYCLE_4B_4C
CHINA_TOURISM_LEISURE_EVENT_PREMIUM
```

---

# 3. deep sub-archetype

```text
자동차:
- Hyundai Motor
- Kia
- hybrid lineup doubling
- EREV bridge
- U.S. tariff task force
- Georgia factory ramp
- buyback / dividend policy
- India IPO capital recycling

항공:
- Korean Air / Asiana integration
- Jin Air + Air Busan + Air Seoul LCC integration
- Boeing 103 aircraft order
- GE engine purchase/maintenance deal
- Jeju Air fatal crash

부품:
- Hyundai Mobis lighting business potential sale
- OPmobility possible acquisition
- lighting revenue > €1B
- portfolio restructuring vs core mobility module/electronics margin

해운:
- HMM / Pan Ocean
- Red Sea rerouting freight-rate support
- Gaza ceasefire / Suez return risk
- gradual 60~90 day normalization
- capacity expansion pressure

레저:
- Lotte Tour / Yellow Balloon / Jeju tourism
- China-Japan diplomatic dispute
- China group visa-free entry into Korea
- cruise rerouting to Jeju / Incheon / Busan
```

---

# 4. 국장 신규 후보 case

## Case A — Hyundai Motor `success_candidate + tariff 4C-watch`

```text
symbol = 005380
case_type = success_candidate + 4C-watch
archetype = HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2
```

### stage date

```text
Stage 1:
2024-08-28
- EV 수요 둔화에 대응해 hybrid 라인업 확대
- EREV / Georgia plant / shareholder return 강화

Stage 2:
2024-08-28
- 2030 global sales target 5.55M vehicles
- 2023 대비 +30%
- hybrid sales goal 2028: 1.33M vehicles
- EV target 2030: 2M vehicles 유지
- 2025~2027 buyback up to 4T won
- quarterly dividend at least 2,500 won/share
- profit return target 35%, 기존 대비 +10pp
- shares +5% intraday, close +4.7%

Stage 2 추가:
2025-01-09
- Hyundai Motor Group 2025 domestic investment 24.3T won / $16.65B
- 전년 대비 +19%
- R&D 11.5T won
- ordinary investment 12T won
- strategic investment 800B won
- Hyundai Motor +2.3%, Kia +3.8%

Stage 4C-watch:
2025-04-24
- Q1 OP 3.6T won, +2%
- U.S. tariffs and auto-parts tariffs risk
- Hyundai/Kia U.S. sales exposure about one-third of global sales
- imports account for roughly two-thirds of U.S. car sales
- shares -0.5% after earnings, KOSPI -0.2%
```

Hyundai Motor는 R9에서 가장 좋은 mobility success_candidate다. 하이브리드 전환, EREV bridge, buyback, 배당, 국내투자까지 Stage 2 증거가 충분하다. 하지만 U.S. tariff exposure가 너무 크다. Reuters는 Hyundai/Kia가 U.S.에서 global sales의 약 1/3을 만들고, U.S. 판매의 약 2/3가 수입차라 관세에 취약하다고 보도했다. 그래서 Green은 hybrid mix와 shareholder return이 OP margin·tariff pass-through·FCF로 닫힐 때다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Hyundai investor-day / domestic investment / Q1 tariff anchors",
  "stage3_price": null,
  "hybrid_strategy_event_date": "2024-08-28",
  "hyundai_event_intraday_mfe_pct": 5.0,
  "hyundai_event_close_mfe_pct": 4.7,
  "global_sales_target_2030_mn": 5.55,
  "growth_vs_2023_pct": 30,
  "hybrid_sales_target_2028_mn": 1.33,
  "ev_sales_target_2030_mn": 2.0,
  "buyback_2025_2027_krw_trn": 4.0,
  "minimum_quarterly_dividend_krw": 2500,
  "profit_return_target_pct": 35,
  "domestic_investment_2025_krw_trn": 24.3,
  "domestic_investment_growth_pct": 19,
  "q1_2025_op_krw_trn": 3.6,
  "q1_2025_op_growth_pct": 2,
  "us_sales_share_context": "about_one_third_global_sales",
  "us_import_share_context": "roughly_two_thirds_of_us_sales",
  "q1_earnings_event_mae_pct": -0.5,
  "kospi_same_context_pct": -0.2,
  "mfe_30d_90d_180d_1y_2y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4C_watch
rerating_result = hybrid_shareholder_return_stage2
stage_failure_type = hybrid_strategy_not_green_until_tariff_margin_FCF
```

---

## Case B — Kia `evidence_good_but_price_failed / auto tariff 4C-watch`

```text
symbol = 000270
case_type = evidence_good_but_price_failed
archetype = AUTO_TARIFF_MARGIN_4C_WATCH
```

### stage date

```text
Stage 1:
2025-04~07
- U.S. auto tariff becomes direct margin issue
- Kia U.S. sales stayed resilient but tariff cost hits OP

Stage 4C-watch:
2025-07-25
- Q2 tariff impact 786B won / $570M
- Q2 OP 2.76T won
- OP -24% YoY
- U.S. sales +5% as consumers pulled forward purchases
- shares -1.7%

Stage 3:
없음
- sales growth was not enough
- tariff cost and incentives ate margin
```

Kia는 R9에서 “판매량이 좋아도 margin이 깨지면 Stage 3가 아니다”라는 반례다. Reuters는 Kia가 Q2에 U.S. tariffs로 7860억 원 비용을 맞았고, OP가 24% 감소했으며, U.S. sales는 +5%였지만 주가는 -1.7%였다고 보도했다. 즉 R9 scoring은 판매량보다 **관세 비용, 가격전가, mix, incentive, OP margin**을 먼저 봐야 한다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Kia Q2 tariff anchor",
  "stage3_price": null,
  "event_date": "2025-07-25",
  "q2_tariff_hit_krw_bn": 786,
  "q2_tariff_hit_usd_mn": 570,
  "q2_op_krw_trn": 2.76,
  "q2_op_decline_pct": -24,
  "us_sales_growth_pct": 5,
  "event_mae_pct": -1.7,
  "tariff_hit_as_share_of_q2_op_pct": 28.5,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = auto_tariff_margin_watch
stage_failure_type = unit_sales_not_margin_green
```

---

## Case C — Hyundai Motor India IPO `failed_rerating / capital recycling watch`

```text
symbol = 005380 / HYUN.NS
case_type = failed_rerating + success_candidate
archetype = INDIA_AUTO_IPO_CAPITAL_RECYCLING
```

### stage date

```text
Stage 1:
2024-10-08~14
- Hyundai Motor sells part of Hyundai Motor India stake
- India auto market / SUV portfolio / capital recycling
- first Hyundai listing outside Korea

Stage 2:
2024-10-14
- $3.3B IPO
- parent sells up to 17.5% stake
- Hyundai India valued up to $19B
- Hyundai India equals about 40% of parent market cap at IPO context
- BlackRock / Fidelity anchor participation
- 142,194,700 shares offered

Stage 4C-watch / failed debut:
2024-10-22
- IPO price 1,960 rupees
- listed 1,934 rupees
- traded 1,882.10 rupees
- dropped as much as -6% in debut
- valuation 1.53T rupees / $18.2B, below target $19B
- retail response tepid due valuation concerns

Stage 3:
없음
- IPO monetization is Stage 2
- parent Green requires proceeds use, India growth, margin, SUV mix, dividend/buyback bridge
```

Hyundai India IPO는 capital recycling으로는 의미가 있지만, debut price action은 실패에 가깝다. Reuters는 Hyundai India가 India 최대 IPO로 $3.3B를 조달했지만, 상장 첫날 6%까지 하락했고 offer price 1,960 rupees 아래에서 거래됐다고 보도했다. 그래서 Hyundai parent Green은 “IPO를 했다”가 아니라 proceeds use, India margin, SUV mix, shareholder return으로 확인해야 한다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Hyundai India IPO and debut anchors",
  "stage3_price": null,
  "ipo_value_usd_bn": 3.3,
  "parent_stake_sale_pct": 17.5,
  "target_valuation_usd_bn": 19,
  "valuation_as_parent_market_cap_pct": 40,
  "shares_offered_mn": 142.1947,
  "offer_price_inr": 1960,
  "listing_price_inr": 1934,
  "morning_trade_price_inr": 1882.10,
  "listing_discount_pct": -1.33,
  "debut_mae_pct": -6.0,
  "valuation_debut_inr_trn": 1.53,
  "valuation_debut_usd_bn": 18.2,
  "market_share_india_pct": 15,
  "ipo_oversubscription": "more_than_2x",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = failed_rerating_watch
rerating_result = India_auto_capital_recycling_stage2
stage_failure_type = IPO_valuation_not_parent_green
```

---

## Case D — Korean Air / Asiana `success_candidate + fleet capex watch`

```text
symbols = 003490 / 020560 / 180640
case_type = success_candidate + 4B-watch
archetype = AIRLINE_CONSOLIDATION_STAGE2
```

### stage date

```text
Stage 1:
2024-11-29
- EU approval / Asiana cargo sale condition
- Jin Air + Air Busan + Air Seoul LCC integration plan
- Korean Air consolidation of domestic airline market

Stage 2:
2024-12-12
- Korean Air completes Asiana acquisition
- 1.8T won / $1.3B deal
- Korean Air acquires 63.88% stake in Asiana
- combined group could account for just over half of South Korea passenger capacity
- becomes world's 12th-largest airline by international capacity
- Asiana subsidiary for up to two years before integration under Korean Air

Stage 2 추가:
2025-08-25
- Korean Air announces order for 103 Boeing aircraft
- GE Aerospace purchase/maintenance engine agreement $13.7B
- largest aircraft order in Korean Air history
- part used to re-equip Asiana

Stage 3:
없음
- consolidation is Stage 2
- route concessions, fleet capex, integration cost, safety, loyalty-program approval, margin/FCF 확인 필요
```

Korean Air/Asiana는 R9에서 가장 강한 항공 consolidation 후보지만, Green은 아직 아니다. Reuters는 Korean Air가 Asiana 63.88%를 인수해 세계 12위권 international capacity carrier가 된다고 보도했다. 다만 통합은 2027년까지 이어지고, LCC 통합·frequent flyer program·route concessions·fleet capex가 남아 있다. 2025년 103대 Boeing order와 $13.7B GE engine deal은 성장 투자이지만 capex 부담이기도 하다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Korean Air-Asiana acquisition / branding / Boeing order anchors",
  "stage3_price": null,
  "deal_value_krw_trn": 1.8,
  "deal_value_usd_bn": 1.3,
  "asiana_stake_acquired_pct": 63.88,
  "integration_target": "Asiana subsidiary up to two years; full integration by 2027 under Korean Air brand",
  "combined_passenger_capacity_share_context": "just_over_half_of_south_korea_capacity",
  "international_capacity_rank_context": 12,
  "boeing_aircraft_order_units": 103,
  "ge_engine_purchase_maintenance_deal_usd_bn": 13.7,
  "frequent_flyer_program_review_due": "2025-06 plan submission to KFTC",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4B_watch
rerating_result = airline_consolidation_stage2
stage_failure_type = merger_completion_not_integration_margin_green
```

---

## Case E — Jeju Air `aviation safety hard 4C`

```text
symbol = 089590
case_type = 4C-thesis-break
archetype = AVIATION_SAFETY_HARD_4C
```

### stage date

```text
Stage 1:
2024-12-29
- Muan International Airport crash
- deadliest air crash in South Korea history
- Jeju Air first fatal flight since founding

Stage 4C:
2024-12-30
- 179 deaths
- Jeju Air shares fall as much as -15.7%
- event low 6,920 won
- market-cap wipeout as much as 95.7B won / $65.2M
- AK Holdings -12%, lowest in 16 years
- Hanatour -7%, Very Good Tour -11%
- government orders emergency safety inspection of entire airline operation system

Stage 3:
N/A
```

Jeju Air는 R9 hard 4C다. 항공은 안전 신뢰가 business model 그 자체다. Reuters는 Jeju Air가 사고 다음 거래일 장중 -15.7%로 6,920원까지 밀렸고, 시총 957억 원이 날아갔다고 보도했다. 여행사 주식까지 동시에 하락했고, 정부는 항공운항 시스템 전체 안전점검을 지시했다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters Jeju Air crash and event-price anchor",
  "stage3_price": null,
  "stage4c_date": "2024-12-30",
  "fatalities": 179,
  "event_low_price_krw": 6920,
  "event_intraday_mae_pct": -15.7,
  "event_midday_mae_pct": -8.5,
  "market_cap_wipeout_krw_bn": 95.7,
  "market_cap_wipeout_usd_mn": 65.2,
  "ak_holdings_mae_pct": -12,
  "korean_air_mae_pct": -1.3,
  "asiana_mae_pct": -0.8,
  "hanatour_mae_pct": -7,
  "very_good_tour_mae_pct": -11,
  "mfe": "N/A",
  "mae_30d_90d_180d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = aviation_safety_hard_4C
stage_failure_type = fatal_safety_event
```

---

## Case F — Hyundai Mobis lighting business `success_candidate / asset recycling`

```text
symbol = 012330
case_type = success_candidate
archetype = AUTO_PARTS_PORTFOLIO_RECYCLING
```

### stage date

```text
Stage 1:
2025-12 / 2026-01
- Hyundai Mobis explores competitiveness improvement / lamp business options
- auto lighting becomes design/safety growth segment
- portfolio recycling possibility

Stage 2:
2026-01-27
- OPmobility signs agreement to explore acquiring controlling stake in Hyundai Mobis lighting division
- financial terms undisclosed
- final agreement expected within 2026
- Hyundai Mobis lighting business weighs over €1B revenue per year, per source/JPMorgan estimate
- OPmobility exterior/lighting business: about €4B sales in first nine months 2025
- OPmobility shares +1% in Paris early trading

Stage 3:
없음
- sale exploration is not Green
- actual deal value, proceeds use, remaining Mobis margin, electronics/module ROIC 확인 필요
```

Hyundai Mobis는 R9 자동차부품 asset recycling 후보지만, 아직 Stage 2다. OPmobility가 Hyundai Mobis lighting division의 controlling stake 인수를 탐색하는 계약을 맺었고, 해당 lighting business는 연간 €1B 이상 revenue로 추정됐다. 다만 financial terms가 없고, final agreement도 아직이다. Green은 actual deal value, proceeds use, remaining business margin, ROIC improvement가 확인되어야 한다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters OPmobility / Hyundai Mobis lighting business anchor",
  "stage3_price": null,
  "potential_transaction_status": "exploratory_agreement",
  "financial_terms_disclosed": false,
  "final_agreement_expected": "within_2026",
  "hyundai_mobis_lighting_revenue_context_eur_bn": 1.0,
  "opmobility_exterior_lighting_9m2025_sales_eur_bn": 4.0,
  "opmobility_early_trading_mfe_pct": 1.0,
  "deal_value_confirmed": false,
  "proceeds_use_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_price_data
rerating_result = auto_parts_portfolio_recycling_stage2
stage_failure_type = exploratory_sale_not_ROIC_green
```

---

## Case G — HMM / Pan Ocean `cyclical_success + Red Sea 4B/4C-watch`

```text
symbols = 011200 / 028670
case_type = cyclical_success + 4B-watch
archetype = RED_SEA_FREIGHT_CYCLE_4B_4C
```

### stage date

```text
Stage 1:
2024-06
- Red Sea rerouting supports freight rates
- Korean shipping stocks participate in transport rally

Stage 2:
2024-06-25 / 2024-06-28
- HMM +2.9% with auto/shipping stocks
- Pan Ocean +3.9%, HMM +2.9% with defense/shipbuilding/shipping rally

Stage 4B-watch:
2025-10-09
- Gaza ceasefire raises probability of Suez/Red Sea reopening
- Maersk -2% on expectations of freight-rate pressure
- shipping lines may wait months before return

Stage 4C-watch:
2025-12-04
- Hapag-Lloyd says no fixed timeline for Suez return
- return would be gradual
- 60~90 day transition period to realign logistics
- freight rates already declining from peaks
- Hapag-Lloyd nine-month net profit -50%

Stage 3:
없음
- freight-cycle rally is not Green
- contract freight, spot-rate durability, bunker cost, capacity normalization, FCF required
```

해운주는 Red Sea rerouting으로 운임이 올라갈 때 cyclical success가 생긴다. 하지만 이건 구조적 Stage 3가 아니라 cycle이다. MarketWatch는 HMM과 Pan Ocean이 2024년 6월 각각 +2.9%, +3.9% 상승했다고 보도했다. 반대로 Gaza ceasefire와 Suez 재개 가능성이 나오면 freight-rate pressure가 발생하고, Maersk는 해당 기대만으로 -2% 하락했다. Hapag-Lloyd는 Suez 복귀가 60~90일 전환기간을 필요로 할 수 있다고 했다. ([마켓워치][7])

### 실제 가격경로 검증

```json
{
  "price_data_source": "MarketWatch Korean shipping event anchors + Reuters Red Sea/Suez reopening risk anchors",
  "stage3_price": null,
  "hmm_event_mfe_2024_06_25_pct": 2.9,
  "hmm_event_mfe_2024_06_28_pct": 2.9,
  "pan_ocean_event_mfe_2024_06_28_pct": 3.9,
  "kospi_2024_06_25_context_pct": 0.3,
  "kospi_2024_06_28_context_pct": 0.2,
  "maersk_ceasefire_event_mae_pct": -2.0,
  "suez_return_transition_period_days": "60-90",
  "hapag_lloyd_9m_net_profit_decline_pct": -50,
  "freight_rate_durability_confirmed": false,
  "mfe_30d_90d_180d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = cyclical_success_4B_watch
rerating_result = Red_Sea_freight_cycle_watch
stage_failure_type = freight_rate_cycle_not_structural_green
```

---

## Case H — China tourism / leisure basket `event_premium`

```text
symbols = 032350 / 104620 / 034230 / 008770 / 004170 / travel-leisure basket
case_type = event_premium + 4B-watch
archetype = CHINA_TOURISM_LEISURE_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-08-06
- Korea offers visa-free entry to Chinese tourist groups
- tourism / casino / hotel / duty-free / cruise demand expectation

Stage 2:
2025-08-06
- Chinese group tourists visa-free from 2025-09-29 to 2026-06
- Hyundai Department Store +7.1%
- Hotel Shilla +4.8%
- Paradise +2.9%
- Hankook Cosmetics +9.9%

Stage 4B:
2025-11-21
- China-Japan diplomatic dispute redirects cruise/tourism interest to Korea
- Lotte Tour Development >+20%
- Yellow Balloon +24%
- Shinsegae +6%
- Adora Magic City Jeju stay extends from usual 9h to 31~57h

Stage 3:
없음
- tourist-flow headline is not Green
- actual arrivals, booking conversion, casino drop, hotel occupancy, ADR, package margin required
```

레저·여행 basket은 R9에서 전형적인 event premium이다. 중국 단체 관광 비자면제와 China-Japan 갈등은 좋은 Stage 2 catalyst지만, 주가가 먼저 뛴다. Reuters는 Lotte Tour Development가 20% 이상, Yellow Balloon이 24%, Shinsegae가 6% 올랐다고 보도했다. 하지만 Green은 실제 booking, cancellation ratio, hotel occupancy, casino drop, ADR, margin으로 닫혀야 한다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters China visa-free and China-Japan tourism rerouting anchors",
  "stage3_price": null,
  "visa_free_start": "2025-09-29",
  "visa_free_end": "2026-06",
  "visa_free_stay_days": 15,
  "hyundai_department_store_mfe_pct": 7.1,
  "hotel_shilla_mfe_pct": 4.8,
  "paradise_mfe_pct": 2.9,
  "hankook_cosmetics_mfe_pct": 9.9,
  "lotte_tour_rerouting_mfe_pct": 20,
  "yellow_balloon_rerouting_mfe_pct": 24,
  "shinsegae_rerouting_mfe_pct": 6,
  "adora_usual_jeju_stay_hours": 9,
  "adora_new_jeju_stay_hours": "31-57",
  "jeju_stay_extension_low_pct": 244.4,
  "jeju_stay_extension_high_pct": 533.3,
  "actual_booking_margin_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
rerating_result = China_tourism_leisure_watch
stage_failure_type = tourist_flow_headline_not_booking_margin_green
```

---

# 5. 이번 R9 case별 stage date 요약

| case                | Stage 1           | Stage 2           | Stage 3 | Stage 4B                 | Stage 4C                       |
| ------------------- | ----------------- | ----------------- | ------- | ------------------------ | ------------------------------ |
| Hyundai Motor       | 2024-08-28        | 2024-08 / 2025-01 | N/A     | shareholder-return watch | 2025 tariff watch              |
| Kia                 | 2025-04~07        | N/A               | N/A     | N/A                      | 2025-07-25 tariff margin watch |
| Hyundai India IPO   | 2024-10           | 2024-10-14        | N/A     | IPO valuation watch      | 2024-10-22 failed debut        |
| Korean Air / Asiana | 2024-11           | 2024-12 / 2025-08 | N/A     | fleet capex watch        | integration/safety watch       |
| Jeju Air            | 2024-12-29        | N/A               | N/A     | N/A                      | 2024-12-30 hard                |
| Hyundai Mobis       | 2025-12 / 2026-01 | 2026-01-27        | N/A     | asset-sale watch         | N/A                            |
| HMM / Pan Ocean     | 2024-06           | 2024-06           | N/A     | freight-cycle watch      | Suez return watch              |
| Tourism basket      | 2025-08           | 2025-08           | N/A     | 2025-11                  | N/A                            |

---

# 6. 실제 가격경로 검증 총괄

| case                |                                          anchor | MFE / MAE 해석                                  | 판정                             |
| ------------------- | ----------------------------------------------: | --------------------------------------------- | ------------------------------ |
| Hyundai Motor       |      +5% intraday / +4.7% close, later Q1 -0.5% | strategy 좋은데 tariff watch                     | success_candidate              |
| Kia                 |       tariff hit 786B won, OP -24%, stock -1.7% | sales보다 margin이 중요                            | evidence_good_but_price_failed |
| Hyundai India IPO   |                                   IPO -6% debut | capital recycling but failed listing          | failed_rerating_watch          |
| Korean Air / Asiana |    1.8T won deal, 63.88% stake, 103 Boeing jets | consolidation Stage 2, capex/integration gate | success_candidate              |
| Jeju Air            |                   -15.7%, 6,920 won, 179 deaths | safety hard 4C                                | thesis_break                   |
| Hyundai Mobis       |   lighting revenue >€1B, deal value undisclosed | asset recycling Stage 2                       | insufficient                   |
| HMM / Pan Ocean     | HMM +2.9%, Pan Ocean +3.9%, Red Sea return risk | cyclical freight-rate watch                   | cyclical_success               |
| Tourism basket      |            Lotte Tour >20%, Yellow Balloon +24% | 관광객 headline event premium                    | event_premium                  |

---

# 7. score-price alignment 판정

```text
success_candidate:
- Hyundai Motor
- Korean Air / Asiana
- Hyundai Mobis lighting portfolio recycling

evidence_good_but_price_failed:
- Kia Q2 tariff case

failed_rerating:
- Hyundai Motor India IPO debut

cyclical_success:
- HMM / Pan Ocean Red Sea freight cycle

event_premium:
- China tourism / Lotte Tour / Yellow Balloon / Shinsegae
- Hyundai Motor shareholder-return event if used before tariff/margin proof
- Korean Air Boeing order if used before ROI proof

price_moved_without_evidence:
- tourism basket before booking / occupancy / casino drop / margin
- HMM/Pan Ocean freight rally before durable contract rates
- Hyundai India IPO valuation if treated as parent Green

thesis_break:
- Jeju Air fatal crash

thesis_break_watch:
- Kia / Hyundai tariff margin
- Korean Air integration / fleet capex
- Hyundai Mobis exploratory sale
- HMM/Pan Ocean Suez normalization risk

hard_4C_confirmed:
- Jeju Air fatal crash
```

---

# 8. 점수비중 교정

## 올릴 축

```text
OP_margin_after_tariff +5
hybrid_SUV_mix_quality +5
price_pass_through +5
shareholder_return_execution +4
integration_synergy_realization +5
fleet_capex_ROI +5
aviation_safety_trust +5
freight_rate_durability +5
booking_occupancy_conversion +5
asset_sale_ROIC +4
```

### 왜 올리나

Kia는 U.S. sales가 +5%였는데 tariff cost 때문에 OP가 -24%였다. Hyundai Motor는 hybrid/shareholder-return이 좋아도 tariff pass-through가 핵심이다. Korean Air는 Asiana 인수와 fleet renewal이 좋지만 integration과 capex ROI가 필요하다. Jeju Air는 safety trust가 R9에서 hard gate라는 걸 보여줬다. HMM/Pan Ocean은 Red Sea 운임 cycle이 구조적 수익인지 확인해야 한다.

## 내릴 축

```text
unit_sales_without_margin -5
IPO_valuation_without_parent_ROI -5
tourist_flow_headline_only -5
freight_rate_spike_only -5
fleet_order_without_ROI -4
exploratory_asset_sale_only -4
tariff_exposure_unhedged -5
fatal_safety_event -5
booking_without_margin -4
```

### 왜 내리나

판매량이 좋아도 관세와 인센티브가 margin을 깨면 Stage 3가 아니다. 관광객 headline은 booking margin이 아니다. 항공기 주문은 성장투자이면서 capex burden이다. Hyundai Mobis lighting sale은 deal value와 proceeds use가 없으면 Green이 아니다. Jeju Air 같은 fatal event는 즉시 hard 4C다.

## Green gate 강화 조건

```text
R9 Stage 3-Green 필수:
1. 자동차는 OP margin after tariff 확인
2. hybrid/SUV mix와 price pass-through 확인
3. shareholder return은 실제 buyback/dividend 실행 확인
4. 항공은 integration synergy / fleet capex ROI / safety trust 확인
5. 해운은 spot이 아니라 contract rate durability와 capacity normalization 확인
6. 레저는 tourist flow가 아니라 booking, occupancy, ADR, casino drop, package margin 확인
7. asset sale은 final deal value, proceeds use, remaining business ROIC 확인
8. price path가 evidence 이후 따라옴

금지:
unit sales only
tourist-flow headline only
IPO valuation only
freight-rate spike only
fleet order only
exploratory asset sale only
fatal safety event unresolved
```

## 4B 조기감지 조건

```text
4B-watch:
hybrid/shareholder-return event로 +5% 이상 급등
tourism/travel basket +20% 이상 급등
freight-rate cycle로 shipping stock short rally
airline consolidation premium before integration proof
aircraft order headline before ROI proof
India IPO valuation before parent capital-return bridge
asset-sale rumor/exploration before final value

4B-elevated:
tariff margin untested
fleet capex large
safety incident history
Red Sea/Suez route normalization risk
booking conversion unconfirmed
IPO weak debut
```

## 4C hard gate 조건

```text
fatal crash / safety inspection
tariff cost crushing margin
airline integration failure
fleet capex overhang with weak demand
tourism cancellation shock
shipping route normalization collapsing freight rates
asset-sale failure after price premium
IPO debut failure if used as parent value-up thesis
```

이번 R9 Loop 13의 hard 4C는 **Jeju Air fatal crash**로 확정한다. Kia/Hyundai tariff, HMM/Pan Ocean freight-cycle reversal, Korean Air integration/capex, tourism headline rally는 4C-watch 또는 4B-watch다.

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 10. 레포 반영용 patch-ready 출력

## docs/round/round_206.md 요약

```md
# R9 Loop 13. Mobility / Transportation / Leisure Price Validation

이번 라운드는 R9 Loop 13 price-validation 라운드다.

핵심 결론:
- Hyundai Motor is hybrid/shareholder-return success_candidate plus tariff 4C-watch. 2030 sales target 5.55M, 2028 hybrid target 1.33M, 2025~2027 buyback up to 4T won, shares +5% intraday and +4.7% close. Later U.S. tariff exposure remains key because Hyundai/Kia get about one-third of global sales from the U.S., and imports are roughly two-thirds of U.S. sales.
- Kia is evidence_good_but_price_failed. Q2 2025 U.S. tariff hit 786B won / $570M, OP -24% to 2.76T won, U.S. sales +5%, shares -1.7%. Unit sales are not Green without margin.
- Hyundai Motor India IPO is failed_rerating_watch. $3.3B IPO, target valuation $19B, offer price 1,960 rupees, traded 1,882.10 rupees, debut down as much as -6%. Parent Green requires proceeds use and capital-return bridge.
- Korean Air / Asiana is airline-consolidation Stage 2. 1.8T won / $1.3B deal, 63.88% Asiana stake, group could account for just over half of Korea passenger capacity and become world’s 12th-largest by international capacity. 103 Boeing aircraft order and $13.7B GE engine deal add fleet-capex gate.
- Jeju Air is aviation-safety hard 4C. 179 deaths, shares -15.7% intraday to 6,920 won, market-cap wipeout 95.7B won. Safety trust is hard gate.
- Hyundai Mobis lighting division is auto-parts portfolio recycling Stage 2. OPmobility explores controlling stake; lighting business revenue estimated over €1B annually. Final deal value and proceeds use required.
- HMM / Pan Ocean is Red Sea freight-cycle cyclical_success plus 4B/4C-watch. HMM +2.9%, Pan Ocean +3.9% during shipping rally, but Suez return could pressure freight rates; return may require 60~90 day transition.
- China tourism / leisure basket is event premium. Visa-free Chinese group travel and China-Japan dispute drove Hyundai Department +7.1%, Hotel Shilla +4.8%, Lotte Tour >20%, Yellow Balloon +24%. Booking, occupancy, ADR and margin required.
```

## docs/checkpoints/checkpoint_28a_round206_r9_loop13.md 요약

```md
# Checkpoint 28A Round 206 R9 Loop 13 Mobility Transport Leisure Price Validation

## 반영 내용
- R9 Loop 13 price-validation 라운드를 추가했다.
- Hyundai Motor hybrid/shareholder-return, Kia tariff margin break, Hyundai India IPO, Korean Air/Asiana integration, Jeju Air crash, Hyundai Mobis lighting asset recycling, HMM/Pan Ocean Red Sea freight cycle, China tourism/leisure event premium을 비교했다.
- Reuters / MarketWatch anchors로 가능한 event MFE/MAE와 deal/capacity/margin-risk metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- OP margin after tariff, hybrid/SUV mix quality, price pass-through, shareholder-return execution, integration synergy, fleet capex ROI, aviation safety trust, freight-rate durability, booking/occupancy conversion, asset-sale ROIC 가중치 강화
- unit sales without margin, IPO valuation without parent ROI, tourist-flow headline-only, freight-rate spike-only, fleet order without ROI, exploratory asset sale-only, unhedged tariff exposure, fatal safety event 감점 강화
```

## data/e2r_case_library/cases_r9_loop13_round206.jsonl 초안

```jsonl
{"case_id":"r9_loop13_hyundai_motor_hybrid_shareholder_return_tariff_watch","symbol":"005380","company_name":"Hyundai Motor","case_type":"success_candidate_4c_watch","primary_archetype":"HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2","stage2_date":"2024-08-28/2025-01-09","stage4c_date":"2025-04-24_watch","price_validation":{"price_data_source":"Reuters Hyundai investor-day / domestic investment / Q1 tariff anchors","stage3_price":null,"hyundai_event_intraday_mfe_pct":5.0,"hyundai_event_close_mfe_pct":4.7,"global_sales_target_2030_mn":5.55,"growth_vs_2023_pct":30,"hybrid_sales_target_2028_mn":1.33,"ev_sales_target_2030_mn":2.0,"buyback_2025_2027_krw_trn":4.0,"minimum_quarterly_dividend_krw":2500,"profit_return_target_pct":35,"domestic_investment_2025_krw_trn":24.3,"domestic_investment_growth_pct":19,"q1_2025_op_krw_trn":3.6,"q1_2025_op_growth_pct":2,"us_sales_share_context":"about_one_third_global_sales","us_import_share_context":"roughly_two_thirds_of_us_sales","q1_earnings_event_mae_pct":-0.5,"kospi_same_context_pct":-0.2,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_4C_watch","rerating_result":"hybrid_shareholder_return_stage2","notes":"Hybrid/shareholder-return evidence is strong, but tariff margin and FCF must clear before Green."}
{"case_id":"r9_loop13_kia_us_tariff_margin_break","symbol":"000270","company_name":"Kia Corp","case_type":"evidence_good_but_price_failed","primary_archetype":"AUTO_TARIFF_MARGIN_4C_WATCH","stage4c_date":"2025-07-25_watch","price_validation":{"price_data_source":"Reuters Kia Q2 tariff anchor","stage3_price":null,"q2_tariff_hit_krw_bn":786,"q2_tariff_hit_usd_mn":570,"q2_op_krw_trn":2.76,"q2_op_decline_pct":-24,"us_sales_growth_pct":5,"event_mae_pct":-1.7,"tariff_hit_as_share_of_q2_op_pct":28.5,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"auto_tariff_margin_watch","notes":"Unit sales grew, but tariff hit crushed OP; R9 Green needs margin after tariff."}
{"case_id":"r9_loop13_hyundai_motor_india_ipo_failed_debut","symbol":"005380/HYUN.NS","company_name":"Hyundai Motor / Hyundai Motor India","case_type":"failed_rerating_watch","primary_archetype":"INDIA_AUTO_IPO_CAPITAL_RECYCLING","stage2_date":"2024-10-14","stage4c_date":"2024-10-22_watch","price_validation":{"price_data_source":"Reuters Hyundai India IPO and debut anchors","stage3_price":null,"ipo_value_usd_bn":3.3,"parent_stake_sale_pct":17.5,"target_valuation_usd_bn":19,"valuation_as_parent_market_cap_pct":40,"shares_offered_mn":142.1947,"offer_price_inr":1960,"listing_price_inr":1934,"morning_trade_price_inr":1882.10,"listing_discount_pct":-1.33,"debut_mae_pct":-6.0,"valuation_debut_inr_trn":1.53,"valuation_debut_usd_bn":18.2,"market_share_india_pct":15,"ipo_oversubscription":"more_than_2x","price_validation_status":"reported_ipo_anchor_not_full_ohlc"},"score_price_alignment":"failed_rerating_watch","rerating_result":"India_auto_capital_recycling_stage2","notes":"IPO monetization is Stage 2, but weak debut blocks parent Green until proceeds use and capital-return bridge are clear."}
{"case_id":"r9_loop13_korean_air_asiana_integration_fleet_capex","symbol":"003490/020560/180640","company_name":"Korean Air / Asiana / Hanjin Kal","case_type":"success_candidate_4b_watch","primary_archetype":"AIRLINE_CONSOLIDATION_STAGE2","stage2_date":"2024-12-12/2025-08-25","price_validation":{"price_data_source":"Reuters Korean Air-Asiana acquisition / branding / Boeing order anchors","stage3_price":null,"deal_value_krw_trn":1.8,"deal_value_usd_bn":1.3,"asiana_stake_acquired_pct":63.88,"integration_target":"Asiana subsidiary up to two years; full integration by 2027 under Korean Air brand","combined_passenger_capacity_share_context":"just_over_half_of_south_korea_capacity","international_capacity_rank_context":12,"boeing_aircraft_order_units":103,"ge_engine_purchase_maintenance_deal_usd_bn":13.7,"frequent_flyer_program_review_due":"2025-06 plan submission to KFTC","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_4B_watch","rerating_result":"airline_consolidation_stage2","notes":"Merger completion is Stage 2; integration synergy, fleet capex ROI, safety and FCF required."}
{"case_id":"r9_loop13_jeju_air_fatal_crash_hard_4c","symbol":"089590","company_name":"Jeju Air","case_type":"4c_thesis_break","primary_archetype":"AVIATION_SAFETY_HARD_4C","stage4c_date":"2024-12-30","price_validation":{"price_data_source":"Reuters Jeju Air crash and event-price anchor","stage3_price":null,"fatalities":179,"event_low_price_krw":6920,"event_intraday_mae_pct":-15.7,"event_midday_mae_pct":-8.5,"market_cap_wipeout_krw_bn":95.7,"market_cap_wipeout_usd_mn":65.2,"ak_holdings_mae_pct":-12,"korean_air_mae_pct":-1.3,"asiana_mae_pct":-0.8,"hanatour_mae_pct":-7,"very_good_tour_mae_pct":-11,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"aviation_safety_hard_4C","notes":"Fatal safety event is R9 hard 4C; safety trust overrides demand and capacity."}
{"case_id":"r9_loop13_hyundai_mobis_lighting_asset_recycling","symbol":"012330","company_name":"Hyundai Mobis","case_type":"success_candidate","primary_archetype":"AUTO_PARTS_PORTFOLIO_RECYCLING","stage2_date":"2026-01-27","price_validation":{"price_data_source":"Reuters OPmobility / Hyundai Mobis lighting business anchor","stage3_price":null,"potential_transaction_status":"exploratory_agreement","financial_terms_disclosed":false,"final_agreement_expected":"within_2026","hyundai_mobis_lighting_revenue_context_eur_bn":1.0,"opmobility_exterior_lighting_9m2025_sales_eur_bn":4.0,"opmobility_early_trading_mfe_pct":1.0,"deal_value_confirmed":false,"proceeds_use_confirmed":false,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_price_data","rerating_result":"auto_parts_portfolio_recycling_stage2","notes":"Exploratory sale is Stage 2; deal value, proceeds use and ROIC improvement required."}
{"case_id":"r9_loop13_hmm_pan_ocean_red_sea_freight_cycle","symbol":"011200/028670","company_name":"HMM / Pan Ocean","case_type":"cyclical_success_4b_watch","primary_archetype":"RED_SEA_FREIGHT_CYCLE_4B_4C","stage2_date":"2024-06","stage4c_date":"2025-10/2025-12_watch","price_validation":{"price_data_source":"MarketWatch Korean shipping event anchors + Reuters Red Sea/Suez reopening risk anchors","stage3_price":null,"hmm_event_mfe_2024_06_25_pct":2.9,"hmm_event_mfe_2024_06_28_pct":2.9,"pan_ocean_event_mfe_2024_06_28_pct":3.9,"kospi_2024_06_25_context_pct":0.3,"kospi_2024_06_28_context_pct":0.2,"maersk_ceasefire_event_mae_pct":-2.0,"suez_return_transition_period_days":"60-90","hapag_lloyd_9m_net_profit_decline_pct":-50,"freight_rate_durability_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"cyclical_success_4B_watch","rerating_result":"Red_Sea_freight_cycle_watch","notes":"Freight-rate cycle is not structural Green until contract rates, capacity normalization and FCF prove durable."}
{"case_id":"r9_loop13_china_tourism_leisure_event_premium","symbol":"032350/104620/034230/008770/004170","company_name":"Lotte Tour / Yellow Balloon / Paradise / Hotel Shilla / Shinsegae","case_type":"event_premium_4b_watch","primary_archetype":"CHINA_TOURISM_LEISURE_EVENT_PREMIUM","stage2_date":"2025-08-06","stage4b_date":"2025-11-21","price_validation":{"price_data_source":"Reuters China visa-free and China-Japan tourism rerouting anchors","stage3_price":null,"visa_free_start":"2025-09-29","visa_free_end":"2026-06","visa_free_stay_days":15,"hyundai_department_store_mfe_pct":7.1,"hotel_shilla_mfe_pct":4.8,"paradise_mfe_pct":2.9,"hankook_cosmetics_mfe_pct":9.9,"lotte_tour_rerouting_mfe_pct":20,"yellow_balloon_rerouting_mfe_pct":24,"shinsegae_rerouting_mfe_pct":6,"adora_usual_jeju_stay_hours":9,"adora_new_jeju_stay_hours":"31-57","jeju_stay_extension_low_pct":244.4,"jeju_stay_extension_high_pct":533.3,"actual_booking_margin_confirmed":false,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"event_premium_4B_watch","rerating_result":"China_tourism_leisure_watch","notes":"Tourist-flow and rerouting headlines are event premium until booking, occupancy, ADR, casino drop and margin confirm."}
```

## data/sector_taxonomy/score_weight_profiles_round206_r9_loop13_v1.csv 초안

```csv
archetype,op_margin_after_tariff,hybrid_suv_mix_quality,price_pass_through,shareholder_return_execution,integration_synergy_realization,fleet_capex_roi,aviation_safety_trust,freight_rate_durability,booking_occupancy_conversion,asset_sale_roic,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
HYBRID_SHAREHOLDER_RETURN_MOBILITY_STAGE2,+5,+5,+5,+4,+0,+2,+2,+0,+0,+1,-3,+4,+4,Hyundai strategy is Stage 2; tariff margin and FCF must confirm.
AUTO_TARIFF_MARGIN_4C_WATCH,+5,+4,+5,+2,+0,+1,+2,+0,+0,+0,0,+3,+5,Kia shows unit sales are not Green if tariff cost crushes OP.
INDIA_AUTO_IPO_CAPITAL_RECYCLING,+4,+4,+3,+5,+0,+2,+1,+0,+0,+4,-5,+5,+4,Hyundai India IPO needs proceeds use and parent capital-return/ROI bridge.
AIRLINE_CONSOLIDATION_STAGE2,+3,+0,+3,+2,+5,+5,+5,+0,+3,+0,-4,+5,+5,Korean Air/Asiana needs integration synergy, safety and fleet capex ROI.
AVIATION_SAFETY_HARD_4C,+0,+0,+0,+0,+0,+0,+5,+0,+3,+0,0,+3,+5,Jeju Air crash confirms fatal safety event as hard 4C.
AUTO_PARTS_PORTFOLIO_RECYCLING,+3,+3,+3,+3,+1,+2,+1,+0,+0,+5,-4,+4,+3,Hyundai Mobis lighting sale requires final deal value and ROIC bridge.
RED_SEA_FREIGHT_CYCLE_4B_4C,+2,+0,+2,+1,+0,+0,+1,+5,+0,+0,-5,+5,+4,HMM/Pan Ocean cycle needs contract freight and FCF durability.
CHINA_TOURISM_LEISURE_EVENT_PREMIUM,+1,+0,+2,+0,+0,+0,+2,+0,+5,+0,-5,+5,+3,Tourism headlines need booking, occupancy, ADR, casino drop and margin.
```

---

# 이번 R9 Loop 13 결론

```text
1. Hyundai Motor는 R9의 강한 success_candidate다.
   hybrid/shareholder return은 좋지만, tariff pass-through와 OP margin이 Stage 3 조건이다.

2. Kia는 evidence_good_but_price_failed다.
   U.S. sales +5%에도 tariff hit 786B won 때문에 OP -24%, 주가 -1.7%가 나왔다.

3. Hyundai Motor India IPO는 failed_rerating_watch다.
   $3.3B IPO 자체는 capital recycling이지만, debut -6%는 valuation gate 실패다.

4. Korean Air/Asiana는 airline consolidation Stage 2다.
   통합 시너지와 fleet capex ROI, safety, loyalty-program approval 전에는 Green이 아니다.

5. Jeju Air는 R9 hard 4C다.
   fatal crash는 수요·노선·가격보다 먼저 보는 safety trust gate다.

6. Hyundai Mobis lighting sale은 asset recycling Stage 2다.
   exploratory agreement라 deal value와 ROIC bridge가 필요하다.

7. HMM/Pan Ocean은 Red Sea freight-cycle cyclical_success다.
   운임 cycle은 좋지만 Suez normalization이 오면 4B/4C-watch가 떠야 한다.

8. China tourism/leisure basket은 event premium이다.
   관광객 headline이 아니라 booking, occupancy, ADR, casino drop, margin이 Stage 3다.
```

한 문장으로 압축하면:

> **R9에서 진짜 Stage 3는 “하이브리드·관광객·항공합병·해운운임·인도 IPO가 좋다”가 아니라, 관세 후 OP margin·integration synergy·safety trust·freight-rate durability·booking margin·capex ROI가 실제 숫자로 닫히는 순간이다.**

[1]: https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/ "https://www.reuters.com/business/autos-transportation/hyundai-motor-targets-30-rise-sales-by-2030-it-expands-hybrid-lineup-2024-08-28/"
[2]: https://www.reuters.com/business/autos-transportation/kia-corp-takes-570-million-hit-us-tariffs-second-quarter-2025-07-25/ "https://www.reuters.com/business/autos-transportation/kia-corp-takes-570-million-hit-us-tariffs-second-quarter-2025-07-25/"
[3]: https://www.reuters.com/markets/deals/hyundai-india-starts-33-bln-ipo-countrys-largest-ever-share-sale-2024-10-14/ "https://www.reuters.com/markets/deals/hyundai-india-starts-33-bln-ipo-countrys-largest-ever-share-sale-2024-10-14/"
[4]: https://www.reuters.com/markets/deals/korean-air-completes-asiana-takeover-form-one-asias-biggest-airlines-2024-12-12/ "https://www.reuters.com/markets/deals/korean-air-completes-asiana-takeover-form-one-asias-biggest-airlines-2024-12-12/"
[5]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/ "https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/"
[6]: https://www.reuters.com/business/opmobility-signs-deal-explore-buying-hyundai-mobis-lighting-business-2026-01-27/ "https://www.reuters.com/business/opmobility-signs-deal-explore-buying-hyundai-mobis-lighting-business-2026-01-27/"
[7]: https://www.marketwatch.com/story/south-korea-s-kospi-0-3-higher-auto-shipping-stocks-advance-market-talk-69976490 "https://www.marketwatch.com/story/south-korea-s-kospi-0-3-higher-auto-shipping-stocks-advance-market-talk-69976490"
[8]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/ "https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/"

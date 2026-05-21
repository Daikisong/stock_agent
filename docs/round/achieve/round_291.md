순서상 이번은 **R9 Loop 14 — 모빌리티·운송·레저 가격경로 검증 라운드**다.

```text
round = R9 Loop 14
round_id = round_219
large_sector = MOBILITY_TRANSPORT_LEISURE
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
next_round = R10 Loop 14
```

이번 R9는 **Hyundai Motor/Kia tariff·hybrid mix, Hyundai/Hyundai Glovis Middle East logistics shock, Korean Air/Asiana 통합, T’way/Air Incheon route·cargo remedy, Jeju Air safety hard 4C, Hyundai Motor India IPO, China tourism/leisure basket, HMM/Red Sea freight-rate cycle**을 본다.

수정주가 기준 일봉 OHLC 전체 window는 이번 환경에서도 안정적으로 확보하지 못했다. `finance` tool은 KRX ticker를 지원하지 않았고, web search에서 KRX/Naver/Yahoo/Stooq의 조정 OHLC window를 일괄 추출할 수 없었다. 그래서 30D/90D/180D/1Y/2Y full MFE·MAE는 임의 생성하지 않고, Reuters/WSJ/FT/AP/MarketWatch가 보도한 **event return, event price, operating profit, tariff cost, deal value, passenger/freight capacity, visitor data, market-cap wipeout**을 가격 anchor로 사용한다.

---

# 1. 이번 라운드 대섹터

```text
R9 = 모빌리티·운송·레저
```

R9에서 진짜 Stage 3는 “현대차”, “하이브리드”, “인도 IPO”, “항공 통합”, “중국 관광객”, “운임 반등”, “중동 물류 차질” 같은 headline이 아니다.

진짜 Stage 3는 아래가 같이 닫히는 순간이다.

```text
자동차:
판매량 → ASP/mix → tariff cost → 현지생산 hedge → 인센티브 → OP margin → FCF

물류/해운:
운임 상승 → 계약운임/spot mix → 선복 활용률 → 연료비 → 항로 안정성 → margin

항공:
탑승률 → yield → 유류비 → 안전신뢰 → 정비비 → 통합 synergy → regulatory remedy

레저/관광:
입국자 수 → 객단가 → 카지노/drop amount → 호텔 ADR/occupancy → 면세/소비 전환 → margin

IPO/해외자회사:
상장 가격 → aftermarket demand → 현지 판매/마진 → parent capital recycling → ROIC
```

---

# 2. 대상 canonical archetype

```text
AUTO_TARIFF_HYBRID_MIX_STAGE2
AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH
AIRLINE_CONSOLIDATION_STAGE2
AIRLINE_REMEDY_ROUTE_CARGO_STAGE2
AVIATION_SAFETY_HARD_4C
OVERSEAS_AUTO_IPO_FAILED_RERATING
CHINA_TOURISM_LEISURE_EVENT_PREMIUM
CONTAINER_SHIPPING_RATE_EVENT_PREMIUM
USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE
```

---

# 3. deep sub-archetype

```text
자동차 tariff / mix:
- Hyundai Motor / Kia
- U.S. 25% tariff → 15% relief
- tariff cost, hybrid mix, Genesis / high-margin models
- EV vs hybrid demand rotation

자동차 물류:
- Hyundai Motor / Hyundai Glovis
- Middle East route disruption
- Europe / North Africa exports
- fuel cost / rerouting / intermediate hubs

항공 통합:
- Korean Air / Asiana
- 63.88% stake
- international capacity ranking
- integration, LCC consolidation, frequent flyer merge, route remedies

항공 remedy:
- T’way Air new Europe routes
- Air Incheon / Asiana Cargo sale
- long-haul aircraft lease, pilots, maintenance support
- execution and profitability gate

안전 hard gate:
- Jeju Air fatal crash
- 179 deaths
- record-low share price
- safety inspection of entire airline-operation system

해외자회사 IPO:
- Hyundai Motor India
- $3.3B IPO
- weak debut
- weak demand and Red Sea export disruption

레저/관광:
- Paradise, Hotel Shilla, Hyundai Department Store, Hankook Cosmetics
- China group-tourist visa-free policy
- visitor count vs spend-per-head and margin

해운/운송:
- HMM read-through
- Red Sea rerouting
- freight rate squeeze and later normalization risk
- used-car export disruption through Hormuz / Dubai / Sri Lanka
```

---

# 4. 국장 신규 후보 case

## Case A — Hyundai Motor / Kia U.S. tariff & hybrid mix

```text
symbols = 005380 / 000270
case_type = success_candidate + 4C-watch
archetype = AUTO_TARIFF_HYBRID_MIX_STAGE2
```

### stage date

```text
Stage 1:
2025-04~2025-07
- U.S. imposes 25% tariff on Korean autos.
- Hyundai/Kia profitability exposed to U.S. market.

Stage 4C-watch:
2025-07-31
- U.S.-Korea deal sets tariff at 15%, lower than 25% but removes previous 2.5% FTA advantage vs Japan.
- Hyundai Motor -4.5%.
- Kia -6.6%.
- Korean automaker shares had already rallied on optimism, then sold off.

Stage 2 relief:
2025-10-30
- Hyundai Q3 OP down 29% to 2.5T won.
- U.S. tariffs cost Hyundai 1.8T won in Q3, up from 828B won in Q2.
- trade deal lowers tariff to 15%.
- Hyundai closes +2.7%.
- U.S. retail sales +12.7%.
- U.S. hybrid sales reach record 20% of U.S. sales.
- Europe eco-friendly vehicles account for 49% of sales.

Stage 3:
없음
- tariff relief + hybrid mix is Stage 2.
- Green requires sustained tariff pass-through, U.S. local production, incentive control, mix margin and FCF.
```

Hyundai/Kia는 R9 자동차에서 “좋은 회사인데 tariff가 margin을 먹는” 정석 case다. 2025년 7월 tariff deal 직후 Hyundai -4.5%, Kia -6.6%가 나왔고, 15% tariff가 25%보다 낮아도 한미 FTA로 갖던 2.5% advantage를 없앴다는 점이 핵심이다. 이후 Hyundai Q3에서는 tariff cost가 1.8T won까지 올라갔지만, hybrid mix와 U.S. sales가 완충하면서 주가는 +2.7%로 마감했다. 이건 Green이 아니라 **tariff shock를 hybrid/high-margin mix가 얼마나 흡수하는지 보는 Stage 2**다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "case_id": "r9_loop14_hyundai_kia_us_tariff_hybrid_mix",
  "symbols": "005380/000270",
  "stage2_date": "2025-10-30",
  "stage4c_watch_date": "2025-07-31",
  "stage3_price": null,
  "price_data_source": "Reuters auto-tariff deal and Hyundai Q3 earnings anchors",
  "hyundai_tariff_deal_event_mae_pct": -4.5,
  "kia_tariff_deal_event_mae_pct": -6.6,
  "tariff_prior_pct": 25,
  "tariff_new_pct": 15,
  "lost_fta_advantage_vs_japan_pct": 2.5,
  "q3_2025_op_krw_trn": 2.5,
  "q3_2025_op_yoy_pct": -29,
  "q3_2025_tariff_cost_krw_trn": 1.8,
  "q2_2025_tariff_cost_krw_bn": 828,
  "q3_2025_revenue_krw_trn": 46.7,
  "q3_2025_revenue_yoy_pct": 8.8,
  "hyundai_q3_event_mfe_pct": 2.7,
  "us_retail_sales_growth_pct": 12.7,
  "us_hybrid_sales_share_pct": 20,
  "europe_eco_friendly_sales_share_pct": 49,
  "mfe_30d_90d_180d_1y_2y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4C_watch
rerating_result = AUTO_TARIFF_HYBRID_MIX_STAGE2
stage_failure_type = tariff_relief_not_margin_green
```

---

## Case B — Hyundai Motor / Hyundai Glovis Middle East logistics shock

```text
symbols = 005380 / 086280
case_type = thesis_break_watch
archetype = AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH
```

### stage date

```text
Stage 1:
2026-03~2026-04
- Middle East conflict disrupts vehicle-export routes.
- Europe and North Africa exports normally transit through Middle East routes.

Stage 4C-watch:
2026-04-03
- Hyundai says exports to Europe and North Africa are disrupted.
- logistics costs rise, deliveries delayed, suppliers pressured.
- Hyundai Glovis cannot access some Middle East routes and temporarily stores cargo.
- shipments diverted to intermediate hubs such as Sri Lanka.
- March shipments to Middle East -49%.
- Hyundai global vehicle sales -2.3% YoY in March.
- Hyundai Motor -1.2%, Hyundai Glovis -0.7%, while KOSPI +2.7%.

Stage 4C-watch validation:
2026-04-23
- Hyundai Q1 2026 OP down 31% to 2.5T won.
- war, U.S. tariffs and macro risks cited.
- raw-material cost pressure around 200B won.
- Middle East/Africa accounted for 8% of 2025 wholesale sales.
- Middle East was highest-margin market per unit, but lost sales hard to reallocate.
```

이 case는 R9에서 “물류가 자동차 마진의 보이지 않는 기어박스”라는 교정값이다. Hyundai는 Middle East route disruption으로 Europe/North Africa export가 막히고, Hyundai Glovis는 일부 route 접근이 어려워 cargo를 임시 보관해야 했다. Hyundai와 Glovis가 각각 -1.2%, -0.7%였고 KOSPI는 +2.7%였다. 이후 Q1 OP -31%, 원재료 비용 200B won 부담, high-margin Middle East 판매 손실이 확인됐다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r9_loop14_hyundai_glovis_middle_east_logistics_4c_watch",
  "symbols": "005380/086280",
  "stage4c_watch_date": "2026-04-03/2026-04-23",
  "stage3_price": null,
  "price_data_source": "Reuters Hyundai export disruption and Q1 earnings anchors",
  "hyundai_event_mae_pct": -1.2,
  "hyundai_glovis_event_mae_pct": -0.7,
  "kospi_same_context_pct": 2.7,
  "hyundai_relative_underperformance_pp": -3.9,
  "glovis_relative_underperformance_pp": -3.4,
  "middle_east_shipments_decline_pct": -49,
  "hyundai_march_global_sales_yoy_pct": -2.3,
  "q1_2026_op_krw_trn": 2.5,
  "q1_2026_op_yoy_pct": -31,
  "q1_raw_material_cost_impact_krw_bn": 200,
  "middle_east_africa_wholesale_sales_share_2025_pct": 8,
  "hybrid_share_total_shipments_q1_2026_pct": 18,
  "us_hybrid_share_q1_2026_pct": 25,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break_watch
rerating_result = AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH
stage_failure_type = route_disruption_high_margin_market_loss
```

---

## Case C — Korean Air / Asiana integration

```text
symbol = 003490 / 020560
case_type = success_candidate
archetype = AIRLINE_CONSOLIDATION_STAGE2
```

### stage date

```text
Stage 1:
2020~2024
- Korean Air pursues Asiana acquisition.
- multi-year global antitrust process delays completion.

Stage 2:
2024-12-12
- Korean Air completes Asiana takeover.
- deal value around $1.3B.
- Korean Air holds 63.88% Asiana stake.
- Asiana becomes subsidiary first, full integration within about two years.
- combined group becomes world’s 12th largest by international capacity.
- no layoffs promised; overlapping staff to be reassigned.
- LCCs to be combined into one entity.

Stage 2 validation:
2025-02-07
- Korean Air 2024 revenue: 16T won, +10.6% YoY.
- 2024 OP: 2T won, +22.5% YoY.
- Q4 cargo revenue +9%, passenger revenue -3%.
- integration with Asiana is still planned over two years.
```

Korean Air/Asiana는 R9 항공 consolidation Stage 2다. 통합은 구조적으로 크지만, Stage 3는 regulatory remedy, 노선 최적화, frequent flyer integration, LCC 통합, 정비·안전·인력 비용을 지나야 한다. Korean Air는 2024년 record revenue 16T won과 OP 2T won을 냈지만, Q4 passenger revenue는 -3%였고 cargo revenue +9%가 받쳤다. 즉 항공 통합은 “합병 완료”가 아니라 **yield·load factor·cargo mix·integration cost**가 핵심이다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "case_id": "r9_loop14_korean_air_asiana_integration_stage2",
  "symbol": "003490/020560",
  "stage2_date": "2024-12-12/2025-02-07",
  "stage3_price": null,
  "price_data_source": "Reuters Korean Air-Asiana completion and 2024 annual earnings anchors",
  "acquisition_value_usd_bn": 1.3,
  "asiana_stake_pct": 63.88,
  "integration_period_years_context": 2,
  "international_capacity_rank_context": 12,
  "revenue_2024_krw_trn": 16,
  "revenue_2024_yoy_pct": 10.6,
  "op_2024_krw_trn": 2,
  "op_2024_yoy_pct": 22.5,
  "q4_cargo_revenue_yoy_pct": 9,
  "q4_passenger_revenue_yoy_pct": -3,
  "direct_event_return": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["integration cost", "route optimization", "load factor", "yield", "LCC consolidation", "safety/service quality"]
}
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = AIRLINE_CONSOLIDATION_STAGE2
stage_failure_type = merger_completion_not_yield_synergy_green
```

---

## Case D — T’way Air / Air Incheon merger remedies

```text
symbols = 091810 / Air Incheon unlisted
case_type = success_candidate + execution_watch
archetype = AIRLINE_REMEDY_ROUTE_CARGO_STAGE2
```

### stage date

```text
Stage 1:
2024-02~2024-03
- Korean Air/Asiana merger remedies create new route/cargo opportunities.
- EU conditions require Europe-route transfer and cargo divestment.

Stage 2:
2024-03-07
- T’way Air sees “golden opportunity” from new EU routes.
- receives routes to Paris, Rome, Barcelona and Frankfurt.
- routes start June~October.
- Korean Air to lease five A330-200 aircraft.
- Korean Air to provide 100 pilots and maintenance support.
- T’way targets 30%~40% growth in 2024.

Stage 2 cargo:
2024-08-07
- Asiana cargo unit sold to Air Incheon for 470B won / $342M.
- cargo unit includes fleet, staff, customers and traffic rights.
- Air Incheon becomes South Korea’s second-largest freight carrier.
- Asiana cargo operations include 11 freighters and 25 cities in 12 countries.

Stage 3:
없음
- route/cargo remedy is Stage 2.
- Green requires load factor, yield, aircraft utilization, cargo contract retention, maintenance reliability and financing.
```

T’way/Air Incheon은 Korean Air/Asiana merger의 remedy beneficiary다. 하지만 “노선 받았다”가 곧 Green은 아니다. T’way는 유럽 장거리 route를 받고 30~40% growth를 목표로 했지만, Korean Air의 항공기·조종사·정비지원에 의존한다. Air Incheon은 470B won에 Asiana cargo를 인수해 2위 화물항공사가 되지만, 11대 freighter, 인력, 고객, traffic rights를 흡수해야 한다. 실행 risk가 크다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r9_loop14_tway_air_incheon_airline_remedy_stage2",
  "symbols": "091810/Air_Incheon_unlisted",
  "stage2_date": "2024-03-07/2024-08-07",
  "stage3_price": null,
  "price_data_source": "Reuters T’way Europe-route remedy and Air Incheon cargo-sale anchors",
  "tway_new_eu_routes": ["Paris", "Rome", "Barcelona", "Frankfurt"],
  "route_start_period": "2024-06_to_2024-10",
  "leased_a330_200_aircraft": 5,
  "pilot_support_count": 100,
  "tway_2024_growth_target_pct": "30-40",
  "asiana_cargo_sale_krw_bn": 470,
  "asiana_cargo_sale_usd_mn": 342,
  "asiana_cargo_freighters": 11,
  "asiana_cargo_cities": 25,
  "asiana_cargo_countries": 12,
  "direct_event_return": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["load_factor", "yield", "aircraft_utilization", "cargo_customer_retention", "maintenance_reliability"]
}
```

### alignment

```text
score_price_alignment = success_candidate_execution_watch
rerating_result = AIRLINE_REMEDY_ROUTE_CARGO_STAGE2
stage_failure_type = route_rights_and_cargo_assets_not_operating_margin_green
```

---

## Case E — Jeju Air crash / aviation safety hard 4C

```text
symbol = 089590
case_type = hard_4C
archetype = AVIATION_SAFETY_HARD_4C
```

### stage date

```text
Stage 1:
2024-12-29
- Jeju Air Boeing 737-800 crashes at Muan International Airport.
- 179 fatalities.
- first fatal crash for Jeju Air since foundation.

Stage 4C:
2024-12-30
- Jeju Air shares fall as much as -15.7%.
- intraday low: 6,920 won.
- shares down 8.5% at 0312 GMT.
- market-cap wipeout up to 95.7B won / $65.2M.
- AK Holdings -12%.
- acting president orders emergency safety inspection of entire airline-operation system.
```

Jeju Air는 R9에서 가장 명확한 hard 4C다. 항공사는 yield, load factor, tourism rebound보다 **safety trust**가 먼저다. Jeju Air 사고는 주가를 장중 -15.7%까지 밀었고, 시총 95.7B won을 지웠다. 이 case는 R9 scoring에서 안전사고가 나면 demand·valuation·관광회복 logic을 즉시 덮는 hard gate다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r9_loop14_jeju_air_safety_hard_4c",
  "symbol": "089590",
  "stage4c_date": "2024-12-30",
  "stage3_price": null,
  "price_data_source": "Reuters Jeju Air crash event-price anchor",
  "fatalities": 179,
  "event_low_price_krw": 6920,
  "event_intraday_mae_pct": -15.7,
  "event_mid_session_mae_pct": -8.5,
  "market_cap_wipeout_krw_bn": 95.7,
  "market_cap_wipeout_usd_mn": 65.2,
  "ak_holdings_event_mae_pct": -12,
  "safety_inspection_ordered": true,
  "mfe_30d_90d_180d_1y": "N/A_after_4C",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = AVIATION_SAFETY_HARD_4C
stage_failure_type = fatal_safety_event_overrides_travel_demand
```

---

## Case F — Hyundai Motor India IPO / overseas mobility failed rerating

```text
symbol = 005380 / HYUN.NS
case_type = failed_rerating
archetype = OVERSEAS_AUTO_IPO_FAILED_RERATING
```

### stage date

```text
Stage 1:
2024-10-14
- Hyundai Motor India launches $3.3B IPO.
- parent sells up to 17.5% stake.
- valuation target up to $19B.
- first listing outside Korea.

Stage 4C-watch / failed debut:
2024-10-22
- IPO offer price: 1,960 rupees.
- listing price: 1,934 rupees.
- traded at 1,882.10 rupees.
- shares drop as much as -6%.
- valuation: 1.53T rupees / $18.2B, below $19B target.
- IPO was oversubscribed more than 2x but retail response weak.

Stage 4C-watch validation:
2024-11-12
- Q2 profit -16.5%.
- domestic sales -6%.
- exports -17% due Red Sea disruption.
- revenue -7.5% to 169.61B rupees.
- volumes -9%.
- shares fell nearly -3% before recovering to about -1%.
```

Hyundai Motor India는 R9의 해외 mobility IPO failed rerating이다. 인도 시장과 SUV portfolio는 구조적으로 좋지만, IPO pricing이 빡빡하면 바로 price test에서 깨진다. 상장일 -6%, 이후 첫 실적에서 profit -16.5%, exports -17%는 “인도 성장”도 **valuation·domestic demand·export logistics**를 통과해야 한다는 증거다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r9_loop14_hyundai_india_ipo_failed_rerating",
  "symbols": "005380/HYUN.NS",
  "stage2_date": "2024-10-14",
  "stage4c_watch_date": "2024-10-22/2024-11-12",
  "stage3_price": null,
  "price_data_source": "Reuters Hyundai Motor India IPO debut and Q2 earnings anchors",
  "ipo_value_usd_bn": 3.3,
  "parent_stake_sale_pct": 17.5,
  "target_valuation_usd_bn": 19,
  "offer_price_inr": 1960,
  "listing_price_inr": 1934,
  "morning_trade_price_inr": 1882.10,
  "debut_mae_pct": -6.0,
  "valuation_debut_inr_trn": 1.53,
  "valuation_debut_usd_bn": 18.2,
  "market_share_india_pct": 15,
  "ipo_oversubscription": "more_than_2x",
  "q2_profit_decline_pct": -16.5,
  "q2_profit_inr_bn": 13.38,
  "domestic_sales_decline_pct": -6,
  "exports_decline_pct": -17,
  "q2_revenue_inr_bn": 169.61,
  "q2_revenue_decline_pct": -7.5,
  "volume_decline_pct": -9,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = failed_rerating
rerating_result = OVERSEAS_AUTO_IPO_QUALITY_GATE
stage_failure_type = IPO_size_and_India_growth_not_aftermarket_margin_green
```

---

## Case G — China tourism / leisure basket

```text
symbols = 034230 / 008770 / 069960 / 123690
company_scope = Paradise / Hotel Shilla / Hyundai Department Store / Hankook Cosmetics
case_type = event_premium + 4B-watch
archetype = CHINA_TOURISM_LEISURE_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2025-03-20
- South Korea announces plan to allow visa-free Chinese tourist groups.
- leisure, hotel, casino and retail names become event beneficiaries.

Stage 2:
2025-08-06
- visa-free entry period set from 2025-09-29 to 2026-06.
- 2024 foreign visitors to Korea: 16.4M, +48% YoY.
- Chinese nationals account for 28%, the largest group.
- 2025 visitor target: 18.5M.
- Hyundai Department Store +7.1%.
- Hotel Shilla +4.8%.
- Paradise +2.9%.
- Hankook Cosmetics +9.9%.

Stage 4B:
- policy rally occurs before actual casino drop amount, hotel ADR/occupancy, duty-free conversion and spending per head.
```

China tourism basket은 R9 leisure event premium이다. 방문객 수 headline은 바로 주가를 움직였지만, leisure Green은 입국자 수가 아니라 casino drop, hotel ADR/occupancy, duty-free conversion, spend-per-head다. 2025년 10월에는 반중·반외국인 집회 단속까지 나왔는데, 이것도 관광 thesis가 단순 입국정책이 아니라 destination safety/image와 붙어 있음을 보여준다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r9_loop14_china_tourism_leisure_basket",
  "symbols": "034230/008770/069960/123690",
  "stage2_date": "2025-08-06",
  "stage4b_date": "2025-08-06",
  "stage3_price": null,
  "price_data_source": "Reuters China group-tourist visa-free and leisure-stock reaction anchors",
  "visa_free_start": "2025-09-29",
  "visa_free_end": "2026-06",
  "visitors_2024_mn": 16.4,
  "visitors_2024_yoy_growth_pct": 48,
  "chinese_visitor_share_2024_pct": 28,
  "visitor_target_2025_mn": 18.5,
  "hyundai_department_store_event_mfe_pct": 7.1,
  "hotel_shilla_event_mfe_pct": 4.8,
  "paradise_event_mfe_pct": 2.9,
  "hankook_cosmetics_event_mfe_pct": 9.9,
  "casino_drop_amount_confirmed": false,
  "hotel_adr_occupancy_confirmed": false,
  "tourist_spend_per_head_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
rerating_result = CHINA_TOURISM_LEISURE_EVENT_STAGE2
stage_failure_type = visitor_count_not_spend_margin_green
```

---

## Case H — HMM / Red Sea freight-rate cycle

```text
symbol = 011200
case_type = event_premium + 4B-watch
archetype = CONTAINER_SHIPPING_RATE_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2024-05~2024-07
- Red Sea disruption forces ships around Cape of Good Hope.
- rerouting ties up vessel capacity and lifts freight rates.
- Korean container carrier HMM is read-through beneficiary.

Stage 2:
2024-07-03
- Hapag-Lloyd says Red Sea rerouting and Asia congestion tied up 5%~9% of global vessel capacity.
- Freightos spot container index rose 40% in six weeks to $5,068.
- global container-space demand expected +3%~4% YoY in 2024.

Stage 4B:
- freight-rate rally is cyclical and route-security dependent.
- if Suez/Red Sea normalizes, added capacity can pressure rates.

Stage 4C-watch:
2025-10-09
- Maersk -2% on expectations Gaza ceasefire may eventually restore Red Sea/Suez route.
- analysts say return to Suez would increase available shipping capacity and pressure freight rates.
```

HMM은 R9 transport에서 freight-rate event premium이다. Red Sea disruption은 선박을 오래 묶어 운임을 올리지만, 이건 structural Stage 3가 아니라 route-security cycle이다. Hapag-Lloyd는 global vessel capacity 5~9%가 묶였고 Freightos spot index가 6주에 40% 올랐다고 했지만, 2025년 Gaza ceasefire 기대에는 Maersk가 -2%로 반응했다. 즉 해운주는 운임 상승보다 **운임 지속성, contract mix, fuel cost, route normalization risk**가 Stage 3 gate다. ([Reuters][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r9_loop14_hmm_red_sea_freight_rate_event_premium",
  "symbol": "011200",
  "stage2_date": "2024-07-03",
  "stage4c_watch_date": "2025-10-09",
  "stage3_price": null,
  "price_data_source": "Reuters Hapag-Lloyd / Maersk Red Sea freight-rate cycle anchors",
  "global_vessel_capacity_tied_pct": "5-9",
  "freightos_spot_index_6w_growth_pct": 40,
  "freightos_spot_index_usd": 5068,
  "global_container_demand_growth_2024_pct": "3-4",
  "maersk_ceasefire_event_mae_pct": -2,
  "rate_normalization_risk": true,
  "hmm_direct_event_price": "price_data_unavailable_after_deep_search",
  "stage3_conditions": ["contract_rate_mix", "fuel_cost", "vessel_utilization", "route_security", "cash_yield"]
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
rerating_result = CONTAINER_SHIPPING_RATE_EVENT_STAGE2
stage_failure_type = freight_rate_spike_not_durable_yield_green
```

---

## Case I — Korea used-car export logistics shock

```text
symbols = used-car exporters / HMM / Hyundai Glovis read-through
case_type = 4C-reference
archetype = USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE
```

### stage date

```text
Stage 1:
2026-03-24
- Iran conflict disrupts Strait of Hormuz / Dubai route.
- Asia used-car export trade is hit.

Stage 4C-reference:
2026-03-24
- Japan and South Korea exported combined $19B worth of used cars last year.
- more than one-third of South Korea’s 883,000 used-car exports went to Middle East.
- Incheon storage complex: about 80% of cars normally bound for Middle East.
- more than 70% of one shipping-company vehicles stuck in storage.
- some HMM containers stuck near Mumbai.
- one exporter has more than half of 6.6B won annual revenue tied to UAE.
```

이 case는 상장사 hard 4C가 아니라 R9 logistics reference다. 한국의 중고차 수출·항만·해운·PCTC·물류는 실제로 Dubai/Strait of Hormuz route에 걸린다. Reuters는 한국 중고차 883,000대 중 1/3 이상이 Middle East로 향했고, 인천 storage complex의 약 80% 물량이 Middle East-bound였으며, 일부 차량은 storage에 stuck 상태라고 보도했다. 이건 자동차 수출·물류 scoring에서 **최종수요와 항로가 같이 닫혀야 한다**는 보정값이다. ([Reuters][9])

### 실제 가격경로 검증

```json
{
  "case_id": "r9_loop14_korea_used_car_export_logistics_shock",
  "symbols": "used_car_exporters/HMM/Hyundai_Glovis_readthrough",
  "stage4c_watch_date": "2026-03-24",
  "stage3_price": null,
  "price_data_source": "Reuters used-car export logistics shock anchor",
  "japan_korea_used_car_exports_usd_bn": 19,
  "korea_used_car_exports_units": 883000,
  "korea_used_car_exports_middle_east_share_pct": "more_than_one_third",
  "incheon_storage_middle_east_bound_share_pct": 80,
  "stuck_storage_share_context_pct": 70,
  "exporter_revenue_tied_to_uae_krw_bn": 6.6,
  "hmm_containers_stuck_near": "Mumbai",
  "listed_direct_price": "price_data_unavailable_after_deep_search",
  "use_as_transport_logistics_4c_reference": true
}
```

### alignment

```text
score_price_alignment = thesis_break_reference
rerating_result = USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE
stage_failure_type = demand_destination_route_disruption
```

---

# 5. 이번 R9 case별 stage date 요약

| case                      | Stage 1     | Stage 2             | Stage 3 | Stage 4B                  | Stage 4C                           |
| ------------------------- | ----------- | ------------------- | ------- | ------------------------- | ---------------------------------- |
| Hyundai/Kia tariff        | 2025-04~07  | 2025-10 Q3 relief   | N/A     | tariff-relief rally watch | 2025-07 tariff selloff             |
| Hyundai/Glovis logistics  | 2026-03~04  | N/A                 | N/A     | N/A                       | 2026-04 route disruption           |
| Korean Air/Asiana         | 2020~2024   | 2024-12 / 2025-02   | N/A     | merger synergy watch      | integration/safety/fuel-cost watch |
| T’way/Air Incheon         | 2024-03     | routes/cargo remedy | N/A     | route premium watch       | execution/capacity watch           |
| Jeju Air                  | 2024-12-29  | N/A                 | N/A     | N/A                       | 2024-12-30 hard                    |
| Hyundai India             | 2024-10 IPO | 2024-10             | N/A     | IPO valuation watch       | debut failure / weak demand        |
| China tourism leisure     | 2025-03     | 2025-08 policy      | N/A     | tourism rally             | spend conversion watch             |
| HMM freight cycle         | 2024-07     | freight-rate spike  | N/A     | rate cycle overheat       | route normalization watch          |
| Used-car export logistics | 2026-03     | N/A                 | N/A     | N/A                       | route disruption reference         |

---

# 6. 실제 가격경로 검증 총괄

| case                      |                                                    가격·사업 anchor | 해석                                | 판정                     |
| ------------------------- | --------------------------------------------------------------: | --------------------------------- | ---------------------- |
| Hyundai/Kia tariff        |                   Hyundai -4.5%, Kia -6.6%, later Hyundai +2.7% | tariff shock + hybrid/mix Stage 2 | success_candidate      |
| Hyundai/Glovis logistics  |            Hyundai -1.2%, Glovis -0.7%, KOSPI +2.7%; Q1 OP -31% | route disruption 4C-watch         | thesis_break_watch     |
| Korean Air/Asiana         |                        63.88% stake, revenue 16T won, OP 2T won | consolidation Stage 2             | success_candidate      |
| T’way/Air Incheon         |             EU routes, 5 A330s, 100 pilots, cargo sale 470B won | remedy beneficiary Stage 2        | success_candidate      |
| Jeju Air                  |                        -15.7%, low 6,920 won, 95.7B won wipeout | safety hard 4C                    | thesis_break           |
| Hyundai India             |                       debut -6%, Q2 profit -16.5%, exports -17% | overseas IPO failed rerating      | failed_rerating        |
| Tourism/leisure           |          Hyundai Dept +7.1%, Hotel Shilla +4.8%, Paradise +2.9% | visitor headline event premium    | event_premium          |
| HMM/Red Sea               | Freightos +40%, capacity tied 5~9%, Maersk -2% on normalization | freight-cycle premium             | event_premium          |
| Used-car export logistics |                883k Korea used-car exports, >1/3 to Middle East | route/destination 4C reference    | thesis_break_reference |

---

# 7. score-price alignment 판정

```text
aligned:
- 없음. R9 이번 라운드는 대부분 Stage 2 또는 4C-watch.

structural_success_candidate:
- Korean Air/Asiana, if integration synergy, yield and LCC consolidation confirm.
- Hyundai/Kia, if tariff pass-through and hybrid/high-margin mix hold.
- T’way/Air Incheon, if route/cargo remedy converts into load factor/yield.

success_candidate:
- Hyundai/Kia tariff/hybrid mix.
- Korean Air/Asiana consolidation.
- T’way/Air Incheon remedy beneficiary.
- China tourism/leisure basket, but only Stage 2.

failed_rerating:
- Hyundai Motor India IPO.
- Hyundai India Q2 post-listing earnings.

overheat / 4B-watch:
- China tourism retail/leisure rally.
- HMM/Red Sea freight-rate spike if treated as durable.
- Korean Air merger synergy before integration cost is visible.

price_moved_without_evidence:
- tourist visa-free headline if treated as casino/hotel margin.
- freight-rate spike if treated as long-term shipping Green.
- tariff relief if treated as auto margin recovery without pass-through.
- route/cargo remedy if treated as T’way/Air Incheon margin before load factor.

evidence_good_but_price_failed:
- Hyundai/Kia tariff relief day, because tariff still removed FTA advantage and stocks sold off.
- Korean Air integration if merger completion is scored before yield/synergy.

thesis_break:
- Jeju Air fatal crash.

thesis_break_watch:
- Hyundai/Glovis Middle East route disruption.
- Hyundai India weak demand/export disruption.
- HMM Red Sea normalization risk.
```

---

# 8. 점수비중 교정

## 올릴 축

```text
tariff_pass_through +5
hybrid_mix_margin +5
local_production_hedge +5
route_security_continuity +5
logistics_cost_control +5
load_factor_yield +5
aviation_safety_trust +5
integration_synergy_execution +5
tourist_spend_per_head +5
freight_rate_durability +5
```

### 왜 올리나

Hyundai/Kia tariff case는 tariff relief가 나와도 주가가 빠질 수 있음을 보여줬다. Hyundai/Glovis는 route security와 logistics cost가 자동차 margin의 하부 gear임을 보여준다. Korean Air/Asiana는 통합이 완료되어도 yield, LCC integration, route remedy가 닫혀야 한다. Jeju Air는 safety trust가 항공주 hard gate임을 증명했다. Tourism basket은 visitor count보다 spend-per-head가 중요하고, HMM은 spot freight spike보다 rate durability가 중요하다.

## 내릴 축

```text
tariff_relief_headline_only -5
visitor_count_only -5
merger_completion_only -5
route_rights_without_load_factor -5
cargo_asset_purchase_without_customer_retention -5
freight_spot_rate_only -5
overseas_IPO_size_only -5
EV_or_hybrid_mix_without_margin -4
safety_risk_unresolved -5
```

### 왜 내리나

R9는 headline이 매우 그럴듯하다. “관세 인하”, “항공 통합”, “중국 관광객”, “운임 급등”, “인도 IPO”는 모두 가격을 움직인다. 하지만 Stage 3는 운영지표다. 자동차는 tariff와 mix margin, 항공은 yield와 안전, 관광은 소비전환, 해운은 운임 지속성과 연료비가 닫혀야 한다.

---

# 9. Green gate 강화 조건

```text
R9 Stage 3-Green 필수:
1. 자동차는 tariff pass-through와 local production hedge 확인.
2. hybrid/Genesis/high-margin mix가 OP margin으로 확인.
3. 물류는 route security, rerouting cost, delivery delay, fuel cost 확인.
4. 항공은 load factor, passenger yield, cargo yield, fuel cost, safety trust 확인.
5. 항공 M&A는 integration cost, route remedy, LCC consolidation, frequent flyer integration 확인.
6. tourism/leisure는 visitor count보다 spend-per-head, occupancy, casino drop, hotel ADR 확인.
7. shipping은 spot rate가 아니라 contract rate mix, vessel utilization, Suez/Red Sea normalization risk 확인.
8. IPO는 offer price가 아니라 aftermarket demand와 first earnings 확인.
9. price path가 evidence 이후 따라옴.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch:
- tariff relief headline으로 자동차주 급등.
- 중국 관광객 visa-free로 카지노/호텔/면세/레저주 급등.
- freight spot rate 급등으로 해운주 선반영.
- airline merger completion만으로 synergy 선반영.
- T’way/Air Incheon route/cargo remedy를 margin으로 바로 가격화.
- overseas subsidiary IPO valuation이 parent rerating으로 바로 연결.
```

---

# 11. 4C hard gate 조건

```text
Hard 4C:
- fatal aviation safety event.
- route disruption that blocks high-margin exports.
- tariff shock not passed through to price.
- major fuel-cost spike without surcharge recovery.
- airline integration failure / safety inspection escalation.
- tourism arrivals without spend conversion.
- freight-rate normalization after spot-rate rally.
- overseas IPO weak debut plus weak first earnings.
```

이번 R9 Loop 14의 hard 4C는 **Jeju Air fatal crash**다. Hyundai/Glovis logistics shock, Hyundai India weak debut, HMM freight-rate normalization risk, tourism spend-conversion risk는 hard 4C가 아니라 **4C-watch / event premium / failed rerating**으로 둔다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_219.md 요약

```md
# R9 Loop 14. Mobility / Transport / Leisure Price Validation

이번 라운드는 R9 Loop 14 price-validation 라운드다.

핵심 결론:
- Hyundai Motor / Kia tariff case is Stage 2 plus 4C-watch. On July 31 2025, Hyundai -4.5% and Kia -6.6% after the U.S.-Korea 15% auto tariff deal because the rate removed Korea’s previous 2.5% FTA advantage versus Japan. In Q3 2025, Hyundai OP fell 29% to 2.5T won, tariff cost reached 1.8T won, but shares closed +2.7% as hybrid mix and U.S. sales cushioned the hit.
- Hyundai Motor / Hyundai Glovis Middle East logistics shock is 4C-watch. On Apr. 3 2026, Hyundai -1.2% and Glovis -0.7% while KOSPI +2.7% as Middle East route disruption raised costs and delayed exports. Q1 2026 OP later fell 31% to 2.5T won.
- Korean Air / Asiana is airline consolidation Stage 2. Korean Air completed $1.3B Asiana takeover, taking 63.88% stake. 2024 revenue reached 16T won and OP 2T won, but integration, LCC consolidation, yield and fuel cost remain gates.
- T’way Air / Air Incheon are merger-remedy Stage 2 cases. T’way receives Europe routes with five A330-200s and 100 pilot/maintenance support; Air Incheon acquires Asiana Cargo for 470B won. Load factor, yield, cargo customer retention and aircraft utilization required.
- Jeju Air is hard 4C. Fatal crash killed 179 people; shares fell as much as -15.7% to 6,920 won and wiped out up to 95.7B won market cap.
- Hyundai Motor India is failed rerating. $3.3B IPO fell as much as -6% on debut, listed below 1,960 rupee offer price, and first post-listing quarter showed profit -16.5%, domestic sales -6%, exports -17%.
- China tourism/leisure basket is event premium. Visa-free Chinese group-tourist policy drove Hyundai Department Store +7.1%, Hotel Shilla +4.8%, Paradise +2.9%, Hankook Cosmetics +9.9%. Spend-per-head and margin required.
- HMM/Red Sea freight-rate cycle is event premium. Red Sea disruption tied up 5%~9% global vessel capacity and Freightos spot index rose 40% in six weeks, but Maersk later fell -2% on route-normalization expectations.
- Used-car export logistics shock is R9 4C reference. Japan and South Korea exported $19B used cars last year; more than one-third of Korea’s 883,000 used-car exports went to the Middle East, and route disruption left vehicles stuck in storage or at sea.
```

## docs/checkpoints/checkpoint_28a_round219_r9_loop14.md 요약

```md
# Checkpoint 28A Round 219 R9 Loop 14 Mobility Transport Leisure Price Validation

## 반영 내용
- R9 Loop 14 price-validation 라운드를 추가했다.
- Hyundai/Kia tariff and hybrid mix, Hyundai/Glovis Middle East logistics shock, Korean Air/Asiana integration, T’way/Air Incheon remedy beneficiaries, Jeju Air hard 4C, Hyundai Motor India IPO, China tourism leisure basket, HMM/Red Sea freight cycle, used-car export logistics shock를 비교했다.
- Reuters / WSJ / FT / AP / MarketWatch anchors로 가능한 event MFE/MAE, event price, OP, tariff cost, deal value, visitor data, freight-rate cycle metrics를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- tariff pass-through, hybrid mix margin, local production hedge, route security continuity, logistics cost control, load factor/yield, aviation safety trust, integration synergy execution, tourist spend per head, freight-rate durability 가중치 강화.
- tariff relief headline-only, visitor count-only, merger completion-only, route rights without load factor, cargo asset purchase without customer retention, freight spot rate-only, overseas IPO size-only, safety risk unresolved 감점 강화.
```

## data/e2r_case_library/cases_r9_loop14_round219.jsonl 초안

```jsonl
{"case_id":"r9_loop14_hyundai_kia_us_tariff_hybrid_mix","symbol":"005380/000270","company_name":"Hyundai Motor / Kia","case_type":"success_candidate_4c_watch","primary_archetype":"AUTO_TARIFF_HYBRID_MIX_STAGE2","stage2_date":"2025-10-30","stage4c_date":"2025-07-31_watch","price_validation":{"price_data_source":"Reuters auto-tariff deal and Hyundai Q3 earnings anchors","stage3_price":null,"hyundai_tariff_deal_event_mae_pct":-4.5,"kia_tariff_deal_event_mae_pct":-6.6,"tariff_prior_pct":25,"tariff_new_pct":15,"lost_fta_advantage_vs_japan_pct":2.5,"q3_2025_op_krw_trn":2.5,"q3_2025_op_yoy_pct":-29,"q3_2025_tariff_cost_krw_trn":1.8,"q2_2025_tariff_cost_krw_bn":828,"q3_2025_revenue_krw_trn":46.7,"q3_2025_revenue_yoy_pct":8.8,"hyundai_q3_event_mfe_pct":2.7,"us_retail_sales_growth_pct":12.7,"us_hybrid_sales_share_pct":20,"europe_eco_friendly_sales_share_pct":49,"mfe_30d_90d_180d_1y_2y":"price_data_unavailable_after_deep_search","mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_4C_watch","rerating_result":"AUTO_TARIFF_HYBRID_MIX_STAGE2","notes":"Tariff relief and hybrid mix are Stage 2; sustained pass-through and margin needed."}
{"case_id":"r9_loop14_hyundai_glovis_middle_east_logistics_4c_watch","symbol":"005380/086280","company_name":"Hyundai Motor / Hyundai Glovis","case_type":"thesis_break_watch","primary_archetype":"AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH","stage4c_date":"2026-04-03/2026-04-23_watch","price_validation":{"price_data_source":"Reuters Hyundai export disruption and Q1 earnings anchors","stage3_price":null,"hyundai_event_mae_pct":-1.2,"hyundai_glovis_event_mae_pct":-0.7,"kospi_same_context_pct":2.7,"hyundai_relative_underperformance_pp":-3.9,"glovis_relative_underperformance_pp":-3.4,"middle_east_shipments_decline_pct":-49,"hyundai_march_global_sales_yoy_pct":-2.3,"q1_2026_op_krw_trn":2.5,"q1_2026_op_yoy_pct":-31,"q1_raw_material_cost_impact_krw_bn":200,"middle_east_africa_wholesale_sales_share_2025_pct":8,"hybrid_share_total_shipments_q1_2026_pct":18,"us_hybrid_share_q1_2026_pct":25,"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","rerating_result":"AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH","notes":"Route disruption and high-margin market loss are explicit mobility 4C-watch gates."}
{"case_id":"r9_loop14_korean_air_asiana_integration_stage2","symbol":"003490/020560","company_name":"Korean Air / Asiana Airlines","case_type":"success_candidate_price_unavailable","primary_archetype":"AIRLINE_CONSOLIDATION_STAGE2","stage2_date":"2024-12-12/2025-02-07","price_validation":{"price_data_source":"Reuters Korean Air-Asiana completion and 2024 annual earnings anchors","stage3_price":null,"acquisition_value_usd_bn":1.3,"asiana_stake_pct":63.88,"integration_period_years_context":2,"international_capacity_rank_context":12,"revenue_2024_krw_trn":16,"revenue_2024_yoy_pct":10.6,"op_2024_krw_trn":2,"op_2024_yoy_pct":22.5,"q4_cargo_revenue_yoy_pct":9,"q4_passenger_revenue_yoy_pct":-3,"direct_event_return":"price_data_unavailable_after_deep_search","stage3_conditions":["integration cost","route optimization","load factor","yield","LCC consolidation","safety/service quality"]},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"AIRLINE_CONSOLIDATION_STAGE2","notes":"Merger completion is Stage 2; yield, load factor, LCC consolidation and integration cost required."}
{"case_id":"r9_loop14_tway_air_incheon_airline_remedy_stage2","symbol":"091810/Air_Incheon_unlisted","company_name":"T’way Air / Air Incheon","case_type":"success_candidate_execution_watch","primary_archetype":"AIRLINE_REMEDY_ROUTE_CARGO_STAGE2","stage2_date":"2024-03-07/2024-08-07","price_validation":{"price_data_source":"Reuters T’way Europe-route remedy and Air Incheon cargo-sale anchors","stage3_price":null,"tway_new_eu_routes":["Paris","Rome","Barcelona","Frankfurt"],"route_start_period":"2024-06_to_2024-10","leased_a330_200_aircraft":5,"pilot_support_count":100,"tway_2024_growth_target_pct":"30-40","asiana_cargo_sale_krw_bn":470,"asiana_cargo_sale_usd_mn":342,"asiana_cargo_freighters":11,"asiana_cargo_cities":25,"asiana_cargo_countries":12,"direct_event_return":"price_data_unavailable_after_deep_search","stage3_conditions":["load_factor","yield","aircraft_utilization","cargo_customer_retention","maintenance_reliability"]},"score_price_alignment":"success_candidate_execution_watch","rerating_result":"AIRLINE_REMEDY_ROUTE_CARGO_STAGE2","notes":"Route rights and cargo assets need operating execution, yield and customer retention."}
{"case_id":"r9_loop14_jeju_air_safety_hard_4c","symbol":"089590","company_name":"Jeju Air","case_type":"hard_4c","primary_archetype":"AVIATION_SAFETY_HARD_4C","stage4c_date":"2024-12-30","price_validation":{"price_data_source":"Reuters Jeju Air crash event-price anchor","stage3_price":null,"fatalities":179,"event_low_price_krw":6920,"event_intraday_mae_pct":-15.7,"event_mid_session_mae_pct":-8.5,"market_cap_wipeout_krw_bn":95.7,"market_cap_wipeout_usd_mn":65.2,"ak_holdings_event_mae_pct":-12,"safety_inspection_ordered":true,"mfe_30d_90d_180d_1y":"N/A_after_4C","mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","rerating_result":"AVIATION_SAFETY_HARD_4C","notes":"Fatal safety event overrides travel-demand and valuation logic."}
{"case_id":"r9_loop14_hyundai_india_ipo_failed_rerating","symbol":"005380/HYUN.NS","company_name":"Hyundai Motor / Hyundai Motor India","case_type":"failed_rerating","primary_archetype":"OVERSEAS_AUTO_IPO_FAILED_RERATING","stage2_date":"2024-10-14","stage4c_date":"2024-10-22/2024-11-12_watch","price_validation":{"price_data_source":"Reuters Hyundai Motor India IPO debut and Q2 earnings anchors","stage3_price":null,"ipo_value_usd_bn":3.3,"parent_stake_sale_pct":17.5,"target_valuation_usd_bn":19,"offer_price_inr":1960,"listing_price_inr":1934,"morning_trade_price_inr":1882.10,"debut_mae_pct":-6.0,"valuation_debut_inr_trn":1.53,"valuation_debut_usd_bn":18.2,"market_share_india_pct":15,"ipo_oversubscription":"more_than_2x","q2_profit_decline_pct":-16.5,"q2_profit_inr_bn":13.38,"domestic_sales_decline_pct":-6,"exports_decline_pct":-17,"q2_revenue_inr_bn":169.61,"q2_revenue_decline_pct":-7.5,"volume_decline_pct":-9,"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"failed_rerating","rerating_result":"OVERSEAS_AUTO_IPO_QUALITY_GATE","notes":"India growth and IPO size failed debut/first-earnings price validation."}
{"case_id":"r9_loop14_china_tourism_leisure_basket","symbol":"034230/008770/069960/123690","company_name":"Paradise / Hotel Shilla / Hyundai Department Store / Hankook Cosmetics","case_type":"event_premium_4b_watch","primary_archetype":"CHINA_TOURISM_LEISURE_EVENT_PREMIUM","stage2_date":"2025-08-06","stage4b_date":"2025-08-06","price_validation":{"price_data_source":"Reuters China group-tourist visa-free and leisure-stock reaction anchors","stage3_price":null,"visa_free_start":"2025-09-29","visa_free_end":"2026-06","visitors_2024_mn":16.4,"visitors_2024_yoy_growth_pct":48,"chinese_visitor_share_2024_pct":28,"visitor_target_2025_mn":18.5,"hyundai_department_store_event_mfe_pct":7.1,"hotel_shilla_event_mfe_pct":4.8,"paradise_event_mfe_pct":2.9,"hankook_cosmetics_event_mfe_pct":9.9,"casino_drop_amount_confirmed":false,"hotel_adr_occupancy_confirmed":false,"tourist_spend_per_head_confirmed":false,"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_4B_watch","rerating_result":"CHINA_TOURISM_LEISURE_EVENT_STAGE2","notes":"Visitor count is not Green until spend-per-head, casino drop, hotel ADR and margin confirm."}
{"case_id":"r9_loop14_hmm_red_sea_freight_rate_event_premium","symbol":"011200","company_name":"HMM / container-shipping read-through","case_type":"event_premium_4b_watch","primary_archetype":"CONTAINER_SHIPPING_RATE_EVENT_PREMIUM","stage2_date":"2024-07-03","stage4c_date":"2025-10-09_watch","price_validation":{"price_data_source":"Reuters Hapag-Lloyd / Maersk Red Sea freight-rate cycle anchors","stage3_price":null,"global_vessel_capacity_tied_pct":"5-9","freightos_spot_index_6w_growth_pct":40,"freightos_spot_index_usd":5068,"global_container_demand_growth_2024_pct":"3-4","maersk_ceasefire_event_mae_pct":-2,"rate_normalization_risk":true,"hmm_direct_event_price":"price_data_unavailable_after_deep_search","stage3_conditions":["contract_rate_mix","fuel_cost","vessel_utilization","route_security","cash_yield"]},"score_price_alignment":"event_premium_4B_watch","rerating_result":"CONTAINER_SHIPPING_RATE_EVENT_STAGE2","notes":"Spot-rate spike is cyclical until contract mix, vessel utilization and route security confirm durability."}
{"case_id":"r9_loop14_korea_used_car_export_logistics_shock","symbol":"used_car_exporters/HMM/Hyundai_Glovis_readthrough","company_name":"Korea used-car export logistics reference","case_type":"4c_reference","primary_archetype":"USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE","stage4c_date":"2026-03-24_watch","price_validation":{"price_data_source":"Reuters used-car export logistics shock anchor","stage3_price":null,"japan_korea_used_car_exports_usd_bn":19,"korea_used_car_exports_units":883000,"korea_used_car_exports_middle_east_share_pct":"more_than_one_third","incheon_storage_middle_east_bound_share_pct":80,"stuck_storage_share_context_pct":70,"exporter_revenue_tied_to_uae_krw_bn":6.6,"hmm_containers_stuck_near":"Mumbai","listed_direct_price":"price_data_unavailable_after_deep_search","use_as_transport_logistics_4c_reference":true},"score_price_alignment":"thesis_break_reference","rerating_result":"USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE","notes":"Destination demand and route availability must both clear for mobility/export logistics."}
```

## data/sector_taxonomy/score_weight_profiles_round219_r9_loop14_v1.csv 초안

```csv
archetype,tariff_pass_through,hybrid_mix_margin,local_production_hedge,route_security_continuity,logistics_cost_control,load_factor_yield,aviation_safety_trust,integration_synergy_execution,tourist_spend_per_head,freight_rate_durability,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
AUTO_TARIFF_HYBRID_MIX_STAGE2,+5,+5,+5,+2,+3,+0,+1,+1,+0,+0,-5,+4,+4,Hyundai/Kia tariff case needs pass-through and hybrid/high-margin mix proof.
AUTO_LOGISTICS_MIDDLE_EAST_4C_WATCH,+3,+3,+3,+5,+5,+0,+1,+1,+0,+2,0,+4,+5,Hyundai/Glovis shows route disruption and logistics cost are mobility hard gates.
AIRLINE_CONSOLIDATION_STAGE2,+1,+0,+0,+3,+4,+5,+5,+5,+1,+1,-5,+4,+4,Korean Air/Asiana needs yield, load factor, LCC consolidation and integration cost proof.
AIRLINE_REMEDY_ROUTE_CARGO_STAGE2,+1,+0,+0,+3,+4,+5,+5,+4,+1,+2,-5,+5,+4,T’way/Air Incheon route/cargo remedy needs aircraft utilization and customer retention.
AVIATION_SAFETY_HARD_4C,+0,+0,+0,+2,+2,+4,+5,+3,+2,+0,0,+4,+5,Jeju Air confirms fatal safety event overrides demand/valuation.
OVERSEAS_AUTO_IPO_FAILED_RERATING,+4,+4,+5,+3,+3,+0,+1,+2,+0,+0,-5,+5,+4,Hyundai India IPO needs aftermarket demand and first-earnings validation.
CHINA_TOURISM_LEISURE_EVENT_PREMIUM,+0,+0,+0,+1,+1,+2,+3,+1,+5,+0,-5,+5,+3,Tourism policy rally needs spend-per-head, occupancy, drop amount and margin.
CONTAINER_SHIPPING_RATE_EVENT_PREMIUM,+0,+0,+0,+5,+5,+0,+1,+1,+0,+5,-5,+5,+4,Red Sea freight spike is Stage 2 until contract-rate durability and route security hold.
USED_CAR_EXPORT_LOGISTICS_4C_REFERENCE,+1,+0,+0,+5,+5,+0,+1,+1,+0,+4,0,+4,+4,Used-car export shock shows destination demand and route availability are linked.
```

---

# 이번 R9 Loop 14 결론

```text
1. Hyundai/Kia는 tariff relief + hybrid mix Stage 2다.
   tariff가 25%에서 15%로 낮아져도 margin 회복은 pass-through와 mix가 닫혀야 한다.

2. Hyundai/Glovis는 route disruption 4C-watch다.
   Middle East 경로 차질은 자동차 수출, 납기, 물류비, high-margin market에 직접 들어간다.

3. Korean Air/Asiana는 airline consolidation Stage 2다.
   통합 완료와 record revenue는 좋지만 yield, LCC 통합, integration cost가 Stage 3 조건이다.

4. T’way/Air Incheon은 remedy beneficiary다.
   노선과 cargo asset은 받았지만 load factor, aircraft utilization, customer retention이 Green 조건이다.

5. Jeju Air는 R9 hard 4C다.
   fatal safety event는 관광수요와 valuation logic을 즉시 덮는다.

6. Hyundai Motor India는 overseas IPO failed rerating이다.
   $3.3B IPO와 India growth가 있어도 debut -6%, 첫 실적 부진이면 Green이 아니다.

7. China tourism/leisure basket은 event premium이다.
   visitor count보다 spend-per-head, casino drop, hotel ADR/occupancy, margin이 중요하다.

8. HMM/Red Sea freight cycle은 4B-watch다.
   spot 운임 spike는 좋지만 route normalization이 오면 바로 반대로 작동한다.

9. Used-car export logistics shock은 R9 reference다.
   최종수요와 항로가 같이 막히면 자동차·물류·해운 value chain이 한꺼번에 흔들린다.
```

한 문장으로 압축하면:

> **R9에서 진짜 Stage 3는 “자동차·항공·해운·관광 headline이 좋다”가 아니라, tariff pass-through·hybrid mix margin·route security·load factor/yield·safety trust·tourist spend-per-head·freight-rate durability가 실제 숫자로 닫히는 순간이다.**

[1]: https://www.reuters.com/business/autos-transportation/south-korea-automaker-shares-slip-after-us-trade-deal-2025-07-31/ "https://www.reuters.com/business/autos-transportation/south-korea-automaker-shares-slip-after-us-trade-deal-2025-07-31/"
[2]: https://www.reuters.com/business/autos-transportation/hyundai-motor-flags-export-disruptions-middle-east-conflict-hits-shipping-2026-04-03/ "https://www.reuters.com/business/autos-transportation/hyundai-motor-flags-export-disruptions-middle-east-conflict-hits-shipping-2026-04-03/"
[3]: https://www.reuters.com/markets/deals/korean-air-completes-asiana-takeover-form-one-asias-biggest-airlines-2024-12-12/ "https://www.reuters.com/markets/deals/korean-air-completes-asiana-takeover-form-one-asias-biggest-airlines-2024-12-12/"
[4]: https://www.reuters.com/business/aerospace-defense/skoreas-tway-air-sees-golden-opportunity-new-eu-routes-2024-03-07/ "https://www.reuters.com/business/aerospace-defense/skoreas-tway-air-sees-golden-opportunity-new-eu-routes-2024-03-07/"
[5]: https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/ "https://www.reuters.com/business/aerospace-defense/jeju-air-shares-plunge-record-low-after-deadly-plane-crash-2024-12-30/"
[6]: https://www.reuters.com/business/autos-transportation/hyundai-indias-shares-fall-13-debut-trade-after-record-33-bln-ipo-2024-10-22/ "https://www.reuters.com/business/autos-transportation/hyundai-indias-shares-fall-13-debut-trade-after-record-33-bln-ipo-2024-10-22/"
[7]: https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/ "https://www.reuters.com/world/china/south-korea-offer-visa-free-entry-chinese-tourists-late-september-2025-08-06/"
[8]: https://www.reuters.com/markets/hapag-lloyd-ceo-sees-solid-shipping-demand-driving-up-freight-rates-2024-07-03/ "https://www.reuters.com/markets/hapag-lloyd-ceo-sees-solid-shipping-demand-driving-up-freight-rates-2024-07-03/"
[9]: https://www.reuters.com/world/middle-east/lamborghinis-stranded-sri-lanka-war-disrupts-asias-used-car-trade-2026-03-24/ "https://www.reuters.com/world/middle-east/lamborghinis-stranded-sri-lanka-war-disrupts-asias-used-car-trade-2026-03-24/"

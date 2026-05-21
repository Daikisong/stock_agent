순서상 이번은 **R1 Loop 13 — 산업재·수주·인프라 가격경로 검증 라운드**다.

```text
round = R1 Loop 13
round_id = round_198
large_sector = INDUSTRIAL_ORDERS_INFRA
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
next_round = R2 Loop 13
```

이번 R1 Loop 13은 이전 R1에서 많이 본 Hanwha Aerospace / Hyundai Rotem K2 / LIG Nex1 / LS Electric / Hyosung Heavy 중심을 줄이고, **조선·해양 MRO, 미국 조선협력 MASGA, 철도 수출, 로봇/산업자동화, 항공우주 방산, 선박 after-market, 수주취소 4C**를 중심으로 본다.

중요한 제한도 같이 남긴다. 이번 pass에서 KRX/Naver/Yahoo/Stooq의 **수정주가 일봉 OHLC 전체 구간**은 안정적으로 확보하지 못했다. 그래서 원시 30D/90D/180D MFE·MAE를 임의로 만들지 않고, Reuters / FT / WSJ / MarketWatch가 보도한 **event price, event return, 계약금액, YTD return, 취소금액, IPO price anchor**만 계산했다. 원시 OHLC가 필요한 칸은 `price_data_unavailable_after_deep_search`로 둔다.

---

# 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
```

R1에서 제일 위험한 착시는 여전히 같다.

```text
수주 headline ≠ Stage 3
MOU ≠ Stage 3
IPO pop ≠ Stage 3
정책 협력 ≠ Stage 3
미국 조선협력 기대 ≠ Stage 3
```

진짜 Stage 3는 **계약 확정 → 납품/공정 → 매출 인식 → 마진 → 운전자본 → 현금회수 → 반복 수주/서비스 매출**까지 닫힐 때다.

---

# 2. 대상 canonical archetype

```text
US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION
SHIPBUILDING_GEOPOLITICAL_SANCTION_4C
SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C
RAIL_EXPORT_MEGA_ORDER_STAGE2
MARINE_AFTERMARKET_RECURRING_SERVICE
INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION
DEFENSE_AEROSPACE_EXPORT_OPTIONALITY
SHIPBUILDING_CONTRACT_CYCLE_4B
```

---

# 3. deep sub-archetype

```text
조선·해양:
- HD Hyundai Heavy / HD Hyundai Mipo merger
- MASGA, U.S. naval / auxiliary shipbuilding
- Hanwha Ocean Philly Shipyard / U.S. Navy MRO
- China sanctions on U.S.-linked Hanwha Ocean subsidiaries
- Samsung Heavy Zvezda cancellation

철도:
- Hyundai Rotem Morocco ONCF double-decker trains
- 2030 World Cup rail investment
- export order vs margin / delivery / FX / financing

선박 after-market:
- HD Hyundai Marine Solution
- ship repair, retrofit, engine after-sales service
- IPO event premium vs recurring service margin

산업자동화:
- Rainbow Robotics / Samsung largest-shareholder transaction
- humanoid / collaborative robot optionality
- strategic equity vs actual order / revenue

항공우주·방산:
- Korea Aerospace Industries
- FA-50 / KF-21 / Europe rearmament optionality
- defense stock rally vs contract/delivery evidence

조선 broad cycle:
- Samsung Heavy / Hanwha Ocean / HD Hyundai Heavy rally on contract wins
- newbuilding price cycle
- 4B if price outruns margin / cash conversion
```

---

# 4. 국장 신규 후보 case

## Case A — HD Hyundai Heavy + HD Hyundai Mipo `success_candidate + 4B-watch`

```text
symbols = 329180 / 010620
case_type = success_candidate + 4B-watch
archetype = US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION
```

### stage date

```text
Stage 1:
2025-08
- Korea-U.S. shipbuilding cooperation
- MASGA / Make American Shipbuilding Great Again
- U.S. naval / icebreaker / auxiliary-ship demand
- Korean shipbuilding capability as strategic infrastructure

Stage 2:
2025-08-27
- HD Hyundai Heavy plans merger with HD Hyundai Mipo
- exchange ratio: 1 HD Hyundai Mipo share for 1.04059146 HD Hyundai Heavy shares
- merged company expected in December 2025
- aim: U.S. shipbuilding market, naval vessels, Arctic icebreakers
- HD Hyundai Heavy +11.3%
- HD Hyundai Mipo +14.6%
- both close at record highs

Stage 3:
없음
- merger announcement은 Stage 2
- U.S. awarded contracts, shipyard acquisition/expansion, margin, FCF 확인 필요

Stage 4B:
2025-08-27
- record-high rally before actual U.S. revenue bridge
```

HD Hyundai Heavy / Mipo는 이번 R1의 강한 success_candidate다. 조선업 수주 사이클뿐 아니라 U.S. naval / icebreaker / shipyard 협력까지 붙은 구조다. 다만 주가가 발표 전후 이미 HD Hyundai Heavy +11.3%, HD Hyundai Mipo +14.6%로 record high까지 갔기 때문에, Stage 3가 아니라 **Stage 2 + 4B-watch**로 둔다. 최종 Green은 U.S. 조선협력의 실제 계약, 설비투자 ROI, 통합 후 margin, 현금회수로 확인해야 한다. ([Reuters][1])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters reported merger/event-return anchors",
  "entry_date": "N/A",
  "stage3_price": null,
  "stage2_date": "2025-08-27",
  "hd_hyundai_heavy_event_mfe_pct": 11.3,
  "hd_hyundai_mipo_event_mfe_pct": 14.6,
  "exchange_ratio": "1 HD Hyundai Mipo share : 1.04059146 HD Hyundai Heavy shares",
  "us_shipbuilding_sector_support_commitment_usd_bn": 150,
  "us_total_investment_package_usd_bn": 350,
  "merger_completion_target": "2025-12",
  "mfe_30d_90d_180d_1y_2y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4B_watch
rerating_result = US_naval_shipbuilding_consolidation_stage2
stage_failure_type = merger_headline_not_contract_margin_green
```

---

## Case B — Hanwha Ocean `success_candidate + sanction 4C-watch`

```text
symbol = 042660
case_type = success_candidate + 4C-watch
archetype = SHIPBUILDING_GEOPOLITICAL_SANCTION_4C
```

### stage date

```text
Stage 1:
2024~2025
- Hanwha Ocean acquires Philly Shipyard
- U.S. Navy MRO / U.S. shipbuilding revival
- MASGA / U.S.-Korea shipbuilding alliance

Stage 2:
2025-04-28 context
- KDB stake-sale report
- Hanwha Ocean shares +139% YTD
- optimism around U.S.-Korea shipbuilding cooperation
- Hanwha acquired Philly Shipyard in 2024

Stage 2 추가:
2025-12-23
- Trump comments on Hanwha building U.S. frigates
- Hanwha Ocean +6% in morning trading

Stage 4C-watch:
2025-10-14
- China sanctions five U.S.-linked Hanwha Ocean subsidiaries
- Chinese organizations and individuals prohibited from dealings with sanctioned units
- Hanwha Ocean closes -5.8%
- intraday decline as much as over -8%
- HD Hyundai Heavy -4.1%
```

Hanwha Ocean은 R1에서 “조선업 구조적 기회”와 “미중 maritime retaliation”이 같이 뜬 case다. U.S. Navy MRO와 Philly Shipyard는 좋은 Stage 2지만, 중국이 Hanwha Ocean의 U.S.-linked subsidiaries를 제재하자 주가는 바로 -5.8%, 장중 over -8%까지 밀렸다. 따라서 Hanwha Ocean은 Green이 아니라 **success_candidate + geopolitical 4C-watch**다. ([Reuters][2])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters/AP/MarketWatch reported anchors",
  "stage3_price": null,
  "reported_ytd_return_2025_pct": 139,
  "trump_frigate_comment_event_mfe_pct": 6,
  "china_sanction_event_close_mae_pct": -5.8,
  "china_sanction_event_intraday_mae_pct": -8.0,
  "hd_hyundai_heavy_same_context_mae_pct": -4.1,
  "philly_shipyard_acquisition_usd_mn": 100,
  "planned_philly_investment_usd_bn": 5,
  "sanctioned_us_linked_subsidiaries": 5,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_with_geopolitical_4C_watch
rerating_result = US_shipbuilding_MRO_option_with_China_sanction_risk
stage_failure_type = strategic_option_not_green_until_contracts_and_geopolitical_clearance
```

---

## Case C — Samsung Heavy Industries `hard 4C / contract cancellation`

```text
symbol = 010140
case_type = 4C-thesis-break
archetype = SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C
```

### stage date

```text
Stage 1:
2020~2021
- Zvezda icebreaker LNG carrier / shuttle tanker block orders
- Russia-linked Arctic LNG / icebreaker project exposure

Stage 4C:
2025-06-18
- Samsung Heavy says Zvezda orders cancelled
- total value 4.85T won / $3.54B
- 10 icebreaker LNG carriers
- 7 icebreaker shuttle tankers
- Samsung Heavy to pursue damages / arbitration context
- Russia-Ukraine uncertainty and unilateral termination by shipowner

Stage 3:
없음
- contract headline failed actual execution
```

Samsung Heavy is the cleanest R1 hard 4C in this round. 계약은 컸지만, 러시아 Zvezda 관련 주문 4.85조 원이 취소됐다. 선박 수주에서는 “계약 체결”보다 **제재·고객·선수금·arbitration·인도 가능성**이 더 중요하다. 이 case는 R1 Green gate에 `counterparty_sanction_and_delivery_risk`를 반드시 넣어야 한다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters cancellation anchor",
  "stage3_price": null,
  "cancelled_orders_krw_trn": 4.85,
  "cancelled_orders_usd_bn": 3.54,
  "cancelled_lng_icebreaker_carriers": 10,
  "cancelled_icebreaker_shuttle_tankers": 7,
  "contract_origin_years": "2020-2021",
  "stated_issue": "shipowner unilateral termination / prolonged Russia-Ukraine uncertainty",
  "legal_response": "arbitration / damages pursuit",
  "mfe": "N/A",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = shipbuilding_contract_quality_failure
stage_failure_type = hard_4C
```

---

## Case D — Hyundai Rotem / Morocco ONCF `success_candidate`

```text
symbol = 064350
case_type = success_candidate
archetype = RAIL_EXPORT_MEGA_ORDER_STAGE2
```

### stage date

```text
Stage 1:
2024~2025
- K-rail export expansion
- Morocco 2030 World Cup rail buildout
- urban / intercity / high-speed network expansion

Stage 2:
2025-02-26
- Hyundai Rotem wins ONCF double-decker train order
- order value about 2.2T won / $1.54B
- largest railway-business order for Hyundai Rotem to date
- Morocco buys 168 trains from Alstom / CAF / Hyundai Rotem
- Hyundai Rotem supplies 110 urban trains
- total Morocco train package $2.9B

Stage 3:
없음
- order value는 강하지만 delivery, localization, financing, margin, FX, cash collection 확인 필요

Stage 4B:
order headline로 price가 먼저 오르면 watch
```

Hyundai Rotem은 R1 철도수출의 좋은 Stage 2다. Morocco ONCF 주문은 Hyundai Rotem 철도 부문 사상 최대 주문으로 약 2.2조 원이고, Morocco 전체 168대 train package 중 Hyundai Rotem은 110대 urban trains를 공급한다. 다만 Stage 3는 납품·현지화·금융조건·마진·현금회수 확인 후다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters order anchors",
  "stage3_price": null,
  "order_value_krw_trn": 2.2,
  "order_value_usd_bn": 1.54,
  "hyundai_rotem_supply_units": 110,
  "morocco_total_train_purchase_units": 168,
  "morocco_total_train_package_usd_bn": 2.9,
  "hyundai_rotem_unit_share_pct": 65.5,
  "hyundai_rotem_order_share_of_total_value_pct": 53.1,
  "project_driver": "Morocco rail expansion ahead of 2030 FIFA World Cup",
  "mfe_30d_90d_180d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate
rerating_result = rail_export_mega_order_stage2
stage_failure_type = order_not_delivery_margin_green
```

---

## Case E — HD Hyundai Marine Solution `event_premium + recurring-service success_candidate`

```text
symbol = 443060
case_type = success_candidate + overheat
archetype = MARINE_AFTERMARKET_RECURRING_SERVICE
```

### stage date

```text
Stage 1:
2024-04~05
- HD Hyundai ship-repair / retrofit / after-sales service IPO
- eco-friendly vessel servicing demand
- marine after-market recurring revenue model

Stage 2:
2024-05-08
- IPO price 83,400 won
- open around 119,900 won
- Reuters Breakingviews: opened almost +44%
- WSJ: close 163,900 won, +97%
- market cap about 7.29T won
- IPO raised about 742.26B won / $546M
- 2023 revenue 1.430T won
- 2023 OP 201.47B won, +42%
- 2023 net profit 151.12B won, +44%

Stage 3:
없음
- IPO pop은 Green 아님
- aftermarket revenue repeatability, margin durability, KKR overhang, acquisition ROI 확인 필요

Stage 4B:
2024-05-08
- IPO close +97%
```

HD Hyundai Marine Solution은 사업모델 자체는 R1에서 좋은 구조다. 선박이 친환경·복잡화될수록 after-sales, retrofit, engine service 수요가 반복될 수 있다. 하지만 IPO 첫날 +97%는 이미 4B다. recurring service 매출과 margin은 좋지만, 상장 직후 가격은 evidence보다 먼저 달렸다. ([월스트리트저널][5])

### 실제 가격경로 검증

```json
{
  "price_data_source": "WSJ / Reuters Breakingviews IPO anchors",
  "ipo_price_krw": 83400,
  "open_price_krw": 119900,
  "close_price_krw": 163900,
  "open_return_pct": 43.8,
  "close_return_pct": 96.5,
  "ipo_raise_krw_bn": 742.26,
  "ipo_raise_usd_mn": 546,
  "market_cap_close_krw_trn": 7.29,
  "revenue_2023_krw_trn": 1.43,
  "op_2023_krw_bn": 201.47,
  "net_profit_2023_krw_bn": 151.12,
  "op_growth_2023_pct": 42,
  "net_profit_growth_2023_pct": 44,
  "op_margin_2023_pct": 14.1,
  "market_cap_to_revenue_2023": 5.1,
  "market_cap_to_op_2023": 36.2,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_4B_overheat
rerating_result = marine_aftermarket_recurring_service_watch
stage_failure_type = IPO_pop_not_green
```

---

## Case F — Rainbow Robotics / Samsung `success_candidate, not Green`

```text
symbol = 277810
case_type = success_candidate + insufficient_price_data
archetype = INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION
```

### stage date

```text
Stage 1:
2024-12-30
- Samsung Electronics becomes largest shareholder of Rainbow Robotics
- humanoid / collaborative robotics strategic push
- Samsung Future Robotics Office creation

Stage 2:
2024-12-30
- Samsung newly takes 267B won / $181M stake
- Samsung previously held 14.71%
- Samsung establishes Future Robotics Office reporting to CEO

Stage 3:
없음
- strategic equity investment is Stage 2
- robot orders, factory deployment, revenue, margin, integration synergies 확인 필요

Stage 4B:
robotics theme로 주가가 먼저 움직이면 watch
```

Rainbow Robotics는 산업자동화 R1 후보지만, Samsung 지분투자는 **전략 option**이지 Stage 3가 아니다. 실제 Green은 로봇 판매, 공장 투입, unit economics, recurring service, Samsung 내부 deployment가 확인되어야 한다. ([Reuters][6])

### 실제 가격경로 검증

```json
{
  "price_data_source": "Reuters strategic-equity anchor",
  "stage3_price": null,
  "samsung_new_stake_value_krw_bn": 267,
  "samsung_new_stake_value_usd_mn": 181,
  "samsung_previous_stake_pct": 14.71,
  "future_robotics_office": true,
  "actual_robot_order_revenue_confirmed": false,
  "rainbow_ohlc": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_insufficient_price_data
rerating_result = industrial_robotics_strategic_option_watch
stage_failure_type = equity_option_not_order_revenue_green
```

---

## Case G — Korea Aerospace Industries `success_candidate + 4B-watch`

```text
symbol = 047810
case_type = success_candidate + 4B-watch
archetype = DEFENSE_AEROSPACE_EXPORT_OPTIONALITY
```

### stage date

```text
Stage 1:
2025-03
- Europe rearmament
- FA-50 / KF-21 / Asian defense exporters re-rating
- Trump NATO pressure / Germany defense spending catalyst

Stage 2:
2025-03-18
- FT reports KAI +55% YTD
- Hanwha Aerospace +134% YTD
- Hyundai Rotem +123% YTD
- South Korean defense companies could win up to 154T won / $106B orders
- KAI exposure: fighter jets / aircraft platform exports

Stage 3:
없음
- defense stock rally는 Stage 2 / 4B-watch
- actual contracts, aircraft delivery, margin, cash collection 확인 필요

Stage 4B:
2025 defense-stock record run
```

KAI는 이번 R1에서 “방산·항공우주 export optionality”로 둔다. FT는 KAI가 2025년 YTD +55%, Hyundai Rotem +123%, Hanwha Aerospace +134%였다고 보도했고, Mirae Asset 쪽 추정으로 한국 기업이 최대 154조 원 규모의 무기 주문을 따낼 수 있다는 기대도 있었다. 하지만 이건 강한 sentiment와 optionality이지, 아직 KAI Stage 3가 아니다. ([Financial Times][7])

### 실제 가격경로 검증

```json
{
  "price_data_source": "FT defense-stock return/order-optionality anchor",
  "stage3_price": null,
  "kai_ytd_return_2025_pct": 55,
  "hyundai_rotem_ytd_return_2025_pct": 123,
  "hanwha_aerospace_ytd_return_2025_pct": 134,
  "potential_korean_defense_orders_krw_trn": 154,
  "potential_korean_defense_orders_usd_bn": 106,
  "actual_kai_contract_delivery_margin_confirmed_in_source": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_4B_watch
rerating_result = defense_aerospace_export_optionality_watch
stage_failure_type = sector_rerating_not_company_stage3
```

---

## Case H — Samsung Heavy / Hanwha Ocean / HD Hyundai Heavy broad shipbuilding rally `cyclical_success + 4B-watch`

```text
symbols = 010140 / 042660 / 329180
case_type = cyclical_success + 4B-watch
archetype = SHIPBUILDING_CONTRACT_CYCLE_4B
```

### stage date

```text
Stage 1:
2024-03
- global shipbuilding order cycle resumes
- newbuilding prices rise
- Korea regains top global shipbuilding order share

Stage 2:
2024-03-14
- Samsung Heavy +16% to 9,210 won
- Hanwha Ocean +13% to 27,450 won
- HD Hyundai Heavy +11% to 122,900 won
- KOSPI +0.5%
- South Korea took 50% of February global shipbuilding orders
- China took 41%
- Clarksons Newbuilding Price Index 181.81, +0.2% weekly

Stage 3:
없음
- broad cycle는 좋지만, individual Green requires backlog mix, steel cost, labor, payment, margin, FCF

Stage 4B:
2024-03-14
- sector-wide +11~16% day move before company-level cash conversion
```

이 case는 R1 조선업의 cyclical_success 기준점이다. 수주 사이클이 좋아지면 sector가 동시에 뛴다. 하지만 그날 Samsung Heavy +16%, Hanwha Ocean +13%, HD Hyundai Heavy +11%는 이미 4B-watch다. 개별 Stage 3는 backlog quality, steel cost, labor, contract margin, cash conversion으로 분해해야 한다. ([월스트리트저널][8])

### 실제 가격경로 검증

```json
{
  "price_data_source": "WSJ Market Talk / Clarksons order-cycle anchor",
  "stage3_price": null,
  "samsung_heavy_event_price_krw": 9210,
  "samsung_heavy_event_mfe_pct": 16,
  "hanwha_ocean_event_price_krw": 27450,
  "hanwha_ocean_event_mfe_pct": 13,
  "hd_hyundai_heavy_event_price_krw": 122900,
  "hd_hyundai_heavy_event_mfe_pct": 11,
  "kospi_same_context_pct": 0.5,
  "samsung_relative_outperformance_pp": 15.5,
  "hanwha_relative_outperformance_pp": 12.5,
  "hyundai_relative_outperformance_pp": 10.5,
  "south_korea_global_orders_share_pct": 50,
  "china_global_orders_share_pct": 41,
  "clarksons_newbuilding_price_index": 181.81,
  "clarksons_weekly_change_pct": 0.2
}
```

### alignment

```text
score_price_alignment = cyclical_success_4B_watch
rerating_result = shipbuilding_contract_cycle_watch
stage_failure_type = sector_order_cycle_not_individual_green
```

---

# 5. 이번 R1 case별 stage date 요약

| case                       | Stage 1    | Stage 2               | Stage 3 | Stage 4B             | Stage 4C         |
| -------------------------- | ---------- | --------------------- | ------- | -------------------- | ---------------- |
| HD Hyundai Heavy/Mipo      | 2025-08    | 2025-08-27            | N/A     | 2025-08-27           | N/A              |
| Hanwha Ocean               | 2024~2025  | 2025 U.S. cooperation | N/A     | 2025 YTD +139% watch | 2025-10-14 watch |
| Samsung Heavy              | 2020~2021  | original contracts    | N/A     | N/A                  | 2025-06-18 hard  |
| Hyundai Rotem Morocco      | 2024~2025  | 2025-02-26            | N/A     | watch                | N/A              |
| HD Hyundai Marine Solution | 2024-04~05 | 2024-05-08            | N/A     | 2024-05-08           | N/A              |
| Rainbow Robotics           | 2024-12-30 | 2024-12-30            | N/A     | watch                | N/A              |
| KAI                        | 2025-03    | 2025-03-18            | N/A     | 2025 defense rally   | N/A              |
| Shipbuilding cycle basket  | 2024-03    | 2024-03-14            | N/A     | 2024-03-14           | N/A              |

---

# 6. 실제 가격경로 검증 총괄

| case                  |                        anchor | MFE / MAE 해석                          | 판정                 |
| --------------------- | ----------------------------: | ------------------------------------- | ------------------ |
| HD Hyundai Heavy/Mipo |               +11.3% / +14.6% | merger + MASGA 기대가 먼저 가격화             | 4B-watch           |
| Hanwha Ocean          | +139% YTD, 이후 sanctions -5.8% | 구조기회와 지정학 리스크 동시                      | success + 4C-watch |
| Samsung Heavy         |           4.85T won cancelled | 계약품질 hard 4C                          | thesis_break       |
| Hyundai Rotem Morocco |                2.2T won order | 대형 수주 Stage 2                         | success_candidate  |
| HD Hyundai Marine     |              IPO +96.5% close | recurring service story보다 IPO pop이 먼저 | overheat           |
| Rainbow Robotics      |        Samsung 267B won stake | 전략지분, 매출 아님                           | success_candidate  |
| KAI                   |                      +55% YTD | sector rerating, company contract 아님  | 4B-watch           |
| Shipbuilding basket   |                       +11~16% | cyclical order rally                  | cyclical_success   |

---

# 7. score-price alignment 판정

```text
structural_success_candidate:
- HD Hyundai Heavy / Mipo
- HD Hyundai Marine Solution
- Hyundai Rotem Morocco
- Rainbow Robotics, but only as strategic option
- KAI, but only as export optionality

cyclical_success:
- Samsung Heavy / Hanwha Ocean / HD Hyundai Heavy broad shipbuilding rally

event_premium:
- HD Hyundai Marine IPO +96.5%
- HD Hyundai Heavy / Mipo merger rally
- defense-stock YTD rally

false_positive_score:
- none confirmed this round as pure false positive
- watch item: shipbuilding / robotics / KAI if actual order/revenue does not follow

price_moved_without_evidence:
- HD Hyundai Marine IPO pop if treated as Stage 3
- KAI defense rerating if treated as company-specific Green
- Rainbow Robotics if Samsung equity stake is treated as revenue

thesis_break:
- Samsung Heavy Zvezda cancellation

thesis_break_watch:
- Hanwha Ocean China sanctions
- shipbuilding U.S.-China port fee / retaliation risk

hard_4C:
- Samsung Heavy order cancellation
```

---

# 8. 점수비중 교정

## 올릴 축

```text
final_contract_quality +5
delivery_schedule_visibility +5
backlog_margin_quality +5
cash_collection_quality +5
counterparty_sanction_check +5
recurring_service_revenue +4
aftermarket_margin_visibility +4
naval_MRO_contract_award +5
integration_synergy_realization +4
actual_robot_order_revenue +5
```

### 왜 올리나

Samsung Heavy cancellation은 수주금액이 커도 counterparty/sanction/delivery risk가 있으면 hard 4C가 된다는 증거다. Hyundai Rotem Morocco는 대형 수주지만 납품·마진·현금회수가 필요하다. HD Hyundai Marine은 after-market 서비스 매출이 좋지만 IPO pop만으로는 Green이 아니다. Hanwha Ocean은 U.S. naval/MRO option이 좋지만 중국 제재가 즉시 가격을 눌렀다.

## 내릴 축

```text
order_headline_only -5
MOU_or_merger_headline_only -5
IPO_pop_only -5
defense_sector_rerating_only -4
strategic_equity_investment_only -4
US_shipbuilding_policy_theme_only -4
counterparty_sanction_risk -5
contract_cancellation_risk -5
geopolitical_port_fee_risk -4
```

### 왜 내리나

HD Hyundai Heavy/Mipo는 merger와 MASGA 기대가 먼저 가격화됐다. Rainbow Robotics는 Samsung 지분투자이지 아직 로봇 매출이 아니다. KAI는 방산주 랠리이지 KAI 개별 delivery/margin evidence가 아니다. Samsung Heavy는 수주취소 hard 4C다.

## Green gate 강화 조건

```text
R1 Stage 3-Green 필수:
1. final contract signed
2. delivery schedule / construction milestone 확인
3. backlog margin quality 확인
4. working capital / advance payment / receivables 확인
5. cash collection 확인
6. counterparty sanction / legal / export-control risk 통과
7. after-market은 recurring revenue와 margin 확인
8. M&A / merger는 integration synergy와 proceeds / FCF 확인
9. robotics / aerospace는 actual order and revenue 확인
10. price path가 evidence 이후 따라옴

금지:
order headline only
MOU only
merger headline only
IPO pop only
strategic stake only
defense-sector YTD rally only
contract cancellation present
sanction / legal / counterparty risk unresolved
```

## 4B 조기감지 조건

```text
4B-watch:
조선주가 수주 cycle 뉴스로 하루 +10~16% 이상 급등
IPO 첫날 +40~100% 상승
merger / MASGA headline로 record high
defense-stock YTD +50~130% 상승
strategic equity stake만으로 robotics stock rerating
shipbuilding policy/MASGA 기대가 actual U.S. order보다 먼저 가격화

4B-elevated:
실제 awarded contract 없음
margin / steel cost / labor cost 미확인
counterparty risk 있음
China/U.S. port fee or sanction risk 있음
KKR / PE overhang 있음
integration synergy 미확인
```

## 4C hard gate 조건

```text
contract cancellation
counterparty illegal termination
sanctioned customer / sanctioned subsidiary
arbitration / advance-payment dispute
export-control / port-fee retaliation
delivery impossible due war / sanctions
shipyard safety / labor stoppage
M&A integration failure
IPO proceeds misuse / aftermarket margin collapse
robotics order failure after strategic investment
```

이번 R1 Loop 13의 hard 4C는 **Samsung Heavy Zvezda cancellation**로 확정한다. Hanwha Ocean China sanctions는 hard 4C가 아니라 강한 4C-watch다.

---

# 9. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 10. 레포 반영용 patch-ready 출력

## docs/round/round_198.md 요약

```md
# R1 Loop 13. Industrial Orders / Infrastructure Price Validation

이번 라운드는 R1 Loop 13 price-validation 라운드다.

핵심 결론:
- HD Hyundai Heavy / HD Hyundai Mipo merger is strong Stage 2 plus 4B-watch. HD Hyundai Heavy +11.3%, HD Hyundai Mipo +14.6%, both record highs, on MASGA / U.S. shipbuilding cooperation. Green requires actual U.S. awards, margin, FCF and integration synergy.
- Hanwha Ocean is success_candidate plus China-sanction 4C-watch. Shares were up 139% YTD on U.S. shipbuilding/MRO optimism, but China sanctions on five U.S.-linked subsidiaries drove Hanwha Ocean -5.8% and as much as over -8% intraday.
- Samsung Heavy Industries is hard 4C. Zvezda orders worth 4.85T won / $3.54B for 10 icebreaker LNG carriers and 7 icebreaker shuttle tankers were cancelled.
- Hyundai Rotem Morocco is rail-export Stage 2. ONCF order value about 2.2T won / $1.54B, 110 urban trains, largest railway-business order to date. Delivery/margin/cash collection required.
- HD Hyundai Marine Solution is recurring marine-service success_candidate but IPO overheat. IPO price 83,400 won, close 163,900 won, +96.5%; 2023 OP 201.47B won, OP margin 14.1%.
- Rainbow Robotics is industrial-robotics strategic option. Samsung newly took a 267B won stake and became largest shareholder, but strategic equity is not robot order/revenue.
- KAI is defense-aerospace optionality Stage 2 plus 4B-watch. KAI +55% YTD in FT context, but company-specific contracts, delivery, margin and cash collection are required.
- Broad Korean shipbuilders rally is cyclical_success plus 4B-watch. Samsung Heavy +16%, Hanwha Ocean +13%, HD Hyundai Heavy +11% on 2024-03-14. Sector order cycle is not individual Green.
```

## docs/checkpoints/checkpoint_28a_round198_r1_loop13.md 요약

```md
# Checkpoint 28A Round 198 R1 Loop 13 Industrial Orders Infra Price Validation

## 반영 내용
- R1 Loop 13 price-validation 라운드를 추가했다.
- U.S. naval shipbuilding/MASGA, Hanwha Ocean sanction risk, Samsung Heavy cancellation, Hyundai Rotem Morocco rail order, HD Hyundai Marine after-market service, Rainbow Robotics strategic equity, KAI aerospace-defense optionality, broad shipbuilding contract cycle을 비교했다.
- Reuters / FT / WSJ / MarketWatch reported anchors로 가능한 event MFE/MAE와 price anchors를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- final contract quality, delivery schedule, backlog margin quality, cash collection, counterparty sanction check, recurring service revenue, naval MRO contract award, integration synergy, actual robot order revenue 가중치 강화
- order headline-only, MOU/merger headline-only, IPO pop-only, strategic equity investment-only, defense-sector rerating-only, U.S. shipbuilding policy theme-only, contract cancellation risk 감점 강화
```

## data/e2r_case_library/cases_r1_loop13_round198.jsonl 초안

```jsonl
{"case_id":"r1_loop13_hd_hyundai_heavy_mipo_masga_merger","symbol":"329180/010620","company_name":"HD Hyundai Heavy Industries / HD Hyundai Mipo","case_type":"success_candidate","primary_archetype":"US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION","stage2_date":"2025-08-27","stage4b_date":"2025-08-27","price_validation":{"price_data_source":"Reuters merger/event-return anchors","stage3_price":null,"hd_hyundai_heavy_event_mfe_pct":11.3,"hd_hyundai_mipo_event_mfe_pct":14.6,"exchange_ratio":"1 HD Hyundai Mipo share for 1.04059146 HD Hyundai Heavy shares","us_shipbuilding_support_commitment_usd_bn":150,"us_total_investment_package_usd_bn":350,"merger_completion_target":"2025-12","price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_4B_watch","rerating_result":"US_naval_shipbuilding_consolidation_stage2","notes":"Merger/MASGA headline is Stage 2; actual U.S. contracts, integration synergy, margin and FCF required before Green."}
{"case_id":"r1_loop13_hanwha_ocean_us_mro_china_sanction_watch","symbol":"042660","company_name":"Hanwha Ocean","case_type":"success_candidate_4c_watch","primary_archetype":"SHIPBUILDING_GEOPOLITICAL_SANCTION_4C","stage2_date":"2025_US_shipbuilding_MRO_context","stage4c_date":"2025-10-14_watch","price_validation":{"price_data_source":"Reuters/AP/MarketWatch reported anchors","stage3_price":null,"reported_ytd_return_2025_pct":139,"trump_frigate_comment_event_mfe_pct":6,"china_sanction_event_close_mae_pct":-5.8,"china_sanction_event_intraday_mae_pct":-8,"hd_hyundai_heavy_same_context_mae_pct":-4.1,"philly_shipyard_acquisition_usd_mn":100,"planned_philly_investment_usd_bn":5,"sanctioned_us_linked_subsidiaries":5,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_with_geopolitical_4C_watch","rerating_result":"US_shipbuilding_MRO_option_with_China_sanction_risk","notes":"U.S. MRO/shipbuilding option is real Stage 2, but China sanctions create 4C-watch."}
{"case_id":"r1_loop13_samsung_heavy_zvezda_cancellation_hard_4c","symbol":"010140","company_name":"Samsung Heavy Industries","case_type":"4c_thesis_break","primary_archetype":"SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C","stage4c_date":"2025-06-18","price_validation":{"price_data_source":"Reuters cancellation anchor","stage3_price":null,"cancelled_orders_krw_trn":4.85,"cancelled_orders_usd_bn":3.54,"cancelled_lng_icebreaker_carriers":10,"cancelled_icebreaker_shuttle_tankers":7,"contract_origin_years":"2020-2021","stated_issue":"shipowner unilateral termination / Russia-Ukraine uncertainty","legal_response":"arbitration / damages pursuit","price_validation_status":"reported_contract_anchor_not_full_ohlc"},"score_price_alignment":"thesis_break","rerating_result":"shipbuilding_contract_quality_failure","notes":"Large order failed execution; contract cancellation is R1 hard 4C."}
{"case_id":"r1_loop13_hyundai_rotem_morocco_oncf_rail_order","symbol":"064350","company_name":"Hyundai Rotem","case_type":"success_candidate","primary_archetype":"RAIL_EXPORT_MEGA_ORDER_STAGE2","stage2_date":"2025-02-26","price_validation":{"price_data_source":"Reuters order anchors","stage3_price":null,"order_value_krw_trn":2.2,"order_value_usd_bn":1.54,"hyundai_rotem_supply_units":110,"morocco_total_train_purchase_units":168,"morocco_total_package_usd_bn":2.9,"hyundai_rotem_unit_share_pct":65.5,"hyundai_rotem_order_share_of_total_value_pct":53.1,"project_driver":"Morocco rail expansion ahead of 2030 FIFA World Cup","price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate","rerating_result":"rail_export_mega_order_stage2","notes":"Order is strong Stage 2; delivery, localization, financing, margin, FX and cash collection required before Green."}
{"case_id":"r1_loop13_hd_hyundai_marine_solution_ipo_aftermarket","symbol":"443060","company_name":"HD Hyundai Marine Solution","case_type":"success_candidate_overheat","primary_archetype":"MARINE_AFTERMARKET_RECURRING_SERVICE","stage2_date":"2024-05-08","stage4b_date":"2024-05-08","price_validation":{"price_data_source":"WSJ/Reuters Breakingviews IPO anchors","ipo_price_krw":83400,"open_price_krw":119900,"close_price_krw":163900,"open_return_pct":43.8,"close_return_pct":96.5,"ipo_raise_krw_bn":742.26,"ipo_raise_usd_mn":546,"market_cap_close_krw_trn":7.29,"revenue_2023_krw_trn":1.43,"op_2023_krw_bn":201.47,"net_profit_2023_krw_bn":151.12,"op_growth_2023_pct":42,"net_profit_growth_2023_pct":44,"op_margin_2023_pct":14.1,"market_cap_to_revenue_2023":5.1,"market_cap_to_op_2023":36.2,"price_validation_status":"reported_ipo_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_but_4B_overheat","rerating_result":"marine_aftermarket_recurring_service_watch","notes":"After-market service model is attractive, but IPO +96.5% close is 4B unless recurring revenue/margin durability confirm."}
{"case_id":"r1_loop13_rainbow_robotics_samsung_strategic_equity","symbol":"277810","company_name":"Rainbow Robotics","case_type":"success_candidate","primary_archetype":"INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION","stage2_date":"2024-12-30","price_validation":{"price_data_source":"Reuters strategic-equity anchor","stage3_price":null,"samsung_new_stake_value_krw_bn":267,"samsung_new_stake_value_usd_mn":181,"samsung_previous_stake_pct":14.71,"future_robotics_office":true,"actual_robot_order_revenue_confirmed":false,"price_validation_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_insufficient_price_data","rerating_result":"industrial_robotics_strategic_option_watch","notes":"Samsung strategic stake is Stage 2; actual robot orders, revenue, margin and deployment required before Green."}
{"case_id":"r1_loop13_kai_defense_aerospace_export_optionality","symbol":"047810","company_name":"Korea Aerospace Industries","case_type":"success_candidate_4b_watch","primary_archetype":"DEFENSE_AEROSPACE_EXPORT_OPTIONALITY","stage2_date":"2025-03-18","stage4b_date":"2025_YTD_defense_rally","price_validation":{"price_data_source":"FT defense-stock return/order-optionality anchor","stage3_price":null,"kai_ytd_return_2025_pct":55,"hyundai_rotem_ytd_return_2025_pct":123,"hanwha_aerospace_ytd_return_2025_pct":134,"potential_korean_defense_orders_krw_trn":154,"potential_korean_defense_orders_usd_bn":106,"actual_kai_contract_delivery_margin_confirmed_in_source":false,"price_validation_status":"reported_return_anchor_not_full_ohlc"},"score_price_alignment":"success_candidate_4B_watch","rerating_result":"defense_aerospace_export_optionality_watch","notes":"Sector rally and order optionality are Stage 2; KAI-specific contracts, deliveries, margin and cash collection required."}
{"case_id":"r1_loop13_korean_shipbuilders_contract_cycle_4b","symbol":"010140/042660/329180","company_name":"Samsung Heavy / Hanwha Ocean / HD Hyundai Heavy broad shipbuilding basket","case_type":"cyclical_success","primary_archetype":"SHIPBUILDING_CONTRACT_CYCLE_4B","stage2_date":"2024-03-14","stage4b_date":"2024-03-14","price_validation":{"price_data_source":"WSJ Market Talk / Clarksons order-cycle anchor","stage3_price":null,"samsung_heavy_event_price_krw":9210,"samsung_heavy_event_mfe_pct":16,"hanwha_ocean_event_price_krw":27450,"hanwha_ocean_event_mfe_pct":13,"hd_hyundai_heavy_event_price_krw":122900,"hd_hyundai_heavy_event_mfe_pct":11,"kospi_same_context_pct":0.5,"samsung_relative_outperformance_pp":15.5,"hanwha_relative_outperformance_pp":12.5,"hyundai_relative_outperformance_pp":10.5,"south_korea_global_orders_share_pct":50,"china_global_orders_share_pct":41,"clarksons_newbuilding_price_index":181.81,"clarksons_weekly_change_pct":0.2,"price_validation_status":"reported_event_anchor_not_full_ohlc"},"score_price_alignment":"cyclical_success_4B_watch","rerating_result":"shipbuilding_contract_cycle_watch","notes":"Sector order cycle is positive, but +11~16% day move is 4B unless individual margin/cash conversion confirms."}
```

## data/sector_taxonomy/score_weight_profiles_round198_r1_loop13_v1.csv 초안

```csv
archetype,final_contract_quality,delivery_schedule,backlog_margin_quality,cash_collection,counterparty_sanction_check,recurring_service_revenue,aftermarket_margin,naval_mro_award,integration_synergy,actual_robot_order_revenue,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
US_NAVAL_SHIPBUILDING_MASGA_CONSOLIDATION,+4,+4,+5,+5,+5,+2,+2,+5,+5,+0,-5,+5,+5,HD Hyundai Heavy/Mipo merger is Stage 2; actual U.S. awards and integration needed.
SHIPBUILDING_GEOPOLITICAL_SANCTION_4C,+4,+4,+5,+5,+5,+2,+2,+5,+3,+0,0,+4,+5,Hanwha Ocean U.S. option is good but China sanctions create 4C-watch.
SHIPBUILDING_CONTRACT_CANCELLATION_HARD_4C,+5,+5,+5,+5,+5,+0,+0,+0,+0,+0,0,+3,+5,Samsung Heavy Zvezda cancellation is hard 4C.
RAIL_EXPORT_MEGA_ORDER_STAGE2,+5,+5,+5,+5,+4,+1,+1,+0,+0,+0,-5,+4,+4,Hyundai Rotem Morocco order needs delivery, localization, margin, FX and cash collection.
MARINE_AFTERMARKET_RECURRING_SERVICE,+3,+3,+4,+5,+3,+5,+5,+2,+2,+0,-5,+5,+3,HD Hyundai Marine after-market model is attractive but IPO pop is 4B.
INDUSTRIAL_ROBOTICS_STRATEGIC_EQUITY_OPTION,+2,+2,+3,+4,+2,+3,+3,+0,+4,+5,-4,+5,+4,Rainbow/Samsung stake is Stage 2 until robot orders/revenue/margin confirm.
DEFENSE_AEROSPACE_EXPORT_OPTIONALITY,+5,+5,+5,+5,+4,+1,+1,+0,+0,+0,-4,+5,+4,KAI needs company-specific contracts/delivery/cash collection; sector rally is not Green.
SHIPBUILDING_CONTRACT_CYCLE_4B,+4,+4,+5,+5,+4,+2,+2,+0,+1,+0,-5,+5,+4,Broad shipbuilder rally is cyclical success but not individual Stage 3.
```

---

# 이번 R1 Loop 13 결론

```text
1. HD Hyundai Heavy / Mipo는 R1의 강한 success_candidate다.
   하지만 merger + MASGA headline으로 record high가 먼저 나왔으므로 Stage 3가 아니라 4B-watch다.

2. Hanwha Ocean은 U.S. naval/MRO option이 강하지만, China sanctions가 4C-watch다.
   +139% YTD 이후 sanctions -5.8%는 지정학 gate를 보여준다.

3. Samsung Heavy는 이번 라운드 hard 4C다.
   4.85T won Zvezda order cancellation은 contract quality gate를 즉시 강화해야 한다.

4. Hyundai Rotem Morocco는 rail-export Stage 2다.
   2.2T won order는 좋지만 delivery, localization, margin, cash collection 전 Green 금지다.

5. HD Hyundai Marine Solution은 recurring after-market story가 좋지만 IPO +96.5%는 4B다.
   service revenue durability와 margin이 확인되어야 한다.

6. Rainbow Robotics는 Samsung strategic equity option이다.
   지분투자만으로는 robot order/revenue Green이 아니다.

7. KAI는 defense aerospace optionality Stage 2다.
   +55% YTD sector rally는 contract/delivery/margin 전 4B-watch다.

8. broad shipbuilding rally는 cyclical_success다.
   Samsung Heavy +16%, Hanwha +13%, HD Hyundai +11%는 업황 반등이지만 개별 Stage 3는 아니다.
```

한 문장으로 압축하면:

> **R1에서 진짜 Stage 3는 “수주·MOU·합병·IPO·정책협력·방산 랠리가 있다”가 아니라, 그 이벤트가 납품·마진·운전자본·현금회수·제재/계약 리스크 통과로 실제 돈이 되는 순간이다.**

[1]: https://www.reuters.com/markets/emerging/south-koreas-top-shipbuilder-acquire-affiliate-tap-us-demand-under-trump-2025-08-27/?utm_source=chatgpt.com "South Korea's top shipbuilder to acquire affiliate to tap US demand under Trump"
[2]: https://www.reuters.com/markets/europe/korea-development-bank-sell-shares-hanwha-ocean-paper-reports-2025-04-28/?utm_source=chatgpt.com "Korea Development Bank to sell shares in Hanwha Ocean, paper reports"
[3]: https://www.reuters.com/business/retail-consumer/samsung-heavy-says-354-billion-icebreaker-orders-russias-zvezda-cancelled-2025-06-18/?utm_source=chatgpt.com "Samsung Heavy says $3.54 billion icebreaker orders from Russia's Zvezda cancelled"
[4]: https://www.reuters.com/markets/deals/hyundai-rotem-wins-15-billion-order-moroccos-national-rail-operator-2025-02-26/?utm_source=chatgpt.com "Hyundai Rotem wins $1.5 billion order from Morocco's national rail operator"
[5]: https://www.wsj.com/business/hd-hyundai-marine-solution-makes-strong-debut-in-south-korea-e5e63451?utm_source=chatgpt.com "KKR-Backed HD Hyundai Marine Makes Strong Debut in South Korea"
[6]: https://www.reuters.com/technology/samsung-electronics-becomes-largest-shareholder-south-koreas-rainbow-robotics-2024-12-30/?utm_source=chatgpt.com "Samsung Electronics becomes largest shareholder of South Korea's Rainbow Robotics"
[7]: https://www.ft.com/content/25226697-47ca-4701-a431-4b45cb85a635?utm_source=chatgpt.com "Asian defence stocks soar to record highs as Europe prepares to re-arm"
[8]: https://www.wsj.com/articles/south-korean-shipbuilders-rally-on-brisk-contract-wins-d44ecb8a?utm_source=chatgpt.com "South Korean Shipbuilders Rally on Brisk Contract Wins"

순서상 이번은 **R1 Loop 14 — 산업재·수주·인프라 가격경로 검증 라운드**다.

```text
round = R1 Loop 14
round_id = round_211
large_sector = INDUSTRIALS_ORDERS_INFRASTRUCTURE
price_validation_completed = partial_with_reported_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
hard_4c_confirmed = true
next_round = R2 Loop 14
```

이번 R1은 기존 대표 case인 HD현대일렉트릭 한 종목만 반복하지 않고, **현대로템 방산 수출, LS일렉트릭·효성중공업 전력망, HD현대중공업/미포 MASGA, 삼성중공업 러시아 계약취소, 한화에어로스페이스 증자 희석, 레인보우로보틱스/Samsung robotics, HD현대마린솔루션 IPO**를 같이 본다.

수정주가 일봉 OHLC 전체 구간은 이번 환경에서 안정적으로 확보하지 못했다. KRX/Naver/Yahoo/Stooq/finance-tool 쪽으로 확인을 시도했지만 국장 종목의 조정 OHLC window를 일괄 추출할 수 없었다. 그래서 30D/90D/180D/1Y full MFE·MAE는 임의 생성하지 않고, Reuters/WSJ/MarketWatch/FT가 보도한 **event price, event return, 계약금액, IPO price, cancellation value, 증자금액, target price**를 가격 anchor로 사용했다.

---

# 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
```

R1에서 진짜 Stage 3는 “수주했다”, “방산이다”, “전력망이다”, “미국 공장이다”, “로봇이다”, “IPO 대박이다”가 아니다.

진짜 Stage 3는 아래가 같이 닫히는 순간이다.

```text
수주 산업재:
수주 → 실제 납품 / revenue recognition → 원가율 → 운전자본 → 현금회수

전력망:
북미/중동 수요 → backlog → 증설 capacity → lead time → margin → working capital

조선:
수주 / 합병 / MRO 진입 → dock capacity → 인력 → 후판가 → 인도 스케줄 → 손실계약 없음

방산:
계약 → 정부 예산 / financing → 납품 → 현지생산 조건 → margin / cash collection

로봇:
지분투자 / 테마 → 실제 출하량 → ASP → 반복 수요 → gross margin

IPO:
공모가 / 첫날 급등 → 상장 후 수요 → 실적 지속성 → lock-up / PE exit pressure
```

---

# 2. 대상 canonical archetype

```text
DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE
GRID_EQUIPMENT_US_GROWTH_STAGE2
TRANSFORMER_CAPACITY_EXPANSION_STAGE2
SHIPBUILDING_MERGER_MASGA_4B
SHIPBUILDING_ORDER_CANCELLATION_HARD_4C
DEFENSE_DILUTION_FALSE_POSITIVE
ROBOTICS_STRATEGIC_STAKE_EVENT_PREMIUM
INDUSTRIAL_SERVICE_IPO_OVERHEAT
```

---

# 3. deep sub-archetype

```text
방산 수출:
- Hyundai Rotem / K2 Poland
- shipment/revenue already recognised vs second-batch expectation
- Europe rearmament bridge
- local production and financing gate

전력망:
- LS Electric / U.S. data center / renewable / EV infra
- U.S. revenue share from <5% to around 20%
- target-price jump but event price failed

변압기 capacity:
- Hyosung Heavy / Hyosung HICO Memphis
- U.S. transformer shortage / GSU lead time
- capacity expansion, but no direct listed price anchor

조선:
- HD Hyundai Heavy + HD Hyundai Mipo merger
- MASGA / U.S.-Korea shipbuilding cooperation
- record-high close but integration and exchange-ratio risk

계약취소:
- Samsung Heavy / Zvezda Russia icebreaker LNG contracts
- 4.85T won / $3.54B cancelled
- arbitration / sanctions / Russia execution risk

방산 희석:
- Hanwha Aerospace 3.6T won share issue
- shares -13%
- FSS revision order
- later revised funding plan

로봇:
- Samsung becomes largest shareholder in Rainbow Robotics
- 267B won stake
- Future Robotics Office
- strategic event, not shipment/margin Green

산업서비스 IPO:
- HD Hyundai Marine Solution
- IPO price 83,400 won
- close 163,900 won, +97%
- ship after-sales / retrofit service
- overheat / IPO-quality gate
```

---

# 4. 국장 신규 후보 case

## Case A — Hyundai Rotem / Poland K2 `aligned_partial Stage 3 candidate`

```text
symbol = 064350
case_type = structural_success_candidate
archetype = DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE
```

### stage date

```text
Stage 1:
2022-08
- Poland signs first K2 batch contract.
- 180 K2 tanks.
- Korean defence export enters European rearmament cycle.

Stage 3 candidate:
2024-04
- Hyundai Rotem had already shipped 18 K2 tanks to Poland.
- Those shipments contributed 270B won to Q1 revenue.
- KB Securities expected OP +85% YoY to 59.1B won.
- shares +9.3% to 41,300 won.
- KOSPI -0.3%.

Stage 2 extension:
2025-08-01
- Poland signs second contract for 180 K2 tanks.
- contract value context: $6.5B.
- 61 tanks to be produced in Poland.
- first deliveries planned for 2026, Polish production 2028~2030.

Stage 4B-watch:
2025
- FT context: Hyundai Rotem +123% YTD on expected Poland/Romania contracts.
- price can front-run multi-year delivery and local-production execution.
```

Hyundai Rotem은 이번 R1에서 가장 Stage 3에 가까운 case다. 단순 “방산 수주 기대”가 아니라 **이미 18대 K2가 폴란드로 출하됐고, Q1 매출 270B won으로 반영됐으며, OP 추정치와 주가가 같이 움직인** 케이스이기 때문이다. 2025년 두 번째 180대 계약은 강한 Stage 2 확장이다. 다만 현지생산 2028~2030, 폴란드 financing, 기술이전, margin은 계속 gate로 남긴다. ([월스트리트저널][1])

### 실제 가격경로 검증

```json
{
  "case_id": "r1_loop14_hyundai_rotem_k2_poland_delivery_stage3_candidate",
  "symbol": "064350",
  "stage3_date_candidate": "2024-04",
  "entry_date": "2024-04 reported event day",
  "stage3_price_krw": 41300,
  "price_data_source": "WSJ event price anchor; Reuters Poland second-contract anchor",
  "event_mfe_pct": 9.3,
  "kospi_same_context_pct": -0.3,
  "relative_outperformance_pp": 9.6,
  "q1_revenue_from_18_k2_shipments_krw_bn": 270,
  "q1_op_estimate_krw_bn": 59.1,
  "op_estimate_growth_pct": 85,
  "target_price_krw": 47500,
  "target_upside_from_stage3_price_pct": 15.0,
  "second_contract_value_usd_bn": 6.5,
  "second_contract_tanks": 180,
  "poland_local_production_units": 61,
  "first_delivery_second_batch": 2026,
  "polish_production_period": "2028-2030",
  "mfe_30d_90d_180d_1y_2y": "price_data_unavailable_after_deep_search",
  "mae_30d_90d_180d_1y": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = aligned_partial
rerating_result = defense_export_delivery_stage3_candidate
stage_failure_type = local_production_financing_margin_gate_remains
```

---

## Case B — LS Electric / U.S. grid growth `evidence good but price failed`

```text
symbol = 010120
case_type = evidence_good_but_price_failed
archetype = GRID_EQUIPMENT_US_GROWTH_STAGE2
```

### stage date

```text
Stage 1:
2024-07-01
- U.S. data-center construction, renewable-energy projects and EV value chain boost electrical-equipment demand.
- LS Electric U.S. revenue opportunity becomes visible.

Stage 2:
2024-07-01
- Daiwa expects U.S. operations to rise from below 5% of 2022 revenue to around 20% of 2024 revenue.
- Daiwa raises 2024~2026 revenue forecasts by 4%~22%.
- target price raised 87% to 280,000 won.
- buy rating maintained.

Stage 3:
없음
- shares were 5.4% lower at 208,500 won despite estimate/target upgrade.
- market did not confirm Green on event day.

Stage 4B-watch:
- grid / data-center theme can front-run actual backlog, capacity and margin.
```

LS Electric은 좋은 산업재 Stage 2지만, 가격경로가 즉시 Green을 인정하지 않았다. U.S. revenue share가 2022년 5% 미만에서 2024년 20% 수준까지 올라갈 수 있다는 전망, target price 87% 상향, 2024~2026 revenue forecast 상향은 모두 강한 evidence다. 그런데 당일 주가는 -5.4%로 208,500원이었다. 이런 case는 `evidence_good_but_price_failed`로 둬야 한다. ([마켓워치][2])

### 실제 가격경로 검증

```json
{
  "case_id": "r1_loop14_ls_electric_us_grid_growth_price_failed",
  "symbol": "010120",
  "stage2_date": "2024-07-01",
  "stage3_price": null,
  "event_price_krw": 208500,
  "event_mae_pct": -5.4,
  "price_data_source": "MarketWatch / Dow Jones event anchor",
  "us_revenue_share_2022_pct": "<5",
  "us_revenue_share_2024_expected_pct": 20,
  "revenue_forecast_raise_2024_2026_pct_range": "4-22",
  "target_price_krw": 280000,
  "target_price_raise_pct": 87,
  "target_upside_from_event_price_pct": 34.3,
  "green_conditions": ["actual_backlog", "capacity", "margin", "working_capital"],
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = evidence_good_but_price_failed
rerating_result = grid_equipment_US_growth_stage2
stage_failure_type = estimate_upgrade_not_price_green
```

---

## Case C — Hyosung Heavy / Hyosung HICO `success_candidate, price unavailable`

```text
symbol = 298040
case_type = success_candidate
archetype = TRANSFORMER_CAPACITY_EXPANSION_STAGE2
```

### stage date

```text
Stage 1:
2025-12-02
- U.S. transformer / grid-equipment shortage intensifies.
- renewable energy, data centers, EVs and aging infrastructure push demand.

Stage 2:
2025-12-02
- Reuters Events reports GSU transformer demand up 274% since 2019.
- average GSU delivery delay 143 weeks.
- Hyosung HICO to spend $157M expanding Memphis transformer plant.
- U.S. is top transformer importer.
- price hikes expected until 2030.

Stage 3:
없음
- capacity expansion is Stage 2.
- Green requires order backlog, shipment, utilization, price/margin, working capital.
```

Hyosung Heavy는 전력망 supercycle의 구조 후보지만, 이번 라운드에서는 직접 주가 anchor를 찾지 못했다. 대신 산업 anchor는 강하다. U.S. GSU transformer demand는 2019년 이후 274% 증가했고, 평균 delivery delay는 143주다. Hyosung HICO는 Memphis transformer plant에 $157M 투자를 발표했다. 다만 이것은 capacity Stage 2일 뿐, 실제 backlog와 margin이 확인돼야 한다. ([Reuters][3])

### 실제 가격경로 검증

```json
{
  "case_id": "r1_loop14_hyosung_heavy_hico_transformer_capacity",
  "symbol": "298040",
  "stage2_date": "2025-12-02",
  "stage3_price": null,
  "price_data_source": "Reuters Events industry-capacity anchor",
  "gsu_transformer_demand_growth_since_2019_pct": 274,
  "gso_delivery_delay_weeks": 143,
  "hyosung_hico_memphis_expansion_usd_mn": 157,
  "us_transformer_importer_status": "top_transformer_importer",
  "price_hike_expected_until": 2030,
  "direct_stock_price_anchor": "price_data_unavailable_after_deep_search",
  "mfe_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_price_data_unavailable
rerating_result = transformer_capacity_expansion_stage2
stage_failure_type = capacity_expansion_not_backlog_margin_green
```

---

## Case D — HD Hyundai Heavy / HD Hyundai Mipo merger `event premium + 4B-watch`

```text
symbols = 329180 / 010620
case_type = event_premium + 4B-watch
archetype = SHIPBUILDING_MERGER_MASGA_4B
```

### stage date

```text
Stage 1:
2025-08-27
- HD Hyundai Heavy announces merger with HD Hyundai Mipo.
- merger framed around U.S.-Korea shipbuilding cooperation.
- MASGA / naval defence / U.S. shipbuilding capacity narrative.

Stage 2:
2025-08-27
- proposed exchange ratio: 1 HD Hyundai Mipo share for 1.04059146 HD Hyundai Heavy shares.
- merged company planned for December.
- target: larger slice of U.S. shipbuilding market.

Stage 4B:
2025-08-27
- HD Hyundai Heavy +11.3%.
- HD Hyundai Mipo +14.6%.
- both close at record highs.
- price moves before actual U.S. MRO / naval order / integration synergy.
```

HD Hyundai Heavy/Mipo merger는 R1에서 좋은 Stage 2지만, 가격경로는 명확한 4B-watch다. U.S.-Korea shipbuilding cooperation과 MASGA theme가 붙자 HD현대중공업 +11.3%, 미포 +14.6%로 record close가 나왔다. 하지만 Green은 실제 U.S. MRO 매출, naval order, dock capacity, 인력, 합병 synergy가 확인될 때다. ([Reuters][4])

### 실제 가격경로 검증

```json
{
  "case_id": "r1_loop14_hd_hhi_mipo_merger_masga_4b",
  "symbols": "329180/010620",
  "stage2_date": "2025-08-27",
  "stage4b_date": "2025-08-27",
  "stage3_price": null,
  "price_data_source": "Reuters merger event anchor",
  "hd_hyundai_heavy_event_mfe_pct": 11.3,
  "hd_hyundai_mipo_event_mfe_pct": 14.6,
  "exchange_ratio_mipo_to_hhi": 1.04059146,
  "merged_company_launch_target": "2025-12",
  "theme": "MASGA / U.S.-Korea shipbuilding cooperation",
  "actual_us_order_confirmed": false,
  "integration_synergy_confirmed": false,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium_4B_watch
rerating_result = shipbuilding_merger_MASGA_stage2
stage_failure_type = merger_theme_not_order_margin_green
```

---

## Case E — Samsung Heavy / Zvezda cancellation `hard 4C`

```text
symbol = 010140
case_type = 4C-thesis-break
archetype = SHIPBUILDING_ORDER_CANCELLATION_HARD_4C
```

### stage date

```text
Stage 1:
2020~2021
- Samsung Heavy wins Russia Zvezda icebreaker ship orders.
- contracts cover blocks/parts for icebreaker LNG carriers and shuttle tankers.

Stage 4C:
2025-06-18
- Samsung Heavy says two Zvezda orders cancelled.
- total value: 4.85T won / $3.54B.
- 10 icebreaker LNG carriers and 7 icebreaker shuttle tankers.
- Zvezda unilaterally informed termination in June 2024.
- Samsung filed Singapore arbitration in July 2024.
- prolonged Russia-Ukraine war created execution uncertainty.

Stage 3:
없음
- backlog that cannot execute is not Green.
```

Samsung Heavy는 R1의 hard 4C다. 4.85T won 규모의 수주가 실제 수행 불가능·계약취소·arbitration으로 바뀌었다. 조선업에서 order backlog는 강력한 evidence지만, 지정학·제재·선주 execution risk가 있으면 Stage 3가 아니라 4C다. ([Reuters][5])

### 실제 가격경로 검증

```json
{
  "case_id": "r1_loop14_samsung_heavy_zvezda_cancellation_hard_4c",
  "symbol": "010140",
  "stage4c_date": "2025-06-18",
  "stage3_price": null,
  "price_data_source": "Reuters contract-cancellation anchor",
  "cancelled_contract_value_krw_trn": 4.85,
  "cancelled_contract_value_usd_bn": 3.54,
  "icebreaker_lng_carriers": 10,
  "icebreaker_shuttle_tankers": 7,
  "zvezda_unilateral_termination_notice": "2024-06",
  "samsung_arbitration_request": "2024-07",
  "risk_cause": "Russia-Ukraine war / execution uncertainty / shipowner termination",
  "mfe": "N/A_no_valid_stage3",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = thesis_break
rerating_result = shipbuilding_order_cancellation_hard_4C
stage_failure_type = backlog_execution_failure
```

---

## Case F — Hanwha Aerospace share sale `false positive / dilution 4B`

```text
symbol = 012450
case_type = false_positive_score + 4B-watch
archetype = DEFENSE_DILUTION_FALSE_POSITIVE
```

### stage date

```text
Stage 1:
2024~2025
- defence export rally.
- Europe rearmament and global security spending support Korean defence names.
- Hanwha Aerospace order expectations surge.

Stage 4B:
2025-03-21
- Hanwha announces 3.6T won / $2.5B share sale for overseas expansion.
- shares -13%.
- worst session since 2016.
- planned issue nearly 6M shares at 605,000 won, 16% discount to previous close.
- stock had more than doubled YTD before announcement.

Stage 4C-watch / governance-quality gate:
2025-03-27
- FSS orders revised filing, saying original filing lacked information needed for rational investor decisions.

Stage 2 revised:
2025-04-18
- company later proposes 1.3T won new share issue to affiliates at 758,000 won/share.
- separate 2.3T won rights offering planned.
```

Hanwha Aerospace는 R1의 dilution calibration이다. 방산 수출 cycle이 아무리 좋아도, 대형 증자가 나오면 EPS·지분희석·자본배분 gate가 즉시 작동한다. 3.6T won share sale 발표 후 주가는 -13%였다. 이후 FSS가 공시 보완을 요구했고, 회사는 수정된 방식의 funding을 냈다. ([Financial Times][6])

### 실제 가격경로 검증

```json
{
  "case_id": "r1_loop14_hanwha_aerospace_share_sale_dilution",
  "symbol": "012450",
  "stage4b_date": "2025-03-21",
  "stage4c_watch_date": "2025-03-27",
  "stage3_price": null,
  "price_data_source": "FT / Reuters share-sale and FSS revision anchors",
  "initial_share_sale_krw_trn": 3.6,
  "initial_share_sale_usd_bn": 2.5,
  "event_mae_pct": -13,
  "planned_new_shares_mn": 6,
  "initial_issue_price_krw": 605000,
  "discount_to_previous_close_pct": -16,
  "stock_ytd_context": "more_than_doubled_before_share_sale",
  "revised_affiliate_issue_krw_trn": 1.3,
  "revised_affiliate_issue_price_krw": 758000,
  "separate_rights_offering_krw_trn": 2.3,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = false_positive_score
rerating_result = defence_export_theme_dilution_gate
stage_failure_type = order_growth_not_green_if_dilution_unclear
```

---

## Case G — Rainbow Robotics / Samsung stake `robotics event premium`

```text
symbol = 277810
case_type = event_premium
archetype = ROBOTICS_STRATEGIC_STAKE_EVENT_PREMIUM
```

### stage date

```text
Stage 1:
2024-12-30
- Samsung Electronics becomes largest shareholder of Rainbow Robotics.
- Samsung creates Future Robotics Office reporting to CEO.
- robotics becomes strategic growth segment.

Stage 2:
2024-12-30
- Samsung newly takes 267B won / $181M stake.
- Samsung had previously been second-largest shareholder with 14.71%.
- stake increases strategic control and robotics integration option.

Stage 3:
없음
- strategic stake is not Green.
- Green requires robot shipment, ASP, factory deployment, gross margin, repeat demand.
```

Rainbow Robotics는 로봇 theme의 Stage 2다. Samsung의 267B won 추가 지분투자와 Future Robotics Office 신설은 강한 strategic evidence다. 그러나 지분투자는 매출이 아니다. Stage 3는 실제 robot shipment, ASP, factory deployment, margin이 확인될 때만 가능하다. ([Reuters][7])

### 실제 가격경로 검증

```json
{
  "case_id": "r1_loop14_rainbow_robotics_samsung_stake_event",
  "symbol": "277810",
  "stage2_date": "2024-12-30",
  "stage3_price": null,
  "price_data_source": "Reuters strategic-stake anchor",
  "new_samsung_stake_investment_krw_bn": 267,
  "new_samsung_stake_investment_usd_mn": 181,
  "samsung_prior_stake_pct": 14.71,
  "future_robotics_office_created": true,
  "actual_robot_shipments_confirmed": false,
  "gross_margin_confirmed": false,
  "direct_event_price": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = event_premium
rerating_result = robotics_strategic_stake_stage2
stage_failure_type = strategic_stake_not_robot_revenue_green
```

---

## Case H — HD Hyundai Marine Solution IPO `industrial-service IPO overheat`

```text
symbol = 443060
case_type = overheat + success_candidate
archetype = INDUSTRIAL_SERVICE_IPO_OVERHEAT
```

### stage date

```text
Stage 1:
2024-04~05
- HD Hyundai Marine Solution IPO.
- marine after-sales / maintenance / repair / retrofit service.
- eco-friendly ships need more servicing and parts.

Stage 2:
2024-05-08
- IPO price: 83,400 won.
- raised 742.26B won / about $546M.
- 8.9M shares sold, half new shares and half KKR stake.
- 2023 revenue 1.43T won.
- 2023 OP 201.47B won.
- 2023 net profit 151.12B won.
- revenue +7.2%, OP +42%, net profit +44%.

Stage 4B:
2024-05-08
- shares close 163,900 won.
- +97% vs IPO price.
- market cap 7.29T won / $5.36B.
- institutional demand about 200x.

Stage 3:
없음
- first-day doubling is overheat.
- Green requires post-IPO earnings durability, lock-up/KKR exit, service-margin persistence.
```

HD Hyundai Marine Solution은 좋은 산업서비스 business지만, 첫날 +97%는 4B-watch다. marine after-sales와 retrofit 수요는 구조적으로 매력적이고 실적도 좋지만, IPO 첫날 두 배 가까운 급등은 aftermarket quality gate가 필요하다. ([월스트리트저널][8])

### 실제 가격경로 검증

```json
{
  "case_id": "r1_loop14_hd_hyundai_marine_ipo_overheat",
  "symbol": "443060",
  "stage2_date": "2024-05-08",
  "stage4b_date": "2024-05-08",
  "stage3_price": null,
  "price_data_source": "WSJ / Reuters IPO debut anchors",
  "ipo_price_krw": 83400,
  "close_price_krw": 163900,
  "debut_mfe_pct": 96.5,
  "ipo_raise_krw_bn": 742.26,
  "ipo_raise_usd_mn": 546,
  "shares_sold_mn": 8.9,
  "market_cap_close_krw_trn": 7.29,
  "market_cap_close_usd_bn": 5.36,
  "revenue_2023_krw_trn": 1.43,
  "op_2023_krw_bn": 201.47,
  "net_profit_2023_krw_bn": 151.12,
  "revenue_growth_2023_pct": 7.2,
  "op_growth_2023_pct": 42,
  "net_profit_growth_2023_pct": 44,
  "mfe_30d_90d": "price_data_unavailable_after_deep_search",
  "mae_30d_90d": "price_data_unavailable_after_deep_search"
}
```

### alignment

```text
score_price_alignment = success_candidate_but_overheat
rerating_result = industrial_service_IPO_stage2
stage_failure_type = first_day_IPO_pop_not_durable_stage3
```

---

# 5. 이번 R1 case별 stage date 요약

| case               | Stage 1               | Stage 2              | Stage 3           | Stage 4B                       | Stage 4C                         |
| ------------------ | --------------------- | -------------------- | ----------------- | ------------------------------ | -------------------------------- |
| Hyundai Rotem K2   | 2022-08               | 2025-08 second batch | 2024-04 candidate | 2025 rearmament overheat watch | local production/financing watch |
| LS Electric        | 2024-07-01            | U.S. grid growth     | N/A               | data-center/grid theme watch   | price failed                     |
| Hyosung Heavy/HICO | 2025-12-02            | transformer capacity | N/A               | capacity theme watch           | backlog/margin unconfirmed       |
| HD HHI/Mipo        | 2025-08-27            | merger/MASGA         | N/A               | +11.3/+14.6%                   | integration/order risk           |
| Samsung Heavy      | 2020~21 orders        | backlog              | N/A               | N/A                            | 2025-06-18 hard                  |
| Hanwha Aerospace   | 2024~25 defence rally | funding revised      | N/A               | 2025-03-21                     | dilution/FSS watch               |
| Rainbow Robotics   | 2024-12-30            | Samsung stake        | N/A               | robotics strategic premium     | shipment/margin absent           |
| HD Hyundai Marine  | 2024-05-08            | IPO                  | N/A               | +97% debut                     | lock-up/valuation watch          |

---

# 6. 실제 가격경로 검증 총괄

| case               |                                          가격 anchor | 해석                                 | 판정                             |
| ------------------ | -------------------------------------------------: | ---------------------------------- | ------------------------------ |
| Hyundai Rotem      |                     41,300 won, +9.3%, KOSPI -0.3% | shipment/revenue/OP estimate 동시 확인 | aligned_partial                |
| LS Electric        |                 208,500 won, -5.4%, target 280,000 | evidence 좋지만 가격 실패                 | evidence_good_but_price_failed |
| Hyosung Heavy/HICO | GSU demand +274%, delay 143 weeks, $157M expansion | 산업 evidence 강하지만 주가 anchor 없음      | success_candidate              |
| HD HHI/Mipo        |                                    +11.3% / +14.6% | merger/MASGA event premium         | 4B-watch                       |
| Samsung Heavy      |                    4.85T won / $3.54B cancellation | backlog hard break                 | thesis_break                   |
| Hanwha Aerospace   |                          -13%, 3.6T won share sale | 방산 성장보다 dilution gate              | false_positive_score           |
| Rainbow Robotics   |                             Samsung stake 267B won | strategic stake, not revenue       | event_premium                  |
| HD Hyundai Marine  |                       IPO 83,400 → 163,900, +96.5% | good business but IPO overheat     | success_candidate_overheat     |

---

# 7. score-price alignment 판정

```text
aligned:
- Hyundai Rotem K2 Poland delivery, partial.

structural_success_candidate:
- Hyundai Rotem
- LS Electric, if backlog/margin later confirms.
- Hyosung Heavy / HICO, if order backlog and capacity utilization confirm.

success_candidate:
- HD Hyundai Heavy / Mipo merger
- HD Hyundai Marine Solution
- Rainbow Robotics

evidence_good_but_price_failed:
- LS Electric.

false_positive_score:
- Hanwha Aerospace share-sale dilution.
- HD Hyundai Marine if first-day IPO pop is treated as Stage 3.
- HD HHI/Mipo if MASGA merger theme is treated as actual U.S. order.

event_premium:
- HD HHI/Mipo merger.
- Rainbow Robotics / Samsung stake.
- HD Hyundai Marine IPO.
- Samsung E&A-style mega-order analog should stay Stage 2 until margin/cashflow.

thesis_break:
- Samsung Heavy Zvezda cancellation.

price_moved_without_evidence:
- Rainbow Robotics if Samsung stake is scored as shipment/margin.
- HD HHI/Mipo if U.S. naval/MRO orders are assumed before contract.
- transformer/grid names if capacity expansion is assumed as margin without backlog.

hard_4C_confirmed:
- Samsung Heavy Industries Zvezda order cancellation.
```

---

# 8. 점수비중 교정

## 올릴 축

```text
actual_delivery_revenue +5
backlog_to_revenue_conversion +5
order_margin_visibility +5
working_capital_control +5
local_production_execution +4
capacity_utilization +5
customer_financing_visibility +4
dilution_adjusted_EPS +5
contract_cancellation_risk +5
aftermarket_IPO_demand +4
```

### 왜 올리나

Hyundai Rotem은 실제 K2 출하와 Q1 revenue/OP estimate가 같이 나와서 Stage 3 candidate로 인정할 수 있다. LS Electric은 성장 전망은 강했지만 주가는 -5.4%였으므로, estimate upgrade보다 실제 backlog·margin을 더 봐야 한다. Samsung Heavy는 backlog가 4.85T won 취소로 바뀌며 hard 4C가 됐다. Hanwha Aerospace는 방산 주문이 좋아도 dilution이 EPS를 바로 깎을 수 있음을 보여줬다. HD Hyundai Marine은 좋은 사업이지만 first-day +97%는 4B다.

## 내릴 축

```text
order_headline_only -5
customer_or_parent_name_only -5
strategic_stake_only -5
capacity_expansion_without_backlog -5
IPO_first_day_pop_only -5
merger_theme_without_synergy -5
defence_order_expectation_without_funding -4
dilutive_share_issue -5
geopolitical_contract_execution_risk -5
```

### 왜 내리나

R1에서 가장 큰 함정은 수주·전력망·방산·조선·로봇이라는 좋은 단어가 cash conversion보다 먼저 가격화되는 것이다. Stage 3는 “수주했다”가 아니라 “수주가 이익과 현금으로 내려왔다”다.

---

# 9. Green gate 강화 조건

```text
R1 Stage 3-Green 필수:
1. 수주가 실제 delivery/revenue로 전환됨.
2. order margin 또는 OP estimate가 확인됨.
3. working capital / advance payment / unbilled receivable risk 없음.
4. 방산은 정부 financing, 현지생산 조건, 납품 schedule 확인.
5. 전력망은 backlog, lead time, capacity utilization, ASP/margin 확인.
6. 조선은 dock capacity, 후판가, 인력, cancellation/sanction risk 확인.
7. 로봇은 strategic stake가 아니라 shipment, ASP, margin 확인.
8. IPO는 첫날 pop이 아니라 aftermarket demand와 실적 지속성 확인.
9. price path가 evidence 이후 따라옴.
```

---

# 10. 4B 조기감지 조건

```text
4B-watch:
- merger/MASGA/미국 MRO headline로 +10% 이상 급등.
- IPO debut +40~100% 급등.
- strategic stake / parent-name event로 revenue 전 급등.
- transformer/grid capacity 투자만으로 backlog 전 급등.
- defence order expectation으로 YTD 100%+ 급등.
- 수주 headline 발표 당일 +5~10% 급등.

4B-elevated:
- contract value는 크지만 delivery/revenue 미확인.
- 현지생산 / financing / 정부예산 남음.
- 증자/희석 가능성.
- 지정학·제재·선주 리스크.
- lock-up / PE exit.
```

---

# 11. 4C hard gate 조건

```text
Hard 4C:
- 대형 계약취소.
- shipowner termination / arbitration.
- 수주 실행 불가능 due sanctions / war.
- dilutive share issue after theme rally.
- FSS revision order / disclosure quality issue.
- IPO debut failure after aggressive pricing.
- strategic customer program cancellation.
- backlog not converting into revenue or cash.
```

이번 R1 Loop 14의 hard 4C는 **Samsung Heavy / Zvezda cancellation**이다. Hyundai Rotem은 `aligned_partial`, LS Electric은 `evidence_good_but_price_failed`, Hanwha Aerospace는 `false_positive_score`, HD HHI/Mipo와 HD Hyundai Marine은 `4B-watch`로 둔다.

---

# 12. production scoring 반영 여부

```text
production_scoring_changed = false
candidate_generation_input = false
shadow_weight_only = true
```

---

# 13. 레포 반영용 patch-ready 출력

## docs/round/round_211.md 요약

```md
# R1 Loop 14. Industrials / Orders / Infrastructure Price Validation

이번 라운드는 R1 Loop 14 price-validation 라운드다.

핵심 결론:
- Hyundai Rotem is aligned_partial Stage 3 candidate. 18 K2 tanks shipped to Poland contributed 270B won to Q1 revenue; OP estimate +85% YoY to 59.1B won; shares +9.3% to 41,300 won while KOSPI -0.3%. Second Poland batch is Stage 2 extension: 180 tanks, about $6.5B, with Polish local production.
- LS Electric is evidence_good_but_price_failed. Daiwa expected U.S. revenue share to rise from below 5% in 2022 to around 20% in 2024 and raised target 87% to 280,000 won, but shares were -5.4% at 208,500 won.
- Hyosung Heavy / HICO is transformer-capacity success_candidate. U.S. GSU transformer demand up 274% since 2019, delivery delay 143 weeks, Hyosung HICO Memphis expansion $157M. Direct stock OHLC unavailable.
- HD Hyundai Heavy / Mipo merger is MASGA event premium and 4B-watch. HD Hyundai Heavy +11.3%, Mipo +14.6%, record highs, exchange ratio 1.04059146. Actual U.S. orders and integration synergy required.
- Samsung Heavy / Zvezda is hard 4C. Two Russian icebreaker orders worth 4.85T won / $3.54B cancelled; covers 10 icebreaker LNG carriers and 7 icebreaker shuttle tankers. Backlog execution failed.
- Hanwha Aerospace is defence dilution false_positive_score. 3.6T won / $2.5B share sale plan drove shares -13%; FSS ordered revised filing; later 1.3T won affiliate issue and 2.3T won rights offering plan appeared.
- Rainbow Robotics / Samsung stake is robotics event premium. Samsung took 267B won / $181M additional stake and became largest shareholder, but shipment, ASP and margin are not confirmed.
- HD Hyundai Marine Solution is industrial-service IPO overheat. IPO price 83,400 won, close 163,900 won, +96.5%; 2023 revenue 1.43T won, OP 201.47B won, net profit 151.12B won. Aftermarket durability and lock-up/KKR exit required.
```

## docs/checkpoints/checkpoint_28a_round211_r1_loop14.md 요약

```md
# Checkpoint 28A Round 211 R1 Loop 14 Industrials Orders Infrastructure Price Validation

## 반영 내용
- R1 Loop 14 price-validation 라운드를 추가했다.
- Hyundai Rotem, LS Electric, Hyosung Heavy/HICO, HD Hyundai Heavy/Mipo, Samsung Heavy, Hanwha Aerospace, Rainbow Robotics, HD Hyundai Marine Solution을 비교했다.
- Reuters / WSJ / MarketWatch / FT anchors로 가능한 event MFE/MAE, stage price, contract value, IPO price, cancellation value, dilution amount를 계산했다.
- full adjusted OHLC가 확보되지 않은 항목은 price_data_unavailable_after_deep_search로 명시했다.
- production scoring은 변경하지 않았다.

## 핵심 보정
- actual delivery revenue, backlog-to-revenue conversion, order margin visibility, working-capital control, local production execution, capacity utilization, customer financing visibility, dilution-adjusted EPS, contract cancellation risk, aftermarket IPO demand 가중치 강화.
- order headline-only, customer/parent name-only, strategic stake-only, capacity expansion without backlog, IPO first-day pop-only, merger theme without synergy, defence order expectation without funding, dilutive share issue 감점 강화.
```

## data/e2r_case_library/cases_r1_loop14_round211.jsonl 초안

```jsonl
{"case_id":"r1_loop14_hyundai_rotem_k2_poland_delivery_stage3_candidate","symbol":"064350","company_name":"Hyundai Rotem","case_type":"structural_success_candidate","primary_archetype":"DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE","stage3_date":"2024-04_candidate","stage2_date":"2025-08-01_extension","price_validation":{"price_data_source":"WSJ event price anchor; Reuters Poland second-contract anchor","stage3_price_krw":41300,"event_mfe_pct":9.3,"kospi_same_context_pct":-0.3,"relative_outperformance_pp":9.6,"q1_revenue_from_18_k2_shipments_krw_bn":270,"q1_op_estimate_krw_bn":59.1,"op_estimate_growth_pct":85,"target_price_krw":47500,"target_upside_from_stage3_price_pct":15.0,"second_contract_value_usd_bn":6.5,"second_contract_tanks":180,"poland_local_production_units":61,"first_delivery_second_batch":2026,"polish_production_period":"2028-2030","mfe_30d_90d_180d_1y_2y":"price_data_unavailable_after_deep_search","mae_30d_90d_180d_1y":"price_data_unavailable_after_deep_search"},"score_price_alignment":"aligned_partial","rerating_result":"defense_export_delivery_stage3_candidate","notes":"Delivery/revenue/OP evidence supports Stage 3 candidate; financing/local production/margin gate remains."}
{"case_id":"r1_loop14_ls_electric_us_grid_growth_price_failed","symbol":"010120","company_name":"LS Electric","case_type":"evidence_good_but_price_failed","primary_archetype":"GRID_EQUIPMENT_US_GROWTH_STAGE2","stage2_date":"2024-07-01","price_validation":{"price_data_source":"MarketWatch/Dow Jones event anchor","stage3_price":null,"event_price_krw":208500,"event_mae_pct":-5.4,"us_revenue_share_2022_pct":"<5","us_revenue_share_2024_expected_pct":20,"revenue_forecast_raise_2024_2026_pct_range":"4-22","target_price_krw":280000,"target_price_raise_pct":87,"target_upside_from_event_price_pct":34.3,"mfe_30d_90d":"price_data_unavailable_after_deep_search","mae_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed","rerating_result":"grid_equipment_US_growth_stage2","notes":"Estimate/target upgrade did not translate to price Green; backlog/margin/working capital required."}
{"case_id":"r1_loop14_hyosung_heavy_hico_transformer_capacity","symbol":"298040","company_name":"Hyosung Heavy Industries / Hyosung HICO","case_type":"success_candidate","primary_archetype":"TRANSFORMER_CAPACITY_EXPANSION_STAGE2","stage2_date":"2025-12-02","price_validation":{"price_data_source":"Reuters Events industry-capacity anchor","stage3_price":null,"gso_transformer_demand_growth_since_2019_pct":274,"gsu_delivery_delay_weeks":143,"hyosung_hico_memphis_expansion_usd_mn":157,"us_transformer_importer_status":"top_transformer_importer","price_hike_expected_until":2030,"direct_stock_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_price_data_unavailable","rerating_result":"transformer_capacity_expansion_stage2","notes":"Capacity expansion and supply shortage are Stage 2; backlog, utilisation and margin required."}
{"case_id":"r1_loop14_hd_hhi_mipo_merger_masga_4b","symbol":"329180/010620","company_name":"HD Hyundai Heavy Industries / HD Hyundai Mipo","case_type":"event_premium_4b_watch","primary_archetype":"SHIPBUILDING_MERGER_MASGA_4B","stage2_date":"2025-08-27","stage4b_date":"2025-08-27","price_validation":{"price_data_source":"Reuters merger event anchor","stage3_price":null,"hd_hyundai_heavy_event_mfe_pct":11.3,"hd_hyundai_mipo_event_mfe_pct":14.6,"exchange_ratio_mipo_to_hhi":1.04059146,"merged_company_launch_target":"2025-12","actual_us_order_confirmed":false,"integration_synergy_confirmed":false,"mfe_30d_90d":"price_data_unavailable_after_deep_search","mae_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium_4B_watch","rerating_result":"shipbuilding_merger_MASGA_stage2","notes":"Merger/MASGA event drove record-high closes before U.S. order or integration margin proof."}
{"case_id":"r1_loop14_samsung_heavy_zvezda_cancellation_hard_4c","symbol":"010140","company_name":"Samsung Heavy Industries","case_type":"4c_thesis_break","primary_archetype":"SHIPBUILDING_ORDER_CANCELLATION_HARD_4C","stage4c_date":"2025-06-18","price_validation":{"price_data_source":"Reuters contract-cancellation anchor","stage3_price":null,"cancelled_contract_value_krw_trn":4.85,"cancelled_contract_value_usd_bn":3.54,"icebreaker_lng_carriers":10,"icebreaker_shuttle_tankers":7,"zvezda_unilateral_termination_notice":"2024-06","samsung_arbitration_request":"2024-07","risk_cause":"Russia-Ukraine war / execution uncertainty / shipowner termination","mfe":"N/A_no_valid_stage3","mae_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break","rerating_result":"shipbuilding_order_cancellation_hard_4C","notes":"Large backlog cancelled; geopolitical and shipowner execution risk are hard gates."}
{"case_id":"r1_loop14_hanwha_aerospace_share_sale_dilution","symbol":"012450","company_name":"Hanwha Aerospace","case_type":"false_positive_score","primary_archetype":"DEFENSE_DILUTION_FALSE_POSITIVE","stage4b_date":"2025-03-21","stage4c_date":"2025-03-27_watch","price_validation":{"price_data_source":"FT / Reuters share-sale and FSS revision anchors","stage3_price":null,"initial_share_sale_krw_trn":3.6,"initial_share_sale_usd_bn":2.5,"event_mae_pct":-13,"planned_new_shares_mn":6,"initial_issue_price_krw":605000,"discount_to_previous_close_pct":-16,"stock_ytd_context":"more_than_doubled_before_share_sale","revised_affiliate_issue_krw_trn":1.3,"revised_affiliate_issue_price_krw":758000,"separate_rights_offering_krw_trn":2.3,"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"false_positive_score","rerating_result":"defence_export_theme_dilution_gate","notes":"Defence order cycle can fail price alignment if dilution and disclosure quality are not scored."}
{"case_id":"r1_loop14_rainbow_robotics_samsung_stake_event","symbol":"277810","company_name":"Rainbow Robotics / Samsung Electronics","case_type":"event_premium","primary_archetype":"ROBOTICS_STRATEGIC_STAKE_EVENT_PREMIUM","stage2_date":"2024-12-30","price_validation":{"price_data_source":"Reuters strategic-stake anchor","stage3_price":null,"new_samsung_stake_investment_krw_bn":267,"new_samsung_stake_investment_usd_mn":181,"samsung_prior_stake_pct":14.71,"future_robotics_office_created":true,"actual_robot_shipments_confirmed":false,"gross_margin_confirmed":false,"direct_event_price":"price_data_unavailable_after_deep_search"},"score_price_alignment":"event_premium","rerating_result":"robotics_strategic_stake_stage2","notes":"Samsung stake is strategic Stage 2; robot shipment, ASP, margin and repeat demand required."}
{"case_id":"r1_loop14_hd_hyundai_marine_ipo_overheat","symbol":"443060","company_name":"HD Hyundai Marine Solution","case_type":"success_candidate_overheat","primary_archetype":"INDUSTRIAL_SERVICE_IPO_OVERHEAT","stage2_date":"2024-05-08","stage4b_date":"2024-05-08","price_validation":{"price_data_source":"WSJ / Reuters IPO debut anchors","stage3_price":null,"ipo_price_krw":83400,"close_price_krw":163900,"debut_mfe_pct":96.5,"ipo_raise_krw_bn":742.26,"ipo_raise_usd_mn":546,"shares_sold_mn":8.9,"market_cap_close_krw_trn":7.29,"market_cap_close_usd_bn":5.36,"revenue_2023_krw_trn":1.43,"op_2023_krw_bn":201.47,"net_profit_2023_krw_bn":151.12,"revenue_growth_2023_pct":7.2,"op_growth_2023_pct":42,"net_profit_growth_2023_pct":44,"mfe_30d_90d":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_but_overheat","rerating_result":"industrial_service_IPO_stage2","notes":"Strong service business but first-day +97% is 4B unless earnings durability and lock-up pressure clear."}
```

## data/sector_taxonomy/score_weight_profiles_round211_r1_loop14_v1.csv 초안

```csv
archetype,actual_delivery_revenue,backlog_to_revenue_conversion,order_margin_visibility,working_capital_control,local_production_execution,capacity_utilization,customer_financing_visibility,dilution_adjusted_eps,contract_cancellation_risk,aftermarket_ipo_demand,event_penalty,4b_watch_sensitivity,hard_4c_sensitivity,notes
DEFENSE_EXPORT_DELIVERY_STAGE3_CANDIDATE,+5,+5,+5,+4,+4,+3,+4,+3,+3,+1,-3,+4,+4,Hyundai Rotem shows delivery/revenue/OP evidence can support Stage 3 candidate.
GRID_EQUIPMENT_US_GROWTH_STAGE2,+3,+5,+5,+5,+2,+5,+2,+2,+3,+0,-5,+5,+3,LS Electric needs backlog/margin confirmation after estimate upgrade price failure.
TRANSFORMER_CAPACITY_EXPANSION_STAGE2,+3,+5,+5,+5,+2,+5,+2,+2,+3,+0,-4,+5,+3,Transformer shortage/capacity expansion is Stage 2 until utilisation and ASP/margin confirm.
SHIPBUILDING_MERGER_MASGA_4B,+3,+4,+5,+5,+3,+5,+3,+3,+4,+1,-5,+5,+4,HD HHI/Mipo merger needs U.S. orders, integration synergy and margin proof.
SHIPBUILDING_ORDER_CANCELLATION_HARD_4C,+0,+5,+5,+5,+2,+3,+4,+2,+5,+0,0,+4,+5,Samsung Heavy cancellation proves backlog execution risk is hard gate.
DEFENSE_DILUTION_FALSE_POSITIVE,+4,+5,+5,+4,+4,+3,+4,+5,+3,+1,-5,+5,+4,Hanwha Aerospace shows defence order cycle must be dilution-adjusted.
ROBOTICS_STRATEGIC_STAKE_EVENT_PREMIUM,+1,+2,+4,+3,+2,+4,+1,+2,+2,+0,-5,+5,+3,Strategic stake is not robot shipment/margin Green.
INDUSTRIAL_SERVICE_IPO_OVERHEAT,+4,+4,+5,+4,+1,+4,+1,+3,+2,+5,-5,+5,+3,HD Hyundai Marine needs aftermarket durability and lock-up/PE exit gate after +97% debut.
```

---

# 이번 R1 Loop 14 결론

```text
1. Hyundai Rotem은 R1에서 aligned_partial Stage 3 candidate다.
   실제 K2 납품, Q1 revenue, OP estimate, 주가반응이 함께 맞았다.

2. LS Electric은 evidence_good_but_price_failed다.
   U.S. grid growth 전망과 target 상향에도 주가는 -5.4%였다.

3. Hyosung Heavy/HICO는 전력망 success_candidate다.
   transformer shortage와 $157M expansion은 좋지만 direct price anchor와 backlog/margin이 필요하다.

4. HD Hyundai Heavy/Mipo merger는 MASGA 4B-watch다.
   +11.3%, +14.6% record close가 나왔지만 실제 U.S. order와 integration synergy 전에는 Green이 아니다.

5. Samsung Heavy는 hard 4C다.
   4.85T won / $3.54B Zvezda order cancellation은 backlog가 무너지는 전형이다.

6. Hanwha Aerospace는 false_positive_score다.
   방산 수출 기대가 강해도 3.6T won 증자와 -13% 가격반응은 dilution gate를 먼저 보게 만든다.

7. Rainbow Robotics는 robotics event premium이다.
   Samsung stake는 강한 Stage 2지만 robot shipment와 margin이 Stage 3 조건이다.

8. HD Hyundai Marine Solution은 산업서비스 success_candidate지만 IPO overheat다.
   +97% debut은 좋은 사업과 별개로 4B-watch가 떠야 한다.
```

한 문장으로 압축하면:

> **R1에서 진짜 Stage 3는 “수주·방산·전력망·조선·로봇·IPO가 좋다”가 아니라, 실제 납품·revenue recognition·order margin·working capital·capacity utilization·dilution-adjusted EPS·aftermarket demand가 숫자로 닫히는 순간이다.**

[1]: https://www.wsj.com/articles/hyundai-rotem-rallies-on-hopes-tank-exports-will-boost-earnings-9322d840?utm_source=chatgpt.com "Hyundai Rotem Rallies on Hopes Tank Exports Will Boost Earnings"
[2]: https://www.marketwatch.com/story/ls-electric-could-gain-from-solid-u-s-business-growth-opportunity-market-talk-3e926067?utm_source=chatgpt.com "LS Electric Could Gain From Solid U.S. Business Growth Opportunity -- Market Talk"
[3]: https://www.reuters.com/business/energy/grid-equipment-makers-invest-us-ease-supply-shortage--reeii-2025-12-02/?utm_source=chatgpt.com "Grid equipment makers invest in US to ease supply shortage"
[4]: https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/?utm_source=chatgpt.com "South Korean shipbuilder HD Hyundai Heavy to merge with affiliate HD Hyundai Mipo"
[5]: https://www.reuters.com/business/retail-consumer/samsung-heavy-says-354-billion-icebreaker-orders-russias-zvezda-cancelled-2025-06-18/?utm_source=chatgpt.com "Samsung Heavy says $3.54 billion icebreaker orders from Russia's Zvezda cancelled"
[6]: https://www.ft.com/content/994a0a80-414f-442f-bf41-f2dbde5a04ca?utm_source=chatgpt.com "South Korea's biggest defence group plans $2.5bn share sale to expand overseas"
[7]: https://www.reuters.com/technology/samsung-electronics-becomes-largest-shareholder-south-koreas-rainbow-robotics-2024-12-30/?utm_source=chatgpt.com "Samsung Electronics becomes largest shareholder of South Korea's Rainbow Robotics"
[8]: https://www.wsj.com/business/hd-hyundai-marine-solution-makes-strong-debut-in-south-korea-e5e63451?utm_source=chatgpt.com "KKR-Backed HD Hyundai Marine Makes Strong Debut in South Korea"

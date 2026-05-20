순서상 이번은 **R1 Loop 16 — 산업재·수주·인프라 trigger-level price validation 라운드**다.

이번 R1은 R13 이후 다시 시작하는 첫 라운드라, 핵심을 조금 바꿔야 한다. **“수주 headline”을 많이 모으는 것보다, 수주·M&A·증설·전략투자가 실제로 backlog→매출→마진→현금흐름으로 이어지는지**를 더 엄격히 본다. 반대로 **대형수주, 조선 M&A, 전력기기 슈퍼사이클, 로봇/데이터센터 인프라 headline**만으로 Green을 주면 안 된다.

```text
round = R1 Loop 16
round_id = round_237
large_sector = INDUSTRIALS_ORDERS_INFRASTRUCTURE
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R2 Loop 16
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y/2Y window는 안정적으로 직접 확보하지 못했다. 그래서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 분리한다. 대신 Reuters/WSJ/MarketWatch가 보도한 **event return, event price, contract value, sector move, market-relative return**을 trigger anchor로 사용한다. R13에서 정리한 원칙대로, **OHLC 미확보 때문에 Stage 후보 자체를 강등하지 않는다.**

---

# 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
```

R1의 core gate는 아래다.

```text
해외 EPC:
signed contract → contract size vs annual order wins → backlog → margin → cash collection → cost overrun

전력기기:
grid / data center demand → transformer order → lead time / capacity → ASP → copper/steel cost → margin → delivery

조선:
contract wins / ship price → backlog → steel cost → delivery schedule → margin → working capital

M&A / 합병:
strategic fit → integration → order funnel → capacity utilization → margin → dilution / control premium

로봇·자동화:
strategic shareholder → product integration → factory deployment → external orders → recurring service revenue

인프라 지정학:
U.S./China policy → sanctions / port fees / naval MRO → order opportunity or contract cancellation → 4B/4C overlay
```

---

# 2. 대상 canonical archetype

```text
OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE
GRID_TRANSFORMER_DATA_CENTER_STAGE2
SHIPBUILDING_MERGER_SCALE_STAGE2_WITH_INTEGRATION_4B
SHIPBUILDING_CONTRACT_WIN_STAGE2_ACTIONABLE
SHIPBUILDING_ORDER_CANCELLATION_4C
GEOPOLITICAL_SANCTION_SHIPBUILDING_4C_WATCH
ROBOTICS_STRATEGIC_CONTROL_STAGE2_WITH_ORDER_GATE
DATA_CENTER_COOLING_MA_STAGE2_PRICE_MUTED
AEROSPACE_EXPORT_CONTRACT_STAGE2
```

---

# 3. deep sub-archetype

```text
Samsung E&A / Fadhili:
- Saudi Aramco Fadhili gas expansion
- $6B contract
- shares +8.5% to 26,750 won
- KOSPI -1.4%
- annual contract wins average KRW8.6T context
- Stage2-Actionable / Stage3-Yellow candidate

LS Electric / U.S. transformer:
- U.S. transformer shortage
- GSU demand +274% since 2019
- substation transformer demand +116%
- transformer prices +80% over five years
- large transformer lead time up to four years
- LS Electric $312M U.S. utility contract for 525kV transformers to data center
- Stage2 event; Green requires capacity/margin/delivery

HD Hyundai Heavy + HD Hyundai Mipo:
- merger to expand U.S. shipbuilding opportunity
- MASGA / U.S.-Korea shipbuilding cooperation
- HD Hyundai Heavy +11.3%
- HD Hyundai Mipo +14.6%
- both record highs
- Stage2-Actionable but integration 4B

Korean shipbuilding contract-win basket:
- Samsung Heavy +16%
- Hanwha Ocean +13%
- HD Hyundai Heavy +11%
- South Korea 50% February global shipbuilding order share
- Clarksons Newbuilding Price Index rising
- Stage2-Actionable, but margin/delivery gate

Samsung Heavy / Zvezda cancellation:
- 4.85T won / $3.54B cancellation
- 10 icebreaker LNG carrier blocks and 7 icebreaker shuttle tanker parts
- arbitration / Russia-Ukraine uncertainty
- order-cancellation 4C-watch

Hanwha Ocean / China sanctions:
- China sanctions five U.S.-linked Hanwha Ocean units
- Hanwha Ocean -5.8%
- HD Hyundai Heavy -4.1%
- U.S. shipbuilding/geopolitical opportunity has 4C overlay

Rainbow Robotics / Samsung:
- Samsung becomes largest shareholder
- 267B won / $181M additional stake
- Samsung Future Robotics Office
- Stage2 strategic control, but no external robot-order evidence yet

Samsung / FlaktGroup:
- 1.5B euro / $1.68B data-center cooling acquisition
- Samsung shares +0.7%
- evidence good but price muted
- data-center cooling infra Stage2, not Green
```

---

# 4. 선정 case 요약

| bucket                                 | case                                | 핵심 판정                                                                                                     |
| -------------------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------- |
| structural_success / Stage2-Actionable | Samsung E&A / Fadhili               | $6B 수주, +8.5%, KOSPI -1.4%. contract size와 relative strength가 닫힘                                          |
| Stage2 event / Yellow 후보 보류            | LS Electric / U.S. transformer      | U.S. transformer shortage + LS $312M data-center transformer contract. 가격 anchor 부족, capacity/margin gate |
| Stage2-Actionable + 4B                 | HD Hyundai Heavy / Mipo merger      | HHI +11.3%, Mipo +14.6%, record highs. U.S. shipbuilding optionality지만 integration gate                   |
| Stage2-Actionable basket               | Shipbuilding contract wins          | Samsung Heavy +16%, Hanwha Ocean +13%, HD Hyundai Heavy +11%. 선가·수주 momentum 강함                           |
| 4C-watch                               | Samsung Heavy / Zvezda cancellation | $3.54B order cancellation. sanctions/war/order execution risk                                             |
| 4C-watch                               | Hanwha Ocean / China sanctions      | Hanwha Ocean -5.8%, HD Hyundai Heavy -4.1%. U.S. shipbuilding opportunity의 geopolitical overlay           |
| Stage2 with order gate                 | Rainbow Robotics / Samsung          | Samsung largest shareholder, robotics office. 실제 order/revenue 전에는 Yellow 금지                              |
| evidence_good_price_muted              | Samsung / FlaktGroup                | AI data-center cooling M&A지만 Samsung +0.7%. price가 Green을 거부                                              |

---

# 5. Case별 trigger grid

## Case A — Samsung E&A / Saudi Aramco Fadhili gas expansion

```text
symbol = 028050
case_type = structural_success / Stage2-Actionable
archetype = OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE
```

| trigger | type                    |       date | 당시 공개 evidence                                                                             | 가격 anchor                      | outcome          |
| ------- | ----------------------- | ---------: | ------------------------------------------------------------------------------------------ | ------------------------------ | ---------------- |
| T0      | Stage2 evidence         | 2024-04-02 | Aramco awards $7.7B Fadhili EPC package to Samsung Engineering, GS E&C, Nesma              | no company price yet           | Stage2           |
| T1      | Stage2-Actionable       | 2024-04-03 | Samsung E&A takes around $6B share of project                                              | +8.5%, 26,750 won, KOSPI -1.4% | excellent entry  |
| T2      | Stage3-Yellow candidate | 2024-04-03 | contract comparable to 2017~2023 average annual contract wins KRW8.6T; completion Nov 2027 | same                           | Yellow candidate |
| T3      | 4B-watch                |  2024~2027 | EPC margin, cost overrun, cash collection, Saudi execution risk                            | full OHLC unavailable          | 4B               |
| T4      | Stage3-Green            |        N/A | backlog-to-OP and cashflow conversion not verified                                         | N/A                            | no Green         |

Samsung E&A는 R1에서 가장 좋은 “수주→Stage2-Actionable” template이다. Aramco는 Fadhili gas plant capacity를 2.5B scf/d에서 4B scf/d로 키우는 $7.7B package를 Samsung Engineering, GS E&C, Nesma에 award했고, Samsung E&A는 약 $6B 규모 계약을 따냈다. 주가는 26,750원까지 +8.5% 올랐고, 같은 시간 KOSPI는 -1.4%였으며, KB Securities는 이 수주가 회사의 2017~2023년 평균 연간 수주액 KRW8.6T와 비교해 큰 규모라고 평가했다. ([Reuters][1])

```json
{
  "case_id": "r1_loop16_samsung_ea_fadhili",
  "symbol": "028050",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_to_Stage3-Yellow_candidate",
  "trigger_date": "2024-04-03",
  "contract_value_usd_bn": 6.0,
  "aramco_total_package_usd_bn": 7.7,
  "event_mfe_pct": 8.5,
  "event_price_high_krw": 26750,
  "kospi_same_context_pct": -1.4,
  "market_relative_return_pp": 9.9,
  "average_annual_contract_wins_2017_2023_krw_trn": 8.6,
  "completion_target": "2027-11",
  "stage3_gate_missing": [
    "gross_margin",
    "cash_collection_schedule",
    "cost_overrun_visibility",
    "Saudi_execution_delay_risk",
    "backlog_to_OP_conversion"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable"
}
```

---

## Case B — LS Electric / U.S. transformer and data-center grid demand

```text
symbol = 010120
case_type = Stage2 event / Stage2-Actionable candidate
archetype = GRID_TRANSFORMER_DATA_CENTER_STAGE2
```

| trigger | type                        |       date | 당시 공개 evidence                                                                                                                          | 가격 anchor                   | outcome                   |
| ------- | --------------------------- | ---------: | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------- |
| T0      | awareness                   | 2024-07-01 | Daiwa says LS U.S. revenue could rise from <5% of total in 2022 to ~20% in 2024                                                         | shares -5.4% at 208,500 won | evidence good, price weak |
| T1      | Stage2 evidence             |    2025-11 | LS Electric announces $312M U.S. utility contract for 525kV transformers to large data center                                           | no LS price anchor          | Stage2                    |
| T2      | Stage2-Actionable candidate | 2026-05-11 | U.S. GSU transformer demand +274%, substation transformer demand +116% since 2019; transformer prices +80%; lead times up to four years | industry evidence           | candidate                 |
| T3      | 4B-watch                    |       2026 | long lead times, copper/grain-oriented electrical steel constraints, capacity bottleneck                                                | no OHLC                     | 4B                        |
| T4      | Stage3-Yellow               |        N/A | LS-specific backlog, capacity, ASP/margin, delivery schedule not verified                                                               | N/A                         | no Yellow                 |

LS Electric은 R1에서 “좋은 산업 evidence지만 가격/실적 gate가 남은” case다. Daiwa는 LS Electric의 U.S. revenue 비중이 2022년 5% 미만에서 2024년 약 20%까지 올라갈 수 있다고 봤고, data-center construction, renewable-energy projects, EV value chain을 근거로 target price를 87% 올렸다. 다만 해당 보도 시점의 주가는 208,500원으로 -5.4%였기 때문에, 이 trigger는 “evidence good, price not confirmed”로 기록해야 한다. ([마켓워치][2])

이후 Reuters는 U.S. transformer shortage를 다루며, LS Electric이 2025년 11월 U.S. utility와 $312M 규모 525kV extra-high-voltage transformer 공급계약을 맺어 2027~2029년 southeastern U.S. large-scale data center에 공급한다고 보도했다. 같은 기사에서 U.S. GSU transformer demand는 2019년 이후 +274%, substation transformer demand는 +116%, transformer prices는 5년간 약 +80%, large unit lead time은 최대 4년까지 길어졌다고 설명했다. ([Reuters][3])

```json
{
  "case_id": "r1_loop16_ls_electric_us_transformer",
  "symbol": "010120",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_event_to_Actionable_candidate",
  "t0_date": "2024-07-01",
  "t0_price_krw": 208500,
  "t0_event_return_pct": -5.4,
  "us_revenue_share_2022_pct": "<5",
  "us_revenue_share_2024e_pct": 20,
  "target_price_raise_pct": 87,
  "target_price_krw": 280000,
  "t1_contract_value_usd_mn": 312,
  "product": "525kV extra-high-voltage transformers",
  "delivery_period": "2027-2029",
  "end_market": "large-scale U.S. data center",
  "us_gsu_transformer_demand_growth_since_2019_pct": 274,
  "us_substation_transformer_demand_growth_since_2019_pct": 116,
  "transformer_price_rise_5y_pct": 80,
  "large_transformer_lead_time_years": 4,
  "stage3_gate_missing": [
    "LS_specific_order_backlog",
    "capacity_expansion",
    "ASP_margin",
    "copper_GOES_cost_pass_through",
    "delivery_execution"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_grid_event_not_Green"
}
```

---

## Case C — HD Hyundai Heavy Industries / HD Hyundai Mipo merger

```text
symbols = 329180 / 010620
case_type = Stage2-Actionable + integration 4B
archetype = SHIPBUILDING_MERGER_SCALE_STAGE2_WITH_INTEGRATION_4B
```

| trigger | type              |       date | 당시 공개 evidence                                                                         | 가격 anchor                                  | outcome    |
| ------- | ----------------- | ---------: | -------------------------------------------------------------------------------------- | ------------------------------------------ | ---------- |
| T0      | awareness         |       2025 | U.S.-Korea shipbuilding cooperation / MASGA / naval demand                             | no price                                   | Stage1     |
| T1      | Stage2-Actionable | 2025-08-27 | HD Hyundai Heavy to merge with HD Hyundai Mipo, aimed at U.S. shipbuilding expansion   | HHI +11.3%, Mipo +14.6%, both record highs | Actionable |
| T2      | 4B-watch          |  2025~2026 | share-exchange ratio, integration, U.S. contract conversion, labor/capacity allocation | no full OHLC                               | 4B         |
| T3      | Stage3-Yellow     |        N/A | U.S. naval/commercial contracts, synergy, margin not confirmed                         | N/A                                        | no Yellow  |

HD Hyundai Heavy–Mipo merger는 R1 조선에서 좋은 Stage2-Actionable이다. Reuters는 세계 최대 조선사 HD Hyundai Heavy가 affiliate HD Hyundai Mipo와 merger를 추진해 U.S. shipbuilding market 진출을 강화한다고 보도했다. 발표 후 HD Hyundai Heavy는 +11.3%, HD Hyundai Mipo는 +14.6% 상승했고 둘 다 record highs로 마감했다. 다만 이건 closing과 synergy가 아직 닫히지 않은 Stage2이며, U.S. contract conversion과 integration이 Stage3 gate다. ([Reuters][4])

```json
{
  "case_id": "r1_loop16_hd_hyundai_heavy_mipo_merger",
  "symbols": "329180/010620",
  "best_trigger": "T1",
  "best_trigger_type": "Stage2-Actionable_with_integration_4B",
  "trigger_date": "2025-08-27",
  "hd_hyundai_heavy_event_return_pct": 11.3,
  "hd_hyundai_mipo_event_return_pct": 14.6,
  "event_price_status": "both_record_highs",
  "share_exchange_ratio": "1_HD_Hyundai_Mipo_share_for_1.04059146_HD_Hyundai_Heavy_shares",
  "strategic_focus": [
    "U.S._shipbuilding_market",
    "MASGA",
    "large_and_mid_sized_shipyard_integration",
    "naval_and_commercial_capacity"
  ],
  "stage3_gate_missing": [
    "merger_completion",
    "U.S._contract_awards",
    "integration_synergy",
    "yard_capacity_utilization",
    "margin_after_integration"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_with_4B_integration_overlay"
}
```

---

## Case D — Korean shipbuilding contract-win basket

```text
symbols = 010140 / 042660 / 329180
company_scope = Samsung Heavy Industries / Hanwha Ocean / HD Hyundai Heavy
case_type = Stage2-Actionable basket
archetype = SHIPBUILDING_CONTRACT_WIN_STAGE2_ACTIONABLE
```

| trigger | type              |    date | 당시 공개 evidence                                                                                                  | 가격 anchor                                                    | outcome    |
| ------- | ----------------- | ------: | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------- |
| T0      | awareness         |    2024 | newbuilding price recovery and Korea order-share rebound                                                        | no price                                                     | Stage1     |
| T1      | Stage2-Actionable | 2024-03 | brisk contract wins and rising new-vessel prices                                                                | Samsung Heavy +16%, Hanwha Ocean +13%, HD Hyundai Heavy +11% | Actionable |
| T2      | Stage2 validation | 2024-03 | South Korea took 50% of global shipbuilding contract wins in February; Clarksons Newbuilding Price Index rising | same                                                         | validation |
| T3      | 4B-watch          |   2024~ | steel cost, labor, delivery schedule, ship-price contract mix                                                   | no OHLC                                                      | 4B         |
| T4      | Stage3-Yellow     |     N/A | company-specific margin and delivery conversion not verified                                                    | N/A                                                          | no Yellow  |

이 case는 R1에서 “업종 전체 Stage2-Actionable”이다. WSJ/Dow Jones는 South Korean shipbuilders가 brisk contract wins와 new vessel price 상승 기대에 급등했고, Samsung Heavy +16%, Hanwha Ocean +13%, HD Hyundai Heavy +11%였다고 보도했다. Clarksons Research 기준 한국은 2월 global shipbuilding contract wins의 50%를 차지하며 중국을 제쳤고, Newbuilding Price Index도 상승했다. 다만 이건 아직 수주·선가 momentum이지, 각 회사의 steel cost, delivery, margin이 닫힌 Green은 아니다. ([월스트리트저널][5])

```json
{
  "case_id": "r1_loop16_shipbuilding_contract_win_basket",
  "symbols": "010140/042660/329180",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_basket",
  "trigger_period": "2024-03",
  "samsung_heavy_event_return_pct": 16,
  "hanwha_ocean_event_return_pct": 13,
  "hd_hyundai_heavy_event_return_pct": 11,
  "korea_global_shipbuilding_order_share_feb_pct": 50,
  "newbuilding_price_index_trend": "rising",
  "stage3_gate_missing": [
    "company_specific_order_backlog",
    "steel_cost_pass_through",
    "delivery_schedule",
    "gross_margin",
    "working_capital",
    "customer_cancellation_risk"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_promote_candidate_basket"
}
```

---

## Case E — Samsung Heavy Industries / Russia Zvezda cancellation

```text
symbol = 010140
case_type = 4C-watch / order cancellation
archetype = SHIPBUILDING_ORDER_CANCELLATION_4C
```

| trigger | type           |       date | 당시 공개 evidence                                                                               | 가격 anchor            | outcome            |
| ------- | -------------- | ---------: | -------------------------------------------------------------------------------------------- | -------------------- | ------------------ |
| T0      | original order |  2020~2021 | icebreaker LNG carriers / shuttle tankers orders from Russia’s Zvezda                        | no current price     | old Stage2         |
| T1      | 4C-watch       | 2025-06-18 | Samsung Heavy says two orders worth 4.85T won / $3.54B cancelled                             | no event price found | order cancellation |
| T2      | 4C validation  | 2025-06-18 | Zvezda had unilaterally notified termination in 2024; Samsung filed arbitration in Singapore | no price             | legal 4C           |
| T3      | relief         |        N/A | damages recovery / replacement order not confirmed                                           | N/A                  | no relief          |

Samsung Heavy는 R1 조선의 hard negative template이다. Reuters는 Samsung Heavy가 Russia Zvezda 관련 두 orders, 총 4.85T won / $3.54B 규모를 cancellation 처리했다고 보도했다. 이 계약은 10 icebreaker LNG carriers와 7 icebreaker shuttle tankers의 parts and blocks 공급을 포함했고, Zvezda가 2024년 일방적으로 termination을 통보했으며 Samsung은 Singapore arbitration을 제기했다. 이 case는 **order backlog가 지정학·제재·법적분쟁으로 사라지는 4C-watch**다. ([Reuters][6])

```json
{
  "case_id": "r1_loop16_samsung_heavy_zvezda_cancellation",
  "symbol": "010140",
  "best_trigger": "T1/T2",
  "best_trigger_type": "4C_watch_order_cancellation",
  "trigger_date": "2025-06-18",
  "cancelled_order_value_krw_trn": 4.85,
  "cancelled_order_value_usd_bn": 3.54,
  "original_order_period": "2020-2021",
  "cancelled_scope": [
    "10_icebreaker_LNG_carrier_parts_blocks",
    "7_icebreaker_shuttle_tanker_parts_blocks"
  ],
  "counterparty": "Zvezda",
  "arbitration": "Singapore",
  "direct_event_price_anchor": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "order_cancellation_4C_watch"
}
```

---

## Case F — Hanwha Ocean / China sanctions on U.S.-linked units

```text
symbols = 042660 / 329180 read-through
case_type = 4C-watch / geopolitical sanction
archetype = GEOPOLITICAL_SANCTION_SHIPBUILDING_4C_WATCH
```

| trigger | type       |       date | 당시 공개 evidence                                                             | 가격 anchor                                  | outcome            |
| ------- | ---------- | ---------: | -------------------------------------------------------------------------- | ------------------------------------------ | ------------------ |
| T0      | awareness  |       2025 | Hanwha Ocean U.S. shipbuilding / Philly Shipyard / U.S. maritime policy    | no price                                   | Stage2 optionality |
| T1      | 4C-watch   | 2025-10-14 | China sanctions five U.S.-linked Hanwha Ocean subsidiaries                 | Hanwha Ocean -5.8%, HD Hyundai Heavy -4.1% | geopolitical 4C    |
| T2      | validation | 2025-10-15 | analysts saw sanctions as warning gesture, but shipbuilding tension rising | no new price                               | 4C-watch           |
| T3      | relief     |        N/A | formal contract protection / sanction scope clarity not confirmed          | N/A                                        | no relief          |

Hanwha Ocean은 U.S. shipbuilding optionality가 큰 만큼 China sanction 4C도 붙는다. Reuters는 China가 Hanwha Ocean의 U.S.-linked subsidiaries 5곳을 sanctions 대상으로 지정했고, 발표 후 Hanwha Ocean shares는 -5.8%, peer HD Hyundai Heavy는 -4.1% 하락했다고 보도했다. 이는 U.S. naval/MRO opportunity가 단순 호재가 아니라, U.S.-China maritime conflict 속에서 geopolitical overlay를 동반한다는 뜻이다. ([Reuters][7])

```json
{
  "case_id": "r1_loop16_hanwha_ocean_china_sanctions",
  "symbols": "042660/329180_readthrough",
  "best_trigger": "T1",
  "best_trigger_type": "4C_watch_geopolitical_sanction",
  "trigger_date": "2025-10-14",
  "sanctioned_units_count": 5,
  "hanwha_ocean_event_return_pct": -5.8,
  "hd_hyundai_heavy_event_return_pct": -4.1,
  "policy_context": [
    "U.S._China_port_fees",
    "U.S._shipbuilding_probe",
    "Hanwha_Philly_Shipyard",
    "U.S._maritime_capacity_rebuild"
  ],
  "trigger_outcome_label": "geopolitical_4C_watch"
}
```

---

## Case G — Rainbow Robotics / Samsung largest-shareholder trigger

```text
symbol = 277810
case_type = Stage2 strategic control with order gate
archetype = ROBOTICS_STRATEGIC_CONTROL_STAGE2_WITH_ORDER_GATE
```

| trigger | type              |                    date | 당시 공개 evidence                                                              | 가격 anchor                     | outcome              |
| ------- | ----------------- | ----------------------: | --------------------------------------------------------------------------- | ----------------------------- | -------------------- |
| T0      | awareness         |               2023~2024 | Samsung had existing 14.71% stake in Rainbow Robotics                       | no price                      | Stage1               |
| T1      | Stage2 evidence   | 2024-12-30 / 2024-12-31 | Samsung becomes largest shareholder via 267B won / $181M additional stake   | no Rainbow price anchor found | Stage2               |
| T2      | Stage2 validation |              2024-12-31 | Samsung creates Future Robotics Office reporting to CEO                     | no price                      | strategic validation |
| T3      | 4B-watch          |                   2025~ | strategic control without external robot order, factory deployment, revenue | no OHLC                       | 4B                   |
| T4      | Stage3-Yellow     |                     N/A | Samsung internal deployment / external order / margin not confirmed         | N/A                           | no Yellow            |

Rainbow Robotics는 R1 robotics/automation의 Stage2 trigger다. Reuters는 Samsung Electronics가 Rainbow Robotics의 largest shareholder가 됐고, 기존 14.71% stake에서 추가로 267B won / 약 $181M stake를 취득했다고 보도했다. 동시에 Samsung은 CEO 직속 Future Robotics Office를 세우겠다고 밝혔다. 이건 strategic control Stage2는 맞지만, robot unit sales, Samsung factory deployment, external orders가 없으면 Stage3로 올리면 안 된다. ([Reuters][8])

```json
{
  "case_id": "r1_loop16_rainbow_robotics_samsung_control",
  "symbol": "277810",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_strategic_control_with_order_gate",
  "trigger_date": "2024-12-30/2024-12-31",
  "samsung_additional_stake_krw_bn": 267,
  "samsung_additional_stake_usd_mn": 181,
  "samsung_prior_stake_pct": 14.71,
  "future_robotics_office": true,
  "direct_rainbow_event_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "Samsung_factory_deployment",
    "external_robot_orders",
    "unit_economics",
    "recurring_service_revenue",
    "supply_chain_capacity"
  ],
  "trigger_outcome_label": "Stage2_strategic_control_not_Green"
}
```

---

## Case H — Samsung / FlaktGroup data-center cooling acquisition

```text
symbol = 005930
case_type = evidence good, price muted
archetype = DATA_CENTER_COOLING_MA_STAGE2_PRICE_MUTED
```

| trigger | type            |       date | 당시 공개 evidence                                                               | 가격 anchor     | outcome     |
| ------- | --------------- | ---------: | ---------------------------------------------------------------------------- | ------------- | ----------- |
| T0      | awareness       |       2025 | AI data-center cooling demand / HVAC M&A search                              | no price      | Stage1      |
| T1      | Stage2 evidence | 2025-05-14 | Samsung to buy FlaktGroup for €1.5B / $1.68B                                 | Samsung +0.7% | price muted |
| T2      | 4B-watch        | 2025-05-14 | deal is more appliance/HVAC than AI-chip game changer; analysts underwhelmed | same          | 4B          |
| T3      | Stage3-Yellow   |        N/A | data-center cooling orders, integration, margin not confirmed                | N/A           | no Yellow   |

Samsung/FlaktGroup은 R1 data-center cooling infrastructure case다. Reuters는 Samsung이 German air conditioning and heating systems maker FlaktGroup을 €1.5B / $1.68B에 인수해 AI data-center cooling demand에 대응한다고 보도했다. 그러나 Samsung shares는 +0.7%에 그쳤고, analysts는 이 deal이 chip business game changer라기보다 consumer electronics/home appliance reinforcement라고 봤다. 즉 evidence는 좋지만 price가 Green을 인정하지 않은 `Stage2 price-muted` case다. ([Reuters][9])

```json
{
  "case_id": "r1_loop16_samsung_flaktgroup_datacenter_cooling",
  "symbol": "005930",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_MA_price_muted",
  "trigger_date": "2025-05-14",
  "acquisition_value_eur_bn": 1.5,
  "acquisition_value_usd_bn": 1.68,
  "event_return_pct": 0.7,
  "strategic_focus": [
    "AI_data_center_cooling",
    "HVAC",
    "commercial_cooling",
    "global_supply_experience"
  ],
  "market_pushback": [
    "not_chip_business_MA",
    "not_game_changing_deal",
    "appliance_HVAC_reinforcement"
  ],
  "stage3_gate_missing": [
    "data_center_cooling_orders",
    "integration_margin",
    "global_customer_wins",
    "capex_ROI",
    "recurring_service_revenue"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "evidence_good_but_price_muted"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                             | best trigger |                            entry anchor |                                                event MFE/MAE |            market-relative | full MFE/MAE | outcome                     |
| -------------------------------- | ------------ | --------------------------------------: | -----------------------------------------------------------: | -------------------------: | ------------ | --------------------------- |
| Samsung E&A / Fadhili            | T1/T2        |                         26,750 won high |                                                        +8.5% |      +9.9pp vs KOSPI -1.4% | unavailable  | excellent Stage2-Actionable |
| LS Electric / U.S. transformer   | T1/T2        | 208,500 won earlier analyst-note anchor |     -5.4% on earlier evidence; $312M later contract no price |                unavailable | unavailable  | Stage2, price not confirmed |
| HD Hyundai Heavy / Mipo merger   | T1           |                            record highs |                                      HHI +11.3%, Mipo +14.6% |                unavailable | unavailable  | Stage2 + integration 4B     |
| Shipbuilding contract-win basket | T1/T2        |                            sector event | Samsung Heavy +16%, Hanwha Ocean +13%, HD Hyundai Heavy +11% |                unavailable | unavailable  | Stage2-Actionable basket    |
| Samsung Heavy / Zvezda           | T1/T2        |                             unavailable |                                         no event price found |                        N/A | unavailable  | order-cancellation 4C       |
| Hanwha Ocean sanctions           | T1           |                                   event |                   Hanwha Ocean -5.8%, HD Hyundai Heavy -4.1% |                unavailable | unavailable  | geopolitical 4C-watch       |
| Rainbow Robotics / Samsung       | T1/T2        |                             unavailable |                                         no event price found |                        N/A | unavailable  | Stage2 strategic control    |
| Samsung / FlaktGroup             | T1/T2        |                           Samsung event |                                                        +0.7% | broadly in line with KOSPI | unavailable  | evidence good, price muted  |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
LS Electric:
U.S. transformer/data-center contract와 U.S. grid shortage는 명확한 Stage2.
하지만 LS-specific price reaction, backlog, margin이 없어서 Actionable 확정은 보류.

Rainbow Robotics:
Samsung control stake와 robotics office는 Stage2.
하지만 external robot order나 Samsung factory deployment 전에는 Yellow 금지.

Samsung FlaktGroup:
AI data-center cooling M&A는 Stage2.
하지만 Samsung +0.7%라 price가 Green을 거부했다.
```

## Stage 2-Actionable entry 성과

```text
Samsung E&A:
$6B contract + +8.5% + KOSPI -1.4% → excellent Stage2-Actionable.

HD Hyundai Heavy / Mipo:
merger + U.S. shipbuilding optionality + +11.3%/+14.6% → Stage2-Actionable.

Shipbuilding basket:
contract wins + ship price + sector rally → Stage2-Actionable.
```

## Stage3-Yellow 후보

```text
Samsung E&A:
margin/cash collection/cost overrun 확인 시 Yellow.

HD Hyundai Heavy / Mipo:
merger closing, U.S. contract conversion, capacity synergy 확인 시 Yellow.

LS Electric:
$312M contract가 backlog/margin/capacity로 연결되고 추가 수주가 확인되면 Yellow.

Shipbuilding basket:
newbuilding price와 order backlog가 delivery margin으로 연결되면 Yellow.
```

## Stage3-Green

```text
이번 R1 Loop 16에서 확정 Green 없음.

이유:
- EPC는 margin/cashflow까지 아직 확인 필요.
- 전력기기는 수요와 수주가 강하지만 LS-specific margin/capacity가 필요.
- 조선은 수주/선가가 좋지만 delivery margin과 steel cost가 gate.
- 로봇은 strategic control만으로는 revenue가 없다.
- M&A는 integration and order conversion 전에는 Green이 아니다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- Samsung E&A / Fadhili
- HD Hyundai Heavy / Mipo merger
- Shipbuilding contract-win basket

Stage2_promote_candidate:
- Samsung E&A
- HD Hyundai Heavy / Mipo
- Shipbuilding basket
- LS Electric, if later contract/backlog/margin confirms

evidence_good_but_price_failed_or_muted:
- LS Electric earlier U.S. growth note, because shares were -5.4%
- Samsung / FlaktGroup, because shares were only +0.7%

event_premium:
- HD Hyundai Heavy / Mipo merger if priced before integration synergies
- shipbuilding basket if priced on contract momentum before margin

false_positive_score:
- Rainbow Robotics if Samsung stake is treated as revenue
- Samsung FlaktGroup if cooling M&A is treated as AI-chip rerating
- shipbuilding sector if order wins are treated as delivered margin

thesis_break_watch:
- Samsung Heavy / Zvezda cancellation
- Hanwha Ocean / China sanctions

hard_4C_success:
- hard 4C not confirmed this round
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
signed_contract_value_vs_backlog,+5,"수주금액이 회사 annual order wins/backlog 대비 크면 Stage2-Actionable 승격","Samsung E&A"
market_relative_event_strength,+4,"KOSPI 대비 +5pp 이상이면 trigger 신뢰도 상승","Samsung E&A"
grid_transformer_backlog_capacity,+5,"전력기기는 transformer demand보다 actual backlog/capacity/margin이 중요","LS Electric"
shipbuilding_newbuilding_price_backlog,+5,"조선은 수주와 선가가 같이 올라야 Stage2-Actionable","Shipbuilding basket"
merger_integration_synergy,+4,"합병은 integration and contract conversion이 확인돼야 Yellow","HD Hyundai Heavy/Mipo"
robotics_order_revenue_bridge,+5,"전략지분은 revenue가 아니라 Stage2; order/deployment가 필요","Rainbow Robotics"
geopolitical_sanction_overlay,+5,"중국 제재/러시아 취소는 조선 backlog 4C overlay","Hanwha Ocean, Samsung Heavy"
data_center_cooling_order_conversion,+4,"cooling M&A는 실제 data-center order와 margin이 필요","Samsung/FlaktGroup"
```

## 내릴 축

```csv
axis,delta,reason,cases
headline_order_without_margin,-5,"대형수주는 margin/cash collection 전에는 Green 금지","Samsung E&A"
transformer_demand_without_company_margin,-4,"전력기기 demand만으로 Green 금지","LS Electric"
shipbuilding_order_without_delivery_margin,-5,"조선 수주는 delivery margin 전까지 Yellow 후보","Shipbuilding basket"
merger_announcement_without_integration,-5,"합병 headline은 integration 전까지 4B","HD Hyundai Heavy/Mipo"
strategic_stake_without_orders,-5,"전략지분은 revenue가 아니다","Rainbow Robotics"
M&A_without_customer_orders,-4,"FlaktGroup 같은 M&A는 actual order 전까지 price-muted 가능","Samsung/FlaktGroup"
geopolitical_opportunity_without_sanction_check,-5,"U.S. shipbuilding opportunity에는 China/Russia sanction overlay 필요","Hanwha Ocean, Samsung Heavy"
```

---

# 10. Stage 2-Actionable 승격 조건

R1 Loop 16 shadow rule:

```text
R1에서 Stage 2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. signed contract value가 annual order wins/backlog 대비 의미 있게 크다.
2. event return이 +5% 이상이다.
3. market-relative return이 +5pp 이상이다.
4. 발주처, 계약범위, 납기, capacity impact가 구체적이다.
5. 수요 cycle이 아니라 company-specific order/backlog가 확인된다.
6. ASP/ship price/transformer price 상승이 margin으로 pass-through될 가능성이 있다.
7. 4C overlay, cancellation, sanctions, legal dispute가 없다.
```

적용:

```text
Samsung E&A:
조건 1,2,3,4 충족 → Stage2-Actionable / Yellow candidate.

HD Hyundai Heavy/Mipo:
조건 2,3 일부, strategic fit 충족 → Stage2-Actionable + integration 4B.

Shipbuilding basket:
조건 2,5,6 충족 → Stage2-Actionable basket.

LS Electric:
조건 4,5는 충족하지만 price/margin 부족 → Stage2 event, Actionable 보류.
```

---

# 11. Stage 3-Yellow 조건

```text
Stage3-Yellow:
- Stage2-Actionable 이후 EPS/OP/FCF 경로가 바뀔 가능성이 높아진 상태.
- 하지만 margin, cash collection, delivery, integration, capacity 중 하나가 남은 상태.
```

Yellow 후보:

```text
Samsung E&A:
contract value와 price reaction은 충분. margin/cash conversion 확인 시 Yellow.

LS Electric:
$312M contract가 backlog와 transformer margin으로 확인되면 Yellow.

HD Hyundai Heavy/Mipo:
merger completion + U.S. order conversion + yard utilization 확인 시 Yellow.

Shipbuilding basket:
newbuilding price + backlog + steel cost control + delivery margin 확인 시 Yellow.
```

Yellow 금지:

```text
Rainbow Robotics:
Samsung stake만 있고 order/deployment 없음.

Samsung FlaktGroup:
M&A는 있지만 Samsung price muted and order conversion 없음.

Samsung Heavy/Zvezda:
order cancellation 4C.

Hanwha Ocean sanctions:
geopolitical 4C-watch.
```

---

# 12. Stage 3-Green 조건

```text
Stage3-Green:
- 해외 EPC 수주가 gross margin and cash collection으로 확인됨
- 전력기기 수주가 backlog, capacity utilization, ASP/margin으로 확인됨
- 조선 수주가 delivery margin and working capital로 확인됨
- 합병/M&A가 integration synergy and customer orders로 확인됨
- 로봇 전략지분이 factory deployment or external orders로 확인됨
- full-window MFE/MAE가 우호적임
- 4B/4C overlay가 해소됨
```

이번 R1 Loop 16에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + margin/cash/delivery conversion not yet verified
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- 대형수주 후 margin/cost overrun이 확인되지 않음
- shipbuilding merger가 integration data 없이 급등
- 전력기기 demand는 강하지만 capacity/margin이 확인되지 않음
- strategic stake / M&A가 revenue 없이 rerating
- U.S. infrastructure optionality가 geopolitical sanction과 충돌
```

적용:

```text
HD Hyundai Heavy/Mipo:
merger surge → integration 4B.

LS Electric:
industry shortage narrative → margin/capacity 4B.

Samsung FlaktGroup:
data-center cooling M&A → order conversion 4B.

Rainbow Robotics:
Samsung control stake → order/deployment 4B.
```

---

# 14. 4C hard gate 조건

```text
R1 4C:
- order cancellation
- customer unilateral termination
- arbitration/legal dispute
- sanctions blocking business with key market
- cost overrun destroying EPC margin
- ship delivery delay/cancellation
- strategic M&A integration failure
- transformer capacity expansion failure or input-cost squeeze
```

이번 R1 Loop 16 hard 4C 확정은 없다.

```text
hard_4c_not_confirmed = true
```

Strong 4C-watch:

```text
- Samsung Heavy / Zvezda cancellation
- Hanwha Ocean / China sanctions
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R13 이후 첫 R1에서 확인한 production 설계 원칙:

```text
1. 수주/계약/합병 evidence는 case row.
2. event price와 reported return은 trigger row.
3. full MFE/MAE는 ohlc_backfill row.
4. OHLC unavailable 때문에 Stage 후보를 강등하지 않는다.
5. 단, price anchor가 없으면 Actionable 확정은 보수적으로 둔다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_237.md 요약

```md
# R1 Loop 16. Industrials / Orders / Infrastructure Trigger-level Price Validation

이번 라운드는 R13 이후 다시 시작한 R1 Loop 16 trigger-level validation 라운드다.

핵심 결론:
- Samsung E&A / Fadhili is the cleanest R1 Stage2-Actionable case. Around $6B contract, shares +8.5% to KRW26,750, KOSPI -1.4%, and contract size comparable to average annual order wins of KRW8.6T. Green requires gross margin, cash collection and cost-overrun visibility.
- LS Electric / U.S. transformer is Stage2 event. U.S. transformer shortage is structural; LS Electric announced a $312M contract for 525kV transformers to a U.S. data-center project, but company-specific price/backlog/margin gates remain.
- HD Hyundai Heavy / HD Hyundai Mipo merger is Stage2-Actionable with integration 4B. HHI +11.3%, Mipo +14.6%, both record highs. Green requires merger completion, U.S. contract conversion and yard-utilization synergy.
- Korean shipbuilding contract-win basket is Stage2-Actionable. Samsung Heavy +16%, Hanwha Ocean +13%, HD Hyundai Heavy +11%; Korea took 50% of global shipbuilding orders in February. Green requires delivery margin and steel-cost pass-through.
- Samsung Heavy / Zvezda cancellation is 4C-watch. 4.85T won / $3.54B icebreaker LNG/shuttle tanker orders cancelled; arbitration and Russia-Ukraine uncertainty remain.
- Hanwha Ocean / China sanctions is geopolitical 4C-watch. Hanwha Ocean -5.8%, HD Hyundai Heavy -4.1% after China sanctioned five U.S.-linked units.
- Rainbow Robotics / Samsung is Stage2 strategic control. Samsung became largest shareholder with 267B won additional stake and created Future Robotics Office, but orders and deployment are missing.
- Samsung / FlaktGroup is evidence-good but price-muted. €1.5B / $1.68B data-center cooling M&A, Samsung +0.7%; order conversion and integration margin are missing.

Main calibration:
- Raise signed_contract_value_vs_backlog, market_relative_event_strength, grid_transformer_backlog_capacity, shipbuilding_newbuilding_price_backlog, merger_integration_synergy, robotics_order_revenue_bridge, geopolitical_sanction_overlay, data_center_cooling_order_conversion.
- Lower headline_order_without_margin, transformer_demand_without_company_margin, shipbuilding_order_without_delivery_margin, merger_announcement_without_integration, strategic_stake_without_orders, M&A_without_customer_orders, geopolitical_opportunity_without_sanction_check.
```

## docs/checkpoints/checkpoint_28a_round237_r1_loop16.md 요약

```md
# Checkpoint 28A Round 237 R1 Loop 16 Trigger-level Calibration

## 반영 내용
- R1 Loop 16 trigger-level validation을 수행했다.
- Samsung E&A Fadhili, LS Electric U.S. transformer, HD Hyundai Heavy/Mipo merger, shipbuilding contract-win basket, Samsung Heavy Zvezda cancellation, Hanwha Ocean China sanctions, Rainbow Robotics Samsung stake, Samsung FlaktGroup cooling M&A를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / WSJ / MarketWatch의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- 해외 EPC는 signed contract value, market-relative reaction, annual-order relevance로 Stage2-Actionable을 판단한다.
- 전력기기는 demand headline보다 backlog, capacity, ASP/margin, delivery가 중요하다.
- 조선은 contract wins and newbuilding prices가 Stage2지만, delivery margin and steel cost가 Green gate다.
- 합병/M&A는 integration and customer order conversion 전에는 4B overlay를 붙인다.
- 전략지분/로봇은 order and deployment 전에는 Stage2 이상으로 올리지 않는다.
- order cancellation and sanctions are R1 4C-watch triggers.
```

## data/e2r_case_library/cases_r1_loop16_round237.jsonl 초안

```jsonl
{"case_id":"r1_loop16_samsung_ea_fadhili","symbol":"028050","company_name":"Samsung E&A","case_type":"Stage2_promote_candidate","primary_archetype":"OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable_to_Stage3-Yellow_candidate","price_validation":{"trigger_date":"2024-04-03","contract_value_usd_bn":6.0,"aramco_total_package_usd_bn":7.7,"event_mfe_pct":8.5,"event_price_high_krw":26750,"kospi_same_context_pct":-1.4,"market_relative_return_pp":9.9,"average_annual_contract_wins_2017_2023_krw_trn":8.6,"completion_target":"2027-11","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable","notes":"Large signed EPC contract plus strong relative price reaction. Green requires margin/cashflow conversion."}
{"case_id":"r1_loop16_ls_electric_us_transformer","symbol":"010120","company_name":"LS Electric","case_type":"Stage2_event_to_Actionable_candidate","primary_archetype":"GRID_TRANSFORMER_DATA_CENTER_STAGE2","best_trigger":"T1/T2","stage_candidate":"Stage2_event","price_validation":{"t0_price_krw":208500,"t0_event_return_pct":-5.4,"us_revenue_share_2022_pct":"<5","us_revenue_share_2024e_pct":20,"target_price_raise_pct":87,"target_price_krw":280000,"t1_contract_value_usd_mn":312,"product":"525kV extra-high-voltage transformers","delivery_period":"2027-2029","end_market":"large-scale U.S. data center","us_gsu_transformer_demand_growth_since_2019_pct":274,"us_substation_transformer_demand_growth_since_2019_pct":116,"transformer_price_rise_5y_pct":80,"large_transformer_lead_time_years":4,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_event_not_Green","notes":"Grid transformer demand is structural, but company-specific backlog/margin/capacity gate remains."}
{"case_id":"r1_loop16_hd_hyundai_heavy_mipo_merger","symbol":"329180/010620","company_name":"HD Hyundai Heavy Industries / HD Hyundai Mipo","case_type":"Stage2_Actionable_with_4B_integration_overlay","primary_archetype":"SHIPBUILDING_MERGER_SCALE_STAGE2_WITH_INTEGRATION_4B","best_trigger":"T1","stage_candidate":"Stage2-Actionable + 4B-watch","price_validation":{"trigger_date":"2025-08-27","hd_hyundai_heavy_event_return_pct":11.3,"hd_hyundai_mipo_event_return_pct":14.6,"event_price_status":"both_record_highs","share_exchange_ratio":"1_HD_Hyundai_Mipo_share_for_1.04059146_HD_Hyundai_Heavy_shares","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate_with_4B","notes":"Merger and U.S. shipbuilding optionality are actionable; integration and contract conversion are gates."}
{"case_id":"r1_loop16_shipbuilding_contract_win_basket","symbol":"010140/042660/329180","company_name":"Samsung Heavy / Hanwha Ocean / HD Hyundai Heavy","case_type":"Stage2_promote_candidate_basket","primary_archetype":"SHIPBUILDING_CONTRACT_WIN_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable_basket","price_validation":{"trigger_period":"2024-03","samsung_heavy_event_return_pct":16,"hanwha_ocean_event_return_pct":13,"hd_hyundai_heavy_event_return_pct":11,"korea_global_shipbuilding_order_share_feb_pct":50,"newbuilding_price_index_trend":"rising","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_promote_candidate","notes":"Contract wins and ship-price momentum are actionable; delivery margin and steel cost are Green gates."}
{"case_id":"r1_loop16_samsung_heavy_zvezda_cancellation","symbol":"010140","company_name":"Samsung Heavy Industries","case_type":"4C_watch_order_cancellation","primary_archetype":"SHIPBUILDING_ORDER_CANCELLATION_4C","best_trigger":"T1/T2","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2025-06-18","cancelled_order_value_krw_trn":4.85,"cancelled_order_value_usd_bn":3.54,"original_order_period":"2020-2021","counterparty":"Zvezda","arbitration":"Singapore","direct_event_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"thesis_break_watch","notes":"Large shipbuilding order cancellation is R1 4C-watch."}
{"case_id":"r1_loop16_hanwha_ocean_china_sanctions","symbol":"042660/329180_readthrough","company_name":"Hanwha Ocean / HD Hyundai Heavy read-through","case_type":"4C_watch_geopolitical_sanction","primary_archetype":"GEOPOLITICAL_SANCTION_SHIPBUILDING_4C_WATCH","best_trigger":"T1","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2025-10-14","sanctioned_units_count":5,"hanwha_ocean_event_return_pct":-5.8,"hd_hyundai_heavy_event_return_pct":-4.1},"score_price_alignment":"thesis_break_watch","notes":"U.S. shipbuilding optionality carries China sanction/geopolitical overlay."}
{"case_id":"r1_loop16_rainbow_robotics_samsung_control","symbol":"277810","company_name":"Rainbow Robotics","case_type":"Stage2_strategic_control_with_order_gate","primary_archetype":"ROBOTICS_STRATEGIC_CONTROL_STAGE2_WITH_ORDER_GATE","best_trigger":"T1/T2","stage_candidate":"Stage2_strategic_control","price_validation":{"trigger_date":"2024-12-30/2024-12-31","samsung_additional_stake_krw_bn":267,"samsung_additional_stake_usd_mn":181,"samsung_prior_stake_pct":14.71,"future_robotics_office":true,"direct_rainbow_event_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"Samsung control stake is Stage2; orders/deployment are required for Yellow."}
{"case_id":"r1_loop16_samsung_flaktgroup_datacenter_cooling","symbol":"005930","company_name":"Samsung Electronics / FlaktGroup","case_type":"evidence_good_but_price_muted","primary_archetype":"DATA_CENTER_COOLING_MA_STAGE2_PRICE_MUTED","best_trigger":"T1/T2","stage_candidate":"Stage2_MA","price_validation":{"trigger_date":"2025-05-14","acquisition_value_eur_bn":1.5,"acquisition_value_usd_bn":1.68,"event_return_pct":0.7,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_muted","notes":"Data-center cooling M&A is real evidence, but price reaction was muted; order conversion required."}
```

## data/e2r_trigger_calibration/triggers_r1_loop16_round237.jsonl 초안

```jsonl
{"trigger_id":"r1l16_samsungea_fadhili_T1","case_id":"r1_loop16_samsung_ea_fadhili","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-03","evidence_available":"Samsung E&A signs around $6B Saudi Aramco Fadhili contract; shares +8.5% to KRW26,750 while KOSPI -1.4%","event_return_pct":8.5,"market_relative_return_pp":9.9,"trigger_outcome_label":"excellent_stage2_actionable","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r1l16_lselectric_transformer_T1","case_id":"r1_loop16_ls_electric_us_transformer","trigger_type":"Stage2_event","trigger_date":"2025-11/2026-05-11","evidence_available":"LS Electric $312M U.S. utility contract for 525kV transformers to data center; U.S. transformer demand and prices sharply higher","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_grid_event_not_Green","promote_to":"Stage2"}
{"trigger_id":"r1l16_hhi_mipo_merger_T1","case_id":"r1_loop16_hd_hyundai_heavy_mipo_merger","trigger_type":"Stage2-Actionable+4B-watch","trigger_date":"2025-08-27","evidence_available":"HD Hyundai Heavy to merge with HD Hyundai Mipo for U.S. shipbuilding expansion; HHI +11.3%, Mipo +14.6%, both record highs","event_return_pct":"HHI +11.3 / Mipo +14.6","trigger_outcome_label":"Stage2_Actionable_with_4B_integration_overlay","promote_to":"Stage2-Actionable+4B"}
{"trigger_id":"r1l16_shipbuilding_basket_T1","case_id":"r1_loop16_shipbuilding_contract_win_basket","trigger_type":"Stage2-Actionable_basket","trigger_date":"2024-03","evidence_available":"South Korean shipbuilders rally on brisk contract wins; Samsung Heavy +16%, Hanwha Ocean +13%, HD Hyundai Heavy +11%; Korea 50% of February global orders","event_return_pct":"16/13/11","trigger_outcome_label":"Stage2_promote_candidate_basket","promote_to":"Stage2-Actionable"}
{"trigger_id":"r1l16_samsungheavy_zvezda_T1","case_id":"r1_loop16_samsung_heavy_zvezda_cancellation","trigger_type":"4C-watch","trigger_date":"2025-06-18","evidence_available":"Samsung Heavy cancels 4.85T won / $3.54B Zvezda icebreaker LNG/shuttle tanker orders and pursues arbitration","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"order_cancellation_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r1l16_hanwhaocean_china_T1","case_id":"r1_loop16_hanwha_ocean_china_sanctions","trigger_type":"4C-watch","trigger_date":"2025-10-14","evidence_available":"China sanctions five U.S.-linked Hanwha Ocean subsidiaries; Hanwha Ocean -5.8%, HD Hyundai Heavy -4.1%","event_return_pct":-5.8,"trigger_outcome_label":"geopolitical_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r1l16_rainbow_samsung_T1","case_id":"r1_loop16_rainbow_robotics_samsung_control","trigger_type":"Stage2_strategic_control","trigger_date":"2024-12-30","evidence_available":"Samsung becomes largest shareholder of Rainbow Robotics via 267B won additional stake and creates Future Robotics Office","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_strategic_control_not_Green","promote_to":"Stage2"}
{"trigger_id":"r1l16_samsung_flakt_T1","case_id":"r1_loop16_samsung_flaktgroup_datacenter_cooling","trigger_type":"Stage2_MA_price_muted","trigger_date":"2025-05-14","evidence_available":"Samsung buys FlaktGroup for €1.5B / $1.68B to strengthen AI data-center cooling; shares +0.7%","event_return_pct":0.7,"trigger_outcome_label":"evidence_good_but_price_muted","promote_to":"Stage2_only"}
```

## data/sector_taxonomy/score_weight_profiles_round237_r1_loop16_v1.csv 초안

```csv
archetype,signed_contract_value_vs_backlog,market_relative_event_strength,grid_transformer_backlog_capacity,shipbuilding_newbuilding_price_backlog,merger_integration_synergy,robotics_order_revenue_bridge,geopolitical_sanction_overlay,data_center_cooling_order_conversion,headline_order_without_margin_penalty,transformer_demand_without_company_margin_penalty,shipbuilding_order_without_delivery_margin_penalty,merger_announcement_without_integration_penalty,strategic_stake_without_orders_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
OVERSEAS_EPC_BACKLOG_STAGE2_ACTIONABLE,+5,+4,+0,+0,+0,+0,+2,+0,-5,-1,-1,-1,-1,large signed contract+relative strength,margin/cash missing,backlog-to-OP+cash,Samsung E&A Fadhili.
GRID_TRANSFORMER_DATA_CENTER_STAGE2,+2,+2,+5,+0,+0,+0,+1,+1,-2,-5,-1,-1,-1,transformer shortage+data-center order,company margin/capacity missing,backlog+capacity+ASP margin,LS Electric U.S. transformer.
SHIPBUILDING_MERGER_SCALE_STAGE2_WITH_INTEGRATION_4B,+1,+4,+0,+5,+5,+0,+4,+0,-2,-1,-4,-5,-1,merger+record-high rally,integration/U.S. contracts pending,synergy+contracts+margin,HD Hyundai Heavy/Mipo.
SHIPBUILDING_CONTRACT_WIN_STAGE2_ACTIONABLE,+3,+5,+0,+5,+1,+0,+3,+0,-3,-1,-5,-2,-1,sector order wins+price momentum,delivery margin missing,delivery+steel cost+margin,Shipbuilding basket.
SHIPBUILDING_ORDER_CANCELLATION_4C,+0,+0,+0,+2,+0,+0,+5,+0,-1,-1,-1,-1,-1,order cancellation/arbitration,damages recovery pending,N/A,Samsung Heavy Zvezda.
GEOPOLITICAL_SANCTION_SHIPBUILDING_4C_WATCH,+0,+0,+0,+3,+0,+0,+5,+0,-1,-1,-2,-1,-1,sanctions/port-fee conflict,scope clarity pending,N/A,Hanwha Ocean China sanctions.
ROBOTICS_STRATEGIC_CONTROL_STAGE2_WITH_ORDER_GATE,+0,+2,+0,+0,+1,+5,+1,+0,-1,-1,-1,-1,-5,strategic shareholder/future office,orders/deployment missing,robot orders+unit economics,Rainbow Robotics.
DATA_CENTER_COOLING_MA_STAGE2_PRICE_MUTED,+1,+1,+1,+0,+3,+0,+1,+5,-1,-2,-1,-2,-1,M&A for data-center cooling,orders/integration margin missing,cooling orders+margin,Samsung FlaktGroup.
```

---

# 이번 R1 Loop 16 결론

```text
1. Samsung E&A / Fadhili는 R1의 가장 좋은 Stage2-Actionable case다.
   signed contract value, event return, market-relative strength가 모두 닫혔다.

2. LS Electric / U.S. transformer는 구조적 Stage2다.
   U.S. grid shortage와 $312M data-center transformer contract는 강하지만, LS-specific backlog/margin이 필요하다.

3. HD Hyundai Heavy / Mipo merger는 Stage2-Actionable + 4B다.
   주가반응은 강하지만 integration과 U.S. contract conversion 전에는 Green이 아니다.

4. Shipbuilding basket은 Stage2-Actionable이다.
   수주와 선가 momentum은 강하지만 delivery margin이 Green gate다.

5. Samsung Heavy / Zvezda cancellation은 order-cancellation 4C-watch다.
   backlog가 지정학/법적분쟁으로 사라질 수 있음을 보여준다.

6. Hanwha Ocean / China sanctions는 geopolitical 4C-watch다.
   U.S. shipbuilding opportunity에는 China sanction overlay가 붙는다.

7. Rainbow Robotics / Samsung은 Stage2 strategic control이다.
   전략지분만으로 revenue가 아니다. order/deployment가 필요하다.

8. Samsung / FlaktGroup은 data-center cooling Stage2지만 price-muted다.
   좋은 M&A라도 market이 +0.7%만 인정하면 Green을 주면 안 된다.
```

한 문장으로 압축하면:

> **R1 Loop 16에서 배운 핵심은 “수주·합병·전력기기·조선 headline”이 아니라, signed contract value, backlog relevance, market-relative strength, capacity, delivery margin, cash collection, integration synergy가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 전략지분, M&A, 조선 merger, transformer shortage narrative, geopolitical optionality만으로는 4B/false positive가 되기 쉽다.**

[1]: https://www.reuters.com/markets/commodities/aramco-awards-77-bln-contracts-fadhili-gas-expansion-2024-04-02/?utm_source=chatgpt.com "Aramco awards $7.7 bln in contracts for Fadhili gas expansion"
[2]: https://www.marketwatch.com/story/ls-electric-could-gain-from-solid-u-s-business-growth-opportunity-market-talk-3e926067?utm_source=chatgpt.com "LS Electric Could Gain From Solid U.S. Business Growth Opportunity -- Market Talk"
[3]: https://www.reuters.com/business/energy/us-power-transformer-buyers-scramble-imports-factory-slots--reeii-2026-05-11/?utm_source=chatgpt.com "US power transformer buyers scramble for imports, factory slots"
[4]: https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/?utm_source=chatgpt.com "South Korean shipbuilder HD Hyundai Heavy to merge with affiliate HD Hyundai Mipo"
[5]: https://www.wsj.com/articles/south-korean-shipbuilders-rally-on-brisk-contract-wins-d44ecb8a?utm_source=chatgpt.com "South Korean Shipbuilders Rally on Brisk Contract Wins"
[6]: https://www.reuters.com/business/retail-consumer/samsung-heavy-says-354-billion-icebreaker-orders-russias-zvezda-cancelled-2025-06-18/?utm_source=chatgpt.com "Samsung Heavy says $3.54 billion icebreaker orders from Russia's Zvezda cancelled"
[7]: https://www.reuters.com/world/asia-pacific/china-takes-steps-against-us-linked-units-skorea-shipbuilder-hanwha-2025-10-14/?utm_source=chatgpt.com "China takes steps against US-linked units of S.Korea shipbuilder Hanwha"
[8]: https://www.reuters.com/technology/samsung-electronics-becomes-largest-shareholder-south-koreas-rainbow-robotics-2024-12-30/?utm_source=chatgpt.com "Samsung Electronics becomes largest shareholder of South Korea's Rainbow Robotics"
[9]: https://www.reuters.com/markets/deals/samsung-electronics-buy-flktgroup-15-bln-euro-2025-05-13/?utm_source=chatgpt.com "Samsung to buy German cooling system maker FlaktGroup for $1.7 billion"

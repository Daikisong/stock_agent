순서상 이번은 **R1 Loop 17 — 산업재·수주·인프라 trigger-level price validation 라운드**다.

이번 R1은 **전력기기·조선·방산형 산업재·원전/SMR 장비·대형 EPC·수주 취소**를 한 묶음으로 본다. 핵심은 단순히 “수주가 크다”가 아니라, **계약금액 → 수주잔고 → 생산능력 → 납기 → 마진 → 현금흐름 → 증자/관세/제재/취소 리스크**까지 닫히는지다.

```text
round = R1 Loop 17
round_id = round_250
large_sector = INDUSTRIALS_ORDERS_INFRASTRUCTURE
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R2 Loop 17
```

중요하게 먼저 말하면, 이번에도 현재 도구 환경에서 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 원본을 안정적으로 직접 열지 못했다. 그래서 **MFE_30D/90D/180D/1Y/2Y와 MAE는 만들지 않는다.** 대신 Reuters/WSJ/MarketWatch의 **reported event return, event price, contract value, stock close/record-high context, cancellation/sanction trigger**를 가격 anchor로 쓴다. 이건 숫자를 꾸며내지 않기 위한 처리다.

---

# 1. 이번 라운드 대섹터

```text
R1 = 산업재·수주·인프라
```

R1의 core gate는 아래다.

```text
전력기기:
AI/data center 전력수요 → transformer/switchgear backlog → 미국 현지 생산능력 → 납기/가격 → margin → capex/원자재/관세 risk

조선:
naval/MASGA policy → MRO / shipyard capacity / merger → orderbook → labor/dock capacity → margin → China sanction / US law risk

방산형 산업재:
수출계약 → 현지생산/기술이전 → 납기 → 수익성 → 추가 주문 → 정치/환율/증자 risk

원전/SMR 장비:
preferred bidder / MOU → final contract → equipment workshare → 제작 capacity → legal/funding → margin

EPC/플랜트:
contract value → gross margin → working capital → cost escalation → claim / delay risk

수주취소/제재:
contract cancellation / arbitration / sanctions → backlog quality impairment → cash collection → thesis break
```

---

# 2. 대상 canonical archetype

```text
SHIPBUILDING_MASGA_MERGER_STAGE2_ACTIONABLE
SHIPBUILDING_NAVAL_EXPORT_STAGE2_WITH_SANCTION_4B
DEFENSE_INDUSTRIAL_EXPORT_STAGE2_YELLOW
GRID_EQUIPMENT_AI_POWER_STAGE2_PROMOTE
GRID_EQUIPMENT_US_CAPACITY_STAGE2_WITH_PRICE_FAILED
TRANSFORMER_CAPACITY_EXPANSION_STAGE2_NO_PRICE
NUCLEAR_SMR_INDUSTRIAL_SUPPLY_STAGE2_WITH_FINAL_CONTRACT_GATE
SHIPBUILDING_ORDER_CANCELLATION_4C
```

---

# 3. deep sub-archetype

```text
HD Hyundai Heavy / HD Hyundai Mipo:
- HD Hyundai Heavy to merge with HD Hyundai Mipo.
- MASGA / U.S.-Korea shipbuilding cooperation / naval demand.
- HD Hyundai Heavy +11.3%, HD Hyundai Mipo +14.6%, both record highs.
- Stage2-Actionable, but integration ratio, U.S. law/Jones Act, actual naval orders remain 4B.

Hanwha Ocean:
- Trump says Hanwha will participate in new U.S. Navy frigate class.
- Hanwha Ocean +6% morning trade.
- China later sanctions five U.S.-linked Hanwha Ocean subsidiaries.
- Hanwha Ocean closed -5.8%, HD Hyundai Heavy -4.1%.
- Stage2 naval export optionality + geopolitical sanction 4B.

Hyundai Rotem:
- Poland signs second large K2 tank contract, 180 tanks, estimated $6.5B.
- 61 tanks to be produced in Poland.
- earlier WSJ event: Hyundai Rotem +9.3% to 41,300 won on Q1 earnings/export expectation.
- Stage2 to Stage3-Yellow candidate if delivery/margin/local-production execution confirm.

HD Hyundai Electric:
- Reuters hedge-fund AI theme: HD Hyundai Electric shares up 333% since January 2024, driven by AI/data-center power demand.
- Stage2_promote_candidate / missed_structural if model was too conservative.
- Green requires backlog, margin, U.S./Saudi ultra-high-voltage transformer share and capex execution.

LS Electric:
- Daiwa raised target to 280,000 won from 150,000 won; U.S. revenue expected to rise from below 5% in 2022 to around 20% in 2024.
- But shares were down 5.4% at 208,500 won on the note.
- evidence_good_but_price_failed; do not promote to Green on report alone.

Hyosung Heavy Industries / Hyosung HICO:
- U.S. transformer shortage; Reuters notes GSU demand up 274% since 2019 and average lead time 143 weeks.
- Hyosung HICO to spend $157M expanding Memphis transformer plant.
- Stage2 capacity expansion, but no direct KRX price anchor.

Doosan Enerbility / SMR / U.S. AI infra:
- Korea-U.S. summit plans included KHNP/Doosan with X-energy/AWS on SMR design, construction and supply chain.
- Doosan also agreed with Fermi America to supply nuclear/SMR equipment for a Texas AI project.
- Stage2 nuclear-industrial supply, but MOU/final contract/workshare/margin gate remains.

Samsung Heavy Industries / Zvezda cancellation:
- Samsung Heavy cancelled two Russia Zvezda icebreaker ship orders worth 4.85T won / $3.54B.
- contracts for 10 icebreaker LNG carriers and 7 icebreaker shuttle tankers were terminated after prolonged war-related uncertainty.
- order cancellation / arbitration 4C-watch.
```

---

# 4. 선정 case 요약

| bucket                                 | case                                        | 핵심 판정                                                                    |
| -------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------ |
| structural_success / Stage2-Actionable | HD Hyundai Heavy + Mipo merger              | +11.3% / +14.6%, record highs, MASGA naval cooperation                   |
| Stage2 + 4B                            | Hanwha Ocean U.S. frigate + China sanctions | +6% on U.S. frigate comment, later -5.8% on China sanctions              |
| Stage3-Yellow candidate                | Hyundai Rotem K2 Poland                     | $6.5B second Poland contract, prior +9.3% export-earnings rally          |
| Stage2_promote_candidate               | HD Hyundai Electric AI power                | +333% since Jan 2024 context; likely missed_structural if Stage2 ignored |
| evidence_good_but_price_failed         | LS Electric U.S. data-center opportunity    | target +87%, U.S. revenue share expected 20%, but shares -5.4%           |
| Stage2 no-price                        | Hyosung Heavy / U.S. transformer capacity   | U.S. GSU demand +274%, lead time 143 weeks, Hyosung HICO $157M expansion |
| Stage2 with final-contract gate        | Doosan Enerbility SMR / AWS / Fermi         | Korea-U.S. SMR supply-chain cooperation; MOU/order conversion needed     |
| 4C-thesis-break                        | Samsung Heavy Zvezda cancellation           | 4.85T won / $3.54B order cancellation, arbitration/damages path          |

---

# 5. 각 case별 trigger grid

## Case A — HD Hyundai Heavy Industries / HD Hyundai Mipo MASGA merger

```text
symbols = 329180 / 010620
case_type = Stage2-Actionable shipbuilding consolidation
archetype = SHIPBUILDING_MASGA_MERGER_STAGE2_ACTIONABLE
```

| trigger |              type | date                   | 당시 공개 evidence                                                                           | 가격 anchor                                     | outcome |
| ------- | ----------------: | ---------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------- | ------- |
| T0      |            Stage1 | 2025-08 summit context | U.S.-Korea shipbuilding cooperation / MASGA theme                                        | no entry                                      |         |
| T1      | Stage2-Actionable | 2025-08-27             | HD Hyundai Heavy to merge with HD Hyundai Mipo to target U.S. shipbuilding/naval demand  | HD HHI +11.3%, Mipo +14.6%, both record highs |         |
| T2      |        validation | 2025-08-27             | exchange ratio 1 Mipo share per 1.04059146 HD HHI shares; merged company planned for Dec | same                                          |         |
| T3      |          4B-watch | 2025~2026              | U.S. naval order timing, Jones Act/U.S. law, integration, labor/dock capacity            | no OHLC                                       |         |
| T4      |     Stage3-Yellow | N/A                    | actual U.S. shipyard/order/workshare/margin not confirmed                                | 보류                                            |         |

HD Hyundai Heavy/Mipo는 R1 Loop 17의 가장 좋은 Stage2-Actionable이다. 단순 shipbuilding sentiment가 아니라, 미국 조선 재건/MASGA와 연결된 구조조정·합병 trigger였고, 발표 전후로 HD Hyundai Heavy가 +11.3%, HD Hyundai Mipo가 +14.6% 오르며 둘 다 record high로 마감했다. Reuters는 이 합병이 U.S.-Korea shipbuilding cooperation과 naval power demand를 겨냥한 것이라고 설명했다. 다만 실제 미국 함정·상선 수주, U.S. legal constraint, 통합 후 margin은 아직 닫히지 않았다. ([Reuters][1])

```json
{
  "case_id": "r1_loop17_hd_hyundai_heavy_mipo_masga",
  "symbols": "329180/010620",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_shipbuilding_consolidation",
  "trigger_date": "2025-08-27",
  "hd_hyundai_heavy_event_return_pct": 11.3,
  "hd_hyundai_mipo_event_return_pct": 14.6,
  "record_high": true,
  "exchange_ratio": "1_HD_Hyundai_Mipo_for_1.04059146_HD_Hyundai_Heavy",
  "strategic_context": "MASGA_US_Korea_shipbuilding_cooperation",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "actual_US_naval_orders",
    "US_shipyard_workshare",
    "Jones_Act_or_US_law_resolution",
    "post_merger_margin",
    "dock_labor_capacity"
  ],
  "trigger_outcome_label": "excellent_stage2_actionable_shipbuilding_consolidation"
}
```

---

## Case B — Hanwha Ocean / U.S. naval optionality + China sanctions

```text
symbol = 042660
case_type = Stage2 naval export optionality + geopolitical 4B
archetype = SHIPBUILDING_NAVAL_EXPORT_STAGE2_WITH_SANCTION_4B
```

| trigger |              type | date       | 당시 공개 evidence                                                                           | 가격 anchor                                                | outcome |
| ------- | ----------------: | ---------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------- |
| T0      |            Stage2 | 2025-12-23 | Trump says Hanwha will participate in new U.S. Navy frigate class                        | Hanwha Ocean +6% morning                                 |         |
| T1      |        validation | 2025       | Hanwha acquired Philly Shipyard for $100M, pledged $5B expansion, U.S. Navy MRO exposure | no direct OHLC                                           |         |
| T2      | 4B / geopolitical | 2025-10-14 | China sanctions five U.S.-linked Hanwha Ocean subsidiaries                               | Hanwha Ocean -5.8%, HD HHI -4.1%; FT says as much as -8% |         |
| T3      |     Stage3-Yellow | N/A        | actual U.S. Navy contract value, margin, China impact not resolved                       | 보류                                                       |         |

Hanwha Ocean은 R1에서 “좋은 산업재 optionality도 geopolitical 4B를 바로 맞을 수 있다”는 case다. U.S. Navy frigate 참여 코멘트에 Hanwha Ocean은 +6% 올랐지만, 중국이 Hanwha Ocean의 U.S.-linked subsidiaries 5곳에 제재를 걸자 Hanwha Ocean은 -5.8%, HD Hyundai Heavy는 -4.1% 하락했다. AP/Reuters는 Hanwha가 Philly Shipyard를 $100M에 인수했고, U.S. shipbuilding infrastructure에 $5B 투자를 약속했으며, U.S. Navy MRO 계약도 확보했다고 보도했다. 따라서 Stage2는 맞지만, China sanction 4B를 반드시 붙인다. ([Reuters][2])

```json
{
  "case_id": "r1_loop17_hanwha_ocean_us_navy_china_sanction",
  "symbol": "042660",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_naval_optionality_with_geopolitical_4B",
  "frigate_trigger_date": "2025-12-23",
  "frigate_event_return_pct": 6,
  "china_sanction_date": "2025-10-14",
  "china_sanction_event_return_pct": -5.8,
  "hd_hyundai_heavy_same_context_return_pct": -4.1,
  "ft_intraday_context_pct": -8,
  "philly_shipyard_acquisition_usd_mn": 100,
  "philly_expansion_pledge_usd_bn": 5,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "formal_US_Navy_contract_value",
    "margin",
    "delivery_schedule",
    "China_sanction_resolution",
    "US_shipyard_capacity"
  ],
  "trigger_outcome_label": "Stage2_naval_optional_with_geopolitical_4B"
}
```

---

## Case C — Hyundai Rotem / K2 Poland second contract

```text
symbol = 064350
case_type = Stage2 export → Stage3-Yellow candidate
archetype = DEFENSE_INDUSTRIAL_EXPORT_STAGE2_YELLOW
```

| trigger |                    type | date       | 당시 공개 evidence                                                             | 가격 anchor                                      | outcome |
| ------- | ----------------------: | ---------- | -------------------------------------------------------------------------- | ---------------------------------------------- | ------- |
| T0      |  Stage2 earnings/export | 2024-04-09 | K2 exports to Poland expected to drive Q1 earnings beat                    | Hyundai Rotem +9.3% to 41,300 won, KOSPI -0.3% |         |
| T1      |         Stage2 evidence | 2025-07-02 | Poland completes negotiations for second batch K2 tanks, estimated $6.5B   | no direct price anchor                         |         |
| T2      |       Stage2 validation | 2025-08-01 | Poland signs second major contract, 180 tanks; 61 to be produced in Poland | no price in source                             |         |
| T3      | Stage3-Yellow candidate | 2025~2026  | repeat Poland order + local production + delivery/service package          | margin/delivery missing                        |         |
| T4      |                4B-watch | 2025~2030  | Polish local production, technology transfer, schedule, margin dilution    | no OHLC                                        |         |

Hyundai Rotem은 R1의 defense-industrial export Yellow 후보로 본다. 2024년에는 K2 Poland shipment가 earnings beat를 만들 것이라는 기대에 주가가 +9.3%로 41,300원까지 올랐고, KOSPI는 -0.3%였다. 2025년에는 Poland가 두 번째 K2 batch 계약을 체결했으며, 180 tanks, 추정 $6.5B 규모이고 61대는 Poland Bumar-Labedny plant에서 생산될 예정이다. 이건 단발 수주가 아니라 repeat order + local production footprint로 올라간다. 다만 margin, 기술이전 cost, 현지생산 execution이 Green gate다. ([월스트리트저널][3])

```json
{
  "case_id": "r1_loop17_hyundai_rotem_k2_poland",
  "symbol": "064350",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage3-Yellow_candidate_defense_industrial_export",
  "earnings_trigger_date": "2024-04-09",
  "earnings_event_return_pct": 9.3,
  "earnings_event_price_krw": 41300,
  "kospi_same_context_pct": -0.3,
  "poland_second_contract_date": "2025-08-01",
  "contract_value_estimate_usd_bn": 6.5,
  "tank_count": 180,
  "poland_local_production_count": 61,
  "first_deliveries_planned": 2026,
  "local_production_period": "2028-2030",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "delivery_margin",
    "local_production_cost",
    "technology_transfer_cost",
    "working_capital",
    "service_package_margin"
  ],
  "trigger_outcome_label": "Stage3_Yellow_candidate_repeat_export"
}
```

---

## Case D — HD Hyundai Electric / AI power-demand transformer cycle

```text
symbol = 267260
case_type = Stage2_promote_candidate / missed_structural risk
archetype = GRID_EQUIPMENT_AI_POWER_STAGE2_PROMOTE
```

| trigger |            type | date       | 당시 공개 evidence                                                                                             | 가격 anchor                                 | outcome |
| ------- | --------------: | ---------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------- |
| T0      |       awareness | 2024H1     | AI/data-center electricity demand broadens from chips to power equipment                                   | no single trigger                         |         |
| T1      | Stage2 evidence | 2024-07-11 | hedge funds broaden Korea AI exposure into electricity equipment; HD Hyundai Electric cited as beneficiary | Reuters says shares up 333% since January |         |
| T2      |      validation | 2025~2026  | Korean second-tier energy/industrial stocks become AI power-chain beneficiaries                            | broad market context                      |         |
| T3      |   Stage3-Yellow | N/A        | backlog, U.S./Saudi market share, transformer ASP, margin not individually validated                       | 보류                                        |         |
| T4      |        4B-watch | 2025~      | capex, lead-time normalization, copper/steel input, overheat                                               | no OHLC                                   |         |

HD Hyundai Electric은 이번 R1에서 “Stage2를 너무 보수적으로 두면 놓치는 구조적 case”로 분류한다. Reuters는 2024년 7월, AI theme가 chipmakers에서 전력장비로 확장되고 있으며 CloudAlpha가 HD Hyundai Electric에 투자했고, 주가가 January 이후 +333% 올랐다고 보도했다. MarketWatch도 2026년 Korea rally에서 HD Hyundai Electric, Hyosung Heavy, LS Electric 같은 energy/industrial names가 AI data-center 전력 인프라 value chain으로 주목받는다고 설명했다. 다만 이 경우는 event-date 하나보다 cycle-entry 문제라서, Green은 backlog/margin/수주잔고로 확인해야 한다. ([Reuters][4])

```json
{
  "case_id": "r1_loop17_hd_hyundai_electric_ai_power",
  "symbol": "267260",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_promote_candidate_grid_equipment",
  "trigger_reference_date": "2024-07-11",
  "reported_share_return_since_jan_2024_pct": 333,
  "theme": "AI_data_center_power_demand",
  "evidence_source_type": "reported_broad_AI_power_chain_investor_flow",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "new_order_backlog",
    "transformer_ASP",
    "US_market_share",
    "Saudi_market_share",
    "operating_margin",
    "capacity_expansion_ROI"
  ],
  "trigger_outcome_label": "missed_structural_if_stage2_ignored"
}
```

---

## Case E — LS Electric / U.S. data-center power opportunity but price failed

```text
symbol = 010120
case_type = evidence_good_but_price_failed
archetype = GRID_EQUIPMENT_US_CAPACITY_STAGE2_WITH_PRICE_FAILED
```

| trigger |            type | date       | 당시 공개 evidence                                                                                                        | 가격 anchor                   | outcome |
| ------- | --------------: | ---------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------- | ------- |
| T0      | Stage2 evidence | 2024-07-01 | Daiwa raises target to 280,000 won from 150,000 won; U.S. revenue share may rise to 20% in 2024 from below 5% in 2022 | shares -5.4% at 208,500 won |         |
| T1      |      validation | 2024-07-01 | demand from data centers, renewables, EV value chain; revenue forecasts raised 4~22%                                  | price failed                |         |
| T2      |        4B-watch | 2024~      | report-driven rerating, order/margin not closed, price reaction negative                                              | 4B                          |         |
| T3      |   Stage3-Yellow | N/A        | actual U.S. order conversion and margin required                                                                      | 보류                          |         |

LS Electric은 RedTeam 관점에서 중요하다. evidence는 좋아 보인다. Daiwa는 target price를 150,000원에서 280,000원으로 87% 올렸고, U.S. revenue share가 2022년 5% 미만에서 2024년 약 20%로 늘 수 있다고 봤다. 그런데 같은 MarketWatch/WSJ market-talk 보도에서 주가는 -5.4%, 208,500원이었다. 즉 **좋은 리포트가 좋은 entry라는 보장은 없다.** 이건 `evidence_good_but_price_failed`로 둬야 한다. ([마켓워치][5])

```json
{
  "case_id": "r1_loop17_ls_electric_us_data_center_price_failed",
  "symbol": "010120",
  "best_trigger": "T0/T2",
  "best_trigger_type": "evidence_good_but_price_failed",
  "trigger_date": "2024-07-01",
  "target_price_old_krw": 150000,
  "target_price_new_krw": 280000,
  "target_price_raise_pct": 87,
  "reported_event_price_krw": 208500,
  "reported_event_return_pct": -5.4,
  "us_revenue_share_2022_context_pct": "<5",
  "us_revenue_share_2024_expected_pct": 20,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "actual_US_orders",
    "backlog",
    "margin",
    "data_center_customer_disclosure",
    "capacity_ROI"
  ],
  "trigger_outcome_label": "evidence_good_but_price_failed"
}
```

---

## Case F — Hyosung Heavy Industries / U.S. transformer capacity

```text
symbol = 298040
case_type = Stage2 capacity expansion without direct price anchor
archetype = TRANSFORMER_CAPACITY_EXPANSION_STAGE2_NO_PRICE
```

| trigger |                     type | date               | 당시 공개 evidence                                                                            | 가격 anchor    | outcome |
| ------- | -----------------------: | ------------------ | ----------------------------------------------------------------------------------------- | ------------ | ------- |
| T0      | Stage2 industry evidence | 2025-12-02         | U.S. grid equipment shortage; GSU demand +274% since 2019, average lead time 143 weeks    | no KRX price |         |
| T1      |  Stage2 company evidence | 2025-11-12 context | Hyosung HICO to spend $157M expanding Memphis transformer plant                           | no KRX price |         |
| T2      |               validation | 2025~2030          | transformer shortages expected to ease by 2030 as investment closes gap                   | no price     |         |
| T3      |                 4B-watch | 2025~              | capex execution, U.S. demand durability, tariff/material cost, overcapacity normalization | no OHLC      |         |
| T4      |            Stage3-Yellow | N/A                | orderbook/margin/capacity utilization not confirmed                                       | 보류           |         |

Hyosung Heavy는 R1에서 HD Hyundai Electric보다 덜 검증된 transformer capacity case로 넣는다. Reuters Events는 U.S. generation step-up transformer demand가 2019년 이후 +274% 늘었고, 평균 lead time이 143주라고 보도했다. 같은 기사에서 Hyosung HICO는 Memphis transformer plant expansion에 $157M를 투자한다고 나온다. 이는 Stage2 capacity evidence다. 그러나 직접 KRX price anchor, orderbook, margin, utilization이 없으므로 Yellow로 올리지 않는다. ([Reuters][6])

```json
{
  "case_id": "r1_loop17_hyosung_heavy_us_transformer_capacity",
  "symbol": "298040",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_transformer_capacity_no_price",
  "industry_reference_date": "2025-12-02",
  "gsu_demand_increase_since_2019_pct": 274,
  "average_lead_time_weeks": 143,
  "hyosung_hico_memphis_expansion_usd_mn": 157,
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "specific_orderbook",
    "capacity_utilization",
    "US_customer_contracts",
    "margin",
    "capex_ROI",
    "supply_shortage_duration"
  ],
  "trigger_outcome_label": "Stage2_capacity_expansion_not_Green"
}
```

---

## Case G — Doosan Enerbility / SMR and U.S. AI infrastructure supply chain

```text
symbol = 034020
case_type = Stage2 nuclear-industrial supply with final-contract gate
archetype = NUCLEAR_SMR_INDUSTRIAL_SUPPLY_STAGE2_WITH_FINAL_CONTRACT_GATE
```

| trigger |                     type | date       | 당시 공개 evidence                                                                              | 가격 anchor              | outcome |
| ------- | -----------------------: | ---------- | ------------------------------------------------------------------------------------------- | ---------------------- | ------- |
| T0      | Stage2 policy/industrial | 2025-08-26 | Korea-U.S. summit: KHNP/Doosan with X-energy/AWS on SMR design, construction, supply chains | no direct Doosan price |         |
| T1      |               validation | 2025-08-26 | Doosan agreement with Fermi America to supply nuclear/SMR equipment for Texas AI project    | no price               |         |
| T2      |                 4B-watch | 2025~      | MOU vs final contract, equipment workshare, financing, licensing, margin                    | 4B                     |         |
| T3      |            Stage3-Yellow | N/A        | final equipment order and margin not confirmed                                              | 보류                     |         |

Doosan Enerbility는 R1의 nuclear-industrial supply-chain Stage2다. Reuters는 Korea-U.S. summit에서 KHNP와 Doosan Enerbility가 X-energy/AWS와 SMR design, construction, supply-chain cooperation을 추진하고, Doosan이 Fermi America의 Texas AI project에 nuclear/SMR equipment를 공급하는 agreement를 맺었다고 보도했다. 핵심은 “AI power + nuclear equipment” 연결이다. 그러나 MOU/협력은 최종 장비 수주가 아니고, licensing/financing/workshare/margin이 닫혀야 Yellow다. ([Reuters][7])

```json
{
  "case_id": "r1_loop17_doosan_enerbility_smr_ai_power",
  "symbol": "034020",
  "best_trigger": "T0/T2",
  "best_trigger_type": "Stage2_nuclear_SMR_industrial_supply",
  "trigger_date": "2025-08-26",
  "counterparties": [
    "KHNP",
    "X-energy",
    "Amazon_Web_Services",
    "Fermi_America"
  ],
  "project_context": "Texas_AI_project_nuclear_SMR_equipment",
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "final_equipment_contract",
    "equipment_workshare",
    "licensing",
    "project_financing",
    "margin",
    "delivery_schedule"
  ],
  "trigger_outcome_label": "Stage2_SMR_supply_chain_not_Green"
}
```

---

## Case H — Samsung Heavy Industries / Zvezda icebreaker order cancellation

```text
symbol = 010140
case_type = 4C order cancellation / thesis break
archetype = SHIPBUILDING_ORDER_CANCELLATION_4C
```

| trigger |            type | date       | 당시 공개 evidence                                                                                 | 가격 anchor       | outcome |
| ------- | --------------: | ---------- | ---------------------------------------------------------------------------------------------- | --------------- | ------- |
| T0      |      old Stage2 | 2020~2021  | Samsung Heavy won icebreaker LNG/shuttle tanker work for Russia Zvezda                         | old orderbook   |         |
| T1      |      4C trigger | 2025-06-18 | Samsung Heavy cancels two Zvezda orders worth 4.85T won / $3.54B                               | no direct price |         |
| T2      |      validation | 2025-06-18 | contracts covered parts/blocks for 10 icebreaker LNG carriers and 7 icebreaker shuttle tankers | no price        |         |
| T3      |       4B/relief | 2025~      | Singapore arbitration / damages claim, advance-payment dispute                                 | no OHLC         |         |
| T4      | Stage3 recovery | N/A        | damages recovery and order replacement not confirmed                                           | 보류              |         |

Samsung Heavy Industries는 R1에서 꼭 넣어야 하는 order-quality 4C다. 수주는 숫자로 볼 때 좋았지만, Reuters에 따르면 Zvezda 관련 4.85T won, $3.54B 규모의 2개 icebreaker order가 취소됐다. 계약은 10척 icebreaker LNG carriers와 7척 icebreaker shuttle tankers 관련 parts/blocks였고, Samsung Heavy는 Zvezda가 불법적으로 termination을 통보했다며 arbitration and damages path를 택했다. 이 case는 “수주잔고 숫자만 보고 Green을 주면 안 된다”는 반례다. ([Reuters][8])

```json
{
  "case_id": "r1_loop17_samsung_heavy_zvezda_cancellation",
  "symbol": "010140",
  "best_trigger": "T1/T3",
  "best_trigger_type": "4C_order_cancellation",
  "trigger_date": "2025-06-18",
  "cancelled_order_value_krw_trn": 4.85,
  "cancelled_order_value_usd_bn": 3.54,
  "original_order_period": "2020-2021",
  "vessel_scope": [
    "10_icebreaker_LNG_carriers",
    "7_icebreaker_shuttle_tankers"
  ],
  "dispute_context": [
    "illegal_termination_by_shipowner",
    "advance_payment_return_demand",
    "Singapore_arbitration",
    "war_related_uncertainty"
  ],
  "direct_price_anchor": "price_data_unavailable_after_deep_search",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_recovery_gate_missing": [
    "damages_recovery",
    "replacement_orders",
    "cash_collection",
    "arbitration_outcome",
    "backlog_quality_rebuild"
  ],
  "trigger_outcome_label": "order_cancellation_4C_thesis_break"
}
```

---

# 6. Trigger별 실제 가격경로 검증 요약

이번 R1 Loop 17은 full OHLC가 없으므로, 아래 표는 **reported event anchor 기준**이다.

| case                  | best trigger |              entry anchor |                       event return / price |                    market-relative | full MFE/MAE | outcome                            |
| --------------------- | ------------ | ------------------------: | -----------------------------------------: | ---------------------------------: | ------------ | ---------------------------------- |
| HD Hyundai Heavy/Mipo | T1           | record-high close context |                            +11.3% / +14.6% |                        unavailable | unavailable  | excellent Stage2-Actionable        |
| Hanwha Ocean          | T0/T2        |                     event |    +6% on frigate, -5.8% on China sanction | HD HHI -4.1% same sanction context | unavailable  | Stage2 + geopolitical 4B           |
| Hyundai Rotem         | T0/T2        |   41,300 won on WSJ event |   +9.3%, KOSPI -0.3%; later $6.5B contract |                       +9.6pp on T0 | unavailable  | Yellow candidate                   |
| HD Hyundai Electric   | T1           |     broad reported return |                       +333% since Jan 2024 |                        unavailable | unavailable  | missed_structural / Stage2 promote |
| LS Electric           | T0           |               208,500 won |                  -5.4% despite target hike |                        unavailable | unavailable  | evidence_good_but_price_failed     |
| Hyosung Heavy         | T0/T1        |            no stock price | industry demand +274%, lead time 143 weeks |                                N/A | unavailable  | Stage2 no-price                    |
| Doosan Enerbility     | T0/T1        |            no stock price |                  SMR/AWS/Fermi cooperation |                                N/A | unavailable  | Stage2 with final-contract gate    |
| Samsung Heavy         | T1           |            no stock price |            4.85T won / $3.54B cancellation |                                N/A | unavailable  | 4C order cancellation              |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
가장 좋은 Stage2:
1. HD Hyundai Heavy / Mipo MASGA merger
2. Hyundai Rotem K2 Poland earnings/export trigger
3. Hanwha Ocean U.S. naval optionality
4. HD Hyundai Electric AI power-chain cycle
5. Samsung Heavy old orderbook 반례: cancellation으로 4C 전환
```

## Stage2-Actionable entry 성과

```text
Stage2-Actionable:
- HD Hyundai Heavy / Mipo: event return +11.3%/+14.6%.
- Hyundai Rotem: +9.3% on export-earnings expectation, repeat Poland contract.
- Hanwha Ocean: +6% on U.S. frigate optionality, but China sanction 4B.

Actionable 보류:
- HD Hyundai Electric: +333% broad move is strong, but trigger date/window not clean.
- Hyosung Heavy: industry/capacity evidence strong, direct KRX price unavailable.
- Doosan Enerbility: SMR cooperation, final order/workshare missing.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- Hyundai Rotem: repeat export + local production + service package.
- HD Hyundai Electric: if backlog/margin/capacity confirm.
- HD Hyundai Heavy: if U.S. shipbuilding orders and integration margin confirm.
- Hanwha Ocean: if formal U.S. Navy contract and China sanction impact resolve.
```

## Stage3-Green

```text
이번 R1 Loop 17에서 확정 Green 없음.

이유:
- 조선/MASGA는 강하지만 actual U.S. order and margin이 없다.
- 전력기기는 구조적 수요는 강하지만 backlog/margin/capacity utilization이 필요하다.
- Hyundai Rotem은 Yellow 후보지만 local production/margin gate가 있다.
- Doosan SMR은 MOU/협력 단계다.
- Samsung Heavy는 order cancellation 4C다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- HD Hyundai Heavy / Mipo merger
- Hyundai Rotem K2 Poland export cycle
- Hanwha Ocean U.S. naval optionality + China sanction 4B
- LS Electric price-failed evidence
- Samsung Heavy order cancellation 4C

Stage2_promote_candidate:
- HD Hyundai Heavy / Mipo
- Hyundai Rotem
- HD Hyundai Electric
- Hanwha Ocean, with China sanction 4B
- Hyosung Heavy, after direct price/orderbook validation

Stage3-Yellow candidate:
- Hyundai Rotem
- HD Hyundai Electric
- HD Hyundai Heavy / Mipo
- Hanwha Ocean after formal contract/sanction resolution

false_positive_score:
- LS Electric을 리포트만 보고 Green으로 올리는 경우
- Doosan SMR을 MOU만 보고 Green으로 올리는 경우
- Hyosung Heavy를 capacity headline만 보고 Green으로 올리는 경우

evidence_good_but_price_failed:
- LS Electric

price_moved_without_clean_trigger:
- HD Hyundai Electric broad +333% cycle; exact trigger-level OHLC unavailable

thesis_break:
- Samsung Heavy / Zvezda cancellation

4B-watch:
- Hanwha Ocean China sanctions
- HD Hyundai Heavy/Mipo integration/Jones Act/U.S. law
- Hyundai Rotem local production/technology transfer
- transformer capacity overbuild / input cost
- SMR final-contract/licensing risk

hard_4C_success:
- Samsung Heavy order cancellation is 4C-watch/thesis break, but full price-path hard 4C cannot be confirmed without OHLC
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
reported_event_return,+5,"+5% 이상 event return은 Stage2-Actionable 후보","HD Hyundai Heavy, Mipo, Hyundai Rotem, Hanwha Ocean"
market_relative_return,+5,"시장 대비 초과수익은 trigger quality 핵심","Hyundai Rotem, Samsung E&A-type benchmark"
contract_value_visibility,+5,"수주/계약금액이 명확하면 headline보다 강한 evidence","Hyundai Rotem, Samsung Heavy cancellation"
naval_shipbuilding_us_workshare,+5,"MASGA/U.S. naval theme는 실제 workshare 확인 시 승격","HD Hyundai Heavy, Hanwha Ocean"
grid_equipment_backlog,+5,"AI 전력기기는 backlog와 transformer ASP가 핵심","HD Hyundai Electric, LS Electric, Hyosung Heavy"
capacity_utilization,+4,"capacity expansion은 utilization 전에는 Stage2","Hyosung Heavy, HD Hyundai Electric"
repeat_export_operator,+4,"반복 수출/현지생산 footprint는 Yellow 후보","Hyundai Rotem"
order_quality_risk,+5,"수주 취소/제재/중재는 backlog quality hard gate","Samsung Heavy, Hanwha Ocean"
```

## 내릴 축

```csv
axis,delta,reason,cases
theme_label_without_orders,-5,"AI/data-center/SMR theme만으로 Green 금지","LS Electric, Doosan"
report_upgrade_without_price_validation,-5,"목표가 상향에도 주가가 하락하면 Actionable 금지","LS Electric"
capacity_headline_without_utilization,-4,"공장 증설만으로 Stage3 금지","Hyosung Heavy"
MOU_without_final_contract,-5,"SMR/MOU는 final contract 전까지 Stage2","Doosan Enerbility"
shipbuilding_policy_without_orders,-4,"MASGA policy는 실제 order/workshare 전까지 Stage2","HD Hyundai Heavy, Hanwha Ocean"
geopolitical_sanction_ignored,-5,"China sanction 같은 4B를 무시하면 false positive","Hanwha Ocean"
orderbook_without_cancellation_check,-5,"수주잔고 숫자만 보고 cancellation risk 무시 금지","Samsung Heavy"
local_production_without_margin,-4,"현지생산/기술이전은 margin 확인 전 4B","Hyundai Rotem"
```

---

# 10. Stage2-Actionable 승격 조건

R1 Loop 17 shadow rule:

```text
R1에서 Stage2 evidence가 아래 중 4개 이상이면 Stage2-Actionable로 승격한다.

1. event return +5% 이상
2. market-relative return +5pp 이상
3. contract/deal/order value가 명확하다
4. 수주가 매출/수주잔고로 직접 연결된다
5. 반복 수주 또는 신규 market entry가 있다
6. 생산능력/현지화가 고객 수요와 직접 연결된다
7. sanction, cancellation, MOU-only, margin unknown 4B가 없다
```

적용:

```text
HD Hyundai Heavy/Mipo:
1,3,5 일부 충족. 7은 아직 U.S. legal/workshare 4B → Stage2-Actionable.

Hyundai Rotem:
1,2,3,4,5 충족. 7은 local production/margin 4B → Stage3-Yellow candidate.

HD Hyundai Electric:
1은 broad-cycle 기준 충족, 3/4는 직접 확인 부족 → Stage2_promote_candidate.

LS Electric:
evidence는 좋지만 event return이 -5.4% → Actionable 금지.

Hyosung Heavy:
6은 충족, direct price/orderbook 부족 → Stage2.

Doosan:
MOU/final contract gate 때문에 Stage2 only.

Samsung Heavy:
cancellation 4C, 승격 금지.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
- Stage2-Actionable 이후 EPS/OP/FCF 경로 변화 가능성이 높아졌지만,
  margin, capacity, delivery, sanction, final contract 중 하나가 남은 상태.
```

Yellow 후보:

```text
Hyundai Rotem:
repeat K2 export + Poland local production + service package. Margin and delivery needed.

HD Hyundai Electric:
AI power transformer demand + broad +333% cycle. Backlog/margin/orderbook needed.

HD Hyundai Heavy/Mipo:
MASGA/naval demand + merger. Actual U.S. workshare and post-merger margin needed.

Hanwha Ocean:
U.S. Navy optionality. China sanction resolution and formal contract needed.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- contract/order value is final.
- backlog converts to profitable revenue.
- production capacity/utilization is visible.
- margin and cash conversion are confirmed.
- sanction/cancellation/MOU-only/legal risk is absent or resolved.
- full-window MFE/MAE is favorable.
```

이번 R1 Loop 17에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + margin/capacity/workshare/finality gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- shipbuilding policy rally before formal U.S. orders.
- China sanction after U.S.-linked naval optionality.
- transformer capacity expansion before utilization.
- target-price upgrade but stock falls.
- local production / technology transfer before margin.
- SMR MOU before final equipment contract.
- orderbook becomes cancellation/arbitration.
```

적용:

```text
HD Hyundai Heavy/Mipo:
MASGA rally, but actual U.S. orders and integration margin needed.

Hanwha Ocean:
U.S. naval optionality + China sanction 4B.

LS Electric:
target-price upgrade but stock down → price-failed 4B.

Hyosung Heavy:
capacity expansion but utilization/orderbook unavailable.

Hyundai Rotem:
local production/technology transfer 4B.

Doosan:
MOU/final-contract 4B.

Samsung Heavy:
order cancellation 4C.
```

---

# 14. 4C hard gate 조건

```text
R1 4C:
- major order cancellation
- arbitration / advance-payment dispute
- geopolitical sanction blocking operations
- final contract failure after preferred bidder/MOU
- large contract with negative margin/cash conversion
- capacity expansion followed by demand collapse
```

이번 R1 Loop 17 hard/strong 4C:

```text
Samsung Heavy / Zvezda cancellation = strong 4C thesis-break
Hanwha Ocean / China sanctions = 4B-to-4C watch
LS Electric price-failed report = false-positive prevention
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R1 production 설계 원칙:

```text
1. 수주 headline과 profitable backlog를 분리한다.
2. 조선 policy/MASGA와 실제 U.S. order/workshare를 분리한다.
3. AI power theme와 transformer backlog/margin을 분리한다.
4. 현지생산/기술이전은 margin 확인 전까지 4B로 둔다.
5. MOU/협력은 final contract 전까지 Stage2다.
6. 수주취소/제재/arbitration은 backlog quality 4C로 즉시 반영한다.
7. 리포트 목표가 상향에도 주가가 하락하면 Actionable 금지한다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_250.md 요약

```md
# R1 Loop 17. Industrials / Orders / Infrastructure Trigger-level Price Validation

이번 라운드는 R1 Loop 17 trigger-level validation 라운드다.

핵심 결론:
- HD Hyundai Heavy / HD Hyundai Mipo is the cleanest R1 Stage2-Actionable case. The merger targets U.S.-Korea shipbuilding cooperation and naval demand under MASGA. HD Hyundai Heavy rose 11.3% and HD Hyundai Mipo 14.6%, both closing at record highs. Green requires actual U.S. order/workshare, post-merger margin and U.S. legal clarity.
- Hanwha Ocean is Stage2 naval optionality with geopolitical 4B. Shares rose 6% after Trump comments on U.S. frigates, but later fell 5.8% after China sanctioned five U.S.-linked subsidiaries. China sanction risk must be attached to U.S.-linked shipbuilding optionality.
- Hyundai Rotem is Stage3-Yellow candidate. It rallied 9.3% to 41,300 won on K2 Poland export-driven earnings expectations, and Poland later signed a second K2 contract for 180 tanks, estimated around $6.5B, with 61 tanks to be produced locally.
- HD Hyundai Electric is Stage2_promote_candidate / missed_structural risk. Reuters reported its shares were up 333% since January 2024 as AI demand broadened into power equipment. Green requires backlog, margin and capacity utilization evidence.
- LS Electric is evidence_good_but_price_failed. Daiwa raised target to 280,000 won and saw U.S. revenue share rising to 20%, but shares were down 5.4% at 208,500 won on the note.
- Hyosung Heavy Industries is Stage2 capacity expansion without price validation. U.S. GSU transformer demand rose 274% since 2019 and lead times averaged 143 weeks; Hyosung HICO plans $157M Memphis expansion. Direct KRX price/orderbook unavailable.
- Doosan Enerbility is Stage2 SMR/AI-power industrial supply. KHNP/Doosan cooperation with X-energy/AWS and Fermi America links nuclear equipment to AI power demand, but final equipment contract/workshare/margin is missing.
- Samsung Heavy Industries is order-cancellation 4C. It cancelled 4.85T won / $3.54B Zvezda icebreaker orders, involving 10 icebreaker LNG carriers and 7 shuttle tankers, and pursued arbitration/damages.

Main calibration:
- Raise reported_event_return, market_relative_return, contract_value_visibility, naval_shipbuilding_us_workshare, grid_equipment_backlog, capacity_utilization, repeat_export_operator, order_quality_risk.
- Lower theme_label_without_orders, report_upgrade_without_price_validation, capacity_headline_without_utilization, MOU_without_final_contract, shipbuilding_policy_without_orders, geopolitical_sanction_ignored, orderbook_without_cancellation_check, local_production_without_margin.
```

## docs/checkpoints/checkpoint_28a_round250_r1_loop17.md 요약

```md
# Checkpoint 28A Round 250 R1 Loop 17 Trigger-level Calibration

## 반영 내용
- R1 Loop 17 trigger-level validation을 수행했다.
- HD Hyundai Heavy/Mipo MASGA merger, Hanwha Ocean U.S. naval optionality and China sanctions, Hyundai Rotem K2 Poland, HD Hyundai Electric AI power, LS Electric price-failed report, Hyosung Heavy transformer expansion, Doosan Enerbility SMR/AI power, Samsung Heavy Zvezda cancellation을 검토했다.
- full adjusted OHLC는 확보하지 못했으므로 Reuters/WSJ/MarketWatch reported event return과 event price anchor를 사용했다.
- MFE/MAE는 조작하지 않고 price_data_unavailable_after_deep_search로 분리했다.

## 핵심 보정
- Industrial order quality must be separated from contract headline size.
- Stage2-Actionable promotion requires reported event return, market-relative strength and contract/deal visibility.
- AI power equipment themes require backlog, ASP, margin and capacity utilization before Green.
- Shipbuilding policy/MASGA needs formal U.S. order/workshare before Yellow/Green.
- Sanctions, order cancellations, MOU-only contracts and price-failed analyst upgrades are 4B/4C gates.
```

## data/e2r_case_library/cases_r1_loop17_round250.jsonl 초안

```jsonl
{"case_id":"r1_loop17_hd_hyundai_heavy_mipo_masga","symbol":"329180/010620","company_name":"HD Hyundai Heavy Industries / HD Hyundai Mipo","case_type":"Stage2_Actionable_shipbuilding_consolidation","primary_archetype":"SHIPBUILDING_MASGA_MERGER_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2025-08-27","hd_hyundai_heavy_event_return_pct":11.3,"hd_hyundai_mipo_event_return_pct":14.6,"record_high":true,"exchange_ratio":"1_HD_Hyundai_Mipo_for_1.04059146_HD_Hyundai_Heavy","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable","notes":"MASGA-linked merger had strong event returns but needs actual U.S. orders/workshare and post-merger margin."}
{"case_id":"r1_loop17_hanwha_ocean_us_navy_china_sanction","symbol":"042660","company_name":"Hanwha Ocean","case_type":"Stage2_naval_optionality_with_geopolitical_4B","primary_archetype":"SHIPBUILDING_NAVAL_EXPORT_STAGE2_WITH_SANCTION_4B","best_trigger":"T0/T2","stage_candidate":"Stage2 + 4B-watch","price_validation":{"frigate_trigger_date":"2025-12-23","frigate_event_return_pct":6,"china_sanction_date":"2025-10-14","china_sanction_event_return_pct":-5.8,"hd_hyundai_heavy_same_context_return_pct":-4.1,"ft_intraday_context_pct":-8,"philly_shipyard_acquisition_usd_mn":100,"philly_expansion_pledge_usd_bn":5,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_with_geopolitical_4B","notes":"U.S. naval optionality is real but China sanction risk is a material 4B."}
{"case_id":"r1_loop17_hyundai_rotem_k2_poland","symbol":"064350","company_name":"Hyundai Rotem","case_type":"Stage3_Yellow_candidate_defense_industrial_export","primary_archetype":"DEFENSE_INDUSTRIAL_EXPORT_STAGE2_YELLOW","best_trigger":"T0/T2","stage_candidate":"Stage3-Yellow_candidate","price_validation":{"earnings_trigger_date":"2024-04-09","earnings_event_return_pct":9.3,"earnings_event_price_krw":41300,"kospi_same_context_pct":-0.3,"poland_second_contract_date":"2025-08-01","contract_value_estimate_usd_bn":6.5,"tank_count":180,"poland_local_production_count":61,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage3_Yellow_candidate","notes":"Repeat export and local production support Yellow candidate; margin and delivery execution are gates."}
{"case_id":"r1_loop17_hd_hyundai_electric_ai_power","symbol":"267260","company_name":"HD Hyundai Electric","case_type":"Stage2_promote_candidate_grid_equipment","primary_archetype":"GRID_EQUIPMENT_AI_POWER_STAGE2_PROMOTE","best_trigger":"T1/T2","stage_candidate":"Stage2_promote_candidate","price_validation":{"trigger_reference_date":"2024-07-11","reported_share_return_since_jan_2024_pct":333,"theme":"AI_data_center_power_demand","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"missed_structural_if_stage2_ignored","notes":"Broad AI power-equipment rally implies potential missed_structural if Stage2 too conservative; backlog/margin required."}
{"case_id":"r1_loop17_ls_electric_us_data_center_price_failed","symbol":"010120","company_name":"LS Electric","case_type":"evidence_good_but_price_failed","primary_archetype":"GRID_EQUIPMENT_US_CAPACITY_STAGE2_WITH_PRICE_FAILED","best_trigger":"T0/T2","stage_candidate":"Stage2_only","price_validation":{"trigger_date":"2024-07-01","target_price_old_krw":150000,"target_price_new_krw":280000,"target_price_raise_pct":87,"reported_event_price_krw":208500,"reported_event_return_pct":-5.4,"us_revenue_share_2024_expected_pct":20,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed","notes":"Target-price upgrade and U.S. growth evidence were good, but price reaction was negative."}
{"case_id":"r1_loop17_hyosung_heavy_us_transformer_capacity","symbol":"298040","company_name":"Hyosung Heavy Industries / Hyosung HICO","case_type":"Stage2_transformer_capacity_no_price","primary_archetype":"TRANSFORMER_CAPACITY_EXPANSION_STAGE2_NO_PRICE","best_trigger":"T0/T2","stage_candidate":"Stage2","price_validation":{"industry_reference_date":"2025-12-02","gsu_demand_increase_since_2019_pct":274,"average_lead_time_weeks":143,"hyosung_hico_memphis_expansion_usd_mn":157,"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2_no_price","notes":"Transformer shortage and U.S. capacity expansion are real, but direct price/orderbook/margin unavailable."}
{"case_id":"r1_loop17_doosan_enerbility_smr_ai_power","symbol":"034020","company_name":"Doosan Enerbility","case_type":"Stage2_nuclear_SMR_industrial_supply","primary_archetype":"NUCLEAR_SMR_INDUSTRIAL_SUPPLY_STAGE2_WITH_FINAL_CONTRACT_GATE","best_trigger":"T0/T2","stage_candidate":"Stage2","price_validation":{"trigger_date":"2025-08-26","counterparties":["KHNP","X-energy","Amazon_Web_Services","Fermi_America"],"project_context":"Texas_AI_project_nuclear_SMR_equipment","direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_not_Green","notes":"SMR/AI-power cooperation is Stage2; final equipment contract, workshare and margin are missing."}
{"case_id":"r1_loop17_samsung_heavy_zvezda_cancellation","symbol":"010140","company_name":"Samsung Heavy Industries","case_type":"4C_order_cancellation","primary_archetype":"SHIPBUILDING_ORDER_CANCELLATION_4C","best_trigger":"T1/T3","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2025-06-18","cancelled_order_value_krw_trn":4.85,"cancelled_order_value_usd_bn":3.54,"vessel_scope":["10_icebreaker_LNG_carriers","7_icebreaker_shuttle_tankers"],"direct_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"order_cancellation_4C_thesis_break","notes":"Major order cancellation shows backlog quality risk; damages recovery and replacement orders are needed for recovery."}
```

## data/e2r_trigger_calibration/triggers_r1_loop17_round250.jsonl 초안

```jsonl
{"trigger_id":"r1l17_hd_hhi_mipo_T1","case_id":"r1_loop17_hd_hyundai_heavy_mipo_masga","trigger_type":"Stage2-Actionable_shipbuilding_merger","trigger_date":"2025-08-27","event_return_pct":"HD_HHI_+11.3_Mipo_+14.6","trigger_outcome_label":"excellent_stage2_actionable_shipbuilding_consolidation","promote_to":"Stage2-Actionable"}
{"trigger_id":"r1l17_hanwha_ocean_frigate_T0","case_id":"r1_loop17_hanwha_ocean_us_navy_china_sanction","trigger_type":"Stage2_naval_optionality","trigger_date":"2025-12-23","event_return_pct":6,"trigger_outcome_label":"Stage2_naval_optional","promote_to":"Stage2"}
{"trigger_id":"r1l17_hanwha_ocean_china_T2","case_id":"r1_loop17_hanwha_ocean_us_navy_china_sanction","trigger_type":"4B_geopolitical_sanction","trigger_date":"2025-10-14","event_return_pct":-5.8,"trigger_outcome_label":"geopolitical_sanction_4B","promote_to":"4B-watch"}
{"trigger_id":"r1l17_hyundai_rotem_earnings_T0","case_id":"r1_loop17_hyundai_rotem_k2_poland","trigger_type":"Stage2-Actionable_export_earnings","trigger_date":"2024-04-09","event_return_pct":9.3,"market_relative_pp":9.6,"trigger_outcome_label":"excellent_export_earnings_entry","promote_to":"Stage2-Actionable"}
{"trigger_id":"r1l17_hyundai_rotem_poland_T2","case_id":"r1_loop17_hyundai_rotem_k2_poland","trigger_type":"Stage3-Yellow_candidate_repeat_export","trigger_date":"2025-08-01","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"repeat_export_yellow_candidate","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r1l17_hd_hyundai_electric_ai_T1","case_id":"r1_loop17_hd_hyundai_electric_ai_power","trigger_type":"Stage2_promote_candidate","trigger_date":"2024-07-11","event_return_pct":"reported_+333_since_Jan_2024","trigger_outcome_label":"missed_structural_if_stage2_ignored","promote_to":"Stage2_promote_candidate"}
{"trigger_id":"r1l17_ls_electric_report_T0","case_id":"r1_loop17_ls_electric_us_data_center_price_failed","trigger_type":"evidence_good_but_price_failed","trigger_date":"2024-07-01","event_return_pct":-5.4,"entry_price_krw":208500,"trigger_outcome_label":"price_failed_report_upgrade","promote_to":"no_actionable"}
{"trigger_id":"r1l17_hyosung_transformer_T0","case_id":"r1_loop17_hyosung_heavy_us_transformer_capacity","trigger_type":"Stage2_capacity_expansion_no_price","trigger_date":"2025-12-02","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"capacity_expansion_not_green","promote_to":"Stage2"}
{"trigger_id":"r1l17_doosan_smr_T0","case_id":"r1_loop17_doosan_enerbility_smr_ai_power","trigger_type":"Stage2_MOU_supply_chain","trigger_date":"2025-08-26","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"MOU_not_final_contract","promote_to":"Stage2"}
{"trigger_id":"r1l17_samsung_heavy_zvezda_T1","case_id":"r1_loop17_samsung_heavy_zvezda_cancellation","trigger_type":"4C_order_cancellation","trigger_date":"2025-06-18","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"order_cancellation_4C","promote_to":"4C-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round250_r1_loop17_v1.csv 초안

```csv
archetype,reported_event_return,market_relative_return,contract_value_visibility,naval_shipbuilding_us_workshare,grid_equipment_backlog,capacity_utilization,repeat_export_operator,order_quality_risk,theme_label_without_orders_penalty,report_upgrade_without_price_validation_penalty,capacity_headline_without_utilization_penalty,mou_without_final_contract_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
SHIPBUILDING_MASGA_MERGER_STAGE2_ACTIONABLE,+5,+4,+3,+5,+0,+3,+2,+3,-2,-1,-2,-1,shipbuilding merger+MASGA event,actual US orders/workshare missing,US order+post-merger margin,HD Hyundai Heavy/Mipo.
SHIPBUILDING_NAVAL_EXPORT_STAGE2_WITH_SANCTION_4B,+4,+2,+3,+5,+0,+2,+3,+5,-2,-1,-1,-1,US Navy optionality,China sanction 4B,formal contract+sanction resolution,Hanwha Ocean.
DEFENSE_INDUSTRIAL_EXPORT_STAGE2_YELLOW,+5,+5,+5,+0,+0,+3,+5,+2,-1,-1,-2,-1,repeat K2 export,local production margin gate,delivery+margin+local production,Hyundai Rotem.
GRID_EQUIPMENT_AI_POWER_STAGE2_PROMOTE,+4,+3,+2,+0,+5,+5,+1,+2,-4,-2,-4,-1,broad AI power rally,backlog/margin missing,orders+ASP+margin,HD Hyundai Electric.
GRID_EQUIPMENT_US_CAPACITY_STAGE2_WITH_PRICE_FAILED,+0,-5,+1,+0,+4,+3,+0,+2,-4,-5,-3,-1,good US data center report but price failed,actionable prohibited,actual orders+margin,LS Electric.
TRANSFORMER_CAPACITY_EXPANSION_STAGE2_NO_PRICE,+1,+0,+1,+0,+5,+5,+0,+2,-3,-1,-4,-1,US transformer shortage and capacity expansion,KRX price/orderbook missing,utilization+orderbook+margin,Hyosung Heavy.
NUCLEAR_SMR_INDUSTRIAL_SUPPLY_STAGE2_WITH_FINAL_CONTRACT_GATE,+1,+0,+2,+0,+1,+3,+0,+3,-3,-1,-2,-5,SMR/AI power cooperation,final contract missing,equipment order+workshare+margin,Doosan Enerbility.
SHIPBUILDING_ORDER_CANCELLATION_4C,-5,-3,-5,+0,+0,+0,+0,+5,-1,-1,-1,-1,major order cancellation,backlog quality impaired,damages recovery+replacement orders,Samsung Heavy.
```

---

# 이번 R1 Loop 17 결론

```text
1. HD Hyundai Heavy / Mipo는 R1의 가장 좋은 Stage2-Actionable이다.
   MASGA/U.S. shipbuilding cooperation + merger + +11.3%/+14.6% record-high reaction이 닫혔다.

2. Hanwha Ocean은 Stage2 naval optionality + China sanction 4B다.
   U.S. Navy frigate comment에는 +6%, 중국 제재에는 -5.8%였다.

3. Hyundai Rotem은 Stage3-Yellow 후보다.
   K2 Poland export가 +9.3% earnings trigger와 $6.5B repeat contract로 연결됐다.

4. HD Hyundai Electric은 missed_structural 가능성이 큰 Stage2_promote_candidate다.
   AI power-equipment cycle에서 +333% broad move가 나왔는데, 너무 보수적이면 놓친다.

5. LS Electric은 evidence_good_but_price_failed다.
   target price와 U.S. growth evidence는 좋았지만, 주가는 -5.4%였다.

6. Hyosung Heavy는 Stage2 capacity expansion이다.
   U.S. transformer shortage와 $157M Memphis expansion은 좋지만, 직접 price/orderbook이 없다.

7. Doosan Enerbility는 Stage2 SMR supply-chain이다.
   AWS/X-energy/Fermi linkage는 좋지만, MOU/final contract gate가 남는다.

8. Samsung Heavy는 order cancellation 4C다.
   4.85T won / $3.54B Zvezda cancellation은 backlog quality를 깨는 thesis-break다.
```

한 문장으로 압축하면:

> **R1 Loop 17에서 배운 핵심은 “수주·합병·AI 전력·조선·SMR headline”이 아니라, event return, market-relative strength, contract finality, backlog quality, capacity utilization, delivery margin, sanction/cancellation risk가 같이 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 리포트 상향, MOU, policy/MASGA narrative, capacity 증설만으로는 4B/false positive가 되기 쉽다.**

다음 순서는 **R2 Loop 17 — AI·반도체·전자부품**이다.

[1]: https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/ "https://www.reuters.com/markets/emerging/south-korean-shipbuilder-hd-hyundai-heavy-merge-with-affiliate-hd-hyundai-mipo-2025-08-27/"
[2]: https://www.reuters.com/world/asia-pacific/hanwha-ocean-shares-jump-6-after-trump-comments-building-us-frigates-2025-12-23/ "https://www.reuters.com/world/asia-pacific/hanwha-ocean-shares-jump-6-after-trump-comments-building-us-frigates-2025-12-23/"
[3]: https://www.wsj.com/articles/hyundai-rotem-rallies-on-hopes-tank-exports-will-boost-earnings-9322d840 "https://www.wsj.com/articles/hyundai-rotem-rallies-on-hopes-tank-exports-will-boost-earnings-9322d840"
[4]: https://www.reuters.com/markets/hedge-funds-turn-south-korea-next-wave-ai-2024-07-11/ "https://www.reuters.com/markets/hedge-funds-turn-south-korea-next-wave-ai-2024-07-11/"
[5]: https://www.marketwatch.com/story/ls-electric-could-gain-from-solid-u-s-business-growth-opportunity-market-talk-3e926067 "https://www.marketwatch.com/story/ls-electric-could-gain-from-solid-u-s-business-growth-opportunity-market-talk-3e926067"
[6]: https://www.reuters.com/business/energy/grid-equipment-makers-invest-us-ease-supply-shortage--reeii-2025-12-02/ "https://www.reuters.com/business/energy/grid-equipment-makers-invest-us-ease-supply-shortage--reeii-2025-12-02/"
[7]: https://www.reuters.com/business/aerospace-defense/south-korean-firms-pledge-150-billion-us-investments-summit-2025-08-26/ "https://www.reuters.com/business/aerospace-defense/south-korean-firms-pledge-150-billion-us-investments-summit-2025-08-26/"
[8]: https://www.reuters.com/business/retail-consumer/samsung-heavy-says-354-billion-icebreaker-orders-russias-zvezda-cancelled-2025-06-18/ "https://www.reuters.com/business/retail-consumer/samsung-heavy-says-354-billion-icebreaker-orders-russias-zvezda-cancelled-2025-06-18/"

순서상 이번은 **R2 Loop 16 — AI·반도체·전자부품 trigger-level price validation 라운드**다.

이번 R2는 R13 이후 두 번째 재순환 라운드라, 핵심을 더 날카롭게 잡아야 한다. **HBM·DRAM 가격·OpenAI/Stargate·파운드리 수주·후공정 장비·수출통제·노동 리스크·전자부품/센서 전략투자**를 한 덩어리로 보지 말고, 각각이 실제로 **wafer/bit shipment → ASP → OP estimate → backlog/capex → margin → 고객 인증**으로 이어졌는지 분리한다.

```text
round = R2 Loop 16
round_id = round_238
large_sector = AI_SEMICONDUCTOR_ELECTRONIC_COMPONENTS
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R3 Loop 16
```

이번에도 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 30D/90D/180D/1Y/2Y window는 안정적으로 직접 확보하지 못했다. 따라서 full MFE/MAE는 만들지 않고 `price_data_unavailable_after_deep_search`로 분리한다. 대신 Reuters/FT/WSJ/MarketWatch/Barron’s가 보도한 **event return, event price, contract value, OP forecast, demand capacity, export-control impact**를 trigger anchor로 사용한다. R13 원칙대로 **OHLC 미확보 때문에 Stage 후보 자체를 강등하지 않는다.**

---

# 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
```

R2의 core gate는 아래다.

```text
HBM / AI memory:
sample → customer qualification → mass production → shipment → ASP → DRAM revenue mix → OP estimate → sold-out capacity

DRAM / NAND pricing:
spot/contract price → long-term supply agreement → module price hike → server demand → margin → inventory risk

Foundry:
contract win → customer identity / node / yield → fab utilization → margin → Texas/Pyeongtaek execution

Advanced packaging / HBM equipment:
SK Hynix/Micron/TSMC/Nvidia supply chain → equipment order → repeat order → capacity expansion → customer concentration risk

Electronic components:
lidar / optical / sensor partnership → mass-production capacity → design-in → customer launch → margin

Policy / 4C:
China fab export license → upgrade ceiling → capex stranded risk
labor strike → DRAM/NAND supply disruption → customer delivery risk
HBM certification delay → inventory write-down → profit miss
```

---

# 2. 대상 canonical archetype

```text
HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE
MEMORY_SUPERCYCLE_ASP_STAGE2_YELLOW
OPENAI_STARGATE_HBM_DEMAND_STAGE2_ACTIONABLE
FOUNDRY_MEGA_CONTRACT_STAGE2_WITH_YIELD_4B
ADVANCED_PACKAGING_EQUIPMENT_STAGE2_WITH_RUMOR_4B
HBM_CERTIFICATION_DELAY_FALSE_POSITIVE
CHINA_FAB_EXPORT_CONTROL_4C_WATCH
SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH
ELECTRONIC_COMPONENT_LIDAR_STAGE2_ORDER_GATE
```

---

# 3. deep sub-archetype

```text
SK Hynix:
- HBM3E 12-layer mass production
- shares > +9% on HBM3E production
- HBM4 internal certification and production readiness
- shares +7.3%, KOSPI +1.2%
- HBM market share projected low-60% range in 2026
- ASML EUV order 11.95T won / $7.97B
- shares +5.7%
- Yongin / M15X HBM and advanced DRAM capacity

Samsung Electronics:
- memory price hikes up to 60%
- 32GB DDR5 $149 → $239
- record Q1 2026 OP guidance 57.2T won, +5% stock reaction
- OpenAI Stargate partnership, Samsung +4.7%, SK Hynix +12%, KOSPI +3%
- foundry $16.5B global-company deal, shares +3.5%
- HBM Nvidia test failure / Q2 2025 profit miss
- labor strike 4C-watch

Hanmi Semiconductor:
- HBM advanced packaging equipment / TSV-TC bonder
- SK Hynix contract KRW21.48B
- recent contract wins around KRW200B
- shares +16% with SK Hynix +4.3%, KOSPI +0.7%
- possible Micron deal media report, shares up to +22%, but unconfirmed

China fab export-control:
- U.S. revokes authorizations for Samsung/SK Hynix China fabs
- Samsung -2.3%, SK Hynix -4.4%, KOSPI -0.7%
- Samsung China DRAM >1/3, SK Hynix China DRAM/NAND 30~40%
- Hana Micron -1.7%, Hanmi -4.4%

LG Innotek / Aeva:
- $50M strategic collaboration
- LG Innotek $32M equity investment
- lidar sensors for vehicles, robotics, consumer electronics, AR
- no KRX price anchor found
```

---

# 4. 선정 case 요약

| bucket                               | case                                    | 핵심 판정                                                                                                    |
| ------------------------------------ | --------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| structural_success / Green candidate | SK Hynix HBM3E/HBM4/EUV                 | HBM3E mass production +9% 이상, HBM4 certification +7.3%, EUV order +5.7%. HBM leadership는 Yellow~Green 후보 |
| Stage3-Yellow candidate              | Samsung memory supercycle               | memory prices up to 60%, Q1 2026 OP guidance 57.2T won, shares +5%. HBM lag와 labor risk는 overlay         |
| Stage2-Actionable                    | Samsung/SK Hynix OpenAI Stargate        | Samsung +4.7%, SK Hynix +12%, KOSPI +3%, OpenAI semiconductor procurement/data center trigger            |
| Stage2 + 4B                          | Samsung foundry $16.5B                  | shares +3.5%, foundry deal large but node/yield/customer/fab utilization gate                            |
| Stage2-Actionable + rumor 4B         | Hanmi Semiconductor HBM equipment       | Hanmi +16%, possible Micron report up to +22%, SK Hynix equipment contracts. Rumor/고객집중 4B               |
| false_positive / 4C-watch            | Samsung HBM certification delay         | HBM Nvidia test fail, shares -2%; Q2 2025 profit miss, shares -0.2% vs KOSPI +1.2%                       |
| 4C-watch                             | Samsung/SK Hynix China fab export curbs | Samsung -2.3%, SK Hynix -4.4%, Hana Micron -1.7%, Hanmi -4.4%                                            |
| 4C-watch                             | Samsung labor strike                    | shares -9.3%, 48k~50k workers, DRAM/NAND supply risk                                                     |
| Stage2 order-gate                    | LG Innotek / Aeva lidar                 | $50M collaboration, $32M equity investment. Design-in/revenue 전에는 Stage2                                 |

---

# 5. Case별 trigger grid

## Case A — SK Hynix / HBM3E, HBM4, ASML EUV capacity

```text
symbol = 000660
case_type = structural_success / Stage3-Yellow to Green candidate
archetype = HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE
```

| trigger |                     type | date                 | 당시 공개 evidence                                                                                                    | 가격 anchor                 | outcome             |
| ------- | -----------------------: | -------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------- | ------------------- |
| T0      |          Stage2 evidence | 2024-09-26           | 12-layer HBM3E mass production start, 50% more capacity than 8-layer version                                      | shares > +9%, KOSPI +1.7% | Stage2-Actionable   |
| T1      |            Stage3-Yellow | 2025-09-12           | HBM4 internal certification completed, production system established, samples shipped in March                    | shares +7.3%, KOSPI +1.2% | Yellow candidate    |
| T2      | Stage3-Yellow validation | 2026-03-24           | ASML EUV order 11.95T won / $7.97B, largest disclosed ASML customer order; Yongin/M15X HBM·advanced DRAM capacity | SK Hynix +5.7%            | capacity validation |
| T3      |          Green candidate | 2025-10-28 / 2026-05 | record OP, 2026 production sold out, shares +200% in 2026 after +274% in 2025                                     | no trigger OHLC           | Green candidate     |
| T4      |                 4B-watch | 2026                 | valuation overheat, labor/bonus inflation, HBM customer concentration                                             | no full OHLC              | 4B                  |
| T5      |             Stage3-Green | 보류                   | full OHLC + multi-quarter margin/cash conversion unavailable                                                      | N/A                       | no confirmed Green  |

SK Hynix는 R2에서 가장 강한 structural case다. 2024년 9월 26일 12-layer HBM3E mass production을 시작했고, Reuters는 해당 주가가 9% 넘게 올랐다고 보도했다. 2025년 9월 12일에는 HBM4 internal certification 완료와 production readiness가 발표되며 SK Hynix가 장중 +7.3% 올랐고, KOSPI +1.2%를 크게 앞섰다. 이어 2026년 3월에는 ASML EUV 장비를 11.95T won, 약 $7.97B 규모로 매입하기로 했고, 이 장비가 Yongin과 M15X의 HBM·advanced DRAM 생산에 쓰일 것이라는 분석과 함께 주가가 +5.7% 올랐다. 이건 단순 AI memory headline이 아니라 **sample → certification → mass production → capex/capacity**가 닫힌 구조다. ([Reuters][1])

```json
{
  "case_id": "r2_loop16_sk_hynix_hbm3e_hbm4_euv",
  "symbol": "000660",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage3-Yellow_to_Green_candidate",
  "hbm3e_mass_production_date": "2024-09-26",
  "hbm3e_event_return_pct": ">9",
  "hbm4_certification_date": "2025-09-12",
  "hbm4_event_return_pct": 7.3,
  "kospi_hbm4_context_pct": 1.2,
  "market_relative_return_pp": 6.1,
  "asml_euv_order_date": "2026-03-24",
  "asml_euv_order_krw_trn": 11.95,
  "asml_euv_order_usd_bn": 7.97,
  "asml_order_event_return_pct": 5.7,
  "capacity_targets": ["Yongin", "M15X", "HBM", "advanced_DRAM"],
  "stage3_gate_missing": [
    "full_OHLC_MFE_MAE",
    "multi_quarter_HBM_margin",
    "customer_concentration_risk",
    "EUV_installation_schedule",
    "HBM4_customer_volume_shipment"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_to_yellow_green_candidate"
}
```

---

## Case B — Samsung Electronics / memory price hike and record profit supercycle

```text
symbol = 005930
case_type = Stage3-Yellow candidate / memory supercycle
archetype = MEMORY_SUPERCYCLE_ASP_STAGE2_YELLOW
```

| trigger |                   type | date       | 당시 공개 evidence                                                                            | 가격 anchor                                                 | outcome                      |
| ------- | ---------------------: | ---------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------- |
| T0      |        Stage2 evidence | 2025-11-17 | Samsung raises certain memory prices by up to 60%; 32GB DDR5 $149 → $239; 16GB/128GB +50% | chip shares rallied, exact KRX trigger price not isolated | Stage2-Actionable            |
| T1      |          Stage3-Yellow | 2026-04-07 | Q1 2026 OP guidance 57.2T won, +8x YoY, sales 133T won, far above expectations            | Samsung +5% to 203,000 won                                | Yellow candidate             |
| T2      | Stage3-Green candidate | 2026-05-06 | Samsung becomes $1T company, shares +14.4%, KOSPI +6.45%                                  | +14.4%                                                    | Green candidate but overheat |
| T3      |               4B-watch | 2026       | memory shortage, long-term contracts, but strike/energy/geopolitical cost risk            | no full OHLC                                              | 4B                           |
| T4      |           Stage3-Green | 보류         | full OHLC + confirmed durable margin unavailable                                          | N/A                                                       | no confirmed Green           |

Samsung memory는 “HBM laggard”에서 “memory ASP supercycle beneficiary”로 바뀐 case다. 2025년 11월 Samsung은 AI data center 수요로 인한 메모리 부족 속에서 일부 memory chip 가격을 9월 대비 최대 60% 올렸고, Reuters는 32GB DDR5 module이 $149에서 $239로 뛰었다고 보도했다. 2026년 4월에는 Q1 operating profit guidance가 57.2T won으로 전년 대비 8배 이상 증가하고, LSEG estimate 40.5T won을 크게 웃돌며 주가가 장중 +5% 올랐다는 FT 보도가 나왔다. 이 조합은 **ASP → 장기계약 → OP guidance beat**가 닫힌 Stage3-Yellow 후보로 봐야 한다. ([Reuters][2])

다만 2026년 5월 Samsung이 $1T market cap에 도달하고 주가가 +14.4% 뛰었던 날은 좋은 Green validation이면서 동시에 4B overheat도 같이 붙는다. 그날 KOSPI는 +6.45%였고 Samsung·SK Hynix가 KOSPI 총가치의 44%를 차지했다는 Reuters 보도가 있어, index crowding/positioning risk를 병기해야 한다. ([Reuters][3])

```json
{
  "case_id": "r2_loop16_samsung_memory_supercycle",
  "symbol": "005930",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage3-Yellow_candidate",
  "memory_price_hike_date": "2025-11-17",
  "max_memory_price_hike_pct": 60,
  "ddr5_32gb_price_before_usd": 149,
  "ddr5_32gb_price_after_usd": 239,
  "q1_2026_op_guidance_krw_trn": 57.2,
  "q1_2026_sales_guidance_krw_trn": 133,
  "q1_2026_op_lseg_estimate_krw_trn": 40.5,
  "record_profit_event_return_pct": 5,
  "record_profit_event_price_krw": 203000,
  "may_2026_event_return_pct": 14.4,
  "kospi_may_2026_event_return_pct": 6.45,
  "stage3_gate_missing": [
    "full_OHLC_MFE_MAE",
    "HBM_Nvidia_volume_certification",
    "strike_risk_resolution",
    "energy_cost_absorption",
    "memory_price_sustainability"
  ],
  "trigger_outcome_label": "Stage3_Yellow_candidate_with_4B_overheat_overlay"
}
```

---

## Case C — Samsung / SK Hynix / OpenAI Stargate partnership

```text
symbols = 005930 / 000660 / affiliates
case_type = Stage2-Actionable demand trigger
archetype = OPENAI_STARGATE_HBM_DEMAND_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                                                | 가격 anchor    | outcome           |
| ------- | ----------------: | ---------- | --------------------------------------------------------------------------------------------- | ------------ | ----------------- |
| T0      |         awareness | 2025-10-01 | OpenAI visit / Korean AI data-center and semiconductor procurement discussions                | no price yet | Stage1            |
| T1      | Stage2-Actionable | 2025-10-02 | Samsung +4.7%, SK Hynix +12%, KOSPI +3%, $37B combined market-cap addition                    | strong event | Actionable        |
| T2      | Stage2 validation | 2025-10-02 | OpenAI Stargate $500B AI infrastructure, Korean-style data centers, semiconductor procurement | same         | demand validation |
| T3      |          4B-watch | 2025~2026  | LOI/partnership, not binding wafer shipment; DRAM wafer demand up to 900k/month cited by FT   | no full OHLC | 4B                |
| T4      |     Stage3-Yellow | N/A        | binding purchase order / price / delivery schedule not verified                               | N/A          | no Yellow         |

OpenAI/Stargate는 R2에서 매우 강한 **demand Stage2-Actionable** trigger다. Reuters는 Samsung이 +4.7%, SK Hynix가 +12% 상승했고, 이 deal이 두 회사의 시총을 $37B 늘렸으며 KOSPI를 +3% 넘게 record high로 밀어 올렸다고 보도했다. FT는 OpenAI와의 letter of intent가 $500B Stargate data center project를 위한 semiconductor supply와 관련돼 있고, SK Hynix가 OpenAI의 HBM 수요를 맞추기 위해 최대 월 900,000 DRAM wafers까지 대응할 생산체계를 언급했다고 보도했다. ([Reuters][4])

하지만 이건 아직 Stage3-Green이 아니다. LOI/strategic partnership은 강하지만, binding purchase order, wafer allocation, ASP, delivery schedule이 확인되어야 Yellow/Green으로 올라간다.

```json
{
  "case_id": "r2_loop16_samsung_skhynix_openai_stargate",
  "symbols": "005930/000660",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable",
  "trigger_date": "2025-10-02",
  "samsung_event_return_pct": 4.7,
  "sk_hynix_event_return_pct": 12.0,
  "kospi_event_return_pct": 3.0,
  "combined_market_cap_addition_usd_bn": 37,
  "stargate_project_value_usd_bn": 500,
  "korea_data_center_capacity_mw_each": 20,
  "openai_dram_wafer_demand_monthly_context": 900000,
  "stage3_gate_missing": [
    "binding_purchase_order",
    "wafer_allocation",
    "HBM_ASP",
    "delivery_schedule",
    "customer_payment_terms"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "excellent_stage2_actionable_demand_trigger"
}
```

---

## Case D — Samsung Electronics / $16.5B foundry contract

```text
symbol = 005930
case_type = Stage2 foundry contract with yield 4B
archetype = FOUNDRY_MEGA_CONTRACT_STAGE2_WITH_YIELD_4B
```

| trigger |            type | date       | 당시 공개 evidence                                                                           | 가격 anchor     | outcome             |
| ------- | --------------: | ---------- | ---------------------------------------------------------------------------------------- | ------------- | ------------------- |
| T0      |       awareness | 2024~2025  | Samsung foundry lag vs TSMC, Texas fab delay, 2nm yield concern                          | no price      | 4B background       |
| T1      | Stage2 evidence | 2025-07-28 | Samsung signs $16.5B contract chip manufacturing deal with unnamed global company        | Samsung +3.5% | Stage2              |
| T2      |        4B-watch | 2025-07-28 | customer confidential until 2033, order unlikely to be cutting-edge 2nm due yield issues | same          | yield/customer gate |
| T3      |   Stage3-Yellow | N/A        | utilization / node / margin / customer identity not confirmed                            | N/A           | no Yellow           |

Samsung foundry deal은 headline size가 크다. Reuters는 Samsung이 unnamed major global company와 $16.5B contract chip manufacturing deal을 signed했고, 주가가 +3.5% 올랐다고 보도했다. 하지만 같은 보도에서 deal details와 counterpart는 2033년 계약 완료까지 비공개이고, BNK analyst는 Samsung의 2nm yield issue 때문에 이 order가 cutting-edge 2nm일 가능성은 낮다고 평가했다. 그래서 이건 `Stage2 foundry contract`이지 Green이 아니다. ([Reuters][5])

```json
{
  "case_id": "r2_loop16_samsung_foundry_165b_contract",
  "symbol": "005930",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_with_yield_4B",
  "trigger_date": "2025-07-28",
  "contract_value_usd_bn": 16.5,
  "contract_end_year": 2033,
  "event_return_pct": 3.5,
  "counterparty_disclosed": false,
  "cutting_edge_2nm_likely": false,
  "reason_cutting_edge_2nm_uncertain": "yield_issues",
  "stage3_gate_missing": [
    "customer_identity",
    "node_details",
    "yield",
    "Texas_fab_utilization",
    "gross_margin",
    "payment_schedule"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_foundry_contract_with_4B_yield_gate"
}
```

---

## Case E — Hanmi Semiconductor / HBM advanced packaging equipment

```text
symbol = 042700
case_type = Stage2-Actionable with rumor/overheat 4B
archetype = ADVANCED_PACKAGING_EQUIPMENT_STAGE2_WITH_RUMOR_4B
```

| trigger |              type | date       | 당시 공개 evidence                                                                                                                | 가격 anchor     | outcome           |
| ------- | ----------------: | ---------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- |
| T0      |   Stage2 evidence | 2024-03-26 | Hanmi supplies SK Hynix with HBM advanced packaging equipment such as TSV-TC bonders; SK Hynix +4.3%, Hanmi +16%, KOSPI +0.7% | Hanmi +16%    | Stage2-Actionable |
| T1      | Stage2 validation | 2024-03    | SK Hynix KRW21.48B contract, recent deals around KRW200B                                                                      | same          | order validation  |
| T2      |  4B / rumor watch | 2024-03-28 | media reports possible Micron deal; Hanmi up to +22%, KOSPI -0.3%; no company confirmation                                    | +22% intraday | 4B rumor          |
| T3      |     Stage3-Yellow | N/A        | repeat order / multi-customer revenue / margin not verified                                                                   | N/A           | no Yellow         |

Hanmi는 R2 후공정 장비에서 좋은 Stage2-Actionable case다. WSJ는 SK Hynix +4.3%, Hanmi Semiconductor +16%, KOSPI +0.7%를 보도했고, Hanmi가 SK Hynix에 TSV-TC bonder 등 HBM advanced packaging equipment를 공급하며 최근 SK Hynix와 KRW21.48B 계약, 약 KRW200B 규모의 최근 계약들을 확보했다고 전했다. 이건 **HBM demand → equipment order → price reaction**이 닫힌 Stage2-Actionable이다. ([월스트리트저널][6])

다만 2024년 3월 28일 media reports of possible Micron deal로 Hanmi가 장중 +22%까지 오른 것은 `4B rumor overlay`다. WSJ는 Micron initial order 가능성이 보도됐지만 Hanmi와 Micron 모두 즉시 comment하지 않았다고 밝혔다. 즉 확정 수주가 아니라 customer diversification 기대다. ([월스트리트저널][7])

```json
{
  "case_id": "r2_loop16_hanmi_semiconductor_hbm_equipment",
  "symbol": "042700",
  "best_trigger": "T0/T1",
  "best_trigger_type": "Stage2-Actionable_with_4B_rumor_overlay",
  "trigger_date": "2024-03-26/2024-03-28",
  "hanmi_event_return_pct": 16,
  "sk_hynix_event_return_pct": 4.3,
  "kospi_event_return_pct": 0.7,
  "market_relative_return_pp": 15.3,
  "skhynix_contract_krw_bn": 21.48,
  "recent_contracts_total_krw_bn": 200,
  "possible_micron_report_intraday_return_pct": 22,
  "micron_deal_confirmed": false,
  "stage3_gate_missing": [
    "repeat_orders",
    "confirmed_Micron_customer",
    "TSMC_Nvidia_supply_chain_volume",
    "equipment_margin",
    "customer_concentration_reduction"
  ],
  "full_mfe_mae_status": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "Stage2_Actionable_but_rumor_4B"
}
```

---

## Case F — Samsung HBM certification delay and Q2 2025 profit miss

```text
symbol = 005930
case_type = false_positive / HBM delay 4C-watch
archetype = HBM_CERTIFICATION_DELAY_FALSE_POSITIVE
```

| trigger |             type | date       | 당시 공개 evidence                                                                                                           | 가격 anchor                               | outcome             |
| ------- | ---------------: | ---------- | ------------------------------------------------------------------------------------------------------------------------ | --------------------------------------- | ------------------- |
| T0      |         4C-watch | 2024-05-24 | Reuters sources say Samsung HBM3/HBM3E failed Nvidia tests due heat/power issues; Samsung disputes specifics             | shares -2%, slightly weaker than market | HBM 4C-watch        |
| T1      |    4C validation | 2025-07-08 | Q2 OP forecast -56% YoY to 4.6T won vs 6.2T estimate; chip profit possibly down >90%; HBM delay and AI China curbs cited | shares -0.2% vs KOSPI +1.2%             | evidence-price weak |
| T2      | relief candidate | 2025-09~   | later certification/price hike possible                                                                                  | handled in Samsung supercycle case      | relief              |
| T3      |    Stage3-Yellow | N/A        | Nvidia volume HBM shipment not confirmed at T1                                                                           | N/A                                     | no Yellow           |

Samsung HBM delay는 R2에서 반드시 별도 red-team row가 필요하다. Reuters는 2024년 5월 Samsung HBM3/HBM3E가 Nvidia tests를 heat and power issues 때문에 통과하지 못했다고 보도했고, Samsung은 구체 claim을 부인했지만 shares는 -2%로 broader market보다 약했다. 2025년 7월에는 Samsung이 Q2 operating profit이 56% 감소한 4.6T won으로 LSEG estimate 6.2T won을 크게 밑돌 것으로 guidance했고, Reuters는 HBM 공급 지연과 U.S. AI chip curbs to China가 원인으로 언급됐다고 보도했다. 이때 Samsung shares는 -0.2%였지만 KOSPI가 +1.2%였으므로 상대적으로 약했다. ([Reuters][8])

```json
{
  "case_id": "r2_loop16_samsung_hbm_delay_false_positive",
  "symbol": "005930",
  "best_trigger": "T0/T1",
  "best_trigger_type": "4C_watch_HBM_certification_delay",
  "t0_date": "2024-05-24",
  "t0_event_return_pct": -2,
  "issue": "HBM3_HBM3E_Nvidia_test_delay",
  "reported_failure_reasons": ["heat", "power_consumption"],
  "samsung_disputed_specific_claims": true,
  "t1_date": "2025-07-08",
  "q2_2025_op_guidance_krw_trn": 4.6,
  "q2_2025_op_lseg_estimate_krw_trn": 6.2,
  "q2_2025_op_yoy_pct": -56,
  "chip_division_op_decline_context": ">90%",
  "t1_event_return_pct": -0.2,
  "kospi_same_context_pct": 1.2,
  "market_relative_return_pp": -1.4,
  "trigger_outcome_label": "HBM_certification_delay_4C_watch"
}
```

---

## Case G — Samsung / SK Hynix China fab export-control curbs

```text
symbols = 005930 / 000660 / 067310 / 042700
case_type = 4C-watch trade-policy shock
archetype = CHINA_FAB_EXPORT_CONTROL_4C_WATCH
```

| trigger |          type | date       | 당시 공개 evidence                                                                           | 가격 anchor                                  | outcome        |
| ------- | ------------: | ---------- | ---------------------------------------------------------------------------------------- | ------------------------------------------ | -------------- |
| T0      |     awareness | 2022~2025  | U.S. chip-equipment export control exemptions for Korean China fabs                      | no price                                   | Stage1 risk    |
| T1      |      4C-watch | 2025-09-01 | U.S. revokes authorizations for Samsung/SK Hynix China fabs, effective in 120 days       | Samsung -2.3%, SK Hynix -4.4%, KOSPI -0.7% | 4C-watch       |
| T2      | 4C validation | 2025-09-01 | Samsung China DRAM >1/3, SK Hynix China DRAM/NAND 30~40%; Hana Micron -1.7%, Hanmi -4.4% | supplier spread                            | validated      |
| T3      |        relief | 2025~      | maintenance license possible, expansion/upgrade constrained                              | no full OHLC                               | partial relief |
| T4      | Stage3-Yellow | N/A        | no growth trigger                                                                        | N/A                                        | N/A            |

이 case는 R2의 textbook 4C-watch다. Reuters는 U.S.가 Samsung과 SK Hynix의 China fabs에 U.S. semiconductor equipment를 들여보낼 수 있게 했던 authorizations를 revoke했고, 이 조치가 120일 뒤 발효된다고 보도했다. Samsung은 -2.3%, SK Hynix는 -4.4%, KOSPI는 -0.7%였고, Hana Micron -1.7%, Hanmi Semiconductor -4.4%까지 동반 약세였다. Samsung DRAM output의 3분의 1 이상, SK Hynix DRAM/NAND의 30~40%가 China 기반이라는 exposure도 확인됐다. ([Reuters][9])

```json
{
  "case_id": "r2_loop16_china_fab_export_control",
  "symbols": "005930/000660/067310/042700",
  "best_trigger": "T1/T2",
  "best_trigger_type": "4C_watch_trade_policy",
  "trigger_date": "2025-09-01",
  "samsung_event_return_pct": -2.3,
  "sk_hynix_event_return_pct": -4.4,
  "kospi_same_context_pct": -0.7,
  "samsung_market_relative_pp": -1.6,
  "skhynix_market_relative_pp": -3.7,
  "hana_micron_event_return_pct": -1.7,
  "hanmi_event_return_pct": -4.4,
  "samsung_china_dram_output_share": ">33%",
  "skhynix_china_dram_nand_output_share_pct": "30-40",
  "policy_effective_delay_days": 120,
  "trigger_outcome_label": "trade_policy_4C_watch"
}
```

---

## Case H — Samsung labor strike risk

```text
symbol = 005930
case_type = 4C-watch labor-output shock
archetype = SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH
```

| trigger |       type | date          | 당시 공개 evidence                                                                                                       | 가격 anchor          | outcome    |
| ------- | ---------: | ------------- | -------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------- |
| T0      |  awareness | 2026-05       | Samsung union dispute over bonus cap and operating-profit pool                                                       | no price           | watch      |
| T1      |   4C-watch | 2026-05-15    | union sticks to 18-day strike plan, >50,000 workers possible                                                         | Samsung -9.3%      | hard watch |
| T2      | validation | 2026-05-19    | nearly 48,000 workers, possible 3~4% DRAM and 2~3% NAND supply disruption, 30T won / $19.9B production-loss scenario | no new price       | validated  |
| T3      |     relief | 2026-05-18~19 | court requires 7,087 essential workers and talks resume                                                              | relief, not growth | 4C relief  |
| T4      |     Stage3 | N/A           | no growth trigger                                                                                                    | N/A                | N/A        |

Samsung labor strike risk is not just a labor story; it is semiconductor output risk. Reuters reported on May 15, 2026 that Samsung shares fell as much as 9.3% after the union kept its 18-day strike plan. Reuters then reported nearly 48,000 workers could strike, and KB Securities estimated an 18-day strike could cut global DRAM supply by 3~4% and NAND by 2~3%; Korean officials warned a worst-case scenario could reduce GDP growth by 0.5 percentage point and imply around 30T won, or $19.9B, of chip-production loss. ([Reuters][10])

```json
{
  "case_id": "r2_loop16_samsung_labor_strike_4c",
  "symbol": "005930",
  "best_trigger": "T1/T2",
  "best_trigger_type": "4C_watch_labor_output_risk",
  "t1_date": "2026-05-15",
  "event_return_pct": -9.3,
  "planned_strike_duration_days": 18,
  "potential_workers": ">50000",
  "t2_date": "2026-05-19",
  "potential_workers_updated": 48000,
  "essential_workers_required": 7087,
  "potential_dram_supply_cut_pct": "3-4",
  "potential_nand_supply_cut_pct": "2-3",
  "potential_chip_production_loss_krw_trn": 30,
  "potential_chip_production_loss_usd_bn": 19.9,
  "trigger_outcome_label": "semiconductor_labor_4C_watch"
}
```

---

## Case I — LG Innotek / Aeva lidar and precision-sensing collaboration

```text
symbol = 011070
case_type = Stage2 electronic component with order gate
archetype = ELECTRONIC_COMPONENT_LIDAR_STAGE2_ORDER_GATE
```

| trigger |              type | date       | 당시 공개 evidence                                                                                                 | 가격 anchor                        | outcome    |
| ------- | ----------------: | ---------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------- | ---------- |
| T0      |         awareness | 2025       | camera module supplier seeks next-generation sensor/robotics/AR growth                                         | no price                         | Stage1     |
| T1      |   Stage2 evidence | 2025-07-29 | LG Innotek to invest $32M in Aeva as part of $50M strategic collaboration                                      | LG Innotek KRX price unavailable | Stage2     |
| T2      | Stage2 validation | 2025-07-29 | Aeva lidar for vehicles, industrial equipment, robotics, consumer devices and AR; low-cost single-chip roadmap | no price                         | validation |
| T3      |          4B-watch | 2025~      | strategic stake but no mass design-in, launch, margin                                                          | no OHLC                          | 4B         |
| T4      |     Stage3-Yellow | N/A        | design-in/order/revenue not confirmed                                                                          | N/A                              | no Yellow  |

LG Innotek/Aeva는 R2 전자부품의 좋은 Stage2 diversification case다. Reuters는 LG Innotek이 lidar sensor maker Aeva에 $32M equity investment를 하고, 전체 $50M strategic collaboration으로 production capacity를 확대한다고 보도했다. Aeva sensors는 vehicles, industrial equipment, robotics, consumer electronics, AR headset까지 target하고, sensor 전체를 저가 single chip으로 통합하는 roadmap을 갖고 있다고 설명했다. 다만 design-in, mass production, 고객 launch, margin이 없으면 Stage3가 아니다. ([Reuters][11])

```json
{
  "case_id": "r2_loop16_lg_innotek_aeva_lidar",
  "symbol": "011070",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2_electronic_component_order_gate",
  "trigger_date": "2025-07-29",
  "strategic_collaboration_value_usd_mn": 50,
  "lg_innotek_equity_investment_usd_mn": 32,
  "stake_pct_context": "single_digit",
  "target_markets": [
    "vehicles",
    "industrial_equipment",
    "robotics",
    "consumer_electronics",
    "AR_headsets"
  ],
  "direct_krx_price_anchor": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "design_in",
    "mass_production_order",
    "customer_launch",
    "sensor_ASP_margin",
    "module_integration_revenue"
  ],
  "trigger_outcome_label": "Stage2_component_diversification_not_Green"
}
```

---

# 6. Trigger별 가격경로 검증 요약

| case                       | best trigger |                     entry anchor |                                    event MFE/MAE |                    market-relative | full MFE/MAE | outcome                          |
| -------------------------- | ------------ | -------------------------------: | -----------------------------------------------: | ---------------------------------: | ------------ | -------------------------------- |
| SK Hynix HBM3E/HBM4/EUV    | T1/T2        |                   reported event |                HBM3E >+9%, HBM4 +7.3%, EUV +5.7% |               HBM4 +6.1pp vs KOSPI | unavailable  | Stage3-Yellow / Green candidate  |
| Samsung memory supercycle  | T0/T1        | 203,000 won on Q1 guidance event |                    +5%, later +14.4% in AI rally | +7.95pp vs KOSPI on May 2026 rally | unavailable  | Stage3-Yellow candidate + 4B     |
| Samsung/SK OpenAI Stargate | T1/T2        |                            event |                           Samsung +4.7%, SK +12% |               SK +9pp vs KOSPI +3% | unavailable  | Stage2-Actionable                |
| Samsung foundry $16.5B     | T1/T2        |                            event |                                    Samsung +3.5% |                        unavailable | unavailable  | Stage2 + yield 4B                |
| Hanmi HBM equipment        | T0/T1        |                            event |                        +16%, possible rumor +22% |             +15.3pp vs KOSPI +0.7% | unavailable  | Stage2-Actionable + rumor 4B     |
| Samsung HBM delay          | T0/T1        |                            event |                  -2%, later -0.2% vs KOSPI +1.2% |                  -1.4pp on Q2 miss | unavailable  | 4C-watch                         |
| China fab export curbs     | T1/T2        |                            event | Samsung -2.3%, SK -4.4%, Hana -1.7%, Hanmi -4.4% |                 SK -3.7pp vs KOSPI | unavailable  | 4C-watch                         |
| Samsung labor strike       | T1/T2        |                            event |                                    Samsung -9.3% |                        unavailable | unavailable  | 4C-watch                         |
| LG Innotek/Aeva            | T1/T2        |                      unavailable |                                     no KRX price |                                N/A | unavailable  | Stage2 component diversification |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
좋은 Stage2:
- Samsung/SK OpenAI Stargate
- Samsung foundry $16.5B
- LG Innotek/Aeva lidar
- Samsung memory price hike

약한 Stage2:
- Samsung foundry는 customer/node/yield가 없어서 Stage2만.
- LG Innotek/Aeva는 design-in/order가 없어 Stage2만.
```

## Stage2-Actionable entry 성과

```text
Actionable:
- SK Hynix HBM4 certification and HBM3E mass production.
- Hanmi HBM packaging equipment contracts.
- OpenAI/Stargate partnership.
- Samsung memory ASP/OP guidance.

단, Actionable이라도 4B가 붙는 것:
- Hanmi possible Micron deal은 rumor.
- Samsung foundry는 yield/customer gate.
- Samsung memory는 labor/energy/overheat overlay.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- SK Hynix: HBM4 certification + EUV capex + HBM leadership.
- Samsung memory: ASP hikes + record OP guidance.
- Hanmi: repeat confirmed orders and margin confirm 시.
- Samsung/SK OpenAI: binding wafer purchase and ASP confirm 시.
```

## Stage3-Green

```text
이번 R2 Loop 16에서 확정 Green은 보류.

이유:
- SK Hynix는 Green candidate지만 full OHLC + multi-quarter HBM margin/cash가 필요.
- Samsung memory는 OP guidance가 강하지만 labor/energy/HBM certification overlay가 있다.
- OpenAI/Stargate는 LOI/partnership에서 binding order로 닫혀야 한다.
- Hanmi는 customer diversification and repeat order가 더 필요하다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- SK Hynix HBM3E/HBM4/EUV
- Samsung memory ASP/OP guidance
- Hanmi HBM equipment
- OpenAI/Stargate demand trigger

Stage2_promote_candidate:
- SK Hynix HBM
- Samsung memory supercycle
- Hanmi Semiconductor
- Samsung/SK OpenAI Stargate

Stage3-Yellow candidate:
- SK Hynix HBM4/EUV
- Samsung memory supercycle
- Hanmi if confirmed Micron/repeat order
- Samsung/SK if OpenAI binding purchase order confirms

evidence_good_but_price_failed_or_muted:
- Samsung foundry $16.5B if treated as 2nm/advanced AI win without evidence
- LG Innotek/Aeva because no KRX price anchor
- Samsung HBM delay/profit miss

false_positive_score:
- Samsung foundry if customer/node/yield are assumed
- Hanmi Micron rumor if treated as confirmed
- OpenAI partnership if treated as actual wafer shipment
- Samsung price hike if labor risk ignored

thesis_break_watch:
- Samsung HBM Nvidia certification delay
- China fab export-control curbs
- Samsung labor strike

hard_4C_success:
- 이번 R2에서는 confirmed hard 4C 없음
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
HBM_customer_certification,+5,"HBM은 customer qualification이 Stage2→Yellow 핵심 gate","SK Hynix, Samsung HBM delay"
HBM_mass_production_shipment,+5,"mass production and shipment는 단순 sample보다 강함","SK Hynix HBM3E/HBM4"
memory_ASP_contract_power,+5,"DDR5/DRAM price hike와 장기계약은 OP bridge","Samsung memory"
OP_estimate_guidance_beat,+5,"OP guidance beat는 Stage3-Yellow 핵심","Samsung memory"
EUV_capacity_commitment,+4,"EUV capex는 HBM/advanced DRAM capacity validation","SK Hynix ASML"
advanced_packaging_order_visibility,+5,"HBM equipment repeat order는 후공정 Stage2-Actionable","Hanmi"
binding_AI_infra_purchase,+5,"OpenAI partnership은 binding PO 전에는 Stage2","Samsung/SK OpenAI"
export_license_stability,+5,"China fab license는 4C hard overlay","Samsung/SK export curbs"
labor_output_continuity,+5,"strike risk는 DRAM/NAND supply hard overlay","Samsung strike"
```

## 내릴 축

```csv
axis,delta,reason,cases
HBM_headline_without_customer_certification,-5,"HBM headline만으로 Green 금지","Samsung HBM delay"
foundry_contract_without_node_yield,-5,"foundry mega contract는 node/yield/customer gate 필요","Samsung foundry"
AI_partnership_without_binding_order,-4,"OpenAI/Stargate LOI는 실제 wafer order 전에는 Stage2","OpenAI Stargate"
equipment_rumor_without_signed_order,-5,"possible Micron deal은 4B rumor","Hanmi"
capex_without_installation_yield,-3,"EUV/capex는 설치·수율 전에는 Green 아님","SK Hynix ASML"
component_partnership_without_design_in,-4,"Aeva/LG Innotek은 design-in 전에는 Stage2","LG Innotek"
memory_supercycle_without_4C_overlay,-3,"supercycle에도 strike/export/energy risk 병기","Samsung memory"
```

---

# 10. Stage2-Actionable 승격 조건

R2 Loop 16 shadow rule:

```text
R2에서 Stage2 evidence가 아래 중 3개 이상이면 Stage2-Actionable로 승격한다.

1. 고객 인증 또는 customer qualification이 확인된다.
2. mass production, shipment, or delivery schedule이 공개된다.
3. ASP/contract price 상승이 확인된다.
4. OP estimate/guidance beat가 있다.
5. event return이 +5% 이상이다.
6. market-relative return이 +5pp 이상이다.
7. equipment/order/capex가 HBM·AI memory capacity와 직접 연결된다.
8. export-control/labor/qualification 4C overlay가 없다.
```

적용:

```text
SK Hynix:
HBM3E mass production + HBM4 certification + EUV capex + strong price reaction → Stage2-Actionable / Yellow candidate.

Samsung memory:
price hike + record OP guidance + +5% reaction → Stage3-Yellow candidate.

Hanmi:
HBM equipment order + +16% + SK Hynix supply chain → Stage2-Actionable.

OpenAI Stargate:
Samsung/SK strong reaction and demand trigger → Stage2-Actionable, but binding order needed.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
- Stage2-Actionable 이후 EPS/OP/FCF 경로 변화 가능성이 높아짐
- 다만 고객별 volume, margin, capacity, 4C overlay 중 하나가 남은 상태
```

Yellow 후보:

```text
SK Hynix:
HBM4 certification and EUV capacity.
남은 gate: customer volume shipment, margin, customer concentration.

Samsung memory:
ASP hike and record OP guidance.
남은 gate: labor risk, energy cost, HBM competitiveness.

Hanmi:
repeat SK Hynix order and possible customer diversification.
남은 gate: confirmed Micron/other customer and margin.

Samsung/SK OpenAI:
demand signal strong.
남은 gate: binding PO, wafer allocation, ASP.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- HBM qualification and volume shipment confirmed
- memory ASP converts to quarterly OP and margin
- equipment order repeats and customer base broadens
- foundry deal node/yield/customer/fab utilization confirmed
- export-control and labor risks stable
- full-window MFE/MAE favorable
```

이번 R2 Loop 16에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + customer-volume/margin/4C overlay not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- HBM rumor or customer-test speculation without certification
- foundry mega-contract without node/yield/customer identity
- equipment customer rumor without signed order
- AI infra partnership without binding wafer order
- valuation surge after memory supercycle without labor/export-control risk pricing
- component strategic partnership without design-in
```

적용:

```text
Samsung foundry:
$16.5B contract but no customer/node/yield → 4B.

Hanmi:
Micron rumor +22% → 4B rumor.

Samsung/SK OpenAI:
partnership is strong, but binding order absent → 4B watch.

LG Innotek/Aeva:
strategic collaboration but design-in absent → 4B.
```

---

# 14. 4C hard gate 조건

```text
R2 4C:
- HBM qualification failure / customer rejection
- export-license revocation limiting China fab upgrade
- labor strike affecting DRAM/NAND supply
- foundry yield failure causing utilization loss
- inventory write-down from unsold HBM
- customer cancellation / delayed qualification
```

이번 R2 Loop 16 hard 4C 확정은 없다.

```text
hard_4c_not_confirmed = true
```

Strong 4C-watch:

```text
- Samsung HBM Nvidia delay
- Samsung Q2 2025 profit miss and HBM inventory write-down risk
- Samsung/SK China fab export curbs
- Samsung labor strike
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R13 이후 R2 production 설계 원칙:

```text
1. HBM은 sample, certification, mass production, volume shipment를 분리한다.
2. partnership과 binding order를 분리한다.
3. foundry contract는 customer/node/yield/utilization이 닫히기 전 Green 금지다.
4. equipment rally는 signed order와 rumor를 분리한다.
5. labor/export-control/HBM delay는 R2 hard overlay로 별도 row에 남긴다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_238.md 요약

```md
# R2 Loop 16. AI / Semiconductor / Electronic Components Trigger-level Price Validation

이번 라운드는 R2 Loop 16 trigger-level validation 라운드다.

핵심 결론:
- SK Hynix is the cleanest HBM structural success. HBM3E 12-layer mass production triggered more than 9% share rally; HBM4 internal certification and production readiness triggered +7.3% vs KOSPI +1.2%; ASML EUV order of 11.95T won / $7.97B triggered +5.7%. This is Stage2-Actionable to Stage3-Yellow/Green candidate, but full OHLC and multi-quarter HBM margin are still required.
- Samsung memory supercycle is Stage3-Yellow candidate. Samsung raised certain memory prices by up to 60%; 32GB DDR5 rose from $149 to $239; Q1 2026 OP guidance was 57.2T won, far above 40.5T won estimate, and shares rose 5%. Labor and HBM certification risk remain overlays.
- Samsung/SK Hynix OpenAI Stargate is Stage2-Actionable. Samsung +4.7%, SK Hynix +12%, KOSPI +3%, combined market cap +$37B. It is not Green until binding wafer purchase, ASP and delivery schedule are confirmed.
- Samsung foundry $16.5B deal is Stage2 with yield 4B. Samsung +3.5%, but customer identity, node, yield and fab utilization are not disclosed; analysts suggested it was unlikely to involve cutting-edge 2nm due yield issues.
- Hanmi Semiconductor HBM equipment is Stage2-Actionable with rumor 4B. Hanmi +16% while KOSPI +0.7%; it supplies SK Hynix with TSV-TC bonders and had KRW21.48B SK Hynix contract plus around KRW200B recent contracts. Possible Micron deal rally up to +22% is rumor until confirmed.
- Samsung HBM certification delay is 4C-watch. Reuters reported HBM3/HBM3E Nvidia test issues; Samsung shares fell 2%. Q2 2025 profit guidance missed badly, with OP down 56% and chip profit possibly down over 90%.
- Samsung/SK Hynix China fab export curbs are 4C-watch. Samsung -2.3%, SK Hynix -4.4%, KOSPI -0.7%; China fabs account for >1/3 of Samsung DRAM and 30~40% of SK Hynix DRAM/NAND.
- Samsung labor strike is 4C-watch. Shares slid 9.3% on strike plan; 48k~50k workers could affect 3~4% DRAM and 2~3% NAND supply.
- LG Innotek/Aeva lidar is Stage2 component diversification. $50M collaboration and $32M equity investment are real evidence, but design-in and revenue are missing.

Main calibration:
- Raise HBM_customer_certification, HBM_mass_production_shipment, memory_ASP_contract_power, OP_estimate_guidance_beat, EUV_capacity_commitment, advanced_packaging_order_visibility, binding_AI_infra_purchase, export_license_stability, labor_output_continuity.
- Lower HBM_headline_without_customer_certification, foundry_contract_without_node_yield, AI_partnership_without_binding_order, equipment_rumor_without_signed_order, component_partnership_without_design_in, memory_supercycle_without_4C_overlay.
```

## docs/checkpoints/checkpoint_28a_round238_r2_loop16.md 요약

```md
# Checkpoint 28A Round 238 R2 Loop 16 Trigger-level Calibration

## 반영 내용
- R2 Loop 16 trigger-level validation을 수행했다.
- SK Hynix HBM3E/HBM4/EUV, Samsung memory supercycle, Samsung/SK OpenAI Stargate, Samsung foundry $16.5B, Hanmi HBM equipment, Samsung HBM delay, China fab export curbs, Samsung labor strike, LG Innotek/Aeva lidar를 검토했다.
- full adjusted OHLC window는 확보하지 못했으므로 Reuters / FT / WSJ / MarketWatch / Barron’s의 reported event return과 event price anchor를 사용했다.
- OHLC 미확보를 이유로 Stage 후보를 강등하지 않고, price_data_unavailable_after_deep_search로 분리 기록했다.

## 핵심 보정
- HBM은 sample → certification → mass production → shipment를 분리한다.
- OpenAI/Stargate 같은 partnership은 binding wafer order 전에는 Stage2-Actionable에 머문다.
- Foundry contract는 customer/node/yield/fab utilization 전에는 Green 금지다.
- Hanmi 같은 equipment supplier는 signed order와 rumor rally를 분리한다.
- China fab export-control, labor strike, HBM customer qualification delay는 R2 4C overlay다.
```

## data/e2r_case_library/cases_r2_loop16_round238.jsonl 초안

```jsonl
{"case_id":"r2_loop16_sk_hynix_hbm3e_hbm4_euv","symbol":"000660","company_name":"SK Hynix","case_type":"Stage3_Yellow_to_Green_candidate","primary_archetype":"HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE","best_trigger":"T1/T2","stage_candidate":"Stage3-Yellow_to_Green_candidate","price_validation":{"hbm3e_mass_production_date":"2024-09-26","hbm3e_event_return_pct":">9","hbm4_certification_date":"2025-09-12","hbm4_event_return_pct":7.3,"kospi_hbm4_context_pct":1.2,"market_relative_return_pp":6.1,"asml_euv_order_date":"2026-03-24","asml_euv_order_krw_trn":11.95,"asml_euv_order_usd_bn":7.97,"asml_order_event_return_pct":5.7,"capacity_targets":["Yongin","M15X","HBM","advanced_DRAM"],"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_to_yellow_green_candidate","notes":"HBM leadership has sample/certification/mass production/capex evidence. Green requires full OHLC and multi-quarter HBM margin."}
{"case_id":"r2_loop16_samsung_memory_supercycle","symbol":"005930","company_name":"Samsung Electronics","case_type":"Stage3_Yellow_candidate_with_4B_overlay","primary_archetype":"MEMORY_SUPERCYCLE_ASP_STAGE2_YELLOW","best_trigger":"T0/T1","stage_candidate":"Stage3-Yellow_candidate","price_validation":{"memory_price_hike_date":"2025-11-17","max_memory_price_hike_pct":60,"ddr5_32gb_price_before_usd":149,"ddr5_32gb_price_after_usd":239,"q1_2026_op_guidance_krw_trn":57.2,"q1_2026_sales_guidance_krw_trn":133,"q1_2026_op_lseg_estimate_krw_trn":40.5,"record_profit_event_return_pct":5,"record_profit_event_price_krw":203000,"may_2026_event_return_pct":14.4,"kospi_may_2026_event_return_pct":6.45,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage3_Yellow_candidate_with_4B","notes":"Memory ASP and OP guidance are strong, but labor/HBM/geopolitical overlays remain."}
{"case_id":"r2_loop16_samsung_skhynix_openai_stargate","symbol":"005930/000660","company_name":"Samsung Electronics / SK Hynix","case_type":"Stage2_promote_candidate","primary_archetype":"OPENAI_STARGATE_HBM_DEMAND_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2025-10-02","samsung_event_return_pct":4.7,"sk_hynix_event_return_pct":12.0,"kospi_event_return_pct":3.0,"combined_market_cap_addition_usd_bn":37,"stargate_project_value_usd_bn":500,"korea_data_center_capacity_mw_each":20,"openai_dram_wafer_demand_monthly_context":900000,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_demand_trigger","notes":"OpenAI/Stargate is major demand evidence, but binding purchase order and ASP are missing."}
{"case_id":"r2_loop16_samsung_foundry_165b_contract","symbol":"005930","company_name":"Samsung Electronics","case_type":"Stage2_with_yield_4B","primary_archetype":"FOUNDRY_MEGA_CONTRACT_STAGE2_WITH_YIELD_4B","best_trigger":"T1/T2","stage_candidate":"Stage2_foundry_contract","price_validation":{"trigger_date":"2025-07-28","contract_value_usd_bn":16.5,"contract_end_year":2033,"event_return_pct":3.5,"counterparty_disclosed":false,"cutting_edge_2nm_likely":false,"reason_cutting_edge_2nm_uncertain":"yield_issues","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_contract_with_4B_yield_gate","notes":"Foundry mega contract needs customer/node/yield/fab utilization before Yellow."}
{"case_id":"r2_loop16_hanmi_semiconductor_hbm_equipment","symbol":"042700","company_name":"Hanmi Semiconductor","case_type":"Stage2_Actionable_with_4B_rumor_overlay","primary_archetype":"ADVANCED_PACKAGING_EQUIPMENT_STAGE2_WITH_RUMOR_4B","best_trigger":"T0/T1","stage_candidate":"Stage2-Actionable + 4B-watch","price_validation":{"trigger_date":"2024-03-26/2024-03-28","hanmi_event_return_pct":16,"sk_hynix_event_return_pct":4.3,"kospi_event_return_pct":0.7,"market_relative_return_pp":15.3,"skhynix_contract_krw_bn":21.48,"recent_contracts_total_krw_bn":200,"possible_micron_report_intraday_return_pct":22,"micron_deal_confirmed":false,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_Actionable_but_rumor_4B","notes":"Signed SK Hynix HBM equipment orders are actionable; possible Micron deal is rumor until confirmed."}
{"case_id":"r2_loop16_samsung_hbm_delay_false_positive","symbol":"005930","company_name":"Samsung Electronics","case_type":"4C_watch_HBM_certification_delay","primary_archetype":"HBM_CERTIFICATION_DELAY_FALSE_POSITIVE","best_trigger":"T0/T1","stage_candidate":"4C-watch","price_validation":{"t0_date":"2024-05-24","t0_event_return_pct":-2,"issue":"HBM3_HBM3E_Nvidia_test_delay","reported_failure_reasons":["heat","power_consumption"],"samsung_disputed_specific_claims":true,"t1_date":"2025-07-08","q2_2025_op_guidance_krw_trn":4.6,"q2_2025_op_lseg_estimate_krw_trn":6.2,"q2_2025_op_yoy_pct":-56,"chip_division_op_decline_context":">90%","t1_event_return_pct":-0.2,"kospi_same_context_pct":1.2,"market_relative_return_pp":-1.4},"score_price_alignment":"thesis_break_watch","notes":"HBM certification delay and profit miss are 4C-watch, not Stage2 promotion."}
{"case_id":"r2_loop16_china_fab_export_control","symbol":"005930/000660/067310/042700","company_name":"Samsung / SK Hynix / Hana Micron / Hanmi Semiconductor","case_type":"4C_watch_trade_policy","primary_archetype":"CHINA_FAB_EXPORT_CONTROL_4C_WATCH","best_trigger":"T1/T2","stage_candidate":"4C-watch","price_validation":{"trigger_date":"2025-09-01","samsung_event_return_pct":-2.3,"sk_hynix_event_return_pct":-4.4,"kospi_same_context_pct":-0.7,"samsung_market_relative_pp":-1.6,"skhynix_market_relative_pp":-3.7,"hana_micron_event_return_pct":-1.7,"hanmi_event_return_pct":-4.4,"samsung_china_dram_output_share":">33%","skhynix_china_dram_nand_output_share_pct":"30-40","policy_effective_delay_days":120},"score_price_alignment":"thesis_break_watch","notes":"China fab license revocation is technology-upgrade ceiling and R2 4C-watch."}
{"case_id":"r2_loop16_samsung_labor_strike_4c","symbol":"005930","company_name":"Samsung Electronics","case_type":"4C_watch_labor_output_risk","primary_archetype":"SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH","best_trigger":"T1/T2","stage_candidate":"4C-watch","price_validation":{"t1_date":"2026-05-15","event_return_pct":-9.3,"planned_strike_duration_days":18,"potential_workers":">50000","t2_date":"2026-05-19","potential_workers_updated":48000,"essential_workers_required":7087,"potential_dram_supply_cut_pct":"3-4","potential_nand_supply_cut_pct":"2-3","potential_chip_production_loss_krw_trn":30,"potential_chip_production_loss_usd_bn":19.9},"score_price_alignment":"thesis_break_watch","notes":"Labor strike can disrupt DRAM/NAND output and delivery reliability; treat as 4C-watch."}
{"case_id":"r2_loop16_lg_innotek_aeva_lidar","symbol":"011070","company_name":"LG Innotek / Aeva","case_type":"Stage2_component_diversification","primary_archetype":"ELECTRONIC_COMPONENT_LIDAR_STAGE2_ORDER_GATE","best_trigger":"T1/T2","stage_candidate":"Stage2","price_validation":{"trigger_date":"2025-07-29","strategic_collaboration_value_usd_mn":50,"lg_innotek_equity_investment_usd_mn":32,"stake_pct_context":"single_digit","target_markets":["vehicles","industrial_equipment","robotics","consumer_electronics","AR_headsets"],"direct_krx_price_anchor":"price_data_unavailable_after_deep_search"},"score_price_alignment":"success_candidate_stage2","notes":"Lidar/sensor diversification is Stage2; design-in and revenue are required for Yellow."}
```

## data/e2r_trigger_calibration/triggers_r2_loop16_round238.jsonl 초안

```jsonl
{"trigger_id":"r2l16_skhynix_hbm4_T1","case_id":"r2_loop16_sk_hynix_hbm3e_hbm4_euv","trigger_type":"Stage3-Yellow_candidate","trigger_date":"2025-09-12","evidence_available":"SK Hynix completed HBM4 internal certification and established production system; shares +7.3% vs KOSPI +1.2%","event_return_pct":7.3,"market_relative_return_pp":6.1,"trigger_outcome_label":"excellent_stage2_to_yellow_candidate","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r2l16_skhynix_asml_T2","case_id":"r2_loop16_sk_hynix_hbm3e_hbm4_euv","trigger_type":"capacity_validation","trigger_date":"2026-03-24","evidence_available":"SK Hynix orders 11.95T won / $7.97B ASML EUV tools for Yongin/M15X HBM and advanced DRAM; shares +5.7%","event_return_pct":5.7,"trigger_outcome_label":"capacity_validation","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r2l16_samsung_memory_T1","case_id":"r2_loop16_samsung_memory_supercycle","trigger_type":"Stage3-Yellow_candidate","trigger_date":"2026-04-07","evidence_available":"Samsung Q1 2026 OP guidance 57.2T won, sales 133T won, far above estimates; shares +5% to 203,000 won","event_return_pct":5,"trigger_outcome_label":"memory_supercycle_yellow_candidate","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r2l16_openai_stargate_T1","case_id":"r2_loop16_samsung_skhynix_openai_stargate","trigger_type":"Stage2-Actionable","trigger_date":"2025-10-02","evidence_available":"OpenAI Stargate partnership; Samsung +4.7%, SK Hynix +12%, KOSPI +3%, combined market cap +$37B","event_return_pct":"Samsung +4.7 / SK Hynix +12","trigger_outcome_label":"excellent_stage2_actionable_demand_trigger","promote_to":"Stage2-Actionable"}
{"trigger_id":"r2l16_samsung_foundry_T1","case_id":"r2_loop16_samsung_foundry_165b_contract","trigger_type":"Stage2_contract_with_4B","trigger_date":"2025-07-28","evidence_available":"Samsung signs $16.5B foundry deal with unnamed global company; shares +3.5%; node/customer/yield not disclosed","event_return_pct":3.5,"trigger_outcome_label":"Stage2_foundry_contract_with_yield_gate","promote_to":"Stage2"}
{"trigger_id":"r2l16_hanmi_hbm_T0","case_id":"r2_loop16_hanmi_semiconductor_hbm_equipment","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-26","evidence_available":"Hanmi supplies SK Hynix HBM advanced packaging equipment; Hanmi +16%, SK Hynix +4.3%, KOSPI +0.7%; KRW21.48B SK Hynix contract and around KRW200B recent contracts","event_return_pct":16,"market_relative_return_pp":15.3,"trigger_outcome_label":"Stage2_Actionable_equipment_order","promote_to":"Stage2-Actionable"}
{"trigger_id":"r2l16_hanmi_micron_rumor_T2","case_id":"r2_loop16_hanmi_semiconductor_hbm_equipment","trigger_type":"4B_rumor_watch","trigger_date":"2024-03-28","evidence_available":"Media reports possible Micron HBM equipment deal; Hanmi up to +22%, but no confirmation from Hanmi or Micron","event_return_pct":22,"trigger_outcome_label":"rumor_4B_watch","promote_to":"4B-watch"}
{"trigger_id":"r2l16_samsung_hbm_delay_T0","case_id":"r2_loop16_samsung_hbm_delay_false_positive","trigger_type":"4C-watch","trigger_date":"2024-05-24","evidence_available":"Reuters sources say Samsung HBM3/HBM3E failed Nvidia tests due heat/power issues; shares -2%; Samsung disputes specific claims","event_return_pct":-2,"trigger_outcome_label":"HBM_certification_delay_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r2l16_china_fab_export_T1","case_id":"r2_loop16_china_fab_export_control","trigger_type":"4C-watch","trigger_date":"2025-09-01","evidence_available":"U.S. revokes authorizations for Samsung/SK Hynix China fabs; Samsung -2.3%, SK Hynix -4.4%, KOSPI -0.7%","event_return_pct":"Samsung -2.3 / SK Hynix -4.4","trigger_outcome_label":"trade_policy_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r2l16_samsung_strike_T1","case_id":"r2_loop16_samsung_labor_strike_4c","trigger_type":"4C-watch","trigger_date":"2026-05-15","evidence_available":"Samsung union sticks to 18-day strike plan; shares slide 9.3%; DRAM/NAND output risk","event_return_pct":-9.3,"trigger_outcome_label":"labor_output_4C_watch","promote_to":"4C-watch"}
{"trigger_id":"r2l16_lginnotek_aeva_T1","case_id":"r2_loop16_lg_innotek_aeva_lidar","trigger_type":"Stage2_component_diversification","trigger_date":"2025-07-29","evidence_available":"LG Innotek $32M equity investment in Aeva as part of $50M lidar strategic collaboration; design-in/revenue not yet confirmed","event_return_pct":"price_data_unavailable_after_deep_search","trigger_outcome_label":"Stage2_component_order_gate","promote_to":"Stage2"}
```

## data/sector_taxonomy/score_weight_profiles_round238_r2_loop16_v1.csv 초안

```csv
archetype,hbm_customer_certification,hbm_mass_production_shipment,memory_asp_contract_power,op_estimate_guidance_beat,euv_capacity_commitment,advanced_packaging_order_visibility,binding_ai_infra_purchase,export_license_stability,labor_output_continuity,hbm_headline_without_customer_certification_penalty,foundry_contract_without_node_yield_penalty,ai_partnership_without_binding_order_penalty,equipment_rumor_without_signed_order_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
HBM_LEADERSHIP_STAGE2_TO_GREEN_CANDIDATE,+5,+5,+4,+4,+4,+2,+3,+3,+2,-5,-1,-2,-1,certification+mass production+EUV,volume shipment/margin pending,HBM volume+margin+favorable OHLC,SK Hynix template.
MEMORY_SUPERCYCLE_ASP_STAGE2_YELLOW,+2,+3,+5,+5,+2,+0,+2,+2,+3,-3,-1,-1,-1,ASP hike+OP guidance,labor/export/energy overlay,ASP+OP+margin+OHLC,Samsung memory template.
OPENAI_STARGATE_HBM_DEMAND_STAGE2_ACTIONABLE,+2,+2,+3,+2,+1,+1,+5,+1,+1,-2,-1,-4,-1,OpenAI demand signal,binding PO missing,wafer allocation+ASP+delivery,Samsung/SK OpenAI.
FOUNDRY_MEGA_CONTRACT_STAGE2_WITH_YIELD_4B,+0,+0,+1,+2,+3,+0,+1,+2,+1,-1,-5,-1,-1,foundry contract,customer/node/yield missing,utilization+yield+margin,Samsung foundry $16.5B.
ADVANCED_PACKAGING_EQUIPMENT_STAGE2_WITH_RUMOR_4B,+2,+2,+1,+2,+1,+5,+1,+1,+1,-2,-1,-1,-5,signed equipment orders,customer diversification/margin pending,repeat orders+margin,Hanmi HBM equipment.
HBM_CERTIFICATION_DELAY_FALSE_POSITIVE,-5,-4,+0,-4,+0,+0,+0,+2,+1,-5,-1,-1,-1,qualification failure/profit miss,relief certification pending,N/A,Samsung HBM delay.
CHINA_FAB_EXPORT_CONTROL_4C_WATCH,+0,+0,+0,+0,+0,+1,+0,+5,+1,-1,-2,-1,-1,license revocation,maintenance license relief pending,N/A,China fab export curbs.
SEMICONDUCTOR_LABOR_STRIKE_4C_WATCH,+0,+0,+2,-3,+0,+0,+0,+1,+5,-1,-1,-1,-1,strike output risk,settlement pending,N/A,Samsung labor strike.
ELECTRONIC_COMPONENT_LIDAR_STAGE2_ORDER_GATE,+0,+1,+1,+1,+0,+0,+0,+1,+1,-1,-1,-1,-1,strategic lidar partnership,design-in/revenue missing,design-in+mass order+margin,LG Innotek/Aeva.
```

---

# 이번 R2 Loop 16 결론

```text
1. SK Hynix HBM은 R2의 가장 강한 structural success다.
   HBM3E mass production, HBM4 certification, ASML EUV capex가 이어졌고 주가반응도 강했다.

2. Samsung memory supercycle은 Stage3-Yellow 후보로 올릴 수 있다.
   DDR5/DRAM 가격 인상과 record OP guidance가 닫혔다. 다만 labor/HBM/export risk는 4B/4C overlay다.

3. OpenAI Stargate는 Stage2-Actionable이다.
   Samsung +4.7%, SK Hynix +12%는 강하지만, binding wafer order와 ASP 전에는 Green이 아니다.

4. Samsung foundry $16.5B deal은 Stage2다.
   계약은 크지만 customer/node/yield/fab utilization이 없으면 Yellow가 아니다.

5. Hanmi Semiconductor는 Stage2-Actionable이다.
   SK Hynix HBM equipment order는 강하지만, Micron rumor는 4B로 분리해야 한다.

6. Samsung HBM delay는 4C-watch다.
   Nvidia qualification delay와 profit miss는 HBM headline에 반대되는 hard overlay다.

7. China fab export-control은 R2 4C-watch다.
   China DRAM/NAND exposure와 upgrade ceiling이 크다.

8. Samsung labor strike는 R2 4C-watch다.
   DRAM/NAND supply와 고객 납기 신뢰를 흔들 수 있다.

9. LG Innotek/Aeva는 Stage2 component diversification이다.
   lidar·robotics·AR optionality는 있지만 design-in/revenue 전에는 Green이 아니다.
```

한 문장으로 압축하면:

> **R2 Loop 16에서 배운 핵심은 “AI 반도체 headline”이 아니라, HBM customer certification, mass production, ASP, OP guidance, EUV capacity, packaging equipment orders, binding AI infrastructure purchase가 닫혀야 Stage3로 올릴 수 있다는 것이다. 반대로 foundry contract without yield, equipment rumor, OpenAI LOI, HBM delay, China fab export-control, labor strike는 반드시 4B/4C로 분리해야 한다.**

[1]: https://www.reuters.com/technology/nvidia-supplier-sk-hynix-says-begins-mass-production-12-layer-hbm3e-chips-2024-09-26/?utm_source=chatgpt.com "Nvidia supplier SK Hynix's shares rally as mass production of latest HBM chips begins"
[2]: https://www.reuters.com/world/china/samsung-hikes-memory-chip-prices-by-up-60-shortage-worsens-sources-say-2025-11-14/?utm_source=chatgpt.com "Samsung hikes memory chip prices by up to 60% as shortage worsens, sources say"
[3]: https://www.reuters.com/world/asia-pacific/south-koreas-kospi-share-index-tops-7000-first-time-2026-05-06/?utm_source=chatgpt.com "Korea's KOSPI breaks 7,000 as AI rally catapults Samsung into $1 trillion club"
[4]: https://www.reuters.com/world/asia-pacific/samsung-sk-hynix-shares-rally-openai-partnerships-2025-10-02/?utm_source=chatgpt.com "Samsung, SK Hynix shares leap after OpenAI chip deal"
[5]: https://www.reuters.com/business/samsung-elec-signs-165-billion-deal-make-chips-global-firm-2025-07-28/?utm_source=chatgpt.com "Samsung Elec signs $16.5 billion deal to make chips for global firm"
[6]: https://www.wsj.com/articles/south-korean-chip-shares-rally-as-ai-frenzy-persists-260f9996?utm_source=chatgpt.com "South Korean Chip Shares Rally as AI Frenzy Persists"
[7]: https://www.wsj.com/articles/hanmi-semiconductor-climbs-after-media-reports-of-possible-deal-with-micron-e85398fb?utm_source=chatgpt.com "Hanmi Semiconductor Climbs After Media Reports of Possible Deal With Micron"
[8]: https://www.reuters.com/technology/samsungs-hbm-chips-failing-nvidia-tests-due-heat-power-consumption-woes-sources-2024-05-23/?utm_source=chatgpt.com "Samsung's HBM chips failing Nvidia tests due to heat and power consumption woes, sources say"
[9]: https://www.reuters.com/world/china/shares-samsung-sk-hynix-drop-after-us-makes-it-harder-make-chips-china-2025-09-01/?utm_source=chatgpt.com "Shares in Samsung, SK Hynix drop after US makes it harder to make chips in China"
[10]: https://www.reuters.com/business/world-at-work/samsung-elecs-union-says-samsung-proposed-unconditional-talks-strike-plan-holds-2026-05-15/?utm_source=chatgpt.com "Samsung's South Korean union sticks to strike plan after talks offer; shares slide"
[11]: https://www.reuters.com/world/asia-pacific/lg-innotek-take-stake-lidar-maker-aeva-part-50-million-deal-2025-07-29/?utm_source=chatgpt.com "LG Innotek to take stake in lidar maker Aeva as part of $50 million deal"

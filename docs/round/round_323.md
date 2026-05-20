순서상 이번은 **R2 Loop 17 — AI·반도체·전자부품 trigger-level price validation 라운드**다.

이번 R2는 **HBM, DRAM/NAND supercycle, AI data center demand, packaging equipment, Samsung HBM catch-up, U.S.-China export control, Samsung labor disruption**을 따로 본다. 핵심은 “AI 반도체”라는 말 자체가 아니라, **고객 인증 → 양산 → 수주/wafer demand → ASP·margin → capex·yield → 규제·노동·중국 fab risk**가 어느 지점에서 가격을 움직였는지다.

```text
round = R2 Loop 17
round_id = round_251
large_sector = AI_SEMICONDUCTOR_ELECTRONIC_COMPONENTS
method = trigger_level_backtest_v1_after_redteam
price_validation_completed = partial_with_reported_event_price_anchors
full_adjusted_ohlc_complete = false
production_scoring_changed = false
shadow_weight_only = true
next_round = R3 Loop 17
```

이번에도 현재 도구 환경에서는 KRX/Naver/Yahoo/Stooq의 수정주가 일봉 OHLC 원본을 안정적으로 확보하지 못했다. 그래서 MFE/MAE 숫자는 만들지 않는다. 대신 Reuters/FT/WSJ/MarketWatch/AP의 **reported event return, event price, contract/order context, qualification/production trigger, export-control selloff, user/supply disruption data**를 가격 anchor로 쓴다. 즉 MFE/MAE field는 `price_data_unavailable_after_deep_search`로 명시한다.

---

# 1. 이번 라운드 대섹터

```text
R2 = AI·반도체·전자부품
```

R2의 core gate는 아래다.

```text
HBM / AI memory:
HBM certification → mass production → Nvidia/AMD/OpenAI demand → wafer allocation → ASP → DRAM mix → margin → capex/yield

Memory supercycle:
AI server demand → HBM capacity absorption → conventional DRAM/NAND shortage → price hikes → earnings → overheat/commodity reversal

Packaging / HBM equipment:
HBM capacity ramp → TC bonder / TSV / packaging equipment orders → customer concentration → repeat order → margin

Samsung catch-up:
HBM3E/HBM4 qualification → Nvidia/AMD supply → Samsung share recovery → margin → labor/yield/export-control 4B

China export control:
U.S. equipment license / VEU revocation → China fab maintenance vs upgrade risk → memory supply → capex restriction → share-price drawdown

Labor / supply disruption:
strike threat → DRAM/NAND supply disruption → bonus/labor-cost reset → margin / production risk
```

---

# 2. 대상 canonical archetype

```text
HBM_FIRST_MOVER_STAGE2_ACTIONABLE
HBM4_CERTIFICATION_STAGE3_YELLOW_CANDIDATE
OPENAI_STARGATE_MEMORY_DEMAND_STAGE2_ACTIONABLE
SAMSUNG_HBM_CATCHUP_STAGE2_WITH_LABOR_4B
HBM_PACKAGING_EQUIPMENT_STAGE2_ACTIONABLE
MEMORY_EARNINGS_GOOD_BUT_PRICE_FAILED
CHINA_EXPORT_CONTROL_4B
LABOR_SUPPLY_DISRUPTION_4B
```

---

# 3. deep sub-archetype

```text
SK Hynix / HBM3E:
- 12-layer HBM3E mass production began in Sep 2024.
- SK Hynix shares rose more than 9%, while KOSPI rose 1.7%.
- Capacity was 50% higher than previous eight-layer chips.
- Stage2-Actionable.

SK Hynix / HBM4:
- internal HBM4 certification completed Sep 2025.
- shares rose as much as 7.3%, KOSPI +1.2%.
- early HBM4 supply may preserve HBM share in low-60% range in 2026.
- Stage3-Yellow candidate, not Green until customer orders/yield/margin.

OpenAI Stargate memory LOI:
- SK Hynix and Samsung signed letter of intent with OpenAI for $500B Stargate AI data center supply.
- SK Hynix +12% intraday / +10% close, Samsung +5% intraday / +3.5% close.
- SK Hynix said OpenAI demand could be up to 900,000 DRAM wafers per month, more than 2x current HBM industry capacity.
- Stage2-Actionable demand shock, LOI/finality 4B.

Samsung HBM catch-up:
- Samsung plans HBM4 production for Nvidia supply; shares +2.2%, SK Hynix -2.9%.
- Samsung/AMD MoU focuses on HBM4 for AMD MI455X and optimized DDR5 for EPYC; also exploring foundry partnership.
- Samsung HBM share still trails SK Hynix, with Samsung around 22% vs SK Hynix around 57%.
- Stage2 catch-up, not Green until large-volume orders/yield/margin.

Hanmi Semiconductor:
- Mar 2024 AI chip rally: SK Hynix +4.3%, Hanmi Semiconductor +16%, KOSPI +0.7%.
- Hanmi supplies SK Hynix with advanced HBM packaging equipment such as TSV-TC bonders.
- Hanmi had KRW21.48B SK Hynix supply deal and recent contracts around KRW200B.
- Stage2-Actionable equipment chain, but customer concentration/yield/capacity 4B.

SK Hynix earnings price-failed:
- Q4 2024 record profit KRW8.1T / $5.64B, HBM 40% of DRAM revenue.
- HBM sales forecast to double.
- shares fell 4% because commodity memory prices and Chinese competition risks were flagged.
- evidence_good_but_price_failed / 4B.

U.S. export controls:
- U.S. revoked authorizations for Samsung/SK Hynix China fabs.
- Samsung -2.3%, SK Hynix -4.4%, KOSPI -0.7%.
- Hana Micron -1.7%, Hanmi Semiconductor -4.4%.
- China fabs represent over one-third of Samsung DRAM and 30~40% of SK Hynix DRAM/NAND output.
- hard 4B export-control gate.

Samsung labor:
- Samsung union strike plan triggered shares -9.3%.
- Almost 48,000 workers / later over 45,000 strike risk.
- possible global supply disruption: up to 4% DRAM and 3% NAND, depending on strike.
- labor-cost/supply 4B, not thesis break if resolved.
```

---

# 4. 선정 case 요약

| bucket                                 | case                                     | 핵심 판정                                                    |
| -------------------------------------- | ---------------------------------------- | -------------------------------------------------------- |
| structural_success / Stage2-Actionable | SK Hynix HBM3E mass production           | +9%+, KOSPI +1.7%, 12-layer HBM3E 양산                     |
| Stage3-Yellow candidate                | SK Hynix HBM4 certification              | +7.3%, KOSPI +1.2%, HBM4 first-mover                     |
| Stage2-Actionable                      | OpenAI Stargate memory LOI               | SK +10% close, Samsung +3.5%, 900k DRAM wafers/mo demand |
| Stage2 catch-up + 4B                   | Samsung HBM4 / Nvidia / AMD              | +2.2%, Nvidia/AMD HBM4 route, labor/yield/share gap 4B   |
| Stage2-Actionable equipment            | Hanmi Semiconductor TC bonder            | Hanmi +16%, SK Hynix +4.3%, SK Hynix supply deals        |
| evidence_good_but_price_failed         | SK Hynix record profit                   | KRW8.1T OP, HBM 40% DRAM revenue, but shares -4%         |
| 4B / thesis-risk                       | U.S. China fab export-control revocation | Samsung -2.3%, SKH -4.4%, Hanmi -4.4%, Hana Micron -1.7% |
| 4B labor/supply                        | Samsung strike risk                      | Samsung -9.3%, possible 4% DRAM/3% NAND supply impact    |

---

# 5. 각 case별 trigger grid

## Case A — SK Hynix 12-layer HBM3E mass production

```text
symbol = 000660
case_type = Stage2-Actionable HBM first mover
archetype = HBM_FIRST_MOVER_STAGE2_ACTIONABLE
```

| trigger |                    type | date       | 당시 공개 evidence                                                                         | 가격 anchor                  | outcome |
| ------- | ----------------------: | ---------- | -------------------------------------------------------------------------------------- | -------------------------- | ------- |
| T0      |               awareness | 2024H1     | Nvidia AI server demand, HBM bottleneck, SK Hynix HBM leadership                       | no entry                   |         |
| T1      |       Stage2-Actionable | 2024-09-26 | 12-layer HBM3E mass production 시작                                                      | SK Hynix +9%+, KOSPI +1.7% |         |
| T2      |              validation | 2024-09-26 | 12-layer HBM3E capacity 50% higher than eight-layer chips                              | same                       |         |
| T3      | Stage3-Yellow candidate | 2024~2025  | customer shipment and premium HBM mix 확대                                               | yield/margin missing       |         |
| T4      |                4B-watch | 2024~      | HBM yield, capacity allocation, conventional DRAM displacement, customer concentration | no full OHLC               |         |
| T5      |            Stage3-Green | N/A        | customer-specific order/margin and full MFE/MAE unavailable                            | 보류                         |         |

SK Hynix의 12-layer HBM3E mass production은 R2의 가장 명확한 Stage2-Actionable이다. Reuters는 SK Hynix가 12-layer HBM3E 양산을 시작했다고 보도했고, 주가는 9% 이상 상승했으며 KOSPI는 1.7% 상승했다. 이 제품은 기존 8-layer보다 capacity가 50% 높고, SK Hynix는 Nvidia AI accelerator의 핵심 HBM 공급자라는 점에서 가격 반응이 단순 기대가 아니라 **제품 양산 trigger**에 붙었다. 다만 Green은 고객별 order visibility, yield, ASP/margin이 닫혀야 한다. ([Reuters][1])

```json
{
  "case_id": "r2_loop17_sk_hynix_hbm3e_mass_production",
  "symbol": "000660",
  "best_trigger": "T1/T2",
  "best_trigger_type": "Stage2-Actionable_HBM_first_mover",
  "trigger_date": "2024-09-26",
  "event_return_pct": ">9",
  "kospi_same_context_pct": 1.7,
  "product": "12-layer_HBM3E",
  "capacity_uplift_vs_8_layer_pct": 50,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "customer_order_volume",
    "HBM_yield",
    "HBM_ASP",
    "gross_margin",
    "capacity_allocation",
    "full_OHLC_MFE_MAE"
  ],
  "trigger_outcome_label": "excellent_stage2_actionable_HBM_mass_production"
}
```

---

## Case B — SK Hynix HBM4 internal certification / mass-production readiness

```text
symbol = 000660
case_type = Stage3-Yellow candidate
archetype = HBM4_CERTIFICATION_STAGE3_YELLOW_CANDIDATE
```

| trigger |                    type | date       | 당시 공개 evidence                                                             | 가격 anchor                   | outcome |
| ------- | ----------------------: | ---------- | -------------------------------------------------------------------------- | --------------------------- | ------- |
| T0      |         Stage2 evidence | 2025-03    | HBM4 12-layer samples shipped to customers                                 | no price                    |         |
| T1      | Stage3-Yellow candidate | 2025-09-12 | HBM4 internal certification completed, production system established       | SK Hynix +7.3%, KOSPI +1.2% |         |
| T2      |              validation | 2025-09-12 | analyst expects low-60% HBM market share in 2026                           | same                        |         |
| T3      |                4B-watch | 2025~2026  | customer-specific base die increases lock-in but also execution complexity | no full OHLC                |         |
| T4      |            Stage3-Green | N/A        | Nvidia/major customer confirmed volume, yield, margin not available        | 보류                          |         |

HBM4 certification은 단순 Stage2보다 한 단계 위다. Reuters는 SK Hynix가 HBM4 internal certification을 완료하고 customer production system을 갖췄다고 보도했고, 주가는 장중 7.3% 올라 record high를 찍었으며 KOSPI는 1.2% 상승했다. 특히 HBM4는 customer-specific logic/base die 구조 때문에 대체가 어려워지는 lock-in 특성이 있어 Yellow 후보로 올릴 수 있다. 다만 Green은 Nvidia/major customer별 volume, yield, margin이 닫혀야 한다. ([Reuters][2])

```json
{
  "case_id": "r2_loop17_sk_hynix_hbm4_certification",
  "symbol": "000660",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage3-Yellow_candidate_HBM4_certification",
  "trigger_date": "2025-09-12",
  "event_return_pct": 7.3,
  "kospi_same_context_pct": 1.2,
  "product": "12-layer_HBM4",
  "expected_hbm_share_2026_context": "low_60pct_range",
  "customer_specific_base_die": true,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_green_gate_missing": [
    "Nvidia_or_top_customer_confirmed_volume",
    "yield",
    "HBM4_ASP",
    "gross_margin",
    "capacity_ramp",
    "full_OHLC_MFE_MAE"
  ],
  "trigger_outcome_label": "Stage3_Yellow_candidate_HBM4_first_mover"
}
```

---

## Case C — OpenAI Stargate memory LOI / SK Hynix and Samsung

```text
symbols = 000660 / 005930
case_type = Stage2-Actionable AI memory demand shock
archetype = OPENAI_STARGATE_MEMORY_DEMAND_STAGE2_ACTIONABLE
```

| trigger |              type | date       | 당시 공개 evidence                                                                 | 가격 anchor                                                         | outcome |
| ------- | ----------------: | ---------- | ------------------------------------------------------------------------------ | ----------------------------------------------------------------- | ------- |
| T0      |         awareness | 2025       | Stargate / AI data center capex 확대                                             | no entry                                                          |         |
| T1      | Stage2-Actionable | 2025-10-02 | SK Hynix and Samsung sign LOI with OpenAI for $500B Stargate supply            | SK +12% intraday / +10% close, Samsung +5% intraday / +3.5% close |         |
| T2      |        validation | 2025-10-02 | OpenAI demand up to 900,000 DRAM wafers/mo, more than 2x HBM industry capacity | same                                                              |         |
| T3      |          4B-watch | 2025~      | LOI not final contract, wafer allocation/capacity/yield uncertain              | 4B                                                                |         |
| T4      |     Stage3-Yellow | N/A        | binding orders, pricing, margin not confirmed                                  | 보류                                                                |         |

OpenAI Stargate LOI는 R2에서 “Stage2를 놓치면 안 되는” demand shock다. FT는 SK Hynix와 Samsung이 OpenAI의 $500B Stargate data center project에 semiconductor를 공급하기 위한 LOI를 체결했고, SK Hynix는 장중 +12%, 종가 +10%, Samsung은 장중 약 +5%, 종가 +3.5% 상승했다고 보도했다. SK Hynix는 OpenAI의 HBM demand가 월 900,000 DRAM wafers까지 갈 수 있다고 했고, 이는 현재 HBM industry capacity의 2배 이상이라는 설명도 붙었다. 하지만 LOI는 final order가 아니라서 4B를 붙인다. ([Financial Times][3])

```json
{
  "case_id": "r2_loop17_openai_stargate_memory_loi",
  "symbols": "000660/005930",
  "best_trigger": "T1/T3",
  "best_trigger_type": "Stage2-Actionable_AI_memory_demand_shock_with_LOI_4B",
  "trigger_date": "2025-10-02",
  "project_value_context_usd_bn": 500,
  "sk_hynix_intraday_return_pct": 12,
  "sk_hynix_close_return_pct": 10,
  "samsung_intraday_return_pct": 5,
  "samsung_close_return_pct": 3.5,
  "openai_dram_wafer_demand_per_month": 900000,
  "demand_vs_current_hbm_capacity": ">2x",
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "4B_overlay": [
    "LOI_not_binding_final_order",
    "capacity_allocation",
    "yield",
    "pricing",
    "delivery_schedule"
  ],
  "trigger_outcome_label": "excellent_stage2_actionable_demand_shock_with_4B"
}
```

---

## Case D — Samsung Electronics HBM catch-up / Nvidia HBM4 and AMD MoU

```text
symbol = 005930
case_type = Stage2 catch-up + labor/yield 4B
archetype = SAMSUNG_HBM_CATCHUP_STAGE2_WITH_LABOR_4B
```

| trigger |            type | date       | 당시 공개 evidence                                                                                    | 가격 anchor                                | outcome |
| ------- | --------------: | ---------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------- |
| T0      | Stage2 catch-up | 2026-01-26 | Samsung to start HBM4 production for Nvidia supply, source says                                   | Samsung +2.2%, SK Hynix -2.9%            |         |
| T1      |      validation | 2026-03-18 | Samsung and AMD sign MoU for HBM4 on AMD MI455X and DDR5 for EPYC; foundry partnership discussion | no direct price                          |         |
| T2      |        4B-watch | 2026       | Samsung HBM share 22% vs SK Hynix 57%; volume/yield still gate                                    | 4B                                       |         |
| T3      |        labor 4B | 2026-05    | union strike risk / bonus dispute                                                                 | shares -9.3% on strike-plan continuation |         |
| T4      |   Stage3-Yellow | N/A        | large-volume Nvidia/AMD shipments and yield/margin not confirmed                                  | 보류                                       |         |

Samsung HBM catch-up는 Stage2다. Reuters는 Samsung이 HBM4 production을 시작해 Nvidia에 공급할 계획이라는 source-based 보도를 냈고, Samsung shares는 2.2% 상승한 반면 SK Hynix는 2.9% 하락했다. 이후 Samsung과 AMD는 AI memory 협력을 위한 MoU를 체결했고, Samsung HBM4는 AMD MI455X에, optimized DDR5는 EPYC에 들어갈 수 있는 방향이 제시됐다. 하지만 Samsung의 HBM share는 약 22%로 SK Hynix 57%보다 낮고, strike/labor-cost 리스크까지 붙었다. 따라서 Green은 아직 아니다. ([Reuters][4])

```json
{
  "case_id": "r2_loop17_samsung_hbm_catchup_nvidia_amd",
  "symbol": "005930",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2_HBM_catchup_with_labor_4B",
  "nvidia_trigger_date": "2026-01-26",
  "samsung_event_return_pct": 2.2,
  "sk_hynix_same_context_return_pct": -2.9,
  "amd_mou_date": "2026-03-18",
  "amd_product_context": "Instinct_MI455X_HBM4_and_EPYC_DDR5",
  "samsung_hbm_share_context_pct": 22,
  "sk_hynix_hbm_share_context_pct": 57,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "large_volume_Nvidia_shipments",
    "AMD_order_volume",
    "HBM4_yield",
    "gross_margin",
    "labor_cost_resolution",
    "full_OHLC_MFE_MAE"
  ],
  "trigger_outcome_label": "Stage2_HBM_catchup_not_Green"
}
```

---

## Case E — Hanmi Semiconductor / HBM packaging equipment

```text
symbol = 042700
case_type = Stage2-Actionable HBM equipment chain
archetype = HBM_PACKAGING_EQUIPMENT_STAGE2_ACTIONABLE
```

| trigger |                      type | date       | 당시 공개 evidence                                                                        | 가격 anchor                               | outcome |
| ------- | ------------------------: | ---------- | ------------------------------------------------------------------------------------- | --------------------------------------- | ------- |
| T0      | Stage2 equipment evidence | 2024-03-26 | AI chip rally; Hanmi supplies SK Hynix with TSV-TC bonders for HBM packaging          | Hanmi +16%, SK Hynix +4.3%, KOSPI +0.7% |         |
| T1      |                validation | 2024-03    | Hanmi signed KRW21.48B supply deal with SK Hynix; recent contract wins around KRW200B | same                                    |         |
| T2      |   Stage3-Yellow candidate | 2024~      | repeat SK Hynix/TSMC/Nvidia onshore HBM supply-chain opportunity                      | customer concentration gate             |         |
| T3      |                  4B-watch | 2025-09    | U.S. China fab waiver revocation selloff hits Hanmi -4.4%                             | 4B                                      |         |
| T4      |              Stage3-Green | N/A        | repeat orders, margin, customer diversification not confirmed                         | 보류                                      |         |

Hanmi Semiconductor는 R2에서 SK Hynix/Samsung 본주보다 더 “소부장 trigger”에 가깝다. WSJ는 2024년 3월 AI chip rally에서 Hanmi Semiconductor가 +16%, SK Hynix가 +4.3%, KOSPI가 +0.7%였다고 보도했다. Hanmi는 SK Hynix에 HBM packaging 장비인 TSV-TC bonder를 공급하며, 직전 SK Hynix와 KRW21.48B supply deal을 맺었고 최근 contract wins가 약 KRW200B였다고 설명했다. 이건 Stage2-Actionable이다. 다만 고객집중, TC bonder 반복수주, margin, 중국 fab 규제 영향이 4B다. ([월스트리트저널][5])

```json
{
  "case_id": "r2_loop17_hanmi_semiconductor_hbm_packaging",
  "symbol": "042700",
  "best_trigger": "T0/T3",
  "best_trigger_type": "Stage2-Actionable_HBM_packaging_equipment",
  "trigger_date": "2024-03-26",
  "hanmi_event_return_pct": 16,
  "sk_hynix_same_context_return_pct": 4.3,
  "kospi_same_context_pct": 0.7,
  "sk_hynix_supply_deal_krw_bn": 21.48,
  "recent_contract_wins_context_krw_bn": 200,
  "equipment": "TSV_TC_bonder_for_HBM_packaging",
  "china_export_control_selloff_pct": -4.4,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "repeat_order_visibility",
    "customer_diversification",
    "gross_margin",
    "capacity",
    "export_control_impact",
    "full_OHLC_MFE_MAE"
  ],
  "trigger_outcome_label": "excellent_stage2_actionable_HBM_equipment_with_4B"
}
```

---

## Case F — SK Hynix record profit, but price failed

```text
symbol = 000660
case_type = evidence_good_but_price_failed
archetype = MEMORY_EARNINGS_GOOD_BUT_PRICE_FAILED
```

| trigger |                     type | date       | 당시 공개 evidence                                                                       | 가격 anchor    | outcome |
| ------- | -----------------------: | ---------- | ------------------------------------------------------------------------------------ | ------------ | ------- |
| T0      | Stage2 earnings evidence | 2025-01-23 | Q4 2024 OP KRW8.1T / $5.64B, surpassed Samsung quarterly profit for first time       | shares -4%   |         |
| T1      |               validation | 2025-01-23 | HBM 40% of DRAM revenue; HBM sales expected to double                                | same         |         |
| T2      |                 4B-watch | 2025-01-23 | commodity memory price declines, smartphones/PC demand weakness, Chinese competition | price failed |         |
| T3      |            Stage3-Yellow | N/A        | conventional DRAM/NAND recovery and HBM margin durability needed                     | 보류           |         |

이 case는 R2의 RedTeam 핵심이다. SK Hynix의 Q4 2024 operating profit은 KRW8.1T, $5.64B로 record였고 Samsung을 처음으로 넘어섰다. HBM은 DRAM revenue의 40%였고 HBM sales는 올해 doubling을 전망했다. 그런데 주가는 4% 하락했다. 이유는 commodity memory price decline, smartphone/PC demand, Chinese competition 리스크가 같이 제시됐기 때문이다. 즉 실적이 좋아도 가격이 실패하면 Stage3-Green을 주면 안 된다. ([Reuters][6])

```json
{
  "case_id": "r2_loop17_sk_hynix_record_profit_price_failed",
  "symbol": "000660",
  "best_trigger": "T0/T2",
  "best_trigger_type": "evidence_good_but_price_failed",
  "trigger_date": "2025-01-23",
  "operating_profit_q4_2024_krw_trn": 8.1,
  "operating_profit_q4_2024_usd_bn": 5.64,
  "hbm_share_of_dram_revenue_pct": 40,
  "hbm_sales_outlook": "double_this_year",
  "event_return_pct": -4,
  "4B_overlay": [
    "commodity_memory_price_decline",
    "smartphone_PC_demand_weakness",
    "Chinese_competition",
    "post_rally_profit_taking"
  ],
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "evidence_good_but_price_failed"
}
```

---

## Case G — U.S. China-fab export-control revocation

```text
symbols = 005930 / 000660 / 067310 / 042700
case_type = China export-control 4B
archetype = CHINA_EXPORT_CONTROL_4B
```

| trigger |            type | date       | 당시 공개 evidence                                                                                       | 가격 anchor                                  | outcome |
| ------- | --------------: | ---------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------ | ------- |
| T0      |      4B trigger | 2025-09-01 | U.S. revokes authorizations allowing Samsung/SK Hynix to obtain U.S. equipment for China chip plants | Samsung -2.3%, SK Hynix -4.4%, KOSPI -0.7% |         |
| T1      |      validation | 2025-09-01 | China >1/3 Samsung DRAM output; SK Hynix China 30~40% DRAM/NAND output                               | same                                       |         |
| T2      | supply-chain 4B | 2025-09-01 | Hana Micron -1.7%, Hanmi Semiconductor -4.4%                                                         | same                                       |         |
| T3      |          relief | 2025-12    | annual license approvals for 2026 reported later, but annual-review uncertainty remains              | no direct KRX price                        |         |
| T4      |   Stage3-Yellow | N/A        | license stability and capex/upgrade allowance needed                                                 | 보류                                         |         |

이 case는 R2에서 절대 빠지면 안 되는 4B다. Reuters는 미국이 Samsung과 SK Hynix의 중국 fab에 대한 장비 반입 authorizations를 철회했고, Samsung은 -2.3%, SK Hynix는 -4.4%, KOSPI는 -0.7%였다고 보도했다. 중국 생산 노출도도 크다. Samsung DRAM의 1/3 이상, SK Hynix DRAM/NAND의 30~40%가 중국 생산기지와 관련된다. Hana Micron은 -1.7%, Hanmi Semiconductor는 -4.4%로 후공정/장비 chain도 같이 맞았다. ([Reuters][7])

```json
{
  "case_id": "r2_loop17_us_export_control_china_fabs",
  "symbols": "005930/000660/067310/042700",
  "best_trigger": "T0/T3",
  "best_trigger_type": "4B_export_control_china_fab",
  "trigger_date": "2025-09-01",
  "samsung_event_return_pct": -2.3,
  "sk_hynix_event_return_pct": -4.4,
  "kospi_same_context_pct": -0.7,
  "hana_micron_event_return_pct": -1.7,
  "hanmi_semiconductor_event_return_pct": -4.4,
  "samsung_china_dram_output_exposure": ">1/3",
  "sk_hynix_china_dram_nand_output_exposure_pct": "30-40",
  "effective_delay_days": 120,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "stage3_gate_missing": [
    "annual_license_stability",
    "upgrade_permission",
    "China_fab_maintenance",
    "capex_shift_to_Korea",
    "supply_disruption_quantification"
  ],
  "trigger_outcome_label": "export_control_4B_success"
}
```

---

## Case H — Samsung labor strike / memory supply disruption risk

```text
symbol = 005930
case_type = labor/supply 4B
archetype = LABOR_SUPPLY_DISRUPTION_4B
```

| trigger |                    type | date       | 당시 공개 evidence                                                                              | 가격 anchor            | outcome |
| ------- | ----------------------: | ---------- | ------------------------------------------------------------------------------------------- | -------------------- | ------- |
| T0      |              4B trigger | 2026-05-15 | Samsung union sticks to 18-day strike plan after pay talks fail                             | Samsung shares -9.3% |         |
| T1      |              validation | 2026-05-19 | nearly 48,000 workers strike risk; demands include removing bonus cap and 15% OP bonus pool | no new price         |         |
| T2      | supply-chain validation | 2026-05    | potential disruption up to 4% DRAM and 3% NAND supply                                       | 4B                   |         |
| T3      |                  relief | 2026-05    | court injunction requires essential workers maintain operations; talks resume               | partial relief       |         |
| T4      |                      4C | N/A        | prolonged strike materially impairing delivery not yet confirmed                            | no hard 4C           |         |

Samsung labor dispute는 4C가 아니라 4B다. Reuters는 union이 18-day strike plan을 유지한다는 보도 이후 Samsung shares가 -9.3%였다고 전했다. 이후 Reuters는 nearly 48,000 workers가 관련되고, union이 bonus cap 제거와 15% operating profit bonus pool을 요구한다고 설명했다. 잠재적으로 DRAM 4%, NAND 3% supply disruption이 가능하다는 분석도 나왔다. 하지만 court injunction과 필수인력 유지, 협상 재개가 있어 thesis break는 아니다. 즉 **Samsung HBM catch-up Stage2에 붙는 labor/supply 4B**가 맞다. ([Reuters][8])

```json
{
  "case_id": "r2_loop17_samsung_labor_memory_supply_4b",
  "symbol": "005930",
  "best_trigger": "T0/T3",
  "best_trigger_type": "4B_labor_supply_disruption",
  "trigger_date": "2026-05-15",
  "event_return_pct": -9.3,
  "planned_strike_days": 18,
  "workers_context": "nearly_48000",
  "bonus_demand": "remove_bonus_cap_and_15pct_operating_profit_pool",
  "possible_dram_supply_impact_pct": 4,
  "possible_nand_supply_impact_pct": 3,
  "court_injunction_essential_workers": true,
  "MFE_30D": "price_data_unavailable_after_deep_search",
  "MAE_30D": "price_data_unavailable_after_deep_search",
  "trigger_outcome_label": "labor_supply_4B_not_hard_4C"
}
```

---

# 6. Trigger별 실제 가격경로 검증 요약

이번 R2 Loop 17은 full OHLC가 없으므로, 아래 표는 **reported event anchor 기준**이다.

| case                   | best trigger | entry anchor |                 event return / price |   market-relative | full MFE/MAE | outcome                        |
| ---------------------- | ------------ | -----------: | -----------------------------------: | ----------------: | ------------ | ------------------------------ |
| SK Hynix HBM3E         | T1           |        event |           SK Hynix +9%+, KOSPI +1.7% |           +7pp 이상 | unavailable  | excellent Stage2-Actionable    |
| SK Hynix HBM4          | T1           |        event |                   +7.3%, KOSPI +1.2% |            +6.1pp | unavailable  | Stage3-Yellow candidate        |
| OpenAI Stargate        | T1           |        event |   SK +10% close, Samsung +3.5% close |       unavailable | unavailable  | Stage2-Actionable + LOI 4B     |
| Samsung HBM catch-up   | T0           |        event |              Samsung +2.2%, SK -2.9% | relative reversal | unavailable  | Stage2 catch-up                |
| Hanmi Semiconductor    | T0           |        event |    Hanmi +16%, SK +4.3%, KOSPI +0.7% |     Hanmi +15.3pp | unavailable  | equipment Stage2-Actionable    |
| SK Hynix record profit | T0           |        event |                -4% despite record OP |      price failed | unavailable  | evidence_good_but_price_failed |
| U.S. export controls   | T0           |        event | Samsung -2.3%, SK -4.4%, KOSPI -0.7% |         SK -3.7pp | unavailable  | export-control 4B              |
| Samsung strike risk    | T0           |        event |                        Samsung -9.3% |       unavailable | unavailable  | labor/supply 4B                |

---

# 7. Case별 trigger 비교

## Stage 2 entry 성과

```text
가장 좋은 Stage2:
1. SK Hynix HBM3E mass production
2. OpenAI Stargate memory LOI
3. Hanmi Semiconductor HBM packaging equipment
4. Samsung HBM4 catch-up, but weaker than SK Hynix
5. SK Hynix HBM4 certification, already Yellow candidate
```

## Stage2-Actionable entry 성과

```text
Stage2-Actionable:
- SK Hynix HBM3E: +9%+, product mass-production trigger.
- OpenAI Stargate LOI: SK +10% close, demand >2x current HBM capacity context.
- Hanmi Semiconductor: +16%, direct HBM packaging-equipment supply chain.
- Samsung HBM catch-up: +2.2% only, Actionable보다는 Stage2 catch-up.

Actionable 금지:
- SK Hynix Q4 record profit if price failed.
- U.S. export-control selloff.
- Samsung labor strike risk.
```

## Stage3-Yellow 후보

```text
Yellow 후보:
- SK Hynix HBM4 certification: +7.3%, customer-specific base die, early supply advantage.
- SK Hynix OpenAI/Stargate if LOI becomes binding order and wafer allocation/pricing are confirmed.
- Hanmi Semiconductor if repeat TC bonder orders and margin continue.
- Samsung if HBM4 shipments to Nvidia/AMD become large-volume and yield improves.
```

## Stage3-Green

```text
이번 R2 Loop 17에서 확정 Green 없음.

이유:
- SK Hynix는 매우 강하지만 HBM4 customer volume/yield/margin까지 아직 field-level OHLC 검증이 없다.
- OpenAI Stargate는 LOI라 final order가 아니다.
- Samsung은 catch-up 중이고 labor/yield/share gap이 남아 있다.
- Hanmi는 equipment chain이지만 customer concentration and repeat order gate가 남아 있다.
- export-control and labor 4B가 전체 sector overlay로 남는다.
```

---

# 8. score-price alignment 판정

```text
aligned:
- SK Hynix HBM3E mass production
- SK Hynix HBM4 certification
- OpenAI Stargate LOI
- Hanmi Semiconductor TC bonder / HBM equipment rally
- U.S. export-control selloff
- Samsung labor strike selloff

Stage2_promote_candidate:
- SK Hynix HBM3E
- OpenAI Stargate memory demand
- Hanmi Semiconductor HBM equipment
- Samsung HBM catch-up, lower confidence
- HD Hyundai Electric-type AI power chain is R1, not R2, but same logic: demand must convert to backlog/margin

Stage3-Yellow candidate:
- SK Hynix HBM4 certification
- SK Hynix if OpenAI/major customer demand becomes binding
- Hanmi if repeat order/margin/customer diversification confirm

false_positive_score:
- SK Hynix record profit if promoted despite -4% price reaction
- Samsung HBM catch-up if promoted without volume/yield
- any report-only semiconductor equipment idea without price/order validation

evidence_good_but_price_failed:
- SK Hynix Q4 record profit / HBM 40% DRAM revenue but shares -4%

event_premium:
- OpenAI Stargate LOI
- Samsung Nvidia HBM4 source-based production news
- Hanmi HBM equipment rally

thesis_break_watch:
- U.S. export-control revocation
- Samsung labor strike / bonus-cost reset
- China fab capex restrictions
- commodity DRAM/NAND price reversal

hard_4C_success:
- hard 4C not confirmed in this R2 round.
- export controls and Samsung labor are strong 4B, not full thesis-break yet.
```

---

# 9. 점수비중 교정

## 올릴 축

```csv
axis,delta,reason,cases
HBM_mass_production,+5,"양산 trigger와 +9% price reaction은 Stage2-Actionable","SK Hynix HBM3E"
HBM4_certification,+5,"HBM4 인증/production system은 Yellow 후보","SK Hynix HBM4"
customer_binding_demand,+5,"OpenAI/Nvidia/AMD demand가 binding으로 닫히면 Yellow/Green","OpenAI, Samsung, SK Hynix"
HBM_wafer_allocation,+5,"wafer demand와 capacity allocation은 EPS 경로 핵심","OpenAI Stargate"
packaging_equipment_orders,+5,"TC bonder/TSV 수주는 HBM capex의 소부장 실체","Hanmi"
market_relative_return,+4,"KOSPI 대비 초과수익은 trigger quality 핵심","SK Hynix, Hanmi"
HBM_yield_margin,+5,"HBM은 yield와 ASP/margin 전까지 Green 금지","SK Hynix, Samsung"
China_fab_license_risk,+5,"중국 fab 장비 라이선스는 sector-wide 4B","Samsung, SK Hynix, Hanmi, Hana Micron"
labor_supply_stability,+4,"메모리 공급망에서 strike/labor-cost risk는 4B","Samsung"
```

## 내릴 축

```csv
axis,delta,reason,cases
earnings_without_price_validation,-5,"record profit에도 주가가 빠지면 Actionable 금지","SK Hynix Q4"
LOI_without_final_order,-4,"LOI만으로 Green 금지","OpenAI Stargate"
HBM_catchup_without_volume,-5,"Samsung catch-up은 volume/yield 전까지 Stage2","Samsung"
report_or_target_without_orders,-4,"리포트/목표가만으로 장비주 Green 금지","semiconductor equipment"
commodity_memory_ignored,-5,"HBM이 좋아도 commodity DRAM/NAND price risk 무시 금지","SK Hynix"
customer_concentration_ignored,-4,"Hanmi/SK Hynix/Nvidia chain은 고객집중 4B","Hanmi"
export_control_ignored,-5,"China fab VEU/license risk 무시하면 false positive","Samsung/SK Hynix"
labor_cost_reset_ignored,-4,"strike 이후 bonus-cost reset은 margin 4B","Samsung"
```

---

# 10. Stage2-Actionable 승격 조건

R2 Loop 17 shadow rule:

```text
R2에서 Stage2 evidence가 아래 중 4개 이상이면 Stage2-Actionable로 승격한다.

1. event return +5% 이상
2. market-relative return +5pp 이상
3. HBM/AI memory 양산, 인증, 공급계약, LOI 등 hard evidence가 있다
4. 고객 수요가 Nvidia/AMD/OpenAI 등 real buyer와 연결된다
5. 장비주는 수주금액 또는 반복수주가 확인된다
6. EPS 경로가 HBM mix, ASP, wafer allocation, margin으로 연결된다
7. export-control / labor / commodity price 4B가 없거나 식별 가능하다
```

적용:

```text
SK Hynix HBM3E:
1,2,3,4,6 충족 → Stage2-Actionable.

SK Hynix HBM4:
1,2,3,4,6 충족 → Stage3-Yellow candidate.

OpenAI Stargate:
1,3,4,6 충족. 그러나 LOI 4B → Stage2-Actionable.

Hanmi Semiconductor:
1,2,3,5,6 충족 → Stage2-Actionable.

Samsung HBM catch-up:
3,4,6 일부 충족. 1 약함, labor/yield 4B 큼 → Stage2.

SK Hynix record profit:
3,4,6 충족하지만 price failed → Actionable 금지.

U.S. export control:
negative 4B trigger → Actionable 금지.
```

---

# 11. Stage3-Yellow 조건

```text
Stage3-Yellow:
Stage2-Actionable 이후 아래 중 2개 이상이 추가로 닫히면 Yellow.

1. HBM4 또는 advanced HBM customer certification
2. confirmed volume or wafer allocation
3. premium HBM ASP / margin visibility
4. repeat order or locked-in customer-specific design
5. capacity ramp without yield issue
6. 4B risks manageable: export license, labor, commodity memory, customer concentration
```

Yellow 후보:

```text
SK Hynix HBM4:
certification + customer-specific design + first-mover share → Yellow.

OpenAI Stargate:
LOI가 binding order로 바뀌고 wafer/month allocation이 확정되면 Yellow.

Hanmi:
repeat SK Hynix/TSMC/Nvidia-linked order and margin 확인 시 Yellow.

Samsung:
HBM4 Nvidia/AMD volume shipment and yield 확인 시 Yellow.
```

---

# 12. Stage3-Green 조건

```text
Stage3-Green:
- customer order is binding and large-volume.
- HBM yield, ASP and gross margin are confirmed.
- wafer allocation expands without killing conventional DRAM/NAND profitability.
- equipment orders repeat and margins hold.
- export-control and labor 4B are resolved.
- full-window MFE/MAE is favorable.
```

이번 R2 Loop 17에서는 **Stage3-Green 확정 없음**.

```text
stage3_green_confirmed = false
reason = full OHLC unavailable + customer volume/yield/margin/export-control/labor gates not fully closed
```

---

# 13. 4B 조기감지 조건

```text
4B trigger:
- HBM evidence strong but commodity memory prices fall.
- LOI before final order.
- Samsung catch-up before volume/yield.
- HBM equipment rally before repeat order.
- China fab export-license revocation.
- labor strike / bonus-cost reset.
- customer concentration in Nvidia/SK Hynix chain.
- DRAM/NAND supply disruption or conventional memory displacement.
```

적용:

```text
SK Hynix:
record profit에도 -4%면 commodity memory 4B.

OpenAI Stargate:
LOI라 final order 4B.

Samsung:
HBM catch-up + labor strike + HBM share gap 4B.

Hanmi:
customer concentration and export-control selloff 4B.

Samsung/SK/Hana/Hanmi:
U.S. China fab authorization revocation 4B.

Samsung labor:
strike risk 4B, hard 4C는 아직 아님.
```

---

# 14. 4C hard gate 조건

```text
R2 4C:
- customer qualification failure after prior Stage2
- large-volume HBM shipment failure
- export-control blocks fab maintenance/upgrade materially
- prolonged strike disrupts memory delivery
- severe yield failure destroys margin
- major customer order cancellation
```

이번 R2 Loop 17에서는 hard 4C 확정은 없다.

```text
hard_4c_confirmed = false
hard_4c_not_confirmed_reason = export controls and labor are severe overlays, but not yet confirmed thesis breaks with irreversible delivery failure or order cancellation.
```

Strong 4B:

```text
- U.S. China fab export-control revocation
- Samsung strike/labor-cost reset
- SK Hynix commodity memory price warning
- Samsung HBM share/yield catch-up risk
- Hanmi customer concentration / export-control sensitivity
```

---

# 15. production scoring 반영 여부

```text
production_scoring_changed = false
shadow_only = true
```

R2 production 설계 원칙:

```text
1. HBM 양산/인증/고객수요 trigger는 Stage2-Actionable 승격에 반영한다.
2. HBM4 인증은 Stage3-Yellow 후보로 별도 tier를 둔다.
3. LOI는 좋은 trigger지만 final order 전까지 Green 금지한다.
4. record earnings라도 price failed면 감점한다.
5. 장비주는 수주금액/반복수주/고객다변화 전까지 Green 금지한다.
6. China fab export control과 labor strike는 sector-wide 4B로 병기한다.
7. Samsung catch-up은 volume/yield before Green 원칙을 적용한다.
```

---

# 16. 레포 반영용 patch-ready 출력

## docs/round/round_251.md 요약

```md
# R2 Loop 17. AI / Semiconductor / Electronics Trigger-level Price Validation

이번 라운드는 R2 Loop 17 trigger-level validation 라운드다.

핵심 결론:
- SK Hynix HBM3E mass production is the cleanest Stage2-Actionable case. SK Hynix began mass production of 12-layer HBM3E chips; shares rose more than 9% while KOSPI rose 1.7%. The product offers 50% more capacity than prior eight-layer chips. Green requires customer volume, yield, ASP and margin.
- SK Hynix HBM4 certification is Stage3-Yellow candidate. It completed internal certification and established a production system; shares rose as much as 7.3% vs KOSPI +1.2%. Customer-specific base die increases lock-in, but customer volume/yield/margin are still gates.
- OpenAI Stargate memory LOI is Stage2-Actionable with LOI 4B. SK Hynix closed +10% and Samsung +3.5% after signing an LOI with OpenAI for the $500B Stargate project. SK Hynix cited demand of up to 900,000 DRAM wafers per month, more than 2x current HBM industry capacity.
- Samsung HBM catch-up is Stage2, not Green. Samsung plans HBM4 production for Nvidia supply; shares rose 2.2% while SK Hynix fell 2.9%. Samsung also signed an AMD MoU for HBM4/DDR5, but its HBM share trails SK Hynix and labor/yield gates remain.
- Hanmi Semiconductor is Stage2-Actionable HBM equipment chain. Hanmi rose 16% while SK Hynix rose 4.3% and KOSPI 0.7%. Hanmi supplies SK Hynix with TSV-TC bonders and had a KRW21.48B supply deal plus around KRW200B recent contract wins.
- SK Hynix record Q4 profit is evidence_good_but_price_failed. OP was KRW8.1T / $5.64B and HBM was 40% of DRAM revenue, but shares fell 4% due commodity memory price and China competition warnings.
- U.S. China fab export-control revocation is sector 4B. Samsung -2.3%, SK Hynix -4.4%, KOSPI -0.7%, Hana Micron -1.7%, Hanmi -4.4%. China fabs represent more than one-third of Samsung DRAM and 30~40% of SK Hynix DRAM/NAND output.
- Samsung labor strike risk is 4B. Shares fell 9.3% after strike-plan continuation; up to 48,000 workers and possible 4% DRAM / 3% NAND supply disruption were discussed.

Main calibration:
- Raise HBM_mass_production, HBM4_certification, customer_binding_demand, HBM_wafer_allocation, packaging_equipment_orders, market_relative_return, HBM_yield_margin, China_fab_license_risk, labor_supply_stability.
- Lower earnings_without_price_validation, LOI_without_final_order, HBM_catchup_without_volume, report_or_target_without_orders, commodity_memory_ignored, customer_concentration_ignored, export_control_ignored, labor_cost_reset_ignored.
```

## docs/checkpoints/checkpoint_28a_round251_r2_loop17.md 요약

```md
# Checkpoint 28A Round 251 R2 Loop 17 Trigger-level Calibration

## 반영 내용
- R2 Loop 17 trigger-level validation을 수행했다.
- SK Hynix HBM3E mass production, SK Hynix HBM4 certification, OpenAI Stargate memory LOI, Samsung HBM catch-up, Hanmi Semiconductor TC bonder equipment, SK Hynix record-profit price failure, U.S. China fab export controls, Samsung labor strike risk를 검토했다.
- full adjusted OHLC는 확보하지 못했으므로 Reuters / FT / WSJ / MarketWatch / AP reported event return과 event price anchor를 사용했다.
- MFE/MAE는 조작하지 않고 price_data_unavailable_after_deep_search로 분리했다.

## 핵심 보정
- HBM mass production and HBM4 certification can promote Stage2 to Stage2-Actionable / Yellow candidate.
- LOI is not final order; it remains 4B before binding customer volume.
- Record earnings are not enough if price reaction fails.
- Equipment-chain names require repeat orders, margin and customer diversification.
- Samsung catch-up requires volume/yield before Green.
- China fab export controls and Samsung labor disruption are sector-wide 4B overlays.
```

## data/e2r_case_library/cases_r2_loop17_round251.jsonl 초안

```jsonl
{"case_id":"r2_loop17_sk_hynix_hbm3e_mass_production","symbol":"000660","company_name":"SK Hynix","case_type":"Stage2_Actionable_HBM_first_mover","primary_archetype":"HBM_FIRST_MOVER_STAGE2_ACTIONABLE","best_trigger":"T1/T2","stage_candidate":"Stage2-Actionable","price_validation":{"trigger_date":"2024-09-26","event_return_pct":">9","kospi_same_context_pct":1.7,"product":"12-layer_HBM3E","capacity_uplift_vs_8_layer_pct":50,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_HBM_mass_production","notes":"HBM mass-production trigger had strong price reaction; Green requires customer volume, yield, ASP and margin."}
{"case_id":"r2_loop17_sk_hynix_hbm4_certification","symbol":"000660","company_name":"SK Hynix","case_type":"Stage3_Yellow_candidate_HBM4_certification","primary_archetype":"HBM4_CERTIFICATION_STAGE3_YELLOW_CANDIDATE","best_trigger":"T1/T3","stage_candidate":"Stage3-Yellow_candidate","price_validation":{"trigger_date":"2025-09-12","event_return_pct":7.3,"kospi_same_context_pct":1.2,"product":"12-layer_HBM4","expected_hbm_share_2026_context":"low_60pct_range","customer_specific_base_die":true,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage3_Yellow_candidate_HBM4_first_mover","notes":"HBM4 certification and customer-specific base die justify Yellow candidate, but volume/yield/margin are still gates."}
{"case_id":"r2_loop17_openai_stargate_memory_loi","symbol":"000660/005930","company_name":"SK Hynix / Samsung Electronics","case_type":"Stage2_Actionable_AI_memory_demand_shock_with_LOI_4B","primary_archetype":"OPENAI_STARGATE_MEMORY_DEMAND_STAGE2_ACTIONABLE","best_trigger":"T1/T3","stage_candidate":"Stage2-Actionable + 4B-watch","price_validation":{"trigger_date":"2025-10-02","project_value_context_usd_bn":500,"sk_hynix_intraday_return_pct":12,"sk_hynix_close_return_pct":10,"samsung_intraday_return_pct":5,"samsung_close_return_pct":3.5,"openai_dram_wafer_demand_per_month":900000,"demand_vs_current_hbm_capacity":">2x","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_demand_shock_with_4B","notes":"Stargate LOI validates HBM demand but remains non-final until binding orders/pricing/capacity allocation."}
{"case_id":"r2_loop17_samsung_hbm_catchup_nvidia_amd","symbol":"005930","company_name":"Samsung Electronics","case_type":"Stage2_HBM_catchup_with_labor_4B","primary_archetype":"SAMSUNG_HBM_CATCHUP_STAGE2_WITH_LABOR_4B","best_trigger":"T0/T3","stage_candidate":"Stage2 + 4B-watch","price_validation":{"nvidia_trigger_date":"2026-01-26","samsung_event_return_pct":2.2,"sk_hynix_same_context_return_pct":-2.9,"amd_mou_date":"2026-03-18","amd_product_context":"Instinct_MI455X_HBM4_and_EPYC_DDR5","samsung_hbm_share_context_pct":22,"sk_hynix_hbm_share_context_pct":57,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"Stage2_HBM_catchup_not_Green","notes":"Samsung catch-up is real but volume, yield, margin and labor-cost risks remain."}
{"case_id":"r2_loop17_hanmi_semiconductor_hbm_packaging","symbol":"042700","company_name":"Hanmi Semiconductor","case_type":"Stage2_Actionable_HBM_packaging_equipment","primary_archetype":"HBM_PACKAGING_EQUIPMENT_STAGE2_ACTIONABLE","best_trigger":"T0/T3","stage_candidate":"Stage2-Actionable + 4B-watch","price_validation":{"trigger_date":"2024-03-26","hanmi_event_return_pct":16,"sk_hynix_same_context_return_pct":4.3,"kospi_same_context_pct":0.7,"sk_hynix_supply_deal_krw_bn":21.48,"recent_contract_wins_context_krw_bn":200,"equipment":"TSV_TC_bonder_for_HBM_packaging","china_export_control_selloff_pct":-4.4,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"excellent_stage2_actionable_HBM_equipment_with_4B","notes":"Hanmi is a clean HBM equipment Stage2, but repeat orders, margin, customer concentration and export-control sensitivity remain gates."}
{"case_id":"r2_loop17_sk_hynix_record_profit_price_failed","symbol":"000660","company_name":"SK Hynix","case_type":"evidence_good_but_price_failed","primary_archetype":"MEMORY_EARNINGS_GOOD_BUT_PRICE_FAILED","best_trigger":"T0/T2","stage_candidate":"Stage2_only","price_validation":{"trigger_date":"2025-01-23","operating_profit_q4_2024_krw_trn":8.1,"operating_profit_q4_2024_usd_bn":5.64,"hbm_share_of_dram_revenue_pct":40,"hbm_sales_outlook":"double_this_year","event_return_pct":-4,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"evidence_good_but_price_failed","notes":"Record profit and HBM mix were strong, but price failed due commodity memory and China-competition warnings."}
{"case_id":"r2_loop17_us_export_control_china_fabs","symbol":"005930/000660/067310/042700","company_name":"Samsung Electronics / SK Hynix / Hana Micron / Hanmi Semiconductor","case_type":"4B_export_control_china_fab","primary_archetype":"CHINA_EXPORT_CONTROL_4B","best_trigger":"T0/T3","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2025-09-01","samsung_event_return_pct":-2.3,"sk_hynix_event_return_pct":-4.4,"kospi_same_context_pct":-0.7,"hana_micron_event_return_pct":-1.7,"hanmi_semiconductor_event_return_pct":-4.4,"samsung_china_dram_output_exposure":">1/3","sk_hynix_china_dram_nand_output_exposure_pct":"30-40","full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"export_control_4B_success","notes":"China fab license risk is a sector-wide 4B and hit both leaders and back-end/equipment names."}
{"case_id":"r2_loop17_samsung_labor_memory_supply_4b","symbol":"005930","company_name":"Samsung Electronics","case_type":"4B_labor_supply_disruption","primary_archetype":"LABOR_SUPPLY_DISRUPTION_4B","best_trigger":"T0/T3","stage_candidate":"4B-watch","price_validation":{"trigger_date":"2026-05-15","event_return_pct":-9.3,"planned_strike_days":18,"workers_context":"nearly_48000","possible_dram_supply_impact_pct":4,"possible_nand_supply_impact_pct":3,"court_injunction_essential_workers":true,"full_ohlc_status":"price_data_unavailable_after_deep_search"},"score_price_alignment":"labor_supply_4B_not_hard_4C","notes":"Strike risk matters for supply and labor cost, but essential-worker injunction and talks prevent hard 4C classification for now."}
```

## data/e2r_trigger_calibration/triggers_r2_loop17_round251.jsonl 초안

```jsonl
{"trigger_id":"r2l17_skh_hbm3e_T1","case_id":"r2_loop17_sk_hynix_hbm3e_mass_production","trigger_type":"Stage2-Actionable_HBM_mass_production","trigger_date":"2024-09-26","event_return_pct":">9","market_relative_pp":">7","trigger_outcome_label":"excellent_stage2_actionable_HBM_mass_production","promote_to":"Stage2-Actionable"}
{"trigger_id":"r2l17_skh_hbm4_T1","case_id":"r2_loop17_sk_hynix_hbm4_certification","trigger_type":"Stage3-Yellow_candidate_HBM4_certification","trigger_date":"2025-09-12","event_return_pct":7.3,"market_relative_pp":6.1,"trigger_outcome_label":"Stage3_Yellow_candidate_HBM4_first_mover","promote_to":"Stage3-Yellow_candidate"}
{"trigger_id":"r2l17_openai_stargate_T1","case_id":"r2_loop17_openai_stargate_memory_loi","trigger_type":"Stage2-Actionable_AI_memory_demand","trigger_date":"2025-10-02","event_return_pct":"SK_Hynix_close_+10_Samsung_close_+3.5","trigger_outcome_label":"excellent_stage2_actionable_demand_shock_with_LOI_4B","promote_to":"Stage2-Actionable+4B"}
{"trigger_id":"r2l17_samsung_hbm4_nvidia_T0","case_id":"r2_loop17_samsung_hbm_catchup_nvidia_amd","trigger_type":"Stage2_HBM_catchup","trigger_date":"2026-01-26","event_return_pct":2.2,"trigger_outcome_label":"Stage2_HBM_catchup_not_Green","promote_to":"Stage2"}
{"trigger_id":"r2l17_hanmi_hbm_equipment_T0","case_id":"r2_loop17_hanmi_semiconductor_hbm_packaging","trigger_type":"Stage2-Actionable_HBM_equipment","trigger_date":"2024-03-26","event_return_pct":16,"market_relative_pp":15.3,"trigger_outcome_label":"excellent_stage2_actionable_HBM_equipment","promote_to":"Stage2-Actionable"}
{"trigger_id":"r2l17_skh_record_profit_T0","case_id":"r2_loop17_sk_hynix_record_profit_price_failed","trigger_type":"evidence_good_but_price_failed","trigger_date":"2025-01-23","event_return_pct":-4,"trigger_outcome_label":"record_profit_price_failed","promote_to":"no_actionable"}
{"trigger_id":"r2l17_us_export_control_T0","case_id":"r2_loop17_us_export_control_china_fabs","trigger_type":"4B_export_control","trigger_date":"2025-09-01","event_return_pct":"Samsung_-2.3_SKH_-4.4_Hanmi_-4.4_Hana_-1.7","trigger_outcome_label":"export_control_4B_success","promote_to":"4B-watch"}
{"trigger_id":"r2l17_samsung_labor_T0","case_id":"r2_loop17_samsung_labor_memory_supply_4b","trigger_type":"4B_labor_supply_disruption","trigger_date":"2026-05-15","event_return_pct":-9.3,"trigger_outcome_label":"labor_supply_4B_not_hard_4C","promote_to":"4B-watch"}
```

## data/sector_taxonomy/score_weight_profiles_round251_r2_loop17_v1.csv 초안

```csv
archetype,hbm_mass_production,hbm4_certification,customer_binding_demand,hbm_wafer_allocation,packaging_equipment_orders,market_relative_return,hbm_yield_margin,china_fab_license_risk,labor_supply_stability,earnings_without_price_validation_penalty,loi_without_final_order_penalty,hbm_catchup_without_volume_penalty,commodity_memory_ignored_penalty,stage2_actionable_promote,stage3_yellow_gate,stage3_green_gate,notes
HBM_FIRST_MOVER_STAGE2_ACTIONABLE,+5,+2,+4,+4,+1,+5,+5,+2,+1,-2,-1,-1,-3,HBM3E mass production with +9% reaction,customer volume/yield missing,customer volume+yield+margin,SK Hynix HBM3E.
HBM4_CERTIFICATION_STAGE3_YELLOW_CANDIDATE,+4,+5,+4,+4,+1,+5,+5,+2,+1,-2,-1,-1,-3,HBM4 certification and +7.3% reaction,volume/yield/margin missing,confirmed volume+margin,SK Hynix HBM4.
OPENAI_STARGATE_MEMORY_DEMAND_STAGE2_ACTIONABLE,+4,+3,+5,+5,+1,+4,+4,+1,+1,-1,-4,-1,-2,OpenAI wafer demand shock,LOI not final,final order+wafer allocation+pricing,OpenAI/SK/Samsung.
SAMSUNG_HBM_CATCHUP_STAGE2_WITH_LABOR_4B,+3,+4,+4,+3,+0,+2,+5,+2,+5,-1,-1,-5,-3,Samsung HBM4 catch-up,volume/yield/labor missing,Nvidia/AMD volume+yield,Samsung.
HBM_PACKAGING_EQUIPMENT_STAGE2_ACTIONABLE,+3,+2,+3,+3,+5,+5,+4,+3,+1,-1,-1,-2,-2,Hanmi TC bonder +16%,repeat order/customer diversification missing,repeat orders+margin+diversification,Hanmi.
MEMORY_EARNINGS_GOOD_BUT_PRICE_FAILED,+3,+2,+3,+2,+0,-5,+4,+3,+1,-5,-1,-1,-5,record profit but shares -4,actionable prohibited,price recovery+commodity stabilization,SK Hynix Q4.
CHINA_EXPORT_CONTROL_4B,+0,+0,+0,+0,+1,-5,+1,+5,+1,-1,-1,-1,-2,VEU revocation hit Samsung/SKH/Hanmi/Hana,license stability missing,annual license stability+capex workaround,China fab risk.
LABOR_SUPPLY_DISRUPTION_4B,+0,+0,+0,+0,+0,-4,+2,+0,+5,-1,-1,-2,-1,Samsung strike risk -9.3,supply disruption not hard 4C yet,labor deal+essential operations,Samsung labor.
```

---

# 이번 R2 Loop 17 결론

```text
1. SK Hynix HBM3E mass production은 R2의 가장 좋은 Stage2-Actionable이다.
   +9% 이상, KOSPI +1.7%, 12-layer HBM3E 양산이 닫혔다.

2. SK Hynix HBM4 certification은 Stage3-Yellow 후보다.
   +7.3%, KOSPI +1.2%, customer-specific base die 구조가 lock-in을 만든다.

3. OpenAI Stargate LOI는 Stage2-Actionable demand shock다.
   SK +10%, Samsung +3.5%, 900,000 DRAM wafers/month demand context가 강하다. 단, LOI라 4B다.

4. Samsung HBM catch-up은 Stage2다.
   HBM4 Nvidia/AMD route는 긍정적이지만 volume/yield/share gap/labor gate가 남았다.

5. Hanmi Semiconductor는 Stage2-Actionable HBM equipment chain이다.
   +16%, SK Hynix supply deal, TSV-TC bonder evidence가 닫혔다.

6. SK Hynix record profit은 evidence_good_but_price_failed다.
   OP KRW8.1T, HBM 40% DRAM revenue였지만 주가 -4%면 Green 금지다.

7. U.S. China fab export-control revocation은 sector-wide 4B다.
   Samsung -2.3%, SKH -4.4%, Hanmi -4.4%, Hana Micron -1.7%가 같이 맞았다.

8. Samsung labor strike risk는 labor/supply 4B다.
   -9.3% price reaction과 DRAM/NAND supply impact 가능성은 크지만, hard 4C는 아직 아니다.
```

한 문장으로 압축하면:

> **R2 Loop 17에서 배운 핵심은 “AI 반도체”라는 테마명이 아니라, HBM 양산·HBM4 인증·고객 wafer demand·TC bonder 반복수주·yield/margin이 닫힌 trigger만 Stage2-Actionable/Yellow로 올려야 한다는 것이다. 반대로 record earnings라도 주가가 빠지거나, LOI·catch-up·리포트·수출통제·노동 리스크가 남아 있으면 Green은 금지다.**

다음 순서는 **R3 Loop 17 — 2차전지·전기차·친환경**이다.

[1]: https://www.reuters.com/technology/nvidia-supplier-sk-hynix-says-begins-mass-production-12-layer-hbm3e-chips-2024-09-26/?utm_source=chatgpt.com "Nvidia supplier SK Hynix's shares rally as mass production of latest HBM chips begins"
[2]: https://www.reuters.com/world/sk-hynix-says-readying-hbm4-production-after-completing-internal-certification-2025-09-12/?utm_source=chatgpt.com "SK Hynix says readying HBM4 production after completing internal certification"
[3]: https://www.ft.com/content/52193ddd-bb37-427a-94b2-197af50d1ee4?utm_source=chatgpt.com "SK Hynix and Samsung shares leap after OpenAI deal"
[4]: https://www.reuters.com/world/asia-pacific/samsung-start-production-hbm4-chips-next-month-nvidia-supply-source-says-2026-01-25/?utm_source=chatgpt.com "Samsung to start production of HBM4 chips next month for Nvidia supply, source says"
[5]: https://www.wsj.com/articles/south-korean-chip-shares-rally-as-ai-frenzy-persists-260f9996?utm_source=chatgpt.com "South Korean Chip Shares Rally as AI Frenzy Persists"
[6]: https://www.reuters.com/technology/nvidia-supplier-sk-hynix-posts-record-quarterly-profit-2025-01-22/?utm_source=chatgpt.com "SK Hynix posts record quarterly profit surpassing Samsung on AI boom"
[7]: https://www.reuters.com/world/china/shares-samsung-sk-hynix-drop-after-us-makes-it-harder-make-chips-china-2025-09-01/?utm_source=chatgpt.com "Shares in Samsung, SK Hynix drop after US makes it harder to make chips in China"
[8]: https://www.reuters.com/business/world-at-work/samsung-elecs-union-says-samsung-proposed-unconditional-talks-strike-plan-holds-2026-05-15/?utm_source=chatgpt.com "Samsung's South Korean union sticks to strike plan after talks offer; shares slide"
